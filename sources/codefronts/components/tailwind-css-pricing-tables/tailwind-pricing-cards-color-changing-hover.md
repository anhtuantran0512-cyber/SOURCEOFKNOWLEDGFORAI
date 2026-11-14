---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-pricing-tables/tailwind-pricing-cards-color-changing-hover/"
title: "Tailwind Pricing Cards with Color-Changing Hover Themes"
section: "components"
category: "tailwind-css-pricing-tables"
category_name: "Tailwind CSS Pricing Tables"
description: "Each tier carries its own hue."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Pricing Cards with Color-Changing Hover Themes
Source: https://codefronts.com/components/tailwind-css-pricing-tables/tailwind-pricing-cards-color-changing-hover/

Each tier carries its own hue. Hover a card and its colour floods the plan name, checkmarks, divider and CTA — and the whole section's backdrop tints to match. Every accent is derived as oklch(L var(--tpt09-c) var(--tpt09-h)) in arbitrary utilities; registering the chroma and the wash hue with @property means the colour itself glides, not just the properties that use it.
## HTML
```html
<section class="tpt-09 group/p relative isolate w-full min-h-svh grid place-items-center overflow-hidden bg-tpt09-bg px-5 py-16 font-tpt09-sans text-tpt09-ink antialiased [transition:--tpt09-wash_700ms] has-[[data-h='160']:hover]:[--tpt09-wash:160] has-[[data-h='160']:focus-within]:[--tpt09-wash:160] has-[[data-h='280']:hover]:[--tpt09-wash:280] has-[[data-h='280']:focus-within]:[--tpt09-wash:280] has-[[data-h='40']:hover]:[--tpt09-wash:40] has-[[data-h='40']:focus-within]:[--tpt09-wash:40]" aria-label="Pricing cards with per-plan colour themes">
  <div aria-hidden="true" class="pointer-events-none absolute inset-0 -z-10 bg-[radial-gradient(60%_80%_at_50%_110%,oklch(0.45_0.16_var(--tpt09-wash)/0.45),transparent_70%)] opacity-0 transition-opacity duration-700 group-has-[article:hover]/p:opacity-100 group-has-[article:focus-within]/p:opacity-100"></div>
  <div class="grid w-full max-w-5xl justify-items-center gap-10">
    <h2 class="text-center text-[clamp(26px,3.8vw,40px)] font-bold tracking-[-0.03em]">A plan for every palette</h2>
    <div class="grid w-full gap-5 md:grid-cols-3">
      <article data-h="160" class="flex flex-col gap-4 rounded-[20px] border-[1.5px] border-[oklch(0.4_calc(var(--tpt09-c)*2)_var(--tpt09-h))] bg-tpt09-card p-7 [transition:--tpt09-c_500ms,translate_500ms] [--tpt09-h:160] hover:-translate-y-1.5 hover:[--tpt09-c:0.17] focus-within:[--tpt09-c:0.17] motion-reduce:transition-none motion-reduce:hover:translate-y-0">
        <h3 class="text-[13px] font-bold tracking-[0.1em] text-[oklch(0.8_var(--tpt09-c)_var(--tpt09-h))] uppercase">Mint</h3>
        <p class="text-[44px] leading-none font-bold tracking-[-0.035em]">$12<small class="text-[15px] font-medium tracking-normal text-tpt09-mut">/mo</small></p>
        <hr class="h-[1.5px] border-0 bg-[oklch(0.45_calc(var(--tpt09-c)*1.6)_var(--tpt09-h))]">
        <ul class="grid flex-1 content-start gap-2.5 text-sm text-tpt09-body *:flex *:gap-2.5 *:before:font-bold *:before:text-[oklch(0.8_var(--tpt09-c)_var(--tpt09-h))] *:before:content-['✓']"><li>Personal licence</li><li>20 exports / month</li><li>1080p renders</li></ul>
        <a href="#" class="grid min-h-11 place-items-center rounded-xl bg-[oklch(0.34_calc(var(--tpt09-c)*1.2)_var(--tpt09-h))] text-sm font-bold text-white no-underline focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-[oklch(0.8_0.15_var(--tpt09-h))]">Get Mint</a>
      </article>
      <article data-h="280" class="flex flex-col gap-4 rounded-[20px] border-[1.5px] border-[oklch(0.4_calc(var(--tpt09-c)*2)_var(--tpt09-h))] bg-tpt09-card p-7 [transition:--tpt09-c_500ms,translate_500ms] [--tpt09-h:280] hover:-translate-y-1.5 hover:[--tpt09-c:0.17] focus-within:[--tpt09-c:0.17] motion-reduce:transition-none motion-reduce:hover:translate-y-0">
        <h3 class="text-[13px] font-bold tracking-[0.1em] text-[oklch(0.8_var(--tpt09-c)_var(--tpt09-h))] uppercase">Violet</h3>
        <p class="text-[44px] leading-none font-bold tracking-[-0.035em]">$32<small class="text-[15px] font-medium tracking-normal text-tpt09-mut">/mo</small></p>
        <hr class="h-[1.5px] border-0 bg-[oklch(0.45_calc(var(--tpt09-c)*1.6)_var(--tpt09-h))]">
        <ul class="grid flex-1 content-start gap-2.5 text-sm text-tpt09-body *:flex *:gap-2.5 *:before:font-bold *:before:text-[oklch(0.8_var(--tpt09-c)_var(--tpt09-h))] *:before:content-['✓']"><li>Commercial licence</li><li>Unlimited exports</li><li>4K renders</li><li>Brand kits</li></ul>
        <a href="#" class="grid min-h-11 place-items-center rounded-xl bg-[oklch(0.34_calc(var(--tpt09-c)*1.2)_var(--tpt09-h))] text-sm font-bold text-white no-underline focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-[oklch(0.8_0.15_var(--tpt09-h))]">Get Violet</a>
      </article>
      <article data-h="40" class="flex flex-col gap-4 rounded-[20px] border-[1.5px] border-[oklch(0.4_calc(var(--tpt09-c)*2)_var(--tpt09-h))] bg-tpt09-card p-7 [transition:--tpt09-c_500ms,translate_500ms] [--tpt09-h:40] hover:-translate-y-1.5 hover:[--tpt09-c:0.17] focus-within:[--tpt09-c:0.17] motion-reduce:transition-none motion-reduce:hover:translate-y-0">
        <h3 class="text-[13px] font-bold tracking-[0.1em] text-[oklch(0.8_var(--tpt09-c)_var(--tpt09-h))] uppercase">Amber</h3>
        <p class="text-[44px] leading-none font-bold tracking-[-0.035em]">$79<small class="text-[15px] font-medium tracking-normal text-tpt09-mut">/mo</small></p>
        <hr class="h-[1.5px] border-0 bg-[oklch(0.45_calc(var(--tpt09-c)*1.6)_var(--tpt09-h))]">
        <ul class="grid flex-1 content-start gap-2.5 text-sm text-tpt09-body *:flex *:gap-2.5 *:before:font-bold *:before:text-[oklch(0.8_var(--tpt09-c)_var(--tpt09-h))] *:before:content-['✓']"><li>Team licence</li><li>Shared libraries</li><li>8K renders</li></ul>
        <a href="#" class="grid min-h-11 place-items-center rounded-xl bg-[oklch(0.34_calc(var(--tpt09-c)*1.2)_var(--tpt09-h))] text-sm font-bold text-white no-underline focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-[oklch(0.8_0.15_var(--tpt09-h))]">Get Amber</a>
      </article>
    </div>
    <p aria-hidden="true" class="rounded-full border border-white/12 px-3.5 py-2 font-tpt09-mono text-[11.5px] text-tpt09-mut">@property --tpt09-c · oklch(L var(--c) var(--h)) · has-[[data-h]:hover]:</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpt09-bg: #0f0f13;
  --color-tpt09-bg: oklch(0.17 0.008 280);
  --color-tpt09-card: #17171d;
  --color-tpt09-card: oklch(0.215 0.01 280);
  --color-tpt09-ink: #ecedf2;
  --color-tpt09-ink: oklch(0.95 0.006 280);
  --color-tpt09-body: #c0c3d0;
  --color-tpt09-body: oklch(0.83 0.015 280);
  --color-tpt09-mut: #9296a6;
  --color-tpt09-mut: oklch(0.69 0.018 280);
  --font-tpt09-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tpt09-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities. */

.tpt-09 {
  width: 100%;
  min-height: 100svh;
}
/* Registered so they interpolate: chroma lifts on hover, wash hue sweeps between cards. */

@property --tpt09-c {
  syntax: '<number>';
  initial-value: 0.02;
  inherits: true;
}

@property --tpt09-wash {
  syntax: '<number>';
  initial-value: 280;
  inherits: true;
}
```
