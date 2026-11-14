---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-liquid-glass-effects/tailwind-liquid-gooey-toggle-switch/"
title: "Tailwind Liquid Gooey Toggle Switch"
section: "design-styles"
category: "tailwind-liquid-glass-effects"
category_name: "Tailwind Liquid Glass Effects"
description: "A handle that behaves like liquid metal: it stretches as it travels, fuses with the track blob, then snaps into place."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Liquid Gooey Toggle Switch
Source: https://codefronts.com/design-styles/tailwind-liquid-glass-effects/tailwind-liquid-gooey-toggle-switch/

A handle that behaves like liquid metal: it stretches as it travels, fuses with the track blob, then snaps into place. The whole state machine is peer plus peer-checked: on a native checkbox, and the only thing utilities cannot express &mdash; the SVG goo filter and its stretch keyframe &mdash; stays in the stylesheet where it belongs.
## HTML
```html
<section class="lgt-04 grid w-full min-h-svh place-items-center p-15 font-lgt04-sans [background:radial-gradient(circle_at_30%_20%,#2a2740,#12101d)]" aria-label="Tailwind liquid gooey toggle switch">
  <svg width="0" height="0" aria-hidden="true" focusable="false" class="absolute">
    <filter id="lgt-04-goo">
      <feGaussianBlur in="SourceGraphic" stdDeviation="6" result="b"/>
      <feColorMatrix in="b" mode="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 20 -9" result="goo"/>
      <feBlend in="SourceGraphic" in2="goo"/>
    </filter>
  </svg>
  <label class="inline-flex cursor-pointer items-center gap-3.5 text-[22px] text-lgt04-fg">
    <input type="checkbox" checked class="peer sr-only">
    <span aria-hidden="true" class="relative h-[1.7em] w-[3.4em] rounded-full border border-white/25 bg-lgt04-off backdrop-blur-[6px] transition-colors duration-350 shadow-[inset_0_2px_8px_rgba(0,0,0,.45),inset_0_1px_0_rgba(255,255,255,.25)] peer-checked:bg-lgt04-on peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-white peer-checked:[&amp;_.lgt-04-fixed]:opacity-0 peer-checked:[&amp;_.lgt-04-handle]:left-[2em] peer-checked:[&amp;_.lgt-04-handle]:animate-lgt04-stretch motion-reduce:[&amp;_.lgt-04-handle]:animate-none">
      <span class="absolute inset-0 [filter:url(#lgt-04-goo)]">
        <span class="lgt-04-fixed absolute top-1/2 left-[0.28em] size-[1.14em] -translate-y-1/2 rounded-full bg-white opacity-90 transition-opacity delay-200 duration-300"></span>
        <span class="lgt-04-handle absolute top-1/2 left-[0.28em] size-[1.14em] -translate-y-1/2 rounded-full bg-white shadow-[0_2px_6px_rgba(0,0,0,.35)] transition-[left] duration-400 ease-lgt04"></span>
      </span>
    </span>
    <span class="text-[0.85em] font-semibold">Liquid mode</span>
  </label>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-lgt04-on: #34d3a4;
  --color-lgt04-on: oklch(0.7 0.17 165);
  --color-lgt04-off: #6c6a85;
  --color-lgt04-off: oklch(0.55 0.03 260);
  --color-lgt04-fg: #eceaf5;
  --font-lgt04-sans: 'Manrope', system-ui, sans-serif;
  --ease-lgt04: cubic-bezier(0.6, -0.4, 0.4, 1.4);
  --animate-lgt04-stretch: lgt-04-stretch 0.4s ease;
}
/* The two things utilities cannot express: a keyframe, and the -50% Y that
   must survive inside the scaleX so the handle stays vertically centred. */

@keyframes lgt-04-stretch {
  0% {
    transform: translateY(-50%) scaleX(1);
  }

  45% {
    transform: translateY(-50%) scaleX(1.55);
  }

  100% {
    transform: translateY(-50%) scaleX(1);
  }
}
```
