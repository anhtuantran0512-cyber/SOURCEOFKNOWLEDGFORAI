---
source: "codefronts"
url: "https://codefronts.com/components/css-svg-stroke-buttons/reduced-motion-fallback-for-stroke-buttons/"
title: "Reduced Motion Fallback for Stroke Buttons"
section: "components"
category: "css-svg-stroke-buttons"
category_name: "CSS SVG Stroke Buttons"
description: "An accessibility settings screen that demonstrates its own setting."
has_js: "false"
---

Here's a working CSS SVG Stroke Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Reduced Motion Fallback for Stroke Buttons
Source: https://codefronts.com/components/css-svg-stroke-buttons/reduced-motion-fallback-for-stroke-buttons/

An accessibility settings screen that demonstrates its own setting. Flip the motion switch and the three sample buttons swap their travelling strokes for instant, full-strength borders — the same block the real prefers-reduced-motion query applies, so what you see in the preview is exactly what a user with the OS setting on gets.
## HTML
```html
<section class="svgb-19">
  <input class="svgb-19__ti" type="checkbox" id="svgb-19-theme">
  <label class="svgb-19__toggle" for="svgb-19-theme">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="svgb-19__sr">Switch colour scheme</span>
  </label>
  <div class="svgb-19__stage">
    <div class="svgb-19__win">
      <div class="svgb-19__side">
        <span class="svgb-19__stitle">Accessibility</span>
        <span class="svgb-19__srow">Display</span>
        <span class="svgb-19__srow svgb-19__srow--on">Motion</span>
        <span class="svgb-19__srow">Pointer</span>
        <span class="svgb-19__srow">Captions</span>
        <span class="svgb-19__srow">Audio</span>
      </div>
      <div class="svgb-19__main">
        <h1 class="svgb-19__h1">Motion</h1>
        <div class="svgb-19__setting">
          <input class="svgb-19__si" type="checkbox" id="svgb-19-sim">
          <label class="svgb-19__switch" for="svgb-19-sim">
            <span class="svgb-19__copy">
              <span class="svgb-19__sname">Reduce motion</span>
              <span class="svgb-19__sdesc">Replaces animated transitions with instant state changes.</span>
            </span>
            <span class="svgb-19__track" aria-hidden="true"><span class="svgb-19__knob"></span></span>
          </label>
        </div>

        <p class="svgb-19__pv">Preview</p>
        <div class="svgb-19__grid">
          <div class="svgb-19__cell">
            <button class="svgb-19__btn" type="button">
              <svg class="svgb-19__frame" viewBox="0 0 236 60" aria-hidden="true">
                <rect class="svgb-19__base" x="2" y="2" width="232" height="56" rx="12" pathLength="1"/>
                <rect class="svgb-19__ink" x="2" y="2" width="232" height="56" rx="12" pathLength="1"/>
              </svg>
              <span class="svgb-19__label">Perimeter draw</span>
            </button>
            <span class="svgb-19__cap">travel &rarr; instant presence</span>
          </div>
          <div class="svgb-19__cell">
            <button class="svgb-19__btn svgb-19__btn--march" type="button">
              <svg class="svgb-19__frame" viewBox="0 0 236 60" aria-hidden="true">
                <rect class="svgb-19__base" x="2" y="2" width="232" height="56" rx="12" pathLength="1"/>
                <rect class="svgb-19__ink svgb-19__ink--march" x="2" y="2" width="232" height="56" rx="12" pathLength="1"/>
              </svg>
              <span class="svgb-19__label">Marching dash</span>
            </button>
            <span class="svgb-19__cap">loop &rarr; static dash</span>
          </div>
          <div class="svgb-19__cell">
            <button class="svgb-19__btn svgb-19__btn--slide" type="button">
              <svg class="svgb-19__frame" viewBox="0 0 236 60" aria-hidden="true">
                <rect class="svgb-19__base" x="2" y="2" width="232" height="56" rx="12" pathLength="1"/>
                <rect class="svgb-19__ink" x="2" y="2" width="232" height="56" rx="12" pathLength="1"/>
              </svg>
              <span class="svgb-19__label">Sliding label</span>
            </button>
            <span class="svgb-19__cap">slide &rarr; colour only</span>
          </div>
        </div>
        <p class="svgb-19__wcag"><span class="svgb-19__chip">WCAG 2.3.3</span> Motion from interaction can be disabled, unless essential.</p>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Public+Sans:wght@400;500;600&family=JetBrains+Mono:wght@400&display=swap');

.svgb-19 {
  --svgb-19-bg: #e7e9ec;
  --svgb-19-bg: oklch(0.935 0.005 250);
  --svgb-19-fg: #12151a;
  --svgb-19-fg: oklch(0.19 0.007 250);
  --svgb-19-muted: #5b616b;
  --svgb-19-muted: oklch(0.505 0.012 250);
  --svgb-19-win: #ffffff;
  --svgb-19-win: oklch(1 0 0);
  --svgb-19-side: #f2f3f6;
  --svgb-19-side: oklch(0.965 0.004 250);
  --svgb-19-rest: rgba(18, 21, 26, 0.15);
  --svgb-19-rest: oklch(0.19 0.007 250 / 0.15);
  --svgb-19-stroke: #1a63d8;
  --svgb-19-stroke: oklch(0.50 0.20 260);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--svgb-19-bg);
  position: relative;
  color: var(--svgb-19-fg);
  font-family: 'Public Sans', system-ui, sans-serif;
}

.svgb-19 *,
.svgb-19 *::before,
.svgb-19 *::after {
  box-sizing: border-box;
}

.svgb-19__stage {
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(16px, 4vw, 56px);
}

.svgb-19__win {
  width: 100%;
  max-width: 940px;
  display: grid;
  grid-template-columns: minmax(0, 200px) 1fr;
  border-radius: 14px;
  overflow: hidden;
  background: var(--svgb-19-win);
  box-shadow: 0 1px 2px oklch(0 0 0 / 0.06), 0 40px 90px -60px oklch(0 0 0 / 0.5);
}

.svgb-19__side {
  display: flex;
  flex-direction: column;
  gap: 3px;
  padding: 18px 12px;
  background: var(--svgb-19-side);
  border-inline-end: 1px solid var(--svgb-19-rest);
}

.svgb-19__stitle {
  padding: 6px 10px 12px;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--svgb-19-muted);
}

.svgb-19__srow {
  padding: 9px 10px;
  border-radius: 7px;
  font-size: 14px;
  color: var(--svgb-19-muted);
}

.svgb-19__srow--on {
  background: color-mix(in oklab, var(--svgb-19-stroke) 12%, transparent);
  color: var(--svgb-19-fg);
  font-weight: 500;
}

.svgb-19__main {
  display: flex;
  flex-direction: column;
  gap: 16px;
  padding: clamp(20px, 3.5vw, 34px);
}

.svgb-19__h1 {
  margin: 0;
  font-size: clamp(24px, 3.4vw, 32px);
  font-weight: 600;
  letter-spacing: -0.025em;
}

.svgb-19__setting {
  border: 1px solid var(--svgb-19-rest);
  border-radius: 12px;
}

.svgb-19__si {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.svgb-19__switch {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
  padding: 16px 18px;
  cursor: pointer;
}

.svgb-19__copy {
  display: flex;
  flex-direction: column;
  gap: 3px;
}

.svgb-19__sname {
  font-size: 15px;
  font-weight: 500;
}

.svgb-19__sdesc {
  font-size: 13px;
  color: var(--svgb-19-muted);
}

.svgb-19__track {
  position: relative;
  flex: none;
  inline-size: 50px;
  block-size: 30px;
  border-radius: 999px;
  background: color-mix(in oklab, var(--svgb-19-fg) 16%, transparent);
  transition: background 200ms ease;
}

.svgb-19__knob {
  position: absolute;
  inset-block-start: 3px;
  inset-inline-start: 3px;
  inline-size: 24px;
  block-size: 24px;
  border-radius: 50%;
  background: #fff;
  box-shadow: 0 1px 3px oklch(0 0 0 / 0.3);
  transition: translate 220ms cubic-bezier(0.22, 1, 0.36, 1);
}

.svgb-19__si:checked + .svgb-19__switch .svgb-19__track {
  background: var(--svgb-19-stroke);
}

.svgb-19__si:checked + .svgb-19__switch .svgb-19__knob {
  translate: 20px 0;
}

.svgb-19__si:focus-visible + .svgb-19__switch {
  outline: 2px solid var(--svgb-19-stroke);
  outline-offset: -2px;
  border-radius: 12px;
}

.svgb-19__pv {
  margin: 6px 0 0;
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-size: 10.5px;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--svgb-19-muted);
}

.svgb-19__grid {
  display: grid;
  gap: clamp(12px, 2vw, 18px);
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 236px), 1fr));
}

.svgb-19__cell {
  display: flex;
  flex-direction: column;
  gap: 9px;
}

.svgb-19__cap {
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-size: 10.5px;
  color: var(--svgb-19-muted);
}

.svgb-19__btn {
  position: relative;
  inline-size: 100%;
  max-inline-size: 236px;
  block-size: 60px;
  display: grid;
  place-items: center;
  border: 0;
  padding: 0;
  border-radius: 12px;
  background: color-mix(in oklab, var(--svgb-19-fg) 4%, transparent);
  color: inherit;
  font: inherit;
  font-size: 14.5px;
  font-weight: 500;
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
  overflow: hidden;
}

.svgb-19__btn:focus-visible {
  outline: 2px solid var(--svgb-19-stroke);
  outline-offset: 3px;
}

.svgb-19__label {
  position: relative;
  z-index: 1;
  transition: translate 320ms cubic-bezier(0.22, 1, 0.36, 1), color 220ms ease;
}

.svgb-19__btn--slide:hover .svgb-19__label,
.svgb-19__btn--slide:focus-visible .svgb-19__label {
  translate: 0 -2px;
  color: var(--svgb-19-stroke);
}

.svgb-19__frame {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  overflow: visible;
}

.svgb-19__frame rect {
  fill: none;
  stroke-linecap: round;
}

.svgb-19__base {
  stroke: var(--svgb-19-rest);
  stroke-width: 1.4px;
}

.svgb-19__ink {
  stroke: var(--svgb-19-stroke);
  stroke-width: 2.2px;
  stroke-dasharray: 1;
  stroke-dashoffset: 1;
  transition: stroke-dashoffset 640ms cubic-bezier(0.22, 1, 0.36, 1);
}

.svgb-19__btn:hover .svgb-19__ink,
.svgb-19__btn:focus-visible .svgb-19__ink {
  stroke-dashoffset: 0;
}

@keyframes svgb-19-march {
  to {
    stroke-dashoffset: -0.1;
  }
}

.svgb-19__ink--march {
  stroke-dasharray: 0.05 0.05;
  stroke-dashoffset: 0;
  animation: svgb-19-march 900ms linear infinite;
  animation-play-state: paused;
  opacity: 0;
  transition: opacity 200ms ease;
}

.svgb-19__btn--march:hover .svgb-19__ink--march,
.svgb-19__btn--march:focus-visible .svgb-19__ink--march {
  opacity: 1;
  animation-play-state: running;
}

.svgb-19__wcag {
  margin: 4px 0 0;
  display: flex;
  gap: 9px;
  align-items: baseline;
  font-size: 12.5px;
  color: var(--svgb-19-muted);
}

.svgb-19__chip {
  flex: none;
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-size: 10px;
  padding: 3px 7px;
  border-radius: 5px;
  background: color-mix(in oklab, var(--svgb-19-stroke) 12%, transparent);
  color: color-mix(in oklab, var(--svgb-19-stroke) 78%, var(--svgb-19-fg));
}
/* the fallback, applied by the media query AND by the settings switch */

@media (prefers-reduced-motion: reduce) {
  .svgb-19__ink {
    transition: none;
    stroke-dasharray: none;
    stroke-dashoffset: 0;
    opacity: 0;
  }

  .svgb-19__btn:hover .svgb-19__ink,
    .svgb-19__btn:focus-visible .svgb-19__ink {
    opacity: 1;
  }

  .svgb-19__ink--march {
    animation: none;
    stroke-dasharray: 0.05 0.05;
  }

  .svgb-19__label {
    transition: color 220ms ease;
  }

  .svgb-19__btn--slide:hover .svgb-19__label,
    .svgb-19__btn--slide:focus-visible .svgb-19__label {
    translate: 0 0;
  }

  .svgb-19__knob,
    .svgb-19__track,
    .svgb-19__toggle,
    .svgb-19__toggle svg {
    transition: none;
  }
}

.svgb-19:has(#svgb-19-sim:checked) .svgb-19__ink {
  transition: none;
  stroke-dasharray: none;
  stroke-dashoffset: 0;
  opacity: 0;
}

.svgb-19:has(#svgb-19-sim:checked) .svgb-19__btn:hover .svgb-19__ink,
.svgb-19:has(#svgb-19-sim:checked) .svgb-19__btn:focus-visible .svgb-19__ink {
  opacity: 1;
}

.svgb-19:has(#svgb-19-sim:checked) .svgb-19__ink--march {
  animation: none;
  stroke-dasharray: 0.05 0.05;
}

.svgb-19:has(#svgb-19-sim:checked) .svgb-19__label {
  transition: color 220ms ease;
}

.svgb-19:has(#svgb-19-sim:checked) .svgb-19__btn--slide:hover .svgb-19__label,
.svgb-19:has(#svgb-19-sim:checked) .svgb-19__btn--slide:focus-visible .svgb-19__label {
  translate: 0 0;
}

.svgb-19__ti {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.svgb-19__toggle {
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

.svgb-19__toggle:hover {
  background: color-mix(in oklab, currentColor 14%, transparent);
}

.svgb-19__toggle:active {
  transform: scale(0.94);
}

.svgb-19__toggle svg {
  inline-size: 18px;
  block-size: 18px;
  transition: transform 400ms cubic-bezier(0.2, 0.7, 0.3, 1);
}

.svgb-19__ti:checked + .svgb-19__toggle svg {
  transform: rotate(180deg);
}

.svgb-19__ti:focus-visible + .svgb-19__toggle {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.svgb-19__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.svgb-19:has(#svgb-19-theme:checked) {
  --svgb-19-bg: #0b0d11;
  --svgb-19-bg: oklch(0.165 0.007 250);
  --svgb-19-fg: #edeff3;
  --svgb-19-fg: oklch(0.955 0.004 250);
  --svgb-19-muted: #8c929c;
  --svgb-19-muted: oklch(0.67 0.012 250);
  --svgb-19-win: #15181e;
  --svgb-19-win: oklch(0.22 0.009 250);
  --svgb-19-side: #11141a;
  --svgb-19-side: oklch(0.19 0.008 250);
  --svgb-19-rest: rgba(237, 239, 243, 0.16);
  --svgb-19-rest: oklch(0.955 0.004 250 / 0.16);
  --svgb-19-stroke: #85b4ff;
  --svgb-19-stroke: oklch(0.79 0.13 262);
}

.svgb-19:has(#svgb-19-theme:checked) .svgb-19__knob {
  background: #0d1014;
}
```
