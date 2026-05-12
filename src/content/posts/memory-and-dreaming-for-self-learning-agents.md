---
title: "Memory and Dreaming for Self-Learning Agents"
date: 2026-05-12
description: "Anthropic PM Mahes walks through memory as a file system for agents, optimistic concurrency for multi-agent teams, and Dreaming — a new out-of-band process that synthesizes learnings across sessions to make tomorrow's agents smarter than today's."
source: https://www.youtube.com/watch?v=RtywqDFBYnQ
cover: https://img.youtube.com/vi/RtywqDFBYnQ/maxresdefault.jpg
speaker: Mahes, Product Manager, Anthropic Platform Team
format: Conference talk
language: English
purpose: Read-aloud article
tags:
  - youtube
  - ai
  - agents
  - anthropic
  - memory
chunks:
  - text: "self-learning agents"
    type: collocation
    meaning: "自我学习的智能体；能从经验中不断积累知识的 AI agent"
  - text: "out of band"
    type: chunk
    meaning: "带外；在主任务流程之外异步运行，不阻塞也不影响正在进行的工作"
  - text: "hot path"
    type: chunk
    meaning: "热路径；系统中对延迟最敏感、最频繁执行的关键路径"
  - text: "optimistic concurrency"
    type: collocation
    meaning: "乐观并发控制；允许多个 agent 并发写入，但在提交前用哈希验证是否会覆盖他人的更改"
  - text: "short circuit"
    type: chunk
    meaning: "短路；跳过重复的调查步骤，直接利用已有结论来节省时间"
  - text: "load-bearing"
    type: chunk
    meaning: "承重的；对整体结果起到关键支撑作用的（工程比喻）"
  - text: "attribution metadata"
    type: collocation
    meaning: "归因元数据；记录某次变更是由哪个 agent、哪个 session、在何时做出的"
  - text: "version history"
    type: collocation
    meaning: "版本历史；对每次内存更新的完整审计日志，可以回溯到任意时间点"
  - text: "test-time compute"
    type: collocation
    meaning: "推理时算力；在推理阶段额外投入计算资源，用来探索更多可能性以提升输出质量"
  - text: "amortize this effort"
    type: chunk
    meaning: "摊销这份工作；让前期的投入（如建立索引）惠及后续所有使用者，平均到每人的成本极低"
  - text: "out-of-date"
    type: chunk
    meaning: "过时的；不再准确反映当前状态的信息"
  - text: "backfill"
    type: chunk
    meaning: "回填；将历史数据或补充信息填入已有结构中，使其更完整"
---

Hey everyone. My name is Mahes and I'm a product manager on the platform team here at Anthropic. Over the past year and a half, I've gotten to work on primitives like MCP and Skills. Today I want to talk about the primitive I'm most excited about next: memory.

I'll cover why we think memory is so important and why we've been spending so much time on it at Anthropic, how we think about designing memory systems built for frontier agents, and I'm excited to introduce Dreaming — a brand new product we're launching today in research preview in the Managed Agents API.

## The Arc of Agent Primitives

Model capabilities have improved really quickly over the last couple of years. Agents are now capable of tasks that take many hours and can run for almost a full day at a time. As models and agents have improved, we've invested in building increasingly higher-level capabilities and primitives — things that get out of the model's way and give agents access to more of their environment.

We launched MCP, which gives agents access to external tools and data. We launched harnesses like Claude Code and the Agent SDK. In October, we launched Skills, which let agents pick up brand-new capabilities that other agents or human users have designed for them. Each primitive has let agents do increasingly powerful things for longer periods of time.

But something is still unsolved: **continuous self-learning and context management over long-horizon tasks**. That's the gap that memory addresses.

With memory, agents can learn about:
- The **tasks** they work on — success criteria, common mistakes, strategies that are or aren't working
- Their **environments** — codebases, files, assets they're constantly interacting with
- **Other agents** in the same environment — sharing learnings, noticing what's going wrong elsewhere, incorporating that into their own understanding

That last point is the one I've been most excited about. Self-managed memory is going to be essential in large and complex multi-agent systems — a swarm of agents working in a similar environment on discrete tasks, essentially building up their own shared model of the world over time.

## Memory in Managed Agents

A few weeks ago, we launched memory in Claude Managed Agents in public beta. This gives developers a frontier memory system that works out of the box to maximize intelligence by default, support systems of many agents running concurrently in the same environment, and give enterprises the flexibility and control they need to run this in production.

We've already heard from teams building on this. Rockutin mentioned that deploying memory helped them drop first-pass mistakes in their internal knowledge agents by 90%, because agents were able to catch mistakes and share them with the next iteration. That also led to better token efficiency, lower costs, and better latency.

### Memory as a File System

Early versions of memory at Anthropic were pretty constrained. CLAUDE.md was an early form — an agent could leave notes for itself, sometimes the user would add notes in the same file. Then we launched a memory tool in our SDKs: a well-specified tool call with specific parameters and output formats.

As agents have improved, we've tried to get more and more out of Claude's way and delegate more decision-making to the model without over-constraining the design. We made a similar move with Skills — we realized agents can manage a virtual environment and their own file system, so why not let them manage memory the same way?

Memory in Claude Managed Agents models memory as a **file system** for Claude: a series of files with a specific hierarchy and format that Claude manages and updates on its own using familiar tools like bash and grep. It can keep memory organized and update it as it works on a task.

This also tracks with what we're seeing in the latest models. Claude Opus 4.7 is significantly better at discerning what content is worth remembering, at deciding the right file structure, and at keeping things organized inside a file system — using the same bash and grep tools that already make Claude so good at agentic coding.

### Permission Scopes

When hundreds or thousands of agents are running in parallel and sharing state, you need to let agents mix and match different memory stores with different access levels.

One agent might have **read-only** access to an org-wide knowledge store — a set of best practices, runbooks for handling common tasks. And it might have **read-write** access to a working memory store that's updated frequently based on what it's currently doing.

This permission scoping is a core property of memory in Managed Agents.

### Optimistic Concurrency

If hundreds or thousands of agents are interacting with the same memory state simultaneously, you can't let them clobber each other's updates. We implemented **optimistic concurrency**: one agent uses a content hash to check whether it would overwrite another agent's changes before making an update. It's a lightweight mechanism that scales to very large multi-agent systems without requiring locks or coordination overhead.

### Developer and Enterprise Control

The most sought-after feature from customers was **version history** — a complete audit log of every time memory was updated. Developers can see an entire history and, importantly, agents themselves can access that same audit log in the future to understand what changed and when.

Alongside that comes **attribution metadata**: which agent made an update, at what time, in which session. This makes memory predictable and in the developer's control.

We also built a **standalone portable API** for customers running bespoke memory pipelines outside of Managed Agents — for example, PII scanning to make sure sensitive content doesn't end up in memory, cleaning up memory in a separate pipeline, or cloning it to external systems. We didn't want to lock anyone into a closed system.

## The Layers of a Frontier Memory System

Taking a step back, we've been building up different layers:

- **Storage layer** — where data is stored, what metadata and attribution live alongside it
- **Structure and content layer** — modeling memory as files in a file system; Skills as procedural memory with a lightweight spec
- **Process layer** — how often memory is updated, what triggers updates, what sources it draws from

Memory in Managed Agents solves a lot of this. But as we scaled up into more complex multi-agent systems, we saw limitations. Sessions were missing learnings that other agents had already figured out. Common mistakes and shared patterns were appearing across multiple agents working in the same environment, but each agent only saw its own slice. Memory stores were becoming stale — not fresh, not holistic.

That's where Dreaming comes in.

## Dreaming: A New Primitive for Memory Quality

Dreaming is a batch, asynchronous process that looks for patterns and mistakes across your recent agent sessions and their transcripts, and automatically produces organized, up-to-date memory content.

We've worked with a few customers in early testing. Harvey, when they deployed Dreaming in one of their legal benchmarks testing realistic legal scenarios, saw a **6x increase in task completion rate**. We're excited to see how other customers use this when they start testing the research preview.

### How Dreaming Works

Dreaming is an **out of band** process — it runs separately from the work happening within a specific session on a specific task. You can kick it off periodically via the console or API on a cron schedule, or plug it in to run after your agents finish a task and spin down, saving learnings before the session closes.

Dreaming comprehensively looks through recent transcripts, finds common mistakes that many agents are making — failed tool calls, inefficient strategies — and identifies what's working. It then produces an updated memory state as a diff that you can apply immediately, or review manually via the API before applying.

The ultimate goal: **continuous self-learning** where the next day's agents automatically get better based on the work and learnings of the previous day.

### Why Out of Band Matters

From a design perspective, there are a few reasons we got excited about Dreaming as an out-of-band process.

**Multi-agent perspective.** When a single agent reads and writes memory, it has the perspective of itself, its own context, and its own task. Dreaming goes a step above that — it looks at multiple agents at once to find shared patterns and learnings that a single agent would never notice from its own limited view.

**Separation of objectives.** We've found consistently that it's important for agents to have discrete, clear objectives as they start working on a task. Dreaming lets us separate the memory quality objective from the task completion objective that most agents already have. The agent does its job; Dreaming worries about keeping memory healthy.

**No latency on the hot path.** Because Dreaming runs in the background and out of band, it does this work without adding any latency to an agent's existing task.

### Scaling Large Memory Systems

Today, most memory deployments are localized — a specific user, a specific task, maybe a small team. But agent systems are quickly reaching enterprise scale. Within Anthropic and within the enterprises we work with, there are already hundreds or thousands of agents running concurrently, sharing state. That effectively turns a memory store into a large knowledge base.

To support this, we need ways to let Claude scale memory systems to be very large while keeping them fresh, organized, and not too token-intensive. Dreaming lets us do this by following similar scaling laws to what we've seen elsewhere — using additional compute and additional effort to keep these systems organized.

One useful analogy is **test-time compute** and thinking models: giving models the ability to explore and try different things, to spend more tokens, leads to much better final outcomes. Dreaming is similar — a dreaming agent spends more tokens to keep the memory system well-organized and up-to-date.

Another analogy is a search index: there's upfront effort to produce a high-quality, up-to-date index, which then makes retrieval fast and efficient. Dreaming creates and curates that index, and then lets us **amortize this effort** across all the downstream agents reading from the shared memory store.

## Putting It Together: A Live Demo

The demo we showed was a site reliability engineering scenario — an SRE agent system that watches for incoming alerts and reacts to them, spinning up specific agents to do triage work or submit PRs.

Each of these agents is equipped with two memory stores:

1. **Org-wide knowledge** (read-only) — runbooks, SLO guidelines, a list of who owns what. This is stable; we don't want agents casually rewriting it.
2. **SRE working memory** (read-write) — updated constantly as agents learn from the environment.

When a P1 alert comes in from the dispatch service, an SRE agent spins up and begins investigating: CPU utilization, traffic patterns, recent PRs. It writes down its learnings to the SRE memory store.

A couple of minutes later, the same alert pages again. A different SRE agent spins up with access to the same memory store. The first thing it sees is a note: "We already investigated this. Here's what we found. Here's how you can **short circuit** what you're looking at." It saves significant time and tokens that would otherwise go to re-investigating the same alert from scratch.

The memory store's **version history** shows every update: what changed, which agent made the change, when, and which session. The **optimistic concurrency** precondition hash is also visible — it lets agents verify they're not overwriting another agent's concurrent update before committing.

### What Dreaming Found

After running a Dreaming job over the past seven days of sessions touching the SRE memory store, it produced a diff with several updates:

- It noticed that multiple agents were triggered exactly 60 seconds after an upstream CPU spike — a pattern no individual agent had recognized because they each only saw their own session. Dreaming inferred there might be inefficient retry logic amplifying the original issue and left a note for future agents.
- It consolidated five duplicate entries from previous agents into a single, clean entry.
- It removed a stale entry that transcripts showed was no longer relevant.
- It added a **verification and backfill** note: "At this point in time, based on the transcript I reviewed, this memory entry is accurate — I was able to verify it against actual agent behavior."

That last piece — verification backfill — is something individual agents working on a task rarely have time to do. Dreaming does it systematically, in the background, so future agents can trust the memory state.

## What Comes Next

Memory and Dreaming together form what we're calling a frontier memory system — at least so far. Memory on one side: a real-time primitive for agents to immediately read and write things as they work. Dreaming on the other: a comprehensive process that verifies, organizes, and enriches that memory based on everything agents have done.

Dreaming is the bridge between intermediate working memory and the large-scale knowledge bases we think are going to be really prominent over the next few months.

I think over the next couple of months, we're going to start seeing agents that run for days at a time. Memory is going to be a **load-bearing** part of what makes that possible. I'm really excited to see what everyone builds with memory and dreaming in the Claude Managed Agents API. You can get started today.

Thank you.
