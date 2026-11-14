---
source: "codefronts"
url: "https://codefronts.com/motion/css-number-counter-animations/art-deco-real-estate/"
title: "Real Estate Price & Square Footage Counter"
section: "motion"
category: "css-number-counter-animations"
category_name: "CSS Number Counter Animations"
description: "A listing card that counts in the price and the floor area, then derives everything else from them — price per square foot, deposit, monthly repayment — so…"
has_js: "true"
---

Here's a working CSS Number Counter Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Real Estate Price & Square Footage Counter
Source: https://codefronts.com/motion/css-number-counter-animations/art-deco-real-estate/

A listing card that counts in the price and the floor area, then derives everything else from them — price per square foot, deposit, monthly repayment — so there is a single source of truth and the derived numbers can never contradict the headline. The down-payment slider recalculates the amortised payment live, which is exactly the interaction that keeps buyers on a listing page.
## HTML
```html
<section class="cnc-22" aria-label="Real estate price and square footage counter demo">
  <div class="cnc-22__stage">
    <article class="cnc-22__card">
      <div class="cnc-22__media">
        <img class="cnc-22__img" loading="lazy" decoding="async" width="900" height="600"
          src="https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?q=80&w=1200&auto=format&fit=crop"
          alt="Exterior of a modern two-storey house with a paved driveway">
        <span class="cnc-22__ribbon">New listing</span>
        <span class="cnc-22__addr">4218 Cedarline Way · Bellevue, WA</span>
      </div>
      <div class="cnc-22__body">
        <p class="cnc-22__price"><span class="cnc-22__pnum" aria-hidden="true">$0</span></p>
        <p class="cnc-22__true">Asking price $1,284,000 · <span class="cnc-22__ppsf" aria-hidden="true">$0</span><span class="cnc-22__ppsfl"> per sq ft</span></p>
        <ul class="cnc-22__facts">
          <li><b class="cnc-22__sqft" aria-hidden="true">0</b><span>sq ft</span></li>
          <li><b>4</b><span>beds</span></li>
          <li><b>3.5</b><span>baths</span></li>
          <li><b>0.31</b><span>acre lot</span></li>
        </ul>
        <div class="cnc-22__calc">
          <div class="cnc-22__calchead">
            <label class="cnc-22__lab" for="cnc-22-dp">Down payment</label>
            <output class="cnc-22__out" id="cnc-22-out" for="cnc-22-dp">20% · $256,800</output>
          </div>
          <input class="cnc-22__range" id="cnc-22-dp" type="range" min="5" max="45" step="1" value="20"
            aria-describedby="cnc-22-out">
          <div class="cnc-22__pay">
            <div><p class="cnc-22__k">Est. monthly</p><p class="cnc-22__v"><span class="cnc-22__mo">$0</span><small>/mo</small></p></div>
            <div><p class="cnc-22__k">Loan amount</p><p class="cnc-22__v"><span class="cnc-22__loan">$0</span></p></div>
          </div>
          <p class="cnc-22__fine">Estimate only · 30-year fixed at 6.25% APR, taxes and insurance excluded.</p>
        </div>
      </div>
    </article>
    <p class="cnc-22__chip" aria-hidden="true">one eased clock · derived $/sq ft · native range + output · Intl currency</p>
  </div>
</section>
```
## CSS
```css
.cnc-22,
.cnc-22 *,
.cnc-22 *::before,
.cnc-22 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cnc-22 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --cnc-22-bg: oklch(0.95 0.012 85);
  --cnc-22-card: oklch(1 0 0);
  --cnc-22-ink: oklch(0.24 0.02 265);
  --cnc-22-mut: oklch(0.57 0.02 265);
  --cnc-22-acc: oklch(0.52 0.11 158);
  --cnc-22-line: oklch(0 0 0/.09);
  background: var(--cnc-22-bg);
  color: var(--cnc-22-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
}

.cnc-22__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 18px;
  padding: clamp(16px,4vw,44px);
}

.cnc-22__card {
  --cnc-22-p: 37.5%;
  width: min(100%,860px);
  display: grid;
  grid-template-columns: 1fr;
  border-radius: 24px;
  overflow: hidden;
  background: var(--cnc-22-card);
  box-shadow: 0 1px 2px oklch(0 0 0/.05),0 30px 70px oklch(0.3 0.03 265/.18);
}

@media (min-width: 760px) {
  .cnc-22__card {
    grid-template-columns: 1.02fr 1fr;
  }
}

.cnc-22__media {
  position: relative;
  min-height: 230px;
  background: linear-gradient(150deg,oklch(0.72 0.07 160),oklch(0.45 0.06 240));
}

.cnc-22__img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  aspect-ratio: 3/2;
}

.cnc-22__ribbon {
  position: absolute;
  top: 16px;
  left: 16px;
  padding: 6px 12px;
  border-radius: 99px;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: oklch(0.99 0 0);
  background: var(--cnc-22-acc);
  box-shadow: 0 6px 18px oklch(0.4 0.08 158/.45);
}

.cnc-22__addr {
  position: absolute;
  left: 16px;
  right: 16px;
  bottom: 14px;
  font-size: 12.5px;
  font-weight: 600;
  color: oklch(0.99 0 0);
  text-shadow: 0 2px 10px oklch(0 0 0/.7);
}

.cnc-22__body {
  padding: clamp(20px,3.4vw,28px);
  display: flex;
  flex-direction: column;
}

.cnc-22__price {
  font-size: clamp(34px,6vw,46px);
  font-weight: 760;
  letter-spacing: -.055em;
  line-height: 1;
  font-variant-numeric: tabular-nums;
  font-feature-settings: 'tnum' 1;
}

.cnc-22__true {
  margin-top: 8px;
  font-size: 12.5px;
  color: var(--cnc-22-mut);
}

.cnc-22__ppsf {
  font-weight: 700;
  color: var(--cnc-22-ink);
  font-variant-numeric: tabular-nums;
}

.cnc-22__facts {
  list-style: none;
  display: grid;
  grid-template-columns: repeat(4,1fr);
  gap: 8px;
  margin-top: 20px;
  padding: 14px 0;
  border-top: 1px solid var(--cnc-22-line);
  border-bottom: 1px solid var(--cnc-22-line);
}

.cnc-22__facts b {
  display: block;
  font-size: 18px;
  font-weight: 730;
  letter-spacing: -.03em;
  font-variant-numeric: tabular-nums;
  font-feature-settings: 'tnum' 1;
}

.cnc-22__facts span {
  font-size: 11px;
  color: var(--cnc-22-mut);
}

.cnc-22__calc {
  margin-top: 20px;
}

.cnc-22__calchead {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 10px;
}

.cnc-22__lab {
  font-size: 12px;
  font-weight: 660;
  color: var(--cnc-22-mut);
}

.cnc-22__out {
  font-size: 13px;
  font-weight: 720;
  font-variant-numeric: tabular-nums;
  font-feature-settings: 'tnum' 1;
}

.cnc-22__range {
  -webkit-appearance: none;
  appearance: none;
  width: 100%;
  height: 44px;
  margin-top: 6px;
  background: transparent;
  cursor: pointer;
}

.cnc-22__range:focus-visible {
  outline: 3px solid var(--cnc-22-acc);
  outline-offset: 3px;
  border-radius: 12px;
}

.cnc-22__range::-webkit-slider-runnable-track {
  height: 8px;
  border-radius: 99px;
  background: linear-gradient(90deg,var(--cnc-22-acc) var(--cnc-22-p),oklch(0 0 0/.1) var(--cnc-22-p));
}

.cnc-22__range::-moz-range-track {
  height: 8px;
  border-radius: 99px;
  background: linear-gradient(90deg,var(--cnc-22-acc) var(--cnc-22-p),oklch(0 0 0/.1) var(--cnc-22-p));
}

.cnc-22__range::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 24px;
  height: 24px;
  margin-top: -8px;
  border-radius: 50%;
  background: var(--cnc-22-card);
  border: 2px solid var(--cnc-22-acc);
  box-shadow: 0 3px 10px oklch(0 0 0/.22);
  transition: transform .18s;
}

.cnc-22__range::-moz-range-thumb {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: var(--cnc-22-card);
  border: 2px solid var(--cnc-22-acc);
  box-shadow: 0 3px 10px oklch(0 0 0/.22);
}

.cnc-22__range:active::-webkit-slider-thumb {
  transform: scale(1.14);
}

.cnc-22__pay {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
  margin-top: 12px;
  padding: 14px 16px;
  border-radius: 16px;
  background: color-mix(in oklch,var(--cnc-22-acc) 8%,oklch(1 0 0));
}

.cnc-22__k {
  font-size: 11px;
  font-weight: 640;
  color: var(--cnc-22-mut);
}

.cnc-22__v {
  margin-top: 4px;
  font-size: 21px;
  font-weight: 750;
  letter-spacing: -.04em;
  font-variant-numeric: tabular-nums;
  font-feature-settings: 'tnum' 1;
}

.cnc-22__v small {
  font-size: .52em;
  font-weight: 640;
  color: var(--cnc-22-mut);
}

.cnc-22__fine {
  margin-top: 10px;
  font-size: 10.5px;
  line-height: 1.5;
  color: var(--cnc-22-mut);
}

.cnc-22__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--cnc-22-mut);
  padding: 7px 14px;
  border: 1px solid oklch(0 0 0/.12);
  border-radius: 99px;
  text-align: center;
  max-width: min(100%,560px);
}

@media (prefers-reduced-motion: reduce) {
  .cnc-22 * {
    animation: none !important;
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  const usd0 = new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD', maximumFractionDigits: 0 });
  const nf = new Intl.NumberFormat('en-US');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const PRICE = 1284000, SQFT = 3240, RATE = 0.0625, YEARS = 30;

  document.querySelectorAll('.cnc-22__card').forEach((card) => {
    if (card.dataset.wired) return;
    card.dataset.wired = '1';
    const pnum = card.querySelector('.cnc-22__pnum');
    const ppsf = card.querySelector('.cnc-22__ppsf');
    const sqft = card.querySelector('.cnc-22__sqft');
    const mo = card.querySelector('.cnc-22__mo');
    const loanEl = card.querySelector('.cnc-22__loan');
    const range = card.querySelector('.cnc-22__range');
    const out = card.querySelector('.cnc-22__out');

    const monthly = (principal) => {
      const r = RATE / 12, n = YEARS * 12;
      return principal * r / (1 - Math.pow(1 + r, -n));
    };
    const paint = (pct, price) => {
      const down = price * (pct / 100), loan = price - down;
      card.style.setProperty('--cnc-22-p', ((pct - 5) / 40 * 100) + '%');
      out.textContent = pct + '% · ' + usd0.format(down);
      loanEl.textContent = usd0.format(loan);
      mo.textContent = usd0.format(monthly(loan));
    };

    const run = (ms) => {
      if (reduce) {
        pnum.textContent = usd0.format(PRICE); sqft.textContent = nf.format(SQFT);
        ppsf.textContent = usd0.format(PRICE / SQFT); paint(+range.value, PRICE); return;
      }
      const t0 = performance.now();
      const step = (t) => {
        const p = Math.min(1, (t - t0) / ms), e = 1 - Math.pow(1 - p, 4);
        const price = Math.round(PRICE * e), area = Math.round(SQFT * e);
        pnum.textContent = usd0.format(price);
        sqft.textContent = nf.format(area);
        ppsf.textContent = usd0.format(area ? price / area : 0);   // derived every frame
        paint(+range.value, price);
        if (p < 1) requestAnimationFrame(step);
      };
      requestAnimationFrame(step);
    };

    range.addEventListener('input', () => paint(+range.value, PRICE));
    if ('IntersectionObserver' in window) {
      const io = new IntersectionObserver((es) => es.forEach((en) => {
        if (en.isIntersecting) { run(1500); io.disconnect(); }
      }), { threshold: 0.3 });
      io.observe(card);
    } else run(1500);
  });
})();
```
