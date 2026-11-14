---
source: "codefronts"
url: "https://codefronts.com/components/css-svg-stroke-buttons/stroke-draw-button-that-reverses-on-mouse-leave/"
title: "Stroke Draw Button That Reverses on Mouse Leave"
section: "components"
category: "css-svg-stroke-buttons"
category_name: "CSS SVG Stroke Buttons"
description: "Three mechanical keycaps on a graphite deck, each wired to a different technique: the first reverses from wherever the pointer left it, the second is a…"
has_js: "false"
---

Here's a working CSS SVG Stroke Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Stroke Draw Button That Reverses on Mouse Leave
Source: https://codefronts.com/components/css-svg-stroke-buttons/stroke-draw-button-that-reverses-on-mouse-leave/

Three mechanical keycaps on a graphite deck, each wired to a different technique: the first reverses from wherever the pointer left it, the second is a keyframe animation that cannot and snaps back, the third draws in 300ms and retracts in 760ms because entry and exit timing are declared in different rules. Sweep the pointer across all three and the difference is physical.
## HTML
```html
<section class="svgb-08">
  <input class="svgb-08__ti" type="checkbox" id="svgb-08-theme">
  <label class="svgb-08__toggle" for="svgb-08-theme">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="svgb-08__sr">Switch colour scheme</span>
  </label>
  <div class="svgb-08__deck">
    <div class="svgb-08__row">
      <div class="svgb-08__slot">
        <button class="svgb-08__key svgb-08__key--sym" type="button">
          <svg class="svgb-08__frame" viewBox="0 0 132 132" aria-hidden="true">
            <rect class="svgb-08__base" x="2" y="2" width="128" height="128" rx="18" vector-effect="non-scaling-stroke"/>
            <rect class="svgb-08__ink" x="2" y="2" width="128" height="128" rx="18" vector-effect="non-scaling-stroke"/>
          </svg>
          <span class="svgb-08__face">
            <span class="svgb-08__glyph">&#8630;</span>
            <span class="svgb-08__legend">reverse</span>
          </span>
        </button>
        <span class="svgb-08__cap svgb-08__cap--ok">transition &middot; 520 / 520</span>
      </div>
      <div class="svgb-08__slot">
        <button class="svgb-08__key svgb-08__key--anim" type="button">
          <svg class="svgb-08__frame" viewBox="0 0 132 132" aria-hidden="true">
            <rect class="svgb-08__base" x="2" y="2" width="128" height="128" rx="18" vector-effect="non-scaling-stroke"/>
            <rect class="svgb-08__ink svgb-08__ink--anim" x="2" y="2" width="128" height="128" rx="18" vector-effect="non-scaling-stroke"/>
          </svg>
          <span class="svgb-08__face">
            <span class="svgb-08__glyph">&#9633;</span>
            <span class="svgb-08__legend">snap</span>
          </span>
        </button>
        <span class="svgb-08__cap svgb-08__cap--bad">keyframes &middot; no memory</span>
      </div>
      <div class="svgb-08__slot">
        <button class="svgb-08__key svgb-08__key--good" type="button">
          <svg class="svgb-08__frame" viewBox="0 0 132 132" aria-hidden="true">
            <rect class="svgb-08__base" x="2" y="2" width="128" height="128" rx="18" vector-effect="non-scaling-stroke"/>
            <rect class="svgb-08__ink svgb-08__ink--good" x="2" y="2" width="128" height="128" rx="18" vector-effect="non-scaling-stroke"/>
          </svg>
          <span class="svgb-08__face">
            <span class="svgb-08__glyph">&#8677;</span>
            <span class="svgb-08__legend">asym</span>
          </span>
        </button>
        <span class="svgb-08__cap svgb-08__cap--ok">300 in &middot; 760 out</span>
      </div>
    </div>
    <div class="svgb-08__plate">
      <span class="svgb-08__pk">interrupt a draw halfway &mdash; only a transition can walk it back</span>
    </div>
  </div>
</section>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap');

.svgb-08 {
  --svgb-08-bg: #17181b;
  --svgb-08-bg: oklch(0.225 0.004 250);
  --svgb-08-cap: #23252a;
  --svgb-08-cap: oklch(0.275 0.006 255);
  --svgb-08-fg: #e9ebee;
  --svgb-08-fg: oklch(0.94 0.004 250);
  --svgb-08-muted: #868b93;
  --svgb-08-muted: oklch(0.655 0.011 250);
  --svgb-08-rest: rgba(233, 235, 238, 0.14);
  --svgb-08-rest: oklch(0.94 0.004 250 / 0.14);
  --svgb-08-stroke: #c6ff4f;
  --svgb-08-stroke: oklch(0.92 0.20 122);
  --svgb-08-warn: #ff7a6b;
  --svgb-08-warn: oklch(0.75 0.16 30);
  --svgb-08-peri: 490;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--svgb-08-bg);
  color: var(--svgb-08-fg);
  font-family: 'Figtree', system-ui, sans-serif;
}

.svgb-08 *,
.svgb-08 *::before,
.svgb-08 *::after {
  box-sizing: border-box;
}

.svgb-08__deck {
  min-height: 100svh;
  display: grid;
  place-content: center;
  justify-items: center;
  gap: clamp(22px, 4vh, 40px);
  padding: clamp(20px, 5vw, 70px);
}

.svgb-08__row {
  display: flex;
  flex-wrap: wrap;
  gap: clamp(18px, 3vw, 34px);
  justify-content: center;
}

.svgb-08__slot {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 14px;
}

.svgb-08__key {
  position: relative;
  inline-size: 132px;
  block-size: 132px;
  display: grid;
  place-items: center;
  border: 0;
  padding: 0;
  border-radius: 18px;
  background: linear-gradient(180deg, color-mix(in oklab, var(--svgb-08-cap) 88%, #fff 12%), var(--svgb-08-cap));
  box-shadow: inset 0 1px 0 oklch(1 0 0 / 0.09), inset 0 -3px 0 oklch(0 0 0 / 0.35), 0 8px 0 color-mix(in oklab, var(--svgb-08-cap) 70%, #000), 0 18px 30px -14px oklch(0 0 0 / 0.7);
  color: inherit;
  font: inherit;
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
  transition: translate 120ms ease, box-shadow 120ms ease;
}

.svgb-08__key:active {
  translate: 0 5px;
  box-shadow: inset 0 1px 0 oklch(1 0 0 / 0.07), inset 0 -2px 0 oklch(0 0 0 / 0.3), 0 3px 0 color-mix(in oklab, var(--svgb-08-cap) 70%, #000), 0 8px 16px -10px oklch(0 0 0 / 0.7);
}

.svgb-08__key:focus-visible {
  outline: none;
  box-shadow: 0 0 0 3px color-mix(in oklab, var(--svgb-08-stroke) 40%, transparent), 0 8px 0 color-mix(in oklab, var(--svgb-08-cap) 70%, #000);
}

.svgb-08__face {
  position: relative;
  z-index: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
}

.svgb-08__glyph {
  font-size: 30px;
  line-height: 1;
  transition: color 300ms ease;
}

.svgb-08__legend {
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-size: 10.5px;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--svgb-08-muted);
}

.svgb-08__key:hover .svgb-08__glyph,
.svgb-08__key:focus-visible .svgb-08__glyph {
  color: var(--svgb-08-stroke);
}

.svgb-08__key--anim:hover .svgb-08__glyph,
.svgb-08__key--anim:focus-visible .svgb-08__glyph {
  color: var(--svgb-08-warn);
}

.svgb-08__frame {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  overflow: visible;
}

.svgb-08__frame rect {
  fill: none;
  stroke-linecap: round;
}

.svgb-08__base {
  stroke: var(--svgb-08-rest);
  stroke-width: 1.4px;
}

.svgb-08__ink {
  stroke: var(--svgb-08-stroke);
  stroke-width: 2.4px;
  stroke-dasharray: var(--svgb-08-peri);
  stroke-dashoffset: var(--svgb-08-peri);
}

.svgb-08__cap {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-size: 11px;
  color: var(--svgb-08-muted);
}

.svgb-08__cap::before {
  content: '';
  inline-size: 6px;
  block-size: 6px;
  border-radius: 50%;
  background: currentColor;
}

.svgb-08__cap--ok {
  color: color-mix(in oklab, var(--svgb-08-stroke) 62%, var(--svgb-08-muted));
}

.svgb-08__cap--bad {
  color: color-mix(in oklab, var(--svgb-08-warn) 62%, var(--svgb-08-muted));
}

.svgb-08__key--sym .svgb-08__ink {
  transition: stroke-dashoffset 520ms cubic-bezier(0.45, 0, 0.55, 1);
}

.svgb-08__key--sym:hover .svgb-08__ink,
.svgb-08__key--sym:focus-visible .svgb-08__ink {
  stroke-dashoffset: 0;
}

@keyframes svgb-08-draw {
  from {
    stroke-dashoffset: 490;
  }

  to {
    stroke-dashoffset: 0;
  }
}

.svgb-08__ink--anim {
  stroke: var(--svgb-08-warn);
}

.svgb-08__key--anim:hover .svgb-08__ink--anim,
.svgb-08__key--anim:focus-visible .svgb-08__ink--anim {
  animation: svgb-08-draw 520ms cubic-bezier(0.45, 0, 0.55, 1) forwards;
}

.svgb-08__ink--good {
  transition: stroke-dashoffset 760ms cubic-bezier(0.22, 1, 0.36, 1) 40ms;
}

.svgb-08__key--good:hover .svgb-08__ink--good,
.svgb-08__key--good:focus-visible .svgb-08__ink--good {
  stroke-dashoffset: 0;
  transition-duration: 300ms;
  transition-delay: 0ms;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
}

.svgb-08__plate {
  padding: 12px 18px;
  border-radius: 10px;
  background: color-mix(in oklab, var(--svgb-08-fg) 4%, transparent);
  border: 1px solid var(--svgb-08-rest);
}

.svgb-08__pk {
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-size: 11px;
  color: var(--svgb-08-muted);
}

.svgb-08__ti {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.svgb-08__toggle {
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

.svgb-08__toggle:hover {
  background: color-mix(in oklab, currentColor 14%, transparent);
}

.svgb-08__toggle:active {
  transform: scale(0.94);
}

.svgb-08__toggle svg {
  inline-size: 18px;
  block-size: 18px;
  transition: transform 400ms cubic-bezier(0.2, 0.7, 0.3, 1);
}

.svgb-08__ti:checked + .svgb-08__toggle svg {
  transform: rotate(180deg);
}

.svgb-08__ti:focus-visible + .svgb-08__toggle {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.svgb-08__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.svgb-08:has(#svgb-08-theme:checked) {
  --svgb-08-bg: #e8e9ec;
  --svgb-08-bg: oklch(0.935 0.004 250);
  --svgb-08-cap: #fbfbfc;
  --svgb-08-cap: oklch(0.985 0.002 250);
  --svgb-08-fg: #14171b;
  --svgb-08-fg: oklch(0.20 0.005 250);
  --svgb-08-muted: #5a6068;
  --svgb-08-muted: oklch(0.50 0.011 250);
  --svgb-08-rest: rgba(20, 23, 27, 0.16);
  --svgb-08-rest: oklch(0.20 0.005 250 / 0.16);
  --svgb-08-stroke: #3f6b00;
  --svgb-08-stroke: oklch(0.48 0.16 126);
  --svgb-08-warn: #b03a26;
  --svgb-08-warn: oklch(0.50 0.17 30);
}

.svgb-08:has(#svgb-08-theme:checked) .svgb-08__key {
  box-shadow: inset 0 1px 0 oklch(1 0 0 / 0.9), inset 0 -3px 0 oklch(0 0 0 / 0.08), 0 8px 0 color-mix(in oklab, var(--svgb-08-cap) 78%, #000 22%), 0 18px 30px -18px oklch(0 0 0 / 0.4);
}

@media (prefers-reduced-motion: reduce) {
  .svgb-08__ink {
    transition: none !important;
    animation: none !important;
    stroke-dasharray: none;
    stroke-dashoffset: 0;
    opacity: 0;
  }

  .svgb-08__key:hover .svgb-08__ink,
    .svgb-08__key:focus-visible .svgb-08__ink {
    opacity: 1;
  }

  .svgb-08__key,
    .svgb-08__glyph,
    .svgb-08__toggle,
    .svgb-08__toggle svg {
    transition: none;
  }
}
```
