---
source: "codefronts"
url: "https://codefronts.com/navigation/css-circular-menus/pie-slice-selector/"
title: "Pie Chart Navigation Menu"
section: "navigation"
category: "css-circular-menus"
category_name: "CSS Circular Menus"
description: "A pie chart that is the menu: four budget categories drawn as proportional slices with a single conic-gradient, plus an invisible hit layer of real buttons…"
has_js: "true"
---

Here's a working CSS Circular Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pie Chart Navigation Menu
Source: https://codefronts.com/navigation/css-circular-menus/pie-slice-selector/

A pie chart that is the menu: four budget categories drawn as proportional slices with a single conic-gradient, plus an invisible hit layer of real buttons over each slice. Click a slice and it 'lifts' toward you while the detail panel updates. Data visualization and navigation in one element — a genuinely different take on the category picker.
## HTML
```html
<section class="ccm-12" aria-label="Pie chart navigation demo">
  <div class="ccm-12__stage">
    <div class="ccm-12__duo">
      <div class="ccm-12__pie" role="group" aria-label="Budget categories">
        <div class="ccm-12__disc" aria-hidden="true"></div>
        <div class="ccm-12__hits"></div>
      </div>
      <aside class="ccm-12__panel" aria-live="polite">
        <em class="ccm-12__cat">Housing</em>
        <strong class="ccm-12__amt">$1,824<span>/mo</span></strong>
        <p class="ccm-12__share">38% of monthly budget</p>
        <div class="ccm-12__bar"><i style="scale:0.38 1"></i></div>
      </aside>
    </div>
  </div>
</section>
```
## CSS
```css
.ccm-12,
.ccm-12 *,
.ccm-12 *::before,
.ccm-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccm-12 {
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: oklch(0.97 0.006 265);
  --c1: oklch(0.62 0.17 265);
  --c2: oklch(0.72 0.15 195);
  --c3: oklch(0.78 0.14 85);
  --c4: oklch(0.68 0.17 350);
  --lift: 10px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: oklch(0.25 0.02 265);
}

.ccm-12__stage {
  width: 100%;
  height: 100vh;
  display: grid;
  place-items: center;
  border-radius: 20px;
  background: oklch(0.97 0.006 265);
  border: 1px solid oklch(0.9 0.01 265);
}

.ccm-12__duo {
  display: flex;
  align-items: center;
  gap: 44px;
  flex-wrap: wrap;
  justify-content: center;
  padding: 30px;
}

.ccm-12__pie {
  position: relative;
  width: 270px;
  height: 270px;
}

.ccm-12__disc {
  position: absolute;
  inset: 0;
  border-radius: 50%;
  box-shadow: 0 24px 50px -24px oklch(0.4 0.08 265 / .5);
}

.ccm-12__hits {
  position: absolute;
  inset: 0;
}

.ccm-12__hits button {
  position: absolute;
  inset: 0;
  border: none;
  border-radius: 50%;
  background: transparent;
  cursor: pointer;
  transition: translate .3s cubic-bezier(.34,1.3,.4,1),filter .3s;
}

.ccm-12__hits button:focus-visible {
  outline: 3px solid oklch(0.5 0.1 265);
  outline-offset: 4px;
}

.ccm-12__hits button.is-active {
  filter: drop-shadow(0 8px 16px oklch(0.4 0.08 265 / .45));
}

.ccm-12__panel {
  display: grid;
  gap: 6px;
  min-width: 220px;
  padding: 24px 26px;
  border-radius: 18px;
  background: #fff;
  border: 1px solid oklch(0.9 0.01 265);
  box-shadow: 0 18px 44px -26px oklch(0.4 0.08 265 / .5);
}

.ccm-12__cat {
  font-style: normal;
  font-size: 12px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: oklch(0.55 0.04 265);
}

.ccm-12__amt {
  font-size: 34px;
  letter-spacing: -.02em;
}

.ccm-12__amt span {
  font-size: 15px;
  font-weight: 500;
  color: oklch(0.55 0.04 265);
}

.ccm-12__share {
  font-size: 13.5px;
  color: oklch(0.45 0.03 265);
}

.ccm-12__bar {
  height: 8px;
  border-radius: 4px;
  background: oklch(0.93 0.01 265);
  overflow: hidden;
  margin-top: 6px;
}

.ccm-12__bar i {
  display: block;
  height: 100%;
  border-radius: 4px;
  background: var(--seg,var(--c1));
  transform-origin: left;
  transition: scale .5s cubic-bezier(.3,1,.35,1),background .3s;
}

@media (prefers-reduced-motion: reduce) {
  .ccm-12 * {
    transition-duration: .01s !important;
  }
}
```

## JavaScript
```js
(() => {
  const data = [
    { label: 'Housing', amt: '$1,824', pct: 38, color: 'var(--c1)' },
    { label: 'Food & dining', amt: '$1,296', pct: 27, color: 'var(--c2)' },
    { label: 'Transport', amt: '$1,056', pct: 22, color: 'var(--c3)' },
    { label: 'Savings', amt: '$624', pct: 13, color: 'var(--c4)' },
  ];
  const root = document.querySelector('.ccm-12');
  const disc = root.querySelector('.ccm-12__disc');
  const hits = root.querySelector('.ccm-12__hits');
  const panel = {
    cat: root.querySelector('.ccm-12__cat'), amt: root.querySelector('.ccm-12__amt'),
    share: root.querySelector('.ccm-12__share'), bar: root.querySelector('.ccm-12__bar i'),
  };
  // 1) paint the pie from the data
  let acc = 0;
  const stops = data.map((d) => {
    const s = d.color + ' ' + acc + '% ' + (acc + d.pct) + '%'; acc += d.pct; return s;
  });
  disc.style.background = 'conic-gradient(' + stops.join(',') + ')';
  // 2) build one clipped hit button per slice from the same numbers
  const P = 40; // polygon resolution per slice
  acc = 0;
  data.forEach((d, idx) => {
    const a0 = acc / 100 * 360 - 90, a1 = (acc + d.pct) / 100 * 360 - 90; acc += d.pct;
    const pts = ['50% 50%'];
    for (let k = 0; k <= P; k++) {
      const a = (a0 + (a1 - a0) * k / P) * Math.PI / 180;
      pts.push((50 + 50 * Math.cos(a)).toFixed(2) + '% ' + (50 + 50 * Math.sin(a)).toFixed(2) + '%');
    }
    const b = document.createElement('button');
    b.type = 'button';
    b.setAttribute('aria-label', d.label + ', ' + d.pct + ' percent of budget');
    b.style.clipPath = 'polygon(' + pts.join(',') + ')';
    const mid = ((a0 + a1) / 2) * Math.PI / 180;
    b.addEventListener('click', () => {
      hits.querySelectorAll('button').forEach((x) => { x.classList.remove('is-active'); x.style.translate = '0 0'; });
      b.classList.add('is-active');
      b.style.translate = (Math.cos(mid) * 10) + 'px ' + (Math.sin(mid) * 10) + 'px';
      panel.cat.textContent = d.label;
      panel.amt.innerHTML = d.amt + '<span>/mo</span>';
      panel.share.textContent = d.pct + '% of monthly budget';
      panel.bar.style.scale = (d.pct / 100) + ' 1';
      panel.bar.style.background = d.color;
    });
    hits.append(b);
  });
})();
```
