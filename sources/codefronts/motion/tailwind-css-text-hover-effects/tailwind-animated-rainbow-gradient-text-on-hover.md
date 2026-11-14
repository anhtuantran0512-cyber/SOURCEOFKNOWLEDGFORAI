---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-animated-rainbow-gradient-text-on-hover/"
title: "Tailwind Animated Rainbow Gradient Text on Hover"
section: "motion"
category: "tailwind-css-text-hover-effects"
category_name: "Tailwind CSS Text Hover Effects"
description: "A Pride headline that turns into flowing rainbow on hover — generated from just two oklch stops with in oklch longer hue, so every hue is equally bright (no…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Animated Rainbow Gradient Text on Hover
Source: https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-animated-rainbow-gradient-text-on-hover/

A Pride headline that turns into flowing rainbow on hover — generated from just two oklch stops with in oklch longer hue, so every hue is equally bright (no muddy sRGB greens). The gradient is 300% wide and travels exactly −300% per loop, so the flow is seamless. The CTA uses the same trick, always-on while hovered.
## HTML
```html
<section class="tth-21 w-full min-h-svh grid place-items-center bg-tth21-bg px-5 py-14 font-tth21-sans text-tth21-ink" aria-label="Rainbow gradient flow demo">
  <div class="flex flex-col items-center gap-[clamp(16px,3vw,26px)] text-center">
    <p class="text-[12.5px] font-extrabold uppercase tracking-[0.24em] text-tth21-mut">Brighton Pride &mdash; March 7, 2026</p>
    <h2 class="leading-none"><a id="tth21-top" href="#tth21-top" class="inline-block rounded-lg px-[0.08em] py-[0.06em] text-[clamp(46px,10.5vw,108px)] font-black leading-[1.02] tracking-[-0.03em] no-underline bg-[linear-gradient(90deg_in_oklch_longer_hue,oklch(0.68_0.19_0),oklch(0.68_0.19_350))] bg-[length:300%_100%] bg-[position:0%_0] bg-clip-text text-tth21-ink transition-colors duration-450 hover:text-transparent hover:animate-tth21-flow focus-visible:text-transparent focus-visible:animate-tth21-flow focus-visible:outline-3 focus-visible:outline-offset-8 focus-visible:outline-[oklch(0.6_0.19_300)] pointer-coarse:text-transparent motion-reduce:animate-none!">EVERY COLOUR<br>OUT LOUD</a></h2>
    <p class="max-w-[52ch] text-[15px] leading-[1.7] text-tth21-mut">Two oklch stops and <code class="rounded bg-tth21-chip px-1.5 py-px font-tth21-mono text-[0.9em]">longer hue</code> generate the whole spectrum &mdash; evenly bright, endlessly looping, only when asked.</p>
    <div class="mt-1.5 flex flex-wrap justify-center gap-3.5">
      <a href="#tth21-top" class="grid min-h-14 place-items-center rounded-full px-8 text-base font-extrabold text-white no-underline bg-[linear-gradient(90deg_in_oklch_longer_hue,oklch(0.52_0.19_0),oklch(0.52_0.19_350))] bg-[length:300%_100%] shadow-[0_10px_30px_oklch(0.5_0.15_320/0.25)] transition-[box-shadow,translate] duration-300 hover:-translate-y-0.5 hover:animate-tth21-flow-fast hover:shadow-[0_16px_40px_oklch(0.5_0.15_320/0.35)] focus-visible:animate-tth21-flow-fast focus-visible:outline-3 focus-visible:outline-offset-[3px] focus-visible:outline-tth21-ink motion-reduce:animate-none!">March with us</a>
      <a href="#tth21-top" class="grid min-h-14 place-items-center rounded-full border-[1.5px] border-tth21-ink/30 px-7 text-base font-bold no-underline transition-[border-color,background-color] duration-300 hover:border-tth21-ink hover:bg-tth21-ink/4 focus-visible:border-tth21-ink focus-visible:outline-3 focus-visible:outline-offset-[3px] focus-visible:outline-[oklch(0.6_0.19_300)]">Route map</a>
    </div>
    <div aria-hidden="true" class="h-1.5 w-40 rounded-full bg-[linear-gradient(90deg_in_oklch_longer_hue,oklch(0.68_0.19_0),oklch(0.68_0.19_350))]"></div>
    <p class="max-w-[54ch] text-[12.5px] leading-[1.7] text-tth21-mut">Hover the headline or the button. The loop is seamless because travel (&minus;300%) equals the canvas width (300%).</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tth21-bg: #fbfaf7;
  --color-tth21-bg: oklch(0.98 0.004 90);
  --color-tth21-chip: #ebeaef;
  --color-tth21-chip: oklch(0.93 0.005 280);
  --color-tth21-ink: #15131c;
  --color-tth21-ink: oklch(0.2 0.01 280);
  --color-tth21-mut: #5d5a68;
  --color-tth21-mut: oklch(0.47 0.015 280);
  --font-tth21-sans: 'Gabarito', system-ui, sans-serif;
  --font-tth21-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tth21-flow: tth21-flow 3.5s linear infinite;
  --animate-tth21-flow-fast: tth21-flow 2.6s linear infinite;

  @keyframes tth21-flow {
    to {
      background-position: -300% 0;
    }
  }
}

.tth-21 {
  width: 100%;
  min-height: 100svh;
}
```
