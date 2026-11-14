---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-chroma-conic-gradient-border-spin-button/"
title: "Tailwind Chroma Conic Gradient Border Spin Button"
section: "motion"
category: "tailwind-css-button-hover-effects"
category_name: "Tailwind CSS Button Hover Effects"
description: "A dark premium CTA wrapped in a razor-thin conic-gradient border that spins continuously like a rotating light source &mdash; the AI/fintech 'live' look."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Chroma Conic Gradient Border Spin Button
Source: https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-chroma-conic-gradient-border-spin-button/

A dark premium CTA wrapped in a razor-thin conic-gradient border that spins continuously like a rotating light source &mdash; the AI/fintech 'live' look. This is the demo where the port is most honest about its limits: @property is what makes an angle animatable at all, and it has no utility form.
## HTML
```html
<div class="tbh-08-group w-full min-h-svh flex flex-wrap">
<section class="tbh-08a flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh08-sans bg-tbh08a-stage" aria-label="Conic border spin button">
  <button type="button" class="relative isolate cursor-pointer border-0 rounded-[14px] px-[38px] py-4 text-base font-bold text-white bg-tbh08a-card transition-[translate] duration-200 before:content-[''] before:absolute before:-inset-0.5 before:z-0 before:rounded-2xl before:bg-[conic-gradient(from_var(--tbh08a-angle),var(--color-tbh08a-c1),var(--color-tbh08a-c2),var(--color-tbh08a-c3),var(--color-tbh08a-c1))] before:animate-tbh08a-spin after:content-[''] after:absolute after:inset-0 after:z-0 after:rounded-[14px] after:bg-tbh08a-card hover:-translate-y-0.5 hover:before:[animation-duration:1.6s] hover:before:[filter:brightness(1.25)_saturate(1.2)] focus-visible:-translate-y-0.5 focus-visible:before:[animation-duration:1.6s] focus-visible:outline-3 focus-visible:outline-tbh08a-c1 focus-visible:outline-offset-4 motion-reduce:before:animate-none motion-reduce:hover:translate-y-0">
    <span class="relative z-[1]">Launch app</span>
  </button>
</section>
<section class="tbh-08b flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh08-sans bg-tbh08b-stage" aria-label="Dual arc border button">
  <button type="button" class="relative isolate cursor-pointer border-0 rounded-full px-10 py-4 text-base font-bold text-tbh08b-ink bg-tbh08b-card transition-[translate] duration-200 before:content-[''] before:absolute before:-inset-0.5 before:z-0 before:rounded-full before:bg-[conic-gradient(from_var(--tbh08b-angle),transparent_0_25%,var(--color-tbh08b-arc)_35%_40%,transparent_50%_75%,var(--color-tbh08b-arc)_85%_90%,transparent)] before:animate-tbh08b-spin after:content-[''] after:absolute after:inset-0 after:z-0 after:rounded-full after:bg-tbh08b-card hover:-translate-y-0.5 hover:before:[animation-duration:1.2s] focus-visible:-translate-y-0.5 focus-visible:before:[animation-duration:1.2s] focus-visible:outline-3 focus-visible:outline-tbh08b-arc focus-visible:outline-offset-4 motion-reduce:before:animate-none motion-reduce:hover:translate-y-0">
    <span class="relative z-[1]">Connect wallet</span>
  </button>
</section>
</div>
```
## CSS
```css
@import "tailwindcss";
/* Stays CSS: a property registration is a type declaration, not a style — there is no
   utility form, and the typed syntax is the only thing that makes the angle animatable. */

@property --tbh08a-angle {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

@property --tbh08b-angle {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

@theme {
  --color-tbh08a-card: #12101c;
  --color-tbh08a-card: oklch(0.18 0.03 285);
  --color-tbh08a-stage: #08070f;
  --color-tbh08a-stage: oklch(0.12 0.02 285);
  --color-tbh08a-c1: #22e3ff;
  --color-tbh08a-c1: oklch(0.85 0.15 210);
  --color-tbh08a-c2: #7c5cff;
  --color-tbh08a-c2: oklch(0.6 0.22 285);
  --color-tbh08a-c3: #ff2bd6;
  --color-tbh08a-c3: oklch(0.7 0.28 330);
  --color-tbh08b-card: #0c1618;
  --color-tbh08b-card: oklch(0.17 0.02 195);
  --color-tbh08b-stage: #050b0c;
  --color-tbh08b-stage: oklch(0.11 0.015 195);
  --color-tbh08b-arc: #2ff5c8;
  --color-tbh08b-arc: oklch(0.85 0.17 170);
  --color-tbh08b-ink: #eafff8;
  --color-tbh08b-ink: oklch(0.97 0.02 170);
  --font-tbh08-sans: 'Space Grotesk', system-ui, sans-serif;
  --animate-tbh08a-spin: tbh08a-spin 4s linear infinite;
  --animate-tbh08b-spin: tbh08b-spin 3s linear infinite;
}
/* Stays CSS: keyframes that animate a registered property. */

@keyframes tbh08a-spin {
  to {
    --tbh08a-angle: 360deg;
  }
}

@keyframes tbh08b-spin {
  to {
    --tbh08b-angle: 360deg;
  }
}

.tbh-08-group {
  width: 100%;
  min-height: 100svh;
}

.tbh-08a,
.tbh-08b {
  min-height: 100svh;
}
```
