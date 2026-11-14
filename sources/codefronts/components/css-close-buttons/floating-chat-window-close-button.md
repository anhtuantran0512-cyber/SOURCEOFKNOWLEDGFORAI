---
source: "codefronts"
url: "https://codefronts.com/components/css-close-buttons/floating-chat-window-close-button/"
title: "Floating Chat Window Close Button"
section: "components"
category: "css-close-buttons"
category_name: "CSS Close Buttons"
description: "The Intercom/Zendesk/Drift launcher pattern: a fixed floating bubble whose speech-balloon icon rotates and cross-fades into an × when the chat panel opens,…"
has_js: "true"
---

Here's a working CSS Close Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Floating Chat Window Close Button
Source: https://codefronts.com/components/css-close-buttons/floating-chat-window-close-button/

The Intercom/Zendesk/Drift launcher pattern: a fixed floating bubble whose speech-balloon icon rotates and cross-fades into an × when the chat panel opens, then back on close. One button, two states, both drawn in pure CSS — the icon swap is a transform crossfade, and the panel's presence is a single aria-expanded toggle.
## HTML
```html
<section class="ccb-04" aria-label="Floating chat close button demo">
  <div class="ccb-04__stage">
    <div class="ccb-04__panel" id="ccb-04-panel" hidden>
      <p class="ccb-04__msg">Hi there 👋 How can we help?</p>
    </div>
    <button class="ccb-04__fab" id="ccb-04-fab" type="button" aria-expanded="false" aria-controls="ccb-04-panel" aria-label="Open chat">
      <span class="ccb-04__bubble" aria-hidden="true"></span>
      <span class="ccb-04__x" aria-hidden="true"></span>
    </button>
  </div>
</section>
```
## CSS
```css
.ccb-04,
.ccb-04 *,
.ccb-04 *::before,
.ccb-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccb-04 {
  --brand-a: oklch(0.6 0.19 280);
  --brand-b: oklch(0.5 0.2 300);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(180deg,oklch(0.97 0.008 280),oklch(0.93 0.02 290));
}

.ccb-04 .ccb-04__stage {
  position: relative;
  width: min(300px,100%);
  height: 220px;
  display: flex;
  align-items: flex-end;
  justify-content: flex-end;
}

.ccb-04 .ccb-04__panel {
  position: absolute;
  bottom: 74px;
  inset-inline-end: 0;
  width: 230px;
  background: #fff;
  border-radius: 16px 16px 4px 16px;
  padding: 18px;
  box-shadow: 0 20px 46px -22px oklch(0.4 0.12 290 / .55);
  transform: translateY(8px);
  opacity: 0;
  transition: transform .25s ease,opacity .25s ease;
}

.ccb-04 .ccb-04__panel.is-open {
  transform: none;
  opacity: 1;
}

.ccb-04 .ccb-04__msg {
  font-size: 14px;
  line-height: 1.5;
  color: oklch(0.35 0.02 290);
}

.ccb-04 .ccb-04__fab {
  display: grid;
  place-items: center;
  width: 60px;
  height: 60px;
  border: none;
  border-radius: 50%;
  background: linear-gradient(140deg,var(--brand-a),var(--brand-b));
  cursor: pointer;
  box-shadow: 0 14px 30px -12px oklch(0.5 0.2 290 / .7);
  transition: transform .2s ease;
}

.ccb-04 .ccb-04__fab:hover {
  transform: translateY(-2px);
}

.ccb-04 .ccb-04__fab:active {
  transform: scale(.93);
}

.ccb-04 .ccb-04__fab:focus-visible {
  outline: 3px solid var(--brand-a);
  outline-offset: 3px;
}

.ccb-04 .ccb-04__bubble,
.ccb-04 .ccb-04__x {
  grid-area: 1/1;
  position: relative;
  width: 24px;
  height: 24px;
  transition: transform .25s ease,opacity .25s ease;
}

.ccb-04 .ccb-04__bubble::before {
  content: "";
  position: absolute;
  inset: 2px 0 6px;
  border-radius: 8px;
  background: #fff;
}

.ccb-04 .ccb-04__bubble::after {
  content: "";
  position: absolute;
  bottom: 1px;
  left: 5px;
  width: 8px;
  height: 8px;
  background: #fff;
  clip-path: polygon(0 0,100% 0,0 100%);
}

.ccb-04 .ccb-04__x::before,
.ccb-04 .ccb-04__x::after {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  width: 18px;
  height: 2.5px;
  border-radius: 2px;
  background: #fff;
}

.ccb-04 .ccb-04__x::before {
  transform: translate(-50%,-50%) rotate(45deg);
}

.ccb-04 .ccb-04__x::after {
  transform: translate(-50%,-50%) rotate(-45deg);
}

.ccb-04 .ccb-04__x {
  transform: rotate(-90deg) scale(.4);
  opacity: 0;
}

.ccb-04 .ccb-04__fab[aria-expanded="true"] .ccb-04__bubble {
  transform: rotate(90deg) scale(.4);
  opacity: 0;
}

.ccb-04 .ccb-04__fab[aria-expanded="true"] .ccb-04__x {
  transform: none;
  opacity: 1;
}

@media (prefers-reduced-motion: reduce) {
  .ccb-04 .ccb-04__fab,
    .ccb-04 .ccb-04__bubble,
    .ccb-04 .ccb-04__x,
    .ccb-04 .ccb-04__panel {
    transition: none;
  }
}
```

## JavaScript
```js
(() => {
  const fab = document.getElementById('ccb-04-fab'); if (!fab) return;
  const panel = document.getElementById('ccb-04-panel');
  fab.addEventListener('click', () => {
    const open = fab.getAttribute('aria-expanded') !== 'true';
    fab.setAttribute('aria-expanded', String(open));
    fab.setAttribute('aria-label', open ? 'Close chat' : 'Open chat');
    panel.hidden = false;                       // keep in DOM for the exit transition
    requestAnimationFrame(() => panel.classList.toggle('is-open', open));
    if (!open) setTimeout(() => { panel.hidden = true; }, 250);
  });
})();
```
