---
source: "codefronts"
url: "https://codefronts.com/layouts/css-feature-sections/expandable-accordion-feature-cards-section/"
title: "Expandable Accordion Feature Cards Section"
section: "layouts"
category: "css-feature-sections"
category_name: "CSS Feature Sections"
description: "Five feature cards stacked vertically, each a native details element that opens to a fuller description, a benefit list and a docs link."
has_js: "false"
---

Here's a working CSS Feature Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Expandable Accordion Feature Cards Section
Source: https://codefronts.com/layouts/css-feature-sections/expandable-accordion-feature-cards-section/

Five feature cards stacked vertically, each a native details element that opens to a fuller description, a benefit list and a docs link. A shared name attribute makes the group exclusive — opening one closes the last — so the whole accordion behaves like a real disclosure widget with keyboard support, focus handling and zero JavaScript.
## HTML
```html
<section class="fs-07" aria-labelledby="fs-07-heading">
  <div class="fs-07__hero" aria-hidden="true">
    <span class="fs-07__wordmark">Fern</span>
    <span class="fs-07__heronav">Field guide to the platform</span>
  </div>

  <div class="fs-07__stage">
    <div class="fs-07__head">
      <p class="fs-07__eyebrow">Capabilities</p>
      <h2 class="fs-07__heading" id="fs-07-heading">Open the one you came for</h2>
      <p class="fs-07__sub">Five capabilities, each with the detail your engineers will ask about second.</p>
    </div>

    <div class="fs-07__list">
      <details class="fs-07__card" name="fs-07" open>
        <summary class="fs-07__summary">
          <span class="fs-07__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="19" height="19" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M4 7h16M4 12h10M4 17h13"/></svg></span>
          <span class="fs-07__stitle">Typed API generation from your schema</span>
          <span class="fs-07__chev" aria-hidden="true"><svg viewBox="0 0 16 16" width="15" height="15" fill="none" stroke="currentColor" stroke-width="1.9"><path d="M6 3.5 10.5 8 6 12.5"/></svg></span>
        </summary>
        <div class="fs-07__panel">
          <p class="fs-07__prose">Point Fern at a schema and it emits a typed client for TypeScript, Python, Go and Kotlin, versioned alongside your API. Breaking changes fail the build before they reach a consumer, and every generated method carries the docstring from the schema description.</p>
          <ul class="fs-07__benefits">
            <li>Four target languages from one source of truth</li>
            <li>Breaking-change detection in CI, not in production</li>
            <li>Docstrings and examples generated with the client</li>
          </ul>
          <a class="fs-07__link" href="#fs-07-heading">Read the generation docs</a>
        </div>
      </details>

      <details class="fs-07__card" name="fs-07">
        <summary class="fs-07__summary">
          <span class="fs-07__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="19" height="19" fill="none" stroke="currentColor" stroke-width="1.7"><circle cx="12" cy="12" r="8"/><path d="M12 8v4l3 2"/></svg></span>
          <span class="fs-07__stitle">Edge caching with per-tenant invalidation</span>
          <span class="fs-07__chev" aria-hidden="true"><svg viewBox="0 0 16 16" width="15" height="15" fill="none" stroke="currentColor" stroke-width="1.9"><path d="M6 3.5 10.5 8 6 12.5"/></svg></span>
        </summary>
        <div class="fs-07__panel">
          <p class="fs-07__prose">Responses are cached at 310 locations and tagged by tenant, so a single customer's write invalidates only their keys. Cold-start reads settle at 40ms in region and 90ms at the far edge, with a stale-while-revalidate window you set per route.</p>
          <ul class="fs-07__benefits">
            <li>Tag-based invalidation, no global purge</li>
            <li>Per-route stale-while-revalidate windows</li>
            <li>Cache hit ratio exposed per tenant in the dashboard</li>
          </ul>
          <a class="fs-07__link" href="#fs-07-heading">See the caching reference</a>
        </div>
      </details>

      <details class="fs-07__card" name="fs-07">
        <summary class="fs-07__summary">
          <span class="fs-07__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="19" height="19" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M12 3l8 4v6c0 4-3.5 7-8 8-4.5-1-8-4-8-8V7z"/></svg></span>
          <span class="fs-07__stitle">Native SSO with SCIM provisioning</span>
          <span class="fs-07__chev" aria-hidden="true"><svg viewBox="0 0 16 16" width="15" height="15" fill="none" stroke="currentColor" stroke-width="1.9"><path d="M6 3.5 10.5 8 6 12.5"/></svg></span>
        </summary>
        <div class="fs-07__panel">
          <p class="fs-07__prose">SAML 2.0 and OIDC on every plan, with SCIM 2.0 for joiners and leavers. Group membership maps to roles you define, so an offboarded engineer loses access the moment the directory updates rather than at the next audit.</p>
          <ul class="fs-07__benefits">
            <li>SAML 2.0 and OIDC, no enterprise upsell</li>
            <li>SCIM group-to-role mapping you control</li>
            <li>Session revocation propagates in under a minute</li>
          </ul>
          <a class="fs-07__link" href="#fs-07-heading">Identity provider setup</a>
        </div>
      </details>

      <details class="fs-07__card" name="fs-07">
        <summary class="fs-07__summary">
          <span class="fs-07__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="19" height="19" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M5 19V9M12 19V5M19 19v-7"/></svg></span>
          <span class="fs-07__stitle">Usage metering you can bill against</span>
          <span class="fs-07__chev" aria-hidden="true"><svg viewBox="0 0 16 16" width="15" height="15" fill="none" stroke="currentColor" stroke-width="1.9"><path d="M6 3.5 10.5 8 6 12.5"/></svg></span>
        </summary>
        <div class="fs-07__panel">
          <p class="fs-07__prose">Every request is metered with an idempotency key and exposed as an hourly rollup, so your finance team reconciles against the same numbers your customers see. Exports land in the warehouse before the invoice run.</p>
          <ul class="fs-07__benefits">
            <li>Hourly rollups with idempotent event keys</li>
            <li>Warehouse export ahead of the billing cycle</li>
            <li>Customer-visible usage matches your invoice</li>
          </ul>
          <a class="fs-07__link" href="#fs-07-heading">Metering and billing guide</a>
        </div>
      </details>

      <details class="fs-07__card" name="fs-07">
        <summary class="fs-07__summary">
          <span class="fs-07__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="19" height="19" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M4 6h16v12H4z"/><path d="M8 10h8M8 14h5"/></svg></span>
          <span class="fs-07__stitle">Audit logs that answer a compliance question</span>
          <span class="fs-07__chev" aria-hidden="true"><svg viewBox="0 0 16 16" width="15" height="15" fill="none" stroke="currentColor" stroke-width="1.9"><path d="M6 3.5 10.5 8 6 12.5"/></svg></span>
        </summary>
        <div class="fs-07__panel">
          <p class="fs-07__prose">Immutable, queryable and streamable to your SIEM. Each entry keeps actor, resource, before and after state, and the API token used — including when that token was rotated mid-session, which is where most audit trails lose the thread.</p>
          <ul class="fs-07__benefits">
            <li>Before and after state on every mutation</li>
            <li>Actor preserved across token rotation</li>
            <li>Streams to Splunk, Datadog or an S3 bucket</li>
          </ul>
          <a class="fs-07__link" href="#fs-07-heading">Audit log schema</a>
        </div>
      </details>
    </div>
  </div>

  <div class="fs-07__below" aria-hidden="true">Compare plans · Book a technical review</div>
</section>
```
## CSS
```css
.fs-07 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --paper: #f4f2e9;
  --paper: oklch(0.96 0.017 105);
  --card: #fbfaf5;
  --ink: #1e2a22;
  --ink: oklch(0.26 0.021 155);
  --muted: #5f6b61;
  --muted: oklch(0.51 0.017 155);
  --rule: #d8d9cb;
  --rule: oklch(0.87 0.015 115);
  --accent: #4a7c59;
  --accent: oklch(0.54 0.078 152);
  --pad: 26px;
  --font-display: "Optima", "Palatino Linotype", "Segoe UI", system-ui, sans-serif;
  background: var(--paper);
  color: var(--ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

.fs-07 *,
.fs-07 *::before,
.fs-07 *::after {
  box-sizing: border-box;
}

.fs-07__hero {
  display: flex;
  flex-wrap: wrap;
  gap: 6px 16px;
  justify-content: space-between;
  align-items: baseline;
  padding: 20px 24px;
}

.fs-07__wordmark {
  font: 600 19px/1 var(--font-display);
  letter-spacing: 0.01em;
}

.fs-07__heronav {
  font-size: 12.5px;
  color: var(--muted);
  font-style: italic;
}

.fs-07__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  padding: clamp(30px, 6vw, 70px) 20px;
}

.fs-07__head {
  inline-size: 100%;
  max-inline-size: 52rem;
  min-inline-size: 0;
  margin: 0 0 clamp(26px, 4vw, 44px);
}

.fs-07__eyebrow {
  margin: 0 0 14px;
  font: 600 11px/1 system-ui, sans-serif;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--accent);
}

.fs-07__heading {
  margin: 0 0 12px;
  font: 500 clamp(28px, 5vw, 44px)/1.1 var(--font-display);
  letter-spacing: -0.01em;
  text-wrap: balance;
}

.fs-07__sub {
  margin: 0;
  max-inline-size: 50ch;
  font-size: 15.5px;
  line-height: 1.7;
  color: var(--muted);
  text-wrap: pretty;
}

.fs-07__list {
  inline-size: 100%;
  max-inline-size: 52rem;
  min-inline-size: 0;
  display: grid;
  gap: 14px;
}

.fs-07__card {
  background: var(--card);
  border-radius: 14px;
  padding: 4px var(--pad);
  border: 1px solid transparent;
}

.fs-07__card[open] {
  border-color: color-mix(in oklab, var(--accent) 28%, var(--rule));
  background: color-mix(in oklab, var(--accent) 4%, var(--card));
}

.fs-07__summary {
  display: grid;
  grid-template-columns: 34px minmax(0, 1fr) 24px;
  align-items: center;
  gap: 14px;
  min-height: 64px;
  padding: 12px 0;
  cursor: pointer;
  list-style: none;
}

.fs-07__summary::-webkit-details-marker {
  display: none;
}

.fs-07__summary::marker {
  content: "";
}

.fs-07__summary:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 4px;
  border-radius: 8px;
}

.fs-07__icon {
  display: grid;
  place-items: center;
  inline-size: 34px;
  block-size: 34px;
  border-radius: 10px;
  color: var(--accent);
  background: color-mix(in oklab, var(--accent) 12%, var(--card));
}

.fs-07__stitle {
  min-inline-size: 0;
  font: 500 clamp(16px, 2.2vw, 19.5px)/1.3 var(--font-display);
  letter-spacing: -0.01em;
  text-wrap: pretty;
}

.fs-07__chev {
  display: grid;
  place-items: center;
  color: var(--muted);
  transition: transform .22s ease;
}

.fs-07__card[open] .fs-07__chev {
  transform: rotate(90deg);
  color: var(--accent);
}

.fs-07__panel {
  padding: 0 0 22px 48px;
}

.fs-07__prose {
  margin: 0 0 16px;
  max-inline-size: 62ch;
  font-size: 14.5px;
  line-height: 1.75;
  color: var(--muted);
  text-wrap: pretty;
}

.fs-07__benefits {
  margin: 0 0 18px;
  padding: 0;
  list-style: none;
  display: grid;
  gap: 9px;
}

.fs-07__benefits li {
  position: relative;
  padding-inline-start: 22px;
  font-size: 14px;
  line-height: 1.55;
  min-inline-size: 0;
}

.fs-07__benefits li::before {
  content: "";
  position: absolute;
  inset-inline-start: 0;
  inset-block-start: 8px;
  inline-size: 8px;
  block-size: 8px;
  border-radius: 50%;
  background: var(--accent);
}

.fs-07__link {
  display: inline-flex;
  align-items: center;
  min-height: 44px;
  font: 600 13.5px/1 system-ui, sans-serif;
  color: var(--accent);
  text-decoration: underline;
  text-underline-offset: 4px;
}

.fs-07__link:hover {
  color: var(--ink);
}

.fs-07__link:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
  border-radius: 4px;
}

.fs-07__below {
  padding: 18px 24px;
  border-block-start: 1px solid var(--rule);
  font-size: 12.5px;
  color: var(--muted);
}

@media (max-width: 520px) {
  .fs-07 {
    --pad: 16px;
  }

  .fs-07__panel {
    padding-inline-start: 0;
  }

  .fs-07__summary {
    grid-template-columns: 30px minmax(0, 1fr) 20px;
    gap: 10px;
  }
}

@supports (interpolate-size: allow-keywords) {
  .fs-07 {
    interpolate-size: allow-keywords;
  }

  .fs-07__card::details-content {
    block-size: 0;
    overflow: hidden;
    transition: block-size .28s ease, content-visibility .28s allow-discrete;
  }

  .fs-07__card[open]::details-content {
    block-size: auto;
  }
}

@media (prefers-reduced-motion: reduce) {
  .fs-07__chev {
    transition: none;
  }

  .fs-07__card::details-content,
    .fs-07__card[open]::details-content {
    transition: none;
  }
}

@media (prefers-color-scheme: dark) {
  .fs-07 {
    --paper: #151a16;
    --card: #1c231d;
    --ink: #eaf0e9;
    --muted: #9fada2;
    --rule: #2b332c;
    --accent: #8fc79f;
  }
}

[data-theme="dark"] .fs-07 {
  --paper: #151a16;
  --card: #1c231d;
  --ink: #eaf0e9;
  --muted: #9fada2;
  --rule: #2b332c;
  --accent: #8fc79f;
}
```
