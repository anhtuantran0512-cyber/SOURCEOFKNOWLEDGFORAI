---
source: "codefronts"
url: "https://codefronts.com/motion/css-link-effects/css-border-draw-link-hover-effect/"
title: "CSS Border Draw Link Hover Effect"
section: "motion"
category: "css-link-effects"
category_name: "CSS Link Effects"
description: "Three box-link border animations, from classic to cutting-edge: a pen that traces the frame edge by edge using chained transition delays, corner brackets…"
has_js: "false"
---

Here's a working CSS Link Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Border Draw Link Hover Effect
Source: https://codefronts.com/motion/css-link-effects/css-border-draw-link-hover-effect/

Three box-link border animations, from classic to cutting-edge: a pen that traces the frame edge by edge using chained transition delays, corner brackets that grow until they meet as a full border, and a conic-gradient comet that orbits the frame — the gradient-angle animation made possible by @property.
## HTML
```html
<section class="cle-03" aria-label="Border draw hover demo">
  <div class="cle-03__stage">
    <div class="cle-03__var"><a href="#a" class="cle-03__draw"><span>Trace the frame</span></a><small class="cle-03__cap">A · pen trace, edge by edge</small></div>
    <div class="cle-03__var"><a href="#b" class="cle-03__corners"><span>Corners meet</span></a><small class="cle-03__cap">B · corners grow to a border</small></div>
    <div class="cle-03__var"><a href="#c" class="cle-03__comet">Comet orbit</a><small class="cle-03__cap">C · conic rim spin (@property)</small></div>
  </div>
</section>
```
## CSS
```css
.cle-03,
.cle-03 *,
.cle-03 *::before,
.cle-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

@property --clh03-a {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

.cle-03 {
  width: 100%;
  min-height: 100vh;
  --ink: oklch(0.93 0.01 250);
  --bg: oklch(0.23 0.02 255);
  --brand: oklch(0.78 0.14 190);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.cle-03__stage {
  width: 100%;
  height: 100vh;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
  gap: 48px 56px;
  background: linear-gradient(165deg,oklch(0.27 0.025 260),oklch(0.2 0.02 250));
  padding: 44px 36px;
}

.cle-03__var {
  display: grid;
  gap: 14px;
  justify-items: center;
}

.cle-03__cap {
  font-size: 10.5px;
  font-weight: 600;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: oklch(0.62 0.03 250);
}

.cle-03 a {
  position: relative;
  display: inline-block;
  padding: 16px 30px;
  color: var(--ink);
  text-decoration: none;
  font-size: 15px;
  font-weight: 600;
  letter-spacing: .05em;
  text-transform: uppercase;
}

.cle-03 a:focus-visible {
  outline: 2px solid var(--brand);
  outline-offset: 6px;
}

.cle-03__draw {
  background: oklch(1 0 0 / .04);
}

.cle-03__draw::before,
.cle-03__draw::after {
  content: "";
  position: absolute;
  width: 0;
  height: 0;
  border: 0 solid var(--brand);
}

.cle-03__draw::before {
  top: 0;
  left: 0;
  border-top-width: 2px;
  border-right-width: 2px;
  transition: height .14s linear,width .14s linear .14s;
}

.cle-03__draw::after {
  bottom: 0;
  right: 0;
  border-bottom-width: 2px;
  border-left-width: 2px;
  transition: height .14s linear .28s,width .14s linear .42s;
}

.cle-03__draw:hover::before,
.cle-03__draw:focus-visible::before {
  width: 100%;
  height: 100%;
  transition: width .14s linear,height .14s linear .14s;
}

.cle-03__draw:hover::after,
.cle-03__draw:focus-visible::after {
  width: 100%;
  height: 100%;
  transition: width .14s linear .28s,height .14s linear .42s;
}

.cle-03__corners span {
  position: static;
}

.cle-03__corners::before,
.cle-03__corners::after,
.cle-03__corners span::before,
.cle-03__corners span::after {
  content: "";
  position: absolute;
  width: 14px;
  height: 14px;
  border: 0 solid oklch(0.62 0.06 200);
  transition: width .35s cubic-bezier(.3,.7,.2,1),height .35s cubic-bezier(.3,.7,.2,1),border-color .35s;
}

.cle-03__corners::before {
  top: 0;
  left: 0;
  border-top-width: 2px;
  border-left-width: 2px;
}

.cle-03__corners::after {
  bottom: 0;
  right: 0;
  border-bottom-width: 2px;
  border-right-width: 2px;
}

.cle-03__corners span::before {
  top: 0;
  right: 0;
  border-top-width: 2px;
  border-right-width: 2px;
}

.cle-03__corners span::after {
  bottom: 0;
  left: 0;
  border-bottom-width: 2px;
  border-left-width: 2px;
}

.cle-03__corners:hover::before,
.cle-03__corners:hover::after,
.cle-03__corners:hover span::before,
.cle-03__corners:hover span::after,
.cle-03__corners:focus-visible::before,
.cle-03__corners:focus-visible::after,
.cle-03__corners:focus-visible span::before,
.cle-03__corners:focus-visible span::after {
  width: 100%;
  height: 100%;
  border-color: var(--brand);
}

.cle-03__comet {
  isolation: isolate;
  border-radius: 10px;
  background: oklch(0.26 0.025 255);
}

.cle-03__comet::before {
  content: "";
  position: absolute;
  inset: -3px;
  z-index: -1;
  border-radius: 13px;
  background: conic-gradient(from var(--clh03-a),transparent 0 72%,var(--brand) 88%,oklch(0.95 0.05 190));
  opacity: 0;
  transition: opacity .3s;
}

.cle-03__comet:hover::before,
.cle-03__comet:focus-visible::before {
  opacity: 1;
  animation: clh03-spin 1.2s linear infinite;
}

@keyframes clh03-spin {
  to {
    --clh03-a: 360deg;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cle-03 * {
    transition-duration: .01s !important;
    transition-delay: 0s !important;
    animation: none !important;
  }

  .cle-03__comet:hover::before {
    opacity: 1;
  }
}
```
