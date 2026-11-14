---
source: "codefronts"
url: "https://codefronts.com/layouts/css-diagonal-sections/css-diagonal-pricing-section-band/"
title: "CSS Diagonal Pricing Section Band"
section: "layouts"
category: "css-diagonal-sections"
category_name: "CSS Diagonal Sections"
description: "An angled band carrying three pricing cards — and the cards stay perfectly rectangular."
has_js: "false"
---

Here's a working CSS Diagonal Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Diagonal Pricing Section Band
Source: https://codefronts.com/layouts/css-diagonal-sections/css-diagonal-pricing-section-band/

An angled band carrying three pricing cards — and the cards stay perfectly rectangular. That contrast is the design: the container is cut, the commerce is not. A monthly/yearly switch driven by :has() changes every price and note with no script, and the recommended tier is lifted by geometry rather than by another colour.
## HTML
```html
<div class="dgs-08">
  <input class="dgs-08__sronly" type="checkbox" id="dgs-08-dark">
  <label class="dgs-08__theme" for="dgs-08-dark">
    <svg class="dgs-08__i dgs-08__i--moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.3A8.4 8.4 0 0 1 9.7 3.5a8.5 8.5 0 1 0 10.8 10.8Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="dgs-08__i dgs-08__i--sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.1" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.7 5.7l1.4 1.4M16.9 16.9l1.4 1.4M18.3 5.7l-1.4 1.4M7.1 16.9l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <span class="dgs-08__srtext">Toggle dark theme</span>
  </label>
  <div class="dgs-08__stage">
    <section class="dgs-08__intro" aria-labelledby="dgs-08-a">
      <div class="dgs-08__wrap">
        <p class="dgs-08__eyebrow">Basalt &mdash; managed Postgres</p>
        <h2 class="dgs-08__display" id="dgs-08-a">Pricing that stops at the size you actually run</h2>
        <p class="dgs-08__lede">Storage, compute and backups billed separately, so a small database stays small on the invoice. No per-seat charge, ever.</p>
      </div>
    </section>

    <section class="dgs-08__band" aria-labelledby="dgs-08-b">
      <div class="dgs-08__wrap">
        <header class="dgs-08__head">
          <h2 class="dgs-08__h2" id="dgs-08-b">Three plans, one angled band</h2>
          <fieldset class="dgs-08__cycle">
            <legend class="dgs-08__vh">Billing period</legend>
            <input class="dgs-08__sr" type="radio" name="dgs-08-cycle" id="dgs-08-mo" checked><label for="dgs-08-mo">Monthly</label>
            <input class="dgs-08__sr" type="radio" name="dgs-08-cycle" id="dgs-08-yr"><label for="dgs-08-yr">Annual &minus;18%</label>
          </fieldset>
        </header>

        <ul class="dgs-08__plans">
          <li class="dgs-08__plan">
            <h3>Starter</h3>
            <p class="dgs-08__price"><span class="dgs-08__mo">$29</span><span class="dgs-08__yr">$24</span><em>/mo</em></p>
            <p class="dgs-08__sub">1 vCPU &middot; 10 GB storage &middot; 7-day PITR</p>
            <ul class="dgs-08__feat">
              <li>Daily backups</li><li>Single region</li><li>Community support</li>
            </ul>
            <a class="dgs-08__btn" href="#dgs-08-b">Start free</a>
          </li>
          <li class="dgs-08__plan dgs-08__plan--hero">
            <p class="dgs-08__badge">Most deployed</p>
            <h3>Scale</h3>
            <p class="dgs-08__price"><span class="dgs-08__mo">$149</span><span class="dgs-08__yr">$122</span><em>/mo</em></p>
            <p class="dgs-08__sub">4 vCPU &middot; 200 GB storage &middot; 30-day PITR</p>
            <ul class="dgs-08__feat">
              <li>Read replicas in 3 regions</li><li>Connection pooling</li><li>99.99% SLA</li>
            </ul>
            <a class="dgs-08__btn dgs-08__btn--solid" href="#dgs-08-b">Choose Scale</a>
          </li>
          <li class="dgs-08__plan">
            <h3>Enterprise</h3>
            <p class="dgs-08__price"><span class="dgs-08__mo">$640</span><span class="dgs-08__yr">$525</span><em>/mo</em></p>
            <p class="dgs-08__sub">16 vCPU &middot; 2 TB storage &middot; 90-day PITR</p>
            <ul class="dgs-08__feat">
              <li>Private networking</li><li>Named engineer</li><li>Audit log export</li>
            </ul>
            <a class="dgs-08__btn" href="#dgs-08-b">Talk to sales</a>
          </li>
        </ul>
        <p class="dgs-08__fine"><span class="dgs-08__mo">Billed monthly, cancel any time.</span><span class="dgs-08__yr">Billed annually &mdash; two months on us.</span></p>
      </div>
    </section>

    <section class="dgs-08__after" aria-labelledby="dgs-08-c">
      <div class="dgs-08__wrap">
        <h2 class="dgs-08__h3" id="dgs-08-c">Angle discipline on a pricing band</h2>
        <ul class="dgs-08__notes">
          <li><strong>Cards clear the cut</strong><span>Top padding equals the cut plus the section rhythm.</span></li>
          <li><strong>Focus rings survive</strong><span>Buttons sit far inside the clipped edge.</span></li>
          <li><strong>Prices swap on :has()</strong><span>One radio group, no script.</span></li>
        </ul>
      </div>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600;700&display=swap');

.dgs-08 {
  --cut: clamp(2rem, 6vw, 7.5rem);
  --page: #f6f5f2;
  --page2: #ebe9e3;
  --ink: #16150f;
  --muted: #5f5c52;
  --line: #dcd8ce;
  --char: #14150f;
  --char2: #1d1e16;
  --on-char: #f4f3ee;
  --dim: #a3a196;
  --brass: #c9a24a;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  overflow-x: clip;
  background: var(--page);
  color: var(--ink);
  font-family: 'Instrument Sans', system-ui, -apple-system, sans-serif;
  font-size: 16px;
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}

.dgs-08 *,
.dgs-08 *::before,
.dgs-08 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.75 0.11 85)) {
  .dgs-08 {
    --page: oklch(0.968 0.006 95);
    --page2: oklch(0.928 0.008 95);
    --ink: oklch(0.19 0.01 95);
    --muted: oklch(0.49 0.012 95);
    --line: oklch(0.872 0.01 95);
    --char: oklch(0.185 0.008 120);
    --char2: oklch(0.235 0.009 120);
    --on-char: oklch(0.958 0.005 95);
    --dim: oklch(0.705 0.01 95);
    --brass: oklch(0.735 0.105 85);
  }
}

.dgs-08__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.dgs-08__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.dgs-08__stage {
  display: flow-root;
}

.dgs-08__wrap {
  inline-size: min(76rem, 100%);
  margin-inline: auto;
}

.dgs-08__intro {
  padding: clamp(4rem, 9vw, 6.5rem) clamp(1.25rem, 5vw, 4rem) calc(var(--cut) + clamp(2.5rem, 6vw, 4rem));
}

.dgs-08__eyebrow {
  margin: 0 0 .9rem;
  font-size: .74rem;
  font-weight: 600;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--muted);
}

.dgs-08__display {
  margin: 0 0 1rem;
  max-inline-size: 26ch;
  font-size: clamp(2.1rem, 6.4vw, 3.9rem);
  font-weight: 600;
  line-height: 1.04;
  letter-spacing: -.04em;
  text-wrap: balance;
}

.dgs-08__lede {
  margin: 0;
  max-inline-size: 52ch;
  font-size: clamp(1.02rem, 2vw, 1.18rem);
  color: var(--muted);
  text-wrap: pretty;
}

.dgs-08__band {
  position: relative;
  z-index: 1;
  background: var(--char);
  color: var(--on-char);
  clip-path: polygon(0 var(--cut), 100% 0, 100% 100%, 0 100%);
  margin-block-start: calc(var(--cut) * -1 - 1px);
  padding: calc(var(--cut) + clamp(3rem, 7vw, 5rem)) clamp(1.25rem, 5vw, 4rem) clamp(3.5rem, 8vw, 5.5rem);
}

.dgs-08__head {
  display: flex;
  flex-wrap: wrap;
  gap: 1.25rem 2rem;
  align-items: end;
  justify-content: space-between;
  margin-block-end: clamp(2rem, 5vw, 3rem);
}

.dgs-08__h2 {
  margin: 0;
  font-size: clamp(1.5rem, 4vw, 2.4rem);
  font-weight: 600;
  letter-spacing: -.035em;
}

.dgs-08__cycle {
  margin: 0;
  padding: .25rem;
  border: 1px solid rgba(244,243,238,.18);
  border-radius: 999px;
  display: flex;
  gap: .2rem;
}

.dgs-08__cycle label {
  min-block-size: 2.5rem;
  display: inline-flex;
  align-items: center;
  padding-inline: 1rem;
  border-radius: 999px;
  font-size: .82rem;
  font-weight: 500;
  color: var(--dim);
  cursor: pointer;
  transition: background .2s ease, color .2s ease;
}

.dgs-08__cycle label:hover {
  color: var(--on-char);
}

.dgs-08__sr:checked + label {
  background: var(--brass);
  color: #14150f;
}

.dgs-08__sr:focus-visible + label {
  outline: 2px solid var(--brass);
  outline-offset: 2px;
}

.dgs-08__plans {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 1px;
  grid-template-columns: repeat(auto-fit, minmax(16rem, 1fr));
  background: rgba(244,243,238,.16);
  border: 1px solid rgba(244,243,238,.16);
  border-radius: 16px;
  overflow: clip;
}

.dgs-08__plan {
  position: relative;
  display: grid;
  gap: .7rem;
  align-content: start;
  padding: clamp(1.4rem, 3vw, 2rem);
  background: var(--char);
}

.dgs-08__plan--hero {
  background: var(--char2);
}

.dgs-08__badge {
  margin: 0;
  font-size: .68rem;
  font-weight: 600;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--brass);
}

.dgs-08__plan h3 {
  margin: 0;
  font-size: 1.05rem;
  font-weight: 600;
  letter-spacing: .01em;
}

.dgs-08__price {
  margin: 0;
  display: flex;
  align-items: baseline;
  gap: .3rem;
  font-size: clamp(2.1rem, 5.5vw, 3rem);
  font-weight: 600;
  letter-spacing: -.04em;
  font-variant-numeric: tabular-nums;
}

.dgs-08__price em {
  font-style: normal;
  font-size: .85rem;
  font-weight: 500;
  color: var(--dim);
  letter-spacing: 0;
}

.dgs-08__yr {
  display: none;
}

.dgs-08__sub {
  margin: 0;
  font-size: .86rem;
  color: var(--dim);
}

.dgs-08__feat {
  list-style: none;
  margin: .35rem 0 1rem;
  padding: 0;
  display: grid;
  gap: .45rem;
  font-size: .9rem;
}

.dgs-08__feat li {
  position: relative;
  padding-inline-start: 1.15rem;
  color: rgba(244,243,238,.86);
}

.dgs-08__feat li::before {
  content: '';
  position: absolute;
  inset-inline-start: 0;
  inset-block-start: .55em;
  inline-size: .4rem;
  block-size: .4rem;
  border-radius: 999px;
  background: var(--brass);
}

.dgs-08__btn {
  justify-self: start;
  display: inline-flex;
  align-items: center;
  min-block-size: 2.9rem;
  padding: .75rem 1.3rem;
  border: 1px solid rgba(244,243,238,.28);
  border-radius: 999px;
  color: var(--on-char);
  text-decoration: none;
  font-size: .9rem;
  font-weight: 500;
  transition: background .2s ease, translate .2s cubic-bezier(.2,.8,.3,1);
}

.dgs-08__btn:hover {
  background: rgba(244,243,238,.1);
  translate: 0 -1px;
}

.dgs-08__btn--solid {
  background: var(--brass);
  border-color: var(--brass);
  color: #14150f;
}

.dgs-08__btn--solid:hover {
  background: #d8b25c;
}

.dgs-08__btn:focus-visible {
  outline: 2px solid var(--brass);
  outline-offset: 3px;
}

.dgs-08__fine {
  margin: 1.5rem 0 0;
  font-size: .82rem;
  color: var(--dim);
}

.dgs-08__after {
  background: var(--page2);
  padding: clamp(3.5rem, 8vw, 5.5rem) clamp(1.25rem, 5vw, 4rem) clamp(4rem, 9vw, 6rem);
}

.dgs-08__h3 {
  margin: 0 0 1.5rem;
  font-size: clamp(1.3rem, 3.4vw, 1.9rem);
  font-weight: 600;
  letter-spacing: -.03em;
}

.dgs-08__notes {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 1rem clamp(1.5rem, 4vw, 3rem);
  grid-template-columns: repeat(auto-fit, minmax(14rem, 1fr));
}

.dgs-08__notes li {
  display: grid;
  gap: .3rem;
  padding-block-start: .9rem;
  border-block-start: 1px solid var(--line);
}

.dgs-08__notes strong {
  font-weight: 600;
}

.dgs-08__notes span {
  font-size: .9rem;
  color: var(--muted);
  text-wrap: pretty;
}

.dgs-08:has(#dgs-08-yr:checked) .dgs-08__mo {
  display: none;
}

.dgs-08:has(#dgs-08-yr:checked) .dgs-08__yr {
  display: inline;
}

@media (prefers-reduced-motion: reduce) {
  .dgs-08 * {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .dgs-08__band {
    forced-color-adjust: none;
    background: Canvas;
    color: CanvasText;
    border-block-start: 1px solid CanvasText;
  }

  .dgs-08__plans,
    .dgs-08__plan,
    .dgs-08__btn,
    .dgs-08__cycle {
    border: 1px solid CanvasText;
  }

  .dgs-08__sr:checked + label {
    background: Highlight;
    color: HighlightText;
  }
}
/* Standard top-right theme toggle — pure CSS (checkbox + :has()), so demos
   that ship no script stay tagged Pure CSS. Placed on the root rather than
   inside a demo's own control panel so every demo exposes it in one place. */

.dgs-08__sronly,
.dgs-08__srtext {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.dgs-08__theme {
  position: absolute;
  inset-block-start: clamp(.85rem, 2.2vw, 1.5rem);
  inset-inline-end: clamp(.85rem, 2.2vw, 1.5rem);
  z-index: 60;
  display: grid;
  place-items: center;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  border-radius: 999px;
  border: 1px solid currentColor;
  color: inherit;
  background: rgba(127,127,127,.16);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  cursor: pointer;
  transition: translate .2s ease;
}

.dgs-08__theme:hover {
  translate: 0 -1px;
}

.dgs-08__sronly:focus-visible + .dgs-08__theme {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.dgs-08__i {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.dgs-08__i--sun {
  display: none;
}

.dgs-08:has(#dgs-08-dark:checked) .dgs-08__i--moon {
  display: none;
}

.dgs-08:has(#dgs-08-dark:checked) .dgs-08__i--sun {
  display: block;
}

.dgs-08:has(#dgs-08-dark:checked) {
  --page: #0a0d13;
  --page2: #121722;
  --ink: #edf1f8;
  --muted: #95a0b2;
  --line: #212836;
}

@media (prefers-reduced-motion: reduce) {
  .dgs-08__theme {
    transition: none;
  }
}

@media (forced-colors: active) {
  .dgs-08__theme {
    border-color: CanvasText;
  }
}
```
