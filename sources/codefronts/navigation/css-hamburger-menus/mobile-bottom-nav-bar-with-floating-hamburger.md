---
source: "codefronts"
url: "https://codefronts.com/navigation/css-hamburger-menus/mobile-bottom-nav-bar-with-floating-hamburger/"
title: "Mobile Bottom Navigation Bar with Floating Hamburger Toggle"
section: "navigation"
category: "css-hamburger-menus"
category_name: "CSS Hamburger Menus"
description: "The app-store staple: a four-tab bottom bar whose center slot holds a raised floating hamburger, sitting in a real curved notch cut from the bar with a CSS…"
has_js: "true"
---

Here's a working CSS Hamburger Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Mobile Bottom Navigation Bar with Floating Hamburger Toggle
Source: https://codefronts.com/navigation/css-hamburger-menus/mobile-bottom-nav-bar-with-floating-hamburger/

The app-store staple: a four-tab bottom bar whose center slot holds a raised floating hamburger, sitting in a real curved notch cut from the bar with a CSS mask — not a fake shadow trick. Tapping it lifts a bottom sheet (grabber handle, two-column shortcut grid, staggered rise) while the disc morphs to ×. Radio-driven tabs, one small script for the sheet's ARIA. This is thumb-zone navigation: everything important within reach of one hand.
## HTML
```html
<section class="chm-21" aria-label="Bottom navigation with floating hamburger demo">
  <div class="chm-21__stage">
    <div class="chm-21__page" aria-hidden="true">
      <div class="chm-21__card"></div>
      <div class="chm-21__ln" style="--w:82%"></div>
      <div class="chm-21__ln" style="--w:64%"></div>
      <div class="chm-21__ln" style="--w:73%"></div>
    </div>
    <button class="chm-21__scrim" type="button" tabindex="-1" aria-hidden="true"></button>
    <div class="chm-21__sheet" id="chm21-sheet" aria-label="Quick actions">
      <i class="chm-21__grab" aria-hidden="true"></i>
      <div class="chm-21__grid">
        <a href="#new" style="--i:0"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 5v14M5 12h14"/></svg>New entry</a>
        <a href="#scan" style="--i:1"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 8V5.5A1.5 1.5 0 0 1 5.5 4H8M16 4h2.5A1.5 1.5 0 0 1 20 5.5V8M20 16v2.5a1.5 1.5 0 0 1-1.5 1.5H16M8 20H5.5A1.5 1.5 0 0 1 4 18.5V16M4 12h16"/></svg>Scan</a>
        <a href="#send" style="--i:2"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="m4 11 16-7-7 16-2.5-6.5Z"/></svg>Send</a>
        <a href="#archive" style="--i:3"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3.5" y="4" width="17" height="5" rx="1.5"/><path d="M5.5 9v9.5h13V9M10 13h4"/></svg>Archive</a>
      </div>
    </div>
    <div class="chm-21__dock">
      <div class="chm-21__barwrap">
        <nav class="chm-21__bar" aria-label="Tabs">
          <label class="chm-21__tab"><input type="radio" name="chm21" checked><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 11.5 12 4l9 7.5"/><path d="M5.5 10v10h13V10"/></svg><span>Home</span><i aria-hidden="true"></i></label>
          <label class="chm-21__tab"><input type="radio" name="chm21"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg><span>Search</span><i aria-hidden="true"></i></label>
          <span class="chm-21__spacer" aria-hidden="true"></span>
          <label class="chm-21__tab"><input type="radio" name="chm21"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 4h12v16l-6-4-6 4Z"/></svg><span>Saved</span><i aria-hidden="true"></i></label>
          <label class="chm-21__tab"><input type="radio" name="chm21"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="8.5" r="3.5"/><path d="M5 20a7 7 0 0 1 14 0"/></svg><span>Profile</span><i aria-hidden="true"></i></label>
        </nav>
      </div>
      <button class="chm-21__fab" type="button" aria-expanded="false" aria-controls="chm21-sheet" aria-label="Open quick actions"><span aria-hidden="true"><i></i><i></i><i></i></span></button>
    </div>
  </div>
</section>
```
## CSS
```css
.chm-21,
.chm-21 *,
.chm-21 *::before,
.chm-21 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.chm-21 {
  background: var(--bg);
  width: 100%;
  min-height: 100vh;
  box-sizing: border-box;
  --bg: oklch(0.965 0.006 250);
  --panel: oklch(1 0 0);
  --edge: oklch(0.9 0.008 250);
  --ink: oklch(0.25 0.018 260);
  --mut: oklch(0.56 0.014 260);
  --acc: oklch(0.58 0.19 285);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  display: grid;
  justify-content: center;
}

.chm-21__stage {
  position: relative;
  width: min(400px,88cqi,88vw);
  height: 560px;
  border-radius: 24px;
  overflow: hidden;
  background: var(--bg);
  border: 1px solid var(--edge);
}

.chm-21__page {
  padding: 24px;
  display: grid;
  gap: 14px;
}

.chm-21__card {
  height: 180px;
  border-radius: 18px;
  background: linear-gradient(145deg,oklch(0.9 0.03 290),oklch(0.85 0.05 265));
}

.chm-21__ln {
  height: 11px;
  width: var(--w);
  border-radius: 99px;
  background: oklch(0.9 0.007 250);
}

.chm-21__scrim {
  position: absolute;
  inset: 0;
  z-index: 2;
  border: none;
  padding: 0;
  background: oklch(0.22 0.02 265/.42);
  opacity: 0;
  visibility: hidden;
  cursor: pointer;
  transition: opacity .3s,visibility 0s .3s;
}

[data-open] .chm-21__scrim {
  opacity: 1;
  visibility: visible;
  transition-delay: 0s;
}

.chm-21__sheet {
  position: absolute;
  inset: auto 10px 96px;
  z-index: 3;
  border-radius: 22px;
  background: var(--panel);
  border: 1px solid var(--edge);
  box-shadow: 0 -18px 44px -22px oklch(0.25 0.04 270/.5);
  padding: 10px 14px 16px;
  translate: 0 calc(100% + 110px);
  visibility: hidden;
  transition: translate .45s cubic-bezier(.32,.72,.28,1),visibility 0s .45s;
}

[data-open] .chm-21__sheet {
  translate: 0 0;
  visibility: visible;
  transition: translate .45s cubic-bezier(.32,.72,.28,1),visibility 0s 0s;
}

.chm-21__grab {
  display: block;
  width: 38px;
  height: 4.5px;
  border-radius: 99px;
  background: oklch(0.87 0.008 250);
  margin: 2px auto 12px;
}

.chm-21__grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
}

.chm-21__grid a {
  display: flex;
  align-items: center;
  gap: 11px;
  min-height: 56px;
  padding: 0 16px;
  border: 1px solid var(--edge);
  border-radius: 14px;
  background: var(--bg);
  font-size: 13.5px;
  font-weight: 600;
  color: var(--ink);
  text-decoration: none;
  opacity: 0;
  translate: 0 12px;
  transition: border-color .2s,color .2s,opacity .3s,translate .35s cubic-bezier(.2,.7,.2,1);
}

[data-open] .chm-21__grid a {
  opacity: 1;
  translate: 0 0;
  transition-delay: 0s,0s,calc(.1s + var(--i)*.04s),calc(.1s + var(--i)*.04s);
}

.chm-21__grid svg {
  width: 19px;
  height: 19px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.8;
  stroke-linecap: round;
  stroke-linejoin: round;
  flex: none;
}

.chm-21__grid a:hover,
.chm-21__grid a:focus-visible {
  border-color: var(--acc);
  color: var(--acc);
}

.chm-21__grid a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.chm-21__dock {
  position: absolute;
  inset: auto 10px 10px;
  z-index: 4;
  height: 74px;
}

.chm-21__barwrap {
  position: absolute;
  inset: 0;
  filter: drop-shadow(0 14px 26px oklch(0.3 0.03 265/.28));
}

.chm-21__bar {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: stretch;
  background: var(--panel);
  border-radius: 22px;
  --notch: 37px;
  -webkit-mask: radial-gradient(circle var(--notch) at 50% 0,transparent 98%,black 100%);
  mask: radial-gradient(circle var(--notch) at 50% 0,transparent 98%,black 100%);
}

.chm-21__tab {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 3px;
  cursor: pointer;
  position: relative;
  color: var(--mut);
  transition: color .2s;
}

.chm-21__tab input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.chm-21__tab svg {
  width: 21px;
  height: 21px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.8;
  stroke-linecap: round;
  stroke-linejoin: round;
  transition: translate .25s cubic-bezier(.3,1.4,.4,1);
}

.chm-21__tab span {
  font-size: 10px;
  font-weight: 600;
}

.chm-21__tab i {
  position: absolute;
  bottom: 7px;
  width: 4px;
  height: 4px;
  border-radius: 50%;
  background: var(--acc);
  scale: 0;
  transition: scale .25s cubic-bezier(.3,1.4,.4,1);
}

.chm-21__tab:hover {
  color: var(--ink);
}

.chm-21__tab:has(:checked) {
  color: var(--acc);
}

.chm-21__tab:has(:checked) svg {
  translate: 0 -2px;
}

.chm-21__tab:has(:checked) i {
  scale: 1;
}

.chm-21__tab:has(:focus-visible) {
  outline: 2px solid var(--acc);
  outline-offset: -4px;
  border-radius: 14px;
}

.chm-21__spacer {
  flex: 0 0 72px;
}

.chm-21__fab {
  position: absolute;
  left: 50%;
  top: -26px;
  translate: -50% 0;
  width: 56px;
  height: 56px;
  border: none;
  border-radius: 50%;
  background: linear-gradient(150deg,var(--acc),oklch(0.5 0.19 300));
  color: oklch(1 0 0);
  cursor: pointer;
  display: grid;
  place-items: center;
  box-shadow: 0 14px 28px -10px color-mix(in oklch,var(--acc) 65%,transparent);
  transition: scale .2s,box-shadow .25s;
}

.chm-21__fab:hover {
  scale: 1.06;
}

.chm-21__fab:active {
  scale: .93;
}

.chm-21__fab:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.chm-21__fab span {
  position: relative;
  width: 18px;
  height: 12px;
  display: block;
}

.chm-21__fab i {
  position: absolute;
  left: 0;
  width: 18px;
  height: 2px;
  border-radius: 2px;
  background: currentColor;
  transition: translate .3s,rotate .3s .05s,opacity .2s;
}

.chm-21__fab i:nth-child(1) {
  top: 0;
}

.chm-21__fab i:nth-child(2) {
  top: 5px;
}

.chm-21__fab i:nth-child(3) {
  top: 10px;
}

[data-open] .chm-21__fab i:nth-child(1) {
  translate: 0 5px;
  rotate: 45deg;
}

[data-open] .chm-21__fab i:nth-child(2) {
  opacity: 0;
}

[data-open] .chm-21__fab i:nth-child(3) {
  translate: 0 -5px;
  rotate: -45deg;
}

@media (prefers-reduced-motion: reduce) {
  .chm-21 * {
    transition-duration: .01s !important;
    transition-delay: 0s !important;
  }
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.chm-21__stage').forEach(function (stage) {
    if (stage.dataset.bound) return; stage.dataset.bound = '1';
    var fab = stage.querySelector('.chm-21__fab');
    function set(open) {
      stage.toggleAttribute('data-open', open);
      fab.setAttribute('aria-expanded', String(open));
      fab.setAttribute('aria-label', open ? 'Close quick actions' : 'Open quick actions');
    }
    fab.addEventListener('click', function () { set(fab.getAttribute('aria-expanded') !== 'true'); });
    stage.querySelector('.chm-21__scrim').addEventListener('click', function () { set(false); });
    stage.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && stage.hasAttribute('data-open')) { set(false); fab.focus(); }
    });
  });
})();
```
