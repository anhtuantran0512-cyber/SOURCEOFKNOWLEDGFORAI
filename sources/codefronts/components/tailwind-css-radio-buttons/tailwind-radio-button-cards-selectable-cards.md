---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-radio-buttons/tailwind-radio-button-cards-selectable-cards/"
title: "Tailwind Radio Button Cards (Selectable Cards)"
section: "components"
category: "tailwind-css-radio-buttons"
category_name: "Tailwind CSS Radio Buttons"
description: "Full selectable cards that act as radio buttons — the checkout and onboarding staple — ported whole into utilities."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Radio Button Cards (Selectable Cards)
Source: https://codefronts.com/components/tailwind-css-radio-buttons/tailwind-radio-button-cards-selectable-cards/

Full selectable cards that act as radio buttons — the checkout and onboarding staple — ported whole into utilities. The card reads its own state with v4's built-in has-checked: variant, descendants follow with group-has-checked:, and the lift is gated behind motion-safe: instead of being undone later.
## HTML
```html
<section class="trb-01 w-full min-h-svh grid place-items-center bg-trb01-bg bg-[radial-gradient(110%_80%_at_50%_0%,var(--color-trb01-glow),transparent_70%)] px-6 py-14 font-trb01-sans text-trb01-ink" aria-label="Selectable card radio buttons demo">
  <fieldset class="group/set w-full max-w-[42rem]">
    <legend class="text-[26px] font-extrabold tracking-[-0.02em]">Shipping speed</legend>
    <p class="mt-1.5 text-sm text-trb01-mut">Every card is a real radio input — click anywhere on it.</p>
    <div class="mt-6 grid grid-cols-[repeat(auto-fit,minmax(11.5rem,1fr))] gap-4">
      <label class="group relative grid cursor-pointer gap-1 rounded-2xl border-2 border-trb01-line bg-white px-5 pt-6 pb-5 transition duration-250 hover:border-trb01-acc/40 has-checked:border-trb01-acc has-checked:shadow-trb01-lift has-focus-visible:outline-3 has-focus-visible:outline-offset-3 has-focus-visible:outline-trb01-acc motion-safe:hover:-translate-y-0.5 motion-safe:has-checked:-translate-y-[3px] motion-reduce:transition-none">
        <input type="radio" name="trb-01" value="standard" class="sr-only" checked>
        <span aria-hidden="true" class="absolute top-3.5 right-3.5 grid size-[22px] place-items-center rounded-full border-2 border-trb01-ring transition after:size-[9px] after:scale-0 after:rounded-full after:bg-white after:transition-transform after:duration-300 after:ease-trb01-spring after:content-[''] group-has-checked:border-trb01-acc group-has-checked:bg-trb01-acc group-has-checked:after:scale-100"></span>
        <svg class="mb-2 size-[26px] text-trb01-icon transition-colors group-has-checked:text-trb01-acc" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7h11v8H3zM14 10h4l3 3v2h-7z"/><circle cx="7" cy="17" r="1.8"/><circle cx="17" cy="17" r="1.8"/></svg>
        <span class="text-base font-bold">Standard</span>
        <span class="text-[13px] text-trb01-mut">4–6 business days</span>
        <span class="mt-2.5 text-[15px] font-extrabold">Free</span>
      </label>
      <label class="group relative grid cursor-pointer gap-1 rounded-2xl border-2 border-trb01-line bg-white px-5 pt-6 pb-5 transition duration-250 hover:border-trb01-acc/40 has-checked:border-trb01-acc has-checked:shadow-trb01-lift has-focus-visible:outline-3 has-focus-visible:outline-offset-3 has-focus-visible:outline-trb01-acc motion-safe:hover:-translate-y-0.5 motion-safe:has-checked:-translate-y-[3px] motion-reduce:transition-none">
        <input type="radio" name="trb-01" value="express" class="sr-only">
        <span aria-hidden="true" class="absolute top-3.5 right-3.5 grid size-[22px] place-items-center rounded-full border-2 border-trb01-ring transition after:size-[9px] after:scale-0 after:rounded-full after:bg-white after:transition-transform after:duration-300 after:ease-trb01-spring after:content-[''] group-has-checked:border-trb01-acc group-has-checked:bg-trb01-acc group-has-checked:after:scale-100"></span>
        <svg class="mb-2 size-[26px] text-trb01-icon transition-colors group-has-checked:text-trb01-acc" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M13 2 4 14h6l-1 8 9-12h-6z"/></svg>
        <span class="text-base font-bold">Express</span>
        <span class="text-[13px] text-trb01-mut">2–3 business days</span>
        <span class="mt-2.5 text-[15px] font-extrabold">$9</span>
      </label>
      <label class="group relative grid cursor-pointer gap-1 rounded-2xl border-2 border-trb01-line bg-white px-5 pt-6 pb-5 transition duration-250 hover:border-trb01-acc/40 has-checked:border-trb01-acc has-checked:shadow-trb01-lift has-focus-visible:outline-3 has-focus-visible:outline-offset-3 has-focus-visible:outline-trb01-acc motion-safe:hover:-translate-y-0.5 motion-safe:has-checked:-translate-y-[3px] motion-reduce:transition-none">
        <input type="radio" name="trb-01" value="overnight" class="sr-only">
        <span aria-hidden="true" class="absolute top-3.5 right-3.5 grid size-[22px] place-items-center rounded-full border-2 border-trb01-ring transition after:size-[9px] after:scale-0 after:rounded-full after:bg-white after:transition-transform after:duration-300 after:ease-trb01-spring after:content-[''] group-has-checked:border-trb01-acc group-has-checked:bg-trb01-acc group-has-checked:after:scale-100"></span>
        <svg class="mb-2 size-[26px] text-trb01-icon transition-colors group-has-checked:text-trb01-acc" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.5 2"/></svg>
        <span class="text-base font-bold">Overnight</span>
        <span class="text-[13px] text-trb01-mut">Next business day</span>
        <span class="mt-2.5 text-[15px] font-extrabold">$24</span>
      </label>
    </div>
    <p class="mt-6 flex items-center gap-2.5 rounded-xl border border-trb01-line bg-white/70 px-4 py-3 text-sm text-trb01-mut">
      <span aria-hidden="true" class="size-2 flex-none rounded-full bg-trb01-acc"></span>
      <span class="hidden group-has-[[value=standard]:checked]/set:inline">Arrives <strong class="font-bold text-trb01-ink">Mon – Wed next week</strong> · free</span>
      <span class="hidden group-has-[[value=express]:checked]/set:inline">Arrives <strong class="font-bold text-trb01-ink">Thursday</strong> · $9 added at checkout</span>
      <span class="hidden group-has-[[value=overnight]:checked]/set:inline">Arrives <strong class="font-bold text-trb01-ink">tomorrow by 10 am</strong> · $24 added at checkout</span>
    </p>
  </fieldset>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-trb01-bg: #f3f4fa;
  --color-trb01-bg: oklch(0.967 0.008 275);
  --color-trb01-glow: #ffffff;
  --color-trb01-glow: oklch(1 0 0);
  --color-trb01-ink: #1c2130;
  --color-trb01-ink: oklch(0.24 0.03 270);
  --color-trb01-mut: #5b6278;
  --color-trb01-mut: oklch(0.5 0.03 270);
  --color-trb01-line: #e3e6f0;
  --color-trb01-line: oklch(0.925 0.012 275);
  --color-trb01-ring: #c3c9da;
  --color-trb01-ring: oklch(0.84 0.02 270);
  --color-trb01-icon: #7d859c;
  --color-trb01-icon: oklch(0.62 0.03 270);
  --color-trb01-acc: #3d5fe0;
  --color-trb01-acc: oklch(0.55 0.2 262);
  --shadow-trb01-lift: 0 16px 30px -18px oklch(0.55 0.2 262 / 0.6);
  --ease-trb01-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
  --font-trb01-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.trb-01 {
  width: 100%;
  min-height: 100svh;
}
```
