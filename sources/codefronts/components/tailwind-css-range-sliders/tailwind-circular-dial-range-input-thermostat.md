---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-range-sliders/tailwind-circular-dial-range-input-thermostat/"
title: "Tailwind CSS Circular Dial Range Input — Smart Thermostat UI"
section: "components"
category: "tailwind-css-range-sliders"
category_name: "Tailwind CSS Range Sliders"
description: "A 270° thermostat arc that fills from cool blue to warm orange, a target marker, ±1° buttons and an ETA that reacts to the gap between current and target."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Circular Dial Range Input — Smart Thermostat UI
Source: https://codefronts.com/components/tailwind-css-range-sliders/tailwind-circular-dial-range-input-thermostat/

A 270° thermostat arc that fills from cool blue to warm orange, a target marker, ±1° buttons and an ETA that reacts to the gap between current and target. The port's neat trick: the arc length is an arbitrary property — [stroke-dashoffset:calc(471_-_353*var(--v))] — so the SVG reads the same --v as everything else.
## HTML
```html
<section class="trs-08 w-full min-h-svh grid place-items-center bg-trs08-bg font-trs08-sans px-5 py-10" id="trs-08-root" style="--v:.545;--tint:var(--color-trs08-warm)">
  <div class="w-[min(380px,100%)] rounded-[28px] bg-trs08-card border border-trs08-edge p-9 text-center shadow-[0_24px_70px_-28px_oklch(0_0_0/0.8)]">
    <div class="flex rounded-xl bg-white/4 p-1 mb-8" role="group" aria-label="Mode">
      <button type="button" data-mode="heat" aria-pressed="true" class="flex-1 min-h-11 rounded-[10px] text-xs font-semibold text-trs08-mut transition-colors duration-200 aria-pressed:bg-[var(--tint)] aria-pressed:text-trs08-bg focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[var(--tint)] motion-reduce:transition-none">Heat</button>
      <button type="button" data-mode="cool" aria-pressed="false" class="flex-1 min-h-11 rounded-[10px] text-xs font-semibold text-trs08-mut transition-colors duration-200 aria-pressed:bg-[var(--tint)] aria-pressed:text-trs08-bg focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[var(--tint)] motion-reduce:transition-none">Cool</button>
      <button type="button" data-mode="fan" aria-pressed="false" class="flex-1 min-h-11 rounded-[10px] text-xs font-semibold text-trs08-mut transition-colors duration-200 aria-pressed:bg-[var(--tint)] aria-pressed:text-trs08-bg focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[var(--tint)] motion-reduce:transition-none">Fan</button>
    </div>

    <div class="relative size-50 mx-auto mb-7">
      <svg viewBox="0 0 180 180" class="size-50 -rotate-[135deg] pointer-events-none" aria-hidden="true">
        <defs>
          <linearGradient id="trs-08-grad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="var(--color-trs08-cool)"/>
            <stop offset="100%" stop-color="var(--tint)"/>
          </linearGradient>
        </defs>
        <circle cx="90" cy="90" r="75" fill="none" stroke="var(--color-trs08-edge)" stroke-width="14" stroke-linecap="round" stroke-dasharray="353 471"/>
        <circle cx="90" cy="90" r="75" fill="none" stroke="url(#trs-08-grad)" stroke-width="14" stroke-linecap="round"
                class="[stroke-dasharray:471] [stroke-dashoffset:calc(471_-_353*var(--v))] [filter:drop-shadow(0_0_7px_var(--tint))]"/>
      </svg>
      <span aria-hidden="true" class="absolute inset-0 rotate-[calc(var(--v)*270deg_-_45deg)]">
        <span class="absolute left-1/2 top-1.5 -translate-x-1/2 w-0.5 h-3 rounded-full bg-white/85"></span>
      </span>
      <div class="absolute inset-0 grid place-content-center">
        <div class="text-[52px] leading-none font-black tracking-tighter text-trs08-ink tabular-nums" id="trs-08-temp">22</div>
        <div class="text-lg text-trs08-mut">°C</div>
        <div class="text-[10px] uppercase tracking-[0.2em] text-trs08-mut mt-1.5">Target</div>
      </div>
    </div>

    <div class="flex items-center gap-3 mb-5">
      <button type="button" id="trs-08-down" aria-label="Decrease target by one degree" class="grid place-items-center size-11 shrink-0 rounded-full border border-trs08-edge text-trs08-ink text-lg transition-colors duration-150 hover:border-(--tint) hover:text-(--tint) focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-(--tint)">−</button>
      <input type="range" min="10" max="32" value="22" id="trs-08-inp" aria-label="Target temperature in Celsius"
             class="flex-1 h-1.5 appearance-none rounded-full bg-trs08-edge outline-none cursor-pointer z-10 focus-visible:outline-2 focus-visible:outline-offset-6 focus-visible:outline-(--tint)">
      <button type="button" id="trs-08-up" aria-label="Increase target by one degree" class="grid place-items-center size-11 shrink-0 rounded-full border border-trs08-edge text-trs08-ink text-lg transition-colors duration-150 hover:border-(--tint) hover:text-(--tint) focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-(--tint)">+</button>
    </div>

    <div class="grid grid-cols-3 gap-2.5">
      <div class="rounded-xl bg-white/3 border border-trs08-edge p-2.5">
        <div class="text-[10px] uppercase tracking-[0.12em] text-trs08-mut">Current</div>
        <div class="text-lg font-bold text-trs08-ink tabular-nums">18°C</div>
      </div>
      <div class="rounded-xl bg-white/3 border border-trs08-edge p-2.5">
        <div class="text-[10px] uppercase tracking-[0.12em] text-trs08-mut">Humidity</div>
        <div class="text-lg font-bold text-trs08-ink tabular-nums">64%</div>
      </div>
      <div class="rounded-xl bg-white/3 border border-trs08-edge p-2.5">
        <div class="text-[10px] uppercase tracking-[0.12em] text-trs08-mut">ETA</div>
        <div class="text-lg font-bold text-trs08-ink tabular-nums" id="trs-08-eta">12m</div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-trs08-bg: #0f1117;
  --color-trs08-bg: oklch(0.18 0.015 265);
  --color-trs08-card: #161b27;
  --color-trs08-card: oklch(0.23 0.02 265);
  --color-trs08-edge: #26344f;
  --color-trs08-edge: oklch(0.33 0.035 262);
  --color-trs08-warm: #f97316;
  --color-trs08-warm: oklch(0.7 0.19 45);
  --color-trs08-cool: #3b82f6;
  --color-trs08-cool: oklch(0.62 0.19 259);
  --color-trs08-fan: #22d3ee;
  --color-trs08-fan: oklch(0.82 0.13 200);
  --color-trs08-ink: #f1f5f9;
  --color-trs08-ink: oklch(0.97 0.006 255);
  --color-trs08-mut: #7b8aa3;
  --color-trs08-mut: oklch(0.63 0.03 255);
  --font-trs08-sans: 'Sora', system-ui, sans-serif;
}

@property --v {
  syntax: "<number>";
  inherits: true;
  initial-value: 0.545;
}
/* Tailwind v4 tree-shakes @theme entries that no generated utility references.
   The mode tints are consumed by raw CSS and by JS, so they are restated here
   as plain custom properties — otherwise every var() chain on them is
   invalid-at-computed-value-time and the tab, thumb and arc paint nothing. */

.trs-08 {
  /* --v is animated here so the arc's stroke-dashoffset and the tick's rotate
       — both calc() readers — recompute every frame. Transitioning those
       properties directly freezes them at their first-paint value. */
  transition: --v .15s ease-out;
  --color-trs08-warm: oklch(0.7 0.19 45);
  --color-trs08-cool: oklch(0.62 0.19 259);
  --color-trs08-fan: oklch(0.82 0.13 200);
  width: 100%;
  min-height: 100svh;
}

.trs-08 input[type="range"]::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 20px;
  height: 20px;
  border-radius: 9999px;
  background: var(--tint);
  box-shadow: 0 0 12px var(--tint);
  cursor: grab;
  transition: transform .15s;
}

.trs-08 input[type="range"]:active::-webkit-slider-thumb {
  transform: scale(1.2);
  cursor: grabbing;
}

.trs-08 input[type="range"]::-moz-range-thumb {
  width: 20px;
  height: 20px;
  border: 0;
  border-radius: 9999px;
  background: var(--tint);
  box-shadow: 0 0 12px var(--tint);
  cursor: grab;
}

@media (prefers-reduced-motion: reduce) {
  .trs-08 {
    transition: none;
  }

  .trs-08 input[type="range"]::-webkit-slider-thumb {
    transition: none;
  }

  .trs-08 input[type="range"]:active::-webkit-slider-thumb {
    transform: none;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.getElementById('trs-08-root');
  var inp = document.getElementById('trs-08-inp');
  var temp = document.getElementById('trs-08-temp');
  var eta = document.getElementById('trs-08-eta');
  var CURRENT = 18;
  var TINTS = { heat: 'var(--color-trs08-warm)', cool: 'var(--color-trs08-cool)', fan: 'var(--color-trs08-fan)' };

  function update(){
    var v = +inp.value;
    root.style.setProperty('--v', (v - +inp.min) / (+inp.max - +inp.min));
    temp.textContent = v;
    var mins = Math.abs(v - CURRENT) * 3;
    eta.textContent = mins === 0 ? 'At temp' : mins + 'm';
    inp.setAttribute('aria-valuetext', v + ' degrees Celsius target, currently ' + CURRENT);
  }
  inp.addEventListener('input', update);
  document.getElementById('trs-08-up').addEventListener('click', function(){ inp.value = Math.min(+inp.max, +inp.value + 1); update(); });
  document.getElementById('trs-08-down').addEventListener('click', function(){ inp.value = Math.max(+inp.min, +inp.value - 1); update(); });
  document.querySelectorAll('[data-mode]').forEach(function(btn){
    btn.addEventListener('click', function(){
      document.querySelectorAll('[data-mode]').forEach(function(b){ b.setAttribute('aria-pressed', 'false'); });
      btn.setAttribute('aria-pressed', 'true');
      root.style.setProperty('--tint', TINTS[btn.dataset.mode]);
    });
  });
  update();
})();
```
