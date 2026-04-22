---
title: "Harness Engineering: Leveraging Codex in an Agent-First World"
date: 2026-04-22
description: "OpenAI 内部团队用 5 个月、0 行手写代码、3–7 名工程师交付百万行代码的内部产品——重点不在 Codex 多强，而在他们怎么改造仓库、文档、架构让 agent 真正跑得动。"
source: https://openai.com/index/harness-engineering/
speaker: "Ryan Lopopolo, Member of Technical Staff at OpenAI"
format: Engineering blog post
language: English
purpose: Read-aloud article
tags:
  - openai
  - codex
  - agent
  - engineering
  - ai-coding
chunks:
  - text: "running an experiment"
    type: collocation
    meaning: "在做一场实验"
    note: "开场常用，比 'we tried' 更有意图感"
  - text: "Humans steer. Agents execute."
    type: formulaic
    meaning: "人类掌舵，Agent 执行"
    note: "全文核心标语，非常适合套用"
  - text: "orders of magnitude"
    type: collocation
    meaning: "数量级（级别的提升）"
    note: "工程/产品场景高频"
  - text: "our one truly scarce resource"
    type: chunk
    meaning: "我们唯一真正稀缺的资源"
    note: "Naval 式金句句式"
  - text: "anchor the system"
    type: collocation
    meaning: "锚定/奠基这套系统"
  - text: "shaped by the agent"
    type: chunk
    meaning: "由 agent 塑造而成"
  - text: "output for output's sake"
    type: formulaic
    meaning: "为产出而产出——空有产出"
    note: "反向警句结构：X for X's sake"
  - text: "hands-on human coding"
    type: chunk
    meaning: "人手亲自写代码"
  - text: "working depth-first"
    type: chunk
    meaning: "按深度优先推进"
  - text: "try harder"
    type: formulaic
    meaning: "'再努力一点'——这里被当作反面答案"
  - text: "what capability is missing"
    type: sentence-frame
    meaning: "缺的是什么能力（用来诊断系统瓶颈）"
  - text: "legible and enforceable"
    type: collocation
    meaning: "清晰可读且可强制执行"
    note: "全文关键词之一"
  - text: "drive a PR to completion"
    type: collocation
    meaning: "把 PR 推到合并"
  - text: "iterate in a loop"
    type: collocation
    meaning: "循环往复地迭代"
  - text: "agent-to-agent"
    type: chunk
    meaning: "代理对代理的（协作模式）"
  - text: "bottleneck became human QA capacity"
    type: chunk
    meaning: "瓶颈变成了人类 QA 的产能"
    note: "'bottleneck became X' 这个句型值得记"
  - text: "fixed constraint"
    type: collocation
    meaning: "固定不变的约束"
  - text: "directly legible to"
    type: chunk
    meaning: "对 ... 可直接读懂/辨认"
  - text: "wired the Chrome DevTools Protocol into"
    type: collocation
    meaning: "把 ... 接入到 ...（wire X into Y）"
    note: "'wire X into Y' 非常地道的工程表达"
  - text: "reason about"
    type: collocation
    meaning: "推理/思考关于..."
    note: "AI/工程语境高频，比 'think about' 更正式"
  - text: "torn down"
    type: chunk
    meaning: "拆掉/销毁（资源）"
    note: "DevOps 术语：spin up / tear down"
  - text: "become tractable"
    type: collocation
    meaning: "变得可解/可处理"
  - text: "system of record"
    type: chunk
    meaning: "真相来源系统——以此为准的数据源"
    note: "企业/架构语境高频"
  - text: "give Codex a map, not a 1,000-page instruction manual"
    type: formulaic
    meaning: "给它一张地图，而不是一本千页说明书"
    note: "非常好的类比金句"
  - text: "context is a scarce resource"
    type: formulaic
    meaning: "上下文是稀缺资源"
  - text: "crowds out"
    type: chunk
    meaning: "挤出/排挤掉"
  - text: "pattern-matching"
    type: chunk
    meaning: "模式匹配（而不是真正理解）"
  - text: "attractive nuisance"
    type: chunk
    meaning: "看起来有用但会招来麻烦的东西"
    note: "法律 + 工程里都用"
  - text: "treat it as the table of contents"
    type: chunk
    meaning: "把它当作目录来用"
  - text: "progressive disclosure"
    type: collocation
    meaning: "渐进披露（UX/文档术语）"
  - text: "first-class artifacts"
    type: chunk
    meaning: "一等公民产物"
    note: "'first-class X' 是工程圈惯用法"
  - text: "doc-gardening"
    type: chunk
    meaning: "文档园丁（定期清理）"
    note: "OpenAI 自造词，可借用"
  - text: "the agent's point of view"
    type: chunk
    meaning: "从 agent 的视角"
  - text: "doesn't exist"
    type: sentence-frame
    meaning: "... 根本就不存在（用来强调不可见=不存在）"
  - text: "push more and more context into the repo"
    type: chunk
    meaning: "把越来越多的上下文塞进仓库"
  - text: "encoded directly into tooling"
    type: collocation
    meaning: "直接编码进工具链里"
  - text: "onboard a new teammate"
    type: collocation
    meaning: "给新同事做入职"
  - text: "better-aligned output"
    type: collocation
    meaning: "对齐程度更高的产出"
  - text: "composability"
    type: chunk
    meaning: "可组合性"
  - text: "parse data shapes at the boundary"
    type: chunk
    meaning: "在边界处解析数据形状"
    note: "'parse don't validate' 的引申"
  - text: "strict boundaries and predictable structure"
    type: collocation
    meaning: "严格的边界 + 可预测的结构"
  - text: "enforced mechanically"
    type: collocation
    meaning: "机械化地强制执行"
    note: "与 'best effort' 对立"
  - text: "speed without decay"
    type: chunk
    meaning: "只快不烂"
    note: "工程质量金句"
  - text: "architectural drift"
    type: collocation
    meaning: "架构漂移"
  - text: "taste invariants"
    type: chunk
    meaning: "品味不变量"
    note: "OpenAI 自创术语"
  - text: "human-first workflow"
    type: chunk
    meaning: "以人为先的工作流"
  - text: "multipliers"
    type: chunk
    meaning: "倍增器"
  - text: "enforce boundaries centrally, allow autonomy locally"
    type: formulaic
    meaning: "集中执行边界，局部放权自治"
    note: "完美的管理学金句，可直接套用"
  - text: "fed back into the system"
    type: chunk
    meaning: "反馈进系统"
  - text: "blocking merge gates"
    type: collocation
    meaning: "阻塞式合并门槛"
  - text: "short-lived"
    type: chunk
    meaning: "生命周期很短的"
  - text: "corrections are cheap, and waiting is expensive"
    type: formulaic
    meaning: "改错便宜，等待昂贵"
    note: "非常精炼的权衡金句"
  - text: "in the loop"
    type: formulaic
    meaning: "留在回路里 / 保持知情"
  - text: "work at a different layer of abstraction"
    type: chunk
    meaning: "在不同的抽象层级上工作"
  - text: "treat it as a signal"
    type: chunk
    meaning: "把它当作一个信号"
  - text: "crossed a meaningful threshold"
    type: collocation
    meaning: "跨过了一个有意义的门槛"
  - text: "end-to-end drive"
    type: chunk
    meaning: "端到端地推进"
  - text: "should not be assumed to generalize"
    type: formulaic
    meaning: "不应被假设可以推广"
    note: "研究/工程论文口吻"
  - text: "AI slop"
    type: chunk
    meaning: "AI 糊涂饭——低质量 AI 产出"
  - text: "golden principles"
    type: chunk
    meaning: "金科玉律"
  - text: "high-interest loan"
    type: chunk
    meaning: "高息贷款（比喻技术债）"
  - text: "compound"
    type: chunk
    meaning: "复利积累"
  - text: "anchor our investments in reality"
    type: chunk
    meaning: "让我们的投入锚定在现实里"
  - text: "shows up more in the scaffolding rather than the code"
    type: chunk
    meaning: "更多体现在脚手架而非代码里"
  - text: "at scale"
    type: formulaic
    meaning: "规模化地"
  - text: "you can just build things"
    type: formulaic
    meaning: "你可以直接动手做事"
    note: "Patrick Collison 那句口号的回声"
---

Over the past five months, our team has been running an experiment: building and shipping an internal beta of a software product with 0 lines of manually-written code.

The product has internal daily users and external alpha testers. It ships, deploys, breaks, and gets fixed. What's different is that every line of code — application logic, tests, CI configuration, documentation, observability, and internal tooling — has been written by Codex. We estimate that we built this in about 1/10th the time it would have taken to write the code by hand.

**Humans steer. Agents execute.**

We intentionally chose this constraint so we would build what was necessary to increase engineering velocity by orders of magnitude. We had weeks to ship what ended up being a million lines of code. To do that, we needed to understand what changes when a software engineering team's primary job is no longer to write code, but to design environments, specify intent, and build feedback loops that allow Codex agents to do reliable work.

This post is about what we learned by building a brand new product with a team of agents — what broke, what compounded, and how to maximize our one truly scarce resource: human time and attention.

## We started with an empty git repository

The first commit to an empty repository landed in late August 2025.

The initial scaffold — repository structure, CI configuration, formatting rules, package manager setup, and application framework — was generated by Codex CLI using GPT-5, guided by a small set of existing templates. Even the initial `AGENTS.md` file that directs agents how to work in the repository was itself written by Codex.

There was no pre-existing human-written code to anchor the system. From the beginning, the repository was shaped by the agent.

Five months later, the repository contains on the order of a million lines of code across application logic, infrastructure, tooling, documentation, and internal developer utilities. Over that period, roughly 1,500 pull requests have been opened and merged with a small team of just three engineers driving Codex. This translates to an average throughput of 3.5 PRs per engineer per day, and surprisingly the throughput has increased as the team has grown to now seven engineers. Importantly, this wasn't output for output's sake: the product has been used by hundreds of users internally, including daily internal power users.

Throughout the development process, humans never directly contributed any code. This became a core philosophy for the team: **no manually-written code.**

## Redefining the role of the engineer

The lack of hands-on human coding introduced a different kind of engineering work, focused on systems, scaffolding, and leverage.

Early progress was slower than we expected, not because Codex was incapable, but because the environment was underspecified. The agent lacked the tools, abstractions, and internal structure required to make progress toward high-level goals. The primary job of our engineering team became enabling the agents to do useful work.

In practice, this meant working depth-first: breaking down larger goals into smaller building blocks (design, code, review, test, etc.), prompting the agent to construct those blocks, and using them to unlock more complex tasks. When something failed, the fix was almost never "try harder." Because the only way to make progress was to get Codex to do the work, human engineers always stepped into the task and asked: *what capability is missing, and how do we make it both legible and enforceable for the agent?*

Humans interact with the system almost entirely through prompts: an engineer describes a task, runs the agent, and allows it to open a pull request. To drive a PR to completion, we instruct Codex to review its own changes locally, request additional specific agent reviews both locally and in the cloud, respond to any human or agent given feedback, and iterate in a loop until all agent reviewers are satisfied (effectively this is a Ralph Wiggum Loop). Codex uses our standard development tools directly (`gh`, local scripts, and repository-embedded skills) to gather context without humans copying and pasting into the CLI.

Humans may review pull requests, but aren't required to. Over time, we've pushed almost all review effort towards being handled agent-to-agent.

## Increasing application legibility

As code throughput increased, our bottleneck became human QA capacity. Because the fixed constraint has been human time and attention, we've worked to add more capabilities to the agent by making things like the application UI, logs, and app metrics themselves directly legible to Codex.

For example, we made the app bootable per git worktree, so Codex could launch and drive one instance per change. We also wired the Chrome DevTools Protocol into the agent runtime and created skills for working with DOM snapshots, screenshots, and navigation. This enabled Codex to reproduce bugs, validate fixes, and reason about UI behavior directly.

![Codex drives the app with Chrome DevTools MCP to validate its work.](https://images.ctfassets.net/kftzwdyauwt9/1Gu58eNlqDEuITmbqJDmq9/1e2e62f7e15fb16d2da0da5407240564/fig_1__codex_drives_the_app_.png?w=1920&q=80&fm=webp)

We did the same for observability tooling. Logs, metrics, and traces are exposed to Codex via a local observability stack that's ephemeral for any given worktree. Codex works on a fully isolated version of that app — including its logs and metrics, which get torn down once that task is complete. Agents can query logs with LogQL and metrics with PromQL. With this context available, prompts like *"ensure service startup completes in under 800ms"* or *"no span in these four critical user journeys exceeds two seconds"* become tractable.

![Giving Codex a full observability stack in local dev.](https://images.ctfassets.net/kftzwdyauwt9/4Xr18TZ5G4Bh8zIgsTFIVK/f7ae689ddd8c31664e39d809b0973425/OAI_Harness_engineering_Giving_Codex_a_full_observability_stack_desktop-light__1_.svg?w=1920&q=80)

We regularly see single Codex runs work on a single task for upwards of six hours (often while the humans are sleeping).

## We made repository knowledge the system of record

Context management is one of the biggest challenges in making agents effective at large and complex tasks. One of the earliest lessons we learned was simple: **give Codex a map, not a 1,000-page instruction manual.**

We tried the "one big `AGENTS.md`" approach. It failed in predictable ways:

- **Context is a scarce resource.** A giant instruction file crowds out the task, the code, and the relevant docs — so the agent either misses key constraints or starts optimizing for the wrong ones.
- **Too much guidance becomes non-guidance.** When everything is "important," nothing is. Agents end up pattern-matching locally instead of navigating intentionally.
- **It rots instantly.** A monolithic manual turns into a graveyard of stale rules. Agents can't tell what's still true, humans stop maintaining it, and the file quietly becomes an attractive nuisance.
- **It's hard to verify.** A single blob doesn't lend itself to mechanical checks (coverage, freshness, ownership, cross-links), so drift is inevitable.

So instead of treating `AGENTS.md` as the encyclopedia, we treat it as the table of contents.

The repository's knowledge base lives in a structured `docs/` directory treated as the system of record. A short `AGENTS.md` (roughly 100 lines) is injected into context and serves primarily as a map, with pointers to deeper sources of truth elsewhere.

```
AGENTS.md
ARCHITECTURE.md
docs/
├── design-docs/
│   ├── index.md
│   ├── core-beliefs.md
│   └── ...
├── exec-plans/
│   ├── active/
│   ├── completed/
│   └── tech-debt-tracker.md
├── generated/
│   └── db-schema.md
├── product-specs/
│   ├── index.md
│   ├── new-user-onboarding.md
│   └── ...
├── references/
│   ├── design-system-reference-llms.txt
│   ├── nixpacks-llms.txt
│   ├── uv-llms.txt
│   └── ...
├── DESIGN.md
├── FRONTEND.md
├── PLANS.md
├── PRODUCT_SENSE.md
├── QUALITY_SCORE.md
├── RELIABILITY.md
└── SECURITY.md
```

Design documentation is catalogued and indexed, including verification status and a set of core beliefs that define agent-first operating principles. Architecture documentation provides a top-level map of domains and package layering. A quality document grades each product domain and architectural layer, tracking gaps over time.

Plans are treated as first-class artifacts. Ephemeral lightweight plans are used for small changes, while complex work is captured in execution plans with progress and decision logs that are checked into the repository. Active plans, completed plans, and known technical debt are all versioned and co-located, allowing agents to operate without relying on external context.

This enables progressive disclosure: agents start with a small, stable entry point and are taught where to look next, rather than being overwhelmed up front.

We enforce this mechanically. Dedicated linters and CI jobs validate that the knowledge base is up to date, cross-linked, and structured correctly. A recurring "doc-gardening" agent scans for stale or obsolete documentation that does not reflect the real code behavior and opens fix-up pull requests.

## Agent legibility is the goal

As the codebase evolved, Codex's framework for design decisions needed to evolve, too.

Because the repository is entirely agent-generated, it's optimized first for Codex's legibility. In the same way teams aim to improve navigability of their code for new engineering hires, our human engineers' goal was making it possible for an agent to reason about the full business domain directly from the repository itself.

From the agent's point of view, anything it can't access in-context while running effectively doesn't exist. Knowledge that lives in Google Docs, chat threads, or people's heads are not accessible to the system. Repository-local, versioned artifacts (e.g., code, markdown, schemas, executable plans) are all it can see.

![The limits of agent knowledge: What Codex can't see doesn't exist.](https://images.ctfassets.net/kftzwdyauwt9/7uWHsJIC6o3uQPsnQ2Avz9/8be3e321892054bd215afb2b250a176a/OAI_Harness_engineering_The_limits_of_agent_knowledge_desktop-light.png?w=1920&q=80&fm=webp)

We learned that we needed to push more and more context into the repo over time. That Slack discussion that aligned the team on an architectural pattern? If it isn't discoverable to the agent, it's illegible in the same way it would be unknown to a new hire joining three months later.

Giving Codex more context means organizing and exposing the right information so the agent can reason over it, rather than overwhelming it with ad-hoc instructions. In the same way you would onboard a new teammate on product principles, engineering norms, and team culture (emoji preferences included), giving the agent this information leads to better-aligned output.

This framing clarified many tradeoffs. We favored dependencies and abstractions that could be fully internalized and reasoned about in-repo. Technologies often described as "boring" tend to be easier for agents to model due to composability, API stability, and representation in the training set. In some cases, it was cheaper to have the agent reimplement subsets of functionality than to work around opaque upstream behavior from public libraries. For example, rather than pulling in a generic `p-limit`-style package, we implemented our own map-with-concurrency helper: it's tightly integrated with our OpenTelemetry instrumentation, has 100% test coverage, and behaves exactly the way our runtime expects.

Pulling more of the system into a form the agent can inspect, validate, and modify directly increases leverage — not just for Codex, but for other agents (e.g. Aardvark) that are working on the codebase as well.

## Enforcing architecture and taste

Documentation alone doesn't keep a fully agent-generated codebase coherent. By enforcing invariants, not micromanaging implementations, we let agents ship fast without undermining the foundation. For example, we require Codex to parse data shapes at the boundary, but are not prescriptive on how that happens (the model seems to like Zod, but we didn't specify that specific library).

Agents are most effective in environments with strict boundaries and predictable structure, so we built the application around a rigid architectural model. Each business domain is divided into a fixed set of layers, with strictly validated dependency directions and a limited set of permissible edges. These constraints are enforced mechanically via custom linters (Codex-generated, of course!) and structural tests.

Within each business domain (e.g. App Settings), code can only depend "forward" through a fixed set of layers (Types → Config → Repo → Service → Runtime → UI). Cross-cutting concerns (auth, connectors, telemetry, feature flags) enter through a single explicit interface: Providers. Anything else is disallowed and enforced mechanically.

![Layered domain architecture with explicit cross-cutting boundaries.](https://images.ctfassets.net/kftzwdyauwt9/4Rlip1H3T9apPlSmWs7Wr8/7708c176bfbe11951e06ad8e2b83bf01/OAI_Harness_engineering_Layered_domain_architecture_with_explicit_cross-cutting_boundries_desktop-light.png?w=1920&q=80&fm=webp)

This is the kind of architecture you usually postpone until you have hundreds of engineers. With coding agents, it's an early prerequisite: the constraints are what allows speed without decay or architectural drift.

In practice, we enforce these rules with custom linters and structural tests, plus a small set of "taste invariants." For example, we statically enforce structured logging, naming conventions for schemas and types, file size limits, and platform-specific reliability requirements with custom lints. Because the lints are custom, we write the error messages to inject remediation instructions into agent context.

In a human-first workflow, these rules might feel pedantic or constraining. With agents, they become multipliers: once encoded, they apply everywhere at once.

At the same time, we're explicit about where constraints matter and where they do not. This resembles leading a large engineering platform organization: **enforce boundaries centrally, allow autonomy locally.** You care deeply about boundaries, correctness, and reproducibility. Within those boundaries, you allow teams — or agents — significant freedom in how solutions are expressed.

The resulting code does not always match human stylistic preferences, and that's okay. As long as the output is correct, maintainable, and legible to future agent runs, it meets the bar.

Human taste is fed back into the system continuously. Review comments, refactoring pull requests, and user-facing bugs are captured as documentation updates or encoded directly into tooling. When documentation falls short, we promote the rule into code.

## Throughput changes the merge philosophy

As Codex's throughput increased, many conventional engineering norms became counterproductive.

The repository operates with minimal blocking merge gates. Pull requests are short-lived. Test flakes are often addressed with follow-up runs rather than blocking progress indefinitely. In a system where agent throughput far exceeds human attention, **corrections are cheap, and waiting is expensive.**

This would be irresponsible in a low-throughput environment. Here, it's often the right tradeoff.

## What "agent-generated" actually means

When we say the codebase is generated by Codex agents, we mean everything in the codebase.

Agents produce:

- Product code and tests
- CI configuration and release tooling
- Internal developer tools
- Documentation and design history
- Evaluation harnesses
- Review comments and responses
- Scripts that manage the repository itself
- Production dashboard definition files

Humans always remain in the loop, but work at a different layer of abstraction than we used to. We prioritize work, translate user feedback into acceptance criteria, and validate outcomes. When the agent struggles, we treat it as a signal: identify what is missing — tools, guardrails, documentation — and feed it back into the repository, always by having Codex itself write the fix.

Agents use our standard development tools directly. They pull review feedback, respond inline, push updates, and often squash and merge their own pull requests.

## Increasing levels of autonomy

As more of the development loop was encoded directly into the system — testing, validation, review, feedback handling, and recovery — the repository recently crossed a meaningful threshold where Codex can end-to-end drive a new feature.

Given a single prompt, the agent can now:

- Validate the current state of the codebase
- Reproduce a reported bug
- Record a video demonstrating the failure
- Implement a fix
- Validate the fix by driving the application
- Record a second video demonstrating the resolution
- Open a pull request
- Respond to agent and human feedback
- Detect and remediate build failures
- Escalate to a human only when judgment is required
- Merge the change

This behavior depends heavily on the specific structure and tooling of this repository and should not be assumed to generalize without similar investment — at least, not yet.

## Entropy and garbage collection

Full agent autonomy also introduces novel problems. Codex replicates patterns that already exist in the repository — even uneven or suboptimal ones. Over time, this inevitably leads to drift.

Initially, humans addressed this manually. Our team used to spend every Friday (20% of the week) cleaning up "AI slop." Unsurprisingly, that didn't scale.

Instead, we started encoding what we call "golden principles" directly into the repository and built a recurring cleanup process. These principles are opinionated, mechanical rules that keep the codebase legible and consistent for future agent runs. For example: (1) we prefer shared utility packages over hand-rolled helpers to keep invariants centralized, and (2) we don't probe data "YOLO-style" — we validate boundaries or rely on typed SDKs so the agent can't accidentally build on guessed shapes. On a regular cadence, we have a set of background Codex tasks that scan for deviations, update quality grades, and open targeted refactoring pull requests. Most of these can be reviewed in under a minute and automerged.

This functions like garbage collection. Technical debt is like a high-interest loan: it's almost always better to pay it down continuously in small increments than to let it compound and tackle it in painful bursts. Human taste is captured once, then enforced continuously on every line of code. This also lets us catch and resolve bad patterns on a daily basis, rather than letting them spread in the code base for days or weeks.

## What we're still learning

This strategy has so far worked well up through internal launch and adoption at OpenAI. Building a real product for real users helped anchor our investments in reality and guide us towards long-term maintainability.

What we don't yet know is how architectural coherence evolves over years in a fully agent-generated system. We're still learning where human judgment adds the most leverage and how to encode that judgment so it compounds. We also don't know how this system will evolve as models continue to become more capable over time.

What's become clear: building software still demands discipline, but the discipline shows up more in the scaffolding rather than the code. The tooling, abstractions, and feedback loops that keep the codebase coherent are increasingly important.

Our most difficult challenges now center on designing environments, feedback loops, and control systems that help agents accomplish our goal: build and maintain complex, reliable software at scale.

As agents like Codex take on larger portions of the software lifecycle, these questions will matter even more. We hope that sharing some early lessons helps you reason about where to invest your effort so you can just build things.

---

*By Ryan Lopopolo. Special thanks to Victor Zhu and Zach Brock, and to the entire team that built this new product.*
