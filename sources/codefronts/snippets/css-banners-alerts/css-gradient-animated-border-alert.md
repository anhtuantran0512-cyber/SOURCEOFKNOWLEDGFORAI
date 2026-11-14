---
source: "codefronts"
url: "https://codefronts.com/snippets/css-banners-alerts/css-gradient-animated-border-alert/"
title: "Animated Gradient Border Alert"
section: "snippets"
category: "css-banners-alerts"
category_name: "CSS Banners & Alerts"
description: "The rotating gradient border, done the correct way: a registered <angle> so the conic gradient actually interpolates, and mask-composite:exclude so the fill…"
has_js: "false"
---

Here's a working CSS Banners & Alert from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Animated Gradient Border Alert
Source: https://codefronts.com/snippets/css-banners-alerts/css-gradient-animated-border-alert/

The rotating gradient border, done the correct way: a registered <angle> so the conic gradient actually interpolates, and mask-composite:exclude so the fill stays a true 1.5px ring instead of a padded box faking it. Three states — processing, ready, failed — plus a soft outer bloom that inherits the same angle.
## HTML
```html
<div class="ba-19">
  <div class="ba-19__stack">
    <div class="ba-19__alert" data-state="processing" role="status">
      <input class="ba-19__vh" type="checkbox" id="ba-19-x1">
      <span class="ba-19__bloom" aria-hidden="true"></span>
      <span class="ba-19__icon" aria-hidden="true">
        <svg viewBox="0 0 20 20" fill="none" focusable="false"><path d="M10 2.6v3.2M10 14.2v3.2M2.6 10h3.2M14.2 10h3.2M4.8 4.8l2.3 2.3M12.9 12.9l2.3 2.3M15.2 4.8l-2.3 2.3M7.1 12.9l-2.3 2.3" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
      </span>
      <div class="ba-19__body">
        <p class="ba-19__title">Rebuilding the search index</p>
        <p class="ba-19__text">1.2 million documents · roughly 4 minutes remaining. You can keep working; results will be stale until this finishes.</p>
      </div>
      <label class="ba-19__x" for="ba-19-x1" tabindex="0" role="button" aria-label="Dismiss">
        <svg viewBox="0 0 16 16" fill="none" aria-hidden="true" focusable="false"><path d="m5 5 6 6m0-6-6 6" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
      </label>
    </div>

    <div class="ba-19__alert" data-state="ready" role="status">
      <input class="ba-19__vh" type="checkbox" id="ba-19-x2">
      <span class="ba-19__bloom" aria-hidden="true"></span>
      <span class="ba-19__icon" aria-hidden="true">
        <svg viewBox="0 0 20 20" fill="none" focusable="false"><path d="m5 10.4 3.3 3.3L15.2 6.6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </span>
      <div class="ba-19__body">
        <p class="ba-19__title">Index rebuilt in 3m 41s</p>
        <p class="ba-19__text">Search is live across all 34 regions. The ring has stopped, because a border that spins forever tells the user nothing finished.</p>
      </div>
      <label class="ba-19__x" for="ba-19-x2" tabindex="0" role="button" aria-label="Dismiss">
        <svg viewBox="0 0 16 16" fill="none" aria-hidden="true" focusable="false"><path d="m5 5 6 6m0-6-6 6" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
      </label>
    </div>

    <div class="ba-19__alert" data-state="failed" role="alert">
      <input class="ba-19__vh" type="checkbox" id="ba-19-x3">
      <span class="ba-19__bloom" aria-hidden="true"></span>
      <span class="ba-19__icon" aria-hidden="true">
        <svg viewBox="0 0 20 20" fill="none" focusable="false"><path d="M10 3.4 17.4 16H2.6z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><path d="M10 8.2v3.4M10 13.6h.01" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg>
      </span>
      <div class="ba-19__body">
        <p class="ba-19__title">Sync to the warehouse failed</p>
        <p class="ba-19__text">Credentials expired 6 hours ago. The last successful sync was 04:12 UTC and no data was lost.</p>
        <p class="ba-19__acts"><a href="#ba-19-a">Rotate credentials</a><a href="#ba-19-a">Open run log</a></p>
      </div>
      <label class="ba-19__x" for="ba-19-x3" tabindex="0" role="button" aria-label="Dismiss">
        <svg viewBox="0 0 16 16" fill="none" aria-hidden="true" focusable="false"><path d="m5 5 6 6m0-6-6 6" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
      </label>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter+Tight:wght@400;500;600&display=swap');

@property --ba-19-a {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

.ba-19 {
  --ring: 1.5px;
  --speed: 4s;
  --bg: #07080b;
  --surface: #101319;
  --ink: #f2f4f8;
  --muted: #939ba8;
  --line: #20242c;
  --c1: #6d5cff;
  --c2: #00e5ff;
  --c3: #ff5cd6;
  --display: "Space Grotesk",ui-sans-serif,system-ui,sans-serif;
  --sans: "Inter Tight",ui-sans-serif,system-ui,-apple-system,sans-serif;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  box-sizing: border-box;
  padding: clamp(1rem,4vw,3rem);
  background: radial-gradient(40rem 26rem at 50% -8%, color-mix(in oklab,var(--c1) 20%,transparent), transparent 68%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
}

.ba-19 *,
.ba-19 *::before,
.ba-19 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(50% 0 0)) {
  .ba-19 {
    --bg: oklch(13% .012 275);
    --surface: oklch(19% .016 275);
    --ink: oklch(96% .006 275);
    --muted: oklch(70% .016 275);
    --line: oklch(27% .018 275);
    --c1: oklch(66% .22 285);
    --c2: oklch(84% .16 200);
    --c3: oklch(74% .2 340);
  }
}

@media (prefers-color-scheme: light) {
  .ba-19:not([data-theme="dark"]) {
    --bg: #f4f5f8;
    --surface: #ffffff;
    --ink: #0d1016;
    --muted: #5b6270;
    --line: #e3e6ec;
  }
}

.ba-19__stack {
  width: min(40rem,100%);
  display: grid;
  gap: 1rem;
}

.ba-19__alert {
  position: relative;
  isolation: isolate;
  display: grid;
  grid-template-columns: auto minmax(0,1fr) auto;
  gap: .85rem;
  align-items: start;
  padding: 1.1rem 1.15rem;
  border-radius: 1.15rem;
  background: var(--surface);
  border: 1px solid transparent;
  transition: opacity .3s ease, translate .3s cubic-bezier(.16,1,.3,1), display .3s allow-discrete;
}

@starting-style {
  .ba-19__alert {
    opacity: 0;
    translate: 0 .5rem;
  }
}

.ba-19__alert:has(input:checked) {
  display: none;
  opacity: 0;
  translate: 0 -.4rem;
}

.ba-19__alert::before {
  content: "";
  position: absolute;
  inset: 0;
  z-index: -1;
  border-radius: inherit;
  padding: var(--ring);
  background: conic-gradient(from var(--ba-19-a), var(--c1), var(--c2) 32%, var(--c3) 62%, var(--c1));
  mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
  mask-composite: exclude;
  -webkit-mask-composite: xor;
  animation: ba-19-spin var(--speed) linear infinite;
}

@keyframes ba-19-spin {
  to {
    --ba-19-a: 360deg;
  }
}

.ba-19__bloom {
  position: absolute;
  inset: -.4rem;
  z-index: -2;
  border-radius: 1.5rem;
  opacity: .4;
  filter: blur(1.25rem);
  background: conic-gradient(from var(--ba-19-a), var(--c1), var(--c2) 32%, var(--c3) 62%, var(--c1));
  animation: ba-19-spin var(--speed) linear infinite;
}

@supports not (mask-composite: exclude) {
  .ba-19__alert {
    border-color: var(--c1);
  }

  .ba-19__alert::before {
    display: none;
  }
}

.ba-19__alert[data-state="ready"] {
  --c1: #12d18e;
  --c2: #7ff3c8;
  --c3: #0a9a6a;
  --speed: 0s;
}

.ba-19__alert[data-state="ready"]::before,
.ba-19__alert[data-state="ready"] .ba-19__bloom {
  animation: none;
  --ba-19-a: 135deg;
}

.ba-19__alert[data-state="failed"] {
  --c1: #ff4d4d;
  --c2: #ffb37a;
  --c3: #c81e5b;
  --speed: 9s;
}

.ba-19__alert[data-state="failed"] .ba-19__bloom {
  opacity: .3;
}

@supports (color: oklch(50% 0 0)) {
  .ba-19__alert[data-state="ready"] {
    --c1: oklch(74% .17 160);
    --c2: oklch(88% .13 165);
    --c3: oklch(62% .15 158);
  }

  .ba-19__alert[data-state="failed"] {
    --c1: oklch(66% .21 25);
    --c2: oklch(82% .14 60);
    --c3: oklch(56% .2 5);
  }
}

.ba-19__icon {
  display: grid;
  place-items: center;
  width: 2.25rem;
  height: 2.25rem;
  flex: none;
  border-radius: .75rem;
  color: var(--c1);
  background: color-mix(in oklab,var(--c1) 15%,transparent);
  border: 1px solid color-mix(in oklab,var(--c1) 30%,transparent);
}

.ba-19__icon svg {
  width: 1.2rem;
  height: 1.2rem;
}

.ba-19__alert[data-state="processing"] .ba-19__icon svg {
  animation: ba-19-tick 3s steps(8,end) infinite;
}

@keyframes ba-19-tick {
  to {
    rotate: 360deg;
  }
}

.ba-19__body {
  min-width: 0;
  display: grid;
  gap: .3rem;
}

.ba-19__title {
  margin: 0;
  font-family: var(--display);
  font-size: .9375rem;
  font-weight: 600;
  line-height: 1.4;
  letter-spacing: -.025em;
}

.ba-19__text {
  margin: 0;
  font-size: .8125rem;
  line-height: 1.6;
  color: var(--muted);
  max-width: 64ch;
  text-wrap: pretty;
  font-variant-numeric: tabular-nums;
}

.ba-19__acts {
  margin: .3rem 0 0;
  display: flex;
  flex-wrap: wrap;
  gap: .85rem;
}

.ba-19__acts a {
  font-size: .8125rem;
  font-weight: 600;
  color: var(--c1);
  text-decoration: underline;
  text-underline-offset: 3px;
  text-decoration-thickness: 1.5px;
}

.ba-19__acts a:hover {
  text-decoration-thickness: 2.5px;
}

.ba-19__x {
  display: grid;
  place-items: center;
  width: 2.25rem;
  height: 2.25rem;
  margin: -.3rem -.3rem 0 0;
  border-radius: .55rem;
  cursor: pointer;
  color: var(--muted);
  transition: color .2s ease, background .2s ease;
}

.ba-19__x:hover {
  color: var(--ink);
  background: color-mix(in oklab,var(--ink) 8%,transparent);
}

.ba-19__x svg {
  width: .95rem;
  height: .95rem;
}

.ba-19__x:focus-visible {
  outline: 2px solid var(--c1);
  outline-offset: 2px;
}

.ba-19__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.ba-19 a {
  color: var(--c2);
}

.ba-19 :focus-visible {
  outline: 2px solid var(--c2);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .ba-19 * {
    animation: none !important;
    transition: none !important;
  }

  .ba-19__alert::before {
    background: linear-gradient(135deg,var(--c1),var(--c3));
  }

  .ba-19__bloom {
    display: none;
  }
}

@media (forced-colors: active) {
  .ba-19__alert {
    border: 1px solid CanvasText;
  }

  .ba-19__alert::before,
    .ba-19__bloom {
    display: none;
  }
}
```
