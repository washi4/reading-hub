import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const posts = defineCollection({
	loader: glob({ base: './src/content/posts', pattern: '**/*.{md,mdx}' }),
	schema: z.object({
		title: z.string(),
		date: z.coerce.date().optional(),
		description: z.string().optional().default(''),
		tags: z.array(z.string()).default([]),
		// Allow arbitrary extra frontmatter fields
		source: z.string().optional(),
		cover: z.string().optional(),
		speaker: z.string().optional(),
		format: z.string().optional(),
		language: z.string().optional(),
		purpose: z.string().optional(),
		chunks: z
			.array(
				z.object({
					text: z.string(),
					type: z
						.enum(['chunk', 'collocation', 'formulaic', 'sentence-frame'])
						.optional(),
					meaning: z.string(),
					note: z.string().optional(),
				}),
			)
			.optional(),
	}),
});

export const collections = { posts };
