---
source: "codefronts"
url: "https://codefronts.com/navigation/css-hamburger-menus/accessible-hamburger-menu-wcag-compliant/"
title: "WCAG Accessible Hamburger Menu HTML CSS JS Example"
section: "navigation"
category: "css-hamburger-menus"
category_name: "CSS Hamburger Menus"
description: "The audit-proof build: a menu drawer implemented as a true modal dialog — role=dialog, aria-modal, focus moved in on open, trapped while open, restored on…"
has_js: "true"
---

Here's a working CSS Hamburger Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: WCAG Accessible Hamburger Menu HTML CSS JS Example
Source: https://codefronts.com/navigation/css-hamburger-menus/accessible-hamburger-menu-wcag-compliant/

The audit-proof build: a menu drawer implemented as a true modal dialog — role=dialog, aria-modal, focus moved in on open, trapped while open, restored on close, background inert, Escape wired, 44px targets, visible focus rings, reduced-motion path. Every requirement is tied to its WCAG success criterion in the docs, so this doubles as the checklist you hand to a reviewer. This is the pattern demo 02's disclosure graduates to when the menu covers the page.
## HTML
```html
<section class="chm-17" aria-label="WCAG accessible hamburger menu demo">
  <div class="chm-17__stage">
    <div class="chm-17__page" id="chm17-page">
      <header class="chm-17__bar">
        <span class="chm-17__brand"><i aria-hidden="true"></i>CivicWorks</span>
        <button class="chm-17__btn" type="button" aria-expanded="false" aria-controls="chm17-menu" aria-label="Open navigation">
          <span class="chm-17__ico" aria-hidden="true"><i></i><i></i><i></i></span>
          <span class="chm-17__btntext" aria-hidden="true">Menu</span>
        </button>
      </header>
      <div class="chm-17__content" aria-hidden="true">
        <div class="chm-17__badge">WCAG 2.2 AA</div>
        <div class="chm-17__ln" style="--w:84%"></div>
        <div class="chm-17__ln" style="--w:66%"></div>
        <div class="chm-17__ln" style="--w:75%"></div>
      </div>
    </div>
    <div class="chm-17__scrim" aria-hidden="true"></div>
    <aside class="chm-17__menu" id="chm17-menu" role="dialog" aria-modal="true" aria-labelledby="chm17-title" tabindex="-1">
      <header class="chm-17__mhead">
        <b id="chm17-title">Navigation</b>
        <button class="chm-17__close" type="button" aria-label="Close navigation"><svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="m6 6 12 12M18 6 6 18"/></svg></button>
      </header>
      <nav aria-label="Primary">
        <ul class="chm-17__list">
          <li><a href="#services" aria-current="page">Services</a></li>
          <li><a href="#permits">Permits &amp; licences</a></li>
          <li><a href="#payments">Payments</a></li>
          <li><a href="#accessibility">Accessibility statement</a></li>
          <li><a href="#contact">Contact us</a></li>
        </ul>
      </nav>
      <p class="chm-17__hint" aria-hidden="true"><kbd>Tab</kbd> cycles inside · <kbd>Esc</kbd> closes &amp; restores focus · page behind is <code>inert</code></p>
    </aside>
    <p class="chm-17__live" role="status" aria-live="polite"></p>
  </div>
</section>
```
## CSS
```css
.chm-17,
.chm-17 *,
.chm-17 *::before,
.chm-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.chm-17 {
  background: var(--bg);
  width: 100%;
  min-height: 100vh;
  box-sizing: border-box;
  --target: 44px;
  --bg: oklch(0.98 0.004 250);
  --panel: oklch(1 0 0);
  --edge: oklch(0.87 0.01 250);
  --ink: oklch(0.22 0.02 255);
  --mut: oklch(0.45 0.018 255);
  --acc: oklch(0.48 0.16 258);
  --focus: oklch(0.55 0.2 262);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  display: grid;
  justify-content: center;
}

.chm-17__stage {
  position: relative;
  width: min(420px,88cqi,88vw);
  height: 540px;
  border-radius: 24px;
  overflow: hidden;
  background: var(--bg);
  border: 1px solid var(--edge);
}

.chm-17__page {
  height: 100%;
}

.chm-17__bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 68px;
  padding: 0 14px 0 22px;
  background: var(--panel);
  border-bottom: 1px solid var(--edge);
}

.chm-17__brand {
  display: flex;
  align-items: center;
  gap: 10px;
  font-weight: 700;
  font-size: 15.5px;
}

.chm-17__brand i {
  width: 20px;
  height: 20px;
  border-radius: 6px;
  background: var(--acc);
}

.chm-17__btn {
  display: flex;
  align-items: center;
  gap: 10px;
  min-height: var(--target);
  min-width: var(--target);
  padding: 0 14px;
  border: 2px solid var(--ink);
  border-radius: 10px;
  background: var(--panel);
  color: var(--ink);
  font: 700 13.5px 'Segoe UI',system-ui,sans-serif;
  cursor: pointer;
  transition: background .2s,color .2s;
}

.chm-17__btn:hover {
  background: var(--ink);
  color: var(--panel);
}

.chm-17__btn:focus-visible {
  outline: 3px solid var(--focus);
  outline-offset: 2px;
}

.chm-17__ico {
  position: relative;
  width: 17px;
  height: 13px;
  display: block;
}

.chm-17__ico i {
  position: absolute;
  left: 0;
  width: 17px;
  height: 2.5px;
  border-radius: 2px;
  background: currentColor;
}

.chm-17__ico i:nth-child(1) {
  top: 0;
}

.chm-17__ico i:nth-child(2) {
  top: 5.25px;
}

.chm-17__ico i:nth-child(3) {
  top: 10.5px;
}

.chm-17__content {
  padding: 22px;
  display: grid;
  gap: 14px;
  justify-items: start;
}

.chm-17__badge {
  font-size: 12px;
  font-weight: 800;
  letter-spacing: .08em;
  color: oklch(1 0 0);
  background: oklch(0.5 0.14 155);
  border-radius: 8px;
  padding: 8px 13px;
  margin-bottom: 6px;
}

.chm-17__ln {
  height: 12px;
  width: var(--w);
  border-radius: 99px;
  background: oklch(0.9 0.008 250);
}

.chm-17__scrim {
  position: absolute;
  inset: 0;
  z-index: 2;
  background: oklch(0.2 0.03 258/.5);
  opacity: 0;
  visibility: hidden;
  transition: opacity .3s,visibility 0s .3s;
}

[data-open] .chm-17__scrim {
  opacity: 1;
  visibility: visible;
  transition-delay: 0s;
}

.chm-17__menu {
  position: absolute;
  inset: 0 0 0 auto;
  z-index: 3;
  width: min(88%,330px);
  background: var(--panel);
  border-left: 1px solid var(--edge);
  box-shadow: -20px 0 44px -20px oklch(0.2 0.04 258/.5);
  display: flex;
  flex-direction: column;
  translate: 100% 0;
  visibility: hidden;
  transition: translate .38s cubic-bezier(.32,.72,.28,1),visibility 0s .38s;
}

[data-open] .chm-17__menu {
  translate: 0 0;
  visibility: visible;
  transition: translate .38s cubic-bezier(.32,.72,.28,1),visibility 0s 0s;
}

.chm-17__mhead {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 16px 14px 12px 22px;
  border-bottom: 2px solid var(--ink);
}

.chm-17__mhead b {
  font-size: 17px;
}

.chm-17__close {
  width: var(--target);
  height: var(--target);
  display: grid;
  place-items: center;
  border: 2px solid var(--ink);
  border-radius: 10px;
  background: var(--panel);
  color: var(--ink);
  cursor: pointer;
  transition: background .2s,color .2s;
}

.chm-17__close:hover {
  background: var(--ink);
  color: var(--panel);
}

.chm-17__close:focus-visible {
  outline: 3px solid var(--focus);
  outline-offset: 2px;
}

.chm-17__list {
  list-style: none;
  padding: 10px 12px;
  display: grid;
  gap: 2px;
}

.chm-17__list a {
  display: flex;
  align-items: center;
  min-height: var(--target);
  padding: 0 12px;
  border-radius: 9px;
  font-size: 15.5px;
  font-weight: 600;
  color: var(--ink);
  text-decoration: underline;
  text-decoration-color: transparent;
  text-underline-offset: 3px;
  transition: background .15s,text-decoration-color .15s;
}

.chm-17__list a:hover {
  background: oklch(0.95 0.008 255);
  text-decoration-color: var(--acc);
}

.chm-17__list a:focus-visible {
  outline: 3px solid var(--focus);
  outline-offset: -3px;
}

.chm-17__list a[aria-current="page"] {
  background: color-mix(in oklch,var(--acc) 10%,transparent);
  color: var(--acc);
  font-weight: 700;
}

.chm-17__hint {
  margin-top: auto;
  padding: 16px 22px;
  font-size: 12px;
  line-height: 1.9;
  color: var(--mut);
  border-top: 1px solid var(--edge);
  text-wrap: pretty;
}

.chm-17__hint kbd {
  font: 700 10.5px ui-monospace,Menlo,Consolas,monospace;
  border: 1.5px solid var(--edge);
  border-bottom-width: 3px;
  border-radius: 5px;
  padding: 1.5px 6px;
  background: var(--bg);
}

.chm-17__hint code {
  font: 11px ui-monospace,Menlo,Consolas,monospace;
  background: oklch(0.93 0.006 250);
  border-radius: 4px;
  padding: 1px 5px;
}

.chm-17__live {
  position: absolute;
  width: 1px;
  height: 1px;
  clip-path: inset(50%);
  overflow: hidden;
  white-space: nowrap;
}

@media (prefers-reduced-motion: reduce) {
  .chm-17 .chm-17__menu {
    translate: 0 0;
    opacity: 0;
    transition: opacity .15s,visibility 0s .15s;
  }

  .chm-17 [data-open] .chm-17__menu {
    opacity: 1;
    transition-delay: 0s;
  }

  .chm-17 * {
    transition-duration: .15s !important;
  }
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.chm-17__stage').forEach(function (stage) {
    if (stage.dataset.bound) return; stage.dataset.bound = '1';
    var page = stage.querySelector('.chm-17__page'),
        menu = stage.querySelector('.chm-17__menu'),
        burger = stage.querySelector('.chm-17__btn'),
        closeBtn = stage.querySelector('.chm-17__close'),
        live = stage.querySelector('.chm-17__live'),
        opener = null;
    function focusables() {
      return menu.querySelectorAll('a[href], button, input, select, textarea, [tabindex]:not([tabindex="-1"])');
    }
    function set(open) {
      stage.toggleAttribute('data-open', open);
      burger.setAttribute('aria-expanded', String(open));
      burger.setAttribute('aria-label', open ? 'Close navigation' : 'Open navigation');
      if (open) {
        opener = document.activeElement;
        page.setAttribute('inert', '');
        closeBtn.focus();
        live.textContent = 'Navigation opened';
      } else {
        page.removeAttribute('inert');
        (opener || burger).focus();
        live.textContent = 'Navigation closed';
      }
    }
    burger.addEventListener('click', function () { set(true); });
    closeBtn.addEventListener('click', function () { set(false); });
    stage.querySelector('.chm-17__scrim').addEventListener('click', function () { set(false); });
    stage.addEventListener('keydown', function (e) {
      if (!stage.hasAttribute('data-open')) return;
      if (e.key === 'Escape') { set(false); return; }
      if (e.key !== 'Tab') return;
      var f = focusables(), first = f[0], last = f[f.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    });
  });
})();
```
