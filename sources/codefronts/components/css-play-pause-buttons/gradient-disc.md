---
source: "codefronts"
url: "https://codefronts.com/components/css-play-pause-buttons/gradient-disc/"
title: "Conic Gradient Play Button with Rotating Rim CSS"
section: "components"
category: "css-play-pause-buttons"
category_name: "CSS Play / Pause Buttons"
description: "A gradient ring that actually rotates — not a spinning element, but an animated @property angle feeding a conic-gradient, clipped to a 3px rim by the…"
has_js: "false"
---

Here's a working CSS Play / Pause Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Conic Gradient Play Button with Rotating Rim CSS
Source: https://codefronts.com/components/css-play-pause-buttons/gradient-disc/

A gradient ring that actually rotates — not a spinning element, but an animated @property angle feeding a conic-gradient, clipped to a 3px rim by the mask-composite border trick. It is the modern way to build gradient borders (no wrapper divs, no background-clip hacks), and because the angle is a registered custom property, the browser can interpolate it on the compositor.
## HTML
```html
<section class="pp-17" aria-label="Conic gradient rotating rim play button demo">
  <div class="pp-17__stage">
    <div class="pp-17__wrap">
      <input class="pp-17-chk" type="checkbox" id="pp-17-toggle" aria-label="Play or pause the mix">
      <label class="pp-17__btn" for="pp-17-toggle">
        <svg viewBox="0 0 24 24" width="30" height="30" aria-hidden="true">
          <path class="pp-17__p" d="M9 5.6v12.8L19 12z" fill="currentColor"/>
          <path class="pp-17__q" d="M8.6 5.6h3.2v12.8H8.6zM12.8 5.6H16v12.8h-3.2z" fill="currentColor"/>
        </svg>
      </label>
      <div class="pp-17__meta">
        <p class="pp-17__title">Aurora Sessions 07</p>
        <p class="pp-17__sub">Continuous DJ mix · 62 min</p>
      </div>
    </div>
    <p class="pp-17__chip" aria-hidden="true">@property &lt;angle&gt; · conic-gradient(from …) · mask-composite rim</p>
  </div>
</section>
```
## CSS
```css
@property --pp-17-angle {
  syntax: '<angle>';
  initial-value: 0deg;
  inherits: false;
}

.pp-17,
.pp-17 *,
.pp-17 *::before,
.pp-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pp-17 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--pp-17-bg);
  --pp-17-bg: oklch(0.16 0.02 280);
  --pp-17-ink: oklch(0.97 0.006 270);
  --pp-17-mut: oklch(0.68 0.02 275);
  --pp-17-c1: oklch(0.8 0.17 200);
  --pp-17-c2: oklch(0.75 0.2 330);
  --pp-17-c3: oklch(0.85 0.16 95);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--pp-17-ink);
}

.pp-17__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 26px;
  padding: clamp(20px,5vw,56px);
  background: radial-gradient(60% 50% at 50% 45%,oklch(0.26 0.07 300/.6),transparent 72%);
}

.pp-17__wrap {
  display: grid;
  justify-items: center;
  gap: 22px;
  text-align: center;
}

.pp-17-chk {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.pp-17__btn {
  position: relative;
  display: grid;
  place-items: center;
  width: 128px;
  height: 128px;
  border-radius: 50%;
  background: oklch(0.21 0.025 280);
  color: var(--pp-17-ink);
  cursor: pointer;
  box-shadow: 0 20px 46px oklch(0 0 0/.5);
  transition: transform .26s cubic-bezier(.34,1.4,.5,1),background .3s;
}

.pp-17__btn:hover {
  transform: scale(1.05);
  background: oklch(0.24 0.03 280);
}

.pp-17__btn::before {
  content: '';
  position: absolute;
  inset: -3px;
  border-radius: 50%;
  padding: 3px;
  background: conic-gradient(from var(--pp-17-angle),var(--pp-17-c1),var(--pp-17-c2),var(--pp-17-c3),var(--pp-17-c1));
  -webkit-mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  animation: pp-17-spin 4s linear infinite;
  animation-play-state: paused;
}

.pp-17__btn::after {
  content: '';
  position: absolute;
  inset: -10px;
  border-radius: 50%;
  background: conic-gradient(from var(--pp-17-angle),var(--pp-17-c1),var(--pp-17-c2),var(--pp-17-c3),var(--pp-17-c1));
  filter: blur(18px);
  opacity: 0;
  z-index: -1;
  transition: opacity .5s;
  animation: pp-17-spin 4s linear infinite;
  animation-play-state: paused;
}

.pp-17-chk:focus-visible+.pp-17__btn {
  outline: 3px solid var(--pp-17-c1);
  outline-offset: 8px;
}

.pp-17__q {
  display: none;
}

.pp-17-chk:checked+.pp-17__btn::before,
.pp-17-chk:checked+.pp-17__btn::after {
  animation-play-state: running;
}

.pp-17-chk:checked+.pp-17__btn::after {
  opacity: .5;
}

.pp-17-chk:checked+.pp-17__btn .pp-17__p {
  display: none;
}

.pp-17-chk:checked+.pp-17__btn .pp-17__q {
  display: block;
}

@keyframes pp-17-spin {
  to {
    --pp-17-angle: 360deg;
  }
}

.pp-17__title {
  font-size: 19px;
  font-weight: 660;
  letter-spacing: -.015em;
}

.pp-17__sub {
  font-size: 13px;
  color: var(--pp-17-mut);
  margin-top: 5px;
}

.pp-17__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--pp-17-mut);
  padding: 7px 14px;
  border: 1px solid oklch(1 0 0/.13);
  border-radius: 99px;
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .pp-17__btn::before,
    .pp-17__btn::after {
    animation: none !important;
  }
}
```
