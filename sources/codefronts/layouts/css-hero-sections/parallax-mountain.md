---
source: "codefronts"
url: "https://codefronts.com/layouts/css-hero-sections/parallax-mountain/"
title: "Parallax Mountain"
section: "layouts"
category: "css-hero-sections"
category_name: "CSS Hero Sections"
description: "Layered SVG mountain silhouettes drift at different speeds — glacier blue and pine on alpine snow. The outdoor / travel-brand parallax landscape."
has_js: "false"
---

Here's a working CSS Hero Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Parallax Mountain
Source: https://codefronts.com/layouts/css-hero-sections/parallax-mountain/

Layered SVG mountain silhouettes drift at different speeds — glacier blue and pine on alpine snow. The outdoor / travel-brand parallax landscape.
## HTML
```html
<section class="hs-25" aria-label="Hero">
  <div class="hs-25__sky" aria-hidden="true"></div>
  <div class="hs-25__sun" aria-hidden="true"></div>
  <svg
    class="hs-25__m hs-25__m3"
    viewBox="0 0 1200 320"
    preserveAspectRatio="none"
    aria-hidden="true"
  >
    <path
      d="M0,320 L0,180 L120,80 L240,140 L360,60 L480,120 L600,40 L720,110 L840,70 L960,130 L1080,90 L1200,150 L1200,320 Z"
      fill="#5a7a8a"
    />
  </svg>
  <svg
    class="hs-25__m hs-25__m2"
    viewBox="0 0 1200 320"
    preserveAspectRatio="none"
    aria-hidden="true"
  >
    <path
      d="M0,320 L0,220 L100,140 L200,200 L320,120 L440,180 L560,100 L680,170 L800,130 L920,200 L1040,150 L1200,200 L1200,320 Z"
      fill="#3a5868"
    />
  </svg>
  <svg
    class="hs-25__m hs-25__m1"
    viewBox="0 0 1200 320"
    preserveAspectRatio="none"
    aria-hidden="true"
  >
    <path
      d="M0,320 L0,260 L120,200 L240,240 L360,180 L480,220 L600,160 L720,210 L840,170 L960,230 L1080,190 L1200,240 L1200,320 Z"
      fill="#1f3a4a"
    />
  </svg>
  <div class="hs-25__inner">
    <span class="hs-25__eye">— EST. 1958 · LAKE COUNTRY</span>
    <h2>Trails that <em>earn the silence.</em></h2>
    <p>Six lodges. One ridge. The mountains your grandfather wrote home about.</p>
    <a class="hs-25__cta" href="#book">Reserve a cabin →</a>
  </div>
</section>
```
## CSS
```css
.hs-25 {
  position: relative;
  overflow: hidden;
  width: 100%;
  min-height: 100vh;
  background: linear-gradient(180deg, #d8e8f0 0%, #a8c8d8 60%, #5a7a8a 100%);
  font-family: 'Inter', system-ui, sans-serif;
  color: #1a2840;
  box-sizing: border-box;
  contain: layout paint;
}

.hs-25__sky {
  position: absolute;
  inset: 0;
  background: radial-gradient(50% 70% at 80% 30%, rgba(255,240,210,0.4), transparent 70%);
}

.hs-25__sun {
  position: absolute;
  top: 18%;
  right: 18%;
  width: 80px;
  height: 80px;
  border-radius: 50%;
  background: #f9f0d6;
  box-shadow: 0 0 60px rgba(249,240,214,0.7);
}

.hs-25__m {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  width: 100%;
  height: 60%;
  animation: hs-25-float 12s ease-in-out infinite alternate;
}

.hs-25__m1 {
  z-index: 3;
  height: 38%;
  animation-duration: 8s;
}

.hs-25__m2 {
  z-index: 2;
  height: 50%;
  animation-duration: 12s;
  animation-delay: -2s;
}

.hs-25__m3 {
  z-index: 1;
  height: 65%;
  animation-duration: 16s;
  animation-delay: -4s;
}

@keyframes hs-25-float {
  0% {
    transform: translateX(0);
  }

  100% {
    transform: translateX(-2%);
  }
}

.hs-25__inner {
  position: relative;
  z-index: 4;
  padding: clamp(28px, 5vw, 56px);
  max-width: 540px;
}

.hs-25__eye {
  display: inline-block;
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  letter-spacing: 0.18em;
  color: #1f3a4a;
  margin-bottom: 14px;
}

.hs-25 h2 {
  margin: 0 0 16px;
  font-family: 'Playfair Display', Georgia, serif;
  font-size: clamp(34px, 5vw, 56px);
  font-weight: 700;
  letter-spacing: -0.02em;
  line-height: 1.05;
  color: #0d2030;
}

.hs-25 h2 em {
  color: #1f3a4a;
  font-style: italic;
}

.hs-25 p {
  margin: 0 0 22px;
  font-size: 16px;
  line-height: 1.55;
  color: #2a4858;
  max-width: 420px;
}

.hs-25__cta {
  display: inline-block;
  padding: 12px 22px;
  background: #f9f0d6;
  color: #1f3a4a;
  border: 2px solid #1f3a4a;
  border-radius: 0;
  font-family: 'JetBrains Mono', monospace;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-decoration: none;
  transition: background 0.15s, color 0.15s;
}

.hs-25__cta:hover {
  background: #1f3a4a;
  color: #f9f0d6;
}

@media (prefers-reduced-motion: reduce) {
  .hs-25__m {
    animation: none;
  }

  .hs-25__cta {
    transition: none;
  }
}
```
