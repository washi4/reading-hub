---
title: "L8 Principal's Agentic Engineering Workflow"
date: 2026-06-23
description: "Former Meta/Microsoft/Atlassian L8 principal engineer Kun Chen walks through his complete agentic engineering workflow — from terminal setup and memory management to parallel agent crews and a first mate that orchestrates everything."
source: https://www.youtube.com/watch?v=iQyg-KypKAA
cover: https://img.youtube.com/vi/iQyg-KypKAA/maxresdefault.jpg
speaker: "Kun Chen, Former L8 Principal Engineer at Meta, Microsoft, and Atlassian"
format: Technical talk + Walkthrough
language: English
purpose: Read-aloud article
tags:
  - youtube
  - agentic-engineering
  - ai-coding
  - workflow
  - terminal
  - claude-code
---

Hi everyone, welcome to this video and this will be a full walkthrough of my agentic engineering workflow.

My name is Kun. I was previously an L8 principal engineer worked at Meta, Microsoft and Atlassian on many large scale systems like the Bing search engine, Windows and Facebook games. In the recent couple of years, I have been building frontier coding agents at Atlassian and helped many engineering teams figure out how to use them effectively. And I have been building heavily with agents myself and shipping 40 to 50 PRs almost every day, sometimes more. And these are all well-tested and shipped to production, not those Minecraft demos you see people vibe code on social media.

I have shaped my workflow to be both highly productive and enjoyable. Many people recently asked me what it looks like. To be honest, I did debate a lot with myself whether I should make this video a paid course because it does have that level of value. But ultimately, I decided to just share it here with everyone because I want to stay focused on building products as my main business.

You can see this is a bit of a long video because I'm going to walk through many fundamental concepts of agentic engineering that not only show you how I do it, but also the why and how things really work under the hood. These are not gimmicks that look cool, but can't actually be used for real work. These are all real workflows that professionals like myself use to get real work done.

By the end of this video, I want you to feel like a captain that can sail a large ship with a crew of agents working for you and do so in a stress-free and satisfying way.

## Chapters Overview

Largely speaking, we will be walking through these chapters. We'll start with assembling our ship where I will introduce the core setup. We will then talk through how we recruit and ramp up our crew mates with the right usage of memory and skills. I'll then demonstrate how we work with a single crew mate effectively. Then we'll upgrade to working with multiple crew mates all at the same time. And lastly, we will recruit a first mate that manages a lot of the overhead for us so we can stay focused on the big picture as a captain.

## Assembling the Ship — Terminal-Centric Workflow

The very first level is to gather our gears and build our ship. Now, as we get into my workflow, something that's going to be really hard to miss is that I do almost everything in my terminal. I know there are a lot of people who will tell you that the graphical user interface is better. It allows richer interactions and better visuals. But I think by the end of this video, I might just be able to convince you that terminal is not quite that yet.

I use the terminal mostly for two very real reasons. One is to allow my hands to almost never have to leave the keyboard. This is actually a much bigger deal than most people think because when your hands stay on the keyboard, you stay in the flow. But if you have to move your hand to the mouse every couple of seconds, it breaks the flow and forces your brain to context switch. I know there are some GUI apps that also have great keybinds that allow you to do most things with the keyboard as well, but that's just not the primary interaction paradigm for GUI apps, and it's hard to build the discipline of hands-on keyboard when every once in a while you still have to use the mouse. Terminal apps, on the other hand, are all designed for the keyboard. So, there's no reason for your hands to move anywhere else.

The other very important factor that drives me to use the terminal is that I can keep the exact same workflow everywhere, even on my phone. But if you really don't like the terminal, that's okay, too. I designed this video to be more about the fundamental concepts behind agentic engineering rather than the mechanics. So, most of the things that I talk about should be applicable to GUI based workflows as well.

### Westerm — The Terminal Emulator

I'm using this beautiful, clean, and elegant terminal emulator you're looking at here is called Westerm. Westerm is a highly performance terminal emulator built by a guy named Wes. It's got 26k GitHub stars and has existed for many years. I like it mostly for two reasons. One is that it's truly crossplatform. It's pretty much the only terminal emulator I can find that can work on Windows exactly the same way it works on Mac and Linux. Right now, I mostly only work on Mac, but it was a big lifesaver when I was working for Microsoft and was forced to use Windows for work.

The other reason is that it's highly customizable. You can write Lua scripts to configure pretty much everything here. Let me show you my config in my files. It's all in this file called `westterm.lua`. It's a Lua script. So, it's not just static values. You can actually set conditions and write various kind of logic to make your config very dynamic and flexible. If I change some settings here, let's say I change the color scheme to chalk, you will see that it does a hot reload instantly, which is super handy. But I still like my rose pine moon.

### T-Max — Terminal Multiplexer

Inside of Westerm, I run something called T-Max. It's short for terminal multiplexer. If you haven't come across this yet, it's probably easiest to just show you what this does. So, I'm typing this command here to start a T-Max session. Now, I'm inside of T-Max. You can see not much is different except for that there's a bar at the top showing some information. And I still get a shell where I can type commands. But now I can split my terminal into multiple panes, as many of them as I like.

This is super useful because I can spin up an agent in one pane and spin up an editor in another and still have a pane to myself. So I can just run commands. I can also spin up multiple tabs and they are also called windows in T-Max. This is very useful for running multiple agent sessions in parallel.

The other cool thing is that T-Max sessions are persistent in the T-Max server. So, if I use a keyboard shortcut here to detach from T-Max, you can see I'm back in the normal shell without the T-max status bar at the top. But if I type the same command to launch T-Max again, I get back to the exact same state I was in before. So, I can continue my work here. What's even more useful is that I can connect to the same session from another device like my laptop or my phone. That's a real game changer that's very hard to replicate without this terminal centric workflow.

If you just install T-Max, by default, it doesn't have the same experience we're showing here, like the tab bar and the metadata. You'll probably need to do a bit of configuration and customize it. Let me show you my T-max config. Most of these settings are key binds that I have been using for many years and built into my muscle memory. Some of these are for styling and various kind of behaviors.

### NeoVim — The Text Editor

This text editor here is NeoVim. It's basically the modern version of Vim. It's my favorite text editor. If you are not familiar with Vim yet, it's an editor whose main purpose is to keep your hands on the keyboard. So, if you watch my keystrokes here, I can move the cursor up and down, left and right with keys. I can also scrub up or scroll down. If I have to make edits, I can go into insert mode and start to type anything I like.

There are a ton of keyboard shortcuts for doing everything you need. For example, let's say I want to delete the current line. I can just type `dd` and it's gone. I can undo it by typing `u`. Oh, and if you look at the left hand side, I have relative line numbers. This line number 238 is the current line number. And the line above shows one, which means it's one line above. And this helps me navigate quickly using the keyboard.

### Claude Code — The Primary Agent

If you look at the left pane, this is one of my crew mates running, and it's Claude Code. You can tell because the input has this `▶` icon. Claude Code is my primary coding agent. It is the most used tool in my workflow. It can do things like reading files, writing code, running shell commands, creating and managing git branches, and many more. By default, Claude Code already knows how to build software with a lot of modern frameworks.

But the real magic is that Claude Code can also be extended with custom tools and custom skills. So, the more you use it, the more powerful it gets. This is what makes it so great because it can evolve with you and your workflow, not the other way around.

## Recruiting and Ramping Up Crew Mates — Memory and Skills

Something you want to establish early on is a way to persistently level up your agents. You want an agent that gets smarter over time, not one that starts from scratch every session. So let me talk about my memory and skills setup.

### Claude Code's Built-in Memory

Claude Code actually has a mechanism for managing memory files. It comes with two types of memory files. One is the global memory file at `~/claude.md`. And the other is project memory files stored in the project's root as `CLAUDE.md`.

The way I do this is that I put information that's relevant to all projects into my global memory file. Things like my biome configuration, the colors I like for my logs, or any rules or conventions that are consistent across every single project that I use. You can customize this global memory file to any degree, and I encourage you to put useful stuff there.

### Global and Project Level Memory Files

Besides the global memory file, each project can also have a project level memory file. The project level memory file is typically stored as `CLAUDE.md` or `AGENTS.md` depending on which agent you use. I did the same thing here with a symbolic link, so the same file is shared for both Claude and other agents.

It has some context on what this project is, how the repo is laid out, some terminology, how some of the most important components work, and how to do end to end testing and some conventions at the bottom. This file is a lot more verbose than the global memory file because this is basically the collective learning of all the agent sessions in this project.

The way I built this file is not by writing everything by hand, but rather that every time I saw the agent doing something wrong, I would correct it and ask it to remember to not make the same mistake again by storing the learning into this memory file. So over time, our crew mates working on this project get smarter and more experienced. You don't need any fancy memory system to do that. This markdown file is all it takes.

### From Memory to Skills

Over time, it does tend to get more and more bloated though. One way I reduce the size of this file is by moving some conditional information that is not always needed into a skill. For example, the end to end testing instruction is only needed if the agent is making changes, right? So, if I just ask the agent a question, this whole section is totally useless and would be wasting tokens.

The way to improve efficiency here is by converting this kind of conditionally useful information from the memory file into skills. I typically just ask the agent to do this. Claude already knew how to do this, what skills mean, and how to create them. But other agent harnesses may not understand how to do that out of the box.

To teach your agent how to create skills, you can install a skill called skill creator which was written by Anthropic. You can do that by running this command: `npx skills`. This CLI from Vercel is very handy. It's basically my main tool for installing and managing skills. It supports pretty much any agent.

### The Power of Progressive Disclosure

Skills are designed for progressive disclosure. Which means when your agent starts, it only loads this tiny description field from your skills into the system prompt to know what these skills do. And only when it actually decides that it needs to use a certain skill, it will then read the rest of this file. This allows you to store a lot of the knowledge about how to do various kind of things without blowing up your system prompt and memory file with a ton of content that uses your tokens for every single request whether the request actually needs those skills or not.

### A Warning About Random Skills

One thing I do want you to know about skills is that you should generally avoid installing random skills from the internet even the ones that have a lot of GitHub stars. First of all, these skills can instruct your agent to run pretty much anything on your machine. This is a very risky thing to do because the agent can leak your API keys or even credentials to your bank account to untrusted third parties without you knowing.

And even if we put aside the security problem, some of the skills actually degrade your agent's performance. Look at this repo here called Andre Karpathy's skills which has 177,000 GitHub stars. That's like massive. So, it must be really good, right? I actually evaluated the skill in this repo with program bench, which tests the agent's ability to build programs end to end. And the result shows that by using this skill, the agent will use 5% more tokens while making the results worse. And if you look closely, this skill is not even written by Andre Karpathy himself.

I'm not here to criticize the author of this repo, though. Being popular is not the same as actually being good. A lot of the skills being widely shared today have not been rigorously evaluated and are typically just some random guy who found something that worked for themselves anecdotally and somehow got it to go viral. Their GitHub stars only tell you how popular they are and not whether they are actually helpful.

So, as a general rule of thumb, I recommend that you do not install any skill from the internet without evaluating it yourself.

## Working with a Single Crew Mate

The first thing about working with a crew mate is how you talk to them. I treat my agents like an incredibly talented but junior engineer who just joined my team. This mental model helps me communicate with them properly. It also helps me set expectations around what they can and cannot do.

I never tell them how to do something. I tell them what I want and let them figure it out. Because if I tell them how to do it, I'm doing half the work, and I could have just done it in the first place. The purpose of using an agent is to delegate, not to micromanage.

So what does an effective prompt look like to me? It's basically a product spec. It describes what needs to be done in terms of what the user should see and how the user should feel, not how the code should be written. It should also specify the acceptance criteria that I will use to validate the work. It doesn't need to be long.

### The No Mistakes Pipeline

But what I found is that even with a perfect prompt, the agent will still produce questionable code. Humans at work don't review their own PRs. We rely on code review to catch our mistakes. An agent is not going to catch the mistakes they just made because they haven't seen the code they just wrote from a fresh perspective. So, we need a code review process for our agents.

When I started, I used to just review the diffs myself and it was pretty painful. I realized that in this age of AI, our job as engineers needs to shift more towards that of an engineering manager or engineering director. Your directors most likely don't review any PRs. Yet, they can influence the quality of their team's software by creating good culture and processes and rely on the team to carry them out. That's what we should do with AI.

What I do here when the agent says the work is done is not to start reviewing the diffs or start manually testing the changes. That's too much overhead on myself. I send the change into a pipeline I built called **no mistakes**.

No mistakes is also free and open source. It orchestrates your agent to execute a series of steps that takes this first pass code all the way through to a clean PR:

1. It would first create a branch if one doesn't exist yet and then create a commit.
2. It takes the change through a pipeline in an isolated work tree. So nothing during the validation would affect your current repo.
3. It understands your real intent behind the change by analyzing your agent session.
4. It rebases the change on top of the latest main branch on remote origin and resolves merge conflicts up front.
5. It starts an adversarial review in its own fresh context window. This is where most problems get caught — obvious problems will get self-corrected, but ambiguous ones that have product implications will be escalated to us humans for a decision.
6. After review, it tries to test the change end to end against the original intent. This step records evidence that proves the change is working that we can later on look at to gain more confidence.
7. It does a documentation pass of updating all relevant documentation to reflect the latest change.
8. It makes sure there's no linting problems before pushing the branch to remote and raises a PR.
9. The no mistakes pipeline will also keep babysitting the PR until it's merged. Because during the PR phase, we can still have merge conflicts that come in or CI pipeline failures.

With no mistakes during the babysitting, we don't have to waste our own time at all. Another way to trigger no mistakes is as a skill. I can just type `/no-mistakes` in the agent and it will do the same pipeline.

This may seem very slow, but in practice, I never stare at this screen. I would go spin up other tasks. I come back only when no mistakes says all checks passed. And that's when I go to the PR and apply my judgment.

Here's the PR from the change we just did. We can see here it summarized the original intent, what changed, how it's tested, and what happened during the no mistakes pipeline. We can click to see the evidence from its testing to know whether it's really done what we asked for. Depending on what the change is, the evidence could be a screenshot like this, a video demo, a log file, or something else. It's designed to give you the most direct way to see the change working as you intended.

We can also see that the pipeline discovered some problems and fixed them before raising the PR. This is a good time to audit whether these changes are actually what we need. If anything doesn't look right, we can go back to the agent and ask for more changes before merging this PR.

The risk assessment here is also very useful. I basically look at this to decide how much time I should spend on reviewing this change in more detail. For low-risk changes, I don't really look at the diff at all because I have validated time and time again for low-risk changes.

### Real Example: Finding Usability Problems

Let me show you a real example that I often do. I go into a project and I say to the agent: "In the rest of the app, try to do different things and find the first usability problem that would confuse you as a kid or stop you from knowing how to proceed."

This kind of prompt is great because it turns the agent into a QA engineer that will go and explore the full surface area of the app, looking for rough edges. And then it comes back and tells me what it found. This is extremely useful because as a developer of this app, I've become blind to these rough edges. The agent brings a fresh pair of eyes that can see what I can't.

## Leveling Up — Working with Multiple Crew Mates

This is when we level up and start working with multiple crew mates in parallel. Taking full advantage of having more than one agent working at any given time is probably the single biggest unlock for productivity. It opens up a whole new paradigm of how you approach software engineering.

It's no longer about just writing code faster. It's about being able to do multiple things at the same time. It's about having a crew.

The trick to making this work well is to leverage T-Max workspaces. A workspace in T-Max allows you to have a group of windows and panes that you can quickly switch between. I typically create one workspace per project. And within each workspace, I can have multiple windows representing different agent sessions working on different tasks in this same project.

### Treehouse — Worktree Management

One thing you'll need to use when working with multiple agents on the same repository is branch isolation. Without it, two agents making changes in the same repo at the same time will step on each other's toes. The way we do branch isolation is by leveraging a git feature called git worktrees.

Of course, creating worktrees by hand is tedious. So, I built a tool called Treehouse. Treehouse is a CLI tool that manages git worktrees for you. The way I use it is by just calling my agent and telling it to use Treehouse to spin up a new worktree with a certain description. For example, I might say: "Treehouse claw. We need to add a dropdown menu for image attachment."

What happens is Treehouse creates a new branch based on the latest main, creates a worktree in an isolated directory, and starts a new agent session inside that worktree. And now I have a clearly labeled agent working on a clearly scoped task, completely isolated from my other sessions.

I can have Treehouse manage its worktree state in a file so next time I come into this hybrid 2 directory, I would wonder what was I doing in this work tree last time. Treehouse also uses a pool of idle worktrees. So next time I ask for a work tree, it will try to reuse one of the idle work trees instead of creating a brand new one.

### Spinning Up Parallel Agent Sessions

Now, you can start stacking these real fast. Let me spin up a few. I'll say: "Treehouse claw. We need to add a cool dropdown menu for the image attachment. When users hover over the image attachment button, they will see a popover. Maybe in the popover we add a label that tells them they can also press and hold and I'll enter."

Then I'll spin up a new tab: "Treehouse claw. The image attachment dropdown menu should have an action that takes a screenshot of the current app and use that as the attachment."

All right, one more tab: "Treehouse claw. Our agent status bar right above the chat input is not always showing bot activity. Look into what happened there and make sure when any bots are in progress, it always displays something that reflects the latest activity."

Boom. We now have three sessions running in parallel. Now I can keep going because none of these sessions will need my attention anytime soon. Especially if I tell them to run no mistakes after implementation. I know whether they need me by looking at the top status bar and I can switch between the tabs using keyboard shortcuts like this. That's very important for managing a lot of parallel sessions efficiently.

## The First Mate — From Sailor to Captain

That said, after doing this for a while, you will discover that juggling between all these sessions is quite exhausting. The constant context switch and having to remind yourself what each session was even doing just doesn't feel like an ideal endgame experience. So, I kept pushing the boundary on this.

And I discovered that I needed a **first mate**. Someone I can talk to as a captain that will carry out all my directions and manage all the crew mates for me so I can focus on the big picture stuff like where should we go next? Not playing whack-a-mole with this increasingly high number of crew mates.

This is how I level up and truly become a captain. My first mate is another free and open-source project and it's very new. The way to use it is by just cloning it. And then I can run an agent in this repository. Now I just talk to it and ask it to work on any projects I like.

First mate is asking how strict I want to be with the code changes in these repos and I want to select full gate to PR. This is basically going to be using no mistakes as the pipeline to validate each change.

Now, a real thing I want to do is for all three projects, I'd like to add an update command on the CLI that will update their version to the latest on npm. And let's see what first mate does. It realizes that this is not one task, but three parallel tasks. And it's now spinning up these tabs in T-Max just like we would behind the scenes. It would also call Treehouse to create work trees and then run an agent in that work tree to get the work done and then it will run no mistakes to validate the change and get the PRs ready for us to review.

Now you can see it's first mate that is doing the juggling. I don't need to worry about any of this now. I can just keep giving it more work.

"Hey first mate, let's also look at the most recent three open issues in the Lavish AXI repo and let's discuss which ones are actionable."

Boom. First mate now is pulling the open issues from the repo while waiting for the three background agents working in parallel. First mate said number 87 is cleanest, very actionable. It's a clear bug — don't toggle in annotation mode.

"All right, first mate. Let's address number 87."

Look now, first mate is juggling a lot of tasks for me that I otherwise would have to manage by myself. Watching it context switch is actually an oddly satisfying experience because I know that's what I would have to do otherwise. First mate is basically all my tools coming together as one cohesive workflow and I have been really happy with it. It's been a pretty significant improvement to my overall experience working with agents. I highly recommend trying it out if you are still directly talking to every single agent session one by one. It will be a pretty massive upgrade.

### The Captain's Mindset Shift

Something you'll start to notice after having a first mate is that because first mate took care of so many things for you, you start to run out of ideas for what to ask it to do. This is a good thing because it indicates the bottleneck is shifting. But it also means you as the captain needs to keep up.

This requires a mindset shift of focusing more of your energy on understanding what matters by talking to your users, understanding the competitive landscape, and crafting a good treasure map that can lead your crew to a good direction. Once you started doing that, congratulations. You have successfully transitioned from a sailor into a great captain.

## Wrapping Up

All right, we have gone from not having a ship to being a captain that has a first mate and a big crew that sail together. This is a pretty good time to wrap up this video. All my tools can be found on my GitHub and will be linked in the description below. They are all free and open source. I built them because I just want to see more people learning how to do agentic engineering effectively and doing it in an enjoyable way. And that's what I hope you can get out of this video.

I will continue to share more of my workflow and things I find useful on my channel. So, don't forget to subscribe if you don't want to miss anything.
