---
source: "codefronts"
url: "https://codefronts.com/layouts/css-hero-sections/gradient-mesh/"
title: "Gradient Mesh"
section: "layouts"
category: "css-hero-sections"
category_name: "CSS Hero Sections"
description: "Tropical mesh gradient — overlapping radial blobs in mango, papaya, and dragon fruit on a warm coral base."
has_js: "false"
---

Here's a working CSS Hero Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Gradient Mesh
Source: https://codefronts.com/layouts/css-hero-sections/gradient-mesh/

Tropical mesh gradient — overlapping radial blobs in mango, papaya, and dragon fruit on a warm coral base. The Stripe / Linear gradient hero, but turned up to a sunset.
## HTML
```html
<section class="hs-03" aria-label="Hero">
  <div class="hs-03__blobs" aria-hidden="true">
    <span></span><span></span><span></span><span></span>
  </div>
  <div class="hs-03__inner">
    <span class="hs-03__eye">launch · summer collection</span>
    <h2>Make your weekends <em>feel like vacation.</em></h2>
    <p>
      The mood-board planner that turns scattered Pinterest tabs into the trip you actually take.
    </p>
    <a class="hs-03__cta" href="#start">Plan a trip →</a>
  </div>
</section>
```
## CSS
```css
.hs-03 {
  position: relative;
  overflow: hidden;
  display: grid;
  place-items: center;
  width: 100%;
  min-height: 100vh;
  padding: clamp(32px, 6vw, 80px) clamp(20px, 5vw, 56px);
  background: #ff5e62;
  font-family: 'Inter', system-ui, sans-serif;
  color: #fff;
  box-sizing: border-box;
  contain: layout paint;
}

.hs-03__blobs {
  position: absolute;
  inset: 0;
}

.hs-03__blobs span {
  position: absolute;
  border-radius: 50%;
  filter: blur(60px);
  animation: hs-03-drift 16s ease-in-out infinite alternate;
}

.hs-03__blobs span:nth-child(1) {
  top: -10%;
  left: 10%;
  width: 460px;
  height: 460px;
  background: radial-gradient(circle, #ffd23f 0%, transparent 70%);
}

.hs-03__blobs span:nth-child(2) {
  top: 20%;
  right: 0;
  width: 420px;
  height: 420px;
  background: radial-gradient(circle, #ee4266 0%, transparent 70%);
  animation-delay: -4s;
}

.hs-03__blobs span:nth-child(3) {
  bottom: 0;
  left: 30%;
  width: 460px;
  height: 460px;
  background: radial-gradient(circle, #ff7e5f 0%, transparent 70%);
  animation-delay: -8s;
}

.hs-03__blobs span:nth-child(4) {
  top: 30%;
  left: -8%;
  width: 360px;
  height: 360px;
  background: radial-gradient(circle, #ffa552 0%, transparent 70%);
  animation-delay: -12s;
}

@keyframes hs-03-drift {
  0% {
    transform: translate(0,0) scale(1);
  }

  50% {
    transform: translate(40px,-30px) scale(1.08);
  }

  100% {
    transform: translate(-40px,40px) scale(0.96);
  }
}

.hs-03__inner {
  position: relative;
  z-index: 1;
  max-width: 640px;
  text-align: center;
}

.hs-03__eye {
  display: inline-block;
  padding: 5px 14px;
  background: rgba(255,255,255,0.18);
  border: 1px solid rgba(255,255,255,0.4);
  border-radius: 999px;
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  margin-bottom: 22px;
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
}

.hs-03 h2 {
  margin: 0 0 18px;
  font-size: clamp(34px, 6vw, 60px);
  font-weight: 900;
  letter-spacing: -0.025em;
  line-height: 1.02;
  text-shadow: 0 2px 24px rgba(238,66,102,0.25);
}

.hs-03 h2 em {
  font-style: italic;
  font-weight: 800;
  color: #fff5d2;
}

.hs-03 p {
  margin: 0 auto 28px;
  font-size: 17px;
  line-height: 1.55;
  max-width: 480px;
  opacity: 0.95;
}

.hs-03__cta {
  display: inline-block;
  padding: 14px 26px;
  background: #fff;
  color: #ee4266;
  border-radius: 999px;
  text-decoration: none;
  font-weight: 700;
  font-size: 15px;
  box-shadow: 0 12px 30px rgba(238,66,102,0.35);
  transition: transform 0.18s;
}

.hs-03__cta:hover {
  transform: translateY(-2px);
}

@media (prefers-reduced-motion: reduce) {
  .hs-03__blobs span {
    animation: none;
  }

  .hs-03__cta {
    transition: none;
  }
}
```
