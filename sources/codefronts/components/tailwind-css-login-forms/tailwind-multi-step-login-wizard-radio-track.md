---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-login-forms/tailwind-multi-step-login-wizard-radio-track/"
title: "Tailwind Multi-Step Login Wizard with Radio-Driven Track"
section: "components"
category: "tailwind-css-login-forms"
category_name: "Tailwind CSS Login Forms"
description: "A multi-stage sign-in that lowers upfront resistance: email, then password, then a security code, with inactive panels sliding off a translated track."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Multi-Step Login Wizard with Radio-Driven Track
Source: https://codefronts.com/components/tailwind-css-login-forms/tailwind-multi-step-login-wizard-radio-track/

A multi-stage sign-in that lowers upfront resistance: email, then password, then a security code, with inactive panels sliding off a translated track. Three radios hold the stage, Next/Back are their labels, and the port's interesting constraint is that Tailwind's peer only reaches later siblings &mdash; which is exactly how this markup is already arranged.
## HTML
```html
<section class="tlf-20 w-full min-h-svh grid place-items-center bg-tlf20-stage font-tlf20-sans p-6">
  <form novalidate class="w-[min(380px,100%)] p-7 bg-white border border-tlf20-edge rounded-[18px] overflow-hidden shadow-[0_24px_56px_-38px_oklch(0.25_0.06_265/0.5)]">
    <input type="radio" name="tlf-20-step" id="tlf-20-s1" checked class="peer/s1 sr-only" aria-label="Step 1 of 3: email">
    <input type="radio" name="tlf-20-step" id="tlf-20-s2" class="peer/s2 sr-only" aria-label="Step 2 of 3: password">
    <input type="radio" name="tlf-20-step" id="tlf-20-s3" class="peer/s3 sr-only" aria-label="Step 3 of 3: security code">
    <div aria-hidden="true" class="h-1.5 mb-6 rounded-full bg-tlf20-track overflow-hidden">
      <span class="block h-full w-1/3 rounded-full bg-tlf20-acc transition-[width] duration-400 ease-[cubic-bezier(0.4,0,0.2,1)] peer-checked/s2:w-2/3 peer-checked/s3:w-full motion-reduce:transition-none"></span>
    </div>
    <div class="overflow-hidden">
      <div class="flex w-[300%] transition-transform duration-450 ease-[cubic-bezier(0.4,0,0.2,1)] peer-checked/s2:-translate-x-1/3 peer-checked/s3:-translate-x-2/3 motion-reduce:transition-none">
        <fieldset class="w-1/3 px-0.5 border-0 flex flex-col gap-3.5">
          <legend class="mb-1 p-0 text-[19px] font-bold text-tlf20-ink">Your email</legend>
          <input type="email" autocomplete="email" placeholder="[email protected]" required class="h-12 px-3.5 rounded-xl text-[15px] text-tlf20-ink bg-tlf20-field border-[1.5px] border-tlf20-fieldedge transition-[border-color,box-shadow] duration-150 placeholder:text-tlf20-ph focus-visible:outline-none focus-visible:border-tlf20-acc focus-visible:ring-4 focus-visible:ring-tlf20-halo">
          <label for="tlf-20-s2" class="grid place-items-center h-12 rounded-xl cursor-pointer bg-tlf20-acc text-white text-[15px] font-semibold transition-[filter] duration-150 hover:brightness-110">Continue</label>
        </fieldset>
        <fieldset class="w-1/3 px-0.5 border-0 flex flex-col gap-3.5">
          <legend class="mb-1 p-0 text-[19px] font-bold text-tlf20-ink">Your password</legend>
          <input type="password" autocomplete="current-password" placeholder="&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;" required class="h-12 px-3.5 rounded-xl text-[15px] text-tlf20-ink bg-tlf20-field border-[1.5px] border-tlf20-fieldedge transition-[border-color,box-shadow] duration-150 placeholder:text-tlf20-ph focus-visible:outline-none focus-visible:border-tlf20-acc focus-visible:ring-4 focus-visible:ring-tlf20-halo">
          <div class="flex gap-2.5">
            <label for="tlf-20-s1" class="grid place-items-center basis-[92px] h-12 rounded-xl cursor-pointer bg-white border-[1.5px] border-tlf20-fieldedge text-tlf20-mut text-[15px] font-semibold transition-colors duration-150 hover:bg-tlf20-hover">Back</label>
            <label for="tlf-20-s3" class="grid place-items-center flex-1 h-12 rounded-xl cursor-pointer bg-tlf20-acc text-white text-[15px] font-semibold transition-[filter] duration-150 hover:brightness-110">Continue</label>
          </div>
        </fieldset>
        <fieldset class="w-1/3 px-0.5 border-0 flex flex-col gap-3.5">
          <legend class="mb-1 p-0 text-[19px] font-bold text-tlf20-ink">Security code</legend>
          <input type="text" inputmode="numeric" autocomplete="one-time-code" placeholder="6-digit code" required class="h-12 px-3.5 rounded-xl text-[15px] tracking-[0.2em] text-tlf20-ink bg-tlf20-field border-[1.5px] border-tlf20-fieldedge transition-[border-color,box-shadow] duration-150 placeholder:tracking-normal placeholder:text-tlf20-ph focus-visible:outline-none focus-visible:border-tlf20-acc focus-visible:ring-4 focus-visible:ring-tlf20-halo">
          <div class="flex gap-2.5">
            <label for="tlf-20-s2" class="grid place-items-center basis-[92px] h-12 rounded-xl cursor-pointer bg-white border-[1.5px] border-tlf20-fieldedge text-tlf20-mut text-[15px] font-semibold transition-colors duration-150 hover:bg-tlf20-hover">Back</label>
            <button type="submit" class="flex-1 h-12 rounded-xl border-0 cursor-pointer bg-tlf20-acc text-white text-[15px] font-semibold transition-[filter,scale] duration-150 hover:brightness-110 active:scale-[0.985] focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tlf20-ring motion-reduce:transition-none motion-reduce:active:scale-100">Sign in</button>
          </div>
        </fieldset>
      </div>
    </div>
  </form>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tlf20-stage: #eef1f7;
  --color-tlf20-stage: oklch(0.95 0.008 265);
  --color-tlf20-edge: #e5e9f2;
  --color-tlf20-edge: oklch(0.92 0.008 265);
  --color-tlf20-fieldedge: #d8deeb;
  --color-tlf20-fieldedge: oklch(0.88 0.012 265);
  --color-tlf20-field: #fafbfe;
  --color-tlf20-field: oklch(0.99 0.003 265);
  --color-tlf20-hover: #f2f5fb;
  --color-tlf20-hover: oklch(0.97 0.006 265);
  --color-tlf20-track: #e6eaf3;
  --color-tlf20-track: oklch(0.93 0.008 265);
  --color-tlf20-ink: #1a2237;
  --color-tlf20-ink: oklch(0.25 0.04 265);
  --color-tlf20-mut: #4e5a76;
  --color-tlf20-mut: oklch(0.45 0.035 265);
  --color-tlf20-ph: #949db5;
  --color-tlf20-ph: oklch(0.67 0.025 265);
  --color-tlf20-acc: #3e59c9;
  --color-tlf20-acc: oklch(0.5 0.18 265);
  --color-tlf20-halo: #bec8f0;
  --color-tlf20-halo: oklch(0.5 0.18 265 / 0.16);
  --color-tlf20-ring: #93a2ea;
  --color-tlf20-ring: oklch(0.5 0.18 265 / 0.5);
  --font-tlf20-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.tlf-20 {
  width: 100%;
  min-height: 100svh;
}
```
