---
source: "codefronts"
url: "https://codefronts.com/components/css-floating-buttons/accessible-wai-aria-floating-action-button-wcag-2-2/"
title: "Accessible WAI-ARIA Floating Action Button (WCAG 2.2)"
section: "components"
category: "css-floating-buttons"
category_name: "CSS Floating Buttons"
description: "A FAB menu that passes an actual audit."
has_js: "true"
---

Here's a working CSS Floating Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Accessible WAI-ARIA Floating Action Button (WCAG 2.2)
Source: https://codefronts.com/components/css-floating-buttons/accessible-wai-aria-floating-action-button-wcag-2-2/

A FAB menu that passes an actual audit. It implements the ARIA menu-button pattern properly: roving tabindex, Arrow/Home/End navigation, Escape to close with focus restored, type-ahead by first letter, a live region announcing the chosen action, 44px targets, a focus ring that survives high-contrast mode, and no target obscured by the floating layer. Every rule here maps to a real failure I have watched people hit.
## HTML
```html
<section class="fb-05" aria-label="Accessible floating action button demo">
  <div class="fb-05__page">
    <p class="fb-05__eyebrow">menu button pattern · roving tabindex</p>
    <h2 class="fb-05__title">Tab to it. Then use the arrows.</h2>
    <p class="fb-05__sub">Enter or Space or Arrow&nbsp;Up opens the menu and focuses the first item. Arrows move, Home/End jump, first letter type-ahead works, Escape closes and returns focus to the button.</p>
    <ul class="fb-05__keys">
      <li><kbd>Tab</kbd> reach the button</li><li><kbd>↑</kbd><kbd>↓</kbd> move</li><li><kbd>Home</kbd><kbd>End</kbd> jump</li><li><kbd>Esc</kbd> close</li>
    </ul>
    <p class="fb-05__live" id="fb-05-live" role="status" aria-live="polite">No action taken yet.</p>
  </div>
  <div class="fb-05__scrim" id="fb-05-scrim" hidden></div>
  <div class="fb-05__dock">
    <ul class="fb-05__menu" id="fb-05-menu" role="menu" aria-label="Quick actions" hidden>
      <li role="none"><button class="fb-05__item" role="menuitem" type="button" tabindex="-1" data-fb-act="New document"><span class="fb-05__iBox" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><path d="M6 3h8l4 4v14H6z" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linejoin="round"/><path d="M14 3v5h4" fill="none" stroke="currentColor" stroke-width="1.9"/></svg></span>New document</button></li>
      <li role="none"><button class="fb-05__item" role="menuitem" type="button" tabindex="-1" data-fb-act="Upload file"><span class="fb-05__iBox" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><path d="M12 17V6M8 10l4-4 4 4" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/><path d="M5 19h14" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg></span>Upload file</button></li>
      <li role="none"><button class="fb-05__item" role="menuitem" type="button" tabindex="-1" data-fb-act="Invite teammate"><span class="fb-05__iBox" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><circle cx="10" cy="8" r="3.4" fill="none" stroke="currentColor" stroke-width="1.9"/><path d="M4 19c0-3.3 2.7-5 6-5s6 1.7 6 5" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/><path d="M19 8v6M16 11h6" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg></span>Invite teammate</button></li>
      <li role="none"><button class="fb-05__item" role="menuitem" type="button" tabindex="-1" data-fb-act="Start recording"><span class="fb-05__iBox" aria-hidden="true"><circle cx="12" cy="12" r="5" fill="currentColor"/><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="1.7"/></svg></span>Start recording</button></li>
    </ul>
    <button class="fb-05__fab" id="fb-05-fab" type="button" aria-expanded="false" aria-haspopup="true" aria-controls="fb-05-menu" aria-label="Quick actions">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 5v14M5 12h14" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg>
    </button>
  </div>
</section>
```
## CSS
```css
.fb-05 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--fb-05-bg);
  --fb-05-bg: oklch(0.98 0.008 250);
  --fb-05-brand: oklch(0.48 0.19 262);
  --fb-05-brandDeep: oklch(0.38 0.17 262);
  --fb-05-ink: oklch(0.21 0.02 260);
  --fb-05-mut: oklch(0.5 0.02 260);
  --fb-05-card: oklch(1 0 0);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--fb-05-ink);
  position: relative;
  display: grid;
  place-items: center;
  padding: clamp(20px,5vw,56px);
  overflow: hidden;
}

.fb-05 *,
.fb-05 *::before,
.fb-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fb-05__page {
  width: min(100%,58ch);
  display: grid;
  gap: 13px;
  justify-items: center;
  text-align: center;
  z-index: 1;
}

.fb-05__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--fb-05-brand);
}

.fb-05__title {
  font-size: clamp(26px,4.6vw,44px);
  line-height: 1.05;
  letter-spacing: -.03em;
  font-weight: 700;
  text-wrap: balance;
}

.fb-05__sub {
  font-size: clamp(13.5px,1.7vw,16.5px);
  line-height: 1.62;
  color: var(--fb-05-mut);
  text-wrap: pretty;
}

.fb-05__keys {
  list-style: none;
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  justify-content: center;
  font-size: 12px;
  color: var(--fb-05-mut);
}

.fb-05__keys li {
  display: flex;
  align-items: center;
  gap: 5px;
  background: var(--fb-05-card);
  border: 1px solid oklch(0.21 0.02 260/.12);
  border-radius: 99px;
  padding: 6px 12px;
}

.fb-05 kbd {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  background: oklch(0.94 0.008 260);
  border: 1px solid oklch(0.21 0.02 260/.16);
  border-bottom-width: 2px;
  border-radius: 5px;
  padding: 1px 5px;
  color: var(--fb-05-ink);
}

.fb-05__live {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  color: var(--fb-05-brandDeep);
  background: oklch(0.48 0.19 262/.08);
  border: 1px dashed oklch(0.48 0.19 262/.35);
  border-radius: 12px;
  padding: 9px 15px;
  min-height: 36px;
  display: grid;
  place-items: center;
}

.fb-05__scrim {
  position: absolute;
  inset: 0;
  z-index: 4;
  background: oklch(0.21 0.02 260/.42);
  -webkit-backdrop-filter: blur(2px);
  backdrop-filter: blur(2px);
  animation: fb-05-fade .2s ease;
}

.fb-05__scrim[hidden] {
  display: none;
}

@keyframes fb-05-fade {
  from {
    opacity: 0;
  }
}

.fb-05__dock {
  position: absolute;
  right: clamp(16px,3vw,32px);
  bottom: calc(clamp(16px,3vw,32px) + env(safe-area-inset-bottom));
  z-index: 5;
  display: grid;
  justify-items: end;
  gap: 14px;
}

.fb-05__menu {
  list-style: none;
  display: grid;
  gap: 9px;
  justify-items: end;
}

.fb-05__menu[hidden] {
  display: none;
}

.fb-05__item {
  display: flex;
  align-items: center;
  gap: 11px;
  min-height: 48px;
  padding: 0 18px 0 10px;
  border: 1px solid oklch(0.21 0.02 260/.1);
  border-radius: 99px;
  background: var(--fb-05-card);
  color: var(--fb-05-ink);
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  box-shadow: 0 10px 26px -14px oklch(0.21 0.02 260/.7);
  animation: fb-05-rise .26s cubic-bezier(.2,.9,.3,1.1) backwards;
  transition: transform .18s ease,background .18s ease;
}

.fb-05__menu li:nth-child(1) .fb-05__item {
  animation-delay: .02s;
}

.fb-05__menu li:nth-child(2) .fb-05__item {
  animation-delay: .06s;
}

.fb-05__menu li:nth-child(3) .fb-05__item {
  animation-delay: .1s;
}

.fb-05__menu li:nth-child(4) .fb-05__item {
  animation-delay: .14s;
}

@keyframes fb-05-rise {
  from {
    opacity: 0;
    transform: translateY(14px) scale(.94);
  }
}

.fb-05__item:hover {
  background: oklch(0.96 0.01 262);
  transform: translateX(-2px);
}

.fb-05__item:focus-visible,
.fb-05__fab:focus-visible {
  outline: 3px solid var(--fb-05-brandDeep);
  outline-offset: 3px;
  box-shadow: 0 0 0 6px oklch(1 0 0/.9),0 10px 26px -14px oklch(0.21 0.02 260/.7);
}

.fb-05__iBox {
  flex: none;
  width: 34px;
  height: 34px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  background: oklch(0.48 0.19 262/.1);
  color: var(--fb-05-brandDeep);
}

.fb-05__iBox svg {
  width: 20px;
  height: 20px;
}

.fb-05__fab {
  display: grid;
  place-items: center;
  inline-size: 60px;
  block-size: 60px;
  border: 0;
  border-radius: 20px;
  cursor: pointer;
  color: oklch(0.99 0.01 262);
  background: linear-gradient(150deg,oklch(0.56 0.2 268),var(--fb-05-brandDeep));
  box-shadow: 0 12px 30px -10px oklch(0.38 0.17 262/.8),0 2px 6px oklch(0.3 0.1 262/.28);
  transition: transform .28s cubic-bezier(.2,1.3,.4,1),border-radius .28s ease;
}

.fb-05__fab svg {
  width: 26px;
  height: 26px;
  transition: rotate .3s cubic-bezier(.3,1.4,.4,1);
}

.fb-05__fab:hover {
  transform: translateY(-2px);
}

.fb-05__fab:active {
  transform: scale(.94);
}

.fb-05__fab[aria-expanded="true"] {
  border-radius: 50%;
}

.fb-05__fab[aria-expanded="true"] svg {
  rotate: 135deg;
}

@media (forced-colors: active) {
  .fb-05__item,
    .fb-05__fab {
    border: 1px solid ButtonText;
  }
}

@media (prefers-reduced-motion: reduce) {
  .fb-05 * {
    animation: none !important;
    transition: none !important;
  }
}
```

## JavaScript
```js
(() => {
  const fab = document.getElementById('fb-05-fab');
  const menu = document.getElementById('fb-05-menu');
  const scrim = document.getElementById('fb-05-scrim');
  const live = document.getElementById('fb-05-live');
  if (!fab || !menu || fab.dataset.fbWired) return;
  fab.dataset.fbWired = '1';
  const items = [...menu.querySelectorAll('.fb-05__item')];
  let active = 0;
  const focusAt = (i) => {
    active = (i + items.length) % items.length;
    items.forEach((el, n) => { el.tabIndex = n === active ? 0 : -1; });
    items[active].focus();
  };
  const open = (fromEnd) => {
    fab.setAttribute('aria-expanded', 'true');
    menu.hidden = false; scrim.hidden = false;
    focusAt(fromEnd ? items.length - 1 : 0);
  };
  const close = (restore) => {
    fab.setAttribute('aria-expanded', 'false');
    menu.hidden = true; scrim.hidden = true;
    if (restore) fab.focus();
  };
  const isOpen = () => fab.getAttribute('aria-expanded') === 'true';
  fab.addEventListener('click', () => (isOpen() ? close(false) : open(false)));
  fab.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowUp') { e.preventDefault(); open(true); }
    if (e.key === 'ArrowDown') { e.preventDefault(); open(false); }
  });
  scrim.addEventListener('click', () => close(true));
  menu.addEventListener('keydown', (e) => {
    const k = e.key;
    if (k === 'ArrowDown') { e.preventDefault(); focusAt(active + 1); }
    else if (k === 'ArrowUp') { e.preventDefault(); focusAt(active - 1); }
    else if (k === 'Home') { e.preventDefault(); focusAt(0); }
    else if (k === 'End') { e.preventDefault(); focusAt(items.length - 1); }
    else if (k === 'Escape') { e.preventDefault(); close(true); }
    else if (k === 'Tab') { close(false); }
    else if (k.length === 1 && /\S/.test(k)) {
      const from = active + 1;
      const found = items.findIndex((el, n) => n >= from && el.textContent.trim().toLowerCase().startsWith(k.toLowerCase()));
      const wrap = found > -1 ? found : items.findIndex((el) => el.textContent.trim().toLowerCase().startsWith(k.toLowerCase()));
      if (wrap > -1) focusAt(wrap);
    }
  });
  items.forEach((el) => el.addEventListener('click', () => {
    live.textContent = el.dataset.fbAct + ' — action fired at ' + new Date().toLocaleTimeString();
    close(true);
  }));
})();
```
