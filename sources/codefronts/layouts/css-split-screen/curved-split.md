---
source: "codefronts"
url: "https://codefronts.com/layouts/css-split-screen/curved-split/"
title: "Curved Split"
section: "layouts"
category: "css-split-screen"
category_name: "CSS Split Screen Layouts"
description: "Surf brand — ocean teal meets sand beige with a wave-curved seam, sunset-coral CTA."
has_js: "false"
---

Here's a working CSS Split Screen Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Curved Split
Source: https://codefronts.com/layouts/css-split-screen/curved-split/

Surf brand — ocean teal meets sand beige with a wave-curved seam, sunset-coral CTA. Pure CSS curve via border-radius and a generous clip-path. The two halves never share a straight line — feels organic, beach-y, hand-shaped.
## HTML
```html
<section class="ss-srf" aria-label="Surfboard hero">
  <aside class="ss-srf-ocean" aria-hidden="true">
    <span class="ss-srf-sun"></span>
    <span class="ss-srf-wave"></span>
    <span class="ss-srf-board"></span>
  </aside>
  <article class="ss-srf-content">
    <span class="ss-srf-eye">▴ Drift Surf Co.</span>
    <h2>Hand-shaped<br />by the <em>tide.</em></h2>
    <p>
      Custom polyurethane boards, glassed in our Ericeira workshop. 6-week lead time, lifetime
      workmanship guarantee.
    </p>
    <div class="ss-srf-stats">
      <div class="ss-srf-stat"><strong>14</strong><span>Shapers</span></div>
      <div class="ss-srf-stat"><strong>2,400</strong><span>Boards / yr</span></div>
      <div class="ss-srf-stat"><strong>1972</strong><span>Founded</span></div>
    </div>
    <button type="button" class="ss-srf-cta">Shape your board →</button>
  </article>
</section>
```
## CSS
```css
.ss-srf {
  width: 100%;
  display: grid;
  grid-template-columns: 45% 55%;
  min-height: 100vh;
  font-family: 'Inter', system-ui, sans-serif;
  background: #f5ecd9;
  color: #1a3a3f;
  border-radius: 0;
  overflow: hidden;
  position: relative;
}

.ss-srf-ocean {
  position: relative;
  background: linear-gradient(180deg, #2c8a8e 0%, #1a3a3f 100%);
  overflow: hidden;
  isolation: isolate;
}

.ss-srf-ocean::after {
  content: '';
  position: absolute;
  right: -120px;
  top: 0;
  bottom: 0;
  width: 240px;
  background: #f5ecd9;
  border-radius: 50% 0 0 50% / 50% 0 0 50%;
  z-index: 2;
}

.ss-srf-sun {
  position: absolute;
  top: 14%;
  left: 22%;
  width: 90px;
  height: 90px;
  border-radius: 50%;
  background: radial-gradient(circle at 35% 35%, #ffe899 0%, #ff8a40 60%, #c45a1c 100%);
  box-shadow: 0 0 60px rgba(255,170,68,0.5);
}

.ss-srf-wave {
  position: absolute;
  bottom: 18%;
  left: -10%;
  right: -20%;
  height: 80px;
  background: radial-gradient(ellipse at 30% 100%, rgba(255,255,255,0.45), transparent 60%), radial-gradient(ellipse at 70% 100%, rgba(255,255,255,0.35), transparent 60%);
  border-radius: 50%;
  filter: blur(2px);
}

.ss-srf-wave::before {
  content: '';
  position: absolute;
  left: 0;
  right: 0;
  bottom: -10px;
  height: 24px;
  background: rgba(255,255,255,0.25);
  border-radius: 50%;
  filter: blur(6px);
}

.ss-srf-board {
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%) rotate(28deg);
  width: 56px;
  height: 240px;
  border-radius: 28px / 90px;
  background: linear-gradient(180deg, #fff 0%, #ffe9c4 50%, #ff8a40 100%);
  box-shadow: 0 8px 24px rgba(0,0,0,0.4);
  z-index: 3;
}

.ss-srf-board::before {
  content: '';
  position: absolute;
  left: 50%;
  top: 12%;
  transform: translateX(-50%);
  width: 2px;
  height: 76%;
  background: rgba(0,0,0,0.18);
}

.ss-srf-content {
  padding: 44px 48px 44px 36px;
  display: flex;
  flex-direction: column;
  gap: 22px;
  position: relative;
  z-index: 1;
}

.ss-srf-eye {
  font-family: 'Inter', sans-serif;
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: #c45a1c;
}

.ss-srf-content h2 {
  margin: 4px 0 0;
  font-family: 'Cormorant Garamond', serif;
  font-size: clamp(36px, 5vw, 60px);
  font-weight: 500;
  line-height: 0.95;
  color: #1a3a3f;
  letter-spacing: -0.02em;
}

.ss-srf-content h2 em {
  font-style: italic;
  color: #c45a1c;
}

.ss-srf-content p {
  margin: 0;
  font-size: 15.5px;
  line-height: 1.6;
  color: #3a5a5f;
  max-width: 460px;
}

.ss-srf-stats {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 14px;
  max-width: 420px;
  padding: 14px 0;
  border-top: 1px solid #c8b896;
  border-bottom: 1px solid #c8b896;
}

.ss-srf-stat {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.ss-srf-stats strong {
  font-family: 'Cormorant Garamond', serif;
  font-size: 28px;
  font-weight: 500;
  color: #2c8a8e;
  letter-spacing: -0.02em;
  font-style: italic;
}

.ss-srf-stats span {
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: 0.16em;
  color: #6a4a35;
  text-transform: uppercase;
}

.ss-srf-cta {
  align-self: flex-start;
  padding: 14px 24px;
  background: #c45a1c;
  color: #fff;
  border: 0;
  border-radius: 28px;
  font-family: 'Inter', sans-serif;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.04em;
  cursor: pointer;
  box-shadow: 0 6px 18px rgba(196,90,28,0.35);
  transition: transform 0.12s, box-shadow 0.12s;
}

.ss-srf-cta:hover {
  transform: translateY(-1px);
  box-shadow: 0 10px 24px rgba(196,90,28,0.45);
}

@media (max-width: 720px) {
  .ss-srf {
    grid-template-columns: 1fr;
  }

  .ss-srf-ocean {
    min-height: 280px;
  }

  .ss-srf-ocean::after {
    display: none;
  }

  .ss-srf-stats {
    grid-template-columns: 1fr;
  }
}
```
