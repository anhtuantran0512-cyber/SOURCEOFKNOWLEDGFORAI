---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-range-sliders/tailwind-centre-origin-balance-slider-audio-pan/"
title: "Tailwind CSS Centre-Origin Balance Slider for Audio Pan Control"
section: "components"
category: "tailwind-css-range-sliders"
category_name: "Tailwind CSS Range Sliders"
description: "A pan control anchored at zero: the fill grows left or right from the midpoint in opposing channel colours, a 24-bar visualiser leans with it, and a centre…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Centre-Origin Balance Slider for Audio Pan Control
Source: https://codefronts.com/components/tailwind-css-range-sliders/tailwind-centre-origin-balance-slider-audio-pan/

A pan control anchored at zero: the fill grows left or right from the midpoint in opposing channel colours, a 24-bar visualiser leans with it, and a centre detent snaps the last few units back to dead centre. Both fills are one expression each — max() and clamp() do what an if/else chain did.
## HTML
```html
<section class="trs-13 w-full min-h-svh grid place-items-center bg-trs13-bg font-trs13-sans px-5 py-10" id="trs-13-root" style="--p:0">
  <div class="w-[min(470px,100%)] rounded-3xl bg-trs13-card border border-trs13-edge p-9 shadow-[0_24px_70px_-28px_oklch(0_0_0/0.8)]">
    <header class="text-center mb-8">
      <h3 class="text-lg font-bold text-trs13-ink m-0">Audio pan control</h3>
      <p class="text-[13px] text-trs13-mut mt-1 m-0">Drag from centre to pan left or right</p>
    </header>

    <div class="flex items-center justify-between gap-4 mb-6">
      <div class="text-center">
        <div class="text-[10px] uppercase tracking-[0.18em] text-trs13-mut">Left</div>
        <div class="font-trs13-mono text-[28px] font-semibold tracking-tight tabular-nums text-trs13-left" id="trs-13-left">50%</div>
      </div>
      <div class="flex flex-col items-center gap-1" id="trs-13-centre" data-centred="true">
        <span class="size-2.5 rounded-full bg-trs13-centre shadow-[0_0_8px_var(--color-trs13-centre)] opacity-30 transition-opacity duration-300 data-[centred=true]:opacity-100 motion-reduce:transition-none" id="trs-13-dot" data-centred="true"></span>
        <span class="text-[10px] font-semibold tracking-wider text-trs13-centre">C</span>
      </div>
      <div class="text-center">
        <div class="text-[10px] uppercase tracking-[0.18em] text-trs13-mut">Right</div>
        <div class="font-trs13-mono text-[28px] font-semibold tracking-tight tabular-nums text-trs13-right" id="trs-13-right">50%</div>
      </div>
    </div>

    <div class="relative h-12 flex items-center mb-2">
      <div class="absolute inset-x-0 h-2 rounded-full bg-trs13-edge"></div>
      <span class="absolute left-1/2 -translate-x-1/2 w-0.5 h-5 bg-trs13-centre/60" aria-hidden="true"></span>
      <div class="absolute right-1/2 h-2 rounded-l-full bg-trs13-left shadow-[0_0_14px_-2px_var(--color-trs13-left)] w-[calc(max(0,-1*var(--p))*50%)]" aria-hidden="true"></div>
      <div class="absolute left-1/2 h-2 rounded-r-full bg-trs13-right shadow-[0_0_14px_-2px_var(--color-trs13-right)] w-[calc(max(0,var(--p))*50%)]" aria-hidden="true"></div>
      <input type="range" min="-100" max="100" value="0" id="trs-13-inp" aria-label="Stereo pan"
             class="absolute inset-0 w-full h-12 appearance-none bg-transparent outline-none cursor-pointer z-10 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-trs13-centre rounded-full">
    </div>

    <div class="flex justify-between text-[11px] font-semibold mb-7">
      <span class="text-trs13-left">◀ L</span>
      <span class="text-trs13-right">R ▶</span>
    </div>

    <div class="flex items-end gap-[3px] h-15" id="trs-13-vis" aria-hidden="true"></div>

    <button type="button" id="trs-13-reset" class="block w-full min-h-11 mt-5 rounded-xl border border-trs13-edge text-xs font-semibold uppercase tracking-[0.12em] text-trs13-mut transition-colors duration-200 hover:border-trs13-centre hover:text-trs13-centre focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-trs13-centre motion-reduce:transition-none">⊙ Reset to centre</button>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-trs13-bg: #0a0f1e;
  --color-trs13-bg: oklch(0.17 0.03 262);
  --color-trs13-card: #111a2f;
  --color-trs13-card: oklch(0.22 0.035 262);
  --color-trs13-edge: #22304d;
  --color-trs13-edge: oklch(0.31 0.04 262);
  --color-trs13-left: #38bdf8;
  --color-trs13-left: oklch(0.75 0.14 225);
  --color-trs13-right: #fb7185;
  --color-trs13-right: oklch(0.72 0.17 15);
  --color-trs13-centre: #a3e635;
  --color-trs13-centre: oklch(0.85 0.19 125);
  --color-trs13-ink: #e2e8f0;
  --color-trs13-ink: oklch(0.92 0.01 255);
  --color-trs13-mut: #7c8ba6;
  --color-trs13-mut: oklch(0.63 0.03 255);
  --font-trs13-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-trs13-mono: 'JetBrains Mono', ui-monospace, monospace;
}

@property --p {
  syntax: "<number>";
  inherits: true;
  initial-value: 0;
}

.trs-13 {
  width: 100%;
  min-height: 100svh;
  transition: --p 75ms linear;
}

@media (prefers-reduced-motion: reduce) {
  .trs-13 {
    transition: none;
  }
}

.trs-13 input[type="range"]::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 28px;
  height: 28px;
  border-radius: 9999px;
  box-sizing: border-box;
  background: var(--color-trs13-edge);
  border: 3px solid var(--color-trs13-ink);
  box-shadow: 0 4px 16px oklch(0 0 0 / 0.55);
  cursor: grab;
  transition: transform .15s;
}

.trs-13 input[type="range"]:active::-webkit-slider-thumb {
  transform: scale(1.14);
  cursor: grabbing;
}

.trs-13 input[type="range"]::-moz-range-thumb {
  width: 28px;
  height: 28px;
  border-radius: 9999px;
  box-sizing: border-box;
  background: var(--color-trs13-edge);
  border: 3px solid var(--color-trs13-ink);
  cursor: grab;
}

@media (prefers-reduced-motion: reduce) {
  .trs-13 input[type="range"]::-webkit-slider-thumb {
    transition: none;
  }

  .trs-13 input[type="range"]:active::-webkit-slider-thumb {
    transform: none;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.getElementById('trs-13-root');
  var inp = document.getElementById('trs-13-inp');
  var dot = document.getElementById('trs-13-dot');
  var vis = document.getElementById('trs-13-vis');
  var leftPct = document.getElementById('trs-13-left');
  var rightPct = document.getElementById('trs-13-right');
  var BARS = 24, DETENT = 5;

  for (var i = 0; i < BARS; i++) {
    var b = document.createElement('span');
    b.className = 'flex-1 rounded-t-sm transition-[height,opacity] duration-150 motion-reduce:transition-none ' + (i < BARS / 2 ? 'bg-trs13-left' : 'bg-trs13-right');
    vis.appendChild(b);
    if (i === BARS / 2 - 1) {
      var d = document.createElement('span');
      d.className = 'w-0.5 h-full shrink-0 bg-trs13-centre/30';
      vis.appendChild(d);
    }
  }
  var bars = Array.prototype.slice.call(vis.querySelectorAll('span:not(.w-0\\.5)'));

  function update(){
    var v = +inp.value;
    if (Math.abs(v) <= DETENT && v !== 0) { v = 0; inp.value = 0; }
    root.style.setProperty('--p', v / 100);
    var l = Math.round(50 - v / 2), r = Math.round(50 + v / 2);
    leftPct.textContent = l + '%';
    rightPct.textContent = r + '%';
    dot.dataset.centred = v === 0 ? 'true' : 'false';
    inp.setAttribute('aria-valuetext', v === 0 ? 'Centred' : Math.abs(v) + '% ' + (v < 0 ? 'left' : 'right'));
    var half = BARS / 2, mag = Math.abs(v);
    bars.forEach(function(bar, i){
      var isLeft = i < half;
      var dist = isLeft ? (half - 1 - i) : (i - half);
      var h;
      if ((v < 0 && isLeft) || (v > 0 && !isLeft)) h = 10 + (dist / (half - 1)) * mag * 0.5;
      else if (v === 0) h = 10 + (1 - dist / half) * 20;
      else h = 8;
      bar.style.height = Math.min(60, h) + 'px';
      bar.style.opacity = String(0.3 + Math.min(60, h) / 60 * 0.7);
    });
  }
  inp.addEventListener('input', update);
  document.getElementById('trs-13-reset').addEventListener('click', function(){ inp.value = 0; update(); });
  update();
})();
```
