---
source: "codefronts"
url: "https://codefronts.com/components/css-play-pause-buttons/liquid-wave/"
title: "Fluid Liquid Wave Fill Toggle"
section: "components"
category: "css-play-pause-buttons"
category_name: "CSS Play / Pause Buttons"
description: "Press play and the button fills with liquid: the level rises, two off-centre 'blobs' rotate behind the surface to make the meniscus ripple, and the icon…"
has_js: "false"
---

Here's a working CSS Play / Pause Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Fluid Liquid Wave Fill Toggle
Source: https://codefronts.com/components/css-play-pause-buttons/liquid-wave/

Press play and the button fills with liquid: the level rises, two off-centre 'blobs' rotate behind the surface to make the meniscus ripple, and the icon inverts as the fluid passes it. The wave is the classic border-radius-plus-rotate trick — no SVG filters, no canvas — and the entire thing runs on two transforms, so it stays smooth on a mid-range phone.
## HTML
```html
<section class="pp-12" aria-label="Liquid wave fill play pause toggle demo">
  <div class="pp-12__stage">
    <div class="pp-12__wrap">
      <input class="pp-12-chk" type="checkbox" id="pp-12-toggle" aria-label="Play or pause">
      <label class="pp-12__btn" for="pp-12-toggle">
        <span class="pp-12__liquid" aria-hidden="true"><i class="pp-12__wave"></i><i class="pp-12__wave pp-12__wave--b"></i></span>
        <svg class="pp-12__icon" viewBox="0 0 24 24" width="34" height="34" aria-hidden="true">
          <path class="pp-12__p" d="M9 5.6v12.8L19 12z" fill="currentColor"/>
          <path class="pp-12__q" d="M8.4 5.6h3.2v12.8H8.4zM12.8 5.6H16v12.8h-3.2z" fill="currentColor"/>
        </svg>
      </label>
      <p class="pp-12__cap">Tap to fill<span>level + two rolling waves</span></p>
    </div>
    <p class="pp-12__chip" aria-hidden="true">border-radius wave trick · mix-blend-mode: difference · transitioned level</p>
  </div>
</section>
```
## CSS
```css
.pp-12,
.pp-12 *,
.pp-12 *::before,
.pp-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pp-12 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--pp-12-bg);
  --pp-12-bg: oklch(0.21 0.04 235);
  --pp-12-ink: oklch(0.97 0.01 220);
  --pp-12-mut: oklch(0.7 0.03 225);
  --pp-12-liquid: oklch(0.72 0.15 195);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--pp-12-ink);
}

.pp-12__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 26px;
  padding: clamp(20px,5vw,56px);
  background: radial-gradient(65% 50% at 50% 45%,oklch(0.3 0.08 210/.7),transparent 70%);
}

.pp-12__wrap {
  display: grid;
  justify-items: center;
  gap: 24px;
}

.pp-12-chk {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.pp-12__btn {
  position: relative;
  display: grid;
  place-items: center;
  width: 150px;
  height: 150px;
  border-radius: 50%;
  border: 2px solid color-mix(in oklch,var(--pp-12-liquid) 55%,transparent);
  background: oklch(0.25 0.03 235);
  color: var(--pp-12-ink);
  cursor: pointer;
  overflow: hidden;
  isolation: isolate;
  box-shadow: 0 20px 50px oklch(0 0 0/.45),inset 0 0 30px oklch(0 0 0/.35);
  transition: border-color .5s,transform .25s cubic-bezier(.34,1.4,.5,1);
}

.pp-12__btn:hover {
  transform: scale(1.04);
}

.pp-12-chk:focus-visible+.pp-12__btn {
  outline: 3px solid var(--pp-12-liquid);
  outline-offset: 6px;
}

.pp-12__liquid {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  top: 100%;
  transition: top .9s cubic-bezier(.55,0,.2,1);
}

.pp-12__wave {
  position: absolute;
  left: -50%;
  top: -165%;
  width: 200%;
  aspect-ratio: 1;
  border-radius: 42% 46% 40% 44%;
  background: var(--pp-12-liquid);
  opacity: .9;
  animation: pp-12-roll 7s linear infinite;
}

.pp-12__wave--b {
  border-radius: 44% 40% 47% 43%;
  opacity: .55;
  animation-duration: 11s;
  animation-direction: reverse;
}

.pp-12__icon {
  position: relative;
  z-index: 2;
  mix-blend-mode: difference;
  color: oklch(0.99 0 0);
}

.pp-12__q {
  display: none;
}

.pp-12-chk:checked+.pp-12__btn {
  border-color: var(--pp-12-liquid);
}

.pp-12-chk:checked+.pp-12__btn .pp-12__liquid {
  top: 12%;
}

.pp-12-chk:checked+.pp-12__btn .pp-12__p {
  display: none;
}

.pp-12-chk:checked+.pp-12__btn .pp-12__q {
  display: block;
}

@keyframes pp-12-roll {
  to {
    rotate: 360deg;
  }
}

.pp-12__cap {
  text-align: center;
  font-size: 15px;
  font-weight: 640;
}

.pp-12__cap span {
  display: block;
  margin-top: 4px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  font-weight: 400;
  color: var(--pp-12-mut);
}

.pp-12__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--pp-12-mut);
  padding: 7px 14px;
  border: 1px solid oklch(1 0 0/.14);
  border-radius: 99px;
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .pp-12__wave {
    animation: none !important;
  }
}
```
