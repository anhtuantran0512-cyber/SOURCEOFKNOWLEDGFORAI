---
source: "codefronts"
url: "https://codefronts.com/navigation/css-circular-menus/service-orbit/"
title: "Circular Service Ring Navigation"
section: "navigation"
category: "css-circular-menus"
category_name: "CSS Circular Menus"
description: "An agency-style services ring: six service chips orbit a brand mark on a slow, hypnotic loop, staying perfectly upright the whole way thanks to the…"
has_js: "false"
---

Here's a working CSS Circular Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Circular Service Ring Navigation
Source: https://codefronts.com/navigation/css-circular-menus/service-orbit/

An agency-style services ring: six service chips orbit a brand mark on a slow, hypnotic loop, staying perfectly upright the whole way thanks to the counter-rotation trick. Hover anywhere and the orbit eases to a stop so the chips become easy targets. Zero JavaScript.
## HTML
```html
<section class="ccm-07" aria-label="Circular service ring demo">
  <div class="ccm-07__stage">
    <nav class="ccm-07__ring" style="--n:6" aria-label="Services">
      <span class="ccm-07__halo" aria-hidden="true"></span>
      <ul class="ccm-07__orbit">
        <li class="ccm-07__seat" style="--i:0"><a class="ccm-07__chip" href="#branding">Branding</a></li>
        <li class="ccm-07__seat" style="--i:1"><a class="ccm-07__chip" href="#web-design">Web design</a></li>
        <li class="ccm-07__seat" style="--i:2"><a class="ccm-07__chip" href="#motion">Motion</a></li>
        <li class="ccm-07__seat" style="--i:3"><a class="ccm-07__chip" href="#strategy">Strategy</a></li>
        <li class="ccm-07__seat" style="--i:4"><a class="ccm-07__chip" href="#content">Content</a></li>
        <li class="ccm-07__seat" style="--i:5"><a class="ccm-07__chip" href="#seo">SEO</a></li>
      </ul>
      <div class="ccm-07__mark"><b>ST</b><span>studio</span></div>
    </nav>
    <p class="ccm-07__note">Hover the ring to pause the orbit</p>
  </div>
</section>
```
## CSS
```css
.ccm-07,
.ccm-07 *,
.ccm-07 *::before,
.ccm-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccm-07 {
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: radial-gradient(circle at 50% 45%,oklch(0.3 0.03 60),oklch(0.2 0.02 50) 75%);
  --brand: oklch(0.78 0.14 85);
  --ink: oklch(0.93 0.01 85);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.ccm-07__stage {
  width: 100%;
  height: 100vh;
  position: relative;
  display: grid;
  place-items: center;
  border-radius: 20px;
  background: radial-gradient(circle at 50% 45%,oklch(0.3 0.03 60),oklch(0.2 0.02 50) 75%);
  overflow: hidden;
}

.ccm-07__ring {
  position: relative;
  width: 150px;
  height: 150px;
  display: grid;
  place-items: center;
  --r: 150px;
}

.ccm-07__halo {
  position: absolute;
  inset: calc(var(--r) * -1 + 75px - 27px);
  border-radius: 50%;
  border: 1px dashed oklch(0.7 0.08 85 / .35);
}

.ccm-07__orbit {
  position: absolute;
  inset: 0;
  list-style: none;
  animation: ccm07-spin 40s linear infinite;
}

.ccm-07__seat {
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  pointer-events: none;
  --a: calc((360deg / var(--n)) * var(--i) - 90deg);
  translate: calc(cos(var(--a)) * var(--r)) calc(sin(var(--a)) * var(--r));
}

.ccm-07__chip {
  pointer-events: auto;
  display: inline-block;
  padding: 11px 20px;
  border-radius: 999px;
  background: oklch(0.98 0.005 85 / .07);
  border: 1px solid oklch(0.85 0.1 85 / .3);
  backdrop-filter: blur(4px);
  color: var(--ink);
  text-decoration: none;
  font-size: 13.5px;
  font-weight: 600;
  letter-spacing: .02em;
  white-space: nowrap;
  animation: ccm07-spin 40s linear infinite reverse;
  transition: background .25s,border-color .25s,color .25s;
}

.ccm-07__chip:hover,
.ccm-07__chip:focus-visible {
  background: var(--brand);
  border-color: var(--brand);
  color: oklch(0.25 0.05 70);
  outline: none;
}

.ccm-07__chip:focus-visible {
  box-shadow: 0 0 0 3px oklch(0.25 0.05 70),0 0 0 6px var(--brand);
}

.ccm-07__ring:hover .ccm-07__orbit,
.ccm-07__ring:hover .ccm-07__chip,
.ccm-07__ring:focus-within .ccm-07__orbit,
.ccm-07__ring:focus-within .ccm-07__chip {
  animation-play-state: paused;
}

.ccm-07__mark {
  position: relative;
  z-index: 1;
  display: grid;
  place-items: center;
  width: 150px;
  height: 150px;
  border-radius: 50%;
  background: linear-gradient(150deg,oklch(0.34 0.04 70),oklch(0.24 0.03 55));
  border: 1px solid oklch(0.85 0.1 85 / .25);
  box-shadow: 0 0 80px -20px oklch(0.78 0.14 85 / .45),inset 0 1px 0 oklch(1 0 0 / .12);
}

.ccm-07__mark b {
  font-size: 34px;
  letter-spacing: .04em;
  color: var(--brand);
}

.ccm-07__mark span {
  font-size: 11px;
  letter-spacing: .3em;
  text-transform: uppercase;
  color: oklch(0.75 0.05 85);
}

.ccm-07__note {
  position: absolute;
  bottom: 20px;
  font-size: 12px;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: oklch(0.7 0.06 85 / .5);
}

@keyframes ccm07-spin {
  to {
    rotate: 360deg;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ccm-07__orbit,
    .ccm-07__chip {
    animation: none;
  }
}
```
