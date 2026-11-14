---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-docs-layout-sticky-table-of-contents/"
title: "Tailwind Docs Layout with Sticky Table of Contents"
section: "layouts"
category: "tailwind-css-grid-layouts"
category_name: "Tailwind CSS Grid Layouts"
description: "A real API reference page: version pill, on-this-page rail that tracks the reader, code samples that scroll instead of shoving the layout around."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Docs Layout with Sticky Table of Contents
Source: https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-docs-layout-sticky-table-of-contents/

A real API reference page: version pill, on-this-page rail that tracks the reader, code samples that scroll instead of shoving the layout around. One missing declaration kills position: sticky in grid — here the cure sits two utilities from the cause.
## HTML
```html
<section class="tgx-02 w-full min-h-svh bg-tgx02-bg text-tgx02-ink font-tgx02-sans p-5">
  <div class="grid grid-cols-[minmax(200px,240px)_minmax(0,1fr)] max-sm:grid-cols-1 gap-6 h-[420px] overflow-y-auto overscroll-contain rounded-2xl border border-tgx02-edge bg-tgx02-panel p-5">
    <aside>
      <nav aria-label="On this page" class="sticky top-0 self-start max-sm:static flex flex-col gap-0.5 rounded-xl border border-tgx02-edge bg-tgx02-nav p-3">
        <div class="flex items-center justify-between gap-2 px-1 pb-2 mb-1 border-b border-tgx02-edge">
          <p class="text-[0.66rem] tracking-[0.14em] uppercase text-tgx02-dim">On this page</p>
          <span class="font-tgx02-mono text-[0.6rem] px-1.5 py-0.5 rounded bg-tgx02-limetint text-tgx02-lime">v3.2</span>
        </div>
        <a href="#tgx02-auth" aria-current="location" class="text-[0.84rem] no-underline rounded-lg px-2.5 min-h-9 flex items-center border-l-2 border-transparent text-tgx02-dim transition-colors hover:text-tgx02-ink hover:bg-tgx02-hover aria-[current=location]:text-tgx02-lime aria-[current=location]:border-l-tgx02-lime aria-[current=location]:bg-tgx02-limetint focus-visible:outline-2 focus-visible:outline-tgx02-lime focus-visible:outline-offset-2">Authentication</a>
        <a href="#tgx02-list" class="text-[0.84rem] no-underline rounded-lg px-2.5 min-h-9 flex items-center border-l-2 border-transparent text-tgx02-dim transition-colors hover:text-tgx02-ink hover:bg-tgx02-hover focus-visible:outline-2 focus-visible:outline-tgx02-lime focus-visible:outline-offset-2">List shipments</a>
        <a href="#tgx02-rate" class="text-[0.84rem] no-underline rounded-lg px-2.5 min-h-9 flex items-center border-l-2 border-transparent text-tgx02-dim transition-colors hover:text-tgx02-ink hover:bg-tgx02-hover focus-visible:outline-2 focus-visible:outline-tgx02-lime focus-visible:outline-offset-2">Rate limits</a>
        <a href="#tgx02-errors" class="text-[0.84rem] no-underline rounded-lg px-2.5 min-h-9 flex items-center border-l-2 border-transparent text-tgx02-dim transition-colors hover:text-tgx02-ink hover:bg-tgx02-hover focus-visible:outline-2 focus-visible:outline-tgx02-lime focus-visible:outline-offset-2">Error codes</a>
        <a href="#tgx02-webhooks" class="text-[0.84rem] no-underline rounded-lg px-2.5 min-h-9 flex items-center border-l-2 border-transparent text-tgx02-dim transition-colors hover:text-tgx02-ink hover:bg-tgx02-hover focus-visible:outline-2 focus-visible:outline-tgx02-lime focus-visible:outline-offset-2">Webhooks</a>
      </nav>
    </aside>
    <main class="flex flex-col gap-7 min-w-0">
      <header class="flex flex-col gap-2">
        <p class="font-tgx02-mono text-[0.68rem] text-tgx02-dim">Northwind Freight API</p>
        <h2 class="text-[1.35rem] font-semibold tracking-[-0.01em]">Shipments</h2>
        <p class="text-[0.88rem] leading-[1.65] text-tgx02-dim">Create, track and reconcile shipments. All endpoints are versioned and return JSON.</p>
      </header>
      <article id="tgx02-auth" class="scroll-mt-4 flex flex-col gap-2">
        <h3 class="text-[1rem] font-semibold text-tgx02-lime">Authentication</h3>
        <p class="text-[0.86rem] leading-[1.65] text-tgx02-dim">Send your secret key as a bearer token. Keys are environment-scoped; a test key never touches a live manifest.</p>
        <pre class="font-tgx02-mono text-[0.76rem] leading-[1.6] text-tgx02-code bg-tgx02-codebg border border-tgx02-edge rounded-lg p-3 overflow-x-auto"><code>curl https://api.northwind.dev/v3/shipments \
  -H "Authorization: Bearer nw_live_8fK2..." \
  -H "Northwind-Version: 2026-07-01"</code></pre>
      </article>
      <article id="tgx02-list" class="scroll-mt-4 flex flex-col gap-2">
        <h3 class="text-[1rem] font-semibold text-tgx02-lime">List shipments</h3>
        <p class="text-[0.86rem] leading-[1.65] text-tgx02-dim">Returns a cursor-paginated list, newest first. The content track is <code class="font-tgx02-mono text-tgx02-ink">minmax(0,1fr)</code>, so the sample above scrolls sideways instead of widening the page.</p>
      </article>
      <article id="tgx02-rate" class="scroll-mt-4 flex flex-col gap-2">
        <h3 class="text-[1rem] font-semibold text-tgx02-lime">Rate limits</h3>
        <p class="text-[0.86rem] leading-[1.65] text-tgx02-dim">1,000 requests per minute per key. Bursts are smoothed over ten seconds; exceeding the window returns <code class="font-tgx02-mono text-tgx02-ink">429</code> with a retry hint.</p>
      </article>
      <article id="tgx02-errors" class="scroll-mt-4 flex flex-col gap-2">
        <h3 class="text-[1rem] font-semibold text-tgx02-lime">Error codes</h3>
        <p class="text-[0.86rem] leading-[1.65] text-tgx02-dim">Every error carries a stable <code class="font-tgx02-mono text-tgx02-ink">type</code>, a human message, and the request id to quote at support.</p>
      </article>
      <article id="tgx02-webhooks" class="scroll-mt-4 flex flex-col gap-2">
        <h3 class="text-[1rem] font-semibold text-tgx02-lime">Webhooks</h3>
        <p class="text-[0.86rem] leading-[1.65] text-tgx02-dim">Subscribe to <code class="font-tgx02-mono text-tgx02-ink">shipment.delivered</code> and friends. Deliveries retry for 24 hours with exponential backoff.</p>
      </article>
    </main>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgx02-bg: #1b1d26;
  --color-tgx02-bg: oklch(0.2 0.02 265);
  --color-tgx02-panel: #21242f;
  --color-tgx02-panel: oklch(0.24 0.025 265);
  --color-tgx02-nav: #272b38;
  --color-tgx02-nav: oklch(0.28 0.03 265);
  --color-tgx02-hover: #2e3242;
  --color-tgx02-hover: oklch(0.32 0.03 265);
  --color-tgx02-codebg: #171923;
  --color-tgx02-codebg: oklch(0.18 0.02 265);
  --color-tgx02-code: #cfe3a8;
  --color-tgx02-code: oklch(0.88 0.08 125);
  --color-tgx02-edge: #363a4a;
  --color-tgx02-edge: oklch(0.36 0.03 265);
  --color-tgx02-ink: #e9eaf0;
  --color-tgx02-ink: oklch(0.93 0.01 260);
  --color-tgx02-dim: #a7abbb;
  --color-tgx02-dim: oklch(0.73 0.02 260);
  --color-tgx02-lime: #b6e84f;
  --color-tgx02-lime: oklch(0.85 0.19 130);
  --color-tgx02-limetint: #2c3826;
  --color-tgx02-limetint: oklch(0.32 0.05 130);
  --font-tgx02-sans: 'Inter Tight', system-ui, sans-serif;
  --font-tgx02-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tgx-02 {
  width: 100%;
  min-height: 100svh;
}
```
