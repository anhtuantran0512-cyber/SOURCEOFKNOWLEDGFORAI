---
source: "codefronts"
url: "https://codefronts.com/motion/css-slide-in-animation/fintech-dashboard-kpi-card-with-count-up/"
title: "Fintech Dashboard KPI Card with Count-Up"
section: "motion"
category: "css-slide-in-animation"
category_name: "CSS Slide In Animation Templates"
description: "Four fintech dashboard KPI cards that slide up from below while their numeric values count up from zero — total revenue, active accounts, transaction volume,…"
has_js: "true"
---

Here's a working CSS Slide In Animation Template from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Fintech Dashboard KPI Card with Count-Up
Source: https://codefronts.com/motion/css-slide-in-animation/fintech-dashboard-kpi-card-with-count-up/

Four fintech dashboard KPI cards that slide up from below while their numeric values count up from zero — total revenue, active accounts, transaction volume, and monthly recurring revenue — the layout used by Stripe Dashboard, Mercury, and modern B2B fintech consoles.
## HTML
```html
<div class="sl-07">
  <div class="sl-07__inner">
    <div class="sl-07__head">
      <p class="sl-07__kicker">Q4 2026 · Live</p>
      <h2>Financial overview</h2>
    </div>
    <div class="sl-07__row">
      <div class="sl-07__card">
        <span class="sl-07__label">Total revenue</span>
        <div class="sl-07__val" data-target="1247830" data-prefix="$" data-comma="1">$0</div>
        <div class="sl-07__trend sl-07__trend--up">↑ 18.4% MoM</div>
      </div>
      <div class="sl-07__card">
        <span class="sl-07__label">Active accounts</span>
        <div class="sl-07__val" data-target="24680" data-comma="1">0</div>
        <div class="sl-07__trend sl-07__trend--up">↑ 12.8% MoM</div>
      </div>
      <div class="sl-07__card">
        <span class="sl-07__label">Transaction volume</span>
        <div class="sl-07__val" data-target="8420000" data-prefix="$" data-comma="1">$0</div>
        <div class="sl-07__trend sl-07__trend--up">↑ 24.1% MoM</div>
      </div>
      <div class="sl-07__card">
        <span class="sl-07__label">MRR growth</span>
        <div class="sl-07__val" data-target="14.7" data-suffix="%" data-decimals="1">0%</div>
        <div class="sl-07__trend sl-07__trend--up">↑ 2.3pp</div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.sl-07 {
  --bg: #0f172a;
  --card: #1e293b;
  --accent: #10b981;
  --danger: #f43f5e;
  --text: #f1f5f9;
  --sub: #94a3b8;
  --line: rgba(148,163,184,.12);
  font-family: -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 56px 24px;
  background: radial-gradient(80% 100% at 20% 0%, rgba(16,185,129,.08) 0%, transparent 60%), var(--bg);
  color: var(--text);
}

.sl-07 *,
.sl-07 *::before,
.sl-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sl-07 ::selection {
  background: var(--accent);
  color: #0f172a;
}

.sl-07__inner {
  width: 100%;
  max-width: 960px;
}

.sl-07__head {
  margin-bottom: 24px;
}

.sl-07__kicker {
  font-size: .7rem;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 6px;
}

.sl-07__head h2 {
  font-size: clamp(1.5rem,3vw,1.9rem);
  font-weight: 800;
  letter-spacing: -.02em;
}

.sl-07__row {
  display: grid;
  grid-template-columns: repeat(4,1fr);
  gap: 14px;
}

.sl-07__card {
  padding: 22px 22px;
  border: 1px solid var(--line);
  border-radius: 12px;
  background: linear-gradient(180deg,rgba(255,255,255,.02),rgba(255,255,255,0)),var(--card);
  box-shadow: 0 12px 28px -14px rgba(0,0,0,.4);
  opacity: 0;
  transform: translateY(30px);
  animation: sl-07-card .55s cubic-bezier(.22,1,.36,1) forwards;
}

.sl-07__card:nth-child(1) {
  animation-delay: .1s;
}

.sl-07__card:nth-child(2) {
  animation-delay: .25s;
}

.sl-07__card:nth-child(3) {
  animation-delay: .4s;
}

.sl-07__card:nth-child(4) {
  animation-delay: .55s;
}

.sl-07__label {
  display: block;
  font-size: .72rem;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--sub);
  margin-bottom: 10px;
}

.sl-07__val {
  font-size: 1.8rem;
  font-weight: 800;
  letter-spacing: -.02em;
  line-height: 1;
  margin-bottom: 8px;
  font-variant-numeric: tabular-nums;
  color: var(--text);
}

.sl-07__trend {
  display: inline-block;
  padding: 3px 8px;
  border-radius: 5px;
  font-size: .7rem;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
}

.sl-07__trend--up {
  background: rgba(16,185,129,.14);
  color: var(--accent);
}

.sl-07__trend--down {
  background: rgba(244,63,94,.14);
  color: var(--danger);
}

@keyframes sl-07-card {
  from {
    opacity: 0;
    transform: translateY(30px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sl-07__card {
    animation: none!important;
    opacity: 1!important;
    transform: none!important;
  }
}

@media (max-width: 820px) {
  .sl-07__row {
    grid-template-columns: repeat(2,1fr);
  }
}

@media (max-width: 520px) {
  .sl-07__row {
    grid-template-columns: 1fr;
  }
}
```

## JavaScript
```js
(function(){
  var vals = document.querySelectorAll('.sl-07__val');
  var reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
  vals.forEach(function(el, i){
    if (el.dataset.animated) return;
    el.dataset.animated = '1';
    var target = parseFloat(el.dataset.target) || 0;
    var prefix = el.dataset.prefix || '';
    var suffix = el.dataset.suffix || '';
    var decimals = parseInt(el.dataset.decimals || '0', 10);
    var comma = el.dataset.comma === '1';
    if (reduced) { el.textContent = prefix + format(target, decimals, comma) + suffix; return; }
    var duration = 1400;
    var delay = 200 + i * 150;
    setTimeout(function(){
      var start = null;
      function step(ts){
        if (!start) start = ts;
        var t = Math.min((ts - start) / duration, 1);
        var eased = 1 - Math.pow(1 - t, 3);
        var v = target * eased;
        el.textContent = prefix + format(v, decimals, comma) + suffix;
        if (t < 1) requestAnimationFrame(step);
      }
      requestAnimationFrame(step);
    }, delay);
  });
  function format(v, decimals, comma){
    var s = decimals > 0 ? v.toFixed(decimals) : String(Math.round(v));
    if (comma) {
      var parts = s.split('.');
      parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ',');
      s = parts.join('.');
    }
    return s;
  }
})();
```
