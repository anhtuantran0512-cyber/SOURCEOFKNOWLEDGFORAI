---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-login-forms/tailwind-slide-over-side-panel-login/"
title: "Tailwind Slide-Over Side Panel Login without JavaScript"
section: "components"
category: "tailwind-css-login-forms"
category_name: "Tailwind CSS Login Forms"
description: "Log in as a slide-over: the panel glides in from the right over a dimmed backdrop without routing away from the storefront &mdash; the e-commerce and…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Slide-Over Side Panel Login without JavaScript
Source: https://codefronts.com/components/tailwind-css-login-forms/tailwind-slide-over-side-panel-login/

Log in as a slide-over: the panel glides in from the right over a dimmed backdrop without routing away from the storefront &mdash; the e-commerce and content-hub pattern. One checkbox, three peer-checked: class lists, zero JavaScript, and the closed state correctly stops intercepting clicks.
## HTML
```html
<section class="tlf-15 relative w-full min-h-svh overflow-hidden bg-tlf15-stage font-tlf15-sans">
  <input type="checkbox" id="tlf-15-open" aria-label="Open sign-in panel" class="peer sr-only">
  <div class="w-full min-h-svh p-7">
    <div class="flex items-center justify-between">
      <span class="text-[17px] font-bold text-tlf15-ink">&#9672; Marketplace</span>
      <label for="tlf-15-open" class="grid place-items-center min-h-11 px-5 rounded-full cursor-pointer bg-tlf15-acc text-white text-sm font-semibold transition-[filter] duration-150 hover:brightness-110">Sign in</label>
    </div>
    <p aria-hidden="true" class="mt-[38vh] text-center text-sm text-tlf15-mut">Your storefront stays put behind the panel.</p>
  </div>
  <label for="tlf-15-open" aria-label="Close sign-in panel" class="absolute inset-0 z-5 cursor-pointer bg-tlf15-scrim opacity-0 pointer-events-none transition-opacity duration-350 peer-checked:opacity-100 peer-checked:pointer-events-auto motion-reduce:transition-none"></label>
  <div role="dialog" aria-label="Sign in" class="absolute top-0 right-0 z-6 h-full w-[min(380px,92%)] p-8 bg-white shadow-[-20px_0_60px_-30px_oklch(0.3_0.05_165/0.55)] translate-x-full transition-transform duration-400 ease-[cubic-bezier(0.4,0,0.2,1)] peer-checked:translate-x-0 peer-focus-visible:outline-3 peer-focus-visible:-outline-offset-4 peer-focus-visible:outline-tlf15-acc motion-reduce:transition-none">
    <label for="tlf-15-open" aria-label="Close" class="absolute top-3 right-3 grid place-items-center size-11 rounded-lg cursor-pointer text-2xl leading-none text-tlf15-mut transition-colors duration-150 hover:bg-tlf15-hover hover:text-tlf15-ink">&times;</label>
    <form novalidate class="mt-8 flex flex-col gap-3.5">
      <h2 class="text-[23px] font-bold text-tlf15-ink">Welcome back</h2>
      <label class="flex flex-col gap-1.5"><span class="text-[13px] font-semibold text-tlf15-label">Email</span>
        <input type="email" autocomplete="email" placeholder="[email protected]" required class="h-12 px-3.5 rounded-xl text-[15px] text-tlf15-ink bg-tlf15-field border-[1.5px] border-tlf15-edge transition-[border-color,box-shadow] duration-150 placeholder:text-tlf15-ph focus-visible:outline-none focus-visible:border-tlf15-acc focus-visible:ring-4 focus-visible:ring-tlf15-halo"></label>
      <label class="flex flex-col gap-1.5"><span class="text-[13px] font-semibold text-tlf15-label">Password</span>
        <input type="password" autocomplete="current-password" placeholder="&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;" required class="h-12 px-3.5 rounded-xl text-[15px] text-tlf15-ink bg-tlf15-field border-[1.5px] border-tlf15-edge transition-[border-color,box-shadow] duration-150 placeholder:text-tlf15-ph focus-visible:outline-none focus-visible:border-tlf15-acc focus-visible:ring-4 focus-visible:ring-tlf15-halo"></label>
      <button type="submit" class="mt-1 h-12 rounded-xl border-0 cursor-pointer bg-tlf15-acc text-white text-[15px] font-semibold transition-[filter,scale] duration-150 hover:brightness-110 active:scale-[0.985] focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tlf15-ring motion-reduce:transition-none motion-reduce:active:scale-100">Sign in</button>
      <p class="text-[12.5px] text-tlf15-mut">Guest checkout is always available.</p>
    </form>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tlf15-stage: #f2f5f3;
  --color-tlf15-stage: oklch(0.96 0.008 165);
  --color-tlf15-ink: #173a2c;
  --color-tlf15-ink: oklch(0.31 0.05 165);
  --color-tlf15-label: #33574a;
  --color-tlf15-label: oklch(0.42 0.04 165);
  --color-tlf15-mut: #5d7a6d;
  --color-tlf15-mut: oklch(0.53 0.03 165);
  --color-tlf15-ph: #8aa79a;
  --color-tlf15-ph: oklch(0.67 0.03 165);
  --color-tlf15-edge: #d3ded7;
  --color-tlf15-edge: oklch(0.88 0.012 165);
  --color-tlf15-field: #fbfdfc;
  --color-tlf15-field: oklch(0.99 0.004 165);
  --color-tlf15-hover: #eef2ef;
  --color-tlf15-hover: oklch(0.95 0.008 165);
  --color-tlf15-acc: #0f7a5a;
  --color-tlf15-acc: oklch(0.5 0.12 165);
  --color-tlf15-halo: #a8d9c7;
  --color-tlf15-halo: oklch(0.5 0.12 165 / 0.18);
  --color-tlf15-ring: #74c2a8;
  --color-tlf15-ring: oklch(0.5 0.12 165 / 0.5);
  --color-tlf15-scrim: #0a1e14;
  --color-tlf15-scrim: oklch(0.2 0.03 165 / 0.45);
  --font-tlf15-sans: 'Be Vietnam Pro', system-ui, sans-serif;
}

.tlf-15 {
  width: 100%;
  min-height: 100svh;
}
```
