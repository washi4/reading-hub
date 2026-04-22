---
name: youtube-clipper
description: >
  Minimal YouTube download + subtitle utilities used by the post-creator skill.
  Downloads videos and VTT subtitles via yt-dlp, and converts auto-generated
  VTT captions into sentence-level SRT suitable for shadow reading or article
  rewriting. Trigger when another skill needs to fetch a YouTube video or
  flatten its captions into readable sentences.
---

# YouTube Clipper (minimal)

This is a trimmed-down version of the upstream
[youtube-clipper skill](https://github.com/op7418/Youtube-clipper-skill),
kept only for the scripts that the `post-creator` skill depends on.

## Requirements

- Python 3.8+
- `pip install yt-dlp`
- `ffmpeg` on PATH (on macOS: `brew install ffmpeg`; for subtitle burning you
  would need `ffmpeg-full`, but this trimmed version doesn't do burning)

## Scripts

All scripts live in `scripts/`. Invoke them with `python3` from any working
directory — they use `pathlib` and resolve paths relative to their arguments.

| Script | Purpose |
|---|---|
| `scripts/download_video.py` | Download a YouTube video (≤1080p) plus English VTT subtitles into `<output_dir>/<videoId>/`. |
| `scripts/vtt_to_shadow_srt.py` | Convert an auto-generated YouTube VTT file into a sentence-level SRT, deduplicating the progressive-display repetitions. |
| `scripts/dedupe_rolling_captions.py` | Clean up rolling-caption repeats left in already-flattened transcripts (each frame repeating part of the previous). Run after flattening SRT → plain text. |
| `scripts/utils.py` | Shared helpers (URL validation, filename sanitising, directory creation). Imported by `download_video.py`. |

### Usage

```bash
# Download video + subtitles
python3 scripts/download_video.py <youtube_url> [output_dir]

# Convert VTT captions to sentence-level SRT
python3 scripts/vtt_to_shadow_srt.py <input.vtt> <output.srt> \
  [--max-duration 8] [--min-duration 1.5]

# Clean up rolling-caption repeats in flattened plain text
python3 scripts/dedupe_rolling_captions.py <input.txt> <output.txt>
# Or use with stdin: cat transcript.txt | python3 scripts/dedupe_rolling_captions.py -
```

### Known caveats

- **YouTube 403 errors:** pass `--cookies-from-browser chrome` by editing
  `download_video.py` or calling `yt_dlp` directly. The script accepts a
  `cookies_from_browser` kwarg.
- **VTT format detection:** `vtt_to_shadow_srt.py` auto-detects `<c>` (auto
  captions) vs `<b>` (manual uploads). Other formats may need cleanup first.

## Scope

This skill intentionally does **not** include: video clipping, subtitle burning,
translation, or bilingual subtitle generation. If those are needed later, pull
the relevant scripts back in from the upstream project.
