---
source: "codefronts"
url: "https://codefronts.com/layouts/css-feature-sections/css-feature-section-3d-perspective-cards/"
title: "Feature Section 3D Perspective Cards"
section: "layouts"
category: "css-feature-sections"
category_name: "CSS Feature Sections"
description: "Four feature cards that tilt in 3D on hover and focus, built with perspective and rotate3d on a shared parent so the cards share one vanishing point instead…"
has_js: "false"
---

Here's a working CSS Feature Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Feature Section 3D Perspective Cards
Source: https://codefronts.com/layouts/css-feature-sections/css-feature-section-3d-perspective-cards/

Four feature cards that tilt in 3D on hover and focus, built with perspective and rotate3d on a shared parent so the cards share one vanishing point instead of each having their own. Depth comes from three stacked shadows at increasing blur, and an inner layer lifts on the Z axis so the icon and title separate from the card face rather than moving with it.
## HTML
```html
<section class="fs-20" aria-labelledby="fs-20-heading">
  <div class="fs-20__hero" aria-hidden="true">
    <span class="fs-20__wordmark">SABLE INDUSTRIES</span>
    <span class="fs-20__heronav">Hardware · Firmware · Fleet</span>
  </div>

  <div class="fs-20__stage">
    <div class="fs-20__head">
      <p class="fs-20__eyebrow">Built to be handled</p>
      <h2 class="fs-20__heading" id="fs-20-heading">Four systems, engineered to be boring in the field</h2>
    </div>

    <ul class="fs-20__grid">
      <li class="fs-20__card">
        <div class="fs-20__layer">
          <span class="fs-20__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3" y="6" width="18" height="12" rx="2"/><path d="M7 10h4M7 14h8"/></svg></span>
          <h3 class="fs-20__ctitle">Edge gateway</h3>
        </div>
        <p class="fs-20__cprose">Buffers ninety days of telemetry locally, so a severed uplink costs you nothing but latency.</p>
        <a class="fs-20__link" href="#fs-20-heading">Specification</a>
      </li>
      <li class="fs-20__card">
        <div class="fs-20__layer">
          <span class="fs-20__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="8"/><path d="M12 4v4M12 16v4M4 12h4M16 12h4"/></svg></span>
          <h3 class="fs-20__ctitle">Signed OTA updates</h3>
        </div>
        <p class="fs-20__cprose">Staged rollouts with an A/B partition and automatic rollback on a failed health check.</p>
        <a class="fs-20__link" href="#fs-20-heading">Update protocol</a>
      </li>
      <li class="fs-20__card">
        <div class="fs-20__layer">
          <span class="fs-20__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 20V8l8-4 8 4v12z"/><path d="M9 20v-7h6v7"/></svg></span>
          <h3 class="fs-20__ctitle">Fleet inventory</h3>
        </div>
        <p class="fs-20__cprose">Every unit's firmware, location and warranty state in one queryable record with a history.</p>
        <a class="fs-20__link" href="#fs-20-heading">Data model</a>
      </li>
      <li class="fs-20__card">
        <div class="fs-20__layer">
          <span class="fs-20__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M6 18 12 5l6 13z"/><path d="M9 18h6"/></svg></span>
          <h3 class="fs-20__ctitle">Anomaly alerting</h3>
        </div>
        <p class="fs-20__cprose">Baselines learned per unit, so a drifting sensor pages before it takes a line down.</p>
        <a class="fs-20__link" href="#fs-20-heading">Alert rules</a>
      </li>
    </ul>
  </div>

  <div class="fs-20__below" aria-hidden="true">Datasheets · Certifications · Contact</div>
</section>
```
## CSS
```css
.fs-20 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --page: #21232a;
  --page: oklch(0.27 0.008 275);
  --card: #2c2f38;
  --card: oklch(0.33 0.009 275);
  --ink: #f2f3f5;
  --muted: #a7abb6;
  --muted: oklch(0.74 0.009 275);
  --rule: #3c404c;
  --rule: oklch(0.4 0.011 275);
  --accent: #3fd28b;
  --accent: oklch(0.79 0.15 158);
  --shadow-ink: rgba(0, 0, 0, 0.5);
  --tilt: 6deg;
  --font-display: "Helvetica Neue", "Inter Tight", system-ui, -apple-system, sans-serif;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

.fs-20 *,
.fs-20 *::before,
.fs-20 *::after {
  box-sizing: border-box;
}

.fs-20__hero {
  display: flex;
  flex-wrap: wrap;
  gap: 6px 16px;
  justify-content: space-between;
  align-items: baseline;
  padding: 16px 22px;
  border-block-end: 1px solid var(--rule);
}

.fs-20__wordmark {
  font: 700 12.5px/1 var(--font-display);
  letter-spacing: 0.24em;
}

.fs-20__heronav {
  font-size: 11.5px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--muted);
}

.fs-20__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  padding: clamp(32px, 6vw, 70px) 18px;
}

.fs-20__head {
  inline-size: 100%;
  max-inline-size: 66rem;
  min-inline-size: 0;
  margin: 0 0 clamp(26px, 4vw, 44px);
}

.fs-20__eyebrow {
  margin: 0 0 14px;
  font: 700 10px/1 var(--font-display);
  letter-spacing: 0.32em;
  text-transform: uppercase;
  color: var(--accent);
}

.fs-20__heading {
  margin: 0;
  max-inline-size: 26ch;
  font: 500 clamp(25px, 4.8vw, 40px)/1.1 var(--font-display);
  letter-spacing: -0.03em;
  text-wrap: balance;
}

.fs-20__grid {
  inline-size: 100%;
  max-inline-size: 66rem;
  min-inline-size: 0;
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 240px), 1fr));
  gap: 20px;
  perspective: 1200px;
  perspective-origin: 50% 40%;
}

.fs-20__card {
  min-inline-size: 0;
  display: flex;
  flex-direction: column;
  gap: 12px;
  padding: 22px 20px 20px;
  background: var(--card);
  border: 1px solid var(--rule);
  border-radius: 10px;
  transform-style: preserve-3d;
  box-shadow: 0 2px 3px var(--shadow-ink), 0 12px 18px -12px var(--shadow-ink), 0 40px 60px -40px var(--shadow-ink);
  transition: transform .3s ease, box-shadow .3s ease, border-color .3s ease;
}

.fs-20__card:hover,
.fs-20__card:focus-within {
  transform: rotate3d(1, -0.6, 0, var(--tilt)) translateZ(14px);
  border-color: color-mix(in oklab, var(--accent) 45%, var(--rule));
  box-shadow: 0 3px 4px var(--shadow-ink), 0 20px 28px -14px var(--shadow-ink), 0 64px 80px -44px var(--shadow-ink);
}

.fs-20__layer {
  display: flex;
  align-items: center;
  gap: 12px;
  transform: translateZ(28px);
}

.fs-20__icon {
  display: grid;
  place-items: center;
  flex: none;
  inline-size: 42px;
  block-size: 42px;
  border-radius: 8px;
  color: var(--accent);
  background: color-mix(in oklab, var(--accent) 12%, var(--card));
  border: 1px solid color-mix(in oklab, var(--accent) 26%, var(--rule));
}

.fs-20__ctitle {
  margin: 0;
  min-inline-size: 0;
  font: 600 13px/1.3 var(--font-display);
  letter-spacing: 0.14em;
  text-transform: uppercase;
}

.fs-20__cprose {
  margin: 0;
  font-size: 13.5px;
  line-height: 1.65;
  color: var(--muted);
  text-wrap: pretty;
}

.fs-20__link {
  display: inline-flex;
  align-items: center;
  align-self: start;
  margin-block-start: auto;
  min-height: 44px;
  font: 600 11px/1 var(--font-display);
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--ink);
  text-decoration: none;
  border-block-end: 1px solid var(--accent);
}

.fs-20__link:hover {
  color: var(--accent);
}

.fs-20__link:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 4px;
}

.fs-20__below {
  padding: 16px 22px;
  border-block-start: 1px solid var(--rule);
  font-size: 11.5px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--muted);
}

@media (prefers-reduced-motion: reduce) {
  .fs-20__card {
    transition: none;
  }

  .fs-20__card:hover,
    .fs-20__card:focus-within {
    transform: none;
  }
}

@media (prefers-color-scheme: light) {
  .fs-20 {
    --page: #eceef1;
    --card: #ffffff;
    --ink: #1c1f26;
    --muted: #5c626e;
    --rule: #dcdfe6;
    --accent: #0f8f5c;
    --shadow-ink: rgba(28, 31, 38, 0.22);
  }
}

[data-theme="dark"] .fs-20 {
  --page: #21232a;
  --card: #2c2f38;
  --ink: #f2f3f5;
  --muted: #a7abb6;
  --rule: #3c404c;
  --accent: #3fd28b;
  --shadow-ink: rgba(0, 0, 0, 0.5);
}
```
