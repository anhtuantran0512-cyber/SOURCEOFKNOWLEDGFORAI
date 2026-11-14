---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-pricing-sections/tailwind-usage-slider-pricing-estimator/"
title: "Tailwind Usage Slider Pricing Estimator"
section: "layouts"
category: "tailwind-css-pricing-sections"
category_name: "Tailwind CSS Pricing Sections"
description: "Drag the slider and the estimate, the request count and the recommended tier all move &mdash; with aria-valuetext announcing the whole result instead of a…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Usage Slider Pricing Estimator
Source: https://codefronts.com/layouts/tailwind-css-pricing-sections/tailwind-usage-slider-pricing-estimator/

Drag the slider and the estimate, the request count and the recommended tier all move &mdash; with aria-valuetext announcing the whole result instead of a bare number. The port is a clean split: every layout and colour decision becomes a utility, and the four vendor pseudo-elements that paint a range track stay in CSS, where Tailwind has no variant and should not.
## HTML
```html
<section class="tps-05 w-full min-h-svh bg-tps05-bg font-tps05-sans text-tps05-ink px-[clamp(20px,4vw,40px)] py-[clamp(28px,5vw,56px)]" aria-label="Usage-based pricing">
  <header class="text-center mb-[clamp(24px,4vw,36px)]">
    <span class="inline-block mb-3.5 px-3 py-1.25 rounded-full bg-tps05-chip border border-tps05-edge2 text-[11px] font-bold tracking-[0.18em] uppercase text-tps05-acc">Pay-as-you-go</span>
    <h2 class="m-0 mb-2.5 text-[clamp(22px,3.4vw,32px)] font-bold tracking-[-0.02em] text-white text-pretty">Only pay for what you actually send.</h2>
    <p class="mx-auto my-0 max-w-[520px] text-sm/relaxed text-tps05-mut">Slide to estimate your monthly bill &mdash; we round up to the nearest tier so you&rsquo;re never surprised.</p>
  </header>
  <div class="max-w-[580px] mx-auto px-[clamp(20px,4vw,32px)] py-[clamp(24px,4vw,36px)] rounded-[18px] bg-linear-to-b from-tps05-card to-tps05-bg border border-tps05-edge shadow-[0_22px_60px_--theme(--color-tps05-glow)]">
    <div class="text-center pb-5.5 mb-5.5 border-b border-dashed border-tps05-edge">
      <span class="block text-[11px] tracking-[0.16em] uppercase text-tps05-mut" id="tps05-lbl">Estimated monthly cost</span>
      <span class="flex justify-center items-baseline gap-1 mt-2 mb-1.5 text-[64px] font-extrabold tracking-[-0.04em] text-transparent bg-linear-to-b from-tps05-acc to-tps05-acc2 bg-clip-text forced-colors:text-[CanvasText]"><em class="self-start pt-3 text-[28px] not-italic opacity-70">$</em><span id="tps05-price">12</span></span>
      <span class="text-[13px] text-tps05-mut"><span id="tps05-units">10K</span> requests on the <strong class="font-bold text-tps05-acc" id="tps05-tier">Starter</strong> tier</span>
    </div>
    <div class="px-1 pb-5.5">
      <label class="sr-only" for="tps05-range">Monthly request volume</label>
      <input type="range" id="tps05-range" min="0" max="100" step="1" value="10" aria-labelledby="tps05-lbl" aria-valuetext="10K requests, Starter tier, 12 dollars per month" class="tps-05__range w-full h-1.5 mt-2 mb-3 bg-transparent cursor-pointer [appearance:none] focus-visible:outline-none">
      <div class="flex justify-between font-tps05-mono text-[10.5px] text-tps05-dim" aria-hidden="true">
        <span>10K</span><span>100K</span><span>500K</span><span>1M</span><span>5M+</span>
      </div>
    </div>
    <ul class="list-none p-0 m-0 mb-5.5 text-[13px]/[1.9] text-tps05-body">
      <li><span class="inline-block w-5 text-tps05-acc" aria-hidden="true">&#10022;</span>No setup fee, no minimum spend</li>
      <li><span class="inline-block w-5 text-tps05-acc" aria-hidden="true">&#10022;</span>Auto-tier switching at every milestone</li>
      <li><span class="inline-block w-5 text-tps05-acc" aria-hidden="true">&#10022;</span>Usage cap option to prevent surprises</li>
    </ul>
    <a href="#start" class="block text-center px-4.5 py-3.25 rounded-[10px] text-sm font-bold tracking-[0.02em] text-white no-underline bg-linear-[135deg,var(--color-tps05-acc),var(--color-tps05-acc2)] shadow-[0_8px_22px_--theme(--color-tps05-glow2)] transition-transform duration-200 hover:-translate-y-px focus-visible:outline-2 focus-visible:outline-tps05-acc3 focus-visible:outline-offset-3 motion-reduce:transition-none motion-reduce:hover:translate-y-0">Start with this plan &rarr;</a>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tps05-bg: #1a0a18;
  --color-tps05-bg: oklch(0.17 0.04 340);
  --color-tps05-card: #2a1227;
  --color-tps05-card: oklch(0.24 0.06 340);
  --color-tps05-edge: #5a2b4c;
  --color-tps05-edge: oklch(0.38 0.08 345);
  --color-tps05-edge2: #7a3a62;
  --color-tps05-edge2: oklch(0.46 0.1 345);
  --color-tps05-chip: #3a1830;
  --color-tps05-chip: oklch(0.28 0.07 345);
  --color-tps05-ink: #fde7f4;
  --color-tps05-ink: oklch(0.95 0.03 340);
  --color-tps05-body: #d8b8cc;
  --color-tps05-body: oklch(0.83 0.05 340);
  --color-tps05-mut: #c2a0b6;
  --color-tps05-mut: oklch(0.75 0.05 340);
  --color-tps05-dim: #9e7590;
  --color-tps05-dim: oklch(0.62 0.06 340);
  --color-tps05-acc: #f472b6;
  --color-tps05-acc: oklch(0.74 0.18 348);
  --color-tps05-acc2: #be185d;
  --color-tps05-acc2: oklch(0.5 0.19 358);
  --color-tps05-acc3: #f9a8d4;
  --color-tps05-acc3: oklch(0.83 0.11 348);
  --color-tps05-glow: #f472b61f;
  --color-tps05-glow: oklch(0.74 0.18 348 / 0.12);
  --color-tps05-glow2: #be185d59;
  --color-tps05-glow2: oklch(0.5 0.19 358 / 0.35);
  --font-tps05-sans: 'Inter', system-ui, sans-serif;
  --font-tps05-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, plus the four vendor pseudo-elements that
   paint a range input. Tailwind has no variant for ::-webkit-slider-thumb or
   ::-moz-range-progress and should not invent one — this is the boundary of what
   utilities can express, so the track and thumbs stay here and read the same
   @theme tokens as the markup. */

.tps-05 {
  width: 100%;
  min-height: 100svh;
}

.tps-05__range::-webkit-slider-runnable-track {
  height: 6px;
  border-radius: 999px;
  background: linear-gradient(90deg,
      var(--color-tps05-acc) 0%,
      var(--color-tps05-acc) var(--tps05-fill, 10%),
      var(--color-tps05-track) var(--tps05-fill, 10%),
      var(--color-tps05-track) 100%);
}

.tps-05__range::-moz-range-track {
  height: 6px;
  border-radius: 999px;
  background: var(--color-tps05-track);
}

.tps-05__range::-moz-range-progress {
  height: 6px;
  border-radius: 999px;
  background: var(--color-tps05-acc);
}

.tps-05__range::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 22px;
  height: 22px;
  margin-top: -8px;
  border-radius: 50%;
  background: #fff;
  border: 3px solid var(--color-tps05-acc);
  box-shadow: 0 4px 12px var(--color-tps05-glow2);
  cursor: grab;
}

.tps-05__range::-moz-range-thumb {
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background: #fff;
  border: 3px solid var(--color-tps05-acc);
  box-shadow: 0 4px 12px var(--color-tps05-glow2);
  cursor: grab;
}

.tps-05__range:focus-visible::-webkit-slider-thumb {
  outline: 3px solid var(--color-tps05-acc3);
  outline-offset: 2px;
}

.tps-05__range:focus-visible::-moz-range-thumb {
  outline: 3px solid var(--color-tps05-acc3);
  outline-offset: 2px;
}
/* Not an @theme entry on purpose: the unfilled track colour is never wanted as a
   bg-/text-/border- utility. */

.tps-05 {
  --color-tps05-track: oklch(0.28 0.05 340);
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tps-05').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var range = root.querySelector('#tps05-range'),
        priceEl = root.querySelector('#tps05-price'),
        unitsEl = root.querySelector('#tps05-units'),
        tierEl = root.querySelector('#tps05-tier');
    if (!range) return;
    var tiers = [
      { units: 10, price: 12, name: 'Starter' },
      { units: 100, price: 49, name: 'Starter' },
      { units: 500, price: 149, name: 'Growth' },
      { units: 1000, price: 249, name: 'Growth' },
      { units: 5000, price: 749, name: 'Scale' }
    ];
    function fmt(k) { return k >= 1000 ? (k / 1000).toFixed(k % 1000 ? 1 : 0) + 'M' : k.toLocaleString() + 'K'; }
    function update() {
      var v = parseInt(range.value, 10);
      var t = tiers[v < 25 ? 0 : v < 50 ? 1 : v < 75 ? 2 : v < 95 ? 3 : 4];
      priceEl.textContent = t.price.toLocaleString();
      unitsEl.textContent = fmt(t.units);
      tierEl.textContent = t.name;
      range.style.setProperty('--tps05-fill', v + '%');
      range.setAttribute('aria-valuetext', fmt(t.units) + ' requests, ' + t.name + ' tier, ' + t.price + ' dollars per month');
    }
    range.addEventListener('input', update);
    update();
  });
})();
```
