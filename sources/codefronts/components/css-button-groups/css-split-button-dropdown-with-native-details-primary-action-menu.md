---
source: "codefronts"
url: "https://codefronts.com/components/css-button-groups/css-split-button-dropdown-with-native-details-primary-action-menu/"
title: "CSS Split Button Dropdown with Native <details> (Primary Action + Menu)"
section: "components"
category: "css-button-groups"
category_name: "CSS Button Groups"
description: "The split button every app toolbar needs: a primary action fused to a caret that opens a dropdown of alternates — Save / Save as / Save a copy."
has_js: "false"
---

Here's a working CSS Button Group from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Split Button Dropdown with Native <details> (Primary Action + Menu)
Source: https://codefronts.com/components/css-button-groups/css-split-button-dropdown-with-native-details-primary-action-menu/

The split button every app toolbar needs: a primary action fused to a caret that opens a dropdown of alternates — Save / Save as / Save a copy. Built on native <details>/<summary> so it opens with zero JavaScript, closes on outside interaction, and keeps full keyboard and screen-reader disclosure semantics. The definitive 'CSS split button dropdown' recipe.
## HTML
```html
<section class="btn-06" aria-label="Split button dropdown demo">
  <div class="btn-06__split">
    <button type="button" class="btn-06__primary">Save changes</button>
    <details class="btn-06__more">
      <summary class="btn-06__caret" aria-label="More save options"></summary>
      <div class="btn-06__menu" role="menu">
        <button type="button" class="btn-06__item" role="menuitem">Save as…</button>
        <button type="button" class="btn-06__item" role="menuitem">Save a copy</button>
        <button type="button" class="btn-06__item" role="menuitem">Save as template</button>
        <div class="btn-06__sep"></div>
        <button type="button" class="btn-06__item btn-06__item--danger" role="menuitem">Discard changes</button>
      </div>
    </details>
  </div>
</section>
```
## CSS
```css
.btn-06,
.btn-06 *,
.btn-06 *::before,
.btn-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.btn-06 {
  --accent: oklch(0.72 0.17 55);
  --accent-d: oklch(0.62 0.17 55);
  --ink: #3a2508;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  background: linear-gradient(160deg,#fff7ea,#ffedd0);
  padding: 120px 20px;
}

.btn-06__split {
  position: relative;
  display: inline-flex;
  border-radius: 14px;
  box-shadow: 0 12px 30px -14px rgba(150,90,10,.7);
}

.btn-06__primary {
  border: none;
  background: var(--accent);
  color: var(--ink);
  font-size: 15.5px;
  font-weight: 750;
  padding: 0 22px;
  height: 50px;
  border-radius: 14px 0 0 14px;
  cursor: pointer;
  transition: filter .15s;
}

.btn-06__primary:hover {
  filter: brightness(1.05);
}

.btn-06__more {
  position: relative;
}

.btn-06__caret {
  list-style: none;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 48px;
  height: 50px;
  background: var(--accent-d);
  border-radius: 0 14px 14px 0;
  cursor: pointer;
  position: relative;
  border-left: 1px solid rgba(90,55,5,.25);
}

.btn-06__caret::-webkit-details-marker {
  display: none;
}

.btn-06__caret::marker {
  content: "";
}

.btn-06__caret::after {
  content: "";
  width: 9px;
  height: 9px;
  border-right: 2.5px solid var(--ink);
  border-bottom: 2.5px solid var(--ink);
  transform: translateY(-2px) rotate(45deg);
  transition: transform .3s;
}

.btn-06__more[open] .btn-06__caret::after {
  transform: translateY(2px) rotate(-135deg);
}

.btn-06__menu {
  position: absolute;
  top: calc(100% + 8px);
  right: 0;
  min-width: 220px;
  background: #fff;
  border: 1px solid #f0dcbb;
  border-radius: 14px;
  padding: 7px;
  z-index: 20;
  box-shadow: 0 24px 50px -22px rgba(120,70,5,.55);
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.btn-06__more[open] .btn-06__menu {
  animation: btn-06-in .22s cubic-bezier(.2,.7,.3,1);
}

@keyframes btn-06-in {
  from {
    opacity: 0;
    translate: 0 -8px;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

.btn-06__item {
  text-align: left;
  border: none;
  background: none;
  font-size: 14.5px;
  font-weight: 600;
  color: #5a3f18;
  padding: 11px 13px;
  border-radius: 9px;
  cursor: pointer;
  transition: background .12s;
}

.btn-06__item:hover {
  background: #fdf1dd;
}

.btn-06__item--danger {
  color: #b23b2e;
}

.btn-06__item--danger:hover {
  background: #fdeae7;
}

.btn-06__sep {
  height: 1px;
  background: #f0dcbb;
  margin: 5px 6px;
}

.btn-06__primary:focus-visible,
.btn-06__caret:focus-visible,
.btn-06__item:focus-visible {
  outline: 3px solid var(--accent-d);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .btn-06__caret::after,
    .btn-06__more[open] .btn-06__menu {
    transition: none;
    animation: none;
  }
}
```
