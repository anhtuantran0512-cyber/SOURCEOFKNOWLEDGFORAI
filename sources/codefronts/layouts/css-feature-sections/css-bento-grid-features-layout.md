---
source: "codefronts"
url: "https://codefronts.com/layouts/css-feature-sections/css-bento-grid-features-layout/"
title: "Bento Grid Features Layout Asymmetric"
section: "layouts"
category: "css-feature-sections"
category_name: "CSS Feature Sections"
description: "An asymmetric bento where the cell size carries the argument: one hero cell for the headline capability, two mid cells for the supporting pair, three small…"
has_js: "false"
---

Here's a working CSS Feature Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Bento Grid Features Layout Asymmetric
Source: https://codefronts.com/layouts/css-feature-sections/css-bento-grid-features-layout/

An asymmetric bento where the cell size carries the argument: one hero cell for the headline capability, two mid cells for the supporting pair, three small cells for the details. Named grid-template-areas describe the whole arrangement in six lines and get redefined at two widths, so the hierarchy survives the fold instead of flattening into six identical boxes.
## HTML
```html
<section class="fs-14" aria-labelledby="fs-14-heading">
  <div class="fs-14__hero-strip" aria-hidden="true">
    <span class="fs-14__wordmark">Fernbox</span>
    <span class="fs-14__heronav">Everything your side project outgrew</span>
  </div>

  <div class="fs-14__stage">
    <div class="fs-14__head">
      <h2 class="fs-14__heading" id="fs-14-heading">Six features, sized by how much you will use them</h2>
    </div>

    <div class="fs-14__bento">
      <article class="fs-14__cell fs-14__cell--hero">
        <p class="fs-14__kicker">The main event</p>
        <h3 class="fs-14__htitle">Deploy from a branch in eleven seconds</h3>
        <p class="fs-14__hprose">Push, and Fernbox builds, uploads and swaps the running version behind an atomic pointer. No downtime window, no warm-up request, no cold Lambda on the first visit.</p>
        <div class="fs-14__metrics">
          <div><b>11s</b><span>median deploy</span></div>
          <div><b>0ms</b><span>swap downtime</span></div>
          <div><b>310</b><span>edge locations</span></div>
        </div>
        <a class="fs-14__cta" href="#fs-14-heading">See a deploy log</a>
      </article>

      <article class="fs-14__cell fs-14__cell--mid1">
        <h3 class="fs-14__ctitle">Preview per pull request</h3>
        <p class="fs-14__cprose">Every branch gets its own URL with seeded data, posted back to the PR as a comment.</p>
      </article>

      <article class="fs-14__cell fs-14__cell--mid2">
        <h3 class="fs-14__ctitle">Logs you can actually grep</h3>
        <p class="fs-14__cprose">Structured, searchable and streamed live to your terminal with one command.</p>
      </article>

      <article class="fs-14__cell fs-14__cell--s1">
        <h3 class="fs-14__stitle">Instant rollback</h3>
        <p class="fs-14__sprose">Point back to any previous build.</p>
      </article>

      <article class="fs-14__cell fs-14__cell--s2">
        <h3 class="fs-14__stitle">Secrets, scoped</h3>
        <p class="fs-14__sprose">Per-environment, never in the build log.</p>
      </article>

      <article class="fs-14__cell fs-14__cell--s3">
        <h3 class="fs-14__stitle">Cron without a server</h3>
        <p class="fs-14__sprose">Schedules with retry and a dead-letter queue.</p>
      </article>
    </div>
  </div>

  <div class="fs-14__below" aria-hidden="true">Docs · Templates · Pricing</div>
</section>
```
## CSS
```css
.fs-14 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --page: #fef6e4;
  --page: oklch(0.965 0.037 88);
  --cell: #ffffff;
  --ink: #17130d;
  --ink: oklch(0.2 0.014 60);
  --muted: #5f5647;
  --muted: oklch(0.48 0.024 75);
  --line: #17130d;
  --accent: #f2622a;
  --accent: oklch(0.66 0.19 40);
  --mint: #cdeedd;
  --mint: oklch(0.92 0.06 165);
  --sky: #d6e4ff;
  --sky: oklch(0.9 0.05 260);
  --shadow-offset: 5px;
  --radius: 14px;
  --font-display: "SF Pro Rounded", ui-rounded, "Trebuchet MS", system-ui, sans-serif;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

.fs-14 *,
.fs-14 *::before,
.fs-14 *::after {
  box-sizing: border-box;
}

.fs-14__hero-strip {
  display: flex;
  flex-wrap: wrap;
  gap: 6px 16px;
  justify-content: space-between;
  align-items: baseline;
  padding: 18px 22px;
  border-block-end: 2px solid var(--line);
}

.fs-14__wordmark {
  font: 700 17px/1 var(--font-display);
  letter-spacing: -0.02em;
}

.fs-14__heronav {
  font-size: 12.5px;
  color: var(--muted);
}

.fs-14__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  padding: clamp(28px, 5vw, 60px) 18px;
}

.fs-14__head {
  inline-size: 100%;
  max-inline-size: 68rem;
  min-inline-size: 0;
  margin: 0 0 26px;
}

.fs-14__heading {
  margin: 0;
  max-inline-size: 26ch;
  font: 700 clamp(26px, 5vw, 42px)/1.05 var(--font-display);
  letter-spacing: -0.03em;
  text-wrap: balance;
}

.fs-14__bento {
  inline-size: 100%;
  max-inline-size: 68rem;
  min-inline-size: 0;
  display: grid;
  gap: 14px;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  grid-template-areas: "hero hero mid1" "hero hero mid2" "s1   s2   s3";
}

.fs-14__cell {
  min-inline-size: 0;
  padding: 20px;
  background: var(--cell);
  border: 2px solid var(--line);
  border-radius: var(--radius);
  box-shadow: var(--shadow-offset) var(--shadow-offset) 0 0 var(--line);
}

.fs-14__cell--hero {
  grid-area: hero;
  display: flex;
  flex-direction: column;
  gap: 14px;
  background: var(--accent);
  color: #fff8f2;
  border-color: var(--line);
}

.fs-14__cell--mid1 {
  grid-area: mid1;
  background: var(--mint);
}

.fs-14__cell--mid2 {
  grid-area: mid2;
  background: var(--sky);
}

.fs-14__cell--s1 {
  grid-area: s1;
}

.fs-14__cell--s2 {
  grid-area: s2;
}

.fs-14__cell--s3 {
  grid-area: s3;
}

.fs-14__kicker {
  margin: 0;
  font: 700 10.5px/1 var(--font-display);
  letter-spacing: 0.22em;
  text-transform: uppercase;
  opacity: 0.85;
}

.fs-14__htitle {
  margin: 0;
  font: 700 clamp(22px, 3.6vw, 33px)/1.08 var(--font-display);
  letter-spacing: -0.03em;
  text-wrap: balance;
}

.fs-14__hprose {
  margin: 0;
  max-inline-size: 46ch;
  font-size: 14.5px;
  line-height: 1.6;
  text-wrap: pretty;
}

.fs-14__metrics {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 90px), 1fr));
  gap: 10px;
  margin-block-start: auto;
}

.fs-14__metrics div {
  min-inline-size: 0;
  padding: 10px 12px;
  background: rgba(255, 248, 242, 0.16);
  border-radius: 9px;
}

.fs-14__metrics b {
  display: block;
  font: 700 20px/1.1 var(--font-display);
  letter-spacing: -0.03em;
}

.fs-14__metrics span {
  font-size: 11px;
  opacity: 0.9;
}

.fs-14__cta {
  display: inline-flex;
  align-items: center;
  align-self: start;
  min-height: 44px;
  padding: 0 18px;
  font: 700 13.5px/1 var(--font-display);
  color: var(--ink);
  background: #fff8f2;
  border: 2px solid var(--line);
  border-radius: 999px;
  text-decoration: none;
}

.fs-14__cta:hover {
  background: var(--page);
}

.fs-14__cta:focus-visible {
  outline: 3px solid var(--line);
  outline-offset: 3px;
}

.fs-14__ctitle {
  margin: 0 0 8px;
  font: 700 clamp(17px, 2.2vw, 20px)/1.2 var(--font-display);
  letter-spacing: -0.02em;
  text-wrap: balance;
}

.fs-14__cprose {
  margin: 0;
  font-size: 13.5px;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.fs-14__stitle {
  margin: 0 0 6px;
  font: 700 15px/1.25 var(--font-display);
  letter-spacing: -0.015em;
}

.fs-14__sprose {
  margin: 0;
  font-size: 12.5px;
  line-height: 1.5;
  color: var(--muted);
  overflow-wrap: anywhere;
}

.fs-14__below {
  padding: 16px 22px;
  border-block-start: 2px solid var(--line);
  font-size: 12.5px;
  color: var(--muted);
}

@media (max-width: 860px) {
  .fs-14__bento {
    grid-template-columns: repeat(2, minmax(0, 1fr));
    grid-template-areas: "hero hero" "mid1 mid2" "s1   s2" "s3   s3";
  }
}

@media (max-width: 520px) {
  .fs-14__bento {
    grid-template-columns: minmax(0, 1fr);
    grid-template-areas: "hero" "mid1" "mid2" "s1" "s2" "s3";
  }

  .fs-14 {
    --shadow-offset: 4px;
  }
}

@media (prefers-color-scheme: dark) {
  .fs-14 {
    --page: #171208;
    --cell: #221c12;
    --ink: #fdf6e8;
    --muted: #b3a690;
    --line: #f0e6d2;
    --accent: #ff7a3d;
    --mint: #1d3a2c;
    --sky: #1c2740;
  }

  .fs-14__cell--hero {
    color: #1a1206;
  }

  .fs-14__cta {
    background: #fdf6e8;
    color: #171208;
  }

  .fs-14__metrics div {
    background: rgba(26, 18, 6, 0.18);
  }
}

[data-theme="dark"] .fs-14 {
  --page: #171208;
  --cell: #221c12;
  --ink: #fdf6e8;
  --muted: #b3a690;
  --line: #f0e6d2;
  --accent: #ff7a3d;
  --mint: #1d3a2c;
  --sky: #1c2740;
}

[data-theme="dark"] .fs-14 .fs-14__cell--hero {
  color: #1a1206;
}
```
