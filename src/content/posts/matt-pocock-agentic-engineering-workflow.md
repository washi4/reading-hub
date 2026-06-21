---
title: "Matt Pocock's Agentic Engineering Workflow (Just Copy Him)"
date: 2026-06-21
description: "David Ondrej interviews Matt Pocock on the model vs. harness debate, strategic vs. tactical programming, what makes a good agent skill, and why your skills are the ceiling on what AI can do."
source: https://www.youtube.com/watch?v=nQwJVHCtDDY
cover: https://img.youtube.com/vi/nQwJVHCtDDY/maxresdefault.jpg
speaker: David Ondrej and Matt Pocock
format: Tech interview / discussion
language: English
purpose: Read-aloud article
tags:
  - youtube
  - ai
  - engineering
  - agentic
chunks:
  - text: "harness"
    type: chunk
    meaning: "围绕模型的工作框架/工具链"
    note: "Matt 强调 harness 和 model 同等重要"
  - text: "strategic programming"
    type: collocation
    meaning: "战略性编程"
    note: "长期架构思考 vs 战术性编码"
  - text: "infinite fleet of tactical programmers"
    type: chunk
    meaning: "无限的战术编程大军"
    note: "指 AI 可以无限量地执行战术性编码任务"
  - text: "skills are the ceiling"
    type: chunk
    meaning: "技能是天花板"
    note: "AI 的能力上限取决于你的技能水平"
  - text: "zone of proximal development"
    type: chunk
    meaning: "最近发展区"
    note: "教育学术语，指学习者略高于当前水平的能力区域"
  - text: "adversarial interviewer"
    type: collocation
    meaning: "对抗式面试官"
  - text: "cues not loops"
    type: chunk
    meaning: "队列而非循环"
    note: "通过任务队列管理 AI 代理，而不是无限循环"
  - text: "hamstringing"
    type: chunk
    meaning: "束缚/削弱"
  - text: "agent-agnostic"
    type: chunk
    meaning: "与具体 AI 代理无关的"
  - text: "upskilling"
    type: chunk
    meaning: "提升技能"
  - text: "pick up the slack"
    type: chunk
    meaning: "弥补不足/收拾烂摊子"
---

Everyone's obsessed with the model. I think they should be more interested in the harness — what you can do to get the most out of the harness. Giving it the right prompts, giving it the right skills to work with, and improving the environment in which the model runs. The model is useful, but the harness has an equal amount of work, and you have much more control of the harness than you do the model.

That's Matt Pocock's core argument. In this interview, David Ondrej sits down with Matt to break down his agentic engineering workflow — how he thinks about AI, skills, and what separates developers who get insanely ahead from those who only get a small boost.

## Strategic vs. Tactical Programming

**David:** What's the main difference between people who use AI to get insanely ahead and the majority of people who only get a small boost from it?

**Matt:** In John Ousterhout's book *Philosophy of Software Design*, he talks about the difference between tactical and strategic programming. I find this distinction so useful when thinking about AI.

Tactical programming is all about the on-the-ground day-to-day stuff — writing code, messing about with syntax, figuring out bugs as they come up, creating commits. Strategic programming is winning the war, not the battle. It's longer-term thinking. It's the general sitting at the top. How does the codebase need to look? What strategies can I use to improve our velocity?

AI has basically eaten tactical programming. It's gone. AI is just better at doing tactical programming than you are, because it can do it for cheaper. So you need to be great at strategic programming in order to get the most out of this infinite fleet of tactical programmers that you now have access to.

## Your Skills Are the Ceiling

**David:** How would you advise people to start teaching themselves to be better?

**Matt:** My skills are a multiplier for AI. If I'm able to oversee a codebase and think about how things should be built, and just tell AI how to do it, then AI has so much richer context to work with.

AI makes senior developers just 10 times better. And it sort of doesn't make sense to hire that many juniors anymore, because juniors get a little boost from AI, but seniors get this ridiculous huge boost. So your skills are the ceiling on what AI can do. If your skills are low, AI is not going to be able to go past that.

Getting good with AI is really about getting good at your domain. A better teacher can use AI to teach people better than a random can. Skills are more important now than they used to be, because you have this multiplier available to you.

## The Teach Skill

**David:** You recently shipped the teach skill. Can you tell us more about that?

**Matt:** I've been a teacher for 10 years — singing and voice straight out of university, then I became a developer and now I teach developers. I thought: what if I take teaching principles like the zone of proximal development, the difference between knowledge, skills, and wisdom — encode that into a skill and use it to create a course on the fly about any topic?

I've been teaching myself Rubik's cube from this. I can solve one from memory now thanks to this skill. It's extremely effective.

**David:** I'm going to pretend I'm a vibe coder. I'm inside an empty directory, I invoke the teach skill, and I dictate: "I am a vibe coder and I want to fill in my knowledge gap so I can ship better software. I know some basic CLI commands and I know just about enough to read some code and use the terminal."

**Matt:** The skill first aligns with what you want. It asks three quick questions to understand your mission. It searches for trusted resources, creates a learning record, a reference cheat sheet, and your first lesson — all as HTML files you can open in a browser. It's perfectly personalized education.

The first lesson for a vibe coder? Git. The highest leverage gap is almost never more syntax — it's the stuff around the code that lets you ship without fear. Git, reading errors, debugging, testing.

You can find it at GitHub — `mattpocock/skills`. Run `npx skills latest add mattpocock/skills` and it works with Claude Code, Cursor, Codex, whatever you use.

## What Makes a Good Agent Skill?

**David:** You have one of the most famous skills repos. What separates a good skill from a bad one?

**Matt:** There are two types of skills. **Abilities** — things you intend the model to invoke itself, like coding standards. **Procedures** — skills you invoke yourself to get the model to behave a certain way.

I prefer procedures. I like to be the one in control. My "grill me" skill is one of my most popular — it's just four or five sentences. It turns the model into an adversarial interviewer. Before implementing code, I say "interview me about this idea, let's reach a shared understanding." It's unreasonably effective.

Every skill leaks its description into the context window. If you have 100 abilities, you're leaking 100 descriptions. So I prefer to keep most knowledge inside the human, not the AI. You are the driver. You take the steering wheel.

## Knowledge, Skills, and Wisdom

There are three things you need to be good at anything:

1. **Knowledge** — understanding it in your head.
2. **Skills** — having done it enough times that it's in muscle memory.
3. **Wisdom** — knowing when to do it, how it fits in the real world.

Wisdom is almost impossible to obtain without actually doing the thing in the exact context where it matters. If you want to be like someone at Anthropic, sure you can gain the knowledge and skills — but you need to go to Anthropic to gain the wisdom.

Being able to bundle the first two into something reusable — that's a fascinating outcome of this weird age we're living in.

## The Agentic Setup: Cues, Not Loops

**David:** What's your actual agentic engineering setup? What tools, what models?

**Matt:** I use Claude Code with Opus 4.8 at medium effort for planning and local implementation. For AFK (away from keyboard) work, I built a tool called Sand Castle — it runs agents inside sandboxes (Docker or Podman). Combined with GitHub Actions, I can parallelize agents on pull requests. A review agent checks the branch, runs type checks, and replies with results.

The way I think about this is **cues, not loops**. A queue of tasks. You scope an item, label it, an agent picks it off the queue, implements it, creates a PR. That's all development really is — a queue of tasks that need to get done.

## Model vs. Harness: The Debate

**David:** I would challenge you on the model vs. harness thing. If you swap in a better engine, everything is instantly better.

**Matt:** People are focused on the wrong thing. They're looking at the big shiny new model when they should focus on what's been working for 30-40 years. People ask me all the time, "How do you optimize for token spend?" Have a codebase that's easier to make changes in. If your codebase architecture is better, you can get a cheaper model to do the same work because your guard rails are better. It needs to spend fewer tokens banging its head against the wall.

There's a famous idea in ML called the bitter lesson — compute will beat you every time because it's increasing at such a high rate. Maybe optimizing my harness is just fighting the inevitable. But I still think there's a lot to be gained by focusing on the fundamentals. I try to keep my workspace and harness agent-agnostic. If I apply good software fundamentals that have always worked, they'll probably continue to work.

**David:** I'd say I'm somewhere in the middle. I'm actively trying to improve my setup every day, but I also want to use the best model possible. What happens when the next generation comes — Opus 6, Fable 6, GPT 7? Won't they require less steering?

**Matt:** I'm not a pundit. I'm trying to do the best with what I have right now. If I try to over-optimize around a model, I lose focus on the fundamentals. If I try to keep things agent-agnostic, what's worked for 30 years will probably keep working.

## The Takeaway

**David:** The exact opposite of you is the quintessential vibe coder — switching tools every week, jumping on every new release, never learning any programming principles. Your approach is: learn the fundamentals, learn how good software looks, and this will be valuable no matter what — no matter if OpenAI is ahead, Anthropic is ahead, or Gemini is ahead.

**Matt:** Exactly. You should be focused on yourself. Upskill yourself for this new world. Don't delegate your thinking — delegate only the tactical stuff. Keep the strategic mindset. Think about the roadmap, where you're going. People are obsessed with the idea that you can delegate everything to AI. You can't. You really can't.
