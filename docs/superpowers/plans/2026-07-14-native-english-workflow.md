# Native-English Learning Workflow Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make YouTube posts source-faithful cleaned transcripts and automatically add reusable native-English chunks.

**Architecture:** Keep subtitle acquisition and normalization in `youtube-clipper`, transcript assembly and orchestration in `post-creator`, and learning annotations in `english-chunks-miner`. The final post body is the sole source for chunk matching, so annotations cannot alter the source-faithful transcript.

**Tech Stack:** Markdown skill specifications, Python subtitle utilities, Astro content collections.

## Global Constraints

- YouTube post bodies use cleaned sentence-level subtitles as their sole authority.
- Cleanup is limited to display-repeat removal, subtitle markup removal, obvious transcription corrections, punctuation, capitalization, and paragraphing.
- Never summarize, paraphrase, compress, add connective prose, or substitute missing captions with generated text.
- English and bilingual posts run chunk mining by default after the body exists.
- Chunks must literally match the final body and be reusable outside the source context.
- Do not change existing posts, application code, runtime dependencies, or unrelated skill files.
- Do not commit unless the user explicitly requests it.

---

### Task 1: Define the subtitle-output contract

**Files:**
- Modify: `.github/skills/youtube-clipper/SKILL.md`

**Interfaces:**
- Consumes: YouTube English VTT captions supplied by `yt-dlp`.
- Produces: A sentence-level SRT and optional deduplicated plain-text transcript that `post-creator` can treat as source material.

- [ ] **Step 1: Add the fidelity contract beneath the skill introduction**

  Add this content after the description of the trimmed scope:

  ```markdown
  ## Transcript Contract

  The output is source material for a native-English transcript, not a summary.
  Remove caption-format artifacts and progressive-display repeats only. Preserve
  wording and order; retain uncertain wording rather than guessing a correction.
  If English captions cannot be downloaded or converted, report the failure and
  do not substitute video metadata or generated prose.
  ```

- [ ] **Step 2: Clarify artifact names in the usage section**

  Replace the conversion comments with names that expose their roles:

  ```bash
  # Produce a sentence-level transcript source.
  python3 scripts/vtt_to_shadow_srt.py <input.vtt> <output.srt> \
    [--max-duration 8] [--min-duration 1.5]

  # Remove rolling display repetition from flattened transcript text.
  python3 scripts/dedupe_rolling_captions.py <input.txt> <output.txt>
  ```

- [ ] **Step 3: Add a documentation-level acceptance example**

  Add this explicit expected outcome after the usage block:

  ```markdown
  A repeated rolling-caption sequence such as `we can we can build` must become
  `we can build`; a non-repeated spoken phrase must remain unchanged.
  ```

- [ ] **Step 4: Review the contract for scope leaks**

  Confirm the skill still excludes translation, generated summaries, subtitle
  burning, and post creation. It should only describe acquisition and faithful
  subtitle normalization.

### Task 2: Make the YouTube post path transcript-first and chunk-complete

**Files:**
- Modify: `.github/skills/post-creator/SKILL.md`

**Interfaces:**
- Consumes: The VTT, sentence-level SRT, and deduplicated plain text produced
  by the YouTube subtitle workflow.
- Produces: One `src/content/posts/<slug>.md` whose body is a cleaned native
  English transcript and whose English/bilingual frontmatter includes chunks.

- [ ] **Step 1: Replace rewrite-oriented language in the top-level contract**

  Change the job statement to require a readable, source-faithful post rather
  than generic read-aloud prose:

  ```markdown
  Create one Astro content post at `src/content/posts/<slug>.md`. The post must
  parse, preserve the source's substance, and keep the source's English voice.
  For YouTube, the cleaned subtitle transcript is the sole authority for the
  body.
  ```

- [ ] **Step 2: Make the subtitle pipeline explicit and complete**

  In the YouTube branch, specify the required artifact chain:

  ```markdown
  Convert the VTT to a sentence-level SRT, flatten its text into
  `tmp/youtube-clips/<videoId>/<videoId>.clean.txt`, and run rolling-caption
  deduplication whenever repeated display fragments remain. If English captions
  are absent or unusable, stop and report the failure.
  ```

  Retain the existing `yt-dlp`, SRT converter, and dedupe commands, but ensure
  their input and output paths are consistent with this chain.

- [ ] **Step 3: Replace the YouTube prose rules with the fidelity boundary**

  Use this rule block:

  ```markdown
  Keep a cleaned, sentence-level transcript:
  - Preserve the speaker's wording, sequence, idioms, complete thoughts,
    `[applause]`, `[laughter]`, and Q&A turns.
  - Only remove display repeats and subtitle artifacts; correct obvious
    transcription errors; add punctuation, capitalization, paragraphs, and
    `##` headings.
  - Do not summarize, compress, paraphrase, add connective prose, or fill
    uncertain wording from context.
  ```

- [ ] **Step 4: Make chunk mining a default final step**

  Replace the conditional wording about running `english-chunks-miner` with:

  ```markdown
  For every English or bilingual post, run `english-chunks-miner` after the
  body is written and before validation. Chinese-only posts omit `chunks`.
  ```

  Update the numbered workflow and quality gate so the default is reflected in
  both places.

- [ ] **Step 5: Run the content validation**

  Run:

  ```bash
  npm run build
  ```

  Expected: Astro finishes successfully and validates all content collection
  frontmatter.

### Task 3: Sharpen native-English chunk selection

**Files:**
- Modify: `.github/skills/english-chunks-miner/SKILL.md`

**Interfaces:**
- Consumes: The finalized English or bilingual post body.
- Produces: A frontmatter-only `chunks:` patch whose entries literally match the
  body.

- [ ] **Step 1: Add a reusable-full-sentence rule to the type taxonomy**

  Add this sentence after the type table:

  ```markdown
  A complete sentence is eligible only when it works as a broadly reusable
  formulaic expression or sentence frame; otherwise extract the reusable
  sub-phrase instead.
  ```

- [ ] **Step 2: Add native-English selection criteria to the candidate gate**

  Extend the candidate step with:

  ```markdown
  Prefer natural spoken or written English that a learner can transfer to a
  different conversation, email, or argument. Reject source-specific lines
  whose value depends on the speaker, event, or story context.
  ```

- [ ] **Step 3: Preserve the literal and frontmatter boundaries**

  Keep the existing case-insensitive literal gate, the frontmatter-only patch
  rule, and the prohibition on story-summary notes. Add an anti-pattern:

  ```markdown
  - Adding a memorable source quotation that is not broadly reusable.
  ```

- [ ] **Step 4: Run a manual skill acceptance pass**

  Review the combined contracts against one hypothetical source phrase:

  ```text
  Transcript body: "I had to put on a brave face."
  Chunk: text: "put on a brave face"
  ```

  Confirm that the phrase is reusable, appears verbatim in the body, and can be
  added without modifying body prose.

### Task 4: Validate cross-skill consistency

**Files:**
- Modify: `.github/skills/youtube-clipper/SKILL.md`
- Modify: `.github/skills/post-creator/SKILL.md`
- Modify: `.github/skills/english-chunks-miner/SKILL.md`

**Interfaces:**
- Consumes: The three revised skill contracts.
- Produces: A coherent workflow with no generated-prose fallback.

- [ ] **Step 1: Inspect only the final skill diffs**

  Run:

  ```bash
  git --no-pager diff -- \
    .github/skills/youtube-clipper/SKILL.md \
    .github/skills/post-creator/SKILL.md \
    .github/skills/english-chunks-miner/SKILL.md
  ```

  Expected: every change supports subtitle fidelity, automatic chunk mining, or
  reusable native-English selection.

- [ ] **Step 2: Scan for contradictory terms**

  Run:

  ```bash
  rg -n "summar|paraphras|rewrite|generated prose|chunk" \
    .github/skills/youtube-clipper/SKILL.md \
    .github/skills/post-creator/SKILL.md \
    .github/skills/english-chunks-miner/SKILL.md
  ```

  Expected: no instruction authorizes summaries, paraphrases, or generated
  replacement text in the YouTube body path.

- [ ] **Step 3: Run the repository validation**

  Run:

  ```bash
  npm run build
  ```

  Expected: Astro build succeeds.
