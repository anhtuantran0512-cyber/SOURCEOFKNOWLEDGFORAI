---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-radio-buttons/tailwind-animated-gradient-border-radio-cards/"
title: "Tailwind Animated Gradient Border Radio Cards"
section: "components"
category: "tailwind-css-radio-buttons"
category_name: "Tailwind CSS Radio Buttons"
description: "Dark glass cards wrapped in a living gradient border: at rest a faint rim; on selection a vivid violet-to-cyan gradient circulates around the perimeter."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Animated Gradient Border Radio Cards
Source: https://codefronts.com/components/tailwind-css-radio-buttons/tailwind-animated-gradient-border-radio-cards/

Dark glass cards wrapped in a living gradient border: at rest a faint rim; on selection a vivid violet-to-cyan gradient circulates around the perimeter. The port uses the two-background trick — [background:linear-gradient(card,card)_padding-box,conic-gradient(from_var(--trb20-angle),…)_border-box] on a transparent border — so there's no wrapper element, and @property animates the angle.
## HTML
```html
<section class="trb-20 w-full min-h-svh grid place-items-center bg-trb20-bg px-6 py-14 font-trb20-sans text-trb20-ink" aria-label="Gradient border card radio demo">
  <fieldset>
    <legend class="text-center text-[26px] font-bold tracking-[-0.02em]">Choose your model</legend>
    <div class="mt-8 flex flex-wrap justify-center gap-5">
      <label class="group relative cursor-pointer">
        <input type="radio" name="trb-20" value="lite" class="sr-only">
        <span class="relative grid w-[12.5rem] gap-1 rounded-[18px] border-[1.5px] border-transparent [background:linear-gradient(170deg,#171927,#101119)_padding-box,conic-gradient(from_var(--trb20-angle),rgb(255_255_255/0.14),rgb(255_255_255/0.05),rgb(255_255_255/0.14))_border-box] px-5 py-6 transition-[translate] duration-300 group-hover:-translate-y-0.5 group-has-checked:animate-trb20-rotate group-has-checked:[background:linear-gradient(170deg,#171927,#101119)_padding-box,conic-gradient(from_var(--trb20-angle),var(--color-trb20-g1),var(--color-trb20-g2),var(--color-trb20-g1))_border-box] group-has-focus-visible:outline-3 group-has-focus-visible:outline-offset-3 group-has-focus-visible:outline-white motion-reduce:group-has-checked:animate-none motion-reduce:group-hover:translate-y-0">
          <span aria-hidden="true" class="absolute top-5 right-5 size-2 rounded-full bg-white/15 group-has-checked:bg-trb20-g2 group-has-checked:shadow-trb20-dot"></span>
          <span class="text-lg font-bold tracking-[-0.01em] text-white">Nova Lite</span>
          <span class="text-[13px] text-trb20-mut">Fast drafts &amp; chat</span>
          <span class="mt-3 font-trb20-mono text-xs font-medium tracking-[0.06em] text-trb20-mut uppercase group-has-checked:text-trb20-g2">128k context</span>
        </span>
      </label>
      <label class="group relative cursor-pointer">
        <input type="radio" name="trb-20" value="pro" class="sr-only" checked>
        <span class="relative grid w-[12.5rem] gap-1 rounded-[18px] border-[1.5px] border-transparent [background:linear-gradient(170deg,#171927,#101119)_padding-box,conic-gradient(from_var(--trb20-angle),rgb(255_255_255/0.14),rgb(255_255_255/0.05),rgb(255_255_255/0.14))_border-box] px-5 py-6 transition-[translate] duration-300 group-hover:-translate-y-0.5 group-has-checked:animate-trb20-rotate group-has-checked:[background:linear-gradient(170deg,#171927,#101119)_padding-box,conic-gradient(from_var(--trb20-angle),var(--color-trb20-g1),var(--color-trb20-g2),var(--color-trb20-g1))_border-box] group-has-focus-visible:outline-3 group-has-focus-visible:outline-offset-3 group-has-focus-visible:outline-white motion-reduce:group-has-checked:animate-none motion-reduce:group-hover:translate-y-0">
          <span aria-hidden="true" class="absolute top-5 right-5 size-2 rounded-full bg-white/15 group-has-checked:bg-trb20-g2 group-has-checked:shadow-trb20-dot"></span>
          <span class="text-lg font-bold tracking-[-0.01em] text-white">Nova Pro</span>
          <span class="text-[13px] text-trb20-mut">Deep reasoning</span>
          <span class="mt-3 font-trb20-mono text-xs font-medium tracking-[0.06em] text-trb20-mut uppercase group-has-checked:text-trb20-g2">1M context</span>
        </span>
      </label>
      <label class="group relative cursor-pointer">
        <input type="radio" name="trb-20" value="vision" class="sr-only">
        <span class="relative grid w-[12.5rem] gap-1 rounded-[18px] border-[1.5px] border-transparent [background:linear-gradient(170deg,#171927,#101119)_padding-box,conic-gradient(from_var(--trb20-angle),rgb(255_255_255/0.14),rgb(255_255_255/0.05),rgb(255_255_255/0.14))_border-box] px-5 py-6 transition-[translate] duration-300 group-hover:-translate-y-0.5 group-has-checked:animate-trb20-rotate group-has-checked:[background:linear-gradient(170deg,#171927,#101119)_padding-box,conic-gradient(from_var(--trb20-angle),var(--color-trb20-g1),var(--color-trb20-g2),var(--color-trb20-g1))_border-box] group-has-focus-visible:outline-3 group-has-focus-visible:outline-offset-3 group-has-focus-visible:outline-white motion-reduce:group-has-checked:animate-none motion-reduce:group-hover:translate-y-0">
          <span aria-hidden="true" class="absolute top-5 right-5 size-2 rounded-full bg-white/15 group-has-checked:bg-trb20-g2 group-has-checked:shadow-trb20-dot"></span>
          <span class="text-lg font-bold tracking-[-0.01em] text-white">Nova Vision</span>
          <span class="text-[13px] text-trb20-mut">Image + video in</span>
          <span class="mt-3 font-trb20-mono text-xs font-medium tracking-[0.06em] text-trb20-mut uppercase group-has-checked:text-trb20-g2">Multimodal</span>
        </span>
      </label>
    </div>
  </fieldset>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-trb20-bg: #0b0c12;
  --color-trb20-bg: oklch(0.155 0.01 275);
  --color-trb20-ink: #edeffa;
  --color-trb20-ink: oklch(0.95 0.012 275);
  --color-trb20-mut: #979db8;
  --color-trb20-mut: oklch(0.7 0.03 275);
  --color-trb20-g1: #9b3ff0;
  --color-trb20-g1: oklch(0.6 0.24 300);
  --color-trb20-g2: #35c6d8;
  --color-trb20-g2: oklch(0.75 0.12 205);
  --shadow-trb20-dot: 0 0 10px oklch(0.75 0.12 205 / 0.8);
  --font-trb20-sans: 'Geist', system-ui, sans-serif;
  --font-trb20-mono: 'Geist Mono', ui-monospace, monospace;
  --animate-trb20-rotate: trb20-rotate 5s linear infinite;

  @keyframes trb20-rotate {
    to {
      --trb20-angle: 360deg;
    }
  }
}
/* Registered so the conic angle interpolates. */

@property --trb20-angle {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.trb-20 {
  width: 100%;
  min-height: 100svh;
}
```
