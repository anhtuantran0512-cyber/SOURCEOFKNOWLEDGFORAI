---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-login-forms/tailwind-split-screen-brand-hero-login-form/"
title: "Tailwind Split-Screen Brand Hero Login Form"
section: "components"
category: "tailwind-css-login-forms"
category_name: "Tailwind CSS Login Forms"
description: "The high-conversion SaaS classic: a 50/50 desktop split with an isolated minimal form on one side and a branded panel — headline, testimonial, gradient mesh…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Split-Screen Brand Hero Login Form
Source: https://codefronts.com/components/tailwind-css-login-forms/tailwind-split-screen-brand-hero-login-form/

The high-conversion SaaS classic: a 50/50 desktop split with an isolated minimal form on one side and a branded panel — headline, testimonial, gradient mesh — on the other. The port's win is the collapse: grid-cols-1 md:grid-cols-[1.05fr_1fr] replaces a media query with a mobile-first default, so the single-column case is what the markup says by default rather than an override at the bottom of a stylesheet.
## HTML
```html
<section class="tlf-01 w-full min-h-svh grid place-items-center bg-tlf01-stage font-tlf01-sans p-6">
  <div class="w-[min(980px,100%)] grid grid-cols-1 md:grid-cols-[1.05fr_1fr] md:min-h-[580px] bg-white rounded-3xl overflow-hidden shadow-[0_30px_70px_-40px_oklch(0.25_0.06_265/0.5)]">
    <aside aria-hidden="true" class="relative hidden md:flex overflow-hidden bg-tlf01-brand text-white">
      <div class="absolute inset-0 bg-[radial-gradient(60%_55%_at_20%_20%,oklch(0.6_0.2_264/0.55),transparent_60%),radial-gradient(55%_50%_at_85%_30%,oklch(0.62_0.18_200/0.5),transparent_60%),radial-gradient(70%_60%_at_60%_100%,oklch(0.6_0.2_330/0.45),transparent_60%)]"></div>
      <div class="relative flex flex-col justify-between gap-6 p-12">
        <div class="text-xl font-extrabold tracking-tight">&#9670; Northwind</div>
        <p class="text-[27px]/[1.28] font-semibold tracking-tight text-pretty">The workspace where product, design and engineering finally share one source of truth.</p>
        <figure class="flex flex-col gap-3.5">
          <blockquote class="text-[15px]/[1.5] text-tlf01-quote">&ldquo;We cut our release cycle in half the month we switched.&rdquo;</blockquote>
          <figcaption class="flex items-center gap-2.5 text-[13px] text-tlf01-cap">
            <span class="grid place-items-center size-8 rounded-full bg-tlf01-acc text-white text-xs font-bold">AR</span>
            Ana Reyes &middot; VP Eng, Lumen
          </figcaption>
        </figure>
      </div>
    </aside>
    <div class="grid place-items-center p-9 sm:p-12">
      <form novalidate class="w-full max-w-[340px] flex flex-col gap-4">
        <h1 class="text-[28px] font-bold tracking-tight text-tlf01-ink">Welcome back</h1>
        <p class="-mt-2.5 mb-1 text-sm text-tlf01-mut">Sign in to your Northwind workspace.</p>
        <label class="flex flex-col gap-1.5">
          <span class="text-[13px] font-semibold text-tlf01-label">Work email</span>
          <input type="email" name="email" autocomplete="email" placeholder="[email protected]" required class="h-12 px-3.5 rounded-xl bg-tlf01-fieldbg text-[15px] text-tlf01-ink border-[1.5px] border-tlf01-edge transition-[border-color,box-shadow] duration-150 placeholder:text-tlf01-ph focus-visible:outline-none focus-visible:border-tlf01-acc focus-visible:ring-4 focus-visible:ring-tlf01-ring">
        </label>
        <label class="flex flex-col gap-1.5">
          <span class="text-[13px] font-semibold text-tlf01-label">Password</span>
          <input type="password" name="password" autocomplete="current-password" placeholder="&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;" required class="h-12 px-3.5 rounded-xl bg-tlf01-fieldbg text-[15px] text-tlf01-ink border-[1.5px] border-tlf01-edge transition-[border-color,box-shadow] duration-150 placeholder:text-tlf01-ph focus-visible:outline-none focus-visible:border-tlf01-acc focus-visible:ring-4 focus-visible:ring-tlf01-ring">
        </label>
        <button type="submit" class="mt-1 h-12 rounded-xl border-0 cursor-pointer bg-tlf01-acc text-white text-[15px] font-semibold transition-[filter,scale] duration-150 hover:brightness-110 active:scale-[0.985] focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-tlf01-ring motion-reduce:transition-none motion-reduce:active:scale-100">Sign in</button>
        <p class="text-center text-[13.5px] text-tlf01-mut">New here? <a href="#" class="font-semibold text-tlf01-acc no-underline hover:underline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tlf01-acc">Create an account</a></p>
      </form>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tlf01-stage: #eef0f5;
  --color-tlf01-stage: oklch(0.95 0.005 265);
  --color-tlf01-brand: #0e1330;
  --color-tlf01-brand: oklch(0.21 0.06 275);
  --color-tlf01-acc: #5a63d8;
  --color-tlf01-acc: oklch(0.58 0.19 264);
  --color-tlf01-ring: #c9cdf4;
  --color-tlf01-ring: oklch(0.58 0.19 264 / 0.22);
  --color-tlf01-ink: #141a2e;
  --color-tlf01-ink: oklch(0.22 0.04 270);
  --color-tlf01-label: #39405a;
  --color-tlf01-label: oklch(0.36 0.04 270);
  --color-tlf01-mut: #626a85;
  --color-tlf01-mut: oklch(0.5 0.03 270);
  --color-tlf01-ph: #a3aac2;
  --color-tlf01-ph: oklch(0.72 0.03 270);
  --color-tlf01-edge: #d6dae6;
  --color-tlf01-edge: oklch(0.87 0.01 270);
  --color-tlf01-fieldbg: #fbfbfe;
  --color-tlf01-fieldbg: oklch(0.99 0.004 270);
  --color-tlf01-quote: #d7ddf5;
  --color-tlf01-quote: oklch(0.89 0.03 270);
  --color-tlf01-cap: #b6bfe2;
  --color-tlf01-cap: oklch(0.79 0.04 270);
  --font-tlf01-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the stage is sized before the browser build has compiled. */

.tlf-01 {
  width: 100%;
  min-height: 100svh;
}
```
