---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-circular-menus/tailwind-css-fan-out-card-menu-animation-workspace-switcher/"
title: "Tailwind CSS Fan-Out Card Menu Animation (Workspace Switcher)"
section: "navigation"
category: "tailwind-css-circular-menus"
category_name: "Tailwind CSS Circular Menus"
description: "A workspace switcher that deals five labelled cards out of a deck: closed, three offset ghost cards labelled &ldquo;5 spaces&rdquo; sit on the trigger; open,…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Fan-Out Card Menu Animation (Workspace Switcher)
Source: https://codefronts.com/navigation/tailwind-css-circular-menus/tailwind-css-fan-out-card-menu-animation-workspace-switcher/

A workspace switcher that deals five labelled cards out of a deck: closed, three offset ghost cards labelled &ldquo;5 spaces&rdquo; sit on the trigger; open, the real cards fan upward along a gentle curve &mdash; each one lifted calc(var(--i)*-4.1rem), pushed right by var(--i)*var(--i)*0.3rem and tilted 2.5&deg; more than the last. The result reads like a dealt hand but stays a scannable list, with icons, counts and shortcut keys, and folds back in reverse order.
## HTML
```html
<section class="tcm-09 w-full min-h-svh grid place-items-center bg-tcm09-bg bg-[radial-gradient(60%_50%_at_40%_60%,var(--color-tcm09-glow),transparent_70%)] px-5 py-14 font-tcm09-sans text-tcm09-ink antialiased" aria-label="Fan-out card menu demo">
  <div class="grid w-full justify-items-center gap-8">
    <header class="grid justify-items-center gap-1.5 text-center">
      <p class="font-tcm09-mono text-[11px] tracking-[0.16em] text-tcm09-acc-ink uppercase">Workspace switcher</p>
      <h2 class="text-[clamp(1.5rem,4vw,2rem)] font-bold tracking-[-0.03em]">Deal your workspace like a hand of cards</h2>
    </header>
    <div id="tcm-09-hand" class="group/fan relative h-[27rem] w-full max-w-[24rem]">
      <nav class="absolute bottom-0 left-6" aria-label="Workspace">
        <ul id="tcm-09-menu" class="absolute bottom-[4.25rem] left-0">
        <li class="absolute bottom-0 left-0 origin-bottom-left rotate-[calc(var(--i)*-2deg)] translate-y-[calc(var(--i)*-3px)] [--i:4] transition-[rotate,translate,scale] duration-500 ease-[cubic-bezier(.34,1.45,.5,1)] delay-[calc((4-var(--i))*40ms)] group-data-open/fan:rotate-[calc(var(--i)*-2.5deg)] group-data-open/fan:translate-x-[calc(var(--i)*var(--i)*0.3rem)] group-data-open/fan:translate-y-[calc(var(--i)*-4.1rem)] group-data-open/fan:delay-[calc(var(--i)*50ms)] hover:z-10 group-data-open/fan:hover:scale-105 group-data-open/fan:focus-within:z-10 group-data-open/fan:focus-within:scale-105 motion-reduce:transition-none">
          <a href="#tcm-09-inbox" data-item class="flex w-[13.5rem] items-center gap-3 rounded-2xl bg-tcm09-card px-3.5 py-3 text-[14.5px] font-semibold text-tcm09-ink shadow-tcm09-card ring-1 ring-tcm09-line pointer-events-none invisible transition-[box-shadow,visibility] duration-500 group-data-open/fan:pointer-events-auto group-data-open/fan:visible hover:shadow-tcm09-lift hover:ring-tcm09-acc/50 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcm09-ring">
            <span aria-hidden="true" class="grid size-9 flex-none place-items-center rounded-xl bg-linear-to-br from-tcm09-acc/15 to-tcm09-acc2/15 text-tcm09-acc-ink"><svg viewBox="0 0 24 24" class="size-[18px]" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M3.5 5h17v14h-17zM3.5 13h5l1.5 2.5h4l1.5-2.5h5"/></svg></span>
            <span class="flex-1">Inbox</span>
            <span class="rounded-full bg-tcm09-acc/10 px-2 py-0.5 text-[11px] font-semibold text-tcm09-acc-ink tabular-nums">12</span>
            <kbd class="rounded-md px-1.5 py-0.5 font-tcm09-mono text-[10.5px] font-medium text-tcm09-mut ring-1 ring-tcm09-line">⌘I</kbd>
          </a>
        </li>
        <li class="absolute bottom-0 left-0 origin-bottom-left rotate-[calc(var(--i)*-2deg)] translate-y-[calc(var(--i)*-3px)] [--i:3] transition-[rotate,translate,scale] duration-500 ease-[cubic-bezier(.34,1.45,.5,1)] delay-[calc((4-var(--i))*40ms)] group-data-open/fan:rotate-[calc(var(--i)*-2.5deg)] group-data-open/fan:translate-x-[calc(var(--i)*var(--i)*0.3rem)] group-data-open/fan:translate-y-[calc(var(--i)*-4.1rem)] group-data-open/fan:delay-[calc(var(--i)*50ms)] hover:z-10 group-data-open/fan:hover:scale-105 group-data-open/fan:focus-within:z-10 group-data-open/fan:focus-within:scale-105 motion-reduce:transition-none">
          <a href="#tcm-09-docs" data-item class="flex w-[13.5rem] items-center gap-3 rounded-2xl bg-tcm09-card px-3.5 py-3 text-[14.5px] font-semibold text-tcm09-ink shadow-tcm09-card ring-1 ring-tcm09-line pointer-events-none invisible transition-[box-shadow,visibility] duration-500 group-data-open/fan:pointer-events-auto group-data-open/fan:visible hover:shadow-tcm09-lift hover:ring-tcm09-acc/50 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcm09-ring">
            <span aria-hidden="true" class="grid size-9 flex-none place-items-center rounded-xl bg-linear-to-br from-tcm09-acc/15 to-tcm09-acc2/15 text-tcm09-acc-ink"><svg viewBox="0 0 24 24" class="size-[18px]" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M4 20h4L19 9l-4-4L4 16v4zM13.5 6.5l4 4"/></svg></span>
            <span class="flex-1">Docs</span>
            <span class="rounded-full bg-tcm09-acc/10 px-2 py-0.5 text-[11px] font-semibold text-tcm09-acc-ink tabular-nums">48</span>
            <kbd class="rounded-md px-1.5 py-0.5 font-tcm09-mono text-[10.5px] font-medium text-tcm09-mut ring-1 ring-tcm09-line">⌘D</kbd>
          </a>
        </li>
        <li class="absolute bottom-0 left-0 origin-bottom-left rotate-[calc(var(--i)*-2deg)] translate-y-[calc(var(--i)*-3px)] [--i:2] transition-[rotate,translate,scale] duration-500 ease-[cubic-bezier(.34,1.45,.5,1)] delay-[calc((4-var(--i))*40ms)] group-data-open/fan:rotate-[calc(var(--i)*-2.5deg)] group-data-open/fan:translate-x-[calc(var(--i)*var(--i)*0.3rem)] group-data-open/fan:translate-y-[calc(var(--i)*-4.1rem)] group-data-open/fan:delay-[calc(var(--i)*50ms)] hover:z-10 group-data-open/fan:hover:scale-105 group-data-open/fan:focus-within:z-10 group-data-open/fan:focus-within:scale-105 motion-reduce:transition-none">
          <a href="#tcm-09-boards" data-item class="flex w-[13.5rem] items-center gap-3 rounded-2xl bg-tcm09-card px-3.5 py-3 text-[14.5px] font-semibold text-tcm09-ink shadow-tcm09-card ring-1 ring-tcm09-line pointer-events-none invisible transition-[box-shadow,visibility] duration-500 group-data-open/fan:pointer-events-auto group-data-open/fan:visible hover:shadow-tcm09-lift hover:ring-tcm09-acc/50 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcm09-ring">
            <span aria-hidden="true" class="grid size-9 flex-none place-items-center rounded-xl bg-linear-to-br from-tcm09-acc/15 to-tcm09-acc2/15 text-tcm09-acc-ink"><svg viewBox="0 0 24 24" class="size-[18px]" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M4 4h7v7H4zM13 4h7v7h-7zM4 13h7v7H4zM13 13h7v7h-7z"/></svg></span>
            <span class="flex-1">Boards</span>
            <span class="rounded-full bg-tcm09-acc/10 px-2 py-0.5 text-[11px] font-semibold text-tcm09-acc-ink tabular-nums">6</span>
            <kbd class="rounded-md px-1.5 py-0.5 font-tcm09-mono text-[10.5px] font-medium text-tcm09-mut ring-1 ring-tcm09-line">⌘B</kbd>
          </a>
        </li>
        <li class="absolute bottom-0 left-0 origin-bottom-left rotate-[calc(var(--i)*-2deg)] translate-y-[calc(var(--i)*-3px)] [--i:1] transition-[rotate,translate,scale] duration-500 ease-[cubic-bezier(.34,1.45,.5,1)] delay-[calc((4-var(--i))*40ms)] group-data-open/fan:rotate-[calc(var(--i)*-2.5deg)] group-data-open/fan:translate-x-[calc(var(--i)*var(--i)*0.3rem)] group-data-open/fan:translate-y-[calc(var(--i)*-4.1rem)] group-data-open/fan:delay-[calc(var(--i)*50ms)] hover:z-10 group-data-open/fan:hover:scale-105 group-data-open/fan:focus-within:z-10 group-data-open/fan:focus-within:scale-105 motion-reduce:transition-none">
          <a href="#tcm-09-reports" data-item class="flex w-[13.5rem] items-center gap-3 rounded-2xl bg-tcm09-card px-3.5 py-3 text-[14.5px] font-semibold text-tcm09-ink shadow-tcm09-card ring-1 ring-tcm09-line pointer-events-none invisible transition-[box-shadow,visibility] duration-500 group-data-open/fan:pointer-events-auto group-data-open/fan:visible hover:shadow-tcm09-lift hover:ring-tcm09-acc/50 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcm09-ring">
            <span aria-hidden="true" class="grid size-9 flex-none place-items-center rounded-xl bg-linear-to-br from-tcm09-acc/15 to-tcm09-acc2/15 text-tcm09-acc-ink"><svg viewBox="0 0 24 24" class="size-[18px]" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M5 20V10M12 20V4M19 20v-7"/></svg></span>
            <span class="flex-1">Reports</span>
            <span class="rounded-full bg-tcm09-acc/10 px-2 py-0.5 text-[11px] font-semibold text-tcm09-acc-ink tabular-nums">3</span>
            <kbd class="rounded-md px-1.5 py-0.5 font-tcm09-mono text-[10.5px] font-medium text-tcm09-mut ring-1 ring-tcm09-line">⌘R</kbd>
          </a>
        </li>
        <li class="absolute bottom-0 left-0 origin-bottom-left rotate-[calc(var(--i)*-2deg)] translate-y-[calc(var(--i)*-3px)] [--i:0] transition-[rotate,translate,scale] duration-500 ease-[cubic-bezier(.34,1.45,.5,1)] delay-[calc((4-var(--i))*40ms)] group-data-open/fan:rotate-[calc(var(--i)*-2.5deg)] group-data-open/fan:translate-x-[calc(var(--i)*var(--i)*0.3rem)] group-data-open/fan:translate-y-[calc(var(--i)*-4.1rem)] group-data-open/fan:delay-[calc(var(--i)*50ms)] hover:z-10 group-data-open/fan:hover:scale-105 group-data-open/fan:focus-within:z-10 group-data-open/fan:focus-within:scale-105 motion-reduce:transition-none">
          <a href="#tcm-09-exports" data-item class="flex w-[13.5rem] items-center gap-3 rounded-2xl bg-tcm09-card px-3.5 py-3 text-[14.5px] font-semibold text-tcm09-ink shadow-tcm09-card ring-1 ring-tcm09-line pointer-events-none invisible transition-[box-shadow,visibility] duration-500 group-data-open/fan:pointer-events-auto group-data-open/fan:visible hover:shadow-tcm09-lift hover:ring-tcm09-acc/50 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcm09-ring">
            <span aria-hidden="true" class="grid size-9 flex-none place-items-center rounded-xl bg-linear-to-br from-tcm09-acc/15 to-tcm09-acc2/15 text-tcm09-acc-ink"><svg viewBox="0 0 24 24" class="size-[18px]" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M12 4v12m0 0-4-4m4 4 4-4M5 20h14"/></svg></span>
            <span class="flex-1">Exports</span>
            
            <kbd class="rounded-md px-1.5 py-0.5 font-tcm09-mono text-[10.5px] font-medium text-tcm09-mut ring-1 ring-tcm09-line">⌘E</kbd>
          </a>
        </li>
        </ul>
        <div aria-hidden="true" class="pointer-events-none absolute bottom-[4.25rem] left-0 h-[3.75rem] w-[13.5rem] transition-opacity duration-300 group-data-open/fan:opacity-0">
          <span class="absolute inset-0 translate-y-[-8px] rotate-[-5deg] rounded-2xl bg-tcm09-card/70 ring-1 ring-tcm09-line"></span>
          <span class="absolute inset-0 translate-y-[-4px] rotate-[-2.5deg] rounded-2xl bg-tcm09-card/85 ring-1 ring-tcm09-line"></span>
          <span class="absolute inset-0 grid place-items-center rounded-2xl bg-tcm09-card text-[13px] font-medium text-tcm09-mut shadow-tcm09-card ring-1 ring-tcm09-line">5 spaces</span>
        </div>
        <button type="button" data-toggle aria-expanded="false" aria-controls="tcm-09-menu" class="flex min-h-13 cursor-pointer items-center gap-3 rounded-2xl bg-linear-to-br from-tcm09-acc to-tcm09-acc2 px-5 text-[14.5px] font-semibold tracking-[0.01em] text-tcm09-on shadow-tcm09-btn transition-[box-shadow,translate] duration-300 hover:-translate-y-0.5 active:translate-y-0 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tcm09-ring motion-reduce:transition-none">
          <span aria-hidden="true" class="grid size-7 place-items-center rounded-lg bg-white/20 text-[12px] font-bold">AC</span>
          Acme Workspace
          <svg viewBox="0 0 24 24" class="size-4 transition-transform duration-500 group-data-open/fan:rotate-180" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M6 15l6-6 6 6"/></svg>
        </button>
      </nav>
    </div>
    <p aria-hidden="true" class="max-w-full rounded-full bg-tcm09-card px-3.5 py-2 text-center font-tcm09-mono text-[11.5px] text-tcm09-mut ring-1 ring-tcm09-line ">group-data-open/fan: translate-y-[calc(var(--i)*-4.1rem)] · translate-x-[calc(var(--i)*var(--i)*0.3rem)] · rotate-[…-2.5deg]</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcm09-bg: #f6f3fb;
  --color-tcm09-bg: oklch(0.969 0.011 303.1);
  --color-tcm09-glow: #ddd6feb3;
  --color-tcm09-glow: oklch(0.894 0.055 293.3 / 0.7);
  --color-tcm09-card: #fffdff;
  --color-tcm09-card: oklch(0.996 0.003 325.6);
  --color-tcm09-ink: #1f1830;
  --color-tcm09-ink: oklch(0.23 0.046 296);
  --color-tcm09-mut: #655c78;
  --color-tcm09-mut: oklch(0.494 0.045 299.5);
  --color-tcm09-line: #e7e1f2;
  --color-tcm09-line: oklch(0.919 0.024 301.9);
  --color-tcm09-acc: #7c3aed;
  --color-tcm09-acc: oklch(0.541 0.247 293);
  --color-tcm09-acc2: #4f46e5;
  --color-tcm09-acc2: oklch(0.511 0.23 277);
  --color-tcm09-acc-ink: #6d28d9;
  --color-tcm09-acc-ink: oklch(0.491 0.241 292.6);
  --color-tcm09-on: #ffffff;
  --color-tcm09-on: oklch(1 0 0);
  --color-tcm09-ring: #6d28d9;
  --color-tcm09-ring: oklch(0.491 0.241 292.6);
  --font-tcm09-sans: 'DM Sans', system-ui, sans-serif;
  --font-tcm09-mono: 'DM Mono', ui-monospace, monospace;
  --shadow-tcm09-card: 0 12px 26px -14px oklch(0.35 0.12 295 / 0.45);
  --shadow-tcm09-lift: 0 18px 36px -12px oklch(0.45 0.2 295 / 0.55);
  --shadow-tcm09-btn: 0 14px 30px -12px oklch(0.45 0.22 290 / 0.7), inset 0 1px 0 oklch(1 0 0 / 0.25);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcm-09 {
  width: 100%;
  min-height: 100svh;
}
/* Dark theme: lilac night: the same tokens re-pointed, so every utility (and every /opacity modifier) follows. */

@media (prefers-color-scheme: dark) {
  .tcm-09:not([data-theme="light"]) {
    color-scheme: dark;
    --color-tcm09-bg: #100d18;
    --color-tcm09-bg: oklch(0.169 0.023 296.4);
    --color-tcm09-glow: #4c1d9559;
    --color-tcm09-glow: oklch(0.38 0.178 293.7 / 0.35);
    --color-tcm09-card: #1b1628;
    --color-tcm09-card: oklch(0.216 0.035 296.1);
    --color-tcm09-ink: #f2eefb;
    --color-tcm09-ink: oklch(0.956 0.018 300.1);
    --color-tcm09-mut: #ada4c4;
    --color-tcm09-mut: oklch(0.737 0.047 298.1);
    --color-tcm09-line: #2e2742;
    --color-tcm09-line: oklch(0.294 0.049 295.1);
    --color-tcm09-acc: #8b5cf6;
    --color-tcm09-acc: oklch(0.606 0.219 292.7);
    --color-tcm09-acc2: #6366f1;
    --color-tcm09-acc2: oklch(0.585 0.204 277.1);
    --color-tcm09-acc-ink: #c4b5fd;
    --color-tcm09-acc-ink: oklch(0.811 0.101 293.6);
    --color-tcm09-on: #ffffff;
    --color-tcm09-on: oklch(1 0 0);
    --color-tcm09-ring: #c4b5fd;
    --color-tcm09-ring: oklch(0.811 0.101 293.6);
  }
}

.tcm-09[data-theme="dark"] {
  color-scheme: dark;
  --color-tcm09-bg: #100d18;
  --color-tcm09-bg: oklch(0.169 0.023 296.4);
  --color-tcm09-glow: #4c1d9559;
  --color-tcm09-glow: oklch(0.38 0.178 293.7 / 0.35);
  --color-tcm09-card: #1b1628;
  --color-tcm09-card: oklch(0.216 0.035 296.1);
  --color-tcm09-ink: #f2eefb;
  --color-tcm09-ink: oklch(0.956 0.018 300.1);
  --color-tcm09-mut: #ada4c4;
  --color-tcm09-mut: oklch(0.737 0.047 298.1);
  --color-tcm09-line: #2e2742;
  --color-tcm09-line: oklch(0.294 0.049 295.1);
  --color-tcm09-acc: #8b5cf6;
  --color-tcm09-acc: oklch(0.606 0.219 292.7);
  --color-tcm09-acc2: #6366f1;
  --color-tcm09-acc2: oklch(0.585 0.204 277.1);
  --color-tcm09-acc-ink: #c4b5fd;
  --color-tcm09-acc-ink: oklch(0.811 0.101 293.6);
  --color-tcm09-on: #ffffff;
  --color-tcm09-on: oklch(1 0 0);
  --color-tcm09-ring: #c4b5fd;
  --color-tcm09-ring: oklch(0.811 0.101 293.6);
}
```

## JavaScript
```js
(() => {
  const root = document.getElementById('tcm-09-hand');
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
