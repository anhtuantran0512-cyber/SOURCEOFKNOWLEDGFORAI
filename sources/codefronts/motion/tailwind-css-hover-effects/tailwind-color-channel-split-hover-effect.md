---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-color-channel-split-hover-effect/"
title: "Tailwind Color Channel Split Hover Effect"
section: "motion"
category: "tailwind-css-hover-effects"
category_name: "Tailwind CSS Hover Effects"
description: "Four colour-separation effects — an RGB text-shadow split, chromatic aberration, a hue-rotate grade and additive screen-blend channels."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Color Channel Split Hover Effect
Source: https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-color-channel-split-hover-effect/

Four colour-separation effects — an RGB text-shadow split, chromatic aberration, a hue-rotate grade and additive screen-blend channels. Offsets are hard-coded shadow lengths; the port's contribution is that the resting and separated states sit together.
## HTML
```html
<section class="thv-20 w-full min-h-svh grid place-items-center bg-thv20-bg font-thv20-sans px-6 py-14">
  <div class="w-[min(760px,100%)] grid grid-cols-[repeat(auto-fit,minmax(260px,1fr))] gap-10">
    <figure class="group flex flex-col items-center gap-5 m-0">
      <div tabindex="0" class="relative grid place-items-center w-full aspect-[4/3] overflow-hidden rounded-xl cursor-pointer bg-[radial-gradient(circle_at_30%_30%,#1e3a8a_0%,transparent_50%),radial-gradient(circle_at_70%_70%,#4c1d95_0%,transparent_50%),linear-gradient(135deg,#0a0a1a,#1a0a2e)] focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv20-red">
        <span class="relative z-10 text-xl font-black tracking-[0.15em] text-white transition-[text-shadow,letter-spacing] duration-450 ease-[cubic-bezier(.4,0,.2,1)] group-hover:tracking-[0.22em] group-hover:[text-shadow:-6px_0_0_var(--color-thv20-red),6px_0_0_var(--color-thv20-blue),0_4px_0_var(--color-thv20-green)] group-focus-visible:tracking-[0.22em] group-focus-visible:[text-shadow:-6px_0_0_var(--color-thv20-red),6px_0_0_var(--color-thv20-blue)] motion-reduce:transition-none">SIGNAL</span>
      </div>
      <figcaption class="text-[11px] tracking-[0.12em] uppercase text-thv20-dim">RGB channel split</figcaption>
    </figure>
    <figure class="group flex flex-col items-center gap-5 m-0">
      <div tabindex="0" class="relative grid place-items-center w-full aspect-[4/3] overflow-hidden rounded-xl cursor-pointer bg-[radial-gradient(circle_at_50%_50%,#1a1a2e_0%,#050505_100%)] focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv20-blue">
        <span class="relative z-10 text-[clamp(1.4rem,4vw,1.8rem)] font-black tracking-[0.12em] text-white transition-[text-shadow,letter-spacing] duration-400 ease-[cubic-bezier(.4,0,.2,1)] group-hover:tracking-[0.18em] group-hover:[text-shadow:5px_0_0_var(--color-thv20-red),-5px_0_0_var(--color-thv20-blue),0_4px_0_rgba(0,255,136,.6)] group-focus-visible:tracking-[0.18em] group-focus-visible:[text-shadow:5px_0_0_var(--color-thv20-red),-5px_0_0_var(--color-thv20-blue)] motion-reduce:transition-none">CHROMATIC</span>
      </div>
      <figcaption class="text-[11px] tracking-[0.12em] uppercase text-thv20-dim">text-shadow aberration</figcaption>
    </figure>
    <figure class="group flex flex-col items-center gap-5 m-0">
      <div tabindex="0" class="relative grid place-items-center w-full aspect-[4/3] overflow-hidden rounded-xl cursor-pointer transition-[filter] duration-500 ease-[cubic-bezier(.4,0,.2,1)] bg-[radial-gradient(circle_at_25%_30%,#fbbf24_0%,transparent_35%),radial-gradient(circle_at_75%_70%,#dc2626_0%,transparent_40%),linear-gradient(135deg,#7c3aed,#ec4899,#f59e0b)] group-hover:[filter:hue-rotate(180deg)_saturate(1.6)] group-focus-visible:[filter:hue-rotate(180deg)_saturate(1.6)] focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-white motion-reduce:transition-none">
        <span class="relative z-10 text-xl font-black tracking-[0.15em] text-white [text-shadow:0_2px_8px_rgba(0,0,0,.8)]">DUOTONE</span>
      </div>
      <figcaption class="text-[11px] tracking-[0.12em] uppercase text-thv20-dim">colour grade shift</figcaption>
    </figure>
    <figure class="group flex flex-col items-center gap-5 m-0">
      <div tabindex="0" class="relative grid place-items-center w-full aspect-[4/3] overflow-hidden rounded-xl cursor-pointer bg-[linear-gradient(135deg,#1a1a2e,#16213e,#0f3460,#533483)] focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv20-red">
        <span aria-hidden="true" class="absolute top-[10%] left-[10%] w-[60%] h-[60%] rounded-full bg-thv20-red mix-blend-screen opacity-0 transition-[opacity,transform] duration-500 ease-[cubic-bezier(.4,0,.2,1)] group-hover:opacity-70 group-hover:-translate-x-2.5 group-focus-visible:opacity-70 motion-reduce:transition-opacity"></span>
        <span aria-hidden="true" class="absolute top-[10%] right-[10%] w-[60%] h-[60%] rounded-full bg-thv20-blue mix-blend-screen opacity-0 transition-[opacity,transform] duration-500 ease-[cubic-bezier(.4,0,.2,1)] group-hover:opacity-70 group-hover:translate-x-2.5 group-focus-visible:opacity-70 motion-reduce:transition-opacity"></span>
        <span class="relative z-10 text-xl font-black tracking-[0.15em] text-white">COMPOSITE</span>
      </div>
      <figcaption class="text-[11px] tracking-[0.12em] uppercase text-thv20-dim">screen blend channels</figcaption>
    </figure>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thv20-bg: #050505;
  --color-thv20-bg: oklch(0.09 0 0);
  --color-thv20-dim: #8b8b93;
  --color-thv20-dim: oklch(0.65 0.01 285);
  --color-thv20-red: #ff0040;
  --color-thv20-red: oklch(0.62 0.28 15);
  --color-thv20-green: #00ff88;
  --color-thv20-green: oklch(0.87 0.26 155);
  --color-thv20-blue: #0040ff;
  --color-thv20-blue: oklch(0.47 0.3 265);
  --font-thv20-sans: 'Space Grotesk', system-ui, sans-serif;
}

.thv-20 {
  width: 100%;
  min-height: 100svh;
}

.thv-20 ::selection {
  background: var(--color-thv20-red);
  color: #fff;
}
```
