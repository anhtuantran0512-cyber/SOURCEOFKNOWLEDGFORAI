---
source: "codefronts"
url: "https://codefronts.com/layouts/css-feature-sections/css-feature-section-dark-glassmorphism/"
title: "Dark Glassmorphism Feature Section"
section: "layouts"
category: "css-feature-sections"
category_name: "CSS Feature Sections"
description: "Frosted feature cards floating over an ambient gradient, with the inner-highlight rim that separates real glass from a translucent rectangle."
has_js: "false"
---

Here's a working CSS Feature Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dark Glassmorphism Feature Section
Source: https://codefronts.com/layouts/css-feature-sections/css-feature-section-dark-glassmorphism/

Frosted feature cards floating over an ambient gradient, with the inner-highlight rim that separates real glass from a translucent rectangle. Includes a zero-JavaScript light-glass toggle built from a checkbox and :has(), with the mirror flip-back rules that keep it correct under both OS colour schemes, and a solid-surface fallback where backdrop-filter is unavailable.
## HTML
```html
<section class="fs-15" aria-labelledby="fs-15-heading">
  <div class="fs-15__hero" aria-hidden="true">
    <span class="fs-15__wordmark">Talon</span>
    <span class="fs-15__heronav">Launch week · day three</span>
  </div>

  <div class="fs-15__stage">
    <div class="fs-15__head">
      <div class="fs-15__headtop">
        <p class="fs-15__eyebrow">Shipped this week</p>
        <label class="fs-15__toggle">
          <input class="fs-15__check" type="checkbox">
          <span class="fs-15__track" aria-hidden="true"><i></i></span>
          <span class="fs-15__tlabel">Flip the glass</span>
        </label>
      </div>
      <h2 class="fs-15__heading" id="fs-15-heading">Four surfaces, rebuilt on the new runtime</h2>
      <p class="fs-15__sub">Everything below is live in production and behind no flag.</p>
    </div>

    <ul class="fs-15__cards">
      <li class="fs-15__card">
        <span class="fs-15__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M13 2 4 14h6l-1 8 9-12h-6z"/></svg></span>
        <h3 class="fs-15__ctitle">Cold starts under 20ms</h3>
        <p class="fs-15__cprose">Isolates boot from a snapshot rather than a container image, so the first request pays no penalty.</p>
        <ul class="fs-15__chips"><li>V8 isolates</li><li>Snapshot boot</li></ul>
      </li>
      <li class="fs-15__card">
        <span class="fs-15__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.7"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/></svg></span>
        <h3 class="fs-15__ctitle">Regional reads, single writer</h3>
        <p class="fs-15__cprose">Read replicas in eleven regions with a consistency token, so you choose freshness per query.</p>
        <ul class="fs-15__chips"><li>11 regions</li><li>Read-your-writes</li></ul>
      </li>
      <li class="fs-15__card">
        <span class="fs-15__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.7"><rect x="3" y="4" width="18" height="16" rx="3"/><path d="M8 9h8M8 13h5"/></svg></span>
        <h3 class="fs-15__ctitle">Queues with a visible backlog</h3>
        <p class="fs-15__cprose">Depth, age and retry count per consumer group, with a dead-letter view you can replay from.</p>
        <ul class="fs-15__chips"><li>Replay window</li><li>Per-group metrics</li></ul>
      </li>
      <li class="fs-15__card">
        <span class="fs-15__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M12 3l8 4v6c0 4-3.5 7-8 8-4.5-1-8-4-8-8V7z"/><path d="M12 9v4"/></svg></span>
        <h3 class="fs-15__ctitle">Secrets bound at the edge</h3>
        <p class="fs-15__cprose">Environment values are decrypted in the isolate, never written to disk and never printed in a build log.</p>
        <ul class="fs-15__chips"><li>KMS-backed</li><li>Per-environment</li></ul>
      </li>
    </ul>
  </div>

  <div class="fs-15__below" aria-hidden="true">Changelog · Runtime docs · Pricing</div>
</section>
```
## CSS
```css
.fs-15 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --bg: #0a0713;
  --bg: oklch(0.16 0.03 300);
  --ink: #f5f1ff;
  --muted: #b7aed4;
  --muted: oklch(0.78 0.04 300);
  --glass-fill: rgba(255, 255, 255, 0.07);
  --glass-rule: rgba(255, 255, 255, 0.16);
  --rim: rgba(255, 255, 255, 0.22);
  --accent: #a78bfa;
  --accent: oklch(0.75 0.15 296);
  --amb1: rgba(167, 139, 250, 0.32);
  --amb2: rgba(56, 189, 248, 0.2);
  --amb3: rgba(236, 72, 153, 0.16);
  --blur: 18px;
  --font-display: "Söhne", "Helvetica Neue", system-ui, -apple-system, sans-serif;
  background-color: var(--bg);
  background-image: radial-gradient(60% 50% at 18% 12%, var(--amb1), transparent 70%), radial-gradient(50% 45% at 82% 30%, var(--amb2), transparent 70%), radial-gradient(55% 50% at 50% 92%, var(--amb3), transparent 70%);
  color: var(--ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

.fs-15 *,
.fs-15 *::before,
.fs-15 *::after {
  box-sizing: border-box;
}

.fs-15__hero {
  display: flex;
  flex-wrap: wrap;
  gap: 6px 16px;
  justify-content: space-between;
  align-items: baseline;
  padding: 20px 26px;
  border-block-end: 1px solid var(--glass-rule);
}

.fs-15__wordmark {
  font: 650 16px/1 var(--font-display);
  letter-spacing: -0.02em;
}

.fs-15__heronav {
  font-size: 12.5px;
  color: var(--muted);
}

.fs-15__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  padding: clamp(32px, 6vw, 72px) 20px;
}

.fs-15__head {
  inline-size: 100%;
  max-inline-size: 66rem;
  min-inline-size: 0;
  margin: 0 0 clamp(26px, 4vw, 44px);
}

.fs-15__headtop {
  display: flex;
  flex-wrap: wrap;
  gap: 14px;
  align-items: center;
  justify-content: space-between;
  margin: 0 0 16px;
}

.fs-15__eyebrow {
  margin: 0;
  font: 650 10.5px/1 var(--font-display);
  letter-spacing: 0.24em;
  text-transform: uppercase;
  color: var(--accent);
}

.fs-15__toggle {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  min-height: 44px;
  cursor: pointer;
}

.fs-15__check {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  clip-path: inset(50%);
  overflow: hidden;
}

.fs-15__track {
  inline-size: 40px;
  block-size: 22px;
  border-radius: 999px;
  background: var(--glass-fill);
  border: 1px solid var(--glass-rule);
  display: grid;
  align-items: center;
  padding: 2px;
  transition: background-color .2s ease;
}

.fs-15__track i {
  inline-size: 16px;
  block-size: 16px;
  border-radius: 50%;
  background: var(--accent);
  transition: transform .2s ease;
}

.fs-15:has(.fs-15__check:checked) .fs-15__track i {
  transform: translateX(18px);
}

.fs-15__check:focus-visible + .fs-15__track {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.fs-15__tlabel {
  font-size: 12.5px;
  color: var(--muted);
}

.fs-15__heading {
  margin: 0 0 12px;
  max-inline-size: 26ch;
  font: 650 clamp(27px, 5.2vw, 44px)/1.08 var(--font-display);
  letter-spacing: -0.035em;
  text-wrap: balance;
}

.fs-15__sub {
  margin: 0;
  font-size: 15px;
  color: var(--muted);
}

.fs-15__cards {
  inline-size: 100%;
  max-inline-size: 66rem;
  min-inline-size: 0;
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 270px), 1fr));
  gap: 18px;
}

.fs-15__card {
  position: relative;
  min-inline-size: 0;
  display: flex;
  flex-direction: column;
  gap: 12px;
  padding: 28px 24px 26px;
  border-radius: 20px;
  background: var(--glass-fill);
  border: 1px solid var(--glass-rule);
  box-shadow: inset 0 1px 0 var(--rim), 0 24px 60px -34px rgba(0, 0, 0, 0.75);
  backdrop-filter: blur(var(--blur)) saturate(150%);
  -webkit-backdrop-filter: blur(var(--blur)) saturate(150%);
}

.fs-15__card::before {
  content: "";
  position: absolute;
  inset: 0 0 auto;
  block-size: 1px;
  border-radius: 20px 20px 0 0;
  background: linear-gradient(90deg, transparent, var(--rim), transparent);
}

.fs-15__icon {
  display: grid;
  place-items: center;
  inline-size: 42px;
  block-size: 42px;
  border-radius: 12px;
  color: var(--accent);
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid var(--glass-rule);
}

.fs-15__ctitle {
  margin: 0;
  font: 650 17px/1.28 var(--font-display);
  letter-spacing: -0.02em;
  text-wrap: balance;
}

.fs-15__cprose {
  margin: 0;
  font-size: 13.5px;
  line-height: 1.65;
  color: var(--muted);
  text-wrap: pretty;
}

.fs-15__chips {
  display: flex;
  flex-wrap: wrap;
  gap: 7px;
  margin: auto 0 0;
  padding: 0;
  list-style: none;
}

.fs-15__chips li {
  padding: 5px 10px;
  font-size: 11px;
  font-weight: 600;
  color: var(--ink);
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid var(--glass-rule);
  border-radius: 999px;
}

.fs-15__below {
  padding: 18px 26px;
  border-block-start: 1px solid var(--glass-rule);
  font-size: 12.5px;
  color: var(--muted);
}

@supports not (backdrop-filter: blur(1px)) {
  .fs-15__card {
    background: #171130;
    background: color-mix(in oklab, var(--bg) 78%, white 6%);
  }
}

@media (prefers-reduced-motion: reduce) {
  .fs-15__track,
    .fs-15__track i {
    transition: none;
  }
}

@media (prefers-color-scheme: light) {
  .fs-15 {
    --bg: #f3f0fb;
    --ink: #171227;
    --muted: #5a5175;
    --glass-fill: rgba(255, 255, 255, 0.55);
    --glass-rule: rgba(23, 18, 39, 0.1);
    --rim: rgba(255, 255, 255, 0.9);
    --accent: #6d3ff0;
    --amb1: rgba(167, 139, 250, 0.4);
    --amb2: rgba(56, 189, 248, 0.28);
    --amb3: rgba(236, 72, 153, 0.22);
  }

  .fs-15__card {
    box-shadow: inset 0 1px 0 var(--rim), 0 24px 50px -34px rgba(23, 18, 39, 0.4);
  }

  .fs-15__icon,
    .fs-15__chips li,
    .fs-15__track {
    background: rgba(255, 255, 255, 0.6);
  }

  .fs-15:has(.fs-15__check:checked) {
    --bg: #0a0713;
    --ink: #f5f1ff;
    --muted: #b7aed4;
    --glass-fill: rgba(255, 255, 255, 0.07);
    --glass-rule: rgba(255, 255, 255, 0.16);
    --rim: rgba(255, 255, 255, 0.22);
    --accent: #a78bfa;
    --amb1: rgba(167, 139, 250, 0.32);
    --amb2: rgba(56, 189, 248, 0.2);
    --amb3: rgba(236, 72, 153, 0.16);
  }

  .fs-15:has(.fs-15__check:checked) .fs-15__card {
    box-shadow: inset 0 1px 0 var(--rim), 0 24px 60px -34px rgba(0, 0, 0, 0.75);
  }

  .fs-15:has(.fs-15__check:checked) .fs-15__icon,
    .fs-15:has(.fs-15__check:checked) .fs-15__chips li,
    .fs-15:has(.fs-15__check:checked) .fs-15__track {
    background: rgba(255, 255, 255, 0.08);
  }
}

@media (prefers-color-scheme: dark) {
  .fs-15 {
    --bg: #0a0713;
    --ink: #f5f1ff;
    --muted: #b7aed4;
    --glass-fill: rgba(255, 255, 255, 0.07);
    --glass-rule: rgba(255, 255, 255, 0.16);
    --rim: rgba(255, 255, 255, 0.22);
    --accent: #a78bfa;
    --amb1: rgba(167, 139, 250, 0.32);
    --amb2: rgba(56, 189, 248, 0.2);
    --amb3: rgba(236, 72, 153, 0.16);
  }

  .fs-15:has(.fs-15__check:checked) {
    --bg: #f3f0fb;
    --ink: #171227;
    --muted: #5a5175;
    --glass-fill: rgba(255, 255, 255, 0.55);
    --glass-rule: rgba(23, 18, 39, 0.1);
    --rim: rgba(255, 255, 255, 0.9);
    --accent: #6d3ff0;
    --amb1: rgba(167, 139, 250, 0.4);
    --amb2: rgba(56, 189, 248, 0.28);
    --amb3: rgba(236, 72, 153, 0.22);
  }

  .fs-15:has(.fs-15__check:checked) .fs-15__card {
    box-shadow: inset 0 1px 0 var(--rim), 0 24px 50px -34px rgba(23, 18, 39, 0.4);
  }

  .fs-15:has(.fs-15__check:checked) .fs-15__icon,
    .fs-15:has(.fs-15__check:checked) .fs-15__chips li,
    .fs-15:has(.fs-15__check:checked) .fs-15__track {
    background: rgba(255, 255, 255, 0.6);
  }
}
```
