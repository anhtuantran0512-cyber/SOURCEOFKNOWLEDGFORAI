---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-login-forms/tailwind-show-hide-password-toggle-aria-pressed/"
title: "Tailwind Show Hide Password Toggle with aria-pressed"
section: "components"
category: "tailwind-css-login-forms"
category_name: "Tailwind CSS Login Forms"
description: "The everyday accessibility win: an eye button inside the password field flips it between hidden and visible so users can catch typos."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Show Hide Password Toggle with aria-pressed
Source: https://codefronts.com/components/tailwind-css-login-forms/tailwind-show-hide-password-toggle-aria-pressed/

The everyday accessibility win: an eye button inside the password field flips it between hidden and visible so users can catch typos. The port's move is styling from the accessibility attribute &mdash; aria-[pressed=true]: draws the strike-through on the eye, so the visual state and the announced state literally cannot diverge.
## HTML
```html
<section class="tlf-24 w-full min-h-svh grid place-items-center bg-tlf24-stage font-tlf24-sans p-6">
  <form novalidate class="w-[min(380px,100%)] flex flex-col gap-3.5 p-8 bg-white border border-tlf24-edge rounded-2xl shadow-[0_22px_50px_-38px_oklch(0.25_0.06_265/0.5)]">
    <h1 class="text-[23px] font-bold text-tlf24-ink">Log in</h1>
    <label class="flex flex-col gap-1.5"><span class="text-[13px] font-semibold text-tlf24-label">Email</span>
      <input type="email" autocomplete="email" placeholder="[email protected]" required class="h-[50px] px-3.5 rounded-xl text-[15px] text-tlf24-ink bg-tlf24-field border-[1.5px] border-tlf24-fieldedge transition-[border-color,box-shadow] duration-150 placeholder:text-tlf24-ph focus-visible:outline-none focus-visible:border-tlf24-acc focus-visible:ring-4 focus-visible:ring-tlf24-halo"></label>
    <div class="flex flex-col gap-1.5">
      <label for="tlf-24-pw" class="text-[13px] font-semibold text-tlf24-label">Password</label>
      <div class="relative">
        <input id="tlf-24-pw" class="tlf-24-pw w-full h-[50px] pl-3.5 pr-14 rounded-xl text-[15px] text-tlf24-ink bg-tlf24-field border-[1.5px] border-tlf24-fieldedge transition-[border-color,box-shadow] duration-150 placeholder:text-tlf24-ph focus-visible:outline-none focus-visible:border-tlf24-acc focus-visible:ring-4 focus-visible:ring-tlf24-halo" type="password" autocomplete="current-password" placeholder="&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;" required>
        <button type="button" aria-pressed="false" aria-label="Show password" class="tlf-24-eye group absolute right-1.5 top-1/2 -translate-y-1/2 grid place-items-center size-11 rounded-[10px] border-0 cursor-pointer bg-transparent text-tlf24-mut transition-colors duration-150 hover:bg-tlf24-stage hover:text-tlf24-acc focus-visible:outline-3 focus-visible:outline-offset-1 focus-visible:outline-tlf24-ring aria-[pressed=true]:text-tlf24-acc">
          <span aria-hidden="true" class="relative block w-[22px] h-3.5 border-2 border-current rounded-[50%/60%] after:content-[''] after:absolute after:left-1/2 after:top-1/2 after:size-1.5 after:-translate-x-1/2 after:-translate-y-1/2 after:rounded-full after:bg-current before:content-[''] before:absolute before:-left-[3px] before:top-[5px] before:w-7 before:h-0.5 before:bg-current before:origin-center before:rotate-[-30deg] before:opacity-0 before:transition-opacity before:duration-150 group-aria-[pressed=true]:before:opacity-100"></span>
        </button>
      </div>
    </div>
    <button type="submit" class="mt-1 h-[50px] rounded-xl border-0 cursor-pointer bg-tlf24-acc text-white text-[15px] font-semibold transition-[filter,scale] duration-150 hover:brightness-110 active:scale-[0.985] focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tlf24-ring motion-reduce:transition-none motion-reduce:active:scale-100">Continue</button>
  </form>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tlf24-stage: #eef1f7;
  --color-tlf24-stage: oklch(0.95 0.008 260);
  --color-tlf24-edge: #e5e9f2;
  --color-tlf24-edge: oklch(0.92 0.008 260);
  --color-tlf24-fieldedge: #d8deeb;
  --color-tlf24-fieldedge: oklch(0.88 0.012 260);
  --color-tlf24-field: #fafbfe;
  --color-tlf24-field: oklch(0.99 0.003 260);
  --color-tlf24-ink: #1a2237;
  --color-tlf24-ink: oklch(0.25 0.04 260);
  --color-tlf24-label: #3d465f;
  --color-tlf24-label: oklch(0.37 0.035 260);
  --color-tlf24-mut: #5f6884;
  --color-tlf24-mut: oklch(0.5 0.03 260);
  --color-tlf24-ph: #949db5;
  --color-tlf24-ph: oklch(0.67 0.025 260);
  --color-tlf24-acc: #3b63c4;
  --color-tlf24-acc: oklch(0.5 0.16 258);
  --color-tlf24-halo: #bfcdee;
  --color-tlf24-halo: oklch(0.5 0.16 258 / 0.16);
  --color-tlf24-ring: #94a8e6;
  --color-tlf24-ring: oklch(0.5 0.16 258 / 0.5);
  --font-tlf24-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.tlf-24 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
const section = document.querySelector('.tlf-24');
const btn = section.querySelector('.tlf-24-eye');
const pw = section.querySelector('.tlf-24-pw');

btn.addEventListener('click', () => {
  const show = pw.type === 'password';
  pw.type = show ? 'text' : 'password';
  btn.setAttribute('aria-pressed', String(show));
  btn.setAttribute('aria-label', show ? 'Hide password' : 'Show password');
  pw.focus();
});
```
