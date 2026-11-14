---
source: "codefronts"
url: "https://codefronts.com/motion/css-card-hover-effects/frosted-glass-intensify/"
title: "Frosted Glass Intensify"
section: "motion"
category: "css-card-hover-effects"
category_name: "CSS Card Hover Effects"
description: "A weather-widget card over a vivid color backdrop whose backdrop-filter blur deepens on hover, melting the colors behind the glass."
has_js: "false"
---

Here's a working CSS Card Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Frosted Glass Intensify
Source: https://codefronts.com/motion/css-card-hover-effects/frosted-glass-intensify/

A weather-widget card over a vivid color backdrop whose backdrop-filter blur deepens on hover, melting the colors behind the glass. Ideal for dashboards, weather/utility widgets, and modern glassmorphism interfaces.
## HTML
```html
<div class="card-27">
  <article class="card-27__card">
    <div class="card-27__inner">
      <span class="card-27__pill">Weather · Now</span>
      <h2 class="card-27__title">Coastal<br>Forecast</h2>
      <p class="card-27__desc">A glass widget over a living wallpaper. Hover and the frost thickens, melting the color behind it.</p>
      <div class="card-27__foot">
        <span>Light fog · breezy</span>
        <b>18°</b>
      </div>
    </div>
  </article>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;500;800&display=swap');

.card-27,
.card-27 *,
.card-27 *::before,
.card-27 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.card-27 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  background: radial-gradient(circle at 20% 30%, #ff5ea0 0 22%, transparent 23%), radial-gradient(circle at 75% 25%, #ffd23f 0 18%, transparent 19%), radial-gradient(circle at 60% 80%, #2bd9c4 0 26%, transparent 27%), radial-gradient(circle at 30% 75%, #6a5cff 0 20%, transparent 21%), #1a0f2e;
  font-family: 'Hanken Grotesk', sans-serif;
  padding: 2rem;
}

.card-27__card {
  position: relative;
  width: 340px;
  height: 440px;
  border-radius: 26px;
  cursor: pointer;
  overflow: hidden;
  background: rgba(255,255,255,0.08);
  border: 1px solid rgba(255,255,255,0.22);
  -webkit-backdrop-filter: blur(4px) saturate(1.1);
  backdrop-filter: blur(4px) saturate(1.1);
  box-shadow: 0 18px 50px rgba(0,0,0,0.3);
  transition: backdrop-filter 0.5s ease, -webkit-backdrop-filter 0.5s ease, background 0.5s ease, border-color 0.5s ease, transform 0.4s ease;
}

.card-27__card:hover {
  -webkit-backdrop-filter: blur(22px) saturate(1.6);
  backdrop-filter: blur(22px) saturate(1.6);
  background: rgba(255,255,255,0.16);
  border-color: rgba(255,255,255,0.4);
  transform: translateY(-6px);
}

.card-27__card::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 45%;
  background: linear-gradient(rgba(255,255,255,0.25), transparent);
  opacity: 0.5;
}

.card-27__inner {
  position: relative;
  z-index: 2;
  height: 100%;
  padding: 2.4rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  color: #fff;
}

.card-27__pill {
  align-self: flex-start;
  font-size: 0.7rem;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  padding: 0.4rem 0.9rem;
  border-radius: 999px;
  background: rgba(255,255,255,0.2);
  border: 1px solid rgba(255,255,255,0.3);
}

.card-27__title {
  font-weight: 800;
  font-size: 2.5rem;
  line-height: 1;
  text-shadow: 0 2px 20px rgba(0,0,0,0.2);
}

.card-27__desc {
  font-size: 0.88rem;
  line-height: 1.6;
  color: rgba(255,255,255,0.92);
}

.card-27__foot {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.8rem;
}

.card-27__foot b {
  font-size: 1.5rem;
  font-weight: 800;
}

@media (prefers-reduced-motion: reduce) {
  .card-27__card {
    transition: none !important;
  }
}
```
