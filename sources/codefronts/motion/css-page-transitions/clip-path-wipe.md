---
source: "codefronts"
url: "https://codefronts.com/motion/css-page-transitions/clip-path-wipe/"
title: "Clip Path Wipe Page Transition Effect"
section: "motion"
category: "css-page-transitions"
category_name: "CSS Page Transitions"
description: "A clip-path wipe used as the overlay's cover and reveal: the panel is not moved, its visible shape is."
has_js: "false"
---

Here's a working CSS Page Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Clip Path Wipe Page Transition Effect
Source: https://codefronts.com/motion/css-page-transitions/clip-path-wipe/

A clip-path wipe used as the overlay's cover and reveal: the panel is not moved, its visible shape is. Cheap to composite, easy to angle, and the most versatile of the mask-based effects &mdash; a straight edge, a diagonal, or a chevron all come from editing one polygon. Three angles are switchable so the difference is visible rather than described.
## HTML
```html
<section class="pt-13" aria-labelledby="pt-13-h">
  <div class="pt-13__theme">
    <input class="pt-13__theme-input" type="checkbox" id="pt-13-theme">
    <label class="pt-13__theme-label" for="pt-13-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="pt-13__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="pt-13__stage">
    <header class="pt-13__bar">
      <p class="pt-13__brand">Talon</p>
      <nav class="pt-13__nav" aria-label="Site pages">
        <input class="pt-13__radio" type="radio" name="pt-13-r" id="pt-13-r1" checked>
        <label class="pt-13__link" for="pt-13-r1">Work</label>
        <input class="pt-13__radio" type="radio" name="pt-13-r" id="pt-13-r2">
        <label class="pt-13__link" for="pt-13-r2">Studio</label>
        <input class="pt-13__radio" type="radio" name="pt-13-r" id="pt-13-r3">
        <label class="pt-13__link" for="pt-13-r3">Contact</label>
      </nav>
    </header>

    <div class="pt-13__intro">
      <p class="pt-13__kicker">Page transitions / 13</p>
      <h2 class="pt-13__h" id="pt-13-h">Wipe the shape, not the panel</h2>
      <p class="pt-13__lede">Pages are DOM sections held by radio inputs and swapped in place. Change the angle to see how much of the character comes from one number.</p>
    </div>

    <div class="pt-13__angles" role="group" aria-label="Wipe angle">
      <input class="pt-13__aradio" type="radio" name="pt-13-a" id="pt-13-a1">
      <label class="pt-13__apill" for="pt-13-a1">Straight</label>
      <input class="pt-13__aradio" type="radio" name="pt-13-a" id="pt-13-a2" checked>
      <label class="pt-13__apill" for="pt-13-a2">Diagonal</label>
      <input class="pt-13__aradio" type="radio" name="pt-13-a" id="pt-13-a3">
      <label class="pt-13__apill" for="pt-13-a3">Steep</label>
    </div>

    <div class="pt-13__view">
      <div class="pt-13__wipe" aria-hidden="true"></div>
      <main class="pt-13__page pt-13__page--1">
        <p class="pt-13__eyebrow">Selected work</p>
        <h3 class="pt-13__title">Eleven projects, four disciplines</h3>
        <ul class="pt-13__list">
          <li><b>Basalt</b><span>identity, 2026</span></li>
          <li><b>Fern Editions</b><span>type design, 2025</span></li>
          <li><b>Orbit Transit</b><span>wayfinding, 2025</span></li>
        </ul>
      </main>
      <main class="pt-13__page pt-13__page--2">
        <p class="pt-13__eyebrow">Studio</p>
        <h3 class="pt-13__title">Nine people, one floor, no account managers</h3>
        <p class="pt-13__text">We take four projects at a time. Everyone who pitches the work also does the work.</p>
      </main>
      <main class="pt-13__page pt-13__page--3">
        <p class="pt-13__eyebrow">Contact</p>
        <h3 class="pt-13__title">Tell us what you are making</h3>
        <ul class="pt-13__list">
          <li><b>New work</b><span>studio at talon.design</span></li>
          <li><b>Press</b><span>Sam Rivera</span></li>
          <li><b>Studio</b><span>14 Bank Row, Lisbon</span></li>
        </ul>
      </main>
    </div>
  </div>
</section>
```
## CSS
```css
.pt-13 {
  --pt-13-bg: #0f0f0f;
  --pt-13-s1: #171717;
  --pt-13-s2: #202020;
  --pt-13-line: #2e2e2e;
  --pt-13-ink: #f5f5f5;
  --pt-13-mut: #9a9a9a;
  --pt-13-acc: #d6ff3f;
  --pt-13-skew: 22%;
  --pt-13-dur: 700ms;
  --pt-13-font-display: "Oswald", "Archivo Narrow", "Roboto Condensed", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--pt-13-bg);
  color: var(--pt-13-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.5;
}

.pt-13 *,
.pt-13 *::before,
.pt-13 *::after {
  box-sizing: border-box;
}

.pt-13:has(.pt-13__theme-input:checked) {
  --pt-13-bg: #fafafa;
  --pt-13-s1: #ffffff;
  --pt-13-s2: #f0f0f0;
  --pt-13-line: #dcdcdc;
  --pt-13-ink: #101010;
  --pt-13-mut: #5c5c5c;
  --pt-13-acc: #4a6b00;
}

@media (prefers-color-scheme: light) {
  .pt-13 {
    --pt-13-bg: #0f0f0f;
    --pt-13-s1: #171717;
    --pt-13-s2: #202020;
    --pt-13-line: #2e2e2e;
    --pt-13-ink: #f5f5f5;
    --pt-13-mut: #9a9a9a;
    --pt-13-acc: #d6ff3f;
  }

  .pt-13:has(.pt-13__theme-input:checked) {
    --pt-13-bg: #fafafa;
    --pt-13-s1: #ffffff;
    --pt-13-s2: #f0f0f0;
    --pt-13-line: #dcdcdc;
    --pt-13-ink: #101010;
    --pt-13-mut: #5c5c5c;
    --pt-13-acc: #4a6b00;
  }
}

@media (prefers-color-scheme: dark) {
  .pt-13:has(.pt-13__theme-input:checked) {
    --pt-13-bg: #fafafa;
    --pt-13-s1: #ffffff;
    --pt-13-s2: #f0f0f0;
    --pt-13-line: #dcdcdc;
    --pt-13-ink: #101010;
    --pt-13-mut: #5c5c5c;
    --pt-13-acc: #4a6b00;
  }
}

@supports (color: oklch(0.9 0.2 120)) {
  .pt-13 {
    --pt-13-acc: oklch(0.93 0.21 118);
  }

  .pt-13:has(.pt-13__theme-input:checked) {
    --pt-13-acc: oklch(0.5 0.15 118);
  }

  @media (prefers-color-scheme: dark) {
    .pt-13:has(.pt-13__theme-input:checked) {
      --pt-13-acc: oklch(0.5 0.15 118);
    }
  }
}

.pt-13__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.pt-13__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 9;
}

.pt-13__theme-input {
  position: absolute;
  opacity: 0;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
}

.pt-13__theme-label {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border: 0;
  background: var(--pt-13-s2);
  color: var(--pt-13-acc);
  cursor: pointer;
}

.pt-13__theme-label svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.pt-13__theme-input:focus-visible + .pt-13__theme-label {
  outline: 2px solid var(--pt-13-acc);
  outline-offset: 2px;
}

.pt-13__stage {
  max-inline-size: 68rem;
  margin-inline: auto;
  padding: clamp(1.25rem, 4vw, 3rem) clamp(1rem, 4vw, 2.25rem) 3rem;
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1.35rem;
}

.pt-13__bar {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.75rem 2rem;
  padding-block-end: 0.9rem;
  padding-inline-end: 3.5rem;
  border-block-end: 1px solid var(--pt-13-line);
}

.pt-13__brand {
  margin: 0;
  font-family: var(--pt-13-font-display);
  font-size: 1.25rem;
  font-weight: 600;
  letter-spacing: 0.14em;
  text-transform: uppercase;
}

.pt-13__nav {
  display: flex;
  flex-wrap: wrap;
  gap: 0.25rem;
  min-inline-size: 0;
}

.pt-13__radio,
.pt-13__aradio {
  position: absolute;
  opacity: 0;
  inline-size: 1px;
  block-size: 1px;
}

.pt-13__link {
  display: flex;
  align-items: center;
  min-block-size: 2.75rem;
  padding: 0.4rem 0.85rem;
  font-family: var(--pt-13-font-display);
  font-size: 0.9rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--pt-13-mut);
  cursor: pointer;
}

.pt-13__radio:checked + .pt-13__link {
  color: var(--pt-13-acc);
  box-shadow: inset 0 -2px 0 var(--pt-13-acc);
}

.pt-13__radio:focus-visible + .pt-13__link {
  outline: 2px solid var(--pt-13-acc);
  outline-offset: 2px;
}

.pt-13__kicker {
  margin: 0 0 0.45rem;
  font-family: var(--pt-13-font-display);
  font-size: 0.78rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--pt-13-mut);
}

.pt-13__h {
  margin: 0 0 0.5rem;
  font-family: var(--pt-13-font-display);
  font-size: clamp(1.6rem, 5.4vw, 2.6rem);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.01em;
}

.pt-13__lede {
  margin: 0;
  max-inline-size: 40rem;
  color: var(--pt-13-mut);
  font-size: 0.93rem;
  text-wrap: pretty;
}

.pt-13__angles {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
}

.pt-13__apill {
  min-block-size: 2.75rem;
  display: flex;
  align-items: center;
  padding: 0.4rem 0.9rem;
  background: var(--pt-13-s2);
  color: var(--pt-13-mut);
  font-family: var(--pt-13-font-display);
  font-size: 0.82rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  cursor: pointer;
}

.pt-13__aradio:checked + .pt-13__apill {
  background: var(--pt-13-acc);
  color: var(--pt-13-bg);
}

.pt-13__aradio:focus-visible + .pt-13__apill {
  outline: 2px solid var(--pt-13-acc);
  outline-offset: 2px;
}

.pt-13__view {
  position: relative;
  overflow: hidden;
  min-inline-size: 0;
  block-size: 18rem;
  background: var(--pt-13-s1);
}

.pt-13__wipe {
  position: absolute;
  inset: 0;
  z-index: 3;
  background: var(--pt-13-acc);
  pointer-events: none;
  clip-path: polygon(0 0, 0 0, 0 100%, 0 100%);
}

.pt-13__page {
  position: absolute;
  inset: 0;
  display: none;
  padding: clamp(1.1rem, 3.5vw, 2rem);
  align-content: center;
}

.pt-13__eyebrow {
  margin: 0 0 0.5rem;
  font-family: var(--pt-13-font-display);
  font-size: 0.76rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--pt-13-acc);
}

.pt-13__title {
  margin: 0 0 0.8rem;
  font-family: var(--pt-13-font-display);
  font-size: clamp(1.3rem, 4.4vw, 2rem);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.005em;
  max-inline-size: 30rem;
}

.pt-13__text {
  margin: 0;
  max-inline-size: 34rem;
  font-size: 0.95rem;
  color: var(--pt-13-mut);
  text-wrap: pretty;
}

.pt-13__list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 0.4rem;
  max-inline-size: 30rem;
}

.pt-13__list li {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  gap: 0.5rem;
  min-inline-size: 0;
  padding-block-end: 0.4rem;
  border-block-end: 1px solid var(--pt-13-line);
  font-size: 0.88rem;
}

.pt-13__list span {
  color: var(--pt-13-mut);
  font-size: 0.8rem;
}

.pt-13:has(#pt-13-a1:checked) {
  --pt-13-skew: 0%;
}

.pt-13:has(#pt-13-a2:checked) {
  --pt-13-skew: 22%;
}

.pt-13:has(#pt-13-a3:checked) {
  --pt-13-skew: 48%;
}

.pt-13__stage:has(#pt-13-r1:checked) .pt-13__page--1,
.pt-13__stage:has(#pt-13-r2:checked) .pt-13__page--2,
.pt-13__stage:has(#pt-13-r3:checked) .pt-13__page--3 {
  display: grid;
}

.pt-13__stage:has(#pt-13-r1:checked) .pt-13__page--1 {
  animation: pt-13-show-1 var(--pt-13-dur) linear both;
}

.pt-13__stage:has(#pt-13-r2:checked) .pt-13__page--2 {
  animation: pt-13-show-2 var(--pt-13-dur) linear both;
}

.pt-13__stage:has(#pt-13-r3:checked) .pt-13__page--3 {
  animation: pt-13-show-3 var(--pt-13-dur) linear both;
}

.pt-13__stage:has(#pt-13-r1:checked) .pt-13__wipe {
  animation: pt-13-wipe-1 var(--pt-13-dur) cubic-bezier(0.65, 0, 0.35, 1) both;
}

.pt-13__stage:has(#pt-13-r2:checked) .pt-13__wipe {
  animation: pt-13-wipe-2 var(--pt-13-dur) cubic-bezier(0.65, 0, 0.35, 1) both;
}

.pt-13__stage:has(#pt-13-r3:checked) .pt-13__wipe {
  animation: pt-13-wipe-3 var(--pt-13-dur) cubic-bezier(0.65, 0, 0.35, 1) both;
}

@keyframes pt-13-wipe-1 {
  0% {
    clip-path: polygon(0 0, 0 0, 0 100%, 0 100%);
  }

  45% {
    clip-path: polygon(0 0, calc(100% + var(--pt-13-skew)) 0, 100% 100%, 0 100%);
  }

  55% {
    clip-path: polygon(0 0, calc(100% + var(--pt-13-skew)) 0, 100% 100%, 0 100%);
  }

  100% {
    clip-path: polygon(100% 0, calc(100% + var(--pt-13-skew)) 0, 100% 100%, 100% 100%);
  }
}

@keyframes pt-13-wipe-2 {
  0% {
    clip-path: polygon(0 0, 0 0, 0 100%, 0 100%);
  }

  45% {
    clip-path: polygon(0 0, calc(100% + var(--pt-13-skew)) 0, 100% 100%, 0 100%);
  }

  55% {
    clip-path: polygon(0 0, calc(100% + var(--pt-13-skew)) 0, 100% 100%, 0 100%);
  }

  100% {
    clip-path: polygon(100% 0, calc(100% + var(--pt-13-skew)) 0, 100% 100%, 100% 100%);
  }
}

@keyframes pt-13-wipe-3 {
  0% {
    clip-path: polygon(0 0, 0 0, 0 100%, 0 100%);
  }

  45% {
    clip-path: polygon(0 0, calc(100% + var(--pt-13-skew)) 0, 100% 100%, 0 100%);
  }

  55% {
    clip-path: polygon(0 0, calc(100% + var(--pt-13-skew)) 0, 100% 100%, 0 100%);
  }

  100% {
    clip-path: polygon(100% 0, calc(100% + var(--pt-13-skew)) 0, 100% 100%, 100% 100%);
  }
}

@keyframes pt-13-show-1 {
  0%,
    50% {
    opacity: 0;
  }

  62%,
    100% {
    opacity: 1;
  }
}

@keyframes pt-13-show-2 {
  0%,
    50% {
    opacity: 0;
  }

  62%,
    100% {
    opacity: 1;
  }
}

@keyframes pt-13-show-3 {
  0%,
    50% {
    opacity: 0;
  }

  62%,
    100% {
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .pt-13 {
    --pt-13-dur: 140ms;
  }

  @keyframes pt-13-wipe-1 {
    0%,
        100% {
      clip-path: polygon(0 0, 0 0, 0 100%, 0 100%);
    }
  }

  @keyframes pt-13-wipe-2 {
    0%,
        100% {
      clip-path: polygon(0 0, 0 0, 0 100%, 0 100%);
    }
  }

  @keyframes pt-13-wipe-3 {
    0%,
        100% {
      clip-path: polygon(0 0, 0 0, 0 100%, 0 100%);
    }
  }

  @keyframes pt-13-show-1 {
    from {
      opacity: 0.5;
    }

    to {
      opacity: 1;
    }
  }

  @keyframes pt-13-show-2 {
    from {
      opacity: 0.5;
    }

    to {
      opacity: 1;
    }
  }

  @keyframes pt-13-show-3 {
    from {
      opacity: 0.5;
    }

    to {
      opacity: 1;
    }
  }
}
```
