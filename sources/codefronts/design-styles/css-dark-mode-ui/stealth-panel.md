---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-dark-mode-ui/stealth-panel/"
title: "Stealth Panel Minimalist Dark UI"
section: "design-styles"
category: "css-dark-mode-ui"
category_name: "CSS Dark Mode UI"
description: "Maximum restraint: no borders, no shadows, no second accent — just surface separation, one hue and a lot of air."
has_js: "false"
---

Here's a working CSS Dark Mode UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Stealth Panel Minimalist Dark UI
Source: https://codefronts.com/design-styles/css-dark-mode-ui/stealth-panel/

Maximum restraint: no borders, no shadows, no second accent — just surface separation, one hue and a lot of air. A settings panel with four preference rows covering the four control types you actually ship (checkbox, switch, radio pair, select), all styled from the same three tokens. Ghost buttons only. The theme toggle is one of the rows, so the control lives where a user would look for it.
## HTML
```html
<div class="dmu-12">
  <div class="dmu-12__stage">
    <section class="dmu-12__panel" aria-labelledby="dmu-12-h">
      <header class="dmu-12__head">
        <h1 class="dmu-12__h1" id="dmu-12-h">Preferences</h1>
        <p class="dmu-12__sub">Workspace defaults for Sam Rivera</p>
      </header>

      <div class="dmu-12__rows">
        <label class="dmu-12__row" for="dmu-12-digest">
          <span class="dmu-12__rowText">
            <span class="dmu-12__rowTitle">Weekly digest</span>
            <span class="dmu-12__rowDesc">One summary email each Monday at 09:00.</span>
          </span>
          <span class="dmu-12__check">
            <input type="checkbox" id="dmu-12-digest" checked>
            <span class="dmu-12__box" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12.6 4.4 4.4L19 7.4"/></svg>
            </span>
          </span>
        </label>

        <label class="dmu-12__row" for="dmu-12-toggle">
          <span class="dmu-12__rowText">
            <span class="dmu-12__rowTitle">Dark appearance</span>
            <span class="dmu-12__rowDesc">Overrides your system setting for this workspace.</span>
          </span>
          <span class="dmu-12__switch">
            <input type="checkbox" id="dmu-12-toggle">
            <span class="dmu-12__track" aria-hidden="true"><span class="dmu-12__knob"></span></span>
          </span>
        </label>

        <div class="dmu-12__row dmu-12__row--radios" role="group" aria-labelledby="dmu-12-view-label">
          <span class="dmu-12__rowText">
            <span class="dmu-12__rowTitle" id="dmu-12-view-label">Default view</span>
            <span class="dmu-12__rowDesc">Where new sessions land.</span>
          </span>
          <span class="dmu-12__radios">
            <input type="radio" name="dmu-12-view" id="dmu-12-board" checked>
            <label class="dmu-12__radio" for="dmu-12-board"><span aria-hidden="true"></span>Board</label>
            <input type="radio" name="dmu-12-view" id="dmu-12-list">
            <label class="dmu-12__radio" for="dmu-12-list"><span aria-hidden="true"></span>List</label>
          </span>
        </div>

        <label class="dmu-12__row" for="dmu-12-tz">
          <span class="dmu-12__rowText">
            <span class="dmu-12__rowTitle">Time zone</span>
            <span class="dmu-12__rowDesc">Used for schedules and digests.</span>
          </span>
          <span class="dmu-12__selectWrap">
            <select class="dmu-12__select" id="dmu-12-tz">
              <option>Europe/London</option>
              <option selected>America/New_York</option>
              <option>Asia/Singapore</option>
              <option>Australia/Sydney</option>
            </select>
            <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m8 10 4 4 4-4"/></svg>
          </span>
        </label>
      </div>

      <footer class="dmu-12__foot">
        <button class="dmu-12__ghost" type="button">Reset to defaults</button>
        <button class="dmu-12__ghost dmu-12__ghost--accent" type="button">Save changes</button>
      </footer>
    </section>
  </div>
</div>
```
## CSS
```css
.dmu-12 {
  --bg: #0b0b0e;
  --panel: #111114;
  --row: #17171c;
  --row-hover: #1e1e25;
  --field: #101014;
  --ink: #f0f0f2;
  --muted: #8b8b94;
  --accent: #c084fc;
  --accent-ink: #1c0a2e;
  --focus: #d8b4fe;
  --row-gap: .35rem;
  --sans: system-ui,-apple-system,"Segoe UI",sans-serif;
  color-scheme: dark;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.dmu-12[data-theme="light"],
.dmu-12:has(#dmu-12-toggle:checked) {
  --bg: #f4f4f6;
  --panel: #ffffff;
  --row: #f6f6f8;
  --row-hover: #eeeef1;
  --field: #ffffff;
  --ink: #101014;
  --muted: #62626e;
  --accent: #7c3aed;
  --accent-ink: #ffffff;
  --focus: #7c3aed;
  color-scheme: light;
}

@media (prefers-color-scheme: light) {
  .dmu-12:not([data-theme="dark"]):not(:has(#dmu-12-toggle:checked)) {
    --bg: #f4f4f6;
    --panel: #ffffff;
    --row: #f6f6f8;
    --row-hover: #eeeef1;
    --field: #ffffff;
    --ink: #101014;
    --muted: #62626e;
    --accent: #7c3aed;
    --accent-ink: #ffffff;
    --focus: #7c3aed;
    color-scheme: light;
  }
  /* flip-back: light OS + switch on restores the dark base */

  .dmu-12:has(#dmu-12-toggle:checked) {
    --bg: #0b0b0e;
    --panel: #111114;
    --row: #17171c;
    --row-hover: #1e1e25;
    --field: #101014;
    --ink: #f0f0f2;
    --muted: #8b8b94;
    --accent: #c084fc;
    --accent-ink: #1c0a2e;
    --focus: #d8b4fe;
    color-scheme: dark;
  }
}

.dmu-12,
.dmu-12 *,
.dmu-12 *::before,
.dmu-12 *::after {
  box-sizing: border-box;
}

.dmu-12__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3rem);
}

.dmu-12__panel {
  width: min(44rem,100%);
  display: grid;
  gap: 1.25rem;
  padding: clamp(1.4rem,4vw,2.4rem);
  border-radius: 1.3rem;
  background: var(--panel);
}

.dmu-12__head {
  display: grid;
  gap: .3rem;
}

.dmu-12__h1 {
  margin: 0;
  font-size: clamp(1.3rem,3vw,1.7rem);
  font-weight: 600;
  letter-spacing: -.03em;
}

.dmu-12__sub {
  margin: 0;
  font-size: .85rem;
  color: var(--muted);
}

.dmu-12__rows {
  display: grid;
  gap: var(--row-gap);
}

.dmu-12__row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1.25rem;
  flex-wrap: wrap;
  margin: 0;
  padding: 1rem 1.1rem;
  border: 0;
  border-radius: .9rem;
  background: var(--row);
  cursor: pointer;
  transition: background-color .2s ease;
}

.dmu-12__row:hover {
  background: var(--row-hover);
}

.dmu-12__row--radios {
  cursor: default;
}

.dmu-12__rowText {
  display: grid;
  gap: .2rem;
  padding: 0;
}

.dmu-12__rowTitle {
  display: block;
  font-size: .92rem;
  font-weight: 550;
}

.dmu-12__rowDesc {
  display: block;
  font-size: .8rem;
  color: var(--muted);
}

.dmu-12__check input,
.dmu-12__switch input,
.dmu-12__radios input {
  position: absolute;
  opacity: 0;
  width: 1px;
  height: 1px;
}

.dmu-12__box {
  display: grid;
  place-items: center;
  width: 1.4rem;
  height: 1.4rem;
  border-radius: .4rem;
  background: var(--field);
  color: var(--accent-ink);
  box-shadow: inset 0 0 0 1px color-mix(in oklab,var(--ink) 14%,transparent);
  transition: background-color .18s ease;
}

.dmu-12__box svg {
  width: .9rem;
  height: .9rem;
  opacity: 0;
}

.dmu-12__check:has(input:checked) .dmu-12__box {
  background: var(--accent);
  box-shadow: none;
}

.dmu-12__check:has(input:checked) .dmu-12__box svg {
  opacity: 1;
}

.dmu-12__check:has(input:focus-visible) .dmu-12__box {
  outline: 2px solid var(--focus);
  outline-offset: 3px;
}

.dmu-12__track {
  position: relative;
  display: block;
  width: 3.1rem;
  height: 1.75rem;
  border-radius: 999px;
  background: color-mix(in oklab,var(--ink) 12%,transparent);
  transition: background-color .22s ease;
}

.dmu-12__knob {
  position: absolute;
  top: .2rem;
  left: .2rem;
  width: 1.35rem;
  height: 1.35rem;
  border-radius: 50%;
  background: var(--panel);
  box-shadow: 0 1px 3px rgba(0,0,0,.5);
  transition: translate .26s cubic-bezier(.16,1,.3,1);
}

.dmu-12__switch:has(input:checked) .dmu-12__track {
  background: var(--accent);
}

.dmu-12__switch:has(input:checked) .dmu-12__knob {
  translate: 1.35rem 0;
}

.dmu-12__switch:has(input:focus-visible) .dmu-12__track {
  outline: 2px solid var(--focus);
  outline-offset: 3px;
}

.dmu-12__radios {
  display: flex;
  gap: .35rem;
}

.dmu-12__radio {
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  min-height: 2.4rem;
  padding: 0 .85rem;
  border-radius: .6rem;
  cursor: pointer;
  font-size: .84rem;
  color: var(--muted);
  background: var(--field);
  transition: color .18s ease, background-color .18s ease;
}

.dmu-12__radio span {
  width: .7rem;
  height: .7rem;
  border-radius: 50%;
  box-shadow: inset 0 0 0 1px color-mix(in oklab,var(--ink) 22%,transparent);
}

.dmu-12__radios input:checked + .dmu-12__radio {
  color: var(--ink);
  background: var(--row-hover);
}

.dmu-12__radios input:checked + .dmu-12__radio span {
  background: var(--accent);
  box-shadow: none;
}

.dmu-12__radios input:focus-visible + .dmu-12__radio {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}

.dmu-12__selectWrap {
  position: relative;
  display: inline-grid;
  align-items: center;
}

.dmu-12__select {
  appearance: none;
  -webkit-appearance: none;
  min-height: 2.6rem;
  padding: 0 2.2rem 0 .85rem;
  border: 0;
  border-radius: .6rem;
  font: inherit;
  font-size: .85rem;
  cursor: pointer;
  background: var(--field);
  color: var(--ink);
  color-scheme: inherit;
}

.dmu-12__select:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}

.dmu-12__selectWrap svg {
  position: absolute;
  right: .6rem;
  width: 1rem;
  height: 1rem;
  pointer-events: none;
  color: var(--muted);
}

.dmu-12__foot {
  display: flex;
  gap: .5rem;
  justify-content: flex-end;
  flex-wrap: wrap;
}

.dmu-12__ghost {
  min-height: 2.7rem;
  padding: 0 1.05rem;
  border: 0;
  border-radius: .65rem;
  cursor: pointer;
  font: inherit;
  font-size: .85rem;
  font-weight: 550;
  background: transparent;
  color: var(--muted);
  transition: background-color .18s ease, color .18s ease;
}

.dmu-12__ghost:hover {
  background: var(--row);
  color: var(--ink);
}

.dmu-12__ghost:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}

.dmu-12__ghost--accent {
  color: var(--accent);
}

.dmu-12__ghost--accent:hover {
  background: color-mix(in oklab,var(--accent) 14%,transparent);
  color: var(--accent);
}

@media (prefers-reduced-motion: reduce) {
  .dmu-12__row,
    .dmu-12__knob,
    .dmu-12__track,
    .dmu-12__box,
    .dmu-12__radio,
    .dmu-12__ghost {
    transition: none;
  }
}

@media (forced-colors: active) {
  .dmu-12__row,
    .dmu-12__panel {
    border: 1px solid CanvasText;
  }

  .dmu-12__switch:has(input:checked) .dmu-12__track,
    .dmu-12__check:has(input:checked) .dmu-12__box {
    background: Highlight;
  }
}
```
