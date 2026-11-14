---
source: "codefronts"
url: "https://codefronts.com/motion/css-page-transitions/ink-bleed/"
title: "Ink Bleed Mask Page Transition"
section: "motion"
category: "css-page-transitions"
category_name: "CSS Page Transitions"
description: "An organic reveal driven by mask-image: an inked panel spreads across the viewport from a point, holds while the route swaps, then contracts away toward the…"
has_js: "false"
---

Here's a working CSS Page Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Ink Bleed Mask Page Transition
Source: https://codefronts.com/motion/css-page-transitions/ink-bleed/

An organic reveal driven by mask-image: an inked panel spreads across the viewport from a point, holds while the route swaps, then contracts away toward the opposite corner. No script, no clip-path polygon &mdash; the shape is a soft radial mask, which is what makes the edge read as ink on paper rather than as a geometric wipe.
## HTML
```html
<section class="pt-16" aria-labelledby="pt-16-h">
  <div class="pt-16__theme">
    <input class="pt-16__theme-input" type="checkbox" id="pt-16-theme">
    <label class="pt-16__theme-label" for="pt-16-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="pt-16__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="pt-16__stage">
    <header class="pt-16__masthead">
      <p class="pt-16__imprint">Fern Editions</p>
      <h2 class="pt-16__h" id="pt-16-h">Printed slowly, on purpose</h2>
    </header>

    <div class="pt-16__view">
      <div class="pt-16__ink" aria-hidden="true"></div>

      <main class="pt-16__page pt-16__page--1">
        <p class="pt-16__eyebrow">The list</p>
        <h3 class="pt-16__h2">Four titles a year</h3>
        <p class="pt-16__lede">Letterpressed in Lisbon. Pages are DOM sections held by radio inputs and swapped in place &mdash; there is no router in this frame.</p>
        <p class="pt-16__meta">Spring list &middot; open for subscriptions</p>
      </main>
      <main class="pt-16__page pt-16__page--2">
        <p class="pt-16__eyebrow">The press</p>
        <h3 class="pt-16__h2">A Vandercook, two cases of Caslon, and time</h3>
        <p class="pt-16__lede">Every sheet is dampened, printed and dried before the next colour. The whole run takes eleven days and cannot be hurried.</p>
        <p class="pt-16__meta">Bank Row, Lisbon</p>
      </main>
      <main class="pt-16__page pt-16__page--3">
        <p class="pt-16__eyebrow">Subscribe</p>
        <h3 class="pt-16__h2">Four books, posted flat</h3>
        <p class="pt-16__lede">Subscribers receive each title as it comes off the press, with the proof sheet folded inside the back cover.</p>
        <p class="pt-16__meta">Enquiries &middot; Jordan Lee</p>
      </main>
    </div>

    <nav class="pt-16__nav" aria-label="Pages">
      <input class="pt-16__radio" type="radio" name="pt-16-r" id="pt-16-r1" checked>
      <label class="pt-16__link" for="pt-16-r1">The list</label>
      <input class="pt-16__radio" type="radio" name="pt-16-r" id="pt-16-r2">
      <label class="pt-16__link" for="pt-16-r2">The press</label>
      <input class="pt-16__radio" type="radio" name="pt-16-r" id="pt-16-r3">
      <label class="pt-16__link" for="pt-16-r3">Subscribe</label>
    </nav>

    <p class="pt-16__note">Page transitions / 16 &mdash; the ink spreads from the lower left, holds while the page swaps, then lifts toward the upper right. Every mask property is declared twice: <code>-webkit-mask</code> first, unprefixed second.</p>
  </div>
</section>
```
## CSS
```css
.pt-16 {
  --pt-16-bg: #f6f1e7;
  --pt-16-ink: #16130f;
  --pt-16-mut: #6a6154;
  --pt-16-acc: #1f4d3f;
  --pt-16-panel: #16130f;
  --pt-16-dur: 900ms;
  --pt-16-font-display: Baskerville, "Libre Baskerville", "Times New Roman", serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--pt-16-bg);
  color: var(--pt-16-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.6;
}

.pt-16 *,
.pt-16 *::before,
.pt-16 *::after {
  box-sizing: border-box;
}

.pt-16:has(.pt-16__theme-input:checked) {
  --pt-16-bg: #12100d;
  --pt-16-ink: #f4efe4;
  --pt-16-mut: #a79d8c;
  --pt-16-acc: #7fc0a8;
  --pt-16-panel: #f4efe4;
}

@media (prefers-color-scheme: dark) {
  .pt-16 {
    --pt-16-bg: #12100d;
    --pt-16-ink: #f4efe4;
    --pt-16-mut: #a79d8c;
    --pt-16-acc: #7fc0a8;
    --pt-16-panel: #f4efe4;
  }

  .pt-16:has(.pt-16__theme-input:checked) {
    --pt-16-bg: #f6f1e7;
    --pt-16-ink: #16130f;
    --pt-16-mut: #6a6154;
    --pt-16-acc: #1f4d3f;
    --pt-16-panel: #16130f;
  }
}

@media (prefers-color-scheme: light) {
  .pt-16:has(.pt-16__theme-input:checked) {
    --pt-16-bg: #12100d;
    --pt-16-ink: #f4efe4;
    --pt-16-mut: #a79d8c;
    --pt-16-acc: #7fc0a8;
    --pt-16-panel: #f4efe4;
  }
}

@supports (color: oklch(0.4 0.08 160)) {
  .pt-16 {
    --pt-16-acc: oklch(0.4 0.08 162);
  }

  .pt-16:has(.pt-16__theme-input:checked) {
    --pt-16-acc: oklch(0.79 0.09 162);
  }

  @media (prefers-color-scheme: dark) {
    .pt-16 {
      --pt-16-acc: oklch(0.79 0.09 162);
    }

    .pt-16:has(.pt-16__theme-input:checked) {
      --pt-16-acc: oklch(0.4 0.08 162);
    }
  }
}

.pt-16__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.pt-16__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 9;
}

.pt-16__theme-input {
  position: absolute;
  opacity: 0;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
}

.pt-16__theme-label {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border: 0;
  background: transparent;
  color: var(--pt-16-mut);
  cursor: pointer;
}

.pt-16__theme-label svg {
  inline-size: 1.2rem;
  block-size: 1.2rem;
}

.pt-16__theme-label:hover {
  color: var(--pt-16-ink);
}

.pt-16__theme-input:focus-visible + .pt-16__theme-label {
  outline: 2px solid var(--pt-16-acc);
  outline-offset: 2px;
}

.pt-16__stage {
  max-inline-size: 62rem;
  margin-inline: auto;
  padding: clamp(1.5rem, 5vw, 3.5rem) clamp(1rem, 5vw, 2.5rem) 3rem;
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1.5rem;
}

.pt-16__view {
  position: relative;
  overflow: hidden;
  min-inline-size: 0;
  min-block-size: 20rem;
}

.pt-16__ink {
  position: absolute;
  inset: -10%;
  z-index: 3;
  background: var(--pt-16-panel);
  pointer-events: none;
  opacity: 0;
  -webkit-mask-image: radial-gradient(circle, #000 38%, rgba(0, 0, 0, 0.55) 58%, transparent 72%);
  mask-image: radial-gradient(circle, #000 38%, rgba(0, 0, 0, 0.55) 58%, transparent 72%);
  -webkit-mask-repeat: no-repeat;
  mask-repeat: no-repeat;
  -webkit-mask-position: 18% 82%;
  mask-position: 18% 82%;
  -webkit-mask-size: 0% 0%;
  mask-size: 0% 0%;
}

.pt-16__masthead {
  border-block-end: 1px solid var(--pt-16-mut);
  padding-block-end: 0.9rem;
}

.pt-16__imprint {
  margin: 0 0 0.5rem;
  font-size: 0.74rem;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--pt-16-acc);
}

.pt-16__page {
  display: none;
  padding: clamp(1rem, 3vw, 2rem) 0;
}

.pt-16__eyebrow {
  margin: 0 0 0.8rem;
  font-size: 0.74rem;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--pt-16-acc);
}

.pt-16__h {
  margin: 0;
  font-family: var(--pt-16-font-display);
  font-size: clamp(1.5rem, 5vw, 2.4rem);
  font-weight: 400;
  line-height: 1.1;
  letter-spacing: -0.015em;
}

.pt-16__h2 {
  margin: 0 0 0.9rem;
  font-family: var(--pt-16-font-display);
  font-size: clamp(1.7rem, 6vw, 3rem);
  font-weight: 400;
  line-height: 1.08;
  letter-spacing: -0.015em;
  max-inline-size: 30rem;
}

.pt-16__lede {
  margin: 0 0 1.1rem;
  max-inline-size: 34rem;
  font-size: 1rem;
  color: var(--pt-16-mut);
  text-wrap: pretty;
}

.pt-16__meta {
  margin: 0;
  font-family: var(--pt-16-font-display);
  font-size: 0.92rem;
  font-style: italic;
  color: var(--pt-16-ink);
}

.pt-16__nav {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem 1.5rem;
  border-block-start: 1px solid var(--pt-16-mut);
  padding-block-start: 0.9rem;
}

.pt-16__radio {
  position: absolute;
  opacity: 0;
  inline-size: 1px;
  block-size: 1px;
}

.pt-16__link {
  min-block-size: 2.75rem;
  display: flex;
  align-items: center;
  font-family: var(--pt-16-font-display);
  font-size: 1rem;
  color: var(--pt-16-mut);
  cursor: pointer;
}

.pt-16__radio:checked + .pt-16__link {
  color: var(--pt-16-ink);
  text-decoration: underline;
  text-underline-offset: 0.3em;
}

.pt-16__radio:focus-visible + .pt-16__link {
  outline: 2px solid var(--pt-16-acc);
  outline-offset: 3px;
}

.pt-16__note {
  margin: 0;
  max-inline-size: 42rem;
  font-size: 0.82rem;
  color: var(--pt-16-mut);
  text-wrap: pretty;
}

.pt-16__note code {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.86em;
}

.pt-16__stage:has(#pt-16-r1:checked) .pt-16__page--1,
.pt-16__stage:has(#pt-16-r2:checked) .pt-16__page--2,
.pt-16__stage:has(#pt-16-r3:checked) .pt-16__page--3 {
  display: block;
}

.pt-16__stage:has(#pt-16-r1:checked) .pt-16__page--1 {
  animation: pt-16-show-1 var(--pt-16-dur) linear both;
}

.pt-16__stage:has(#pt-16-r2:checked) .pt-16__page--2 {
  animation: pt-16-show-2 var(--pt-16-dur) linear both;
}

.pt-16__stage:has(#pt-16-r3:checked) .pt-16__page--3 {
  animation: pt-16-show-3 var(--pt-16-dur) linear both;
}

.pt-16__stage:has(#pt-16-r1:checked) .pt-16__ink {
  animation: pt-16-bleed-1 var(--pt-16-dur) cubic-bezier(0.45, 0.05, 0.3, 1) both;
}

.pt-16__stage:has(#pt-16-r2:checked) .pt-16__ink {
  animation: pt-16-bleed-2 var(--pt-16-dur) cubic-bezier(0.45, 0.05, 0.3, 1) both;
}

.pt-16__stage:has(#pt-16-r3:checked) .pt-16__ink {
  animation: pt-16-bleed-3 var(--pt-16-dur) cubic-bezier(0.45, 0.05, 0.3, 1) both;
}

@keyframes pt-16-bleed-1 {
  0% {
    opacity: 1;
    -webkit-mask-size: 0% 0%;
    mask-size: 0% 0%;
    -webkit-mask-position: 18% 82%;
    mask-position: 18% 82%;
  }

  42%,
    54% {
    opacity: 1;
    -webkit-mask-size: 340% 340%;
    mask-size: 340% 340%;
    -webkit-mask-position: 18% 82%;
    mask-position: 18% 82%;
  }

  99% {
    opacity: 1;
    -webkit-mask-size: 0% 0%;
    mask-size: 0% 0%;
    -webkit-mask-position: 86% 14%;
    mask-position: 86% 14%;
  }

  100% {
    opacity: 0;
    -webkit-mask-size: 0% 0%;
    mask-size: 0% 0%;
  }
}

@keyframes pt-16-bleed-2 {
  0% {
    opacity: 1;
    -webkit-mask-size: 0% 0%;
    mask-size: 0% 0%;
    -webkit-mask-position: 18% 82%;
    mask-position: 18% 82%;
  }

  42%,
    54% {
    opacity: 1;
    -webkit-mask-size: 340% 340%;
    mask-size: 340% 340%;
    -webkit-mask-position: 18% 82%;
    mask-position: 18% 82%;
  }

  99% {
    opacity: 1;
    -webkit-mask-size: 0% 0%;
    mask-size: 0% 0%;
    -webkit-mask-position: 86% 14%;
    mask-position: 86% 14%;
  }

  100% {
    opacity: 0;
    -webkit-mask-size: 0% 0%;
    mask-size: 0% 0%;
  }
}

@keyframes pt-16-bleed-3 {
  0% {
    opacity: 1;
    -webkit-mask-size: 0% 0%;
    mask-size: 0% 0%;
    -webkit-mask-position: 18% 82%;
    mask-position: 18% 82%;
  }

  42%,
    54% {
    opacity: 1;
    -webkit-mask-size: 340% 340%;
    mask-size: 340% 340%;
    -webkit-mask-position: 18% 82%;
    mask-position: 18% 82%;
  }

  99% {
    opacity: 1;
    -webkit-mask-size: 0% 0%;
    mask-size: 0% 0%;
    -webkit-mask-position: 86% 14%;
    mask-position: 86% 14%;
  }

  100% {
    opacity: 0;
    -webkit-mask-size: 0% 0%;
    mask-size: 0% 0%;
  }
}

@keyframes pt-16-show-1 {
  0%,
    46% {
    opacity: 0;
  }

  58%,
    100% {
    opacity: 1;
  }
}

@keyframes pt-16-show-2 {
  0%,
    46% {
    opacity: 0;
  }

  58%,
    100% {
    opacity: 1;
  }
}

@keyframes pt-16-show-3 {
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
  .pt-16 {
    --pt-16-dur: 160ms;
  }

  @keyframes pt-16-bleed-1 {
    0%,
        100% {
      opacity: 0;
    }
  }

  @keyframes pt-16-bleed-2 {
    0%,
        100% {
      opacity: 0;
    }
  }

  @keyframes pt-16-bleed-3 {
    0%,
        100% {
      opacity: 0;
    }
  }

  @keyframes pt-16-show-1 {
    from {
      opacity: 0.5;
    }

    to {
      opacity: 1;
    }
  }

  @keyframes pt-16-show-2 {
    from {
      opacity: 0.5;
    }

    to {
      opacity: 1;
    }
  }

  @keyframes pt-16-show-3 {
    from {
      opacity: 0.5;
    }

    to {
      opacity: 1;
    }
  }
}
```
