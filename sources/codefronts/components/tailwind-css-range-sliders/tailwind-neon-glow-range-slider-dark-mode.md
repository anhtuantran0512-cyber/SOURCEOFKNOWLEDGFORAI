---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-range-sliders/tailwind-neon-glow-range-slider-dark-mode/"
title: "Tailwind CSS Neon Glow Range Slider for Dark Mode UI"
section: "components"
category: "tailwind-css-range-sliders"
category_name: "Tailwind CSS Range Sliders"
description: "A razor-thin track that floods with violet-to-cyan light as the thumb travels, plus a 30-bar intensity meter whose top quarter switches to cyan as a warning…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Neon Glow Range Slider for Dark Mode UI
Source: https://codefronts.com/components/tailwind-css-range-sliders/tailwind-neon-glow-range-slider-dark-mode/

A razor-thin track that floods with violet-to-cyan light as the thumb travels, plus a 30-bar intensity meter whose top quarter switches to cyan as a warning zone. The port's gain is that the glow scales with the value: opacity-[calc(0.25_+_var(--v)*0.6)] ties bloom intensity to the reading instead of holding one static shadow.
## HTML
```html
<section class="trs-03 w-full min-h-svh grid place-items-center bg-trs03-bg font-trs03-mono px-6 py-10" id="trs-03-root" style="--v:.73">
  <div class="relative w-[min(460px,100%)] rounded-2xl bg-trs03-panel border border-trs03-neon/25 px-8 py-9 shadow-[0_0_50px_-10px_var(--color-trs03-neon)]">
    <span class="absolute top-2.5 left-2.5 size-3 border-t-2 border-l-2 border-trs03-neon/70" aria-hidden="true"></span>
    <span class="absolute top-2.5 right-2.5 size-3 border-t-2 border-r-2 border-trs03-neon/70" aria-hidden="true"></span>
    <span class="absolute bottom-2.5 left-2.5 size-3 border-b-2 border-l-2 border-trs03-neon/70" aria-hidden="true"></span>
    <span class="absolute bottom-2.5 right-2.5 size-3 border-b-2 border-r-2 border-trs03-neon/70" aria-hidden="true"></span>

    <header class="flex items-center justify-between gap-4 mb-7">
      <h3 class="text-[11px] tracking-[0.3em] uppercase text-trs03-mut m-0">Intensity level</h3>
      <span class="text-[11px] tracking-[0.2em] text-trs03-cyan animate-trs03-blink motion-reduce:animate-none">● LIVE</span>
    </header>

    <div class="flex items-baseline gap-2 mb-8">
      <span class="text-trs03-neon bg-gradient-to-r from-trs03-neon to-trs03-cyan bg-clip-text text-transparent text-7xl font-bold leading-none tracking-tighter tabular-nums" id="trs-03-val">73</span>
      <span class="text-2xl text-trs03-mut">%</span>
    </div>

    <div class="relative h-8 flex items-center mb-3">
      <div class="absolute inset-x-0 h-0.5 rounded-full bg-trs03-mut/35"></div>
      <div class="absolute left-0 h-0.5 rounded-full w-[calc(var(--v)*100%)] bg-gradient-to-r from-trs03-neon to-trs03-cyan shadow-[0_0_10px_var(--color-trs03-neon)]"></div>
      <div class="absolute left-0 h-0.5 rounded-full w-[calc(var(--v)*100%)] shadow-[0_0_34px_8px_var(--color-trs03-neon)] opacity-[calc(0.25_+_var(--v)*0.6)]" aria-hidden="true"></div>
      <input type="range" min="0" max="100" value="73" id="trs-03-inp" aria-label="Intensity level"
             class="absolute inset-0 w-full h-8 appearance-none bg-transparent outline-none cursor-pointer z-10 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-trs03-cyan rounded-full">
    </div>

    <div class="flex justify-between text-[10px] text-trs03-mut mb-6">
      <span>0</span><span>25</span><span>50</span><span>75</span><span>100</span>
    </div>

    <div class="flex gap-[3px]" id="trs-03-meter" aria-hidden="true"></div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-trs03-bg: #040408;
  --color-trs03-bg: oklch(0.11 0.012 285);
  --color-trs03-panel: #0c0c18;
  --color-trs03-panel: oklch(0.16 0.02 285);
  --color-trs03-neon: #b400ff;
  --color-trs03-neon: oklch(0.6 0.29 305);
  --color-trs03-cyan: #00f5ff;
  --color-trs03-cyan: oklch(0.88 0.15 200);
  --color-trs03-ink: #e8e8ff;
  --color-trs03-ink: oklch(0.93 0.02 285);
  --color-trs03-mut: #8a8ab8;
  --color-trs03-mut: oklch(0.65 0.05 285);
  --font-trs03-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-trs03-blink: trs03-blink 1.4s step-end infinite;
}

@keyframes trs03-blink {
  0%,
    100% {
    opacity: 1;
  }

  50% {
    opacity: 0.15;
  }
}

@property --v {
  syntax: "<number>";
  inherits: true;
  initial-value: 0.73;
}

.trs-03 {
  width: 100%;
  min-height: 100svh;
}
/* Thumb: the cathode ring at the point of contact. */

.trs-03 input[type="range"]::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 22px;
  height: 22px;
  border-radius: 9999px;
  background: var(--color-trs03-bg);
  border: 2px solid var(--color-trs03-cyan);
  box-shadow: 0 0 10px var(--color-trs03-cyan), 0 0 30px color-mix(in oklab, var(--color-trs03-cyan) 40%, transparent);
  cursor: grab;
  transition: box-shadow .2s, transform .15s;
}

.trs-03 input[type="range"]:active::-webkit-slider-thumb {
  transform: scale(1.2);
  cursor: grabbing;
  box-shadow: 0 0 20px var(--color-trs03-cyan), 0 0 60px color-mix(in oklab, var(--color-trs03-cyan) 55%, transparent);
}

.trs-03 input[type="range"]::-moz-range-thumb {
  width: 22px;
  height: 22px;
  border-radius: 9999px;
  background: var(--color-trs03-bg);
  border: 2px solid var(--color-trs03-cyan);
  box-shadow: 0 0 10px var(--color-trs03-cyan);
  cursor: grab;
}

@media (prefers-reduced-motion: reduce) {
  .trs-03 input[type="range"]::-webkit-slider-thumb {
    transition: none;
  }

  .trs-03 input[type="range"]:active::-webkit-slider-thumb {
    transform: none;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.getElementById('trs-03-root');
  var inp = document.getElementById('trs-03-inp');
  var val = document.getElementById('trs-03-val');
  var meter = document.getElementById('trs-03-meter');
  var BARS = 30, HI = 0.75;

  for (var i = 0; i < BARS; i++) {
    var b = document.createElement('span');
    b.className = 'flex-1 h-1 rounded-sm bg-white/8 transition-colors duration-150 data-[on=true]:bg-trs03-neon data-[on=true]:shadow-[0_0_6px_var(--color-trs03-neon)] data-[hi=true]:bg-trs03-cyan data-[hi=true]:shadow-[0_0_6px_var(--color-trs03-cyan)] motion-reduce:transition-none';
    b.dataset.on = 'false'; b.dataset.hi = 'false';
    meter.appendChild(b);
  }
  var bars = Array.prototype.slice.call(meter.children);

  function update(){
    var v = +inp.value;
    root.style.setProperty('--v', v / 100);
    val.textContent = v;
    var on = Math.round(v / 100 * BARS);
    bars.forEach(function(b, i){
      var lit = i < on;
      b.dataset.on = lit ? 'true' : 'false';
      b.dataset.hi = (lit && i >= BARS * HI) ? 'true' : 'false';
    });
  }
  inp.addEventListener('input', update);
  update();
})();
```
