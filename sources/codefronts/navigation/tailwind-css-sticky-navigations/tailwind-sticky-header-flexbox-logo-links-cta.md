---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-sticky-navigations/tailwind-sticky-header-flexbox-logo-links-cta/"
title: "Tailwind Sticky Header with Flexbox (Logo, Links, CTA)"
section: "navigation"
category: "tailwind-css-sticky-navigations"
category_name: "Tailwind CSS Sticky Navigations"
description: "The three-zone header every SaaS ships — logo left, links centred, actions right — built with one flex row."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Sticky Header with Flexbox (Logo, Links, CTA)
Source: https://codefronts.com/navigation/tailwind-css-sticky-navigations/tailwind-sticky-header-flexbox-logo-links-cta/

The three-zone header every SaaS ships — logo left, links centred, actions right — built with one flex row. flex-1 justify-center centres the links in the leftover space, and below md the nav drops into its own swipeable row with max-md:order-last max-md:basis-full, so nothing is hidden behind a menu.
## HTML
```html
<div class="tsn-02 w-full min-h-svh bg-tsn02-bg font-tsn02-sans text-tsn02-ink antialiased" aria-label="Tailwind flexbox sticky header demo">
  <a href="#tsn-02-main" class="sr-only focus:not-sr-only focus:fixed focus:left-3 focus:top-3 focus:z-[100] focus:rounded-lg focus:bg-tsn02-ink focus:px-4 focus:py-3 focus:text-sm focus:font-semibold focus:text-tsn02-bg">Skip to content</a>
  <header class="sticky top-0 z-40 flex min-h-16 flex-wrap items-center gap-x-6 border-b border-tsn02-line bg-tsn02-bg/85 px-[max(1.25rem,calc((100%-72rem)/2))] backdrop-blur-lg">
    <a href="#tsn-02-s1" class="flex min-h-11 items-center gap-2 rounded-lg text-[17px] font-extrabold tracking-[-0.03em] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tsn02-acc">
      <span aria-hidden="true" class="grid size-8 place-items-center rounded-full bg-tsn02-acc text-[13px] font-bold text-tsn02-bg">N</span>Northwind
    </a>
    <nav aria-label="Primary" class="flex flex-1 justify-center gap-1 max-md:order-last max-md:basis-full max-md:justify-start max-md:overflow-x-auto max-md:pb-2 max-md:[scrollbar-width:none]">
      <a href="#tsn-02-s1" aria-current="page" class="relative inline-flex min-h-11 flex-none items-center px-3 text-sm font-semibold text-tsn02-mut transition-colors after:absolute after:inset-x-3 after:bottom-2 after:h-0.5 after:origin-left after:scale-x-0 after:rounded-full after:bg-tsn02-acc after:transition-transform hover:text-tsn02-ink hover:after:scale-x-100 focus-visible:outline-2 focus-visible:outline-tsn02-acc aria-[current=page]:text-tsn02-ink aria-[current=page]:after:scale-x-100">Platform</a>
      <a href="#tsn-02-s2" class="relative inline-flex min-h-11 flex-none items-center px-3 text-sm font-semibold text-tsn02-mut transition-colors after:absolute after:inset-x-3 after:bottom-2 after:h-0.5 after:origin-left after:scale-x-0 after:rounded-full after:bg-tsn02-acc after:transition-transform hover:text-tsn02-ink hover:after:scale-x-100 focus-visible:outline-2 focus-visible:outline-tsn02-acc">Customers</a>
      <a href="#tsn-02-s3" class="relative inline-flex min-h-11 flex-none items-center px-3 text-sm font-semibold text-tsn02-mut transition-colors after:absolute after:inset-x-3 after:bottom-2 after:h-0.5 after:origin-left after:scale-x-0 after:rounded-full after:bg-tsn02-acc after:transition-transform hover:text-tsn02-ink hover:after:scale-x-100 focus-visible:outline-2 focus-visible:outline-tsn02-acc">Pricing</a>
      <a href="#tsn-02-s4" class="relative inline-flex min-h-11 flex-none items-center px-3 text-sm font-semibold text-tsn02-mut transition-colors after:absolute after:inset-x-3 after:bottom-2 after:h-0.5 after:origin-left after:scale-x-0 after:rounded-full after:bg-tsn02-acc after:transition-transform hover:text-tsn02-ink hover:after:scale-x-100 focus-visible:outline-2 focus-visible:outline-tsn02-acc">Company</a>
    </nav>
    <div class="ms-auto flex items-center gap-2">
      <a href="#tsn-02-s4" class="inline-flex min-h-11 items-center rounded-full px-4 text-sm font-semibold text-tsn02-ink hover:bg-tsn02-ink/5 focus-visible:outline-2 focus-visible:outline-tsn02-acc max-sm:hidden">Sign in</a>
      <a href="#tsn-02-s3" class="group inline-flex min-h-11 items-center gap-1.5 rounded-full bg-tsn02-acc pl-4 pr-3 text-sm font-bold text-tsn02-bg transition-colors hover:bg-tsn02-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsn02-acc">Book a demo <svg class="size-4 transition-transform group-hover:translate-x-0.5 motion-reduce:transition-none" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
    </div>
  </header>
  <div class="px-[max(1.25rem,calc((100%-72rem)/2))] pt-[clamp(3rem,8vw,6rem)] pb-[clamp(2rem,5vw,3.5rem)]">
    <p class="font-tsn02-mono text-[11.5px] font-medium uppercase tracking-[0.16em] text-tsn02-acc">flex · flex-1 · order</p>
    <h1 class="mt-4 max-w-[18ch] text-[clamp(34px,5.6vw,64px)] font-semibold leading-[1.02] tracking-[-0.035em] text-balance">Logo, links, action — one flex row</h1>
    <p class="mt-5 max-w-[54ch] text-[clamp(15px,1.6vw,17px)] leading-relaxed text-tsn02-mut text-pretty">Resize the window below 768px: the links wrap into their own swipeable row inside the same sticky bar.</p>
  </div>
  <main id="tsn-02-main" class="px-[max(1.25rem,calc((100%-72rem)/2))] grid pb-24">
    <section id="tsn-02-s1" class="scroll-mt-24 max-md:scroll-mt-32 min-h-[48svh] border-t border-tsn02-line py-[clamp(2.5rem,6vw,4.5rem)]" aria-labelledby="tsn-02-h1">
      <p class="font-tsn02-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn02-acc">Platform</p>
      <h2 id="tsn-02-h1" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">flex-1 does the centring</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn02-mut text-pretty">The nav takes the free space between the logo and the actions, then centres its links inside it. No absolute positioning, no magic widths.</p>
    </section>
    <section id="tsn-02-s2" class="scroll-mt-24 max-md:scroll-mt-32 min-h-[48svh] border-t border-tsn02-line py-[clamp(2.5rem,6vw,4.5rem)]" aria-labelledby="tsn-02-h2">
      <p class="font-tsn02-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn02-acc">Customers</p>
      <h2 id="tsn-02-h2" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Wrap instead of hide</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn02-mut text-pretty">Below <code class="rounded-md bg-tsn02-acc/10 px-1.5 py-0.5 font-tsn02-mono text-[0.86em] text-tsn02-ink">md</code> the nav becomes <code class="rounded-md bg-tsn02-acc/10 px-1.5 py-0.5 font-tsn02-mono text-[0.86em] text-tsn02-ink">order-last basis-full</code>, so it drops under the logo. Every link stays one tap away — no hamburger needed for four items.</p>
    </section>
    <section id="tsn-02-s3" class="scroll-mt-24 max-md:scroll-mt-32 min-h-[48svh] border-t border-tsn02-line py-[clamp(2.5rem,6vw,4.5rem)]" aria-labelledby="tsn-02-h3">
      <p class="font-tsn02-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn02-acc">Pricing</p>
      <h2 id="tsn-02-h3" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">ms-auto pins the actions</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn02-mut text-pretty">When the row wraps, <code class="rounded-md bg-tsn02-acc/10 px-1.5 py-0.5 font-tsn02-mono text-[0.86em] text-tsn02-ink">ms-auto</code> keeps “Book a demo” glued to the right edge of the first line.</p>
    </section>
    <section id="tsn-02-s4" class="scroll-mt-24 max-md:scroll-mt-32 min-h-[48svh] border-t border-tsn02-line py-[clamp(2.5rem,6vw,4.5rem)]" aria-labelledby="tsn-02-h4">
      <p class="font-tsn02-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn02-acc">Company</p>
      <h2 id="tsn-02-h4" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">min-h, never h</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn02-mut text-pretty">A wrapping header must be allowed to grow. <code class="rounded-md bg-tsn02-acc/10 px-1.5 py-0.5 font-tsn02-mono text-[0.86em] text-tsn02-ink">min-h-16</code> keeps the desktop rhythm while letting the phone layout gain a second row.</p>
    </section>
  </main>
  <footer class="border-t border-tsn02-line px-[max(1.25rem,calc((100%-72rem)/2))] py-10 font-tsn02-mono text-xs text-tsn02-mut">Tailwind sticky navigation · pattern 02 of 25</footer>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsn02-bg: #f8f4ec;
  --color-tsn02-bg: oklch(0.97 0.012 85);
  --color-tsn02-surface: #fffdf8;
  --color-tsn02-surface: oklch(0.995 0.006 85);
  --color-tsn02-ink: #1f2a22;
  --color-tsn02-ink: oklch(0.27 0.025 150);
  --color-tsn02-mut: #55604f;
  --color-tsn02-mut: oklch(0.47 0.03 140);
  --color-tsn02-acc: #2f6b46;
  --color-tsn02-acc: oklch(0.47 0.1 152);
  --color-tsn02-line: #1f2a221a;
  --color-tsn02-line: oklch(0.27 0.025 150 / 0.1);
  --font-tsn02-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tsn02-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, restated in CSS so the page is sized before the browser build compiles. */

.tsn-02 {
  width: 100%;
  min-height: 100svh;
}
/* Smooth anchor jumps live on <html>, outside the markup, so they stay in CSS. */

@media (prefers-reduced-motion: no-preference) {
  :root:has(.tsn-02) {
    scroll-behavior: smooth;
  }
}
```
