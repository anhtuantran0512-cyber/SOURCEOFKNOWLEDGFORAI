---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-login-forms/tailwind-secure-vault-login-user-invalid-error/"
title: "Tailwind Secure Vault Login with user-invalid Error State"
section: "components"
category: "tailwind-css-login-forms"
category_name: "Tailwind CSS Login Forms"
description: "An ironclad industrial login for banking and secure-storage: flat steel tones, geometric borders, a lock crest and a crimson error state that shakes once…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Secure Vault Login with user-invalid Error State
Source: https://codefronts.com/components/tailwind-css-login-forms/tailwind-secure-vault-login-user-invalid-error/

An ironclad industrial login for banking and secure-storage: flat steel tones, geometric borders, a lock crest and a crimson error state that shakes once when a field is left invalid. The port upgrades the validation itself &mdash; user-invalid: replaces the original's :invalid:not(:focus):not(:placeholder-shown) stack and only fires after the user has actually interacted.
## HTML
```html
<section class="tlf-22 w-full min-h-svh grid place-items-center bg-tlf22-stage font-tlf22-sans p-6">
  <form novalidate class="w-[min(390px,100%)] flex flex-col gap-4 p-8 bg-tlf22-steel border border-tlf22-line rounded-xl shadow-[0_30px_70px_-40px_black,inset_0_1px_0_oklch(1_0_0/0.05)]">
    <div aria-hidden="true" class="grid place-items-center size-13 rounded-[10px] text-2xl bg-tlf22-crest border-2 border-tlf22-line">&#128274;</div>
    <h1 class="text-xl font-bold text-tlf22-ink">Secure Vault Access</h1>
    <p class="-mt-2.5 text-[12.5px] uppercase tracking-[0.06em] text-tlf22-mut">Authorised personnel only.</p>
    <div class="flex flex-col gap-1.5">
      <label for="tlf-22-acct" class="text-xs font-bold uppercase tracking-[0.05em] text-tlf22-label">Account ID</label>
      <input id="tlf-22-acct" type="text" inputmode="numeric" pattern="[0-9]{6,}" placeholder="000000" required class="h-12 px-3.5 rounded-md font-tlf22-mono text-[15px] tracking-[0.08em] text-tlf22-ink bg-tlf22-field border-[1.5px] border-tlf22-line transition-[border-color,box-shadow] duration-150 placeholder:text-tlf22-ph placeholder:tracking-[0.15em] focus-visible:outline-none focus-visible:border-tlf22-acc focus-visible:ring-3 focus-visible:ring-tlf22-halo user-invalid:border-tlf22-danger user-invalid:ring-3 user-invalid:ring-tlf22-dangerhalo user-invalid:animate-tlf22-shake motion-reduce:user-invalid:animate-none">
      <div class="h-0 opacity-0 overflow-hidden transition-opacity duration-200 has-user-invalid:h-auto has-user-invalid:opacity-100"><span role="alert" aria-live="polite" class="text-xs font-semibold text-tlf22-danger">Enter a valid 6+ digit account ID.</span></div>
    </div>
    <div class="flex flex-col gap-1.5">
      <label for="tlf-22-pin" class="text-xs font-bold uppercase tracking-[0.05em] text-tlf22-label">Passphrase</label>
      <input id="tlf-22-pin" type="password" autocomplete="current-password" placeholder="&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;" required minlength="8" class="h-12 px-3.5 rounded-md font-tlf22-mono text-[15px] tracking-[0.08em] text-tlf22-ink bg-tlf22-field border-[1.5px] border-tlf22-line transition-[border-color,box-shadow] duration-150 placeholder:text-tlf22-ph placeholder:tracking-[0.15em] focus-visible:outline-none focus-visible:border-tlf22-acc focus-visible:ring-3 focus-visible:ring-tlf22-halo user-invalid:border-tlf22-danger user-invalid:ring-3 user-invalid:ring-tlf22-dangerhalo user-invalid:animate-tlf22-shake motion-reduce:user-invalid:animate-none">
      <div class="h-0 opacity-0 overflow-hidden transition-opacity duration-200 has-user-invalid:h-auto has-user-invalid:opacity-100"><span role="alert" aria-live="polite" class="text-xs font-semibold text-tlf22-danger">Passphrase must be at least 8 characters.</span></div>
    </div>
    <button type="submit" class="h-12 mt-1 rounded-md cursor-pointer bg-tlf22-btn border border-tlf22-acc text-tlf22-btnink text-sm font-bold uppercase tracking-[0.08em] transition-[background-color,scale] duration-150 hover:bg-tlf22-btnhover active:scale-[0.985] focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tlf22-ring motion-reduce:transition-colors motion-reduce:active:scale-100">Unlock</button>
  </form>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tlf22-stage: #0d1015;
  --color-tlf22-stage: oklch(0.15 0.008 250);
  --color-tlf22-steel: #1c222c;
  --color-tlf22-steel: oklch(0.23 0.012 250);
  --color-tlf22-crest: #141922;
  --color-tlf22-crest: oklch(0.19 0.012 250);
  --color-tlf22-field: #12161e;
  --color-tlf22-field: oklch(0.18 0.012 250);
  --color-tlf22-line: #3a4452;
  --color-tlf22-line: oklch(0.34 0.018 250);
  --color-tlf22-ink: #e8edf3;
  --color-tlf22-ink: oklch(0.94 0.008 250);
  --color-tlf22-label: #a8b3c4;
  --color-tlf22-label: oklch(0.76 0.018 250);
  --color-tlf22-mut: #8e9aab;
  --color-tlf22-mut: oklch(0.67 0.02 250);
  --color-tlf22-ph: #6b7688;
  --color-tlf22-ph: oklch(0.55 0.02 250);
  --color-tlf22-acc: #5ec4e0;
  --color-tlf22-acc: oklch(0.76 0.13 210);
  --color-tlf22-halo: #a6dcec;
  --color-tlf22-halo: oklch(0.76 0.13 210 / 0.25);
  --color-tlf22-ring: #8ed3e7;
  --color-tlf22-ring: oklch(0.76 0.13 210 / 0.55);
  --color-tlf22-btn: #14323d;
  --color-tlf22-btn: oklch(0.76 0.13 210 / 0.16);
  --color-tlf22-btnhover: #1a4453;
  --color-tlf22-btnhover: oklch(0.76 0.13 210 / 0.26);
  --color-tlf22-btnink: #dff2fb;
  --color-tlf22-btnink: oklch(0.95 0.03 210);
  --color-tlf22-danger: #f28b7d;
  --color-tlf22-danger: oklch(0.72 0.16 25);
  --color-tlf22-dangerhalo: #e97a6a;
  --color-tlf22-dangerhalo: oklch(0.72 0.16 25 / 0.22);
  --font-tlf22-sans: 'IBM Plex Sans', system-ui, sans-serif;
  --font-tlf22-mono: 'IBM Plex Mono', ui-monospace, Menlo, monospace;
  --animate-tlf22-shake: tlf-22-shake 0.4s ease-in-out 1;
}

@keyframes tlf-22-shake {
  0%,
    100% {
    transform: translateX(0);
  }

  20% {
    transform: translateX(-6px);
  }

  40% {
    transform: translateX(6px);
  }

  60% {
    transform: translateX(-4px);
  }

  80% {
    transform: translateX(4px);
  }
}

.tlf-22 {
  width: 100%;
  min-height: 100svh;
  color-scheme: dark;
}
```
