---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-pricing-tables/tailwind-css-3d-flip-pricing-cards/"
title: "Tailwind CSS 3D Flip Pricing Cards"
section: "components"
category: "tailwind-css-pricing-tables"
category_name: "Tailwind CSS Pricing Tables"
description: "Click &ldquo;View details&rdquo; and the whole pricing card turns 180&deg; to reveal specs and fine print on its back."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS 3D Flip Pricing Cards
Source: https://codefronts.com/components/tailwind-css-pricing-tables/tailwind-css-3d-flip-pricing-cards/

Click &ldquo;View details&rdquo; and the whole pricing card turns 180&deg; to reveal specs and fine print on its back. Tailwind v4 ships the 3D kit natively — perspective-[1400px], transform-3d, backface-hidden, rotate-y-180 — so the entire flip is a hidden checkbox and group-has-checked/f:. No JavaScript, and focus can never land on the face you can't see.
## HTML
```html
<section class="tpt-10 w-full min-h-svh grid place-items-center bg-tpt10-bg px-5 py-16 font-tpt10-sans text-tpt10-ink antialiased" aria-label="Pricing cards that flip to show plan details">
  <div class="grid w-full max-w-5xl justify-items-center gap-10">
    <h2 class="text-center text-[clamp(26px,3.8vw,40px)] font-extrabold tracking-[-0.03em]">Every detail, one flip away</h2>
    <div class="grid w-full gap-5 md:grid-cols-3">
      <div class="group/f perspective-[1400px]">
        <input type="checkbox" id="tpt10-a" class="peer sr-only" aria-label="Show Launch plan details">
        <div class="grid h-full rounded-[20px] transition-transform duration-700 ease-[cubic-bezier(.5,0,.2,1)] transform-3d group-has-checked/f:rotate-y-180 peer-focus-visible:outline-3 peer-focus-visible:outline-offset-4 peer-focus-visible:outline-tpt10-acc motion-reduce:transition-none">
          <article class="col-start-1 row-start-1 flex flex-col gap-3 rounded-[20px] border border-tpt10-line bg-white p-7 backface-hidden [transition:visibility_0s_.35s] group-has-checked/f:invisible">
            <h3 class="text-[13px] font-bold tracking-[0.08em] text-tpt10-mut uppercase">Launch</h3>
            <p class="text-[44px] leading-none font-extrabold tracking-[-0.035em]">$25<small class="text-[15px] font-semibold tracking-normal text-tpt10-mut">/mo</small></p>
            <p class="flex-1 text-sm leading-relaxed text-tpt10-body">For new stores finding their footing.</p>
            <a href="#" class="grid min-h-11 place-items-center rounded-xl border-[1.5px] border-tpt10-line text-sm font-bold text-tpt10-ink no-underline transition-colors hover:border-tpt10-acc focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt10-acc">Choose Launch</a>
            <label for="tpt10-a" class="grid min-h-11 cursor-pointer place-items-center rounded-xl text-[13px] font-bold text-tpt10-acc-ink transition-colors hover:bg-tpt10-acc/10">View details ⟳</label>
          </article>
          <article class="invisible col-start-1 row-start-1 flex rotate-y-180 flex-col gap-3 rounded-[20px] bg-tpt10-ink p-7 text-tpt10-bg backface-hidden [transition:visibility_0s_.35s] group-has-checked/f:visible">
            <h4 class="text-[15px] font-bold">Launch — details</h4>
            <ul class="grid flex-1 content-start gap-2.5 text-sm text-tpt10-back-body *:flex *:gap-2.5 *:before:text-tpt10-acc-lite *:before:content-['•']"><li>1 staff account</li><li>2.9% + 30¢ per online sale</li><li>Basic reports</li><li>14-day trial, cancel anytime</li></ul>
            <label for="tpt10-a" class="grid min-h-11 cursor-pointer place-items-center rounded-xl text-[13px] font-bold text-tpt10-acc-lite transition-colors hover:bg-white/8">⟲ Back</label>
          </article>
        </div>
      </div>
      <div class="group/f perspective-[1400px]">
        <input type="checkbox" id="tpt10-b" class="peer sr-only" aria-label="Show Grow plan details">
        <div class="grid h-full rounded-[20px] transition-transform duration-700 ease-[cubic-bezier(.5,0,.2,1)] transform-3d group-has-checked/f:rotate-y-180 peer-focus-visible:outline-3 peer-focus-visible:outline-offset-4 peer-focus-visible:outline-tpt10-acc motion-reduce:transition-none">
          <article class="relative col-start-1 row-start-1 flex flex-col gap-3 rounded-[20px] bg-white p-7 shadow-[0_18px_40px_-24px_var(--color-tpt10-acc)] ring-2 ring-tpt10-acc backface-hidden [transition:visibility_0s_.35s] group-has-checked/f:invisible">
            <h3 class="text-[13px] font-bold tracking-[0.08em] text-tpt10-acc-ink uppercase">Grow</h3>
            <p class="text-[44px] leading-none font-extrabold tracking-[-0.035em]">$65<small class="text-[15px] font-semibold tracking-normal text-tpt10-mut">/mo</small></p>
            <p class="flex-1 text-sm leading-relaxed text-tpt10-body">For stores scaling past six figures.</p>
            <a href="#" class="grid min-h-11 place-items-center rounded-xl bg-tpt10-acc text-sm font-bold text-white no-underline transition-colors hover:bg-tpt10-acc-ink focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt10-acc">Choose Grow</a>
            <label for="tpt10-b" class="grid min-h-11 cursor-pointer place-items-center rounded-xl text-[13px] font-bold text-tpt10-acc-ink transition-colors hover:bg-tpt10-acc/10">View details ⟳</label>
          </article>
          <article class="invisible col-start-1 row-start-1 flex rotate-y-180 flex-col gap-3 rounded-[20px] bg-tpt10-ink p-7 text-tpt10-bg backface-hidden [transition:visibility_0s_.35s] group-has-checked/f:visible">
            <h4 class="text-[15px] font-bold">Grow — details</h4>
            <ul class="grid flex-1 content-start gap-2.5 text-sm text-tpt10-back-body *:flex *:gap-2.5 *:before:text-tpt10-acc-lite *:before:content-['•']"><li>5 staff accounts</li><li>2.4% + 30¢ per online sale</li><li>Advanced reports &amp; forecasts</li><li>Abandoned-cart recovery</li></ul>
            <label for="tpt10-b" class="grid min-h-11 cursor-pointer place-items-center rounded-xl text-[13px] font-bold text-tpt10-acc-lite transition-colors hover:bg-white/8">⟲ Back</label>
          </article>
        </div>
      </div>
      <div class="group/f perspective-[1400px]">
        <input type="checkbox" id="tpt10-c" class="peer sr-only" aria-label="Show Advanced plan details">
        <div class="grid h-full rounded-[20px] transition-transform duration-700 ease-[cubic-bezier(.5,0,.2,1)] transform-3d group-has-checked/f:rotate-y-180 peer-focus-visible:outline-3 peer-focus-visible:outline-offset-4 peer-focus-visible:outline-tpt10-acc motion-reduce:transition-none">
          <article class="col-start-1 row-start-1 flex flex-col gap-3 rounded-[20px] border border-tpt10-line bg-white p-7 backface-hidden [transition:visibility_0s_.35s] group-has-checked/f:invisible">
            <h3 class="text-[13px] font-bold tracking-[0.08em] text-tpt10-mut uppercase">Advanced</h3>
            <p class="text-[44px] leading-none font-extrabold tracking-[-0.035em]">$199<small class="text-[15px] font-semibold tracking-normal text-tpt10-mut">/mo</small></p>
            <p class="flex-1 text-sm leading-relaxed text-tpt10-body">For high-volume, multi-region brands.</p>
            <a href="#" class="grid min-h-11 place-items-center rounded-xl border-[1.5px] border-tpt10-line text-sm font-bold text-tpt10-ink no-underline transition-colors hover:border-tpt10-acc focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt10-acc">Choose Advanced</a>
            <label for="tpt10-c" class="grid min-h-11 cursor-pointer place-items-center rounded-xl text-[13px] font-bold text-tpt10-acc-ink transition-colors hover:bg-tpt10-acc/10">View details ⟳</label>
          </article>
          <article class="invisible col-start-1 row-start-1 flex rotate-y-180 flex-col gap-3 rounded-[20px] bg-tpt10-ink p-7 text-tpt10-bg backface-hidden [transition:visibility_0s_.35s] group-has-checked/f:visible">
            <h4 class="text-[15px] font-bold">Advanced — details</h4>
            <ul class="grid flex-1 content-start gap-2.5 text-sm text-tpt10-back-body *:flex *:gap-2.5 *:before:text-tpt10-acc-lite *:before:content-['•']"><li>15 staff accounts</li><li>1.9% + 30¢ per online sale</li><li>Custom report builder</li><li>Duty &amp; tax calculators</li></ul>
            <label for="tpt10-c" class="grid min-h-11 cursor-pointer place-items-center rounded-xl text-[13px] font-bold text-tpt10-acc-lite transition-colors hover:bg-white/8">⟲ Back</label>
          </article>
        </div>
      </div>
    </div>
    <p aria-hidden="true" class="rounded-full border border-tpt10-line bg-white px-3.5 py-2 font-tpt10-mono text-[11.5px] text-tpt10-mut">perspective-[1400px] · transform-3d · backface-hidden · rotate-y-180</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpt10-bg: #eef2f6;
  --color-tpt10-bg: oklch(0.96 0.008 245);
  --color-tpt10-ink: #15202c;
  --color-tpt10-ink: oklch(0.24 0.03 250);
  --color-tpt10-body: #4b596a;
  --color-tpt10-body: oklch(0.45 0.03 250);
  --color-tpt10-back-body: #d3dbe5;
  --color-tpt10-back-body: oklch(0.88 0.015 250);
  --color-tpt10-mut: #5d6b7d;
  --color-tpt10-mut: oklch(0.51 0.03 250);
  --color-tpt10-line: #dce3eb;
  --color-tpt10-line: oklch(0.91 0.012 245);
  --color-tpt10-acc: #1a86d4;
  --color-tpt10-acc: oklch(0.6 0.15 245);
  --color-tpt10-acc-ink: #0f65a6;
  --color-tpt10-acc-ink: oklch(0.5 0.13 248);
  --color-tpt10-acc-lite: #8cc6f5;
  --color-tpt10-acc-lite: oklch(0.8 0.09 240);
  --font-tpt10-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tpt10-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities. */

.tpt-10 {
  width: 100%;
  min-height: 100svh;
}
```
