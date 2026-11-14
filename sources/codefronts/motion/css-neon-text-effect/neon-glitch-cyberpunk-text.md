---
source: "codefronts"
url: "https://codefronts.com/motion/css-neon-text-effect/neon-glitch-cyberpunk-text/"
title: "Neon Glitch Cyberpunk Text"
section: "motion"
category: "css-neon-text-effect"
category_name: "CSS Neon Text Effects"
description: "A datamoshed neon title that tears into offset cyan/magenta channels and clips into horizontal bands — the RGB-split glitch cyberpunk and web3 pages want,…"
has_js: "false"
---

Here's a working CSS Neon Text Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neon Glitch Cyberpunk Text
Source: https://codefronts.com/motion/css-neon-text-effect/neon-glitch-cyberpunk-text/

A datamoshed neon title that tears into offset cyan/magenta channels and clips into horizontal bands — the RGB-split glitch cyberpunk and web3 pages want, built from two pseudo-element clones and clip-path, no JS.
## HTML
```html
<div class="cnt-17">
  <h2 class="cnt-17__glitch" data-text="OVERRIDE">OVERRIDE</h2>
</div>
```
## CSS
```css
.cnt-17,
.cnt-17 *,
.cnt-17 *::before,
.cnt-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cnt-17 ::selection {
  background: oklch(0.72 0.24 340);
  color: #fff;
}

.cnt-17 {
  --c1: oklch(0.82 0.16 200);
  --c2: oklch(0.72 0.26 340);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  background: repeating-linear-gradient(0deg,#070709 0 3px,#0a0a0d 3px 6px);
}

.cnt-17__glitch {
  position: relative;
  font-size: clamp(44px,11vw,110px);
  font-weight: 900;
  letter-spacing: .04em;
  color: #f4f6ff;
  text-shadow: 0 0 6px #fff,0 0 20px rgba(180,220,255,.5);
}

.cnt-17__glitch::before,
.cnt-17__glitch::after {
  content: attr(data-text);
  position: absolute;
  inset: 0;
  mix-blend-mode: screen;
}

.cnt-17__glitch::before {
  color: var(--c1);
  text-shadow: 0 0 14px var(--c1);
  animation: cnt-17-a 2.6s steps(2,end) infinite;
}

.cnt-17__glitch::after {
  color: var(--c2);
  text-shadow: 0 0 14px var(--c2);
  animation: cnt-17-b 2.1s steps(2,end) infinite reverse;
}

@keyframes cnt-17-a {
  0% {
    transform: translate(0,0);
    clip-path: inset(20% 0 55% 0);
  }

  20% {
    transform: translate(-4px,0);
    clip-path: inset(70% 0 10% 0);
  }

  40% {
    transform: translate(3px,0);
    clip-path: inset(10% 0 80% 0);
  }

  60% {
    transform: translate(-2px,0);
    clip-path: inset(48% 0 30% 0);
  }

  80% {
    transform: translate(4px,0);
    clip-path: inset(85% 0 2% 0);
  }

  100% {
    transform: translate(0,0);
    clip-path: inset(30% 0 45% 0);
  }
}

@keyframes cnt-17-b {
  0% {
    transform: translate(0,0);
    clip-path: inset(62% 0 12% 0);
  }

  25% {
    transform: translate(5px,0);
    clip-path: inset(12% 0 74% 0);
  }

  50% {
    transform: translate(-3px,0);
    clip-path: inset(40% 0 40% 0);
  }

  75% {
    transform: translate(3px,0);
    clip-path: inset(78% 0 6% 0);
  }

  100% {
    transform: translate(0,0);
    clip-path: inset(24% 0 58% 0);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cnt-17__glitch::before,
    .cnt-17__glitch::after {
    animation: none;
    clip-path: none;
    transform: none;
    opacity: .5;
  }
}
```

## JavaScript
```js
/* No JavaScript — two pseudo clones + animated clip-path insets create the RGB glitch. */
```
