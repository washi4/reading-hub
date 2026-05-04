---
title: "Agent Harness vs Everything Else: The Real Difference"
date: 2026-05-04
description: "A clear breakdown of what an agent harness actually is, how it differs from frameworks like LangChain, and the nine components every modern harness needs."
source: https://www.youtube.com/watch?v=nWzXyjXCoCE
cover: https://img.youtube.com/vi/nWzXyjXCoCE/maxresdefault.jpg
speaker: Prompt Engineering (YouTube channel)
format: Technical explainer
language: English
purpose: Read-aloud article
tags:
  - youtube
  - ai
  - engineering
  - agents
  - llm
chunks:
  - text: "fixed architecture"
    type: collocation
    meaning: "固定架构；不需要人来组装的预设结构"
  - text: "one-shot text generators"
    type: chunk
    meaning: "一次性文本生成器；给一个问题，输出一个答案就停了"
  - text: "think of the model as the engine and the harness around it as the car"
    type: sentence-frame
    meaning: "把模型想象成发动机，把 harness 想象成整辆车"
  - text: "wire them together"
    type: chunk
    meaning: "把各个组件连接起来，手动组装"
  - text: "ships a working agent"
    type: chunk
    meaning: "直接交付一个可运行的智能体，开箱即用"
  - text: "span, restrict, and collect"
    type: chunk
    meaning: "展开子任务、限制权限、收集结果——子智能体的三步模式"
  - text: "non-negotiable"
    type: chunk
    meaning: "不可或缺的，必须有的"
  - text: "append-only"
    type: chunk
    meaning: "只追加不修改；一种安全的持久化方式"
  - text: "prefix caching"
    type: collocation
    meaning: "前缀缓存；LLM 推理中对重复 system prompt 的优化"
  - text: "life cycle hooks"
    type: chunk
    meaning: "生命周期钩子；在工具执行前后注入自定义逻辑"
  - text: "at dispatch time"
    type: chunk
    meaning: "在调度时刻；工具被调用的那一刻"
  - text: "destructive"
    type: chunk
    meaning: "破坏性的（操作）；如删除文件、执行高权限命令"
---

Everybody talks about agent harnesses, but what exactly is a harness? Even people who are actively building agents can't always give you a clean answer. The word gets thrown around constantly, but nobody really agrees on what it means.

In this piece, I want to do three things: define what a harness actually is (and just as importantly, what it's not), walk through nine components that make a modern harness, and then build a tiny one in Python so you can see exactly what's going on inside.

## What Is a Harness?

In simple terms, a harness is a fixed architecture that turns a model into an agent. Modern LLMs are just one-shot text generators. You ask a question, it answers and stops. A harness is what gives it the ability to take action, see the consequences, and keep going until the problem is actually solved. Think of the model as the engine and the harness around it as the car. That's what makes an agent.

A great example is agentic coding tools like Codex, Cursor, Claude Code, and Windsurf. These are all harnesses. Each one started from a concrete problem — making a model write and edit code across a real repository — and they have converged on remarkably similar architectures.

## Harness vs. Framework

Before we get into the components, let's clear up a common confusion: the difference between a harness and a framework.

Frameworks are things like LangChain, LangGraph, AutoGen, and CrewAI. These are **not** harnesses. People use these terms interchangeably right now and it's getting confusing.

A **framework** gives you abstractions: state graphs, chains, memory connections, retrievers. You as the human architect have to wire them together. The fundamental assumption is that you will configure these pieces.

A **harness** comes from the opposite direction. There's no assembly step. It ships a working agent. Everything comes wired together. Another way to put it: a framework is built for a human to assemble an agent. A harness is built for the agent itself to complete a task. You provide the goal; the harness handles the rest.

## The Nine Components

### 1. The While Loop

This is the foundation — the outer iteration loop. At its core, a harness is a while loop. The model reads its system prompt, decides which tool to call, runs the tool, feeds the result back into the context, and loops again. This process keeps repeating until the model produces a text-only response or hits a maximum iteration cap. Think of this outer loop as the engine that runs everything.

### 2. Context Management

On every turn the conversation tree grows — more user messages, more tool calls, more tool results — until you hit the context limit of the LLM. The harness has to decide what to keep verbatim, what to summarize, and what to throw away.

In Claude Code's case, the budget used to be around 200,000 tokens; now it's up to 1 million for Opus. When you reach roughly 80–90% of the limit, a compaction triggers: the most recent messages stay in full, and everything older gets summarized. This compaction is critically important and can have serious consequences if not done carefully.

### 3. Skills and Tools

**Tools** are the primitives: read a file, edit a file, run bash, search code. They're universal — any harness needs them.

**Skills** are a layer on top. They encode organizational knowledge and are usually stored in markdown files. Skills are specific to your team and your workflow.

Then there's the **registry** — it tracks what's available, what permissions each thing needs, and how calls get dispatched.

### 4. Sub-Agent Management

At some point a task gets too large or too parallel for a single conversation thread. The harness creates sub-agents that work in isolation. Each sub-agent gets its own session, its own restricted set of tools, and a focused system prompt: "You're working on this specific task." The pattern to reach for is: span, restrict, and collect.

### 5. Built-in Skills

Every harness ships with a baseline set of skills that work out of the box: file operations (read, write, edit, search), cell execution, code navigation, and similar primitives. These are non-negotiable. If your agent cannot read or edit files, it isn't a coding agent.

Beyond the primitives, modern harnesses also ship higher-level skills: how to make a Git commit, open a pull request, run tests and parse results. Some of these will be specific to the harness vendor.

### 6. Session Persistence (Memory)

A long agent session is stateful. If the process crashes, you need to resume from where you left off. Modern harnesses handle this elegantly with **append-only** JSON or markdown files. Every message, every tool result, every compaction event gets written as one line. The append-only design means two runs of the harness can share the same log without stepping on each other, and if the harness dies mid-run, everything already written is safe on disk.

### 7. System Prompt Assembly

This one surprises most people: the system prompt is not a static string. It's a pipeline that walks ancestor directories looking for specific types of instructions — `AGENTS.md`, `CLAUDE.md`, memory files — and assembles them dynamically at runtime.

One important caveat: if you dynamically introduce components into the system prompt, you break **prefix caching**. To protect caching, keep the static part first and append dynamic content second. The order matters.

### 8. Life Cycle Hooks

Hooks are the extensibility layer. They let you inject custom logic before or after a tool runs without touching the harness itself.

A **pre-tool hook** fires before execution. It receives the tool name and input and can allow, deny, or modify the call. A **post-tool hook** runs after and can inspect the results — it can't block anything, but it's valuable for auditing, logging, and observability.

Hooks are also how enterprises adopt harnesses today. They use pre-tool hooks to enforce policy, and post-tool hooks to feed audit trails into existing observability stacks.

### 9. Permissions and Safety

This is the layer that makes the difference between a useful tool and a dangerous one. Modern harnesses define a hierarchy of permission modes: read-only, workspace write, full access. Each tool declares the minimum permission it requires, and the harness enforces that **at dispatch time** — before the tool ever runs.

For tools like bash, the harness classifies commands dynamically. `ls` and `grep` stay at read-only. `rm`, `sudo`, or `shutdown` jump straight to full access, determined by parsing the command string.

On top of static rules, the agent can pause and ask: "Should I run this?" Before executing anything **destructive**, you want an interactive approval layer built into the harness. That's the safety guarantee.

## A Minimal Python Implementation

The best way to understand a harness is to build one. Here's what a minimal reference implementation looks like in Python.

**The main engine** is the while loop that assembles the system prompt and starts iterating. On every loop: compact the context if it's grown too large, make a model call, check whether it returned a text-only response or a tool call, dispatch accordingly, and append the result. Cap the total iterations so the loop can never run forever.

**Context management** in the simplest form is a compaction function: if the conversation history grows beyond a threshold, summarize the older messages into a single block and replace them. More advanced techniques exist, but this is the reference baseline.

**The tool and skills registry** uses a small data class for each tool: a name, a required permission level, a handler function, and a one-line description. The registry is a dictionary from tool name to that record. Skills are registered the same way — they're just tools whose handler reads a markdown file at invocation time.

**Sub-agents** are defined by archetype: exploration, general, and verification. Each archetype has its own permission level, restricted tool list, and focused system prompt. The harness spawns them for parallel or isolated work.

**Session memory** uses an append-only file. Every event gets written as one line of JSON, flushed immediately. The replay method reads the file back line by line to reconstruct the session. If the harness crashes after a write, that event is already safe on disk.

**System prompt assembly** reads `AGENTS.md`, `CLAUDE.md`, or any other memory files from disk and appends them to the static base prompt. Keep the static part first — the dynamic content goes after, to preserve prefix caching.

**Hooks** are two-stage: a pre-tool hook that can allow or deny the call, and a post-tool hook that sees the output and records it for observability. Neither touches the core loop.

**Permissions** enforce at dispatch: each tool declares its minimum required level, and the harness checks before running. For bash specifically, the harness parses the command string and classifies it dynamically — safe read operations stay at read-only, anything destructive triggers a full-access requirement and an interactive approval prompt.

---

Those are the nine components every harness needs: iteration loop, context management, skills and tools, sub-agent management, built-in skills, session persistence, system prompt assembly, life cycle hooks, and permissions. Get these right, and you have a solid foundation for building agents that actually work in production.
