---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-range-sliders/tailwind-retro-8-bit-pixel-art-range-slider/"
title: "Tailwind CSS Retro 8-Bit Pixel Art Range Slider (Game HP Bar)"
section: "components"
category: "tailwind-css-range-sliders"
category_name: "Tailwind CSS Range Sliders"
description: "An arcade HP meter: segmented bar, gold octagon thumb, a sprite that changes with damage, coin lives and a scanline overlay."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Retro 8-Bit Pixel Art Range Slider (Game HP Bar)
Source: https://codefronts.com/components/tailwind-css-range-sliders/tailwind-retro-8-bit-pixel-art-range-slider/

An arcade HP meter: segmented bar, gold octagon thumb, a sprite that changes with damage, coin lives and a scanline overlay. The port keeps the crunch — steps() timing, zero-blur shadows, no transitions on the fill — and adds a damage flash and a status line the original only hinted at.
## HTML
```html
<section class="trs-14 w-full min-h-svh grid place-items-center bg-trs14-bg font-trs14-mono [image-rendering:pixelated] px-6 py-12" id="trs-14-root" style="--v:.75" data-hurt="false">
  <div class="w-[min(430px,100%)] bg-trs14-card border-[3px] border-trs14-edge p-7 shadow-[3px_0_0_var(--color-trs14-edge),0_3px_0_var(--color-trs14-edge),6px_6px_0_oklch(0_0_0/0.6)]">
    <div class="relative bg-[#0d0d1a] border-[3px] border-black p-5 mb-5 flex items-center gap-4 shadow-[inset_0_0_20px_oklch(0_0_0/0.8),0_0_30px_-8px_var(--color-trs14-blue)] data-[hurt=true]:bg-[#3a0d14] transition-none" id="trs-14-screen" data-hurt="false">
      <span class="absolute inset-0 pointer-events-none bg-[repeating-linear-gradient(0deg,transparent_0_2px,oklch(0_0_0/0.16)_2px_4px)]" aria-hidden="true"></span>
      <div class="text-[40px] leading-none shrink-0 animate-trs14-bob motion-reduce:animate-none" id="trs-14-sprite" aria-hidden="true">⚔️</div>
      <div class="flex-1">
        <div class="flex items-center justify-between mb-1.5">
          <span class="font-trs14-pixel text-[9px] uppercase text-trs14-mut">HP</span>
          <span class="text-base font-bold text-trs14-gold tabular-nums" id="trs-14-hp">75 / 100</span>
        </div>
        <div class="h-3.5 bg-black border-2 border-[#333] overflow-hidden">
          <div class="h-full w-[calc(var(--v)*100%)] bg-trs14-green shadow-[inset_0_2px_0_oklch(1_0_0/0.3)] transition-none" id="trs-14-bar"></div>
        </div>
        <p class="font-trs14-pixel text-[8px] leading-relaxed text-trs14-mut mt-2 m-0" id="trs-14-status" aria-live="polite">READY</p>
      </div>
    </div>

    <p class="font-trs14-pixel text-[8px] text-center uppercase tracking-[0.2em] text-trs14-mut mb-3 m-0">⬛ Power level ⬛</p>

    <div class="relative h-5 bg-black border-[3px] border-[#333] mb-3">
      <div class="absolute inset-y-0 left-0 w-[calc(var(--v)*100%)] bg-[repeating-linear-gradient(90deg,var(--color-trs14-blue)_0_12px,transparent_12px_16px)] transition-none" aria-hidden="true"></div>
      <input type="range" min="0" max="100" step="5" value="75" id="trs-14-inp" aria-label="Power level"
             class="absolute inset-0 w-full h-full appearance-none bg-transparent outline-none cursor-ew-resize z-10 focus-visible:outline-[3px] focus-visible:outline-offset-4 focus-visible:outline-trs14-gold">
    </div>

    <div class="flex flex-wrap justify-center gap-1.5 mt-4" id="trs-14-coins" aria-hidden="true"></div>

    <div class="flex gap-2 mt-5">
      <button type="button" data-set="0" class="flex-1 min-h-11 font-trs14-pixel text-[8px] uppercase tracking-wider text-white bg-trs14-red border-[3px] border-black shadow-[3px_3px_0_#000] transition-[translate,box-shadow] duration-100 active:translate-x-[2px] active:translate-y-[2px] active:shadow-[1px_1px_0_#000] focus-visible:outline-[3px] focus-visible:outline-offset-2 focus-visible:outline-trs14-gold motion-reduce:transition-none">☠ Dead</button>
      <button type="button" data-set="100" class="flex-1 min-h-11 font-trs14-pixel text-[8px] uppercase tracking-wider text-black bg-trs14-gold border-[3px] border-black shadow-[3px_3px_0_#000] transition-[translate,box-shadow] duration-100 active:translate-x-[2px] active:translate-y-[2px] active:shadow-[1px_1px_0_#000] focus-visible:outline-[3px] focus-visible:outline-offset-2 focus-visible:outline-trs14-gold motion-reduce:transition-none">★ Max HP</button>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-trs14-bg: #1a1c2c;
  --color-trs14-bg: oklch(0.24 0.035 285);
  --color-trs14-card: #29293d;
  --color-trs14-card: oklch(0.31 0.03 285);
  --color-trs14-edge: #4a4a62;
  --color-trs14-edge: oklch(0.42 0.03 285);
  --color-trs14-gold: #f5a623;
  --color-trs14-gold: oklch(0.79 0.16 75);
  --color-trs14-red: #ff0044;
  --color-trs14-red: oklch(0.6 0.27 15);
  --color-trs14-green: #00e676;
  --color-trs14-green: oklch(0.83 0.21 150);
  --color-trs14-blue: #29adff;
  --color-trs14-blue: oklch(0.72 0.15 240);
  --color-trs14-mut: #9a9ac0;
  --color-trs14-mut: oklch(0.68 0.04 285);
  --font-trs14-mono: 'Space Mono', ui-monospace, monospace;
  --font-trs14-pixel: 'Press Start 2P', 'Space Mono', monospace;
  --animate-trs14-bob: trs14-bob 0.6s steps(2) infinite;
}

@keyframes trs14-bob {
  0%,
    100% {
    transform: translateY(0);
  }

  50% {
    transform: translateY(-4px);
  }
}

@property --v {
  syntax: "<number>";
  inherits: true;
  initial-value: 0.75;
}

.trs-14 {
  width: 100%;
  min-height: 100svh;
}
/* The gem thumb: an octagon, WebKit only — Firefox gets a square block. */

.trs-14 input[type="range"]::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 20px;
  height: 26px;
  border: 0;
  background: var(--color-trs14-gold);
  box-shadow: 3px 3px 0 #000, -1px -1px 0 oklch(1 0 0 / 0.5);
  clip-path: polygon(20% 0, 80% 0, 100% 20%, 100% 80%, 80% 100%, 20% 100%, 0 80%, 0 20%);
  cursor: ew-resize;
}

.trs-14 input[type="range"]::-moz-range-thumb {
  width: 20px;
  height: 26px;
  border: 3px solid #000;
  border-radius: 0;
  background: var(--color-trs14-gold);
  cursor: ew-resize;
}
```

## JavaScript
```js
(function(){
  var root = document.getElementById('trs-14-root');
  var screenEl = document.getElementById('trs-14-screen');
  var inp = document.getElementById('trs-14-inp');
  var bar = document.getElementById('trs-14-bar');
  var hp = document.getElementById('trs-14-hp');
  var sprite = document.getElementById('trs-14-sprite');
  var status = document.getElementById('trs-14-status');
  var coinsEl = document.getElementById('trs-14-coins');
  var COINS = 10;
  var SPRITES = [
    { max: 20, icon: '💀', tone: 'bg-trs14-red', text: 'CRITICAL — GAME OVER SOON' },
    { max: 40, icon: '😵', tone: 'bg-trs14-red', text: 'DANGER — FIND A POTION' },
    { max: 60, icon: '😤', tone: 'bg-trs14-gold', text: 'WOUNDED' },
    { max: 80, icon: '⚔️', tone: 'bg-trs14-green', text: 'READY' },
    { max: 100, icon: '🔱', tone: 'bg-trs14-green', text: 'FULL POWER' }
  ];
  var prev = +inp.value, flash;

  for (var i = 0; i < COINS; i++) {
    var c = document.createElement('span');
    c.className = 'text-lg grayscale brightness-50 transition-[filter] duration-150 data-[on=true]:grayscale-0 data-[on=true]:brightness-100 data-[on=true]:drop-shadow-[0_0_4px_var(--color-trs14-gold)] motion-reduce:transition-none';
    c.dataset.on = 'false';
    c.textContent = '🪙';
    coinsEl.appendChild(c);
  }
  var coins = Array.prototype.slice.call(coinsEl.children);

  function update(){
    var v = +inp.value;
    root.style.setProperty('--v', v / 100);
    hp.textContent = v + ' / 100';
    var sp = SPRITES.find(function(s){ return v <= s.max; }) || SPRITES[4];
    sprite.textContent = sp.icon;
    status.textContent = sp.text;
    bar.className = 'h-full w-[calc(var(--v)*100%)] shadow-[inset_0_2px_0_oklch(1_0_0/0.3)] transition-none ' + sp.tone;
    var on = Math.round(v / 100 * COINS);
    coins.forEach(function(c, i){ c.dataset.on = i < on ? 'true' : 'false'; });
    inp.setAttribute('aria-valuetext', v + ' of 100 hit points, ' + sp.text.toLowerCase());
    if (v < prev) {
      screenEl.dataset.hurt = 'true';
      clearTimeout(flash);
      flash = setTimeout(function(){ screenEl.dataset.hurt = 'false'; }, 220);
    }
    prev = v;
  }
  inp.addEventListener('input', update);
  document.querySelectorAll('[data-set]').forEach(function(b){
    b.addEventListener('click', function(){ inp.value = b.dataset.set; update(); });
  });
  update();
})();
```
