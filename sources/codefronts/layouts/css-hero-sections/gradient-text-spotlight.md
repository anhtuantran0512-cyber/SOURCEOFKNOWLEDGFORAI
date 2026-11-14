---
source: "codefronts"
url: "https://codefronts.com/layouts/css-hero-sections/gradient-text-spotlight/"
title: "Gradient Text Spotlight"
section: "layouts"
category: "css-hero-sections"
category_name: "CSS Hero Sections"
description: "Oversized headline with an animated marigold → ruby → grape gradient sweeping across the letters. The Linear / Apple wordmark shimmer treatment."
has_js: "false"
---

Here's a working CSS Hero Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Gradient Text Spotlight
Source: https://codefronts.com/layouts/css-hero-sections/gradient-text-spotlight/

Oversized headline with an animated marigold → ruby → grape gradient sweeping across the letters. The Linear / Apple wordmark shimmer treatment.
## HTML
```html
<section class="hs-20" aria-label="Hero">
  <div class="hs-20__inner">
    <span class="hs-20__eye">v3 launching tuesday</span>
    <h2>Made for the way <span class="hs-20__shine">creative people</span> actually work.</h2>
    <p>One canvas. Every layer. Zero exporting between apps to nudge a kerning pair.</p>
    <a class="hs-20__cta" href="#waitlist">Join the waitlist →</a>
  </div>
</section>
```
## CSS
```css
.hs-20 {
  display: grid;
  place-items: center;
  width: 100%;
  min-height: 100vh;
  padding: clamp(28px, 5vw, 64px) clamp(20px, 5vw, 56px);
  background: radial-gradient(60% 60% at 50% 0%, rgba(120,30,90,0.18), transparent 70%), #1a0d20;
  font-family: 'Inter', system-ui, sans-serif;
  color: #f4e8d0;
  box-sizing: border-box;
}

.hs-20__inner {
  max-width: 720px;
  text-align: center;
}

.hs-20__eye {
  display: inline-block;
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  letter-spacing: 0.16em;
  color: #f5b148;
  padding: 4px 10px;
  border: 1px solid rgba(245,177,72,0.4);
  border-radius: 999px;
  margin-bottom: 22px;
}

.hs-20 h2 {
  margin: 0 0 18px;
  font-size: clamp(38px, 6vw, 68px);
  font-weight: 800;
  letter-spacing: -0.025em;
  line-height: 1.05;
}

.hs-20__shine {
  display: inline-block;
  background: linear-gradient(90deg, #f5b148, #d63a5e, #7e2d8a, #f5b148);
  background-size: 200% 100%;
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  animation: hs-20-sweep 4s linear infinite;
}

@keyframes hs-20-sweep {
  to {
    background-position: 200% 0;
  }
}

.hs-20 p {
  margin: 0 auto 26px;
  font-size: 17px;
  line-height: 1.55;
  color: #b8a890;
  max-width: 460px;
}

.hs-20__cta {
  display: inline-block;
  padding: 13px 26px;
  background: linear-gradient(90deg, #f5b148, #d63a5e);
  color: #1a0d20;
  border-radius: 999px;
  text-decoration: none;
  font-weight: 700;
  font-size: 14.5px;
  box-shadow: 0 12px 30px rgba(214,58,94,0.35);
  transition: transform 0.15s;
}

.hs-20__cta:hover {
  transform: translateY(-1px);
}

@media (prefers-reduced-motion: reduce) {
  .hs-20__shine {
    animation: none;
    background-position: 0 0;
  }

  .hs-20__cta {
    transition: none;
  }
}
```
