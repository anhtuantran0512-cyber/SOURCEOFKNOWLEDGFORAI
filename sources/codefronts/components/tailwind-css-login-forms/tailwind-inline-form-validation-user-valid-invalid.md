---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-login-forms/tailwind-inline-form-validation-user-valid-invalid/"
title: "Tailwind Inline Form Validation with user-valid and user-invalid"
section: "components"
category: "tailwind-css-login-forms"
category_name: "Tailwind CSS Login Forms"
description: "Enterprise-grade instant feedback with no JavaScript: each field shows a tick when valid and a red hint when not, driven by native constraint validation."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Inline Form Validation with user-valid and user-invalid
Source: https://codefronts.com/components/tailwind-css-login-forms/tailwind-inline-form-validation-user-valid-invalid/

Enterprise-grade instant feedback with no JavaScript: each field shows a tick when valid and a red hint when not, driven by native constraint validation. Two v4 variants carry the whole thing &mdash; user-valid: and user-invalid: &mdash; and the hint reveal uses the grid-template-rows: 0fr &rarr; 1fr trick, which is the only way to animate a collapsed auto height.
## HTML
```html
<section class="tlf-28 w-full min-h-svh grid place-items-center bg-tlf28-stage font-tlf28-sans p-6">
  <form novalidate class="w-[min(400px,100%)] flex flex-col gap-4 p-8 bg-white border border-tlf28-edge rounded-2xl shadow-[0_22px_50px_-38px_oklch(0.25_0.06_265/0.5)]">
    <h1 class="mb-0.5 text-[22px] font-bold text-tlf28-ink">Create account</h1>
    <div class="flex flex-col gap-1.5">
      <label for="tlf-28-email" class="text-[13px] font-semibold text-tlf28-label">Work email</label>
      <div class="relative">
        <input id="tlf-28-email" type="email" autocomplete="email" placeholder="[email protected]" required aria-describedby="tlf-28-email-hint" class="peer w-full h-12 pl-3.5 pr-11 rounded-xl text-[15px] text-tlf28-ink bg-tlf28-field border-[1.5px] border-tlf28-fieldedge transition-[border-color,box-shadow] duration-150 placeholder:text-tlf28-ph focus-visible:outline-none focus-visible:border-tlf28-acc focus-visible:ring-4 focus-visible:ring-tlf28-halo user-valid:border-tlf28-ok user-invalid:border-tlf28-bad">
        <span aria-hidden="true" class="absolute right-3.5 top-1/2 size-5 -translate-y-1/2 scale-40 opacity-0 transition-[opacity,scale] duration-200 peer-user-valid:opacity-100 peer-user-valid:scale-100 peer-user-invalid:opacity-100 peer-user-invalid:scale-100 before:content-[''] before:absolute after:content-[''] after:absolute peer-user-valid:before:left-1.5 peer-user-valid:before:top-0.5 peer-user-valid:before:w-1.5 peer-user-valid:before:h-2.5 peer-user-valid:before:border-r-[2.5px] peer-user-valid:before:border-b-[2.5px] peer-user-valid:before:border-tlf28-ok peer-user-valid:before:rotate-[42deg] peer-user-invalid:before:left-[9px] peer-user-invalid:before:top-1 peer-user-invalid:before:w-[2.5px] peer-user-invalid:before:h-[13px] peer-user-invalid:before:bg-tlf28-bad peer-user-invalid:before:rotate-45 peer-user-invalid:after:left-[9px] peer-user-invalid:after:top-1 peer-user-invalid:after:w-[2.5px] peer-user-invalid:after:h-[13px] peer-user-invalid:after:bg-tlf28-bad peer-user-invalid:after:-rotate-45"></span>
      </div>
      <div class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-250 has-user-invalid:grid-rows-[1fr] motion-reduce:transition-none"><p id="tlf-28-email-hint" class="overflow-hidden text-xs text-tlf28-bad">Enter a valid email address.</p></div>
    </div>
    <div class="flex flex-col gap-1.5">
      <label for="tlf-28-user" class="text-[13px] font-semibold text-tlf28-label">Username</label>
      <div class="relative">
        <input id="tlf-28-user" type="text" autocomplete="username" placeholder="min 4 characters" required minlength="4" pattern="[a-zA-Z0-9_]+" aria-describedby="tlf-28-user-hint" class="peer w-full h-12 pl-3.5 pr-11 rounded-xl text-[15px] text-tlf28-ink bg-tlf28-field border-[1.5px] border-tlf28-fieldedge transition-[border-color,box-shadow] duration-150 placeholder:text-tlf28-ph focus-visible:outline-none focus-visible:border-tlf28-acc focus-visible:ring-4 focus-visible:ring-tlf28-halo user-valid:border-tlf28-ok user-invalid:border-tlf28-bad">
        <span aria-hidden="true" class="absolute right-3.5 top-1/2 size-5 -translate-y-1/2 scale-40 opacity-0 transition-[opacity,scale] duration-200 peer-user-valid:opacity-100 peer-user-valid:scale-100 peer-user-invalid:opacity-100 peer-user-invalid:scale-100 before:content-[''] before:absolute after:content-[''] after:absolute peer-user-valid:before:left-1.5 peer-user-valid:before:top-0.5 peer-user-valid:before:w-1.5 peer-user-valid:before:h-2.5 peer-user-valid:before:border-r-[2.5px] peer-user-valid:before:border-b-[2.5px] peer-user-valid:before:border-tlf28-ok peer-user-valid:before:rotate-[42deg] peer-user-invalid:before:left-[9px] peer-user-invalid:before:top-1 peer-user-invalid:before:w-[2.5px] peer-user-invalid:before:h-[13px] peer-user-invalid:before:bg-tlf28-bad peer-user-invalid:before:rotate-45 peer-user-invalid:after:left-[9px] peer-user-invalid:after:top-1 peer-user-invalid:after:w-[2.5px] peer-user-invalid:after:h-[13px] peer-user-invalid:after:bg-tlf28-bad peer-user-invalid:after:-rotate-45"></span>
      </div>
      <div class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-250 has-user-invalid:grid-rows-[1fr] motion-reduce:transition-none"><p id="tlf-28-user-hint" class="overflow-hidden text-xs text-tlf28-bad">4+ letters, numbers or underscore.</p></div>
    </div>
    <div class="flex flex-col gap-1.5">
      <label for="tlf-28-pw" class="text-[13px] font-semibold text-tlf28-label">Password</label>
      <div class="relative">
        <input id="tlf-28-pw" type="password" autocomplete="new-password" placeholder="min 8 characters" required minlength="8" aria-describedby="tlf-28-pw-hint" class="peer w-full h-12 pl-3.5 pr-11 rounded-xl text-[15px] text-tlf28-ink bg-tlf28-field border-[1.5px] border-tlf28-fieldedge transition-[border-color,box-shadow] duration-150 placeholder:text-tlf28-ph focus-visible:outline-none focus-visible:border-tlf28-acc focus-visible:ring-4 focus-visible:ring-tlf28-halo user-valid:border-tlf28-ok user-invalid:border-tlf28-bad">
        <span aria-hidden="true" class="absolute right-3.5 top-1/2 size-5 -translate-y-1/2 scale-40 opacity-0 transition-[opacity,scale] duration-200 peer-user-valid:opacity-100 peer-user-valid:scale-100 peer-user-invalid:opacity-100 peer-user-invalid:scale-100 before:content-[''] before:absolute after:content-[''] after:absolute peer-user-valid:before:left-1.5 peer-user-valid:before:top-0.5 peer-user-valid:before:w-1.5 peer-user-valid:before:h-2.5 peer-user-valid:before:border-r-[2.5px] peer-user-valid:before:border-b-[2.5px] peer-user-valid:before:border-tlf28-ok peer-user-valid:before:rotate-[42deg] peer-user-invalid:before:left-[9px] peer-user-invalid:before:top-1 peer-user-invalid:before:w-[2.5px] peer-user-invalid:before:h-[13px] peer-user-invalid:before:bg-tlf28-bad peer-user-invalid:before:rotate-45 peer-user-invalid:after:left-[9px] peer-user-invalid:after:top-1 peer-user-invalid:after:w-[2.5px] peer-user-invalid:after:h-[13px] peer-user-invalid:after:bg-tlf28-bad peer-user-invalid:after:-rotate-45"></span>
      </div>
      <div class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-250 has-user-invalid:grid-rows-[1fr] motion-reduce:transition-none"><p id="tlf-28-pw-hint" class="overflow-hidden text-xs text-tlf28-bad">At least 8 characters.</p></div>
    </div>
    <button type="submit" class="h-12 mt-1 rounded-xl border-0 cursor-pointer bg-tlf28-acc text-white text-[15px] font-semibold transition-[filter,scale] duration-150 hover:brightness-110 active:scale-[0.99] focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tlf28-ring motion-reduce:transition-none motion-reduce:active:scale-100">Sign up</button>
  </form>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tlf28-stage: #eef1f7;
  --color-tlf28-stage: oklch(0.95 0.008 265);
  --color-tlf28-edge: #e5e9f2;
  --color-tlf28-edge: oklch(0.92 0.008 265);
  --color-tlf28-fieldedge: #d8deeb;
  --color-tlf28-fieldedge: oklch(0.88 0.012 265);
  --color-tlf28-field: #fafbfe;
  --color-tlf28-field: oklch(0.99 0.003 265);
  --color-tlf28-ink: #1a2237;
  --color-tlf28-ink: oklch(0.25 0.04 265);
  --color-tlf28-label: #3d465f;
  --color-tlf28-label: oklch(0.37 0.035 265);
  --color-tlf28-ph: #949db5;
  --color-tlf28-ph: oklch(0.67 0.025 265);
  --color-tlf28-acc: #3d5ec6;
  --color-tlf28-acc: oklch(0.5 0.16 262);
  --color-tlf28-halo: #bfcbee;
  --color-tlf28-halo: oklch(0.5 0.16 262 / 0.16);
  --color-tlf28-ring: #94a5e6;
  --color-tlf28-ring: oklch(0.5 0.16 262 / 0.5);
  --color-tlf28-ok: #2b7a52;
  --color-tlf28-ok: oklch(0.5 0.12 155);
  --color-tlf28-bad: #bc3b28;
  --color-tlf28-bad: oklch(0.5 0.18 25);
  --font-tlf28-sans: 'Public Sans', system-ui, sans-serif;
}

.tlf-28 {
  width: 100%;
  min-height: 100svh;
}
```
