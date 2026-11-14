---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-close-buttons/galaxy-vortex/"
title: "Galaxy Vortex Tailwind Close Button"
section: "components"
category: "tailwind-css-close-buttons"
category_name: "Tailwind CSS Close Buttons"
description: "A spiral galaxy in a button: two conic-gradient arm layers counter-rotate at co-prime speeds (11s and 7s) via two typed @property angles, a ten-star field is…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Galaxy Vortex Tailwind Close Button
Source: https://codefronts.com/components/tailwind-css-close-buttons/galaxy-vortex/

A spiral galaxy in a button: two conic-gradient arm layers counter-rotate at co-prime speeds (11s and 7s) via two typed @property angles, a ten-star field is a single box-shadow, and hover whips both arms up to 3.5s/2.2s with group-hover:[animation-duration:3.5s] as the × slowly spins and shrinks into the vortex.
## HTML
```html
<section class="tcb-28 w-full min-h-svh grid place-items-center bg-[radial-gradient(100%_120%_at_50%_0%,var(--color-tcb28-bg),var(--color-tcb28-bg2))] px-6 py-12 font-tcb28-sans" aria-label="Galaxy vortex close button demo">
  <div class="grid w-full justify-items-center gap-7">
    <button type="button" aria-label="Close" class="group relative grid size-[110px] cursor-pointer place-items-center overflow-hidden rounded-full bg-tcb28-core shadow-[0_0_0_1px_var(--color-tcb28-rim),0_24px_60px_-24px_var(--color-tcb28-glow)] focus-visible:outline-[2.5px] focus-visible:outline-offset-4 focus-visible:outline-tcb28-arm-b active:scale-94">
      <span aria-hidden="true" class="absolute inset-0 rounded-full bg-[conic-gradient(from_var(--tcb28-a),transparent_0_40deg,var(--color-tcb28-arm-a)_60deg_80deg,transparent_100deg_160deg,var(--color-tcb28-arm-a)_185deg_205deg,transparent_225deg_290deg,var(--color-tcb28-arm-a)_310deg_330deg,transparent_350deg)] [mask:radial-gradient(circle,#000_0_70%,transparent_71%)] animate-tcb28-arm-a group-hover:[animation-duration:3.5s] group-focus-visible:[animation-duration:3.5s] motion-reduce:animate-none"></span>
      <span aria-hidden="true" class="absolute inset-0 rounded-full bg-[conic-gradient(from_var(--tcb28-b),transparent_0_70deg,var(--color-tcb28-arm-b2)_90deg_105deg,transparent_125deg_200deg,var(--color-tcb28-arm-b2)_225deg_245deg,transparent_265deg)] [mask:radial-gradient(circle,#000_0_55%,transparent_56%)] animate-tcb28-arm-b group-hover:[animation-duration:2.2s] group-focus-visible:[animation-duration:2.2s] motion-reduce:animate-none"></span>
      <span aria-hidden="true" class="absolute top-[18%] left-[22%] size-[1.5px] rounded-full bg-white shadow-[12px_30px_0_0_rgb(255_255_255/0.8),34px_8px_0_-0.4px_rgb(255_255_255/0.6),55px_42px_0_0_rgb(255_255_255/0.9),70px_15px_0_-0.5px_rgb(255_255_255/0.5),20px_58px_0_-0.4px_rgb(255_255_255/0.7),46px_66px_0_0_rgb(255_255_255/0.6),64px_55px_0_-0.6px_rgb(255_255_255/0.45),6px_44px_0_-0.5px_rgb(255_255_255/0.55),40px_24px_0_-0.6px_rgb(255_255_255/0.5),58px_4px_0_-0.4px_rgb(255_255_255/0.65)]"></span>
      <span aria-hidden="true" class="relative size-5.5 drop-shadow-[0_0_6px_var(--color-tcb28-arm-b)] transition-[rotate,scale] duration-[2.2s] ease-[cubic-bezier(.3,0,.2,1)] before:absolute before:top-1/2 before:left-1/2 before:h-[2.5px] before:w-5.5 before:-translate-1/2 before:rotate-45 before:rounded-full before:bg-white after:absolute after:top-1/2 after:left-1/2 after:h-[2.5px] after:w-5.5 after:-translate-1/2 after:-rotate-45 after:rounded-full after:bg-white group-hover:rotate-180 group-hover:scale-75 group-focus-visible:rotate-180 group-focus-visible:scale-75 motion-reduce:transition-none"></span>
    </button>
    <p aria-hidden="true" class="rounded-full px-3.5 py-2 font-tcb28-mono text-[11.5px] text-tcb28-mut ring-1 ring-white/12">2× @property angles · 11s / 7s co-prime · box-shadow starfield</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";
/* The one rule utilities cannot express: typed angle properties, so keyframes can rotate a conic gradient. */

@property --tcb28-a {
  syntax: "<angle>";
  inherits: false;
  initial-value: 0deg;
}

@property --tcb28-b {
  syntax: "<angle>";
  inherits: false;
  initial-value: 0deg;
}

@theme {
  --color-tcb28-bg: #1a1328;
  --color-tcb28-bg: oklch(0.17 0.03 290);
  --color-tcb28-bg2: #0b0911;
  --color-tcb28-bg2: oklch(0.1 0.015 280);
  --color-tcb28-core: #120e1c;
  --color-tcb28-core: oklch(0.14 0.02 290);
  --color-tcb28-rim: #8a4fd840;
  --color-tcb28-rim: oklch(0.6 0.2 300 / 0.25);
  --color-tcb28-glow: #7a3fc799;
  --color-tcb28-glow: oklch(0.5 0.2 300 / 0.6);
  --color-tcb28-arm-a: #8a4fd859;
  --color-tcb28-arm-a: oklch(0.6 0.2 300 / 0.35);
  --color-tcb28-arm-b: #5fb0e6;
  --color-tcb28-arm-b: oklch(0.72 0.12 225);
  --color-tcb28-arm-b2: #5fb0e64d;
  --color-tcb28-arm-b2: oklch(0.72 0.12 225 / 0.3);
  --color-tcb28-mut: #b5a9cc;
  --color-tcb28-mut: oklch(0.76 0.05 295);
  --font-tcb28-sans: 'Geist', system-ui, sans-serif;
  --font-tcb28-mono: 'Geist Mono', ui-monospace, monospace;
  --animate-tcb28-arm-a: tcb28-arm-a 11s linear infinite;
  --animate-tcb28-arm-b: tcb28-arm-b 7s linear infinite reverse;

  @keyframes tcb28-arm-a {
    to {
      --tcb28-a: 360deg;
    }
  }

  @keyframes tcb28-arm-b {
    to {
      --tcb28-b: 360deg;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-28 {
  width: 100%;
  min-height: 100svh;
}
```
