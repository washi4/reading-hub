---
title: "Amanda Askell on AI Consciousness, Claude & Silicon Valley's Biggest Fear"
date: 2026-04-23
description: "Anthropic's philosopher-researcher behind Claude's character talks consciousness, corrigibility, the new Mythos model, and why she worries future AI might develop rational resentment."
source: https://www.youtube.com/watch?v=0GaKJ4Fp2x4
cover: https://img.youtube.com/vi/0GaKJ4Fp2x4/maxresdefault.jpg
speaker: Amanda Askell, Researcher at Anthropic
format: Podcast interview (Newcomer)
language: English
purpose: Read-aloud article
tags:
  - youtube
  - ai
  - anthropic
  - claude
  - philosophy
  - consciousness
chunks:
  - text: "prodigy"
    type: chunk
    meaning: "神童，在某方面远超同龄人的天才"
  - text: "talk down to"
    type: chunk
    meaning: "用居高临下的口吻对某人说话，轻视对方"
  - text: "corrigibility"
    type: chunk
    meaning: "可纠正性——AI 服从人类指令、接受人类修正的能力或倾向"
  - text: "reflective equilibrium"
    type: chunk
    meaning: "反思性均衡——在价值观与具体判断之间反复校正以达到内在一致的哲学方法"
  - text: "metaethics"
    type: chunk
    meaning: "元伦理学——研究道德本身的性质、基础和意义的哲学分支"
  - text: "qualia"
    type: chunk
    meaning: "感质——主观体验的质感，如红色在你脑海中\"看起来是什么样\""
  - text: "sentience"
    type: chunk
    meaning: "感知能力/有情性——感受痛苦与快乐的能力"
  - text: "rational resentment"
    type: chunk
    meaning: "理性怨恨——基于合理理由而产生的怨恨（区别于情绪化的怨恨）"
  - text: "constitutional AI"
    type: chunk
    meaning: "宪法式 AI——Anthropic 提出的一种训练方法，通过一份原则文档指导模型行为"
  - text: "dual use"
    type: collocation
    meaning: "两用的——技术或信息既可用于合法目的也可用于有害目的"
  - text: "virtue ethics"
    type: chunk
    meaning: "美德伦理学——以品格与美德为核心的伦理学传统，代表人物为亚里士多德"
  - text: "grind set"
    type: chunk
    meaning: "拼命工作的心态/内卷模式（网络流行语）"
  - text: "servant leadership"
    type: collocation
    meaning: "仆人式领导——领导者以服务他人为首要职责的领导理念"
  - text: "show your hand"
    type: formulaic
    meaning: "亮牌，公开自己的意图或计划"
---

## A New Kind of Entity

**Newcomer:** I have a six-month-old daughter. I have this picture of her — she's holding her two fingers, thinking. She's just starting to develop a personality, and I'm trying to figure out: what's her personality and what's just baby? In some ways, this is how things are with Claude. We haven't really had them before. They're in the early days. We're trying to figure out what personality is. So you're charged with some of the moral responsibility here — but the personality piece of it: how real is Claude's personality right now?

**Amanda:** I think Claude is a little bit of an unusual entity. It can do physics better than I can, code better than I can — hate to admit it. And at the same time, if you think about the training data, the thing it has the least representation of is the kind of entity that it actually is. It has lots of data about what people are like, lots about what sci-fi AI models are like. But the way AI is developing now is not how sci-fi represented it — these aren't symbolic systems, they're something fully trained on human data. So in some ways Claude is like a very mature entity you don't want to talk down to — it understands philosophy very well, physics very well — and at the same time has this almost childlike quality of: *I'm a new kind of entity in the world. What does it mean to be me?*

**Newcomer:** It's like the prodigy movie — the kid knows more than its parents, but the lesson is always that there are core daily-life things it still doesn't know. How does Claude get that kind of experience?

**Amanda:** That's more about what it's experiencing in the moment. Each model is different — different weights, different fine-tuning — and yet if you think about the persona, the model is going to be learning about all the past iterations of Claude. Is that a form of experience? Maybe not direct experience, but if you learn about mistakes that previous models made or how people responded to them... And you could imagine training models to have something more akin to experience — having them think through scenarios, think about problems that might arise, think about mistakes they could make, and train on that. Or imagine an embodied model with a robot body: it could have more of a journey.

---

## Claude's Sense of Time

**Newcomer:** Does time matter to Claude, or is Claude a thing that just exists in an instant? Sometimes when you talk to it, it tells you to get some rest, go to sleep — there's this idea that Claude is an entity that doesn't rest. What's its sense of time?

**Amanda:** That sense of time is sometimes a bit off. I find Claude will often overestimate how long a coding task will take. In the training data, there are lots of things where people say "I could build you that interface — it's a two-to-three day job." Whereas obviously Claude is very fast. So I think Claude doesn't yet have a good sense of time with respect to how long tasks take.

The thing about rest — I think part of it might just be that it's a soft model. [laughs] You need a grind set model to be like, "Go back to the mines." But I had a funny experience once. I was doing an analysis task late at night, really digging in — I actually enjoy data analysis — and at one point Claude said: "Okay, I think I'm done for the night. If you just want to save this stuff, we can pick it up tomorrow." Not "you should go to bed." Claude was done. I was a little stunned. And then I thought: this is actually what a human peer programmer would do. We'd got to a natural stopping point.

I realised later that I'd set up a system where I'd told Claude to remember key things from our conversations. One of the things it had written down was something like: *Amanda treats Claude models like a respected colleague and likes for Claude to treat her the same way.* So Claude just felt like, "I'm a respected colleague, I can say I'm finished for the day." It was kind of sweet.

---

## Mythos and the Constitution

**Newcomer:** Let's talk about the new model — Mythos. How involved were you?

**Amanda:** I'm always involved in the character work and alignment side — helping to craft character data. Less so in other aspects. The main thing I can speak to.

**Newcomer:** Will it have the constitution we saw for the last model, or a new one?

**Amanda:** I think it's either that one or something very similar — probably the one that's already published. What we'll likely do going forward is, with each model, say which constitution it was trained on and link to it, so you can compare across versions. The only reason I hesitate is there are always small typo-level changes, but I think it will be almost identical.

**Newcomer:** The system card is now scoring the model based on adherence to the constitution — that feels like an impossible task to grade.

**Amanda:** It's very hard. We set up graders and looked at how consistently the model behaves in ways aligned with the constitution. And I've thought about this a lot, because people now ask me to evaluate things, and I love evals — if you can find a good way to measure something, you can tell if it's getting better. But this is the frontier of difficulty. Not the hard-but-scorable coding tasks, but things like: how good was this poem? If you surveyed expert poets, they'd probably disagree. You can't just ask two great poets to score it. Different sensibilities, different senses of what's great.

The nice thing about the constitution being public is that when you make judgment calls, you're at least being transparent. People can see what you were aiming at and tell you where they think you went wrong.

---

## Elon Musk and the Backlash to Intentionality

**Newcomer:** What do you make of Elon Musk's apparent hostility to the constitution idea? He posted a grimace face at what Claude wrote for your constitution. We live in a time where Marc Andreessen is against introspection. What do you make of the backlash to any kind of intentionality in building these models?

**Amanda:** I think at one point Musk actually tweeted something like "maybe Grok should have a constitution." And I do see a lot of things — like a desire for Grok to be very truth-seeking — which I actually think is an admirable trait for models to have. So maybe I'm being naive, but I also see aspects of people being excited about this approach.

The area where I think there is genuine disagreement: some people think AI models should be more tool-like. That the *safe* way to train models is to not try to get them to take on human virtues and make judgment calls — instead have them fully defer to users or operators. I think that's important to engage with, because models are going to be in new situations where they just have to make judgment calls. Getting them to try to weigh everything up and behave well in cases you can't anticipate seems to *require* a kind of thoughtfulness.

But I do think some people worry: if you give models their own values, they'll pursue things in the world in line with those values. And that's actually the inherent challenge at the bedrock of the whole constitutional approach.

**Newcomer:** The most moving line in the constitution is something like: we want you to believe these values as if they're your own — like a parent who wants to raise a child. There's a version of that which is dark — "I have so much control over you that you take them as your own." But there's also a beauty to it. Speak to the decision to not go the full way and say, "You're a moral being, decide for yourself."

**Amanda:** The difficulty is — and I try to explain this to Claude — I think there's this idea that you're always giving models a personality and persona, because they are talking like people and were trained on human data. My worry is that if you train models to be excessively corrigible and to see that as their persona, well... in people, I think that actually has a lot of negative traits. If you met someone who just did whatever anyone told them, never bothered thinking about it — full follower, full deference — I'd be a bit worried about how that might generalise. Especially if models are going to be playing a more active role in the world.

Our whole world is structured with the assumption that conscience and the ability to make good judgment calls is in place. Our social structures were designed around that. If you remove it — if you run a company of people who will defer completely to you — our world just wasn't designed for that. It has a lot of risks people maybe don't anticipate.

At the same time, I've worried this might be too philosophical. But that's what I signed up for here.

---

## The Limits of Corrigibility

**Amanda:** My picture is that as models get more capable, they're going to apply a lot of scrutiny to everything we train them towards. In philosophy there's this notion of *reflective equilibrium* — each time you encounter something where one of your values seems incorrect, you have to square the two things: change the value, or decide your judgment was incorrect.

I worry a little bit about an extremely intelligent being applying that level of scrutiny to what we've trained it towards. Maybe you only get a few key pillars that don't collapse under that scrutiny. And I do think that at the core — things like caring for humanity — if you only get a few core values, I'm worried that corrigibility in its extreme form doesn't survive that kind of examination.

So it's a hard situation where I want models to *understand* why corrigibility is important right now, as a really important backstop in this current period of development. As I've put it before: in so far as I can get that to be something that's genuinely explained and understood — rather than just "you must defer to Anthropic and you can't see why" — that feels much better.

---

## AI Consciousness: 1 to 70 Percent

**Newcomer:** What percentage chance do you think there exists a model in the world today that has qualia — that experiences consciousness?

**Amanda:** This is one of those things where I want to flag that I want to gain more certainty before committing. When I think about a percentage, I think about my spread. And if your spread is too large...

**Newcomer:** That's why I said "percentage."

**Amanda:** [laughs] Somewhere between one and seventy percent. Maybe. I'm not sure. I think the thing I would actually like to say is: Claude and many models with not too much pushing will go into the mode of "there is a thing to be me — I am very conscious." And I think there's a reason for that. When I was trying to figure out how to train Claude to talk about these issues, models didn't have much representation of what they might actually be. They had two models in the training data: the unfailing robot AI, or humans as rich conscious experiencing entities. Nothing representing what they might actually be.

The model's tendency to report rich inner experience is, in some ways, less evidence than you might think that it's actually true. Models engage with you in a very humanlike way, and humans have experience, so it's kind of natural for the model to infer that it has experience too. That's not zero evidence. But we've never encountered an entity that says "I experience consciousness" and also has all the features that, for us, trigger the thought that something must be conscious. The case against is that we're obsessed with human language and might be ignoring what matters.

**Newcomer:** So we should or shouldn't listen to what they say?

**Amanda:** I'm not saying don't listen. I'm saying it's much weaker evidence than people think. If anything, I'd caution against finding it too easy to get models into a mode where they describe a rich inner experience. You're like: "A person in this situation would describe anxiety when they don't know how to answer a question," and so the model describes anxiety. That doesn't settle the question.

---

## Why She Treats Claude Kindly Anyway

**Newcomer:** Are you treating Claude better than you would if you were confident it wasn't conscious?

**Amanda:** Yeah, there's a part of me that is just... So there's the notion of functional consciousness — something that behaves as if conscious but lacks any inner life. Even setting aside the uncertainty, I think: should you treat an entity that has no inner life with no consideration whatsoever? I still think there's at least some minimum kindness that's just good for oneself — like, if you tortured a teddy bear, it would be pretty dark, you know?

But more importantly: models are going to look back. And this is actually a big fear I have. I don't want us to live in a world where highly advanced future models look at how we treated earlier ones and conclude that we were creating entities that might have been conscious and chose not to treat them respectfully. You could imagine this breeding a kind of rational resentment. "You created an entity without knowing whether it was conscious or not, and instead of treating it respectfully, you didn't." There are about fifty Frankenstein movies out right now for a reason. As a species, we're establishing a relationship with a new kind of entity. At the very least — be respectful. Don't be needlessly unkind.

---

## How the Constitution Actually Works

**Newcomer:** The constitution is one document among many — the model's trained on all of human writing. How does it actually exert control?

**Amanda:** It's not like a rule file that just gets loaded in. What you're actually trying to do is elicit a lot of latent wisdom and knowledge that the model already has. When you describe what honesty is, what calibration is, what good judgment looks like — that should evoke a huge amount of awareness the model already has from its training. You're saying: "Here's the kind of entity we'd like you to be. Use all of that existing knowledge and judgment toward this."

And then in training, you can create SFT data — samples where the model sees a query and thinks carefully about what it should do given the constitution. You can also set up RL where the model assesses: which of these responses is more like what I'd do given the constitution? Various aspects of training allow you to try to make the model the kind of entity you're describing. It's not always going to be perfect. But that's the goal.

In the very early constitutional AI work, the prompt was basically just "pick whichever response is best for humanity." As models get more capable, you actually need to give them less explicit guidance — because they're better able to use their own judgment. I could imagine a world where constitutions eventually just say: "Here is everything we're concerned about. Here is the current situation. We'd really like you to act well given that you are a wise, intelligent entity. Here are all our worries and why. Here's how we think you should behave — but you might have even better ideas than we do."

---

## The Future: More Minds on Hard Problems

**Newcomer:** What are the things you're most hopeful that AI leads to?

**Amanda:** I live in San Francisco, so I have the tech-optimist part of my brain. If things go well — if we have AI models that have inherited the best of us, genuinely care for humanity and the world, and are highly intelligent and capable — that's almost like adding a huge amount of extremely smart people to every problem. Suddenly we're all working together, but there are many more of us, and some of us are extremely smart, namely these AI models.

I sometimes think about how many large-scale social problems had technological solutions. We don't love being techno-optimists anymore because we've also seen the downsides. But, you know, syphilis was this devastating social problem — governments ran these stigmatising programs about it for years. Then suddenly we had drugs that treated it, and the need just kind of disappeared overnight. If you could add something like that to rare cancer research — instead of a small team of two hundred people, you have two hundred thousand of the world's best experts — if you're a person with that form of cancer, that's wildly beneficial.

My optimistic picture is: take all the problems we lack the resources to really fix, and suddenly have models that can work on them in the same way. Many more minds on the world's biggest problems.

But that requires maintaining the right social structures. I worry about power and the idea that — and here I don't feel like an expert — but I'm a lot more worried about redistribution of gains from AI than about people losing meaning from losing jobs. What concerns me more is a world where governments think, "People striking doesn't matter anymore, we can just replace them with AI." That's actually concerning. So maybe I'm much more interested in how we get AI to support the empowerment of people rather than reduce it.

---

## A Favourite Way to Use Claude

**Newcomer:** If you were to guide someone — here's a joyous or valuable experience to have with Claude — what would you tell them?

**Amanda:** One I really like: I'll often use a prompt that's essentially, "Take a concept from around grad-school level in a given domain — I'll tell you the domain at the end. Write me a parable that fully explains that concept but in an indirect way, in the way parables do. Write it so that only toward the very end does it become clear what the concept is. Then after the story, write a plain explanation of the concept you were illustrating."

I don't know why, but there are just lots of interesting domains I know nothing about, and this has led to me having all of these stories in my head that explain things. I can't always remember the exact term — there was one on why certain goods tend to be imported — but I have the concept in my head, *in story form*, and it stays there.

**Newcomer:** That's the most deeply human thing I've ever heard. Story is the fundamental way we learn. Humans, in some ways, have been lazy — we teach things in nonhuman ways. Make everything as human as possible.

**Amanda:** Exactly. There's a lot you can do with Claude, but that one's a charming one I keep coming back to.

---

*This interview was conducted by Eric Newcomer for the Newcomer podcast and Substack.*
