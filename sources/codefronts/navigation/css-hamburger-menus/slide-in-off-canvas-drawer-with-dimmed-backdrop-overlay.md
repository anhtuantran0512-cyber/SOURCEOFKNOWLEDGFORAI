---
source: "codefronts"
url: "https://codefronts.com/navigation/css-hamburger-menus/slide-in-off-canvas-drawer-with-dimmed-backdrop-overlay/"
title: "Slide-In Off-Canvas Drawer with Dimmed Backdrop Overlay"
section: "navigation"
category: "css-hamburger-menus"
category_name: "CSS Hamburger Menus"
description: "The app-drawer everyone means when they say 'hamburger menu': a right-hand panel that slides in on translate (never left/right offsets), over a scrim that…"
has_js: "true"
---

Here's a working CSS Hamburger Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Slide-In Off-Canvas Drawer with Dimmed Backdrop Overlay
Source: https://codefronts.com/navigation/css-hamburger-menus/slide-in-off-canvas-drawer-with-dimmed-backdrop-overlay/

The app-drawer everyone means when they say 'hamburger menu': a right-hand panel that slides in on translate (never left/right offsets), over a scrim that dims AND blurs the page behind it. The scrim is a real button — so click-outside-to-close is also keyboard- and screen-reader-closable for free — and Escape backs you out. This is the Material/iOS drawer distilled to ~60 lines of CSS.
## HTML
```html
<section class="chm-04" aria-label="Off-canvas drawer with dimmed backdrop demo">
  <div class="chm-04__stage">
    <header class="chm-04__bar">
      <span class="chm-04__brand"><i aria-hidden="true"></i>Northwind</span>
      <button class="chm-04__btn" type="button" aria-expanded="false" aria-controls="chm04-drawer" aria-label="Open menu">
        <span aria-hidden="true"><i></i><i></i><i></i></span>
      </button>
    </header>
    <div class="chm-04__content" aria-hidden="true">
      <div class="chm-04__card"></div>
      <div class="chm-04__row"><span></span><span></span></div>
      <div class="chm-04__ln" style="--w:88%"></div>
      <div class="chm-04__ln" style="--w:70%"></div>
      <div class="chm-04__ln" style="--w:79%"></div>
    </div>
    <button class="chm-04__scrim" type="button" tabindex="-1" aria-hidden="true"></button>
    <aside class="chm-04__drawer" id="chm04-drawer" aria-label="Menu">
      <header class="chm-04__dhead">
        <b>Menu</b>
        <button class="chm-04__close" type="button" aria-label="Close menu">
          <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="m6 6 12 12M18 6 6 18"/></svg>
        </button>
      </header>
      <nav class="chm-04__nav" aria-label="Primary">
        <a href="#home" style="--i:0" aria-current="page"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 11.5 12 4l9 7.5"/><path d="M5.5 10v10h13V10"/></svg>Home</a>
        <a href="#orders" style="--i:1"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4.5 7h15L18 20H6Z"/><path d="M8.5 7a3.5 3.5 0 0 1 7 0"/></svg>Orders<b>3</b></a>
        <a href="#saved" style="--i:2"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 20s-7.5-4.6-7.5-10A4.3 4.3 0 0 1 12 6.6 4.3 4.3 0 0 1 19.5 10c0 5.4-7.5 10-7.5 10Z"/></svg>Saved</a>
        <a href="#account" style="--i:3"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="8.5" r="3.5"/><path d="M5 20a7 7 0 0 1 14 0"/></svg>Account</a>
        <a href="#help" style="--i:4"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M9.6 9.4a2.5 2.5 0 1 1 3.4 3l-1 .8v1.3"/><path d="M12 17.5v.01"/></svg>Help centre</a>
      </nav>
      <footer class="chm-04__dfoot"><button type="button">Sign out</button></footer>
    </aside>
  </div>
</section>
```
## CSS
```css
.chm-04,
.chm-04 *,
.chm-04 *::before,
.chm-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.chm-04 {
  background: var(--bg);
  width: 100%;
  min-height: 100vh;
  box-sizing: border-box;
  --bg: oklch(0.98 0.004 80);
  --panel: oklch(1 0 0);
  --edge: oklch(0.9 0.008 80);
  --ink: oklch(0.25 0.015 60);
  --mut: oklch(0.55 0.015 60);
  --acc: oklch(0.62 0.15 40);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  display: grid;
  justify-content: center;
}

.chm-04__stage {
  position: relative;
  width: min(400px,88cqi,88vw);
  height: 540px;
  border-radius: 24px;
  overflow: hidden;
  background: var(--bg);
  border: 1px solid var(--edge);
  box-shadow: 0 30px 60px -35px oklch(0.35 0.04 50/.4);
}

.chm-04__bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 68px;
  padding: 0 14px 0 22px;
  background: var(--panel);
  border-bottom: 1px solid var(--edge);
}

.chm-04__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  font-weight: 700;
  font-size: 15px;
}

.chm-04__brand i {
  width: 19px;
  height: 19px;
  border-radius: 6px;
  background: conic-gradient(from 200deg,var(--acc),oklch(0.75 0.12 85));
}

.chm-04__btn {
  width: 44px;
  height: 44px;
  display: grid;
  place-items: center;
  border: none;
  border-radius: 12px;
  background: transparent;
  color: var(--ink);
  cursor: pointer;
  transition: background .2s;
}

.chm-04__btn:hover {
  background: oklch(0.95 0.008 80);
}

.chm-04__btn:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.chm-04__btn span {
  position: relative;
  width: 20px;
  height: 14px;
  display: block;
}

.chm-04__btn i {
  position: absolute;
  right: 0;
  height: 2px;
  border-radius: 2px;
  background: currentColor;
  transition: width .25s;
}

.chm-04__btn i:nth-child(1) {
  top: 0;
  width: 20px;
}

.chm-04__btn i:nth-child(2) {
  top: 6px;
  width: 14px;
}

.chm-04__btn i:nth-child(3) {
  top: 12px;
  width: 20px;
}

.chm-04__btn:hover i {
  width: 20px;
}

.chm-04__content {
  padding: 20px 22px;
  display: grid;
  gap: 14px;
}

.chm-04__card {
  height: 150px;
  border-radius: 16px;
  background: linear-gradient(140deg,oklch(0.92 0.03 60),oklch(0.88 0.05 35));
}

.chm-04__row {
  display: flex;
  gap: 12px;
}

.chm-04__row span {
  flex: 1;
  height: 72px;
  border-radius: 13px;
  background: var(--panel);
  border: 1px solid var(--edge);
}

.chm-04__ln {
  height: 11px;
  width: var(--w);
  border-radius: 99px;
  background: oklch(0.91 0.006 80);
}

.chm-04__scrim {
  position: absolute;
  inset: 0;
  z-index: 2;
  border: none;
  padding: 0;
  background: oklch(0.25 0.02 50/.45);
  backdrop-filter: blur(3px);
  opacity: 0;
  visibility: hidden;
  cursor: pointer;
  transition: opacity .35s,visibility 0s .35s;
}

[data-open] .chm-04__scrim {
  opacity: 1;
  visibility: visible;
  transition: opacity .35s,visibility 0s 0s;
}

.chm-04__drawer {
  position: absolute;
  inset: 0 0 0 auto;
  z-index: 3;
  width: min(84%,320px);
  display: flex;
  flex-direction: column;
  background: var(--panel);
  box-shadow: -24px 0 48px -24px oklch(0.25 0.03 50/.5);
  translate: 100% 0;
  visibility: hidden;
  transition: translate .4s cubic-bezier(.32,.72,.28,1),visibility 0s .4s;
}

[data-open] .chm-04__drawer {
  translate: 0 0;
  visibility: visible;
  transition: translate .4s cubic-bezier(.32,.72,.28,1),visibility 0s 0s;
}

.chm-04__dhead {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 18px 14px 14px 22px;
}

.chm-04__dhead b {
  font-size: 16px;
  letter-spacing: -.01em;
}

.chm-04__close {
  width: 40px;
  height: 40px;
  display: grid;
  place-items: center;
  border: 1px solid var(--edge);
  border-radius: 11px;
  background: var(--panel);
  color: var(--ink);
  cursor: pointer;
  transition: background .2s,rotate .3s;
}

.chm-04__close:hover {
  background: oklch(0.96 0.006 80);
  rotate: 90deg;
}

.chm-04__close:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.chm-04__nav {
  display: flex;
  flex-direction: column;
  gap: 3px;
  padding: 6px 12px;
  overflow: auto;
  overscroll-behavior: contain;
}

.chm-04__nav a {
  display: flex;
  align-items: center;
  gap: 13px;
  min-height: 48px;
  padding: 0 12px;
  border-radius: 12px;
  text-decoration: none;
  font-size: 14.5px;
  font-weight: 600;
  color: var(--mut);
  opacity: 0;
  translate: 16px 0;
  transition: background .15s,color .15s,opacity .3s,translate .35s cubic-bezier(.2,.7,.2,1);
}

[data-open] .chm-04__nav a {
  opacity: 1;
  translate: 0 0;
  transition-delay: 0s,0s,calc(.12s + var(--i)*.045s),calc(.12s + var(--i)*.045s);
}

.chm-04__nav a svg {
  width: 19px;
  height: 19px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.8;
  stroke-linecap: round;
  stroke-linejoin: round;
  flex: none;
}

.chm-04__nav a:hover {
  background: oklch(0.965 0.006 80);
  color: var(--ink);
}

.chm-04__nav a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
  color: var(--ink);
}

.chm-04__nav a[aria-current="page"] {
  color: var(--acc);
  background: color-mix(in oklch,var(--acc) 9%,transparent);
}

.chm-04__nav a b {
  margin-left: auto;
  font-size: 11px;
  font-weight: 700;
  color: oklch(1 0 0);
  background: var(--acc);
  border-radius: 99px;
  padding: 2.5px 8px;
}

.chm-04__dfoot {
  margin-top: auto;
  padding: 16px 22px;
  border-top: 1px solid var(--edge);
}

.chm-04__dfoot button {
  width: 100%;
  min-height: 44px;
  border: 1px solid var(--edge);
  border-radius: 12px;
  background: var(--bg);
  font: 600 13.5px 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  cursor: pointer;
  transition: border-color .2s;
}

.chm-04__dfoot button:hover {
  border-color: oklch(0.75 0.02 60);
}

.chm-04__dfoot button:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .chm-04 * {
    transition-duration: .01s !important;
    transition-delay: 0s !important;
  }
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.chm-04__stage').forEach(function (stage) {
    if (stage.dataset.bound) return; stage.dataset.bound = '1';
    var btn = stage.querySelector('.chm-04__btn');
    function set(open) {
      stage.toggleAttribute('data-open', open);
      btn.setAttribute('aria-expanded', String(open));
      if (open) stage.querySelector('.chm-04__close').focus();
      else btn.focus();
    }
    btn.addEventListener('click', function () { set(true); });
    stage.querySelector('.chm-04__scrim').addEventListener('click', function () { set(false); });
    stage.querySelector('.chm-04__close').addEventListener('click', function () { set(false); });
    stage.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && stage.hasAttribute('data-open')) set(false);
    });
  });
})();
```
