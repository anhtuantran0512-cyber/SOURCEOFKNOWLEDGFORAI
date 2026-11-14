---
source: "codefronts"
url: "https://codefronts.com/layouts/css-aspect-ratio/css-aspect-ratio-media-query-orientation/"
title: "CSS Aspect Ratio Media Query Orientation"
section: "layouts"
category: "css-aspect-ratio"
category_name: "CSS Aspect Ratio Demos"
description: "Aspect-ratio as a query, not a property: this instrument panel reorganizes itself with @media (orientation:…) and (min-aspect-ratio:16/9) — reacting to the…"
has_js: "false"
---

Here's a working CSS Aspect Ratio Demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Aspect Ratio Media Query Orientation
Source: https://codefronts.com/layouts/css-aspect-ratio/css-aspect-ratio-media-query-orientation/

Aspect-ratio as a query, not a property: this instrument panel reorganizes itself with @media (orientation:…) and (min-aspect-ratio:16/9) — reacting to the viewport's shape, which width breakpoints can't see — and its HUD lights up whichever queries currently match, live. The star exhibit is a resize:both playground box that classifies its own proportions (portrait → square → landscape → cinematic) using container aspect-ratio queries: grab its corner and watch a component respond to its shape, not the screen's.
## HTML
```html
<section class="car-13" aria-label="Aspect ratio media query demo">
  <div class="car-13__stage" id="car13-top">
    <header class="car-13__bar">
      <p class="car-13__brand">RATIO/LAB<span>viewport &amp; container shape instruments</span></p>
      <p class="car-13__now" aria-live="polite">pane is <b class="car-13__now--land">landscape</b><b class="car-13__now--port">portrait</b><b class="car-13__now--cine"> · wider than 16:9</b></p>
    </header>
    <div class="car-13__app">
      <aside class="car-13__hud" aria-label="Live media query matches">
        <h2>@media — matching now</h2>
        <ul>
          <li class="car-13__mq car-13__mq--land"><i aria-hidden="true"></i><code>(orientation: landscape)</code></li>
          <li class="car-13__mq car-13__mq--port"><i aria-hidden="true"></i><code>(orientation: portrait)</code></li>
          <li class="car-13__mq car-13__mq--sq"><i aria-hidden="true"></i><code>(max-aspect-ratio: 1/1)</code></li>
          <li class="car-13__mq car-13__mq--wide"><i aria-hidden="true"></i><code>(min-aspect-ratio: 3/2)</code></li>
          <li class="car-13__mq car-13__mq--cine"><i aria-hidden="true"></i><code>(min-aspect-ratio: 16/9)</code></li>
        </ul>
        <p class="car-13__hudnote">Drag the pane's <em>shape</em>, not just its width — these react to width ÷ height. This layout itself stacks when the pane goes portrait.</p>
      </aside>
      <main class="car-13__lab-zone">
        <h2>Container shape playground <span>— drag the corner handle ↘</span></h2>
        <div class="car-13__lab" aria-label="Resizable box that classifies its own aspect ratio">
          <div class="car-13__reading car-13__reading--tall"><b>PORTRAIT</b><span>ratio &lt; 3:4 — stack everything, one thumb column</span><i class="car-13__mini car-13__mini--tall" aria-hidden="true"></i></div>
          <div class="car-13__reading car-13__reading--sq"><b>SQUARE-ISH</b><span>3:4 – 3:2 — balanced grid, 2-up cards</span><i class="car-13__mini car-13__mini--sq" aria-hidden="true"></i></div>
          <div class="car-13__reading car-13__reading--land"><b>LANDSCAPE</b><span>3:2 – 2:1 — sidebar + content earn their keep</span><i class="car-13__mini car-13__mini--land" aria-hidden="true"></i></div>
          <div class="car-13__reading car-13__reading--cine"><b>CINEMATIC</b><span>&gt; 2:1 — letterbox media, span the panorama</span><i class="car-13__mini car-13__mini--cine" aria-hidden="true"></i></div>
          <span class="car-13__handle" aria-hidden="true">↘</span>
        </div>
        <p class="car-13__labnote"><code>container: car13lab / size</code> + <code>@container (min-aspect-ratio: …)</code> — the box consults its own shape; the viewport is never asked.</p>
      </main>
    </div>
    <footer class="car-13__foot">Width says how much room; ratio says what shape the room is. A demo from the CodeFronts aspect-ratio collection.</footer>
  </div>
</section>
```
## CSS
```css
.car-13,
.car-13 *,
.car-13 *::before,
.car-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.car-13 {
  --bg: oklch(0.15 0.015 170);
  --panel: oklch(0.19 0.02 170);
  --ink: oklch(0.95 0.01 160);
  --mut: oklch(0.65 0.03 165);
  --line: oklch(0.3 0.03 170);
  --acc: oklch(0.82 0.17 155);
  --amber: oklch(0.8 0.14 85);
  font-family: ui-monospace,'Cascadia Code',Menlo,Consolas,monospace;
  color: var(--ink);
  container-type: inline-size;
  display: block;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: var(--bg);
}

.car-13__stage {
  width: 100%;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  background: radial-gradient(120% 90% at 85% -10%,oklch(0.22 0.04 170/.8),transparent 60%),var(--bg);
}

.car-13__bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  flex-wrap: wrap;
  padding: 16px clamp(16px,4cqi,40px);
  border-bottom: 1px solid var(--line);
}

.car-13__brand {
  font-size: 15px;
  font-weight: 800;
  letter-spacing: .12em;
}

.car-13__brand span {
  display: block;
  font-size: 10px;
  font-weight: 400;
  letter-spacing: .04em;
  color: var(--mut);
  margin-top: 2px;
}

.car-13__now {
  font-size: 12px;
  color: var(--mut);
}

.car-13__now b {
  color: var(--acc);
  font-weight: 700;
}

.car-13__now--port {
  display: none;
}

.car-13__now--cine {
  display: none;
  color: var(--amber);
}

.car-13__app {
  flex: 1;
  display: grid;
  grid-template-columns: minmax(280px,340px) minmax(0,1fr);
  gap: clamp(14px,2.5cqi,26px);
  padding: clamp(14px,2.5cqi,26px) clamp(16px,4cqi,40px);
  align-items: start;
  min-height: 0;
}

.car-13__hud {
  border: 1px solid var(--line);
  border-radius: 14px;
  background: var(--panel);
  padding: 16px;
}

.car-13__hud h2,
.car-13__lab-zone h2 {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--mut);
}

.car-13__lab-zone h2 span {
  text-transform: none;
  letter-spacing: 0;
  color: var(--acc);
}

.car-13__hud ul {
  list-style: none;
  margin-top: 12px;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.car-13__mq {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 9px 10px;
  border-radius: 9px;
  border: 1px solid transparent;
  transition: background .25s,border-color .25s;
}

.car-13__mq i {
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: oklch(0.35 0.02 170);
  flex: none;
  transition: background .25s,box-shadow .25s;
}

.car-13__mq code {
  font-size: 11.5px;
  color: var(--mut);
}

.car-13__hudnote {
  margin-top: 14px;
  font-size: 11px;
  line-height: 1.6;
  color: var(--mut);
}

.car-13__hudnote em {
  font-style: normal;
  color: var(--amber);
}

.car-13__lab-zone {
  min-width: 0;
}

.car-13__lab {
  position: relative;
  margin-top: 12px;
  width: min(100%,560px);
  height: 300px;
  min-width: 220px;
  min-height: 150px;
  max-width: 100%;
  resize: both;
  overflow: hidden;
  border: 1.5px solid var(--line);
  border-radius: 14px;
  background: linear-gradient(140deg,var(--panel),oklch(0.16 0.02 190));
  container: car13lab/size;
  display: grid;
  place-items: center;
  padding: 18px;
}

.car-13__handle {
  position: absolute;
  right: 6px;
  bottom: 2px;
  font-size: 14px;
  color: var(--acc);
  pointer-events: none;
  animation: car13-nudge 1.6s ease-in-out infinite;
}

@keyframes car13-nudge {
  0%,
    100% {
    translate: 0 0;
  }

  50% {
    translate: 3px 3px;
  }
}

.car-13__reading {
  display: none;
  text-align: center;
  max-width: 44ch;
  flex-direction: column;
  align-items: center;
  gap: 8px;
}

.car-13__reading b {
  font-size: clamp(18px,6cqi,30px);
  letter-spacing: .18em;
  font-weight: 800;
}

.car-13__reading span {
  font-size: 12px;
  line-height: 1.5;
  color: var(--mut);
}

.car-13__mini {
  display: block;
  border: 1.5px dashed color-mix(in oklch,var(--acc) 55%,var(--line));
  border-radius: 6px;
  margin-top: 6px;
  background: oklch(0.25 0.05 165/.4);
}

.car-13__mini--tall {
  width: 34px;
  aspect-ratio: 9/16;
}

.car-13__mini--sq {
  width: 52px;
  aspect-ratio: 1;
}

.car-13__mini--land {
  width: 86px;
  aspect-ratio: 16/9;
}

.car-13__mini--cine {
  width: 110px;
  aspect-ratio: 21/8;
}

@container car13lab (max-aspect-ratio: 3/4) {
  .car-13__reading--tall {
    display: flex;
  }
}

@container car13lab (min-aspect-ratio: 3/4) and (max-aspect-ratio: 3/2) {
  .car-13__reading--sq {
    display: flex;
  }
}

@container car13lab (min-aspect-ratio: 3/2) and (max-aspect-ratio: 2/1) {
  .car-13__reading--land {
    display: flex;
  }
}

@container car13lab (min-aspect-ratio: 2/1) {
  .car-13__reading--cine {
    display: flex;
    color: var(--amber);
  }
}

@container car13lab (min-aspect-ratio: 2/1) {
  .car-13__lab {
    border-color: color-mix(in oklch,var(--amber) 50%,var(--line));
  }
}

.car-13__labnote {
  margin-top: 12px;
  font-size: 11.5px;
  line-height: 1.6;
  color: var(--mut);
}

.car-13__labnote code {
  background: oklch(0.24 0.03 170);
  padding: 2px 6px;
  border-radius: 5px;
  color: var(--acc);
  font-size: .95em;
}

.car-13__foot {
  padding: 12px clamp(16px,4cqi,40px) 24px;
  border-top: 1px solid var(--line);
  font-size: 11.5px;
  color: var(--mut);
}

@media (orientation: landscape) {
  .car-13__mq--land {
    background: oklch(0.24 0.04 165/.7);
    border-color: color-mix(in oklch,var(--acc) 35%,transparent);
  }

  .car-13__mq--land i {
    background: var(--acc);
    box-shadow: 0 0 10px var(--acc);
  }

  .car-13__mq--land code {
    color: var(--ink);
  }
}

@media (orientation: portrait) {
  .car-13__mq--port {
    background: oklch(0.24 0.04 165/.7);
    border-color: color-mix(in oklch,var(--acc) 35%,transparent);
  }

  .car-13__mq--port i {
    background: var(--acc);
    box-shadow: 0 0 10px var(--acc);
  }

  .car-13__mq--port code {
    color: var(--ink);
  }

  .car-13__now--land {
    display: none;
  }

  .car-13__now--port {
    display: inline;
  }

  .car-13__app {
    grid-template-columns: 1fr;
  }
}

@media (max-aspect-ratio: 1/1) {
  .car-13__mq--sq {
    background: oklch(0.24 0.04 165/.7);
    border-color: color-mix(in oklch,var(--acc) 35%,transparent);
  }

  .car-13__mq--sq i {
    background: var(--acc);
    box-shadow: 0 0 10px var(--acc);
  }

  .car-13__mq--sq code {
    color: var(--ink);
  }
}

@media (min-aspect-ratio: 3/2) {
  .car-13__mq--wide {
    background: oklch(0.24 0.04 165/.7);
    border-color: color-mix(in oklch,var(--acc) 35%,transparent);
  }

  .car-13__mq--wide i {
    background: var(--acc);
    box-shadow: 0 0 10px var(--acc);
  }

  .car-13__mq--wide code {
    color: var(--ink);
  }
}

@media (min-aspect-ratio: 16/9) {
  .car-13__mq--cine {
    background: oklch(0.27 0.05 90/.5);
    border-color: color-mix(in oklch,var(--amber) 40%,transparent);
  }

  .car-13__mq--cine i {
    background: var(--amber);
    box-shadow: 0 0 10px var(--amber);
  }

  .car-13__mq--cine code {
    color: var(--ink);
  }

  .car-13__now--cine {
    display: inline;
  }
}

@media (prefers-reduced-motion: reduce) {
  .car-13__handle {
    animation: none;
  }

  .car-13 * {
    transition-duration: .01ms !important;
  }
}
```
