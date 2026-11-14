---
source: "codefronts"
url: "https://codefronts.com/components/css-play-pause-buttons/cassette-tape/"
title: "Vintage Cassette Tape Audio Control"
section: "components"
category: "css-play-pause-buttons"
category_name: "CSS Play / Pause Buttons"
description: "A working mixtape: both reels turn while the tape plays, the spools are conic-gradient spokes with radial hub shading, and the handwritten label sits behind…"
has_js: "false"
---

Here's a working CSS Play / Pause Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Vintage Cassette Tape Audio Control
Source: https://codefronts.com/components/css-play-pause-buttons/cassette-tape/

A working mixtape: both reels turn while the tape plays, the spools are conic-gradient spokes with radial hub shading, and the handwritten label sits behind a glossy shell highlight. It is a still-life of a real object built from four gradients — and the reels use the same animation-play-state discipline as the vinyl demo, so pausing freezes them mid-rotation.
## HTML
```html
<section class="pp-24" aria-label="Vintage cassette tape audio control demo">
  <div class="pp-24__stage">
    <div class="pp-24__deck">
      <div class="pp-24__shell" aria-hidden="true">
        <span class="pp-24__gloss"></span>
        <div class="pp-24__window">
          <span class="pp-24__reel"></span>
          <span class="pp-24__tape"></span>
          <span class="pp-24__reel pp-24__reel--b"></span>
        </div>
        <p class="pp-24__label"><b>SUMMER MIX '87</b><i>side a · 45 min</i></p>
        <span class="pp-24__screws"></span>
      </div>
      <div class="pp-24__controls">
        <span class="pp-24__led" aria-hidden="true"></span>
        <input class="pp-24-chk" type="checkbox" id="pp-24-toggle" aria-label="Play or pause the mixtape">
        <label class="pp-24__btn" for="pp-24-toggle">
          <span class="pp-24__glyph" aria-hidden="true">
            <svg viewBox="0 0 24 24" width="18" height="18">
              <path class="pp-24__p" d="M9 5.8v12.4L18.6 12z" fill="currentColor"/>
              <path class="pp-24__q" d="M8.6 5.8h3.1v12.4H8.6zM13 5.8h3.1v12.4H13z" fill="currentColor"/>
            </svg>
          </span>
          <span class="pp-24__word-off">PLAY</span><span class="pp-24__word-on">PAUSE</span>
        </label>
      </div>
    </div>
    <p class="pp-24__chip" aria-hidden="true">conic-gradient spokes · shared keyframe, two speeds · play-state freeze</p>
  </div>
</section>
```
## CSS
```css
.pp-24,
.pp-24 *,
.pp-24 *::before,
.pp-24 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pp-24 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--pp-24-bg);
  --pp-24-bg: oklch(0.24 0.02 60);
  --pp-24-shell: oklch(0.86 0.05 75);
  --pp-24-shell2: oklch(0.72 0.07 60);
  --pp-24-ink: oklch(0.25 0.03 60);
  --pp-24-mut: oklch(0.72 0.03 65);
  --pp-24-tape: oklch(0.28 0.03 45);
  --pp-24-led: oklch(0.65 0.22 28);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--pp-24-mut);
}

.pp-24__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 24px;
  padding: clamp(20px,5vw,56px);
  background: radial-gradient(75% 60% at 50% 10%,oklch(0.32 0.05 65/.7),transparent 72%);
}

.pp-24__deck {
  display: grid;
  justify-items: center;
  gap: 22px;
}

.pp-24__shell {
  position: relative;
  width: min(92vw,400px);
  aspect-ratio: 16/10;
  border-radius: 12px;
  background: linear-gradient(165deg,var(--pp-24-shell),var(--pp-24-shell2));
  box-shadow: inset 0 2px 0 oklch(1 0 0/.5),inset 0 -3px 8px oklch(0 0 0/.25),0 26px 60px oklch(0 0 0/.55);
  overflow: hidden;
}

.pp-24__gloss {
  position: absolute;
  inset: 0;
  background: linear-gradient(105deg,oklch(1 0 0/.32) 0 18%,transparent 34%,oklch(1 0 0/.12) 62%,transparent 78%);
}

.pp-24__window {
  position: absolute;
  top: 12%;
  left: 12%;
  right: 12%;
  height: 44%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 7%;
  border-radius: 8px;
  background: oklch(0.18 0.02 55);
  box-shadow: inset 0 2px 8px oklch(0 0 0/.7),0 1px 0 oklch(1 0 0/.35);
}

.pp-24__reel {
  position: relative;
  width: 31%;
  aspect-ratio: 1;
  border-radius: 50%;
  background: conic-gradient(from 0deg,var(--pp-24-shell) 0 10deg,transparent 10deg 50deg,var(--pp-24-shell) 50deg 70deg,transparent 70deg 110deg,var(--pp-24-shell) 110deg 130deg,transparent 130deg 170deg,var(--pp-24-shell) 170deg 190deg,transparent 190deg 230deg,var(--pp-24-shell) 230deg 250deg,transparent 250deg 290deg,var(--pp-24-shell) 290deg 310deg,transparent 310deg 350deg,var(--pp-24-shell) 350deg 360deg),radial-gradient(circle,oklch(0.4 0.03 55) 0 26%,var(--pp-24-tape) 26% 100%);
  box-shadow: 0 0 0 2px oklch(0 0 0/.5),inset 0 0 12px oklch(0 0 0/.6);
  animation: pp-24-spin 2.4s linear infinite;
  animation-play-state: paused;
}

.pp-24__reel--b {
  animation-duration: 3.1s;
}

.pp-24__tape {
  flex: 1;
  height: 26%;
  margin: 0 4%;
  border-radius: 4px;
  background: linear-gradient(180deg,oklch(0.35 0.03 45),var(--pp-24-tape));
  box-shadow: inset 0 1px 0 oklch(1 0 0/.12);
}

.pp-24__label {
  position: absolute;
  left: 9%;
  right: 9%;
  bottom: 9%;
  padding: 9px 14px;
  border-radius: 4px;
  background: oklch(0.96 0.02 90);
  color: var(--pp-24-ink);
  box-shadow: 0 1px 0 oklch(0 0 0/.2);
  rotate: -.6deg;
}

.pp-24__label b {
  display: block;
  font-size: 15px;
  font-weight: 700;
  letter-spacing: .06em;
}

.pp-24__label i {
  display: block;
  font-size: 11px;
  font-style: normal;
  letter-spacing: .14em;
  text-transform: uppercase;
  opacity: .6;
  margin-top: 3px;
}

.pp-24__screws {
  position: absolute;
  inset: 8px;
  border-radius: 8px;
  box-shadow: inset 0 0 0 1px oklch(0 0 0/.12);
}

.pp-24__controls {
  display: flex;
  align-items: center;
  gap: 16px;
}

.pp-24__led {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: oklch(0.35 0.04 30);
  box-shadow: inset 0 1px 2px oklch(0 0 0/.6);
  transition: background .3s,box-shadow .3s;
}

.pp-24-chk {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.pp-24__btn {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  min-height: 48px;
  padding: 0 22px;
  border-radius: 8px;
  background: linear-gradient(180deg,oklch(0.4 0.02 60),oklch(0.31 0.02 60));
  color: oklch(0.94 0.02 70);
  font-size: 12.5px;
  font-weight: 700;
  letter-spacing: .18em;
  cursor: pointer;
  box-shadow: 0 4px 0 oklch(0.2 0.02 60),0 6px 14px oklch(0 0 0/.45),inset 0 1px 0 oklch(1 0 0/.2);
  transition: translate .1s linear,box-shadow .1s linear;
}

.pp-24__btn:active {
  translate: 0 3px;
  box-shadow: 0 1px 0 oklch(0.2 0.02 60),0 2px 8px oklch(0 0 0/.45),inset 0 1px 0 oklch(1 0 0/.2);
}

.pp-24-chk:focus-visible+.pp-24__btn {
  outline: 3px solid var(--pp-24-shell);
  outline-offset: 4px;
}

.pp-24__q,
.pp-24__word-on {
  display: none;
}

.pp-24__deck:has(.pp-24-chk:checked) .pp-24__reel {
  animation-play-state: running;
}

.pp-24__deck:has(.pp-24-chk:checked) .pp-24__led {
  background: var(--pp-24-led);
  box-shadow: 0 0 12px var(--pp-24-led);
}

.pp-24__deck:has(.pp-24-chk:checked) .pp-24__p,
.pp-24__deck:has(.pp-24-chk:checked) .pp-24__word-off {
  display: none;
}

.pp-24__deck:has(.pp-24-chk:checked) .pp-24__q,
.pp-24__deck:has(.pp-24-chk:checked) .pp-24__word-on {
  display: inline-block;
}

@keyframes pp-24-spin {
  to {
    rotate: 360deg;
  }
}

.pp-24__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--pp-24-mut);
  padding: 7px 14px;
  border: 1px solid oklch(1 0 0/.14);
  border-radius: 99px;
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .pp-24__reel {
    animation: none !important;
  }

  .pp-24 * {
    transition-duration: .01ms !important;
  }
}
```
