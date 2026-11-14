---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-login-forms/tailwind-glassmorphism-login-card-backdrop-filter/"
title: "Tailwind Glassmorphism Login Card with backdrop-filter"
section: "components"
category: "tailwind-css-login-forms"
category_name: "Tailwind CSS Login Forms"
description: "The glassmorphism login for high-end creative apps: a frosted translucent card floating over a rich gradient backdrop, with a real blur, a fine light edge…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Glassmorphism Login Card with backdrop-filter
Source: https://codefronts.com/components/tailwind-css-login-forms/tailwind-glassmorphism-login-card-backdrop-filter/

The glassmorphism login for high-end creative apps: a frosted translucent card floating over a rich gradient backdrop, with a real blur, a fine light edge and an inset highlight. The port's honest contribution is the contrast work &mdash; slash-opacity utilities make it trivially easy to see, and fix, exactly how transparent each layer is.
## HTML
```html
<section class="tlf-19 relative w-full min-h-svh grid place-items-center overflow-hidden font-tlf19-sans p-6">
  <div aria-hidden="true" class="absolute inset-0 bg-[radial-gradient(50%_60%_at_20%_25%,oklch(0.72_0.2_20),transparent_60%),radial-gradient(55%_55%_at_80%_20%,oklch(0.7_0.19_300),transparent_60%),radial-gradient(60%_60%_at_60%_90%,oklch(0.72_0.18_210),transparent_60%),linear-gradient(135deg,oklch(0.25_0.09_290),oklch(0.24_0.06_235))]"></div>
  <form novalidate class="tlf-19-glass relative z-1 w-[min(380px,100%)] flex flex-col gap-3.5 p-8 rounded-[22px] text-white bg-white/15 backdrop-blur-[18px] border border-white/30 shadow-[0_30px_70px_-30px_oklch(0_0_0/0.5),inset_0_1px_0_oklch(1_0_0/0.35)]">
    <h1 class="text-[26px] font-bold tracking-tight [text-shadow:0_1px_12px_oklch(0_0_0/0.25)]">Sign in</h1>
    <p class="-mt-2 mb-1 text-sm text-white">Welcome back to Studio.</p>
    <label class="flex flex-col gap-1.5"><span class="text-[13px] font-semibold text-white">Email</span>
      <input type="email" autocomplete="email" placeholder="[email protected]" required class="h-12 px-3.5 rounded-[14px] text-[15px] text-white bg-white/15 border border-white/35 transition-[background-color,border-color,box-shadow] duration-150 placeholder:text-white/70 focus-visible:outline-none focus-visible:border-white focus-visible:bg-white/25 focus-visible:ring-4 focus-visible:ring-white/25"></label>
    <label class="flex flex-col gap-1.5"><span class="text-[13px] font-semibold text-white">Password</span>
      <input type="password" autocomplete="current-password" placeholder="&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;" required class="h-12 px-3.5 rounded-[14px] text-[15px] text-white bg-white/15 border border-white/35 transition-[background-color,border-color,box-shadow] duration-150 placeholder:text-white/70 focus-visible:outline-none focus-visible:border-white focus-visible:bg-white/25 focus-visible:ring-4 focus-visible:ring-white/25"></label>
    <button type="submit" class="mt-1 h-12 rounded-[14px] border-0 cursor-pointer bg-white/95 text-tlf19-ink text-[15px] font-bold transition-[filter,scale] duration-150 hover:brightness-105 active:scale-[0.985] focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-white motion-reduce:transition-none motion-reduce:active:scale-100">Enter studio</button>
    <p class="text-center text-[13px]"><a href="#" class="text-white underline decoration-white/50 underline-offset-2 hover:decoration-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white">Forgot password?</a></p>
  </form>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tlf19-ink: #132038;
  --color-tlf19-ink: oklch(0.25 0.05 260);
  --color-tlf19-acc: #3aa8c8;
  --color-tlf19-acc: oklch(0.72 0.16 210);
  --font-tlf19-sans: 'Urbanist', system-ui, sans-serif;
}

.tlf-19 {
  width: 100%;
  min-height: 100svh;
  color-scheme: dark;
}
/* Safari < 16.4 prefix. */

.tlf-19 .tlf-19-glass {
  -webkit-backdrop-filter: blur(18px);
}
/* No backdrop-filter: raise the fill so the card is a flat translucent panel, not a transparent one. */

@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .tlf-19 .tlf-19-glass {
    background: oklch(0.3 0.04 270 / 0.82);
  }
}
```
