---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-gradient-text/css-glitter-sparkle-gradient-text-effect/"
title: "CSS Glitter Sparkle Gradient Text Effect"
section: "design-styles"
category: "css-gradient-text"
category_name: "CSS Gradient Text Designs"
description: "Gold-pink-violet gradient text paired with animating spark particles via absolute-positioned siblings and staggered scale/opacity keyframes recreates the…"
has_js: "false"
---

Here's a working CSS Gradient Text Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Glitter Sparkle Gradient Text Effect
Source: https://codefronts.com/design-styles/css-gradient-text/css-glitter-sparkle-gradient-text-effect/

Gold-pink-violet gradient text paired with animating spark particles via absolute-positioned siblings and staggered scale/opacity keyframes recreates the glitter foil aesthetic.
## HTML
```html
<div class="gt-19">
  <span class="gt-19__label">Glitter sparkle gradient</span>
  <div style="position:relative; display:inline-block;">
    <div class="gt-19__glitter">SPARKLE</div>
    <div class="gt-19__sparks">
      <div class="gt-19__spark"></div>
      <div class="gt-19__spark"></div>
      <div class="gt-19__spark"></div>
      <div class="gt-19__spark"></div>
      <div class="gt-19__spark"></div>
      <div class="gt-19__spark"></div>
      <div class="gt-19__spark"></div>
      <div class="gt-19__spark"></div>
      <div class="gt-19__spark"></div>
      <div class="gt-19__spark"></div>
    </div>
  </div>
  <p class="gt-19__sub">GLITTER · SHIMMER · GLOW</p>
  <div class="gt-19__row">
    <span class="gt-19__gem">✦ GOLD ✦</span>
    <span class="gt-19__gem">✦ PINK ✦</span>
    <span class="gt-19__gem">✦ VIOLET ✦</span>
  </div>
</div>
```
## CSS
```css
.gt-19,
.gt-19 *,
.gt-19 *::before,
.gt-19 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.gt-19 {
  --bg: #0d0015;
  --g1: #ffd700;
  --g2: #ff69b4;
  --g3: #da70d6;
  --g4: #ff6347;
  font-family: 'Paytone One', sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 3rem;
  padding: 3rem 2rem;
  position: relative;
  overflow: hidden;
}

.gt-19__label {
  font-size: .7rem;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: #3a1040;
  font-family: monospace;
}

.gt-19__glitter {
  font-size: clamp(3rem, 12vw, 8rem);
  line-height: 1;
  letter-spacing: .04em;
  position: relative;
  display: inline-block;
  background: linear-gradient(135deg,
      var(--g1) 0%, var(--g2) 25%,
      var(--g3) 50%, var(--g4) 75%, var(--g1) 100%
    );
  background-size: 200% 200%;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: gt-19-glitter 3s ease-in-out infinite;
  filter: drop-shadow(0 0 6px #ffd70060) drop-shadow(0 0 20px #ff69b440);
}
/* Sparkle particles via pseudo elements on sibling spans */

.gt-19__sparks {
  position: absolute;
  inset: 0;
  pointer-events: none;
}

.gt-19__spark {
  position: absolute;
  width: 4px;
  height: 4px;
  border-radius: 50%;
  background: radial-gradient(circle, #fff 40%, #ffd70060 100%);
  animation: gt-19-spark 2s ease-in-out infinite;
}
/* Position sparks around the text area */

.gt-19__spark:nth-child(1) {
  top: 10%;
  left: 5%;
  animation-delay: 0s;
  width: 6px;
  height: 6px;
}

.gt-19__spark:nth-child(2) {
  top: 20%;
  left: 80%;
  animation-delay: -.4s;
}

.gt-19__spark:nth-child(3) {
  top: 70%;
  left: 15%;
  animation-delay: -.8s;
  width: 5px;
  height: 5px;
}

.gt-19__spark:nth-child(4) {
  top: 80%;
  left: 90%;
  animation-delay: -1.2s;
}

.gt-19__spark:nth-child(5) {
  top: 40%;
  left: 95%;
  animation-delay: -1.6s;
  width: 3px;
  height: 3px;
}

.gt-19__spark:nth-child(6) {
  top: 50%;
  left: 2%;
  animation-delay: -0.2s;
}

.gt-19__spark:nth-child(7) {
  top: 5%;
  left: 50%;
  animation-delay: -0.6s;
  width: 5px;
  height: 5px;
}

.gt-19__spark:nth-child(8) {
  top: 90%;
  left: 50%;
  animation-delay: -1s;
}

.gt-19__spark:nth-child(9) {
  top: 30%;
  left: 30%;
  animation-delay: -1.4s;
  width: 3px;
  height: 3px;
}

.gt-19__spark:nth-child(10) {
  top: 60%;
  left: 70%;
  animation-delay: -1.8s;
  width: 6px;
  height: 6px;
}

.gt-19__sub {
  font-family: monospace;
  font-size: clamp(.7rem, 2vw, 1rem);
  letter-spacing: .25em;
  background: linear-gradient(90deg, var(--g1), var(--g3), var(--g2));
  background-size: 200% 100%;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: gt-19-flow 4s linear infinite;
}

.gt-19__row {
  display: flex;
  gap: 2rem;
  flex-wrap: wrap;
  justify-content: center;
}

.gt-19__gem {
  font-size: clamp(1.2rem, 4vw, 2rem);
  background: linear-gradient(135deg, var(--g1), var(--g3));
  background-size: 200% 200%;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: gt-19-glitter 2.5s ease-in-out infinite;
  filter: drop-shadow(0 0 4px #ffd70050);
}

.gt-19__gem:nth-child(2) {
  animation-delay: -.6s;
  background-image: linear-gradient(135deg, var(--g2), var(--g4));
}

.gt-19__gem:nth-child(3) {
  animation-delay: -1.2s;
  background-image: linear-gradient(135deg, var(--g3), var(--g1));
}

@keyframes gt-19-glitter {
  0%,
    100% {
    background-position: 0% 0%;
    filter: drop-shadow(0 0 6px #ffd70060) drop-shadow(0 0 20px #ff69b440);
  }

  50% {
    background-position: 100% 100%;
    filter: drop-shadow(0 0 12px #ffd700a0) drop-shadow(0 0 40px #ff69b480);
  }
}

@keyframes gt-19-spark {
  0%,
    100% {
    transform: scale(1);
    opacity: .8;
  }

  50% {
    transform: scale(1.8) rotate(45deg);
    opacity: 0;
  }
}

@keyframes gt-19-flow {
  0% {
    background-position: 0% center;
  }

  100% {
    background-position: 200% center;
  }
}

@media (prefers-reduced-motion: reduce) {
  .gt-19__glitter,
    .gt-19__spark,
    .gt-19__sub,
    .gt-19__gem {
    animation: none;
    filter: none;
  }
}
```
