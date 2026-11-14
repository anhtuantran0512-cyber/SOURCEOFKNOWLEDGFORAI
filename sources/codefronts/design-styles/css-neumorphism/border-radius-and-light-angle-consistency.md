---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-neumorphism/border-radius-and-light-angle-consistency/"
title: "Border Radius and Light Angle Consistency"
section: "design-styles"
category: "css-neumorphism"
category_name: "CSS Neumorphism"
description: "Two rules that decide whether a soft-UI interface looks designed or assembled: one light source for the whole page, and a radius scale that grows with the…"
has_js: "false"
---

Here's a working CSS Neumorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Border Radius and Light Angle Consistency
Source: https://codefronts.com/design-styles/css-neumorphism/border-radius-and-light-angle-consistency/

Two rules that decide whether a soft-UI interface looks designed or assembled: one light source for the whole page, and a radius scale that grows with the element. Twelve tiles show radius against size, a control panel shows what happens when three components disagree about where the light is, and the offset-to-radius relationship is spelled out with numbers.
## HTML
```html
<section class="nm-18" aria-labelledby="nm-18-heading">
      <input type="checkbox" id="nm-18-theme" class="nm-18__themeinput">
      <label for="nm-18-theme" class="nm-18__themebtn">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 3a9 9 0 1 0 9 9 7 7 0 0 1-9-9Z"/></svg>
        Theme
      </label>
  <div class="nm-18__stage">
    <header class="nm-18__head">
      <p class="nm-18__kicker">Geometry</p>
      <h2 class="nm-18__heading" id="nm-18-heading">One lamp, and a radius that scales</h2>
      <p class="nm-18__sub">Two rules. Break either and the interface reads as assembled rather than designed.</p>
    </header>

    <div class="nm-18__scale">
      <div class="nm-18__item"><span class="nm-18__chip"></span><b>Chip</b><em>8px radius · 4px offset</em></div>
      <div class="nm-18__item"><span class="nm-18__btnlike"></span><b>Button</b><em>14px radius · 7px offset</em></div>
      <div class="nm-18__item"><span class="nm-18__cardlike"></span><b>Card</b><em>24px radius · 10px offset</em></div>
      <div class="nm-18__item"><span class="nm-18__circle"></span><b>Knob</b><em>50% radius · 7px offset</em></div>
    </div>

    <div class="nm-18__compare">
      <div class="nm-18__panel nm-18__panel--bad">
        <p class="nm-18__plabel nm-18__plabel--warn">Three light sources</p>
        <div class="nm-18__row">
          <span class="nm-18__box nm-18__box--l1"></span>
          <span class="nm-18__box nm-18__box--l2"></span>
          <span class="nm-18__box nm-18__box--l3"></span>
        </div>
        <p class="nm-18__pnote">Each component picked its own offsets. The eye reads three unrelated objects photographed separately.</p>
      </div>
      <div class="nm-18__panel">
        <p class="nm-18__plabel">One light source</p>
        <div class="nm-18__row">
          <span class="nm-18__box"></span>
          <span class="nm-18__box"></span>
          <span class="nm-18__box"></span>
        </div>
        <p class="nm-18__pnote">All three derive from one angle token. Same components, one scene.</p>
      </div>
    </div>

    <div class="nm-18__nest">
      <div class="nm-18__outer">
        <div class="nm-18__inner"><span class="nm-18__innerlabel">Inner radius = outer − padding</span></div>
      </div>
      <p class="nm-18__nestnote">Concentric corners. A nested well that reuses its parent's radius looks subtly wrong at every corner, and nobody can ever say why.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.nm-18 {
  position: relative;
  --nm-18-surface: #e6e7e3;
  --nm-18-dark: rgba(172,174,166,0.64);
  --nm-18-light: rgba(255,255,255,0.94);
  --nm-18-ink: #272923;
  --nm-18-muted: #575a51;
  --nm-18-border: #979a90;
  --nm-18-accent: #4a6b3c;
  --nm-18-warn: #9a4f2b;
  --nm-18-dist: 9px;
  --nm-18-pad: 14px;
  --nm-18-r-card: 24px;
  --nm-18-font-display: "Neue Haas Grotesk", "Helvetica Neue", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--nm-18-surface);
  color: var(--nm-18-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

@supports (color: oklch(0.9 0.01 120)) {
  .nm-18 {
    --nm-18-surface: oklch(0.917 0.007 120);
    --nm-18-ink: oklch(0.27 0.013 122);
    --nm-18-muted: oklch(0.45 0.014 122);
    --nm-18-accent: oklch(0.48 0.08 138);
    --nm-18-warn: oklch(0.48 0.12 45);
  }
}

@supports (color: color-mix(in oklab, #fff, #000)) {
  .nm-18 {
    --nm-18-dark: color-mix(in oklab, var(--nm-18-surface), #000 20%);
    --nm-18-light: color-mix(in oklab, var(--nm-18-surface), #fff 92%);
    --nm-18-border: color-mix(in oklab, var(--nm-18-surface), var(--nm-18-ink) 33%);
  }
}

.nm-18 *,
.nm-18 *::before,
.nm-18 *::after {
  box-sizing: border-box;
}

.nm-18__stage {
  max-width: 1000px;
  margin: 0 auto;
  min-height: 100vh;
  padding: clamp(26px, 5vw, 56px) clamp(16px, 4vw, 40px);
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: clamp(22px, 3.6vw, 34px);
}

.nm-18__head {
  max-width: 56ch;
  display: flex;
  flex-direction: column;
  gap: 9px;
}

.nm-18__kicker {
  margin: 0;
  font-size: 0.7rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--nm-18-muted);
}

.nm-18__heading {
  margin: 0;
  font-family: var(--nm-18-font-display);
  font-size: clamp(1.5rem, 4.2vw, 2.2rem);
  font-weight: 600;
  letter-spacing: -0.03em;
  line-height: 1.12;
  text-wrap: balance;
}

.nm-18__sub {
  margin: 0;
  font-size: 0.94rem;
  line-height: 1.6;
  color: var(--nm-18-muted);
  text-wrap: pretty;
}

.nm-18__scale {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 150px), 1fr));
  gap: clamp(16px, 3vw, 26px);
}

.nm-18__item {
  display: flex;
  flex-direction: column;
  gap: 8px;
  align-items: flex-start;
  min-inline-size: 0;
}

.nm-18__item b {
  font-family: var(--nm-18-font-display);
  font-size: 0.88rem;
  font-weight: 600;
}

.nm-18__item em {
  font-style: normal;
  font-size: 0.72rem;
  color: var(--nm-18-muted);
}

.nm-18__chip,
.nm-18__btnlike,
.nm-18__cardlike,
.nm-18__circle {
  display: block;
  background: var(--nm-18-surface);
  border: 1px solid var(--nm-18-border);
  margin-bottom: 6px;
}

.nm-18__chip {
  width: 78px;
  height: 30px;
  border-radius: 8px;
  box-shadow: 4px 4px 9px var(--nm-18-dark), -4px -4px 9px var(--nm-18-light);
}

.nm-18__btnlike {
  width: 118px;
  height: 46px;
  border-radius: 14px;
  box-shadow: 7px 7px 15px var(--nm-18-dark), -7px -7px 15px var(--nm-18-light);
}

.nm-18__cardlike {
  width: 100%;
  max-width: 150px;
  height: 84px;
  border-radius: var(--nm-18-r-card);
  box-shadow: 10px 10px 21px var(--nm-18-dark), -10px -10px 21px var(--nm-18-light);
}

.nm-18__circle {
  width: 56px;
  height: 56px;
  border-radius: 50%;
  box-shadow: 7px 7px 15px var(--nm-18-dark), -7px -7px 15px var(--nm-18-light);
}

.nm-18__compare {
  display: grid;
  grid-template-columns: 1fr;
  gap: clamp(16px, 2.8vw, 24px);
}

@media (min-width: 680px) {
  .nm-18__compare {
    grid-template-columns: 1fr 1fr;
  }
}

.nm-18__panel {
  border-radius: var(--nm-18-r-card);
  padding: clamp(18px, 3vw, 24px);
  display: flex;
  flex-direction: column;
  gap: 16px;
  min-inline-size: 0;
  background: var(--nm-18-surface);
  border: 1px solid var(--nm-18-border);
  box-shadow: inset 5px 5px 12px var(--nm-18-dark), inset -5px -5px 12px var(--nm-18-light);
}

.nm-18__plabel {
  margin: 0;
  font-family: var(--nm-18-font-display);
  font-size: 0.7rem;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  font-weight: 700;
  color: var(--nm-18-accent);
}

.nm-18__plabel--warn {
  color: var(--nm-18-warn);
}

.nm-18__row {
  display: flex;
  flex-wrap: wrap;
  gap: 18px;
}

.nm-18__box {
  width: 62px;
  height: 62px;
  border-radius: 16px;
  background: var(--nm-18-surface);
  border: 1px solid var(--nm-18-border);
  box-shadow: var(--nm-18-dist) var(--nm-18-dist) calc(var(--nm-18-dist) * 2) var(--nm-18-dark), calc(var(--nm-18-dist) * -1) calc(var(--nm-18-dist) * -1) calc(var(--nm-18-dist) * 2) var(--nm-18-light);
}

.nm-18__box--l1 {
  box-shadow: 9px 9px 18px var(--nm-18-dark), -9px -9px 18px var(--nm-18-light);
}

.nm-18__box--l2 {
  box-shadow: -9px 9px 18px var(--nm-18-dark), 9px -9px 18px var(--nm-18-light);
}

.nm-18__box--l3 {
  box-shadow: 0 11px 18px var(--nm-18-dark), 0 -11px 18px var(--nm-18-light);
}

.nm-18__pnote {
  margin: 0;
  font-size: 0.8rem;
  line-height: 1.58;
  color: var(--nm-18-muted);
  text-wrap: pretty;
}

.nm-18__nest {
  display: grid;
  grid-template-columns: 1fr;
  gap: clamp(16px, 3vw, 26px);
  align-items: center;
}

@media (min-width: 680px) {
  .nm-18__nest {
    grid-template-columns: minmax(0, 300px) minmax(0, 1fr);
  }
}

.nm-18__outer {
  border-radius: var(--nm-18-r-card);
  padding: var(--nm-18-pad);
  background: var(--nm-18-surface);
  border: 1px solid var(--nm-18-border);
  box-shadow: 11px 11px 23px var(--nm-18-dark), -11px -11px 23px var(--nm-18-light);
}

.nm-18__inner {
  border-radius: calc(var(--nm-18-r-card) - var(--nm-18-pad));
  min-height: 84px;
  display: grid;
  place-items: center;
  padding: 14px;
  text-align: center;
  background: var(--nm-18-surface);
  box-shadow: inset 5px 5px 11px var(--nm-18-dark), inset -5px -5px 11px var(--nm-18-light);
}

.nm-18__innerlabel {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.72rem;
  color: var(--nm-18-muted);
}

.nm-18__nestnote {
  margin: 0;
  font-size: 0.85rem;
  line-height: 1.62;
  color: var(--nm-18-muted);
  text-wrap: pretty;
}

@media (prefers-color-scheme: dark) {
  .nm-18 {
    --nm-18-surface: #272923;
    --nm-18-dark: rgba(11,12,10,0.72);
    --nm-18-light: rgba(88,92,82,0.44);
    --nm-18-ink: #e9eae4;
    --nm-18-muted: #9ba095;
    --nm-18-border: #858a7f;
    --nm-18-accent: #8dbd78;
    --nm-18-warn: #dd8f5f;
  }

  @supports (color: color-mix(in oklab, #fff, #000)) {
    .nm-18 {
      --nm-18-dark: color-mix(in oklab, var(--nm-18-surface), #000 55%);
      --nm-18-light: color-mix(in oklab, var(--nm-18-surface), #fff 14%);
    }
  }
}

.nm-18[data-theme="dark"] {
  --nm-18-surface: #272923;
  --nm-18-dark: rgba(11,12,10,0.72);
  --nm-18-light: rgba(88,92,82,0.44);
  --nm-18-ink: #e9eae4;
  --nm-18-muted: #9ba095;
  --nm-18-border: #858a7f;
  --nm-18-accent: #8dbd78;
  --nm-18-warn: #dd8f5f;
}

@supports (color: color-mix(in oklab, #fff, #000)) {
  .nm-18[data-theme="dark"] {
    --nm-18-dark: color-mix(in oklab, var(--nm-18-surface), #000 55%);
    --nm-18-light: color-mix(in oklab, var(--nm-18-surface), #fff 14%);
  }
}
/* Pure-CSS theme toggle. Mirrors the [data-theme="dark"] rules above so
   the demo's own dark palette is reachable from inside the demo. */

.nm-18__themeinput {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: 0;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.nm-18__themebtn {
  position: absolute;
  inset-block-start: clamp(10px, 2vw, 18px);
  inset-inline-end: clamp(10px, 2vw, 18px);
  z-index: 5;
  display: inline-flex;
  align-items: center;
  gap: 7px;
  min-height: 44px;
  padding: 0 14px;
  border-radius: 999px;
  background: var(--nm-18-surface);
  color: var(--nm-18-ink);
  border: 1px solid var(--nm-18-line);
  font: 600 11px/1 var(--nm-18-font-display, system-ui);
  letter-spacing: 0.12em;
  text-transform: uppercase;
  cursor: pointer;
  box-shadow: var(--nm-18-distance, 6px) var(--nm-18-distance, 6px) var(--nm-18-blur, 14px) var(--nm-18-dark), calc(-1 * var(--nm-18-distance, 6px)) calc(-1 * var(--nm-18-distance, 6px)) var(--nm-18-blur, 14px) var(--nm-18-light);
  transition: box-shadow 180ms ease, color 180ms ease;
}

.nm-18__themebtn:hover {
  color: var(--nm-18-ink);
}

.nm-18__themeinput:focus-visible + .nm-18__themebtn {
  outline: 2px solid var(--nm-18-ink);
  outline-offset: 3px;
}

.nm-18:has(#nm-18-theme:checked) .nm-18__themebtn {
  box-shadow: inset var(--nm-18-distance, 6px) var(--nm-18-distance, 6px) var(--nm-18-blur, 14px) var(--nm-18-dark), inset calc(-1 * var(--nm-18-distance, 6px)) calc(-1 * var(--nm-18-distance, 6px)) var(--nm-18-blur, 14px) var(--nm-18-light);
}

.nm-18__themebtn svg {
  inline-size: 13px;
  block-size: 13px;
  flex: none;
}

.nm-18:has(#nm-18-theme:checked) {
  --nm-18-surface: #272923;
  --nm-18-dark: rgba(11,12,10,0.72);
  --nm-18-light: rgba(88,92,82,0.44);
  --nm-18-ink: #e9eae4;
  --nm-18-muted: #9ba095;
  --nm-18-border: #858a7f;
  --nm-18-accent: #8dbd78;
  --nm-18-warn: #dd8f5f;
}

@media (prefers-color-scheme: light) {
  .nm-18:has(#nm-18-theme:checked) {
    --nm-18-surface: #272923;
    --nm-18-dark: rgba(11,12,10,0.72);
    --nm-18-light: rgba(88,92,82,0.44);
    --nm-18-ink: #e9eae4;
    --nm-18-muted: #9ba095;
    --nm-18-border: #858a7f;
    --nm-18-accent: #8dbd78;
    --nm-18-warn: #dd8f5f;
  }
}

@media (prefers-color-scheme: dark) {
  /* Base already resolves dark here, so :checked restores light —
       without this the toggle is inert for dark-OS visitors. */

  .nm-18:has(#nm-18-theme:checked) {
    --nm-18-surface: #e6e7e3;
    --nm-18-dark: rgba(172,174,166,0.64);
    --nm-18-light: rgba(255,255,255,0.94);
    --nm-18-ink: #272923;
    --nm-18-muted: #575a51;
    --nm-18-border: #979a90;
    --nm-18-accent: #4a6b3c;
    --nm-18-warn: #9a4f2b;
  }
}

@media (prefers-reduced-motion: reduce) {
  .nm-18__themebtn {
    transition: none;
  }
}
```
