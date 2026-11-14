---
source: "codefronts"
url: "https://codefronts.com/navigation/css-hamburger-menus/css-push-page-navigation-menu-off-canvas-content-shift/"
title: "CSS Push Page Navigation Menu (Off-Canvas Content Shift)"
section: "navigation"
category: "css-hamburger-menus"
category_name: "CSS Hamburger Menus"
description: "Instead of layering a drawer OVER the page, the whole #site-canvas glides aside to reveal the menu resting beneath it — the page becomes a physical sheet you…"
has_js: "true"
---

Here's a working CSS Hamburger Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Push Page Navigation Menu (Off-Canvas Content Shift)
Source: https://codefronts.com/navigation/css-hamburger-menus/css-push-page-navigation-menu-off-canvas-content-shift/

Instead of layering a drawer OVER the page, the whole #site-canvas glides aside to reveal the menu resting beneath it — the page becomes a physical sheet you slide off a shelf. One transform on one wrapper does all the work; the menu never moves at all. This build adds the 2026 finish: the canvas shrinks 6%, picks up a corner radius and a deep shadow, so the page visibly becomes an object floating above the nav layer.
## HTML
```html
<section class="chm-08" aria-label="Push page off-canvas navigation demo">
  <div class="chm-08__viewport">
    <nav class="chm-08__menu" id="chm08-menu" aria-label="Site">
      <b class="chm-08__hello" style="--i:0">Good evening, Ash</b>
      <a href="#today" style="--i:1" aria-current="page"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2 2M19.1 4.9 17 7M7 17l-2.1 2.1"/></svg>Today</a>
      <a href="#inbox" style="--i:2"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 13h5l2 3h4l2-3h5"/><path d="M5 5h14l2 8v6H3v-6Z"/></svg>Inbox<b>7</b></a>
      <a href="#projects" style="--i:3"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3.5" y="5" width="17" height="15" rx="2.5"/><path d="M3.5 10h17M9 5V3.5M15 5V3.5"/></svg>Projects</a>
      <a href="#notes" style="--i:4"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 4h11l3 3v13H5Z"/><path d="M15.5 4v3.5H19M8.5 12h7M8.5 16h5"/></svg>Notes</a>
      <a href="#settings" style="--i:5"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="3"/><path d="M12 2.5v3M12 18.5v3M2.5 12h3M18.5 12h3M5 5l2 2M17 17l2 2M19 5l-2 2M7 17l-2 2"/></svg>Settings</a>
      <span class="chm-08__ver" style="--i:6">v4.2 · push-canvas pattern</span>
    </nav>
    <div class="chm-08__canvas" id="chm08-canvas">
      <header class="chm-08__bar">
        <button class="chm-08__btn" type="button" aria-expanded="false" aria-controls="chm08-menu" aria-label="Open menu"><span aria-hidden="true"><i></i><i></i><i></i></span></button>
        <strong>Daybook</strong>
        <span class="chm-08__avatar" aria-hidden="true">A</span>
      </header>
      <div class="chm-08__content" aria-hidden="true">
        <div class="chm-08__big"></div>
        <div class="chm-08__ln" style="--w:83%"></div>
        <div class="chm-08__ln" style="--w:64%"></div>
        <div class="chm-08__ln" style="--w:71%"></div>
        <div class="chm-08__two"><span></span><span></span></div>
      </div>
    </div>
    <button class="chm-08__catch" type="button" tabindex="-1" aria-hidden="true"></button>
  </div>
</section>
```
## CSS
```css
.chm-08,
.chm-08 *,
.chm-08 *::before,
.chm-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.chm-08 {
  background: var(--bg);
  width: 100%;
  min-height: 100vh;
  box-sizing: border-box;
  --w: 270px;
  --bg: oklch(0.2 0.035 280);
  --page: oklch(0.98 0.004 260);
  --edge: oklch(0.9 0.008 260);
  --ink: oklch(0.25 0.02 265);
  --mut: oklch(0.55 0.015 265);
  --acc: oklch(0.7 0.16 300);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  display: grid;
  justify-content: center;
}

.chm-08__viewport {
  position: relative;
  width: min(400px,88cqi,88vw);
  height: 540px;
  border-radius: 24px;
  overflow: hidden;
  background: radial-gradient(120% 100% at 0% 100%,oklch(0.26 0.06 300/.6),transparent 55%),var(--bg);
  border: 1px solid oklch(0.32 0.04 280);
}

.chm-08__menu {
  position: absolute;
  inset: 0 auto 0 0;
  width: var(--w);
  padding: 30px 22px;
  display: flex;
  flex-direction: column;
  gap: 4px;
  color: oklch(0.93 0.01 280);
}

.chm-08__hello {
  font-size: 17px;
  letter-spacing: -.01em;
  margin-bottom: 18px;
}

.chm-08__menu a {
  display: flex;
  align-items: center;
  gap: 12px;
  min-height: 46px;
  padding: 0 12px;
  margin: 0 -12px;
  border-radius: 12px;
  text-decoration: none;
  font-size: 14.5px;
  font-weight: 600;
  color: oklch(0.75 0.025 285);
  transition: background .2s,color .2s;
}

.chm-08__menu a svg {
  width: 19px;
  height: 19px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
  flex: none;
}

.chm-08__menu a:hover,
.chm-08__menu a:focus-visible {
  color: oklch(0.97 0.008 285);
  background: oklch(1 0 0/.07);
}

.chm-08__menu a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
}

.chm-08__menu a[aria-current="page"] {
  color: oklch(0.97 0.008 285);
  background: color-mix(in oklch,var(--acc) 22%,transparent);
}

.chm-08__menu a b {
  margin-left: auto;
  font-size: 10.5px;
  font-weight: 700;
  background: var(--acc);
  color: oklch(0.15 0.03 300);
  border-radius: 99px;
  padding: 2px 7px;
}

.chm-08__ver {
  margin-top: auto;
  font-size: 11px;
  color: oklch(0.6 0.03 285);
}

.chm-08__menu a,
.chm-08__hello,
.chm-08__ver {
  translate: -26px 0;
  opacity: .4;
  transition: translate .5s cubic-bezier(.32,.72,.28,1),opacity .4s,background .2s,color .2s;
}

[data-open] .chm-08__menu a,
[data-open] .chm-08__hello,
[data-open] .chm-08__ver {
  translate: 0 0;
  opacity: 1;
  transition-delay: calc(var(--i)*.035s);
}

.chm-08__canvas {
  position: relative;
  z-index: 1;
  height: 100%;
  background: var(--page);
  display: flex;
  flex-direction: column;
  transition: translate .5s cubic-bezier(.32,.72,.28,1),scale .5s cubic-bezier(.32,.72,.28,1),border-radius .5s,box-shadow .5s;
}

[data-open] .chm-08__canvas {
  translate: min(var(--w),76%) 0;
  scale: .94;
  border-radius: 22px;
  box-shadow: -30px 24px 60px -20px oklch(0.12 0.04 280/.6);
}

.chm-08__bar {
  display: flex;
  align-items: center;
  gap: 12px;
  height: 64px;
  padding: 0 16px;
  border-bottom: 1px solid var(--edge);
}

.chm-08__bar strong {
  font-size: 15px;
  letter-spacing: -.01em;
}

.chm-08__btn {
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

.chm-08__btn:hover {
  background: oklch(0.94 0.008 265);
}

.chm-08__btn:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.chm-08__btn span {
  position: relative;
  width: 19px;
  height: 13px;
  display: block;
}

.chm-08__btn i {
  position: absolute;
  left: 0;
  width: 19px;
  height: 2px;
  border-radius: 2px;
  background: currentColor;
  transition: translate .3s,rotate .3s .05s,opacity .2s;
}

.chm-08__btn i:nth-child(1) {
  top: 0;
}

.chm-08__btn i:nth-child(2) {
  top: 5.5px;
}

.chm-08__btn i:nth-child(3) {
  top: 11px;
}

[data-open] .chm-08__btn i:nth-child(1) {
  translate: 0 5.5px;
  rotate: 45deg;
}

[data-open] .chm-08__btn i:nth-child(2) {
  opacity: 0;
}

[data-open] .chm-08__btn i:nth-child(3) {
  translate: 0 -5.5px;
  rotate: -45deg;
}

.chm-08__avatar {
  margin-left: auto;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  font-size: 12px;
  font-weight: 700;
  color: oklch(1 0 0);
  background: linear-gradient(140deg,var(--acc),oklch(0.55 0.18 260));
}

.chm-08__content {
  flex: 1;
  padding: 20px;
  display: grid;
  gap: 13px;
  align-content: start;
}

.chm-08__big {
  height: 150px;
  border-radius: 16px;
  background: linear-gradient(140deg,oklch(0.93 0.02 290),oklch(0.88 0.045 310));
}

.chm-08__ln {
  height: 11px;
  width: var(--w);
  border-radius: 99px;
  background: oklch(0.92 0.006 265);
}

.chm-08__two {
  display: flex;
  gap: 12px;
}

.chm-08__two span {
  flex: 1;
  height: 84px;
  border-radius: 14px;
  background: oklch(1 0 0);
  border: 1px solid var(--edge);
}

.chm-08__catch {
  position: absolute;
  inset: 0 0 0 var(--w);
  z-index: 5;
  display: none;
  border: none;
  background: transparent;
  cursor: w-resize;
}

[data-open] .chm-08__catch {
  display: block;
}

@media (prefers-reduced-motion: reduce) {
  .chm-08 * {
    transition-duration: .01s !important;
    transition-delay: 0s !important;
  }
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.chm-08__viewport').forEach(function (vp) {
    if (vp.dataset.bound) return; vp.dataset.bound = '1';
    var btn = vp.querySelector('.chm-08__btn'), canvas = vp.querySelector('.chm-08__canvas');
    function set(open) {
      vp.toggleAttribute('data-open', open);
      btn.setAttribute('aria-expanded', String(open));
      if (open) { canvas.setAttribute('inert', ''); vp.querySelector('.chm-08__menu a').focus(); }
      else { canvas.removeAttribute('inert'); btn.focus(); }
    }
    btn.addEventListener('click', function () { set(true); });
    vp.querySelector('.chm-08__catch').addEventListener('click', function () { set(false); });
    vp.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && vp.hasAttribute('data-open')) set(false);
    });
  });
})();
```
