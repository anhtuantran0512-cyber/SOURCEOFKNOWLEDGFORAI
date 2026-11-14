---
source: "codefronts"
url: "https://codefronts.com/snippets/css-faq-accordion/2-column-grid-faq-accordion-flexbox/"
title: "2-Column Grid FAQ Accordion Flexbox"
section: "snippets"
category: "css-faq-accordion"
category_name: "CSS FAQ Accordions"
description: "A wide FAQ split into two independent columns — the layout every marketing site wants past 8 questions, done so an opening panel pushes down only its own…"
has_js: "false"
---

Here's a working CSS FAQ Accordion from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: 2-Column Grid FAQ Accordion Flexbox
Source: https://codefronts.com/snippets/css-faq-accordion/2-column-grid-faq-accordion-flexbox/

A wide FAQ split into two independent columns — the layout every marketing site wants past 8 questions, done so an opening panel pushes down only its own column, never its horizontal neighbor. The tutorial covers the trap almost everyone hits (one grid of items = row-aligned cells that stretch each other), why the fix is two column containers, when flexbox beats grid here, and a container query that collapses to one column inside narrow parents.
## HTML
```html
<section class="cfa-14" aria-label="Two column grid FAQ accordion">
  <div class="cfa-14__stage">
    <div class="cfa-14__wrap">
      <header class="cfa-14__head">
        <h1>Everything buyers ask</h1>
        <p>Two independent columns — open any panel and only its own column reflows.</p>
      </header>
      <div class="cfa-14__cols">
        <div class="cfa-14__col">
          <details class="cfa-14__item" open>
            <summary class="cfa-14__q">How fast is onboarding?<i aria-hidden="true"></i></summary>
            <div class="cfa-14__a"><p>Most teams import their data and invite the team in under an hour. A guided setup checklist tracks the six steps, and a specialist can join a call for workspaces over 50 seats.</p></div>
          </details>
          <details class="cfa-14__item">
            <summary class="cfa-14__q">Can we migrate from a competitor?<i aria-hidden="true"></i></summary>
            <div class="cfa-14__a"><p>One-click importers cover the four biggest tools, mapping projects, comments and attachments. Anything else comes in via CSV or the API — migrations team included on annual plans.</p></div>
          </details>
          <details class="cfa-14__item">
            <summary class="cfa-14__q">Is training included?<i aria-hidden="true"></i></summary>
            <div class="cfa-14__a"><p>Live weekly webinars and a self-serve academy are free for everyone. Enterprise plans add two bespoke training sessions recorded for your internal wiki.</p></div>
          </details>
          <details class="cfa-14__item">
            <summary class="cfa-14__q">What uptime do you guarantee?<i aria-hidden="true"></i></summary>
            <div class="cfa-14__a"><p>99.9% on every paid plan, 99.99% with the enterprise SLA — backed by service credits, with a public status page and 5-year incident history.</p></div>
          </details>
        </div>
        <div class="cfa-14__col">
          <details class="cfa-14__item">
            <summary class="cfa-14__q">Where is data stored?<i aria-hidden="true"></i></summary>
            <div class="cfa-14__a"><p>US or EU region, chosen at workspace creation and never moved without written consent. Backups stay in-region, encrypted with per-tenant keys.</p></div>
          </details>
          <details class="cfa-14__item">
            <summary class="cfa-14__q">Do you support SSO / SCIM?<i aria-hidden="true"></i></summary>
            <div class="cfa-14__a"><p>SAML SSO and SCIM provisioning ship on the Business tier — Okta, Entra, Google and OneLogin have first-party guides. Enforced 2FA is available on every plan, free.</p></div>
          </details>
          <details class="cfa-14__item">
            <summary class="cfa-14__q">Can we self-host?<i aria-hidden="true"></i></summary>
            <div class="cfa-14__a"><p>No — and honestly, that is why the product ships weekly. The compliance package (SOC 2 Type II, ISO 27001, DPA, pen-test summaries) answers what self-hosting usually stands in for.</p></div>
          </details>
          <details class="cfa-14__item">
            <summary class="cfa-14__q">What's the contract minimum?<i aria-hidden="true"></i></summary>
            <div class="cfa-14__a"><p>None on monthly. Annual contracts are 12 months with a 60-day opt-out pilot window for new enterprise customers — if it isn't landing, you leave with a full refund.</p></div>
          </details>
        </div>
      </div>
      <p class="cfa-14__foot">Grid places the columns, flexbox stacks the items — the split is what keeps neighbors independent. CodeFronts collection.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.cfa-14,
.cfa-14 *,
.cfa-14 *::before,
.cfa-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cfa-14 {
  --bg: oklch(0.98 0.006 200);
  --panel: oklch(1 0 0);
  --ink: oklch(0.22 0.03 220);
  --mut: oklch(0.5 0.02 215);
  --line: oklch(0.89 0.012 205);
  --acc: oklch(0.6 0.13 210);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.cfa-14__stage {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(20px,4vw,56px);
  background: linear-gradient(180deg,color-mix(in oklch,var(--acc) 7%,var(--bg)),var(--bg) 35%);
  container: cfa14/inline-size;
}

.cfa-14__wrap {
  width: min(100%,960px);
}

.cfa-14__head {
  text-align: center;
}

.cfa-14__head h1 {
  font-size: clamp(26px,4cqi,40px);
  font-weight: 800;
  letter-spacing: -.025em;
}

.cfa-14__head p {
  margin-top: 8px;
  font-size: 14.5px;
  color: var(--mut);
}

.cfa-14__cols {
  margin-top: 30px;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0 clamp(18px,3cqi,36px);
  align-items: start;
}

.cfa-14__col {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.cfa-14__item {
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 14px;
  box-shadow: 0 2px 10px oklch(0.4 0.04 215/.05);
  interpolate-size: allow-keywords;
  transition: border-color .3s,box-shadow .3s;
}

.cfa-14__item[open] {
  border-color: color-mix(in oklch,var(--acc) 40%,var(--line));
  box-shadow: 0 10px 28px oklch(0.4 0.06 212/.1);
}

.cfa-14__q {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 14px;
  min-height: 44px;
  padding: 15px 17px;
  cursor: pointer;
  font-size: 14.5px;
  font-weight: 650;
  list-style: none;
  transition: color .2s;
}

.cfa-14__q::-webkit-details-marker {
  display: none;
}

.cfa-14__q:hover {
  color: var(--acc);
}

.cfa-14__q:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
  border-radius: 14px;
}

.cfa-14__q i {
  flex: none;
  width: 8px;
  height: 8px;
  border-right: 2px solid var(--acc);
  border-bottom: 2px solid var(--acc);
  rotate: 45deg;
  translate: 0 -2px;
  transition: rotate .35s;
}

.cfa-14__item[open] .cfa-14__q i {
  rotate: 225deg;
  translate: 0 2px;
}

.cfa-14__a p {
  padding: 0 17px 16px;
  font-size: 13.5px;
  line-height: 1.7;
  color: var(--mut);
}

@supports (interpolate-size: allow-keywords) {
  .cfa-14__item::details-content {
    height: 0;
    overflow: clip;
    opacity: 0;
    transition: height .38s cubic-bezier(.4,0,.2,1),opacity .3s,content-visibility .38s allow-discrete;
  }

  .cfa-14__item[open]::details-content {
    height: auto;
    opacity: 1;
  }
}

.cfa-14__foot {
  margin-top: 26px;
  text-align: center;
  font-size: 12.5px;
  color: var(--mut);
}

@container cfa14 (width < 680px) {
  .cfa-14__cols {
    grid-template-columns: 1fr;
    gap: 12px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cfa-14 *,
    .cfa-14 .cfa-14__item::details-content {
    transition-duration: .01ms !important;
  }
}
```
