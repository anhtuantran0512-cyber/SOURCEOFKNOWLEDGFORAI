---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-pricing-sections/tailwind-currency-switcher-pricing-section/"
title: "Tailwind Currency Switcher Pricing Section"
section: "layouts"
category: "tailwind-css-pricing-sections"
category_name: "Tailwind CSS Pricing Sections"
description: "Three currencies, nine prices, zero JavaScript: hidden radios plus group-has-[…]: swap every visible price across all three tiers at once."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Currency Switcher Pricing Section
Source: https://codefronts.com/layouts/tailwind-css-pricing-sections/tailwind-currency-switcher-pricing-section/

Three currencies, nine prices, zero JavaScript: hidden radios plus group-has-[…]: swap every visible price across all three tiers at once. Burgundy on cream, with the featured tier inverted &mdash; and the port's clean-up is the inverted card, whose eight descendant override rules become ordinary utilities on the elements themselves.
## HTML
```html
<section class="tps-17 group w-full min-h-svh bg-tps17-paper font-tps17-sans text-tps17-ink px-[clamp(20px,4vw,40px)] py-[clamp(28px,5vw,56px)]" aria-label="Pricing">
  <header class="text-center mb-[clamp(24px,4vw,36px)]">
    <h2 class="m-0 mb-2 font-tps17-serif text-[clamp(26px,4vw,38px)] font-bold italic tracking-[-0.015em] text-tps17-wine">Pricing in your currency.</h2>
    <p class="m-0 mb-5 text-sm text-tps17-muted">Pay where you live, with the rate fixed at billing time.</p>
    <fieldset class="relative inline-grid grid-cols-3 m-0 p-0.75 rounded-full bg-white border-[1.5px] border-tps17-wine">
      <legend class="sr-only">Currency</legend>
      <input type="radio" name="tps-17__c" id="tps-17-usd" class="peer/usd sr-only" checked>
      <label for="tps-17-usd" class="col-start-1 row-start-1 px-[22px] py-1.75 rounded-full font-tps17-mono text-xs font-bold tracking-[0.1em] text-tps17-muted cursor-pointer transition-[background-color,color] duration-[180ms] peer-checked/usd:bg-tps17-wine peer-checked/usd:text-tps17-cream peer-focus-visible/usd:outline-2 peer-focus-visible/usd:outline-tps17-wine peer-focus-visible/usd:outline-offset-[3px] motion-reduce:transition-none">USD</label>
      <input type="radio" name="tps-17__c" id="tps-17-eur" class="peer/eur sr-only">
      <label for="tps-17-eur" class="col-start-2 row-start-1 px-[22px] py-1.75 rounded-full font-tps17-mono text-xs font-bold tracking-[0.1em] text-tps17-muted cursor-pointer transition-[background-color,color] duration-[180ms] peer-checked/eur:bg-tps17-wine peer-checked/eur:text-tps17-cream peer-focus-visible/eur:outline-2 peer-focus-visible/eur:outline-tps17-wine peer-focus-visible/eur:outline-offset-[3px] motion-reduce:transition-none">EUR</label>
      <input type="radio" name="tps-17__c" id="tps-17-gbp" class="peer/gbp sr-only">
      <label for="tps-17-gbp" class="col-start-3 row-start-1 px-[22px] py-1.75 rounded-full font-tps17-mono text-xs font-bold tracking-[0.1em] text-tps17-muted cursor-pointer transition-[background-color,color] duration-[180ms] peer-checked/gbp:bg-tps17-wine peer-checked/gbp:text-tps17-cream peer-focus-visible/gbp:outline-2 peer-focus-visible/gbp:outline-tps17-wine peer-focus-visible/gbp:outline-offset-[3px] motion-reduce:transition-none">GBP</label>
    </fieldset>
  </header>
  <div class="grid grid-cols-1 md:grid-cols-[repeat(3,minmax(0,1fr))] items-center gap-[18px] max-w-[380px] md:max-w-[1000px] mx-auto">
    <article class="relative flex flex-col px-[22px] pt-[26px] pb-[22px] rounded-[8px] bg-white border border-tps17-line">
      <h3 class="m-0 mb-3 font-tps17-serif text-[22px] font-bold italic text-tps17-wine">Petit</h3>
      <div class="flex items-baseline gap-1 mb-[18px] pb-[18px] border-b border-dashed border-tps17-line text-[38px] font-extrabold tracking-[-0.03em]">
        <span class="hidden group-has-[#tps-17-usd:checked]:inline">$12</span><span class="hidden group-has-[#tps-17-eur:checked]:inline">&euro;11</span><span class="hidden group-has-[#tps-17-gbp:checked]:inline">&pound;10</span>
        <em class="not-italic ml-1.5 text-[13px] font-medium text-tps17-muted">/month</em>
      </div>
      <ul class="list-none p-0 m-0 mb-5 flex-1 text-[13.5px]/[1.95] text-tps17-body">
        <li class="before:content-['\25C6'] before:inline-block before:w-5 before:text-[9px] before:text-tps17-wine">Solo cellar</li>
        <li class="before:content-['\25C6'] before:inline-block before:w-5 before:text-[9px] before:text-tps17-wine">3 bottles tracked</li>
        <li class="before:content-['\25C6'] before:inline-block before:w-5 before:text-[9px] before:text-tps17-wine">Email reminders</li>
      </ul>
      <a href="#petit" class="block text-center px-4 py-2.75 rounded-[6px] bg-transparent text-tps17-wine border-[1.5px] border-current text-[13px] font-semibold uppercase tracking-[0.04em] no-underline transition-[background-color,color] duration-[180ms] hover:bg-tps17-wine hover:text-tps17-cream focus-visible:outline-2 focus-visible:outline-current focus-visible:outline-offset-[3px] motion-reduce:transition-none">Choose Petit</a>
    </article>
    <article class="relative flex flex-col px-[22px] pt-[26px] pb-[22px] rounded-[8px] bg-tps17-wine text-tps17-cream md:scale-[1.04] shadow-[0_18px_44px_--alpha(--color-tps17-wine/30)]">
      <span class="absolute -top-3 left-1/2 -translate-x-1/2 whitespace-nowrap px-2.75 py-1 rounded-full bg-tps17-paper text-tps17-wine border-[1.5px] border-tps17-wine font-tps17-mono text-[10.5px] font-bold uppercase tracking-[0.12em]">Sommelier&rsquo;s pick</span>
      <h3 class="m-0 mb-3 font-tps17-serif text-[22px] font-bold italic text-tps17-cream">Reserve</h3>
      <div class="flex items-baseline gap-1 mb-[18px] pb-[18px] border-b border-dashed border-tps17-cream/25 text-[38px] font-extrabold tracking-[-0.03em]">
        <span class="hidden group-has-[#tps-17-usd:checked]:inline">$36</span><span class="hidden group-has-[#tps-17-eur:checked]:inline">&euro;33</span><span class="hidden group-has-[#tps-17-gbp:checked]:inline">&pound;28</span>
        <em class="not-italic ml-1.5 text-[13px] font-medium text-tps17-cream/70">/month</em>
      </div>
      <ul class="list-none p-0 m-0 mb-5 flex-1 text-[13.5px]/[1.95] text-tps17-cream">
        <li class="before:content-['\25C6'] before:inline-block before:w-5 before:text-[9px] before:text-tps17-cream">Full cellar</li>
        <li class="before:content-['\25C6'] before:inline-block before:w-5 before:text-[9px] before:text-tps17-cream">Unlimited bottles</li>
        <li class="before:content-['\25C6'] before:inline-block before:w-5 before:text-[9px] before:text-tps17-cream">Tasting notes</li>
        <li class="before:content-['\25C6'] before:inline-block before:w-5 before:text-[9px] before:text-tps17-cream">Pairing engine</li>
      </ul>
      <a href="#reserve" class="block text-center px-4 py-2.75 rounded-[6px] bg-tps17-cream text-tps17-wine border-[1.5px] border-tps17-cream text-[13px] font-semibold uppercase tracking-[0.04em] no-underline transition-[background-color,color] duration-[180ms] hover:bg-transparent hover:text-tps17-cream focus-visible:outline-2 focus-visible:outline-tps17-cream focus-visible:outline-offset-[3px] motion-reduce:transition-none">Choose Reserve</a>
    </article>
    <article class="relative flex flex-col px-[22px] pt-[26px] pb-[22px] rounded-[8px] bg-white border border-tps17-line">
      <h3 class="m-0 mb-3 font-tps17-serif text-[22px] font-bold italic text-tps17-wine">Grand Cru</h3>
      <div class="flex items-baseline gap-1 mb-[18px] pb-[18px] border-b border-dashed border-tps17-line text-[38px] font-extrabold tracking-[-0.03em]">
        <span class="hidden group-has-[#tps-17-usd:checked]:inline">$96</span><span class="hidden group-has-[#tps-17-eur:checked]:inline">&euro;88</span><span class="hidden group-has-[#tps-17-gbp:checked]:inline">&pound;76</span>
        <em class="not-italic ml-1.5 text-[13px] font-medium text-tps17-muted">/month</em>
      </div>
      <ul class="list-none p-0 m-0 mb-5 flex-1 text-[13.5px]/[1.95] text-tps17-body">
        <li class="before:content-['\25C6'] before:inline-block before:w-5 before:text-[9px] before:text-tps17-wine">Multi-cellar</li>
        <li class="before:content-['\25C6'] before:inline-block before:w-5 before:text-[9px] before:text-tps17-wine">Insurance valuation</li>
        <li class="before:content-['\25C6'] before:inline-block before:w-5 before:text-[9px] before:text-tps17-wine">White-glove setup</li>
      </ul>
      <a href="#grand" class="block text-center px-4 py-2.75 rounded-[6px] bg-transparent text-tps17-wine border-[1.5px] border-current text-[13px] font-semibold uppercase tracking-[0.04em] no-underline transition-[background-color,color] duration-[180ms] hover:bg-tps17-wine hover:text-tps17-cream focus-visible:outline-2 focus-visible:outline-current focus-visible:outline-offset-[3px] motion-reduce:transition-none">Talk to us</a>
    </article>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tps17-paper: #faf6ee;
  --color-tps17-paper: oklch(0.97 0.012 85);
  --color-tps17-cream: #faf6ee;
  --color-tps17-cream: oklch(0.97 0.012 85);
  --color-tps17-ink: #2a0a14;
  --color-tps17-ink: oklch(0.21 0.06 10);
  --color-tps17-wine: #6b1224;
  --color-tps17-wine: oklch(0.34 0.13 15);
  --color-tps17-body: #4a2030;
  --color-tps17-body: oklch(0.32 0.07 8);
  --color-tps17-muted: #8a4555;
  --color-tps17-muted: oklch(0.48 0.09 10);
  --color-tps17-line: #e7d8c8;
  --color-tps17-line: oklch(0.89 0.025 75);
  --font-tps17-serif: 'Playfair Display', Georgia, serif;
  --font-tps17-mono: 'JetBrains Mono', monospace;
  --font-tps17-sans: 'Public Sans', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the section is sized correctly in the moment before the
   browser build has compiled its utilities. */

.tps-17 {
  width: 100%;
  min-height: 100svh;
}
```
