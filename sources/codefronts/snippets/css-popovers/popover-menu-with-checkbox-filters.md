---
source: "codefronts"
url: "https://codefronts.com/snippets/css-popovers/popover-menu-with-checkbox-filters/"
title: "Popover Menu with Checkbox Filters"
section: "snippets"
category: "css-popovers"
category_name: "CSS Popovers"
description: "The clearest real use of popover=manual: a filter menu the user ticks several boxes in, which must not vanish because a click landed slightly outside it."
has_js: "false"
---

Here's a working CSS Popover from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Popover Menu with Checkbox Filters
Source: https://codefronts.com/snippets/css-popovers/popover-menu-with-checkbox-filters/

The clearest real use of popover=manual: a filter menu the user ticks several boxes in, which must not vanish because a click landed slightly outside it. Manual opts out of light dismiss and Escape, so the panel ships a visible Apply and a Close — the trade the auto behaviour from demo 02 cannot make.
## HTML
```html
<div class="pop-15">
  <div class="pop-15__stage">
    <div class="pop-15__tool">
      <div class="pop-15__bar">
        <span class="pop-15__title">Shipments · 1,284 rows</span>
        <button class="pop-15__chip" type="button" popovertarget="pop-15-filters" popovertargetaction="show">
          <svg viewBox="0 0 16 16" width="13" height="13" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M2.5 4h11M4.5 8h7M6.5 12h3"/></svg>
          Filters
          <span class="pop-15__count">3</span>
        </button>
      </div>
      <table class="pop-15__table">
        <thead>
          <tr><th class="pop-15__th" scope="col">Ref</th><th class="pop-15__th" scope="col">Lane</th><th class="pop-15__th pop-15__th--num" scope="col">Weight</th></tr>
        </thead>
        <tbody>
          <tr class="pop-15__tr"><td class="pop-15__td">SH-8841</td><td class="pop-15__td">Rotterdam → Leeds</td><td class="pop-15__td pop-15__td--num">1,240 kg</td></tr>
          <tr class="pop-15__tr"><td class="pop-15__td">SH-8842</td><td class="pop-15__td">Gdansk → Bremen</td><td class="pop-15__td pop-15__td--num">860 kg</td></tr>
          <tr class="pop-15__tr"><td class="pop-15__td">SH-8843</td><td class="pop-15__td">Vigo → Nantes</td><td class="pop-15__td pop-15__td--num">3,105 kg</td></tr>
          <tr class="pop-15__tr"><td class="pop-15__td">SH-8844</td><td class="pop-15__td">Oslo → Aarhus</td><td class="pop-15__td pop-15__td--num">412 kg</td></tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="pop-15__panel" popover="manual" id="pop-15-filters" role="group" aria-labelledby="pop-15-legend">
    <div class="pop-15__phead">
      <p class="pop-15__ptitle" id="pop-15-legend">Filter shipments</p>
      <button class="pop-15__x" type="button" popovertarget="pop-15-filters" popovertargetaction="hide" aria-label="Close filters">
        <svg viewBox="0 0 16 16" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M4 4l8 8M12 4l-8 8"/></svg>
      </button>
    </div>
    <fieldset class="pop-15__set">
      <legend class="pop-15__legend">Status</legend>
      <label class="pop-15__check"><input class="pop-15__box" type="checkbox" checked> In transit</label>
      <label class="pop-15__check"><input class="pop-15__box" type="checkbox" checked> Held at customs</label>
      <label class="pop-15__check"><input class="pop-15__box" type="checkbox"> Delivered</label>
      <label class="pop-15__check"><input class="pop-15__box" type="checkbox" checked> Exception raised</label>
      <label class="pop-15__check"><input class="pop-15__box" type="checkbox"> Cancelled</label>
    </fieldset>
    <p class="pop-15__nag">Tick several. Click the table behind me. I am still here.</p>
    <div class="pop-15__acts">
      <button class="pop-15__apply" type="button" popovertarget="pop-15-filters" popovertargetaction="hide">Apply filters</button>
      <button class="pop-15__cancel" type="button" popovertarget="pop-15-filters" popovertargetaction="hide">Close</button>
    </div>
  </div>
</div>
```
## CSS
```css
.pop-15 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --bg: #f4f4f2;
  --surface: #ffffff;
  --ink: #171614;
  --muted: #6d6a63;
  --rule: #171614;
  --hair: #e0dfd9;
  --ember: #d1471f;
  --font-ui: ui-sans-serif, system-ui, "Segoe UI", sans-serif;
  --font-mono: ui-monospace, "SFMono-Regular", Menlo, monospace;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--font-ui);
  padding: 38px 16px;
}

.pop-15__stage {
  display: grid;
  place-items: center;
  max-inline-size: 100%;
  min-height: calc(100vh - 76px);
}

.pop-15__tool {
  inline-size: 100%;
  max-inline-size: 33rem;
  min-inline-size: 0;
  background: var(--surface);
  border: 2px solid var(--rule);
  box-shadow: 7px 7px 0 var(--ember);
}

.pop-15__bar {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  align-items: center;
  justify-content: space-between;
  padding: 10px 12px;
  border-block-end: 2px solid var(--rule);
}

.pop-15__title {
  font: 650 12.5px/1.2 var(--font-mono);
  min-inline-size: 0;
}

.pop-15__chip {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  min-height: 44px;
  padding: 0 12px;
  font: 700 11.5px/1 var(--font-ui);
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: var(--surface);
  background: var(--ink);
  border: 2px solid var(--ink);
  cursor: pointer;
  anchor-name: --pop-15-anchor;
}

.pop-15__chip:focus-visible {
  outline: 3px solid var(--ember);
  outline-offset: 2px;
}

.pop-15__count {
  display: grid;
  place-items: center;
  min-inline-size: 18px;
  block-size: 18px;
  font: 700 10.5px/1 var(--font-mono);
  color: var(--ink);
  background: var(--ember);
}

.pop-15__table {
  inline-size: 100%;
  border-collapse: collapse;
}

.pop-15__th {
  padding: 7px 12px;
  text-align: start;
  font: 700 9.5px/1 var(--font-ui);
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--muted);
  border-block-end: 1px solid var(--hair);
}

.pop-15__th--num,
.pop-15__td--num {
  text-align: end;
}

.pop-15__td {
  padding: 8px 12px;
  font: 500 12px/1.3 var(--font-mono);
  border-block-end: 1px solid var(--hair);
  min-inline-size: 0;
}

.pop-15__td--num {
  font-variant-numeric: tabular-nums;
  color: var(--muted);
  white-space: nowrap;
}

.pop-15__tr:last-child .pop-15__td {
  border-block-end: 0;
}

.pop-15__panel {
  position: fixed;
  margin: 0;
  inline-size: min(18rem, calc(100vw - 24px));
  max-inline-size: calc(100vw - 24px);
  padding: 13px;
  color: var(--ink);
  background: var(--surface);
  border: 2px solid var(--rule);
  border-radius: 0;
  box-shadow: 7px 7px 0 var(--ember);
}

@supports (anchor-name: --a) {
  .pop-15__panel {
    position-anchor: --pop-15-anchor;
    position-area: block-end span-inline-start;
    inset: auto;
    margin-block-start: 9px;
    position-try-fallbacks: flip-block, flip-inline;
  }
}

.pop-15__phead {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
  margin-bottom: 10px;
}

.pop-15__ptitle {
  margin: 0;
  font: 700 11px/1 var(--font-ui);
  letter-spacing: 0.16em;
  text-transform: uppercase;
}

.pop-15__x {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 44px;
  min-height: 44px;
  margin: -13px -13px -13px 0;
  color: var(--ink);
  background: none;
  border: 0;
  cursor: pointer;
}

.pop-15__x:focus-visible {
  outline: 3px solid var(--ember);
  outline-offset: -3px;
}

.pop-15__set {
  margin: 0;
  padding: 0;
  border: 0;
  display: grid;
}

.pop-15__legend {
  padding: 0;
  margin-bottom: 4px;
  font: 600 10.5px/1 var(--font-mono);
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--muted);
}

.pop-15__check {
  display: flex;
  align-items: center;
  gap: 10px;
  min-height: 44px;
  font-size: 13px;
  cursor: pointer;
  min-inline-size: 0;
}

.pop-15__box {
  flex: none;
  inline-size: 18px;
  block-size: 18px;
  margin: 0;
  accent-color: var(--ember);
  cursor: pointer;
}

.pop-15__box:focus-visible {
  outline: 3px solid var(--ember);
  outline-offset: 2px;
}

.pop-15__nag {
  margin: 8px 0 12px;
  padding-block-start: 10px;
  border-block-start: 1px solid var(--hair);
  font-size: 11.5px;
  line-height: 1.55;
  color: var(--ember);
  font-weight: 600;
}

.pop-15__acts {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.pop-15__apply,
.pop-15__cancel {
  flex: 1 1 auto;
  min-inline-size: 0;
  min-height: 44px;
  padding: 0 12px;
  font: 700 11.5px/1 var(--font-ui);
  letter-spacing: 0.06em;
  text-transform: uppercase;
  cursor: pointer;
  border: 2px solid var(--ink);
}

.pop-15__apply {
  color: var(--surface);
  background: var(--ink);
}

.pop-15__cancel {
  color: var(--ink);
  background: var(--surface);
}

.pop-15__apply:focus-visible,
.pop-15__cancel:focus-visible {
  outline: 3px solid var(--ember);
  outline-offset: 2px;
}

@media (prefers-color-scheme: dark) {
  .pop-15 {
    --bg: #121110;
    --surface: #1c1b19;
    --ink: #f1efe9;
    --muted: #98948b;
    --rule: #f1efe9;
    --hair: #2e2c28;
    --ember: #ff7043;
  }

  .pop-15__chip {
    color: #121110;
  }

  .pop-15__count {
    color: #121110;
  }

  .pop-15__apply {
    color: #121110;
  }
}

[data-theme="dark"] .pop-15 {
  --bg: #121110;
  --surface: #1c1b19;
  --ink: #f1efe9;
  --muted: #98948b;
  --rule: #f1efe9;
  --hair: #2e2c28;
  --ember: #ff7043;
}

[data-theme="dark"] .pop-15 .pop-15__chip,
[data-theme="dark"] .pop-15 .pop-15__count,
[data-theme="dark"] .pop-15 .pop-15__apply {
  color: #121110;
}
```
