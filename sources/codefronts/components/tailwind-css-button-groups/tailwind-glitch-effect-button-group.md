---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-button-groups/tailwind-glitch-effect-button-group/"
title: "Tailwind Glitch Effect Button Group (Cyberpunk RGB-Split Audio Filter)"
section: "components"
category: "tailwind-css-button-groups"
category_name: "Tailwind CSS Button Groups"
description: "A cyberpunk audio-filter selector: picking a mode fires a 0.45s RGB-split glitch &mdash; cyan and magenta copies of the label…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Glitch Effect Button Group (Cyberpunk RGB-Split Audio Filter)
Source: https://codefronts.com/components/tailwind-css-button-groups/tailwind-glitch-effect-button-group/

A cyberpunk audio-filter selector: picking a mode fires a 0.45s RGB-split glitch &mdash; cyan and magenta copies of the label (before:content-[attr(data-txt)], after:…) jitter apart while the button slices with stepped clip-path keyframes &mdash; then settles into a steady neon state. A live equaliser above the buttons reshapes itself for each filter, so the choice has a visible meaning.
## HTML
```html
<section class="tbg-22 w-full min-h-svh grid place-items-center bg-tbg22-bg px-5 py-14 font-tbg22-mono text-tbg22-ink" aria-label="RGB-split glitch button group demo">
  <div class="group/fx grid w-full max-w-[33rem] gap-4">
    <div class="flex items-end justify-between">
      <p id="tbg22-label" class="ml-0.5 text-[11px] font-bold uppercase tracking-[0.26em] text-tbg22-mut">Audio filter</p>
      <div aria-hidden="true" class="flex h-10 items-end gap-1">
        <span class="h-[50%] w-1.5 rounded-sm bg-tbg22-acc shadow-[0_0_8px_var(--color-tbg22-acc)] transition-[height] duration-500 group-has-[#tbg22-bass:checked]/fx:h-[95%] group-has-[#tbg22-vocal:checked]/fx:h-[20%] group-has-[#tbg22-lofi:checked]/fx:h-[30%]"></span>
        <span class="h-[55%] w-1.5 rounded-sm bg-tbg22-acc shadow-[0_0_8px_var(--color-tbg22-acc)] transition-[height] duration-500 group-has-[#tbg22-bass:checked]/fx:h-[85%] group-has-[#tbg22-vocal:checked]/fx:h-[35%] group-has-[#tbg22-lofi:checked]/fx:h-[60%]"></span>
        <span class="h-[50%] w-1.5 rounded-sm bg-tbg22-acc shadow-[0_0_8px_var(--color-tbg22-acc)] transition-[height] duration-500 group-has-[#tbg22-bass:checked]/fx:h-[70%] group-has-[#tbg22-vocal:checked]/fx:h-[60%] group-has-[#tbg22-lofi:checked]/fx:h-[25%]"></span>
        <span class="h-[55%] w-1.5 rounded-sm bg-tbg22-acc shadow-[0_0_8px_var(--color-tbg22-acc)] transition-[height] duration-500 group-has-[#tbg22-bass:checked]/fx:h-[50%] group-has-[#tbg22-vocal:checked]/fx:h-[90%] group-has-[#tbg22-lofi:checked]/fx:h-[70%]"></span>
        <span class="h-[50%] w-1.5 rounded-sm bg-tbg22-acc shadow-[0_0_8px_var(--color-tbg22-acc)] transition-[height] duration-500 group-has-[#tbg22-bass:checked]/fx:h-[35%] group-has-[#tbg22-vocal:checked]/fx:h-[95%] group-has-[#tbg22-lofi:checked]/fx:h-[30%]"></span>
        <span class="h-[55%] w-1.5 rounded-sm bg-tbg22-acc shadow-[0_0_8px_var(--color-tbg22-acc)] transition-[height] duration-500 group-has-[#tbg22-bass:checked]/fx:h-[25%] group-has-[#tbg22-vocal:checked]/fx:h-[65%] group-has-[#tbg22-lofi:checked]/fx:h-[55%]"></span>
        <span class="h-[50%] w-1.5 rounded-sm bg-tbg22-acc shadow-[0_0_8px_var(--color-tbg22-acc)] transition-[height] duration-500 group-has-[#tbg22-bass:checked]/fx:h-[20%] group-has-[#tbg22-vocal:checked]/fx:h-[35%] group-has-[#tbg22-lofi:checked]/fx:h-[25%]"></span>
        <span class="h-[55%] w-1.5 rounded-sm bg-tbg22-acc shadow-[0_0_8px_var(--color-tbg22-acc)] transition-[height] duration-500 group-has-[#tbg22-bass:checked]/fx:h-[15%] group-has-[#tbg22-vocal:checked]/fx:h-[20%] group-has-[#tbg22-lofi:checked]/fx:h-[45%]"></span>
      </div>
    </div>
    <div role="radiogroup" aria-labelledby="tbg22-label" class="grid grid-cols-2 gap-2.5 sm:grid-cols-4">
      <label data-txt="CLEAN" class="relative grid min-h-13 cursor-pointer place-items-center rounded-[10px] border-[1.5px] border-tbg22-line bg-tbg22-key text-sm font-extrabold tracking-[0.1em] text-tbg22-mut transition-[color,border-color,background-color] duration-200 before:pointer-events-none before:absolute before:inset-0 before:grid before:place-items-center before:text-tbg22-cyan before:opacity-0 before:content-[attr(data-txt)] after:pointer-events-none after:absolute after:inset-0 after:grid after:place-items-center after:text-tbg22-mag after:opacity-0 after:content-[attr(data-txt)] hover:border-tbg22-hover hover:text-tbg22-ink has-checked:border-tbg22-acc has-checked:bg-tbg22-on has-checked:text-tbg22-acc has-checked:shadow-[0_0_20px_-8px_var(--color-tbg22-acc),inset_0_0_12px_-8px_var(--color-tbg22-acc)] has-checked:[text-shadow:0_0_10px_color-mix(in_oklab,var(--color-tbg22-acc)_70%,transparent)] has-checked:animate-tbg22-glitch has-checked:before:animate-tbg22-c has-checked:after:animate-tbg22-m has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-tbg22-acc motion-reduce:animate-none! motion-reduce:before:hidden motion-reduce:after:hidden"><input type="radio" name="tbg22" id="tbg22-clean" class="sr-only" checked>CLEAN</label>
      <label data-txt="BASS" class="relative grid min-h-13 cursor-pointer place-items-center rounded-[10px] border-[1.5px] border-tbg22-line bg-tbg22-key text-sm font-extrabold tracking-[0.1em] text-tbg22-mut transition-[color,border-color,background-color] duration-200 before:pointer-events-none before:absolute before:inset-0 before:grid before:place-items-center before:text-tbg22-cyan before:opacity-0 before:content-[attr(data-txt)] after:pointer-events-none after:absolute after:inset-0 after:grid after:place-items-center after:text-tbg22-mag after:opacity-0 after:content-[attr(data-txt)] hover:border-tbg22-hover hover:text-tbg22-ink has-checked:border-tbg22-acc has-checked:bg-tbg22-on has-checked:text-tbg22-acc has-checked:shadow-[0_0_20px_-8px_var(--color-tbg22-acc),inset_0_0_12px_-8px_var(--color-tbg22-acc)] has-checked:[text-shadow:0_0_10px_color-mix(in_oklab,var(--color-tbg22-acc)_70%,transparent)] has-checked:animate-tbg22-glitch has-checked:before:animate-tbg22-c has-checked:after:animate-tbg22-m has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-tbg22-acc motion-reduce:animate-none! motion-reduce:before:hidden motion-reduce:after:hidden"><input type="radio" name="tbg22" id="tbg22-bass" class="sr-only">BASS</label>
      <label data-txt="VOCAL" class="relative grid min-h-13 cursor-pointer place-items-center rounded-[10px] border-[1.5px] border-tbg22-line bg-tbg22-key text-sm font-extrabold tracking-[0.1em] text-tbg22-mut transition-[color,border-color,background-color] duration-200 before:pointer-events-none before:absolute before:inset-0 before:grid before:place-items-center before:text-tbg22-cyan before:opacity-0 before:content-[attr(data-txt)] after:pointer-events-none after:absolute after:inset-0 after:grid after:place-items-center after:text-tbg22-mag after:opacity-0 after:content-[attr(data-txt)] hover:border-tbg22-hover hover:text-tbg22-ink has-checked:border-tbg22-acc has-checked:bg-tbg22-on has-checked:text-tbg22-acc has-checked:shadow-[0_0_20px_-8px_var(--color-tbg22-acc),inset_0_0_12px_-8px_var(--color-tbg22-acc)] has-checked:[text-shadow:0_0_10px_color-mix(in_oklab,var(--color-tbg22-acc)_70%,transparent)] has-checked:animate-tbg22-glitch has-checked:before:animate-tbg22-c has-checked:after:animate-tbg22-m has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-tbg22-acc motion-reduce:animate-none! motion-reduce:before:hidden motion-reduce:after:hidden"><input type="radio" name="tbg22" id="tbg22-vocal" class="sr-only">VOCAL</label>
      <label data-txt="LO-FI" class="relative grid min-h-13 cursor-pointer place-items-center rounded-[10px] border-[1.5px] border-tbg22-line bg-tbg22-key text-sm font-extrabold tracking-[0.1em] text-tbg22-mut transition-[color,border-color,background-color] duration-200 before:pointer-events-none before:absolute before:inset-0 before:grid before:place-items-center before:text-tbg22-cyan before:opacity-0 before:content-[attr(data-txt)] after:pointer-events-none after:absolute after:inset-0 after:grid after:place-items-center after:text-tbg22-mag after:opacity-0 after:content-[attr(data-txt)] hover:border-tbg22-hover hover:text-tbg22-ink has-checked:border-tbg22-acc has-checked:bg-tbg22-on has-checked:text-tbg22-acc has-checked:shadow-[0_0_20px_-8px_var(--color-tbg22-acc),inset_0_0_12px_-8px_var(--color-tbg22-acc)] has-checked:[text-shadow:0_0_10px_color-mix(in_oklab,var(--color-tbg22-acc)_70%,transparent)] has-checked:animate-tbg22-glitch has-checked:before:animate-tbg22-c has-checked:after:animate-tbg22-m has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-tbg22-acc motion-reduce:animate-none! motion-reduce:before:hidden motion-reduce:after:hidden"><input type="radio" name="tbg22" id="tbg22-lofi" class="sr-only">LO-FI</label>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbg22-bg: #050506;
  --color-tbg22-key: #101014;
  --color-tbg22-line: #24242c;
  --color-tbg22-hover: #3a3a48;
  --color-tbg22-on: #0c1410;
  --color-tbg22-ink: #dcdce4;
  --color-tbg22-mut: #92929c;
  --color-tbg22-mut: oklch(0.67 0.012 285);
  --color-tbg22-acc: #2ee6a0;
  --color-tbg22-acc: oklch(0.82 0.17 160);
  --color-tbg22-cyan: #00f6ff;
  --color-tbg22-mag: #ff2bd0;
  --font-tbg22-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tbg22-glitch: tbg22-glitch 0.45s steps(2, end);
  --animate-tbg22-c: tbg22-c 0.45s steps(2, end);
  --animate-tbg22-m: tbg22-m 0.45s steps(2, end);

  @keyframes tbg22-glitch {
    0% {
      clip-path: inset(0 0 0 0);
    }

    20% {
      clip-path: inset(20% 0 55% 0);
    }

    40% {
      clip-path: inset(65% 0 12% 0);
    }

    60% {
      clip-path: inset(35% 0 40% 0);
    }

    80% {
      clip-path: inset(10% 0 75% 0);
    }

    100% {
      clip-path: inset(0 0 0 0);
    }
  }

  @keyframes tbg22-c {
    0%,
        100% {
      opacity: 0;
      translate: 0 0;
    }

    15% {
      opacity: 0.9;
      translate: -4px -2px;
    }

    45% {
      opacity: 0.9;
      translate: 3px 1px;
    }

    70% {
      opacity: 0.6;
      translate: -2px 2px;
    }
  }

  @keyframes tbg22-m {
    0%,
        100% {
      opacity: 0;
      translate: 0 0;
    }

    15% {
      opacity: 0.9;
      translate: 4px 2px;
    }

    45% {
      opacity: 0.9;
      translate: -3px -1px;
    }

    70% {
      opacity: 0.6;
      translate: 2px -2px;
    }
  }
}
/* Root rule: the full-bleed contract, restated so the stage is sized before the browser build compiles. */

.tbg-22 {
  width: 100%;
  min-height: 100svh;
}
```
