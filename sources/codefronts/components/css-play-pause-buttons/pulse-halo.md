---
source: "codefronts"
url: "https://codefronts.com/components/css-play-pause-buttons/pulse-halo/"
title: "Pulsing Halo Video Play Icon"
section: "components"
category: "css-play-pause-buttons"
category_name: "CSS Play / Pause Buttons"
description: "The attention magnet used on every hero video: concentric rings that expand and fade out of the play button forever, drawing the eye without moving the layout."
has_js: "false"
---

Here's a working CSS Play / Pause Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pulsing Halo Video Play Icon
Source: https://codefronts.com/components/css-play-pause-buttons/pulse-halo/

The attention magnet used on every hero video: concentric rings that expand and fade out of the play button forever, drawing the eye without moving the layout. Two pseudo-elements and one keyframe produce an infinite radar pulse, staggered by a negative delay so a new ring leaves before the last one dies — and the pulse politely stops once the video is playing, because a control that keeps shouting after you've obeyed it is just noise.
## HTML
```html
<section class="pp-13" aria-label="Pulsing halo video play icon demo">
  <div class="pp-13__stage">
    <div class="pp-13__thumb">
      <img class="pp-13__img" src="https://images.unsplash.com/photo-1536440136628-849c177e76a1?q=80&w=1100&auto=format&fit=crop" alt="" loading="lazy">
      <span class="pp-13__scrim" aria-hidden="true"></span>
      <input class="pp-13-chk" type="checkbox" id="pp-13-toggle" aria-label="Play or pause the trailer">
      <label class="pp-13__btn" for="pp-13-toggle">
        <svg viewBox="0 0 24 24" width="30" height="30" aria-hidden="true">
          <path class="pp-13__p" d="M9 5.4v13.2L19.2 12z" fill="currentColor"/>
          <path class="pp-13__q" d="M8.4 5.4h3.2v13.2H8.4zM12.8 5.4H16v13.2h-3.2z" fill="currentColor"/>
        </svg>
      </label>
      <div class="pp-13__meta">
        <p class="pp-13__kicker">Official trailer</p>
        <p class="pp-13__title">The Long Descent</p>
      </div>
    </div>
    <p class="pp-13__chip" aria-hidden="true">two pseudo-element rings · negative delay stagger · scale + opacity only</p>
  </div>
</section>
```
## CSS
```css
.pp-13,
.pp-13 *,
.pp-13 *::before,
.pp-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pp-13 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--pp-13-bg);
  --pp-13-bg: oklch(0.13 0.015 265);
  --pp-13-ink: oklch(0.98 0.004 250);
  --pp-13-mut: oklch(0.72 0.02 255);
  --pp-13-halo: oklch(0.95 0.02 250);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--pp-13-ink);
}

.pp-13__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 22px;
  padding: clamp(18px,4vw,52px);
}

.pp-13__thumb {
  position: relative;
  width: min(100%,720px);
  aspect-ratio: 16/9;
  border-radius: 20px;
  overflow: hidden;
  background: linear-gradient(140deg,oklch(0.35 0.06 250),oklch(0.18 0.03 280));
  box-shadow: 0 30px 70px oklch(0 0 0/.55);
}

.pp-13__img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.pp-13__scrim {
  position: absolute;
  inset: 0;
  background: radial-gradient(45% 45% at 50% 50%,oklch(0 0 0/.42),transparent 70%),linear-gradient(to top,oklch(0 0 0/.7),transparent 55%);
}

.pp-13-chk {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.pp-13__btn {
  position: absolute;
  top: 50%;
  left: 50%;
  translate: -50% -50%;
  display: grid;
  place-items: center;
  width: 92px;
  height: 92px;
  border-radius: 50%;
  background: oklch(1 0 0/.16);
  border: 2px solid oklch(1 0 0/.55);
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
  color: var(--pp-13-ink);
  cursor: pointer;
  transition: background .3s,scale .3s cubic-bezier(.34,1.4,.5,1),opacity .3s;
}

.pp-13__btn::before,
.pp-13__btn::after {
  content: '';
  position: absolute;
  inset: -2px;
  border-radius: 50%;
  border: 2px solid var(--pp-13-halo);
  pointer-events: none;
  animation: pp-13-pulse 2.6s cubic-bezier(.25,.6,.3,1) infinite;
}

.pp-13__btn::after {
  animation-delay: -1.3s;
}

.pp-13__btn:hover {
  background: oklch(1 0 0/.28);
  scale: 1.06;
}

.pp-13-chk:focus-visible+.pp-13__btn {
  outline: 3px solid var(--pp-13-halo);
  outline-offset: 6px;
}

@keyframes pp-13-pulse {
  from {
    scale: 1;
    opacity: .8;
  }

  to {
    scale: 2.4;
    opacity: 0;
  }
}

.pp-13__q {
  display: none;
}

.pp-13__thumb:has(.pp-13-chk:checked) .pp-13__btn::before,
.pp-13__thumb:has(.pp-13-chk:checked) .pp-13__btn::after {
  animation: none;
  opacity: 0;
}

.pp-13__thumb:has(.pp-13-chk:checked) .pp-13__btn {
  scale: .82;
  opacity: .35;
}

.pp-13__thumb:has(.pp-13-chk:checked) .pp-13__btn:hover,
.pp-13__thumb:has(.pp-13-chk:checked) .pp-13__btn:focus-visible {
  opacity: 1;
  scale: .9;
}

.pp-13__thumb:has(.pp-13-chk:checked) .pp-13__p {
  display: none;
}

.pp-13__thumb:has(.pp-13-chk:checked) .pp-13__q {
  display: block;
}

.pp-13__thumb:has(.pp-13-chk:checked) .pp-13__scrim {
  opacity: .45;
}

.pp-13__meta {
  position: absolute;
  left: 26px;
  bottom: 24px;
}

.pp-13__kicker {
  font-size: 11px;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--pp-13-mut);
}

.pp-13__title {
  font-size: clamp(20px,3vw,28px);
  font-weight: 670;
  letter-spacing: -.02em;
  margin-top: 6px;
  text-shadow: 0 2px 14px oklch(0 0 0/.6);
}

.pp-13__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--pp-13-mut);
  padding: 7px 14px;
  border: 1px solid oklch(1 0 0/.13);
  border-radius: 99px;
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .pp-13__btn::before,
    .pp-13__btn::after {
    animation: none;
    opacity: 0;
  }

  .pp-13 * {
    transition-duration: .01ms !important;
  }
}
```
