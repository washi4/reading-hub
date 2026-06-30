---
title: "Building Great Agent Skills: The Missing Manual"
date: 2026-06-30
description: "Matt Pocock presents a practical framework for writing great agent skills — a four-part checklist covering triggers, structure, steering, and pruning to escape 'skill hell'."
source: https://www.youtube.com/watch?v=UNzCG3lw6O0
cover: https://img.youtube.com/vi/UNzCG3lw6O0/maxresdefault.jpg
speaker: "Matt Pocock, Creator of MattPCO Skills"
format: Conference talk
language: English
purpose: Read-aloud article
tags:
  - youtube
  - agent-skills
  - ai-coding
  - workflow
  - best-practices
  - matt-pocock
---

Hello friends. I was dearly hoping to be able to come to the AI Engineer World's Fair, but family matters have intruded and I'm not able to make it. However, I will not be leaving you empty-handed. I'm going to give you the talk that I would have given in San Francisco.

This talk is called **The Missing Manual: How to Write Great Skills**. And I think that the ability to distinguish good skills from bad skills is only getting more important.

## Skill Hell

As developers, we seem to be pretty talented at finding different forms of hell for us to go to. A few years ago, we had **tutorial hell** — where you would go into a bunch of tutorials trying to learn something, not be able to piece it together, and get into this cycle you couldn't get out of. We had **framework hell** — where every other 10 minutes there was a JavaScript framework being announced and you had to learn the hot new thing all the time.

And now I think we have another version: **skill hell**. Skill hell is where you have all of these skills available freely available that you can download and contribute to, but you don't really know how the pieces all work together. You can't tell a good skill from a bad skill. This means that people are trying to piece together these frameworks and try everything that's out there all at once, and they don't get the results that the skills themselves promise.

This is true at an individual level, but it's also true at an organization level, too. Organizations have no understanding of how to build good skills — how to take their operating procedures and turn them into things that an agent can do. And if you don't do that, then it's hard to get the bounty that skills can offer.

Just one more skill, bro. That's kind of seems like what we're saying. And I feel a bit of guilt here, too, because we have MattPCO Skills, which is my skills repo, one of the most popular engineering skill sets out there. And so I feel like I want to help the people who use my skills get out of skill hell.

## What Is Missing?

What is actually missing here? In my opinion, the thing that we're missing is we don't know what makes a skill great. We can't yet look at a skill and go, "Okay, this skill is doing these good things and these bad things." There's no shared rubric, no framework for looking at a skill and making it better.

So that's what I'm going to give you in this talk. I'm going to give you a **skill checklist** — a checklist of things you can look at inside the skill to make sure that it's doing what it says it's doing, and ways you can improve it.

This checklist has four parts:

1. **The Trigger** — How the skill is invoked and the decisions that you need to design there
2. **The Structure** — How the skill is actually composed and laid out internally
3. **Steering** — How you get the skill to tell the agent what to do
4. **Pruning** — How to make the skill as small as possible

All of this has been encoded into a new skill in my repo called `writing-great-skills`. If you've got an immediate use case, just go to my skills repo and use this skill to either improve your skills or write great new ones.

## 1. The Trigger — User Invoked vs Model Invoked

In order to talk about the trigger, I'm going to do a bit of comparison. My skills are often compared to another set of extremely popular engineering skills called **Superpowers**. And I'm really often asked: how do your skills compare to Superpowers? What's the difference between them?

To understand that, we need to understand the difference between **user invoked** and **model invoked** skills.

Anytime you have a skill, you can always invoke it manually. The skill sits on your file system. The agent will just be able to pull up the skill and understand what's in there. And you can always do that by communicating that to the agent. That's a user invoked skill.

Another way that skills can be invoked is by the agent itself. These are called **model invoked skills**. You take a description of the skill, the description always ends up in the agent's context, and the agent can look at that and go, "Okay, based on that description, I'm going to invoke the skill and read the rest of it."

### User Invoked Skills

My philosophy is to keep skills user invoked. It puts a bit more cognitive load on the user — you have to remember the name of a skill and invoke it — but it removes the unpredictability of the model choosing when to fire.

Superpowers uses a different philosophy. A lot of its skills are model invoked. The agent will read the descriptions of all skills at startup and decide which ones to invoke during the flow.

### The Predictability Trade-off

The problem with model invoked skills is that you're trusting the model to know when to invoke the skill. Even if you have a perfect description, the model may just choose not to follow it, even if it's absolutely perfect for the task. It may just choose not to invoke the skill. I much prefer removing that level of unpredictability, imposing a bit more cognitive load on the user. What you get is you're removing a class of problem from even being a problem.

This unpredictability leaves people needing to eval their skills to make sure they're being called at the right time, which is really nasty and a problem I prefer to avoid.

But what I'm hoping to show you here is that model invoked skills and user invoked skills both have their costs. So it's not an easy decision which one you choose.

## 2. The Structure — Steps and Reference

I think of there as being two main units that you need to put into most skills:

- **The Steps** — The step-by-step procedure that the skill is going to walk through
- **The Reference** — Any supporting information that helps it walk through those steps

You can have skills that have no steps and are only reference. And you can have skills that have no reference and only a set of simple steps to walk through. But if you start thinking of skills as composed of these two units, it really helps break them down.

### Example: to-prd Skill

One of my skills called `to-prd` creates a product requirements document out of the current context window. It's got three steps:

1. Find the relevant context
2. Confirm the test seams with the user (a human-in-the-loop checkpoint)
3. Write the product requirements document

And it's got two bits of reference material:
- What is a test seam
- A product requirements document template

So this is a great way to write a skill from scratch. You work out if you need some steps, then you write those steps, and you work out what reference material those steps need and put it in a separate spot in the skill.

### Tip: Keep the Main Skill.md Small

Every skill is composed of its **description** and then a **skill.md** file and then any reference material that branches off that. If we make the skill.md file small, we're saving in a bunch of different ways. Smaller skills are just easier to maintain, easier to audit, fewer words to think about. And every time you shave off a word, that is a token saved.

One really useful way you can make your skill smaller is by thinking about the different **branches** of the skill — the different ways the skill can be used. If you have reference material that's only used in one branch, then that's a candidate for being removed from the main skill.md.

For instance, with `to-prd`, we need the PRD template every single time because we are always creating a PRD. So all reference material belongs in the skill.md file.

But consider a different skill of mine called `domain-modeling`. It does two things: it updates a local glossary called `context.md`, and it also creates architectural decision records. In other words, it has two or maybe three branches. This means we don't need to include the ADR template or the context.md template into the main skill. They can be moved into separate files behind a **context pointer**:

```
If you need the template or need to update the context.md file, go to this file.
```

I call that an external reference. It's a reference that's external to the skill.md that you can just easily reference. The agent can pull it in very easily because it's bundled along with the skill.

## 3. Steering — How to Guide the Agent

Steering is about how you direct the agent's behavior inside the skill. And for this, I want to talk about the concept of **leading words**.

When you look at a reasoning trace — the agent's internal monologue before it takes an action — you want certain words to appear naturally. The reasoning trace is the agent thinking through what to do. If we can get the right words into that reasoning trace, we can get the agent to follow our desired path without imposing a huge amount of structure.

For example, in my `domain-modeling` skill, I have three leading words that I want to appear in the reasoning trace:

- **Sharpen** — When we want to update the glossary with new terms
- **Capture** — When we want to record an architectural decision
- **Design** — When we want to design a module from scratch

These words appear in the skill's description and in the opening paragraph. The agent reads them, and they end up in its reasoning trace. This is a lightweight way to steer the agent without heavy-handed instructions.

### Leg Work vs Steering

The rest of the structure — the steps, the reference material — that's **leg work**. That's the stuff that actually does the work. But steering is different. Steering is about putting the right conceptual hooks in the agent's mind so it naturally moves in the right direction.

When you write a skill, you want to maximize the steering density and minimize the leg work for the parts that don't need it. If you find that a skill is doing too many different things, that might be a signal to break it down further.

## 4. Pruning — Making Skills Small

Once we've got a working skill, we need to prune it. Make it as small as possible. This is crucial because every word in a skill is a token that gets consumed every time the skill is invoked, even if that part isn't relevant to the current task.

### Watch for Duplication

Don't repeat yourself. Every part of the skill should have a single source of truth. If you have a piece of reference material like a PRD template, make sure you don't repeat it in several places or cover multiple steps in multiple places.

### Watch for Sediment

Sediment happens when people are working on the same set of docs. Everyone starts contributing to a shared markdown file. People add their own stuff, they don't feel brave enough to delete or modify anyone else's, and you end up with this huge amount of sediment with often irrelevant material.

With a skill with a lot of sediment, you really need to look at structure. Make sure the stuff that's been added is relevant for all branches. If it's not, move it into the correct branches. Or if it's just totally irrelevant, remove it. Or if it's totally stale, kill it dead.

### Watch for No-ops

No-ops are things inside the skill that appear to do something but don't actually influence the agent's behavior inside the context of the skill. This is really common when an agent writes your skills.

Let's imagine we have an implement skill and an entire paragraph telling the agent to write a long detailed commit message. What would happen if you just deleted that paragraph? The agent would probably still write a decent long commit message. That paragraph was a no-op.

People ask me a lot how I get my skills so small. It's using these techniques — deletion tests, making sure I compact things into leading words, not having anything irrelevant, and not having any sediment.

## The Full Checklist

So here's the full sweep of things:

1. **Check the trigger** — Make sure it's firing at the right times. Check whether you're imposing context load or cognitive load.
2. **Check the structure** — Think about branches. Structure things into steps and reference. Make sure material that's only relevant for one branch is outside of the main skill.md.
3. **Check the steering** — Condense text down into leading words and watch those leading words appear in the reasoning traces. Also think about leg work — should you break this skill down further to increase its focus on the current phase?
4. **Prune** — Do a final pruning pass over the entire skill. Watch for sediment, watch for crud, and watch especially for no-ops.

## Getting Started

The best way to get started with this framework is inside the `writing-great-skills` skill. You can check it out from MattPCO Skills, download it, use it to improve your own skills, and maybe even use it to run over some community-authored skills so that you can check whether the skills you're actually pulling in are any good.

If you want to follow along with my stuff, then I have a newsletter up on aihero.dev. And my plans for the next few months are to release an AI coding crash course, which is an intro to a lot of the stuff I've been talking about and how you get off the ground working with engineering and AI.

I hope that what I've given you is enough to help you escape from skill hell, or at least try to make the bitter journey out of there. I'm so sorry not to be able to attend in person, but thanks for watching. I'll see you very soon.
