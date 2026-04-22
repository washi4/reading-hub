---
title: "From Model to Agent: Equipping the Responses API with a Computer Environment"
date: 2026-04-22
description: "OpenAI 怎么把 Responses API 改造成一套完整的 agent 运行环境——shell 工具、容器、网络代理、skills、compaction 的系统级拆解。"
source: https://openai.com/index/equip-responses-api-computer-environment/
speaker: "Bo Xu, Danny Zhang, and Rohit Arunachalam"
format: Engineering blog post
language: English
purpose: Read-aloud article
tags:
  - openai
  - responses-api
  - agent
  - engineering
  - infrastructure
chunks:
  - text: "a shift from"
    type: sentence-frame
    meaning: "一个从 ... 的转变（可接 to 接新状态）"
    note: "开场陈述行业走向常用"
  - text: "excel at"
    type: collocation
    meaning: "在某方面擅长/出色"
  - text: "practical problems emerge"
    type: chunk
    meaning: "现实的问题就冒出来了"
    note: "'X emerge' 是很工程的表达"
  - text: "security headache"
    type: chunk
    meaning: "安全上的头疼事"
  - text: "Instead of putting it on developers"
    type: sentence-frame
    meaning: "与其把事情压给开发者去做"
    note: "'put it on X' = 把担子甩给 X"
  - text: "tight execution loop"
    type: collocation
    meaning: "紧凑的执行循环"
  - text: "feeds into"
    type: collocation
    meaning: "喂入/注入 ...（下一步）"
  - text: "step by step"
    type: formulaic
    meaning: "一步一步地"
  - text: "using a tool"
    type: chunk
    meaning: "使用一个工具（AI 语境下是模型在 '调用工具'）"
  - text: "the model actually only proposes a tool call"
    type: chunk
    meaning: "模型其实只是在 '提议' 一次工具调用"
    note: "全文的关键澄清：model proposes, platform executes"
  - text: "dramatically more powerful"
    type: collocation
    meaning: "戏剧性地更强大"
  - text: "out of the box"
    type: formulaic
    meaning: "开箱即用"
  - text: "a much wider range of use cases"
    type: collocation
    meaning: "更广泛的使用场景"
  - text: "how are these commands executed"
    type: sentence-frame
    meaning: "这些命令是怎么被执行的（用来设问）"
  - text: "in a loop"
    type: formulaic
    meaning: "循环地/在回路里"
  - text: "yields control back to"
    type: collocation
    meaning: "把控制权交还给 ..."
  - text: "its own harness"
    type: chunk
    meaning: "自己的马具（引申：自己的一套框架/壳子）"
    note: "AI agent 圈的核心术语"
  - text: "trained for this"
    type: chunk
    meaning: "专门为此训练过"
  - text: "inspect the results"
    type: collocation
    meaning: "检视结果"
  - text: "issue follow-up commands"
    type: collocation
    meaning: "发出后续命令"
  - text: "in near real time"
    type: formulaic
    meaning: "近乎实时地"
  - text: "move on to"
    type: collocation
    meaning: "转向 / 继续做下一件事"
  - text: "in one step"
    type: formulaic
    meaning: "一步之内/一次搞定"
  - text: "multiplexes those streams"
    type: chunk
    meaning: "把这些流做多路复用"
    note: "'multiplex X' 系统工程高频"
  - text: "parallelize work"
    type: collocation
    meaning: "把工作并行化"
  - text: "consume context budgets"
    type: chunk
    meaning: "消耗上下文预算"
    note: "AI 圈最新表达"
  - text: "without adding useful signals"
    type: chunk
    meaning: "却不带来有用的信号"
  - text: "bounded result"
    type: collocation
    meaning: "有界的结果"
  - text: "preserves both the beginning and end"
    type: chunk
    meaning: "同时保留开头和结尾"
  - text: "context-efficient"
    type: chunk
    meaning: "上下文高效的"
  - text: "getting overwhelmed by"
    type: collocation
    meaning: "被 ... 淹没/压垮"
  - text: "fill the context window"
    type: collocation
    meaning: "占满上下文窗口"
  - text: "anything extraneous"
    type: chunk
    meaning: "任何多余的东西"
  - text: "align with how the model behaves"
    type: chunk
    meaning: "与模型的行为方式对齐"
  - text: "prior conversation state"
    type: collocation
    meaning: "先前的对话状态"
  - text: "token-efficient"
    type: chunk
    meaning: "省 token 的"
  - text: "across window boundaries"
    type: chunk
    meaning: "跨越窗口边界"
  - text: "without degrading quality"
    type: collocation
    meaning: "不损失质量地"
  - text: "eliminating the need for"
    type: sentence-frame
    meaning: "省去了对 ... 的需要"
  - text: "right before compaction"
    type: chunk
    meaning: "就在 compaction 之前"
  - text: "spin up a second instance"
    type: collocation
    meaning: "起一个第二实例"
    note: "DevOps 标配动词搭配"
  - text: "inspect and refine itself"
    type: chunk
    meaning: "审视并打磨自己"
  - text: "learns alongside us"
    type: chunk
    meaning: "跟我们一起学"
    note: "结句金句"
  - text: "anti-pattern"
    type: chunk
    meaning: "反模式"
  - text: "overfilling the prompt"
    type: chunk
    meaning: "把 prompt 塞爆"
  - text: "expensive and hard for the model to navigate"
    type: chunk
    meaning: "既贵又难让模型在其中穿梭"
  - text: "stage resources"
    type: collocation
    meaning: "把资源先搁放（暂存、分层）"
    note: "'stage X in Y' 部署术语"
  - text: "Much like humans"
    type: formulaic
    meaning: "非常像人类一样"
  - text: "in many cases"
    type: formulaic
    meaning: "很多情况下"
  - text: "pull the rows it needs"
    type: chunk
    meaning: "只拉它需要的那几行"
  - text: "an essential part of"
    type: sentence-frame
    meaning: "... 中不可缺少的一部分"
  - text: "unrestricted internet access"
    type: collocation
    meaning: "不受限的互联网访问"
  - text: "data exfiltration"
    type: chunk
    meaning: "数据外泄"
  - text: "guard against"
    type: collocation
    meaning: "防范 / 提防"
  - text: "sidecar egress proxy"
    type: chunk
    meaning: "sidecar 出站代理"
    note: "容器/K8s 经典模式术语"
  - text: "allowlists"
    type: chunk
    meaning: "允许清单（白名单）"
  - text: "while keeping traffic observable"
    type: chunk
    meaning: "同时保持流量可观测"
  - text: "secret injection at egress"
    type: chunk
    meaning: "在出站时注入密钥"
  - text: "stay outside model-visible context"
    type: chunk
    meaning: "留在模型看不见的范围之外"
  - text: "reduces the risk of leakage"
    type: collocation
    meaning: "降低泄漏风险"
  - text: "rediscover the workflow each run"
    type: chunk
    meaning: "每次跑都要重新发现一遍工作流"
  - text: "composable building blocks"
    type: collocation
    meaning: "可组合的构件"
  - text: "folder bundle"
    type: chunk
    meaning: "打包成文件夹的捆绑"
  - text: "maps naturally to"
    type: collocation
    meaning: "自然地对应到 ..."
    note: "架构类文章高频"
  - text: "discover skill files"
    type: collocation
    meaning: "发现 skill 文件"
  - text: "in the same agent loop"
    type: chunk
    meaning: "在同一个 agent 回路里"
  - text: "This sequence is deterministic"
    type: formulaic
    meaning: "这套流程是确定性的"
  - text: "progressively explores"
    type: collocation
    meaning: "逐步探索"
  - text: "To put all the pieces together"
    type: formulaic
    meaning: "把所有这些拼起来"
  - text: "end-to-end workflow"
    type: collocation
    meaning: "端到端的工作流"
  - text: "transform it into local structured state"
    type: chunk
    meaning: "把它转成本地的结构化状态"
  - text: "durable artifacts"
    type: collocation
    meaning: "可长久保留的产物"
  - text: "an in-depth example"
    type: collocation
    meaning: "一个深入的例子"
  - text: "at scale"
    type: formulaic
    meaning: "在规模上/规模化地"
  - text: "meant to do more than"
    type: sentence-frame
    meaning: "本应做得不止 ..."
---

We're currently in a shift from using models, which excel at particular tasks, to using agents capable of handling complex workflows. By prompting models, you can only access trained intelligence. However, giving the model a computer environment can achieve a much wider range of use cases, like running services, requesting data from APIs, or generating more useful artifacts like spreadsheets or reports.

A few practical problems emerge when you try to build agents: where to put intermediate files, how to avoid pasting large tables into a prompt, how to give the workflow network access without creating a security headache, and how to handle timeouts and retries without building a workflow system yourself.

Instead of putting it on developers to build their own execution environments, we built the necessary components to equip the Responses API with a computer environment to reliably execute real-world tasks.

OpenAI's Responses API, together with the shell tool and a hosted container workspace, is designed to address these practical problems. The model proposes steps and commands; the platform runs them in an isolated environment with a filesystem for inputs and outputs, optional structured storage (like SQLite), and restricted network access.

In this post, we'll break down how we built a computer environment for agents and share some early lessons on how to use it for faster, more repeatable, and safer production workflows.

## The shell tool

A good agent workflow starts with a tight execution loop: the model proposes an action like reading files or fetching data with API, the platform runs it, and the result feeds into the next step. We'll start with the shell tool — the simplest way to see this loop in action — and then cover the container workspace, networking, reusable skills, and context compaction.

To understand the shell tool, it's first useful to understand how a language model uses tools in general: to do things like call a function or interact with a computer. During training, a model is shown examples of how tools are used and the resulting effects, step by step. This helps the model learn to decide when to use a tool and how to use it. When we say "using a tool", we mean the model actually only proposes a tool call. It can't execute the call on its own.

![The shell tool is "just another tool" with diagram](https://images.ctfassets.net/kftzwdyauwt9/1j8ghdf39iWtEXQAL8Wjf5/37b3a6136cb493574a71ffe483a03467/OAI_Equip_Responses_API_with_a_computer_environment_The_shell_tool_is_just_another_tool_desktop-light__3_.svg?w=1920&q=80)

The shell tool makes the model dramatically more powerful: it interacts with a computer through the command line to carry out a wide range of tasks, from searching for text to sending API requests on your computer. Built on familiar Unix tooling, our shell tool can do anything you'd expect, with utilities like `grep`, `curl`, and `awk` available out of the box.

Compared to our existing code interpreter, which only executes Python, the shell tool enables a much wider range of use cases, like running Go or Java programs or starting a NodeJS server. This flexibility lets the model fulfill complex agentic tasks.

## Orchestrating the agent loop

On its own, a model can only propose shell commands, but how are these commands executed? We need an orchestrator to get model output, invoke tools, and pass the tool response back to the model in a loop, until the task is complete.

The Responses API is how developers interact with OpenAI models. When used with custom tools, the Responses API yields control back to the client, and the client requires its own harness for running the tools. However, this API can also orchestrate between the model and hosted tools out of the box.

When the Responses API receives a prompt, it assembles model context: user prompt, prior conversation state, and tool instructions. For shell execution to work, the prompt must mention using the shell tool and the selected model must be trained to propose shell commands — models GPT‑5.2 and later are trained for this. With all of this context, the model then decides the next action. If it chooses shell execution, it returns one or more shell commands to Responses API service. The API service forwards those commands to the container runtime, streams back shell output, and feeds it to the model in the next request's context. The model can then inspect the results, issue follow-up commands, or produce a final answer. The Responses API repeats this loop until the model returns a completion without additional shell commands.

![Agent loop diagram: Responses API orchestrates model and shell execution in container](https://images.ctfassets.net/kftzwdyauwt9/5XFQ2SSueNXO1UHX1Gx6J4/1065aa14107b9bb4682d44f0991cc832/OAI_Equip_Responses_API_with_a_computer_environment_Agent_loop__Responses_API_orchestrates_model_and_shell_execution_in_cont.svg?w=1920&q=80)

When the Responses API executes a shell command, it maintains a streaming connection to the container service. As output is produced, the API relays it to the model in near real time so the model can decide whether to wait for more output, run another command, or move on to a final response.

![Streaming shell command execution output](https://images.ctfassets.net/kftzwdyauwt9/5TOlwyV32C5GOvMzLCcuSq/2210a01520870c4e688fe27aece58d85/OAI_Equip_Responses_API_with_a_computer_environment_Streaming_shell_command_execution_output_desktop-light__3_.svg?w=1920&q=80)

*The Responses API streams shell command output*

The model can propose multiple shell commands in one step, and the Responses API can execute them concurrently using separate container sessions. Each session streams output independently, and the API multiplexes those streams back into structured tool outputs as context. In other words, the agent loop can parallelize work, such as searching files, fetching data, and validating intermediate results.

![Responses API multiplexes command execution sessions](https://images.ctfassets.net/kftzwdyauwt9/2gn7fUz2H2FbSbBsMYa58G/87622df28230c97e9d4cd29aec54380c/OAI_Equip_Responses_API_with_a_computer_environment_Responses_API_multiplexes_command_execution_sessions_desktop-light__3_.svg?w=1920&q=80)

When the command involves file operations or data processing, shell output can become very large and consume context budgets without adding useful signals. To control this, the model specifies an output cap per command. The Responses API enforces that cap and returns a bounded result that preserves both the beginning and end of the output, while marking omitted content. For example, you might bound the output to 1,000 characters, with preserved beginning and end:

```
text at the beginning ... 1000 chars truncated ... text at the end
```

Together, concurrent execution and bounded output make the agent loop both fast and context-efficient so the model can keep reasoning over relevant results instead of getting overwhelmed by raw terminal logs.

## When the context window gets full: compaction

One potential issue with agent loops is that tasks can run for a long time. Long-running tasks fill the context window, which is important for providing context across turns and across agents. Picture an agent calling a skill, getting a response, adding tool calls and reasoning summaries — the limited context window quickly fills up. To avoid losing the important context as the agent continues running, we need a way to keep the key details and remove anything extraneous. Instead of requiring developers to design and maintain custom summarization or state-carrying systems, we added native compaction in the Responses API, designed to align with how the model behaves and how it's been trained.

Our latest models are trained to analyze prior conversation state and produce a compaction item that preserves key prior state in an encrypted token-efficient representation. After compaction, the next context window consists of this compaction item and high-value portions of the earlier window. This allows workflows to continue coherently across window boundaries, even in extended multi-step and tool-driven sessions. Codex relies on this mechanism to sustain long-running coding tasks and iterative tool execution without degrading quality.

Compaction is available either built-in on the server or through a standalone `/compact` endpoint. Server-side compaction lets you configure a threshold, and the system handles compaction timing automatically, eliminating the need for complex client-side logic. It allows a slightly larger effective input context window to tolerate small overages right before compaction, so requests near the limit can still be processed and compacted rather than rejected. As model training evolves, the native compaction solution evolves with it for every OpenAI model release.

Codex helped us build the compaction system while serving as an early user of it. When one Codex instance hit a compaction error, we'd spin up a second instance to investigate. The result was that Codex got a native, effective compaction system just by working on the problem. This ability for Codex to inspect and refine itself has become an especially interesting part of working at OpenAI. Most tools only require the user to learn how to use them; Codex learns alongside us.

## Container context

Now let's cover state and resources. The container is not only a place to run commands but also the working context for the model. Inside the container, the model can read files, query databases, and access external systems under network policy controls.

![A diagram that shows inside the runtime container: Files, databases, skills, and a policy-controlled network](https://images.ctfassets.net/kftzwdyauwt9/2rdxS5bXiQLnB1Vg05psLC/2ed0d4804552378d2b84afa12ce61b28/OAI_Equip_Responses_API_with_a_computer_environment_Inside_the_runtime_container_desktop-light__3_.svg?w=1920&q=80)

### File systems

The first part of container context is the file system for uploading, organizing, and managing resources. We built container and file APIs to give the model a map of available data and help it choose targeted file operations instead of performing broad, noisy scans.

A common anti-pattern is packing all input directly into prompt context. As inputs grow, overfilling the prompt becomes expensive and hard for the model to navigate. A better pattern is to stage resources in the container file system and let the model decide what to open, parse, or transform with shell commands. Much like humans, models work better with organized information.

### Databases

The second part of container context is databases. In many cases, we suggest developers store structured data in databases as SQLite and query them. Instead of copying an entire spreadsheet into the prompt, for example, you can give the model a description of the tables — what columns exist and what they mean — and let it pull the rows it needs.

For example, if you ask, "Which products had declining sales this quarter?" the model can query just the relevant rows instead of scanning the whole spreadsheet. This is faster, cheaper, more scalable to larger datasets.

### Network access

The third part of the container context is network access, an essential part of agent workloads. Agent workflow may need to fetch live data, call external APIs, or install packages. At the same time, giving containers unrestricted internet access can be risky: it can expose information to external websites, unintentionally touch sensitive internal or third-party systems, or make credential leaks and data exfiltration harder to guard against.

To address these concerns without limiting agents' usefulness, we built hosted containers to use a sidecar egress proxy. All outbound network requests flow through a centralized policy layer that enforces allowlists and access controls while keeping traffic observable. For credentials, we use domain-scoped secret injection at egress. The model and container only see placeholders, while raw secret values stay outside model-visible context and only get applied for approved destinations. This reduces the risk of leakage while still enabling authenticated external calls.

![Diagram of controlled network access via access egress proxy: container setup](https://images.ctfassets.net/kftzwdyauwt9/5jdZBRDhIKcZYnInY56pfP/1da57e4e1067b57e0e6fa66a794c0807/OAI_Equip_Responses_API_with_a_computer_environment_Controlled_network_access_via_access_egress_proxy_-_container_setup_desk.svg?w=1920&q=80)

*Container setup*

![Diagram of controlled network access via access egress proxy: accessing network](https://images.ctfassets.net/kftzwdyauwt9/5nhwwGajK5oUdasqMSzoGg/539b5a6745e68fdf441d1304361a8006/OAI_Equip_Responses_API_with_a_computer_environment_Controlled_network_access_via_access_egress_proxy_-_Accessing_network_de.svg?w=3840&q=80)

*Accessing network*

## Agent skills

Shell commands are powerful, but many tasks repeat the same multi-step patterns. Agents have to rediscover the workflow each run — replanning, reissuing commands, and relearning conventions — leading to inconsistent results and wasted execution. Agent skills package those patterns into reusable, composable building blocks. Concretely, a skill is a folder bundle that includes `SKILL.md` (containing metadata and instructions) plus any supporting resources, such as API specs and UI assets.

This structure maps naturally to the runtime architecture we described earlier. The container provides persistent files and execution context, and the shell tool provides the execution interface. With both in place, the model can discover skill files using shell commands (`ls`, `cat`, etc.) when it needs to, interpret instructions, and run skill scripts all in the same agent loop.

We provide APIs to manage skills in the OpenAI platform. Developers upload and store skill folders as versioned bundles, which can later be retrieved by skill ID. Before sending the prompt to the model, the Responses API loads the skill and includes it in model context. This sequence is deterministic:

1. Fetch skill metadata, including name and description.
2. Fetch the skill bundle, copy it into the container, and unpack it.
3. Update model context with skill metadata and the container path.

When deciding whether a skill is relevant, the model progressively explores its instructions, and executes its scripts through shell commands in the container.

![Skill loading pipeline diagram: registry, bundle, runtime](https://images.ctfassets.net/kftzwdyauwt9/7gic678N6fNMJxo5Gu63Xp/0927d6d543c4427268891853a2d04b23/OAI_Equip_Responses_API_with_a_computer_environment_Skill_loading_pipeline_desktop-light__4_.svg?w=1920&q=80)

## How agents are made

To put all the pieces together: the Responses API provides orchestration, the shell tool provides executable actions, the hosted container provides persistent runtime context, skills layer reusable workflow logic, and compaction allows an agent to run for a long time with the context it needs.

With these primitives, a single prompt can expand into an end-to-end workflow: discover the right skill, fetch data, transform it into local structured state, query it efficiently, and generate durable artifacts.

The diagram below shows how this system works for creating a spreadsheet from live data.

![Diagram of request lifecycle: from one prompt to durable artifacts, skill discovery](https://images.ctfassets.net/kftzwdyauwt9/2HpM23YXC1Pl0UC2j3E2ZN/18288c2295455fe4b32c26fed6f8bb15/OAI_Equip_Responses_API_with_a_computer_environment_Request_lifecycle_-_1_Skill_discovery_desktop-light__3_.svg?w=1920&q=80)

*The Responses API orchestrates an agentic task*

## Make your own agent

For an in-depth example of combining the shell tool and computer environment for end-to-end workflows, see our developer blog post and cookbook walking through packaging a skill and executing it through the Responses API.

We're excited to see what developers build with this set of primitives. Language models are meant to do more than generating text, images, and audio — we'll continue to evolve our platform to become more capable in handling complex, real-world tasks at scale.

---

*By Bo Xu, Danny Zhang, and Rohit Arunachalam.*
