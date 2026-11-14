---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-range-sliders/tailwind-isometric-3d-range-slider-perspective/"
title: "Tailwind CSS Isometric 3D Range Slider with Perspective Plane"
section: "components"
category: "tailwind-css-range-sliders"
category_name: "Tailwind CSS Range Sliders"
description: "A slider lying flat on a tilted grid plane, with a cast shadow that travels under the thumb and three live metrics."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Isometric 3D Range Slider with Perspective Plane
Source: https://codefronts.com/components/tailwind-css-range-sliders/tailwind-isometric-3d-range-slider-perspective/

A slider lying flat on a tilted grid plane, with a cast shadow that travels under the thumb and three live metrics. The port is unusually clean: perspective-[800px], transform-3d, rotate-x-30 and -rotate-z-10 are all first-class v4 utilities, so the entire 3D stage is a class list.
## HTML
```html
<section class="trs-15 w-full min-h-svh grid place-items-center bg-trs15-bg font-trs15-sans px-6 py-14 perspective-[800px]" id="trs-15-root" style="--v:.65">
  <div class="w-[min(470px,100%)]">
    <header class="flex items-end justify-between gap-4 mb-5">
      <h3 class="text-xl font-extrabold tracking-tight text-trs15-ink m-0">Isometric control plane</h3>
      <div class="text-right">
        <div class="text-4xl font-black tracking-tight tabular-nums text-trs15-acc drop-shadow-[0_0_20px_var(--color-trs15-acc)]"><span id="trs-15-val">65</span>%</div>
        <div class="font-trs15-mono text-[10px] tracking-[0.15em] text-trs15-mut">INTENSITY</div>
      </div>
    </header>

    <div class="relative transform-3d rotate-x-30 -rotate-z-10 px-6 py-8 motion-reduce:transform-none">
      <div class="trs-15__grid absolute inset-0 rounded-lg border border-trs15-acc/25" aria-hidden="true">
        <span class="absolute inset-x-0 -bottom-2 h-2 bg-trs15-acc/15 origin-top -rotate-x-90"></span>
      </div>
      <div class="relative z-10">
        <div class="rounded-lg border border-trs15-acc/30 bg-black/60 p-2.5 shadow-[0_8px_32px_oklch(0_0_0/0.55),inset_0_1px_0_oklch(1_0_0/0.06)]">
          <div class="relative h-2.5 rounded-full bg-black/55">
            <div class="absolute inset-y-0 left-0 rounded-full w-[calc(var(--v)*100%)] bg-gradient-to-r from-trs15-acc to-trs15-cyan shadow-[0_0_20px_-2px_var(--color-trs15-acc)]"></div>
            <input type="range" min="0" max="100" value="65" id="trs-15-inp" aria-label="Intensity"
                   class="absolute inset-0 w-full h-full appearance-none bg-transparent outline-none cursor-ew-resize z-10 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-trs15-cyan rounded-full">
          </div>
        </div>
        <span class="block h-1 mt-1.5 w-8 -translate-x-1/2 ml-[calc(var(--v)*100%)] rounded-full bg-[radial-gradient(ellipse_at_center,var(--color-trs15-acc),transparent_70%)] opacity-60 blur-[1px]" aria-hidden="true"></span>
        <div class="flex justify-between font-trs15-mono text-[10px] text-trs15-mut mt-3">
          <span>0</span><span>25</span><span>50</span><span>75</span><span>100</span>
        </div>
      </div>
    </div>

    <div class="grid grid-cols-3 gap-3 mt-6">
      <div class="rounded-xl border border-trs15-acc/20 bg-trs15-acc/8 p-3 text-center">
        <div class="text-lg font-extrabold text-trs15-acc tabular-nums" id="trs-15-pow">65W</div>
        <div class="font-trs15-mono text-[10px] tracking-wider text-trs15-mut">POWER</div>
      </div>
      <div class="rounded-xl border border-trs15-acc/20 bg-trs15-acc/8 p-3 text-center">
        <div class="text-lg font-extrabold text-trs15-acc tabular-nums" id="trs-15-spd">5.2m/s</div>
        <div class="font-trs15-mono text-[10px] tracking-wider text-trs15-mut">SPEED</div>
      </div>
      <div class="rounded-xl border border-trs15-acc/20 bg-trs15-acc/8 p-3 text-center">
        <div class="text-lg font-extrabold text-trs15-acc tabular-nums" id="trs-15-eff">A</div>
        <div class="font-trs15-mono text-[10px] tracking-wider text-trs15-mut">EFFICIENCY</div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-trs15-bg: #0d0d1f;
  --color-trs15-bg: oklch(0.17 0.035 285);
  --color-trs15-acc: #8b5cf6;
  --color-trs15-acc: oklch(0.63 0.21 295);
  --color-trs15-cyan: #22d3ee;
  --color-trs15-cyan: oklch(0.82 0.13 200);
  --color-trs15-grid: #2a2050;
  --color-trs15-grid: oklch(0.3 0.07 295);
  --color-trs15-ink: #f0f0ff;
  --color-trs15-ink: oklch(0.96 0.015 290);
  --color-trs15-mut: #8a85b8;
  --color-trs15-mut: oklch(0.64 0.05 290);
  --font-trs15-sans: 'Sora', system-ui, sans-serif;
  --font-trs15-mono: 'JetBrains Mono', ui-monospace, monospace;
}

@property --v {
  syntax: "<number>";
  inherits: true;
  initial-value: 0.65;
}

.trs-15 {
  width: 100%;
  min-height: 100svh;
  transition: --v 75ms linear;
}

@media (prefers-reduced-motion: reduce) {
  .trs-15 {
    transition: none;
  }
}
/* Two stacked gradient layers + a background-size pair: CSS, not a utility. */

.trs-15 .trs-15__grid {
  --grid: oklch(0.3 0.07 295);
  background: linear-gradient(var(--grid) 1px, transparent 1px), linear-gradient(90deg, var(--grid) 1px, transparent 1px);
  background-size: 24px 24px;
}
/* The peg: a tall prism with a lit top face and a hard base. */

.trs-15 input[type="range"]::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 24px;
  height: 30px;
  border: 0;
  border-radius: 4px 4px 0 0;
  background: linear-gradient(180deg, #c4b5fd, var(--color-trs15-acc));
  box-shadow: 0 -4px 12px color-mix(in oklab, var(--color-trs15-acc) 55%, transparent), 0 4px 0 oklch(0 0 0 / 0.45);
  cursor: ew-resize;
  transition: transform .15s;
}

.trs-15 input[type="range"]:active::-webkit-slider-thumb {
  transform: scaleY(1.12);
}

.trs-15 input[type="range"]::-moz-range-thumb {
  width: 24px;
  height: 30px;
  border: 0;
  border-radius: 4px;
  background: var(--color-trs15-acc);
  cursor: ew-resize;
}

@media (prefers-reduced-motion: reduce) {
  .trs-15 input[type="range"]::-webkit-slider-thumb {
    transition: none;
  }

  .trs-15 input[type="range"]:active::-webkit-slider-thumb {
    transform: none;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.getElementById('trs-15-root');
  var inp = document.getElementById('trs-15-inp');
  var GRADES = ['D', 'C', 'C+', 'B', 'B+', 'A', 'A+'];
  function update(){
    var v = +inp.value;
    root.style.setProperty('--v', v / 100);
    document.getElementById('trs-15-val').textContent = v;
    document.getElementById('trs-15-pow').textContent = v + 'W';
    document.getElementById('trs-15-spd').textContent = (v / 100 * 8).toFixed(1) + 'm/s';
    var g = GRADES[Math.min(GRADES.length - 1, Math.floor(v / 100 * GRADES.length))];
    document.getElementById('trs-15-eff').textContent = g;
    inp.setAttribute('aria-valuetext', v + ' percent intensity, grade ' + g);
  }
  inp.addEventListener('input', update);
  update();
})();
```
