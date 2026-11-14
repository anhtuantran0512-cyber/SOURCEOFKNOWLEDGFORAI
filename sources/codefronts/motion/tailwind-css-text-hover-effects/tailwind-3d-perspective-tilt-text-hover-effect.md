---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-3d-perspective-tilt-text-hover-effect/"
title: "Tailwind 3D Perspective Tilt Text Hover Effect"
section: "motion"
category: "tailwind-css-text-hover-effects"
category_name: "Tailwind CSS Text Hover Effects"
description: "A conference wordmark that leans toward the cursor from any corner — without JavaScript."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind 3D Perspective Tilt Text Hover Effect
Source: https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-3d-perspective-tilt-text-hover-effect/

A conference wordmark that leans toward the cursor from any corner — without JavaScript. Four invisible quadrant zones are named peers (peer/tl…peer/br); the word reads peer-hover/tl:rotate-x-[11deg] peer-hover/tl:-rotate-y-[13deg] and a matching shadow that always falls away from the tilt. Keyboard focus plays a gentle sway.
## HTML
```html
<section class="tth-22 w-full min-h-svh grid place-items-center bg-tth22-bg bg-[radial-gradient(80%_65%_at_50%_30%,var(--color-tth22-glow),var(--color-tth22-bg)_75%)] px-5 py-14 font-tth22-sans text-tth22-ink" aria-label="Perspective tilt text demo">
  <div class="flex flex-col items-center gap-[clamp(18px,3.4vw,28px)] text-center">
    <p class="text-[12.5px] font-extrabold uppercase tracking-[0.24em] text-tth22-mut">Pivot &mdash; the design systems summit</p>
    <a id="tth22-top" href="#tth22-top" aria-label="PIVOT '26 — get tickets" class="group/tilt relative block rounded-2xl px-[clamp(20px,4vw,44px)] py-[clamp(16px,3vw,30px)] no-underline perspective-[850px] focus-visible:outline-[2.5px] focus-visible:outline-offset-4 focus-visible:outline-tth22-acc">
      <i aria-hidden="true" class="peer/tl absolute left-0 top-0 z-10 size-1/2"></i><i aria-hidden="true" class="peer/tr absolute right-0 top-0 z-10 size-1/2"></i><i aria-hidden="true" class="peer/bl absolute bottom-0 left-0 z-10 size-1/2"></i><i aria-hidden="true" class="peer/br absolute bottom-0 right-0 z-10 size-1/2"></i>
      <span aria-hidden="true" class="block text-[clamp(58px,13.5vw,140px)] font-black leading-none tracking-[-0.04em] [text-shadow:0_.06em_.09em_oklch(0.2_0.02_270/0.22)] transition-[transform,text-shadow] duration-500 ease-[cubic-bezier(.2,.8,.25,1)] peer-hover/tl:rotate-x-[11deg] peer-hover/tl:-rotate-y-[13deg] peer-hover/tl:[text-shadow:.07em_.11em_.13em_oklch(0.2_0.02_270/0.42)] peer-hover/tr:rotate-x-[11deg] peer-hover/tr:rotate-y-[13deg] peer-hover/tr:[text-shadow:-.07em_.11em_.13em_oklch(0.2_0.02_270/0.42)] peer-hover/bl:-rotate-x-[11deg] peer-hover/bl:-rotate-y-[13deg] peer-hover/bl:[text-shadow:.07em_-.07em_.13em_oklch(0.2_0.02_270/0.4)] peer-hover/br:-rotate-x-[11deg] peer-hover/br:rotate-y-[13deg] peer-hover/br:[text-shadow:-.07em_-.07em_.13em_oklch(0.2_0.02_270/0.4)] group-focus-visible/tilt:animate-tth22-sway motion-reduce:transition-none motion-reduce:animate-none!">PIVOT<span class="text-tth22-acc">&rsquo;26</span></span>
    </a>
    <p class="max-w-[52ch] text-[15px] leading-[1.7] text-tth22-mut">Approach the wordmark from any corner &mdash; it leans toward you. Four invisible hover quadrants, four poses, one transition blending them. No script.</p>
    <p class="text-[12.5px] text-tth22-mut">The shadow always slides opposite the tilt &mdash; fixed lamp, turning object. <kbd class="rounded-[5px] border border-b-2 border-tth22-line bg-white px-1.5 py-0.5 font-tth22-mono text-[11px]">Tab</kbd> to it for the keyboard sway.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tth22-bg: #eceef3;
  --color-tth22-bg: oklch(0.94 0.006 260);
  --color-tth22-glow: #f6f7fa;
  --color-tth22-glow: oklch(0.975 0.004 260);
  --color-tth22-ink: #1a1c2b;
  --color-tth22-ink: oklch(0.22 0.02 270);
  --color-tth22-mut: #5a5d6c;
  --color-tth22-mut: oklch(0.47 0.015 265);
  --color-tth22-acc: #3c55d8;
  --color-tth22-acc: oklch(0.52 0.2 265);
  --color-tth22-line: #d4d6de;
  --color-tth22-line: oklch(0.86 0.008 260);
  --font-tth22-sans: 'Schibsted Grotesk', system-ui, sans-serif;
  --font-tth22-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tth22-sway: tth22-sway 3.2s ease-in-out infinite;

  @keyframes tth22-sway {
    0%,
        100% {
      transform: rotateX(9deg) rotateY(-11deg);
    }

    50% {
      transform: rotateX(-9deg) rotateY(11deg);
    }
  }
}

.tth-22 {
  width: 100%;
  min-height: 100svh;
}
```
