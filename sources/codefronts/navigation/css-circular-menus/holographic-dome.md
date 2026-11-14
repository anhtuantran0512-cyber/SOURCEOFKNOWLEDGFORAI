---
source: "codefronts"
url: "https://codefronts.com/navigation/css-circular-menus/holographic-dome/"
title: "Glowing Cyberpunk Radial UI"
section: "navigation"
category: "css-circular-menus"
category_name: "CSS Circular Menus"
description: "A sci-fi HUD ring: a scanning sweep rotates behind six neon nodes, dashed orbit rails counter-rotate at different speeds, and the whole thing hums with…"
has_js: "true"
---

Here's a working CSS Circular Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glowing Cyberpunk Radial UI
Source: https://codefronts.com/navigation/css-circular-menus/holographic-dome/

A sci-fi HUD ring: a scanning sweep rotates behind six neon nodes, dashed orbit rails counter-rotate at different speeds, and the whole thing hums with layered box-shadow glow. Every glow is pure CSS — no images, no canvas — making this the reference for game UIs, dashboards that want drama, and portfolio pieces.
## HTML
```html
<section class="ccm-16" aria-label="Cyberpunk radial HUD demo">
  <div class="ccm-16__stage">
    <nav class="ccm-16__hud" style="--n:6" aria-label="Ship systems">
      <span class="ccm-16__scan" aria-hidden="true"></span>
      <span class="ccm-16__rail ccm-16__rail--a" aria-hidden="true"></span>
      <span class="ccm-16__rail ccm-16__rail--b" aria-hidden="true"></span>
      <ul class="ccm-16__nodes">
        <li style="--i:0"><button type="button" class="is-active" aria-pressed="true" data-sys="NAV — plotting course">NAV</button></li>
        <li style="--i:1"><button type="button" aria-pressed="false" data-sys="SHIELDS — 94% integrity">SHD</button></li>
        <li style="--i:2"><button type="button" aria-pressed="false" data-sys="WEAPONS — safeties on">WPN</button></li>
        <li style="--i:3"><button type="button" aria-pressed="false" data-sys="COMMS — channel open">COM</button></li>
        <li style="--i:4"><button type="button" aria-pressed="false" data-sys="ENGINES — 62% thrust">ENG</button></li>
        <li style="--i:5"><button type="button" aria-pressed="false" data-sys="SENSORS — sweep active">SNS</button></li>
      </ul>
      <div class="ccm-16__core"><em>SYSTEM</em><output class="ccm-16__read" aria-live="polite">NAV — plotting course</output></div>
    </nav>
  </div>
</section>
```
## CSS
```css
.ccm-16,
.ccm-16 *,
.ccm-16 *::before,
.ccm-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccm-16 {
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: radial-gradient(circle at 50% 45%,oklch(0.22 0.03 240),var(--bg) 70%);
  --neon: oklch(0.85 0.15 190);
  --neon-dim: oklch(0.85 0.15 190 / .25);
  --bg: oklch(0.16 0.02 250);
  font-family: ui-monospace,'Cascadia Code',Menlo,monospace;
}

.ccm-16__stage {
  width: 100%;
  height: 100vh;
  position: relative;
  display: grid;
  place-items: center;
  border-radius: 20px;
  overflow: hidden;
  background: radial-gradient(circle at 50% 45%,oklch(0.22 0.03 240),var(--bg) 70%);
}

.ccm-16__stage::before {
  content: "";
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(0deg,transparent 0 3px,oklch(0 0 0 / .12) 3px 4px);
  pointer-events: none;
}

.ccm-16__hud {
  position: relative;
  width: 360px;
  height: 360px;
  display: grid;
  place-items: center;
}

.ccm-16__scan {
  position: absolute;
  inset: 14px;
  border-radius: 50%;
  background: conic-gradient(from 0deg,transparent 78%,var(--neon-dim) 98%,oklch(0.85 0.15 190 / .5));
  animation: ccm16-rot 6s linear infinite;
  mask: radial-gradient(circle,transparent 34%,black 35%);
}

.ccm-16__rail {
  position: absolute;
  border-radius: 50%;
}

.ccm-16__rail--a {
  inset: 0;
  border: 1px dashed oklch(0.7 0.1 190 / .4);
  animation: ccm16-rot 60s linear infinite;
}

.ccm-16__rail--b {
  inset: 38px;
  border: 1px dashed oklch(0.7 0.1 190 / .25);
  animation: ccm16-rot 45s linear infinite reverse;
}

.ccm-16__nodes {
  position: absolute;
  inset: 0;
  list-style: none;
}

.ccm-16__nodes li {
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  pointer-events: none;
  --a: calc((360deg / var(--n)) * var(--i) - 90deg);
  translate: calc(cos(var(--a)) * 152px) calc(sin(var(--a)) * 152px);
}

.ccm-16__nodes button {
  pointer-events: auto;
  width: 56px;
  height: 56px;
  border-radius: 50%;
  border: 1px solid oklch(0.7 0.12 190 / .6);
  background: oklch(0.2 0.03 230 / .9);
  color: var(--neon);
  font: 700 12px/1 ui-monospace,Menlo,monospace;
  letter-spacing: .08em;
  cursor: pointer;
  box-shadow: 0 0 6px oklch(0.85 0.15 190 / .25),inset 0 0 8px oklch(0.85 0.15 190 / .15);
  transition: box-shadow .25s,border-color .25s,color .25s,scale .25s;
}

.ccm-16__nodes button:hover,
.ccm-16__nodes button:focus-visible {
  border-color: var(--neon);
  box-shadow: 0 0 4px var(--neon),0 0 14px var(--neon-dim),inset 0 0 10px oklch(0.85 0.15 190 / .3);
  outline: none;
  scale: 1.08;
}

.ccm-16__nodes button:focus-visible {
  outline: 1px solid var(--neon);
  outline-offset: 5px;
}

.ccm-16__nodes button.is-active {
  background: var(--neon);
  color: oklch(0.18 0.03 230);
  box-shadow: 0 0 6px var(--neon),0 0 18px var(--neon),0 0 44px var(--neon-dim);
}

.ccm-16__core {
  position: relative;
  display: grid;
  justify-items: center;
  gap: 8px;
  width: 200px;
  height: 200px;
  border-radius: 50%;
  place-content: center;
  text-align: center;
  background: oklch(0.19 0.025 240 / .9);
  border: 1px solid oklch(0.7 0.12 190 / .5);
  box-shadow: inset 0 0 30px oklch(0.85 0.15 190 / .12),0 0 40px -10px oklch(0.85 0.15 190 / .3);
}

.ccm-16__core em {
  font-style: normal;
  font-size: 10px;
  letter-spacing: .4em;
  color: oklch(0.6 0.08 190);
}

.ccm-16__read {
  font-size: 13px;
  line-height: 1.5;
  color: var(--neon);
  text-shadow: 0 0 8px var(--neon-dim);
  max-width: 150px;
  animation: ccm16-flicker 4s linear infinite;
}

@keyframes ccm16-rot {
  to {
    rotate: 360deg;
  }
}

@keyframes ccm16-flicker {
  0%,
    91%,
    94%,
    98%,
    100% {
    opacity: 1;
  }

  92%,
    96% {
    opacity: .55;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ccm-16 * {
    animation: none !important;
    transition-duration: .01s !important;
  }
}
```

## JavaScript
```js
(() => {
  const hud = document.querySelector('.ccm-16__hud');
  const read = hud.querySelector('.ccm-16__read');
  hud.querySelectorAll('.ccm-16__nodes button').forEach((b) => {
    b.addEventListener('click', () => {
      hud.querySelectorAll('.ccm-16__nodes button').forEach((x) => { x.classList.remove('is-active'); x.setAttribute('aria-pressed', 'false'); });
      b.classList.add('is-active'); b.setAttribute('aria-pressed', 'true');
      read.textContent = b.dataset.sys;
    });
  });
})();
```
