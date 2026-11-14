---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-sticky-navigations/minimal-tailwind-sticky-header-single-cta-button/"
title: "Minimal Tailwind Sticky Header with Single CTA Button"
section: "navigation"
category: "tailwind-css-sticky-navigations"
category_name: "Tailwind CSS Sticky Navigations"
description: "For launch pages where the only job is one action: a wordmark on the left, a single high-emphasis button on the right, and nothing else."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Minimal Tailwind Sticky Header with Single CTA Button
Source: https://codefronts.com/navigation/tailwind-css-sticky-navigations/minimal-tailwind-sticky-header-single-cta-button/

For launch pages where the only job is one action: a wordmark on the left, a single high-emphasis button on the right, and nothing else. The CTA carries the personality — a light sweep drawn with before: utilities, an arrow chip that nudges forward, and a press state — all in one class list, zero JavaScript.
## HTML
```html
<div class="tsn-13 w-full min-h-svh bg-tsn13-bg font-tsn13-sans text-tsn13-ink antialiased" aria-label="Minimal sticky header with single CTA demo">
  <header class="sticky top-0 z-40 flex h-[4.5rem] items-center justify-between gap-4 bg-tsn13-bg/80 px-[max(1.25rem,calc((100%-72rem)/2))] backdrop-blur-xl">
    <div class="flex items-center gap-4">
      <a href="#tsn-13-s1" class="flex min-h-11 items-center rounded text-2xl font-bold tracking-[-0.05em] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tsn13-ink">quill<span aria-hidden="true" class="text-tsn13-acc2">.</span></a>
      <p class="flex items-center gap-2 rounded-full border border-tsn13-line px-3 py-1 font-tsn13-mono text-[11px] text-tsn13-mut max-sm:hidden"><span aria-hidden="true" class="size-1.5 animate-pulse rounded-full bg-tsn13-acc2 motion-reduce:animate-none"></span>Private beta · 214 spots left</p>
    </div>
    <a href="#tsn-13-s4" class="group relative inline-flex min-h-11 items-center gap-3 overflow-hidden rounded-full bg-tsn13-ink py-1.5 pl-5 pr-1.5 text-sm font-semibold text-tsn13-bg shadow-[0_10px_24px_-10px_rgb(20_20_10/0.5)] transition-transform before:absolute before:inset-y-0 before:-left-1/2 before:w-1/3 before:-skew-x-12 before:bg-white/25 before:transition-transform before:duration-700 hover:before:translate-x-[420%] active:scale-[0.97] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsn13-ink motion-reduce:before:hidden">
      Join the waitlist
      <span aria-hidden="true" class="grid size-8 place-items-center rounded-full bg-tsn13-acc text-tsn13-ink transition-transform duration-300 group-hover:translate-x-0.5 group-hover:-rotate-45 motion-reduce:transition-none"><svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span>
    </a>
  </header>
  <div class="px-[max(1.25rem,calc((100%-72rem)/2))] pt-[clamp(3rem,8vw,6rem)] pb-[clamp(2rem,5vw,3.5rem)]">
    <p class="font-tsn13-mono text-[11.5px] font-medium uppercase tracking-[0.16em] text-tsn13-acc">one action · zero links</p>
    <h1 class="mt-4 max-w-[18ch] text-[clamp(44px,8vw,104px)] font-semibold leading-[0.95] tracking-[-0.05em] text-balance">Write less. Say more.</h1>
    <p class="mt-5 max-w-[54ch] text-[clamp(15px,1.6vw,17px)] leading-relaxed text-tsn13-mut text-pretty">A launch page header has one job. Hover the button: the sweep, the arrow and the press state carry all the personality the header needs.</p>
  </div>
  <main id="tsn-13-main" class="px-[max(1.25rem,calc((100%-72rem)/2))] grid pb-24">
    <section id="tsn-13-s1" class="scroll-mt-24 min-h-[48svh] border-t border-tsn13-line py-[clamp(2.5rem,6vw,4.5rem)]" aria-labelledby="tsn-13-h1">
      <p class="font-tsn13-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn13-acc">Focus</p>
      <h2 id="tsn-13-h1" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Two items, maximum calm</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn13-mut text-pretty">A wordmark and a button, pushed apart with <code class="rounded-md bg-tsn13-acc/10 px-1.5 py-0.5 font-tsn13-mono text-[0.86em] text-tsn13-ink">justify-between</code>. Nothing competes, so the eye lands where you want it.</p>
    </section>
    <section id="tsn-13-s2" class="scroll-mt-24 min-h-[48svh] border-t border-tsn13-line py-[clamp(2.5rem,6vw,4.5rem)]" aria-labelledby="tsn-13-h2">
      <p class="font-tsn13-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn13-acc">Craft</p>
      <h2 id="tsn-13-h2" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">A shine with no extra element</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn13-mut text-pretty">The sweep is a skewed <code class="rounded-md bg-tsn13-acc/10 px-1.5 py-0.5 font-tsn13-mono text-[0.86em] text-tsn13-ink">before:</code> pseudo-element parked off the left edge and translated across on hover, clipped by <code class="rounded-md bg-tsn13-acc/10 px-1.5 py-0.5 font-tsn13-mono text-[0.86em] text-tsn13-ink">overflow-hidden</code>.</p>
    </section>
    <section id="tsn-13-s3" class="scroll-mt-24 min-h-[48svh] border-t border-tsn13-line py-[clamp(2.5rem,6vw,4.5rem)]" aria-labelledby="tsn-13-h3">
      <p class="font-tsn13-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn13-acc">Feedback</p>
      <h2 id="tsn-13-h3" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Hover, press, done</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn13-mut text-pretty">The arrow chip nudges and turns on hover; <code class="rounded-md bg-tsn13-acc/10 px-1.5 py-0.5 font-tsn13-mono text-[0.86em] text-tsn13-ink">active:scale-[0.97]</code> gives a physical press. Under <code class="rounded-md bg-tsn13-acc/10 px-1.5 py-0.5 font-tsn13-mono text-[0.86em] text-tsn13-ink">motion-reduce</code> the sweep disappears.</p>
    </section>
    <section id="tsn-13-s4" class="scroll-mt-24 min-h-[48svh] border-t border-tsn13-line py-[clamp(2.5rem,6vw,4.5rem)]" aria-labelledby="tsn-13-h4">
      <p class="font-tsn13-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn13-acc">Waitlist</p>
      <h2 id="tsn-13-h4" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Status with a pulse</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn13-mut text-pretty">A quiet “Private beta” chip beside the logo adds urgency without adding a link — and hides below <code class="rounded-md bg-tsn13-acc/10 px-1.5 py-0.5 font-tsn13-mono text-[0.86em] text-tsn13-ink">sm</code> so the button never wraps.</p>
    </section>
  </main>
  <footer class="border-t border-tsn13-line px-[max(1.25rem,calc((100%-72rem)/2))] py-10 font-tsn13-mono text-xs text-tsn13-mut">Tailwind sticky navigation · pattern 13 of 25</footer>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsn13-bg: #f2efe8;
  --color-tsn13-bg: oklch(0.953 0.01 90);
  --color-tsn13-surface: #faf8f3;
  --color-tsn13-surface: oklch(0.981 0.006 90);
  --color-tsn13-ink: #171712;
  --color-tsn13-ink: oklch(0.2 0.01 105);
  --color-tsn13-mut: #5b5a50;
  --color-tsn13-mut: oklch(0.46 0.015 105);
  --color-tsn13-acc: #d4f04a;
  --color-tsn13-acc: oklch(0.91 0.18 118);
  --color-tsn13-acc2: #e0532f;
  --color-tsn13-acc2: oklch(0.62 0.18 38);
  --color-tsn13-line: #17171226;
  --color-tsn13-line: oklch(0.2 0.01 105 / 0.15);
  --font-tsn13-sans: 'Instrument Sans', system-ui, sans-serif;
  --font-tsn13-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, restated in CSS so the page is sized before the browser build compiles. */

.tsn-13 {
  width: 100%;
  min-height: 100svh;
}
/* Smooth anchor jumps live on <html>, outside the markup, so they stay in CSS. */

@media (prefers-reduced-motion: no-preference) {
  :root:has(.tsn-13) {
    scroll-behavior: smooth;
  }
}
```
