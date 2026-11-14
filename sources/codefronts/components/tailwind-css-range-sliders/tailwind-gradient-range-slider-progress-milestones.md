---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-range-sliders/tailwind-gradient-range-slider-progress-milestones/"
title: "Tailwind CSS Gradient Range Slider with Progress Milestones"
section: "components"
category: "tailwind-css-range-sliders"
category_name: "Tailwind CSS Range Sliders"
description: "A course-progress slider whose fill carries one continuous sunset gradient and whose big percentage is cut from the same gradient, so number and track are…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Gradient Range Slider with Progress Milestones
Source: https://codefronts.com/components/tailwind-css-range-sliders/tailwind-gradient-range-slider-progress-milestones/

A course-progress slider whose fill carries one continuous sunset gradient and whose big percentage is cut from the same gradient, so number and track are visibly the same object. Three milestone cards light as thresholds pass, and progress survives a reload.
## HTML
```html
<section class="trs-09 w-full min-h-svh grid place-items-center bg-trs09-bg font-trs09-sans px-5 py-10" id="trs-09-root" style="--v:.67">
  <div class="w-[min(460px,100%)] rounded-3xl bg-white p-9 shadow-[0_18px_50px_-24px_oklch(0.3_0.03_300/0.35),0_1px_3px_oklch(0.3_0.03_300/0.06)]">
    <header class="flex items-start justify-between gap-4 mb-9">
      <div>
        <h3 class="text-xl font-extrabold tracking-tight text-trs09-ink m-0">Course progress</h3>
        <p class="text-[13px] text-trs09-mut mt-1 m-0">Drag to explore your journey</p>
      </div>
      <div class="text-[28px] font-black tracking-tight tabular-nums text-trs09-mid bg-gradient-to-r from-trs09-warm via-trs09-mid to-trs09-cool bg-clip-text text-transparent"><span id="trs-09-pct">67</span>%</div>
    </header>

    <div class="relative h-12 flex items-center mb-8">
      <div class="absolute inset-x-0 h-3 rounded-full bg-trs09-track"></div>
      <div class="absolute left-0 h-3 rounded-full w-[calc(var(--v)*100%)] bg-gradient-to-r from-trs09-warm via-trs09-mid to-trs09-cool"></div>
      <input type="range" min="0" max="100" value="67" id="trs-09-inp" aria-label="Course progress"
             class="absolute inset-0 w-full h-12 appearance-none bg-transparent outline-none cursor-pointer z-10 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-trs09-mid rounded-full">
    </div>

    <div class="grid grid-cols-3 gap-3" id="trs-09-steps">
      <div data-min="0" data-on="true" class="rounded-2xl bg-trs09-track p-3.5 transition-[background-color,box-shadow] duration-300 data-[on=true]:bg-gradient-to-br data-[on=true]:from-trs09-warm/12 data-[on=true]:to-trs09-cool/12 data-[on=true]:shadow-[inset_0_0_0_1px_color-mix(in_oklab,var(--color-trs09-mid)_30%,transparent)] motion-reduce:transition-none">
        <div class="text-[22px] leading-none mb-1.5 opacity-40 transition-opacity duration-300 data-[on=true]:opacity-100 motion-reduce:transition-none" aria-hidden="true">🏁</div>
        <div class="text-xs font-bold text-trs09-ink">Foundations</div>
        <div class="text-[10px] text-trs09-mut mt-0.5">0–33% complete</div>
      </div>
      <div data-min="34" data-on="true" class="rounded-2xl bg-trs09-track p-3.5 transition-[background-color,box-shadow] duration-300 data-[on=true]:bg-gradient-to-br data-[on=true]:from-trs09-warm/12 data-[on=true]:to-trs09-cool/12 data-[on=true]:shadow-[inset_0_0_0_1px_color-mix(in_oklab,var(--color-trs09-mid)_30%,transparent)] motion-reduce:transition-none">
        <div class="text-[22px] leading-none mb-1.5 opacity-40 transition-opacity duration-300 data-[on=true]:opacity-100 motion-reduce:transition-none" aria-hidden="true">🔬</div>
        <div class="text-xs font-bold text-trs09-ink">Deep dive</div>
        <div class="text-[10px] text-trs09-mut mt-0.5">34–66% complete</div>
      </div>
      <div data-min="67" data-on="false" class="rounded-2xl bg-trs09-track p-3.5 transition-[background-color,box-shadow] duration-300 data-[on=true]:bg-gradient-to-br data-[on=true]:from-trs09-warm/12 data-[on=true]:to-trs09-cool/12 data-[on=true]:shadow-[inset_0_0_0_1px_color-mix(in_oklab,var(--color-trs09-mid)_30%,transparent)] motion-reduce:transition-none">
        <div class="text-[22px] leading-none mb-1.5 opacity-40 transition-opacity duration-300 data-[on=true]:opacity-100 motion-reduce:transition-none" aria-hidden="true">🚀</div>
        <div class="text-xs font-bold text-trs09-ink">Mastery</div>
        <div class="text-[10px] text-trs09-mut mt-0.5">67–100% complete</div>
      </div>
    </div>

    <p class="text-[11px] text-trs09-mut mt-5 m-0" aria-live="polite" id="trs-09-status">Deep dive · 33% to go</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-trs09-bg: #faf9fb;
  --color-trs09-bg: oklch(0.98 0.004 300);
  --color-trs09-track: #f1f1f4;
  --color-trs09-track: oklch(0.95 0.005 300);
  --color-trs09-warm: #f97316;
  --color-trs09-warm: oklch(0.7 0.19 45);
  --color-trs09-mid: #ec4899;
  --color-trs09-mid: oklch(0.65 0.23 350);
  --color-trs09-cool: #a855f7;
  --color-trs09-cool: oklch(0.63 0.24 302);
  --color-trs09-ink: #111827;
  --color-trs09-ink: oklch(0.22 0.02 265);
  --color-trs09-mut: #6b7280;
  --color-trs09-mut: oklch(0.55 0.02 265);
  --font-trs09-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

@property --v {
  syntax: "<number>";
  inherits: true;
  initial-value: 0.67;
}
/* Animate the property, never the width that reads it. */

.trs-09 {
  width: 100%;
  min-height: 100svh;
  transition: --v 75ms linear;
}

@media (prefers-reduced-motion: reduce) {
  .trs-09 {
    transition: none;
  }
}
/* Ring thumb: border-image cannot coexist with border-radius, so the ring is a
   thick solid border over a white core — per-engine, therefore CSS. */

.trs-09 input[type="range"]::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 26px;
  height: 26px;
  border-radius: 9999px;
  box-sizing: border-box;
  background: #fff;
  border: 4px solid var(--color-trs09-mid);
  box-shadow: 0 0 0 6px color-mix(in oklab, var(--color-trs09-mid) 14%, transparent), 0 4px 16px oklch(0 0 0 / 0.15);
  cursor: grab;
  transition: transform .15s, box-shadow .15s;
}

.trs-09 input[type="range"]:active::-webkit-slider-thumb {
  transform: scale(1.14);
  cursor: grabbing;
  box-shadow: 0 0 0 10px color-mix(in oklab, var(--color-trs09-mid) 18%, transparent), 0 4px 16px oklch(0 0 0 / 0.15);
}

.trs-09 input[type="range"]::-moz-range-thumb {
  width: 26px;
  height: 26px;
  border-radius: 9999px;
  box-sizing: border-box;
  background: #fff;
  border: 4px solid var(--color-trs09-mid);
  cursor: grab;
}

@media (prefers-reduced-motion: reduce) {
  .trs-09 input[type="range"]::-webkit-slider-thumb {
    transition: none;
  }

  .trs-09 input[type="range"]:active::-webkit-slider-thumb {
    transform: none;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.getElementById('trs-09-root');
  var inp = document.getElementById('trs-09-inp');
  var pct = document.getElementById('trs-09-pct');
  var status = document.getElementById('trs-09-status');
  var steps = Array.prototype.slice.call(document.getElementById('trs-09-steps').children);
  var KEY = 'trs09-progress';

  try { var saved = localStorage.getItem(KEY); if (saved !== null) inp.value = saved; } catch (e) {}

  function update(){
    var v = +inp.value;
    root.style.setProperty('--v', v / 100);
    pct.textContent = v;
    var current = 'Foundations';
    steps.forEach(function(s){
      var on = v >= +s.dataset.min;
      s.dataset.on = on ? 'true' : 'false';
      if (on) current = s.querySelector('div:nth-child(2)').textContent;
    });
    status.textContent = current + ' · ' + (100 - v) + '% to go';
    inp.setAttribute('aria-valuetext', v + '% complete, ' + current);
    try { localStorage.setItem(KEY, String(v)); } catch (e) {}
  }
  inp.addEventListener('input', update);
  update();
})();
```
