---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-liquid-glass-effects/tailwind-liquid-glass-input-form-fields/"
title: "Tailwind Liquid Glass Input Form Fields"
section: "design-styles"
category: "tailwind-liquid-glass-effects"
category_name: "Tailwind Liquid Glass Effects"
description: "A sign-up form where focusing a field lights a refractive border that travels around it."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Liquid Glass Input Form Fields
Source: https://codefronts.com/design-styles/tailwind-liquid-glass-effects/tailwind-liquid-glass-input-form-fields/

A sign-up form where focusing a field lights a refractive border that travels around it. The port keeps the one thing utilities genuinely cannot do &mdash; @property registering the angle as an <angle> so it can tween &mdash; in CSS, and expresses everything else, including the mask-composite rim trick, as before: utilities under a focus-within: variant.
## HTML
```html
<section class="lgt-07 grid w-full min-h-svh place-items-center p-15 font-lgt07-sans [background:conic-gradient(from_210deg_at_30%_30%,#2a2350,#3a2a60,#1c2450,#2a2350)]" aria-label="Tailwind liquid glass form fields">
  <form novalidate class="w-[min(400px,92vw)] rounded-[26px] border border-white/28 bg-white/10 p-8.5 backdrop-blur-[22px] backdrop-saturate-170 shadow-[inset_0_1px_0_rgba(255,255,255,.4),0_30px_60px_-30px_rgba(0,0,0,.6)]">
    <h3 class="mb-5.5 text-2xl font-extrabold text-white">Create account</h3>

    <div class="mb-4.5">
      <label for="lgt-07-name" class="mb-1.75 block text-xs font-semibold uppercase tracking-[0.06em] text-white/70">Full name</label>
      <span class="relative block before:pointer-events-none before:absolute before:-inset-0.5 before:rounded-[16px] before:p-0.5 before:opacity-0 before:transition-opacity before:duration-300 before:[background:conic-gradient(from_var(--lgt-07-angle),var(--color-lgt07-accent),oklch(0.7_0.18_200),oklch(0.72_0.17_330),var(--color-lgt07-accent))] before:[mask-image:linear-gradient(#000_0_0),linear-gradient(#000_0_0)] before:[mask-clip:content-box,border-box] before:[mask-composite:exclude] focus-within:before:opacity-100 focus-within:before:animate-lgt07-spin motion-reduce:focus-within:before:animate-none">
        <input id="lgt-07-name" type="text" autocomplete="name" placeholder="Ada Lovelace" class="relative z-1 block w-full rounded-[14px] border border-white/25 bg-white/8 px-3.75 py-3.25 text-[15px] text-white outline-none backdrop-blur-[8px] shadow-[inset_0_1px_0_rgba(255,255,255,.3)] transition-colors duration-200 placeholder:text-white/50 focus:bg-white/14">
      </span>
    </div>

    <div class="mb-4.5">
      <label for="lgt-07-email" class="mb-1.75 block text-xs font-semibold uppercase tracking-[0.06em] text-white/70">Email</label>
      <span class="relative block before:pointer-events-none before:absolute before:-inset-0.5 before:rounded-[16px] before:p-0.5 before:opacity-0 before:transition-opacity before:duration-300 before:[background:conic-gradient(from_var(--lgt-07-angle),var(--color-lgt07-accent),oklch(0.7_0.18_200),oklch(0.72_0.17_330),var(--color-lgt07-accent))] before:[mask-image:linear-gradient(#000_0_0),linear-gradient(#000_0_0)] before:[mask-clip:content-box,border-box] before:[mask-composite:exclude] focus-within:before:opacity-100 focus-within:before:animate-lgt07-spin motion-reduce:focus-within:before:animate-none">
        <input id="lgt-07-email" type="email" autocomplete="email" placeholder="[email protected]" class="relative z-1 block w-full rounded-[14px] border border-white/25 bg-white/8 px-3.75 py-3.25 text-[15px] text-white outline-none backdrop-blur-[8px] shadow-[inset_0_1px_0_rgba(255,255,255,.3)] transition-colors duration-200 placeholder:text-white/50 focus:bg-white/14">
      </span>
    </div>

    <div class="mb-4.5">
      <label for="lgt-07-pass" class="mb-1.75 block text-xs font-semibold uppercase tracking-[0.06em] text-white/70">Password</label>
      <span class="relative block before:pointer-events-none before:absolute before:-inset-0.5 before:rounded-[16px] before:p-0.5 before:opacity-0 before:transition-opacity before:duration-300 before:[background:conic-gradient(from_var(--lgt-07-angle),var(--color-lgt07-accent),oklch(0.7_0.18_200),oklch(0.72_0.17_330),var(--color-lgt07-accent))] before:[mask-image:linear-gradient(#000_0_0),linear-gradient(#000_0_0)] before:[mask-clip:content-box,border-box] before:[mask-composite:exclude] focus-within:before:opacity-100 focus-within:before:animate-lgt07-spin motion-reduce:focus-within:before:animate-none">
        <input id="lgt-07-pass" type="password" autocomplete="new-password" placeholder="&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;" class="relative z-1 block w-full rounded-[14px] border border-white/25 bg-white/8 px-3.75 py-3.25 text-[15px] text-white outline-none backdrop-blur-[8px] shadow-[inset_0_1px_0_rgba(255,255,255,.3)] transition-colors duration-200 placeholder:text-white/50 focus:bg-white/14">
      </span>
    </div>

    <button type="submit" class="mt-1.5 w-full cursor-pointer rounded-[14px] border border-lgt07-accent/60 bg-linear-to-b from-lgt07-accent-top to-lgt07-accent py-3.5 text-base font-bold text-white shadow-[inset_0_1px_0_rgba(255,255,255,.5),0_14px_28px_-16px_rgba(0,0,0,.6)] transition-transform duration-150 hover:-translate-y-0.5 focus-visible:-translate-y-0.5 focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-white motion-reduce:transition-none">Sign up</button>
  </form>
</section>
```
## CSS
```css
@import "tailwindcss";
/* Not portable to a utility, and must not be dropped: registering the angle as an
   <angle> is what lets the browser interpolate it instead of snapping. */

@property --lgt-07-angle {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

@theme {
  --color-lgt07-accent: #8b5cf6;
  --color-lgt07-accent: oklch(0.68 0.19 285);
  --color-lgt07-accent-top: #a78bfa;
  --color-lgt07-accent-top: oklch(0.74 0.16 285);
  --font-lgt07-sans: 'Manrope', system-ui, sans-serif;
  --animate-lgt07-spin: lgt-07-spin 3s linear infinite;
}

@keyframes lgt-07-spin {
  to {
    --lgt-07-angle: 360deg;
  }
}
```
