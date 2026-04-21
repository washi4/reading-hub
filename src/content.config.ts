import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const posts = defineCollection({
	loader: glob({ base: './src/content/posts', pattern: '**/*.{md,mdx}' }),
	schema: z.object({
		title: z.string(),
		date: z.coerce.date(),
		description: z.string(),
		tags: z.array(z.string()).default([]),
	}),
});

export const collections = { posts };
