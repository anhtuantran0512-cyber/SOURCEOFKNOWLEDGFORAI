---
source: "codefronts"
url: "https://codefronts.com/motion/css-hover-effects/css-strikethrough-hover-link-effect/"
title: "CSS Strikethrough Hover Link Effect"
section: "motion"
category: "css-hover-effects"
category_name: "CSS Hover Effects"
description: "Links that animate a strikethrough line across the text on hover — six creative strikethrough styles including wavy, dotted, and multi-pass."
has_js: "false"
---

Here's a working CSS Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Strikethrough Hover Link Effect
Source: https://codefronts.com/motion/css-hover-effects/css-strikethrough-hover-link-effect/

Links that animate a strikethrough line across the text on hover — six creative strikethrough styles including wavy, dotted, and multi-pass.
## HTML
```html
<div class="hv-27">
  <p class="hv-27__label">Strikethrough Hover Links — 6 Styles</p>

  <div class="hv-27__group">
    <a class="hv-27__link hv-27__link--solid" href="#">Solid Strike</a>
    <a class="hv-27__link hv-27__link--thin" href="#">Hair-thin Strike</a>
    <a class="hv-27__link hv-27__link--thick" href="#">Chunky Strike</a>
  </div>

  <div class="hv-27__group">
    <a class="hv-27__link hv-27__link--wavy" href="#">Wavy Strike</a>
    <a class="hv-27__link hv-27__link--dashed" href="#">Dashed Strike</a>
    <a class="hv-27__link hv-27__link--double" href="#">Double Strike</a>
  </div>
</div>
```
## CSS
```css
.hv-27,
.hv-27 *,
.hv-27 *::before,
.hv-27 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.hv-27 {
  --st-color: #e05;
  --st-thickness: 2px;
  font-family: system-ui, sans-serif;
  background: #0c0c0f;
  padding: 3rem 2rem;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  gap: 2.5rem;
  align-items: center;
  justify-content: center;
}

.hv-27__label {
  color: #444;
  font-size: .72rem;
  letter-spacing: .15em;
  text-transform: uppercase;
}

.hv-27__group {
  display: flex;
  gap: 3rem;
  flex-wrap: wrap;
  justify-content: center;
}

.hv-27__link {
  color: #ddd;
  text-decoration: none;
  font-size: 1.35rem;
  font-weight: 600;
  position: relative;
  transition: color .25s;
}
/* Shared ::after base */

.hv-27__link::after {
  content: '';
  position: absolute;
  left: 0;
  width: 100%;
  background: var(--st-color);
  transform: scaleX(0);
  transform-origin: left;
  transition: transform .32s cubic-bezier(.4,0,.2,1);
}
/* ── 1. Solid Strike ── */

.hv-27__link--solid::after {
  top: 50%;
  height: var(--st-thickness);
  margin-top: calc(var(--st-thickness) / -2);
}

.hv-27__link--solid:hover::after {
  transform: scaleX(1);
}

.hv-27__link--solid:hover {
  color: #888;
}
/* ── 2. Hair-thin ── */

.hv-27__link--thin::after {
  top: 50%;
  height: 1px;
  margin-top: -.5px;
  background: #fff;
  opacity: .7;
}

.hv-27__link--thin:hover::after {
  transform: scaleX(1);
}

.hv-27__link--thin:hover {
  color: #666;
}
/* ── 3. Chunky Strike ── */

.hv-27__link--thick::after {
  top: 44%;
  height: 6px;
  margin-top: -3px;
  border-radius: 3px;
  background: #f7a600;
  opacity: .85;
}

.hv-27__link--thick:hover::after {
  transform: scaleX(1);
}

.hv-27__link--thick:hover {
  color: #f7a600;
}
/* ── 4. Wavy Strike ── */

.hv-27__link--wavy::after {
  top: 54%;
  height: 4px;
  background: radial-gradient(ellipse 3px 2px at 3px 2px, #e05 100%, transparent) 0/6px 4px repeat-x, radial-gradient(ellipse 3px 2px at 3px 0px, transparent 100%, #e05) 3px/6px 4px repeat-x;
  background-color: transparent;
}

.hv-27__link--wavy:hover::after {
  transform: scaleX(1);
}

.hv-27__link--wavy:hover {
  color: #e05;
}
/* ── 5. Dashed Strike ── */

.hv-27__link--dashed::after {
  top: 50%;
  height: 2px;
  margin-top: -1px;
  background: repeating-linear-gradient(
      90deg,
      #7c6af7 0, #7c6af7 6px,
      transparent 6px, transparent 10px
    );
}

.hv-27__link--dashed:hover::after {
  transform: scaleX(1);
}

.hv-27__link--dashed:hover {
  color: #7c6af7;
}
/* ── 6. Double Strike ── */

.hv-27__link--double::before,
.hv-27__link--double::after {
  content: '';
  position: absolute;
  left: 0;
  width: 100%;
  height: 1.5px;
  background: #5cf;
  transform: scaleX(0);
}

.hv-27__link--double::before {
  top: 42%;
  transform-origin: right;
  transition: transform .3s cubic-bezier(.4,0,.2,1);
}

.hv-27__link--double::after {
  top: 56%;
  transform-origin: left;
  transition: transform .3s cubic-bezier(.4,0,.2,1) .06s;
}

.hv-27__link--double:hover::before,
.hv-27__link--double:hover::after {
  transform: scaleX(1);
}

.hv-27__link--double:hover {
  color: #5cf;
}

@media (prefers-reduced-motion: reduce) {
  .hv-27__link::before,
    .hv-27__link::after {
    transition: none !important;
  }
}
```
