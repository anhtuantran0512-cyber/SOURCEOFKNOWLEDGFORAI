---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-sticky-navigations/tailwind-sticky-announcement-bar-above-navbar/"
title: "Tailwind Sticky Announcement Bar Above Navbar"
section: "navigation"
category: "tailwind-css-sticky-navigations"
category_name: "Tailwind CSS Sticky Navigations"
description: "Two sticky layers that stack and stay: a dismissible announcement at top-0 and the main nav pinned right under it at top-11."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Sticky Announcement Bar Above Navbar
Source: https://codefronts.com/navigation/tailwind-css-sticky-navigations/tailwind-sticky-announcement-bar-above-navbar/

Two sticky layers that stack and stay: a dismissible announcement at top-0 and the main nav pinned right under it at top-11. Dismissing sets one attribute on the root — the banner disappears via group-data-dismissed/root:hidden, the nav slides up to top-0, and section anchor offsets shrink to match. Focus moves to the nav so keyboard users aren't stranded.
## HTML
```html
<div class="tsn-18 group/root w-full min-h-svh bg-tsn18-bg font-tsn18-sans text-tsn18-ink antialiased" aria-label="Sticky announcement bar above navbar demo">
  <div data-tsn18-ann role="region" aria-label="Announcement" class="sticky top-0 z-50 flex h-11 items-center justify-center gap-3 bg-[linear-gradient(90deg,var(--color-tsn18-acc),var(--color-tsn18-acc2))] pl-4 pr-12 text-[13px] text-white group-data-dismissed/root:hidden">
    <span aria-hidden="true" class="rounded-full bg-white/20 px-2 py-0.5 font-tsn18-mono text-[10.5px] font-semibold uppercase tracking-[0.12em] max-sm:hidden">New</span>
    <p class="truncate"><strong class="font-semibold">Polaris 3.0 is live</strong><span class="max-sm:hidden"> — realtime sync on every plan.</span></p>
    <a href="#tsn-18-s2" class="inline-flex min-h-11 flex-none items-center gap-1 font-semibold underline decoration-white/50 underline-offset-4 hover:decoration-white focus-visible:outline-2 focus-visible:outline-white">See what’s new <svg class="size-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
    <button type="button" data-tsn18-close class="absolute right-0.5 grid size-11 place-items-center rounded-full text-white/85 hover:bg-white/15 hover:text-white focus-visible:outline-2 focus-visible:-outline-offset-4 focus-visible:outline-white"><span class="sr-only">Dismiss announcement</span><svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6 6 18"/></svg></button>
  </div>
  <header class="sticky top-11 z-40 flex h-16 items-center gap-6 border-b border-tsn18-line bg-tsn18-bg/85 px-[max(1.25rem,calc((100%-72rem)/2))] backdrop-blur-xl group-data-dismissed/root:top-0">
    <a data-tsn18-brand href="#tsn-18-s1" class="flex min-h-11 flex-none items-center gap-2 rounded-lg font-semibold tracking-tight focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tsn18-acc2"><span aria-hidden="true" class="text-xl text-tsn18-acc2">✦</span>Polaris</a>
    <nav aria-label="Primary" class="flex min-w-0 flex-1 gap-1 overflow-x-auto [scrollbar-width:none]">
      <a href="#tsn-18-s1" aria-current="page" class="inline-flex min-h-11 flex-none items-center rounded-full px-3.5 text-sm font-medium text-tsn18-mut hover:text-tsn18-ink focus-visible:outline-2 focus-visible:outline-tsn18-acc2 aria-[current=page]:text-tsn18-ink">Product</a>
      <a href="#tsn-18-s2" class="inline-flex min-h-11 flex-none items-center rounded-full px-3.5 text-sm font-medium text-tsn18-mut hover:text-tsn18-ink focus-visible:outline-2 focus-visible:outline-tsn18-acc2">What’s new</a>
      <a href="#tsn-18-s3" class="inline-flex min-h-11 flex-none items-center rounded-full px-3.5 text-sm font-medium text-tsn18-mut hover:text-tsn18-ink focus-visible:outline-2 focus-visible:outline-tsn18-acc2">Pricing</a>
      <a href="#tsn-18-s4" class="inline-flex min-h-11 flex-none items-center rounded-full px-3.5 text-sm font-medium text-tsn18-mut hover:text-tsn18-ink focus-visible:outline-2 focus-visible:outline-tsn18-acc2">Company</a>
    </nav>
    <a href="#tsn-18-s3" class="inline-flex min-h-11 flex-none items-center rounded-full bg-tsn18-ink px-4 text-sm font-semibold text-tsn18-bg hover:bg-tsn18-acc2 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsn18-acc2 max-sm:hidden">Get started</a>
  </header>
  <div class="px-[max(1.25rem,calc((100%-72rem)/2))] pt-[clamp(3rem,8vw,6rem)] pb-[clamp(2rem,5vw,3.5rem)]">
    <p class="font-tsn18-mono text-[11.5px] font-medium uppercase tracking-[0.16em] text-tsn18-acc">top-0 + top-11 · dual-stick</p>
    <h1 class="mt-4 max-w-[18ch] text-[clamp(34px,5.6vw,64px)] font-semibold leading-[1.02] tracking-[-0.035em] text-balance">Two bars, one clean stack</h1>
    <p class="mt-5 max-w-[54ch] text-[clamp(15px,1.6vw,17px)] leading-relaxed text-tsn18-mut text-pretty">Scroll: the announcement and the nav both pin, one above the other. Dismiss the banner and the nav slides into its place — anchors adjust too.</p>
  </div>
  <main id="tsn-18-main" class="px-[max(1.25rem,calc((100%-72rem)/2))] grid gap-5 pb-24">
    <section id="tsn-18-s1" class="scroll-mt-32 group-data-dismissed/root:scroll-mt-24 min-h-[44svh] rounded-[1.75rem] border border-tsn18-line bg-tsn18-surface p-[clamp(1.5rem,4vw,3rem)] shadow-[0_1px_2px_rgb(0_0_0/0.04)]" aria-labelledby="tsn-18-h1">
      <p class="font-tsn18-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn18-acc">Product</p>
      <h2 id="tsn-18-h1" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Offset maths, nothing more</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn18-mut text-pretty">The banner is <code class="rounded-md bg-tsn18-acc/10 px-1.5 py-0.5 font-tsn18-mono text-[0.86em] text-tsn18-ink">h-11 sticky top-0</code>; the nav is <code class="rounded-md bg-tsn18-acc/10 px-1.5 py-0.5 font-tsn18-mono text-[0.86em] text-tsn18-ink">sticky top-11</code>. The second bar’s inset equals the first bar’s height.</p>
    </section>
    <section id="tsn-18-s2" class="scroll-mt-32 group-data-dismissed/root:scroll-mt-24 min-h-[44svh] rounded-[1.75rem] border border-tsn18-line bg-tsn18-surface p-[clamp(1.5rem,4vw,3rem)] shadow-[0_1px_2px_rgb(0_0_0/0.04)]" aria-labelledby="tsn-18-h2">
      <p class="font-tsn18-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn18-acc">What’s new</p>
      <h2 id="tsn-18-h2" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">One attribute, three changes</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn18-mut text-pretty">Dismissing sets <code class="rounded-md bg-tsn18-acc/10 px-1.5 py-0.5 font-tsn18-mono text-[0.86em] text-tsn18-ink">data-dismissed</code> on the root. The banner hides, the nav moves to <code class="rounded-md bg-tsn18-acc/10 px-1.5 py-0.5 font-tsn18-mono text-[0.86em] text-tsn18-ink">top-0</code>, and every section’s <code class="rounded-md bg-tsn18-acc/10 px-1.5 py-0.5 font-tsn18-mono text-[0.86em] text-tsn18-ink">scroll-mt</code> shrinks — all in the markup.</p>
    </section>
    <section id="tsn-18-s3" class="scroll-mt-32 group-data-dismissed/root:scroll-mt-24 min-h-[44svh] rounded-[1.75rem] border border-tsn18-line bg-tsn18-surface p-[clamp(1.5rem,4vw,3rem)] shadow-[0_1px_2px_rgb(0_0_0/0.04)]" aria-labelledby="tsn-18-h3">
      <p class="font-tsn18-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn18-acc">Pricing</p>
      <h2 id="tsn-18-h3" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Fixed height, on purpose</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn18-mut text-pretty">The banner truncates instead of wrapping, so its height — and therefore the nav’s offset — is the same on every screen.</p>
    </section>
    <section id="tsn-18-s4" class="scroll-mt-32 group-data-dismissed/root:scroll-mt-24 min-h-[44svh] rounded-[1.75rem] border border-tsn18-line bg-tsn18-surface p-[clamp(1.5rem,4vw,3rem)] shadow-[0_1px_2px_rgb(0_0_0/0.04)]" aria-labelledby="tsn-18-h4">
      <p class="font-tsn18-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn18-acc">Company</p>
      <h2 id="tsn-18-h4" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Focus has somewhere to go</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn18-mut text-pretty">Removing the focused close button would drop focus to the page. The script hands it to the nav’s brand link instead.</p>
    </section>
  </main>
  <footer class="border-t border-tsn18-line px-[max(1.25rem,calc((100%-72rem)/2))] py-10 font-tsn18-mono text-xs text-tsn18-mut">Tailwind sticky navigation · pattern 18 of 25</footer>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsn18-bg: #120d1c;
  --color-tsn18-bg: oklch(0.17 0.03 300);
  --color-tsn18-surface: #1b1528;
  --color-tsn18-surface: oklch(0.21 0.035 300);
  --color-tsn18-ink: #f4eefb;
  --color-tsn18-ink: oklch(0.96 0.015 310);
  --color-tsn18-mut: #b3a8c6;
  --color-tsn18-mut: oklch(0.76 0.04 300);
  --color-tsn18-acc: #6d3df5;
  --color-tsn18-acc: oklch(0.52 0.24 285);
  --color-tsn18-acc2: #ff5fa2;
  --color-tsn18-acc2: oklch(0.7 0.2 355);
  --color-tsn18-line: #f4eefb1a;
  --color-tsn18-line: oklch(0.96 0.015 310 / 0.1);
  --font-tsn18-sans: 'Sora', system-ui, sans-serif;
  --font-tsn18-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, restated in CSS so the page is sized before the browser build compiles. */

.tsn-18 {
  width: 100%;
  min-height: 100svh;
}
/* Smooth anchor jumps live on <html>, outside the markup, so they stay in CSS. */

@media (prefers-reduced-motion: no-preference) {
  :root:has(.tsn-18) {
    scroll-behavior: smooth;
  }
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('.tsn-18').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    root.querySelector('[data-tsn18-close]').addEventListener('click', () => {
      root.setAttribute('data-dismissed', '');
      root.querySelector('[data-tsn18-brand]').focus();
    });
  });
})();
```
