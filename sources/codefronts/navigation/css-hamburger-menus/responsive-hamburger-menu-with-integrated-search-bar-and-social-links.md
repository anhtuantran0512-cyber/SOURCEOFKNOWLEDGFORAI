---
source: "codefronts"
url: "https://codefronts.com/navigation/css-hamburger-menus/responsive-hamburger-menu-with-integrated-search-bar-and-social-links/"
title: "Responsive Hamburger Menu with Integrated Search Bar & Social Links"
section: "navigation"
category: "css-hamburger-menus"
category_name: "CSS Hamburger Menus"
description: "The publisher/e-commerce drawer that has to carry a whole header's worth of jobs: a real search field that auto-focuses on open, primary nav with item…"
has_js: "true"
---

Here's a working CSS Hamburger Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Responsive Hamburger Menu with Integrated Search Bar & Social Links
Source: https://codefronts.com/navigation/css-hamburger-menus/responsive-hamburger-menu-with-integrated-search-bar-and-social-links/

The publisher/e-commerce drawer that has to carry a whole header's worth of jobs: a real search field that auto-focuses on open, primary nav with item counts, a New badge, a social row of inline-SVG icons, and a newsletter CTA pinned to the bottom. The layout lesson is the drawer's internal grid — search fixed at top, nav scrolls in the middle, socials+CTA anchored at the bottom — so content growth never pushes actions off-screen.
## HTML
```html
<section class="chm-06" aria-label="Hamburger menu with search and social links demo">
  <div class="chm-06__stage">
    <header class="chm-06__bar">
      <button class="chm-06__btn" type="button" aria-expanded="false" aria-controls="chm06-drawer" aria-label="Open menu"><span aria-hidden="true"><i></i><i></i><i></i></span></button>
      <span class="chm-06__brand">KIOSK<i>daily</i></span>
      <span class="chm-06__cart" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><path d="M4.5 7h15L18 20H6Z"/><path d="M8.5 7a3.5 3.5 0 0 1 7 0"/></svg><b>2</b></span>
    </header>
    <div class="chm-06__content" aria-hidden="true">
      <div class="chm-06__hero"></div>
      <div class="chm-06__ln" style="--w:86%"></div>
      <div class="chm-06__ln" style="--w:64%"></div>
    </div>
    <button class="chm-06__scrim" type="button" tabindex="-1" aria-hidden="true"></button>
    <aside class="chm-06__drawer" id="chm06-drawer" aria-label="Menu">
      <div class="chm-06__top">
        <form class="chm-06__search" role="search">
          <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
          <input type="search" placeholder="Search stories, topics…" aria-label="Search">
        </form>
        <button class="chm-06__close" type="button" aria-label="Close menu"><svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="m6 6 12 12M18 6 6 18"/></svg></button>
      </div>
      <nav class="chm-06__nav" aria-label="Sections">
        <a href="#latest">Latest<span>128</span></a>
        <a href="#tech">Technology<span>41</span></a>
        <a href="#design">Design<span>27</span></a>
        <a href="#culture">Culture<b class="chm-06__new">New</b></a>
        <a href="#podcasts">Podcasts<span>12</span></a>
        <a href="#archive">Archive</a>
      </nav>
      <footer class="chm-06__foot">
        <div class="chm-06__social">
          <a href="#x" aria-label="Follow on X"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 4l7.2 9.3L4.4 20h2.1l5.6-5.5L16.8 20H20l-7.5-9.7L18.9 4h-2.1l-5.2 5.1L7.2 4H4Z"/></svg></a>
          <a href="#instagram" aria-label="Follow on Instagram"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3.5" y="3.5" width="17" height="17" rx="4.5" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="12" cy="12" r="4" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="17.2" cy="6.8" r="1.3"/></svg></a>
          <a href="#youtube" aria-label="Subscribe on YouTube"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="2.5" y="6" width="19" height="12" rx="3.5" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M10.5 9.8v4.4l4-2.2Z"/></svg></a>
          <a href="#rss" aria-label="RSS feed"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 19a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"/><path d="M4 11a9 9 0 0 1 9 9M4 5a15 15 0 0 1 15 15" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></a>
        </div>
        <button class="chm-06__cta" type="button">Get the newsletter</button>
      </footer>
    </aside>
  </div>
</section>
```
## CSS
```css
.chm-06,
.chm-06 *,
.chm-06 *::before,
.chm-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.chm-06 {
  background: var(--bg);
  width: 100%;
  min-height: 100vh;
  box-sizing: border-box;
  --bg: oklch(0.975 0.006 70);
  --panel: oklch(1 0 0);
  --edge: oklch(0.89 0.01 70);
  --ink: oklch(0.23 0.015 50);
  --mut: oklch(0.54 0.015 50);
  --acc: oklch(0.6 0.19 25);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  display: grid;
  justify-content: center;
}

.chm-06__stage {
  position: relative;
  width: min(400px,88cqi,88vw);
  height: 560px;
  border-radius: 24px;
  overflow: hidden;
  background: var(--bg);
  border: 1px solid var(--edge);
}

.chm-06__bar {
  display: flex;
  align-items: center;
  gap: 12px;
  height: 66px;
  padding: 0 18px;
  background: var(--panel);
  border-bottom: 1px solid var(--edge);
}

.chm-06__btn {
  width: 44px;
  height: 44px;
  margin-left: -8px;
  display: grid;
  place-items: center;
  border: none;
  border-radius: 12px;
  background: transparent;
  color: var(--ink);
  cursor: pointer;
  transition: background .2s;
}

.chm-06__btn:hover {
  background: oklch(0.955 0.008 70);
}

.chm-06__btn:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.chm-06__btn span {
  position: relative;
  width: 20px;
  height: 14px;
  display: block;
}

.chm-06__btn i {
  position: absolute;
  left: 0;
  width: 20px;
  height: 2px;
  background: currentColor;
  border-radius: 2px;
}

.chm-06__btn i:nth-child(1) {
  top: 0;
}

.chm-06__btn i:nth-child(2) {
  top: 6px;
}

.chm-06__btn i:nth-child(3) {
  top: 12px;
}

.chm-06__brand {
  font-size: 17px;
  font-weight: 800;
  letter-spacing: .14em;
}

.chm-06__brand i {
  font-style: normal;
  font-weight: 400;
  letter-spacing: 0;
  color: var(--acc);
}

.chm-06__cart {
  position: relative;
  margin-left: auto;
  color: var(--ink);
}

.chm-06__cart b {
  position: absolute;
  top: -7px;
  right: -9px;
  font-size: 9.5px;
  font-weight: 700;
  color: oklch(1 0 0);
  background: var(--acc);
  border-radius: 99px;
  padding: 1.5px 5.5px;
}

.chm-06__content {
  padding: 18px;
  display: grid;
  gap: 13px;
}

.chm-06__hero {
  height: 180px;
  border-radius: 14px;
  background: linear-gradient(145deg,oklch(0.9 0.03 50),oklch(0.85 0.055 25));
}

.chm-06__ln {
  height: 11px;
  width: var(--w);
  border-radius: 99px;
  background: oklch(0.9 0.008 70);
}

.chm-06__scrim {
  position: absolute;
  inset: 0;
  z-index: 2;
  border: none;
  padding: 0;
  background: oklch(0.22 0.02 40/.42);
  backdrop-filter: blur(2px);
  opacity: 0;
  visibility: hidden;
  cursor: pointer;
  transition: opacity .3s,visibility 0s .3s;
}

[data-open] .chm-06__scrim {
  opacity: 1;
  visibility: visible;
  transition-delay: 0s;
}

.chm-06__drawer {
  position: absolute;
  inset: 0 auto 0 0;
  z-index: 3;
  width: min(88%,330px);
  display: grid;
  grid-template-rows: auto 1fr auto;
  background: var(--panel);
  box-shadow: 24px 0 48px -24px oklch(0.25 0.03 40/.45);
  translate: -102% 0;
  visibility: hidden;
  transition: translate .42s cubic-bezier(.32,.72,.28,1),visibility 0s .42s;
}

[data-open] .chm-06__drawer {
  translate: 0 0;
  visibility: visible;
  transition: translate .42s cubic-bezier(.32,.72,.28,1),visibility 0s 0s;
}

.chm-06__top {
  display: flex;
  gap: 10px;
  align-items: center;
  padding: 16px 16px 12px;
}

.chm-06__search {
  flex: 1;
  display: flex;
  align-items: center;
  gap: 9px;
  min-height: 44px;
  padding: 0 14px;
  border: 1.5px solid var(--edge);
  border-radius: 12px;
  color: var(--mut);
  transition: border-color .2s;
}

.chm-06__search:focus-within {
  border-color: var(--acc);
  color: var(--acc);
}

.chm-06__search input {
  flex: 1;
  min-width: 0;
  border: none;
  outline: none;
  background: transparent;
  font: 14px 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.chm-06__close {
  width: 44px;
  height: 44px;
  flex: none;
  display: grid;
  place-items: center;
  border: 1.5px solid var(--edge);
  border-radius: 12px;
  background: var(--panel);
  color: var(--ink);
  cursor: pointer;
  transition: background .2s;
}

.chm-06__close:hover {
  background: oklch(0.96 0.006 70);
}

.chm-06__close:focus-visible,
.chm-06__cta:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.chm-06__nav {
  overflow: auto;
  min-height: 0;
  overscroll-behavior: contain;
  display: flex;
  flex-direction: column;
  padding: 4px 10px;
}

.chm-06__nav a {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  min-height: 50px;
  padding: 0 12px;
  border-radius: 11px;
  text-decoration: none;
  font-size: 15.5px;
  font-weight: 700;
  letter-spacing: -.01em;
  color: var(--ink);
  transition: background .15s,color .15s;
}

.chm-06__nav a:hover {
  background: oklch(0.965 0.008 70);
  color: var(--acc);
}

.chm-06__nav a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
}

.chm-06__nav span {
  font-size: 11.5px;
  font-weight: 600;
  color: var(--mut);
  font-variant-numeric: tabular-nums;
}

.chm-06__new {
  font-size: 10px;
  font-weight: 800;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: oklch(1 0 0);
  background: var(--acc);
  border-radius: 99px;
  padding: 3px 8px;
}

.chm-06__foot {
  padding: 14px 16px 18px;
  border-top: 1px solid var(--edge);
  display: grid;
  gap: 12px;
}

.chm-06__social {
  display: flex;
  gap: 8px;
}

.chm-06__social a {
  width: 44px;
  height: 44px;
  display: grid;
  place-items: center;
  border: 1.5px solid var(--edge);
  border-radius: 12px;
  color: var(--ink);
  transition: border-color .2s,color .2s,translate .15s;
}

.chm-06__social a svg {
  width: 18px;
  height: 18px;
  fill: currentColor;
}

.chm-06__social a:hover,
.chm-06__social a:focus-visible {
  border-color: var(--acc);
  color: var(--acc);
  translate: 0 -2px;
}

.chm-06__social a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.chm-06__cta {
  min-height: 48px;
  border: none;
  border-radius: 12px;
  background: var(--ink);
  color: oklch(0.97 0.005 70);
  font: 700 14px 'Segoe UI',system-ui,sans-serif;
  cursor: pointer;
  transition: background .2s;
}

.chm-06__cta:hover {
  background: var(--acc);
}

@media (prefers-reduced-motion: reduce) {
  .chm-06 * {
    transition-duration: .01s !important;
    transition-delay: 0s !important;
  }
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.chm-06__stage').forEach(function (stage) {
    if (stage.dataset.bound) return; stage.dataset.bound = '1';
    var btn = stage.querySelector('.chm-06__btn');
    function set(open) {
      stage.toggleAttribute('data-open', open);
      btn.setAttribute('aria-expanded', String(open));
      if (open) stage.querySelector('.chm-06__search input').focus({ preventScroll: true });
      else btn.focus();
    }
    btn.addEventListener('click', function () { set(true); });
    stage.querySelector('.chm-06__scrim').addEventListener('click', function () { set(false); });
    stage.querySelector('.chm-06__close').addEventListener('click', function () { set(false); });
    stage.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && stage.hasAttribute('data-open')) set(false);
    });
  });
})();
```
