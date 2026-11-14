---
source: "codefronts"
url: "https://codefronts.com/motion/css-link-effects/encircled/"
title: "CSS Circle / Encircled Outline Hover Effect"
section: "motion"
category: "css-link-effects"
category_name: "CSS Link Effects"
description: "The hand-annotated look: hover and a pencil loop draws itself around the link, like a margin note from a good editor."
has_js: "false"
---

Here's a working CSS Link Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Circle / Encircled Outline Hover Effect
Source: https://codefronts.com/motion/css-link-effects/encircled/

The hand-annotated look: hover and a pencil loop draws itself around the link, like a margin note from a good editor. One wobbly inline-SVG path and the stroke-dasharray draw-on trick — plus a double-scribble variant and a soft ellipse highlight that stamps in behind the word. The pathLength attribute makes the dash math trivial.
## HTML
```html
<section class="cle-10" aria-label="Encircled link hover demo">
  <div class="cle-10__stage">
    <p class="cle-10__prose">The judges shortlisted <a href="#a" class="cle-10__loop">fourteen entries<svg viewBox="0 0 160 56" preserveAspectRatio="none" aria-hidden="true"><path d="M8 28 C10 12 62 5 102 7 C140 9 155 17 152 30 C149 45 106 53 60 50 C22 48 5 41 8 26 C9 21 14 17 22 14" pathLength="1"/></svg></a>, argued for an hour about <a href="#b" class="cle-10__scribble">two of them<svg viewBox="0 0 160 56" preserveAspectRatio="none" aria-hidden="true"><path d="M10 30 C12 14 70 6 108 9 C142 12 153 20 150 31 C147 44 100 52 58 49 C24 47 8 40 10 28 C12 13 76 3 116 7 C146 10 157 20 154 32 C150 46 96 55 52 51 C26 49 12 44 12 36" pathLength="1"/></svg></a>, and quietly agreed the winner had been <a href="#c" class="cle-10__stamp">obvious all along<svg viewBox="0 0 160 56" preserveAspectRatio="none" aria-hidden="true"><ellipse cx="80" cy="28" rx="74" ry="24"/></svg></a>.</p>
    <div class="cle-10__legend"><small class="cle-10__cap">A · pencil loop</small><small class="cle-10__cap">B · double scribble</small><small class="cle-10__cap">C · stamped ellipse</small></div>
  </div>
</section>
```
## CSS
```css
.cle-10,
.cle-10 *,
.cle-10 *::before,
.cle-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cle-10 {
  width: 100%;
  min-height: 100vh;
  --ink: oklch(0.28 0.03 60);
  --pen: oklch(0.6 0.19 30);
  font-family: Georgia,'Times New Roman',serif;
}

.cle-10__stage {
  width: 100%;
  height: 100vh;
  display: grid;
  align-content: center;
  justify-items: center;
  gap: 44px;
  border: 1px solid oklch(0.9 0.02 80);
  background: linear-gradient(175deg,oklch(0.985 0.01 85),oklch(0.955 0.02 80));
  padding: 44px 36px;
  color: var(--ink);
}

.cle-10__prose {
  max-width: 46ch;
  font-size: 22px;
  line-height: 2;
  text-wrap: pretty;
}

.cle-10__legend {
  display: flex;
  gap: 36px;
}

.cle-10__cap {
  font-size: 10.5px;
  font-weight: 600;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: oklch(0.55 0.04 60);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.cle-10 a {
  position: relative;
  color: var(--ink);
  text-decoration: none;
  font-style: italic;
  font-weight: 600;
  white-space: nowrap;
}

.cle-10 a:focus-visible {
  outline: 2px solid var(--pen);
  outline-offset: 4px;
  border-radius: 3px;
}

.cle-10 svg {
  position: absolute;
  inset: -.4em -.65em;
  width: calc(100% + 1.3em);
  height: calc(100% + .8em);
  overflow: visible;
  pointer-events: none;
}

.cle-10 svg path,
.cle-10 svg ellipse {
  fill: none;
  stroke: var(--pen);
  stroke-width: 2.2;
  stroke-linecap: round;
  vector-effect: non-scaling-stroke;
}

.cle-10__loop path {
  stroke-dasharray: 1 1.5;
  stroke-dashoffset: 1.2;
  transition: stroke-dashoffset .45s ease-in;
}

.cle-10__loop:hover path,
.cle-10__loop:focus-visible path {
  stroke-dashoffset: 0;
  transition: stroke-dashoffset .55s cubic-bezier(.4,0,.3,1);
}

.cle-10__scribble path {
  stroke-dasharray: 1 1.5;
  stroke-dashoffset: 1.2;
  transition: stroke-dashoffset .6s ease-in;
}

.cle-10__scribble:hover path,
.cle-10__scribble:focus-visible path {
  stroke-dashoffset: 0;
  transition: stroke-dashoffset .9s cubic-bezier(.4,0,.3,1);
}

.cle-10__stamp ellipse {
  fill: oklch(0.75 0.15 55 / .3);
  stroke: none;
  transform-box: fill-box;
  transform-origin: center;
  scale: .8;
  opacity: 0;
  transition: scale .3s cubic-bezier(.3,1.5,.4,1),opacity .25s;
}

.cle-10__stamp:hover ellipse,
.cle-10__stamp:focus-visible ellipse {
  scale: 1;
  opacity: 1;
}

@media (prefers-reduced-motion: reduce) {
  .cle-10 * {
    transition-duration: .01s !important;
  }
}
```
