---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-login-forms/tailwind-floating-pill-login-widget/"
title: "Tailwind Floating Pill Login Widget Docked Over App Content"
section: "components"
category: "tailwind-css-login-forms"
category_name: "Tailwind CSS Login Forms"
description: "An ultra-compact login widget that floats above app content like a modular control card &mdash; fully pill-shaped, docked bottom-centre, ideal for mobile web…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Floating Pill Login Widget Docked Over App Content
Source: https://codefronts.com/components/tailwind-css-login-forms/tailwind-floating-pill-login-widget/

An ultra-compact login widget that floats above app content like a modular control card &mdash; fully pill-shaped, docked bottom-centre, ideal for mobile web overlays. The port's practical win is the safe-area dock: bottom-[calc(2rem+env(safe-area-inset-bottom,0px))] is one arbitrary value instead of a variable plus a fallback chain.
## HTML
```html
<section class="tlf-13 relative w-full min-h-svh overflow-hidden grid place-items-center bg-tlf13-stage font-tlf13-sans p-6">
  <div aria-hidden="true" class="absolute inset-0 grid place-items-center text-[38px] font-extrabold tracking-wide text-tlf13-ghost bg-[repeating-linear-gradient(45deg,oklch(0.92_0.02_290)_0_24px,oklch(0.94_0.015_290)_24px_48px)]">your app content</div>
  <form novalidate class="absolute left-1/2 -translate-x-1/2 bottom-[calc(2rem+env(safe-area-inset-bottom,0px))] flex flex-wrap items-center gap-2 w-[min(480px,calc(100%-32px))] p-2 pl-4 max-[520px]:p-3 rounded-full max-[520px]:rounded-[26px] bg-white/85 backdrop-blur-xl border border-white/70 shadow-[0_20px_50px_-18px_oklch(0.3_0.08_300/0.45)]">
    <span aria-hidden="true" class="flex-none text-xl text-tlf13-acc">&#9680;</span>
    <label class="flex-1 min-w-0 max-[520px]:basis-full pr-1.5 border-r border-tlf13-rule max-[520px]:border-r-0 max-[520px]:border-b max-[520px]:border-tlf13-rule max-[520px]:pb-1"><span class="sr-only">Email</span>
      <input type="email" autocomplete="email" placeholder="Email" required class="w-full h-11 px-1.5 rounded-full bg-transparent border-0 text-[14.5px] text-tlf13-ink transition-shadow duration-150 placeholder:text-tlf13-ph focus-visible:outline-none focus-visible:ring-3 focus-visible:ring-tlf13-halo"></label>
    <label class="flex-1 min-w-0 max-[520px]:basis-full"><span class="sr-only">Password</span>
      <input type="password" autocomplete="current-password" placeholder="Password" required class="w-full h-11 px-1.5 rounded-full bg-transparent border-0 text-[14.5px] text-tlf13-ink transition-shadow duration-150 placeholder:text-tlf13-ph focus-visible:outline-none focus-visible:ring-3 focus-visible:ring-tlf13-halo"></label>
    <button type="submit" aria-label="Sign in" class="flex-none grid place-items-center size-11 max-[520px]:ml-auto rounded-full border-0 cursor-pointer bg-tlf13-acc text-white text-[19px] transition-[filter,scale] duration-150 hover:brightness-110 active:scale-95 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tlf13-ring motion-reduce:transition-none motion-reduce:active:scale-100"><span aria-hidden="true">&rarr;</span></button>
  </form>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tlf13-stage: #eceaf5;
  --color-tlf13-stage: oklch(0.93 0.015 290);
  --color-tlf13-ghost: #b8b2cf;
  --color-tlf13-ghost: oklch(0.76 0.03 290);
  --color-tlf13-ink: #241b3a;
  --color-tlf13-ink: oklch(0.26 0.05 295);
  --color-tlf13-ph: #857ca3;
  --color-tlf13-ph: oklch(0.58 0.04 295);
  --color-tlf13-rule: #ddd7ec;
  --color-tlf13-rule: oklch(0.88 0.02 295);
  --color-tlf13-acc: #7a5ae0;
  --color-tlf13-acc: oklch(0.56 0.2 290);
  --color-tlf13-halo: #c4b4f5;
  --color-tlf13-halo: oklch(0.56 0.2 290 / 0.3);
  --color-tlf13-ring: #ac95f0;
  --color-tlf13-ring: oklch(0.56 0.2 290 / 0.55);
  --font-tlf13-sans: 'Figtree', system-ui, sans-serif;
}

.tlf-13 {
  width: 100%;
  min-height: 100svh;
}
/* Safari < 16.4 backdrop-filter prefix. */

.tlf-13 form {
  -webkit-backdrop-filter: blur(24px);
}
```
