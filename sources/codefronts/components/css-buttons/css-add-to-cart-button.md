---
source: "codefronts"
url: "https://codefronts.com/components/css-buttons/css-add-to-cart-button/"
title: "CSS Add to Cart Button"
section: "components"
category: "css-buttons"
category_name: "CSS Buttons"
description: "The single most-measured button in e-commerce: press it and a cart glyph arcs into a badge, the badge digit bumps, and the label swaps to \"Added\" before…"
has_js: "true"
---

Here's a working CSS Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Add to Cart Button
Source: https://codefronts.com/components/css-buttons/css-add-to-cart-button/

The single most-measured button in e-commerce: press it and a cart glyph arcs into a badge, the badge digit bumps, and the label swaps to "Added" before returning to idle — with the real count announced politely so screen-reader users hear the outcome instead of watching it.
## HTML
```html
<div class="cb-09">
  <div class="cb-09__stage">
    <button class="cb-09__btn" type="button" data-state="idle">
      <span class="cb-09__slot cb-09__slot--idle">
        <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 4h2.2l2.3 10.5h9.8L19.5 7H6"/><circle cx="9.5" cy="19" r="1.5"/><circle cx="16.5" cy="19" r="1.5"/></svg>
        <span>Add to cart — $148</span>
      </span>
      <span class="cb-09__slot cb-09__slot--done">
        <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5 10 17.5 19 6.5"/></svg>
        <span>Added to cart</span>
      </span>
      <span class="cb-09__fly" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 4h2.2l2.3 10.5h9.8L19.5 7H6"/></svg>
      </span>
      <span class="cb-09__badge" aria-hidden="true">2</span>
    </button>
    <span class="cb-09__sr" role="status" aria-live="polite"></span>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap');

.cb-09 {
  --bg: #f7f5f2;
  --accent: #111827;
  --ink: #ffffff;
  --ok: #15803d;
  --badge: #f59e0b;
  --badge-ink: #1c1206;
  --dx: 6.5rem;
  --dy: 3.2rem;
  --radius: .85rem;
  --sans: "Plus Jakarta Sans",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(50% 0 0)) {
  .cb-09 {
    --bg: oklch(97% .006 85);
    --accent: oklch(20% .015 265);
    --ok: oklch(52% .14 148);
    --badge: oklch(78% .16 74);
  }
}

@media (prefers-color-scheme: dark) {
  .cb-09:not([data-theme="light"]) {
    --bg: #0c0b0a;
    --accent: #f5f4f0;
    --ink: #0e0e10;
    --ok: #22c55e;
  }
}

.cb-09[data-theme="dark"] {
  --bg: #0c0b0a;
  --accent: #f5f4f0;
  --ink: #0e0e10;
  --ok: #22c55e;
}

.cb-09,
.cb-09 *,
.cb-09 *::before,
.cb-09 *::after {
  box-sizing: border-box;
}

.cb-09__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,6vw,4rem);
}

.cb-09__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cb-09__btn {
  position: relative;
  cursor: pointer;
  display: grid;
  align-items: center;
  min-height: 3.4rem;
  padding: 0 1.8rem;
  border: 0;
  border-radius: var(--radius);
  font: inherit;
  font-size: 1rem;
  font-weight: 700;
  letter-spacing: -.01em;
  color: var(--ink);
  background: var(--accent);
  box-shadow: 0 12px 26px -14px color-mix(in oklab,var(--accent) 85%,transparent);
  transition: translate .22s cubic-bezier(.16,1,.3,1), background-color .35s ease;
}

.cb-09__slot {
  grid-area: 1/1;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: .6rem;
  opacity: 0;
  scale: .94;
  transition: opacity .2s ease, scale .3s cubic-bezier(.16,1,.3,1);
}

.cb-09__slot svg {
  width: 1.2rem;
  height: 1.2rem;
  flex: none;
}

.cb-09__btn[data-state="idle"] .cb-09__slot--idle,
.cb-09__btn[data-state="done"] .cb-09__slot--done {
  opacity: 1;
  scale: 1;
}

.cb-09__btn[data-state="done"] {
  background: var(--ok);
}

.cb-09__btn:hover {
  translate: 0 -2px;
}

.cb-09__btn:active {
  translate: 0 1px;
  scale: .99;
}

.cb-09__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.cb-09__fly {
  position: absolute;
  left: 1.8rem;
  top: 50%;
  margin-top: -.6rem;
  width: 1.2rem;
  height: 1.2rem;
  opacity: 0;
  pointer-events: none;
  color: var(--ink);
}

.cb-09__fly svg {
  width: 100%;
  height: 100%;
}

.cb-09__btn.is-fly .cb-09__fly {
  animation: cb-09-fly .72s cubic-bezier(.32,.06,.6,1) forwards;
}

@keyframes cb-09-fly {
  0% {
    translate: 0 0;
    scale: 1;
    opacity: 1;
  }

  55% {
    translate: calc(var(--dx) * .6) calc(var(--dy) * -1);
    scale: .72;
    opacity: 1;
  }

  100% {
    translate: var(--dx) -.4rem;
    scale: .25;
    opacity: 0;
  }
}

.cb-09__badge {
  position: absolute;
  top: -.55rem;
  right: -.55rem;
  min-width: 1.65rem;
  height: 1.65rem;
  padding: 0 .35rem;
  display: grid;
  place-items: center;
  border-radius: 999px;
  font-size: .8125rem;
  font-weight: 800;
  font-variant-numeric: tabular-nums;
  color: var(--badge-ink);
  background: var(--badge);
  box-shadow: 0 2px 8px -2px color-mix(in oklab,var(--badge) 80%,transparent);
}

.cb-09__badge.is-bump {
  animation: cb-09-bump .5s cubic-bezier(.16,1,.3,1);
}

@keyframes cb-09-bump {
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

@media (prefers-reduced-motion: reduce) {
  .cb-09__btn,
    .cb-09__slot {
    transition: none;
  }

  .cb-09__fly {
    display: none;
  }

  .cb-09__badge.is-bump {
    animation: none;
    outline: 2px solid var(--badge);
    outline-offset: 2px;
  }
}

@media (forced-colors: active) {
  .cb-09__btn {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
  }

  .cb-09__badge {
    background: Highlight;
    color: HighlightText;
  }
}
```

## JavaScript
```js
(() => {
  const btn = document.querySelector('.cb-09__btn');
  const badge = document.querySelector('.cb-09__badge');
  const live = document.querySelector('.cb-09__sr');
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
