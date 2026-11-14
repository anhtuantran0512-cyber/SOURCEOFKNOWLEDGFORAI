---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-gradient-text/css-holographic-foil-iridescent-gradient-text/"
title: "CSS Holographic Foil Iridescent Gradient Text"
section: "design-styles"
category: "css-gradient-text"
category_name: "CSS Gradient Text Designs"
description: "A dense multi-stop rainbow gradient animating diagonally across text and card surfaces recreates the colour-shifting prismatic effect of holographic foil…"
has_js: "false"
---

Here's a working CSS Gradient Text Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Holographic Foil Iridescent Gradient Text
Source: https://codefronts.com/design-styles/css-gradient-text/css-holographic-foil-iridescent-gradient-text/

A dense multi-stop rainbow gradient animating diagonally across text and card surfaces recreates the colour-shifting prismatic effect of holographic foil stickers.
## HTML
```html
<div class="gt-09">
  <span class="gt-09__label">Holographic foil gradient</span>
  <h1 class="gt-09__holo">HOLOFX</h1>
  <p class="gt-09__sub">Prismatic iridescent text</p>
  <div class="gt-09__cards">
    <div class="gt-09__card">
      <span class="gt-09__card-text">SHIMMER</span>
    </div>
    <div class="gt-09__card">
      <span class="gt-09__card-text">GLIMMER</span>
    </div>
    <div class="gt-09__card">
      <span class="gt-09__card-text">REFLECT</span>
    </div>
  </div>
</div>
```
## CSS
```css
.gt-09,
.gt-09 *,
.gt-09 *::before,
.gt-09 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.gt-09 {
  --bg: #0a0a12;
  font-family: 'Outfit', sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 3rem;
  padding: 3rem 2rem;
}

.gt-09__label {
  font-size: .7rem;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: #333;
}

.gt-09__holo {
  font-size: clamp(3rem, 12vw, 8rem);
  font-weight: 900;
  line-height: 1;
  letter-spacing: .05em;
  background: linear-gradient(
      135deg,
      #ff0080 0%,
      #ff8c00 10%,
      #ffe100 20%,
      #40ff00 30%,
      #00cfff 40%,
      #8000ff 50%,
      #ff0080 60%,
      #ff8c00 70%,
      #ffe100 80%,
      #40ff00 90%,
      #00cfff 100%
    );
  background-size: 300% 300%;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: gt-09-holo 4s ease infinite;
  filter: drop-shadow(0 2px 20px rgba(255,0,128,.3));
}

.gt-09__sub {
  font-size: clamp(1rem, 3vw, 1.5rem);
  font-weight: 800;
  background: linear-gradient(90deg,
      #00cfff, #8000ff, #ff0080, #ff8c00, #ffe100
    );
  background-size: 200% 100%;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: gt-09-scroll 3s linear infinite;
  letter-spacing: .12em;
}

.gt-09__cards {
  display: flex;
  gap: 1.5rem;
  flex-wrap: wrap;
  justify-content: center;
}

.gt-09__card {
  padding: 1.5rem 2rem;
  border-radius: 12px;
  background: linear-gradient(135deg, #ffffff08, #ffffff03);
  border: 1px solid #ffffff15;
  backdrop-filter: blur(8px);
  position: relative;
  overflow: hidden;
}

.gt-09__card::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg,
      #ff008020, #00cfff20, #8000ff20
    );
  background-size: 200% 200%;
  animation: gt-09-holo 6s ease infinite;
  border-radius: 12px;
}

.gt-09__card-text {
  font-size: 1.3rem;
  font-weight: 900;
  position: relative;
  background: linear-gradient(135deg, #ff0080, #00cfff, #8000ff, #ff0080);
  background-size: 200% 200%;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: gt-09-holo 3s ease infinite;
}

.gt-09__card:nth-child(2) .gt-09__card-text {
  animation-delay: -.7s;
}

.gt-09__card:nth-child(3) .gt-09__card-text {
  animation-delay: -1.4s;
}

@keyframes gt-09-holo {
  0% {
    background-position: 0% 0%;
  }

  50% {
    background-position: 100% 100%;
  }

  100% {
    background-position: 0% 0%;
  }
}

@keyframes gt-09-scroll {
  0% {
    background-position: 0% center;
  }

  100% {
    background-position: 200% center;
  }
}

@media (prefers-reduced-motion: reduce) {
  .gt-09__holo,
    .gt-09__sub,
    .gt-09__card-text,
    .gt-09__card::before {
    animation: none;
  }
}
```
