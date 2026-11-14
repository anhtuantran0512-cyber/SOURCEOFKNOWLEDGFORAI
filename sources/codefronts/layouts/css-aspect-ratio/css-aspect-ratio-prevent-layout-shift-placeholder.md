---
source: "codefronts"
url: "https://codefronts.com/layouts/css-aspect-ratio/css-aspect-ratio-prevent-layout-shift-placeholder/"
title: "CSS Aspect Ratio Prevent Layout Shift Placeholder"
section: "layouts"
category: "css-aspect-ratio"
category_name: "CSS Aspect Ratio Demos"
description: "A split-screen lab that makes Cumulative Layout Shift visible: the same article twice, images arriving on a simulated slow connection."
has_js: "true"
---

Here's a working CSS Aspect Ratio Demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Aspect Ratio Prevent Layout Shift Placeholder
Source: https://codefronts.com/layouts/css-aspect-ratio/css-aspect-ratio-prevent-layout-shift-placeholder/

A split-screen lab that makes Cumulative Layout Shift visible: the same article twice, images arriving on a simulated slow connection. The left pane reserves nothing — headlines lurch as each photo lands. The right pane gives every image aspect-ratio: 3/2 plus a shimmer skeleton — pixels pour into pre-reserved boxes and the text never moves. A live CLS meter (PerformanceObserver) keeps score, and a replay button re-runs the network as many times as you need to believe it.
## HTML
```html
<section class="car-08" aria-label="Prevent layout shift placeholder demo">
  <div class="car-08__stage" id="car08-top">
    <header class="car-08__bar">
      <div>
        <h1>Layout-shift lab</h1>
        <p>Same article, same slow network. One pane reserves image space with <code>aspect-ratio</code>; one doesn't.</p>
      </div>
      <p class="car-08__cls" aria-live="polite">CLS recorded <b>0.0000</b><span>Chromium only</span></p>
      <button class="car-08__replay" type="button">↻ Replay slow network</button>
    </header>
    <div class="car-08__split">
      <article class="car-08__pane car-08__pane--raw" aria-label="Without reservation">
        <header class="car-08__panehead"><b class="car-08__dot car-08__dot--bad" aria-hidden="true"></b><h2>Unreserved</h2><span>img { height: auto } — nothing else</span></header>
        <div class="car-08__feed">
          <h3>Trail report: the long way around Sorapiss</h3>
          <p class="car-08__meta">Ren Ito · 11 min read</p>
          <img data-src="https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?q=80&w=1200&h=800&auto=format&fit=crop" width="1200" height="800" alt="Mountain ridge at dawn" class="car-08__img car-08__img--raw">
          <p>The photo above arrives late — and when it does, this paragraph gets shoved down by its full height. On a phone, that's the moment you tap the wrong link.</p>
          <img data-src="https://images.unsplash.com/photo-1501785888041-af3ef285b470?q=80&w=1200&h=800&auto=format&fit=crop" width="1200" height="800" alt="Lake at golden hour" class="car-08__img car-08__img--raw">
          <p class="car-08__marker">⬑ Watch this line jump on every replay.</p>
        </div>
      </article>
      <article class="car-08__pane car-08__pane--safe" aria-label="Reserved with aspect-ratio">
        <header class="car-08__panehead"><b class="car-08__dot car-08__dot--good" aria-hidden="true"></b><h2>Reserved</h2><span>img { aspect-ratio: 3/2 } + shimmer</span></header>
        <div class="car-08__feed">
          <h3>Trail report: the long way around Sorapiss</h3>
          <p class="car-08__meta">Ren Ito · 11 min read</p>
          <img data-src="https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?q=80&w=1200&h=800&auto=format&fit=crop" width="1200" height="800" alt="Mountain ridge at dawn" class="car-08__img car-08__img--safe">
          <p>The box above existed at its final size before a single byte of image arrived. Pixels pour in; geometry holds; this paragraph has never moved.</p>
          <img data-src="https://images.unsplash.com/photo-1501785888041-af3ef285b470?q=80&w=1200&h=800&auto=format&fit=crop" width="1200" height="800" alt="Lake at golden hour" class="car-08__img car-08__img--safe">
          <p class="car-08__marker">⬑ This line has been exactly here since first paint.</p>
        </div>
      </article>
    </div>
    <footer class="car-08__foot">CLS is a Core Web Vitals ranking signal; 0.1 is the whole-page budget and one unreserved hero can spend it. Reserve with <code>aspect-ratio</code> (design-imposed shape) or <code>width</code>/<code>height</code> attributes (per-asset shape). A demo from the CodeFronts aspect-ratio collection.</footer>
  </div>
</section>
```
## CSS
```css
.car-08,
.car-08 *,
.car-08 *::before,
.car-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.car-08 {
  --bg: oklch(0.15 0.012 260);
  --panel: oklch(0.2 0.015 260);
  --ink: oklch(0.95 0.006 250);
  --mut: oklch(0.66 0.015 255);
  --line: oklch(0.31 0.02 260);
  --good: oklch(0.75 0.17 150);
  --bad: oklch(0.66 0.21 25);
  --acc: oklch(0.78 0.13 220);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
  display: block;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: var(--bg);
}

.car-08__stage {
  width: 100%;
  container: car08/inline-size;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  background: var(--bg);
}

.car-08__bar {
  display: flex;
  align-items: center;
  gap: 18px;
  flex-wrap: wrap;
  padding: 20px clamp(16px,4cqi,40px);
  border-bottom: 1px solid var(--line);
  position: sticky;
  top: 0;
  z-index: 5;
  background: color-mix(in oklch,var(--bg) 88%,transparent);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
}

.car-08__bar h1 {
  font-size: clamp(17px,2.4cqi,22px);
  letter-spacing: -.02em;
  font-weight: 800;
}

.car-08__bar p {
  font-size: 12.5px;
  color: var(--mut);
  margin-top: 3px;
  max-width: 52ch;
}

.car-08__bar code,
.car-08__foot code,
.car-08__panehead span {
  font-family: ui-monospace,Menlo,Consolas,monospace;
}

.car-08__bar code,
.car-08__foot code {
  font-size: .92em;
  background: oklch(0.26 0.02 260);
  padding: 2px 6px;
  border-radius: 5px;
  color: var(--acc);
}

.car-08__cls {
  margin-left: auto;
  text-align: right;
  font-size: 11px;
  color: var(--mut);
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 2px;
}

.car-08__cls b {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 20px;
  color: var(--acc);
  font-weight: 700;
}

.car-08__replay {
  display: grid;
  place-items: center;
  min-height: 46px;
  padding: 0 18px;
  border-radius: 12px;
  border: 1.5px solid var(--acc);
  background: transparent;
  color: var(--acc);
  font: inherit;
  font-size: 13.5px;
  font-weight: 700;
  cursor: pointer;
  transition: background .2s,color .2s,translate .2s;
}

.car-08__replay:hover,
.car-08__replay:focus-visible {
  background: var(--acc);
  color: oklch(0.18 0.03 220);
  translate: 0 -1px;
}

.car-08__replay:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.car-08__split {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: clamp(14px,2.5cqi,24px);
  padding: clamp(16px,3cqi,28px) clamp(16px,4cqi,40px);
  align-items: start;
}

.car-08__pane {
  border: 1px solid var(--line);
  border-radius: 16px;
  background: var(--panel);
  overflow: hidden;
}

.car-08__pane--raw {
  border-color: color-mix(in oklch,var(--bad) 45%,var(--line));
}

.car-08__pane--safe {
  border-color: color-mix(in oklch,var(--good) 45%,var(--line));
}

.car-08__panehead {
  display: flex;
  align-items: baseline;
  gap: 9px;
  padding: 13px 16px;
  border-bottom: 1px solid var(--line);
}

.car-08__panehead h2 {
  font-size: 14px;
  font-weight: 800;
  letter-spacing: -.01em;
}

.car-08__panehead span {
  font-size: 10.5px;
  color: var(--mut);
  margin-left: auto;
  text-align: right;
}

.car-08__dot {
  width: 9px;
  height: 9px;
  border-radius: 50%;
  align-self: center;
}

.car-08__dot--bad {
  background: var(--bad);
  box-shadow: 0 0 10px var(--bad);
}

.car-08__dot--good {
  background: var(--good);
  box-shadow: 0 0 10px var(--good);
}

.car-08__feed {
  padding: 16px 16px 20px;
}

.car-08__feed h3 {
  font-size: 16.5px;
  letter-spacing: -.015em;
  line-height: 1.25;
}

.car-08__meta {
  font-size: 11.5px;
  color: var(--mut);
  margin: 5px 0 12px;
}

.car-08__feed p {
  font-size: 13px;
  line-height: 1.6;
  color: var(--mut);
  margin: 12px 0;
}

.car-08__img {
  display: block;
  width: 100%;
  border-radius: 10px;
  object-fit: cover;
  background: oklch(0.26 0.015 260);
}

.car-08__img--raw {
  height: auto;
}

.car-08__img--safe {
  aspect-ratio: 3/2;
  background: linear-gradient(110deg,oklch(0.26 0.015 260) 30%,oklch(0.33 0.02 260) 45%,oklch(0.26 0.015 260) 60%) 0 0/200% 100%;
  animation: car08-shimmer 1.3s linear infinite;
}

@keyframes car08-shimmer {
  to {
    background-position: -200% 0;
  }
}

.car-08__marker {
  font-weight: 700;
  color: var(--ink) !important;
  border-left: 3px solid var(--acc);
  padding-left: 10px;
}

.car-08__foot {
  padding: 16px clamp(16px,4cqi,40px) 30px;
  font-size: 12.5px;
  line-height: 1.7;
  color: var(--mut);
  border-top: 1px solid var(--line);
}

@container car08 (width < 700px) {
  .car-08__split {
    grid-template-columns: 1fr;
  }

  .car-08__cls {
    margin-left: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .car-08__img--safe {
    animation: none;
  }

  .car-08 * {
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.car-08');
  if (!root || root.dataset.init) return;
  root.dataset.init = '1';
  const imgs = [...root.querySelectorAll('img[data-src]')];
  const meter = root.querySelector('.car-08__cls b');
  let cls = 0;
  try {
    new PerformanceObserver((list) => {
      list.getEntries().forEach((e) => { if (!e.hadRecentInput) cls += e.value; });
      meter.textContent = cls.toFixed(4);
    }).observe({ type: 'layout-shift', buffered: true });
  } catch (err) { meter.textContent = 'n/a'; }
  const run = () => imgs.forEach((im, i) => {
    im.removeAttribute('src');
    setTimeout(() => { im.src = im.dataset.src; }, 900 + (i % 2) * 500 + Math.floor(i / 2) * 150);
  });
  root.querySelector('.car-08__replay').addEventListener('click', run);
  run();
})();
```
