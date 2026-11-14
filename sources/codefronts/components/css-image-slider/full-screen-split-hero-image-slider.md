---
source: "codefronts"
url: "https://codefronts.com/components/css-image-slider/full-screen-split-hero-image-slider/"
title: "Full-Screen Split Hero Image Slider"
section: "components"
category: "css-image-slider"
category_name: "CSS Image Sliders"
description: "Full-screen split hero image slider — an agency-grade full-bleed photo half paired with a typographic half that swap content in sync as you switch destinations."
has_js: "true"
---

Here's a working CSS Image Slider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Full-Screen Split Hero Image Slider
Source: https://codefronts.com/components/css-image-slider/full-screen-split-hero-image-slider/

Full-screen split hero image slider — an agency-grade full-bleed photo half paired with a typographic half that swap content in sync as you switch destinations. Copy-paste ready for real-estate listing heroes (Zillow / Redfin / Airbnb / Vrbo pattern), travel-resort landing pages, and portfolio splash screens. Built on :has() plus an animated @property gradient sweep, with a natural upgrade path to the View Transitions API for cross-fade page swaps. No JavaScript.
## HTML
```html
<div class="cis-06">
  <input type="radio" name="cis-06" id="cis-06-1" checked>
  <input type="radio" name="cis-06" id="cis-06-2">
  <input type="radio" name="cis-06" id="cis-06-3">

  <div class="cis-06__scenes" aria-hidden="true">
    <div class="cis-06__scene s1"><img src="https://picsum.photos/seed/cis06a/1400/1600" alt=""></div>
    <div class="cis-06__scene s2"><img src="https://picsum.photos/seed/cis06b/1400/1600" alt=""></div>
    <div class="cis-06__scene s3"><img src="https://picsum.photos/seed/cis06c/1400/1600" alt=""></div>
  </div>

  <div class="cis-06__content">
    <div class="cis-06__panel p1">
      <span class="cis-06__kick">Nº 01 — Nordic</span>
      <h2 class="cis-06__title">Silence,<br>engineered.</h2>
      <p class="cis-06__lede">Cabins carved into the treeline. Nothing but weather and time.</p>
    </div>
    <div class="cis-06__panel p2">
      <span class="cis-06__kick">Nº 02 — Coastal</span>
      <h2 class="cis-06__title">Salt air,<br>slow days.</h2>
      <p class="cis-06__lede">A shoreline studio where the tide sets the schedule.</p>
    </div>
    <div class="cis-06__panel p3">
      <span class="cis-06__kick">Nº 03 — Highland</span>
      <h2 class="cis-06__title">Above<br>the cloud line.</h2>
      <p class="cis-06__lede">Thin air, wide light, and a horizon that keeps going.</p>
    </div>

    <div class="cis-06__tabs">
      <label class="cis-06__tab" for="cis-06-1"><span>01</span>Nordic</label>
      <label class="cis-06__tab" for="cis-06-2"><span>02</span>Coastal</label>
      <label class="cis-06__tab" for="cis-06-3"><span>03</span>Highland</label>
    </div>
  </div>
</div>
```
## CSS
```css
@property --angle {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

.cis-06,
.cis-06 *,
.cis-06 *::before,
.cis-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cis-06 ::selection {
  background: oklch(0.82 0.14 55);
  color: #160f04;
}

.cis-06 {
  --accent: oklch(0.82 0.14 55);
  --dur: .7s;
  position: relative;
  overflow: hidden;
  isolation: isolate;
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: #f6f2ea;
  min-height: 100vh;
  width: 100%;
  background: #0a0906;
}

.cis-06 input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}
/* full-viewport photo scenes, cross-faded */

.cis-06__scenes {
  position: absolute;
  inset: 0;
  z-index: 0;
}

.cis-06__scene {
  position: absolute;
  inset: 0;
  opacity: 0;
  transform: scale(1.08);
  transition: opacity var(--dur) ease,transform 1.4s ease;
}

.cis-06__scene img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  filter: brightness(.62) saturate(1.05);
}

.cis-06__scene::after {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(90deg,rgba(8,7,5,.9) 0%,rgba(8,7,5,.35) 46%,transparent 72%);
}

.cis-06:has(#cis-06-1:checked) .s1,
.cis-06:has(#cis-06-2:checked) .s2,
.cis-06:has(#cis-06-3:checked) .s3 {
  opacity: 1;
  transform: scale(1);
}
/* content column */

.cis-06__content {
  position: relative;
  z-index: 2;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 22px;
  padding: clamp(28px,7vw,110px);
  max-width: 640px;
}

.cis-06__panel {
  position: absolute;
  left: clamp(28px,7vw,110px);
  right: 24px;
  opacity: 0;
  transform: translateX(-34px);
  pointer-events: none;
  transition: opacity var(--dur) ease,transform var(--dur) cubic-bezier(.16,1,.3,1);
}

.cis-06:has(#cis-06-1:checked) .p1,
.cis-06:has(#cis-06-2:checked) .p2,
.cis-06:has(#cis-06-3:checked) .p3 {
  opacity: 1;
  transform: none;
  pointer-events: auto;
  position: relative;
}

.cis-06__kick {
  display: inline-block;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .3em;
  text-transform: uppercase;
  color: var(--accent);
}

.cis-06__title {
  font-size: clamp(40px,7vw,78px);
  line-height: .98;
  font-weight: 800;
  letter-spacing: -.02em;
  margin: 14px 0 16px;
  text-wrap: balance;
}

.cis-06__lede {
  font-size: clamp(15px,1.6vw,18px);
  line-height: 1.5;
  color: #cfc7b8;
  max-width: 34ch;
}
/* tabs with animated conic sweep on the active one */

.cis-06__tabs {
  position: relative;
  display: flex;
  gap: 12px;
  margin-top: 38px;
}

.cis-06__tab {
  position: relative;
  display: flex;
  align-items: center;
  gap: 9px;
  cursor: pointer;
  padding: 12px 18px;
  border-radius: 999px;
  font-size: 14px;
  font-weight: 600;
  color: #d8d0c2;
  background: rgba(255,255,255,.05);
  border: 1px solid rgba(255,255,255,.12);
  transition: color .3s,background .3s;
}

.cis-06__tab span {
  font-size: 11px;
  font-weight: 700;
  opacity: .6;
}

.cis-06__tab:hover {
  background: rgba(255,255,255,.1);
  color: #fff;
}

.cis-06:has(#cis-06-1:checked) .cis-06__tab:nth-of-type(1),
.cis-06:has(#cis-06-2:checked) .cis-06__tab:nth-of-type(2),
.cis-06:has(#cis-06-3:checked) .cis-06__tab:nth-of-type(3) {
  color: #160f04;
  border-color: transparent;
  background: var(--accent);
}

.cis-06:has(#cis-06-1:checked) .cis-06__tab:nth-of-type(1)::before,
.cis-06:has(#cis-06-2:checked) .cis-06__tab:nth-of-type(2)::before,
.cis-06:has(#cis-06-3:checked) .cis-06__tab:nth-of-type(3)::before {
  content: "";
  position: absolute;
  inset: -2px;
  border-radius: inherit;
  z-index: -1;
  background: conic-gradient(from var(--angle),transparent,var(--accent),transparent 40%);
  animation: cis-06-spin 3s linear infinite;
}

@keyframes cis-06-spin {
  to {
    --angle: 360deg;
  }
}

.cis-06 input:focus-visible + input + input ~ .cis-06__content .cis-06__tabs,
.cis-06 input:focus-visible ~ .cis-06__content .cis-06__tab {
  outline: none;
}

.cis-06:has(input:focus-visible) .cis-06__tabs {
  box-shadow: 0 0 0 3px color-mix(in oklab,var(--accent) 60%,transparent);
  border-radius: 999px;
}

@media (max-width: 720px) {
  .cis-06__scene::after {
    background: linear-gradient(0deg,rgba(8,7,5,.94) 8%,rgba(8,7,5,.4) 55%,transparent);
  }

  .cis-06__content {
    justify-content: flex-end;
    padding-bottom: 56px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cis-06__scene,
    .cis-06__panel {
    transition: opacity .2s;
  }

  .cis-06__scene {
    transform: none;
  }

  .cis-06 [class$="__tab"]::before {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript required — :has() drives the scene + text swap.
   Optional View Transitions upgrade (add if you want shared-element cross-fade):

   document.querySelectorAll('.cis-06 input').forEach(function(r){
     r.addEventListener('change', function(){
       if (!document.startViewTransition) return;   // progressive enhancement
       // state is already applied by :checked; wrap any extra DOM work here
       document.startViewTransition(function(){});
     });
   });  */
```
