---
source: "codefronts"
url: "https://codefronts.com/layouts/css-hero-sections/conic-orbit-hero/"
title: "Conic Orbit Hero"
section: "layouts"
category: "css-hero-sections"
category_name: "CSS Hero Sections"
description: "Solar-corona conic gradient ring orbits the headline using @property animatable angle."
has_js: "false"
---

Here's a working CSS Hero Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Conic Orbit Hero
Source: https://codefronts.com/layouts/css-hero-sections/conic-orbit-hero/

Solar-corona conic gradient ring orbits the headline using @property animatable angle. Gold and ember orange on jet black — the AI / launch treatment with a stellar feel.
## HTML
```html
<section class="hs-30" aria-label="Hero">
  <div class="hs-30__stage">
    <div class="hs-30__ring" aria-hidden="true"></div>
    <div class="hs-30__core" aria-hidden="true"></div>
  </div>
  <div class="hs-30__inner">
    <span class="hs-30__eye">solar v3</span>
    <h2>Compute that <em>moves at the speed of light.</em></h2>
    <p>The new generation of inference cards. 3× the throughput. Half the heat.</p>
    <a class="hs-30__cta" href="#preorder">Pre-order →</a>
  </div>
</section>
```
## CSS
```css
@property --hs-30__a {
  syntax: '<angle>';
  initial-value: 0deg;
  inherits: false;
}

.hs-30 {
  position: relative;
  overflow: hidden;
  display: grid;
  grid-template-columns: 1fr 1fr;
  width: 100%;
  min-height: 100vh;
  padding: clamp(28px, 5vw, 56px);
  gap: clamp(24px, 4vw, 56px);
  align-items: center;
  background: #0a0805;
  font-family: 'Inter', system-ui, sans-serif;
  color: #f8e8c8;
  box-sizing: border-box;
}

.hs-30__stage {
  position: relative;
  height: 100%;
  min-height: 320px;
  display: grid;
  place-items: center;
}

.hs-30__ring {
  width: 320px;
  height: 320px;
  border-radius: 50%;
  background: conic-gradient(from var(--hs-30__a),
        #f8d248, #ff6b1a, #d63a18, #ff6b1a, #f8d248);
  filter: blur(8px);
  animation: hs-30-spin 12s linear infinite;
  -webkit-mask: radial-gradient(circle, transparent 96px, #000 100px, #000 158px, transparent 162px);
  mask: radial-gradient(circle, transparent 96px, #000 100px, #000 158px, transparent 162px);
}

.hs-30__core {
  position: absolute;
  width: 200px;
  height: 200px;
  border-radius: 50%;
  background: radial-gradient(circle, #ff6b1a 0%, #d63a18 50%, #6b1a08 100%);
  box-shadow: 0 0 80px rgba(255,107,26,0.4);
}

@keyframes hs-30-spin {
  to {
    --hs-30__a: 360deg;
  }
}

.hs-30__inner {
  position: relative;
  z-index: 1;
}

.hs-30__eye {
  display: inline-block;
  font-family: 'JetBrains Mono', monospace;
  font-size: 11.5px;
  letter-spacing: 0.16em;
  color: #f8d248;
  padding: 4px 12px;
  background: rgba(248,210,72,0.12);
  border: 1px solid rgba(248,210,72,0.4);
  border-radius: 999px;
  margin-bottom: 18px;
}

.hs-30 h2 {
  margin: 0 0 16px;
  font-size: clamp(28px, 4vw, 44px);
  font-weight: 800;
  letter-spacing: -0.025em;
  line-height: 1.1;
  color: #f8e8c8;
  word-wrap: break-word;
}

.hs-30 h2 em {
  background: linear-gradient(90deg, #f8d248, #ff6b1a);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  font-style: italic;
  display: inline-block;
}

.hs-30 p {
  margin: 0 0 26px;
  font-size: 16px;
  line-height: 1.55;
  color: #b89878;
  max-width: 420px;
}

.hs-30__cta {
  display: inline-block;
  padding: 13px 26px;
  background: linear-gradient(135deg, #ff6b1a, #d63a18);
  color: #0a0805;
  border-radius: 999px;
  text-decoration: none;
  font-weight: 800;
  font-size: 14.5px;
  box-shadow: 0 14px 36px rgba(255,107,26,0.35);
  transition: transform 0.15s;
}

.hs-30__cta:hover {
  transform: translateY(-1px);
}

@media (max-width: 720px) {
  .hs-30 {
    grid-template-columns: 1fr;
  }

  .hs-30__ring,
    .hs-30__core {
    width: 200px;
    height: 200px;
  }

  .hs-30__core {
    width: 130px;
    height: 130px;
  }

  .hs-30__ring {
    -webkit-mask: radial-gradient(circle, transparent 60px, #000 64px, #000 98px, transparent 102px);
    mask: radial-gradient(circle, transparent 60px, #000 64px, #000 98px, transparent 102px);
  }
}

@media (prefers-reduced-motion: reduce) {
  .hs-30__ring {
    animation: none;
  }

  .hs-30__cta {
    transition: none;
  }
}
```
