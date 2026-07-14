---
name: youtube-clipper
description: >
  Minimal YouTube download + subtitle utilities used by the post-creator skill.
  Downloads videos and VTT subtitles via yt-dlp, and converts auto-generated
  VTT captions into sentence-level SRT suitable for shadow reading or
  downstream transcript processing. Trigger when another skill needs to fetch a
  YouTube video or flatten its captions into readable sentences.
---

# YouTube Clipper (minimal)

This is a trimmed-down version of the upstream
[youtube-clipper skill](https://github.com/op7418/Youtube-clipper-skill),
kept only for the scripts that the `post-creator` skill depends on.

## Transcript Contract

The output is source material for a native-English transcript, not a summary.
Remove caption-format artifacts and progressive-display repeats only. Preserve
wording and order; retain uncertain wording rather than guessing a correction.
If English captions cannot be downloaded or converted, report the failure and
do not substitute video metadata or generated prose.

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

# Produce a sentence-level transcript source.
python3 scripts/vtt_to_shadow_srt.py <input.vtt> <output.srt> \
  [--max-duration 8] [--min-duration 1.5]

# Remove rolling display repetition from flattened transcript text.
python3 scripts/dedupe_rolling_captions.py <input.txt> <output.txt>
# Or use with stdin: cat transcript.txt | python3 scripts/dedupe_rolling_captions.py -
```

A repeated rolling-caption sequence such as `we can we can build` must become
`we can build`; a non-repeated spoken phrase must remain unchanged.

### Known caveats

- **YouTube 403 errors:** pass `--cookies-from-browser chrome` by editing
  `download_video.py` or calling `yt_dlp` directly. The script accepts a
  `cookies_from_browser` kwarg.
- **VTT format detection:** `vtt_to_shadow_srt.py` auto-detects `<c>` (auto
  captions) vs `<b>` (manual uploads). Other formats may need cleanup first.

## Scope

This skill intentionally does **not** include: video clipping, subtitle burning,
post creation, translation, summary generation, or bilingual subtitle
generation. It only covers caption acquisition and faithful subtitle
normalization. If those are needed later, pull the relevant scripts back in
from the upstream project.
