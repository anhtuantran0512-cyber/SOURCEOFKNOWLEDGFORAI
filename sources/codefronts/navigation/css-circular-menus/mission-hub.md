---
source: "codefronts"
url: "https://codefronts.com/navigation/css-circular-menus/mission-hub/"
title: "Responsive Dashboard Radial Hub"
section: "navigation"
category: "css-circular-menus"
category_name: "CSS Circular Menus"
description: "A hub-and-spoke dashboard switcher: six module tiles orbit a live KPI core, connected by faint spokes, and the whole constellation scales fluidly because…"
has_js: "true"
---

Here's a working CSS Circular Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Responsive Dashboard Radial Hub
Source: https://codefronts.com/navigation/css-circular-menus/mission-hub/

A hub-and-spoke dashboard switcher: six module tiles orbit a live KPI core, connected by faint spokes, and the whole constellation scales fluidly because every radius derives from one container-query unit. Click a module and the core morphs into that module's headline stat.
## HTML
```html
<section class="ccm-06" aria-label="Dashboard radial hub demo">
  <div class="ccm-06__stage">
    <fieldset class="ccm-06__hub" style="--n:6"><legend class="ccm-06__sr">Choose a dashboard module</legend>
      <div class="ccm-06__space">
        <span class="ccm-06__spoke" style="--i:0" aria-hidden="true"></span>
        <span class="ccm-06__spoke" style="--i:1" aria-hidden="true"></span>
        <span class="ccm-06__spoke" style="--i:2" aria-hidden="true"></span>
        <span class="ccm-06__spoke" style="--i:3" aria-hidden="true"></span>
        <span class="ccm-06__spoke" style="--i:4" aria-hidden="true"></span>
        <span class="ccm-06__spoke" style="--i:5" aria-hidden="true"></span>
        <div class="ccm-06__mod" style="--i:0"><input type="radio" name="ccm06" id="ccm06-a" data-stat="$84.2k" data-delta="+12.4% this month" value="Revenue" checked><label for="ccm06-a"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 19L9 13l4 4 7-8M4 5v14h16"/></svg>Revenue</label></div>
        <div class="ccm-06__mod" style="--i:1"><input type="radio" name="ccm06" id="ccm06-b" data-stat="12,408" data-delta="+318 new this week" value="Users"><label for="ccm06-b"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="9" cy="8" r="3.5"/><path d="M3 20c0-3.5 2.7-5.5 6-5.5s6 2 6 5.5M16 4.6a3.5 3.5 0 0 1 0 6.8M17.5 14.7c2.1.7 3.5 2.4 3.5 5.3"/></svg>Users</label></div>
        <div class="ccm-06__mod" style="--i:2"><input type="radio" name="ccm06" id="ccm06-c" data-stat="98.2%" data-delta="uptime, 30 days" value="Systems"><label for="ccm06-c"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="4" y="4" width="16" height="7" rx="2"/><rect x="4" y="13" width="16" height="7" rx="2"/><path d="M8 7.5h.01M8 16.5h.01"/></svg>Systems</label></div>
        <div class="ccm-06__mod" style="--i:3"><input type="radio" name="ccm06" id="ccm06-d" data-stat="1,294" data-delta="orders in queue" value="Orders"><label for="ccm06-d"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 7l8-4 8 4v10l-8 4-8-4zM4 7l8 4m0 0l8-4m-8 4v10"/></svg>Orders</label></div>
        <div class="ccm-06__mod" style="--i:4"><input type="radio" name="ccm06" id="ccm06-e" data-stat="4.8★" data-delta="avg. review score" value="Reviews"><label for="ccm06-e"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3.5l2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 16.9l-5.2 2.7 1-5.8L3.5 9.7l5.9-.9z"/></svg>Reviews</label></div>
        <div class="ccm-06__mod" style="--i:5"><input type="radio" name="ccm06" id="ccm06-f" data-stat="37" data-delta="open tickets" value="Support"><label for="ccm06-f"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="3.5"/><path d="M5.7 5.7l3.8 3.8M14.5 14.5l3.8 3.8M18.3 5.7l-3.8 3.8M9.5 14.5l-3.8 3.8"/></svg>Support</label></div>
        <div class="ccm-06__core"><em class="ccm-06__corelabel">Revenue</em><strong class="ccm-06__stat">$84.2k</strong><span class="ccm-06__delta">+12.4% this month</span></div>
      </div>
    </fieldset>
  </div>
</section>
```
## CSS
```css
.ccm-06,
.ccm-06 *,
.ccm-06 *::before,
.ccm-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccm-06 {
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(180deg,oklch(0.24 0.03 230),oklch(0.18 0.025 245));
  --brand: oklch(0.72 0.15 195);
  --ink: oklch(0.92 0.01 210);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.ccm-06__stage {
  width: 100%;
  height: 100vh;
  display: grid;
  place-items: center;
  border-radius: 20px;
  background: linear-gradient(180deg,oklch(0.24 0.03 230),oklch(0.18 0.025 245));
  overflow: hidden;
}

.ccm-06__hub {
  border: none;
  width: min(460px,92%);
  container-type: inline-size;
}

.ccm-06__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  clip-path: inset(50%);
  overflow: hidden;
  white-space: nowrap;
}

.ccm-06__space {
  position: relative;
  height: 100cqi;
  max-height: 460px;
  display: grid;
  place-items: center;
  --r: 34cqi;
}

.ccm-06__spoke {
  position: absolute;
  left: 50%;
  top: 50%;
  width: var(--r);
  height: 1px;
  background: linear-gradient(90deg,oklch(0.7 0.1 200 / .0) 20%,oklch(0.7 0.1 200 / .35));
  --a: calc((360deg / var(--n)) * var(--i) - 90deg);
  rotate: var(--a);
  transform-origin: left center;
}

.ccm-06__mod {
  position: absolute;
  left: 50%;
  top: 50%;
  --a: calc((360deg / var(--n)) * var(--i) - 90deg);
  translate: calc(cos(var(--a)) * var(--r) - 50%) calc(sin(var(--a)) * var(--r) - 50%);
}

.ccm-06__mod input {
  position: absolute;
  width: 1px;
  height: 1px;
  clip-path: inset(50%);
  overflow: hidden;
}

.ccm-06__mod label {
  display: grid;
  justify-items: center;
  gap: 6px;
  width: 19cqi;
  min-width: 74px;
  padding: 12px 6px 10px;
  border-radius: 16px;
  background: oklch(0.3 0.03 230 / .8);
  border: 1px solid oklch(0.6 0.06 210 / .3);
  backdrop-filter: blur(4px);
  font-size: clamp(10px,2.6cqi,12.5px);
  font-weight: 600;
  cursor: pointer;
  transition: background .25s,border-color .25s,translate .25s;
}

.ccm-06__mod label:hover {
  translate: 0 -3px;
  background: oklch(0.34 0.04 225 / .9);
}

.ccm-06__mod :checked + label {
  background: linear-gradient(160deg,color-mix(in oklab,var(--brand) 30%,oklch(0.3 0.03 230)),oklch(0.3 0.03 230));
  border-color: var(--brand);
  box-shadow: 0 0 0 1px var(--brand),0 8px 24px -8px oklch(0.72 0.15 195 / .5);
}

.ccm-06__mod :focus-visible + label {
  outline: 3px solid var(--brand);
  outline-offset: 3px;
}

.ccm-06__mod svg {
  width: clamp(16px,5cqi,22px);
  height: auto;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
  color: var(--brand);
}

.ccm-06__core {
  position: absolute;
  display: grid;
  justify-items: center;
  gap: 3px;
  width: 36cqi;
  height: 36cqi;
  max-width: 170px;
  max-height: 170px;
  border-radius: 50%;
  place-content: center;
  text-align: center;
  background: radial-gradient(circle at 35% 30%,oklch(0.32 0.04 220),oklch(0.22 0.03 240));
  border: 1px solid oklch(0.65 0.1 200 / .4);
  box-shadow: 0 0 60px -10px oklch(0.72 0.15 195 / .35),inset 0 1px 0 oklch(1 0 0 / .1);
}

.ccm-06__corelabel {
  font-style: normal;
  font-size: clamp(9px,2.4cqi,11px);
  letter-spacing: .16em;
  text-transform: uppercase;
  color: oklch(0.7 0.08 200);
}

.ccm-06__stat {
  font-size: clamp(20px,7cqi,34px);
  letter-spacing: -.02em;
}

.ccm-06__delta {
  font-size: clamp(9px,2.4cqi,11.5px);
  color: var(--brand);
}

@media (prefers-reduced-motion: reduce) {
  .ccm-06 * {
    transition-duration: .01s !important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.ccm-06');
  const core = root.querySelector('.ccm-06__core');
  const label = root.querySelector('.ccm-06__corelabel');
  const stat = root.querySelector('.ccm-06__stat');
  const delta = root.querySelector('.ccm-06__delta');
  root.addEventListener('change', (e) => {
    if (e.target.name !== 'ccm06') return;
    const swap = () => {
      label.textContent = e.target.value;
      stat.textContent = e.target.dataset.stat;
      delta.textContent = e.target.dataset.delta;
    };
    if (matchMedia('(prefers-reduced-motion: reduce)').matches) { swap(); return; }
    core.animate([{ opacity: 1 }, { opacity: 0.2 }], { duration: 120 }).finished.then(() => {
      swap();
      core.animate([{ opacity: 0.2, scale: '0.96' }, { opacity: 1, scale: '1' }], { duration: 220, easing: 'ease-out' });
    });
  });
})();
```
