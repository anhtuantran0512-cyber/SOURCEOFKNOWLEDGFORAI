---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-floating-label-inputs/tailwind-filled-underline-floating-label-input/"
title: "Tailwind Filled & Underline Floating Label Input"
section: "components"
category: "tailwind-css-floating-label-inputs"
category_name: "Tailwind CSS Floating Label Inputs"
description: "The calm, editorial filled field: a tinted box with only a bottom border, where focus sweeps an accent underline from the centre outward (after:scale-x-0…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Filled & Underline Floating Label Input
Source: https://codefronts.com/components/tailwind-css-floating-label-inputs/tailwind-filled-underline-floating-label-input/

The calm, editorial filled field: a tinted box with only a bottom border, where focus sweeps an accent underline from the centre outward (after:scale-x-0 focus-within:after:scale-x-100) and the label performs a blink-swap — fading out mid-field and re-materialising in its floated spot via animate-tfl10-swap.
## HTML
```html
<section class="tfl-10 w-full min-h-svh grid place-items-center bg-tfl10-bg px-5 py-12 font-tfl10-sans" aria-label="Filled underline floating label demo">
  <form class="flex w-full max-w-[380px] flex-col gap-[22px] rounded-[18px] bg-white p-8 shadow-[0_20px_50px_-30px_oklch(0.3_0.04_210/0.35)] ring-1 ring-tfl10-ink/5" novalidate>
    <div class="grid gap-1">
      <h3 class="font-tfl10-serif text-[30px]/tight text-tfl10-ink">Stay in the <em class="text-tfl10-acc">loop</em></h3>
      <p class="text-sm text-tfl10-mut">One thoughtful email a month. No noise.</p>
    </div>
    <div class="relative after:pointer-events-none after:absolute after:inset-x-0 after:bottom-0 after:h-0.5 after:origin-center after:scale-x-0 after:bg-tfl10-acc after:transition-[scale] after:duration-[250ms] after:ease-out after:content-[''] focus-within:after:scale-x-100 motion-reduce:after:transition-none">
      <input class="peer h-14 w-full rounded-t-[10px] border-b-2 border-tfl10-line bg-tfl10-acc/7 px-3.5 pt-[22px] pb-1.5 text-base text-tfl10-ink outline-hidden transition-[background-color] duration-200 hover:bg-tfl10-acc/11 focus:bg-tfl10-acc/10" type="text" id="tfl-10-first" name="given-name" placeholder=" " autocomplete="given-name">
      <label class="pointer-events-none absolute left-3.5 top-1/2 origin-left -translate-y-1/2 text-base text-tfl10-mut transition-[translate,scale,color] duration-[180ms] peer-focus:translate-y-[calc(-50%_-_13px)] peer-focus:scale-72 peer-focus:animate-tfl10-swap peer-focus:text-tfl10-acc peer-[:not(:placeholder-shown)]:translate-y-[calc(-50%_-_13px)] peer-[:not(:placeholder-shown)]:scale-72 peer-[:not(:placeholder-shown)]:animate-tfl10-swap motion-reduce:animate-none! motion-reduce:transition-none" for="tfl-10-first">First name</label>
    </div>
    <div class="relative after:pointer-events-none after:absolute after:inset-x-0 after:bottom-0 after:h-0.5 after:origin-center after:scale-x-0 after:bg-tfl10-acc after:transition-[scale] after:duration-[250ms] after:ease-out after:content-[''] focus-within:after:scale-x-100 motion-reduce:after:transition-none">
      <input class="peer h-14 w-full rounded-t-[10px] border-b-2 border-tfl10-line bg-tfl10-acc/7 px-3.5 pt-[22px] pb-1.5 text-base text-tfl10-ink outline-hidden transition-[background-color] duration-200 hover:bg-tfl10-acc/11 focus:bg-tfl10-acc/10" type="email" id="tfl-10-mail" name="email" placeholder=" " autocomplete="email">
      <label class="pointer-events-none absolute left-3.5 top-1/2 origin-left -translate-y-1/2 text-base text-tfl10-mut transition-[translate,scale,color] duration-[180ms] peer-focus:translate-y-[calc(-50%_-_13px)] peer-focus:scale-72 peer-focus:animate-tfl10-swap peer-focus:text-tfl10-acc peer-[:not(:placeholder-shown)]:translate-y-[calc(-50%_-_13px)] peer-[:not(:placeholder-shown)]:scale-72 peer-[:not(:placeholder-shown)]:animate-tfl10-swap motion-reduce:animate-none! motion-reduce:transition-none" for="tfl-10-mail">Email address</label>
    </div>
    <button class="min-h-12 cursor-pointer rounded-xl bg-tfl10-ink text-[15px] font-semibold text-white transition-[filter,scale] duration-150 hover:brightness-150 active:scale-98 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tfl10-acc/60" type="button">Subscribe</button>
  </form>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfl10-bg: #f3f6f6;
  --color-tfl10-bg: oklch(0.97 0.004 200);
  --color-tfl10-ink: #16232a;
  --color-tfl10-ink: oklch(0.24 0.02 225);
  --color-tfl10-mut: #56696f;
  --color-tfl10-mut: oklch(0.49 0.025 215);
  --color-tfl10-line: #a9b8bf;
  --color-tfl10-line: oklch(0.77 0.02 220);
  --color-tfl10-acc: #0f7f98;
  --color-tfl10-acc: oklch(0.53 0.1 215);
  --font-tfl10-sans: 'Instrument Sans', system-ui, sans-serif;
  --font-tfl10-serif: 'Instrument Serif', Georgia, serif;
  --animate-tfl10-swap: tfl10-swap 0.32s both;

  @keyframes tfl10-swap {
    0% {
      opacity: 1;
      translate: 0 -50%;
      scale: 1;
    }

    45% {
      opacity: 0;
      translate: 0 calc(-50% + 5px);
      scale: 1;
    }

    55% {
      opacity: 0;
      translate: 0 calc(-50% - 18px);
      scale: 0.72;
    }

    100% {
      opacity: 1;
      translate: 0 calc(-50% - 13px);
      scale: 0.72;
    }
  }
}

.tfl-10 {
  width: 100%;
  min-height: 100svh;
}
```
