---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-circular-menus/tailwind-css-glassmorphism-radial-menu-with-the-popover-api/"
title: "Tailwind CSS Glassmorphism Radial Menu with the Popover API"
section: "navigation"
category: "tailwind-css-circular-menus"
category_name: "Tailwind CSS Circular Menus"
description: "A frosted-glass app launcher on a vivid wallpaper, built on the native Popover API: popovertarget gives top-layer rendering, light-dismiss and Escape for…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Glassmorphism Radial Menu with the Popover API
Source: https://codefronts.com/navigation/tailwind-css-circular-menus/tailwind-css-glassmorphism-radial-menu-with-the-popover-api/

A frosted-glass app launcher on a vivid wallpaper, built on the native Popover API: popovertarget gives top-layer rendering, light-dismiss and Escape for free, and Tailwind&rsquo;s open: + starting:open: + transition-discrete animate it in and out. Six glass tiles ride the ring through two layers of backdrop-blur; the script is three lines that close the popover when you pick an app.
## HTML
```html
<section class="tcm-15 relative w-full min-h-svh grid place-items-center overflow-hidden bg-linear-140 from-tcm15-w1 via-tcm15-w2 to-tcm15-w3 px-5 py-14 font-tcm15-sans text-white antialiased" aria-label="Glassmorphism radial popover menu demo">
  <div aria-hidden="true" class="pointer-events-none absolute inset-0">
    <span class="absolute -top-16 -left-16 size-72 rounded-full bg-tcm15-b1/60 blur-[2px]"></span>
    <span class="absolute top-[30%] -right-12 size-56 rounded-full bg-tcm15-b2/50"></span>
    <span class="absolute -bottom-32 left-[22%] size-80 rounded-full bg-tcm15-b3/55"></span>
  </div>
  <div class="relative grid justify-items-center gap-6 text-center">
    <p class="font-tcm15-mono text-[12px] tracking-[0.2em] text-white/80 uppercase">Prism OS · Launcher</p>
    <p class="text-[clamp(3.5rem,12vw,5.5rem)] leading-none font-light tracking-[-0.05em] tabular-nums [text-shadow:0_2px_20px_oklch(0.3_0.15_290/0.4)]">09:41</p>
    <button type="button" popovertarget="tcm-15-pop" class="grid size-16 cursor-pointer place-items-center rounded-full bg-white/18 text-white ring-1 ring-white/40 shadow-tcm15-orb backdrop-blur-xl backdrop-saturate-150 transition-[scale,background-color] duration-300 hover:scale-107 hover:bg-white/25 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-white" aria-label="Open launcher">
      <svg viewBox="0 0 24 24" class="size-6" fill="currentColor" aria-hidden="true"><circle cx="6" cy="6" r="1.8"/><circle cx="12" cy="6" r="1.8"/><circle cx="18" cy="6" r="1.8"/><circle cx="6" cy="12" r="1.8"/><circle cx="12" cy="12" r="1.8"/><circle cx="18" cy="12" r="1.8"/><circle cx="6" cy="18" r="1.8"/><circle cx="12" cy="18" r="1.8"/><circle cx="18" cy="18" r="1.8"/></svg>
    </button>
    <p class="text-[13px] text-white/80">Esc or tap outside to close</p>
  </div>
  <nav id="tcm-15-pop" popover aria-label="Launcher" class="fixed inset-0 m-auto size-[min(21rem,90vw)] overflow-visible rounded-full border-0 bg-white/10 p-0 text-white shadow-tcm15-glass ring-1 ring-white/30 backdrop-blur-2xl backdrop-saturate-160 [--n:6] [--r:min(7.4rem,32vw)] opacity-0 scale-80 transition-[opacity,scale,display,overlay] transition-discrete duration-350 ease-[cubic-bezier(.34,1.45,.5,1)] open:opacity-100 open:scale-100 starting:open:opacity-0 starting:open:scale-75 backdrop:bg-tcm15-scrim/20 backdrop:backdrop-blur-[2px] motion-reduce:transition-none">
    <ul class="absolute inset-0">
        <li class="absolute inset-0 grid place-items-center pointer-events-none [--i:0] [--a:calc(360deg/var(--n)*var(--i)-90deg)]">
          <a href="#tcm-15-profile" data-item class="tcm15-polar pointer-events-auto grid w-[4.6rem] justify-items-center gap-1.5 rounded-2xl bg-white/14 px-1 py-3 text-[11.5px] font-semibold tracking-[0.02em] text-white ring-1 ring-white/30 backdrop-blur-md [text-shadow:0_1px_2px_oklch(0.3_0.1_290/0.5)] transition-[background-color,translate,scale] duration-300 hover:bg-white/28 hover:scale-105 focus-visible:bg-white/28 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white"><svg viewBox="0 0 24 24" class="size-5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M12 4.4a3.6 3.6 0 1 0 0 7.2 3.6 3.6 0 0 0 0-7.2zM5 20c.8-3.6 3.6-5.5 7-5.5s6.2 1.9 7 5.5"/></svg>Profile</a>
        </li>
        <li class="absolute inset-0 grid place-items-center pointer-events-none [--i:1] [--a:calc(360deg/var(--n)*var(--i)-90deg)]">
          <a href="#tcm-15-inbox" data-item class="tcm15-polar pointer-events-auto grid w-[4.6rem] justify-items-center gap-1.5 rounded-2xl bg-white/14 px-1 py-3 text-[11.5px] font-semibold tracking-[0.02em] text-white ring-1 ring-white/30 backdrop-blur-md [text-shadow:0_1px_2px_oklch(0.3_0.1_290/0.5)] transition-[background-color,translate,scale] duration-300 hover:bg-white/28 hover:scale-105 focus-visible:bg-white/28 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white"><svg viewBox="0 0 24 24" class="size-5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M3.5 5h17v14h-17zM3.5 13h5l1.5 2.5h4l1.5-2.5h5"/></svg>Inbox</a>
        </li>
        <li class="absolute inset-0 grid place-items-center pointer-events-none [--i:2] [--a:calc(360deg/var(--n)*var(--i)-90deg)]">
          <a href="#tcm-15-tasks" data-item class="tcm15-polar pointer-events-auto grid w-[4.6rem] justify-items-center gap-1.5 rounded-2xl bg-white/14 px-1 py-3 text-[11.5px] font-semibold tracking-[0.02em] text-white ring-1 ring-white/30 backdrop-blur-md [text-shadow:0_1px_2px_oklch(0.3_0.1_290/0.5)] transition-[background-color,translate,scale] duration-300 hover:bg-white/28 hover:scale-105 focus-visible:bg-white/28 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white"><svg viewBox="0 0 24 24" class="size-5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M4 4h16v16H4zM8.5 12.5l2.5 2.5 4.5-5"/></svg>Tasks</a>
        </li>
        <li class="absolute inset-0 grid place-items-center pointer-events-none [--i:3] [--a:calc(360deg/var(--n)*var(--i)-90deg)]">
          <a href="#tcm-15-stats" data-item class="tcm15-polar pointer-events-auto grid w-[4.6rem] justify-items-center gap-1.5 rounded-2xl bg-white/14 px-1 py-3 text-[11.5px] font-semibold tracking-[0.02em] text-white ring-1 ring-white/30 backdrop-blur-md [text-shadow:0_1px_2px_oklch(0.3_0.1_290/0.5)] transition-[background-color,translate,scale] duration-300 hover:bg-white/28 hover:scale-105 focus-visible:bg-white/28 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white"><svg viewBox="0 0 24 24" class="size-5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M5 20V10M12 20V4M19 20v-7"/></svg>Stats</a>
        </li>
        <li class="absolute inset-0 grid place-items-center pointer-events-none [--i:4] [--a:calc(360deg/var(--n)*var(--i)-90deg)]">
          <a href="#tcm-15-files" data-item class="tcm15-polar pointer-events-auto grid w-[4.6rem] justify-items-center gap-1.5 rounded-2xl bg-white/14 px-1 py-3 text-[11.5px] font-semibold tracking-[0.02em] text-white ring-1 ring-white/30 backdrop-blur-md [text-shadow:0_1px_2px_oklch(0.3_0.1_290/0.5)] transition-[background-color,translate,scale] duration-300 hover:bg-white/28 hover:scale-105 focus-visible:bg-white/28 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white"><svg viewBox="0 0 24 24" class="size-5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M4 7a2 2 0 0 1 2-2h4l2 2.5h6a2 2 0 0 1 2 2V17a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2z"/></svg>Files</a>
        </li>
        <li class="absolute inset-0 grid place-items-center pointer-events-none [--i:5] [--a:calc(360deg/var(--n)*var(--i)-90deg)]">
          <a href="#tcm-15-more" data-item class="tcm15-polar pointer-events-auto grid w-[4.6rem] justify-items-center gap-1.5 rounded-2xl bg-white/14 px-1 py-3 text-[11.5px] font-semibold tracking-[0.02em] text-white ring-1 ring-white/30 backdrop-blur-md [text-shadow:0_1px_2px_oklch(0.3_0.1_290/0.5)] transition-[background-color,translate,scale] duration-300 hover:bg-white/28 hover:scale-105 focus-visible:bg-white/28 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white"><svg viewBox="0 0 24 24" class="size-5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M12 3.5a8.5 8.5 0 1 0 0 17 8.5 8.5 0 0 0 0-17zM12 8.5v7M8.5 12h7"/></svg>More</a>
        </li>
    </ul>
    <span aria-hidden="true" class="absolute top-1/2 left-1/2 grid size-20 -translate-1/2 place-items-center rounded-full bg-white/12 font-tcm15-mono text-[11px] tracking-[0.16em] text-white/85 uppercase ring-1 ring-white/30">Apps</span>
  </nav>
  <div class="absolute bottom-6">
    <p aria-hidden="true" class="max-w-full rounded-full bg-tcm15-card px-3.5 py-2 text-center font-tcm15-mono text-[11.5px] text-tcm15-mut ring-1 ring-tcm15-line backdrop-blur">popover · open: · starting:open: · transition-discrete · backdrop-blur-2xl</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcm15-w1: #8b5cf6;
  --color-tcm15-w1: oklch(0.606 0.219 292.7);
  --color-tcm15-w2: #6366f1;
  --color-tcm15-w2: oklch(0.585 0.204 277.1);
  --color-tcm15-w3: #14b8a6;
  --color-tcm15-w3: oklch(0.704 0.123 182.5);
  --color-tcm15-b1: #f0abfc;
  --color-tcm15-b1: oklch(0.833 0.132 321.4);
  --color-tcm15-b2: #bef264;
  --color-tcm15-b2: oklch(0.897 0.179 126.7);
  --color-tcm15-b3: #fdba74;
  --color-tcm15-b3: oklch(0.837 0.117 66.3);
  --color-tcm15-scrim: #1e1b4b;
  --color-tcm15-scrim: oklch(0.257 0.086 281.3);
  --color-tcm15-card: #ffffff26;
  --color-tcm15-card: oklch(1 0 0 / 0.15);
  --color-tcm15-mut: #ffffffe6;
  --color-tcm15-mut: oklch(1 0 0 / 0.9);
  --color-tcm15-line: #ffffff4d;
  --color-tcm15-line: oklch(1 0 0 / 0.3);
  --font-tcm15-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tcm15-mono: 'Space Mono', ui-monospace, monospace;
  --shadow-tcm15-orb: 0 16px 40px -14px oklch(0.3 0.15 290 / 0.7), inset 0 1px 0 oklch(1 0 0 / 0.45);
  --shadow-tcm15-glass: 0 30px 90px -30px oklch(0.2 0.1 290 / 0.85), inset 0 1px 0 oklch(1 0 0 / 0.35);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcm-15 {
  width: 100%;
  min-height: 100svh;
}
/* The radial formula, as a real utility: position = (cos a · r, sin a · r). Items set --a and --r. */

@utility tcm15-polar {
  translate: calc(cos(var(--a)) * var(--r)) calc(sin(var(--a)) * var(--r));
}
/* Dark theme: deep prism: the same tokens re-pointed, so every utility (and every /opacity modifier) follows. */

@media (prefers-color-scheme: dark) {
  .tcm-15:not([data-theme="light"]) {
    color-scheme: dark;
    --color-tcm15-w1: #3b0764;
    --color-tcm15-w1: oklch(0.291 0.143 302.7);
    --color-tcm15-w2: #1e1b4b;
    --color-tcm15-w2: oklch(0.257 0.086 281.3);
    --color-tcm15-w3: #134e4a;
    --color-tcm15-w3: oklch(0.386 0.059 188.4);
    --color-tcm15-b1: #a21caf;
    --color-tcm15-b1: oklch(0.518 0.226 323.9);
    --color-tcm15-b2: #4d7c0f;
    --color-tcm15-b2: oklch(0.532 0.141 131.6);
    --color-tcm15-b3: #c2410c;
    --color-tcm15-b3: oklch(0.553 0.174 38.4);
    --color-tcm15-scrim: #000000;
    --color-tcm15-scrim: oklch(0 0 0);
    --color-tcm15-card: #ffffff1f;
    --color-tcm15-card: oklch(1 0 0 / 0.12);
    --color-tcm15-mut: #ffffffe6;
    --color-tcm15-mut: oklch(1 0 0 / 0.9);
    --color-tcm15-line: #ffffff40;
    --color-tcm15-line: oklch(1 0 0 / 0.25);
  }
}

.tcm-15[data-theme="dark"] {
  color-scheme: dark;
  --color-tcm15-w1: #3b0764;
  --color-tcm15-w1: oklch(0.291 0.143 302.7);
  --color-tcm15-w2: #1e1b4b;
  --color-tcm15-w2: oklch(0.257 0.086 281.3);
  --color-tcm15-w3: #134e4a;
  --color-tcm15-w3: oklch(0.386 0.059 188.4);
  --color-tcm15-b1: #a21caf;
  --color-tcm15-b1: oklch(0.518 0.226 323.9);
  --color-tcm15-b2: #4d7c0f;
  --color-tcm15-b2: oklch(0.532 0.141 131.6);
  --color-tcm15-b3: #c2410c;
  --color-tcm15-b3: oklch(0.553 0.174 38.4);
  --color-tcm15-scrim: #000000;
  --color-tcm15-scrim: oklch(0 0 0);
  --color-tcm15-card: #ffffff1f;
  --color-tcm15-card: oklch(1 0 0 / 0.12);
  --color-tcm15-mut: #ffffffe6;
  --color-tcm15-mut: oklch(1 0 0 / 0.9);
  --color-tcm15-line: #ffffff40;
  --color-tcm15-line: oklch(1 0 0 / 0.25);
}
```

## JavaScript
```js
(() => {
  const pop = document.getElementById('tcm-15-pop');
  if (!pop || pop.dataset.wired) return;
  pop.dataset.wired = '1';
  pop.querySelectorAll('[data-item]').forEach((a) => a.addEventListener('click', () => pop.hidePopover()));
})();
```
