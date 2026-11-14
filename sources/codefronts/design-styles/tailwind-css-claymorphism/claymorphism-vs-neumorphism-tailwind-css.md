---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-claymorphism/claymorphism-vs-neumorphism-tailwind-css/"
title: "Claymorphism vs Neumorphism in Tailwind CSS (Side-by-Side)"
section: "design-styles"
category: "tailwind-css-claymorphism"
category_name: "Tailwind CSS Claymorphism"
description: "The comparison people actually search for: two identical cards that differ only in shadow strategy — extruded-from-the-page neumorphism and lifted-object…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Claymorphism vs Neumorphism in Tailwind CSS (Side-by-Side)
Source: https://codefronts.com/design-styles/tailwind-css-claymorphism/claymorphism-vs-neumorphism-tailwind-css/

The comparison people actually search for: two identical cards that differ only in shadow strategy — extruded-from-the-page neumorphism and lifted-object claymorphism — with a switch that re-skins the neumorphic card in clay tokens. The port fixes the original's half-swap (the button kept its 14px corner) and adds a live contrast verdict to each card.
## HTML
```html
<section class="tcl-04 group/demo w-full min-h-svh grid place-items-center bg-tcl04-bg px-5 py-14 font-tcl04-sans text-tcl04-ink" aria-label="Claymorphism versus neumorphism comparison demo">
  <div class="grid w-full justify-items-center gap-[clamp(24px,4vw,40px)]">
    <header class="grid max-w-[60ch] justify-items-center gap-4 text-center">
      <h2 class="font-tcl04-display text-[clamp(26px,3.8vw,38px)] font-extrabold leading-[1.08] tracking-[-0.03em] text-balance">Clay vs Neu — same card, two depth models</h2>
      <label class="inline-flex min-h-12 cursor-pointer items-center gap-3 rounded-full bg-tcl04-soft py-1.5 pr-5.5 pl-2 text-sm font-semibold shadow-tcl04-pill has-[:focus-visible]:outline-3 has-[:focus-visible]:outline-offset-3 has-[:focus-visible]:outline-tcl04-ink">
        <input class="peer sr-only" type="checkbox" role="switch" id="tcl-04-swap">
        <span aria-hidden="true" class="relative h-9 w-15 rounded-full bg-tcl04-bg shadow-tcl04-track transition-colors duration-300 peer-checked:bg-tcl04-clay/70"></span>
        <span aria-hidden="true" class="absolute ml-1 size-7 rounded-full bg-white shadow-tcl04-knob transition-transform duration-300 ease-[cubic-bezier(.34,1.4,.5,1)] peer-checked:translate-x-6 motion-reduce:transition-none"></span>
        Apply clay tokens to both
      </label>
    </header>
    <div class="grid w-full max-w-[900px] grid-cols-[repeat(auto-fit,minmax(270px,1fr))] gap-[clamp(20px,3vw,34px)]">
      <article class="grid content-start gap-3 rounded-[18px] bg-tcl04-bg p-[clamp(24px,3vw,32px)] shadow-tcl04-neu transition-[translate,background-color,border-radius] duration-500 ease-[cubic-bezier(.34,1.3,.5,1)] hover:-translate-y-1.5 group-has-[#tcl-04-swap:checked]/demo:rounded-[38px] group-has-[#tcl-04-swap:checked]/demo:bg-tcl04-clay group-has-[#tcl-04-swap:checked]/demo:shadow-tcl04-clay motion-reduce:transition-none">
        <p class="text-[11.5px] font-bold uppercase tracking-[0.16em] text-tcl04-mut">Neumorphism</p>
        <h3 class="font-tcl04-display text-[22px] font-bold tracking-[-0.02em]">Soft UI</h3>
        <p class="text-sm leading-relaxed text-tcl04-ink/85 text-pretty">The object is the page, extruded. Fill matches the background; two mirrored outset shadows do all the work.</p>
        <dl class="mt-1 grid gap-2 text-[13px]">
          <div class="flex justify-between gap-3 border-b border-tcl04-ink/12 pb-2"><dt class="font-semibold text-tcl04-mut">Fill</dt><dd class="text-right">= page color</dd></div>
          <div class="flex justify-between gap-3 border-b border-tcl04-ink/12 pb-2"><dt class="font-semibold text-tcl04-mut">Shadows</dt><dd class="text-right">2 outset, mirrored</dd></div>
          <div class="flex justify-between gap-3 border-b border-tcl04-ink/12 pb-2"><dt class="font-semibold text-tcl04-mut">Radius</dt><dd class="text-right">12–20px</dd></div>
        </dl>
        <p class="inline-flex items-center gap-2 justify-self-start rounded-full bg-tcl04-warn/15 px-3 py-1.5 text-[12.5px] font-semibold text-tcl04-warn group-has-[#tcl-04-swap:checked]/demo:bg-tcl04-ok/15 group-has-[#tcl-04-swap:checked]/demo:text-tcl04-ok"><span aria-hidden="true" class="size-2 rounded-full bg-current"></span><span class="group-has-[#tcl-04-swap:checked]/demo:hidden">Edge contrast: shadow only · fails 3:1</span><span class="hidden group-has-[#tcl-04-swap:checked]/demo:inline">Edge contrast: real fill · testable</span></p>
        <button type="button" class="mt-1.5 min-h-12 cursor-pointer justify-self-start rounded-[14px] bg-tcl04-soft px-6 text-sm font-semibold text-tcl04-ink shadow-tcl04-btn transition-[translate,box-shadow,border-radius] duration-200 active:translate-y-0.75 active:shadow-tcl04-press focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-tcl04-ink group-has-[#tcl-04-swap:checked]/demo:rounded-[22px]">Press me</button>
      </article>
      <article class="grid content-start gap-3 rounded-[38px] bg-tcl04-clay p-[clamp(24px,3vw,32px)] shadow-tcl04-clay transition-[translate] duration-500 ease-[cubic-bezier(.34,1.3,.5,1)] hover:-translate-y-1.5 motion-reduce:transition-none">
        <p class="text-[11.5px] font-bold uppercase tracking-[0.16em] text-tcl04-ink/70">Claymorphism</p>
        <h3 class="font-tcl04-display text-[22px] font-bold tracking-[-0.02em]">Clay UI</h3>
        <p class="text-sm leading-relaxed text-tcl04-ink/85 text-pretty">A separate object on the page. Own fill, outer drop for mass, two insets for thickness and sheen.</p>
        <dl class="mt-1 grid gap-2 text-[13px]">
          <div class="flex justify-between gap-3 border-b border-tcl04-ink/12 pb-2"><dt class="font-semibold text-tcl04-ink/70">Fill</dt><dd class="text-right">lighter than page</dd></div>
          <div class="flex justify-between gap-3 border-b border-tcl04-ink/12 pb-2"><dt class="font-semibold text-tcl04-ink/70">Shadows</dt><dd class="text-right">1 outset + 2 inset</dd></div>
          <div class="flex justify-between gap-3 border-b border-tcl04-ink/12 pb-2"><dt class="font-semibold text-tcl04-ink/70">Radius</dt><dd class="text-right">28–48px</dd></div>
        </dl>
        <p class="inline-flex items-center gap-2 justify-self-start rounded-full bg-white/45 px-3 py-1.5 text-[12.5px] font-semibold text-tcl04-ok"><span aria-hidden="true" class="size-2 rounded-full bg-current"></span>Edge contrast: real fill · testable</p>
        <button type="button" class="mt-1.5 min-h-12 cursor-pointer justify-self-start rounded-[22px] bg-tcl04-soft px-6 text-sm font-semibold text-tcl04-ink shadow-tcl04-btn transition-[translate,box-shadow] duration-200 active:translate-y-0.75 active:shadow-tcl04-press focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-tcl04-ink">Press me</button>
      </article>
    </div>
    <p aria-hidden="true" class="rounded-full bg-white/55 px-4 py-2 text-center font-tcl04-mono text-[11.5px] text-tcl04-mut">same markup · token-only difference · group-has-[#swap:checked]/demo:</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcl04-bg: #e3e8f2;
  --color-tcl04-bg: oklch(0.93 0.015 265);
  --color-tcl04-light: #ffffffeb;
  --color-tcl04-light: oklch(1 0 0 / 0.92);
  --color-tcl04-shade: #7486ab8c;
  --color-tcl04-shade: oklch(0.62 0.06 265 / 0.55);
  --color-tcl04-ink: #242b3b;
  --color-tcl04-ink: oklch(0.29 0.03 265);
  --color-tcl04-mut: #4e586c;
  --color-tcl04-mut: oklch(0.46 0.035 265);
  --color-tcl04-clay: #b7c6ff;
  --color-tcl04-clay: oklch(0.84 0.1 275);
  --color-tcl04-soft: color-mix(in oklch, var(--color-tcl04-bg) 80%, white);
  --color-tcl04-warn: #a7391e;
  --color-tcl04-warn: oklch(0.5 0.15 35);
  --color-tcl04-ok: #006836;
  --color-tcl04-ok: oklch(0.45 0.12 155);
  --font-tcl04-display: 'Bricolage Grotesque', system-ui, sans-serif;
  --font-tcl04-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tcl04-mono: 'JetBrains Mono', ui-monospace, monospace;
  --shadow-tcl04-neu: -9px -9px 18px var(--color-tcl04-light), 9px 9px 20px var(--color-tcl04-shade);
  --shadow-tcl04-clay: 0 26px 46px -16px var(--color-tcl04-shade), inset 0 -16px 26px -12px var(--color-tcl04-shade), inset 0 18px 26px -8px var(--color-tcl04-light);
  --shadow-tcl04-btn: 0 10px 18px -12px var(--color-tcl04-shade), inset 0 -8px 12px -9px var(--color-tcl04-shade), inset 0 9px 12px -7px var(--color-tcl04-light);
  --shadow-tcl04-press: 0 4px 8px -8px var(--color-tcl04-shade), inset 0 8px 14px -8px var(--color-tcl04-shade), inset 0 -6px 12px -9px var(--color-tcl04-light);
  --shadow-tcl04-pill: 0 12px 22px -14px var(--color-tcl04-shade), inset 0 -8px 14px -10px var(--color-tcl04-shade), inset 0 10px 14px -8px var(--color-tcl04-light);
  --shadow-tcl04-track: inset 0 4px 8px -3px var(--color-tcl04-shade), inset 0 -3px 6px -3px var(--color-tcl04-light);
  --shadow-tcl04-knob: 0 4px 8px -3px var(--color-tcl04-shade), inset 0 -3px 5px -3px var(--color-tcl04-shade);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcl-04 {
  width: 100%;
  min-height: 100svh;
}
```
