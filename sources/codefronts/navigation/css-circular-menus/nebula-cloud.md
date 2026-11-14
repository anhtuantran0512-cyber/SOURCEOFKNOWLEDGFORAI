---
source: "codefronts"
url: "https://codefronts.com/navigation/css-circular-menus/nebula-cloud/"
title: "Blurred Particle Radial Overlay"
section: "navigation"
category: "css-circular-menus"
category_name: "CSS Circular Menus"
description: "The full-takeover treatment: the trigger blooms into an overlay where six destinations circle a glowing core while soft bokeh particles drift through the…"
has_js: "true"
---

Here's a working CSS Circular Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Blurred Particle Radial Overlay
Source: https://codefronts.com/navigation/css-circular-menus/nebula-cloud/

The full-takeover treatment: the trigger blooms into an overlay where six destinations circle a glowing core while soft bokeh particles drift through the background blur. Built on a native dialog element, so focus trapping, Escape and inert-ing the page behind come free from the browser. The closing act for this collection — every technique from the previous 25 demos in one composition.
## HTML
```html
<section class="ccm-26" aria-label="Particle overlay menu demo">
  <div class="ccm-26__stage">
    <header class="ccm-26__fakehero"><h3>Aurora Festival '27</h3><p>Three nights of light, sound and code.</p>
      <button type="button" class="ccm-26__open">Explore the festival</button>
    </header>
    <dialog class="ccm-26__overlay" aria-label="Festival navigation">
      <div class="ccm-26__bokeh" aria-hidden="true"></div>
      <nav class="ccm-26__ringbox" style="--n:6">
        <ul class="ccm-26__ring">
          <li style="--i:0"><a href="#lineup">Lineup</a></li>
          <li style="--i:1"><a href="#tickets">Tickets</a></li>
          <li style="--i:2"><a href="#map">Map</a></li>
          <li style="--i:3"><a href="#food">Food</a></li>
          <li style="--i:4"><a href="#art">Art</a></li>
          <li style="--i:5"><a href="#faq">FAQ</a></li>
        </ul>
        <div class="ccm-26__coreglow"><b>AF</b><span>'27</span></div>
      </nav>
      <button type="button" class="ccm-26__close" aria-label="Close menu">✕</button>
    </dialog>
  </div>
</section>
```
## CSS
```css
.ccm-26,
.ccm-26 *,
.ccm-26 *::before,
.ccm-26 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccm-26 {
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(160deg,oklch(0.22 0.06 300),oklch(0.17 0.05 250) 55%,oklch(0.2 0.06 190));
  --brand: oklch(0.8 0.15 160);
  --brand2: oklch(0.7 0.17 310);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.ccm-26__stage {
  width: 100%;
  height: 100vh;
  position: relative;
  display: grid;
  place-items: center;
  border-radius: 20px;
  overflow: hidden;
  background: linear-gradient(160deg,oklch(0.22 0.06 300),oklch(0.17 0.05 250) 55%,oklch(0.2 0.06 190));
  color: #fff;
}

.ccm-26__fakehero {
  display: grid;
  justify-items: center;
  gap: 10px;
  text-align: center;
  padding: 20px;
}

.ccm-26__fakehero h3 {
  font-size: 30px;
  letter-spacing: -.02em;
  background: linear-gradient(90deg,var(--brand),var(--brand2));
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.ccm-26__fakehero p {
  color: oklch(0.8 0.03 260);
  font-size: 14.5px;
}

.ccm-26__open {
  margin-top: 14px;
  padding: 15px 28px;
  border: 1px solid oklch(0.8 0.1 200 / .5);
  border-radius: 999px;
  background: oklch(1 0 0 / .08);
  backdrop-filter: blur(6px);
  color: #fff;
  font: 700 14.5px/1 'Segoe UI',system-ui,sans-serif;
  letter-spacing: .03em;
  cursor: pointer;
  transition: background .25s,scale .25s;
  box-shadow: 0 0 40px -8px oklch(0.8 0.15 160 / .4);
}

.ccm-26__open:hover {
  background: oklch(1 0 0 / .16);
  scale: 1.04;
}

.ccm-26__open:focus-visible {
  outline: 3px solid var(--brand);
  outline-offset: 3px;
}

.ccm-26__overlay {
  position: fixed;
  inset: 0;
  width: 100%;
  height: 100%;
  max-width: none;
  max-height: none;
  border: none;
  background: transparent;
  display: grid;
  place-items: center;
  overflow: hidden;
  color: #fff;
}

.ccm-26__overlay:not([open]) {
  display: none;
}

.ccm-26__overlay::backdrop {
  background: radial-gradient(circle at 50% 50%,oklch(0.25 0.07 280 / .75),oklch(0.12 0.04 270 / .92));
  backdrop-filter: blur(18px);
}

.ccm-26__overlay[open] {
  animation: ccm26-in .5s cubic-bezier(.32,1.2,.4,1);
}

@keyframes ccm26-in {
  from {
    opacity: 0;
    scale: .92;
  }
}

.ccm-26__bokeh {
  position: absolute;
  inset: 0;
  pointer-events: none;
}

.ccm-26__bokeh span {
  position: absolute;
  border-radius: 50%;
  background: var(--c);
  filter: blur(var(--b));
  opacity: .5;
  animation: ccm26-drift var(--dur) ease-in-out infinite alternate,ccm26-sway var(--dur2) ease-in-out infinite alternate;
  animation-delay: var(--del),var(--del2);
}

.ccm-26__ringbox {
  position: relative;
  width: 150px;
  height: 150px;
  display: grid;
  place-items: center;
  --r: 150px;
}

.ccm-26__ring {
  position: absolute;
  inset: 0;
  list-style: none;
}

.ccm-26__ring li {
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  pointer-events: none;
  --a: calc((360deg / var(--n)) * var(--i) - 90deg);
  translate: calc(cos(var(--a)) * var(--r)) calc(sin(var(--a)) * var(--r));
}

.ccm-26__ring a {
  pointer-events: auto;
  display: grid;
  place-items: center;
  min-width: 92px;
  padding: 15px 20px;
  border-radius: 999px;
  background: oklch(1 0 0 / .09);
  border: 1px solid oklch(1 0 0 / .22);
  backdrop-filter: blur(8px);
  color: #fff;
  text-decoration: none;
  font-size: 14.5px;
  font-weight: 700;
  letter-spacing: .04em;
  transition: background .25s,border-color .25s,translate .25s,box-shadow .25s;
}

.ccm-26__ring a:hover,
.ccm-26__ring a:focus-visible {
  background: oklch(1 0 0 / .18);
  border-color: var(--brand);
  translate: 0 -4px;
  box-shadow: 0 0 34px -6px oklch(0.8 0.15 160 / .55);
  outline: none;
}

.ccm-26__ring a:focus-visible {
  outline: 2px solid var(--brand);
  outline-offset: 3px;
}

.ccm-26__coreglow {
  display: grid;
  place-items: center;
  width: 128px;
  height: 128px;
  border-radius: 50%;
  background: radial-gradient(circle at 38% 32%,oklch(0.35 0.09 250),oklch(0.22 0.06 270) 72%);
  border: 1px solid oklch(1 0 0 / .25);
  box-shadow: 0 0 90px -10px oklch(0.8 0.15 160 / .5),0 0 140px -20px oklch(0.7 0.17 310 / .45),inset 0 1px 0 oklch(1 0 0 / .2);
}

.ccm-26__coreglow b {
  font-size: 32px;
  letter-spacing: .06em;
  background: linear-gradient(90deg,var(--brand),var(--brand2));
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.ccm-26__coreglow span {
  font-size: 11px;
  letter-spacing: .3em;
  color: oklch(0.75 0.05 260);
}

.ccm-26__close {
  position: absolute;
  top: 26px;
  right: 26px;
  width: 48px;
  height: 48px;
  border-radius: 50%;
  border: 1px solid oklch(1 0 0 / .3);
  background: oklch(1 0 0 / .1);
  color: #fff;
  font-size: 16px;
  cursor: pointer;
  transition: background .2s,rotate .3s;
}

.ccm-26__close:hover {
  background: oklch(1 0 0 / .22);
  rotate: 90deg;
}

.ccm-26__close:focus-visible {
  outline: 3px solid var(--brand);
  outline-offset: 3px;
}

@keyframes ccm26-drift {
  from {
    translate: 0 26px;
  }

  to {
    translate: 0 -26px;
  }
}

@keyframes ccm26-sway {
  from {
    margin-left: -14px;
  }

  to {
    margin-left: 14px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ccm-26 * {
    animation: none !important;
    transition-duration: .01s !important;
  }
}
```

## JavaScript
```js
(() => {
  const stage = document.querySelector('.ccm-26__stage');
  const overlay = stage.querySelector('.ccm-26__overlay');
  const bokeh = overlay.querySelector('.ccm-26__bokeh');
  const hues = [160, 310, 250, 200];
  for (let i = 0; i < 16; i++) {
    const s = document.createElement('span');
    const size = 10 + Math.random() * 60;
    s.style.width = s.style.height = size.toFixed(0) + 'px';
    s.style.left = (Math.random() * 100).toFixed(1) + '%';
    s.style.top = (Math.random() * 100).toFixed(1) + '%';
    s.style.setProperty('--b', (size / 7).toFixed(1) + 'px');
    s.style.setProperty('--c', 'oklch(0.8 0.13 ' + hues[i % hues.length] + ' / .5)');
    s.style.setProperty('--dur', (7 + Math.random() * 9).toFixed(1) + 's');
    s.style.setProperty('--dur2', (9 + Math.random() * 11).toFixed(1) + 's');
    s.style.setProperty('--del', (-Math.random() * 12).toFixed(1) + 's');
    s.style.setProperty('--del2', (-Math.random() * 12).toFixed(1) + 's');
    bokeh.append(s);
  }
  stage.querySelector('.ccm-26__open').addEventListener('click', () => overlay.showModal());
  overlay.querySelector('.ccm-26__close').addEventListener('click', () => overlay.close());
})();
```
