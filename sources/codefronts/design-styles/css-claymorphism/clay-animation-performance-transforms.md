---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-claymorphism/clay-animation-performance-transforms/"
title: "Clay Animation Performance & Transform Optimization"
section: "design-styles"
category: "css-claymorphism"
category_name: "CSS Claymorphism"
description: "Measure it, do not guess."
has_js: "true"
---

Here's a working CSS Claymorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Clay Animation Performance & Transform Optimization
Source: https://codefronts.com/design-styles/css-claymorphism/clay-animation-performance-transforms/

Measure it, do not guess. Twenty-four clay tiles animate under a live FPS meter in two modes: the naive one animates box-shadow blur directly, the optimized one pre-renders both shadow states and cross-fades a pseudo-element while transform does the motion. The frame counter and long-frame tally are real, and the gap is visible on screen.
## HTML
```html
<section class="cl-20" aria-label="Clay animation performance and transform optimization demo">
  <div class="cl-20__stage">
    <div class="cl-20__panel" data-mode="fast">
      <header class="cl-20__head">
        <div>
          <h2 class="cl-20__h">Measure the shadow tax</h2>
          <p class="cl-20__lede">24 tiles, one continuous animation. Switch modes and watch the meter — same visual result, very different cost.</p>
        </div>
        <div class="cl-20__meter" role="status" aria-live="off">
          <p class="cl-20__fps"><b class="cl-20__fpsVal">60</b> fps</p>
          <p class="cl-20__jank">long frames: <b class="cl-20__jankVal">0</b></p>
          <span class="cl-20__graph" aria-hidden="true"></span>
        </div>
      </header>
      <div class="cl-20__modes" role="group" aria-label="Animation mode">
        <button class="cl-20__mode is-on" type="button" data-set="fast" aria-pressed="true">Optimized · transform + opacity</button>
        <button class="cl-20__mode" type="button" data-set="slow" aria-pressed="false">Naive · animating box-shadow</button>
      </div>
      <div class="cl-20__grid"></div>
      <p class="cl-20__hint">Optimized mode pre-renders both shadow states and cross-fades them; motion is <code>translate</code> + <code>scale</code> only.</p>
    </div>
    <p class="cl-20__chip" aria-hidden="true">shadow = paint · transform/opacity = composite · rAF meter, real numbers</p>
  </div>
</section>
```
## CSS
```css
.cl-20,
.cl-20 *,
.cl-20 *::before,
.cl-20 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cl-20 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--cl-20-bg);
  --cl-20-bg: oklch(0.94 0.026 135);
  --cl-20-clay: oklch(0.88 0.07 135);
  --cl-20-accent: oklch(0.8 0.14 140);
  --cl-20-shade: oklch(0.53 0.09 138/.5);
  --cl-20-light: oklch(1 0.015 135/.95);
  --cl-20-ink: oklch(0.27 0.05 138);
  --cl-20-mut: oklch(0.5 0.04 138);
  font-family: system-ui,-apple-system,'Segoe UI',sans-serif;
  color: var(--cl-20-ink);
}

.cl-20__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 18px;
  padding: clamp(18px,4vw,52px);
}

.cl-20__panel {
  width: min(100%,900px);
  display: grid;
  gap: clamp(16px,2.6vw,24px);
  padding: clamp(20px,3.2vw,34px);
  border-radius: 44px;
  background: color-mix(in oklch,var(--cl-20-bg) 93%,white);
  box-shadow: 0 30px 58px -24px var(--cl-20-shade),inset 0 -16px 28px -16px var(--cl-20-shade),inset 0 18px 28px -12px var(--cl-20-light);
}

.cl-20__head {
  display: flex;
  flex-wrap: wrap;
  gap: 18px;
  align-items: center;
  justify-content: space-between;
}

.cl-20__h {
  font-size: clamp(21px,3.2vw,30px);
  font-weight: 780;
  letter-spacing: -.022em;
}

.cl-20__lede {
  margin-top: 6px;
  max-width: 46ch;
  font-size: 14px;
  line-height: 1.55;
  color: var(--cl-20-mut);
  text-wrap: pretty;
}

.cl-20__meter {
  display: grid;
  gap: 4px;
  min-width: 150px;
  padding: 14px 18px;
  border-radius: 26px;
  background: color-mix(in oklch,var(--cl-20-bg) 96%,oklch(0.66 0.06 138));
  box-shadow: inset 0 10px 18px -8px var(--cl-20-shade),inset 0 -7px 13px -10px var(--cl-20-light);
}

.cl-20__fps {
  font-size: 13px;
  color: var(--cl-20-mut);
  font-variant-numeric: tabular-nums;
}

.cl-20__fps b {
  font-size: 30px;
  font-weight: 790;
  letter-spacing: -.03em;
  color: var(--cl-20-ink);
}

.cl-20__jank {
  font-size: 11.5px;
  color: var(--cl-20-mut);
  font-variant-numeric: tabular-nums;
}

.cl-20__jank b {
  color: oklch(0.55 0.17 25);
  font-weight: 740;
}

.cl-20__graph {
  display: flex;
  align-items: flex-end;
  gap: 2px;
  height: 26px;
  margin-top: 4px;
}

.cl-20__graph i {
  flex: 1;
  min-width: 2px;
  border-radius: 2px;
  background: var(--cl-20-accent);
  height: 100%;
  transform-origin: bottom;
  scale: 1 var(--cl-20-s,.1);
}

.cl-20__modes {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.cl-20__mode {
  flex: 1;
  min-width: 200px;
  min-height: 52px;
  padding: 0 20px;
  border: 0;
  border-radius: 24px;
  font: inherit;
  font-size: 13.5px;
  font-weight: 660;
  color: var(--cl-20-mut);
  cursor: pointer;
  background: color-mix(in oklch,var(--cl-20-bg) 92%,white);
  box-shadow: 0 12px 20px -14px var(--cl-20-shade),inset 0 -8px 14px -10px var(--cl-20-shade),inset 0 10px 14px -8px var(--cl-20-light);
  transition: color .25s,background .25s,translate .18s,scale .18s cubic-bezier(.2,.8,.3,1.4);
}

.cl-20__mode:hover {
  translate: 0 -3px;
  color: var(--cl-20-ink);
}

.cl-20__mode:active {
  scale: 1 .94;
  translate: 0 2px;
}

.cl-20__mode:focus-visible {
  outline: 3px solid var(--cl-20-ink);
  outline-offset: 3px;
}

.cl-20__mode.is-on {
  color: oklch(0.24 0.07 140);
  background: var(--cl-20-accent);
  box-shadow: 0 16px 26px -12px var(--cl-20-shade),inset 0 -10px 16px -9px var(--cl-20-shade),inset 0 12px 16px -7px var(--cl-20-light);
}

.cl-20__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(64px,1fr));
  gap: clamp(8px,1.6vw,14px);
  padding: clamp(12px,2vw,18px);
  border-radius: 34px;
  background: color-mix(in oklch,var(--cl-20-bg) 96%,oklch(0.7 0.05 138));
  box-shadow: inset 0 12px 22px -10px var(--cl-20-shade),inset 0 -9px 16px -12px var(--cl-20-light);
}

.cl-20__tile {
  position: relative;
  aspect-ratio: 1;
  border-radius: 22px;
  contain: paint;
  background: var(--cl-20-clay);
  box-shadow: 0 10px 18px -8px var(--cl-20-shade),inset 0 -8px 13px -8px var(--cl-20-shade),inset 0 10px 13px -6px var(--cl-20-light);
}

.cl-20__tile::after {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: inherit;
  opacity: 0;
  box-shadow: 0 24px 34px -10px var(--cl-20-shade),inset 0 -10px 16px -8px var(--cl-20-shade),inset 0 14px 18px -6px var(--cl-20-light);
}

.cl-20__panel[data-mode="fast"] .cl-20__tile {
  animation: cl-20-lift 1.6s ease-in-out infinite alternate;
  animation-delay: calc(var(--cl-20-i) * 55ms);
  will-change: transform;
}

.cl-20__panel[data-mode="fast"] .cl-20__tile::after {
  animation: cl-20-fade 1.6s ease-in-out infinite alternate;
  animation-delay: calc(var(--cl-20-i) * 55ms);
}

.cl-20__panel[data-mode="slow"] .cl-20__tile {
  animation: cl-20-shadow 1.6s ease-in-out infinite alternate;
  animation-delay: calc(var(--cl-20-i) * 55ms);
}

@keyframes cl-20-lift {
  from {
    translate: 0 0;
    scale: 1;
  }

  to {
    translate: 0 -9px;
    scale: 1.05;
  }
}

@keyframes cl-20-fade {
  from {
    opacity: 0;
  }

  to {
    opacity: 1;
  }
}

@keyframes cl-20-shadow {
  from {
    box-shadow: 0 10px 18px -8px var(--cl-20-shade),inset 0 -8px 13px -8px var(--cl-20-shade),inset 0 10px 13px -6px var(--cl-20-light);
  }

  to {
    box-shadow: 0 34px 56px -8px var(--cl-20-shade),inset 0 -18px 30px -8px var(--cl-20-shade),inset 0 24px 34px -6px var(--cl-20-light);
  }
}

.cl-20__hint {
  font-size: 12.5px;
  line-height: 1.55;
  color: var(--cl-20-mut);
  text-align: center;
  text-wrap: pretty;
}

.cl-20__hint code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
}

.cl-20__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--cl-20-mut);
  padding: 9px 16px;
  border-radius: 99px;
  text-align: center;
  background: oklch(1 0 0/.6);
  box-shadow: inset 0 -4px 10px -8px var(--cl-20-shade),inset 0 6px 10px -6px oklch(1 0 0);
}

@media (prefers-reduced-motion: reduce) {
  .cl-20__tile,
    .cl-20__tile::after {
    animation: none !important;
  }

  .cl-20 * {
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('.cl-20__panel').forEach((panel) => {
    if (panel.dataset.wired) return;
    panel.dataset.wired = '1';
    const grid = panel.querySelector('.cl-20__grid');
    const graph = panel.querySelector('.cl-20__graph');
    const fpsVal = panel.querySelector('.cl-20__fpsVal');
    const jankVal = panel.querySelector('.cl-20__jankVal');
    const TILES = 24, BARS = 28;

    for (let i = 0; i < TILES; i++) {
      const t = document.createElement('div');
      t.className = 'cl-20__tile';
      t.style.setProperty('--cl-20-i', String(i));
      grid.appendChild(t);
    }
    const bars = [];
    for (let i = 0; i < BARS; i++) {
      const b = document.createElement('i');
      graph.appendChild(b);
      bars.push(b);
    }

    panel.querySelectorAll('.cl-20__mode').forEach((btn) => {
      btn.addEventListener('click', () => {
        panel.dataset.mode = btn.dataset.set;
        jank = 0;
        jankVal.textContent = '0';
        panel.querySelectorAll('.cl-20__mode').forEach((b) => {
          const on = b === btn;
          b.classList.toggle('is-on', on);
          b.setAttribute('aria-pressed', String(on));
        });
      });
    });

    let frames = 0, jank = 0, last = performance.now(), mark = last, cursor = 0;
    const tick = (now) => {
      const dt = now - last;
      last = now;
      frames++;
      if (dt > 24) { jank++; jankVal.textContent = String(jank); }
      if (now - mark >= 500) {
        const fps = Math.round((frames * 1000) / (now - mark));
        fpsVal.textContent = String(fps);
        bars[cursor % BARS].style.setProperty('--cl-20-s', String(Math.max(0.06, Math.min(1, fps / 60))));
        cursor++;
        frames = 0;
        mark = now;
      }
      requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  });
})();
```
