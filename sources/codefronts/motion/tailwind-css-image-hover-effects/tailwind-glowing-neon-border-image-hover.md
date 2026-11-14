---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-image-hover-effects/tailwind-glowing-neon-border-image-hover/"
title: "Tailwind Glowing Neon Border Image Hover"
section: "motion"
category: "tailwind-css-image-hover-effects"
category_name: "Tailwind CSS Image Hover Effects"
description: "Three stacked shadows in one property &mdash; hairline, 20px bloom, 60px ambient &mdash; driven by a per-card --glow custom property, so one class list glows…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Glowing Neon Border Image Hover
Source: https://codefronts.com/motion/tailwind-css-image-hover-effects/tailwind-glowing-neon-border-image-hover/

Three stacked shadows in one property &mdash; hairline, 20px bloom, 60px ambient &mdash; driven by a per-card --glow custom property, so one class list glows in three colours. The corner brackets, which the CSS version builds from two pseudo-elements, become before: and after: utilities on the frame.
## HTML
```html
<section class="tih-10 w-full min-h-svh grid place-items-center bg-tih10-bg font-tih10-sans px-6 py-10" aria-label="Neon glow border image hover demo">
  <div class="grid w-full max-w-195 gap-5 grid-cols-1 sm:grid-cols-3">
    <article style="--glow:oklch(0.82 0.15 320); --glow-dim:oklch(0.82 0.15 320/0.25); --glow2:oklch(0.79 0.13 205)" class="group relative rounded-[14px] border border-[oklch(1_0_0/0.06)] transition-[box-shadow,border-color] duration-400 ease-tih10 hover:border-[var(--glow)] hover:shadow-[0_0_0_1px_var(--glow),0_0_20px_var(--glow),0_0_60px_var(--glow-dim)] motion-reduce:transition-none">
      <div class="relative aspect-square grid place-items-center overflow-hidden rounded-t-[13px] text-[var(--glow)] bg-[image:url('https://picsum.photos/seed/tih10-gpu/600/600'),linear-gradient(135deg,oklch(0.16_0.06_305),oklch(0.28_0.14_305),oklch(0.42_0.2_302))] bg-cover bg-center bg-no-repeat before:content-[''] before:absolute before:top-2 before:left-2 before:w-4 before:h-4 before:border-t-2 before:border-l-2 before:border-current before:opacity-0 before:transition-opacity before:duration-400 after:content-[''] after:absolute after:bottom-2 after:right-2 after:w-4 after:h-4 after:border-b-2 after:border-r-2 after:border-current after:opacity-0 after:transition-opacity after:duration-400 group-hover:before:opacity-100 group-hover:after:opacity-100 motion-reduce:before:transition-none motion-reduce:after:transition-none">
      </div>
      <div class="px-4 py-3.5 rounded-b-[13px] bg-[oklch(0_0_0/0.3)]">
        <h3 class="text-[13px] font-bold text-tih10-text">Cipher X9 GPU</h3>
        <p class="mt-0.75 text-[11px] text-tih10-muted">24GB GDDR7 &middot; Ray Tracing</p>
        <p class="mt-2 text-xs font-extrabold bg-clip-text text-transparent bg-linear-[90deg,var(--glow),var(--glow2)]">&#9733; 98 / 100 Performance</p>
      </div>
    </article>
    <article style="--glow:oklch(0.79 0.13 205); --glow-dim:oklch(0.79 0.13 205/0.25); --glow2:oklch(0.88 0.13 150)" class="group relative rounded-[14px] border border-[oklch(1_0_0/0.06)] transition-[box-shadow,border-color] duration-400 ease-tih10 hover:border-[var(--glow)] hover:shadow-[0_0_0_1px_var(--glow),0_0_20px_var(--glow),0_0_60px_var(--glow-dim)] motion-reduce:transition-none">
      <div class="relative aspect-square grid place-items-center overflow-hidden rounded-t-[13px] text-[var(--glow)] bg-[image:url('https://picsum.photos/seed/tih10-oled/600/600'),linear-gradient(135deg,oklch(0.17_0.04_230),oklch(0.3_0.07_230),oklch(0.42_0.1_232))] bg-cover bg-center bg-no-repeat before:content-[''] before:absolute before:top-2 before:left-2 before:w-4 before:h-4 before:border-t-2 before:border-l-2 before:border-current before:opacity-0 before:transition-opacity before:duration-400 after:content-[''] after:absolute after:bottom-2 after:right-2 after:w-4 after:h-4 after:border-b-2 after:border-r-2 after:border-current after:opacity-0 after:transition-opacity after:duration-400 group-hover:before:opacity-100 group-hover:after:opacity-100 motion-reduce:before:transition-none motion-reduce:after:transition-none">
      </div>
      <div class="px-4 py-3.5 rounded-b-[13px] bg-[oklch(0_0_0/0.3)]">
        <h3 class="text-[13px] font-bold text-tih10-text">Horizon 4K OLED</h3>
        <p class="mt-0.75 text-[11px] text-tih10-muted">240Hz &middot; 1ms GTG &middot; HDR</p>
        <p class="mt-2 text-xs font-extrabold bg-clip-text text-transparent bg-linear-[90deg,var(--glow),var(--glow2)]">&#9733; 96 / 100 Visuals</p>
      </div>
    </article>
    <article style="--glow:oklch(0.88 0.13 150); --glow-dim:oklch(0.88 0.13 150/0.25); --glow2:oklch(0.82 0.15 320)" class="group relative rounded-[14px] border border-[oklch(1_0_0/0.06)] transition-[box-shadow,border-color] duration-400 ease-tih10 hover:border-[var(--glow)] hover:shadow-[0_0_0_1px_var(--glow),0_0_20px_var(--glow),0_0_60px_var(--glow-dim)] motion-reduce:transition-none">
      <div class="relative aspect-square grid place-items-center overflow-hidden rounded-t-[13px] text-[var(--glow)] bg-[image:url('https://picsum.photos/seed/tih10-keyboard/600/600'),linear-gradient(135deg,oklch(0.16_0.04_160),oklch(0.3_0.08_162),oklch(0.38_0.09_163))] bg-cover bg-center bg-no-repeat before:content-[''] before:absolute before:top-2 before:left-2 before:w-4 before:h-4 before:border-t-2 before:border-l-2 before:border-current before:opacity-0 before:transition-opacity before:duration-400 after:content-[''] after:absolute after:bottom-2 after:right-2 after:w-4 after:h-4 after:border-b-2 after:border-r-2 after:border-current after:opacity-0 after:transition-opacity after:duration-400 group-hover:before:opacity-100 group-hover:after:opacity-100 motion-reduce:before:transition-none motion-reduce:after:transition-none">
      </div>
      <div class="px-4 py-3.5 rounded-b-[13px] bg-[oklch(0_0_0/0.3)]">
        <h3 class="text-[13px] font-bold text-tih10-text">Spectra 75% MK</h3>
        <p class="mt-0.75 text-[11px] text-tih10-muted">Optical &middot; Per-key RGB</p>
        <p class="mt-2 text-xs font-extrabold bg-clip-text text-transparent bg-linear-[90deg,var(--glow),var(--glow2)]">&#9733; 94 / 100 Feel</p>
      </div>
    </article>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tih10-bg: #030308;
  --color-tih10-bg: oklch(0.08 0.008 285);
  --color-tih10-text: #f1f5f9;
  --color-tih10-text: oklch(0.96 0.005 250);
  --color-tih10-muted: #64748b;
  --color-tih10-muted: oklch(0.58 0.035 255);
  --font-tih10-sans: 'Space Grotesk', system-ui, sans-serif;
  --ease-tih10: cubic-bezier(0.25, 0.46, 0.45, 0.94);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the stage is correctly sized before the browser build compiles. */

.tih-10 {
  width: 100%;
  min-height: 100svh;
}

.tih-10 ::selection {
  background: oklch(0.82 0.15 320);
  color: #000;
}
```
