/**
 * Cloudflare Worker for Autonomous Signal Ingestion & Lead Pipeline
 * Runs on cron schedule (every 4 hours) to fetch new leads, signals, and alerts.
 */

export default {
  async scheduled(event, env, ctx) {
    ctx.waitUntil(handleScheduledTask(env));
  },
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    if (url.pathname === "/status") {
      return new Response(JSON.stringify({ status: "active", mode: "autonomous_signal_hunter" }), {
        headers: { "Content-Type": "application/json" }
      });
    }
    if (url.pathname === "/run-cycle") {
      ctx.waitUntil(handleScheduledTask(env));
      return new Response(JSON.stringify({ message: "Signal scan triggered in background" }), {
        headers: { "Content-Type": "application/json" }
      });
    }
    return new Response("Applied Work Autonomous Lead Hunter Worker is running.");
  }
};

async function handleScheduledTask(env) {
  console.log("Starting scheduled autonomous lead hunter cycle...");
  const timestamp = new Date().toISOString();
  
  // Scrapes public signal feeds (Reddit, HN, RSS)
  const feeds = [
    "https://hnrss.org/newest?q=GPU+cluster+OR+H100+OR+RLHF",
    "https://hnrss.org/newest?q=dataset+OR+bankruptcy+OR+liquidating"
  ];

  for (const feed of feeds) {
    try {
      const resp = await fetch(feed);
      if (resp.ok) {
        const text = await resp.text();
        console.log(`Fetched feed ${feed}, length: ${text.length}`);
      }
    } catch (e) {
      console.error(`Error fetching ${feed}:`, e);
    }
  }

  console.log(`Cycle finished at ${timestamp}`);
}
