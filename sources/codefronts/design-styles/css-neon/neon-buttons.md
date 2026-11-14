---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-neon/neon-buttons/"
title: "Neon Glow Button Construction Reference"
section: "design-styles"
category: "css-neon"
category_name: "CSS Neon Effects"
description: "The three-layer stack applied to the smallest honest test surface: a button with rest, hover, active and focus-visible states, each layer annotated with the…"
has_js: "false"
---

Here's a working CSS Neon Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neon Glow Button Construction Reference
Source: https://codefronts.com/design-styles/css-neon/neon-buttons/

The three-layer stack applied to the smallest honest test surface: a button with rest, hover, active and focus-visible states, each layer annotated with the values it uses. The chrome is deliberately plain so the subject stays the light — what changes between states, what must not change, and why the focus state is a ring rather than a brighter halo.
## HTML
```html
<section class="nn-09" aria-labelledby="nn-09-heading">
  <div class="nn-09__stage">
    <div class="nn-09__theme">
      <input class="nn-09__tin" type="checkbox" id="nn-09-theme">
      <label class="nn-09__tlab" for="nn-09-theme">
        <svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M8 1.5v2M8 12.5v2M1.5 8h2M12.5 8h2M3.4 3.4l1.4 1.4M11.2 11.2l1.4 1.4M12.6 3.4l-1.4 1.4M4.8 11.2l-1.4 1.4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"></path><circle cx="8" cy="8" r="2.6" fill="none" stroke="currentColor" stroke-width="1.5"></circle></svg>
        Flip light / dark
      </label>
    </div>
    <header class="nn-09__head">
      <p class="nn-09__kicker">Four states, one stack</p>
      <h2 class="nn-09__heading" id="nn-09-heading">The glow stack on a deliberately plain button</h2>
      <p class="nn-09__sub">Hover, press and focus the control. The blur radii never change &mdash; only the alphas, plus one inset layer on press and a real ring on focus.</p>
    </header>

    <div class="nn-09__deck">
      <div class="nn-09__well">
        <button class="nn-09__btn" type="button">Deploy to production</button>
        <button class="nn-09__btn nn-09__btn--quiet" type="button">Run checks first</button>
        <button class="nn-09__btn" type="button" disabled>Deploy to production</button>
        <p class="nn-09__hint">The third button is disabled: every layer is removed, and only the label contrast is kept.</p>
      </div>

      <table class="nn-09__table">
        <caption class="nn-09__caption">Per-state layer values</caption>
        <thead>
          <tr><th scope="col">State</th><th scope="col">Core</th><th scope="col">Halo</th><th scope="col">Bloom</th><th scope="col">Extra</th></tr>
        </thead>
        <tbody>
          <tr><th scope="row">Rest</th><td>6px / .6</td><td>18px / .34</td><td>44px / .16</td><td>&mdash;</td></tr>
          <tr><th scope="row">Hover</th><td>6px / 1</td><td>18px / .55</td><td>44px / .3</td><td>&mdash;</td></tr>
          <tr><th scope="row">Active</th><td>4px / 1</td><td>12px / .4</td><td>none</td><td>inset 10px</td></tr>
          <tr><th scope="row">Focus-visible</th><td>6px / .6</td><td>18px / .34</td><td>44px / .16</td><td>2px ring, 2px offset</td></tr>
        </tbody>
      </table>
    </div>

    <p class="nn-09__rule">Hover changes brightness. Press changes direction &mdash; the light moves inside. Focus adds a ring, because a blurred edge has no boundary for a contrast ratio to be measured against.</p>
  </div>
</section>
```
## CSS
```css
.nn-09 {
  --nn-09-bad: #f4a4a4;
  --nn-09-warn: #f0c88a;
  --nn-09-spec-neon: #ff7a5c;
}

@media (prefers-color-scheme: light) {
  .nn-09 {
    --nn-09-bad: #a12a20;
    --nn-09-warn: #78490a;
  }

  .nn-09:has(#nn-09-theme:checked) {
    --nn-09-bad: #f4a4a4;
    --nn-09-warn: #f0c88a;
  }
}

@media (prefers-color-scheme: dark) {
  .nn-09:has(#nn-09-theme:checked) {
    --nn-09-bad: #a12a20;
    --nn-09-warn: #78490a;
  }
}

.nn-09[data-theme="light"] {
  --nn-09-bad: #a12a20;
  --nn-09-warn: #78490a;
}

.nn-09 {
  --nn-09-spec-ink: #f8efe9;
  --nn-09-spec-dim: #a89689;
}

.nn-09__theme {
  position: absolute;
  inset-block-start: clamp(10px, 2vw, 18px);
  inset-inline-end: clamp(10px, 2vw, 18px);
  z-index: 5;
  display: flex;
  justify-content: flex-end;
}

.nn-09__tin {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.nn-09__tlab {
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  min-height: 44px;
  padding: 0 .8rem;
  border: 1px solid currentColor;
  font-size: .7rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  cursor: pointer;
  opacity: .7;
}

.nn-09__tlab svg {
  width: .9rem;
  height: .9rem;
  flex: none;
}

.nn-09__tlab:hover {
  opacity: 1;
}

.nn-09__tin:focus-visible + .nn-09__tlab {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

@media (prefers-color-scheme: light) {
  .nn-09:has(#nn-09-theme:checked) {
    --nn-09-bg: #0d0a09;
    --nn-09-well: #14100e;
    --nn-09-line: #2b231f;
    --nn-09-ink: #f8efe9;
    --nn-09-muted: #a89689;
    --nn-09-neon: #ff7a5c;
  }
}

@media (prefers-color-scheme: dark) {
  .nn-09:has(#nn-09-theme:checked) {
    --nn-09-bg: #efeae7;
    --nn-09-well: #1d1715;
    --nn-09-line: #cdc4bf;
    --nn-09-ink: #16110f;
    --nn-09-muted: #564a44;
    --nn-09-neon: #a83415;
  }
}

.nn-09 {
  --nn-09-hue: 28;
  --nn-09-bg: #0d0a09;
  --nn-09-well: #14100e;
  --nn-09-line: #2b231f;
  --nn-09-ink: #f8efe9;
  --nn-09-muted: #a89689;
  --nn-09-neon: #ff7a5c;
  --nn-09-core: rgba(255, 122, 92, .6);
  --nn-09-halo: rgba(255, 122, 92, .34);
  --nn-09-bloom: rgba(255, 122, 92, .16);
  --nn-09-core-hi: rgba(255, 122, 92, 1);
  --nn-09-halo-hi: rgba(255, 122, 92, .55);
  --nn-09-bloom-hi: rgba(255, 122, 92, .3);
  --nn-09-font-display: system-ui, "Helvetica Neue", Arial, sans-serif;
  width: 100%;
  min-height: 100vh;
  position: relative;
  display: block;
  box-sizing: border-box;
  background: var(--nn-09-bg);
  color: var(--nn-09-ink);
  font-family: system-ui, sans-serif;
}

.nn-09 *,
.nn-09 *::before,
.nn-09 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(50% 0.1 200)) {
  .nn-09 {
    --nn-09-bg: oklch(15% 0.012 40);
    --nn-09-well: oklch(19% 0.016 40);
    --nn-09-line: oklch(29% 0.02 40);
    --nn-09-ink: oklch(96% 0.014 45);
    --nn-09-muted: oklch(74% 0.024 45);
    --nn-09-neon: oklch(76% 0.17 var(--nn-09-hue));
    --nn-09-core: oklch(76% 0.17 var(--nn-09-hue) / .6);
    --nn-09-halo: oklch(74% 0.16 var(--nn-09-hue) / .34);
    --nn-09-bloom: oklch(72% 0.15 var(--nn-09-hue) / .16);
    --nn-09-core-hi: oklch(80% 0.18 var(--nn-09-hue) / 1);
    --nn-09-halo-hi: oklch(76% 0.17 var(--nn-09-hue) / .55);
    --nn-09-bloom-hi: oklch(74% 0.16 var(--nn-09-hue) / .3);
  }
}

@media (prefers-color-scheme: light) {
  .nn-09 {
    --nn-09-bg: #efeae7;
    --nn-09-well: #1d1715;
    --nn-09-line: #cdc4bf;
    --nn-09-ink: #16110f;
    --nn-09-muted: #564a44;
    --nn-09-neon: #a83415;
  }
}

.nn-09[data-theme="light"] {
  --nn-09-bg: #efeae7;
  --nn-09-well: #1d1715;
  --nn-09-line: #cdc4bf;
  --nn-09-ink: #16110f;
  --nn-09-muted: #564a44;
  --nn-09-neon: #a83415;
}

.nn-09[data-theme="dark"] {
  --nn-09-bad: #f4a4a4;
  --nn-09-warn: #f0c88a;
  --nn-09-bg: #0d0a09;
  --nn-09-well: #14100e;
  --nn-09-line: #2b231f;
  --nn-09-ink: #f8efe9;
  --nn-09-muted: #a89689;
  --nn-09-neon: #ff7a5c;
}

.nn-09__stage {
  max-width: 66rem;
  margin: 0 auto;
  padding: clamp(1.25rem, 4vw, 1.75rem) clamp(1rem, 4vw, 1.75rem) clamp(1.75rem, 5vw, 2.25rem);
  display: grid;
  gap: clamp(1.15rem, 3vw, 1.5rem);
}

.nn-09__kicker {
  margin: 0 0 .4rem;
  font-size: .72rem;
  font-weight: 600;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--nn-09-neon);
}

.nn-09__heading {
  margin: 0;
  font-family: var(--nn-09-font-display);
  font-size: clamp(1.35rem, 4.6vw, 2rem);
  font-weight: 650;
  letter-spacing: -.022em;
  text-wrap: balance;
}

.nn-09__sub {
  margin: .55rem 0 0;
  max-width: 42rem;
  font-size: .9rem;
  line-height: 1.6;
  color: var(--nn-09-muted);
  text-wrap: pretty;
}

.nn-09__deck {
  display: grid;
  gap: 1rem;
  grid-template-columns: 1fr;
}

@media (min-width: 56rem) {
  .nn-09__deck {
    grid-template-columns: minmax(0, 20rem) minmax(0, 1fr);
    align-items: start;
  }
}

.nn-09__well {
  display: grid;
  gap: .8rem;
  justify-items: start;
  padding: clamp(1.15rem, 4vw, 1.5rem);
  border-radius: .5rem;
  border: 1px solid var(--nn-09-line);
  background: var(--nn-09-well);
}

.nn-09__btn {
  min-height: 44px;
  padding: .7rem 1.2rem;
  border: 1px solid var(--nn-09-spec-neon);
  border-radius: .35rem;
  background: #17110f;
  color: var(--nn-09-spec-ink);
  font-family: inherit;
  font-size: .88rem;
  font-weight: 550;
  letter-spacing: -.01em;
  cursor: pointer;
  transition: box-shadow 140ms ease, background-color 140ms ease;
  box-shadow: 0 0 .38rem var(--nn-09-core), 0 0 1.1rem var(--nn-09-halo), 0 0 clamp(1.5rem, 7vw, 2.75rem) var(--nn-09-bloom);
}

.nn-09__btn:hover {
  box-shadow: 0 0 .38rem var(--nn-09-core-hi), 0 0 1.1rem var(--nn-09-halo-hi), 0 0 clamp(1.5rem, 7vw, 2.75rem) var(--nn-09-bloom-hi);
}

.nn-09__btn:active {
  box-shadow: 0 0 .25rem var(--nn-09-core-hi), 0 0 .75rem var(--nn-09-halo), inset 0 0 .65rem var(--nn-09-halo-hi);
}

.nn-09__btn:focus-visible {
  outline: 2px solid var(--nn-09-ink);
  outline-offset: 2px;
}

.nn-09__btn--quiet {
  border-color: var(--nn-09-line);
  color: var(--nn-09-spec-dim);
  box-shadow: 0 0 .38rem var(--nn-09-core), 0 0 1.1rem var(--nn-09-halo);
}

.nn-09__btn--quiet:hover {
  color: var(--nn-09-spec-ink);
  box-shadow: 0 0 .38rem var(--nn-09-core-hi), 0 0 1.1rem var(--nn-09-halo-hi);
}

.nn-09__btn[disabled] {
  border-color: var(--nn-09-line);
  color: var(--nn-09-spec-dim);
  box-shadow: none;
  cursor: not-allowed;
}

.nn-09__hint {
  margin: 0;
  font-size: .76rem;
  line-height: 1.5;
  color: var(--nn-09-spec-dim);
  text-wrap: pretty;
}

.nn-09__table {
  width: 100%;
  border-collapse: collapse;
  font-size: .78rem;
  min-inline-size: 0;
}

.nn-09__caption {
  padding-bottom: .5rem;
  text-align: left;
  font-size: .7rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--nn-09-muted);
}

.nn-09__table th,
.nn-09__table td {
  padding: .55rem .5rem;
  text-align: left;
  border-bottom: 1px solid var(--nn-09-line);
}

.nn-09__table thead th {
  font-family: ui-monospace, Menlo, monospace;
  font-size: .68rem;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: var(--nn-09-muted);
  font-weight: 400;
}

.nn-09__table tbody th {
  font-weight: 600;
  color: var(--nn-09-neon);
}

.nn-09__table td {
  font-family: ui-monospace, Menlo, monospace;
  font-size: .72rem;
  color: var(--nn-09-ink);
}

.nn-09__rule {
  margin: 0;
  padding: .95rem 1.1rem;
  border-radius: .5rem;
  border: 1px solid var(--nn-09-line);
  border-left: 2px solid var(--nn-09-neon);
  font-size: .86rem;
  line-height: 1.6;
  text-wrap: pretty;
}
```
