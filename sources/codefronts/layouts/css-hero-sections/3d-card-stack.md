---
source: "codefronts"
url: "https://codefronts.com/layouts/css-hero-sections/3d-card-stack/"
title: "3D Card Stack"
section: "layouts"
category: "css-hero-sections"
category_name: "CSS Hero Sections"
description: "Three luxury-cosmetics product cards in 3D perspective, fanning forward on hover. Champagne and soft blush on jet — the high-end beauty / fragrance treatment."
has_js: "false"
---

Here's a working CSS Hero Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: 3D Card Stack
Source: https://codefronts.com/layouts/css-hero-sections/3d-card-stack/

Three luxury-cosmetics product cards in 3D perspective, fanning forward on hover. Champagne and soft blush on jet — the high-end beauty / fragrance treatment.
## HTML
```html
<section class="hs-27" aria-label="Hero">
  <div class="hs-27__copy">
    <span class="hs-27__eye">— Cuvée 04</span>
    <h2>The fragrance <em>three editors couldn't stop wearing.</em></h2>
    <p>Bergamot, oud, and a single drop of Damascus rose. 50ml. Limited.</p>
    <a class="hs-27__cta" href="#shop">Discover the bottle</a>
  </div>
  <div class="hs-27__stack">
    <article class="hs-27__card hs-27__c1"><strong>04</strong><em>Cuvée</em></article>
    <article class="hs-27__card hs-27__c2"><strong>04</strong><em>Cuvée</em></article>
    <article class="hs-27__card hs-27__c3"><strong>04</strong><em>Cuvée</em></article>
  </div>
</section>
```
## CSS
```css
.hs-27 {
  display: grid;
  grid-template-columns: 1fr 1fr;
  width: 100%;
  min-height: 100vh;
  padding: clamp(28px, 5vw, 56px);
  gap: clamp(20px, 4vw, 56px);
  align-items: center;
  background: #0d0a0a;
  font-family: 'Inter', system-ui, sans-serif;
  color: #f0e0c8;
  box-sizing: border-box;
  perspective: 1200px;
}

.hs-27__eye {
  display: inline-block;
  font-family: 'Cormorant Garamond', Georgia, serif;
  font-style: italic;
  font-size: 16px;
  color: #c69e5a;
  margin-bottom: 14px;
}

.hs-27 h2 {
  margin: 0 0 18px;
  font-family: 'Playfair Display', Georgia, serif;
  font-size: clamp(28px, 4.5vw, 46px);
  font-weight: 600;
  letter-spacing: -0.01em;
  line-height: 1.1;
  color: #f0e0c8;
}

.hs-27 h2 em {
  color: #f5c2c8;
  font-style: italic;
}

.hs-27 p {
  margin: 0 0 24px;
  font-size: 15px;
  line-height: 1.6;
  color: #b89878;
  max-width: 380px;
}

.hs-27__cta {
  display: inline-block;
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.16em;
  color: #c69e5a;
  text-decoration: none;
  border-bottom: 1.5px solid #c69e5a;
  padding-bottom: 3px;
  transition: color 0.18s, border-color 0.18s;
}

.hs-27__cta:hover {
  color: #f5c2c8;
  border-color: #f5c2c8;
}

.hs-27__stack {
  position: relative;
  height: 100%;
  min-height: 360px;
  display: grid;
  place-items: center;
  transform-style: preserve-3d;
}

.hs-27__card {
  position: absolute;
  width: 180px;
  height: 260px;
  background: linear-gradient(135deg, #2a1a1a 0%, #0d0a0a 100%);
  border: 1px solid #c69e5a;
  border-radius: 6px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 8px;
  transition: transform 0.4s cubic-bezier(.22,1,.36,1);
}

.hs-27__card strong {
  font-family: 'Playfair Display', Georgia, serif;
  font-size: 64px;
  font-weight: 800;
  font-style: italic;
  color: #c69e5a;
  line-height: 1;
}

.hs-27__card em {
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  font-style: normal;
  letter-spacing: 0.24em;
  color: #c69e5a;
}

.hs-27__c1 {
  transform: translateX(-90px) rotateY(20deg) translateZ(-40px);
}

.hs-27__c2 {
  transform: translateZ(0);
  z-index: 2;
  background: linear-gradient(135deg, #3a2828 0%, #1a1010 100%);
}

.hs-27__c3 {
  transform: translateX(90px) rotateY(-20deg) translateZ(-40px);
}

.hs-27__stack:hover .hs-27__c1 {
  transform: translateX(-130px) rotateY(20deg) translateZ(0);
}

.hs-27__stack:hover .hs-27__c2 {
  transform: translateZ(40px);
}

.hs-27__stack:hover .hs-27__c3 {
  transform: translateX(130px) rotateY(-20deg) translateZ(0);
}

@media (max-width: 720px) {
  .hs-27 {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .hs-27__card {
    transition: none;
  }

  .hs-27__cta {
    transition: none;
  }
}
```
