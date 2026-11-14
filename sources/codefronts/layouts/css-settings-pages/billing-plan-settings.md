---
source: "codefronts"
url: "https://codefronts.com/layouts/css-settings-pages/billing-plan-settings/"
title: "Billing and Plan Settings Page"
section: "layouts"
category: "css-settings-pages"
category_name: "CSS Settings Pages"
description: "A premium SaaS billing page in pure CSS: a current-plan summary with seat math and a billing-period progress bar, a Monthly / Annual segmented toggle with a…"
has_js: "false"
---

Here's a working CSS Settings Page from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Billing and Plan Settings Page
Source: https://codefronts.com/layouts/css-settings-pages/billing-plan-settings/

A premium SaaS billing page in pure CSS: a current-plan summary with seat math and a billing-period progress bar, a Monthly / Annual segmented toggle with a sliding thumb that swaps every price on the page, selectable plan cards with a 'Current' badge, and a confirmation strip that appears only when you pick a different plan. Every interaction is driven by native radio inputs and the :has() selector — zero JavaScript.
## HTML
```html
<section class="csp-02">
  <div class="csp-02__wrap">
    <header class="csp-02__head">
      <div>
        <h1>Billing &amp; plan</h1>
        <p>Manage your subscription, seats and billing cycle.</p>
      </div>
      <fieldset class="csp-02__cycle">
        <legend class="csp-02__sr">Billing cycle</legend>
        <input type="radio" name="csp02-cycle" id="csp02-month" checked>
        <label for="csp02-month">Monthly</label>
        <input type="radio" name="csp02-cycle" id="csp02-year">
        <label for="csp02-year">Annual <em>Save 20%</em></label>
      </fieldset>
    </header>

    <article class="csp-02__current">
      <div class="csp-02__curmain">
        <span class="csp-02__eyebrow">Current plan</span>
        <h2>Pro <span class="csp-02__pill">Active</span></h2>
        <p><span class="csp-02__m">$24</span><span class="csp-02__y">$19</span> per seat × 8 seats · next invoice <strong><span class="csp-02__m">$192.00</span><span class="csp-02__y">$1,824.00</span></strong> on Nov 14, 2026</p>
      </div>
      <div class="csp-02__period">
        <div class="csp-02__periodtop"><span>Billing period</span><span>18 of 30 days</span></div>
        <div class="csp-02__track"><i style="width:60%"></i></div>
        <div class="csp-02__links"><a href="#">Manage seats</a><a href="#">Update payment method</a></div>
      </div>
    </article>

    <fieldset class="csp-02__plans">
      <legend class="csp-02__sr">Choose a plan</legend>
      <label class="csp-02__plan">
        <input type="radio" name="csp02-plan" class="csp-02__sr">
        <span class="csp-02__pname">Starter</span>
        <span class="csp-02__price"><b>$0</b><small>per seat / mo</small></span>
        <span class="csp-02__pdesc">For individuals getting organised.</span>
        <ul><li>Up to 3 projects</li><li>1 GB storage</li><li>Community support</li></ul>
        <span class="csp-02__cta">Downgrade</span>
      </label>
      <label class="csp-02__plan is-current">
        <input type="radio" name="csp02-plan" class="csp-02__sr" checked>
        <span class="csp-02__pname">Pro <span class="csp-02__badge">Current</span></span>
        <span class="csp-02__price"><b class="csp-02__m">$24</b><b class="csp-02__y">$19</b><small>per seat / mo</small></span>
        <span class="csp-02__pdesc">For growing teams shipping every week.</span>
        <ul><li>Unlimited projects</li><li>100 GB storage</li><li>Guest access &amp; SSO</li></ul>
        <span class="csp-02__cta">Your plan</span>
      </label>
      <label class="csp-02__plan">
        <input type="radio" name="csp02-plan" class="csp-02__sr">
        <span class="csp-02__pname">Business <span class="csp-02__badge csp-02__badge--alt">Recommended</span></span>
        <span class="csp-02__price"><b class="csp-02__m">$45</b><b class="csp-02__y">$36</b><small>per seat / mo</small></span>
        <span class="csp-02__pdesc">For organisations that need control.</span>
        <ul><li>Audit log &amp; SCIM</li><li>1 TB storage</li><li>Priority support, 99.9% SLA</li></ul>
        <span class="csp-02__cta">Upgrade</span>
      </label>
    </fieldset>

    <div class="csp-02__confirm" role="status">
      <p>You'll be switched at the end of the current period. Unused time is prorated.</p>
      <a class="csp-02__btn" href="#">Confirm plan change</a>
    </div>
  </div>
</section>
```
## CSS
```css
.csp-02,
.csp-02 *,
.csp-02 *::before,
.csp-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.csp-02 {
  --bg: oklch(0.16 0.015 270);
  --surface: oklch(0.205 0.018 270);
  --raised: oklch(0.24 0.02 270);
  --text: oklch(0.96 0.005 270);
  --muted: oklch(0.72 0.015 270);
  --line: oklch(0.31 0.02 270);
  --accent: oklch(0.78 0.14 165);
  --accent-ink: oklch(0.2 0.04 165);
  color-scheme: dark;
  container-type: inline-size;
  min-height: 100vh;
  min-height: 100dvh;
  padding: 40px 24px;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: radial-gradient(90% 60% at 80% -10%,oklch(0.3 0.06 200/.5),transparent 60%),var(--bg);
  color: var(--text);
  width: 100%;
}

.csp-02__sr {
  position: absolute!important;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.csp-02__wrap {
  max-width: 960px;
  margin-inline: auto;
  display: flex;
  flex-direction: column;
  gap: 22px;
}

.csp-02__head {
  display: flex;
  flex-wrap: wrap;
  align-items: flex-end;
  justify-content: space-between;
  gap: 16px;
}

.csp-02__head h1 {
  font: 700 30px/1.1 system-ui,sans-serif;
  letter-spacing: -.025em;
}

.csp-02__head p {
  font: 400 15px/1.5 system-ui,sans-serif;
  color: var(--muted);
  margin-top: 6px;
}

.csp-02__cycle {
  position: relative;
  display: grid;
  grid-template-columns: 1fr 1fr;
  padding: 4px;
  border: 1px solid var(--line);
  border-radius: 12px;
  background: var(--surface);
}

.csp-02__cycle::before {
  content: "";
  position: absolute;
  inset: 4px auto 4px 4px;
  width: calc(50% - 4px);
  border-radius: 9px;
  background: var(--raised);
  box-shadow: 0 1px 0 oklch(1 0 0/.06) inset,0 4px 12px oklch(0 0 0/.3);
  transition: translate .3s cubic-bezier(.3,.7,.3,1);
}

.csp-02__cycle input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.csp-02__cycle label {
  position: relative;
  z-index: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  min-height: 40px;
  padding: 0 16px;
  border-radius: 9px;
  font: 600 13.5px/1 system-ui,sans-serif;
  color: var(--muted);
  cursor: pointer;
  white-space: nowrap;
  transition: color .2s;
}

.csp-02__cycle label em {
  font: 700 10.5px/1 system-ui,sans-serif;
  font-style: normal;
  padding: 3px 6px;
  border-radius: 999px;
  color: var(--accent-ink);
  background: var(--accent);
}

.csp-02__cycle input:checked+label {
  color: var(--text);
}

.csp-02__cycle input:focus-visible+label {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.csp-02:has(#csp02-year:checked) .csp-02__cycle::before {
  translate: 100% 0;
}

.csp-02__y {
  display: none;
}

.csp-02:has(#csp02-year:checked) .csp-02__m {
  display: none;
}

.csp-02:has(#csp02-year:checked) .csp-02__y {
  display: inline;
}

.csp-02__current {
  display: grid;
  grid-template-columns: minmax(0,1.3fr) minmax(0,1fr);
  gap: 28px;
  padding: 24px;
  border: 1px solid var(--line);
  border-radius: 18px;
  background: linear-gradient(180deg,oklch(1 0 0/.03),transparent),var(--surface);
}

.csp-02__curmain {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.csp-02__eyebrow {
  font: 600 11px/1 ui-monospace,Menlo,monospace;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
}

.csp-02__current h2 {
  display: flex;
  align-items: center;
  gap: 10px;
  font: 700 26px/1.1 system-ui,sans-serif;
  letter-spacing: -.02em;
}

.csp-02__current p {
  font: 400 14px/1.6 system-ui,sans-serif;
  color: var(--muted);
  text-wrap: pretty;
}

.csp-02__current p strong {
  color: var(--text);
  font-weight: 650;
}

.csp-02__pill {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 4px 10px;
  border-radius: 999px;
  font: 600 11.5px/1 system-ui,sans-serif;
  color: var(--accent);
  background: oklch(0.78 0.14 165/.12);
}

.csp-02__pill::before {
  content: "";
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: currentColor;
}

.csp-02__period {
  display: flex;
  flex-direction: column;
  gap: 10px;
  justify-content: center;
}

.csp-02__periodtop {
  display: flex;
  justify-content: space-between;
  font: 500 13px/1 system-ui,sans-serif;
  color: var(--muted);
}

.csp-02__periodtop span:last-child {
  color: var(--text);
  font-variant-numeric: tabular-nums;
}

.csp-02__track {
  height: 8px;
  border-radius: 999px;
  background: oklch(1 0 0/.08);
  overflow: hidden;
}

.csp-02__track i {
  display: block;
  height: 100%;
  border-radius: inherit;
  background: linear-gradient(90deg,oklch(0.7 0.12 200),var(--accent));
}

.csp-02__links {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  margin-top: 4px;
}

.csp-02__links a {
  font: 600 13px/1 system-ui,sans-serif;
  color: var(--text);
  text-decoration: underline;
  text-decoration-color: oklch(1 0 0/.25);
  text-underline-offset: 4px;
}

.csp-02__links a:hover {
  text-decoration-color: var(--accent);
}

.csp-02__plans {
  border: 0;
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(240px,1fr));
  gap: 16px;
}

.csp-02__plan {
  position: relative;
  display: flex;
  flex-direction: column;
  gap: 12px;
  padding: 22px;
  border: 1px solid var(--line);
  border-radius: 18px;
  background: var(--surface);
  cursor: pointer;
  transition: border-color .2s,transform .2s,box-shadow .2s;
}

.csp-02__plan:hover {
  border-color: oklch(0.42 0.03 270);
  transform: translateY(-2px);
}

.csp-02__plan:has(input:checked) {
  border-color: var(--accent);
  box-shadow: 0 0 0 1px var(--accent),0 24px 50px -30px oklch(0.78 0.14 165/.6);
}

.csp-02__plan:has(input:focus-visible) {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.csp-02__pname {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
  font: 650 16px/1.2 system-ui,sans-serif;
}

.csp-02__badge {
  padding: 4px 9px;
  border-radius: 999px;
  font: 600 11px/1 system-ui,sans-serif;
  color: var(--muted);
  background: oklch(1 0 0/.07);
}

.csp-02__badge--alt {
  color: var(--accent-ink);
  background: var(--accent);
}

.csp-02__price {
  display: flex;
  align-items: baseline;
  gap: 8px;
}

.csp-02__price b {
  font: 750 38px/1 system-ui,sans-serif;
  letter-spacing: -.03em;
  font-variant-numeric: tabular-nums;
}

.csp-02__price small {
  font: 400 13px/1 system-ui,sans-serif;
  color: var(--muted);
}

.csp-02__pdesc {
  font: 400 13.5px/1.5 system-ui,sans-serif;
  color: var(--muted);
}

.csp-02__plan ul {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 8px;
  padding-top: 12px;
  border-top: 1px solid var(--line);
  flex: 1;
}

.csp-02__plan li {
  display: flex;
  gap: 9px;
  font: 400 13.5px/1.4 system-ui,sans-serif;
}

.csp-02__plan li::before {
  content: "";
  flex: none;
  width: 16px;
  height: 16px;
  margin-top: 1px;
  border-radius: 50%;
  background: oklch(0.78 0.14 165/.15) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Cpath d='m4.5 8.2 2.2 2.2 4.8-4.8' fill='none' stroke='%2366e0b4' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/16px no-repeat;
}

.csp-02__cta {
  display: grid;
  place-items: center;
  min-height: 44px;
  border-radius: 11px;
  font: 650 14px/1 system-ui,sans-serif;
  border: 1px solid var(--line);
  color: var(--text);
  transition: background .2s,color .2s;
}

.csp-02__plan:has(input:checked) .csp-02__cta {
  background: var(--accent);
  color: var(--accent-ink);
  border-color: transparent;
}

.csp-02__plan.is-current:has(input:checked) .csp-02__cta {
  background: transparent;
  color: var(--muted);
  border-color: var(--line);
}

.csp-02__confirm {
  display: none;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  flex-wrap: wrap;
  padding: 14px 14px 14px 20px;
  border-radius: 14px;
  background: var(--raised);
  border: 1px solid var(--line);
  animation: csp02-in .35s cubic-bezier(.2,.9,.3,1.1);
}

.csp-02__confirm p {
  font: 400 13.5px/1.5 system-ui,sans-serif;
  color: var(--muted);
}

.csp-02:has(.csp-02__plan:not(.is-current) input:checked) .csp-02__confirm {
  display: flex;
}

.csp-02__btn {
  display: inline-flex;
  align-items: center;
  min-height: 44px;
  padding: 0 18px;
  border-radius: 11px;
  font: 650 14px/1 system-ui,sans-serif;
  text-decoration: none;
  color: var(--accent-ink);
  background: var(--accent);
}

.csp-02__btn:focus-visible,
.csp-02__links a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

@keyframes csp02-in {
  from {
    opacity: 0;
    translate: 0 8px;
  }
}

@container (max-width: 640px) {
  .csp-02__current {
    grid-template-columns: minmax(0,1fr);
  }

  .csp-02__head {
    align-items: stretch;
    flex-direction: column;
  }
}

@media (prefers-reduced-motion: reduce) {
  .csp-02 * {
    transition: none!important;
    animation: none!important;
  }
}
```

## JavaScript
```js
/* No JavaScript by design — radio inputs + :has() drive every state. */
```
