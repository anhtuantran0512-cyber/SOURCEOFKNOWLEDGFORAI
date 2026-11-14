---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-modals/tailwind-signup-modal-origami-fan-deploy-3d-panels/"
title: "Tailwind Signup Modal with 3D Origami Fan Deploy Panels"
section: "components"
category: "tailwind-css-modals"
category_name: "Tailwind CSS Modals"
description: "A registration card whose three horizontal panels — header, form, benefits strip — fan down like origami, each starting folded back on the X axis."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Signup Modal with 3D Origami Fan Deploy Panels
Source: https://codefronts.com/components/tailwind-css-modals/tailwind-signup-modal-origami-fan-deploy-3d-panels/

A registration card whose three horizontal panels — header, form, benefits strip — fan down like origami, each starting folded back on the X axis. The port uses v4's perspective-*, transform-3d and backface-hidden utilities for the 3D stage and one animate-tw03-fold theme animation with three [animation-delay:…] offsets.
## HTML
```html
<section class="tw-03 w-full min-h-svh grid place-items-center bg-tw03-bg font-tw03-sans px-6 py-10">
  <button type="button" data-tw03-open class="inline-flex items-center justify-center min-h-11 px-6 rounded-[9px] border-0 text-[15px] font-semibold text-white bg-tw03-good shadow-[0_8px_20px_-6px_var(--color-tw03-glow)] cursor-pointer transition-[background-color,translate] duration-200 hover:bg-tw03-goodhover hover:-translate-y-px focus-visible:outline-2 focus-visible:outline-tw03-good focus-visible:outline-offset-2 motion-reduce:hover:translate-y-0">Create account</button>

  <dialog id="tw-03-dlg" aria-labelledby="tw-03-title" class="group m-auto w-[min(460px,94vw)] p-0 border-0 bg-transparent perspective-[1400px] opacity-0 transition-[opacity,overlay,display] duration-200 transition-discrete open:opacity-100 open:starting:opacity-0 open:backdrop:bg-tw03-scrim open:backdrop:backdrop-blur-[6px]">
    <div class="relative rounded-[14px] overflow-hidden bg-tw03-card text-tw03-ink shadow-[0_40px_60px_-20px_#00000059] transform-3d">
      <button type="button" data-tw03-close aria-label="Close dialog" class="absolute top-3.5 right-3.5 z-10 grid place-items-center size-9 rounded-lg border-0 bg-transparent text-tw03-sub text-base cursor-pointer transition-colors duration-200 hover:bg-tw03-well hover:text-tw03-ink focus-visible:outline-2 focus-visible:outline-tw03-good focus-visible:outline-offset-2">&#10005;</button>

      <div class="px-8 pt-8 pb-5 opacity-0 rotate-x-[-90deg] origin-top backface-hidden group-open:animate-tw03-fold [animation-delay:150ms] motion-reduce:animate-none motion-reduce:opacity-100 motion-reduce:rotate-x-0">
        <h2 id="tw-03-title" class="mb-1.5 text-[1.55rem] font-extrabold tracking-[-0.02em] leading-tight">Create your free account</h2>
        <p class="text-sm text-tw03-sub">Start your 14-day trial · No credit card required</p>
      </div>

      <div class="px-8 pb-5 opacity-0 rotate-x-[-90deg] origin-top backface-hidden group-open:animate-tw03-fold [animation-delay:350ms] motion-reduce:animate-none motion-reduce:opacity-100 motion-reduce:rotate-x-0">
        <form method="dialog" class="flex flex-col gap-3.5">
          <label class="flex flex-col gap-1.5">
            <span class="text-[13px] font-semibold text-tw03-sub">How should we call you?</span>
            <input type="text" autofocus required autocomplete="given-name" placeholder="Alex" class="min-h-11 px-3.5 rounded-[9px] border border-tw03-line bg-tw03-well text-[15px] text-tw03-ink placeholder:text-tw03-sub transition-[border-color,background-color] duration-200 focus:outline-none focus:border-tw03-good focus:bg-white">
          </label>
          <label class="flex flex-col gap-1.5">
            <span class="text-[13px] font-semibold text-tw03-sub">Email</span>
            <input type="email" required autocomplete="email" placeholder="[email protected]" class="min-h-11 px-3.5 rounded-[9px] border border-tw03-line bg-tw03-well text-[15px] text-tw03-ink placeholder:text-tw03-sub transition-[border-color,background-color] duration-200 focus:outline-none focus:border-tw03-good focus:bg-white">
          </label>
          <label class="flex flex-col gap-1.5">
            <span class="text-[13px] font-semibold text-tw03-sub">Password</span>
            <input type="password" required minlength="10" autocomplete="new-password" spellcheck="false" class="min-h-11 px-3.5 rounded-[9px] border border-tw03-line bg-tw03-well text-[15px] text-tw03-ink transition-[border-color,background-color] duration-200 focus:outline-none focus:border-tw03-good focus:bg-white">
            <span aria-hidden="true" class="grid grid-cols-4 gap-1 mt-1.5">
              <span class="h-1 rounded-full bg-tw03-good"></span>
              <span class="h-1 rounded-full bg-tw03-good"></span>
              <span class="h-1 rounded-full bg-tw03-good"></span>
              <span class="h-1 rounded-full bg-tw03-line"></span>
            </span>
            <small class="text-xs tracking-wide text-tw03-sub">Good · 10+ characters · Not in breach databases</small>
          </label>
          <label class="flex items-start gap-2.5 py-1 text-[13.5px] leading-snug cursor-pointer">
            <input type="checkbox" required class="shrink-0 mt-0.5 size-4 accent-tw03-good cursor-pointer focus-visible:outline-2 focus-visible:outline-tw03-good focus-visible:outline-offset-2">
            <span>I agree to the <a href="#" class="text-tw03-good underline">Terms of Service</a> and <a href="#" class="text-tw03-good underline">Privacy Policy</a></span>
          </label>
          <label class="flex items-start gap-2.5 py-1 text-[13.5px] leading-snug cursor-pointer">
            <input type="checkbox" class="shrink-0 mt-0.5 size-4 accent-tw03-good cursor-pointer focus-visible:outline-2 focus-visible:outline-tw03-good focus-visible:outline-offset-2">
            <span>Send me product updates and CSS tips (optional)</span>
          </label>
          <button type="submit" class="min-h-11 mt-1.5 px-5 rounded-[9px] border-0 bg-tw03-good text-[15px] font-bold text-white shadow-[0_8px_20px_-6px_var(--color-tw03-glow)] cursor-pointer transition-[background-color,translate] duration-200 hover:bg-tw03-goodhover hover:-translate-y-px focus-visible:outline-2 focus-visible:outline-tw03-good focus-visible:outline-offset-2 motion-reduce:hover:translate-y-0">Create free account &rarr;</button>
        </form>
      </div>

      <div class="px-8 pt-4 pb-[22px] border-t border-tw03-line opacity-0 rotate-x-[-90deg] origin-top backface-hidden group-open:animate-tw03-fold [animation-delay:550ms] motion-reduce:animate-none motion-reduce:opacity-100 motion-reduce:rotate-x-0">
        <ul class="flex flex-wrap justify-center gap-4 list-none text-xs font-semibold tracking-wide text-tw03-sub">
          <li>✓ 14-day trial</li>
          <li>✓ No credit card</li>
          <li>✓ Cancel anytime</li>
        </ul>
      </div>
    </div>
  </dialog>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tw03-bg: #f7f8fa;
  --color-tw03-bg: oklch(0.98 0.003 255);
  --color-tw03-card: #ffffff;
  --color-tw03-card: oklch(1 0 0);
  --color-tw03-well: #f7f8fa;
  --color-tw03-well: oklch(0.97 0.004 255);
  --color-tw03-ink: #0f0f14;
  --color-tw03-ink: oklch(0.18 0.01 285);
  --color-tw03-sub: #6b7280;
  --color-tw03-sub: oklch(0.56 0.02 265);
  --color-tw03-line: #e5e7eb;
  --color-tw03-line: oklch(0.92 0.004 265);
  --color-tw03-good: #10b981;
  --color-tw03-good: oklch(0.7 0.15 163);
  --color-tw03-goodhover: #059669;
  --color-tw03-goodhover: oklch(0.63 0.14 163);
  --color-tw03-glow: #10b98180;
  --color-tw03-glow: oklch(0.7 0.15 163 / 0.5);
  --color-tw03-scrim: #0f172a99;
  --color-tw03-scrim: oklch(0.23 0.04 265 / 0.6);
  --font-tw03-sans: 'Outfit', system-ui, sans-serif;
  --animate-tw03-fold: tw03-fold .5s cubic-bezier(.34, 1.12, .5, 1) forwards;
}

.tw-03 {
  width: 100%;
}
/* The fold's keyframes. rotate is the individual property v4's rotate-x-* utilities
   also write, so the resting utility and the animation agree. */

@keyframes tw03-fold {
  from {
    opacity: 0;
    rotate: x -90deg;
  }

  50% {
    opacity: 1;
  }

  to {
    opacity: 1;
    rotate: x 0deg;
  }
}

#tw-03-dlg::backdrop {
  background: oklch(0.23 0.04 265 / 0);
  backdrop-filter: blur(0px);
  transition: background .22s ease, backdrop-filter .22s ease, overlay .22s allow-discrete, display .22s allow-discrete;
}

@starting-style {
  #tw-03-dlg[open]::backdrop {
    background: oklch(0.23 0.04 265 / 0);
    backdrop-filter: blur(0px);
  }
}

@media (prefers-reduced-motion: reduce) {
  #tw-03-dlg::backdrop {
    transition-duration: .001s;
  }
}
```

## JavaScript
```js
(function () {
  var root = document.querySelector('.tw-03');
  var dlg = root.querySelector('#tw-03-dlg');
  var card = dlg.firstElementChild;
  root.querySelector('[data-tw03-open]').addEventListener('click', function () { dlg.showModal(); });
  root.querySelector('[data-tw03-close]').addEventListener('click', function () { dlg.close(); });
  dlg.addEventListener('click', function (e) {
    var r = card.getBoundingClientRect();
    if (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) dlg.close();
  });
})();
```
