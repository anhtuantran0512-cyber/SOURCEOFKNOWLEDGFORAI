---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-saas-pricing-toggle-monthly-annually-segmented-pill/"
title: "Tailwind SaaS Pricing Toggle — Monthly / Annually Segmented Pill"
section: "components"
category: "tailwind-css-toggles-switches"
category_name: "Tailwind CSS Toggles & Switches"
description: "The billing switcher every pricing page ships: two sr-only radios, a highlight pill that glides behind the active label, a save badge, and a price that…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind SaaS Pricing Toggle — Monthly / Annually Segmented Pill
Source: https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-saas-pricing-toggle-monthly-annually-segmented-pill/

The billing switcher every pricing page ships: two sr-only radios, a highlight pill that glides behind the active label, a save badge, and a price that live-swaps underneath &mdash; all from peer-checked: and one has-checked: on the card. Radios mean arrow-key navigation comes free.
## HTML
```html
<section class="ttg-07 w-full min-h-svh grid place-items-center px-5 py-14 bg-ttg07-bg font-ttg07-sans" aria-label="Pricing period toggle">
  <div class="w-[min(360px,100%)] flex flex-col items-center gap-5 p-7 rounded-[26px] bg-white shadow-[0_30px_60px_-40px_oklch(0.4_0.12_285/0.55)] border border-ttg07-edge has-[.ttg07-y:checked]:[&_.ttg07-pm]:opacity-0 has-[.ttg07-y:checked]:[&_.ttg07-pm]:-translate-y-2 has-[.ttg07-y:checked]:[&_.ttg07-py]:opacity-100 has-[.ttg07-y:checked]:[&_.ttg07-py]:translate-y-0">
    <div role="radiogroup" aria-label="Billing period" class="relative w-full grid grid-cols-2 p-1 rounded-full bg-ttg07-tint">
      <input type="radio" name="ttg-07" id="ttg-07-m" checked class="peer/monthly sr-only">
      <input type="radio" name="ttg-07" id="ttg-07-y" class="ttg07-y peer/yearly sr-only">
      <span aria-hidden="true" class="absolute top-1 left-1 z-0 w-[calc(50%-4px)] h-[calc(100%-8px)] rounded-full bg-ttg07-acc shadow-[0_6px_16px_-6px_oklch(0.5_0.19_285/0.75)] transition-transform duration-[350ms] ease-[cubic-bezier(0.3,1,0.35,1.05)] peer-checked/yearly:translate-x-full motion-reduce:duration-100"></span>
      <label for="ttg-07-m" class="relative z-10 flex items-center justify-center min-h-11 rounded-full text-[14px] font-bold cursor-pointer transition-colors duration-200 text-ttg07-mute peer-checked/monthly:text-white">Monthly</label>
      <label for="ttg-07-y" class="relative z-10 flex items-center justify-center gap-1.5 min-h-11 rounded-full text-[14px] font-bold cursor-pointer transition-colors duration-200 text-ttg07-mute peer-checked/yearly:text-white">
        Annually
        <em class="not-italic text-[11px] font-extrabold px-1.5 py-0.5 rounded-full bg-ttg07-savebg text-ttg07-saveink transition-colors duration-200 peer-checked/yearly:bg-white/25 peer-checked/yearly:text-white">&minus;20%</em>
      </label>
    </div>
    <div class="relative w-full h-14">
      <p class="ttg07-pm absolute inset-0 flex items-baseline justify-center gap-2 transition-[opacity,transform] duration-300 motion-reduce:transition-opacity"><b class="text-[40px] font-extrabold tracking-[-0.02em] text-ttg07-ink">$24</b><span class="text-[13px] text-ttg07-mute">/mo &middot; billed monthly</span></p>
      <p class="ttg07-py absolute inset-0 flex items-baseline justify-center gap-2 opacity-0 translate-y-2 transition-[opacity,transform] duration-300 motion-reduce:transition-opacity"><b class="text-[40px] font-extrabold tracking-[-0.02em] text-ttg07-ink">$19</b><span class="text-[13px] text-ttg07-mute">/mo &middot; billed yearly</span></p>
    </div>
    <p class="text-[12.5px] text-ttg07-mute">Pro plan &middot; unlimited projects</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg07-bg: #f5f4fb;
  --color-ttg07-bg: oklch(0.96 0.01 285);
  --color-ttg07-edge: #eae8f4;
  --color-ttg07-edge: oklch(0.93 0.012 285);
  --color-ttg07-tint: #edebf6;
  --color-ttg07-tint: oklch(0.94 0.014 285);
  --color-ttg07-acc: #5b4ae0;
  --color-ttg07-acc: oklch(0.52 0.19 285);
  --color-ttg07-ink: #201b38;
  --color-ttg07-ink: oklch(0.25 0.04 285);
  --color-ttg07-mute: #6f6a86;
  --color-ttg07-mute: oklch(0.55 0.03 285);
  --color-ttg07-savebg: #cdf0dc;
  --color-ttg07-savebg: oklch(0.91 0.08 155);
  --color-ttg07-saveink: #1f6b45;
  --color-ttg07-saveink: oklch(0.45 0.11 155);
  --font-ttg07-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.ttg-07 {
  width: 100%;
  min-height: 100svh;
}
```
