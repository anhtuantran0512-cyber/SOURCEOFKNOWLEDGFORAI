---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-sticky-navigations/tailwind-css-sticky-navbar-no-javascript/"
title: "Tailwind CSS Sticky Navbar (No JavaScript, sticky top-0)"
section: "navigation"
category: "tailwind-css-sticky-navigations"
category_name: "Tailwind CSS Sticky Navigations"
description: "The baseline every other pattern here extends: sticky top-0 z-40 pins a product header to the viewport, bg-tsn01-bg/75 backdrop-blur-xl lets the page…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Sticky Navbar (No JavaScript, sticky top-0)
Source: https://codefronts.com/navigation/tailwind-css-sticky-navigations/tailwind-css-sticky-navbar-no-javascript/

The baseline every other pattern here extends: sticky top-0 z-40 pins a product header to the viewport, bg-tsn01-bg/75 backdrop-blur-xl lets the page dissolve beneath it, and scroll-mt-24 on every section stops in-page anchors from landing behind the bar.
## HTML
```html
<div class="tsn-01 w-full min-h-svh bg-tsn01-bg font-tsn01-sans text-tsn01-ink antialiased" aria-label="Tailwind sticky navbar demo">
  <a href="#tsn-01-main" class="sr-only focus:not-sr-only focus:fixed focus:left-3 focus:top-3 focus:z-[100] focus:rounded-lg focus:bg-tsn01-ink focus:px-4 focus:py-3 focus:text-sm focus:font-semibold focus:text-tsn01-bg">Skip to content</a>
  <header class="sticky top-0 z-40 flex h-16 items-center gap-4 border-b border-tsn01-line bg-tsn01-bg/75 px-[max(1.25rem,calc((100%-72rem)/2))] backdrop-blur-xl backdrop-saturate-150 sm:gap-8">
    <a href="#tsn-01-s1" class="flex min-h-11 flex-none items-center gap-2.5 rounded-lg text-[15px] font-semibold tracking-tight focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tsn01-acc">
      <span aria-hidden="true" class="size-7 rounded-lg bg-[conic-gradient(from_200deg,var(--color-tsn01-acc),var(--color-tsn01-acc2),var(--color-tsn01-acc))] shadow-[inset_0_0_0_1px_rgb(255_255_255/0.25)]"></span>Meridian
    </a>
    <nav aria-label="Primary" class="flex min-w-0 flex-1 gap-1 overflow-x-auto [scrollbar-width:none]">
      <a href="#tsn-01-s1" aria-current="page" class="inline-flex min-h-11 flex-none items-center rounded-full px-3.5 text-sm font-medium text-tsn01-mut transition-colors hover:bg-tsn01-ink/5 hover:text-tsn01-ink focus-visible:outline-2 focus-visible:outline-tsn01-acc aria-[current=page]:text-tsn01-ink">Product</a>
      <a href="#tsn-01-s2" class="inline-flex min-h-11 flex-none items-center rounded-full px-3.5 text-sm font-medium text-tsn01-mut transition-colors hover:bg-tsn01-ink/5 hover:text-tsn01-ink focus-visible:outline-2 focus-visible:outline-tsn01-acc">Pricing</a>
      <a href="#tsn-01-s3" class="inline-flex min-h-11 flex-none items-center rounded-full px-3.5 text-sm font-medium text-tsn01-mut transition-colors hover:bg-tsn01-ink/5 hover:text-tsn01-ink focus-visible:outline-2 focus-visible:outline-tsn01-acc">Docs</a>
      <a href="#tsn-01-s4" class="inline-flex min-h-11 flex-none items-center rounded-full px-3.5 text-sm font-medium text-tsn01-mut transition-colors hover:bg-tsn01-ink/5 hover:text-tsn01-ink focus-visible:outline-2 focus-visible:outline-tsn01-acc">Changelog</a>
    </nav>
    <a href="#tsn-01-s4" class="inline-flex min-h-11 flex-none items-center rounded-full bg-tsn01-ink px-4 text-sm font-semibold text-tsn01-bg shadow-[0_6px_16px_-6px_var(--color-tsn01-acc)] transition hover:-translate-y-px hover:bg-tsn01-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsn01-acc motion-reduce:transition-none">Start free</a>
  </header>
  <div class="px-[max(1.25rem,calc((100%-72rem)/2))] pt-[clamp(3rem,8vw,6rem)] pb-[clamp(2rem,5vw,3.5rem)]">
    <p class="font-tsn01-mono text-[11.5px] font-medium uppercase tracking-[0.16em] text-tsn01-acc">sticky · top-0 · z-40</p>
    <h1 class="mt-4 max-w-[18ch] text-[clamp(34px,5.6vw,64px)] font-semibold leading-[1.02] tracking-[-0.035em] text-balance">The sticky header, done properly</h1>
    <p class="mt-5 max-w-[54ch] text-[clamp(15px,1.6vw,17px)] leading-relaxed text-tsn01-mut text-pretty">Scroll the page. The bar pins at the top, and every anchor link lands below it — not behind it.</p>
  </div>
  <main id="tsn-01-main" class="px-[max(1.25rem,calc((100%-72rem)/2))] grid gap-5 pb-24">
    <section id="tsn-01-s1" class="scroll-mt-24 min-h-[44svh] rounded-[1.75rem] border border-tsn01-line bg-tsn01-surface p-[clamp(1.5rem,4vw,3rem)] shadow-[0_1px_2px_rgb(0_0_0/0.04)]" aria-labelledby="tsn-01-h1">
      <p class="font-tsn01-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn01-acc">Product</p>
      <h2 id="tsn-01-h1" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Three utilities, one caveat</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn01-mut text-pretty">A sticky box keeps its space in normal flow, so nothing jumps when it pins — the layout shift you get for free with <code class="rounded-md bg-tsn01-acc/10 px-1.5 py-0.5 font-tsn01-mono text-[0.86em] text-tsn01-ink">fixed</code> never happens.</p>
    </section>
    <section id="tsn-01-s2" class="scroll-mt-24 min-h-[44svh] rounded-[1.75rem] border border-tsn01-line bg-tsn01-surface p-[clamp(1.5rem,4vw,3rem)] shadow-[0_1px_2px_rgb(0_0_0/0.04)]" aria-labelledby="tsn-01-h2">
      <p class="font-tsn01-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn01-acc">Pricing</p>
      <h2 id="tsn-01-h2" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Anchors that clear the bar</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn01-mut text-pretty">Click any link above. <code class="rounded-md bg-tsn01-acc/10 px-1.5 py-0.5 font-tsn01-mono text-[0.86em] text-tsn01-ink">scroll-mt-24</code> on each section offsets the jump by the header height, for clicks, <code class="rounded-md bg-tsn01-acc/10 px-1.5 py-0.5 font-tsn01-mono text-[0.86em] text-tsn01-ink">:target</code> and keyboard focus alike.</p>
    </section>
    <section id="tsn-01-s3" class="scroll-mt-24 min-h-[44svh] rounded-[1.75rem] border border-tsn01-line bg-tsn01-surface p-[clamp(1.5rem,4vw,3rem)] shadow-[0_1px_2px_rgb(0_0_0/0.04)]" aria-labelledby="tsn-01-h3">
      <p class="font-tsn01-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn01-acc">Docs</p>
      <h2 id="tsn-01-h3" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">The overflow trap</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn01-mut text-pretty">The nearest scrolling ancestor becomes the sticky port. One stray <code class="rounded-md bg-tsn01-acc/10 px-1.5 py-0.5 font-tsn01-mono text-[0.86em] text-tsn01-ink">overflow-hidden</code> higher up and the bar quietly scrolls away with the page — reach for <code class="rounded-md bg-tsn01-acc/10 px-1.5 py-0.5 font-tsn01-mono text-[0.86em] text-tsn01-ink">overflow-x-clip</code>.</p>
    </section>
    <section id="tsn-01-s4" class="scroll-mt-24 min-h-[44svh] rounded-[1.75rem] border border-tsn01-line bg-tsn01-surface p-[clamp(1.5rem,4vw,3rem)] shadow-[0_1px_2px_rgb(0_0_0/0.04)]" aria-labelledby="tsn-01-h4">
      <p class="font-tsn01-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn01-acc">Changelog</p>
      <h2 id="tsn-01-h4" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Bounded by its parent</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn01-mut text-pretty">Sticky elements never leave their containing block. Wrap the header with a single section and it releases at that section’s end — chapter headers with zero script.</p>
      <p class="mt-8 inline-flex rounded-full border border-tsn01-line px-3.5 py-2 font-tsn01-mono text-[11.5px] text-tsn01-mut">0 bytes of JS · 0 lines of custom CSS</p>
    </section>
  </main>
  <footer class="border-t border-tsn01-line px-[max(1.25rem,calc((100%-72rem)/2))] py-10 font-tsn01-mono text-xs text-tsn01-mut">Tailwind sticky navigation · pattern 01 of 25</footer>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsn01-bg: #f4f5fb;
  --color-tsn01-bg: oklch(0.967 0.008 265);
  --color-tsn01-surface: #ffffff;
  --color-tsn01-surface: oklch(1 0 0);
  --color-tsn01-ink: #1c1e33;
  --color-tsn01-ink: oklch(0.22 0.022 272);
  --color-tsn01-mut: #5c5f78;
  --color-tsn01-mut: oklch(0.48 0.025 272);
  --color-tsn01-acc: #5547d6;
  --color-tsn01-acc: oklch(0.52 0.2 278);
  --color-tsn01-acc2: #8b7cf6;
  --color-tsn01-acc2: oklch(0.66 0.17 290);
  --color-tsn01-line: #1c1e331a;
  --color-tsn01-line: oklch(0.22 0.022 272 / 0.1);
  --font-tsn01-sans: 'Geist', system-ui, sans-serif;
  --font-tsn01-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, restated in CSS so the page is sized before the browser build compiles. */

.tsn-01 {
  width: 100%;
  min-height: 100svh;
}
/* Smooth anchor jumps live on <html>, outside the markup, so they stay in CSS. */

@media (prefers-reduced-motion: no-preference) {
  :root:has(.tsn-01) {
    scroll-behavior: smooth;
  }
}
```
