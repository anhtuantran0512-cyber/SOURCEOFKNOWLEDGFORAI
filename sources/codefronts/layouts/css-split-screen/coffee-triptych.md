---
source: "codefronts"
url: "https://codefronts.com/layouts/css-split-screen/coffee-triptych/"
title: "Coffee Triptych"
section: "layouts"
category: "css-split-screen"
category_name: "CSS Split Screen Layouts"
description: "Three coffee blends side-by-side — espresso brown, cream, copper."
has_js: "false"
---

Here's a working CSS Split Screen Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Coffee Triptych
Source: https://codefronts.com/layouts/css-split-screen/coffee-triptych/

Three coffee blends side-by-side — espresso brown, cream, copper. Three vertical panels in a single row, each with its own roast story. Hover any panel to reveal the tasting notes. CSS grid with 1fr 1fr 1fr and a shared expand-on-hover behavior.
## HTML
```html
<section class="ss-trip" aria-label="Coffee blend triptych">
  <article class="ss-trip-card ss-trip-light">
    <header>
      <span class="ss-trip-bean" aria-hidden="true"></span>
      <h2>Misty<br />Morning</h2>
      <span class="ss-trip-roast">LIGHT ROAST</span>
    </header>
    <p class="ss-trip-notes">Bright, floral, lemon zest. Single origin Ethiopia.</p>
    <footer>€18 · 250g</footer>
  </article>
  <article class="ss-trip-card ss-trip-medium">
    <header>
      <span class="ss-trip-bean" aria-hidden="true"></span>
      <h2>Honey<br />House</h2>
      <span class="ss-trip-roast">MEDIUM</span>
    </header>
    <p class="ss-trip-notes">Caramel, almond, ripe stone fruit. Costa Rica blend.</p>
    <footer>€20 · 250g</footer>
  </article>
  <article class="ss-trip-card ss-trip-dark">
    <header>
      <span class="ss-trip-bean" aria-hidden="true"></span>
      <h2>Midnight<br />Hour</h2>
      <span class="ss-trip-roast">DARK ROAST</span>
    </header>
    <p class="ss-trip-notes">Dark chocolate, smoke, lingering espresso finish.</p>
    <footer>€22 · 250g</footer>
  </article>
</section>
```
## CSS
```css
.ss-trip {
  width: 100%;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  min-height: 100vh;
  font-family: 'Inter', system-ui, sans-serif;
  background: #2a1810;
  border-radius: 0;
  overflow: hidden;
}

.ss-trip-card {
  position: relative;
  padding: 40px 28px;
  display: flex;
  flex-direction: column;
  gap: 18px;
  cursor: pointer;
  transition: padding 0.32s ease;
  border-right: 1px solid rgba(0,0,0,0.2);
  isolation: isolate;
}

.ss-trip-card:last-child {
  border-right: 0;
}

.ss-trip-light {
  background: linear-gradient(180deg, #f4ebd6 0%, #e8d4ba 100%);
  color: #5a3825;
}

.ss-trip-medium {
  background: linear-gradient(180deg, #b8924a 0%, #8a6420 100%);
  color: #f4ebd6;
}

.ss-trip-dark {
  background: linear-gradient(180deg, #2a1810 0%, #1a0e08 100%);
  color: #f4ebd6;
}

.ss-trip-card header {
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.ss-trip-bean {
  width: 56px;
  height: 56px;
  border-radius: 50% 50% 50% 50% / 60% 60% 40% 40%;
  position: relative;
  box-shadow: 0 6px 14px rgba(0,0,0,0.25);
}

.ss-trip-bean::before {
  content: '';
  position: absolute;
  top: 12%;
  left: 50%;
  transform: translateX(-50%);
  width: 4px;
  height: 76%;
  background: rgba(0,0,0,0.4);
  border-radius: 2px;
}

.ss-trip-light .ss-trip-bean {
  background: linear-gradient(135deg, #c89868 0%, #8a5825 100%);
}

.ss-trip-medium .ss-trip-bean {
  background: linear-gradient(135deg, #6a3818 0%, #3a1808 100%);
}

.ss-trip-dark .ss-trip-bean {
  background: linear-gradient(135deg, #2a0806 0%, #050000 100%);
}

.ss-trip-card h2 {
  margin: 0;
  font-family: 'Cormorant Garamond', serif;
  font-size: clamp(28px, 4vw, 44px);
  font-weight: 500;
  line-height: 0.95;
  font-style: italic;
  letter-spacing: -0.01em;
}

.ss-trip-roast {
  font-size: 10.5px;
  font-weight: 800;
  letter-spacing: 0.22em;
  opacity: 0.7;
}

.ss-trip-notes {
  margin: 0;
  font-family: 'Cormorant Garamond', serif;
  font-size: 17px;
  line-height: 1.5;
  opacity: 0.85;
  font-style: italic;
  max-width: 200px;
}

.ss-trip-card footer {
  margin-top: auto;
  font-family: 'Inter', sans-serif;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.08em;
  padding-top: 16px;
  border-top: 1px dashed currentColor;
  opacity: 0.85;
}

.ss-trip-card:hover {
  padding: 36px 28px 36px 36px;
}

.ss-trip-card::after {
  content: '→';
  position: absolute;
  top: 28px;
  right: 28px;
  font-size: 22px;
  font-weight: 100;
  opacity: 0;
  transition: opacity 0.24s, transform 0.24s;
}

.ss-trip-card:hover::after {
  opacity: 1;
  transform: translateX(4px);
}

@media (max-width: 720px) {
  .ss-trip {
    grid-template-columns: 1fr;
  }

  .ss-trip-card {
    border-right: 0;
    border-bottom: 1px solid rgba(0,0,0,0.2);
  }

  .ss-trip-card:last-child {
    border-bottom: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ss-trip-card {
    transition: none;
  }
}
```
