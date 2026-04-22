#!/usr/bin/env python3
"""
影子跟读字幕处理工具
========================
将 YouTube VTT 字幕转换为逐句分割的 SRT，适合影子跟读练习

功能特点:
- 自动检测 VTT 格式（<c> 自动生成 / <b> 手动上传）
- 连续重复块去重（解决 YouTube 逐行展开式重复）
- 智能分句：按标点 + 停顿合并片段为完整自然句
- 过长句子自动在合理位置分割
- 过短句子自动与相邻句合并
- 支持配置最大/最小句子时长

用法:
    python vtt_to_shadow_srt.py <input.vtt> <output.srt> [--max-duration N] [--min-duration N]

参数:
    input.vtt        YouTube VTT 字幕文件
    output.srt       输出的 SRT 字幕文件
    --max-duration   单句最大时长（秒），默认 8
    --min-duration   单句最小时长（秒），默认 1.5

示例:
    python vtt_to_shadow_srt.py video.en.vtt video_shadow.srt
    python vtt_to_shadow_srt.py video.en.vtt video_shadow.srt --max-duration 6 --min-duration 2
"""

import re
import sys
import html
from pathlib import Path


def parse_time(time_str):
    """解析时间字符串为秒数"""
    time_str = time_str.strip().replace(',', '.')
    parts = time_str.split(':')
    if len(parts) == 3:
        h, m, s = parts
        return float(h) * 3600 + float(m) * 60 + float(s)
    elif len(parts) == 2:
        m, s = parts
        return float(m) * 60 + float(s)
    return 0


def format_srt_time(seconds):
    """秒数转换为 SRT 时间格式 (HH:MM:SS,mmm)"""
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = seconds % 60
    return f"{h:02d}:{m:02d}:{s:06.3f}".replace('.', ',')


def clean_text(text):
    """清理字幕文本中的 HTML 标记和格式"""
    # 移除所有 HTML/VTT 标签 (<b>, <c>, <i>, 等)
    text = re.sub(r'<[^>]+>', '', text)
    # 解码 HTML 实体
    text = html.unescape(text)
    # 移除 >> 说话人切换标记
    text = re.sub(r'>>\s*', '', text)
    # 移除多余空格
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def detect_vtt_format(content):
    """
    检测 VTT 文件格式

    Returns:
        'auto_generated' - YouTube 自动生成字幕 (含 <c> 单词级时间戳)
        'manual' - 手动上传字幕 (含 <b> 标签或纯文本，无单词级时间戳)
    """
    if '<c>' in content and re.search(r'<\d{2}:\d{2}:\d{2}\.\d{3}>', content):
        return 'auto_generated'
    return 'manual'


def parse_vtt_blocks(content):
    """
    解析 VTT 文件为块列表

    跳过 VTT 头部、序号行，提取每个时间戳块的文本

    Returns:
        list of {start: float, end: float, text: str}
    """
    blocks = []
    lines = content.split('\n')
    current_start = None
    current_end = None
    current_lines = []

    for line in lines:
        line_stripped = line.strip()

        # 跳过 VTT 头部
        if line_stripped.startswith('WEBVTT') or \
           line_stripped.startswith('Kind:') or \
           line_stripped.startswith('Language:'):
            continue

        # 跳过纯数字序号行
        if re.match(r'^\d+$', line_stripped):
            continue

        if '-->' in line_stripped:
            # 保存上一个块
            if current_start is not None and current_lines:
                text = ' '.join(current_lines)
                text = clean_text(text)
                if text:
                    blocks.append({
                        'start': current_start,
                        'end': current_end,
                        'text': text
                    })

            # 解析新时间戳
            parts = line_stripped.split('-->')
            current_start = parse_time(parts[0].strip())
            # 去掉 position/alignment 等属性，只取时间部分
            end_part = parts[1].strip().split()[0]
            current_end = parse_time(end_part)
            current_lines = []
        elif line_stripped and current_start is not None:
            current_lines.append(line_stripped)

    # 最后一个块
    if current_start is not None and current_lines:
        text = ' '.join(current_lines)
        text = clean_text(text)
        if text:
            blocks.append({
                'start': current_start,
                'end': current_end,
                'text': text
            })

    return blocks


def dedup_consecutive(blocks):
    """
    连续重复块去重

    YouTube 手动上传字幕常见"逐行展开"模式：同一句话在连续 3-5 个块中
    重复出现，每块时间范围递进。去重后只保留一个条目，取第一次出现的
    start 和最后一次出现的 end。

    示例:
        输入:  5 个块都是 "The screen door keeps bugs outside."
        输出:  1 个块 "The screen door keeps bugs outside." (合并时间)
    """
    if not blocks:
        return []

    deduped = []
    current = blocks[0].copy()

    for block in blocks[1:]:
        if block['text'] == current['text']:
            # 相同文本，扩展时间范围
            current['end'] = max(current['end'], block['end'])
        else:
            deduped.append(current)
            current = block.copy()

    deduped.append(current)
    return deduped


def merge_to_sentences(blocks, pause_threshold=0.5, min_duration=1.5, max_duration=8.0):
    """
    将片段合并为完整自然句

    策略（按优先级）:
    1. 当前片段以句末标点 (.?!) 结尾 + 有间隔 → 新句子
    2. 间隔 > pause_threshold → 新句子
    3. 合并后会超过 max_duration + 当前已足够长 → 新句子
    4. 当前已超过 max_duration，在从句标点处分割
    5. 超过 max_duration * 1.2，激进分割
    6. 硬上限 max_duration * 1.5，无条件分割

    Args:
        blocks: 去重后的字幕块列表
        pause_threshold: 停顿阈值（秒），大于此值视为句子边界
        min_duration: 最小句子时长（秒）
        max_duration: 最大句子时长（秒）
    """
    if not blocks:
        return []

    sentences = []
    current = blocks[0].copy()

    sentence_end_chars = set('.?!。？！')
    clause_chars = set(',;:，；：')

    for block in blocks[1:]:
        gap = block['start'] - current['end']
        current_text = current['text'].strip()
        current_duration = current['end'] - current['start']
        would_be_duration = block['end'] - current['start']

        should_split = False

        # 条件1: 当前以句末标点结尾 + 有间隔
        if current_text and current_text[-1] in sentence_end_chars:
            if gap > 0.15 or current_duration >= min_duration:
                should_split = True

        # 条件2: 停顿超过阈值
        if gap > pause_threshold:
            should_split = True

        # 条件3: 合并后会超过 max_duration，且当前已有足够时长
        if would_be_duration > max_duration and current_duration >= min_duration:
            should_split = True

        # 条件4: 当前已超过 max_duration，在从句标点处分割
        if current_duration > max_duration:
            if current_text and current_text[-1] in clause_chars and gap > 0.1:
                should_split = True
            elif gap > 0.1:
                should_split = True

        # 条件5: 超长句子，激进分割
        if current_duration > max_duration * 1.2 and gap > 0.05:
            should_split = True

        # 条件6: 硬上限，无条件分割
        if current_duration > max_duration * 1.5:
            should_split = True

        if should_split:
            sentences.append(current)
            current = block.copy()
        else:
            # 合并到当前句子
            current['text'] = current['text'] + ' ' + block['text']
            current['end'] = block['end']

    sentences.append(current)
    return sentences


def merge_short_sentences(sentences, min_duration=1.5, max_duration=8.0):
    """
    合并过短的句子到相邻句子

    如果一个句子 < min_duration 秒，尝试:
    1. 向后合并（如果合并后不超过 max_duration）
    2. 向前合并（如果向后不行）
    3. 保留原样（如果都不行）
    """
    if len(sentences) <= 1:
        return sentences

    merged = []
    i = 0
    while i < len(sentences):
        s = sentences[i].copy()
        duration = s['end'] - s['start']

        # 如果过短，尝试向后合并
        if duration < min_duration and i + 1 < len(sentences):
            next_s = sentences[i + 1]
            combined_duration = next_s['end'] - s['start']
            if combined_duration <= max_duration:
                s['text'] = s['text'] + ' ' + next_s['text']
                s['end'] = next_s['end']
                i += 2
                merged.append(s)
                continue

        # 如果过短且无法向后合并，尝试向前合并
        if duration < min_duration and merged:
            prev = merged[-1]
            combined_duration = s['end'] - prev['start']
            if combined_duration <= max_duration:
                prev['text'] = prev['text'] + ' ' + s['text']
                prev['end'] = s['end']
                i += 1
                continue

        merged.append(s)
        i += 1

    return merged


def write_srt(sentences, output_path):
    """输出为 SRT 格式"""
    with open(output_path, 'w', encoding='utf-8') as f:
        for i, entry in enumerate(sentences, 1):
            start = format_srt_time(entry['start'])
            end = format_srt_time(entry['end'])
            f.write(f"{i}\n")
            f.write(f"{start} --> {end}\n")
            f.write(f"{entry['text']}\n\n")


def process_manual_vtt(content, max_duration=8.0, min_duration=1.5):
    """
    处理手动上传的 VTT 字幕（<b> 标签或纯文本格式）

    流程: 解析 VTT 块 → 连续去重 → 合并为自然句 → 合并过短句

    Args:
        content: VTT 文件内容
        max_duration: 单句最大时长
        min_duration: 单句最小时长

    Returns:
        list of {start, end, text}
    """
    # Step 1: 解析 VTT 块
    blocks = parse_vtt_blocks(content)
    print(f"   VTT 块: {len(blocks)}")

    # Step 2: 连续重复去重
    deduped = dedup_consecutive(blocks)
    removed = len(blocks) - len(deduped)
    print(f"   去重后: {len(deduped)} (移除 {removed} 个重复块)")

    # Step 3: 合并为自然句
    sentences = merge_to_sentences(
        deduped,
        pause_threshold=0.5,
        min_duration=min_duration,
        max_duration=max_duration
    )
    print(f"   合并为句子: {len(sentences)}")

    # Step 4: 合并过短句子
    before_merge = len(sentences)
    sentences = merge_short_sentences(
        sentences,
        min_duration=min_duration,
        max_duration=max_duration
    )
    if len(sentences) < before_merge:
        print(f"   合并短句后: {len(sentences)} (合并了 {before_merge - len(sentences)} 个短句)")

    return sentences


def process_vtt(vtt_path, output_path, max_duration=8.0, min_duration=1.5):
    """
    处理 VTT 文件，自动检测格式并转换为逐句 SRT

    自动检测 VTT 格式:
    - <c> 标签 (自动生成字幕) → 使用 extract_precise_subtitles 的精确处理
    - <b> 标签/纯文本 (手动上传) → 使用去重 + 合并逻辑

    Args:
        vtt_path: 输入 VTT 文件路径
        output_path: 输出 SRT 文件路径
        max_duration: 单句最大时长（秒）
        min_duration: 单句最小时长（秒）

    Returns:
        sentences: 处理后的句子列表 [{start, end, text}, ...]
    """
    print(f"📝 影子跟读字幕处理...")
    print(f"   输入: {vtt_path}")

    with open(vtt_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 检测格式
    fmt = detect_vtt_format(content)
    print(f"   格式: {'自动生成 (<c> 标签)' if fmt == 'auto_generated' else '手动上传 (<b>/纯文本)'}")

    if fmt == 'auto_generated':
        # 使用 extract_precise_subtitles.py 的精确处理逻辑
        try:
            script_dir = Path(__file__).parent
            if str(script_dir) not in sys.path:
                sys.path.insert(0, str(script_dir))
            from extract_precise_subtitles import process_vtt as process_precise
            print(f"   使用精确时间戳处理引擎...")
            sentences = process_precise(vtt_path, output_path, max_duration=max_duration)
            return sentences
        except ImportError:
            print("   ⚠️  无法导入 extract_precise_subtitles，回退到通用处理")
            sentences = process_manual_vtt(content, max_duration, min_duration)
    else:
        sentences = process_manual_vtt(content, max_duration, min_duration)

    # 输出 SRT
    write_srt(sentences, output_path)

    # 统计信息
    print(f"\n✅ 处理完成")
    print(f"   输出: {output_path}")
    print(f"   句子数: {len(sentences)}")

    durations = [s['end'] - s['start'] for s in sentences]
    if durations:
        avg_dur = sum(durations) / len(durations)
        over_max = sum(1 for d in durations if d > max_duration)
        under_min = sum(1 for d in durations if d < min_duration)
        print(f"\n📊 时长统计:")
        print(f"   最短: {min(durations):.1f}s | 平均: {avg_dur:.1f}s | 最长: {max(durations):.1f}s")
        print(f"   目标范围: {min_duration}s ~ {max_duration}s")
        if over_max > 0:
            print(f"   ⚠️  {over_max} 条超过上限")
        if under_min > 0:
            print(f"   ⚠️  {under_min} 条低于下限")
        if over_max == 0 and under_min == 0:
            print(f"   ✅ 所有句子在目标范围内")

    # 预览前 15 条
    print(f"\n📋 前 15 条预览:")
    for i, s in enumerate(sentences[:15], 1):
        d = s['end'] - s['start']
        text = s['text'][:65] + ('...' if len(s['text']) > 65 else '')
        warn = ' ⚠️' if d > max_duration or d < min_duration else ''
        print(f"   {i:3d}. [{format_srt_time(s['start'])[:8]}→{format_srt_time(s['end'])[:8]}] ({d:.1f}s){warn} {text}")

    return sentences


def main():
    if len(sys.argv) < 3:
        print("影子跟读字幕处理工具")
        print("=" * 40)
        print()
        print("将 YouTube VTT 字幕转换为逐句 SRT，适合影子跟读练习")
        print()
        print("用法: python vtt_to_shadow_srt.py <input.vtt> <output.srt> [options]")
        print()
        print("选项:")
        print("  --max-duration N  单句最大时长，默认 8 秒")
        print("  --min-duration N  单句最小时长，默认 1.5 秒")
        print()
        print("示例:")
        print("  python vtt_to_shadow_srt.py video.en.vtt video_shadow.srt")
        print("  python vtt_to_shadow_srt.py video.en.vtt video_shadow.srt --max-duration 6")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    # 解析可选参数
    max_duration = 8.0
    min_duration = 1.5

    for i, arg in enumerate(sys.argv):
        if arg == '--max-duration' and i + 1 < len(sys.argv):
            try:
                max_duration = float(sys.argv[i + 1])
            except ValueError:
                print(f"⚠️  无效的 --max-duration 值，使用默认 {max_duration}")
        if arg == '--min-duration' and i + 1 < len(sys.argv):
            try:
                min_duration = float(sys.argv[i + 1])
            except ValueError:
                print(f"⚠️  无效的 --min-duration 值，使用默认 {min_duration}")

    if not Path(input_path).exists():
        print(f"❌ 文件不存在: {input_path}")
        sys.exit(1)

    process_vtt(input_path, output_path, max_duration=max_duration, min_duration=min_duration)


if __name__ == '__main__':
    main()
