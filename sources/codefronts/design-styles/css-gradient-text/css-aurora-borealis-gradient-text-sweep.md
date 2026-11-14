---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-gradient-text/css-aurora-borealis-gradient-text-sweep/"
title: "CSS Aurora Borealis Gradient Text Sweep"
section: "design-styles"
category: "css-gradient-text"
category_name: "CSS Gradient Text Designs"
description: "An aurora-inspired diagonal gradient sweeps across a headline using animated background-position on a multi-stop linear-gradient with teal, violet, and…"
has_js: "false"
---

Here's a working CSS Gradient Text Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Aurora Borealis Gradient Text Sweep
Source: https://codefronts.com/design-styles/css-gradient-text/css-aurora-borealis-gradient-text-sweep/

An aurora-inspired diagonal gradient sweeps across a headline using animated background-position on a multi-stop linear-gradient with teal, violet, and emerald hues.
## HTML
```html
<div class="gt-02">
  <div class="gt-02__bg-glow"></div>
  <span class="gt-02__label">Aurora sweep effect</span>
  <h1 class="gt-02__headline">AURORA</h1>
  <p class="gt-02__sub">Northern lights typography</p>
  <div class="gt-02__row">
    <span class="gt-02__chip">TEAL</span>
    <span class="gt-02__chip">VIOLET</span>
    <span class="gt-02__chip">EMERALD</span>
  </div>
</div>
```
## CSS
```css
.gt-02,
.gt-02 *,
.gt-02 *::before,
.gt-02 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.gt-02 {
  --bg: #020b18;
  --a1: #00ffe7;
  --a2: #7b2fff;
  --a3: #00c3ff;
  --a4: #52ff7d;
  font-family: 'Orbitron', sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 2.5rem;
  padding: 3rem 2rem;
  overflow: hidden;
  position: relative;
}

.gt-02__bg-glow {
  position: absolute;
  width: 60vw;
  height: 40vh;
  background: radial-gradient(ellipse at center, #7b2fff22 0%, transparent 70%);
  top: 20%;
  left: 20%;
  animation: gt-02-bgmove 8s ease-in-out infinite alternate;
  pointer-events: none;
}

.gt-02__label {
  font-size: .65rem;
  letter-spacing: .25em;
  text-transform: uppercase;
  color: #00ffe740;
  position: relative;
}

.gt-02__headline {
  font-size: clamp(2.5rem, 10vw, 7rem);
  font-weight: 900;
  line-height: 1;
  letter-spacing: .05em;
  background: linear-gradient(135deg, var(--a1) 0%, var(--a2) 40%, var(--a3) 70%, var(--a4) 100%);
  background-size: 200% 200%;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: gt-02-aurora 5s ease-in-out infinite alternate;
  position: relative;
}

.gt-02__sub {
  font-size: clamp(.8rem, 2.5vw, 1.1rem);
  font-weight: 700;
  letter-spacing: .3em;
  background: linear-gradient(90deg, var(--a4), var(--a1));
  background-size: 200% 100%;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: gt-02-slide 3s linear infinite;
}

.gt-02__row {
  display: flex;
  gap: 2rem;
  position: relative;
}

.gt-02__chip {
  font-size: clamp(1rem, 3vw, 1.6rem);
  font-weight: 700;
  padding: .4em .8em;
  border: 1px solid #00ffe720;
  border-radius: 4px;
  background: linear-gradient(135deg, var(--a1), var(--a2), var(--a3));
  background-size: 300% 300%;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: gt-02-aurora 4s ease-in-out infinite alternate;
}

.gt-02__chip:nth-child(2) {
  animation-delay: -.8s;
}

.gt-02__chip:nth-child(3) {
  animation-delay: -1.6s;
}

@keyframes gt-02-aurora {
  0% {
    background-position: 0% 0%;
  }

  100% {
    background-position: 100% 100%;
  }
}

@keyframes gt-02-slide {
  0% {
    background-position: 0% center;
  }

  100% {
    background-position: 200% center;
  }
}

@keyframes gt-02-bgmove {
  0% {
    transform: translate(0, 0) scale(1);
  }

  100% {
    transform: translate(15%, 10%) scale(1.3);
  }
}

@media (prefers-reduced-motion: reduce) {
  .gt-02__headline,
    .gt-02__sub,
    .gt-02__chip,
    .gt-02__bg-glow {
    animation: none;
  }
}
```
