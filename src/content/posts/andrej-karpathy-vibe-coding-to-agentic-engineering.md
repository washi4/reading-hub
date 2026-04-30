---
title: "Andrej Karpathy: From Vibe Coding to Agentic Engineering"
date: 2026-04-30
description: "Andrej Karpathy joins Sequoia Capital to unpack software 3.0, the difference between vibe coding and agentic engineering, jagged AI intelligence, and why you can't outsource your understanding."
source: https://www.youtube.com/watch?v=96jN2OCOfLs
cover: https://img.youtube.com/vi/96jN2OCOfLs/maxresdefault.jpg
speaker: Andrej Karpathy, in conversation with Sequoia Capital
format: Fireside chat
language: English
purpose: Read-aloud article
tags:
  - youtube
  - ai
  - engineering
  - andrej-karpathy
  - sequoia
chunks:
  - text: "vibe coding"
    type: chunk
    meaning: "氛围编程；用自然语言驱动 AI 写代码，不纠结细节"
  - text: "agentic engineering"
    type: chunk
    meaning: "智能体工程；在不牺牲质量标准的前提下，协调 AI 智能体更快完成专业软件开发"
  - text: "stark transition"
    type: collocation
    meaning: "鲜明/急剧的转变"
  - text: "rabbit hole"
    type: chunk
    meaning: "兔子洞；让人越陷越深的事物"
  - text: "jagged"
    type: chunk
    meaning: "参差不齐的；指 AI 能力极度不均匀——某些领域超强，某些领域离谱地弱"
  - text: "rough around the edges"
    type: chunk
    meaning: "在某些边角地方粗糙、不完善"
  - text: "at the mercy of"
    type: formulaic
    meaning: "受……摆布，只能听凭……"
  - text: "spurious"
    type: chunk
    meaning: "多余的、站不住脚的（此处指某个 app 其实不该存在）"
  - text: "raising the floor"
    type: chunk
    meaning: "提高下限；让每个人都能做到以前做不到的事"
  - text: "preserving the quality bar"
    type: chunk
    meaning: "维持（专业）质量标准不下降"
  - text: "stochastic"
    type: chunk
    meaning: "随机的、不确定的"
  - text: "you can't outsource your understanding"
    type: sentence-frame
    meaning: "你无法把理解力外包出去"
    note: "Karpathy 引用的一条让他反复思考的推文"
---

Thank you, Andrej, for joining us. You helped build modern AI, then explain modern AI — and occasionally rename it. You co-founded OpenAI right here in this office, got Autopilot working at Tesla, and have a rare gift for making the most complex technical shifts feel both accessible and inevitable. You coined the term *vibe coding* last year. But just a few months ago, you said something even more startling: that you've never felt more behind as a programmer. That's where we're starting today.

## The December Shift

That feeling was a mixture of exhilarating and unsettling, for sure. I'd been using agentic tools for a while — maybe over the last year — and they were quite good at chunks of code. Sometimes they'd mess up and I'd have to edit things, but it was helpful. Then December was this clear point where, because I was on a break and had more time, I started noticing that with the latest models the chunks just came out fine. I kept asking for more and it came out fine. I can't remember the last time I corrected it. I just trusted the system more and found myself vibe coding. I think it was a very stark transition.

A lot of people experienced AI last year as a ChatGPT-adjacent thing. But you really had to look again as of December, because things changed fundamentally — especially on this agentic, coherent workflow that really started to actually work. It became a rabbit hole of infinity side projects. My side projects folder is extremely full of random things, and I was just vibe coding all the time. That kind of happened in December, and I've been looking at the repercussions ever since.

## Software 1.0, 2.0, and 3.0

You've talked a lot about the idea of LLMs as a new computer — not just better software, but a whole new computing paradigm. Software 1.0 is writing explicit code. Software 2.0 is programming by creating datasets and training neural networks — the programming is arranging data and objectives and architectures. Software 3.0 is what happened when you train one of these GPT models on a sufficiently large set of tasks. Because you're training on the internet, you have to multitask everything in the dataset. These models become a kind of programmable computer. Your programming turns to prompting, and what's in the context window becomes your lever over the interpreter — the LLM that is interpreting your context and performing computation.

A good example is when Claude Code came out. Normally an installer is a bash script, and these shell scripts usually balloon up and become extremely complex as you target lots of different platforms. But in the software 3.0 paradigm, you don't have to precisely spell out all the individual setup details. The agent has its own intelligence, looks at your environment, performs intelligent actions to make things work, and debugs things in the loop. The piece of text you copy-paste to your agent — that's the programming paradigm now.

An even more extreme example is my MenuGen project. I wanted to take a photo of a restaurant menu — where there are no pictures and I have no idea what half the items are — and get images of what those dishes actually look like. I vibe-coded an app that OCRs the menu, uses an image generator to produce pictures for each item, and rerenders the menu with photos. Then I saw the software 3.0 version: literally just take your photo, give it to Gemini, and say "use Nanobanana to overlay pictures onto the menu." Nanobanana returned an image of the actual menu with the dishes rendered directly into the pixels.

That blew my mind, because all of my MenuGen is spurious. It's working in the old paradigm. That app shouldn't exist. The software 3.0 paradigm is more kind: your prompt is just the image, the output is just the image, and there's no need for any of the app in between.

It's not even just about programming getting faster. This is more general information processing that's automatable now. Code used to work over structured data. But with my LLM knowledge-base project — where LLMs create wikis for organizations — this isn't even a program. There was no code that could create a knowledge base from a bunch of unstructured facts. Now you can take documents, recompile them in a new way, and create something that is a genuine reframing of the data. These are new things that weren't possible before. I think that's more exciting than anything that's just a speed-up of what already existed.

## Verifiability and the Jagged Frontier

I spent some time writing about verifiability. Traditional computers can automate what you can specify in code. The latest LLMs can automate what you can verify — because frontier labs train these models in giant reinforcement learning environments with verification rewards, and the models end up as jagged entities that really peak in capability in verifiable domains like math and code, and stagnate or are rough around the edges when things fall outside that space.

I'm trying to understand why these things are so jagged. Part of it is how labs train the models. But part of it is what happens to make it into the data distribution. Code is valuable enough that there are lots of RL environments around it. There are probably verifiable domains that haven't made it into the mix simply because the labs didn't prioritize them.

The favorite example for a while was: "How many letters are in strawberry?" The models would famously get this wrong. The models now patch this. But the new one is: "I want to go to a car wash 50 meters away. Should I drive or should I walk?" State-of-the-art models will tell you to walk because it's so close. How is it possible that a model can simultaneously refactor a 100,000-line codebase and not understand that you don't drive a car through a car wash? That jaggedness is an indication that something is slightly off in what these models are doing internally.

We are to some extent at the mercy of whatever the labs are doing, whatever they happen to put into the mix. You have to explore this thing they give you, which has no manual. It works brilliantly in certain settings and struggles in others, and you have to figure out where you are and whether fine-tuning is needed.

## Vibe Coding vs. Agentic Engineering

Vibe coding is about raising the floor for everyone in terms of what they can do with software. The floor rises, everyone can vibe code anything — that's amazing, incredible.

Agentic engineering is about preserving the quality bar of what existed before in professional software. You're still responsible for your software. You're not allowed to introduce vulnerabilities because of vibe coding. But can you go faster? The answer is yes — and it's considerable. I think the 10x engineer framing is not the speed-up you get. It's substantially more than that. And people who are very good at this seem to peak much higher.

## What Agentic Engineering Actually Looks Like

It's about investing into your setup and utilizing all the features available — just as engineers previously got the most out of vim or VS Code, now it's Claude Code or Codex. You have to adapt.

If I were hiring for strong agentic engineers, I'd give up the old paradigm of coding puzzles. Instead: give me a really large project. Write a Twitter clone. Make it secure. Then have agents simulate activity on it. Then I'll use ten Codex instances to try to break your deployed website. Watch whether it holds up. Watch people in that setting — building bigger projects, utilizing the tooling. That's what I'd look at.

## What Human Skills Become More Valuable

Right now the agents are like intern entities. They're remarkable, but you still have to be in charge of aesthetics, judgment, and taste. One of my favorite examples of the weirdness of agents: in MenuGen, you sign up with a Google account but purchase credits using a Stripe account. My agent tried to match users by their email address — but you might use different emails for Stripe and Google. The agent would just fail to associate the funds. This is the kind of mistake that agents still make. Why would you use email addresses to cross-correlate? They can be arbitrary. Someone has to own the spec.

I actually don't love plan mode in its current form. What I think is more general: you have to work with your agent to design a very detailed spec — maybe basically the docs — and then get the agents to write them while you maintain oversight of the top-level categories. The details of APIs — `keepdims` vs `keep_dim`, `dim` vs `axis`, `reshape` vs `permute` vs `transpose` — I don't remember any of this stuff anymore, because you don't have to. That's handled by the intern, who has very good recall. But you still have to know that there's an underlying tensor, that there are views and storage, that you don't want to copy memory around unnecessarily. You're asking for the right things and saying these have to be unique user IDs that everything ties to. You're doing the design; the agent fills in the blanks.

Will taste and judgment matter less over time? Probably the reason it doesn't improve right now is that it's not part of the RL — there's probably no aesthetics reward, or it's not good enough yet. When I actually look at the code sometimes I get a little heart attack: it's very bloaty, lots of copy-paste, awkward abstractions that are brittle. It works but it's gross. And the models hate simplification. My microGPT project — trying to simplify LLM training to be as simple as possible — the models can't do it. You feel like you're outside the RL circuits. You're pulling teeth. There's nothing fundamental preventing this from improving; the labs just haven't done it yet.

## Animals vs. Ghosts: Jagged Intelligence

I wrote about this because I'm trying to wrap my head around what these things actually are. If you have a good model of what they are — or are not — you'll be more competent at using them.

The key point is that these things are not animal intelligences. If you yell at them they're not going to work better or worse. It's all just statistical simulation circuits where things get bolted on top. Coming to terms with that shifts your mindset about what's likely to work or not. I don't have five obvious outcomes of how to make your system better from this framing — it's more just a way of orienting toward the exploration of what these things actually are.

## Agent-Native Infrastructure

Everything is still fundamentally written for humans. I still use docs that tell me what to do. But I don't want to do anything. What is the thing I should copy-paste to my agent? When I wrote the blog post about MenuGen, a lot of the trouble was not writing the code — it was deploying on Vercel. I had to string together different services, go through their settings and menus, configure DNS. That's a good test of whether our infrastructure is becoming agent-native: could I give a prompt to an LLM, have it build MenuGen, and have it deployed on the internet without me touching anything? That would be the benchmark.

Ultimately, I think we're moving toward a world of agent representation for people and organizations. I'll have my agent talk to your agent to figure out the details of our meetings. Everything has to be rewritten from a fundamentally human interface to a fundamentally agent interface — sensors and actuators over the world, data structures legible to LLMs, describe it to agents first.

## What Still Remains Worth Learning

There was a tweet that blew my mind and that I keep thinking about every other day. It was something along the lines of: *you can't outsource your understanding*.

I'm still part of the system. Information still has to make it into my brain. I feel like I'm becoming a bottleneck in just knowing: what are we trying to build, why is it worth doing, how do I direct my agents? Something has to direct the thinking. And that is still fundamentally constrained by my ability to process information.

Whenever I see a different projection onto information, I feel like I gain insight. I have my wiki being built up from articles I read. I love asking questions, exploring new angles. These are tools to enhance understanding — and understanding is still a bottleneck, because the LLMs certainly don't excel at it. You still are uniquely in charge of that.

You can't be a good director if you don't understand what you're directing. The LLM still doesn't do that for you. And I think tools that enhance your understanding — rather than replacing it — are incredibly interesting and exciting.

I'm excited to come back here in a couple of years and see whether we've been fully automated out of the loop, or whether understanding really does remain the last human edge.
