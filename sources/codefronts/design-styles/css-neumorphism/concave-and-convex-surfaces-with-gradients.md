---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-neumorphism/concave-and-convex-surfaces-with-gradients/"
title: "Concave and Convex Surfaces with Gradients"
section: "design-styles"
category: "css-neumorphism"
category_name: "CSS Neumorphism"
description: "The fourth axis of soft UI after raised, inset and flat: surface curvature."
has_js: "false"
---

Here's a working CSS Neumorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Concave and Convex Surfaces with Gradients
Source: https://codefronts.com/design-styles/css-neumorphism/concave-and-convex-surfaces-with-gradients/

The fourth axis of soft UI after raised, inset and flat: surface curvature. A barely-there linear-gradient at the same angle as the light source makes a surface read as bulging toward you or dished away from you, without touching the shadow pair. Four tiles — flat, convex, concave, and pressure-dished — with their gradient stops printed underneath, plus the angle rule that keeps curvature and lighting consistent.
## HTML
```html
<section class="nm-07" aria-labelledby="nm-07-heading">
      <input type="checkbox" id="nm-07-theme" class="nm-07__themeinput">
      <label for="nm-07-theme" class="nm-07__themebtn">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 3a9 9 0 1 0 9 9 7 7 0 0 1-9-9Z"/></svg>
        Theme
      </label>
  <div class="nm-07__stage">
    <header class="nm-07__head">
      <p class="nm-07__kicker">Curvature</p>
      <h2 class="nm-07__heading" id="nm-07-heading">Flat, convex, concave, dished</h2>
      <p class="nm-07__sub">A six-percent gradient at the light angle. Same shadow pair on all four tiles — only the surface curves.</p>
    </header>

    <div class="nm-07__grid">
      <figure class="nm-07__cell">
        <div class="nm-07__tile nm-07__tile--flat"></div>
        <figcaption class="nm-07__cap"><b>Flat</b><span>no gradient · the default</span></figcaption>
      </figure>
      <figure class="nm-07__cell">
        <div class="nm-07__tile nm-07__tile--convex"></div>
        <figcaption class="nm-07__cap"><b>Convex</b><span>light → dark along 145deg</span></figcaption>
      </figure>
      <figure class="nm-07__cell">
        <div class="nm-07__tile nm-07__tile--concave"></div>
        <figcaption class="nm-07__cap"><b>Concave</b><span>dark → light along 145deg</span></figcaption>
      </figure>
      <figure class="nm-07__cell">
        <div class="nm-07__tile nm-07__tile--dish"></div>
        <figcaption class="nm-07__cap"><b>Pressure dish</b><span>concave gradient + inset pair</span></figcaption>
      </figure>
    </div>

    <div class="nm-07__applied">
      <div class="nm-07__player">
        <div class="nm-07__display">
          <p class="nm-07__track">Sonatine, third movement</p>
          <p class="nm-07__artist">Meridian Quartet · 4:12</p>
        </div>
        <div class="nm-07__controls">
          <button class="nm-07__knob" type="button" aria-label="Rewind"><svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path d="M11 6 4 12l7 6V6zM20 6l-7 6 7 6V6z" fill="currentColor"/></svg></button>
          <button class="nm-07__knob nm-07__knob--big" type="button" aria-label="Play"><svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path d="M8 5.5 19 12 8 18.5v-13z" fill="currentColor"/></svg></button>
          <button class="nm-07__knob" type="button" aria-label="Forward"><svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path d="M13 6l7 6-7 6V6zM4 6l7 6-7 6V6z" fill="currentColor"/></svg></button>
        </div>
      </div>
      <p class="nm-07__note">The display is a pressure dish, the transport buttons are convex. Concave holds content, convex invites a press — that division is most of what curvature is for.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.nm-07 {
  position: relative;
  --nm-07-surface: #e6e2dd;
  --nm-07-hi: #f0ede9;
  --nm-07-lo: #d9d4ce;
  --nm-07-dark: rgba(176,169,160,0.66);
  --nm-07-light: rgba(255,255,255,0.92);
  --nm-07-ink: #2c2925;
  --nm-07-muted: #635d55;
  --nm-07-border: #a49c92;
  --nm-07-accent: #8a5a3c;
  --nm-07-angle: 145deg;
  --nm-07-dist: clamp(7px, 1.5vw, 11px);
  --nm-07-blur: clamp(14px, 3vw, 22px);
  --nm-07-font-display: "Palatino Linotype", "Book Antiqua", Palatino, Georgia, serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--nm-07-surface);
  color: var(--nm-07-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

@supports (color: oklch(0.9 0.01 70)) {
  .nm-07 {
    --nm-07-surface: oklch(0.907 0.008 72);
    --nm-07-ink: oklch(0.28 0.011 66);
    --nm-07-muted: oklch(0.47 0.014 68);
    --nm-07-accent: oklch(0.48 0.075 52);
  }
}

@supports (color: color-mix(in oklab, #fff, #000)) {
  .nm-07 {
    --nm-07-dark: color-mix(in oklab, var(--nm-07-surface), #000 20%);
    --nm-07-light: color-mix(in oklab, var(--nm-07-surface), #fff 90%);
    --nm-07-hi: color-mix(in oklab, var(--nm-07-surface), #fff 26%);
    --nm-07-lo: color-mix(in oklab, var(--nm-07-surface), #000 6%);
    --nm-07-border: color-mix(in oklab, var(--nm-07-surface), var(--nm-07-ink) 34%);
  }
}

.nm-07 *,
.nm-07 *::before,
.nm-07 *::after {
  box-sizing: border-box;
}

.nm-07__stage {
  max-width: 1020px;
  margin: 0 auto;
  min-height: 100vh;
  padding: clamp(26px, 5vw, 58px) clamp(16px, 4vw, 42px);
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: clamp(24px, 4vw, 40px);
}

.nm-07__head {
  max-width: 58ch;
  display: flex;
  flex-direction: column;
  gap: 9px;
}

.nm-07__kicker {
  margin: 0;
  font-size: 0.7rem;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--nm-07-muted);
}

.nm-07__heading {
  margin: 0;
  font-family: var(--nm-07-font-display);
  font-size: clamp(1.6rem, 4.4vw, 2.4rem);
  font-weight: 400;
  letter-spacing: -0.01em;
  line-height: 1.12;
  text-wrap: balance;
}

.nm-07__sub {
  margin: 0;
  font-size: 0.94rem;
  line-height: 1.6;
  color: var(--nm-07-muted);
  text-wrap: pretty;
}

.nm-07__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 168px), 1fr));
  gap: clamp(16px, 2.8vw, 24px);
}

.nm-07__cell {
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 12px;
  min-inline-size: 0;
}

.nm-07__tile {
  aspect-ratio: 1.3;
  border-radius: 20px;
  border: 1px solid var(--nm-07-border);
  background: var(--nm-07-surface);
  box-shadow: var(--nm-07-dist) var(--nm-07-dist) var(--nm-07-blur) var(--nm-07-dark), calc(var(--nm-07-dist) * -1) calc(var(--nm-07-dist) * -1) var(--nm-07-blur) var(--nm-07-light);
}

.nm-07__tile--convex {
  background: linear-gradient(var(--nm-07-angle), var(--nm-07-hi), var(--nm-07-lo));
}

.nm-07__tile--concave {
  background: linear-gradient(var(--nm-07-angle), var(--nm-07-lo), var(--nm-07-hi));
}

.nm-07__tile--dish {
  background: linear-gradient(var(--nm-07-angle), var(--nm-07-lo), var(--nm-07-hi));
  box-shadow: inset var(--nm-07-dist) var(--nm-07-dist) var(--nm-07-blur) var(--nm-07-dark), inset calc(var(--nm-07-dist) * -1) calc(var(--nm-07-dist) * -1) var(--nm-07-blur) var(--nm-07-light);
}

.nm-07__cap {
  display: flex;
  flex-direction: column;
  gap: 3px;
  min-inline-size: 0;
}

.nm-07__cap b {
  font-family: var(--nm-07-font-display);
  font-size: 0.95rem;
  font-weight: 600;
}

.nm-07__cap span {
  font-size: 0.74rem;
  line-height: 1.45;
  color: var(--nm-07-muted);
}

.nm-07__applied {
  display: grid;
  grid-template-columns: 1fr;
  gap: clamp(16px, 3vw, 26px);
  align-items: center;
}

@media (min-width: 720px) {
  .nm-07__applied {
    grid-template-columns: minmax(0, 1.15fr) minmax(0, 1fr);
  }
}

.nm-07__player {
  border-radius: 24px;
  padding: clamp(18px, 3vw, 26px);
  display: flex;
  flex-direction: column;
  gap: 18px;
  min-inline-size: 0;
  background: linear-gradient(var(--nm-07-angle), var(--nm-07-hi), var(--nm-07-lo));
  border: 1px solid var(--nm-07-border);
  box-shadow: var(--nm-07-dist) var(--nm-07-dist) var(--nm-07-blur) var(--nm-07-dark), calc(var(--nm-07-dist) * -1) calc(var(--nm-07-dist) * -1) var(--nm-07-blur) var(--nm-07-light);
}

.nm-07__display {
  border-radius: 16px;
  padding: 18px 20px;
  min-inline-size: 0;
  background: linear-gradient(var(--nm-07-angle), var(--nm-07-lo), var(--nm-07-hi));
  box-shadow: inset 6px 6px 12px var(--nm-07-dark), inset -6px -6px 12px var(--nm-07-light);
}

.nm-07__track {
  margin: 0 0 4px;
  font-family: var(--nm-07-font-display);
  font-size: 1.02rem;
}

.nm-07__artist {
  margin: 0;
  font-size: 0.78rem;
  color: var(--nm-07-muted);
}

.nm-07__controls {
  display: flex;
  gap: 14px;
  align-items: center;
  justify-content: center;
}

.nm-07__knob {
  width: 48px;
  height: 48px;
  display: grid;
  place-items: center;
  border-radius: 50%;
  border: 1px solid var(--nm-07-border);
  color: var(--nm-07-ink);
  cursor: pointer;
  background: linear-gradient(var(--nm-07-angle), var(--nm-07-hi), var(--nm-07-lo));
  box-shadow: 6px 6px 12px var(--nm-07-dark), -6px -6px 12px var(--nm-07-light);
  transition: box-shadow 160ms ease;
}

.nm-07__knob--big {
  width: 60px;
  height: 60px;
  color: var(--nm-07-accent);
}

.nm-07__knob:active {
  background: linear-gradient(var(--nm-07-angle), var(--nm-07-lo), var(--nm-07-hi));
  box-shadow: inset 5px 5px 10px var(--nm-07-dark), inset -5px -5px 10px var(--nm-07-light);
}

.nm-07__knob:focus-visible {
  outline: 2px solid var(--nm-07-accent);
  outline-offset: 3px;
}

.nm-07__note {
  margin: 0;
  font-size: 0.86rem;
  line-height: 1.62;
  color: var(--nm-07-muted);
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .nm-07__knob {
    transition: none;
  }
}

@media (prefers-color-scheme: dark) {
  .nm-07 {
    --nm-07-surface: #2e2b27;
    --nm-07-hi: #3a3630;
    --nm-07-lo: #272420;
    --nm-07-dark: rgba(13,12,10,0.7);
    --nm-07-light: rgba(96,90,82,0.44);
    --nm-07-ink: #ece7e0;
    --nm-07-muted: #a89f93;
    --nm-07-border: #857c71;
    --nm-07-accent: #d9a077;
  }

  @supports (color: color-mix(in oklab, #fff, #000)) {
    .nm-07 {
      --nm-07-dark: color-mix(in oklab, var(--nm-07-surface), #000 54%);
      --nm-07-light: color-mix(in oklab, var(--nm-07-surface), #fff 14%);
      --nm-07-hi: color-mix(in oklab, var(--nm-07-surface), #fff 8%);
      --nm-07-lo: color-mix(in oklab, var(--nm-07-surface), #000 12%);
    }
  }
}

.nm-07[data-theme="dark"] {
  --nm-07-surface: #2e2b27;
  --nm-07-hi: #3a3630;
  --nm-07-lo: #272420;
  --nm-07-dark: rgba(13,12,10,0.7);
  --nm-07-light: rgba(96,90,82,0.44);
  --nm-07-ink: #ece7e0;
  --nm-07-muted: #a89f93;
  --nm-07-border: #857c71;
  --nm-07-accent: #d9a077;
}

@supports (color: color-mix(in oklab, #fff, #000)) {
  .nm-07[data-theme="dark"] {
    --nm-07-dark: color-mix(in oklab, var(--nm-07-surface), #000 54%);
    --nm-07-light: color-mix(in oklab, var(--nm-07-surface), #fff 14%);
    --nm-07-hi: color-mix(in oklab, var(--nm-07-surface), #fff 8%);
    --nm-07-lo: color-mix(in oklab, var(--nm-07-surface), #000 12%);
  }
}
/* Pure-CSS theme toggle. Mirrors the [data-theme="dark"] rules above so
   the demo's own dark palette is reachable from inside the demo. */

.nm-07__themeinput {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: 0;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.nm-07__themebtn {
  position: absolute;
  inset-block-start: clamp(10px, 2vw, 18px);
  inset-inline-end: clamp(10px, 2vw, 18px);
  z-index: 5;
  display: inline-flex;
  align-items: center;
  gap: 7px;
  min-height: 44px;
  padding: 0 14px;
  border-radius: 999px;
  background: var(--nm-07-surface);
  color: var(--nm-07-ink);
  border: 1px solid var(--nm-07-line);
  font: 600 11px/1 var(--nm-07-font-display, system-ui);
  letter-spacing: 0.12em;
  text-transform: uppercase;
  cursor: pointer;
  box-shadow: var(--nm-07-distance, 6px) var(--nm-07-distance, 6px) var(--nm-07-blur, 14px) var(--nm-07-dark), calc(-1 * var(--nm-07-distance, 6px)) calc(-1 * var(--nm-07-distance, 6px)) var(--nm-07-blur, 14px) var(--nm-07-light);
  transition: box-shadow 180ms ease, color 180ms ease;
}

.nm-07__themebtn:hover {
  color: var(--nm-07-ink);
}

.nm-07__themeinput:focus-visible + .nm-07__themebtn {
  outline: 2px solid var(--nm-07-ink);
  outline-offset: 3px;
}

.nm-07:has(#nm-07-theme:checked) .nm-07__themebtn {
  box-shadow: inset var(--nm-07-distance, 6px) var(--nm-07-distance, 6px) var(--nm-07-blur, 14px) var(--nm-07-dark), inset calc(-1 * var(--nm-07-distance, 6px)) calc(-1 * var(--nm-07-distance, 6px)) var(--nm-07-blur, 14px) var(--nm-07-light);
}

.nm-07__themebtn svg {
  inline-size: 13px;
  block-size: 13px;
  flex: none;
}

.nm-07:has(#nm-07-theme:checked) {
  --nm-07-surface: #2e2b27;
  --nm-07-hi: #3a3630;
  --nm-07-lo: #272420;
  --nm-07-dark: rgba(13,12,10,0.7);
  --nm-07-light: rgba(96,90,82,0.44);
  --nm-07-ink: #ece7e0;
  --nm-07-muted: #a89f93;
  --nm-07-border: #857c71;
  --nm-07-accent: #d9a077;
}

@media (prefers-color-scheme: light) {
  .nm-07:has(#nm-07-theme:checked) {
    --nm-07-surface: #2e2b27;
    --nm-07-hi: #3a3630;
    --nm-07-lo: #272420;
    --nm-07-dark: rgba(13,12,10,0.7);
    --nm-07-light: rgba(96,90,82,0.44);
    --nm-07-ink: #ece7e0;
    --nm-07-muted: #a89f93;
    --nm-07-border: #857c71;
    --nm-07-accent: #d9a077;
  }
}

@media (prefers-color-scheme: dark) {
  /* Base already resolves dark here, so :checked restores light —
       without this the toggle is inert for dark-OS visitors. */

  .nm-07:has(#nm-07-theme:checked) {
    --nm-07-surface: #e6e2dd;
    --nm-07-hi: #f0ede9;
    --nm-07-lo: #d9d4ce;
    --nm-07-dark: rgba(176,169,160,0.66);
    --nm-07-light: rgba(255,255,255,0.92);
    --nm-07-ink: #2c2925;
    --nm-07-muted: #635d55;
    --nm-07-border: #a49c92;
    --nm-07-accent: #8a5a3c;
  }
}

@media (prefers-reduced-motion: reduce) {
  .nm-07__themebtn {
    transition: none;
  }
}
```
