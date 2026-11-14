---
source: "codefronts"
url: "https://codefronts.com/navigation/css-hamburger-menus/hamburger-menu-with-morphing-icon-animations/"
title: "CSS Hamburger Menu Morphing to Close Icon Animation"
section: "navigation"
category: "css-hamburger-menus"
category_name: "CSS Hamburger Menus"
description: "Not a rotate trick — a true shape morph."
has_js: "true"
---

Here's a working CSS Hamburger Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Hamburger Menu Morphing to Close Icon Animation
Source: https://codefronts.com/navigation/css-hamburger-menus/hamburger-menu-with-morphing-icon-animations/

Not a rotate trick — a true shape morph. The burger is one SVG whose line geometry is written in CSS via the d property, and because d: path() is now animatable, the browser interpolates the actual path coordinates from ☰ to ✕. Straight lines bend through genuinely in-between shapes, something transforms can't produce, with zero libraries where GreenSock or Flubber used to be mandatory. Includes the transform-based fallback behind @supports.
## HTML
```html
<section class="chm-10" aria-label="SVG path morph hamburger icon demo">
  <div class="chm-10__stage">
    <div class="chm-10__bar">
      <header class="chm-10__head">
        <span class="chm-10__brand">monoline<i>®</i></span>
        <button class="chm-10__btn" type="button" aria-expanded="false" aria-controls="chm10-panel" aria-label="Open menu">
          <svg class="chm-10__ico" viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true">
            <path class="chm-10__top" d="M 3 6 L 21 6"/>
            <path class="chm-10__mid" d="M 3 12 L 21 12"/>
            <path class="chm-10__bot" d="M 3 18 L 21 18"/>
          </svg>
        </button>
      </header>
      <nav class="chm-10__panel" id="chm10-panel" aria-label="Primary">
        <ul>
          <li><a href="#shop">Shop</a></li>
          <li><a href="#lookbook">Lookbook</a></li>
          <li><a href="#stores">Stores</a></li>
          <li><a href="#journal">Journal</a></li>
        </ul>
      </nav>
    </div>
    <p class="chm-10__note" aria-hidden="true">the <code>d</code> attribute itself is transitioning — slow it in DevTools and watch the endpoints travel</p>
  </div>
</section>
```
## CSS
```css
.chm-10,
.chm-10 *,
.chm-10 *::before,
.chm-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.chm-10 {
  background: var(--bg);
  width: 100%;
  min-height: 100vh;
  box-sizing: border-box;
  --bg: oklch(0.97 0.003 90);
  --panel: oklch(1 0 0);
  --edge: oklch(0.88 0.005 90);
  --ink: oklch(0.2 0.01 90);
  --mut: oklch(0.52 0.01 90);
  --acc: oklch(0.62 0.19 30);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.chm-10__stage {
  min-height: 400px;
  border-radius: 18px;
  border: 1px solid var(--edge);
  background: var(--bg);
  padding: 26px;
  display: flex;
  flex-direction: column;
  gap: 18px;
  align-items: center;
  justify-content: center;
}

.chm-10__bar {
  width: min(420px,100%);
  background: var(--panel);
  border: 1.5px solid var(--ink);
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 5px 5px 0 oklch(0.2 0.01 90/.1);
}

.chm-10__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 14px 14px 14px 20px;
}

.chm-10__brand {
  font-size: 15.5px;
  font-weight: 700;
  letter-spacing: -.01em;
}

.chm-10__brand i {
  font-style: normal;
  font-size: 10px;
  vertical-align: super;
  color: var(--mut);
}

.chm-10__btn {
  width: 46px;
  height: 46px;
  display: grid;
  place-items: center;
  border: 1.5px solid var(--ink);
  border-radius: 12px;
  background: var(--panel);
  color: var(--ink);
  cursor: pointer;
  transition: background .2s,color .2s,box-shadow .2s,translate .15s;
}

.chm-10__btn:hover {
  background: var(--ink);
  color: var(--panel);
}

.chm-10__btn:active {
  translate: 1px 1px;
}

.chm-10__btn:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.chm-10__top,
.chm-10__mid,
.chm-10__bot {
  transition: d .45s cubic-bezier(.65,0,.35,1),opacity .3s;
}

.chm-10__top {
  d: path("M 3 6 L 21 6");
}

.chm-10__mid {
  d: path("M 3 12 L 21 12");
}

.chm-10__bot {
  d: path("M 3 18 L 21 18");
}

[data-open] .chm-10__top {
  d: path("M 5 5 L 19 19");
}

[data-open] .chm-10__mid {
  d: path("M 12 12 L 12 12");
  opacity: 0;
}

[data-open] .chm-10__bot {
  d: path("M 5 19 L 19 5");
}

@supports not (d: path("M0 0h1")) {
  .chm-10__ico path {
    transition: translate .3s,rotate .3s .05s,opacity .2s;
    transform-origin: 12px 12px;
  }

  [data-open] .chm-10__ico .chm-10__top {
    translate: 0 6px;
    rotate: 45deg;
  }

  [data-open] .chm-10__ico .chm-10__mid {
    opacity: 0;
  }

  [data-open] .chm-10__ico .chm-10__bot {
    translate: 0 -6px;
    rotate: -45deg;
  }
}

.chm-10__panel {
  display: grid;
  grid-template-rows: 0fr;
  opacity: 0;
  transition: grid-template-rows .4s cubic-bezier(.2,.7,.2,1),opacity .3s;
}

[data-open] .chm-10__panel {
  grid-template-rows: 1fr;
  opacity: 1;
}

.chm-10__panel ul {
  list-style: none;
  overflow: hidden;
  min-height: 0;
}

.chm-10__panel a {
  display: flex;
  align-items: center;
  justify-content: space-between;
  min-height: 52px;
  padding: 0 20px;
  border-top: 1.5px solid var(--ink);
  text-decoration: none;
  font-size: 15px;
  font-weight: 700;
  letter-spacing: .02em;
  text-transform: uppercase;
  color: var(--ink);
  transition: background .15s,color .15s,padding .2s;
}

.chm-10__panel a::after {
  content: "→";
}

.chm-10__panel a:hover,
.chm-10__panel a:focus-visible {
  background: var(--ink);
  color: var(--panel);
  padding-left: 26px;
}

.chm-10__panel a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -4px;
}

.chm-10__note {
  width: min(420px,100%);
  font-size: 12px;
  line-height: 1.6;
  color: var(--mut);
  text-align: center;
  text-wrap: pretty;
}

.chm-10__note code {
  font: 11px ui-monospace,Menlo,Consolas,monospace;
  background: oklch(0.92 0.005 90);
  border-radius: 5px;
  padding: 1.5px 6px;
}

@media (prefers-reduced-motion: reduce) {
  .chm-10 * {
    transition-duration: .01s !important;
  }
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.chm-10__bar').forEach(function (bar) {
    if (bar.dataset.bound) return; bar.dataset.bound = '1';
    var btn = bar.querySelector('.chm-10__btn');
    function set(open) {
      bar.toggleAttribute('data-open', open);
      btn.setAttribute('aria-expanded', String(open));
      btn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    }
    btn.addEventListener('click', function () { set(btn.getAttribute('aria-expanded') !== 'true'); });
    bar.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && bar.hasAttribute('data-open')) { set(false); btn.focus(); }
    });
  });
})();
```
