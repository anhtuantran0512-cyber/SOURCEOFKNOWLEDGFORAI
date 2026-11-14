---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-range-sliders/tailwind-neumorphic-volume-slider-soft-ui/"
title: "Tailwind CSS Neumorphic Volume Slider with Soft UI Shadows"
section: "components"
category: "tailwind-css-range-sliders"
category_name: "Tailwind CSS Range Sliders"
description: "Soft UI done honestly: one base colour, two opposing shadows, and nothing else."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Neumorphic Volume Slider with Soft UI Shadows
Source: https://codefronts.com/components/tailwind-css-range-sliders/tailwind-neumorphic-volume-slider-soft-ui/

Soft UI done honestly: one base colour, two opposing shadows, and nothing else. The port reads well because neumorphism is entirely a shadow language — shadow-[10px_10px_30px_var(--color-trs02-dark),-10px_-10px_30px_var(--color-trs02-light)] states the extrusion inline, and the pressed state is the same utility with inset and smaller offsets.
## HTML
```html
<section class="trs-02 w-full min-h-svh grid place-items-center bg-trs02-base font-trs02-sans px-5 py-10" id="trs-02-root" style="--v:.6">
  <div class="w-[min(400px,100%)] rounded-[28px] bg-trs02-base p-9 shadow-[10px_10px_30px_var(--color-trs02-dark),-10px_-10px_30px_var(--color-trs02-light)]">
    <header class="flex items-center justify-between gap-3 mb-8">
      <button type="button" aria-label="Previous track" class="grid place-items-center size-13 rounded-2xl bg-trs02-base text-trs02-mut shadow-[5px_5px_14px_var(--color-trs02-dark),-5px_-5px_14px_var(--color-trs02-light)] transition-shadow duration-200 hover:text-trs02-acc active:shadow-[inset_4px_4px_10px_var(--color-trs02-dark),inset_-4px_-4px_10px_var(--color-trs02-light)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-trs02-acc">
        <svg viewBox="0 0 24 24" class="size-5 fill-none stroke-current stroke-2 [stroke-linecap:round]"><polyline points="15 18 9 12 15 6"/></svg>
      </button>
      <h3 class="text-[15px] font-bold tracking-wide text-trs02-ink m-0">Volume control</h3>
      <button type="button" aria-label="Next track" class="grid place-items-center size-13 rounded-2xl bg-trs02-base text-trs02-mut shadow-[5px_5px_14px_var(--color-trs02-dark),-5px_-5px_14px_var(--color-trs02-light)] transition-shadow duration-200 hover:text-trs02-acc active:shadow-[inset_4px_4px_10px_var(--color-trs02-dark),inset_-4px_-4px_10px_var(--color-trs02-light)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-trs02-acc">
        <svg viewBox="0 0 24 24" class="size-5 fill-none stroke-current stroke-2 [stroke-linecap:round]"><polyline points="9 18 15 12 9 6"/></svg>
      </button>
    </header>

    <div class="rounded-2xl bg-trs02-base px-5 py-6 mb-7 shadow-[inset_5px_5px_14px_var(--color-trs02-dark),inset_-5px_-5px_14px_var(--color-trs02-light)]">
      <input type="range" min="0" max="100" value="60" id="trs-02-vol" aria-label="Volume"
             class="block w-full h-2 appearance-none bg-transparent outline-none cursor-pointer bg-[linear-gradient(90deg,var(--color-trs02-acc)_calc(var(--v)*100%),var(--color-trs02-dark)_calc(var(--v)*100%))] rounded-full focus-visible:outline-2 focus-visible:outline-offset-8 focus-visible:outline-trs02-acc">
    </div>

    <div class="flex items-end justify-between gap-4">
      <div class="flex items-baseline gap-1">
        <span class="text-[42px] leading-none font-black tracking-tight text-trs02-ink tabular-nums" id="trs-02-num">60</span>
        <span class="text-base font-medium text-trs02-mut">%</span>
      </div>
      <div class="flex items-end gap-[5px]" id="trs-02-meter" aria-hidden="true"></div>
      <button type="button" id="trs-02-mute" aria-pressed="false" class="grid place-items-center min-h-11 min-w-11 rounded-2xl bg-trs02-base text-trs02-mut shadow-[5px_5px_14px_var(--color-trs02-dark),-5px_-5px_14px_var(--color-trs02-light)] transition-shadow duration-200 aria-pressed:text-trs02-acc aria-pressed:shadow-[inset_4px_4px_10px_var(--color-trs02-dark),inset_-4px_-4px_10px_var(--color-trs02-light)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-trs02-acc">
        <span class="sr-only">Mute</span>
        <svg viewBox="0 0 24 24" class="size-5 fill-current"><polygon points="11,5 6,9 2,9 2,15 6,15 11,19"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
      </button>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-trs02-base: #e0e5ec;
  --color-trs02-base: oklch(0.91 0.01 255);
  --color-trs02-dark: #b3bac6;
  --color-trs02-dark: oklch(0.79 0.018 258);
  --color-trs02-light: #ffffff;
  --color-trs02-light: oklch(1 0 0);
  --color-trs02-acc: #5a4ff3;
  --color-trs02-acc: oklch(0.53 0.21 280);
  --color-trs02-ink: #2f3a4c;
  --color-trs02-ink: oklch(0.36 0.03 262);
  --color-trs02-mut: #5c6b83;
  --color-trs02-mut: oklch(0.5 0.035 258);
  --font-trs02-sans: 'Outfit', system-ui, sans-serif;
}

@property --v {
  syntax: "<number>";
  inherits: true;
  initial-value: 0.6;
}

.trs-02 {
  width: 100%;
  min-height: 100svh;
}
/* Thumb: the extruded knob, and the only place the neumorphic shadow pair
   cannot be written as a utility. */

.trs-02 input[type="range"]::-webkit-slider-runnable-track {
  height: 8px;
  border-radius: 9999px;
  background: transparent;
}

.trs-02 input[type="range"]::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 32px;
  height: 32px;
  margin-top: -12px;
  border-radius: 9999px;
  background: var(--color-trs02-base);
  cursor: grab;
  box-shadow: 5px 5px 14px var(--color-trs02-dark), -5px -5px 14px var(--color-trs02-light);
  transition: box-shadow .2s;
}

.trs-02 input[type="range"]:active::-webkit-slider-thumb {
  cursor: grabbing;
  box-shadow: 3px 3px 8px var(--color-trs02-dark), -3px -3px 8px var(--color-trs02-light), 0 0 0 5px color-mix(in oklab, var(--color-trs02-acc) 28%, transparent);
}

.trs-02 input[type="range"]::-moz-range-track {
  height: 8px;
  border-radius: 9999px;
  background: var(--color-trs02-dark);
}

.trs-02 input[type="range"]::-moz-range-progress {
  height: 8px;
  border-radius: 9999px;
  background: var(--color-trs02-acc);
}

.trs-02 input[type="range"]::-moz-range-thumb {
  width: 32px;
  height: 32px;
  border: 0;
  border-radius: 9999px;
  background: var(--color-trs02-base);
  cursor: grab;
  box-shadow: 5px 5px 14px var(--color-trs02-dark), -5px -5px 14px var(--color-trs02-light);
}

@media (prefers-reduced-motion: reduce) {
  .trs-02 input[type="range"]::-webkit-slider-thumb {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.getElementById('trs-02-root');
  var inp = document.getElementById('trs-02-vol');
  var num = document.getElementById('trs-02-num');
  var meter = document.getElementById('trs-02-meter');
  var mute = document.getElementById('trs-02-mute');
  var heights = [10,14,18,22,28,34,28,22,18,14,10,8];
  var last = 60;

  heights.forEach(function(h){
    var b = document.createElement('span');
    b.className = 'w-1.5 rounded-full bg-trs02-dark transition-colors duration-300 data-[on=true]:bg-trs02-acc motion-reduce:transition-none';
    b.style.height = h + 'px';
    b.dataset.on = 'false';
    meter.appendChild(b);
  });
  var bars = Array.prototype.slice.call(meter.children);

  function update(){
    var v = +inp.value;
    root.style.setProperty('--v', v / 100);
    num.textContent = v;
    inp.setAttribute('aria-valuetext', v === 0 ? 'Muted' : v + ' percent');
    var on = Math.round(v / 100 * bars.length);
    bars.forEach(function(b, i){ b.dataset.on = i < on ? 'true' : 'false'; });
    mute.setAttribute('aria-pressed', String(v === 0));
  }

  inp.addEventListener('input', function(){ if (+inp.value > 0) last = +inp.value; update(); });
  mute.addEventListener('click', function(){
    inp.value = +inp.value === 0 ? (last || 60) : 0;
    update();
  });
  update();
})();
```
