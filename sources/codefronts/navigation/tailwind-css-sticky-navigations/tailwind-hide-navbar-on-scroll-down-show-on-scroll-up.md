---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-sticky-navigations/tailwind-hide-navbar-on-scroll-down-show-on-scroll-up/"
title: "Tailwind Hide on Scroll Down, Show on Scroll Up Navbar"
section: "navigation"
category: "tailwind-css-sticky-navigations"
category_name: "Tailwind CSS Sticky Navigations"
description: "The “headroom” header news sites use: it slides away as you read down and returns the instant you scroll up."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Hide on Scroll Down, Show on Scroll Up Navbar
Source: https://codefronts.com/navigation/tailwind-css-sticky-navigations/tailwind-hide-navbar-on-scroll-down-show-on-scroll-up/

The “headroom” header news sites use: it slides away as you read down and returns the instant you scroll up. data-hidden:-translate-y-full moves it on the compositor, a 6px delta filter ignores trackpad jitter, and keyboard focus always brings it back — a gap most hide-on-scroll scripts leave open.
## HTML
```html
<div class="tsn-07 w-full min-h-svh bg-tsn07-bg font-tsn07-serif text-tsn07-ink antialiased" aria-label="Hide on scroll down, show on scroll up navbar demo">
  <a href="#tsn-07-main" class="sr-only focus:not-sr-only focus:fixed focus:left-3 focus:top-3 focus:z-[100] focus:rounded-lg focus:bg-tsn07-ink focus:px-4 focus:py-3 focus:text-sm focus:font-semibold focus:text-tsn07-bg">Skip to content</a>
  <header data-tsn07-header class="sticky top-0 z-40 border-b border-tsn07-ink bg-tsn07-bg/95 backdrop-blur-md transition-transform duration-300 ease-out data-hidden:-translate-y-full motion-reduce:transition-none">
    <div class="flex h-16 items-center gap-6 px-[max(1.25rem,calc((100%-72rem)/2))]">
      <a href="#tsn-07-s1" class="flex min-h-11 items-center rounded text-[26px] font-semibold italic tracking-[-0.02em] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tsn07-acc">The Tidewater</a>
      <nav aria-label="Sections" class="flex min-w-0 flex-1 gap-0.5 overflow-x-auto font-tsn07-sans [scrollbar-width:none]">
        <a href="#tsn-07-s1" aria-current="page" class="inline-flex min-h-11 flex-none items-center px-3 text-[13px] font-semibold uppercase tracking-[0.08em] text-tsn07-mut hover:text-tsn07-ink focus-visible:outline-2 focus-visible:outline-tsn07-acc aria-[current=page]:text-tsn07-acc">World</a>
        <a href="#tsn-07-s2" class="inline-flex min-h-11 flex-none items-center px-3 text-[13px] font-semibold uppercase tracking-[0.08em] text-tsn07-mut hover:text-tsn07-ink focus-visible:outline-2 focus-visible:outline-tsn07-acc">Climate</a>
        <a href="#tsn-07-s3" class="inline-flex min-h-11 flex-none items-center px-3 text-[13px] font-semibold uppercase tracking-[0.08em] text-tsn07-mut hover:text-tsn07-ink focus-visible:outline-2 focus-visible:outline-tsn07-acc">Culture</a>
        <a href="#tsn-07-s4" class="inline-flex min-h-11 flex-none items-center px-3 text-[13px] font-semibold uppercase tracking-[0.08em] text-tsn07-mut hover:text-tsn07-ink focus-visible:outline-2 focus-visible:outline-tsn07-acc">Opinion</a>
      </nav>
      <a href="#tsn-07-s4" class="inline-flex min-h-11 flex-none items-center rounded-sm bg-tsn07-acc px-4 font-tsn07-sans text-sm font-bold text-white hover:bg-tsn07-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsn07-acc">Subscribe</a>
    </div>
  </header>
  <div class="px-[max(1.25rem,calc((100%-48rem)/2))] pt-[clamp(3rem,8vw,6rem)] pb-[clamp(2rem,5vw,3.5rem)]">
    <p class="font-tsn07-mono text-[11.5px] font-medium uppercase tracking-[0.16em] text-tsn07-acc">data-hidden · -translate-y-full</p>
    <h1 class="mt-4 max-w-[18ch] text-[clamp(36px,6vw,68px)] font-medium leading-[1.02] tracking-[-0.025em] text-balance">The header that knows when to leave</h1>
    <p class="mt-5 max-w-[54ch] text-[clamp(15px,1.6vw,17px)] leading-relaxed text-tsn07-mut text-pretty">Read down and the masthead slides away. Flick up a few pixels and it is back. Tab with the keyboard and it never hides a focused link.</p>
  </div>
  <main id="tsn-07-main" class="px-[max(1.25rem,calc((100%-48rem)/2))] grid pb-24">
    <section id="tsn-07-s1" class="scroll-mt-24 min-h-[48svh] border-t border-tsn07-line py-[clamp(2.5rem,6vw,4.5rem)]" aria-labelledby="tsn-07-h1">
      <p class="font-tsn07-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn07-acc">World</p>
      <h2 id="tsn-07-h1" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Direction beats position</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn07-mut text-pretty">The script compares this frame’s scroll with the last committed one. Down by 6px or more hides, up by 6px reveals. Everything under 6px is trackpad noise and ignored.</p>
    </section>
    <section id="tsn-07-s2" class="scroll-mt-24 min-h-[48svh] border-t border-tsn07-line py-[clamp(2.5rem,6vw,4.5rem)]" aria-labelledby="tsn-07-h2">
      <p class="font-tsn07-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn07-acc">Climate</p>
      <h2 id="tsn-07-h2" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Slide, never reflow</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn07-mut text-pretty">Hiding is <code class="rounded-md bg-tsn07-acc/10 px-1.5 py-0.5 font-tsn07-mono text-[0.86em] text-tsn07-ink">-translate-y-full</code> on the compositor. The bar leaves its sticky slot without moving a single line of the article beneath it.</p>
    </section>
    <section id="tsn-07-s3" class="scroll-mt-24 min-h-[48svh] border-t border-tsn07-line py-[clamp(2.5rem,6vw,4.5rem)]" aria-labelledby="tsn-07-h3">
      <p class="font-tsn07-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn07-acc">Culture</p>
      <h2 id="tsn-07-h3" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Focus always wins</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn07-mut text-pretty">A <code class="rounded-md bg-tsn07-acc/10 px-1.5 py-0.5 font-tsn07-mono text-[0.86em] text-tsn07-ink">focusin</code> listener clears <code class="rounded-md bg-tsn07-acc/10 px-1.5 py-0.5 font-tsn07-mono text-[0.86em] text-tsn07-ink">data-hidden</code>, so keyboard users can never tab into a link that is off-screen.</p>
    </section>
    <section id="tsn-07-s4" class="scroll-mt-24 min-h-[48svh] border-t border-tsn07-line py-[clamp(2.5rem,6vw,4.5rem)]" aria-labelledby="tsn-07-h4">
      <p class="font-tsn07-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn07-acc">Opinion</p>
      <h2 id="tsn-07-h4" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Calm motion on request</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn07-mut text-pretty">Under <code class="rounded-md bg-tsn07-acc/10 px-1.5 py-0.5 font-tsn07-mono text-[0.86em] text-tsn07-ink">motion-reduce</code> the slide becomes a snap. The behaviour stays; the movement goes.</p>
    </section>
  </main>
  <footer class="border-t border-tsn07-line px-[max(1.25rem,calc((100%-48rem)/2))] py-10 font-tsn07-mono text-xs text-tsn07-mut">Tailwind sticky navigation · pattern 07 of 25</footer>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsn07-bg: #f7f4ee;
  --color-tsn07-bg: oklch(0.966 0.01 85);
  --color-tsn07-surface: #fffdf9;
  --color-tsn07-surface: oklch(0.995 0.005 85);
  --color-tsn07-ink: #161a24;
  --color-tsn07-ink: oklch(0.2 0.02 265);
  --color-tsn07-mut: #535868;
  --color-tsn07-mut: oklch(0.45 0.022 265);
  --color-tsn07-acc: #1f4fa8;
  --color-tsn07-acc: oklch(0.45 0.15 262);
  --color-tsn07-line: #161a2426;
  --color-tsn07-line: oklch(0.2 0.02 265 / 0.15);
  --font-tsn07-serif: 'Newsreader', Georgia, serif;
  --font-tsn07-sans: 'Geist', system-ui, sans-serif;
  --font-tsn07-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, restated in CSS so the page is sized before the browser build compiles. */

.tsn-07 {
  width: 100%;
  min-height: 100svh;
}
/* Smooth anchor jumps live on <html>, outside the markup, so they stay in CSS. */

@media (prefers-reduced-motion: no-preference) {
  :root:has(.tsn-07) {
    scroll-behavior: smooth;
  }
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('.tsn-07').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    const hdr = root.querySelector('[data-tsn07-header]');
    let last = Math.max(0, window.scrollY), queued = false;
    const update = () => {
      queued = false;
      const y = Math.max(0, window.scrollY);
      const delta = y - last;
      if (Math.abs(delta) < 6) return;
      const hide = delta > 0 && y > hdr.offsetHeight * 2 && !hdr.contains(document.activeElement);
      hdr.toggleAttribute('data-hidden', hide);
      last = y;
    };
    window.addEventListener('scroll', () => {
      if (!queued) { queued = true; requestAnimationFrame(update); }
    }, { passive: true });
    hdr.addEventListener('focusin', () => hdr.removeAttribute('data-hidden'));
  });
})();
```
