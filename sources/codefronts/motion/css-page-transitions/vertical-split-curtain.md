---
source: "codefronts"
url: "https://codefronts.com/motion/css-page-transitions/vertical-split-curtain/"
title: "Split Curtain Page Transition Effect"
section: "motion"
category: "css-page-transitions"
category_name: "CSS Page Transitions"
description: "Two panels close from the edges, meet in the middle while the route swaps, then part again."
has_js: "false"
---

Here's a working CSS Page Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Split Curtain Page Transition Effect
Source: https://codefronts.com/motion/css-page-transitions/vertical-split-curtain/

Two panels close from the edges, meet in the middle while the route swaps, then part again. It is the most theatrical effect here and the one most easily overdone &mdash; the whole thing has to stay under about half a second or a navigation starts to feel like a stage production. Built with radios and two @keyframes, no script.
## HTML
```html
<section class="pt-18" aria-labelledby="pt-18-h">
  <div class="pt-18__theme">
    <input class="pt-18__theme-input" type="checkbox" id="pt-18-theme">
    <label class="pt-18__theme-label" for="pt-18-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="pt-18__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="pt-18__stage">
    <header class="pt-18__head">
      <p class="pt-18__kicker">Page transitions / 18</p>
      <h2 class="pt-18__h" id="pt-18-h">Panels close, panels part</h2>
      <p class="pt-18__lede">A master-detail pair. Details are DOM sections held by radio inputs and swapped while the panels are shut &mdash; no script, no navigation.</p>
    </header>

    <div class="pt-18__split">
      <nav class="pt-18__list" aria-label="Programme">
        <input class="pt-18__radio" type="radio" name="pt-18-r" id="pt-18-r1" checked>
        <label class="pt-18__row" for="pt-18-r1"><b>Thu 14</b><span>Meridian Quartet</span></label>
        <input class="pt-18__radio" type="radio" name="pt-18-r" id="pt-18-r2">
        <label class="pt-18__row" for="pt-18-r2"><b>Fri 15</b><span>Nova Ensemble</span></label>
        <input class="pt-18__radio" type="radio" name="pt-18-r" id="pt-18-r3">
        <label class="pt-18__row" for="pt-18-r3"><b>Sat 16</b><span>Talon Solo</span></label>
      </nav>

      <div class="pt-18__view">
        <div class="pt-18__panel pt-18__panel--l" aria-hidden="true"></div>
        <div class="pt-18__panel pt-18__panel--r" aria-hidden="true"></div>
        <main class="pt-18__detail pt-18__detail--1">
          <p class="pt-18__eyebrow">Thursday 14, 19:30</p>
          <h3 class="pt-18__title">Meridian Quartet</h3>
          <p class="pt-18__text">Three works written for the hall, played without an interval. Doors at 19:00.</p>
          <p class="pt-18__price">From 18</p>
        </main>
        <main class="pt-18__detail pt-18__detail--2">
          <p class="pt-18__eyebrow">Friday 15, 20:00</p>
          <h3 class="pt-18__title">Nova Ensemble</h3>
          <p class="pt-18__text">Eleven players, one amplified room. Late seating between pieces only.</p>
          <p class="pt-18__price">From 24</p>
        </main>
        <main class="pt-18__detail pt-18__detail--3">
          <p class="pt-18__eyebrow">Saturday 16, 18:00</p>
          <h3 class="pt-18__title">Talon Solo</h3>
          <p class="pt-18__text">A single instrument and a long programme. Standing tickets released on the day.</p>
          <p class="pt-18__price">From 12</p>
        </main>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.pt-18 {
  --pt-18-bg: #f7f5f0;
  --pt-18-s1: #ffffff;
  --pt-18-s2: #edeae2;
  --pt-18-line: #d8d3c7;
  --pt-18-ink: #14120f;
  --pt-18-mut: #66604f;
  --pt-18-acc: #a51f2e;
  --pt-18-dur: 460ms;
  --pt-18-font-display: "Oswald", "Archivo Narrow", "Haettenschweiler", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--pt-18-bg);
  color: var(--pt-18-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.5;
}

.pt-18 *,
.pt-18 *::before,
.pt-18 *::after {
  box-sizing: border-box;
}

.pt-18:has(.pt-18__theme-input:checked) {
  --pt-18-bg: #100f0d;
  --pt-18-s1: #181613;
  --pt-18-s2: #201d19;
  --pt-18-line: #322d26;
  --pt-18-ink: #f4f1ea;
  --pt-18-mut: #a49c8a;
  --pt-18-acc: #f0616f;
}

@media (prefers-color-scheme: dark) {
  .pt-18 {
    --pt-18-bg: #100f0d;
    --pt-18-s1: #181613;
    --pt-18-s2: #201d19;
    --pt-18-line: #322d26;
    --pt-18-ink: #f4f1ea;
    --pt-18-mut: #a49c8a;
    --pt-18-acc: #f0616f;
  }

  .pt-18:has(.pt-18__theme-input:checked) {
    --pt-18-bg: #f7f5f0;
    --pt-18-s1: #ffffff;
    --pt-18-s2: #edeae2;
    --pt-18-line: #d8d3c7;
    --pt-18-ink: #14120f;
    --pt-18-mut: #66604f;
    --pt-18-acc: #a51f2e;
  }
}

@media (prefers-color-scheme: light) {
  .pt-18:has(.pt-18__theme-input:checked) {
    --pt-18-bg: #100f0d;
    --pt-18-s1: #181613;
    --pt-18-s2: #201d19;
    --pt-18-line: #322d26;
    --pt-18-ink: #f4f1ea;
    --pt-18-mut: #a49c8a;
    --pt-18-acc: #f0616f;
  }
}

@supports (color: oklch(0.45 0.18 20)) {
  .pt-18 {
    --pt-18-acc: oklch(0.45 0.18 22);
  }

  .pt-18:has(.pt-18__theme-input:checked) {
    --pt-18-acc: oklch(0.72 0.16 18);
  }

  @media (prefers-color-scheme: dark) {
    .pt-18 {
      --pt-18-acc: oklch(0.72 0.16 18);
    }

    .pt-18:has(.pt-18__theme-input:checked) {
      --pt-18-acc: oklch(0.45 0.18 22);
    }
  }
}

.pt-18__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.pt-18__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 9;
}

.pt-18__theme-input {
  position: absolute;
  opacity: 0;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
}

.pt-18__theme-label {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border: 0;
  background: transparent;
  color: var(--pt-18-acc);
  cursor: pointer;
}

.pt-18__theme-label svg {
  inline-size: 1.2rem;
  block-size: 1.2rem;
}

.pt-18__theme-input:focus-visible + .pt-18__theme-label {
  outline: 2px solid var(--pt-18-acc);
  outline-offset: 2px;
}

.pt-18__stage {
  max-inline-size: 64rem;
  margin-inline: auto;
  padding: clamp(1.25rem, 4vw, 3rem) clamp(1rem, 4vw, 2.25rem) 3rem;
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1.5rem;
}

.pt-18__kicker {
  margin: 0 0 0.45rem;
  font-family: var(--pt-18-font-display);
  font-size: 0.76rem;
  letter-spacing: 0.24em;
  text-transform: uppercase;
  color: var(--pt-18-acc);
}

.pt-18__h {
  margin: 0 0 0.5rem;
  font-family: var(--pt-18-font-display);
  font-size: clamp(1.6rem, 5.2vw, 2.5rem);
  font-weight: 500;
  letter-spacing: 0.02em;
  text-transform: uppercase;
}

.pt-18__lede {
  margin: 0;
  max-inline-size: 40rem;
  color: var(--pt-18-mut);
  font-size: 0.93rem;
  text-wrap: pretty;
}

.pt-18__split {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1rem;
}

@media (min-width: 48rem) {
  .pt-18__split {
    grid-template-columns: minmax(0, 15rem) minmax(0, 1fr);
  }
}

.pt-18__list {
  min-inline-size: 0;
  display: grid;
  gap: 0.25rem;
  align-content: start;
}

.pt-18__radio {
  position: absolute;
  opacity: 0;
  inline-size: 1px;
  block-size: 1px;
}

.pt-18__row {
  min-block-size: 2.75rem;
  display: grid;
  grid-template-columns: 3.5rem minmax(0, 1fr);
  gap: 0.6rem;
  align-items: center;
  padding: 0.6rem 0.2rem;
  border-block-end: 1px solid var(--pt-18-line);
  cursor: pointer;
  color: var(--pt-18-mut);
}

.pt-18__row b {
  font-family: var(--pt-18-font-display);
  font-size: 0.9rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
}

.pt-18__row span {
  font-size: 0.9rem;
  min-inline-size: 0;
}

.pt-18__radio:checked + .pt-18__row {
  color: var(--pt-18-ink);
}

.pt-18__radio:checked + .pt-18__row b {
  color: var(--pt-18-acc);
}

.pt-18__radio:focus-visible + .pt-18__row {
  outline: 2px solid var(--pt-18-acc);
  outline-offset: 2px;
}

.pt-18__view {
  position: relative;
  overflow: hidden;
  min-inline-size: 0;
  block-size: 15rem;
  background: var(--pt-18-s1);
}

.pt-18__panel {
  position: absolute;
  inset-block: 0;
  inline-size: 51%;
  z-index: 3;
  background: var(--pt-18-acc);
  pointer-events: none;
}

.pt-18__panel--l {
  inset-inline-start: 0;
  transform: translateX(-101%);
}

.pt-18__panel--r {
  inset-inline-end: 0;
  transform: translateX(101%);
}

.pt-18__detail {
  position: absolute;
  inset: 0;
  display: none;
  padding: clamp(1.1rem, 3.5vw, 2rem);
  align-content: center;
}

.pt-18__eyebrow {
  margin: 0 0 0.5rem;
  font-family: var(--pt-18-font-display);
  font-size: 0.78rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--pt-18-mut);
}

.pt-18__title {
  margin: 0 0 0.7rem;
  font-family: var(--pt-18-font-display);
  font-size: clamp(1.5rem, 5vw, 2.2rem);
  font-weight: 500;
  letter-spacing: 0.02em;
  text-transform: uppercase;
}

.pt-18__text {
  margin: 0 0 0.9rem;
  max-inline-size: 30rem;
  font-size: 0.93rem;
  color: var(--pt-18-mut);
  text-wrap: pretty;
}

.pt-18__price {
  margin: 0;
  font-family: var(--pt-18-font-display);
  font-size: 1.05rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--pt-18-acc);
}

.pt-18__split:has(#pt-18-r1:checked) .pt-18__detail--1,
.pt-18__split:has(#pt-18-r2:checked) .pt-18__detail--2,
.pt-18__split:has(#pt-18-r3:checked) .pt-18__detail--3 {
  display: grid;
}

.pt-18__split:has(#pt-18-r1:checked) .pt-18__detail--1 {
  animation: pt-18-show-1 var(--pt-18-dur) linear both;
}

.pt-18__split:has(#pt-18-r2:checked) .pt-18__detail--2 {
  animation: pt-18-show-2 var(--pt-18-dur) linear both;
}

.pt-18__split:has(#pt-18-r3:checked) .pt-18__detail--3 {
  animation: pt-18-show-3 var(--pt-18-dur) linear both;
}

.pt-18__split:has(#pt-18-r1:checked) .pt-18__panel--l {
  animation: pt-18-left-1 var(--pt-18-dur) cubic-bezier(0.5, 0, 0.4, 1) both;
}

.pt-18__split:has(#pt-18-r2:checked) .pt-18__panel--l {
  animation: pt-18-left-2 var(--pt-18-dur) cubic-bezier(0.5, 0, 0.4, 1) both;
}

.pt-18__split:has(#pt-18-r3:checked) .pt-18__panel--l {
  animation: pt-18-left-3 var(--pt-18-dur) cubic-bezier(0.5, 0, 0.4, 1) both;
}

.pt-18__split:has(#pt-18-r1:checked) .pt-18__panel--r {
  animation: pt-18-right-1 var(--pt-18-dur) cubic-bezier(0.5, 0, 0.4, 1) both;
}

.pt-18__split:has(#pt-18-r2:checked) .pt-18__panel--r {
  animation: pt-18-right-2 var(--pt-18-dur) cubic-bezier(0.5, 0, 0.4, 1) both;
}

.pt-18__split:has(#pt-18-r3:checked) .pt-18__panel--r {
  animation: pt-18-right-3 var(--pt-18-dur) cubic-bezier(0.5, 0, 0.4, 1) both;
}

@keyframes pt-18-left-1 {
  0% {
    transform: translateX(-101%);
  }

  42%,
    56% {
    transform: translateX(0);
  }

  100% {
    transform: translateX(-101%);
  }
}

@keyframes pt-18-left-2 {
  0% {
    transform: translateX(-101%);
  }

  42%,
    56% {
    transform: translateX(0);
  }

  100% {
    transform: translateX(-101%);
  }
}

@keyframes pt-18-left-3 {
  0% {
    transform: translateX(-101%);
  }

  42%,
    56% {
    transform: translateX(0);
  }

  100% {
    transform: translateX(-101%);
  }
}

@keyframes pt-18-right-1 {
  0% {
    transform: translateX(101%);
  }

  42%,
    56% {
    transform: translateX(0);
  }

  100% {
    transform: translateX(101%);
  }
}

@keyframes pt-18-right-2 {
  0% {
    transform: translateX(101%);
  }

  42%,
    56% {
    transform: translateX(0);
  }

  100% {
    transform: translateX(101%);
  }
}

@keyframes pt-18-right-3 {
  0% {
    transform: translateX(101%);
  }

  42%,
    56% {
    transform: translateX(0);
  }

  100% {
    transform: translateX(101%);
  }
}

@keyframes pt-18-show-1 {
  0%,
    46% {
    opacity: 0;
  }

  58%,
    100% {
    opacity: 1;
  }
}

@keyframes pt-18-show-2 {
  0%,
    46% {
    opacity: 0;
  }

  58%,
    100% {
    opacity: 1;
  }
}

@keyframes pt-18-show-3 {
  0%,
    46% {
    opacity: 0;
  }

  58%,
    100% {
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .pt-18 {
    --pt-18-dur: 120ms;
  }

  @keyframes pt-18-left-1 {
    0%,
        100% {
      transform: translateX(-101%);
    }
  }

  @keyframes pt-18-left-2 {
    0%,
        100% {
      transform: translateX(-101%);
    }
  }

  @keyframes pt-18-left-3 {
    0%,
        100% {
      transform: translateX(-101%);
    }
  }

  @keyframes pt-18-right-1 {
    0%,
        100% {
      transform: translateX(101%);
    }
  }

  @keyframes pt-18-right-2 {
    0%,
        100% {
      transform: translateX(101%);
    }
  }

  @keyframes pt-18-right-3 {
    0%,
        100% {
      transform: translateX(101%);
    }
  }

  @keyframes pt-18-show-1 {
    from {
      opacity: 0.5;
    }

    to {
      opacity: 1;
    }
  }

  @keyframes pt-18-show-2 {
    from {
      opacity: 0.5;
    }

    to {
      opacity: 1;
    }
  }

  @keyframes pt-18-show-3 {
    from {
      opacity: 0.5;
    }

    to {
      opacity: 1;
    }
  }
}
```
