---
source: "codefronts"
url: "https://codefronts.com/layouts/css-feature-sections/sticky-scroll-storytelling-feature-section/"
title: "Sticky Scroll Storytelling Feature Section"
section: "layouts"
category: "css-feature-sections"
category_name: "CSS Feature Sections"
description: "A four-step product story: the copy scrolls, the mockup beside it pins and swaps state as each step takes focus."
has_js: "false"
---

Here's a working CSS Feature Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sticky Scroll Storytelling Feature Section
Source: https://codefronts.com/layouts/css-feature-sections/sticky-scroll-storytelling-feature-section/

A four-step product story: the copy scrolls, the mockup beside it pins and swaps state as each step takes focus. Every step owns its own sticky media, so the swap is layout rather than script, and a view() timeline crossfades the pinned panel in and out. Where scroll-driven animations are missing, each step simply shows its own static mockup.
## HTML
```html
<section class="fs-12" aria-labelledby="fs-12-heading">
  <div class="fs-12__hero" aria-hidden="true">
    <span class="fs-12__wordmark">Nova</span>
    <span class="fs-12__heronav">How a release moves through Nova</span>
  </div>

  <div class="fs-12__stage">
    <div class="fs-12__head">
      <p class="fs-12__eyebrow">The path of a change</p>
      <h2 class="fs-12__heading" id="fs-12-heading">From branch to production, one scroll at a time</h2>
      <p class="fs-12__sub">Four steps. The panel on the right keeps up as you read.</p>
    </div>

    <div class="fs-12__story">
      <div class="fs-12__step">
        <div class="fs-12__text">
          <p class="fs-12__num">01</p>
          <h3 class="fs-12__stitle">Open the branch, get an environment</h3>
          <p class="fs-12__prose">Every branch gets a full preview stack with seeded data and its own subdomain. Reviewers click a link instead of pulling your code and guessing at the migration order.</p>
          <ul class="fs-12__bullets"><li>Seeded from a sanitised snapshot</li><li>Torn down on merge</li></ul>
        </div>
        <div class="fs-12__mediacell">
          <div class="fs-12__panel">
            <div class="fs-12__ptop"><span class="fs-12__pdot"></span>preview · feat/checkout-retry</div>
            <div class="fs-12__prow"><b>Environment</b><i>ready in 38s</i></div>
            <div class="fs-12__bar" style="--w:100%"></div>
            <div class="fs-12__prow"><b>Seed data</b><i>2.1M rows</i></div>
            <div class="fs-12__bar" style="--w:82%"></div>
            <div class="fs-12__prow"><b>Migrations</b><i>4 applied</i></div>
            <div class="fs-12__bar" style="--w:66%"></div>
          </div>
        </div>
      </div>

      <div class="fs-12__step">
        <div class="fs-12__text">
          <p class="fs-12__num">02</p>
          <h3 class="fs-12__stitle">Checks that read like a review, not a log</h3>
          <p class="fs-12__prose">Tests, type checks and a visual diff report as one status with a plain-language summary. A failing check names the file and the assertion, not a job id.</p>
          <ul class="fs-12__bullets"><li>Flake detection over the last 200 runs</li><li>Visual diff per component</li></ul>
        </div>
        <div class="fs-12__mediacell">
          <div class="fs-12__panel">
            <div class="fs-12__ptop"><span class="fs-12__pdot"></span>checks · 12 of 12</div>
            <ul class="fs-12__checks">
              <li><span>✓</span>unit · 1,842 passed</li>
              <li><span>✓</span>types · no errors</li>
              <li><span>✓</span>visual · 3 diffs approved</li>
              <li><span>✓</span>contract · schema compatible</li>
              <li><span>✓</span>a11y · 0 violations</li>
            </ul>
          </div>
        </div>
      </div>

      <div class="fs-12__step">
        <div class="fs-12__text">
          <p class="fs-12__num">03</p>
          <h3 class="fs-12__stitle">Ship to a slice before shipping to everyone</h3>
          <p class="fs-12__prose">Roll out by percentage, region or account tier. Nova watches error rate and latency against the baseline and holds the rollout if either drifts past your threshold.</p>
          <ul class="fs-12__bullets"><li>Automatic hold on regression</li><li>Per-tier targeting</li></ul>
        </div>
        <div class="fs-12__mediacell">
          <div class="fs-12__panel">
            <div class="fs-12__ptop"><span class="fs-12__pdot"></span>rollout · 25% · holding</div>
            <div class="fs-12__gauge"><i style="--w:25%"></i></div>
            <div class="fs-12__prow"><b>Error rate</b><i>0.04% · baseline 0.05%</i></div>
            <div class="fs-12__prow"><b>P95 latency</b><i>212ms · baseline 205ms</i></div>
            <div class="fs-12__prow"><b>Next gate</b><i>50% in 20m</i></div>
          </div>
        </div>
      </div>

      <div class="fs-12__step">
        <div class="fs-12__text">
          <p class="fs-12__num">04</p>
          <h3 class="fs-12__stitle">Roll back in one action, with the reason attached</h3>
          <p class="fs-12__prose">A rollback reverts the release and files the incident with the metric that triggered it, the diff and the owner. The postmortem starts already written.</p>
          <ul class="fs-12__bullets"><li>One-action revert, under 30 seconds</li><li>Incident drafted from the trigger</li></ul>
        </div>
        <div class="fs-12__mediacell">
          <div class="fs-12__panel">
            <div class="fs-12__ptop"><span class="fs-12__pdot"></span>incident · INC-204 · resolved</div>
            <div class="fs-12__prow"><b>Trigger</b><i>P95 latency +38%</i></div>
            <div class="fs-12__prow"><b>Reverted</b><i>28s after gate</i></div>
            <div class="fs-12__prow"><b>Owner</b><i>Jordan Lee</i></div>
            <div class="fs-12__bar" style="--w:100%"></div>
            <div class="fs-12__prow"><b>Customer impact</b><i>none recorded</i></div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="fs-12__below" aria-hidden="true">Read the deployment docs · See pricing</div>
</section>
```
## CSS
```css
.fs-12 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --page: #f6f7f9;
  --page: oklch(0.972 0.004 250);
  --card: #ffffff;
  --ink: #131720;
  --ink: oklch(0.21 0.014 260);
  --muted: #5c6577;
  --muted: oklch(0.5 0.021 262);
  --rule: #dfe3ea;
  --rule: oklch(0.9 0.008 255);
  --accent: #2f7ff0;
  --accent: oklch(0.62 0.17 255);
  --pin: 12vh;
  --step-gap: clamp(48px, 9vh, 110px);
  --font-display: "Geist", "Inter Tight", system-ui, -apple-system, sans-serif;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

.fs-12 *,
.fs-12 *::before,
.fs-12 *::after {
  box-sizing: border-box;
}

.fs-12__hero {
  display: flex;
  flex-wrap: wrap;
  gap: 6px 16px;
  justify-content: space-between;
  align-items: baseline;
  padding: 16px 22px;
  background: var(--card);
  border-block-end: 1px solid var(--rule);
}

.fs-12__wordmark {
  font: 700 15px/1 var(--font-display);
  letter-spacing: -0.03em;
}

.fs-12__heronav {
  font-size: 12px;
  color: var(--muted);
}

.fs-12__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  padding: clamp(30px, 5vw, 60px) 18px clamp(40px, 8vw, 90px);
}

.fs-12__head {
  inline-size: 100%;
  max-inline-size: 64rem;
  min-inline-size: 0;
  margin: 0 0 clamp(22px, 4vw, 40px);
}

.fs-12__eyebrow {
  margin: 0 0 12px;
  font: 650 10.5px/1 var(--font-display);
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--accent);
}

.fs-12__heading {
  margin: 0 0 10px;
  max-inline-size: 30ch;
  font: 650 clamp(26px, 4.8vw, 40px)/1.1 var(--font-display);
  letter-spacing: -0.035em;
  text-wrap: balance;
}

.fs-12__sub {
  margin: 0;
  font-size: 14.5px;
  color: var(--muted);
}

.fs-12__story {
  inline-size: 100%;
  max-inline-size: 64rem;
  min-inline-size: 0;
  display: grid;
  gap: var(--step-gap);
}

.fs-12__step {
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(0, 1fr);
  gap: clamp(20px, 4vw, 46px);
  align-items: start;
  min-block-size: 72vh;
}

.fs-12__text {
  min-inline-size: 0;
  position: sticky;
  inset-block-start: var(--pin);
  padding-block-start: 4px;
}

.fs-12__num {
  margin: 0 0 10px;
  font: 650 12px/1 var(--font-display);
  letter-spacing: 0.14em;
  color: var(--accent);
}

.fs-12__stitle {
  margin: 0 0 12px;
  font: 650 clamp(19px, 2.8vw, 26px)/1.2 var(--font-display);
  letter-spacing: -0.025em;
  text-wrap: balance;
}

.fs-12__prose {
  margin: 0 0 16px;
  max-inline-size: 44ch;
  font-size: 14.5px;
  line-height: 1.7;
  color: var(--muted);
  text-wrap: pretty;
}

.fs-12__bullets {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: 8px;
}

.fs-12__bullets li {
  position: relative;
  padding-inline-start: 18px;
  font-size: 13.5px;
  color: var(--muted);
  min-inline-size: 0;
}

.fs-12__bullets li::before {
  content: "";
  position: absolute;
  inset-inline-start: 0;
  inset-block-start: 7px;
  inline-size: 7px;
  block-size: 7px;
  border-radius: 2px;
  background: var(--accent);
}

.fs-12__mediacell {
  min-inline-size: 0;
}

.fs-12__panel {
  position: sticky;
  inset-block-start: var(--pin);
  min-inline-size: 0;
  padding: 16px;
  background: var(--card);
  border: 1px solid var(--rule);
  border-radius: 14px;
  box-shadow: 0 14px 34px -22px rgba(19, 23, 32, 0.35);
}

.fs-12__ptop {
  display: flex;
  align-items: center;
  gap: 8px;
  margin: 0 0 14px;
  padding-block-end: 12px;
  border-block-end: 1px solid var(--rule);
  font: 600 11.5px/1 var(--font-display);
  letter-spacing: 0.02em;
  color: var(--muted);
}

.fs-12__pdot {
  inline-size: 8px;
  block-size: 8px;
  border-radius: 50%;
  background: var(--accent);
  flex: none;
}

.fs-12__prow {
  display: flex;
  flex-wrap: wrap;
  gap: 4px 10px;
  justify-content: space-between;
  padding: 8px 0;
  font-size: 12.5px;
  min-inline-size: 0;
}

.fs-12__prow b {
  font-weight: 600;
}

.fs-12__prow i {
  font-style: normal;
  color: var(--muted);
}

.fs-12__bar {
  block-size: 6px;
  margin: 2px 0 6px;
  border-radius: 3px;
  background: color-mix(in oklab, var(--accent) 15%, var(--page));
  overflow: hidden;
}

.fs-12__bar::after {
  content: "";
  display: block;
  inline-size: var(--w, 50%);
  block-size: 100%;
  border-radius: 3px;
  background: var(--accent);
}

.fs-12__checks {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: 9px;
}

.fs-12__checks li {
  display: grid;
  grid-template-columns: 20px minmax(0, 1fr);
  gap: 8px;
  align-items: center;
  font-size: 12.5px;
  color: var(--muted);
}

.fs-12__checks span {
  display: grid;
  place-items: center;
  inline-size: 20px;
  block-size: 20px;
  border-radius: 50%;
  font-size: 11px;
  font-weight: 700;
  color: #fff;
  background: var(--accent);
}

.fs-12__gauge {
  block-size: 10px;
  margin: 0 0 14px;
  border-radius: 5px;
  background: color-mix(in oklab, var(--accent) 14%, var(--page));
  overflow: hidden;
}

.fs-12__gauge i {
  display: block;
  inline-size: var(--w, 25%);
  block-size: 100%;
  background: var(--accent);
}

.fs-12__below {
  padding: 16px 22px;
  background: var(--card);
  border-block-start: 1px solid var(--rule);
  font-size: 12px;
  color: var(--muted);
}

@supports (animation-timeline: view()) {
  .fs-12__panel {
    animation: fs-12-in linear both;
    animation-timeline: view();
    animation-range: entry 10% cover 34%;
  }

  @keyframes fs-12-in {
    from {
      opacity: 0;
      transform: translateY(24px) scale(0.985);
    }

    to {
      opacity: 1;
      transform: none;
    }
  }
}

@media (max-width: 820px) {
  .fs-12__step {
    grid-template-columns: minmax(0, 1fr);
    min-block-size: 0;
  }

  .fs-12__text {
    position: static;
  }

  .fs-12__panel {
    position: static;
  }
}

@media (prefers-reduced-motion: reduce) {
  .fs-12__panel {
    animation: none;
    opacity: 1;
    transform: none;
  }
}

@media (prefers-color-scheme: dark) {
  .fs-12 {
    --page: #0f1218;
    --card: #161b24;
    --ink: #eef1f6;
    --muted: #98a2b5;
    --rule: #262d38;
    --accent: #5c9bff;
  }

  .fs-12__panel {
    box-shadow: 0 14px 34px -22px rgba(0, 0, 0, 0.7);
  }

  .fs-12__checks span {
    color: #0f1218;
  }
}

[data-theme="dark"] .fs-12 {
  --page: #0f1218;
  --card: #161b24;
  --ink: #eef1f6;
  --muted: #98a2b5;
  --rule: #262d38;
  --accent: #5c9bff;
}

[data-theme="dark"] .fs-12 .fs-12__checks span {
  color: #0f1218;
}
```
