---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-login-forms/tailwind-accessible-compact-login-modal/"
title: "Tailwind Accessible Compact Login Modal with Scale-In"
section: "components"
category: "tailwind-css-login-forms"
category_name: "Tailwind CSS Login Forms"
description: "A light pop-up auth dialog for media and membership sites: a small centred card scales in over blurred page content."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Accessible Compact Login Modal with Scale-In
Source: https://codefronts.com/components/tailwind-css-login-forms/tailwind-accessible-compact-login-modal/

A light pop-up auth dialog for media and membership sites: a small centred card scales in over blurred page content. Accessibility-first &mdash; real dialog semantics, visible focus on every control, and a closed overlay that cannot intercept clicks. The port also states the pattern's limit honestly: CSS gets you the look, <dialog> gets you focus trapping.
## HTML
```html
<section class="tlf-18 relative w-full min-h-svh overflow-hidden bg-tlf18-stage font-tlf18-sans">
  <input type="checkbox" id="tlf-18-open" checked aria-label="Open login dialog" class="peer sr-only">
  <div class="w-full min-h-svh grid place-items-center gap-4 p-8 text-center">
    <div>
      <p aria-hidden="true" class="text-xs font-semibold uppercase tracking-[0.14em] text-tlf18-mut">Members-only story &middot; 4 min read</p>
      <h1 aria-hidden="true" class="mt-3 mb-5 max-w-[22ch] mx-auto text-[32px]/[1.2] font-semibold text-tlf18-ink font-tlf18-display">The quiet economics of the second-hand book trade</h1>
      <label for="tlf-18-open" class="inline-grid place-items-center min-h-11 px-6 rounded-full cursor-pointer bg-tlf18-acc text-white text-sm font-semibold transition-[filter] duration-150 hover:brightness-110">Log in to read</label>
    </div>
  </div>
  <div class="absolute inset-0 z-5 grid place-items-center p-6 bg-tlf18-scrim opacity-0 pointer-events-none transition-[opacity,backdrop-filter] duration-250 peer-checked:opacity-100 peer-checked:pointer-events-auto peer-checked:backdrop-blur-sm motion-reduce:transition-opacity">
    <label for="tlf-18-open" aria-label="Close dialog" class="absolute inset-0 cursor-pointer"></label>
    <form novalidate role="dialog" aria-modal="true" aria-label="Log in" class="relative w-[min(360px,100%)] flex flex-col gap-3.5 p-8 bg-white rounded-[18px] shadow-[0_30px_70px_-30px_oklch(0.2_0.02_280/0.45)] scale-95 transition-transform duration-250 peer-checked:scale-100 motion-reduce:transition-none">
      <label for="tlf-18-open" aria-label="Close" class="absolute top-2.5 right-2.5 grid place-items-center size-11 rounded-lg cursor-pointer text-2xl leading-none text-tlf18-mut transition-colors duration-150 hover:bg-tlf18-hover hover:text-tlf18-ink">&times;</label>
      <h2 class="text-xl font-semibold text-tlf18-ink font-tlf18-display">Welcome back</h2>
      <p class="-mt-1.5 mb-1 text-[13px] text-tlf18-mut">Members read everything, ad-free.</p>
      <label class="flex flex-col gap-1.5"><span class="text-[13px] font-semibold text-tlf18-label">Email</span>
        <input type="email" autocomplete="email" placeholder="[email protected]" required class="h-12 px-3.5 rounded-xl text-[15px] text-tlf18-ink bg-tlf18-field border-[1.5px] border-tlf18-edge transition-[border-color,box-shadow] duration-150 placeholder:text-tlf18-ph focus-visible:outline-none focus-visible:border-tlf18-acc focus-visible:ring-4 focus-visible:ring-tlf18-halo"></label>
      <label class="flex flex-col gap-1.5"><span class="text-[13px] font-semibold text-tlf18-label">Password</span>
        <input type="password" autocomplete="current-password" placeholder="&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;" required class="h-12 px-3.5 rounded-xl text-[15px] text-tlf18-ink bg-tlf18-field border-[1.5px] border-tlf18-edge transition-[border-color,box-shadow] duration-150 placeholder:text-tlf18-ph focus-visible:outline-none focus-visible:border-tlf18-acc focus-visible:ring-4 focus-visible:ring-tlf18-halo"></label>
      <button type="submit" class="mt-1 h-12 rounded-xl border-0 cursor-pointer bg-tlf18-acc text-white text-[15px] font-semibold transition-[filter,scale] duration-150 hover:brightness-110 active:scale-[0.985] focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tlf18-ring motion-reduce:transition-none motion-reduce:active:scale-100">Log in</button>
    </form>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tlf18-stage: #f7f5f2;
  --color-tlf18-stage: oklch(0.97 0.006 75);
  --color-tlf18-ink: #1f1d1a;
  --color-tlf18-ink: oklch(0.24 0.012 70);
  --color-tlf18-label: #45413c;
  --color-tlf18-label: oklch(0.4 0.014 70);
  --color-tlf18-mut: #6d6862;
  --color-tlf18-mut: oklch(0.54 0.014 70);
  --color-tlf18-ph: #9b958d;
  --color-tlf18-ph: oklch(0.68 0.014 70);
  --color-tlf18-edge: #e2ded8;
  --color-tlf18-edge: oklch(0.9 0.008 70);
  --color-tlf18-field: #fdfcfb;
  --color-tlf18-field: oklch(0.99 0.003 70);
  --color-tlf18-hover: #f1efec;
  --color-tlf18-hover: oklch(0.95 0.006 70);
  --color-tlf18-acc: #9a3412;
  --color-tlf18-acc: oklch(0.45 0.15 40);
  --color-tlf18-halo: #e8c0a8;
  --color-tlf18-halo: oklch(0.45 0.15 40 / 0.18);
  --color-tlf18-ring: #d09272;
  --color-tlf18-ring: oklch(0.45 0.15 40 / 0.5);
  --color-tlf18-scrim: #1f1d1a;
  --color-tlf18-scrim: oklch(0.24 0.012 70 / 0.42);
  --font-tlf18-display: 'Newsreader', Georgia, serif;
  --font-tlf18-sans: 'DM Sans', system-ui, sans-serif;
}

.tlf-18 {
  width: 100%;
  min-height: 100svh;
}
/* Safari < 16.4 backdrop-filter prefix; applied only while the dialog is open. */

.tlf-18 .peer:checked ~ div > div,
.tlf-18 input:checked ~ div[class*="z-5"] {
  -webkit-backdrop-filter: blur(4px);
}
```
