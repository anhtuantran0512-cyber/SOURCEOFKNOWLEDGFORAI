---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-range-sliders/tailwind-brutalist-range-slider-thick-block/"
title: "Tailwind CSS Brutalist Range Slider with Thick Block Track"
section: "components"
category: "tailwind-css-range-sliders"
category_name: "Tailwind CSS Range Sliders"
description: "Brutalism as a system: 3px black rules, zero-blur offset shadows, one red block for a thumb and no rounded corners anywhere."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Brutalist Range Slider with Thick Block Track
Source: https://codefronts.com/components/tailwind-css-range-sliders/tailwind-brutalist-range-slider-thick-block/

Brutalism as a system: 3px black rules, zero-blur offset shadows, one red block for a thumb and no rounded corners anywhere. The port suits it — shadow-[6px_6px_0_var(--color-trs11-ink)] and border-[3px] say the whole aesthetic, and the preset row is a real segmented control.
## HTML
```html
<section class="trs-11 w-full min-h-svh grid place-items-center bg-trs11-bg font-trs11-mono px-6 py-12" id="trs-11-root" style="--v:.64">
  <div class="w-[min(440px,100%)] bg-trs11-card border-[3px] border-trs11-ink shadow-[6px_6px_0_var(--color-trs11-ink)]">
    <header class="flex items-center justify-between gap-4 bg-trs11-ink px-5 py-2.5 text-white">
      <span class="text-xs font-bold uppercase tracking-[0.2em]">CONFIG.SYS</span>
      <span class="flex gap-1.5" aria-hidden="true"><span class="size-2.5 rounded-full bg-white/30"></span><span class="size-2.5 rounded-full bg-white/30"></span><span class="size-2.5 rounded-full bg-white/30"></span></span>
    </header>

    <div class="p-8">
      <div class="mb-6">
        <div class="text-[80px] leading-none font-bold tracking-tighter text-trs11-ink tabular-nums" id="trs-11-num">64</div>
        <div class="text-xs uppercase tracking-[0.2em] text-trs11-mut mt-1">Allocation units</div>
      </div>

      <div class="relative h-8 border-[3px] border-trs11-ink bg-trs11-grey mb-2">
        <div class="absolute inset-y-0 left-0 bg-trs11-ink w-[calc(var(--v)*100%)] transition-none"></div>
        <input type="range" min="0" max="100" step="4" value="64" id="trs-11-inp" aria-label="Allocation units"
               class="absolute inset-0 w-full h-full appearance-none bg-transparent outline-none cursor-ew-resize z-10 focus-visible:outline-[3px] focus-visible:outline-offset-4 focus-visible:outline-trs11-hot">
      </div>

      <div class="flex justify-between text-[10px] text-trs11-mut mb-7">
        <span class="flex flex-col items-center"><span class="text-trs11-ink text-xs" aria-hidden="true">|</span>0</span>
        <span class="flex flex-col items-center"><span class="text-trs11-ink text-xs" aria-hidden="true">|</span>25</span>
        <span class="flex flex-col items-center"><span class="text-trs11-ink text-xs" aria-hidden="true">|</span>50</span>
        <span class="flex flex-col items-center"><span class="text-trs11-ink text-xs" aria-hidden="true">|</span>75</span>
        <span class="flex flex-col items-center"><span class="text-trs11-ink text-xs" aria-hidden="true">|</span>100</span>
      </div>

      <div class="flex" role="group" aria-label="Presets" id="trs-11-presets">
        <button type="button" data-val="0" aria-pressed="false" class="flex-1 min-h-11 border-[3px] border-trs11-ink bg-transparent text-xs font-bold uppercase tracking-wider text-trs11-ink transition-colors duration-150 hover:bg-trs11-ink hover:text-white aria-pressed:bg-trs11-ink aria-pressed:text-white focus-visible:outline-[3px] focus-visible:outline-offset-2 focus-visible:outline-trs11-hot">Reset</button>
        <button type="button" data-val="50" aria-pressed="false" class="flex-1 min-h-11 border-[3px] border-l-0 border-trs11-ink bg-transparent text-xs font-bold uppercase tracking-wider text-trs11-ink transition-colors duration-150 hover:bg-trs11-ink hover:text-white aria-pressed:bg-trs11-ink aria-pressed:text-white focus-visible:outline-[3px] focus-visible:outline-offset-2 focus-visible:outline-trs11-hot">Half</button>
        <button type="button" data-val="64" aria-pressed="true" class="flex-1 min-h-11 border-[3px] border-l-0 border-trs11-ink bg-transparent text-xs font-bold uppercase tracking-wider text-trs11-ink transition-colors duration-150 hover:bg-trs11-ink hover:text-white aria-pressed:bg-trs11-ink aria-pressed:text-white focus-visible:outline-[3px] focus-visible:outline-offset-2 focus-visible:outline-trs11-hot">Default</button>
        <button type="button" data-val="100" aria-pressed="false" class="flex-1 min-h-11 border-[3px] border-l-0 border-trs11-ink bg-transparent text-xs font-bold uppercase tracking-wider text-trs11-ink transition-colors duration-150 hover:bg-trs11-ink hover:text-white aria-pressed:bg-trs11-ink aria-pressed:text-white focus-visible:outline-[3px] focus-visible:outline-offset-2 focus-visible:outline-trs11-hot">Max</button>
      </div>

      <p class="text-[10px] uppercase tracking-[0.15em] text-trs11-mut mt-5 m-0">Keys: 1-9 set 10-90% · 0 sets 100% · ← → step</p>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-trs11-bg: #f5f0e8;
  --color-trs11-bg: oklch(0.95 0.018 85);
  --color-trs11-card: #ece6da;
  --color-trs11-card: oklch(0.92 0.02 85);
  --color-trs11-grey: #cdc7bb;
  --color-trs11-grey: oklch(0.82 0.015 85);
  --color-trs11-ink: #111111;
  --color-trs11-ink: oklch(0.15 0 0);
  --color-trs11-hot: #d63427;
  --color-trs11-hot: oklch(0.55 0.21 27);
  --color-trs11-mut: #6f6a61;
  --color-trs11-mut: oklch(0.52 0.012 85);
  --font-trs11-mono: 'Space Mono', ui-monospace, monospace;
}

@property --v {
  syntax: "<number>";
  inherits: true;
  initial-value: 0.64;
}

.trs-11 {
  width: 100%;
  min-height: 100svh;
}
/* The block thumb: square, full track height, hard black right edge. */

.trs-11 input[type="range"]::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 28px;
  height: 26px;
  border: 0;
  border-radius: 0;
  border-right: 3px solid var(--color-trs11-ink);
  background: var(--color-trs11-hot);
  cursor: ew-resize;
  transition: background .15s;
}

.trs-11 input[type="range"]:hover::-webkit-slider-thumb {
  background: oklch(0.62 0.22 27);
}

.trs-11 input[type="range"]::-moz-range-thumb {
  width: 28px;
  height: 26px;
  border: 0;
  border-radius: 0;
  background: var(--color-trs11-hot);
  cursor: ew-resize;
}

@media (prefers-reduced-motion: reduce) {
  .trs-11 input[type="range"]::-webkit-slider-thumb {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.getElementById('trs-11-root');
  var inp = document.getElementById('trs-11-inp');
  var num = document.getElementById('trs-11-num');
  var buttons = Array.prototype.slice.call(document.querySelectorAll('#trs-11-presets button'));

  function update(){
    var v = +inp.value;
    root.style.setProperty('--v', v / 100);
    num.textContent = v;
    buttons.forEach(function(b){ b.setAttribute('aria-pressed', String(+b.dataset.val === v)); });
  }
  inp.addEventListener('input', update);
  buttons.forEach(function(b){
    b.addEventListener('click', function(){ inp.value = b.dataset.val; update(); });
  });
  document.addEventListener('keydown', function(e){
    if (e.target.tagName === 'INPUT' && e.target !== inp) return;
    if (e.key >= '1' && e.key <= '9') { inp.value = +e.key * 10; update(); }
    else if (e.key === '0') { inp.value = 100; update(); }
  });
  update();
})();
```
