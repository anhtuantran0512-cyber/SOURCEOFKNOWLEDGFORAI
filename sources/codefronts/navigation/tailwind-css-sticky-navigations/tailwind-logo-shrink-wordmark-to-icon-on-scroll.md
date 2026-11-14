---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-sticky-navigations/tailwind-logo-shrink-wordmark-to-icon-on-scroll/"
title: "Tailwind Sticky Logo Shrink: Wordmark to Icon on Scroll"
section: "navigation"
category: "tailwind-css-sticky-navigations"
category_name: "Tailwind CSS Sticky Navigations"
description: "The full wordmark greets you; once you scroll, the letters fold away and only the mark remains, freeing room for the nav."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Sticky Logo Shrink: Wordmark to Icon on Scroll
Source: https://codefronts.com/navigation/tailwind-css-sticky-navigations/tailwind-logo-shrink-wordmark-to-icon-on-scroll/

The full wordmark greets you; once you scroll, the letters fold away and only the mark remains, freeing room for the nav. The collapse animates grid-cols-[1fr] to grid-cols-[0fr] — a true width-to-zero transition with no measuring — and the link keeps a stable aria-label, so assistive tech always hears “Orbit Labs”.
## HTML
```html
<div class="tsn-10 w-full min-h-svh bg-tsn10-bg font-tsn10-sans text-tsn10-ink antialiased" aria-label="Wordmark to icon logo morph demo">
  <a href="#tsn-10-main" class="sr-only focus:not-sr-only focus:fixed focus:left-3 focus:top-3 focus:z-[100] focus:rounded-lg focus:bg-tsn10-ink focus:px-4 focus:py-3 focus:text-sm focus:font-semibold focus:text-tsn10-bg">Skip to content</a>
  <header data-tsn10-header class="group/hdr sticky top-0 z-40 flex h-[4.5rem] items-center gap-4 border-b border-tsn10-line bg-tsn10-bg/80 px-[max(1.25rem,calc((100%-72rem)/2))] backdrop-blur-xl transition-[height] duration-300 data-scrolled:h-14 motion-reduce:transition-none sm:gap-8">
    <a href="#tsn-10-s1" aria-label="Orbit Labs home" class="group flex min-h-11 flex-none items-center rounded-lg focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tsn10-acc">
      <svg class="size-9 flex-none text-tsn10-acc transition-transform duration-500 group-hover:rotate-[30deg] motion-reduce:transition-none" viewBox="0 0 36 36" fill="none" aria-hidden="true" focusable="false"><circle cx="18" cy="18" r="6" fill="currentColor"/><ellipse cx="18" cy="18" rx="15" ry="7" stroke="currentColor" stroke-width="2" transform="rotate(-28 18 18)"/><circle cx="30.5" cy="11.5" r="2.5" fill="var(--color-tsn10-acc2)"/></svg>
      <span aria-hidden="true" class="grid grid-cols-[1fr] transition-[grid-template-columns,opacity] duration-500 ease-out group-data-scrolled/hdr:grid-cols-[0fr] group-data-scrolled/hdr:opacity-0 motion-reduce:transition-none">
        <span class="min-w-0 overflow-hidden whitespace-nowrap pl-2.5 text-lg font-extrabold tracking-[-0.03em]">Orbit Labs</span>
      </span>
    </a>
    <nav aria-label="Primary" class="flex min-w-0 flex-1 gap-1 overflow-x-auto [scrollbar-width:none]">
      <a href="#tsn-10-s1" aria-current="page" class="inline-flex min-h-11 flex-none items-center rounded-full px-3.5 text-sm font-semibold text-tsn10-mut hover:text-tsn10-ink focus-visible:outline-2 focus-visible:outline-tsn10-acc aria-[current=page]:bg-tsn10-acc/15 aria-[current=page]:text-tsn10-ink">Missions</a>
      <a href="#tsn-10-s2" class="inline-flex min-h-11 flex-none items-center rounded-full px-3.5 text-sm font-semibold text-tsn10-mut hover:text-tsn10-ink focus-visible:outline-2 focus-visible:outline-tsn10-acc">Research</a>
      <a href="#tsn-10-s3" class="inline-flex min-h-11 flex-none items-center rounded-full px-3.5 text-sm font-semibold text-tsn10-mut hover:text-tsn10-ink focus-visible:outline-2 focus-visible:outline-tsn10-acc">Telemetry</a>
      <a href="#tsn-10-s4" class="inline-flex min-h-11 flex-none items-center rounded-full px-3.5 text-sm font-semibold text-tsn10-mut hover:text-tsn10-ink focus-visible:outline-2 focus-visible:outline-tsn10-acc">Careers</a>
    </nav>
    <a href="#tsn-10-s4" class="inline-flex min-h-11 flex-none items-center rounded-full bg-tsn10-ink px-4 text-sm font-bold text-tsn10-bg hover:bg-tsn10-acc2 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsn10-acc max-sm:hidden">Launch</a>
  </header>
  <div class="px-[max(1.25rem,calc((100%-72rem)/2))] pt-[clamp(3rem,8vw,6rem)] pb-[clamp(2rem,5vw,3.5rem)]">
    <p class="font-tsn10-mono text-[11.5px] font-medium uppercase tracking-[0.16em] text-tsn10-acc">grid-cols-[1fr] → [0fr]</p>
    <h1 class="mt-4 max-w-[18ch] text-[clamp(34px,5.6vw,64px)] font-semibold leading-[1.02] tracking-[-0.035em] text-balance">A logo that steps aside</h1>
    <p class="mt-5 max-w-[54ch] text-[clamp(15px,1.6vw,17px)] leading-relaxed text-tsn10-mut text-pretty">Scroll and watch the brand. The wordmark folds into the mark, the bar tightens, and the nav gets the room it needs on small screens.</p>
  </div>
  <main id="tsn-10-main" class="px-[max(1.25rem,calc((100%-72rem)/2))] grid gap-5 pb-24">
    <section id="tsn-10-s1" class="scroll-mt-20 min-h-[44svh] rounded-[1.75rem] border border-tsn10-line bg-tsn10-surface p-[clamp(1.5rem,4vw,3rem)] shadow-[0_1px_2px_rgb(0_0_0/0.04)]" aria-labelledby="tsn-10-h1">
      <p class="font-tsn10-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn10-acc">Missions</p>
      <h2 id="tsn-10-h1" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Width to zero, no measuring</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn10-mut text-pretty">The wordmark lives in a one-track grid. <code class="rounded-md bg-tsn10-acc/10 px-1.5 py-0.5 font-tsn10-mono text-[0.86em] text-tsn10-ink">grid-cols-[1fr]</code> to <code class="rounded-md bg-tsn10-acc/10 px-1.5 py-0.5 font-tsn10-mono text-[0.86em] text-tsn10-ink">[0fr]</code> interpolates smoothly — no <code class="rounded-md bg-tsn10-acc/10 px-1.5 py-0.5 font-tsn10-mono text-[0.86em] text-tsn10-ink">scrollWidth</code>, no max-width guesswork.</p>
    </section>
    <section id="tsn-10-s2" class="scroll-mt-20 min-h-[44svh] rounded-[1.75rem] border border-tsn10-line bg-tsn10-surface p-[clamp(1.5rem,4vw,3rem)] shadow-[0_1px_2px_rgb(0_0_0/0.04)]" aria-labelledby="tsn-10-h2">
      <p class="font-tsn10-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn10-acc">Research</p>
      <h2 id="tsn-10-h2" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">min-w-0 is the hinge</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn10-mut text-pretty">Grid items refuse to shrink below their content by default. <code class="rounded-md bg-tsn10-acc/10 px-1.5 py-0.5 font-tsn10-mono text-[0.86em] text-tsn10-ink">min-w-0</code> on the text lets the track pull it to nothing while <code class="rounded-md bg-tsn10-acc/10 px-1.5 py-0.5 font-tsn10-mono text-[0.86em] text-tsn10-ink">overflow-hidden</code> clips the letters.</p>
    </section>
    <section id="tsn-10-s3" class="scroll-mt-20 min-h-[44svh] rounded-[1.75rem] border border-tsn10-line bg-tsn10-surface p-[clamp(1.5rem,4vw,3rem)] shadow-[0_1px_2px_rgb(0_0_0/0.04)]" aria-labelledby="tsn-10-h3">
      <p class="font-tsn10-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn10-acc">Telemetry</p>
      <h2 id="tsn-10-h3" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">The name never disappears</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn10-mut text-pretty">The link carries <code class="rounded-md bg-tsn10-acc/10 px-1.5 py-0.5 font-tsn10-mono text-[0.86em] text-tsn10-ink">aria-label="Orbit Labs home"</code> and the visible wordmark is <code class="rounded-md bg-tsn10-acc/10 px-1.5 py-0.5 font-tsn10-mono text-[0.86em] text-tsn10-ink">aria-hidden</code>. Screen readers hear the same name in both states.</p>
    </section>
    <section id="tsn-10-s4" class="scroll-mt-20 min-h-[44svh] rounded-[1.75rem] border border-tsn10-line bg-tsn10-surface p-[clamp(1.5rem,4vw,3rem)] shadow-[0_1px_2px_rgb(0_0_0/0.04)]" aria-labelledby="tsn-10-h4">
      <p class="font-tsn10-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn10-acc">Careers</p>
      <h2 id="tsn-10-h4" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Room where it counts</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn10-mut text-pretty">On a phone, the folded logo frees roughly 110px — enough for the whole nav row to fit without scrolling.</p>
    </section>
  </main>
  <footer class="border-t border-tsn10-line px-[max(1.25rem,calc((100%-72rem)/2))] py-10 font-tsn10-mono text-xs text-tsn10-mut">Tailwind sticky navigation · pattern 10 of 25</footer>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsn10-bg: #0d0b1a;
  --color-tsn10-bg: oklch(0.16 0.03 290);
  --color-tsn10-surface: #151229;
  --color-tsn10-surface: oklch(0.2 0.04 290);
  --color-tsn10-ink: #efecff;
  --color-tsn10-ink: oklch(0.95 0.02 290);
  --color-tsn10-mut: #a9a3c7;
  --color-tsn10-mut: oklch(0.74 0.04 290);
  --color-tsn10-acc: #9b8cff;
  --color-tsn10-acc: oklch(0.7 0.16 285);
  --color-tsn10-acc2: #ff9d6b;
  --color-tsn10-acc2: oklch(0.78 0.14 45);
  --color-tsn10-line: #efecff1a;
  --color-tsn10-line: oklch(0.95 0.02 290 / 0.1);
  --font-tsn10-sans: 'Manrope', system-ui, sans-serif;
  --font-tsn10-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, restated in CSS so the page is sized before the browser build compiles. */

.tsn-10 {
  width: 100%;
  min-height: 100svh;
}
/* Smooth anchor jumps live on <html>, outside the markup, so they stay in CSS. */

@media (prefers-reduced-motion: no-preference) {
  :root:has(.tsn-10) {
    scroll-behavior: smooth;
  }
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('.tsn-10').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    const hdr = root.querySelector('[data-tsn10-header]');
    let on = false, queued = false;
    const update = () => {
      queued = false;
      const y = window.scrollY;
      if (!on && y > 80) { on = true; hdr.setAttribute('data-scrolled', ''); }
      else if (on && y < 12) { on = false; hdr.removeAttribute('data-scrolled'); }
    };
    window.addEventListener('scroll', () => {
      if (!queued) { queued = true; requestAnimationFrame(update); }
    }, { passive: true });
    update();
  });
})();
```
