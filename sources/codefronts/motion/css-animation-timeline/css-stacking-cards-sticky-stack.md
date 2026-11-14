---
source: "codefronts"
url: "https://codefronts.com/motion/css-animation-timeline/css-stacking-cards-sticky-stack/"
title: "CSS Stacking Cards (Sticky Stack)"
section: "motion"
category: "css-animation-timeline"
category_name: "CSS animation-timeline Demos"
description: "The agency-portfolio showstopper: case-study cards pin to the viewport with position:sticky, and as each new card rolls over the last, the buried card scales…"
has_js: "false"
---

Here's a working CSS animation-timeline Demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Stacking Cards (Sticky Stack)
Source: https://codefronts.com/motion/css-animation-timeline/css-stacking-cards-sticky-stack/

The agency-portfolio showstopper: case-study cards pin to the viewport with position:sticky, and as each new card rolls over the last, the buried card scales down, dims and slips upward — depth choreography driven per-card by its own view() timeline, no index math, no JS.
## HTML
```html
<section class="sda-04" aria-label="Sticky stacking case study cards" role="region" tabindex="0">
  <div class="sda-04__flow">
    <p class="sda-04__hint">Scroll — each card buries the last ↓</p>
    <article class="sda-04__card" style="--i:0;--tint:oklch(0.6 0.17 264)"><span class="sda-04__tag">Case study · 01</span><h3>Meridian Bank</h3><p>Rebuilt the onboarding flow around progressive disclosure; activation up 34%.</p><span class="sda-04__foot">Fintech · 2025</span></article>
    <article class="sda-04__card" style="--i:1;--tint:oklch(0.62 0.15 210)"><span class="sda-04__tag">Case study · 02</span><h3>Fieldnote</h3><p>A note-taking canvas for ecologists — offline-first, sync when the trail ends.</p><span class="sda-04__foot">SaaS · 2025</span></article>
    <article class="sda-04__card" style="--i:2;--tint:oklch(0.64 0.16 150)"><span class="sda-04__tag">Case study · 03</span><h3>Grove &amp; Co.</h3><p>Editorial e-commerce with a scroll-driven lookbook; bounce rate halved.</p><span class="sda-04__foot">Retail · 2026</span></article>
    <article class="sda-04__card" style="--i:3;--tint:oklch(0.66 0.17 60)"><span class="sda-04__tag">Case study · 04</span><h3>Waypoint</h3><p>Trip-planning PWA — map-first UI, 60fps scroll choreography on mid-range phones.</p><span class="sda-04__foot">Travel · 2026</span></article>
    <p class="sda-04__end">Four cards. Zero JavaScript. One timeline each.</p>
  </div>
</section>
```
## CSS
```css
.sda-04,
.sda-04 *,
.sda-04 *::before,
.sda-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sda-04 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: oklch(0.18 0.02 270);
  width: 100%;
  height: 100vh;
  overflow-y: auto;
  padding: 0 20px;
}

.sda-04__flow {
  width: min(560px,100%);
  margin: 0 auto;
  padding: 10vh 0 44vh;
}

.sda-04__hint {
  position: sticky;
  top: 26px;
  text-align: center;
  font-size: 11.5px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: oklch(0.6 0.03 270);
  margin-bottom: 9vh;
}

.sda-04__card {
  position: sticky;
  top: calc(84px + var(--i)*14px);
  height: 300px;
  margin-bottom: 9vh;
  border-radius: 24px;
  padding: 34px 36px;
  display: flex;
  flex-direction: column;
  color: #fff;
  background: linear-gradient(140deg,var(--tint),oklch(from var(--tint) calc(l - 0.18) c calc(h + 30)));
  box-shadow: 0 34px 70px -30px rgba(0,0,0,.75);
  transform-origin: center top;
}

.sda-04__tag {
  font: 700 11px ui-monospace,Menlo,monospace;
  letter-spacing: .14em;
  text-transform: uppercase;
  opacity: .75;
}

.sda-04__card h3 {
  font-size: 32px;
  font-weight: 800;
  letter-spacing: -.02em;
  margin: 16px 0 10px;
}

.sda-04__card p {
  font-size: 16px;
  line-height: 1.6;
  max-width: 38ch;
  opacity: .94;
  text-wrap: pretty;
}

.sda-04__foot {
  margin-top: auto;
  font-size: 12.5px;
  font-weight: 600;
  letter-spacing: .08em;
  text-transform: uppercase;
  opacity: .7;
}

.sda-04__end {
  text-align: center;
  font-size: 13.5px;
  color: oklch(0.6 0.03 270);
  padding-top: 10vh;
}

.sda-04:focus-visible {
  outline: 3px solid oklch(0.65 0.15 210);
  outline-offset: -3px;
}

@supports (animation-timeline: view()) {
  .sda-04__card {
    animation: sda-04-bury linear both;
    animation-timeline: view();
    animation-range: exit-crossing;
  }
}

@keyframes sda-04-bury {
  to {
    transform: translateY(-10px) scale(.92);
    filter: brightness(.62);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sda-04__card {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — position:sticky pins each card while its own view() timeline (animation-range: exit-crossing) scales and dims it exactly as the next card rolls over. */
```
