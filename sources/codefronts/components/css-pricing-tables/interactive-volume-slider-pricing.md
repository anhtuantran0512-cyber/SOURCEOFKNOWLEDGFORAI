---
source: "codefronts"
url: "https://codefronts.com/components/css-pricing-tables/interactive-volume-slider-pricing/"
title: "Interactive Volume Slider Pricing"
section: "components"
category: "css-pricing-tables"
category_name: "CSS Pricing Tables"
description: "The usage-based pricing calculator SaaS teams actually ship: drag a \"team size\" range slider and every tier's monthly total recalculates live, the per-seat…"
has_js: "true"
---

Here's a working CSS Pricing Table from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Interactive Volume Slider Pricing
Source: https://codefronts.com/components/css-pricing-tables/interactive-volume-slider-pricing/

The usage-based pricing calculator SaaS teams actually ship: drag a "team size" range slider and every tier's monthly total recalculates live, the per-seat maths updates, and the recommended plan badge jumps to whichever tier is now the best deal.
## HTML
```html
<section class="prc-11" aria-label="Usage-based pricing calculator">
  <header class="prc-11__head">
    <h2>How big is your team?</h2>
    <div class="prc-11__sliderrow">
      <label for="prc-11-range" class="prc-11__count"><output id="prc-11-out">10</output> seats</label>
      <input type="range" id="prc-11-range" min="1" max="100" step="1" value="10" aria-describedby="prc-11-out">
    </div>
  </header>
  <div class="prc-11__grid" id="prc-11-grid">
    <article class="prc-11__card" data-tier="0"><span class="prc-11__best-badge">Best value</span><h3>Starter</h3><p class="prc-11__total"><span class="prc-11__amount">$70</span><small>/mo</small></p><p class="prc-11__math"></p><ul><li>Core features</li><li>Standard support</li></ul><a href="#" class="prc-11__cta">Choose Starter</a></article>
    <article class="prc-11__card" data-tier="1"><span class="prc-11__best-badge">Best value</span><h3>Team</h3><p class="prc-11__total"><span class="prc-11__amount">$99</span><small>/mo</small></p><p class="prc-11__math"></p><ul><li>Everything in Starter</li><li>Roles &amp; permissions</li><li>Priority support</li></ul><a href="#" class="prc-11__cta">Choose Team</a></article>
    <article class="prc-11__card" data-tier="2"><span class="prc-11__best-badge">Best value</span><h3>Business</h3><p class="prc-11__total"><span class="prc-11__amount">$249</span><small>/mo</small></p><p class="prc-11__math"></p><ul><li>Everything in Team</li><li>SSO &amp; audit log</li><li>99.9% SLA</li></ul><a href="#" class="prc-11__cta">Choose Business</a></article>
  </div>
  <p class="prc-11__live" id="prc-11-live" aria-live="polite"></p>
</section>
```
## CSS
```css
.prc-11,
.prc-11 *,
.prc-11 *::before,
.prc-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.prc-11 {
  --accent: oklch(0.62 0.18 145);
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #101511;
  color: #e9efe9;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 56px 24px;
}

.prc-11__head {
  text-align: center;
  margin-bottom: 38px;
}

.prc-11__head h2 {
  font-size: clamp(24px,3.6vw,34px);
  font-weight: 800;
  letter-spacing: -.02em;
  margin-bottom: 22px;
}

.prc-11__sliderrow {
  display: flex;
  flex-direction: column;
  gap: 12px;
  align-items: center;
}

.prc-11__count {
  font-size: 14px;
  font-weight: 600;
  color: #9fb0a0;
}

.prc-11__count output {
  font-size: 20px;
  font-weight: 800;
  color: var(--accent);
  margin-right: 4px;
}

.prc-11 input[type=range] {
  --pct: 9%;
  width: min(420px,86vw);
  height: 6px;
  border-radius: 99px;
  appearance: none;
  -webkit-appearance: none;
  background: linear-gradient(to right,var(--accent) var(--pct),#28322a var(--pct));
  cursor: pointer;
}

.prc-11 input[type=range]::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: #fff;
  border: 5px solid var(--accent);
  box-shadow: 0 4px 12px rgba(0,0,0,.4);
  transition: transform .15s;
}

.prc-11 input[type=range]::-webkit-slider-thumb:hover {
  transform: scale(1.15);
}

.prc-11 input[type=range]::-moz-range-thumb {
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: #fff;
  border: 5px solid var(--accent);
}

.prc-11 input[type=range]:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 6px;
}

.prc-11__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(220px,1fr));
  gap: 18px;
  width: min(880px,100%);
  margin: 0 auto;
}

.prc-11__card {
  position: relative;
  background: #161d17;
  border: 1.5px solid #263028;
  border-radius: 18px;
  padding: 28px;
  display: flex;
  flex-direction: column;
  gap: 8px;
  transition: border-color .35s,box-shadow .35s;
}

.prc-11__card.prc-11__best {
  border-color: var(--accent);
  box-shadow: 0 18px 44px -26px oklch(0.62 0.18 145/.6);
}

.prc-11__best-badge {
  position: absolute;
  top: -11px;
  right: 20px;
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .08em;
  text-transform: uppercase;
  padding: 4px 10px;
  border-radius: 99px;
  background: var(--accent);
  color: #0c130d;
  opacity: 0;
  transform: translateY(4px);
  transition: opacity .35s,transform .35s;
}

.prc-11__card.prc-11__best .prc-11__best-badge {
  opacity: 1;
  transform: translateY(0);
}

.prc-11__card h3 {
  font-size: 14px;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: #93a394;
}

.prc-11__total {
  font-size: 40px;
  font-weight: 800;
  letter-spacing: -.03em;
  font-variant-numeric: tabular-nums;
}

.prc-11__total small {
  font-size: 15px;
  font-weight: 600;
  color: #93a394;
}

.prc-11__math {
  font-size: 12px;
  color: #7c8c7d;
  min-height: 16px;
  margin-bottom: 10px;
  font-variant-numeric: tabular-nums;
}

.prc-11__card ul {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 8px;
  font-size: 13.5px;
  color: #bccabc;
  flex: 1;
  margin-bottom: 18px;
}

.prc-11__card li::before {
  content: "✓";
  color: var(--accent);
  font-weight: 700;
  margin-right: 8px;
}

.prc-11__cta {
  text-align: center;
  text-decoration: none;
  font-weight: 700;
  font-size: 13.5px;
  padding: 12px;
  border-radius: 11px;
  border: 1px solid #2c382e;
  color: #e9efe9;
  transition: border-color .2s,background .2s;
}

.prc-11__cta:hover {
  border-color: var(--accent);
}

.prc-11__card.prc-11__best .prc-11__cta {
  background: var(--accent);
  border-color: var(--accent);
  color: #0c130d;
}

.prc-11__cta:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

.prc-11__live {
  position: absolute;
  width: 1px;
  height: 1px;
  clip-path: inset(50%);
  overflow: hidden;
  white-space: nowrap;
}

@media (prefers-reduced-motion: reduce) {
  .prc-11__card,
    .prc-11__best-badge {
    transition-duration: .01s;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.prc-11');
  const range = root.querySelector('#prc-11-range');
  const out = root.querySelector('#prc-11-out');
  const live = root.querySelector('#prc-11-live');
  const cards = [...root.querySelectorAll('.prc-11__card')];
  const TIERS = [
    { name: 'Starter', base: 0, seat: 7 },
    { name: 'Team', base: 49, seat: 5 },
    { name: 'Business', base: 149, seat: 3.5 },
  ];
  const ANNOUNCE_MS = 600;
  let announceTimer;
  function update() {
    const seats = +range.value;
    out.textContent = seats;
    range.style.setProperty('--pct', ((seats - range.min) / (range.max - range.min) * 100) + '%');
    let bestIdx = 0, bestPrice = Infinity;
    TIERS.forEach((t, i) => {
      const total = Math.round(t.base + t.seat * seats);
      cards[i].querySelector('.prc-11__amount').textContent = '$' + total;
      cards[i].querySelector('.prc-11__math').textContent =
        (t.base ? '$' + t.base + ' base + ' : '') + '$' + t.seat + ' × ' + seats + ' seats';
      if (total < bestPrice) { bestPrice = total; bestIdx = i; }
    });
    cards.forEach((c, i) => c.classList.toggle('prc-11__best', i === bestIdx));
    clearTimeout(announceTimer);
    announceTimer = setTimeout(() => {
      live.textContent = seats + ' seats: best value is ' + TIERS[bestIdx].name + ' at $' + bestPrice + ' per month.';
    }, ANNOUNCE_MS);
  }
  range.addEventListener('input', update);
  update();
})();
```
