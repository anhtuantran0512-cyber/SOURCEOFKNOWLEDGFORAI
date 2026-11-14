---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-pricing-sections/tailwind-single-premium-pricing-card/"
title: "Tailwind Single Premium Pricing Card"
section: "layouts"
category: "tailwind-css-pricing-sections"
category_name: "Tailwind CSS Pricing Sections"
description: "One product, one price, one card &mdash; brass on deep navy, an 88px serif numeral and a testimonial doing the anchoring that a tier ladder normally does."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Single Premium Pricing Card
Source: https://codefronts.com/layouts/tailwind-css-pricing-sections/tailwind-single-premium-pricing-card/

One product, one price, one card &mdash; brass on deep navy, an 88px serif numeral and a testimonial doing the anchoring that a tier ladder normally does. The port's interesting move is the before: variant: the diagonal sheen that was a ::before rule becomes six utilities on the card itself, so the decoration travels with the element it decorates.
## HTML
```html
<section class="tps-06 w-full min-h-svh flex items-center justify-center bg-tps06-bg bg-[radial-gradient(60%_60%_at_30%_0%,var(--color-tps06-glow1),transparent_60%),radial-gradient(50%_50%_at_90%_100%,var(--color-tps06-glow2),transparent_60%)] font-tps06-sans text-tps06-ink px-[clamp(20px,4vw,40px)] py-[clamp(28px,5vw,56px)]" aria-label="Pricing">
  <article class="relative w-full max-w-[540px] p-[clamp(28px,5vw,44px)] rounded-[22px] text-center bg-linear-to-b from-tps06-card to-tps06-bg border border-tps06-gold shadow-[0_20px_60px_--theme(--color-tps06-glow3),inset_0_0_0_1px_--theme(--color-tps06-glow1)] before:content-[''] before:absolute before:inset-0 before:rounded-[22px] before:bg-[linear-gradient(135deg,transparent_40%,var(--color-tps06-sheen)_50%,transparent_60%)] before:pointer-events-none">
    <span class="inline-block mb-4.5 px-3.5 py-1.25 rounded-full border border-tps06-goldedge text-[11px] font-semibold tracking-[0.18em] uppercase text-tps06-gold">One plan &middot; everything included</span>
    <h2 class="m-0 mb-3.5 font-tps06-display text-[clamp(28px,4.5vw,44px)] font-bold tracking-[-0.01em] text-white text-pretty">The whole product, <em class="italic text-tps06-gold">flat fee.</em></h2>
    <p class="mx-auto mt-0 mb-7 max-w-[380px] text-[14.5px]/relaxed text-tps06-mut">Stop comparing tiers. One price. Every feature. Every team member. As long as you need it.</p>
    <div class="flex flex-col items-center gap-1 mb-7 py-5.5 border-y border-tps06-goldsoft">
      <span class="font-tps06-display text-[clamp(56px,9vw,88px)] font-extrabold leading-none tracking-[-0.04em] text-transparent bg-linear-to-b from-tps06-gold2 to-tps06-gold bg-clip-text forced-colors:text-[CanvasText]"><em class="align-top pr-0.5 text-[0.5em] not-italic opacity-85">$</em>249</span>
      <span class="text-[13px] text-tps06-mut">per month, billed annually</span>
    </div>
    <ul class="list-none p-0 m-0 mb-7 grid grid-cols-1 sm:grid-cols-2 gap-y-2.5 gap-x-5.5 text-left text-[13.5px] text-tps06-ink">
      <li><span class="inline-block w-5 font-bold text-tps06-gold" aria-hidden="true">&#10003;</span>Unlimited team members</li>
      <li><span class="inline-block w-5 font-bold text-tps06-gold" aria-hidden="true">&#10003;</span>Unlimited projects &amp; storage</li>
      <li><span class="inline-block w-5 font-bold text-tps06-gold" aria-hidden="true">&#10003;</span>SSO &amp; SAML included</li>
      <li><span class="inline-block w-5 font-bold text-tps06-gold" aria-hidden="true">&#10003;</span>SOC 2 &amp; HIPAA ready</li>
      <li><span class="inline-block w-5 font-bold text-tps06-gold" aria-hidden="true">&#10003;</span>Priority email + chat support</li>
      <li><span class="inline-block w-5 font-bold text-tps06-gold" aria-hidden="true">&#10003;</span>30-day money-back guarantee</li>
    </ul>
    <a href="#buy" class="relative z-1 block px-5 py-3.5 rounded-[10px] text-[15px] font-bold tracking-[0.01em] no-underline text-tps06-bg bg-linear-to-b from-tps06-gold2 to-tps06-gold shadow-[0_10px_24px_--theme(--color-tps06-glow4)] transition-transform duration-200 hover:-translate-y-px focus-visible:outline-2 focus-visible:outline-tps06-gold2 focus-visible:outline-offset-3 motion-reduce:transition-none motion-reduce:hover:translate-y-0">Buy now &mdash; instant access</a>
    <p class="mt-3 mb-6.5 text-xs text-tps06-dim">No demo required. Cancel any time, refund any time within 30 days.</p>
    <blockquote class="m-0 pt-5.5 border-t border-dashed border-tps06-goldsoft">
      <p class="m-0 mb-2 font-tps06-display text-base/snug italic text-tps06-ink">&ldquo;It paid for itself in the first week. We never looked at the tier ladder again.&rdquo;</p>
      <cite class="not-italic text-xs tracking-[0.05em] text-tps06-dim">&mdash; Maya R., Head of Ops at Northwood</cite>
    </blockquote>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tps06-bg: #0b0b1a;
  --color-tps06-bg: oklch(0.15 0.03 280);
  --color-tps06-card: #14142a;
  --color-tps06-card: oklch(0.2 0.04 280);
  --color-tps06-ink: #f4ecd8;
  --color-tps06-ink: oklch(0.94 0.03 90);
  --color-tps06-mut: #b8a888;
  --color-tps06-mut: oklch(0.73 0.05 90);
  --color-tps06-dim: #8a8068;
  --color-tps06-dim: oklch(0.58 0.04 90);
  --color-tps06-gold: #d4af37;
  --color-tps06-gold: oklch(0.76 0.13 88);
  --color-tps06-gold2: #ffd479;
  --color-tps06-gold2: oklch(0.89 0.12 88);
  --color-tps06-goldedge: #a68a2c;
  --color-tps06-goldedge: oklch(0.62 0.11 88);
  --color-tps06-goldsoft: #4a3f1d;
  --color-tps06-goldsoft: oklch(0.36 0.06 88);
  --color-tps06-sheen: #ffd4791a;
  --color-tps06-sheen: oklch(0.89 0.12 88 / 0.06);
  --color-tps06-glow1: #d4af371f;
  --color-tps06-glow1: oklch(0.76 0.13 88 / 0.12);
  --color-tps06-glow2: #d4af371a;
  --color-tps06-glow2: oklch(0.76 0.13 88 / 0.1);
  --color-tps06-glow3: #d4af3726;
  --color-tps06-glow3: oklch(0.76 0.13 88 / 0.15);
  --color-tps06-glow4: #d4af374d;
  --color-tps06-glow4: oklch(0.76 0.13 88 / 0.3);
  --font-tps06-sans: 'Inter', system-ui, sans-serif;
  --font-tps06-display: 'Playfair Display', Georgia, serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the section is correctly sized in the moment before the
   browser build has compiled its utilities. */

.tps-06 {
  width: 100%;
  min-height: 100svh;
}
```
