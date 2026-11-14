---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-claymorphism/tailwind-pricing-table-monthly-yearly-toggle-clay/"
title: "Tailwind Pricing Table with Monthly/Yearly Toggle (Clay Style)"
section: "design-styles"
category: "tailwind-css-claymorphism"
category_name: "Tailwind CSS Claymorphism"
description: "Three plans where hierarchy comes from depth, not a coloured border: the popular tier floats a full elevation tier above its neighbours, is physically…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Pricing Table with Monthly/Yearly Toggle (Clay Style)
Source: https://codefronts.com/design-styles/tailwind-css-claymorphism/tailwind-pricing-table-monthly-yearly-toggle-clay/

Three plans where hierarchy comes from depth, not a coloured border: the popular tier floats a full elevation tier above its neighbours, is physically larger, and wears a clay ribbon. The billing switch is a checkbox read by group-has-[#tcl-15-billing:checked]/demo:, so prices change with no script. New: yearly shows the monthly equivalent with a "billed $182 yearly" line — the pattern buyers compare on.
## HTML
```html
<section class="tcl-15 group/demo w-full min-h-svh grid place-items-center bg-tcl15-bg bg-[radial-gradient(85%_55%_at_50%_0%,var(--color-tcl15-glow),transparent_66%)] px-5 py-14 font-tcl15-sans text-tcl15-ink" aria-label="Clay pricing table with raised popular tier demo">
  <div class="grid w-full justify-items-center gap-[clamp(26px,4vw,40px)]">
    <header class="grid justify-items-center gap-4.5 text-center">
      <h2 class="font-tcl15-display text-[clamp(28px,4.2vw,42px)] font-extrabold leading-[1.05] tracking-[-0.03em] text-balance">Plans that feel their weight</h2>
      <label class="inline-flex min-h-13 cursor-pointer items-center gap-3.5 rounded-full bg-tcl15-soft px-5 text-sm font-semibold shadow-tcl15-pill has-focus-visible:outline-3 has-focus-visible:outline-offset-3 has-focus-visible:outline-tcl15-ink">
        <span class="text-tcl15-ink transition-colors group-has-[#tcl-15-billing:checked]/demo:text-tcl15-mut">Monthly</span>
        <input type="checkbox" role="switch" id="tcl-15-billing" class="peer sr-only" aria-label="Bill yearly">
        <span aria-hidden="true" class="relative h-7.5 w-13 rounded-full bg-tcl15-well shadow-tcl15-track">
          <span class="absolute top-0.75 left-0.75 size-6 rounded-full bg-white shadow-tcl15-knob transition-[translate,background-color] duration-300 ease-[cubic-bezier(.34,1.5,.5,1)] group-has-[#tcl-15-billing:checked]/demo:translate-x-5.5 group-has-[#tcl-15-billing:checked]/demo:bg-tcl15-accent motion-reduce:transition-none"></span>
        </span>
        <span class="inline-flex items-center gap-2 text-tcl15-mut transition-colors group-has-[#tcl-15-billing:checked]/demo:text-tcl15-ink">Yearly <b class="rounded-full bg-tcl15-accent/45 px-2.25 py-1.25 text-[10.5px] font-bold uppercase tracking-[0.08em] text-tcl15-ink opacity-60 transition-[opacity,scale] duration-300 ease-[cubic-bezier(.34,1.5,.5,1)] group-has-[#tcl-15-billing:checked]/demo:scale-106 group-has-[#tcl-15-billing:checked]/demo:opacity-100">save 20%</b></span>
      </label>
    </header>
    <div class="grid w-full max-w-[1020px] grid-cols-[repeat(auto-fit,minmax(250px,1fr))] items-center gap-[clamp(20px,3vw,28px)]">
      <article class="grid content-start gap-2.75 rounded-[38px] bg-tcl15-clay p-[clamp(24px,3vw,32px)] shadow-tcl15-tier2 transition-[translate] duration-[400ms] ease-[cubic-bezier(.34,1.3,.5,1)] hover:-translate-y-1.5">
        <p class="text-xs font-bold uppercase tracking-[0.15em] text-tcl15-ink/70">Starter</p>
        <p class="font-tcl15-display text-[clamp(32px,4.4vw,42px)] leading-none font-extrabold tracking-[-0.04em] tabular-nums">$0<em class="text-[15px] font-semibold not-italic tracking-normal text-tcl15-mut">/mo</em></p>
        <p class="text-[12.5px] text-tcl15-mut">Free forever</p>
        <p class="text-[13.5px] leading-normal text-tcl15-ink/85 text-pretty">Every snippet, no account needed.</p>
        <ul class="mt-1.5 mb-0.5 grid gap-1.75 rounded-3xl bg-tcl15-well px-4.5 py-4 text-[13.5px] shadow-tcl15-feats">
          <li class="flex items-center gap-2.5 before:size-2 before:flex-none before:rounded-full before:bg-tcl15-dot">All 20 demos</li><li class="flex items-center gap-2.5 before:size-2 before:flex-none before:rounded-full before:bg-tcl15-dot">Copy any snippet</li><li class="flex items-center gap-2.5 before:size-2 before:flex-none before:rounded-full before:bg-tcl15-dot">Community support</li>
        </ul>
        <button type="button" class="mt-1.5 min-h-13 cursor-pointer rounded-3xl bg-tcl15-soft px-5.5 text-[14.5px] font-bold shadow-tcl15-btn transition-[translate,scale,box-shadow] duration-200 ease-[cubic-bezier(.2,.8,.3,1.4)] hover:-translate-y-0.75 active:translate-y-0.75 active:scale-y-94 active:shadow-tcl15-press focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-tcl15-ink">Start free</button>
      </article>
      <article class="relative z-10 grid content-start gap-2.75 rounded-[38px] bg-tcl15-pop p-[clamp(24px,3vw,32px)] pt-[clamp(32px,3.6vw,42px)] shadow-tcl15-tier4 transition-[translate] duration-[400ms] ease-[cubic-bezier(.34,1.3,.5,1)] hover:-translate-y-2.5 md:scale-104">
        <span class="absolute -top-3.5 left-1/2 -translate-x-1/2 rounded-full bg-tcl15-ribbon px-4 py-2 text-[11px] font-bold uppercase tracking-[0.12em] whitespace-nowrap text-white shadow-tcl15-ribbon">Most popular</span>
        <p class="text-xs font-bold uppercase tracking-[0.15em] text-tcl15-ink/70">Pro</p>
        <p class="font-tcl15-display text-[clamp(32px,4.4vw,42px)] leading-none font-extrabold tracking-[-0.04em] tabular-nums"><span class="group-has-[#tcl-15-billing:checked]/demo:hidden">$19</span><span class="hidden group-has-[#tcl-15-billing:checked]/demo:inline">$15</span><em class="text-[15px] font-semibold not-italic tracking-normal text-tcl15-ink/70">/mo</em></p>
        <p class="text-[12.5px] text-tcl15-ink/75"><span class="group-has-[#tcl-15-billing:checked]/demo:hidden">Billed monthly</span><span class="hidden group-has-[#tcl-15-billing:checked]/demo:inline">Billed $182 yearly</span></p>
        <p class="text-[13.5px] leading-normal text-tcl15-ink/85 text-pretty">Figma tokens, dark-mode variants and the clay generator.</p>
        <ul class="mt-1.5 mb-0.5 grid gap-1.75 rounded-3xl bg-tcl15-popwell px-4.5 py-4 text-[13.5px] shadow-tcl15-feats">
          <li class="flex items-center gap-2.5 before:size-2 before:flex-none before:rounded-full before:bg-tcl15-dot">Token &amp; Tailwind presets</li><li class="flex items-center gap-2.5 before:size-2 before:flex-none before:rounded-full before:bg-tcl15-dot">Dark-mode recalibration</li><li class="flex items-center gap-2.5 before:size-2 before:flex-none before:rounded-full before:bg-tcl15-dot">Figma clay library</li><li class="flex items-center gap-2.5 before:size-2 before:flex-none before:rounded-full before:bg-tcl15-dot">Priority answers</li>
        </ul>
        <button type="button" class="mt-1.5 min-h-13 cursor-pointer rounded-3xl bg-tcl15-accent px-5.5 text-[14.5px] font-bold text-tcl15-accentink shadow-tcl15-btn transition-[translate,scale,box-shadow] duration-200 ease-[cubic-bezier(.2,.8,.3,1.4)] hover:-translate-y-0.75 active:translate-y-0.75 active:scale-y-94 active:shadow-tcl15-press focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-tcl15-ink">Get Pro</button>
      </article>
      <article class="grid content-start gap-2.75 rounded-[38px] bg-tcl15-clay p-[clamp(24px,3vw,32px)] shadow-tcl15-tier2 transition-[translate] duration-[400ms] ease-[cubic-bezier(.34,1.3,.5,1)] hover:-translate-y-1.5">
        <p class="text-xs font-bold uppercase tracking-[0.15em] text-tcl15-ink/70">Team</p>
        <p class="font-tcl15-display text-[clamp(32px,4.4vw,42px)] leading-none font-extrabold tracking-[-0.04em] tabular-nums"><span class="group-has-[#tcl-15-billing:checked]/demo:hidden">$49</span><span class="hidden group-has-[#tcl-15-billing:checked]/demo:inline">$39</span><em class="text-[15px] font-semibold not-italic tracking-normal text-tcl15-mut">/mo</em></p>
        <p class="text-[12.5px] text-tcl15-mut"><span class="group-has-[#tcl-15-billing:checked]/demo:hidden">Billed monthly</span><span class="hidden group-has-[#tcl-15-billing:checked]/demo:inline">Billed $470 yearly</span></p>
        <p class="text-[13.5px] leading-normal text-tcl15-ink/85 text-pretty">Shared design tokens for the whole product team.</p>
        <ul class="mt-1.5 mb-0.5 grid gap-1.75 rounded-3xl bg-tcl15-well px-4.5 py-4 text-[13.5px] shadow-tcl15-feats">
          <li class="flex items-center gap-2.5 before:size-2 before:flex-none before:rounded-full before:bg-tcl15-dot">10 seats</li><li class="flex items-center gap-2.5 before:size-2 before:flex-none before:rounded-full before:bg-tcl15-dot">Design-system audit</li><li class="flex items-center gap-2.5 before:size-2 before:flex-none before:rounded-full before:bg-tcl15-dot">Onboarding session</li>
        </ul>
        <button type="button" class="mt-1.5 min-h-13 cursor-pointer rounded-3xl bg-tcl15-soft px-5.5 text-[14.5px] font-bold shadow-tcl15-btn transition-[translate,scale,box-shadow] duration-200 ease-[cubic-bezier(.2,.8,.3,1.4)] hover:-translate-y-0.75 active:translate-y-0.75 active:scale-y-94 active:shadow-tcl15-press focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-tcl15-ink">Talk to us</button>
      </article>
    </div>
    <p aria-hidden="true" class="rounded-full bg-white/55 px-4 py-2 text-center font-tcl15-mono text-[11.5px] text-tcl15-mut">hierarchy from elevation + scale · group-has-[#billing:checked]/demo: price swap · tabular-nums</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcl15-bg: #deedfe;
  --color-tcl15-bg: oklch(0.94 0.028 250);
  --color-tcl15-glow: #e4f8ff;
  --color-tcl15-glow: oklch(0.97 0.03 240);
  --color-tcl15-clay: #c8e1fb;
  --color-tcl15-clay: oklch(0.9 0.045 250);
  --color-tcl15-pop: #9fe4fa;
  --color-tcl15-pop: oklch(0.88 0.075 220);
  --color-tcl15-soft: #e2f0ff;
  --color-tcl15-soft: oklch(0.95 0.025 250);
  --color-tcl15-well: #bfd7f1;
  --color-tcl15-well: oklch(0.87 0.045 250);
  --color-tcl15-popwell: #9bd9ef;
  --color-tcl15-popwell: oklch(0.85 0.07 222);
  --color-tcl15-accent: #34dde5;
  --color-tcl15-accent: oklch(0.82 0.13 200);
  --color-tcl15-accentink: #002735;
  --color-tcl15-accentink: oklch(0.25 0.06 220);
  --color-tcl15-ribbon: #065da0;
  --color-tcl15-ribbon: oklch(0.47 0.13 250);
  --color-tcl15-dot: #00878f;
  --color-tcl15-dot: oklch(0.55 0.13 200);
  --color-tcl15-shade: #416f9e80;
  --color-tcl15-shade: oklch(0.53 0.09 250 / 0.5);
  --color-tcl15-light: #f9fffff2;
  --color-tcl15-light: oklch(1 0.012 250 / 0.95);
  --color-tcl15-ink: #0f253b;
  --color-tcl15-ink: oklch(0.26 0.05 250);
  --color-tcl15-mut: #42576e;
  --color-tcl15-mut: oklch(0.45 0.045 250);
  --font-tcl15-display: 'Bricolage Grotesque', system-ui, sans-serif;
  --font-tcl15-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tcl15-mono: 'JetBrains Mono', ui-monospace, monospace;
  --shadow-tcl15-tier2: 0 18px 34px -8px var(--color-tcl15-shade), inset 0 -8px 16px -8px var(--color-tcl15-shade), inset 0 10px 16px -6px var(--color-tcl15-light);
  --shadow-tcl15-tier4: 0 36px 68px -16px var(--color-tcl15-shade), inset 0 -16px 32px -8px var(--color-tcl15-shade), inset 0 20px 32px -6px var(--color-tcl15-light);
  --shadow-tcl15-pill: 0 14px 24px -16px var(--color-tcl15-shade), inset 0 -9px 15px -11px var(--color-tcl15-shade), inset 0 11px 15px -8px var(--color-tcl15-light);
  --shadow-tcl15-track: inset 0 8px 14px -6px var(--color-tcl15-shade), inset 0 -5px 10px -8px var(--color-tcl15-light);
  --shadow-tcl15-knob: 0 7px 12px -5px var(--color-tcl15-shade), inset 0 -5px 8px -6px var(--color-tcl15-shade), inset 0 7px 9px -5px var(--color-tcl15-light);
  --shadow-tcl15-feats: inset 0 9px 16px -8px var(--color-tcl15-shade), inset 0 -6px 12px -10px var(--color-tcl15-light);
  --shadow-tcl15-btn: 0 14px 22px -12px var(--color-tcl15-shade), inset 0 -10px 16px -9px var(--color-tcl15-shade), inset 0 12px 16px -7px var(--color-tcl15-light);
  --shadow-tcl15-press: 0 0 0 0 transparent, inset 0 12px 18px -8px var(--color-tcl15-shade), inset 0 -6px 12px -9px var(--color-tcl15-light);
  --shadow-tcl15-ribbon: 0 12px 20px -8px var(--color-tcl15-shade), inset 0 -5px 9px -6px oklch(0 0 0 / 0.4), inset 0 7px 9px -5px oklch(1 0 0 / 0.45);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcl-15 {
  width: 100%;
  min-height: 100svh;
}
```
