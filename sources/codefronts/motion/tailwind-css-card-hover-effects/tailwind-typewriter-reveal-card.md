---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-typewriter-reveal-card/"
title: "Tailwind Typewriter Reveal Card with Steps Animation & Caret"
section: "motion"
category: "tailwind-css-card-hover-effects"
category_name: "Tailwind CSS Card Hover Effects"
description: "A field-journal card that types its two-line entry on hover, caret blinking, on aged grain paper."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Typewriter Reveal Card with Steps Animation & Caret
Source: https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-typewriter-reveal-card/

A field-journal card that types its two-line entry on hover, caret blinking, on aged grain paper. The reveal is a width animation stepped by character count &mdash; which makes it the one demo where the keyframes and the copy are coupled, and the port makes that coupling visible.
## HTML
```html
<section class="tch-24 w-full min-h-svh grid place-items-center bg-tch24-bg bg-[radial-gradient(circle_at_50%_50%,#e8e1d2,#c9c0ad)] font-tch24-mono p-8">
  <article tabindex="0" class="group relative w-[350px] h-[440px] rounded overflow-hidden cursor-pointer outline-none bg-tch24-paper border border-tch24-edge shadow-[0_16px_36px_rgb(60_50_30/0.25)] focus-visible:outline-2 focus-visible:outline-tch24-ink focus-visible:outline-offset-4 before:content-[''] before:absolute before:inset-0 before:pointer-events-none before:bg-[radial-gradient(rgb(120_100_70/0.06)_0.5px,transparent_0.6px)] before:bg-[length:4px_4px]">
    <div class="relative z-2 h-full p-[2.4rem] flex flex-col text-tch24-ink">
      <div class="text-[0.72rem] tracking-[0.18em] uppercase text-tch24-mut border-b border-tch24-edge pb-3 mb-6">Dispatch No. 14 — Field Log</div>
      <h2 class="font-tch24-display text-[2rem] leading-[1.15] mb-5 min-h-[4.6rem]">The Cartographer's<br>Last Letter</h2>
      <p class="font-tch24-display text-[0.95rem] leading-[1.7] w-0 overflow-hidden whitespace-nowrap border-r-2 border-r-transparent group-hover:animate-tch24-type-a group-focus-visible:animate-tch24-type-a motion-reduce:w-full motion-reduce:animate-none">They said the river had no end —</p>
      <p class="font-tch24-display text-[0.95rem] leading-[1.7] w-0 overflow-hidden whitespace-nowrap border-r-2 border-r-transparent group-hover:animate-tch24-type-b group-focus-visible:animate-tch24-type-b motion-reduce:w-full motion-reduce:animate-none">so I followed it anyway.</p>
      <div class="mt-auto text-[0.75rem] tracking-[0.1em] text-tch24-mut">— hover to type the entry —</div>
    </div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@keyframes tch24-type {
  from {
    width: 0;
    border-right-color: var(--color-tch24-ink);
  }

  99% {
    border-right-color: var(--color-tch24-ink);
  }

  to {
    width: 100%;
    border-right-color: transparent;
  }
}

@theme {
  --color-tch24-bg: #ddd6c7;
  --color-tch24-bg: oklch(0.87 0.02 85);
  --color-tch24-paper: #f7f2e7;
  --color-tch24-paper: oklch(0.96 0.015 85);
  --color-tch24-edge: #d8cfba;
  --color-tch24-edge: oklch(0.85 0.02 85);
  --color-tch24-ink: #2c2419;
  --color-tch24-ink: oklch(0.26 0.02 70);
  --color-tch24-mut: #8a7a5a;
  --color-tch24-mut: oklch(0.57 0.04 80);
  --font-tch24-mono: 'Courier Prime', ui-monospace, monospace;
  --font-tch24-display: 'Special Elite', ui-monospace, monospace;
  --animate-tch24-type-a: tch24-type 2.2s steps(32) forwards;
  --animate-tch24-type-b: tch24-type 1.8s steps(24) 2.2s forwards;
}

.tch-24 {
  width: 100%;
  min-height: 100svh;
}
```
