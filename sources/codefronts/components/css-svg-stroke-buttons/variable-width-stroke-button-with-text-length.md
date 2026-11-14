---
source: "codefronts"
url: "https://codefronts.com/components/css-svg-stroke-buttons/variable-width-stroke-button-with-text-length/"
title: "Variable Width Stroke Button with Text Length"
section: "components"
category: "css-svg-stroke-buttons"
category_name: "CSS SVG Stroke Buttons"
description: "A weight ladder: six labels from three characters to thirty-five, each with its own stroke weight, dash rhythm and draw duration computed from the character…"
has_js: "true"
---

Here's a working CSS SVG Stroke Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Variable Width Stroke Button with Text Length
Source: https://codefronts.com/components/css-svg-stroke-buttons/variable-width-stroke-button-with-text-length/

A weight ladder: six labels from three characters to thirty-five, each with its own stroke weight, dash rhythm and draw duration computed from the character count. The bottom pair is the control — the same two extremes at a fixed 2px — so you can see the optical problem the ladder solves rather than take it on trust.
## HTML
```html
<section class="svgb-20">
  <input class="svgb-20__ti" type="checkbox" id="svgb-20-theme">
  <label class="svgb-20__toggle" for="svgb-20-theme">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="svgb-20__sr">Switch colour scheme</span>
  </label>
  <div class="svgb-20__stage">
    <div class="svgb-20__sheet">
      <div class="svgb-20__head">
        <h1 class="svgb-20__title">Weight<br>Ladder</h1>
        <p class="svgb-20__sub">stroke-width: clamp(1.5px, 1.1px + chars &times; 0.055px, 3px)</p>
      </div>

      <ol class="svgb-20__ladder">
        <li class="svgb-20__rung">
          <span class="svgb-20__n">03</span>
          <button class="svgb-20__btn" type="button" data-chars="3" style="--svgb-20-chars: 3">
            <svg class="svgb-20__frame" aria-hidden="true"><rect class="svgb-20__ink" data-chars="3" pathLength="1" vector-effect="non-scaling-stroke"/></svg>
            <span class="svgb-20__label">Buy</span>
          </button>
          <span class="svgb-20__w">1.5px</span>
        </li>
        <li class="svgb-20__rung">
          <span class="svgb-20__n">08</span>
          <button class="svgb-20__btn" type="button" data-chars="8" style="--svgb-20-chars: 8">
            <svg class="svgb-20__frame" aria-hidden="true"><rect class="svgb-20__ink" data-chars="8" pathLength="1" vector-effect="non-scaling-stroke"/></svg>
            <span class="svgb-20__label">Add note</span>
          </button>
          <span class="svgb-20__w">1.5px</span>
        </li>
        <li class="svgb-20__rung">
          <span class="svgb-20__n">13</span>
          <button class="svgb-20__btn" type="button" data-chars="13" style="--svgb-20-chars: 13">
            <svg class="svgb-20__frame" aria-hidden="true"><rect class="svgb-20__ink" data-chars="13" pathLength="1" vector-effect="non-scaling-stroke"/></svg>
            <span class="svgb-20__label">Export as CSV</span>
          </button>
          <span class="svgb-20__w">1.8px</span>
        </li>
        <li class="svgb-20__rung">
          <span class="svgb-20__n">22</span>
          <button class="svgb-20__btn" type="button" data-chars="22" style="--svgb-20-chars: 22">
            <svg class="svgb-20__frame" aria-hidden="true"><rect class="svgb-20__ink" data-chars="22" pathLength="1" vector-effect="non-scaling-stroke"/></svg>
            <span class="svgb-20__label">Schedule for next week</span>
          </button>
          <span class="svgb-20__w">2.3px</span>
        </li>
        <li class="svgb-20__rung">
          <span class="svgb-20__n">35</span>
          <button class="svgb-20__btn" type="button" data-chars="35" style="--svgb-20-chars: 35">
            <svg class="svgb-20__frame" aria-hidden="true"><rect class="svgb-20__ink" data-chars="35" pathLength="1" vector-effect="non-scaling-stroke"/></svg>
            <span class="svgb-20__label">Duplicate workspace and invite team</span>
          </button>
          <span class="svgb-20__w">3.0px</span>
        </li>
      </ol>

      <div class="svgb-20__control">
        <span class="svgb-20__ctl">control &middot; fixed 2px</span>
        <div class="svgb-20__pair">
          <button class="svgb-20__btn svgb-20__btn--flat" type="button" data-chars="3" style="--svgb-20-chars: 3">
            <svg class="svgb-20__frame" aria-hidden="true"><rect class="svgb-20__ink svgb-20__ink--flat" data-chars="3" pathLength="1" vector-effect="non-scaling-stroke"/></svg>
            <span class="svgb-20__label">Buy</span>
          </button>
          <button class="svgb-20__btn svgb-20__btn--flat" type="button" data-chars="35" style="--svgb-20-chars: 35">
            <svg class="svgb-20__frame" aria-hidden="true"><rect class="svgb-20__ink svgb-20__ink--flat" data-chars="35" pathLength="1" vector-effect="non-scaling-stroke"/></svg>
            <span class="svgb-20__label">Duplicate workspace and invite team</span>
          </button>
        </div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Archivo:wdth,[email protected],400;75..125,700&family=JetBrains+Mono:wght@400;500&display=swap');

@property --svgb-20-chars {
  syntax: '<integer>';
  inherits: true;
  initial-value: 12;
}
/* the duty cycle of the measure: 0.65 = ticks with gaps, 1 = a closed border.
   Registering it makes it interpolable, so the dash pattern recomputes per frame. */

@property --svgb-20-duty {
  syntax: '<number>';
  inherits: true;
  initial-value: 0.65;
}

.svgb-20 {
  --svgb-20-bg: #101010;
  --svgb-20-bg: oklch(0.18 0 0);
  --svgb-20-fg: #f4f4f0;
  --svgb-20-fg: oklch(0.96 0.005 100);
  --svgb-20-muted: #8d8d86;
  --svgb-20-muted: oklch(0.67 0.008 100);
  --svgb-20-rest: rgba(244, 244, 240, 0.16);
  --svgb-20-rest: oklch(0.96 0.005 100 / 0.16);
  --svgb-20-stroke: #d8ff2b;
  --svgb-20-stroke: oklch(0.93 0.22 116);
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--svgb-20-bg);
  color: var(--svgb-20-fg);
  font-family: 'Archivo', system-ui, sans-serif;
}

.svgb-20 *,
.svgb-20 *::before,
.svgb-20 *::after {
  box-sizing: border-box;
}

.svgb-20__stage {
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(22px, 5vw, 68px);
}

.svgb-20__sheet {
  width: 100%;
  max-width: 900px;
  display: flex;
  flex-direction: column;
  gap: clamp(20px, 3vw, 32px);
}

.svgb-20__head {
  display: flex;
  flex-wrap: wrap;
  align-items: flex-end;
  justify-content: space-between;
  gap: 14px;
  padding-block-end: 16px;
  border-block-end: 1px solid var(--svgb-20-rest);
}

.svgb-20__title {
  margin: 0;
  font-size: clamp(38px, 7vw, 82px);
  font-weight: 700;
  font-stretch: 118%;
  line-height: 0.88;
  letter-spacing: -0.045em;
  text-transform: uppercase;
}

.svgb-20__sub {
  margin: 0;
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-size: 11px;
  letter-spacing: 0.02em;
  color: var(--svgb-20-muted);
}

.svgb-20__ladder {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: clamp(12px, 2vw, 18px);
}

.svgb-20__rung {
  display: grid;
  grid-template-columns: 34px 1fr 54px;
  gap: clamp(12px, 2.5vw, 22px);
  align-items: center;
}

.svgb-20__n,
.svgb-20__w {
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-size: 11px;
  color: var(--svgb-20-muted);
  font-variant-numeric: tabular-nums;
}

.svgb-20__w {
  text-align: end;
}

.svgb-20__btn {
  position: relative;
  display: inline-grid;
  place-items: center;
  justify-self: start;
  min-inline-size: 96px;
  min-block-size: 62px;
  padding: 0 clamp(20px, 2.6vw, 32px);
  border: 0;
  border-radius: 4px;
  background: transparent;
  color: inherit;
  font: inherit;
  font-size: clamp(15px, calc(14px + var(--svgb-20-chars) * 0.04px), 18px);
  font-weight: 400;
  letter-spacing: -0.01em;
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
}

.svgb-20__btn:focus-visible {
  outline: 2px solid var(--svgb-20-stroke);
  outline-offset: 3px;
}

.svgb-20__label {
  position: relative;
  z-index: 1;
  white-space: nowrap;
  transition: color 260ms ease;
}

.svgb-20__btn:hover .svgb-20__label,
.svgb-20__btn:focus-visible .svgb-20__label {
  color: var(--svgb-20-stroke);
}

.svgb-20__frame {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  overflow: visible;
}

.svgb-20__ink {
  fill: none;
  x: 1.5px;
  y: 1.5px;
  width: calc(100% - 3px);
  height: calc(100% - 3px);
  rx: 4px;
  stroke: var(--svgb-20-rest);
  stroke-width: clamp(1.5px, calc(1.1px + var(--svgb-20-chars) * 0.055px), 3px);
  stroke-linecap: butt;
  /* one tick per character: pathLength 1 makes the segment 1/chars at any width */
  stroke-dasharray: calc(var(--svgb-20-duty) / var(--svgb-20-chars)) calc((1 - var(--svgb-20-duty)) / var(--svgb-20-chars));
  transition: stroke 240ms ease;
}
/* progressive enhancement: attr() with a type reads the count straight off the rect,
   dropping the inline custom property. It must resolve on the element that carries
   the declaration — the rect — not on the button. */

@supports (stroke-width: attr(data-chars type(<number>))) {
  .svgb-20__ink {
    stroke-width: clamp(1.5px, calc(1.1px + attr(data-chars type(<number>), 12) * 0.055px), 3px);
  }
}
/* hover closes the gaps: every tick grows into its neighbour until the measure becomes a border */

.svgb-20__btn {
  transition: --svgb-20-duty calc(340ms + var(--svgb-20-chars) * 14ms) cubic-bezier(0.22, 1, 0.36, 1);
}

.svgb-20__btn:hover,
.svgb-20__btn:focus-visible {
  --svgb-20-duty: 1;
}

.svgb-20__btn:hover .svgb-20__ink,
.svgb-20__btn:focus-visible .svgb-20__ink {
  stroke: var(--svgb-20-stroke);
}

.svgb-20__ink--flat {
  stroke-width: 2px;
  transition-duration: 560ms;
}

.svgb-20__control {
  display: flex;
  flex-direction: column;
  gap: 12px;
  padding-block-start: 18px;
  border-block-start: 1px solid var(--svgb-20-rest);
}

.svgb-20__ctl {
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-size: 10.5px;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--svgb-20-muted);
}

.svgb-20__pair {
  display: flex;
  flex-wrap: wrap;
  gap: 14px;
  align-items: center;
}

.svgb-20__btn--flat {
  color: var(--svgb-20-muted);
}

.svgb-20__ti {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.svgb-20__toggle {
  position: absolute;
  z-index: 5;
  inset-block-start: 16px;
  inset-inline-end: 16px;
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border-radius: 2px;
  border: 1px solid color-mix(in oklab, currentColor 22%, transparent);
  background: color-mix(in oklab, currentColor 7%, transparent);
  color: inherit;
  cursor: pointer;
  transition: background 160ms ease, transform 160ms ease;
}

.svgb-20__toggle:hover {
  background: color-mix(in oklab, currentColor 14%, transparent);
}

.svgb-20__toggle:active {
  transform: scale(0.94);
}

.svgb-20__toggle svg {
  inline-size: 18px;
  block-size: 18px;
  transition: transform 400ms cubic-bezier(0.2, 0.7, 0.3, 1);
}

.svgb-20__ti:checked + .svgb-20__toggle svg {
  transform: rotate(180deg);
}

.svgb-20__ti:focus-visible + .svgb-20__toggle {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.svgb-20__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.svgb-20:has(#svgb-20-theme:checked) {
  --svgb-20-bg: #f4f4f0;
  --svgb-20-bg: oklch(0.96 0.005 100);
  --svgb-20-fg: #111111;
  --svgb-20-fg: oklch(0.185 0 0);
  --svgb-20-muted: #5e5e58;
  --svgb-20-muted: oklch(0.50 0.008 100);
  --svgb-20-rest: rgba(17, 17, 17, 0.18);
  --svgb-20-rest: oklch(0.185 0 0 / 0.18);
  --svgb-20-stroke: #4a5c00;
  --svgb-20-stroke: oklch(0.44 0.14 116);
}

@media (prefers-reduced-motion: reduce) {
  .svgb-20__btn {
    transition: none;
  }

  .svgb-20__ink {
    transition: stroke 200ms ease;
    stroke-dasharray: none;
  }

  .svgb-20__label,
    .svgb-20__toggle,
    .svgb-20__toggle svg {
    transition: none;
  }
}
```

## JavaScript
```js
/* Optional convenience: the count can equally be printed into the markup by your template. */
(function () {
  var root = document.querySelector('.svgb-20');
  if (!root) return;
  root.querySelectorAll('.svgb-20__btn').forEach(function (btn) {
    var n = btn.querySelector('.svgb-20__label').textContent.trim().length;
    btn.dataset.chars = String(n);
    btn.style.setProperty('--svgb-20-chars', String(n));
    /* attr() resolves against the element the declaration sits on, so the rect
       needs its own copy — the button's attribute is not in scope for it. */
    var ink = btn.querySelector('.svgb-20__ink');
    if (ink) ink.dataset.chars = String(n);
  });
})();
```
