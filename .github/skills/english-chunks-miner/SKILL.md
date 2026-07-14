---
name: english-chunks-miner
description: >
  Mine reusable English chunks from a reading-hub post into the frontmatter
  `chunks:` YAML used for inline highlights. Use after a post body exists, when
  the user says "挖语块", "mine chunks", "生成 chunks", or asks for
  learn-while-reading annotations.
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - AskUserQuestion
---

# English Chunks Miner

Job: read one `src/content/posts/<slug>.md` post and patch a literal-match
`chunks:` block into its frontmatter. Do not publish, sync, download, summarize,
or change unrelated fields.

## Principle

> Fluency ≠ grammar + vocab. Fluency = a big mental library of **pre-assembled phrases**
> you can drop into speech without composing word-by-word.

Mine reusable building blocks, not obvious words. Quality beats count.

## The four types

| Type (YAML) | Definition | Good examples | Skip |
|---|---|---|---|
| `chunk` | Fixed multi-word phrase, remembered whole | `start over`, `put on a brave face`, `at the end of the day` | single common words |
| `collocation` | Words that conventionally pair | `make a decision`, `drilled into me`, `heavy rain` | obvious free combos (`red car`) |
| `formulaic` | Ritualised expressions tied to a situation | `I'll get back to you`, `fast forward`, `long story short` | quotes from the speaker |
| `sentence-frame` | Template with a slot | `The thing is ___`, `What I mean is ___`, `I was wondering if ___` | complete sentences |

A complete sentence is eligible only when it works as a broadly reusable formulaic expression or sentence frame; otherwise extract the reusable sub-phrase instead.

## Workflow

1. **Resolve one post.** If the user named a file, use it. Otherwise glob
  `src/content/posts/*.md` and ask which post to mine. Completion: exactly one
  target file is identified.
2. **Read and classify.** Parse frontmatter and body. If `language: Chinese` or
  the body is mostly Chinese, stop and report that no chunks were added.
  Completion: existing frontmatter shape and language are known.
3. **Mine candidates.** Pull every B2+ expression worth teaching, with no count
  target. Prefer natural spoken or written English that a learner can transfer to a different conversation, email, or argument. Reject source-specific lines whose value depends on the speaker, event, or story context. Keep only phrases reusable outside this article. Completion: every candidate has a type, concise Chinese meaning, and optional note.
4. **Run the literal gate.** Each `text` must appear verbatim in the body,
  case-insensitive. The highlighter is a literal substring matcher; if the post
  says `"playing it safe"`, use that exact form, not `"play it safe"`.
  Completion: every surviving `text` grep-matches the body.
5. **Run the quality gate.** Drop duplicates, near-duplicates, one-word entries,
  proper nouns, numbers, beginner vocabulary, article-only quotes, and entries
  whose `note` summarizes the story instead of the expression. Prefer at least
  two types when the article supports them. Completion: every remaining entry
  passes all gates.
6. **Patch frontmatter only.** Insert or replace the `chunks:` block at the end
  of the existing frontmatter, before the closing `---`. Preserve all other
  fields and their order.
7. **Report.** Tell the user the file, count, and final entries. Completion: the
  user can review every added chunk without opening the file.

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

Quote every `text`, `meaning`, and `note` with double quotes. Omit `note` when it
does not add usage context, register, or a common pitfall.

## Anti-patterns

- Including `however`, `also`, `really`, or other single adverbs.
- Inventing a `meaning` that paraphrases instead of translating.
- Adding `chunks:` to a Chinese-only post.
- Reordering or rewriting unrelated frontmatter.
- Using YAML anchors in `text`.
- Summarizing the article in `note`.
- Adding a memorable source quotation that is not broadly reusable.
