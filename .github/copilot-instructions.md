# Copilot Instructions — Reading Hub

A personal English "read-while-learning" site built with **Astro 6 + content collections**. Posts are sourced from YouTube videos, web articles, or user drafts and rendered with inline English-chunk highlights and tooltip annotations.

Deployed to GitHub Pages from `main` via `.github/workflows/deploy.yml`.

---

## Commands

```bash
npm run dev      # dev server at http://localhost:4321
npm run build    # production build → ./dist
npm run preview  # preview the build locally
npm run astro -- check  # type-check .astro files
```

No test runner is configured.

---

## Architecture

### Content pipeline

```
Source (YouTube / URL / text)
  → post-creator skill → src/content/posts/<slug>.md
  → english-chunks-miner skill → patches chunks: into frontmatter
  → npm run build → GitHub Pages
```

All posts live in `src/content/posts/` as `.md` files. The Astro content collection loader (`src/content.config.ts`) validates frontmatter with Zod on every build.

### Chunk highlighting (client-side)

`src/pages/posts/[slug].astro` serialises the `chunks` array into `data-chunks` on `.article-body`. An inline `<script>` DOM-walks every text node and wraps the **first** (case-insensitive) verbatim match of each chunk in:

```html
<mark class="chunk-highlight">
  <span class="chunk-tooltip">…</span>
</mark>
```

Tooltip is a real child element (not `title` or `data-*`), triggered by both `:hover` and a `.chunk-open` class toggled on tap, giving identical desktop-hover and mobile-tap experiences. Chunks are sorted longest-first before matching so `"play it safe"` beats `"play it"`.

The walker deliberately skips `SCRIPT`, `STYLE`, `CODE`, `PRE`, and `MARK` nodes.

### Page layout

- `src/layouts/BaseLayout.astro` — shell with `<header>`, `<main>`, `<footer>`, dark-mode init script (reads `localStorage('reading-hub-theme')` before first paint to avoid flash)
- `src/pages/index.astro` — post list, sorted by `date` descending
- `src/pages/posts/[slug].astro` — article detail with cover image, tags, source link, article body, chunks panel

YouTube cover images are auto-derived from `source` if `cover` is omitted: the page extracts the `videoId` and constructs `https://img.youtube.com/vi/<videoId>/maxresdefault.jpg`. The `<img>` uses `aspect-ratio: 2/1; object-fit: cover` to crop TED/landscape black bars.

---

## Key Conventions

### Post frontmatter

Required: `title`. Everything else is optional but strongly encouraged.

```yaml
---
title: "Title — Subtitle"          # quote strings containing : or —
date: 2026-04-23                   # TODAY's date, NOT the source publish date (index sorts by this)
description: "One-sentence summary."
source: https://...
cover: https://img.youtube.com/vi/<videoId>/maxresdefault.jpg
speaker: Name, Role
format: TED-style talk + Q&A
language: English                  # English | Chinese | Bilingual
purpose: Read-aloud article
tags:
  - youtube                        # tags as a YAML list, not inline array
  - career
chunks:
  - text: "play it safe"           # exact verbatim phrase in the body (case-insensitive match)
    type: chunk                    # chunk | collocation | formulaic | sentence-frame
    meaning: "稳妥行事，不冒险"
    note: "optional usage tip"     # omit key rather than leaving empty
---
```

- `date` must be today's date (`date +%Y-%m-%d`), not the original source date. Old videos added today should rank at the top of the list.
- `tags` must be a YAML list (one item per line), not `tags: [a, b]`.
- `chunks[].text` must match the article body **verbatim** (case-insensitive). The highlighter is a literal substring match, no stemming.
- Omit `chunks` entirely for Chinese-only posts.

### Slug rules

- Filename = slug = `src/content/posts/<slug>.md`
- Lowercase ASCII, hyphen-separated, no spaces or punctuation except `-`
- For Chinese-titled posts, derive a pinyin or English slug from the topic

### Skills

Three bundled skills handle content ingestion — invoke them via Copilot chat rather than writing scripts manually:

| Skill | Trigger | What it does |
|---|---|---|
| `post-creator` | "add a post", "turn this into a post", YouTube/URL + "转成文章" | Fetches source, converts to read-aloud markdown, writes `src/content/posts/<slug>.md` |
| `english-chunks-miner` | "挖语块", "mine chunks" | Reads an existing post, proposes `chunks:` YAML, patches frontmatter |
| `baoyu-url-to-markdown` | called internally by `post-creator` | Fetches a URL via Chrome CDP and converts to clean markdown |

Full rules for each skill are in their respective `SKILL.md` under `.github/skills/`.

### YouTube posts

Preferred subtitle download (requires `yt-dlp` + Chrome cookies):

```bash
mkdir -p tmp/youtube-clips/<videoId>
yt-dlp --skip-download --write-auto-subs --sub-lang en --sub-format vtt \
  --cookies-from-browser chrome \
  -o 'tmp/youtube-clips/%(id)s/%(id)s.%(ext)s' <url>
```

VTT → readable text pipeline:
1. `vtt_to_shadow_srt.py` — flatten VTT to sentence-level SRT
2. `dedupe_rolling_captions.py` — remove YouTube's sliding-window caption repeats (typically 3× compression)

`tmp/` is git-ignored; use it for all download intermediaries.

### Writing style for posts

- Rewrite transcripts as read-aloud-friendly prose — fix disfluencies, merge fragments, add paragraph breaks and `##` headings every 3–6 paragraphs
- Preserve the speaker's voice and memorable lines verbatim
- Keep `[applause]` / `[laughter]` stage cues
- For talks with Q&A: split after a `---` rule, format as `**Interviewer:**` / `**Speaker:**`
- `##` headings only (not `#`; that's reserved for the optional document title)
- Long articles (>2000 words) should be kept whole — the site is designed for long-form reading

### Deployment

Do **not** auto-commit or push after writing a post. Tell the user the file path and suggest `npm run dev` to preview; only push when asked.

---

## Astro config notes

- `site: 'https://washi4.github.io'`, `base: '/reading-hub'` — all internal links must use `import.meta.env.BASE_URL` (already done in `BaseLayout.astro`)
- Node ≥ 22.12.0 required
- Content collection uses Astro 5+ `glob()` loader (not the legacy `type: 'content'` API)
