---
source: "codefronts"
url: "https://codefronts.com/components/css-floating-buttons/morph-expand-fab/"
title: "Morphing FAB Button That Expands to Pill CSS"
section: "components"
category: "css-floating-buttons"
category_name: "CSS Floating Buttons"
description: "A FAB that does not open a panel — it becomes one."
has_js: "true"
---

Here's a working CSS Floating Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Morphing FAB Button That Expands to Pill CSS
Source: https://codefronts.com/components/css-floating-buttons/morph-expand-fab/

A FAB that does not open a panel — it becomes one. Tap the circle and it stretches into a search pill with a live input and results; dismiss and it retracts into the same circle. Uses the View Transition API for the shared-element morph with a pure-CSS fallback, so the container feels continuous instead of one element vanishing while another appears.
## HTML
```html
<section class="fb-11" aria-label="Morphing floating button demo">
  <div class="fb-11__page">
    <p class="fb-11__eyebrow">view-transition-name · shared element</p>
    <h2 class="fb-11__title">The button becomes the panel</h2>
    <p class="fb-11__sub">No fade-out, no pop-in. One container that stretches, keeps its identity, and hands focus to the field inside it.</p>
    <p class="fb-11__chip">startViewTransition() · Escape to retract</p>
  </div>
  <div class="fb-11__dock" id="fb-11-dock" data-open="false">
    <div class="fb-11__pill" id="fb-11-pill">
      <span class="fb-11__pIco" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><circle cx="11" cy="11" r="6.4" fill="none" stroke="currentColor" stroke-width="2"/><path d="M15.8 15.8L21 21" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></span>
      <input class="fb-11__input" id="fb-11-input" type="text" placeholder="Search commands…" aria-label="Search commands" autocomplete="off">
      <button class="fb-11__close" id="fb-11-close" type="button" aria-label="Close search">×</button>
      <ul class="fb-11__results" id="fb-11-results">
        <li><button type="button"><kbd>⌘K</kbd>Open command palette</button></li>
        <li><button type="button"><kbd>N</kbd>New document</button></li>
        <li><button type="button"><kbd>T</kbd>Toggle theme</button></li>
      </ul>
    </div>
    <button class="fb-11__fab" id="fb-11-fab" type="button" aria-expanded="false" aria-controls="fb-11-pill" aria-label="Open search">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6.4" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="M15.8 15.8L21 21" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>
    </button>
  </div>
</section>
```
## CSS
```css
.fb-11 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--fb-11-bg);
  --fb-11-bg: linear-gradient(200deg,oklch(0.22 0.04 275),oklch(0.14 0.02 275) 65%);
  --fb-11-brand: oklch(0.74 0.16 165);
  --fb-11-ink: oklch(0.97 0.01 275);
  --fb-11-mut: oklch(0.75 0.02 275);
  --fb-11-card: oklch(0.24 0.03 275);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--fb-11-ink);
  position: relative;
  display: grid;
  place-items: center;
  padding: clamp(20px,5vw,56px);
  overflow: hidden;
}

.fb-11 *,
.fb-11 *::before,
.fb-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fb-11__page {
  width: min(100%,54ch);
  display: grid;
  gap: 12px;
  justify-items: center;
  text-align: center;
}

.fb-11__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--fb-11-brand);
}

.fb-11__title {
  font-size: clamp(26px,4.6vw,44px);
  line-height: 1.05;
  letter-spacing: -.03em;
  font-weight: 700;
  text-wrap: balance;
}

.fb-11__sub {
  font-size: clamp(13.5px,1.7vw,16.5px);
  line-height: 1.62;
  color: var(--fb-11-mut);
  text-wrap: pretty;
}

.fb-11__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--fb-11-mut);
  padding: 8px 14px;
  border: 1px solid oklch(1 0 0/.16);
  border-radius: 99px;
}

.fb-11__dock {
  position: absolute;
  right: clamp(18px,4vw,44px);
  bottom: calc(clamp(18px,4vw,44px) + env(safe-area-inset-bottom));
  z-index: 5;
  display: grid;
  justify-items: end;
}

.fb-11__fab {
  view-transition-name: fb-11-morph;
  display: grid;
  place-items: center;
  inline-size: 62px;
  block-size: 62px;
  border: 0;
  border-radius: 50%;
  cursor: pointer;
  color: oklch(0.16 0.04 165);
  background: linear-gradient(150deg,oklch(0.86 0.14 155),var(--fb-11-brand));
  box-shadow: 0 14px 34px -12px oklch(0.74 0.16 165/.6),0 2px 6px oklch(0.1 0.02 275/.6);
  transition: transform .28s cubic-bezier(.2,1.3,.4,1),opacity .2s ease;
}

.fb-11__fab svg {
  width: 26px;
  height: 26px;
}

.fb-11__fab:hover {
  transform: translateY(-2px) scale(1.04);
}

.fb-11__fab:active {
  transform: scale(.93);
}

.fb-11__fab:focus-visible {
  outline: 3px solid var(--fb-11-brand);
  outline-offset: 4px;
}

.fb-11__pill {
  display: none;
  view-transition-name: fb-11-morph;
  width: min(86vw,392px);
  padding: 10px 10px 10px 16px;
  border-radius: 26px;
  background: var(--fb-11-card);
  border: 1px solid oklch(1 0 0/.1);
  box-shadow: 0 30px 70px -26px oklch(0.05 0.02 275/.9),0 2px 6px oklch(0.05 0.02 275/.5);
  grid-template-columns: auto 1fr auto;
  align-items: center;
  gap: 10px;
  transition: width .34s cubic-bezier(.2,.9,.3,1),border-radius .34s ease;
}

.fb-11__dock[data-open="true"] .fb-11__pill {
  display: grid;
}

.fb-11__dock[data-open="true"] .fb-11__fab {
  display: none;
}

.fb-11__pIco {
  display: grid;
  place-items: center;
  color: var(--fb-11-brand);
}

.fb-11__pIco svg {
  width: 20px;
  height: 20px;
}

.fb-11__input {
  grid-column: 2;
  min-height: 42px;
  border: 0;
  background: transparent;
  color: var(--fb-11-ink);
  font-size: 15.5px;
  font-family: inherit;
  outline: 0;
  min-width: 0;
}

.fb-11__input::placeholder {
  color: oklch(0.65 0.02 275);
}

.fb-11__input:focus-visible {
  outline: 2px solid var(--fb-11-brand);
  outline-offset: 4px;
  border-radius: 8px;
}

.fb-11__close {
  grid-column: 3;
  width: 38px;
  height: 38px;
  border: 0;
  border-radius: 50%;
  background: oklch(1 0 0/.07);
  color: var(--fb-11-mut);
  font-size: 20px;
  line-height: 1;
  cursor: pointer;
  transition: background .18s ease,color .18s ease;
}

.fb-11__close:hover {
  background: oklch(1 0 0/.14);
  color: var(--fb-11-ink);
}

.fb-11__close:focus-visible {
  outline: 2.5px solid var(--fb-11-brand);
  outline-offset: 2px;
}

.fb-11__results {
  grid-column: 1/-1;
  list-style: none;
  display: grid;
  gap: 2px;
  margin-top: 6px;
  border-top: 1px solid oklch(1 0 0/.08);
  padding-top: 8px;
}

.fb-11__results button {
  display: flex;
  align-items: center;
  gap: 11px;
  width: 100%;
  min-height: 44px;
  padding: 0 12px;
  border: 0;
  border-radius: 14px;
  background: transparent;
  color: var(--fb-11-ink);
  font-size: 14px;
  font-family: inherit;
  text-align: left;
  cursor: pointer;
  transition: background .16s ease;
}

.fb-11__results button:hover {
  background: oklch(1 0 0/.07);
}

.fb-11__results button:focus-visible {
  outline: 2.5px solid var(--fb-11-brand);
  outline-offset: -2px;
}

.fb-11__results kbd {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 10.5px;
  min-width: 32px;
  text-align: center;
  padding: 3px 6px;
  border-radius: 6px;
  background: oklch(1 0 0/.09);
  border: 1px solid oklch(1 0 0/.12);
  color: var(--fb-11-mut);
}

::view-transition-group(fb-11-morph) {
  animation-duration: .42s;
  animation-timing-function: cubic-bezier(.2,.9,.25,1);
}

@media (prefers-reduced-motion: reduce) {
  .fb-11 * {
    transition: none !important;
  }

  ::view-transition-group(fb-11-morph) {
    animation-duration: .01ms;
  }
}
```

## JavaScript
```js
(() => {
  const dock = document.getElementById('fb-11-dock');
  const fab = document.getElementById('fb-11-fab');
  const input = document.getElementById('fb-11-input');
  const close = document.getElementById('fb-11-close');
  if (!dock || !fab || fab.dataset.fbWired) return;
  fab.dataset.fbWired = '1';
  const apply = (open) => {
    dock.dataset.open = String(open);
    fab.setAttribute('aria-expanded', String(open));
  };
  const swap = (open) => {
    if (!document.startViewTransition) { apply(open); return Promise.resolve(); }
    return document.startViewTransition(() => apply(open)).finished;
  };
  fab.addEventListener('click', () => { swap(true).then(() => input.focus()); });
  close.addEventListener('click', () => { swap(false).then(() => fab.focus()); });
  input.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') { swap(false).then(() => fab.focus()); }
  });
})();
```
