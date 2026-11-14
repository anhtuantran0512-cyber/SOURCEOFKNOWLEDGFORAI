---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-neon/neon-cyberpunk-palette/"
title: "Cyberpunk Neon Palette and Token Set"
section: "design-styles"
category: "css-neon"
category_name: "CSS Neon Effects"
description: "A token system where one hue value drives the core, halo and bloom layers across a small component set, so retinting is a one-value edit rather than a…"
has_js: "false"
---

Here's a working CSS Neon Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Cyberpunk Neon Palette and Token Set
Source: https://codefronts.com/design-styles/css-neon/neon-cyberpunk-palette/

A token system where one hue value drives the core, halo and bloom layers across a small component set, so retinting is a one-value edit rather than a search-and-replace. Three hue presets switch the entire set with no JavaScript, using :has() on radio inputs, and the token table shows exactly what is derived from what.
## HTML
```html
<section class="nn-16" aria-labelledby="nn-16-heading">
  <div class="nn-16__stage">
    <div class="nn-16__theme">
      <input class="nn-16__tin" type="checkbox" id="nn-16-theme">
      <label class="nn-16__tlab" for="nn-16-theme">
        <svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M8 1.5v2M8 12.5v2M1.5 8h2M12.5 8h2M3.4 3.4l1.4 1.4M11.2 11.2l1.4 1.4M12.6 3.4l-1.4 1.4M4.8 11.2l-1.4 1.4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"></path><circle cx="8" cy="8" r="2.6" fill="none" stroke="currentColor" stroke-width="1.5"></circle></svg>
        Flip light / dark
      </label>
    </div>
    <header class="nn-16__head">
      <p class="nn-16__kicker">One token, four components</p>
      <h2 class="nn-16__heading" id="nn-16-heading">Retinting a neon set should be one edit</h2>
      <p class="nn-16__sub">Core, halo and bloom are all derived from a single hue value. Switch it below &mdash; radio inputs and <span class="nn-16__code">:has()</span>, no script.</p>
    </header>

    <fieldset class="nn-16__switch">
      <legend class="nn-16__legend">Hue preset</legend>
      <div class="nn-16__opts">
        <input class="nn-16__radio" type="radio" name="nn-16-hue" id="nn-16-h1" checked>
        <label class="nn-16__opt" for="nn-16-h1">248 &middot; electric blue</label>
        <input class="nn-16__radio" type="radio" name="nn-16-hue" id="nn-16-h2">
        <label class="nn-16__opt" for="nn-16-h2">158 &middot; acid green</label>
        <input class="nn-16__radio" type="radio" name="nn-16-hue" id="nn-16-h3">
        <label class="nn-16__opt" for="nn-16-h3">330 &middot; hot pink</label>
      </div>
    </fieldset>

    <div class="nn-16__set">
      <div class="nn-16__card">
        <p class="nn-16__badge">Live</p>
        <p class="nn-16__ctitle">Talon gateway</p>
        <p class="nn-16__cbody">Edge nodes in three regions. Median response 41ms over the last hour.</p>
        <div class="nn-16__meter"><span class="nn-16__fill"></span></div>
        <button class="nn-16__btn" type="button">Open channel</button>
      </div>

      <table class="nn-16__tokens">
        <caption class="nn-16__caption">Derivation chain</caption>
        <thead><tr><th scope="col">Token</th><th scope="col">Derived from</th></tr></thead>
        <tbody>
          <tr><th scope="row">--nn-16-hue</th><td>the one value you edit</td></tr>
          <tr><th scope="row">--nn-16-base</th><td>oklch(78% .19 hue)</td></tr>
          <tr><th scope="row">--nn-16-core</th><td>mix(base 85%, transparent)</td></tr>
          <tr><th scope="row">--nn-16-halo</th><td>mix(base 45%, transparent)</td></tr>
          <tr><th scope="row">--nn-16-bloom</th><td>mix(base 24%, transparent)</td></tr>
          <tr><th scope="row">--nn-16-edge</th><td>mix(base 55%, line)</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>
```
## CSS
```css
.nn-16 {
  --nn-16-bad: #f4a4a4;
  --nn-16-warn: #f0c88a;
}

@media (prefers-color-scheme: light) {
  .nn-16 {
    --nn-16-bad: #a12a20;
    --nn-16-warn: #78490a;
  }

  .nn-16:has(#nn-16-theme:checked) {
    --nn-16-bad: #f4a4a4;
    --nn-16-warn: #f0c88a;
  }
}

@media (prefers-color-scheme: dark) {
  .nn-16:has(#nn-16-theme:checked) {
    --nn-16-bad: #a12a20;
    --nn-16-warn: #78490a;
  }
}

.nn-16[data-theme="light"] {
  --nn-16-bad: #a12a20;
  --nn-16-warn: #78490a;
}

.nn-16 {
  --nn-16-spec-ink: #f0ecfa;
  --nn-16-spec-dim: #a196bd;
}

.nn-16__theme {
  position: absolute;
  inset-block-start: clamp(10px, 2vw, 18px);
  inset-inline-end: clamp(10px, 2vw, 18px);
  z-index: 5;
  display: flex;
  justify-content: flex-end;
}

.nn-16__tin {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.nn-16__tlab {
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

.nn-16__tlab svg {
  width: .9rem;
  height: .9rem;
  flex: none;
}

.nn-16__tlab:hover {
  opacity: 1;
}

.nn-16__tin:focus-visible + .nn-16__tlab {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

@media (prefers-color-scheme: light) {
  .nn-16:has(#nn-16-theme:checked) {
    --nn-16-bg: #120e1c;
    --nn-16-panel: #191327;
    --nn-16-line: #2c2342;
    --nn-16-ink: #f0ecfa;
    --nn-16-muted: #a196bd;
  }
}

@media (prefers-color-scheme: dark) {
  .nn-16:has(#nn-16-theme:checked) {
    --nn-16-bg: #edeaf3;
    --nn-16-panel: #ffffff;
    --nn-16-line: #ccc5da;
    --nn-16-ink: #150f22;
    --nn-16-muted: #544a68;
  }
}

.nn-16 {
  --nn-16-hue: 248;
  --nn-16-bg: #120e1c;
  --nn-16-panel: #191327;
  --nn-16-line: #2c2342;
  --nn-16-ink: #f0ecfa;
  --nn-16-muted: #a196bd;
  --nn-16-base: #7b8cff;
  --nn-16-core: rgba(123, 140, 255, .85);
  --nn-16-halo: rgba(123, 140, 255, .45);
  --nn-16-bloom: rgba(123, 140, 255, .24);
  --nn-16-edge: #4a4f96;
  --nn-16-font-display: system-ui, "Helvetica Neue", Arial, sans-serif;
  width: 100%;
  min-height: 100vh;
  position: relative;
  display: block;
  box-sizing: border-box;
  background: var(--nn-16-bg);
  color: var(--nn-16-ink);
  font-family: system-ui, sans-serif;
}

.nn-16 *,
.nn-16 *::before,
.nn-16 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(50% 0.1 200)) {
  .nn-16 {
    --nn-16-bg: oklch(17% 0.035 295);
    --nn-16-panel: oklch(21% 0.045 295);
    --nn-16-line: oklch(31% 0.05 295);
    --nn-16-ink: oklch(96% 0.014 295);
    --nn-16-muted: oklch(73% 0.035 295);
    --nn-16-base: oklch(78% 0.19 var(--nn-16-hue));
  }
}

@supports (color: color-mix(in oklab, red, blue)) {
  .nn-16 {
    --nn-16-core: color-mix(in oklab, var(--nn-16-base) 85%, transparent);
    --nn-16-halo: color-mix(in oklab, var(--nn-16-base) 45%, transparent);
    --nn-16-bloom: color-mix(in oklab, var(--nn-16-base) 24%, transparent);
    --nn-16-edge: color-mix(in oklab, var(--nn-16-base) 55%, var(--nn-16-line));
  }
}

@supports selector(:has(*)) {
  .nn-16:has(#nn-16-h2:checked) {
    --nn-16-hue: 158;
  }

  .nn-16:has(#nn-16-h3:checked) {
    --nn-16-hue: 330;
  }
}

@media (prefers-color-scheme: light) {
  .nn-16 {
    --nn-16-bg: #edeaf3;
    --nn-16-panel: #ffffff;
    --nn-16-line: #ccc5da;
    --nn-16-ink: #150f22;
    --nn-16-muted: #544a68;
  }
}

.nn-16[data-theme="light"] {
  --nn-16-bg: #edeaf3;
  --nn-16-panel: #ffffff;
  --nn-16-line: #ccc5da;
  --nn-16-ink: #150f22;
  --nn-16-muted: #544a68;
}

.nn-16[data-theme="dark"] {
  --nn-16-bad: #f4a4a4;
  --nn-16-warn: #f0c88a;
  --nn-16-bg: #120e1c;
  --nn-16-panel: #191327;
  --nn-16-line: #2c2342;
  --nn-16-ink: #f0ecfa;
  --nn-16-muted: #a196bd;
}

.nn-16__stage {
  max-width: 66rem;
  margin: 0 auto;
  padding: clamp(1.25rem, 4vw, 1.75rem) clamp(1rem, 4vw, 1.75rem) clamp(1.75rem, 5vw, 2.25rem);
  display: grid;
  gap: clamp(1.1rem, 3vw, 1.5rem);
}

.nn-16__kicker {
  margin: 0 0 .4rem;
  font-size: .72rem;
  font-weight: 600;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--nn-16-base);
}

.nn-16__heading {
  margin: 0;
  font-family: var(--nn-16-font-display);
  font-size: clamp(1.3rem, 4.6vw, 1.95rem);
  font-weight: 640;
  letter-spacing: -.025em;
  text-wrap: balance;
}

.nn-16__sub {
  margin: .5rem 0 0;
  max-width: 40rem;
  font-size: .89rem;
  line-height: 1.6;
  color: var(--nn-16-muted);
  text-wrap: pretty;
}

.nn-16__code {
  font-family: ui-monospace, Menlo, monospace;
  font-size: .9em;
  color: var(--nn-16-base);
}

.nn-16__switch {
  margin: 0;
  padding: .75rem .85rem;
  border: 1px solid var(--nn-16-line);
  border-radius: .5rem;
  background: var(--nn-16-panel);
}

.nn-16__legend {
  padding: 0 .35rem;
  font-size: .68rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--nn-16-muted);
}

.nn-16__opts {
  display: flex;
  gap: .4rem;
  flex-wrap: wrap;
}

.nn-16__radio {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.nn-16__opt {
  display: flex;
  align-items: center;
  min-height: 44px;
  padding: 0 .85rem;
  border: 1px solid var(--nn-16-line);
  border-radius: .35rem;
  font-size: .8rem;
  color: var(--nn-16-muted);
  cursor: pointer;
}

.nn-16__opt:hover {
  color: var(--nn-16-ink);
  border-color: var(--nn-16-edge);
}

.nn-16__radio:checked + .nn-16__opt {
  color: var(--nn-16-ink);
  border-color: var(--nn-16-base);
  box-shadow: 0 0 .3rem var(--nn-16-core), 0 0 1rem var(--nn-16-halo);
}

.nn-16__radio:focus-visible + .nn-16__opt {
  outline: 2px solid var(--nn-16-ink);
  outline-offset: 2px;
}

.nn-16__set {
  display: grid;
  gap: 1rem;
  grid-template-columns: 1fr;
  align-items: start;
}

@media (min-width: 54rem) {
  .nn-16__set {
    grid-template-columns: minmax(0, 22rem) minmax(0, 1fr);
  }
}

.nn-16__card {
  display: grid;
  gap: .6rem;
  justify-items: start;
  padding: clamp(1rem, 3.5vw, 1.35rem);
  border: 1px solid var(--nn-16-edge);
  border-radius: .6rem;
  background: var(--nn-16-panel);
  box-shadow: 0 0 .3rem var(--nn-16-core), 0 0 1.1rem var(--nn-16-halo), 0 0 clamp(1.75rem, 8vw, 3rem) var(--nn-16-bloom);
}

.nn-16__badge {
  margin: 0;
  padding: .2rem .5rem;
  border-radius: 999px;
  border: 1px solid var(--nn-16-base);
  color: var(--nn-16-base);
  font-size: .66rem;
  font-weight: 650;
  letter-spacing: .12em;
  text-transform: uppercase;
  box-shadow: 0 0 .3rem var(--nn-16-halo);
}

.nn-16__ctitle {
  margin: 0;
  font-family: var(--nn-16-font-display);
  font-size: 1.05rem;
  font-weight: 640;
  letter-spacing: -.02em;
}

.nn-16__cbody {
  margin: 0;
  font-size: .84rem;
  line-height: 1.55;
  color: var(--nn-16-muted);
  text-wrap: pretty;
}

.nn-16__meter {
  width: 100%;
  height: .4rem;
  border-radius: 999px;
  background: color-mix(in srgb, var(--nn-16-line) 70%, transparent);
  overflow: hidden;
}

.nn-16__fill {
  display: block;
  width: 68%;
  height: 100%;
  background: var(--nn-16-base);
  box-shadow: 0 0 .35rem var(--nn-16-core), 0 0 .9rem var(--nn-16-halo);
}

.nn-16__btn {
  min-height: 44px;
  padding: 0 1rem;
  border: 1px solid var(--nn-16-base);
  border-radius: .35rem;
  background: color-mix(in srgb, var(--nn-16-base) 14%, transparent);
  color: var(--nn-16-ink);
  font-family: inherit;
  font-size: .84rem;
  font-weight: 550;
  cursor: pointer;
  box-shadow: 0 0 .3rem var(--nn-16-core), 0 0 1rem var(--nn-16-halo);
}

.nn-16__btn:hover {
  background: color-mix(in srgb, var(--nn-16-base) 22%, transparent);
}

.nn-16__btn:focus-visible {
  outline: 2px solid var(--nn-16-ink);
  outline-offset: 2px;
}

.nn-16__tokens {
  width: 100%;
  border-collapse: collapse;
  font-size: .78rem;
  min-inline-size: 0;
}

.nn-16__caption {
  padding-bottom: .5rem;
  text-align: left;
  font-size: .68rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--nn-16-muted);
}

.nn-16__tokens th,
.nn-16__tokens td {
  padding: .5rem .5rem;
  text-align: left;
  border-bottom: 1px solid var(--nn-16-line);
}

.nn-16__tokens thead th {
  font-size: .66rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--nn-16-muted);
  font-weight: 400;
}

.nn-16__tokens tbody th {
  font-family: ui-monospace, Menlo, monospace;
  font-size: .72rem;
  font-weight: 400;
  color: var(--nn-16-base);
}

.nn-16__tokens td {
  font-family: ui-monospace, Menlo, monospace;
  font-size: .72rem;
  color: var(--nn-16-muted);
}
```
