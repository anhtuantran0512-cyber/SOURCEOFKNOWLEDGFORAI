---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-saas-dashboard-sidebar-dark-mode-switch/"
title: "Tailwind SaaS Dashboard Sidebar with Native Dark Mode Switch"
section: "layouts"
category: "tailwind-css-sidebar-layouts"
category_name: "Tailwind CSS Sidebar Layouts"
description: "The 2027 SaaS shell in one file: brand, nav, user badge and a real light/dark switch that re-skins the ENTIRE app from a single checkbox."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind SaaS Dashboard Sidebar with Native Dark Mode Switch
Source: https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-saas-dashboard-sidebar-dark-mode-switch/

The 2027 SaaS shell in one file: brand, nav, user badge and a real light/dark switch that re-skins the ENTIRE app from a single checkbox. The port's win is that the theme flip gets simpler in v4 &mdash; every utility already compiles to var(--color-tsl01-*), so one scoped rule re-points the tokens and the whole shell follows without a single conditional class.
## HTML
```html
<section class="tsl-01 w-full h-svh min-h-svh grid grid-cols-[250px_1fr] font-tsl01-sans bg-tsl01-bg text-tsl01-ink transition-colors duration-[350ms]">
  <aside class="flex flex-col gap-1.5 px-3.5 py-5 bg-tsl01-panel border-r border-tsl01-line transition-colors duration-[350ms]">
    <div class="flex items-center gap-2.5 px-2.5 pt-1 pb-[18px] text-base font-bold tracking-tight">
      <span aria-hidden="true" class="w-[26px] h-[26px] rounded-lg bg-[conic-gradient(from_210deg,var(--color-tsl01-accent),oklch(0.6_0.18_220))]"></span>Nimbus
    </div>
    <nav aria-label="Main" class="flex flex-col gap-0.5">
      <a href="#" aria-current="page" class="flex items-center gap-3 min-h-11 px-3 rounded-[10px] text-sm font-medium text-tsl01-mut no-underline transition-colors duration-200 hover:text-tsl01-ink hover:bg-tsl01-hover aria-[current=page]:text-tsl01-accentink aria-[current=page]:bg-tsl01-active focus-visible:outline-2 focus-visible:outline-tsl01-accent focus-visible:outline-offset-2"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-[18px] h-[18px] fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round]"><path d="M3 10.5 12 3l9 7.5M5.5 9.5V21h13V9.5"/></svg>Overview</a>
      <a href="#" class="flex items-center gap-3 min-h-11 px-3 rounded-[10px] text-sm font-medium text-tsl01-mut no-underline transition-colors duration-200 hover:text-tsl01-ink hover:bg-tsl01-hover focus-visible:outline-2 focus-visible:outline-tsl01-accent focus-visible:outline-offset-2"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-[18px] h-[18px] fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round]"><path d="M4 20V10m6 10V4m6 16v-7"/></svg>Analytics</a>
      <a href="#" class="flex items-center gap-3 min-h-11 px-3 rounded-[10px] text-sm font-medium text-tsl01-mut no-underline transition-colors duration-200 hover:text-tsl01-ink hover:bg-tsl01-hover focus-visible:outline-2 focus-visible:outline-tsl01-accent focus-visible:outline-offset-2"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-[18px] h-[18px] fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round]"><circle cx="9" cy="8" r="3.5"/><path d="M3 20c0-3.3 2.7-5.5 6-5.5s6 2.2 6 5.5m1-13.5a3.5 3.5 0 0 1 0 7"/></svg>Customers</a>
      <a href="#" class="flex items-center gap-3 min-h-11 px-3 rounded-[10px] text-sm font-medium text-tsl01-mut no-underline transition-colors duration-200 hover:text-tsl01-ink hover:bg-tsl01-hover focus-visible:outline-2 focus-visible:outline-tsl01-accent focus-visible:outline-offset-2"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-[18px] h-[18px] fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round]"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 10h18"/></svg>Billing</a>
      <a href="#" class="flex items-center gap-3 min-h-11 px-3 rounded-[10px] text-sm font-medium text-tsl01-mut no-underline transition-colors duration-200 hover:text-tsl01-ink hover:bg-tsl01-hover focus-visible:outline-2 focus-visible:outline-tsl01-accent focus-visible:outline-offset-2"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-[18px] h-[18px] fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round]"><circle cx="12" cy="12" r="3"/><path d="M12 2v3m0 14v3M2 12h3m14 0h3M4.9 4.9l2.1 2.1m10 10 2.1 2.1m0-14.2-2.1 2.1m-10 10-2.1 2.1"/></svg>Settings</a>
    </nav>
    <label class="tsl-01-switch mt-auto flex items-center gap-2.5 min-h-11 px-3 rounded-[10px] text-[13px] font-medium text-tsl01-mut cursor-pointer transition-colors hover:text-tsl01-ink">
      <input type="checkbox" id="tsl01-sw" class="sr-only">
      <span aria-hidden="true" class="tsl-01-track w-9 h-5 shrink-0 rounded-full bg-tsl01-line p-0.5 transition-colors duration-[250ms]">
        <span class="tsl-01-thumb block w-4 h-4 rounded-full bg-tsl01-ink transition-[translate,background-color] duration-[250ms] motion-reduce:transition-colors"></span>
      </span>Light mode
    </label>
    <div class="flex items-center gap-2.5 px-2.5 py-3 border-t border-tsl01-line text-[13px] leading-[1.35] font-medium transition-colors duration-[350ms]">
      <span aria-hidden="true" class="grid place-items-center w-8 h-8 shrink-0 rounded-full text-[11px] font-bold text-white bg-[linear-gradient(135deg,var(--color-tsl01-accent),oklch(0.6_0.18_220))]">AK</span>
      <span><strong class="block">Ada Kim</strong><small class="block text-[11.5px] font-normal text-tsl01-mut">[email protected]</small></span>
    </div>
  </aside>
  <main class="p-8 overflow-y-auto [scrollbar-gutter:stable]">
    <h1 class="text-[22px] font-semibold leading-tight mb-5">Good morning, Ada</h1>
    <div class="grid grid-cols-[repeat(auto-fit,minmax(150px,1fr))] gap-3.5">
      <article class="grid gap-2 p-[18px] rounded-2xl bg-tsl01-panel border border-tsl01-line transition-colors duration-[350ms]"><small class="text-[11px] font-medium uppercase tracking-[0.07em] text-tsl01-mut">MRR</small><strong class="text-[22px] font-semibold tabular-nums">$48,210</strong></article>
      <article class="grid gap-2 p-[18px] rounded-2xl bg-tsl01-panel border border-tsl01-line transition-colors duration-[350ms]"><small class="text-[11px] font-medium uppercase tracking-[0.07em] text-tsl01-mut">Active users</small><strong class="text-[22px] font-semibold tabular-nums">12,904</strong></article>
      <article class="grid gap-2 p-[18px] rounded-2xl bg-tsl01-panel border border-tsl01-line transition-colors duration-[350ms]"><small class="text-[11px] font-medium uppercase tracking-[0.07em] text-tsl01-mut">Churn</small><strong class="text-[22px] font-semibold tabular-nums">1.8%</strong></article>
    </div>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsl01-bg: #131519;
  --color-tsl01-bg: oklch(0.14 0.015 265);
  --color-tsl01-panel: #1a1d22;
  --color-tsl01-panel: oklch(0.17 0.018 265);
  --color-tsl01-ink: #e9ebee;
  --color-tsl01-ink: oklch(0.93 0.005 265);
  --color-tsl01-mut: #969aa2;
  --color-tsl01-mut: oklch(0.65 0.01 265);
  --color-tsl01-line: #3a3e45;
  --color-tsl01-line: oklch(0.28 0.015 265);
  --color-tsl01-accent: #4fd6a8;
  --color-tsl01-accent: oklch(0.7 0.15 165);
  /* Text-weight accent: the pill's label needs 4.5:1 against the tint in BOTH
       skins, which the display accent only clears on the dark ground. */
  --color-tsl01-accentink: #4fd6a8;
  --color-tsl01-accentink: oklch(0.7 0.15 165);
  --color-tsl01-hover: rgb(233 235 238 / 0.06);
  --color-tsl01-hover: color-mix(in oklab, oklch(0.93 0.005 265) 6%, transparent);
  --color-tsl01-active: rgb(79 214 168 / 0.16);
  --color-tsl01-active: color-mix(in oklab, oklch(0.7 0.15 165) 16%, transparent);
  --font-tsl01-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   utilities, so the shell is sized before the browser build has compiled. */

.tsl-01 {
  width: 100%;
  height: 100svh;
  min-height: 100svh;
  color-scheme: dark;
}
/* STATE — the switch input is the shell's descendant, not the track's sibling,
   so the resting look is utilities and the checked look is three scoped rules. */

#tsl01-sw:checked ~ .tsl-01-track {
  background: var(--color-tsl01-accent);
}

#tsl01-sw:checked ~ .tsl-01-track .tsl-01-thumb {
  translate: 16px 0;
  background: #fff;
}

#tsl01-sw:focus-visible ~ .tsl-01-track {
  outline: 2px solid var(--color-tsl01-accent);
  outline-offset: 2px;
}
/* THE LIGHT SKIN — the one thing that cannot be a utility, and should not be:
   re-pointing the tokens re-skins every utility that reads them, with no dark:
   duplicate anywhere in the markup. */

.tsl-01:has(.tsl-01-switch input:checked) {
  --color-tsl01-bg: oklch(0.97 0.004 100);
  --color-tsl01-panel: oklch(1 0 0);
  --color-tsl01-ink: oklch(0.25 0.02 265);
  --color-tsl01-mut: oklch(0.52 0.015 265);
  --color-tsl01-line: oklch(0.9 0.006 265);
  --color-tsl01-hover: color-mix(in oklab, oklch(0.25 0.02 265) 6%, transparent);
  --color-tsl01-accentink: oklch(0.48 0.15 165);
  color-scheme: light;
}

@media (prefers-reduced-motion: reduce) {
  .tsl-01,
    .tsl-01 * {
    transition-duration: 1ms !important;
  }
}
```
