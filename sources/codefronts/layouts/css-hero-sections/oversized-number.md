---
source: "codefronts"
url: "https://codefronts.com/layouts/css-hero-sections/oversized-number/"
title: "Oversized Number"
section: "layouts"
category: "css-hero-sections"
category_name: "CSS Hero Sections"
description: "Vintage wine-label poster — a massive faded burgundy \"1924\" set behind italic serif copy with gold-leaf accents on cream paper."
has_js: "false"
---

Here's a working CSS Hero Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Oversized Number
Source: https://codefronts.com/layouts/css-hero-sections/oversized-number/

Vintage wine-label poster — a massive faded burgundy "1924" set behind italic serif copy with gold-leaf accents on cream paper.
## HTML
```html
<section class="hs-13" aria-label="Hero">
  <div class="hs-13__bg" aria-hidden="true">1924</div>
  <div class="hs-13__inner">
    <span class="hs-13__eye">— Estate · Vinifera ·</span>
    <h2>A century of <em>quiet wines.</em></h2>
    <p>
      Six grapes. Four hectares. One family that still skips the marketing and lets the vintage
      speak.
    </p>
    <a class="hs-13__cta" href="#cellar">Visit the cellar</a>
  </div>
</section>
```
## CSS
```css
.hs-13 {
  position: relative;
  overflow: hidden;
  display: grid;
  place-items: center;
  width: 100%;
  min-height: 100vh;
  padding: clamp(28px, 5vw, 64px) clamp(20px, 5vw, 56px);
  background: #f5ebd4;
  font-family: 'Playfair Display', Georgia, serif;
  color: #2a0a18;
  box-sizing: border-box;
}

.hs-13__bg {
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%,-50%);
  font-size: clamp(220px, 38vw, 480px);
  font-weight: 900;
  line-height: 1;
  color: #6b1230;
  opacity: 0.12;
  pointer-events: none;
  letter-spacing: -0.02em;
}

.hs-13__inner {
  position: relative;
  z-index: 1;
  max-width: 580px;
  text-align: center;
}

.hs-13__eye {
  display: inline-block;
  font-family: 'Cormorant Garamond', Georgia, serif;
  font-style: italic;
  font-size: 16px;
  color: #c69e3d;
  margin-bottom: 16px;
  letter-spacing: 0.08em;
}

.hs-13 h2 {
  margin: 0 0 18px;
  font-size: clamp(36px, 6vw, 60px);
  font-weight: 600;
  line-height: 1.05;
}

.hs-13 h2 em {
  color: #6b1230;
  font-style: italic;
}

.hs-13 p {
  font-family: 'Cormorant Garamond', Georgia, serif;
  font-style: italic;
  font-size: 18px;
  line-height: 1.55;
  color: #5a3848;
  margin: 0 auto 24px;
  max-width: 460px;
}

.hs-13__cta {
  display: inline-block;
  padding: 12px 28px;
  background: transparent;
  color: #6b1230;
  border: 1.5px solid #6b1230;
  border-radius: 0;
  text-decoration: none;
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  transition: background 0.18s, color 0.18s;
}

.hs-13__cta:hover {
  background: #6b1230;
  color: #f5ebd4;
}

@media (prefers-reduced-motion: reduce) {
  .hs-13__cta {
    transition: none;
  }
}
```
