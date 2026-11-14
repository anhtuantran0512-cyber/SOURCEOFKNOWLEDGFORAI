---
source: "codefronts"
url: "https://codefronts.com/snippets/css-popovers/match-anchor-width-for-dropdowns/"
title: "Match Anchor Width for Dropdowns"
section: "snippets"
category: "css-popovers"
category_name: "CSS Popovers"
description: "A floating panel that is exactly as wide as the control that opened it reads as part of that control; one that is a little narrower or wider reads as a bug."
has_js: "false"
---

Here's a working CSS Popover from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Match Anchor Width for Dropdowns
Source: https://codefronts.com/snippets/css-popovers/match-anchor-width-for-dropdowns/

A floating panel that is exactly as wide as the control that opened it reads as part of that control; one that is a little narrower or wider reads as a bug. anchor-size(width) makes the panel size itself from its anchor with no measurement, and min-width: anchor-size(width) gives the forgiving variant that can still grow for long option labels.
## HTML
```html
<div class="pop-09">
  <div class="pop-09__stage">
    <form class="pop-09__form" aria-label="Deployment target">
      <p class="pop-09__legend">Deploy target</p>
      <label class="pop-09__label" for="pop-09-env">Environment</label>
      <button class="pop-09__field" type="button" id="pop-09-env" popovertarget="pop-09-list">
        <span class="pop-09__value">Production · eu-west-1</span>
        <svg class="pop-09__chev" viewBox="0 0 16 16" width="14" height="14" fill="none" stroke="currentColor" stroke-width="1.9" aria-hidden="true"><path d="M4 6.5 8 10.5 12 6.5"/></svg>
      </button>
      <p class="pop-09__help">The panel below takes its width from this button, live.</p>
      <div class="pop-09__meta">
        <span class="pop-09__pill">anchor-size(width)</span>
        <span class="pop-09__pill pop-09__pill--alt">min-inline-size variant in the CSS</span>
      </div>
    </form>
  </div>

  <div class="pop-09__list" popover="auto" id="pop-09-list" role="group" aria-label="Environments">
    <p class="pop-09__opt pop-09__opt--on">Production · eu-west-1</p>
    <p class="pop-09__opt">Staging · eu-west-1</p>
    <p class="pop-09__opt">Preview · ephemeral per branch</p>
    <p class="pop-09__opt">Local · docker compose</p>
  </div>
</div>
```
## CSS
```css
.pop-09 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --bg: #f4f7fb;
  --surface: #ffffff;
  --ink: #101a2b;
  --muted: #5b6b85;
  --rule: #ccd7e6;
  --brand: #1e5aa8;
  --font-ui: ui-sans-serif, system-ui, "Segoe UI", sans-serif;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--font-ui);
  padding: 40px 18px;
}

.pop-09__stage {
  display: grid;
  place-items: center;
  max-inline-size: 100%;
  min-height: calc(100vh - 80px);
}

.pop-09__form {
  inline-size: 100%;
  max-inline-size: 25rem;
  min-inline-size: 0;
  background: var(--surface);
  border: 1px solid var(--rule);
  border-radius: 6px;
  padding: 20px 18px 18px;
}

.pop-09__legend {
  margin: 0 0 16px;
  font: 700 10px/1 var(--font-ui);
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--brand);
}

.pop-09__label {
  display: block;
  margin-bottom: 6px;
  font-size: 12px;
  font-weight: 600;
  color: var(--muted);
}

.pop-09__field {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  inline-size: 100%;
  min-height: 44px;
  padding: 0 12px;
  font: 500 13.5px/1 var(--font-ui);
  text-align: start;
  color: var(--ink);
  background: var(--surface);
  border: 1px solid var(--rule);
  border-radius: 5px;
  cursor: pointer;
  anchor-name: --pop-09-anchor;
}

.pop-09__field:hover {
  border-color: var(--brand);
}

.pop-09__field:focus-visible {
  outline: 3px solid var(--brand);
  outline-offset: 2px;
}

.pop-09__value {
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.pop-09__chev {
  flex: none;
  color: var(--muted);
}

.pop-09__help {
  margin: 8px 0 14px;
  font-size: 12px;
  color: var(--muted);
}

.pop-09__meta {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}

.pop-09__pill {
  padding: 5px 9px;
  font: 600 10.5px/1.3 ui-monospace, Menlo, monospace;
  color: var(--brand);
  background: color-mix(in oklab, var(--brand) 10%, var(--surface));
  border-radius: 3px;
}

.pop-09__pill--alt {
  color: var(--muted);
  background: var(--bg);
}

.pop-09__list {
  position: fixed;
  margin: 0;
  inline-size: min(23rem, calc(100vw - 32px));
  max-inline-size: calc(100vw - 32px);
  padding: 5px;
  color: var(--ink);
  background: var(--surface);
  border: 1px solid var(--rule);
  border-radius: 5px;
  box-shadow: 0 16px 32px -20px rgba(16, 26, 43, 0.55);
}

@supports (anchor-name: --a) {
  .pop-09__list {
    position-anchor: --pop-09-anchor;
    position-area: block-end span-inline-end;
    inset: auto;
    inline-size: anchor-size(width);
    max-inline-size: calc(100vw - 32px);
    margin-block-start: 6px;
  }
}

.pop-09__opt {
  margin: 0;
  padding: 10px 10px;
  font-size: 13px;
  line-height: 1.3;
  border-radius: 3px;
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.pop-09__opt + .pop-09__opt {
  margin-block-start: 1px;
}

.pop-09__opt--on {
  font-weight: 650;
  color: var(--brand);
  background: color-mix(in oklab, var(--brand) 9%, var(--surface));
}

@media (prefers-color-scheme: dark) {
  .pop-09 {
    --bg: #0d131d;
    --surface: #161e2b;
    --ink: #e9eff8;
    --muted: #8f9fb8;
    --rule: #2a3547;
    --brand: #74a8ee;
  }
}

[data-theme="dark"] .pop-09 {
  --bg: #0d131d;
  --surface: #161e2b;
  --ink: #e9eff8;
  --muted: #8f9fb8;
  --rule: #2a3547;
  --brand: #74a8ee;
}
```
