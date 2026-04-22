# Reading Hub

一个为 Wayne 个人定制的 **英语「边读边学」站点**。把 YouTube 视频、网络文章、自己的草稿等任何源材料，统一变成可在手机上沉浸阅读的双语学习页面。

部署：GitHub Pages（`main` 分支自动构建）。

## 它在干什么

- **统一收口**：YouTube 字幕 / 网页文章 / 自己写的内容，全部转成 Astro content collection 里的 markdown post。
- **语块高亮**：每篇文章 frontmatter 里挑出最值得复用的英语表达（chunks / collocations / formulaic / sentence frames），正文里用黄色高亮标记，鼠标悬停或手机点击会弹出中文含义、类型徽章、使用说明。
- **底部语块面板**：文章末尾自动汇总这篇里学到的所有语块，方便回顾。
- **明暗模式**：跟随系统，也可手动切换。
- **响应式**：桌面阅读 + 手机随时翻看，都做了适配（tooltip 在手机上点击展开、封面自动裁掉黑边、viewport 铺满）。

## 内容是怎么进来的

走 `.github/skills/post-creator` 这个 skill：

1. 给 AI 一个 YouTube 链接 / 文章 URL / 一段文字 / 自己的草稿
2. AI 自动转成 read-aloud-friendly 的 markdown，写入 `src/content/posts/<slug>.md`，带完整 frontmatter
3. 接着调用 `.github/skills/english-chunks-miner` 从这篇 post 里挖出可复用的英语表达，patch 回 frontmatter 的 `chunks` 字段
4. 推送到 `main`，GitHub Actions 自动构建部署

详细规则见两个 skill 的 `SKILL.md`。

## 项目结构

```
reading-hub/
├── src/
│   ├── content/
│   │   ├── posts/                  # 所有文章 markdown 在这里
│   │   └── content.config.ts       # 文章 schema：title / date / tags / cover / source / chunks
│   ├── pages/
│   │   ├── index.astro             # 首页文章列表
│   │   └── posts/[slug].astro      # 文章详情页（含语块高亮 + tooltip + 底部面板）
│   ├── layouts/BaseLayout.astro
│   ├── components/ThemeToggle.astro
│   └── styles/global.css
├── public/                         # 静态资源
├── .github/
│   ├── skills/
│   │   ├── post-creator/           # 把任意源转成 post
│   │   ├── english-chunks-miner/   # 从 post 挖语块
│   │   └── youtube-clipper/        # 下载 / 转字幕 / 提取等脚本
│   └── workflows/deploy.yml        # GitHub Pages 自动部署
└── astro.config.mjs
```

## 本地开发

```bash
npm install
npm run dev      # http://localhost:4321
npm run build    # 产物在 ./dist
npm run preview  # 本地预览构建产物
```

## 写作流程

不要手写 frontmatter 和 chunks，让 skill 来做：

- **加新文章**：在 chat 里说 "把这个 YouTube 视频转成 reading-hub post" + 链接，让 `post-creator` skill 跑完整个流程
- **只补语块**：让 `english-chunks-miner` 直接读已存在的 post，patch 回 chunks 字段
- **手动微调**：构建前用 `npm run dev` 实时预览高亮和 tooltip 是否正确

## 关键技术点

- Astro 5 + content collections（zod schema 校验 frontmatter）
- 客户端 DOM walker 在文章正文里把 chunks 用 `<mark class="chunk-highlight">` 包起来
- Tooltip 是真实子元素 `.chunk-tooltip`，由 `:hover` + `.chunk-open` class 双触发，桌面 hover 和手机点击体验一致
- YouTube 缩略图用 `aspect-ratio: 2/1; object-fit: cover` 自动裁掉 TED / 横屏视频自带的黑边
# Astro Starter Kit: Minimal

```sh
npm create astro@latest -- --template minimal
```

> 🧑‍🚀 **Seasoned astronaut?** Delete this file. Have fun!

## 🚀 Project Structure

Inside of your Astro project, you'll see the following folders and files:

```text
/
├── public/
├── src/
│   └── pages/
│       └── index.astro
└── package.json
```

Astro looks for `.astro` or `.md` files in the `src/pages/` directory. Each page is exposed as a route based on its file name.

There's nothing special about `src/components/`, but that's where we like to put any Astro/React/Vue/Svelte/Preact components.

Any static assets, like images, can be placed in the `public/` directory.

## 🧞 Commands

All commands are run from the root of the project, from a terminal:

| Command                   | Action                                           |
| :------------------------ | :----------------------------------------------- |
| `npm install`             | Installs dependencies                            |
| `npm run dev`             | Starts local dev server at `localhost:4321`      |
| `npm run build`           | Build your production site to `./dist/`          |
| `npm run preview`         | Preview your build locally, before deploying     |
| `npm run astro ...`       | Run CLI commands like `astro add`, `astro check` |
| `npm run astro -- --help` | Get help using the Astro CLI                     |

## 👀 Want to learn more?

Feel free to check [our documentation](https://docs.astro.build) or jump into our [Discord server](https://astro.build/chat).
