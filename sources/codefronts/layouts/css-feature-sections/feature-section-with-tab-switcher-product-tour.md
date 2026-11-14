---
source: "codefronts"
url: "https://codefronts.com/layouts/css-feature-sections/feature-section-with-tab-switcher-product-tour/"
title: "Feature Section with Tab Switcher Product Tour"
section: "layouts"
category: "css-feature-sections"
category_name: "CSS Feature Sections"
description: "A product-tour feature block: five labelled tabs across the top, and the active tab swaps a CSS-drawn product screenshot plus a three-point benefit list…"
has_js: "true"
---

Here's a working CSS Feature Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Feature Section with Tab Switcher Product Tour
Source: https://codefronts.com/layouts/css-feature-sections/feature-section-with-tab-switcher-product-tour/

A product-tour feature block: five labelled tabs across the top, and the active tab swaps a CSS-drawn product screenshot plus a three-point benefit list underneath. Panel switching is a radio group and a sibling combinator, so the swap costs no script and survives with JS disabled; the twenty lines of JS only add arrow-key and Home / End roving so the strip behaves like a real tablist.
## HTML
```html
<section class="fs-01" aria-labelledby="fs-01-heading">
  <div class="fs-01__hero" aria-hidden="true">
    <span class="fs-01__wordmark">Meridian</span>
    <span class="fs-01__herotext">Ship the pipeline, not the plumbing</span>
  </div>

  <div class="fs-01__stage">
    <div class="fs-01__head">
      <p class="fs-01__eyebrow">Product tour</p>
      <h2 class="fs-01__heading" id="fs-01-heading">Five surfaces, one control plane</h2>
      <p class="fs-01__sub">Every team touches a different part of Meridian. Step through the ones yours will live in.</p>
    </div>

    <div class="fs-01__tour">
      <input class="fs-01__radio" type="radio" name="fs-01-tabs" id="fs-01-t1" checked>
      <input class="fs-01__radio" type="radio" name="fs-01-tabs" id="fs-01-t2">
      <input class="fs-01__radio" type="radio" name="fs-01-tabs" id="fs-01-t3">
      <input class="fs-01__radio" type="radio" name="fs-01-tabs" id="fs-01-t4">
      <input class="fs-01__radio" type="radio" name="fs-01-tabs" id="fs-01-t5">

      <div class="fs-01__tabs" role="tablist" aria-label="Product tour sections">
        <label class="fs-01__tab" for="fs-01-t1" role="tab" id="fs-01-lab1" aria-controls="fs-01-p1" aria-selected="true">Overview</label>
        <label class="fs-01__tab" for="fs-01-t2" role="tab" id="fs-01-lab2" aria-controls="fs-01-p2" aria-selected="false">Analytics</label>
        <label class="fs-01__tab" for="fs-01-t3" role="tab" id="fs-01-lab3" aria-controls="fs-01-p3" aria-selected="false">Automations</label>
        <label class="fs-01__tab" for="fs-01-t4" role="tab" id="fs-01-lab4" aria-controls="fs-01-p4" aria-selected="false">Integrations</label>
        <label class="fs-01__tab" for="fs-01-t5" role="tab" id="fs-01-lab5" aria-controls="fs-01-p5" aria-selected="false">Security</label>
      </div>

      <div class="fs-01__panels">
        <article class="fs-01__panel" data-tab="1" role="tabpanel" id="fs-01-p1" aria-labelledby="fs-01-lab1">
          <div class="fs-01__shot">
            <div class="fs-01__shotbar"><span></span><span></span><span></span></div>
            <div class="fs-01__shotgrid">
              <div class="fs-01__tile fs-01__tile--wide"><b>Warehouse sync</b><i style="inline-size:82%"></i><i style="inline-size:64%"></i></div>
              <div class="fs-01__tile"><b>Freshness</b><i style="inline-size:44%"></i></div>
              <div class="fs-01__tile"><b>Owners</b><i style="inline-size:70%"></i></div>
              <div class="fs-01__tile fs-01__tile--wide"><b>Run history</b><i style="inline-size:90%"></i><i style="inline-size:36%"></i></div>
            </div>
          </div>
          <div class="fs-01__copy">
            <h3 class="fs-01__ptitle">One place every pipeline reports to</h3>
            <ul class="fs-01__list">
              <li>Model, run and owner in a single view — no tab archaeology</li>
              <li>Freshness SLAs per dataset with a breach timeline</li>
              <li>Column-level lineage rendered from the warehouse itself</li>
            </ul>
            <a class="fs-01__cta" href="#fs-01-heading">Read the overview docs</a>
          </div>
        </article>

        <article class="fs-01__panel" data-tab="2" role="tabpanel" id="fs-01-p2" aria-labelledby="fs-01-lab2">
          <div class="fs-01__shot">
            <div class="fs-01__shotbar"><span></span><span></span><span></span></div>
            <div class="fs-01__chart">
              <div style="block-size:38%"></div><div style="block-size:56%"></div><div style="block-size:44%"></div>
              <div style="block-size:72%"></div><div style="block-size:61%"></div><div style="block-size:88%"></div>
              <div style="block-size:70%"></div><div style="block-size:96%"></div>
            </div>
            <p class="fs-01__shotcap">Events per minute · rolling 8h</p>
          </div>
          <div class="fs-01__copy">
            <h3 class="fs-01__ptitle">Query the event stream, not a nightly export</h3>
            <ul class="fs-01__list">
              <li>Sub-second aggregates over the last 30 days of raw events</li>
              <li>Saved segments that any teammate can fork and rerun</li>
              <li>Every chart exports as SQL you can paste into your editor</li>
            </ul>
            <a class="fs-01__cta" href="#fs-01-heading">See the query reference</a>
          </div>
        </article>

        <article class="fs-01__panel" data-tab="3" role="tabpanel" id="fs-01-p3" aria-labelledby="fs-01-lab3">
          <div class="fs-01__shot">
            <div class="fs-01__shotbar"><span></span><span></span><span></span></div>
            <div class="fs-01__flow">
              <div class="fs-01__node">Row lands</div>
              <div class="fs-01__wire"></div>
              <div class="fs-01__node">Schema check</div>
              <div class="fs-01__wire"></div>
              <div class="fs-01__node fs-01__node--on">Notify owner</div>
            </div>
          </div>
          <div class="fs-01__copy">
            <h3 class="fs-01__ptitle">Rules that run the moment data lands</h3>
            <ul class="fs-01__list">
              <li>Trigger on schema drift, null spikes or a missed SLA</li>
              <li>Branching conditions without a workflow DSL to learn</li>
              <li>Dry-run any automation against last week of real rows</li>
            </ul>
            <a class="fs-01__cta" href="#fs-01-heading">Browse automation recipes</a>
          </div>
        </article>

        <article class="fs-01__panel" data-tab="4" role="tabpanel" id="fs-01-p4" aria-labelledby="fs-01-lab4">
          <div class="fs-01__shot">
            <div class="fs-01__shotbar"><span></span><span></span><span></span></div>
            <div class="fs-01__shotgrid">
              <div class="fs-01__tile"><b>Snowflake</b><i style="inline-size:100%"></i></div>
              <div class="fs-01__tile"><b>BigQuery</b><i style="inline-size:100%"></i></div>
              <div class="fs-01__tile"><b>Kafka</b><i style="inline-size:78%"></i></div>
              <div class="fs-01__tile"><b>Postgres</b><i style="inline-size:100%"></i></div>
              <div class="fs-01__tile"><b>S3</b><i style="inline-size:92%"></i></div>
              <div class="fs-01__tile"><b>dbt</b><i style="inline-size:100%"></i></div>
            </div>
          </div>
          <div class="fs-01__copy">
            <h3 class="fs-01__ptitle">Connectors that speak your warehouse dialect</h3>
            <ul class="fs-01__list">
              <li>Nineteen first-party sources with incremental backfill</li>
              <li>Typed client generation for TypeScript, Python and Go</li>
              <li>Bring your own connector through the ingest API</li>
            </ul>
            <a class="fs-01__cta" href="#fs-01-heading">View all connectors</a>
          </div>
        </article>

        <article class="fs-01__panel" data-tab="5" role="tabpanel" id="fs-01-p5" aria-labelledby="fs-01-lab5">
          <div class="fs-01__shot">
            <div class="fs-01__shotbar"><span></span><span></span><span></span></div>
            <div class="fs-01__shotgrid">
              <div class="fs-01__tile fs-01__tile--wide"><b>SSO · SAML 2.0</b><i style="inline-size:100%"></i></div>
              <div class="fs-01__tile"><b>SCIM</b><i style="inline-size:100%"></i></div>
              <div class="fs-01__tile"><b>Audit log</b><i style="inline-size:86%"></i></div>
              <div class="fs-01__tile fs-01__tile--wide"><b>Field-level encryption</b><i style="inline-size:74%"></i></div>
            </div>
          </div>
          <div class="fs-01__copy">
            <h3 class="fs-01__ptitle">Controls your security review already asks for</h3>
            <ul class="fs-01__list">
              <li>SAML SSO with SCIM provisioning and deprovisioning</li>
              <li>Per-field encryption keys held in your own KMS</li>
              <li>Immutable audit log streamed to your SIEM</li>
            </ul>
            <a class="fs-01__cta" href="#fs-01-heading">Read the security overview</a>
          </div>
        </article>
      </div>
    </div>
  </div>

  <div class="fs-01__below" aria-hidden="true">
    <span>Trusted by 4,100 data teams</span>
    <span>Pricing next</span>
  </div>
</section>
```
## CSS
```css
.fs-01 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --s0: #070d18;
  --s0: oklch(0.17 0.032 258);
  --s1: #0d1526;
  --s1: oklch(0.22 0.036 258);
  --s2: #14203a;
  --s2: oklch(0.27 0.045 258);
  --s3: #1d2c4c;
  --s3: oklch(0.33 0.05 258);
  --ink: #eef3fb;
  --ink: oklch(0.97 0.012 250);
  --muted: #9aabc6;
  --muted: oklch(0.74 0.031 254);
  --accent: #3ddbe0;
  --accent: oklch(0.85 0.115 195);
  --rule: #223354;
  --rule: oklch(0.31 0.043 258);
  --panel-min: 26rem;
  --font-display: "Söhne", system-ui, -apple-system, "Segoe UI", sans-serif;
  background: var(--s0);
  color: var(--ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  padding: 0 0 0;
}

.fs-01 *,
.fs-01 *::before,
.fs-01 *::after {
  box-sizing: border-box;
}

.fs-01__hero {
  display: flex;
  flex-wrap: wrap;
  gap: 8px 18px;
  align-items: baseline;
  padding: 18px 20px;
  border-bottom: 1px solid var(--rule);
  background: var(--s1);
}

.fs-01__wordmark {
  font: 700 14px/1 var(--font-display);
  letter-spacing: -0.02em;
}

.fs-01__herotext {
  font-size: 12.5px;
  color: var(--muted);
}

.fs-01__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  padding: clamp(30px, 6vw, 68px) 16px;
}

.fs-01__head {
  inline-size: 100%;
  max-inline-size: 62rem;
  min-inline-size: 0;
  margin: 0 0 28px;
}

.fs-01__eyebrow {
  margin: 0 0 12px;
  font: 700 10.5px/1 var(--font-display);
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--accent);
}

.fs-01__heading {
  margin: 0 0 12px;
  font: 600 clamp(26px, 5vw, 42px)/1.1 var(--font-display);
  letter-spacing: -0.03em;
  text-wrap: balance;
}

.fs-01__sub {
  margin: 0;
  max-inline-size: 46ch;
  font-size: 15px;
  line-height: 1.65;
  color: var(--muted);
  text-wrap: pretty;
}

.fs-01__tour {
  inline-size: 100%;
  max-inline-size: 62rem;
  min-inline-size: 0;
}

.fs-01__radio {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  clip-path: inset(50%);
  overflow: hidden;
  white-space: nowrap;
}

.fs-01__tabs {
  display: flex;
  gap: 4px;
  margin: 0 0 22px;
  padding: 4px;
  background: var(--s1);
  border: 1px solid var(--rule);
  border-radius: 10px;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  scrollbar-width: thin;
}

.fs-01__tab {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  flex: 1 1 auto;
  min-inline-size: max-content;
  min-height: 44px;
  padding: 0 16px;
  font: 600 13px/1 var(--font-display);
  letter-spacing: -0.01em;
  color: var(--muted);
  border-radius: 7px;
  cursor: pointer;
  scroll-snap-align: start;
  white-space: nowrap;
  transition: color .18s ease, background-color .18s ease;
}

.fs-01__tab:hover {
  color: var(--ink);
  background: var(--s2);
}

.fs-01__tab::after {
  content: "";
  position: absolute;
  inset-inline: 14px;
  inset-block-end: 4px;
  block-size: 2px;
  border-radius: 2px;
  background: var(--accent);
  transform: scaleX(0);
  transition: transform .2s ease;
}

#fs-01-t1:checked ~ .fs-01__tabs [for="fs-01-t1"],
#fs-01-t2:checked ~ .fs-01__tabs [for="fs-01-t2"],
#fs-01-t3:checked ~ .fs-01__tabs [for="fs-01-t3"],
#fs-01-t4:checked ~ .fs-01__tabs [for="fs-01-t4"],
#fs-01-t5:checked ~ .fs-01__tabs [for="fs-01-t5"] {
  color: var(--ink);
  background: var(--s2);
}

#fs-01-t1:checked ~ .fs-01__tabs [for="fs-01-t1"]::after,
#fs-01-t2:checked ~ .fs-01__tabs [for="fs-01-t2"]::after,
#fs-01-t3:checked ~ .fs-01__tabs [for="fs-01-t3"]::after,
#fs-01-t4:checked ~ .fs-01__tabs [for="fs-01-t4"]::after,
#fs-01-t5:checked ~ .fs-01__tabs [for="fs-01-t5"]::after {
  transform: scaleX(1);
}

.fs-01__radio:focus-visible ~ .fs-01__tabs label[aria-selected="true"],
.fs-01__tab:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.fs-01__panels {
  min-block-size: var(--panel-min);
}

.fs-01__panel {
  display: none;
}

#fs-01-t1:checked ~ .fs-01__panels [data-tab="1"],
#fs-01-t2:checked ~ .fs-01__panels [data-tab="2"],
#fs-01-t3:checked ~ .fs-01__panels [data-tab="3"],
#fs-01-t4:checked ~ .fs-01__panels [data-tab="4"],
#fs-01-t5:checked ~ .fs-01__panels [data-tab="5"] {
  display: grid;
  grid-template-columns: minmax(0, 1.25fr) minmax(0, 1fr);
  gap: clamp(20px, 4vw, 40px);
}

.fs-01__shot {
  min-inline-size: 0;
  background: var(--s1);
  border: 1px solid var(--rule);
  border-radius: 12px;
  padding: 12px;
}

.fs-01__shotbar {
  display: flex;
  gap: 6px;
  margin: 0 0 12px;
}

.fs-01__shotbar span {
  inline-size: 9px;
  block-size: 9px;
  border-radius: 50%;
  background: var(--s3);
}

.fs-01__shotgrid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 120px), 1fr));
  gap: 8px;
}

.fs-01__tile {
  min-inline-size: 0;
  padding: 12px;
  background: var(--s2);
  border-radius: 9px;
  border: 1px solid var(--rule);
}

.fs-01__tile--wide {
  grid-column: span 2;
}

.fs-01__tile b {
  display: block;
  margin: 0 0 10px;
  font-size: 11.5px;
  font-weight: 600;
  color: var(--ink);
}

.fs-01__tile i {
  display: block;
  block-size: 6px;
  margin-block-start: 6px;
  border-radius: 3px;
  background: var(--s3);
}

.fs-01__tile i:first-of-type {
  background: color-mix(in oklab, var(--accent) 55%, var(--s3));
}

.fs-01__chart {
  display: flex;
  align-items: flex-end;
  gap: 6px;
  block-size: 190px;
  padding: 10px;
  background: var(--s2);
  border-radius: 9px;
}

.fs-01__chart div {
  flex: 1;
  min-inline-size: 0;
  border-radius: 4px 4px 2px 2px;
  background: linear-gradient(180deg, var(--accent), color-mix(in oklab, var(--accent) 25%, var(--s2)));
}

.fs-01__shotcap {
  margin: 10px 2px 0;
  font-size: 11px;
  color: var(--muted);
}

.fs-01__flow {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 8px;
  padding: 24px 12px;
  background: var(--s2);
  border-radius: 9px;
  min-block-size: 190px;
}

.fs-01__node {
  padding: 10px 13px;
  font-size: 12px;
  font-weight: 600;
  border: 1px solid var(--rule);
  border-radius: 8px;
  background: var(--s1);
}

.fs-01__node--on {
  border-color: var(--accent);
  color: var(--accent);
}

.fs-01__wire {
  flex: 1 1 22px;
  min-inline-size: 18px;
  block-size: 1px;
  background: var(--rule);
}

.fs-01__copy {
  min-inline-size: 0;
}

.fs-01__ptitle {
  margin: 0 0 16px;
  font: 600 clamp(18px, 2.6vw, 23px)/1.25 var(--font-display);
  letter-spacing: -0.02em;
}

.fs-01__list {
  margin: 0 0 22px;
  padding: 0;
  list-style: none;
  display: grid;
  gap: 12px;
}

.fs-01__list li {
  position: relative;
  padding-inline-start: 24px;
  font-size: 14px;
  line-height: 1.6;
  color: var(--muted);
  min-inline-size: 0;
  text-wrap: pretty;
}

.fs-01__list li::before {
  content: "";
  position: absolute;
  inset-inline-start: 0;
  inset-block-start: 7px;
  inline-size: 12px;
  block-size: 7px;
  border-inline-start: 2px solid var(--accent);
  border-block-end: 2px solid var(--accent);
  transform: rotate(-45deg);
}

.fs-01__cta {
  display: inline-flex;
  align-items: center;
  min-height: 44px;
  padding: 0 18px;
  font: 600 13px/1 var(--font-display);
  color: var(--s0);
  background: var(--accent);
  border-radius: 8px;
  text-decoration: none;
}

.fs-01__cta:hover {
  background: color-mix(in oklab, var(--accent) 82%, white);
}

.fs-01__cta:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.fs-01__below {
  display: flex;
  flex-wrap: wrap;
  gap: 10px 18px;
  justify-content: space-between;
  padding: 16px 20px;
  border-block-start: 1px solid var(--rule);
  background: var(--s1);
  font-size: 12px;
  color: var(--muted);
}

@media (max-width: 760px) {
  #fs-01-t1:checked ~ .fs-01__panels [data-tab="1"],
    #fs-01-t2:checked ~ .fs-01__panels [data-tab="2"],
    #fs-01-t3:checked ~ .fs-01__panels [data-tab="3"],
    #fs-01-t4:checked ~ .fs-01__panels [data-tab="4"],
    #fs-01-t5:checked ~ .fs-01__panels [data-tab="5"] {
    grid-template-columns: minmax(0, 1fr);
  }

  .fs-01__panels {
    min-block-size: 0;
  }

  .fs-01__tab {
    flex: 0 0 auto;
  }
}

@media (prefers-reduced-motion: reduce) {
  .fs-01__tab,
    .fs-01__tab::after {
    transition: none;
  }
}

@media (prefers-color-scheme: light) {
  .fs-01 {
    --s0: #f6f8fc;
    --s1: #ffffff;
    --s2: #eef2f9;
    --s3: #dde5f1;
    --ink: #0d1526;
    --muted: #5b6a85;
    --rule: #dbe3ef;
    --accent: #0e7c86;
  }

  .fs-01__cta {
    color: #ffffff;
  }

  .fs-01__tile i:first-of-type {
    background: color-mix(in oklab, var(--accent) 35%, var(--s3));
  }
}

[data-theme="dark"] .fs-01 {
  --s0: #070d18;
  --s1: #0d1526;
  --s2: #14203a;
  --s3: #1d2c4c;
  --ink: #eef3fb;
  --muted: #9aabc6;
  --rule: #223354;
  --accent: #3ddbe0;
}

[data-theme="dark"] .fs-01 .fs-01__cta {
  color: #070d18;
}
```

## JavaScript
```js
const tour = document.querySelector('.fs-01__tour');
if (tour) {
  const radios = [...tour.querySelectorAll('.fs-01__radio')];
  const labels = [...tour.querySelectorAll('.fs-01__tab')];
  const sync = () => labels.forEach((l, i) => l.setAttribute('aria-selected', String(radios[i].checked)));
  const move = (i) => { const n = (i + radios.length) % radios.length; radios[n].checked = true; radios[n].focus(); sync(); };
  radios.forEach((r) => r.addEventListener('change', sync));
  tour.addEventListener('keydown', (e) => {
    const i = radios.findIndex((r) => r === document.activeElement);
    if (i < 0) return;
    const keys = { ArrowRight: i + 1, ArrowLeft: i - 1, Home: 0, End: radios.length - 1 };
    if (!(e.key in keys)) return;
    e.preventDefault();
    move(keys[e.key]);
  });
  sync();
}
```
