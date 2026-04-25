---
title: "How to Build a Company With AI From the Ground Up — Diana, Y Combinator"
date: 2026-04-25
description: "YC partner Diana argues AI should be your company's operating system, not just a productivity tool — covering closed-loop systems, software factories, queryable orgs, and the three new employee archetypes."
source: https://www.youtube.com/watch?v=EN7frwQIbKc
cover: https://img.youtube.com/vi/EN7frwQIbKc/maxresdefault.jpg
speaker: Diana, Partner at Y Combinator
format: Talk (Y Combinator)
language: English
purpose: Read-aloud article
tags:
  - youtube
  - ai
  - startups
  - yc
  - product
chunks:
  - text: "operating system your company runs on"
    type: chunk
    meaning: "公司运行的操作系统——AI 不是工具，而是整个公司的底层基础设施"
  - text: "closed loop"
    type: chunk
    meaning: "闭环——能持续采集反馈并自我调整的系统，相对于开环（open loop）"
  - text: "open loop"
    type: chunk
    meaning: "开环——没有反馈机制的执行系统，决策后不系统性地衡量结果"
  - text: "queryable"
    type: chunk
    meaning: "可查询的——整个组织的信息对 AI 可见可检索"
  - text: "legible"
    type: chunk
    meaning: "可读取的、透明的——信息结构化到 AI 能理解和使用的程度"
  - text: "software factories"
    type: chunk
    meaning: "软件工厂——人写规格和测试，AI agent 负责生成代码并迭代直到通过测试"
  - text: "test-driven development"
    type: chunk
    meaning: "测试驱动开发（TDD）——先写测试再写实现代码的开发方式"
  - text: "human middleware"
    type: chunk
    meaning: "人肉中间层——靠人工传递和转述信息的管理层级，AI 时代应该消除"
  - text: "directly responsible individual"
    type: chunk
    meaning: "直接负责人（DRI）——对某个结果负单一责任的人，苹果公司发明的管理概念"
    note: "缩写 DRI，强调一人一事、无处躲藏"
  - text: "token maxing"
    type: chunk
    meaning: "Token 最大化——用最高的 API 用量换取最大产出，而非扩张人头"
  - text: "skunk works"
    type: chunk
    meaning: "臭鼬工厂——企业内部独立运作、不受常规流程约束的小型精英团队"
  - text: "break your own priors"
    type: chunk
    meaning: "打破你自己的预设——亲手体验之后改变对可能性的认知"
---

Hi, I'm Diana, and I'm a partner at YC. Over the past few months, it's become clear to me that AI is not just going to change how quickly software gets built or what workflows get automated. It's going to fundamentally change the way startups should be run — from what roles will exist, to what products are possible to build.

In this talk, I want to discuss how founders should think about building an AI-native company, what roles their team should have, and what concrete internal practices they can adopt right now to move much faster.

## Productivity Is the Wrong Frame

Currently, most people talk about AI in terms of productivity. They'll talk about how it can make engineers more productive, or say "we need to add Copilot to existing workflows and ship more features." This framing misses the shift we're currently seeing, which is less about productivity boosts than **entirely new capabilities**.

The right person with AI tools can now build features that used to require an entire team — or were just impossible. Thinking about AI in terms of new capabilities has several implications for how founders should run their companies.

At a high level: AI should not be a tool your company just uses. **It should be the operating system your company runs on.** Every workflow, every decision, and every process should flow through an intelligent layer that is constantly learning and improving.

## Closed Loops vs. Open Loops

What this means concretely: every important process in your company should be captured by an intelligent closed loop.

A closed loop captures information, feeds it back into an intelligent system, and improves the process over time. If you've studied control systems, you'll know the difference. An open loop is controlled but has no feedback. In the old world, companies basically ran as open loops — you made a decision, executed it, and didn't always systematically measure the outcome and adjust the process. Open loops are inherently lossy.

A closed loop, by contrast, is self-regulating. It continuously monitors its output and adjusts its process to better meet the stated goal. Closed loops are extremely powerful for correctness and stability.

With self-improving agents, your company should run as a closed loop.

## Making Your Company Queryable

To build these closed loops, you need to make your entire company **queryable**. The whole organisation should be legible to AI. Every important action should produce an artifact that the intelligence at the centre of the company can learn from and use to self-improve.

This means:
- Recording your meetings with an AI notetaker
- Minimising DMs and emails in favour of channels agents can read
- Embedding agents throughout communication channels
- Building custom dashboards covering everything: revenue, sales, engineering, hiring, ops — all of it

Here's a concrete example. Take engineering management and sprint planning. If you have an agent with access to your Linear tickets, all your Slack engineering channels, customer feedback from emails or tools like Pylon and GitHub, high-level plans in Notion or Google Docs, sales call recordings, and daily standup recordings — that agent can analyse what was actually shipped in your previous sprint and how well it met customer needs. For real.

From there, you can go further. With full visibility into what shipped, what worked, and what didn't, agents can start looking ahead: proposing sprint plans for engineers that are far more predictable, accurate, and on track. The days of anchor-manager status rollups that are super lossy are gone.

Having managed engineering teams myself and now seeing this across multiple YC companies — this is a game-changer. What used to require constant coordination becomes legible and queryable by default. I've seen teams cut their engineering sprint time in half and get close to 10x more done in that time.

The overarching principle: to get their full capabilities, you need to provide models with as much context as you would provide an employee. When you do this, your company stops operating as an open loop where information is fragmented and manually interpreted. It becomes a closed loop system. Status, decisions, and outcomes are continuously captured and fed back into the intelligence layer. The result: a system that always has an up-to-date view of what's actually happening.

## Software Factories

There's also a new paradigm emerging for how the highest-velocity companies build product: **AI software factories**.

If you're familiar with test-driven development — TDD — this is the next evolution of that. With software factories, humans write a spec and a set of tests that define success, and then AI agents generate the implementation, write code, and iterate until the tests pass. The human defines what to build and judges the output. The actual code is the agent's job.

Some companies have already pushed this to the point where their repos contain no handwritten code — just specs and test harnesses. Strong DM's AI team is an example. Their goal was a system that essentially eliminated the need for a human to write or review code. So they built a software factory where specs and scenario-based validations drive agents to write tests and iterate on code until it meets a probabilistic satisfaction threshold. And it works.

This is how you achieve the thousand-X engineer that people talk about — by surrounding a single engineer with a system of agents that enables them to build things they would have never been able to build before. The era of the thousand-X, or even ten-thousand-X, engineer is here.

## No More Human Middleware

One implication of building your company this way — with AI loops everywhere, a queryable organisation, and software factories — is that the classic management hierarchy no longer makes sense.

In the old world, you needed middle managers and coordinators to route information inefficiently up and down an organisation. In the new world, the intelligence layer serves that purpose. If your company is queryable, artifact-rich, and legible to an AI, you should have almost no human middleware. This matters because your company's velocity is only as fast as its information flow. Every layer of human routing you can remove is a direct speed gain.

A great example is what Jack Dorsey is doing at Block. After going deep on the tools, he's come to the same conclusion many have: this is about more than incremental productivity gains. His view is that if you keep the same org chart and management structure, you've missed the shift entirely. The company itself has to be rebuilt as an intelligence layer — with humans at the edge guiding it, rather than routing information through it.

## Three New Employee Archetypes

Jack suggests every company going forward will have three employee archetypes:

**The Individual Contributor (IC) — the builder-operator.** This is someone who directly makes and runs things. In an AI-native company, this is not limited to engineers. Everyone builds — ops, support, sales. Everyone comes to meetings with working prototypes, not pitch decks.

**The DRI — the Directly Responsible Individual** focused on strategy and customer outcomes. This is not a classic manager. It's the person with clear responsibility for a result. One person, one outcome, no hiding.

**The AI Founder type.** This person still builds, still coaches, and leads by example. If you're the founder, this needs to be you — at the forefront, showing your team what massive capability gains look like. Not delegating your AI strategy to someone else.

With this structure, companies will be able to get outsized results with much smaller teams. **Maximising token usage, not headcount, will be the critical shift.** The best companies will be the ones that are token maxing.

Think about the trade-off this way: one person with AI tools can be the equivalent of what used to take a large engineering team at a pre-AI company. That means dramatically leaner engineering, design, HR, and admin teams. You should be willing to run an uncomfortably high API bill — because it's replacing what would have taken a far more expensive and inflated headcount.

## Startups Have the Edge

But don't just take my word for any of this. You cannot outsource your conviction on the power of these tools. You need to develop it yourself by actually sitting with coding agents and using them until you start to break your own priors about what is now possible to build.

If you are an early-stage founder, you have a huge advantage. You don't have legacy systems or thousands of people to retrain. You are small enough to build your company right from day one.

The opposite is true for existing companies. They have to maintain and grow a live product while unwinding years of standard operating procedures and core assumptions about how software gets built. Some large companies can achieve this by spinning up small internal skunk works teams that build AI-native systems from scratch, separate from the core business — Mutiny is a great example of this. But for most, every change to core processes risks breaking something that already works. Large companies will have a much harder time going AI-native.

Startups don't have that constraint. That's a major edge to take advantage of. You can design your systems, workflows, and culture around AI from the start — and as a result, operate a thousand times faster than the incumbents.
