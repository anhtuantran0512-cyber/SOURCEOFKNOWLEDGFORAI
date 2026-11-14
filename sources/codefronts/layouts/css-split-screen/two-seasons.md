---
source: "codefronts"
url: "https://codefronts.com/layouts/css-split-screen/two-seasons/"
title: "Two Seasons"
section: "layouts"
category: "css-split-screen"
category_name: "CSS Split Screen Layouts"
description: "Two seasons of fashion — autumn (rust + ochre + olive) on one side, winter (steel + cobalt + ash) on the other."
has_js: "false"
---

Here's a working CSS Split Screen Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Two Seasons
Source: https://codefronts.com/layouts/css-split-screen/two-seasons/

Two seasons of fashion — autumn (rust + ochre + olive) on one side, winter (steel + cobalt + ash) on the other. Click either label to slide the other half open. Pure CSS via radio inputs + sibling selectors; no JS.
## HTML
```html
<section class="ss-szn" aria-label="Seasonal lookbook split">
  <input id="ss-szn-a" type="radio" name="ss-szn" checked />
  <input id="ss-szn-w" type="radio" name="ss-szn" />
  <article class="ss-szn-fall">
    <span class="ss-szn-tag">FW · Autumn</span>
    <h2>Burnt &amp;<br />Bronzed.</h2>
    <p>
      Wool tweeds, raw selvedge denim, oxblood leather. The fall capsule, hand-finished in our
      atelier.
    </p>
    <ul class="ss-szn-pieces">
      <li><b>01</b> Camel coat</li>
      <li><b>02</b> Rust knit</li>
      <li><b>03</b> Olive trouser</li>
    </ul>
    <label for="ss-szn-w" class="ss-szn-switch">View Winter capsule →</label>
  </article>
  <article class="ss-szn-winter">
    <span class="ss-szn-tag">SS · Winter</span>
    <h2>Cold &amp;<br />Quiet.</h2>
    <p>
      Cashmere knits, double-faced wool coats, alpine boots. The winter capsule, made for stillness.
    </p>
    <ul class="ss-szn-pieces">
      <li><b>01</b> Storm coat</li>
      <li><b>02</b> Steel knit</li>
      <li><b>03</b> Snow boot</li>
    </ul>
    <label for="ss-szn-a" class="ss-szn-switch">← Back to Autumn</label>
  </article>
</section>
```
## CSS
```css
.ss-szn {
  width: 100%;
  position: relative;
  display: grid;
  grid-template-columns: 50% 50%;
  min-height: 100vh;
  font-family: 'Cormorant Garamond', 'Georgia', serif;
  border-radius: 0;
  overflow: hidden;
  isolation: isolate;
  transition: grid-template-columns 0.5s cubic-bezier(0.32, 0.72, 0, 1);
}

.ss-szn:has(#ss-szn-a:checked) {
  grid-template-columns: 65% 35%;
}

.ss-szn:has(#ss-szn-w:checked) {
  grid-template-columns: 35% 65%;
}

.ss-szn input {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip: rect(0 0 0 0);
}

.ss-szn-fall,
.ss-szn-winter {
  padding: 44px 40px;
  display: flex;
  flex-direction: column;
  gap: 18px;
  overflow: hidden;
  position: relative;
  transition: opacity 0.4s ease;
}

.ss-szn-fall {
  background: radial-gradient(60% 80% at 30% 30%, #d97a3c 0%, transparent 60%), linear-gradient(180deg, #6e3825 0%, #2a1810 100%);
  color: #f5e6c8;
}

.ss-szn-fall::before {
  content: '';
  position: absolute;
  top: -10%;
  right: -10%;
  width: 40%;
  height: 50%;
  background: radial-gradient(circle, rgba(255,180,80,0.4), transparent 70%);
  filter: blur(40px);
}

.ss-szn-winter {
  background: radial-gradient(60% 80% at 70% 70%, #4a6a8a 0%, transparent 60%), linear-gradient(180deg, #1a2838 0%, #0e1620 100%);
  color: #d4dce4;
}

.ss-szn-winter::before {
  content: '';
  position: absolute;
  bottom: -10%;
  left: -10%;
  width: 40%;
  height: 50%;
  background: radial-gradient(circle, rgba(180,200,240,0.3), transparent 70%);
  filter: blur(40px);
}

.ss-szn-tag {
  font-family: 'Inter', sans-serif;
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 0.24em;
  align-self: flex-start;
  padding: 6px 12px;
  border: 1px solid currentColor;
}

.ss-szn-fall .ss-szn-tag {
  color: #ffd400;
}

.ss-szn-winter .ss-szn-tag {
  color: #8ac4ff;
}

.ss-szn-fall h2,
.ss-szn-winter h2 {
  margin: 6px 0 0;
  font-size: clamp(40px, 5.5vw, 64px);
  font-weight: 500;
  line-height: 0.92;
  letter-spacing: -0.02em;
  font-style: italic;
}

.ss-szn-fall p,
.ss-szn-winter p {
  margin: 0;
  font-family: 'Inter', sans-serif;
  font-size: 14.5px;
  line-height: 1.6;
  max-width: 360px;
  opacity: 0.85;
}

.ss-szn-pieces {
  list-style: none;
  margin: auto 0 0;
  padding: 14px 0;
  border-top: 1px solid currentColor;
  border-bottom: 1px solid currentColor;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.ss-szn-pieces li {
  display: flex;
  align-items: baseline;
  gap: 14px;
  font-family: 'Cormorant Garamond', serif;
  font-size: 18px;
  font-style: italic;
}

.ss-szn-pieces b {
  font-family: 'Inter', sans-serif;
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 0.16em;
  font-style: normal;
}

.ss-szn-fall .ss-szn-pieces b {
  color: #ffd400;
}

.ss-szn-winter .ss-szn-pieces b {
  color: #8ac4ff;
}

.ss-szn-switch {
  align-self: flex-start;
  padding: 10px 18px;
  font-family: 'Inter', sans-serif;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.12em;
  cursor: pointer;
  border: 1px solid currentColor;
  background: transparent;
  transition: background 0.16s, color 0.16s;
}

.ss-szn-fall .ss-szn-switch:hover {
  background: #ffd400;
  color: #2a1810;
  border-color: #ffd400;
}

.ss-szn-winter .ss-szn-switch:hover {
  background: #8ac4ff;
  color: #0e1620;
  border-color: #8ac4ff;
}

.ss-szn:has(#ss-szn-w:checked) .ss-szn-fall {
  opacity: 0.6;
}

.ss-szn:has(#ss-szn-a:checked) .ss-szn-winter {
  opacity: 0.6;
}

@media (max-width: 720px) {
  .ss-szn,
    .ss-szn:has(#ss-szn-a:checked),
    .ss-szn:has(#ss-szn-w:checked) {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ss-szn {
    transition: none;
  }
}
```
