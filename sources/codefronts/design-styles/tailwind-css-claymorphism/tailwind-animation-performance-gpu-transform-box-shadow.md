---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-claymorphism/tailwind-animation-performance-gpu-transform-box-shadow/"
title: "Tailwind Animation Performance: GPU Transform vs Box-Shadow (Live FPS Meter)"
section: "design-styles"
category: "tailwind-css-claymorphism"
category_name: "Tailwind CSS Claymorphism"
description: "Measure it, don't guess."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Animation Performance: GPU Transform vs Box-Shadow (Live FPS Meter)
Source: https://codefronts.com/design-styles/tailwind-css-claymorphism/tailwind-animation-performance-gpu-transform-box-shadow/

Measure it, don't guess. Clay tiles animate under a live FPS meter in two modes: the naive one animates box-shadow directly; the optimized one pre-renders the lifted shadow on an after: layer and cross-fades its opacity while translate/scale do the motion. Mode is a data-mode attribute read by group-data-[mode=fast]/panel:. New: a 24 / 96 tile stress switch and a running average, so the gap shows on fast machines too.
## HTML
```html
<section class="tcl-20 w-full min-h-svh grid place-items-center bg-tcl20-bg px-4 py-12 font-tcl20-sans text-tcl20-ink" aria-label="Clay animation performance and transform optimization demo">
  <div class="grid w-full justify-items-center gap-4.5">
    <div data-tcl20-panel data-mode="fast" class="group/panel grid w-full max-w-[920px] gap-[clamp(16px,2.6vw,24px)] rounded-[44px] bg-tcl20-panel p-[clamp(20px,3.2vw,36px)] shadow-tcl20-panel">
      <header class="flex flex-wrap items-center justify-between gap-4.5">
        <div>
          <h2 class="font-tcl20-display text-[clamp(24px,3.4vw,32px)] font-extrabold tracking-[-0.03em]">Measure the shadow tax</h2>
          <p class="mt-1.5 max-w-[46ch] text-sm leading-normal text-tcl20-mut text-pretty">One continuous animation. Switch modes and watch the meter — same visual result, very different cost.</p>
        </div>
        <div role="status" aria-live="off" class="grid min-w-[170px] gap-1 rounded-[26px] bg-tcl20-well px-4.5 py-3.5 shadow-tcl20-well">
          <p class="text-[13px] text-tcl20-mut tabular-nums"><b data-fps class="font-tcl20-display text-[32px] font-extrabold tracking-[-0.03em] text-tcl20-ink">60</b> fps</p>
          <p class="text-[11.5px] text-tcl20-mut tabular-nums">avg <b data-avg class="font-bold text-tcl20-ink">60</b> · long frames <b data-jank class="font-bold text-tcl20-bad">0</b></p>
          <span data-graph aria-hidden="true" class="mt-1 flex h-6.5 items-end gap-0.5"></span>
        </div>
      </header>
      <div class="flex flex-wrap gap-2.5" role="group" aria-label="Animation mode">
        <button type="button" data-set="fast" aria-pressed="true" class="min-h-13 min-w-[200px] flex-1 cursor-pointer rounded-3xl bg-tcl20-soft px-5 text-[13.5px] font-semibold text-tcl20-mut shadow-tcl20-btn transition-[color,background-color,translate,scale] duration-200 ease-[cubic-bezier(.2,.8,.3,1.4)] hover:-translate-y-0.75 hover:text-tcl20-ink active:translate-y-0.5 active:scale-y-94 focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-tcl20-ink aria-pressed:bg-tcl20-accent aria-pressed:font-bold aria-pressed:text-tcl20-accentink">Optimized · transform + opacity</button>
        <button type="button" data-set="slow" aria-pressed="false" class="min-h-13 min-w-[200px] flex-1 cursor-pointer rounded-3xl bg-tcl20-soft px-5 text-[13.5px] font-semibold text-tcl20-mut shadow-tcl20-btn transition-[color,background-color,translate,scale] duration-200 ease-[cubic-bezier(.2,.8,.3,1.4)] hover:-translate-y-0.75 hover:text-tcl20-ink active:translate-y-0.5 active:scale-y-94 focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-tcl20-ink aria-pressed:bg-tcl20-bad aria-pressed:font-bold aria-pressed:text-white">Naive · animating box-shadow</button>
        <button type="button" data-stress data-count="96" aria-pressed="false" class="min-h-13 cursor-pointer rounded-3xl bg-tcl20-soft px-5 font-tcl20-mono text-[12.5px] font-semibold text-tcl20-mut shadow-tcl20-btn transition-[color,background-color,translate] duration-200 hover:-translate-y-0.75 hover:text-tcl20-ink focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-tcl20-ink aria-pressed:bg-tcl20-ink aria-pressed:text-white"><span data-count-label>Stress: 24 tiles</span></button>
      </div>
      <div data-grid class="grid grid-cols-[repeat(auto-fit,minmax(56px,1fr))] gap-[clamp(8px,1.6vw,14px)] rounded-[34px] bg-tcl20-well p-[clamp(12px,2vw,18px)] shadow-tcl20-well"></div>
      <p class="text-center text-[12.5px] leading-normal text-tcl20-mut text-pretty">Optimized mode pre-renders both shadow states and cross-fades them; motion is <code class="font-tcl20-mono text-xs">translate</code> + <code class="font-tcl20-mono text-xs">scale</code> only.</p>
    </div>
    <p aria-hidden="true" class="rounded-full bg-white/60 px-4 py-2 text-center font-tcl20-mono text-[11.5px] text-tcl20-mut">shadow = paint · transform/opacity = composite · group-data-[mode=fast]/panel: · real rAF numbers</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcl20-bg: #e4efde;
  --color-tcl20-bg: oklch(0.94 0.026 135);
  --color-tcl20-panel: #edf5e9;
  --color-tcl20-panel: oklch(0.96 0.018 135);
  --color-tcl20-soft: #eaf3e6;
  --color-tcl20-soft: oklch(0.955 0.02 135);
  --color-tcl20-well: #dae8d5;
  --color-tcl20-well: oklch(0.915 0.03 138);
  --color-tcl20-clay: #c4e2b4;
  --color-tcl20-clay: oklch(0.88 0.07 135);
  --color-tcl20-accent: #8bd47b;
  --color-tcl20-accent: oklch(0.8 0.14 140);
  --color-tcl20-accentink: #092703;
  --color-tcl20-accentink: oklch(0.24 0.07 140);
  --color-tcl20-bad: #c53637;
  --color-tcl20-bad: oklch(0.55 0.18 25);
  --color-tcl20-shade: #51784480;
  --color-tcl20-shade: oklch(0.53 0.09 138 / 0.5);
  --color-tcl20-light: #fbfff8f2;
  --color-tcl20-light: oklch(1 0.015 135 / 0.95);
  --color-tcl20-ink: #172a11;
  --color-tcl20-ink: oklch(0.26 0.05 138);
  --color-tcl20-mut: #495b43;
  --color-tcl20-mut: oklch(0.45 0.045 138);
  --font-tcl20-display: 'Bricolage Grotesque', system-ui, sans-serif;
  --font-tcl20-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tcl20-mono: 'JetBrains Mono', ui-monospace, monospace;
  --shadow-tcl20-panel: 0 30px 58px -24px var(--color-tcl20-shade), inset 0 -16px 28px -16px var(--color-tcl20-shade), inset 0 18px 28px -12px var(--color-tcl20-light);
  --shadow-tcl20-well: inset 0 12px 22px -10px var(--color-tcl20-shade), inset 0 -9px 16px -12px var(--color-tcl20-light);
  --shadow-tcl20-btn: 0 12px 20px -14px var(--color-tcl20-shade), inset 0 -8px 14px -10px var(--color-tcl20-shade), inset 0 10px 14px -8px var(--color-tcl20-light);
  --shadow-tcl20-rest: 0 10px 18px -8px var(--color-tcl20-shade), inset 0 -8px 13px -8px var(--color-tcl20-shade), inset 0 10px 13px -6px var(--color-tcl20-light);
  --shadow-tcl20-lifted: 0 24px 34px -10px var(--color-tcl20-shade), inset 0 -10px 16px -8px var(--color-tcl20-shade), inset 0 14px 18px -6px var(--color-tcl20-light);
  --animate-tcl20-lift: tcl20-lift 1.6s ease-in-out infinite alternate;
  --animate-tcl20-fade: tcl20-fade 1.6s ease-in-out infinite alternate;
  --animate-tcl20-shadow: tcl20-shadow 1.6s ease-in-out infinite alternate;

  @keyframes tcl20-lift {
    from {
      translate: 0 0;
      scale: 1;
    }

    to {
      translate: 0 -9px;
      scale: 1.05;
    }
  }

  @keyframes tcl20-fade {
    from {
      opacity: 0;
    }

    to {
      opacity: 1;
    }
  }

  @keyframes tcl20-shadow {
    from {
      box-shadow: 0 10px 18px -8px var(--color-tcl20-shade), inset 0 -8px 13px -8px var(--color-tcl20-shade), inset 0 10px 13px -6px var(--color-tcl20-light);
    }

    to {
      box-shadow: 0 34px 56px -8px var(--color-tcl20-shade), inset 0 -18px 30px -8px var(--color-tcl20-shade), inset 0 24px 34px -6px var(--color-tcl20-light);
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcl-20 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const TILE = 'relative aspect-square rounded-[22px] bg-tcl20-clay shadow-tcl20-rest [contain:paint] [animation-delay:calc(var(--tcl20-i)*55ms)] after:absolute after:inset-0 after:rounded-[inherit] after:opacity-0 after:shadow-tcl20-lifted after:[animation-delay:calc(var(--tcl20-i)*55ms)] group-data-[mode=fast]/panel:animate-tcl20-lift group-data-[mode=fast]/panel:will-change-transform group-data-[mode=fast]/panel:after:animate-tcl20-fade group-data-[mode=slow]/panel:animate-tcl20-shadow motion-reduce:animate-none! motion-reduce:after:animate-none!';
  const BAR = 'h-full min-w-0.5 flex-1 origin-bottom rounded-sm bg-tcl20-accent [scale:1_var(--tcl20-s,.1)]';
  document.querySelectorAll('[data-tcl20-panel]').forEach((panel) => {
    if (panel.dataset.wired) return;
    panel.dataset.wired = '1';
    const grid = panel.querySelector('[data-grid]');
    const graph = panel.querySelector('[data-graph]');
    const fpsEl = panel.querySelector('[data-fps]');
    const avgEl = panel.querySelector('[data-avg]');
    const jankEl = panel.querySelector('[data-jank]');
    const stress = panel.querySelector('[data-stress]');
    const BARS = 28;
    let jank = 0, samples = [];
    const build = (n) => {
      grid.replaceChildren();
      for (let i = 0; i < n; i++) {
        const t = document.createElement('div');
        t.className = TILE;
        t.style.setProperty('--tcl20-i', String(i % 24));
        grid.appendChild(t);
      }
    };
    const reset = () => { jank = 0; samples = []; jankEl.textContent = '0'; };
    build(24);
    const bars = [];
    for (let i = 0; i < BARS; i++) {
      const b = document.createElement('i');
      b.className = BAR;
      graph.appendChild(b);
      bars.push(b);
    }
    panel.querySelectorAll('[data-set]').forEach((btn) => {
      btn.addEventListener('click', () => {
        panel.dataset.mode = btn.dataset.set;
        panel.querySelectorAll('[data-set]').forEach((b) => b.setAttribute('aria-pressed', String(b === btn)));
        reset();
      });
    });
    stress.addEventListener('click', () => {
      const on = stress.getAttribute('aria-pressed') !== 'true';
      stress.setAttribute('aria-pressed', String(on));
      stress.querySelector('[data-count-label]').textContent = 'Stress: ' + (on ? stress.dataset.count : 24) + ' tiles';
      build(on ? Number(stress.dataset.count) : 24);
      reset();
    });
    let frames = 0, last = performance.now(), mark = last, cursor = 0;
    const tick = (now) => {
      const dt = now - last;
      last = now;
      frames++;
      if (dt > 24) { jank++; jankEl.textContent = String(jank); }
      if (now - mark >= 500) {
        const fps = Math.round((frames * 1000) / (now - mark));
        samples.push(fps);
        if (samples.length > 20) samples.shift();
        fpsEl.textContent = String(fps);
        avgEl.textContent = String(Math.round(samples.reduce((a, b) => a + b, 0) / samples.length));
        bars[cursor % BARS].style.setProperty('--tcl20-s', String(Math.max(0.06, Math.min(1, fps / 60))));
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
