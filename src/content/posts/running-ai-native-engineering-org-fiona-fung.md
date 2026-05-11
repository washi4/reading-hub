---
title: "Running an AI-Native Engineering Org"
date: 2026-05-11
description: "Fiona Fung, head of Claude Code at Anthropic, shares five hard-won lessons on rewriting team norms when engineering bandwidth is no longer the bottleneck."
source: https://www.youtube.com/watch?v=igO8iyca2_g
cover: https://img.youtube.com/vi/igO8iyca2_g/maxresdefault.jpg
speaker: Fiona Fung, Head of Claude Code Engineering & Product, Anthropic
format: Conference talk
language: English
purpose: Read-aloud article
tags:
  - youtube
  - ai
  - engineering
  - leadership
  - anthropic
chunks:
  - text: "what served you prior may not serve you any longer"
    type: sentence-frame
    meaning: "曾经适合你的，未必还适合你"
    note: "本文的核心主题，适用于任何正在快速变化的工作方式"
  - text: "bottlenecks have moved"
    type: chunk
    meaning: "瓶颈已经转移"
  - text: "quietly stops working"
    type: chunk
    meaning: "悄悄地失效；不是突然崩掉，而是逐渐失去意义"
  - text: "JIT planning"
    type: collocation
    meaning: "即时规划；按需计划，避免过度超前的路线图（借用 just-in-time 的概念）"
  - text: "code wins"
    type: formulaic
    meaning: "以代码说话；用实际可运行的代码来解决技术争论"
  - text: "shift left"
    type: chunk
    meaning: "左移；把质量验证提前到更早阶段（如自动化测试），而不是等上线后才发现问题"
  - text: "trust but verify"
    type: formulaic
    meaning: "信任，但要验证；让 AI 做大部分工作，但人类仍需核查关键部分"
  - text: "dogfooding"
    type: chunk
    meaning: "自用产品；团队内部大量使用自己构建的产品，以获得真实体验"
  - text: "roles are blurring"
    type: chunk
    meaning: "角色边界正在模糊；工程师、设计师、PM 的分工越来越不清晰"
  - text: "Claudify"
    type: chunk
    meaning: "Claudify：用 Claude 自动化某个工作流程"
  - text: "explicit permission to kill old processes"
    type: chunk
    meaning: "明确授权废除旧流程；给团队一个清晰的信号：可以放弃那些不再有效的做法"
  - text: "noisiest workflow"
    type: chunk
    meaning: "最嘈杂、最费时、最让人头疼的工作流"
---

Good afternoon and thanks for attending. My name is Fiona Fung and I lead Claude Code and Cody engineering and product here at Anthropic. Before Anthropic, I had led and grown teams at Meta and Microsoft. For today's talk, I want to cover five themes I've noticed as we've built out the Claude Code team — and more broadly, as the whole industry figures out what it means to run an engineering organization in an AI-native world.

I'll warn you upfront: I wrote these slides a month ago and I've already had to change some of the content. When I started the deck, there were no routines in Claude Code. That's how fast things are moving.

## The Shift: Bottlenecks Have Moved

I call the first theme "the shift." The subtitle says it best: **what served you prior may not serve you any longer.** That constant growth mindset is the muscle that has served me best across every role, at every company — and especially right now.

Here is what I mean by the shift. For years, engineering bandwidth was the expensive thing. Coding throughput was costly. Think about every process we built around shipping software — waterfall, then agile — almost all of it was designed to manage the scarcity of engineers writing code. When you couldn't write much code, you planned extensively before writing any.

Actually, let me take a small detour. This is not the first time our industry has had to adapt. I started my career around 2000, working on Visual Studio 2005. In those days, we shipped software on CD-ROMs — before that, floppy disks. There were hard ship deadlines because we had to get the bits to the manufacturing lab to be burned onto the discs, packed into boxes, and shipped to stores. When software distribution moved online, that changed everything about how we shipped. So the current shift feels dramatic, but we've done this before.

What's different now: coding is rarely the slow part anymore. And it's not just that it got a little faster — the throughput has radically increased. We're generating far more code than we used to, and so the **bottlenecks have moved**. They've shifted toward:

- **Verification and review** — is this code correct? Who checks it?
- **Cross-functional coordination** — security, legal, product partners trying to keep pace
- **Maintenance** — what is the ongoing cost of all this generated code?

The question that keeps coming up from every engineering leader I talk to: "How are humans keeping up with code review when the generation rate is this high?" That's the real challenge now. Not bandwidth. Throughput.

## Team Norms We Had to Rewrite

### Planning: From Six-Month Roadmaps to JIT Planning

When I first joined Anthropic, I asked the obvious manager question: "Don't we need a six-month roadmap?" We put together a solid one. It was good for about three months. By the time I came back after the new year, so many things had changed that the plan felt obsolete.

So now we practice what I call **JIT planning** — just-in-time planning, borrowing from just-in-time manufacturing. The idea is to do just the right amount of planning at the right moment, because prototyping and code generation are no longer bottlenecks. The question changes from "how much should we plan before we build?" to "how fast can we learn something real?"

On Claude Code, we've dramatically reduced design docs before coding. For certain teams, in certain high-stakes scenarios, design docs are still really important — especially for async discussions. But our default now is: "Here's an idea, go prototype." Discussions happen in PRs, not documents. Most product conversations happen around something that already runs.

What did we double down on? Verification. Because when throughput goes up and there are new ways to break things, you have to **shift left** — catch issues earlier, closer to the source, through more automation. I want to find bugs before you do. And what's better than me finding a bug is my team not producing that bug at all, because the tests caught it at check-in.

### Technical Debates: Code Wins

Early in my time at Claude Code, I wanted to do a refactoring. Boris and I had a healthy technical debate about which direction to go. My old instinct was to find a whiteboard room and sketch it out. Then I caught myself — wait.

Instead, I generated three separate PRs implementing each option we'd been debating. And the interesting part: I cared not just about the API design, but about the impact on all the callers. By having Claude help me generate all three versions, the conversation shifted from "which design sounds better" to "here's the actual diff for each approach, and here's what breaks." **Code wins.** That is now our default mode.

One critical caveat: this makes it even more important to have strong team culture around alignment. What absolutely won't fly is someone staying up until 3 a.m. to submit their PR last so their approach wins by default. When you can generate code fast, the temptation to "just ship it" is real. Open, honest technical debate still matters — it just happens later in the process, around real code instead of hypotheticals.

### Code Review: Trust But Verify

How do you keep up with code review when the generation rate has changed this much? Our answer is layered.

Claude handles all the styling, lint feedback, early bug catching, test generation, and PR cleanup before a full commit. By the time a PR reaches a human reviewer, most of the mechanical work is already done.

Where I still definitely want a human:

- **Legal review** — always, without exception
- **Security-sensitive code** — trust boundaries, permissions, anything where a mistake could be serious
- **Product sense and taste** — I'll give you an example here

Last holiday season, I wanted to give Claude Code a little holiday theme in the terminal. I asked Claude Code to "turn Claude into a snowman." Claude's ASCII art in those days... was not great. What it produced looked more like the Mr. Peanut character than a snowman. When I asked my design partner to review it, she gave me exactly the feedback I needed.

**Trust but verify.** That's the principle. Claude does a lot. Humans hold the accountability for judgment calls, relationships, and taste.

### Team Makeup: Roles Are Blurring

**Roles are blurring.** My PM writes code — a lot of it, which is genuinely fun to watch. My engineers are now doing things that used to require a dedicated content designer or a dedicated design partner. Cross-functional gaps that used to require hiring a specialist can sometimes be filled by Claude.

On the Claude Code team, there are two engineering profiles I index on heavily:

1. **Creative builders with product sense** — the dreamers, passionate about shipping something that solves a real problem, iterating until it's delightful
2. **Deep systems expertise** — distributed systems, reliability engineering, the hard parts that still require hard-won knowledge (like building Claude Code Remote to run Claude everywhere)

What I index on less: raw throughput. Thanks to the models, we're already generating a lot of code. What I need from people is judgment, not speed.

### Org Shape: Flat, with Dogfooding Baked In

This one made my recruiting partners nervous.

I've shipped products across many teams — Visual Studio, Facebook Marketplace, AR/VR, now Claude Code. The thing that has consistently helped me ship great product is heavy, relentless **dogfooding**. Leaders have to use the thing they're building. Not occasionally — constantly.

So I set up the Claude Code org to require that every manager start as an IC first. My recruiters were skeptical. "No manager will be interested in that," they said. My response: this is what dogfooding on the Claude Code team means. If someone's not interested, it's better to find out early.

I've kept the org as flat as possible. Pods have high agency — they own their triage, their planning rituals, their on-call processes, which workflows to **Claudify** first. But there's one overall team mission, not a separate mission per pod. When you need to shift direction, a flat org with a single mission makes that dramatically easier.

And without Claude, I genuinely don't think I could still be active in the codebase as a leader. At Meta, I would try to submit one PR per year just to stay grounded — but internal tools changed so fast that by the time I learned a workflow, it had already changed. Now I just ask Claude. It removed that barrier completely.

## How We Rolled It Out

We balance mandating and enabling. Some things are team-wide norms:

- Every Claude Code team member — including cross-functional partners — uses Claude Code
- **Claudify everything you can** — always ask "Is there some way Claude could help with this?" before doing it manually
- **Explicit permission to kill old processes** — this one is my favorite

On that last point: processes never kill themselves. We just layer more on top. I inherited a team that had so many SLAs that we had to create a meta-SLA to rank the SLAs. Things accumulate.

So we make it a team norm to periodically ask: does this still serve its intended purpose? Early on, we did standups. The team got bigger, so we moved to a spreadsheet for weekly status updates. Then I thought — wait, can we just run a Claude Code script that aggregates everyone's progress from their repos? Now I get a cleaner summary with less work from everyone. The spreadsheet is gone.

We leave most workflow decisions to individual pods: how to do triage, how to run standups, which workflows to automate first. We have suggestions and learnings to share, but high agency at the pod level matters.

## Does It Actually Work?

I can't share explicit numbers, but here are three metrics I watch:

**Onboarding ramp-up time** has dramatically decreased. New engineers — and designers, and PMs — become effective contributors much faster than before.

**PR cycle time** has shortened. But pay attention to what this reveals: if cycle time is still high despite Claude-assisted development, you may have found a bottleneck elsewhere in the pipeline — CI, build infrastructure, review queues — that can't keep up with the throughput.

**Claude-assisted commit rate** — at Claude Code, by default every commit is Claude-assisted. I haven't seen a non-Claude-assisted commit in roughly four months.

One important caveat: throughput is not the goal. It's a signal. The real question is always: what is the product problem you're trying to solve, and is quality and reliability improving? Don't chase the AI-generated code percentage headline. Chase the outcome.

## Audit Your Own Effort

I'll be honest — I still have open questions I'm working through.

iOS and Android orgs are interesting. When engineers can more efficiently flex across mobile platforms with AI assistance, does it still make sense to maintain separate iOS and Android teams? I don't know yet.

How much should you push toward fully automated review? The right balance between "fast enough" and "lost something important" isn't fixed — it shifts as model capabilities improve. What required more human verification six months ago might be safely automated today.

And as roles blur, how do you make sure everyone still feels equally productive?

My takeaway for you: pick your **noisiest workflow**. The most expensive one, the one people dread, the one where everyone is on their laptop except when it's their turn to speak. Ask a simple question: *is this still serving its intended purpose?*

I was once on a team that ran a weekly review with 50 people in a large room. Everyone was on their laptops until it was their turn to give a status update. One day I just asked: why are we having this meeting? Everyone looked around and said — yeah, good point. We canceled it.

That's the mindset I'm encouraging: keep your processes under constant review. Give your team explicit permission to kill the ones that have quietly stopped working. And always be asking: what is it I'm actually trying to accomplish, and is there a way Claude could help?

Thanks so much for attending. I really did think this room was going to be empty. I'm around today and tomorrow — come find me if you want to talk more.

[applause]
