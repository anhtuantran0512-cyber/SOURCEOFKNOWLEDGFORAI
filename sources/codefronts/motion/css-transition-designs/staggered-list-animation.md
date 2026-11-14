---
source: "codefronts"
url: "https://codefronts.com/motion/css-transition-designs/staggered-list-animation/"
title: "Staggered Transition Delay with Custom Property Index"
section: "motion"
category: "css-transition-designs"
category_name: "CSS Transitions"
description: "Per-item transition-delay computed from an index custom property set inline — style=\"--i: 3\" plus calc(var(--i) * 60ms) — so a list of any length staggers…"
has_js: "false"
---

Here's a working CSS Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Staggered Transition Delay with Custom Property Index
Source: https://codefronts.com/motion/css-transition-designs/staggered-list-animation/

Per-item transition-delay computed from an index custom property set inline — style="--i: 3" plus calc(var(--i) * 60ms) — so a list of any length staggers from a single rule. Compared directly against the :nth-child() approach, which needs one selector per item and silently stops staggering the moment the list grows past the last rule you wrote.
## HTML
```html
<section class="trn-18" aria-labelledby="trn-18-heading">
  <div class="trn-18__stage">
    <div class="trn-18__theme">
      <input class="trn-18__themecb" type="checkbox" id="trn-18-theme">
      <label class="trn-18__themebtn" for="trn-18-theme">
        <span class="trn-18__themeico" aria-hidden="true">
          <svg class="trn-18__sun" viewBox="0 0 20 20" width="15" height="15"><circle cx="10" cy="10" r="3.9" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M10 1.7v2.1M10 16.2v2.1M1.7 10h2.1M16.2 10h2.1M4.2 4.2l1.5 1.5M14.3 14.3l1.5 1.5M15.8 4.2l-1.5 1.5M5.7 14.3l-1.5 1.5" stroke="currentColor" stroke-width="1.4"/></svg>
          <svg class="trn-18__moon" viewBox="0 0 20 20" width="15" height="15"><path d="M15.4 12.7A6.7 6.7 0 0 1 7.3 4.6a6.8 6.8 0 1 0 8.1 8.1Z" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>
        </span>
        <span>Theme</span>
      </label>
    </div>
    <header class="trn-18__head">
      <h2 class="trn-18__heading" id="trn-18-heading">One rule, any number of items</h2>
      <p class="trn-18__sub">Hover or focus either column. Both stagger — only one of them keeps working when the list grows.</p>
    </header>

    <div class="trn-18__pair">
      <article class="trn-18__col">
        <h3 class="trn-18__label trn-18__label--good">calc(var(--i) * 60ms) — one rule, six items</h3>
        <div class="trn-18__list trn-18__list--var" tabindex="0">
          <p class="trn-18__row" style="--i: 0"><span>Deploy to production</span><code>--i: 0 · 0ms</code></p>
          <p class="trn-18__row" style="--i: 1"><span>Sync 4 repositories</span><code>--i: 1 · 60ms</code></p>
          <p class="trn-18__row" style="--i: 2"><span>Invite teammate</span><code>--i: 2 · 120ms</code></p>
          <p class="trn-18__row" style="--i: 3"><span>Rotate access keys</span><code>--i: 3 · 180ms</code></p>
          <p class="trn-18__row" style="--i: 4"><span>Review audit log</span><code>--i: 4 · 240ms</code></p>
          <p class="trn-18__row" style="--i: 5"><span>Archive workspace</span><code>--i: 5 · 300ms</code></p>
        </div>
      </article>

      <article class="trn-18__col">
        <h3 class="trn-18__label trn-18__label--bad">:nth-child() — five rules, six items</h3>
        <div class="trn-18__list trn-18__list--nth" tabindex="0">
          <p class="trn-18__row"><span>Deploy to production</span><code>rule 1 · 0ms</code></p>
          <p class="trn-18__row"><span>Sync 4 repositories</span><code>rule 2 · 60ms</code></p>
          <p class="trn-18__row"><span>Invite teammate</span><code>rule 3 · 120ms</code></p>
          <p class="trn-18__row"><span>Rotate access keys</span><code>rule 4 · 180ms</code></p>
          <p class="trn-18__row"><span>Review audit log</span><code>rule 5 · 240ms</code></p>
          <p class="trn-18__row"><span>Archive workspace</span><code>no rule · 0ms</code></p>
        </div>
      </article>
    </div>

    <p class="trn-18__foot">The sixth row on the right has no matching selector, so it arrives first and the cascade reads as broken. Nothing in the stylesheet says the list got longer.</p>
  </div>
</section>
```
## CSS
```css
.trn-18 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --page: #f7f3ec;
  --page: oklch(0.96 0.012 82);
  --ink: #241f19;
  --ink: oklch(0.26 0.016 68);
  --muted: #6d6355;
  --muted: oklch(0.51 0.02 74);
  --rule: #d5ccbd;
  --rule: oklch(0.86 0.018 80);
  --coral: #d1532f;
  --coral: oklch(0.6 0.16 38);
  --bad: #8f6c1f;
  --bad: oklch(0.53 0.11 88);
  --step: 60ms;
  --font-display: "Bookman Old Style", "Rockwell", "Roboto Slab", Georgia, serif;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

.trn-18 *,
.trn-18 *::before,
.trn-18 *::after {
  box-sizing: border-box;
}

.trn-18__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  padding: clamp(22px, 5vw, 52px) 14px;
}

.trn-18__head {
  inline-size: 100%;
  max-inline-size: 58rem;
  min-inline-size: 0;
  margin: 0 0 20px;
}

.trn-18__heading {
  margin: 0 0 8px;
  font: 600 clamp(23px, 4.4vw, 34px)/1.1 var(--font-display);
  letter-spacing: -0.015em;
  text-wrap: balance;
}

.trn-18__sub {
  margin: 0;
  max-inline-size: 54ch;
  font-size: 14px;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.trn-18__pair {
  inline-size: 100%;
  max-inline-size: 58rem;
  min-inline-size: 0;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 17rem), 1fr));
  gap: 18px;
}

.trn-18__col {
  min-inline-size: 0;
}

.trn-18__label {
  margin: 0 0 8px;
  font: 500 11.5px/1.4 ui-monospace, Menlo, monospace;
}

.trn-18__label--good {
  color: var(--coral);
}

.trn-18__label--bad {
  color: var(--bad);
}

.trn-18__list {
  border-block-start: 1px solid var(--ink);
}

.trn-18__list:focus-visible {
  outline: 2px solid var(--coral);
  outline-offset: 3px;
}

.trn-18__row {
  display: flex;
  flex-wrap: wrap;
  gap: 2px 10px;
  align-items: baseline;
  justify-content: space-between;
  min-inline-size: 0;
  margin: 0;
  padding: 8px 2px;
  border-block-end: 1px solid var(--rule);
  opacity: 0.28;
  transform: translateY(-4px);
  transition: opacity 240ms ease, transform 240ms cubic-bezier(.2, .8, .3, 1);
}

.trn-18__row span {
  min-inline-size: 0;
  font: 500 13px/1.3 var(--font-display);
}

.trn-18__row code {
  font: 400 10.5px/1 ui-monospace, Menlo, monospace;
  color: var(--muted);
}

.trn-18__list--var .trn-18__row {
  transition-delay: calc(min(var(--i, 0), 5) * var(--step));
}

.trn-18__list--var:hover .trn-18__row,
.trn-18__list--var:focus-visible .trn-18__row {
  opacity: 1;
  transform: translateY(0);
}

.trn-18__list--nth .trn-18__row:nth-child(1) {
  transition-delay: 0ms;
}

.trn-18__list--nth .trn-18__row:nth-child(2) {
  transition-delay: 60ms;
}

.trn-18__list--nth .trn-18__row:nth-child(3) {
  transition-delay: 120ms;
}

.trn-18__list--nth .trn-18__row:nth-child(4) {
  transition-delay: 180ms;
}

.trn-18__list--nth .trn-18__row:nth-child(5) {
  transition-delay: 240ms;
}

.trn-18__list--nth:hover .trn-18__row,
.trn-18__list--nth:focus-visible .trn-18__row {
  opacity: 1;
  transform: translateY(0);
}

.trn-18__foot {
  inline-size: 100%;
  max-inline-size: 58rem;
  margin: 18px 0 0;
  padding-block-start: 14px;
  border-block-start: 1px solid var(--rule);
  font-size: 12.5px;
  line-height: 1.6;
  color: var(--muted);
}

@media (prefers-reduced-motion: reduce) {
  .trn-18__row {
    transform: none;
    transition: opacity 140ms ease;
  }

  .trn-18__list--var .trn-18__row {
    transition-delay: calc(min(var(--i, 0), 5) * 15ms);
  }

  .trn-18__list--nth .trn-18__row:nth-child(1),
    .trn-18__list--nth .trn-18__row:nth-child(2),
    .trn-18__list--nth .trn-18__row:nth-child(3),
    .trn-18__list--nth .trn-18__row:nth-child(4),
    .trn-18__list--nth .trn-18__row:nth-child(5) {
    transition-delay: 15ms;
  }

  .trn-18__list--var:hover .trn-18__row,
    .trn-18__list--var:focus-visible .trn-18__row,
    .trn-18__list--nth:hover .trn-18__row,
    .trn-18__list--nth:focus-visible .trn-18__row {
    transform: none;
  }
}

@media (prefers-color-scheme: dark) {
  .trn-18 {
    --page: #1a1712;
    --page: oklch(0.21 0.014 70);
    --ink: #f2ece1;
    --ink: oklch(0.95 0.014 82);
    --muted: #a79c8c;
    --muted: oklch(0.71 0.02 80);
    --rule: #322c24;
    --rule: oklch(0.3 0.016 74);
    --coral: #f08256;
    --coral: oklch(0.75 0.14 42);
    --bad: #d3b25c;
    --bad: oklch(0.79 0.11 90);
  }
}

[data-theme="dark"] .trn-18 {
  --page: #1a1712;
  --ink: #f2ece1;
  --muted: #a79c8c;
  --rule: #322c24;
  --coral: #f08256;
  --bad: #d3b25c;
}

.trn-18__theme {
  position: relative;
  inline-size: 100%;
  min-inline-size: 0;
  display: flex;
  justify-content: flex-end;
  margin: 0 0 14px;
}

.trn-18__themecb {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  clip-path: inset(50%);
  overflow: hidden;
}

.trn-18__themebtn {
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

.trn-18__themebtn:hover {
  color: var(--ink);
}

.trn-18__themecb:focus-visible + .trn-18__themebtn {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.trn-18__themeico {
  display: grid;
  place-items: center;
  inline-size: 15px;
  block-size: 15px;
}

.trn-18__themeico svg {
  grid-area: 1 / 1;
  transition: opacity 200ms ease;
}

.trn-18__sun {
  opacity: 1;
}

.trn-18__moon {
  opacity: 0.34;
}

.trn-18:has(#trn-18-theme:checked) .trn-18__sun {
  opacity: 0.34;
}

.trn-18:has(#trn-18-theme:checked) .trn-18__moon {
  opacity: 1;
}

@media (prefers-color-scheme: light) {
  .trn-18:has(#trn-18-theme:checked) {
    --page: #1a1712;
    --page: oklch(0.21 0.014 70);
    --ink: #f2ece1;
    --ink: oklch(0.95 0.014 82);
    --muted: #a79c8c;
    --muted: oklch(0.71 0.02 80);
    --rule: #322c24;
    --rule: oklch(0.3 0.016 74);
    --coral: #f08256;
    --coral: oklch(0.75 0.14 42);
    --bad: #d3b25c;
    --bad: oklch(0.79 0.11 90);
  }
}

@media (prefers-color-scheme: dark) {
  .trn-18:has(#trn-18-theme:checked) {
    --page: #f7f3ec;
    --page: oklch(0.96 0.012 82);
    --ink: #241f19;
    --ink: oklch(0.26 0.016 68);
    --muted: #6d6355;
    --muted: oklch(0.51 0.02 74);
    --rule: #d5ccbd;
    --rule: oklch(0.86 0.018 80);
    --coral: #d1532f;
    --coral: oklch(0.6 0.16 38);
    --bad: #8f6c1f;
    --bad: oklch(0.53 0.11 88);
    --step: 60ms;
    --font-display: "Bookman Old Style", "Rockwell", "Roboto Slab", Georgia, serif;
    background: var(--page);
  }

  .trn-18:has(#trn-18-theme:checked) .trn-18__sun {
    opacity: 1;
  }

  .trn-18:has(#trn-18-theme:checked) .trn-18__moon {
    opacity: 0.34;
  }
}
```
