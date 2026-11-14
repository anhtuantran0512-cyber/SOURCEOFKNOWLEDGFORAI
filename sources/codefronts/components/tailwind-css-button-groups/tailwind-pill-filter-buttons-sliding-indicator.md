---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-button-groups/tailwind-pill-filter-buttons-sliding-indicator/"
title: "Tailwind Pill Filter Button Group with Sliding Indicator (Anchor Positioning)"
section: "components"
category: "tailwind-css-button-groups"
category_name: "Tailwind CSS Button Groups"
description: "Category filter pills of different widths with a single highlight that glides to whichever is checked — and resizes to fit it."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Pill Filter Button Group with Sliding Indicator (Anchor Positioning)
Source: https://codefronts.com/components/tailwind-css-button-groups/tailwind-pill-filter-buttons-sliding-indicator/

Category filter pills of different widths with a single highlight that glides to whichever is checked — and resizes to fit it. The CSS original hard-coded every pill's pixel offset; this port lets CSS Anchor Positioning measure instead: the checked pill gets has-checked:[anchor-name:--tbg08-on] and the indicator sizes itself with w-[anchor-size(width)]. Change a label, add a count, swap the font &mdash; it still lines up.
## HTML
```html
<section class="tbg-08 w-full min-h-svh grid place-items-center bg-tbg08-bg bg-[radial-gradient(130%_130%_at_20%_0%,var(--color-tbg08-glow),transparent_70%)] px-5 py-14 font-tbg08-sans text-white" aria-label="Pill filter button group demo">
  <div class="grid w-full max-w-[36rem] gap-3.5">
    <p id="tbg08-label" class="ml-1 text-xs font-bold uppercase tracking-[0.14em] text-tbg08-acc-l">Browse by team</p>
    <div role="radiogroup" aria-labelledby="tbg08-label" class="relative flex w-fit max-w-full flex-wrap gap-1 rounded-[1.75rem] border border-white/12 bg-white/5 p-1 backdrop-blur-sm">
      <label class="group/p relative z-1 flex min-h-11 cursor-pointer items-center gap-2 rounded-full px-4.5 text-[14.5px] font-semibold text-white/72 transition-colors duration-300 hover:text-white has-checked:text-white has-checked:[anchor-name:--tbg08-on] has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-tbg08-acc-l not-supports-[anchor-name:--x]:has-checked:bg-tbg08-acc"><input type="radio" name="tbg08" class="sr-only" checked>All <span class="rounded-full bg-white/10 px-1.5 text-[11px] tabular-nums group-has-checked/p:bg-white/25">48</span></label>
      <label class="group/p relative z-1 flex min-h-11 cursor-pointer items-center gap-2 rounded-full px-4.5 text-[14.5px] font-semibold text-white/72 transition-colors duration-300 hover:text-white has-checked:text-white has-checked:[anchor-name:--tbg08-on] has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-tbg08-acc-l not-supports-[anchor-name:--x]:has-checked:bg-tbg08-acc"><input type="radio" name="tbg08" class="sr-only">Design <span class="rounded-full bg-white/10 px-1.5 text-[11px] tabular-nums group-has-checked/p:bg-white/25">12</span></label>
      <label class="group/p relative z-1 flex min-h-11 cursor-pointer items-center gap-2 rounded-full px-4.5 text-[14.5px] font-semibold text-white/72 transition-colors duration-300 hover:text-white has-checked:text-white has-checked:[anchor-name:--tbg08-on] has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-tbg08-acc-l not-supports-[anchor-name:--x]:has-checked:bg-tbg08-acc"><input type="radio" name="tbg08" class="sr-only">Engineering <span class="rounded-full bg-white/10 px-1.5 text-[11px] tabular-nums group-has-checked/p:bg-white/25">21</span></label>
      <label class="group/p relative z-1 flex min-h-11 cursor-pointer items-center gap-2 rounded-full px-4.5 text-[14.5px] font-semibold text-white/72 transition-colors duration-300 hover:text-white has-checked:text-white has-checked:[anchor-name:--tbg08-on] has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-tbg08-acc-l not-supports-[anchor-name:--x]:has-checked:bg-tbg08-acc"><input type="radio" name="tbg08" class="sr-only">Growth <span class="rounded-full bg-white/10 px-1.5 text-[11px] tabular-nums group-has-checked/p:bg-white/25">9</span></label>
      <label class="group/p relative z-1 flex min-h-11 cursor-pointer items-center gap-2 rounded-full px-4.5 text-[14.5px] font-semibold text-white/72 transition-colors duration-300 hover:text-white has-checked:text-white has-checked:[anchor-name:--tbg08-on] has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-tbg08-acc-l not-supports-[anchor-name:--x]:has-checked:bg-tbg08-acc"><input type="radio" name="tbg08" class="sr-only">Support <span class="rounded-full bg-white/10 px-1.5 text-[11px] tabular-nums group-has-checked/p:bg-white/25">6</span></label>
      <span aria-hidden="true" class="pointer-events-none absolute z-0 rounded-full bg-tbg08-acc shadow-[0_4px_18px_-4px_var(--color-tbg08-acc)] [position-anchor:--tbg08-on] top-[anchor(top)] left-[anchor(left)] h-[anchor-size(height)] w-[anchor-size(width)] transition-all duration-400 ease-[cubic-bezier(.34,1.3,.5,1)] motion-reduce:transition-none not-supports-[anchor-name:--x]:hidden"></span>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbg08-bg: #160820;
  --color-tbg08-glow: #2e1135;
  --color-tbg08-acc: #d8337f;
  --color-tbg08-acc: oklch(0.6 0.21 355);
  --color-tbg08-acc-l: #ff8cc1;
  --color-tbg08-acc-l: oklch(0.78 0.14 355);
  --font-tbg08-sans: 'Outfit', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, restated so the stage is sized before the browser build compiles. */

.tbg-08 {
  width: 100%;
  min-height: 100svh;
}
```
