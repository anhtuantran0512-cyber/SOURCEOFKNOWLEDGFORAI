---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-typewriter-retype-terminal-button-effect/"
title: "Tailwind Typewriter Retype Terminal Button Effect"
section: "motion"
category: "tailwind-css-button-hover-effects"
category_name: "Tailwind CSS Button Hover Effects"
description: "A retro-terminal CTA where, on hover, the label retypes character by character with a blinking caret &mdash; nostalgic and techy for dev tools and docs."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Typewriter Retype Terminal Button Effect
Source: https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-typewriter-retype-terminal-button-effect/

A retro-terminal CTA where, on hover, the label retypes character by character with a blinking caret &mdash; nostalgic and techy for dev tools and docs. The ch unit and the steps() count are the whole effect, and both are now visible in the markup where the character count lives.
## HTML
```html
<div class="tbh-26-group w-full min-h-svh flex flex-wrap">
<section class="tbh-26a flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh26-mono bg-tbh26a-stage" aria-label="Typewriter retype button">
  <button type="button" class="group/btn cursor-pointer rounded-md border border-tbh26a-term px-7 py-4 text-base font-bold text-tbh26a-term bg-tbh26a-panel shadow-[0_0_20px_-8px_var(--color-tbh26a-term)] focus-visible:outline-3 focus-visible:outline-tbh26a-term focus-visible:outline-offset-4">
    <span class="inline-block overflow-hidden whitespace-nowrap align-bottom w-[12ch] border-r-2 border-tbh26a-term animate-tbh26a-blink group-hover/btn:[animation:var(--animate-tbh26a-type),var(--animate-tbh26a-blink)] group-focus-visible/btn:[animation:var(--animate-tbh26a-type),var(--animate-tbh26a-blink)] motion-reduce:animate-none motion-reduce:w-[12ch]">$ deploy_now</span>
  </button>
</section>
<section class="tbh-26b flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh26-mono bg-tbh26b-stage" aria-label="Prompt caret button">
  <button type="button" class="group/btn inline-flex items-center gap-0.5 cursor-pointer rounded-md border border-tbh26b-term px-[30px] py-4 text-base font-bold text-tbh26b-term bg-tbh26b-panel focus-visible:outline-3 focus-visible:outline-tbh26b-term focus-visible:outline-offset-4">
    <span class="overflow-hidden whitespace-nowrap max-w-[9ch] transition-[max-width] duration-700 ease-[steps(9)] group-hover/btn:max-w-0 group-focus-visible/btn:max-w-0 motion-reduce:transition-none motion-reduce:max-w-[9ch]">run build</span>
    <span aria-hidden="true" class="w-[9px] h-[1.1em] bg-tbh26b-term animate-tbh26b-blink group-hover/btn:animate-tbh26b-blinkfast group-focus-visible/btn:animate-tbh26b-blinkfast motion-reduce:animate-none"></span>
  </button>
</section>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbh26a-term: #57e08a;
  --color-tbh26a-term: oklch(0.82 0.19 145);
  --color-tbh26a-stage: #06120b;
  --color-tbh26a-stage: oklch(0.13 0.02 150);
  --color-tbh26a-panel: #0a1c12;
  --color-tbh26a-panel: oklch(0.18 0.03 150);
  --color-tbh26b-term: #e0c04a;
  --color-tbh26b-term: oklch(0.8 0.16 90);
  --color-tbh26b-stage: #12100a;
  --color-tbh26b-stage: oklch(0.15 0.02 85);
  --color-tbh26b-panel: #1c180c;
  --color-tbh26b-panel: oklch(0.2 0.03 85);
  --font-tbh26-mono: 'JetBrains Mono', ui-monospace, Menlo, monospace;
  --animate-tbh26a-type: tbh26a-type 1s steps(12) forwards;
  --animate-tbh26a-blink: tbh26a-blink 1s steps(1) infinite;
  --animate-tbh26b-blink: tbh26b-blink 1s steps(1) infinite;
  --animate-tbh26b-blinkfast: tbh26b-blink 0.4s steps(1) infinite;
}
/* Stays CSS: the typing keyframe animates width in ch units, and the caret keyframes flip a
   border colour and an opacity — none of which has a keyframe-able utility form. */

@keyframes tbh26a-type {
  from {
    width: 0;
  }

  to {
    width: 12ch;
  }
}

@keyframes tbh26a-blink {
  50% {
    border-color: transparent;
  }
}

@keyframes tbh26b-blink {
  50% {
    opacity: 0;
  }
}

.tbh-26-group {
  width: 100%;
  min-height: 100svh;
}

.tbh-26a,
.tbh-26b {
  min-height: 100svh;
}
```
