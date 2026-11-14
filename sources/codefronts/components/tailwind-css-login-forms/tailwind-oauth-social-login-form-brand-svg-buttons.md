---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-login-forms/tailwind-oauth-social-login-form-brand-svg-buttons/"
title: "Tailwind OAuth Social Login Form with Brand SVG Buttons"
section: "components"
category: "tailwind-css-login-forms"
category_name: "Tailwind CSS Login Forms"
description: "OAuth-first done right: prominent Google and GitHub buttons up top with crisp inline brand SVGs, an &ldquo;or continue with email&rdquo; divider, and the…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind OAuth Social Login Form with Brand SVG Buttons
Source: https://codefronts.com/components/tailwind-css-login-forms/tailwind-oauth-social-login-form-brand-svg-buttons/

OAuth-first done right: prominent Google and GitHub buttons up top with crisp inline brand SVGs, an &ldquo;or continue with email&rdquo; divider, and the email path tucked neatly beneath for those who want it. The port's quiet upgrade is sr-only &mdash; the CSS original hand-rolled a clip:rect(0 0 0 0) visually-hidden class, and Tailwind ships the modern, correct version as one utility.
## HTML
```html
<section class="tlf-06 w-full min-h-svh grid place-items-center bg-tlf06-stage font-tlf06-sans p-6">
  <form novalidate class="w-[min(380px,100%)] flex flex-col gap-3 p-8 bg-white border border-tlf06-edge rounded-2xl shadow-[0_22px_50px_-38px_oklch(0.25_0.06_265/0.5)]">
    <h1 class="mb-1.5 text-center text-[22px] font-bold tracking-tight text-tlf06-ink">Log in to Orbit</h1>
    <button type="button" class="flex items-center justify-center gap-3 h-12 rounded-xl cursor-pointer bg-white border-[1.5px] border-tlf06-edge text-tlf06-ink text-[14.5px] font-semibold transition-[background-color,border-color,translate] duration-150 hover:bg-tlf06-hover hover:border-tlf06-edgehover hover:-translate-y-px active:translate-y-0 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tlf06-ring motion-reduce:transition-colors motion-reduce:hover:translate-y-0">
      <svg viewBox="0 0 24 24" aria-hidden="true" class="size-5 flex-none"><path fill="#4285F4" d="M23 12.3c0-.8-.1-1.6-.2-2.3H12v4.5h6.2a5.3 5.3 0 0 1-2.3 3.5v2.9h3.7C21.8 19 23 15.9 23 12.3z"></path><path fill="#34A853" d="M12 24c3.1 0 5.7-1 7.6-2.8l-3.7-2.9c-1 .7-2.4 1.1-3.9 1.1-3 0-5.5-2-6.4-4.7H1.7v3A12 12 0 0 0 12 24z"></path><path fill="#FBBC05" d="M5.6 14.7a7.2 7.2 0 0 1 0-4.6v-3H1.7a12 12 0 0 0 0 10.6l3.9-3z"></path><path fill="#EA4335" d="M12 4.8c1.7 0 3.2.6 4.4 1.7l3.3-3.3A12 12 0 0 0 1.7 6.4l3.9 3C6.5 6.8 9 4.8 12 4.8z"></path></svg>
      Continue with Google
    </button>
    <button type="button" class="flex items-center justify-center gap-3 h-12 rounded-xl cursor-pointer bg-white border-[1.5px] border-tlf06-edge text-tlf06-ink text-[14.5px] font-semibold transition-[background-color,border-color,translate] duration-150 hover:bg-tlf06-hover hover:border-tlf06-edgehover hover:-translate-y-px active:translate-y-0 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tlf06-ring motion-reduce:transition-colors motion-reduce:hover:translate-y-0">
      <svg viewBox="0 0 24 24" aria-hidden="true" class="size-5 flex-none"><path fill="#181717" d="M12 .5A12 12 0 0 0 8.2 23.9c.6.1.8-.3.8-.6v-2c-3.3.7-4-1.6-4-1.6-.6-1.4-1.3-1.8-1.3-1.8-1.1-.7 0-.7 0-.7 1.2.1 1.8 1.2 1.8 1.2 1 1.8 2.8 1.3 3.5 1 .1-.8.4-1.3.7-1.6-2.7-.3-5.5-1.3-5.5-5.9 0-1.3.5-2.4 1.2-3.2 0-.4-.5-1.6.2-3.2 0 0 1-.3 3.3 1.2a11.5 11.5 0 0 1 6 0C17.3 5 18.3 5.3 18.3 5.3c.7 1.6.2 2.8.1 3.2.8.8 1.2 1.9 1.2 3.2 0 4.6-2.8 5.6-5.5 5.9.4.4.8 1.1.8 2.2v3.3c0 .3.2.7.8.6A12 12 0 0 0 12 .5z"></path></svg>
      Continue with GitHub
    </button>
    <div class="flex items-center gap-3 my-1 text-xs text-tlf06-mut before:content-[''] before:flex-1 before:h-px before:bg-tlf06-edge after:content-[''] after:flex-1 after:h-px after:bg-tlf06-edge"><span>or continue with email</span></div>
    <label class="flex flex-col"><span class="sr-only">Email</span>
      <input type="email" autocomplete="email" placeholder="[email protected]" required class="w-full h-12 px-3.5 rounded-xl bg-tlf06-fieldbg text-[14.5px] text-tlf06-ink border-[1.5px] border-tlf06-edge transition-[border-color,box-shadow] duration-150 placeholder:text-tlf06-ph focus-visible:outline-none focus-visible:border-tlf06-acc focus-visible:ring-4 focus-visible:ring-tlf06-halo"></label>
    <label class="flex flex-col"><span class="sr-only">Password</span>
      <input type="password" autocomplete="current-password" placeholder="Password" required class="w-full h-12 px-3.5 rounded-xl bg-tlf06-fieldbg text-[14.5px] text-tlf06-ink border-[1.5px] border-tlf06-edge transition-[border-color,box-shadow] duration-150 placeholder:text-tlf06-ph focus-visible:outline-none focus-visible:border-tlf06-acc focus-visible:ring-4 focus-visible:ring-tlf06-halo"></label>
    <button type="submit" class="mt-1 h-12 rounded-xl border-0 cursor-pointer bg-tlf06-acc text-white text-[15px] font-semibold transition-[filter,scale] duration-150 hover:brightness-110 active:scale-[0.985] focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tlf06-ring motion-reduce:transition-none motion-reduce:active:scale-100">Log in</button>
  </form>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tlf06-stage: #f4f5f9;
  --color-tlf06-stage: oklch(0.96 0.005 270);
  --color-tlf06-edge: #dde1ec;
  --color-tlf06-edge: oklch(0.89 0.01 270);
  --color-tlf06-edgehover: #c6ccdd;
  --color-tlf06-edgehover: oklch(0.83 0.016 270);
  --color-tlf06-hover: #f7f8fc;
  --color-tlf06-hover: oklch(0.98 0.004 270);
  --color-tlf06-fieldbg: #fbfbfe;
  --color-tlf06-fieldbg: oklch(0.99 0.004 270);
  --color-tlf06-ink: #161c2e;
  --color-tlf06-ink: oklch(0.23 0.04 270);
  --color-tlf06-mut: #646b84;
  --color-tlf06-mut: oklch(0.51 0.03 270);
  --color-tlf06-ph: #98a0b6;
  --color-tlf06-ph: oklch(0.68 0.025 270);
  --color-tlf06-acc: #4353c4;
  --color-tlf06-acc: oklch(0.5 0.16 265);
  --color-tlf06-halo: #c2c8ee;
  --color-tlf06-halo: oklch(0.5 0.16 265 / 0.16);
  --color-tlf06-ring: #9aa4e4;
  --color-tlf06-ring: oklch(0.5 0.16 265 / 0.45);
  --font-tlf06-sans: 'DM Sans', system-ui, sans-serif;
}

.tlf-06 {
  width: 100%;
  min-height: 100svh;
}
```
