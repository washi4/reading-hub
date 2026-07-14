---
title: "Why My AI Workflow Is Better Than Yours (as a Software Engineer)"
date: 2026-07-14
description: "Duke Pan walks through his AI workspace, memory setup, manager-worker automations, and engineering workflow."
source: https://www.youtube.com/watch?v=TK6R_8ZWSvs
cover: https://img.youtube.com/vi/TK6R_8ZWSvs/maxresdefault.jpg
speaker: Duke Pan
format: YouTube workflow tutorial
language: English
purpose: Read-aloud article
tags:
  - youtube
  - ai-workflow
  - software-engineering
  - productivity
chunks:
  - text: "the key idea here is"
    type: sentence-frame
    meaning: "核心想法是……"
  - text: "learn along the way"
    type: chunk
    meaning: "在过程中学习"
  - text: "no matter what you do"
    type: sentence-frame
    meaning: "无论你做什么"
  - text: "by the end of this"
    type: sentence-frame
    meaning: "等这件事结束时"
  - text: "most of the time"
    type: formulaic
    meaning: "大多数时候；通常"
  - text: "the reason for that is"
    type: sentence-frame
    meaning: "那是因为……"
  - text: "the problem with that is"
    type: sentence-frame
    meaning: "那样做的问题是……"
  - text: "instead of saying"
    type: sentence-frame
    meaning: "不说……而是……"
  - text: "when you're done"
    type: sentence-frame
    meaning: "你做完之后"
  - text: "from one chat to another"
    type: chunk
    meaning: "从一个聊天窗口到另一个"
  - text: "spin up projects"
    type: collocation
    meaning: "快速创建项目"
  - text: "being slept on"
    type: formulaic
    meaning: "被低估；没有得到应有重视"
---

What's up guys? Today I'm going to show you my complete AI setup and workflow. This is going to be useful for you whether you're a software engineer, a student, a business owner, founder, creator, or just an individual who wants to increase his productivity and efficiency overall. The key idea here is that your AI becomes more useful when it has a proper workspace and memory setup. A lot of people talk about second brain or clone yourself, and this is exactly what we're doing here, but it's more than just a file or a wiki.

It involves the entire workspace you're working in and it's related to all the repositories that you work in within the workspace as well. So, I'm going to show you what harness I use, what model I use, and how my memory is set up, and some of the deeper engineering workflows I go through, and examples of automations I have. By the end of this, you should have a much better idea on how to set up your workspace as well, so that it can improve over time with you and learn who you are, and also just how all of this works together. I have a software engineering background. I worked at companies like Meta, Coinbase, and Tesla AI, and also have my own startup.

I'm also integrating AI and building AI agents into a billion-dollar big tech company. So, I have been working with small, medium businesses, and also startups, and big tech scale type of data for AI agents integrations. So, this is exactly the workflow I use for software engineering workflows, but also my own business workflows. And you don't even have to know how to code, you can learn along the way. It's more so processes and frameworks that you have to understand, which will help you no matter what you do.

So, quickly here, three concepts you have to understand is the model, the harness, and the workspace. So, the model is the actual intelligence, whether you use GPT 5.5, for example, Claude Opus, or Fable. That determines the level of intelligence your harness will have. The harness itself is sort of the platform around the intelligence that tells the intelligence how to use certain tools that it has access to, or open the browser, how to browse around things. It can loop itself on the intelligence to perform chain of thought, or maybe elicit you for more questions, deciding when to continue and when to stop.

So, that's part of the prompt, but also the harness capability itself. So, harnesses are stuff like Codex, Claude Code, Open Claw, and Hermes, or Pi. Then, the workspace itself is where you're going to open your harness and apply your intelligence in. So, this can just be a folder locally on your laptop or computer in the cloud or it could be in a sandbox. Most of the time it's just going to be local to your computer.

So, you should choose a folder where you're super set your master workspace and a lot of your files and other projects will be within this larger workspace and you'll see why. So, one of the most important things is you want to have your workspace to be model agnostic. You want to be able to change what model you use for whatever project you're in and still retain the memory of previous stuff you worked with. So, the main harness I actually use is Codex most of the time. Cloud Code is really popular right now.

I think Codex is being slept on and the reason for that is because the Codex desktop UI is incredibly well done and I think it's the best UI experience you can get out there between any of the harnesses currently existing and that's why I also use this over the CLI or terminal. It's very easy to spin up projects. For example, on your left side you see all your projects. You can open a new one that is local or remote on a different machine and it appears here as a separate thing. In the Cloud's UI you actually have to create a new group.

It's not automatically made for you. And you can also send messages from one chat to another. So, that's essentially sending a message from one agent to another. I'll do an example here. So, here I'm going to say, "Can you send a message to my other chat session titled test workspace?" Now, we don't need extra high for this.

We can just use light reasoning. So, a lot of times it's good to change between the reasoning levels when the thing you're doing doesn't require that much. This is not even so much to save tokens because if you're on, let's say the pro plan, you have a lot of tokens. It's more so for the speed. When you use light mode, it's just way more fast and extra high or high definitely for any type of planning activity or a more involved task and light and medium for easier tasks for speed.

And you can see here it says, "I found a thread titled test workspace. What message do you want to send to it? Just send hello." So, for example, this can be super useful when you already have a project going on and you have another chat session that is somewhat related to it. So, maybe in the other chat session you were doing some research, and in the other agent you were doing implementation. So, then from your research, when you're done, instead of saying, "Oh, give me a summary." and then you copy-paste that into the other chat session, which is something you would have to do in Claude, uh you can just say, "Send this message over there." And you can see delegation received from this other chat, and it will tell you sent from Codex from another thread.

So, the UI is very good here. And sometimes, when you send a lot of stuff, there's also it appears like by itself a list of steps it's like taking or it's running through. Also, you have on your right side a side chat. This will contain all the context that you have here previously. So, a lot of times you just want to ask something on the side, you don't want to pollute the main context.

It's very easy to just start the side chat, and then you can say, "What was I talking about?" And you'll see it this will have the complete context of everything that was here. You see, you basically set up the side conversation, visible context. So, the agents.md is a file that's automatically sent into each one of your chat sessions, so it's obviously going to have it here. And you can see delegated side thread with input hello. In Claude, for example, you'd have to use the {slash} by the way command, but the problem with that is the by the way command pops up a separate window that does not have access to any of your tooling.

Like, it cannot browse the web on the by the way chat, right, the pop-up. But here, this side chat in Codex has essentially all the functionalities that your main chat has, but it contains the context. And so, you can perform even heavy research in here. But the only thing is this side chat will expire after some time, which is fine, because you can always send this to again a new chat here if you want to preserve it. So, you have a lot of flexibility on how you send your messages between your different agents.

You can also spawn a new work tree as a new chat session. Spawn a new work tree from this chat session and make it a new chat. So, the Duke Bot workspace I have is the main workspace all of my projects are in. Look at this, it creates a new chat that appears on the UI here that indicates that it's a fork through this little arrow here, and it has all the context of the the one. So, then you can do more experimentation here without messing up the existing implementation that you already continued here.

And it has this UI as well indicating the work tree that it created. So, it's very flexible on any type of agentic activity you want to do within. Then obviously also have the remote control here. If you see the little green dot, these are chat sessions and repositories that are on my Mac mini in my other room and I can directly access these chats from my MacBook that I'm on currently. So, this will edit the file system on my Mac mini.

And this is very easy to set up. Just in settings, you can go to connections, you can control other devices and you can just set it up here. So, it's very quick. Claude has something similar, but in my experience when I tried to set it up, it has been a lot more laggy and buggy than Codex. Now, I do also use Claude.

Claude sometimes I feel like it's better at design and also Fable 5 is obviously the most intelligent model right now out there, but there's also some drawbacks to Fable where it's kind of slow. Fable is more of something I'd want to just give it a prompt and then I leave or do something else. Cuz it always runs for a while. And Fable performs well at those tasks where you give it a big task and you let it run. It's not as good for a little fast back and forth because it's not fast.

And it doesn't have fast mode compared to Codex which has the fast mode. It's just better overall when your iteration is faster because then you get to answer your questions faster and get to see the results faster and then you see if your idea is working or not. So, Claude I still like to use it for Fable and sometimes I switch it to send F5 when I'm just asking like a quick question, but most of the time if I'm using Claude it's because I want to use Fable. So, for example here, I'm working on a content automation system that automatically downloads my virtual long form content from my live streams. I stream every Sunday on YouTube and on Twitch myself Vibe Coding, my business and also I have client calls where I'm helping people integrate AI and just working on their business in general and I want to have this content automation system that automatically clips all of my stuff and post them and also generates a thumbnail, the title and uploads.

So, this is quite an involved system, especially some of the videos I have are over 3 hour long. So, this is where I'm using Fable to kind of give me the architecture of my workspace for like this specific content agent. And the last piece of harness I want to show you guys is my open claw. So, uh you can either use open claw, Hermes, or even both. I already had open claw set up.

I think if I had to set it up today, I would set up Hermes cuz it's just a bit more stable. But, open claw works great for me. I already have it set up. For example, here, you know, I can see I have a trading bot that I have been running for a while and I have multiple different type of agents in here. I have like a one for admin, which I use for any type of like a email negotiation, brand sponsorships, making media kits for me, and just checking my emails in general.

Got to have a coding one that focuses more on my coding tasks. I have a creative one for video scripting and stuff like that. And this is my general bot here where I have general stuff. For example, this is like I think this is like a weekly heartbeat or something that tells me how much I spent. I think this is like a daily thing.

This is just for something specific cuz I was trying to see how much the heartbeat cost because open claw uses a lot of tokens. So, you should be careful when you set this up. If you don't have the pro plan in GPT, I probably wouldn't recommend having the heartbeat at all. So, I set it to the like very cheaper model to see how much it cost. But, you can see this is not a lot, but what the heartbeat it is is just every day checks your workspace and your transcripts and it sees if there's something to notify you with.

For example, if I have a meeting coming up, it'll tell me. But, again, this is something for open claw. I also have something for my receipts. I throw business expenses I want to write off. Every week it runs this.

It looks at my emails and see what are potential stuff that I need to note down as a business expense. So, this one it says no strong business recommendations this week. It also has a weekly memory MD curation. So, I'll get to this during the memory section, but essentially I want to show you that this is my open claw harness, which is communicates with me through my Telegram. And the open claw is set up on my Mac mini.

So, it just runs 24/7. I can talk to it anytime. I also have this set up with, for example, my mom. I have like a therapist bot for her and I also have it with my friends and my brother. So, a lot of people can use my open claw.

So, if you're asking for the main differences, now open claw, I mostly just use it as a personal assistant, right? So, if I'm on the go, I can send messages to it. It's always running for me. I can connect it with other people more easily through Telegram, whereas like Codex and Claude is kind of harder. You'd have to implement them with some sort of Telegram, whereas Telegram is like almost built in to open claw.

So, it's just easier to set up and it acts more for me as a personal assistant that reminds me of things. I can run cron jobs on a weekly or daily basis. And when I'm traveling, for example, I went to Mexico with my girlfriend last week, it planned the whole itinerary for me. Then I can update it within open claw itself and it always has the memory of our reservations and itineraries and stuff like that. And my girlfriend can also ask it to update it.

I know I'm going through a lot and because this video is supposed to be sort of a overview, I can't go into any of these too deeply, otherwise this video would never end. So, if you're interested in any of these parts I'm talking about, I can deep dive into Codex, into Claude, into the harness part, into open claw and how to set any of this stuff up. Just let me know or come to my live streams or join my private community. I can talk about any of that over there. All right, so that's what it comes with the harness.

Now, let's talk about the models a bit before we go to the workspace part. As far as models go, I talked about this a little bit, but for Codex, definitely GPT 5.5 and you want to use extra high or high when it comes to any task that you feel like it involves a lot of changes or a lot of planning. And for any type of implementation, you can just use medium or light. So, depending on what plan you have, if you're on the pro plan, $200 a month, ChatGPT or OpenAI subsidizes a lot of credits. I feel like it's more credits than Claude.

So, you can feel free to use higher extra high more on fast mode even and you're still going to have enough tokens unless you're really just like spamming as hell hard. And for any type of quick questions, I usually use light mode because it's just faster and it consumes less tokens. Then when it comes to Claude, Fable 5 is best for any type of complicated deep reasoning, long activity and the way you want to use this is you tell it to delegate to cheaper models like Opus 4.8 or Sonnet 5, Sonnet 4.6 during the implementation. During the prompting, you just say delegate tasks to cheaper models like these so you can save on tokens because Haiku 5 is damn expensive. I'm on the max plan because I'm sponsored by Anthropic and they give this for me for a few months, but if I wasn't, I probably would have the regular pro plan because most of the time I'm using Codex.

And Haiku is also going to be gone off the subscription plan very soon or even by the time this video is out. Honestly, I would probably go for the Codex plan more so than the Claude one. All right, now finally we talked about the harness and the model and now we're going to talk about the workspace. My workspace is called DukeBot. You can see all the files and folders inside here and this is essentially how you set up your agent.

You want to be very careful how you set up the set of folders and skill files and memory files, all this stuff. My base repository is set up through Open Claude. When you set up Open Claude, it gives you some of these files, for example, the memory folder and some of these other ones too, but a lot of these I added afterwards. Essentially, if you set up Hermes or Open Claude, it comes with the built-in memory system and you can leverage that as a starting point, but you still have to update your workspace a bit because you want your workspace to be model agnostic. Meaning, whether I use this workspace with in Codex or Claude or Open Claude or Hermes, it's going to know the same things about me.

And this is very important because these Frontier Labs can change their models or close access to their models or sometimes it's the same model, but they deteriorate the performance. It's just not stable. You cannot count on them on being the same level of quality and same price over time. So, you have to build your workspace for the long term here that is model agnostic. And one way to do this is to set up your workspace with an open source harness first like Hermes or Open Claude.

So, it has some built-in memory stuff. Most importantly, you also want to put into your agents.md. Agents.md is the file that both Codex and Claude are going to read in. Claude is going to read in the Claude.md, but you can just put and read agents.md within the Claude.md. So, it's like centralized file for the short-term memory stuff.

In here, I specify my memory routing. So, the reads and the writes. That way, every time Codex perform a session, I finish a a sort of a task within it, it's able to write stuff back to my memory, and also it knows to read through my memory. So, whatever I'm doing with an open claw, Codex, or Claude, any of these harnesses will have memory of long term. So, I would say there's four parts to long-term memory.

I kind of call it medium-term memory. So, this one, agents.md, is kind of like a medium-term, right? It's just like that memory file. It's the same as like memory.md. And then you have your actual really long-term memory, which is one, a knowledge graph, two, a tabular database, and three, a vector search database.

The knowledge graph is what's commonly known as the second brain or Obsidian graph that a lot of people talk about, and I have this here within my wiki. I can show you within my Obsidian itself. You can see that it looks like this. It has a lot of my stuff that are related to me and some of the clients I have, some of the stuff I'm working on, or videos I'm working on. So, a bunch of stuff.

I don't think I'm going to click into them because there's some confidential stuff. I have, for example, clients I work with, and if you also have that, or even if you're an employee, let's say you're working at Big Tech, then you're going to have projects that you work on, or other teammates. These are all good things to have in your knowledge graph. That way, your agent knows everything, just like how you know everything. So, then it can do anything you can do.

And again, you want to have this in your medium-term memory, so that it's always updated, right? So, it says, "Read the wiki for relevant durable background pages, and only open specific pages needed." It's not going to ingest the whole thing. It's all within one page, there's like links to other pages. It knows if it should traverse a link list, right, or not. I also have a vector search database that is not written here because I just set it up, I think, last week, but essentially using Neon.

So, I'm using Neon for my tabular and vector search database. I don't have this set up properly in my agents.md yet because I'm still testing some of the workflows to make sure that things are good, but it's definitely something I would add here if I want to completely optimize my long-term memory workflow. For example, Open Claw checks through a vector search on your past transcripts. So, if you ask something, it will kind of look through relevant past transcripts into your new chat. And that's part of the reason why it consumes a lot of tokens is because it has this memory capability.

Also, you can see my few workspaces here. I'm in coding creative research. These are folders that OpenClaw has set up for me. So, if you create a new agent with an OpenClaw, they just set up these repositories automatically. And then you see I can also have my content automation system repository.

So, these are like repositories within repositories. They're like Git sub modules. And within this one, I built most of these projects within Codex and Claude itself without OpenClaw. But it's in the same outer space. And any of these harnesses are able to access this repository and play with the functionalities in here.

So, for example, if I tell it to look within here to start, let's say a editing workflow, automated editing, then it will look into this agents.md. Remember, agents.md is usually like the entry point for any of these agents you're running, and it'll be able to know that whatever it files it needs to access to either start the editing workflow or the title packaging workflow, or thumbnail workflow, uploading, whatever it needs to do. All right, so that's pretty much it about the workspace and the memory. Again, let me know if there's any parts of that that you would like me to dig deeper on or have completely tutorial on how to set that up. Let's show an actual example for my content automation workflow here.

So, I can show you guys an actual automation. And let's just say we're running a test to show a demo. I would like to show the audience the idea, the clipping workflow we have that picks ideas from existing VOD, to video, long-form video. And let's say it edits three clips. And for this, [snorts] it's mostly implementation of existing stuff.

I'm just going to use Medium here. So, a lot of times when you ask your agent for some stuff, you can say, "Give me your answer in an HTML." So, it's like a visual format, and it will display on the side here the actual HTML visual, and it's just easier to look at the answer. But here, since it's like a video, I'm not going to do that. I guess I can explain how this process works a little bit while it's running. For this part specifically, it has already access to this 3-hour VOD and it needs to transcribe it first of all into different chunks and then gather the segments of topics that are related together and then from those topics it needs to select the ones that seems relevant for a good video.

I have design principles within this to indicate what's a good video and what's not. As so you see very fast, it generated a few already. Oh, well, this is exactly what I was talking about the visual summary. So this is from like a live stream I did. Let's see this video.

And you need to break your eyes reading all the slop. Too much reading. That's very true. I have the same experience. It's a lot of reading.

One way to help with this is instead of making your AI generate a text response, tell it to generate an HTML visual so that you can actually look at the thing visually. Much easier on your eye and your brain since your, you know, prefrontal cortex is much more developed for visual learning than to read. That's true. That's one way to help it and also just tell it to be more concise and, you know, respond with less text. That's why you have to be very careful how you See, there's a cut there, too.

And you have subtitles. It has a little nice fade out. So this is an example of a clip. It's a pretty simple one. I think this is great.

Like I would post this as part of my clips channel at I'm Duke Pan. I have a lot of stuff on there, so go check it out if you want to learn more. So you can see this workflow essentially working, right? So this went from mostly editing because I think I already ran the transcribing workflow before for this specific VOD. But the idea here is when you're making automations, you want to make sure you have a manager worker pattern.

In your prompt design, you want to specifically indicate cuz usually when your workflow is a bit complicated, you have multiple steps. You can't just have one single agent do all of these steps. So you want to have the manager agent delegate each of these steps to other agents. And these other sub agents can also delegate to other sub agents. And this works no matter what harness you're using.

It can just spawn sub agents to do the specific workflow and then your manager agent can either tell it to retry or if there's an issue or elicit you for more questions. So that way you protect the context of the managing agent. Otherwise, all your defined steps within your prompt might get lost and you're going to not have deterministic workflows. That's essentially what you need if you're having some medium-size complicated workflows. Honestly, even if you have an easy workflow, I would still recommend using the manager-worker pattern for sub-agents.

Now, if your thing is like very complicated or if you're working in Big Tech where access and security is more important, then you might want to implement an actual custom agent for it using something like LangGraph. So, then you have explicit code that's telling you based on the LLM decision, do you want to go this way or that way? So, then you only have two possibilities and the LLM can't just choose some random stuff that you're not supposed to do. It just depends on how strict your workflow needs to be. For most of the cases, if you just use manager-worker pattern, it works pretty nicely even if it's just LLMs controlling this.

Now, for the actual engineering workflow, if you're software engineering and you push your PRs, even if you're not, when your project gets a little bit more complicated or if you have clients, then you have to be careful when you're vibe coding. You can't just push code in without reviewing it. You want to have agent set up to review. Now, you got to just keep in mind what the bottleneck is because writing code now is a lot faster and easier, but the review process is still a bit bottlenecked. So, in order to help with that, what I usually implement, for example, if I'm working with a Big Tech client, all of the PRs there, I have multiple agents reviewing the PR.

So, if I implement it with Codex, then I would have Claude review it. Codex review those comments and make any appropriate changes and then Claude review it again and Codex makes any changes. So, I have exchange for maybe one to three exchanges just to make sure and then it has a confidence level that's indicated on the PR on how comfortable it is to merge. Now, you want to be careful here. You can merge things just like that by looking at the code a little bit and mostly letting agents do the review process.

But, this mostly works if you already have most of your architecture foundation set up for your code base. All right, let's say if you're building a website or an app, you want to make sure the foundational architecture is good. So, spend a lot more time on designing the foundational architecture in the early stages. If you don't and your foundation is trash, then your AI will just build trash on top of trash. Cuz it kind of learns from the patterns within your code base as well.

So, it's good to have a good foundation. And if you have tech debt on the random features on the top, or classes, or repeated model names, it doesn't actually matter that much, because it's easy to replace tech debts since it's so quick to write code now. So, you just want to make sure the foundation is good. So, I'm just going to say whether you're a student, a founder, business owner, creator, or engineer, I guess a recommendation on what you should take out of this. a student, I would recommend trying to set up a workspace like this, such as Open Claude or Hermes, and playing with Codex in it. And try to make Codex understand the memory that is built in with Open Claude.

And through this process, you'll kind of understand how memory works within these agent workspaces, and that'll be very helpful for you long-term. And also, how to build some automations within this workspace, where you're using the manager-worker pattern. That way, you also understand context management within these agents. If you're a business owner or founder, entrepreneur, I would recommend setting up the knowledge graph. So, after you have your workspace set up, you're optimizing for speed here.

Maybe you don't set up Open Claude yet, just set up Codex first. If you had to set up one thing, I would recommend that to be Codex even over Claude, because everything I just said. Also, Codex has image generation that Claude doesn't. So, there's just so many bonuses you get out of having the Codex subscription over any of other harnesses. Just set up Codex, set up this main workspace you're working in, and have that agents.md file properly set up, and then build the knowledge graph through the wiki by using the Andre Caparti prompt.

That way, all of your clients, you have them as personas within your workspace, and can improve over time. And that would be very good for your clients, because it just means you're going to be able to deliver better value for your clients by knowing them better. If you're a creator, or you want to optimize your content workflow, I would suggest trying to build that content automation system, but it's very complicated, so I'll start with the research flow. And a lot of difficulties as a creator is, "Oh, what should I do today? What should I do tomorrow?" And by building a research process, you can start without a blank slate, right?

So, the research process is like you want it to be evidence-based. Learning the pattern between research, analysis, and action. So, a lot of the agent stuff is going to be this, right? So, you research some type of data where you scrape some type of data with your agent, and then you analyze this data, and then you perform an action. The action could be posting something or sending a message or trading a stock, any of this.

You're going to see this pattern everywhere when you're building agents or agentic workflows, when you're building automations. And again, I would recommend Codex. If you're an engineer, then I would recommend heavily using the cross-model review. That will make your review process a lot easier. Most of the engineers I know, they're bottlenecked on the review process.

They know how to use these harnesses to write code, but then the review process just takes forever or they're not really well done. And it's way better to have these models review it first instead of like merging in slop. And also making sure that what you're merging in, you should review heavily if it's a foundational change. And if you're able to determine it's more like a leaf node change, like a small tech debt, or something that doesn't affect the architecture, then it's way easier to just merge that in without doing a deep dive of the code. Lastly, I would just say whatever you're doing, make sure to not spend too much time on trying to make things perfect cuz it's not going to be perfect on the first try.

You should just work to have a long-term workspace and have your memory management built somewhat correctly. That way it learns from you and it improves over time. And remember that the important here is the business outcome, right? Whether you're a student, if your goal is learning, if your business, your goal is to earn more money or to better deliver value to your clients. If you're working as a software engineer in big tech, that is get your tasks done in time.

Whether it's that you're a software engineer in big tech and you're trying to get your tasks done correctly and picking the right projects. All of this, having this right setup can help you with. Remember what is the actual goal you're trying to achieve because experimenting, writing code, and all this stuff is a lot easier now. Like how we predicted almost 3 years ago now when I did the AI code editor startup, it's really up to you on finding the business outcomes where you should land impact whatever work you're focused on and using your setup to efficiently and quickly iterate so that you can understand if you're on the right path. Now again, if any of these parts you would like me to dive deeper on or how to set this up, let me know in the comments or DM me or whatever and I will pick some parts to focus on first to perform a deeper dive in.

I also livestream every Sunday on YouTube and on Twitch. On YouTube I'm Duke Pan Channel, on Twitch is twitch.tv/ryanpan. I stream for multiple hours where I have a client calls and answer questions from you guys to help with AI integrations, building startups, building software and anything like that. If you want to have a actual client, if you want to actually have more personalized help, I also have this private community here that I made recently because people were asking me for more personalized help. So feel free to join this.

I have weekly meetings here and I will discuss with you exactly what your issues are, what are your next step actions and how to get over any hump, anything regarding software, startups or content. I've been doing this for a while so I'm happy to help here. For example, I post my trading bot updates and also my meeting summaries. You can have questions here which I'll help answer. For example, this person needs help on distribution and I can help review his content and where he should post them and what he should focus on.

Some other people are building like educational platforms or just any type of projects. If you really want to take it to the next step and want personalized help, otherwise I post most of my videos here for free on my YouTube channel so you can go take a look on the channel. All right guys, I hope that was helpful. Leave a like, comment, subscribe and let me know what you want to see next. Peace.
