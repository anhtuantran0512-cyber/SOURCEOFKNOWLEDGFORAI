---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-isometric-illustration-hero-section/"
title: "Isometric Illustration Hero Section in Tailwind CSS"
section: "layouts"
category: "tailwind-css-hero-sections"
category_name: "Tailwind CSS Hero Sections"
description: "A cozy work-from-home isometric scene — desk, glowing laptop, steaming mug, plant and lamp — built from CSS boxes in true 3D with preserve-3d."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Isometric Illustration Hero Section in Tailwind CSS
Source: https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-isometric-illustration-hero-section/

A cozy work-from-home isometric scene — desk, glowing laptop, steaming mug, plant and lamp — built from CSS boxes in true 3D with preserve-3d. Mauve, dusty rose and sage, with a gentle float so the room feels alive.
## HTML
```html
<section class="ths-26 grid w-full min-h-svh items-center gap-10 bg-ths26-bg bg-[radial-gradient(70%_60%_at_70%_30%,rgb(216_150_180/0.22),transparent_70%)] px-5 py-16 font-ths26-sans text-ths26-ink sm:px-12 lg:grid-cols-2 lg:gap-14" aria-label="Isometric illustration hero">
  <div class="max-w-lg">
    <span class="font-ths26-mono text-[11px] tracking-[0.16em] text-ths26-mauve">/ for the home office crowd</span>
    <h1 class="mt-4 font-ths26-serif text-[clamp(38px,5.4vw,60px)] leading-[1.04] font-semibold tracking-[-0.015em] text-balance">Deep work, <em class="text-ths26-mauve">without the doom-tabs.</em></h1>
    <p class="mt-5 max-w-md text-base/relaxed text-ths26-body">A focus timer that stays in the menu bar, not your face. Three tasks a day, one calm afternoon.</p>
    <div class="mt-8 flex flex-wrap items-center gap-4">
      <a href="#start" class="inline-flex min-h-12 items-center rounded-full bg-ths26-ink px-6 text-[15px] font-semibold text-ths26-bg transition hover:bg-ths26-mauve focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-ths26-ink motion-reduce:transition-none">Start a session →</a>
      <span class="inline-flex items-center gap-2 rounded-full bg-white/70 px-4 py-2 font-ths26-mono text-xs text-ths26-body"><span aria-hidden="true" class="size-2 rounded-full bg-ths26-sage"></span>25:00 focus · macOS &amp; Windows</span>
    </div>
  </div>
  <div aria-hidden="true" class="grid min-h-[380px] place-items-center [perspective:1000px]">
    <div class="scale-[1.25] animate-ths26-float transform-3d motion-reduce:animate-none sm:scale-[1.45]">
      <div class="relative h-[150px] w-[230px] rounded-md bg-linear-135 from-ths26-oak to-ths26-oak2 shadow-[0_10px_0_var(--color-ths26-oak3),0_40px_50px_-10px_rgb(74_40_64/0.35)] transform-3d [transform:rotateX(60deg)_rotateZ(-45deg)]">
        <div class="absolute top-[22%] left-[22%] h-[52px] w-[78px] rounded bg-ths26-ink transform-3d [transform:translateZ(2px)]">
          <div class="absolute -top-[54px] left-0 h-[54px] w-full origin-bottom rounded-t bg-ths26-ink p-1 [transform:rotateX(-100deg)]"><div class="size-full rounded-sm bg-linear-to-br from-ths26-rose to-ths26-blush shadow-[0_0_24px_rgb(216_168_192/0.8)]"></div></div>
        </div>
        <div class="absolute top-[24%] right-[12%] size-6 rounded-full bg-ths26-sage shadow-[0_3px_0_var(--color-ths26-sage2)] transform-3d [transform:translateZ(4px)]">
          <span class="absolute bottom-full left-1 h-6 w-1 origin-bottom animate-ths26-steam rounded-full bg-white/70 [transform:rotateX(-90deg)] motion-reduce:hidden"></span>
          <span class="absolute bottom-full left-3.5 h-5 w-1 origin-bottom animate-ths26-steam rounded-full bg-white/60 [animation-delay:-1s] [transform:rotateX(-90deg)] motion-reduce:hidden"></span>
        </div>
        <div class="absolute right-[6%] bottom-[10%] size-8 rounded-md bg-ths26-oak3 transform-3d [transform:translateZ(2px)]">
          <div class="absolute bottom-full left-1/2 h-12 w-8 origin-bottom -translate-x-1/2 [transform:rotateX(-90deg)]"><span class="absolute bottom-0 left-1/2 h-10 w-1.5 -translate-x-1/2 rounded-full bg-ths26-leaf2"></span><span class="absolute bottom-4 left-0 h-6 w-4 rounded-[100%_0] bg-ths26-leaf"></span><span class="absolute right-0 bottom-6 h-6 w-4 rounded-[0_100%] bg-ths26-leaf"></span></div>
        </div>
        <div class="absolute top-[8%] left-[6%] size-5 rounded-full bg-ths26-rose transform-3d [transform:translateZ(2px)]">
          <div class="absolute bottom-full left-1/2 h-16 w-10 origin-bottom -translate-x-1/2 [transform:rotateX(-90deg)]"><span class="absolute bottom-0 left-1/2 h-14 w-1 -translate-x-1/2 bg-ths26-rose"></span><span class="absolute top-0 left-0 h-5 w-10 rounded-t-full bg-ths26-peach shadow-[0_8px_30px_rgb(240_192_168/0.9)]"></span></div>
        </div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ths26-bg: #f0e8e2;
  --color-ths26-bg: oklch(0.936 0.012 59.6);
  --color-ths26-ink: #4a2840;
  --color-ths26-ink: oklch(0.33 0.062 338.9);
  --color-ths26-body: #5e3f50;
  --color-ths26-body: oklch(0.409 0.05 345.5);
  --color-ths26-mauve: #84516f;
  --color-ths26-mauve: oklch(0.503 0.08 344.2);
  --color-ths26-rose: #d8a8c0;
  --color-ths26-rose: oklch(0.782 0.064 347.2);
  --color-ths26-blush: #f4d4e2;
  --color-ths26-blush: oklch(0.901 0.04 349.7);
  --color-ths26-peach: #f0c0a8;
  --color-ths26-peach: oklch(0.844 0.064 47.9);
  --color-ths26-sage: #b5cfa0;
  --color-ths26-sage: oklch(0.823 0.07 131.4);
  --color-ths26-sage2: #8aa877;
  --color-ths26-sage2: oklch(0.696 0.077 133.7);
  --color-ths26-leaf: #7fa37a;
  --color-ths26-leaf: oklch(0.677 0.071 141.6);
  --color-ths26-leaf2: #5e7f5a;
  --color-ths26-leaf2: oklch(0.561 0.067 141.9);
  --color-ths26-oak: #e0c8a8;
  --color-ths26-oak: oklch(0.845 0.051 74.9);
  --color-ths26-oak2: #b89878;
  --color-ths26-oak2: oklch(0.701 0.059 66.6);
  --color-ths26-oak3: #9a7a5c;
  --color-ths26-oak3: oklch(0.603 0.059 64.5);
  --font-ths26-serif: 'Cormorant Garamond', Georgia, serif;
  --font-ths26-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-ths26-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-ths26-float: ths26-float 6s ease-in-out infinite;
  --animate-ths26-steam: ths26-steam 2.4s ease-out infinite;

  @keyframes ths26-float {
    50% {
      translate: 0 -8px;
    }
  }

  @keyframes ths26-steam {
    0% {
      opacity: 0;
      scale: 1 0.4;
    }

    40% {
      opacity: 1;
    }

    100% {
      opacity: 0;
      scale: 1 1.4;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ths-26 {
  width: 100%;
  min-height: 100svh;
}
```
