---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-modals/tailwind-password-reset-modal-corner-slide-spin/"
title: "Tailwind Password Reset Modal with Enumeration-Safe Confirmation"
section: "components"
category: "tailwind-css-modals"
category_name: "Tailwind CSS Modals"
description: "The collection's closing bookend: demo 01's corner swing reused on a warmer palette, proving the entrance library travels."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Password Reset Modal with Enumeration-Safe Confirmation
Source: https://codefronts.com/components/tailwind-css-modals/tailwind-password-reset-modal-corner-slide-spin/

The collection's closing bookend: demo 01's corner swing reused on a warmer palette, proving the entrance library travels. The port adds what the original only warned about — a neutral, enumeration-safe confirmation that swaps in place via one data-view attribute and announces itself to screen readers.
## HTML
```html
<section class="tw-18 w-full min-h-svh grid place-items-center bg-tw18-bg font-tw18-sans px-6 py-10">
  <button type="button" data-tw18-open class="inline-flex items-center justify-center min-h-11 px-6 rounded-lg border border-tw18-line bg-tw18-card text-[15px] font-semibold text-tw18-brand cursor-pointer transition-[background-color,border-color] duration-200 hover:bg-tw18-well hover:border-tw18-brand focus-visible:outline-2 focus-visible:outline-tw18-brand focus-visible:outline-offset-2">Forgot password?</button>

  <dialog id="tw-18-dlg" data-view="form" aria-labelledby="tw-18-title" class="group m-auto w-[min(400px,94vw)] p-0 border-0 rounded-[14px] text-center text-tw18-ink bg-tw18-card shadow-[0_30px_60px_-20px_#0f172a47] origin-bottom-right opacity-0 transition-[opacity,translate,rotate,scale,overlay,display] duration-[400ms] ease-[cubic-bezier(.34,1.36,.44,1)] transition-discrete open:opacity-100 open:translate-x-0 open:translate-y-0 open:rotate-0 open:scale-100 open:starting:opacity-0 open:starting:translate-x-6 open:starting:translate-y-8 open:starting:rotate-3 open:starting:scale-[0.96] open:backdrop:bg-tw18-scrim open:backdrop:backdrop-blur-[4px] motion-reduce:transition-[opacity] motion-reduce:duration-150">
    <div class="relative px-[30px] pt-8 pb-6">
      <button type="button" data-tw18-close aria-label="Close dialog" class="absolute top-3.5 right-3.5 grid place-items-center size-9 rounded-lg border-0 bg-transparent text-[15px] text-tw18-sub cursor-pointer transition-colors duration-200 hover:bg-tw18-well hover:text-tw18-ink focus-visible:outline-2 focus-visible:outline-tw18-brand focus-visible:outline-offset-2">&#10005;</button>

      <div class="group-data-[view=sent]:hidden">
        <span aria-hidden="true" class="inline-grid place-items-center size-13 mb-3.5 rounded-full bg-tw18-tint text-2xl text-tw18-brand">&#128273;</span>
        <h2 id="tw-18-title" class="mb-2 text-[1.35rem] font-extrabold tracking-[-0.015em] leading-tight">Reset your password</h2>
        <p class="mb-5 text-sm leading-relaxed text-tw18-sub text-pretty">Enter your email and we'll send a link to reset your password. Link expires in 30 minutes.</p>

        <form data-tw18-form class="flex flex-col gap-3">
          <label class="flex flex-col gap-1.5 text-left">
            <span class="text-xs font-bold uppercase tracking-[0.06em] text-tw18-sub">Email address</span>
            <input type="email" autofocus required autocomplete="email" placeholder="[email protected]" class="min-h-11 px-3.5 rounded-lg border border-tw18-line bg-white text-[15px] text-tw18-ink placeholder:text-tw18-sub transition-[border-color,box-shadow] duration-200 focus:outline-none focus:border-tw18-brand focus:shadow-[0_0_0_3px_var(--color-tw18-ring)] user-invalid:border-tw18-bad">
          </label>
          <button type="submit" class="min-h-11 mt-1 px-5 rounded-lg border-0 bg-tw18-brand text-[15px] font-bold text-white shadow-[0_8px_18px_-6px_var(--color-tw18-glow)] cursor-pointer transition-[background-color,translate] duration-200 hover:bg-tw18-branddark hover:-translate-y-px focus-visible:outline-2 focus-visible:outline-tw18-brand focus-visible:outline-offset-[3px] motion-reduce:hover:translate-y-0">Send reset link &rarr;</button>
        </form>
      </div>

      <div hidden class="group-data-[view=sent]:block">
        <span aria-hidden="true" class="inline-grid place-items-center size-13 mb-3.5 rounded-full bg-tw18-goodtint text-2xl text-tw18-good">&#9993;</span>
        <h3 class="mb-2 text-[1.35rem] font-extrabold tracking-[-0.015em] leading-tight">Check your inbox</h3>
        <p aria-live="polite" class="mb-5 text-sm leading-relaxed text-tw18-sub text-pretty">If an account exists for that address, a reset link is on its way. It expires in 30 minutes.</p>
        <button type="button" data-tw18-ack data-tw18-close class="w-full min-h-11 px-5 rounded-lg border-0 bg-tw18-brand text-[15px] font-bold text-white cursor-pointer transition-colors duration-200 hover:bg-tw18-branddark focus-visible:outline-2 focus-visible:outline-tw18-brand focus-visible:outline-offset-[3px]">Got it</button>
      </div>

      <div class="pt-4 mt-4 border-t border-tw18-line">
        <button type="button" data-tw18-close class="min-h-11 px-3 bg-transparent border-0 text-sm font-semibold text-tw18-brand cursor-pointer hover:underline focus-visible:outline-2 focus-visible:outline-tw18-brand focus-visible:outline-offset-2">&larr; Return to sign in</button>
        <p class="text-xs text-tw18-sub">Can't access this email? <a href="#" class="font-semibold text-tw18-brand underline">Contact support</a></p>
      </div>
    </div>
  </dialog>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tw18-bg: #f8fafc;
  --color-tw18-bg: oklch(0.98 0.005 250);
  --color-tw18-card: #ffffff;
  --color-tw18-card: oklch(1 0 0);
  --color-tw18-well: #f1f5f9;
  --color-tw18-well: oklch(0.96 0.006 250);
  --color-tw18-ink: #0f172a;
  --color-tw18-ink: oklch(0.23 0.04 265);
  --color-tw18-sub: #52627a;
  --color-tw18-sub: oklch(0.48 0.03 255);
  --color-tw18-line: #e2e8f0;
  --color-tw18-line: oklch(0.92 0.01 250);
  --color-tw18-brand: #2563eb;
  --color-tw18-brand: oklch(0.53 0.2 262);
  --color-tw18-branddark: #1d4ed8;
  --color-tw18-branddark: oklch(0.48 0.2 262);
  --color-tw18-tint: #3b82f61f;
  --color-tw18-tint: oklch(0.62 0.19 259 / 0.12);
  --color-tw18-ring: #3b82f626;
  --color-tw18-ring: oklch(0.62 0.19 259 / 0.15);
  --color-tw18-glow: #3b82f680;
  --color-tw18-glow: oklch(0.62 0.19 259 / 0.5);
  --color-tw18-good: #047857;
  --color-tw18-good: oklch(0.52 0.12 164);
  --color-tw18-goodtint: #0478571f;
  --color-tw18-goodtint: oklch(0.52 0.12 164 / 0.12);
  --color-tw18-bad: #c81e1e;
  --color-tw18-bad: oklch(0.53 0.2 27);
  --color-tw18-scrim: #0f172a8c;
  --color-tw18-scrim: oklch(0.23 0.04 265 / 0.55);
  --font-tw18-sans: 'Outfit', system-ui, sans-serif;
}

.tw-18 {
  width: 100%;
}

#tw-18-dlg::backdrop {
  background: oklch(0.23 0.04 265 / 0);
  backdrop-filter: blur(0px);
  transition: background .25s ease, backdrop-filter .25s ease, overlay .25s allow-discrete, display .25s allow-discrete;
}

@starting-style {
  #tw-18-dlg[open]::backdrop {
    background: oklch(0.23 0.04 265 / 0);
    backdrop-filter: blur(0px);
  }
}

@media (prefers-reduced-motion: reduce) {
  #tw-18-dlg::backdrop {
    transition-duration: .001s;
  }
}
```

## JavaScript
```js
(function () {
  var root = document.querySelector('.tw-18');
  var dlg = root.querySelector('#tw-18-dlg');
  var card = dlg.firstElementChild;
  var form = root.querySelector('[data-tw18-form]');
  var ack = root.querySelector('[data-tw18-ack]');

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    // Same response either way: never reveal whether the address is registered.
    dlg.dataset.view = 'sent';
    ack.focus();
  });
  dlg.addEventListener('close', function () { dlg.dataset.view = 'form'; form.reset(); });

  root.querySelector('[data-tw18-open]').addEventListener('click', function () { dlg.showModal(); });
  root.querySelectorAll('[data-tw18-close]').forEach(function (b) {
    b.addEventListener('click', function () { dlg.close(); });
  });
  dlg.addEventListener('click', function (e) {
    var r = card.getBoundingClientRect();
    if (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) dlg.close();
  });
})();
```
