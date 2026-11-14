---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-login-forms/tailwind-animated-mascot-login-covers-eyes/"
title: "Tailwind Animated Mascot Login that Covers Its Eyes"
section: "components"
category: "tailwind-css-login-forms"
category_name: "Tailwind CSS Login Forms"
description: "A character sits above the form and reacts to the user: eyes glance down at the email field, then hands shoot up to cover them the moment the password field…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Animated Mascot Login that Covers Its Eyes
Source: https://codefronts.com/components/tailwind-css-login-forms/tailwind-animated-mascot-login-covers-eyes/

A character sits above the form and reacts to the user: eyes glance down at the email field, then hands shoot up to cover them the moment the password field is focused. The port is group-has-*'s best demo in the collection &mdash; the CSS original's .card:has(.field--pw:focus-within) .arm becomes a variant on the arm itself.
## HTML
```html
<section class="tlf-17 w-full min-h-svh grid place-items-center bg-tlf17-stage font-tlf17-sans p-6">
  <form novalidate class="group/card relative w-[min(360px,100%)] flex flex-col gap-3.5 pt-16 px-8 pb-8 bg-white border border-tlf17-edge rounded-[20px] shadow-[0_24px_56px_-38px_oklch(0.4_0.08_50/0.5)]">
    <div aria-hidden="true" class="absolute -top-12 left-1/2 -translate-x-1/2 size-24">
      <svg viewBox="0 0 120 120" class="w-full h-full overflow-visible">
        <circle cx="60" cy="60" r="44" class="fill-tlf17-fur"></circle>
        <circle cx="30" cy="26" r="12" class="fill-tlf17-fur2"></circle>
        <circle cx="90" cy="26" r="12" class="fill-tlf17-fur2"></circle>
        <circle cx="46" cy="56" r="7" class="tlf-17-eye fill-tlf17-eye origin-center transition-transform duration-200 group-has-[.tlf-17-email:focus-within]/card:translate-y-[3px] group-has-[.tlf-17-pw:focus-within]/card:scale-y-[0.15] motion-reduce:transition-none"></circle>
        <circle cx="74" cy="56" r="7" class="tlf-17-eye fill-tlf17-eye origin-center transition-transform duration-200 group-has-[.tlf-17-email:focus-within]/card:translate-y-[3px] group-has-[.tlf-17-pw:focus-within]/card:scale-y-[0.15] motion-reduce:transition-none"></circle>
        <ellipse cx="60" cy="72" rx="7" ry="5" class="fill-tlf17-nose"></ellipse>
        <path d="M22 96 q10 -14 26 -8" fill="none" stroke-width="12" stroke-linecap="round" class="stroke-tlf17-fur2 origin-center transition-transform duration-300 ease-[cubic-bezier(0.4,0,0.2,1)] group-has-[.tlf-17-pw:focus-within]/card:[transform:rotate(-62deg)_translate(6px,-30px)] motion-reduce:transition-none"></path>
        <path d="M98 96 q-10 -14 -26 -8" fill="none" stroke-width="12" stroke-linecap="round" class="stroke-tlf17-fur2 origin-center transition-transform duration-300 ease-[cubic-bezier(0.4,0,0.2,1)] group-has-[.tlf-17-pw:focus-within]/card:[transform:rotate(62deg)_translate(-6px,-30px)] motion-reduce:transition-none"></path>
      </svg>
    </div>
    <h1 class="text-center text-[22px] font-bold text-tlf17-ink">Hey there!</h1>
    <label class="tlf-17-email flex flex-col gap-1.5"><span class="text-[13px] font-semibold text-tlf17-label">Email</span>
      <input type="email" autocomplete="email" placeholder="[email protected]" required class="h-12 px-3.5 rounded-xl text-[15px] text-tlf17-ink bg-tlf17-field border-[1.5px] border-tlf17-fieldedge transition-[border-color,box-shadow] duration-150 placeholder:text-tlf17-ph focus-visible:outline-none focus-visible:border-tlf17-acc focus-visible:ring-4 focus-visible:ring-tlf17-halo"></label>
    <label class="tlf-17-pw flex flex-col gap-1.5"><span class="text-[13px] font-semibold text-tlf17-label">Password</span>
      <input type="password" autocomplete="current-password" placeholder="&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;" required class="h-12 px-3.5 rounded-xl text-[15px] text-tlf17-ink bg-tlf17-field border-[1.5px] border-tlf17-fieldedge transition-[border-color,box-shadow] duration-150 placeholder:text-tlf17-ph focus-visible:outline-none focus-visible:border-tlf17-acc focus-visible:ring-4 focus-visible:ring-tlf17-halo"></label>
    <button type="submit" class="mt-1 h-12 rounded-xl border-0 cursor-pointer bg-tlf17-acc text-white text-[15px] font-semibold transition-[filter,scale] duration-150 hover:brightness-110 active:scale-[0.985] focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tlf17-ring motion-reduce:transition-none motion-reduce:active:scale-100">Log in</button>
  </form>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tlf17-stage: #fdf3ea;
  --color-tlf17-stage: oklch(0.97 0.02 65);
  --color-tlf17-edge: #f0e2d5;
  --color-tlf17-edge: oklch(0.93 0.02 65);
  --color-tlf17-fieldedge: #ecd9c7;
  --color-tlf17-fieldedge: oklch(0.9 0.03 65);
  --color-tlf17-field: #fffdfb;
  --color-tlf17-field: oklch(0.995 0.004 65);
  --color-tlf17-ink: #4a2c15;
  --color-tlf17-ink: oklch(0.33 0.06 55);
  --color-tlf17-label: #6d4a2c;
  --color-tlf17-label: oklch(0.44 0.06 55);
  --color-tlf17-ph: #9d7e63;
  --color-tlf17-ph: oklch(0.62 0.05 60);
  --color-tlf17-acc: #c05a1e;
  --color-tlf17-acc: oklch(0.56 0.16 45);
  --color-tlf17-halo: #f0c3a4;
  --color-tlf17-halo: oklch(0.56 0.16 45 / 0.18);
  --color-tlf17-ring: #e39a6d;
  --color-tlf17-ring: oklch(0.56 0.16 45 / 0.5);
  --color-tlf17-fur: #e0a05c;
  --color-tlf17-fur: oklch(0.75 0.13 65);
  --color-tlf17-fur2: #cf8a45;
  --color-tlf17-fur2: oklch(0.68 0.14 60);
  --color-tlf17-eye: #2a1a10;
  --color-tlf17-eye: oklch(0.22 0.04 50);
  --color-tlf17-nose: #3a2418;
  --color-tlf17-nose: oklch(0.28 0.05 50);
  --font-tlf17-sans: 'Baloo 2', system-ui, sans-serif;
}

.tlf-17 {
  width: 100%;
  min-height: 100svh;
}
```
