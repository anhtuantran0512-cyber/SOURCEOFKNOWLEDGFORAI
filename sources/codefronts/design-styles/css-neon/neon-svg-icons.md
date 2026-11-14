---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-neon/neon-svg-icons/"
title: "Neon Icon Glow with SVG Filters"
section: "design-styles"
category: "css-neon"
category_name: "CSS Neon Effects"
description: "Demo 06's technique applied at component scale: an icon set lit by one shared SVG <filter>, defined once and referenced by every glyph."
has_js: "false"
---

Here's a working CSS Neon Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neon Icon Glow with SVG Filters
Source: https://codefronts.com/design-styles/css-neon/neon-svg-icons/

Demo 06's technique applied at component scale: an icon set lit by one shared SVG <filter>, defined once and referenced by every glyph. Covers the two things that bite at set scale &mdash; a filter id that has to be unique across the whole document, and the per-icon cost of a filter that is cheap on one glyph and expensive on twenty.
## HTML
```html
<section class="nn-18" aria-labelledby="nn-18-heading">
  <div class="nn-18__stage">
    <div class="nn-18__theme">
      <input class="nn-18__tin" type="checkbox" id="nn-18-theme">
      <label class="nn-18__tlab" for="nn-18-theme">
        <svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M8 1.5v2M8 12.5v2M1.5 8h2M12.5 8h2M3.4 3.4l1.4 1.4M11.2 11.2l1.4 1.4M12.6 3.4l-1.4 1.4M4.8 11.2l-1.4 1.4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"></path><circle cx="8" cy="8" r="2.6" fill="none" stroke="currentColor" stroke-width="1.5"></circle></svg>
        Flip light / dark
      </label>
    </div>
    <header class="nn-18__head">
      <p class="nn-18__kicker">One filter, eight glyphs</p>
      <h2 class="nn-18__heading" id="nn-18-heading">A lit icon set from a single shared filter</h2>
      <p class="nn-18__sub">The filter is defined once and referenced by every icon. Its id is namespaced, because filter ids are document-global.</p>
    </header>

    <svg class="nn-18__defs" width="0" height="0" aria-hidden="true" focusable="false">
      <defs>
        <filter id="nn-18-glow" x="-60%" y="-60%" width="220%" height="220%">
          <feGaussianBlur in="SourceGraphic" stdDeviation="1.1" result="nn18core"></feGaussianBlur>
          <feGaussianBlur in="SourceGraphic" stdDeviation="3.4" result="nn18halo"></feGaussianBlur>
          <feMerge>
            <feMergeNode in="nn18halo"></feMergeNode>
            <feMergeNode in="nn18halo"></feMergeNode>
            <feMergeNode in="nn18core"></feMergeNode>
            <feMergeNode in="SourceGraphic"></feMergeNode>
          </feMerge>
        </filter>
      </defs>
    </svg>

    <ul class="nn-18__grid">
      <li class="nn-18__cell">
        <svg class="nn-18__icon" viewBox="0 0 24 24" role="img" aria-label="Power"><g filter="url(#nn-18-glow)"><path d="M13 2 5 14h6l-1 8 8-12h-6z" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linejoin="round"></path></g></svg>
        <p class="nn-18__label">Power</p>
      </li>
      <li class="nn-18__cell">
        <svg class="nn-18__icon" viewBox="0 0 24 24" role="img" aria-label="Terminal"><g filter="url(#nn-18-glow)"><path d="M3 4h18v16H3z M7 10l3 2-3 2 M13 14h4" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"></path></g></svg>
        <p class="nn-18__label">Terminal</p>
      </li>
      <li class="nn-18__cell">
        <svg class="nn-18__icon" viewBox="0 0 24 24" role="img" aria-label="Deploy"><g filter="url(#nn-18-glow)"><path d="M12 3v12 M8 7l4-4 4 4 M4 17v3h16v-3" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"></path></g></svg>
        <p class="nn-18__label">Deploy</p>
      </li>
      <li class="nn-18__cell">
        <svg class="nn-18__icon" viewBox="0 0 24 24" role="img" aria-label="Secrets"><g filter="url(#nn-18-glow)"><path d="M6 11h12v9H6z M9 11V8a3 3 0 0 1 6 0v3" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linejoin="round"></path></g></svg>
        <p class="nn-18__label">Secrets</p>
      </li>
      <li class="nn-18__cell">
        <svg class="nn-18__icon" viewBox="0 0 24 24" role="img" aria-label="Alerts"><g filter="url(#nn-18-glow)"><path d="M6 16V10a6 6 0 0 1 12 0v6l2 3H4z M10 21h4" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"></path></g></svg>
        <p class="nn-18__label">Alerts</p>
      </li>
      <li class="nn-18__cell">
        <svg class="nn-18__icon" viewBox="0 0 24 24" role="img" aria-label="Regions"><g filter="url(#nn-18-glow)"><path d="M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18z M3 12h18 M12 3c3 3.5 3 14 0 18" fill="none" stroke="currentColor" stroke-width="1.75"></path></g></svg>
        <p class="nn-18__label">Regions</p>
      </li>
      <li class="nn-18__cell">
        <svg class="nn-18__icon" viewBox="0 0 24 24" role="img" aria-label="Metrics"><g filter="url(#nn-18-glow)"><path d="M4 19V9 M10 19V4 M16 19v-7 M22 19H2" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round"></path></g></svg>
        <p class="nn-18__label">Metrics</p>
      </li>
      <li class="nn-18__cell">
        <svg class="nn-18__icon" viewBox="0 0 24 24" role="img" aria-label="Channels"><g filter="url(#nn-18-glow)"><path d="M4 6h16 M4 12h10 M4 18h13" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round"></path></g></svg>
        <p class="nn-18__label">Channels</p>
      </li>
    </ul>

    <p class="nn-18__rule">Filter ids have no scope. Two components defining the same id on one page means the later one wins and the earlier set renders unlit &mdash; which is why every id here starts with the demo prefix.</p>
  </div>
</section>
```
## CSS
```css
.nn-18 {
  --nn-18-bad: #f4a4a4;
  --nn-18-warn: #f0c88a;
  --nn-18-spec-neon: #b6f24a;
}

@media (prefers-color-scheme: light) {
  .nn-18 {
    --nn-18-bad: #a12a20;
    --nn-18-warn: #78490a;
  }

  .nn-18:has(#nn-18-theme:checked) {
    --nn-18-bad: #f4a4a4;
    --nn-18-warn: #f0c88a;
  }
}

@media (prefers-color-scheme: dark) {
  .nn-18:has(#nn-18-theme:checked) {
    --nn-18-bad: #a12a20;
    --nn-18-warn: #78490a;
  }
}

.nn-18[data-theme="light"] {
  --nn-18-bad: #a12a20;
  --nn-18-warn: #78490a;
}

.nn-18 {
  --nn-18-spec-ink: #eff5e4;
  --nn-18-spec-dim: #99a483;
}

.nn-18__theme {
  position: absolute;
  inset-block-start: clamp(10px, 2vw, 18px);
  inset-inline-end: clamp(10px, 2vw, 18px);
  z-index: 5;
  display: flex;
  justify-content: flex-end;
}

.nn-18__tin {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.nn-18__tlab {
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

.nn-18__tlab svg {
  width: .9rem;
  height: .9rem;
  flex: none;
}

.nn-18__tlab:hover {
  opacity: 1;
}

.nn-18__tin:focus-visible + .nn-18__tlab {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

@media (prefers-color-scheme: light) {
  .nn-18:has(#nn-18-theme:checked) {
    --nn-18-bg: #0d1008;
    --nn-18-panel: #12160b;
    --nn-18-line: #262d16;
    --nn-18-ink: #eff5e4;
    --nn-18-muted: #99a483;
    --nn-18-neon: #b6f24a;
  }
}

@media (prefers-color-scheme: dark) {
  .nn-18:has(#nn-18-theme:checked) {
    --nn-18-bg: #ecefe4;
    --nn-18-panel: #ffffff;
    --nn-18-line: #c9cdba;
    --nn-18-ink: #101408;
    --nn-18-muted: #4d5340;
    --nn-18-neon: #3f6b06;
  }
}

.nn-18 {
  --nn-18-hue: 130;
  --nn-18-bg: #0d1008;
  --nn-18-panel: #12160b;
  --nn-18-line: #262d16;
  --nn-18-ink: #eff5e4;
  --nn-18-muted: #99a483;
  --nn-18-neon: #b6f24a;
  --nn-18-font-display: "Gill Sans", "Trebuchet MS", Optima, system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  position: relative;
  display: block;
  box-sizing: border-box;
  background: var(--nn-18-bg);
  color: var(--nn-18-ink);
  font-family: system-ui, sans-serif;
}

.nn-18 *,
.nn-18 *::before,
.nn-18 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(50% 0.1 200)) {
  .nn-18 {
    --nn-18-bg: oklch(15% 0.025 125);
    --nn-18-panel: oklch(19% 0.03 125);
    --nn-18-line: oklch(29% 0.035 125);
    --nn-18-ink: oklch(96% 0.016 125);
    --nn-18-muted: oklch(72% 0.028 125);
    --nn-18-neon: oklch(88% 0.19 var(--nn-18-hue));
  }
}

@media (prefers-color-scheme: light) {
  .nn-18 {
    --nn-18-bg: #ecefe4;
    --nn-18-panel: #ffffff;
    --nn-18-line: #c9cdba;
    --nn-18-ink: #101408;
    --nn-18-muted: #4d5340;
    --nn-18-neon: #3f6b06;
  }
}

.nn-18[data-theme="light"] {
  --nn-18-bg: #ecefe4;
  --nn-18-panel: #ffffff;
  --nn-18-line: #c9cdba;
  --nn-18-ink: #101408;
  --nn-18-muted: #4d5340;
  --nn-18-neon: #3f6b06;
}

.nn-18[data-theme="dark"] {
  --nn-18-bad: #f4a4a4;
  --nn-18-warn: #f0c88a;
  --nn-18-bg: #0d1008;
  --nn-18-panel: #12160b;
  --nn-18-line: #262d16;
  --nn-18-ink: #eff5e4;
  --nn-18-muted: #99a483;
  --nn-18-neon: #b6f24a;
}

.nn-18__stage {
  max-width: 62rem;
  margin: 0 auto;
  padding: clamp(1rem, 3vw, 1.35rem) clamp(.75rem, 3vw, 1.35rem) clamp(1.5rem, 4vw, 1.85rem);
  display: grid;
  gap: clamp(.85rem, 2.5vw, 1.1rem);
}

.nn-18__kicker {
  margin: 0 0 .3rem;
  font-family: var(--nn-18-font-display);
  font-size: .74rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--nn-18-neon);
}

.nn-18__heading {
  margin: 0;
  font-family: var(--nn-18-font-display);
  font-size: clamp(1.25rem, 4.4vw, 1.8rem);
  font-weight: 500;
  text-wrap: balance;
}

.nn-18__sub {
  margin: .4rem 0 0;
  max-width: 40rem;
  font-size: .86rem;
  line-height: 1.55;
  color: var(--nn-18-muted);
  text-wrap: pretty;
}

.nn-18__defs {
  position: absolute;
  width: 0;
  height: 0;
  overflow: hidden;
}

.nn-18__grid {
  margin: 0;
  padding: .5rem;
  list-style: none;
  display: grid;
  gap: .5rem;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 7rem), 1fr));
  border: 1px solid var(--nn-18-line);
  border-radius: .35rem;
  background: var(--nn-18-panel);
}

.nn-18__cell {
  display: grid;
  gap: .4rem;
  justify-items: center;
  padding: .8rem .5rem;
  border: 1px solid transparent;
  border-radius: .25rem;
  color: var(--nn-18-neon);
  min-inline-size: 0;
}

.nn-18__cell:hover {
  border-color: var(--nn-18-line);
  color: var(--nn-18-ink);
}

.nn-18__icon {
  width: clamp(1.9rem, 7vw, 2.4rem);
  height: auto;
  display: block;
  overflow: visible;
}

.nn-18__label {
  margin: 0;
  font-family: var(--nn-18-font-display);
  font-size: .74rem;
  letter-spacing: .04em;
  color: var(--nn-18-muted);
  text-align: center;
}

.nn-18__rule {
  margin: 0;
  padding: .85rem 1rem;
  border: 1px solid var(--nn-18-line);
  border-left: 2px solid var(--nn-18-neon);
  border-radius: .25rem;
  font-size: .82rem;
  line-height: 1.6;
  color: var(--nn-18-ink);
  text-wrap: pretty;
}
```
