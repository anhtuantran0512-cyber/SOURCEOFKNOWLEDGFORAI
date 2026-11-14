---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-close-buttons/tailwind-hamburger-to-x-menu-button-animation/"
title: "Tailwind Hamburger to X Menu Button Animation"
section: "components"
category: "tailwind-css-close-buttons"
category_name: "Tailwind CSS Close Buttons"
description: "Three bars become an ×: the top bar drops translate-y-2.5 and turns rotate-45, the middle one fades with scale-x-40, the bottom mirrors the top — all keyed…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Hamburger to X Menu Button Animation
Source: https://codefronts.com/components/tailwind-css-close-buttons/tailwind-hamburger-to-x-menu-button-animation/

Three bars become an ×: the top bar drops translate-y-2.5 and turns rotate-45, the middle one fades with scale-x-40, the bottom mirrors the top — all keyed off group-aria-expanded:. The menu wipes open with an animated clip-path, and the port fixes a real bug in the original: the collapsed links were still in the tab order. Now the closed nav is inert and Esc closes it.
## HTML
```html
<section class="tcb-08 w-full min-h-svh grid place-items-center bg-tcb08-bg px-6 py-12 font-tcb08-sans text-tcb08-ink" aria-label="Hamburger to X menu button demo">
  <div class="grid w-full justify-items-center gap-7">
    <div class="w-full max-w-[21rem]">
      <div class="flex items-center justify-between rounded-t-2xl border border-tcb08-line bg-tcb08-bar py-3 ps-5 pe-3">
        <span class="text-xs font-bold tracking-[0.16em]">NORTHWIND</span>
        <button id="tcb-08-btn" type="button" aria-expanded="false" aria-controls="tcb-08-nav" aria-label="Open menu" class="group flex size-11 cursor-pointer flex-col justify-center gap-2 rounded-xl p-2.5 transition-colors hover:bg-white/7 focus-visible:outline-[2.5px] focus-visible:outline-offset-2 focus-visible:outline-tcb08-acc motion-reduce:transition-none">
          <span aria-hidden="true" class="block h-0.5 w-full rounded-full bg-tcb08-ink transition duration-300 ease-[cubic-bezier(.4,0,.2,1)] group-aria-expanded:translate-y-2.5 group-aria-expanded:rotate-45 motion-reduce:transition-none"></span>
          <span aria-hidden="true" class="block h-0.5 w-full rounded-full bg-tcb08-ink transition duration-200 group-aria-expanded:scale-x-40 group-aria-expanded:opacity-0 motion-reduce:transition-none"></span>
          <span aria-hidden="true" class="block h-0.5 w-full rounded-full bg-tcb08-ink transition duration-300 ease-[cubic-bezier(.4,0,.2,1)] group-aria-expanded:-translate-y-2.5 group-aria-expanded:-rotate-45 motion-reduce:transition-none"></span>
        </button>
      </div>
      <nav id="tcb-08-nav" aria-label="Main" class="flex flex-col overflow-hidden rounded-b-2xl border border-t-0 border-tcb08-line bg-tcb08-panel transition-[clip-path] duration-350 ease-[cubic-bezier(.4,0,.2,1)] [clip-path:inset(0_0_100%_0)] data-open:[clip-path:inset(0)] motion-reduce:transition-none">
        <a href="#" class="flex min-h-12 items-center justify-between border-t border-tcb08-line/60 px-5 text-sm transition-colors hover:bg-white/5 focus-visible:outline-2 focus-visible:-outline-offset-3 focus-visible:outline-tcb08-acc">Work <span aria-hidden="true" class="text-tcb08-mut">→</span></a>
        <a href="#" class="flex min-h-12 items-center justify-between border-t border-tcb08-line/60 px-5 text-sm transition-colors hover:bg-white/5 focus-visible:outline-2 focus-visible:-outline-offset-3 focus-visible:outline-tcb08-acc">Studio <span aria-hidden="true" class="text-tcb08-mut">→</span></a>
        <a href="#" class="flex min-h-12 items-center justify-between border-t border-tcb08-line/60 px-5 text-sm transition-colors hover:bg-white/5 focus-visible:outline-2 focus-visible:-outline-offset-3 focus-visible:outline-tcb08-acc">Contact <span aria-hidden="true" class="text-tcb08-mut">→</span></a>
      </nav>
    </div>
    <p aria-hidden="true" class="rounded-full px-3.5 py-2 font-tcb08-mono text-[11.5px] text-tcb08-mut ring-1 ring-white/12">group-aria-expanded:rotate-45 · data-open:[clip-path:inset(0)] · inert</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcb08-bg: #13151f;
  --color-tcb08-bg: oklch(0.18 0.025 270);
  --color-tcb08-bar: #1c1f2c;
  --color-tcb08-bar: oklch(0.23 0.03 270);
  --color-tcb08-panel: #191b27;
  --color-tcb08-panel: oklch(0.21 0.028 270);
  --color-tcb08-line: #3a3e50;
  --color-tcb08-line: oklch(0.35 0.03 270);
  --color-tcb08-ink: #e7e8ef;
  --color-tcb08-ink: oklch(0.93 0.01 270);
  --color-tcb08-mut: #a3a6b8;
  --color-tcb08-mut: oklch(0.74 0.025 270);
  --color-tcb08-acc: #9197f2;
  --color-tcb08-acc: oklch(0.7 0.15 275);
  --font-tcb08-sans: 'Geist', system-ui, sans-serif;
  --font-tcb08-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-08 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const btn = document.getElementById('tcb-08-btn');
  if (!btn || btn.dataset.wired) return;
  btn.dataset.wired = '1';
  const nav = document.getElementById('tcb-08-nav');
  const set = (open) => {
    btn.setAttribute('aria-expanded', String(open));
    btn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    nav.toggleAttribute('data-open', open);
    nav.inert = !open;
  };
  set(false);
  btn.addEventListener('click', () => set(btn.getAttribute('aria-expanded') !== 'true'));
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && btn.getAttribute('aria-expanded') === 'true') { set(false); btn.focus(); }
  });
})();
```
