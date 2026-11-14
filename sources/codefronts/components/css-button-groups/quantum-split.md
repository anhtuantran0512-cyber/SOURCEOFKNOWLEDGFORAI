---
source: "codefronts"
url: "https://codefronts.com/components/css-button-groups/quantum-split/"
title: "CSS Split Button with Quantum Chevron Reveal (Animated Menu Materialize)"
section: "components"
category: "css-button-groups"
category_name: "CSS Button Groups"
description: "A split button where the dropdown doesn't just appear — it materializes: on opening, the caret splits into a quantum shimmer and menu items phase in one…"
has_js: "false"
---

Here's a working CSS Button Group from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Split Button with Quantum Chevron Reveal (Animated Menu Materialize)
Source: https://codefronts.com/components/css-button-groups/quantum-split/

A split button where the dropdown doesn't just appear — it materializes: on opening, the caret splits into a quantum shimmer and menu items phase in one after another with a clip-path wipe and blur-in. A cinematic 'CSS split button quantum chevron reveal' built on native <details>, so the drama is pure CSS and the semantics stay honest.
## HTML
```html
<section class="btn-15" aria-label="Quantum chevron split button demo">
  <div class="btn-15__split">
    <button type="button" class="btn-15__primary">Deploy</button>
    <details class="btn-15__more">
      <summary class="btn-15__caret" aria-label="More deploy options"></summary>
      <div class="btn-15__menu" role="menu">
        <button type="button" class="btn-15__item" role="menuitem">Deploy to preview</button>
        <button type="button" class="btn-15__item" role="menuitem">Deploy to staging</button>
        <button type="button" class="btn-15__item" role="menuitem">Deploy to production</button>
        <button type="button" class="btn-15__item" role="menuitem">Roll back last</button>
      </div>
    </details>
  </div>
</section>
```
## CSS
```css
.btn-15,
.btn-15 *,
.btn-15 *::before,
.btn-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.btn-15 {
  --a1: oklch(0.8 0.15 200);
  --a2: oklch(0.62 0.2 300);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  background: radial-gradient(120% 100% at 50% 0%,#0e1626,#060810);
  padding: 120px 20px;
}

.btn-15__split {
  position: relative;
  display: inline-flex;
  border-radius: 14px;
  box-shadow: 0 0 0 1px rgba(120,200,255,.2),0 20px 50px -24px rgba(30,120,255,.6);
}

.btn-15__primary {
  border: none;
  background: linear-gradient(120deg,var(--a1),var(--a2));
  color: #07101c;
  font-size: 15.5px;
  font-weight: 800;
  padding: 0 24px;
  height: 52px;
  border-radius: 14px 0 0 14px;
  cursor: pointer;
  transition: filter .15s;
}

.btn-15__primary:hover {
  filter: brightness(1.1);
}

.btn-15__more {
  position: relative;
}

.btn-15__caret {
  list-style: none;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 50px;
  height: 52px;
  background: rgba(255,255,255,.06);
  border-radius: 0 14px 14px 0;
  cursor: pointer;
  position: relative;
  border-left: 1px solid rgba(150,210,255,.25);
  backdrop-filter: blur(4px);
}

.btn-15__caret::-webkit-details-marker {
  display: none;
}

.btn-15__caret::marker {
  content: "";
}

.btn-15__caret::after,
.btn-15__caret::before {
  content: "";
  position: absolute;
  width: 9px;
  height: 9px;
  border-right: 2.5px solid var(--a1);
  border-bottom: 2.5px solid var(--a1);
  transform: translateY(-2px) rotate(45deg);
  transition: transform .3s,opacity .3s;
}

.btn-15__caret::before {
  border-color: var(--a2);
  opacity: 0;
}

.btn-15__more[open] .btn-15__caret::after {
  transform: translateY(2px) rotate(-135deg) translateX(2px);
}

.btn-15__more[open] .btn-15__caret::before {
  transform: translateY(0) rotate(-135deg) translateX(-3px);
  opacity: .8;
}

.btn-15__menu {
  position: absolute;
  top: calc(100% + 10px);
  right: 0;
  min-width: 230px;
  background: rgba(14,22,40,.92);
  border: 1px solid rgba(120,200,255,.22);
  border-radius: 14px;
  padding: 7px;
  z-index: 20;
  box-shadow: 0 30px 60px -24px rgba(20,80,220,.7);
  display: flex;
  flex-direction: column;
  gap: 2px;
  backdrop-filter: blur(14px);
}

.btn-15__more[open] .btn-15__menu {
  animation: btn-15-wipe .35s cubic-bezier(.2,.7,.3,1) both;
}

@keyframes btn-15-wipe {
  from {
    clip-path: inset(0 0 100% 0 round 14px);
    opacity: 0;
  }

  to {
    clip-path: inset(0 0 0 0 round 14px);
    opacity: 1;
  }
}

.btn-15__item {
  text-align: left;
  border: none;
  background: none;
  font-size: 14.5px;
  font-weight: 650;
  color: #cfe2f5;
  padding: 11px 13px;
  border-radius: 9px;
  cursor: pointer;
  transition: background .12s;
}

.btn-15__more[open] .btn-15__item {
  animation: btn-15-phase .4s both;
}

.btn-15__more[open] .btn-15__item:nth-child(1) {
  animation-delay: .05s;
}

.btn-15__more[open] .btn-15__item:nth-child(2) {
  animation-delay: .11s;
}

.btn-15__more[open] .btn-15__item:nth-child(3) {
  animation-delay: .17s;
}

.btn-15__more[open] .btn-15__item:nth-child(4) {
  animation-delay: .23s;
}

@keyframes btn-15-phase {
  from {
    opacity: 0;
    filter: blur(6px);
    translate: 0 -6px;
  }

  to {
    opacity: 1;
    filter: blur(0);
    translate: 0 0;
  }
}

.btn-15__item:hover {
  background: rgba(120,200,255,.12);
}

.btn-15__primary:focus-visible,
.btn-15__caret:focus-visible,
.btn-15__item:focus-visible {
  outline: 3px solid var(--a1);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .btn-15__more[open] .btn-15__menu,
    .btn-15__more[open] .btn-15__item {
    animation: none;
  }

  .btn-15__caret::after,
    .btn-15__caret::before {
    transition: none;
  }
}
```
