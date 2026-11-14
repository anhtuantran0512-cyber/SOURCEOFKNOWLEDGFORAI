---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-modals/tailwind-gdpr-cookie-preferences-modal-unfolding-rows/"
title: "Tailwind GDPR Cookie Preferences Modal with Unfolding Category Rows"
section: "components"
category: "tailwind-css-modals"
category_name: "Tailwind CSS Modals"
description: "A consent centre whose four category rows unfold downward like origami while the title and the three actions are readable from frame one — the fast path…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind GDPR Cookie Preferences Modal with Unfolding Category Rows
Source: https://codefronts.com/components/tailwind-css-modals/tailwind-gdpr-cookie-preferences-modal-unfolding-rows/

A consent centre whose four category rows unfold downward like origami while the title and the three actions are readable from frame one — the fast path stays fast. The port drives the cascade from the dialog's own [open] state with in-[dialog[open]]: plus per-row [transition-delay:…], and builds the toggles from peer-checked: instead of custom controls.
## HTML
```html
<section class="tw-07 w-full min-h-svh grid place-items-center bg-tw07-bg font-tw07-sans px-6 py-10">
  <button type="button" data-tw07-open class="inline-flex items-center justify-center min-h-11 px-6 rounded-lg border border-tw07-line bg-tw07-card text-[15px] font-semibold text-tw07-ink cursor-pointer transition-colors duration-200 hover:bg-tw07-well2 focus-visible:outline-2 focus-visible:outline-tw07-ink focus-visible:outline-offset-2">Cookie preferences</button>

  <dialog id="tw-07-dlg" aria-labelledby="tw-07-title" class="m-auto w-[min(560px,94vw)] p-0 border-0 rounded-[14px] text-left text-tw07-ink bg-tw07-card shadow-[0_40px_60px_-20px_#0f172a59] opacity-0 transition-[opacity,overlay,display] duration-200 transition-discrete open:opacity-100 open:starting:opacity-0 open:backdrop:bg-tw07-scrim open:backdrop:backdrop-blur-[4px]">
    <div class="relative px-8 pt-8 pb-6">
      <button type="button" data-tw07-close aria-label="Close dialog" class="absolute top-3.5 right-3.5 grid place-items-center size-9 rounded-lg border-0 bg-transparent text-tw07-sub text-base cursor-pointer transition-colors duration-200 hover:bg-tw07-well2 hover:text-tw07-ink focus-visible:outline-2 focus-visible:outline-tw07-ink focus-visible:outline-offset-2">&#10005;</button>

      <h2 id="tw-07-title" class="mb-2 text-[1.35rem] font-extrabold tracking-[-0.015em] leading-tight">Cookie preferences</h2>
      <p class="mb-5 text-sm leading-relaxed text-tw07-sub text-pretty">We use cookies to enhance your experience, analyze site traffic, and improve services. You can accept all, reject all non-essential, or customize per category.</p>

      <div class="flex flex-col gap-2 mb-5 perspective-[900px]">
        <div class="px-4 py-3.5 rounded-[9px] border border-tw07-line bg-tw07-well origin-bottom backface-hidden opacity-0 rotate-x-[-180deg] transition-[opacity,rotate] duration-700 ease-[cubic-bezier(.4,.15,.25,1)] in-[dialog[open]]:opacity-100 in-[dialog[open]]:rotate-x-0 [transition-delay:0ms] motion-reduce:transition-opacity motion-reduce:rotate-x-0 motion-reduce:[transition-delay:0ms]">
          <div class="flex justify-between items-start gap-3.5">
            <div>
              <h3 class="mb-0.5 text-sm font-bold">Strictly necessary</h3>
              <p class="text-xs leading-snug text-tw07-sub">Session cookies, CSRF tokens, load balancing. Cannot be disabled.</p>
            </div>
            <span class="shrink-0 grid place-items-center w-[42px] h-[22px] rounded-full bg-tw07-locked text-[0.62rem] font-extrabold tracking-wider text-white">ON</span>
          </div>
        </div>

        <div class="px-4 py-3.5 rounded-[9px] border border-tw07-line bg-tw07-well origin-bottom backface-hidden opacity-0 rotate-x-[-180deg] transition-[opacity,rotate] duration-700 ease-[cubic-bezier(.4,.15,.25,1)] in-[dialog[open]]:opacity-100 in-[dialog[open]]:rotate-x-0 [transition-delay:180ms] motion-reduce:transition-opacity motion-reduce:rotate-x-0 motion-reduce:[transition-delay:0ms]">
          <div class="flex justify-between items-start gap-3.5">
            <div>
              <h3 class="mb-0.5 text-sm font-bold">Analytics</h3>
              <p class="text-xs leading-snug text-tw07-sub">Google Analytics, PostHog. Helps us understand aggregate usage patterns.</p>
            </div>
            <label class="shrink-0 cursor-pointer">
              <input type="checkbox" checked class="peer sr-only">
              <span class="sr-only">Allow analytics cookies</span>
              <span aria-hidden="true" class="grid items-center w-[42px] h-[22px] rounded-full bg-tw07-off transition-colors duration-200 peer-checked:bg-tw07-good peer-focus-visible:outline-2 peer-focus-visible:outline-tw07-ink peer-focus-visible:outline-offset-2"><span class="block size-[18px] ml-0.5 rounded-full bg-white transition-transform duration-200 peer-checked:translate-x-5 motion-reduce:transition-none"></span></span>
            </label>
          </div>
        </div>

        <div class="px-4 py-3.5 rounded-[9px] border border-tw07-line bg-tw07-well origin-bottom backface-hidden opacity-0 rotate-x-[-180deg] transition-[opacity,rotate] duration-700 ease-[cubic-bezier(.4,.15,.25,1)] in-[dialog[open]]:opacity-100 in-[dialog[open]]:rotate-x-0 [transition-delay:360ms] motion-reduce:transition-opacity motion-reduce:rotate-x-0 motion-reduce:[transition-delay:0ms]">
          <div class="flex justify-between items-start gap-3.5">
            <div>
              <h3 class="mb-0.5 text-sm font-bold">Marketing</h3>
              <p class="text-xs leading-snug text-tw07-sub">Facebook Pixel, LinkedIn Insight Tag. Enables retargeting and personalized ads.</p>
            </div>
            <label class="shrink-0 cursor-pointer">
              <input type="checkbox" class="peer sr-only">
              <span class="sr-only">Allow marketing cookies</span>
              <span aria-hidden="true" class="grid items-center w-[42px] h-[22px] rounded-full bg-tw07-off transition-colors duration-200 peer-checked:bg-tw07-good peer-focus-visible:outline-2 peer-focus-visible:outline-tw07-ink peer-focus-visible:outline-offset-2"><span class="block size-[18px] ml-0.5 rounded-full bg-white transition-transform duration-200 peer-checked:translate-x-5 motion-reduce:transition-none"></span></span>
            </label>
          </div>
        </div>

        <div class="px-4 py-3.5 rounded-[9px] border border-tw07-line bg-tw07-well origin-bottom backface-hidden opacity-0 rotate-x-[-180deg] transition-[opacity,rotate] duration-700 ease-[cubic-bezier(.4,.15,.25,1)] in-[dialog[open]]:opacity-100 in-[dialog[open]]:rotate-x-0 [transition-delay:540ms] motion-reduce:transition-opacity motion-reduce:rotate-x-0 motion-reduce:[transition-delay:0ms]">
          <div class="flex justify-between items-start gap-3.5">
            <div>
              <h3 class="mb-0.5 text-sm font-bold">Personalization</h3>
              <p class="text-xs leading-snug text-tw07-sub">Recommendation engine, saved preferences, theme mode. Improves your experience.</p>
            </div>
            <label class="shrink-0 cursor-pointer">
              <input type="checkbox" checked class="peer sr-only">
              <span class="sr-only">Allow personalization cookies</span>
              <span aria-hidden="true" class="grid items-center w-[42px] h-[22px] rounded-full bg-tw07-off transition-colors duration-200 peer-checked:bg-tw07-good peer-focus-visible:outline-2 peer-focus-visible:outline-tw07-ink peer-focus-visible:outline-offset-2"><span class="block size-[18px] ml-0.5 rounded-full bg-white transition-transform duration-200 peer-checked:translate-x-5 motion-reduce:transition-none"></span></span>
            </label>
          </div>
        </div>
      </div>

      <div class="grid grid-cols-3 gap-2 mb-4 max-[440px]:grid-cols-1">
        <button type="button" autofocus data-tw07-close class="min-h-11 px-4 rounded-lg border border-tw07-line bg-tw07-well2 text-sm font-semibold text-tw07-ink cursor-pointer transition-colors duration-200 hover:bg-tw07-well3 focus-visible:outline-2 focus-visible:outline-tw07-ink focus-visible:outline-offset-2">Reject all</button>
        <button type="button" data-tw07-close class="min-h-11 px-4 rounded-lg border border-tw07-line bg-tw07-well2 text-sm font-semibold text-tw07-ink cursor-pointer transition-colors duration-200 hover:bg-tw07-well3 focus-visible:outline-2 focus-visible:outline-tw07-ink focus-visible:outline-offset-2">Save preferences</button>
        <button type="button" data-tw07-close class="min-h-11 px-4 rounded-lg border border-tw07-line bg-tw07-well2 text-sm font-semibold text-tw07-ink cursor-pointer transition-colors duration-200 hover:bg-tw07-well3 focus-visible:outline-2 focus-visible:outline-tw07-ink focus-visible:outline-offset-2">Accept all</button>
      </div>

      <p class="pt-3.5 border-t border-tw07-line text-xs text-tw07-sub">Read our <a href="#" class="text-tw07-ink underline">Cookie Policy</a> and <a href="#" class="text-tw07-ink underline">Privacy Policy</a>. You can change preferences anytime.</p>
    </div>
  </dialog>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tw07-bg: #f8fafc;
  --color-tw07-bg: oklch(0.98 0.005 250);
  --color-tw07-card: #ffffff;
  --color-tw07-card: oklch(1 0 0);
  --color-tw07-well: #fafbfc;
  --color-tw07-well: oklch(0.98 0.003 255);
  --color-tw07-well2: #f1f5f9;
  --color-tw07-well2: oklch(0.96 0.006 250);
  --color-tw07-well3: #e2e8f0;
  --color-tw07-well3: oklch(0.92 0.01 250);
  --color-tw07-ink: #1e293b;
  --color-tw07-ink: oklch(0.3 0.03 258);
  --color-tw07-sub: #55657c;
  --color-tw07-sub: oklch(0.5 0.03 255);
  --color-tw07-line: #e2e8f0;
  --color-tw07-line: oklch(0.92 0.01 250);
  --color-tw07-good: #059669;
  --color-tw07-good: oklch(0.63 0.14 163);
  --color-tw07-off: #94a3b8;
  --color-tw07-off: oklch(0.7 0.03 255);
  --color-tw07-locked: #64748b;
  --color-tw07-locked: oklch(0.55 0.03 255);
  --color-tw07-scrim: #0f172a99;
  --color-tw07-scrim: oklch(0.23 0.04 265 / 0.6);
  --font-tw07-sans: 'Outfit', system-ui, sans-serif;
}

.tw-07 {
  width: 100%;
}

#tw-07-dlg::backdrop {
  background: oklch(0.23 0.04 265 / 0);
  backdrop-filter: blur(0px);
  transition: background .2s ease, backdrop-filter .2s ease, overlay .2s allow-discrete, display .2s allow-discrete;
}

@starting-style {
  #tw-07-dlg[open]::backdrop {
    background: oklch(0.23 0.04 265 / 0);
    backdrop-filter: blur(0px);
  }
}

@media (prefers-reduced-motion: reduce) {
  #tw-07-dlg::backdrop {
    transition-duration: .001s;
  }
}
```

## JavaScript
```js
(function () {
  var root = document.querySelector('.tw-07');
  var dlg = root.querySelector('#tw-07-dlg');
  var card = dlg.firstElementChild;
  root.querySelector('[data-tw07-open]').addEventListener('click', function () { dlg.showModal(); });
  root.querySelectorAll('[data-tw07-close]').forEach(function (b) {
    // Production: read the toggles here and gate your script loader on the result.
    b.addEventListener('click', function () { dlg.close(); });
  });
  dlg.addEventListener('click', function (e) {
    var r = card.getBoundingClientRect();
    if (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) dlg.close();
  });
})();
```
