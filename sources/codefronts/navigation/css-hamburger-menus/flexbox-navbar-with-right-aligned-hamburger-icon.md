---
source: "codefronts"
url: "https://codefronts.com/navigation/css-hamburger-menus/flexbox-navbar-with-right-aligned-hamburger-icon/"
title: "Flexbox Navbar Right-Aligned Hamburger Icon CSS"
section: "navigation"
category: "css-hamburger-menus"
category_name: "CSS Hamburger Menus"
description: "The layout lesson behind every navbar, taught on the navbar itself: flip the X-ray switch and the bar reveals its own construction — dashed outlines, the…"
has_js: "false"
---

Here's a working CSS Hamburger Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Flexbox Navbar Right-Aligned Hamburger Icon CSS
Source: https://codefronts.com/navigation/css-hamburger-menus/flexbox-navbar-with-right-aligned-hamburger-icon/

The layout lesson behind every navbar, taught on the navbar itself: flip the X-ray switch and the bar reveals its own construction — dashed outlines, the flex axis, and callouts pinned to the three declarations doing all the work (display:flex + align-items:center on the bar, gap for spacing, margin-inline-start:auto on the burger doing the right-alignment). The eternal question 'how do I push the hamburger right?' answered by a diagram you can toggle, not a paragraph.
## HTML
```html
<section class="chm-23" aria-label="Flexbox navbar anatomy demo">
  <div class="chm-23__stage">
    <div class="chm-23__ctl">
      <label class="chm-23__switch" for="chm23-x">
        <input type="checkbox" id="chm23-x">
        <i aria-hidden="true"></i>X-ray the layout
      </label>
    </div>
    <div class="chm-23__lab">
      <header class="chm-23__bar">
        <span class="chm-23__brand"><i aria-hidden="true"></i>Framework</span>
        <nav class="chm-23__links" aria-label="Primary">
          <a href="#docs">Docs</a>
          <a href="#examples">Examples</a>
        </nav>
        <button class="chm-23__burger" type="button" aria-label="Open menu (demo)"><span aria-hidden="true"><i></i><i></i><i></i></span></button>
        <span class="chm-23__co chm-23__co--bar"><code>display:flex · align-items:center · gap:24px</code></span>
        <span class="chm-23__co chm-23__co--auto"><code>margin-inline-start:auto</code> ← pushes right</span>
        <span class="chm-23__co chm-23__co--gap"><code>gap</code></span>
      </header>
      <div class="chm-23__axis" aria-hidden="true"><i></i>main axis →</div>
    </div>
    <p class="chm-23__note" aria-hidden="true">the bar stays fully functional under the annotations — inspect a live specimen</p>
  </div>
</section>
```
## CSS
```css
.chm-23,
.chm-23 *,
.chm-23 *::before,
.chm-23 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.chm-23 {
  background: var(--bg);
  width: 100%;
  min-height: 100vh;
  box-sizing: border-box;
  --bg: oklch(0.975 0.004 250);
  --panel: oklch(1 0 0);
  --edge: oklch(0.89 0.009 250);
  --ink: oklch(0.24 0.018 255);
  --mut: oklch(0.53 0.014 255);
  --blue: oklch(0.55 0.18 255);
  --amber: oklch(0.68 0.15 70);
  --violet: oklch(0.55 0.19 300);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.chm-23__stage {
  border-radius: 18px;
  border: 1px solid var(--edge);
  background: var(--bg);
  padding: 24px;
  display: grid;
  gap: 8px;
}

.chm-23__ctl {
  display: flex;
  justify-content: flex-end;
}

.chm-23__switch {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 13px;
  font-weight: 700;
  cursor: pointer;
  min-height: 44px;
  padding: 0 4px;
}

.chm-23__switch input {
  position: absolute;
  width: 1px;
  height: 1px;
  clip-path: inset(50%);
  overflow: hidden;
  white-space: nowrap;
}

.chm-23__switch i {
  width: 40px;
  height: 23px;
  border-radius: 99px;
  background: oklch(0.88 0.01 250);
  position: relative;
  transition: background .25s;
  flex: none;
}

.chm-23__switch i::after {
  content: "";
  position: absolute;
  top: 2.5px;
  left: 2.5px;
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: oklch(1 0 0);
  box-shadow: 0 2px 5px oklch(0.3 0.02 255/.35);
  transition: translate .25s cubic-bezier(.2,.7,.2,1);
}

.chm-23:has(#chm23-x:checked) .chm-23__switch i {
  background: var(--blue);
}

.chm-23:has(#chm23-x:checked) .chm-23__switch i::after {
  translate: 17px 0;
}

.chm-23__switch:has(:focus-visible) i {
  outline: 2px solid var(--blue);
  outline-offset: 2px;
}

.chm-23__lab {
  padding: 56px 8px 40px;
  position: relative;
}

.chm-23__bar {
  position: relative;
  display: flex;
  align-items: center;
  gap: 24px;
  min-height: 60px;
  padding: 0 20px;
  background: var(--panel);
  border: 1px solid var(--edge);
  border-radius: 14px;
  box-shadow: 0 14px 34px -26px oklch(0.3 0.04 255/.6);
  transition: outline-color .25s;
  outline: 2px dashed transparent;
  outline-offset: 5px;
}

.chm-23__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  font-weight: 800;
  font-size: 15px;
}

.chm-23__brand i {
  width: 19px;
  height: 19px;
  border-radius: 6px;
  background: conic-gradient(from 210deg,var(--blue),var(--violet));
}

.chm-23__links {
  display: flex;
  gap: 4px;
}

.chm-23__links a {
  padding: 9px 12px;
  border-radius: 8px;
  font-size: 13.5px;
  font-weight: 600;
  color: var(--mut);
  text-decoration: none;
  transition: color .15s,background .15s;
}

.chm-23__links a:hover,
.chm-23__links a:focus-visible {
  color: var(--ink);
  background: oklch(0.96 0.006 250);
}

.chm-23__links a:focus-visible {
  outline: 2px solid var(--blue);
  outline-offset: 2px;
}

.chm-23__burger {
  margin-inline-start: auto;
  width: 46px;
  height: 46px;
  display: grid;
  place-items: center;
  border: 1px solid var(--edge);
  border-radius: 11px;
  background: var(--panel);
  color: var(--ink);
  cursor: pointer;
  transition: background .2s,outline-color .25s;
  outline: 2px dashed transparent;
  outline-offset: 3px;
}

.chm-23__burger:hover {
  background: oklch(0.96 0.006 250);
}

.chm-23__burger:focus-visible {
  outline: 2px solid var(--blue) !important;
  outline-offset: 2px;
}

.chm-23__burger span {
  position: relative;
  width: 18px;
  height: 12px;
  display: block;
}

.chm-23__burger i {
  position: absolute;
  left: 0;
  width: 18px;
  height: 2px;
  border-radius: 2px;
  background: currentColor;
}

.chm-23__burger i:nth-child(1) {
  top: 0;
}

.chm-23__burger i:nth-child(2) {
  top: 5px;
}

.chm-23__burger i:nth-child(3) {
  top: 10px;
}

.chm-23:has(#chm23-x:checked) .chm-23__bar {
  outline-color: var(--blue);
}

.chm-23:has(#chm23-x:checked) .chm-23__burger {
  outline-color: var(--amber);
}

.chm-23:has(#chm23-x:checked) .chm-23__links {
  outline: 2px dashed var(--violet);
  outline-offset: 3px;
  border-radius: 8px;
}

.chm-23__co {
  position: absolute;
  font-size: 11px;
  font-weight: 700;
  color: oklch(1 0 0);
  padding: 5px 10px;
  border-radius: 7px;
  white-space: nowrap;
  opacity: 0;
  translate: 0 6px;
  transition: opacity .3s,translate .35s cubic-bezier(.2,.7,.2,1);
  pointer-events: none;
}

.chm-23__co code {
  font: 700 10.5px ui-monospace,Menlo,Consolas,monospace;
}

.chm-23__co--bar {
  top: -44px;
  left: 0;
  background: var(--blue);
}

.chm-23__co--bar::after {
  content: "";
  position: absolute;
  top: 100%;
  left: 18px;
  border: 5px solid transparent;
  border-top-color: var(--blue);
}

.chm-23__co--auto {
  bottom: -34px;
  right: 0;
  background: var(--amber);
}

.chm-23__co--auto::after {
  content: "";
  position: absolute;
  bottom: 100%;
  right: 20px;
  border: 5px solid transparent;
  border-bottom-color: var(--amber);
}

.chm-23__co--gap {
  top: -44px;
  left: 44%;
  background: var(--violet);
}

.chm-23__co--gap::after {
  content: "";
  position: absolute;
  top: 100%;
  left: 14px;
  border: 5px solid transparent;
  border-top-color: var(--violet);
}

.chm-23:has(#chm23-x:checked) .chm-23__co {
  opacity: 1;
  translate: 0 0;
}

.chm-23:has(#chm23-x:checked) .chm-23__co--auto {
  transition-delay: .08s;
}

.chm-23:has(#chm23-x:checked) .chm-23__co--gap {
  transition-delay: .16s;
}

.chm-23__axis {
  position: absolute;
  left: 8px;
  right: 8px;
  bottom: 8px;
  display: flex;
  align-items: center;
  gap: 8px;
  font: 700 10px ui-monospace,Menlo,Consolas,monospace;
  letter-spacing: .08em;
  color: var(--blue);
  opacity: 0;
  transition: opacity .3s .2s;
}

.chm-23__axis i {
  flex: 1;
  height: 2px;
  background: repeating-linear-gradient(90deg,var(--blue) 0 8px,transparent 8px 14px);
}

.chm-23:has(#chm23-x:checked) .chm-23__axis {
  opacity: .8;
}

.chm-23__note {
  font-size: 12px;
  color: var(--mut);
  text-align: center;
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .chm-23 * {
    transition-duration: .01s !important;
    transition-delay: 0s !important;
  }
}
```
