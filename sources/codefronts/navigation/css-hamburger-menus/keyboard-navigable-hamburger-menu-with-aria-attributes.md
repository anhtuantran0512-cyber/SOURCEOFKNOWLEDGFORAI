---
source: "codefronts"
url: "https://codefronts.com/navigation/css-hamburger-menus/keyboard-navigable-hamburger-menu-with-aria-attributes/"
title: "Keyboard Navigable Hamburger Menu with ARIA Attributes"
section: "navigation"
category: "css-hamburger-menus"
category_name: "CSS Hamburger Menus"
description: "The WAI-ARIA disclosure-navigation pattern, implemented exactly as the APG specifies and annotated so you can defend it in an accessibility audit: a real…"
has_js: "true"
---

Here's a working CSS Hamburger Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Keyboard Navigable Hamburger Menu with ARIA Attributes
Source: https://codefronts.com/navigation/css-hamburger-menus/keyboard-navigable-hamburger-menu-with-aria-attributes/

The WAI-ARIA disclosure-navigation pattern, implemented exactly as the APG specifies and annotated so you can defend it in an accessibility audit: a real button carrying aria-expanded + aria-controls, a plain nav > ul of links (no role=menu — that's for app menus, not site nav), Arrow/Home/End roving focus, and Escape that closes and hands focus back. A visible key-legend strip makes the demo self-teaching: press the keys it shows.
## HTML
```html
<section class="chm-02" aria-label="Keyboard navigable ARIA hamburger menu demo">
  <div class="chm-02__stage">
    <div class="chm-02__bar">
      <header class="chm-02__head">
        <span class="chm-02__brand"><i aria-hidden="true"></i>Fieldnote</span>
        <button class="chm-02__btn" type="button" aria-expanded="false" aria-controls="chm02-panel">
          <span class="chm-02__ico" aria-hidden="true"><i></i><i></i><i></i></span>Menu
        </button>
      </header>
      <nav class="chm-02__panel" id="chm02-panel" aria-label="Primary">
        <ul>
          <li><a href="#dashboard" aria-current="page">Dashboard</a></li>
          <li><a href="#projects">Projects</a></li>
          <li><a href="#reports">Reports</a></li>
          <li><a href="#team">Team</a></li>
          <li><a href="#settings">Settings</a></li>
        </ul>
      </nav>
    </div>
    <p class="chm-02__keys" aria-hidden="true">
      <kbd>Tab</kbd> reach button · <kbd>Enter</kbd> open · <kbd>↓</kbd><kbd>↑</kbd> move · <kbd>Home</kbd><kbd>End</kbd> jump · <kbd>Esc</kbd> close &amp; return
    </p>
    <output class="chm-02__sr" aria-hidden="true">aria-expanded: <b>false</b></output>
  </div>
</section>
```
## CSS
```css
.chm-02,
.chm-02 *,
.chm-02 *::before,
.chm-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.chm-02 {
  background: var(--bg);
  width: 100%;
  min-height: 100vh;
  box-sizing: border-box;
  --bg: oklch(0.985 0.003 250);
  --panel: oklch(1 0 0);
  --edge: oklch(0.9 0.01 250);
  --ink: oklch(0.25 0.02 255);
  --mut: oklch(0.54 0.015 255);
  --acc: oklch(0.52 0.17 262);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.chm-02__stage {
  min-height: 420px;
  border-radius: 18px;
  border: 1px solid var(--edge);
  background: var(--bg);
  padding: 26px;
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.chm-02__bar {
  width: min(440px,100%);
  margin-inline: auto;
  background: var(--panel);
  border: 1px solid var(--edge);
  border-radius: 16px;
  box-shadow: 0 16px 40px -28px oklch(0.35 0.05 260/.5);
  overflow: hidden;
}

.chm-02__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 12px 12px 18px;
}

.chm-02__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  font-weight: 700;
  font-size: 15px;
  letter-spacing: -.01em;
}

.chm-02__brand i {
  width: 18px;
  height: 18px;
  border-radius: 5px;
  background: conic-gradient(from 180deg,var(--acc),oklch(0.7 0.13 200));
}

.chm-02__btn {
  display: flex;
  align-items: center;
  gap: 10px;
  min-height: 44px;
  padding: 0 16px;
  border: 1px solid var(--edge);
  border-radius: 11px;
  background: var(--panel);
  font: 600 13.5px 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  cursor: pointer;
  transition: border-color .2s,background .2s;
}

.chm-02__btn:hover {
  background: oklch(0.965 0.006 250);
  border-color: oklch(0.8 0.02 255);
}

.chm-02__btn:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.chm-02__ico {
  position: relative;
  width: 16px;
  height: 12px;
  display: block;
}

.chm-02__ico i {
  position: absolute;
  left: 0;
  width: 16px;
  height: 2px;
  border-radius: 2px;
  background: currentColor;
  transition: translate .25s,rotate .25s .04s,opacity .2s;
}

.chm-02__ico i:nth-child(1) {
  top: 0;
}

.chm-02__ico i:nth-child(2) {
  top: 5px;
}

.chm-02__ico i:nth-child(3) {
  top: 10px;
}

.chm-02__btn[aria-expanded="true"] .chm-02__ico i:nth-child(1) {
  translate: 0 5px;
  rotate: 45deg;
}

.chm-02__btn[aria-expanded="true"] .chm-02__ico i:nth-child(2) {
  opacity: 0;
  translate: -5px 0;
}

.chm-02__btn[aria-expanded="true"] .chm-02__ico i:nth-child(3) {
  translate: 0 -5px;
  rotate: -45deg;
}

.chm-02__panel {
  display: grid;
  grid-template-rows: 0fr;
  opacity: 0;
  transition: grid-template-rows .35s cubic-bezier(.2,.7,.2,1),opacity .25s;
}

.chm-02__bar:has([aria-expanded="true"]) .chm-02__panel {
  grid-template-rows: 1fr;
  opacity: 1;
}

.chm-02__panel ul {
  list-style: none;
  overflow: hidden;
  min-height: 0;
  display: flex;
  flex-direction: column;
  padding: 0 8px;
}

.chm-02__bar:has([aria-expanded="true"]) .chm-02__panel ul {
  padding-bottom: 8px;
  border-top: 1px solid var(--edge);
}

.chm-02__panel a {
  display: flex;
  align-items: center;
  min-height: 46px;
  padding: 0 12px;
  margin-top: 4px;
  border-radius: 9px;
  text-decoration: none;
  font-size: 14px;
  font-weight: 600;
  color: var(--mut);
  transition: background .15s,color .15s;
}

.chm-02__panel a:hover {
  background: oklch(0.96 0.008 255);
  color: var(--ink);
}

.chm-02__panel a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
  color: var(--ink);
}

.chm-02__panel a[aria-current="page"] {
  color: var(--acc);
  background: color-mix(in oklch,var(--acc) 9%,transparent);
}

.chm-02__keys {
  width: min(440px,100%);
  margin-inline: auto;
  font-size: 12px;
  line-height: 2.1;
  color: var(--mut);
  text-align: center;
  text-wrap: pretty;
}

.chm-02__keys kbd {
  display: inline-block;
  min-width: 26px;
  text-align: center;
  font: 600 11px ui-monospace,Menlo,Consolas,monospace;
  color: var(--ink);
  background: var(--panel);
  border: 1px solid var(--edge);
  border-bottom-width: 2px;
  border-radius: 6px;
  padding: 2px 6px;
  margin: 0 2px;
}

.chm-02__sr {
  width: min(440px,100%);
  margin-inline: auto;
  text-align: center;
  font: 12px ui-monospace,Menlo,Consolas,monospace;
  color: var(--mut);
}

.chm-02__sr b {
  color: var(--acc);
}

@media (prefers-reduced-motion: reduce) {
  .chm-02 * {
    transition-duration: .01s !important;
  }
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.chm-02__stage').forEach(function (stage) {
    if (stage.dataset.bound) return; stage.dataset.bound = '1';
    var btn = stage.querySelector('.chm-02__btn'),
        panel = stage.querySelector('.chm-02__panel'),
        out = stage.querySelector('.chm-02__sr b'),
        links = Array.prototype.slice.call(panel.querySelectorAll('a'));
    function set(open, refocus) {
      btn.setAttribute('aria-expanded', String(open));
      if (out) out.textContent = String(open);
      if (open) links[0].focus();
      else if (refocus) btn.focus();
    }
    btn.addEventListener('click', function () { set(btn.getAttribute('aria-expanded') !== 'true'); });
    stage.addEventListener('keydown', function (e) {
      var open = btn.getAttribute('aria-expanded') === 'true';
      if (e.key === 'Escape' && open) { set(false, true); return; }
      var i = links.indexOf(document.activeElement);
      if (i < 0) return;
      var next = { ArrowDown: i + 1, ArrowUp: i - 1, Home: 0, End: links.length - 1 }[e.key];
      if (next === undefined) return;
      e.preventDefault();
      links[(next + links.length) % links.length].focus();
    });
    stage.addEventListener('focusout', function () {
      requestAnimationFrame(function () {
        if (!stage.contains(document.activeElement)) set(false, false);
      });
    });
  });
})();
```
