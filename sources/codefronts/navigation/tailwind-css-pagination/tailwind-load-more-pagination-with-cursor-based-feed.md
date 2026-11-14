---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-pagination/tailwind-load-more-pagination-with-cursor-based-feed/"
title: "Tailwind Load More Pagination with Cursor-Based Feed"
section: "navigation"
category: "tailwind-css-pagination"
category_name: "Tailwind CSS Pagination"
description: "A load-more feed built the way the API underneath works: cursor paging, so there is no page count and no “jump to 40” — just Load older below and a new…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Load More Pagination with Cursor-Based Feed
Source: https://codefronts.com/navigation/tailwind-css-pagination/tailwind-load-more-pagination-with-cursor-based-feed/

A load-more feed built the way the API underneath works: cursor paging, so there is no page count and no “jump to 40” — just Load older below and a new events pill above. The script only flips hidden, disabled and data-loading / data-end; utilities render the spinner, the end-of-log state and a starting: highlight that fades from each freshly loaded row.
## HTML
```html
<section class="tpg-13 w-full min-h-svh grid place-items-center bg-tpg13-bg bg-[radial-gradient(50%_40%_at_20%_15%,var(--color-tpg13-glow),transparent_70%),radial-gradient(45%_40%_at_85%_90%,var(--color-tpg13-glow2),transparent_70%)] px-5 py-14 font-tpg13-sans text-tpg13-ink antialiased" aria-label="Load more pagination with cursor-based feed demo">
  <div class="grid w-full max-w-[40rem] justify-items-center gap-8">
    <div class="grid w-full gap-6" id="tpg-13-feed">
      <header class="grid gap-2">
        <p class="flex items-center gap-2 text-xs font-medium tracking-[0.12em] uppercase text-tpg13-mut"><span aria-hidden="true" class="relative flex size-2"><span class="absolute inset-0 animate-ping rounded-full bg-tpg13-c2/60 motion-reduce:animate-none"></span><span class="relative size-2 rounded-full bg-tpg13-c2 shadow-tpg13-dot"></span></span>Event stream</p>
        <h2 class="text-[clamp(1.5rem,3.4vw,1.9rem)] font-semibold tracking-[-0.03em]">Audit log</h2>
        <p class="max-w-[32rem] text-sm leading-relaxed text-tpg13-mut text-pretty">Each request carries the id of the last row you saw, so events written while you read never shift the window &mdash; the classic failure of <span class="font-tpg13-mono text-[13px]">LIMIT</span> + <span class="font-tpg13-mono text-[13px]">OFFSET</span>.</p>
      </header>

      <div class="overflow-hidden rounded-2xl bg-tpg13-card shadow-tpg13-card ring-1 ring-tpg13-line">
        <div class="flex items-center justify-between gap-3 border-b border-tpg13-line py-2 ps-4 pe-2 sm:ps-5">
          <p class="min-w-0 truncate text-[13px] text-tpg13-mut"><span class="font-medium text-tpg13-ink">acme-web</span> &middot; production</p>
          <button type="button" data-newer class="group/new inline-flex min-h-11 flex-none cursor-pointer items-center gap-2 rounded-full bg-linear-to-r from-tpg13-a to-tpg13-b px-3.5 text-[13px] font-medium text-tpg13-on-acc shadow-tpg13-neon transition-[box-shadow,translate,filter] duration-300 ease-[cubic-bezier(.16,1,.3,1)] hover:-translate-y-px hover:shadow-tpg13-neon-hi hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg13-ring disabled:cursor-not-allowed disabled:hover:translate-y-0 data-end:cursor-default data-end:bg-none data-end:font-normal data-end:text-tpg13-mut data-end:shadow-none data-end:hover:brightness-100 motion-reduce:transition-none">
            <svg class="group-data-loading/new:hidden group-data-end/new:hidden" viewBox="0 0 16 16" width="13" height="13" aria-hidden="true"><path d="M8 13V3.5M3.5 8 8 3.5 12.5 8" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>
            <svg class="hidden animate-spin group-data-loading/new:block motion-reduce:animate-none" viewBox="0 0 16 16" width="13" height="13" aria-hidden="true"><circle cx="8" cy="8" r="6" fill="none" stroke="currentColor" stroke-opacity=".25" stroke-width="2"/><path d="M14 8a6 6 0 0 0-6-6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
            <span class="group-data-end/new:hidden">2 new events</span><span class="hidden group-data-end/new:inline">Up to date</span>
          </button>
        </div>
        <ol role="list" aria-label="Events, newest first" data-list>
          <li data-row="evt_8f2c" data-batch="new" hidden class="flex items-start gap-3.5 border-b border-tpg13-line px-4 py-3.5 transition-[background-color,opacity,translate] duration-700 ease-[cubic-bezier(.16,1,.3,1)] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tpg13-ring sm:px-5 starting:bg-tpg13-c1/14 starting:-translate-y-1.5 starting:opacity-0 motion-reduce:transition-none">
            <span aria-hidden="true" class="mt-1.5 size-2 flex-none rounded-full bg-tpg13-ok ring-4 ring-tpg13-ok/15"></span>
            <div class="min-w-0 flex-1"><p class="font-tpg13-mono text-[13px] font-medium tracking-[-0.01em]">deploy.promoted</p><p class="mt-0.5 truncate text-[13px] text-tpg13-mut">web &middot; Alex Chen &middot; preview &rarr; production</p></div>
            <div class="flex flex-none flex-col items-end gap-1"><time class="text-xs text-tpg13-mut tabular-nums">12:46</time><code class="rounded-md bg-tpg13-c1/8 px-1.5 py-0.5 font-tpg13-mono text-[11px] text-tpg13-mut ring-1 ring-tpg13-c1/20">evt_8f2c</code></div>
          </li>
          <li data-row="evt_8f2b" data-batch="new" hidden class="flex items-start gap-3.5 border-b border-tpg13-line px-4 py-3.5 transition-[background-color,opacity,translate] duration-700 ease-[cubic-bezier(.16,1,.3,1)] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tpg13-ring sm:px-5 starting:bg-tpg13-c1/14 starting:-translate-y-1.5 starting:opacity-0 motion-reduce:transition-none">
            <span aria-hidden="true" class="mt-1.5 size-2 flex-none rounded-full bg-tpg13-info ring-4 ring-tpg13-info/15"></span>
            <div class="min-w-0 flex-1"><p class="font-tpg13-mono text-[13px] font-medium tracking-[-0.01em]">alert.resolved</p><p class="mt-0.5 truncate text-[13px] text-tpg13-mut">api &middot; system &middot; p95 latency back under 300 ms</p></div>
            <div class="flex flex-none flex-col items-end gap-1"><time class="text-xs text-tpg13-mut tabular-nums">12:44</time><code class="rounded-md bg-tpg13-c1/8 px-1.5 py-0.5 font-tpg13-mono text-[11px] text-tpg13-mut ring-1 ring-tpg13-c1/20">evt_8f2b</code></div>
          </li>
          <li data-row="evt_8f2a" class="flex items-start gap-3.5 border-b border-tpg13-line px-4 py-3.5 transition-[background-color,opacity,translate] duration-700 ease-[cubic-bezier(.16,1,.3,1)] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tpg13-ring sm:px-5 motion-reduce:transition-none">
            <span aria-hidden="true" class="mt-1.5 size-2 flex-none rounded-full bg-tpg13-ok ring-4 ring-tpg13-ok/15"></span>
            <div class="min-w-0 flex-1"><p class="font-tpg13-mono text-[13px] font-medium tracking-[-0.01em]">deploy.succeeded</p><p class="mt-0.5 truncate text-[13px] text-tpg13-mut">web &middot; Alex Chen &middot; build 4f1c2e</p></div>
            <div class="flex flex-none flex-col items-end gap-1"><time class="text-xs text-tpg13-mut tabular-nums">12:41</time><code class="rounded-md bg-tpg13-c1/8 px-1.5 py-0.5 font-tpg13-mono text-[11px] text-tpg13-mut ring-1 ring-tpg13-c1/20">evt_8f2a</code></div>
          </li>
          <li data-row="evt_8f29" class="flex items-start gap-3.5 border-b border-tpg13-line px-4 py-3.5 transition-[background-color,opacity,translate] duration-700 ease-[cubic-bezier(.16,1,.3,1)] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tpg13-ring sm:px-5 motion-reduce:transition-none">
            <span aria-hidden="true" class="mt-1.5 size-2 flex-none rounded-full bg-tpg13-info ring-4 ring-tpg13-info/15"></span>
            <div class="min-w-0 flex-1"><p class="font-tpg13-mono text-[13px] font-medium tracking-[-0.01em]">index.rebuilt</p><p class="mt-0.5 truncate text-[13px] text-tpg13-mut">search &middot; system &middot; 18,204 documents</p></div>
            <div class="flex flex-none flex-col items-end gap-1"><time class="text-xs text-tpg13-mut tabular-nums">12:38</time><code class="rounded-md bg-tpg13-c1/8 px-1.5 py-0.5 font-tpg13-mono text-[11px] text-tpg13-mut ring-1 ring-tpg13-c1/20">evt_8f29</code></div>
          </li>
          <li data-row="evt_8f28" class="flex items-start gap-3.5 border-b border-tpg13-line px-4 py-3.5 transition-[background-color,opacity,translate] duration-700 ease-[cubic-bezier(.16,1,.3,1)] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tpg13-ring sm:px-5 motion-reduce:transition-none">
            <span aria-hidden="true" class="mt-1.5 size-2 flex-none rounded-full bg-tpg13-warn ring-4 ring-tpg13-warn/15"></span>
            <div class="min-w-0 flex-1"><p class="font-tpg13-mono text-[13px] font-medium tracking-[-0.01em]">key.rotated</p><p class="mt-0.5 truncate text-[13px] text-tpg13-mut">auth &middot; Priya Sharma &middot; stripe-live</p></div>
            <div class="flex flex-none flex-col items-end gap-1"><time class="text-xs text-tpg13-mut tabular-nums">12:30</time><code class="rounded-md bg-tpg13-c1/8 px-1.5 py-0.5 font-tpg13-mono text-[11px] text-tpg13-mut ring-1 ring-tpg13-c1/20">evt_8f28</code></div>
          </li>
          <li data-row="evt_8f27" data-batch="1" hidden class="flex items-start gap-3.5 border-b border-tpg13-line px-4 py-3.5 transition-[background-color,opacity,translate] duration-700 ease-[cubic-bezier(.16,1,.3,1)] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tpg13-ring sm:px-5 starting:bg-tpg13-c1/14 starting:-translate-y-1.5 starting:opacity-0 motion-reduce:transition-none">
            <span aria-hidden="true" class="mt-1.5 size-2 flex-none rounded-full bg-tpg13-vio ring-4 ring-tpg13-vio/15"></span>
            <div class="min-w-0 flex-1"><p class="font-tpg13-mono text-[13px] font-medium tracking-[-0.01em]">webhook.retried</p><p class="mt-0.5 truncate text-[13px] text-tpg13-mut">billing &middot; system &middot; attempt 2 of 5</p></div>
            <div class="flex flex-none flex-col items-end gap-1"><time class="text-xs text-tpg13-mut tabular-nums">12:12</time><code class="rounded-md bg-tpg13-c1/8 px-1.5 py-0.5 font-tpg13-mono text-[11px] text-tpg13-mut ring-1 ring-tpg13-c1/20">evt_8f27</code></div>
          </li>
          <li data-row="evt_8f26" data-batch="1" hidden class="flex items-start gap-3.5 border-b border-tpg13-line px-4 py-3.5 transition-[background-color,opacity,translate] duration-700 ease-[cubic-bezier(.16,1,.3,1)] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tpg13-ring sm:px-5 starting:bg-tpg13-c1/14 starting:-translate-y-1.5 starting:opacity-0 motion-reduce:transition-none">
            <span aria-hidden="true" class="mt-1.5 size-2 flex-none rounded-full bg-tpg13-vio ring-4 ring-tpg13-vio/15"></span>
            <div class="min-w-0 flex-1"><p class="font-tpg13-mono text-[13px] font-medium tracking-[-0.01em]">plan.upgraded</p><p class="mt-0.5 truncate text-[13px] text-tpg13-mut">billing &middot; Jordan Lee &middot; Team &rarr; Scale</p></div>
            <div class="flex flex-none flex-col items-end gap-1"><time class="text-xs text-tpg13-mut tabular-nums">11:58</time><code class="rounded-md bg-tpg13-c1/8 px-1.5 py-0.5 font-tpg13-mono text-[11px] text-tpg13-mut ring-1 ring-tpg13-c1/20">evt_8f26</code></div>
          </li>
          <li data-row="evt_8f25" data-batch="1" hidden class="flex items-start gap-3.5 border-b border-tpg13-line px-4 py-3.5 transition-[background-color,opacity,translate] duration-700 ease-[cubic-bezier(.16,1,.3,1)] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tpg13-ring sm:px-5 starting:bg-tpg13-c1/14 starting:-translate-y-1.5 starting:opacity-0 motion-reduce:transition-none">
            <span aria-hidden="true" class="mt-1.5 size-2 flex-none rounded-full bg-tpg13-info ring-4 ring-tpg13-info/15"></span>
            <div class="min-w-0 flex-1"><p class="font-tpg13-mono text-[13px] font-medium tracking-[-0.01em]">seat.invited</p><p class="mt-0.5 truncate text-[13px] text-tpg13-mut">team &middot; Sam Rivera &middot; [email protected]</p></div>
            <div class="flex flex-none flex-col items-end gap-1"><time class="text-xs text-tpg13-mut tabular-nums">11:47</time><code class="rounded-md bg-tpg13-c1/8 px-1.5 py-0.5 font-tpg13-mono text-[11px] text-tpg13-mut ring-1 ring-tpg13-c1/20">evt_8f25</code></div>
          </li>
          <li data-row="evt_8f24" data-batch="2" hidden class="flex items-start gap-3.5 border-b border-tpg13-line px-4 py-3.5 transition-[background-color,opacity,translate] duration-700 ease-[cubic-bezier(.16,1,.3,1)] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tpg13-ring sm:px-5 starting:bg-tpg13-c1/14 starting:-translate-y-1.5 starting:opacity-0 motion-reduce:transition-none">
            <span aria-hidden="true" class="mt-1.5 size-2 flex-none rounded-full bg-tpg13-info ring-4 ring-tpg13-info/15"></span>
            <div class="min-w-0 flex-1"><p class="font-tpg13-mono text-[13px] font-medium tracking-[-0.01em]">export.finished</p><p class="mt-0.5 truncate text-[13px] text-tpg13-mut">reports &middot; Priya Sharma &middot; 2.4 MB CSV</p></div>
            <div class="flex flex-none flex-col items-end gap-1"><time class="text-xs text-tpg13-mut tabular-nums">11:20</time><code class="rounded-md bg-tpg13-c1/8 px-1.5 py-0.5 font-tpg13-mono text-[11px] text-tpg13-mut ring-1 ring-tpg13-c1/20">evt_8f24</code></div>
          </li>
          <li data-row="evt_8f23" data-batch="2" hidden class="flex items-start gap-3.5 border-b border-tpg13-line px-4 py-3.5 transition-[background-color,opacity,translate] duration-700 ease-[cubic-bezier(.16,1,.3,1)] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tpg13-ring sm:px-5 starting:bg-tpg13-c1/14 starting:-translate-y-1.5 starting:opacity-0 motion-reduce:transition-none">
            <span aria-hidden="true" class="mt-1.5 size-2 flex-none rounded-full bg-tpg13-warn ring-4 ring-tpg13-warn/15"></span>
            <div class="min-w-0 flex-1"><p class="font-tpg13-mono text-[13px] font-medium tracking-[-0.01em]">rule.disabled</p><p class="mt-0.5 truncate text-[13px] text-tpg13-mut">alerts &middot; Alex Chen &middot; disk-usage-80</p></div>
            <div class="flex flex-none flex-col items-end gap-1"><time class="text-xs text-tpg13-mut tabular-nums">11:04</time><code class="rounded-md bg-tpg13-c1/8 px-1.5 py-0.5 font-tpg13-mono text-[11px] text-tpg13-mut ring-1 ring-tpg13-c1/20">evt_8f23</code></div>
          </li>
          <li data-row="evt_8f22" data-batch="2" hidden class="flex items-start gap-3.5 border-b border-tpg13-line px-4 py-3.5 transition-[background-color,opacity,translate] duration-700 ease-[cubic-bezier(.16,1,.3,1)] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tpg13-ring sm:px-5 starting:bg-tpg13-c1/14 starting:-translate-y-1.5 starting:opacity-0 motion-reduce:transition-none">
            <span aria-hidden="true" class="mt-1.5 size-2 flex-none rounded-full bg-tpg13-warn ring-4 ring-tpg13-warn/15"></span>
            <div class="min-w-0 flex-1"><p class="font-tpg13-mono text-[13px] font-medium tracking-[-0.01em]">login.blocked</p><p class="mt-0.5 truncate text-[13px] text-tpg13-mut">auth &middot; system &middot; 6 failed attempts</p></div>
            <div class="flex flex-none flex-col items-end gap-1"><time class="text-xs text-tpg13-mut tabular-nums">10:52</time><code class="rounded-md bg-tpg13-c1/8 px-1.5 py-0.5 font-tpg13-mono text-[11px] text-tpg13-mut ring-1 ring-tpg13-c1/20">evt_8f22</code></div>
          </li>
          <li data-row="evt_8f21" data-batch="3" hidden class="flex items-start gap-3.5 border-b border-tpg13-line px-4 py-3.5 transition-[background-color,opacity,translate] duration-700 ease-[cubic-bezier(.16,1,.3,1)] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tpg13-ring sm:px-5 starting:bg-tpg13-c1/14 starting:-translate-y-1.5 starting:opacity-0 motion-reduce:transition-none">
            <span aria-hidden="true" class="mt-1.5 size-2 flex-none rounded-full bg-tpg13-ok ring-4 ring-tpg13-ok/15"></span>
            <div class="min-w-0 flex-1"><p class="font-tpg13-mono text-[13px] font-medium tracking-[-0.01em]">backup.completed</p><p class="mt-0.5 truncate text-[13px] text-tpg13-mut">db &middot; system &middot; 41 GB snapshot</p></div>
            <div class="flex flex-none flex-col items-end gap-1"><time class="text-xs text-tpg13-mut tabular-nums">10:30</time><code class="rounded-md bg-tpg13-c1/8 px-1.5 py-0.5 font-tpg13-mono text-[11px] text-tpg13-mut ring-1 ring-tpg13-c1/20">evt_8f21</code></div>
          </li>
          <li data-row="evt_8f20" data-batch="3" hidden class="flex items-start gap-3.5 border-b border-tpg13-line px-4 py-3.5 transition-[background-color,opacity,translate] duration-700 ease-[cubic-bezier(.16,1,.3,1)] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tpg13-ring sm:px-5 starting:bg-tpg13-c1/14 starting:-translate-y-1.5 starting:opacity-0 motion-reduce:transition-none">
            <span aria-hidden="true" class="mt-1.5 size-2 flex-none rounded-full bg-tpg13-warn ring-4 ring-tpg13-warn/15"></span>
            <div class="min-w-0 flex-1"><p class="font-tpg13-mono text-[13px] font-medium tracking-[-0.01em]">token.revoked</p><p class="mt-0.5 truncate text-[13px] text-tpg13-mut">auth &middot; Jordan Lee &middot; ci-runner-03</p></div>
            <div class="flex flex-none flex-col items-end gap-1"><time class="text-xs text-tpg13-mut tabular-nums">10:05</time><code class="rounded-md bg-tpg13-c1/8 px-1.5 py-0.5 font-tpg13-mono text-[11px] text-tpg13-mut ring-1 ring-tpg13-c1/20">evt_8f20</code></div>
          </li>
          <li data-row="evt_8f1f" data-batch="3" hidden class="flex items-start gap-3.5 border-b border-tpg13-line px-4 py-3.5 transition-[background-color,opacity,translate] duration-700 ease-[cubic-bezier(.16,1,.3,1)] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tpg13-ring sm:px-5 starting:bg-tpg13-c1/14 starting:-translate-y-1.5 starting:opacity-0 motion-reduce:transition-none">
            <span aria-hidden="true" class="mt-1.5 size-2 flex-none rounded-full bg-tpg13-ok ring-4 ring-tpg13-ok/15"></span>
            <div class="min-w-0 flex-1"><p class="font-tpg13-mono text-[13px] font-medium tracking-[-0.01em]">deploy.rolled_back</p><p class="mt-0.5 truncate text-[13px] text-tpg13-mut">web &middot; Sam Rivera &middot; build 9a07b1</p></div>
            <div class="flex flex-none flex-col items-end gap-1"><time class="text-xs text-tpg13-mut tabular-nums">09:48</time><code class="rounded-md bg-tpg13-c1/8 px-1.5 py-0.5 font-tpg13-mono text-[11px] text-tpg13-mut ring-1 ring-tpg13-c1/20">evt_8f1f</code></div>
          </li>
        </ol>
        <div class="p-2">
          <button type="button" data-older class="group/more flex min-h-11 w-full cursor-pointer items-center justify-center gap-2 rounded-xl border border-transparent text-[13px] font-medium text-tpg13-ink transition-[background-color,border-color,box-shadow] duration-300 ease-[cubic-bezier(.16,1,.3,1)] hover:border-tpg13-c1/30 hover:bg-tpg13-c1/8 hover:shadow-tpg13-neon-soft focus-visible:outline-2 focus-visible:outline-offset-0 focus-visible:outline-tpg13-ring disabled:cursor-not-allowed disabled:hover:shadow-none data-loading:animate-tpg13-orbit data-loading:[background:linear-gradient(var(--color-tpg13-card),var(--color-tpg13-card))_padding-box,conic-gradient(from_var(--tpg13-angle),var(--color-tpg13-c1),var(--color-tpg13-c2),transparent_45%,transparent_70%,var(--color-tpg13-c1))_border-box] data-end:cursor-default data-end:border-transparent data-end:bg-transparent data-end:text-tpg13-mut data-end:shadow-none motion-reduce:data-loading:animate-none">
            <span class="inline-flex items-center gap-2 group-data-loading/more:hidden group-data-end/more:hidden"><span class="bg-linear-to-r from-tpg13-a to-tpg13-b bg-clip-text font-semibold text-transparent">Load older events</span><svg class="text-tpg13-b" viewBox="0 0 16 16" width="13" height="13" aria-hidden="true"><path d="M8 3v9.5M3.5 8 8 12.5 12.5 8" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            <span class="hidden items-center gap-2 text-tpg13-mut group-data-loading/more:inline-flex"><svg class="animate-spin text-tpg13-c1 motion-reduce:animate-none" viewBox="0 0 16 16" width="14" height="14" aria-hidden="true"><circle cx="8" cy="8" r="6" fill="none" stroke="currentColor" stroke-opacity=".25" stroke-width="2"/><path d="M14 8a6 6 0 0 0-6-6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>Loading&hellip;</span>
            <span class="hidden group-data-end/more:inline">You&rsquo;ve reached the start of the log</span>
          </button>
        </div>
      </div>

      <p data-status role="status" aria-live="polite" class="text-center font-tpg13-mono text-xs text-tpg13-mut tabular-nums">before=evt_8f2a &middot; after=evt_8f28 &middot; limit=3</p>
    </div>
    <p aria-hidden="true" class="rounded-full bg-tpg13-card px-3.5 py-2 font-tpg13-mono text-[11.5px] text-tpg13-mut ring-1 ring-tpg13-line">group-data-loading/more: · starting:</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpg13-bg: #f7f4fe;
  --color-tpg13-bg: oklch(0.972 0.014 300);
  --color-tpg13-glow: #ddd0fdb3;
  --color-tpg13-glow: oklch(0.882 0.063 298 / 0.70);
  --color-tpg13-glow2: #fbcfe899;
  --color-tpg13-glow2: oklch(0.899 0.059 343 / 0.60);
  --color-tpg13-card: #fdfbff;
  --color-tpg13-card: oklch(0.991 0.006 308);
  --color-tpg13-ink: #1d1430;
  --color-tpg13-ink: oklch(0.219 0.054 297);
  --color-tpg13-mut: #5f5578;
  --color-tpg13-mut: oklch(0.473 0.057 297);
  --color-tpg13-line: #e9e2f7;
  --color-tpg13-line: oklch(0.925 0.029 301);
  --color-tpg13-c1: #8b5cf6;
  --color-tpg13-c1: oklch(0.606 0.219 293);
  --color-tpg13-c2: #ec4899;
  --color-tpg13-c2: oklch(0.656 0.212 354);
  --color-tpg13-a: #7c3aed;
  --color-tpg13-a: oklch(0.541 0.247 293);
  --color-tpg13-b: #be185d;
  --color-tpg13-b: oklch(0.525 0.199 4);
  --color-tpg13-on-acc: #ffffff;
  --color-tpg13-on-acc: oklch(1.000 0.000 0);
  --color-tpg13-ok: #0d9488;
  --color-tpg13-ok: oklch(0.600 0.104 185);
  --color-tpg13-info: #8b5cf6;
  --color-tpg13-info: oklch(0.606 0.219 293);
  --color-tpg13-warn: #f59e0b;
  --color-tpg13-warn: oklch(0.769 0.165 70);
  --color-tpg13-vio: #ec4899;
  --color-tpg13-vio: oklch(0.656 0.212 354);
  --color-tpg13-ring: #7c3aed;
  --color-tpg13-ring: oklch(0.541 0.247 293);
  --font-tpg13-sans: 'Geist', system-ui, sans-serif;
  --font-tpg13-mono: 'Geist Mono', ui-monospace, monospace;
  --animate-tpg13-orbit: tpg13-orbit 1.1s linear infinite;

  @keyframes tpg13-orbit {
    to {
      --tpg13-angle: 360deg;
    }
  }
  --shadow-tpg13-card: 0 1px 2px oklch(0.35 0.15 295 / 0.06), 0 16px 40px -18px oklch(0.5 0.22 295 / 0.3);
  --shadow-tpg13-neon: inset 0 1px 0 oklch(1 0 0 / 0.25), 0 6px 18px -6px oklch(0.6 0.22 300 / 0.55);
  --shadow-tpg13-neon-hi: inset 0 1px 0 oklch(1 0 0 / 0.3), 0 10px 26px -6px oklch(0.62 0.24 330 / 0.6);
  --shadow-tpg13-neon-soft: 0 8px 22px -12px oklch(0.6 0.22 295 / 0.5);
  --shadow-tpg13-dot: 0 0 8px oklch(0.66 0.22 355 / 0.8);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tpg-13 {
  width: 100%;
  min-height: 100svh;
}
/* The conic loading ring rotates a registered angle; @property is an at-rule utilities cannot express. */

@property --tpg13-angle {
  syntax: "<angle>";
  inherits: false;
  initial-value: 0deg;
}
/* Dark theme: Nebula night — deep violet stage, neon glows; same tokens, re-pointed. */

@media (prefers-color-scheme: dark) {
  .tpg-13:not([data-theme="light"]) {
    --color-tpg13-bg: #0d0a1a;
    --color-tpg13-bg: oklch(0.158 0.033 291);
    --color-tpg13-glow: #4c1d9580;
    --color-tpg13-glow: oklch(0.380 0.178 294 / 0.50);
    --color-tpg13-glow2: #83184366;
    --color-tpg13-glow2: oklch(0.408 0.144 2 / 0.40);
    --color-tpg13-card: #151027;
    --color-tpg13-card: oklch(0.193 0.045 292);
    --color-tpg13-ink: #f1ecff;
    --color-tpg13-ink: oklch(0.953 0.026 298);
    --color-tpg13-mut: #a99fc8;
    --color-tpg13-mut: oklch(0.725 0.060 296);
    --color-tpg13-line: #2a2245;
    --color-tpg13-line: oklch(0.280 0.063 292);
    --color-tpg13-c1: #a78bfa;
    --color-tpg13-c1: oklch(0.709 0.159 294);
    --color-tpg13-c2: #f472b6;
    --color-tpg13-c2: oklch(0.725 0.175 350);
    --color-tpg13-a: #a78bfa;
    --color-tpg13-a: oklch(0.709 0.159 294);
    --color-tpg13-b: #f472b6;
    --color-tpg13-b: oklch(0.725 0.175 350);
    --color-tpg13-on-acc: #1a0b2e;
    --color-tpg13-on-acc: oklch(0.195 0.067 300);
    --color-tpg13-ok: #2dd4bf;
    --color-tpg13-ok: oklch(0.785 0.133 182);
    --color-tpg13-info: #a78bfa;
    --color-tpg13-info: oklch(0.709 0.159 294);
    --color-tpg13-warn: #fbbf24;
    --color-tpg13-warn: oklch(0.837 0.164 84);
    --color-tpg13-vio: #f472b6;
    --color-tpg13-vio: oklch(0.725 0.175 350);
    --color-tpg13-ring: #c4b5fd;
    --color-tpg13-ring: oklch(0.811 0.101 294);
    --shadow-tpg13-card: 0 0 0 1px oklch(0.7 0.15 295 / 0.08), 0 1px 0 oklch(1 0 0 / 0.05) inset, 0 24px 60px -24px oklch(0.45 0.22 295 / 0.55);
    --shadow-tpg13-neon: inset 0 1px 0 oklch(1 0 0 / 0.45), 0 0 0 1px oklch(0.72 0.16 300 / 0.35), 0 0 22px -2px oklch(0.7 0.2 320 / 0.6);
    --shadow-tpg13-neon-hi: inset 0 1px 0 oklch(1 0 0 / 0.5), 0 0 0 1px oklch(0.75 0.16 340 / 0.5), 0 0 32px 0 oklch(0.72 0.2 330 / 0.7);
    --shadow-tpg13-neon-soft: 0 0 24px -6px oklch(0.7 0.18 295 / 0.55);
    --shadow-tpg13-dot: 0 0 10px oklch(0.75 0.18 350 / 0.95);
  }
}

.tpg-13[data-theme="dark"] {
  --color-tpg13-bg: #0d0a1a;
  --color-tpg13-bg: oklch(0.158 0.033 291);
  --color-tpg13-glow: #4c1d9580;
  --color-tpg13-glow: oklch(0.380 0.178 294 / 0.50);
  --color-tpg13-glow2: #83184366;
  --color-tpg13-glow2: oklch(0.408 0.144 2 / 0.40);
  --color-tpg13-card: #151027;
  --color-tpg13-card: oklch(0.193 0.045 292);
  --color-tpg13-ink: #f1ecff;
  --color-tpg13-ink: oklch(0.953 0.026 298);
  --color-tpg13-mut: #a99fc8;
  --color-tpg13-mut: oklch(0.725 0.060 296);
  --color-tpg13-line: #2a2245;
  --color-tpg13-line: oklch(0.280 0.063 292);
  --color-tpg13-c1: #a78bfa;
  --color-tpg13-c1: oklch(0.709 0.159 294);
  --color-tpg13-c2: #f472b6;
  --color-tpg13-c2: oklch(0.725 0.175 350);
  --color-tpg13-a: #a78bfa;
  --color-tpg13-a: oklch(0.709 0.159 294);
  --color-tpg13-b: #f472b6;
  --color-tpg13-b: oklch(0.725 0.175 350);
  --color-tpg13-on-acc: #1a0b2e;
  --color-tpg13-on-acc: oklch(0.195 0.067 300);
  --color-tpg13-ok: #2dd4bf;
  --color-tpg13-ok: oklch(0.785 0.133 182);
  --color-tpg13-info: #a78bfa;
  --color-tpg13-info: oklch(0.709 0.159 294);
  --color-tpg13-warn: #fbbf24;
  --color-tpg13-warn: oklch(0.837 0.164 84);
  --color-tpg13-vio: #f472b6;
  --color-tpg13-vio: oklch(0.725 0.175 350);
  --color-tpg13-ring: #c4b5fd;
  --color-tpg13-ring: oklch(0.811 0.101 294);
  --shadow-tpg13-card: 0 0 0 1px oklch(0.7 0.15 295 / 0.08), 0 1px 0 oklch(1 0 0 / 0.05) inset, 0 24px 60px -24px oklch(0.45 0.22 295 / 0.55);
  --shadow-tpg13-neon: inset 0 1px 0 oklch(1 0 0 / 0.45), 0 0 0 1px oklch(0.72 0.16 300 / 0.35), 0 0 22px -2px oklch(0.7 0.2 320 / 0.6);
  --shadow-tpg13-neon-hi: inset 0 1px 0 oklch(1 0 0 / 0.5), 0 0 0 1px oklch(0.75 0.16 340 / 0.5), 0 0 32px 0 oklch(0.72 0.2 330 / 0.7);
  --shadow-tpg13-neon-soft: 0 0 24px -6px oklch(0.7 0.18 295 / 0.55);
  --shadow-tpg13-dot: 0 0 10px oklch(0.75 0.18 350 / 0.95);
}
```

## JavaScript
```js
(() => {
  const root = document.getElementById('tpg-13-feed');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const list = root.querySelector('[data-list]');
  const status = root.querySelector('[data-status]');
  const older = root.querySelector('[data-older]');
  const newer = root.querySelector('[data-newer]');
  const shown = () => [...list.querySelectorAll('[data-row]:not([hidden])')];
  const report = (msg) => {
    const v = shown();
    status.textContent = msg + 'before=' + v[0].dataset.row + ' · after=' + v[v.length - 1].dataset.row + ' · limit=3';
  };
  let batch = 1;
  const load = (btn, key, keyboard, done) => {
    btn.disabled = true;
    btn.setAttribute('data-loading', '');
    list.setAttribute('aria-busy', 'true');
    setTimeout(() => {
      const rows = [...list.querySelectorAll('[data-batch="' + key + '"]')];
      rows.forEach((r) => { r.hidden = false; });
      btn.removeAttribute('data-loading');
      list.removeAttribute('aria-busy');
      done();
      report('Loaded ' + rows.length + (key === 'new' ? ' newer' : ' older') + ' events. ');
      if (keyboard && rows[0]) { rows[0].setAttribute('tabindex', '-1'); rows[0].focus(); }
    }, 650);
  };
  older.addEventListener('click', (e) => {
    load(older, String(batch), e.detail === 0, () => {
      batch += 1;
      if (list.querySelector('[data-batch="' + batch + '"]')) older.disabled = false;
      else older.setAttribute('data-end', '');
    });
  });
  newer.addEventListener('click', (e) => load(newer, 'new', e.detail === 0, () => newer.setAttribute('data-end', '')));
})();
```
