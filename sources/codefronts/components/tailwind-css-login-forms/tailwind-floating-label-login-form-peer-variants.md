---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-login-forms/tailwind-floating-label-login-form-peer-variants/"
title: "Tailwind Floating Label Login Form with peer Variants"
section: "components"
category: "tailwind-css-login-forms"
category_name: "Tailwind CSS Login Forms"
description: "The Material-modern favourite: the label sits inside the field, then glides up to a miniaturised top label the moment the field is focused or filled &mdash;…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Floating Label Login Form with peer Variants
Source: https://codefronts.com/components/tailwind-css-login-forms/tailwind-floating-label-login-form-peer-variants/

The Material-modern favourite: the label sits inside the field, then glides up to a miniaturised top label the moment the field is focused or filled &mdash; no JavaScript, no keystroke listeners. This is peer's showcase demo: the CSS original's input:focus + label, input:not(:placeholder-shown) + label becomes peer-focus: and peer-[:not(:placeholder-shown)]: on the label itself.
## HTML
```html
<section class="tlf-03 w-full min-h-svh grid place-items-center bg-tlf03-stage font-tlf03-sans p-6">
  <form novalidate class="w-[min(380px,100%)] flex flex-col gap-6 p-8 bg-white border border-tlf03-edge rounded-2xl shadow-[0_22px_50px_-36px_oklch(0.3_0.04_220/0.5)]">
    <h1 class="text-2xl font-bold tracking-tight text-tlf03-ink">Log in</h1>
    <div class="relative focus-within:[&>input]:border-tlf03-acc">
      <input id="tlf-03-email" type="email" autocomplete="email" placeholder=" " required class="peer w-full h-14 pt-[18px] pb-1 px-0.5 text-base text-tlf03-ink bg-transparent border-0 border-b-2 border-tlf03-line transition-colors duration-200 focus-visible:outline-none">
      <label for="tlf-03-email" class="absolute left-0.5 top-[18px] text-base text-tlf03-ph pointer-events-none origin-top-left transition-[translate,scale,color] duration-200 peer-focus:-translate-y-4 peer-focus:scale-75 peer-focus:text-tlf03-acc peer-[:not(:placeholder-shown)]:-translate-y-4 peer-[:not(:placeholder-shown)]:scale-75 peer-[:not(:placeholder-shown)]:text-tlf03-acc motion-reduce:transition-none">Email address</label>
    </div>
    <div class="relative focus-within:[&>input]:border-tlf03-acc">
      <input id="tlf-03-pw" type="password" autocomplete="current-password" placeholder=" " required class="peer w-full h-14 pt-[18px] pb-1 px-0.5 text-base text-tlf03-ink bg-transparent border-0 border-b-2 border-tlf03-line transition-colors duration-200 focus-visible:outline-none">
      <label for="tlf-03-pw" class="absolute left-0.5 top-[18px] text-base text-tlf03-ph pointer-events-none origin-top-left transition-[translate,scale,color] duration-200 peer-focus:-translate-y-4 peer-focus:scale-75 peer-focus:text-tlf03-acc peer-[:not(:placeholder-shown)]:-translate-y-4 peer-[:not(:placeholder-shown)]:scale-75 peer-[:not(:placeholder-shown)]:text-tlf03-acc motion-reduce:transition-none">Password</label>
    </div>
    <div class="flex items-center justify-between text-[13px]">
      <label class="flex items-center gap-2 min-h-11 text-tlf03-mut cursor-pointer"><input type="checkbox" class="size-4 accent-tlf03-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tlf03-acc"> Remember me</label>
      <a href="#" class="font-semibold text-tlf03-acc no-underline hover:underline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tlf03-acc">Forgot?</a>
    </div>
    <button type="submit" class="h-13 rounded-xl border-0 cursor-pointer bg-tlf03-acc text-white text-[15px] font-semibold transition-[filter,scale] duration-150 hover:brightness-110 active:scale-[0.985] focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-tlf03-ring motion-reduce:transition-none motion-reduce:active:scale-100">Continue</button>
  </form>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tlf03-stage: #f3f6f8;
  --color-tlf03-stage: oklch(0.96 0.006 220);
  --color-tlf03-edge: #e3e8ee;
  --color-tlf03-edge: oklch(0.92 0.008 220);
  --color-tlf03-line: #cdd6dd;
  --color-tlf03-line: oklch(0.86 0.012 220);
  --color-tlf03-ink: #12222b;
  --color-tlf03-ink: oklch(0.24 0.03 220);
  --color-tlf03-mut: #51606a;
  --color-tlf03-mut: oklch(0.48 0.02 220);
  --color-tlf03-ph: #76858f;
  --color-tlf03-ph: oklch(0.6 0.02 220);
  --color-tlf03-acc: #1a8aa8;
  --color-tlf03-acc: oklch(0.55 0.11 220);
  --color-tlf03-ring: #7fc3d6;
  --color-tlf03-ring: oklch(0.55 0.11 220 / 0.5);
  --font-tlf03-sans: 'DM Sans', system-ui, sans-serif;
}

.tlf-03 {
  width: 100%;
  min-height: 100svh;
}
```
