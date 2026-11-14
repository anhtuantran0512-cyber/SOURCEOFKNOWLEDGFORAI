---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-hover-effects/smoke-dissolve-particle-effect/"
title: "Smoke / Dissolve Particle Effect"
section: "motion"
category: "css-text-hover-effects"
category_name: "CSS Text Hover Effects"
description: "Hold the cursor on the title and it exhales: each letter blurs, lightens, drifts up along its own slightly different heading, and thins to nothing — smoke…"
has_js: "false"
---

Here's a working CSS Text Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Smoke / Dissolve Particle Effect
Source: https://codefronts.com/motion/css-text-hover-effects/smoke-dissolve-particle-effect/

Hold the cursor on the title and it exhales: each letter blurs, lightens, drifts up along its own slightly different heading, and thins to nothing — smoke leaving a cooling fire. Pull away mid-dissolve and it re-condenses through the exact same path, because everything is transitions (never keyframes): per-letter drift vectors and rotations live in inline custom properties, delays stagger 35ms per letter, and filter:blur() is the actual smoke. The full word stays in the accessibility tree via aria-label while the letter spans do the vanishing.
## HTML
```html
<section class="cth-23" aria-label="Smoke dissolve text demo">
  <div class="cth-23__stage">
    <div class="cth-23__scene">
      <p class="cth-23__eyebrow">A film by Ines Marlowe</p>
      <h1 class="cth-23__title" tabindex="0" aria-label="AFTERGLOW">
        <span aria-hidden="true"><i style="--i:0;--dx:-.1em;--dr:-8deg">A</i><i style="--i:1;--dx:.06em;--dr:5deg">F</i><i style="--i:2;--dx:-.04em;--dr:-4deg">T</i><i style="--i:3;--dx:.14em;--dr:9deg">E</i><i style="--i:4;--dx:-.12em;--dr:-6deg">R</i><i style="--i:5;--dx:.05em;--dr:7deg">G</i><i style="--i:6;--dx:-.07em;--dr:-9deg">L</i><i style="--i:7;--dx:.11em;--dr:4deg">O</i><i style="--i:8;--dx:-.05em;--dr:-5deg">W</i></span>
      </h1>
      <p class="cth-23__sub">In cinemas October &mdash; the story of everything we let cool.</p>
      <p class="cth-23__hint">Rest the cursor on the title and hold; pull away mid-dissolve and it re-condenses along the same path. Transitions, never keyframes &mdash; that's the whole trick.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.cth-23,
.cth-23 *,
.cth-23 *::before,
.cth-23 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cth-23 {
  --bg: oklch(0.15 0.008 270);
  --ink: oklch(0.9 0.01 80);
  --mut: oklch(0.56 0.015 275);
  font-family: Georgia,'Times New Roman',serif;
  color: var(--ink);
}

.cth-23__stage {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  background: radial-gradient(100% 90% at 50% 100%,oklch(0.2 0.02 50/.55),transparent 55%),radial-gradient(90% 70% at 50% 20%,oklch(0.18 0.01 275),var(--bg) 75%);
  padding: clamp(20px,4vw,56px);
  container: cth23/inline-size;
}

.cth-23__scene {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: clamp(16px,3cqi,26px);
}

.cth-23__eyebrow {
  font-size: 12px;
  letter-spacing: .34em;
  text-transform: uppercase;
  color: var(--mut);
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-weight: 600;
}

.cth-23__title {
  padding: clamp(24px,5cqi,48px) clamp(16px,3cqi,32px);
  letter-spacing: .16em;
  border-radius: 14px;
}

.cth-23__title:focus-visible {
  outline: 1.5px solid var(--ink);
  outline-offset: 4px;
}

.cth-23__title i {
  display: inline-block;
  font-style: normal;
  font-size: clamp(44px,10cqi,104px);
  font-weight: 500;
  line-height: 1;
  translate: 0 0;
  rotate: 0deg;
  opacity: 1;
  filter: blur(0);
  transition: translate 1s cubic-bezier(.3,.6,.2,1),rotate 1s ease,opacity 1s ease,filter 1s ease,color 1s ease;
  transition-delay: calc(var(--i)*35ms);
}

.cth-23__title:hover i,
.cth-23__title:focus-visible i {
  translate: var(--dx) -1.25em;
  rotate: var(--dr);
  opacity: 0;
  filter: blur(.14em);
  color: oklch(0.98 0.005 80);
}

.cth-23__sub {
  font-size: 14.5px;
  font-style: italic;
  color: var(--mut);
  letter-spacing: .02em;
}

.cth-23__hint {
  font-size: 12.5px;
  line-height: 1.7;
  color: var(--mut);
  max-width: 56ch;
  font-family: 'Segoe UI',system-ui,sans-serif;
}

@media (prefers-reduced-motion: reduce) {
  .cth-23__title i {
    transition: opacity .4s ease !important;
    transition-delay: 0s !important;
  }

  .cth-23__title:hover i,
    .cth-23__title:focus-visible i {
    translate: 0 0;
    rotate: 0deg;
    filter: blur(0);
    opacity: .45;
  }
}
```
