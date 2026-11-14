---
source: "codefronts"
url: "https://codefronts.com/components/css-button-groups/pixel-matrix/"
title: "CSS Pixel Matrix Button Group with LED Segment Glow (Retro Display Buttons)"
section: "components"
category: "css-button-groups"
category_name: "CSS Button Groups"
description: "A button group that looks like a retro LED dot-matrix panel — each button is a grid of tiny pixels that light up amber/green when active, complete with…"
has_js: "false"
---

Here's a working CSS Button Group from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Pixel Matrix Button Group with LED Segment Glow (Retro Display Buttons)
Source: https://codefronts.com/components/css-button-groups/pixel-matrix/

A button group that looks like a retro LED dot-matrix panel — each button is a grid of tiny pixels that light up amber/green when active, complete with segment glow and a dark board bezel. The nostalgic-yet-modern 'CSS pixel matrix LED button group' for playful dashboards, retro UIs and hardware-style controls.
## HTML
```html
<section class="btn-17" aria-label="Pixel matrix LED button group demo">
  <div class="btn-17__board">
    <p class="btn-17__label">Transport</p>
    <div class="btn-17__keys" role="radiogroup" aria-label="Transport mode">
      <input type="radio" name="btn-17" id="btn-17-1" class="btn-17__in" checked>
      <label for="btn-17-1" class="btn-17__key btn-17__key--go" aria-label="Run"><span>RUN</span></label>
      <input type="radio" name="btn-17" id="btn-17-2" class="btn-17__in">
      <label for="btn-17-2" class="btn-17__key btn-17__key--wait" aria-label="Pause"><span>WAIT</span></label>
      <input type="radio" name="btn-17" id="btn-17-3" class="btn-17__in">
      <label for="btn-17-3" class="btn-17__key btn-17__key--stop" aria-label="Stop"><span>STOP</span></label>
    </div>
  </div>
</section>
```
## CSS
```css
.btn-17,
.btn-17 *,
.btn-17 *::before,
.btn-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.btn-17 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: radial-gradient(120% 120% at 50% 0%,#161616,#050505);
  padding: 44px 20px;
}

.btn-17__board {
  width: min(520px,100%);
  background: linear-gradient(180deg,#1c1c1c,#0e0e0e);
  border: 1px solid #2c2c2c;
  border-radius: 20px;
  padding: 24px;
  box-shadow: inset 0 2px 10px rgba(0,0,0,.8),0 30px 70px -40px #000;
}

.btn-17__label {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .24em;
  color: #5a5a5a;
  margin: 0 0 14px 2px;
}

.btn-17__keys {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 12px;
}

.btn-17__in {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.btn-17__key {
  --led: rgba(120,120,120,.22);
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 80px;
  border-radius: 12px;
  background: #0a0a0a;
  border: 1.5px solid #262626;
  cursor: pointer;
  overflow: hidden;
  box-shadow: inset 0 2px 6px rgba(0,0,0,.7);
}

.btn-17__key::before {
  content: "";
  position: absolute;
  inset: 0;
  background: radial-gradient(circle,var(--led) 30%,transparent 34%) 0 0/7px 7px;
  transition: background .25s,filter .25s;
}

.btn-17__key span {
  position: relative;
  z-index: 1;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 16px;
  font-weight: 800;
  letter-spacing: .12em;
  color: var(--led);
  text-shadow: none;
  transition: color .25s,text-shadow .25s;
}

.btn-17__key--go.btn-17__key {
}

.btn-17__in:checked + .btn-17__key--go {
  --led: #3dff6e;
  border-color: #1c7a3a;
}

.btn-17__in:checked + .btn-17__key--wait {
  --led: #ffb000;
  border-color: #8a6000;
}

.btn-17__in:checked + .btn-17__key--stop {
  --led: #ff4242;
  border-color: #8a2020;
}

.btn-17__in:checked + .btn-17__key::before {
  filter: drop-shadow(0 0 5px var(--led));
}

.btn-17__in:checked + .btn-17__key span {
  color: #fff;
  text-shadow: 0 0 8px var(--led),0 0 16px var(--led);
}

.btn-17__in:checked + .btn-17__key {
  box-shadow: inset 0 2px 6px rgba(0,0,0,.7),0 0 22px -6px var(--led);
}

.btn-17__key::after {
  content: "";
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(0deg,rgba(255,255,255,.04) 0 1px,transparent 1px 3px);
  pointer-events: none;
}

.btn-17__in:focus-visible + .btn-17__key {
  outline: 3px solid #fff;
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .btn-17__key::before,
    .btn-17__key span {
    transition: none;
  }
}
```
