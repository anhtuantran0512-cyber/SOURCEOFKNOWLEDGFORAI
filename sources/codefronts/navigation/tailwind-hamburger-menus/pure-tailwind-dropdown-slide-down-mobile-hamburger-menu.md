---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-hamburger-menus/pure-tailwind-dropdown-slide-down-mobile-hamburger-menu/"
title: "Pure Tailwind Dropdown Slide Down Mobile Hamburger Menu"
section: "navigation"
category: "tailwind-hamburger-menus"
category_name: "Tailwind Hamburger Menus"
description: "How to animate a menu to height:auto &mdash; the question with a decade of bad answers &mdash; solved twice in utilities: the [grid-template-rows:0fr] &rarr;…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure Tailwind Dropdown Slide Down Mobile Hamburger Menu
Source: https://codefronts.com/navigation/tailwind-hamburger-menus/pure-tailwind-dropdown-slide-down-mobile-hamburger-menu/

How to animate a menu to height:auto &mdash; the question with a decade of bad answers &mdash; solved twice in utilities: the [grid-template-rows:0fr] &rarr; 1fr technique that is Baseline everywhere, and the 2026-native interpolate-size: allow-keywords written out beside it as the alternative. They are alternatives, not layers &mdash; the second one swaps the panel's display model, so this demo ships the grid version and documents the other. Zero JavaScript.
## HTML
```html
<section class="thb-18 w-full min-h-svh bg-thb18-bg font-thb18-sans text-thb18-ink px-5 py-9" aria-label="Slide down dropdown hamburger menu demo">
  <div class="min-h-100 flex flex-col items-center justify-center gap-4 p-6.5 rounded-[18px] border border-thb18-edge bg-thb18-bg">
    <div class="group relative w-[min(420px,100%)] overflow-hidden rounded-2xl border border-thb18-edge bg-thb18-panel shadow-[0_16px_38px_-28px_oklch(0.35_0.06_50/0.55)]">
      <input type="checkbox" id="thb18-t" class="peer absolute w-px h-px overflow-hidden whitespace-nowrap [clip-path:inset(50%)]">
      <header class="flex items-center justify-between p-3 pl-5">
        <span class="flex items-center gap-2.5 text-[15.5px] font-extrabold tracking-[-0.01em]">
          <i class="w-5 h-5 rounded-full bg-[radial-gradient(circle_at_35%_30%,oklch(0.8_0.1_70),var(--color-thb18-acc)_70%)]" aria-hidden="true"></i>brewline
        </span>
        <label for="thb18-t" class="grid place-items-center w-11.5 h-11.5 rounded-xl border border-thb18-edge cursor-pointer select-none transition-[background,border-color] duration-200 hover:bg-thb18-hover peer-focus-visible:outline-2 peer-focus-visible:outline-thb18-acc peer-focus-visible:outline-offset-2">
          <span class="relative block w-4.5 h-3" aria-hidden="true">
            <i class="absolute left-0 top-0 w-4.5 h-0.5 rounded-sm bg-thb18-ink transition-[translate,rotate] duration-280 group-has-checked:translate-y-[5px] group-has-checked:rotate-45 motion-reduce:transition-none"></i>
            <i class="absolute left-0 top-[5px] w-4.5 h-0.5 rounded-sm bg-thb18-ink transition-[opacity] duration-200 group-has-checked:opacity-0 motion-reduce:transition-none"></i>
            <i class="absolute left-0 top-2.5 w-4.5 h-0.5 rounded-sm bg-thb18-ink transition-[translate,rotate] duration-280 group-has-checked:-translate-y-[5px] group-has-checked:-rotate-45 motion-reduce:transition-none"></i>
          </span>
        </label>
      </header>
      <nav aria-label="Primary" class="thb18-panel grid [grid-template-rows:0fr] transition-[grid-template-rows] duration-400 ease-thb18 group-has-checked:[grid-template-rows:1fr] motion-reduce:transition-none">
        <ul class="list-none min-h-0 overflow-hidden">
          <li style="--i:0" class="opacity-0 -translate-y-2 transition-[opacity,translate] duration-300 ease-thb18 group-has-checked:opacity-100 group-has-checked:translate-y-0 group-has-checked:[transition-delay:calc(120ms+var(--i)*40ms)] motion-reduce:translate-y-0 motion-reduce:duration-150"><a href="#menu" aria-current="page" class="group/l flex items-center justify-between min-h-12 px-5 border-t border-[color-mix(in_oklch,var(--color-thb18-edge)_55%,transparent)] text-[14.5px] font-semibold text-thb18-mut no-underline transition-[background,color] duration-150 hover:bg-thb18-hover hover:text-thb18-ink focus-visible:bg-thb18-hover focus-visible:text-thb18-ink focus-visible:outline-2 focus-visible:outline-thb18-acc focus-visible:-outline-offset-2 aria-current:text-thb18-acc">Menu<span class="opacity-0 -translate-x-1.5 transition-[opacity,translate] duration-200 group-hover/l:opacity-100 group-hover/l:translate-x-0 group-focus-visible/l:opacity-100 group-focus-visible/l:translate-x-0" aria-hidden="true">&rarr;</span></a></li>
          <li style="--i:1" class="opacity-0 -translate-y-2 transition-[opacity,translate] duration-300 ease-thb18 group-has-checked:opacity-100 group-has-checked:translate-y-0 group-has-checked:[transition-delay:calc(120ms+var(--i)*40ms)] motion-reduce:translate-y-0 motion-reduce:duration-150"><a href="#locations" class="group/l flex items-center justify-between min-h-12 px-5 border-t border-[color-mix(in_oklch,var(--color-thb18-edge)_55%,transparent)] text-[14.5px] font-semibold text-thb18-mut no-underline transition-[background,color] duration-150 hover:bg-thb18-hover hover:text-thb18-ink focus-visible:bg-thb18-hover focus-visible:text-thb18-ink focus-visible:outline-2 focus-visible:outline-thb18-acc focus-visible:-outline-offset-2">Locations<span class="opacity-0 -translate-x-1.5 transition-[opacity,translate] duration-200 group-hover/l:opacity-100 group-hover/l:translate-x-0 group-focus-visible/l:opacity-100 group-focus-visible/l:translate-x-0" aria-hidden="true">&rarr;</span></a></li>
          <li style="--i:2" class="opacity-0 -translate-y-2 transition-[opacity,translate] duration-300 ease-thb18 group-has-checked:opacity-100 group-has-checked:translate-y-0 group-has-checked:[transition-delay:calc(120ms+var(--i)*40ms)] motion-reduce:translate-y-0 motion-reduce:duration-150"><a href="#beans" class="group/l flex items-center justify-between min-h-12 px-5 border-t border-[color-mix(in_oklch,var(--color-thb18-edge)_55%,transparent)] text-[14.5px] font-semibold text-thb18-mut no-underline transition-[background,color] duration-150 hover:bg-thb18-hover hover:text-thb18-ink focus-visible:bg-thb18-hover focus-visible:text-thb18-ink focus-visible:outline-2 focus-visible:outline-thb18-acc focus-visible:-outline-offset-2">Beans &amp; gear<span class="opacity-0 -translate-x-1.5 transition-[opacity,translate] duration-200 group-hover/l:opacity-100 group-hover/l:translate-x-0 group-focus-visible/l:opacity-100 group-focus-visible/l:translate-x-0" aria-hidden="true">&rarr;</span></a></li>
          <li style="--i:3" class="opacity-0 -translate-y-2 transition-[opacity,translate] duration-300 ease-thb18 group-has-checked:opacity-100 group-has-checked:translate-y-0 group-has-checked:[transition-delay:calc(120ms+var(--i)*40ms)] motion-reduce:translate-y-0 motion-reduce:duration-150"><a href="#wholesale" class="group/l flex items-center justify-between min-h-12 px-5 border-t border-[color-mix(in_oklch,var(--color-thb18-edge)_55%,transparent)] text-[14.5px] font-semibold text-thb18-mut no-underline transition-[background,color] duration-150 hover:bg-thb18-hover hover:text-thb18-ink focus-visible:bg-thb18-hover focus-visible:text-thb18-ink focus-visible:outline-2 focus-visible:outline-thb18-acc focus-visible:-outline-offset-2">Wholesale<span class="opacity-0 -translate-x-1.5 transition-[opacity,translate] duration-200 group-hover/l:opacity-100 group-hover/l:translate-x-0 group-focus-visible/l:opacity-100 group-focus-visible/l:translate-x-0" aria-hidden="true">&rarr;</span></a></li>
          <li style="--i:4" class="opacity-0 -translate-y-2 transition-[opacity,translate] duration-300 ease-thb18 group-has-checked:opacity-100 group-has-checked:translate-y-0 group-has-checked:[transition-delay:calc(120ms+var(--i)*40ms)] motion-reduce:translate-y-0 motion-reduce:duration-150"><a href="#careers" class="group/l flex items-center justify-between min-h-12 px-5 border-t border-[color-mix(in_oklch,var(--color-thb18-edge)_55%,transparent)] text-[14.5px] font-semibold text-thb18-mut no-underline transition-[background,color] duration-150 hover:bg-thb18-hover hover:text-thb18-ink focus-visible:bg-thb18-hover focus-visible:text-thb18-ink focus-visible:outline-2 focus-visible:outline-thb18-acc focus-visible:-outline-offset-2">Careers<span class="opacity-0 -translate-x-1.5 transition-[opacity,translate] duration-200 group-hover/l:opacity-100 group-hover/l:translate-x-0 group-focus-visible/l:opacity-100 group-focus-visible/l:translate-x-0" aria-hidden="true">&rarr;</span></a></li>
        </ul>
      </nav>
    </div>
    <p class="w-[min(420px,100%)] text-center text-xs leading-relaxed text-thb18-mut text-pretty" aria-hidden="true">opens to <b class="font-semibold text-thb18-ink">height:auto</b> &mdash; grid <code class="font-thb18-mono text-[11px] px-1.5 py-0.5 rounded bg-thb18-code">0fr&rarr;1fr</code> base, <code class="font-thb18-mono text-[11px] px-1.5 py-0.5 rounded bg-thb18-code">interpolate-size</code> where supported. No max-height hack.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thb18-bg: #faf8f5;
  --color-thb18-bg: oklch(0.975 0.006 60);
  --color-thb18-panel: #ffffff;
  --color-thb18-panel: oklch(1 0 0);
  --color-thb18-hover: #f6f3ee;
  --color-thb18-hover: oklch(0.97 0.008 60);
  --color-thb18-edge: #e0dbd2;
  --color-thb18-edge: oklch(0.88 0.012 60);
  --color-thb18-code: #ebe5da;
  --color-thb18-code: oklch(0.92 0.01 60);
  --color-thb18-ink: #3a3229;
  --color-thb18-ink: oklch(0.25 0.02 45);
  --color-thb18-mut: #776e62;
  --color-thb18-mut: oklch(0.52 0.018 45);
  --color-thb18-acc: #b8793c;
  --color-thb18-acc: oklch(0.6 0.13 55);
  --font-thb18-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-thb18-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-thb18: cubic-bezier(0.2, 0.7, 0.2, 1);
}
/* The interpolate-size alternative is deliberately NOT shipped here, and is written out in the
   "How it works" and "Customize it" notes rather than as commented-out CSS: it swaps the panel's
   display model from grid to block, so it REPLACES the row-track utilities instead of layering on
   them. The grid technique is what ships — Baseline everywhere, and exact to content height. */
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh. It scopes the demo, and it holds the stage at full height in the
   moment before the browser build has compiled its utilities. */

.thb-18 {
  width: 100%;
  min-height: 100svh;
}
```
