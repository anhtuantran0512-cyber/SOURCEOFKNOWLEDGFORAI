---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-stacked-cards/tailwind-stacked-testimonial-slider-radio/"
title: "Tailwind Stacked Testimonial Slider Radio"
section: "components"
category: "tailwind-stacked-cards"
category_name: "Tailwind Stacked Cards"
description: "Three reviews, a cyclic stack, no JavaScript &mdash; and the port's headline feature is named peers."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Stacked Testimonial Slider Radio
Source: https://codefronts.com/components/tailwind-stacked-cards/tailwind-stacked-testimonial-slider-radio/

Three reviews, a cyclic stack, no JavaScript &mdash; and the port's headline feature is named peers. The mapping here is a rotation (radio&nbsp;1 puts quote&nbsp;2 second and quote&nbsp;3 third; radio&nbsp;2 rotates it on), which nesting cannot solve because each quote must respond to all three radios. peer/t1, peer/t2, peer/t3 plus peer-checked/t2: expresses it exactly, and nine positional selectors disappear.
## HTML
```html
<section class="stk-30 grid w-full min-h-svh place-items-center px-5 py-15 font-stk30-sans bg-linear-[160deg,var(--color-stk30-p1),var(--color-stk30-p2)]" aria-label="Customer testimonials">
  <div class="relative grid w-[min(330px,88vw)] grid-cols-[1fr_auto_auto_auto_1fr] justify-items-center gap-y-7">
    <input class="peer/t1 absolute size-0 opacity-0" type="radio" name="stk-30" id="stk-30-t1" checked aria-label="Testimonial 1">
    <input class="peer/t2 absolute size-0 opacity-0" type="radio" name="stk-30" id="stk-30-t2" aria-label="Testimonial 2">
    <input class="peer/t3 absolute size-0 opacity-0" type="radio" name="stk-30" id="stk-30-t3" aria-label="Testimonial 3">
      <figure class="col-span-5 col-start-1 row-start-1 flex h-75 w-full flex-col justify-between rounded-[22px] border border-stk30-line bg-stk30-card p-7.5 opacity-0 shadow-[0_18px_40px_rgba(120,80,50,0.18)] translate-y-7 scale-[0.88] z-1 transition-[transform,opacity] duration-600 ease-stk30 peer-checked/t1:z-4 peer-checked/t1:translate-y-0 peer-checked/t1:scale-100 peer-checked/t1:opacity-100 peer-checked/t3:z-3 peer-checked/t3:translate-y-3.5 peer-checked/t3:scale-[0.94] peer-checked/t3:opacity-55 peer-checked/t2:z-2 peer-checked/t2:translate-y-7 peer-checked/t2:scale-[0.88] peer-checked/t2:opacity-30 motion-reduce:transition-none">
        <blockquote class="m-0 font-stk30-serif text-xl italic leading-snug text-stk30-ink">&ldquo;This completely changed how our team ships. We cut launch time in half.&rdquo;</blockquote>
        <figcaption class="flex items-center gap-3">
          <span class="block size-11 shrink-0 rounded-full bg-linear-[135deg,var(--color-stk30-av1a),var(--color-stk30-av1b)]" aria-hidden="true"></span>
          <span><b class="block text-[0.9rem] font-semibold text-stk30-name">Maya Chen</b><span class="text-[0.78rem] text-stk30-meta">Head of Product, Loop</span></span>
        </figcaption>
      </figure>
      <figure class="col-span-5 col-start-1 row-start-1 flex h-75 w-full flex-col justify-between rounded-[22px] border border-stk30-line bg-stk30-card p-7.5 opacity-0 shadow-[0_18px_40px_rgba(120,80,50,0.18)] translate-y-7 scale-[0.88] z-1 transition-[transform,opacity] duration-600 ease-stk30 peer-checked/t2:z-4 peer-checked/t2:translate-y-0 peer-checked/t2:scale-100 peer-checked/t2:opacity-100 peer-checked/t1:z-3 peer-checked/t1:translate-y-3.5 peer-checked/t1:scale-[0.94] peer-checked/t1:opacity-55 peer-checked/t3:z-2 peer-checked/t3:translate-y-7 peer-checked/t3:scale-[0.88] peer-checked/t3:opacity-30 motion-reduce:transition-none">
        <blockquote class="m-0 font-stk30-serif text-xl italic leading-snug text-stk30-ink">&ldquo;Beautiful, fast, and genuinely a joy to use every single day.&rdquo;</blockquote>
        <figcaption class="flex items-center gap-3">
          <span class="block size-11 shrink-0 rounded-full bg-linear-[135deg,var(--color-stk30-av2a),var(--color-stk30-av2b)]" aria-hidden="true"></span>
          <span><b class="block text-[0.9rem] font-semibold text-stk30-name">Theo Marsh</b><span class="text-[0.78rem] text-stk30-meta">Founder, Northbeam</span></span>
        </figcaption>
      </figure>
      <figure class="col-span-5 col-start-1 row-start-1 flex h-75 w-full flex-col justify-between rounded-[22px] border border-stk30-line bg-stk30-card p-7.5 opacity-0 shadow-[0_18px_40px_rgba(120,80,50,0.18)] translate-y-7 scale-[0.88] z-1 transition-[transform,opacity] duration-600 ease-stk30 peer-checked/t3:z-4 peer-checked/t3:translate-y-0 peer-checked/t3:scale-100 peer-checked/t3:opacity-100 peer-checked/t2:z-3 peer-checked/t2:translate-y-3.5 peer-checked/t2:scale-[0.94] peer-checked/t2:opacity-55 peer-checked/t1:z-2 peer-checked/t1:translate-y-7 peer-checked/t1:scale-[0.88] peer-checked/t1:opacity-30 motion-reduce:transition-none">
        <blockquote class="m-0 font-stk30-serif text-xl italic leading-snug text-stk30-ink">&ldquo;The support alone is worth it. Best decision we made this year.&rdquo;</blockquote>
        <figcaption class="flex items-center gap-3">
          <span class="block size-11 shrink-0 rounded-full bg-linear-[135deg,var(--color-stk30-av3a),var(--color-stk30-av3b)]" aria-hidden="true"></span>
          <span><b class="block text-[0.9rem] font-semibold text-stk30-name">Lena Ortiz</b><span class="text-[0.78rem] text-stk30-meta">CTO, Brightside</span></span>
        </figcaption>
      </figure>
      <label class="col-start-2 row-start-2 grid size-11 cursor-pointer place-items-center rounded-full before:block before:size-2.75 before:rounded-full before:bg-stk30-dot before:transition-[background-color,transform] before:duration-300 hover:before:bg-stk30-dothover peer-checked/t1:before:scale-130 peer-checked/t1:before:bg-stk30-active peer-focus-visible/t1:outline-3 peer-focus-visible/t1:outline-stk30-active" for="stk-30-t1">
        <span class="sr-only">Show testimonial 1</span>
      </label>
      <label class="col-start-3 row-start-2 grid size-11 cursor-pointer place-items-center rounded-full before:block before:size-2.75 before:rounded-full before:bg-stk30-dot before:transition-[background-color,transform] before:duration-300 hover:before:bg-stk30-dothover peer-checked/t2:before:scale-130 peer-checked/t2:before:bg-stk30-active peer-focus-visible/t2:outline-3 peer-focus-visible/t2:outline-stk30-active" for="stk-30-t2">
        <span class="sr-only">Show testimonial 2</span>
      </label>
      <label class="col-start-4 row-start-2 grid size-11 cursor-pointer place-items-center rounded-full before:block before:size-2.75 before:rounded-full before:bg-stk30-dot before:transition-[background-color,transform] before:duration-300 hover:before:bg-stk30-dothover peer-checked/t3:before:scale-130 peer-checked/t3:before:bg-stk30-active peer-focus-visible/t3:outline-3 peer-focus-visible/t3:outline-stk30-active" for="stk-30-t3">
        <span class="sr-only">Show testimonial 3</span>
      </label>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-stk30-p1: #fef6ee;
  --color-stk30-p1: oklch(0.97 0.016 75);
  --color-stk30-p2: #f4e4d4;
  --color-stk30-p2: oklch(0.92 0.030 70);
  --color-stk30-card: #fffdfa;
  --color-stk30-card: oklch(0.99 0.006 80);
  --color-stk30-line: #f0e2d2;
  --color-stk30-line: oklch(0.93 0.020 75);
  --color-stk30-ink: #3a2e24;
  --color-stk30-ink: oklch(0.33 0.022 60);
  --color-stk30-name: #2a201a;
  --color-stk30-name: oklch(0.26 0.020 55);
  --color-stk30-meta: #9b7d5f;
  --color-stk30-meta: oklch(0.62 0.045 65);
  --color-stk30-dot: #d8c3aa;
  --color-stk30-dot: oklch(0.83 0.035 75);
  --color-stk30-dothover: #c9a98a;
  --color-stk30-dothover: oklch(0.76 0.050 70);
  --color-stk30-active: #b8553f;
  --color-stk30-active: oklch(0.55 0.145 35);
  --color-stk30-av1a: #ff9a3c;
  --color-stk30-av1b: #ff5e62;
  --color-stk30-av2a: #43cea2;
  --color-stk30-av2b: #185a9d;
  --color-stk30-av3a: #c471f5;
  --color-stk30-av3b: #7f53ac;
  --font-stk30-sans: 'Geist', system-ui, sans-serif;
  --font-stk30-serif: 'Newsreader', Georgia, serif;
  --ease-stk30: cubic-bezier(0.3, 0.9, 0.3, 1);
}
```
