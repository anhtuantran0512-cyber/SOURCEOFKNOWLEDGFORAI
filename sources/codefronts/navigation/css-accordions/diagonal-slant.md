---
source: "codefronts"
url: "https://codefronts.com/navigation/css-accordions/diagonal-slant/"
title: "Diagonal Slant Accordion — Skewed Parallelogram Headers"
section: "navigation"
category: "css-accordions"
category_name: "CSS Accordions — Vertical & Horizontal"
description: "Headers as racing stripes: every summary is a parallelogram skewed −6°, stacked with alternating offsets so the closed accordion reads as a dynamic diagonal…"
has_js: "false"
---

Here's a working CSS Accordions — Vertical & Horizontal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Diagonal Slant Accordion — Skewed Parallelogram Headers
Source: https://codefronts.com/navigation/css-accordions/diagonal-slant/

Headers as racing stripes: every summary is a parallelogram skewed −6°, stacked with alternating offsets so the closed accordion reads as a dynamic diagonal composition. Opening un-skews the active stripe back to square while its body slides out beneath — geometry itself is the state indicator. Built for sports, esports and event brands.
## HTML
```html
<section class="acc-23" aria-label="Diagonal slant accordion demo">
  <div class="acc-23__wrap">
    <h3 class="acc-23__title">Match day guide</h3>
    <details class="acc-23__item" style="--c:oklch(0.62 0.22 25)" open>
      <summary class="acc-23__sum"><span class="acc-23__box"><span class="acc-23__text">Tickets &amp; entry<i>»</i></span></span></summary>
      <div class="acc-23__body"><p>Gates open 90 minutes before kickoff. Digital tickets only — add yours to your wallet before you reach the ground; signal drops in the crowd.</p></div>
    </details>
    <details class="acc-23__item" style="--c:oklch(0.75 0.16 85)">
      <summary class="acc-23__sum"><span class="acc-23__box"><span class="acc-23__text">Getting there<i>»</i></span></span></summary>
      <div class="acc-23__body"><p>The stadium loop bus runs every 6 minutes from Central. Cycling? Two thousand racks at the north gate, free and staffed.</p></div>
    </details>
    <details class="acc-23__item" style="--c:oklch(0.6 0.15 250)">
      <summary class="acc-23__sum"><span class="acc-23__box"><span class="acc-23__text">Food &amp; drink<i>»</i></span></span></summary>
      <div class="acc-23__body"><p>Twelve local vendors on the concourse. Refillable cups save you a dollar a pour — taps at every block entrance.</p></div>
    </details>
    <details class="acc-23__item" style="--c:oklch(0.55 0.18 145)">
      <summary class="acc-23__sum"><span class="acc-23__box"><span class="acc-23__text">Accessibility<i>»</i></span></span></summary>
      <div class="acc-23__body"><p>Step-free routes from every gate, sensory kits at guest services, and audio-descriptive commentary on channel 3 of the stadium app.</p></div>
    </details>
  </div>
</section>
```
## CSS
```css
.acc-23,
.acc-23 *,
.acc-23 *::before,
.acc-23 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.acc-23 {
  --ink: #15161c;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #eceef2;
  padding: 44px 32px;
}

.acc-23__wrap {
  width: min(560px,100%);
  padding: 0 24px;
}

.acc-23__title {
  font-size: 26px;
  font-weight: 850;
  color: var(--ink);
  letter-spacing: -.02em;
  text-transform: uppercase;
  font-style: italic;
  margin-bottom: 20px;
}

.acc-23__item {
  margin-bottom: 14px;
}

.acc-23__item:nth-child(odd of .acc-23__item) .acc-23__box {
  translate: 10px 0;
}

.acc-23__item:nth-child(even of .acc-23__item) .acc-23__box {
  translate: -10px 0;
}

.acc-23__sum {
  list-style: none;
  cursor: pointer;
  display: block;
}

.acc-23__sum::-webkit-details-marker {
  display: none;
}

.acc-23__sum::marker {
  content: "";
}

.acc-23__box {
  display: block;
  background: var(--c);
  box-shadow: 5px 5px 0 color-mix(in oklab,var(--c) 45%,#000);
  transform: skewX(-6deg);
  transition: transform .35s cubic-bezier(.3,1.2,.4,1),translate .35s cubic-bezier(.3,1.2,.4,1),box-shadow .35s;
}

.acc-23__item[open] .acc-23__box {
  transform: skewX(0);
  translate: 0 0;
  box-shadow: 0 5px 0 color-mix(in oklab,var(--c) 45%,#000);
}

.acc-23__sum:hover .acc-23__box {
  filter: brightness(1.05);
}

.acc-23__text {
  display: flex;
  align-items: center;
  gap: 12px;
  min-height: 56px;
  padding: 8px 22px;
  font-size: 16px;
  font-weight: 800;
  letter-spacing: .04em;
  text-transform: uppercase;
  color: #fff;
  transform: skewX(6deg);
  transition: transform .35s cubic-bezier(.3,1.2,.4,1);
}

.acc-23__item[open] .acc-23__text {
  transform: skewX(0);
}

.acc-23__text i {
  font-style: normal;
  margin-left: auto;
  transition: rotate .3s;
}

.acc-23__item[open] .acc-23__text i {
  rotate: 90deg;
}

.acc-23__body {
  padding: 16px 24px 6px;
  font-size: 14.5px;
  line-height: 1.65;
  color: #3c4152;
}

.acc-23__item[open] .acc-23__body {
  animation: acc-23-in .35s ease-out;
}

@keyframes acc-23-in {
  from {
    opacity: 0;
    translate: 0 -6px;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

.acc-23__sum:focus-visible {
  outline: 3px solid var(--ink);
  outline-offset: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .acc-23__box,
    .acc-23__text,
    .acc-23__text i {
    transition: none;
  }

  .acc-23__item[open] .acc-23__body {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — headers are skewX(-6deg) boxes with +6deg counter-skewed text; details[open] transitions both to 0 so the stripe squares up as its body opens. */
```
