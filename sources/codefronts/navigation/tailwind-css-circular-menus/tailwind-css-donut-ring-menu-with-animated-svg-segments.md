---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-circular-menus/tailwind-css-donut-ring-menu-with-animated-svg-segments/"
title: "Tailwind CSS Donut Ring Menu with Animated SVG Segments"
section: "navigation"
category: "tailwind-css-circular-menus"
category_name: "Tailwind CSS Circular Menus"
description: "A segmented ring that draws itself: tap the hub and five SVG arcs sweep in one after another with the classic dash trick &mdash; [stroke-dashoffset:L] &rarr;…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Donut Ring Menu with Animated SVG Segments
Source: https://codefronts.com/navigation/tailwind-css-circular-menus/tailwind-css-donut-ring-menu-with-animated-svg-segments/

A segmented ring that draws itself: tap the hub and five SVG arcs sweep in one after another with the classic dash trick &mdash; [stroke-dashoffset:L] &rarr; group-data-open/donut:[stroke-dashoffset:0] &mdash; while labels follow the curve. Hover or focus a label and its arc swells from 34 to 46 units via group-has-[[data-seg='2']:hover]/donut:, pure CSS reaching from HTML into SVG.
## HTML
```html
<section class="tcm-13 w-full min-h-svh grid place-items-center bg-tcm13-bg bg-[radial-gradient(55%_50%_at_50%_45%,var(--color-tcm13-glow),transparent_72%)] px-4 py-14 font-tcm13-sans text-tcm13-ink antialiased" aria-label="Donut ring menu demo">
  <div class="grid w-full justify-items-center gap-7">
    <header class="grid justify-items-center gap-1.5 text-center">
      <p class="font-tcm13-mono text-[11px] tracking-[0.16em] text-tcm13-acc-ink uppercase">Halo · Project app</p>
      <h2 class="text-[clamp(1.5rem,4vw,2rem)] font-semibold tracking-[-0.03em]">A ring that draws itself</h2>
    </header>
    <nav id="tcm-13-donut" class="group/donut relative size-[min(18.75rem,86vw)]" aria-label="Project sections">
      <svg viewBox="0 0 300 300" class="absolute inset-0 size-full overflow-visible drop-shadow-[0_12px_24px_oklch(0.3_0.1_250/0.3)]" aria-hidden="true">
        <circle cx="150" cy="150" r="108" class="fill-none stroke-tcm13-track [stroke-width:34] opacity-60"/>
          <path d="M 154.71 42.10 A 108 108 0 0 1 251.16 112.18" class="fill-none stroke-tcm13-c1 [stroke-dasharray:126.3] [stroke-dashoffset:126.3] [stroke-width:34] opacity-0 transition-[stroke-dashoffset,opacity,stroke-width] duration-600 ease-[cubic-bezier(.16,1,.3,1)] delay-[0ms] group-data-open/donut:[stroke-dashoffset:0] group-data-open/donut:opacity-100 group-has-[[data-seg='0']:is(:hover,:focus-visible)]/donut:[stroke-width:46] motion-reduce:transition-none"/>
          <path d="M 254.07 121.14 A 108 108 0 0 1 217.23 234.52" class="fill-none stroke-tcm13-c2 [stroke-dasharray:126.3] [stroke-dashoffset:126.3] [stroke-width:34] opacity-0 transition-[stroke-dashoffset,opacity,stroke-width] duration-600 ease-[cubic-bezier(.16,1,.3,1)] delay-[70ms] group-data-open/donut:[stroke-dashoffset:0] group-data-open/donut:opacity-100 group-has-[[data-seg='1']:is(:hover,:focus-visible)]/donut:[stroke-width:46] motion-reduce:transition-none"/>
          <path d="M 209.61 240.06 A 108 108 0 0 1 90.39 240.06" class="fill-none stroke-tcm13-c3 [stroke-dasharray:126.3] [stroke-dashoffset:126.3] [stroke-width:34] opacity-0 transition-[stroke-dashoffset,opacity,stroke-width] duration-600 ease-[cubic-bezier(.16,1,.3,1)] delay-[140ms] group-data-open/donut:[stroke-dashoffset:0] group-data-open/donut:opacity-100 group-has-[[data-seg='2']:is(:hover,:focus-visible)]/donut:[stroke-width:46] motion-reduce:transition-none"/>
          <path d="M 82.77 234.52 A 108 108 0 0 1 45.93 121.14" class="fill-none stroke-tcm13-c4 [stroke-dasharray:126.3] [stroke-dashoffset:126.3] [stroke-width:34] opacity-0 transition-[stroke-dashoffset,opacity,stroke-width] duration-600 ease-[cubic-bezier(.16,1,.3,1)] delay-[210ms] group-data-open/donut:[stroke-dashoffset:0] group-data-open/donut:opacity-100 group-has-[[data-seg='3']:is(:hover,:focus-visible)]/donut:[stroke-width:46] motion-reduce:transition-none"/>
          <path d="M 48.84 112.18 A 108 108 0 0 1 145.29 42.10" class="fill-none stroke-tcm13-c5 [stroke-dasharray:126.3] [stroke-dashoffset:126.3] [stroke-width:34] opacity-0 transition-[stroke-dashoffset,opacity,stroke-width] duration-600 ease-[cubic-bezier(.16,1,.3,1)] delay-[280ms] group-data-open/donut:[stroke-dashoffset:0] group-data-open/donut:opacity-100 group-has-[[data-seg='4']:is(:hover,:focus-visible)]/donut:[stroke-width:46] motion-reduce:transition-none"/>
      </svg>
      <ul id="tcm-13-menu" class="absolute inset-0">
          <li class="absolute top-[20.88%] left-[71.16%] -translate-1/2"><a href="#tcm-13-overview" data-item data-seg="0" class="block rotate-[36deg] rounded-md px-1.5 py-3 text-[12.5px] font-semibold tracking-[0.02em] text-white [text-shadow:0_1px_3px_oklch(0.2_0.05_250/0.6)] invisible opacity-0 translate-y-1 transition-[opacity,translate,visibility] duration-300 delay-[250ms] group-data-open/donut:visible group-data-open/donut:translate-y-0 group-data-open/donut:opacity-100 focus-visible:outline-2 focus-visible:outline-white">Overview</a></li>
          <li class="absolute top-[61.12%] left-[84.24%] -translate-1/2"><a href="#tcm-13-projects" data-item data-seg="1" class="block rotate-[288deg] rounded-md px-1.5 py-3 text-[12.5px] font-semibold tracking-[0.02em] text-white [text-shadow:0_1px_3px_oklch(0.2_0.05_250/0.6)] invisible opacity-0 translate-y-1 transition-[opacity,translate,visibility] duration-300 delay-[320ms] group-data-open/donut:visible group-data-open/donut:translate-y-0 group-data-open/donut:opacity-100 focus-visible:outline-2 focus-visible:outline-white">Projects</a></li>
          <li class="absolute top-[86.00%] left-[50.00%] -translate-1/2"><a href="#tcm-13-team" data-item data-seg="2" class="block rotate-[360deg] rounded-md px-1.5 py-3 text-[12.5px] font-semibold tracking-[0.02em] text-white [text-shadow:0_1px_3px_oklch(0.2_0.05_250/0.6)] invisible opacity-0 translate-y-1 transition-[opacity,translate,visibility] duration-300 delay-[390ms] group-data-open/donut:visible group-data-open/donut:translate-y-0 group-data-open/donut:opacity-100 focus-visible:outline-2 focus-visible:outline-white">Team</a></li>
          <li class="absolute top-[61.12%] left-[15.76%] -translate-1/2"><a href="#tcm-13-billing" data-item data-seg="3" class="block rotate-[432deg] rounded-md px-1.5 py-3 text-[12.5px] font-semibold tracking-[0.02em] text-white [text-shadow:0_1px_3px_oklch(0.2_0.05_250/0.6)] invisible opacity-0 translate-y-1 transition-[opacity,translate,visibility] duration-300 delay-[460ms] group-data-open/donut:visible group-data-open/donut:translate-y-0 group-data-open/donut:opacity-100 focus-visible:outline-2 focus-visible:outline-white">Billing</a></li>
          <li class="absolute top-[20.88%] left-[28.84%] -translate-1/2"><a href="#tcm-13-settings" data-item data-seg="4" class="block rotate-[324deg] rounded-md px-1.5 py-3 text-[12.5px] font-semibold tracking-[0.02em] text-white [text-shadow:0_1px_3px_oklch(0.2_0.05_250/0.6)] invisible opacity-0 translate-y-1 transition-[opacity,translate,visibility] duration-300 delay-[530ms] group-data-open/donut:visible group-data-open/donut:translate-y-0 group-data-open/donut:opacity-100 focus-visible:outline-2 focus-visible:outline-white">Settings</a></li>
      </ul>
      <button type="button" data-toggle aria-expanded="false" aria-controls="tcm-13-menu" class="absolute top-1/2 left-1/2 z-10 grid size-[33%] -translate-1/2 cursor-pointer place-content-center justify-items-center gap-1 rounded-full bg-[radial-gradient(circle_at_36%_30%,var(--color-tcm13-hub-hi),var(--color-tcm13-hub))] text-[13px] font-bold tracking-[0.12em] text-tcm13-ink uppercase shadow-tcm13-hub ring-1 ring-tcm13-line transition-[box-shadow,scale] duration-300 hover:scale-[1.03] group-data-open/donut:shadow-tcm13-hub-on focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tcm13-ring">
        <svg viewBox="0 0 24 24" class="size-5 group-data-open/donut:hidden" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M4 6h16M4 12h16M4 18h16"/></svg><svg viewBox="0 0 24 24" class="size-5 hidden group-data-open/donut:block" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6 6 18"/></svg><span>Menu</span>
      </button>
    </nav>
    <p aria-hidden="true" class="max-w-full rounded-full bg-tcm13-card px-3.5 py-2 text-center font-tcm13-mono text-[11.5px] text-tcm13-mut ring-1 ring-tcm13-line ">[stroke-dashoffset:L] → group-data-open/donut:[stroke-dashoffset:0] · group-has-[[data-seg]:hover]/donut:</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcm13-bg: #f1f5fb;
  --color-tcm13-bg: oklch(0.969 0.009 258.3);
  --color-tcm13-glow: #bfdbfeb3;
  --color-tcm13-glow: oklch(0.882 0.057 254.1 / 0.7);
  --color-tcm13-track: #dbe4f0;
  --color-tcm13-track: oklch(0.916 0.019 255.5);
  --color-tcm13-hub: #eef3fa;
  --color-tcm13-hub: oklch(0.962 0.011 256.7);
  --color-tcm13-hub-hi: #ffffff;
  --color-tcm13-hub-hi: oklch(1 0 0);
  --color-tcm13-ink: #13223a;
  --color-tcm13-ink: oklch(0.252 0.05 259.4);
  --color-tcm13-mut: #55657e;
  --color-tcm13-mut: oklch(0.503 0.045 259.2);
  --color-tcm13-line: #d8e1ee;
  --color-tcm13-line: oklch(0.907 0.02 257.5);
  --color-tcm13-c1: #2563eb;
  --color-tcm13-c1: oklch(0.546 0.215 262.9);
  --color-tcm13-c2: #0891b2;
  --color-tcm13-c2: oklch(0.609 0.111 221.7);
  --color-tcm13-c3: #059669;
  --color-tcm13-c3: oklch(0.596 0.127 163.2);
  --color-tcm13-c4: #d97706;
  --color-tcm13-c4: oklch(0.666 0.157 58.3);
  --color-tcm13-c5: #9333ea;
  --color-tcm13-c5: oklch(0.558 0.252 302.3);
  --color-tcm13-acc-ink: #1d4ed8;
  --color-tcm13-acc-ink: oklch(0.488 0.217 264.4);
  --color-tcm13-ring: #1d4ed8;
  --color-tcm13-ring: oklch(0.488 0.217 264.4);
  --color-tcm13-card: #ffffff;
  --color-tcm13-card: oklch(1 0 0);
  --font-tcm13-sans: 'Sora', system-ui, sans-serif;
  --font-tcm13-mono: 'JetBrains Mono', ui-monospace, monospace;
  --shadow-tcm13-hub: 0 18px 36px -14px oklch(0.3 0.1 255 / 0.55), inset 0 1px 0 oklch(1 0 0 / 0.5);
  --shadow-tcm13-hub-on: 0 0 0 7px oklch(0.6 0.18 255 / 0.18), 0 18px 36px -14px oklch(0.3 0.1 255 / 0.55);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcm-13 {
  width: 100%;
  min-height: 100svh;
}
/* Dark theme: steel night: the same tokens re-pointed, so every utility (and every /opacity modifier) follows. */

@media (prefers-color-scheme: dark) {
  .tcm-13:not([data-theme="light"]) {
    color-scheme: dark;
    --color-tcm13-bg: #0a1020;
    --color-tcm13-bg: oklch(0.176 0.035 267.3);
    --color-tcm13-glow: #1e3a8a66;
    --color-tcm13-glow: oklch(0.379 0.138 265.5 / 0.4);
    --color-tcm13-track: #1c2840;
    --color-tcm13-track: oklch(0.278 0.048 263.4);
    --color-tcm13-hub: #111a2e;
    --color-tcm13-hub: oklch(0.22 0.042 264.8);
    --color-tcm13-hub-hi: #22314f;
    --color-tcm13-hub-hi: oklch(0.315 0.058 263.3);
    --color-tcm13-ink: #e8effc;
    --color-tcm13-ink: oklch(0.951 0.019 263);
    --color-tcm13-mut: #9eb0cc;
    --color-tcm13-mut: oklch(0.753 0.045 259.2);
    --color-tcm13-line: #25334f;
    --color-tcm13-line: oklch(0.323 0.054 263.4);
    --color-tcm13-c1: #3b82f6;
    --color-tcm13-c1: oklch(0.623 0.188 259.8);
    --color-tcm13-c2: #06b6d4;
    --color-tcm13-c2: oklch(0.715 0.126 215.2);
    --color-tcm13-c3: #10b981;
    --color-tcm13-c3: oklch(0.696 0.149 162.5);
    --color-tcm13-c4: #f59e0b;
    --color-tcm13-c4: oklch(0.769 0.165 70.1);
    --color-tcm13-c5: #a855f7;
    --color-tcm13-c5: oklch(0.627 0.233 303.9);
    --color-tcm13-acc-ink: #93c5fd;
    --color-tcm13-acc-ink: oklch(0.809 0.096 251.8);
    --color-tcm13-ring: #93c5fd;
    --color-tcm13-ring: oklch(0.809 0.096 251.8);
    --color-tcm13-card: #111a2e;
    --color-tcm13-card: oklch(0.22 0.042 264.8);
  }
}

.tcm-13[data-theme="dark"] {
  color-scheme: dark;
  --color-tcm13-bg: #0a1020;
  --color-tcm13-bg: oklch(0.176 0.035 267.3);
  --color-tcm13-glow: #1e3a8a66;
  --color-tcm13-glow: oklch(0.379 0.138 265.5 / 0.4);
  --color-tcm13-track: #1c2840;
  --color-tcm13-track: oklch(0.278 0.048 263.4);
  --color-tcm13-hub: #111a2e;
  --color-tcm13-hub: oklch(0.22 0.042 264.8);
  --color-tcm13-hub-hi: #22314f;
  --color-tcm13-hub-hi: oklch(0.315 0.058 263.3);
  --color-tcm13-ink: #e8effc;
  --color-tcm13-ink: oklch(0.951 0.019 263);
  --color-tcm13-mut: #9eb0cc;
  --color-tcm13-mut: oklch(0.753 0.045 259.2);
  --color-tcm13-line: #25334f;
  --color-tcm13-line: oklch(0.323 0.054 263.4);
  --color-tcm13-c1: #3b82f6;
  --color-tcm13-c1: oklch(0.623 0.188 259.8);
  --color-tcm13-c2: #06b6d4;
  --color-tcm13-c2: oklch(0.715 0.126 215.2);
  --color-tcm13-c3: #10b981;
  --color-tcm13-c3: oklch(0.696 0.149 162.5);
  --color-tcm13-c4: #f59e0b;
  --color-tcm13-c4: oklch(0.769 0.165 70.1);
  --color-tcm13-c5: #a855f7;
  --color-tcm13-c5: oklch(0.627 0.233 303.9);
  --color-tcm13-acc-ink: #93c5fd;
  --color-tcm13-acc-ink: oklch(0.809 0.096 251.8);
  --color-tcm13-ring: #93c5fd;
  --color-tcm13-ring: oklch(0.809 0.096 251.8);
  --color-tcm13-card: #111a2e;
  --color-tcm13-card: oklch(0.22 0.042 264.8);
}
```

## JavaScript
```js
(() => {
  const root = document.getElementById('tcm-13-donut');
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
