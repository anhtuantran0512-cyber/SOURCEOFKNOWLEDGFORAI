---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-hover-effects/elastic-rubber-band-bounce/"
title: "Elastic / Rubber Band Bounce"
section: "motion"
category: "css-text-hover-effects"
category_name: "CSS Text Hover Effects"
description: "Letters made of gum: hovering the wordmark fires a squash-and-stretch keyframe through every letter with a 40ms stagger — scaleX fattens while scaleY…"
has_js: "false"
---

Here's a working CSS Text Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Elastic / Rubber Band Bounce
Source: https://codefronts.com/motion/css-text-hover-effects/elastic-rubber-band-bounce/

Letters made of gum: hovering the wordmark fires a squash-and-stretch keyframe through every letter with a 40ms stagger — scaleX fattens while scaleY squashes, whips past center the other way, and rings down to rest, the same overshoot curve animators have used since Disney's nine old men. Each letter also carries its own candy color that saturates as it wobbles. The big CTA is the container version: one squishy button that stretches wide on hover and SQUASHES flat on press, because :active without squash is a lie on a page like this.
## HTML
```html
<section class="cth-19" aria-label="Elastic rubber band text demo">
  <div class="cth-19__stage">
    <div class="cth-19__scene">
      <p class="cth-19__eyebrow">After-school coding camp &middot; ages 7&ndash;11</p>
      <a class="cth-19__word" href="#cth19-top" id="cth19-top" aria-label="WIGGLE CLUB">
        <span aria-hidden="true"><i style="--i:0;--c:oklch(0.65 0.21 25)">W</i><i style="--i:1;--c:oklch(0.7 0.18 65)">I</i><i style="--i:2;--c:oklch(0.72 0.19 140)">G</i><i style="--i:3;--c:oklch(0.65 0.16 220)">G</i><i style="--i:4;--c:oklch(0.6 0.2 290)">L</i><i style="--i:5;--c:oklch(0.66 0.22 340)">E</i></span>
        <span class="cth-19__second" aria-hidden="true"><i style="--i:6;--c:oklch(0.7 0.18 65)">C</i><i style="--i:7;--c:oklch(0.72 0.19 140)">L</i><i style="--i:8;--c:oklch(0.65 0.16 220)">U</i><i style="--i:9;--c:oklch(0.6 0.2 290)">B</i></span>
      </a>
      <p class="cth-19__sub">Blocks in term one, robots by term three. Snacks throughout.</p>
      <a class="cth-19__btn" href="#cth19-top">Save a spot<span aria-hidden="true"> &rarr;</span></a>
      <p class="cth-19__hint">Hover the name (squash &amp; stretch, staggered 40ms) &mdash; then press the button and feel it squash. Origin sits at the baseline so letters bounce off the floor.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.cth-19,
.cth-19 *,
.cth-19 *::before,
.cth-19 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cth-19 {
  --bg: oklch(0.965 0.02 95);
  --ink: oklch(0.28 0.05 280);
  --mut: oklch(0.5 0.04 285);
  --acc: oklch(0.65 0.21 25);
  font-family: ui-rounded,'SF Pro Rounded','Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.cth-19__stage {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  background: radial-gradient(85% 70% at 50% 18%,oklch(0.985 0.012 95),var(--bg) 70%);
  padding: clamp(20px,4vw,56px);
  container: cth19/inline-size;
}

.cth-19__scene {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: clamp(14px,2.8cqi,24px);
}

.cth-19__eyebrow {
  font-size: 13px;
  font-weight: 800;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--mut);
}

.cth-19__word {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: .05em .35em;
  text-decoration: none;
  font-size: clamp(54px,12.5cqi,128px);
  font-weight: 900;
  letter-spacing: -.02em;
  line-height: 1;
  padding: .15em .1em;
}

.cth-19__word:focus-visible {
  outline: 3px solid var(--acc);
  outline-offset: 8px;
  border-radius: 12px;
}

.cth-19__word i {
  display: inline-block;
  font-style: normal;
  color: var(--ink);
  transform-origin: 50% 78%;
  transition: color .3s ease;
}

.cth-19__word:hover i,
.cth-19__word:focus-visible i {
  color: var(--c);
  animation: cth19-rubber .8s cubic-bezier(.3,.6,.4,1) both;
  animation-delay: calc(var(--i)*40ms);
}

@keyframes cth19-rubber {
  0% {
    transform: scale(1,1);
  }

  30% {
    transform: scale(1.28,.72);
  }

  42% {
    transform: scale(.78,1.24);
  }

  56% {
    transform: scale(1.14,.88);
  }

  70% {
    transform: scale(.94,1.06);
  }

  84% {
    transform: scale(1.03,.98);
  }

  100% {
    transform: scale(1,1);
  }
}

.cth-19__sub {
  font-size: 15.5px;
  font-weight: 600;
  color: var(--mut);
  max-width: 40ch;
  line-height: 1.6;
}

.cth-19__btn {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  min-height: 58px;
  padding: 0 34px;
  margin-top: 6px;
  border-radius: 99px;
  background: var(--acc);
  color: oklch(0.99 0.005 95);
  font-size: 17px;
  font-weight: 900;
  letter-spacing: .01em;
  text-decoration: none;
  box-shadow: 0 6px 0 0 color-mix(in oklch,var(--acc) 55%,oklch(0.2 0.05 25));
  scale: 1 1;
  transition: scale .45s cubic-bezier(.28,2.2,.4,1),box-shadow .2s ease,translate .2s ease;
}

.cth-19__btn:hover,
.cth-19__btn:focus-visible {
  scale: 1.08 .92;
}

.cth-19__btn:active {
  scale: .94 1.04;
  translate: 0 4px;
  box-shadow: 0 2px 0 0 color-mix(in oklch,var(--acc) 55%,oklch(0.2 0.05 25));
  transition-duration: .08s;
}

.cth-19__btn:focus-visible {
  outline: 3px solid var(--ink);
  outline-offset: 4px;
}

.cth-19__hint {
  font-size: 12.5px;
  line-height: 1.7;
  color: var(--mut);
  max-width: 56ch;
  font-family: 'Segoe UI',system-ui,sans-serif;
}

@media (prefers-reduced-motion: reduce) {
  .cth-19 i {
    animation: none !important;
  }

  .cth-19__btn {
    transition: none;
  }
}
```
