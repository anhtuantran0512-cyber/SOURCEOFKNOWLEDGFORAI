---
source: "codefronts"
url: "https://codefronts.com/layouts/css-feature-sections/css-animated-feature-cards-scroll-reveal/"
title: "Animated Feature Cards Scroll Reveal"
section: "layouts"
category: "css-feature-sections"
category_name: "CSS Feature Sections"
description: "Six feature cards that scale and fade into place as they enter the viewport, driven entirely by a view() timeline — no observer, no scroll listener, nothing…"
has_js: "false"
---

Here's a working CSS Feature Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Animated Feature Cards Scroll Reveal
Source: https://codefronts.com/layouts/css-feature-sections/css-animated-feature-cards-scroll-reveal/

Six feature cards that scale and fade into place as they enter the viewport, driven entirely by a view() timeline — no observer, no scroll listener, nothing on the main thread. Each card animates on its own progress, which produces a natural stagger from the grid layout itself, and the @supports gate leaves non-supporting engines with all six cards fully settled.
## HTML
```html
<section class="fs-16" aria-labelledby="fs-16-heading">
  <div class="fs-16__hero" aria-hidden="true">
    <span class="fs-16__wordmark">Ember Works</span>
    <span class="fs-16__heronav">Field service, scheduled properly</span>
  </div>

  <div class="fs-16__stage">
    <div class="fs-16__head">
      <p class="fs-16__eyebrow">Built for the van, not the desk</p>
      <h2 class="fs-16__heading" id="fs-16-heading">Six capabilities your crew will notice on week one</h2>
      <p class="fs-16__sub">Scroll — each card settles as it arrives. No JavaScript is involved.</p>
    </div>

    <ul class="fs-16__grid">
      <li class="fs-16__card">
        <span class="fs-16__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="21" height="21" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M4 17V7l8-3 8 3v10l-8 3z"/><path d="M12 4v16"/></svg></span>
        <h3 class="fs-16__ctitle">Route planning that respects traffic</h3>
        <p class="fs-16__cprose">Jobs are ordered by drive time at the hour they will actually happen, not by straight-line distance.</p>
      </li>
      <li class="fs-16__card">
        <span class="fs-16__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="21" height="21" fill="none" stroke="currentColor" stroke-width="1.7"><rect x="4" y="5" width="16" height="15" rx="2"/><path d="M9 3v4M15 3v4M4 11h16"/></svg></span>
        <h3 class="fs-16__ctitle">Offline-first job sheets</h3>
        <p class="fs-16__cprose">Photos, signatures and parts used are captured in a basement and sync when the van reaches signal.</p>
      </li>
      <li class="fs-16__card">
        <span class="fs-16__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="21" height="21" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M12 3v6M12 21v-6M3 12h6M21 12h-6"/><circle cx="12" cy="12" r="3"/></svg></span>
        <h3 class="fs-16__ctitle">Parts stock per vehicle</h3>
        <p class="fs-16__cprose">Van inventory decrements on job completion and reorders against a minimum you set per part.</p>
      </li>
      <li class="fs-16__card">
        <span class="fs-16__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="21" height="21" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M5 20v-6h4v6M15 20v-9h4v9"/><path d="M3 20h18"/></svg></span>
        <h3 class="fs-16__ctitle">First-time-fix reporting</h3>
        <p class="fs-16__cprose">See which job types come back, by technician and by part, with the callout reason attached.</p>
      </li>
      <li class="fs-16__card">
        <span class="fs-16__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="21" height="21" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M4 6h16v12H4z"/><path d="m4 8 8 5 8-5"/></svg></span>
        <h3 class="fs-16__ctitle">Customer updates that arrive</h3>
        <p class="fs-16__cprose">A two-hour window on booking, a live ETA on the day, and a receipt with photos on completion.</p>
      </li>
      <li class="fs-16__card">
        <span class="fs-16__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="21" height="21" fill="none" stroke="currentColor" stroke-width="1.7"><circle cx="12" cy="12" r="9"/><path d="m8.5 12.5 2.5 2.5 4.5-5"/></svg></span>
        <h3 class="fs-16__ctitle">Compliance certificates on file</h3>
        <p class="fs-16__cprose">Gas, electrical and lift certificates expire loudly, with the renewal booked before the lapse.</p>
      </li>
    </ul>
  </div>

  <div class="fs-16__below" aria-hidden="true">Pricing · Book a demo</div>
</section>
```
## CSS
```css
.fs-16 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --page: #f6f1ea;
  --page: oklch(0.96 0.014 75);
  --card: #fffdfa;
  --ink: #241d16;
  --ink: oklch(0.26 0.018 60);
  --muted: #6b5d50;
  --muted: oklch(0.53 0.024 65);
  --rule: #e2d8ca;
  --rule: oklch(0.89 0.017 80);
  --accent: #d2521f;
  --accent: oklch(0.6 0.17 42);
  --font-display: "Optima", "Palatino Linotype", "Segoe UI", system-ui, sans-serif;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

.fs-16 *,
.fs-16 *::before,
.fs-16 *::after {
  box-sizing: border-box;
}

.fs-16__hero {
  display: flex;
  flex-wrap: wrap;
  gap: 6px 16px;
  justify-content: space-between;
  align-items: baseline;
  padding: 18px 24px;
  border-block-end: 1px solid var(--rule);
}

.fs-16__wordmark {
  font: 600 17px/1 var(--font-display);
  letter-spacing: 0.01em;
}

.fs-16__heronav {
  font-size: 12.5px;
  color: var(--muted);
}

.fs-16__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  padding: clamp(30px, 5.5vw, 66px) 18px clamp(60px, 12vh, 140px);
}

.fs-16__head {
  inline-size: 100%;
  max-inline-size: 66rem;
  min-inline-size: 0;
  margin: 0 0 clamp(24px, 4vw, 42px);
}

.fs-16__eyebrow {
  margin: 0 0 12px;
  font: 600 11px/1 system-ui, sans-serif;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--accent);
}

.fs-16__heading {
  margin: 0 0 10px;
  max-inline-size: 30ch;
  font: 500 clamp(26px, 5vw, 42px)/1.08 var(--font-display);
  letter-spacing: -0.02em;
  text-wrap: balance;
}

.fs-16__sub {
  margin: 0;
  font-size: 14.5px;
  color: var(--muted);
}

.fs-16__grid {
  inline-size: 100%;
  max-inline-size: 66rem;
  min-inline-size: 0;
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 280px), 1fr));
  gap: 20px;
}

.fs-16__card {
  min-inline-size: 0;
  display: flex;
  flex-direction: column;
  gap: 12px;
  padding: 24px 22px 26px;
  background: var(--card);
  border: 1px solid var(--rule);
  border-radius: 6px;
  opacity: 1;
  transform: none;
  box-shadow: 0 18px 40px -28px color-mix(in oklab, var(--accent) 55%, transparent);
}

.fs-16__icon {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border-radius: 50%;
  color: var(--accent);
  background: color-mix(in oklab, var(--accent) 11%, var(--card));
}

.fs-16__ctitle {
  margin: 0;
  font: 500 18px/1.25 var(--font-display);
  letter-spacing: -0.015em;
  text-wrap: balance;
}

.fs-16__cprose {
  margin: 0;
  font-size: 13.5px;
  line-height: 1.65;
  color: var(--muted);
  text-wrap: pretty;
}

.fs-16__below {
  padding: 18px 24px;
  border-block-start: 1px solid var(--rule);
  font-size: 12.5px;
  color: var(--muted);
}

@supports (animation-timeline: view()) {
  .fs-16__card {
    animation: fs-16-reveal linear both;
    animation-timeline: view();
    animation-range: entry 15% cover 40%;
  }

  @keyframes fs-16-reveal {
    from {
      opacity: 0;
      transform: scale(0.94) translateY(18px);
      box-shadow: 0 4px 10px -8px color-mix(in oklab, var(--accent) 40%, transparent);
    }

    to {
      opacity: 1;
      transform: none;
    }
  }
}

@media (prefers-reduced-motion: reduce) {
  .fs-16__card {
    animation: none;
    opacity: 1;
    transform: none;
  }
}

@media (prefers-color-scheme: dark) {
  .fs-16 {
    --page: #1a1510;
    --card: #221c16;
    --ink: #f5efe6;
    --muted: #ab9c8c;
    --rule: #332b22;
    --accent: #f2854f;
  }
}

[data-theme="dark"] .fs-16 {
  --page: #1a1510;
  --card: #221c16;
  --ink: #f5efe6;
  --muted: #ab9c8c;
  --rule: #332b22;
  --accent: #f2854f;
}
```
