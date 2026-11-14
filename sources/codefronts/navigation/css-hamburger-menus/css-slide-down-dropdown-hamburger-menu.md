---
source: "codefronts"
url: "https://codefronts.com/navigation/css-hamburger-menus/css-slide-down-dropdown-hamburger-menu/"
title: "CSS Dropdown Slide Down Mobile Hamburger Menu"
section: "navigation"
category: "css-hamburger-menus"
category_name: "CSS Hamburger Menus"
description: "How to animate a menu to height:auto — the question with a decade of bad answers (the max-height hack and its awkward timing) — solved twice: the…"
has_js: "false"
---

Here's a working CSS Hamburger Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Dropdown Slide Down Mobile Hamburger Menu
Source: https://codefronts.com/navigation/css-hamburger-menus/css-slide-down-dropdown-hamburger-menu/

How to animate a menu to height:auto — the question with a decade of bad answers (the max-height hack and its awkward timing) — solved twice: the grid-template-rows 0fr→1fr technique that's Baseline everywhere today, and the 2026-native interpolate-size: allow-keywords, which makes height:auto simply… transition, layered on via @supports so supporting browsers get real easing on the true height. The menu drops from under the bar; a checkbox drives it, zero JS.
## HTML
```html
<section class="chm-18" aria-label="Slide down dropdown hamburger menu demo">
  <div class="chm-18__stage">
    <div class="chm-18__bar">
      <input type="checkbox" id="chm18-t" class="chm-18__state">
      <header class="chm-18__head">
        <span class="chm-18__brand"><i aria-hidden="true"></i>brewline</span>
        <label for="chm18-t" class="chm-18__burger"><span aria-hidden="true"><i></i><i></i><i></i></span></label>
      </header>
      <nav class="chm-18__panel" aria-label="Primary">
        <ul>
          <li style="--i:0"><a href="#menu" aria-current="page">Menu</a></li>
          <li style="--i:1"><a href="#locations">Locations</a></li>
          <li style="--i:2"><a href="#beans">Beans &amp; gear</a></li>
          <li style="--i:3"><a href="#wholesale">Wholesale</a></li>
          <li style="--i:4"><a href="#careers">Careers</a></li>
        </ul>
      </nav>
    </div>
    <p class="chm-18__note" aria-hidden="true">opens to <b>height:auto</b> — grid <code>0fr→1fr</code> base, <code>interpolate-size</code> where supported. No max-height hack.</p>
  </div>
</section>
```
## CSS
```css
.chm-18,
.chm-18 *,
.chm-18 *::before,
.chm-18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.chm-18 {
  background: var(--bg);
  width: 100%;
  min-height: 100vh;
  box-sizing: border-box;
  --bg: oklch(0.975 0.006 60);
  --panel: oklch(1 0 0);
  --edge: oklch(0.88 0.012 60);
  --ink: oklch(0.25 0.02 45);
  --mut: oklch(0.52 0.018 45);
  --acc: oklch(0.6 0.13 55);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.chm-18__stage {
  min-height: 400px;
  border-radius: 18px;
  border: 1px solid var(--edge);
  background: var(--bg);
  padding: 26px;
  display: flex;
  flex-direction: column;
  gap: 16px;
  align-items: center;
  justify-content: center;
}

.chm-18__bar {
  width: min(420px,100%);
  background: var(--panel);
  border: 1px solid var(--edge);
  border-radius: 16px;
  box-shadow: 0 16px 38px -28px oklch(0.35 0.06 50/.55);
  overflow: hidden;
  position: relative;
}

.chm-18__state {
  position: absolute;
  width: 1px;
  height: 1px;
  clip-path: inset(50%);
  overflow: hidden;
  white-space: nowrap;
}

.chm-18__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 12px 12px 20px;
}

.chm-18__brand {
  display: flex;
  align-items: center;
  gap: 10px;
  font-weight: 800;
  font-size: 15.5px;
  letter-spacing: -.01em;
}

.chm-18__brand i {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: radial-gradient(circle at 35% 30%,oklch(0.8 0.1 70),var(--acc) 70%);
}

.chm-18__burger {
  width: 46px;
  height: 46px;
  display: grid;
  place-items: center;
  border: 1px solid var(--edge);
  border-radius: 12px;
  cursor: pointer;
  transition: background .2s,border-color .2s;
}

.chm-18__burger:hover {
  background: oklch(0.965 0.008 60);
}

.chm-18__state:focus-visible ~ .chm-18__head .chm-18__burger {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.chm-18__burger span {
  position: relative;
  width: 18px;
  height: 12px;
  display: block;
}

.chm-18__burger i {
  position: absolute;
  left: 0;
  width: 18px;
  height: 2px;
  border-radius: 2px;
  background: var(--ink);
  transition: translate .28s,rotate .28s .04s,opacity .2s;
}

.chm-18__burger i:nth-child(1) {
  top: 0;
}

.chm-18__burger i:nth-child(2) {
  top: 5px;
}

.chm-18__burger i:nth-child(3) {
  top: 10px;
}

.chm-18__state:checked ~ .chm-18__head .chm-18__burger i:nth-child(1) {
  translate: 0 5px;
  rotate: 45deg;
}

.chm-18__state:checked ~ .chm-18__head .chm-18__burger i:nth-child(2) {
  opacity: 0;
}

.chm-18__state:checked ~ .chm-18__head .chm-18__burger i:nth-child(3) {
  translate: 0 -5px;
  rotate: -45deg;
}

.chm-18__panel {
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows .4s cubic-bezier(.2,.7,.2,1);
}

.chm-18__state:checked ~ .chm-18__panel {
  grid-template-rows: 1fr;
}

.chm-18__panel ul {
  list-style: none;
  overflow: hidden;
  min-height: 0;
}

.chm-18__panel li {
  opacity: 0;
  translate: 0 -8px;
  transition: opacity .25s,translate .3s cubic-bezier(.2,.7,.2,1);
}

.chm-18__state:checked ~ .chm-18__panel li {
  opacity: 1;
  translate: 0 0;
  transition-delay: calc(.12s + var(--i)*.04s);
}

.chm-18__panel a {
  display: flex;
  align-items: center;
  justify-content: space-between;
  min-height: 48px;
  padding: 0 20px;
  font-size: 14.5px;
  font-weight: 600;
  color: var(--mut);
  text-decoration: none;
  border-top: 1px solid color-mix(in oklch,var(--edge) 55%,transparent);
  transition: background .15s,color .15s;
}

.chm-18__panel a::after {
  content: "→";
  opacity: 0;
  translate: -6px 0;
  transition: opacity .2s,translate .2s;
}

.chm-18__panel a:hover,
.chm-18__panel a:focus-visible {
  background: oklch(0.97 0.008 60);
  color: var(--ink);
}

.chm-18__panel a:hover::after,
.chm-18__panel a:focus-visible::after {
  opacity: 1;
  translate: 0 0;
}

.chm-18__panel a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
}

.chm-18__panel a[aria-current="page"] {
  color: var(--acc);
}

@supports (interpolate-size: allow-keywords) {
  .chm-18 {
    background: var(--bg);
    width: 100%;
    min-height: 100vh;
    box-sizing: border-box;
    interpolate-size: allow-keywords;
  }

  .chm-18__panel {
    display: block;
    height: 0;
    overflow: hidden;
    transition: height .4s cubic-bezier(.2,.7,.2,1);
  }

  .chm-18__state:checked ~ .chm-18__panel {
    height: auto;
  }
}

.chm-18__note {
  width: min(420px,100%);
  font-size: 12px;
  line-height: 1.6;
  color: var(--mut);
  text-align: center;
  text-wrap: pretty;
}

.chm-18__note code {
  font: 11px ui-monospace,Menlo,Consolas,monospace;
  background: oklch(0.92 0.01 60);
  border-radius: 5px;
  padding: 1.5px 6px;
}

@media (prefers-reduced-motion: reduce) {
  .chm-18 * {
    transition-duration: .01s !important;
    transition-delay: 0s !important;
  }
}
```
