---
source: "codefronts"
url: "https://codefronts.com/motion/css-transition-designs/flip-card-3d-transition/"
title: "Transform Transitions on the Compositor Thread"
section: "motion"
category: "css-transition-designs"
category_name: "CSS Transitions"
description: "Two identical cards, side by side and both labelled: the left one transitions top, left and width, the right one transitions transform."
has_js: "false"
---

Here's a working CSS Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Transform Transitions on the Compositor Thread
Source: https://codefronts.com/motion/css-transition-designs/flip-card-3d-transition/

Two identical cards, side by side and both labelled: the left one transitions top, left and width, the right one transitions transform. The rules and their per-frame cost are printed on each card, so the difference between a transition that re-runs layout sixty times a second and one that hands a matrix to the compositor is readable rather than theoretical.
## HTML
```html
<section class="trn-03" aria-labelledby="trn-03-heading">
  <div class="trn-03__stage">
    <div class="trn-03__theme">
      <input class="trn-03__themecb" type="checkbox" id="trn-03-theme">
      <label class="trn-03__themebtn" for="trn-03-theme">
        <span class="trn-03__themeico" aria-hidden="true">
          <svg class="trn-03__sun" viewBox="0 0 20 20" width="15" height="15"><circle cx="10" cy="10" r="3.9" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M10 1.7v2.1M10 16.2v2.1M1.7 10h2.1M16.2 10h2.1M4.2 4.2l1.5 1.5M14.3 14.3l1.5 1.5M15.8 4.2l-1.5 1.5M5.7 14.3l-1.5 1.5" stroke="currentColor" stroke-width="1.4"/></svg>
          <svg class="trn-03__moon" viewBox="0 0 20 20" width="15" height="15"><path d="M15.4 12.7A6.7 6.7 0 0 1 7.3 4.6a6.8 6.8 0 1 0 8.1 8.1Z" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>
        </span>
        <span>Theme</span>
      </label>
    </div>
    <header class="trn-03__head">
      <h2 class="trn-03__heading" id="trn-03-heading">Same motion, two very different bills</h2>
      <p class="trn-03__sub">Hover or focus either card. The rule and the pipeline it triggers are printed on each side.</p>
    </header>

    <div class="trn-03__pair">
      <article class="trn-03__side trn-03__side--bad">
        <p class="trn-03__sidelabel">Transitions top / left / width — reflows every frame</p>
        <div class="trn-03__frame">
          <button class="trn-03__card trn-03__card--layout" type="button">
            <span class="trn-03__ctitle">Basalt build 4192</span>
            <span class="trn-03__cmeta">passed · 2m 14s</span>
          </button>
        </div>
        <ul class="trn-03__pipeline">
          <li class="trn-03__on">layout</li>
          <li class="trn-03__on">paint</li>
          <li class="trn-03__on">composite</li>
        </ul>
        <code class="trn-03__code">transition: top 420ms ease, left 420ms ease, width 420ms ease;</code>
        <p class="trn-03__cost">Main thread, 60&times; per second. Competes with every script on the page.</p>
      </article>

      <article class="trn-03__side trn-03__side--good">
        <p class="trn-03__sidelabel">Transitions transform — composited, off the main thread</p>
        <div class="trn-03__frame">
          <button class="trn-03__card trn-03__card--xform" type="button">
            <span class="trn-03__ctitle">Basalt build 4192</span>
            <span class="trn-03__cmeta">passed · 2m 14s</span>
          </button>
        </div>
        <ul class="trn-03__pipeline">
          <li>layout</li>
          <li>paint</li>
          <li class="trn-03__on">composite</li>
        </ul>
        <code class="trn-03__code">transition: transform 420ms cubic-bezier(.2,.7,.3,1);</code>
        <p class="trn-03__cost">One matrix handed to the compositor. Layout and paint are untouched.</p>
      </article>
    </div>

    <p class="trn-03__foot"><strong>will-change</strong> is set on hover intent here, not permanently — a promoted layer costs GPU memory for as long as it exists.</p>
  </div>
</section>
```
## CSS
```css
.trn-03 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --page: #f7f4ee;
  --page: oklch(0.97 0.011 85);
  --card: #fffdf8;
  --ink: #1c1a15;
  --ink: oklch(0.23 0.012 75);
  --muted: #6b6558;
  --muted: oklch(0.52 0.018 82);
  --rule: #d9d3c4;
  --rule: oklch(0.87 0.018 84);
  --bad: #c2371f;
  --bad: oklch(0.52 0.185 32);
  --good: #1f7a45;
  --good: oklch(0.5 0.126 154);
  --travel: 46%;
  --font-display: "Helvetica Neue", system-ui, -apple-system, sans-serif;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

.trn-03 *,
.trn-03 *::before,
.trn-03 *::after {
  box-sizing: border-box;
}

.trn-03__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  padding: clamp(22px, 5vw, 52px) 14px;
}

.trn-03__head {
  inline-size: 100%;
  max-inline-size: 56rem;
  min-inline-size: 0;
  margin: 0 0 22px;
}

.trn-03__heading {
  margin: 0 0 8px;
  font: 700 clamp(23px, 4.4vw, 34px)/1.1 var(--font-display);
  letter-spacing: -0.025em;
  text-wrap: balance;
}

.trn-03__sub {
  margin: 0;
  max-inline-size: 50ch;
  font-size: 14px;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.trn-03__pair {
  inline-size: 100%;
  max-inline-size: 56rem;
  min-inline-size: 0;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 17rem), 1fr));
  gap: 14px;
}

.trn-03__side {
  min-inline-size: 0;
  padding: 12px;
  background: var(--card);
  border: 1.5px solid var(--ink);
  border-radius: 2px;
  box-shadow: 5px 5px 0 var(--ink);
}

.trn-03__sidelabel {
  margin: 0 0 10px;
  font: 700 11.5px/1.4 ui-monospace, Menlo, monospace;
  letter-spacing: 0.01em;
}

.trn-03__side--bad .trn-03__sidelabel {
  color: var(--bad);
}

.trn-03__side--good .trn-03__sidelabel {
  color: var(--good);
}

.trn-03__frame {
  position: relative;
  block-size: 132px;
  border: 1px dashed var(--rule);
  background: var(--page);
  overflow: hidden;
}

.trn-03__card {
  position: absolute;
  inset-block-start: 10px;
  inset-inline-start: 8px;
  inline-size: 48%;
  min-inline-size: 132px;
  min-height: 62px;
  display: grid;
  gap: 4px;
  align-content: center;
  padding: 10px 12px;
  text-align: start;
  background: var(--card);
  border: 1px solid var(--ink);
  border-radius: 2px;
  cursor: pointer;
}

.trn-03__card:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.trn-03__ctitle {
  font: 600 13px/1.2 var(--font-display);
  color: var(--ink);
}

.trn-03__cmeta {
  font: 400 11px/1 ui-monospace, Menlo, monospace;
  color: var(--muted);
}

.trn-03__card--layout {
  transition: top 420ms ease, left 420ms ease, width 420ms ease, border-color 420ms ease;
}

.trn-03__side--bad:hover .trn-03__card--layout,
.trn-03__card--layout:focus-visible {
  inset-block-start: 56px;
  inset-inline-start: var(--travel);
  inline-size: 44%;
  border-color: var(--bad);
}

.trn-03__card--xform {
  transition: transform 420ms cubic-bezier(.2, .7, .3, 1), border-color 420ms ease;
}

.trn-03__side--good:hover .trn-03__card--xform {
  will-change: transform;
}

.trn-03__side--good:hover .trn-03__card--xform,
.trn-03__card--xform:focus-visible {
  transform: translate(88%, 46px) scale(0.94);
  border-color: var(--good);
}

.trn-03__pipeline {
  list-style: none;
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin: 10px 0 0;
  padding: 0;
}

.trn-03__pipeline li {
  padding: 4px 8px;
  border: 1px solid var(--rule);
  border-radius: 2px;
  font: 500 10.5px/1 ui-monospace, Menlo, monospace;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--rule);
}

.trn-03__side--bad .trn-03__on {
  color: var(--bad);
  border-color: var(--bad);
}

.trn-03__side--good .trn-03__on {
  color: var(--good);
  border-color: var(--good);
}

.trn-03__code {
  display: block;
  margin-block-start: 10px;
  padding: 8px;
  background: var(--page);
  border: 1px solid var(--rule);
  font: 400 11px/1.5 ui-monospace, Menlo, monospace;
  color: var(--ink);
  overflow-wrap: anywhere;
}

.trn-03__cost {
  margin: 8px 0 0;
  font-size: 12px;
  line-height: 1.5;
  color: var(--muted);
}

.trn-03__foot {
  inline-size: 100%;
  max-inline-size: 56rem;
  margin: 16px 0 0;
  font-size: 12.5px;
  line-height: 1.55;
  color: var(--muted);
}

.trn-03__foot strong {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 11.5px;
  color: var(--ink);
}

@media (prefers-reduced-motion: reduce) {
  .trn-03__card--layout,
    .trn-03__card--xform {
    transition: border-color 140ms ease, background-color 140ms ease;
  }

  .trn-03__side--bad:hover .trn-03__card--layout,
    .trn-03__card--layout:focus-visible {
    inset-block-start: 10px;
    inset-inline-start: 8px;
    inline-size: 48%;
    background: #fbe9e4;
  }

  .trn-03__side--good:hover .trn-03__card--xform,
    .trn-03__card--xform:focus-visible {
    transform: none;
    background: #e4f3ea;
  }
}

@media (prefers-color-scheme: dark) {
  .trn-03 {
    --page: #16150f;
    --page: oklch(0.2 0.012 80);
    --card: #1f1d16;
    --ink: #f3efe4;
    --ink: oklch(0.95 0.014 85);
    --muted: #a39b89;
    --muted: oklch(0.72 0.02 84);
    --rule: #35322a;
    --bad: #ff8163;
    --bad: oklch(0.74 0.16 38);
    --good: #58d68d;
    --good: oklch(0.8 0.14 156);
  }

  .trn-03__side {
    box-shadow: 5px 5px 0 #35322a;
  }

  .trn-03__pipeline li {
    color: #565044;
    border-color: #35322a;
  }
}

[data-theme="dark"] .trn-03 {
  --page: #16150f;
  --card: #1f1d16;
  --ink: #f3efe4;
  --muted: #a39b89;
  --rule: #35322a;
  --bad: #ff8163;
  --good: #58d68d;
}

[data-theme="dark"] .trn-03__side {
  box-shadow: 5px 5px 0 #35322a;
}

[data-theme="dark"] .trn-03__pipeline li {
  color: #565044;
  border-color: #35322a;
}

.trn-03__theme {
  position: relative;
  inline-size: 100%;
  min-inline-size: 0;
  display: flex;
  justify-content: flex-end;
  margin: 0 0 14px;
}

.trn-03__themecb {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  clip-path: inset(50%);
  overflow: hidden;
}

.trn-03__themebtn {
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

.trn-03__themebtn:hover {
  color: var(--ink);
}

.trn-03__themecb:focus-visible + .trn-03__themebtn {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.trn-03__themeico {
  display: grid;
  place-items: center;
  inline-size: 15px;
  block-size: 15px;
}

.trn-03__themeico svg {
  grid-area: 1 / 1;
  transition: opacity 200ms ease;
}

.trn-03__sun {
  opacity: 1;
}

.trn-03__moon {
  opacity: 0.34;
}

.trn-03:has(#trn-03-theme:checked) .trn-03__sun {
  opacity: 0.34;
}

.trn-03:has(#trn-03-theme:checked) .trn-03__moon {
  opacity: 1;
}

@media (prefers-color-scheme: light) {
  .trn-03:has(#trn-03-theme:checked) {
    --page: #16150f;
    --page: oklch(0.2 0.012 80);
    --card: #1f1d16;
    --ink: #f3efe4;
    --ink: oklch(0.95 0.014 85);
    --muted: #a39b89;
    --muted: oklch(0.72 0.02 84);
    --rule: #35322a;
    --bad: #ff8163;
    --bad: oklch(0.74 0.16 38);
    --good: #58d68d;
    --good: oklch(0.8 0.14 156);
  }

  .trn-03:has(#trn-03-theme:checked) .trn-03__side {
    box-shadow: 5px 5px 0 #35322a;
  }

  .trn-03:has(#trn-03-theme:checked) .trn-03__pipeline li {
    color: #565044;
    border-color: #35322a;
  }
}

@media (prefers-color-scheme: dark) {
  .trn-03:has(#trn-03-theme:checked) {
    --page: #f7f4ee;
    --page: oklch(0.97 0.011 85);
    --card: #fffdf8;
    --ink: #1c1a15;
    --ink: oklch(0.23 0.012 75);
    --muted: #6b6558;
    --muted: oklch(0.52 0.018 82);
    --rule: #d9d3c4;
    --rule: oklch(0.87 0.018 84);
    --bad: #c2371f;
    --bad: oklch(0.52 0.185 32);
    --good: #1f7a45;
    --good: oklch(0.5 0.126 154);
    --travel: 46%;
    --font-display: "Helvetica Neue", system-ui, -apple-system, sans-serif;
    background: var(--page);
  }

  .trn-03:has(#trn-03-theme:checked) .trn-03__side {
    min-inline-size: 0;
    padding: 12px;
    background: var(--card);
    border: 1.5px solid var(--ink);
    border-radius: 2px;
    box-shadow: 5px 5px 0 var(--ink);
  }

  .trn-03:has(#trn-03-theme:checked) .trn-03__pipeline li {
    padding: 4px 8px;
    border: 1px solid var(--rule);
    border-radius: 2px;
    font: 500 10.5px/1 ui-monospace, Menlo, monospace;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: var(--rule);
  }

  .trn-03:has(#trn-03-theme:checked) .trn-03__sun {
    opacity: 1;
  }

  .trn-03:has(#trn-03-theme:checked) .trn-03__moon {
    opacity: 0.34;
  }
}
```
