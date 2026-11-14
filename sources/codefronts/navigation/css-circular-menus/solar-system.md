---
source: "codefronts"
url: "https://codefronts.com/navigation/css-circular-menus/solar-system/"
title: "Solar System Radial Submenu Navigation"
section: "navigation"
category: "css-circular-menus"
category_name: "CSS Circular Menus"
description: "A two-level radial system: three 'planets' orbit the sun, and selecting a planet spawns its own ring of 'moons' — child links orbiting the child."
has_js: "true"
---

Here's a working CSS Circular Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Solar System Radial Submenu Navigation
Source: https://codefronts.com/navigation/css-circular-menus/solar-system/

A two-level radial system: three 'planets' orbit the sun, and selecting a planet spawns its own ring of 'moons' — child links orbiting the child. It solves the real problem flat radial menus can't: hierarchy. Categories on ring one, their contents on ring two, with the selected planet enlarging into a local hub.
## HTML
```html
<section class="ccm-18" aria-label="Solar system nested menu demo">
  <div class="ccm-18__stage">
    <nav class="ccm-18__space" style="--n:3" aria-label="Product areas">
      <span class="ccm-18__orbitline" aria-hidden="true"></span>
      <div class="ccm-18__sun">Docs</div>
      <ul class="ccm-18__planets">
        <li class="ccm-18__planet" style="--i:0">
          <button type="button" aria-expanded="false">Guides</button>
          <ul class="ccm-18__moons" style="--n:3">
            <li style="--i:0"><a href="#quickstart">Quickstart</a></li>
            <li style="--i:1"><a href="#tutorials">Tutorials</a></li>
            <li style="--i:2"><a href="#recipes">Recipes</a></li>
          </ul>
        </li>
        <li class="ccm-18__planet" style="--i:1">
          <button type="button" aria-expanded="false">API</button>
          <ul class="ccm-18__moons" style="--n:3">
            <li style="--i:0"><a href="#rest">REST</a></li>
            <li style="--i:1"><a href="#graphql">GraphQL</a></li>
            <li style="--i:2"><a href="#webhooks">Webhooks</a></li>
          </ul>
        </li>
        <li class="ccm-18__planet" style="--i:2">
          <button type="button" aria-expanded="false">SDKs</button>
          <ul class="ccm-18__moons" style="--n:3">
            <li style="--i:0"><a href="#js">JavaScript</a></li>
            <li style="--i:1"><a href="#python">Python</a></li>
            <li style="--i:2"><a href="#go">Go</a></li>
          </ul>
        </li>
      </ul>
    </nav>
    <p class="ccm-18__note">Click a planet to reveal its moons</p>
  </div>
</section>
```
## CSS
```css
.ccm-18,
.ccm-18 *,
.ccm-18 *::before,
.ccm-18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccm-18 {
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: radial-gradient(circle at 50% 45%,oklch(0.26 0.04 265),oklch(0.17 0.03 275) 75%);
  --brand: oklch(0.75 0.13 200);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: oklch(0.92 0.01 220);
}

.ccm-18__stage {
  width: 100%;
  height: 100vh;
  position: relative;
  display: grid;
  place-items: center;
  border-radius: 20px;
  background: radial-gradient(circle at 50% 45%,oklch(0.26 0.04 265),oklch(0.17 0.03 275) 75%);
  overflow: hidden;
}

.ccm-18__space {
  position: relative;
  width: 200px;
  height: 200px;
  display: grid;
  place-items: center;
  --pr: 140px;
}

.ccm-18__orbitline {
  position: absolute;
  inset: 50%;
  width: calc(var(--pr) * 2);
  height: calc(var(--pr) * 2);
  translate: -50% -50%;
  border-radius: 50%;
  border: 1px dashed oklch(0.6 0.06 250 / .3);
}

.ccm-18__sun {
  display: grid;
  place-items: center;
  width: 96px;
  height: 96px;
  border-radius: 50%;
  background: radial-gradient(circle at 35% 30%,oklch(0.85 0.13 85),oklch(0.7 0.16 60));
  color: oklch(0.3 0.06 65);
  font-weight: 800;
  font-size: 17px;
  letter-spacing: .01em;
  box-shadow: 0 0 60px -8px oklch(0.8 0.15 75 / .6);
}

.ccm-18__planets {
  position: absolute;
  inset: 0;
  list-style: none;
}

.ccm-18__planet {
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  pointer-events: none;
  --a: calc((360deg / var(--n)) * var(--i) - 90deg);
  translate: calc(cos(var(--a)) * var(--pr)) calc(sin(var(--a)) * var(--pr));
}

.ccm-18__planet > button {
  pointer-events: auto;
  width: 72px;
  height: 72px;
  border-radius: 50%;
  border: 1px solid oklch(0.65 0.09 210 / .5);
  background: radial-gradient(circle at 35% 30%,oklch(0.45 0.09 215),oklch(0.32 0.07 230));
  color: #fff;
  font: 700 13px/1 'Segoe UI',system-ui,sans-serif;
  cursor: pointer;
  box-shadow: 0 12px 30px -12px oklch(0 0 0 / .8);
  transition: scale .4s cubic-bezier(.32,1.25,.4,1),opacity .3s,box-shadow .3s;
}

.ccm-18__planet > button:hover {
  scale: 1.1;
}

.ccm-18__planet > button:focus-visible {
  outline: 3px solid var(--brand);
  outline-offset: 4px;
}

.ccm-18__planet.is-open > button {
  scale: 1.35;
  box-shadow: 0 0 0 5px oklch(0.75 0.13 200 / .3),0 12px 30px -12px oklch(0 0 0 / .8);
}

.ccm-18__planet.is-muted > button {
  opacity: .35;
  scale: .85;
}

.ccm-18__moons {
  position: absolute;
  inset: 0;
  list-style: none;
  --r: 86px;
  pointer-events: none;
}

.ccm-18__moons li {
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  pointer-events: none;
  --ma: calc((360deg / var(--n)) * var(--i) - 90deg);
  translate: 0 0;
  opacity: 0;
  scale: .3;
  visibility: hidden;
  transition: translate .45s cubic-bezier(.34,1.35,.4,1),opacity .25s,scale .45s cubic-bezier(.34,1.35,.4,1),visibility 0s .45s;
  transition-delay: calc(var(--i) * 45ms);
}

.ccm-18__planet.is-open .ccm-18__moons {
  pointer-events: auto;
}

.ccm-18__planet.is-open .ccm-18__moons li {
  translate: calc(cos(var(--ma)) * var(--r)) calc(sin(var(--ma)) * var(--r));
  opacity: 1;
  scale: 1;
  visibility: visible;
  transition: translate .45s cubic-bezier(.34,1.35,.4,1),opacity .25s,scale .45s cubic-bezier(.34,1.35,.4,1),visibility 0s;
  transition-delay: calc(.1s + var(--i) * 55ms);
}

.ccm-18__planet.is-open .ccm-18__moons a {
  pointer-events: auto;
}

.ccm-18__moons a {
  display: grid;
  place-items: center;
  min-width: 58px;
  height: 40px;
  padding: 0 12px;
  border-radius: 999px;
  background: oklch(0.9 0.02 210);
  color: oklch(0.28 0.05 230);
  text-decoration: none;
  font-size: 11.5px;
  font-weight: 700;
  box-shadow: 0 8px 20px -8px oklch(0 0 0 / .7);
  white-space: nowrap;
  transition: background .2s,scale .2s;
}

.ccm-18__moons a:hover,
.ccm-18__moons a:focus-visible {
  background: var(--brand);
  scale: 1.08;
  outline: none;
}

.ccm-18__moons a:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 2px;
}

.ccm-18__note {
  position: absolute;
  bottom: 20px;
  font-size: 12px;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: oklch(0.65 0.05 240 / .55);
}

@media (prefers-reduced-motion: reduce) {
  .ccm-18 * {
    transition-duration: .01s !important;
    transition-delay: 0s !important;
  }
}
```

## JavaScript
```js
(() => {
  const planets = [...document.querySelectorAll('.ccm-18__planet')];
  const closeAll = (except) => planets.forEach((p) => {
    if (p !== except) {
      p.classList.remove('is-open');
      p.querySelector('button').setAttribute('aria-expanded', 'false');
    }
    p.classList.toggle('is-muted', !!except && p !== except);
  });
  planets.forEach((p) => {
    const btn = p.querySelector('button');
    btn.addEventListener('click', () => {
      const opening = !p.classList.contains('is-open');
      closeAll(opening ? p : null);
      p.classList.toggle('is-open', opening);
      btn.setAttribute('aria-expanded', String(opening));
      if (opening) {
        const first = p.querySelector('.ccm-18__moons a');
        setTimeout(() => first && first.focus(), 480);
      }
    });
  });
  document.addEventListener('keydown', (e) => {
    if (e.key !== 'Escape') return;
    const open = planets.find((p) => p.classList.contains('is-open'));
    if (open) { closeAll(null); open.querySelector('button').focus(); }
  });
})();
```
