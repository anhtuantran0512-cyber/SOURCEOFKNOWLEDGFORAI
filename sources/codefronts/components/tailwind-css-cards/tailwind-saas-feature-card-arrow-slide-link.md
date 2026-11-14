---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-cards/tailwind-saas-feature-card-arrow-slide-link/"
title: "Tailwind SaaS Feature Card with Arrow-Slide Link"
section: "components"
category: "tailwind-css-cards"
category_name: "Tailwind CSS Cards"
description: "The smallest card in the collection and the most copy-pasted shape in SaaS: gradient icon tile, NEW chip, headline, one line of copy, and a Learn-more link…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind SaaS Feature Card with Arrow-Slide Link
Source: https://codefronts.com/components/tailwind-css-cards/tailwind-saas-feature-card-arrow-slide-link/

The smallest card in the collection and the most copy-pasted shape in SaaS: gradient icon tile, NEW chip, headline, one line of copy, and a Learn-more link whose arrow slides when you hover anywhere on the tile. The port's win is that the two-selector arrow rule becomes one group-hover/card: utility.
## HTML
```html
<section class="twc-12 w-full min-h-svh flex items-center justify-center px-5 py-9 bg-twc12-bg font-twc12-sans">
  <article class="group/card relative w-full max-w-[340px] p-5.5 rounded-[18px] bg-white border border-black/6 shadow-[0_2px_10px_oklch(0_0_0/0.03)] transition-[transform,box-shadow,border-color] duration-250 hover:-translate-y-0.5 hover:border-twc12-acc/20 [@media(hover:hover)]:hover:shadow-[0_14px_32px_oklch(0_0_0/0.06),0_0_0_4px_oklch(0.55_0.2_275/0.05)] motion-reduce:transition-none motion-reduce:hover:translate-y-0">

    <span aria-hidden="true" class="inline-flex items-center justify-center size-11 mb-4 rounded-xl [background:linear-gradient(135deg,#818cf8_0%,#6366f1_100%)] shadow-[0_6px_16px_oklch(0.55_0.2_275/0.28),inset_0_0_0_1px_oklch(1_0_0/0.4)]">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="7" r="4"/><path d="M3 21v-2a4 4 0 0 1 4-4h4a4 4 0 0 1 4 4v2"/><circle cx="17" cy="7" r="4" opacity="0.6"/><path d="M14 15h4a4 4 0 0 1 4 4v2" opacity="0.6"/></svg>
    </span>

    <span class="absolute top-5.5 right-5.5 px-2 py-[3px] rounded-full font-twc12-mono text-[10px] font-bold tracking-[0.14em] uppercase text-twc12-acc bg-twc12-acc/10 border border-twc12-acc/20">New</span>

    <h3 class="m-0 mb-1.5 pr-16 text-[17px] font-bold tracking-[-0.01em] text-twc12-ink">Real-time collaboration</h3>
    <p class="m-0 mb-4 text-[13px]/[1.55] text-twc12-muted">See teammates' cursors and edits as they happen &mdash; no refresh, no conflicts.</p>

    <a href="#learn" class="inline-flex items-center gap-1.5 min-h-11 rounded-md no-underline text-[13px] font-bold text-twc12-accdeep transition-colors duration-200 hover:text-twc12-accdark hover:underline hover:underline-offset-[3px] focus-visible:outline-2 focus-visible:outline-twc12-acc focus-visible:outline-offset-[3px]">
      Learn more
      <span aria-hidden="true" class="inline-flex items-center transition-transform duration-200 ease-out group-hover/card:translate-x-[3px] motion-reduce:transition-none motion-reduce:group-hover/card:translate-x-0">
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
      </span>
    </a>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-twc12-bg: #f8f7f4;
  --color-twc12-bg: oklch(0.97 0.005 90);
  --color-twc12-ink: #1a1a1a;
  --color-twc12-ink: oklch(0.21 0.005 270);
  --color-twc12-muted: #6b6b7c;
  --color-twc12-muted: oklch(0.51 0.02 285);
  --color-twc12-acc: #6366f1;
  --color-twc12-acc: oklch(0.55 0.2 275);
  --color-twc12-accdeep: #4338ca;
  --color-twc12-accdeep: oklch(0.42 0.21 275);
  --color-twc12-accdark: #312e81;
  --color-twc12-accdark: oklch(0.32 0.15 275);
  --font-twc12-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-twc12-mono: 'JetBrains Mono', ui-monospace, Menlo, monospace;
}
/* The smallest stylesheet in the collection: tokens and the root contract. */

.twc-12 {
  width: 100%;
  min-height: 100svh;
}
```
