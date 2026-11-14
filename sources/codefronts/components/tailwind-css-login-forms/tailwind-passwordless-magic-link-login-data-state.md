---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-login-forms/tailwind-passwordless-magic-link-login-data-state/"
title: "Tailwind Passwordless Magic Link Login with data-state Machine"
section: "components"
category: "tailwind-css-login-forms"
category_name: "Tailwind CSS Login Forms"
description: "The hyper-minimalist single-field entry (Linear / Substack): one email input and a Send magic link button that swaps to a spinner and then a check-your-inbox…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Passwordless Magic Link Login with data-state Machine
Source: https://codefronts.com/components/tailwind-css-login-forms/tailwind-passwordless-magic-link-login-data-state/

The hyper-minimalist single-field entry (Linear / Substack): one email input and a Send magic link button that swaps to a spinner and then a check-your-inbox confirmation, all at a locked height so nothing jumps. The port is the cleanest possible demonstration of group-data-[state=…]: &mdash; nineteen lines of attribute-selector CSS collapse into variants on the three elements that actually change.
## HTML
```html
<section class="tlf-07 w-full min-h-svh grid place-items-center bg-tlf07-stage font-tlf07-sans p-6">
  <form novalidate data-state="idle" class="tlf-07-form group/form relative w-[min(380px,100%)] min-h-[280px] p-8 bg-tlf07-card border border-tlf07-edge rounded-[18px] overflow-hidden shadow-[0_30px_70px_-44px_black]">
    <div class="flex flex-col gap-3.5 transition-[opacity,translate] duration-300 group-data-[state=sent]/form:opacity-0 group-data-[state=sent]/form:-translate-y-2.5 group-data-[state=sent]/form:pointer-events-none motion-reduce:transition-none">
      <h1 class="text-2xl font-bold tracking-tight text-tlf07-ink">Sign in</h1>
      <p class="mb-1 text-sm/[1.5] text-tlf07-mut">We&rsquo;ll email you a magic link &mdash; no password needed.</p>
      <label class="flex flex-col"><span class="sr-only">Email address</span>
        <input type="email" name="email" autocomplete="email" inputmode="email" placeholder="[email protected]" required class="w-full h-[50px] px-4 rounded-xl bg-tlf07-field text-[15px] text-tlf07-ink border-[1.5px] border-tlf07-fieldedge transition-[border-color,box-shadow] duration-150 placeholder:text-tlf07-ph focus-visible:outline-none focus-visible:border-tlf07-acc focus-visible:ring-4 focus-visible:ring-tlf07-halo"></label>
      <button type="submit" class="relative h-[50px] rounded-xl border-0 cursor-pointer overflow-hidden bg-tlf07-acc text-white text-[15px] font-semibold transition-[filter,scale] duration-150 hover:brightness-110 active:scale-[0.985] focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-tlf07-ring group-data-[state=loading]/form:pointer-events-none after:content-[''] after:absolute after:top-1/2 after:left-1/2 after:size-[18px] after:-mt-[9px] after:-ml-[9px] after:rounded-full after:border-[2.5px] after:border-white/40 after:border-t-white after:opacity-0 after:animate-tlf07-spin group-data-[state=loading]/form:after:opacity-100 motion-reduce:transition-none motion-reduce:after:animate-none">
        <span class="transition-opacity duration-150 group-data-[state=loading]/form:opacity-0">Send magic link</span>
      </button>
    </div>
    <div role="status" aria-live="polite" class="absolute inset-x-8 inset-y-8 flex flex-col items-center justify-center gap-3.5 text-center opacity-0 translate-y-2.5 pointer-events-none transition-[opacity,translate] duration-300 group-data-[state=sent]/form:opacity-100 group-data-[state=sent]/form:translate-y-0 group-data-[state=sent]/form:pointer-events-auto motion-reduce:transition-none">
      <span aria-hidden="true" class="relative size-13 rounded-full bg-tlf07-ok after:content-[''] after:absolute after:left-[18px] after:top-[14px] after:w-3 after:h-[22px] after:border-tlf07-okink after:border-[0_3px_3px_0] after:rotate-[42deg]"></span>
      <h2 class="text-xl font-bold text-tlf07-ink">Check your inbox</h2>
      <p class="text-[13.5px]/[1.5] text-tlf07-mut">We sent a link to <b class="tlf-07-addr text-tlf07-strong">[email protected]</b>. It expires in 10 minutes.</p>
    </div>
  </form>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tlf07-stage: #0f1117;
  --color-tlf07-stage: oklch(0.17 0.012 265);
  --color-tlf07-card: #171a23;
  --color-tlf07-card: oklch(0.21 0.014 265);
  --color-tlf07-edge: #262a37;
  --color-tlf07-edge: oklch(0.28 0.016 265);
  --color-tlf07-field: #11141c;
  --color-tlf07-field: oklch(0.18 0.014 265);
  --color-tlf07-fieldedge: #333a4c;
  --color-tlf07-fieldedge: oklch(0.34 0.02 265);
  --color-tlf07-ink: #f2f4fa;
  --color-tlf07-ink: oklch(0.97 0.006 265);
  --color-tlf07-strong: #cdd3e6;
  --color-tlf07-strong: oklch(0.86 0.02 265);
  --color-tlf07-mut: #a4abbf;
  --color-tlf07-mut: oklch(0.74 0.02 265);
  --color-tlf07-ph: #7c849c;
  --color-tlf07-ph: oklch(0.6 0.02 265);
  --color-tlf07-acc: #8a5cf6;
  --color-tlf07-acc: oklch(0.6 0.2 280);
  --color-tlf07-halo: #c3aefb;
  --color-tlf07-halo: oklch(0.6 0.2 280 / 0.22);
  --color-tlf07-ring: #b39cf9;
  --color-tlf07-ring: oklch(0.6 0.2 280 / 0.55);
  --color-tlf07-ok: #56d98c;
  --color-tlf07-ok: oklch(0.78 0.17 155);
  --color-tlf07-okink: #08210f;
  --color-tlf07-okink: oklch(0.2 0.06 150);
  --font-tlf07-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --animate-tlf07-spin: tlf-07-spin 0.7s linear infinite;
}

@keyframes tlf-07-spin {
  to {
    transform: rotate(360deg);
  }
}

.tlf-07 {
  width: 100%;
  min-height: 100svh;
  color-scheme: dark;
}
```

## JavaScript
```js
const form = document.querySelector('.tlf-07-form');
const email = form.querySelector('input[type=email]');
const btn = form.querySelector('button[type=submit]');

function send() {
  if (form.dataset.state !== 'idle') return;
  if (!email.checkValidity()) { email.reportValidity(); return; }
  form.querySelector('.tlf-07-addr').textContent = email.value || '[email protected]';
  form.dataset.state = 'loading';
  setTimeout(() => { form.dataset.state = 'sent'; }, 1400);
}

btn.addEventListener('click', (e) => { e.preventDefault(); send(); });
email.addEventListener('keydown', (e) => { if (e.key === 'Enter') { e.preventDefault(); send(); } });
```
