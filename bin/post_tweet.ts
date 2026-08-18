#!/usr/bin/env bun
// Post one text tweet through the existing x-agent client.
// Run with cwd = ~/.claude/x-agent so bun auto-loads its .env.
// Deliberately not going through x-agent/post.ts: that path requires an image
// on every post for the news feed, which these do not need.
const text = process.argv[2];
if (!text) {
  console.error("usage: bun post_tweet.ts <text> [--dry]");
  process.exit(2);
}
if (process.argv.includes("--dry")) {
  console.log(`DRY (${text.length} raw chars):\n${text}`);
  process.exit(0);
}
const { postTweet } = await import(`${process.env.HOME}/.claude/x-agent/lib/x.ts`);
const res = await postTweet(text);
console.log(`posted ${res.id}`);
