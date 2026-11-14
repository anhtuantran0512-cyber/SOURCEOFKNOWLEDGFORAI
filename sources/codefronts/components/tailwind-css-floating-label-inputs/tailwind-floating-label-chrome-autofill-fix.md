---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-floating-label-inputs/tailwind-floating-label-chrome-autofill-fix/"
title: "Tailwind Floating Label with Chrome Autofill Fix"
section: "components"
category: "tailwind-css-floating-label-inputs"
category_name: "Tailwind CSS Floating Label Inputs"
description: "Chrome autofills and the label crashes through the value — unless peer-autofill: joins the float."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Floating Label with Chrome Autofill Fix
Source: https://codefronts.com/components/tailwind-css-floating-label-inputs/tailwind-floating-label-chrome-autofill-fix/

Chrome autofills and the label crashes through the value — unless peer-autofill: joins the float. The port adds peer-[:-webkit-autofill]: as its own utility (so an unknown selector can never kill the list), re-skins the yellow wash with autofill:shadow-[inset_0_0_0_1000px_…], and floats the label out of the field into an eyebrow above it.
## HTML
```html
<section class="tfl-05 w-full min-h-svh grid place-items-center bg-tfl05-bg px-5 py-12 font-tfl05-sans" aria-label="Autofill-proof floating label demo">
  <form class="flex w-full max-w-[400px] flex-col gap-7 rounded-3xl border border-tfl05-edge bg-tfl05-card p-8 shadow-[0_30px_80px_-40px_oklch(0_0_0/0.8)]" novalidate>
    <div class="grid gap-1.5">
      <h3 class="text-2xl font-extrabold tracking-[-0.02em] text-tfl05-ink">Ship to</h3>
      <p class="text-[13px]/relaxed text-tfl05-mut">Autofill this form from your browser — the labels stay floated.</p>
    </div>
    <div class="relative">
      <input class="peer h-14 w-full rounded-xl border-[1.5px] border-tfl05-line bg-tfl05-field px-4 text-base text-tfl05-ink caret-tfl05-acc outline-hidden transition-[border-color,box-shadow] duration-200 hover:border-tfl05-line-hover focus:border-tfl05-acc focus:ring-4 focus:ring-tfl05-acc/20 autofill:shadow-[inset_0_0_0_1000px_var(--color-tfl05-field)] [&:-webkit-autofill]:shadow-[inset_0_0_0_1000px_var(--color-tfl05-field)] [&:-webkit-autofill]:[-webkit-text-fill-color:var(--color-tfl05-ink)]" type="text" id="tfl-05-name" name="name" placeholder=" " autocomplete="name">
      <label class="pointer-events-none absolute left-4 top-1/2 origin-left -translate-y-1/2 text-base text-tfl05-mut transition-[translate,scale,color,letter-spacing] duration-[240ms] ease-[cubic-bezier(.3,.7,.3,1)] peer-focus:translate-x-[-16px] peer-focus:translate-y-[calc(-50%_-_42px)] peer-focus:scale-70 peer-focus:font-semibold peer-focus:tracking-[.08em] peer-focus:text-tfl05-acc peer-[:not(:placeholder-shown)]:translate-x-[-16px] peer-[:not(:placeholder-shown)]:translate-y-[calc(-50%_-_42px)] peer-[:not(:placeholder-shown)]:scale-70 peer-[:not(:placeholder-shown)]:font-semibold peer-[:not(:placeholder-shown)]:tracking-[.08em] peer-autofill:translate-x-[-16px] peer-autofill:translate-y-[calc(-50%_-_42px)] peer-autofill:scale-70 peer-autofill:font-semibold peer-autofill:tracking-[.08em] peer-[:-webkit-autofill]:translate-x-[-16px] peer-[:-webkit-autofill]:translate-y-[calc(-50%_-_42px)] peer-[:-webkit-autofill]:scale-70 peer-[:-webkit-autofill]:font-semibold peer-[:-webkit-autofill]:tracking-[.08em] motion-reduce:transition-none" for="tfl-05-name">Full name</label>
    </div>
    <div class="relative">
      <input class="peer h-14 w-full rounded-xl border-[1.5px] border-tfl05-line bg-tfl05-field px-4 text-base text-tfl05-ink caret-tfl05-acc outline-hidden transition-[border-color,box-shadow] duration-200 hover:border-tfl05-line-hover focus:border-tfl05-acc focus:ring-4 focus:ring-tfl05-acc/20 autofill:shadow-[inset_0_0_0_1000px_var(--color-tfl05-field)] [&:-webkit-autofill]:shadow-[inset_0_0_0_1000px_var(--color-tfl05-field)] [&:-webkit-autofill]:[-webkit-text-fill-color:var(--color-tfl05-ink)]" type="email" id="tfl-05-email" name="email" placeholder=" " autocomplete="email">
      <label class="pointer-events-none absolute left-4 top-1/2 origin-left -translate-y-1/2 text-base text-tfl05-mut transition-[translate,scale,color,letter-spacing] duration-[240ms] ease-[cubic-bezier(.3,.7,.3,1)] peer-focus:translate-x-[-16px] peer-focus:translate-y-[calc(-50%_-_42px)] peer-focus:scale-70 peer-focus:font-semibold peer-focus:tracking-[.08em] peer-focus:text-tfl05-acc peer-[:not(:placeholder-shown)]:translate-x-[-16px] peer-[:not(:placeholder-shown)]:translate-y-[calc(-50%_-_42px)] peer-[:not(:placeholder-shown)]:scale-70 peer-[:not(:placeholder-shown)]:font-semibold peer-[:not(:placeholder-shown)]:tracking-[.08em] peer-autofill:translate-x-[-16px] peer-autofill:translate-y-[calc(-50%_-_42px)] peer-autofill:scale-70 peer-autofill:font-semibold peer-autofill:tracking-[.08em] peer-[:-webkit-autofill]:translate-x-[-16px] peer-[:-webkit-autofill]:translate-y-[calc(-50%_-_42px)] peer-[:-webkit-autofill]:scale-70 peer-[:-webkit-autofill]:font-semibold peer-[:-webkit-autofill]:tracking-[.08em] motion-reduce:transition-none" for="tfl-05-email">Email</label>
    </div>
    <div class="relative">
      <input class="peer h-14 w-full rounded-xl border-[1.5px] border-tfl05-line bg-tfl05-field px-4 text-base text-tfl05-ink caret-tfl05-acc outline-hidden transition-[border-color,box-shadow] duration-200 hover:border-tfl05-line-hover focus:border-tfl05-acc focus:ring-4 focus:ring-tfl05-acc/20 autofill:shadow-[inset_0_0_0_1000px_var(--color-tfl05-field)] [&:-webkit-autofill]:shadow-[inset_0_0_0_1000px_var(--color-tfl05-field)] [&:-webkit-autofill]:[-webkit-text-fill-color:var(--color-tfl05-ink)]" type="text" id="tfl-05-street" name="street-address" placeholder=" " autocomplete="street-address">
      <label class="pointer-events-none absolute left-4 top-1/2 origin-left -translate-y-1/2 text-base text-tfl05-mut transition-[translate,scale,color,letter-spacing] duration-[240ms] ease-[cubic-bezier(.3,.7,.3,1)] peer-focus:translate-x-[-16px] peer-focus:translate-y-[calc(-50%_-_42px)] peer-focus:scale-70 peer-focus:font-semibold peer-focus:tracking-[.08em] peer-focus:text-tfl05-acc peer-[:not(:placeholder-shown)]:translate-x-[-16px] peer-[:not(:placeholder-shown)]:translate-y-[calc(-50%_-_42px)] peer-[:not(:placeholder-shown)]:scale-70 peer-[:not(:placeholder-shown)]:font-semibold peer-[:not(:placeholder-shown)]:tracking-[.08em] peer-autofill:translate-x-[-16px] peer-autofill:translate-y-[calc(-50%_-_42px)] peer-autofill:scale-70 peer-autofill:font-semibold peer-autofill:tracking-[.08em] peer-[:-webkit-autofill]:translate-x-[-16px] peer-[:-webkit-autofill]:translate-y-[calc(-50%_-_42px)] peer-[:-webkit-autofill]:scale-70 peer-[:-webkit-autofill]:font-semibold peer-[:-webkit-autofill]:tracking-[.08em] motion-reduce:transition-none" for="tfl-05-street">Street address</label>
    </div>
    <button class="min-h-12 cursor-pointer rounded-xl bg-tfl05-acc text-[15px] font-extrabold text-tfl05-on-acc transition-[filter,scale] duration-150 hover:brightness-110 active:scale-98 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tfl05-acc/60" type="submit">Save address</button>
  </form>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfl05-bg: #0f1420;
  --color-tfl05-bg: oklch(0.19 0.02 265);
  --color-tfl05-card: #171d2e;
  --color-tfl05-card: oklch(0.23 0.03 265);
  --color-tfl05-edge: #232b42;
  --color-tfl05-edge: oklch(0.29 0.035 265);
  --color-tfl05-field: #101627;
  --color-tfl05-field: oklch(0.2 0.03 265);
  --color-tfl05-line: #2b3450;
  --color-tfl05-line: oklch(0.32 0.04 268);
  --color-tfl05-line-hover: #3b4668;
  --color-tfl05-line-hover: oklch(0.39 0.05 268);
  --color-tfl05-ink: #eef1fa;
  --color-tfl05-ink: oklch(0.96 0.01 270);
  --color-tfl05-mut: #9aa2bc;
  --color-tfl05-mut: oklch(0.72 0.03 270);
  --color-tfl05-acc: #2fc2b0;
  --color-tfl05-acc: oklch(0.74 0.13 180);
  --color-tfl05-on-acc: #04211e;
  --color-tfl05-on-acc: oklch(0.22 0.04 180);
  --font-tfl05-sans: 'Manrope', system-ui, sans-serif;
}

.tfl-05 {
  width: 100%;
  min-height: 100svh;
}
```
