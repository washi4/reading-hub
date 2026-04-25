---
title: "How to Make Claude Code Your AI Engineering Team — Garry Tan, Y Combinator"
date: 2026-04-25
description: "YC president Garry Tan demos GStack, his open-source harness that turns Claude Code into a full AI engineering team — with office hours, adversarial review, design brainstorming, and a headless browser built in."
source: https://www.youtube.com/watch?v=wkv2ifxPpF8
cover: https://img.youtube.com/vi/wkv2ifxPpF8/maxresdefault.jpg
speaker: Garry Tan, President & CEO of Y Combinator
format: Demo talk (Y Combinator)
language: English
purpose: Read-aloud article
tags:
  - youtube
  - ai
  - coding
  - agents
  - yc
chunks:
  - text: "agent era"
    type: chunk
    meaning: "Agent 时代——AI 以自主 agent 形式完成工程工作的新阶段"
  - text: "thin harness fat skills"
    type: chunk
    meaning: "薄脚手架、厚技能——框架本身极简，真正的能力封装在各个技能模块里"
  - text: "silently breaks"
    type: collocation
    meaning: "悄无声息地出错——代码看起来正常但实际已损坏，没有任何报错提示"
  - text: "out of the box"
    type: formulaic
    meaning: "开箱即用，不需要额外配置"
  - text: "wandering"
    type: chunk
    meaning: "（模型）漫游/发散——没有明确约束时 AI 容易偏离方向乱猜"
  - text: "forcing questions"
    type: chunk
    meaning: "逼迫性提问——迫使你真正思考核心假设的问题"
  - text: "wedge strategy"
    type: chunk
    meaning: "楔子策略——先用一个低门槛功能切入市场，再扩展到更大业务"
  - text: "adversarial review"
    type: collocation
    meaning: "对抗性审查——主动寻找方案漏洞和弱点的评审方式"
  - text: "on rails"
    type: chunk
    meaning: "按预定轨道走——指死板的流程，没有弹性"
  - text: "let the agents cook"
    type: chunk
    meaning: "让 agent 跑起来、放手让它干（引申自 let it cook）"
  - text: "supply chain attacks"
    type: collocation
    meaning: "供应链攻击——通过污染依赖包或第三方组件来入侵软件"
  - text: "let it rip"
    type: formulaic
    meaning: "放手去做，全速启动"
---

Hi, I'm Garry — president and CEO of Y Combinator. I'm also an engineer who spent the first decade of my career building software full-time. I studied computer systems engineering at Stanford, then was employee number 10 at Palantir, where I was engineer, designer, and product manager all at once. I co-founded Posterous, a microblogging platform that sold to Twitter. I built the first version of Bookface, YC's internal social platform and knowledge base. Basically, I've written a lot of code in my career.

And I'm here to tell you: we are in a completely new era of building software. The **agent era**.

## Why Teams Beat Solo Models

It turns out the way to get agents to do real work is the same way humans have always done it — as a team, with roles, with process, with review. I built GStack to encode this three weeks ago, and it now has more GitHub stars than Ruby on Rails.

I've coded more in the past two months than I did in all of 2013 — which is the last time I worked really, really hard as an engineer. I started playing with Claude Code back in January, after hearing people like Andrej Karpathy and Boris Cherny say they weren't manually writing any code anymore. I got completely hooked.

Along the way, I've essentially rebuilt all of Posterous — what took two years, $10 million, and ten engineers to build.

But out of the box, the model wanders. It doesn't know your codebase well, so it guesses. And guessing at that scale is how you get plausible-looking code that silently breaks.

The bottleneck here is not the model's intelligence. As long as you set the models up right, they are already smart enough to do extraordinary work on your codebase. The bottleneck is scaffolding — and most scaffolding is too thick. **The scaffolding should be trivially thin.**

GStack is my implementation of the thin harness, fat skills approach.

## What GStack Is

GStack is an open-source repo that turns Claude Code into an AI engineering team. It does this through skills — modular commands that act like a team of specialists.

There are 28 different commands now, and the repo has more than 70,000 stars. Some users report spending 80–90% of their Claude Code time in just three skills: Office Hours, Plan, and CEO Review.

Let me show you how it works.

## Office Hours: YC Distilled

The best way to get started with GStack is through the **Office Hours** skill. This is the distilled version of thousands of hours that the 16 YC partners have spent — many, many years honing and perfecting — now compressed into code. Call it a 10% strength version of what we do at YC every day.

It starts by asking six forcing questions to help you reframe your product before you start building.

Here's a live demo. Today we're going to make a tax app — something that goes into your Gmail and pulls out all your 1099s. It's tax day.

The skill kicks off by asking: *"What's the strongest evidence that you have that someone actually wants this?"* This is one of the most important questions to ask yourself when deciding whether to work on something. I answer: I have more than five bank accounts and hunting down all my 1099s every year is genuinely painful. My accountant sends me annoyed emails.

From that conversation, the model figures out: the user isn't just thinking about document aggregation. They're seeing a funnel. The hook is "we'll find all your 1099s for you." The expansion is: now that you have your docs, let's get your taxes prepared — matchmaking and lead generation for tax preparers. It's a classic wedge strategy. You can charge $2 to $5 for 1099 aggregation, but you can charge a percentage of the transaction with a tax preparer, which might be 10x more.

This is one of the most fun parts of using Office Hours and GStack — it's not an on-rails experience. It's a conversation. If you just typed your original prompt directly to Claude Code, it would just go do it. It would find your 1099s. But it wouldn't think: *Who is the user? What is the business model? What's the pain point? Who wants this?* That's the kind of structured thinking we do every day with founders — and so does this skill.

## Adversarial Review

After Office Hours produces a design doc, GStack runs a multi-step adversarial review — it tries to put your idea through the paces, finds issues, and auto-fixes them where it can.

In our demo: no failure handling. No privacy section. 2FA handoff had no proposed solution. The skill caught 16 issues automatically and fixed what it could. Our doc improved from a score of 6 out of 10 to 8 out of 10, with three remaining issues to address later.

## Design Shotgun

After locking in the adversarial review, we jump to **Design Shotgun** — one of my favourite tools. It identifies all the views your app needs, you pick one to design, and then it farms out generation to multiple models (including OpenAI's image generation) and returns three visual directions.

For the tax app, we got three dashboard options:

- **Option A** — Command center style. Dense, data-forward. A Linux hacker would love it.
- **Option B** — Friendly and card-based, with progress rings. Good for normal people. My pick — five stars.
- **Option C** — Too complicated. Hard pass.

We go with B. Variant locked in. The whole thing takes about sixty seconds. If you don't like any of them, you regenerate. It's visual brainstorming at the speed of thought.

## The Browser Is Built In

One of the real magic moments for me was realising I needed to automate QA. Once the agent is doing all the planning, design, and coding, I found myself sitting there doing QA — probably the least fun part of software development. So I tried to automate that too.

Claude in Chrome MCP is one of the worst pieces of software I've ever used. Every action caused it to think and think. There was crazy context bloat. Often it wouldn't do anything, but it would still take two to three seconds when it was working.

So I wrote a CLI wrapper around Playwright and Chromium — a full headed and headless browser baked into GStack. Now Claude Code can actually use the browser: take screenshots, do complex interactions, click things, fill forms, download media, run regression tests, assess real browser bugs in JavaScript and CSS.

That's the **browse** tool. And it's how browser automation — like our tax app flow where the AI logs into bank portals and downloads PDFs — actually becomes viable.

## Running at Scale

Here's how I actually work day-to-day: I run 10 to 15 parallel Claude Code sessions at the same time.

In one session I might be running Office Hours on a brand new idea. In another, I'm evaluating incoming open-source PRs from the community. I sit on about 400 open PRs right now across my projects. I evaluate them in waves.

I don't have a to-do list anymore. Whenever I have an idea, get a bug report, or see someone frustrated on X with something GStack does, I just click the plus icon in Conductor. It creates a new work tree. Each work item gets its own branch. I run Office Hours, CEO Review, adversarial review, end review — my normal process. When it's ready to land, it lands.

I can do 10, 15, 20, sometimes 50 PRs in any given day, depending on how many meetings I have.

One thing I'm genuinely paranoid about right now: supply chain attacks. AI coding is moving fast and the attack surface is real. Having GStack as a structured review layer helps me catch issues I'd otherwise miss.

## Where This Is Heading

GStack is my attempt to get toward what I call a level-7 software factory. It doesn't get you to level 8 — but it gets you close. That's where I can run multiple Conductor windows on different projects, sometimes three or four on the same project simultaneously, with parallel PRs, parallel branches, parallel features all landing more or less at the same time.

The idea: there's a **ship tool** that's the final step before a PR lands on main. It runs all the checks and makes sure things are actually ready.

---

GStack is available right now at [github.com/gritan/gstack](https://github.com/gritan/gstack). When you run `/office-hours`, you're getting a version of the real product thinking we do at YC with founders — similar pushback, similar reframing, before you ever meet us.

This is the most incredible time in history to build software. The barrier to building just collapsed. The only question left is: what are you going to build?

It's time to let it rip. Go make something people want.
