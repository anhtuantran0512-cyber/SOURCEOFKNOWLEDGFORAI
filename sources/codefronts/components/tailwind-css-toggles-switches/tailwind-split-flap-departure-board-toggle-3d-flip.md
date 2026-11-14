---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-split-flap-departure-board-toggle-3d-flip/"
title: "Tailwind Split-Flap Departure Board Toggle (3D Flip)"
section: "components"
category: "tailwind-css-toggles-switches"
category_name: "Tailwind CSS Toggles & Switches"
description: "An airport departure-board cell that flips between OFF and ON: the top half hinges down over the bottom in real 3D, revealing the new word exactly like a…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Split-Flap Departure Board Toggle (3D Flip)
Source: https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-split-flap-departure-board-toggle-3d-flip/

An airport departure-board cell that flips between OFF and ON: the top half hinges down over the bottom in real 3D, revealing the new word exactly like a mechanical split-flap. Four half-height layers, one rotate-x-180, zero JavaScript.
## HTML
```html
<section class="ttg-12 w-full min-h-svh flex flex-col items-center justify-center gap-7 px-5 py-14 bg-ttg12-bg font-ttg12-mono" aria-label="Split-flap board toggle">
  <label for="ttg-12-sw" class="flex flex-col items-center gap-4 cursor-pointer">
    <input type="checkbox" id="ttg-12-sw" role="switch" aria-label="Departures feed" class="peer sr-only">
    <span aria-hidden="true" class="relative w-[150px] h-24 perspective-[500px] drop-shadow-[0_14px_24px_oklch(0_0_0/0.6)] peer-checked:[&_.ttg12-flap]:-rotate-x-180 peer-focus-visible:outline-3 peer-focus-visible:outline-ttg12-glyph peer-focus-visible:outline-offset-[5px] peer-focus-visible:rounded-[10px]">
      <b class="absolute top-0 left-0 w-[150px] h-12 overflow-hidden rounded-t-lg bg-ttg12-cardhi text-ttg12-glyph text-[44px] font-bold tracking-[0.04em] text-center"><i class="not-italic block leading-[96px]">ON</i></b>
      <b class="absolute top-12 left-0 w-[150px] h-12 overflow-hidden rounded-b-lg bg-ttg12-cardlo text-ttg12-glyph text-[44px] font-bold tracking-[0.04em] text-center"><i class="not-italic block leading-[96px] -translate-y-12">OFF</i></b>
      <b class="ttg12-flap absolute top-0 left-0 w-[150px] h-12 transform-3d origin-bottom transition-transform duration-[600ms] ease-[cubic-bezier(0.4,0,0.6,1)] motion-reduce:duration-[10ms]">
        <span class="absolute top-0 left-0 w-[150px] h-12 overflow-hidden rounded-t-lg backface-hidden bg-ttg12-cardhi text-ttg12-glyph text-[44px] font-bold tracking-[0.04em] text-center"><i class="not-italic block leading-[96px]">OFF</i></span>
        <span class="absolute top-0 left-0 w-[150px] h-12 overflow-hidden rounded-b-lg backface-hidden rotate-x-180 bg-ttg12-cardlo text-ttg12-glyph text-[44px] font-bold tracking-[0.04em] text-center"><i class="not-italic block leading-[96px] -translate-y-12">ON</i></span>
      </b>
      <em class="absolute top-[47px] left-0 right-0 h-0.5 z-[5] bg-ttg12-hinge before:content-[''] before:absolute before:-top-1 before:-left-0.5 before:w-[5px] before:h-2.5 before:rounded-sm before:bg-ttg12-hinge after:content-[''] after:absolute after:-top-1 after:-right-0.5 after:w-[5px] after:h-2.5 after:rounded-sm after:bg-ttg12-hinge"></em>
    </span>
    <span class="text-[13px] tracking-[0.16em] uppercase text-ttg12-label">Departures feed</span>
  </label>
  <p class="font-ttg12-sans text-[11px] tracking-[0.14em] uppercase text-ttg12-mute">Mechanical split-flap &middot; click to flip</p>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg12-bg: #14130f;
  --color-ttg12-bg: oklch(0.19 0.008 90);
  --color-ttg12-cardhi: #262320;
  --color-ttg12-cardhi: oklch(0.27 0.008 75);
  --color-ttg12-cardlo: #1e1c19;
  --color-ttg12-cardlo: oklch(0.23 0.008 75);
  --color-ttg12-glyph: #f7dc84;
  --color-ttg12-glyph: oklch(0.89 0.12 92);
  --color-ttg12-hinge: #0d0c0a;
  --color-ttg12-hinge: oklch(0.15 0.006 90);
  --color-ttg12-label: #a49b81;
  --color-ttg12-label: oklch(0.7 0.03 92);
  --color-ttg12-mute: #6f684f;
  --color-ttg12-mute: oklch(0.52 0.03 92);
  --font-ttg12-mono: 'JetBrains Mono', ui-monospace, 'SF Mono', Menlo, monospace;
  --font-ttg12-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.ttg-12 {
  width: 100%;
  min-height: 100svh;
}
```
