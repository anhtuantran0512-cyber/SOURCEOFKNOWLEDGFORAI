---
source: "codefronts"
url: "https://codefronts.com/components/css-close-buttons/hamburger-to-x-morph-close-button/"
title: "Hamburger to X Morph Close Button"
section: "components"
category: "css-close-buttons"
category_name: "CSS Close Buttons"
description: "The most-searched icon animation on the web: three menu bars morph into an × when the fullscreen nav opens."
has_js: "true"
---

Here's a working CSS Close Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Hamburger to X Morph Close Button
Source: https://codefronts.com/components/css-close-buttons/hamburger-to-x-morph-close-button/

The most-searched icon animation on the web: three menu bars morph into an × when the fullscreen nav opens. The middle bar fades as the outer bars translate to centre THEN rotate — a two-stage transform choreographed with pure transition timing, plus the aria-expanded wiring every hamburger tutorial forgets.
## HTML
```html
<section class="ccb-08" aria-label="Hamburger to X morph demo">
  <div class="ccb-08__appbar">
    <span class="ccb-08__brand">MENU DEMO</span>
    <button class="ccb-08__burger" id="ccb-08-btn" type="button" aria-expanded="false" aria-controls="ccb-08-nav" aria-label="Open menu">
      <span class="ccb-08__bar" aria-hidden="true"></span>
      <span class="ccb-08__bar" aria-hidden="true"></span>
      <span class="ccb-08__bar" aria-hidden="true"></span>
    </button>
  </div>
  <nav class="ccb-08__nav" id="ccb-08-nav">
    <a class="ccb-08__link" href="#">Work</a>
    <a class="ccb-08__link" href="#">Studio</a>
    <a class="ccb-08__link" href="#">Contact</a>
  </nav>
</section>
```
## CSS
```css
.ccb-08,
.ccb-08 *,
.ccb-08 *::before,
.ccb-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccb-08 {
  --gap: 8px;
  --ink: oklch(0.92 0.01 270);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 0;
  padding: 48px 24px;
  background: oklch(0.18 0.025 270);
}

.ccb-08 .ccb-08__appbar {
  width: min(340px,100%);
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: oklch(0.23 0.03 270);
  border: 1px solid oklch(0.35 0.03 270 / .6);
  border-radius: 14px 14px 0 0;
  padding: 12px 12px 12px 18px;
}

.ccb-08 .ccb-08__brand {
  font: 700 12px/1 'Segoe UI',system-ui,sans-serif;
  letter-spacing: .14em;
  color: var(--ink);
}

.ccb-08 .ccb-08__burger {
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: var(--gap);
  width: 44px;
  height: 44px;
  padding: 10px;
  border: none;
  border-radius: 10px;
  background: transparent;
  cursor: pointer;
  transition: background .15s ease;
}

.ccb-08 .ccb-08__burger:hover {
  background: rgba(255,255,255,.07);
}

.ccb-08 .ccb-08__burger:focus-visible {
  outline: 2.5px solid oklch(0.7 0.15 270);
  outline-offset: 2px;
}

.ccb-08 .ccb-08__bar {
  display: block;
  width: 100%;
  height: 2px;
  border-radius: 2px;
  background: var(--ink);
  transition: transform .3s cubic-bezier(.4,0,.2,1),opacity .2s ease;
}

.ccb-08 .ccb-08__burger[aria-expanded="true"] .ccb-08__bar:nth-child(1) {
  transform: translateY(calc(var(--gap) + 2px)) rotate(45deg);
}

.ccb-08 .ccb-08__burger[aria-expanded="true"] .ccb-08__bar:nth-child(2) {
  opacity: 0;
  transform: scaleX(.4);
}

.ccb-08 .ccb-08__burger[aria-expanded="true"] .ccb-08__bar:nth-child(3) {
  transform: translateY(calc((var(--gap) + 2px) * -1)) rotate(-45deg);
}

.ccb-08 .ccb-08__nav {
  width: min(340px,100%);
  display: flex;
  flex-direction: column;
  background: oklch(0.21 0.028 270);
  border: 1px solid oklch(0.35 0.03 270 / .6);
  border-top: none;
  border-radius: 0 0 14px 14px;
  overflow: hidden;
  clip-path: inset(0 0 100% 0);
  transition: clip-path .35s cubic-bezier(.4,0,.2,1);
}

.ccb-08 .ccb-08__nav.is-open {
  clip-path: inset(0 0 0 0);
}

.ccb-08 .ccb-08__link {
  padding: 14px 18px;
  font-size: 14px;
  color: var(--ink);
  text-decoration: none;
  border-top: 1px solid oklch(0.3 0.03 270 / .5);
  transition: background .15s ease;
}

.ccb-08 .ccb-08__link:hover {
  background: rgba(255,255,255,.05);
}

.ccb-08 .ccb-08__link:focus-visible {
  outline: 2px solid oklch(0.7 0.15 270);
  outline-offset: -3px;
}

@media (prefers-reduced-motion: reduce) {
  .ccb-08 .ccb-08__bar,
    .ccb-08 .ccb-08__nav {
    transition: none;
  }
}
```

## JavaScript
```js
(() => {
  const btn = document.getElementById('ccb-08-btn'); if (!btn) return;
  const nav = document.getElementById('ccb-08-nav');
  btn.addEventListener('click', () => {
    const open = btn.getAttribute('aria-expanded') !== 'true';
    btn.setAttribute('aria-expanded', String(open));
    btn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    nav.classList.toggle('is-open', open);
  });
})();
```
