---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-login-forms/tailwind-3d-flip-login-card-password-reset/"
title: "Tailwind 3D Flip Login Card with Password Reset Back Face"
section: "components"
category: "tailwind-css-login-forms"
category_name: "Tailwind CSS Login Forms"
description: "Forgot Password lives on the back of the login card: tick a hidden checkbox and the whole card rotates in 3D to reveal the recovery form &mdash; no redirect,…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind 3D Flip Login Card with Password Reset Back Face
Source: https://codefronts.com/components/tailwind-css-login-forms/tailwind-3d-flip-login-card-password-reset/

Forgot Password lives on the back of the login card: tick a hidden checkbox and the whole card rotates in 3D to reveal the recovery form &mdash; no redirect, no bleed-through. v4 makes this port unusually clean, because rotate-y-180, backface-hidden, transform-3d and perspective-[1400px] are all real utilities now.
## HTML
```html
<section class="tlf-11 w-full min-h-svh grid place-items-center bg-tlf11-stage font-tlf11-sans p-6">
  <div class="relative w-[min(380px,100%)] perspective-[1400px]">
    <input type="checkbox" id="tlf-11-flip" aria-label="Show password reset form" class="peer sr-only">
    <div class="relative w-full min-h-[420px] transform-3d transition-transform duration-700 ease-[cubic-bezier(0.4,0,0.2,1)] peer-checked:rotate-y-180 peer-focus-visible:outline-3 peer-focus-visible:outline-offset-[6px] peer-focus-visible:outline-tlf11-ring peer-focus-visible:rounded-[18px] motion-reduce:duration-0">
      <form novalidate class="absolute inset-0 backface-hidden flex flex-col gap-3 p-8 bg-white border border-tlf11-edge rounded-[18px] shadow-[0_24px_56px_-38px_oklch(0.35_0.06_50/0.5)]">
        <h2 class="mb-1 text-[23px] font-bold text-tlf11-ink">Sign in</h2>
        <input type="email" placeholder="Email" autocomplete="email" required class="h-12 px-3.5 rounded-xl text-[14.5px] text-tlf11-ink bg-tlf11-field border-[1.5px] border-tlf11-fieldedge transition-[border-color,box-shadow] duration-150 placeholder:text-tlf11-ph focus-visible:outline-none focus-visible:border-tlf11-acc focus-visible:ring-4 focus-visible:ring-tlf11-halo">
        <input type="password" placeholder="Password" autocomplete="current-password" required class="h-12 px-3.5 rounded-xl text-[14.5px] text-tlf11-ink bg-tlf11-field border-[1.5px] border-tlf11-fieldedge transition-[border-color,box-shadow] duration-150 placeholder:text-tlf11-ph focus-visible:outline-none focus-visible:border-tlf11-acc focus-visible:ring-4 focus-visible:ring-tlf11-halo">
        <button type="submit" class="h-12 rounded-xl border-0 cursor-pointer bg-tlf11-acc text-white text-[15px] font-semibold transition-[filter,scale] duration-150 hover:brightness-110 active:scale-[0.985] focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tlf11-ring motion-reduce:transition-none motion-reduce:active:scale-100">Log in</button>
        <label for="tlf-11-flip" class="grid place-items-center self-center min-h-11 px-2 text-[13px] font-semibold text-tlf11-acc cursor-pointer hover:underline">Forgot password?</label>
      </form>
      <form novalidate class="absolute inset-0 backface-hidden rotate-y-180 flex flex-col gap-3 p-8 bg-white border border-tlf11-edge rounded-[18px] shadow-[0_24px_56px_-38px_oklch(0.35_0.06_50/0.5)]">
        <h2 class="text-[23px] font-bold text-tlf11-ink">Reset password</h2>
        <p class="-mt-1.5 mb-1 text-[13.5px]/[1.5] text-tlf11-mut">Enter your email and we&rsquo;ll send a reset link.</p>
        <input type="email" placeholder="Email" autocomplete="email" required class="h-12 px-3.5 rounded-xl text-[14.5px] text-tlf11-ink bg-tlf11-field border-[1.5px] border-tlf11-fieldedge transition-[border-color,box-shadow] duration-150 placeholder:text-tlf11-ph focus-visible:outline-none focus-visible:border-tlf11-acc focus-visible:ring-4 focus-visible:ring-tlf11-halo">
        <button type="submit" class="h-12 rounded-xl border-0 cursor-pointer bg-tlf11-acc text-white text-[15px] font-semibold transition-[filter,scale] duration-150 hover:brightness-110 active:scale-[0.985] focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tlf11-ring motion-reduce:transition-none motion-reduce:active:scale-100">Send link</button>
        <label for="tlf-11-flip" class="grid place-items-center self-center min-h-11 px-2 text-[13px] font-semibold text-tlf11-acc cursor-pointer hover:underline">&larr; Back to sign in</label>
      </form>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tlf11-stage: #f5f2ef;
  --color-tlf11-stage: oklch(0.96 0.008 60);
  --color-tlf11-edge: #eadfd6;
  --color-tlf11-edge: oklch(0.91 0.015 60);
  --color-tlf11-fieldedge: #e0d3c8;
  --color-tlf11-fieldedge: oklch(0.87 0.02 60);
  --color-tlf11-field: #fdfbf9;
  --color-tlf11-field: oklch(0.99 0.004 60);
  --color-tlf11-ink: #2a1c12;
  --color-tlf11-ink: oklch(0.25 0.03 50);
  --color-tlf11-mut: #776154;
  --color-tlf11-mut: oklch(0.52 0.03 50);
  --color-tlf11-ph: #9a8577;
  --color-tlf11-ph: oklch(0.63 0.03 50);
  --color-tlf11-acc: #b1452a;
  --color-tlf11-acc: oklch(0.53 0.17 30);
  --color-tlf11-halo: #e9bdb0;
  --color-tlf11-halo: oklch(0.53 0.17 30 / 0.16);
  --color-tlf11-ring: #d9927f;
  --color-tlf11-ring: oklch(0.53 0.17 30 / 0.5);
  --font-tlf11-sans: 'Epilogue', system-ui, sans-serif;
}

.tlf-11 {
  width: 100%;
  min-height: 100svh;
}
/* Older WebKit still wants the prefixed backface property. */

.tlf-11 form {
  -webkit-backface-visibility: hidden;
}
```
