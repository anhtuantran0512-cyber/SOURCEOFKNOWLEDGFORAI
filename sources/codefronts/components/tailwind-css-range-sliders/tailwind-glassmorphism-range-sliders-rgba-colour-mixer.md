---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-range-sliders/tailwind-glassmorphism-range-sliders-rgba-colour-mixer/"
title: "Tailwind CSS Glassmorphism Range Sliders — RGBA Colour Mixer"
section: "components"
category: "tailwind-css-range-sliders"
category_name: "Tailwind CSS Range Sliders"
description: "Four frosted tracks — R, G, B and opacity — over a four-point radial gradient, with a live swatch, hex and rgba readouts, copy-to-clipboard and an EyeDropper…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Glassmorphism Range Sliders — RGBA Colour Mixer
Source: https://codefronts.com/components/tailwind-css-range-sliders/tailwind-glassmorphism-range-sliders-rgba-colour-mixer/

Four frosted tracks — R, G, B and opacity — over a four-point radial gradient, with a live swatch, hex and rgba readouts, copy-to-clipboard and an EyeDropper pick. Glass is where Tailwind is strongest: backdrop-blur-xl bg-white/8 border-white/20 is the entire material.
## HTML
```html
<section class="trs-16 w-full min-h-svh grid place-items-center px-5 py-10 font-trs16-sans" id="trs-16-root" style="--r:.706;--g:.471;--b:.941;--a:.85">
  <div class="w-[min(470px,100%)] rounded-[28px] bg-white/8 backdrop-blur-xl border border-white/20 p-9 shadow-[0_24px_70px_-28px_oklch(0_0_0/0.6),inset_0_1px_0_oklch(1_0_0/0.25)]">
    <header class="flex items-start justify-between gap-4 mb-7">
      <div>
        <h3 class="text-lg font-bold text-white m-0">Colour mixer</h3>
        <p class="text-xs text-white/55 mt-1 m-0">Glassmorphism RGBA controller</p>
      </div>
      <div class="flex rounded-xl bg-black/25 border border-white/20 p-0.5" role="group" aria-label="Colour model">
        <button type="button" aria-pressed="true" class="min-h-9 rounded-[10px] px-3 text-[11px] font-semibold text-white/55 transition-colors duration-200 aria-pressed:bg-white/15 aria-pressed:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white">RGBA</button>
        <button type="button" aria-pressed="false" class="min-h-9 rounded-[10px] px-3 text-[11px] font-semibold text-white/55 transition-colors duration-200 aria-pressed:bg-white/15 aria-pressed:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white">HSL</button>
      </div>
    </header>

    <div class="flex flex-col gap-5" id="trs-16-rows"></div>

    <div class="flex items-center gap-4 mt-7 rounded-2xl bg-black/20 backdrop-blur-md border border-white/20 p-4">
      <div class="size-13 shrink-0 rounded-xl border border-white/25 shadow-[0_4px_16px_oklch(0_0_0/0.35)]" id="trs-16-swatch" aria-hidden="true"></div>
      <div class="min-w-0">
        <div class="font-trs16-mono text-lg font-bold tracking-[0.1em] text-white" id="trs-16-hex">#B478F0</div>
        <div class="text-[11px] text-white/55 truncate" id="trs-16-rgba">rgba(180, 120, 240, 0.85)</div>
      </div>
      <div class="ml-auto flex gap-2">
        <button type="button" id="trs-16-pick" hidden class="grid place-items-center min-h-11 min-w-11 rounded-xl bg-white/10 border border-white/20 text-white transition-colors duration-150 hover:bg-white/20 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white">
          <span class="sr-only">Pick a colour from the screen</span>
          <svg viewBox="0 0 24 24" class="size-5 fill-none stroke-current stroke-2"><path d="M4 20l6-6M14 6l4 4M12.5 3.5l8 8-3 3-8-8z"/></svg>
        </button>
        <button type="button" id="trs-16-copy" data-copied="false" class="min-h-11 rounded-xl bg-white/12 border border-white/25 px-3.5 text-xs font-semibold text-white transition-colors duration-150 hover:bg-white/20 data-[copied=true]:bg-white/85 data-[copied=true]:text-black focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white">Copy</button>
      </div>
    </div>
    <p class="sr-only" aria-live="polite" id="trs-16-live"></p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --font-trs16-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-trs16-mono: 'JetBrains Mono', ui-monospace, monospace;
}

@property --r {
  syntax: "<number>";
  inherits: true;
  initial-value: 0.7;
}

@property --g {
  syntax: "<number>";
  inherits: true;
  initial-value: 0.47;
}

@property --b {
  syntax: "<number>";
  inherits: true;
  initial-value: 0.94;
}

@property --a {
  syntax: "<number>";
  inherits: true;
  initial-value: 0.85;
}
/* Channel fills read these through calc(), so the transition lives here. */

.trs-16 {
  transition: --r 75ms linear, --g 75ms linear, --b 75ms linear, --a 75ms linear;
}

@media (prefers-reduced-motion: reduce) {
  .trs-16 {
    transition: none;
  }
}
/* A comma-separated multi-layer gradient is not an arbitrary background value
   v4 can parse, so the stage paint stays CSS — the glass has to have something
   behind it or backdrop-filter frosts nothing. */

.trs-16 {
  width: 100%;
  min-height: 100svh;
  background: radial-gradient(ellipse at 20% 30%, #7c3aed 0%, transparent 50%), radial-gradient(ellipse at 80% 20%, #0891b2 0%, transparent 50%), radial-gradient(ellipse at 60% 80%, #be185d 0%, transparent 50%), radial-gradient(ellipse at 10% 80%, #059669 0%, transparent 50%), #0f0f1a;
}
/* Frosted thumb: backdrop-filter on a pseudo-element, which has no utility form. */

.trs-16 input[type="range"]::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 22px;
  height: 22px;
  border-radius: 9999px;
  background: oklch(1 0 0 / 0.25);
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
  border: 1.5px solid oklch(1 0 0 / 0.6);
  box-shadow: 0 4px 16px oklch(0 0 0 / 0.3), inset 0 1px 0 oklch(1 0 0 / 0.4);
  cursor: grab;
  transition: transform .15s, box-shadow .15s;
}

.trs-16 input[type="range"]:active::-webkit-slider-thumb {
  transform: scale(1.18);
  cursor: grabbing;
  box-shadow: 0 4px 24px oklch(0 0 0 / 0.4), 0 0 0 5px oklch(1 0 0 / 0.12);
}

.trs-16 input[type="range"]::-moz-range-thumb {
  width: 22px;
  height: 22px;
  border-radius: 9999px;
  background: oklch(1 0 0 / 0.25);
  border: 1.5px solid oklch(1 0 0 / 0.6);
  cursor: grab;
}

@media (prefers-reduced-motion: reduce) {
  .trs-16 input[type="range"]::-webkit-slider-thumb {
    transition: none;
  }

  .trs-16 input[type="range"]:active::-webkit-slider-thumb {
    transform: none;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.getElementById('trs-16-root');
  var rowsEl = document.getElementById('trs-16-rows');
  var swatch = document.getElementById('trs-16-swatch');
  var hexEl = document.getElementById('trs-16-hex');
  var rgbaEl = document.getElementById('trs-16-rgba');
  var live = document.getElementById('trs-16-live');
  var copyBtn = document.getElementById('trs-16-copy');
  var pickBtn = document.getElementById('trs-16-pick');
  var CHANNELS = [
    { key: 'r', name: 'Red', max: 255, value: 180, fill: 'bg-gradient-to-r from-red-500/70 to-red-500/90 shadow-[0_0_12px_oklch(0.63_0.22_25/0.4)]' },
    { key: 'g', name: 'Green', max: 255, value: 120, fill: 'bg-gradient-to-r from-green-500/70 to-green-500/90 shadow-[0_0_12px_oklch(0.72_0.19_145/0.4)]' },
    { key: 'b', name: 'Blue', max: 255, value: 240, fill: 'bg-gradient-to-r from-blue-500/70 to-blue-500/90 shadow-[0_0_12px_oklch(0.62_0.19_259/0.4)]' },
    { key: 'a', name: 'Opacity', max: 100, value: 85, fill: 'bg-gradient-to-r from-white/30 to-white/70 shadow-[0_0_8px_oklch(1_0_0/0.25)]' }
  ];
  var inputs = {};

  CHANNELS.forEach(function(ch){
    var row = document.createElement('div');
    row.className = 'flex flex-col gap-2';
    row.innerHTML =
      '<div class="flex items-center justify-between">' +
        '<span class="text-xs font-medium text-white/55">' + ch.name + '</span>' +
        '<span class="text-sm font-bold text-white tabular-nums" data-out></span>' +
      '</div>' +
      '<div class="relative h-6 rounded-full bg-black/25 backdrop-blur-sm border border-white/15 p-[3px]">' +
        '<div class="relative w-full h-full">' +
          '<div class="absolute inset-y-0 left-0 rounded-full ' + ch.fill + ' w-[calc(var(--' + ch.key + ')*100%)]"></div>' +
        '</div>' +
      '</div>';
    var holder = row.querySelector('.relative.w-full');
    var inp = document.createElement('input');
    inp.type = 'range'; inp.min = '0'; inp.max = String(ch.max); inp.value = String(ch.value);
    inp.setAttribute('aria-label', ch.name);
    inp.className = 'absolute inset-0 w-full h-full appearance-none bg-transparent outline-none cursor-pointer z-10 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-white rounded-full';
    inp.addEventListener('input', update);
    holder.appendChild(inp);
    rowsEl.appendChild(row);
    inputs[ch.key] = { input: inp, out: row.querySelector('[data-out]'), ch: ch };
  });

  function hex2(n){ return n.toString(16).padStart(2, '0').toUpperCase(); }
  function current(){
    var r = +inputs.r.input.value, g = +inputs.g.input.value, b = +inputs.b.input.value;
    var a = (+inputs.a.input.value / 100).toFixed(2);
    return { r: r, g: g, b: b, a: a, css: 'rgba(' + r + ', ' + g + ', ' + b + ', ' + a + ')', hex: '#' + hex2(r) + hex2(g) + hex2(b) };
  }

  function update(){
    CHANNELS.forEach(function(ch){
      var o = inputs[ch.key];
      root.style.setProperty('--' + ch.key, +o.input.value / ch.max);
      o.out.textContent = ch.key === 'a' ? o.input.value + '%' : o.input.value;
      o.input.setAttribute('aria-valuetext', ch.name + ' ' + o.input.value);
    });
    var c = current();
    swatch.style.background = c.css;
    hexEl.textContent = c.hex;
    rgbaEl.textContent = c.css;
    copyBtn.dataset.copied = 'false';
    copyBtn.textContent = 'Copy';
  }

  copyBtn.addEventListener('click', function(){
    var c = current();
    var done = function(msg){ live.textContent = msg; };
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(c.css).then(function(){
        copyBtn.dataset.copied = 'true';
        copyBtn.textContent = 'Copied';
        done(c.css + ' copied to clipboard');
      }).catch(function(){ done('Copy blocked by the browser'); });
    } else { done('Clipboard unavailable'); }
  });

  if (window.EyeDropper) {
    pickBtn.hidden = false;
    pickBtn.addEventListener('click', function(){
      new window.EyeDropper().open().then(function(res){
        var m = res.sRGBHex.replace('#', '');
        inputs.r.input.value = parseInt(m.slice(0, 2), 16);
        inputs.g.input.value = parseInt(m.slice(2, 4), 16);
        inputs.b.input.value = parseInt(m.slice(4, 6), 16);
        update();
        live.textContent = 'Picked ' + res.sRGBHex;
      }).catch(function(){});
    });
  }
  update();
})();
```
