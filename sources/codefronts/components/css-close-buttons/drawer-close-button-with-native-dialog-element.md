---
source: "codefronts"
url: "https://codefronts.com/components/css-close-buttons/drawer-close-button-with-native-dialog-element/"
title: "Drawer Close Button with Native dialog Element"
section: "components"
category: "css-close-buttons"
category_name: "CSS Close Buttons"
description: "The platform-native pattern every 2026 tutorial should teach: a slide-in side drawer built on the real <dialog> element, so focus trapping, Esc-to-close,…"
has_js: "true"
---

Here's a working CSS Close Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Drawer Close Button with Native dialog Element
Source: https://codefronts.com/components/css-close-buttons/drawer-close-button-with-native-dialog-element/

The platform-native pattern every 2026 tutorial should teach: a slide-in side drawer built on the real <dialog> element, so focus trapping, Esc-to-close, top-layer stacking and ::backdrop come FREE from the browser. The close button just calls dialog.close() — and @starting-style animates the entry without a single class toggle.
## HTML
```html
<section class="ccb-10" aria-label="Native dialog drawer close demo">
  <button class="ccb-10__open" id="ccb-10-open" type="button">Open drawer</button>
  <dialog class="ccb-10__drawer" id="ccb-10-drawer" aria-labelledby="ccb-10-title">
    <header class="ccb-10__head">
      <h3 class="ccb-10__title" id="ccb-10-title">Filters</h3>
      <button class="ccb-10__close" id="ccb-10-close" type="button" aria-label="Close drawer" autofocus>
        <span class="ccb-10__x" aria-hidden="true"></span>
      </button>
    </header>
    <p class="ccb-10__text">Esc, the ×, or a backdrop click all close me — the browser does the focus trap.</p>
  </dialog>
</section>
```
## CSS
```css
.ccb-10,
.ccb-10 *,
.ccb-10 *::before,
.ccb-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccb-10 {
  --w: 300px;
  --accent: oklch(0.6 0.15 220);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(180deg,oklch(0.96 0.008 220),oklch(0.92 0.015 225));
}

.ccb-10 .ccb-10__open {
  font: 600 14px/1 'Segoe UI',system-ui,sans-serif;
  color: #fff;
  background: var(--accent);
  border: none;
  border-radius: 12px;
  padding: 14px 22px;
  cursor: pointer;
  box-shadow: 0 12px 26px -12px oklch(0.5 0.15 220 / .7);
  transition: transform .15s ease;
}

.ccb-10 .ccb-10__open:hover {
  transform: translateY(-1px);
}

.ccb-10 .ccb-10__open:active {
  transform: scale(.97);
}

.ccb-10 .ccb-10__open:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

.ccb-10 .ccb-10__drawer {
  position: fixed;
  inset: 0 0 0 auto;
  width: min(var(--w),85vw);
  height: 100dvh;
  max-height: none;
  border: none;
  border-inline-start: 1px solid oklch(0.88 0.01 220);
  background: #fff;
  padding: 22px;
  box-shadow: -24px 0 60px -30px oklch(0.35 0.06 225 / .5);
  transition: translate .35s cubic-bezier(.4,0,.2,1),display .35s allow-discrete,overlay .35s allow-discrete;
  translate: 0 0;
}

.ccb-10 .ccb-10__drawer:not([open]) {
  translate: 100% 0;
}

@starting-style {
  .ccb-10 .ccb-10__drawer[open] {
    translate: 100% 0;
  }
}

.ccb-10 .ccb-10__drawer::backdrop {
  background: oklch(0.25 0.03 240 / .35);
  backdrop-filter: blur(3px);
}

.ccb-10 .ccb-10__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  margin-bottom: 14px;
}

.ccb-10 .ccb-10__title {
  font-size: 16px;
  color: oklch(0.3 0.02 225);
}

.ccb-10 .ccb-10__text {
  font-size: 13.5px;
  line-height: 1.55;
  color: oklch(0.5 0.02 225);
}

.ccb-10 .ccb-10__close {
  position: relative;
  display: grid;
  place-items: center;
  width: 40px;
  height: 40px;
  border: none;
  border-radius: 10px;
  background: oklch(0.95 0.008 220);
  cursor: pointer;
  transition: background .15s ease;
}

.ccb-10 .ccb-10__close:hover {
  background: oklch(0.91 0.015 220);
}

.ccb-10 .ccb-10__close:active {
  transform: scale(.93);
}

.ccb-10 .ccb-10__close:focus-visible {
  outline: 2.5px solid var(--accent);
  outline-offset: 2px;
}

.ccb-10 .ccb-10__x {
  position: relative;
  width: 16px;
  height: 16px;
}

.ccb-10 .ccb-10__x::before,
.ccb-10 .ccb-10__x::after {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  width: 16px;
  height: 2px;
  border-radius: 2px;
  background: oklch(0.4 0.02 225);
}

.ccb-10 .ccb-10__x::before {
  transform: translate(-50%,-50%) rotate(45deg);
}

.ccb-10 .ccb-10__x::after {
  transform: translate(-50%,-50%) rotate(-45deg);
}

@media (prefers-reduced-motion: reduce) {
  .ccb-10 .ccb-10__drawer,
    .ccb-10 .ccb-10__close,
    .ccb-10 .ccb-10__open {
    transition: none;
  }
}
```

## JavaScript
```js
(() => {
  const drawer = document.getElementById('ccb-10-drawer'); if (!drawer) return;
  document.getElementById('ccb-10-open').addEventListener('click', () => drawer.showModal());
  document.getElementById('ccb-10-close').addEventListener('click', () => drawer.close());
  drawer.addEventListener('click', (e) => {           // light dismiss: click on the backdrop closes
    if (e.target === drawer) drawer.close();
  });
})();
```
