---
title: "Finally. Agent Loops Clearly Explained."
date: 2026-06-23
description: "Nate Herk breaks down what agent loops actually are — the difference between prompting agents and designing loops, when to use them, and how to build loops that actually work."
source: https://www.youtube.com/watch?v=EuzYhzB0vbI
cover: https://img.youtube.com/vi/EuzYhzB0vbI/maxresdefault.jpg
speaker: "Nate Herk, AI Automation Educator"
format: Technical explainer + Walkthrough
language: English
purpose: Read-aloud article
tags:
  - youtube
  - agent-loops
  - ai-coding
  - workflow
  - automation
  - claude-code
---

Right here, I've got four different agents that are looping, calling other sub agents, and writing all these prompts for me, and designing systems for me. But, is this actually productive, or is that just a cool demo?

Here's your monthly reminder that you shouldn't be prompting coding agents anymore. You should be designing loops that prompt your agents.

Boris Cherny and Peter Steinberg publicly said they no longer prompt their coding agents. They write loops. A loop is three things: a trigger, an action, and a stop condition. If you're still writing prompts for coding agents, you're falling behind. You need to build a meta agent that infers what loops you would have wanted based on your vibe, and then write those loops.

## What Are Agent Loops?

We're seeing a ton of talk about agent loops, loop engineering, whatever you want to call it. So, I wanted to make a video to clear up what that actually means. Because I think that everyone kind of has their own spin and a different definition of what this is, and it applies to everyone very, very differently.

I think that this definition sums it up pretty well. **Loop engineering is replacing yourself as the person who prompts the agent. You design the system that does that instead.** A loop here can be thought of as a recursive goal, where you define a purpose, and the AI iterates until complete.

And there's really two most important pillars of that in my mind:

1. **The goal** — What is the actual objective? Something typically that's objective, not subjective.
2. **Verification** — How does the agent know what that stop condition is? How does it check and iterate?

## Do You Actually Need Agent Loops?

If you take all that advice and then you start designing swarms and fleets of agents that constantly run 24/7, then you need to think about: what are you actually doing here? And is this actually moving the needle?

I thought to myself, how do I actually use agent loops? Because when you read some of those tweets, you kind of think to yourself, "Okay, if I'm not having five agents that are continuously around the clock orchestrating five of their own agents, then I'm falling behind, or I'm not using my Claude subscription in the best way." And I think that that's very false. Because if you don't understand what you're doing, then you're probably just going to scale problems, and you're going to have a ton of bugs and a ton of things that you're going to have to fix later.

And also, not all of us are in a scenario where having agents work 24/7 around the clock actually benefits us. For example, I don't. I have agents that do things on a certain cadence and I have agents that do things based on certain event actions, but just having them do 24/7 work for me isn't helpful. I think if I was working with a team on a codebase and we were building a product and we were constantly iterating and pulling in different things, then it would maybe make more sense, but for me, that doesn't apply.

So, I just wanted to come in here, explain this as simple as I can, and hopefully shed some light on where you guys can start applying loops into your workflows and why and how.

## How an Agent Loop Works

An agent loop is just an AI that:

1. **Reasons** on what to do
2. **Acts** on what to do — starts implementing
3. **Observes** the result
4. **Repeats** over and over until some sort of goal is met

A really simple visual that I like to think about: **AI is never perfect.** It's never going to one-shot something and you just accept that final output.

If we have attempts on the x-axis and quality on the y-axis, let's think about this. On attempt one, if you are just giving your agent some sort of simple task, maybe you get to 50%. Then you look at that and say, "Okay, here are some changes to make." By attempt two, maybe you bump up another five or 10%. Every time that you give more feedback and iterate, you just kind of keep moving up on quality until you hit somewhere where you're okay with that, 90, 95%.

The whole idea is: **why don't we outsource this feedback and iteration loop to an agent rather than having the human do that?** Because this is going to happen either way. So, if we have an agent do that instead of a human, the agent can go much faster, run through many more attempts, and it can even find ways to speed up the process itself.

### The Cake Test

Think of it like baking a cake. When you're making a cake, you stick the fork in it, and when it comes out and it doesn't have batter all over it, that means it's done. That's a **done criteria**. How do you tell your agent something as objective as possible: what is the stop criteria, what is the definition of done?

So what the agent will do is it will reason, it will plan out, and then it will start to implement. After it implemented, it will observe. Maybe that's visual verification, maybe that's running an actual code test. Whatever it means to verify, it has to verify. Then after it looks at the results, it will say: "Did I meet this done criteria? If no, I'm going to act again, then observe again, and then reason. Otherwise, I'm going to stop."

## Different Types of Loops

The majority of tasks don't need massive loops. But I've started building some sort of loop for most of my tasks, just because of that verification piece. This piece is so important. But a lot of times, you don't need some sort of massive agent architecture in order to run a dynamic looping workflow. You just get it done with one simple terminal session and a good prompt.

Here are the patterns I see most:

- **Solo loop** — One agent that's reasoning, acting, observing, and repeating. This is what I'm typically doing the most.
- **Maker-checker** — One agent that does the thing and then one agent that grades the thing and gives feedback.
- **Manager with helpers** — One main agent that's orchestrating the whole thing with sub agents.

## Real Example: Thumbnail Generation

This first example was from Matthew Berman's Loop Library. I used a `/goal` prompt in Claude Code to make me a thumbnail.

The prompt was: "Make 10 thumbnail concepts and score each one against Mr. Beast YouTube thumbnails using a rubric. Clarity at small size, curiosity, emotional pull, visual contrast."

After it makes those 10, it selects the top three, it identifies the weakest part of each concept, it improves them, rescores them, and then it continues iterating on the strongest concept until it's satisfied.

One of the issues with this prompt is that the definition of done was "until you're satisfied." Sometimes you have to have these subjective sort of grading criteria, but you want to get it as objective as possible. **The best agent loops are where you literally say: "Keep iterating until X metric equals Y result."**

It created 10 thumbnails — number one through number ten. It ended up choosing number one, number two, and number eight as the top contenders. Then it iterated on these. Here's number one original, here's number one V2, here's number two original, here's number two V2, and here's number eight original, and here's number eight V2. After those version twos, it said, "Okay, number eight's the best. So, here is number eight V3."

This was the final thumbnail we got after running this goal, which took Claude Code **27 minutes**.

If we wanted to improve this flow, we would try to figure out how to make this scoring more objective. Maybe create a separate sub agent that was a dedicated scorer, and prompt that scoring agent and run it through a bunch of evaluations so that we could feel more confident about its scoring ability.

## Real Example: 3D Model with Three.js

The next one was another `/goal` prompt. This one took **37 minutes**. The prompt was from Matthew Berman's Loop Library — it was basically supposed to make a plane using Three.js.

We can see this is the spinning plane that it made. We can sort of zoom in, move it around. From a looping perspective, what it had to do was it had to build it and then check it against the prompt. Verify itself.

This is where the real power of loops comes in. When I first manually prompted Claude Code to generate Three.js demos, they would pretty much always be broken. But when you make it loop, it can check itself against its own output and fix issues. So this is the single most valuable piece.

## Real Example: YouTube Video Transcription

Even the transcript for this video — the captions that you're watching right now — was created using an agent loop. What the loop does is it takes the raw YouTube transcript, breaks it into scenes and beats, removes mistakes and pauses, generates visual cues and overlays, and then syncs everything.

Every time I have to make one of these videos, I basically chuck it in, do a `/goal`, and it does everything for me. It has to get the transcript, cut out the mistakes and the pauses, it has to make the beats, it has to sync the beats, it has to render them, and then it has a ton of verification on making sure that all of the beats are in bounds and that they line up with the transcript correctly.

That is how you're able to see a lot of these people say, "Okay, I did this with one shot, with one prompt." Because it was a loop, because it had verification and iteration.

## What Makes a Loop Actually Work?

- **A checkable goal** — Something objective you can measure against
- **A hard stop** — Prevent infinite loops
- **Good tools** — The agent needs the right capabilities
- **Memory** — Track what's been tried
- **A separate checker** — Fresh perspective for verification
- **Planning first** — Reason before acting
- **Logging** — Know what happened
- **Cost awareness** — Loops can run for a long time

A lot of times these loops can run for a long time, and especially if you have a pretty hard goal that might take a lot of iteration, and then if the done criteria is also very hard where maybe it just can't actually ever hit that, then that thing's going to run for a long time. I've had a couple loops that have gone for **12 hours plus**, and they're just not super useful to me. Most of the time when I'm running loops that run for a while, it's usually more like 35 minutes or maybe a couple hours.

## Don't Overthink It

Just because you're seeing someone like Peter Steinberg saying something about agent loops doesn't actually mean that this applies directly to you and your use case. Because he's a hardcore coder, he's building agents, he works at OpenAI. This probably makes a lot of sense for the way that he works and has probably 10xed his productivity.

That's the cool thing about AI — it's going to seep into every single vertical and every single role. Not everyone will use it the same. So, it's good to stay up to date with what people like Peter Steinberg are saying, but that doesn't mean you have to drop everything right now and go try it. Or maybe it's good to try it, but that doesn't mean you have to fully integrate it into every single Claude Code session forever.

Coming from a non-coding background, from a perspective of someone who uses Claude Code all the time, 24/7, but uses it for knowledge work rather than massive database codebase refactors — that's the way that I feel about these agent loops. I do use them, I just don't go for those fancy runs that run for three days straight.

A lot of times if I have a big goal, I will shoot off a nice chunky loop before I go to bed, and I can wake up with something that's run for maybe four or maybe eight hours, and that is truly very beneficial. A lot of that stuff is more experimental for me, and then I'm able to take that output I got from the overnight run and then chuck it back into some more loops or iterate on that myself as a human.

So, there's a little bit more detail that was covered in this slide deck as well as this full audit, which is way more wordy and super ugly to look at. The link for that is down in the description. You'll hop in the free school community, go to classroom, click on all YouTube resources, and you can find everything in there.

But, that's going to do it for today. If you guys enjoyed the video or you learned something new, please give it a like. Helps me out a ton. And as always, I appreciate you guys making it to the end of the video, and I'll see you on the next one.
