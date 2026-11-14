---
source: "codefronts"
url: "https://codefronts.com/layouts/css-hero-sections/photo-card-hero/"
title: "Photo Card Hero"
section: "layouts"
category: "css-hero-sections"
category_name: "CSS Hero Sections"
description: "Aesop / Apple-style full-bleed photo with copy in the bottom-left corner. Desaturated denim photograph painted in CSS, rust accent, linen card overlay."
has_js: "false"
---

Here's a working CSS Hero Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Photo Card Hero
Source: https://codefronts.com/layouts/css-hero-sections/photo-card-hero/

Aesop / Apple-style full-bleed photo with copy in the bottom-left corner. Desaturated denim photograph painted in CSS, rust accent, linen card overlay.
## HTML
```html
<section class="hs-15" aria-label="Hero">
  <div class="hs-15__wall" aria-hidden="true"></div>
  <div class="hs-15__light" aria-hidden="true"></div>
  <div class="hs-15__scene" aria-hidden="true">
    <span class="hs-15__shelf"></span>
    <span class="hs-15__peg"></span>
    <div class="hs-15__coat">
      <span class="hs-15__collar"></span>
      <span class="hs-15__pocket hs-15__pocket-l"></span>
      <span class="hs-15__pocket hs-15__pocket-r"></span>
      <span class="hs-15__button hs-15__b1"></span>
      <span class="hs-15__button hs-15__b2"></span>
      <span class="hs-15__button hs-15__b3"></span>
    </div>
    <span class="hs-15__shadow"></span>
  </div>
  <span class="hs-15__grain" aria-hidden="true"></span>
  <article class="hs-15__card">
    <span class="hs-15__eye">— A garment for the long haul</span>
    <h2>The chore coat, <em>made to age.</em></h2>
    <p>
      Heavy duck canvas. Rivet-tacked seams. The kind of jacket that earns its character on the
      wearer, not in the wash.
    </p>
    <a class="hs-15__cta" href="#shop">Read the story →</a>
  </article>
  <span class="hs-15__meta" aria-hidden="true">N°04 — DUCK CANVAS WORKWEAR · MADE IN PORTUGAL</span>
</section>
```
## CSS
```css
.hs-15 {
  position: relative;
  overflow: hidden;
  width: 100%;
  min-height: 100vh;
  background: linear-gradient(180deg, #2c3a48 0%, #1f2a35 60%, #15202a 100%);
  font-family: 'Inter', system-ui, sans-serif;
  color: #f3eadb;
  box-sizing: border-box;
  display: grid;
  grid-template-columns: 1.05fr 1fr;
  align-items: stretch;
}

.hs-15__wall {
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(95deg, transparent 0 80px, rgba(255,255,255,0.018) 80px 81px), repeating-linear-gradient(0deg, transparent 0 4px, rgba(0,0,0,0.06) 4px 5px);
  pointer-events: none;
}

.hs-15__light {
  position: absolute;
  inset: 0;
  background: radial-gradient(40% 60% at 30% 25%, rgba(255,230,180,0.16) 0%, transparent 60%), radial-gradient(80% 100% at 50% 100%, rgba(0,0,0,0.5) 0%, transparent 70%);
  pointer-events: none;
}

.hs-15__scene {
  position: relative;
  grid-column: 1;
  grid-row: 1;
  align-self: stretch;
  display: grid;
  place-items: center;
  z-index: 1;
}

.hs-15__shelf {
  position: absolute;
  top: 18%;
  left: 18%;
  right: 18%;
  height: 8px;
  background: linear-gradient(180deg, #5a3e22 0%, #3a2814 100%);
  box-shadow: 0 1px 0 rgba(255,255,255,0.08) inset, 0 4px 8px rgba(0,0,0,0.35);
  border-radius: 2px;
}

.hs-15__peg {
  position: absolute;
  top: 16%;
  left: 50%;
  width: 14px;
  height: 26px;
  background: linear-gradient(180deg, #c89a4e 0%, #7a5a2e 100%);
  border-radius: 6px 6px 4px 4px;
  transform: translateX(-50%);
  box-shadow: 0 2px 4px rgba(0,0,0,0.4);
  z-index: 2;
}

.hs-15__coat {
  position: absolute;
  top: 22%;
  left: 50%;
  width: 200px;
  height: 280px;
  transform: translateX(-50%);
  background: radial-gradient(80% 100% at 50% 0%, #4a5e7a 0%, #34465c 50%, #1f2a3a 100%);
  clip-path: polygon(
      35% 0%, 65% 0%,
      78% 8%, 95% 14%,
      100% 100%,
      0% 100%,
      5% 14%, 22% 8%
    );
  box-shadow: inset -8px 0 24px rgba(0,0,0,0.4), inset 8px 0 16px rgba(255,255,255,0.04);
}

.hs-15__collar {
  position: absolute;
  top: 4%;
  left: 50%;
  width: 56px;
  height: 24px;
  transform: translateX(-50%);
  background: #5a708c;
  clip-path: polygon(0% 0%, 100% 0%, 75% 100%, 25% 100%);
}

.hs-15__pocket {
  position: absolute;
  top: 50%;
  width: 50px;
  height: 60px;
  background: rgba(0,0,0,0.18);
  border: 1.5px solid #2a3848;
  border-radius: 2px;
}

.hs-15__pocket-l {
  left: 14%;
}

.hs-15__pocket-r {
  right: 14%;
}

.hs-15__button {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  width: 8px;
  height: 8px;
  background: radial-gradient(circle at 35% 35%, #d8a05c 0%, #6a4818 100%);
  border-radius: 50%;
  box-shadow: 0 1px 2px rgba(0,0,0,0.4);
}

.hs-15__b1 {
  top: 22%;
}

.hs-15__b2 {
  top: 40%;
}

.hs-15__b3 {
  top: 58%;
}

.hs-15__shadow {
  position: absolute;
  bottom: 0;
  left: 50%;
  width: 240px;
  height: 24px;
  transform: translateX(-50%);
  background: radial-gradient(50% 100% at 50% 0%, rgba(0,0,0,0.55), transparent 70%);
  filter: blur(4px);
}

.hs-15__grain {
  position: absolute;
  inset: 0;
  background-image: radial-gradient(circle at 25% 25%, rgba(255,255,255,0.025) 0.5px, transparent 1px), radial-gradient(circle at 75% 75%, rgba(0,0,0,0.05) 0.5px, transparent 1px);
  background-size: 3px 3px;
  pointer-events: none;
  z-index: 3;
  mix-blend-mode: overlay;
}

.hs-15__card {
  grid-column: 2;
  grid-row: 1;
  align-self: end;
  justify-self: start;
  margin: 0 0 clamp(28px, 4vw, 48px) 0;
  max-width: 440px;
  background: #f3eadb;
  color: #1a2434;
  padding: clamp(22px, 3vw, 32px);
  border-radius: 2px;
  box-shadow: 0 22px 40px rgba(0,0,0,0.32);
  position: relative;
  z-index: 4;
}

.hs-15__eye {
  display: block;
  font-family: 'Cormorant Garamond', Georgia, serif;
  font-style: italic;
  font-size: 14px;
  color: #b85020;
  margin-bottom: 10px;
  letter-spacing: 0.02em;
}

.hs-15 h2 {
  margin: 0 0 14px;
  font-family: 'Cormorant Garamond', Georgia, serif;
  font-size: clamp(28px, 3.6vw, 40px);
  font-weight: 600;
  letter-spacing: -0.01em;
  line-height: 1.1;
}

.hs-15 h2 em {
  color: #b85020;
  font-style: italic;
}

.hs-15__card p {
  margin: 0 0 18px;
  font-size: 14px;
  line-height: 1.6;
  color: #4a5466;
}

.hs-15__cta {
  display: inline-block;
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: #1a2434;
  text-decoration: none;
  border-bottom: 1.5px solid #1a2434;
  padding-bottom: 3px;
  transition: color 0.15s, border-color 0.15s;
}

.hs-15__cta:hover {
  color: #b85020;
  border-color: #b85020;
}

.hs-15__meta {
  position: absolute;
  bottom: clamp(14px, 2vw, 22px);
  left: clamp(20px, 3vw, 32px);
  font-family: 'JetBrains Mono', monospace;
  font-size: 10px;
  letter-spacing: 0.18em;
  color: rgba(243,234,219,0.55);
  z-index: 4;
}

@media (max-width: 720px) {
  .hs-15 {
    grid-template-columns: 1fr;
    grid-template-rows: 280px auto;
  }

  .hs-15__scene {
    grid-column: 1;
    grid-row: 1;
  }

  .hs-15__card {
    grid-column: 1;
    grid-row: 2;
    margin: -40px 16px 16px;
    align-self: auto;
    justify-self: stretch;
  }

  .hs-15__meta {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .hs-15__cta {
    transition: none;
  }
}
```
