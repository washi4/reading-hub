---
title: "Don't Ship Skills Without Evals — Philipp Schmid, Google DeepMind"
date: 2026-07-18
description: "Philipp Schmid explains why skills need evals, how to think about capability and preference skills, and how DeepMind tests skills before shipping them."
source: https://www.youtube.com/watch?v=0vphxNt4wyk
cover: https://img.youtube.com/vi/0vphxNt4wyk/maxresdefault.jpg
speaker: Philipp Schmid, Google DeepMind
format: Technical talk
language: English
purpose: Read-aloud article
tags:
  - youtube
  - ai
  - agents
  - evals
  - skills
chunks:
  - text: "progressive disclosure"
    type: collocation
    meaning: "渐进式披露"
  - text: "capability skills"
    type: chunk
    meaning: "能力型技能"
  - text: "preference skills"
    type: chunk
    meaning: "偏好型技能"
  - text: "write directives over passive information"
    type: formulaic
    meaning: "写指令，不要写被动描述"
  - text: "create outcomes, not paths"
    type: formulaic
    meaning: "关注结果，不关注路径"
  - text: "negative tests"
    type: chunk
    meaning: "负向测试"
  - text: "start small"
    type: chunk
    meaning: "从小处开始"
  - text: "isolated runs"
    type: collocation
    meaning: "隔离运行"
  - text: "ablation tests"
    type: collocation
    meaning: "消融测试"
  - text: "Run more than one trial"
    type: sentence-frame
    meaning: "多跑几轮试验"
  - text: "The better the model gets"
    type: sentence-frame
    meaning: "模型越强，就越……"
---

## Why skills need evals

[music] Yes, so hi everyone. My name is Philip. I'm based out of Germany. I'm part of the Google DeepMind team mostly working on Gemini API and agents. And we are going to talk about why you should not ship skills without evals.

Before we start, I need a little bit of your help. If you use coding agents to write code, raise your hand. If you use skills with it, raise your hand. Do you have evals for those skills? Not a lot of hands. Everyone uses skills, no one has evals. Hopefully we can fix that today.

The reason is simple: agents are really non-deterministic. You might not know if your task fails because your skill is bad or because it is just too challenging for the model. A lot of skills look fine at a glance, but then fail in production because nobody checked them properly.

There is also an important difference between the agents we use and the agents we build. When you use agents like Claude Code or Cursor, you are the engineer and you know when a skill should trigger. But when you build an agent for customers, they do not know what a skill is. They do not start their prompt with "use customer support skill" or "use refund skill." That is why the triggering and the eval story matter so much.

## What a skill is

A skill is basically a folder with a `skills.md` file and some additional assets. Skills work through progressive disclosure. First you have the title and description. Then you have the body with more instructions and references. Then the model can go deep into reference files where all of the context lives.

I like to separate skills into two kinds: capability skills and preference skills. Capability skills teach models something they cannot do consistently yet, like tracing logs or creating a React app. Those skills are temporary. The better the model gets, the more likely it is that we can remove them.

Preference skills are more durable. They encode team workflows, style, or company-specific conventions. Those are valuable, and we really want to make sure they keep working when we update our agents.

## Do skills work?

Yes, they do.

Skills Bench has shown that skills improve performance by roughly 15% on average across open and closed models. It covers around 100 different tasks across coding and productivity, and it has a leaderboard and community contributions.

The same benchmark also looked at self-generated or AI-generated skills. That matters because it is very easy to ask a coding agent to create a skill and then just accept the result. But human-written skills are the best we can provide. AI-generated skills can actually hurt performance.

Another useful lesson is that skills should stay lean. If a skill is above 500 lines, you should look at it very carefully. Keep the description short, keep the skill body focused, and push deeper detail into reference files.

## Write directives, not essays

If the description is too weak, the skill might trigger too often or not at all. So you need to be specific about the why, the how, and the when.

Do not write passive prose like, "The Interactions API is recommended for multi-chat because it handles session state." Be more directive: use the Interactions API if you are working on a chat application.

The same applies to negative cases. Always say when not to use the skill. If the skill is only for React components or Tailwind CSS, say that. Do not leave the model guessing.

And test early. Create 10 or 20 prompts: five happy-path prompts, five negative prompts, and then some real production traces if you have them. Real-world data is the best data.

## A simple eval harness

Earlier this year, DeepMind wanted to create a skill for the Gemini Interactions API. The API was released after the last training cutoff, so Gemini did not really know how to use it yet.

We created 117 test cases based on real user data, synthetic prompts, and failure patterns where the model used the wrong Gemini version or the wrong pattern. The result was that performance improved to almost 90% for generating valid Interactions API code with the latest Gemini models.

The harness was intentionally simple. One part was a JSON file with test cases: a prompt, a language, a should-trigger flag, and expected checks. The other part was a Python script that ran an agent and collected the output. Most skill evals can be regex. In our case, we mostly checked whether the correct SDK, model, and methods were used, and whether old patterns appeared.

That makes the eval cheap to run. You do not need an LLM-as-judge for every case, although you can use one when the skill is more complex and you need to inspect traces or multi-step behavior.

## How DeepMind runs skill evals

Internally, every skill has tests alongside it. Each test has multiple cases with prompts. We run them in clean workspaces so the environment is isolated. We can define startup commands, script evals, and LLM-as-a-judge checks.

The important part is that every change to a skill runs through the evals, and the change does not get merged unless it improves the test cases. You can only change the skill if it improves the eval or if you add new evals.

## The practical lessons

The talk ended with a simple checklist:

Write directives over passive information. Include negative tests. Start small. Create outcomes, not paths. Do not test whether the model loads the skill on the first turn; test whether it can actually achieve the task.

Use isolated runs, because coding agents are very good at cheating if they can see prior context. Run more than one trial, because models are non-deterministic. Test across different harnesses, because a skill might work in one agent but fail in another.

And keep the eval even if you retire the skill. If the model becomes good enough without the skill, the eval is still useful. It helps you detect when performance starts to degrade again.

## Homework

If you are back from holiday on Monday, pick your most used skill and write five test prompts. Try to find your most used skills from your trajectories and turn them into evals.

You do not need a huge harness to start. A JSON or YAML file plus a small script is enough. Then run ablation tests: with the skill and without the skill. That is how you know whether the skill is actually helping.

So, don't ship skills without evals. [applause]
