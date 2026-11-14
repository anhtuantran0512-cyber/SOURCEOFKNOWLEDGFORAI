---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-floating-label-inputs/pure-tailwind-floating-label-input-no-javascript/"
title: "Pure Tailwind Floating Label Input (No JavaScript)"
section: "components"
category: "tailwind-css-floating-label-inputs"
category_name: "Tailwind CSS Floating Label Inputs"
description: "The canonical floating label in its native Tailwind form: peer on the input, and peer-focus: plus peer-[:not(:placeholder-shown)]: on the label."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure Tailwind Floating Label Input (No JavaScript)
Source: https://codefronts.com/components/tailwind-css-floating-label-inputs/pure-tailwind-floating-label-input-no-javascript/

The canonical floating label in its native Tailwind form: peer on the input, and peer-focus: plus peer-[:not(:placeholder-shown)]: on the label. The label floats with translate-y-[calc(-50%_-_13px)] scale-72 — transform-only, zero listeners, zero hydration. Every other demo in the collection builds on this one.
## HTML
```html
<section class="tfl-04 w-full min-h-svh grid place-items-center bg-tfl04-bg px-5 py-12 font-tfl04-sans" aria-label="Pure Tailwind floating label demo">
  <form class="flex w-full max-w-[380px] flex-col gap-5 rounded-3xl bg-white p-8 shadow-[0_24px_60px_-30px_oklch(0.3_0.06_265/0.4)] ring-1 ring-tfl04-ink/5" novalidate>
    <div class="mb-1 grid gap-1">
      <h3 class="text-2xl font-extrabold tracking-[-0.02em] text-tfl04-ink">Sign in</h3>
      <p class="text-sm text-tfl04-mut">Welcome back — pick up where you left off.</p>
    </div>
    <div class="relative">
      <input class="peer h-14 w-full rounded-xl border-[1.5px] border-tfl04-line bg-white px-4 pt-[22px] pb-1.5 text-base text-tfl04-ink outline-hidden transition-[border-color,box-shadow] duration-200 hover:border-tfl04-line-hover focus:border-tfl04-acc focus:ring-4 focus:ring-tfl04-acc/15 motion-reduce:transition-none" type="email" id="tfl-04-email" name="email" placeholder=" " autocomplete="email">
      <label class="pointer-events-none absolute left-4 top-1/2 origin-left -translate-y-1/2 text-base text-tfl04-mut transition-[translate,scale,color] duration-200 ease-out peer-focus:translate-y-[calc(-50%_-_13px)] peer-focus:scale-72 peer-focus:text-tfl04-acc peer-[:not(:placeholder-shown)]:translate-y-[calc(-50%_-_13px)] peer-[:not(:placeholder-shown)]:scale-72 motion-reduce:transition-none" for="tfl-04-email">Email address</label>
    </div>
    <div class="relative">
      <input class="peer h-14 w-full rounded-xl border-[1.5px] border-tfl04-line bg-white px-4 pt-[22px] pb-1.5 text-base text-tfl04-ink outline-hidden transition-[border-color,box-shadow] duration-200 hover:border-tfl04-line-hover focus:border-tfl04-acc focus:ring-4 focus:ring-tfl04-acc/15 motion-reduce:transition-none" type="text" id="tfl-04-name" name="name" placeholder=" " autocomplete="name">
      <label class="pointer-events-none absolute left-4 top-1/2 origin-left -translate-y-1/2 text-base text-tfl04-mut transition-[translate,scale,color] duration-200 ease-out peer-focus:translate-y-[calc(-50%_-_13px)] peer-focus:scale-72 peer-focus:text-tfl04-acc peer-[:not(:placeholder-shown)]:translate-y-[calc(-50%_-_13px)] peer-[:not(:placeholder-shown)]:scale-72 motion-reduce:transition-none" for="tfl-04-name">Full name</label>
    </div>
    <button class="min-h-12 cursor-pointer rounded-xl bg-tfl04-acc text-[15px] font-bold text-white shadow-[0_10px_24px_-12px_var(--color-tfl04-acc)] transition-[filter,scale] duration-150 hover:brightness-110 active:scale-98 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tfl04-acc/50 motion-reduce:transition-none" type="button">Continue</button>
  </form>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfl04-bg: #f2f3f7;
  --color-tfl04-bg: oklch(0.96 0.006 270);
  --color-tfl04-ink: #191c2b;
  --color-tfl04-ink: oklch(0.22 0.03 270);
  --color-tfl04-mut: #62677c;
  --color-tfl04-mut: oklch(0.5 0.03 270);
  --color-tfl04-line: #d6d9e4;
  --color-tfl04-line: oklch(0.88 0.015 270);
  --color-tfl04-line-hover: #b4b9cc;
  --color-tfl04-line-hover: oklch(0.78 0.025 270);
  --color-tfl04-acc: #4a50d4;
  --color-tfl04-acc: oklch(0.5 0.2 272);
  --font-tfl04-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.tfl-04 {
  width: 100%;
  min-height: 100svh;
}
```
