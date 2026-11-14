---
source: "codefronts"
url: "https://codefronts.com/navigation/css-navigation-menu-designs/css-neon-glow-navigation-menu/"
title: "CSS Neon Glow Navigation Menu"
section: "navigation"
category: "css-navigation-menu-designs"
category_name: "CSS Navigation Menus"
description: "A cyberpunk-inspired navigation menu with neon glow effects, flickering animations, and a dark grid background."
has_js: "false"
---

Here's a working CSS Navigation Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Neon Glow Navigation Menu
Source: https://codefronts.com/navigation/css-navigation-menu-designs/css-neon-glow-navigation-menu/

A cyberpunk-inspired navigation menu with neon glow effects, flickering animations, and a dark grid background. Active and hovered links pulse with multi-layer `box-shadow` and `text-shadow` glows in electric cyan and magenta, creating a retro-futuristic aesthetic.
## HTML
```html
<div class="nav-14">
  <nav class="nav-14__bar" role="navigation">
    <div class="nav-14__logo">NEO<span>N</span></div>
    <ul class="nav-14__links">
      <li>
        <a href="#" class="nav-14__active">
          <svg viewBox="0 0 24 24"><path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/></svg>
          Home
        </a>
      </li>
      <li>
        <a href="#">
          <svg viewBox="0 0 24 24"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>
          Systems
        </a>
      </li>
      <li>
        <a href="#">
          <svg viewBox="0 0 24 24"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>
          Network
        </a>
      </li>
      <li>
        <a href="#">
          <svg viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
          Security
        </a>
      </li>
      <li>
        <a href="#">
          <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="3"/><path d="M19.07 4.93l-1.41 1.41M5.34 18.66l-1.41 1.41M20 12h2M2 12H0M19.07 19.07l-1.41-1.41M5.34 5.34L3.93 3.93M12 20v2M12 2v2"/></svg>
          Config
        </a>
      </li>
    </ul>
    <a href="#" class="nav-14__btn">Access</a>
  </nav>
  <div class="nav-14__hero">
    <p class="nav-14__scantext">▶ System online — hover nav links above</p>
    <h1>
      <span>Navigate the</span>
      <span class="nav-14__neon-c">Cyber</span>
      <span class="nav-14__neon-m">Grid</span>
    </h1>
    <p>Each link has a neon underline that extends outward on hover via <code>left</code>/<code>right</code> transitions with a <code>box-shadow</code> glow. The top border has a scanning gradient animation.</p>
    <div class="nav-14__cards">
      <div class="nav-14__card">
        <svg viewBox="0 0 24 24"><rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8M12 17v4"/></svg>
        <div><p>Underline Glow</p><span>CSS box-shadow on ::after</span></div>
      </div>
      <div class="nav-14__card">
        <svg viewBox="0 0 24 24"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
        <div><p>Scan Gradient</p><span>CSS @keyframes on border</span></div>
      </div>
      <div class="nav-14__card">
        <svg viewBox="0 0 24 24"><path d="M22 19a2 2 0 01-2 2H4a2 2 0 01-2-2V5a2 2 0 012-2h5l2 3h9a2 2 0 012 2z"/></svg>
        <div><p>Fill Button</p><span>translateX slide-in reveal</span></div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.nav-14,
.nav-14 *,
.nav-14 *::before,
.nav-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.nav-14 ::selection {
  background: #00ff9d;
  color: #000;
}

.nav-14 {
  --bg: #030307;
  --text: #e8e8f0;
  --muted: #52527a;
  --cyan: #00e5ff;
  --green: #00ff9d;
  --magenta: #ff00ff;
  --amber: #ffaa00;
  --pink: #ff2d7f;
  font-family: 'Rajdhani',system-ui,sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}
/* grid lines bg */

.nav-14::before {
  content: '';
  position: fixed;
  inset: 0;
  background-image: linear-gradient(rgba(0,229,255,.03) 1px,transparent 1px), linear-gradient(90deg,rgba(0,229,255,.03) 1px,transparent 1px);
  background-size: 40px 40px;
  pointer-events: none;
  z-index: 0;
}

.nav-14__bar {
  position: relative;
  z-index: 100;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 48px;
  height: 68px;
  border-bottom: 1px solid rgba(0,229,255,.15);
  background: rgba(3,3,7,.8);
  backdrop-filter: blur(8px);
}
/* neon underline anim */

.nav-14__bar::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 1px;
  background: linear-gradient(90deg,transparent 0%,var(--cyan) 30%,var(--magenta) 70%,transparent 100%);
  opacity: .5;
  animation: nav-14-scanline 4s linear infinite;
}

@keyframes nav-14-scanline {
  0% {
    background-position: -100% 0;
  }

  100% {
    background-position: 200% 0;
  }
}

.nav-14__logo {
  font-size: 1.6rem;
  font-weight: 700;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--cyan);
  text-shadow: 0 0 12px var(--cyan),0 0 30px rgba(0,229,255,.4);
  display: flex;
  align-items: center;
  gap: 2px;
}

.nav-14__logo span {
  color: var(--magenta);
  text-shadow: 0 0 12px var(--magenta),0 0 30px rgba(255,0,255,.4);
}

.nav-14__links {
  display: flex;
  align-items: center;
  gap: 4px;
  list-style: none;
}

.nav-14__links a {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 8px 14px;
  color: var(--muted);
  text-decoration: none;
  font-size: .875rem;
  font-weight: 600;
  letter-spacing: .08em;
  text-transform: uppercase;
  border-radius: 4px;
  position: relative;
  transition: color .2s;
}

.nav-14__links a::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  right: 50%;
  height: 1.5px;
  background: currentColor;
  transition: left .25s ease,right .25s ease,box-shadow .25s;
}

.nav-14__links a:hover {
  color: var(--text);
}

.nav-14__links a:hover::after {
  left: 8px;
  right: 8px;
  box-shadow: 0 0 8px currentColor;
}

.nav-14__links a.nav-14__active {
  color: var(--cyan);
  text-shadow: 0 0 8px rgba(0,229,255,.5);
}

.nav-14__links a.nav-14__active::after {
  left: 8px;
  right: 8px;
  box-shadow: 0 0 8px var(--cyan);
}

.nav-14__links a svg {
  width: 14px;
  height: 14px;
  stroke: currentColor;
  fill: none;
  stroke-width: 2;
  opacity: .7;
}
/* neon circle btn */

.nav-14__btn {
  padding: 8px 20px;
  border-radius: 4px;
  background: transparent;
  border: 1px solid var(--cyan);
  color: var(--cyan);
  font-size: .8125rem;
  font-weight: 700;
  letter-spacing: .1em;
  text-transform: uppercase;
  text-decoration: none;
  transition: background .2s,box-shadow .2s,color .2s;
  position: relative;
  overflow: hidden;
}

.nav-14__btn::before {
  content: '';
  position: absolute;
  inset: 0;
  background: var(--cyan);
  transform: translateX(-101%);
  transition: transform .2s ease;
  z-index: -1;
}

.nav-14__btn:hover {
  color: #000;
  box-shadow: 0 0 20px rgba(0,229,255,.4);
}

.nav-14__btn:hover::before {
  transform: translateX(0);
}
/* hero */

.nav-14__hero {
  position: relative;
  z-index: 1;
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 80px 24px;
  text-align: center;
}

.nav-14__scantext {
  font-size: .7rem;
  font-weight: 600;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--cyan);
  margin-bottom: 28px;
  animation: nav-14-blink 2.5s step-end infinite;
}

@keyframes nav-14-blink {
  0%,
    100% {
    opacity: 1;
  }

  50% {
    opacity: .2;
  }
}

.nav-14__hero h1 {
  font-size: clamp(3rem,9vw,7rem);
  font-weight: 700;
  letter-spacing: .05em;
  text-transform: uppercase;
  color: transparent;
  -webkit-text-stroke: 1px rgba(255,255,255,.2);
  position: relative;
  margin-bottom: 8px;
  line-height: .95;
}

.nav-14__hero h1 span {
  display: block;
  color: var(--text);
  -webkit-text-stroke: 0;
  text-shadow: 0 0 40px rgba(0,229,255,.15);
}

.nav-14__hero h1 span.nav-14__neon-c {
  color: var(--cyan);
  text-shadow: 0 0 20px var(--cyan),0 0 50px rgba(0,229,255,.3);
  -webkit-text-stroke: 0;
}

.nav-14__hero h1 span.nav-14__neon-m {
  color: var(--magenta);
  text-shadow: 0 0 20px var(--magenta),0 0 50px rgba(255,0,255,.3);
  -webkit-text-stroke: 0;
}

.nav-14__hero p {
  font-size: 1rem;
  color: var(--muted);
  max-width: 480px;
  line-height: 1.65;
  margin-top: 28px;
}
/* floating nav cards */

.nav-14__cards {
  display: flex;
  flex-wrap: wrap;
  gap: 14px;
  margin-top: 48px;
  justify-content: center;
}

.nav-14__card {
  background: rgba(255,255,255,.025);
  border-radius: 8px;
  padding: 18px 24px;
  display: flex;
  align-items: center;
  gap: 12px;
  transition: border-color .2s,box-shadow .2s;
}

.nav-14__card:nth-child(1) {
  border: 1px solid rgba(0,229,255,.25);
}

.nav-14__card:nth-child(1):hover {
  border-color: var(--cyan);
  box-shadow: 0 0 20px rgba(0,229,255,.15);
}

.nav-14__card:nth-child(2) {
  border: 1px solid rgba(255,0,255,.2);
}

.nav-14__card:nth-child(2):hover {
  border-color: var(--magenta);
  box-shadow: 0 0 20px rgba(255,0,255,.12);
}

.nav-14__card:nth-child(3) {
  border: 1px solid rgba(0,255,157,.2);
}

.nav-14__card:nth-child(3):hover {
  border-color: var(--green);
  box-shadow: 0 0 20px rgba(0,255,157,.12);
}

.nav-14__card svg {
  width: 20px;
  height: 20px;
  flex-shrink: 0;
  stroke: currentColor;
  fill: none;
  stroke-width: 1.75;
}

.nav-14__card:nth-child(1) svg {
  color: var(--cyan);
}

.nav-14__card:nth-child(2) svg {
  color: var(--magenta);
}

.nav-14__card:nth-child(3) svg {
  color: var(--green);
}

.nav-14__card p {
  font-size: .8rem;
  font-weight: 600;
  letter-spacing: .04em;
  color: var(--text);
  text-transform: uppercase;
  margin: 0;
}

.nav-14__card span {
  font-size: .7rem;
  color: var(--muted);
  display: block;
  margin-top: 2px;
  text-transform: none;
  letter-spacing: 0;
}

@media (max-width: 680px) {
  .nav-14__links {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .nav-14__bar::after,
    .nav-14__scantext {
    animation: none;
  }

  .nav-14__links a::after,
    .nav-14__btn::before,
    .nav-14__links a,
    .nav-14__btn {
    transition: none;
  }
}
```
