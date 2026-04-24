/**
 * Estimate reading time + word count for a markdown body.
 *
 * Pace: ~220 English words/minute + ~400 CJK chars/minute.
 * Slower than silent reading to reflect read-aloud use.
 */
export function readingStats(rawBody: string): { minutes: number; totalWords: number } {
	const stripped = rawBody
		.replace(/```[\s\S]*?```/g, ' ')
		.replace(/`[^`]*`/g, ' ')
		.replace(/!\[[^\]]*\]\([^)]*\)/g, ' ')
		.replace(/\[([^\]]*)\]\([^)]*\)/g, '$1')
		.replace(/[#>*_~\-]/g, ' ');
	const englishWords = (stripped.match(/[A-Za-z][A-Za-z'-]*/g) ?? []).length;
	const cjkChars = (stripped.match(/[\u4e00-\u9fff]/g) ?? []).length;
	const minutes = Math.max(1, Math.round(englishWords / 220 + cjkChars / 400));
	return { minutes, totalWords: englishWords + cjkChars };
}
