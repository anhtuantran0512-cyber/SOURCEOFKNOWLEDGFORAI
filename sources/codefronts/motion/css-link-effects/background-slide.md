---
source: "codefronts"
url: "https://codefronts.com/motion/css-link-effects/background-slide/"
title: "CSS Background Slide Link Hover"
section: "motion"
category: "css-link-effects"
category_name: "CSS Link Effects"
description: "Directional fills for real navigation — squared menu items in an app bar, not pill buttons (that's demo 04; this is its edge-to-edge sibling)."
has_js: "false"
---

Here's a working CSS Link Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Background Slide Link Hover
Source: https://codefronts.com/motion/css-link-effects/background-slide/

Directional fills for real navigation — squared menu items in an app bar, not pill buttons (that's demo 04; this is its edge-to-edge sibling). A panel that rises from the baseline, doors that close outward from the centerline, and a diagonal blade wipe via clip-path. All compositor-only, all with the label color cross-fading on the same clock.
## HTML
```html
<section class="cle-18" aria-label="Background slide nav demo">
  <div class="cle-18__stage">
    <nav class="cle-18__bar" aria-label="App sections">
      <span class="cle-18__brand" aria-hidden="true">◆ Ledgerline</span>
      <div class="cle-18__links">
        <a href="#a" class="cle-18__rise" aria-current="page">Dashboard</a>
        <a href="#a2" class="cle-18__rise">Reports</a>
        <a href="#b" class="cle-18__doors">Forecasts</a>
        <a href="#c" class="cle-18__blade">Settings</a>
      </div>
    </nav>
    <div class="cle-18__legend"><small class="cle-18__cap">A · rise from baseline</small><small class="cle-18__cap">B · center-out doors</small><small class="cle-18__cap">C · diagonal blade</small></div>
  </div>
</section>
```
## CSS
```css
.cle-18,
.cle-18 *,
.cle-18 *::before,
.cle-18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cle-18 {
  width: 100%;
  min-height: 100vh;
  --bar: oklch(0.23 0.02 265);
  --txt: oklch(0.88 0.02 265);
  --accent: oklch(0.82 0.15 85);
  --on: oklch(0.24 0.04 85);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.cle-18__stage {
  width: 100%;
  height: 100vh;
  display: grid;
  align-content: center;
  justify-items: center;
  gap: 36px;
  border: 1px solid oklch(0.9 0.012 265);
  background: linear-gradient(170deg,oklch(0.96 0.008 265),oklch(0.92 0.015 265));
  padding: 44px 28px;
}

.cle-18__bar {
  display: flex;
  align-items: stretch;
  gap: 26px;
  width: min(680px,100%);
  padding: 0 10px 0 24px;
  border-radius: 14px;
  background: var(--bar);
  box-shadow: 0 20px 44px -24px oklch(0.2 0.04 265 / .8);
}

.cle-18__brand {
  align-self: center;
  color: var(--accent);
  font-weight: 700;
  font-size: 14.5px;
  letter-spacing: .04em;
  margin-right: auto;
}

.cle-18__links {
  display: flex;
}

.cle-18 a {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  display: grid;
  place-items: center;
  padding: 20px 20px;
  color: var(--txt);
  text-decoration: none;
  font-size: 14px;
  font-weight: 600;
  letter-spacing: .02em;
  transition: color .3s;
}

.cle-18 a:hover,
.cle-18 a:focus-visible,
.cle-18 a[aria-current="page"] {
  color: var(--on);
}

.cle-18 a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: -4px;
}

.cle-18 a::before,
.cle-18 a::after {
  content: "";
  position: absolute;
  inset: 0;
  z-index: -1;
  background: var(--accent);
}

.cle-18__rise::before {
  translate: 0 101%;
  transition: translate .35s cubic-bezier(.3,.8,.25,1);
}

.cle-18__rise:hover::before,
.cle-18__rise:focus-visible::before,
.cle-18__rise[aria-current="page"]::before {
  translate: 0 0;
}

.cle-18__rise::after {
  content: none;
}

.cle-18__doors::before {
  right: 50%;
  transform-origin: right;
  scale: 0 1;
  transition: scale .32s cubic-bezier(.3,.8,.25,1);
}

.cle-18__doors::after {
  left: 50%;
  transform-origin: left;
  scale: 0 1;
  transition: scale .32s cubic-bezier(.3,.8,.25,1);
}

.cle-18__doors:hover::before,
.cle-18__doors:hover::after,
.cle-18__doors:focus-visible::before,
.cle-18__doors:focus-visible::after {
  scale: 1 1;
}

.cle-18__blade::before {
  clip-path: polygon(-35% 0,-20% 0,-35% 100%,-50% 100%);
  transition: clip-path .4s cubic-bezier(.3,.8,.25,1);
}

.cle-18__blade::after {
  content: none;
}

.cle-18__blade:hover::before,
.cle-18__blade:focus-visible::before {
  clip-path: polygon(-35% 0,115% 0,100% 100%,-50% 100%);
}

.cle-18__legend {
  display: flex;
  flex-wrap: wrap;
  gap: 32px;
}

.cle-18__cap {
  font-size: 10.5px;
  font-weight: 600;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: oklch(0.55 0.03 265);
}

@media (prefers-reduced-motion: reduce) {
  .cle-18 * {
    transition-duration: .01s !important;
  }
}
```
