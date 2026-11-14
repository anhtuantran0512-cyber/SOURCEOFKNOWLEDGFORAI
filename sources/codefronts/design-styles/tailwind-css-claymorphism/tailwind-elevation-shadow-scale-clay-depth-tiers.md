---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-claymorphism/tailwind-elevation-shadow-scale-clay-depth-tiers/"
title: "Tailwind Elevation Shadow Scale: Clay Depth Tiers"
section: "design-styles"
category: "tailwind-css-claymorphism"
category_name: "Tailwind CSS Claymorphism"
description: "Four elevation tiers — inset well, resting, raised, floating — driven by one integer."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Elevation Shadow Scale: Clay Depth Tiers
Source: https://codefronts.com/design-styles/tailwind-css-claymorphism/tailwind-elevation-shadow-scale-clay-depth-tiers/

Four elevation tiers — inset well, resting, raised, floating — driven by one integer. The port turns that integer into a functional utility: @utility tcl07-tier-* { --tcl07-elev: --value(integer) } mints tcl07-tier-1…tcl07-tier-4, so hover:tcl07-tier-3 promotes a card one tier. New: each tile shows a live elevation gauge, and the tiles are real focusable buttons.
## HTML
```html
<section class="tcl-07 w-full min-h-svh grid place-items-center bg-tcl07-bg bg-[radial-gradient(80%_55%_at_50%_0%,var(--color-tcl07-glow),transparent_66%)] px-5 py-14 font-tcl07-sans text-tcl07-ink" aria-label="Clay depth tiers for visual hierarchy demo">
  <div class="grid w-full justify-items-center gap-[clamp(24px,4vw,40px)]">
    <header class="grid max-w-[58ch] gap-2.5 text-center">
      <h2 class="font-tcl07-display text-[clamp(28px,4vw,40px)] font-extrabold leading-[1.05] tracking-[-0.03em] text-balance">Four tiers, one number</h2>
      <p class="text-[15px] leading-relaxed text-tcl07-mut text-pretty">Hover or tab to any tile: it is promoted exactly one tier. Every length is derived from <code class="font-tcl07-mono text-[13.5px]">--tcl07-elev</code>.</p>
    </header>
    <div class="grid w-full max-w-[920px] gap-4 rounded-[44px] bg-tcl07-well p-[clamp(20px,3vw,32px)] shadow-tcl07-well">
      <p class="text-center text-[11.5px] font-bold uppercase tracking-[0.13em] text-tcl07-mut">Tier 0 — inset well · holds content</p>
      <div class="grid grid-cols-[repeat(auto-fit,minmax(200px,1fr))] items-center gap-[clamp(16px,2.6vw,26px)]">
        <button type="button" class="group grid min-h-[156px] cursor-pointer content-center gap-1.5 rounded-[34px] bg-tcl07-clay p-6 text-left tcl07-clay tcl07-tier-1 transition-[--tcl07-elev,scale] duration-[400ms] ease-[cubic-bezier(.34,1.3,.5,1)] hover:tcl07-tier-2 focus-visible:tcl07-tier-2 focus-visible:outline-3 focus-visible:outline-offset-4 focus-visible:outline-tcl07-ink active:tcl07-tier-0 motion-reduce:transition-none">
          <b class="text-xs font-bold uppercase tracking-[0.14em] text-tcl07-ink/65">Tier 1</b>
          <span class="font-tcl07-display text-xl font-bold tracking-[-0.015em]">Resting surface</span>
          <span class="text-[13px] text-tcl07-ink/75">lists, groups, rows</span>
          <span aria-hidden="true" class="mt-2 flex gap-1"><i class="h-1.5 w-5 rounded-full bg-tcl07-ink"></i><i class="h-1.5 w-5 rounded-full bg-tcl07-ink/15 transition-colors group-hover:bg-tcl07-ink group-focus-visible:bg-tcl07-ink"></i><i class="h-1.5 w-5 rounded-full bg-tcl07-ink/15"></i><i class="h-1.5 w-5 rounded-full bg-tcl07-ink/15"></i></span>
        </button>
        <button type="button" class="group grid min-h-[156px] cursor-pointer content-center gap-1.5 rounded-[34px] bg-tcl07-clay p-6 text-left tcl07-clay tcl07-tier-2 transition-[--tcl07-elev,scale] duration-[400ms] ease-[cubic-bezier(.34,1.3,.5,1)] hover:tcl07-tier-3 focus-visible:tcl07-tier-3 focus-visible:outline-3 focus-visible:outline-offset-4 focus-visible:outline-tcl07-ink active:tcl07-tier-0 motion-reduce:transition-none">
          <b class="text-xs font-bold uppercase tracking-[0.14em] text-tcl07-ink/65">Tier 2</b>
          <span class="font-tcl07-display text-xl font-bold tracking-[-0.015em]">Raised surface</span>
          <span class="text-[13px] text-tcl07-ink/75">cards, buttons, tabs</span>
          <span aria-hidden="true" class="mt-2 flex gap-1"><i class="h-1.5 w-5 rounded-full bg-tcl07-ink"></i><i class="h-1.5 w-5 rounded-full bg-tcl07-ink"></i><i class="h-1.5 w-5 rounded-full bg-tcl07-ink/15 transition-colors group-hover:bg-tcl07-ink group-focus-visible:bg-tcl07-ink"></i><i class="h-1.5 w-5 rounded-full bg-tcl07-ink/15"></i></span>
        </button>
        <button type="button" class="group grid min-h-[156px] cursor-pointer content-center gap-1.5 rounded-[34px] bg-tcl07-clay p-6 text-left tcl07-clay tcl07-tier-3 transition-[--tcl07-elev,scale] duration-[400ms] ease-[cubic-bezier(.34,1.3,.5,1)] hover:tcl07-tier-4 hover:scale-[1.02] focus-visible:tcl07-tier-4 focus-visible:outline-3 focus-visible:outline-offset-4 focus-visible:outline-tcl07-ink active:tcl07-tier-0 active:scale-100 motion-reduce:transition-none">
          <b class="text-xs font-bold uppercase tracking-[0.14em] text-tcl07-ink/65">Tier 3</b>
          <span class="font-tcl07-display text-xl font-bold tracking-[-0.015em]">Floating surface</span>
          <span class="text-[13px] text-tcl07-ink/75">menus, popovers, FABs</span>
          <span aria-hidden="true" class="mt-2 flex gap-1"><i class="h-1.5 w-5 rounded-full bg-tcl07-ink"></i><i class="h-1.5 w-5 rounded-full bg-tcl07-ink"></i><i class="h-1.5 w-5 rounded-full bg-tcl07-ink"></i><i class="h-1.5 w-5 rounded-full bg-tcl07-ink/15 transition-colors group-hover:bg-tcl07-ink group-focus-visible:bg-tcl07-ink"></i></span>
        </button>
      </div>
    </div>
    <p aria-hidden="true" class="rounded-full bg-white/55 px-4 py-2 text-center font-tcl07-mono text-[11.5px] text-tcl07-mut">tcl07-tier-2 hover:tcl07-tier-3 active:tcl07-tier-0 · @utility --value(integer)</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@property --tcl07-elev {
  syntax: '<number>';
  inherits: false;
  initial-value: 2;
}

@theme {
  --color-tcl07-bg: #fbe0e1;
  --color-tcl07-bg: oklch(0.93 0.03 15);
  --color-tcl07-glow: #ffeee9;
  --color-tcl07-glow: oklch(0.97 0.03 30);
  --color-tcl07-well: #fadada;
  --color-tcl07-well: oklch(0.915 0.035 18);
  --color-tcl07-clay: #fdc8c7;
  --color-tcl07-clay: oklch(0.88 0.06 20);
  --color-tcl07-shade: #ae60648c;
  --color-tcl07-shade: oklch(0.58 0.1 18 / 0.55);
  --color-tcl07-light: #fffcf8f2;
  --color-tcl07-light: oklch(1 0.015 40 / 0.95);
  --color-tcl07-ink: #3e1e1e;
  --color-tcl07-ink: oklch(0.28 0.05 20);
  --color-tcl07-mut: #6f4a4a;
  --color-tcl07-mut: oklch(0.45 0.05 20);
  --font-tcl07-display: 'Bricolage Grotesque', system-ui, sans-serif;
  --font-tcl07-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tcl07-mono: 'JetBrains Mono', ui-monospace, monospace;
  --shadow-tcl07-well: inset 0 14px 26px -10px var(--color-tcl07-shade), inset 0 -12px 22px -12px var(--color-tcl07-light);
}
/* One integer per element: tcl07-tier-0 … tcl07-tier-4 (any integer works). */

@utility tcl07-tier-* {
  --tcl07-elev: --value(integer);
}

@utility tcl07-clay {
  translate: 0 calc(var(--tcl07-elev) * -1px);
  box-shadow: 0 calc(var(--tcl07-elev) * 9px) calc(var(--tcl07-elev) * 18px + 1px) calc(var(--tcl07-elev) * -5px) var(--color-tcl07-shade), inset 0 calc(var(--tcl07-elev) * -5px - 4px) calc(var(--tcl07-elev) * 9px + 8px) -8px var(--color-tcl07-shade), inset 0 calc(var(--tcl07-elev) * 6px + 4px) calc(var(--tcl07-elev) * 9px + 8px) -6px var(--color-tcl07-light);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcl-07 {
  width: 100%;
  min-height: 100svh;
}
```
