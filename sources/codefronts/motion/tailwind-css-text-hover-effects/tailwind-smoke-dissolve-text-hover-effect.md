---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-smoke-dissolve-text-hover-effect/"
title: "Tailwind Smoke Dissolve Text Hover Effect"
section: "motion"
category: "tailwind-css-text-hover-effects"
category_name: "Tailwind CSS Text Hover Effects"
description: "A film title that dissolves into smoke: each letter drifts up, sideways and rotated by its own --tth23-dx/--tth23-dr, blurring to nothing in a 35ms stagger."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Smoke Dissolve Text Hover Effect
Source: https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-smoke-dissolve-text-hover-effect/

A film title that dissolves into smoke: each letter drifts up, sideways and rotated by its own --tth23-dx/--tth23-dr, blurring to nothing in a 35ms stagger. Because it's transitions, pulling away mid-dissolve re-condenses the word along the same path. All from the parent: group-hover/title:*:-translate-y-[1.25em] *:blur-[.14em] *:opacity-0.
## HTML
```html
<section class="tth-23 w-full min-h-svh grid place-items-center bg-tth23-bg bg-[radial-gradient(100%_90%_at_50%_100%,oklch(0.24_0.05_50/0.6),transparent_55%),radial-gradient(90%_70%_at_50%_20%,var(--color-tth23-glow),var(--color-tth23-bg)_75%)] px-5 py-14 font-tth23-serif text-tth23-ink" aria-label="Smoke dissolve text demo">
  <div class="flex flex-col items-center gap-[clamp(16px,3vw,26px)] text-center">
    <p class="font-tth23-sans text-xs font-semibold uppercase tracking-[0.34em] text-tth23-mut">A film by Ines Marlowe</p>
    <h2><a id="tth23-top" href="#tth23-top" aria-label="AFTERGLOW — watch the trailer" class="group/title block rounded-[14px] px-[clamp(16px,3vw,32px)] py-[clamp(24px,5vw,48px)] tracking-[0.16em] no-underline focus-visible:outline-[1.5px] focus-visible:outline-offset-4 focus-visible:outline-tth23-ink">
      <span aria-hidden="true" class="*:inline-block *:text-[clamp(44px,10vw,104px)] *:font-medium *:not-italic *:leading-none *:transition-[translate,rotate,opacity,filter,color] *:duration-1000 *:ease-[cubic-bezier(.3,.6,.2,1)] *:delay-[calc(var(--i)*35ms)] group-hover/title:*:translate-x-(--tth23-dx) group-hover/title:*:-translate-y-[1.25em] group-hover/title:*:rotate-(--tth23-dr) group-hover/title:*:opacity-0 group-hover/title:*:blur-[.14em] group-hover/title:*:text-white group-focus-visible/title:*:-translate-y-[1.25em] group-focus-visible/title:*:opacity-0 group-focus-visible/title:*:blur-[.14em] motion-reduce:*:transition-opacity motion-reduce:*:delay-0 motion-reduce:group-hover/title:*:translate-x-0 motion-reduce:group-hover/title:*:translate-y-0 motion-reduce:group-hover/title:*:rotate-0 motion-reduce:group-hover/title:*:blur-none motion-reduce:group-hover/title:*:opacity-45"><i style="--i:0;--tth23-dx:-.1em;--tth23-dr:-8deg">A</i><i style="--i:1;--tth23-dx:.06em;--tth23-dr:5deg">F</i><i style="--i:2;--tth23-dx:-.04em;--tth23-dr:-4deg">T</i><i style="--i:3;--tth23-dx:.14em;--tth23-dr:9deg">E</i><i style="--i:4;--tth23-dx:-.12em;--tth23-dr:-6deg">R</i><i style="--i:5;--tth23-dx:.05em;--tth23-dr:7deg">G</i><i style="--i:6;--tth23-dx:-.07em;--tth23-dr:-9deg">L</i><i style="--i:7;--tth23-dx:.11em;--tth23-dr:4deg">O</i><i style="--i:8;--tth23-dx:-.05em;--tth23-dr:-5deg">W</i></span>
    </a></h2>
    <p class="text-lg italic tracking-[0.02em] text-tth23-mut">In cinemas October &mdash; the story of everything we let cool.</p>
    <a href="#tth23-top" class="inline-flex min-h-11 items-center gap-2.5 rounded-full border border-tth23-ink/25 px-5 font-tth23-sans text-[13px] font-semibold uppercase tracking-[0.14em] no-underline transition-[border-color,background-color] duration-300 hover:border-tth23-ink hover:bg-tth23-ink/5 focus-visible:outline-[1.5px] focus-visible:outline-offset-4 focus-visible:outline-tth23-ink"><span aria-hidden="true" class="grid size-5 place-items-center rounded-full bg-tth23-ink text-[9px] text-tth23-bg">&#9654;</span>Watch the trailer</a>
    <p class="max-w-[56ch] font-tth23-sans text-[12.5px] leading-[1.7] text-tth23-mut">Rest the cursor on the title and hold; pull away mid-dissolve and it re-condenses along the same path. Transitions, never keyframes &mdash; that's the whole trick.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tth23-bg: #0d0e14;
  --color-tth23-bg: oklch(0.15 0.008 270);
  --color-tth23-glow: #15161d;
  --color-tth23-glow: oklch(0.19 0.01 275);
  --color-tth23-ink: #e9e3d6;
  --color-tth23-ink: oklch(0.91 0.015 80);
  --color-tth23-mut: #9b9aa7;
  --color-tth23-mut: oklch(0.7 0.015 275);
  --font-tth23-serif: 'Cormorant Garamond', Georgia, serif;
  --font-tth23-sans: 'Manrope', system-ui, sans-serif;
}

.tth-23 {
  width: 100%;
  min-height: 100svh;
}
```
