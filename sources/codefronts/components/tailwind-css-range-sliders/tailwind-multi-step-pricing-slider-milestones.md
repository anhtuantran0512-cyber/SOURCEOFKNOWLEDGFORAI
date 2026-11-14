---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-range-sliders/tailwind-multi-step-pricing-slider-milestones/"
title: "Tailwind CSS Multi-Step Pricing Slider with Snapping Milestones"
section: "components"
category: "tailwind-css-range-sliders"
category_name: "Tailwind CSS Range Sliders"
description: "Four plans, one snapping track, and a progress line that springs into place."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Multi-Step Pricing Slider with Snapping Milestones
Source: https://codefronts.com/components/tailwind-css-range-sliders/tailwind-multi-step-pricing-slider-milestones/

Four plans, one snapping track, and a progress line that springs into place. The port's honest upgrade is that the step dots are now real buttons — the CSS version drew them as decorations and left tapping "between steps" to chance; here every dot is a 44px control, and the slider remains for keyboard and drag.
## HTML
```html
<section class="trs-05 w-full min-h-svh grid place-items-center bg-trs05-bg font-trs05-sans px-5 py-10" id="trs-05-root" style="--step:0">
  <div class="w-[min(520px,100%)] rounded-3xl bg-white p-9 shadow-[0_18px_50px_-24px_oklch(0.4_0.06_260/0.45),0_1px_3px_oklch(0.4_0.06_260/0.08)]">
    <div class="flex items-center justify-between gap-4 mb-5">
      <span class="inline-flex items-center gap-2 rounded-full bg-trs05-tint border border-trs05-edge text-trs05-acc text-[11px] font-bold uppercase tracking-[0.1em] px-3 py-1.5"><span class="size-1.5 rounded-full bg-trs05-ok"></span>Pricing plan</span>
      <div class="flex rounded-xl bg-trs05-tint p-0.5" role="group" aria-label="Billing period">
        <button type="button" id="trs-05-monthly" aria-pressed="true" class="min-h-9 rounded-[10px] px-3 text-xs font-semibold text-trs05-mut transition-colors duration-150 aria-pressed:bg-white aria-pressed:text-trs05-acc aria-pressed:shadow-sm focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-trs05-acc">Monthly</button>
        <button type="button" id="trs-05-annual" aria-pressed="false" class="min-h-9 rounded-[10px] px-3 text-xs font-semibold text-trs05-mut transition-colors duration-150 aria-pressed:bg-white aria-pressed:text-trs05-acc aria-pressed:shadow-sm focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-trs05-acc">Annual <span class="text-trs05-ok">−17%</span></button>
      </div>
    </div>

    <h3 class="text-[22px] font-extrabold tracking-tight text-trs05-ink m-0">Choose your plan</h3>
    <p class="text-sm text-trs05-mut mt-1.5 mb-9 m-0">Drag the slider, or pick a step</p>

    <div class="relative mb-4">
      <div class="absolute top-4 inset-x-4 h-1 rounded-full bg-trs05-track overflow-hidden">
        <div class="h-full rounded-full bg-gradient-to-r from-trs05-acc to-trs05-acc2 w-[calc(var(--step)/3*100%)]"></div>
      </div>
      <div class="relative z-10 flex justify-between" id="trs-05-steps"></div>
    </div>

    <input type="range" min="0" max="3" step="1" value="0" id="trs-05-inp" aria-label="Plan tier"
           class="block w-full h-1 appearance-none bg-transparent outline-none cursor-pointer mb-8 focus-visible:outline-2 focus-visible:outline-offset-8 focus-visible:outline-trs05-acc rounded-full">

    <div class="relative rounded-2xl bg-trs05-tint border border-trs05-edge p-5" aria-live="polite">
      <span class="absolute -top-2.5 right-5 hidden rounded-full bg-trs05-acc px-2.5 py-0.5 text-[10px] font-bold uppercase tracking-wider text-white data-[show=true]:inline-block" id="trs-05-ribbon" data-show="false">Most popular</span>
      <div class="text-base font-extrabold text-trs05-navy" id="trs-05-name">Free</div>
      <div class="flex items-baseline gap-1 mt-1">
        <span class="text-[32px] font-black text-trs05-acc tabular-nums" id="trs-05-price">$0</span>
        <span class="text-sm font-medium text-trs05-mut" id="trs-05-period">/month</span>
      </div>
      <p class="text-[13px] text-trs05-ink/70 mt-2 m-0" id="trs-05-perks">Up to 3 projects · 1 GB storage · Community support</p>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-trs05-bg: #f6f8fc;
  --color-trs05-bg: oklch(0.97 0.008 255);
  --color-trs05-tint: #eff5ff;
  --color-trs05-tint: oklch(0.96 0.02 255);
  --color-trs05-edge: #c9dcfb;
  --color-trs05-edge: oklch(0.87 0.05 255);
  --color-trs05-track: #dfe6f1;
  --color-trs05-track: oklch(0.91 0.015 255);
  --color-trs05-acc: #1d4ed8;
  --color-trs05-acc: oklch(0.48 0.22 264);
  --color-trs05-acc2: #3b82f6;
  --color-trs05-acc2: oklch(0.62 0.19 259);
  --color-trs05-navy: #1e3a8a;
  --color-trs05-navy: oklch(0.36 0.16 264);
  --color-trs05-ok: #0f9e6e;
  --color-trs05-ok: oklch(0.6 0.14 164);
  --color-trs05-ink: #0f172a;
  --color-trs05-ink: oklch(0.22 0.03 262);
  --color-trs05-mut: #64748b;
  --color-trs05-mut: oklch(0.55 0.03 255);
  --font-trs05-sans: 'Sora', system-ui, sans-serif;
}

@property --step {
  syntax: "<number>";
  inherits: true;
  initial-value: 0;
}
/* Transition the REGISTERED PROPERTY, not the width that reads it: a property
   whose computed value comes from a var() keeps its first-paint value when it
   carries its own transition, because the declared calc() token stream never
   changes. Animating --step re-evaluates every dependent utility per frame. */

.trs-05 {
  width: 100%;
  min-height: 100svh;
  transition: --step .4s cubic-bezier(0.34, 1.56, 0.64, 1);
}

@media (prefers-reduced-motion: reduce) {
  .trs-05 {
    transition: none;
  }
}
/* The step dots are the visible thumb, so the native one is a transparent
   hit target — hidden, but never removed from the tab order. */

.trs-05 input[type="range"]::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 28px;
  height: 28px;
  border-radius: 9999px;
  background: transparent;
  cursor: pointer;
}

.trs-05 input[type="range"]::-moz-range-thumb {
  width: 28px;
  height: 28px;
  border: 0;
  border-radius: 9999px;
  background: transparent;
  cursor: pointer;
}
```

## JavaScript
```js
(function(){
  var root = document.getElementById('trs-05-root');
  var inp = document.getElementById('trs-05-inp');
  var stepsEl = document.getElementById('trs-05-steps');
  var ribbon = document.getElementById('trs-05-ribbon');
  var monthlyBtn = document.getElementById('trs-05-monthly');
  var annualBtn = document.getElementById('trs-05-annual');
  var PLANS = [
    { name: 'Free', price: 0, perks: 'Up to 3 projects · 1 GB storage · Community support', mark: 'F' },
    { name: 'Starter', price: 12, perks: 'Up to 20 projects · 10 GB storage · Email support', mark: 'S' },
    { name: 'Pro', price: 39, perks: 'Unlimited projects · 100 GB storage · Priority support', mark: 'P', popular: true },
    { name: 'Enterprise', price: 99, perks: 'Everything in Pro · SSO · SLA · Dedicated manager', mark: 'E' }
  ];
  var annual = false;

  PLANS.forEach(function(p, i){
    var b = document.createElement('button');
    b.type = 'button';
    b.dataset.state = 'idle';
    b.className = 'group flex flex-col items-center gap-2 min-h-11 px-1 bg-transparent border-0 cursor-pointer focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-trs05-acc rounded-lg';
    b.innerHTML =
      '<span class="grid place-items-center size-8 rounded-full text-xs font-bold border-[3px] bg-trs05-track border-trs05-track text-trs05-mut transition-[background-color,border-color,color,scale,box-shadow] duration-300 group-data-[state=done]:bg-trs05-ok group-data-[state=done]:border-trs05-ok group-data-[state=done]:text-white group-data-[state=active]:bg-trs05-acc group-data-[state=active]:border-trs05-acc group-data-[state=active]:text-white group-data-[state=active]:scale-115 group-data-[state=active]:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-trs05-acc)_22%,transparent)] motion-reduce:transition-none motion-reduce:group-data-[state=active]:scale-100">' + p.mark + '</span>' +
      '<span class="text-[11px] font-semibold text-trs05-mut whitespace-nowrap transition-colors duration-300 group-data-[state=done]:text-trs05-ink group-data-[state=active]:text-trs05-ink motion-reduce:transition-none">' + p.name + '</span>';
    b.addEventListener('click', function(){ inp.value = i; update(); });
    stepsEl.appendChild(b);
  });
  var dots = Array.prototype.slice.call(stepsEl.children);

  function update(){
    var v = +inp.value, p = PLANS[v];
    root.style.setProperty('--step', v);
    dots.forEach(function(d, i){
      d.dataset.state = i === v ? 'active' : (i < v ? 'done' : 'idle');
      d.setAttribute('aria-pressed', String(i === v));
    });
    var price = annual ? p.price * 10 : p.price;
    document.getElementById('trs-05-name').textContent = p.name;
    document.getElementById('trs-05-price').textContent = '$' + price;
    document.getElementById('trs-05-period').textContent = annual ? '/year' : '/month';
    document.getElementById('trs-05-perks').textContent = p.perks;
    ribbon.dataset.show = p.popular ? 'true' : 'false';
    inp.setAttribute('aria-valuetext', p.name + ', $' + price + (annual ? ' per year' : ' per month'));
  }

  function setPeriod(isAnnual){
    annual = isAnnual;
    monthlyBtn.setAttribute('aria-pressed', String(!annual));
    annualBtn.setAttribute('aria-pressed', String(annual));
    update();
  }
  monthlyBtn.addEventListener('click', function(){ setPeriod(false); });
  annualBtn.addEventListener('click', function(){ setPeriod(true); });
  inp.addEventListener('input', update);
  update();
})();
```
