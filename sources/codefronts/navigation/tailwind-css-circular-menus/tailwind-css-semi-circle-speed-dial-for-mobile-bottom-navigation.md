---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-circular-menus/tailwind-css-semi-circle-speed-dial-for-mobile-bottom-navigation/"
title: "Tailwind CSS Semi-Circle Speed Dial for Mobile Bottom Navigation"
section: "navigation"
category: "tailwind-css-circular-menus"
category_name: "Tailwind CSS Circular Menus"
description: "The radial pattern that actually belongs on phones: a centred &ldquo;Create&rdquo; button raises a half-disc sheet and fans five labelled actions across…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Semi-Circle Speed Dial for Mobile Bottom Navigation
Source: https://codefronts.com/navigation/tailwind-css-circular-menus/tailwind-css-semi-circle-speed-dial-for-mobile-bottom-navigation/

The radial pattern that actually belongs on phones: a centred &ldquo;Create&rdquo; button raises a half-disc sheet and fans five labelled actions across 180&deg; &mdash; exactly the sweep of a thumb. The angle formula divides by n &minus; 1 so actions land on both ends of the arc, the dial respects env(safe-area-inset-bottom), and a scrim dims the feed behind it.
## HTML
```html
<section class="tcm-14 w-full min-h-svh grid place-items-center bg-tcm14-bg bg-[radial-gradient(60%_50%_at_50%_100%,var(--color-tcm14-glow),transparent_70%)] px-5 py-14 font-tcm14-sans text-tcm14-ink antialiased" aria-label="Semi-circle speed dial demo">
  <div class="grid w-full justify-items-center gap-7">
    <div id="tcm-14-phone" class="group/dial relative h-[36rem] w-full max-w-[22rem] overflow-hidden rounded-[2.5rem] bg-tcm14-card shadow-tcm14-phone ring-1 ring-tcm14-line">
      <header class="flex items-center justify-between px-5 pt-6 pb-4"><p class="text-lg font-extrabold tracking-[-0.03em]">frame<span class="text-tcm14-acc">.</span></p><span aria-hidden="true" class="size-8 rounded-full bg-linear-to-br from-tcm14-acc to-tcm14-acc2"></span></header>
      <div class="grid gap-3 px-4">
        <div class="overflow-hidden rounded-2xl bg-tcm14-sunk ring-1 ring-tcm14-line">
          <div aria-hidden="true" class="h-24 bg-linear-to-br from-amber-300 to-rose-400"></div>
          <p class="px-3.5 py-2.5 text-[13px]"><b class="font-semibold">Ana</b> <span class="text-tcm14-mut">Golden hour at the pier</span></p>
        </div>
        <div class="overflow-hidden rounded-2xl bg-tcm14-sunk ring-1 ring-tcm14-line">
          <div aria-hidden="true" class="h-24 bg-linear-to-br from-sky-300 to-indigo-400"></div>
          <p class="px-3.5 py-2.5 text-[13px]"><b class="font-semibold">Teo</b> <span class="text-tcm14-mut">Studio day, film only</span></p>
        </div>
      </div>
      <div data-close aria-hidden="true" class="absolute inset-0 bg-tcm14-scrim/0 transition-colors duration-300 pointer-events-none group-data-open/dial:pointer-events-auto group-data-open/dial:bg-tcm14-scrim/35"></div>
      <span aria-hidden="true" class="pointer-events-none absolute -bottom-[12.5rem] left-1/2 -ml-[13.5rem] size-[27rem] rounded-full bg-linear-to-b from-tcm14-acc to-tcm14-acc2 shadow-tcm14-sheet translate-y-full transition-[translate] duration-500 ease-[cubic-bezier(.16,1,.3,1)] group-data-open/dial:translate-y-0 motion-reduce:transition-none"></span>
      <nav class="absolute bottom-0 left-1/2 pb-[max(1.25rem,env(safe-area-inset-bottom))]" aria-label="Create">
        <ul id="tcm-14-menu" class="absolute bottom-[3.05rem] left-0 [--n:5]">
          <li class="absolute bottom-0 left-0 [--i:0] [--a:calc(180deg+180deg/(var(--n)-1)*var(--i))] [--r:0rem] group-data-open/dial:[--r:6.9rem]">
            <a href="#tcm-14-camera" data-item class="tcm14-polar -m-6 grid w-12 justify-items-center gap-1.5 text-[11px] font-semibold text-white invisible scale-40 opacity-0 transition-[translate,scale,opacity,visibility] duration-500 ease-[cubic-bezier(.34,1.45,.5,1)] delay-[calc(var(--i)*45ms)] group-data-open/dial:visible group-data-open/dial:scale-100 group-data-open/dial:opacity-100 focus-visible:outline-none motion-reduce:transition-none [&:focus-visible>span]:outline-2 [&:focus-visible>span]:outline-offset-2 [&:focus-visible>span]:outline-white">
              <span class="grid size-12 place-items-center rounded-full bg-white/15 ring-1 ring-white/25 transition-colors hover:bg-white/30"><svg viewBox="0 0 24 24" class="size-[21px]" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M4 8h3l2-3h6l2 3h3v11H4zM12 9.8a3.2 3.2 0 1 0 0 6.4 3.2 3.2 0 0 0 0-6.4z"/></svg></span>Camera
            </a>
          </li>
          <li class="absolute bottom-0 left-0 [--i:1] [--a:calc(180deg+180deg/(var(--n)-1)*var(--i))] [--r:0rem] group-data-open/dial:[--r:6.9rem]">
            <a href="#tcm-14-gallery" data-item class="tcm14-polar -m-6 grid w-12 justify-items-center gap-1.5 text-[11px] font-semibold text-white invisible scale-40 opacity-0 transition-[translate,scale,opacity,visibility] duration-500 ease-[cubic-bezier(.34,1.45,.5,1)] delay-[calc(var(--i)*45ms)] group-data-open/dial:visible group-data-open/dial:scale-100 group-data-open/dial:opacity-100 focus-visible:outline-none motion-reduce:transition-none [&:focus-visible>span]:outline-2 [&:focus-visible>span]:outline-offset-2 [&:focus-visible>span]:outline-white">
              <span class="grid size-12 place-items-center rounded-full bg-white/15 ring-1 ring-white/25 transition-colors hover:bg-white/30"><svg viewBox="0 0 24 24" class="size-[21px]" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M4 5h16v14H4zM4 16l5-5 4 4 3-3 4 4M15.5 9a1 1 0 1 0 0-.01"/></svg></span>Gallery
            </a>
          </li>
          <li class="absolute bottom-0 left-0 [--i:2] [--a:calc(180deg+180deg/(var(--n)-1)*var(--i))] [--r:0rem] group-data-open/dial:[--r:6.9rem]">
            <a href="#tcm-14-post" data-item class="tcm14-polar -m-6 grid w-12 justify-items-center gap-1.5 text-[11px] font-semibold text-white invisible scale-40 opacity-0 transition-[translate,scale,opacity,visibility] duration-500 ease-[cubic-bezier(.34,1.45,.5,1)] delay-[calc(var(--i)*45ms)] group-data-open/dial:visible group-data-open/dial:scale-100 group-data-open/dial:opacity-100 focus-visible:outline-none motion-reduce:transition-none [&:focus-visible>span]:outline-2 [&:focus-visible>span]:outline-offset-2 [&:focus-visible>span]:outline-white">
              <span class="grid size-12 place-items-center rounded-full bg-white/15 ring-1 ring-white/25 transition-colors hover:bg-white/30"><svg viewBox="0 0 24 24" class="size-[21px]" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M4 20h4L19 9l-4-4L4 16v4zM13.5 6.5l4 4"/></svg></span>Post
            </a>
          </li>
          <li class="absolute bottom-0 left-0 [--i:3] [--a:calc(180deg+180deg/(var(--n)-1)*var(--i))] [--r:0rem] group-data-open/dial:[--r:6.9rem]">
            <a href="#tcm-14-voice" data-item class="tcm14-polar -m-6 grid w-12 justify-items-center gap-1.5 text-[11px] font-semibold text-white invisible scale-40 opacity-0 transition-[translate,scale,opacity,visibility] duration-500 ease-[cubic-bezier(.34,1.45,.5,1)] delay-[calc(var(--i)*45ms)] group-data-open/dial:visible group-data-open/dial:scale-100 group-data-open/dial:opacity-100 focus-visible:outline-none motion-reduce:transition-none [&:focus-visible>span]:outline-2 [&:focus-visible>span]:outline-offset-2 [&:focus-visible>span]:outline-white">
              <span class="grid size-12 place-items-center rounded-full bg-white/15 ring-1 ring-white/25 transition-colors hover:bg-white/30"><svg viewBox="0 0 24 24" class="size-[21px]" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M12 3a3 3 0 0 1 3 3v6a3 3 0 0 1-6 0V6a3 3 0 0 1 3-3zM6 11a6 6 0 0 0 12 0M12 17v4"/></svg></span>Voice
            </a>
          </li>
          <li class="absolute bottom-0 left-0 [--i:4] [--a:calc(180deg+180deg/(var(--n)-1)*var(--i))] [--r:0rem] group-data-open/dial:[--r:6.9rem]">
            <a href="#tcm-14-live" data-item class="tcm14-polar -m-6 grid w-12 justify-items-center gap-1.5 text-[11px] font-semibold text-white invisible scale-40 opacity-0 transition-[translate,scale,opacity,visibility] duration-500 ease-[cubic-bezier(.34,1.45,.5,1)] delay-[calc(var(--i)*45ms)] group-data-open/dial:visible group-data-open/dial:scale-100 group-data-open/dial:opacity-100 focus-visible:outline-none motion-reduce:transition-none [&:focus-visible>span]:outline-2 [&:focus-visible>span]:outline-offset-2 [&:focus-visible>span]:outline-white">
              <span class="grid size-12 place-items-center rounded-full bg-white/15 ring-1 ring-white/25 transition-colors hover:bg-white/30"><svg viewBox="0 0 24 24" class="size-[21px]" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M12 9.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5zM7.1 7.1a7 7 0 0 0 0 9.8M16.9 7.1a7 7 0 0 1 0 9.8M4.2 4.2a11 11 0 0 0 0 15.6M19.8 4.2a11 11 0 0 1 0 15.6"/></svg></span>Live
            </a>
          </li>
        </ul>
        <button type="button" data-toggle aria-expanded="false" aria-controls="tcm-14-menu" aria-label="Create" class="relative z-10 grid size-15 -translate-x-1/2 cursor-pointer place-items-center rounded-full bg-linear-to-br from-tcm14-acc to-tcm14-acc2 text-white shadow-tcm14-fab ring-4 ring-tcm14-card transition-[rotate,box-shadow] duration-500 ease-[cubic-bezier(.34,1.45,.5,1)] group-data-open/dial:rotate-135 group-data-open/dial:ring-white/20 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tcm14-ring motion-reduce:transition-none"><svg viewBox="0 0 24 24" class="size-6" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M12 5v14M5 12h14"/></svg></button>
      </nav>
    </div>
    <p aria-hidden="true" class="max-w-full rounded-full bg-tcm14-card px-3.5 py-2 text-center font-tcm14-mono text-[11.5px] text-tcm14-mut ring-1 ring-tcm14-line ">[--a:calc(180deg+180deg/(var(--n)-1)*var(--i))] · translate-y-full → group-data-open/dial:translate-y-0</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcm14-bg: #f5f1fb;
  --color-tcm14-bg: oklch(0.964 0.014 304.1);
  --color-tcm14-glow: #e9d5ffb3;
  --color-tcm14-glow: oklch(0.902 0.06 306.7 / 0.7);
  --color-tcm14-card: #fffdff;
  --color-tcm14-card: oklch(0.996 0.003 325.6);
  --color-tcm14-sunk: #f6f2fc;
  --color-tcm14-sunk: oklch(0.967 0.014 304.1);
  --color-tcm14-ink: #1f1630;
  --color-tcm14-ink: oklch(0.226 0.05 298.3);
  --color-tcm14-mut: #655b7a;
  --color-tcm14-mut: oklch(0.493 0.05 299.3);
  --color-tcm14-line: #e8e1f3;
  --color-tcm14-line: oklch(0.921 0.025 303.5);
  --color-tcm14-acc: #9333ea;
  --color-tcm14-acc: oklch(0.558 0.252 302.3);
  --color-tcm14-acc2: #6d28d9;
  --color-tcm14-acc2: oklch(0.491 0.241 292.6);
  --color-tcm14-scrim: #1f1630;
  --color-tcm14-scrim: oklch(0.226 0.05 298.3);
  --color-tcm14-ring: #7e22ce;
  --color-tcm14-ring: oklch(0.496 0.237 301.9);
  --font-tcm14-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tcm14-mono: 'JetBrains Mono', ui-monospace, monospace;
  --shadow-tcm14-phone: 0 1px 2px oklch(0.3 0.1 300 / 0.06), 0 34px 70px -30px oklch(0.4 0.2 300 / 0.5);
  --shadow-tcm14-sheet: 0 -14px 44px -14px oklch(0.45 0.22 300 / 0.6);
  --shadow-tcm14-fab: 0 14px 30px -10px oklch(0.45 0.24 300 / 0.7);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcm-14 {
  width: 100%;
  min-height: 100svh;
}
/* The radial formula, as a real utility: position = (cos a · r, sin a · r). Items set --a and --r. */

@utility tcm14-polar {
  translate: calc(cos(var(--a)) * var(--r)) calc(sin(var(--a)) * var(--r));
}
/* Dark theme: grape night: the same tokens re-pointed, so every utility (and every /opacity modifier) follows. */

@media (prefers-color-scheme: dark) {
  .tcm-14:not([data-theme="light"]) {
    color-scheme: dark;
    --color-tcm14-bg: #0f0b18;
    --color-tcm14-bg: oklch(0.162 0.027 297.4);
    --color-tcm14-glow: #581c8766;
    --color-tcm14-glow: oklch(0.381 0.166 305 / 0.4);
    --color-tcm14-card: #181226;
    --color-tcm14-card: oklch(0.201 0.04 296.5);
    --color-tcm14-sunk: #211a33;
    --color-tcm14-sunk: oklch(0.239 0.047 295.5);
    --color-tcm14-ink: #f4effc;
    --color-tcm14-ink: oklch(0.96 0.018 303.4);
    --color-tcm14-mut: #b1a6c9;
    --color-tcm14-mut: oklch(0.746 0.051 299.5);
    --color-tcm14-line: #2e2645;
    --color-tcm14-line: oklch(0.293 0.056 294.6);
    --color-tcm14-acc: #a855f7;
    --color-tcm14-acc: oklch(0.627 0.233 303.9);
    --color-tcm14-acc2: #7c3aed;
    --color-tcm14-acc2: oklch(0.541 0.247 293);
    --color-tcm14-scrim: #000000;
    --color-tcm14-scrim: oklch(0 0 0);
    --color-tcm14-ring: #d8b4fe;
    --color-tcm14-ring: oklch(0.827 0.108 306.4);
  }
}

.tcm-14[data-theme="dark"] {
  color-scheme: dark;
  --color-tcm14-bg: #0f0b18;
  --color-tcm14-bg: oklch(0.162 0.027 297.4);
  --color-tcm14-glow: #581c8766;
  --color-tcm14-glow: oklch(0.381 0.166 305 / 0.4);
  --color-tcm14-card: #181226;
  --color-tcm14-card: oklch(0.201 0.04 296.5);
  --color-tcm14-sunk: #211a33;
  --color-tcm14-sunk: oklch(0.239 0.047 295.5);
  --color-tcm14-ink: #f4effc;
  --color-tcm14-ink: oklch(0.96 0.018 303.4);
  --color-tcm14-mut: #b1a6c9;
  --color-tcm14-mut: oklch(0.746 0.051 299.5);
  --color-tcm14-line: #2e2645;
  --color-tcm14-line: oklch(0.293 0.056 294.6);
  --color-tcm14-acc: #a855f7;
  --color-tcm14-acc: oklch(0.627 0.233 303.9);
  --color-tcm14-acc2: #7c3aed;
  --color-tcm14-acc2: oklch(0.541 0.247 293);
  --color-tcm14-scrim: #000000;
  --color-tcm14-scrim: oklch(0 0 0);
  --color-tcm14-ring: #d8b4fe;
  --color-tcm14-ring: oklch(0.827 0.108 306.4);
}
```

## JavaScript
```js
(() => {
  const root = document.getElementById('tcm-14-phone');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const btn = root.querySelector('[data-toggle]');
  const items = [...root.querySelectorAll('[data-item]')];
  const set = (open, focus) => {
    root.toggleAttribute('data-open', open);
    btn.setAttribute('aria-expanded', String(open));
    if (open && focus && items[0]) setTimeout(() => items[0].focus(), 220);
  };
  btn.addEventListener('click', (e) => set(!root.hasAttribute('data-open'), e.detail === 0));
  root.querySelectorAll('[data-close]').forEach((el) => el.addEventListener('click', () => set(false)));
  root.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && root.hasAttribute('data-open')) { set(false); btn.focus(); return; }
    const k = items.indexOf(document.activeElement);
    const d = { ArrowRight: 1, ArrowDown: 1, ArrowLeft: -1, ArrowUp: -1 }[e.key];
    if (k < 0 || !d) return;
    e.preventDefault();
    items[(k + d + items.length) % items.length].focus();
  });
  document.addEventListener('pointerdown', (e) => { if (!root.contains(e.target)) set(false); });
})();
```
