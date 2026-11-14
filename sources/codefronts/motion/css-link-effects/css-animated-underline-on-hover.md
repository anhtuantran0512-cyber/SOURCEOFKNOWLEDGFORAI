---
source: "codefronts"
url: "https://codefronts.com/motion/css-link-effects/css-animated-underline-on-hover/"
title: "CSS Animated Underline on Hover"
section: "motion"
category: "css-link-effects"
category_name: "CSS Link Effects"
description: "The foundational link micro-interaction, four ways: grow from the left, bloom from the center, wipe straight through (enter left, exit right — the trick…"
has_js: "false"
---

Here's a working CSS Link Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Animated Underline on Hover
Source: https://codefronts.com/motion/css-link-effects/css-animated-underline-on-hover/

The foundational link micro-interaction, four ways: grow from the left, bloom from the center, wipe straight through (enter left, exit right — the trick everyone asks about), and the modern native route that animates text-underline-offset and text-decoration-thickness. Learn all four here and you can read 90% of the underline effects on the web.
## HTML
```html
<section class="cle-01" aria-label="Animated underline hover demo">
  <div class="cle-01__stage">
    <nav class="cle-01__nav" aria-label="Demo navigation">
      <span class="cle-01__logo" aria-hidden="true"></span>
      <a href="#work" class="cle-01__thru">Work</a>
      <a href="#studio" class="cle-01__thru">Studio</a>
      <a href="#journal" class="cle-01__thru">Journal</a>
      <a href="#contact" class="cle-01__thru">Contact</a>
    </nav>
    <div class="cle-01__row">
      <div class="cle-01__var"><a href="#a" class="cle-01__grow">Grow from left</a><small class="cle-01__cap">A · scale, origin left</small></div>
      <div class="cle-01__var"><a href="#b" class="cle-01__center">Bloom from center</a><small class="cle-01__cap">B · scale, origin center</small></div>
      <div class="cle-01__var"><a href="#c" class="cle-01__thru cle-01__big">Wipe through</a><small class="cle-01__cap">C · enters left, exits right</small></div>
      <div class="cle-01__var"><a href="#d" class="cle-01__native">Native decoration</a><small class="cle-01__cap">D · underline-offset + thickness</small></div>
    </div>
  </div>
</section>
```
## CSS
```css
.cle-01,
.cle-01 *,
.cle-01 *::before,
.cle-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cle-01 {
  width: 100%;
  min-height: 100vh;
  --ink: oklch(0.25 0.02 262);
  --brand: oklch(0.55 0.21 262);
  --muted: oklch(0.55 0.02 262);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.cle-01__stage {
  width: 100%;
  height: 100vh;
  display: grid;
  align-content: center;
  justify-items: center;
  gap: 56px;
  border: 1px solid oklch(0.9 0.01 262);
  background: linear-gradient(175deg,oklch(0.99 0.004 262),oklch(0.955 0.012 262));
  padding: 44px 36px;
}

.cle-01__nav {
  display: flex;
  align-items: center;
  gap: 34px;
  padding: 16px 30px;
  border-radius: 999px;
  background: oklch(1 0 0 / .75);
  border: 1px solid oklch(0.91 0.012 262);
  box-shadow: 0 10px 30px -18px oklch(0.35 0.06 262 / .5);
}

.cle-01__logo {
  width: 22px;
  height: 22px;
  border-radius: 7px;
  background: conic-gradient(from 210deg,var(--brand),oklch(0.72 0.15 300));
}

.cle-01__row {
  display: flex;
  flex-wrap: wrap;
  gap: 44px 60px;
  justify-content: center;
}

.cle-01__var {
  display: grid;
  gap: 13px;
  justify-items: center;
}

.cle-01__cap {
  font-size: 10.5px;
  font-weight: 600;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
}

.cle-01 a {
  color: var(--ink);
  text-decoration: none;
  font-size: 15.5px;
  font-weight: 600;
  letter-spacing: .01em;
}

.cle-01 a:focus-visible {
  outline: 2px solid var(--brand);
  outline-offset: 5px;
  border-radius: 2px;
}

.cle-01__row a {
  font-size: 19px;
}

.cle-01__grow,
.cle-01__center {
  position: relative;
  padding-bottom: 5px;
}

.cle-01__grow::after,
.cle-01__center::after {
  content: "";
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  height: 2px;
  border-radius: 2px;
  background: var(--brand);
  scale: 0 1;
  transition: scale .35s cubic-bezier(.2,.7,.2,1);
}

.cle-01__grow::after {
  transform-origin: left;
}

.cle-01__center::after {
  transform-origin: center;
}

.cle-01__grow:hover::after,
.cle-01__grow:focus-visible::after,
.cle-01__center:hover::after,
.cle-01__center:focus-visible::after {
  scale: 1 1;
}

.cle-01__thru {
  background: linear-gradient(var(--brand),var(--brand)) no-repeat right bottom / 0% 2px;
  padding-bottom: 5px;
  transition: background-size .35s cubic-bezier(.2,.7,.2,1),color .25s;
}

.cle-01__thru:hover,
.cle-01__thru:focus-visible {
  background-position: left bottom;
  background-size: 100% 2px;
  color: var(--brand);
}

.cle-01__native {
  text-decoration: underline;
  text-decoration-color: oklch(0.82 0.02 262);
  text-decoration-thickness: 1.5px;
  text-underline-offset: 4px;
  transition: text-decoration-color .3s,text-underline-offset .3s,text-decoration-thickness .3s;
}

.cle-01__native:hover,
.cle-01__native:focus-visible {
  text-decoration-color: var(--brand);
  text-underline-offset: 8px;
  text-decoration-thickness: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .cle-01 * {
    transition-duration: .01s !important;
  }
}
```
