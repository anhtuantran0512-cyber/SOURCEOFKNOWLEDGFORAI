---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-3d-tilt-hover-cards/pure-tailwind-3d-tilt-card-no-javascript/"
title: "Pure Tailwind 3D Tilt Card — No JavaScript (:has() Hover Zones)"
section: "components"
category: "tailwind-css-3d-tilt-hover-cards"
category_name: "Tailwind CSS 3D Tilt Hover Cards"
description: "Zero JavaScript, zero listeners: nine invisible hover zones tile the card, and has-[[data-z=c]:hover]:[--rx:var(--tx)] maps whichever zone the cursor…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure Tailwind 3D Tilt Card — No JavaScript (:has() Hover Zones)
Source: https://codefronts.com/components/tailwind-css-3d-tilt-hover-cards/pure-tailwind-3d-tilt-card-no-javascript/

Zero JavaScript, zero listeners: nine invisible hover zones tile the card, and has-[[data-z=c]:hover]:[--rx:var(--tx)] maps whichever zone the cursor occupies to a tilt pose. Eased transitions blend the nine poses into motion that feels continuous. New in the port: the glare glides between zones because --ttc15-mx/--ttc15-my are registered with @property and transitioned.
## HTML
```html
<section class="ttc-15 w-full min-h-svh grid place-items-center bg-ttc15-bg bg-[radial-gradient(80%_90%_at_25%_15%,var(--color-ttc15-lobe),transparent_60%)] px-6 py-14 font-ttc15-sans text-white" aria-label="Pure Tailwind no-JavaScript 3D tilt card demo">
  <div class="grid w-full justify-items-center gap-8">
    <article class="group/card relative grid aspect-[31/24] w-full max-w-[20rem] grid-cols-3 grid-rows-3 rounded-[22px] border border-white/12 bg-linear-165 from-ttc15-card1 to-ttc15-card2 shadow-[0_28px_58px_-28px_oklch(0_0_0/0.8)] [--tx:10deg] [--ty:10deg] [transform:perspective(1000px)_rotateX(var(--rx,0deg))_rotateY(var(--ry,0deg))] [transition:transform_0.35s_ease,--ttc15-mx_0.35s_ease,--ttc15-my_0.35s_ease]
      has-[[data-z=a]:hover]:[--rx:var(--tx)] has-[[data-z=a]:hover]:[--ry:calc(var(--ty)*-1)] has-[[data-z=a]:hover]:[--ttc15-mx:16%] has-[[data-z=a]:hover]:[--ttc15-my:16%]
      has-[[data-z=b]:hover]:[--rx:var(--tx)] has-[[data-z=b]:hover]:[--ry:0deg] has-[[data-z=b]:hover]:[--ttc15-mx:50%] has-[[data-z=b]:hover]:[--ttc15-my:16%]
      has-[[data-z=c]:hover]:[--rx:var(--tx)] has-[[data-z=c]:hover]:[--ry:var(--ty)] has-[[data-z=c]:hover]:[--ttc15-mx:84%] has-[[data-z=c]:hover]:[--ttc15-my:16%]
      has-[[data-z=d]:hover]:[--rx:0deg] has-[[data-z=d]:hover]:[--ry:calc(var(--ty)*-1)] has-[[data-z=d]:hover]:[--ttc15-mx:16%] has-[[data-z=d]:hover]:[--ttc15-my:50%]
      has-[[data-z=e]:hover]:[--rx:0deg] has-[[data-z=e]:hover]:[--ry:0deg] has-[[data-z=e]:hover]:[--ttc15-mx:50%] has-[[data-z=e]:hover]:[--ttc15-my:50%]
      has-[[data-z=f]:hover]:[--rx:0deg] has-[[data-z=f]:hover]:[--ry:var(--ty)] has-[[data-z=f]:hover]:[--ttc15-mx:84%] has-[[data-z=f]:hover]:[--ttc15-my:50%]
      has-[[data-z=g]:hover]:[--rx:calc(var(--tx)*-1)] has-[[data-z=g]:hover]:[--ry:calc(var(--ty)*-1)] has-[[data-z=g]:hover]:[--ttc15-mx:16%] has-[[data-z=g]:hover]:[--ttc15-my:84%]
      has-[[data-z=h]:hover]:[--rx:calc(var(--tx)*-1)] has-[[data-z=h]:hover]:[--ry:0deg] has-[[data-z=h]:hover]:[--ttc15-mx:50%] has-[[data-z=h]:hover]:[--ttc15-my:84%]
      has-[[data-z=i]:hover]:[--rx:calc(var(--tx)*-1)] has-[[data-z=i]:hover]:[--ry:var(--ty)] has-[[data-z=i]:hover]:[--ttc15-mx:84%] has-[[data-z=i]:hover]:[--ttc15-my:84%]
      has-[:focus-visible]:[--rx:3deg] [@media(hover:none)]:[transform:none] motion-reduce:[transform:none] motion-reduce:[transition:none]">
      <i data-z="a" class="z-30"></i><i data-z="b" class="z-30"></i><i data-z="c" class="z-30"></i>
      <i data-z="d" class="z-30"></i><i data-z="e" class="z-30"></i><i data-z="f" class="z-30"></i>
      <i data-z="g" class="z-30"></i><i data-z="h" class="z-30"></i><i data-z="i" class="z-30"></i>
      <div aria-hidden="true" class="pointer-events-none absolute inset-0 z-10 rounded-[inherit] bg-[radial-gradient(240px_circle_at_var(--ttc15-mx)_var(--ttc15-my),oklch(1_0_0/0.17),transparent_62%)] opacity-0 transition-opacity duration-350 group-hover/card:opacity-100 motion-reduce:hidden"></div>
      <div class="pointer-events-none absolute inset-0 z-20 flex flex-col p-7">
        <p class="font-ttc15-mono text-[10.5px] font-bold tracking-[0.2em] text-ttc15-acc">0 KB OF JAVASCRIPT</p>
        <h3 class="mt-3 text-[30px] leading-none font-bold tracking-[-0.02em]">Pure CSS Tilt</h3>
        <p class="mt-3 text-[14px] leading-[1.55] text-ttc15-mut text-pretty">Nine invisible hover zones + <code class="font-ttc15-mono text-[12.5px] text-white">:has()</code> — no listeners, no library, no main-thread work.</p>
      </div>
      <a href="#" class="pointer-events-auto absolute bottom-7 left-7 z-40 inline-flex min-h-11 items-center rounded-full bg-ttc15-acc px-5 text-[13px] font-semibold text-ttc15-bg no-underline transition-[filter] hover:brightness-110 focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-white">Read the technique</a>
    </article>
    <p aria-hidden="true" class="rounded-full border border-white/12 bg-white/5 px-3.5 py-2 font-ttc15-mono text-[11.5px] text-ttc15-mut">has-[[data-z=c]:hover]:[--rx:var(--tx)] · @property glare</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttc15-bg: #0e0d15;
  --color-ttc15-bg: oklch(0.15 0.015 280);
  --color-ttc15-lobe: #3a3014cc;
  --color-ttc15-lobe: oklch(0.26 0.05 85 / 0.8);
  --color-ttc15-card1: #2a2619;
  --color-ttc15-card1: oklch(0.22 0.03 85);
  --color-ttc15-card2: #16141d;
  --color-ttc15-card2: oklch(0.16 0.02 280);
  --color-ttc15-acc: #f0c14b;
  --color-ttc15-acc: oklch(0.83 0.14 85);
  --color-ttc15-mut: #c9c5cf;
  --color-ttc15-mut: oklch(0.83 0.015 290);
  --font-ttc15-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-ttc15-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Registered so the glare centre INTERPOLATES between zones instead of jumping — an at-rule, so it stays CSS. */

@property --ttc15-mx {
  syntax: "<percentage>";
  inherits: true;
  initial-value: 50%;
}

@property --ttc15-my {
  syntax: "<percentage>";
  inherits: true;
  initial-value: 50%;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttc-15 {
  width: 100%;
  min-height: 100svh;
}
```
