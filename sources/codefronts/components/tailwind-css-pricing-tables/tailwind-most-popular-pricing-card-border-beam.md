---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-pricing-tables/tailwind-most-popular-pricing-card-border-beam/"
title: "Tailwind \"Most Popular\" Pricing Card with Animated Border Beam"
section: "components"
category: "tailwind-css-pricing-tables"
category_name: "Tailwind CSS Pricing Tables"
description: "A comet of light orbits the &ldquo;Most popular&rdquo; card — the border-beam effect every SaaS landing page wants — drawn with the two-background…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind "Most Popular" Pricing Card with Animated Border Beam
Source: https://codefronts.com/components/tailwind-css-pricing-tables/tailwind-most-popular-pricing-card-border-beam/

A comet of light orbits the &ldquo;Most popular&rdquo; card — the border-beam effect every SaaS landing page wants — drawn with the two-background padding-box / border-box trick and spun by animating one registered @property angle. The beam is a single arbitrary [background:…] utility; a blurred before: copy supplies the glow. No mask, no SVG.
## HTML
```html
<section class="tpt-06 w-full min-h-svh grid place-items-center bg-tpt06-bg bg-[radial-gradient(60%_50%_at_50%_45%,var(--color-tpt06-glow),transparent)] px-5 py-16 font-tpt06-sans text-tpt06-ink antialiased" aria-label="Pricing with highlighted most popular plan">
  <div class="isolate grid w-full max-w-5xl justify-items-center gap-10">
    <div class="grid w-full gap-5 md:grid-cols-3 md:items-center">
      <article class="flex flex-col gap-4 rounded-[20px] border border-tpt06-line bg-tpt06-card p-7">
        <h3 class="text-[13px] font-semibold tracking-[0.08em] text-tpt06-mut uppercase">Indie</h3>
        <p class="text-[44px] leading-none font-bold tracking-[-0.035em]">$10<small class="text-[15px] font-medium tracking-normal text-tpt06-mut">/mo</small></p>
        <ul class="grid flex-1 content-start gap-2.5 text-sm text-tpt06-body *:flex *:gap-2.5 *:before:font-bold *:before:text-tpt06-beam *:before:content-['✓']"><li>1 product</li><li>Standard checkout</li><li>2% transaction fee</li></ul>
        <a href="#" class="grid min-h-11 place-items-center rounded-xl border border-tpt06-line text-sm font-semibold text-tpt06-ink no-underline transition-colors hover:border-tpt06-beam focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt06-beam">Go Indie</a>
      </article>
      <article class="relative flex animate-tpt06-spin flex-col gap-4 rounded-[20px] border-2 border-transparent px-7 py-9 [background:linear-gradient(var(--color-tpt06-card-hi),var(--color-tpt06-card-hi))_padding-box,conic-gradient(from_var(--tpt06-a),var(--color-tpt06-line)_0deg_300deg,var(--color-tpt06-beam)_340deg,white_350deg,var(--color-tpt06-beam)_355deg,var(--color-tpt06-line)_360deg)_border-box] before:pointer-events-none before:absolute before:-inset-[2px] before:-z-10 before:rounded-[inherit] before:opacity-50 before:blur-xl before:content-[''] before:[background:conic-gradient(from_var(--tpt06-a),transparent_0deg_300deg,var(--color-tpt06-beam)_345deg,transparent_360deg)] motion-reduce:animate-none">
        <span class="w-max rounded-full border border-tpt06-beam/40 bg-tpt06-beam/12 px-3 py-1 text-[10.5px] font-bold tracking-[0.1em] text-tpt06-beam uppercase">Most popular</span>
        <h3 class="text-[13px] font-semibold tracking-[0.08em] text-tpt06-mut uppercase">Business</h3>
        <p class="text-[48px] leading-none font-bold tracking-[-0.035em]">$29<small class="text-[15px] font-medium tracking-normal text-tpt06-mut">/mo</small></p>
        <ul class="grid flex-1 content-start gap-2.5 text-sm text-tpt06-body *:flex *:gap-2.5 *:before:font-bold *:before:text-tpt06-beam *:before:content-['✓']"><li>Unlimited products</li><li>Custom checkout</li><li>0.5% transaction fee</li><li>Subscriptions &amp; trials</li></ul>
        <a href="#" class="grid min-h-11 place-items-center rounded-xl bg-tpt06-beam text-sm font-bold text-tpt06-on-beam no-underline transition hover:brightness-110 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt06-beam">Go Business</a>
      </article>
      <article class="flex flex-col gap-4 rounded-[20px] border border-tpt06-line bg-tpt06-card p-7">
        <h3 class="text-[13px] font-semibold tracking-[0.08em] text-tpt06-mut uppercase">Platform</h3>
        <p class="text-[44px] leading-none font-bold tracking-[-0.035em]">$85<small class="text-[15px] font-medium tracking-normal text-tpt06-mut">/mo</small></p>
        <ul class="grid flex-1 content-start gap-2.5 text-sm text-tpt06-body *:flex *:gap-2.5 *:before:font-bold *:before:text-tpt06-beam *:before:content-['✓']"><li>Everything in Business</li><li>Marketplace payouts</li><li>0% transaction fee</li></ul>
        <a href="#" class="grid min-h-11 place-items-center rounded-xl border border-tpt06-line text-sm font-semibold text-tpt06-ink no-underline transition-colors hover:border-tpt06-beam focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt06-beam">Go Platform</a>
      </article>
    </div>
    <p aria-hidden="true" class="rounded-full border border-white/12 px-3.5 py-2 font-tpt06-mono text-[11.5px] text-tpt06-mut">@property &lt;angle&gt; · padding-box / border-box · animate-tpt06-spin</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpt06-bg: #0b0d14;
  --color-tpt06-bg: oklch(0.16 0.015 270);
  --color-tpt06-glow: #2a230f80;
  --color-tpt06-glow: oklch(0.27 0.04 85 / 0.5);
  --color-tpt06-card: #151824;
  --color-tpt06-card: oklch(0.21 0.022 270);
  --color-tpt06-card-hi: #191d2b;
  --color-tpt06-card-hi: oklch(0.235 0.025 270);
  --color-tpt06-line: #2a2f42;
  --color-tpt06-line: oklch(0.31 0.03 270);
  --color-tpt06-ink: #edf0f7;
  --color-tpt06-ink: oklch(0.95 0.008 270);
  --color-tpt06-body: #c2c7d8;
  --color-tpt06-body: oklch(0.83 0.02 270);
  --color-tpt06-mut: #9aa1b8;
  --color-tpt06-mut: oklch(0.72 0.025 270);
  --color-tpt06-beam: #f2c14e;
  --color-tpt06-beam: oklch(0.83 0.15 85);
  --color-tpt06-on-beam: #1d1603;
  --color-tpt06-on-beam: oklch(0.2 0.03 85);
  --font-tpt06-sans: 'Geist', system-ui, sans-serif;
  --font-tpt06-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tpt06-spin: tpt06-spin 4s linear infinite;

  @keyframes tpt06-spin {
    to {
      --tpt06-a: 570deg;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities. */

.tpt-06 {
  width: 100%;
  min-height: 100svh;
}
/* Registered so the angle interpolates; inherits:true lets the before: glow read the same value.
   Initial 210deg is also the frozen reduced-motion pose. */

@property --tpt06-a {
  syntax: '<angle>';
  initial-value: 210deg;
  inherits: true;
}
```
