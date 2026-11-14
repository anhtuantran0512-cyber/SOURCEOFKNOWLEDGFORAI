---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-blockquotes/aurora-gradient-background-tailwind-blockquote/"
title: "Aurora Gradient Background Tailwind Blockquote"
section: "snippets"
category: "tailwind-css-blockquotes"
category_name: "Tailwind CSS Blockquotes"
description: "Three blurred radial blobs drift and screen-blend while a wrapper slowly rotates hue, behind a frosted quote panel."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Aurora Gradient Background Tailwind Blockquote
Source: https://codefronts.com/snippets/tailwind-css-blockquotes/aurora-gradient-background-tailwind-blockquote/

Three blurred radial blobs drift and screen-blend while a wrapper slowly rotates hue, behind a frosted quote panel. The port adds a static star field — eight 1px radial gradients in one bg-[…] — so the aurora reads as sky rather than lava lamp, and sets the quote in Instrument Serif.
## HTML
```html
<section class="tbq-18 relative w-full min-h-svh grid place-items-center overflow-hidden bg-tbq18-bg px-5 py-14 font-tbq18-sans text-tbq18-ink" aria-label="Aurora gradient background blockquote demo">
  <div aria-hidden="true" class="pointer-events-none absolute -inset-[10%] animate-tbq18-hue motion-reduce:animate-none">
    <i class="absolute -top-[18%] -left-[12%] size-[55vmax] animate-tbq18-drift rounded-full bg-[radial-gradient(circle,var(--color-tbq18-b1),transparent_65%)] blur-[70px] mix-blend-screen motion-reduce:animate-none"></i>
    <i class="absolute -top-[6%] -right-[14%] size-[48vmax] animate-tbq18-drift rounded-full bg-[radial-gradient(circle,var(--color-tbq18-b2),transparent_65%)] blur-[70px] mix-blend-screen [animation-direction:alternate-reverse] [animation-duration:31s] motion-reduce:animate-none"></i>
    <i class="absolute -bottom-[28%] left-[22%] size-[42vmax] animate-tbq18-drift rounded-full bg-[radial-gradient(circle,var(--color-tbq18-b3),transparent_65%)] blur-[70px] mix-blend-screen [animation-duration:23s] motion-reduce:animate-none"></i>
  </div>
  <div aria-hidden="true" class="pointer-events-none absolute inset-0 opacity-70 bg-[radial-gradient(1px_1px_at_12%_22%,white,transparent),radial-gradient(1px_1px_at_28%_68%,white,transparent),radial-gradient(1.5px_1.5px_at_44%_12%,white,transparent),radial-gradient(1px_1px_at_61%_80%,white,transparent),radial-gradient(1px_1px_at_72%_30%,white,transparent),radial-gradient(1.5px_1.5px_at_86%_58%,white,transparent),radial-gradient(1px_1px_at_92%_14%,white,transparent),radial-gradient(1px_1px_at_6%_88%,white,transparent)]"></div>
  <div class="relative grid w-full justify-items-center gap-8">
    <figure class="w-full max-w-[580px] rounded-3xl border border-white/16 bg-tbq18-panel p-[clamp(30px,5vw,50px)] text-center shadow-[inset_0_1px_0_oklch(1_0_0/0.14),0_30px_70px_oklch(0_0_0/0.5)] supports-[backdrop-filter:blur(1px)]:bg-tbq18-glass supports-[backdrop-filter:blur(1px)]:backdrop-blur-[14px] supports-[backdrop-filter:blur(1px)]:backdrop-saturate-140">
      <p class="mb-4 text-[11.5px] font-bold tracking-[0.3em] uppercase text-tbq18-mut">Above the weather</p>
      <blockquote>
        <p class="font-tbq18-display text-[clamp(32px,4.6vw,50px)] leading-[1.1] tracking-[-0.01em] text-balance [text-shadow:0_2px_12px_oklch(0_0_0/0.3)]">“Somewhere, something incredible is waiting to be known.”</p>
      </blockquote>
      <figcaption class="mt-5 text-sm text-tbq18-mut">— Carl Sagan</figcaption>
    </figure>
    <p aria-hidden="true" class="rounded-full border border-white/14 bg-tbq18-glass px-3.5 py-2 font-tbq18-mono text-[11.5px] text-tbq18-mut">mix-blend-screen blobs · animate-tbq18-hue · star field bg-[…]</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbq18-bg: #070811;
  --color-tbq18-bg: oklch(0.14 0.02 275);
  --color-tbq18-ink: #f2f5fb;
  --color-tbq18-ink: oklch(0.97 0.008 260);
  --color-tbq18-mut: #b3bfd2;
  --color-tbq18-mut: oklch(0.8 0.03 260);
  --color-tbq18-panel: #1314238c;
  --color-tbq18-panel: oklch(0.2 0.03 280 / 0.55);
  --color-tbq18-glass: #13142352;
  --color-tbq18-glass: oklch(0.2 0.03 280 / 0.32);
  --color-tbq18-b1: #00cfdd80;
  --color-tbq18-b1: oklch(0.75 0.19 200 / 0.5);
  --color-tbq18-b2: #845cf773;
  --color-tbq18-b2: oklch(0.6 0.22 290 / 0.45);
  --color-tbq18-b3: #e45cbe66;
  --color-tbq18-b3: oklch(0.68 0.2 340 / 0.4);
  --font-tbq18-display: 'Instrument Serif', Georgia, serif;
  --font-tbq18-sans: 'Geist', system-ui, sans-serif;
  --font-tbq18-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tbq18-drift: tbq18-drift 26s ease-in-out infinite alternate;
  --animate-tbq18-hue: tbq18-hue 44s linear infinite;

  @keyframes tbq18-drift {
    from {
      transform: translate(-8%, -6%) scale(1);
    }

    to {
      transform: translate(10%, 8%) scale(1.18);
    }
  }

  @keyframes tbq18-hue {
    to {
      filter: hue-rotate(360deg);
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tbq-18 {
  width: 100%;
  min-height: 100svh;
}
```
