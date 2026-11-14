---
source: "codefronts"
url: "https://codefronts.com/motion/css-transition-designs/button-hover-transitions/"
title: "CSS Transition Property Reference and Timing"
section: "motion"
category: "css-transition-designs"
category_name: "CSS Transitions"
description: "The reference build the rest of the collection borrows from: three buttons that spell out the shorthand order, an annotated panel naming every longhand it…"
has_js: "false"
---

Here's a working CSS Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Transition Property Reference and Timing
Source: https://codefronts.com/motion/css-transition-designs/button-hover-transitions/

The reference build the rest of the collection borrows from: three buttons that spell out the shorthand order, an annotated panel naming every longhand it expands to, and three identical markers running the same distance under ease, ease-in-out and a custom cubic-bezier() so the curves are visually distinguishable. Includes the beginner trap where two bare time values are silently read as duration then delay.
## HTML
```html
<section class="trn-01" aria-labelledby="trn-01-heading">
  <div class="trn-01__stage">
    <div class="trn-01__theme">
      <input class="trn-01__themecb" type="checkbox" id="trn-01-theme">
      <label class="trn-01__themebtn" for="trn-01-theme">
        <span class="trn-01__themeico" aria-hidden="true">
          <svg class="trn-01__sun" viewBox="0 0 20 20" width="15" height="15"><circle cx="10" cy="10" r="3.9" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M10 1.7v2.1M10 16.2v2.1M1.7 10h2.1M16.2 10h2.1M4.2 4.2l1.5 1.5M14.3 14.3l1.5 1.5M15.8 4.2l-1.5 1.5M5.7 14.3l-1.5 1.5" stroke="currentColor" stroke-width="1.4"/></svg>
          <svg class="trn-01__moon" viewBox="0 0 20 20" width="15" height="15"><path d="M15.4 12.7A6.7 6.7 0 0 1 7.3 4.6a6.8 6.8 0 1 0 8.1 8.1Z" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>
        </span>
        <span>Theme</span>
      </label>
    </div>
    <header class="trn-01__head">
      <p class="trn-01__kicker">transition · reference</p>
      <h2 class="trn-01__heading" id="trn-01-heading">The shorthand, its longhands, and the curve</h2>
      <p class="trn-01__sub">Three slots you can reorder, two you cannot. Everything below runs on state change only.</p>
    </header>

    <div class="trn-01__grid">
      <article class="trn-01__panel">
        <h3 class="trn-01__ptitle">01 · Shorthand order</h3>
        <p class="trn-01__note">Hover or focus each button. The rule it runs is printed underneath it.</p>
        <div class="trn-01__row">
          <div class="trn-01__unit">
            <button class="trn-01__btn trn-01__btn--a" type="button">Deploy to production</button>
            <code class="trn-01__code">transition: background-color 180ms ease</code>
          </div>
          <div class="trn-01__unit">
            <button class="trn-01__btn trn-01__btn--b" type="button">Sync 4 repositories</button>
            <code class="trn-01__code">transition: transform 320ms cubic-bezier(.34,1.2,.64,1)</code>
          </div>
          <div class="trn-01__unit">
            <button class="trn-01__btn trn-01__btn--c" type="button">Invite teammate</button>
            <code class="trn-01__code">transition: color 200ms ease-out 90ms</code>
          </div>
        </div>
      </article>

      <article class="trn-01__panel">
        <h3 class="trn-01__ptitle">02 · What the shorthand expands to</h3>
        <dl class="trn-01__spec">
          <dt>transition-property</dt><dd>transform</dd>
          <dt>transition-duration</dt><dd>320ms &nbsp;<span class="trn-01__hint">first time value</span></dd>
          <dt>transition-timing-function</dt><dd>cubic-bezier(.34, 1.2, .64, 1)</dd>
          <dt>transition-delay</dt><dd>80ms &nbsp;<span class="trn-01__hint">second time value</span></dd>
          <dt>transition-behavior</dt><dd>normal &nbsp;<span class="trn-01__hint">see demo 08</span></dd>
        </dl>
        <p class="trn-01__trap"><svg viewBox="0 0 16 16" width="15" height="15" aria-hidden="true"><path d="M8 1.6 15 14H1L8 1.6Z" fill="none" stroke="currentColor" stroke-width="1.4"/><path d="M8 6v4M8 11.6v.9" stroke="currentColor" stroke-width="1.4"/></svg><span><strong>The order trap.</strong> <code>opacity 2s 1s</code> is a 2s fade delayed by 1s — not a 1s fade delayed by 2s. Only the sequence tells them apart.</span></p>
      </article>

      <article class="trn-01__panel trn-01__panel--wide">
        <h3 class="trn-01__ptitle">03 · Same distance, same duration, three curves</h3>
        <div class="trn-01__lab">
          <input class="trn-01__switch" type="checkbox" id="trn-01-run">
          <label class="trn-01__runbtn" for="trn-01-run">
            <svg viewBox="0 0 16 16" width="14" height="14" aria-hidden="true"><path d="M4 3l9 5-9 5V3Z" fill="currentColor"/></svg>
            <span>Run the three curves</span>
          </label>
          <ul class="trn-01__tracks">
            <li class="trn-01__trackrow">
              <span class="trn-01__tlabel">ease</span>
              <span class="trn-01__track"><span class="trn-01__runner trn-01__runner--ease"><span class="trn-01__dot"></span></span></span>
              <code class="trn-01__tvalue">cubic-bezier(.25,.1,.25,1)</code>
            </li>
            <li class="trn-01__trackrow">
              <span class="trn-01__tlabel">ease-in-out</span>
              <span class="trn-01__track"><span class="trn-01__runner trn-01__runner--io"><span class="trn-01__dot"></span></span></span>
              <code class="trn-01__tvalue">cubic-bezier(.42,0,.58,1)</code>
            </li>
            <li class="trn-01__trackrow">
              <span class="trn-01__tlabel">overshoot</span>
              <span class="trn-01__track"><span class="trn-01__runner trn-01__runner--over"><span class="trn-01__dot"></span></span></span>
              <code class="trn-01__tvalue">cubic-bezier(.34,1.2,.64,1)</code>
            </li>
          </ul>
        </div>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
.trn-01 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --page: #f4f7fb;
  --page: oklch(0.97 0.008 250);
  --grid: #dfe7f2;
  --grid: oklch(0.92 0.017 248);
  --card: #ffffff;
  --ink: #101a2b;
  --ink: oklch(0.21 0.028 258);
  --muted: #5a6a83;
  --muted: oklch(0.51 0.031 252);
  --rule: #cdd8e8;
  --rule: oklch(0.87 0.02 250);
  --accent: #1d5fd6;
  --accent: oklch(0.52 0.185 261);
  --dur: 320ms;
  --travel: 100%;
  --font-display: ui-monospace, "JetBrains Mono", "SFMono-Regular", Menlo, monospace;
  background: linear-gradient(var(--grid) 1px, transparent 1px) 0 0 / 100% 28px, linear-gradient(90deg, var(--grid) 1px, transparent 1px) 0 0 / 28px 100%, var(--page);
  color: var(--ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

.trn-01 *,
.trn-01 *::before,
.trn-01 *::after {
  box-sizing: border-box;
}

.trn-01__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  padding: clamp(24px, 5vw, 56px) 16px;
}

.trn-01__head {
  inline-size: 100%;
  max-inline-size: 60rem;
  min-inline-size: 0;
  margin: 0 0 24px;
}

.trn-01__kicker {
  margin: 0 0 10px;
  font: 500 11px/1 var(--font-display);
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--accent);
}

.trn-01__heading {
  margin: 0 0 10px;
  font: 500 clamp(23px, 4.4vw, 34px)/1.15 var(--font-display);
  letter-spacing: -0.02em;
  text-wrap: balance;
}

.trn-01__sub {
  margin: 0;
  max-inline-size: 52ch;
  font-size: 14.5px;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.trn-01__grid {
  inline-size: 100%;
  max-inline-size: 60rem;
  min-inline-size: 0;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 17rem), 1fr));
  gap: 18px;
}

.trn-01__panel {
  min-inline-size: 0;
  padding: 18px;
  background: var(--card);
  border: 1px solid var(--rule);
  border-radius: 4px;
  box-shadow: 0 1px 0 var(--rule);
}

.trn-01__panel--wide {
  grid-column: 1 / -1;
}

.trn-01__ptitle {
  margin: 0 0 6px;
  padding-block-end: 8px;
  border-block-end: 1px solid var(--rule);
  font: 500 11.5px/1.3 var(--font-display);
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--muted);
}

.trn-01__note {
  margin: 10px 0 14px;
  font-size: 13px;
  line-height: 1.55;
  color: var(--muted);
}

.trn-01__row {
  display: grid;
  gap: 14px;
}

.trn-01__unit {
  display: grid;
  gap: 7px;
  min-inline-size: 0;
}

.trn-01__btn {
  min-height: 44px;
  padding: 0 16px;
  border: 1px solid var(--accent);
  border-radius: 3px;
  font: 500 13.5px/1 system-ui, sans-serif;
  color: var(--accent);
  background: var(--card);
  cursor: pointer;
  justify-self: start;
  max-inline-size: 100%;
}

.trn-01__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.trn-01__btn--a {
  transition: background-color 180ms ease, color 180ms ease;
}

.trn-01__btn--a:hover,
.trn-01__btn--a:focus-visible {
  background: var(--accent);
  color: #fff;
}

.trn-01__btn--b {
  transition: transform var(--dur) cubic-bezier(.34, 1.2, .64, 1);
}

.trn-01__btn--b:hover,
.trn-01__btn--b:focus-visible {
  transform: translateX(10px);
}

.trn-01__btn--c {
  transition: color 200ms ease-out 90ms, border-color 200ms ease-out 90ms;
}

.trn-01__btn--c:hover,
.trn-01__btn--c:focus-visible {
  color: var(--ink);
  border-color: var(--ink);
}

.trn-01__code {
  display: block;
  padding: 7px 9px;
  background: var(--page);
  border: 1px dashed var(--rule);
  border-radius: 3px;
  font: 400 11.5px/1.45 var(--font-display);
  color: var(--muted);
  overflow-wrap: anywhere;
}

.trn-01__spec {
  margin: 12px 0 0;
  display: grid;
  grid-template-columns: minmax(0, auto) minmax(0, 1fr);
  gap: 0;
  font-size: 12.5px;
}

.trn-01__spec dt {
  padding: 8px 12px 8px 0;
  border-block-start: 1px solid var(--rule);
  font: 500 12px/1.4 var(--font-display);
  color: var(--ink);
  min-inline-size: 0;
  overflow-wrap: anywhere;
}

.trn-01__spec dd {
  margin: 0;
  padding: 8px 0;
  border-block-start: 1px solid var(--rule);
  font: 400 12px/1.4 var(--font-display);
  color: var(--muted);
  min-inline-size: 0;
  overflow-wrap: anywhere;
}

.trn-01__hint {
  font-family: system-ui, sans-serif;
  font-size: 11px;
  color: var(--accent);
}

.trn-01__trap {
  display: flex;
  gap: 9px;
  align-items: flex-start;
  margin: 16px 0 0;
  padding: 11px 12px;
  background: var(--page);
  border-inline-start: 2px solid var(--accent);
  font-size: 12.5px;
  line-height: 1.55;
  color: var(--muted);
}

.trn-01__trap svg {
  flex: none;
  margin-block-start: 2px;
  color: var(--accent);
}

.trn-01__trap code {
  font: 400 12px/1 var(--font-display);
  color: var(--ink);
}

.trn-01__lab {
  margin-block-start: 14px;
}

.trn-01__switch {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  clip-path: inset(50%);
  overflow: hidden;
}

.trn-01__runbtn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  min-height: 44px;
  padding: 0 16px;
  background: var(--accent);
  color: #fff;
  border-radius: 3px;
  cursor: pointer;
  font: 500 13px/1 system-ui, sans-serif;
  transition: background-color 160ms ease;
}

.trn-01__switch:focus-visible + .trn-01__runbtn {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.trn-01__switch:checked + .trn-01__runbtn {
  background: var(--ink);
}

.trn-01__switch:checked + .trn-01__runbtn svg {
  display: none;
}

.trn-01__switch:checked + .trn-01__runbtn span::after {
  content: " · running";
  color: #cbd8f2;
}

.trn-01__tracks {
  list-style: none;
  margin: 18px 0 0;
  padding: 0;
  display: grid;
  gap: 14px;
}

.trn-01__trackrow {
  display: grid;
  grid-template-columns: 7rem minmax(0, 1fr);
  gap: 6px 12px;
  align-items: center;
}

.trn-01__tlabel {
  font: 500 12px/1 var(--font-display);
  color: var(--ink);
}

.trn-01__track {
  position: relative;
  block-size: 22px;
  border: 1px solid var(--rule);
  border-radius: 2px;
  background: var(--page);
  overflow: hidden;
}

.trn-01__runner {
  position: absolute;
  inset-block: 0;
  inset-inline-start: 0;
  inline-size: 100%;
}

.trn-01__dot {
  position: absolute;
  inset-block-start: 3px;
  inline-size: 14px;
  block-size: 14px;
  border-radius: 50%;
  background: var(--accent);
}

.trn-01__runner--ease {
  transition: transform var(--dur) ease;
}

.trn-01__runner--io {
  transition: transform var(--dur) cubic-bezier(.42, 0, .58, 1);
}

.trn-01__runner--over {
  transition: transform var(--dur) cubic-bezier(.34, 1.2, .64, 1);
}

.trn-01:has(#trn-01-run:checked) .trn-01__runner {
  transform: translateX(calc(var(--travel) - 18px));
}

.trn-01__tvalue {
  grid-column: 2;
  font: 400 11px/1.4 var(--font-display);
  color: var(--muted);
  overflow-wrap: anywhere;
}

@media (max-width: 560px) {
  .trn-01__trackrow {
    grid-template-columns: minmax(0, 1fr);
  }

  .trn-01__tvalue {
    grid-column: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .trn-01__btn--b {
    transition: opacity 120ms ease;
  }

  .trn-01__btn--b:hover,
    .trn-01__btn--b:focus-visible {
    transform: none;
    opacity: 0.72;
  }

  .trn-01__runner,
    .trn-01__runner--ease,
    .trn-01__runner--io,
    .trn-01__runner--over {
    transition-duration: 120ms;
    transition-timing-function: linear;
  }
}

@media (prefers-color-scheme: dark) {
  .trn-01 {
    --page: #0b1220;
    --page: oklch(0.19 0.03 258);
    --grid: #16203a;
    --grid: oklch(0.25 0.036 258);
    --card: #111a2c;
    --card: oklch(0.22 0.032 258);
    --ink: #e8eefb;
    --ink: oklch(0.95 0.012 250);
    --muted: #96a6c2;
    --muted: oklch(0.72 0.03 252);
    --rule: #22304f;
    --rule: oklch(0.3 0.04 256);
    --accent: #7aa7ff;
    --accent: oklch(0.75 0.13 262);
  }

  .trn-01__btn--a:hover,
    .trn-01__btn--a:focus-visible {
    color: #0b1220;
  }

  .trn-01__runbtn {
    color: #0b1220;
  }

  .trn-01__switch:checked + .trn-01__runbtn {
    color: #e8eefb;
  }
}

[data-theme="dark"] .trn-01 {
  --page: #0b1220;
  --grid: #16203a;
  --card: #111a2c;
  --ink: #e8eefb;
  --muted: #96a6c2;
  --rule: #22304f;
  --accent: #7aa7ff;
}

[data-theme="dark"] .trn-01__btn--a:hover,
[data-theme="dark"] .trn-01__btn--a:focus-visible {
  color: #0b1220;
}

[data-theme="dark"] .trn-01__runbtn {
  color: #0b1220;
}

[data-theme="dark"] .trn-01__switch:checked + .trn-01__runbtn {
  color: #e8eefb;
}

.trn-01__theme {
  position: relative;
  inline-size: 100%;
  min-inline-size: 0;
  display: flex;
  justify-content: flex-end;
  margin: 0 0 14px;
}

.trn-01__themecb {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  clip-path: inset(50%);
  overflow: hidden;
}

.trn-01__themebtn {
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

.trn-01__themebtn:hover {
  color: var(--ink);
}

.trn-01__themecb:focus-visible + .trn-01__themebtn {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.trn-01__themeico {
  display: grid;
  place-items: center;
  inline-size: 15px;
  block-size: 15px;
}

.trn-01__themeico svg {
  grid-area: 1 / 1;
  transition: opacity 200ms ease;
}

.trn-01__sun {
  opacity: 1;
}

.trn-01__moon {
  opacity: 0.34;
}

.trn-01:has(#trn-01-theme:checked) .trn-01__sun {
  opacity: 0.34;
}

.trn-01:has(#trn-01-theme:checked) .trn-01__moon {
  opacity: 1;
}

@media (prefers-color-scheme: light) {
  .trn-01:has(#trn-01-theme:checked) {
    --page: #0b1220;
    --page: oklch(0.19 0.03 258);
    --grid: #16203a;
    --grid: oklch(0.25 0.036 258);
    --card: #111a2c;
    --card: oklch(0.22 0.032 258);
    --ink: #e8eefb;
    --ink: oklch(0.95 0.012 250);
    --muted: #96a6c2;
    --muted: oklch(0.72 0.03 252);
    --rule: #22304f;
    --rule: oklch(0.3 0.04 256);
    --accent: #7aa7ff;
    --accent: oklch(0.75 0.13 262);
  }

  .trn-01:has(#trn-01-theme:checked) .trn-01__btn--a:hover,
    .trn-01:has(#trn-01-theme:checked) .trn-01__btn--a:focus-visible {
    color: #0b1220;
  }

  .trn-01:has(#trn-01-theme:checked) .trn-01__runbtn {
    color: #0b1220;
  }

  .trn-01:has(#trn-01-theme:checked) .trn-01__switch:checked + .trn-01__runbtn {
    color: #e8eefb;
  }
}

@media (prefers-color-scheme: dark) {
  .trn-01:has(#trn-01-theme:checked) {
    --page: #f4f7fb;
    --page: oklch(0.97 0.008 250);
    --grid: #dfe7f2;
    --grid: oklch(0.92 0.017 248);
    --card: #ffffff;
    --ink: #101a2b;
    --ink: oklch(0.21 0.028 258);
    --muted: #5a6a83;
    --muted: oklch(0.51 0.031 252);
    --rule: #cdd8e8;
    --rule: oklch(0.87 0.02 250);
    --accent: #1d5fd6;
    --accent: oklch(0.52 0.185 261);
    --dur: 320ms;
    --travel: 100%;
    --font-display: ui-monospace, "JetBrains Mono", "SFMono-Regular", Menlo, monospace;
    background: linear-gradient(var(--grid) 1px, transparent 1px) 0 0 / 100% 28px, linear-gradient(90deg, var(--grid) 1px, transparent 1px) 0 0 / 28px 100%, var(--page);
  }

  .trn-01:has(#trn-01-theme:checked) .trn-01__btn--a:hover,
    .trn-01:has(#trn-01-theme:checked) .trn-01__btn--a:focus-visible {
    background: var(--accent);
    color: #fff;
  }

  .trn-01:has(#trn-01-theme:checked) .trn-01__runbtn {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    min-height: 44px;
    padding: 0 16px;
    background: var(--accent);
    color: #fff;
    border-radius: 3px;
    cursor: pointer;
    font: 500 13px/1 system-ui, sans-serif;
    transition: background-color 160ms ease;
  }

  .trn-01:has(#trn-01-theme:checked) .trn-01__switch:checked + .trn-01__runbtn {
    background: var(--ink);
  }

  .trn-01:has(#trn-01-theme:checked) .trn-01__sun {
    opacity: 1;
  }

  .trn-01:has(#trn-01-theme:checked) .trn-01__moon {
    opacity: 0.34;
  }
}
```
