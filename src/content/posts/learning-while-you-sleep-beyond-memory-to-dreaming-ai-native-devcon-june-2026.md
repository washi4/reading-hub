---
title: "Lamis Mukta - Learning while you sleep: Beyond memory to dreaming - AI Native DevCon June 2026"
date: 2026-07-06
description: "Lamis Mukta explains how context engineering, memory systems, and dreaming help agents learn across sessions and improve in production."
source: https://youtu.be/tTcxVv8HHNw
cover: https://img.youtube.com/vi/tTcxVv8HHNw/maxresdefault.jpg
speaker: Lamis Mukta, Anthropic
format: Conference talk + Q&A
language: English
purpose: Read-aloud article
tags:
  - youtube
  - ai
  - agents
  - memory
  - context-engineering
  - dreaming
chunks:
  - text: "what it really takes"
    type: sentence-frame
    meaning: "真正需要的是……"
    note: "用于引出核心要求或难点。"
  - text: "translate that into durable, scalable, useful products"
    type: collocation
    meaning: "把它转化成耐用、可扩展、真正有用的产品"
  - text: "do the simple thing that works"
    type: formulaic
    meaning: "先做那个有效的简单方案"
  - text: "the boring parts"
    type: chunk
    meaning: "那些无聊但占精力的部分"
  - text: "progressive disclosure"
    type: chunk
    meaning: "渐进式披露/按需展开信息"
  - text: "autonomously manage"
    type: collocation
    meaning: "自主管理"
  - text: "file systems"
    type: chunk
    meaning: "文件系统"
  - text: "state of the art"
    type: collocation
    meaning: "最先进的水平"
    note: "原文是 state of art / state of the art 的口语化说法。"
  - text: "out-of-band memory curation"
    type: chunk
    meaning: "带外的记忆整理"
  - text: "a second-order process over memory"
    type: sentence-frame
    meaning: "对记忆进行二阶处理的流程"
  - text: "go stale"
    type: formulaic
    meaning: "变旧、失去时效"
  - text: "the next run"
    type: chunk
    meaning: "下一次运行"
  - text: "close the loop"
    type: formulaic
    meaning: "形成闭环"
  - text: "the real world"
    type: chunk
    meaning: "现实世界"
  - text: "the bottleneck was no longer typing"
    type: sentence-frame
    meaning: "瓶颈不再是打字了"
  - text: "give agents autonomy"
    type: collocation
    meaning: "给智能体自主权"
---

# Lamis Mukta - Learning while you sleep: Beyond memory to dreaming - AI Native DevCon June 2026

## Context engineering is the real lever

[applause] Lamis opens with a simple claim: models keep getting smarter, but smarter models do not automatically become better products. To make them useful in the real world, you still have to answer the harder question: what it really takes to translate that into durable, scalable, useful products. In her framing, the bottleneck was no longer typing; it was thinking.

Her answer is context engineering. The raw model intelligence is there, but the context around it is what makes the model succeed inside a codebase, inside an organization, or inside an agent fleet. That context can be orthogonal to intelligence itself. A new model will not automatically know your workflows, your preferences, or the habits of your team.

So the first lesson is Anthropic's familiar one: do the simple thing that works. The payoff comes from starting with small, practical context rather than overbuilding some grand system from day one.

## From Claude.md to skills

The talk then walks through the recent path the team has taken. It started with Claude.md files: plain markdown, injected at the beginning of a session, that give the model a few instructions about the codebase, the organization, or the user's preferences. That sounds modest, but it was unreasonably effective.

The limitation was obvious too. If the file keeps growing, you get context bloat. What happens when an important file becomes very, very long?

From there came memory tools. Instead of making memory static and fully human-managed, the idea was to let agents autonomously manage their own memory systems: decide what to read, what to write, and when to update. That is where autonomy starts to matter. The agent is not just using context; it is helping maintain it.

Next came skills, which solve the ever-growing context problem through progressive disclosure. A skill keeps the procedural workflow in a short front matter and pushes the detail into the body. The agent only pays attention to the small part it needs right now, while the deeper material stays available until it matters. Lamis compares that to a bookshelf: you do not need every book in your head all the time, but you want to know which one to pull off the shelf when the conversation calls for it.

## Memory as file systems

The current state of the art, she says, is to model memory systems as file systems. That is deliberately focused on the boring parts in the best possible way. You can fill them with markdown. Agents already know how to use normal file system tools like bash and grep. Let them search the filesystem instead of inventing some special-purpose memory API for every read and write.

That search behavior mirrors progressive disclosure again. You can index the memories well, let agents search intelligently, and give them autonomy when they are writing to memory too.

If it works, you start to get the feeling of continual learning. The second time an agent sees a task, it should do it better. It should remember what went wrong, spend fewer tokens, and become faster and cheaper over time.

## Production changes the problem

But then production shows up.

Once many agents are collaborating over long periods of time, and once codebases get complicated, the clean theoretical story gets messy. Multiple agents can try to write to the same memory file at once. One agent can decide to update the organization-wide contacts file that every other agent is reading. Memories can go stale. Worse, they can be written incorrectly or even maliciously injected.

So the memory system needs guardrails.

Lamis lays out the main ones. Versioning matters, so you can track changes and roll back when a new update is bad. Concurrency matters, so an agent checks whether the memory changed between the moment it drafted an edit and the moment it writes it. Permissioning matters, because not every memory should be writable. Some memories are organization-wide and read-only; others are small scratchpads for an individual agent. Portability matters too, because well-curated context should be usable across multiple product surfaces and systems.

## Why it works

When those pieces come together, the gains are real. Agents get better accuracy on the second try. They get faster because they need fewer tokens and can one-shot more tasks. Product teams get context back because the agents are doing more of the self-learning loop themselves.

That is the nice part: the system becomes symbiotic. The agent improves, the human gets back time, and the memory store gets better with use.

## The limitation of in-band learning

The next bottleneck is in-band memory.

In-band memory means the agent is reading from and writing to memory during the same session in which it is trying to do the task. That has two limitations. First, there is a resource tradeoff: should the agent spend capacity on the current task, or on making future runs better? Second, there is a visibility problem: a single session cannot see cross-session patterns.

If the same mistake keeps happening across sessions, the agent cannot naturally spot the pattern. If different fleets are failing in different ways, a single session still cannot see the whole picture.

The answer is out-of-band memory curation. Lamis uses a school analogy: students do the work, teachers mark it, and a head teacher sees the pattern across the whole fleet. That is exactly the role here. Some process with dedicated capacity should look across transcripts, see what is going wrong, and steer the curriculum.

## Dreaming

That is where dreaming comes in.

Dreaming is a second-order process over memory. It runs in batch, asynchronously, with dedicated resources. It reviews the existing memory store, looks at a collection of transcripts, and proposes changes. In other words, it is the thing that helps memory itself stay effective.

She gives a few examples. If every geography student gets the same question wrong, the teacher realizes the topic is missing from the curriculum. If a class keeps using radians when the test expected degrees, maybe the calculator setup is wrong. In agent terms, that means the transcripts are showing a tool configuration problem, or a missing piece of shared context, or an organization-wide convention that should really be in memory.

Dreaming helps close the loop. It helps cut stale memory, add missing memory, and organize the store so that the next run is smarter.

## The final takeaway

By the end, the message is clear. Start with the simple thing that works. Use Claude.md, skills, and autonomous memory where they help. When the system grows, add the deterministic guardrails that make versioning, concurrency, permissions, and auditing safe. Give agents autonomy when it makes sense, and when you need to improve memory across sessions, add dreaming as the out-of-band layer that helps the system learn over time.

Lamis closes by reminding the room that this is still open territory. Context engineering only really took off in the past year, and there is still a lot to learn. But the direction is obvious: keep thinking, keep learning, and keep dreaming.

---

## Q&A

**Interviewer:** Are you being reckless with safety when you let these systems loose?

**Lamis:** Not really. The key is to put proper security layers around them. You can keep the sandbox small, control what the agent can access, and still let people explore what is possible.

**Interviewer:** At what point are we reinventing databases from first principles?

**Lamis:** Some of it does look familiar. But that is the point: once we know the primitives that work, it makes sense to codify them deterministically in the harness instead of pretending everything has to stay fully agentic.

**Interviewer:** How do you scale dreaming across different permission sets?

**Lamis:** You attach the right transcripts. Dreaming does not have to inspect everything in a time period. It can mirror the same permission model as the underlying memory store.

[applause]
