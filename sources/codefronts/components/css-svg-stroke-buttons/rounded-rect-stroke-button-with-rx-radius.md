---
source: "codefronts"
url: "https://codefronts.com/components/css-svg-stroke-buttons/rounded-rect-stroke-button-with-rx-radius/"
title: "Rounded Rect Stroke Button with rx Radius"
section: "components"
category: "css-svg-stroke-buttons"
category_name: "CSS SVG Stroke Buttons"
description: "A radius inspector whose border is a contour sheet: all four candidate radii are drawn at once as faint outlines, so you can see that they share every…"
has_js: "false"
---

Here's a working CSS SVG Stroke Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Rounded Rect Stroke Button with rx Radius
Source: https://codefronts.com/components/css-svg-stroke-buttons/rounded-rect-stroke-button-with-rx-radius/

A radius inspector whose border is a contour sheet: all four candidate radii are drawn at once as faint outlines, so you can see that they share every straight edge and diverge only at the corners. Pick a value and that contour is the one that inks itself, with the perimeter arithmetic printed beside it and the active row highlighted. rx is driven as a CSS geometry property from a custom property, so the shape, the resting edge and the dash constant all change from one radio button — including the stadium case, where SVG's clamping rule is not the one CSS taught you.
## HTML
```html
<section class="svgb-05">
  <input class="svgb-05__ti" type="checkbox" id="svgb-05-theme">
  <label class="svgb-05__toggle" for="svgb-05-theme">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="svgb-05__sr">Switch colour scheme</span>
  </label>
  <div class="svgb-05__stage">
    <div class="svgb-05__panel">
      <div class="svgb-05__radios" role="radiogroup" aria-label="Corner radius">
        <input class="svgb-05__r svgb-05__r--0" type="radio" name="svgb-05-rx" id="svgb-05-rx0">
        <label class="svgb-05__seg svgb-05__seg--0" for="svgb-05-rx0">0</label>
        <input class="svgb-05__r svgb-05__r--8" type="radio" name="svgb-05-rx" id="svgb-05-rx8" checked>
        <label class="svgb-05__seg svgb-05__seg--8" for="svgb-05-rx8">8</label>
        <input class="svgb-05__r svgb-05__r--20" type="radio" name="svgb-05-rx" id="svgb-05-rx20">
        <label class="svgb-05__seg svgb-05__seg--20" for="svgb-05-rx20">20</label>
        <input class="svgb-05__r svgb-05__r--52" type="radio" name="svgb-05-rx" id="svgb-05-rx52">
        <label class="svgb-05__seg svgb-05__seg--52" for="svgb-05-rx52">52 = h/2</label>
      </div>

      <div class="svgb-05__bed">
        <span class="svgb-05__ruler" aria-hidden="true"></span>
        <button class="svgb-05__specimen" type="button">
          <svg class="svgb-05__frame" viewBox="0 0 360 104" aria-hidden="true">
            <rect class="svgb-05__ghost svgb-05__ghost--0" x="0" y="0" width="360" height="104"/>
            <rect class="svgb-05__ghost svgb-05__ghost--8" x="0" y="0" width="360" height="104"/>
            <rect class="svgb-05__ghost svgb-05__ghost--20" x="0" y="0" width="360" height="104"/>
            <rect class="svgb-05__ghost svgb-05__ghost--52" x="0" y="0" width="360" height="104"/>
            <rect class="svgb-05__base" x="0" y="0" width="360" height="104"/>
            <rect class="svgb-05__ink" x="0" y="0" width="360" height="104"/>
          </svg>
          <span class="svgb-05__label">Hover to draw</span>
        </button>
      </div>

      <dl class="svgb-05__table">
        <div class="svgb-05__tr svgb-05__tr--0"><dt>rx 0</dt><dd>2(360 + 104)</dd><dd class="svgb-05__val">928</dd></div>
        <div class="svgb-05__tr svgb-05__tr--8"><dt>rx 8</dt><dd>2(344) + 2(88) + 2&pi;(8)</dd><dd class="svgb-05__val">915</dd></div>
        <div class="svgb-05__tr svgb-05__tr--20"><dt>rx 20</dt><dd>2(320) + 2(64) + 2&pi;(20)</dd><dd class="svgb-05__val">894</dd></div>
        <div class="svgb-05__tr svgb-05__tr--52"><dt>rx 52</dt><dd>2(256) + &pi;(104)</dd><dd class="svgb-05__val">839</dd></div>
      </dl>
      <p class="svgb-05__warn"><span class="svgb-05__wtag">note</span> rx 999 is not a stadium in SVG &mdash; ry copies rx before clamping, so a 360&times;104 rect resolves to rx 180 / ry 52: an ellipse of about 785 units, not the 839-unit stadium.</p>
    </div>
  </div>
</section>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap');

.svgb-05 {
  --svgb-05-bg: #f4f4f6;
  --svgb-05-bg: oklch(0.962 0.003 300);
  --svgb-05-fg: #16161c;
  --svgb-05-fg: oklch(0.20 0.006 300);
  --svgb-05-muted: #62636f;
  --svgb-05-muted: oklch(0.525 0.012 300);
  --svgb-05-panel: #ffffff;
  --svgb-05-panel: oklch(1 0 0);
  --svgb-05-rest: rgba(22, 22, 28, 0.14);
  --svgb-05-rest: oklch(0.20 0.006 300 / 0.14);
  --svgb-05-stroke: #e5117a;
  --svgb-05-stroke: oklch(0.58 0.24 358);
  --svgb-05-rx: 8px;
  --svgb-05-peri: 915;
  --svgb-05-hlbg: color-mix(in oklab, var(--svgb-05-stroke) 10%, transparent);
  --svgb-05-hlfg: color-mix(in oklab, var(--svgb-05-stroke) 70%, var(--svgb-05-fg));
  --svgb-05-segsh: 0 1px 2px oklch(0 0 0 / 0.12);
  --svgb-05-dur: 720ms;
  --svgb-05-ease: cubic-bezier(0.16, 1, 0.3, 1);
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--svgb-05-bg);
  color: var(--svgb-05-fg);
  font-family: 'Outfit', system-ui, sans-serif;
}

.svgb-05 *,
.svgb-05 *::before,
.svgb-05 *::after {
  box-sizing: border-box;
}

.svgb-05__stage {
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(20px, 5vw, 64px);
}

.svgb-05__panel {
  width: 100%;
  max-width: 620px;
  display: flex;
  flex-direction: column;
  gap: clamp(18px, 3vw, 26px);
  padding: clamp(20px, 4vw, 34px);
  border-radius: 18px;
  background: var(--svgb-05-panel);
  box-shadow: 0 1px 2px oklch(0 0 0 / 0.05), 0 26px 60px -44px oklch(0 0 0 / 0.35);
}

.svgb-05__radios {
  display: flex;
  gap: 6px;
  padding: 5px;
  border-radius: 12px;
  background: color-mix(in oklab, var(--svgb-05-fg) 5%, transparent);
}

.svgb-05__r {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.svgb-05__seg {
  flex: 1;
  min-block-size: 40px;
  display: grid;
  place-items: center;
  border-radius: 9px;
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-size: 12.5px;
  color: var(--svgb-05-muted);
  cursor: pointer;
  transition: background 180ms ease, color 180ms ease;
}

.svgb-05__seg:hover {
  color: var(--svgb-05-fg);
}
/* the active pill and the active row are driven by inherited custom properties set on
   the root, not by :has() descendant rules — one invalidation point, no stale highlights */

.svgb-05__seg--0 {
  background: var(--svgb-05-sb-0, transparent);
  color: var(--svgb-05-sc-0, var(--svgb-05-muted));
  box-shadow: var(--svgb-05-ss-0, none);
}

.svgb-05__seg--8 {
  background: var(--svgb-05-sb-8, transparent);
  color: var(--svgb-05-sc-8, var(--svgb-05-muted));
  box-shadow: var(--svgb-05-ss-8, none);
}

.svgb-05__seg--20 {
  background: var(--svgb-05-sb-20, transparent);
  color: var(--svgb-05-sc-20, var(--svgb-05-muted));
  box-shadow: var(--svgb-05-ss-20, none);
}

.svgb-05__seg--52 {
  background: var(--svgb-05-sb-52, transparent);
  color: var(--svgb-05-sc-52, var(--svgb-05-muted));
  box-shadow: var(--svgb-05-ss-52, none);
}

.svgb-05__r:focus-visible + .svgb-05__seg {
  outline: 2px solid var(--svgb-05-stroke);
  outline-offset: 2px;
}

.svgb-05__bed {
  position: relative;
  display: grid;
  place-items: center;
  padding-block: clamp(18px, 4vw, 32px);
}

.svgb-05__ruler {
  position: absolute;
  inset-inline: 0;
  inset-block-start: 0;
  block-size: 100%;
  background: repeating-linear-gradient(90deg, var(--svgb-05-rest) 0 1px, transparent 1px 20px);
  mask-image: linear-gradient(#000 0 6px, transparent 6px calc(100% - 6px), #000 calc(100% - 6px));
  opacity: 0.7;
}

.svgb-05__specimen {
  position: relative;
  inline-size: min(360px, 100%);
  block-size: 104px;
  display: grid;
  place-items: center;
  border: 0;
  padding: 0;
  border-radius: var(--svgb-05-rx);
  background: color-mix(in oklab, var(--svgb-05-stroke) 6%, transparent);
  box-shadow: inset 0 0 0 1px var(--svgb-05-rest);
  color: inherit;
  font: inherit;
  font-size: 16px;
  font-weight: 500;
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
  transition: border-radius 420ms var(--svgb-05-ease);
}

.svgb-05__specimen:focus-visible {
  outline: 2px solid var(--svgb-05-stroke);
  outline-offset: 4px;
}

.svgb-05__label {
  position: relative;
  z-index: 1;
}

.svgb-05__frame {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  overflow: visible;
}

.svgb-05__frame rect {
  fill: none;
  rx: var(--svgb-05-rx);
  transition: rx 420ms var(--svgb-05-ease);
}

.svgb-05__base {
  stroke: var(--svgb-05-rest);
  stroke-width: 1.5px;
}

.svgb-05__ink {
  stroke: var(--svgb-05-stroke);
  stroke-width: 2.4px;
  stroke-linecap: butt;
  stroke-dasharray: var(--svgb-05-peri);
  stroke-dashoffset: var(--svgb-05-peri);
  transition: rx 420ms var(--svgb-05-ease), stroke-dashoffset var(--svgb-05-dur) var(--svgb-05-ease);
}

.svgb-05__specimen:hover .svgb-05__ink,
.svgb-05__specimen:focus-visible .svgb-05__ink {
  stroke-dashoffset: 0;
}

.svgb-05:has(.svgb-05__r--0:checked) {
  --svgb-05-rx: 0px;
  --svgb-05-peri: 928;
  --svgb-05-hl-0: var(--svgb-05-hlbg);
  --svgb-05-hc-0: var(--svgb-05-hlfg);
  --svgb-05-sb-0: var(--svgb-05-panel);
  --svgb-05-sc-0: var(--svgb-05-fg);
  --svgb-05-ss-0: var(--svgb-05-segsh);
}

.svgb-05:has(.svgb-05__r--8:checked) {
  --svgb-05-rx: 8px;
  --svgb-05-peri: 915;
  --svgb-05-hl-8: var(--svgb-05-hlbg);
  --svgb-05-hc-8: var(--svgb-05-hlfg);
  --svgb-05-sb-8: var(--svgb-05-panel);
  --svgb-05-sc-8: var(--svgb-05-fg);
  --svgb-05-ss-8: var(--svgb-05-segsh);
}

.svgb-05:has(.svgb-05__r--20:checked) {
  --svgb-05-rx: 20px;
  --svgb-05-peri: 894;
  --svgb-05-hl-20: var(--svgb-05-hlbg);
  --svgb-05-hc-20: var(--svgb-05-hlfg);
  --svgb-05-sb-20: var(--svgb-05-panel);
  --svgb-05-sc-20: var(--svgb-05-fg);
  --svgb-05-ss-20: var(--svgb-05-segsh);
}

.svgb-05:has(.svgb-05__r--52:checked) {
  --svgb-05-rx: 52px;
  --svgb-05-peri: 839;
  --svgb-05-hl-52: var(--svgb-05-hlbg);
  --svgb-05-hc-52: var(--svgb-05-hlfg);
  --svgb-05-sb-52: var(--svgb-05-panel);
  --svgb-05-sc-52: var(--svgb-05-fg);
  --svgb-05-ss-52: var(--svgb-05-segsh);
}
/* every radius on screen at once: the contours only diverge at the corners */

.svgb-05__frame .svgb-05__ghost {
  stroke: var(--svgb-05-rest);
  stroke-width: 1px;
  opacity: 0.4;
}

.svgb-05__frame .svgb-05__ghost--0 {
  rx: 0px;
}

.svgb-05__frame .svgb-05__ghost--8 {
  rx: 8px;
}

.svgb-05__frame .svgb-05__ghost--20 {
  rx: 20px;
}

.svgb-05__frame .svgb-05__ghost--52 {
  rx: 52px;
}

.svgb-05:has(.svgb-05__r--0:checked) .svgb-05__ghost--0,
.svgb-05:has(.svgb-05__r--8:checked) .svgb-05__ghost--8,
.svgb-05:has(.svgb-05__r--20:checked) .svgb-05__ghost--20,
.svgb-05:has(.svgb-05__r--52:checked) .svgb-05__ghost--52 {
  opacity: 0;
}

.svgb-05__table {
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.svgb-05__tr {
  display: grid;
  grid-template-columns: 62px 1fr auto;
  gap: 12px;
  align-items: center;
  padding: 9px 12px;
  border-radius: 8px;
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-size: 11.5px;
  transition: background 200ms ease, color 200ms ease;
}

.svgb-05__tr dt,
.svgb-05__tr dd {
  margin: 0;
}

.svgb-05__val {
  font-variant-numeric: tabular-nums;
}

.svgb-05__tr--0 {
  background: var(--svgb-05-hl-0, transparent);
  color: var(--svgb-05-hc-0, var(--svgb-05-muted));
}

.svgb-05__tr--8 {
  background: var(--svgb-05-hl-8, transparent);
  color: var(--svgb-05-hc-8, var(--svgb-05-muted));
}

.svgb-05__tr--20 {
  background: var(--svgb-05-hl-20, transparent);
  color: var(--svgb-05-hc-20, var(--svgb-05-muted));
}

.svgb-05__tr--52 {
  background: var(--svgb-05-hl-52, transparent);
  color: var(--svgb-05-hc-52, var(--svgb-05-muted));
}

.svgb-05__warn {
  margin: 0;
  display: flex;
  gap: 9px;
  align-items: baseline;
  font-size: 12.5px;
  line-height: 1.5;
  color: var(--svgb-05-muted);
}

.svgb-05__wtag {
  flex: none;
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-size: 10px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  padding: 3px 7px;
  border-radius: 5px;
  background: color-mix(in oklab, var(--svgb-05-fg) 8%, transparent);
}

.svgb-05__ti {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.svgb-05__toggle {
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

.svgb-05__toggle:hover {
  background: color-mix(in oklab, currentColor 14%, transparent);
}

.svgb-05__toggle:active {
  transform: scale(0.94);
}

.svgb-05__toggle svg {
  inline-size: 18px;
  block-size: 18px;
  transition: transform 400ms cubic-bezier(0.2, 0.7, 0.3, 1);
}

.svgb-05__ti:checked + .svgb-05__toggle svg {
  transform: rotate(180deg);
}

.svgb-05__ti:focus-visible + .svgb-05__toggle {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.svgb-05__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.svgb-05:has(#svgb-05-theme:checked) {
  --svgb-05-bg: #0d0d11;
  --svgb-05-bg: oklch(0.175 0.006 300);
  --svgb-05-fg: #eeeef3;
  --svgb-05-fg: oklch(0.955 0.004 300);
  --svgb-05-muted: #8d8e9b;
  --svgb-05-muted: oklch(0.675 0.012 300);
  --svgb-05-panel: #16161d;
  --svgb-05-panel: oklch(0.222 0.009 300);
  --svgb-05-rest: rgba(238, 238, 243, 0.16);
  --svgb-05-rest: oklch(0.955 0.004 300 / 0.16);
  --svgb-05-stroke: #ff7ac0;
  --svgb-05-stroke: oklch(0.79 0.17 355);
}

.svgb-05:has(#svgb-05-theme:checked) .svgb-05__panel {
  box-shadow: inset 0 1px 0 oklch(1 0 0 / 0.05), 0 30px 70px -46px oklch(0 0 0 / 0.85);
}

@media (prefers-reduced-motion: reduce) {
  .svgb-05__ink,
    .svgb-05__frame rect,
    .svgb-05__specimen,
    .svgb-05__seg,
    .svgb-05__tr {
    transition: none;
  }

  .svgb-05__ink {
    stroke-dasharray: none;
    stroke-dashoffset: 0;
    opacity: 0;
  }

  .svgb-05__specimen:hover .svgb-05__ink,
    .svgb-05__specimen:focus-visible .svgb-05__ink {
    opacity: 1;
  }

  .svgb-05__toggle,
    .svgb-05__toggle svg {
    transition: none;
  }
}
```
