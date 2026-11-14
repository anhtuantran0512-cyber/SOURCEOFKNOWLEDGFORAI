---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-radio-buttons/tailwind-liquid-wave-fill-radio-button/"
title: "Tailwind Liquid Wave Fill Radio Button"
section: "components"
category: "tailwind-css-radio-buttons"
category_name: "Tailwind CSS Radio Buttons"
description: "Circular options that fill with liquid when selected: an aqua wave rises inside the checked circle, its surface rolling with two counter-rotating crests."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Liquid Wave Fill Radio Button
Source: https://codefronts.com/components/tailwind-css-radio-buttons/tailwind-liquid-wave-fill-radio-button/

Circular options that fill with liquid when selected: an aqua wave rises inside the checked circle, its surface rolling with two counter-rotating crests. The port splits the motion across v4's individual transform properties — translate raises the water, rotate rolls it — so the rise transitions while the roll loops, with no combined keyframe.
## HTML
```html
<section class="trb-18 w-full min-h-svh grid place-items-center bg-trb18-bg px-6 py-14 font-trb18-sans text-trb18-ink" aria-label="Liquid wave fill radio buttons demo">
  <fieldset>
    <legend class="text-center text-[26px] font-extrabold tracking-[-0.025em]">Roast strength</legend>
    <div class="mt-8 flex flex-wrap justify-center gap-8">
      <label class="group relative grid cursor-pointer justify-items-center gap-3">
        <input type="radio" name="trb-18" value="mild" class="sr-only">
        <span aria-hidden="true" class="relative grid size-[88px] place-items-center overflow-hidden rounded-full border-[2.5px] border-trb18-line bg-white transition-[border-color,box-shadow] duration-300 group-hover:border-trb18-aqua group-has-checked:border-trb18-aqua group-has-checked:shadow-trb18-cup group-has-focus-visible:outline-3 group-has-focus-visible:outline-offset-3 group-has-focus-visible:outline-trb18-ink">
          <span class="pointer-events-none absolute top-full left-1/2 -ml-[110%] aspect-square w-[220%] translate-y-[4%] rounded-[42%] bg-trb18-aqua transition-[translate] duration-1000 ease-trb18-rise group-has-checked:-translate-y-[64%] group-has-checked:animate-trb18-roll motion-reduce:group-has-checked:animate-none"></span>
          <span class="pointer-events-none absolute top-full left-1/2 -ml-[110%] aspect-square w-[220%] translate-y-[4%] rounded-[44%] bg-trb18-deep opacity-50 transition-[translate] duration-1000 ease-trb18-rise group-has-checked:-translate-y-[64%] group-has-checked:animate-trb18-roll-back motion-reduce:group-has-checked:animate-none"></span>
          <span class="relative text-[26px] font-extrabold text-trb18-letter transition-colors delay-200 duration-400 group-has-checked:text-white">S</span>
        </span>
        <span class="grid justify-items-center"><span class="text-[15px] font-bold text-trb18-mut transition-colors group-has-checked:text-trb18-ink">Smooth</span><span class="text-xs text-trb18-mut">Caramel, low acid</span></span>
      </label>
      <label class="group relative grid cursor-pointer justify-items-center gap-3">
        <input type="radio" name="trb-18" value="medium" class="sr-only" checked>
        <span aria-hidden="true" class="relative grid size-[88px] place-items-center overflow-hidden rounded-full border-[2.5px] border-trb18-line bg-white transition-[border-color,box-shadow] duration-300 group-hover:border-trb18-aqua group-has-checked:border-trb18-aqua group-has-checked:shadow-trb18-cup group-has-focus-visible:outline-3 group-has-focus-visible:outline-offset-3 group-has-focus-visible:outline-trb18-ink">
          <span class="pointer-events-none absolute top-full left-1/2 -ml-[110%] aspect-square w-[220%] translate-y-[4%] rounded-[42%] bg-trb18-aqua transition-[translate] duration-1000 ease-trb18-rise group-has-checked:-translate-y-[64%] group-has-checked:animate-trb18-roll motion-reduce:group-has-checked:animate-none"></span>
          <span class="pointer-events-none absolute top-full left-1/2 -ml-[110%] aspect-square w-[220%] translate-y-[4%] rounded-[44%] bg-trb18-deep opacity-50 transition-[translate] duration-1000 ease-trb18-rise group-has-checked:-translate-y-[64%] group-has-checked:animate-trb18-roll-back motion-reduce:group-has-checked:animate-none"></span>
          <span class="relative text-[26px] font-extrabold text-trb18-letter transition-colors delay-200 duration-400 group-has-checked:text-white">M</span>
        </span>
        <span class="grid justify-items-center"><span class="text-[15px] font-bold text-trb18-mut transition-colors group-has-checked:text-trb18-ink">Medium</span><span class="text-xs text-trb18-mut">Balanced, cocoa</span></span>
      </label>
      <label class="group relative grid cursor-pointer justify-items-center gap-3">
        <input type="radio" name="trb-18" value="bold" class="sr-only">
        <span aria-hidden="true" class="relative grid size-[88px] place-items-center overflow-hidden rounded-full border-[2.5px] border-trb18-line bg-white transition-[border-color,box-shadow] duration-300 group-hover:border-trb18-aqua group-has-checked:border-trb18-aqua group-has-checked:shadow-trb18-cup group-has-focus-visible:outline-3 group-has-focus-visible:outline-offset-3 group-has-focus-visible:outline-trb18-ink">
          <span class="pointer-events-none absolute top-full left-1/2 -ml-[110%] aspect-square w-[220%] translate-y-[4%] rounded-[42%] bg-trb18-aqua transition-[translate] duration-1000 ease-trb18-rise group-has-checked:-translate-y-[64%] group-has-checked:animate-trb18-roll motion-reduce:group-has-checked:animate-none"></span>
          <span class="pointer-events-none absolute top-full left-1/2 -ml-[110%] aspect-square w-[220%] translate-y-[4%] rounded-[44%] bg-trb18-deep opacity-50 transition-[translate] duration-1000 ease-trb18-rise group-has-checked:-translate-y-[64%] group-has-checked:animate-trb18-roll-back motion-reduce:group-has-checked:animate-none"></span>
          <span class="relative text-[26px] font-extrabold text-trb18-letter transition-colors delay-200 duration-400 group-has-checked:text-white">B</span>
        </span>
        <span class="grid justify-items-center"><span class="text-[15px] font-bold text-trb18-mut transition-colors group-has-checked:text-trb18-ink">Bold</span><span class="text-xs text-trb18-mut">Smoky, full body</span></span>
      </label>
    </div>
  </fieldset>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-trb18-bg: #eef6f8;
  --color-trb18-bg: oklch(0.967 0.01 215);
  --color-trb18-ink: #173039;
  --color-trb18-ink: oklch(0.3 0.04 225);
  --color-trb18-mut: #4f6770;
  --color-trb18-mut: oklch(0.49 0.03 220);
  --color-trb18-line: #cfe0e6;
  --color-trb18-line: oklch(0.9 0.02 215);
  --color-trb18-letter: #a9bec6;
  --color-trb18-letter: oklch(0.8 0.025 215);
  --color-trb18-aqua: #2fa3c0;
  --color-trb18-aqua: oklch(0.66 0.11 220);
  --color-trb18-deep: #1d6d85;
  --color-trb18-deep: oklch(0.5 0.09 225);
  --shadow-trb18-cup: 0 12px 26px -12px oklch(0.66 0.11 220 / 0.6);
  --ease-trb18-rise: cubic-bezier(0.22, 1, 0.36, 1);
  --font-trb18-sans: 'Bricolage Grotesque', system-ui, sans-serif;
  --animate-trb18-roll: trb18-roll 5s linear infinite;
  --animate-trb18-roll-back: trb18-roll 7s linear infinite reverse;

  @keyframes trb18-roll {
    from {
      rotate: 0deg;
    }

    to {
      rotate: 360deg;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.trb-18 {
  width: 100%;
  min-height: 100svh;
}
```
