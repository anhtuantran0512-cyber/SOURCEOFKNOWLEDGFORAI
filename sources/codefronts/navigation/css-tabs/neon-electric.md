---
source: "codefronts"
url: "https://codefronts.com/navigation/css-tabs/neon-electric/"
title: "Neon Electric"
section: "navigation"
category: "css-tabs"
category_name: "CSS Tabs"
description: "Each tab owns its own electric accent via a CSS custom property."
has_js: "false"
---

Here's a working CSS Tab from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neon Electric
Source: https://codefronts.com/navigation/css-tabs/neon-electric/

Each tab owns its own electric accent via a CSS custom property. The active tab lights up with a neon border and a soft outer glow in its color. Pure CSS via radio inputs and `:has()` panel switching.
## HTML
```html
<div class="tt22">
  <nav class="tt22n">
    <input type="radio" name="tt22" id="tt22-r1" checked />
    <label class="tt22b" for="tt22-r1" style="--c: #ff3df5">Pulse</label>
    <input type="radio" name="tt22" id="tt22-r2" />
    <label class="tt22b" for="tt22-r2" style="--c: #3df5ff">Wave</label>
    <input type="radio" name="tt22" id="tt22-r3" />
    <label class="tt22b" for="tt22-r3" style="--c: #caff3d">Surge</label>
    <input type="radio" name="tt22" id="tt22-r4" />
    <label class="tt22b" for="tt22-r4" style="--c: #ff913d">Bloom</label>
  </nav>
  <div class="tt22p">Pulse — short, rhythmic bursts of light.</div>
  <div class="tt22p">Wave — continuous oscillating motion.</div>
  <div class="tt22p">Surge — sudden upward power swell.</div>
  <div class="tt22p">Bloom — soft expanding glow front.</div>
</div>
```
## CSS
```css
.tt22 {
  background: #0c0c12;
  padding: 22px 18px;
  font-family: ui-monospace, monospace;
  min-height: 100vh;
  box-sizing: border-box;
  width: 100%;
}

.tt22n {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  min-width: 0;
}

.tt22n input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.tt22b {
  flex: 1;
  min-width: 0;
  padding: 11px 12px;
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 6px;
  background: transparent;
  font: 700 11px/1 ui-monospace, monospace;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: rgba(255, 255, 255, 0.45);
  cursor: pointer;
  text-align: center;
  transition: color 0.25s, border-color 0.25s, box-shadow 0.3s, background 0.25s;
  white-space: nowrap;
}

.tt22b:hover {
  color: rgba(255, 255, 255, 0.85);
  border-color: rgba(255, 255, 255, 0.2);
}

.tt22n input:checked + .tt22b {
  color: var(--c);
  border-color: var(--c);
  background: color-mix(in srgb, var(--c) 12%, transparent);
  box-shadow: 0 0 12px color-mix(in srgb, var(--c) 50%, transparent), inset 0 0 8px color-mix(in srgb, var(--c) 25%, transparent);
}

.tt22n input:focus-visible + .tt22b {
  outline: 2px dashed var(--c);
  outline-offset: 2px;
}

.tt22p {
  display: none;
  padding-top: 18px;
  font: 12px/1.55 ui-monospace, monospace;
  color: rgba(255, 255, 255, 0.6);
  letter-spacing: 0.04em;
}

.tt22:has(#tt22-r1:checked) .tt22p:nth-of-type(1),
.tt22:has(#tt22-r2:checked) .tt22p:nth-of-type(2),
.tt22:has(#tt22-r3:checked) .tt22p:nth-of-type(3),
.tt22:has(#tt22-r4:checked) .tt22p:nth-of-type(4) {
  display: block;
}
```
