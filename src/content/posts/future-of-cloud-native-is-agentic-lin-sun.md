---
title: "The Future of Cloud Native Is Agentic — Lin Sun, KubeCon 2026"
date: 2026-04-27
description: "Solo.io 开源负责人 Lin Sun 在 KubeCon 2026 上展示如何用 AI agent + MCP 服务器管理 Kubernetes，并在台上飞了一架无人机。"
source: https://www.youtube.com/watch?v=AUtZ0TkZb8I
cover: https://img.youtube.com/vi/AUtZ0TkZb8I/maxresdefault.jpg
speaker: Lin Sun, Head of Open Source, Solo.io
format: KubeCon keynote + live demo
language: English
purpose: Read-aloud article
tags:
  - youtube
  - cloud-native
  - kubernetes
  - ai
  - mcp
  - kubecon
chunks:
  - text: "fast forward"
    type: formulaic
    meaning: "快进到（某个时间点），跳过中间过程"
    note: "常用于叙事中跳跃到未来某节点，如 'fast forward two years'"
  - text: "navigate the ecosystem"
    type: collocation
    meaning: "在生态系统中找到方向、摸清门道"
  - text: "play a huge role"
    type: collocation
    meaning: "发挥重要作用"
  - text: "fingers crossed"
    type: chunk
    meaning: "希望好运，祈祷一切顺利（双手交叉手指的动作）"
  - text: "fall back to"
    type: collocation
    meaning: "退而求其次，回退到备用方案"
  - text: "wrap up"
    type: chunk
    meaning: "收尾，总结，结束"
  - text: "in the open"
    type: chunk
    meaning: "公开地，开放地，不藏着掖着"
  - text: "burned my demo gods"
    type: chunk
    meaning: "消耗了演示运气（幽默说法，意为为了一个效果搭上了所有运气）"
  - text: "mutual TLS"
    type: collocation
    meaning: "双向 TLS 认证，双方互相验证证书的安全协议"
  - text: "you always need a backup on stage"
    type: sentence-frame
    meaning: "台上永远需要备用方案（现场表演铁律）"
---

## From 2016 to 10 Million Users

I still remember my first KubeCon. It was in Seattle, 2016 — the very first KubeCon organized by the CNCF. Like many of you, I spent most of that conference trying to figure out what Kubernetes even is. What is a pod? What is declarative YAML? And Helm was one of the biggest things at the conference.

Fast forward to two years ago: as part of the TOC, I surveyed the cloud-native community — leaders and end users alike — asking what the biggest pain points were in the ecosystem. And I heard the same answer over and over: *complexity*. Too many things to learn, too many tools to pick from, too hard to just navigate the ecosystem.

Last year in May, I had the opportunity to attend KCD Texas, where Chris Aniszczyk gave a keynote about how we scaled cloud-native users from zero to ten million in less than ten years. That is a genuinely impressive number. But I started thinking: how do we do better? How do we reach the *next* ten million users — and do it faster, without adding even more complexity?

With the rise of agentic AI, I believe it is going to play a huge role in the future of cloud-native.

## The Demo Setup

Let me show you what I mean. I have Cursor open with an MCP server configuration. I have two MCP servers running: one is my Solo CDM MCP server running inside my Kubernetes cluster, and the other is the GitHub MCP server proxied through an agent gateway proxy. I also have my own AI agent exposed as an MCP server.

I want to show you a demo application I built for this keynote. Let me start simple.

> *Hello. Can you please create an Argo CD application for me using the Argo CD MCP server? Call it "demo", namespace is "default", path is "YAMLs", repository is…*

[The network drops.] Ah — conference Wi-Fi. You can't rely on that. [laughter]

Let me try again. Fingers crossed.

## AI + MCP + Kubernetes in Action

After a brief network recovery, the AI picks up the request and creates the Argo CD application. It asks for my approval — which I enthusiastically give — and the application starts syncing into the cluster.

Once it's synced, I hop into the Argo CD UI to confirm: the front-end and back-end are running, a dedicated gateway is deployed, and everything looks healthy. But there are no HTTP routes yet — so no way to actually access the application from outside.

This is where the second piece of the demo comes in.

> *Hello. What K agent agents do you have access to?*

K agent is a CNCF sandbox project. I have two agents running on top of it in my cluster. I ask the AI to involve the reliability agent with a specific task:

> *Can you create an HTTP route from the agent gateway proxy in the default namespace to the front-end service in the default namespace? And can you also open a pull request for me, grabbing the repository from the Argo CD application?*

The agent gets to work. A few moments later — a PR appears. [applause] I walk the audience through it: an HTTP route from the agent gateway proxy to the front-end, running on port 80. The room approves. I hit merge.

Argo CD syncs the new PR into the cluster. The application is live and reachable through the gateway.

Every connection is secured through mutual TLS. I am running everything in Istio service mesh with ambient mode — no sidecar required. The stack: Argo CD, GitHub MCP server, K agent as MCP server, agent gateway as the MCP gateway in front of all the servers, and agent scale handling routing logic.

That was mission number one.

## Mission Two: Flying a Drone on Stage

Our next mission was even more ambitious: fly a drone on stage. I placed a small drone right next to me on the podium and attempted to connect to its Wi-Fi.

"You guys are using all this Wi-Fi?" [laughter]

After multiple reconnection attempts — and burning my demo gods getting the HTTP route just right — I eventually managed to get the drone airborne and flying across the stage. [applause] The camera feed, however, refused to cooperate. 

"You always need a backup on stage." [laughter]

The backup plan: a web camera on a phone. Not glamorous, but it worked. I captured photos from both sides of the audience and had the application run an AI comparison — analyzing engagement, smiles, and active gestures.

## The Future Is Agentic

Let me wrap up. In this demo, we showed:

- **Argo CD + MCP server** — the AI created an Argo CD application via natural language
- **K agent exposed as MCP server** — a CNCF sandbox project bridging AI agents and Kubernetes
- **Agent gateway** — serving as the MCP gateway in front of multiple MCP servers
- **Agent scale** — enabling the agent to craft the perfect HTTP route autonomously

Cloud-native reached ten million users in ten years. Agentic AI is how we reach the next ten million — faster, with less friction, by letting AI navigate the ecosystem on behalf of new users.

So let's build. Build more MCP servers. Build more AI agents. Build more skills. And let's do it in the open, sharing with each other, keeping the cloud-native community moving forward.

Thank you. [applause]
