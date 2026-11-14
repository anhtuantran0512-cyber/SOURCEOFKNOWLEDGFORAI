---
source: "codefronts"
url: "https://codefronts.com/motion/css-loader-designs/css-wave-bars-audio-loader/"
title: "CSS Wave Bars Audio Loader"
section: "motion"
category: "css-loader-designs"
category_name: "CSS Loaders"
description: "Four music-visualiser CSS loaders — classic audio bars, a 10-band spectrum analyser, a waveform timeline, and a dual-channel VU meter — styled with a retro…"
has_js: "false"
---

Here's a working CSS Loader from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Wave Bars Audio Loader
Source: https://codefronts.com/motion/css-loader-designs/css-wave-bars-audio-loader/

Four music-visualiser CSS loaders — classic audio bars, a 10-band spectrum analyser, a waveform timeline, and a dual-channel VU meter — styled with a retro green terminal palette.
## HTML
```html
<div class="ld-13">
  <div class="ld-13__stage">
    <div class="ld-13__cell"><div class="ld-13__bars"><span></span><span></span><span></span><span></span><span></span><span></span><span></span></div><span class="ld-13__label">Audio Bars</span></div>
    <div class="ld-13__cell"><div class="ld-13__spectrum"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></div><span class="ld-13__label">Spectrum</span></div>
    <div class="ld-13__cell"><div class="ld-13__wave-line"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></div><span class="ld-13__label">Waveform</span></div>
    <div class="ld-13__cell">
      <div class="ld-13__vu">
        <div class="ld-13__vu-col"><div class="ld-13__vu-seg"></div><div class="ld-13__vu-seg"></div><div class="ld-13__vu-seg"></div><div class="ld-13__vu-seg"></div><div class="ld-13__vu-seg"></div><div class="ld-13__vu-seg"></div></div>
```
## CSS
```css
.ld-13,
.ld-13 *,
.ld-13 *::before,
.ld-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ld-13 {
  --bg: #001a00;
  --c1: #00ff41;
  --c2: #00cc33;
  --c3: #39ff14;
  --c4: #7fff00;
  background: var(--bg);
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  font-family: 'Courier New',monospace;
}

.ld-13__stage {
  display: flex;
  gap: 70px;
  flex-wrap: wrap;
  justify-content: center;
  padding: 40px;
  align-items: center;
}

.ld-13__cell {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
}

.ld-13__label {
  color: rgba(0,255,65,.3);
  font-size: 11px;
  letter-spacing: 1.5px;
  text-transform: uppercase;
}
/* Classic audio bars */

.ld-13__bars {
  display: flex;
  gap: 4px;
  align-items: flex-end;
  height: 50px;
}

.ld-13__bars span {
  width: 6px;
  border-radius: 3px 3px 0 0;
  background: var(--c1);
  box-shadow: 0 0 6px var(--c1);
  animation: ld-13-bar 0.9s ease-in-out infinite alternate;
}

.ld-13__bars span:nth-child(1) {
  height: 15px;
  animation-delay: 0s;
}

.ld-13__bars span:nth-child(2) {
  height: 35px;
  animation-delay: .05s;
  background: var(--c2);
}

.ld-13__bars span:nth-child(3) {
  height: 50px;
  animation-delay: .1s;
}

.ld-13__bars span:nth-child(4) {
  height: 28px;
  animation-delay: .15s;
  background: var(--c3);
}

.ld-13__bars span:nth-child(5) {
  height: 42px;
  animation-delay: .2s;
}

.ld-13__bars span:nth-child(6) {
  height: 20px;
  animation-delay: .25s;
  background: var(--c2);
}

.ld-13__bars span:nth-child(7) {
  height: 36px;
  animation-delay: .3s;
}

@keyframes ld-13-bar {
  0% {
    transform: scaleY(.3);
  }

  100% {
    transform: scaleY(1);
  }
}
/* Spectrum */

.ld-13__spectrum {
  display: flex;
  gap: 3px;
  align-items: center;
  height: 60px;
}

.ld-13__spectrum span {
  width: 5px;
  border-radius: 3px;
  background: linear-gradient(to top,var(--c1),var(--c4));
  animation: ld-13-spectrum 1.2s ease-in-out infinite;
}

.ld-13__spectrum span:nth-child(1) {
  animation-delay: 0s;
}

.ld-13__spectrum span:nth-child(2) {
  animation-delay: .05s;
}

.ld-13__spectrum span:nth-child(3) {
  animation-delay: .1s;
}

.ld-13__spectrum span:nth-child(4) {
  animation-delay: .15s;
}

.ld-13__spectrum span:nth-child(5) {
  animation-delay: .2s;
}

.ld-13__spectrum span:nth-child(6) {
  animation-delay: .25s;
}

.ld-13__spectrum span:nth-child(7) {
  animation-delay: .3s;
}

.ld-13__spectrum span:nth-child(8) {
  animation-delay: .35s;
}

.ld-13__spectrum span:nth-child(9) {
  animation-delay: .4s;
}

.ld-13__spectrum span:nth-child(10) {
  animation-delay: .45s;
}

@keyframes ld-13-spectrum {
  0%,
    100% {
    height: 8px;
    opacity: .4;
  }

  50% {
    height: 52px;
    opacity: 1;
  }
}
/* Waveform line */

.ld-13__wave-line {
  width: 160px;
  height: 40px;
  display: flex;
  gap: 2px;
  align-items: center;
}

.ld-13__wave-line span {
  flex: 1;
  border-radius: 2px;
  background: var(--c1);
  animation: ld-13-wave 1s ease-in-out infinite;
}

.ld-13__wave-line span:nth-child(1) {
  animation-delay: 0s;
}

.ld-13__wave-line span:nth-child(2) {
  animation-delay: .06s;
}

.ld-13__wave-line span:nth-child(3) {
  animation-delay: .12s;
}

.ld-13__wave-line span:nth-child(4) {
  animation-delay: .18s;
}

.ld-13__wave-line span:nth-child(5) {
  animation-delay: .24s;
}

.ld-13__wave-line span:nth-child(6) {
  animation-delay: .30s;
}

.ld-13__wave-line span:nth-child(7) {
  animation-delay: .36s;
}

.ld-13__wave-line span:nth-child(8) {
  animation-delay: .42s;
}

.ld-13__wave-line span:nth-child(9) {
  animation-delay: .48s;
}

.ld-13__wave-line span:nth-child(10) {
  animation-delay: .54s;
}

.ld-13__wave-line span:nth-child(11) {
  animation-delay: .60s;
}

.ld-13__wave-line span:nth-child(12) {
  animation-delay: .66s;
}

@keyframes ld-13-wave {
  0%,
    100% {
    height: 4px;
  }

  50% {
    height: 36px;
  }
}
/* VU Meter */

.ld-13__vu {
  display: flex;
  gap: 6px;
}

.ld-13__vu-col {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.ld-13__vu-seg {
  width: 12px;
  height: 6px;
  border-radius: 1px;
  background: rgba(0,255,65,.12);
  animation: ld-13-vu 1.2s ease-in-out infinite;
}

.ld-13__vu-col:nth-child(1) .ld-13__vu-seg:nth-child(1) {
  animation-delay: 0s;
  --h: 6;
}

.ld-13__vu-col:nth-child(1) .ld-13__vu-seg:nth-child(2) {
  animation-delay: .05s;
}

.ld-13__vu-col:nth-child(1) .ld-13__vu-seg:nth-child(3) {
  animation-delay: .1s;
}

.ld-13__vu-col:nth-child(1) .ld-13__vu-seg:nth-child(4) {
  animation-delay: .15s;
}

.ld-13__vu-col:nth-child(1) .ld-13__vu-seg:nth-child(5) {
  animation-delay: .2s;
  background: rgba(255,255,0,.12);
}

.ld-13__vu-col:nth-child(1) .ld-13__vu-seg:nth-child(6) {
  animation-delay: .25s;
  background: rgba(255,0,0,.12);
}

.ld-13__vu-col:nth-child(2) .ld-13__vu-seg:nth-child(1) {
  animation-delay: .1s;
}

.ld-13__vu-col:nth-child(2) .ld-13__vu-seg:nth-child(2) {
  animation-delay: .15s;
}

.ld-13__vu-col:nth-child(2) .ld-13__vu-seg:nth-child(3) {
  animation-delay: .2s;
}

.ld-13__vu-col:nth-child(2) .ld-13__vu-seg:nth-child(4) {
  animation-delay: .25s;
}

.ld-13__vu-col:nth-child(2) .ld-13__vu-seg:nth-child(5) {
  animation-delay: .3s;
  background: rgba(255,255,0,.12);
}

.ld-13__vu-col:nth-child(2) .ld-13__vu-seg:nth-child(6) {
  animation-delay: .35s;
  background: rgba(255,0,0,.12);
}

@keyframes ld-13-vu {
  0%,
    100% {
    background: rgba(0,255,65,.08);
  }

  50% {
    background: var(--c1);
    box-shadow: 0 0 4px var(--c1);
  }
}

@media (prefers-reduced-motion: reduce) {
  .ld-13__bars span,
    .ld-13__spectrum span,
    .ld-13__wave-line span,
    .ld-13__vu-seg {
    animation: none;
    height: 20px;
  }
}
```
