---
source: "codefronts"
url: "https://codefronts.com/snippets/css-ribbons/clip-path-polygon-ribbon/"
title: "Clip-Path Polygon Ribbon"
section: "snippets"
category: "css-ribbons"
category_name: "CSS Ribbons"
description: "The finale and the reference implementation: three ribbon archetypes — banner, corner, bookmark — each drawn by a single element with a single clip-path, no…"
has_js: "true"
---

Here's a working CSS Ribbon from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Clip-Path Polygon Ribbon
Source: https://codefronts.com/snippets/css-ribbons/clip-path-polygon-ribbon/

The finale and the reference implementation: three ribbon archetypes — banner, corner, bookmark — each drawn by a single element with a single clip-path, no pseudo-elements, no wrappers, no overflow tricks. Every coordinate is a registered @property, so you can drag the sliders and watch the polygon interpolate live, then copy the exact CSS the playground produces.
## HTML
```html
<section class="rib-20" aria-label="Pure CSS clip-path polygon ribbon playground demo">
  <div class="rib-20__stage">
    <div class="rib-20__lab">
      <div class="rib-20__shapes">
        <div class="rib-20__slot">
          <span class="rib-20__ribbon rib-20__ribbon--banner">Swallowtail banner</span>
          <span class="rib-20__cap">banner</span>
        </div>
        <div class="rib-20__slot">
          <span class="rib-20__ribbon rib-20__ribbon--corner">Corner flag</span>
          <span class="rib-20__cap">corner</span>
        </div>
        <div class="rib-20__slot">
          <span class="rib-20__ribbon rib-20__ribbon--book">Bookmark</span>
          <span class="rib-20__cap">bookmark</span>
        </div>
      </div>
      <div class="rib-20__controls">
        <div class="rib-20__ctrl">
          <label class="rib-20__lbl" for="rib-20-notch">Notch depth <output class="rib-20__out" id="rib-20-notch-out">26px</output></label>
          <input class="rib-20__range" id="rib-20-notch" type="range" min="0" max="60" value="26" step="1" data-var="--rib-20-notch">
        </div>
        <div class="rib-20__ctrl">
          <label class="rib-20__lbl" for="rib-20-tail">Tail length <output class="rib-20__out" id="rib-20-tail-out">22px</output></label>
          <input class="rib-20__range" id="rib-20-tail" type="range" min="0" max="70" value="22" step="1" data-var="--rib-20-tail">
        </div>
        <div class="rib-20__ctrl">
          <label class="rib-20__lbl" for="rib-20-bevel">Bevel <output class="rib-20__out" id="rib-20-bevel-out">14px</output></label>
          <input class="rib-20__range" id="rib-20-bevel" type="range" min="0" max="48" value="14" step="1" data-var="--rib-20-bevel">
        </div>
        <div class="rib-20__presets" role="group" aria-label="Presets">
          <button class="rib-20__preset" type="button" data-preset="26,22,14">Default</button>
          <button class="rib-20__preset" type="button" data-preset="52,8,0">Deep V</button>
          <button class="rib-20__preset" type="button" data-preset="0,46,34">Arrow</button>
        </div>
      </div>
      <pre class="rib-20__readout" tabindex="0" aria-label="Generated CSS"><code id="rib-20-css"></code></pre>
    </div>
    <p class="rib-20__chip" aria-hidden="true">one element · one clip-path · registered &lt;length&gt; properties · zero pseudo-elements</p>
  </div>
</section>
```
## CSS
```css
@property --rib-20-notch {
  syntax: '<length>';
  inherits: true;
  initial-value: 26px;
}

@property --rib-20-tail {
  syntax: '<length>';
  inherits: true;
  initial-value: 22px;
}

@property --rib-20-bevel {
  syntax: '<length>';
  inherits: true;
  initial-value: 14px;
}

.rib-20,
.rib-20 *,
.rib-20 *::before,
.rib-20 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.rib-20 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --rib-20-bg: #0f1013;
  --rib-20-bg: oklch(0.19 0.004 265);
  --rib-20-panel: #181a1f;
  --rib-20-panel: oklch(0.24 0.006 265);
  --rib-20-ink: #eceef2;
  --rib-20-ink: oklch(0.95 0.004 265);
  --rib-20-mut: #888e9b;
  --rib-20-mut: oklch(0.64 0.012 265);
  --rib-20-a: #7c5cff;
  --rib-20-a: oklch(0.62 0.21 290);
  --rib-20-b: #25d0a8;
  --rib-20-b: oklch(0.78 0.15 168);
  --rib-20-c: #ffb020;
  --rib-20-c: oklch(0.8 0.16 72);
  background: var(--rib-20-bg);
  color: var(--rib-20-ink);
  font-family: system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.rib-20__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(14px,2.6vw,22px);
  padding: clamp(18px,4vw,52px);
}

.rib-20__lab {
  width: min(100%,840px);
  display: grid;
  gap: clamp(18px,3vw,26px);
  padding: clamp(20px,4vw,32px);
  border-radius: 24px;
  background: var(--rib-20-panel);
  border: 1px solid oklch(1 0 0/.08);
  box-shadow: 0 34px 74px -38px oklch(0 0 0/.9);
}

.rib-20__shapes {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(190px,1fr));
  gap: clamp(14px,2.4vw,20px);
  align-items: start;
}

.rib-20__slot {
  display: grid;
  justify-items: center;
  gap: 10px;
  padding: clamp(16px,3vw,24px) 10px;
  border-radius: 16px;
  background: oklch(1 0 0/.035);
  border: 1px solid oklch(1 0 0/.06);
}

.rib-20__ribbon {
  display: grid;
  place-items: center;
  text-align: center;
  font-size: 13px;
  font-weight: 750;
  letter-spacing: .05em;
  color: oklch(0.16 0.02 290);
  filter: drop-shadow(0 10px 16px oklch(0 0 0/.55));
  transition: --rib-20-notch .45s cubic-bezier(.16,1,.3,1),--rib-20-tail .45s cubic-bezier(.16,1,.3,1),--rib-20-bevel .45s cubic-bezier(.16,1,.3,1);
}

.rib-20__ribbon--banner {
  inline-size: 100%;
  min-block-size: 60px;
  padding: 14px calc(var(--rib-20-notch) + 14px);
  background: linear-gradient(100deg,color-mix(in oklch,var(--rib-20-a) 100%,white 18%),var(--rib-20-a));
  clip-path: polygon(0 0,100% 0,calc(100% - var(--rib-20-notch)) 50%,100% 100%,0 100%,var(--rib-20-notch) 50%);
}

.rib-20__ribbon--corner {
  inline-size: 100%;
  min-block-size: 78px;
  padding: 14px 16px;
  background: linear-gradient(140deg,color-mix(in oklch,var(--rib-20-b) 100%,white 16%),var(--rib-20-b));
  clip-path: polygon(0 0,100% 0,100% calc(100% - var(--rib-20-bevel)),calc(100% - var(--rib-20-bevel)) 100%,var(--rib-20-tail) 100%,0 calc(100% - var(--rib-20-tail)));
}

.rib-20__ribbon--book {
  inline-size: 86px;
  min-block-size: 110px;
  padding: 14px 8px calc(var(--rib-20-tail) + 12px);
  align-content: start;
  background: linear-gradient(180deg,color-mix(in oklch,var(--rib-20-c) 100%,white 18%),var(--rib-20-c));
  clip-path: polygon(0 0,100% 0,100% 100%,50% calc(100% - var(--rib-20-tail)),0 100%);
}

.rib-20__cap {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .1em;
  color: var(--rib-20-mut);
}

.rib-20__controls {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(190px,1fr));
  gap: 16px;
  align-items: end;
  padding-block-start: clamp(4px,1vw,8px);
  border-block-start: 1px solid oklch(1 0 0/.07);
}

.rib-20__ctrl {
  display: grid;
  gap: 9px;
}

.rib-20__lbl {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  font-size: 12.5px;
  font-weight: 620;
  color: var(--rib-20-mut);
}

.rib-20__out {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  padding: 3px 8px;
  border-radius: 6px;
  background: oklch(1 0 0/.08);
  color: var(--rib-20-ink);
  font-variant-numeric: tabular-nums;
}

.rib-20__range {
  -webkit-appearance: none;
  appearance: none;
  inline-size: 100%;
  block-size: 32px;
  background: transparent;
  cursor: pointer;
}

.rib-20__range::-webkit-slider-runnable-track {
  block-size: 6px;
  border-radius: 99px;
  background: oklch(1 0 0/.14);
}

.rib-20__range::-moz-range-track {
  block-size: 6px;
  border-radius: 99px;
  background: oklch(1 0 0/.14);
}

.rib-20__range::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  inline-size: 22px;
  block-size: 22px;
  margin-block-start: -8px;
  border-radius: 50%;
  background: var(--rib-20-ink);
  box-shadow: 0 2px 6px oklch(0 0 0/.6);
  border: 0;
}

.rib-20__range::-moz-range-thumb {
  inline-size: 22px;
  block-size: 22px;
  border-radius: 50%;
  background: var(--rib-20-ink);
  border: 0;
  box-shadow: 0 2px 6px oklch(0 0 0/.6);
}

.rib-20__range:focus-visible {
  outline: 3px solid var(--rib-20-a);
  outline-offset: 4px;
  border-radius: 8px;
}

.rib-20__presets {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.rib-20__preset {
  min-height: 44px;
  padding-inline: 15px;
  border: 1.5px solid oklch(1 0 0/.16);
  border-radius: 11px;
  background: transparent;
  color: var(--rib-20-ink);
  font: inherit;
  font-size: 13px;
  font-weight: 620;
  cursor: pointer;
  transition: background .2s,border-color .2s;
}

.rib-20__preset:hover {
  background: oklch(1 0 0/.08);
  border-color: var(--rib-20-a);
}

.rib-20__preset:focus-visible {
  outline: 3px solid var(--rib-20-a);
  outline-offset: 3px;
}

.rib-20__readout {
  padding: 16px;
  border-radius: 14px;
  background: oklch(0 0 0/.42);
  border: 1px solid oklch(1 0 0/.07);
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  line-height: 1.65;
  color: oklch(0.86 0.02 168);
  overflow-x: auto;
  white-space: pre;
}

.rib-20__readout:focus-visible {
  outline: 2px solid var(--rib-20-b);
  outline-offset: 2px;
}

.rib-20__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--rib-20-mut);
  padding: 8px 15px;
  border: 1px solid oklch(1 0 0/.14);
  border-radius: 99px;
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .rib-20 * {
    transition-duration: .01ms !important;
    animation: none !important;
  }
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('.rib-20__lab').forEach((lab) => {
    if (lab.dataset.wired) return;
    lab.dataset.wired = '1';
    const ranges = [...lab.querySelectorAll('.rib-20__range')];
    const out = lab.querySelector('#rib-20-css');

    const paint = () => {
      const v = {};
      ranges.forEach((r) => {
        // A registered <length> property will NOT accept a unitless number.
        lab.style.setProperty(r.dataset.var, r.value + 'px');
        lab.querySelector('#' + r.id + '-out').textContent = r.value + 'px';
        v[r.dataset.var] = r.value + 'px';
      });
      out.textContent =
        '.ribbon {\n' +
        '  --notch: ' + v['--rib-20-notch'] + ';\n' +
        '  --tail:  ' + v['--rib-20-tail'] + ';\n' +
        '  clip-path: polygon(\n' +
        '    0 0, 100% 0,\n' +
        '    calc(100% - var(--notch)) 50%,\n' +
        '    100% 100%, 0 100%,\n' +
        '    var(--notch) 50%);\n' +
        '}';
    };

    ranges.forEach((r) => r.addEventListener('input', paint));
    lab.querySelectorAll('.rib-20__preset').forEach((btn) => {
      btn.addEventListener('click', () => {
        const vals = btn.dataset.preset.split(',');
        ranges.forEach((r, i) => { r.value = vals[i]; });
        paint();
      });
    });
    paint();
  });
})();
```
