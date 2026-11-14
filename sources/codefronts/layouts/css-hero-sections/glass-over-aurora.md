---
source: "codefronts"
url: "https://codefronts.com/layouts/css-hero-sections/glass-over-aurora/"
title: "Glass over Aurora"
section: "layouts"
category: "css-hero-sections"
category_name: "CSS Hero Sections"
description: "Frosted-glass card floating over a calm spa aurora — pale mint, champagne gold, soft rose. The wellness / luxury beauty editorial treatment."
has_js: "false"
---

Here's a working CSS Hero Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glass over Aurora
Source: https://codefronts.com/layouts/css-hero-sections/glass-over-aurora/

Frosted-glass card floating over a calm spa aurora — pale mint, champagne gold, soft rose. The wellness / luxury beauty editorial treatment.
## HTML
```html
<section class="hs-04" aria-label="Hero">
  <div class="hs-04__aurora" aria-hidden="true"></div>
  <article class="hs-04__card">
    <span class="hs-04__eye">A daily ritual</span>
    <h2>Skincare without <em>the homework.</em></h2>
    <p>Three minutes. Two products. One routine that fits the life you actually live.</p>
    <a class="hs-04__cta" href="#start">Find your routine</a>
  </article>
</section>
```
## CSS
```css
.hs-04 {
  position: relative;
  overflow: hidden;
  display: grid;
  place-items: center;
  width: 100%;
  min-height: 100vh;
  padding: clamp(28px, 5vw, 64px) clamp(20px, 5vw, 56px);
  background: radial-gradient(circle at 20% 20%, #d6f0e0 0%, transparent 50%), radial-gradient(circle at 85% 30%, #f9d4c8 0%, transparent 55%), radial-gradient(circle at 50% 90%, #f3e3c0 0%, transparent 50%), #faf6ed;
  font-family: 'Inter', system-ui, sans-serif;
  color: #3d3a2c;
  box-sizing: border-box;
  contain: layout paint;
}

.hs-04__aurora {
  position: absolute;
  inset: -10%;
  background: conic-gradient(from 90deg, #d6f0e0, #f9d4c8, #f3e3c0, #d6f0e0);
  filter: blur(50px);
  opacity: 0.5;
  animation: hs-04-spin 30s linear infinite;
}

@keyframes hs-04-spin {
  to {
    transform: rotate(360deg);
  }
}

.hs-04__card {
  position: relative;
  z-index: 1;
  max-width: 520px;
  background: rgba(255,255,255,0.55);
  border: 1px solid rgba(255,255,255,0.85);
  border-radius: 24px;
  padding: clamp(28px, 4vw, 44px);
  text-align: center;
  backdrop-filter: blur(20px) saturate(140%);
  -webkit-backdrop-filter: blur(20px) saturate(140%);
  box-shadow: 0 22px 60px rgba(195,150,120,0.18);
}

.hs-04__eye {
  display: inline-block;
  font-family: 'Cormorant Garamond', Georgia, serif;
  font-size: 14px;
  font-style: italic;
  color: #b8956a;
  margin-bottom: 14px;
}

.hs-04 h2 {
  margin: 0 0 16px;
  font-family: 'Cormorant Garamond', Georgia, serif;
  font-size: clamp(32px, 5vw, 52px);
  font-weight: 500;
  letter-spacing: -0.015em;
  line-height: 1.05;
  color: #2a2818;
}

.hs-04 h2 em {
  color: #b8956a;
  font-weight: 600;
}

.hs-04 p {
  margin: 0 auto 24px;
  font-size: 15px;
  line-height: 1.6;
  color: #6b6755;
  max-width: 380px;
}

.hs-04__cta {
  display: inline-block;
  padding: 12px 28px;
  background: #2a2818;
  color: #faf6ed;
  border-radius: 999px;
  text-decoration: none;
  font-size: 14px;
  font-weight: 600;
  letter-spacing: 0.04em;
  transition: background 0.18s;
}

.hs-04__cta:hover {
  background: #b8956a;
}

@media (prefers-reduced-motion: reduce) {
  .hs-04__aurora {
    animation: none;
  }

  .hs-04__cta {
    transition: none;
  }
}
```
