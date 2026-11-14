---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-flip-cards/tailwind-pricing-plan-flip-card-gradient-price-feature-reveal/"
title: "Tailwind Pricing Plan Flip Card with Gradient Price & Feature Reveal"
section: "components"
category: "tailwind-css-flip-cards"
category_name: "Tailwind CSS Flip Cards"
description: "A SaaS pricing tier that lifts from its base rather than spinning around its centre: the top edge swings toward the camera on rotateX while the bottom stays…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Pricing Plan Flip Card with Gradient Price & Feature Reveal
Source: https://codefronts.com/components/tailwind-css-flip-cards/tailwind-pricing-plan-flip-card-gradient-price-feature-reveal/

A SaaS pricing tier that lifts from its base rather than spinning around its centre: the top edge swings toward the camera on rotateX while the bottom stays anchored, revealing the full feature ledger. The gradient price survives the port as bg-linear-135 bg-clip-text text-transparent, three utilities where the CSS needed four prefixed declarations.
## HTML
```html
<section class="tfc-02 w-full min-h-svh grid place-items-center bg-tfc02-bg font-tfc02-sans px-5 py-10 text-tfc02-ink">
  <div class="group relative w-[320px] h-[470px] [perspective:1200px] rounded-3xl has-[:focus-visible]:outline-2 has-[:focus-visible]:outline-tfc02-acc has-[:focus-visible]:outline-offset-4">
    <input id="tfc-02-flip" type="checkbox" class="peer sr-only">
    <label for="tfc-02-flip" class="absolute inset-0 z-20 cursor-pointer rounded-3xl"><span class="sr-only">Show the full Pro plan feature list</span></label>

    <div class="relative w-full h-full origin-bottom transition-transform duration-[850ms] ease-[cubic-bezier(.34,1.2,.4,1)] [transform-style:preserve-3d] group-hover:[transform:translateY(-100%)_rotateX(180deg)] group-has-checked:[transform:translateY(-100%)_rotateX(180deg)] group-has-[:focus-visible]:[transform:translateY(-100%)_rotateX(180deg)] motion-reduce:transition-none">

      <div class="absolute inset-0 flex flex-col rounded-3xl overflow-hidden bg-linear-160 from-tfc02-panel to-tfc02-panel2 border border-tfc02-edge shadow-[0_1px_2px_oklch(0_0_0/0.45),0_24px_50px_-16px_oklch(0.55_0.15_165/0.25)] [backface-visibility:hidden] [-webkit-backface-visibility:hidden]">
        <div aria-hidden="true" class="pointer-events-none absolute -top-16 left-1/2 size-52 -translate-x-1/2 bg-[radial-gradient(circle,oklch(0.7_0.15_165/0.25),transparent_70%)]"></div>
        <div class="relative px-7 pt-8 pb-6 text-center">
          <div class="mx-auto mb-4 grid size-14 place-items-center rounded-2xl border border-tfc02-edge bg-linear-135 from-tfc02-acc/20 to-tfc02-acc/5">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" class="text-tfc02-acc" aria-hidden="true"><path d="M5 19l3-8 8-3-3 8-8 3z"/><path d="M12 12l6-6"/></svg>
          </div>
          <p class="mb-2 text-[11px] font-bold uppercase tracking-[0.2em] text-tfc02-acc">Pro Plan</p>
          <p class="flex items-baseline justify-center gap-1">
            <span class="mt-1.5 text-xl font-bold text-tfc02-muted">$</span>
            <span class="bg-linear-135 from-tfc02-acc to-tfc02-acc3 bg-clip-text text-[52px] font-black leading-none tracking-[-0.03em] text-transparent">49</span>
          </p>
          <p class="mt-1.5 text-[13px] text-tfc02-muted">per month, billed annually</p>
        </div>
        <div class="mx-7 h-px bg-linear-to-r from-transparent via-tfc02-acc/25 to-transparent"></div>
        <div class="flex-1 px-7 py-6">
          <p class="mb-3.5 text-[10px] uppercase tracking-[0.12em] text-tfc02-dim">Includes</p>
          <ul class="flex flex-col gap-2.5 text-[13px] text-tfc02-muted">
            <li class="flex items-center gap-2.5 before:size-1.5 before:shrink-0 before:rounded-full before:bg-tfc02-acc">Unlimited projects</li>
            <li class="flex items-center gap-2.5 before:size-1.5 before:shrink-0 before:rounded-full before:bg-tfc02-acc">Advanced analytics</li>
            <li class="flex items-center gap-2.5 before:size-1.5 before:shrink-0 before:rounded-full before:bg-tfc02-acc">Priority support</li>
            <li class="flex items-center gap-2.5 before:size-1.5 before:shrink-0 before:rounded-full before:bg-tfc02-acc">Custom domains</li>
          </ul>
        </div>
        <p class="px-7 pb-6 text-center text-[11px] tracking-[0.08em] text-tfc02-dim">Hover, tap or press Space for all features</p>
      </div>

      <div class="absolute inset-0 flex flex-col rounded-3xl overflow-hidden p-7 bg-linear-160 from-tfc02-back to-tfc02-back2 border border-tfc02-edge2 shadow-[0_1px_2px_oklch(0_0_0/0.45),0_24px_50px_-16px_oklch(0.5_0.2_295/0.3)] [transform:rotateX(180deg)] [backface-visibility:hidden] [-webkit-backface-visibility:hidden]">
        <h3 class="mb-5 text-[13px] font-bold uppercase tracking-[0.12em] text-tfc02-purple">Everything in Pro</h3>
        <ul class="flex flex-1 flex-col gap-2.5 text-[13px] text-tfc02-ink/80">
          <li class="flex items-center gap-3 rounded-xl border border-white/6 bg-white/3 px-3.5 py-2.5"><span class="grid size-5 shrink-0 place-items-center rounded-md border border-tfc02-acc/30 bg-tfc02-acc/15"><svg viewBox="0 0 12 12" class="size-3 fill-none stroke-tfc02-acc stroke-[2.5]" aria-hidden="true"><polyline points="2,6 5,9 10,3"/></svg></span>Unlimited projects &amp; workspaces</li>
          <li class="flex items-center gap-3 rounded-xl border border-white/6 bg-white/3 px-3.5 py-2.5"><span class="grid size-5 shrink-0 place-items-center rounded-md border border-tfc02-acc/30 bg-tfc02-acc/15"><svg viewBox="0 0 12 12" class="size-3 fill-none stroke-tfc02-acc stroke-[2.5]" aria-hidden="true"><polyline points="2,6 5,9 10,3"/></svg></span>Advanced real-time analytics</li>
          <li class="flex items-center gap-3 rounded-xl border border-white/6 bg-white/3 px-3.5 py-2.5"><span class="grid size-5 shrink-0 place-items-center rounded-md border border-tfc02-acc/30 bg-tfc02-acc/15"><svg viewBox="0 0 12 12" class="size-3 fill-none stroke-tfc02-acc stroke-[2.5]" aria-hidden="true"><polyline points="2,6 5,9 10,3"/></svg></span>Custom domain mapping</li>
          <li class="flex items-center gap-3 rounded-xl border border-white/6 bg-white/3 px-3.5 py-2.5"><span class="grid size-5 shrink-0 place-items-center rounded-md border border-tfc02-acc/30 bg-tfc02-acc/15"><svg viewBox="0 0 12 12" class="size-3 fill-none stroke-tfc02-acc stroke-[2.5]" aria-hidden="true"><polyline points="2,6 5,9 10,3"/></svg></span>API access (10k req/day)</li>
          <li class="flex items-center gap-3 rounded-xl border border-white/6 bg-white/3 px-3.5 py-2.5"><span class="grid size-5 shrink-0 place-items-center rounded-md border border-tfc02-acc/30 bg-tfc02-acc/15"><svg viewBox="0 0 12 12" class="size-3 fill-none stroke-tfc02-acc stroke-[2.5]" aria-hidden="true"><polyline points="2,6 5,9 10,3"/></svg></span>Priority 4h support SLA</li>
          <li class="flex items-center gap-3 rounded-xl border border-tfc02-gold/20 bg-tfc02-gold/6 px-3.5 py-2.5"><span class="grid size-5 shrink-0 place-items-center rounded-md border border-tfc02-gold/30 bg-tfc02-gold/15"><svg viewBox="0 0 12 12" class="size-3 fill-none stroke-tfc02-gold stroke-[2.5]" aria-hidden="true"><polyline points="2,6 5,9 10,3"/></svg></span>AI content generation (50/mo)</li>
          <li class="flex items-center gap-3 rounded-xl border border-tfc02-gold/20 bg-tfc02-gold/6 px-3.5 py-2.5"><span class="grid size-5 shrink-0 place-items-center rounded-md border border-tfc02-gold/30 bg-tfc02-gold/15"><svg viewBox="0 0 12 12" class="size-3 fill-none stroke-tfc02-gold stroke-[2.5]" aria-hidden="true"><polyline points="2,6 5,9 10,3"/></svg></span>White-label exports</li>
        </ul>
        <button type="button" class="relative z-30 mt-5 min-h-11 w-full rounded-xl bg-linear-135 from-tfc02-acc to-tfc02-acc2 text-sm font-extrabold tracking-[0.04em] text-black transition-transform duration-150 hover:-translate-y-px focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2 motion-reduce:hover:translate-y-0">Get Started &mdash; $49/mo</button>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfc02-bg: #050d0a;
  --color-tfc02-bg: oklch(0.14 0.02 165);
  --color-tfc02-panel: #071a12;
  --color-tfc02-panel: oklch(0.19 0.04 165);
  --color-tfc02-panel2: #0a2e1e;
  --color-tfc02-panel2: oklch(0.26 0.06 165);
  --color-tfc02-back: #0a0a1e;
  --color-tfc02-back: oklch(0.17 0.04 285);
  --color-tfc02-back2: #0d1533;
  --color-tfc02-back2: oklch(0.21 0.07 275);
  --color-tfc02-acc: #10b981;
  --color-tfc02-acc: oklch(0.72 0.16 165);
  --color-tfc02-acc2: #059669;
  --color-tfc02-acc2: oklch(0.61 0.14 165);
  --color-tfc02-acc3: #34d399;
  --color-tfc02-acc3: oklch(0.8 0.14 165);
  --color-tfc02-gold: #f59e0b;
  --color-tfc02-gold: oklch(0.77 0.16 70);
  --color-tfc02-purple: #8b5cf6;
  --color-tfc02-purple: oklch(0.63 0.2 295);
  --color-tfc02-ink: #f0fdf4;
  --color-tfc02-ink: oklch(0.98 0.02 160);
  --color-tfc02-muted: #9fd9bd;
  --color-tfc02-muted: oklch(0.82 0.06 165);
  --color-tfc02-dim: #77a691;
  --color-tfc02-dim: oklch(0.68 0.04 165);
  --color-tfc02-edge: #17553c;
  --color-tfc02-edge: oklch(0.4 0.09 165);
  --color-tfc02-edge2: #453089;
  --color-tfc02-edge2: oklch(0.4 0.14 292);
  --font-tfc02-sans: 'Sora', system-ui, sans-serif;
}

.tfc-02 {
  width: 100%;
  min-height: 100svh;
}

@media (prefers-reduced-motion: reduce) {
  .tfc-02 * {
    transition-duration: 1ms !important;
  }
}
```
