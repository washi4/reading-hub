---
title: "Agents Need More Than a Chat — Jacob Lauritzen, CTO of Legora"
date: 2026-04-23
description: "Why complex AI agents need high-bandwidth, persistent interfaces instead of chat boxes — trust, control, verifiability, and the future of human-agent collaboration."
source: https://www.youtube.com/watch?v=XNtkiQJ49Ps
cover: https://img.youtube.com/vi/XNtkiQJ49Ps/maxresdefault.jpg
speaker: Jacob Lauritzen, CTO of Legora
format: Conference talk (AI Engineer)
language: English
purpose: Read-aloud article
tags:
  - youtube
  - ai
  - agents
  - product
chunks:
  - text: "flash banging"
    type: chunk
    meaning: "强烈闪光晃眼（这里指白色界面刺眼）"
    note: "俚语，源自游戏中的闪光弹"
  - text: "context rot"
    type: chunk
    meaning: "上下文腐烂/退化——agent 的上下文窗口因信息过多而开始遗忘关键内容"
  - text: "end-to-end"
    type: collocation
    meaning: "端到端，从头到尾全流程完成"
  - text: "verifier's rule"
    type: chunk
    meaning: "可验证者法则——如果一项任务容易被验证，AI 就能通过迭代解决它"
  - text: "post-train"
    type: chunk
    meaning: "后训练，在基础模型之上进一步强化训练"
  - text: "proxy for verification"
    type: collocation
    meaning: "验证的替代指标，用近似方法代替直接验证"
  - text: "instill their knowledge"
    type: collocation
    meaning: "将人的判断/知识注入（到 agent 的工作中）"
  - text: "YOLO mode"
    type: chunk
    meaning: "无监督全自动模式，放手让 agent 随意执行"
    note: "YOLO = You Only Live Once，引申为\"不管不顾地放开跑\""
  - text: "let it rip"
    type: formulaic
    meaning: "放手让它跑，全速启动"
  - text: "progressive discovery"
    type: chunk
    meaning: "渐进式发现——agent 在执行过程中按需获取信息，而非全部提前规划"
  - text: "elicitation"
    type: chunk
    meaning: "信息引出/征询——agent 主动询问人类以获取所需信息"
  - text: "high bandwidth artifacts"
    type: chunk
    meaning: "高带宽的协作载体（如文档、表格），相对于低带宽的聊天框"
  - text: "low bandwidth interface"
    type: chunk
    meaning: "低带宽界面，指聊天框这种一维、线性的交互方式"
  - text: "decision log"
    type: collocation
    meaning: "决策日志，记录 agent 在不确定时自主做出的决定，供人类事后审查"
---

It's 5:00 p.m. on a Friday, and there are just a few of you left — the rest have drifted toward the Friday beer. So I'll try to be a little quick. I'm here to talk to you about vertical AI, complex agents, and why I think they need more than just the chat.

## The Problem with Chat

If you've ever worked with a long-running complex agent, you've probably tried something like this. You're told to research something, draft a contract, make no mistakes. So the agent starts thinking, starts reading, launches a bunch of sub-agents, does web search, writes files, launches more sub-agents, does more reading, writes more files — keeps going, takes forever.

After 30 minutes, it gives you your contract. You take a look. Clause three doesn't look right. Did it make a mistake? Could it look at another document? "You're absolutely right."

Then you see it: **compaction**. That's when you know you can give up. It's going to forget everything. It's in the context rot state. Anyway, it continues, and you get a new contract. Was it only clause three that was changed? Probably not. And so you end up in this state. Not the greatest experience.

## Who We Are

My name is Jacob. I'm the CTO of Legora. We are a collaborative AI workspace for law firms — a vertical AI company. We have more than 1,000 customers across more than 50 markets. We've raised a fair bit of money and we're growing extremely fast — I'm being told maybe the fastest in history. We're also hiring engineers in London, so if anyone's interested in joining this journey, please come talk to me after.

## The New Economics of Production

Our goal, and the goal of most vertical AI companies, is to make agents complete more and more complex work end-to-end. What it means to do that has changed a lot in the past 6 to 12 months because there are new economics of production.

It used to be that if you wanted to complete end-to-end work, you'd focus on just doing the work — that was the main thing, actually getting it done. But today things look a little different, because right now **planning work and reviewing work is the new bottleneck**. Doing the actual work is extremely cheap and easy. But now you have to spend time on planning, gathering non-functional requirements, writing specs, and you have to spend a lot of time reviewing the work. And if anyone's reviewed big PRs on GitHub, it really sucks. It's extremely painful.

Maybe, if you're fully AI-pilled, you just get your AI agents to review their own work with no humans involved. Maybe it works, maybe it doesn't.

## The Verifier's Rule

When thinking about completing complex work — the planning stage, the doing stage, and the reviewing stage — the verifier's rule is a useful frame. It was coined by Jason, and it states: if a task is solvable and easy to verify, it's going to get solved by AI.

He was primarily talking about foundational models — if you can make something easy to verify, you can set up an RL environment, post-train on it, and the model will solve it. But I think it also applies to agents. If you can make a task verifiable, you can run an agent in a loop and tell it, "Hey, you did this wrong, please fix it," and it'll eventually get there.

Different industries sit at different places in this spectrum. And within a single vertical, tasks are at different places too.

Take legal. Checking definitions in a contract — super easy to verify, super easy to get done. Writing a contract — very easy to solve, but actually extremely difficult to verify. When you write a contract, the only time you can truly verify whether the language works is if it goes to court and a judge rules on it. Litigation strategy is basically impossible to verify. If you ask five lawyers what the right strategy is for a given case, you'll get five different answers. No objective truth means it's very hard for AI to solve.

Similarly with coding: some parts are easy, but building a successful consumer app is very difficult to verify.

## Trust and Control

When we think about involving humans where they really matter and letting agents do the work they can handle, two things are important: **trust** and **control**.

Control is how effectively a human can instill their knowledge into the work the agent is doing — how well can you steer it? Trust is about how much you need to review. If you have very low trust, you're going to look at every single agent trace and see exactly what it did. If you have very high trust, you won't look at it at all.

### Increasing Trust

To increase trust, you have a few options.

First, you can **bring a task down in the difficulty spectrum**. A coding example: if you want to implement a feature, give the agent browser access and set up test-driven development. Suddenly it's a verifiable task and the agent will do much better.

Second, you can **look for a proxy for verification**. For contracts, take a look at your previous golden contracts — the ones you know work well — and set up a test: is the new contract similar to the old one? That's a proxy that allows the agent to do a much better job.

Third, you can **decompose tasks**. Instead of asking an agent to write a whole contract, turn that into a bunch of smaller tasks. Leave the high-judgment calls — picking a risk profile, choosing precedent documents, setting a negotiation stance — to the human. Let the agent handle what's easy to verify: apply formatting, run definition checking (essentially linting: are all definitions used? are all used terms defined?). This is something you can build, and the agent can execute it extremely well.

Fourth, you can **add guardrails**. Guardrails increase trust by limiting what the agent can do. Instead of having access to everything, you say: you can only edit these three files, you can only read from this directory, you can only search these websites. By constraining scope, you build more confidence that it won't do anything unexpected.

A familiar example is Claude Code. At very low trust, it asks you every single time it wants to do anything — which makes it nearly useless. At the high-trust end of the spectrum, you just YOLO mode it, let it rip, and hope it doesn't delete your production database.

### Increasing Control

Now, control. How do we increase it?

Complex agent work can be thought of as a tree of tasks — a DAG. Here's an example: I want the agent to write a report on a bunch of employment contracts. It plans to research the organisation first, then review the contracts clause by clause, and finally draft a report.

**Pure execution** — giving the agent one instruction and waiting — is extremely low control. I can only impose my judgment at the root level. The agent does all the work, comes back at the end, and then I can try to redirect it. That's basically the painful example I showed at the beginning.

**Planning** is better. Before the agent starts, it outlines its approach and we align on what it should do. "Take exactly these steps, look for these clauses, review these things." It gives you more control and lets you steer the agent upfront. The problem is that to give good planning input, you basically have to do all the thinking yourself. It's inefficient, and it's impossible for the agent to truly know whether it has all the information it needs. If one of those contracts has a special clause, the agent wouldn't know to look for it at the planning stage. Planning is like working with a co-worker who comes to you to discuss the approach, you align with them, and then you never hear from them again until they deliver the final document. Not a great way to collaborate.

**Skills** are really, really good. They allow you to encode human judgment directly into the nodes of work in the task tree. You can say: whenever you review a confidentiality clause, do it this way. The really good thing about skills is that they allow for contingencies. If there's a special EU law that applies to a termination clause, I can put that in a skill, so the agent knows how to handle that special case whatever happens when it actually does the work. Skills also enable progressive discovery — whatever the agent encounters, it knows how to pick it up and handle it.

The problem is you don't have skills for everything.

**Elicitation** — asking the user — is the next step. You may have skills, but for cases those don't cover, the agent comes to you and says: "Here's a thing I don't know how to handle. What do you want me to do?"

What you don't want is for the agent to be blocked waiting for an answer. The ideal implementation: tell the agent that if it's unsure, it should make a decision, unblock itself, but write the decision to a **decision log**. The human can then review the decision log afterwards and reverse any decisions that were wrong.

## Chat Is Not the Right Interface

Now, the right UX for all of this — if you imagine that work tree being ten times bigger, a hundred times bigger — is definitely **not chat**. You don't want to open a chat that's infinitely long, where you have to answer 50 questions without the right context to do so.

Chat is one-dimensional. It's a very low bandwidth interface. It tries to collapse an entire work tree into a single linear thread.

So what's a better interface? I think humans and agents should collaborate in **high bandwidth artifacts** — things that are persistent, that feel natural for the kind of work being done, and that look different from industry to industry and vertical to vertical.

An example from us is a **document**. That's a durable interface where collaboration makes sense. You can highlight clause three and ask the agent to change only clause three. You can add comments, tag agents, tag collaborators, hand off parts of the document to specialist agents.

Another example is our **tabular review**. I ask the agent to do a contract review, and instead of streaming text at me, it spins up a structured table — a known primitive our users are familiar with. It reviews all the contracts and flags a few items it wants my take on. I can see at a glance where the problems are, quickly instill my judgment, and kick off the rest of the agent work from there.

## Language Is Universal — But Agents Aren't Human

What we're seeing right now is a convergence of UI. Chat boxes as input are great — they're extremely flexible and you can do a lot with them. But you don't want chat to be your main mode of collaboration with a complex agent.

Language is the universal interface. It's what people use to communicate. You can do almost everything with words. But agents aren't humans. A few minutes ago I was describing our org chart to a potential hire, and I was limited to language. I wished I could just draw it up and have them interact with it — but I can't, because I'm a human.

Agents are not limited that way. So we should not constrain them to human language.

Thank you. [applause]
