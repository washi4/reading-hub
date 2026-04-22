#!/usr/bin/env python3
"""
下载 YouTube 视频和字幕
使用 yt-dlp 下载视频（最高 1080p）和英文字幕
"""

import sys
import json
from pathlib import Path

try:
    import yt_dlp
except ImportError:
    print("❌ Error: yt-dlp not installed")
    print("Please install: pip install yt-dlp")
    sys.exit(1)

from utils import (
    validate_url,
    sanitize_filename,
    format_file_size,
    get_video_duration_display,
    ensure_directory
)


def download_video(url: str, output_dir: str = None, cookies_from_browser: str = None) -> dict:
    """
    下载 YouTube 视频和字幕

    Args:
        url: YouTube URL
        output_dir: 输出目录，默认为当前目录
        cookies_from_browser: 浏览器名称，用于提取 cookies（解决 403 错误）

    Returns:
        dict: {
            'video_path': 视频文件路径,
            'subtitle_path': 字幕文件路径,
            'title': 视频标题,
            'duration': 视频时长（秒）,
            'file_size': 文件大小（字节）,
            'video_id': 视频ID,
            'video_dir': 视频专属目录
        }

    Raises:
        ValueError: 无效的 URL
        Exception: 下载失败
    """
    # 验证 URL
    if not validate_url(url):
        raise ValueError(f"Invalid YouTube URL: {url}")

    # 设置输出目录
    if output_dir is None:
        output_dir = Path.cwd()
    else:
        output_dir = Path(output_dir)

    output_dir = ensure_directory(output_dir)

    print(f"🎬 开始下载视频...")
    print(f"   URL: {url}")
    if cookies_from_browser:
        print(f"   Cookies: 从 {cookies_from_browser} 浏览器提取")

    # 配置 yt-dlp 选项（合并元数据获取和下载，避免重复 API 调用）
    meta_opts = {'quiet': True}
    if cookies_from_browser:
        meta_opts['cookiesfrombrowser'] = (cookies_from_browser,)
    
    with yt_dlp.YoutubeDL(meta_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        video_id = info.get('id', 'unknown')
        title = info.get('title', 'Unknown')
        duration = info.get('duration', 0)

    # 创建视频专属目录（按 video_id）
    video_dir = output_dir / video_id
    video_dir = ensure_directory(video_dir)

    print(f"   视频ID: {video_id}")
    print(f"   输出目录: {video_dir}")

    # 配置 yt-dlp 选项
    ydl_opts = {
        # 视频格式：最高 1080p，优先 mp4
        'format': 'bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[height<=1080][ext=mp4]/best',

        # 输出模板：放在视频专属目录下
        'outtmpl': str(video_dir / '%(id)s.%(ext)s'),

        # 下载字幕
        'writesubtitles': True,
        'writeautomaticsub': True,  # 自动字幕作为备选
        'subtitleslangs': ['en'],   # 英文字幕
        'subtitlesformat': 'vtt',   # VTT 格式

        # 不下载缩略图
        'writethumbnail': False,

        # 静默模式（减少输出）
        'quiet': False,
        'no_warnings': False,

        # 重试逻辑（提高下载可靠性）
        'retries': 3,
        'fragment_retries': 5,
        'socket_timeout': 30,

        # 进度钩子
        'progress_hooks': [_progress_hook],
    }

    # 添加 cookies 支持（解决 YouTube 403 错误）
    if cookies_from_browser:
        ydl_opts['cookiesfrombrowser'] = (cookies_from_browser,)

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"\n📊 视频信息:")
            print(f"   标题: {title}")
            print(f"   时长: {get_video_duration_display(duration)}")

            # 下载视频
            print(f"\n📥 开始下载...")
            info = ydl.extract_info(url, download=True)

            # 获取下载的文件路径
            video_filename = ydl.prepare_filename(info)
            video_path = Path(video_filename)

            # 查找字幕文件（使用 glob 更可靠）
            subtitle_path = None
            vtt_files = list(video_path.parent.glob(f"{video_id}*.vtt"))
            if vtt_files:
                # 优先选择 .en.vtt
                en_vtts = [f for f in vtt_files if '.en.' in f.name]
                subtitle_path = en_vtts[0] if en_vtts else vtt_files[0]

            # 获取文件大小
            file_size = video_path.stat().st_size if video_path.exists() else 0

            # 验证下载结果
            if not video_path.exists():
                raise Exception("Video file not found after download")

            print(f"\n✅ 视频下载完成: {video_path.name}")
            print(f"   大小: {format_file_size(file_size)}")

            if subtitle_path and subtitle_path.exists():
                print(f"✅ 字幕下载完成: {subtitle_path.name}")
            else:
                print(f"⚠️  未找到英文字幕")
                print(f"   提示：某些视频可能没有字幕或需要自动生成")

            print(f"\n📁 输出目录: {video_dir}")

            return {
                'video_path': str(video_path),
                'subtitle_path': str(subtitle_path) if subtitle_path else None,
                'title': title,
                'duration': duration,
                'file_size': file_size,
                'video_id': video_id,
                'video_dir': str(video_dir)
            }

    except Exception as e:
        print(f"\n❌ 下载失败: {str(e)}")
        raise


def _progress_hook(d):
    """下载进度回调"""
    if d['status'] == 'downloading':
        # 显示下载进度
        if 'downloaded_bytes' in d and 'total_bytes' in d and d['total_bytes']:
            percent = d['downloaded_bytes'] / d['total_bytes'] * 100
            downloaded = format_file_size(d['downloaded_bytes'])
            total = format_file_size(d['total_bytes'])
            speed = d.get('speed') or 0
            speed_str = format_file_size(speed) + '/s' if speed else 'N/A'

            # 使用 \r 实现进度条覆盖
            bar_length = 30
            filled = int(bar_length * percent / 100)
            bar = '█' * filled + '░' * (bar_length - filled)

            print(f"\r   [{bar}] {percent:.1f}% - {downloaded}/{total} - {speed_str}", end='', flush=True)
        elif 'downloaded_bytes' in d:
            # 无总大小信息时，只显示已下载
            downloaded = format_file_size(d['downloaded_bytes'])
            speed = d.get('speed', 0)
            speed_str = format_file_size(speed) + '/s' if speed else 'N/A'
            print(f"\r   下载中... {downloaded} - {speed_str}", end='', flush=True)

    elif d['status'] == 'finished':
        print()  # 换行


def main():
    """命令行入口"""
    if len(sys.argv) < 2:
        print("Usage: python download_video.py <youtube_url> [output_dir] [--cookies-from-browser BROWSER]")
        print("\nExample:")
        print("  python download_video.py https://youtube.com/watch?v=Ckt1cj0xjRM")
        print("  python download_video.py https://youtube.com/watch?v=Ckt1cj0xjRM ~/Downloads")
        print("  python download_video.py https://youtube.com/watch?v=Ckt1cj0xjRM --cookies-from-browser chrome")
        print("\n如果遇到 403 错误，请使用 --cookies-from-browser chrome 参数")
        sys.exit(1)

    url = sys.argv[1]
    output_dir = None
    cookies_from_browser = None
    
    # 解析参数
    i = 2
    while i < len(sys.argv):
        if sys.argv[i] == '--cookies-from-browser' and i + 1 < len(sys.argv):
            cookies_from_browser = sys.argv[i + 1]
            i += 2
        elif output_dir is None and not sys.argv[i].startswith('--'):
            output_dir = sys.argv[i]
            i += 1
        else:
            i += 1

    try:
        result = download_video(url, output_dir, cookies_from_browser=cookies_from_browser)

        # 输出 JSON 结果（供其他脚本使用）
        print("\n" + "="*60)
        print("下载结果 (JSON):")
        print(json.dumps(result, indent=2, ensure_ascii=False))

    except Exception as e:
        print(f"\n❌ 错误: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
