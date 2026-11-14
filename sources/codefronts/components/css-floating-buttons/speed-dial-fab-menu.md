---
source: "codefronts"
url: "https://codefronts.com/components/css-floating-buttons/speed-dial-fab-menu/"
title: "Vertical and Horizontal Speed Dial FAB Menu CSS"
section: "components"
category: "css-floating-buttons"
category_name: "CSS Floating Buttons"
description: "One speed dial, four directions."
has_js: "true"
---

Here's a working CSS Floating Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Vertical and Horizontal Speed Dial FAB Menu CSS
Source: https://codefronts.com/components/css-floating-buttons/speed-dial-fab-menu/

One speed dial, four directions. The same markup expands up, down, left or right by changing a single data-dir attribute — flex-direction and transform-origin follow from it, and the stagger reverses so items always animate away from the button. Includes the layout logic for when to pick each direction, which matters more than the animation.
## HTML
```html
<section class="fb-10" aria-label="Vertical and horizontal speed dial demo">
  <div class="fb-10__page">
    <p class="fb-10__eyebrow">one dial · four directions</p>
    <h2 class="fb-10__title">Direction is an attribute</h2>
    <p class="fb-10__sub">Pick an axis, then open the dial. Same markup, same stagger logic, flex-direction does the work.</p>
    <div class="fb-10__seg" role="group" aria-label="Dial direction">
      <button class="fb-10__segBtn is-on" type="button" data-fb-dir="up" aria-pressed="true">Up</button>
      <button class="fb-10__segBtn" type="button" data-fb-dir="left" aria-pressed="false">Left</button>
      <button class="fb-10__segBtn" type="button" data-fb-dir="down" aria-pressed="false">Down</button>
      <button class="fb-10__segBtn" type="button" data-fb-dir="right" aria-pressed="false">Right</button>
    </div>
    <p class="fb-10__chip" id="fb-10-chip">data-dir="up" · column-reverse · stagger 0→3</p>
  </div>
  <div class="fb-10__dock" id="fb-10-dock" data-dir="up" data-open="false">
    <ul class="fb-10__items" id="fb-10-items">
      <li style="--fb-10-i:0"><button class="fb-10__item" type="button" tabindex="-1" aria-label="Share"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="18" cy="5.5" r="2.6" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="6" cy="12" r="2.6" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="18" cy="18.5" r="2.6" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M8.4 10.8l7.2-3.9M8.4 13.2l7.2 3.9" stroke="currentColor" stroke-width="1.8"/></svg></button></li>
      <li style="--fb-10-i:1"><button class="fb-10__item" type="button" tabindex="-1" aria-label="Duplicate"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><rect x="8" y="8" width="12" height="12" rx="2.4" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M16 5.5A2.5 2.5 0 0 0 13.5 4h-7A2.5 2.5 0 0 0 4 6.5v7A2.5 2.5 0 0 0 5.5 16" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg></button></li>
      <li style="--fb-10-i:2"><button class="fb-10__item" type="button" tabindex="-1" aria-label="Pin"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M9 3h6l-1 6 4 3v2H6v-2l4-3z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><path d="M12 14v7" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg></button></li>
      <li style="--fb-10-i:3"><button class="fb-10__item fb-10__item--danger" type="button" tabindex="-1" aria-label="Delete"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M5 7h14M9 7V5h6v2M7 7l1 13h8l1-13" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></button></li>
    </ul>
    <button class="fb-10__fab" id="fb-10-fab" type="button" aria-expanded="false" aria-controls="fb-10-items" aria-label="Open actions">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 5v14M5 12h14" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg>
    </button>
  </div>
</section>
```
## CSS
```css
.fb-10 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--fb-10-bg);
  --fb-10-bg: oklch(0.96 0.01 240);
  --fb-10-brand: oklch(0.5 0.15 250);
  --fb-10-brandDeep: oklch(0.38 0.14 252);
  --fb-10-ink: oklch(0.23 0.02 250);
  --fb-10-mut: oklch(0.53 0.02 250);
  --fb-10-card: oklch(1 0 0);
  --fb-10-off: 16px;
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--fb-10-ink);
  position: relative;
  padding: clamp(20px,5vw,56px);
  overflow: hidden;
}

.fb-10 *,
.fb-10 *::before,
.fb-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fb-10__page {
  width: min(100%,54ch);
  display: grid;
  gap: 14px;
  justify-items: center;
  text-align: center;
}

.fb-10__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--fb-10-brand);
}

.fb-10__title {
  font-size: clamp(26px,4.6vw,44px);
  line-height: 1.05;
  letter-spacing: -.03em;
  font-weight: 700;
  text-wrap: balance;
}

.fb-10__sub {
  font-size: clamp(13.5px,1.7vw,16.5px);
  line-height: 1.62;
  color: var(--fb-10-mut);
  text-wrap: pretty;
}

.fb-10__seg {
  display: flex;
  flex-wrap: wrap;
  gap: 4px;
  padding: 5px;
  border-radius: 99px;
  background: var(--fb-10-card);
  border: 1px solid oklch(0.23 0.02 250/.1);
  box-shadow: 0 6px 20px -14px oklch(0.23 0.02 250/.8);
}

.fb-10__segBtn {
  min-height: 40px;
  padding: 0 18px;
  border: 0;
  border-radius: 99px;
  background: transparent;
  color: var(--fb-10-mut);
  font-size: 13.5px;
  font-weight: 620;
  cursor: pointer;
  transition: background .18s ease,color .18s ease;
}

.fb-10__segBtn:hover {
  background: oklch(0.5 0.15 250/.08);
  color: var(--fb-10-ink);
}

.fb-10__segBtn.is-on {
  background: var(--fb-10-brand);
  color: oklch(0.99 0.01 250);
}

.fb-10__segBtn:focus-visible {
  outline: 2.5px solid var(--fb-10-brandDeep);
  outline-offset: 2px;
}

.fb-10__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--fb-10-mut);
  padding: 8px 14px;
  border: 1px solid oklch(0.23 0.02 250/.14);
  border-radius: 99px;
}

.fb-10__dock {
  position: absolute;
  z-index: 5;
  display: flex;
  align-items: center;
  gap: 14px;
}

.fb-10__dock[data-dir="up"] {
  inset: auto clamp(20px,5vw,52px) calc(clamp(20px,5vw,52px) + env(safe-area-inset-bottom)) auto;
  flex-direction: column-reverse;
}

.fb-10__dock[data-dir="down"] {
  inset: clamp(20px,5vw,52px) clamp(20px,5vw,52px) auto auto;
  flex-direction: column;
}

.fb-10__dock[data-dir="left"] {
  inset: auto clamp(20px,5vw,52px) calc(clamp(20px,5vw,52px) + env(safe-area-inset-bottom)) auto;
  flex-direction: row-reverse;
}

.fb-10__dock[data-dir="right"] {
  inset: auto auto calc(clamp(20px,5vw,52px) + env(safe-area-inset-bottom)) clamp(20px,5vw,52px);
  flex-direction: row;
}

.fb-10__items {
  list-style: none;
  display: flex;
  gap: 12px;
  align-items: center;
}

.fb-10__dock[data-dir="up"] .fb-10__items {
  flex-direction: column-reverse;
}

.fb-10__dock[data-dir="down"] .fb-10__items {
  flex-direction: column;
}

.fb-10__dock[data-dir="left"] .fb-10__items {
  flex-direction: row-reverse;
}

.fb-10__dock[data-dir="right"] .fb-10__items {
  flex-direction: row;
}

.fb-10__items li {
  display: grid;
}

.fb-10__item {
  display: grid;
  place-items: center;
  inline-size: 48px;
  block-size: 48px;
  border: 1px solid oklch(0.23 0.02 250/.08);
  border-radius: 50%;
  background: var(--fb-10-card);
  color: var(--fb-10-brandDeep);
  cursor: pointer;
  box-shadow: 0 10px 24px -14px oklch(0.23 0.02 250/.9);
  opacity: 0;
  scale: .4;
  pointer-events: none;
  transition: opacity .22s ease,scale .3s cubic-bezier(.2,1.35,.4,1),translate .3s cubic-bezier(.2,1.2,.4,1),background .18s ease,color .18s ease;
  transition-delay: calc((3 - var(--fb-10-i)) * 40ms);
}

.fb-10__item svg {
  width: 21px;
  height: 21px;
}

.fb-10__dock[data-dir="up"] .fb-10__item {
  translate: 0 var(--fb-10-off);
}

.fb-10__dock[data-dir="down"] .fb-10__item {
  translate: 0 calc(var(--fb-10-off) * -1);
}

.fb-10__dock[data-dir="left"] .fb-10__item {
  translate: var(--fb-10-off) 0;
}

.fb-10__dock[data-dir="right"] .fb-10__item {
  translate: calc(var(--fb-10-off) * -1) 0;
}

.fb-10__dock[data-open="true"] .fb-10__item {
  opacity: 1;
  scale: 1;
  translate: 0 0;
  pointer-events: auto;
  transition-delay: calc(var(--fb-10-i) * 50ms);
}

.fb-10__item:hover {
  background: var(--fb-10-brand);
  color: oklch(0.99 0.01 250);
}

.fb-10__item--danger:hover {
  background: oklch(0.58 0.21 25);
}

.fb-10__item:focus-visible {
  outline: 3px solid var(--fb-10-brandDeep);
  outline-offset: 3px;
}

.fb-10__item:active {
  scale: .9;
}

.fb-10__fab {
  flex: none;
  display: grid;
  place-items: center;
  inline-size: 60px;
  block-size: 60px;
  border: 0;
  border-radius: 50%;
  cursor: pointer;
  color: oklch(0.99 0.01 250);
  background: linear-gradient(150deg,oklch(0.58 0.16 248),var(--fb-10-brandDeep));
  box-shadow: 0 12px 30px -10px oklch(0.38 0.14 252/.85),0 2px 6px oklch(0.3 0.08 252/.3);
  transition: transform .28s cubic-bezier(.2,1.3,.4,1);
}

.fb-10__fab svg {
  width: 26px;
  height: 26px;
  transition: rotate .32s cubic-bezier(.3,1.35,.4,1);
}

.fb-10__fab:hover {
  transform: scale(1.05);
}

.fb-10__fab:active {
  transform: scale(.93);
}

.fb-10__fab:focus-visible {
  outline: 3px solid var(--fb-10-brandDeep);
  outline-offset: 4px;
}

.fb-10__fab[aria-expanded="true"] svg {
  rotate: 45deg;
}

@media (prefers-reduced-motion: reduce) {
  .fb-10 * {
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  const dock = document.getElementById('fb-10-dock');
  const fab = document.getElementById('fb-10-fab');
  const chip = document.getElementById('fb-10-chip');
  if (!dock || !fab || fab.dataset.fbWired) return;
  fab.dataset.fbWired = '1';
  const items = [...dock.querySelectorAll('.fb-10__item')];
  const flexMap = { up: 'column-reverse', down: 'column', left: 'row-reverse', right: 'row' };
  const set = (open) => {
    dock.dataset.open = String(open);
    fab.setAttribute('aria-expanded', String(open));
    fab.setAttribute('aria-label', open ? 'Close actions' : 'Open actions');
    items.forEach((i) => { i.tabIndex = open ? 0 : -1; });
  };
  fab.addEventListener('click', () => set(dock.dataset.open !== 'true'));
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && dock.dataset.open === 'true') { set(false); fab.focus(); }
  });
  document.querySelectorAll('.fb-10__segBtn').forEach((btn) => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.fb-10__segBtn').forEach((b) => {
        b.classList.toggle('is-on', b === btn);
        b.setAttribute('aria-pressed', String(b === btn));
      });
      dock.dataset.dir = btn.dataset.fbDir;
      chip.textContent = 'data-dir="' + btn.dataset.fbDir + '" · ' + flexMap[btn.dataset.fbDir] + ' · stagger 0→3';
    });
  });
})();
```
