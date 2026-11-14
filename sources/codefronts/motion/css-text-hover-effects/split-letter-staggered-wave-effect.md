---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-hover-effects/split-letter-staggered-wave-effect/"
title: "Split Letter / Staggered Wave Effect"
section: "motion"
category: "css-text-hover-effects"
category_name: "CSS Text Hover Effects"
description: "Hover the wordmark and the letters take off one by one — a wave built from transition-delay:calc(var(--i)*45ms), which is the professional choice over…"
has_js: "false"
---

Here's a working CSS Text Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Split Letter / Staggered Wave Effect
Source: https://codefronts.com/motion/css-text-hover-effects/split-letter-staggered-wave-effect/

Hover the wordmark and the letters take off one by one — a wave built from transition-delay:calc(var(--i)*45ms), which is the professional choice over keyframes for one huge reason: transitions are REVERSIBLE, so when the cursor leaves mid-wave the letters settle back in the same stagger instead of snapping to frame zero. Letters are pre-split in the HTML with an index custom property each (no JS splitter), aria-hidden as a group, with the real word on the parent for screen readers and find-in-page.
## HTML
```html
<section class="cth-10" aria-label="Staggered letter wave demo">
  <div class="cth-10__stage">
    <div class="cth-10__scene">
      <p class="cth-10__eyebrow">Cold-pressed &middot; Bondi since 2019</p>
      <a class="cth-10__wave" href="#cth10-top" id="cth10-top" aria-label="SUNDAZE">
        <span aria-hidden="true"><i style="--i:0">S</i><i style="--i:1">U</i><i style="--i:2">N</i><i style="--i:3">D</i><i style="--i:4">A</i><i style="--i:5">Z</i><i style="--i:6">E</i></span>
      </a>
      <nav class="cth-10__nav" aria-label="Flavours">
        <a class="cth-10__link" href="#cth10-top" aria-label="Mango"><span aria-hidden="true"><i style="--i:0">M</i><i style="--i:1">a</i><i style="--i:2">n</i><i style="--i:3">g</i><i style="--i:4">o</i></span></a>
        <a class="cth-10__link" href="#cth10-top" aria-label="Guava"><span aria-hidden="true"><i style="--i:0">G</i><i style="--i:1">u</i><i style="--i:2">a</i><i style="--i:3">v</i><i style="--i:4">a</i></span></a>
        <a class="cth-10__link" href="#cth10-top" aria-label="Yuzu"><span aria-hidden="true"><i style="--i:0">Y</i><i style="--i:1">u</i><i style="--i:2">z</i><i style="--i:3">u</i></span></a>
      </nav>
      <p class="cth-10__hint">Hover, leave mid-wave, hover again &mdash; transitions reverse through the same stagger, which keyframes can't do. Real word lives in <code>aria-label</code>.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.cth-10,
.cth-10 *,
.cth-10 *::before,
.cth-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cth-10 {
  --bg: oklch(0.93 0.06 85);
  --ink: oklch(0.32 0.08 50);
  --acc: oklch(0.62 0.19 35);
  --sea: oklch(0.6 0.13 220);
  --mut: oklch(0.48 0.06 55);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.cth-10__stage {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  background: linear-gradient(180deg,oklch(0.95 0.05 90),var(--bg) 55%,oklch(0.9 0.07 70));
  padding: clamp(20px,4vw,56px);
  container: cth10/inline-size;
}

.cth-10__scene {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: clamp(16px,3cqi,26px);
}

.cth-10__eyebrow {
  font-size: 12.5px;
  font-weight: 800;
  letter-spacing: .26em;
  text-transform: uppercase;
  color: var(--mut);
}

.cth-10__wave {
  display: inline-block;
  text-decoration: none;
  color: var(--ink);
  font-size: clamp(56px,13.5cqi,140px);
  font-weight: 900;
  letter-spacing: -.03em;
  line-height: 1;
  padding: .18em .1em .1em;
}

.cth-10__wave:focus-visible {
  outline: 3px solid var(--acc);
  outline-offset: 8px;
  border-radius: 10px;
}

.cth-10__wave i,
.cth-10__link i {
  display: inline-block;
  font-style: normal;
  translate: 0 0;
  rotate: 0deg;
  transition: translate .5s cubic-bezier(.34,1.9,.5,1),rotate .5s cubic-bezier(.34,1.9,.5,1),color .35s ease;
  transition-delay: calc(var(--i)*45ms),calc(var(--i)*45ms),calc(var(--i)*45ms);
}

.cth-10__wave:hover i,
.cth-10__wave:focus-visible i {
  translate: 0 -.22em;
  color: var(--acc);
}

.cth-10__wave:hover i:nth-child(even),
.cth-10__wave:focus-visible i:nth-child(even) {
  rotate: 6deg;
  color: var(--sea);
}

.cth-10__nav {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: clamp(10px,2.4cqi,22px);
}

.cth-10__link {
  display: grid;
  place-items: center;
  min-height: 48px;
  padding: 0 22px;
  border: 2.5px solid var(--ink);
  border-radius: 99px;
  background: oklch(0.97 0.02 90);
  text-decoration: none;
  color: var(--ink);
  font-size: 17px;
  font-weight: 800;
  transition: background .3s ease,border-color .3s ease;
}

.cth-10__link:hover,
.cth-10__link:focus-visible {
  background: oklch(1 0 0);
  border-color: var(--acc);
}

.cth-10__link:focus-visible {
  outline: 3px solid var(--acc);
  outline-offset: 3px;
}

.cth-10__link i {
  transition-duration: .4s;
}

.cth-10__link:hover i,
.cth-10__link:focus-visible i {
  translate: 0 -.14em;
  color: var(--acc);
}

.cth-10__hint {
  font-size: 12.5px;
  line-height: 1.7;
  color: var(--mut);
  max-width: 54ch;
}

.cth-10__hint code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .9em;
  background: oklch(0.88 0.05 85);
  padding: 1px 6px;
  border-radius: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .cth-10 i {
    transition: color .3s ease !important;
    transition-delay: 0s !important;
  }
}
```
