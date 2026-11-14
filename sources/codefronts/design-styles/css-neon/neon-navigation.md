---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-neon/neon-navigation/"
title: "Neon Navigation with Active Glow State"
section: "design-styles"
category: "css-neon"
category_name: "CSS Neon Effects"
description: "A navigation bar where the current item glows &mdash; and where the glow is the third signal, not the only one."
has_js: "false"
---

Here's a working CSS Neon Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neon Navigation with Active Glow State
Source: https://codefronts.com/design-styles/css-neon/neon-navigation/

A navigation bar where the current item glows &mdash; and where the glow is the third signal, not the only one. aria-current drives a weight change, a solid indicator bar and the light together, so the current page is identifiable with the glow removed, in forced-colours mode, or by anyone who cannot separate the two hues.
## HTML
```html
<section class="nn-14" aria-labelledby="nn-14-heading">
  <div class="nn-14__stage">
    <div class="nn-14__theme">
      <input class="nn-14__tin" type="checkbox" id="nn-14-theme">
      <label class="nn-14__tlab" for="nn-14-theme">
        <svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M8 1.5v2M8 12.5v2M1.5 8h2M12.5 8h2M3.4 3.4l1.4 1.4M11.2 11.2l1.4 1.4M12.6 3.4l-1.4 1.4M4.8 11.2l-1.4 1.4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"></path><circle cx="8" cy="8" r="2.6" fill="none" stroke="currentColor" stroke-width="1.5"></circle></svg>
        Flip light / dark
      </label>
    </div>
    <header class="nn-14__head">
      <p class="nn-14__kicker">Three cues, one state</p>
      <h2 class="nn-14__heading" id="nn-14-heading">The current item glows, but the glow is not the signal</h2>
      <p class="nn-14__sub">Bar, weight, light &mdash; in that order of importance. Remove the light and the state is still obvious.</p>
    </header>

    <nav class="nn-14__bar" aria-label="Workspace sections">
      <ul class="nn-14__list">
        <li class="nn-14__item"><a class="nn-14__link" href="#nn-14-heading">Overview</a></li>
        <li class="nn-14__item"><a class="nn-14__link" href="#nn-14-heading" aria-current="page">Deployments</a></li>
        <li class="nn-14__item"><a class="nn-14__link" href="#nn-14-heading">Logs</a></li>
        <li class="nn-14__item"><a class="nn-14__link" href="#nn-14-heading">Repositories</a></li>
        <li class="nn-14__item"><a class="nn-14__link" href="#nn-14-heading">Settings</a></li>
      </ul>
    </nav>

    <div class="nn-14__panel">
      <p class="nn-14__ptitle">Deployments</p>
      <ul class="nn-14__rows">
        <li class="nn-14__row"><span class="nn-14__rname">orbit-api</span><span class="nn-14__rmeta">v2.3.1 &middot; 6 replicas healthy</span></li>
        <li class="nn-14__row"><span class="nn-14__rname">fern-worker</span><span class="nn-14__rmeta">v1.8.0 &middot; rolling 2 of 4</span></li>
        <li class="nn-14__row"><span class="nn-14__rname">quill-web</span><span class="nn-14__rmeta">v4.0.2 &middot; 3 replicas healthy</span></li>
      </ul>
    </div>

    <ol class="nn-14__cues">
      <li class="nn-14__cue"><span class="nn-14__cnum">1</span>Solid 2px bar &mdash; survives forced-colours mode</li>
      <li class="nn-14__cue"><span class="nn-14__cnum">2</span>Weight 650 vs 450 &mdash; needs no colour perception</li>
      <li class="nn-14__cue"><span class="nn-14__cnum">3</span>Glow &mdash; character only, safe to remove</li>
    </ol>
  </div>
</section>
```
## CSS
```css
.nn-14 {
  --nn-14-bad: #f4a4a4;
  --nn-14-warn: #f0c88a;
  --nn-14-spec-neon: #ffc247;
}

@media (prefers-color-scheme: light) {
  .nn-14 {
    --nn-14-bad: #a12a20;
    --nn-14-warn: #78490a;
  }

  .nn-14:has(#nn-14-theme:checked) {
    --nn-14-bad: #f4a4a4;
    --nn-14-warn: #f0c88a;
  }
}

@media (prefers-color-scheme: dark) {
  .nn-14:has(#nn-14-theme:checked) {
    --nn-14-bad: #a12a20;
    --nn-14-warn: #78490a;
  }
}

.nn-14[data-theme="light"] {
  --nn-14-bad: #a12a20;
  --nn-14-warn: #78490a;
}

.nn-14 {
  --nn-14-spec-ink: #ecf7f3;
  --nn-14-spec-dim: #8bada6;
}

.nn-14__theme {
  position: absolute;
  inset-block-start: clamp(10px, 2vw, 18px);
  inset-inline-end: clamp(10px, 2vw, 18px);
  z-index: 5;
  display: flex;
  justify-content: flex-end;
}

.nn-14__tin {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.nn-14__tlab {
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

.nn-14__tlab svg {
  width: .9rem;
  height: .9rem;
  flex: none;
}

.nn-14__tlab:hover {
  opacity: 1;
}

.nn-14__tin:focus-visible + .nn-14__tlab {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

@media (prefers-color-scheme: light) {
  .nn-14:has(#nn-14-theme:checked) {
    --nn-14-bg: #071412;
    --nn-14-panel: #0b1c19;
    --nn-14-line: #17332e;
    --nn-14-ink: #ecf7f3;
    --nn-14-muted: #8bada6;
    --nn-14-neon: #ffc247;
  }
}

@media (prefers-color-scheme: dark) {
  .nn-14:has(#nn-14-theme:checked) {
    --nn-14-bg: #e8efec;
    --nn-14-panel: #ffffff;
    --nn-14-line: #c4d0cc;
    --nn-14-ink: #0b1a17;
    --nn-14-muted: #47605a;
    --nn-14-neon: #7a4c00;
  }
}

.nn-14 {
  --nn-14-hue: 68;
  --nn-14-bg: #071412;
  --nn-14-panel: #0b1c19;
  --nn-14-line: #17332e;
  --nn-14-ink: #ecf7f3;
  --nn-14-muted: #8bada6;
  --nn-14-neon: #ffc247;
  --nn-14-core: rgba(255, 194, 71, .85);
  --nn-14-halo: rgba(255, 194, 71, .38);
  --nn-14-font-display: ui-rounded, "SF Pro Rounded", "Nunito", "Segoe UI", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  position: relative;
  display: block;
  box-sizing: border-box;
  background: var(--nn-14-bg);
  color: var(--nn-14-ink);
  font-family: system-ui, sans-serif;
}

.nn-14 *,
.nn-14 *::before,
.nn-14 *::after {
  box-sizing: border-box;
}

.nn-14 a {
  color: var(--nn-14-muted);
  text-decoration: none;
}

.nn-14 a:hover {
  color: var(--nn-14-ink);
}

@supports (color: oklch(50% 0.1 200)) {
  .nn-14 {
    --nn-14-bg: oklch(16.5% 0.024 178);
    --nn-14-panel: oklch(20.5% 0.03 178);
    --nn-14-line: oklch(30% 0.035 178);
    --nn-14-ink: oklch(96% 0.014 178);
    --nn-14-muted: oklch(73% 0.024 178);
    --nn-14-neon: oklch(86% 0.16 var(--nn-14-hue));
    --nn-14-core: oklch(86% 0.16 var(--nn-14-hue) / .85);
    --nn-14-halo: oklch(82% 0.15 var(--nn-14-hue) / .38);
  }
}

@media (prefers-color-scheme: light) {
  .nn-14 {
    --nn-14-bg: #e8efec;
    --nn-14-panel: #ffffff;
    --nn-14-line: #c4d0cc;
    --nn-14-ink: #0b1a17;
    --nn-14-muted: #47605a;
    --nn-14-neon: #7a4c00;
  }
}

.nn-14[data-theme="light"] {
  --nn-14-bg: #e8efec;
  --nn-14-panel: #ffffff;
  --nn-14-line: #c4d0cc;
  --nn-14-ink: #0b1a17;
  --nn-14-muted: #47605a;
  --nn-14-neon: #7a4c00;
}

.nn-14[data-theme="dark"] {
  --nn-14-bad: #f4a4a4;
  --nn-14-warn: #f0c88a;
  --nn-14-bg: #071412;
  --nn-14-panel: #0b1c19;
  --nn-14-line: #17332e;
  --nn-14-ink: #ecf7f3;
  --nn-14-muted: #8bada6;
  --nn-14-neon: #ffc247;
}

.nn-14__stage {
  /* minmax(0, 1fr) not the implicit auto track: an auto column is sized
       to its widest child's min-content, so one non-shrinking item (the
       horizontally-scrolling nav) pushed the whole grid to 465px and every
       sibling stretched to match, overflowing 320px viewports by 157px. */
  grid-template-columns: minmax(0, 1fr);
  max-width: 60rem;
  margin: 0 auto;
  padding: clamp(1rem, 3vw, 1.4rem) clamp(.75rem, 3vw, 1.4rem) clamp(1.5rem, 4vw, 1.9rem);
  display: grid;
  gap: clamp(.85rem, 2.5vw, 1.1rem);
}

.nn-14__kicker {
  margin: 0 0 .3rem;
  font-family: var(--nn-14-font-display);
  font-size: .72rem;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--nn-14-neon);
}

.nn-14__heading {
  margin: 0;
  font-family: var(--nn-14-font-display);
  font-size: clamp(1.2rem, 4.2vw, 1.75rem);
  font-weight: 700;
  letter-spacing: -.015em;
  text-wrap: balance;
}

.nn-14__sub {
  margin: .4rem 0 0;
  max-width: 40rem;
  font-size: .86rem;
  line-height: 1.55;
  color: var(--nn-14-muted);
  text-wrap: pretty;
}

.nn-14__bar {
  border-bottom: 1px solid var(--nn-14-line);
}

.nn-14__list {
  margin: 0;
  padding: 0;
  list-style: none;
  display: flex;
  gap: .25rem;
  overflow-x: auto;
  scroll-snap-type: inline mandatory;
  scrollbar-width: thin;
}

.nn-14__item {
  flex: none;
  scroll-snap-align: start;
  scroll-margin-inline: .5rem;
}

.nn-14__link {
  position: relative;
  display: flex;
  align-items: center;
  min-height: 44px;
  padding: 0 .85rem;
  font-family: var(--nn-14-font-display);
  font-size: .86rem;
  font-weight: 450;
  white-space: nowrap;
}

.nn-14__link::after {
  content: "";
  position: absolute;
  inset: auto .85rem 0 .85rem;
  height: 2px;
  background: transparent;
}

.nn-14__link:hover::after {
  background: color-mix(in srgb, var(--nn-14-muted) 55%, transparent);
}

.nn-14__link[aria-current="page"] {
  color: var(--nn-14-ink);
  font-weight: 650;
  text-shadow: 0 0 .35rem var(--nn-14-halo);
}

.nn-14__link[aria-current="page"]::after {
  background: var(--nn-14-neon);
  box-shadow: 0 0 .3rem var(--nn-14-core), 0 0 clamp(.7rem, 3vw, 1rem) var(--nn-14-halo);
}

.nn-14__link:focus-visible {
  outline: 2px solid var(--nn-14-ink);
  outline-offset: -2px;
  border-radius: .2rem;
}

.nn-14__panel {
  padding: clamp(.85rem, 3vw, 1.1rem);
  border: 1px solid var(--nn-14-line);
  border-radius: .6rem;
  background: var(--nn-14-panel);
}

.nn-14__ptitle {
  margin: 0 0 .6rem;
  font-family: var(--nn-14-font-display);
  font-size: .92rem;
  font-weight: 700;
}

.nn-14__rows {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: 0;
}

.nn-14__row {
  display: flex;
  justify-content: space-between;
  gap: 1rem;
  flex-wrap: wrap;
  padding: .5rem 0;
  border-top: 1px solid var(--nn-14-line);
  min-inline-size: 0;
}

.nn-14__rname {
  font-family: ui-monospace, Menlo, monospace;
  font-size: .8rem;
  color: var(--nn-14-ink);
}

.nn-14__rmeta {
  font-size: .78rem;
  color: var(--nn-14-muted);
  min-inline-size: 0;
}

.nn-14__cues {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: .4rem;
}

.nn-14__cue {
  display: flex;
  align-items: baseline;
  gap: .5rem;
  font-size: .8rem;
  color: var(--nn-14-muted);
  min-inline-size: 0;
}

.nn-14__cnum {
  flex: none;
  display: grid;
  place-items: center;
  width: 1.3rem;
  height: 1.3rem;
  border-radius: 999px;
  background: color-mix(in srgb, var(--nn-14-neon) 18%, transparent);
  color: var(--nn-14-neon);
  font-family: ui-monospace, Menlo, monospace;
  font-size: .68rem;
}
```
