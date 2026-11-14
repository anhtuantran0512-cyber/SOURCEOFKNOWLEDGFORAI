---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-neumorphism/neumorphism-css-dual-shadow-reference-build/"
title: "Neumorphism CSS Dual Shadow Reference Build"
section: "design-styles"
category: "css-neumorphism"
category_name: "CSS Neumorphism"
description: "The reference build every other demo in this collection borrows from."
has_js: "false"
---

Here's a working CSS Neumorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neumorphism CSS Dual Shadow Reference Build
Source: https://codefronts.com/design-styles/css-neumorphism/neumorphism-css-dual-shadow-reference-build/

The reference build every other demo in this collection borrows from. One surface, one box-shadow declaration, both halves labelled in place: the dark shadow offset away from the light, the light shadow offset toward it. An annotation panel names all six values, and a side panel shows the effect collapsing the moment the surface stops matching its parent's background — the single rule the technique cannot survive without.
## HTML
```html
<section class="nm-01" aria-labelledby="nm-01-heading">
      <input type="checkbox" id="nm-01-theme" class="nm-01__themeinput">
      <label for="nm-01-theme" class="nm-01__themebtn">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 3a9 9 0 1 0 9 9 7 7 0 0 1-9-9Z"/></svg>
        Theme
      </label>
  <div class="nm-01__stage">
    <header class="nm-01__head">
      <p class="nm-01__kicker">Reference build</p>
      <h2 class="nm-01__heading" id="nm-01-heading">One declaration, two shadows</h2>
      <p class="nm-01__sub">The dark half offsets away from the light source. The light half offsets toward it. Both colours come from the surface token.</p>
    </header>

    <div class="nm-01__grid">
      <div class="nm-01__diagram">
        <span class="nm-01__ray nm-01__ray--light" aria-hidden="true">
          <svg viewBox="0 0 40 40" width="26" height="26"><circle cx="20" cy="20" r="7" fill="none" stroke="currentColor" stroke-width="2"/><path d="M20 3v6M20 31v6M3 20h6M31 20h6M8 8l4 4M28 28l4 4M32 8l-4 4M12 28l-4 4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
          <em class="nm-01__raytext">Light source · top left</em>
        </span>

        <div class="nm-01__surface">
          <span class="nm-01__surfacelabel">Surface</span>
        </div>

        <p class="nm-01__callout nm-01__callout--light">Light shadow<br><code>-10px -10px 20px</code> lightened</p>
        <p class="nm-01__callout nm-01__callout--dark">Dark shadow<br><code>10px 10px 20px</code> darkened</p>
      </div>

      <div class="nm-01__panels">
        <article class="nm-01__panel">
          <h3 class="nm-01__ptitle">The six values, twice</h3>
          <ul class="nm-01__values">
            <li class="nm-01__value"><b>offset-x</b><span>10px / -10px</span></li>
            <li class="nm-01__value"><b>offset-y</b><span>10px / -10px</span></li>
            <li class="nm-01__value"><b>blur</b><span>20px both</span></li>
            <li class="nm-01__value"><b>spread</b><span>0 both</span></li>
            <li class="nm-01__value"><b>colour A</b><span>surface darkened 18%</span></li>
            <li class="nm-01__value"><b>colour B</b><span>surface lightened 85%</span></li>
          </ul>
          <code class="nm-01__code">box-shadow:<br>&nbsp;&nbsp;10px 10px 20px var(--dark),<br>&nbsp;&nbsp;-10px -10px 20px var(--light);</code>
        </article>

        <article class="nm-01__panel nm-01__panel--rule">
          <h3 class="nm-01__ptitle">The rule</h3>
          <p class="nm-01__note">The surface must be the same colour as its parent. Push it out of the page — do not place it on top.</p>
          <div class="nm-01__compare">
            <div class="nm-01__case">
              <div class="nm-01__chip nm-01__chip--ok"></div>
              <span class="nm-01__caselabel nm-01__caselabel--ok">Matches parent — reads as extruded</span>
            </div>
            <div class="nm-01__case">
              <div class="nm-01__chip nm-01__chip--bad"></div>
              <span class="nm-01__caselabel nm-01__caselabel--bad">5% lighter than parent — reads as a card</span>
            </div>
          </div>
        </article>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.nm-01 {
  position: relative;
  --nm-01-surface: #e0e5ec;
  --nm-01-dark: rgba(163,177,198,0.62);
  --nm-01-light: rgba(255,255,255,0.92);
  --nm-01-ink: #2c313a;
  --nm-01-muted: #6b7280;
  --nm-01-line: rgba(44,49,58,0.22);
  --nm-01-bad: #b4442f;
  --nm-01-good: #3f6f4b;
  --nm-01-distance: clamp(6px, 1.4vw, 11px);
  --nm-01-blur: clamp(12px, 2.8vw, 22px);
  --nm-01-radius: 22px;
  --nm-01-font-display: ui-monospace, "SFMono-Regular", "Cascadia Mono", Menlo, monospace;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--nm-01-surface);
  color: var(--nm-01-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(0.9 0.01 255)) {
  .nm-01 {
    --nm-01-surface: oklch(0.911 0.013 254);
    --nm-01-ink: oklch(0.31 0.018 262);
    --nm-01-muted: oklch(0.55 0.019 262);
  }
}

@supports (color: color-mix(in oklab, #fff, #000)) {
  .nm-01 {
    --nm-01-dark: color-mix(in oklab, var(--nm-01-surface), #000 22%);
    --nm-01-light: color-mix(in oklab, var(--nm-01-surface), #fff 88%);
  }
}

.nm-01 *,
.nm-01 *::before,
.nm-01 *::after {
  box-sizing: border-box;
}

.nm-01__stage {
  max-width: 1120px;
  margin: 0 auto;
  padding: clamp(24px, 5vw, 60px) clamp(16px, 4vw, 48px);
  display: flex;
  flex-direction: column;
  gap: clamp(24px, 4vw, 44px);
  justify-content: center;
  min-height: 100vh;
}

.nm-01__head {
  max-width: 60ch;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.nm-01__kicker {
  margin: 0;
  font-family: var(--nm-01-font-display);
  font-size: 0.72rem;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--nm-01-muted);
}

.nm-01__heading {
  margin: 0;
  font-family: var(--nm-01-font-display);
  font-size: clamp(1.5rem, 4.2vw, 2.3rem);
  font-weight: 600;
  letter-spacing: -0.02em;
  line-height: 1.14;
  text-wrap: balance;
}

.nm-01__sub {
  margin: 0;
  font-size: 0.95rem;
  line-height: 1.6;
  color: var(--nm-01-muted);
  text-wrap: pretty;
}

.nm-01__grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: clamp(28px, 5vw, 48px);
  align-items: center;
}

@media (min-width: 900px) {
  .nm-01__grid {
    grid-template-columns: minmax(0, 1.05fr) minmax(0, 1fr);
  }
}

.nm-01__diagram {
  position: relative;
  display: grid;
  place-items: center;
  padding: clamp(38px, 8vw, 64px) 0;
  min-inline-size: 0;
}

.nm-01__ray {
  position: absolute;
  top: 0;
  left: 0;
  display: flex;
  align-items: center;
  gap: 8px;
  color: var(--nm-01-muted);
}

.nm-01__raytext {
  font-family: var(--nm-01-font-display);
  font-size: 0.68rem;
  font-style: normal;
  letter-spacing: 0.06em;
}

.nm-01__surface {
  width: clamp(150px, 40vw, 220px);
  aspect-ratio: 1;
  border-radius: var(--nm-01-radius);
  background: var(--nm-01-surface);
  border: 1px solid transparent;
  display: grid;
  place-items: center;
  box-shadow: var(--nm-01-distance) var(--nm-01-distance) var(--nm-01-blur) var(--nm-01-dark), calc(var(--nm-01-distance) * -1) calc(var(--nm-01-distance) * -1) var(--nm-01-blur) var(--nm-01-light);
}

.nm-01__surfacelabel {
  font-family: var(--nm-01-font-display);
  font-size: 0.7rem;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--nm-01-muted);
}

.nm-01__callout {
  position: absolute;
  margin: 0;
  font-size: 0.72rem;
  line-height: 1.45;
  color: var(--nm-01-muted);
  max-width: 15ch;
}

.nm-01__callout code {
  font-family: var(--nm-01-font-display);
  font-size: 0.68rem;
  color: var(--nm-01-ink);
}

.nm-01__callout--light {
  top: 8%;
  right: 2%;
  text-align: right;
}

.nm-01__callout--dark {
  bottom: 8%;
  left: 2%;
}

.nm-01__panels {
  display: flex;
  flex-direction: column;
  gap: clamp(16px, 2.6vw, 24px);
  min-inline-size: 0;
}

.nm-01__panel {
  background: var(--nm-01-surface);
  border-radius: 18px;
  padding: clamp(18px, 3vw, 26px);
  border: 1px solid transparent;
  box-shadow: calc(var(--nm-01-distance) * 0.7) calc(var(--nm-01-distance) * 0.7) calc(var(--nm-01-blur) * 0.8) var(--nm-01-dark), calc(var(--nm-01-distance) * -0.7) calc(var(--nm-01-distance) * -0.7) calc(var(--nm-01-blur) * 0.8) var(--nm-01-light);
}

.nm-01__ptitle {
  margin: 0 0 12px;
  font-family: var(--nm-01-font-display);
  font-size: 0.78rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  font-weight: 600;
}

.nm-01__values {
  list-style: none;
  margin: 0 0 16px;
  padding: 0;
  display: grid;
  gap: 6px;
}

.nm-01__value {
  display: flex;
  justify-content: space-between;
  gap: 12px;
  font-size: 0.78rem;
  min-inline-size: 0;
}

.nm-01__value b {
  font-family: var(--nm-01-font-display);
  font-weight: 600;
}

.nm-01__value span {
  color: var(--nm-01-muted);
  text-align: right;
  min-inline-size: 0;
}

.nm-01__code {
  display: block;
  font-family: var(--nm-01-font-display);
  font-size: 0.72rem;
  line-height: 1.7;
  color: var(--nm-01-ink);
  padding: 14px 16px;
  border-radius: 12px;
  border: 1px solid var(--nm-01-line);
  background: var(--nm-01-surface);
  box-shadow: inset 3px 3px 7px var(--nm-01-dark), inset -3px -3px 7px var(--nm-01-light);
  overflow-wrap: anywhere;
}

.nm-01__note {
  margin: 0 0 16px;
  font-size: 0.85rem;
  line-height: 1.6;
  color: var(--nm-01-muted);
  text-wrap: pretty;
}

.nm-01__compare {
  display: grid;
  grid-template-columns: 1fr;
  gap: 14px;
}

@media (min-width: 420px) {
  .nm-01__compare {
    grid-template-columns: 1fr 1fr;
  }
}

.nm-01__case {
  display: flex;
  flex-direction: column;
  gap: 10px;
  align-items: flex-start;
  min-inline-size: 0;
}

.nm-01__chip {
  width: 100%;
  height: 62px;
  border-radius: 14px;
  border: 1px solid transparent;
  box-shadow: calc(var(--nm-01-distance) * 0.6) calc(var(--nm-01-distance) * 0.6) calc(var(--nm-01-blur) * 0.6) var(--nm-01-dark), calc(var(--nm-01-distance) * -0.6) calc(var(--nm-01-distance) * -0.6) calc(var(--nm-01-blur) * 0.6) var(--nm-01-light);
}

.nm-01__chip--ok {
  background: var(--nm-01-surface);
}

.nm-01__chip--bad {
  background: #eef1f6;
}

@supports (color: color-mix(in oklab, #fff, #000)) {
  .nm-01__chip--bad {
    background: color-mix(in oklab, var(--nm-01-surface), #fff 45%);
  }
}

.nm-01__caselabel {
  font-size: 0.72rem;
  line-height: 1.45;
  font-weight: 500;
}

.nm-01__caselabel--ok {
  color: var(--nm-01-good);
}

.nm-01__caselabel--bad {
  color: var(--nm-01-bad);
}

@media (prefers-color-scheme: dark) {
  .nm-01 {
    --nm-01-surface: #2a2f38;
    --nm-01-dark: rgba(12,14,18,0.72);
    --nm-01-light: rgba(86,94,108,0.5);
    --nm-01-ink: #dfe3ea;
    --nm-01-muted: #99a1af;
    --nm-01-line: rgba(223,227,234,0.22);
    --nm-01-bad: #e0836c;
    --nm-01-good: #86c096;
  }

  @supports (color: color-mix(in oklab, #fff, #000)) {
    .nm-01 {
      --nm-01-dark: color-mix(in oklab, var(--nm-01-surface), #000 55%);
      --nm-01-light: color-mix(in oklab, var(--nm-01-surface), #fff 16%);
    }
  }

  .nm-01__chip--bad {
    background: #363c47;
  }
}

.nm-01[data-theme="dark"] {
  --nm-01-surface: #2a2f38;
  --nm-01-dark: rgba(12,14,18,0.72);
  --nm-01-light: rgba(86,94,108,0.5);
  --nm-01-ink: #dfe3ea;
  --nm-01-muted: #99a1af;
  --nm-01-line: rgba(223,227,234,0.22);
  --nm-01-bad: #e0836c;
  --nm-01-good: #86c096;
}

@supports (color: color-mix(in oklab, #fff, #000)) {
  .nm-01[data-theme="dark"] {
    --nm-01-dark: color-mix(in oklab, var(--nm-01-surface), #000 55%);
    --nm-01-light: color-mix(in oklab, var(--nm-01-surface), #fff 16%);
  }
}

.nm-01[data-theme="dark"] .nm-01__chip--bad {
  background: #363c47;
}
/* Pure-CSS theme toggle. Mirrors the [data-theme="dark"] rules above so
   the demo's own dark palette is reachable from inside the demo. */

.nm-01__themeinput {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: 0;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.nm-01__themebtn {
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
  background: var(--nm-01-surface);
  color: var(--nm-01-ink);
  border: 1px solid var(--nm-01-line);
  font: 600 11px/1 var(--nm-01-font-display, system-ui);
  letter-spacing: 0.12em;
  text-transform: uppercase;
  cursor: pointer;
  box-shadow: var(--nm-01-distance, 6px) var(--nm-01-distance, 6px) var(--nm-01-blur, 14px) var(--nm-01-dark), calc(-1 * var(--nm-01-distance, 6px)) calc(-1 * var(--nm-01-distance, 6px)) var(--nm-01-blur, 14px) var(--nm-01-light);
  transition: box-shadow 180ms ease, color 180ms ease;
}

.nm-01__themebtn:hover {
  color: var(--nm-01-ink);
}

.nm-01__themeinput:focus-visible + .nm-01__themebtn {
  outline: 2px solid var(--nm-01-ink);
  outline-offset: 3px;
}

.nm-01:has(#nm-01-theme:checked) .nm-01__themebtn {
  box-shadow: inset var(--nm-01-distance, 6px) var(--nm-01-distance, 6px) var(--nm-01-blur, 14px) var(--nm-01-dark), inset calc(-1 * var(--nm-01-distance, 6px)) calc(-1 * var(--nm-01-distance, 6px)) var(--nm-01-blur, 14px) var(--nm-01-light);
}

.nm-01__themebtn svg {
  inline-size: 13px;
  block-size: 13px;
  flex: none;
}

.nm-01:has(#nm-01-theme:checked) {
  --nm-01-surface: #2a2f38;
  --nm-01-dark: rgba(12,14,18,0.72);
  --nm-01-light: rgba(86,94,108,0.5);
  --nm-01-ink: #dfe3ea;
  --nm-01-muted: #99a1af;
  --nm-01-line: rgba(223,227,234,0.22);
  --nm-01-bad: #e0836c;
  --nm-01-good: #86c096;
}

@media (prefers-color-scheme: light) {
  .nm-01:has(#nm-01-theme:checked) {
    --nm-01-surface: #2a2f38;
    --nm-01-dark: rgba(12,14,18,0.72);
    --nm-01-light: rgba(86,94,108,0.5);
    --nm-01-ink: #dfe3ea;
    --nm-01-muted: #99a1af;
    --nm-01-line: rgba(223,227,234,0.22);
    --nm-01-bad: #e0836c;
    --nm-01-good: #86c096;
  }
}

@media (prefers-color-scheme: dark) {
  /* Base already resolves dark here, so :checked restores light —
       without this the toggle is inert for dark-OS visitors. */

  .nm-01:has(#nm-01-theme:checked) {
    --nm-01-surface: #e0e5ec;
    --nm-01-dark: rgba(163,177,198,0.62);
    --nm-01-light: rgba(255,255,255,0.92);
    --nm-01-ink: #2c313a;
    --nm-01-muted: #6b7280;
    --nm-01-line: rgba(44,49,58,0.22);
    --nm-01-bad: #b4442f;
    --nm-01-good: #3f6f4b;
  }
}

@media (prefers-reduced-motion: reduce) {
  .nm-01__themebtn {
    transition: none;
  }
}
```
