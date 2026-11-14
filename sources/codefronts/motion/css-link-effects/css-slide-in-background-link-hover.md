---
source: "codefronts"
url: "https://codefronts.com/motion/css-link-effects/css-slide-in-background-link-hover/"
title: "CSS Slide-In Background Link Hover"
section: "motion"
category: "css-link-effects"
category_name: "CSS Link Effects"
description: "The button-fill classic, engineered properly: a background that slides in behind the label while the text color cross-fades in sync."
has_js: "false"
---

Here's a working CSS Link Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Slide-In Background Link Hover
Source: https://codefronts.com/motion/css-link-effects/css-slide-in-background-link-hover/

The button-fill classic, engineered properly: a background that slides in behind the label while the text color cross-fades in sync. Three builds — a straight left-to-right fill, a skewed panel that glides through, and a two-tone fill where an accent sweep leads and the main color chases it 90ms behind.
## HTML
```html
<section class="cle-04" aria-label="Slide-in background hover demo">
  <div class="cle-04__stage">
    <div class="cle-04__var"><a href="#a" class="cle-04__fill">Start a project</a><small class="cle-04__cap">A · scaleX fill</small></div>
    <div class="cle-04__var"><a href="#b" class="cle-04__skew">See the work</a><small class="cle-04__cap">B · skewed glide</small></div>
    <div class="cle-04__var"><a href="#c" class="cle-04__duo">Book a call</a><small class="cle-04__cap">C · two-tone chase</small></div>
  </div>
</section>
```
## CSS
```css
.cle-04,
.cle-04 *,
.cle-04 *::before,
.cle-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cle-04 {
  width: 100%;
  min-height: 100vh;
  --ink: oklch(0.24 0.02 270);
  --brand: oklch(0.5 0.21 272);
  --lead: oklch(0.72 0.19 330);
  --paper: oklch(0.99 0.003 270);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.cle-04__stage {
  width: 100%;
  height: 100vh;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
  gap: 44px 52px;
  border: 1px solid oklch(0.9 0.012 270);
  background: linear-gradient(160deg,oklch(0.975 0.008 270),oklch(0.94 0.018 285));
  padding: 44px 36px;
}

.cle-04__var {
  display: grid;
  gap: 14px;
  justify-items: center;
}

.cle-04__cap {
  font-size: 10.5px;
  font-weight: 600;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: oklch(0.55 0.03 275);
}

.cle-04 a {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  display: inline-block;
  padding: 16px 32px;
  border-radius: 999px;
  border: 1.5px solid oklch(0.55 0.1 272 / .45);
  background: var(--paper);
  color: var(--ink);
  text-decoration: none;
  font-size: 15.5px;
  font-weight: 700;
  letter-spacing: .02em;
  transition: color .3s,border-color .3s;
  box-shadow: 0 10px 26px -18px oklch(0.4 0.15 272 / .55);
}

.cle-04 a:focus-visible {
  outline: 3px solid var(--brand);
  outline-offset: 3px;
}

.cle-04 a::before,
.cle-04 a::after {
  content: "";
  position: absolute;
  inset: 0;
  z-index: -1;
}

.cle-04 a:hover,
.cle-04 a:focus-visible {
  color: oklch(0.99 0.005 272);
  border-color: transparent;
}

.cle-04__fill::before {
  background: var(--brand);
  transform: scaleX(0);
  transform-origin: left;
  transition: transform .38s cubic-bezier(.25,.8,.25,1);
}

.cle-04__fill:hover::before,
.cle-04__fill:focus-visible::before {
  transform: scaleX(1);
}

.cle-04__skew::before {
  inset: -2px -22%;
  background: linear-gradient(120deg,var(--brand),oklch(0.42 0.19 290));
  transform: translateX(-118%) skewX(-16deg);
  transition: transform .45s cubic-bezier(.3,.8,.25,1);
}

.cle-04__skew:hover::before,
.cle-04__skew:focus-visible::before {
  transform: translateX(0) skewX(-16deg);
}

.cle-04__duo::before,
.cle-04__duo::after {
  transform: scaleX(0);
  transform-origin: left;
  transition: transform .4s cubic-bezier(.25,.8,.25,1);
}

.cle-04__duo::before {
  background: var(--lead);
}

.cle-04__duo::after {
  background: var(--brand);
  transition-delay: 90ms;
}

.cle-04__duo:hover::before,
.cle-04__duo:hover::after,
.cle-04__duo:focus-visible::before,
.cle-04__duo:focus-visible::after {
  transform: scaleX(1);
}

.cle-04__duo:hover,
.cle-04__duo:focus-visible {
  transition-delay: 60ms;
}

@media (prefers-reduced-motion: reduce) {
  .cle-04 * {
    transition-duration: .01s !important;
    transition-delay: 0s !important;
  }
}
```
