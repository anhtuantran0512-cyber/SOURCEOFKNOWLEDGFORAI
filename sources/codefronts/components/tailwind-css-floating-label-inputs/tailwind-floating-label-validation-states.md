---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-floating-label-inputs/tailwind-floating-label-validation-states/"
title: "Tailwind Floating Label Validation States (Error + Success)"
section: "components"
category: "tailwind-css-floating-label-inputs"
category_name: "Tailwind CSS Floating Label Inputs"
description: "CSS-only validation that waits for the user: peer-user-invalid: turns border, label and message red only after interaction,…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Floating Label Validation States (Error + Success)
Source: https://codefronts.com/components/tailwind-css-floating-label-inputs/tailwind-floating-label-validation-states/

CSS-only validation that waits for the user: peer-user-invalid: turns border, label and message red only after interaction, has-[input:user-invalid]:animate-tfl06-shake nudges the field, and has-[input:user-valid]:after:opacity-100 reveals a check chip. Native constraint attributes do all the checking; the label flips on a 3D rotateX as it floats.
## HTML
```html
<section class="tfl-06 w-full min-h-svh grid place-items-center bg-tfl06-bg px-5 py-12 font-tfl06-sans" aria-label="Floating label validation demo">
  <form class="flex w-full max-w-[400px] flex-col gap-2 rounded-3xl bg-white p-8 shadow-[0_24px_60px_-32px_oklch(0.3_0.03_80/0.4)] ring-1 ring-tfl06-ink/5">
    <div class="mb-4 grid gap-1">
      <h3 class="text-2xl font-extrabold tracking-[-0.02em] text-tfl06-ink">Create account</h3>
      <p class="text-sm text-tfl06-mut">Type, then tab away to see each field validate.</p>
    </div>
    <div class="relative pb-[26px] has-[input:user-invalid]:animate-tfl06-shake after:pointer-events-none after:absolute after:right-3.5 after:top-7 after:grid after:size-6 after:-translate-y-1/2 after:scale-50 after:place-items-center after:rounded-full after:bg-tfl06-ok after:text-xs after:font-extrabold after:text-white after:opacity-0 after:transition-[opacity,scale] after:duration-200 after:content-['✓'] has-[input:user-valid]:after:scale-100 has-[input:user-valid]:after:opacity-100 motion-reduce:animate-none">
      <input class="peer h-14 w-full rounded-xl border-[1.5px] border-tfl06-line bg-white pt-[22px] pr-12 pb-1.5 pl-4 text-base text-tfl06-ink outline-hidden transition-[border-color,box-shadow] duration-200 hover:border-tfl06-line-hover focus:border-tfl06-acc focus:ring-4 focus:ring-tfl06-acc/15 user-valid:border-tfl06-ok user-invalid:border-tfl06-err user-invalid:ring-4 user-invalid:ring-tfl06-err/12" type="email" id="tfl-06-email" name="email" placeholder=" " required autocomplete="email" aria-describedby="tfl-06-email-msg">
      <label class="pointer-events-none absolute left-4 top-7 origin-left -translate-y-1/2 text-base text-tfl06-mut [transform:perspective(320px)_rotateX(0deg)] transition-[translate,scale,transform,color] duration-400 ease-[cubic-bezier(.35,.7,.3,1)] peer-focus:translate-y-[calc(-50%_-_13px)] peer-focus:scale-72 peer-focus:[transform:perspective(320px)_rotateX(360deg)] peer-focus:text-tfl06-acc peer-[:not(:placeholder-shown)]:translate-y-[calc(-50%_-_13px)] peer-[:not(:placeholder-shown)]:scale-72 peer-[:not(:placeholder-shown)]:[transform:perspective(320px)_rotateX(360deg)] peer-user-valid:text-tfl06-ok peer-user-invalid:text-tfl06-err motion-reduce:transition-none" for="tfl-06-email">Email address</label>
      <p class="absolute bottom-1 left-0.5 text-xs/tight text-tfl06-mut transition-colors peer-user-invalid:font-semibold peer-user-invalid:text-tfl06-err" id="tfl-06-email-msg">Enter a valid email, e.g. [email protected]</p>
    </div>
    <div class="relative pb-[26px] has-[input:user-invalid]:animate-tfl06-shake after:pointer-events-none after:absolute after:right-3.5 after:top-7 after:grid after:size-6 after:-translate-y-1/2 after:scale-50 after:place-items-center after:rounded-full after:bg-tfl06-ok after:text-xs after:font-extrabold after:text-white after:opacity-0 after:transition-[opacity,scale] after:duration-200 after:content-['✓'] has-[input:user-valid]:after:scale-100 has-[input:user-valid]:after:opacity-100 motion-reduce:animate-none">
      <input class="peer h-14 w-full rounded-xl border-[1.5px] border-tfl06-line bg-white pt-[22px] pr-12 pb-1.5 pl-4 text-base text-tfl06-ink outline-hidden transition-[border-color,box-shadow] duration-200 hover:border-tfl06-line-hover focus:border-tfl06-acc focus:ring-4 focus:ring-tfl06-acc/15 user-valid:border-tfl06-ok user-invalid:border-tfl06-err user-invalid:ring-4 user-invalid:ring-tfl06-err/12" type="text" id="tfl-06-user" name="username" placeholder=" " required minlength="4" pattern="[a-zA-Z0-9_]+" autocomplete="username" aria-describedby="tfl-06-user-msg">
      <label class="pointer-events-none absolute left-4 top-7 origin-left -translate-y-1/2 text-base text-tfl06-mut [transform:perspective(320px)_rotateX(0deg)] transition-[translate,scale,transform,color] duration-400 ease-[cubic-bezier(.35,.7,.3,1)] peer-focus:translate-y-[calc(-50%_-_13px)] peer-focus:scale-72 peer-focus:[transform:perspective(320px)_rotateX(360deg)] peer-focus:text-tfl06-acc peer-[:not(:placeholder-shown)]:translate-y-[calc(-50%_-_13px)] peer-[:not(:placeholder-shown)]:scale-72 peer-[:not(:placeholder-shown)]:[transform:perspective(320px)_rotateX(360deg)] peer-user-valid:text-tfl06-ok peer-user-invalid:text-tfl06-err motion-reduce:transition-none" for="tfl-06-user">Username</label>
      <p class="absolute bottom-1 left-0.5 text-xs/tight text-tfl06-mut transition-colors peer-user-invalid:font-semibold peer-user-invalid:text-tfl06-err" id="tfl-06-user-msg">4+ characters — letters, numbers, underscores</p>
    </div>
    <button class="mt-2 min-h-12 cursor-pointer rounded-xl bg-tfl06-ink text-[15px] font-bold text-white transition-[filter,scale] duration-150 hover:brightness-150 active:scale-98 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tfl06-acc/50" type="submit">Sign up</button>
  </form>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfl06-bg: #f4f3f0;
  --color-tfl06-bg: oklch(0.96 0.005 90);
  --color-tfl06-ink: #221f18;
  --color-tfl06-ink: oklch(0.23 0.012 85);
  --color-tfl06-mut: #6a6558;
  --color-tfl06-mut: oklch(0.5 0.02 85);
  --color-tfl06-line: #d9d6cd;
  --color-tfl06-line: oklch(0.87 0.012 90);
  --color-tfl06-line-hover: #bdb8ab;
  --color-tfl06-line-hover: oklch(0.78 0.018 90);
  --color-tfl06-acc: #4a50d4;
  --color-tfl06-acc: oklch(0.5 0.2 272);
  --color-tfl06-err: #c8372e;
  --color-tfl06-err: oklch(0.55 0.19 27);
  --color-tfl06-ok: #1f8a4c;
  --color-tfl06-ok: oklch(0.55 0.14 152);
  --font-tfl06-sans: 'DM Sans', system-ui, sans-serif;
  --animate-tfl06-shake: tfl06-shake 0.3s ease;

  @keyframes tfl06-shake {
    20% {
      transform: translateX(-5px);
    }

    40% {
      transform: translateX(5px);
    }

    60% {
      transform: translateX(-3px);
    }

    80% {
      transform: translateX(3px);
    }
  }
}

.tfl-06 {
  width: 100%;
  min-height: 100svh;
}
```
