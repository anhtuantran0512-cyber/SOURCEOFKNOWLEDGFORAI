---
source: "codefronts"
url: "https://codefronts.com/layouts/css-feature-sections/css-feature-section-timeline-layout/"
title: "Feature Section Timeline Layout Vertical"
section: "layouts"
category: "css-feature-sections"
category_name: "CSS Feature Sections"
description: "Six features as milestones on a central rail, alternating left and right, with the rail drawn as a gradient so it fades at both ends instead of stopping…"
has_js: "false"
---

Here's a working CSS Feature Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Feature Section Timeline Layout Vertical
Source: https://codefronts.com/layouts/css-feature-sections/css-feature-section-timeline-layout/

Six features as milestones on a central rail, alternating left and right, with the rail drawn as a gradient so it fades at both ends instead of stopping abruptly. Built on an ordered list because the sequence is the content, and the whole thing collapses to a single left-aligned column on narrow screens without changing the marker positions.
## HTML
```html
<section class="fs-22" aria-labelledby="fs-22-heading">
  <div class="fs-22__hero" aria-hidden="true">
    <span class="fs-22__wordmark">quill/changelog</span>
    <span class="fs-22__heronav">shipped · in progress · planned</span>
  </div>

  <div class="fs-22__stage">
    <div class="fs-22__head">
      <p class="fs-22__eyebrow">Onboarding, in order</p>
      <h2 class="fs-22__heading" id="fs-22-heading">What your first fortnight with Quill looks like</h2>
      <p class="fs-22__sub">Six milestones. Most teams reach the last one inside two weeks.</p>
    </div>

    <ol class="fs-22__timeline">
      <li class="fs-22__item">
        <span class="fs-22__marker" aria-hidden="true"></span>
        <article class="fs-22__card">
          <p class="fs-22__stamp">Day 1</p>
          <h3 class="fs-22__ctitle">Connect your first source</h3>
          <p class="fs-22__cprose">Paste a connection string, pick the schemas you care about, and the first sync completes while you finish the tour.</p>
        </article>
      </li>
      <li class="fs-22__item">
        <span class="fs-22__marker" aria-hidden="true"></span>
        <article class="fs-22__card">
          <p class="fs-22__stamp">Day 2</p>
          <h3 class="fs-22__ctitle">Invite the team, map the roles</h3>
          <p class="fs-22__cprose">Directory groups become Quill roles, so analysts get write access to their own space and nothing else.</p>
        </article>
      </li>
      <li class="fs-22__item">
        <span class="fs-22__marker" aria-hidden="true"></span>
        <article class="fs-22__card">
          <p class="fs-22__stamp">Day 4</p>
          <h3 class="fs-22__ctitle">Set freshness expectations</h3>
          <p class="fs-22__cprose">Declare an SLA per dataset. Breaches page the owner with the last good run attached, not a generic alert.</p>
        </article>
      </li>
      <li class="fs-22__item">
        <span class="fs-22__marker" aria-hidden="true"></span>
        <article class="fs-22__card">
          <p class="fs-22__stamp">Day 7</p>
          <h3 class="fs-22__ctitle">Ship the first automation</h3>
          <p class="fs-22__cprose">Trigger on schema drift or a null spike, dry-run it against last week of real rows, then enable it.</p>
        </article>
      </li>
      <li class="fs-22__item">
        <span class="fs-22__marker" aria-hidden="true"></span>
        <article class="fs-22__card">
          <p class="fs-22__stamp">Day 10</p>
          <h3 class="fs-22__ctitle">Wire the warehouse export</h3>
          <p class="fs-22__cprose">Incremental exports on a schedule, with a manifest your dbt project can depend on safely.</p>
        </article>
      </li>
      <li class="fs-22__item">
        <span class="fs-22__marker" aria-hidden="true"></span>
        <article class="fs-22__card">
          <p class="fs-22__stamp">Day 14</p>
          <h3 class="fs-22__ctitle">Hand over the runbook</h3>
          <p class="fs-22__cprose">Ownership, escalation and retention are documented from your actual configuration — nothing left to write up.</p>
        </article>
      </li>
    </ol>
  </div>

  <div class="fs-22__below" aria-hidden="true">Full changelog · Migration guide</div>
</section>
```
## CSS
```css
.fs-22 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --page: #fbfbfc;
  --page: oklch(0.985 0.002 270);
  --card: #ffffff;
  --ink: #17181d;
  --ink: oklch(0.22 0.007 275);
  --muted: #5c6070;
  --muted: oklch(0.5 0.014 272);
  --rule: #e2e3e9;
  --rule: oklch(0.9 0.005 270);
  --accent: #4b56d9;
  --accent: oklch(0.5 0.19 272);
  --rail: 2px;
  --font-display: "IBM Plex Mono", "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

.fs-22 *,
.fs-22 *::before,
.fs-22 *::after {
  box-sizing: border-box;
}

.fs-22__hero {
  display: flex;
  flex-wrap: wrap;
  gap: 6px 16px;
  justify-content: space-between;
  align-items: baseline;
  padding: 14px 20px;
  background: var(--card);
  border-block-end: 1px solid var(--rule);
  font: 500 12px/1 var(--font-display);
  color: var(--muted);
}

.fs-22__wordmark {
  color: var(--ink);
}

.fs-22__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  padding: clamp(28px, 5vw, 60px) 16px;
}

.fs-22__head {
  inline-size: 100%;
  max-inline-size: 58rem;
  min-inline-size: 0;
  margin: 0 0 clamp(24px, 4vw, 40px);
  text-align: center;
}

.fs-22__eyebrow {
  margin: 0 0 12px;
  font: 500 11px/1 var(--font-display);
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--accent);
}

.fs-22__heading {
  margin: 0 auto 10px;
  max-inline-size: 26ch;
  font: 600 clamp(25px, 4.6vw, 38px)/1.12 system-ui, sans-serif;
  letter-spacing: -0.035em;
  text-wrap: balance;
}

.fs-22__sub {
  margin: 0 auto;
  max-inline-size: 48ch;
  font-size: 14.5px;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.fs-22__timeline {
  position: relative;
  inline-size: 100%;
  max-inline-size: 58rem;
  min-inline-size: 0;
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: 20px;
}

.fs-22__timeline::before {
  content: "";
  position: absolute;
  inset-block: 0;
  inset-inline-start: 50%;
  translate: -50% 0;
  inline-size: var(--rail);
  background: linear-gradient(180deg, transparent, var(--rule) 7%, var(--rule) 93%, transparent);
}

.fs-22__item {
  position: relative;
  display: grid;
  grid-template-columns: minmax(0, 1fr) 46px minmax(0, 1fr);
  align-items: center;
  min-inline-size: 0;
}

.fs-22__item > .fs-22__card {
  grid-column: 1;
  text-align: end;
}

.fs-22__item:nth-child(even) > .fs-22__card {
  grid-column: 3;
  text-align: start;
}

.fs-22__marker {
  grid-column: 2;
  justify-self: center;
  inline-size: 15px;
  block-size: 15px;
  border-radius: 50%;
  background: var(--card);
  border: var(--rail) solid var(--accent);
  box-shadow: 0 0 0 5px color-mix(in oklab, var(--accent) 12%, var(--page));
}

.fs-22__card {
  min-inline-size: 0;
  padding: 16px 18px;
  background: var(--card);
  border: 1px solid var(--rule);
  border-radius: 10px;
}

.fs-22__stamp {
  margin: 0 0 8px;
  font: 500 10.5px/1 var(--font-display);
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--accent);
}

.fs-22__ctitle {
  margin: 0 0 7px;
  font: 600 16px/1.3 system-ui, sans-serif;
  letter-spacing: -0.02em;
  text-wrap: balance;
}

.fs-22__cprose {
  margin: 0;
  font-size: 13.5px;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.fs-22__below {
  padding: 14px 20px;
  background: var(--card);
  border-block-start: 1px solid var(--rule);
  font: 500 11.5px/1 var(--font-display);
  color: var(--muted);
}

@media (max-width: 700px) {
  .fs-22__timeline::before {
    inset-inline-start: 8px;
    translate: 0 0;
  }

  .fs-22__item {
    grid-template-columns: 26px minmax(0, 1fr);
  }

  .fs-22__item > .fs-22__card,
    .fs-22__item:nth-child(even) > .fs-22__card {
    grid-column: 2;
    text-align: start;
  }

  .fs-22__marker {
    grid-column: 1;
    justify-self: start;
    margin-inline-start: 1px;
  }
}

@media (prefers-color-scheme: dark) {
  .fs-22 {
    --page: #0e0f13;
    --card: #16181f;
    --ink: #eeeff4;
    --muted: #979cae;
    --rule: #252833;
    --accent: #8b93ff;
  }
}

[data-theme="dark"] .fs-22 {
  --page: #0e0f13;
  --card: #16181f;
  --ink: #eeeff4;
  --muted: #979cae;
  --rule: #252833;
  --accent: #8b93ff;
}
```
