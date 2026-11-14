---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-pricing-tables/tailwind-pricing-cards-corner-ribbon-bookmark/"
title: "Tailwind Pricing Cards with Corner Ribbon & Bookmark Banner"
section: "components"
category: "tailwind-css-pricing-tables"
category_name: "Tailwind CSS Pricing Tables"
description: "Classic e-commerce trust styling: a diagonal corner ribbon with folded-back ends and a notched bookmark that drops in on load — both drawn with clip-path and…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Pricing Cards with Corner Ribbon & Bookmark Banner
Source: https://codefronts.com/components/tailwind-css-pricing-tables/tailwind-pricing-cards-corner-ribbon-bookmark/

Classic e-commerce trust styling: a diagonal corner ribbon with folded-back ends and a notched bookmark that drops in on load — both drawn with clip-path and pseudo-element utilities, no images. The fold-back triangles are before:/after: squares clipped by [clip-path:polygon(…)], tinted with a darker rib-fold token.
## HTML
```html
<section class="tpt-17 w-full min-h-svh grid place-items-center bg-tpt17-bg px-5 py-20 font-tpt17-sans text-tpt17-ink antialiased" aria-label="Pricing cards with ribbon and bookmark accents">
  <div class="grid w-full max-w-5xl justify-items-center gap-12">
    <h2 class="text-center font-tpt17-serif text-[clamp(30px,4.4vw,48px)] leading-tight font-medium tracking-[-0.02em] text-balance">Launch week <em class="text-tpt17-rib">pricing</em></h2>
    <div class="grid w-full gap-8 md:grid-cols-3 md:gap-6">
      <article class="relative flex flex-col gap-2 rounded-2xl border border-tpt17-line bg-white px-7 pt-10 pb-7">
        <span aria-hidden="true" class="absolute -top-1 left-6 animate-tpt17-drop bg-tpt17-ink px-2.5 pt-3 pb-4 text-[11px] font-bold tracking-[0.12em] text-white uppercase [animation-delay:.5s] [clip-path:polygon(0_0,100%_0,100%_100%,50%_calc(100%-8px),0_100%)] motion-reduce:animate-none">Deal</span>
        <h3 class="text-[13px] font-bold tracking-[0.08em] text-tpt17-mut uppercase">Basic</h3>
        <p class="text-[44px] leading-tight font-extrabold tracking-[-0.035em]">$14<small class="text-[15px] font-semibold tracking-normal text-tpt17-mut">/mo</small></p>
        <p class="mt-1 mb-5 flex-1 text-sm leading-relaxed text-tpt17-body"><strong class="font-semibold text-tpt17-ink">Launch deal:</strong> this price is locked for life.</p>
        <a href="#" class="grid min-h-11 place-items-center rounded-xl border-[1.5px] border-tpt17-line text-sm font-bold text-tpt17-ink no-underline transition-colors hover:border-tpt17-rib focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt17-rib">Get Basic</a>
      </article>
      <article class="relative flex flex-col gap-2 rounded-2xl bg-white px-7 pt-10 pb-7 shadow-[0_18px_40px_-26px_var(--color-tpt17-rib)] ring-2 ring-tpt17-rib">
        <span aria-hidden="true" class="pointer-events-none absolute -top-1.5 -right-1.5 size-28 overflow-hidden before:absolute before:top-0 before:left-3.5 before:size-1.5 before:bg-tpt17-rib-fold before:content-[''] before:[clip-path:polygon(0_100%,100%_100%,100%_0)] after:absolute after:right-0 after:bottom-3.5 after:size-1.5 after:bg-tpt17-rib-fold after:content-[''] after:[clip-path:polygon(0_0,0_100%,100%_0)]"><span class="absolute top-6.5 -right-8.5 block w-40 rotate-45 animate-tpt17-slide bg-tpt17-rib py-1.5 text-center text-[12.5px] font-extrabold tracking-[0.1em] text-white shadow-[0_4px_10px_oklch(0_0_0/0.18)] [animation-delay:.3s] motion-reduce:animate-none">−30%</span></span>
        <h3 class="text-[13px] font-bold tracking-[0.08em] text-tpt17-rib-ink uppercase">Plus</h3>
        <p class="flex items-baseline gap-2 text-[44px] leading-tight font-extrabold tracking-[-0.035em]"><span>$34</span><small class="text-[15px] font-semibold tracking-normal text-tpt17-mut">/mo</small><s class="text-lg font-semibold tracking-normal text-tpt17-mut">$49</s></p>
        <p class="mt-1 mb-5 flex-1 text-sm leading-relaxed text-tpt17-body"><strong class="font-semibold text-tpt17-ink">30% off</strong> when billed annually.</p>
        <a href="#" class="grid min-h-11 place-items-center rounded-xl bg-tpt17-rib text-sm font-bold text-white no-underline transition-colors hover:bg-tpt17-rib-ink focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt17-rib">Get Plus</a>
      </article>
      <article class="relative flex flex-col gap-2 rounded-2xl border border-tpt17-line bg-white px-7 pt-10 pb-7">
        <h3 class="text-[13px] font-bold tracking-[0.08em] text-tpt17-mut uppercase">Max</h3>
        <p class="text-[44px] leading-tight font-extrabold tracking-[-0.035em]">$74<small class="text-[15px] font-semibold tracking-normal text-tpt17-mut">/mo</small></p>
        <p class="mt-1 mb-5 flex-1 text-sm leading-relaxed text-tpt17-body">The full suite with priority everything.</p>
        <a href="#" class="grid min-h-11 place-items-center rounded-xl border-[1.5px] border-tpt17-line text-sm font-bold text-tpt17-ink no-underline transition-colors hover:border-tpt17-rib focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt17-rib">Get Max</a>
      </article>
    </div>
    <p aria-hidden="true" class="rounded-full border border-tpt17-line bg-white px-3.5 py-2 font-tpt17-mono text-[11.5px] text-tpt17-mut">rotate-45 strip · before:[clip-path:polygon(…)] folds · animate-tpt17-drop</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpt17-bg: #f6f4f1;
  --color-tpt17-bg: oklch(0.965 0.006 70);
  --color-tpt17-ink: #1e1a17;
  --color-tpt17-ink: oklch(0.22 0.01 60);
  --color-tpt17-body: #544b43;
  --color-tpt17-body: oklch(0.43 0.02 60);
  --color-tpt17-mut: #6f665e;
  --color-tpt17-mut: oklch(0.52 0.018 60);
  --color-tpt17-line: #e6e0d9;
  --color-tpt17-line: oklch(0.91 0.012 70);
  --color-tpt17-rib: #d8284a;
  --color-tpt17-rib: oklch(0.57 0.21 15);
  --color-tpt17-rib-ink: #b01a3a;
  --color-tpt17-rib-ink: oklch(0.49 0.19 15);
  --color-tpt17-rib-fold: #7c1127;
  --color-tpt17-rib-fold: oklch(0.37 0.14 15);
  --font-tpt17-serif: 'Newsreader', Georgia, serif;
  --font-tpt17-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tpt17-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tpt17-slide: tpt17-slide 0.7s cubic-bezier(0.3, 1.4, 0.4, 1) both;
  --animate-tpt17-drop: tpt17-drop 0.6s cubic-bezier(0.3, 1.5, 0.4, 1) both;

  @keyframes tpt17-slide {
    from {
      translate: 112px -112px;
    }
  }

  @keyframes tpt17-drop {
    from {
      translate: 0 -110%;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities. */

.tpt-17 {
  width: 100%;
  min-height: 100svh;
}
```
