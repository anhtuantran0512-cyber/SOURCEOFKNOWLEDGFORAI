---
source: "codefronts"
url: "https://codefronts.com/navigation/css-hamburger-menus/responsive-navbar-with-mobile-only-hamburger-toggle/"
title: "Responsive Navbar Mobile Hamburger Toggle Media Queries"
section: "navigation"
category: "css-hamburger-menus"
category_name: "CSS Hamburger Menus"
description: "The breakpoint swap every site ships: inline links on wide screens, hamburger + slide-down panel on narrow — except this stage has a drag handle on its right…"
has_js: "false"
---

Here's a working CSS Hamburger Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Responsive Navbar Mobile Hamburger Toggle Media Queries
Source: https://codefronts.com/navigation/css-hamburger-menus/responsive-navbar-with-mobile-only-hamburger-toggle/

The breakpoint swap every site ships: inline links on wide screens, hamburger + slide-down panel on narrow — except this stage has a drag handle on its right edge, so you can resize the component and watch the swap happen live. Built on a container query (the 2026 default; the exact media-query equivalent is printed in the docs), with a checkbox toggle so the whole thing stays zero-JS.
## HTML
```html
<section class="chm-13" aria-label="Responsive navbar breakpoint demo">
  <div class="chm-13__stage">
    <p class="chm-13__hint" aria-hidden="true">↔ drag the right edge — the navbar watches its own width (620px breakpoint)</p>
    <div class="chm-13__resize">
      <div class="chm-13__navwrap">
        <header class="chm-13__bar">
          <input type="checkbox" id="chm13-t" class="chm-13__state">
          <span class="chm-13__brand"><i aria-hidden="true"></i>Statement</span>
          <nav class="chm-13__links" aria-label="Primary">
            <a href="#product" aria-current="page">Product</a>
            <a href="#method">Method</a>
            <a href="#pricing">Pricing</a>
            <a href="#company">Company</a>
          </nav>
          <a class="chm-13__cta" href="#start">Get started</a>
          <label for="chm13-t" class="chm-13__burger" aria-hidden="true"><span><i></i><i></i><i></i></span></label>
          <nav class="chm-13__panel" aria-label="Primary mobile">
            <ul>
              <li><a href="#product" aria-current="page">Product</a></li>
              <li><a href="#method">Method</a></li>
              <li><a href="#pricing">Pricing</a></li>
              <li><a href="#company">Company</a></li>
            </ul>
          </nav>
        </header>
        <div class="chm-13__page" aria-hidden="true"><div class="chm-13__ln" style="--w:64%"></div><div class="chm-13__ln" style="--w:82%"></div><div class="chm-13__ln" style="--w:47%"></div></div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.chm-13,
.chm-13 *,
.chm-13 *::before,
.chm-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.chm-13 {
  background: var(--bg);
  width: 100%;
  min-height: 100vh;
  box-sizing: border-box;
  --bg: oklch(0.975 0.004 260);
  --panel: oklch(1 0 0);
  --edge: oklch(0.89 0.009 260);
  --ink: oklch(0.24 0.018 262);
  --mut: oklch(0.53 0.015 262);
  --acc: oklch(0.58 0.2 275);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.chm-13__stage {
  border: 1px solid var(--edge);
  border-radius: 18px;
  background: var(--bg);
  padding: 20px;
}

.chm-13__hint {
  font-size: 12px;
  color: var(--mut);
  margin-bottom: 14px;
}

.chm-13__resize {
  resize: horizontal;
  overflow: hidden;
  min-width: min(300px,100%);
  max-width: 100%;
  width: 100%;
  border-right: 3px dashed color-mix(in oklch,var(--acc) 45%,var(--edge));
  padding-right: 14px;
}

.chm-13__navwrap {
  container-type: inline-size;
}

.chm-13__bar {
  position: relative;
  display: flex;
  align-items: center;
  gap: 26px;
  min-height: 64px;
  padding: 8px 20px;
  background: var(--panel);
  border: 1px solid var(--edge);
  border-radius: 14px;
  box-shadow: 0 12px 30px -22px oklch(0.35 0.05 265/.5);
  flex-wrap: wrap;
}

.chm-13__state {
  position: absolute;
  width: 1px;
  height: 1px;
  clip-path: inset(50%);
  overflow: hidden;
  white-space: nowrap;
}

.chm-13__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  font-weight: 800;
  font-size: 15px;
  letter-spacing: -.01em;
}

.chm-13__brand i {
  width: 19px;
  height: 19px;
  border-radius: 6px;
  background: conic-gradient(from 210deg,var(--acc),oklch(0.72 0.13 200));
  rotate: 8deg;
}

.chm-13__links {
  display: flex;
  gap: 4px;
  margin-left: 6px;
}

.chm-13__links a {
  position: relative;
  padding: 9px 12px;
  font-size: 13.5px;
  font-weight: 600;
  color: var(--mut);
  text-decoration: none;
  transition: color .18s;
}

.chm-13__links a::after {
  content: "";
  position: absolute;
  left: 12px;
  right: 12px;
  bottom: 4px;
  height: 2px;
  border-radius: 2px;
  background: var(--acc);
  scale: 0 1;
  transform-origin: left;
  transition: scale .25s cubic-bezier(.2,.7,.2,1);
}

.chm-13__links a:hover,
.chm-13__links a:focus-visible,
.chm-13__links a[aria-current="page"] {
  color: var(--ink);
}

.chm-13__links a:hover::after,
.chm-13__links a:focus-visible::after,
.chm-13__links a[aria-current="page"]::after {
  scale: 1 1;
}

.chm-13__links a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
  border-radius: 6px;
}

.chm-13__cta {
  margin-left: auto;
  min-height: 40px;
  display: inline-flex;
  align-items: center;
  padding: 0 18px;
  border-radius: 10px;
  background: var(--ink);
  color: oklch(0.97 0.005 260);
  font-size: 13px;
  font-weight: 700;
  text-decoration: none;
  transition: background .2s,translate .15s;
}

.chm-13__cta:hover {
  background: var(--acc);
}

.chm-13__cta:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.chm-13__cta:active {
  translate: 0 1px;
}

.chm-13__burger {
  display: none;
  width: 44px;
  height: 44px;
  place-items: center;
  border: 1px solid var(--edge);
  border-radius: 11px;
  cursor: pointer;
  transition: background .2s;
}

.chm-13__burger:hover {
  background: oklch(0.96 0.006 260);
}

.chm-13__state:focus-visible ~ .chm-13__burger {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.chm-13__burger span {
  position: relative;
  width: 18px;
  height: 12px;
  display: block;
}

.chm-13__burger i {
  position: absolute;
  left: 0;
  width: 18px;
  height: 2px;
  border-radius: 2px;
  background: var(--ink);
  transition: translate .28s,rotate .28s .04s,opacity .2s;
}

.chm-13__burger i:nth-child(1) {
  top: 0;
}

.chm-13__burger i:nth-child(2) {
  top: 5px;
}

.chm-13__burger i:nth-child(3) {
  top: 10px;
}

.chm-13__state:checked ~ .chm-13__burger i:nth-child(1) {
  translate: 0 5px;
  rotate: 45deg;
}

.chm-13__state:checked ~ .chm-13__burger i:nth-child(2) {
  opacity: 0;
}

.chm-13__state:checked ~ .chm-13__burger i:nth-child(3) {
  translate: 0 -5px;
  rotate: -45deg;
}

.chm-13__panel {
  display: none;
  flex-basis: 100%;
  min-width: 0;
}

.chm-13__panel ul {
  list-style: none;
  overflow: hidden;
  min-height: 0;
  display: grid;
}

.chm-13__panel a {
  display: flex;
  align-items: center;
  min-height: 46px;
  padding: 0 12px;
  border-radius: 9px;
  font-size: 14px;
  font-weight: 600;
  color: var(--mut);
  text-decoration: none;
  transition: background .15s,color .15s;
}

.chm-13__panel a:hover,
.chm-13__panel a:focus-visible {
  background: oklch(0.96 0.008 260);
  color: var(--ink);
}

.chm-13__panel a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
}

.chm-13__panel a[aria-current="page"] {
  color: var(--acc);
}

@container (max-width: 620px) {
  .chm-13__links {
    display: none;
  }

  .chm-13__burger {
    display: grid;
    order: 5;
  }

  .chm-13__cta {
    margin-left: auto;
  }

  .chm-13__panel {
    display: grid;
    grid-template-rows: 0fr;
    opacity: 0;
    transition: grid-template-rows .35s cubic-bezier(.2,.7,.2,1),opacity .28s;
  }

  .chm-13__state:checked ~ .chm-13__panel {
    grid-template-rows: 1fr;
    opacity: 1;
  }

  .chm-13__panel ul {
    padding-top: 6px;
  }

  .chm-13__state:checked ~ .chm-13__panel ul {
    border-top: 1px solid var(--edge);
    margin-top: 4px;
  }
}

.chm-13__page {
  padding: 18px 4px;
  display: grid;
  gap: 12px;
}

.chm-13__ln {
  height: 11px;
  width: var(--w);
  border-radius: 99px;
  background: oklch(0.9 0.007 260);
}

@media (prefers-reduced-motion: reduce) {
  .chm-13 * {
    transition-duration: .01s !important;
  }
}
```
