---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-tabs/tailwind-tabs-particle-burst-animation/"
title: "Tailwind Tabs with Particle Burst Animation"
section: "navigation"
category: "tailwind-css-tabs"
category_name: "Tailwind CSS Tabs"
description: "Selecting a tab fires eight coloured sparks outward from its label while a coral underline slides beneath."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Tabs with Particle Burst Animation
Source: https://codefronts.com/navigation/tailwind-css-tabs/tailwind-tabs-particle-burst-animation/

Selecting a tab fires eight coloured sparks outward from its label while a coral underline slides beneath. The original spawned DOM nodes in JavaScript and removed them with timers; the port keeps eight sparks per tab and starts their animation with group-has-checked/tab:animate-ttb12-burst — an animation restarts whenever its selector starts matching.
## HTML
```html
<section class="ttb-12 group/tabs grid min-h-svh w-full place-items-center bg-ttb12-bg bg-[radial-gradient(60%_45%_at_50%_45%,var(--color-ttb12-glow),transparent)] px-5 py-14 font-ttb12-sans text-ttb12-ink" aria-label="Particle burst tabs demo">
  <div class="grid w-full max-w-md justify-items-center gap-9">
    <div role="radiogroup" aria-label="Effect" class="relative flex w-full border-b border-white/10 [--i:0] has-[#ttb12-r2:checked]:[--i:1] has-[#ttb12-r3:checked]:[--i:2] has-[#ttb12-r4:checked]:[--i:3]">
      <label class="group/tab relative flex min-h-12 flex-1 cursor-pointer items-center justify-center text-[13px] font-semibold tracking-[0.04em] text-ttb12-mut transition-colors hover:text-ttb12-ink has-checked:text-ttb12-coral has-focus-visible:outline-2 has-focus-visible:-outline-offset-2 has-focus-visible:outline-ttb12-coral"><input class="sr-only" type="radio" name="ttb12" id="ttb12-r1" checked>Spark<span aria-hidden="true" class="pointer-events-none absolute top-1/2 left-1/2 motion-reduce:hidden"><i class="absolute -top-[3px] -left-[3px] size-1.5 rounded-full bg-ttb12-s1 opacity-0 [--dx:42px] [--dy:0px] group-has-checked/tab:animate-ttb12-burst"></i><i class="absolute -top-[3px] -left-[3px] size-1.5 rounded-full bg-ttb12-s2 opacity-0 [--dx:30px] [--dy:30px] group-has-checked/tab:animate-ttb12-burst"></i><i class="absolute -top-[3px] -left-[3px] size-1.5 rounded-full bg-ttb12-s3 opacity-0 [--dx:0px] [--dy:38px] group-has-checked/tab:animate-ttb12-burst"></i><i class="absolute -top-[3px] -left-[3px] size-1.5 rounded-full bg-ttb12-s4 opacity-0 [--dx:-31px] [--dy:31px] group-has-checked/tab:animate-ttb12-burst"></i><i class="absolute -top-[3px] -left-[3px] size-1.5 rounded-full bg-ttb12-s5 opacity-0 [--dx:-44px] [--dy:0px] group-has-checked/tab:animate-ttb12-burst"></i><i class="absolute -top-[3px] -left-[3px] size-1.5 rounded-full bg-ttb12-s1 opacity-0 [--dx:-29px] [--dy:-29px] group-has-checked/tab:animate-ttb12-burst"></i><i class="absolute -top-[3px] -left-[3px] size-1.5 rounded-full bg-ttb12-s2 opacity-0 [--dx:0px] [--dy:-40px] group-has-checked/tab:animate-ttb12-burst"></i><i class="absolute -top-[3px] -left-[3px] size-1.5 rounded-full bg-ttb12-s3 opacity-0 [--dx:32px] [--dy:-32px] group-has-checked/tab:animate-ttb12-burst"></i></span></label>
      <label class="group/tab relative flex min-h-12 flex-1 cursor-pointer items-center justify-center text-[13px] font-semibold tracking-[0.04em] text-ttb12-mut transition-colors hover:text-ttb12-ink has-checked:text-ttb12-coral has-focus-visible:outline-2 has-focus-visible:-outline-offset-2 has-focus-visible:outline-ttb12-coral"><input class="sr-only" type="radio" name="ttb12" id="ttb12-r2">Bloom<span aria-hidden="true" class="pointer-events-none absolute top-1/2 left-1/2 motion-reduce:hidden"><i class="absolute -top-[3px] -left-[3px] size-1.5 rounded-full bg-ttb12-s1 opacity-0 [--dx:42px] [--dy:0px] group-has-checked/tab:animate-ttb12-burst"></i><i class="absolute -top-[3px] -left-[3px] size-1.5 rounded-full bg-ttb12-s2 opacity-0 [--dx:30px] [--dy:30px] group-has-checked/tab:animate-ttb12-burst"></i><i class="absolute -top-[3px] -left-[3px] size-1.5 rounded-full bg-ttb12-s3 opacity-0 [--dx:0px] [--dy:38px] group-has-checked/tab:animate-ttb12-burst"></i><i class="absolute -top-[3px] -left-[3px] size-1.5 rounded-full bg-ttb12-s4 opacity-0 [--dx:-31px] [--dy:31px] group-has-checked/tab:animate-ttb12-burst"></i><i class="absolute -top-[3px] -left-[3px] size-1.5 rounded-full bg-ttb12-s5 opacity-0 [--dx:-44px] [--dy:0px] group-has-checked/tab:animate-ttb12-burst"></i><i class="absolute -top-[3px] -left-[3px] size-1.5 rounded-full bg-ttb12-s1 opacity-0 [--dx:-29px] [--dy:-29px] group-has-checked/tab:animate-ttb12-burst"></i><i class="absolute -top-[3px] -left-[3px] size-1.5 rounded-full bg-ttb12-s2 opacity-0 [--dx:0px] [--dy:-40px] group-has-checked/tab:animate-ttb12-burst"></i><i class="absolute -top-[3px] -left-[3px] size-1.5 rounded-full bg-ttb12-s3 opacity-0 [--dx:32px] [--dy:-32px] group-has-checked/tab:animate-ttb12-burst"></i></span></label>
      <label class="group/tab relative flex min-h-12 flex-1 cursor-pointer items-center justify-center text-[13px] font-semibold tracking-[0.04em] text-ttb12-mut transition-colors hover:text-ttb12-ink has-checked:text-ttb12-coral has-focus-visible:outline-2 has-focus-visible:-outline-offset-2 has-focus-visible:outline-ttb12-coral"><input class="sr-only" type="radio" name="ttb12" id="ttb12-r3">Burst<span aria-hidden="true" class="pointer-events-none absolute top-1/2 left-1/2 motion-reduce:hidden"><i class="absolute -top-[3px] -left-[3px] size-1.5 rounded-full bg-ttb12-s1 opacity-0 [--dx:42px] [--dy:0px] group-has-checked/tab:animate-ttb12-burst"></i><i class="absolute -top-[3px] -left-[3px] size-1.5 rounded-full bg-ttb12-s2 opacity-0 [--dx:30px] [--dy:30px] group-has-checked/tab:animate-ttb12-burst"></i><i class="absolute -top-[3px] -left-[3px] size-1.5 rounded-full bg-ttb12-s3 opacity-0 [--dx:0px] [--dy:38px] group-has-checked/tab:animate-ttb12-burst"></i><i class="absolute -top-[3px] -left-[3px] size-1.5 rounded-full bg-ttb12-s4 opacity-0 [--dx:-31px] [--dy:31px] group-has-checked/tab:animate-ttb12-burst"></i><i class="absolute -top-[3px] -left-[3px] size-1.5 rounded-full bg-ttb12-s5 opacity-0 [--dx:-44px] [--dy:0px] group-has-checked/tab:animate-ttb12-burst"></i><i class="absolute -top-[3px] -left-[3px] size-1.5 rounded-full bg-ttb12-s1 opacity-0 [--dx:-29px] [--dy:-29px] group-has-checked/tab:animate-ttb12-burst"></i><i class="absolute -top-[3px] -left-[3px] size-1.5 rounded-full bg-ttb12-s2 opacity-0 [--dx:0px] [--dy:-40px] group-has-checked/tab:animate-ttb12-burst"></i><i class="absolute -top-[3px] -left-[3px] size-1.5 rounded-full bg-ttb12-s3 opacity-0 [--dx:32px] [--dy:-32px] group-has-checked/tab:animate-ttb12-burst"></i></span></label>
      <label class="group/tab relative flex min-h-12 flex-1 cursor-pointer items-center justify-center text-[13px] font-semibold tracking-[0.04em] text-ttb12-mut transition-colors hover:text-ttb12-ink has-checked:text-ttb12-coral has-focus-visible:outline-2 has-focus-visible:-outline-offset-2 has-focus-visible:outline-ttb12-coral"><input class="sr-only" type="radio" name="ttb12" id="ttb12-r4">Flare<span aria-hidden="true" class="pointer-events-none absolute top-1/2 left-1/2 motion-reduce:hidden"><i class="absolute -top-[3px] -left-[3px] size-1.5 rounded-full bg-ttb12-s1 opacity-0 [--dx:42px] [--dy:0px] group-has-checked/tab:animate-ttb12-burst"></i><i class="absolute -top-[3px] -left-[3px] size-1.5 rounded-full bg-ttb12-s2 opacity-0 [--dx:30px] [--dy:30px] group-has-checked/tab:animate-ttb12-burst"></i><i class="absolute -top-[3px] -left-[3px] size-1.5 rounded-full bg-ttb12-s3 opacity-0 [--dx:0px] [--dy:38px] group-has-checked/tab:animate-ttb12-burst"></i><i class="absolute -top-[3px] -left-[3px] size-1.5 rounded-full bg-ttb12-s4 opacity-0 [--dx:-31px] [--dy:31px] group-has-checked/tab:animate-ttb12-burst"></i><i class="absolute -top-[3px] -left-[3px] size-1.5 rounded-full bg-ttb12-s5 opacity-0 [--dx:-44px] [--dy:0px] group-has-checked/tab:animate-ttb12-burst"></i><i class="absolute -top-[3px] -left-[3px] size-1.5 rounded-full bg-ttb12-s1 opacity-0 [--dx:-29px] [--dy:-29px] group-has-checked/tab:animate-ttb12-burst"></i><i class="absolute -top-[3px] -left-[3px] size-1.5 rounded-full bg-ttb12-s2 opacity-0 [--dx:0px] [--dy:-40px] group-has-checked/tab:animate-ttb12-burst"></i><i class="absolute -top-[3px] -left-[3px] size-1.5 rounded-full bg-ttb12-s3 opacity-0 [--dx:32px] [--dy:-32px] group-has-checked/tab:animate-ttb12-burst"></i></span></label>
      <span aria-hidden="true" class="pointer-events-none absolute -bottom-px left-0 h-0.5 w-1/4 translate-x-[calc(var(--i)*100%)] rounded-full bg-ttb12-coral shadow-[0_0_12px_var(--color-ttb12-coral)] transition-transform duration-400 ease-[cubic-bezier(0.65,0,0.35,1)] motion-reduce:transition-none"></span>
    </div>
    <p aria-hidden="true" class="rounded-full border border-white/10 px-3.5 py-2 font-ttb12-mono text-[11.5px] text-ttb12-mut">group-has-checked/tab:animate-burst · [--dx] [--dy] · 0 timers</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttb12-bg: #1a1322;
  --color-ttb12-bg: oklch(0.203 0.031 305.2);
  --color-ttb12-glow: #2c1d38;
  --color-ttb12-glow: oklch(0.263 0.053 308.7);
  --color-ttb12-ink: #f7f1fa;
  --color-ttb12-ink: oklch(0.965 0.013 314.8);
  --color-ttb12-mut: #ab9fb8;
  --color-ttb12-mut: oklch(0.721 0.038 307.0);
  --color-ttb12-coral: #ff7a7a;
  --color-ttb12-coral: oklch(0.735 0.163 21.9);
  --color-ttb12-s1: #ff6b6b;
  --color-ttb12-s1: oklch(0.712 0.181 22.8);
  --color-ttb12-s2: #ffd166;
  --color-ttb12-s2: oklch(0.880 0.135 86.1);
  --color-ttb12-s3: #06d6a0;
  --color-ttb12-s3: oklch(0.777 0.160 166.6);
  --color-ttb12-s4: #4cc9f0;
  --color-ttb12-s4: oklch(0.782 0.121 222.5);
  --color-ttb12-s5: #ef476f;
  --color-ttb12-s5: oklch(0.648 0.204 11.1);
  --font-ttb12-sans: 'Geist', system-ui, sans-serif;
  --font-ttb12-mono: 'Geist Mono', ui-monospace, monospace;
  --animate-ttb12-burst: ttb12-burst 0.6s cubic-bezier(0.2, 0.6, 0.4, 1) both;

  @keyframes ttb12-burst {
    from {
      opacity: 1;
      translate: 0 0;
      scale: 1;
    }

    to {
      opacity: 0;
      translate: var(--dx) var(--dy);
      scale: 0.3;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttb-12 {
  width: 100%;
  min-height: 100svh;
}
```
