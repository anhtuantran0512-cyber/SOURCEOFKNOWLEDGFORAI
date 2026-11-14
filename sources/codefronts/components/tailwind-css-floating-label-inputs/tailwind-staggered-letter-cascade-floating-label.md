---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-floating-label-inputs/tailwind-staggered-letter-cascade-floating-label/"
title: "Tailwind Staggered Letter-Cascade Floating Label"
section: "components"
category: "tailwind-css-floating-label-inputs"
category_name: "Tailwind CSS Floating Label Inputs"
description: "Each letter of the label rises on its own, a left-to-right wave: one *: class list styles every letter span, *:[transition-delay:calc(var(--i)*30ms)]…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Staggered Letter-Cascade Floating Label
Source: https://codefronts.com/components/tailwind-css-floating-label-inputs/tailwind-staggered-letter-cascade-floating-label/

Each letter of the label rises on its own, a left-to-right wave: one *: class list styles every letter span, *:[transition-delay:calc(var(--i)*30ms)] staggers them, and group-focus-within: + group-has-[input:not(:placeholder-shown)]: fire the float. The real label text sits in an sr-only span so screen readers hear a word, not letters.
## HTML
```html
<section class="tfl-01 w-full min-h-svh grid place-items-center bg-tfl01-bg bg-[radial-gradient(90%_70%_at_50%_0%,var(--color-tfl01-glow),transparent_70%)] px-5 py-12 font-tfl01-sans" aria-label="Staggered letter cascade floating label demo">
  <form class="flex w-full max-w-[380px] flex-col gap-5 rounded-3xl bg-white p-8 shadow-[0_24px_60px_-32px_oklch(0.35_0.12_320/0.45)] ring-1 ring-tfl01-ink/5" novalidate>
    <div class="mb-1 grid gap-1">
      <h3 class="text-2xl font-extrabold tracking-[-0.02em] text-tfl01-ink">Join the studio</h3>
      <p class="text-sm text-tfl01-mut">Focus a field and watch the label ripple.</p>
    </div>
    <div class="group relative">
      <input class="peer h-14 w-full rounded-xl border-[1.5px] border-tfl01-line bg-white px-4 pt-[22px] pb-1.5 text-base text-tfl01-ink outline-hidden transition-[border-color,box-shadow] duration-200 hover:border-tfl01-line-hover focus:border-tfl01-acc focus:ring-4 focus:ring-tfl01-acc/15" type="text" id="tfl-01-name" name="name" placeholder=" " autocomplete="name">
      <label class="pointer-events-none absolute left-4 top-1/2 -translate-y-1/2 text-base text-tfl01-mut *:inline-block *:origin-bottom-left *:transition-[translate,scale,color] *:duration-[340ms] *:ease-[cubic-bezier(.3,1.6,.4,1)] *:[transition-delay:calc(var(--i)*30ms)] group-focus-within:*:-translate-y-3.5 group-focus-within:*:scale-72 group-focus-within:*:text-tfl01-acc group-has-[input:not(:placeholder-shown)]:*:-translate-y-3.5 group-has-[input:not(:placeholder-shown)]:*:scale-72 motion-reduce:*:[transition-delay:0s]" for="tfl-01-name">
        <span class="sr-only">Your name</span>
        <span aria-hidden="true" style="--i:0">Y</span><span aria-hidden="true" style="--i:1">o</span><span aria-hidden="true" style="--i:2">u</span><span aria-hidden="true" style="--i:3">r</span><span aria-hidden="true" style="--i:4">&nbsp;</span><span aria-hidden="true" style="--i:5">n</span><span aria-hidden="true" style="--i:6">a</span><span aria-hidden="true" style="--i:7">m</span><span aria-hidden="true" style="--i:8">e</span>
      </label>
    </div>
    <div class="group relative">
      <input class="peer h-14 w-full rounded-xl border-[1.5px] border-tfl01-line bg-white px-4 pt-[22px] pb-1.5 text-base text-tfl01-ink outline-hidden transition-[border-color,box-shadow] duration-200 hover:border-tfl01-line-hover focus:border-tfl01-acc focus:ring-4 focus:ring-tfl01-acc/15" type="email" id="tfl-01-mail" name="email" placeholder=" " autocomplete="email">
      <label class="pointer-events-none absolute left-4 top-1/2 -translate-y-1/2 text-base text-tfl01-mut *:inline-block *:origin-bottom-left *:transition-[translate,scale,color] *:duration-[340ms] *:ease-[cubic-bezier(.3,1.6,.4,1)] *:[transition-delay:calc(var(--i)*30ms)] group-focus-within:*:-translate-y-3.5 group-focus-within:*:scale-72 group-focus-within:*:text-tfl01-acc group-has-[input:not(:placeholder-shown)]:*:-translate-y-3.5 group-has-[input:not(:placeholder-shown)]:*:scale-72 motion-reduce:*:[transition-delay:0s]" for="tfl-01-mail">
        <span class="sr-only">Email</span>
        <span aria-hidden="true" style="--i:0">E</span><span aria-hidden="true" style="--i:1">m</span><span aria-hidden="true" style="--i:2">a</span><span aria-hidden="true" style="--i:3">i</span><span aria-hidden="true" style="--i:4">l</span>
      </label>
    </div>
    <button class="mt-1 min-h-12 cursor-pointer rounded-xl bg-tfl01-acc text-[15px] font-bold text-white shadow-[0_10px_24px_-12px_var(--color-tfl01-acc)] transition-[filter,scale] duration-150 hover:brightness-110 active:scale-98 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tfl01-acc/50" type="button">Apply</button>
  </form>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfl01-bg: #f6eff6;
  --color-tfl01-bg: oklch(0.96 0.012 320);
  --color-tfl01-glow: #fff9ff;
  --color-tfl01-glow: oklch(0.99 0.008 320);
  --color-tfl01-ink: #241a24;
  --color-tfl01-ink: oklch(0.23 0.025 320);
  --color-tfl01-mut: #6f5e73;
  --color-tfl01-mut: oklch(0.5 0.03 315);
  --color-tfl01-line: #e3d5e3;
  --color-tfl01-line: oklch(0.88 0.02 320);
  --color-tfl01-line-hover: #c9b5ca;
  --color-tfl01-line-hover: oklch(0.79 0.03 320);
  --color-tfl01-acc: #b43aa9;
  --color-tfl01-acc: oklch(0.55 0.19 325);
  --font-tfl01-sans: 'Bricolage Grotesque', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tfl-01 {
  width: 100%;
  min-height: 100svh;
}
```
