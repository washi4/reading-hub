---
title: "How to Build a Self-Improving Company with AI"
date: 2026-05-24
description: "A YC partner argues that AI doesn't just make employees more productive — it lets you reimagine the entire company as a set of recursive, self-improving loops."
source: https://www.youtube.com/watch?v=X_JsIHUfUjc
cover: https://img.youtube.com/vi/X_JsIHUfUjc/maxresdefault.jpg
speaker: Y Combinator
format: Talk
language: English
purpose: Read-aloud article
tags:
  - youtube
  - ai
  - startup
  - company-building
  - yc
chunks:
  - text: "project power"
    type: collocation
    meaning: "投射力量，扩展影响力"
  - text: "spans of control"
    type: chunk
    meaning: "管辖范围（管理层级中一个人直接管理的下属数量）"
  - text: "bolt onto the side"
    type: chunk
    meaning: "附加在旁边，硬加上去"
  - text: "recursive self-improving AI loops"
    type: chunk
    meaning: "递归式自我改进的 AI 循环"
  - text: "burn tokens, not headcount"
    type: formulaic
    meaning: "花 token，不花人头（用 AI 算力代替招人）"
  - text: "token maxing"
    type: chunk
    meaning: "把 AI 用量拉满"
  - text: "directly responsible individuals"
    type: chunk
    meaning: "直接责任人（DRI），指对某事负全责的具体个人"
  - text: "at the bleeding edge"
    type: chunk
    meaning: "在最前沿，最先锋的位置"
  - text: "legible to AI"
    type: collocation
    meaning: "对 AI 可读/可理解"
  - text: "diorize it"
    type: chunk
    meaning: "（此处指）把大量录音精炼、分类、摘要成可用信息"
  - text: "one-shot"
    type: chunk
    meaning: "一次性生成（不需要迭代）"
  - text: "the company brain"
    type: chunk
    meaning: "公司大脑（所有数据、知识、技能的集合）"
  - text: "high stakes moments"
    type: collocation
    meaning: "高风险时刻，利害攸关的场合"
---

## From Roman Legions to AI Loops

This is based a little bit off a talk Diana gave — there's a video up over the weekend which is super cool. Jack Dorsey was tweeting some stuff like two or three weeks ago that I thought was super cool, and I've kind of stolen a bunch of those ideas and shoved them into here. This talk is pretty conceptual and high-level about thinking about how to build companies.

So, the Roman legions were designed to project power over two continents from Rome at the center to people on Hadrian's Wall up in Scotland. The idea was nested hierarchies with consistent spans of control — you had named individuals with spans of control to pass orders down and send information back up the hierarchy.

If you think about most companies today, they are organized like a Roman legion, where human beings are the conduit for information flowing up and down. Jack Dorsey's tweet, which I thought was great, was this: there's an underlying assumption that hierarchically organized companies are the way we should be organizing our economic units of value. And I think AI basically breaks that.

## Productivity Is the Wrong Frame

If you talked to people a year ago about how AI was useful, they talked about productivity — co-pilots, making engineers 20% more productive, adding co-pilots to workflows, shipping more software. But I think that is actually a broken way of thinking about AI. That's like Pete had a great blog post: we're basically just taking the old way of working and adding a more powerful engine onto it.

Instead of that, I think you can reimagine what a company is and how it acts. As Gary's been talking — he can genuinely produce more code than an entire engineering team.

## Extract Domain Knowledge

The thing that's really stuck with me is this idea of extracting the domain knowledge from your company and defining it as context, or a set of skills, or whatever you want to call it. There's domain knowledge or business knowledge or some know-how that's inside the heads of people and in Slack messages and in emails and in Notion. All of this information together defines how your company works.

If you can make that legible, you suddenly can move from this hierarchical organization to a sort of intelligent, AI-powered organization with AI-native software. AI isn't something you bolt onto the side of a company. It's not a tool you give to your engineers to make them more productive. I think you can reimagine what a company is as a set of recursive self-improving AI loops.

This is really, really important — because when it gets there, I think the company starts to self-improve even when you're sleeping.

## The AI Loop

Let me give you an example. Diana talks about this as well — this AI loop. You start with:

1. **A sensor layer** — that's a fancy word, but really it might be emails from your customers, support tickets, code changes, people canceling their subscription, product telemetry. It's sensor data to get information from the outside world.

2. **A policy layer** — decision layer, rules about what the AI can do, what it has to ask a human permission for, what it must log.

3. **A tool layer** — that's Gary's skills and code. Basically deterministic APIs, things like "query my database" or "look at my calendar." A set of tools that the AI can call.

4. **A quality gate** — that might be evals, safety filters, human review for high-risk stuff.

5. **A learning mechanism** — your system interacts with the real world, picks up where it doesn't work, and loops back into the top again.

If you can run every single step of that without human intervention — with minimal human intervention — your system gets better and better while you're sleeping.

## A Real Example at YC

I can give you actual examples of this that are live right now. We started with an agent that you can ask, and it has deterministic tools to query our database. Pretty simple — like "When did I last have office hours with this company?"

Then it got a little smarter. For a company I'm doing office hours with right now, they need introductions for anyone in petrochemicals or something, and it could query the database in different ways and use RAG and all sorts of stuff to come up with five relevant founders for you to meet. But again, this is a sidekick. This is like last year's version of how AI is making me better as a group partner. It's making me 20 or 30% more effective.

The aha moment for me came when we put a monitoring agent on top of that which looked at every single query every single YC employee was doing — and saw when it worked and when it did not work. It's like, "Oh, why not? What would have made this query work? Do we need different deterministic tools? Do we need to update the skills file? Do we need a different database view? Do we need a new index?"

This literally happens overnight now. It writes the code, puts in a merge request to the YC codebase, has an agent review it, merge it, and deploy it. So when a human comes the next day to ask the same query, it will now succeed.

For me, that was the holy shit moment. That's not just AI making you 20 or 30% more valuable. It is the AI going through this loop to figure out how to self-improve.

## Throw Tokens at the Problem

I think if you can identify parts of your company that work like this and have the human in a monitoring, supervisory capacity, you can just throw tokens at this problem and your company will get better.

Other examples: if you have product analytics, have an agent go through your product analytics to figure out what part of your sales funnel is presenting the highest amount of friction, research best practices, put in place an A/B test, run it for a week, pick the best version, and deploy it. Then do that again and again. Just have a self-optimizing product loop.

Or you do it with customer service. You have customer suggestions coming in, triage it with an agent that acts like your chief product officer and your chief technology officer, making judgment calls — "This is a suggestion we just don't want to do, we'll discard it" versus "This is a suggestion in line with our roadmap — we can do it overnight. Let's write the code, deploy it, ship it to the customer without a human being involved."

If you can think about each part of your company as a self-improving recursive AI loop, it becomes very different from this hierarchically organized Roman legion.

## Implications: Burn Tokens, Not Headcount

So what are the implications if you want to do this?

One: burn tokens, not headcount. We are seeing companies get to Demo Day with about 5x more revenue per employee than they did 18 months ago. I think that's going to continue to Series A and Series B. You're going to be constrained on token usage, not on headcount, really soon.

The blunt measure now is just measuring everyone's token usage, which is obviously dumb and gameable at the extreme, but directionally I think is correct. We're in the phase of figuring out what is possible right now, so everyone should be experimenting to the max. As soon as you turn it into a leaderboard and people get promoted or fired based on it, obviously it gets gamed. But I think directionally, figuring out who in your organization is token maxing and who is not is a good way to think about which employees you should be spending your time with.

## Middle Management Is Done

I think middle management is done. I just don't think you need middle management for this coordination problem. I think AI should be doing it.

For me, there are two roles that really matter. I think everyone just has to be an IC now — a builder, an operator. And crucially, having directly responsible individuals: to get anything done, I think you need a named human, not a committee, not a group of people, just a single person. I think you can build companies based on ICs effectively. Middle management is over.

## Make Everything Legible

Building this self-improving company — that's the dream. And by the way, people are at the bleeding edge of this right now. I'm not sure anyone has a truly self-improving company in every function. You might prove me wrong.

What would I do? First of all, make the entire organization legible to AI. What does that mean? You've got to record everything. Everything. Everything.

Simplistically — all of our partner emails now, if you email a YC partner, that email is in the YC database. Every Slack message, every DM, every office hour we've started recording for the last three or four months. Every single thing that happens — if it is recorded, it happened to the AI. If it did not get recorded, it did not happen to your intelligence.

I was talking with some founders just now and having really good conversations about their company, but every conversation I had, I was like, "I need to be recording this conversation." Because some guy wanted an introduction to — I can't even remember who now. I promised an introduction and said, "Email me afterwards because I'm going to forget. I'm going to talk to 20 people." So it needs to be on my phone, or a clip, or smart glasses, or we deck out every room with microphones. Basically, everything needs to be recorded so it can be legible to the AI.

## Diorize and Synthesize

As Gary talked about, you cannot pump in 100,000 hours worth of recordings into a context window. So you have to diorize it — basically aggregate it down, synthesize it into the important parts, and give the AI breadcrumbs.

Here's an example. Who's read the YC user manual? It was written 5 to 10 years ago, most of it. It's kind of out of date. Haj thought last weekend — since we've now got about 2,000 hours of recorded office hours in the last 3 months — why don't we regenerate the user manual?

You give it a set of instructions, diorize it down, categorize it into areas like fundraising, hiring, co-founder disputes, whatever. Then write a new user manual. By the end of the weekend, he had a 150-page user manual, which is dramatically better than the existing one. And now we can update it every single month. So our user manual becomes self-improving. Every new piece of advice we give is compared with the existing user manual and either incorporated or thrown away. The user manual becomes this up-to-date living brain of the advice we give to founders.

And obviously it doesn't stop as a user manual. You pump it in as context to an AI agent and suddenly you can ask a super intelligent AI and get the combined wisdom of 16 YC partners in one — but only if it's legible. You have to record everything.

## Software Is Ephemeral, Context Is Valuable

The second point is the same: if it creates an artifact that can self-improve, it's legible. If it doesn't, throw it away.

The third point is that every function can generate on-demand software. Codex is now good enough — you can one-shot most simple internal software dashboards to a pretty high level of quality. I tried it over the weekend on a bunch of our stuff. It's just unreal.

All of your internal operations teams should be sitting on this layer of intelligence and understanding, then creating their own dashboards and workflows. I would see those as entirely disposable. I would very preciously store all the data — as Gary said, he puts all of his emails in markdown. Never throw anything away, but treat the software as ephemeral. You can generate it, regenerate it.

The valuable part is the comprehension inside people's heads of "this is how the function works, this is how we run a YC event." The software to actually run the event? Generate it for the event, throw it away. The models get smarter in a month or two — throw the software away, give it your original set of instructions, and regenerate.

The business context and skills are the valuable part. The software on top of it is ephemeral.

## Where Do Humans Fit?

So what are humans for in this world? I think we're talking about a company brain — all of your data, your emails, your DMs, the skills, the know-how — that is the company brain. The humans sit around the edge of this, interfacing with the real world. It's where this intelligence makes contact with reality.

Human beings reach into places the models can't go yet. That might be a conference. I would say a phone call, but I think the AI can reach into phone calls pretty easily now. I think it's novel situations, ethical considerations, high stakes moments. It's where the founder comes to us and is thinking about breaking up with their co-founder. Those real high-stakes, high-emotion moments where you really want a human being — that's where the human fits.

For all of you — sales conversations. I think that's a human being in the room for the next 20 years. The humans live around the edge.

I will leave you this one question: **If you were building your company today, would you start it in this shape?** For most of you, you're small enough to build it right. I don't think you have any excuse. And I know there are a few of you in the process of ripping up and rebuilding your company.

With that, I will stop, and we'll hand over to Pete. Thank you for listening.

[applause]
