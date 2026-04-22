---
name: english-chunks-miner
description: >
  Mine English "chunks" (lexical chunks, collocations, formulaic expressions,
  sentence frames) from a reading-hub post and emit them as the YAML `chunks:`
  block that the post-creator layout renders as inline highlights + a review
  panel. Run this *after* a post's body is written; it reads the markdown,
  proposes chunks with Chinese meanings, and patches the frontmatter.
  Trigger phrases: "挖语块", "mine chunks", "生成 chunks", "给这篇文章加学习标注",
  "learn-while-reading", "English chunks for this post".
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - AskUserQuestion
---

# English Chunks Miner (reading-hub edition)

> Simplified from the full `english-chunks-miner` skill in `my-ai/`. In reading-hub
> the only job is: **read one post → output YAML chunks for its frontmatter**.
> We don't publish to 小红书 / 公众号, we don't sync to any knowledge base,
> we don't download subtitles — the post already exists.

## When to use

- User asks for chunks, highlights, or "learn-while-reading" annotations on a post.
- After `post-creator` has written a fresh post and you want to add the study layer.
- Post is in `src/content/posts/<slug>.md` and contains substantive English prose.

## Core principle

> Fluency ≠ grammar + vocab. Fluency = a big mental library of **pre-assembled phrases**
> you can drop into speech without composing word-by-word.

Mine for reusable building blocks, not obvious words. Quality > quantity.

## The four types

| Type (YAML) | Definition | Good examples | Skip |
|---|---|---|---|
| `chunk` | Fixed multi-word phrase, remembered whole | `start over`, `put on a brave face`, `at the end of the day` | single common words |
| `collocation` | Words that conventionally pair | `make a decision`, `drilled into me`, `heavy rain` | obvious free combos (`red car`) |
| `formulaic` | Ritualised expressions tied to a situation | `I'll get back to you`, `fast forward`, `long story short` | quotes from the speaker |
| `sentence-frame` | Template with a slot | `The thing is ___`, `What I mean is ___`, `I was wondering if ___` | complete sentences |

## Workflow

1. **Read the target post.** Glob `src/content/posts/*.md` if the user didn't name one; otherwise read the file they point at. Parse the existing frontmatter so you can preserve it.
2. **Skip if not English.** If `language` is `Chinese` or the body is mostly Chinese, stop and tell the user — no chunks to mine.
3. **Mine chunks** from the body — pull every expression that's genuinely worth teaching. No upper cap. Rules:
   - Each `text` must appear **verbatim** (case-insensitive) in the article. The runtime highlighter does a literal substring match — it doesn't stem. If the post says `"playing it safe"`, use that exact form, not `"play it safe"`.
   - Pick expressions a Chinese learner at B2+ level could realistically miss or misuse. Skip beginner vocabulary.
   - Prefer phrases that are **re-usable** outside this article (you can imagine them in a meeting, email, chat).
   - Diversify across the four types when possible; don't return 12 `chunk`s.
   - One entry per expression — don't duplicate variants.
4. **Write each entry** with:
   - `text`: the exact phrase to highlight.
   - `type`: one of `chunk` / `collocation` / `formulaic` / `sentence-frame`.
   - `meaning`: concise Chinese translation. No redundant 的 / 了 / 呢.
   - `note` (optional): usage context, register, or a common pitfall. Skip when the phrase is self-explanatory.
5. **Patch the frontmatter.** Insert a `chunks:` block at the end of the existing frontmatter. Preserve indentation and the final `---`. Do not reorder other fields.
6. **Report** the count and list the entries back to the user so they can tweak before committing.

## Output format (exact)

Append to frontmatter:

```yaml
chunks:
  - text: "start over"
    type: chunk
    meaning: "重新开始"
    note: "比 start again 更有推翻重来的意味"
  - text: "drilled into me"
    type: collocation
    meaning: "反复灌输让我记牢"
  - text: "fast forward"
    type: formulaic
    meaning: "时间快进（叙事跳过中间细节）"
  - text: "The thing is"
    type: sentence-frame
    meaning: "关键是……（引出真正想说的话）"
```

Quote every `text` and `meaning` with double quotes (YAML-safe). `note` is optional — omit the key rather than leaving it empty.

## Quality bar

Before patching, sanity-check:

- [ ] Every `text` grep-matches the article body (case-insensitive).
- [ ] Every entry passes the "re-usable outside this article" test — if you can't imagine using it elsewhere, drop it. Quality bar, not a count bar.
- [ ] No duplicates, no near-duplicates (pick one of `play it safe` / `playing it safe` based on what's in the article).
- [ ] Chinese meanings are specific, not paraphrases of the English. `make a decision` → `做决定`, not `决定做某事`.
- [ ] Types are distributed: ideally at least 2 different types appear.
- [ ] No proper nouns, no numbers, no one-word entries.

## Anti-patterns

- ❌ Including `however`, `also`, `really`, or other single adverbs.
- ❌ Inventing a `meaning` that's a paraphrase rather than a translation.
- ❌ Adding a `chunks:` block to a Chinese-only post.
- ❌ Changing any other frontmatter field while patching.
- ❌ Using regex metacharacters or YAML anchors in `text`.
- ❌ Summarising the article in `note` — `note` is about the *expression*, not the story.

## Example run

Input (user): "挖一下 `i-left-everything-and-moved-to-hong-kong.md` 的语块"

Actions:
1. Read `src/content/posts/i-left-everything-and-moved-to-hong-kong.md`.
2. Scan the body, pick 8 phrases that recur in everyday English: `start over`, `play it safe`, `drilled into me`, `fast forward`, `itch to do something`, `once-in-a-lifetime opportunity`, `put on a brave face`, `bawling my eyes out`.
3. Write the `chunks:` YAML block, diversify across types (4 `chunk`s, 2 `collocation`s, 1 `formulaic`, no sentence-frame this time — OK since variety is aimed-for, not required).
4. Edit the file, inserting before the closing `---` of the frontmatter.
5. Report: "Added 8 chunks to `i-left-everything-and-moved-to-hong-kong.md`. Run `npm run dev` to see inline highlights."

## Relationship to post-creator

`post-creator` writes the post (title, body, basic frontmatter, cover). This skill adds the `chunks:` annotation layer. They can run back-to-back: `post-creator` → `english-chunks-miner` → `npm run build`. Neither needs the other — a post without `chunks:` just renders without highlights.
