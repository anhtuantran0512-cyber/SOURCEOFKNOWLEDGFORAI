---
source: "codefronts"
url: "https://codefronts.com/layouts/css-split-screen/coffee-origin-story/"
title: "Coffee Origin Story"
section: "layouts"
category: "css-split-screen"
category_name: "CSS Split Screen Layouts"
description: "Coffee origin story — kraft brown + cream + gold leaf."
has_js: "false"
---

Here's a working CSS Split Screen Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Coffee Origin Story
Source: https://codefronts.com/layouts/css-split-screen/coffee-origin-story/

Coffee origin story — kraft brown + cream + gold leaf. Two-column editorial: hero image map on the left, a numbered story of the bean's journey on the right. Real <ol> with custom counter styling.
## HTML
```html
<section class="ss-cof" aria-label="Coffee origin story">
  <aside class="ss-cof-map">
    <span class="ss-cof-eye">ORIGIN · COLOMBIA</span>
    <h2>From bean<br />to <em>brew.</em></h2>
    <div class="ss-cof-map-svg" aria-hidden="true">
      <span class="ss-cof-pin"></span>
      <span class="ss-cof-pin ss-cof-pin-2"></span>
      <span class="ss-cof-pin ss-cof-pin-3"></span>
      <span class="ss-cof-route"></span>
    </div>
    <ul class="ss-cof-meta">
      <li><strong>1,840m</strong> Altitude</li>
      <li><strong>Q-cup 88+</strong> Score</li>
      <li><strong>Caturra</strong> Varietal</li>
    </ul>
  </aside>
  <article class="ss-cof-story">
    <span class="ss-cof-folio">— Five steps to your cup</span>
    <ol>
      <li>
        <h3>Hand-picked at sunrise</h3>
        <p>
          Only the cherries that turn deep red on the tree. Picked between 5am and 9am, before the
          heat sets in.
        </p>
      </li>
      <li>
        <h3>Washed &amp; sun-dried</h3>
        <p>72 hours on raised beds. Daily turning by the same family of farmers since 1962.</p>
      </li>
      <li>
        <h3>Shipped in jute</h3>
        <p>Single-origin lots, no blending. From Pereira to our roastery in 18 days.</p>
      </li>
      <li>
        <h3>Slow-roasted weekly</h3>
        <p>Light medium, 14 minutes. We rest the beans 48 hours before grinding.</p>
      </li>
      <li>
        <h3>In your cup, today</h3>
        <p>Bright, clean, with notes of brown sugar and ripe peach.</p>
      </li>
    </ol>
  </article>
</section>
```
## CSS
```css
.ss-cof {
  width: 100%;
  display: grid;
  grid-template-columns: 40% 60%;
  min-height: 100vh;
  font-family: 'Inter', system-ui, sans-serif;
  background: #f5ecdc;
  color: #2a1810;
  border-radius: 0;
  overflow: hidden;
}

.ss-cof-map {
  background: linear-gradient(180deg, #6e3818 0%, #3a1808 100%);
  color: #f5ecdc;
  padding: 40px 32px;
  display: flex;
  flex-direction: column;
  gap: 18px;
  position: relative;
  border-right: 1px solid #2a1810;
}

.ss-cof-eye {
  font-family: 'Inter', sans-serif;
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 0.24em;
  color: #d4af37;
}

.ss-cof-map h2 {
  margin: 4px 0 0;
  font-family: 'Cormorant Garamond', serif;
  font-size: clamp(36px, 5vw, 56px);
  font-weight: 500;
  line-height: 0.94;
  color: #f5ecdc;
  letter-spacing: -0.02em;
}

.ss-cof-map h2 em {
  font-style: italic;
  color: #d4af37;
}

.ss-cof-map-svg {
  position: relative;
  flex: 1;
  min-height: 200px;
  background: radial-gradient(60% 60% at 50% 50%, rgba(245,236,220,0.08) 0%, transparent 70%);
  border: 1px dashed rgba(212,175,55,0.4);
  margin-top: 12px;
}

.ss-cof-pin {
  position: absolute;
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: #d4af37;
  box-shadow: 0 0 0 4px rgba(212,175,55,0.25), 0 0 18px rgba(212,175,55,0.4);
}

.ss-cof-pin {
  top: 22%;
  left: 32%;
}

.ss-cof-pin-2 {
  top: 52%;
  left: 58%;
  width: 10px;
  height: 10px;
}

.ss-cof-pin-3 {
  top: 78%;
  left: 24%;
  width: 12px;
  height: 12px;
}

.ss-cof-route {
  position: absolute;
  top: 22%;
  left: 32%;
  width: 140px;
  height: 60%;
  border: 1.5px dashed #d4af37;
  border-color: transparent #d4af37 #d4af37 transparent;
  border-radius: 0 50% 50% 0 / 0 28% 28% 0;
  pointer-events: none;
}

.ss-cof-meta {
  list-style: none;
  margin: 0;
  padding: 14px 0;
  border-top: 1px solid rgba(212,175,55,0.3);
  display: flex;
  flex-direction: column;
  gap: 8px;
  font-family: 'Cormorant Garamond', serif;
  font-size: 16px;
  font-style: italic;
  color: #f5ecdc;
}

.ss-cof-meta strong {
  font-family: 'Inter', sans-serif;
  font-size: 13px;
  font-weight: 700;
  font-style: normal;
  color: #d4af37;
  letter-spacing: 0.04em;
  margin-right: 8px;
}

.ss-cof-story {
  padding: 40px 36px;
  display: flex;
  flex-direction: column;
  gap: 18px;
  background: repeating-linear-gradient(0deg, transparent 0 32px, rgba(110,30,30,0.03) 32px 33px), #faf3e2;
  overflow-y: auto;
}

.ss-cof-folio {
  font-family: 'Inter', sans-serif;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.24em;
  color: #6e3818;
  text-transform: uppercase;
}

.ss-cof-story ol {
  list-style: none;
  counter-reset: cof;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.ss-cof-story li {
  counter-increment: cof;
  padding-left: 60px;
  position: relative;
  padding-bottom: 18px;
  border-bottom: 1px dotted #c8b896;
}

.ss-cof-story li:last-child {
  border-bottom: 0;
}

.ss-cof-story li::before {
  content: counter(cof, decimal-leading-zero);
  position: absolute;
  left: 0;
  top: 0;
  font-family: 'Cormorant Garamond', serif;
  font-size: 38px;
  font-weight: 500;
  font-style: italic;
  color: #d4af37;
  line-height: 1;
}

.ss-cof-story h3 {
  margin: 0;
  font-family: 'Cormorant Garamond', serif;
  font-size: 22px;
  font-weight: 500;
  font-style: italic;
  color: #2a1810;
  letter-spacing: -0.01em;
}

.ss-cof-story p {
  margin: 4px 0 0;
  font-size: 14px;
  line-height: 1.6;
  color: #4a3825;
}

@media (max-width: 720px) {
  .ss-cof {
    grid-template-columns: 1fr;
  }

  .ss-cof-map {
    border-right: 0;
    border-bottom: 1px solid #2a1810;
  }
}
```
