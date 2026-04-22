---
name: post-creator
description: >
  Create a new reading post for the reading-hub Astro site from any source —
  a YouTube video, a web article URL, a pasted text, or the user's own draft.
  Non-markdown sources are converted to clean, read-aloud-friendly markdown
  with proper frontmatter that satisfies the Astro content collection schema,
  then written to `src/content/posts/<slug>.md`.
  Make sure to use this skill whenever the user wants to add an article to
  reading-hub, save a YouTube video as a reading-friendly article, archive a
  web article, publish their own writing to the site, or asks to "turn this
  into a post", even if they don't explicitly name the reading-hub project.
  Trigger phrases include "加一篇文章", "创建一个 post", "把这个视频变成文章",
  "发到 reading-hub", "转成朗读文章", "save this to reading-hub", "new post",
  or whenever the user provides a YouTube URL / web URL / raw text and asks
  to turn it into a reading post.
allowed-tools:
  - Read
  - Write
  - Bash
  - Glob
  - AskUserQuestion
---

# Reading Hub Post Creator

This skill makes sure every post lands at `src/content/posts/<slug>.md` with the correct frontmatter, passes the content collection schema, and reads comfortably aloud.

## What this skill does

1. Identifies the source type: **YouTube video**, **web article URL**, **raw text / existing md**, or **user's own draft**.
2. For non-markdown sources, converts the source into clean markdown prose (not subtitle fragments, not HTML soup).
3. Writes a properly formatted post file to `src/content/posts/<slug>.md` with valid frontmatter that satisfies the schema in `src/content.config.ts`.
4. Returns the file path so the user can preview it with `npm run dev`.

## Output location & filename rules

- Always write to `src/content/posts/<slug>.md` (relative to the reading-hub repo root).
- `<slug>` must be: lowercase ASCII, words separated by `-`, no spaces, no punctuation except `-`. For Chinese-titled articles, use a pinyin or English slug derived from the topic, not the raw Chinese.
- If a file with the same slug already exists, confirm with the user before overwriting. Do not silently clobber.

## Required frontmatter

The Astro content collection (`src/content.config.ts`) accepts:

| Field | Required | Notes |
|---|---|---|
| `title` | yes | Human-readable title. For talks, can include a subtitle after `—`. |
| `date` | recommended | **The date this post was generated, NOT the source publish date.** Use today (`date +%Y-%m-%d`). The index page sorts by this field, so using the video upload date would bury freshly-added older content at the bottom of the list. |
| `description` | recommended | One-sentence summary. Chinese or English. Used on index page. |
| `tags` | recommended | Array of lowercase slugs, e.g. `[youtube, opensource, career]`. |
| `source` | for external sources | Original URL. Rendered as a link at the top of the article (and the "watch original" button for YouTube). |
| `cover` | for YouTube / when available | Absolute image URL. For YouTube, use `https://img.youtube.com/vi/<videoId>/maxresdefault.jpg`. Rendered as a clickable hero image that opens the source. If omitted on a YouTube post, the layout auto-derives it from `source`. |
| `speaker` | for talks/interviews | Name + role. |
| `format` | optional | e.g. `TED-style talk + Q&A`, `blog post`, `podcast transcript`. |
| `language` | optional | `English`, `Chinese`, or `Bilingual`. |
| `purpose` | optional | e.g. `Read-aloud article`, `Study notes`. |
| `chunks` | recommended for English/bilingual | Array of English expressions to highlight inline with Chinese meanings. See the dedicated section below. |

Use this exact YAML block layout (tags as a list, not inline) — it matches the existing posts in the repo:

```yaml
---
title: "<title>"
date: 2026-04-22   # today, from `date +%Y-%m-%d` — NOT the source publish date
description: "<one-sentence summary>"
source: https://...
cover: https://img.youtube.com/vi/<videoId>/maxresdefault.jpg   # YouTube only
speaker: <name, role>
format: <format>
language: <language>
purpose: <purpose>
tags:
  - tag-a
  - tag-b
---
```

Strings with `:` or `—` should be quoted. Omit fields you don't have — don't invent speakers or sources.

## Workflow by source type

### A. YouTube video

All required tools are bundled in this repo under `.github/skills/youtube-clipper/` — do not depend on any sibling workspace.

Default working directory for downloads: `tmp/youtube-clips/<videoId>/` (create if missing, git-ignored). If the user already has a VTT file elsewhere, use theirs.

1. **Download subtitles.** Prefer `yt-dlp` CLI directly — the bundled `download_video.py` has been known to fail silently on some videos. From the reading-hub repo root:
   ```bash
   mkdir -p tmp/youtube-clips/<videoId>
   yt-dlp --skip-download --write-auto-subs --sub-lang en --sub-format vtt \
     --cookies-from-browser chrome \
     -o 'tmp/youtube-clips/%(id)s/%(id)s.%(ext)s' <url>
   ```
   Requires `yt-dlp` on PATH (`pip install yt-dlp`). Cookies bypass the 403 errors that hit anonymous requests. Also fetch metadata (title, uploader, upload date) to fill frontmatter:
   ```bash
   yt-dlp --skip-download --print "%(title)s|%(uploader)s|%(upload_date)s" \
     --cookies-from-browser chrome <url>
   ```
   If you also need the video file, use `.github/skills/youtube-clipper/scripts/download_video.py <url> tmp/youtube-clips`.
2. **Convert VTT to sentence-level SRT:**
   ```bash
   python3 .github/skills/youtube-clipper/scripts/vtt_to_shadow_srt.py \
     tmp/youtube-clips/<videoId>/<videoId>.en.vtt /tmp/<videoId>.srt
   ```
   Then concatenate the subtitle lines (every 3rd block in each SRT entry) into continuous text and strip VTT artifacts (`<c>`, `&gt;`, position tags).
3. **Remove rolling-caption repeats.** YouTube auto-captions often use a sliding window where each frame repeats part of the previous frame. After flattening, run the dedupe pass — it typically cuts word count by ~3× without losing content:
   ```bash
   python3 .github/skills/youtube-clipper/scripts/dedupe_rolling_captions.py \
     /tmp/<videoId>.flat.txt /tmp/<videoId>.clean.txt
   ```
   If the flattened text still has phrases like `"moved to Hong Kong. This moved to Hong Kong. This moved to Hong Kong."`, this step is mandatory. If it's already clean, the script is a no-op.
4. **Fill frontmatter.** Required YouTube-specific fields:
   - `date`: **today's date** (`date +%Y-%m-%d`). Do NOT use the video upload date — the index sorts by this field and backfilled old videos should still rank by when you added them.
   - `source`: the canonical `https://www.youtube.com/watch?v=<videoId>` URL.
   - `cover`: `https://img.youtube.com/vi/<videoId>/maxresdefault.jpg` (the layout also auto-derives this from `source` if you omit it, but setting it explicitly keeps posts self-describing).
   - `speaker`: uploader / presenter name from the metadata fetch above.
3. **Rewrite as an article, don't just paste the transcript.** This is the step that makes the result read-aloud friendly:
   - Fix disfluencies: `I I I` → `I`, `no reason no reason` → `no reason — no reason`
   - Merge fragments into complete sentences; add proper punctuation
   - Break into logical paragraphs; add `##` section headings every 3–6 paragraphs
   - Preserve voice, idiomatic phrases, and memorable lines verbatim (e.g. `the mad lad figured it out on its own`)
   - Keep stage cues like `[applause]`, `[laughter]` — they help the reader pace themselves
   - For talks with Q&A, add a `---` then a `## Q&A` section formatted as `**Interviewer:** ...` / `**Speaker:** ...`
4. **Fill frontmatter** with `source: https://www.youtube.com/watch?v=<videoId>`, `speaker`, `format: TED-style talk + Q&A` (or similar), `language: English`, `purpose: Read-aloud article`.
5. Reference: `src/content/posts/What's OpenClaw.md` is the canonical template for this flow.

### B. Web article URL

1. Fetch and convert the URL to markdown using the bundled `baoyu-url-to-markdown` skill:
   ```bash
   npx -y bun .github/skills/baoyu-url-to-markdown/scripts/main.ts <url> -o tmp/<slug>.raw.md
   # For login-required pages, add --wait
   ```
   Requires `bun` via `npx`. Fallback: any tool that produces clean markdown with the article body (no nav/ads).
2. Strip site chrome: sidebars, "related posts", share buttons, cookie banners, footer links.
3. Preserve the article's own headings (`##`, `###`), block quotes, and code blocks.
4. **Preserve inline images.** If the source article has figures, diagrams, or screenshots, keep them in the post body as `![alt text](https://...)` at the same position they appear in the source. Use the original CDN URL — don't download, don't strip. Only skip purely decorative chrome (logos, share icons, "keep reading" cards). When in doubt, keep it: a figure diagram is part of the argument. Before saving, scan the raw source for `![` / `<img` / `<figure>` and verify every substantive one made it into the post.
5. Add frontmatter with `source: <original URL>`. If the page has a byline, use `speaker: <author>` (or leave it off — don't invent).
6. If the article is long (>2000 words), keep it whole — reading-hub is for long-form. Don't summarize unless the user asks.

### C. Raw text or existing markdown

1. If the user pastes text, ask them (briefly) for a title if one isn't obvious, then format:
   - Add frontmatter
   - Ensure the first heading is `# <title>` (optional; many posts skip it since the title comes from frontmatter — match the style of nearby posts)
   - Clean up paragraph breaks and straighten quotes/dashes
2. If they give you an existing `.md` file, read it, keep the body, and only add/fix frontmatter to match the schema.

### D. User's own draft (Chinese / bilingual)

See `src/content/posts/hello-world.md` and `sample-transcript.md` for the in-repo style: mixed Chinese/English paragraphs are welcome, use `**bold**` for key terms, `- ` for bullets, `>` for pulled quotes. Set `language: Bilingual` when both languages appear in substantial amounts.

## English chunks (learn-while-reading)

This site doubles as an English-study tool. For any **English or bilingual** post, include a `chunks` array in the frontmatter. The layout will:

- Auto-highlight each chunk's **first occurrence** in the article body with a yellow underline.
- Show the Chinese meaning (and any note) on hover or tap.
- Render a `📘 本文语块` review list at the bottom of the article.

### Frontmatter format

```yaml
chunks:
  - text: "play it safe"            # the exact English phrase to match (case-insensitive)
    type: chunk                     # chunk | collocation | formulaic | sentence-frame
    meaning: "稳妥行事，不冒险"       # Chinese meaning, shown in tooltip + list
    note: "自述性格常用"              # optional extra context / usage tip
  - text: "once-in-a-lifetime opportunity"
    type: collocation
    meaning: "千载难逢的机会"
```

### How to pick chunks

Mine them with the bundled **`english-chunks-miner`** skill at `.github/skills/english-chunks-miner/SKILL.md` — run it right after writing the post body and it will patch the `chunks:` block into the frontmatter for you. Include every expression that's genuinely worth teaching; the layout only highlights each phrase's **first** occurrence, so a long list stays readable. Prefer:

| Type | Good examples | Avoid |
|---|---|---|
| `chunk` | `start over`, `put on a brave face`, `bawling my eyes out` | single common words |
| `collocation` | `drilled into me`, `itch to do something`, `make a decision` | obvious free combinations |
| `formulaic` | `fast forward`, `long story short`, `to be fair` | |
| `sentence-frame` | `The thing is …`, `What I mean is …` | |

### Rules

- `text` must appear **verbatim** somewhere in the article body (case-insensitive). If the post only has `"playing it safe"`, change `text` to `"playing it safe"` — the matcher doesn't stem.
- The highlighter only marks the **first** occurrence to avoid visual noise; the review list still shows every entry.
- Skip the field entirely for Chinese-only posts or when there's nothing worth teaching — an empty list is cleaner than junk.
- For YouTube posts, pipe the deduped transcript through the `english-chunks-miner` skill, then translate / annotate the output into this YAML shape.

## Quality bar before writing the file

Check these before saving:

- [ ] Frontmatter parses as YAML; `title` present; `tags` is a list; dates in `YYYY-MM-DD`.
- [ ] Slug is ASCII, lowercase, hyphen-separated.
- [ ] No VTT timestamps, no `<c>` tags, no `&gt;` or other HTML entities leaked into the body.
- [ ] For web-article sources: every substantive figure/diagram/screenshot from the original is present in the post body as `![alt](url)`. Decorative chrome (site logos, share buttons, "keep reading" cards) is excluded.
- [ ] Paragraphs have blank lines between them. Section headings use `##` (not `#`; that's reserved for the document title if used at all).
- [ ] Long talks have Q&A split out after a `---` rule.
- [ ] No hallucinated speaker names, quotes, or sources. If the transcript didn't name someone, call them `Interviewer` or by their role.

## After writing

Tell the user the final path (linked) and a one-line preview hint:

```
cd reading-hub && npm run dev
```

Then wait — don't auto-commit or push unless asked.

## Anti-patterns

- Pasting raw VTT subtitle blocks as the post body. The whole point of this site is that posts read aloud naturally.
- Filling `speaker` or `source` with guesses. Leave the field out if you don't know.
- Creating the file outside `src/content/posts/`. The Astro loader won't pick it up anywhere else.
- Inventing Chinese translations when the source is English-only — unless the user explicitly asks for a bilingual version.
- Auto-summarizing long articles. Reading-hub exists to host long-form; preserve it.
