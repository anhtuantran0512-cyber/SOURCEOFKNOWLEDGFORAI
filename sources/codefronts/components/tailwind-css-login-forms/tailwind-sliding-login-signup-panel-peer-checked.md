---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-login-forms/tailwind-sliding-login-signup-panel-peer-checked/"
title: "Tailwind Sliding Login and Sign Up Panel with peer-checked"
section: "components"
category: "tailwind-css-login-forms"
category_name: "Tailwind CSS Login Forms"
description: "One window, two workflows: Login and Sign Up sit side by side and a gradient overlay glides across to reveal whichever you need."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Sliding Login and Sign Up Panel with peer-checked
Source: https://codefronts.com/components/tailwind-css-login-forms/tailwind-sliding-login-signup-panel-peer-checked/

One window, two workflows: Login and Sign Up sit side by side and a gradient overlay glides across to reveal whichever you need. The classic dual-panel auth, driven by a single focusable checkbox &mdash; and the port's win is that the whole state machine is now four peer-checked: class lists instead of six descendant selectors.
## HTML
```html
<section class="tlf-10 w-full min-h-svh grid place-items-center bg-tlf10-stage font-tlf10-sans p-6">
  <div class="relative w-[min(760px,100%)] min-h-[560px] md:min-h-[460px] bg-white rounded-[20px] overflow-hidden shadow-[0_30px_70px_-42px_oklch(0.25_0.06_265/0.55)]">
    <input type="checkbox" id="tlf-10-mode" aria-label="Switch between login and sign up" class="peer sr-only">
    <form novalidate class="absolute top-0 left-0 w-full md:w-1/2 h-full flex flex-col justify-center gap-3 p-8 pb-[150px] md:p-10 md:pb-10 z-2 transition-opacity duration-400 peer-checked:opacity-0 peer-checked:z-1 motion-reduce:transition-none">
      <h2 class="mb-1 text-[23px] font-bold text-tlf10-ink">Sign in</h2>
      <input type="email" placeholder="Email" autocomplete="email" required class="h-12 px-3.5 rounded-xl text-[14.5px] text-tlf10-ink bg-tlf10-field border-[1.5px] border-tlf10-edge transition-[border-color,box-shadow] duration-150 placeholder:text-tlf10-ph focus-visible:outline-none focus-visible:border-tlf10-acc focus-visible:ring-4 focus-visible:ring-tlf10-halo">
      <input type="password" placeholder="Password" autocomplete="current-password" required class="h-12 px-3.5 rounded-xl text-[14.5px] text-tlf10-ink bg-tlf10-field border-[1.5px] border-tlf10-edge transition-[border-color,box-shadow] duration-150 placeholder:text-tlf10-ph focus-visible:outline-none focus-visible:border-tlf10-acc focus-visible:ring-4 focus-visible:ring-tlf10-halo">
      <button type="submit" class="mt-1 h-12 rounded-xl border-0 cursor-pointer bg-tlf10-acc text-white text-[15px] font-semibold transition-[filter,scale] duration-150 hover:brightness-110 active:scale-[0.985] focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tlf10-ring motion-reduce:transition-none motion-reduce:active:scale-100">Log in</button>
    </form>
    <form novalidate class="absolute top-0 right-0 w-full md:w-1/2 h-full flex flex-col justify-center gap-3 p-8 pb-[150px] md:p-10 md:pb-10 opacity-0 z-1 transition-opacity duration-400 peer-checked:opacity-100 peer-checked:z-2 motion-reduce:transition-none">
      <h2 class="mb-1 text-[23px] font-bold text-tlf10-ink">Create account</h2>
      <input type="text" placeholder="Full name" autocomplete="name" required class="h-12 px-3.5 rounded-xl text-[14.5px] text-tlf10-ink bg-tlf10-field border-[1.5px] border-tlf10-edge transition-[border-color,box-shadow] duration-150 placeholder:text-tlf10-ph focus-visible:outline-none focus-visible:border-tlf10-acc focus-visible:ring-4 focus-visible:ring-tlf10-halo">
      <input type="email" placeholder="Email" autocomplete="email" required class="h-12 px-3.5 rounded-xl text-[14.5px] text-tlf10-ink bg-tlf10-field border-[1.5px] border-tlf10-edge transition-[border-color,box-shadow] duration-150 placeholder:text-tlf10-ph focus-visible:outline-none focus-visible:border-tlf10-acc focus-visible:ring-4 focus-visible:ring-tlf10-halo">
      <input type="password" placeholder="Password" autocomplete="new-password" required class="h-12 px-3.5 rounded-xl text-[14.5px] text-tlf10-ink bg-tlf10-field border-[1.5px] border-tlf10-edge transition-[border-color,box-shadow] duration-150 placeholder:text-tlf10-ph focus-visible:outline-none focus-visible:border-tlf10-acc focus-visible:ring-4 focus-visible:ring-tlf10-halo">
      <button type="submit" class="mt-1 h-12 rounded-xl border-0 cursor-pointer bg-tlf10-acc text-white text-[15px] font-semibold transition-[filter,scale] duration-150 hover:brightness-110 active:scale-[0.985] focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tlf10-ring motion-reduce:transition-none motion-reduce:active:scale-100">Sign up</button>
    </form>
    <div class="absolute bottom-0 left-0 w-full h-[150px] md:top-0 md:bottom-auto md:left-auto md:right-0 md:w-1/2 md:h-full z-3 overflow-hidden text-white rounded-t-3xl md:rounded-[120px_20px_20px_120px] bg-[linear-gradient(135deg,oklch(0.55_0.19_264),oklch(0.5_0.2_300))] transition-[translate,border-radius] duration-500 ease-[cubic-bezier(0.4,0,0.2,1)] peer-checked:md:-translate-x-full peer-checked:md:rounded-[20px_120px_120px_20px] peer-focus-visible:outline-3 peer-focus-visible:-outline-offset-4 peer-focus-visible:outline-white peer-checked:[&>div:first-child]:-translate-y-full peer-checked:md:[&>div:first-child]:-translate-x-full peer-checked:md:[&>div:first-child]:translate-y-0 peer-checked:[&>div:last-child]:translate-y-0 peer-checked:md:[&>div:last-child]:translate-x-0 motion-reduce:transition-none">
      <div class="absolute inset-0 flex flex-col items-center justify-center gap-3 p-6 md:p-10 text-center transition-[translate] duration-500 ease-[cubic-bezier(0.4,0,0.2,1)] motion-reduce:transition-none">
        <h3 class="text-xl md:text-2xl font-bold">New here?</h3>
        <p class="hidden md:block max-w-[240px] text-sm/[1.5] text-tlf10-panelink">Create an account and start your free trial.</p>
        <label for="tlf-10-mode" class="grid place-items-center min-h-11 mt-1.5 px-7 rounded-full border-[1.5px] border-white cursor-pointer text-sm font-semibold transition-colors duration-150 hover:bg-white hover:text-tlf10-acc">Sign up</label>
      </div>
      <div class="absolute inset-0 flex flex-col items-center justify-center gap-3 p-6 md:p-10 text-center translate-y-full md:translate-y-0 md:translate-x-full transition-[translate] duration-500 ease-[cubic-bezier(0.4,0,0.2,1)] motion-reduce:transition-none">
        <h3 class="text-xl md:text-2xl font-bold">One of us?</h3>
        <p class="hidden md:block max-w-[240px] text-sm/[1.5] text-tlf10-panelink">Sign in to pick up right where you left off.</p>
        <label for="tlf-10-mode" class="grid place-items-center min-h-11 mt-1.5 px-7 rounded-full border-[1.5px] border-white cursor-pointer text-sm font-semibold transition-colors duration-150 hover:bg-white hover:text-tlf10-acc">Log in</label>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tlf10-stage: #eef0f6;
  --color-tlf10-stage: oklch(0.95 0.008 270);
  --color-tlf10-ink: #161c2e;
  --color-tlf10-ink: oklch(0.23 0.04 270);
  --color-tlf10-ph: #8e96ad;
  --color-tlf10-ph: oklch(0.65 0.025 270);
  --color-tlf10-edge: #d7dbe6;
  --color-tlf10-edge: oklch(0.87 0.01 270);
  --color-tlf10-field: #fafbfe;
  --color-tlf10-field: oklch(0.99 0.003 270);
  --color-tlf10-acc: #5560d4;
  --color-tlf10-acc: oklch(0.55 0.19 264);
  --color-tlf10-halo: #c5caf2;
  --color-tlf10-halo: oklch(0.55 0.19 264 / 0.16);
  --color-tlf10-ring: #9ba3e8;
  --color-tlf10-ring: oklch(0.55 0.19 264 / 0.5);
  --color-tlf10-panelink: #eae6ff;
  --color-tlf10-panelink: oklch(0.93 0.03 290);
  --font-tlf10-sans: 'Outfit', system-ui, sans-serif;
}

.tlf-10 {
  width: 100%;
  min-height: 100svh;
}
```
