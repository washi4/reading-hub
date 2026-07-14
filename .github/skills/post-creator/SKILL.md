---
name: post-creator
description: >
  Create reading-hub posts from YouTube videos, web article URLs, pasted text,
  existing markdown, or user drafts. Use when the user wants to add/archive/save
  content as a reading-friendly article, says "turn this into a post", "发到
  reading-hub", "转成朗读文章", "加一篇文章", or provides a source and asks for a
  reading post. Writes `src/content/posts/<slug>.md` with Astro-valid
  frontmatter and source-faithful body content.
allowed-tools:
  - Read
  - Write
  - Bash
  - Glob
  - AskUserQuestion
---

# Reading Hub Post Creator

Create one Astro content post at `src/content/posts/<slug>.md`. The post must parse, preserve the source's substance, and keep the source's English voice. For YouTube, the cleaned subtitle transcript is the sole authority for the body.

## Steps

1. **Classify source.** Identify exactly one branch: YouTube, web article URL, raw text/existing markdown, or user draft. Ask only for a missing title or source needed to proceed. Completion criterion: branch, title basis, and source URL/file/text are known.
2. **Build clean body.** Convert source to markdown using the branch rules below. Completion criterion: body has no extraction artifacts and preserves the source's substantive content and voice.
3. **Prepare frontmatter.** Use today's date from `date +%Y-%m-%d`, a valid slug, and only fields supported by `src/content.config.ts`. Completion criterion: frontmatter is YAML-safe, has `title`, and `tags` is a YAML list.
4. **Write post.** Save only under `src/content/posts/<slug>.md`; if the file exists, ask before overwriting. Completion criterion: file exists at that path and no unrelated files were changed.
5. **Run chunk mining.** For every English or bilingual post, run `english-chunks-miner` after the body is written and before validation. Chinese-only posts omit `chunks`. Completion criterion: English/bilingual frontmatter includes `chunks:` or the post is correctly marked Chinese-only.
6. **Validate.** Run `npm run build` from the reading-hub repo root. If it fails because of this post, fix and rerun once. Completion criterion: build passes, or the remaining failure is unrelated and reported.
7. **Finish.** Report the linked path and preview command: `cd reading-hub && npm run dev`. Do not commit or push unless asked.

## Frontmatter

Supported fields: `title`, `date`, `description`, `tags`, `source`, `cover`, `speaker`, `format`, `language`, `purpose`, `chunks`.

Use this layout. Omit unknown fields; never invent speaker, source, or quotes.

```yaml
---
title: "<title>"
date: 2026-04-22
description: "<one-sentence summary>"
source: https://...
cover: https://img.youtube.com/vi/<videoId>/maxresdefault.jpg
speaker: <name, role>
format: <format>
language: <English | Chinese | Bilingual>
purpose: Read-aloud article
tags:
  - tag-a
  - tag-b
---
```

Rules:
- `date` is the generation date, not source publish date. Backfilled old content should appear as newly added.
- Quote strings containing `:` or `—`.
- Slug is lowercase ASCII, hyphen-separated, no punctuation except `-`. For Chinese titles, use pinyin or an English topic slug.
- For every English or bilingual post, run `english-chunks-miner` after the body is written and before validation. Chinese-only posts omit `chunks`.

## Branch Rules

### YouTube

Work from the reading-hub repo root. Store intermediates in `tmp/youtube-clips/<videoId>/`.

1. Fetch subtitles and metadata with `yt-dlp`:

```bash
mkdir -p tmp/youtube-clips/<videoId>
yt-dlp --skip-download --write-auto-subs --sub-lang en --sub-format vtt \
  --cookies-from-browser chrome \
  -o 'tmp/youtube-clips/%(id)s/%(id)s.%(ext)s' <url>
yt-dlp --skip-download --print "%(title)s|%(uploader)s|%(upload_date)s" \
  --cookies-from-browser chrome <url>
```

2. Convert the VTT to a sentence-level SRT, flatten its text into `tmp/youtube-clips/<videoId>/<videoId>.flat.txt`, and run rolling-caption deduplication into `tmp/youtube-clips/<videoId>/<videoId>.clean.txt` whenever repeated display fragments remain:

```bash
python3 .github/skills/youtube-clipper/scripts/vtt_to_shadow_srt.py \
  tmp/youtube-clips/<videoId>/<videoId>.en.vtt \
  tmp/youtube-clips/<videoId>/<videoId>.srt
python3 - <<'PY'
from pathlib import Path

srt_path = Path("tmp/youtube-clips/<videoId>/<videoId>.srt")
flat_path = Path("tmp/youtube-clips/<videoId>/<videoId>.flat.txt")

lines = []
for raw in srt_path.read_text(encoding="utf-8").splitlines():
    line = raw.strip()
    if line and not line.isdigit() and "-->" not in line:
        lines.append(line)

flat_path.write_text(" ".join(lines) + "\n", encoding="utf-8")
PY
python3 .github/skills/youtube-clipper/scripts/dedupe_rolling_captions.py \
  tmp/youtube-clips/<videoId>/<videoId>.flat.txt \
  tmp/youtube-clips/<videoId>/<videoId>.clean.txt
```

If English captions are absent or unusable, stop and report the failure. The flattened subtitle text lives at `tmp/youtube-clips/<videoId>/<videoId>.flat.txt`; after dedupe, treat `tmp/youtube-clips/<videoId>/<videoId>.clean.txt` as the canonical cleaned transcript. Dedupe is mandatory whenever sliding-window repeats remain.

3. Keep a cleaned, sentence-level transcript:
- Preserve the speaker's wording, sequence, idioms, complete thoughts, `[applause]`, `[laughter]`, and Q&A turns.
- Only remove display repeats and subtitle artifacts; correct obvious transcription errors; add punctuation, capitalization, and paragraphs.
- Do not summarize, compress, paraphrase, add connective prose, or fill uncertain wording from context.

4. Frontmatter defaults: `source: https://www.youtube.com/watch?v=<videoId>`, `cover: https://img.youtube.com/vi/<videoId>/maxresdefault.jpg`, `speaker` from metadata, `format` matching the source, `language: English`, `purpose: Read-aloud article`, and a YAML `tags:` list that includes `youtube`.

Reference template: `src/content/posts/openclaw-ted-talk.md`.

### Web Article URL

1. Convert with the bundled URL converter:

```bash
npx -y bun .github/skills/baoyu-url-to-markdown/scripts/main.ts <url> -o tmp/<slug>.raw.md
# Add --wait for login-required pages.
```

Fallback to any method that yields clean article markdown.

2. Preserve the article, not the website shell:
- Remove nav, sidebars, share widgets, cookie banners, footer links, and related-post cards.
- Preserve headings, block quotes, code blocks, and substantive figures.
- Keep original CDN image URLs as `![alt](url)` in the same body position. Skip only decorative chrome images.
- Long articles stay whole unless the user asks for a summary.

3. Frontmatter defaults: `source: <url>`, `speaker` only if byline is present, `format: blog post` or more specific, `language` matching the article.

### Raw Text Or Existing Markdown

- Pasted text: infer title when obvious; otherwise ask briefly. Add frontmatter and clean paragraph breaks.
- Existing markdown file: preserve body and fix only frontmatter needed for schema compliance.
- Match nearby post style: most posts rely on frontmatter title and use `##` body headings, not `#`.

### User Draft

- Preserve the user's structure and voice.
- Chinese/English mixed drafts are allowed; set `language: Bilingual` when both are substantial.
- Use `**bold**`, lists, and block quotes when they clarify the draft; do not invent bilingual translation unless asked.

## Quality Gate

Before saving and before final response, check every relevant item:

- Frontmatter parses; `title` exists; `tags` is a YAML list; date is `YYYY-MM-DD`.
- Slug is valid and unique, or overwrite was confirmed.
- Body has blank lines between paragraphs. For non-YouTube sources, keep or add `##` sections only when the source structure warrants them.
- No VTT timestamps, cue numbers, `<c>` tags, position tags, `&gt;`, or HTML soup leaked into body.
- Web articles keep every substantive figure/diagram/screenshot from source.
- YouTube posts keep a cleaned, sentence-level transcript; no summarizing, compression, paraphrase, connective filler, or context-based gap filling.
- Long talks with Q&A are split after `---`.
- No hallucinated speaker names, quotes, sources, or translations.
- Every English/bilingual post has `chunks:` added via `english-chunks-miner` before validation; Chinese-only posts omit `chunks`.

## Anti-Patterns

- Raw VTT blocks as article body.
- Inline-array tags (`tags: [a, b]`).
- Files outside `src/content/posts/`.
- Source publish date in `date`.
- Guessing metadata.
- Stripping article diagrams or screenshots.
- Auto-summarizing long-form content.