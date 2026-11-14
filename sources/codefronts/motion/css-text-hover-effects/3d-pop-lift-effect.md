---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-hover-effects/3d-pop-lift-effect/"
title: "3D Pop / Lift Effect"
section: "motion"
category: "css-text-hover-effects"
category_name: "CSS Text Hover Effects"
description: "Type that physically leaves the page: hover lifts the headline up and left while a six-layer text-shadow staircase extrudes beneath it and a soft blurred…"
has_js: "false"
---

Here's a working CSS Text Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: 3D Pop / Lift Effect
Source: https://codefronts.com/motion/css-text-hover-effects/3d-pop-lift-effect/

Type that physically leaves the page: hover lifts the headline up and left while a six-layer text-shadow staircase extrudes beneath it and a soft blurred shadow falls further away — the full lighting story of an object gaining altitude. The trick that makes it GLIDE instead of snap is the one nobody documents: shadow lists only interpolate when both states have the SAME number of layers, so the resting state declares all seven shadows at zero offset. Includes the pressed state (:active drops it back down) because a pop without a press feels broken.
## HTML
```html
<section class="cth-09" aria-label="3D pop lift text demo">
  <div class="cth-09__stage">
    <div class="cth-09__scene">
      <p class="cth-09__eyebrow">Riverside park &middot; Jan 30&ndash;31 &middot; all ages</p>
      <h1 class="cth-09__title"><a class="cth-09__pop" href="#cth09-top" id="cth09-top">JELLY<br>JAM &rsquo;26</a></h1>
      <p class="cth-09__sub">Two days of wobble-pop, jam stalls and the inflatable orchestra. Hover the headline &mdash; then actually press it.</p>
      <div class="cth-09__row">
        <a class="cth-09__btn cth-09__btn--solid" href="#cth09-top">Get tickets</a>
        <a class="cth-09__btn" href="#cth09-top">Line-up</a>
      </div>
      <p class="cth-09__hint">Same-length <code>text-shadow</code> lists interpolate &mdash; the extrusion grows, never blinks. <code>:active</code> presses it back into the page.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.cth-09,
.cth-09 *,
.cth-09 *::before,
.cth-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cth-09 {
  --bg: oklch(0.95 0.035 95);
  --ink: oklch(0.3 0.09 305);
  --side: oklch(0.68 0.19 30);
  --soft: oklch(0.3 0.08 300);
  --mut: oklch(0.48 0.05 300);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.cth-09__stage {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  background: radial-gradient(90% 70% at 50% 20%,oklch(0.97 0.025 95),var(--bg) 75%);
  padding: clamp(20px,4vw,56px);
  container: cth09/inline-size;
}

.cth-09__scene {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: clamp(16px,3cqi,24px);
}

.cth-09__eyebrow {
  font-size: 12.5px;
  font-weight: 800;
  letter-spacing: .24em;
  text-transform: uppercase;
  color: var(--mut);
}

.cth-09__title {
  line-height: .96;
}

.cth-09__pop {
  display: inline-block;
  font-size: clamp(58px,13cqi,132px);
  font-weight: 900;
  letter-spacing: -.015em;
  color: var(--ink);
  text-decoration: none;
  translate: 0 0;
  text-shadow: 0 0 0 var(--side),0 0 0 var(--side),0 0 0 var(--side),0 0 0 var(--side),0 0 0 var(--side),0 0 0 var(--side),0 0 0 transparent;
  transition: translate .3s cubic-bezier(.34,1.8,.4,1),text-shadow .3s cubic-bezier(.34,1.8,.4,1);
}

.cth-09__pop:hover,
.cth-09__pop:focus-visible {
  translate: .05em -.14em;
  text-shadow: .02em .02em 0 var(--side),.045em .045em 0 var(--side),.07em .07em 0 var(--side),.095em .095em 0 var(--side),.12em .12em 0 var(--side),.145em .145em 0 var(--side),.3em .42em 1em oklch(0.3 0.08 300/.35);
}

.cth-09__pop:active {
  translate: .01em .02em;
  text-shadow: .008em .008em 0 var(--side),.016em .016em 0 var(--side),.024em .024em 0 var(--side),.03em .03em 0 var(--side),.036em .036em 0 var(--side),.042em .042em 0 var(--side),.05em .08em .2em oklch(0.3 0.08 300/.3);
  transition-duration: .09s;
}

.cth-09__pop:focus-visible {
  outline: 3px solid var(--side);
  outline-offset: 10px;
  border-radius: 6px;
}

.cth-09__sub {
  font-size: 15px;
  line-height: 1.65;
  color: var(--mut);
  max-width: 44ch;
  font-weight: 550;
}

.cth-09__row {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 14px;
  margin-top: 4px;
}

.cth-09__btn {
  display: grid;
  place-items: center;
  min-height: 52px;
  padding: 0 26px;
  border-radius: 14px;
  font-size: 15.5px;
  font-weight: 800;
  text-decoration: none;
  color: var(--ink);
  border: 2.5px solid var(--ink);
  background: oklch(0.98 0.01 95);
  translate: 0 0;
  box-shadow: 0 0 0 0 var(--ink),0 0 0 0 transparent;
  transition: translate .22s cubic-bezier(.34,1.8,.4,1),box-shadow .22s cubic-bezier(.34,1.8,.4,1);
}

.cth-09__btn--solid {
  background: var(--side);
  border-color: var(--ink);
  color: oklch(0.98 0.01 95);
}

.cth-09__btn:hover,
.cth-09__btn:focus-visible {
  translate: -2px -5px;
  box-shadow: 4px 6px 0 0 var(--ink),10px 16px 26px -6px oklch(0.3 0.08 300/.3);
}

.cth-09__btn:active {
  translate: 1px 2px;
  box-shadow: 0 0 0 0 var(--ink),0 0 0 0 transparent;
  transition-duration: .08s;
}

.cth-09__btn:focus-visible {
  outline: 3px solid var(--side);
  outline-offset: 3px;
}

.cth-09__hint {
  font-size: 12.5px;
  color: var(--mut);
}

.cth-09__hint code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .9em;
  background: oklch(0.9 0.03 95);
  padding: 1px 6px;
  border-radius: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .cth-09 * {
    transition-duration: .01ms !important;
  }
}
```
