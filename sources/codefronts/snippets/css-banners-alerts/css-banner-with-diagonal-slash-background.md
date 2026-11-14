---
source: "codefronts"
url: "https://codefronts.com/snippets/css-banners-alerts/css-banner-with-diagonal-slash-background/"
title: "Diagonal Stripe Promo Banner"
section: "snippets"
category: "css-banners-alerts"
category_name: "CSS Banners & Alerts"
description: "Diagonal geometry done three ways in one banner: a hazard-stripe field from repeating-linear-gradient that scrolls on a registered angle, a hard slash split…"
has_js: "false"
---

Here's a working CSS Banners & Alert from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Diagonal Stripe Promo Banner
Source: https://codefronts.com/snippets/css-banners-alerts/css-banner-with-diagonal-slash-background/

Diagonal geometry done three ways in one banner: a hazard-stripe field from repeating-linear-gradient that scrolls on a registered angle, a hard slash split cut with clip-path, and a rotating conic badge — all pure CSS, all GPU-cheap, and all pausing under prefers-reduced-motion. The promo code reveals with a checkbox, no script.
## HTML
```html
<div class="ba-17">
  <section class="ba-17__banner" aria-labelledby="ba-17-h">
    <div class="ba-17__left" aria-hidden="true">
      <span class="ba-17__stripes"></span>
      <span class="ba-17__badge">
        <span class="ba-17__badgeRing"></span>
        <b>40</b><i>% off</i>
      </span>
    </div>

    <div class="ba-17__right">
      <p class="ba-17__eyebrow">Workshop season · ends Sunday</p>
      <h2 class="ba-17__h" id="ba-17-h">Two days of CSS that ships</h2>
      <p class="ba-17__sub">Container queries, scroll-driven motion and anchor positioning, rebuilt live from your own components. Recordings included, no slides.</p>

      <div class="ba-17__cta">
        <a class="ba-17__book" href="#ba-17-h">Book a seat<svg viewBox="0 0 20 20" fill="none" aria-hidden="true" focusable="false"><path d="M4 10h11m-4.4-4.4L15 10l-4.4 4.4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
        <span class="ba-17__codeWrap">
          <input class="ba-17__vh" type="checkbox" id="ba-17-reveal">
          <label class="ba-17__reveal" for="ba-17-reveal" tabindex="0" role="button">Reveal promo code</label>
          <span class="ba-17__code"><em>Code</em> STRIPES40</span>
        </span>
      </div>

      <ul class="ba-17__facts">
        <li><b>2</b> days, live</li>
        <li><b>14</b> seats left</li>
        <li><b>4.9</b> average rating</li>
      </ul>
    </div>
  </section>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Archivo:wdth,[email protected],400;75..125,600;75..125,800&family=DM+Sans:opsz,[email protected],400;9..40,500&display=swap');

@property --ba-17-a {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

.ba-17 {
  --stripe: 1.1rem;
  --ang: 115deg;
  --bg: #101014;
  --ink: #0c0c0f;
  --paper: #f7f5f0;
  --muted: #5d5a54;
  --acc: #ffd400;
  --acc2: #ff4d00;
  --s1: #0c0c0f;
  --display: "Archivo",ui-sans-serif,system-ui,sans-serif;
  --sans: "DM Sans",ui-sans-serif,system-ui,-apple-system,sans-serif;
  container-type: inline-size;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  box-sizing: border-box;
  padding: clamp(1rem,4vw,3rem);
  background: var(--bg);
  color: var(--paper);
  font-family: var(--sans);
}

.ba-17 *,
.ba-17 *::before,
.ba-17 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(50% 0 0)) {
  .ba-17 {
    --bg: oklch(17% .01 280);
    --paper: oklch(97% .012 90);
    --ink: oklch(14% .012 280);
    --muted: oklch(55% .014 80);
    --acc: oklch(89% .18 98);
    --acc2: oklch(66% .23 40);
  }
}

@media (prefers-color-scheme: light) {
  .ba-17:not([data-theme="dark"]) {
    --bg: #eceae4;
  }
}

.ba-17__banner {
  position: relative;
  width: min(64rem,100%);
  overflow: hidden;
  display: grid;
  grid-template-columns: minmax(0,.85fr) minmax(0,1.15fr);
  border-radius: 1.75rem;
  background: var(--paper);
  color: var(--ink);
  box-shadow: 0 3rem 6rem -2.5rem rgb(0 0 0 / .6);
  isolation: isolate;
}

.ba-17__left {
  position: relative;
  min-height: clamp(14rem,34vh,20rem);
  background: var(--acc);
  overflow: hidden;
}

.ba-17__stripes {
  position: absolute;
  inset: -20%;
  background-image: repeating-linear-gradient(var(--ang), var(--s1) 0 var(--stripe), transparent var(--stripe) calc(var(--stripe) * 2));
  background-size: 200% 200%;
  opacity: .9;
  mix-blend-mode: multiply;
  animation: ba-17-slide 14s linear infinite;
}

@keyframes ba-17-slide {
  to {
    background-position: 40rem 0;
  }
}

.ba-17__badge {
  position: absolute;
  inset-block-start: 50%;
  inset-inline-start: 50%;
  translate: -50% -50%;
  display: grid;
  place-items: center;
  width: clamp(7rem,16cqw,9.5rem);
  aspect-ratio: 1;
  border-radius: 999px;
  background: var(--paper);
  color: var(--ink);
  text-align: center;
  box-shadow: 0 1.5rem 3rem -1rem rgb(0 0 0 / .35);
}

.ba-17__badgeRing {
  position: absolute;
  inset: -.5rem;
  border-radius: 999px;
  padding: .35rem;
  background: conic-gradient(from var(--ba-17-a), var(--acc2), var(--ink) 32%, var(--acc2) 62%, var(--ink));
  mask: radial-gradient(circle, transparent 62%, black 64%);
  animation: ba-17-spin 9s linear infinite;
}

@keyframes ba-17-spin {
  to {
    --ba-17-a: 360deg;
  }
}

.ba-17__badge b {
  grid-area: 1/1;
  font-family: var(--display);
  font-size: clamp(2rem,6cqw,3rem);
  font-weight: 800;
  font-stretch: 112%;
  letter-spacing: -.05em;
  line-height: 1;
  translate: 0 -.35rem;
  font-variant-numeric: tabular-nums;
}

.ba-17__badge i {
  grid-area: 1/1;
  align-self: end;
  font-style: normal;
  font-family: var(--display);
  font-size: .6875rem;
  font-weight: 600;
  letter-spacing: .2em;
  text-transform: uppercase;
  translate: 0 -1.6rem;
}

.ba-17__right {
  position: relative;
  padding: clamp(1.5rem,4cqw,2.75rem) clamp(1.5rem,4cqw,3rem);
  display: grid;
  gap: .85rem;
  align-content: center;
  background: var(--paper);
  clip-path: polygon(11% 0, 100% 0, 100% 100%, 0% 100%);
  padding-inline-start: clamp(2.25rem,10cqw,5rem);
  margin-inline-start: -7%;
}

.ba-17__eyebrow {
  margin: 0;
  font-family: var(--display);
  font-size: .6875rem;
  font-weight: 600;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--acc2);
}

.ba-17__h {
  margin: 0;
  font-family: var(--display);
  font-size: clamp(1.875rem,6.5cqw,3.5rem);
  font-weight: 800;
  font-stretch: 112%;
  line-height: .95;
  letter-spacing: -.05em;
  text-wrap: balance;
  color: var(--ink);
}

.ba-17__sub {
  margin: 0;
  font-size: clamp(.875rem,1.7cqw,1rem);
  line-height: 1.6;
  color: var(--muted);
  max-width: 52ch;
  text-wrap: pretty;
}

.ba-17__cta {
  display: flex;
  flex-wrap: wrap;
  gap: .6rem;
  align-items: center;
  margin-block-start: .25rem;
}

.ba-17__book {
  display: inline-flex;
  align-items: center;
  gap: .45rem;
  min-height: 3rem;
  padding: .85rem 1.4rem;
  border-radius: .85rem;
  text-decoration: none;
  background: var(--ink);
  color: var(--paper);
  font-family: var(--display);
  font-size: .9375rem;
  font-weight: 600;
  letter-spacing: -.01em;
  transition: translate .2s cubic-bezier(.16,1,.3,1), box-shadow .25s ease, background .2s ease;
}

.ba-17__book svg {
  width: 1.05rem;
  height: 1.05rem;
  transition: translate .25s cubic-bezier(.16,1,.3,1);
}

.ba-17__book:hover {
  translate: 0 -2px;
  background: var(--acc2);
  box-shadow: 0 1rem 2rem -1rem color-mix(in oklab,var(--acc2) 70%,transparent);
}

.ba-17__book:hover svg {
  translate: .25rem 0;
}

.ba-17__codeWrap {
  position: relative;
  display: inline-grid;
}

.ba-17__reveal {
  display: inline-flex;
  align-items: center;
  min-height: 3rem;
  padding: .85rem 1.1rem;
  cursor: pointer;
  border: 1.5px dashed color-mix(in oklab,var(--ink) 35%,transparent);
  border-radius: .85rem;
  font-size: .875rem;
  font-weight: 600;
  color: var(--muted);
  transition: border-color .2s ease, color .2s ease, opacity .25s ease, display .25s allow-discrete;
}

.ba-17__reveal:hover {
  color: var(--ink);
  border-color: var(--ink);
}

.ba-17__reveal:focus-visible {
  outline: 2px solid var(--acc2);
  outline-offset: 2px;
}

.ba-17__code {
  display: none;
  align-items: center;
  gap: .5rem;
  min-height: 3rem;
  padding: .85rem 1.1rem;
  border-radius: .85rem;
  background: var(--acc);
  color: var(--ink);
  font-family: var(--display);
  font-size: .9375rem;
  font-weight: 800;
  letter-spacing: .06em;
  transition: opacity .25s ease, translate .25s ease, display .25s allow-discrete;
}

@starting-style {
  .ba-17__code {
    opacity: 0;
    translate: 0 .4rem;
  }
}

.ba-17__code em {
  font-style: normal;
  font-size: .5625rem;
  font-weight: 600;
  letter-spacing: .18em;
  text-transform: uppercase;
  opacity: .6;
}

.ba-17__codeWrap:has(#ba-17-reveal:checked) .ba-17__reveal {
  display: none;
  opacity: 0;
}

.ba-17__codeWrap:has(#ba-17-reveal:checked) .ba-17__code {
  display: flex;
}

.ba-17__facts {
  margin: .35rem 0 0;
  padding: .85rem 0 0;
  list-style: none;
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
  border-block-start: 1px solid color-mix(in oklab,var(--ink) 14%,transparent);
  font-size: .75rem;
  color: var(--muted);
}

.ba-17__facts b {
  display: block;
  font-family: var(--display);
  font-size: 1.25rem;
  font-weight: 800;
  color: var(--ink);
  letter-spacing: -.03em;
  font-variant-numeric: tabular-nums;
}

.ba-17__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.ba-17 a {
  color: var(--acc2);
}

.ba-17 :focus-visible {
  outline: 2px solid var(--acc2);
  outline-offset: 2px;
}

@container (max-width: 46rem) {
  .ba-17__banner {
    grid-template-columns: 1fr;
  }

  .ba-17__left {
    min-height: 9rem;
  }

  .ba-17__right {
    clip-path: polygon(0 8%, 100% 0, 100% 100%, 0 100%);
    margin-inline-start: 0;
    margin-block-start: -3%;
    padding-inline-start: clamp(1.5rem,4cqw,3rem);
    padding-block-start: clamp(2rem,7cqw,3.25rem);
  }
}

@media (prefers-reduced-motion: reduce) {
  .ba-17 * {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .ba-17__banner {
    border: 1px solid CanvasText;
  }

  .ba-17__book {
    background: Highlight;
    color: HighlightText;
  }

  .ba-17__stripes {
    display: none;
  }
}
```
