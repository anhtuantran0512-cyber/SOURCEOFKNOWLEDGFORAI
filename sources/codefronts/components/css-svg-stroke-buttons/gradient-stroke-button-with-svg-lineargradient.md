---
source: "codefronts"
url: "https://codefronts.com/components/css-svg-stroke-buttons/gradient-stroke-button-with-svg-lineargradient/"
title: "Gradient Stroke Button with SVG linearGradient"
section: "components"
category: "css-svg-stroke-buttons"
category_name: "CSS SVG Stroke Buttons"
description: "A festival poster where the ticket CTA is the only lit object on the page: a wave-edged ribbon &mdash; no rect, no rx, a single closed path of eight…"
has_js: "false"
---

Here's a working CSS SVG Stroke Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Gradient Stroke Button with SVG linearGradient
Source: https://codefronts.com/components/css-svg-stroke-buttons/gradient-stroke-button-with-svg-lineargradient/

A festival poster where the ticket CTA is the only lit object on the page: a wave-edged ribbon &mdash; no rect, no rx, a single closed path of eight quadratic crests per edge &mdash; whose stroke is a three-stop linearGradient in user space, hue-cycling through its own stops while the dash reveals it. One attribute — stroke="url(#id)" — replaces every background-clip gradient-border hack, and the two traps it brings with it are both on display.
## HTML
```html
<section class="svgb-07">
  <input class="svgb-07__ti" type="checkbox" id="svgb-07-theme">
  <label class="svgb-07__toggle" for="svgb-07-theme">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="svgb-07__sr">Switch colour scheme</span>
  </label>
  <img class="svgb-07__bgimg" src="https://picsum.photos/seed/svgb07crowd/1600/1100" alt="" width="1600" height="1100" loading="lazy" decoding="async">
  <div class="svgb-07__poster">
    <div class="svgb-07__meta">
      <span>Pier 44 &middot; Rotterdam</span>
      <span>19 &mdash; 21 June</span>
    </div>
    <h1 class="svgb-07__name">Chroma<span>Nights</span></h1>
    <p class="svgb-07__bill">Aurelia &middot; K&aacute;rmen &middot; Low Static &middot; Nadir &middot; Volta Kids &middot; Sonnet 8</p>
    <div class="svgb-07__cta">
      <button class="svgb-07__btn" type="button">
        <svg class="svgb-07__frame" viewBox="0 0 300 72" aria-hidden="true">
          <defs>
            <linearGradient id="svgb-07-grad" gradientUnits="userSpaceOnUse" x1="0" y1="72" x2="300" y2="0">
              <stop class="svgb-07-s1" offset="0"/>
              <stop class="svgb-07-s2" offset="0.5"/>
              <stop class="svgb-07-s3" offset="1"/>
            </linearGradient>
          </defs>
          <path class="svgb-07__base" d="M14 14q8.5 -16 17 0q8.5 16 17 0q8.5 -16 17 0q8.5 16 17 0q8.5 -16 17 0q8.5 16 17 0q8.5 -16 17 0q8.5 16 17 0q8.5 -16 17 0q8.5 16 17 0q8.5 -16 17 0q8.5 16 17 0q8.5 -16 17 0q8.5 16 17 0q8.5 -16 17 0q8.5 16 17 0C300 24 300 48 286 58q-8.5 16 -17 0q-8.5 -16 -17 0q-8.5 16 -17 0q-8.5 -16 -17 0q-8.5 16 -17 0q-8.5 -16 -17 0q-8.5 16 -17 0q-8.5 -16 -17 0q-8.5 16 -17 0q-8.5 -16 -17 0q-8.5 16 -17 0q-8.5 -16 -17 0q-8.5 16 -17 0q-8.5 -16 -17 0q-8.5 16 -17 0q-8.5 -16 -17 0C0 48 0 24 14 14Z" pathLength="1" vector-effect="non-scaling-stroke"/>
          <path class="svgb-07__ink" d="M14 14q8.5 -16 17 0q8.5 16 17 0q8.5 -16 17 0q8.5 16 17 0q8.5 -16 17 0q8.5 16 17 0q8.5 -16 17 0q8.5 16 17 0q8.5 -16 17 0q8.5 16 17 0q8.5 -16 17 0q8.5 16 17 0q8.5 -16 17 0q8.5 16 17 0q8.5 -16 17 0q8.5 16 17 0C300 24 300 48 286 58q-8.5 16 -17 0q-8.5 -16 -17 0q-8.5 16 -17 0q-8.5 -16 -17 0q-8.5 16 -17 0q-8.5 -16 -17 0q-8.5 16 -17 0q-8.5 -16 -17 0q-8.5 16 -17 0q-8.5 -16 -17 0q-8.5 16 -17 0q-8.5 -16 -17 0q-8.5 16 -17 0q-8.5 -16 -17 0q-8.5 16 -17 0q-8.5 -16 -17 0C0 48 0 24 14 14Z" pathLength="1" vector-effect="non-scaling-stroke"/>
        </svg>
        <span class="svgb-07__label">Three-day pass &mdash; &euro;89</span>
      </button>
      <button class="svgb-07__badge" type="button" aria-label="Play the lineup mix">
        <svg class="svgb-07__bframe" viewBox="0 0 72 72" aria-hidden="true">
          <path class="svgb-07__base" d="M36.00 6.00A18 18 0 0 1 53.63 11.73A18 18 0 0 1 64.53 26.73A18 18 0 0 1 64.53 45.27A18 18 0 0 1 53.63 60.27A18 18 0 0 1 36.00 66.00A18 18 0 0 1 18.37 60.27A18 18 0 0 1 7.47 45.27A18 18 0 0 1 7.47 26.73A18 18 0 0 1 18.37 11.73A18 18 0 0 1 36.00 6.00Z" pathLength="1" vector-effect="non-scaling-stroke"/>
          <path class="svgb-07__bink" d="M36.00 6.00A18 18 0 0 1 53.63 11.73A18 18 0 0 1 64.53 26.73A18 18 0 0 1 64.53 45.27A18 18 0 0 1 53.63 60.27A18 18 0 0 1 36.00 66.00A18 18 0 0 1 18.37 60.27A18 18 0 0 1 7.47 45.27A18 18 0 0 1 7.47 26.73A18 18 0 0 1 18.37 11.73A18 18 0 0 1 36.00 6.00Z" pathLength="1" vector-effect="non-scaling-stroke"/>
        </svg>
        <svg class="svgb-07__play" viewBox="0 0 24 24" aria-hidden="true"><path d="M9.5 7 17 12l-7.5 5Z"/></svg>
      </button>
    </div>
  </div>
</section>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,[email protected],400;12..96,800&family=IBM+Plex+Mono:wght@400;500&display=swap');

.svgb-07 {
  --svgb-07-bg: #07070c;
  --svgb-07-bg: oklch(0.14 0.01 285);
  --svgb-07-fg: #f4f2f8;
  --svgb-07-fg: oklch(0.965 0.006 285);
  --svgb-07-muted: #a49fb4;
  --svgb-07-muted: oklch(0.72 0.02 290);
  --svgb-07-rest: rgba(244, 242, 248, 0.22);
  --svgb-07-rest: oklch(0.965 0.006 285 / 0.22);
  --svgb-07-a: #ff5db1;
  --svgb-07-a: oklch(0.72 0.22 350);
  --svgb-07-b: #7b5cff;
  --svgb-07-b: oklch(0.60 0.24 290);
  --svgb-07-c: #35e8c5;
  --svgb-07-c: oklch(0.85 0.15 175);
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--svgb-07-bg);
  color: var(--svgb-07-fg);
  font-family: 'Bricolage Grotesque', system-ui, sans-serif;
  overflow: hidden;
  isolation: isolate;
}

.svgb-07 *,
.svgb-07 *::before,
.svgb-07 *::after {
  box-sizing: border-box;
}

.svgb-07__bgimg {
  position: absolute;
  inset: 0;
  z-index: -2;
  inline-size: 100%;
  block-size: 100%;
  object-fit: cover;
  opacity: 0.34;
  filter: grayscale(1) contrast(1.25);
}

.svgb-07::before {
  content: '';
  position: absolute;
  inset: 0;
  z-index: -1;
  pointer-events: none;
  background: radial-gradient(70% 50% at 20% 15%, color-mix(in oklab, var(--svgb-07-b) 34%, transparent), transparent 62%), radial-gradient(60% 50% at 85% 85%, color-mix(in oklab, var(--svgb-07-a) 26%, transparent), transparent 62%), linear-gradient(180deg, transparent 40%, var(--svgb-07-bg));
}

.svgb-07__poster {
  position: relative;
  min-height: 100svh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: clamp(14px, 2.5vw, 26px);
  padding: clamp(24px, 6vw, 84px);
  max-width: 1200px;
  margin-inline: auto;
}

.svgb-07__meta {
  display: flex;
  flex-wrap: wrap;
  gap: 8px 26px;
  font-family: 'IBM Plex Mono', ui-monospace, monospace;
  font-size: 11.5px;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--svgb-07-muted);
}

.svgb-07__name {
  margin: 0;
  font-size: clamp(58px, 16vw, 200px);
  font-weight: 800;
  line-height: 0.82;
  letter-spacing: -0.055em;
  text-transform: uppercase;
}

.svgb-07__name span {
  display: block;
  color: transparent;
  -webkit-text-stroke: 1.5px var(--svgb-07-fg);
  padding-inline-start: 0.12em;
}

.svgb-07__bill {
  margin: 0 0 clamp(8px, 2vw, 16px);
  max-width: 46ch;
  font-size: clamp(14px, 1.6vw, 18px);
  line-height: 1.6;
  color: var(--svgb-07-muted);
}

.svgb-07__cta {
  display: flex;
  flex-wrap: wrap;
  gap: 18px;
  align-items: center;
}

.svgb-07__btn {
  position: relative;
  inline-size: min(300px, 88vw);
  block-size: 72px;
  display: grid;
  place-items: center;
  border: 0;
  padding: 0;
  border-radius: 999px;
  background: transparent;
  color: inherit;
  font: inherit;
  font-size: 15.5px;
  font-weight: 400;
  letter-spacing: 0.01em;
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
}

.svgb-07__label {
  position: relative;
  z-index: 1;
}

.svgb-07__btn:focus-visible,
.svgb-07__badge:focus-visible {
  outline: none;
  box-shadow: 0 0 0 3px color-mix(in oklab, var(--svgb-07-c) 55%, transparent);
}

.svgb-07__frame,
.svgb-07__bframe {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  overflow: visible;
}

.svgb-07__frame path,
.svgb-07__bframe path {
  fill: none;
  stroke-linejoin: round;
  stroke-linecap: round;
}

.svgb-07__frame .svgb-07__base,
.svgb-07__bframe .svgb-07__base {
  stroke: var(--svgb-07-rest);
  stroke-width: 1.4px;
  fill: oklch(1 0 0 / 0.05);
}

.svgb-07:has(#svgb-07-theme:checked) .svgb-07__base {
  fill: oklch(0 0 0 / 0.04);
}

.svgb-07__ink {
  stroke: url(#svgb-07-grad);
  stroke-width: 2.6px;
  stroke-linecap: round;
  stroke-dasharray: 1;
  stroke-dashoffset: 1;
  transition: stroke-dashoffset 980ms cubic-bezier(0.16, 1, 0.3, 1);
  filter: drop-shadow(0 0 10px color-mix(in oklab, var(--svgb-07-b) 55%, transparent));
}

.svgb-07__btn:hover .svgb-07__ink,
.svgb-07__btn:focus-visible .svgb-07__ink {
  stroke-dashoffset: 0;
}

.svgb-07__badge {
  position: relative;
  inline-size: 72px;
  block-size: 72px;
  display: grid;
  place-items: center;
  border: 0;
  padding: 0;
  border-radius: 50%;
  background: transparent;
  color: inherit;
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
}

.svgb-07__bink {
  stroke: url(#svgb-07-grad);
  stroke-width: 2.6px;
  stroke-linecap: round;
  stroke-dasharray: 1;
  stroke-dashoffset: 1;
  transition: stroke-dashoffset 700ms cubic-bezier(0.16, 1, 0.3, 1);
}

.svgb-07__badge:hover .svgb-07__bink,
.svgb-07__badge:focus-visible .svgb-07__bink {
  stroke-dashoffset: 0;
}

.svgb-07__play {
  position: relative;
  z-index: 1;
  inline-size: 22px;
  block-size: 22px;
  fill: var(--svgb-07-fg);
}

.svgb-07-s1 {
  stop-color: #ff5db1;
  stop-color: var(--svgb-07-a);
  animation: svgb-07-cyc 7s linear infinite;
}

.svgb-07-s2 {
  stop-color: #7b5cff;
  stop-color: var(--svgb-07-b);
  animation: svgb-07-cyc 7s linear infinite -2.33s;
}

.svgb-07-s3 {
  stop-color: #35e8c5;
  stop-color: var(--svgb-07-c);
  animation: svgb-07-cyc 7s linear infinite -4.66s;
}

@keyframes svgb-07-cyc {
  0% {
    stop-color: oklch(0.72 0.22 350);
  }

  33% {
    stop-color: oklch(0.60 0.24 290);
  }

  66% {
    stop-color: oklch(0.85 0.15 175);
  }

  100% {
    stop-color: oklch(0.72 0.22 350);
  }
}

.svgb-07__ti {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.svgb-07__toggle {
  position: absolute;
  z-index: 5;
  inset-block-start: 16px;
  inset-inline-end: 16px;
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border-radius: 999px;
  border: 1px solid color-mix(in oklab, currentColor 22%, transparent);
  background: color-mix(in oklab, currentColor 10%, transparent);
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
  color: inherit;
  cursor: pointer;
  transition: background 160ms ease, transform 160ms ease;
}

.svgb-07__toggle:hover {
  background: color-mix(in oklab, currentColor 16%, transparent);
}

.svgb-07__toggle:active {
  transform: scale(0.94);
}

.svgb-07__toggle svg {
  inline-size: 18px;
  block-size: 18px;
  transition: transform 400ms cubic-bezier(0.2, 0.7, 0.3, 1);
}

.svgb-07__ti:checked + .svgb-07__toggle svg {
  transform: rotate(180deg);
}

.svgb-07__ti:focus-visible + .svgb-07__toggle {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.svgb-07__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.svgb-07:has(#svgb-07-theme:checked) {
  --svgb-07-bg: #f3f1f7;
  --svgb-07-bg: oklch(0.955 0.006 285);
  --svgb-07-fg: #121017;
  --svgb-07-fg: oklch(0.185 0.012 285);
  --svgb-07-muted: #565064;
  --svgb-07-muted: oklch(0.49 0.022 290);
  --svgb-07-rest: rgba(18, 16, 23, 0.2);
  --svgb-07-rest: oklch(0.185 0.012 285 / 0.2);
  --svgb-07-a: #b3006b;
  --svgb-07-a: oklch(0.48 0.22 355);
  --svgb-07-b: #3f27c8;
  --svgb-07-b: oklch(0.40 0.22 288);
  --svgb-07-c: #00705f;
  --svgb-07-c: oklch(0.46 0.10 175);
}

.svgb-07:has(#svgb-07-theme:checked) .svgb-07__bgimg {
  opacity: 0.16;
  filter: grayscale(1) contrast(1.1);
}

.svgb-07:has(#svgb-07-theme:checked) .svgb-07__name span {
  -webkit-text-stroke-color: var(--svgb-07-fg);
}

.svgb-07:has(#svgb-07-theme:checked) .svgb-07-s1,
.svgb-07:has(#svgb-07-theme:checked) .svgb-07-s2,
.svgb-07:has(#svgb-07-theme:checked) .svgb-07-s3 {
  animation-name: svgb-07-cyc-light;
}

@keyframes svgb-07-cyc-light {
  0% {
    stop-color: oklch(0.48 0.22 355);
  }

  33% {
    stop-color: oklch(0.40 0.22 288);
  }

  66% {
    stop-color: oklch(0.46 0.10 175);
  }

  100% {
    stop-color: oklch(0.48 0.22 355);
  }
}

@media (prefers-reduced-motion: reduce) {
  .svgb-07-s1,
    .svgb-07-s2,
    .svgb-07-s3 {
    animation: none;
  }

  .svgb-07__ink,
    .svgb-07__bink {
    transition: none;
    stroke-dasharray: none;
    stroke-dashoffset: 0;
    opacity: 0;
  }

  .svgb-07__btn:hover .svgb-07__ink,
    .svgb-07__btn:focus-visible .svgb-07__ink,
    .svgb-07__badge:hover .svgb-07__bink,
    .svgb-07__badge:focus-visible .svgb-07__bink {
    opacity: 1;
  }

  .svgb-07__toggle,
    .svgb-07__toggle svg {
    transition: none;
  }
}
```
