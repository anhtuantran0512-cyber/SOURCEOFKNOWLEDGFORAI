---
source: "codefronts"
url: "https://codefronts.com/motion/css-transition-designs/underline-animation-hover/"
title: "Underline Transitions with Transform Origin"
section: "motion"
category: "css-transition-designs"
category_name: "CSS Transitions"
description: "The scaleX() underline, taught as a transform-origin lesson rather than a link effect."
has_js: "false"
---

Here's a working CSS Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Underline Transitions with Transform Origin
Source: https://codefronts.com/motion/css-transition-designs/underline-animation-hover/

The scaleX() underline, taught as a transform-origin lesson rather than a link effect. Four rows show what the property actually controls: growing from the left, retreating to the right, opening from the centre, and the one people ask about — switching the origin between the hover and resting state so the rule enters from the left and exits to the right.
## HTML
```html
<section class="trn-14" aria-labelledby="trn-14-heading">
  <div class="trn-14__stage">
    <div class="trn-14__theme">
      <input class="trn-14__themecb" type="checkbox" id="trn-14-theme">
      <label class="trn-14__themebtn" for="trn-14-theme">
        <span class="trn-14__themeico" aria-hidden="true">
          <svg class="trn-14__sun" viewBox="0 0 20 20" width="15" height="15"><circle cx="10" cy="10" r="3.9" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M10 1.7v2.1M10 16.2v2.1M1.7 10h2.1M16.2 10h2.1M4.2 4.2l1.5 1.5M14.3 14.3l1.5 1.5M15.8 4.2l-1.5 1.5M5.7 14.3l-1.5 1.5" stroke="currentColor" stroke-width="1.4"/></svg>
          <svg class="trn-14__moon" viewBox="0 0 20 20" width="15" height="15"><path d="M15.4 12.7A6.7 6.7 0 0 1 7.3 4.6a6.8 6.8 0 1 0 8.1 8.1Z" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>
        </span>
        <span>Theme</span>
      </label>
    </div>
    <header class="trn-14__head">
      <p class="trn-14__kicker">transform-origin</p>
      <h2 class="trn-14__heading" id="trn-14-heading">Same scale, four anchors</h2>
      <p class="trn-14__sub">Hover or Tab through each row. Every underline runs <code>scaleX(0)</code> to <code>scaleX(1)</code> — only the origin changes.</p>
    </header>

    <ul class="trn-14__rows">
      <li class="trn-14__row">
        <a class="trn-14__link trn-14__link--left" href="#trn-14-heading">Deploy to production</a>
        <code class="trn-14__spec">transform-origin: left</code>
        <span class="trn-14__desc">Grows rightward from the start of the text.</span>
      </li>
      <li class="trn-14__row">
        <a class="trn-14__link trn-14__link--right" href="#trn-14-heading">Sync 4 repositories</a>
        <code class="trn-14__spec">transform-origin: right</code>
        <span class="trn-14__desc">Grows leftward, and retreats back to the right.</span>
      </li>
      <li class="trn-14__row">
        <a class="trn-14__link trn-14__link--center" href="#trn-14-heading">Invite teammate</a>
        <code class="trn-14__spec">transform-origin: center</code>
        <span class="trn-14__desc">Opens from the middle in both directions at once.</span>
      </li>
      <li class="trn-14__row">
        <a class="trn-14__link trn-14__link--swap" href="#trn-14-heading">Rotate access keys</a>
        <code class="trn-14__spec">right &rarr; left on hover</code>
        <span class="trn-14__desc">In from the left, out to the right — one gesture, two origins.</span>
      </li>
    </ul>

    <p class="trn-14__foot">Decorative link treatments live in css-link-effects. This demo stays on the property: what <code>transform-origin</code> anchors, and when it is read.</p>
  </div>
</section>
```
## CSS
```css
.trn-14 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --page: #0f0f0f;
  --ink: #f7f7f5;
  --ink: oklch(0.97 0.003 100);
  --muted: #8a8a86;
  --muted: oklch(0.62 0.005 100);
  --accent: #ffd400;
  --accent: oklch(0.88 0.19 98);
  --thick: 2px;
  --font-display: "Helvetica Neue", "Arial Narrow", system-ui, sans-serif;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

.trn-14 *,
.trn-14 *::before,
.trn-14 *::after {
  box-sizing: border-box;
}

.trn-14__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  padding: clamp(34px, 7vw, 84px) 18px;
}

.trn-14__head {
  inline-size: 100%;
  max-inline-size: 52rem;
  min-inline-size: 0;
  margin: 0 0 44px;
}

.trn-14__kicker {
  margin: 0 0 16px;
  font: 600 11px/1 var(--font-display);
  letter-spacing: 0.3em;
  text-transform: uppercase;
  color: var(--accent);
}

.trn-14__heading {
  margin: 0 0 14px;
  font: 700 clamp(30px, 6.4vw, 54px)/1 var(--font-display);
  letter-spacing: -0.035em;
  text-transform: uppercase;
  text-wrap: balance;
}

.trn-14__sub {
  margin: 0;
  max-inline-size: 48ch;
  font-size: 15px;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.trn-14__sub code {
  font: 400 13px/1 ui-monospace, Menlo, monospace;
  color: var(--ink);
}

.trn-14__rows {
  list-style: none;
  inline-size: 100%;
  max-inline-size: 52rem;
  min-inline-size: 0;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 34px;
}

.trn-14__row {
  min-inline-size: 0;
  display: grid;
  gap: 8px;
}

.trn-14__link {
  position: relative;
  justify-self: start;
  display: inline-block;
  max-inline-size: 100%;
  padding-block-end: 6px;
  color: var(--ink);
  text-decoration: none;
  font: 600 clamp(20px, 3.6vw, 28px)/1.15 var(--font-display);
  letter-spacing: -0.025em;
  transition: color 240ms ease;
}

.trn-14__link:hover {
  color: var(--accent);
}

.trn-14__link:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 4px;
}

.trn-14__link::after {
  content: "";
  position: absolute;
  inset-inline: 0;
  inset-block-end: 0;
  block-size: var(--thick);
  background: var(--accent);
  transform: scaleX(0);
  transition: transform 360ms cubic-bezier(.25, .8, .25, 1);
}

.trn-14__link:hover::after,
.trn-14__link:focus-visible::after {
  transform: scaleX(1);
}

.trn-14__link--left::after {
  transform-origin: left;
}

.trn-14__link--right::after {
  transform-origin: right;
}

.trn-14__link--center::after {
  transform-origin: center;
}

.trn-14__link--swap::after {
  transform-origin: right;
}

.trn-14__link--swap:hover::after,
.trn-14__link--swap:focus-visible::after {
  transform-origin: left;
}

.trn-14__spec {
  font: 400 12px/1 ui-monospace, Menlo, monospace;
  color: var(--accent);
}

.trn-14__desc {
  font-size: 13.5px;
  line-height: 1.5;
  color: var(--muted);
  text-wrap: pretty;
}

.trn-14__foot {
  inline-size: 100%;
  max-inline-size: 52rem;
  margin: 44px 0 0;
  padding-block-start: 20px;
  border-block-start: 1px solid #262626;
  font-size: 12.5px;
  line-height: 1.6;
  color: var(--muted);
}

.trn-14__foot code {
  font: 400 11.5px/1 ui-monospace, Menlo, monospace;
  color: var(--ink);
}

@media (prefers-reduced-motion: reduce) {
  .trn-14__link::after {
    transform: scaleX(1);
    opacity: 0;
    transition: opacity 150ms ease;
  }

  .trn-14__link:hover::after,
    .trn-14__link:focus-visible::after {
    transform: scaleX(1);
    opacity: 1;
  }
}

@media (prefers-color-scheme: light) {
  .trn-14 {
    --page: #fbfbf9;
    --ink: #101010;
    --muted: #6a6a66;
    --accent: #a37b00;
  }

  .trn-14__foot {
    border-block-start-color: #e2e2de;
  }
}

[data-theme="dark"] .trn-14 {
  --page: #0f0f0f;
  --ink: #f7f7f5;
  --muted: #8a8a86;
  --accent: #ffd400;
}

[data-theme="dark"] .trn-14__foot {
  border-block-start-color: #262626;
}

.trn-14__theme {
  position: relative;
  inline-size: 100%;
  min-inline-size: 0;
  display: flex;
  justify-content: flex-end;
  margin: 0 0 14px;
}

.trn-14__themecb {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  clip-path: inset(50%);
  overflow: hidden;
}

.trn-14__themebtn {
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

.trn-14__themebtn:hover {
  color: var(--ink);
}

.trn-14__themecb:focus-visible + .trn-14__themebtn {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.trn-14__themeico {
  display: grid;
  place-items: center;
  inline-size: 15px;
  block-size: 15px;
}

.trn-14__themeico svg {
  grid-area: 1 / 1;
  transition: opacity 200ms ease;
}

.trn-14__sun {
  opacity: 0.34;
}

.trn-14__moon {
  opacity: 1;
}

.trn-14:has(#trn-14-theme:checked) .trn-14__sun {
  opacity: 1;
}

.trn-14:has(#trn-14-theme:checked) .trn-14__moon {
  opacity: 0.34;
}

@media (prefers-color-scheme: dark) {
  .trn-14:has(#trn-14-theme:checked) {
    --page: #fbfbf9;
    --ink: #101010;
    --muted: #6a6a66;
    --accent: #a37b00;
  }

  .trn-14:has(#trn-14-theme:checked) .trn-14__foot {
    border-block-start-color: #e2e2de;
  }
}

@media (prefers-color-scheme: light) {
  .trn-14:has(#trn-14-theme:checked) {
    --page: #0f0f0f;
    --ink: #f7f7f5;
    --ink: oklch(0.97 0.003 100);
    --muted: #8a8a86;
    --muted: oklch(0.62 0.005 100);
    --accent: #ffd400;
    --accent: oklch(0.88 0.19 98);
    --thick: 2px;
    --font-display: "Helvetica Neue", "Arial Narrow", system-ui, sans-serif;
    background: var(--page);
  }

  .trn-14:has(#trn-14-theme:checked) .trn-14__foot {
    inline-size: 100%;
    max-inline-size: 52rem;
    margin: 44px 0 0;
    padding-block-start: 20px;
    border-block-start: 1px solid #262626;
    font-size: 12.5px;
    line-height: 1.6;
    color: var(--muted);
  }

  .trn-14:has(#trn-14-theme:checked) .trn-14__sun {
    opacity: 0.34;
  }

  .trn-14:has(#trn-14-theme:checked) .trn-14__moon {
    opacity: 1;
  }
}
```
