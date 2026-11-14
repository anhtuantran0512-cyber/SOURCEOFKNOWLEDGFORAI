---
source: "codefronts"
url: "https://codefronts.com/navigation/css-accordions/paper-folded/"
title: "Paper Fold 3D Accordion — perspective + rotateX Unfolding Panels"
section: "navigation"
category: "css-accordions"
category_name: "CSS Accordions — Vertical & Horizontal"
description: "Sections unfold like a letter: each body starts folded flat against its header (rotateX(-90°) in real 3D perspective) and swings down open, with a gradient…"
has_js: "false"
---

Here's a working CSS Accordions — Vertical & Horizontal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Paper Fold 3D Accordion — perspective + rotateX Unfolding Panels
Source: https://codefronts.com/navigation/css-accordions/paper-folded/

Sections unfold like a letter: each body starts folded flat against its header (rotateX(-90°) in real 3D perspective) and swings down open, with a gradient shadow that sweeps off the paper as it flattens. The most physical open animation an accordion can have — for invitations, storytelling pages and product reveals.
## HTML
```html
<section class="acc-28" aria-label="Paper fold 3D accordion demo">
  <div class="acc-28__wrap">
    <p class="acc-28__kicker">You are invited</p>
    <h3 class="acc-28__title">Midsummer letterpress fair</h3>
    <details class="acc-28__item" open>
      <summary class="acc-28__sum">When &amp; where<span class="acc-28__fold-mark">⌄</span></summary>
      <div class="acc-28__hinge"><div class="acc-28__paper"><p>Saturday June 20th, 10am – dusk, in the old print works on Fanø. The building has no number; follow the smell of ink.</p></div></div>
    </details>
    <details class="acc-28__item">
      <summary class="acc-28__sum">What to bring<span class="acc-28__fold-mark">⌄</span></summary>
      <div class="acc-28__hinge"><div class="acc-28__paper"><p>Paper you love, cash for the swap tables, and an apron you don't. The presses are hand-cranked and generous with ink.</p></div></div>
    </details>
    <details class="acc-28__item">
      <summary class="acc-28__sum">RSVP<span class="acc-28__fold-mark">⌄</span></summary>
      <div class="acc-28__hinge"><div class="acc-28__paper"><p>Post a card to the workshop — yes, actual post — or sign the ledger at the studio. Capacity is whatever the fire marshal says it is.</p></div></div>
    </details>
  </div>
</section>
```
## CSS
```css
.acc-28,
.acc-28 *,
.acc-28 *::before,
.acc-28 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.acc-28 {
  --accent: oklch(0.5 0.12 30);
  font-family: Georgia,'Times New Roman',serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #efe9df;
  padding: 44px 24px;
}

.acc-28__wrap {
  width: min(520px,100%);
}

.acc-28__kicker {
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .22em;
  text-transform: uppercase;
  color: #9c8f7c;
  text-align: center;
}

.acc-28__title {
  font-size: 29px;
  font-weight: 700;
  color: #2e2618;
  letter-spacing: -.01em;
  text-align: center;
  margin: 8px 0 24px;
  font-style: italic;
}

.acc-28__item {
  perspective: 900px;
  overflow: hidden;
  margin-bottom: 12px;
}

.acc-28__sum {
  list-style: none;
  display: flex;
  align-items: center;
  justify-content: space-between;
  min-height: 56px;
  padding: 8px 20px;
  background: #fbf7ef;
  border: 1.5px solid #ddd2bf;
  font-size: 17px;
  font-weight: 700;
  color: #2e2618;
  cursor: pointer;
  transition: background .2s;
}

.acc-28__sum::-webkit-details-marker {
  display: none;
}

.acc-28__sum::marker {
  content: "";
}

.acc-28__sum:hover {
  background: #f5efe2;
}

.acc-28__item[open] .acc-28__sum {
  background: #f5efe2;
  border-bottom-style: dashed;
}

.acc-28__fold-mark {
  font-size: 18px;
  color: #a08d6f;
  transition: rotate .3s;
}

.acc-28__item[open] .acc-28__fold-mark {
  rotate: 180deg;
}

.acc-28__hinge {
  transform-origin: top;
}

.acc-28__item[open] .acc-28__hinge {
  animation: acc-28-unfold .55s cubic-bezier(.3,1.15,.4,1);
}

@keyframes acc-28-unfold {
  from {
    transform: rotateX(-90deg);
  }

  to {
    transform: rotateX(0);
  }
}

.acc-28__paper {
  position: relative;
  padding: 20px 22px 22px;
  background: #fdfaf3 repeating-linear-gradient(0deg,transparent 0 26px,#efe6d2 26px 27px);
  border: 1.5px solid #ddd2bf;
  border-top: none;
}

.acc-28__paper::before {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(rgba(60,40,10,.35),transparent 60%);
  pointer-events: none;
  opacity: 0;
}

.acc-28__item[open] .acc-28__paper::before {
  animation: acc-28-shadow .55s ease-out;
}

@keyframes acc-28-shadow {
  from {
    opacity: 1;
  }

  to {
    opacity: 0;
  }
}

.acc-28__paper p {
  font-size: 15.5px;
  line-height: 1.75;
  color: #4a3f2c;
}

.acc-28__sum:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .acc-28__item[open] .acc-28__hinge,
    .acc-28__item[open] .acc-28__paper::before {
    animation: none;
  }

  .acc-28__fold-mark {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the body is a top-hinged plane in real perspective: details[open] runs a rotateX(-90deg → 0) keyframe while a gradient shadow overlay fades out in sync, like paper unfolding into light. */
```
