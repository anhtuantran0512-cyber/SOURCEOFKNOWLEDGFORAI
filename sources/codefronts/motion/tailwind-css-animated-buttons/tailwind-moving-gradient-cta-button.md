---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-animated-buttons/tailwind-moving-gradient-cta-button/"
title: "Tailwind Moving Gradient CTA Button"
section: "motion"
category: "tailwind-css-animated-buttons"
category_name: "Tailwind CSS Animated Buttons"
description: "An infinite colour-cycling CTA: one oversized gradient, one background-position loop."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Moving Gradient CTA Button
Source: https://codefronts.com/motion/tailwind-css-animated-buttons/tailwind-moving-gradient-cta-button/

An infinite colour-cycling CTA: one oversized gradient, one background-position loop. The port is nearly a transcription &mdash; bg-[linear-gradient(...)] bg-[size:300%_300%] animate-tab07-shift &mdash; and the notable part is how the reduced-motion fallback becomes a one-utility override instead of a duplicated rule.
## HTML
```html
<section class="tab-07 w-full min-h-svh grid place-items-center bg-tab07-bg font-tab07-sans px-6 py-10">
  <div class="w-[min(440px,100%)] text-center px-8 py-10 rounded-2xl bg-tab07-card border border-white/8">
    <p class="text-xs tracking-[0.18em] uppercase text-tab07-acc m-0">Limited Time Offer</p>
    <h2 class="mt-3 mb-3 text-[1.8rem] font-bold text-tab07-ink">Start Your Free Trial</h2>
    <p class="mb-7 text-[0.9rem] leading-relaxed text-tab07-mut">14 days free, no credit card required. Cancel anytime with one click.</p>
    <button type="button" class="inline-flex items-center justify-center min-h-11 px-10 text-base font-bold tracking-[0.03em] text-white rounded-xl cursor-pointer bg-[linear-gradient(90deg,#7c3aed,#06b6d4,#f43f5e,#7c3aed)] bg-[size:300%_300%] animate-tab07-shift shadow-[0_4px_20px_oklch(0.53_0.25_295/0.4)] transition-[translate,box-shadow,filter] duration-200 hover:brightness-110 hover:-translate-y-0.5 hover:shadow-[0_6px_32px_oklch(0.53_0.25_295/0.6)] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-white active:translate-y-0 active:brightness-95 motion-reduce:animate-none motion-reduce:bg-[linear-gradient(90deg,#7c3aed,#06b6d4)] motion-reduce:transition-none">Claim Your Free Trial &rarr;</button>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tab07-bg: #0a0a14;
  --color-tab07-bg: oklch(0.11 0.02 275);
  --color-tab07-card: #13131f;
  --color-tab07-card: oklch(0.16 0.02 275);
  --color-tab07-ink: #f1f5f9;
  --color-tab07-ink: oklch(0.96 0.005 250);
  --color-tab07-mut: #94a3b8;
  --color-tab07-mut: oklch(0.72 0.03 255);
  --color-tab07-acc: #a78bfa;
  --color-tab07-acc: oklch(0.74 0.15 292);
  --font-tab07-sans: 'Space Grotesk', system-ui, sans-serif;
  --animate-tab07-shift: tab07-shift 4s ease infinite;
}

@keyframes tab07-shift {
  0% {
    background-position: 0% 50%;
  }

  50% {
    background-position: 100% 50%;
  }

  100% {
    background-position: 0% 50%;
  }
}

.tab-07 {
  width: 100%;
  min-height: 100svh;
}

.tab-07 ::selection {
  background: var(--color-tab07-acc);
  color: #14091f;
}
```
