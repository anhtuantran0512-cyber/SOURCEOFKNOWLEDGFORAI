---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-sticky-navigations/tailwind-transparent-to-solid-navbar-on-scroll/"
title: "Tailwind Transparent to Solid Navbar on Scroll"
section: "navigation"
category: "tailwind-css-sticky-navigations"
category_name: "Tailwind CSS Sticky Navigations"
description: "White type floating over a full-bleed hero that turns into a frosted solid bar the moment the hero scrolls away."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Transparent to Solid Navbar on Scroll
Source: https://codefronts.com/navigation/tailwind-css-sticky-navigations/tailwind-transparent-to-solid-navbar-on-scroll/

White type floating over a full-bleed hero that turns into a frosted solid bar the moment the hero scrolls away. A negative margin (-mb-[4.5rem]) lets the hero sit under the sticky header, and an IntersectionObserver — not a scroll listener — flips data-solid exactly when the hero's bottom crosses the bar.
## HTML
```html
<div class="tsn-08 w-full min-h-svh bg-tsn08-bg font-tsn08-sans text-tsn08-ink antialiased" aria-label="Transparent to solid navbar on scroll demo">
  <a href="#tsn-08-main" class="sr-only focus:not-sr-only focus:fixed focus:left-3 focus:top-3 focus:z-[100] focus:rounded-lg focus:bg-tsn08-ink focus:px-4 focus:py-3 focus:text-sm focus:font-semibold focus:text-tsn08-bg">Skip to content</a>
  <header data-tsn08-header class="group/hdr sticky top-0 z-40 -mb-[4.5rem] flex h-[4.5rem] items-center gap-6 text-white px-[max(1.25rem,calc((100%-72rem)/2))] transition-[background-color,color,box-shadow] duration-500 data-solid:bg-tsn08-bg/85 data-solid:text-tsn08-ink data-solid:shadow-[0_1px_0_var(--color-tsn08-line),0_12px_30px_-18px_rgb(30_40_40/0.35)] data-solid:backdrop-blur-xl motion-reduce:transition-none">
    <a href="#tsn-08-hero" class="flex min-h-11 items-center rounded font-tsn08-serif text-[30px] leading-none tracking-[-0.01em] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-current">Aster</a>
    <nav aria-label="Primary" class="ms-auto flex gap-1 max-md:hidden">
      <a href="#tsn-08-s1" class="inline-flex min-h-11 items-center rounded-full px-4 text-sm font-medium opacity-85 transition hover:opacity-100 hover:bg-current/10 focus-visible:outline-2 focus-visible:outline-current">Stay</a>
      <a href="#tsn-08-s2" class="inline-flex min-h-11 items-center rounded-full px-4 text-sm font-medium opacity-85 transition hover:opacity-100 hover:bg-current/10 focus-visible:outline-2 focus-visible:outline-current">Dine</a>
      <a href="#tsn-08-s3" class="inline-flex min-h-11 items-center rounded-full px-4 text-sm font-medium opacity-85 transition hover:opacity-100 hover:bg-current/10 focus-visible:outline-2 focus-visible:outline-current">Spa</a>
      <a href="#tsn-08-s4" class="inline-flex min-h-11 items-center rounded-full px-4 text-sm font-medium opacity-85 transition hover:opacity-100 hover:bg-current/10 focus-visible:outline-2 focus-visible:outline-current">Journal</a>
    </nav>
    <a href="#tsn-08-s4" class="inline-flex min-h-11 items-center rounded-full border border-white/60 px-5 text-sm font-semibold backdrop-blur-sm transition hover:bg-white hover:text-tsn08-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-current group-data-solid/hdr:border-tsn08-acc group-data-solid/hdr:bg-tsn08-acc group-data-solid/hdr:text-white max-md:ms-auto">Reserve</a>
  </header>
  <section id="tsn-08-hero" data-tsn08-hero aria-labelledby="tsn-08-title" class="relative isolate grid min-h-svh content-end overflow-hidden bg-[linear-gradient(160deg,#2c6e6a,#0f2a2c)] px-[max(1.25rem,calc((100%-72rem)/2))] pb-[clamp(3rem,8vw,6rem)] text-white">
    <img src="https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?auto=format&fit=crop&w=1600&q=70" alt="" class="absolute inset-0 -z-10 size-full object-cover">
    <div aria-hidden="true" class="absolute inset-0 -z-10 bg-[linear-gradient(to_bottom,rgb(10_20_20/0.55),transparent_28%,transparent_45%,rgb(10_20_20/0.7))]"></div>
    <p class="font-tsn08-mono text-[11.5px] uppercase tracking-[0.18em] text-white/85">IntersectionObserver · data-solid</p>
    <h1 id="tsn-08-title" class="mt-4 max-w-[13ch] font-tsn08-serif text-[clamp(48px,9vw,112px)] leading-[0.92] tracking-[-0.02em]">Where the coast slows down</h1>
    <p class="mt-6 max-w-[44ch] text-[17px] leading-relaxed text-white/90">Scroll past the photograph. The moment it clears the bar, the header turns solid and the type switches to ink.</p>
  </section>
  <main id="tsn-08-main" class="px-[max(1.25rem,calc((100%-72rem)/2))] grid gap-5 pt-[clamp(2rem,5vw,3.5rem)] pb-24">
    <section id="tsn-08-s1" class="scroll-mt-24 min-h-[44svh] rounded-[1.75rem] border border-tsn08-line bg-tsn08-surface p-[clamp(1.5rem,4vw,3rem)] shadow-[0_1px_2px_rgb(0_0_0/0.04)]" aria-labelledby="tsn-08-h1">
      <p class="font-tsn08-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn08-acc">Stay</p>
      <h2 id="tsn-08-h1" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Overlap without fixed</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn08-mut text-pretty">A negative bottom margin equal to the header’s height lets the hero start under the sticky bar. It still pins, still reserves no extra space, still respects its parent.</p>
    </section>
    <section id="tsn-08-s2" class="scroll-mt-24 min-h-[44svh] rounded-[1.75rem] border border-tsn08-line bg-tsn08-surface p-[clamp(1.5rem,4vw,3rem)] shadow-[0_1px_2px_rgb(0_0_0/0.04)]" aria-labelledby="tsn-08-h2">
      <p class="font-tsn08-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn08-acc">Dine</p>
      <h2 id="tsn-08-h2" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Observe, don’t listen</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn08-mut text-pretty">An <code class="rounded-md bg-tsn08-acc/10 px-1.5 py-0.5 font-tsn08-mono text-[0.86em] text-tsn08-ink">IntersectionObserver</code> watches the hero with a 72px top inset. No scroll handler, no per-frame reads — the browser tells you when the line is crossed.</p>
    </section>
    <section id="tsn-08-s3" class="scroll-mt-24 min-h-[44svh] rounded-[1.75rem] border border-tsn08-line bg-tsn08-surface p-[clamp(1.5rem,4vw,3rem)] shadow-[0_1px_2px_rgb(0_0_0/0.04)]" aria-labelledby="tsn-08-h3">
      <p class="font-tsn08-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn08-acc">Spa</p>
      <h2 id="tsn-08-h3" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">A scrim, not a hope</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn08-mut text-pretty">White type over a bright sky fails contrast. A soft top gradient keeps the transparent header legible on any photograph.</p>
    </section>
    <section id="tsn-08-s4" class="scroll-mt-24 min-h-[44svh] rounded-[1.75rem] border border-tsn08-line bg-tsn08-surface p-[clamp(1.5rem,4vw,3rem)] shadow-[0_1px_2px_rgb(0_0_0/0.04)]" aria-labelledby="tsn-08-h4">
      <p class="font-tsn08-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn08-acc">Journal</p>
      <h2 id="tsn-08-h4" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">The CTA changes clothes</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn08-mut text-pretty">Outlined on the photo, filled with the accent on the solid bar. One <code class="rounded-md bg-tsn08-acc/10 px-1.5 py-0.5 font-tsn08-mono text-[0.86em] text-tsn08-ink">group-data-solid/hdr:</code> variant per property.</p>
    </section>
  </main>
  <footer class="border-t border-tsn08-line px-[max(1.25rem,calc((100%-72rem)/2))] py-10 font-tsn08-mono text-xs text-tsn08-mut">Tailwind sticky navigation · pattern 08 of 25</footer>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsn08-bg: #f6f3ec;
  --color-tsn08-bg: oklch(0.963 0.012 90);
  --color-tsn08-surface: #fffdf8;
  --color-tsn08-surface: oklch(0.994 0.006 90);
  --color-tsn08-ink: #1b2626;
  --color-tsn08-ink: oklch(0.25 0.018 195);
  --color-tsn08-mut: #526060;
  --color-tsn08-mut: oklch(0.46 0.02 195);
  --color-tsn08-acc: #1e6f69;
  --color-tsn08-acc: oklch(0.48 0.08 185);
  --color-tsn08-line: #1b26261a;
  --color-tsn08-line: oklch(0.25 0.018 195 / 0.1);
  --font-tsn08-serif: 'Instrument Serif', Georgia, serif;
  --font-tsn08-sans: 'DM Sans', system-ui, sans-serif;
  --font-tsn08-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, restated in CSS so the page is sized before the browser build compiles. */

.tsn-08 {
  width: 100%;
  min-height: 100svh;
}
/* Smooth anchor jumps live on <html>, outside the markup, so they stay in CSS. */

@media (prefers-reduced-motion: no-preference) {
  :root:has(.tsn-08) {
    scroll-behavior: smooth;
  }
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('.tsn-08').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    const hdr = root.querySelector('[data-tsn08-header]');
    const hero = root.querySelector('[data-tsn08-hero]');
    const io = new IntersectionObserver(([entry]) => {
      hdr.toggleAttribute('data-solid', !entry.isIntersecting);
    }, { rootMargin: '-' + hdr.offsetHeight + 'px 0px 0px 0px' });
    io.observe(hero);
  });
})();
```
