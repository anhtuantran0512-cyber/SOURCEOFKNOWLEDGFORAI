---
source: "codefronts"
url: "https://codefronts.com/layouts/css-hero-sections/neon-cta-hero/"
title: "Neon CTA Hero"
section: "layouts"
category: "css-hero-sections"
category_name: "CSS Hero Sections"
description: "Tokyo-cyberpunk neon CTA — pure black backdrop, neon pink and electric cyan glows, single CTA that breathes with a soft pulse. The conversion-funnel pattern."
has_js: "false"
---

Here's a working CSS Hero Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neon CTA Hero
Source: https://codefronts.com/layouts/css-hero-sections/neon-cta-hero/

Tokyo-cyberpunk neon CTA — pure black backdrop, neon pink and electric cyan glows, single CTA that breathes with a soft pulse. The conversion-funnel pattern.
## HTML
```html
<section class="hs-24" aria-label="Hero">
  <span class="hs-24__grid" aria-hidden="true"></span>
  <div class="hs-24__inner">
    <span class="hs-24__eye">/ ENTER THE NIGHT MARKET</span>
    <h2>Order ramen at <em>3 a.m.</em> like the locals do.</h2>
    <p>50 Tokyo back-alley vendors. One delivery app. One foreigner-friendly menu.</p>
    <a class="hs-24__cta" href="#order">Open the menu</a>
  </div>
</section>
```
## CSS
```css
.hs-24 {
  position: relative;
  overflow: hidden;
  display: grid;
  place-items: center;
  width: 100%;
  min-height: 100vh;
  padding: clamp(28px, 5vw, 64px) clamp(20px, 5vw, 56px);
  background: #0a0014;
  font-family: 'Inter', system-ui, sans-serif;
  color: #fff;
  box-sizing: border-box;
  contain: layout paint;
}

.hs-24__grid {
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 220%;
  height: 50%;
  background: repeating-linear-gradient(0deg, transparent 0 24px, rgba(238,82,206,0.32) 24px 25px), repeating-linear-gradient(90deg, transparent 0 24px, rgba(34,211,238,0.32) 24px 25px);
  transform: translateX(-50%) perspective(800px) rotateX(60deg);
  transform-origin: center top;
  mask-image: linear-gradient(180deg, transparent 0%, #000 40%);
  -webkit-mask-image: linear-gradient(180deg, transparent 0%, #000 40%);
  pointer-events: none;
}

.hs-24__inner {
  position: relative;
  z-index: 1;
  max-width: 720px;
  text-align: center;
}

.hs-24__eye {
  display: inline-block;
  font-family: 'JetBrains Mono', monospace;
  font-size: 11.5px;
  letter-spacing: 0.24em;
  color: #22d3ee;
  padding: 4px 14px;
  border: 1px solid #22d3ee;
  text-shadow: 0 0 10px rgba(34,211,238,0.6);
  margin-bottom: 22px;
}

.hs-24 h2 {
  margin: 0 0 18px;
  font-size: clamp(36px, 6vw, 64px);
  font-weight: 900;
  letter-spacing: -0.02em;
  line-height: 1.05;
  text-shadow: 0 0 30px rgba(238,82,206,0.4);
}

.hs-24 h2 em {
  color: #ee52ce;
  font-style: italic;
  text-shadow: 0 0 18px rgba(238,82,206,0.7);
}

.hs-24 p {
  margin: 0 auto 28px;
  font-size: 16px;
  color: #a890c8;
  max-width: 460px;
  line-height: 1.55;
}

.hs-24__cta {
  display: inline-block;
  padding: 14px 36px;
  background: transparent;
  color: #ee52ce;
  border: 2px solid #ee52ce;
  border-radius: 0;
  font-weight: 800;
  font-size: 15px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  text-decoration: none;
  box-shadow: 0 0 18px rgba(238,82,206,0.5), inset 0 0 18px rgba(238,82,206,0.18);
  animation: hs-24-pulse 2.4s ease-in-out infinite alternate;
  transition: background 0.15s, color 0.15s;
}

@keyframes hs-24-pulse {
  from {
    box-shadow: 0 0 14px rgba(238,82,206,0.4), inset 0 0 14px rgba(238,82,206,0.14);
  }

  to {
    box-shadow: 0 0 28px rgba(238,82,206,0.7), inset 0 0 24px rgba(238,82,206,0.28);
  }
}

.hs-24__cta:hover {
  background: #ee52ce;
  color: #0a0014;
}

@media (prefers-reduced-motion: reduce) {
  .hs-24__cta {
    animation: none;
    transition: none;
  }
}
```
