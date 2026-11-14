---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-claymorphism/tailwind-badge-pill-tag-components-clay/"
title: "Tailwind Badge & Pill Tag Components (Clay Style)"
section: "design-styles"
category: "tailwind-css-claymorphism"
category_name: "Tailwind CSS Claymorphism"
description: "A full badge and tag system at clay scale: hue-driven status badges, count bubbles on clay avatars, removable filter tags, and a size scale from micro to hero."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Badge & Pill Tag Components (Clay Style)
Source: https://codefronts.com/design-styles/tailwind-css-claymorphism/tailwind-badge-pill-tag-components-clay/

A full badge and tag system at clay scale: hue-driven status badges, count bubbles on clay avatars, removable filter tags, and a size scale from micro to hero. Two custom utilities carry the recipe — tcl12-badge reads one [--tcl12-h:150] hue, tcl12-pill scales every shadow length from one [--tcl12-u:1.25] unit. New: removed tags leave the tab order, and clearing them all shows an empty state.
## HTML
```html
<section class="tcl-12 w-full min-h-svh grid place-items-center bg-tcl12-bg px-5 py-14 font-tcl12-sans text-tcl12-ink" aria-label="Clay badge and pill tag system demo">
  <div class="grid w-full justify-items-center gap-5">
    <div class="grid w-full max-w-[740px] gap-[clamp(20px,3vw,28px)] rounded-[42px] bg-tcl12-panel p-[clamp(22px,3.4vw,36px)] shadow-tcl12-panel">
      <div class="grid gap-3">
        <h3 class="text-[11.5px] font-bold uppercase tracking-[0.13em] text-tcl12-mut">Status badges</h3>
        <div class="flex flex-wrap items-center gap-2.5">
          <span class="tcl12-badge [--tcl12-h:150] inline-flex min-h-8.5 items-center gap-2 rounded-full px-3.75 text-[13px] font-semibold transition-transform duration-200 hover:-translate-y-0.5"><i aria-hidden="true" class="size-2.25 rounded-full bg-[oklch(0.58_0.16_var(--tcl12-h))] shadow-[inset_0_2px_3px_-1px_oklch(1_0_0/.7)]"></i>Published</span>
          <span class="tcl12-badge [--tcl12-h:85] inline-flex min-h-8.5 items-center gap-2 rounded-full px-3.75 text-[13px] font-semibold transition-transform duration-200 hover:-translate-y-0.5"><i aria-hidden="true" class="size-2.25 rounded-full bg-[oklch(0.58_0.16_var(--tcl12-h))] shadow-[inset_0_2px_3px_-1px_oklch(1_0_0/.7)]"></i>In review</span>
          <span class="tcl12-badge [--tcl12-h:25] inline-flex min-h-8.5 items-center gap-2 rounded-full px-3.75 text-[13px] font-semibold transition-transform duration-200 hover:-translate-y-0.5"><i aria-hidden="true" class="size-2.25 rounded-full bg-[oklch(0.58_0.16_var(--tcl12-h))] shadow-[inset_0_2px_3px_-1px_oklch(1_0_0/.7)]"></i>Blocked</span>
          <span class="tcl12-badge [--tcl12-h:250] inline-flex min-h-8.5 items-center gap-2 rounded-full px-3.75 text-[13px] font-semibold transition-transform duration-200 hover:-translate-y-0.5"><i aria-hidden="true" class="size-2.25 rounded-full bg-[oklch(0.58_0.16_var(--tcl12-h))] shadow-[inset_0_2px_3px_-1px_oklch(1_0_0/.7)]"></i>Scheduled</span>
          <span class="inline-flex min-h-8.5 items-center gap-2 rounded-full bg-tcl12-soft px-3.75 text-[13px] font-semibold text-tcl12-mut shadow-tcl12-ghost"><i aria-hidden="true" class="size-2.25 rounded-full bg-tcl12-mut"></i>Draft</span>
        </div>
      </div>
      <div class="grid gap-3">
        <h3 class="text-[11.5px] font-bold uppercase tracking-[0.13em] text-tcl12-mut">Size scale · one --tcl12-u unit</h3>
        <div class="flex flex-wrap items-baseline gap-2.5">
          <span class="tcl12-pill [--tcl12-u:.62] text-[11px]">micro</span>
          <span class="tcl12-pill [--tcl12-u:.8] text-[12.5px]">small</span>
          <span class="tcl12-pill [--tcl12-u:1] text-sm">base</span>
          <span class="tcl12-pill [--tcl12-u:1.25] text-base">large</span>
          <span class="tcl12-pill [--tcl12-u:1.5] text-lg">hero</span>
        </div>
      </div>
      <div class="grid gap-3">
        <h3 class="text-[11.5px] font-bold uppercase tracking-[0.13em] text-tcl12-mut">Count bubbles</h3>
        <div class="flex flex-wrap items-center gap-4">
          <span class="relative grid size-14 place-items-center rounded-[22px] bg-[oklch(0.85_0.09_30)] text-sm font-bold tracking-[0.02em] shadow-tcl12-avatar">JD<b aria-label="3 unread messages" class="absolute -top-1.75 -right-1.75 grid h-6 min-w-6 place-items-center rounded-full bg-tcl12-count px-1.5 text-xs font-bold text-white tabular-nums shadow-tcl12-count">3</b></span>
          <span class="relative grid size-14 place-items-center rounded-[22px] bg-[oklch(0.85_0.08_200)] text-sm font-bold tracking-[0.02em] shadow-tcl12-avatar">SR<b aria-label="12 unread messages" class="absolute -top-1.75 -right-1.75 grid h-6 min-w-6 place-items-center rounded-full bg-tcl12-hot px-1.5 text-xs font-bold text-white tabular-nums shadow-tcl12-count">12</b></span>
          <span class="relative grid size-14 place-items-center rounded-[22px] bg-[oklch(0.86_0.09_145)] text-sm font-bold tracking-[0.02em] shadow-tcl12-avatar">MK<b aria-label="New activity" class="absolute -top-1 -right-1 size-3.5 rounded-full bg-tcl12-live shadow-tcl12-count"></b></span>
        </div>
      </div>
      <div class="grid gap-3">
        <h3 class="text-[11.5px] font-bold uppercase tracking-[0.13em] text-tcl12-mut">Removable filter tags · pure CSS</h3>
        <div class="group/tags flex min-h-11 flex-wrap items-center gap-2.5">
          <label class="inline-flex min-h-11 cursor-pointer items-center gap-2.5 rounded-full bg-tcl12-tag pr-2 pl-4 text-[13.5px] font-semibold shadow-tcl12-tag transition-[scale,opacity,margin,translate,visibility] duration-300 ease-[cubic-bezier(.34,1.3,.5,1)] hover:-translate-y-0.5 has-checked:pointer-events-none has-checked:invisible has-checked:-me-3.5 has-checked:scale-55 has-checked:opacity-0 has-focus-visible:outline-3 has-focus-visible:outline-offset-3 has-focus-visible:outline-tcl12-ink">Motion<input type="checkbox" class="sr-only" aria-label="Remove tag: Motion"><span aria-hidden="true" class="relative size-7 rounded-full bg-tcl12-soft shadow-[inset_0_4px_7px_-4px_var(--color-tcl12-shade)] before:absolute before:top-1/2 before:left-1/2 before:h-0.5 before:w-2.5 before:-translate-1/2 before:rotate-45 before:rounded-sm before:bg-tcl12-mut after:absolute after:top-1/2 after:left-1/2 after:h-0.5 after:w-2.5 after:-translate-1/2 after:-rotate-45 after:rounded-sm after:bg-tcl12-mut"></span></label>
          <label class="inline-flex min-h-11 cursor-pointer items-center gap-2.5 rounded-full bg-tcl12-tag pr-2 pl-4 text-[13.5px] font-semibold shadow-tcl12-tag transition-[scale,opacity,margin,translate,visibility] duration-300 ease-[cubic-bezier(.34,1.3,.5,1)] hover:-translate-y-0.5 has-checked:pointer-events-none has-checked:invisible has-checked:-me-3.5 has-checked:scale-55 has-checked:opacity-0 has-focus-visible:outline-3 has-focus-visible:outline-offset-3 has-focus-visible:outline-tcl12-ink">Shadows<input type="checkbox" class="sr-only" aria-label="Remove tag: Shadows"><span aria-hidden="true" class="relative size-7 rounded-full bg-tcl12-soft shadow-[inset_0_4px_7px_-4px_var(--color-tcl12-shade)] before:absolute before:top-1/2 before:left-1/2 before:h-0.5 before:w-2.5 before:-translate-1/2 before:rotate-45 before:rounded-sm before:bg-tcl12-mut after:absolute after:top-1/2 after:left-1/2 after:h-0.5 after:w-2.5 after:-translate-1/2 after:-rotate-45 after:rounded-sm after:bg-tcl12-mut"></span></label>
          <label class="inline-flex min-h-11 cursor-pointer items-center gap-2.5 rounded-full bg-tcl12-tag pr-2 pl-4 text-[13.5px] font-semibold shadow-tcl12-tag transition-[scale,opacity,margin,translate,visibility] duration-300 ease-[cubic-bezier(.34,1.3,.5,1)] hover:-translate-y-0.5 has-checked:pointer-events-none has-checked:invisible has-checked:-me-3.5 has-checked:scale-55 has-checked:opacity-0 has-focus-visible:outline-3 has-focus-visible:outline-offset-3 has-focus-visible:outline-tcl12-ink">Radius<input type="checkbox" class="sr-only" aria-label="Remove tag: Radius"><span aria-hidden="true" class="relative size-7 rounded-full bg-tcl12-soft shadow-[inset_0_4px_7px_-4px_var(--color-tcl12-shade)] before:absolute before:top-1/2 before:left-1/2 before:h-0.5 before:w-2.5 before:-translate-1/2 before:rotate-45 before:rounded-sm before:bg-tcl12-mut after:absolute after:top-1/2 after:left-1/2 after:h-0.5 after:w-2.5 after:-translate-1/2 after:-rotate-45 after:rounded-sm after:bg-tcl12-mut"></span></label>
          <label class="inline-flex min-h-11 cursor-pointer items-center gap-2.5 rounded-full bg-tcl12-tag pr-2 pl-4 text-[13.5px] font-semibold shadow-tcl12-tag transition-[scale,opacity,margin,translate,visibility] duration-300 ease-[cubic-bezier(.34,1.3,.5,1)] hover:-translate-y-0.5 has-checked:pointer-events-none has-checked:invisible has-checked:-me-3.5 has-checked:scale-55 has-checked:opacity-0 has-focus-visible:outline-3 has-focus-visible:outline-offset-3 has-focus-visible:outline-tcl12-ink">Tailwind<input type="checkbox" class="sr-only" aria-label="Remove tag: Tailwind"><span aria-hidden="true" class="relative size-7 rounded-full bg-tcl12-soft shadow-[inset_0_4px_7px_-4px_var(--color-tcl12-shade)] before:absolute before:top-1/2 before:left-1/2 before:h-0.5 before:w-2.5 before:-translate-1/2 before:rotate-45 before:rounded-sm before:bg-tcl12-mut after:absolute after:top-1/2 after:left-1/2 after:h-0.5 after:w-2.5 after:-translate-1/2 after:-rotate-45 after:rounded-sm after:bg-tcl12-mut"></span></label>
          <label class="inline-flex min-h-11 cursor-pointer items-center gap-2.5 rounded-full bg-tcl12-tag pr-2 pl-4 text-[13.5px] font-semibold shadow-tcl12-tag transition-[scale,opacity,margin,translate,visibility] duration-300 ease-[cubic-bezier(.34,1.3,.5,1)] hover:-translate-y-0.5 has-checked:pointer-events-none has-checked:invisible has-checked:-me-3.5 has-checked:scale-55 has-checked:opacity-0 has-focus-visible:outline-3 has-focus-visible:outline-offset-3 has-focus-visible:outline-tcl12-ink">A11y<input type="checkbox" class="sr-only" aria-label="Remove tag: A11y"><span aria-hidden="true" class="relative size-7 rounded-full bg-tcl12-soft shadow-[inset_0_4px_7px_-4px_var(--color-tcl12-shade)] before:absolute before:top-1/2 before:left-1/2 before:h-0.5 before:w-2.5 before:-translate-1/2 before:rotate-45 before:rounded-sm before:bg-tcl12-mut after:absolute after:top-1/2 after:left-1/2 after:h-0.5 after:w-2.5 after:-translate-1/2 after:-rotate-45 after:rounded-sm after:bg-tcl12-mut"></span></label>
          <p class="hidden items-center gap-2 text-[13.5px] font-semibold text-tcl12-mut group-[:not(:has(input:not(:checked)))]/tags:flex">All filters cleared — showing every lesson.</p>
        </div>
      </div>
    </div>
    <p aria-hidden="true" class="rounded-full bg-white/55 px-4 py-2 text-center font-tcl12-mono text-[11.5px] text-tcl12-mut">@utility tcl12-badge [--tcl12-h] · @utility tcl12-pill [--tcl12-u] · has-checked: removal</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcl12-bg: #f2e7f5;
  --color-tcl12-bg: oklch(0.94 0.022 320);
  --color-tcl12-panel: #f6eff8;
  --color-tcl12-panel: oklch(0.96 0.014 320);
  --color-tcl12-soft: #f3ebf5;
  --color-tcl12-soft: oklch(0.95 0.016 320);
  --color-tcl12-clay: #ead1f0;
  --color-tcl12-clay: oklch(0.89 0.05 320);
  --color-tcl12-tag: #f0ddf4;
  --color-tcl12-tag: oklch(0.92 0.036 320);
  --color-tcl12-count: #9b49ae;
  --color-tcl12-count: oklch(0.55 0.17 320);
  --color-tcl12-hot: #cc272e;
  --color-tcl12-hot: oklch(0.55 0.2 25);
  --color-tcl12-live: #3fc168;
  --color-tcl12-live: oklch(0.72 0.17 150);
  --color-tcl12-shade: #86628f80;
  --color-tcl12-shade: oklch(0.55 0.08 320 / 0.5);
  --color-tcl12-light: #fffdfff2;
  --color-tcl12-light: oklch(1 0.01 320 / 0.95);
  --color-tcl12-ink: #311e36;
  --color-tcl12-ink: oklch(0.27 0.05 320);
  --color-tcl12-mut: #635068;
  --color-tcl12-mut: oklch(0.46 0.045 320);
  --font-tcl12-display: 'Bricolage Grotesque', system-ui, sans-serif;
  --font-tcl12-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tcl12-mono: 'JetBrains Mono', ui-monospace, monospace;
  --shadow-tcl12-panel: 0 30px 60px -24px var(--color-tcl12-shade), inset 0 -16px 28px -16px var(--color-tcl12-shade), inset 0 18px 28px -12px var(--color-tcl12-light);
  --shadow-tcl12-ghost: inset 0 5px 10px -5px var(--color-tcl12-shade), inset 0 -4px 8px -6px var(--color-tcl12-light);
  --shadow-tcl12-avatar: 0 12px 22px -10px var(--color-tcl12-shade), inset 0 -9px 15px -9px var(--color-tcl12-shade), inset 0 11px 15px -7px var(--color-tcl12-light);
  --shadow-tcl12-count: 0 0 0 3px var(--color-tcl12-panel), 0 6px 10px -4px var(--color-tcl12-shade), inset 0 5px 7px -4px oklch(1 0 0 / 0.55);
  --shadow-tcl12-tag: 0 8px 15px -6px var(--color-tcl12-shade), inset 0 -6px 11px -7px var(--color-tcl12-shade), inset 0 7px 11px -6px var(--color-tcl12-light);
}
/* Hue-driven badge: set [--tcl12-h:<hue>] on the element. */

@utility tcl12-badge {
  color: oklch(0.3 0.06 var(--tcl12-h, 320));
  background: oklch(0.88 0.075 var(--tcl12-h, 320));
  box-shadow: 0 7px 13px -5px oklch(0.55 0.1 var(--tcl12-h, 320) / 0.5), inset 0 -5px 9px -6px oklch(0.55 0.1 var(--tcl12-h, 320) / 0.55), inset 0 6px 9px -5px oklch(1 0.02 var(--tcl12-h, 320) / 0.95);
}
/* Unit-scaled pill: set [--tcl12-u:<number>] on the element. */

@utility tcl12-pill {
  display: inline-grid;
  place-items: center;
  min-height: calc(34px * var(--tcl12-u, 1));
  padding-inline: calc(18px * var(--tcl12-u, 1));
  border-radius: 9999px;
  font-weight: 600;
  background: var(--color-tcl12-clay);
  box-shadow: 0 calc(6px * var(--tcl12-u, 1)) calc(12px * var(--tcl12-u, 1)) calc(-4px * var(--tcl12-u, 1)) var(--color-tcl12-shade), inset 0 calc(-5px * var(--tcl12-u, 1)) calc(9px * var(--tcl12-u, 1)) -6px var(--color-tcl12-shade), inset 0 calc(6px * var(--tcl12-u, 1)) calc(9px * var(--tcl12-u, 1)) -5px var(--color-tcl12-light);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcl-12 {
  width: 100%;
  min-height: 100svh;
}
```
