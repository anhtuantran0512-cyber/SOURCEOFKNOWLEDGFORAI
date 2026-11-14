---
source: "codefronts"
url: "https://codefronts.com/snippets/css-popovers/basic-anchored-popover/"
title: "Basic Anchored Popover"
section: "snippets"
category: "css-popovers"
category_name: "CSS Popovers"
description: "The two features compose but ship separately: popover handles the top layer and dismissal, anchor positioning handles where the panel lands."
has_js: "false"
---

Here's a working CSS Popover from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Basic Anchored Popover
Source: https://codefronts.com/snippets/css-popovers/basic-anchored-popover/

The two features compose but ship separately: popover handles the top layer and dismissal, anchor positioning handles where the panel lands. Name the trigger with anchor-name, point the panel at it with position-anchor, pick a side with position-area, and the entire measure-and-reposition dance that positioning libraries exist for disappears into four declarations.
## HTML
```html
<div class="pop-03">
  <div class="pop-03__stage">
    <div class="pop-03__card">
      <p class="pop-03__kicker">Checkout · Order 40118</p>
      <h2 class="pop-03__h">Two features, one panel</h2>
      <table class="pop-03__table">
        <tbody>
          <tr class="pop-03__row"><th class="pop-03__th" scope="row">Subtotal</th><td class="pop-03__td">$248.00</td></tr>
          <tr class="pop-03__row">
            <th class="pop-03__th" scope="row">
              <button class="pop-03__chip" type="button" popovertarget="pop-03-panel">
                Duties estimate
                <svg viewBox="0 0 16 16" width="12" height="12" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="8" cy="8" r="6"/><path d="M8 7.2v4M8 5.2v.6"/></svg>
              </button>
            </th>
            <td class="pop-03__td">$19.84</td>
          </tr>
          <tr class="pop-03__row"><th class="pop-03__th" scope="row">Shipping</th><td class="pop-03__td">$0.00</td></tr>
          <tr class="pop-03__row pop-03__row--total"><th class="pop-03__th" scope="row">Total</th><td class="pop-03__td">$267.84</td></tr>
        </tbody>
      </table>
      <p class="pop-03__foot">The chip is the anchor. The panel finds it by name.</p>
    </div>
  </div>

  <div class="pop-03__panel" popover="auto" id="pop-03-panel" role="group" aria-label="How duties are estimated">
    <p class="pop-03__ptitle">How this is estimated</p>
    <p class="pop-03__pbody">8% of the declared value for goods entering the EU under DDP terms. Final duties are set at the border and may differ by a few cents.</p>
    <dl class="pop-03__dl">
      <div class="pop-03__dlrow"><dt class="pop-03__dt">Basis</dt><dd class="pop-03__dd">$248.00</dd></div>
      <div class="pop-03__dlrow"><dt class="pop-03__dt">Rate</dt><dd class="pop-03__dd">8.0%</dd></div>
    </dl>
  </div>
</div>
```
## CSS
```css
.pop-03 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --paper: #f2ebdd;
  --pop: #fffdf7;
  --ink: #241f16;
  --muted: #6f6350;
  --edge: #241f16;
  --accent: #b4451f;
  --font-ui: "Iowan Old Style", Georgia, "Times New Roman", serif;
  --font-alt: ui-sans-serif, system-ui, sans-serif;
  background: var(--paper);
  color: var(--ink);
  font-family: var(--font-alt);
  padding: 40px 18px;
}

.pop-03__stage {
  display: grid;
  place-items: center;
  max-inline-size: 100%;
  min-height: calc(100vh - 80px);
}

.pop-03__card {
  inline-size: 100%;
  max-inline-size: 30rem;
  min-inline-size: 0;
  background: var(--pop);
  border: 2px solid var(--edge);
  padding: 22px 20px 20px;
  box-shadow: 8px 8px 0 var(--edge);
}

.pop-03__kicker {
  margin: 0 0 8px;
  font: 700 10.5px/1 var(--font-alt);
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--accent);
}

.pop-03__h {
  margin: 0 0 20px;
  font: 400 clamp(22px, 5vw, 30px)/1.15 var(--font-ui);
  letter-spacing: -0.01em;
}

.pop-03__table {
  inline-size: 100%;
  border-collapse: collapse;
}

.pop-03__row {
  border-block-end: 1px solid rgba(36, 31, 22, 0.16);
}

.pop-03__th {
  text-align: start;
  padding: 11px 0;
  font: 400 14px/1.4 var(--font-alt);
  color: var(--muted);
  min-inline-size: 0;
}

.pop-03__td {
  text-align: end;
  padding: 11px 0;
  font: 500 14px/1.4 var(--font-alt);
  font-variant-numeric: tabular-nums;
  white-space: nowrap;
}

.pop-03__row--total {
  border-block-end: 0;
}

.pop-03__row--total .pop-03__th,
.pop-03__row--total .pop-03__td {
  font-weight: 700;
  color: var(--ink);
  font-size: 15px;
}

.pop-03__chip {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  min-height: 44px;
  padding: 0 11px;
  font: 600 13px/1 var(--font-alt);
  color: var(--ink);
  background: var(--paper);
  border: 2px solid var(--edge);
  cursor: pointer;
  anchor-name: --pop-03-anchor;
}

.pop-03__chip:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

.pop-03__foot {
  margin: 16px 0 0;
  font-size: 12px;
  color: var(--muted);
}

.pop-03__panel {
  position: fixed;
  margin: 0;
  inline-size: min(20rem, calc(100vw - 32px));
  max-inline-size: calc(100vw - 32px);
  padding: 16px;
  color: var(--ink);
  background: var(--pop);
  border: 2px solid var(--edge);
  box-shadow: 6px 6px 0 var(--edge);
}

@supports (anchor-name: --a) {
  .pop-03__panel {
    position-anchor: --pop-03-anchor;
    position-area: block-end span-inline-end;
    inset: auto;
    margin-block-start: 10px;
    position-try-fallbacks: flip-block, flip-inline;
  }
}

.pop-03__ptitle {
  margin: 0 0 8px;
  font: 700 10.5px/1 var(--font-alt);
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--accent);
}

.pop-03__pbody {
  margin: 0 0 14px;
  font: 400 13.5px/1.6 var(--font-alt);
  color: var(--muted);
  text-wrap: pretty;
}

.pop-03__dl {
  margin: 0;
  display: grid;
  gap: 6px;
  border-block-start: 2px solid var(--edge);
  padding-block-start: 10px;
}

.pop-03__dlrow {
  display: flex;
  justify-content: space-between;
  gap: 12px;
  min-inline-size: 0;
}

.pop-03__dt {
  margin: 0;
  font-size: 12.5px;
  color: var(--muted);
}

.pop-03__dd {
  margin: 0;
  font-size: 12.5px;
  font-weight: 650;
  font-variant-numeric: tabular-nums;
}

@media (prefers-color-scheme: dark) {
  .pop-03 {
    --paper: #191510;
    --pop: #221d16;
    --ink: #f4ece0;
    --muted: #a89880;
    --edge: #f4ece0;
    --accent: #e58a5c;
  }
}

[data-theme="dark"] .pop-03 {
  --paper: #191510;
  --pop: #221d16;
  --ink: #f4ece0;
  --muted: #a89880;
  --edge: #f4ece0;
  --accent: #e58a5c;
}
```
