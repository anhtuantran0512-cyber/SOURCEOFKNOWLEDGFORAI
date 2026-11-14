---
source: "codefronts"
url: "https://codefronts.com/components/css-svg-stroke-buttons/non-scaling-stroke-button-that-resizes-with-text/"
title: "Non Scaling Stroke Button That Resizes with Text"
section: "components"
category: "css-svg-stroke-buttons"
category_name: "CSS SVG Stroke Buttons"
description: "The same call to action in six languages, right-to-left included, each button sized by its own text."
has_js: "false"
---

Here's a working CSS SVG Stroke Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Non Scaling Stroke Button That Resizes with Text
Source: https://codefronts.com/components/css-svg-stroke-buttons/non-scaling-stroke-button-that-resizes-with-text/

The same call to action in six languages, right-to-left included, each button sized by its own text. Every frame is one fixed 200&times;56 viewBox stretched to whatever width the label needs, so the resting border is genuinely wrong &mdash; thin on the sides, heavy top and bottom. Hover does not draw a line: it wipes the corrected stroke across the button from the leading edge, so what you watch is a border becoming even rather than becoming present. Corners are square on purpose, which isolates the stroke error from the geometry error.
## HTML
```html
<section class="svgb-10">
  <input class="svgb-10__ti" type="checkbox" id="svgb-10-theme">
  <label class="svgb-10__toggle" for="svgb-10-theme">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="svgb-10__sr">Switch colour scheme</span>
  </label>
  <div class="svgb-10__stage">
    <div class="svgb-10__sheet">
      <p class="svgb-10__kicker">One component &middot; six locales &middot; zero fixed widths</p>

      <ul class="svgb-10__rows">
        <li class="svgb-10__row">
          <span class="svgb-10__loc">en</span>
          <button class="svgb-10__btn" type="button">
            <svg class="svgb-10__frame" viewBox="0 0 200 56" preserveAspectRatio="none" aria-hidden="true"><rect class="svgb-10__raw" x="1" y="1" width="198" height="54"/></svg>
            <svg class="svgb-10__frame svgb-10__frame--true" viewBox="0 0 200 56" preserveAspectRatio="none" aria-hidden="true"><rect class="svgb-10__true" x="1" y="1" width="198" height="54" vector-effect="non-scaling-stroke"/></svg>
            <span class="svgb-10__seam" aria-hidden="true"></span>
            <span class="svgb-10__label">Start free trial</span>
          </button>
        </li>
        <li class="svgb-10__row">
          <span class="svgb-10__loc">de</span>
          <button class="svgb-10__btn" type="button">
            <svg class="svgb-10__frame" viewBox="0 0 200 56" preserveAspectRatio="none" aria-hidden="true"><rect class="svgb-10__raw" x="1" y="1" width="198" height="54"/></svg>
            <svg class="svgb-10__frame svgb-10__frame--true" viewBox="0 0 200 56" preserveAspectRatio="none" aria-hidden="true"><rect class="svgb-10__true" x="1" y="1" width="198" height="54" vector-effect="non-scaling-stroke"/></svg>
            <span class="svgb-10__seam" aria-hidden="true"></span>
            <span class="svgb-10__label" lang="de">Kostenlos testen starten</span>
          </button>
        </li>
        <li class="svgb-10__row">
          <span class="svgb-10__loc">fi</span>
          <button class="svgb-10__btn" type="button">
            <svg class="svgb-10__frame" viewBox="0 0 200 56" preserveAspectRatio="none" aria-hidden="true"><rect class="svgb-10__raw" x="1" y="1" width="198" height="54"/></svg>
            <svg class="svgb-10__frame svgb-10__frame--true" viewBox="0 0 200 56" preserveAspectRatio="none" aria-hidden="true"><rect class="svgb-10__true" x="1" y="1" width="198" height="54" vector-effect="non-scaling-stroke"/></svg>
            <span class="svgb-10__seam" aria-hidden="true"></span>
            <span class="svgb-10__label" lang="fi">Aloita maksuton kokeilujakso</span>
          </button>
        </li>
        <li class="svgb-10__row">
          <span class="svgb-10__loc">ja</span>
          <button class="svgb-10__btn" type="button">
            <svg class="svgb-10__frame" viewBox="0 0 200 56" preserveAspectRatio="none" aria-hidden="true"><rect class="svgb-10__raw" x="1" y="1" width="198" height="54"/></svg>
            <svg class="svgb-10__frame svgb-10__frame--true" viewBox="0 0 200 56" preserveAspectRatio="none" aria-hidden="true"><rect class="svgb-10__true" x="1" y="1" width="198" height="54" vector-effect="non-scaling-stroke"/></svg>
            <span class="svgb-10__seam" aria-hidden="true"></span>
            <span class="svgb-10__label" lang="ja">&#28961;&#26009;&#12487;&#12514;</span>
          </button>
        </li>
        <li class="svgb-10__row" dir="rtl">
          <span class="svgb-10__loc">ar</span>
          <button class="svgb-10__btn" type="button">
            <svg class="svgb-10__frame" viewBox="0 0 200 56" preserveAspectRatio="none" aria-hidden="true"><rect class="svgb-10__raw" x="1" y="1" width="198" height="54"/></svg>
            <svg class="svgb-10__frame svgb-10__frame--true" viewBox="0 0 200 56" preserveAspectRatio="none" aria-hidden="true"><rect class="svgb-10__true" x="1" y="1" width="198" height="54" vector-effect="non-scaling-stroke"/></svg>
            <span class="svgb-10__seam" aria-hidden="true"></span>
            <span class="svgb-10__label" lang="ar">&#1575;&#1576;&#1583;&#1571; &#1575;&#1604;&#1606;&#1587;&#1582;&#1577; &#1575;&#1604;&#1605;&#1580;&#1575;&#1606;&#1610;&#1577;</span>
          </button>
        </li>
        <li class="svgb-10__row">
          <span class="svgb-10__loc">live</span>
          <button class="svgb-10__btn svgb-10__btn--edit" type="button">
            <svg class="svgb-10__frame" viewBox="0 0 200 56" preserveAspectRatio="none" aria-hidden="true"><rect class="svgb-10__raw" x="1" y="1" width="198" height="54"/></svg>
            <svg class="svgb-10__frame svgb-10__frame--true" viewBox="0 0 200 56" preserveAspectRatio="none" aria-hidden="true"><rect class="svgb-10__true" x="1" y="1" width="198" height="54" vector-effect="non-scaling-stroke"/></svg>
            <span class="svgb-10__seam" aria-hidden="true"></span>
            <span class="svgb-10__label" contenteditable="true" spellcheck="false">Type to resize the frame</span>
          </button>
        </li>
      </ul>

      <div class="svgb-10__ab">
        <div class="svgb-10__abcell">
          <div class="svgb-10__wide">
            <svg class="svgb-10__vb" viewBox="0 0 200 56" preserveAspectRatio="none" aria-hidden="true">
              <rect class="svgb-10__vbline" x="2" y="2" width="196" height="52" rx="14" vector-effect="non-scaling-stroke"/>
            </svg>
            <span class="svgb-10__wl">non-scaling-stroke</span>
          </div>
          <code class="svgb-10__cap">even 2px on all four edges</code>
        </div>
        <div class="svgb-10__abcell">
          <div class="svgb-10__wide">
            <svg class="svgb-10__vb" viewBox="0 0 200 56" preserveAspectRatio="none" aria-hidden="true">
              <rect class="svgb-10__vbline svgb-10__vbline--raw" x="2" y="2" width="196" height="52" rx="14"/>
            </svg>
            <span class="svgb-10__wl">unprotected</span>
          </div>
          <code class="svgb-10__cap">uneven &middot; the more-scaled axis paints thicker</code>
        </div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter+Tight:wght@400;500;600&family=JetBrains+Mono:wght@400&display=swap');

.svgb-10 {
  --svgb-10-bg: #f7f5f0;
  --svgb-10-bg: oklch(0.972 0.008 90);
  --svgb-10-fg: #17161a;
  --svgb-10-fg: oklch(0.20 0.006 290);
  --svgb-10-muted: #6c6a75;
  --svgb-10-muted: oklch(0.555 0.012 290);
  --svgb-10-rest: rgba(23, 22, 26, 0.16);
  --svgb-10-rest: oklch(0.20 0.006 290 / 0.16);
  --svgb-10-stroke: #5b21f0;
  --svgb-10-stroke: oklch(0.46 0.26 295);
  --svgb-10-warn: #c4341f;
  --svgb-10-warn: oklch(0.53 0.19 32);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--svgb-10-bg);
  position: relative;
  color: var(--svgb-10-fg);
  font-family: 'Inter Tight', system-ui, sans-serif;
}

.svgb-10 *,
.svgb-10 *::before,
.svgb-10 *::after {
  box-sizing: border-box;
}

.svgb-10__stage {
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(22px, 5vw, 68px);
}

.svgb-10__sheet {
  width: 100%;
  max-width: 880px;
  display: flex;
  flex-direction: column;
  gap: clamp(20px, 3vw, 32px);
}

.svgb-10__kicker {
  margin: 0;
  font-family: 'Instrument Serif', ui-serif, Georgia, serif;
  font-size: clamp(22px, 3.6vw, 38px);
  font-style: italic;
  letter-spacing: -0.02em;
  line-height: 1.15;
}

.svgb-10__rows {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.svgb-10__row {
  display: flex;
  align-items: center;
  gap: 16px;
  padding-block: 4px;
  border-block-start: 1px solid var(--svgb-10-rest);
  padding-block-start: 14px;
}

.svgb-10__loc {
  flex: none;
  inline-size: 42px;
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-size: 10.5px;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--svgb-10-muted);
}

.svgb-10__btn {
  position: relative;
  display: inline-grid;
  place-items: center;
  min-inline-size: 92px;
  min-block-size: 56px;
  padding: 0 26px;
  border: 0;
  border-radius: 0;
  background: transparent;
  color: inherit;
  font: inherit;
  font-size: 15px;
  font-weight: 500;
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
}

.svgb-10__btn:focus-visible {
  outline: 2px solid var(--svgb-10-stroke);
  outline-offset: 3px;
}

.svgb-10__label {
  position: relative;
  z-index: 1;
  outline: none;
}

.svgb-10__btn--edit .svgb-10__label {
  min-inline-size: 4ch;
  caret-color: var(--svgb-10-stroke);
}

.svgb-10__frame {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  overflow: visible;
}

.svgb-10__frame rect {
  fill: none;
}
/* the resting edge is the UNPROTECTED stroke: one fixed viewBox stretched to the
   button's width, so the sides thin out as the label grows */

.svgb-10__raw {
  stroke: var(--svgb-10-rest);
  stroke-width: 2px;
  transition: stroke 240ms ease;
}

.svgb-10__btn:hover .svgb-10__raw,
.svgb-10__btn:focus-visible .svgb-10__raw {
  stroke: color-mix(in oklab, var(--svgb-10-warn) 45%, transparent);
}
/* hover wipes the corrected stroke across it — a clip-path reveal, not a dash draw,
   so what you watch is the line becoming even rather than becoming present */

.svgb-10__frame--true {
  clip-path: inset(0 100% 0 0);
  transition: clip-path 760ms cubic-bezier(0.22, 1, 0.36, 1);
}

.svgb-10__true {
  stroke: var(--svgb-10-stroke);
  stroke-width: 2px;
  vector-effect: non-scaling-stroke;
}
/* inset() is physical, so RTL needs its own resting edge or the reveal fights the seam */

[dir="rtl"] .svgb-10__frame--true {
  clip-path: inset(0 0 0 100%);
}

.svgb-10__btn:hover .svgb-10__frame--true,
.svgb-10__btn:focus-visible .svgb-10__frame--true {
  clip-path: inset(0 0 0 0);
}

.svgb-10__seam {
  position: absolute;
  inset-block: -4px;
  inline-size: 1.5px;
  inset-inline-start: 0;
  background: var(--svgb-10-stroke);
  opacity: 0;
  pointer-events: none;
}

.svgb-10__btn:hover .svgb-10__seam,
.svgb-10__btn:focus-visible .svgb-10__seam {
  animation: svgb-10-seam 760ms cubic-bezier(0.22, 1, 0.36, 1) forwards;
}

@keyframes svgb-10-seam {
  0% {
    inset-inline-start: 0;
    opacity: 0;
  }

  10% {
    opacity: 1;
  }

  86% {
    opacity: 1;
  }

  100% {
    inset-inline-start: 100%;
    opacity: 0;
  }
}

.svgb-10__ab {
  display: grid;
  gap: clamp(16px, 3vw, 28px);
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 280px), 1fr));
  padding-block-start: 6px;
  border-block-start: 1px solid var(--svgb-10-rest);
}

.svgb-10__abcell {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.svgb-10__wide {
  position: relative;
  display: grid;
  place-items: center;
  block-size: 88px;
}

.svgb-10__vb {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  overflow: visible;
}

.svgb-10__vbline {
  fill: none;
  stroke: var(--svgb-10-stroke);
  stroke-width: 2px;
}

.svgb-10__vbline--raw {
  stroke: #c4341f;
  stroke: oklch(0.53 0.19 32);
}

.svgb-10__wl {
  position: relative;
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-size: 12px;
}

.svgb-10__cap {
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-size: 11px;
  color: var(--svgb-10-muted);
}

.svgb-10__ti {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.svgb-10__toggle {
  position: absolute;
  z-index: 5;
  inset-block-start: 16px;
  inset-inline-end: 16px;
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border-radius: 999px;
  border: 1px solid color-mix(in oklab, currentColor 20%, transparent);
  background: color-mix(in oklab, currentColor 7%, transparent);
  color: inherit;
  cursor: pointer;
  transition: background 160ms ease, transform 160ms ease;
}

.svgb-10__toggle:hover {
  background: color-mix(in oklab, currentColor 14%, transparent);
}

.svgb-10__toggle:active {
  transform: scale(0.94);
}

.svgb-10__toggle svg {
  inline-size: 18px;
  block-size: 18px;
  transition: transform 400ms cubic-bezier(0.2, 0.7, 0.3, 1);
}

.svgb-10__ti:checked + .svgb-10__toggle svg {
  transform: rotate(180deg);
}

.svgb-10__ti:focus-visible + .svgb-10__toggle {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.svgb-10__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.svgb-10:has(#svgb-10-theme:checked) {
  --svgb-10-bg: #0f0e12;
  --svgb-10-bg: oklch(0.18 0.006 290);
  --svgb-10-fg: #f0eff4;
  --svgb-10-fg: oklch(0.96 0.004 290);
  --svgb-10-muted: #918f9c;
  --svgb-10-muted: oklch(0.68 0.012 290);
  --svgb-10-rest: rgba(240, 239, 244, 0.18);
  --svgb-10-rest: oklch(0.96 0.004 290 / 0.18);
  --svgb-10-stroke: #c4a8ff;
  --svgb-10-stroke: oklch(0.82 0.15 295);
}

.svgb-10:has(#svgb-10-theme:checked) .svgb-10__vbline--raw {
  stroke: oklch(0.75 0.16 32);
}

@media (prefers-reduced-motion: reduce) {
  .svgb-10__frame--true {
    transition: none;
  }

  .svgb-10__seam {
    display: none;
  }

  .svgb-10__toggle,
    .svgb-10__toggle svg {
    transition: none;
  }
}
```
