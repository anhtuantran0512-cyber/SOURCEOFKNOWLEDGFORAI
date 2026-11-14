---
source: "codefronts"
url: "https://codefronts.com/motion/css-transition-designs/loading-skeleton-transition/"
title: "Transitioning Height Auto with interpolate-size"
section: "motion"
category: "css-transition-designs"
category_name: "CSS Transitions"
description: "The oldest unsolved transition problem: height: auto had no numeric value to interpolate toward, so every accordion guessed with max-height — clipping tall…"
has_js: "false"
---

Here's a working CSS Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Transitioning Height Auto with interpolate-size
Source: https://codefronts.com/motion/css-transition-designs/loading-skeleton-transition/

The oldest unsolved transition problem: height: auto had no numeric value to interpolate toward, so every accordion guessed with max-height — clipping tall content or easing against a value the content never reaches. interpolate-size: allow-keywords makes the keyword interpolable. All three techniques are shown open and closed, side by side and labelled.
## HTML
```html
<section class="trn-10" aria-labelledby="trn-10-heading">
  <div class="trn-10__stage">
    <div class="trn-10__theme">
      <input class="trn-10__themecb" type="checkbox" id="trn-10-theme">
      <label class="trn-10__themebtn" for="trn-10-theme">
        <span class="trn-10__themeico" aria-hidden="true">
          <svg class="trn-10__sun" viewBox="0 0 20 20" width="15" height="15"><circle cx="10" cy="10" r="3.9" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M10 1.7v2.1M10 16.2v2.1M1.7 10h2.1M16.2 10h2.1M4.2 4.2l1.5 1.5M14.3 14.3l1.5 1.5M15.8 4.2l-1.5 1.5M5.7 14.3l-1.5 1.5" stroke="currentColor" stroke-width="1.4"/></svg>
          <svg class="trn-10__moon" viewBox="0 0 20 20" width="15" height="15"><path d="M15.4 12.7A6.7 6.7 0 0 1 7.3 4.6a6.8 6.8 0 1 0 8.1 8.1Z" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>
        </span>
        <span>Theme</span>
      </label>
    </div>
    <header class="trn-10__head">
      <p class="trn-10__kicker">height: auto</p>
      <h2 class="trn-10__heading" id="trn-10-heading">Three ways to open a panel, one that finally reads right</h2>
      <p class="trn-10__sub">One switch drives all three. The content is identical, so any difference is the technique.</p>
    </header>

    <input class="trn-10__input" type="checkbox" id="trn-10-open">
    <label class="trn-10__switch" for="trn-10-open"><span class="trn-10__switchtext">Toggle all three panels</span></label>

    <div class="trn-10__grid">
      <article class="trn-10__col">
        <h3 class="trn-10__label trn-10__label--good">interpolate-size: allow-keywords</h3>
        <div class="trn-10__panel">
          <div class="trn-10__body trn-10__body--auto">
            <div class="trn-10__inner">
              <p class="trn-10__prose">Retention policy applies to every dataset in the Orbit workspace. Rows older than 400 days are moved to cold storage on the first of the month.</p>
              <p class="trn-10__prose">Owners are notified seven days before the move.</p>
            </div>
          </div>
        </div>
        <code class="trn-10__code">height: 0 &rarr; auto</code>
        <p class="trn-10__verdict">Eases across the real content height. Nothing is guessed.</p>
      </article>

      <article class="trn-10__col">
        <h3 class="trn-10__label trn-10__label--ok">grid-template-rows: minmax(0, 0fr) &rarr; minmax(0, 1fr)</h3>
        <div class="trn-10__panel">
          <div class="trn-10__body trn-10__body--grid">
            <div class="trn-10__inner">
              <p class="trn-10__prose">Retention policy applies to every dataset in the Orbit workspace. Rows older than 400 days are moved to cold storage on the first of the month.</p>
              <p class="trn-10__prose">Owners are notified seven days before the move.</p>
            </div>
          </div>
        </div>
        <code class="trn-10__code">grid-template-rows: minmax(0, 0fr) &rarr; minmax(0, 1fr)</code>
        <p class="trn-10__verdict">Correct everywhere today. Needs the minmax(0, ...) floor &mdash; a bare 0fr leaves a line showing.</p>
      </article>

      <article class="trn-10__col">
        <h3 class="trn-10__label trn-10__label--bad">max-height: 500px guess</h3>
        <div class="trn-10__panel">
          <div class="trn-10__body trn-10__body--max">
            <div class="trn-10__inner">
              <p class="trn-10__prose">Retention policy applies to every dataset in the Orbit workspace. Rows older than 400 days are moved to cold storage on the first of the month.</p>
              <p class="trn-10__prose">Owners are notified seven days before the move.</p>
            </div>
          </div>
        </div>
        <code class="trn-10__code">max-height: 0 &rarr; 500px</code>
        <p class="trn-10__verdict">Opens fast, then stalls — the curve is spread over 500px of which 180px is real.</p>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
.trn-10 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  interpolate-size: allow-keywords;
  --page: #efe7de;
  --page: oklch(0.93 0.018 70);
  --surface: #e6dcd0;
  --surface: oklch(0.9 0.021 72);
  --card: #f7f2eb;
  --ink: #33261c;
  --ink: oklch(0.31 0.033 55);
  --muted: #6f5c4d;
  --muted: oklch(0.5 0.032 58);
  --accent: #b1552a;
  --accent: oklch(0.56 0.14 45);
  --ok: #7a6a3d;
  --ok: oklch(0.53 0.07 96);
  --bad: #9e3a3a;
  --bad: oklch(0.47 0.13 25);
  --dur: 380ms;
  --font-display: "Hoefler Text", "Iowan Old Style", Georgia, serif;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

.trn-10 *,
.trn-10 *::before,
.trn-10 *::after {
  box-sizing: border-box;
}

.trn-10__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  padding: clamp(30px, 6vw, 68px) 18px;
}

.trn-10__head {
  inline-size: 100%;
  max-inline-size: 60rem;
  min-inline-size: 0;
  margin: 0 0 24px;
}

.trn-10__kicker {
  margin: 0 0 12px;
  font: 400 12px/1 ui-monospace, Menlo, monospace;
  letter-spacing: 0.1em;
  color: var(--accent);
}

.trn-10__heading {
  margin: 0 0 12px;
  font: 500 clamp(26px, 4.8vw, 38px)/1.1 var(--font-display);
  letter-spacing: -0.02em;
  text-wrap: balance;
}

.trn-10__sub {
  margin: 0;
  max-inline-size: 52ch;
  font-size: 15px;
  line-height: 1.65;
  color: var(--muted);
  text-wrap: pretty;
}

.trn-10__input {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  clip-path: inset(50%);
  overflow: hidden;
}

.trn-10__switch {
  inline-size: 100%;
  max-inline-size: 60rem;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 48px;
  padding: 0 22px;
  margin-block-end: 26px;
  cursor: pointer;
  background: var(--surface);
  border-radius: 3px;
  font: 500 13px/1 var(--font-display);
  letter-spacing: 0.04em;
  color: var(--ink);
  transition: background-color 220ms ease, color 220ms ease;
}

.trn-10__switch:hover {
  background: var(--accent);
  color: var(--card);
}

.trn-10__input:focus-visible + .trn-10__switch {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.trn-10__input:checked + .trn-10__switch {
  background: var(--ink);
  color: var(--card);
}

.trn-10__input:checked + .trn-10__switch .trn-10__switchtext::after {
  content: " · open";
  opacity: 0.6;
}

.trn-10__grid {
  inline-size: 100%;
  max-inline-size: 60rem;
  min-inline-size: 0;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 16rem), 1fr));
  gap: 22px;
}

.trn-10__col {
  min-inline-size: 0;
}

.trn-10__label {
  margin: 0 0 12px;
  font: 400 12.5px/1.45 ui-monospace, Menlo, monospace;
}

.trn-10__label--good {
  color: var(--accent);
}

.trn-10__label--ok {
  color: var(--ok);
}

.trn-10__label--bad {
  color: var(--bad);
}

.trn-10__panel {
  background: var(--card);
  border-radius: 3px;
}

.trn-10__body {
  overflow: clip;
}

.trn-10__inner {
  padding: 14px 16px;
}

.trn-10__prose {
  margin: 0 0 10px;
  font-size: 13.5px;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.trn-10__prose:last-child {
  margin-block-end: 0;
}

.trn-10__body--auto {
  display: grid;
  grid-template-rows: minmax(0, 0fr);
  transition: grid-template-rows var(--dur) cubic-bezier(.3, .8, .3, 1);
}

.trn-10__body--auto > .trn-10__inner {
  min-block-size: 0;
}

.trn-10:has(#trn-10-open:checked) .trn-10__body--auto {
  grid-template-rows: minmax(0, 1fr);
}

@supports (interpolate-size: allow-keywords) {
  .trn-10__body--auto {
    display: block;
    grid-template-rows: none;
    block-size: 0;
    transition: block-size var(--dur) cubic-bezier(.3, .8, .3, 1);
  }

  .trn-10:has(#trn-10-open:checked) .trn-10__body--auto {
    block-size: auto;
  }
}

.trn-10__body--grid {
  display: grid;
  grid-template-rows: minmax(0, 0fr);
  transition: grid-template-rows var(--dur) cubic-bezier(.3, .8, .3, 1);
}

.trn-10__body--grid > .trn-10__inner {
  min-block-size: 0;
}

.trn-10:has(#trn-10-open:checked) .trn-10__body--grid {
  grid-template-rows: minmax(0, 1fr);
}

.trn-10__body--max {
  max-block-size: 0;
  transition: max-block-size var(--dur) cubic-bezier(.3, .8, .3, 1);
}

.trn-10:has(#trn-10-open:checked) .trn-10__body--max {
  max-block-size: 500px;
}

.trn-10__code {
  display: block;
  margin-block-start: 10px;
  padding: 8px 10px;
  background: var(--surface);
  font: 400 11.5px/1.5 ui-monospace, Menlo, monospace;
  color: var(--ink);
  overflow-wrap: anywhere;
}

.trn-10__verdict {
  margin: 9px 0 0;
  font-size: 12.5px;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .trn-10__body--auto,
    .trn-10__body--grid,
    .trn-10__body--max {
    transition-duration: 140ms;
  }

  .trn-10__switch {
    transition-duration: 140ms;
  }
}

@media (prefers-color-scheme: dark) {
  .trn-10 {
    --page: #1c1713;
    --page: oklch(0.22 0.018 58);
    --surface: #262019;
    --surface: oklch(0.27 0.02 62);
    --card: #201a15;
    --ink: #f0e7dd;
    --ink: oklch(0.94 0.016 72);
    --muted: #a89584;
    --muted: oklch(0.71 0.026 66);
    --accent: #e2895a;
    --accent: oklch(0.75 0.13 48);
    --ok: #cbbd7f;
    --bad: #e57373;
  }

  .trn-10__switch:hover {
    color: #1c1713;
  }

  .trn-10__input:checked + .trn-10__switch {
    background: var(--accent);
    color: #1c1713;
  }
}

[data-theme="dark"] .trn-10 {
  --page: #1c1713;
  --surface: #262019;
  --card: #201a15;
  --ink: #f0e7dd;
  --muted: #a89584;
  --accent: #e2895a;
  --ok: #cbbd7f;
  --bad: #e57373;
}

[data-theme="dark"] .trn-10__switch:hover {
  color: #1c1713;
}

[data-theme="dark"] .trn-10__input:checked + .trn-10__switch {
  background: var(--accent);
  color: #1c1713;
}

.trn-10__theme {
  position: relative;
  inline-size: 100%;
  min-inline-size: 0;
  display: flex;
  justify-content: flex-end;
  margin: 0 0 14px;
}

.trn-10__themecb {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  clip-path: inset(50%);
  overflow: hidden;
}

.trn-10__themebtn {
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

.trn-10__themebtn:hover {
  color: var(--ink);
}

.trn-10__themecb:focus-visible + .trn-10__themebtn {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.trn-10__themeico {
  display: grid;
  place-items: center;
  inline-size: 15px;
  block-size: 15px;
}

.trn-10__themeico svg {
  grid-area: 1 / 1;
  transition: opacity 200ms ease;
}

.trn-10__sun {
  opacity: 1;
}

.trn-10__moon {
  opacity: 0.34;
}

.trn-10:has(#trn-10-theme:checked) .trn-10__sun {
  opacity: 0.34;
}

.trn-10:has(#trn-10-theme:checked) .trn-10__moon {
  opacity: 1;
}

@media (prefers-color-scheme: light) {
  .trn-10:has(#trn-10-theme:checked) {
    --page: #1c1713;
    --page: oklch(0.22 0.018 58);
    --surface: #262019;
    --surface: oklch(0.27 0.02 62);
    --card: #201a15;
    --ink: #f0e7dd;
    --ink: oklch(0.94 0.016 72);
    --muted: #a89584;
    --muted: oklch(0.71 0.026 66);
    --accent: #e2895a;
    --accent: oklch(0.75 0.13 48);
    --ok: #cbbd7f;
    --bad: #e57373;
  }

  .trn-10:has(#trn-10-theme:checked) .trn-10__switch:hover {
    color: #1c1713;
  }

  .trn-10:has(#trn-10-theme:checked) .trn-10__input:checked + .trn-10__switch {
    background: var(--accent);
    color: #1c1713;
  }
}

@media (prefers-color-scheme: dark) {
  .trn-10:has(#trn-10-theme:checked) {
    --page: #efe7de;
    --page: oklch(0.93 0.018 70);
    --surface: #e6dcd0;
    --surface: oklch(0.9 0.021 72);
    --card: #f7f2eb;
    --ink: #33261c;
    --ink: oklch(0.31 0.033 55);
    --muted: #6f5c4d;
    --muted: oklch(0.5 0.032 58);
    --accent: #b1552a;
    --accent: oklch(0.56 0.14 45);
    --ok: #7a6a3d;
    --ok: oklch(0.53 0.07 96);
    --bad: #9e3a3a;
    --bad: oklch(0.47 0.13 25);
    --dur: 380ms;
    --font-display: "Hoefler Text", "Iowan Old Style", Georgia, serif;
    background: var(--page);
  }

  .trn-10:has(#trn-10-theme:checked) .trn-10__switch:hover {
    background: var(--accent);
    color: var(--card);
  }

  .trn-10:has(#trn-10-theme:checked) .trn-10__input:checked + .trn-10__switch {
    background: var(--ink);
    color: var(--card);
  }

  .trn-10:has(#trn-10-theme:checked) .trn-10__sun {
    opacity: 1;
  }

  .trn-10:has(#trn-10-theme:checked) .trn-10__moon {
    opacity: 0.34;
  }
}
```
