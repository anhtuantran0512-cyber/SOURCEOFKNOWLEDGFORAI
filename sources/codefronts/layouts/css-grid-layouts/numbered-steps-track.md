---
source: "codefronts"
url: "https://codefronts.com/layouts/css-grid-layouts/numbered-steps-track/"
title: "Numbered Steps Track"
section: "layouts"
category: "css-grid-layouts"
category_name: "CSS Grid Layouts"
description: "An onboarding/setup timeline as a two-column grid: auto-numbered circles (CSS counters — renumber by reordering HTML) in a fixed rail, content beside them,…"
has_js: "false"
---

Here's a working CSS Grid Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Numbered Steps Track
Source: https://codefronts.com/layouts/css-grid-layouts/numbered-steps-track/

An onboarding/setup timeline as a two-column grid: auto-numbered circles (CSS counters — renumber by reordering HTML) in a fixed rail, content beside them, and a connecting line drawn per-item so it starts and stops exactly at the first and last step. An <ol> underneath, as the semantics demand.
## HTML
```html
<section class="cgl-25" aria-label="Numbered steps demo">
  <ol class="cgl-25__track">
    <li class="is-done"><h4>Create your account</h4><p>Email, password, verify. The circle numbers itself with a CSS counter.</p></li>
    <li class="is-done"><h4>Connect a repository</h4><p>The connector line is per-item — watch it stop cleanly at the last step.</p></li>
    <li class="is-current"><h4>Configure the pipeline</h4><p>You are here. One class flips circle, ring and text state together.</p></li>
    <li><h4>Ship to production</h4><p>No line below — :last-child suppresses the connector.</p></li>
  </ol>
</section>
```
## CSS
```css
.cgl-25,
.cgl-25 *,
.cgl-25 *::before,
.cgl-25 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cgl-25 {
  width: 100%;
  min-height: 100vh;
  --gold: oklch(0.8 0.13 85);
  --ink: oklch(0.93 0.01 85);
  --dim: oklch(0.62 0.02 85);
  --bg: oklch(0.17 0.015 85);
  --line: oklch(0.35 0.03 85);
  font-family: system-ui,sans-serif;
  background: var(--bg);
  padding: 1.6rem 1.4rem;
}

.cgl-25 .cgl-25__track {
  list-style: none;
  counter-reset: step;
  display: flex;
  flex-direction: column;
  gap: 1.6rem;
  max-inline-size: 520px;
  margin-inline: auto;
}

.cgl-25 .cgl-25__track li {
  counter-increment: step;
  display: grid;
  grid-template-columns: 44px minmax(0,1fr);
  column-gap: 14px;
  position: relative;
}

.cgl-25 .cgl-25__track li::before {
  content: counter(step);
  grid-column: 1;
  inline-size: 36px;
  aspect-ratio: 1;
  border-radius: 50%;
  display: grid;
  place-items: center;
  font-weight: 700;
  font-size: .9rem;
  color: var(--dim);
  background: var(--bg);
  border: 2px solid var(--line);
  z-index: 1;
}

.cgl-25 .cgl-25__track li::after {
  content: "";
  position: absolute;
  inset-inline-start: 17px;
  inset-block-start: 40px;
  inline-size: 2px;
  block-size: calc(100% - 36px + 1.6rem);
  background: var(--line);
}

.cgl-25 .cgl-25__track li:last-child::after {
  content: none;
}

.cgl-25 .cgl-25__track li>* {
  grid-column: 2;
}

.cgl-25 .cgl-25__track li h4 {
  font-size: .95rem;
  color: var(--ink);
  padding-block-start: .4rem;
}

.cgl-25 .cgl-25__track li p {
  font-size: .8rem;
  line-height: 1.6;
  color: var(--dim);
  margin-block-start: .3rem;
}

.cgl-25 li.is-done::before {
  color: var(--bg);
  background: var(--gold);
  border-color: var(--gold);
  content: "✓";
}

.cgl-25 li.is-done::after {
  background: var(--gold);
}

.cgl-25 li.is-current::before {
  color: var(--gold);
  border-color: var(--gold);
  animation: cgl-25-pulse 2s ease-in-out infinite;
}

@keyframes cgl-25-pulse {
  50% {
    box-shadow: 0 0 0 6px color-mix(in oklab,var(--gold) 25%,transparent);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cgl-25 li.is-current::before {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — CSS counters number the circles; each item draws its own connector, suppressed on :last-child. */
```
