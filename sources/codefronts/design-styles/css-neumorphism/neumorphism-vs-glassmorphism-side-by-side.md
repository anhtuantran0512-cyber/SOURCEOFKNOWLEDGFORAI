---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-neumorphism/neumorphism-vs-glassmorphism-side-by-side/"
title: "Neumorphism vs Glassmorphism Side by Side"
section: "design-styles"
category: "css-neumorphism"
category_name: "CSS Neumorphism"
description: "The two styles people conflate, rendered on the same background with both sides labelled."
has_js: "false"
---

Here's a working CSS Neumorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neumorphism vs Glassmorphism Side by Side
Source: https://codefronts.com/design-styles/css-neumorphism/neumorphism-vs-glassmorphism-side-by-side/

The two styles people conflate, rendered on the same background with both sides labelled. Neumorphism is opaque, the same colour as its parent, and lit by a mirrored shadow pair. Glassmorphism is translucent, blurs what sits behind it, and needs a light border to catch its edge. The practical rule sits underneath: soft UI needs a plain background, glass needs a busy one, which is why swapping one for the other rarely survives a redesign.
## HTML
```html
<section class="nm-02" aria-labelledby="nm-02-heading">
      <input type="checkbox" id="nm-02-theme" class="nm-02__themeinput">
      <label for="nm-02-theme" class="nm-02__themebtn">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 3a9 9 0 1 0 9 9 7 7 0 0 1-9-9Z"/></svg>
        Theme
      </label>
  <div class="nm-02__stage">
    <header class="nm-02__head">
      <p class="nm-02__kicker">Comparison</p>
      <h2 class="nm-02__heading" id="nm-02-heading">Soft UI and frosted glass are not interchangeable</h2>
      <p class="nm-02__sub">Same page, same components, different backgrounds — because each style depends on the one the other cannot use.</p>
    </header>

    <div class="nm-02__split">
      <div class="nm-02__side nm-02__side--nm-02-soft">
        <p class="nm-02__sidelabel">Neumorphism — opaque, matches its parent, no blur</p>
        <div class="nm-02__card nm-02__card--nm-02-soft">
          <p class="nm-02__cardkicker">Storage</p>
          <p class="nm-02__cardvalue">64.2 <em>GB</em></p>
          <p class="nm-02__cardmeta">of 128 GB used on Meridian</p>
          <div class="nm-02__bar"><span class="nm-02__barfill nm-02__barfill--nm-02-soft"></span></div>
          <button class="nm-02__btn nm-02__btn--nm-02-soft" type="button">Manage storage</button>
        </div>
        <ul class="nm-02__facts">
          <li class="nm-02__fact">Background required: <b>flat, single colour</b></li>
          <li class="nm-02__fact">Depth from: <b>mirrored shadow pair</b></li>
          <li class="nm-02__fact">Edge contrast: <b>none unless added</b></li>
        </ul>
      </div>

      <div class="nm-02__side nm-02__side--nm-02-glass">
        <p class="nm-02__sidelabel nm-02__sidelabel--nm-02-glass">Glassmorphism — translucent, blurs the backdrop, lit border</p>
        <div class="nm-02__card nm-02__card--nm-02-glass">
          <p class="nm-02__cardkicker">Storage</p>
          <p class="nm-02__cardvalue">64.2 <em>GB</em></p>
          <p class="nm-02__cardmeta">of 128 GB used on Meridian</p>
          <div class="nm-02__bar nm-02__bar--nm-02-glass"><span class="nm-02__barfill nm-02__barfill--nm-02-glass"></span></div>
          <button class="nm-02__btn nm-02__btn--nm-02-glass" type="button">Manage storage</button>
        </div>
        <ul class="nm-02__facts nm-02__facts--nm-02-glass">
          <li class="nm-02__fact">Background required: <b>busy, image or gradient</b></li>
          <li class="nm-02__fact">Depth from: <b>backdrop-filter blur</b></li>
          <li class="nm-02__fact">Edge contrast: <b>hairline border, free</b></li>
        </ul>
      </div>
    </div>

    <p class="nm-02__rule">The practical rule: neumorphism needs a plain background to work, glassmorphism needs a busy one. A redesign that changes the page background usually invalidates whichever one you chose.</p>
  </div>
</section>
```
## CSS
```css
.nm-02 {
  position: relative;
  --nm-02-surface: #ece6dc;
  --nm-02-dark: rgba(179,167,148,0.62);
  --nm-02-light: rgba(255,253,248,0.95);
  --nm-02-ink: #34302a;
  --nm-02-muted: #6f6759;
  --nm-02-accent: #3f5f96;
  --nm-02-glassink: #1e2735;
  --nm-02-distance: clamp(7px, 1.6vw, 13px);
  --nm-02-blur: clamp(16px, 3.4vw, 28px);
  --nm-02-font-display: Georgia, "Iowan Old Style", "Times New Roman", serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--nm-02-surface);
  color: var(--nm-02-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

@supports (color: oklch(0.9 0.01 80)) {
  .nm-02 {
    --nm-02-surface: oklch(0.923 0.017 82);
    --nm-02-ink: oklch(0.31 0.012 70);
    --nm-02-muted: oklch(0.53 0.017 76);
    --nm-02-accent: oklch(0.51 0.09 258);
  }
}

@supports (color: color-mix(in oklab, #fff, #000)) {
  .nm-02 {
    --nm-02-dark: color-mix(in oklab, var(--nm-02-surface), #000 20%);
    --nm-02-light: color-mix(in oklab, var(--nm-02-surface), #fff 90%);
  }
}

.nm-02 *,
.nm-02 *::before,
.nm-02 *::after {
  box-sizing: border-box;
}

.nm-02__stage {
  max-width: 1140px;
  margin: 0 auto;
  padding: clamp(24px, 5vw, 56px) clamp(16px, 4vw, 44px);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: clamp(22px, 3.5vw, 36px);
}

.nm-02__head {
  max-width: 62ch;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.nm-02__kicker {
  margin: 0;
  font-size: 0.7rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--nm-02-muted);
}

.nm-02__heading {
  margin: 0;
  font-family: var(--nm-02-font-display);
  font-size: clamp(1.55rem, 4.4vw, 2.5rem);
  font-weight: 400;
  line-height: 1.12;
  letter-spacing: -0.015em;
  text-wrap: balance;
}

.nm-02__sub {
  margin: 0;
  font-size: 0.95rem;
  line-height: 1.6;
  color: var(--nm-02-muted);
  text-wrap: pretty;
}

.nm-02__split {
  display: grid;
  grid-template-columns: 1fr;
  gap: clamp(18px, 3vw, 26px);
}

@media (min-width: 760px) {
  .nm-02__split {
    grid-template-columns: 1fr 1fr;
  }
}

.nm-02__side {
  border-radius: 24px;
  padding: clamp(18px, 3vw, 28px);
  display: flex;
  flex-direction: column;
  gap: 18px;
  min-inline-size: 0;
}

.nm-02__side--nm-02-soft {
  background: var(--nm-02-surface);
}

.nm-02__side--nm-02-glass {
  background-color: #4a5b74;
  background-image: radial-gradient(circle at 18% 22%, #d98b5f 0, transparent 42%), radial-gradient(circle at 82% 18%, #6f8fb5 0, transparent 46%), radial-gradient(circle at 62% 88%, #2f3d52 0, transparent 52%);
  color: #f3f5f9;
}

.nm-02__sidelabel {
  margin: 0;
  font-size: 0.74rem;
  font-weight: 600;
  letter-spacing: 0.02em;
  line-height: 1.45;
  color: var(--nm-02-muted);
}

.nm-02__sidelabel--nm-02-glass {
  color: rgba(243,245,249,0.86);
}

.nm-02__card {
  border-radius: 20px;
  padding: clamp(18px, 3vw, 26px);
  display: flex;
  flex-direction: column;
  gap: 12px;
  min-inline-size: 0;
}

.nm-02__card--nm-02-soft {
  background: var(--nm-02-surface);
  border: 1px solid transparent;
  box-shadow: var(--nm-02-distance) var(--nm-02-distance) var(--nm-02-blur) var(--nm-02-dark), calc(var(--nm-02-distance) * -1) calc(var(--nm-02-distance) * -1) var(--nm-02-blur) var(--nm-02-light);
}

.nm-02__card--nm-02-glass {
  background: rgba(255,255,255,0.16);
  border: 1px solid rgba(255,255,255,0.42);
  box-shadow: 0 12px 34px rgba(14,20,32,0.3);
}

@supports ((-webkit-backdrop-filter: blur(4px)) or (backdrop-filter: blur(4px))) {
  .nm-02__card--nm-02-glass {
    -webkit-backdrop-filter: blur(18px) saturate(1.4);
    backdrop-filter: blur(18px) saturate(1.4);
    background: rgba(255,255,255,0.12);
  }
}

.nm-02__cardkicker {
  margin: 0;
  font-size: 0.7rem;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  opacity: 0.72;
}

.nm-02__cardvalue {
  margin: 0;
  font-family: var(--nm-02-font-display);
  font-size: clamp(1.9rem, 6vw, 2.6rem);
  line-height: 1;
  font-variant-numeric: tabular-nums;
}

.nm-02__cardvalue em {
  font-style: normal;
  font-size: 0.42em;
  letter-spacing: 0.06em;
  opacity: 0.7;
}

.nm-02__cardmeta {
  margin: 0;
  font-size: 0.82rem;
  opacity: 0.78;
}

.nm-02__bar {
  height: 12px;
  border-radius: 999px;
  background: var(--nm-02-surface);
  box-shadow: inset 3px 3px 6px var(--nm-02-dark), inset -3px -3px 6px var(--nm-02-light);
  overflow: hidden;
}

.nm-02__bar--nm-02-glass {
  background: rgba(20,28,42,0.34);
  box-shadow: none;
  border: 1px solid rgba(255,255,255,0.3);
}

.nm-02__barfill {
  display: block;
  height: 100%;
  width: 50%;
  border-radius: 999px;
}

.nm-02__barfill--nm-02-soft {
  background: var(--nm-02-accent);
}

.nm-02__barfill--nm-02-glass {
  background: #f6d9a8;
}

.nm-02__btn {
  margin-top: 4px;
  min-height: 44px;
  border-radius: 14px;
  font: inherit;
  font-size: 0.86rem;
  font-weight: 600;
  cursor: pointer;
  padding: 0 18px;
  transition: transform 140ms ease;
}

.nm-02__btn--nm-02-soft {
  background: var(--nm-02-surface);
  color: var(--nm-02-ink);
  border: 1px solid var(--nm-02-muted);
  box-shadow: 5px 5px 12px var(--nm-02-dark), -5px -5px 12px var(--nm-02-light);
}

.nm-02__btn--nm-02-soft:active {
  box-shadow: inset 4px 4px 9px var(--nm-02-dark), inset -4px -4px 9px var(--nm-02-light);
}

.nm-02__btn--nm-02-glass {
  background: rgba(255,255,255,0.2);
  color: #fff;
  border: 1px solid rgba(255,255,255,0.55);
}

.nm-02__btn--nm-02-glass:active {
  transform: translateY(1px);
}

.nm-02__btn:focus-visible {
  outline: 2px solid var(--nm-02-accent);
  outline-offset: 3px;
}

.nm-02__btn--nm-02-glass:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 3px;
}

.nm-02__facts {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 7px;
}

.nm-02__fact {
  font-size: 0.78rem;
  line-height: 1.5;
  color: var(--nm-02-muted);
  min-inline-size: 0;
}

.nm-02__fact b {
  color: var(--nm-02-ink);
  font-weight: 600;
}

.nm-02__facts--nm-02-glass .nm-02__fact {
  color: rgba(243,245,249,0.82);
}

.nm-02__facts--nm-02-glass .nm-02__fact b {
  color: #fff;
}

.nm-02__rule {
  margin: 0;
  max-width: 72ch;
  font-size: 0.88rem;
  line-height: 1.65;
  color: var(--nm-02-muted);
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .nm-02__btn {
    transition: none;
  }
}

@media (prefers-color-scheme: dark) {
  .nm-02 {
    --nm-02-surface: #2f2b26;
    --nm-02-dark: rgba(14,12,10,0.7);
    --nm-02-light: rgba(96,88,76,0.48);
    --nm-02-ink: #ece5da;
    --nm-02-muted: #a89b89;
    --nm-02-accent: #8aa9dd;
  }

  @supports (color: color-mix(in oklab, #fff, #000)) {
    .nm-02 {
      --nm-02-dark: color-mix(in oklab, var(--nm-02-surface), #000 52%);
      --nm-02-light: color-mix(in oklab, var(--nm-02-surface), #fff 15%);
    }
  }
}

.nm-02[data-theme="dark"] {
  --nm-02-surface: #2f2b26;
  --nm-02-dark: rgba(14,12,10,0.7);
  --nm-02-light: rgba(96,88,76,0.48);
  --nm-02-ink: #ece5da;
  --nm-02-muted: #a89b89;
  --nm-02-accent: #8aa9dd;
}

@supports (color: color-mix(in oklab, #fff, #000)) {
  .nm-02[data-theme="dark"] {
    --nm-02-dark: color-mix(in oklab, var(--nm-02-surface), #000 52%);
    --nm-02-light: color-mix(in oklab, var(--nm-02-surface), #fff 15%);
  }
}
/* Pure-CSS theme toggle. Mirrors the [data-theme="dark"] rules above so
   the demo's own dark palette is reachable from inside the demo. */

.nm-02__themeinput {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: 0;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.nm-02__themebtn {
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
  background: var(--nm-02-surface);
  color: var(--nm-02-ink);
  border: 1px solid var(--nm-02-line);
  font: 600 11px/1 var(--nm-02-font-display, system-ui);
  letter-spacing: 0.12em;
  text-transform: uppercase;
  cursor: pointer;
  box-shadow: var(--nm-02-distance, 6px) var(--nm-02-distance, 6px) var(--nm-02-blur, 14px) var(--nm-02-dark), calc(-1 * var(--nm-02-distance, 6px)) calc(-1 * var(--nm-02-distance, 6px)) var(--nm-02-blur, 14px) var(--nm-02-light);
  transition: box-shadow 180ms ease, color 180ms ease;
}

.nm-02__themebtn:hover {
  color: var(--nm-02-ink);
}

.nm-02__themeinput:focus-visible + .nm-02__themebtn {
  outline: 2px solid var(--nm-02-ink);
  outline-offset: 3px;
}

.nm-02:has(#nm-02-theme:checked) .nm-02__themebtn {
  box-shadow: inset var(--nm-02-distance, 6px) var(--nm-02-distance, 6px) var(--nm-02-blur, 14px) var(--nm-02-dark), inset calc(-1 * var(--nm-02-distance, 6px)) calc(-1 * var(--nm-02-distance, 6px)) var(--nm-02-blur, 14px) var(--nm-02-light);
}

.nm-02__themebtn svg {
  inline-size: 13px;
  block-size: 13px;
  flex: none;
}

.nm-02:has(#nm-02-theme:checked) {
  --nm-02-surface: #2f2b26;
  --nm-02-dark: rgba(14,12,10,0.7);
  --nm-02-light: rgba(96,88,76,0.48);
  --nm-02-ink: #ece5da;
  --nm-02-muted: #a89b89;
  --nm-02-accent: #8aa9dd;
}

@media (prefers-color-scheme: light) {
  .nm-02:has(#nm-02-theme:checked) {
    --nm-02-surface: #2f2b26;
    --nm-02-dark: rgba(14,12,10,0.7);
    --nm-02-light: rgba(96,88,76,0.48);
    --nm-02-ink: #ece5da;
    --nm-02-muted: #a89b89;
    --nm-02-accent: #8aa9dd;
  }
}

@media (prefers-color-scheme: dark) {
  /* Base already resolves dark here, so :checked restores light —
       without this the toggle is inert for dark-OS visitors. */

  .nm-02:has(#nm-02-theme:checked) {
    --nm-02-surface: #ece6dc;
    --nm-02-dark: rgba(179,167,148,0.62);
    --nm-02-light: rgba(255,253,248,0.95);
    --nm-02-ink: #34302a;
    --nm-02-muted: #6f6759;
    --nm-02-accent: #3f5f96;
  }
}

@media (prefers-reduced-motion: reduce) {
  .nm-02__themebtn {
    transition: none;
  }
}
```
