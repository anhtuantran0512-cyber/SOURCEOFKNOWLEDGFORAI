---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-pricing-tables/tailwind-bundle-pricing-calculator-checkboxes/"
title: "Tailwind Bundle Pricing Calculator with Checkboxes"
section: "components"
category: "tailwind-css-pricing-tables"
category_name: "Tailwind CSS Pricing Tables"
description: "A build-your-own-bundle calculator: tick add-ons on and off and the order summary re-tallies live — line items unfold, the total pops, and a 10% bundle…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Bundle Pricing Calculator with Checkboxes
Source: https://codefronts.com/components/tailwind-css-pricing-tables/tailwind-bundle-pricing-calculator-checkboxes/

A build-your-own-bundle calculator: tick add-ons on and off and the order summary re-tallies live — line items unfold, the total pops, and a 10% bundle discount unlocks at three add-ons. Rows are styled by has-checked:; summary lines fold with grid-rows-[0fr] &rarr; data-on:grid-rows-[1fr]; and a savings nudge tells the buyer exactly how close the discount is.
## HTML
```html
<section class="tpt-14 w-full min-h-svh grid place-items-center bg-tpt14-bg px-5 py-16 font-tpt14-sans text-tpt14-ink antialiased" aria-label="Build your bundle pricing calculator" data-tpt14-root>
  <div class="grid w-full max-w-4xl gap-7 md:grid-cols-[1.2fr_0.9fr]">
    <div>
      <h2 class="text-[clamp(26px,3.6vw,36px)] font-extrabold tracking-[-0.03em]">Build your bundle</h2>
      <p class="mt-2 mb-6 text-sm text-tpt14-mut">Base platform $29/mo · add what you need · 3+ add-ons save 10%</p>
      <ul class="grid gap-2.5">
        <li><label class="group/row flex min-h-14 cursor-pointer items-center gap-3.5 rounded-2xl border-[1.5px] border-tpt14-line bg-white px-4.5 text-[15px] font-semibold transition-[border-color,background-color,scale] duration-250 hover:border-tpt14-acc/50 active:scale-[.985] has-checked:border-tpt14-acc has-checked:bg-tpt14-acc/6 has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-tpt14-acc"><input type="checkbox" class="sr-only" id="tpt14-a" data-price="12"><span aria-hidden="true" class="grid size-5 flex-none place-items-center rounded-md border-2 border-tpt14-box text-transparent transition-colors group-has-checked/row:border-tpt14-acc group-has-checked/row:bg-tpt14-acc group-has-checked/row:text-white"><svg class="size-3" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 6.5 4.8 9 10 3.5"/></svg></span><span class="flex-1">Analytics <span class="block text-xs font-normal text-tpt14-mut">Dashboards &amp; funnels</span></span><b class="font-semibold text-tpt14-mut tabular-nums">$12</b></label></li>
        <li><label class="group/row flex min-h-14 cursor-pointer items-center gap-3.5 rounded-2xl border-[1.5px] border-tpt14-line bg-white px-4.5 text-[15px] font-semibold transition-[border-color,background-color,scale] duration-250 hover:border-tpt14-acc/50 active:scale-[.985] has-checked:border-tpt14-acc has-checked:bg-tpt14-acc/6 has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-tpt14-acc"><input type="checkbox" class="sr-only" id="tpt14-b" data-price="9"><span aria-hidden="true" class="grid size-5 flex-none place-items-center rounded-md border-2 border-tpt14-box text-transparent transition-colors group-has-checked/row:border-tpt14-acc group-has-checked/row:bg-tpt14-acc group-has-checked/row:text-white"><svg class="size-3" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 6.5 4.8 9 10 3.5"/></svg></span><span class="flex-1">Automations <span class="block text-xs font-normal text-tpt14-mut">Triggers &amp; workflows</span></span><b class="font-semibold text-tpt14-mut tabular-nums">$9</b></label></li>
        <li><label class="group/row flex min-h-14 cursor-pointer items-center gap-3.5 rounded-2xl border-[1.5px] border-tpt14-line bg-white px-4.5 text-[15px] font-semibold transition-[border-color,background-color,scale] duration-250 hover:border-tpt14-acc/50 active:scale-[.985] has-checked:border-tpt14-acc has-checked:bg-tpt14-acc/6 has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-tpt14-acc"><input type="checkbox" class="sr-only" id="tpt14-c" data-price="15"><span aria-hidden="true" class="grid size-5 flex-none place-items-center rounded-md border-2 border-tpt14-box text-transparent transition-colors group-has-checked/row:border-tpt14-acc group-has-checked/row:bg-tpt14-acc group-has-checked/row:text-white"><svg class="size-3" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 6.5 4.8 9 10 3.5"/></svg></span><span class="flex-1">AI Assist <span class="block text-xs font-normal text-tpt14-mut">Drafts, summaries, replies</span></span><b class="font-semibold text-tpt14-mut tabular-nums">$15</b></label></li>
        <li><label class="group/row flex min-h-14 cursor-pointer items-center gap-3.5 rounded-2xl border-[1.5px] border-tpt14-line bg-white px-4.5 text-[15px] font-semibold transition-[border-color,background-color,scale] duration-250 hover:border-tpt14-acc/50 active:scale-[.985] has-checked:border-tpt14-acc has-checked:bg-tpt14-acc/6 has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-tpt14-acc"><input type="checkbox" class="sr-only" id="tpt14-d" data-price="7"><span aria-hidden="true" class="grid size-5 flex-none place-items-center rounded-md border-2 border-tpt14-box text-transparent transition-colors group-has-checked/row:border-tpt14-acc group-has-checked/row:bg-tpt14-acc group-has-checked/row:text-white"><svg class="size-3" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 6.5 4.8 9 10 3.5"/></svg></span><span class="flex-1">Forms <span class="block text-xs font-normal text-tpt14-mut">Surveys &amp; signups</span></span><b class="font-semibold text-tpt14-mut tabular-nums">$7</b></label></li>
        <li><label class="group/row flex min-h-14 cursor-pointer items-center gap-3.5 rounded-2xl border-[1.5px] border-tpt14-line bg-white px-4.5 text-[15px] font-semibold transition-[border-color,background-color,scale] duration-250 hover:border-tpt14-acc/50 active:scale-[.985] has-checked:border-tpt14-acc has-checked:bg-tpt14-acc/6 has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-tpt14-acc"><input type="checkbox" class="sr-only" id="tpt14-e" data-price="19"><span aria-hidden="true" class="grid size-5 flex-none place-items-center rounded-md border-2 border-tpt14-box text-transparent transition-colors group-has-checked/row:border-tpt14-acc group-has-checked/row:bg-tpt14-acc group-has-checked/row:text-white"><svg class="size-3" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 6.5 4.8 9 10 3.5"/></svg></span><span class="flex-1">White-label <span class="block text-xs font-normal text-tpt14-mut">Your domain, your brand</span></span><b class="font-semibold text-tpt14-mut tabular-nums">$19</b></label></li>
      </ul>
    </div>
    <aside class="flex h-max flex-col gap-4 rounded-3xl bg-tpt14-ink p-7 text-tpt14-on-ink md:sticky md:top-6" aria-label="Order summary">
      <h3 class="text-[13px] font-bold tracking-[0.08em] text-tpt14-sum-mut uppercase">Your plan</h3>
      <ul class="grid text-sm">
        <li class="flex justify-between py-1"><span>Platform</span><b class="font-semibold tabular-nums">$29</b></li>
        <li data-for="tpt14-a" class="grid grid-rows-[0fr] -translate-x-1.5 opacity-0 transition-[grid-template-rows,opacity,translate] duration-300 data-on:translate-x-0 data-on:grid-rows-[1fr] data-on:opacity-100 motion-reduce:transition-none"><span class="flex min-h-0 justify-between overflow-hidden"><span class="py-1">Analytics</span><b class="py-1 font-semibold tabular-nums">$12</b></span></li>
        <li data-for="tpt14-b" class="grid grid-rows-[0fr] -translate-x-1.5 opacity-0 transition-[grid-template-rows,opacity,translate] duration-300 data-on:translate-x-0 data-on:grid-rows-[1fr] data-on:opacity-100 motion-reduce:transition-none"><span class="flex min-h-0 justify-between overflow-hidden"><span class="py-1">Automations</span><b class="py-1 font-semibold tabular-nums">$9</b></span></li>
        <li data-for="tpt14-c" class="grid grid-rows-[0fr] -translate-x-1.5 opacity-0 transition-[grid-template-rows,opacity,translate] duration-300 data-on:translate-x-0 data-on:grid-rows-[1fr] data-on:opacity-100 motion-reduce:transition-none"><span class="flex min-h-0 justify-between overflow-hidden"><span class="py-1">AI Assist</span><b class="py-1 font-semibold tabular-nums">$15</b></span></li>
        <li data-for="tpt14-d" class="grid grid-rows-[0fr] -translate-x-1.5 opacity-0 transition-[grid-template-rows,opacity,translate] duration-300 data-on:translate-x-0 data-on:grid-rows-[1fr] data-on:opacity-100 motion-reduce:transition-none"><span class="flex min-h-0 justify-between overflow-hidden"><span class="py-1">Forms</span><b class="py-1 font-semibold tabular-nums">$7</b></span></li>
        <li data-for="tpt14-e" class="grid grid-rows-[0fr] -translate-x-1.5 opacity-0 transition-[grid-template-rows,opacity,translate] duration-300 data-on:translate-x-0 data-on:grid-rows-[1fr] data-on:opacity-100 motion-reduce:transition-none"><span class="flex min-h-0 justify-between overflow-hidden"><span class="py-1">White-label</span><b class="py-1 font-semibold tabular-nums">$19</b></span></li>
        <li data-disc class="grid grid-rows-[0fr] opacity-0 transition-[grid-template-rows,opacity] duration-300 data-on:grid-rows-[1fr] data-on:opacity-100 motion-reduce:transition-none"><span class="flex min-h-0 justify-between overflow-hidden text-tpt14-ok"><span class="py-1">Bundle −10%</span><b data-disc-amt class="py-1 font-semibold tabular-nums">−$0</b></span></li>
      </ul>
      <p data-nudge class="rounded-xl bg-white/6 px-3.5 py-2.5 text-[13px] text-tpt14-sum-mut">Add 3 add-ons to save 10%</p>
      <p class="flex items-baseline gap-2 border-t border-white/12 pt-4 text-sm font-semibold" aria-live="polite"><span>Total</span><output data-total class="ml-auto inline-block text-[34px] font-extrabold tracking-[-0.03em] tabular-nums data-pop:animate-tpt14-pop motion-reduce:data-pop:animate-none">$29</output><small class="text-tpt14-sum-mut">/mo</small></p>
      <a href="#" class="grid min-h-12 place-items-center rounded-xl bg-tpt14-acc text-sm font-bold text-white no-underline transition hover:brightness-110 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt14-on-ink">Start with this bundle</a>
    </aside>
    <p aria-hidden="true" class="justify-self-center rounded-full border border-tpt14-line bg-white px-3.5 py-2 font-tpt14-mono text-[11.5px] text-tpt14-mut md:col-span-2">has-checked: · data-on:grid-rows-[1fr] · data-pop:animate-tpt14-pop</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpt14-bg: #fbf7f4;
  --color-tpt14-bg: oklch(0.975 0.007 55);
  --color-tpt14-ink: #241a15;
  --color-tpt14-ink: oklch(0.23 0.02 45);
  --color-tpt14-on-ink: #f5ede7;
  --color-tpt14-on-ink: oklch(0.95 0.012 55);
  --color-tpt14-sum-mut: #c2b2a5;
  --color-tpt14-sum-mut: oklch(0.77 0.025 55);
  --color-tpt14-mut: #6f6258;
  --color-tpt14-mut: oklch(0.5 0.02 55);
  --color-tpt14-line: #eadfd7;
  --color-tpt14-line: oklch(0.91 0.015 55);
  --color-tpt14-box: #cdbdb1;
  --color-tpt14-box: oklch(0.8 0.02 55);
  --color-tpt14-acc: #e04a25;
  --color-tpt14-acc: oklch(0.6 0.2 35);
  --color-tpt14-ok: #86d89a;
  --color-tpt14-ok: oklch(0.82 0.12 150);
  --font-tpt14-sans: 'Bricolage Grotesque', system-ui, sans-serif;
  --font-tpt14-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tpt14-pop: tpt14-pop 0.35s cubic-bezier(0.3, 1.6, 0.4, 1);

  @keyframes tpt14-pop {
    40% {
      scale: 1.14;
      color: oklch(0.8 0.15 40);
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities. */

.tpt-14 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('[data-tpt14-root]').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    const boxes = [...root.querySelectorAll('input[type="checkbox"]')];
    const total = root.querySelector('[data-total]');
    const disc = root.querySelector('[data-disc]');
    const discAmt = root.querySelector('[data-disc-amt]');
    const nudge = root.querySelector('[data-nudge]');
    const BASE = 29, DISC_AT = 3, DISC_PCT = 0.1;
    const update = () => {
      const picked = boxes.filter((b) => b.checked);
      boxes.forEach((b) => root.querySelector('[data-for="' + b.id + '"]').toggleAttribute('data-on', b.checked));
      const sum = BASE + picked.reduce((s, b) => s + +b.dataset.price, 0);
      const hasDisc = picked.length >= DISC_AT;
      const off = hasDisc ? Math.round(sum * DISC_PCT) : 0;
      const left = DISC_AT - picked.length;
      disc.toggleAttribute('data-on', hasDisc);
      discAmt.textContent = '−$' + off;
      nudge.hidden = hasDisc;
      nudge.textContent = 'Add ' + left + ' more add-on' + (left === 1 ? '' : 's') + ' to save 10%';
      total.textContent = '$' + (sum - off);
      total.removeAttribute('data-pop');
      requestAnimationFrame(() => requestAnimationFrame(() => total.setAttribute('data-pop', '')));
    };
    boxes.forEach((b) => b.addEventListener('change', update));
  });
})();
```
