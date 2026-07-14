# Native-English Learning Workflow Design

## Goal

Make YouTube posts a faithful, readable record of native English while
automatically adding only reusable learning annotations. The workflow must not
summarize, paraphrase, or replace speech with model-generated prose.

## Scope

This design updates the contracts of:

- `.github/skills/youtube-clipper/SKILL.md`
- `.github/skills/post-creator/SKILL.md`
- `.github/skills/english-chunks-miner/SKILL.md`

It does not change existing posts, application code, or runtime dependencies.

## Workflow

1. `youtube-clipper` downloads the English VTT and removes progressive-display
   repetition to produce sentence-level subtitle text.
2. `post-creator` uses that cleaned subtitle text as the sole authority for a
   YouTube post body. It writes a readable transcript and then runs
   `english-chunks-miner` by default for English and bilingual posts.
3. `english-chunks-miner` patches only the post frontmatter with expressions
   that match the final body verbatim.

The subtitle artifact remains an intermediate source in `tmp/`; the published
post body is the cleaned, sentence-level native-English transcript.

## Transcript Fidelity

Allowed transcript cleanup is limited to:

- removing VTT markup, timestamps, cue numbers, and progressive-display repeats;
- correcting obvious transcription errors;
- applying punctuation, capitalization, and paragraph boundaries; and
- retaining speaker order, stage cues, and Q&A turns.

The workflow must retain the talk's content and sequence. It must not
summarize, compress, paraphrase, add connective prose, or invent missing
speech. When a wording is uncertain, preserve the subtitle wording rather
than guess. Missing or unusable captions stop the YouTube-post path and are
reported; metadata, descriptions, or model knowledge cannot substitute for
the transcript.

## Learning Annotations

Chunk mining is a default final step after an English or bilingual body exists.
Candidates must be natural, reusable phrases, collocations, formulaic
expressions, or sentence frames. A complete sentence is eligible only when it
is broadly reusable outside its original context.

Every chunk must:

- appear verbatim in the body, case-insensitively;
- include a concise Chinese meaning;
- avoid proper nouns, beginner-level single words, story summaries, and
  source-specific quotations; and
- preserve all unrelated frontmatter fields and order.

## Skill Contracts

`youtube-clipper` documents its output format and cleanup limits.

`post-creator` makes subtitle text the sole YouTube-body source, calls the
chunk miner by default, and rejects rewriting-oriented language.

`english-chunks-miner` keeps its literal-match and frontmatter-only boundaries,
while allowing a narrowly defined class of broadly reusable full sentences.

## Failure Handling And Validation

Each skill reports a source or processing failure explicitly instead of
silently falling back to generated prose. The post creator validates resulting
content with `npm run build` and fixes only failures introduced by the new
post. Skill changes are reviewed against this workflow and the existing build
command verifies the repository still accepts its content definitions.
