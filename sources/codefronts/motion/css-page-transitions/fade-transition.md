---
source: "codefronts"
url: "https://codefronts.com/motion/css-page-transitions/fade-transition/"
title: "CSS Page Fade Transition on Route Change"
section: "motion"
category: "css-page-transitions"
category_name: "CSS Page Transitions"
description: "The simplest correct transition and the one to reach for by default."
has_js: "false"
---

Here's a working CSS Page Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Page Fade Transition on Route Change
Source: https://codefronts.com/motion/css-page-transitions/fade-transition/

The simplest correct transition and the one to reach for by default. Opacity only, no transform, so it never fights scroll position or layout and costs almost nothing to composite. Everything else in this collection is measured against it &mdash; if a fancier effect is not clearly better than this, ship this.
## HTML
```html
<section class="pt-10" aria-labelledby="pt-10-h">
  <div class="pt-10__theme">
    <input class="pt-10__theme-input" type="checkbox" id="pt-10-theme">
    <label class="pt-10__theme-label" for="pt-10-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="pt-10__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="pt-10__stage">
    <header class="pt-10__head">
      <p class="pt-10__kicker">Page transitions / 10</p>
      <h2 class="pt-10__h" id="pt-10-h">The baseline fade</h2>
      <p class="pt-10__lede">Opacity only, no script. Routes are DOM sections held by radio inputs and swapped in place &mdash; there is no router in this frame.</p>
    </header>

    <div class="pt-10__app">
      <nav class="pt-10__side" aria-label="Workspace routes">
        <p class="pt-10__side-t">Prism</p>
        <div class="pt-10__routes">
          <input class="pt-10__radio" type="radio" name="pt-10-r" id="pt-10-r1" checked>
          <label class="pt-10__nav" for="pt-10-r1">
            <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><rect x="4" y="4" width="7" height="7" fill="currentColor"/><rect x="13" y="4" width="7" height="7" opacity="0.4" fill="currentColor"/><rect x="4" y="13" width="7" height="7" opacity="0.4" fill="currentColor"/><rect x="13" y="13" width="7" height="7" opacity="0.4" fill="currentColor"/></svg>
            Dashboard
          </label>
          <input class="pt-10__radio" type="radio" name="pt-10-r" id="pt-10-r2">
          <label class="pt-10__nav" for="pt-10-r2">
            <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 18V9m5 9V5m5 13v-6m5 6V8" stroke="currentColor" stroke-width="2" fill="none"/></svg>
            Analytics
          </label>
          <input class="pt-10__radio" type="radio" name="pt-10-r" id="pt-10-r3">
          <label class="pt-10__nav" for="pt-10-r3">
            <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="8" r="3.2" fill="currentColor"/><path d="M5 20c0-3.6 3.1-5.5 7-5.5s7 1.9 7 5.5" fill="currentColor"/></svg>
            Team
          </label>
        </div>
      </nav>

      <div class="pt-10__view">
        <div class="pt-10__veil" aria-hidden="true"></div>
        <main class="pt-10__route pt-10__route--1">
          <h3 class="pt-10__title">Dashboard</h3>
          <div class="pt-10__cards">
            <div class="pt-10__card"><b>2.14M</b><span>requests today</span></div>
            <div class="pt-10__card"><b>41ms</b><span>median latency</span></div>
            <div class="pt-10__card"><b>0</b><span>open incidents</span></div>
          </div>
          <p class="pt-10__text">All four regions healthy. Last deployment promoted by Alex Chen 24 minutes ago.</p>
        </main>
        <main class="pt-10__route pt-10__route--2">
          <h3 class="pt-10__title">Analytics</h3>
          <div class="pt-10__cards">
            <div class="pt-10__card"><b>18.4%</b><span>week on week</span></div>
            <div class="pt-10__card"><b>3m 12s</b><span>median session</span></div>
            <div class="pt-10__card"><b>62%</b><span>returning</span></div>
          </div>
          <p class="pt-10__text">Growth is concentrated in the API surface rather than the dashboard, which matches the migration plan.</p>
        </main>
        <main class="pt-10__route pt-10__route--3">
          <h3 class="pt-10__title">Team</h3>
          <div class="pt-10__cards">
            <div class="pt-10__card"><b>14</b><span>members</span></div>
            <div class="pt-10__card"><b>2</b><span>pending invites</span></div>
            <div class="pt-10__card"><b>3</b><span>admins</span></div>
          </div>
          <p class="pt-10__text">Priya Sharma and Jordan Lee both hold admin. Sam Rivera&rsquo;s invitation expires on Friday.</p>
        </main>
      </div>
    </div>

    <figure class="pt-10__meter">
      <figcaption class="pt-10__meter-cap">Fade duration</figcaption>
      <div class="pt-10__scale" aria-hidden="true"><span class="pt-10__band"></span><span class="pt-10__mark"></span></div>
      <p class="pt-10__meter-t">This demo runs at 210ms. Under 120ms reads as a flicker; over 300ms reads as waiting.</p>
    </figure>
  </div>
</section>
```
## CSS
```css
.pt-10 {
  --pt-10-bg: #fafafa;
  --pt-10-s1: #ffffff;
  --pt-10-s2: #f2f2f3;
  --pt-10-line: #e2e2e4;
  --pt-10-ink: #18181b;
  --pt-10-mut: #63636b;
  --pt-10-acc: #3f3f46;
  --pt-10-dur: 210ms;
  --pt-10-shadow: 0 1px 2px rgba(24, 24, 27, 0.05), 0 12px 32px -18px rgba(24, 24, 27, 0.25);
  --pt-10-font-display: "Inter", "Helvetica Neue", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--pt-10-bg);
  color: var(--pt-10-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.55;
}

.pt-10 *,
.pt-10 *::before,
.pt-10 *::after {
  box-sizing: border-box;
}

.pt-10:has(.pt-10__theme-input:checked) {
  --pt-10-bg: #09090b;
  --pt-10-s1: #121215;
  --pt-10-s2: #19191d;
  --pt-10-line: #26262b;
  --pt-10-ink: #f4f4f5;
  --pt-10-mut: #9c9ca6;
  --pt-10-acc: #d4d4d8;
  --pt-10-shadow: 0 1px 2px rgba(0, 0, 0, 0.6), 0 12px 32px -18px rgba(0, 0, 0, 0.8);
}

@media (prefers-color-scheme: dark) {
  .pt-10 {
    --pt-10-bg: #09090b;
    --pt-10-s1: #121215;
    --pt-10-s2: #19191d;
    --pt-10-line: #26262b;
    --pt-10-ink: #f4f4f5;
    --pt-10-mut: #9c9ca6;
    --pt-10-acc: #d4d4d8;
    --pt-10-shadow: 0 1px 2px rgba(0, 0, 0, 0.6), 0 12px 32px -18px rgba(0, 0, 0, 0.8);
  }

  .pt-10:has(.pt-10__theme-input:checked) {
    --pt-10-bg: #fafafa;
    --pt-10-s1: #ffffff;
    --pt-10-s2: #f2f2f3;
    --pt-10-line: #e2e2e4;
    --pt-10-ink: #18181b;
    --pt-10-mut: #63636b;
    --pt-10-acc: #3f3f46;
    --pt-10-shadow: 0 1px 2px rgba(24, 24, 27, 0.05), 0 12px 32px -18px rgba(24, 24, 27, 0.25);
  }
}

@media (prefers-color-scheme: light) {
  .pt-10:has(.pt-10__theme-input:checked) {
    --pt-10-bg: #09090b;
    --pt-10-s1: #121215;
    --pt-10-s2: #19191d;
    --pt-10-line: #26262b;
    --pt-10-ink: #f4f4f5;
    --pt-10-mut: #9c9ca6;
    --pt-10-acc: #d4d4d8;
  }
}

@supports (color: oklch(0.4 0.01 280)) {
  .pt-10 {
    --pt-10-acc: oklch(0.38 0.01 285);
  }

  .pt-10:has(.pt-10__theme-input:checked) {
    --pt-10-acc: oklch(0.86 0.01 285);
  }

  @media (prefers-color-scheme: dark) {
    .pt-10 {
      --pt-10-acc: oklch(0.86 0.01 285);
    }

    .pt-10:has(.pt-10__theme-input:checked) {
      --pt-10-acc: oklch(0.38 0.01 285);
    }
  }
}

.pt-10__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.pt-10__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 9;
}

.pt-10__theme-input {
  position: absolute;
  opacity: 0;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
}

.pt-10__theme-label {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border: 1px solid var(--pt-10-line);
  border-radius: 0.6rem;
  background: var(--pt-10-s1);
  color: var(--pt-10-mut);
  cursor: pointer;
  box-shadow: var(--pt-10-shadow);
}

.pt-10__theme-label svg {
  inline-size: 1.1rem;
  block-size: 1.1rem;
}

.pt-10__theme-input:focus-visible + .pt-10__theme-label {
  outline: 2px solid var(--pt-10-acc);
  outline-offset: 2px;
}

.pt-10__stage {
  max-inline-size: 66rem;
  margin-inline: auto;
  padding: clamp(1.25rem, 4vw, 3rem) clamp(1rem, 4vw, 2.25rem) 3rem;
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1.4rem;
}

.pt-10__kicker {
  margin: 0 0 0.45rem;
  font-size: 0.73rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--pt-10-mut);
}

.pt-10__h {
  margin: 0 0 0.5rem;
  font-family: var(--pt-10-font-display);
  font-size: clamp(1.4rem, 4.4vw, 2.05rem);
  font-weight: 600;
  letter-spacing: -0.025em;
}

.pt-10__lede {
  margin: 0;
  max-inline-size: 42rem;
  color: var(--pt-10-mut);
  font-size: 0.94rem;
  text-wrap: pretty;
}

.pt-10__app {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 0;
  background: var(--pt-10-s1);
  border: 1px solid var(--pt-10-line);
  border-radius: 0.85rem;
  box-shadow: var(--pt-10-shadow);
  overflow: hidden;
}

@media (min-width: 44rem) {
  .pt-10__app {
    grid-template-columns: 12rem minmax(0, 1fr);
  }
}

.pt-10__side {
  min-inline-size: 0;
  padding: 0.9rem;
  background: var(--pt-10-s2);
  border-inline-end: 1px solid var(--pt-10-line);
}

.pt-10__side-t {
  margin: 0 0 0.8rem;
  font-family: var(--pt-10-font-display);
  font-size: 0.95rem;
  font-weight: 600;
  letter-spacing: -0.01em;
}

.pt-10__routes {
  display: grid;
  gap: 0.2rem;
}

.pt-10__radio {
  position: absolute;
  opacity: 0;
  inline-size: 1px;
  block-size: 1px;
}

.pt-10__nav {
  display: flex;
  align-items: center;
  gap: 0.55rem;
  min-block-size: 2.75rem;
  padding: 0.45rem 0.6rem;
  border-radius: 0.45rem;
  color: var(--pt-10-mut);
  font-size: 0.88rem;
  cursor: pointer;
}

.pt-10__nav svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
  flex: none;
}

.pt-10__nav:hover {
  background: var(--pt-10-s1);
  color: var(--pt-10-ink);
}

.pt-10__radio:checked + .pt-10__nav {
  background: var(--pt-10-s1);
  color: var(--pt-10-ink);
  font-weight: 600;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.08);
}

.pt-10__radio:focus-visible + .pt-10__nav {
  outline: 2px solid var(--pt-10-acc);
  outline-offset: 2px;
}

.pt-10__view {
  position: relative;
  overflow: hidden;
  min-inline-size: 0;
  min-block-size: 15.5rem;
}

.pt-10__veil {
  position: absolute;
  inset: 0;
  z-index: 3;
  background: var(--pt-10-bg);
  opacity: 0;
  pointer-events: none;
}

.pt-10__route {
  display: none;
  padding: clamp(1rem, 3vw, 1.6rem);
}

.pt-10__title {
  margin: 0 0 0.9rem;
  font-family: var(--pt-10-font-display);
  font-size: 1.15rem;
  font-weight: 600;
  letter-spacing: -0.015em;
}

.pt-10__cards {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 0.6rem;
  margin-block-end: 1rem;
}

@media (min-width: 30rem) {
  .pt-10__cards {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }
}

.pt-10__card {
  min-inline-size: 0;
  display: grid;
  gap: 0.15rem;
  padding: 0.75rem 0.85rem;
  background: var(--pt-10-s2);
  border-radius: 0.55rem;
}

.pt-10__card b {
  font-family: var(--pt-10-font-display);
  font-size: 1.25rem;
  font-weight: 600;
  font-variant-numeric: tabular-nums;
  letter-spacing: -0.02em;
}

.pt-10__card span {
  font-size: 0.73rem;
  color: var(--pt-10-mut);
}

.pt-10__text {
  margin: 0;
  max-inline-size: 38rem;
  font-size: 0.9rem;
  color: var(--pt-10-mut);
  text-wrap: pretty;
}

.pt-10__app:has(#pt-10-r1:checked) .pt-10__route--1,
.pt-10__app:has(#pt-10-r2:checked) .pt-10__route--2,
.pt-10__app:has(#pt-10-r3:checked) .pt-10__route--3 {
  display: block;
}

.pt-10__app:has(#pt-10-r1:checked) .pt-10__route--1 {
  animation: pt-10-in-1 var(--pt-10-dur) linear both;
}

.pt-10__app:has(#pt-10-r2:checked) .pt-10__route--2 {
  animation: pt-10-in-2 var(--pt-10-dur) linear both;
}

.pt-10__app:has(#pt-10-r3:checked) .pt-10__route--3 {
  animation: pt-10-in-3 var(--pt-10-dur) linear both;
}

.pt-10__app:has(#pt-10-r1:checked) .pt-10__veil {
  animation: pt-10-veil-1 var(--pt-10-dur) linear both;
}

.pt-10__app:has(#pt-10-r2:checked) .pt-10__veil {
  animation: pt-10-veil-2 var(--pt-10-dur) linear both;
}

.pt-10__app:has(#pt-10-r3:checked) .pt-10__veil {
  animation: pt-10-veil-3 var(--pt-10-dur) linear both;
}

@keyframes pt-10-in-1 {
  0%,
    45% {
    opacity: 0;
  }

  100% {
    opacity: 1;
  }
}

@keyframes pt-10-in-2 {
  0%,
    45% {
    opacity: 0;
  }

  100% {
    opacity: 1;
  }
}

@keyframes pt-10-in-3 {
  0%,
    45% {
    opacity: 0;
  }

  100% {
    opacity: 1;
  }
}

@keyframes pt-10-veil-1 {
  0% {
    opacity: 0;
  }

  40% {
    opacity: 0.9;
  }

  100% {
    opacity: 0;
  }
}

@keyframes pt-10-veil-2 {
  0% {
    opacity: 0;
  }

  40% {
    opacity: 0.9;
  }

  100% {
    opacity: 0;
  }
}

@keyframes pt-10-veil-3 {
  0% {
    opacity: 0;
  }

  40% {
    opacity: 0.9;
  }

  100% {
    opacity: 0;
  }
}

.pt-10__meter {
  margin: 0;
}

.pt-10__meter-cap {
  font-size: 0.72rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--pt-10-mut);
  margin-block-end: 0.5rem;
}

.pt-10__scale {
  position: relative;
  block-size: 0.5rem;
  border-radius: 999px;
  background: var(--pt-10-s2);
  overflow: hidden;
}

.pt-10__band {
  position: absolute;
  inset-block: 0;
  inset-inline-start: 30%;
  inline-size: 30%;
  background: var(--pt-10-line);
}

.pt-10__mark {
  position: absolute;
  inset-block: 0;
  inset-inline-start: 42%;
  inline-size: 2px;
  background: var(--pt-10-acc);
}

.pt-10__meter-t {
  margin: 0.5rem 0 0;
  font-size: 0.82rem;
  color: var(--pt-10-mut);
}

@media (prefers-reduced-motion: reduce) {
  .pt-10 {
    --pt-10-dur: 80ms;
  }

  @keyframes pt-10-veil-1 {
    0%,
        100% {
      opacity: 0;
    }
  }

  @keyframes pt-10-veil-2 {
    0%,
        100% {
      opacity: 0;
    }
  }

  @keyframes pt-10-veil-3 {
    0%,
        100% {
      opacity: 0;
    }
  }
}
```
