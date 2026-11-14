---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-button-groups/tailwind-liquid-metal-segmented-control/"
title: "Tailwind Liquid Metal Segmented Control (Animated Chrome Thumb)"
section: "components"
category: "tailwind-css-button-groups"
category_name: "Tailwind CSS Button Groups"
description: "A dark segmented control with a polished-chrome thumb: an @property-registered angle spins the metallic gradient, a glint sweeps across it every few seconds,…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Liquid Metal Segmented Control (Animated Chrome Thumb)
Source: https://codefronts.com/components/tailwind-css-button-groups/tailwind-liquid-metal-segmented-control/

A dark segmented control with a polished-chrome thumb: an @property-registered angle spins the metallic gradient, a glint sweeps across it every few seconds, and the thumb squashes and stretches like mercury every time it lands. The CSS original only wobbled on the first move &mdash; this port gives each position its own squash keyframe, so the stretch replays on every change.
## HTML
```html
<section class="tbg-12 w-full min-h-svh grid place-items-center bg-tbg12-bg bg-[radial-gradient(120%_120%_at_50%_0%,var(--color-tbg12-glow),transparent_70%)] px-5 py-14 font-tbg12-sans text-tbg12-ink" aria-label="Liquid metal segmented control demo">
  <div class="grid w-full max-w-[28rem] gap-3.5">
    <p id="tbg12-label" class="ml-1 text-xs font-bold uppercase tracking-[0.16em] text-tbg12-mut">Rendering mode</p>
    <div role="radiogroup" aria-labelledby="tbg12-label" class="group/seg relative grid grid-cols-3 rounded-2xl border border-tbg12-line bg-tbg12-well p-1.5 shadow-[inset_0_2px_8px_rgb(0_0_0/0.6)]">
      <label class="relative z-2 grid min-h-12 cursor-pointer place-items-center rounded-xl text-[15px] font-semibold text-tbg12-mut transition-colors duration-300 hover:text-tbg12-ink has-checked:text-tbg12-on has-checked:[text-shadow:0_1px_0_rgb(255_255_255/0.45)] has-focus-visible:outline-3 has-focus-visible:outline-offset-3 has-focus-visible:outline-tbg12-focus"><input type="radio" name="tbg12" id="tbg12-1" class="sr-only" checked>Auto</label>
      <label class="relative z-2 grid min-h-12 cursor-pointer place-items-center rounded-xl text-[15px] font-semibold text-tbg12-mut transition-colors duration-300 hover:text-tbg12-ink has-checked:text-tbg12-on has-checked:[text-shadow:0_1px_0_rgb(255_255_255/0.45)] has-focus-visible:outline-3 has-focus-visible:outline-offset-3 has-focus-visible:outline-tbg12-focus"><input type="radio" name="tbg12" id="tbg12-2" class="sr-only">Metal</label>
      <label class="relative z-2 grid min-h-12 cursor-pointer place-items-center rounded-xl text-[15px] font-semibold text-tbg12-mut transition-colors duration-300 hover:text-tbg12-ink has-checked:text-tbg12-on has-checked:[text-shadow:0_1px_0_rgb(255_255_255/0.45)] has-focus-visible:outline-3 has-focus-visible:outline-offset-3 has-focus-visible:outline-tbg12-focus"><input type="radio" name="tbg12" id="tbg12-3" class="sr-only">Glass</label>
      <span aria-hidden="true" class="pointer-events-none absolute top-1.5 bottom-1.5 left-1.5 z-1 w-[calc((100%-0.75rem)/3)] animate-tbg12-sq1 rounded-xl shadow-tbg12-thumb transition-[translate] duration-500 ease-[cubic-bezier(.5,-0.2,.3,1.3)] group-has-[#tbg12-2:checked]/seg:translate-x-full group-has-[#tbg12-2:checked]/seg:animate-tbg12-sq2 group-has-[#tbg12-3:checked]/seg:translate-x-[200%] group-has-[#tbg12-3:checked]/seg:animate-tbg12-sq3 motion-reduce:animate-none! motion-reduce:duration-300">
        <span class="absolute inset-0 overflow-hidden rounded-xl bg-[linear-gradient(var(--tbg12-sheen),#f4f6fb_0%,#c3cad9_30%,#7a8398_55%,#dfe4ee_80%,#f4f6fb_100%)] animate-tbg12-sheen after:absolute after:inset-0 after:-translate-x-[120%] after:bg-[linear-gradient(105deg,transparent_35%,rgb(255_255_255/0.85)_50%,transparent_65%)] after:animate-tbg12-glint after:content-[''] motion-reduce:animate-none motion-reduce:after:animate-none"></span>
      </span>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";
/* @property is an at-rule with no utility: it makes the gradient angle animatable. */

@property --tbg12-sheen {
  syntax: "<angle>";
  inherits: true;
  initial-value: 0deg;
}

@theme {
  --color-tbg12-bg: #0c0e14;
  --color-tbg12-glow: #232834;
  --color-tbg12-well: #171a22;
  --color-tbg12-line: #2a2f3c;
  --color-tbg12-ink: #eef1f7;
  --color-tbg12-mut: #a2aabd;
  --color-tbg12-mut: oklch(0.74 0.025 265);
  --color-tbg12-on: #11141c;
  --color-tbg12-focus: #9fb0ff;
  --shadow-tbg12-thumb: 0 4px 14px -4px rgb(0 0 0 / 0.8), inset 0 1px 1px rgb(255 255 255 / 0.9), inset 0 -2px 4px rgb(0 0 0 / 0.3);
  --font-tbg12-sans: 'Familjen Grotesk', system-ui, sans-serif;
  --animate-tbg12-sheen: tbg12-sheen 5s linear infinite;
  --animate-tbg12-glint: tbg12-glint 5s ease-in-out infinite;
  --animate-tbg12-sq1: tbg12-sq1 0.5s ease;
  --animate-tbg12-sq2: tbg12-sq2 0.5s ease;
  --animate-tbg12-sq3: tbg12-sq3 0.5s ease;

  @keyframes tbg12-sheen {
    to {
      --tbg12-sheen: 360deg;
    }
  }

  @keyframes tbg12-glint {
    0%,
        60% {
      translate: -120% 0;
    }

    80%,
        100% {
      translate: 120% 0;
    }
  }

  @keyframes tbg12-sq1 {
    40% {
      scale: 1.16 0.82;
    }

    70% {
      scale: 0.94 1.08;
    }

    100% {
      scale: 1 1;
    }
  }

  @keyframes tbg12-sq2 {
    40% {
      scale: 1.16 0.82;
    }

    70% {
      scale: 0.94 1.08;
    }

    100% {
      scale: 1 1;
    }
  }

  @keyframes tbg12-sq3 {
    40% {
      scale: 1.16 0.82;
    }

    70% {
      scale: 0.94 1.08;
    }

    100% {
      scale: 1 1;
    }
  }
}
/* Root rule: the full-bleed contract, restated so the stage is sized before the browser build compiles. */

.tbg-12 {
  width: 100%;
  min-height: 100svh;
}
```
