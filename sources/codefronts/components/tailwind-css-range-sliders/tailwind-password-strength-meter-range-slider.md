---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-range-sliders/tailwind-password-strength-meter-range-slider/"
title: "Tailwind CSS Password Strength Meter with Range Slider Control"
section: "components"
category: "tailwind-css-range-sliders"
category_name: "Tailwind CSS Range Sliders"
description: "Four strength zones — weak, fair, good, strong — driving a shield, four segments, the fill, the numeral and a live checklist."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Password Strength Meter with Range Slider Control
Source: https://codefronts.com/components/tailwind-css-range-sliders/tailwind-password-strength-meter-range-slider/

Four strength zones — weak, fair, good, strong — driving a shield, four segments, the fill, the numeral and a live checklist. The port replaces eight inline style writes per change with one --tone property, and the slider is now linked to a real password field: type, and the meter follows.
## HTML
```html
<section class="trs-12 w-full min-h-svh grid place-items-center bg-trs12-bg font-trs12-sans px-5 py-10" id="trs-12-root" style="--v:.143;--tone:var(--color-trs12-fair)">
  <div class="w-[min(430px,100%)] rounded-3xl bg-trs12-card border border-trs12-edge p-9 shadow-[0_24px_70px_-28px_oklch(0_0_0/0.75)]">
    <div class="grid place-items-center size-14 rounded-2xl text-[28px] mb-5 bg-[color-mix(in_oklab,var(--tone)_18%,transparent)] shadow-[0_0_28px_-6px_var(--tone)]" id="trs-12-shield" aria-hidden="true">🔒</div>

    <h3 class="text-xl font-bold text-trs12-ink m-0">Password strength</h3>
    <p class="text-[13px] text-trs12-mut mt-1 mb-6 m-0">Type a password, or drag the character count</p>

    <label class="block mb-6">
      <span class="sr-only">Password</span>
      <input type="password" id="trs-12-pw" autocomplete="new-password" placeholder="Try typing here…"
             class="w-full min-h-11 rounded-xl bg-trs12-well border border-trs12-edge px-3.5 font-trs12-mono text-sm text-trs12-ink placeholder:text-trs12-mut outline-none transition-colors duration-200 focus-visible:border-(--tone) focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-(--tone)">
    </label>

    <div class="flex items-center justify-between gap-3 mb-3">
      <span class="text-[13px] text-trs12-mut">Strength level</span>
      <span class="rounded-full px-2.5 py-1 text-xs font-bold transition-[background-color,color] duration-400 motion-reduce:transition-none" id="trs-12-badge" aria-live="polite">Fair</span>
    </div>

    <div class="flex gap-1 mb-6" id="trs-12-segs" aria-hidden="true">
      <span class="flex-1 h-1.5 rounded-full bg-trs12-edge data-[on=true]:bg-(--tone)" data-on="false"></span>
      <span class="flex-1 h-1.5 rounded-full bg-trs12-edge data-[on=true]:bg-(--tone)" data-on="false"></span>
      <span class="flex-1 h-1.5 rounded-full bg-trs12-edge data-[on=true]:bg-(--tone)" data-on="false"></span>
      <span class="flex-1 h-1.5 rounded-full bg-trs12-edge data-[on=true]:bg-(--tone)" data-on="false"></span>
    </div>

    <div class="relative h-12 flex items-center mb-5">
      <div class="absolute inset-x-0 h-2.5 rounded-full bg-trs12-edge"></div>
      <div class="absolute left-0 h-2.5 rounded-full w-[calc(var(--v)*100%)] bg-(--tone)"></div>
      <input type="range" min="4" max="32" value="8" id="trs-12-inp" aria-label="Password length"
             class="absolute inset-0 w-full h-12 appearance-none bg-transparent outline-none cursor-pointer z-10 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-(--tone) rounded-full">
    </div>

    <div class="flex items-baseline gap-2 mb-6">
      <span class="text-[64px] leading-none font-bold tracking-tighter tabular-nums text-(--tone)" id="trs-12-num">8</span>
      <span class="text-[13px] text-trs12-mut">characters</span>
    </div>

    <ul class="flex flex-col gap-2 m-0 p-0 list-none" id="trs-12-rules"></ul>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-trs12-bg: #0f172a;
  --color-trs12-bg: oklch(0.21 0.03 262);
  --color-trs12-card: #1c2740;
  --color-trs12-card: oklch(0.27 0.035 262);
  --color-trs12-well: #16203a;
  --color-trs12-well: oklch(0.24 0.035 262);
  --color-trs12-edge: #35435e;
  --color-trs12-edge: oklch(0.38 0.035 262);
  --color-trs12-ink: #f1f5f9;
  --color-trs12-ink: oklch(0.97 0.006 255);
  --color-trs12-mut: #8494ad;
  --color-trs12-mut: oklch(0.66 0.03 255);
  --color-trs12-weak: #ef4444;
  --color-trs12-weak: oklch(0.63 0.22 25);
  --color-trs12-fair: #f59e0b;
  --color-trs12-fair: oklch(0.76 0.16 70);
  --color-trs12-good: #10b981;
  --color-trs12-good: oklch(0.7 0.16 165);
  --color-trs12-strong: #06b6d4;
  --color-trs12-strong: oklch(0.73 0.13 205);
  --font-trs12-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-trs12-mono: 'JetBrains Mono', ui-monospace, monospace;
}

@property --v {
  syntax: "<number>";
  inherits: true;
  initial-value: 0.143;
}
/* Zone colours are read by raw CSS (the thumb) and by JS, never by a generated
   utility, so v4 would tree-shake them out of @theme — restated here. */
/* --tone is registered as a <color> and animated here; its consumers must NOT
   carry their own paint transitions or they freeze at the first-paint zone. */

@property --tone {
  syntax: "<color>";
  inherits: true;
  initial-value: oklch(0.76 0.16 70);
}

.trs-12 {
  transition: --tone .4s ease;
  --color-trs12-weak: oklch(0.63 0.22 25);
  --color-trs12-fair: oklch(0.76 0.16 70);
  --color-trs12-good: oklch(0.7 0.16 165);
  --color-trs12-strong: oklch(0.73 0.13 205);
  width: 100%;
  min-height: 100svh;
}

.trs-12 input[type="range"]::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 26px;
  height: 26px;
  border-radius: 9999px;
  box-sizing: border-box;
  background: #fff;
  border: 3px solid var(--tone);
  box-shadow: 0 2px 12px oklch(0 0 0 / 0.45);
  cursor: grab;
  transition: border-color .4s, transform .15s;
}

.trs-12 input[type="range"]:active::-webkit-slider-thumb {
  transform: scale(1.14);
  cursor: grabbing;
}

.trs-12 input[type="range"]::-moz-range-thumb {
  width: 26px;
  height: 26px;
  border-radius: 9999px;
  box-sizing: border-box;
  background: #fff;
  border: 3px solid var(--tone);
  cursor: grab;
}

@media (prefers-reduced-motion: reduce) {
  .trs-12 {
    transition: none;
  }

  .trs-12 input[type="range"]::-webkit-slider-thumb {
    transition: none;
  }

  .trs-12 input[type="range"]:active::-webkit-slider-thumb {
    transform: none;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.getElementById('trs-12-root');
  var inp = document.getElementById('trs-12-inp');
  var pw = document.getElementById('trs-12-pw');
  var num = document.getElementById('trs-12-num');
  var badge = document.getElementById('trs-12-badge');
  var shield = document.getElementById('trs-12-shield');
  var segs = Array.prototype.slice.call(document.getElementById('trs-12-segs').children);
  var rulesEl = document.getElementById('trs-12-rules');
  var LEVELS = [
    { max: 7,  tone: 'var(--color-trs12-weak)',   label: 'Weak',   badgeBg: 'oklch(0.95 0.03 25)',  badgeInk: 'oklch(0.4 0.16 25)',  icon: '🔓', segs: 1 },
    { max: 11, tone: 'var(--color-trs12-fair)',   label: 'Fair',   badgeBg: 'oklch(0.96 0.04 85)',  badgeInk: 'oklch(0.45 0.13 70)', icon: '🔒', segs: 2 },
    { max: 19, tone: 'var(--color-trs12-good)',   label: 'Good',   badgeBg: 'oklch(0.95 0.04 165)', badgeInk: 'oklch(0.42 0.12 165)',icon: '🛡️', segs: 3 },
    { max: 99, tone: 'var(--color-trs12-strong)', label: 'Strong', badgeBg: 'oklch(0.95 0.04 205)', badgeInk: 'oklch(0.42 0.1 205)', icon: '🔐', segs: 4 }
  ];
  var RULES = [[8, '8+ characters for basic security'], [12, '12+ characters recommended'], [20, '20+ characters for maximum security']];
  var lastLabel = '';

  RULES.forEach(function(r){
    var li = document.createElement('li');
    li.dataset.ok = 'false';
    li.className = 'flex items-center gap-2.5 text-[13px] text-trs12-mut transition-colors duration-300 data-[ok=true]:text-trs12-ink motion-reduce:transition-none';
    li.innerHTML = '<span class="grid place-items-center size-5 shrink-0 rounded-full bg-trs12-edge text-[11px] transition-colors duration-300 data-[ok=true]:bg-trs12-good motion-reduce:transition-none" data-ok="false" aria-hidden="true">✗</span><span>' + r[1] + '</span>';
    rulesEl.appendChild(li);
  });
  var rows = Array.prototype.slice.call(rulesEl.children);

  function level(v){ for (var i = 0; i < LEVELS.length; i++) if (v <= LEVELS[i].max) return LEVELS[i]; return LEVELS[3]; }

  function update(){
    var v = +inp.value, lv = level(v);
    root.style.setProperty('--tone', lv.tone);
    root.style.setProperty('--v', (v - +inp.min) / (+inp.max - +inp.min));
    num.textContent = v;
    shield.textContent = lv.icon;
    if (lv.label !== lastLabel) {
      badge.textContent = lv.label;
      badge.style.backgroundColor = lv.badgeBg;
      badge.style.color = lv.badgeInk;
      lastLabel = lv.label;
    }
    segs.forEach(function(s, i){ s.dataset.on = i < lv.segs ? 'true' : 'false'; });
    rows.forEach(function(row, i){
      var ok = v >= RULES[i][0];
      row.dataset.ok = ok ? 'true' : 'false';
      var icon = row.firstElementChild;
      icon.dataset.ok = ok ? 'true' : 'false';
      icon.textContent = ok ? '✓' : '✗';
    });
    inp.setAttribute('aria-valuetext', lv.label + ', ' + v + ' characters');
  }

  inp.addEventListener('input', function(){ update(); });
  pw.addEventListener('input', function(){
    inp.value = Math.min(+inp.max, Math.max(+inp.min, pw.value.length));
    update();
  });
  update();
})();
```
