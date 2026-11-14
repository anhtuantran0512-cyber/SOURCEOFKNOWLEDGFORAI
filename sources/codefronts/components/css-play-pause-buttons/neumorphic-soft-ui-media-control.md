---
source: "codefronts"
url: "https://codefronts.com/components/css-play-pause-buttons/neumorphic-soft-ui-media-control/"
title: "Neumorphic Soft UI Media Control"
section: "components"
category: "css-play-pause-buttons"
category_name: "CSS Play / Pause Buttons"
description: "Soft UI done properly: the button is extruded from the surface with a matched light/dark shadow pair, and pressing it swaps to inset shadows so the control…"
has_js: "false"
---

Here's a working CSS Play / Pause Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neumorphic Soft UI Media Control
Source: https://codefronts.com/components/css-play-pause-buttons/neumorphic-soft-ui-media-control/

Soft UI done properly: the button is extruded from the surface with a matched light/dark shadow pair, and pressing it swaps to inset shadows so the control physically sinks in. The demo also fixes neumorphism's fatal flaw — its notorious contrast failure — by keeping the icon and label at accessible contrast and adding a visible focus ring, so it looks like 2019's dream and passes 2027's audits.
## HTML
```html
<section class="pp-04" aria-label="Neumorphic soft UI media control demo">
  <div class="pp-04__stage">
    <div class="pp-04__panel">
      <p class="pp-04__eyebrow">Now playing</p>
      <p class="pp-04__title">Soft Machine</p>
      <div class="pp-04__row">
        <button class="pp-04__mini" type="button" aria-label="Previous track">
          <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path d="M7 6v12M19 6l-9 6 9 6z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/></svg>
        </button>
        <input class="pp-04__chk" type="checkbox" id="pp-04-toggle" aria-label="Play or pause Soft Machine">
        <label class="pp-04__btn" for="pp-04-toggle">
          <svg viewBox="0 0 24 24" width="26" height="26" aria-hidden="true">
            <path class="pp-04__p" d="M8.6 5.4v13.2L19 12z" fill="currentColor"/>
            <path class="pp-04__q" d="M8 5h3.1v14H8zM12.9 5H16v14h-3.1z" fill="currentColor"/>
          </svg>
        </label>
        <button class="pp-04__mini" type="button" aria-label="Next track">
          <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path d="M17 6v12M5 6l9 6-9 6z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/></svg>
        </button>
      </div>
      <span class="pp-04__track" aria-hidden="true"><b></b></span>
    </div>
    <p class="pp-04__chip" aria-hidden="true">dual box-shadow extrusion · inset on :checked · color-mix() derived light</p>
  </div>
</section>
```
## CSS
```css
.pp-04,
.pp-04 *,
.pp-04 *::before,
.pp-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pp-04 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--pp-04-bg);
  --pp-04-surface: oklch(0.93 0.008 265);
  --pp-04-bg: oklch(0.93 0.008 265);
  --pp-04-dark: color-mix(in oklch,var(--pp-04-surface) 84%,black);
  --pp-04-light: color-mix(in oklch,var(--pp-04-surface) 62%,white);
  --pp-04-ink: oklch(0.34 0.02 265);
  --pp-04-mut: oklch(0.56 0.015 265);
  --pp-04-acc: oklch(0.58 0.15 275);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--pp-04-ink);
}

.pp-04__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 26px;
  padding: clamp(20px,5vw,56px);
}

.pp-04__panel {
  display: grid;
  justify-items: center;
  gap: 6px;
  width: min(100%,360px);
  padding: 34px 30px 30px;
  border-radius: 34px;
  background: var(--pp-04-surface);
  box-shadow: 14px 14px 32px var(--pp-04-dark),-14px -14px 32px var(--pp-04-light);
}

.pp-04__eyebrow {
  font-size: 11px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--pp-04-mut);
}

.pp-04__title {
  font-size: 20px;
  font-weight: 650;
  letter-spacing: -.015em;
}

.pp-04__row {
  display: flex;
  align-items: center;
  gap: 20px;
  margin-top: 18px;
}

.pp-04__chk {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.pp-04__btn {
  display: grid;
  place-items: center;
  width: 88px;
  height: 88px;
  border-radius: 50%;
  background: var(--pp-04-surface);
  color: var(--pp-04-acc);
  cursor: pointer;
  box-shadow: 9px 9px 20px var(--pp-04-dark),-9px -9px 20px var(--pp-04-light),inset 0 0 0 1px color-mix(in oklch,var(--pp-04-dark) 45%,transparent);
  transition: box-shadow .26s ease,color .26s,transform .26s;
}

.pp-04__btn:hover {
  transform: translateY(-2px);
}

.pp-04__chk:checked+.pp-04__btn {
  color: var(--pp-04-ink);
  box-shadow: inset 7px 7px 15px var(--pp-04-dark),inset -7px -7px 15px var(--pp-04-light);
  transform: none;
}

.pp-04__chk:focus-visible+.pp-04__btn {
  outline: 3px solid var(--pp-04-acc);
  outline-offset: 5px;
}

.pp-04__q {
  display: none;
}

.pp-04__chk:checked+.pp-04__btn .pp-04__p {
  display: none;
}

.pp-04__chk:checked+.pp-04__btn .pp-04__q {
  display: block;
}

.pp-04__mini {
  display: grid;
  place-items: center;
  width: 52px;
  height: 52px;
  border: 0;
  border-radius: 50%;
  background: var(--pp-04-surface);
  color: var(--pp-04-mut);
  cursor: pointer;
  box-shadow: 6px 6px 14px var(--pp-04-dark),-6px -6px 14px var(--pp-04-light);
  transition: box-shadow .22s,color .22s;
}

.pp-04__mini:hover {
  color: var(--pp-04-acc);
}

.pp-04__mini:active {
  box-shadow: inset 5px 5px 11px var(--pp-04-dark),inset -5px -5px 11px var(--pp-04-light);
}

.pp-04__mini:focus-visible {
  outline: 3px solid var(--pp-04-acc);
  outline-offset: 4px;
}

.pp-04__track {
  display: block;
  width: 100%;
  height: 12px;
  margin-top: 26px;
  border-radius: 99px;
  background: var(--pp-04-surface);
  box-shadow: inset 4px 4px 9px var(--pp-04-dark),inset -4px -4px 9px var(--pp-04-light);
  overflow: hidden;
  padding: 3px;
}

.pp-04__track b {
  display: block;
  height: 100%;
  width: 0;
  border-radius: 99px;
  background: var(--pp-04-acc);
  animation: pp-04-fill 16s linear infinite;
  animation-play-state: paused;
}

.pp-04__panel:has(.pp-04__chk:checked) .pp-04__track b {
  animation-play-state: running;
}

@keyframes pp-04-fill {
  from {
    width: 0;
  }

  to {
    width: 100%;
  }
}

.pp-04__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--pp-04-mut);
  padding: 8px 14px;
  border-radius: 99px;
  background: var(--pp-04-surface);
  box-shadow: inset 3px 3px 7px var(--pp-04-dark),inset -3px -3px 7px var(--pp-04-light);
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .pp-04 * {
    transition-duration: .01ms !important;
    animation: none !important;
  }
}
```
