---
source: "codefronts"
url: "https://codefronts.com/layouts/css-hero-sections/particle-starfield/"
title: "Particle Starfield"
section: "layouts"
category: "css-hero-sections"
category_name: "CSS Hero Sections"
description: "Pure-CSS starfield — dots positioned via radial-gradient on a deep-navy backdrop. Electric yellow accent and dim white copy. No canvas, no per-particle DOM."
has_js: "false"
---

Here's a working CSS Hero Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Particle Starfield
Source: https://codefronts.com/layouts/css-hero-sections/particle-starfield/

Pure-CSS starfield — dots positioned via radial-gradient on a deep-navy backdrop. Electric yellow accent and dim white copy. No canvas, no per-particle DOM.
## HTML
```html
<section class="hs-28" aria-label="Hero">
  <div class="hs-28__stars" aria-hidden="true"></div>
  <div class="hs-28__stars hs-28__stars-2" aria-hidden="true"></div>
  <div class="hs-28__inner">
    <span class="hs-28__eye">★ NIGHT SKY ATLAS</span>
    <h2>Every constellation, <em>over your back yard tonight.</em></h2>
    <p>
      Point your phone up. We'll tell you which star is where, why it has that name, and when to
      look again.
    </p>
    <a class="hs-28__cta" href="#download">Get the atlas</a>
  </div>
</section>
```
## CSS
```css
.hs-28 {
  position: relative;
  overflow: hidden;
  display: grid;
  place-items: center;
  width: 100%;
  min-height: 100vh;
  padding: clamp(28px, 5vw, 64px) clamp(20px, 5vw, 56px);
  background: radial-gradient(ellipse at 50% 100%, rgba(248,210,72,0.16), transparent 70%), linear-gradient(180deg, #050a1a 0%, #0a1428 60%, #1a2840 100%);
  font-family: 'Inter', system-ui, sans-serif;
  color: #f0eee0;
  box-sizing: border-box;
  contain: layout paint;
}

.hs-28__stars {
  position: absolute;
  inset: 0;
  background-image: radial-gradient(1px 1px at 12% 8%, #fff, transparent), radial-gradient(1px 1px at 28% 24%, #f8d248, transparent), radial-gradient(1.5px 1.5px at 44% 12%, #fff, transparent), radial-gradient(1px 1px at 60% 30%, #fff, transparent), radial-gradient(2px 2px at 78% 18%, #f8d248, transparent), radial-gradient(1px 1px at 90% 32%, #fff, transparent), radial-gradient(1px 1px at 18% 48%, #fff, transparent), radial-gradient(1.5px 1.5px at 35% 64%, #fff, transparent), radial-gradient(1px 1px at 52% 52%, #f8d248, transparent), radial-gradient(2px 2px at 70% 76%, #fff, transparent), radial-gradient(1px 1px at 84% 60%, #fff, transparent), radial-gradient(1.5px 1.5px at 8% 80%, #fff, transparent), radial-gradient(1px 1px at 96% 88%, #fff, transparent);
  background-size: 100% 100%;
  animation: hs-28-twinkle 4s ease-in-out infinite alternate;
}

.hs-28__stars-2 {
  background-image: radial-gradient(1px 1px at 22% 14%, rgba(255,255,255,0.5), transparent), radial-gradient(1px 1px at 48% 30%, rgba(248,210,72,0.5), transparent), radial-gradient(1px 1px at 66% 8%, rgba(255,255,255,0.5), transparent), radial-gradient(1px 1px at 84% 44%, rgba(255,255,255,0.5), transparent), radial-gradient(1px 1px at 14% 62%, rgba(255,255,255,0.5), transparent), radial-gradient(1px 1px at 76% 88%, rgba(255,255,255,0.5), transparent);
  animation-delay: -2s;
}

@keyframes hs-28-twinkle {
  from {
    opacity: 0.5;
  }

  to {
    opacity: 1;
  }
}

.hs-28__inner {
  position: relative;
  z-index: 1;
  max-width: 640px;
  text-align: center;
}

.hs-28__eye {
  display: inline-block;
  font-family: 'JetBrains Mono', monospace;
  font-size: 11.5px;
  letter-spacing: 0.24em;
  color: #f8d248;
  margin-bottom: 22px;
}

.hs-28 h2 {
  margin: 0 0 16px;
  font-family: 'Playfair Display', Georgia, serif;
  font-size: clamp(34px, 5vw, 56px);
  font-weight: 700;
  letter-spacing: -0.02em;
  line-height: 1.05;
  color: #f0eee0;
}

.hs-28 h2 em {
  color: #f8d248;
  font-style: italic;
}

.hs-28 p {
  margin: 0 auto 26px;
  font-size: 16px;
  line-height: 1.55;
  color: #b8b0a0;
  max-width: 460px;
}

.hs-28__cta {
  display: inline-block;
  padding: 13px 26px;
  background: #f8d248;
  color: #050a1a;
  border-radius: 0;
  text-decoration: none;
  font-weight: 800;
  font-size: 14.5px;
  letter-spacing: 0.04em;
  transition: background 0.15s;
}

.hs-28__cta:hover {
  background: #fff;
}

@media (prefers-reduced-motion: reduce) {
  .hs-28__stars {
    animation: none;
  }

  .hs-28__cta {
    transition: none;
  }
}
```
