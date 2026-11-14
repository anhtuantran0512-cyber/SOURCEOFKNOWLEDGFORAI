---
source: "codefronts"
url: "https://codefronts.com/layouts/css-card-grid-layout/css-hero-photo-collage-grid/"
title: "CSS Hero Photo Collage Grid"
section: "layouts"
category: "css-card-grid-layout"
category_name: "CSS Card Grid Layouts"
description: "A landing-page hero with a 5-tile asymmetric photo collage on the right and a marketing headline + CTA on the left — the exact pattern Airbnb, Notion, and…"
has_js: "false"
---

Here's a working CSS Card Grid Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Hero Photo Collage Grid
Source: https://codefronts.com/layouts/css-card-grid-layout/css-hero-photo-collage-grid/

A landing-page hero with a 5-tile asymmetric photo collage on the right and a marketing headline + CTA on the left — the exact pattern Airbnb, Notion, and Linear use to combine narrative copy with visual proof on their homepage hero. Photos are CSS gradient placeholders with location labels and category pills.
## HTML
```html
<div class="cg-12">
  <div class="cg-12__inner">

    <div class="cg-12__copy">
      <span class="cg-12__kicker">New · 2026 collection</span>
      <h2 class="cg-12__title">Stay places that<br><em>feel like home.</em></h2>
      <p class="cg-12__lede">Hand-picked stays in 47 cities. Verified by humans. Booked by people who care where they sleep.</p>
      <div class="cg-12__actions">
        <a href="#" class="cg-12__cta">Browse stays →</a>
        <a href="#" class="cg-12__link">How it works</a>
      </div>
      <div class="cg-12__metrics">
        <div><strong>4.9 ★</strong><span>Avg rating</span></div>
        <div><strong>12K+</strong><span>Verified stays</span></div>
        <div><strong>47</strong><span>Cities</span></div>
      </div>
    </div>

    <div class="cg-12__collage">
      <div class="cg-12__photo cg-12__photo--1">
        <span class="cg-12__pill">Iceland</span>
        <span class="cg-12__label">Black Sand Cabin</span>
      </div>
      <div class="cg-12__photo cg-12__photo--2">
        <span class="cg-12__pill">Tokyo</span>
        <span class="cg-12__label">Shibuya Loft</span>
      </div>
      <div class="cg-12__photo cg-12__photo--3">
        <span class="cg-12__pill">Lisbon</span>
        <span class="cg-12__label">Alfama Studio</span>
      </div>
      <div class="cg-12__photo cg-12__photo--4">
        <span class="cg-12__pill">Marrakech</span>
        <span class="cg-12__label">Medina Riad</span>
      </div>
      <div class="cg-12__photo cg-12__photo--5">
        <span class="cg-12__pill">Brooklyn</span>
        <span class="cg-12__label">Williamsburg Flat</span>
      </div>
    </div>

  </div>
</div>
```
## CSS
```css
.cg-12,
.cg-12 *,
.cg-12 *::before,
.cg-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cg-12 ::selection {
  background: #0f172a;
  color: #fff;
}

.cg-12 {
  --bg: #fafaf7;
  --ink: #0f172a;
  --muted: #64748b;
  --accent: #dc2626;
  --line: #e2e8f0;
  min-height: 100vh;
  background: var(--bg);
  padding: clamp(28px,4vw,56px) clamp(20px,3vw,48px);
  font-family: -apple-system,BlinkMacSystemFont,"Inter","Segoe UI",sans-serif;
  color: var(--ink);
  display: flex;
  align-items: center;
  justify-content: center;
}

.cg-12__inner {
  width: 100%;
  max-width: 1200px;
  display: grid;
  grid-template-columns: 1fr 1.2fr;
  gap: clamp(24px,3.4vw,56px);
  align-items: center;
}

.cg-12__copy {
  display: flex;
  flex-direction: column;
  gap: 18px;
  max-width: 520px;
}

.cg-12__kicker {
  display: inline-block;
  width: fit-content;
  font-size: .72rem;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--accent);
  padding: 5px 12px;
  border-radius: 999px;
  background: rgba(220,38,38,.1);
}

.cg-12__title {
  font-size: clamp(2.2rem,4.5vw,3.6rem);
  font-weight: 900;
  letter-spacing: -.03em;
  line-height: 1.02;
}

.cg-12__title em {
  font-style: italic;
  color: var(--accent);
  font-family: Georgia,"Times New Roman",serif;
  font-weight: 700;
}

.cg-12__lede {
  font-size: clamp(.96rem,1.2vw,1.1rem);
  color: var(--muted);
  line-height: 1.55;
  max-width: 46ch;
}

.cg-12__actions {
  display: flex;
  align-items: center;
  gap: 16px;
  flex-wrap: wrap;
  margin-top: 6px;
}

.cg-12__cta {
  display: inline-block;
  background: var(--ink);
  color: #fff;
  padding: 14px 22px;
  border-radius: 10px;
  font-weight: 700;
  font-size: .96rem;
  text-decoration: none;
  transition: transform .2s,background .2s;
}

.cg-12__cta:hover {
  background: var(--accent);
  transform: translateY(-2px);
}

.cg-12__link {
  font-size: .94rem;
  font-weight: 600;
  color: var(--ink);
  text-decoration: none;
  position: relative;
}

.cg-12__link::after {
  content: "";
  position: absolute;
  left: 0;
  right: 0;
  bottom: -3px;
  height: 1.5px;
  background: currentColor;
}

.cg-12__metrics {
  display: flex;
  gap: clamp(20px,3vw,40px);
  margin-top: 16px;
  padding-top: 24px;
  border-top: 1px solid var(--line);
}

.cg-12__metrics > div {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.cg-12__metrics strong {
  font-size: 1.5rem;
  font-weight: 900;
  letter-spacing: -.02em;
}

.cg-12__metrics span {
  font-size: .78rem;
  color: var(--muted);
  font-weight: 600;
}
/* Collage */

.cg-12__collage {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  grid-template-rows: repeat(3,1fr);
  gap: clamp(8px,1vw,14px);
  aspect-ratio: 1.05/1;
  min-height: clamp(320px,42vw,560px);
}

.cg-12__photo {
  position: relative;
  border-radius: 14px;
  overflow: hidden;
  display: flex;
  align-items: flex-end;
  padding: 12px;
  isolation: isolate;
}

.cg-12__photo::after {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg,transparent 45%,rgba(0,0,0,.55));
  z-index: 0;
}

.cg-12__pill {
  position: absolute;
  top: 10px;
  right: 10px;
  background: rgba(255,255,255,.92);
  color: var(--ink);
  font-size: .62rem;
  font-weight: 700;
  letter-spacing: .1em;
  text-transform: uppercase;
  padding: 4px 9px;
  border-radius: 999px;
  backdrop-filter: blur(8px);
  z-index: 2;
}

.cg-12__label {
  position: relative;
  z-index: 1;
  color: #fff;
  font-size: .86rem;
  font-weight: 700;
  letter-spacing: -.005em;
  text-shadow: 0 1px 3px rgba(0,0,0,.4);
}

.cg-12__photo--1 {
  grid-column: 1 / span 2;
  grid-row: 1 / span 2;
  background: linear-gradient(135deg,#1e3a5f,#0f1c2e);
}

.cg-12__photo--2 {
  grid-column: 3 / span 1;
  grid-row: 1 / span 1;
  background: linear-gradient(135deg,#d97a99,#7a3855);
}

.cg-12__photo--3 {
  grid-column: 3 / span 1;
  grid-row: 2 / span 1;
  background: linear-gradient(135deg,#f4a572,#d97f4f);
}

.cg-12__photo--4 {
  grid-column: 1 / span 1;
  grid-row: 3 / span 1;
  background: linear-gradient(135deg,#e6c54a,#a8732d);
}

.cg-12__photo--5 {
  grid-column: 2 / span 2;
  grid-row: 3 / span 1;
  background: linear-gradient(135deg,#7aa852,#3d6a2a);
}

@media (max-width: 900px) {
  .cg-12__inner {
    grid-template-columns: 1fr;
    gap: 32px;
  }

  .cg-12__copy {
    max-width: none;
    text-align: center;
    align-items: center;
  }

  .cg-12__kicker {
    margin: 0 auto 0 0;
  }

  .cg-12__collage {
    aspect-ratio: 1.4/1;
    min-height: 280px;
  }
}

@media (max-width: 560px) {
  .cg-12__metrics {
    gap: 14px;
  }

  .cg-12__metrics strong {
    font-size: 1.25rem;
  }

  .cg-12__collage {
    aspect-ratio: 1/1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cg-12__cta {
    transition: none;
  }
}
```
