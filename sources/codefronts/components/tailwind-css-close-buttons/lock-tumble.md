---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-close-buttons/lock-tumble/"
title: "Lock Tumbler Tailwind Close Button (@property)"
section: "components"
category: "tailwind-css-close-buttons"
category_name: "Tailwind CSS Close Buttons"
description: "A brass combination dial: the × ratchets through hold-heavy keyframes like tumbler clicks while a masked tick ring counter-spins, its angle driven by a typed…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Lock Tumbler Tailwind Close Button (@property)
Source: https://codefronts.com/components/tailwind-css-close-buttons/lock-tumble/

A brass combination dial: the × ratchets through hold-heavy keyframes like tumbler clicks while a masked tick ring counter-spins, its angle driven by a typed @property. Both motions are @theme animations — --animate-tcb12-tumble and --animate-tcb12-ring — applied with group-hover:animate-tcb12-*. The @property registration is the one thing that must stay CSS.
## HTML
```html
<section class="tcb-12 w-full min-h-svh grid place-items-center bg-[radial-gradient(120%_120%_at_50%_0%,var(--color-tcb12-bg),var(--color-tcb12-bg2))] px-6 py-12 font-tcb12-sans" aria-label="Lock tumbler close button demo">
  <div class="grid w-full justify-items-center gap-7">
    <button type="button" aria-label="Close" class="group relative size-21 cursor-pointer rounded-full bg-[conic-gradient(from_210deg,var(--color-tcb12-ba),var(--color-tcb12-bb)_30%,var(--color-tcb12-ba)_52%,var(--color-tcb12-bb)_78%,var(--color-tcb12-ba))] shadow-[0_18px_40px_-16px_rgb(0_0_0/0.75),inset_0_2px_3px_rgb(255_255_255/0.45),inset_0_-3px_6px_rgb(0_0_0/0.4)] before:absolute before:inset-2.5 before:rounded-full before:bg-[radial-gradient(circle_at_32%_28%,var(--color-tcb12-face1),var(--color-tcb12-face2)_70%)] before:shadow-[inset_0_2px_6px_rgb(0_0_0/0.6)] focus-visible:outline-3 focus-visible:outline-offset-4 focus-visible:outline-tcb12-ba active:scale-94">
      <span aria-hidden="true" class="absolute inset-0.5 rounded-full bg-[repeating-conic-gradient(from_var(--tcb12-a),transparent_0_8deg,var(--color-tcb12-tick)_8deg_10deg)] [mask:radial-gradient(circle,transparent_62%,#000_63%,#000_74%,transparent_75%)] group-hover:animate-tcb12-ring group-focus-visible:animate-tcb12-ring motion-reduce:animate-none!"></span>
      <span aria-hidden="true" class="absolute inset-0 block before:absolute before:top-1/2 before:left-1/2 before:h-[3.5px] before:w-6.5 before:-translate-1/2 before:rotate-45 before:rounded-[2px] before:bg-linear-to-b before:from-tcb12-x1 before:to-tcb12-x2 before:shadow-[0_1px_2px_rgb(0_0_0/0.5)] after:absolute after:top-1/2 after:left-1/2 after:h-[3.5px] after:w-6.5 after:-translate-1/2 after:-rotate-45 after:rounded-[2px] after:bg-linear-to-b after:from-tcb12-x1 after:to-tcb12-x2 after:shadow-[0_1px_2px_rgb(0_0_0/0.5)] group-hover:animate-tcb12-tumble group-focus-visible:animate-tcb12-tumble motion-reduce:animate-none!"></span>
    </button>
    <p aria-hidden="true" class="rounded-full px-3.5 py-2 font-tcb12-mono text-[11.5px] text-tcb12-mut ring-1 ring-white/12">@property --tcb12-a · group-hover:animate-tcb12-ring · [mask:…]</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";
/* The one rule utilities cannot express: a typed custom property, so keyframes can animate a gradient angle. */

@property --tcb12-a {
  syntax: "<angle>";
  inherits: false;
  initial-value: 0deg;
}

@theme {
  --color-tcb12-bg: #3a2d1f;
  --color-tcb12-bg: oklch(0.32 0.04 60);
  --color-tcb12-bg2: #221a12;
  --color-tcb12-bg2: oklch(0.2 0.02 50);
  --color-tcb12-ba: #d8b56a;
  --color-tcb12-ba: oklch(0.78 0.1 85);
  --color-tcb12-bb: #8b6d37;
  --color-tcb12-bb: oklch(0.55 0.09 75);
  --color-tcb12-face1: #574530;
  --color-tcb12-face1: oklch(0.42 0.05 70);
  --color-tcb12-face2: #2e2419;
  --color-tcb12-face2: oklch(0.26 0.03 60);
  --color-tcb12-tick: #332818e6;
  --color-tcb12-tick: oklch(0.3 0.03 60 / 0.9);
  --color-tcb12-x1: #f4e1ae;
  --color-tcb12-x1: oklch(0.92 0.06 85);
  --color-tcb12-x2: #b79a5e;
  --color-tcb12-x2: oklch(0.7 0.08 80);
  --color-tcb12-mut: #cdb89a;
  --color-tcb12-mut: oklch(0.79 0.04 75);
  --font-tcb12-sans: 'Geist', system-ui, sans-serif;
  --font-tcb12-mono: 'Geist Mono', ui-monospace, monospace;
  --animate-tcb12-tumble: tcb12-tumble 1.1s cubic-bezier(0.3,0,0.2,1) 1 both;
  --animate-tcb12-ring: tcb12-ring 2.4s linear infinite;

  @keyframes tcb12-tumble {
    0% {
      transform: rotate(0);
    }

    14%,
        26% {
      transform: rotate(-20deg);
    }

    40%,
        52% {
      transform: rotate(-38deg);
    }

    68%,
        78% {
      transform: rotate(18deg);
    }

    100% {
      transform: rotate(0);
    }
  }

  @keyframes tcb12-ring {
    to {
      --tcb12-a: -360deg;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-12 {
  width: 100%;
  min-height: 100svh;
}
```
