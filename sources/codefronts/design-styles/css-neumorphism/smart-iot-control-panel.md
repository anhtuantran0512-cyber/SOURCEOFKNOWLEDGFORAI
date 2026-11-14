---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-neumorphism/smart-iot-control-panel/"
title: "Soft UI Tabs and Segmented Control"
section: "design-styles"
category: "css-neumorphism"
category_name: "CSS Neumorphism"
description: "Segmented controls and tab bars where the selected segment is pressed into the track and the rest sit flush."
has_js: "false"
---

Here's a working CSS Neumorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Soft UI Tabs and Segmented Control
Source: https://codefronts.com/design-styles/css-neumorphism/smart-iot-control-panel/

Segmented controls and tab bars where the selected segment is pressed into the track and the rest sit flush. Built on radio inputs so the whole thing works without script, with the selected panel revealed by :has(). Includes the two-way version soft UI does best — a recessed track holding raised segments — and the filter-chip row that uses the same logic.
## HTML
```html
<section class="nm-19" aria-labelledby="nm-19-heading">
      <input type="checkbox" id="nm-19-theme" class="nm-19__themeinput">
      <label for="nm-19-theme" class="nm-19__themebtn">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 3a9 9 0 1 0 9 9 7 7 0 0 1-9-9Z"/></svg>
        Theme
      </label>
  <div class="nm-19__stage">
    <header class="nm-19__head">
      <p class="nm-19__kicker">Component · segmented</p>
      <h2 class="nm-19__heading" id="nm-19-heading">Selected is the one that moved</h2>
      <p class="nm-19__sub">Radio inputs, a recessed track, and <code>:has()</code> switching the panel — no script anywhere.</p>
    </header>

    <div class="nm-19__tabs">
      <div class="nm-19__track" role="group" aria-label="View">
        <input class="nm-19__radio" type="radio" name="nm-19-view" id="nm-19-v1" checked>
        <label class="nm-19__seg" for="nm-19-v1">Summary</label>
        <input class="nm-19__radio" type="radio" name="nm-19-view" id="nm-19-v2">
        <label class="nm-19__seg" for="nm-19-v2">Timeline</label>
        <input class="nm-19__radio" type="radio" name="nm-19-view" id="nm-19-v3">
        <label class="nm-19__seg" for="nm-19-v3">Ledger</label>
      </div>

      <div class="nm-19__panels">
        <div class="nm-19__panel" data-panel="1">
          <h3 class="nm-19__ptitle">Summary</h3>
          <p class="nm-19__pbody">Three invoices cleared this week and one query outstanding with the Halden account. Net position improved by £2,140.</p>
        </div>
        <div class="nm-19__panel" data-panel="2">
          <h3 class="nm-19__ptitle">Timeline</h3>
          <p class="nm-19__pbody">Mon — invoice 4821 issued. Wed — payment received, 4818. Thu — query raised on 4822. Fri — reconciliation run completed.</p>
        </div>
        <div class="nm-19__panel" data-panel="3">
          <h3 class="nm-19__ptitle">Ledger</h3>
          <p class="nm-19__pbody">Full transaction list, including the two adjustments posted against the Q2 credit note. Export available as CSV or OFX.</p>
        </div>
      </div>
    </div>

    <div class="nm-19__alt">
      <p class="nm-19__altlabel">Flush track, inset selection — the other valid metaphor</p>
      <div class="nm-19__track nm-19__track--flush" role="group" aria-label="Range">
        <input class="nm-19__radio" type="radio" name="nm-19-range" id="nm-19-r1">
        <label class="nm-19__seg" for="nm-19-r1">7d</label>
        <input class="nm-19__radio" type="radio" name="nm-19-range" id="nm-19-r2" checked>
        <label class="nm-19__seg" for="nm-19-r2">30d</label>
        <input class="nm-19__radio" type="radio" name="nm-19-range" id="nm-19-r3">
        <label class="nm-19__seg" for="nm-19-r3">90d</label>
        <input class="nm-19__radio" type="radio" name="nm-19-range" id="nm-19-r4">
        <label class="nm-19__seg" for="nm-19-r4">All</label>
      </div>
    </div>

    <div class="nm-19__chips">
      <input class="nm-19__radio" type="radio" name="nm-19-filter" id="nm-19-f1" checked>
      <label class="nm-19__chip" for="nm-19-f1">Everything</label>
      <input class="nm-19__radio" type="radio" name="nm-19-filter" id="nm-19-f2">
      <label class="nm-19__chip" for="nm-19-f2">Unpaid</label>
      <input class="nm-19__radio" type="radio" name="nm-19-filter" id="nm-19-f3">
      <label class="nm-19__chip" for="nm-19-f3">Overdue</label>
      <input class="nm-19__radio" type="radio" name="nm-19-filter" id="nm-19-f4">
      <label class="nm-19__chip" for="nm-19-f4">Drafts</label>
    </div>
  </div>
</section>
```
## CSS
```css
.nm-19 {
  position: relative;
  --nm-19-surface: #e6e4e8;
  --nm-19-dark: rgba(172,169,178,0.62);
  --nm-19-light: rgba(255,255,255,0.94);
  --nm-19-ink: #272530;
  --nm-19-muted: #5a5766;
  --nm-19-border: #97939f;
  --nm-19-accent: #4b5aa0;
  --nm-19-radius: 14px;
  --nm-19-font-display: "Basis Grotesque", "Helvetica Neue", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--nm-19-surface);
  color: var(--nm-19-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

@supports (color: oklch(0.9 0.01 300)) {
  .nm-19 {
    --nm-19-surface: oklch(0.913 0.008 305);
    --nm-19-ink: oklch(0.27 0.018 300);
    --nm-19-muted: oklch(0.46 0.02 300);
    --nm-19-accent: oklch(0.47 0.11 275);
  }
}

@supports (color: color-mix(in oklab, #fff, #000)) {
  .nm-19 {
    --nm-19-dark: color-mix(in oklab, var(--nm-19-surface), #000 19%);
    --nm-19-light: color-mix(in oklab, var(--nm-19-surface), #fff 92%);
    --nm-19-border: color-mix(in oklab, var(--nm-19-surface), var(--nm-19-ink) 33%);
  }
}

.nm-19 *,
.nm-19 *::before,
.nm-19 *::after {
  box-sizing: border-box;
}

.nm-19__stage {
  max-width: 880px;
  margin: 0 auto;
  min-height: 100vh;
  padding: clamp(26px, 5vw, 56px) clamp(16px, 4vw, 40px);
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: clamp(22px, 3.4vw, 32px);
}

.nm-19__head {
  max-width: 56ch;
  display: flex;
  flex-direction: column;
  gap: 9px;
}

.nm-19__kicker {
  margin: 0;
  font-size: 0.7rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--nm-19-muted);
}

.nm-19__heading {
  margin: 0;
  font-family: var(--nm-19-font-display);
  font-size: clamp(1.5rem, 4.2vw, 2.2rem);
  font-weight: 650;
  letter-spacing: -0.025em;
  line-height: 1.12;
  text-wrap: balance;
}

.nm-19__sub {
  margin: 0;
  font-size: 0.94rem;
  line-height: 1.6;
  color: var(--nm-19-muted);
  text-wrap: pretty;
}

.nm-19__sub code {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.88em;
  color: var(--nm-19-ink);
}

.nm-19__tabs {
  display: flex;
  flex-direction: column;
  gap: clamp(16px, 2.6vw, 22px);
}

.nm-19__track {
  display: grid;
  grid-auto-flow: column;
  grid-auto-columns: 1fr;
  gap: 8px;
  padding: 8px;
  border-radius: calc(var(--nm-19-radius) + 8px);
  background: var(--nm-19-surface);
  border: 1px solid var(--nm-19-border);
  box-shadow: inset 5px 5px 11px var(--nm-19-dark), inset -5px -5px 11px var(--nm-19-light);
}

.nm-19__track--flush {
  box-shadow: 8px 8px 17px var(--nm-19-dark), -8px -8px 17px var(--nm-19-light);
}

.nm-19__radio {
  position: absolute;
  width: 1px;
  height: 1px;
  clip-path: inset(50%);
  overflow: hidden;
}

.nm-19__seg {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 46px;
  padding: 0 12px;
  border-radius: var(--nm-19-radius);
  cursor: pointer;
  color: var(--nm-19-muted);
  font-family: var(--nm-19-font-display);
  font-size: 0.87rem;
  font-weight: 500;
  text-align: center;
  min-inline-size: 0;
  transition: color 150ms ease;
}

.nm-19__radio:checked + .nm-19__seg {
  color: var(--nm-19-ink);
  font-weight: 650;
  background: var(--nm-19-surface);
  box-shadow: 5px 5px 11px var(--nm-19-dark), -5px -5px 11px var(--nm-19-light);
}

.nm-19__radio:checked + .nm-19__seg::after {
  content: "";
  position: absolute;
  bottom: 7px;
  width: 18px;
  height: 2px;
  border-radius: 999px;
  background: var(--nm-19-accent);
}

.nm-19__track--flush .nm-19__radio:checked + .nm-19__seg {
  box-shadow: inset 4px 4px 9px var(--nm-19-dark), inset -4px -4px 9px var(--nm-19-light);
}

.nm-19__radio:focus-visible + .nm-19__seg {
  outline: 2px solid var(--nm-19-accent);
  outline-offset: -2px;
}

.nm-19__panels {
  border-radius: 20px;
  padding: clamp(18px, 3vw, 26px);
  min-inline-size: 0;
  background: var(--nm-19-surface);
  border: 1px solid var(--nm-19-border);
  box-shadow: 9px 9px 19px var(--nm-19-dark), -9px -9px 19px var(--nm-19-light);
}

.nm-19__panel {
  display: none;
}

.nm-19__panel[data-panel="1"] {
  display: block;
}

.nm-19__tabs:has(#nm-19-v2:checked) .nm-19__panel[data-panel="1"] {
  display: none;
}

.nm-19__tabs:has(#nm-19-v2:checked) .nm-19__panel[data-panel="2"] {
  display: block;
}

.nm-19__tabs:has(#nm-19-v3:checked) .nm-19__panel[data-panel="1"] {
  display: none;
}

.nm-19__tabs:has(#nm-19-v3:checked) .nm-19__panel[data-panel="3"] {
  display: block;
}

.nm-19__ptitle {
  margin: 0 0 8px;
  font-family: var(--nm-19-font-display);
  font-size: 1.05rem;
  font-weight: 650;
  letter-spacing: -0.015em;
}

.nm-19__pbody {
  margin: 0;
  font-size: 0.87rem;
  line-height: 1.65;
  color: var(--nm-19-muted);
  text-wrap: pretty;
}

.nm-19__alt {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.nm-19__altlabel {
  margin: 0;
  font-size: 0.72rem;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--nm-19-muted);
  font-weight: 600;
}

.nm-19__chips {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.nm-19__chip {
  display: inline-flex;
  align-items: center;
  min-height: 44px;
  padding: 0 16px;
  border-radius: 10px;
  cursor: pointer;
  color: var(--nm-19-muted);
  font-size: 0.83rem;
  font-weight: 500;
  border: 1px solid var(--nm-19-border);
  background: var(--nm-19-surface);
  box-shadow: 4px 4px 10px var(--nm-19-dark), -4px -4px 10px var(--nm-19-light);
}

.nm-19__radio:checked + .nm-19__chip {
  color: var(--nm-19-accent);
  border-color: var(--nm-19-accent);
  font-weight: 650;
  box-shadow: inset 4px 4px 9px var(--nm-19-dark), inset -4px -4px 9px var(--nm-19-light);
}

.nm-19__radio:focus-visible + .nm-19__chip {
  outline: 2px solid var(--nm-19-accent);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .nm-19__seg {
    transition: none;
  }
}

@media (prefers-color-scheme: dark) {
  .nm-19 {
    --nm-19-surface: #282630;
    --nm-19-dark: rgba(11,10,14,0.72);
    --nm-19-light: rgba(88,85,100,0.44);
    --nm-19-ink: #e8e6ef;
    --nm-19-muted: #9d99ab;
    --nm-19-border: #868295;
    --nm-19-accent: #97a5e8;
  }

  @supports (color: color-mix(in oklab, #fff, #000)) {
    .nm-19 {
      --nm-19-dark: color-mix(in oklab, var(--nm-19-surface), #000 55%);
      --nm-19-light: color-mix(in oklab, var(--nm-19-surface), #fff 14%);
    }
  }
}

.nm-19[data-theme="dark"] {
  --nm-19-surface: #282630;
  --nm-19-dark: rgba(11,10,14,0.72);
  --nm-19-light: rgba(88,85,100,0.44);
  --nm-19-ink: #e8e6ef;
  --nm-19-muted: #9d99ab;
  --nm-19-border: #868295;
  --nm-19-accent: #97a5e8;
}

@supports (color: color-mix(in oklab, #fff, #000)) {
  .nm-19[data-theme="dark"] {
    --nm-19-dark: color-mix(in oklab, var(--nm-19-surface), #000 55%);
    --nm-19-light: color-mix(in oklab, var(--nm-19-surface), #fff 14%);
  }
}
/* Pure-CSS theme toggle. Mirrors the [data-theme="dark"] rules above so
   the demo's own dark palette is reachable from inside the demo. */

.nm-19__themeinput {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: 0;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.nm-19__themebtn {
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
  background: var(--nm-19-surface);
  color: var(--nm-19-ink);
  border: 1px solid var(--nm-19-line);
  font: 600 11px/1 var(--nm-19-font-display, system-ui);
  letter-spacing: 0.12em;
  text-transform: uppercase;
  cursor: pointer;
  box-shadow: var(--nm-19-distance, 6px) var(--nm-19-distance, 6px) var(--nm-19-blur, 14px) var(--nm-19-dark), calc(-1 * var(--nm-19-distance, 6px)) calc(-1 * var(--nm-19-distance, 6px)) var(--nm-19-blur, 14px) var(--nm-19-light);
  transition: box-shadow 180ms ease, color 180ms ease;
}

.nm-19__themebtn:hover {
  color: var(--nm-19-ink);
}

.nm-19__themeinput:focus-visible + .nm-19__themebtn {
  outline: 2px solid var(--nm-19-ink);
  outline-offset: 3px;
}

.nm-19:has(#nm-19-theme:checked) .nm-19__themebtn {
  box-shadow: inset var(--nm-19-distance, 6px) var(--nm-19-distance, 6px) var(--nm-19-blur, 14px) var(--nm-19-dark), inset calc(-1 * var(--nm-19-distance, 6px)) calc(-1 * var(--nm-19-distance, 6px)) var(--nm-19-blur, 14px) var(--nm-19-light);
}

.nm-19__themebtn svg {
  inline-size: 13px;
  block-size: 13px;
  flex: none;
}

.nm-19:has(#nm-19-theme:checked) {
  --nm-19-surface: #282630;
  --nm-19-dark: rgba(11,10,14,0.72);
  --nm-19-light: rgba(88,85,100,0.44);
  --nm-19-ink: #e8e6ef;
  --nm-19-muted: #9d99ab;
  --nm-19-border: #868295;
  --nm-19-accent: #97a5e8;
}

@media (prefers-color-scheme: light) {
  .nm-19:has(#nm-19-theme:checked) {
    --nm-19-surface: #282630;
    --nm-19-dark: rgba(11,10,14,0.72);
    --nm-19-light: rgba(88,85,100,0.44);
    --nm-19-ink: #e8e6ef;
    --nm-19-muted: #9d99ab;
    --nm-19-border: #868295;
    --nm-19-accent: #97a5e8;
  }
}

@media (prefers-color-scheme: dark) {
  /* Base already resolves dark here, so :checked restores light —
       without this the toggle is inert for dark-OS visitors. */

  .nm-19:has(#nm-19-theme:checked) {
    --nm-19-surface: #e6e4e8;
    --nm-19-dark: rgba(172,169,178,0.62);
    --nm-19-light: rgba(255,255,255,0.94);
    --nm-19-ink: #272530;
    --nm-19-muted: #5a5766;
    --nm-19-border: #97939f;
    --nm-19-accent: #4b5aa0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .nm-19__themebtn {
    transition: none;
  }
}
```
