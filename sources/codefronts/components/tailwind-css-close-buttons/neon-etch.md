---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-close-buttons/neon-etch/"
title: "Neon Glow Tailwind Close Button"
section: "components"
category: "tailwind-css-close-buttons"
category_name: "Tailwind CSS Close Buttons"
description: "A neon tube that strikes on hover: the × idles as a dim, lightly glowing filament, then a ballast-misfire keyframe flickers it before three stacked…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neon Glow Tailwind Close Button
Source: https://codefronts.com/components/tailwind-css-close-buttons/neon-etch/

A neon tube that strikes on hover: the × idles as a dim, lightly glowing filament, then a ballast-misfire keyframe flickers it before three stacked drop-shadow() shells lock it at full glow. A blurred after: puddle brightens on the glass below. The port raises the idle state to a legible 3:1 — the original's resting × sat at 35% opacity and nearly vanished.
## HTML
```html
<section class="tcb-21 w-full min-h-svh grid place-items-center bg-[radial-gradient(100%_120%_at_50%_10%,var(--color-tcb21-bg),var(--color-tcb21-bg2))] px-6 py-12 font-tcb21-sans" aria-label="Neon glow close button demo">
  <div class="grid w-full justify-items-center gap-7">
    <button type="button" aria-label="Close" class="group relative grid size-21 cursor-pointer place-items-center rounded-[18px] border border-tcb21-neon/22 bg-linear-160 from-white/5 to-white/1 shadow-[0_20px_44px_-22px_rgb(0_0_0/0.9),inset_0_1px_0_rgb(255_255_255/0.07)] backdrop-blur-sm transition-colors duration-250 after:absolute after:inset-x-3.5 after:bottom-2.5 after:h-2.5 after:rounded-full after:bg-tcb21-neon after:opacity-12 after:blur-[14px] after:transition-opacity after:duration-300 hover:border-tcb21-neon/50 hover:after:opacity-40 focus-visible:border-tcb21-neon/50 focus-visible:outline-[2.5px] focus-visible:outline-offset-3 focus-visible:outline-tcb21-neon focus-visible:after:opacity-40 active:scale-95 motion-reduce:transition-none">
      <span aria-hidden="true" class="relative size-7 opacity-55 drop-shadow-[0_0_2px_var(--color-tcb21-neon)] before:absolute before:top-1/2 before:left-1/2 before:h-[3px] before:w-7 before:-translate-1/2 before:rotate-45 before:rounded-full before:bg-tcb21-tube after:absolute after:top-1/2 after:left-1/2 after:h-[3px] after:w-7 after:-translate-1/2 after:-rotate-45 after:rounded-full after:bg-tcb21-tube group-hover:animate-tcb21-strike group-focus-visible:animate-tcb21-strike motion-reduce:group-hover:animate-none motion-reduce:group-hover:opacity-100 motion-reduce:group-focus-visible:animate-none motion-reduce:group-focus-visible:opacity-100"></span>
    </button>
    <p aria-hidden="true" class="rounded-full px-3.5 py-2 font-tcb21-mono text-[11.5px] text-tcb21-mut ring-1 ring-white/12">drop-shadow ×3 · animate-tcb21-strike · after:blur-[14px]</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcb21-bg: #221a30;
  --color-tcb21-bg: oklch(0.2 0.03 300);
  --color-tcb21-bg2: #110d19;
  --color-tcb21-bg2: oklch(0.12 0.015 290);
  --color-tcb21-neon: #ff5fd2;
  --color-tcb21-neon: oklch(0.75 0.21 335);
  --color-tcb21-tube: #ffc2ec;
  --color-tcb21-tube: oklch(0.9 0.09 340);
  --color-tcb21-mut: #c2a9cf;
  --color-tcb21-mut: oklch(0.77 0.06 320);
  --font-tcb21-sans: 'Geist', system-ui, sans-serif;
  --font-tcb21-mono: 'Geist Mono', ui-monospace, monospace;
  --animate-tcb21-strike: tcb21-strike 0.9s ease-out forwards;

  @keyframes tcb21-strike {
    0% {
      opacity: 0.55;
      filter: drop-shadow(0 0 2px var(--color-tcb21-neon));
    }

    8% {
      opacity: 0.8;
    }

    11%,
        18% {
      opacity: 0.5;
    }

    21% {
      opacity: 0.9;
    }

    24%,
        30% {
      opacity: 0.55;
    }

    55%,
        100% {
      opacity: 1;
      filter: drop-shadow(0 0 2px var(--color-tcb21-neon)) drop-shadow(0 0 6px var(--color-tcb21-neon)) drop-shadow(0 0 14px var(--color-tcb21-neon));
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-21 {
  width: 100%;
  min-height: 100svh;
}
```
