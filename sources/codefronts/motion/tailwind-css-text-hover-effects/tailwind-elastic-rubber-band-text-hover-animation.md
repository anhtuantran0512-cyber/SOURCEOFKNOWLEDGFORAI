---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-elastic-rubber-band-text-hover-animation/"
title: "Tailwind Elastic Rubber Band Text Hover Animation"
section: "motion"
category: "tailwind-css-text-hover-effects"
category_name: "Tailwind CSS Text Hover Effects"
description: "A kids' coding-camp wordmark where every letter squashes and stretches like rubber, staggered 40ms and recoloured per letter."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Elastic Rubber Band Text Hover Animation
Source: https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-elastic-rubber-band-text-hover-animation/

A kids' coding-camp wordmark where every letter squashes and stretches like rubber, staggered 40ms and recoloured per letter. The whole animation is group-hover/word:*:animate-tth19-rubber on the parent with *:[animation-delay:calc(var(--i)*40ms)]; the CTA squashes on hover and presses with active:.
## HTML
```html
<section class="tth-19 w-full min-h-svh grid place-items-center bg-tth19-bg bg-[radial-gradient(85%_70%_at_50%_18%,var(--color-tth19-glow),var(--color-tth19-bg)_70%)] px-5 py-14 font-tth19-sans text-tth19-ink" aria-label="Elastic rubber band text demo">
  <div class="flex flex-col items-center gap-[clamp(14px,2.8vw,24px)] text-center">
    <p class="text-[13px] font-extrabold uppercase tracking-[0.2em] text-tth19-mut">After-school coding camp &middot; ages 7&ndash;11</p>
    <a id="tth19-top" href="#tth19-top" aria-label="WIGGLE CLUB" class="group/word flex flex-wrap justify-center gap-x-[0.35em] gap-y-[0.05em] rounded-xl px-[0.1em] py-[0.15em] font-tth19-display text-[clamp(54px,12.5vw,128px)] font-bold leading-none tracking-[-0.01em] no-underline focus-visible:outline-3 focus-visible:outline-offset-8 focus-visible:outline-tth19-acc">
      <span aria-hidden="true" class="*:inline-block *:not-italic *:origin-[50%_78%] *:transition-colors *:duration-300 *:[animation-delay:calc(var(--i)*40ms)] group-hover/word:*:animate-tth19-rubber group-hover/word:*:text-(--tth19-c) group-focus-visible/word:*:animate-tth19-rubber group-focus-visible/word:*:text-(--tth19-c) motion-reduce:*:animate-none!"><i style="--i:0;--tth19-c:oklch(0.62 0.21 25)">W</i><i style="--i:1;--tth19-c:oklch(0.66 0.18 60)">I</i><i style="--i:2;--tth19-c:oklch(0.6 0.17 145)">G</i><i style="--i:3;--tth19-c:oklch(0.58 0.15 230)">G</i><i style="--i:4;--tth19-c:oklch(0.55 0.2 290)">L</i><i style="--i:5;--tth19-c:oklch(0.6 0.22 345)">E</i></span>
      <span aria-hidden="true" class="*:inline-block *:not-italic *:origin-[50%_78%] *:transition-colors *:duration-300 *:[animation-delay:calc(var(--i)*40ms)] group-hover/word:*:animate-tth19-rubber group-hover/word:*:text-(--tth19-c) group-focus-visible/word:*:animate-tth19-rubber group-focus-visible/word:*:text-(--tth19-c) motion-reduce:*:animate-none!"><i style="--i:6;--tth19-c:oklch(0.66 0.18 60)">C</i><i style="--i:7;--tth19-c:oklch(0.6 0.17 145)">L</i><i style="--i:8;--tth19-c:oklch(0.58 0.15 230)">U</i><i style="--i:9;--tth19-c:oklch(0.55 0.2 290)">B</i></span>
    </a>
    <p class="max-w-[40ch] text-[15.5px] font-semibold leading-[1.6] text-tth19-mut">Blocks in term one, robots by term three. Snacks throughout.</p>
    <a href="#tth19-top" class="group/btn mt-1.5 flex min-h-[58px] items-center justify-center gap-2 rounded-full bg-tth19-acc px-[34px] font-tth19-display text-[17px] font-bold tracking-[0.01em] text-white no-underline shadow-[0_6px_0_0_var(--color-tth19-acc-deep)] transition-[scale,box-shadow,translate] duration-450 ease-[cubic-bezier(.28,2.2,.4,1)] hover:scale-x-108 hover:scale-y-92 focus-visible:scale-x-108 focus-visible:scale-y-92 focus-visible:outline-3 focus-visible:outline-offset-4 focus-visible:outline-tth19-ink active:translate-y-1 active:scale-x-94 active:scale-y-104 active:shadow-[0_2px_0_0_var(--color-tth19-acc-deep)] active:duration-80 motion-reduce:transition-none">Save a spot<span aria-hidden="true" class="transition-transform duration-300 group-hover/btn:translate-x-1">&rarr;</span></a>
    <p class="max-w-[56ch] text-[12.5px] leading-[1.7] text-tth19-mut">Hover the name (squash &amp; stretch, staggered 40ms) &mdash; then press the button and feel it squash. Origin sits at the baseline so letters bounce off the floor.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tth19-bg: #faf6e9;
  --color-tth19-bg: oklch(0.965 0.02 95);
  --color-tth19-glow: #fdfbf4;
  --color-tth19-glow: oklch(0.985 0.012 95);
  --color-tth19-ink: #352a57;
  --color-tth19-ink: oklch(0.28 0.05 280);
  --color-tth19-mut: #5a5373;
  --color-tth19-mut: oklch(0.45 0.04 285);
  --color-tth19-acc: #e3392f;
  --color-tth19-acc: oklch(0.6 0.21 25);
  --color-tth19-acc-deep: #8f2019;
  --color-tth19-acc-deep: oklch(0.42 0.15 25);
  --font-tth19-display: 'Fredoka', ui-rounded, system-ui, sans-serif;
  --font-tth19-sans: 'Nunito', system-ui, sans-serif;
  --animate-tth19-rubber: tth19-rubber 0.8s cubic-bezier(0.3, 0.6, 0.4, 1) both;

  @keyframes tth19-rubber {
    0% {
      transform: scale(1, 1);
    }

    30% {
      transform: scale(1.28, 0.72);
    }

    42% {
      transform: scale(0.78, 1.24);
    }

    56% {
      transform: scale(1.14, 0.88);
    }

    70% {
      transform: scale(0.94, 1.06);
    }

    84% {
      transform: scale(1.03, 0.98);
    }

    100% {
      transform: scale(1, 1);
    }
  }
}

.tth-19 {
  width: 100%;
  min-height: 100svh;
}
```
