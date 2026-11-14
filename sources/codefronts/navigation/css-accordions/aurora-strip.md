---
source: "codefronts"
url: "https://codefronts.com/navigation/css-accordions/aurora-strip/"
title: "Aurora Strip Horizontal Accordion — Animated Gradient Glow Panels"
section: "navigation"
category: "css-accordions"
category_name: "CSS Accordions — Vertical & Horizontal"
description: "Dark glass columns over a living aurora: each collapsed strip leaks a slit of moving color, and the open panel becomes a window onto the full animation —…"
has_js: "false"
---

Here's a working CSS Accordions — Vertical & Horizontal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Aurora Strip Horizontal Accordion — Animated Gradient Glow Panels
Source: https://codefronts.com/navigation/css-accordions/aurora-strip/

Dark glass columns over a living aurora: each collapsed strip leaks a slit of moving color, and the open panel becomes a window onto the full animation — layered conic and radial gradients drifting on independent timings via animated hue rotation. The 'animated gradient border/panel' effect at accordion scale.
## HTML
```html
<section class="acc-22" aria-label="Aurora strip animated gradient accordion demo">
  <div class="acc-22__stage" role="group" aria-label="Product principles">
    <div class="acc-22__aurora"></div>
    <div class="acc-22__panel">
      <input type="radio" name="acc-22" id="acc-22-a" checked>
      <label class="acc-22__face" for="acc-22-a"><span class="acc-22__tab">Calm</span>
        <span class="acc-22__body"><b>Calm by default</b><p>No badges, no streaks, no red dots. The interface waits for you — never the other way around.</p></span>
      </label>
    </div>
    <div class="acc-22__panel">
      <input type="radio" name="acc-22" id="acc-22-b">
      <label class="acc-22__face" for="acc-22-b"><span class="acc-22__tab">Ambient</span>
        <span class="acc-22__body"><b>Ambient awareness</b><p>State lives in color and light, not notification counts. You sense change peripherally, like weather.</p></span>
      </label>
    </div>
    <div class="acc-22__panel">
      <input type="radio" name="acc-22" id="acc-22-c">
      <label class="acc-22__face" for="acc-22-c"><span class="acc-22__tab">Yours</span>
        <span class="acc-22__body"><b>Yours to keep</b><p>Local-first files, open formats, and an export button that produces something actually useful.</p></span>
      </label>
    </div>
  </div>
</section>
```
## CSS
```css
@property --acc-22-hue {
  syntax: "<number>";
  inherits: true;
  initial-value: 210;
}

.acc-22,
.acc-22 *,
.acc-22 *::before,
.acc-22 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.acc-22 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #0b0d14;
  padding: 44px 24px;
}

.acc-22__stage {
  position: relative;
  display: flex;
  gap: 8px;
  width: min(780px,100%);
  height: 380px;
  border-radius: 20px;
  overflow: hidden;
  padding: 10px;
  background: #0e1120;
}

.acc-22__aurora {
  position: absolute;
  inset: -30%;
  background: radial-gradient(50% 60% at 25% 30%,hsl(var(--acc-22-hue) 80% 60% / .5),transparent 70%),radial-gradient(45% 55% at 75% 40%,hsl(calc(var(--acc-22-hue) + 80) 75% 55% / .45),transparent 70%),radial-gradient(60% 50% at 50% 85%,hsl(calc(var(--acc-22-hue) + 160) 70% 50% / .4),transparent 70%);
  filter: blur(30px);
  animation: acc-22-cycle 24s linear infinite;
}

@keyframes acc-22-cycle {
  to {
    --acc-22-hue: 570;
  }
}

.acc-22__aurora::after {
  content: "";
  position: absolute;
  inset: 0;
  background: conic-gradient(from 200deg at 50% 50%,transparent 0 40%,rgba(255,255,255,.08) 50%,transparent 60% 100%);
  animation: acc-22-shimmer 9s ease-in-out infinite alternate;
}

@keyframes acc-22-shimmer {
  from {
    translate: -12% -6%;
  }

  to {
    translate: 12% 6%;
  }
}

.acc-22__panel {
  position: relative;
  z-index: 1;
  display: flex;
  flex-grow: 1;
  flex-basis: 0;
  min-width: 64px;
  transition: flex-grow .55s cubic-bezier(.4,0,.2,1);
}

.acc-22__panel:has(input:checked) {
  flex-grow: 5;
}

.acc-22__panel input {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.acc-22__face {
  position: relative;
  flex: 1;
  display: block;
  cursor: pointer;
  border-radius: 12px;
  overflow: hidden;
  background: rgba(8,10,20,.72);
  border: 1px solid rgba(255,255,255,.12);
  backdrop-filter: blur(2px);
  transition: background .4s,border-color .4s;
}

.acc-22__panel:has(input:checked) .acc-22__face {
  background: rgba(8,10,20,.28);
  border-color: rgba(255,255,255,.28);
}

.acc-22__face:hover {
  border-color: rgba(255,255,255,.3);
}

.acc-22__tab {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  writing-mode: vertical-rl;
  rotate: 180deg;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: rgba(255,255,255,.7);
  transition: opacity .25s;
}

.acc-22__panel:has(input:checked) .acc-22__tab {
  opacity: 0;
}

.acc-22__body {
  position: absolute;
  inset: auto 0 0 0;
  padding: 70px 24px 22px;
  background: linear-gradient(transparent,rgba(5,6,14,.8));
  display: flex;
  flex-direction: column;
  gap: 8px;
  opacity: 0;
  translate: 0 10px;
  transition: opacity .35s .2s,translate .35s .2s;
}

.acc-22__panel:has(input:checked) .acc-22__body {
  opacity: 1;
  translate: 0 0;
}

.acc-22__body b {
  font-size: 22px;
  font-weight: 800;
  color: rgba(255,255,255,.94);
  letter-spacing: -.01em;
}

.acc-22__body p {
  font-size: 14px;
  line-height: 1.6;
  color: rgba(255,255,255,.78);
  max-width: 46ch;
}

.acc-22__panel:has(input:focus-visible) .acc-22__face {
  outline: 3px solid #fff;
  outline-offset: 2px;
}

@media (max-width: 600px) {
  .acc-22__stage {
    flex-direction: column;
    height: auto;
  }

  .acc-22__panel {
    min-height: 60px;
  }

  .acc-22__panel:has(input:checked) {
    min-height: 250px;
  }

  .acc-22__tab {
    writing-mode: horizontal-tb;
    rotate: none;
    justify-content: flex-start;
    padding: 0 20px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .acc-22__aurora,
    .acc-22__aurora::after {
    animation: none;
  }

  .acc-22__panel,
    .acc-22__body,
    .acc-22__tab {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a registered @property number animates the aurora's hue 0→360 while a second unsynchronized shimmer loop crosses it; glass panels above dim or expose the shared layer as radios toggle. */
```
