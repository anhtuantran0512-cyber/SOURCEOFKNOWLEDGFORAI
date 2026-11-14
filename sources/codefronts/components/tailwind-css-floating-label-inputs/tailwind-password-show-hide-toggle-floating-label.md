---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-floating-label-inputs/tailwind-password-show-hide-toggle-floating-label/"
title: "Tailwind Password Input with Show/Hide Toggle and Floating Label"
section: "components"
category: "tailwind-css-floating-label-inputs"
category_name: "Tailwind CSS Floating Label Inputs"
description: "The login-form workhorse, finished: a floating-label password field with a 44px eye <button> whose icons swap via group-aria-pressed/eye:, plus the strength…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Password Input with Show/Hide Toggle and Floating Label
Source: https://codefronts.com/components/tailwind-css-floating-label-inputs/tailwind-password-show-hide-toggle-floating-label/

The login-form workhorse, finished: a floating-label password field with a 44px eye <button> whose icons swap via group-aria-pressed/eye:, plus the strength meter the CSS original only described — four segments lit by group-data-[strength=N]/pw: variants. The script flips attributes; every visual lives in utilities. The label springs with an overshoot bezier.
## HTML
```html
<section class="tfl-15 w-full min-h-svh grid place-items-center bg-tfl15-bg px-5 py-12 font-tfl15-sans" aria-label="Password floating label with toggle demo">
  <form class="flex w-full max-w-[380px] flex-col gap-6 rounded-3xl bg-white p-8 shadow-[0_24px_60px_-32px_oklch(0.3_0.06_265/0.4)] ring-1 ring-tfl15-ink/5" novalidate>
    <div class="grid gap-1">
      <h3 class="text-2xl font-extrabold tracking-[-0.02em] text-tfl15-ink">Choose a password</h3>
      <p class="text-sm text-tfl15-mut">Use a phrase you'll remember.</p>
    </div>
    <div class="group/pw relative" data-tfl15-field data-strength="0">
      <input class="peer h-14 w-full rounded-xl border-[1.5px] border-tfl15-line bg-white pt-[22px] pr-[58px] pb-1.5 pl-4 text-base text-tfl15-ink outline-hidden transition-[border-color,box-shadow] duration-200 hover:border-tfl15-line-hover focus:border-tfl15-acc focus:ring-4 focus:ring-tfl15-acc/15" type="password" id="tfl-15-pass" name="new-password" placeholder=" " autocomplete="new-password" minlength="8" aria-describedby="tfl-15-hint">
      <label class="pointer-events-none absolute left-4 top-7 origin-left -translate-y-1/2 text-base text-tfl15-mut transition-[translate,scale,color] duration-500 ease-[cubic-bezier(.3,1.8,.4,.9)] peer-focus:translate-y-[calc(-50%_-_13px)] peer-focus:scale-72 peer-focus:text-tfl15-acc peer-[:not(:placeholder-shown)]:translate-y-[calc(-50%_-_13px)] peer-[:not(:placeholder-shown)]:scale-72 motion-reduce:transition-none" for="tfl-15-pass">Password</label>
      <button class="group/eye absolute top-1.5 right-1.5 grid size-11 cursor-pointer place-items-center rounded-[10px] text-tfl15-mut transition-colors duration-150 hover:bg-tfl15-bg hover:text-tfl15-ink focus-visible:outline-3 focus-visible:outline-offset-1 focus-visible:outline-tfl15-acc/50" type="button" data-toggle aria-pressed="false" aria-label="Show password" aria-controls="tfl-15-pass">
        <svg class="col-start-1 row-start-1 transition-opacity duration-150 group-aria-pressed/eye:opacity-0" aria-hidden="true" viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12s3.5-6.5 10-6.5S22 12 22 12s-3.5 6.5-10 6.5S2 12 2 12Z"></path><circle cx="12" cy="12" r="3"></circle></svg>
        <svg class="col-start-1 row-start-1 opacity-0 transition-opacity duration-150 group-aria-pressed/eye:opacity-100" aria-hidden="true" viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12s3.5-6.5 10-6.5S22 12 22 12s-3.5 6.5-10 6.5S2 12 2 12Z"></path><circle cx="12" cy="12" r="3"></circle><path d="m4 4 16 16"></path></svg>
      </button>
      <div class="mt-3 grid grid-cols-4 gap-1.5" aria-hidden="true">
        <span class="h-1 rounded-full bg-tfl15-line transition-colors duration-300 group-data-[strength=1]/pw:bg-tfl15-err group-data-[strength=2]/pw:bg-tfl15-warn group-data-[strength=3]/pw:bg-tfl15-ok group-data-[strength=4]/pw:bg-tfl15-ok"></span>
        <span class="h-1 rounded-full bg-tfl15-line transition-colors duration-300 group-data-[strength=2]/pw:bg-tfl15-warn group-data-[strength=3]/pw:bg-tfl15-ok group-data-[strength=4]/pw:bg-tfl15-ok"></span>
        <span class="h-1 rounded-full bg-tfl15-line transition-colors duration-300 group-data-[strength=3]/pw:bg-tfl15-ok group-data-[strength=4]/pw:bg-tfl15-ok"></span>
        <span class="h-1 rounded-full bg-tfl15-line transition-colors duration-300 group-data-[strength=4]/pw:bg-tfl15-ok"></span>
      </div>
      <p class="mt-2 flex justify-between gap-3 text-[13px] text-tfl15-mut"><span id="tfl-15-hint">At least 8 characters</span><span class="font-semibold group-data-[strength=1]/pw:text-tfl15-err group-data-[strength=2]/pw:text-tfl15-warn-ink group-data-[strength=3]/pw:text-tfl15-ok group-data-[strength=4]/pw:text-tfl15-ok" role="status" aria-live="polite" data-status></span></p>
    </div>
    <button class="min-h-12 cursor-pointer rounded-xl bg-tfl15-acc text-[15px] font-bold text-white shadow-[0_10px_24px_-12px_var(--color-tfl15-acc)] transition-[filter,scale] duration-150 hover:brightness-110 active:scale-98 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tfl15-acc/50" type="button">Create account</button>
  </form>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfl15-bg: #f1f2f7;
  --color-tfl15-bg: oklch(0.96 0.007 270);
  --color-tfl15-ink: #191c2b;
  --color-tfl15-ink: oklch(0.22 0.03 270);
  --color-tfl15-mut: #62677c;
  --color-tfl15-mut: oklch(0.5 0.03 270);
  --color-tfl15-line: #d6d9e4;
  --color-tfl15-line: oklch(0.88 0.015 270);
  --color-tfl15-line-hover: #b4b9cc;
  --color-tfl15-line-hover: oklch(0.78 0.025 270);
  --color-tfl15-acc: #4a50d4;
  --color-tfl15-acc: oklch(0.5 0.2 272);
  --color-tfl15-err: #c8372e;
  --color-tfl15-err: oklch(0.55 0.19 27);
  --color-tfl15-warn: #e0a21a;
  --color-tfl15-warn: oklch(0.76 0.15 78);
  --color-tfl15-warn-ink: #8a5a00;
  --color-tfl15-warn-ink: oklch(0.5 0.11 70);
  --color-tfl15-ok: #1f8a4c;
  --color-tfl15-ok: oklch(0.55 0.14 152);
  --font-tfl15-sans: 'Geist', system-ui, sans-serif;
}

.tfl-15 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const LABELS = ['', 'Weak', 'Fair', 'Good', 'Strong'];
  const score = (v) => !v ? 0 : Math.max(1, [v.length >= 8, /[a-z]/.test(v) && /[A-Z]/.test(v), /\d/.test(v), /[^A-Za-z0-9]/.test(v)].filter(Boolean).length);
  document.querySelectorAll('[data-tfl15-field]').forEach((field) => {
    if (field.dataset.wired) return;
    field.dataset.wired = '1';
    const input = field.querySelector('input');
    const btn = field.querySelector('[data-toggle]');
    const status = field.querySelector('[data-status]');
    btn.addEventListener('click', () => {
      const show = input.type === 'password';
      input.type = show ? 'text' : 'password';
      btn.setAttribute('aria-pressed', String(show));
      btn.setAttribute('aria-label', show ? 'Hide password' : 'Show password');
    });
    input.addEventListener('input', () => {
      const s = score(input.value);
      field.dataset.strength = String(s);
      status.textContent = LABELS[s];
    });
  });
})();
```
