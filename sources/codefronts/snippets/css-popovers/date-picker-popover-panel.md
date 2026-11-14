---
source: "codefronts"
url: "https://codefronts.com/snippets/css-popovers/date-picker-popover-panel/"
title: "Date Picker Popover Panel"
section: "snippets"
category: "css-popovers"
category_name: "CSS Popovers"
description: "A calendar panel tethered to a date field, with the month laid out as a plain CSS grid and no date logic at all."
has_js: "false"
---

Here's a working CSS Popover from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Date Picker Popover Panel
Source: https://codefronts.com/snippets/css-popovers/date-picker-popover-panel/

A calendar panel tethered to a date field, with the month laid out as a plain CSS grid and no date logic at all. The demo is the panel and its tethering: how a popover attaches to an input, how the grid stays legible at 320px, and why the field needs readonly or a real picker behind it before this ships.
## HTML
```html
<div class="pop-14">
  <div class="pop-14__stage">
    <div class="pop-14__form">
      <p class="pop-14__kicker">Booking · Studio 2</p>
      <label class="pop-14__label" for="pop-14-date">Session date</label>
      <div class="pop-14__field">
        <input class="pop-14__input" id="pop-14-date" type="text" value="14 September 2026" readonly aria-describedby="pop-14-help">
        <button class="pop-14__icon" type="button" popovertarget="pop-14-cal" aria-label="Choose a date">
          <svg viewBox="0 0 20 20" width="17" height="17" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="3" y="4.6" width="14" height="12" rx="2"/><path d="M3 8.4h14M7 3v2.6M13 3v2.6"/></svg>
        </button>
      </div>
      <p class="pop-14__help" id="pop-14-help">The field is the anchor. The icon button is only the invoker.</p>
    </div>
  </div>

  <div class="pop-14__cal" popover="auto" id="pop-14-cal" role="group" aria-label="September 2026">
    <div class="pop-14__calhead">
      <span class="pop-14__month">September 2026</span>
      <span class="pop-14__static">static month</span>
    </div>
    <div class="pop-14__dows" aria-hidden="true">
      <span>M</span><span>T</span><span>W</span><span>T</span><span>F</span><span>S</span><span>S</span>
    </div>
    <div class="pop-14__grid" role="grid" aria-label="Days in September 2026">
      <span class="pop-14__day pop-14__day--mute">31</span>
      <span class="pop-14__day">1</span><span class="pop-14__day">2</span><span class="pop-14__day">3</span><span class="pop-14__day">4</span><span class="pop-14__day">5</span><span class="pop-14__day">6</span>
      <span class="pop-14__day">7</span><span class="pop-14__day">8</span><span class="pop-14__day">9</span><span class="pop-14__day">10</span><span class="pop-14__day">11</span><span class="pop-14__day">12</span><span class="pop-14__day">13</span>
      <span class="pop-14__day pop-14__day--sel" aria-selected="true">14</span><span class="pop-14__day">15</span><span class="pop-14__day">16</span><span class="pop-14__day pop-14__day--now" aria-current="date">17</span><span class="pop-14__day">18</span><span class="pop-14__day">19</span><span class="pop-14__day">20</span>
      <span class="pop-14__day">21</span><span class="pop-14__day">22</span><span class="pop-14__day">23</span><span class="pop-14__day">24</span><span class="pop-14__day">25</span><span class="pop-14__day">26</span><span class="pop-14__day">27</span>
      <span class="pop-14__day">28</span><span class="pop-14__day">29</span><span class="pop-14__day">30</span>
      <span class="pop-14__day pop-14__day--mute">1</span><span class="pop-14__day pop-14__day--mute">2</span><span class="pop-14__day pop-14__day--mute">3</span><span class="pop-14__day pop-14__day--mute">4</span>
    </div>
  </div>
</div>
```
## CSS
```css
.pop-14 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --bg: #f0ebe3;
  --surface: #fffdf9;
  --ink: #26221c;
  --muted: #7b7062;
  --rule: #ddd4c6;
  --sel: #3f6a4e;
  --font-ui: ui-sans-serif, system-ui, "Segoe UI", sans-serif;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--font-ui);
  padding: 40px 18px;
}

.pop-14__stage {
  display: grid;
  place-items: center;
  max-inline-size: 100%;
  min-height: calc(100vh - 80px);
}

.pop-14__form {
  inline-size: 100%;
  max-inline-size: 24rem;
  min-inline-size: 0;
  background: var(--surface);
  border: 1px solid var(--rule);
  border-radius: 8px;
  padding: 20px 18px 18px;
}

.pop-14__kicker {
  margin: 0 0 16px;
  font: 700 10px/1 var(--font-ui);
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--sel);
}

.pop-14__label {
  display: block;
  margin-bottom: 6px;
  font-size: 12px;
  font-weight: 600;
  color: var(--muted);
}

.pop-14__field {
  display: flex;
  align-items: center;
  gap: 4px;
  padding-inline-end: 4px;
  background: var(--surface);
  border: 1px solid var(--rule);
  border-radius: 7px;
  anchor-name: --pop-14-anchor;
}

.pop-14__field:focus-within {
  border-color: var(--sel);
}

.pop-14__input {
  flex: 1 1 auto;
  min-inline-size: 0;
  min-height: 44px;
  padding: 0 12px;
  font: 500 13.5px/1 var(--font-ui);
  color: var(--ink);
  background: transparent;
  border: 0;
  border-radius: 7px 0 0 7px;
}

.pop-14__input:focus-visible {
  outline: 3px solid var(--sel);
  outline-offset: -1px;
}

.pop-14__icon {
  flex: none;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 44px;
  min-height: 44px;
  color: var(--muted);
  background: transparent;
  border: 0;
  border-radius: 6px;
  cursor: pointer;
}

.pop-14__icon:hover {
  color: var(--sel);
  background: var(--bg);
}

.pop-14__icon:focus-visible {
  outline: 3px solid var(--sel);
  outline-offset: -2px;
}

.pop-14__help {
  margin: 9px 0 0;
  font-size: 12px;
  line-height: 1.6;
  color: var(--muted);
}

.pop-14__cal {
  position: fixed;
  margin: 0;
  inline-size: min(20rem, calc(100vw - 28px));
  max-inline-size: calc(100vw - 28px);
  padding: 14px;
  color: var(--ink);
  background: var(--surface);
  border: 1px solid var(--rule);
  border-radius: 8px;
  box-shadow: 0 22px 44px -26px rgba(38, 34, 28, 0.5);
}

@supports (anchor-name: --a) {
  .pop-14__cal {
    position-anchor: --pop-14-anchor;
    position-area: block-end span-inline-end;
    inset: auto;
    margin-block-start: 7px;
    position-try-fallbacks: flip-block;
  }
}

.pop-14__calhead {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 10px;
  margin-bottom: 12px;
}

.pop-14__month {
  font-size: 13px;
  font-weight: 650;
}

.pop-14__static {
  font: 600 9.5px/1 var(--font-ui);
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--muted);
}

.pop-14__dows,
.pop-14__grid {
  display: grid;
  grid-template-columns: repeat(7, minmax(0, 1fr));
  gap: 2px;
}

.pop-14__dows {
  margin-bottom: 4px;
}

.pop-14__dows span {
  text-align: center;
  font: 700 10px/1 var(--font-ui);
  color: var(--muted);
}

.pop-14__day {
  display: grid;
  place-items: center;
  aspect-ratio: 1;
  min-height: 34px;
  font-size: 12.5px;
  font-variant-numeric: tabular-nums;
  border-radius: 6px;
}

.pop-14__day--mute {
  color: color-mix(in oklab, var(--muted) 55%, transparent);
}

.pop-14__day--now {
  box-shadow: inset 0 0 0 1px var(--muted);
}

.pop-14__day--sel {
  font-weight: 700;
  color: var(--surface);
  background: var(--sel);
  box-shadow: inset 0 0 0 2px var(--sel);
}

@media (min-width: 420px) {
  .pop-14__day {
    min-height: 38px;
  }
}

@media (prefers-color-scheme: dark) {
  .pop-14 {
    --bg: #17140f;
    --surface: #211d17;
    --ink: #f2ece1;
    --muted: #a39682;
    --rule: #362f26;
    --sel: #7fb894;
  }

  .pop-14__day--sel {
    color: #17140f;
  }
}

[data-theme="dark"] .pop-14 {
  --bg: #17140f;
  --surface: #211d17;
  --ink: #f2ece1;
  --muted: #a39682;
  --rule: #362f26;
  --sel: #7fb894;
}

[data-theme="dark"] .pop-14 .pop-14__day--sel {
  color: #17140f;
}
```
