---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-login-forms/tailwind-animated-conic-gradient-border-login-card/"
title: "Tailwind Animated Conic Gradient Border Login Card"
section: "components"
category: "tailwind-css-login-forms"
category_name: "Tailwind CSS Login Forms"
description: "A glowing conic light rotates continuously around the card's edge &mdash; the fast-moving-tech accent, rendered by animating one registered angle property…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Animated Conic Gradient Border Login Card
Source: https://codefronts.com/components/tailwind-css-login-forms/tailwind-animated-conic-gradient-border-login-card/

A glowing conic light rotates continuously around the card's edge &mdash; the fast-moving-tech accent, rendered by animating one registered angle property rather than repainting a gradient. The @property registration is the part utilities cannot express, which makes this the clearest example in the collection of the CSS that must stay CSS.
## HTML
```html
<section class="tlf-21 w-full min-h-svh grid place-items-center bg-tlf21-stage font-tlf21-sans p-6">
  <div class="tlf-21-ring relative isolate w-[min(380px,100%)] p-0.5 rounded-[20px] before:content-[''] before:absolute before:inset-0 before:-z-1 before:rounded-[inherit] before:bg-[conic-gradient(from_var(--tlf-21-spin),oklch(0.7_0.2_20),oklch(0.72_0.18_300),oklch(0.75_0.16_200),oklch(0.78_0.18_130),oklch(0.7_0.2_20))] before:animate-tlf21-spin after:content-[''] after:absolute after:inset-0 after:-z-2 after:rounded-[inherit] after:opacity-70 after:blur-[16px] after:bg-[conic-gradient(from_var(--tlf-21-spin),oklch(0.7_0.2_20),oklch(0.72_0.18_300),oklch(0.75_0.16_200),oklch(0.78_0.18_130),oklch(0.7_0.2_20))] after:animate-tlf21-spin motion-reduce:before:animate-none motion-reduce:after:animate-none">
    <form novalidate class="relative flex flex-col gap-3.5 p-8 rounded-[18px] bg-tlf21-card text-tlf21-ink">
      <h1 class="text-2xl font-bold tracking-tight">Sign in</h1>
      <p class="-mt-2 mb-1 text-[13.5px] text-tlf21-mut">Ship faster with Comet.</p>
      <label class="flex flex-col gap-1.5"><span class="text-[13px] font-semibold text-tlf21-label">Email</span>
        <input type="email" autocomplete="email" placeholder="[email protected]" required class="h-12 px-3.5 rounded-xl text-[15px] text-tlf21-ink bg-tlf21-field border-[1.5px] border-tlf21-fieldedge transition-[border-color,box-shadow] duration-150 placeholder:text-tlf21-ph focus-visible:outline-none focus-visible:border-tlf21-acc focus-visible:ring-4 focus-visible:ring-tlf21-halo"></label>
      <label class="flex flex-col gap-1.5"><span class="text-[13px] font-semibold text-tlf21-label">Password</span>
        <input type="password" autocomplete="current-password" placeholder="&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;" required class="h-12 px-3.5 rounded-xl text-[15px] text-tlf21-ink bg-tlf21-field border-[1.5px] border-tlf21-fieldedge transition-[border-color,box-shadow] duration-150 placeholder:text-tlf21-ph focus-visible:outline-none focus-visible:border-tlf21-acc focus-visible:ring-4 focus-visible:ring-tlf21-halo"></label>
      <button type="submit" class="mt-1 h-12 rounded-xl border-0 cursor-pointer text-tlf21-btnink text-[15px] font-bold bg-[linear-gradient(90deg,oklch(0.85_0.15_130),oklch(0.85_0.14_200))] transition-[filter,scale] duration-150 hover:brightness-105 active:scale-[0.985] focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-tlf21-ring motion-reduce:transition-none motion-reduce:active:scale-100">Continue</button>
    </form>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@property --tlf-21-spin {
  syntax: '<angle>';
  initial-value: 0deg;
  inherits: false;
}

@theme {
  --color-tlf21-stage: #07080d;
  --color-tlf21-stage: oklch(0.12 0.01 270);
  --color-tlf21-card: #12141d;
  --color-tlf21-card: oklch(0.19 0.014 270);
  --color-tlf21-field: #0e1019;
  --color-tlf21-field: oklch(0.16 0.014 270);
  --color-tlf21-fieldedge: #2a2f3d;
  --color-tlf21-fieldedge: oklch(0.3 0.018 270);
  --color-tlf21-ink: #eceef6;
  --color-tlf21-ink: oklch(0.95 0.006 270);
  --color-tlf21-label: #c2c8d9;
  --color-tlf21-label: oklch(0.84 0.014 270);
  --color-tlf21-mut: #a0a7bb;
  --color-tlf21-mut: oklch(0.72 0.018 270);
  --color-tlf21-ph: #757d95;
  --color-tlf21-ph: oklch(0.58 0.02 270);
  --color-tlf21-acc: #b37cf0;
  --color-tlf21-acc: oklch(0.72 0.18 300);
  --color-tlf21-halo: #d4bcf6;
  --color-tlf21-halo: oklch(0.72 0.18 300 / 0.22);
  --color-tlf21-ring: #b9e88f;
  --color-tlf21-ring: oklch(0.85 0.15 130 / 0.6);
  --color-tlf21-btnink: #0a0b10;
  --color-tlf21-btnink: oklch(0.15 0.01 270);
  --font-tlf21-sans: 'Chivo', system-ui, sans-serif;
  --animate-tlf21-spin: tlf-21-spin 5s linear infinite;
}

@keyframes tlf-21-spin {
  to {
    --tlf-21-spin: 360deg;
  }
}

.tlf-21 {
  width: 100%;
  min-height: 100svh;
  color-scheme: dark;
}
/* No conic-gradient / @property: a static linear ring instead of a flickering one. */

@supports not (background: conic-gradient(from 0deg, red, red)) {
  .tlf-21 .tlf-21-ring::before {
    background: linear-gradient(135deg, oklch(0.7 0.2 20), oklch(0.75 0.16 200));
  }

  .tlf-21 .tlf-21-ring::after {
    display: none;
  }
}
```
