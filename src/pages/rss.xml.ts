import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';
import type { APIContext } from 'astro';

export async function GET(context: APIContext) {
	const posts = await getCollection('posts');
	const sorted = posts.sort((a, b) => {
		const da = a.data.date?.getTime() ?? 0;
		const db = b.data.date?.getTime() ?? 0;
		return db - da;
	});
	return rss({
		title: 'Reading Hub',
		description: '中英混合长文阅读站：YouTube 转录、技术长文、朗读笔记。',
		site: context.site ?? 'https://washi4.github.io/reading-hub',
		items: sorted.map((post) => ({
			title: post.data.title,
			pubDate: post.data.date ?? new Date(),
			description: post.data.description ?? '',
			link: `/posts/${post.id}/`,
			categories: post.data.tags,
		})),
		trailingSlash: true,
	});
}
