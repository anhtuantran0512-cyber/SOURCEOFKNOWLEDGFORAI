---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-neumorphism/dark-mode-neumorphism/"
title: "Neumorphic Dark Mode Shadow Recalibration"
section: "design-styles"
category: "css-neumorphism"
category_name: "CSS Neumorphism"
description: "Dark neumorphism is not the light theme with inverted colours — the mix ratios have to change or the surface looks flat and grimy."
has_js: "false"
---

Here's a working CSS Neumorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neumorphic Dark Mode Shadow Recalibration
Source: https://codefronts.com/design-styles/css-neumorphism/dark-mode-neumorphism/

Dark neumorphism is not the light theme with inverted colours — the mix ratios have to change or the surface looks flat and grimy. Side-by-side cards show the naive inversion against a recalibrated pair, with the numbers: darker surfaces need a much heavier shadow and a much weaker highlight, because there is no headroom above the surface and plenty below it.
## HTML
```html
<section class="nm-16" aria-labelledby="nm-16-heading">
      <input type="checkbox" id="nm-16-theme" class="nm-16__themeinput">
      <label for="nm-16-theme" class="nm-16__themebtn">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 3a9 9 0 1 0 9 9 7 7 0 0 1-9-9Z"/></svg>
        Theme
      </label>
  <div class="nm-16__stage">
    <header class="nm-16__head">
      <p class="nm-16__kicker">Theming</p>
      <h2 class="nm-16__heading" id="nm-16-heading">Dark mode is not the light theme inverted</h2>
      <p class="nm-16__sub">Same geometry, different ratios. The highlight has to come down or the object glows instead of catching light.</p>
    </header>

    <div class="nm-16__compare">
      <div class="nm-16__side nm-16__side--light">
        <p class="nm-16__sidelabel">Light · 20% black / 90% white</p>
        <div class="nm-16__card">
          <p class="nm-16__cardtitle">Deployment</p>
          <p class="nm-16__cardvalue">18 <em>builds</em></p>
          <div class="nm-16__track"><span class="nm-16__fill" style="width:64%"></span></div>
        </div>
      </div>
      <div class="nm-16__side nm-16__side--dark">
        <p class="nm-16__sidelabel">Dark · 55% black / 14% white</p>
        <div class="nm-16__card">
          <p class="nm-16__cardtitle">Deployment</p>
          <p class="nm-16__cardvalue">18 <em>builds</em></p>
          <div class="nm-16__track"><span class="nm-16__fill" style="width:64%"></span></div>
        </div>
      </div>
      <div class="nm-16__side nm-16__side--naive">
        <p class="nm-16__sidelabel nm-16__sidelabel--warn">Naive inversion · 20% black / 90% white on dark</p>
        <div class="nm-16__card">
          <p class="nm-16__cardtitle">Deployment</p>
          <p class="nm-16__cardvalue">18 <em>builds</em></p>
          <div class="nm-16__track"><span class="nm-16__fill" style="width:64%"></span></div>
        </div>
      </div>
    </div>

    <dl class="nm-16__table">
      <div class="nm-16__trow"><dt>Surface lightness</dt><dd>L 0.91 light · L 0.28 dark — never below 0.22</dd></div>
      <div class="nm-16__trow"><dt>Dark shadow mix</dt><dd>20% black light · 55% black dark</dd></div>
      <div class="nm-16__trow"><dt>Light shadow mix</dt><dd>90% white light · 14% white dark</dd></div>
      <div class="nm-16__trow"><dt>Boundary border</dt><dd>33% toward ink light · 42% toward ink dark</dd></div>
    </dl>
  </div>
</section>
```
## CSS
```css
.nm-16 {
  position: relative;
  --nm-16-surface: #e8e8ea;
  --nm-16-dark: rgba(174,174,180,0.62);
  --nm-16-light: rgba(255,255,255,0.94);
  --nm-16-ink: #26262b;
  --nm-16-muted: #585862;
  --nm-16-border: #98989f;
  --nm-16-accent: #37697e;
  --nm-16-warn: #9c4a2e;
  --nm-16-font-display: "Space Grotesk", "Helvetica Neue", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--nm-16-surface);
  color: var(--nm-16-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

@supports (color: oklch(0.9 0.005 280)) {
  .nm-16 {
    --nm-16-surface: oklch(0.921 0.003 280);
    --nm-16-ink: oklch(0.26 0.01 285);
    --nm-16-muted: oklch(0.45 0.013 285);
    --nm-16-accent: oklch(0.48 0.07 225);
    --nm-16-warn: oklch(0.48 0.13 42);
  }
}

@supports (color: color-mix(in oklab, #fff, #000)) {
  .nm-16 {
    --nm-16-dark: color-mix(in oklab, var(--nm-16-surface), #000 20%);
    --nm-16-light: color-mix(in oklab, var(--nm-16-surface), #fff 90%);
    --nm-16-border: color-mix(in oklab, var(--nm-16-surface), var(--nm-16-ink) 33%);
  }
}

.nm-16 *,
.nm-16 *::before,
.nm-16 *::after {
  box-sizing: border-box;
}

.nm-16__stage {
  max-width: 1060px;
  margin: 0 auto;
  min-height: 100vh;
  padding: clamp(26px, 5vw, 56px) clamp(16px, 4vw, 40px);
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: clamp(22px, 3.6vw, 34px);
}

.nm-16__head {
  max-width: 58ch;
  display: flex;
  flex-direction: column;
  gap: 9px;
}

.nm-16__kicker {
  margin: 0;
  font-size: 0.7rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--nm-16-muted);
}

.nm-16__heading {
  margin: 0;
  font-family: var(--nm-16-font-display);
  font-size: clamp(1.5rem, 4.2vw, 2.2rem);
  font-weight: 600;
  letter-spacing: -0.03em;
  line-height: 1.12;
  text-wrap: balance;
}

.nm-16__sub {
  margin: 0;
  font-size: 0.94rem;
  line-height: 1.6;
  color: var(--nm-16-muted);
  text-wrap: pretty;
}

.nm-16__compare {
  display: grid;
  grid-template-columns: 1fr;
  gap: clamp(16px, 2.6vw, 22px);
}

@media (min-width: 760px) {
  .nm-16__compare {
    grid-template-columns: repeat(3, 1fr);
  }
}

.nm-16__side {
  border-radius: 22px;
  padding: clamp(16px, 2.6vw, 22px);
  display: flex;
  flex-direction: column;
  gap: 14px;
  min-inline-size: 0;
  background: var(--nm-16-surface);
}

.nm-16__side--dark,
.nm-16__side--naive {
  --nm-16-surface: #2a2a30;
  --nm-16-ink: #eaeaef;
  --nm-16-muted: #9d9daa;
  --nm-16-border: #8a8a97;
  --nm-16-accent: #79b4cc;
  color: var(--nm-16-ink);
}

@supports (color: oklch(0.28 0.008 285)) {
  .nm-16__side--dark,
    .nm-16__side--naive {
    --nm-16-surface: oklch(0.285 0.008 285);
    --nm-16-ink: oklch(0.93 0.006 285);
  }
}

.nm-16__side--dark {
  --nm-16-dark: rgba(11,11,14,0.72);
  --nm-16-light: rgba(88,88,100,0.42);
}

@supports (color: color-mix(in oklab, #fff, #000)) {
  .nm-16__side--dark {
    --nm-16-dark: color-mix(in oklab, var(--nm-16-surface), #000 55%);
    --nm-16-light: color-mix(in oklab, var(--nm-16-surface), #fff 14%);
    --nm-16-border: color-mix(in oklab, var(--nm-16-surface), var(--nm-16-ink) 42%);
  }
}

.nm-16__side--naive {
  --nm-16-dark: rgba(35,35,40,0.62);
  --nm-16-light: rgba(255,255,255,0.9);
}

@supports (color: color-mix(in oklab, #fff, #000)) {
  .nm-16__side--naive {
    --nm-16-dark: color-mix(in oklab, var(--nm-16-surface), #000 20%);
    --nm-16-light: color-mix(in oklab, var(--nm-16-surface), #fff 90%);
  }
}

.nm-16__sidelabel {
  margin: 0;
  font-size: 0.72rem;
  font-weight: 600;
  line-height: 1.45;
  color: var(--nm-16-muted);
}

.nm-16__sidelabel--warn {
  color: #e08a68;
}

.nm-16__card {
  border-radius: 18px;
  padding: clamp(16px, 2.6vw, 22px);
  display: flex;
  flex-direction: column;
  gap: 10px;
  min-inline-size: 0;
  background: var(--nm-16-surface);
  border: 1px solid var(--nm-16-border);
  box-shadow: 9px 9px 19px var(--nm-16-dark), -9px -9px 19px var(--nm-16-light);
}

.nm-16__cardtitle {
  margin: 0;
  font-size: 0.68rem;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--nm-16-muted);
}

.nm-16__cardvalue {
  margin: 0;
  font-family: var(--nm-16-font-display);
  font-size: clamp(1.6rem, 5vw, 2.1rem);
  font-weight: 600;
  letter-spacing: -0.03em;
  font-variant-numeric: tabular-nums;
}

.nm-16__cardvalue em {
  font-style: normal;
  font-size: 0.42em;
  letter-spacing: 0.05em;
  color: var(--nm-16-muted);
}

.nm-16__track {
  height: 12px;
  border-radius: 999px;
  background: var(--nm-16-surface);
  box-shadow: inset 3px 3px 7px var(--nm-16-dark), inset -3px -3px 7px var(--nm-16-light);
  overflow: hidden;
}

.nm-16__fill {
  display: block;
  height: 100%;
  border-radius: 999px;
  background: var(--nm-16-accent);
}

.nm-16__table {
  margin: 0;
  display: grid;
  gap: 10px;
}

.nm-16__trow {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  gap: 10px;
  padding-bottom: 9px;
  border-bottom: 1px dotted var(--nm-16-border);
  min-inline-size: 0;
}

.nm-16__trow dt {
  font-family: var(--nm-16-font-display);
  font-size: 0.8rem;
  font-weight: 600;
  min-inline-size: 0;
}

.nm-16__trow dd {
  margin: 0;
  font-size: 0.8rem;
  color: var(--nm-16-muted);
  text-align: right;
  min-inline-size: 0;
}

@media (prefers-color-scheme: dark) {
  .nm-16 {
    --nm-16-surface: #2a2a30;
    --nm-16-dark: rgba(11,11,14,0.72);
    --nm-16-light: rgba(88,88,100,0.42);
    --nm-16-ink: #eaeaef;
    --nm-16-muted: #9d9daa;
    --nm-16-border: #8a8a97;
    --nm-16-accent: #79b4cc;
    --nm-16-warn: #e08a68;
  }

  @supports (color: color-mix(in oklab, #fff, #000)) {
    .nm-16 {
      --nm-16-dark: color-mix(in oklab, var(--nm-16-surface), #000 55%);
      --nm-16-light: color-mix(in oklab, var(--nm-16-surface), #fff 14%);
    }
  }

  .nm-16__side--light {
    --nm-16-surface: #e8e8ea;
    --nm-16-ink: #26262b;
    --nm-16-muted: #585862;
    --nm-16-border: #98989f;
    --nm-16-dark: rgba(174,174,180,0.62);
    --nm-16-light: rgba(255,255,255,0.94);
    --nm-16-accent: #37697e;
    color: var(--nm-16-ink);
  }
}

.nm-16[data-theme="dark"] {
  --nm-16-surface: #2a2a30;
  --nm-16-dark: rgba(11,11,14,0.72);
  --nm-16-light: rgba(88,88,100,0.42);
  --nm-16-ink: #eaeaef;
  --nm-16-muted: #9d9daa;
  --nm-16-border: #8a8a97;
  --nm-16-accent: #79b4cc;
  --nm-16-warn: #e08a68;
}

@supports (color: color-mix(in oklab, #fff, #000)) {
  .nm-16[data-theme="dark"] {
    --nm-16-dark: color-mix(in oklab, var(--nm-16-surface), #000 55%);
    --nm-16-light: color-mix(in oklab, var(--nm-16-surface), #fff 14%);
  }
}

.nm-16[data-theme="dark"] .nm-16__side--light {
  --nm-16-surface: #e8e8ea;
  --nm-16-ink: #26262b;
  --nm-16-muted: #585862;
  --nm-16-border: #98989f;
  --nm-16-dark: rgba(174,174,180,0.62);
  --nm-16-light: rgba(255,255,255,0.94);
  --nm-16-accent: #37697e;
  color: var(--nm-16-ink);
}
/* Pure-CSS theme toggle. Mirrors the [data-theme="dark"] rules above so
   the demo's own dark palette is reachable from inside the demo. */

.nm-16__themeinput {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: 0;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.nm-16__themebtn {
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
  background: var(--nm-16-surface);
  color: var(--nm-16-ink);
  border: 1px solid var(--nm-16-line);
  font: 600 11px/1 var(--nm-16-font-display, system-ui);
  letter-spacing: 0.12em;
  text-transform: uppercase;
  cursor: pointer;
  box-shadow: var(--nm-16-distance, 6px) var(--nm-16-distance, 6px) var(--nm-16-blur, 14px) var(--nm-16-dark), calc(-1 * var(--nm-16-distance, 6px)) calc(-1 * var(--nm-16-distance, 6px)) var(--nm-16-blur, 14px) var(--nm-16-light);
  transition: box-shadow 180ms ease, color 180ms ease;
}

.nm-16__themebtn:hover {
  color: var(--nm-16-ink);
}

.nm-16__themeinput:focus-visible + .nm-16__themebtn {
  outline: 2px solid var(--nm-16-ink);
  outline-offset: 3px;
}

.nm-16:has(#nm-16-theme:checked) .nm-16__themebtn {
  box-shadow: inset var(--nm-16-distance, 6px) var(--nm-16-distance, 6px) var(--nm-16-blur, 14px) var(--nm-16-dark), inset calc(-1 * var(--nm-16-distance, 6px)) calc(-1 * var(--nm-16-distance, 6px)) var(--nm-16-blur, 14px) var(--nm-16-light);
}

.nm-16__themebtn svg {
  inline-size: 13px;
  block-size: 13px;
  flex: none;
}

.nm-16:has(#nm-16-theme:checked) {
  --nm-16-surface: #2a2a30;
  --nm-16-dark: rgba(11,11,14,0.72);
  --nm-16-light: rgba(88,88,100,0.42);
  --nm-16-ink: #eaeaef;
  --nm-16-muted: #9d9daa;
  --nm-16-border: #8a8a97;
  --nm-16-accent: #79b4cc;
  --nm-16-warn: #e08a68;
}

@media (prefers-color-scheme: light) {
  .nm-16:has(#nm-16-theme:checked) {
    --nm-16-surface: #2a2a30;
    --nm-16-dark: rgba(11,11,14,0.72);
    --nm-16-light: rgba(88,88,100,0.42);
    --nm-16-ink: #eaeaef;
    --nm-16-muted: #9d9daa;
    --nm-16-border: #8a8a97;
    --nm-16-accent: #79b4cc;
    --nm-16-warn: #e08a68;
  }
}

@media (prefers-color-scheme: dark) {
  /* Base already resolves dark here, so :checked restores light —
       without this the toggle is inert for dark-OS visitors. */

  .nm-16:has(#nm-16-theme:checked) {
    --nm-16-surface: #e8e8ea;
    --nm-16-dark: rgba(174,174,180,0.62);
    --nm-16-light: rgba(255,255,255,0.94);
    --nm-16-ink: #26262b;
    --nm-16-muted: #585862;
    --nm-16-border: #98989f;
    --nm-16-accent: #37697e;
    --nm-16-warn: #9c4a2e;
  }
}

@media (prefers-reduced-motion: reduce) {
  .nm-16__themebtn {
    transition: none;
  }
}
```
