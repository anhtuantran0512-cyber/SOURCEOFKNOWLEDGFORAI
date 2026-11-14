---
source: "codefronts"
url: "https://codefronts.com/motion/css-neon-text-effect/80s-retro-synthwave-neon-text/"
title: "80s Retro Synthwave Neon Text"
section: "motion"
category: "css-neon-text-effect"
category_name: "CSS Neon Text Effects"
description: "The full magenta-and-cyan Miami-sunset headline: chrome-gradient title, glowing subhead and a perspective grid horizon."
has_js: "false"
---

Here's a working CSS Neon Text Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: 80s Retro Synthwave Neon Text
Source: https://codefronts.com/motion/css-neon-text-effect/80s-retro-synthwave-neon-text/

The full magenta-and-cyan Miami-sunset headline: chrome-gradient title, glowing subhead and a perspective grid horizon. The distinct synthwave aesthetic creative portfolios and music apps search for by name.
## HTML
```html
<div class="cnt-05">
  <div class="cnt-05__stage">
    <p class="cnt-05__kick">◆ SIDE&nbsp;A ◆</p>
    <h2 class="cnt-05__title">NIGHT DRIVE</h2>
    <p class="cnt-05__sub">endless highway · 1986</p>
  </div>
  <div class="cnt-05__grid" aria-hidden="true"></div>
</div>
```
## CSS
```css
.cnt-05,
.cnt-05 *,
.cnt-05 *::before,
.cnt-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cnt-05 ::selection {
  background: oklch(0.72 0.26 330);
  color: #12000c;
}

.cnt-05 {
  --mag: oklch(0.7 0.27 350);
  --cyan: oklch(0.85 0.15 200);
  font-family: 'Segoe UI',system-ui,sans-serif;
  position: relative;
  overflow: hidden;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(180deg,#1a0526 0%,#2b0730 42%,#3a0b2e 52%,#0a0410 100%);
}

.cnt-05__stage {
  position: relative;
  z-index: 2;
  text-align: center;
  padding-bottom: 12vh;
}

.cnt-05__kick {
  font: 13px ui-monospace,Menlo,monospace;
  letter-spacing: .5em;
  color: var(--cyan);
  text-shadow: 0 0 10px var(--cyan);
  margin-bottom: 20px;
}

.cnt-05__title {
  font-size: clamp(48px,13vw,132px);
  font-weight: 900;
  line-height: .9;
  letter-spacing: .02em;
  background: linear-gradient(180deg,#fff 8%,#ffd9f4 34%,var(--mag) 52%,#7a1150 53%,#ffb8ec 74%,#fff 96%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
  filter: drop-shadow(0 0 6px #fff) drop-shadow(0 0 22px var(--mag)) drop-shadow(0 0 54px var(--mag));
}

.cnt-05__sub {
  margin-top: 18px;
  font-size: clamp(14px,3vw,22px);
  font-weight: 600;
  letter-spacing: .32em;
  color: var(--cyan);
  text-shadow: 0 0 8px var(--cyan),0 0 24px color-mix(in oklch,var(--cyan) 70%,transparent);
}

.cnt-05__grid {
  position: absolute;
  left: -25%;
  right: -25%;
  bottom: 0;
  height: 50vh;
  z-index: 1;
  background: linear-gradient(90deg,transparent,var(--mag),transparent) 0 0/100% 2px no-repeat, repeating-linear-gradient(90deg,transparent 0 calc(11.11% - 1px),color-mix(in oklch,var(--cyan) 80%,transparent) calc(11.11% - 1px) 11.11%), repeating-linear-gradient(0deg,transparent 0 39px,color-mix(in oklch,var(--cyan) 80%,transparent) 39px 40px);
  transform: perspective(340px) rotateX(70deg);
  transform-origin: bottom center;
  mask: linear-gradient(0deg,#000 30%,transparent);
  animation: cnt-05-grid 4s linear infinite;
}

@keyframes cnt-05-grid {
  from {
    background-position: 0 0,0 0,0 0;
  }

  to {
    background-position: 0 0,0 0,0 40px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cnt-05__grid {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — chrome-clip title, drop-shadow glow and a CSS perspective grid. */
```
