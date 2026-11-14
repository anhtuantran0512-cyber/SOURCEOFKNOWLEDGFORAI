---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-sticky-navigations/tailwind-sticky-header-shrink-on-scroll/"
title: "Tailwind Sticky Header Shrink on Scroll"
section: "navigation"
category: "tailwind-css-sticky-navigations"
category_name: "Tailwind CSS Sticky Navigations"
description: "A roomy 80px header that settles into a 52px compact bar once you scroll — logo, padding, CTA and shadow all transition together."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Sticky Header Shrink on Scroll
Source: https://codefronts.com/navigation/tailwind-css-sticky-navigations/tailwind-sticky-header-shrink-on-scroll/

A roomy 80px header that settles into a 52px compact bar once you scroll — logo, padding, CTA and shadow all transition together. The script only flips data-scrolled; every size lives in group-data-scrolled/hdr: variants. Hysteresis (shrink past 64px, grow back under 8px) kills the threshold flicker the CSS original had.
## HTML
```html
<div class="tsn-06 w-full min-h-svh bg-tsn06-bg font-tsn06-sans text-tsn06-ink antialiased" aria-label="Tailwind shrink on scroll header demo">
  <a href="#tsn-06-main" class="sr-only focus:not-sr-only focus:fixed focus:left-3 focus:top-3 focus:z-[100] focus:rounded-lg focus:bg-tsn06-ink focus:px-4 focus:py-3 focus:text-sm focus:font-semibold focus:text-tsn06-bg">Skip to content</a>
  <header data-tsn06-header class="group/hdr sticky top-0 z-40 flex h-20 items-center gap-6 border-b border-transparent bg-tsn06-bg px-[max(1.25rem,calc((100%-72rem)/2))] transition-[height,background-color,box-shadow,border-color] duration-300 ease-out data-scrolled:h-13 data-scrolled:border-tsn06-line data-scrolled:bg-tsn06-bg/85 data-scrolled:shadow-[0_8px_24px_-12px_rgb(60_30_20/0.25)] data-scrolled:backdrop-blur-xl motion-reduce:transition-none">
    <a href="#tsn-06-s1" class="flex min-h-11 items-center gap-3 rounded-lg focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tsn06-acc">
      <span aria-hidden="true" class="grid size-10 place-items-center rounded-xl bg-tsn06-acc text-lg font-extrabold text-tsn06-bg transition-[width,height,border-radius] duration-300 group-data-scrolled/hdr:size-8 group-data-scrolled/hdr:rounded-lg motion-reduce:transition-none">L</span>
      <span class="text-xl font-bold tracking-[-0.03em] transition-[font-size] duration-300 group-data-scrolled/hdr:text-base motion-reduce:transition-none">Lumen Studio</span>
    </a>
    <span aria-hidden="true" class="rounded-full bg-tsn06-ink/6 px-2.5 py-1 font-tsn06-mono text-[11px] text-tsn06-mut max-sm:hidden"><span class="group-data-scrolled/hdr:hidden">h-20 · 80px</span><span class="hidden group-data-scrolled/hdr:inline">h-13 · 52px</span></span>
    <nav aria-label="Primary" class="ms-auto flex gap-1 max-md:hidden">
      <a href="#tsn-06-s1" aria-current="page" class="inline-flex min-h-11 items-center rounded-full px-4 text-sm font-semibold text-tsn06-mut hover:text-tsn06-ink focus-visible:outline-2 focus-visible:outline-tsn06-acc aria-[current=page]:text-tsn06-acc">Work</a>
      <a href="#tsn-06-s2" class="inline-flex min-h-11 items-center rounded-full px-4 text-sm font-semibold text-tsn06-mut hover:text-tsn06-ink focus-visible:outline-2 focus-visible:outline-tsn06-acc">Services</a>
      <a href="#tsn-06-s3" class="inline-flex min-h-11 items-center rounded-full px-4 text-sm font-semibold text-tsn06-mut hover:text-tsn06-ink focus-visible:outline-2 focus-visible:outline-tsn06-acc">Studio</a>
    </nav>
    <a href="#tsn-06-s4" class="inline-flex min-h-11 items-center rounded-full border-2 border-tsn06-ink px-5 text-sm font-bold transition-[background-color,color,padding] duration-300 hover:bg-tsn06-ink hover:text-tsn06-bg focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsn06-acc group-data-scrolled/hdr:border-tsn06-acc group-data-scrolled/hdr:bg-tsn06-acc group-data-scrolled/hdr:px-4 group-data-scrolled/hdr:text-tsn06-bg max-md:ms-auto">Start a project</a>
  </header>
  <div class="px-[max(1.25rem,calc((100%-72rem)/2))] pt-[clamp(3rem,8vw,6rem)] pb-[clamp(2rem,5vw,3.5rem)]">
    <p class="font-tsn06-mono text-[11.5px] font-medium uppercase tracking-[0.16em] text-tsn06-acc">data-scrolled · h-20 → h-13</p>
    <h1 class="mt-4 max-w-[18ch] text-[clamp(38px,6.4vw,76px)] font-extrabold leading-[0.98] tracking-[-0.045em] text-balance">Big when you arrive, quiet when you read</h1>
    <p class="mt-5 max-w-[54ch] text-[clamp(15px,1.6vw,17px)] leading-relaxed text-tsn06-mut text-pretty">Scroll a little. The header eases from 80px to 52px, the logo tightens, and the outlined CTA fills in — all from one attribute.</p>
  </div>
  <main id="tsn-06-main" class="px-[max(1.25rem,calc((100%-72rem)/2))] grid gap-5 pb-24">
    <section id="tsn-06-s1" class="scroll-mt-20 min-h-[44svh] rounded-[1.75rem] border border-tsn06-line bg-tsn06-surface p-[clamp(1.5rem,4vw,3rem)] shadow-[0_1px_2px_rgb(0_0_0/0.04)]" aria-labelledby="tsn-06-h1">
      <p class="font-tsn06-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn06-acc">Work</p>
      <h2 id="tsn-06-h1" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">One attribute, six transitions</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn06-mut text-pretty">Height, border, background, shadow, logo and CTA all read <code class="rounded-md bg-tsn06-acc/10 px-1.5 py-0.5 font-tsn06-mono text-[0.86em] text-tsn06-ink">data-scrolled</code> through the <code class="rounded-md bg-tsn06-acc/10 px-1.5 py-0.5 font-tsn06-mono text-[0.86em] text-tsn06-ink">group/hdr</code> name. The script never touches a class.</p>
    </section>
    <section id="tsn-06-s2" class="scroll-mt-20 min-h-[44svh] rounded-[1.75rem] border border-tsn06-line bg-tsn06-surface p-[clamp(1.5rem,4vw,3rem)] shadow-[0_1px_2px_rgb(0_0_0/0.04)]" aria-labelledby="tsn-06-h2">
      <p class="font-tsn06-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn06-acc">Services</p>
      <h2 id="tsn-06-h2" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">A dead zone kills the flicker</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn06-mut text-pretty">The bar shrinks past 64px of scroll and only grows back below 8px. The 28px layout shift can never bounce the page across the threshold.</p>
    </section>
    <section id="tsn-06-s3" class="scroll-mt-20 min-h-[44svh] rounded-[1.75rem] border border-tsn06-line bg-tsn06-surface p-[clamp(1.5rem,4vw,3rem)] shadow-[0_1px_2px_rgb(0_0_0/0.04)]" aria-labelledby="tsn-06-h3">
      <p class="font-tsn06-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn06-acc">Studio</p>
      <h2 id="tsn-06-h3" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Throttled to the frame</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn06-mut text-pretty">Scroll events are coalesced into one <code class="rounded-md bg-tsn06-acc/10 px-1.5 py-0.5 font-tsn06-mono text-[0.86em] text-tsn06-ink">requestAnimationFrame</code> callback, so the listener does at most one read per painted frame.</p>
    </section>
    <section id="tsn-06-s4" class="scroll-mt-20 min-h-[44svh] rounded-[1.75rem] border border-tsn06-line bg-tsn06-surface p-[clamp(1.5rem,4vw,3rem)] shadow-[0_1px_2px_rgb(0_0_0/0.04)]" aria-labelledby="tsn-06-h4">
      <p class="font-tsn06-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn06-acc">Contact</p>
      <h2 id="tsn-06-h4" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">The CTA earns emphasis</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn06-mut text-pretty">In the compact state the outlined button fills with the accent: when the header gets smaller, the one action that matters gets louder.</p>
    </section>
  </main>
  <footer class="border-t border-tsn06-line px-[max(1.25rem,calc((100%-72rem)/2))] py-10 font-tsn06-mono text-xs text-tsn06-mut">Tailwind sticky navigation · pattern 06 of 25</footer>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsn06-bg: #fbf6ee;
  --color-tsn06-bg: oklch(0.975 0.013 75);
  --color-tsn06-surface: #fffcf7;
  --color-tsn06-surface: oklch(0.993 0.007 75);
  --color-tsn06-ink: #2a1d17;
  --color-tsn06-ink: oklch(0.25 0.025 45);
  --color-tsn06-mut: #6a5a50;
  --color-tsn06-mut: oklch(0.49 0.03 45);
  --color-tsn06-acc: #d9472b;
  --color-tsn06-acc: oklch(0.6 0.19 35);
  --color-tsn06-line: #2a1d171a;
  --color-tsn06-line: oklch(0.25 0.025 45 / 0.1);
  --font-tsn06-sans: 'Bricolage Grotesque', system-ui, sans-serif;
  --font-tsn06-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, restated in CSS so the page is sized before the browser build compiles. */

.tsn-06 {
  width: 100%;
  min-height: 100svh;
}
/* Smooth anchor jumps live on <html>, outside the markup, so they stay in CSS. */

@media (prefers-reduced-motion: no-preference) {
  :root:has(.tsn-06) {
    scroll-behavior: smooth;
  }
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('.tsn-06').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    const hdr = root.querySelector('[data-tsn06-header]');
    let compact = false, queued = false;
    const update = () => {
      queued = false;
      const y = window.scrollY;
      if (!compact && y > 64) { compact = true; hdr.setAttribute('data-scrolled', ''); }
      else if (compact && y < 8) { compact = false; hdr.removeAttribute('data-scrolled'); }
    };
    window.addEventListener('scroll', () => {
      if (!queued) { queued = true; requestAnimationFrame(update); }
    }, { passive: true });
    update();
  });
})();
```
