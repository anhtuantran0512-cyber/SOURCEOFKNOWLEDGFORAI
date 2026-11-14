---
source: "codefronts"
url: "https://codefronts.com/navigation/css-vertical-tabs/pricing-comparison-vertical-tabs/"
title: "Pricing Comparison Vertical Tabs"
section: "navigation"
category: "css-vertical-tabs"
category_name: "CSS Vertical Tabs"
description: "Two independent CSS-only controls on one surface: a vertical rail that swaps plans, and a monthly/annual segment that rewrites every price — without…"
has_js: "false"
---

Here's a working CSS Vertical Tab from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pricing Comparison Vertical Tabs
Source: https://codefronts.com/navigation/css-vertical-tabs/pricing-comparison-vertical-tabs/

Two independent CSS-only controls on one surface: a vertical rail that swaps plans, and a monthly/annual segment that rewrites every price — without duplicating a single card. Both prices live in the DOM at once and :has() decides which one is visible, so the annual saving is honest, the markup stays flat, and there is no JavaScript to hydrate.
## HTML
```html
<section class="vt-11" aria-label="Pricing comparison vertical tabs demo">
  <div class="vt-11__stage">
    <div class="vt-11__card">
      <div class="vt-11__rail" role="radiogroup" aria-label="Choose a plan">
        <div class="vt-11__col">
          <p class="vt-11__railhead">Choose a plan</p>
          <input class="vt-11__radio" type="radio" name="vt-11-plan" id="vt-11-t1">
          <label class="vt-11__tab" for="vt-11-t1"><span class="vt-11__tabhead"><b>Starter</b><small>Solo builders</small></span><span class="vt-11__tabprice"><span class="vt-11__mo">$12</span><span class="vt-11__yr">$120</span><i class="vt-11__cad vt-11__mo">/mo</i><i class="vt-11__cad vt-11__yr">/yr</i></span><span class="vt-11__caret" aria-hidden="true">›</span></label>
          <input class="vt-11__radio" type="radio" name="vt-11-plan" id="vt-11-t2" checked>
          <label class="vt-11__tab" for="vt-11-t2"><em class="vt-11__badge">Popular</em><span class="vt-11__tabhead"><b>Growth</b><small>Small teams</small></span><span class="vt-11__tabprice"><span class="vt-11__mo">$29</span><span class="vt-11__yr">$290</span><i class="vt-11__cad vt-11__mo">/mo</i><i class="vt-11__cad vt-11__yr">/yr</i></span><span class="vt-11__caret" aria-hidden="true">›</span></label>
          <input class="vt-11__radio" type="radio" name="vt-11-plan" id="vt-11-t3">
          <label class="vt-11__tab" for="vt-11-t3"><span class="vt-11__tabhead"><b>Scale</b><small>Growing orgs</small></span><span class="vt-11__tabprice"><span class="vt-11__mo">$79</span><span class="vt-11__yr">$790</span><i class="vt-11__cad vt-11__mo">/mo</i><i class="vt-11__cad vt-11__yr">/yr</i></span><span class="vt-11__caret" aria-hidden="true">›</span></label>
        </div>
        <div class="vt-11__panels">
          <article class="vt-11__panel" id="vt-11-p1">
            <h3 class="vt-11__h">Starter</h3>
            <p class="vt-11__price"><span class="vt-11__cur">$</span><b class="vt-11__mo">12</b><b class="vt-11__yr">120</b><span class="vt-11__per vt-11__mo">/mo, billed monthly</span><span class="vt-11__per vt-11__yr">/yr, billed annually</span></p>
            <ul class="vt-11__feat"><li data-on="1">3 projects<span class="vt-11__sr">Included</span></li><li data-on="1">Community support<span class="vt-11__sr">Included</span></li><li data-on="0">SSO &amp; SAML<span class="vt-11__sr">Not included</span></li><li data-on="0">Audit log<span class="vt-11__sr">Not included</span></li></ul>
          </article>
          <article class="vt-11__panel" id="vt-11-p2">
            <h3 class="vt-11__h">Growth</h3>
            <p class="vt-11__price"><span class="vt-11__cur">$</span><b class="vt-11__mo">29</b><b class="vt-11__yr">290</b><span class="vt-11__per vt-11__mo">/mo, billed monthly</span><span class="vt-11__per vt-11__yr">/yr, billed annually</span></p>
            <ul class="vt-11__feat"><li data-on="1">Unlimited projects<span class="vt-11__sr">Included</span></li><li data-on="1">Priority support<span class="vt-11__sr">Included</span></li><li data-on="1">SSO &amp; SAML<span class="vt-11__sr">Included</span></li><li data-on="0">Audit log<span class="vt-11__sr">Not included</span></li></ul>
          </article>
          <article class="vt-11__panel" id="vt-11-p3">
            <h3 class="vt-11__h">Scale</h3>
            <p class="vt-11__price"><span class="vt-11__cur">$</span><b class="vt-11__mo">79</b><b class="vt-11__yr">790</b><span class="vt-11__per vt-11__mo">/mo, billed monthly</span><span class="vt-11__per vt-11__yr">/yr, billed annually</span></p>
            <ul class="vt-11__feat"><li data-on="1">Unlimited projects<span class="vt-11__sr">Included</span></li><li data-on="1">Dedicated CSM<span class="vt-11__sr">Included</span></li><li data-on="1">SSO &amp; SAML<span class="vt-11__sr">Included</span></li><li data-on="1">Audit log<span class="vt-11__sr">Included</span></li></ul>
          </article>
          <div class="vt-11__cycle" role="radiogroup" aria-label="Billing cycle">
            <input class="vt-11__cyradio" type="radio" name="vt-11-cycle" id="vt-11-c-mo" checked>
            <label for="vt-11-c-mo">Monthly</label>
            <input class="vt-11__cyradio" type="radio" name="vt-11-cycle" id="vt-11-c-yr">
            <label for="vt-11-c-yr">Annual <em>2 months free</em></label>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.vt-11 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--vt-11-bg);
  --vt-11-bg: oklch(0.15 0.02 265);
  --vt-11-card: oklch(0.205 0.024 265);
  --vt-11-rail: oklch(0.185 0.022 265);
  --vt-11-ink: oklch(0.97 0.006 265);
  --vt-11-mut: oklch(0.7 0.016 265);
  --vt-11-acc: oklch(0.82 0.17 88);
  --vt-11-line: oklch(1 0 0/.1);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--vt-11-ink);
}

.vt-11 *,
.vt-11 *::before,
.vt-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.vt-11__stage {
  min-height: 100svh;
  display: grid;
  place-content: center;
  justify-items: center;
  padding: clamp(16px,4vw,56px);
  background: radial-gradient(65% 50% at 80% 0%,oklch(0.34 0.09 80/.45),transparent),radial-gradient(55% 45% at 10% 100%,oklch(0.3 0.07 300/.4),transparent);
}

.vt-11__card {
  width: min(96vw,900px);
  border: 1px solid var(--vt-11-line);
  border-radius: 20px;
  background: var(--vt-11-card);
  box-shadow: 0 30px 80px -38px oklch(0 0 0/.85);
  overflow: hidden;
}

.vt-11__rail {
  display: grid;
  grid-template-columns: minmax(220px,272px) minmax(0,1fr);
  align-items: stretch;
}

.vt-11__col {
  display: flex;
  flex-direction: column;
  gap: 6px;
  background: var(--vt-11-rail);
  padding: 14px 12px 16px;
  border-right: 1px solid var(--vt-11-line);
}

.vt-11__railhead {
  padding: 4px 8px 8px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 10px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: color-mix(in oklch,var(--vt-11-mut) 80%,transparent);
}

.vt-11__radio,
.vt-11__cyradio {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.vt-11__tab {
  position: relative;
  display: grid;
  grid-template-columns: 1fr auto auto;
  align-items: center;
  gap: 14px;
  padding: 14px 40px 14px 16px;
  border-radius: 12px;
  border: 1px solid transparent;
  background: color-mix(in oklch,var(--vt-11-card) 60%,transparent);
  color: var(--vt-11-mut);
  cursor: pointer;
  transition: color .2s ease,background .2s ease,border-color .2s ease,transform .2s ease;
}

.vt-11__tabhead {
  display: grid;
  gap: 3px;
  min-inline-size: 0;
}

.vt-11__tabhead b {
  font-size: 14.4px;
  font-weight: 700;
  letter-spacing: -.01em;
  color: var(--vt-11-ink);
}

.vt-11__tabhead small {
  font-size: 11.5px;
  font-weight: 500;
  color: var(--vt-11-mut);
}

.vt-11__tabprice {
  display: flex;
  align-items: baseline;
  gap: 2px;
  font-variant-numeric: tabular-nums;
  color: var(--vt-11-mut);
  transition: color .2s ease;
}

.vt-11__tabprice span:not(.vt-11__cad) {
  font-size: 15.4px;
  font-weight: 700;
  letter-spacing: -.02em;
}

.vt-11__cad {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 10.5px;
  font-style: normal;
  opacity: .7;
}

.vt-11__caret {
  position: absolute;
  inset-inline-end: 14px;
  inset-block-start: 50%;
  translate: 0 -50%;
  font-size: 16px;
  line-height: 1;
  color: var(--vt-11-mut);
  opacity: 0;
  transform: translateX(-3px);
  transition: opacity .22s ease,transform .22s ease,color .22s ease;
}

.vt-11__badge {
  position: absolute;
  inset-block-start: -7px;
  inset-inline-end: 12px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 9px;
  font-style: normal;
  letter-spacing: .1em;
  text-transform: uppercase;
  padding: 3px 8px;
  border-radius: 99px;
  background: var(--vt-11-acc);
  color: oklch(0.18 0.02 265);
  box-shadow: 0 4px 12px -4px color-mix(in oklch,var(--vt-11-acc) 60%,transparent);
}

.vt-11__tab:hover {
  background: oklch(1 0 0/.04);
  border-color: oklch(1 0 0/.06);
}

.vt-11__tab:hover .vt-11__caret {
  opacity: .4;
  transform: translateX(0);
}

.vt-11__radio:checked+.vt-11__tab {
  background: linear-gradient(135deg,color-mix(in oklch,var(--vt-11-acc) 18%,transparent),color-mix(in oklch,var(--vt-11-acc) 6%,transparent));
  border-color: color-mix(in oklch,var(--vt-11-acc) 46%,transparent);
  color: var(--vt-11-ink);
}

.vt-11__radio:checked+.vt-11__tab .vt-11__tabprice {
  color: var(--vt-11-acc);
}

.vt-11__radio:checked+.vt-11__tab .vt-11__caret {
  opacity: 1;
  transform: translateX(0);
  color: var(--vt-11-acc);
}

.vt-11__radio:focus-visible+.vt-11__tab {
  outline: 2px solid var(--vt-11-acc);
  outline-offset: 2px;
}

.vt-11__panels {
  position: relative;
  display: grid;
  min-height: clamp(300px,38vw,352px);
  padding: clamp(22px,3.4vw,38px);
}

.vt-11__panel {
  grid-area: 1/1;
  align-content: center;
  display: grid;
  gap: 14px;
  justify-items: start;
  padding-block-end: 56px;
  opacity: 0;
  visibility: hidden;
  transform: translateY(9px);
  transition: opacity .3s ease,transform .36s cubic-bezier(.32,.72,.3,1),visibility 0s .36s;
}

.vt-11__card:has(#vt-11-t1:checked) #vt-11-p1,
.vt-11__card:has(#vt-11-t2:checked) #vt-11-p2,
.vt-11__card:has(#vt-11-t3:checked) #vt-11-p3 {
  opacity: 1;
  visibility: visible;
  transform: none;
  transition-delay: 0s;
}

.vt-11__h {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--vt-11-acc);
}

.vt-11__price {
  display: flex;
  align-items: baseline;
  gap: 5px;
  flex-wrap: wrap;
  font-variant-numeric: tabular-nums;
}

.vt-11__cur {
  font-size: 22px;
  font-weight: 600;
  color: var(--vt-11-mut);
}

.vt-11__price b {
  font-size: clamp(40px,6.4vw,58px);
  line-height: 1;
  font-weight: 750;
  letter-spacing: -.04em;
}

.vt-11__per {
  font-size: 13px;
  color: var(--vt-11-mut);
}

.vt-11__yr {
  display: none;
}

.vt-11__card:has(#vt-11-c-yr:checked) .vt-11__mo {
  display: none;
}

.vt-11__card:has(#vt-11-c-yr:checked) .vt-11__yr {
  display: inline;
}

.vt-11__feat {
  list-style: none;
  display: grid;
  gap: 9px;
}

.vt-11__feat li {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 14.2px;
  color: var(--vt-11-mut);
}

.vt-11__feat li::before {
  content: "";
  inline-size: 17px;
  block-size: 17px;
  flex: none;
  border-radius: 99px;
  background: color-mix(in oklch,var(--vt-11-acc) 18%,transparent);
  box-shadow: inset 0 0 0 1px color-mix(in oklch,var(--vt-11-acc) 45%,transparent);
}

.vt-11__feat li[data-on="1"] {
  color: var(--vt-11-ink);
}

.vt-11__feat li[data-on="1"]::before {
  background: var(--vt-11-acc);
  box-shadow: none;
}

.vt-11__feat li[data-on="0"] {
  opacity: .55;
}

.vt-11__feat li[data-on="0"]::before {
  background: transparent;
  box-shadow: inset 0 0 0 1px oklch(1 0 0/.22);
}

.vt-11__cycle {
  position: absolute;
  inset-block-end: clamp(18px,2.6vw,28px);
  inset-inline-start: clamp(22px,3.4vw,38px);
  display: flex;
  gap: 4px;
  padding: 4px;
  border-radius: 99px;
  background: oklch(0 0 0/.3);
  border: 1px solid var(--vt-11-line);
}

.vt-11__cycle label {
  display: flex;
  align-items: center;
  gap: 7px;
  min-height: 36px;
  padding: 0 14px;
  border-radius: 99px;
  font-size: 12.6px;
  font-weight: 600;
  color: var(--vt-11-mut);
  cursor: pointer;
  transition: color .2s ease,background .2s ease;
}

.vt-11__cycle label em {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 9.5px;
  font-style: normal;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: var(--vt-11-acc);
}

.vt-11__cycle label:hover {
  color: var(--vt-11-ink);
}

.vt-11__cyradio:checked+label {
  color: oklch(0.18 0.02 265);
  background: var(--vt-11-acc);
}

.vt-11__cyradio:checked+label em {
  color: oklch(0.18 0.02 265);
  opacity: .7;
}

.vt-11__cyradio:focus-visible+label {
  outline: 2px solid var(--vt-11-acc);
  outline-offset: 2px;
}

.vt-11__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

@media (max-width: 680px) {
  .vt-11__rail {
    grid-template-columns: 1fr;
  }

  .vt-11__col {
    border-right: 0;
    border-bottom: 1px solid var(--vt-11-line);
  }

  .vt-11__cycle {
    position: static;
    margin-block-start: 6px;
  }

  .vt-11__panel {
    padding-block-end: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .vt-11 * {
    transition-duration: .01ms !important;
  }
}
```
