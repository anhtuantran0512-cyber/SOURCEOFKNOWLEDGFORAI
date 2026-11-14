---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-gradient-text/css-liquid-mercury-metallic-gradient-text/"
title: "CSS Liquid Mercury Metallic Gradient Text"
section: "design-styles"
category: "css-gradient-text"
category_name: "CSS Gradient Text Designs"
description: "A cool blue-grey metallic gradient with rippling background-position animation and teardrop orbs below the headline evoke the look of flowing liquid mercury."
has_js: "false"
---

Here's a working CSS Gradient Text Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Liquid Mercury Metallic Gradient Text
Source: https://codefronts.com/design-styles/css-gradient-text/css-liquid-mercury-metallic-gradient-text/

A cool blue-grey metallic gradient with rippling background-position animation and teardrop orbs below the headline evoke the look of flowing liquid mercury.
## HTML
```html
<div class="gt-12">
  <span class="gt-12__label">liquid mercury gradient</span>
  <div class="gt-12__mercury">MERCURY</div>
  <div class="gt-12__drops">
    <div class="gt-12__drop"></div>
    <div class="gt-12__drop"></div>
    <div class="gt-12__drop"></div>
    <div class="gt-12__drop"></div>
  </div>
  <p class="gt-12__sub">reflective metallic shimmer</p>
</div>
```
## CSS
```css
.gt-12,
.gt-12 *,
.gt-12 *::before,
.gt-12 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.gt-12 {
  --bg: #080808;
  --m1: #c8d8e8;
  --m2: #e8eff8;
  --m3: #8090a0;
  --m4: #404858;
  font-family: 'Bebas Neue', sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 3rem;
  padding: 3rem 2rem;
}

.gt-12__label {
  font-family: 'Space Mono', monospace;
  font-size: .6rem;
  letter-spacing: .3em;
  text-transform: uppercase;
  color: #2a3040;
}

.gt-12__mercury {
  font-size: clamp(4rem, 15vw, 10rem);
  line-height: 1;
  letter-spacing: .1em;
  background: linear-gradient(180deg,
      var(--m2) 0%,
      var(--m1) 20%,
      var(--m3) 35%,
      var(--m2) 50%,
      var(--m4) 65%,
      var(--m1) 80%,
      var(--m3) 100%
    );
  background-size: 100% 300%;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: gt-12-liquid 4s ease-in-out infinite;
  filter: drop-shadow(0 4px 12px rgba(200,216,232,.15));
}

.gt-12__drops {
  display: flex;
  gap: .8rem;
  align-items: center;
}

.gt-12__drop {
  border-radius: 50% 50% 50% 50% / 60% 60% 40% 40%;
  background: linear-gradient(180deg, var(--m2), var(--m3));
  animation: gt-12-drip 2.5s ease-in-out infinite;
  filter: drop-shadow(0 2px 6px rgba(200,216,232,.2));
}

.gt-12__drop:nth-child(1) {
  width: 14px;
  height: 18px;
  animation-delay: 0s;
}

.gt-12__drop:nth-child(2) {
  width: 22px;
  height: 28px;
  animation-delay: -.5s;
}

.gt-12__drop:nth-child(3) {
  width: 18px;
  height: 22px;
  animation-delay: -1s;
}

.gt-12__drop:nth-child(4) {
  width: 14px;
  height: 18px;
  animation-delay: -1.5s;
}

.gt-12__sub {
  font-family: 'Space Mono', monospace;
  font-size: clamp(.7rem, 2vw, .9rem);
  letter-spacing: .2em;
  background: linear-gradient(90deg, var(--m3), var(--m2), var(--m3));
  background-size: 200% 100%;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: gt-12-flow 5s linear infinite;
}

@keyframes gt-12-liquid {
  0%,
    100% {
    background-position: center 0%;
  }

  50% {
    background-position: center 100%;
  }
}

@keyframes gt-12-drip {
  0%,
    100% {
    transform: scaleY(1) translateY(0);
  }

  50% {
    transform: scaleY(1.2) translateY(4px);
  }
}

@keyframes gt-12-flow {
  0% {
    background-position: 0% center;
  }

  100% {
    background-position: 200% center;
  }
}

@media (prefers-reduced-motion: reduce) {
  .gt-12__mercury,
    .gt-12__drop,
    .gt-12__sub {
    animation: none;
  }
}
```
