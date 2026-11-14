---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-modals/tailwind-login-modal-staggered-blur-in-content-drop/"
title: "Tailwind Login Modal with Staggered Blur-In Content Drop"
section: "components"
category: "tailwind-css-modals"
category_name: "Tailwind CSS Modals"
description: "A SaaS sign-in whose shell appears crisp and whose contents develop like a photograph — brand, title, social row, divider, fields and submit each clearing an…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Login Modal with Staggered Blur-In Content Drop
Source: https://codefronts.com/components/tailwind-css-modals/tailwind-login-modal-staggered-blur-in-content-drop/

A SaaS sign-in whose shell appears crisp and whose contents develop like a photograph — brand, title, social row, divider, fields and submit each clearing an 8px blur on a staggered offset. The port turns the original's eleven nth-child delay rules into one animate-tw02-drop theme utility plus an [animation-delay:…] on each child.
## HTML
```html
<section class="tw-02 w-full min-h-svh grid place-items-center bg-tw02-bg font-tw02-sans px-6 py-10">
  <button type="button" data-tw02-open class="inline-flex items-center justify-center min-h-11 px-6 rounded-[9px] border-0 text-[15px] font-semibold text-white bg-tw02-brand shadow-[0_8px_20px_-6px_var(--color-tw02-glow)] cursor-pointer transition-[translate,box-shadow] duration-200 hover:-translate-y-px hover:shadow-[0_12px_26px_-6px_var(--color-tw02-glow)] focus-visible:outline-2 focus-visible:outline-tw02-brandlt focus-visible:outline-offset-2 motion-reduce:hover:translate-y-0">Sign in</button>

  <dialog id="tw-02-dlg" aria-labelledby="tw-02-title" class="group m-auto w-[min(420px,94vw)] p-0 border border-tw02-line rounded-2xl text-tw02-ink bg-tw02-card shadow-[0_40px_60px_-20px_#000000a0] opacity-0 transition-[opacity,overlay,display] duration-200 transition-discrete open:opacity-100 open:starting:opacity-0 open:backdrop:bg-tw02-scrim open:backdrop:backdrop-blur-[8px]">
    <div class="relative px-8 pt-9 pb-7">
      <button type="button" data-tw02-close aria-label="Close dialog" class="absolute top-3.5 right-3.5 grid place-items-center size-9 rounded-lg border-0 bg-transparent text-tw02-sub text-base cursor-pointer transition-colors duration-200 hover:bg-tw02-hover hover:text-tw02-ink focus-visible:outline-2 focus-visible:outline-tw02-brandlt focus-visible:outline-offset-2">&#10005;</button>

      <div class="inline-flex items-center gap-2 mb-6 text-sm font-bold tracking-wide text-tw02-brandlt opacity-0 blur-[8px] group-open:animate-tw02-drop [animation-delay:150ms] motion-reduce:animate-none motion-reduce:opacity-100 motion-reduce:blur-none">
        <span aria-hidden="true" class="text-sm leading-none">&#9670;</span><span>CodeFronts</span>
      </div>

      <h2 id="tw-02-title" class="mb-1.5 text-[1.6rem] font-extrabold tracking-[-0.02em] leading-tight opacity-0 blur-[8px] group-open:animate-tw02-drop [animation-delay:220ms] motion-reduce:animate-none motion-reduce:opacity-100 motion-reduce:blur-none">Welcome back</h2>
      <p class="mb-6 text-[15px] text-tw02-sub opacity-0 blur-[8px] group-open:animate-tw02-drop [animation-delay:280ms] motion-reduce:animate-none motion-reduce:opacity-100 motion-reduce:blur-none">Sign in to your workspace</p>

      <div class="flex flex-col gap-2 mb-[18px]">
        <button type="button" class="inline-flex items-center justify-center gap-2.5 min-h-11 px-3.5 rounded-[9px] border border-tw02-line bg-tw02-hover text-[15px] font-medium text-tw02-ink cursor-pointer transition-colors duration-200 hover:border-tw02-linehover hover:bg-tw02-hover2 focus-visible:outline-2 focus-visible:outline-tw02-brandlt focus-visible:outline-offset-2 opacity-0 blur-[8px] group-open:animate-tw02-drop [animation-delay:350ms] motion-reduce:animate-none motion-reduce:opacity-100 motion-reduce:blur-none"><span aria-hidden="true" class="grid place-items-center size-5 rounded bg-white text-[0.72rem] font-extrabold text-tw02-bg">G</span>Continue with Google</button>
        <button type="button" class="inline-flex items-center justify-center gap-2.5 min-h-11 px-3.5 rounded-[9px] border border-tw02-line bg-tw02-hover text-[15px] font-medium text-tw02-ink cursor-pointer transition-colors duration-200 hover:border-tw02-linehover hover:bg-tw02-hover2 focus-visible:outline-2 focus-visible:outline-tw02-brandlt focus-visible:outline-offset-2 opacity-0 blur-[8px] group-open:animate-tw02-drop [animation-delay:400ms] motion-reduce:animate-none motion-reduce:opacity-100 motion-reduce:blur-none"><span aria-hidden="true" class="grid place-items-center size-5 rounded bg-tw02-gh text-[0.85rem] font-extrabold text-white">&#9673;</span>Continue with GitHub</button>
        <button type="button" class="inline-flex items-center justify-center gap-2.5 min-h-11 px-3.5 rounded-[9px] border border-tw02-line bg-tw02-hover text-[15px] font-medium text-tw02-ink cursor-pointer transition-colors duration-200 hover:border-tw02-linehover hover:bg-tw02-hover2 focus-visible:outline-2 focus-visible:outline-tw02-brandlt focus-visible:outline-offset-2 opacity-0 blur-[8px] group-open:animate-tw02-drop [animation-delay:450ms] motion-reduce:animate-none motion-reduce:opacity-100 motion-reduce:blur-none"><span aria-hidden="true" class="grid place-items-center size-5 rounded bg-tw02-brand text-[0.72rem] font-extrabold text-white">&#9889;</span>SSO / SAML</button>
      </div>

      <div class="flex items-center gap-3 my-4 text-xs tracking-wide text-tw02-sub opacity-0 blur-[8px] group-open:animate-tw02-drop [animation-delay:550ms] before:content-[''] before:flex-1 before:h-px before:bg-tw02-line after:content-[''] after:flex-1 after:h-px after:bg-tw02-line motion-reduce:animate-none motion-reduce:opacity-100 motion-reduce:blur-none"><span>or continue with email</span></div>

      <form method="dialog" class="flex flex-col gap-3.5 mb-5">
        <label class="flex flex-col gap-1.5 opacity-0 blur-[8px] group-open:animate-tw02-drop [animation-delay:620ms] motion-reduce:animate-none motion-reduce:opacity-100 motion-reduce:blur-none">
          <span class="text-[13px] font-semibold text-tw02-sub">Email</span>
          <input type="email" autofocus required autocomplete="email" placeholder="[email protected]" class="min-h-11 px-3.5 rounded-[9px] border border-tw02-line bg-tw02-hover text-[15px] text-tw02-ink placeholder:text-tw02-sub transition-[border-color,background-color] duration-200 focus:outline-none focus:border-tw02-brandlt focus:bg-tw02-brandwash">
        </label>
        <label class="flex flex-col gap-1.5 opacity-0 blur-[8px] group-open:animate-tw02-drop [animation-delay:680ms] motion-reduce:animate-none motion-reduce:opacity-100 motion-reduce:blur-none">
          <span class="flex items-baseline justify-between text-[13px] font-semibold text-tw02-sub">Password <a href="#" class="text-xs font-medium text-tw02-brandlt no-underline hover:underline">Forgot?</a></span>
          <input type="password" required autocomplete="current-password" spellcheck="false" class="min-h-11 px-3.5 rounded-[9px] border border-tw02-line bg-tw02-hover text-[15px] text-tw02-ink transition-[border-color,background-color] duration-200 focus:outline-none focus:border-tw02-brandlt focus:bg-tw02-brandwash">
        </label>
        <button type="submit" class="min-h-11 px-5 rounded-[9px] border-0 bg-tw02-brand text-[15px] font-semibold text-white shadow-[0_8px_20px_-6px_var(--color-tw02-glow)] cursor-pointer transition-[translate,box-shadow] duration-200 hover:-translate-y-px hover:shadow-[0_12px_26px_-6px_var(--color-tw02-glow)] focus-visible:outline-2 focus-visible:outline-tw02-brandlt focus-visible:outline-offset-2 opacity-0 blur-[8px] group-open:animate-tw02-drop [animation-delay:750ms] motion-reduce:animate-none motion-reduce:opacity-100 motion-reduce:blur-none motion-reduce:hover:translate-y-0">Sign in &rarr;</button>
      </form>

      <p class="pt-4 text-center text-sm text-tw02-sub border-t border-tw02-line opacity-0 blur-[8px] group-open:animate-tw02-drop [animation-delay:820ms] motion-reduce:animate-none motion-reduce:opacity-100 motion-reduce:blur-none">Don't have an account? <a href="#" class="font-semibold text-tw02-brandlt no-underline hover:underline">Sign up</a></p>
    </div>
  </dialog>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tw02-bg: #0a0e1c;
  --color-tw02-bg: oklch(0.16 0.03 267);
  --color-tw02-card: #141a2e;
  --color-tw02-card: oklch(0.22 0.035 267);
  --color-tw02-ink: #f0eeff;
  --color-tw02-ink: oklch(0.94 0.02 290);
  --color-tw02-sub: #9d97c8;
  --color-tw02-sub: oklch(0.71 0.05 290);
  --color-tw02-brand: #7c3aed;
  --color-tw02-brand: oklch(0.54 0.25 296);
  --color-tw02-brandlt: #a78bfa;
  --color-tw02-brandlt: oklch(0.73 0.16 296);
  --color-tw02-brandwash: #7c3aed12;
  --color-tw02-brandwash: oklch(0.54 0.25 296 / 0.08);
  --color-tw02-glow: #7c3aed8c;
  --color-tw02-glow: oklch(0.54 0.25 296 / 0.55);
  --color-tw02-line: #94a3b824;
  --color-tw02-line: oklch(0.7 0.03 255 / 0.16);
  --color-tw02-linehover: #94a3b847;
  --color-tw02-linehover: oklch(0.7 0.03 255 / 0.3);
  --color-tw02-hover: #ffffff08;
  --color-tw02-hover: oklch(1 0 0 / 0.03);
  --color-tw02-hover2: #ffffff10;
  --color-tw02-hover2: oklch(1 0 0 / 0.07);
  --color-tw02-gh: #24292f;
  --color-tw02-gh: oklch(0.28 0.01 265);
  --color-tw02-scrim: #050814b8;
  --color-tw02-scrim: oklch(0.12 0.02 267 / 0.72);
  --font-tw02-sans: 'Outfit', system-ui, sans-serif;
  --animate-tw02-drop: tw02-drop .5s cubic-bezier(.22, 1, .36, 1) both;
}

.tw-02 {
  width: 100%;
}
/* The cascade's keyframes: theme registers the animation, CSS holds the steps. */

@keyframes tw02-drop {
  from {
    opacity: 0;
    filter: blur(8px);
    translate: 0 12px;
  }

  to {
    opacity: 1;
    filter: blur(0);
    translate: 0 0;
  }
}

#tw-02-dlg::backdrop {
  background: oklch(0.12 0.02 267 / 0);
  backdrop-filter: blur(0px);
  transition: background .22s ease, backdrop-filter .22s ease, overlay .22s allow-discrete, display .22s allow-discrete;
}

@starting-style {
  #tw-02-dlg[open]::backdrop {
    background: oklch(0.12 0.02 267 / 0);
    backdrop-filter: blur(0px);
  }
}

@media (prefers-reduced-motion: reduce) {
  #tw-02-dlg::backdrop {
    transition-duration: .001s;
  }
}
```

## JavaScript
```js
(function () {
  var root = document.querySelector('.tw-02');
  var dlg = root.querySelector('#tw-02-dlg');
  var card = dlg.firstElementChild;
  root.querySelector('[data-tw02-open]').addEventListener('click', function () { dlg.showModal(); });
  root.querySelector('[data-tw02-close]').addEventListener('click', function () { dlg.close(); });
  dlg.addEventListener('click', function (e) {
    var r = card.getBoundingClientRect();
    if (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) dlg.close();
  });
})();
```
