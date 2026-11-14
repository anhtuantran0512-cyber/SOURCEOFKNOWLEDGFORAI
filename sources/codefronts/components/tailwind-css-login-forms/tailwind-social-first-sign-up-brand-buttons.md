---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-login-forms/tailwind-social-first-sign-up-brand-buttons/"
title: "Tailwind Social-First Sign Up with Brand-Compliant Buttons"
section: "components"
category: "tailwind-css-login-forms"
category_name: "Tailwind CSS Login Forms"
description: "Consumer-mobile onboarding that leads with big, brand-compliant social blocks &mdash; Apple, Google, Facebook &mdash; stacked full-width for one-tap entry,…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Social-First Sign Up with Brand-Compliant Buttons
Source: https://codefronts.com/components/tailwind-css-login-forms/tailwind-social-first-sign-up-brand-buttons/

Consumer-mobile onboarding that leads with big, brand-compliant social blocks &mdash; Apple, Google, Facebook &mdash; stacked full-width for one-tap entry, with the email path pushed politely below. The port is mostly a lesson in what not to tokenise: provider colours are contractual, so they stay literal hex in the class list.
## HTML
```html
<section class="tlf-16 w-full min-h-svh grid place-items-center bg-tlf16-stage font-tlf16-sans p-6">
  <div class="w-[min(380px,100%)] p-9 text-center bg-white border border-tlf16-edge rounded-[20px] shadow-[0_22px_50px_-38px_oklch(0.25_0.03_280/0.5)]">
    <div aria-hidden="true" class="mb-2 text-[34px] text-tlf16-acc">&#10035;</div>
    <h1 class="text-2xl font-extrabold tracking-tight text-tlf16-ink">Join Frame</h1>
    <p class="mt-1.5 mb-6 text-sm text-tlf16-mut">Create your account in one tap.</p>
    <div class="flex flex-col gap-3">
      <button type="button" class="flex items-center justify-center gap-3 h-13 rounded-xl cursor-pointer border border-transparent bg-black text-white text-[15px] font-semibold transition-[filter,scale] duration-150 hover:brightness-150 active:scale-[0.986] focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tlf16-ring motion-reduce:transition-none motion-reduce:active:scale-100">
        <svg viewBox="0 0 24 24" aria-hidden="true" class="size-5 flex-none"><path fill="currentColor" d="M16.4 12.6c0-2.3 1.9-3.4 2-3.5-1.1-1.6-2.8-1.8-3.4-1.8-1.4-.1-2.8.9-3.5.9s-1.8-.8-3-.8c-1.5 0-3 .9-3.8 2.3-1.6 2.8-.4 7 1.2 9.3.8 1.1 1.7 2.4 2.9 2.3 1.2 0 1.6-.7 3-.7s1.8.7 3 .7 2-1 2.8-2.1c.9-1.3 1.2-2.5 1.3-2.6-.1 0-2.5-1-2.5-3.7zM14.2 5.6c.6-.8 1-1.9.9-3-.9 0-2 .6-2.7 1.4-.6.7-1.1 1.8-.9 2.9 1 0 2-.5 2.7-1.3z"></path></svg>
        Continue with Apple
      </button>
      <button type="button" class="flex items-center justify-center gap-3 h-13 rounded-xl cursor-pointer bg-white border border-tlf16-googleedge text-tlf16-googleink text-[15px] font-semibold transition-[background-color,scale] duration-150 hover:bg-tlf16-hover active:scale-[0.986] focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tlf16-ring motion-reduce:transition-none motion-reduce:active:scale-100">
        <svg viewBox="0 0 24 24" aria-hidden="true" class="size-5 flex-none"><path fill="#4285F4" d="M23 12.3c0-.8-.1-1.6-.2-2.3H12v4.5h6.2a5.3 5.3 0 0 1-2.3 3.5v2.9h3.7C21.8 19 23 15.9 23 12.3z"></path><path fill="#34A853" d="M12 24c3.1 0 5.7-1 7.6-2.8l-3.7-2.9c-1 .7-2.4 1.1-3.9 1.1-3 0-5.5-2-6.4-4.7H1.7v3A12 12 0 0 0 12 24z"></path><path fill="#FBBC05" d="M5.6 14.7a7.2 7.2 0 0 1 0-4.6v-3H1.7a12 12 0 0 0 0 10.6l3.9-3z"></path><path fill="#EA4335" d="M12 4.8c1.7 0 3.2.6 4.4 1.7l3.3-3.3A12 12 0 0 0 1.7 6.4l3.9 3C6.5 6.8 9 4.8 12 4.8z"></path></svg>
        Continue with Google
      </button>
      <button type="button" class="flex items-center justify-center gap-3 h-13 rounded-xl cursor-pointer border border-transparent bg-[#1877F2] text-white text-[15px] font-semibold transition-[filter,scale] duration-150 hover:brightness-105 active:scale-[0.986] focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tlf16-ring motion-reduce:transition-none motion-reduce:active:scale-100">
        <svg viewBox="0 0 24 24" aria-hidden="true" class="size-5 flex-none"><path fill="currentColor" d="M24 12a12 12 0 1 0-13.9 11.9v-8.4H7v-3.5h3.1V9.4c0-3 1.8-4.7 4.5-4.7 1.3 0 2.7.2 2.7.2v3h-1.5c-1.5 0-2 .9-2 1.9v2.2h3.4l-.5 3.5h-2.9v8.4A12 12 0 0 0 24 12z"></path></svg>
        Continue with Facebook
      </button>
    </div>
    <a href="#" class="inline-grid place-items-center min-h-11 mt-4 text-[13.5px] font-medium text-tlf16-mut no-underline hover:text-tlf16-ink hover:underline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tlf16-ring">or sign up with email</a>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tlf16-stage: #f4f4f7;
  --color-tlf16-stage: oklch(0.96 0.004 285);
  --color-tlf16-edge: #eaeaef;
  --color-tlf16-edge: oklch(0.93 0.004 285);
  --color-tlf16-hover: #f6f7fa;
  --color-tlf16-hover: oklch(0.975 0.004 285);
  --color-tlf16-ink: #16171f;
  --color-tlf16-ink: oklch(0.22 0.012 285);
  --color-tlf16-mut: #64667a;
  --color-tlf16-mut: oklch(0.5 0.02 285);
  --color-tlf16-acc: #6a4ee0;
  --color-tlf16-acc: oklch(0.52 0.2 285);
  --color-tlf16-ring: #8f7cf0;
  --color-tlf16-ring: oklch(0.52 0.2 285 / 0.6);
  --color-tlf16-googleedge: #dadce0;
  --color-tlf16-googleink: #3c4043;
  --font-tlf16-sans: 'Manrope', system-ui, sans-serif;
}

.tlf-16 {
  width: 100%;
  min-height: 100svh;
}
```
