---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-sticky-navigations/tailwind-navbar-sliding-underline-active-link/"
title: "Tailwind Navbar with Sliding Underline Active Link"
section: "navigation"
category: "tailwind-css-sticky-navigations"
category_name: "Tailwind CSS Sticky Navigations"
description: "One accent bar glides beneath the nav — following your pointer and keyboard focus, then settling back on the current page when you leave."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Navbar with Sliding Underline Active Link
Source: https://codefronts.com/navigation/tailwind-css-sticky-navigations/tailwind-navbar-sliding-underline-active-link/

One accent bar glides beneath the nav — following your pointer and keyboard focus, then settling back on the current page when you leave. The bar is positioned by two custom properties consumed with v4's shorthand, w-(--tsn11-w) translate-x-(--tsn11-x), so the script only measures; Tailwind owns the motion.
## HTML
```html
<div class="tsn-11 w-full min-h-svh bg-tsn11-bg font-tsn11-sans text-tsn11-ink antialiased" aria-label="Sliding underline active link navbar demo">
  <a href="#tsn-11-main" class="sr-only focus:not-sr-only focus:fixed focus:left-3 focus:top-3 focus:z-[100] focus:rounded-lg focus:bg-tsn11-ink focus:px-4 focus:py-3 focus:text-sm focus:font-semibold focus:text-tsn11-bg">Skip to content</a>
  <header class="sticky top-0 z-40 flex h-16 items-center gap-6 border-b border-tsn11-line bg-tsn11-bg/85 px-[max(1.25rem,calc((100%-72rem)/2))] backdrop-blur-xl">
    <a href="#tsn-11-s1" class="flex min-h-11 flex-none items-center gap-2 rounded-lg font-semibold tracking-tight focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tsn11-acc"><span aria-hidden="true" class="h-4 w-1.5 skew-x-[-14deg] rounded-sm bg-tsn11-acc shadow-[6px_0_0_color-mix(in_oklab,var(--color-tsn11-acc)_45%,transparent)]"></span><span class="pl-2">Kinetic</span></a>
    <nav data-tsn11-nav aria-label="Primary" style="--tsn11-x:0px;--tsn11-w:0px" class="relative mx-auto flex min-w-0 gap-1 overflow-x-auto [scrollbar-width:none]">
      <a href="#tsn-11-s1" aria-current="page" class="inline-flex min-h-11 flex-none items-center px-4 text-sm font-medium text-tsn11-mut transition-colors hover:text-tsn11-ink focus-visible:text-tsn11-ink focus-visible:outline-none aria-[current=page]:text-tsn11-ink">Overview</a>
      <a href="#tsn-11-s2" class="inline-flex min-h-11 flex-none items-center px-4 text-sm font-medium text-tsn11-mut transition-colors hover:text-tsn11-ink focus-visible:text-tsn11-ink focus-visible:outline-none aria-[current=page]:text-tsn11-ink">Engine</a>
      <a href="#tsn-11-s3" class="inline-flex min-h-11 flex-none items-center px-4 text-sm font-medium text-tsn11-mut transition-colors hover:text-tsn11-ink focus-visible:text-tsn11-ink focus-visible:outline-none aria-[current=page]:text-tsn11-ink">Integrations</a>
      <a href="#tsn-11-s4" class="inline-flex min-h-11 flex-none items-center px-4 text-sm font-medium text-tsn11-mut transition-colors hover:text-tsn11-ink focus-visible:text-tsn11-ink focus-visible:outline-none aria-[current=page]:text-tsn11-ink">Pricing</a>
      <span data-tsn11-ind aria-hidden="true" class="pointer-events-none absolute bottom-1.5 left-0 h-[3px] w-(--tsn11-w) translate-x-(--tsn11-x) rounded-full bg-tsn11-acc shadow-[0_0_14px_var(--color-tsn11-acc)] transition-[translate,width] duration-300 ease-[cubic-bezier(0.2,0.8,0.2,1)] motion-reduce:transition-none"></span>
    </nav>
    <a href="#tsn-11-s4" class="inline-flex min-h-11 flex-none items-center rounded-lg bg-tsn11-acc px-4 text-sm font-semibold text-tsn11-bg hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsn11-acc max-sm:hidden">Try Kinetic</a>
  </header>
  <div class="px-[max(1.25rem,calc((100%-72rem)/2))] pt-[clamp(3rem,8vw,6rem)] pb-[clamp(2rem,5vw,3.5rem)]">
    <p class="font-tsn11-mono text-[11.5px] font-medium uppercase tracking-[0.16em] text-tsn11-acc">w-(--tsn11-w) · translate-x-(--tsn11-x)</p>
    <h1 class="mt-4 max-w-[18ch] text-[clamp(34px,5.6vw,64px)] font-semibold leading-[1.02] tracking-[-0.035em] text-balance">An indicator with somewhere to be</h1>
    <p class="mt-5 max-w-[54ch] text-[clamp(15px,1.6vw,17px)] leading-relaxed text-tsn11-mut text-pretty">Hover across the nav, or Tab through it. The line follows you, then glides home to the current page when you leave. Click a link to move “home”.</p>
  </div>
  <main id="tsn-11-main" class="px-[max(1.25rem,calc((100%-72rem)/2))] grid gap-5 pb-24">
    <section id="tsn-11-s1" class="scroll-mt-24 min-h-[44svh] rounded-[1.75rem] border border-tsn11-line bg-tsn11-surface p-[clamp(1.5rem,4vw,3rem)] shadow-[0_1px_2px_rgb(0_0_0/0.04)]" aria-labelledby="tsn-11-h1">
      <p class="font-tsn11-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn11-acc">Overview</p>
      <h2 id="tsn-11-h1" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Measure in JS, move in CSS</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn11-mut text-pretty">The script writes two numbers to the nav. <code class="rounded-md bg-tsn11-acc/10 px-1.5 py-0.5 font-tsn11-mono text-[0.86em] text-tsn11-ink">w-(--tsn11-w)</code> and <code class="rounded-md bg-tsn11-acc/10 px-1.5 py-0.5 font-tsn11-mono text-[0.86em] text-tsn11-ink">translate-x-(--tsn11-x)</code> turn them into motion — v4’s shorthand for a utility bound to a custom property.</p>
    </section>
    <section id="tsn-11-s2" class="scroll-mt-24 min-h-[44svh] rounded-[1.75rem] border border-tsn11-line bg-tsn11-surface p-[clamp(1.5rem,4vw,3rem)] shadow-[0_1px_2px_rgb(0_0_0/0.04)]" aria-labelledby="tsn-11-h2">
      <p class="font-tsn11-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn11-acc">Engine</p>
      <h2 id="tsn-11-h2" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Keyboard moves it too</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn11-mut text-pretty">Focus is treated exactly like hover. The visible focus cue is the bar plus the brightened label, so the default outline can step aside without leaving keyboard users blind.</p>
    </section>
    <section id="tsn-11-s3" class="scroll-mt-24 min-h-[44svh] rounded-[1.75rem] border border-tsn11-line bg-tsn11-surface p-[clamp(1.5rem,4vw,3rem)] shadow-[0_1px_2px_rgb(0_0_0/0.04)]" aria-labelledby="tsn-11-h3">
      <p class="font-tsn11-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn11-acc">Integrations</p>
      <h2 id="tsn-11-h3" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Always home again</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn11-mut text-pretty">Leave the nav and the line returns to <code class="rounded-md bg-tsn11-acc/10 px-1.5 py-0.5 font-tsn11-mono text-[0.86em] text-tsn11-ink">aria-current="page"</code>. The current page is never ambiguous, even mid-gesture.</p>
    </section>
    <section id="tsn-11-s4" class="scroll-mt-24 min-h-[44svh] rounded-[1.75rem] border border-tsn11-line bg-tsn11-surface p-[clamp(1.5rem,4vw,3rem)] shadow-[0_1px_2px_rgb(0_0_0/0.04)]" aria-labelledby="tsn-11-h4">
      <p class="font-tsn11-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn11-acc">Pricing</p>
      <h2 id="tsn-11-h4" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Re-measured on change</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn11-mut text-pretty">A <code class="rounded-md bg-tsn11-acc/10 px-1.5 py-0.5 font-tsn11-mono text-[0.86em] text-tsn11-ink">ResizeObserver</code> and <code class="rounded-md bg-tsn11-acc/10 px-1.5 py-0.5 font-tsn11-mono text-[0.86em] text-tsn11-ink">document.fonts.ready</code> keep the bar exact when the window resizes or the web font swaps in.</p>
    </section>
  </main>
  <footer class="border-t border-tsn11-line px-[max(1.25rem,calc((100%-72rem)/2))] py-10 font-tsn11-mono text-xs text-tsn11-mut">Tailwind sticky navigation · pattern 11 of 25</footer>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsn11-bg: #121214;
  --color-tsn11-bg: oklch(0.19 0.004 285);
  --color-tsn11-surface: #1a1a1e;
  --color-tsn11-surface: oklch(0.225 0.006 285);
  --color-tsn11-ink: #f2f1ee;
  --color-tsn11-ink: oklch(0.96 0.004 90);
  --color-tsn11-mut: #a3a2a8;
  --color-tsn11-mut: oklch(0.72 0.008 285);
  --color-tsn11-acc: #ffb224;
  --color-tsn11-acc: oklch(0.82 0.16 75);
  --color-tsn11-line: #f2f1ee1a;
  --color-tsn11-line: oklch(0.96 0.004 90 / 0.1);
  --font-tsn11-sans: 'Sora', system-ui, sans-serif;
  --font-tsn11-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, restated in CSS so the page is sized before the browser build compiles. */

.tsn-11 {
  width: 100%;
  min-height: 100svh;
}
/* Smooth anchor jumps live on <html>, outside the markup, so they stay in CSS. */

@media (prefers-reduced-motion: no-preference) {
  :root:has(.tsn-11) {
    scroll-behavior: smooth;
  }
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('.tsn-11').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    const nav = root.querySelector('[data-tsn11-nav]');
    const links = [...nav.querySelectorAll('a')];
    const current = () => links.find((l) => l.getAttribute('aria-current') === 'page') || links[0];
    const move = (a) => {
      nav.style.setProperty('--tsn11-x', a.offsetLeft + 'px');
      nav.style.setProperty('--tsn11-w', a.offsetWidth + 'px');
    };
    links.forEach((a) => {
      a.addEventListener('pointerenter', () => move(a));
      a.addEventListener('focus', () => move(a));
      a.addEventListener('click', () => {
        links.forEach((l) => l.removeAttribute('aria-current'));
        a.setAttribute('aria-current', 'page');
        move(a);
      });
    });
    nav.addEventListener('pointerleave', () => move(current()));
    nav.addEventListener('focusout', (e) => { if (!nav.contains(e.relatedTarget)) move(current()); });
    new ResizeObserver(() => move(current())).observe(nav);
    if (document.fonts) document.fonts.ready.then(() => move(current()));
    move(current());
  });
})();
```
