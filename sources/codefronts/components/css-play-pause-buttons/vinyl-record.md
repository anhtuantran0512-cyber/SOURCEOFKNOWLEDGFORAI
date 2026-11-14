---
source: "codefronts"
url: "https://codefronts.com/components/css-play-pause-buttons/vinyl-record/"
title: "Vinyl Record Spinning Audio Control"
section: "components"
category: "css-play-pause-buttons"
category_name: "CSS Play / Pause Buttons"
description: "A turntable that actually behaves like one: the record spins at a constant 33⅓-ish rate, the tonearm swings onto the groove when you press play, and pausing…"
has_js: "false"
---

Here's a working CSS Play / Pause Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Vinyl Record Spinning Audio Control
Source: https://codefronts.com/components/css-play-pause-buttons/vinyl-record/

A turntable that actually behaves like one: the record spins at a constant 33⅓-ish rate, the tonearm swings onto the groove when you press play, and pausing freezes the disc where it stopped instead of snapping it back to zero. That last detail is the whole lesson — it comes free from animation-play-state, the most under-used property in CSS media UI.
## HTML
```html
<section class="pp-09" aria-label="Spinning vinyl record audio control demo">
  <div class="pp-09__stage">
    <div class="pp-09__deck">
      <div class="pp-09__platter">
        <div class="pp-09__disc">
          <img class="pp-09__label" src="https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?q=80&w=400&auto=format&fit=crop" alt="" width="120" height="120" loading="lazy">
          <span class="pp-09__spindle" aria-hidden="true"></span>
        </div>
        <span class="pp-09__arm" aria-hidden="true"><i></i></span>
      </div>
      <div class="pp-09__panel">
        <p class="pp-09__side">Side A · 33⅓</p>
        <p class="pp-09__title">Analog Sundown</p>
        <p class="pp-09__artist">The Groove Committee</p>
        <input class="pp-09-chk" type="checkbox" id="pp-09-toggle" aria-label="Play or pause Analog Sundown">
        <label class="pp-09__btn" for="pp-09-toggle">
          <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true">
            <path class="pp-09__p" d="M8.8 5.6v12.8L18.6 12z" fill="currentColor"/>
            <path class="pp-09__q" d="M8.4 5.6h3v12.8h-3zM12.9 5.6h3v12.8h-3z" fill="currentColor"/>
          </svg>
          <span class="pp-09__btn-on">Pause</span><span class="pp-09__btn-off">Play</span>
        </label>
      </div>
    </div>
    <p class="pp-09__chip" aria-hidden="true">animation-play-state · repeating-radial-gradient grooves · tonearm transform-origin</p>
  </div>
</section>
```
## CSS
```css
.pp-09,
.pp-09 *,
.pp-09 *::before,
.pp-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pp-09 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--pp-09-bg);
  --pp-09-bg: oklch(0.19 0.02 55);
  --pp-09-card: oklch(0.25 0.025 55);
  --pp-09-ink: oklch(0.96 0.01 80);
  --pp-09-mut: oklch(0.7 0.03 65);
  --pp-09-acc: oklch(0.78 0.15 68);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--pp-09-ink);
}

.pp-09__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 24px;
  padding: clamp(20px,5vw,56px);
  background: radial-gradient(70% 60% at 50% 10%,oklch(0.3 0.06 60/.6),transparent 70%);
}

.pp-09__deck {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
  gap: 34px;
  padding: 30px 36px;
  border-radius: 26px;
  background: var(--pp-09-card);
  box-shadow: 0 0 0 1px oklch(1 0 0/.07),0 30px 70px oklch(0 0 0/.5);
}

.pp-09__platter {
  position: relative;
  width: 236px;
  height: 236px;
  flex: none;
  border-radius: 50%;
  background: oklch(0.22 0.02 55);
  box-shadow: inset 0 0 0 8px oklch(0.28 0.02 55),0 16px 40px oklch(0 0 0/.5);
}

.pp-09__disc {
  position: absolute;
  inset: 10px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  background: repeating-radial-gradient(circle at 50% 50%,oklch(0.16 0.005 60) 0 2px,oklch(0.2 0.008 60) 2px 4px),conic-gradient(from 210deg,transparent 0deg,oklch(1 0 0/.09) 24deg,transparent 60deg,transparent 200deg,oklch(1 0 0/.06) 232deg,transparent 268deg);
  animation: pp-09-spin 3.6s linear infinite;
  animation-play-state: paused;
}

.pp-09__label {
  width: 44%;
  height: 44%;
  border-radius: 50%;
  object-fit: cover;
  background: linear-gradient(135deg,var(--pp-09-acc),oklch(0.45 0.12 30));
  box-shadow: 0 0 0 1px oklch(0 0 0/.4);
}

.pp-09__spindle {
  position: absolute;
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: oklch(0.72 0.02 80);
  box-shadow: inset 0 -1px 2px oklch(0 0 0/.6);
}

.pp-09__arm {
  position: absolute;
  top: 16px;
  right: 14px;
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: oklch(0.75 0.02 80);
  transform-origin: 50% 50%;
  rotate: -26deg;
  transition: rotate .7s cubic-bezier(.4,0,.2,1);
}

.pp-09__arm i {
  position: absolute;
  top: 6px;
  left: 6px;
  width: 6px;
  height: 126px;
  border-radius: 4px;
  background: linear-gradient(180deg,oklch(0.8 0.02 80),oklch(0.62 0.02 80));
  transform-origin: top center;
  rotate: 22deg;
}

.pp-09__arm i::after {
  content: '';
  position: absolute;
  bottom: -6px;
  left: -5px;
  width: 16px;
  height: 14px;
  border-radius: 3px;
  background: oklch(0.35 0.03 40);
  box-shadow: 0 2px 4px oklch(0 0 0/.5);
}

.pp-09__panel {
  min-width: 190px;
}

.pp-09__side {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .16em;
  color: var(--pp-09-acc);
}

.pp-09__title {
  font-size: 24px;
  font-weight: 660;
  letter-spacing: -.02em;
  margin-top: 8px;
}

.pp-09__artist {
  font-size: 13.5px;
  color: var(--pp-09-mut);
  margin-top: 4px;
}

.pp-09-chk {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.pp-09__btn {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  min-height: 48px;
  margin-top: 22px;
  padding: 0 22px 0 18px;
  border-radius: 99px;
  background: var(--pp-09-acc);
  color: oklch(0.22 0.04 60);
  font-size: 14.5px;
  font-weight: 660;
  cursor: pointer;
  transition: transform .22s cubic-bezier(.34,1.4,.5,1),background .25s;
}

.pp-09__btn:hover {
  transform: translateY(-2px);
}

.pp-09-chk:focus-visible+.pp-09__btn {
  outline: 3px solid var(--pp-09-ink);
  outline-offset: 3px;
}

.pp-09__q,
.pp-09__btn-on {
  display: none;
}

.pp-09__deck:has(.pp-09-chk:checked) .pp-09__disc {
  animation-play-state: running;
}

.pp-09__deck:has(.pp-09-chk:checked) .pp-09__arm {
  rotate: 6deg;
}

.pp-09__deck:has(.pp-09-chk:checked) .pp-09__p,
.pp-09__deck:has(.pp-09-chk:checked) .pp-09__btn-off {
  display: none;
}

.pp-09__deck:has(.pp-09-chk:checked) .pp-09__q,
.pp-09__deck:has(.pp-09-chk:checked) .pp-09__btn-on {
  display: inline-block;
}

@keyframes pp-09-spin {
  to {
    rotate: 360deg;
  }
}

.pp-09__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--pp-09-mut);
  padding: 7px 14px;
  border: 1px solid oklch(1 0 0/.13);
  border-radius: 99px;
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .pp-09__disc {
    animation: none !important;
  }

  .pp-09 * {
    transition-duration: .01ms !important;
  }
}
```
