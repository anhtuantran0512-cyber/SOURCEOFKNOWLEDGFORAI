---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-pricing-sections/tailwind-per-seat-pricing-calculator/"
title: "Tailwind Per-Seat Pricing Calculator"
section: "layouts"
category: "tailwind-css-pricing-sections"
category_name: "Tailwind CSS Pricing Sections"
description: "Real interactive math: native +/&minus; buttons and a number field drive a live per-seat &times; seats &times; cycle total."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Per-Seat Pricing Calculator
Source: https://codefronts.com/layouts/tailwind-css-pricing-sections/tailwind-per-seat-pricing-calculator/

Real interactive math: native +/&minus; buttons and a number field drive a live per-seat &times; seats &times; cycle total. The port moves every visual state into the class list &mdash; the checked cycle label via peer-checked:, the clamped-out buttons via disabled: &mdash; leaving the JS to do arithmetic and nothing else.
## HTML
```html
<section class="tps-11 w-full min-h-svh bg-tps11-bg bg-[radial-gradient(60%_80%_at_80%_0%,--alpha(--color-tps11-indigo/18),transparent_60%),radial-gradient(60%_80%_at_0%_100%,--alpha(--color-tps11-sky/14),transparent_60%)] font-tps11-sans text-tps11-body px-[clamp(20px,4vw,40px)] py-[clamp(28px,5vw,56px)]" aria-label="Per-seat calculator">
  <header class="text-center mb-[clamp(24px,4vw,36px)]">
    <span class="inline-block mb-3.5 px-3 py-1.25 rounded-full bg-tps11-indigo/12 border border-tps11-indigo/28 text-[11px] font-bold uppercase tracking-[0.18em] text-tps11-indigo">Build your plan</span>
    <h2 class="m-0 mb-2 text-[clamp(22px,3.4vw,32px)] font-bold tracking-[-0.02em] text-white">Per-seat pricing, calculated live.</h2>
    <p class="m-0 text-sm text-tps11-muted">One number to change. Everything else updates with you.</p>
  </header>
  <div class="grid grid-cols-1 md:grid-cols-[1.1fr_1fr] max-w-[820px] mx-auto rounded-[18px] overflow-hidden bg-tps11-card/70 border border-tps11-indigo/20 backdrop-blur-[8px] shadow-[0_24px_60px_rgba(0,0,0,0.35)]">
    <div class="flex flex-col gap-[22px] p-[clamp(22px,4vw,32px)] border-b md:border-b-0 md:border-r border-tps11-indigo/15">
      <fieldset class="m-0 p-1 grid grid-cols-2 rounded-[10px] border border-tps11-indigo/20 bg-tps11-bg/40">
        <legend class="sr-only">Billing cycle</legend>
        <input type="radio" name="tps-11__cycle" id="tps-11__m" class="peer/m sr-only" checked>
        <label for="tps-11__m" class="col-start-1 row-start-1 text-center px-3 py-2.25 rounded-[7px] text-[12.5px] font-semibold text-tps11-muted cursor-pointer transition-[background-color,color] duration-[180ms] peer-checked/m:bg-linear-135 peer-checked/m:from-tps11-indigo peer-checked/m:to-tps11-sky peer-checked/m:text-white peer-focus-visible/m:outline-2 peer-focus-visible/m:outline-tps11-indigo peer-focus-visible/m:outline-offset-2 motion-reduce:transition-none">Monthly</label>
        <input type="radio" name="tps-11__cycle" id="tps-11__y" class="peer/y sr-only">
        <label for="tps-11__y" class="col-start-2 row-start-1 text-center px-3 py-2.25 rounded-[7px] text-[12.5px] font-semibold text-tps11-muted cursor-pointer transition-[background-color,color] duration-[180ms] peer-checked/y:bg-linear-135 peer-checked/y:from-tps11-indigo peer-checked/y:to-tps11-sky peer-checked/y:text-white peer-focus-visible/y:outline-2 peer-focus-visible/y:outline-tps11-indigo peer-focus-visible/y:outline-offset-2 motion-reduce:transition-none">Yearly &middot; save 25%</label>
      </fieldset>
      <div>
        <span class="block mb-2 text-[11px] uppercase tracking-[0.16em] text-tps11-muted">Team size</span>
        <div class="grid grid-cols-[44px_1fr_44px] rounded-[10px] overflow-hidden border border-tps11-indigo/25 bg-tps11-bg/50">
          <button type="button" id="tps-11__dec" aria-label="Decrease team size" class="size-11 bg-transparent border-0 cursor-pointer font-[inherit] text-[22px] font-bold text-tps11-indigo transition-[background-color,color] duration-150 hover:bg-tps11-indigo/15 hover:text-white focus-visible:outline-2 focus-visible:outline-tps11-indigo focus-visible:-outline-offset-2 disabled:opacity-40 disabled:cursor-not-allowed disabled:hover:bg-transparent disabled:hover:text-tps11-indigo motion-reduce:transition-none">&minus;</button>
          <input type="number" id="tps-11__seats" value="5" min="1" max="500" inputmode="numeric" pattern="[0-9]*" aria-label="Number of team members" class="appearance-none [&amp;::-webkit-outer-spin-button]:appearance-none [&amp;::-webkit-inner-spin-button]:appearance-none [&amp;::-webkit-inner-spin-button]:m-0 bg-transparent border-0 border-x border-tps11-indigo/18 outline-0 text-center font-[inherit] text-[22px] font-bold tracking-[-0.01em] text-white focus-visible:bg-tps11-indigo/12">
          <button type="button" id="tps-11__inc" aria-label="Increase team size" class="size-11 bg-transparent border-0 cursor-pointer font-[inherit] text-[22px] font-bold text-tps11-indigo transition-[background-color,color] duration-150 hover:bg-tps11-indigo/15 hover:text-white focus-visible:outline-2 focus-visible:outline-tps11-indigo focus-visible:-outline-offset-2 disabled:opacity-40 disabled:cursor-not-allowed disabled:hover:bg-transparent disabled:hover:text-tps11-indigo motion-reduce:transition-none">+</button>
        </div>
        <span class="block mt-2 text-[11.5px] text-tps11-dim">Up to 500 seats. Above that, we&rsquo;ll talk.</span>
      </div>
    </div>
    <div class="flex flex-col p-[clamp(22px,4vw,32px)] bg-linear-180 from-tps11-indigo/10 to-tps11-sky/6" aria-live="polite">
      <div class="flex justify-between items-baseline py-2.5 text-[13.5px]"><span class="text-tps11-muted">Seats</span><strong id="tps-11__out-seats" class="font-semibold text-white">5 members</strong></div>
      <div class="flex justify-between items-baseline py-2.5 text-[13.5px]"><span class="text-tps11-muted">Per seat</span><strong id="tps-11__out-per" class="font-semibold text-white">$12.00 / mo</strong></div>
      <div class="flex justify-between items-baseline py-2.5 text-[13.5px]"><span class="text-tps11-muted">Cycle</span><strong id="tps-11__out-cyc" class="font-semibold text-white">Monthly</strong></div>
      <hr class="border-0 border-t border-dashed border-tps11-indigo/25 my-1">
      <div class="flex justify-between items-baseline py-2.5">
        <span class="text-[13px] uppercase tracking-[0.04em] text-tps11-label">Total today</span>
        <strong id="tps-11__out-total" class="text-[clamp(28px,4vw,38px)] font-extrabold tracking-[-0.02em] bg-linear-90 from-tps11-indigo to-tps11-sky bg-clip-text text-transparent">$60.00</strong>
      </div>
      <p id="tps-11__out-foot" class="mt-1 mb-4 text-xs text-tps11-dim">Billed monthly &middot; cancel any time</p>
      <a href="#start" class="block mt-auto text-center px-4.5 py-3 rounded-[10px] bg-linear-135 from-tps11-indigo to-tps11-sky text-white no-underline text-sm font-bold shadow-[0_10px_24px_--alpha(--color-tps11-indigo/30)] transition-[translate] duration-[180ms] hover:-translate-y-px focus-visible:outline-2 focus-visible:outline-tps11-indigo focus-visible:outline-offset-[3px] motion-reduce:transition-none motion-reduce:hover:translate-y-0">Start 14-day trial &rarr;</a>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tps11-bg: #07091a;
  --color-tps11-bg: oklch(0.13 0.04 267);
  --color-tps11-card: #141630;
  --color-tps11-card: oklch(0.22 0.05 277);
  --color-tps11-body: #e6e9ff;
  --color-tps11-body: oklch(0.92 0.03 280);
  --color-tps11-muted: #9aa3c8;
  --color-tps11-muted: oklch(0.7 0.05 277);
  --color-tps11-dim: #8b93b8;
  --color-tps11-dim: oklch(0.64 0.05 277);
  --color-tps11-label: #93c5fd;
  --color-tps11-label: oklch(0.81 0.1 250);
  --color-tps11-indigo: #818cf8;
  --color-tps11-indigo: oklch(0.68 0.16 277);
  --color-tps11-sky: #38bdf8;
  --color-tps11-sky: oklch(0.75 0.14 231);
  --font-tps11-sans: 'Manrope', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the section is sized correctly in the moment before the
   browser build has compiled its utilities. */

.tps-11 {
  width: 100%;
  min-height: 100svh;
}
/* Firefox's number-input spinner has no pseudo-element to target, so the
   -moz-appearance hint stays a real declaration. Chromium's two spin buttons
   ARE reachable, and are handled by arbitrary variants in the markup. */

.tps-11 input[type="number"] {
  -moz-appearance: textfield;
}
```

## JavaScript
```js
(function () {
  var seats    = document.getElementById('tps-11__seats');
  var dec      = document.getElementById('tps-11__dec');
  var inc      = document.getElementById('tps-11__inc');
  var rY       = document.getElementById('tps-11__y');
  var outSeats = document.getElementById('tps-11__out-seats');
  var outPer   = document.getElementById('tps-11__out-per');
  var outCyc   = document.getElementById('tps-11__out-cyc');
  var outTot   = document.getElementById('tps-11__out-total');
  var outFoot  = document.getElementById('tps-11__out-foot');
  if (!seats || !inc) return;

  var BASE_MONTHLY = 12;    // $12 / seat / mo
  var YEARLY_DISC  = 0.25;  // 25% off when billed yearly

  function clamp(v) {
    if (isNaN(v) || v < 1) return 1;
    return v > 500 ? 500 : v;
  }
  function fmt(n) { return '
export const slugify = ( /** @type {string} */ name) =>
    name.toLowerCase().replace(/&/g, 'and').replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '');

export const items = _raw.map((t) => ({ ...t, slug: t.slug || slugify(t.name) }));

export const itemsBySlug = Object.fromEntries(items.map(i => [i.slug, i]));

export default items;
 + n.toFixed(2); }

  // The script sets values and the two disabled flags. It adds no classes:
  // every visual state is a variant reading a native control's own state.
  function update() {
    var n      = clamp(parseInt(seats.value, 10));
    seats.value = n;
    var yearly = rY.checked;
    var per    = yearly ? BASE_MONTHLY * (1 - YEARLY_DISC) : BASE_MONTHLY;
    var total  = per * n * (yearly ? 12 : 1);

    outSeats.textContent = n + (n === 1 ? ' member' : ' members');
    outPer.textContent   = fmt(per) + ' / mo';
    outCyc.textContent   = yearly ? 'Yearly (\u201325%)' : 'Monthly';
    outTot.textContent   = fmt(total);
    outFoot.textContent  = yearly
      ? 'Billed yearly \u00b7 ' + fmt(total) + ' once, then renews annually'
      : 'Billed monthly \u00b7 cancel any time';

    dec.disabled = n <= 1;
    inc.disabled = n >= 500;
  }

  dec.addEventListener('click', function () { seats.value = clamp(parseInt(seats.value, 10) - 1); update(); });
  inc.addEventListener('click', function () { seats.value = clamp(parseInt(seats.value, 10) + 1); update(); });
  seats.addEventListener('input', update);
  document.getElementById('tps-11__m').addEventListener('change', update);
  rY.addEventListener('change', update);
  update();
})();
```
