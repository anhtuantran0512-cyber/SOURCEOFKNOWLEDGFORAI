---
source: "codefronts"
url: "https://codefronts.com/navigation/css-accordions/circular-arc/"
title: "Circular Dial Accordion — Conic-Gradient Progress Ring Toggles"
section: "navigation"
category: "css-accordions"
category_name: "CSS Accordions — Vertical & Horizontal"
description: "Every header wears a dial: a conic-gradient ring that sits empty when closed and sweeps a full 360° arc when its section opens, animated smoothly with a…"
has_js: "false"
---

Here's a working CSS Accordions — Vertical & Horizontal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Circular Dial Accordion — Conic-Gradient Progress Ring Toggles
Source: https://codefronts.com/navigation/css-accordions/circular-arc/

Every header wears a dial: a conic-gradient ring that sits empty when closed and sweeps a full 360° arc when its section opens, animated smoothly with a registered @property angle. Reads as 'sections you complete' — made for course syllabi, checklists and guided setups where progress is the mental model.
## HTML
```html
<section class="acc-25" aria-label="Circular dial progress accordion demo">
  <div class="acc-25__wrap">
    <p class="acc-25__kicker">Unit 3 · Typography</p>
    <h3 class="acc-25__title">Course syllabus</h3>
    <details class="acc-25__item" open>
      <summary class="acc-25__sum"><span class="acc-25__dial"><span class="acc-25__chev"></span></span><span class="acc-25__lab">Anatomy of a typeface<small>12 min · reading</small></span></summary>
      <div class="acc-25__body"><p>Baseline, x-height, ascenders, apertures — the vocabulary you need before any font pairing makes sense. Includes a labeled specimen to keep.</p></div>
    </details>
    <details class="acc-25__item">
      <summary class="acc-25__sum"><span class="acc-25__dial"><span class="acc-25__chev"></span></span><span class="acc-25__lab">Choosing a text face<small>18 min · exercise</small></span></summary>
      <div class="acc-25__body"><p>You'll set the same paragraph in six serifs and learn to SEE the difference between a book face and a display face at reading size.</p></div>
    </details>
    <details class="acc-25__item">
      <summary class="acc-25__sum"><span class="acc-25__dial"><span class="acc-25__chev"></span></span><span class="acc-25__lab">Scale &amp; rhythm<small>15 min · reading</small></span></summary>
      <div class="acc-25__body"><p>Modular scales, line-height ratios and why 45–75 characters per line survives every redesign. The math is three multiplications.</p></div>
    </details>
    <details class="acc-25__item">
      <summary class="acc-25__sum"><span class="acc-25__dial"><span class="acc-25__chev"></span></span><span class="acc-25__lab">Pairing under pressure<small>20 min · project</small></span></summary>
      <div class="acc-25__body"><p>A timed brief: pick two faces for a museum identity and defend the choice in three sentences. Peer review closes the unit.</p></div>
    </details>
  </div>
</section>
```
## CSS
```css
@property --acc-25-arc {
  syntax: "<angle>";
  inherits: false;
  initial-value: 0deg;
}

.acc-25,
.acc-25 *,
.acc-25 *::before,
.acc-25 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.acc-25 {
  --accent: oklch(0.6 0.15 60);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #faf7f0;
  padding: 44px 24px;
}

.acc-25__wrap {
  width: min(560px,100%);
  background: #fff;
  border-radius: 20px;
  padding: 36px 34px;
  box-shadow: 0 24px 60px -34px rgba(70,50,15,.3);
}

.acc-25__kicker {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--accent);
}

.acc-25__title {
  font-size: 25px;
  font-weight: 800;
  color: #2a2415;
  letter-spacing: -.02em;
  margin: 6px 0 16px;
}

.acc-25__item {
  border-top: 1px solid #efe9dc;
}

.acc-25__sum {
  list-style: none;
  display: flex;
  align-items: center;
  gap: 16px;
  min-height: 64px;
  padding: 10px 4px;
  cursor: pointer;
}

.acc-25__sum::-webkit-details-marker {
  display: none;
}

.acc-25__sum::marker {
  content: "";
}

.acc-25__dial {
  --acc-25-arc: 0deg;
  position: relative;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  flex: none;
  background: conic-gradient(var(--accent) calc(var(--acc-25-arc) - .5deg),#eae4d6 var(--acc-25-arc));
  transition: --acc-25-arc .6s cubic-bezier(.4,0,.2,1);
  display: grid;
  place-content: center;
}

.acc-25__dial::before {
  content: "";
  position: absolute;
  inset: 4px;
  border-radius: 50%;
  background: #fff;
}

.acc-25__item[open] .acc-25__dial {
  --acc-25-arc: 360deg;
}

.acc-25__chev {
  position: relative;
  z-index: 1;
  width: 8px;
  height: 8px;
  border-right: 2px solid #9b8d6f;
  border-bottom: 2px solid #9b8d6f;
  rotate: 45deg;
  translate: 0 -1.5px;
  transition: rotate .35s,border-color .3s;
}

.acc-25__item[open] .acc-25__chev {
  rotate: 225deg;
  translate: 0 1.5px;
  border-color: var(--accent);
}

.acc-25__lab {
  display: flex;
  flex-direction: column;
  gap: 2px;
  font-size: 16px;
  font-weight: 700;
  color: #2a2415;
}

.acc-25__lab small {
  font-size: 12px;
  font-weight: 600;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: #a29677;
}

.acc-25__item[open] .acc-25__lab {
  color: var(--accent);
}

.acc-25__body {
  padding: 0 4px 20px 60px;
  font-size: 14.5px;
  line-height: 1.65;
  color: #5b5138;
}

.acc-25__item[open] .acc-25__body {
  animation: acc-25-in .35s ease-out;
}

@keyframes acc-25-in {
  from {
    opacity: 0;
    translate: 0 -6px;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

.acc-25__sum:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
  border-radius: 10px;
}

@media (prefers-reduced-motion: reduce) {
  .acc-25__dial {
    transition: none;
  }

  .acc-25__chev {
    transition: none;
  }

  .acc-25__item[open] .acc-25__body {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the dial is a conic-gradient ring whose arc angle is a registered @property; details[open] transitions it 0deg→360deg so the ring sweeps closed like a timer. */
```
