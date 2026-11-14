---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-circular-menus/tailwind-css-quarter-circle-corner-menu-bottom-right-arc/"
title: "Tailwind CSS Quarter Circle Corner Menu (Bottom-Right Arc)"
section: "navigation"
category: "tailwind-css-circular-menus"
category_name: "Tailwind CSS Circular Menus"
description: "A docked corner launcher over a long-read article: a quarter-circle sheet sweeps out of the bottom-right corner and five page actions ride its curved edge."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Quarter Circle Corner Menu (Bottom-Right Arc)
Source: https://codefronts.com/navigation/tailwind-css-circular-menus/tailwind-css-quarter-circle-corner-menu-bottom-right-arc/

A docked corner launcher over a long-read article: a quarter-circle sheet sweeps out of the bottom-right corner and five page actions ride its curved edge. The sheet is one gradient circle scaled from 0 to 1 &mdash; a single compositor-only transform &mdash; and the actions sit on an inset 188&deg;&rarr;262&deg; arc so the first and last never kiss the card edges.
## HTML
```html
<section class="tcm-05 w-full min-h-svh grid place-items-center bg-tcm05-bg bg-[radial-gradient(60%_50%_at_80%_100%,var(--color-tcm05-glow),transparent_70%)] px-5 py-14 font-tcm05-sans text-tcm05-ink antialiased" aria-label="Quarter circle corner menu demo">
  <div class="grid w-full justify-items-center gap-7">
    <article id="tcm-05-page" class="group/dock relative h-[34rem] w-full max-w-[44rem] overflow-hidden rounded-3xl bg-tcm05-card shadow-tcm05-card ring-1 ring-tcm05-line">
      <div class="px-6 pt-8 sm:px-10">
        <p class="font-tcm05-mono text-[11.5px] text-tcm05-acc-ink">Guides · Field notes</p>
        <h2 class="mt-2 max-w-[28rem] text-[clamp(1.5rem,3.6vw,2rem)] leading-tight font-semibold tracking-[-0.03em] text-balance">Designing for the thumb, not the cursor</h2>
        <p class="mt-3 max-w-[30rem] text-[15px] leading-relaxed text-tcm05-mut text-pretty">Most phones are held in one hand, and the bottom-right corner is the easiest place to reach. That makes it prime real estate for the actions people repeat most &mdash; and a quarter circle is the shape a thumb draws naturally.</p>
        <div aria-hidden="true" class="mt-6 grid max-w-[30rem] gap-2.5"><span class="h-2.5 rounded-full bg-tcm05-sunk"></span><span class="h-2.5 w-[86%] rounded-full bg-tcm05-sunk"></span><span class="h-2.5 w-[64%] rounded-full bg-tcm05-sunk"></span></div>
      </div>
      <div class="absolute right-0 bottom-0">
        <span aria-hidden="true" class="pointer-events-none absolute -right-[16.25rem] -bottom-[16.25rem] size-[32.5rem] rounded-full bg-linear-to-tl from-tcm05-a to-tcm05-b shadow-tcm05-sheet scale-0 transition-[scale] duration-500 ease-[cubic-bezier(.16,1,.3,1)] group-data-open/dock:scale-100 motion-reduce:transition-none"></span>
        <ul id="tcm-05-menu" class="absolute right-[2.875rem] bottom-[2.875rem]">
          <li class="absolute right-0 bottom-0 [--i:0] [--a:calc(188deg+var(--i)*18.5deg)] [--r:0rem] group-data-open/dock:[--r:10.75rem]">
            <button type="button" data-item class="group/act tcm05-polar relative -m-[1.375rem] grid size-11 cursor-pointer place-items-center rounded-full bg-white/12 text-white ring-1 ring-white/20 invisible opacity-0 transition-[translate,opacity,visibility,background-color] duration-500 ease-[cubic-bezier(.34,1.45,.5,1)] delay-[calc(var(--i)*40ms)] group-data-open/dock:visible group-data-open/dock:opacity-100 hover:bg-white/25 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-white motion-reduce:transition-none" aria-label="Download">
              <svg viewBox="0 0 24 24" class="size-5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M12 4v12m0 0-4-4m4 4 4-4M5 20h14"/></svg>
              <span aria-hidden="true" class="pointer-events-none absolute top-1/2 right-[calc(100%+0.5rem)] translate-x-1 -translate-y-1/2 rounded-lg bg-tcm05-tip px-2.5 py-1.5 text-[12px] font-semibold whitespace-nowrap text-white opacity-0 shadow-tcm05-tip transition-[opacity,translate] duration-200 group-hover/act:translate-x-0 group-hover/act:opacity-100 group-focus-visible/act:translate-x-0 group-focus-visible/act:opacity-100">Download</span>
            </button>
          </li>
          <li class="absolute right-0 bottom-0 [--i:1] [--a:calc(188deg+var(--i)*18.5deg)] [--r:0rem] group-data-open/dock:[--r:10.75rem]">
            <button type="button" data-item class="group/act tcm05-polar relative -m-[1.375rem] grid size-11 cursor-pointer place-items-center rounded-full bg-white/12 text-white ring-1 ring-white/20 invisible opacity-0 transition-[translate,opacity,visibility,background-color] duration-500 ease-[cubic-bezier(.34,1.45,.5,1)] delay-[calc(var(--i)*40ms)] group-data-open/dock:visible group-data-open/dock:opacity-100 hover:bg-white/25 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-white motion-reduce:transition-none" aria-label="Share">
              <svg viewBox="0 0 24 24" class="size-5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M6 9.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5zM18 3.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5zM18 15.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5zM8.2 10.8l7.6-3.6M8.2 13.2l7.6 3.6"/></svg>
              <span aria-hidden="true" class="pointer-events-none absolute top-1/2 right-[calc(100%+0.5rem)] translate-x-1 -translate-y-1/2 rounded-lg bg-tcm05-tip px-2.5 py-1.5 text-[12px] font-semibold whitespace-nowrap text-white opacity-0 shadow-tcm05-tip transition-[opacity,translate] duration-200 group-hover/act:translate-x-0 group-hover/act:opacity-100 group-focus-visible/act:translate-x-0 group-focus-visible/act:opacity-100">Share</span>
            </button>
          </li>
          <li class="absolute right-0 bottom-0 [--i:2] [--a:calc(188deg+var(--i)*18.5deg)] [--r:0rem] group-data-open/dock:[--r:10.75rem]">
            <button type="button" data-item class="group/act tcm05-polar relative -m-[1.375rem] grid size-11 cursor-pointer place-items-center rounded-full bg-white/12 text-white ring-1 ring-white/20 invisible opacity-0 transition-[translate,opacity,visibility,background-color] duration-500 ease-[cubic-bezier(.34,1.45,.5,1)] delay-[calc(var(--i)*40ms)] group-data-open/dock:visible group-data-open/dock:opacity-100 hover:bg-white/25 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-white motion-reduce:transition-none" aria-label="Save">
              <svg viewBox="0 0 24 24" class="size-5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M12 20s-7-4.4-9.3-8.8A5.2 5.2 0 0 1 12 6.4a5.2 5.2 0 0 1 9.3 4.8C19 15.6 12 20 12 20z"/></svg>
              <span aria-hidden="true" class="pointer-events-none absolute top-1/2 right-[calc(100%+0.5rem)] translate-x-1 -translate-y-1/2 rounded-lg bg-tcm05-tip px-2.5 py-1.5 text-[12px] font-semibold whitespace-nowrap text-white opacity-0 shadow-tcm05-tip transition-[opacity,translate] duration-200 group-hover/act:translate-x-0 group-hover/act:opacity-100 group-focus-visible/act:translate-x-0 group-focus-visible/act:opacity-100">Save</span>
            </button>
          </li>
          <li class="absolute right-0 bottom-0 [--i:3] [--a:calc(188deg+var(--i)*18.5deg)] [--r:0rem] group-data-open/dock:[--r:10.75rem]">
            <button type="button" data-item class="group/act tcm05-polar relative -m-[1.375rem] grid size-11 cursor-pointer place-items-center rounded-full bg-white/12 text-white ring-1 ring-white/20 invisible opacity-0 transition-[translate,opacity,visibility,background-color] duration-500 ease-[cubic-bezier(.34,1.45,.5,1)] delay-[calc(var(--i)*40ms)] group-data-open/dock:visible group-data-open/dock:opacity-100 hover:bg-white/25 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-white motion-reduce:transition-none" aria-label="Comment">
              <svg viewBox="0 0 24 24" class="size-5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M7 8h10M7 12h6M4 4h16v13H9l-5 4z"/></svg>
              <span aria-hidden="true" class="pointer-events-none absolute top-1/2 right-[calc(100%+0.5rem)] translate-x-1 -translate-y-1/2 rounded-lg bg-tcm05-tip px-2.5 py-1.5 text-[12px] font-semibold whitespace-nowrap text-white opacity-0 shadow-tcm05-tip transition-[opacity,translate] duration-200 group-hover/act:translate-x-0 group-hover/act:opacity-100 group-focus-visible/act:translate-x-0 group-focus-visible/act:opacity-100">Comment</span>
            </button>
          </li>
          <li class="absolute right-0 bottom-0 [--i:4] [--a:calc(188deg+var(--i)*18.5deg)] [--r:0rem] group-data-open/dock:[--r:10.75rem]">
            <button type="button" data-item class="group/act tcm05-polar relative -m-[1.375rem] grid size-11 cursor-pointer place-items-center rounded-full bg-white/12 text-white ring-1 ring-white/20 invisible opacity-0 transition-[translate,opacity,visibility,background-color] duration-500 ease-[cubic-bezier(.34,1.45,.5,1)] delay-[calc(var(--i)*40ms)] group-data-open/dock:visible group-data-open/dock:opacity-100 hover:bg-white/25 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-white motion-reduce:transition-none" aria-label="Help">
              <svg viewBox="0 0 24 24" class="size-5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18zM9.5 9.3a2.6 2.6 0 0 1 5 .9c0 1.8-2.5 2.3-2.5 3.8M12 17.2v.01"/></svg>
              <span aria-hidden="true" class="pointer-events-none absolute top-1/2 right-[calc(100%+0.5rem)] translate-x-1 -translate-y-1/2 rounded-lg bg-tcm05-tip px-2.5 py-1.5 text-[12px] font-semibold whitespace-nowrap text-white opacity-0 shadow-tcm05-tip transition-[opacity,translate] duration-200 group-hover/act:translate-x-0 group-hover/act:opacity-100 group-focus-visible/act:translate-x-0 group-focus-visible/act:opacity-100">Help</span>
            </button>
          </li>
        </ul>
        <button type="button" data-toggle aria-expanded="false" aria-controls="tcm-05-menu" aria-label="Page actions" class="absolute right-6 bottom-6 z-10 grid size-14 cursor-pointer place-items-center rounded-full bg-linear-to-br from-tcm05-a to-tcm05-b text-white shadow-tcm05-fab transition-[rotate,background-color,box-shadow] duration-500 ease-[cubic-bezier(.34,1.45,.5,1)] group-data-open/dock:rotate-90 group-data-open/dock:bg-none group-data-open/dock:bg-white/15 group-data-open/dock:shadow-none focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tcm05-ring motion-reduce:transition-none"><svg viewBox="0 0 24 24" class="size-6" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M5 12h.01M12 12h.01M19 12h.01"/></svg></button>
      </div>
    </article>
    <p aria-hidden="true" class="max-w-full rounded-full bg-tcm05-card px-3.5 py-2 text-center font-tcm05-mono text-[11.5px] text-tcm05-mut ring-1 ring-tcm05-line ">scale-0 → group-data-open/dock:scale-100 · [--a:calc(188deg+var(--i)*18.5deg)]</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcm05-bg: #eef5ff;
  --color-tcm05-bg: oklch(0.968 0.015 257.2);
  --color-tcm05-glow: #bfdbfeb3;
  --color-tcm05-glow: oklch(0.882 0.057 254.1 / 0.7);
  --color-tcm05-card: #fbfdff;
  --color-tcm05-card: oklch(0.993 0.003 247.9);
  --color-tcm05-sunk: #e7effb;
  --color-tcm05-sunk: oklch(0.95 0.018 258.4);
  --color-tcm05-ink: #0d1b33;
  --color-tcm05-ink: oklch(0.224 0.051 260.5);
  --color-tcm05-mut: #4b5d7a;
  --color-tcm05-mut: oklch(0.475 0.052 259.8);
  --color-tcm05-line: #d9e4f5;
  --color-tcm05-line: oklch(0.916 0.026 259);
  --color-tcm05-a: #2563eb;
  --color-tcm05-a: oklch(0.546 0.215 262.9);
  --color-tcm05-b: #0891b2;
  --color-tcm05-b: oklch(0.609 0.111 221.7);
  --color-tcm05-acc-ink: #1d4ed8;
  --color-tcm05-acc-ink: oklch(0.488 0.217 264.4);
  --color-tcm05-tip: #0d1b33;
  --color-tcm05-tip: oklch(0.224 0.051 260.5);
  --color-tcm05-ring: #1d4ed8;
  --color-tcm05-ring: oklch(0.488 0.217 264.4);
  --font-tcm05-sans: 'Geist', system-ui, sans-serif;
  --font-tcm05-mono: 'Geist Mono', ui-monospace, monospace;
  --shadow-tcm05-card: 0 1px 2px oklch(0.3 0.1 260 / 0.07), 0 28px 60px -28px oklch(0.45 0.18 255 / 0.4);
  --shadow-tcm05-sheet: 0 -10px 50px -12px oklch(0.4 0.15 250 / 0.55);
  --shadow-tcm05-fab: 0 14px 30px -10px oklch(0.5 0.2 255 / 0.65), inset 0 1px 0 oklch(1 0 0 / 0.3);
  --shadow-tcm05-tip: 0 10px 22px -10px oklch(0.2 0.1 260 / 0.6);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcm-05 {
  width: 100%;
  min-height: 100svh;
}
/* The radial formula, as a real utility: position = (cos a · r, sin a · r). Items set --a and --r. */

@utility tcm05-polar {
  translate: calc(cos(var(--a)) * var(--r)) calc(sin(var(--a)) * var(--r));
}
/* Dark theme: deep ocean: the same tokens re-pointed, so every utility (and every /opacity modifier) follows. */

@media (prefers-color-scheme: dark) {
  .tcm-05:not([data-theme="light"]) {
    color-scheme: dark;
    --color-tcm05-bg: #07101f;
    --color-tcm05-bg: oklch(0.173 0.034 259.5);
    --color-tcm05-glow: #1e3a8a73;
    --color-tcm05-glow: oklch(0.379 0.138 265.5 / 0.45);
    --color-tcm05-card: #0d1a30;
    --color-tcm05-card: oklch(0.219 0.047 260.3);
    --color-tcm05-sunk: #16263f;
    --color-tcm05-sunk: oklch(0.268 0.052 259);
    --color-tcm05-ink: #eaf2ff;
    --color-tcm05-ink: oklch(0.959 0.019 260.2);
    --color-tcm05-mut: #a3b7d6;
    --color-tcm05-mut: oklch(0.775 0.05 259.1);
    --color-tcm05-line: #1f3352;
    --color-tcm05-line: oklch(0.32 0.061 258.9);
    --color-tcm05-a: #2563eb;
    --color-tcm05-a: oklch(0.546 0.215 262.9);
    --color-tcm05-b: #0891b2;
    --color-tcm05-b: oklch(0.609 0.111 221.7);
    --color-tcm05-acc-ink: #93c5fd;
    --color-tcm05-acc-ink: oklch(0.809 0.096 251.8);
    --color-tcm05-tip: #020617;
    --color-tcm05-tip: oklch(0.129 0.041 264.7);
    --color-tcm05-ring: #93c5fd;
    --color-tcm05-ring: oklch(0.809 0.096 251.8);
  }
}

.tcm-05[data-theme="dark"] {
  color-scheme: dark;
  --color-tcm05-bg: #07101f;
  --color-tcm05-bg: oklch(0.173 0.034 259.5);
  --color-tcm05-glow: #1e3a8a73;
  --color-tcm05-glow: oklch(0.379 0.138 265.5 / 0.45);
  --color-tcm05-card: #0d1a30;
  --color-tcm05-card: oklch(0.219 0.047 260.3);
  --color-tcm05-sunk: #16263f;
  --color-tcm05-sunk: oklch(0.268 0.052 259);
  --color-tcm05-ink: #eaf2ff;
  --color-tcm05-ink: oklch(0.959 0.019 260.2);
  --color-tcm05-mut: #a3b7d6;
  --color-tcm05-mut: oklch(0.775 0.05 259.1);
  --color-tcm05-line: #1f3352;
  --color-tcm05-line: oklch(0.32 0.061 258.9);
  --color-tcm05-a: #2563eb;
  --color-tcm05-a: oklch(0.546 0.215 262.9);
  --color-tcm05-b: #0891b2;
  --color-tcm05-b: oklch(0.609 0.111 221.7);
  --color-tcm05-acc-ink: #93c5fd;
  --color-tcm05-acc-ink: oklch(0.809 0.096 251.8);
  --color-tcm05-tip: #020617;
  --color-tcm05-tip: oklch(0.129 0.041 264.7);
  --color-tcm05-ring: #93c5fd;
  --color-tcm05-ring: oklch(0.809 0.096 251.8);
}
```

## JavaScript
```js
(() => {
  const root = document.getElementById('tcm-05-page');
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
