---
source: "codefronts"
url: "https://codefronts.com/navigation/css-accordions/vinyl-spine/"
title: "Vinyl Spine Horizontal Accordion — Record Shelf with Pull-Out Sleeves"
section: "navigation"
category: "css-accordions"
category_name: "CSS Accordions — Vertical & Horizontal"
description: "A crate of records you can flip through: collapsed panels are album spines — textured cardboard edges with the artist name running down them — and the…"
has_js: "false"
---

Here's a working CSS Accordions — Vertical & Horizontal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Vinyl Spine Horizontal Accordion — Record Shelf with Pull-Out Sleeves
Source: https://codefronts.com/navigation/css-accordions/vinyl-spine/

A crate of records you can flip through: collapsed panels are album spines — textured cardboard edges with the artist name running down them — and the selected one pulls out to reveal its full sleeve, a spinning vinyl disc peeking from the edge. Skeuomorphism with a purpose: everyone already knows how to browse a shelf.
## HTML
```html
<section class="acc-20" aria-label="Vinyl record shelf accordion demo">
  <div class="acc-20__shelf" role="group" aria-label="Record crate">
    <div class="acc-20__panel" style="--sleeve:oklch(0.55 0.19 25);--sleeve2:oklch(0.3 0.1 25)">
      <input type="radio" name="acc-20" id="acc-20-a" checked>
      <label class="acc-20__face" for="acc-20-a">
        <span class="acc-20__spine"><span class="acc-20__artist">Marlowe Quartet</span><span class="acc-20__cat">MQ-004</span></span>
        <span class="acc-20__sleeve"><span class="acc-20__disc"></span><span class="acc-20__art"></span><span class="acc-20__meta"><b>Night Currents</b><i>Marlowe Quartet · 1974</i><p>Modal jazz cut live to tape in one November evening. Side B is a single 19-minute take.</p></span></span>
      </label>
    </div>
    <div class="acc-20__panel" style="--sleeve:oklch(0.5 0.12 250);--sleeve2:oklch(0.25 0.08 250)">
      <input type="radio" name="acc-20" id="acc-20-b">
      <label class="acc-20__face" for="acc-20-b">
        <span class="acc-20__spine"><span class="acc-20__artist">Sofia Reyes Trio</span><span class="acc-20__cat">SR-011</span></span>
        <span class="acc-20__sleeve"><span class="acc-20__disc"></span><span class="acc-20__art"></span><span class="acc-20__meta"><b>Harbor Lights</b><i>Sofia Reyes Trio · 1981</i><p>Bossa-inflected standards recorded in a converted lighthouse. The foghorn on track 3 was not planned.</p></span></span>
      </label>
    </div>
    <div class="acc-20__panel" style="--sleeve:oklch(0.6 0.14 140);--sleeve2:oklch(0.3 0.09 140)">
      <input type="radio" name="acc-20" id="acc-20-c">
      <label class="acc-20__face" for="acc-20-c">
        <span class="acc-20__spine"><span class="acc-20__artist">The Meridian Six</span><span class="acc-20__cat">ME-023</span></span>
        <span class="acc-20__sleeve"><span class="acc-20__disc"></span><span class="acc-20__art"></span><span class="acc-20__meta"><b>Slow Orbit</b><i>The Meridian Six · 1977</i><p>Six horns, no rhythm section. Somehow it swings anyway — the arranger never explained how.</p></span></span>
      </label>
    </div>
  </div>
</section>
```
## CSS
```css
.acc-20,
.acc-20 *,
.acc-20 *::before,
.acc-20 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.acc-20 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #241f1b;
  padding: 44px 24px;
}

.acc-20__shelf {
  display: flex;
  gap: 6px;
  width: min(780px,100%);
  height: 400px;
  padding: 14px;
  background: #33291f;
  border-radius: 14px;
  box-shadow: inset 0 2px 12px rgba(0,0,0,.5);
}

.acc-20__panel {
  display: flex;
  flex-grow: 1;
  flex-basis: 0;
  min-width: 72px;
  transition: flex-grow .55s cubic-bezier(.4,0,.2,1);
}

.acc-20__panel:has(input:checked) {
  flex-grow: 6;
}

.acc-20__panel input {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.acc-20__face {
  position: relative;
  flex: 1;
  display: block;
  cursor: pointer;
  border-radius: 6px;
  overflow: hidden;
}

.acc-20__spine {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  padding: 16px 0;
  background: var(--sleeve2) repeating-linear-gradient(90deg,rgba(255,255,255,.06) 0 2px,transparent 2px 7px);
  transition: opacity .3s .1s;
}

.acc-20__panel:has(input:checked) .acc-20__spine {
  opacity: 0;
}

.acc-20__artist {
  writing-mode: vertical-rl;
  font-size: 14px;
  font-weight: 700;
  letter-spacing: .1em;
  color: #f2e9dc;
}

.acc-20__cat {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 10px;
  color: rgba(242,233,220,.6);
}

.acc-20__sleeve {
  position: absolute;
  inset: 0;
  opacity: 0;
  transition: opacity .35s .2s;
}

.acc-20__panel:has(input:checked) .acc-20__sleeve {
  opacity: 1;
}

.acc-20__art {
  position: absolute;
  inset: 0;
  background: linear-gradient(150deg,var(--sleeve) 0%,var(--sleeve2) 100%);
  box-shadow: inset 0 0 0 1px rgba(255,255,255,.12);
}

.acc-20__art::after {
  content: "";
  position: absolute;
  inset: 18px 18px auto;
  height: 44%;
  background: radial-gradient(140px 90px at 30% 40%,rgba(255,255,255,.35),transparent 70%),radial-gradient(180px 120px at 75% 60%,rgba(0,0,0,.3),transparent 70%);
  border-radius: 4px;
}

.acc-20__disc {
  position: absolute;
  top: 50%;
  right: -70px;
  translate: 0 -50%;
  width: 230px;
  height: 230px;
  border-radius: 50%;
  background: repeating-radial-gradient(circle at center,#111 0 1.5px,#1d1d1d 1.5px 3px);
  box-shadow: 0 6px 24px rgba(0,0,0,.55);
  transition: right .5s cubic-bezier(.3,1.1,.4,1) .15s;
  animation: acc-20-spin 1.8s linear infinite;
  animation-play-state: paused;
  z-index: 0;
}

.acc-20__disc::after {
  content: "";
  position: absolute;
  inset: 50%;
  translate: -50% -50%;
  width: 74px;
  height: 74px;
  border-radius: 50%;
  background: var(--sleeve);
  border: 2px solid #0d0d0d;
}

.acc-20__panel:has(input:checked) .acc-20__disc {
  right: -40px;
  animation-play-state: running;
}

@keyframes acc-20-spin {
  to {
    rotate: 360deg;
  }
}

.acc-20__meta {
  position: absolute;
  inset: auto 0 0 0;
  z-index: 1;
  padding: 60px 22px 20px;
  background: linear-gradient(transparent,rgba(0,0,0,.68));
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.acc-20__meta b {
  font-size: 22px;
  font-weight: 800;
  color: #fff;
  letter-spacing: -.01em;
}

.acc-20__meta i {
  font-style: normal;
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: rgba(255,255,255,.75);
}

.acc-20__meta p {
  font-size: 13px;
  line-height: 1.55;
  color: rgba(255,255,255,.85);
  max-width: 44ch;
}

.acc-20__panel:has(input:focus-visible) .acc-20__face {
  outline: 3px solid #f2e9dc;
  outline-offset: 3px;
}

@media (max-width: 620px) {
  .acc-20__shelf {
    flex-direction: column;
    height: auto;
  }

  .acc-20__panel {
    min-height: 64px;
  }

  .acc-20__panel:has(input:checked) {
    min-height: 300px;
  }

  .acc-20__artist {
    writing-mode: horizontal-tb;
  }

  .acc-20__spine {
    flex-direction: row;
    padding: 0 18px;
    align-items: center;
  }
}

@media (prefers-reduced-motion: reduce) {
  .acc-20__disc {
    animation: none;
    transition: none;
  }

  .acc-20__panel,
    .acc-20__spine,
    .acc-20__sleeve {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — spines expand via flex-grow; the vinyl disc is concentric repeating-radial-gradient grooves whose spin animation is always declared but paused, flipping to running only while its radio is checked. */
```
