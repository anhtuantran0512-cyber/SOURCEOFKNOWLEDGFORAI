---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-range-sliders/tailwind-liquid-glass-slider-gooey-value-bubble/"
title: "Tailwind CSS Liquid Glass Slider with Gooey Morphing Value Bubble"
section: "components"
category: "tailwind-css-range-sliders"
category_name: "Tailwind CSS Range Sliders"
description: "The iOS-style fluid control: the value bubble grows out of the track itself, fused by a gooey SVG filter, then floats over the thumb as you drag."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Liquid Glass Slider with Gooey Morphing Value Bubble
Source: https://codefronts.com/components/tailwind-css-range-sliders/tailwind-liquid-glass-slider-gooey-value-bubble/

The iOS-style fluid control: the value bubble grows out of the track itself, fused by a gooey SVG filter, then floats over the thumb as you drag. Everything except the filter primitives is a utility — and the show condition is has-[input:active]:, so hover, drag, and keyboard focus all trigger the same morph.
## HTML
```html
<section class="trs-17 w-full min-h-svh grid place-items-center px-6 py-10 font-trs17-sans" id="trs-17-root" style="--v:.6">
  <svg class="absolute size-0" aria-hidden="true"><filter id="trs-17-goo"><feGaussianBlur in="SourceGraphic" stdDeviation="6" result="b"/><feColorMatrix in="b" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 22 -9"/></filter></svg>

  <article class="w-[min(370px,100%)] rounded-3xl isolate p-6 text-white bg-white/11 border border-white/35 backdrop-blur-[22px] saturate-180 shadow-[inset_0_1px_0_oklch(1_0_0/0.45),0_30px_60px_-30px_oklch(0_0_0/0.7)]">
    <header class="flex items-baseline justify-between gap-3 mb-2">
      <h3 class="text-base font-extrabold tracking-wide m-0">Display</h3>
      <span class="text-[11px] font-semibold text-white/60">Drag the thumb →</span>
    </header>

    <div class="mt-3.5">
      <div class="flex items-center justify-between gap-2 mb-3">
        <label for="trs-17-input" class="inline-flex items-center gap-1.5 text-[13px] font-semibold text-white/90"><span aria-hidden="true">☀︎</span> Brightness</label>
        <span class="text-sm font-extrabold tabular-nums min-w-[3ch] text-right" id="trs-17-out">60</span>
      </div>

      <div class="group/slider relative h-8 flex items-center has-[input:focus-visible]:outline-2 has-[input:focus-visible]:outline-offset-6 has-[input:focus-visible]:outline-white rounded-full">
        <div class="absolute inset-x-0 h-2 rounded-full bg-white/16 border border-white/25" aria-hidden="true"></div>
        <span class="absolute inset-0 [filter:url(#trs-17-goo)] pointer-events-none" aria-hidden="true">
          <span class="absolute left-0 top-1/2 -translate-y-1/2 h-2 rounded-full w-[calc(var(--v)*100%)] bg-gradient-to-r from-trs17-acc/60 to-trs17-acc shadow-[0_0_12px_-2px_var(--color-trs17-acc)]"></span>
          <span class="absolute top-1/2 left-[calc(var(--v)*100%)] -translate-x-1/2 -translate-y-1/2 grid place-items-center size-5.5 rounded-full text-[0px] text-[#3a2a05] font-extrabold bg-[radial-gradient(circle_at_35%_30%,#fff,var(--color-trs17-acc))] border border-white/60 shadow-[inset_0_2px_4px_oklch(1_0_0/0.9),inset_0_-3px_5px_oklch(0_0_0/0.18),0_6px_14px_oklch(0_0_0/0.35)] transition-[width,height,font-size] duration-250 ease-[cubic-bezier(0.34,1.6,0.5,1)] group-hover/slider:size-8 group-hover/slider:text-[12px] group-has-[input:active]/slider:size-8 group-has-[input:active]/slider:text-[12px] group-has-[input:focus-visible]/slider:size-8 group-has-[input:focus-visible]/slider:text-[12px] motion-reduce:transition-none" id="trs-17-bubble">60</span>
        </span>
        <input type="range" min="0" max="100" value="60" id="trs-17-input" aria-label="Brightness"
               class="absolute inset-0 w-full h-full m-0 appearance-none bg-transparent opacity-0 cursor-pointer z-10">
      </div>
    </div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-trs17-acc: #f0b429;
  --color-trs17-acc: oklch(0.8 0.17 65);
  --font-trs17-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

@property --v {
  syntax: "<number>";
  inherits: true;
  initial-value: 0.6;
}

.trs-17 {
  transition: --v 75ms linear;
}

@media (prefers-reduced-motion: reduce) {
  .trs-17 {
    transition: none;
  }
}

.trs-17 {
  width: 100%;
  min-height: 100svh;
  background: radial-gradient(120% 120% at 70% 20%, #1e293b, #0f172a 70%);
}
/* The native thumb is a transparent hit target: the visible bubble is the
   glass span inside the gooey group. */

.trs-17 input[type="range"]::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 32px;
  height: 32px;
  border-radius: 9999px;
  background: transparent;
  cursor: grab;
}

.trs-17 input[type="range"]:active::-webkit-slider-thumb {
  cursor: grabbing;
}

.trs-17 input[type="range"]::-moz-range-thumb {
  width: 32px;
  height: 32px;
  border: 0;
  border-radius: 9999px;
  background: transparent;
  cursor: grab;
}
```

## JavaScript
```js
(function(){
  var root = document.getElementById('trs-17-root');
  var inp = document.getElementById('trs-17-input');
  var bubble = document.getElementById('trs-17-bubble');
  var out = document.getElementById('trs-17-out');
  function update(){
    var v = +inp.value;
    root.style.setProperty('--v', v / 100);
    bubble.textContent = v;
    out.textContent = v;
    inp.setAttribute('aria-valuetext', v + ' percent brightness');
  }
  inp.addEventListener('input', update);
  update();
})();
```
