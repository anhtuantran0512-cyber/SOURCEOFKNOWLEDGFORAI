---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-range-sliders/tailwind-range-slider-popup-value-bubble-loan-calculator/"
title: "Tailwind CSS Range Slider with Pop-Up Value Bubble (Loan Calculator)"
section: "components"
category: "tailwind-css-range-sliders"
category_name: "Tailwind CSS Range Sliders"
description: "A loan slider whose value bubble springs out of the thumb while you drag, with live monthly payment, total interest and a working term selector."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Range Slider with Pop-Up Value Bubble (Loan Calculator)
Source: https://codefronts.com/components/tailwind-css-range-sliders/tailwind-range-slider-popup-value-bubble-loan-calculator/

A loan slider whose value bubble springs out of the thumb while you drag, with live monthly payment, total interest and a working term selector. The port deletes four JS event listeners: has-[input:active]: and has-[input:focus-visible]: show the bubble, so pointer and keyboard behave identically.
## HTML
```html
<section class="trs-10 w-full min-h-svh grid place-items-center bg-trs10-bg font-trs10-sans px-5 py-10" id="trs-10-root" style="--v:.286">
  <div class="w-[min(460px,100%)] rounded-3xl bg-trs10-card border border-trs10-edge p-9 shadow-[0_24px_70px_-28px_oklch(0_0_0/0.7)]">
    <header class="mb-3">
      <h3 class="text-lg font-extrabold text-trs10-ink m-0">Loan calculator</h3>
      <p class="text-[13px] text-trs10-mut mt-1 m-0">Drag to adjust your loan amount</p>
    </header>

    <div class="flex items-baseline gap-1.5 mt-5 mb-11">
      <span class="text-2xl font-bold text-trs10-acc2">$</span>
      <span class="text-[56px] leading-none font-black tracking-tighter text-trs10-ink tabular-nums" id="trs-10-amount">15,000</span>
      <span class="text-sm text-trs10-mut self-end mb-2">loan</span>
    </div>

    <div class="relative pt-14" id="trs-10-wrap">
      <div aria-hidden="true" class="absolute top-0 left-[calc(var(--v)*100%)] -translate-x-1/2 flex flex-col items-center pointer-events-none">
        <span class="origin-bottom scale-0 rounded-full bg-trs10-acc px-3.5 py-1.5 font-trs10-mono text-[13px] font-semibold text-white whitespace-nowrap shadow-[0_6px_22px_-4px_var(--color-trs10-acc)] transition-transform duration-250 ease-[cubic-bezier(0.34,1.56,0.64,1)] group-has-[input:active]/wrap:scale-100 motion-reduce:transition-none" id="trs-10-tip">$15,000</span>
      </div>
      <div class="group/wrap relative">
        <div class="h-2 rounded-full bg-white/8"></div>
        <div class="absolute left-0 bottom-0 h-2 rounded-full w-[calc(var(--v)*100%)] bg-gradient-to-r from-trs10-acc to-trs10-acc2 shadow-[0_0_18px_-2px_var(--color-trs10-acc)]"></div>
        <input type="range" min="1000" max="50000" step="500" value="15000" id="trs-10-inp" aria-label="Loan amount"
               class="absolute -bottom-3.5 left-0 w-full h-9 appearance-none bg-transparent outline-none cursor-pointer z-10 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-trs10-acc2 rounded-full">
      </div>
    </div>

    <div class="flex justify-between font-trs10-mono text-[11px] text-trs10-mut mt-3.5">
      <span>$1K</span><span>$10K</span><span>$25K</span><span>$50K</span>
    </div>

    <div class="flex gap-2 mt-6" role="group" aria-label="Loan term" id="trs-10-terms">
      <button type="button" data-term="12" aria-pressed="false" class="flex-1 min-h-11 rounded-xl border border-trs10-edge text-xs font-semibold text-trs10-mut transition-colors duration-150 hover:text-trs10-ink aria-pressed:border-trs10-acc2 aria-pressed:bg-trs10-acc/20 aria-pressed:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-trs10-acc2">12 mo</button>
      <button type="button" data-term="24" aria-pressed="false" class="flex-1 min-h-11 rounded-xl border border-trs10-edge text-xs font-semibold text-trs10-mut transition-colors duration-150 hover:text-trs10-ink aria-pressed:border-trs10-acc2 aria-pressed:bg-trs10-acc/20 aria-pressed:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-trs10-acc2">24 mo</button>
      <button type="button" data-term="36" aria-pressed="false" class="flex-1 min-h-11 rounded-xl border border-trs10-edge text-xs font-semibold text-trs10-mut transition-colors duration-150 hover:text-trs10-ink aria-pressed:border-trs10-acc2 aria-pressed:bg-trs10-acc/20 aria-pressed:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-trs10-acc2">36 mo</button>
      <button type="button" data-term="60" aria-pressed="true" class="flex-1 min-h-11 rounded-xl border border-trs10-edge text-xs font-semibold text-trs10-mut transition-colors duration-150 hover:text-trs10-ink aria-pressed:border-trs10-acc2 aria-pressed:bg-trs10-acc/20 aria-pressed:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-trs10-acc2">60 mo</button>
    </div>

    <div class="grid grid-cols-3 mt-6 pt-5 border-t border-trs10-edge text-center">
      <div>
        <div class="text-[11px] tracking-wide text-trs10-mut">Monthly</div>
        <div class="text-base font-bold text-trs10-ink tabular-nums mt-1" id="trs-10-mo">$298</div>
      </div>
      <div class="border-x border-trs10-edge">
        <div class="text-[11px] tracking-wide text-trs10-mut">Rate APR</div>
        <div class="text-base font-bold text-trs10-ink tabular-nums mt-1">6.9%</div>
      </div>
      <div>
        <div class="text-[11px] tracking-wide text-trs10-mut">Total interest</div>
        <div class="text-base font-bold text-trs10-ink tabular-nums mt-1" id="trs-10-int">$2,880</div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-trs10-bg: #1e1b4b;
  --color-trs10-bg: oklch(0.26 0.1 285);
  --color-trs10-card: #2b2760;
  --color-trs10-card: oklch(0.31 0.1 285);
  --color-trs10-edge: #433d84;
  --color-trs10-edge: oklch(0.4 0.1 285);
  --color-trs10-acc: #7c3aed;
  --color-trs10-acc: oklch(0.54 0.25 295);
  --color-trs10-acc2: #a78bfa;
  --color-trs10-acc2: oklch(0.75 0.14 295);
  --color-trs10-ink: #ede9fe;
  --color-trs10-ink: oklch(0.94 0.03 290);
  --color-trs10-mut: #a99fe0;
  --color-trs10-mut: oklch(0.73 0.08 290);
  --font-trs10-sans: 'Outfit', system-ui, sans-serif;
  --font-trs10-mono: 'JetBrains Mono', ui-monospace, monospace;
}

@property --v {
  syntax: "<number>";
  inherits: true;
  initial-value: 0.286;
}

.trs-10 {
  width: 100%;
  min-height: 100svh;
}

.trs-10 input[type="range"]::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 24px;
  height: 24px;
  border-radius: 9999px;
  background: #fff;
  border: 3px solid var(--color-trs10-acc);
  box-shadow: 0 0 14px -2px var(--color-trs10-acc);
  cursor: grab;
  transition: transform .15s;
}

.trs-10 input[type="range"]:active::-webkit-slider-thumb {
  transform: scale(1.15);
  cursor: grabbing;
}

.trs-10 input[type="range"]::-moz-range-thumb {
  width: 24px;
  height: 24px;
  border-radius: 9999px;
  background: #fff;
  border: 3px solid var(--color-trs10-acc);
  cursor: grab;
}

@media (prefers-reduced-motion: reduce) {
  .trs-10 input[type="range"]::-webkit-slider-thumb {
    transition: none;
  }

  .trs-10 input[type="range"]:active::-webkit-slider-thumb {
    transform: none;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.getElementById('trs-10-root');
  var inp = document.getElementById('trs-10-inp');
  var tip = document.getElementById('trs-10-tip');
  var amount = document.getElementById('trs-10-amount');
  var mo = document.getElementById('trs-10-mo');
  var interest = document.getElementById('trs-10-int');
  var APR = 0.069;
  var term = 60;

  function money(n){ return '$' + Math.round(n).toLocaleString('en-US'); }
  function short(n){ return n >= 1000 ? '$' + Math.round(n / 1000) + 'K' : '$' + n; }

  function update(){
    var v = +inp.value;
    root.style.setProperty('--v', (v - +inp.min) / (+inp.max - +inp.min));
    tip.textContent = short(v);
    amount.textContent = v.toLocaleString('en-US');
    var r = APR / 12;
    var m = v * r * Math.pow(1 + r, term) / (Math.pow(1 + r, term) - 1);
    mo.textContent = money(m);
    interest.textContent = money(m * term - v);
    inp.setAttribute('aria-valuetext', money(v) + ', ' + money(m) + ' per month over ' + term + ' months');
  }

  document.querySelectorAll('#trs-10-terms button').forEach(function(btn){
    btn.addEventListener('click', function(){
      document.querySelectorAll('#trs-10-terms button').forEach(function(b){ b.setAttribute('aria-pressed', 'false'); });
      btn.setAttribute('aria-pressed', 'true');
      term = +btn.dataset.term;
      update();
    });
  });
  inp.addEventListener('input', update);
  update();
})();
```
