---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-sticky-navigations/responsive-tailwind-sticky-navbar-hamburger-menu/"
title: "Responsive Tailwind Sticky Navbar with Hamburger Menu"
section: "navigation"
category: "tailwind-css-sticky-navigations"
category_name: "Tailwind CSS Sticky Navigations"
description: "The responsive header with a hamburger that morphs into an X and a menu that opens by animating grid-rows-[0fr] to grid-rows-[1fr] — true height animation…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Responsive Tailwind Sticky Navbar with Hamburger Menu
Source: https://codefronts.com/navigation/tailwind-css-sticky-navigations/responsive-tailwind-sticky-navbar-hamburger-menu/

The responsive header with a hamburger that morphs into an X and a menu that opens by animating grid-rows-[0fr] to grid-rows-[1fr] — true height animation without measuring. A nine-line script sets one data-open attribute; every visual state is a group-data-open/hdr: variant. Escape closes, focus returns, and the closed panel is inert.
## HTML
```html
<div class="tsn-03 w-full min-h-svh bg-tsn03-bg font-tsn03-sans text-tsn03-ink antialiased" aria-label="Responsive Tailwind hamburger navbar demo">
  <header data-tsn03-header class="group/hdr sticky top-0 z-40 border-b border-tsn03-line bg-tsn03-bg/85 backdrop-blur-xl">
    <div class="flex h-16 items-center gap-6 px-[max(1.25rem,calc((100%-72rem)/2))]">
      <a href="#tsn-03-s1" class="flex min-h-11 items-center gap-2 rounded-lg text-lg font-bold tracking-[-0.03em] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tsn03-acc"><span aria-hidden="true" class="size-3 rotate-45 rounded-[3px] bg-tsn03-acc"></span>Fieldnote</a>
      <nav aria-label="Primary" class="ms-auto flex gap-1 max-md:hidden">
        <a href="#tsn-03-s1" aria-current="page" class="inline-flex min-h-11 items-center rounded-full px-4 text-sm font-medium text-tsn03-mut hover:text-tsn03-ink focus-visible:outline-2 focus-visible:outline-tsn03-acc aria-[current=page]:bg-tsn03-ink/8 aria-[current=page]:text-tsn03-ink">Journal</a>
        <a href="#tsn-03-s2" class="inline-flex min-h-11 items-center rounded-full px-4 text-sm font-medium text-tsn03-mut hover:text-tsn03-ink focus-visible:outline-2 focus-visible:outline-tsn03-acc">Templates</a>
        <a href="#tsn-03-s3" class="inline-flex min-h-11 items-center rounded-full px-4 text-sm font-medium text-tsn03-mut hover:text-tsn03-ink focus-visible:outline-2 focus-visible:outline-tsn03-acc">Sync</a>
        <a href="#tsn-03-s4" class="inline-flex min-h-11 items-center rounded-full px-4 text-sm font-medium text-tsn03-mut hover:text-tsn03-ink focus-visible:outline-2 focus-visible:outline-tsn03-acc">Pricing</a>
      </nav>
      <a href="#tsn-03-s4" class="inline-flex min-h-11 items-center rounded-full bg-tsn03-acc px-5 text-sm font-bold text-tsn03-bg transition hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsn03-acc max-md:ms-auto max-sm:hidden">Get the app</a>
      <button type="button" data-tsn03-toggle aria-expanded="false" aria-controls="tsn-03-menu" class="relative grid size-11 place-items-center rounded-full border border-tsn03-line hover:bg-tsn03-ink/5 focus-visible:outline-2 focus-visible:outline-tsn03-acc max-sm:ms-auto md:hidden">
        <span class="sr-only">Menu</span>
        <span aria-hidden="true" class="absolute h-0.5 w-5 -translate-y-1.5 rounded-full bg-current transition-transform duration-300 group-data-open/hdr:translate-y-0 group-data-open/hdr:rotate-45 motion-reduce:transition-none"></span>
        <span aria-hidden="true" class="absolute h-0.5 w-5 rounded-full bg-current transition-opacity group-data-open/hdr:opacity-0"></span>
        <span aria-hidden="true" class="absolute h-0.5 w-5 translate-y-1.5 rounded-full bg-current transition-transform duration-300 group-data-open/hdr:translate-y-0 group-data-open/hdr:-rotate-45 motion-reduce:transition-none"></span>
      </button>
    </div>
    <div id="tsn-03-menu" inert class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-300 ease-out group-data-open/hdr:grid-rows-[1fr] motion-reduce:transition-none md:hidden">
      <div class="min-h-0 overflow-hidden">
        <nav aria-label="Mobile" class="grid gap-1 px-5 pb-6 pt-2">
          <a href="#tsn-03-s1" class="flex min-h-14 items-center justify-between border-b border-tsn03-line text-2xl font-semibold tracking-tight opacity-0 transition-[opacity,translate] delay-75 duration-300 -translate-y-1 group-data-open/hdr:translate-y-0 group-data-open/hdr:opacity-100 focus-visible:outline-2 focus-visible:outline-tsn03-acc">Journal<span aria-hidden="true" class="text-tsn03-acc">01</span></a>
          <a href="#tsn-03-s2" class="flex min-h-14 items-center justify-between border-b border-tsn03-line text-2xl font-semibold tracking-tight opacity-0 transition-[opacity,translate] delay-100 duration-300 -translate-y-1 group-data-open/hdr:translate-y-0 group-data-open/hdr:opacity-100 focus-visible:outline-2 focus-visible:outline-tsn03-acc">Templates<span aria-hidden="true" class="text-tsn03-acc">02</span></a>
          <a href="#tsn-03-s3" class="flex min-h-14 items-center justify-between border-b border-tsn03-line text-2xl font-semibold tracking-tight opacity-0 transition-[opacity,translate] delay-150 duration-300 -translate-y-1 group-data-open/hdr:translate-y-0 group-data-open/hdr:opacity-100 focus-visible:outline-2 focus-visible:outline-tsn03-acc">Sync<span aria-hidden="true" class="text-tsn03-acc">03</span></a>
          <a href="#tsn-03-s4" class="flex min-h-14 items-center justify-between border-b border-tsn03-line text-2xl font-semibold tracking-tight opacity-0 transition-[opacity,translate] delay-200 duration-300 -translate-y-1 group-data-open/hdr:translate-y-0 group-data-open/hdr:opacity-100 focus-visible:outline-2 focus-visible:outline-tsn03-acc">Pricing<span aria-hidden="true" class="text-tsn03-acc">04</span></a>
          <a href="#tsn-03-s4" class="mt-4 inline-flex min-h-12 items-center justify-center rounded-full bg-tsn03-acc text-base font-bold text-tsn03-bg sm:hidden">Get the app</a>
        </nav>
      </div>
    </div>
  </header>
  <div class="px-[max(1.25rem,calc((100%-72rem)/2))] pt-[clamp(3rem,8vw,6rem)] pb-[clamp(2rem,5vw,3.5rem)]">
    <p class="font-tsn03-mono text-[11.5px] font-medium uppercase tracking-[0.16em] text-tsn03-acc">group-data-open · grid-rows-[1fr]</p>
    <h1 class="mt-4 max-w-[18ch] text-[clamp(34px,5.6vw,64px)] font-semibold leading-[1.02] tracking-[-0.035em] text-balance">A hamburger that earns its place</h1>
    <p class="mt-5 max-w-[54ch] text-[clamp(15px,1.6vw,17px)] leading-relaxed text-tsn03-mut text-pretty">Narrow the window below 768px and open the menu. It pushes down with a real height animation, staggers its links in, and closes on Escape.</p>
  </div>
  <main id="tsn-03-main" class="px-[max(1.25rem,calc((100%-72rem)/2))] grid gap-5 pb-24">
    <section id="tsn-03-s1" class="scroll-mt-24 min-h-[44svh] rounded-[1.75rem] border border-tsn03-line bg-tsn03-surface p-[clamp(1.5rem,4vw,3rem)] shadow-[0_1px_2px_rgb(0_0_0/0.04)]" aria-labelledby="tsn-03-h1">
      <p class="font-tsn03-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn03-acc">Journal</p>
      <h2 id="tsn-03-h1" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Height to auto, without measuring</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn03-mut text-pretty">The panel animates <code class="rounded-md bg-tsn03-acc/10 px-1.5 py-0.5 font-tsn03-mono text-[0.86em] text-tsn03-ink">grid-rows-[0fr]</code> to <code class="rounded-md bg-tsn03-acc/10 px-1.5 py-0.5 font-tsn03-mono text-[0.86em] text-tsn03-ink">[1fr]</code>. The browser interpolates the track; no <code class="rounded-md bg-tsn03-acc/10 px-1.5 py-0.5 font-tsn03-mono text-[0.86em] text-tsn03-ink">scrollHeight</code> reads, no magic max-height.</p>
    </section>
    <section id="tsn-03-s2" class="scroll-mt-24 min-h-[44svh] rounded-[1.75rem] border border-tsn03-line bg-tsn03-surface p-[clamp(1.5rem,4vw,3rem)] shadow-[0_1px_2px_rgb(0_0_0/0.04)]" aria-labelledby="tsn-03-h2">
      <p class="font-tsn03-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn03-acc">Templates</p>
      <h2 id="tsn-03-h2" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">One attribute, every state</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn03-mut text-pretty">The script toggles <code class="rounded-md bg-tsn03-acc/10 px-1.5 py-0.5 font-tsn03-mono text-[0.86em] text-tsn03-ink">data-open</code>. The X morph, the panel and the stagger are all <code class="rounded-md bg-tsn03-acc/10 px-1.5 py-0.5 font-tsn03-mono text-[0.86em] text-tsn03-ink">group-data-open/hdr:</code> variants in the markup.</p>
    </section>
    <section id="tsn-03-s3" class="scroll-mt-24 min-h-[44svh] rounded-[1.75rem] border border-tsn03-line bg-tsn03-surface p-[clamp(1.5rem,4vw,3rem)] shadow-[0_1px_2px_rgb(0_0_0/0.04)]" aria-labelledby="tsn-03-h3">
      <p class="font-tsn03-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn03-acc">Sync</p>
      <h2 id="tsn-03-h3" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Closed means unreachable</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn03-mut text-pretty">A collapsed panel is <code class="rounded-md bg-tsn03-acc/10 px-1.5 py-0.5 font-tsn03-mono text-[0.86em] text-tsn03-ink">inert</code>, so its links leave the tab order and the accessibility tree until the menu opens.</p>
    </section>
    <section id="tsn-03-s4" class="scroll-mt-24 min-h-[44svh] rounded-[1.75rem] border border-tsn03-line bg-tsn03-surface p-[clamp(1.5rem,4vw,3rem)] shadow-[0_1px_2px_rgb(0_0_0/0.04)]" aria-labelledby="tsn-03-h4">
      <p class="font-tsn03-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn03-acc">Pricing</p>
      <h2 id="tsn-03-h4" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Escape always works</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn03-mut text-pretty">Escape closes the menu and returns focus to the toggle. Tapping a link closes it too, so the anchor lands on an uncovered page.</p>
    </section>
  </main>
  <footer class="border-t border-tsn03-line px-[max(1.25rem,calc((100%-72rem)/2))] py-10 font-tsn03-mono text-xs text-tsn03-mut">Tailwind sticky navigation · pattern 03 of 25</footer>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsn03-bg: #0f1110;
  --color-tsn03-bg: oklch(0.17 0.006 150);
  --color-tsn03-surface: #171a18;
  --color-tsn03-surface: oklch(0.21 0.008 150);
  --color-tsn03-ink: #eef2ea;
  --color-tsn03-ink: oklch(0.95 0.012 130);
  --color-tsn03-mut: #a3aa9d;
  --color-tsn03-mut: oklch(0.72 0.018 130);
  --color-tsn03-acc: #c6f24e;
  --color-tsn03-acc: oklch(0.9 0.19 125);
  --color-tsn03-line: #eef2ea1f;
  --color-tsn03-line: oklch(0.95 0.012 130 / 0.12);
  --font-tsn03-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tsn03-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, restated in CSS so the page is sized before the browser build compiles. */

.tsn-03 {
  width: 100%;
  min-height: 100svh;
}
/* Smooth anchor jumps live on <html>, outside the markup, so they stay in CSS. */

@media (prefers-reduced-motion: no-preference) {
  :root:has(.tsn-03) {
    scroll-behavior: smooth;
  }
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('.tsn-03').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    const hdr = root.querySelector('[data-tsn03-header]');
    const btn = root.querySelector('[data-tsn03-toggle]');
    const panel = root.querySelector('#tsn-03-menu');
    const set = (open) => {
      hdr.toggleAttribute('data-open', open);
      btn.setAttribute('aria-expanded', String(open));
      panel.inert = !open;
    };
    btn.addEventListener('click', () => set(!hdr.hasAttribute('data-open')));
    panel.addEventListener('click', (e) => { if (e.target.closest('a')) set(false); });
    root.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && hdr.hasAttribute('data-open')) { set(false); btn.focus(); }
    });
    matchMedia('(min-width: 768px)').addEventListener('change', (e) => { if (e.matches) set(false); });
  });
})();
```
