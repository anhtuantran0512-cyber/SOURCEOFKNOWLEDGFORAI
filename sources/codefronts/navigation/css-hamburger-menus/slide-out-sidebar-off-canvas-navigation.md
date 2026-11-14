---
source: "codefronts"
url: "https://codefronts.com/navigation/css-hamburger-menus/slide-out-sidebar-off-canvas-navigation/"
title: "CSS Slide Out Sidebar Navigation / Off Canvas Menu"
section: "navigation"
category: "css-hamburger-menus"
category_name: "CSS Hamburger Menus"
description: "The workhorse app sidebar, structured the way real products need it: grouped sections with sticky-feeling headers (Workspace / Library / Support), icon+label…"
has_js: "true"
---

Here's a working CSS Hamburger Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Slide Out Sidebar Navigation / Off Canvas Menu
Source: https://codefronts.com/navigation/css-hamburger-menus/slide-out-sidebar-off-canvas-navigation/

The workhorse app sidebar, structured the way real products need it: grouped sections with sticky-feeling headers (Workspace / Library / Support), icon+label rows with an active indicator bar, a keyboard-shortcut hint column, and a user card pinned to the bottom. Slides over content from the left with a soft scrim, and the section groups cascade in with micro-delays so the panel feels assembled, not dumped.
## HTML
```html
<section class="chm-12" aria-label="Slide out sidebar navigation demo">
  <div class="chm-12__stage">
    <header class="chm-12__bar">
      <button class="chm-12__btn" type="button" aria-expanded="false" aria-controls="chm12-drawer" aria-label="Open navigation"><span aria-hidden="true"><i></i><i></i><i></i></span></button>
      <strong>Tessera</strong>
      <span class="chm-12__crumb" aria-hidden="true">/ Q3 planning</span>
    </header>
    <div class="chm-12__content" aria-hidden="true">
      <div class="chm-12__block"></div>
      <div class="chm-12__two"><span></span><span></span></div>
      <div class="chm-12__ln" style="--w2:78%"></div>
      <div class="chm-12__ln" style="--w2:62%"></div>
    </div>
    <button class="chm-12__scrim" type="button" tabindex="-1" aria-hidden="true"></button>
    <aside class="chm-12__drawer" id="chm12-drawer" aria-label="Navigation">
      <header class="chm-12__dhead">
        <span class="chm-12__logo" aria-hidden="true">T</span>
        <b>Tessera</b>
        <button class="chm-12__close" type="button" aria-label="Close navigation"><svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="m6 6 12 12M18 6 6 18"/></svg></button>
      </header>
      <nav class="chm-12__nav" aria-label="Primary">
        <div class="chm-12__group" style="--g:0">
          <span class="chm-12__cap">Workspace</span>
          <a href="#board" aria-current="page"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3.5" y="3.5" width="7.5" height="10" rx="1.5"/><rect x="13" y="3.5" width="7.5" height="6" rx="1.5"/><rect x="13" y="11.5" width="7.5" height="9" rx="1.5"/><rect x="3.5" y="15.5" width="7.5" height="5" rx="1.5"/></svg>Board<kbd aria-hidden="true">⌘1</kbd></a>
          <a href="#timeline"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3.5 6h11M3.5 12h17M3.5 18h8"/><circle cx="18" cy="6" r="2"/><circle cx="15" cy="18" r="2"/></svg>Timeline<kbd aria-hidden="true">⌘2</kbd></a>
          <a href="#backlog"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 6h16M4 12h16M4 18h16"/><circle cx="4" cy="6" r="1.4"/><circle cx="4" cy="12" r="1.4"/><circle cx="4" cy="18" r="1.4"/></svg>Backlog<b class="chm-12__count">24</b></a>
        </div>
        <div class="chm-12__group" style="--g:1">
          <span class="chm-12__cap">Library</span>
          <a href="#docs"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5.5 4h9l4 4v12h-13Z"/><path d="M14 4v4.5h4.5"/></svg>Documents</a>
          <a href="#assets"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3.5" y="5" width="17" height="14" rx="2"/><circle cx="9" cy="10.5" r="1.8"/><path d="m3.5 16.5 5-4 4 3.5 3-2.5 5 3.5"/></svg>Assets</a>
          <a href="#reports"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 20V9M12 20V4M19 20v-7"/></svg>Reports</a>
        </div>
        <div class="chm-12__group" style="--g:2">
          <span class="chm-12__cap">Support</span>
          <a href="#help"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M9.6 9.4a2.5 2.5 0 1 1 3.4 3l-1 .8v1.3M12 17.5v.01"/></svg>Help &amp; docs</a>
          <a href="#invite"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="10" cy="8.5" r="3.5"/><path d="M3.5 20a6.5 6.5 0 0 1 13 0M18 8v6M15 11h6"/></svg>Invite team</a>
        </div>
      </nav>
      <footer class="chm-12__user">
        <span class="chm-12__ava" aria-hidden="true">MK</span>
        <span class="chm-12__who"><b>Mara Kade</b><small>[email protected]</small></span>
        <button type="button" aria-label="Account options">⋯</button>
      </footer>
    </aside>
  </div>
</section>
```
## CSS
```css
.chm-12,
.chm-12 *,
.chm-12 *::before,
.chm-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.chm-12 {
  background: var(--bg);
  width: 100%;
  min-height: 100vh;
  box-sizing: border-box;
  --w: 288px;
  --bg: oklch(0.975 0.004 250);
  --edge: oklch(0.9 0.008 250);
  --ink: oklch(0.25 0.015 255);
  --mut: oklch(0.55 0.012 255);
  --dark: oklch(0.21 0.022 262);
  --dedge: oklch(0.3 0.025 262);
  --dink: oklch(0.93 0.008 260);
  --dmut: oklch(0.66 0.02 260);
  --acc: oklch(0.73 0.14 175);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  display: grid;
  justify-content: center;
}

.chm-12__stage {
  position: relative;
  width: min(420px,88cqi,88vw);
  height: 560px;
  border-radius: 24px;
  overflow: hidden;
  background: var(--bg);
  border: 1px solid var(--edge);
}

.chm-12__bar {
  display: flex;
  align-items: center;
  gap: 12px;
  height: 64px;
  padding: 0 16px;
  background: oklch(1 0 0);
  border-bottom: 1px solid var(--edge);
}

.chm-12__bar strong {
  font-size: 15px;
  letter-spacing: -.01em;
}

.chm-12__crumb {
  font-size: 13px;
  color: var(--mut);
}

.chm-12__btn {
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

.chm-12__btn:hover {
  background: oklch(0.95 0.006 250);
}

.chm-12__btn:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.chm-12__btn span {
  position: relative;
  width: 19px;
  height: 13px;
  display: block;
}

.chm-12__btn i {
  position: absolute;
  left: 0;
  height: 2px;
  border-radius: 2px;
  background: currentColor;
  transition: width .25s;
}

.chm-12__btn i:nth-child(1) {
  top: 0;
  width: 19px;
}

.chm-12__btn i:nth-child(2) {
  top: 5.5px;
  width: 13px;
}

.chm-12__btn i:nth-child(3) {
  top: 11px;
  width: 16px;
}

.chm-12__btn:hover i {
  width: 19px;
}

.chm-12__content {
  padding: 18px;
  display: grid;
  gap: 13px;
}

.chm-12__block {
  height: 160px;
  border-radius: 15px;
  background: linear-gradient(145deg,oklch(0.92 0.02 190),oklch(0.88 0.035 165));
}

.chm-12__two {
  display: flex;
  gap: 12px;
}

.chm-12__two span {
  flex: 1;
  height: 78px;
  border-radius: 13px;
  background: oklch(1 0 0);
  border: 1px solid var(--edge);
}

.chm-12__ln {
  height: 11px;
  width: var(--w2);
  border-radius: 99px;
  background: oklch(0.91 0.006 250);
}

.chm-12__scrim {
  position: absolute;
  inset: 0;
  z-index: 2;
  border: none;
  padding: 0;
  background: oklch(0.2 0.02 260/.4);
  opacity: 0;
  visibility: hidden;
  cursor: pointer;
  transition: opacity .32s,visibility 0s .32s;
}

[data-open] .chm-12__scrim {
  opacity: 1;
  visibility: visible;
  transition-delay: 0s;
}

.chm-12__drawer {
  position: absolute;
  inset: 0 auto 0 0;
  z-index: 3;
  width: min(88%,var(--w));
  display: grid;
  grid-template-rows: auto 1fr auto;
  background: var(--dark);
  color: var(--dink);
  box-shadow: 24px 0 48px -22px oklch(0.15 0.03 262/.6);
  translate: -102% 0;
  visibility: hidden;
  transition: translate .42s cubic-bezier(.32,.72,.28,1),visibility 0s .42s;
}

[data-open] .chm-12__drawer {
  translate: 0 0;
  visibility: visible;
  transition: translate .42s cubic-bezier(.32,.72,.28,1),visibility 0s 0s;
}

.chm-12__dhead {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 18px 14px 14px 18px;
}

.chm-12__logo {
  width: 28px;
  height: 28px;
  border-radius: 9px;
  display: grid;
  place-items: center;
  font-size: 13px;
  font-weight: 800;
  color: oklch(0.15 0.02 262);
  background: linear-gradient(140deg,var(--acc),oklch(0.6 0.12 210));
}

.chm-12__dhead b {
  font-size: 15px;
}

.chm-12__close {
  margin-left: auto;
  width: 38px;
  height: 38px;
  display: grid;
  place-items: center;
  border: 1px solid var(--dedge);
  border-radius: 10px;
  background: transparent;
  color: var(--dmut);
  cursor: pointer;
  transition: color .2s,border-color .2s;
}

.chm-12__close:hover {
  color: var(--dink);
  border-color: oklch(0.42 0.03 262);
}

.chm-12__close:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.chm-12__nav {
  overflow: auto;
  min-height: 0;
  overscroll-behavior: contain;
  padding: 6px 12px 14px;
}

.chm-12__group + .chm-12__group {
  margin-top: 18px;
}

.chm-12__cap {
  display: block;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: oklch(0.52 0.02 262);
  padding: 0 10px 7px;
}

.chm-12__nav a {
  position: relative;
  display: flex;
  align-items: center;
  gap: 12px;
  min-height: 44px;
  padding: 0 10px 0 14px;
  border-radius: 10px;
  text-decoration: none;
  font-size: 13.5px;
  font-weight: 600;
  color: var(--dmut);
  opacity: 0;
  translate: -14px 0;
  transition: background .15s,color .15s,opacity .3s,translate .35s cubic-bezier(.2,.7,.2,1);
}

[data-open] .chm-12__nav a {
  opacity: 1;
  translate: 0 0;
  transition-delay: 0s,0s,calc(.1s + var(--g)*.06s),calc(.1s + var(--g)*.06s);
}

.chm-12__nav a::before {
  content: "";
  position: absolute;
  left: 2px;
  top: 20%;
  width: 3.5px;
  height: 60%;
  border-radius: 99px;
  background: var(--acc);
  scale: 1 0;
  transition: scale .25s;
}

.chm-12__nav a svg {
  width: 18px;
  height: 18px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
  flex: none;
}

.chm-12__nav a:hover {
  color: var(--dink);
  background: oklch(1 0 0/.06);
}

.chm-12__nav a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
  color: var(--dink);
}

.chm-12__nav a[aria-current="page"] {
  color: var(--dink);
  background: oklch(1 0 0/.07);
}

.chm-12__nav a[aria-current="page"]::before {
  scale: 1 1;
}

.chm-12__nav a[aria-current="page"] svg {
  stroke: var(--acc);
}

.chm-12__nav kbd {
  margin-left: auto;
  font: 600 10px ui-monospace,Menlo,Consolas,monospace;
  color: oklch(0.55 0.02 262);
  border: 1px solid var(--dedge);
  border-radius: 5px;
  padding: 2px 6px;
}

.chm-12__count {
  margin-left: auto;
  font-size: 10.5px;
  font-weight: 700;
  color: oklch(0.15 0.02 262);
  background: var(--acc);
  border-radius: 99px;
  padding: 2px 7px;
}

.chm-12__user {
  display: flex;
  align-items: center;
  gap: 11px;
  padding: 13px 14px;
  border-top: 1px solid var(--dedge);
}

.chm-12__ava {
  width: 34px;
  height: 34px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  font-size: 11.5px;
  font-weight: 700;
  color: oklch(0.15 0.02 262);
  background: linear-gradient(140deg,oklch(0.75 0.12 90),var(--acc));
}

.chm-12__who {
  display: grid;
  line-height: 1.25;
}

.chm-12__who b {
  font-size: 13px;
}

.chm-12__who small {
  font-size: 11px;
  color: var(--dmut);
}

.chm-12__user button {
  margin-left: auto;
  width: 36px;
  height: 36px;
  border: none;
  border-radius: 9px;
  background: transparent;
  color: var(--dmut);
  font-size: 16px;
  cursor: pointer;
  transition: background .2s,color .2s;
}

.chm-12__user button:hover {
  background: oklch(1 0 0/.07);
  color: var(--dink);
}

.chm-12__user button:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .chm-12 * {
    transition-duration: .01s !important;
    transition-delay: 0s !important;
  }
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.chm-12__stage').forEach(function (stage) {
    if (stage.dataset.bound) return; stage.dataset.bound = '1';
    var btn = stage.querySelector('.chm-12__btn');
    function set(open) {
      stage.toggleAttribute('data-open', open);
      btn.setAttribute('aria-expanded', String(open));
      if (open) stage.querySelector('.chm-12__close').focus();
      else btn.focus();
    }
    btn.addEventListener('click', function () { set(true); });
    stage.querySelector('.chm-12__scrim').addEventListener('click', function () { set(false); });
    stage.querySelector('.chm-12__close').addEventListener('click', function () { set(false); });
    stage.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && stage.hasAttribute('data-open')) set(false);
    });
  });
})();
```
