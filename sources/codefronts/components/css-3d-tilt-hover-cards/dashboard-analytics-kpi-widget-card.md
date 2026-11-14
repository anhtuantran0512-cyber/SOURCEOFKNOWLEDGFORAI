---
source: "codefronts"
url: "https://codefronts.com/components/css-3d-tilt-hover-cards/dashboard-analytics-kpi-widget-card/"
title: "Dashboard Analytics KPI Widget Card"
section: "components"
category: "css-3d-tilt-hover-cards"
category_name: "CSS 3D Tilt Hover Cards"
description: "A FinTech KPI widget with enterprise-grade restraint: perspective(1600px) with tilt capped at ±4°, a drop-shadow that deepens as the card lifts 6px on hover,…"
has_js: "true"
---

Here's a working CSS 3D Tilt Hover Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dashboard Analytics KPI Widget Card
Source: https://codefronts.com/components/css-3d-tilt-hover-cards/dashboard-analytics-kpi-widget-card/

A FinTech KPI widget with enterprise-grade restraint: perspective(1600px) with tilt capped at ±4°, a drop-shadow that deepens as the card lifts 6px on hover, and a CSS-only sparkline of flex bars that stagger-grow when the tilt arms. Proof that 3D belongs in dashboards — at homeopathic doses.
## HTML
```html
<section class="thc-10" aria-label="Dashboard KPI widget tilt card demo">
  <article class="thc-10__card" tabindex="0" aria-label="Monthly recurring revenue: 84,200 dollars, up 12.4 percent">
    <div class="thc-10__head">
      <p class="thc-10__label">Monthly Recurring Revenue</p>
      <span class="thc-10__delta">&#9650; 12.4%</span>
    </div>
    <p class="thc-10__value">$84,200</p>
    <div class="thc-10__spark" aria-hidden="true">
      <i style="--v:32"></i><i style="--v:41"></i><i style="--v:38"></i><i style="--v:52"></i><i style="--v:47"></i><i style="--v:58"></i><i style="--v:54"></i><i style="--v:66"></i><i style="--v:61"></i><i style="--v:72"></i><i style="--v:69"></i><i style="--v:83"></i><i style="--v:92"></i>
    </div>
    <p class="thc-10__foot">vs. $74,900 last month</p>
  </article>
</section>
```
## CSS
```css
.thc-10,
.thc-10 *,
.thc-10 *::before,
.thc-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.thc-10 {
  --acc: oklch(0.7 0.15 150);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(180deg,oklch(0.975 0.005 250),oklch(0.94 0.01 250));
}

.thc-10 .thc-10__card {
  width: min(300px,100%);
  padding: 24px;
  border-radius: 18px;
  background: #fff;
  border: 1px solid oklch(0.9 0.008 250);
  transform: perspective(1600px) rotateX(var(--rx,0deg)) rotateY(var(--ry,0deg)) translateY(var(--lift,0px));
  transition: transform .5s cubic-bezier(.2,.9,.3,1.05),box-shadow .5s ease;
  box-shadow: 0 10px 24px -18px oklch(0.4 0.03 250 / .5);
  cursor: default;
}

.thc-10 .thc-10__card.is-live {
  --lift: -6px;
  transition: transform .09s linear,box-shadow .4s ease;
  box-shadow: 0 30px 50px -24px oklch(0.4 0.05 250 / .55);
}

.thc-10 .thc-10__card:focus-visible {
  outline: 3px solid var(--acc);
  outline-offset: 4px;
}

.thc-10 .thc-10__head {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 10px;
}

.thc-10 .thc-10__label {
  font-size: 12px;
  font-weight: 600;
  color: oklch(0.55 0.02 250);
}

.thc-10 .thc-10__delta {
  font-size: 11px;
  font-weight: 700;
  color: var(--acc);
  background: color-mix(in oklab,var(--acc) 14%,white);
  border-radius: 999px;
  padding: 5px 9px;
}

.thc-10 .thc-10__value {
  margin-top: 12px;
  font-size: 34px;
  font-weight: 800;
  letter-spacing: -.02em;
  color: oklch(0.22 0.02 250);
  font-variant-numeric: tabular-nums;
}

.thc-10 .thc-10__spark {
  display: flex;
  align-items: flex-end;
  gap: 4px;
  height: 52px;
  margin-top: 18px;
}

.thc-10 .thc-10__spark i {
  flex: 1;
  height: calc(var(--v) * 1%);
  border-radius: 3px 3px 0 0;
  background: linear-gradient(180deg,var(--acc),color-mix(in oklab,var(--acc) 45%,white));
  transform-origin: bottom;
}

.thc-10 .thc-10__card.is-live .thc-10__spark i {
  animation: thc-10-grow .4s cubic-bezier(.2,.9,.3,1.1) backwards;
}

.thc-10 .thc-10__spark i:nth-child(2n) {
  animation-delay: .05s;
}

.thc-10 .thc-10__spark i:nth-child(3n) {
  animation-delay: .1s;
}

.thc-10 .thc-10__spark i:nth-child(5n) {
  animation-delay: .15s;
}

@keyframes thc-10-grow {
  from {
    transform: scaleY(.55);
  }
}

.thc-10 .thc-10__foot {
  margin-top: 14px;
  font-size: 11.5px;
  color: oklch(0.6 0.015 250);
}

@media (prefers-reduced-motion: reduce) {
  .thc-10 .thc-10__card {
    transition: none;
  }

  .thc-10 .thc-10__card.is-live .thc-10__spark i {
    animation: none;
  }
}
```

## JavaScript
```js
(() => {
  const card = document.querySelector('.thc-10 .thc-10__card');
  if (!card) return;
  if (!matchMedia('(hover:hover) and (pointer:fine)').matches) return;
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const MAX = 4; // enterprise dose: elevation, not rotation
  card.addEventListener('pointermove', (e) => {
    const r = card.getBoundingClientRect();
    const px = (e.clientX - r.left) / r.width, py = (e.clientY - r.top) / r.height;
    card.style.setProperty('--rx', ((0.5 - py) * MAX).toFixed(2) + 'deg');
    card.style.setProperty('--ry', ((px - 0.5) * MAX).toFixed(2) + 'deg');
    card.classList.add('is-live'); // adds the -6px lift + deep shadow + bar re-grow
  });
  card.addEventListener('pointerleave', () => {
    card.classList.remove('is-live');
    card.style.setProperty('--rx', '0deg');
    card.style.setProperty('--ry', '0deg');
  });
})();
```
