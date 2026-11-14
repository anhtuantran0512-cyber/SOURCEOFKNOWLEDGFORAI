---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-neumorphism/neumorphic-palette-tokens-with-color-mix/"
title: "Neumorphic Palette Tokens with color-mix"
section: "design-styles"
category: "css-neumorphism"
category_name: "CSS Neumorphism"
description: "One surface token feeds an entire soft-UI palette."
has_js: "false"
---

Here's a working CSS Neumorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neumorphic Palette Tokens with color-mix
Source: https://codefronts.com/design-styles/css-neumorphism/neumorphic-palette-tokens-with-color-mix/

One surface token feeds an entire soft-UI palette. Four cards on four different surface colours — grey, sand, sage, slate — all rendering from the same component CSS, because both shadow colours are derived with color-mix(in oklab) rather than hardcoded. Includes the pair of cards showing what happens when you copy the standard blue-grey shadows onto a warm surface: the shadows read as dirt.
## HTML
```html
<section class="nm-06" aria-labelledby="nm-06-heading">
      <input type="checkbox" id="nm-06-theme" class="nm-06__themeinput">
      <label for="nm-06-theme" class="nm-06__themebtn">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 3a9 9 0 1 0 9 9 7 7 0 0 1-9-9Z"/></svg>
        Theme
      </label>
  <div class="nm-06__stage">
    <header class="nm-06__head">
      <p class="nm-06__kicker">Tokens</p>
      <h2 class="nm-06__heading" id="nm-06-heading">One surface token, four palettes</h2>
      <p class="nm-06__sub">Identical component CSS on every card. Only <code>--surface</code> and <code>--ink</code> change; both shadows, the border and the muted text derive.</p>
    </header>

    <div class="nm-06__grid">
      <article class="nm-06__card" data-swatch="grey">
        <p class="nm-06__name">Ash</p>
        <div class="nm-06__well"><span class="nm-06__wellbar" style="width:72%"></span></div>
        <dl class="nm-06__spec">
          <div class="nm-06__srow"><dt>surface</dt><dd>oklch(.91 .012 258)</dd></div>
          <div class="nm-06__srow"><dt>dark</dt><dd>mix +20% black</dd></div>
          <div class="nm-06__srow"><dt>light</dt><dd>mix +90% white</dd></div>
        </dl>
      </article>
      <article class="nm-06__card" data-swatch="sand">
        <p class="nm-06__name">Sand</p>
        <div class="nm-06__well"><span class="nm-06__wellbar" style="width:48%"></span></div>
        <dl class="nm-06__spec">
          <div class="nm-06__srow"><dt>surface</dt><dd>oklch(.92 .028 78)</dd></div>
          <div class="nm-06__srow"><dt>dark</dt><dd>mix +20% black</dd></div>
          <div class="nm-06__srow"><dt>light</dt><dd>mix +90% white</dd></div>
        </dl>
      </article>
      <article class="nm-06__card" data-swatch="sage">
        <p class="nm-06__name">Sage</p>
        <div class="nm-06__well"><span class="nm-06__wellbar" style="width:63%"></span></div>
        <dl class="nm-06__spec">
          <div class="nm-06__srow"><dt>surface</dt><dd>oklch(.90 .031 150)</dd></div>
          <div class="nm-06__srow"><dt>dark</dt><dd>mix +20% black</dd></div>
          <div class="nm-06__srow"><dt>light</dt><dd>mix +90% white</dd></div>
        </dl>
      </article>
      <article class="nm-06__card" data-swatch="slate">
        <p class="nm-06__name">Slate</p>
        <div class="nm-06__well"><span class="nm-06__wellbar" style="width:86%"></span></div>
        <dl class="nm-06__spec">
          <div class="nm-06__srow"><dt>surface</dt><dd>oklch(.34 .018 258)</dd></div>
          <div class="nm-06__srow"><dt>dark</dt><dd>mix +52% black</dd></div>
          <div class="nm-06__srow"><dt>light</dt><dd>mix +15% white</dd></div>
        </dl>
      </article>
    </div>

    <div class="nm-06__compare">
      <div class="nm-06__case">
        <div class="nm-06__chip nm-06__chip--derived"></div>
        <p class="nm-06__caselabel">Derived in oklab — the shadow keeps the surface's hue</p>
      </div>
      <div class="nm-06__case">
        <div class="nm-06__chip nm-06__chip--stock"></div>
        <p class="nm-06__caselabel nm-06__caselabel--warn">Stock blue-grey shadows on a warm surface — reads as dirt</p>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.nm-06 {
  position: relative;
  --nm-06-surface: #eceff4;
  --nm-06-ink: #232830;
  --nm-06-dark: rgba(168,176,190,0.6);
  --nm-06-light: rgba(255,255,255,0.95);
  --nm-06-muted: #616a78;
  --nm-06-border: #99a1ae;
  --nm-06-accent: #3d6ea8;
  --nm-06-warn: #a4472f;
  --nm-06-dist: clamp(6px, 1.4vw, 10px);
  --nm-06-blur: clamp(12px, 2.8vw, 20px);
  --nm-06-font-display: ui-monospace, "SFMono-Regular", Menlo, monospace;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--nm-06-surface);
  color: var(--nm-06-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

@supports (color: oklch(0.9 0.01 258)) {
  .nm-06 {
    --nm-06-surface: oklch(0.937 0.008 258);
    --nm-06-ink: oklch(0.27 0.017 262);
    --nm-06-accent: oklch(0.51 0.11 252);
    --nm-06-warn: oklch(0.49 0.14 38);
  }
}

@supports (color: color-mix(in oklab, #fff, #000)) {
  .nm-06 {
    --nm-06-dark: color-mix(in oklab, var(--nm-06-surface), #000 18%);
    --nm-06-light: color-mix(in oklab, var(--nm-06-surface), #fff 92%);
    --nm-06-muted: color-mix(in oklab, var(--nm-06-surface), var(--nm-06-ink) 62%);
    --nm-06-border: color-mix(in oklab, var(--nm-06-surface), var(--nm-06-ink) 35%);
  }
}

.nm-06 *,
.nm-06 *::before,
.nm-06 *::after {
  box-sizing: border-box;
}

.nm-06__stage {
  max-width: 1080px;
  margin: 0 auto;
  min-height: 100vh;
  padding: clamp(26px, 5vw, 58px) clamp(16px, 4vw, 42px);
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: clamp(22px, 3.6vw, 36px);
}

.nm-06__head {
  max-width: 62ch;
  display: flex;
  flex-direction: column;
  gap: 9px;
}

.nm-06__kicker {
  margin: 0;
  font-family: var(--nm-06-font-display);
  font-size: 0.7rem;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--nm-06-muted);
}

.nm-06__heading {
  margin: 0;
  font-family: var(--nm-06-font-display);
  font-size: clamp(1.5rem, 4.2vw, 2.25rem);
  font-weight: 600;
  letter-spacing: -0.02em;
  line-height: 1.12;
  text-wrap: balance;
}

.nm-06__sub {
  margin: 0;
  font-size: 0.94rem;
  line-height: 1.6;
  color: var(--nm-06-muted);
  text-wrap: pretty;
}

.nm-06__sub code {
  font-family: var(--nm-06-font-display);
  font-size: 0.86em;
  color: var(--nm-06-ink);
}

.nm-06__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 200px), 1fr));
  gap: clamp(14px, 2.4vw, 22px);
}

.nm-06__card {
  --nm-06-surface: #eceff4;
  --nm-06-ink: #232830;
  border-radius: 20px;
  padding: clamp(16px, 2.6vw, 22px);
  display: flex;
  flex-direction: column;
  gap: 14px;
  min-inline-size: 0;
  background: var(--nm-06-surface);
  color: var(--nm-06-ink);
  border: 1px solid var(--nm-06-border);
  box-shadow: var(--nm-06-dist) var(--nm-06-dist) var(--nm-06-blur) var(--nm-06-dark), calc(var(--nm-06-dist) * -1) calc(var(--nm-06-dist) * -1) var(--nm-06-blur) var(--nm-06-light);
}

.nm-06__card[data-swatch="grey"] {
  --nm-06-surface: #e2e6ee;
  --nm-06-ink: #232830;
}

.nm-06__card[data-swatch="sand"] {
  --nm-06-surface: #eee3d1;
  --nm-06-ink: #2f2820;
}

.nm-06__card[data-swatch="sage"] {
  --nm-06-surface: #dde7d9;
  --nm-06-ink: #212a20;
}

.nm-06__card[data-swatch="slate"] {
  --nm-06-surface: #333a45;
  --nm-06-ink: #eef1f6;
  --nm-06-dark: rgba(15,18,23,0.72);
  --nm-06-light: rgba(104,114,132,0.44);
}

@supports (color: oklch(0.9 0.01 258)) {
  .nm-06__card[data-swatch="grey"] {
    --nm-06-surface: oklch(0.912 0.012 258);
  }

  .nm-06__card[data-swatch="sand"] {
    --nm-06-surface: oklch(0.921 0.028 78);
    --nm-06-ink: oklch(0.27 0.019 70);
  }

  .nm-06__card[data-swatch="sage"] {
    --nm-06-surface: oklch(0.902 0.031 150);
    --nm-06-ink: oklch(0.26 0.024 150);
  }

  .nm-06__card[data-swatch="slate"] {
    --nm-06-surface: oklch(0.343 0.018 258);
    --nm-06-ink: oklch(0.95 0.008 258);
  }
}

@supports (color: color-mix(in oklab, #fff, #000)) {
  .nm-06__card[data-swatch="slate"] {
    --nm-06-dark: color-mix(in oklab, var(--nm-06-surface), #000 52%);
    --nm-06-light: color-mix(in oklab, var(--nm-06-surface), #fff 15%);
  }
}

.nm-06__name {
  margin: 0;
  font-family: var(--nm-06-font-display);
  font-size: 0.95rem;
  font-weight: 600;
  letter-spacing: 0.02em;
}

.nm-06__well {
  height: 14px;
  border-radius: 999px;
  background: var(--nm-06-surface);
  box-shadow: inset 3px 3px 6px var(--nm-06-dark), inset -3px -3px 6px var(--nm-06-light);
  overflow: hidden;
}

.nm-06__wellbar {
  display: block;
  height: 100%;
  border-radius: 999px;
  background: var(--nm-06-accent);
}

.nm-06__spec {
  margin: 0;
  display: grid;
  gap: 6px;
}

.nm-06__srow {
  display: flex;
  justify-content: space-between;
  gap: 10px;
  font-family: var(--nm-06-font-display);
  font-size: 0.68rem;
  min-inline-size: 0;
}

.nm-06__srow dt {
  color: var(--nm-06-muted);
}

.nm-06__srow dd {
  margin: 0;
  text-align: right;
  min-inline-size: 0;
  overflow-wrap: anywhere;
}

.nm-06__compare {
  display: grid;
  grid-template-columns: 1fr;
  gap: clamp(14px, 2.4vw, 22px);
}

@media (min-width: 620px) {
  .nm-06__compare {
    grid-template-columns: 1fr 1fr;
  }
}

.nm-06__case {
  display: flex;
  flex-direction: column;
  gap: 10px;
  min-inline-size: 0;
}

.nm-06__chip {
  height: 74px;
  border-radius: 18px;
  background: #eee3d1;
  border: 1px solid transparent;
}

@supports (color: oklch(0.9 0.03 78)) {
  .nm-06__chip {
    background: oklch(0.921 0.028 78);
  }
}

.nm-06__chip--derived {
  box-shadow: 8px 8px 16px rgba(196,176,142,0.7), -8px -8px 16px rgba(255,252,244,0.95);
}

@supports (color: color-mix(in oklab, #fff, #000)) {
  .nm-06__chip--derived {
    box-shadow: 8px 8px 16px color-mix(in oklab, #eee3d1, #000 20%), -8px -8px 16px color-mix(in oklab, #eee3d1, #fff 90%);
  }
}

.nm-06__chip--stock {
  box-shadow: 8px 8px 16px rgba(163,177,198,0.85), -8px -8px 16px rgba(240,244,252,0.95);
}

.nm-06__caselabel {
  margin: 0;
  font-size: 0.78rem;
  line-height: 1.5;
  color: var(--nm-06-muted);
  text-wrap: pretty;
}

.nm-06__caselabel--warn {
  color: var(--nm-06-warn);
}

@media (prefers-color-scheme: dark) {
  .nm-06 {
    --nm-06-surface: #23272e;
    --nm-06-ink: #eaedf3;
    --nm-06-dark: rgba(10,12,15,0.72);
    --nm-06-light: rgba(86,93,106,0.42);
    --nm-06-accent: #86aee2;
    --nm-06-warn: #e6947a;
  }

  @supports (color: color-mix(in oklab, #fff, #000)) {
    .nm-06 {
      --nm-06-dark: color-mix(in oklab, var(--nm-06-surface), #000 55%);
      --nm-06-light: color-mix(in oklab, var(--nm-06-surface), #fff 13%);
    }
  }
}

.nm-06[data-theme="dark"] {
  --nm-06-surface: #23272e;
  --nm-06-ink: #eaedf3;
  --nm-06-dark: rgba(10,12,15,0.72);
  --nm-06-light: rgba(86,93,106,0.42);
  --nm-06-accent: #86aee2;
  --nm-06-warn: #e6947a;
}

@supports (color: color-mix(in oklab, #fff, #000)) {
  .nm-06[data-theme="dark"] {
    --nm-06-dark: color-mix(in oklab, var(--nm-06-surface), #000 55%);
    --nm-06-light: color-mix(in oklab, var(--nm-06-surface), #fff 13%);
  }
}
/* Pure-CSS theme toggle. Mirrors the [data-theme="dark"] rules above so
   the demo's own dark palette is reachable from inside the demo. */

.nm-06__themeinput {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: 0;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.nm-06__themebtn {
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
  background: var(--nm-06-surface);
  color: var(--nm-06-ink);
  border: 1px solid var(--nm-06-line);
  font: 600 11px/1 var(--nm-06-font-display, system-ui);
  letter-spacing: 0.12em;
  text-transform: uppercase;
  cursor: pointer;
  box-shadow: var(--nm-06-distance, 6px) var(--nm-06-distance, 6px) var(--nm-06-blur, 14px) var(--nm-06-dark), calc(-1 * var(--nm-06-distance, 6px)) calc(-1 * var(--nm-06-distance, 6px)) var(--nm-06-blur, 14px) var(--nm-06-light);
  transition: box-shadow 180ms ease, color 180ms ease;
}

.nm-06__themebtn:hover {
  color: var(--nm-06-ink);
}

.nm-06__themeinput:focus-visible + .nm-06__themebtn {
  outline: 2px solid var(--nm-06-ink);
  outline-offset: 3px;
}

.nm-06:has(#nm-06-theme:checked) .nm-06__themebtn {
  box-shadow: inset var(--nm-06-distance, 6px) var(--nm-06-distance, 6px) var(--nm-06-blur, 14px) var(--nm-06-dark), inset calc(-1 * var(--nm-06-distance, 6px)) calc(-1 * var(--nm-06-distance, 6px)) var(--nm-06-blur, 14px) var(--nm-06-light);
}

.nm-06__themebtn svg {
  inline-size: 13px;
  block-size: 13px;
  flex: none;
}

.nm-06:has(#nm-06-theme:checked) {
  --nm-06-surface: #23272e;
  --nm-06-ink: #eaedf3;
  --nm-06-dark: rgba(10,12,15,0.72);
  --nm-06-light: rgba(86,93,106,0.42);
  --nm-06-accent: #86aee2;
  --nm-06-warn: #e6947a;
}

@media (prefers-color-scheme: light) {
  .nm-06:has(#nm-06-theme:checked) {
    --nm-06-surface: #23272e;
    --nm-06-ink: #eaedf3;
    --nm-06-dark: rgba(10,12,15,0.72);
    --nm-06-light: rgba(86,93,106,0.42);
    --nm-06-accent: #86aee2;
    --nm-06-warn: #e6947a;
  }
}

@media (prefers-color-scheme: dark) {
  /* Base already resolves dark here, so :checked restores light —
       without this the toggle is inert for dark-OS visitors. */

  .nm-06:has(#nm-06-theme:checked) {
    --nm-06-surface: #eceff4;
    --nm-06-ink: #232830;
    --nm-06-dark: rgba(168,176,190,0.6);
    --nm-06-light: rgba(255,255,255,0.95);
    --nm-06-accent: #3d6ea8;
    --nm-06-warn: #a4472f;
  }
}

@media (prefers-reduced-motion: reduce) {
  .nm-06__themebtn {
    transition: none;
  }
}
```
