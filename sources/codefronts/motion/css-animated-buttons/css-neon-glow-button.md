---
source: "codefronts"
url: "https://codefronts.com/motion/css-animated-buttons/css-neon-glow-button/"
title: "CSS Neon Glow Button"
section: "motion"
category: "css-animated-buttons"
category_name: "CSS Animated Buttons"
description: "A neon-lit CTA button with a pulsing glow halo and colour-shifting outline, built entirely with CSS box-shadow animations and no JavaScript."
has_js: "false"
---

Here's a working CSS Animated Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Neon Glow Button
Source: https://codefronts.com/motion/css-animated-buttons/css-neon-glow-button/

A neon-lit CTA button with a pulsing glow halo and colour-shifting outline, built entirely with CSS box-shadow animations and no JavaScript.
## HTML
```html
<div class="ab-01">
  <div class="ab-01__scene">
    <p class="ab-01__label">Premium SaaS — Launch Your Project</p>
    <h2 class="ab-01__headline">Build faster.<br>Ship smarter.</h2>
    <p class="ab-01__sub">Join 50,000+ developers already on the platform.</p>
    <button class="ab-01__btn">Get Started Free</button>
    <p class="ab-01__hint">No credit card required · Cancel anytime</p>
  </div>
</div>
```
## CSS
```css
.ab-01,
.ab-01 *,
.ab-01 *::before,
.ab-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ab-01 ::selection {
  background: #b829ff;
  color: #fff;
}

.ab-01 {
  --neon: #b829ff;
  --neon-dim: rgba(184,41,255,.35);
  --bg: #0a0010;
  --text: #e8d5ff;
  font-family: system-ui,sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.ab-01__scene {
  text-align: center;
  padding: 2.5rem 2rem;
  max-width: 520px;
}

.ab-01__label {
  font-size: .72rem;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--neon);
  margin-bottom: .75rem;
  opacity: .8;
}

.ab-01__headline {
  font-size: clamp(1.8rem,4vw,2.6rem);
  font-weight: 800;
  color: #fff;
  line-height: 1.15;
  margin-bottom: .75rem;
}

.ab-01__sub {
  font-size: .95rem;
  color: var(--text);
  opacity: .7;
  margin-bottom: 2rem;
}

.ab-01__btn {
  position: relative;
  display: inline-flex;
  align-items: center;
  gap: .5rem;
  padding: .85rem 2.4rem;
  font-size: 1rem;
  font-weight: 700;
  letter-spacing: .04em;
  color: #fff;
  background: transparent;
  border: 2px solid var(--neon);
  border-radius: 8px;
  cursor: pointer;
  outline: none;
  text-transform: uppercase;
  transition: color .3s,background .3s,border-color .3s,box-shadow .3s;
  box-shadow: 0 0 8px var(--neon-dim),0 0 20px var(--neon-dim),inset 0 0 10px rgba(184,41,255,.08);
  animation: ab-01-pulse 2s ease-in-out infinite;
  will-change: box-shadow;
  text-shadow: 0 0 8px rgba(184,41,255,.6);
}

.ab-01__btn:hover {
  background: var(--neon);
  color: #fff;
  box-shadow: 0 0 16px var(--neon),0 0 40px var(--neon),0 0 80px var(--neon-dim),inset 0 0 16px rgba(255,255,255,.15);
  text-shadow: none;
  animation-play-state: paused;
}

.ab-01__btn:active {
  transform: scale(.97);
}

@keyframes ab-01-pulse {
  0%,
    100% {
    box-shadow: 0 0 8px var(--neon-dim),0 0 20px var(--neon-dim),inset 0 0 10px rgba(184,41,255,.08);
  }

  50% {
    box-shadow: 0 0 14px var(--neon),0 0 36px var(--neon-dim),0 0 60px rgba(184,41,255,.15),inset 0 0 16px rgba(184,41,255,.12);
  }
}

.ab-01__hint {
  margin-top: 1rem;
  font-size: .78rem;
  color: var(--text);
  opacity: .45;
}

@media (prefers-reduced-motion: reduce) {
  .ab-01__btn {
    animation: none;
  }
}
```
