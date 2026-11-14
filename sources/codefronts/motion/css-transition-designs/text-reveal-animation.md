---
source: "codefronts"
url: "https://codefronts.com/motion/css-transition-designs/text-reveal-animation/"
title: "Custom Easing with the linear Timing Function"
section: "motion"
category: "css-transition-designs"
category_name: "CSS Transitions"
description: "cubic-bezier() can only describe a single smooth curve, so a bounce that settles twice is impossible to express."
has_js: "false"
---

Here's a working CSS Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Custom Easing with the linear Timing Function
Source: https://codefronts.com/motion/css-transition-designs/text-reveal-animation/

cubic-bezier() can only describe a single smooth curve, so a bounce that settles twice is impossible to express. The linear() timing function takes a list of stops instead and approximates springs, bounces and stepped eases directly in a transition. Three markers run the same distance under three linear() strings, each printed beside its track, behind an @supports gate with a bezier fallback declared first.
## HTML
```html
<section class="trn-04" aria-labelledby="trn-04-heading">
  <div class="trn-04__stage">
    <div class="trn-04__theme">
      <input class="trn-04__themecb" type="checkbox" id="trn-04-theme">
      <label class="trn-04__themebtn" for="trn-04-theme">
        <span class="trn-04__themeico" aria-hidden="true">
          <svg class="trn-04__sun" viewBox="0 0 20 20" width="15" height="15"><circle cx="10" cy="10" r="3.9" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M10 1.7v2.1M10 16.2v2.1M1.7 10h2.1M16.2 10h2.1M4.2 4.2l1.5 1.5M14.3 14.3l1.5 1.5M15.8 4.2l-1.5 1.5M5.7 14.3l-1.5 1.5" stroke="currentColor" stroke-width="1.4"/></svg>
          <svg class="trn-04__moon" viewBox="0 0 20 20" width="15" height="15"><path d="M15.4 12.7A6.7 6.7 0 0 1 7.3 4.6a6.8 6.8 0 1 0 8.1 8.1Z" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>
        </span>
        <span>Theme</span>
      </label>
    </div>
    <header class="trn-04__head">
      <p class="trn-04__kicker">timing-function: linear()</p>
      <h2 class="trn-04__heading" id="trn-04-heading">Easing that changes direction</h2>
      <p class="trn-04__sub">One state change, three easing polylines. Every value string is printed as it ships.</p>
    </header>

    <div class="trn-04__lab">
      <input class="trn-04__switch" type="checkbox" id="trn-04-run">
      <label class="trn-04__run" for="trn-04-run"><span class="trn-04__runin">Send</span><span class="trn-04__runout">Return</span></label>

      <ul class="trn-04__list">
        <li class="trn-04__row">
          <div class="trn-04__meta"><span class="trn-04__name">bounce</span><span class="trn-04__tag">settles twice</span></div>
          <div class="trn-04__track"><span class="trn-04__runner trn-04__runner--bounce"><span class="trn-04__chip">Deploy</span></span></div>
          <code class="trn-04__value">linear(0, 1.06 38%, 0.94 55%, 1.02 72%, 0.99 86%, 1)</code>
        </li>
        <li class="trn-04__row">
          <div class="trn-04__meta"><span class="trn-04__name">spring</span><span class="trn-04__tag">one long overshoot</span></div>
          <div class="trn-04__track"><span class="trn-04__runner trn-04__runner--spring"><span class="trn-04__chip">Sync</span></span></div>
          <code class="trn-04__value">linear(0, 0.38 18%, 0.86 38%, 1.12 58%, 1.02 80%, 1)</code>
        </li>
        <li class="trn-04__row">
          <div class="trn-04__meta"><span class="trn-04__name">stepped</span><span class="trn-04__tag">holds mid-flight</span></div>
          <div class="trn-04__track"><span class="trn-04__runner trn-04__runner--step"><span class="trn-04__chip">Invite</span></span></div>
          <code class="trn-04__value">linear(0, 0.3 20%, 0.3 45%, 0.72 62%, 0.72 78%, 1)</code>
        </li>
      </ul>

      <p class="trn-04__gate">Base rule ships <code>cubic-bezier(.34, 1.16, .64, 1)</code>. The polylines are applied inside <code>@supports (transition-timing-function: linear(0, 1))</code>, so an engine without <code>linear()</code> still moves — it just cannot change direction twice.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.trn-04 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --page: #000000;
  --card: #08090b;
  --ink: #f2fff5;
  --ink: oklch(0.98 0.02 155);
  --muted: #7c8a80;
  --muted: oklch(0.63 0.02 155);
  --rule: #1a1d1b;
  --accent: #4dff8f;
  --accent: oklch(0.88 0.21 148);
  --dur: 620ms;
  --font-display: ui-monospace, "JetBrains Mono", Menlo, monospace;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

.trn-04 *,
.trn-04 *::before,
.trn-04 *::after {
  box-sizing: border-box;
}

.trn-04__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  padding: clamp(28px, 6vw, 68px) 16px;
}

.trn-04__head {
  inline-size: 100%;
  max-inline-size: 56rem;
  min-inline-size: 0;
  margin: 0 0 32px;
}

.trn-04__kicker {
  margin: 0 0 14px;
  font: 400 11.5px/1 var(--font-display);
  letter-spacing: 0.1em;
  color: var(--accent);
}

.trn-04__heading {
  margin: 0 0 12px;
  font: 400 clamp(26px, 5vw, 40px)/1.08 var(--font-display);
  letter-spacing: -0.03em;
  text-wrap: balance;
}

.trn-04__sub {
  margin: 0;
  max-inline-size: 50ch;
  font-size: 14.5px;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.trn-04__lab {
  inline-size: 100%;
  max-inline-size: 56rem;
  min-inline-size: 0;
}

.trn-04__switch {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  clip-path: inset(50%);
  overflow: hidden;
}

.trn-04__run {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 44px;
  min-inline-size: 118px;
  padding: 0 20px;
  border: 1px solid var(--accent);
  border-radius: 999px;
  cursor: pointer;
  font: 500 13px/1 var(--font-display);
  letter-spacing: 0.06em;
  color: var(--accent);
  text-transform: uppercase;
  transition: background-color 200ms ease, color 200ms ease;
}

.trn-04__run:hover {
  background: rgba(77, 255, 143, 0.12);
}

.trn-04__switch:focus-visible + .trn-04__run {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.trn-04__switch:checked + .trn-04__run {
  background: var(--accent);
  color: #000;
}

.trn-04__runout {
  display: none;
}

.trn-04__switch:checked + .trn-04__run .trn-04__runin {
  display: none;
}

.trn-04__switch:checked + .trn-04__run .trn-04__runout {
  display: inline;
}

.trn-04__list {
  list-style: none;
  margin: 34px 0 0;
  padding: 0;
  display: grid;
  gap: 30px;
}

.trn-04__row {
  min-inline-size: 0;
  display: grid;
  gap: 10px;
}

.trn-04__meta {
  display: flex;
  flex-wrap: wrap;
  gap: 4px 12px;
  align-items: baseline;
}

.trn-04__name {
  font: 500 15px/1 var(--font-display);
  color: var(--ink);
}

.trn-04__tag {
  font-size: 12px;
  color: var(--muted);
}

.trn-04__track {
  position: relative;
  block-size: 38px;
  border-block-end: 1px solid var(--rule);
}

.trn-04__runner {
  position: absolute;
  inset-block-start: 0;
  inset-inline-start: 0;
  inline-size: 100%;
  transition: transform var(--dur) cubic-bezier(.34, 1.16, .64, 1);
}

.trn-04__chip {
  display: inline-flex;
  align-items: center;
  min-height: 30px;
  padding: 0 12px;
  background: var(--card);
  border: 1px solid var(--accent);
  border-radius: 4px;
  font: 500 12px/1 var(--font-display);
  color: var(--accent);
  box-shadow: 0 0 22px -6px var(--accent);
}

.trn-04:has(#trn-04-run:checked) .trn-04__runner {
  transform: translateX(calc(100% - 78px));
}

@supports (transition-timing-function: linear(0, 1)) {
  .trn-04__runner--bounce {
    transition-timing-function: linear(0, 1.06 38%, 0.94 55%, 1.02 72%, 0.99 86%, 1);
  }

  .trn-04__runner--spring {
    transition-timing-function: linear(0, 0.38 18%, 0.86 38%, 1.12 58%, 1.02 80%, 1);
  }

  .trn-04__runner--step {
    transition-timing-function: linear(0, 0.3 20%, 0.3 45%, 0.72 62%, 0.72 78%, 1);
  }
}

.trn-04__value {
  display: block;
  font: 400 11.5px/1.55 var(--font-display);
  color: var(--muted);
  overflow-wrap: anywhere;
}

.trn-04__gate {
  margin: 34px 0 0;
  padding: 14px 16px;
  border: 1px solid var(--rule);
  border-radius: 6px;
  font-size: 12.5px;
  line-height: 1.65;
  color: var(--muted);
}

.trn-04__gate code {
  font: 400 11.5px/1 var(--font-display);
  color: var(--ink);
  overflow-wrap: anywhere;
}

@media (prefers-reduced-motion: reduce) {
  .trn-04__runner {
    transition: transform 160ms linear, opacity 160ms linear;
  }

  .trn-04__runner--bounce,
    .trn-04__runner--spring,
    .trn-04__runner--step {
    transition-timing-function: linear;
  }

  .trn-04:has(#trn-04-run:checked) .trn-04__runner {
    transform: translateX(calc(100% - 78px));
  }
}

@media (prefers-color-scheme: light) {
  .trn-04 {
    --page: #fbfdfb;
    --card: #ffffff;
    --ink: #0a1410;
    --muted: #5c6b62;
    --rule: #dde5e0;
    --accent: #0f7d43;
  }

  .trn-04__chip {
    box-shadow: 0 2px 10px -4px rgba(15, 125, 67, 0.5);
  }

  .trn-04__switch:checked + .trn-04__run {
    color: #fbfdfb;
  }
}

[data-theme="dark"] .trn-04 {
  --page: #000000;
  --card: #08090b;
  --ink: #f2fff5;
  --muted: #7c8a80;
  --rule: #1a1d1b;
  --accent: #4dff8f;
}

[data-theme="dark"] .trn-04__chip {
  box-shadow: 0 0 22px -6px var(--accent);
}

[data-theme="dark"] .trn-04__switch:checked + .trn-04__run {
  color: #000;
}

.trn-04__theme {
  position: relative;
  inline-size: 100%;
  min-inline-size: 0;
  display: flex;
  justify-content: flex-end;
  margin: 0 0 14px;
}

.trn-04__themecb {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  clip-path: inset(50%);
  overflow: hidden;
}

.trn-04__themebtn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  min-height: 44px;
  padding: 0 14px;
  border: 1px solid currentColor;
  border-radius: 999px;
  cursor: pointer;
  color: var(--muted);
  font: 500 11px/1 ui-monospace, Menlo, monospace;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  transition: color 200ms ease, opacity 200ms ease;
}

.trn-04__themebtn:hover {
  color: var(--ink);
}

.trn-04__themecb:focus-visible + .trn-04__themebtn {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.trn-04__themeico {
  display: grid;
  place-items: center;
  inline-size: 15px;
  block-size: 15px;
}

.trn-04__themeico svg {
  grid-area: 1 / 1;
  transition: opacity 200ms ease;
}

.trn-04__sun {
  opacity: 0.34;
}

.trn-04__moon {
  opacity: 1;
}

.trn-04:has(#trn-04-theme:checked) .trn-04__sun {
  opacity: 1;
}

.trn-04:has(#trn-04-theme:checked) .trn-04__moon {
  opacity: 0.34;
}

@media (prefers-color-scheme: dark) {
  .trn-04:has(#trn-04-theme:checked) {
    --page: #fbfdfb;
    --card: #ffffff;
    --ink: #0a1410;
    --muted: #5c6b62;
    --rule: #dde5e0;
    --accent: #0f7d43;
  }

  .trn-04:has(#trn-04-theme:checked) .trn-04__chip {
    box-shadow: 0 2px 10px -4px rgba(15, 125, 67, 0.5);
  }

  .trn-04:has(#trn-04-theme:checked) .trn-04__switch:checked + .trn-04__run {
    color: #fbfdfb;
  }
}

@media (prefers-color-scheme: light) {
  .trn-04:has(#trn-04-theme:checked) {
    --page: #000000;
    --card: #08090b;
    --ink: #f2fff5;
    --ink: oklch(0.98 0.02 155);
    --muted: #7c8a80;
    --muted: oklch(0.63 0.02 155);
    --rule: #1a1d1b;
    --accent: #4dff8f;
    --accent: oklch(0.88 0.21 148);
    --dur: 620ms;
    --font-display: ui-monospace, "JetBrains Mono", Menlo, monospace;
    background: var(--page);
  }

  .trn-04:has(#trn-04-theme:checked) .trn-04__chip {
    display: inline-flex;
    align-items: center;
    min-height: 30px;
    padding: 0 12px;
    background: var(--card);
    border: 1px solid var(--accent);
    border-radius: 4px;
    font: 500 12px/1 var(--font-display);
    color: var(--accent);
    box-shadow: 0 0 22px -6px var(--accent);
  }

  .trn-04:has(#trn-04-theme:checked) .trn-04__switch:checked + .trn-04__run {
    background: var(--accent);
    color: #000;
  }

  .trn-04:has(#trn-04-theme:checked) .trn-04__sun {
    opacity: 0.34;
  }

  .trn-04:has(#trn-04-theme:checked) .trn-04__moon {
    opacity: 1;
  }
}
```
