---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-modals/tailwind-onboarding-welcome-modal-blur-in-content-drop/"
title: "Tailwind SaaS Onboarding Welcome Modal with Cascading Blur-In"
section: "components"
category: "tailwind-css-modals"
category_name: "Tailwind CSS Modals"
description: "A first-run welcome whose contents develop in sequence — stepper, illustration, headline, copy, CTA — over a deliberately unhurried 1.3 seconds. Same cascade…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind SaaS Onboarding Welcome Modal with Cascading Blur-In
Source: https://codefronts.com/components/tailwind-css-modals/tailwind-onboarding-welcome-modal-blur-in-content-drop/

A first-run welcome whose contents develop in sequence — stepper, illustration, headline, copy, CTA — over a deliberately unhurried 1.3 seconds. Same cascade technique as demo 02, applied to a moment that can afford the time, with the primary action clickable from the first frame rather than at the end of the choreography.
## HTML
```html
<section class="tw-16 w-full min-h-svh grid place-items-center bg-tw16-bg font-tw16-sans px-6 py-10">
  <button type="button" data-tw16-open class="inline-flex items-center justify-center min-h-11 px-6 rounded-[9px] border-0 bg-tw16-brand text-[15px] font-bold text-white shadow-[0_8px_20px_-6px_var(--color-tw16-glow)] cursor-pointer transition-[background-color,translate] duration-200 hover:bg-tw16-branddark hover:-translate-y-px focus-visible:outline-2 focus-visible:outline-tw16-brand focus-visible:outline-offset-2 motion-reduce:hover:translate-y-0">Sign in as Alex</button>

  <dialog id="tw-16-dlg" aria-labelledby="tw-16-title" class="group m-auto w-[min(440px,94vw)] p-0 border-0 rounded-2xl text-center text-tw16-ink bg-tw16-card shadow-[0_40px_60px_-20px_#1e1b4b59] opacity-0 transition-[opacity,overlay,display] duration-300 transition-discrete open:opacity-100 open:starting:opacity-0 open:backdrop:bg-tw16-scrim open:backdrop:backdrop-blur-[6px]">
    <div class="relative px-8 pt-8 pb-6">
      <button type="button" data-tw16-close aria-label="Skip onboarding for now" class="absolute top-3.5 right-3.5 grid place-items-center size-9 rounded-lg border-0 bg-transparent text-[15px] text-tw16-sub cursor-pointer transition-colors duration-200 hover:bg-tw16-line hover:text-tw16-ink focus-visible:outline-2 focus-visible:outline-tw16-brand focus-visible:outline-offset-2">&#10005;</button>

      <div role="progressbar" aria-valuenow="1" aria-valuemin="1" aria-valuemax="3" aria-label="Step 1 of 3" class="flex justify-center gap-1.5 mb-5">
        <span class="w-7 h-1 rounded-full bg-tw16-brand"></span>
        <span class="w-7 h-1 rounded-full bg-tw16-line"></span>
        <span class="w-7 h-1 rounded-full bg-tw16-line"></span>
      </div>

      <div role="img" aria-label="Colourful abstract workspace illustration" class="relative w-[170px] h-[120px] mx-auto mb-[18px] opacity-0 blur-[8px] group-open:animate-tw16-drop [animation-delay:200ms] motion-reduce:animate-none motion-reduce:opacity-100 motion-reduce:blur-none">
        <span class="absolute top-2 left-0 w-[110px] h-20 rounded-[14px] -rotate-6 bg-linear-to-br from-tw16-brandlt to-tw16-brand"></span>
        <span class="absolute top-5 left-[60px] w-[90px] h-24 rounded-[14px] rotate-3 bg-linear-to-br from-tw16-amberlt to-tw16-amber"></span>
        <span class="absolute top-11 left-[110px] size-15 rounded-full bg-linear-to-br from-tw16-mintlt to-tw16-mint"></span>
      </div>

      <p class="mb-1.5 text-sm font-semibold text-tw16-sub opacity-0 blur-[8px] group-open:animate-tw16-drop [animation-delay:320ms] motion-reduce:animate-none motion-reduce:opacity-100 motion-reduce:blur-none">Welcome, Alex</p>
      <h2 id="tw-16-title" class="mb-2.5 text-[1.6rem] font-extrabold tracking-[-0.02em] leading-tight bg-linear-to-br from-tw16-ink to-tw16-brand bg-clip-text text-transparent opacity-0 blur-[8px] group-open:animate-tw16-drop [animation-delay:440ms] motion-reduce:animate-none motion-reduce:opacity-100 motion-reduce:blur-none">Let's set up your workspace</h2>
      <p class="mb-5 text-sm leading-relaxed text-tw16-sub text-pretty opacity-0 blur-[8px] group-open:animate-tw16-drop [animation-delay:560ms] motion-reduce:animate-none motion-reduce:opacity-100 motion-reduce:blur-none">Answer a few quick questions and we'll tailor Northlight to how your team ships. Takes about 2 minutes.</p>

      <button type="button" autofocus data-tw16-close class="w-full min-h-11 mb-2 px-5 py-3.5 rounded-[9px] border-0 bg-tw16-brand text-[15px] font-bold text-white shadow-[0_10px_24px_-6px_var(--color-tw16-glow)] cursor-pointer transition-[background-color,translate] duration-200 hover:bg-tw16-branddark hover:-translate-y-px focus-visible:outline-2 focus-visible:outline-tw16-brand focus-visible:outline-offset-[3px] opacity-0 blur-[8px] group-open:animate-tw16-drop [animation-delay:680ms] motion-reduce:animate-none motion-reduce:opacity-100 motion-reduce:blur-none motion-reduce:hover:translate-y-0">Get started · 2 min</button>
      <button type="button" data-tw16-close class="w-full min-h-11 px-4 rounded-md border-0 bg-transparent text-[13px] font-medium text-tw16-sub cursor-pointer transition-colors duration-200 hover:text-tw16-ink hover:underline focus-visible:outline-2 focus-visible:outline-tw16-brand focus-visible:outline-offset-2 opacity-0 blur-[8px] group-open:animate-tw16-drop [animation-delay:800ms] motion-reduce:animate-none motion-reduce:opacity-100 motion-reduce:blur-none">I'll do this later</button>
    </div>
  </dialog>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tw16-bg: #faf7ff;
  --color-tw16-bg: oklch(0.97 0.015 300);
  --color-tw16-card: #ffffff;
  --color-tw16-card: oklch(1 0 0);
  --color-tw16-ink: #1e1b4b;
  --color-tw16-ink: oklch(0.26 0.09 285);
  --color-tw16-sub: #5c6270;
  --color-tw16-sub: oklch(0.51 0.02 268);
  --color-tw16-line: #ede9fe;
  --color-tw16-line: oklch(0.94 0.025 300);
  --color-tw16-brand: #7c3aed;
  --color-tw16-brand: oklch(0.54 0.25 296);
  --color-tw16-branddark: #6d28d9;
  --color-tw16-branddark: oklch(0.49 0.24 296);
  --color-tw16-brandlt: #a78bfa;
  --color-tw16-brandlt: oklch(0.73 0.16 296);
  --color-tw16-amber: #f59e0b;
  --color-tw16-amber: oklch(0.75 0.16 70);
  --color-tw16-amberlt: #fbbf24;
  --color-tw16-amberlt: oklch(0.83 0.16 84);
  --color-tw16-mint: #10b981;
  --color-tw16-mint: oklch(0.7 0.15 163);
  --color-tw16-mintlt: #34d399;
  --color-tw16-mintlt: oklch(0.77 0.14 163);
  --color-tw16-glow: #7c3aed80;
  --color-tw16-glow: oklch(0.54 0.25 296 / 0.5);
  --color-tw16-scrim: #1e1b4b80;
  --color-tw16-scrim: oklch(0.26 0.09 285 / 0.5);
  --font-tw16-sans: 'Outfit', system-ui, sans-serif;
  --animate-tw16-drop: tw16-drop .5s cubic-bezier(.22, 1, .36, 1) forwards;
}

.tw-16 {
  width: 100%;
}

@keyframes tw16-drop {
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

#tw-16-dlg::backdrop {
  background: oklch(0.26 0.09 285 / 0);
  backdrop-filter: blur(0px);
  transition: background .3s ease, backdrop-filter .3s ease, overlay .3s allow-discrete, display .3s allow-discrete;
}

@starting-style {
  #tw-16-dlg[open]::backdrop {
    background: oklch(0.26 0.09 285 / 0);
    backdrop-filter: blur(0px);
  }
}

@media (prefers-reduced-motion: reduce) {
  #tw-16-dlg::backdrop {
    transition-duration: .001s;
  }
}
```

## JavaScript
```js
(function () {
  var root = document.querySelector('.tw-16');
  var dlg = root.querySelector('#tw-16-dlg');
  var card = dlg.firstElementChild;
  // Production: show once per user, e.g. guard on a server flag rather than a click.
  root.querySelector('[data-tw16-open]').addEventListener('click', function () { dlg.showModal(); });
  root.querySelectorAll('[data-tw16-close]').forEach(function (b) {
    b.addEventListener('click', function () { dlg.close(); });
  });
  dlg.addEventListener('click', function (e) {
    var r = card.getBoundingClientRect();
    if (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) dlg.close();
  });
})();
```
