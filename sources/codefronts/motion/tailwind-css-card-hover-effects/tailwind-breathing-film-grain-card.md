---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-breathing-film-grain-card/"
title: "Tailwind Breathing Film Grain Card with SVG Turbulence Noise"
section: "motion"
category: "tailwind-css-card-hover-effects"
category_name: "Tailwind CSS Card Hover Effects"
description: "A sepia Super-8 card whose grain breathes faster and stronger on hover."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Breathing Film Grain Card with SVG Turbulence Noise
Source: https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-breathing-film-grain-card/

A sepia Super-8 card whose grain breathes faster and stronger on hover. The noise is a data-URI SVG feTurbulence &mdash; real fractal noise, not dots &mdash; and the hover doesn't start an animation so much as speed one up.
## HTML
```html
<section class="tch-26 w-full min-h-svh grid place-items-center bg-tch26-bg font-tch26-mono p-8">
  <article tabindex="0" class="group relative w-[330px] h-[440px] rounded-lg overflow-hidden cursor-pointer outline-none bg-[linear-gradient(160deg,#3a2e22,#1b140d)] shadow-[0_20px_45px_rgb(0_0_0/0.5)] focus-visible:outline-2 focus-visible:outline-tch26-acc focus-visible:outline-offset-4 before:content-[''] before:absolute before:inset-0 before:bg-[radial-gradient(ellipse_at_50%_35%,rgb(210_170_110/0.35),transparent_60%),linear-gradient(160deg,#5a4732,#241a10)] after:content-[''] after:absolute after:inset-0 after:z-3 after:pointer-events-none after:shadow-[inset_0_0_90px_rgb(0_0_0/0.7)]">
    <div class="absolute -inset-1/2 z-2 pointer-events-none opacity-12 mix-blend-overlay animate-tch26-drift transition-opacity duration-500 group-hover:opacity-42 group-hover:[animation-duration:0.25s] group-focus-visible:opacity-42 motion-reduce:animate-none bg-[url('data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22120%22%20height%3D%22120%22%3E%3Cfilter%20id%3D%22n%22%3E%3CfeTurbulence%20type%3D%22fractalNoise%22%20baseFrequency%3D%220.9%22%20numOctaves%3D%223%22%20stitchTiles%3D%22stitch%22%2F%3E%3C%2Ffilter%3E%3Crect%20width%3D%22100%25%22%20height%3D%22100%25%22%20filter%3D%22url(%23n)%22%2F%3E%3C%2Fsvg%3E')]"></div>
    <div class="relative z-4 h-full p-[2.4rem] flex flex-col justify-between text-tch26-ink">
      <span class="text-[0.72rem] tracking-[0.2em] text-tch26-acc">SUPER 8 · 1974</span>
      <h2 class="font-tch26-display font-semibold italic text-[3rem] leading-[0.95]">Golden<br>Hour Reel</h2>
      <p class="text-[0.82rem] leading-[1.65] text-tch26-body">A scanned film transfer. Hover and the grain breathes, like light running through celluloid.</p>
    </div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@keyframes tch26-drift {
  0% {
    transform: translate(0,0);
  }

  25% {
    transform: translate(-8%, 5%);
  }

  50% {
    transform: translate(6%, -8%);
  }

  75% {
    transform: translate(-5%, -4%);
  }

  100% {
    transform: translate(7%, 6%);
  }
}

@theme {
  --color-tch26-bg: #16130f;
  --color-tch26-bg: oklch(0.18 0.01 70);
  --color-tch26-ink: #f0e2cc;
  --color-tch26-ink: oklch(0.92 0.03 80);
  --color-tch26-body: #c4b39a;
  --color-tch26-body: oklch(0.77 0.03 80);
  --color-tch26-acc: #c9a877;
  --color-tch26-acc: oklch(0.74 0.07 75);
  --font-tch26-mono: 'Fragment Mono', ui-monospace, monospace;
  --font-tch26-display: 'Cormorant', Georgia, serif;
  --animate-tch26-drift: tch26-drift 0.6s steps(4) infinite;
}

.tch-26 {
  width: 100%;
  min-height: 100svh;
}
```
