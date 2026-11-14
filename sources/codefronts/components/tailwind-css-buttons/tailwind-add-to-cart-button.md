---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-buttons/tailwind-add-to-cart-button/"
title: "Tailwind Add to Cart Button"
section: "components"
category: "tailwind-css-buttons"
category_name: "Tailwind CSS Buttons"
description: "The most-measured button in e-commerce: press it and a cart glyph arcs into a badge, the digit bumps, and the label swaps to \"Added\" before returning to idle…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Add to Cart Button
Source: https://codefronts.com/components/tailwind-css-buttons/tailwind-add-to-cart-button/

The most-measured button in e-commerce: press it and a cart glyph arcs into a badge, the digit bumps, and the label swaps to "Added" before returning to idle — with the real count announced politely, so screen-reader users hear the outcome instead of watching it.
## HTML
```html
<div class="tb-09 w-full min-h-svh grid place-items-center bg-tb09-bg font-tb09-sans antialiased p-[clamp(1.5rem,6vw,4rem)]">
  <button type="button" data-state="idle" style="--tb-09-dx:6.5rem;--tb-09-dy:3.2rem" class="tb-09__btn group relative cursor-pointer grid items-center min-h-14 px-7 border-0 rounded-[0.85rem] text-base font-bold tracking-[-0.01em] text-tb09-ink bg-tb09-accent shadow-[0_12px_26px_-14px_var(--color-tb09-glow)] transition-[translate,background-color,scale] duration-200 ease-tb09-out data-[state=done]:bg-tb09-ok hover:-translate-y-0.5 active:translate-y-px active:scale-[0.99] focus-visible:outline-2 focus-visible:outline-offset-[3px] focus-visible:outline-tb09-accent motion-reduce:transition-none motion-reduce:hover:translate-y-0">
    <span class="col-start-1 row-start-1 flex items-center justify-center gap-2.5 opacity-0 scale-95 transition-[opacity,scale] duration-200 ease-tb09-out group-data-[state=idle]:opacity-100 group-data-[state=idle]:scale-100 motion-reduce:transition-none">
      <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" class="size-[1.2rem] shrink-0"><path d="M3 4h2.2l2.3 10.5h9.8L19.5 7H6"/><circle cx="9.5" cy="19" r="1.5"/><circle cx="16.5" cy="19" r="1.5"/></svg>
      <span>Add to cart — $148</span>
    </span>
    <span class="col-start-1 row-start-1 flex items-center justify-center gap-2.5 opacity-0 scale-95 transition-[opacity,scale] duration-200 ease-tb09-out group-data-[state=done]:opacity-100 group-data-[state=done]:scale-100 motion-reduce:transition-none">
      <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" class="size-[1.2rem] shrink-0"><path d="M5 12.5 10 17.5 19 6.5"/></svg>
      <span>Added to cart</span>
    </span>
    <span aria-hidden="true" class="absolute left-7 top-1/2 -mt-[0.6rem] size-[1.2rem] opacity-0 pointer-events-none text-tb09-ink group-[.is-fly]:animate-tb09-fly motion-reduce:hidden">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-full"><path d="M3 4h2.2l2.3 10.5h9.8L19.5 7H6"/></svg>
    </span>
    <span aria-hidden="true" class="tb-09__badge absolute -top-2 -right-2 min-w-7 h-7 px-1.5 grid place-items-center rounded-full text-[0.8125rem] font-extrabold tabular-nums text-tb09-badge-ink bg-tb09-badge shadow-[0_2px_8px_-2px_var(--color-tb09-badge-glow)] [&.is-bump]:animate-tb09-bump motion-reduce:[&.is-bump]:animate-none motion-reduce:[&.is-bump]:outline-2 motion-reduce:[&.is-bump]:outline-tb09-badge motion-reduce:[&.is-bump]:outline-offset-2">2</span>
  </button>
  <span role="status" aria-live="polite" class="tb-09__live sr-only"></span>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tb09-bg: #f7f5f2;
  --color-tb09-bg: oklch(0.97 0.006 85);
  --color-tb09-accent: #111827;
  --color-tb09-accent: oklch(0.2 0.015 265);
  --color-tb09-ink: #ffffff;
  --color-tb09-ok: #15803d;
  --color-tb09-ok: oklch(0.52 0.14 148);
  --color-tb09-badge: #f59e0b;
  --color-tb09-badge: oklch(0.78 0.16 74);
  --color-tb09-badge-ink: #1c1206;
  --color-tb09-badge-ink: oklch(0.2 0.03 60);
  --color-tb09-badge-glow: #f59e0bcc;
  --color-tb09-badge-glow: oklch(0.78 0.16 74 / 0.8);
  --color-tb09-glow: #111827d9;
  --color-tb09-glow: oklch(0.2 0.015 265 / 0.85);
  --font-tb09-sans: "Plus Jakarta Sans", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --ease-tb09-out: cubic-bezier(0.16, 1, 0.3, 1);
  --animate-tb09-fly: tb-09-fly 0.72s cubic-bezier(0.32, 0.06, 0.6, 1) forwards;
  --animate-tb09-bump: tb-09-bump 0.5s cubic-bezier(0.16, 1, 0.3, 1);
}

@keyframes tb-09-fly {
  0% {
    translate: 0 0;
    scale: 1;
    opacity: 1;
  }

  55% {
    translate: calc(var(--tb-09-dx) * 0.6) calc(var(--tb-09-dy) * -1);
    scale: 0.72;
    opacity: 1;
  }

  100% {
    translate: var(--tb-09-dx) -0.4rem;
    scale: 0.25;
    opacity: 0;
  }
}

@keyframes tb-09-bump {
  0% {
    scale: 1;
  }

  35% {
    scale: 1.35;
    rotate: -6deg;
  }

  100% {
    scale: 1;
    rotate: 0deg;
  }
}

.tb-09 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
}

@media (prefers-color-scheme: dark) {
  .tb-09:not([data-theme="light"]) {
    --color-tb09-bg: oklch(0.13 0.006 70);
    --color-tb09-accent: oklch(0.95 0.005 85);
    --color-tb09-ink: oklch(0.16 0.006 265);
    --color-tb09-ok: oklch(0.72 0.17 148);
  }
}

.tb-09[data-theme="dark"] {
  --color-tb09-bg: oklch(0.13 0.006 70);
  --color-tb09-accent: oklch(0.95 0.005 85);
  --color-tb09-ink: oklch(0.16 0.006 265);
  --color-tb09-ok: oklch(0.72 0.17 148);
}

@media (forced-colors: active) {
  .tb-09 button {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
  }

  .tb-09__badge {
    background: Highlight;
    color: HighlightText;
  }
}
```

## JavaScript
```js
(() => {
  const btn = document.querySelector('.tb-09__btn');
  const badge = document.querySelector('.tb-09__badge');
  const live = document.querySelector('.tb-09__live');
  if (!btn) return;
  let count = Number(badge.textContent) || 0;
  let timer;
  btn.addEventListener('click', () => {
    count += 1;
    btn.classList.remove('is-fly');
    badge.classList.remove('is-bump');
    void btn.offsetWidth; // force reflow so both animations restart
    btn.classList.add('is-fly');
    btn.dataset.state = 'done';
    setTimeout(() => { badge.textContent = String(count); badge.classList.add('is-bump'); }, 380);
    live.textContent = 'Added. Cart has ' + count + ' items.';
    clearTimeout(timer);
    timer = setTimeout(() => { btn.dataset.state = 'idle'; btn.classList.remove('is-fly'); }, 1600);
  });
})();
```
