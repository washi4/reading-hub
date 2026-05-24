---
title: "Build Core Skills to Thrive as an AI-Era Developer"
date: 2026-05-24
description: "Google's developer intelligence team shares research on the T-shaped engineer model — the skills, patterns, and mindsets needed to thrive when AI handles more and more of the execution."
source: https://www.youtube.com/watch?v=q_Jq4IgYImk
cover: https://img.youtube.com/vi/q_Jq4IgYImk/maxresdefault.jpg
speaker: Andrew and Nicole, Developer Intelligence Team at Google
format: Conference talk (Google I/O)
language: English
purpose: Read-aloud article
tags:
  - youtube
  - ai
  - software-engineering
  - google
  - career
chunks:
  - text: "T-shaped software engineering"
    type: chunk
    meaning: "T 型工程师——横向广博基础 + 纵向深度专精"
  - text: "shifting left on intent"
    type: chunk
    meaning: "把意图前置——在开发流程更早阶段明确目标和决策"
  - text: "delegate tasks, not judgment"
    type: formulaic
    meaning: "委派任务，而非委派判断力"
  - text: "garbage in, garbage out"
    type: formulaic
    meaning: "垃圾进，垃圾出（输入差，输出也差）"
  - text: "force multiplier"
    type: collocation
    meaning: "力量倍增器，增效器"
  - text: "cognitive debt"
    type: collocation
    meaning: "认知债务（积累的未消化复杂性）"
  - text: "blast radius"
    type: chunk
    meaning: "爆炸半径——出错时影响范围"
  - text: "spec-driven development"
    type: chunk
    meaning: "规格驱动开发——先写详细需求再执行"
  - text: "value translators"
    type: chunk
    meaning: "价值翻译者——把用户/业务需求转化为精确的技术要求"
  - text: "productive struggle"
    type: collocation
    meaning: "有成效的挣扎（刻意练习中必要的困难）"
  - text: "psychological safety"
    type: collocation
    meaning: "心理安全感（团队中可以安全犯错/发言的文化）"
  - text: "automation trap"
    type: chunk
    meaning: "自动化陷阱——过度委派导致质量失控"
  - text: "agent sprawl"
    type: collocation
    meaning: "智能体蔓延（agent 数量失控难以管理）"
---

[music]

Hi everyone. How are we doing?

[laughter]

We're Andrew and Nicole. We're both leads on the developer intelligence team here at Google. Together we spend our careers studying software engineers — the people, the processes, the tools, the systems, the culture. We want to start by recognizing this is a big moment for software engineering. You see quotes that really emphasize not just the magnitude of the moment, but the speed at which change is happening.

Our goal today is to share some of our research, some of our knowledge about what we're seeing inside of Google, and ultimately answer this question: **How can we, as software engineers, continue to thrive in the AI-native era?**

We're going to walk through this T-shaped software engineering role that we're seeing really grow in importance. We'll detail some of the patterns in how software engineering is being done, the skills and capabilities we're seeing our top engineers embody, and introduce practical tips for how you can think about your role.

## Setting the Scene

First, we want to make sure we're all on the same page. This is a big moment, but what's actually happening?

We're seeing fairly pervasive adoption of AI tools for software engineering — probably not a surprise to anyone here. The majority of tech professionals are using AI and relying on it, in many cases, a lot.

We're also seeing profound impact. Inside of Google, three quarters of all code is written by AI. At the same time, people are very reasonably asking: is it actually improving productivity? Is it 10%? 10x? 100x? The truth is, in some places there's even a productivity paradox occurring. Our DORA team found that increasing AI adoption can lead to individual productivity benefits while simultaneously decreasing team-level benefits.

Over the last year inside of Google, we've seen some really interesting patterns emerge. Not only is AI generating an increasing amount of code with more autonomy, we're seeing that with the right systems and environments in place, that code actually lasts. This presentation is about the skills and capabilities that allow that to happen.

There are also interesting emergent behaviors beyond those top-line numbers. The engineers that use AI the most are actually spending more time coding, more time ideating, and more time collaborating with their peers. This is maybe counterintuitive — they're doing more of these activities; the shape just looks a little different. Our top-performing engineers are more active, not less, even though they're delegating more work to AI.

Now, those AI benefits aren't necessarily homogeneous. We all know the old adage: garbage in, garbage out. We've seen research around the need to not only master working with AI, but also the context and domain in which you're applying it.

Furthermore — and this is likely preaching to the choir — software engineering is so much more than coding. Coding was never actually the bottleneck. To get the true benefits, we need to recognize two things. First, think about AI for the entire software development life cycle, not just code generation. Second, this isn't about applying AI to old ways of working. The magic happens when traditional processes are evolved and even transformed. We're seeing totally new processes emerge with totally new roles in the SDLC.

## You Are Not Alone

So I go back to the question: this is a lot of change to deal with. Hopefully today I've got two pieces of good news for you.

The first: however you are feeling, trust me, you are not alone. There's a lot of research on this, and a lot of really complex emotions are emerging. None of this is surprising given the size and speed of change. The excitement is real, the opportunities are real, but it is a lot.

The second piece of good news: this talk is about how you can rise above all of this and continue to thrive in this AI-native era. There are no magic wands, but there are ways to thrive. We're seeing strong evidence that despite the new shape of the software engineering role, when the change is approached intentionally, this really can and should be the most exciting time to work in this field.

## Five Patterns of AI-Native Engineers

Let's talk about the patterns we're seeing in our highest-performing engineers who are really adopting an AI-native approach. As Andrew mentioned, our job is to study and measure the engineering system and all the pieces within it. We're measuring end-to-end time — how long it takes from an initial seed of an idea all the way to getting it into a real user's hands. Not just coding, but the entire product development process.

In that system, our most productive AI-native engineers are doing a few things differently. Here are five patterns.

### Pattern 1: Operating at Higher Altitudes

These engineers are combining their engineering knowledge with their understanding of business context and user needs. They're thinking deeply about *why* they're building, not just what or how.

This has always been what's expected of senior engineers. But now that AI is accelerating execution, doing it well has never been more important.

### Pattern 2: Shifting Left on Intent

Traditionally, "shifting left" meant moving testing or security earlier in the SDLC. But today, with more work being handled autonomously by agents, we need to shift left on intent. We need to spend more time and energy upfront to plan, explain clear instructions, talk about trade-offs, and provide the right context.

A fundamental source of truth is moving away from the code itself and shifting toward the structured intent that happens upfront. Our engineers are writing specification files — which, if we think about it, is really product thinking made explicit. This helps guide AI, but it also documents decisions much more explicitly.

As agents take on more execution, they need to know these trade-offs. Building without capturing intent is tempting — it's fun on a weekend — but we risk prototypes that no one understands the rationale for. When we actively organize this continuously evolving knowledge, that's a strong strategy to prevent severe cognitive overload.

### Pattern 3: Designing Environments, Not Just Code

Our top engineers are not live-coding. They're not just prompting for code. They're designing environments — setting guardrails, creating systems so that agents and humans can work together toward a goal and a broader purpose.

Think of this like creating a system of reasoning so you can operate at scale beyond what one person can do. This includes setting up teams of agents, giving them the right context, the right skills to act. Our top engineers don't just want fast code — they want verified high-quality code. When we delegate execution, how do we keep the bar high? How do agents know when to act or even where to debate each other to find better solutions?

### Pattern 4: Micro Teams and Decoupled Roles

AI isn't just changing how people build, but *who* can build. It's decoupling a person's job role from the types of tasks they perform.

We're seeing the rise of the micro team — small, cross-functional, agile pods with less communication overhead and much tighter collaboration loops. These teams execute at large scale and good velocity thanks to the agents they deploy. But this is only possible if we shift left on intent, because that helps us master delegation to agents. We must clearly articulate the context, constraints, goals, trade-offs, and success criteria.

### Pattern 5: A Scientific Mindset

If we're going to work at the cutting edge, we need to be open to failure. Things move fast — it's rarely about getting it right the first time. It's about learning what we can as we move and then iterating.

Every week, our engineers experiment with new approaches and invest in codifying that learning back into the system. It isn't a scientific mindset if we randomly explore and never capture those learnings.

## The T-Shaped Engineer

Pulling this together: shift left, shift up, and design systems. System design includes the environment, the actors — humans, agents, and tools — and the culture that ties it all together. This lets us focus on the most important problems, learn and adapt quickly, and execute effectively while feeding insights back in.

Our top performers are increasingly T-shaped. The idea of a T-shaped developer isn't new, but we're seeing a few things emerge.

The **horizontal bar** of the T represents a broad foundation of knowledge in the wider software engineering ecosystem. You don't need expertise in every area, but you need good understanding of how key parts of the system work.

The **vertical stem** represents deep specialized knowledge and hands-on expertise — within a specific field like fintech, or a particular technology stack.

What's evolving:

- **A new horizontal layer**: Effectively working with AI. It's non-negotiable that AI-native engineers understand the constraints of AI in a task-specific context, assess quality of outputs, and steer AI effectively.
- **Adjacent engineering skills**: Because AI creates more functional code, key considerations around security, reliability, deployment, and compliance become even more important.
- **Adjacent non-engineering skills**: Business and user context. Because AI can handle the *how* of coding, we must understand the *why*.

This is already what's expected of senior developers. But now that engineers work at higher altitudes, the difference is a fundamental assumption about using AI effectively — and that AI makes depth and breadth needs more acute. We need adjacent knowledge; we need depth. Otherwise, AI just makes us do wrong things faster.

## Core Software Engineering Skills

To understand how these are evolving, let me share a story from our search organization. Right now, product managers are shipping features all the way through to live experiments. They aren't writing traditional code — they're using internal platforms that translate their intent into working features on our production tech stack.

From the outside, you might think: if PMs are coding their way to production, what role do core software engineering skills play? The reality is, none of this is possible without an incredibly advanced platform. Deep expertise in system architectures, language frameworks — they're all baked into the platform, as are scalability and reliability requirements.

The engineer isn't handcrafting individual features. They're precision engineering the ecosystem that allows those features to exist safely. That requires more engineering depth, not less.

### Three Shifts in Core Skills

**1. Verification becomes the bottleneck.** Code generation happens faster and faster. AI is a massive force multiplier, but you must possess the deep expertise to evaluate, integrate, and maintain its output. At the scale AI operates, this isn't about manually verifying line by line — it's about setting effective feedback loops, catching issues reliably in low-stakes environments, and targeting human attention on the highest-value work.

**2. Engineers don't write code — they control.** If you lack deep engineering understanding, AI can generate technical and cognitive debt at an incredibly fast rate. Our teams are building internal platforms that go from intent to functioning, high-quality, reliable, secure code. Engineers think about boundaries and guardrails — specifying nuanced style guide conventions that agents must adhere to, with checks and balances to detect drift.

We know these models sound incredibly confident. We know it's easy to accept changes wholesale at scale. Delegate tasks, not judgment. Your core engineering skills push the model in the right direction.

**3. Feedback loops prevent intellectual passivity.** Getting end-user feedback, performance feedback, measuring adherence to intent — observability is critical so we can establish where guardrails are missing or agents are making incorrect assumptions.

### Practical Tips for Core Skills

- **Re-implementation as a learning tool.** Don't just accept AI's first draft. Instruct it to tear down and re-implement. Ask it to document its logic — why it approached things differently, what it learned. This checks initial assumptions and surfaces where context is missing.

- **Walkthroughs of alien code.** Have engineers explain code or systems they didn't write — to build the shared mental model. Analog approaches work incredibly well here. We've seen teams adopt more whiteboarding to articulate system logic. Code is increasingly not the first-class outcome; adherence to intent and shared understanding of the system should be deliberate deliverables.

- **Skill files and rule files.** Explicitly codify team practices, expectations, and institutional knowledge for your agents in a consistent, scalable way. Our best teams create structured agent role profiles with specific behavioral attributes. Being forced to reflect on what good looks like keeps your core engineering skills sharp.

## GenAI Fluency: From Conductor to Orchestrator

We're moving beyond AI enhancement to AI-native engineering — a big mental model shift from conducting a single agent to orchestrating an entire system.

### Three Principles

**1. Manage teams of asynchronous agents.** Each has its own context window, its own area of responsibility. The human software engineer sets the environment and directs the flow.

**2. Teach agents how to act.** Give them skills — the exact recipes, tools, and domain knowledge to execute. Know when to delegate and when not to. Our top teams avoid the automation trap by establishing clear human baselines and measuring verification overheads.

**3. Evaluation cost is the new bottleneck.** Where we don't see enough success, we analyze agent traces and build shared understanding of where the system can improve — tool usability, agent skills, missing context.

### Examples at Google

- **Adversarial review agents** push at decisions and edge cases. Traces are documented; intent and agent rules are updated from learnings.
- **Code review agents** evaluate functionality, reliability, performance, usability, security, and maintainability — not to replace human reviewers, but to create tighter feedback loops and catch issues earlier.
- **Shepherding agents** guide changes through CI/CD pipelines, triggering review agents multiple times, leveraging risk assessor agents that flag high-risk changes for human review.

### Upskilling Tips

- **Upskill on evals.** Because verification is such a bottleneck, you need confidence in evaluating AI output. The whole T-shape is essential here — AI, software engineering, user, and business skills together produce realistic, grounded, relevant evals.

- **Agent journaling.** Force your agents to constantly reflect and document. It's fascinating to see how your agent perceived its day — where it got stuck, confused, or productive. These reflections reveal how to improve the ecosystem. If an agent consistently struggles with a tool, you might have a tool usability problem.

- **Build teams of agents.** Now is the time to scale beyond a single agent. For example, in our TensorFlow migration — highly complex, delicate work — one team deployed a strict three-agent architecture: a planner agent that generates verifiable migration steps, an orchestrator agent that groups those steps, and a coder agent that executes them. Different playbooks are fed in for YouTube-specific versus other product area practices.

- **Precision engineering, not vague prompts.** Spec-driven development means product thinking and architectural decision-making are documented upfront. Goals, constraints, rationale — these are critical context not just for agents, but for the broader team.

## Adjacent Engineering Skills

If your organization has high-quality internal platforms, strong APIs, and clear, well-documented workflows, AI acts as a powerful collaborator. But if you suffer from fragmented tooling, siloed data, and fragile infrastructure, AI won't save you — it'll simply help you generate technical debt faster.

Our DORA research speaks directly to this point: **AI is an amplifier and it is a mirror.** It magnifies existing strengths while holding up a mirror to weaknesses.

### Three Principles

**1. Embed best practices into platforms.** The search PM story is relevant here too. Embedding best practices directly into a high-quality internal platform allowed us to ship features without handcrafting each line. While we've seen increases in AI-written code, we have not seen any measurable increase in outages or decrease in system reliability. We want 10x the velocity without 10x the risk.

**2. Tiered risk environments.** Different applications have different environmental needs. An internal Google app doesn't need to scale to a billion users. Get from prototype to production incrementally, moving through different risk profiles — containing the blast radius while achieving faster feedback loops.

**3. Effective experimentation.** When features move through your system faster, how do you get them to users in a way that isolates them and allows measurable understanding of performance?

### Building These Muscles

- **Blame-free postmortems.** Document, read, and discuss outages and incidents. This builds intuition for edge cases, scale limitations, and reliability threats. Triangulate postmortem documents with agent self-reflections and observability traces.

- **Use AI to stress test, not just build.** Set up red team agents to see your system through the eyes of malicious actors. Have agents explain how they would exploit the system — this trains you and your agents to spot vulnerabilities.

- **Analog system mapping.** Whiteboards are at a premium. Manually trace a pipeline to build mental models of things like enterprise compliance before code is written.

- **Invest in observability.** If features move through your system at 10x speed, you need to monitor them. We found earlier-career engineers getting blocked by opaque performance metrics. Investing in observability tools and unified data agents — with access to code, error logs, performance data, stack traces — empowered those engineers to better interpret complicated systems. Use AI not just to build, but to understand.

## Adjacent Non-Engineering Skills

Now that agents handle routine execution, engineers have the mandate to focus more on the *what* and the *why*. For many of us, this is uncomfortable. Our DORA research highlighted that many developers face a real identity threat — we've historically derived so much value from the sheer craft of coding.

We need to deliberately shift how we think about and measure our worth. That broader value comes from solving real human and real business problems.

Our engineers are increasingly acting as **value translators** — taking user needs and business needs and turning them into precise requirements. Consider a feature request to "improve performance." An AI might find and refactor an inefficient loop. But a value translator first asks: improve performance for *whom*? Under what conditions? They look at metrics and user feedback, find the specific user segment, and guide AI to optimize the critical code paths for that scenario.

Human taste and judgment are essential to point AI resources in the right direction.

> "The most effective people are those who can hold their vision while remaining committed to seeing current reality clearly." — Peter Senge

This perfectly captures the T-shaped engineer: broad vision from adjacent skills, intimate understanding of technical reality from engineering depth, and systems and practices to capture intent and maintain understanding.

### Tips for Non-Engineering Skills

- **Don't let AI synthesize all your user feedback.** It's tempting to dump user feedback logs into an LLM and ask for a summary. But we're seeing an increase in traditional high-touch user feedback sessions. Hearing the actual joy or frustration in a user's voice builds profound empathy and makes the *why* more real.

- **Spec-driven development.** Treat your spec as the ultimate product deliverable. Our best teams are fiercely protective of their specifications. A lot of cognitive energy goes into debating goals, business logic, and edge case constraints. Forcing this clear articulation early ensures teams align on the why and helps agents access nuanced institutional knowledge.

## Pulling It All Together

When we combine deep expertise to catch AI's mistakes, orchestration skills to manage the fleet, adjacent engineering to understand the system, and non-engineering skills for broader context — that's what it takes to thrive in an AI-native era.

We're talking about possessing the skills to capture and translate knowledge in a way that preserves signal-to-noise for both humans and agents, creating a virtuous improvement system.

## A Note for Engineering Leaders

Engineers don't work outside an org. The hard truth: you can't mandate a T-shaped developer inside a broken system. As our DORA research shows, AI can be a harsh mirror reflecting all weaknesses as well as strengths. Well-aligned teams with strong practices see AI accelerate value delivery. Fragmented tooling, siloed data, or a culture of blame? AI simply exposes the bottlenecks.

> "A bad system will beat a good person every time." — W. Edwards Deming

We're asking engineers to focus on the hardest architectural decisions, verify machine output, and context-switch between multiple agents. This can be cognitively exhausting. 10x output can't come with 10x cognitive load, or we'll burn people out.

### Three Shifts for Leaders

**1. Redefine how you measure productivity.** Stop measuring pull request throughput or lines of code. Reward outcomes and business needs met. If we only measure speed and never quality, developers won't rigorously verify AI's output, and system instability skyrockets.

**2. Protect productive struggle.** Carve out dedicated time during work hours for devs to learn tools and understand systems. Encourage manual architectural walkthroughs and experimentation. If you don't give space to build mental models, your team drowns in cognitive debt.

**3. Foster radical psychological safety.** We're in an era of experimentation. Teams are going to build agentic workflows that fail. If your culture punishes failures, developers will fall back on old, safe ways of working. Celebrate intelligent failure. Create blame-free postmortems so the whole team learns.

## The Joy of Building Remains

Managing an agent workforce while architecting complex systems could sound exhausting — it forces us to stay in a high-altitude decision space. The silver lining: while the nature of effort is changing, we still have the joy of building.

By investing in the expanded T-shaped skill set, you get to see your ideas come to life at unprecedented speeds, closer to the actual software you want to create. You aren't leaving behind the craft of software engineering — you're stepping up to its highest and most impactful level.

The software engineering role is not vanishing. It's evolving. If anything, it's becoming more important.

Shift left. Shift up. Design systems, not just bits of code.

Thank you.

[music]
