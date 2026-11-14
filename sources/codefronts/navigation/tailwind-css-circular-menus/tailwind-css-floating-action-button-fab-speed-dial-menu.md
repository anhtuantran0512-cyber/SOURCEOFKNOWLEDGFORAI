---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-circular-menus/tailwind-css-floating-action-button-fab-speed-dial-menu/"
title: "Tailwind CSS Floating Action Button (FAB) Speed Dial Menu"
section: "navigation"
category: "tailwind-css-circular-menus"
category_name: "Tailwind CSS Circular Menus"
description: "The Material speed dial, rebuilt as a Tailwind v4 component inside a believable notes app: a gradient FAB fans four quick actions along a 90&deg; arc placed…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Floating Action Button (FAB) Speed Dial Menu
Source: https://codefronts.com/navigation/tailwind-css-circular-menus/tailwind-css-floating-action-button-fab-speed-dial-menu/

The Material speed dial, rebuilt as a Tailwind v4 component inside a believable notes app: a gradient FAB fans four quick actions along a 90&deg; arc placed by real CSS trigonometry, a soft scrim dims the screen, and a toast confirms what you picked. The arc lives in one @utility tcm01-polar; state is a single data-open attribute read by group-data-open/fab:.
## HTML
```html
<section class="tcm-01 w-full min-h-svh grid place-items-center bg-tcm01-bg bg-[radial-gradient(60%_50%_at_20%_0%,var(--color-tcm01-glow),transparent_70%),radial-gradient(50%_45%_at_100%_100%,var(--color-tcm01-glow2),transparent_70%)] px-5 py-14 font-tcm01-sans text-tcm01-ink antialiased" aria-label="Floating action button speed dial demo">
  <div class="grid w-full max-w-[25rem] justify-items-center gap-7">
    <article id="tcm-01-app" class="group/fab relative h-[36rem] w-full overflow-hidden rounded-[2.25rem] bg-tcm01-card shadow-tcm01-card ring-1 ring-tcm01-line">
      <header class="flex items-end justify-between px-6 pt-8 pb-5">
        <div>
          <p class="text-[12px] font-semibold tracking-[0.14em] text-tcm01-acc-ink uppercase">Wednesday</p>
          <h2 class="mt-1 text-[1.75rem] leading-none font-bold tracking-[-0.035em]">Notes</h2>
        </div>
        <span aria-hidden="true" class="grid size-10 place-items-center rounded-full bg-linear-to-br from-tcm01-acc to-tcm01-acc2 text-[13px] font-bold text-tcm01-on shadow-tcm01-glow">VK</span>
      </header>
      <ul class="grid gap-2.5 px-5">
          <li class="flex items-center gap-3 rounded-2xl bg-tcm01-sunk px-4 py-3.5 ring-1 ring-tcm01-line">
            <span aria-hidden="true" class="size-2 flex-none rounded-full bg-linear-to-br from-tcm01-acc to-tcm01-acc2"></span>
            <span class="min-w-0 flex-1"><span class="block truncate text-[15px] font-semibold tracking-[-0.01em]">Quarterly roadmap</span><span class="block text-[12.5px] text-tcm01-mut">Pinned · edited 9 min ago</span></span>
            <span class="rounded-full bg-tcm01-acc/10 px-2 py-0.5 text-[11px] font-semibold text-tcm01-acc-ink">Roadmap</span>
          </li>
          <li class="flex items-center gap-3 rounded-2xl bg-tcm01-sunk px-4 py-3.5 ring-1 ring-tcm01-line">
            <span aria-hidden="true" class="size-2 flex-none rounded-full bg-linear-to-br from-tcm01-acc to-tcm01-acc2"></span>
            <span class="min-w-0 flex-1"><span class="block truncate text-[15px] font-semibold tracking-[-0.01em]">Launch checklist</span><span class="block text-[12.5px] text-tcm01-mut">12 of 18 done</span></span>
            <span class="rounded-full bg-tcm01-acc/10 px-2 py-0.5 text-[11px] font-semibold text-tcm01-acc-ink">Work</span>
          </li>
          <li class="flex items-center gap-3 rounded-2xl bg-tcm01-sunk px-4 py-3.5 ring-1 ring-tcm01-line">
            <span aria-hidden="true" class="size-2 flex-none rounded-full bg-linear-to-br from-tcm01-acc to-tcm01-acc2"></span>
            <span class="min-w-0 flex-1"><span class="block truncate text-[15px] font-semibold tracking-[-0.01em]">Interview notes — Ana</span><span class="block text-[12.5px] text-tcm01-mut">Yesterday</span></span>
            <span class="rounded-full bg-tcm01-acc/10 px-2 py-0.5 text-[11px] font-semibold text-tcm01-acc-ink">Hiring</span>
          </li>
          <li class="flex items-center gap-3 rounded-2xl bg-tcm01-sunk px-4 py-3.5 ring-1 ring-tcm01-line">
            <span aria-hidden="true" class="size-2 flex-none rounded-full bg-linear-to-br from-tcm01-acc to-tcm01-acc2"></span>
            <span class="min-w-0 flex-1"><span class="block truncate text-[15px] font-semibold tracking-[-0.01em]">Reading list</span><span class="block text-[12.5px] text-tcm01-mut">7 articles saved</span></span>
            <span class="rounded-full bg-tcm01-acc/10 px-2 py-0.5 text-[11px] font-semibold text-tcm01-acc-ink">Personal</span>
          </li>
          <li class="flex items-center gap-3 rounded-2xl bg-tcm01-sunk px-4 py-3.5 ring-1 ring-tcm01-line">
            <span aria-hidden="true" class="size-2 flex-none rounded-full bg-linear-to-br from-tcm01-acc to-tcm01-acc2"></span>
            <span class="min-w-0 flex-1"><span class="block truncate text-[15px] font-semibold tracking-[-0.01em]">Design crit — Oct 28</span><span class="block text-[12.5px] text-tcm01-mut">Tomorrow · 10:30</span></span>
            <span class="rounded-full bg-tcm01-acc/10 px-2 py-0.5 text-[11px] font-semibold text-tcm01-acc-ink">Work</span>
          </li>
      </ul>
      <div data-close aria-hidden="true" class="absolute inset-0 bg-tcm01-scrim/0 opacity-0 backdrop-blur-[2px] transition-opacity duration-300 pointer-events-none group-data-open/fab:pointer-events-auto group-data-open/fab:bg-tcm01-scrim/40 group-data-open/fab:opacity-100 motion-reduce:transition-none"></div>
      <p data-toast role="status" aria-live="polite" class="absolute top-5 left-1/2 -translate-x-1/2 -translate-y-3 rounded-full bg-tcm01-tip px-4 py-2 text-[13px] font-semibold whitespace-nowrap text-white opacity-0 shadow-tcm01-tip transition-[opacity,translate] duration-300 data-show:translate-y-0 data-show:opacity-100"></p>
      <nav class="absolute right-6 bottom-6" aria-label="Quick actions">
        <ul id="tcm-01-menu" class="absolute right-7 bottom-7">
          <li class="absolute right-0 bottom-0 [--a:calc(180deg+var(--i)*30deg)] [--i:0] [--r:0rem] group-data-open/fab:[--r:7.25rem]">
            <button type="button" data-item data-say="New note" class="group/act tcm01-polar relative -m-6 grid size-12 cursor-pointer place-items-center rounded-full bg-tcm01-card text-tcm01-acc-ink shadow-tcm01-act ring-1 ring-tcm01-line invisible scale-40 opacity-0 transition-[translate,scale,opacity,visibility,background-color,color] duration-500 ease-[cubic-bezier(.34,1.45,.5,1)] delay-[calc((3-var(--i))*30ms)] group-data-open/fab:visible group-data-open/fab:scale-100 group-data-open/fab:opacity-100 group-data-open/fab:delay-[calc(var(--i)*55ms)] hover:bg-linear-to-br hover:from-tcm01-acc hover:to-tcm01-acc2 hover:text-tcm01-on hover:ring-transparent focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tcm01-ring motion-reduce:transition-none" aria-label="New note">
              <svg viewBox="0 0 24 24" class="size-5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M4 20h4L19 9l-4-4L4 16v4zM13.5 6.5l4 4"/></svg>
              <span aria-hidden="true" class="pointer-events-none absolute top-1/2 right-[calc(100%+0.625rem)] translate-x-1 -translate-y-1/2 rounded-lg bg-tcm01-tip px-2.5 py-1.5 text-[12px] font-semibold whitespace-nowrap text-white opacity-0 shadow-tcm01-tip transition-[opacity,translate] duration-200 group-hover/act:translate-x-0 group-hover/act:opacity-100 group-focus-visible/act:translate-x-0 group-focus-visible/act:opacity-100">New note</span>
            </button>
          </li>
          <li class="absolute right-0 bottom-0 [--a:calc(180deg+var(--i)*30deg)] [--i:1] [--r:0rem] group-data-open/fab:[--r:7.25rem]">
            <button type="button" data-item data-say="Upload image" class="group/act tcm01-polar relative -m-6 grid size-12 cursor-pointer place-items-center rounded-full bg-tcm01-card text-tcm01-acc-ink shadow-tcm01-act ring-1 ring-tcm01-line invisible scale-40 opacity-0 transition-[translate,scale,opacity,visibility,background-color,color] duration-500 ease-[cubic-bezier(.34,1.45,.5,1)] delay-[calc((3-var(--i))*30ms)] group-data-open/fab:visible group-data-open/fab:scale-100 group-data-open/fab:opacity-100 group-data-open/fab:delay-[calc(var(--i)*55ms)] hover:bg-linear-to-br hover:from-tcm01-acc hover:to-tcm01-acc2 hover:text-tcm01-on hover:ring-transparent focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tcm01-ring motion-reduce:transition-none" aria-label="Upload image">
              <svg viewBox="0 0 24 24" class="size-5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M4 5h16v14H4zM4 16l5-5 4 4 3-3 4 4M15.5 9a1 1 0 1 0 0-.01"/></svg>
              <span aria-hidden="true" class="pointer-events-none absolute top-1/2 right-[calc(100%+0.625rem)] translate-x-1 -translate-y-1/2 rounded-lg bg-tcm01-tip px-2.5 py-1.5 text-[12px] font-semibold whitespace-nowrap text-white opacity-0 shadow-tcm01-tip transition-[opacity,translate] duration-200 group-hover/act:translate-x-0 group-hover/act:opacity-100 group-focus-visible/act:translate-x-0 group-focus-visible/act:opacity-100">Upload image</span>
            </button>
          </li>
          <li class="absolute right-0 bottom-0 [--a:calc(180deg+var(--i)*30deg)] [--i:2] [--r:0rem] group-data-open/fab:[--r:7.25rem]">
            <button type="button" data-item data-say="Record voice" class="group/act tcm01-polar relative -m-6 grid size-12 cursor-pointer place-items-center rounded-full bg-tcm01-card text-tcm01-acc-ink shadow-tcm01-act ring-1 ring-tcm01-line invisible scale-40 opacity-0 transition-[translate,scale,opacity,visibility,background-color,color] duration-500 ease-[cubic-bezier(.34,1.45,.5,1)] delay-[calc((3-var(--i))*30ms)] group-data-open/fab:visible group-data-open/fab:scale-100 group-data-open/fab:opacity-100 group-data-open/fab:delay-[calc(var(--i)*55ms)] hover:bg-linear-to-br hover:from-tcm01-acc hover:to-tcm01-acc2 hover:text-tcm01-on hover:ring-transparent focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tcm01-ring motion-reduce:transition-none" aria-label="Record voice">
              <svg viewBox="0 0 24 24" class="size-5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M12 3a3 3 0 0 1 3 3v6a3 3 0 0 1-6 0V6a3 3 0 0 1 3-3zM6 11a6 6 0 0 0 12 0M12 17v4"/></svg>
              <span aria-hidden="true" class="pointer-events-none absolute top-1/2 right-[calc(100%+0.625rem)] translate-x-1 -translate-y-1/2 rounded-lg bg-tcm01-tip px-2.5 py-1.5 text-[12px] font-semibold whitespace-nowrap text-white opacity-0 shadow-tcm01-tip transition-[opacity,translate] duration-200 group-hover/act:translate-x-0 group-hover/act:opacity-100 group-focus-visible/act:translate-x-0 group-focus-visible/act:opacity-100">Record voice</span>
            </button>
          </li>
          <li class="absolute right-0 bottom-0 [--a:calc(180deg+var(--i)*30deg)] [--i:3] [--r:0rem] group-data-open/fab:[--r:7.25rem]">
            <button type="button" data-item data-say="Schedule" class="group/act tcm01-polar relative -m-6 grid size-12 cursor-pointer place-items-center rounded-full bg-tcm01-card text-tcm01-acc-ink shadow-tcm01-act ring-1 ring-tcm01-line invisible scale-40 opacity-0 transition-[translate,scale,opacity,visibility,background-color,color] duration-500 ease-[cubic-bezier(.34,1.45,.5,1)] delay-[calc((3-var(--i))*30ms)] group-data-open/fab:visible group-data-open/fab:scale-100 group-data-open/fab:opacity-100 group-data-open/fab:delay-[calc(var(--i)*55ms)] hover:bg-linear-to-br hover:from-tcm01-acc hover:to-tcm01-acc2 hover:text-tcm01-on hover:ring-transparent focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tcm01-ring motion-reduce:transition-none" aria-label="Schedule">
              <svg viewBox="0 0 24 24" class="size-5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M5 5h14v15H5zM5 9h14M9 3v4M15 3v4"/></svg>
              <span aria-hidden="true" class="pointer-events-none absolute top-1/2 right-[calc(100%+0.625rem)] translate-x-1 -translate-y-1/2 rounded-lg bg-tcm01-tip px-2.5 py-1.5 text-[12px] font-semibold whitespace-nowrap text-white opacity-0 shadow-tcm01-tip transition-[opacity,translate] duration-200 group-hover/act:translate-x-0 group-hover/act:opacity-100 group-focus-visible/act:translate-x-0 group-focus-visible/act:opacity-100">Schedule</span>
            </button>
          </li>
        </ul>
        <button type="button" data-toggle aria-expanded="false" aria-controls="tcm-01-menu" aria-label="Quick actions" class="relative grid size-14 cursor-pointer place-items-center rounded-full bg-linear-to-br from-tcm01-acc to-tcm01-acc2 text-tcm01-on shadow-tcm01-fab transition-[rotate,box-shadow,scale] duration-500 ease-[cubic-bezier(.34,1.45,.5,1)] hover:scale-105 active:scale-95 group-data-open/fab:rotate-135 group-data-open/fab:shadow-tcm01-glow focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tcm01-ring motion-reduce:transition-none">
          <span aria-hidden="true" class="absolute inset-0 rounded-full ring-2 ring-tcm01-acc2/50 animate-ping [animation-iteration-count:2] group-data-open/fab:hidden motion-reduce:hidden"></span>
          <svg viewBox="0 0 24 24" class="size-6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M12 5v14M5 12h14"/></svg>
        </button>
      </nav>
    </article>
    <p aria-hidden="true" class="max-w-full rounded-full bg-tcm01-card px-3.5 py-2 text-center font-tcm01-mono text-[11.5px] text-tcm01-mut ring-1 ring-tcm01-line ">tcm01-polar · group-data-open/fab: · delay-[calc(var(--i)*55ms)]</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcm01-bg: #f6f3ff;
  --color-tcm01-bg: oklch(0.97 0.016 297.5);
  --color-tcm01-glow: #ddd6feb3;
  --color-tcm01-glow: oklch(0.894 0.055 293.3 / 0.7);
  --color-tcm01-glow2: #fbcfe880;
  --color-tcm01-glow2: oklch(0.899 0.059 343.2 / 0.5);
  --color-tcm01-card: #fffdff;
  --color-tcm01-card: oklch(0.996 0.003 325.6);
  --color-tcm01-sunk: #f8f5ff;
  --color-tcm01-sunk: oklch(0.975 0.014 299.8);
  --color-tcm01-ink: #1e1538;
  --color-tcm01-ink: oklch(0.228 0.065 292.3);
  --color-tcm01-mut: #625a7c;
  --color-tcm01-mut: oklch(0.489 0.054 295.1);
  --color-tcm01-line: #e9e3f8;
  --color-tcm01-line: oklch(0.927 0.029 298.9);
  --color-tcm01-acc: #7c3aed;
  --color-tcm01-acc: oklch(0.541 0.247 293);
  --color-tcm01-acc2: #c026d3;
  --color-tcm01-acc2: oklch(0.591 0.257 322.9);
  --color-tcm01-acc-ink: #6d28d9;
  --color-tcm01-acc-ink: oklch(0.491 0.241 292.6);
  --color-tcm01-on: #ffffff;
  --color-tcm01-on: oklch(1 0 0);
  --color-tcm01-tip: #2a1b4e;
  --color-tcm01-tip: oklch(0.272 0.09 293);
  --color-tcm01-scrim: #1e1538;
  --color-tcm01-scrim: oklch(0.228 0.065 292.3);
  --color-tcm01-ring: #7c3aed;
  --color-tcm01-ring: oklch(0.541 0.247 293);
  --font-tcm01-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tcm01-mono: 'JetBrains Mono', ui-monospace, monospace;
  --shadow-tcm01-card: 0 1px 2px oklch(0.3 0.1 295 / 0.08), 0 30px 60px -28px oklch(0.45 0.2 300 / 0.45);
  --shadow-tcm01-act: 0 10px 22px -10px oklch(0.45 0.2 300 / 0.55), inset 0 1px 0 oklch(1 0 0 / 0.6);
  --shadow-tcm01-fab: 0 16px 32px -10px oklch(0.55 0.25 310 / 0.65), inset 0 1px 0 oklch(1 0 0 / 0.3);
  --shadow-tcm01-glow: 0 0 0 6px oklch(0.6 0.22 300 / 0.18), 0 10px 24px -8px oklch(0.55 0.25 310 / 0.6);
  --shadow-tcm01-tip: 0 10px 24px -10px oklch(0.2 0.1 295 / 0.6);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcm-01 {
  width: 100%;
  min-height: 100svh;
}
/* The radial formula, as a real utility: position = (cos a · r, sin a · r). Items set --a and --r. */

@utility tcm01-polar {
  translate: calc(cos(var(--a)) * var(--r)) calc(sin(var(--a)) * var(--r));
}
/* Dark theme: ultraviolet night: the same tokens re-pointed, so every utility (and every /opacity modifier) follows. */

@media (prefers-color-scheme: dark) {
  .tcm-01:not([data-theme="light"]) {
    color-scheme: dark;
    --color-tcm01-bg: #0f0b1d;
    --color-tcm01-bg: oklch(0.166 0.037 292.1);
    --color-tcm01-glow: #4c1d9566;
    --color-tcm01-glow: oklch(0.38 0.178 293.7 / 0.4);
    --color-tcm01-glow2: #86198f4d;
    --color-tcm01-glow2: oklch(0.452 0.192 324.6 / 0.3);
    --color-tcm01-card: #17122b;
    --color-tcm01-card: oklch(0.203 0.049 290.6);
    --color-tcm01-sunk: #1f1838;
    --color-tcm01-sunk: oklch(0.236 0.06 291.2);
    --color-tcm01-ink: #f3efff;
    --color-tcm01-ink: oklch(0.96 0.022 297.4);
    --color-tcm01-mut: #b4abd3;
    --color-tcm01-mut: oklch(0.762 0.057 295.3);
    --color-tcm01-line: #2d2550;
    --color-tcm01-line: oklch(0.297 0.076 289.5);
    --color-tcm01-acc: #8b5cf6;
    --color-tcm01-acc: oklch(0.606 0.219 292.7);
    --color-tcm01-acc2: #d946ef;
    --color-tcm01-acc2: oklch(0.667 0.259 322.1);
    --color-tcm01-acc-ink: #c4b5fd;
    --color-tcm01-acc-ink: oklch(0.811 0.101 293.6);
    --color-tcm01-on: #ffffff;
    --color-tcm01-on: oklch(1 0 0);
    --color-tcm01-tip: #3b2a6b;
    --color-tcm01-tip: oklch(0.342 0.109 291.7);
    --color-tcm01-scrim: #05030c;
    --color-tcm01-scrim: oklch(0.11 0.026 295.6);
    --color-tcm01-ring: #c4b5fd;
    --color-tcm01-ring: oklch(0.811 0.101 293.6);
  }
}

.tcm-01[data-theme="dark"] {
  color-scheme: dark;
  --color-tcm01-bg: #0f0b1d;
  --color-tcm01-bg: oklch(0.166 0.037 292.1);
  --color-tcm01-glow: #4c1d9566;
  --color-tcm01-glow: oklch(0.38 0.178 293.7 / 0.4);
  --color-tcm01-glow2: #86198f4d;
  --color-tcm01-glow2: oklch(0.452 0.192 324.6 / 0.3);
  --color-tcm01-card: #17122b;
  --color-tcm01-card: oklch(0.203 0.049 290.6);
  --color-tcm01-sunk: #1f1838;
  --color-tcm01-sunk: oklch(0.236 0.06 291.2);
  --color-tcm01-ink: #f3efff;
  --color-tcm01-ink: oklch(0.96 0.022 297.4);
  --color-tcm01-mut: #b4abd3;
  --color-tcm01-mut: oklch(0.762 0.057 295.3);
  --color-tcm01-line: #2d2550;
  --color-tcm01-line: oklch(0.297 0.076 289.5);
  --color-tcm01-acc: #8b5cf6;
  --color-tcm01-acc: oklch(0.606 0.219 292.7);
  --color-tcm01-acc2: #d946ef;
  --color-tcm01-acc2: oklch(0.667 0.259 322.1);
  --color-tcm01-acc-ink: #c4b5fd;
  --color-tcm01-acc-ink: oklch(0.811 0.101 293.6);
  --color-tcm01-on: #ffffff;
  --color-tcm01-on: oklch(1 0 0);
  --color-tcm01-tip: #3b2a6b;
  --color-tcm01-tip: oklch(0.342 0.109 291.7);
  --color-tcm01-scrim: #05030c;
  --color-tcm01-scrim: oklch(0.11 0.026 295.6);
  --color-tcm01-ring: #c4b5fd;
  --color-tcm01-ring: oklch(0.811 0.101 293.6);
}
```

## JavaScript
```js
(() => {
  const root = document.getElementById('tcm-01-app');
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
  const toast = root.querySelector('[data-toast]');
  let t;
  items.forEach((b) => b.addEventListener('click', () => {
    set(false); btn.focus();
    toast.textContent = b.dataset.say + ' — ready';
    toast.setAttribute('data-show', '');
    clearTimeout(t); t = setTimeout(() => toast.removeAttribute('data-show'), 1800);
  }));
  document.addEventListener('pointerdown', (e) => { if (!root.contains(e.target)) set(false); });
})();
```
