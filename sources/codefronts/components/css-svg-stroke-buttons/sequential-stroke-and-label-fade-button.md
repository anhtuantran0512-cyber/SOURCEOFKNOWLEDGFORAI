---
source: "codefronts"
url: "https://codefronts.com/components/css-svg-stroke-buttons/sequential-stroke-and-label-fade-button/"
title: "Sequential Stroke and Label Fade Button"
section: "components"
category: "css-svg-stroke-buttons"
category_name: "CSS SVG Stroke Buttons"
description: "An engraved invitation, choreographed in four beats: the outer rule draws, the inner rule follows it in, the serif line fades up and opens its…"
has_js: "false"
---

Here's a working CSS SVG Stroke Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sequential Stroke and Label Fade Button
Source: https://codefronts.com/components/css-svg-stroke-buttons/sequential-stroke-and-label-fade-button/

An engraved invitation, choreographed in four beats: the outer rule draws, the inner rule follows it in, the serif line fades up and opens its letter-spacing, and the seal mark lands last. Leave the card and the sequence rewinds — seal, text, inner, outer — because the exit delays are declared separately and run faster than the entrance.
## HTML
```html
<section class="svgb-13">
  <input class="svgb-13__ti" type="checkbox" id="svgb-13-theme">
  <label class="svgb-13__toggle" for="svgb-13-theme">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="svgb-13__sr">Switch colour scheme</span>
  </label>
  <div class="svgb-13__stage">
    <div class="svgb-13__col">
      <p class="svgb-13__house">Maison Verrier &middot; Est. 1904</p>
      <button class="svgb-13__card" type="button">
        <svg class="svgb-13__frame" viewBox="0 0 420 200" aria-hidden="true">
          <rect class="svgb-13__base" x="2" y="2" width="416" height="196" pathLength="1"/>
          <rect class="svgb-13__base" x="16" y="16" width="388" height="168" pathLength="1"/>
          <rect class="svgb-13__outer" x="2" y="2" width="416" height="196" pathLength="1"/>
          <rect class="svgb-13__inner" x="16" y="16" width="388" height="168" pathLength="1"/>
        </svg>
        <span class="svgb-13__body">
          <span class="svgb-13__eyebrow">Private view</span>
          <span class="svgb-13__text">The Glass Hours</span>
          <span class="svgb-13__sub">Thursday, 12 November &middot; 19:00</span>
          <span class="svgb-13__seal" aria-hidden="true">
            <svg viewBox="0 0 40 40" aria-hidden="true">
              <circle class="svgb-13__sealring" cx="20" cy="20" r="17" pathLength="1"/>
              <path class="svgb-13__sealmark" d="M13 21.5 18 26.5 27.5 14" pathLength="1"/>
            </svg>
            <span class="svgb-13__rsvp">RSVP</span>
          </span>
        </span>
      </button>
      <button class="svgb-13__card svgb-13__card--quick" type="button">
        <svg class="svgb-13__frame" viewBox="0 0 420 200" aria-hidden="true">
          <rect class="svgb-13__base" x="2" y="2" width="416" height="196" pathLength="1"/>
          <rect class="svgb-13__base" x="16" y="16" width="388" height="168" pathLength="1"/>
          <rect class="svgb-13__outer" x="2" y="2" width="416" height="196" pathLength="1"/>
          <rect class="svgb-13__inner" x="16" y="16" width="388" height="168" pathLength="1"/>
        </svg>
        <span class="svgb-13__body">
          <span class="svgb-13__eyebrow">Two-beat version</span>
          <span class="svgb-13__text">Waiting list</span>
          <span class="svgb-13__sub">Frames together &middot; text at 200ms</span>
          <span class="svgb-13__seal" aria-hidden="true">
            <svg viewBox="0 0 40 40" aria-hidden="true">
              <circle class="svgb-13__sealring" cx="20" cy="20" r="17" pathLength="1"/>
              <path class="svgb-13__sealmark" d="M13 21.5 18 26.5 27.5 14" pathLength="1"/>
            </svg>
            <span class="svgb-13__rsvp">Join</span>
          </span>
        </span>
      </button>
    </div>
  </div>
</section>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;600&family=Manrope:wght@400;500;600&display=swap');

.svgb-13 {
  --svgb-13-bg: #100e0a;
  --svgb-13-bg: oklch(0.175 0.012 70);
  --svgb-13-fg: #f4eee1;
  --svgb-13-fg: oklch(0.95 0.02 85);
  --svgb-13-muted: #a2967f;
  --svgb-13-muted: oklch(0.68 0.028 80);
  --svgb-13-rest: rgba(244, 238, 225, 0.14);
  --svgb-13-rest: oklch(0.95 0.02 85 / 0.14);
  --svgb-13-stroke: #d9b26a;
  --svgb-13-stroke: oklch(0.79 0.10 82);
  --svgb-13-step: 130ms;
  --svgb-13-dur: 460ms;
  --svgb-13-ease: cubic-bezier(0.22, 1, 0.36, 1);
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--svgb-13-bg);
  color: var(--svgb-13-fg);
  font-family: 'Manrope', system-ui, sans-serif;
}

.svgb-13 *,
.svgb-13 *::before,
.svgb-13 *::after {
  box-sizing: border-box;
}

.svgb-13::before {
  content: '';
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: radial-gradient(60% 50% at 50% 30%, color-mix(in oklab, var(--svgb-13-stroke) 9%, transparent), transparent 70%);
}

.svgb-13__stage {
  position: relative;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(22px, 5vw, 70px);
}

.svgb-13__col {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: clamp(18px, 3vw, 30px);
}

.svgb-13__house {
  margin: 0;
  font-family: 'Cormorant Garamond', ui-serif, Georgia, serif;
  font-size: 13px;
  letter-spacing: 0.42em;
  text-transform: uppercase;
  color: var(--svgb-13-muted);
}

.svgb-13__card {
  position: relative;
  inline-size: min(420px, 92vw);
  block-size: 200px;
  display: grid;
  place-items: center;
  border: 0;
  padding: 0;
  border-radius: 0;
  background: color-mix(in oklab, var(--svgb-13-fg) 3%, transparent);
  color: inherit;
  font: inherit;
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
}

.svgb-13__card:focus-visible {
  outline: 1px solid var(--svgb-13-stroke);
  outline-offset: 8px;
}

.svgb-13__frame {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  overflow: visible;
}

.svgb-13__frame rect {
  fill: none;
}

.svgb-13__base {
  stroke: var(--svgb-13-rest);
  stroke-width: 1px;
}

.svgb-13__outer,
.svgb-13__inner {
  stroke: var(--svgb-13-stroke);
  stroke-dasharray: 1;
  stroke-dashoffset: 1;
  transition: stroke-dashoffset 620ms var(--svgb-13-ease);
}

.svgb-13__outer {
  stroke-width: 1.6px;
  transition-delay: calc(var(--svgb-13-step) * 1.6);
}

.svgb-13__inner {
  stroke-width: 0.9px;
  transition-delay: calc(var(--svgb-13-step) * 1.2);
}

.svgb-13__body {
  position: relative;
  z-index: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  padding: 0 40px;
  text-align: center;
}

.svgb-13__eyebrow {
  font-size: 9.5px;
  letter-spacing: 0.34em;
  text-transform: uppercase;
  color: var(--svgb-13-muted);
  opacity: 0.75;
  transition: opacity var(--svgb-13-dur) ease, color var(--svgb-13-dur) ease;
  transition-delay: calc(var(--svgb-13-step) * 0.6);
}

.svgb-13__text {
  font-family: 'Cormorant Garamond', ui-serif, Georgia, serif;
  font-size: clamp(28px, 4.6vw, 44px);
  font-weight: 400;
  line-height: 1.05;
  letter-spacing: 0.01em;
  opacity: 0.66;
  transition: opacity var(--svgb-13-dur) ease, letter-spacing 620ms var(--svgb-13-ease), color var(--svgb-13-dur) ease;
  transition-delay: calc(var(--svgb-13-step) * 0.3);
}

.svgb-13__sub {
  font-size: 11.5px;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--svgb-13-muted);
  opacity: 0;
  translate: 0 5px;
  transition: opacity 320ms ease, translate 320ms var(--svgb-13-ease);
  transition-delay: 0ms;
}

.svgb-13__seal {
  position: absolute;
  inset-block-end: -26px;
  inset-inline-end: -14px;
  display: grid;
  place-items: center;
  inline-size: 54px;
  block-size: 54px;
  opacity: 0;
  scale: 0.9;
  transition: opacity 300ms ease, scale 420ms var(--svgb-13-ease);
  transition-delay: 0ms;
}

.svgb-13__seal svg {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
}

.svgb-13__sealring,
.svgb-13__sealmark {
  fill: none;
  stroke: var(--svgb-13-stroke);
  stroke-width: 1.4px;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.svgb-13__rsvp {
  position: relative;
  font-size: 7.5px;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--svgb-13-stroke);
}

.svgb-13__card:hover .svgb-13__outer,
.svgb-13__card:focus-visible .svgb-13__outer {
  stroke-dashoffset: 0;
  transition-delay: 0ms;
}

.svgb-13__card:hover .svgb-13__inner,
.svgb-13__card:focus-visible .svgb-13__inner {
  stroke-dashoffset: 0;
  transition-delay: calc(var(--svgb-13-step) * 1.4);
}

.svgb-13__card:hover .svgb-13__eyebrow,
.svgb-13__card:focus-visible .svgb-13__eyebrow {
  opacity: 1;
  color: var(--svgb-13-stroke);
  transition-delay: calc(var(--svgb-13-step) * 2.4);
}

.svgb-13__card:hover .svgb-13__text,
.svgb-13__card:focus-visible .svgb-13__text {
  opacity: 1;
  letter-spacing: 0.06em;
  transition-delay: calc(var(--svgb-13-step) * 2.6);
}

.svgb-13__card:hover .svgb-13__sub,
.svgb-13__card:focus-visible .svgb-13__sub {
  opacity: 1;
  translate: 0 0;
  transition-delay: calc(var(--svgb-13-step) * 3.1);
}

.svgb-13__card:hover .svgb-13__seal,
.svgb-13__card:focus-visible .svgb-13__seal {
  opacity: 1;
  scale: 1;
  transition-delay: calc(var(--svgb-13-step) * 3.6);
}

.svgb-13__card--quick {
  --svgb-13-step: 0ms;
}

.svgb-13__card--quick:hover .svgb-13__text,
.svgb-13__card--quick:focus-visible .svgb-13__text {
  transition-delay: 200ms;
}

.svgb-13__card--quick:hover .svgb-13__sub,
.svgb-13__card--quick:focus-visible .svgb-13__sub {
  transition-delay: 240ms;
}

.svgb-13__card--quick:hover .svgb-13__seal,
.svgb-13__card--quick:focus-visible .svgb-13__seal {
  transition-delay: 280ms;
}

.svgb-13__ti {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.svgb-13__toggle {
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
  background: color-mix(in oklab, currentColor 7%, transparent);
  color: inherit;
  cursor: pointer;
  transition: background 160ms ease, transform 160ms ease;
}

.svgb-13__toggle:hover {
  background: color-mix(in oklab, currentColor 14%, transparent);
}

.svgb-13__toggle:active {
  transform: scale(0.94);
}

.svgb-13__toggle svg {
  inline-size: 18px;
  block-size: 18px;
  transition: transform 400ms cubic-bezier(0.2, 0.7, 0.3, 1);
}

.svgb-13__ti:checked + .svgb-13__toggle svg {
  transform: rotate(180deg);
}

.svgb-13__ti:focus-visible + .svgb-13__toggle {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.svgb-13__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.svgb-13:has(#svgb-13-theme:checked) {
  --svgb-13-bg: #f7f3ea;
  --svgb-13-bg: oklch(0.968 0.014 85);
  --svgb-13-fg: #1b1710;
  --svgb-13-fg: oklch(0.215 0.015 70);
  --svgb-13-muted: #6f6551;
  --svgb-13-muted: oklch(0.525 0.025 80);
  --svgb-13-rest: rgba(27, 23, 16, 0.16);
  --svgb-13-rest: oklch(0.215 0.015 70 / 0.16);
  --svgb-13-stroke: #7a5a12;
  --svgb-13-stroke: oklch(0.50 0.10 80);
}

@media (prefers-reduced-motion: reduce) {
  .svgb-13__outer,
    .svgb-13__inner,
    .svgb-13__eyebrow,
    .svgb-13__text,
    .svgb-13__sub,
    .svgb-13__seal {
    transition: none !important;
    transition-delay: 0ms !important;
  }

  .svgb-13__outer,
    .svgb-13__inner {
    stroke-dasharray: none;
    stroke-dashoffset: 0;
    opacity: 0;
  }

  .svgb-13__card:hover .svgb-13__outer,
    .svgb-13__card:focus-visible .svgb-13__outer,
    .svgb-13__card:hover .svgb-13__inner,
    .svgb-13__card:focus-visible .svgb-13__inner {
    opacity: 1;
  }

  .svgb-13__toggle,
    .svgb-13__toggle svg {
    transition: none;
  }
}
```
