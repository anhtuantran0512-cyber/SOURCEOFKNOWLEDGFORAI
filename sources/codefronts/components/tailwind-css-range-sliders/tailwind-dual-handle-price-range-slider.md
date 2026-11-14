---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-range-sliders/tailwind-dual-handle-price-range-slider/"
title: "Tailwind CSS Dual-Handle Price Range Slider with Live Product Count"
section: "components"
category: "tailwind-css-range-sliders"
category_name: "Tailwind CSS Range Sliders"
description: "The e-commerce workhorse: two thumbs on one track, an accent-lit segment between them, and a live result count."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Dual-Handle Price Range Slider with Live Product Count
Source: https://codefronts.com/components/tailwind-css-range-sliders/tailwind-dual-handle-price-range-slider/

The e-commerce workhorse: two thumbs on one track, an accent-lit segment between them, and a live result count. The port's win is geometry — the CSS original wrote four inline styles per frame and could drift; here two custom properties (--lo, --hi) drive the fill, both handles and both tooltips through calc() utilities, so the lit segment and the handles cannot disagree.
## HTML
```html
<section class="trs-01 w-full min-h-svh grid place-items-center bg-trs01-bg font-trs01-sans px-5 py-10" id="trs-01-root" style="--lo:.1;--hi:.75">
  <div class="w-[min(480px,100%)] rounded-3xl bg-trs01-card border border-trs01-edge p-7 pt-6 shadow-[0_24px_70px_-20px_oklch(0.2_0.06_250/0.55)] overflow-visible">
    <header class="flex items-start justify-between gap-4 mb-7">
      <div>
        <h3 class="text-[17px] font-extrabold tracking-tight text-trs01-ink m-0">Price range</h3>
        <p class="text-xs text-trs01-mut mt-1 m-0">Filter products by budget</p>
      </div>
      <span class="shrink-0 rounded-full bg-trs01-acc/12 border border-trs01-acc/35 text-trs01-acc text-[10px] font-bold tracking-[0.12em] px-2.5 py-1">E-SHOP</span>
    </header>

    <div class="grid grid-cols-2 gap-3 mb-6">
      <div class="rounded-2xl bg-trs01-well border border-trs01-edge px-4 py-3">
        <div class="text-[10px] font-semibold tracking-[0.14em] text-trs01-mut uppercase">Min</div>
        <div class="font-trs01-mono text-2xl font-bold text-trs01-acc tabular-nums mt-0.5"><span class="text-sm align-super text-trs01-mut">$</span><span id="trs-01-min">20</span></div>
      </div>
      <div class="rounded-2xl bg-trs01-well border border-trs01-edge px-4 py-3">
        <div class="text-[10px] font-semibold tracking-[0.14em] text-trs01-mut uppercase">Max</div>
        <div class="font-trs01-mono text-2xl font-bold text-trs01-acc tabular-nums mt-0.5"><span class="text-sm align-super text-trs01-mut">$</span><span id="trs-01-max">150</span></div>
      </div>
    </div>

    <div class="flex items-end gap-[3px] h-14 mb-1 px-px" id="trs-01-hist" aria-hidden="true"></div>

    <div class="relative h-12 flex items-center" id="trs-01-wrap">
      <div class="absolute inset-x-0 h-1.5 rounded-full bg-trs01-track"></div>
      <div class="absolute h-1.5 rounded-full bg-gradient-to-r from-trs01-acc to-trs01-acc2 shadow-[0_0_14px_var(--color-trs01-acc)] left-[calc(var(--lo)*100%)] w-[calc((var(--hi)_-_var(--lo))*100%)]"></div>

      <input type="range" id="trs-01-lo" min="0" max="200" value="20" aria-label="Minimum price" data-top="true"
             class="peer/lo absolute inset-0 w-full h-full m-0 appearance-none bg-transparent opacity-0 pointer-events-none z-10 data-[top=true]:z-20 focus-visible:opacity-0">
      <input type="range" id="trs-01-hi" min="0" max="200" value="150" aria-label="Maximum price" data-top="false"
             class="peer/hi absolute inset-0 w-full h-full m-0 appearance-none bg-transparent opacity-0 pointer-events-none z-10 data-[top=true]:z-20">

      <span aria-hidden="true" class="absolute top-1/2 left-[calc(var(--lo)*100%)] -translate-x-1/2 -translate-y-1/2 size-5.5 rounded-full bg-white border-[3px] border-trs01-acc shadow-[0_0_0_4px_var(--color-trs01-ring),0_4px_12px_oklch(0.15_0.05_250/0.5)] transition-transform duration-150 peer-active/lo:scale-115 peer-focus-visible/lo:ring-2 peer-focus-visible/lo:ring-white motion-reduce:transition-none">
        <span class="absolute bottom-[calc(100%_+_10px)] left-1/2 -translate-x-1/2 rounded-md bg-trs01-acc px-1.5 py-0.5 font-trs01-mono text-[10px] font-bold text-trs01-bg whitespace-nowrap opacity-0 transition-opacity duration-200 peer-active/lo:opacity-100 peer-focus-visible/lo:opacity-100 motion-reduce:transition-none" id="trs-01-tip-lo">$20</span>
      </span>
      <span aria-hidden="true" class="absolute top-1/2 left-[calc(var(--hi)*100%)] -translate-x-1/2 -translate-y-1/2 size-5.5 rounded-full bg-white border-[3px] border-trs01-acc shadow-[0_0_0_4px_var(--color-trs01-ring),0_4px_12px_oklch(0.15_0.05_250/0.5)] transition-transform duration-150 peer-active/hi:scale-115 motion-reduce:transition-none">
        <span class="absolute bottom-[calc(100%_+_10px)] left-1/2 -translate-x-1/2 rounded-md bg-trs01-acc px-1.5 py-0.5 font-trs01-mono text-[10px] font-bold text-trs01-bg whitespace-nowrap opacity-0 transition-opacity duration-200 peer-active/hi:opacity-100 motion-reduce:transition-none" id="trs-01-tip-hi">$150</span>
      </span>
    </div>

    <div class="flex justify-between font-trs01-mono text-[10px] text-trs01-mut mb-5">
      <span>$0</span><span>$50</span><span>$100</span><span>$150</span><span>$200</span>
    </div>

    <footer class="flex items-center justify-between gap-4 pt-5 border-t border-trs01-edge">
      <p class="text-[13px] text-trs01-mut m-0" aria-live="polite"><strong class="text-trs01-acc font-bold tabular-nums" id="trs-01-count">183</strong> products in range</p>
      <button type="button" class="min-h-11 rounded-xl bg-trs01-acc px-5 text-[13px] font-bold text-trs01-bg transition-[translate,box-shadow] duration-150 hover:-translate-y-px hover:shadow-[0_8px_22px_-6px_var(--color-trs01-acc)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-trs01-acc motion-reduce:hover:translate-y-0">Apply filter</button>
    </footer>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-trs01-bg: #0a1628;
  --color-trs01-bg: oklch(0.2 0.045 255);
  --color-trs01-card: #142042;
  --color-trs01-card: oklch(0.26 0.055 262);
  --color-trs01-well: #18264a;
  --color-trs01-well: oklch(0.29 0.055 262);
  --color-trs01-edge: #1f3159;
  --color-trs01-edge: oklch(0.34 0.06 262);
  --color-trs01-track: #22365f;
  --color-trs01-track: oklch(0.36 0.055 262);
  --color-trs01-acc: #00c896;
  --color-trs01-acc: oklch(0.75 0.16 165);
  --color-trs01-acc2: #00e5b0;
  --color-trs01-acc2: oklch(0.84 0.15 168);
  --color-trs01-ring: #0d3b34;
  --color-trs01-ring: oklch(0.36 0.07 168);
  --color-trs01-ink: #e8f0fe;
  --color-trs01-ink: oklch(0.95 0.015 255);
  --color-trs01-mut: #7d94ba;
  --color-trs01-mut: oklch(0.66 0.045 255);
  --font-trs01-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-trs01-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Registered so the calc()-driven fill and handles interpolate instead of jumping. */

@property --lo {
  syntax: "<number>";
  inherits: true;
  initial-value: 0;
}

@property --hi {
  syntax: "<number>";
  inherits: true;
  initial-value: 1;
}

.trs-01 {
  width: 100%;
  min-height: 100svh;
  transition: --lo 60ms linear, --hi 60ms linear;
}

@media (prefers-reduced-motion: reduce) {
  .trs-01 {
    transition: none;
  }
}
/* The one thing utilities cannot say: the native thumbs are invisible hit targets
   layered over the utility-styled handles, and they alone take pointer events. */

.trs-01 input[type="range"]::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 26px;
  height: 26px;
  border-radius: 9999px;
  background: transparent;
  pointer-events: all;
  cursor: grab;
}

.trs-01 input[type="range"]:active::-webkit-slider-thumb {
  cursor: grabbing;
}

.trs-01 input[type="range"]::-moz-range-thumb {
  width: 26px;
  height: 26px;
  border: 0;
  border-radius: 9999px;
  background: transparent;
  pointer-events: all;
  cursor: grab;
}
```

## JavaScript
```js
(function(){
  var root = document.getElementById('trs-01-root');
  var lo = document.getElementById('trs-01-lo'), hi = document.getElementById('trs-01-hi');
  var hist = document.getElementById('trs-01-hist');
  var GAP = 10, TOTAL = 247, BARS = 24;
  var shape = [12,18,26,38,52,68,84,96,100,92,80,70,62,54,46,40,34,28,23,19,15,12,9,7];

  shape.forEach(function(h){
    var b = document.createElement('span');
    b.className = 'flex-1 rounded-sm bg-trs01-track transition-colors duration-200 data-[in=true]:bg-trs01-acc/70 motion-reduce:transition-none';
    b.style.height = Math.max(6, h * 0.5) + 'px';
    b.dataset.in = 'false';
    hist.appendChild(b);
  });
  var bars = Array.prototype.slice.call(hist.children);

  function frac(v){ return (v - +lo.min) / (+lo.max - +lo.min); }

  function update(){
    var a = Math.min(+lo.value, +hi.value), b = Math.max(+lo.value, +hi.value);
    if (b - a < GAP) { if (document.activeElement === lo) { a = Math.min(b - GAP, a); lo.value = a; } else { b = a + GAP; hi.value = b; } }
    root.style.setProperty('--lo', frac(a));
    root.style.setProperty('--hi', frac(b));
    document.getElementById('trs-01-min').textContent = a;
    document.getElementById('trs-01-max').textContent = b;
    document.getElementById('trs-01-tip-lo').textContent = '$' + a;
    document.getElementById('trs-01-tip-hi').textContent = '$' + b;
    lo.setAttribute('aria-valuetext', '$' + a + ' minimum');
    hi.setAttribute('aria-valuetext', '$' + b + ' maximum');
    bars.forEach(function(bar, i){
      var c = (i + 0.5) / BARS;
      bar.dataset.in = (c >= frac(a) && c <= frac(b)) ? 'true' : 'false';
    });
    document.getElementById('trs-01-count').textContent = Math.max(3, Math.round(TOTAL * (b - a) / 200));
  }

  [lo, hi].forEach(function(inp){
    inp.addEventListener('input', function(){
      lo.dataset.top = String(inp === lo);
      hi.dataset.top = String(inp === hi);
      update();
    });
    inp.addEventListener('pointerdown', function(){
      lo.dataset.top = String(inp === lo);
      hi.dataset.top = String(inp === hi);
    });
  });
  update();
})();
```
