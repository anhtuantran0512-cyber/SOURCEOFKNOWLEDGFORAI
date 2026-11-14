---
source: "codefronts"
url: "https://codefronts.com/layouts/css-hero-sections/kinetic-type-hero/"
title: "Kinetic Type Hero"
section: "layouts"
category: "css-hero-sections"
category_name: "CSS Hero Sections"
description: "Rave-poster kinetic typography — letters rotate, scale, and float individually using per-letter delay."
has_js: "false"
---

Here's a working CSS Hero Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Kinetic Type Hero
Source: https://codefronts.com/layouts/css-hero-sections/kinetic-type-hero/

Rave-poster kinetic typography — letters rotate, scale, and float individually using per-letter delay. Acid green and magenta on pure black with strobe-like accents.
## HTML
```html
<section class="hs-18" aria-label="Hero">
  <div class="hs-18-pulse" aria-hidden="true"></div>
  <h2 class="hs-18__h">
    <span style="--i: 0">F</span><span style="--i: 1">U</span><span style="--i: 2">L</span
    ><span style="--i: 3">L</span>
    <span class="hs-18__gap"></span>
    <span style="--i: 4">B</span><span style="--i: 5">A</span><span style="--i: 6">S</span
    ><span style="--i: 7">S</span>
    <span class="hs-18__gap"></span>
    <em
      ><span style="--i: 8">M</span><span style="--i: 9">O</span><span style="--i: 10">D</span
      ><span style="--i: 11">E</span></em
    >
  </h2>
  <p class="hs-18__p">
    A booking app for warehouse parties. The line is the door, not the website.
  </p>
  <a class="hs-18__cta" href="#tickets">Get tickets ⚡</a>
</section>
```
## CSS
```css
.hs-18 {
  position: relative;
  display: grid;
  place-items: center;
  width: 100%;
  min-height: 100vh;
  padding: clamp(28px, 5vw, 64px) clamp(20px, 5vw, 56px);
  background: #0a0a0a;
  font-family: 'Inter', system-ui, sans-serif;
  color: #fff;
  box-sizing: border-box;
  overflow: hidden;
  text-align: center;
}

.hs-18-pulse {
  position: absolute;
  inset: 0;
  background: radial-gradient(60% 50% at 30% 30%, rgba(196,255,82,0.18), transparent 60%), radial-gradient(50% 50% at 80% 70%, rgba(238,82,206,0.20), transparent 60%);
  animation: hs-18-pulse 2.4s ease-in-out infinite alternate;
}

@keyframes hs-18-pulse {
  from {
    opacity: 0.6;
  }

  to {
    opacity: 1;
  }
}

.hs-18__h {
  position: relative;
  z-index: 1;
  margin: 0 0 22px;
  font-family: 'Inter', sans-serif;
  font-size: clamp(48px, 9vw, 110px);
  font-weight: 900;
  letter-spacing: -0.04em;
  line-height: 0.92;
  text-transform: uppercase;
}

.hs-18__h span {
  display: inline-block;
  animation: hs-18-jitter 2s ease-in-out infinite;
  animation-delay: calc(var(--i, 0) * 0.06s);
}

.hs-18__h em {
  color: #ee52ce;
  font-style: italic;
}

.hs-18__h em span {
  color: #ee52ce;
}

.hs-18__h > span:nth-child(-n+4) {
  color: #c4ff52;
}

.hs-18__gap {
  display: inline-block;
  width: 0.4em;
}

@keyframes hs-18-jitter {
  0%,
    100% {
    transform: translateY(0) rotate(0deg) scale(1);
  }

  25% {
    transform: translateY(-8px) rotate(-2deg) scale(1.04);
  }

  50% {
    transform: translateY(0) rotate(2deg) scale(0.98);
  }

  75% {
    transform: translateY(6px) rotate(-1deg) scale(1.02);
  }
}

.hs-18__p {
  position: relative;
  z-index: 1;
  margin: 0 auto 26px;
  font-size: 16px;
  color: #888;
  max-width: 440px;
}

.hs-18__cta {
  position: relative;
  z-index: 1;
  display: inline-block;
  padding: 14px 28px;
  background: #c4ff52;
  color: #0a0a0a;
  border-radius: 0;
  text-decoration: none;
  font-weight: 800;
  font-size: 14.5px;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  box-shadow: 0 0 28px rgba(196,255,82,0.45);
  transition: background 0.15s, color 0.15s, box-shadow 0.15s;
}

.hs-18__cta:hover {
  background: #ee52ce;
  color: #fff;
  box-shadow: 0 0 28px rgba(238,82,206,0.55);
}

@media (prefers-reduced-motion: reduce) {
  .hs-18__h span,
    .hs-18-pulse {
    animation: none;
  }

  .hs-18__cta {
    transition: none;
  }
}
```
