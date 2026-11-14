---
source: "codefronts"
url: "https://codefronts.com/navigation/css-hamburger-menus/neumorphic-hamburger-menu-toggle-button/"
title: "Neumorphic Hamburger Toggle Button HTML CSS"
section: "navigation"
category: "css-hamburger-menus"
category_name: "CSS Hamburger Menus"
description: "Soft-UI physics done by the rules: the burger is a clay button raised from the surface by the canonical dual shadow (light from the top-left, dark to the…"
has_js: "false"
---

Here's a working CSS Hamburger Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neumorphic Hamburger Toggle Button HTML CSS
Source: https://codefronts.com/navigation/css-hamburger-menus/neumorphic-hamburger-menu-toggle-button/

Soft-UI physics done by the rules: the burger is a clay button raised from the surface by the canonical dual shadow (light from the top-left, dark to the bottom-right), and pressing it doesn't move it — it inverts the shadows to inset, so the button visibly sinks INTO the surface while its lines fold to an X. The state is a real checkbox (a toggle IS a checkbox), the soft menu card floats up on the same material system, and the docs carry the honest accessibility warning neumorphism demands.
## HTML
```html
<section class="chm-26" aria-label="Neumorphic hamburger toggle demo">
  <div class="chm-26__stage">
    <input type="checkbox" id="chm26-t" class="chm-26__state">
    <div class="chm-26__plate">
      <label for="chm26-t" class="chm-26__btn">
        <span class="chm-26__ico" aria-hidden="true"><i></i><i></i><i></i></span>
      </label>
      <span class="chm-26__word" aria-hidden="true"><b class="chm-26__w1">rest</b><b class="chm-26__w2">pressed</b></span>
    </div>
    <nav class="chm-26__menu" aria-label="Menu">
      <a href="#home" style="--i:0"><i class="chm-26__dot" aria-hidden="true"></i>Home</a>
      <a href="#library" style="--i:1"><i class="chm-26__dot" aria-hidden="true"></i>Library</a>
      <a href="#stats" style="--i:2"><i class="chm-26__dot" aria-hidden="true"></i>Statistics</a>
      <a href="#settings" style="--i:3"><i class="chm-26__dot" aria-hidden="true"></i>Settings</a>
    </nav>
    <p class="chm-26__note" aria-hidden="true">same clay, two shadows — pressed = the pair goes <code>inset</code>. Note the focus ring stays loud on purpose.</p>
  </div>
</section>
```
## CSS
```css
.chm-26,
.chm-26 *,
.chm-26 *::before,
.chm-26 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.chm-26 {
  background: var(--bg);
  width: 100%;
  min-height: 100vh;
  box-sizing: border-box;
  --clay: oklch(0.92 0.012 260);
  --lite: oklch(0.99 0.005 260);
  --shade: oklch(0.78 0.02 260);
  --ink: oklch(0.32 0.02 262);
  --mut: oklch(0.52 0.018 262);
  --acc: oklch(0.65 0.11 190);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.chm-26__stage {
  position: relative;
  min-height: 480px;
  border-radius: 22px;
  background: var(--clay);
  padding: 34px 28px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 26px;
  border: 1px solid oklch(0.87 0.014 260);
}

.chm-26__state {
  position: absolute;
  width: 1px;
  height: 1px;
  clip-path: inset(50%);
  overflow: hidden;
  white-space: nowrap;
}

.chm-26__plate {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 14px;
}

.chm-26__btn {
  width: 74px;
  height: 74px;
  display: grid;
  place-items: center;
  border-radius: 22px;
  background: var(--clay);
  cursor: pointer;
  box-shadow: -7px -7px 14px var(--lite),7px 7px 14px var(--shade);
  transition: box-shadow .3s ease;
}

.chm-26__btn:hover {
  box-shadow: -9px -9px 18px var(--lite),9px 9px 18px var(--shade);
}

.chm-26__state:focus-visible ~ .chm-26__plate .chm-26__btn {
  outline: 3px solid var(--acc);
  outline-offset: 3px;
}

.chm-26__state:checked ~ .chm-26__plate .chm-26__btn {
  box-shadow: inset -5px -5px 10px var(--lite),inset 5px 5px 10px var(--shade);
}

.chm-26__ico {
  position: relative;
  width: 24px;
  height: 16px;
  display: block;
}

.chm-26__ico i {
  position: absolute;
  left: 0;
  width: 24px;
  height: 2.6px;
  border-radius: 3px;
  background: var(--ink);
  transition: translate .3s cubic-bezier(.2,.7,.2,1),rotate .3s cubic-bezier(.2,.7,.2,1) .05s,opacity .2s,background .3s;
}

.chm-26__ico i:nth-child(1) {
  top: 0;
}

.chm-26__ico i:nth-child(2) {
  top: 6.7px;
}

.chm-26__ico i:nth-child(3) {
  top: 13.4px;
}

.chm-26__state:checked ~ .chm-26__plate .chm-26__ico i {
  background: var(--acc);
}

.chm-26__state:checked ~ .chm-26__plate .chm-26__ico i:nth-child(1) {
  translate: 0 6.7px;
  rotate: 45deg;
}

.chm-26__state:checked ~ .chm-26__plate .chm-26__ico i:nth-child(2) {
  opacity: 0;
  scale: .4 1;
}

.chm-26__state:checked ~ .chm-26__plate .chm-26__ico i:nth-child(3) {
  translate: 0 -6.7px;
  rotate: -45deg;
}

.chm-26__word {
  position: relative;
  height: 16px;
  overflow: hidden;
  display: block;
  font-size: 11px;
  letter-spacing: .22em;
  text-transform: uppercase;
  color: var(--mut);
}

.chm-26__word b {
  display: block;
  height: 16px;
  line-height: 16px;
  font-weight: 700;
  transition: translate .35s cubic-bezier(.2,.7,.2,1);
}

.chm-26__state:checked ~ .chm-26__plate .chm-26__word b {
  translate: 0 -16px;
}

.chm-26__menu {
  width: min(280px,100%);
  display: grid;
  gap: 14px;
  padding: 6px;
}

.chm-26__menu a {
  display: flex;
  align-items: center;
  gap: 13px;
  min-height: 52px;
  padding: 0 20px;
  border-radius: 16px;
  background: var(--clay);
  color: var(--ink);
  font-size: 14px;
  font-weight: 700;
  text-decoration: none;
  box-shadow: -6px -6px 12px var(--lite),6px 6px 12px var(--shade);
  opacity: 0;
  translate: 0 12px;
  pointer-events: none;
  transition: box-shadow .25s,opacity .3s,translate .35s cubic-bezier(.2,.7,.2,1),color .2s;
}

.chm-26__state:checked ~ .chm-26__menu a {
  opacity: 1;
  translate: 0 0;
  pointer-events: auto;
  transition-delay: 0s,calc(.08s + var(--i)*.05s),calc(.08s + var(--i)*.05s),0s;
}

.chm-26__menu a:hover {
  color: var(--acc);
}

.chm-26__menu a:active {
  box-shadow: inset -4px -4px 8px var(--lite),inset 4px 4px 8px var(--shade);
}

.chm-26__menu a:focus-visible {
  outline: 3px solid var(--acc);
  outline-offset: 2px;
}

.chm-26__dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--clay);
  box-shadow: inset -2px -2px 4px var(--lite),inset 2px 2px 4px var(--shade);
  transition: background .2s,box-shadow .2s;
}

.chm-26__menu a:hover .chm-26__dot,
.chm-26__menu a:focus-visible .chm-26__dot {
  background: var(--acc);
  box-shadow: none;
}

.chm-26__note {
  margin-top: auto;
  font-size: 12px;
  line-height: 1.6;
  color: var(--mut);
  text-align: center;
  max-width: 34ch;
  text-wrap: pretty;
}

.chm-26__note code {
  font: 11px ui-monospace,Menlo,Consolas,monospace;
  background: oklch(0.88 0.014 260);
  border-radius: 5px;
  padding: 1.5px 6px;
}

@media (prefers-reduced-motion: reduce) {
  .chm-26 * {
    transition-duration: .01s !important;
    transition-delay: 0s !important;
  }
}
```
