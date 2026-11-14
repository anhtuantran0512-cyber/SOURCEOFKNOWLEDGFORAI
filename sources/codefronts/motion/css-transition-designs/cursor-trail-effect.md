---
source: "codefronts"
url: "https://codefronts.com/motion/css-transition-designs/cursor-trail-effect/"
title: "Transition All Versus Explicit Property Lists"
section: "motion"
category: "css-transition-designs"
category_name: "CSS Transitions"
description: "transition: all looks like convenience and causes three concrete problems: it animates properties you never intended — including ones a parent changed — it…"
has_js: "false"
---

Here's a working CSS Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Transition All Versus Explicit Property Lists
Source: https://codefronts.com/motion/css-transition-designs/cursor-trail-effect/

transition: all looks like convenience and causes three concrete problems: it animates properties you never intended — including ones a parent changed — it makes per-property durations impossible, and it asks the engine to watch every animatable property on the element. Both cards are labelled and identical except for that one declaration; only one of them glitches.
## HTML
```html
<section class="trn-19" aria-labelledby="trn-19-heading">
  <div class="trn-19__stage">
    <div class="trn-19__theme">
      <input class="trn-19__themecb" type="checkbox" id="trn-19-theme">
      <label class="trn-19__themebtn" for="trn-19-theme">
        <span class="trn-19__themeico" aria-hidden="true">
          <svg class="trn-19__sun" viewBox="0 0 20 20" width="15" height="15"><circle cx="10" cy="10" r="3.9" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M10 1.7v2.1M10 16.2v2.1M1.7 10h2.1M16.2 10h2.1M4.2 4.2l1.5 1.5M14.3 14.3l1.5 1.5M15.8 4.2l-1.5 1.5M5.7 14.3l-1.5 1.5" stroke="currentColor" stroke-width="1.4"/></svg>
          <svg class="trn-19__moon" viewBox="0 0 20 20" width="15" height="15"><path d="M15.4 12.7A6.7 6.7 0 0 1 7.3 4.6a6.8 6.8 0 1 0 8.1 8.1Z" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>
        </span>
        <span>Theme</span>
      </label>
    </div>
    <header class="trn-19__head">
      <p class="trn-19__kicker">transition-property</p>
      <h2 class="trn-19__heading" id="trn-19-heading">The convenience that animates your mistakes</h2>
      <p class="trn-19__sub">Hover each group. The parent changes its padding on hover; watch what each card does with that.</p>
    </header>

    <div class="trn-19__pair">
      <div class="trn-19__group trn-19__group--bad">
        <p class="trn-19__label trn-19__label--bad">transition: all 260ms — catches the parent's padding change</p>
        <article class="trn-19__card trn-19__card--all">
          <h3 class="trn-19__ctitle">Talon &middot; api-gateway</h3>
          <p class="trn-19__cmeta">p99 184ms &middot; 3 replicas</p>
          <span class="trn-19__pill">healthy</span>
        </article>
        <ul class="trn-19__inventory">
          <li>transform &mdash; intended</li>
          <li>background-color &mdash; intended</li>
          <li>padding &mdash; inherited from parent, unintended</li>
          <li>border-radius &mdash; unintended</li>
          <li>letter-spacing &mdash; unintended</li>
        </ul>
      </div>

      <div class="trn-19__group trn-19__group--good">
        <p class="trn-19__label trn-19__label--good">transition-property: transform, background-color — two, named</p>
        <article class="trn-19__card trn-19__card--list">
          <h3 class="trn-19__ctitle">Talon &middot; api-gateway</h3>
          <p class="trn-19__cmeta">p99 184ms &middot; 3 replicas</p>
          <span class="trn-19__pill">healthy</span>
        </article>
        <ul class="trn-19__inventory">
          <li>transform &mdash; 160ms, composited</li>
          <li>background-color &mdash; 300ms, own pacing</li>
          <li>everything else &mdash; not watched</li>
        </ul>
      </div>
    </div>

    <code class="trn-19__code">transition-property: transform, background-color; transition-duration: 160ms, 300ms;</code>
  </div>
</section>
```
## CSS
```css
.trn-19 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --page: #f1f3f6;
  --page: oklch(0.96 0.005 265);
  --card: #ffffff;
  --ink: #1b1f27;
  --ink: oklch(0.24 0.012 265);
  --muted: #626b7a;
  --muted: oklch(0.52 0.016 265);
  --rule: #d5dae2;
  --rule: oklch(0.88 0.008 265);
  --bad: #c02a3f;
  --bad: oklch(0.51 0.18 15);
  --good: #1e7a54;
  --good: oklch(0.5 0.11 160);
  --font-display: ui-monospace, "IBM Plex Mono", Menlo, monospace;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

.trn-19 *,
.trn-19 *::before,
.trn-19 *::after {
  box-sizing: border-box;
}

.trn-19__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  padding: clamp(18px, 4vw, 44px) 12px;
}

.trn-19__head {
  inline-size: 100%;
  max-inline-size: 54rem;
  min-inline-size: 0;
  margin: 0 0 16px;
}

.trn-19__kicker {
  margin: 0 0 7px;
  font: 500 10.5px/1 var(--font-display);
  letter-spacing: 0.1em;
  color: var(--muted);
}

.trn-19__heading {
  margin: 0 0 6px;
  font: 500 clamp(21px, 4vw, 30px)/1.14 var(--font-display);
  letter-spacing: -0.025em;
  text-wrap: balance;
}

.trn-19__sub {
  margin: 0;
  max-inline-size: 56ch;
  font-size: 13px;
  line-height: 1.5;
  color: var(--muted);
  text-wrap: pretty;
}

.trn-19__pair {
  inline-size: 100%;
  max-inline-size: 54rem;
  min-inline-size: 0;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 16rem), 1fr));
  gap: 10px;
}

.trn-19__group {
  min-inline-size: 0;
  padding: 8px;
  background: var(--card);
  border: 1px solid var(--rule);
  border-radius: 5px;
  box-shadow: 0 1px 2px rgba(27, 31, 39, 0.05);
}

.trn-19__group--bad:hover {
  padding: 14px;
}

.trn-19__label {
  margin: 0 0 8px;
  font: 500 10.5px/1.4 var(--font-display);
}

.trn-19__label--bad {
  color: var(--bad);
}

.trn-19__label--good {
  color: var(--good);
}

.trn-19__card {
  min-inline-size: 0;
  padding: 10px;
  background: var(--page);
  border: 1px solid var(--rule);
  border-radius: 4px;
}

.trn-19__ctitle {
  margin: 0 0 3px;
  font: 500 12.5px/1.2 var(--font-display);
  letter-spacing: -0.01em;
}

.trn-19__cmeta {
  margin: 0 0 7px;
  font-size: 11px;
  line-height: 1.3;
  color: var(--muted);
}

.trn-19__pill {
  display: inline-block;
  padding: 3px 7px;
  border-radius: 3px;
  background: rgba(30, 122, 84, 0.12);
  font: 500 10px/1 var(--font-display);
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--good);
}

.trn-19__card--all {
  transition: all 260ms ease;
}

.trn-19__group--bad:hover .trn-19__card--all {
  transform: translateY(-3px);
  background: #fdecef;
  border-radius: 14px;
  letter-spacing: 0.04em;
}

.trn-19__card--list {
  transition-property: transform, background-color;
  transition-duration: 160ms, 300ms;
  transition-timing-function: cubic-bezier(.2, .8, .3, 1), ease;
}

.trn-19__group--good:hover .trn-19__card--list {
  transform: translateY(-3px);
  background: #e8f5ee;
}

.trn-19__inventory {
  list-style: none;
  margin: 8px 0 0;
  padding: 0;
  display: grid;
  gap: 3px;
  font: 400 10.5px/1.4 var(--font-display);
  color: var(--muted);
}

.trn-19__code {
  display: block;
  inline-size: 100%;
  max-inline-size: 54rem;
  margin-block-start: 12px;
  padding: 8px 10px;
  background: var(--card);
  border: 1px solid var(--rule);
  border-radius: 4px;
  font: 400 10.5px/1.5 var(--font-display);
  color: var(--ink);
  overflow-wrap: anywhere;
}

@media (prefers-reduced-motion: reduce) {
  .trn-19__card--all {
    transition: background-color 140ms ease;
  }

  .trn-19__group--bad:hover .trn-19__card--all {
    transform: none;
    border-radius: 4px;
    letter-spacing: normal;
  }

  .trn-19__group--bad:hover {
    padding: 8px;
  }

  .trn-19__card--list {
    transition-property: background-color;
    transition-duration: 140ms;
  }

  .trn-19__group--good:hover .trn-19__card--list {
    transform: none;
  }
}

@media (prefers-color-scheme: dark) {
  .trn-19 {
    --page: #0f1319;
    --page: oklch(0.19 0.012 265);
    --card: #161b23;
    --card: oklch(0.23 0.014 265);
    --ink: #e7ebf2;
    --ink: oklch(0.94 0.008 265);
    --muted: #97a1b2;
    --muted: oklch(0.71 0.018 265);
    --rule: #262d38;
    --rule: oklch(0.29 0.016 265);
    --bad: #ff7086;
    --bad: oklch(0.74 0.15 15);
    --good: #4fd39b;
    --good: oklch(0.81 0.12 162);
  }

  .trn-19__group {
    box-shadow: none;
  }

  .trn-19__pill {
    background: rgba(79, 211, 155, 0.14);
  }

  .trn-19__group--bad:hover .trn-19__card--all {
    background: #3a1c23;
  }

  .trn-19__group--good:hover .trn-19__card--list {
    background: #16302a;
  }
}

[data-theme="dark"] .trn-19 {
  --page: #0f1319;
  --card: #161b23;
  --ink: #e7ebf2;
  --muted: #97a1b2;
  --rule: #262d38;
  --bad: #ff7086;
  --good: #4fd39b;
}

[data-theme="dark"] .trn-19__group {
  box-shadow: none;
}

[data-theme="dark"] .trn-19__group--bad:hover .trn-19__card--all {
  background: #3a1c23;
}

[data-theme="dark"] .trn-19__group--good:hover .trn-19__card--list {
  background: #16302a;
}

.trn-19__theme {
  position: relative;
  inline-size: 100%;
  min-inline-size: 0;
  display: flex;
  justify-content: flex-end;
  margin: 0 0 14px;
}

.trn-19__themecb {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  clip-path: inset(50%);
  overflow: hidden;
}

.trn-19__themebtn {
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

.trn-19__themebtn:hover {
  color: var(--ink);
}

.trn-19__themecb:focus-visible + .trn-19__themebtn {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.trn-19__themeico {
  display: grid;
  place-items: center;
  inline-size: 15px;
  block-size: 15px;
}

.trn-19__themeico svg {
  grid-area: 1 / 1;
  transition: opacity 200ms ease;
}

.trn-19__sun {
  opacity: 1;
}

.trn-19__moon {
  opacity: 0.34;
}

.trn-19:has(#trn-19-theme:checked) .trn-19__sun {
  opacity: 0.34;
}

.trn-19:has(#trn-19-theme:checked) .trn-19__moon {
  opacity: 1;
}

@media (prefers-color-scheme: light) {
  .trn-19:has(#trn-19-theme:checked) {
    --page: #0f1319;
    --page: oklch(0.19 0.012 265);
    --card: #161b23;
    --card: oklch(0.23 0.014 265);
    --ink: #e7ebf2;
    --ink: oklch(0.94 0.008 265);
    --muted: #97a1b2;
    --muted: oklch(0.71 0.018 265);
    --rule: #262d38;
    --rule: oklch(0.29 0.016 265);
    --bad: #ff7086;
    --bad: oklch(0.74 0.15 15);
    --good: #4fd39b;
    --good: oklch(0.81 0.12 162);
  }

  .trn-19:has(#trn-19-theme:checked) .trn-19__group {
    box-shadow: none;
  }

  .trn-19:has(#trn-19-theme:checked) .trn-19__pill {
    background: rgba(79, 211, 155, 0.14);
  }

  .trn-19:has(#trn-19-theme:checked) .trn-19__group--bad:hover .trn-19__card--all {
    background: #3a1c23;
  }

  .trn-19:has(#trn-19-theme:checked) .trn-19__group--good:hover .trn-19__card--list {
    background: #16302a;
  }
}

@media (prefers-color-scheme: dark) {
  .trn-19:has(#trn-19-theme:checked) {
    --page: #f1f3f6;
    --page: oklch(0.96 0.005 265);
    --card: #ffffff;
    --ink: #1b1f27;
    --ink: oklch(0.24 0.012 265);
    --muted: #626b7a;
    --muted: oklch(0.52 0.016 265);
    --rule: #d5dae2;
    --rule: oklch(0.88 0.008 265);
    --bad: #c02a3f;
    --bad: oklch(0.51 0.18 15);
    --good: #1e7a54;
    --good: oklch(0.5 0.11 160);
    --font-display: ui-monospace, "IBM Plex Mono", Menlo, monospace;
    background: var(--page);
  }

  .trn-19:has(#trn-19-theme:checked) .trn-19__group {
    min-inline-size: 0;
    padding: 8px;
    background: var(--card);
    border: 1px solid var(--rule);
    border-radius: 5px;
    box-shadow: 0 1px 2px rgba(27, 31, 39, 0.05);
  }

  .trn-19:has(#trn-19-theme:checked) .trn-19__pill {
    display: inline-block;
    padding: 3px 7px;
    border-radius: 3px;
    background: rgba(30, 122, 84, 0.12);
    font: 500 10px/1 var(--font-display);
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: var(--good);
  }

  .trn-19:has(#trn-19-theme:checked) .trn-19__group--bad:hover .trn-19__card--all {
    transform: translateY(-3px);
    background: #fdecef;
    border-radius: 14px;
    letter-spacing: 0.04em;
  }

  .trn-19:has(#trn-19-theme:checked) .trn-19__group--good:hover .trn-19__card--list {
    transform: translateY(-3px);
    background: #e8f5ee;
  }

  .trn-19:has(#trn-19-theme:checked) .trn-19__sun {
    opacity: 1;
  }

  .trn-19:has(#trn-19-theme:checked) .trn-19__moon {
    opacity: 0.34;
  }
}
```
