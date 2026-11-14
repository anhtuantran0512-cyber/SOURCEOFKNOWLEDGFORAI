---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-range-sliders/tailwind-vertical-range-sliders-audio-equalizer/"
title: "Tailwind CSS Vertical Range Sliders — 10-Band Audio Equalizer"
section: "components"
category: "tailwind-css-range-sliders"
category_name: "Tailwind CSS Range Sliders"
description: "Ten copper faders in inset steel grooves, dB readouts per band, four presets — and a live SVG response curve above the rack that the CSS original only listed…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Vertical Range Sliders — 10-Band Audio Equalizer
Source: https://codefronts.com/components/tailwind-css-range-sliders/tailwind-vertical-range-sliders-audio-equalizer/

Ten copper faders in inset steel grooves, dB readouts per band, four presets — and a live SVG response curve above the rack that the CSS original only listed as a "customization". Vertical orientation is one arbitrary utility pair now: [writing-mode:vertical-lr] [direction:rtl].
## HTML
```html
<section class="trs-07 w-full min-h-svh grid place-items-center bg-trs07-bg font-trs07-sans px-5 py-10">
  <div class="w-[min(520px,100%)] rounded-3xl bg-trs07-panel border border-trs07-edge p-8 shadow-[0_24px_70px_-26px_oklch(0_0_0/0.85)]">
    <header class="flex items-center justify-between gap-4 mb-6">
      <h3 class="text-sm font-bold uppercase tracking-[0.2em] text-trs07-ink m-0">Equalizer</h3>
      <div class="flex gap-1.5" aria-hidden="true">
        <span class="size-2 rounded-full bg-[#ff5f57] shadow-[0_0_6px_#ff5f57]"></span>
        <span class="size-2 rounded-full bg-[#febc2e] shadow-[0_0_6px_#febc2e]"></span>
        <span class="size-2 rounded-full bg-[#28c840] shadow-[0_0_6px_#28c840]"></span>
      </div>
    </header>

    <svg viewBox="0 0 300 60" class="w-full h-14 mb-2 overflow-visible" aria-hidden="true">
      <defs>
        <linearGradient id="trs-07-curve" x1="0" y1="0" x2="1" y2="0">
          <stop offset="0%" stop-color="var(--color-trs07-copper)"/>
          <stop offset="100%" stop-color="var(--color-trs07-copperlit)"/>
        </linearGradient>
      </defs>
      <line x1="0" y1="30" x2="300" y2="30" class="stroke-trs07-edge" stroke-width="1" stroke-dasharray="3 4"/>
      <polyline id="trs-07-curve-line" fill="none" stroke="url(#trs-07-curve)" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" points=""/>
    </svg>

    <div class="flex justify-between items-end h-52 mb-4" id="trs-07-rack" role="group" aria-label="Frequency bands"></div>

    <div class="flex flex-wrap gap-2 pt-4 border-t border-trs07-edge" id="trs-07-presets" role="group" aria-label="Equalizer presets">
      <button type="button" data-preset="flat" aria-pressed="true" class="min-h-11 rounded-full border border-trs07-edge bg-transparent px-4 text-[11px] font-semibold text-trs07-mut transition-colors duration-200 hover:border-trs07-copper hover:text-trs07-copper aria-pressed:border-trs07-copper aria-pressed:bg-trs07-copper/12 aria-pressed:text-trs07-copperlit focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-trs07-copper motion-reduce:transition-none">Flat</button>
      <button type="button" data-preset="bass" aria-pressed="false" class="min-h-11 rounded-full border border-trs07-edge bg-transparent px-4 text-[11px] font-semibold text-trs07-mut transition-colors duration-200 hover:border-trs07-copper hover:text-trs07-copper aria-pressed:border-trs07-copper aria-pressed:bg-trs07-copper/12 aria-pressed:text-trs07-copperlit focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-trs07-copper motion-reduce:transition-none">Bass boost</button>
      <button type="button" data-preset="treble" aria-pressed="false" class="min-h-11 rounded-full border border-trs07-edge bg-transparent px-4 text-[11px] font-semibold text-trs07-mut transition-colors duration-200 hover:border-trs07-copper hover:text-trs07-copper aria-pressed:border-trs07-copper aria-pressed:bg-trs07-copper/12 aria-pressed:text-trs07-copperlit focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-trs07-copper motion-reduce:transition-none">Treble</button>
      <button type="button" data-preset="vocal" aria-pressed="false" class="min-h-11 rounded-full border border-trs07-edge bg-transparent px-4 text-[11px] font-semibold text-trs07-mut transition-colors duration-200 hover:border-trs07-copper hover:text-trs07-copper aria-pressed:border-trs07-copper aria-pressed:bg-trs07-copper/12 aria-pressed:text-trs07-copperlit focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-trs07-copper motion-reduce:transition-none">Vocal</button>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-trs07-bg: #111318;
  --color-trs07-bg: oklch(0.18 0.01 262);
  --color-trs07-panel: #1a1d24;
  --color-trs07-panel: oklch(0.23 0.012 262);
  --color-trs07-edge: #2d3240;
  --color-trs07-edge: oklch(0.32 0.018 262);
  --color-trs07-copper: #b87333;
  --color-trs07-copper: oklch(0.62 0.12 55);
  --color-trs07-copperlit: #d4925a;
  --color-trs07-copperlit: oklch(0.72 0.1 55);
  --color-trs07-ink: #e2e8f0;
  --color-trs07-ink: oklch(0.92 0.01 255);
  --color-trs07-mut: #8a97ab;
  --color-trs07-mut: oklch(0.66 0.025 255);
  --font-trs07-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-trs07-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.trs-07 {
  width: 100%;
  min-height: 100svh;
}
/* Faders: the copper cap, plus the vertical appearance fallback for older
   WebKit. Everything else about orientation is a utility. */

.trs-07 input[type="range"] {
  -webkit-appearance: slider-vertical;
}

.trs-07 input[type="range"]::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 30px;
  height: 18px;
  border-radius: 4px;
  background: linear-gradient(180deg, #c8a07a 0%, #8b5e3c 50%, #c8a07a 100%);
  border: 1px solid oklch(1 0 0 / 0.16);
  box-shadow: 0 2px 8px oklch(0 0 0 / 0.5), inset 0 1px 0 oklch(1 0 0 / 0.2);
  cursor: grab;
  transition: box-shadow .15s;
}

.trs-07 input[type="range"]:active::-webkit-slider-thumb {
  cursor: grabbing;
  box-shadow: 0 0 0 4px color-mix(in oklab, var(--color-trs07-copper) 32%, transparent), 0 2px 8px oklch(0 0 0 / 0.5);
}

.trs-07 input[type="range"]::-moz-range-thumb {
  width: 30px;
  height: 18px;
  border-radius: 4px;
  background: linear-gradient(180deg, #c8a07a 0%, #8b5e3c 50%, #c8a07a 100%);
  border: 1px solid oklch(1 0 0 / 0.16);
  cursor: grab;
}

@media (prefers-reduced-motion: reduce) {
  .trs-07 input[type="range"]::-webkit-slider-thumb {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  var rack = document.getElementById('trs-07-rack');
  var curve = document.getElementById('trs-07-curve-line');
  var BANDS = [
    { label: '32', val: 50 }, { label: '64', val: 60 }, { label: '125', val: 70 },
    { label: '250', val: 65 }, { label: '500', val: 50 }, { label: '1K', val: 55 },
    { label: '2K', val: 60 }, { label: '4K', val: 58 }, { label: '8K', val: 50 }, { label: '16K', val: 45 }
  ];
  var PRESETS = {
    flat: [50,50,50,50,50,50,50,50,50,50],
    bass: [80,78,72,65,55,48,44,42,40,38],
    treble: [40,40,42,44,50,58,68,75,78,80],
    vocal: [38,42,50,65,72,70,65,55,48,42]
  };
  var faders = [];

  function db(v){ return (v - 50 >= 0 ? '+' : '') + (v - 50); }

  BANDS.forEach(function(band){
    var col = document.createElement('div');
    col.className = 'flex flex-col items-center gap-2 w-8';
    var readout = document.createElement('span');
    readout.className = 'font-trs07-mono text-[10px] text-trs07-mut tabular-nums';
    readout.textContent = db(band.val);
    var wrap = document.createElement('div');
    wrap.className = 'relative h-40 w-8 grid place-items-center';
    wrap.innerHTML = '<span class="absolute w-1.5 h-full rounded-full bg-gradient-to-b from-trs07-edge to-trs07-panel shadow-[inset_2px_2px_4px_oklch(0_0_0/0.6),inset_-1px_-1px_3px_oklch(1_0_0/0.05)]" aria-hidden="true"></span>';
    var inp = document.createElement('input');
    inp.type = 'range'; inp.min = '0'; inp.max = '100'; inp.value = band.val;
    inp.setAttribute('orient', 'vertical');
    inp.setAttribute('aria-label', band.label + ' hertz band');
    inp.className = 'relative z-10 w-8 h-40 appearance-none bg-transparent outline-none cursor-pointer [writing-mode:vertical-lr] [direction:rtl] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-trs07-copper rounded-full';
    inp.addEventListener('input', function(){
      readout.textContent = db(+inp.value);
      inp.setAttribute('aria-valuetext', db(+inp.value) + ' decibels at ' + band.label + ' hertz');
      draw();
    });
    wrap.appendChild(inp);
    var label = document.createElement('span');
    label.className = 'text-[10px] font-semibold uppercase tracking-wider text-trs07-copper';
    label.textContent = band.label;
    col.appendChild(readout); col.appendChild(wrap); col.appendChild(label);
    rack.appendChild(col);
    faders.push(inp);
  });

  function draw(){
    var pts = faders.map(function(f, i){
      var x = (i / (faders.length - 1)) * 300;
      var y = 30 - ((+f.value - 50) / 50) * 26;
      return x.toFixed(1) + ',' + y.toFixed(1);
    });
    curve.setAttribute('points', pts.join(' '));
  }

  document.querySelectorAll('#trs-07-presets button').forEach(function(btn){
    btn.addEventListener('click', function(){
      document.querySelectorAll('#trs-07-presets button').forEach(function(b){ b.setAttribute('aria-pressed', 'false'); });
      btn.setAttribute('aria-pressed', 'true');
      var vals = PRESETS[btn.dataset.preset];
      faders.forEach(function(f, i){ f.value = vals[i]; f.dispatchEvent(new Event('input')); });
    });
  });
  draw();
})();
```
