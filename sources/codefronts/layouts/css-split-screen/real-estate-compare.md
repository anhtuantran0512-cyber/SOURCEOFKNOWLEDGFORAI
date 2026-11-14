---
source: "codefronts"
url: "https://codefronts.com/layouts/css-split-screen/real-estate-compare/"
title: "Real-estate Compare"
section: "layouts"
category: "css-split-screen"
category_name: "CSS Split Screen Layouts"
description: "Compare two properties — terracotta + olive + warm beige."
has_js: "false"
---

Here's a working CSS Split Screen Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Real-estate Compare
Source: https://codefronts.com/layouts/css-split-screen/real-estate-compare/

Compare two properties — terracotta + olive + warm beige. Two cards side by side, each with hero number, key stats, and price. Hover any side to scale up; the other dims subtly. CSS transform + opacity transitions.
## HTML
```html
<section class="ss-est" aria-label="Property comparison">
  <article class="ss-est-card ss-est-warm">
    <header>
      <span class="ss-est-tag">FOR SALE · Verified</span>
      <h3>Casa Sol</h3>
      <p>Mid-century courtyard home, walking distance to the village.</p>
    </header>
    <div class="ss-est-photo" aria-hidden="true">
      <span class="ss-est-house"></span>
      <span class="ss-est-tree"></span>
      <span class="ss-est-tree2"></span>
    </div>
    <dl class="ss-est-stats">
      <dt>Beds</dt>
      <dd>4</dd>
      <dt>Baths</dt>
      <dd>3</dd>
      <dt>Sq m</dt>
      <dd>240</dd>
      <dt>Built</dt>
      <dd>1958</dd>
    </dl>
    <footer>
      <strong>€840,000</strong>
      <button type="button">Schedule tour →</button>
    </footer>
  </article>
  <article class="ss-est-card ss-est-cool">
    <header>
      <span class="ss-est-tag">FOR SALE · New listing</span>
      <h3>Casa Verde</h3>
      <p>Modern earth-tone build with garden views and original olive trees.</p>
    </header>
    <div class="ss-est-photo" aria-hidden="true">
      <span class="ss-est-house ss-est-house-2"></span>
      <span class="ss-est-tree"></span>
      <span class="ss-est-tree2"></span>
    </div>
    <dl class="ss-est-stats">
      <dt>Beds</dt>
      <dd>3</dd>
      <dt>Baths</dt>
      <dd>2</dd>
      <dt>Sq m</dt>
      <dd>185</dd>
      <dt>Built</dt>
      <dd>2022</dd>
    </dl>
    <footer>
      <strong>€720,000</strong>
      <button type="button">Schedule tour →</button>
    </footer>
  </article>
</section>
```
## CSS
```css
.ss-est {
  width: 100%;
  display: grid;
  grid-template-columns: 1fr 1fr;
  min-height: 100vh;
  font-family: 'Inter', system-ui, sans-serif;
  gap: 0;
  background: #efe7d4;
  border-radius: 0;
  overflow: hidden;
}

.ss-est-card {
  padding: 36px 32px;
  display: flex;
  flex-direction: column;
  gap: 18px;
  position: relative;
  transition: transform 0.32s ease, opacity 0.32s ease;
  isolation: isolate;
}

.ss-est-warm {
  background: linear-gradient(180deg, #d97a3c 0%, #b85a2c 100%);
  color: #fff8e8;
  border-right: 1px solid rgba(0,0,0,0.18);
}

.ss-est-cool {
  background: linear-gradient(180deg, #6e7a3c 0%, #4a5a25 100%);
  color: #f4ecd0;
}

.ss-est:has(.ss-est-warm:hover) .ss-est-cool,
.ss-est:has(.ss-est-cool:hover) .ss-est-warm {
  opacity: 0.6;
}

.ss-est-card:hover {
  transform: scale(1.02);
  z-index: 2;
}

.ss-est-tag {
  font-family: 'Courier New', monospace;
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: 0.18em;
  align-self: flex-start;
  padding: 4px 10px;
  background: rgba(0,0,0,0.18);
}

.ss-est-card h3 {
  margin: 6px 0 0;
  font-family: 'Cormorant Garamond', serif;
  font-size: clamp(28px, 4vw, 40px);
  font-weight: 500;
  letter-spacing: -0.02em;
  font-style: italic;
}

.ss-est-card header p {
  margin: 4px 0 0;
  font-size: 13.5px;
  line-height: 1.55;
  opacity: 0.85;
  max-width: 280px;
}

.ss-est-photo {
  position: relative;
  aspect-ratio: 16 / 9;
  background: linear-gradient(180deg, rgba(255,255,255,0.18) 0%, rgba(255,255,255,0.04) 100%);
  border: 1px solid rgba(255,255,255,0.18);
  overflow: hidden;
}

.ss-est-house {
  position: absolute;
  bottom: 12%;
  left: 50%;
  transform: translateX(-50%);
  width: 50%;
  height: 50%;
  background: linear-gradient(180deg, #f5e6c8 0%, #d4c598 100%);
  border-bottom: 4px solid rgba(0,0,0,0.3);
}

.ss-est-house::before {
  content: '';
  position: absolute;
  left: -8%;
  right: -8%;
  top: -22%;
  height: 28%;
  background: #6e1f1c;
  clip-path: polygon(50% 0, 100% 100%, 0 100%);
}

.ss-est-house::after {
  content: '';
  position: absolute;
  left: 30%;
  bottom: 0;
  width: 18%;
  height: 50%;
  background: #2a1810;
}

.ss-est-house-2 {
  background: linear-gradient(180deg, #d8d0b8 0%, #a8a088 100%);
}

.ss-est-house-2::before {
  background: #2a3325;
  clip-path: polygon(0 0, 100% 0, 100% 100%, 0 100%);
  height: 14%;
  top: -14%;
}

.ss-est-tree,
.ss-est-tree2 {
  position: absolute;
  bottom: 12%;
  width: 40px;
  height: 60px;
  background: radial-gradient(circle at 50% 30%, #4a6a25 0%, #2a3a18 100%);
  border-radius: 50%;
}

.ss-est-tree {
  left: 8%;
}

.ss-est-tree2 {
  right: 8%;
  bottom: 14%;
  width: 50px;
  height: 50px;
}

.ss-est-stats {
  margin: 0;
  padding: 14px 0;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 6px;
  border-top: 1px solid rgba(255,255,255,0.18);
  border-bottom: 1px solid rgba(255,255,255,0.18);
}

.ss-est-stats dt {
  font-family: 'Courier New', monospace;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.16em;
  opacity: 0.6;
}

.ss-est-stats dd {
  margin: 2px 0 0;
  font-family: 'Cormorant Garamond', serif;
  font-size: 22px;
  font-weight: 500;
  font-style: italic;
}

.ss-est-card footer {
  margin-top: auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 14px;
}

.ss-est-card footer strong {
  font-family: 'Cormorant Garamond', serif;
  font-size: 26px;
  font-weight: 500;
  letter-spacing: -0.01em;
}

.ss-est-card footer button {
  padding: 11px 18px;
  background: rgba(0,0,0,0.25);
  color: inherit;
  border: 1px solid rgba(255,255,255,0.3);
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.04em;
  cursor: pointer;
  transition: background 0.14s;
}

.ss-est-card footer button:hover {
  background: rgba(0,0,0,0.45);
}

@media (max-width: 720px) {
  .ss-est {
    grid-template-columns: 1fr;
  }

  .ss-est-warm {
    border-right: 0;
    border-bottom: 1px solid rgba(0,0,0,0.18);
  }

  .ss-est-card:hover {
    transform: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ss-est-card {
    transition: none;
  }
}
```
