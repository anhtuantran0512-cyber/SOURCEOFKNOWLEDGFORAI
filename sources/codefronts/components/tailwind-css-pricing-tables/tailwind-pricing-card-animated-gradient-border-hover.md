---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-pricing-tables/tailwind-pricing-card-animated-gradient-border-hover/"
title: "Tailwind Pricing Card with Animated Gradient Border on Hover"
section: "components"
category: "tailwind-css-pricing-tables"
category_name: "Tailwind CSS Pricing Tables"
description: "Hover a clean minimal card and a pink-to-violet-to-cyan border draws itself clockwise from twelve o'clock, then un-draws when you leave."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Pricing Card with Animated Gradient Border on Hover
Source: https://codefronts.com/components/tailwind-css-pricing-tables/tailwind-pricing-card-animated-gradient-border-hover/

Hover a clean minimal card and a pink-to-violet-to-cyan border draws itself clockwise from twelve o'clock, then un-draws when you leave. The border is one arbitrary [background:…] utility using the padding-box / border-box trick; its visible arc length is a registered @property percentage, transitioned by hover:[--tpt16-p:100%].
## HTML
```html
<section class="tpt-16 w-full min-h-svh grid place-items-center bg-tpt16-bg px-5 py-16 font-tpt16-sans text-tpt16-ink antialiased" aria-label="Pricing cards with gradient border draw effect">
  <div class="grid w-full max-w-5xl justify-items-center gap-10">
    <h2 class="text-center text-[clamp(26px,3.8vw,40px)] font-bold tracking-[-0.03em]">Sketch it. Ship it.</h2>
    <div class="grid w-full gap-5 md:grid-cols-3">
      <article class="flex flex-col gap-1.5 rounded-[20px] border-2 border-transparent p-8 [background:linear-gradient(white,white)_padding-box,conic-gradient(from_-90deg,var(--color-tpt16-c1),var(--color-tpt16-c2)_calc(var(--tpt16-p)*.5),var(--color-tpt16-c3)_var(--tpt16-p),var(--color-tpt16-line)_0)_border-box] [transition:--tpt16-p_800ms_cubic-bezier(.5,0,.2,1),box-shadow_350ms] hover:shadow-[0_20px_44px_-28px_var(--color-tpt16-c2)] hover:[--tpt16-p:100%] focus-within:[--tpt16-p:100%] motion-reduce:[transition:none]">
        <h3 class="text-[13px] font-semibold tracking-[0.08em] text-tpt16-mut uppercase">Sketch</h3>
        <p class="text-[44px] leading-tight font-bold tracking-[-0.035em]">$11<small class="text-[15px] font-medium tracking-normal text-tpt16-mut">/mo</small></p>
        <ul class="mt-3 mb-6 grid flex-1 content-start gap-2.5 text-sm text-tpt16-body *:flex *:gap-2.5 *:before:text-tpt16-c2 *:before:content-['→']"><li>3 boards</li><li>PNG export</li><li>Version history</li></ul>
        <a href="#" class="grid min-h-11 place-items-center rounded-xl bg-tpt16-ink text-sm font-semibold text-white no-underline transition hover:bg-linear-to-r hover:from-tpt16-c1 hover:via-tpt16-c2 hover:to-tpt16-c3-ink focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt16-c2">Start Sketch</a>
      </article>
      <article class="relative flex flex-col gap-1.5 rounded-[20px] border-2 border-transparent p-8 [--tpt16-p:22%] [background:linear-gradient(white,white)_padding-box,conic-gradient(from_-90deg,var(--color-tpt16-c1),var(--color-tpt16-c2)_calc(var(--tpt16-p)*.5),var(--color-tpt16-c3)_var(--tpt16-p),var(--color-tpt16-line)_0)_border-box] [transition:--tpt16-p_800ms_cubic-bezier(.5,0,.2,1),box-shadow_350ms] hover:shadow-[0_20px_44px_-28px_var(--color-tpt16-c2)] hover:[--tpt16-p:100%] focus-within:[--tpt16-p:100%] motion-reduce:[transition:none]">
        <span class="absolute -top-3 left-8 rounded-full bg-linear-to-r from-tpt16-c1 to-tpt16-c2 px-3 py-1 text-[10.5px] font-bold tracking-[0.08em] text-white uppercase">Most popular</span>
        <h3 class="text-[13px] font-semibold tracking-[0.08em] text-tpt16-c2 uppercase">Draft</h3>
        <p class="text-[44px] leading-tight font-bold tracking-[-0.035em]">$27<small class="text-[15px] font-medium tracking-normal text-tpt16-mut">/mo</small></p>
        <ul class="mt-3 mb-6 grid flex-1 content-start gap-2.5 text-sm text-tpt16-body *:flex *:gap-2.5 *:before:text-tpt16-c2 *:before:content-['→']"><li>Unlimited boards</li><li>SVG + PDF export</li><li>Comments &amp; mentions</li></ul>
        <a href="#" class="grid min-h-11 place-items-center rounded-xl bg-tpt16-ink text-sm font-semibold text-white no-underline transition hover:bg-linear-to-r hover:from-tpt16-c1 hover:via-tpt16-c2 hover:to-tpt16-c3-ink focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt16-c2">Start Draft</a>
      </article>
      <article class="flex flex-col gap-1.5 rounded-[20px] border-2 border-transparent p-8 [background:linear-gradient(white,white)_padding-box,conic-gradient(from_-90deg,var(--color-tpt16-c1),var(--color-tpt16-c2)_calc(var(--tpt16-p)*.5),var(--color-tpt16-c3)_var(--tpt16-p),var(--color-tpt16-line)_0)_border-box] [transition:--tpt16-p_800ms_cubic-bezier(.5,0,.2,1),box-shadow_350ms] hover:shadow-[0_20px_44px_-28px_var(--color-tpt16-c2)] hover:[--tpt16-p:100%] focus-within:[--tpt16-p:100%] motion-reduce:[transition:none]">
        <h3 class="text-[13px] font-semibold tracking-[0.08em] text-tpt16-mut uppercase">Studio</h3>
        <p class="text-[44px] leading-tight font-bold tracking-[-0.035em]">$68<small class="text-[15px] font-medium tracking-normal text-tpt16-mut">/mo</small></p>
        <ul class="mt-3 mb-6 grid flex-1 content-start gap-2.5 text-sm text-tpt16-body *:flex *:gap-2.5 *:before:text-tpt16-c2 *:before:content-['→']"><li>Everything in Draft</li><li>Team libraries</li><li>SSO</li></ul>
        <a href="#" class="grid min-h-11 place-items-center rounded-xl bg-tpt16-ink text-sm font-semibold text-white no-underline transition hover:bg-linear-to-r hover:from-tpt16-c1 hover:via-tpt16-c2 hover:to-tpt16-c3-ink focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt16-c2">Start Studio</a>
      </article>
    </div>
    <p aria-hidden="true" class="rounded-full border border-tpt16-line bg-white px-3.5 py-2 font-tpt16-mono text-[11.5px] text-tpt16-mut">@property --tpt16-p · hover:[--tpt16-p:100%] · padding-box / border-box</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpt16-bg: #fafafa;
  --color-tpt16-bg: oklch(0.985 0 0);
  --color-tpt16-ink: #191919;
  --color-tpt16-ink: oklch(0.21 0 0);
  --color-tpt16-body: #474747;
  --color-tpt16-body: oklch(0.42 0 0);
  --color-tpt16-mut: #6b6b6b;
  --color-tpt16-mut: oklch(0.53 0 0);
  --color-tpt16-line: #e8e8e8;
  --color-tpt16-line: oklch(0.93 0 0);
  --color-tpt16-c1: #e8338a;
  --color-tpt16-c1: oklch(0.62 0.23 355);
  --color-tpt16-c2: #6a3fe0;
  --color-tpt16-c2: oklch(0.53 0.22 285);
  --color-tpt16-c3: #19b3d6;
  --color-tpt16-c3: oklch(0.71 0.13 215);
  --color-tpt16-c3-ink: #0f7f9c;
  --color-tpt16-c3-ink: oklch(0.55 0.1 220);
  --font-tpt16-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tpt16-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities. */

.tpt-16 {
  width: 100%;
  min-height: 100svh;
}
/* Registered so the arc length can transition. */

@property --tpt16-p {
  syntax: '<percentage>';
  initial-value: 0%;
  inherits: false;
}
```
