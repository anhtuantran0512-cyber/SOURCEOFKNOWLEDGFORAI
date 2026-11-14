---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-login-forms/tailwind-password-strength-meter-data-score/"
title: "Tailwind Password Strength Meter with data-score Variants"
section: "components"
category: "tailwind-css-login-forms"
category_name: "Tailwind CSS Login Forms"
description: "A sign-up password field with a live strength estimate: four segments and a word label that move from red through amber to green as the user types."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Password Strength Meter with data-score Variants
Source: https://codefronts.com/components/tailwind-css-login-forms/tailwind-password-strength-meter-data-score/

A sign-up password field with a live strength estimate: four segments and a word label that move from red through amber to green as the user types. The scoring is the only JavaScript; every colour tier is a group-data-[score=N]: variant, so swapping in zxcvbn later changes one function and no CSS.
## HTML
```html
<section class="tlf-26 w-full min-h-svh grid place-items-center bg-tlf26-stage font-tlf26-sans p-6">
  <form novalidate class="w-[min(400px,100%)] flex flex-col gap-4 p-8 bg-white border border-tlf26-edge rounded-2xl shadow-[0_22px_50px_-38px_oklch(0.25_0.06_265/0.5)]">
    <h1 class="text-[22px] font-bold text-tlf26-ink">Create your password</h1>
    <div class="tlf-26-field group/field flex flex-col gap-2.5" data-score="0">
      <label for="tlf-26-pw" class="text-[13px] font-semibold text-tlf26-label">Password</label>
      <input id="tlf-26-pw" class="tlf-26-pw h-[50px] px-3.5 rounded-xl text-[15px] text-tlf26-ink bg-tlf26-field border-[1.5px] border-tlf26-fieldedge transition-[border-color,box-shadow] duration-150 placeholder:text-tlf26-ph focus-visible:outline-none focus-visible:border-tlf26-acc focus-visible:ring-4 focus-visible:ring-tlf26-halo" type="password" autocomplete="new-password" placeholder="Choose a strong password" required>
      <div aria-hidden="true" class="flex gap-1.5 h-1.5">
        <span class="flex-1 rounded-full bg-tlf26-track transition-colors duration-250 group-data-[score=1]/field:bg-tlf26-s1 group-data-[score=2]/field:bg-tlf26-s2 group-data-[score=3]/field:bg-tlf26-s3 group-data-[score=4]/field:bg-tlf26-s4"></span>
        <span class="flex-1 rounded-full bg-tlf26-track transition-colors duration-250 group-data-[score=2]/field:bg-tlf26-s2 group-data-[score=3]/field:bg-tlf26-s3 group-data-[score=4]/field:bg-tlf26-s4"></span>
        <span class="flex-1 rounded-full bg-tlf26-track transition-colors duration-250 group-data-[score=3]/field:bg-tlf26-s3 group-data-[score=4]/field:bg-tlf26-s4"></span>
        <span class="flex-1 rounded-full bg-tlf26-track transition-colors duration-250 group-data-[score=4]/field:bg-tlf26-s4"></span>
      </div>
      <p class="tlf-26-hint text-[12.5px] text-tlf26-mut transition-colors duration-200 group-data-[score=1]/field:text-tlf26-s1ink group-data-[score=2]/field:text-tlf26-s2ink group-data-[score=3]/field:text-tlf26-s3ink group-data-[score=4]/field:text-tlf26-s4ink" role="status" aria-live="polite">Use 8+ characters with letters, numbers &amp; symbols.</p>
    </div>
    <button type="submit" class="h-[50px] rounded-xl border-0 cursor-pointer bg-tlf26-acc text-white text-[15px] font-semibold transition-[filter,scale] duration-150 hover:brightness-110 active:scale-[0.99] focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tlf26-ring motion-reduce:transition-none motion-reduce:active:scale-100">Create account</button>
  </form>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tlf26-stage: #eef1f7;
  --color-tlf26-stage: oklch(0.95 0.008 260);
  --color-tlf26-edge: #e5e9f2;
  --color-tlf26-edge: oklch(0.92 0.008 260);
  --color-tlf26-fieldedge: #d8deeb;
  --color-tlf26-fieldedge: oklch(0.88 0.012 260);
  --color-tlf26-field: #fafbfe;
  --color-tlf26-field: oklch(0.99 0.003 260);
  --color-tlf26-track: #e2e7f0;
  --color-tlf26-track: oklch(0.92 0.008 260);
  --color-tlf26-ink: #1a2237;
  --color-tlf26-ink: oklch(0.25 0.04 260);
  --color-tlf26-label: #3d465f;
  --color-tlf26-label: oklch(0.37 0.035 260);
  --color-tlf26-mut: #666e88;
  --color-tlf26-mut: oklch(0.52 0.03 260);
  --color-tlf26-ph: #949db5;
  --color-tlf26-ph: oklch(0.67 0.025 260);
  --color-tlf26-acc: #3b63c4;
  --color-tlf26-acc: oklch(0.5 0.16 258);
  --color-tlf26-halo: #bfcdee;
  --color-tlf26-halo: oklch(0.5 0.16 258 / 0.16);
  --color-tlf26-ring: #94a8e6;
  --color-tlf26-ring: oklch(0.5 0.16 258 / 0.5);
  --color-tlf26-s1: #e06a58;
  --color-tlf26-s1: oklch(0.63 0.19 25);
  --color-tlf26-s2: #d79a3c;
  --color-tlf26-s2: oklch(0.72 0.14 65);
  --color-tlf26-s3: #b8b93a;
  --color-tlf26-s3: oklch(0.76 0.13 100);
  --color-tlf26-s4: #4fa878;
  --color-tlf26-s4: oklch(0.66 0.14 155);
  --color-tlf26-s1ink: #b93f2c;
  --color-tlf26-s1ink: oklch(0.5 0.18 25);
  --color-tlf26-s2ink: #8d5c12;
  --color-tlf26-s2ink: oklch(0.5 0.13 65);
  --color-tlf26-s3ink: #6b6c14;
  --color-tlf26-s3ink: oklch(0.48 0.12 100);
  --color-tlf26-s4ink: #257a4c;
  --color-tlf26-s4ink: oklch(0.47 0.12 155);
  --font-tlf26-sans: 'Manrope', system-ui, sans-serif;
}

.tlf-26 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
const section = document.querySelector('.tlf-26');
const field = section.querySelector('.tlf-26-field');
const pw = section.querySelector('.tlf-26-pw');
const hint = section.querySelector('.tlf-26-hint');

const labels = [
  'Use 8+ characters with letters, numbers & symbols.',
  'Very weak password',
  'Weak password',
  'Good password',
  'Strong password'
];

pw.addEventListener('input', () => {
  const v = pw.value;
  let s = 0;
  if (v.length >= 8) s++;
  if (/[A-Z]/.test(v) && /[a-z]/.test(v)) s++;
  if (/[0-9]/.test(v)) s++;
  if (/[^A-Za-z0-9]/.test(v)) s++;
  if (v.length === 0) s = 0; else if (v.length < 6) s = 1;
  field.dataset.score = String(s);
  hint.textContent = labels[s];
});
```
