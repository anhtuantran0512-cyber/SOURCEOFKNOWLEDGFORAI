---
source: "codefronts"
url: "https://codefronts.com/components/css-button-groups/cellular-toggle/"
title: "CSS Format Toggle Button Group with Conic Fill (Radial Sweep Select)"
section: "components"
category: "css-button-groups"
category_name: "CSS Button Groups"
description: "An export-format toggle — PNG / JPG / WebP / AVIF — where selecting an option sweeps a conic-gradient fill around the button like a radar wipe before…"
has_js: "false"
---

Here's a working CSS Button Group from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Format Toggle Button Group with Conic Fill (Radial Sweep Select)
Source: https://codefronts.com/components/css-button-groups/cellular-toggle/

An export-format toggle — PNG / JPG / WebP / AVIF — where selecting an option sweeps a conic-gradient fill around the button like a radar wipe before settling into a solid state. A striking 'CSS format toggle button group conic fill' using an @property-animated angle, with real radios keeping it single-select and accessible.
## HTML
```html
<section class="btn-16" aria-label="Conic fill format toggle demo">
  <div class="btn-16__wrap">
    <p class="btn-16__label">Export format</p>
    <div class="btn-16__group" role="radiogroup" aria-label="Export format">
      <input type="radio" name="btn-16" id="btn-16-1" class="btn-16__in" checked>
      <label for="btn-16-1" class="btn-16__cell" style="--c:#ff5d73">PNG</label>
      <input type="radio" name="btn-16" id="btn-16-2" class="btn-16__in">
      <label for="btn-16-2" class="btn-16__cell" style="--c:#ffb44d">JPG</label>
      <input type="radio" name="btn-16" id="btn-16-3" class="btn-16__in">
      <label for="btn-16-3" class="btn-16__cell" style="--c:#4dd9c4">WebP</label>
      <input type="radio" name="btn-16" id="btn-16-4" class="btn-16__in">
      <label for="btn-16-4" class="btn-16__cell" style="--c:#7d9bff">AVIF</label>
    </div>
  </div>
</section>
```
## CSS
```css
@property --btn-16-a {
  syntax: "<angle>";
  inherits: false;
  initial-value: 0deg;
}

.btn-16,
.btn-16 *,
.btn-16 *::before,
.btn-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.btn-16 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(160deg,#14121c,#0c0a12);
  padding: 44px 20px;
}

.btn-16__wrap {
  width: min(500px,100%);
}

.btn-16__label {
  font-size: 12px;
  font-weight: 800;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: #b8b0d0;
  margin: 0 0 14px 2px;
}

.btn-16__group {
  display: grid;
  grid-template-columns: repeat(4,1fr);
  gap: 12px;
}

.btn-16__in {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.btn-16__cell {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 66px;
  font-size: 15px;
  font-weight: 800;
  letter-spacing: .02em;
  color: #8b84a6;
  background: #1a1726;
  border: 1.5px solid #2a2540;
  border-radius: 16px;
  cursor: pointer;
  overflow: hidden;
  transition: color .3s,border-color .3s;
}

.btn-16__cell::before {
  content: "";
  position: absolute;
  inset: 0;
  background: conic-gradient(from -90deg,var(--c) var(--btn-16-a),transparent 0);
  opacity: 0;
  transition: opacity .2s;
}

.btn-16__cell:hover {
  color: #d6cff0;
  border-color: #3a3358;
}

.btn-16__in:checked + .btn-16__cell {
  color: #fff;
  border-color: var(--c);
}

.btn-16__in:checked + .btn-16__cell::before {
  opacity: .9;
  animation: btn-16-sweep .65s cubic-bezier(.3,.7,.3,1) forwards;
}

@keyframes btn-16-sweep {
  from {
    --btn-16-a: 0deg;
  }

  to {
    --btn-16-a: 360deg;
  }
}

.btn-16__cell span,
.btn-16__cell {
  z-index: 0;
}

.btn-16__in:checked + .btn-16__cell {
  z-index: 1;
}

.btn-16__cell {
  isolation: isolate;
}

.btn-16__in:checked + .btn-16__cell {
  text-shadow: 0 1px 6px rgba(0,0,0,.5);
}

.btn-16__in:focus-visible + .btn-16__cell {
  outline: 3px solid var(--c);
  outline-offset: 2px;
}

@supports not (background: conic-gradient(from 0deg,red var(--btn-16-a),transparent 0)) {
  .btn-16__in:checked + .btn-16__cell {
    background: var(--c);
  }
}

@media (prefers-reduced-motion: reduce) {
  .btn-16__in:checked + .btn-16__cell::before {
    animation: none;
    --btn-16-a: 360deg;
  }
}
```
