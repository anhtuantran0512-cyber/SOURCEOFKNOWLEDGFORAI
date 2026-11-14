---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-button-groups/tailwind-holographic-icon-segmented-control/"
title: "Tailwind Holographic Icon Segmented Control (Grid / List View Switcher)"
section: "components"
category: "tailwind-css-button-groups"
category_name: "Tailwind CSS Button Groups"
description: "An icon-only view switcher (Grid, List, Gallery, Map) with an iridescent foil thumb: four hue bands driven by an @property hue drift, a mix-blend-color-dodge…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Holographic Icon Segmented Control (Grid / List View Switcher)
Source: https://codefronts.com/components/tailwind-css-button-groups/tailwind-holographic-icon-segmented-control/

An icon-only view switcher (Grid, List, Gallery, Map) with an iridescent foil thumb: four hue bands driven by an @property hue drift, a mix-blend-color-dodge diffraction layer and a periodic white glare. A caption under the control spells out the current view, so the icon-only design no longer leaves anyone guessing.
## HTML
```html
<section class="tbg-19 w-full min-h-svh grid place-items-center bg-tbg19-bg bg-[radial-gradient(120%_120%_at_50%_0%,var(--color-tbg19-glow),transparent_70%)] px-5 py-14 font-tbg19-sans text-tbg19-ink" aria-label="Holographic icon segmented control demo">
  <div class="group/w grid w-full max-w-[26rem] gap-3.5">
    <p id="tbg19-label" class="ml-1 text-xs font-semibold uppercase tracking-[0.16em] text-tbg19-acc">View</p>
    <div role="radiogroup" aria-labelledby="tbg19-label" class="group/seg relative grid grid-cols-4 rounded-2xl border border-white/12 bg-white/4 p-1.5 backdrop-blur-sm">
      <label aria-label="Grid view" class="relative z-2 grid min-h-12 cursor-pointer place-items-center rounded-xl text-tbg19-mut transition-colors duration-300 hover:text-tbg19-ink has-checked:text-tbg19-on has-focus-visible:outline-3 has-focus-visible:outline-offset-3 has-focus-visible:outline-white"><input type="radio" name="tbg19" id="tbg19-1" class="sr-only" checked><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.1" aria-hidden="true"><rect x="4" y="4" width="7" height="7" rx="1.5"/><rect x="13" y="4" width="7" height="7" rx="1.5"/><rect x="4" y="13" width="7" height="7" rx="1.5"/><rect x="13" y="13" width="7" height="7" rx="1.5"/></svg></label>
      <label aria-label="List view" class="relative z-2 grid min-h-12 cursor-pointer place-items-center rounded-xl text-tbg19-mut transition-colors duration-300 hover:text-tbg19-ink has-checked:text-tbg19-on has-focus-visible:outline-3 has-focus-visible:outline-offset-3 has-focus-visible:outline-white"><input type="radio" name="tbg19" id="tbg19-2" class="sr-only"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" aria-hidden="true"><path d="M9 6h11M9 12h11M9 18h11M4.5 6h.01M4.5 12h.01M4.5 18h.01"/></svg></label>
      <label aria-label="Gallery view" class="relative z-2 grid min-h-12 cursor-pointer place-items-center rounded-xl text-tbg19-mut transition-colors duration-300 hover:text-tbg19-ink has-checked:text-tbg19-on has-focus-visible:outline-3 has-focus-visible:outline-offset-3 has-focus-visible:outline-white"><input type="radio" name="tbg19" id="tbg19-3" class="sr-only"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 15l5-4 4 3 3-2 6 5"/><circle cx="9" cy="9" r="1.4"/></svg></label>
      <label aria-label="Map view" class="relative z-2 grid min-h-12 cursor-pointer place-items-center rounded-xl text-tbg19-mut transition-colors duration-300 hover:text-tbg19-ink has-checked:text-tbg19-on has-focus-visible:outline-3 has-focus-visible:outline-offset-3 has-focus-visible:outline-white"><input type="radio" name="tbg19" id="tbg19-4" class="sr-only"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linejoin="round" aria-hidden="true"><path d="M9 4L3 6v14l6-2 6 2 6-2V4l-6 2-6-2zM9 4v14M15 6v14"/></svg></label>
      <span aria-hidden="true" class="pointer-events-none absolute top-1.5 bottom-1.5 left-1.5 z-1 w-[calc((100%-0.75rem)/4)] overflow-hidden rounded-xl bg-[repeating-linear-gradient(68deg,hsl(var(--tbg19-h)_92%_66%)_0_14px,hsl(calc(var(--tbg19-h)_+_60deg)_92%_66%)_14px_28px,hsl(calc(var(--tbg19-h)_+_130deg)_92%_66%)_28px_42px,hsl(calc(var(--tbg19-h)_+_200deg)_92%_66%)_42px_56px)] shadow-[0_6px_20px_-6px_hsl(var(--tbg19-h)_90%_60%/0.8)] animate-tbg19-drift transition-transform duration-400 ease-[cubic-bezier(.34,1.35,.5,1)] before:absolute before:inset-0 before:bg-[repeating-linear-gradient(-58deg,rgb(255_255_255/0.5)_0_4px,transparent_4px_16px)] before:opacity-55 before:mix-blend-color-dodge before:content-[''] after:absolute after:-inset-[40%] after:-translate-x-[80%] after:bg-[linear-gradient(110deg,transparent_40%,rgb(255_255_255/0.9)_50%,transparent_60%)] after:animate-tbg19-glare after:content-[''] group-has-[#tbg19-2:checked]/seg:translate-x-full group-has-[#tbg19-3:checked]/seg:translate-x-[200%] group-has-[#tbg19-4:checked]/seg:translate-x-[300%] motion-reduce:animate-none motion-reduce:after:animate-none motion-reduce:duration-200"></span>
    </div>
    <p class="ml-1 text-[13px] text-tbg19-mut">Showing as <b class="font-semibold text-tbg19-ink"><span class="hidden group-has-[#tbg19-1:checked]/w:inline">grid</span><span class="hidden group-has-[#tbg19-2:checked]/w:inline">list</span><span class="hidden group-has-[#tbg19-3:checked]/w:inline">gallery</span><span class="hidden group-has-[#tbg19-4:checked]/w:inline">map</span></b></p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";
/* @property is an at-rule with no utility: it makes the hue animatable. */

@property --tbg19-h {
  syntax: "<angle>";
  inherits: true;
  initial-value: 0deg;
}

@theme {
  --color-tbg19-bg: #0a0710;
  --color-tbg19-glow: #1c1629;
  --color-tbg19-ink: #f1edff;
  --color-tbg19-mut: #b5aed0;
  --color-tbg19-mut: oklch(0.77 0.04 295);
  --color-tbg19-on: #1a0d2e;
  --color-tbg19-acc: #c9b8ff;
  --font-tbg19-sans: 'Lexend', system-ui, sans-serif;
  --animate-tbg19-drift: tbg19-drift 6s linear infinite;
  --animate-tbg19-glare: tbg19-glare 6s ease-in-out infinite;

  @keyframes tbg19-drift {
    to {
      --tbg19-h: 360deg;
    }
  }

  @keyframes tbg19-glare {
    0%,
        55% {
      translate: -80% 0;
    }

    80%,
        100% {
      translate: 80% 0;
    }
  }
}
/* Root rule: the full-bleed contract, restated so the stage is sized before the browser build compiles. */

.tbg-19 {
  width: 100%;
  min-height: 100svh;
}
```
