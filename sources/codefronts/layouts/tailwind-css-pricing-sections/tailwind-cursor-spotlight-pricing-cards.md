---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-pricing-sections/tailwind-cursor-spotlight-pricing-cards/"
title: "Tailwind Cursor Spotlight Pricing Cards"
section: "layouts"
category: "tailwind-css-pricing-sections"
category_name: "Tailwind CSS Pricing Sections"
description: "Amber light follows the cursor across black cards &mdash; and lands centred when you tab to one, so keyboard users get the same affordance."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Cursor Spotlight Pricing Cards
Source: https://codefronts.com/layouts/tailwind-css-pricing-sections/tailwind-cursor-spotlight-pricing-cards/

Amber light follows the cursor across black cards &mdash; and lands centred when you tab to one, so keyboard users get the same affordance. The JS sets two custom properties and stops there; group-hover: and group-focus-within: own the reveal, which is the cleanest possible division between script and style.
## HTML
```html
<section class="tps-20 w-full min-h-svh bg-tps20-bg font-tps20-mono text-tps20-body px-[clamp(20px,4vw,40px)] py-[clamp(28px,5vw,56px)]" aria-label="Pricing">
  <header class="text-center mb-[clamp(24px,4vw,40px)]">
    <h2 class="m-0 mb-2 font-tps20-display text-[clamp(22px,3.4vw,32px)] font-bold tracking-[-0.02em] text-white">Move the light. Read the price.</h2>
    <p class="m-0 text-[13.5px] text-tps20-muted">Cursor-aware cards. Real cards, real prices, real keyboard support.</p>
  </header>
  <div class="grid grid-cols-1 md:grid-cols-[repeat(3,minmax(0,1fr))] items-stretch gap-3.5 max-w-[360px] md:max-w-[980px] mx-auto">
    <article data-tps20-card tabindex="0" class="group relative isolate overflow-hidden flex flex-col px-[22px] pt-6 pb-5 rounded-[14px] bg-tps20-card border border-tps20-line transition-[border-color,translate] duration-200 hover:border-tps20-amber hover:-translate-y-0.5 focus-within:border-tps20-amber focus-within:-translate-y-0.5 focus:outline-0 focus-visible:outline-2 focus-visible:outline-tps20-amber focus-visible:outline-offset-[3px] motion-reduce:transition-none motion-reduce:hover:translate-y-0 motion-reduce:focus-within:translate-y-0">
      <div class="absolute inset-0 z-0 pointer-events-none opacity-0 transition-opacity duration-[250ms] group-hover:opacity-100 group-focus-within:opacity-100 bg-[radial-gradient(180px_circle_at_var(--tps20-x,50%)_var(--tps20-y,50%),--alpha(--color-tps20-amber/40)_0%,--alpha(--color-tps20-amber/10)_30%,transparent_60%)] motion-reduce:transition-none" aria-hidden="true"></div>
      <h3 class="relative z-1 m-0 mb-3 text-[13px] font-bold uppercase tracking-[0.16em] text-tps20-amber">OSS</h3>
      <div class="relative z-1 flex items-baseline gap-2 mb-[18px] text-[38px] font-extrabold tracking-[-0.03em] text-white">$0<span class="text-xs font-medium tracking-[0.04em] text-tps20-muted">open source</span></div>
      <ul class="relative z-1 list-none p-0 m-0 mb-5 flex-1 text-[12.5px]/[2] text-tps20-list">
        <li class="before:content-['&gt;_'] before:text-tps20-amber">Self-hosted</li>
        <li class="before:content-['&gt;_'] before:text-tps20-amber">MIT licence</li>
        <li class="before:content-['&gt;_'] before:text-tps20-amber">GitHub issues</li>
      </ul>
      <a href="#oss" class="relative z-1 block text-center px-4 py-2.5 rounded-[6px] bg-transparent text-tps20-amber border-[1.5px] border-tps20-amber-dark text-[11.5px] font-bold uppercase tracking-[0.1em] no-underline transition-[background-color,color,border-color] duration-[180ms] hover:bg-tps20-amber hover:text-tps20-bg hover:border-tps20-amber focus-visible:outline-2 focus-visible:outline-tps20-amber focus-visible:outline-offset-[3px] motion-reduce:transition-none">Clone the repo</a>
    </article>
    <article data-tps20-card tabindex="0" class="group relative isolate overflow-hidden flex flex-col px-[22px] pt-6 pb-5 rounded-[14px] bg-linear-180 from-tps20-card-hi to-tps20-card border border-tps20-amber-dark transition-[border-color,translate] duration-200 hover:border-tps20-amber hover:-translate-y-0.5 focus-within:border-tps20-amber focus-within:-translate-y-0.5 focus:outline-0 focus-visible:outline-2 focus-visible:outline-tps20-amber focus-visible:outline-offset-[3px] motion-reduce:transition-none motion-reduce:hover:translate-y-0 motion-reduce:focus-within:translate-y-0">
      <div class="absolute inset-0 z-0 pointer-events-none opacity-0 transition-opacity duration-[250ms] group-hover:opacity-100 group-focus-within:opacity-100 bg-[radial-gradient(180px_circle_at_var(--tps20-x,50%)_var(--tps20-y,50%),--alpha(--color-tps20-amber/40)_0%,--alpha(--color-tps20-amber/10)_30%,transparent_60%)] motion-reduce:transition-none" aria-hidden="true"></div>
      <span class="relative z-1 self-start mb-2.5 px-2.5 py-0.75 rounded-[4px] bg-tps20-amber text-tps20-bg text-[10px] font-bold uppercase tracking-[0.12em]">Recommended</span>
      <h3 class="relative z-1 m-0 mb-3 text-[13px] font-bold uppercase tracking-[0.16em] text-tps20-amber">Cloud</h3>
      <div class="relative z-1 flex items-baseline gap-2 mb-[18px] text-[38px] font-extrabold tracking-[-0.03em] text-white">$24<span class="text-xs font-medium tracking-[0.04em] text-tps20-muted">/mo</span></div>
      <ul class="relative z-1 list-none p-0 m-0 mb-5 flex-1 text-[12.5px]/[2] text-tps20-list">
        <li class="before:content-['&gt;_'] before:text-tps20-amber">Hosted &amp; maintained</li>
        <li class="before:content-['&gt;_'] before:text-tps20-amber">Auto-updates + backups</li>
        <li class="before:content-['&gt;_'] before:text-tps20-amber">Email support</li>
        <li class="before:content-['&gt;_'] before:text-tps20-amber">API access</li>
      </ul>
      <a href="#cloud" class="relative z-1 block text-center px-4 py-2.5 rounded-[6px] bg-tps20-amber text-tps20-bg border-[1.5px] border-tps20-amber text-[11.5px] font-bold uppercase tracking-[0.1em] no-underline transition-[filter] duration-[180ms] hover:brightness-110 focus-visible:outline-2 focus-visible:outline-tps20-amber focus-visible:outline-offset-[3px] motion-reduce:transition-none">Choose Cloud</a>
    </article>
    <article data-tps20-card tabindex="0" class="group relative isolate overflow-hidden flex flex-col px-[22px] pt-6 pb-5 rounded-[14px] bg-tps20-card border border-tps20-line transition-[border-color,translate] duration-200 hover:border-tps20-amber hover:-translate-y-0.5 focus-within:border-tps20-amber focus-within:-translate-y-0.5 focus:outline-0 focus-visible:outline-2 focus-visible:outline-tps20-amber focus-visible:outline-offset-[3px] motion-reduce:transition-none motion-reduce:hover:translate-y-0 motion-reduce:focus-within:translate-y-0">
      <div class="absolute inset-0 z-0 pointer-events-none opacity-0 transition-opacity duration-[250ms] group-hover:opacity-100 group-focus-within:opacity-100 bg-[radial-gradient(180px_circle_at_var(--tps20-x,50%)_var(--tps20-y,50%),--alpha(--color-tps20-amber/40)_0%,--alpha(--color-tps20-amber/10)_30%,transparent_60%)] motion-reduce:transition-none" aria-hidden="true"></div>
      <h3 class="relative z-1 m-0 mb-3 text-[13px] font-bold uppercase tracking-[0.16em] text-tps20-amber">Self-Hosted Pro</h3>
      <div class="relative z-1 flex items-baseline gap-2 mb-[18px] text-[38px] font-extrabold tracking-[-0.03em] text-white">$199<span class="text-xs font-medium tracking-[0.04em] text-tps20-muted">/yr</span></div>
      <ul class="relative z-1 list-none p-0 m-0 mb-5 flex-1 text-[12.5px]/[2] text-tps20-list">
        <li class="before:content-['&gt;_'] before:text-tps20-amber">Commercial licence</li>
        <li class="before:content-['&gt;_'] before:text-tps20-amber">Priority email support</li>
        <li class="before:content-['&gt;_'] before:text-tps20-amber">Audit logs</li>
      </ul>
      <a href="#shp" class="relative z-1 block text-center px-4 py-2.5 rounded-[6px] bg-transparent text-tps20-amber border-[1.5px] border-tps20-amber-dark text-[11.5px] font-bold uppercase tracking-[0.1em] no-underline transition-[background-color,color,border-color] duration-[180ms] hover:bg-tps20-amber hover:text-tps20-bg hover:border-tps20-amber focus-visible:outline-2 focus-visible:outline-tps20-amber focus-visible:outline-offset-[3px] motion-reduce:transition-none">Buy licence</a>
    </article>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tps20-bg: #050505;
  --color-tps20-bg: oklch(0.09 0 0);
  --color-tps20-card: #0a0a0a;
  --color-tps20-card: oklch(0.13 0 0);
  --color-tps20-card-hi: #1a0f02;
  --color-tps20-card-hi: oklch(0.18 0.03 70);
  --color-tps20-line: #2a2418;
  --color-tps20-line: oklch(0.26 0.02 80);
  --color-tps20-body: #f5e6c8;
  --color-tps20-body: oklch(0.93 0.04 85);
  --color-tps20-list: #d8c69a;
  --color-tps20-list: oklch(0.84 0.06 88);
  --color-tps20-muted: #a89470;
  --color-tps20-muted: oklch(0.68 0.05 85);
  --color-tps20-amber: #f59e0b;
  --color-tps20-amber: oklch(0.75 0.16 70);
  --color-tps20-amber-dark: #b45309;
  --color-tps20-amber-dark: oklch(0.55 0.15 55);
  --font-tps20-mono: 'JetBrains Mono', monospace;
  --font-tps20-display: 'Inter Tight', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the section is sized correctly in the moment before the
   browser build has compiled its utilities. */

.tps-20 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(function () {
  // The script's whole contribution is two custom properties. The reveal,
  // the fade, the gradient and the reduced-motion fallback are all utilities.
  var cards = document.querySelectorAll('[data-tps20-card]');
  Array.prototype.forEach.call(cards, function (card) {
    card.addEventListener('pointermove', function (e) {
      var rect = card.getBoundingClientRect();
      card.style.setProperty('--tps20-x', ((e.clientX - rect.left) / rect.width) * 100 + '%');
      card.style.setProperty('--tps20-y', ((e.clientY - rect.top) / rect.height) * 100 + '%');
    });
    // Keyboard parity: park the light in the middle when the card is focused.
    card.addEventListener('focus', function () {
      card.style.setProperty('--tps20-x', '50%');
      card.style.setProperty('--tps20-y', '50%');
    });
  });
})();
```
