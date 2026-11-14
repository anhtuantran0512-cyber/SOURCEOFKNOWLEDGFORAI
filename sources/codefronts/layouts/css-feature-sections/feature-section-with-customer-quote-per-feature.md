---
source: "codefronts"
url: "https://codefronts.com/layouts/css-feature-sections/feature-section-with-customer-quote-per-feature/"
title: "Feature Section with Customer Quote per Feature"
section: "layouts"
category: "css-feature-sections"
category_name: "CSS Feature Sections"
description: "Four feature rows where each claim is answered immediately by a customer saying it worked — feature copy on one side, a pull-quote with avatar, name and role…"
has_js: "false"
---

Here's a working CSS Feature Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Feature Section with Customer Quote per Feature
Source: https://codefronts.com/layouts/css-feature-sections/feature-section-with-customer-quote-per-feature/

Four feature rows where each claim is answered immediately by a customer saying it worked — feature copy on one side, a pull-quote with avatar, name and role on the other. Built as real blockquote and cite markup on an editorial off-white ground with a serif display face, no cards and no shadows, so the quotes read as testimony rather than as widgets.
## HTML
```html
<section class="fs-11" aria-labelledby="fs-11-heading">
  <div class="fs-11__hero" aria-hidden="true">
    <span class="fs-11__wordmark">Aperture</span>
    <span class="fs-11__heronav">Research operations, end to end</span>
  </div>

  <div class="fs-11__stage">
    <div class="fs-11__head">
      <p class="fs-11__eyebrow">Proof, per feature</p>
      <h2 class="fs-11__heading" id="fs-11-heading">Four claims, and the customers who tested them</h2>
    </div>

    <div class="fs-11__rows">
      <div class="fs-11__row">
        <article class="fs-11__feature">
          <h3 class="fs-11__ftitle">Recruit participants without a spreadsheet</h3>
          <p class="fs-11__fprose">Screeners, scheduling and incentives live in one record per participant. Consent expiry is tracked automatically, so a panel does not quietly go stale between studies.</p>
        </article>
        <blockquote class="fs-11__quote">
          <p class="fs-11__qtext">We cut recruiting from nine days to two, and I stopped being the bottleneck for every study.</p>
          <footer class="fs-11__attrib">
            <span class="fs-11__avatar" aria-hidden="true">AC</span>
            <span class="fs-11__who"><b>Alex Chen</b><span>Research Lead, Sable</span></span>
          </footer>
        </blockquote>
      </div>

      <div class="fs-11__row">
        <article class="fs-11__feature">
          <h3 class="fs-11__ftitle">Transcripts that are searchable across studies</h3>
          <p class="fs-11__fprose">Every session is transcribed, speaker-labelled and indexed with the study it belongs to. Search once and get the four interviews where anyone mentioned pricing.</p>
        </article>
        <blockquote class="fs-11__quote">
          <p class="fs-11__qtext">A designer found six months of pricing objections in an afternoon. That used to be a whole project.</p>
          <footer class="fs-11__attrib">
            <span class="fs-11__avatar" aria-hidden="true">PS</span>
            <span class="fs-11__who"><b>Priya Sharma</b><span>Head of Design, Meridian</span></span>
          </footer>
        </blockquote>
      </div>

      <div class="fs-11__row">
        <article class="fs-11__feature">
          <h3 class="fs-11__ftitle">Findings that ship as a link, not a deck</h3>
          <p class="fs-11__fprose">Clip a moment, attach it to a finding, and the finding keeps the evidence with it. Product managers get the timestamped clip instead of your summary of it.</p>
        </article>
        <blockquote class="fs-11__quote">
          <p class="fs-11__qtext">Nobody asks me to make slides any more. They watch the ninety-second clip and argue about the fix instead.</p>
          <footer class="fs-11__attrib">
            <span class="fs-11__avatar" aria-hidden="true">JL</span>
            <span class="fs-11__who"><b>Jordan Lee</b><span>Staff Researcher, Orbit</span></span>
          </footer>
        </blockquote>
      </div>

      <div class="fs-11__row">
        <article class="fs-11__feature">
          <h3 class="fs-11__ftitle">Governance the legal team signs off once</h3>
          <p class="fs-11__fprose">Regional data residency, per-study retention windows and revocable consent, with an export of everything a participant asked to be forgotten.</p>
        </article>
        <blockquote class="fs-11__quote">
          <p class="fs-11__qtext">Our privacy review took four days. The previous tool took a quarter and we still shipped with caveats.</p>
          <footer class="fs-11__attrib">
            <span class="fs-11__avatar" aria-hidden="true">SR</span>
            <span class="fs-11__who"><b>Sam Rivera</b><span>Ops Manager, Vale</span></span>
          </footer>
        </blockquote>
      </div>
    </div>
  </div>

  <div class="fs-11__below" aria-hidden="true">More customer stories · Plans</div>
</section>
```
## CSS
```css
.fs-11 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --paper: #f7f6f2;
  --paper: oklch(0.972 0.005 95);
  --ink: #16171b;
  --ink: oklch(0.2 0.008 265);
  --muted: #55575f;
  --muted: oklch(0.46 0.011 265);
  --rule: #dedcd4;
  --rule: oklch(0.89 0.008 95);
  --accent: #33418c;
  --accent: oklch(0.4 0.13 272);
  --rowpad: clamp(28px, 4.5vw, 52px);
  --font-display: Georgia, "Iowan Old Style", "Times New Roman", serif;
  background: var(--paper);
  color: var(--ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

.fs-11 *,
.fs-11 *::before,
.fs-11 *::after {
  box-sizing: border-box;
}

.fs-11__hero {
  display: flex;
  flex-wrap: wrap;
  gap: 6px 16px;
  justify-content: space-between;
  align-items: baseline;
  padding: 20px 24px;
  border-block-end: 1px solid var(--rule);
}

.fs-11__wordmark {
  font: 400 20px/1 var(--font-display);
  letter-spacing: -0.01em;
}

.fs-11__heronav {
  font-size: 12.5px;
  color: var(--muted);
}

.fs-11__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  padding: clamp(32px, 6vw, 72px) 20px;
}

.fs-11__head {
  inline-size: 100%;
  max-inline-size: 62rem;
  min-inline-size: 0;
  margin: 0 0 clamp(20px, 3vw, 34px);
}

.fs-11__eyebrow {
  margin: 0 0 14px;
  font: 700 10.5px/1 system-ui, sans-serif;
  letter-spacing: 0.26em;
  text-transform: uppercase;
  color: var(--accent);
}

.fs-11__heading {
  margin: 0;
  max-inline-size: 26ch;
  font: 400 clamp(28px, 5.4vw, 46px)/1.1 var(--font-display);
  letter-spacing: -0.015em;
  text-wrap: balance;
}

.fs-11__rows {
  inline-size: 100%;
  max-inline-size: 62rem;
  min-inline-size: 0;
}

.fs-11__row {
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(0, 0.9fr);
  gap: clamp(20px, 4vw, 48px);
  align-items: start;
  padding-block: var(--rowpad);
  border-block-start: 1px solid var(--rule);
}

.fs-11__row:last-child {
  border-block-end: 1px solid var(--rule);
}

.fs-11__feature {
  min-inline-size: 0;
}

.fs-11__ftitle {
  margin: 0 0 12px;
  font: 400 clamp(20px, 2.8vw, 27px)/1.2 var(--font-display);
  letter-spacing: -0.01em;
  text-wrap: balance;
}

.fs-11__fprose {
  margin: 0;
  max-inline-size: 44ch;
  font-size: 15px;
  line-height: 1.75;
  color: var(--muted);
  text-wrap: pretty;
}

.fs-11__quote {
  position: relative;
  margin: 0;
  min-inline-size: 0;
  padding-inline-start: 30px;
}

.fs-11__quote::before {
  content: "\201C";
  position: absolute;
  inset-inline-start: -6px;
  inset-block-start: -14px;
  font: 400 62px/1 var(--font-display);
  color: color-mix(in oklab, var(--accent) 35%, var(--paper));
}

.fs-11__qtext {
  margin: 0 0 16px;
  font: 400 clamp(16px, 2.2vw, 20px)/1.55 var(--font-display);
  font-style: italic;
  letter-spacing: -0.005em;
  text-wrap: pretty;
}

.fs-11__attrib {
  display: flex;
  align-items: center;
  gap: 12px;
  min-inline-size: 0;
}

.fs-11__avatar {
  display: grid;
  place-items: center;
  flex: none;
  inline-size: 42px;
  block-size: 42px;
  border-radius: 50%;
  font: 700 13px/1 system-ui, sans-serif;
  letter-spacing: 0.04em;
  color: var(--accent);
  background: color-mix(in oklab, var(--accent) 14%, var(--paper));
  box-shadow: inset 0 0 0 1px color-mix(in oklab, var(--accent) 30%, transparent);
}

.fs-11__who {
  display: grid;
  gap: 1px;
  min-inline-size: 0;
}

.fs-11__who b {
  font-size: 13.5px;
  font-weight: 650;
}

.fs-11__who span {
  font-size: 12.5px;
  color: var(--muted);
}

.fs-11__below {
  padding: 18px 24px;
  border-block-start: 1px solid var(--rule);
  font-size: 12.5px;
  color: var(--muted);
}

@media (max-width: 780px) {
  .fs-11__row {
    grid-template-columns: minmax(0, 1fr);
  }
}

@media (prefers-color-scheme: dark) {
  .fs-11 {
    --paper: #14151a;
    --ink: #f1f1ee;
    --muted: #a2a3ac;
    --rule: #282a31;
    --accent: #a5b0ef;
  }
}

[data-theme="dark"] .fs-11 {
  --paper: #14151a;
  --ink: #f1f1ee;
  --muted: #a2a3ac;
  --rule: #282a31;
  --accent: #a5b0ef;
}
```
