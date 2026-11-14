---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-modals/tailwind-confirm-delete-modal-corner-slide-spin/"
title: "Tailwind Confirm Delete Modal with Corner Slide-and-Spin Entrance"
section: "components"
category: "tailwind-css-modals"
category_name: "Tailwind CSS Modals"
description: "A destructive-action confirmation whose card swings in from the bottom-right at 3° and settles square."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Confirm Delete Modal with Corner Slide-and-Spin Entrance
Source: https://codefronts.com/components/tailwind-css-modals/tailwind-confirm-delete-modal-corner-slide-spin/

A destructive-action confirmation whose card swings in from the bottom-right at 3° and settles square. The port keeps the muted intensity of the original — a spring easing token, not a bounce — and states the whole entrance as open: plus open:starting: on the dialog, so the closed state, the open state and the pre-transition frame are one class list.
## HTML
```html
<section class="tw-01 w-full min-h-svh grid place-items-center bg-tw01-bg font-tw01-sans px-6 py-10">
  <button type="button" data-tw01-open class="inline-flex items-center justify-center min-h-11 px-6 rounded-lg text-[15px] font-semibold text-tw01-danger bg-transparent border border-tw01-danger cursor-pointer transition-colors duration-200 hover:bg-tw01-danger hover:text-white focus-visible:outline-2 focus-visible:outline-tw01-danger focus-visible:outline-offset-2">Delete report</button>

  <dialog id="tw-01-dlg" aria-labelledby="tw-01-title" aria-describedby="tw-01-desc" class="m-auto w-[min(360px,94vw)] p-0 border-0 rounded-[14px] text-center text-tw01-ink bg-tw01-card shadow-[0_30px_60px_-20px_#00000066] origin-bottom-right opacity-0 transition-[opacity,translate,rotate,scale,overlay,display] duration-[400ms] ease-[var(--ease-tw01-spring)] transition-discrete open:opacity-100 open:translate-x-0 open:translate-y-0 open:rotate-0 open:scale-100 open:starting:opacity-0 open:starting:translate-x-6 open:starting:translate-y-8 open:starting:rotate-3 open:starting:scale-[0.96] open:backdrop:bg-tw01-scrim open:backdrop:backdrop-blur-[4px] motion-reduce:transition-[opacity] motion-reduce:duration-150">
    <div class="px-[26px] pt-[26px] pb-[22px]">
      <span aria-hidden="true" class="inline-grid place-items-center size-12 mb-4 rounded-full bg-tw01-tint text-tw01-danger">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 6h18M8 6V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2M6 6l1 14a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2l1-14"/></svg>
      </span>
      <h2 id="tw-01-title" class="mb-2 text-[1.15rem] font-bold tracking-[-0.01em] leading-tight text-tw01-ink">Delete this report?</h2>
      <p id="tw-01-desc" class="mb-[22px] text-sm leading-relaxed text-tw01-sub text-pretty">You're about to permanently delete <strong class="font-semibold text-tw01-ink">Q3 Financial Report.pdf</strong>. This action cannot be undone and any team members sharing this report will lose access immediately.</p>
      <div class="grid grid-cols-2 gap-2">
        <button type="button" autofocus data-tw01-close class="min-h-11 rounded-lg border-0 text-sm font-semibold text-tw01-ink bg-tw01-well cursor-pointer transition-[background-color,translate] duration-150 hover:bg-tw01-wellhover active:translate-y-px focus-visible:outline-2 focus-visible:outline-tw01-ink focus-visible:outline-offset-2 motion-reduce:active:translate-y-0">Cancel</button>
        <button type="button" data-tw01-close class="min-h-11 rounded-lg border-0 text-sm font-semibold text-white bg-tw01-danger cursor-pointer transition-[background-color,translate] duration-150 hover:bg-tw01-dangerhover active:translate-y-px focus-visible:outline-2 focus-visible:outline-tw01-danger focus-visible:outline-offset-2 motion-reduce:active:translate-y-0">Delete report</button>
      </div>
    </div>
  </dialog>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tw01-bg: #f8fafc;
  --color-tw01-bg: oklch(0.98 0.005 250);
  --color-tw01-card: #ffffff;
  --color-tw01-card: oklch(1 0 0);
  --color-tw01-well: #f1f5f9;
  --color-tw01-well: oklch(0.96 0.006 250);
  --color-tw01-wellhover: #e2e8f0;
  --color-tw01-wellhover: oklch(0.92 0.01 250);
  --color-tw01-ink: #0f172a;
  --color-tw01-ink: oklch(0.23 0.04 265);
  --color-tw01-sub: #64748b;
  --color-tw01-sub: oklch(0.55 0.03 255);
  --color-tw01-danger: #dc2626;
  --color-tw01-danger: oklch(0.58 0.21 27);
  --color-tw01-dangerhover: #b91c1c;
  --color-tw01-dangerhover: oklch(0.51 0.19 27);
  --color-tw01-tint: #dc262624;
  --color-tw01-tint: oklch(0.58 0.21 27 / 0.14);
  --color-tw01-scrim: #0f172ab8;
  --color-tw01-scrim: oklch(0.23 0.04 265 / 0.72);
  --font-tw01-sans: 'Outfit', system-ui, sans-serif;
  --ease-tw01-spring: cubic-bezier(0.34, 1.36, 0.44, 1);
}
/* Root rule: the width half of the full-bleed contract; the height comes from the
   markup's min-h-svh utility. */

.tw-01 {
  width: 100%;
}
/* The one thing the variants cannot hold: the ::backdrop enter/exit transition. */

#tw-01-dlg::backdrop {
  background: oklch(0.23 0.04 265 / 0);
  backdrop-filter: blur(0px);
  transition: background .22s ease, backdrop-filter .22s ease, overlay .22s allow-discrete, display .22s allow-discrete;
}

@starting-style {
  #tw-01-dlg[open]::backdrop {
    background: oklch(0.23 0.04 265 / 0);
    backdrop-filter: blur(0px);
  }
}

@media (prefers-reduced-motion: reduce) {
  #tw-01-dlg::backdrop {
    transition-duration: .001s;
  }
}
```

## JavaScript
```js
(function () {
  var root = document.querySelector('.tw-01');
  var dlg = root.querySelector('#tw-01-dlg');
  var card = dlg.firstElementChild;
  root.querySelector('[data-tw01-open]').addEventListener('click', function () { dlg.showModal(); });
  root.querySelectorAll('[data-tw01-close]').forEach(function (b) {
    b.addEventListener('click', function () { dlg.close(); });
  });
  // Light-dismiss: the click landed on the dialog box, outside the card's rect.
  dlg.addEventListener('click', function (e) {
    var r = card.getBoundingClientRect();
    if (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) dlg.close();
  });
})();
```
