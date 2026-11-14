---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-login-forms/tailwind-minimalist-fintech-login-card-layered-shadow/"
title: "Tailwind Minimalist Fintech Login Card with Layered Shadow"
section: "components"
category: "tailwind-css-login-forms"
category_name: "Tailwind CSS Login Forms"
description: "Crisp, flat, geometric fintech polish: high-contrast type, generous field padding, and the signature two-layer soft shadow that makes a card float just enough."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Minimalist Fintech Login Card with Layered Shadow
Source: https://codefronts.com/components/tailwind-css-login-forms/tailwind-minimalist-fintech-login-card-layered-shadow/

Crisp, flat, geometric fintech polish: high-contrast type, generous field padding, and the signature two-layer soft shadow that makes a card float just enough. The port's interesting move is the divider &mdash; before: and after: flex lines with flex-1 h-px, which is one of the few places two pseudo-element utilities read better than the CSS they replace.
## HTML
```html
<section class="tlf-05 w-full min-h-svh grid place-items-center bg-tlf05-stage font-tlf05-sans p-6">
  <form novalidate class="w-[min(380px,100%)] flex flex-col gap-4 p-8 bg-white rounded-[14px] shadow-[0_8px_24px_oklch(0.25_0.03_265/0.08),0_2px_4px_oklch(0.25_0.03_265/0.04)]">
    <div aria-hidden="true" class="text-[15px] font-extrabold tracking-tight text-tlf05-acc">&#9646; Payflow</div>
    <h1 class="text-xl font-semibold tracking-tight text-tlf05-ink">Sign in to your account</h1>
    <label class="flex flex-col gap-1.5">
      <span class="text-[13px] font-semibold text-tlf05-label">Email</span>
      <input type="email" autocomplete="email" placeholder="[email protected]" required class="h-11 px-3.5 rounded-lg text-[14.5px] text-tlf05-ink border border-tlf05-edge shadow-[0_1px_3px_oklch(0.25_0.03_265/0.1),0_1px_2px_oklch(0.25_0.03_265/0.06)] transition-[border-color,box-shadow] duration-150 placeholder:text-tlf05-ph focus-visible:outline-none focus-visible:border-tlf05-acc focus-visible:ring-3 focus-visible:ring-tlf05-halo">
    </label>
    <label class="flex flex-col gap-1.5">
      <span class="text-[13px] font-semibold text-tlf05-label">Password</span>
      <input type="password" autocomplete="current-password" placeholder="Enter your password" required class="h-11 px-3.5 rounded-lg text-[14.5px] text-tlf05-ink border border-tlf05-edge shadow-[0_1px_3px_oklch(0.25_0.03_265/0.1),0_1px_2px_oklch(0.25_0.03_265/0.06)] transition-[border-color,box-shadow] duration-150 placeholder:text-tlf05-ph focus-visible:outline-none focus-visible:border-tlf05-acc focus-visible:ring-3 focus-visible:ring-tlf05-halo">
    </label>
    <button type="submit" class="h-11 rounded-lg border-0 cursor-pointer bg-tlf05-acc text-white text-[14.5px] font-semibold shadow-[0_1px_3px_oklch(0.25_0.03_265/0.1),0_1px_2px_oklch(0.25_0.03_265/0.06)] transition-[filter,translate] duration-150 hover:brightness-110 active:translate-y-px focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tlf05-ring motion-reduce:transition-none motion-reduce:active:translate-y-0">Continue</button>
    <div class="flex items-center gap-3 text-xs uppercase tracking-[0.06em] text-tlf05-mut before:content-[''] before:flex-1 before:h-px before:bg-tlf05-rule after:content-[''] after:flex-1 after:h-px after:bg-tlf05-rule"><span>or</span></div>
    <button type="button" class="h-11 rounded-lg cursor-pointer bg-white border border-tlf05-edge text-tlf05-ink text-sm font-semibold shadow-[0_1px_3px_oklch(0.25_0.03_265/0.1),0_1px_2px_oklch(0.25_0.03_265/0.06)] transition-colors duration-150 hover:bg-tlf05-stage focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tlf05-ring">Single sign-on (SSO)</button>
    <p class="text-center text-[13px] text-tlf05-mut">Don&rsquo;t have an account? <a href="#" class="font-semibold text-tlf05-acc no-underline hover:underline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tlf05-acc">Sign up</a></p>
  </form>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tlf05-stage: #f6f9fc;
  --color-tlf05-stage: oklch(0.975 0.006 245);
  --color-tlf05-ink: #1a1f36;
  --color-tlf05-ink: oklch(0.25 0.04 270);
  --color-tlf05-label: #3c4257;
  --color-tlf05-label: oklch(0.38 0.03 270);
  --color-tlf05-mut: #5f6b80;
  --color-tlf05-mut: oklch(0.5 0.025 265);
  --color-tlf05-ph: #97a1b5;
  --color-tlf05-ph: oklch(0.68 0.02 265);
  --color-tlf05-edge: #e0e4eb;
  --color-tlf05-edge: oklch(0.91 0.008 265);
  --color-tlf05-rule: #e6e9f0;
  --color-tlf05-rule: oklch(0.93 0.006 265);
  --color-tlf05-acc: #5348d6;
  --color-tlf05-acc: oklch(0.51 0.2 277);
  --color-tlf05-halo: #c4bff2;
  --color-tlf05-halo: oklch(0.51 0.2 277 / 0.22);
  --color-tlf05-ring: #a79ff0;
  --color-tlf05-ring: oklch(0.51 0.2 277 / 0.5);
  --font-tlf05-sans: 'Manrope', ui-sans-serif, system-ui, sans-serif;
}

.tlf-05 {
  width: 100%;
  min-height: 100svh;
}
```
