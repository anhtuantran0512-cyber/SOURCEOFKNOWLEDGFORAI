---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-feature-sections/tailwind-problem-vs-solution-feature-section/"
title: "Tailwind Problem vs Solution Feature Section"
section: "layouts"
category: "tailwind-css-feature-sections"
category_name: "Tailwind CSS Feature Sections"
description: "The before/after pitch: a muted 'the old way' card beside a glowing 'with Fern' card, joined by a round arrow badge."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Problem vs Solution Feature Section
Source: https://codefronts.com/layouts/tailwind-css-feature-sections/tailwind-problem-vs-solution-feature-section/

The before/after pitch: a muted 'the old way' card beside a glowing 'with Fern' card, joined by a round arrow badge. The highlight card's gradient border is a padding-box / border-box background pair — two arbitrary background layers, no pseudo-element and no wrapper.
## HTML
```html
<section class="tfs-04 w-full min-h-svh bg-tfs04-bg px-5 py-20 font-tfs04-sans text-tfs04-ink antialiased sm:py-28" aria-labelledby="tfs-04-h">
  <div class="mx-auto grid w-full max-w-6xl gap-14">
    <header class="mx-auto grid max-w-2xl gap-4 text-center">
      <p class="text-sm font-bold uppercase tracking-[0.18em] text-tfs04-acc">The difference</p>
      <h2 id="tfs-04-h" class="text-balance text-4xl font-extrabold tracking-tight sm:text-5xl">Stop stitching tools together</h2>
      <p class="text-pretty text-lg text-tfs04-mut">Fern replaces the spreadsheet, the ticket queue and the status meeting with one shared roadmap.</p>
    </header>
    <div class="relative grid gap-6 lg:grid-cols-2 lg:gap-10">
      <article class="grid content-start gap-6 rounded-3xl border border-tfs04-line bg-tfs04-card p-8 sm:p-10">
        <div class="flex items-center gap-3"><span class="grid size-10 place-items-center rounded-full bg-rose-100 text-rose-600"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="M18 6 6 18M6 6l12 12"/></svg></span><h3 class="text-xl font-bold">The old way</h3></div>
        <ul class="grid gap-4 text-tfs04-mut">
          <li class="flex gap-3"><span class="mt-1 text-rose-500"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M18 6 6 18M6 6l12 12"/></svg></span><span class="line-through decoration-rose-400/60">Roadmap lives in a spreadsheet nobody trusts</span></li>
          <li class="flex gap-3"><span class="mt-1 text-rose-500"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M18 6 6 18M6 6l12 12"/></svg></span><span class="line-through decoration-rose-400/60">Status chased across six Slack threads</span></li>
          <li class="flex gap-3"><span class="mt-1 text-rose-500"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M18 6 6 18M6 6l12 12"/></svg></span><span class="line-through decoration-rose-400/60">Customer requests lost in support tickets</span></li>
          <li class="flex gap-3"><span class="mt-1 text-rose-500"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M18 6 6 18M6 6l12 12"/></svg></span><span class="line-through decoration-rose-400/60">Weekly hour-long sync just to align</span></li>
        </ul>
        <p class="mt-2 rounded-2xl bg-tfs04-bg p-4 text-sm text-tfs04-mut"><strong class="text-tfs04-ink">~6 hours</strong> per PM per week lost to coordination.</p>
      </article>
      <div aria-hidden="true" class="mx-auto grid size-14 place-items-center rounded-full bg-tfs04-ink text-white shadow-xl ring-8 ring-tfs04-bg lg:absolute lg:left-1/2 lg:top-1/2 lg:z-10 lg:-translate-x-1/2 lg:-translate-y-1/2"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-6 rotate-90 lg:rotate-0"><path d="M5 12h14M13 6l6 6-6 6"/></svg></div>
      <article class="grid content-start gap-6 rounded-3xl border-2 border-transparent p-8 shadow-[0_30px_80px_-30px_var(--color-tfs04-acc)] [background:linear-gradient(var(--color-tfs04-card),var(--color-tfs04-card))_padding-box,linear-gradient(135deg,var(--color-tfs04-acc),var(--color-tfs04-acc2))_border-box] sm:p-10">
        <div class="flex items-center gap-3"><span class="grid size-10 place-items-center rounded-full bg-tfs04-acc text-white"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="M20 6 9 17l-5-5"/></svg></span><h3 class="text-xl font-bold">With Fern</h3></div>
        <ul class="grid gap-4">
          <li class="flex gap-3"><span class="mt-1 text-tfs04-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M20 6 9 17l-5-5"/></svg></span>A live roadmap synced to every issue</li>
          <li class="flex gap-3"><span class="mt-1 text-tfs04-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M20 6 9 17l-5-5"/></svg></span>Automatic status from linked pull requests</li>
          <li class="flex gap-3"><span class="mt-1 text-tfs04-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M20 6 9 17l-5-5"/></svg></span>Requests clustered and ranked by revenue</li>
          <li class="flex gap-3"><span class="mt-1 text-tfs04-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M20 6 9 17l-5-5"/></svg></span>Async updates that write themselves</li>
        </ul>
        <p class="mt-2 rounded-2xl bg-tfs04-acc/10 p-4 text-sm"><strong class="text-tfs04-acc">5h back</strong> every week, measured across 900 teams.</p>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfs04-bg: #f3f6f4;
  --color-tfs04-bg: oklch(0.97 0.004 157);
  --color-tfs04-card: #ffffff;
  --color-tfs04-card: oklch(1. 0 0);
  --color-tfs04-ink: #0f1f17;
  --color-tfs04-ink: oklch(0.222 0.027 161);
  --color-tfs04-mut: #4a5a52;
  --color-tfs04-mut: oklch(0.451 0.024 164);
  --color-tfs04-line: #dbe3de;
  --color-tfs04-line: oklch(0.908 0.011 159);
  --color-tfs04-acc: #059669;
  --color-tfs04-acc: oklch(0.596 0.127 163);
  --color-tfs04-acc2: #84cc16;
  --color-tfs04-acc2: oklch(0.768 0.204 131);
  --font-tfs04-sans: 'Manrope', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tfs-04 {
  width: 100%;
  min-height: 100svh;
}
```
