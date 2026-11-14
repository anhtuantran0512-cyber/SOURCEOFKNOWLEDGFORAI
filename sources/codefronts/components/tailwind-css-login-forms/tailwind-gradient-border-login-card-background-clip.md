---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-login-forms/tailwind-gradient-border-login-card-background-clip/"
title: "Tailwind Gradient Border Login Card with background-clip"
section: "components"
category: "tailwind-css-login-forms"
category_name: "Tailwind CSS Login Forms"
description: "A dark-mode SaaS card wrapped in a fine multi-colour gradient hairline &mdash; one element, no nested wrapper, corners still round."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Gradient Border Login Card with background-clip
Source: https://codefronts.com/components/tailwind-css-login-forms/tailwind-gradient-border-login-card-background-clip/

A dark-mode SaaS card wrapped in a fine multi-colour gradient hairline &mdash; one element, no nested wrapper, corners still round. The whole technique survives the port as a single arbitrary bg-[…] utility holding both background layers and their clips, which is either the best or the worst advertisement for arbitrary values depending on your taste.
## HTML
```html
<section class="tlf-14 w-full min-h-svh grid place-items-center bg-tlf14-stage font-tlf14-sans p-6">
  <form novalidate class="w-[min(380px,100%)] flex flex-col gap-3.5 p-8 rounded-[18px] border-[1.5px] border-transparent text-tlf14-ink bg-[linear-gradient(var(--color-tlf14-card),var(--color-tlf14-card))_padding-box,linear-gradient(135deg,oklch(0.7_0.2_20),oklch(0.7_0.18_300),oklch(0.75_0.16_200))_border-box] shadow-[0_30px_70px_-44px_black]">
    <h1 class="text-[23px] font-bold tracking-tight">Sign in</h1>
    <p class="-mt-2 mb-1 text-[13.5px] text-tlf14-mut">Access your dashboard.</p>
    <label class="flex flex-col gap-1.5"><span class="text-[13px] font-semibold text-tlf14-label">Email</span>
      <input type="email" autocomplete="email" placeholder="[email protected]" required class="h-12 px-3.5 rounded-xl text-[15px] text-tlf14-ink bg-tlf14-field border-[1.5px] border-tlf14-fieldedge transition-[border-color,box-shadow] duration-150 placeholder:text-tlf14-ph focus-visible:outline-none focus-visible:border-tlf14-acc focus-visible:ring-4 focus-visible:ring-tlf14-halo"></label>
    <label class="flex flex-col gap-1.5"><span class="text-[13px] font-semibold text-tlf14-label">Password</span>
      <input type="password" autocomplete="current-password" placeholder="&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;" required class="h-12 px-3.5 rounded-xl text-[15px] text-tlf14-ink bg-tlf14-field border-[1.5px] border-tlf14-fieldedge transition-[border-color,box-shadow] duration-150 placeholder:text-tlf14-ph focus-visible:outline-none focus-visible:border-tlf14-acc focus-visible:ring-4 focus-visible:ring-tlf14-halo"></label>
    <button type="submit" class="mt-1 h-12 rounded-xl border-0 cursor-pointer text-white text-[15px] font-semibold bg-[linear-gradient(135deg,oklch(0.62_0.2_20),oklch(0.58_0.18_300))] transition-[filter,scale] duration-150 hover:brightness-110 active:scale-[0.985] focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-tlf14-ring motion-reduce:transition-none motion-reduce:active:scale-100">Continue</button>
    <p class="text-center text-[13px] text-tlf14-mut">No account? <a href="#" class="font-semibold text-tlf14-link no-underline hover:underline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tlf14-link">Start free</a></p>
  </form>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tlf14-stage: #0b0d13;
  --color-tlf14-stage: oklch(0.15 0.013 270);
  --color-tlf14-card: #151823;
  --color-tlf14-card: oklch(0.2 0.015 270);
  --color-tlf14-field: #101320;
  --color-tlf14-field: oklch(0.18 0.015 270);
  --color-tlf14-fieldedge: #2a2f3d;
  --color-tlf14-fieldedge: oklch(0.3 0.018 270);
  --color-tlf14-ink: #e9ecf5;
  --color-tlf14-ink: oklch(0.94 0.008 270);
  --color-tlf14-label: #c2c8d9;
  --color-tlf14-label: oklch(0.84 0.014 270);
  --color-tlf14-mut: #a0a7bb;
  --color-tlf14-mut: oklch(0.72 0.018 270);
  --color-tlf14-ph: #757d95;
  --color-tlf14-ph: oklch(0.58 0.02 270);
  --color-tlf14-acc: #b37cf0;
  --color-tlf14-acc: oklch(0.7 0.18 300);
  --color-tlf14-halo: #d4bcf6;
  --color-tlf14-halo: oklch(0.7 0.18 300 / 0.22);
  --color-tlf14-ring: #c7a8f4;
  --color-tlf14-ring: oklch(0.7 0.18 300 / 0.6);
  --color-tlf14-link: #f0a68f;
  --color-tlf14-link: oklch(0.78 0.12 30);
  --font-tlf14-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tlf-14 {
  width: 100%;
  min-height: 100svh;
  color-scheme: dark;
}
```
