---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-responsive-card-grid-integrations-directory/"
title: "Tailwind Responsive Card Grid for an Integrations Directory"
section: "layouts"
category: "tailwind-css-grid-layouts"
category_name: "Tailwind CSS Grid Layouts"
description: "An integrations marketplace: six connectors with categories, install counts and status badges, laid out by one utility that goes 4-up to 1-up as the…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Responsive Card Grid for an Integrations Directory
Source: https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-responsive-card-grid-integrations-directory/

An integrations marketplace: six connectors with categories, install counts and status badges, laid out by one utility that goes 4-up to 1-up as the container narrows. No breakpoints anywhere in the file.
## HTML
```html
<section class="tgx-11 w-full min-h-svh bg-tgx11-bg font-tgx11-sans p-6">
  <header class="flex items-end justify-between gap-4 flex-wrap mb-5">
    <div class="flex flex-col gap-1">
      <p class="text-[0.68rem] tracking-[0.18em] uppercase text-tgx11-mut">Relay · Integrations</p>
      <h2 class="text-[1.4rem] font-semibold tracking-[-0.01em] text-tgx11-ink">Connect your stack</h2>
    </div>
    <div class="flex gap-2 text-[0.75rem]">
      <span class="px-3 py-1.5 rounded-full bg-tgx11-ink text-white font-medium">All 42</span>
      <span class="px-3 py-1.5 rounded-full bg-white border border-tgx11-edge text-tgx11-mut">Installed 6</span>
    </div>
  </header>
  <div class="grid grid-cols-[repeat(auto-fit,minmax(min(230px,100%),1fr))] gap-3.5">
    <article class="group flex flex-col gap-3 rounded-2xl bg-white border border-tgx11-edge p-4 shadow-[0_10px_24px_-20px_oklch(0.4_0.05_220/0.8)] transition duration-200 hover:-translate-y-1 hover:shadow-[0_18px_34px_-20px_oklch(0.4_0.06_220/0.9)] focus-within:-translate-y-1 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <div class="flex items-start justify-between gap-3">
        <span aria-hidden="true" class="size-10 grid place-items-center rounded-xl bg-tgx11-slackbg text-white font-semibold text-[0.95rem]">S</span>
        <span class="text-[0.64rem] font-medium px-2 py-1 rounded-full bg-tgx11-oktint text-tgx11-ok">Installed</span>
      </div>
      <div class="flex flex-col gap-1">
        <h3 class="text-[0.95rem] font-semibold text-tgx11-ink">Slack</h3>
        <p class="text-[0.8rem] leading-[1.55] text-tgx11-mut">Route incidents to a channel and acknowledge without leaving the thread.</p>
      </div>
      <div class="mt-auto flex items-center justify-between gap-2 pt-2 border-t border-tgx11-edge">
        <span class="text-[0.72rem] text-tgx11-mut tabular-nums">18.4k installs</span>
        <a href="#0" class="text-[0.78rem] font-semibold text-tgx11-accent no-underline min-h-11 inline-flex items-center hover:underline underline-offset-4 focus-visible:outline-2 focus-visible:outline-tgx11-accent focus-visible:outline-offset-2 rounded">Configure</a>
      </div>
    </article>
    <article class="group flex flex-col gap-3 rounded-2xl bg-white border border-tgx11-edge p-4 shadow-[0_10px_24px_-20px_oklch(0.4_0.05_220/0.8)] transition duration-200 hover:-translate-y-1 hover:shadow-[0_18px_34px_-20px_oklch(0.4_0.06_220/0.9)] focus-within:-translate-y-1 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <div class="flex items-start justify-between gap-3">
        <span aria-hidden="true" class="size-10 grid place-items-center rounded-xl bg-tgx11-ghbg text-white font-semibold text-[0.95rem]">GH</span>
        <span class="text-[0.64rem] font-medium px-2 py-1 rounded-full bg-tgx11-oktint text-tgx11-ok">Installed</span>
      </div>
      <div class="flex flex-col gap-1">
        <h3 class="text-[0.95rem] font-semibold text-tgx11-ink">GitHub</h3>
        <p class="text-[0.8rem] leading-[1.55] text-tgx11-mut">Link deploys to commits and close incidents from a pull request.</p>
      </div>
      <div class="mt-auto flex items-center justify-between gap-2 pt-2 border-t border-tgx11-edge">
        <span class="text-[0.72rem] text-tgx11-mut tabular-nums">31.2k installs</span>
        <a href="#0" class="text-[0.78rem] font-semibold text-tgx11-accent no-underline min-h-11 inline-flex items-center hover:underline underline-offset-4 focus-visible:outline-2 focus-visible:outline-tgx11-accent focus-visible:outline-offset-2 rounded">Configure</a>
      </div>
    </article>
    <article class="group flex flex-col gap-3 rounded-2xl bg-white border border-tgx11-edge p-4 shadow-[0_10px_24px_-20px_oklch(0.4_0.05_220/0.8)] transition duration-200 hover:-translate-y-1 hover:shadow-[0_18px_34px_-20px_oklch(0.4_0.06_220/0.9)] focus-within:-translate-y-1 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <div class="flex items-start justify-between gap-3">
        <span aria-hidden="true" class="size-10 grid place-items-center rounded-xl bg-tgx11-pdbg text-white font-semibold text-[0.95rem]">PD</span>
        <span class="text-[0.64rem] font-medium px-2 py-1 rounded-full bg-tgx11-warntint text-tgx11-warn">Needs auth</span>
      </div>
      <div class="flex flex-col gap-1">
        <h3 class="text-[0.95rem] font-semibold text-tgx11-ink">PagerDuty</h3>
        <p class="text-[0.8rem] leading-[1.55] text-tgx11-mut">Escalate after two missed acknowledgements, on your existing rota.</p>
      </div>
      <div class="mt-auto flex items-center justify-between gap-2 pt-2 border-t border-tgx11-edge">
        <span class="text-[0.72rem] text-tgx11-mut tabular-nums">9.8k installs</span>
        <a href="#0" class="text-[0.78rem] font-semibold text-tgx11-accent no-underline min-h-11 inline-flex items-center hover:underline underline-offset-4 focus-visible:outline-2 focus-visible:outline-tgx11-accent focus-visible:outline-offset-2 rounded">Reconnect</a>
      </div>
    </article>
    <article class="group flex flex-col gap-3 rounded-2xl bg-white border border-tgx11-edge p-4 shadow-[0_10px_24px_-20px_oklch(0.4_0.05_220/0.8)] transition duration-200 hover:-translate-y-1 hover:shadow-[0_18px_34px_-20px_oklch(0.4_0.06_220/0.9)] focus-within:-translate-y-1 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <div class="flex items-start justify-between gap-3">
        <span aria-hidden="true" class="size-10 grid place-items-center rounded-xl bg-tgx11-lnbg text-white font-semibold text-[0.95rem]">L</span>
        <span class="text-[0.64rem] font-medium px-2 py-1 rounded-full bg-tgx11-neutraltint text-tgx11-mut">Available</span>
      </div>
      <div class="flex flex-col gap-1">
        <h3 class="text-[0.95rem] font-semibold text-tgx11-ink">Linear</h3>
        <p class="text-[0.8rem] leading-[1.55] text-tgx11-mut">Open an issue from any alert, with the timeline attached automatically.</p>
      </div>
      <div class="mt-auto flex items-center justify-between gap-2 pt-2 border-t border-tgx11-edge">
        <span class="text-[0.72rem] text-tgx11-mut tabular-nums">12.1k installs</span>
        <a href="#0" class="text-[0.78rem] font-semibold text-tgx11-accent no-underline min-h-11 inline-flex items-center hover:underline underline-offset-4 focus-visible:outline-2 focus-visible:outline-tgx11-accent focus-visible:outline-offset-2 rounded">Install</a>
      </div>
    </article>
    <article class="group flex flex-col gap-3 rounded-2xl bg-white border border-tgx11-edge p-4 shadow-[0_10px_24px_-20px_oklch(0.4_0.05_220/0.8)] transition duration-200 hover:-translate-y-1 hover:shadow-[0_18px_34px_-20px_oklch(0.4_0.06_220/0.9)] focus-within:-translate-y-1 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <div class="flex items-start justify-between gap-3">
        <span aria-hidden="true" class="size-10 grid place-items-center rounded-xl bg-tgx11-dtbg text-white font-semibold text-[0.95rem]">DT</span>
        <span class="text-[0.64rem] font-medium px-2 py-1 rounded-full bg-tgx11-neutraltint text-tgx11-mut">Available</span>
      </div>
      <div class="flex flex-col gap-1">
        <h3 class="text-[0.95rem] font-semibold text-tgx11-ink">Datadog</h3>
        <p class="text-[0.8rem] leading-[1.55] text-tgx11-mut">Pull monitor state into Relay boards and keep one source of truth.</p>
      </div>
      <div class="mt-auto flex items-center justify-between gap-2 pt-2 border-t border-tgx11-edge">
        <span class="text-[0.72rem] text-tgx11-mut tabular-nums">7.4k installs</span>
        <a href="#0" class="text-[0.78rem] font-semibold text-tgx11-accent no-underline min-h-11 inline-flex items-center hover:underline underline-offset-4 focus-visible:outline-2 focus-visible:outline-tgx11-accent focus-visible:outline-offset-2 rounded">Install</a>
      </div>
    </article>
    <article class="group flex flex-col gap-3 rounded-2xl bg-white border border-tgx11-edge p-4 shadow-[0_10px_24px_-20px_oklch(0.4_0.05_220/0.8)] transition duration-200 hover:-translate-y-1 hover:shadow-[0_18px_34px_-20px_oklch(0.4_0.06_220/0.9)] focus-within:-translate-y-1 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <div class="flex items-start justify-between gap-3">
        <span aria-hidden="true" class="size-10 grid place-items-center rounded-xl bg-tgx11-nbbg text-white font-semibold text-[0.95rem]">N</span>
        <span class="text-[0.64rem] font-medium px-2 py-1 rounded-full bg-tgx11-neutraltint text-tgx11-mut">Available</span>
      </div>
      <div class="flex flex-col gap-1">
        <h3 class="text-[0.95rem] font-semibold text-tgx11-ink">Notion</h3>
        <p class="text-[0.8rem] leading-[1.55] text-tgx11-mut">Write post-incident reviews straight into your team's database.</p>
      </div>
      <div class="mt-auto flex items-center justify-between gap-2 pt-2 border-t border-tgx11-edge">
        <span class="text-[0.72rem] text-tgx11-mut tabular-nums">5.6k installs</span>
        <a href="#0" class="text-[0.78rem] font-semibold text-tgx11-accent no-underline min-h-11 inline-flex items-center hover:underline underline-offset-4 focus-visible:outline-2 focus-visible:outline-tgx11-accent focus-visible:outline-offset-2 rounded">Install</a>
      </div>
    </article>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgx11-bg: #eef3f5;
  --color-tgx11-bg: oklch(0.95 0.008 215);
  --color-tgx11-edge: #d5e0e5;
  --color-tgx11-edge: oklch(0.89 0.012 215);
  --color-tgx11-ink: #1d2a30;
  --color-tgx11-ink: oklch(0.26 0.02 215);
  --color-tgx11-mut: #55666e;
  --color-tgx11-mut: oklch(0.48 0.02 215);
  --color-tgx11-accent: #0f6f8c;
  --color-tgx11-accent: oklch(0.47 0.1 220);
  --color-tgx11-ok: #16704f;
  --color-tgx11-ok: oklch(0.46 0.1 160);
  --color-tgx11-oktint: #dff0e8;
  --color-tgx11-oktint: oklch(0.93 0.03 160);
  --color-tgx11-warn: #8a5410;
  --color-tgx11-warn: oklch(0.48 0.1 70);
  --color-tgx11-warntint: #f6ebd8;
  --color-tgx11-warntint: oklch(0.93 0.035 80);
  --color-tgx11-neutraltint: #e7edf0;
  --color-tgx11-neutraltint: oklch(0.93 0.008 215);
  --color-tgx11-slackbg: #4a154b;
  --color-tgx11-slackbg: oklch(0.32 0.12 320);
  --color-tgx11-ghbg: #24292f;
  --color-tgx11-ghbg: oklch(0.28 0.01 250);
  --color-tgx11-pdbg: #1a6f45;
  --color-tgx11-pdbg: oklch(0.45 0.11 155);
  --color-tgx11-lnbg: #3f4bb8;
  --color-tgx11-lnbg: oklch(0.45 0.16 275);
  --color-tgx11-dtbg: #5a3aa8;
  --color-tgx11-dtbg: oklch(0.42 0.16 295);
  --color-tgx11-nbbg: #33383d;
  --color-tgx11-nbbg: oklch(0.34 0.008 250);
  --font-tgx11-sans: 'Inter Tight', system-ui, sans-serif;
}

.tgx-11 {
  width: 100%;
  min-height: 100svh;
}
```
