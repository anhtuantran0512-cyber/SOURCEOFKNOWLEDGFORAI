---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-pricing-tables/neumorphic-pricing-table-tailwind-css/"
title: "Neumorphic Pricing Table in Tailwind CSS (Soft UI)"
section: "components"
category: "tailwind-css-pricing-tables"
category_name: "Tailwind CSS Pricing Tables"
description: "Tactile soft-UI pricing: cards extrude from a same-colour surface with the signature light/dark shadow pair, and the selected plan's button sinks into the…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neumorphic Pricing Table in Tailwind CSS (Soft UI)
Source: https://codefronts.com/components/tailwind-css-pricing-tables/neumorphic-pricing-table-tailwind-css/

Tactile soft-UI pricing: cards extrude from a same-colour surface with the signature light/dark shadow pair, and the selected plan's button sinks into the surface. v4's separate inset-shadow-* utility makes the press honest — has-checked:shadow-none has-checked:inset-shadow-[…] — and because neumorphism is weak on contrast, a real accent ring and a &ldquo;Selected&rdquo; label carry the state.
## HTML
```html
<section class="tpt-18 w-full min-h-svh grid place-items-center bg-tpt18-base px-5 py-16 font-tpt18-sans text-tpt18-ink antialiased" aria-label="Neumorphic pricing tiers">
  <div class="grid w-full max-w-5xl justify-items-center gap-11">
    <h2 class="text-center text-[clamp(26px,3.8vw,40px)] font-extrabold tracking-[-0.02em]">Choose your calm</h2>
    <fieldset class="grid w-full gap-7 md:grid-cols-3">
      <legend class="sr-only">Plan</legend>
      <label class="group/c flex cursor-pointer flex-col gap-2 rounded-[26px] border-2 border-transparent bg-tpt18-base p-8 shadow-[-9px_-9px_20px_var(--color-tpt18-lite),9px_9px_20px_var(--color-tpt18-shade)] transition-[box-shadow,border-color,translate] duration-300 hover:-translate-y-0.5 has-checked:border-tpt18-acc has-checked:shadow-[-4px_-4px_12px_var(--color-tpt18-lite),4px_4px_12px_var(--color-tpt18-shade)] has-focus-visible:outline-3 has-focus-visible:outline-offset-4 has-focus-visible:outline-tpt18-acc motion-reduce:hover:translate-y-0">
        <input type="radio" name="tpt18-plan" value="calm" class="sr-only">
        <h3 class="text-[13px] font-extrabold tracking-[0.1em] text-tpt18-mut uppercase">Calm</h3>
        <p class="text-[44px] leading-tight font-extrabold tracking-[-0.03em]">$7<small class="text-[15px] font-bold tracking-normal text-tpt18-mut">/mo</small></p>
        <ul class="mt-2 mb-6 grid flex-1 content-start gap-2.5 text-sm font-medium text-tpt18-body *:flex *:items-center *:gap-3 *:before:size-2 *:before:rounded-full *:before:bg-tpt18-acc *:before:content-['']"><li>10 sessions / month</li><li>Sleep stories</li></ul>
        <span class="grid min-h-12 place-items-center rounded-2xl bg-tpt18-base text-sm font-extrabold text-tpt18-ink shadow-[-5px_-5px_12px_var(--color-tpt18-lite),5px_5px_12px_var(--color-tpt18-shade)] transition-[box-shadow,color,translate] duration-200 group-hover/c:text-tpt18-acc group-active/c:translate-y-px group-active/c:shadow-none group-active/c:inset-shadow-[4px_4px_10px_var(--color-tpt18-shade)] group-has-checked/c:text-tpt18-acc group-has-checked/c:shadow-none group-has-checked/c:inset-shadow-[4px_4px_10px_var(--color-tpt18-shade)]"><span class="group-has-checked/c:hidden">Select</span><span class="hidden group-has-checked/c:inline">✓ Selected</span></span>
      </label>
      <label class="group/c flex cursor-pointer flex-col gap-2 rounded-[26px] border-2 border-transparent bg-tpt18-base p-8 shadow-[-9px_-9px_20px_var(--color-tpt18-lite),9px_9px_20px_var(--color-tpt18-shade)] transition-[box-shadow,border-color,translate] duration-300 hover:-translate-y-0.5 has-checked:border-tpt18-acc has-checked:shadow-[-4px_-4px_12px_var(--color-tpt18-lite),4px_4px_12px_var(--color-tpt18-shade)] has-focus-visible:outline-3 has-focus-visible:outline-offset-4 has-focus-visible:outline-tpt18-acc motion-reduce:hover:translate-y-0">
        <input type="radio" name="tpt18-plan" value="focus" class="sr-only" checked>
        <h3 class="text-[13px] font-extrabold tracking-[0.1em] text-tpt18-mut uppercase">Focus</h3>
        <p class="text-[44px] leading-tight font-extrabold tracking-[-0.03em]">$14<small class="text-[15px] font-bold tracking-normal text-tpt18-mut">/mo</small></p>
        <ul class="mt-2 mb-6 grid flex-1 content-start gap-2.5 text-sm font-medium text-tpt18-body *:flex *:items-center *:gap-3 *:before:size-2 *:before:rounded-full *:before:bg-tpt18-acc *:before:content-['']"><li>Unlimited sessions</li><li>Focus soundscapes</li><li>Mood &amp; streak stats</li></ul>
        <span class="grid min-h-12 place-items-center rounded-2xl bg-tpt18-base text-sm font-extrabold text-tpt18-ink shadow-[-5px_-5px_12px_var(--color-tpt18-lite),5px_5px_12px_var(--color-tpt18-shade)] transition-[box-shadow,color,translate] duration-200 group-hover/c:text-tpt18-acc group-active/c:translate-y-px group-active/c:shadow-none group-active/c:inset-shadow-[4px_4px_10px_var(--color-tpt18-shade)] group-has-checked/c:text-tpt18-acc group-has-checked/c:shadow-none group-has-checked/c:inset-shadow-[4px_4px_10px_var(--color-tpt18-shade)]"><span class="group-has-checked/c:hidden">Select</span><span class="hidden group-has-checked/c:inline">✓ Selected</span></span>
      </label>
      <label class="group/c flex cursor-pointer flex-col gap-2 rounded-[26px] border-2 border-transparent bg-tpt18-base p-8 shadow-[-9px_-9px_20px_var(--color-tpt18-lite),9px_9px_20px_var(--color-tpt18-shade)] transition-[box-shadow,border-color,translate] duration-300 hover:-translate-y-0.5 has-checked:border-tpt18-acc has-checked:shadow-[-4px_-4px_12px_var(--color-tpt18-lite),4px_4px_12px_var(--color-tpt18-shade)] has-focus-visible:outline-3 has-focus-visible:outline-offset-4 has-focus-visible:outline-tpt18-acc motion-reduce:hover:translate-y-0">
        <input type="radio" name="tpt18-plan" value="flow" class="sr-only">
        <h3 class="text-[13px] font-extrabold tracking-[0.1em] text-tpt18-mut uppercase">Flow</h3>
        <p class="text-[44px] leading-tight font-extrabold tracking-[-0.03em]">$21<small class="text-[15px] font-bold tracking-normal text-tpt18-mut">/mo</small></p>
        <ul class="mt-2 mb-6 grid flex-1 content-start gap-2.5 text-sm font-medium text-tpt18-body *:flex *:items-center *:gap-3 *:before:size-2 *:before:rounded-full *:before:bg-tpt18-acc *:before:content-['']"><li>Everything in Focus</li><li>Weekly 1:1 coaching</li></ul>
        <span class="grid min-h-12 place-items-center rounded-2xl bg-tpt18-base text-sm font-extrabold text-tpt18-ink shadow-[-5px_-5px_12px_var(--color-tpt18-lite),5px_5px_12px_var(--color-tpt18-shade)] transition-[box-shadow,color,translate] duration-200 group-hover/c:text-tpt18-acc group-active/c:translate-y-px group-active/c:shadow-none group-active/c:inset-shadow-[4px_4px_10px_var(--color-tpt18-shade)] group-has-checked/c:text-tpt18-acc group-has-checked/c:shadow-none group-has-checked/c:inset-shadow-[4px_4px_10px_var(--color-tpt18-shade)]"><span class="group-has-checked/c:hidden">Select</span><span class="hidden group-has-checked/c:inline">✓ Selected</span></span>
      </label>
    </fieldset>
    <p aria-hidden="true" class="rounded-full px-4 py-2 font-tpt18-mono text-[11.5px] text-tpt18-mut shadow-[inset_-3px_-3px_8px_var(--color-tpt18-lite),inset_3px_3px_8px_var(--color-tpt18-shade)]">shadow-[light,dark] · has-checked:inset-shadow-[…] · radio cards</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpt18-base: #e4e9f2;
  --color-tpt18-base: oklch(0.93 0.012 260);
  --color-tpt18-lite: #f8faff;
  --color-tpt18-lite: oklch(0.985 0.005 260);
  --color-tpt18-shade: #b9c1d3;
  --color-tpt18-shade: oklch(0.8 0.025 262);
  --color-tpt18-ink: #262c3c;
  --color-tpt18-ink: oklch(0.28 0.03 265);
  --color-tpt18-body: #404863;
  --color-tpt18-body: oklch(0.4 0.04 265);
  --color-tpt18-mut: #535c77;
  --color-tpt18-mut: oklch(0.47 0.04 265);
  --color-tpt18-acc: #4252c9;
  --color-tpt18-acc: oklch(0.5 0.18 268);
  --font-tpt18-sans: 'Nunito', system-ui, sans-serif;
  --font-tpt18-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities. */

.tpt-18 {
  width: 100%;
  min-height: 100svh;
}
```
