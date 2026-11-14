---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-gradient-effect/multi-color-rainbow-text-gradient-css/"
title: "Multi Color Rainbow Text Gradient CSS"
section: "motion"
category: "css-text-gradient-effect"
category_name: "CSS Text Gradient Effects"
description: "A six-stop HSL hue-wheel gradient cycling 0°→320°, with a continuously animated version driven by background-position shifting."
has_js: "false"
---

Here's a working CSS Text Gradient Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Multi Color Rainbow Text Gradient CSS
Source: https://codefronts.com/motion/css-text-gradient-effect/multi-color-rainbow-text-gradient-css/

A six-stop HSL hue-wheel gradient cycling 0°→320°, with a continuously animated version driven by background-position shifting.
## HTML
```html
<div class="tg-15">
  <div class="tg-15__scene">
    <h1 class="tg-15__rainbow">Spectacular</h1>
    <h2 class="tg-15__rainbow tg-15__anim">Iridescent</h2>
    <div class="tg-15__tag-cloud">
      <span class="tg-15__tag tg-15__t1">Design</span>
      <span class="tg-15__tag tg-15__t2">Colour</span>
      <span class="tg-15__tag tg-15__t3">Motion</span>
      <span class="tg-15__tag tg-15__t4">Type</span>
      <span class="tg-15__tag tg-15__t5">Play</span>
    </div>
    <p class="tg-15__note">4+ colour stops in a <code>linear-gradient</code> create a true rainbow spectrum. Keep saturation high and transition through the full hue wheel (0°→360°) for the most vivid result.</p>
  </div>
</div>
```
## CSS
```css
.tg-15,
.tg-15 *,
.tg-15 *::before,
.tg-15 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.tg-15 ::selection {
  background: #ec4899;
  color: #fff;
}

.tg-15 {
  --bg: #06030c;
  --text: #e2e8f0;
  --muted: #64748b;
  font-family: system-ui, -apple-system, sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 24px;
}

.tg-15__scene {
  max-width: 640px;
  width: 100%;
  text-align: center;
}
/* Full-spectrum rainbow: 6 stops cycling through hsl hues */

.tg-15__rainbow {
  background: linear-gradient(
      90deg,
      hsl(0,   100%, 60%) 0%,
      hsl(45,  100%, 60%) 20%,
      hsl(120, 100%, 45%) 40%,
      hsl(200, 100%, 55%) 60%,
      hsl(270, 100%, 65%) 80%,
      hsl(320, 100%, 60%) 100%
    );
  background-size: 200% 100%;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
  font-weight: 900;
  letter-spacing: -.04em;
  line-height: 1;
  display: block;
}

.tg-15__rainbow:first-child {
  font-size: clamp(3rem, 10vw, 5.5rem);
  margin-bottom: 6px;
}

.tg-15__rainbow.tg-15__anim {
  font-size: clamp(1.8rem, 6vw, 3.5rem);
  background: linear-gradient(
      90deg,
      hsl(200, 100%, 60%) 0%,
      hsl(270, 100%, 65%) 16%,
      hsl(320, 100%, 60%) 33%,
      hsl(0,   100%, 60%) 50%,
      hsl(45,  100%, 60%) 66%,
      hsl(120, 100%, 45%) 83%,
      hsl(200, 100%, 60%) 100%
    );
  background-size: 200% 100%;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: tg-15-shift 3s linear infinite;
  margin-bottom: 32px;
}

@keyframes tg-15-shift {
  0% {
    background-position: 0% 0%;
  }

  100% {
    background-position: 200% 0%;
  }
}

.tg-15__tag-cloud {
  display: flex;
  gap: 10px;
  justify-content: center;
  flex-wrap: wrap;
  margin-bottom: 28px;
}

.tg-15__tag {
  font-size: .85rem;
  font-weight: 700;
  padding: 6px 16px;
  border-radius: 99px;
  border: 1.5px solid transparent;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
  position: relative;
}

.tg-15__tag::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: 99px;
  border: 1.5px solid currentColor;
  opacity: .3;
}
/* background-image (not shorthand) — shorthand resets background-clip
   to border-box and the .tg-15__tag text clipping silently fails. */

.tg-15__t1 {
  background-image: linear-gradient(90deg,hsl(0,90%,60%),hsl(30,90%,60%));
}

.tg-15__t2 {
  background-image: linear-gradient(90deg,hsl(60,90%,50%),hsl(120,90%,45%));
}

.tg-15__t3 {
  background-image: linear-gradient(90deg,hsl(160,90%,45%),hsl(200,90%,55%));
}

.tg-15__t4 {
  background-image: linear-gradient(90deg,hsl(240,90%,65%),hsl(280,90%,65%));
}

.tg-15__t5 {
  background-image: linear-gradient(90deg,hsl(300,90%,60%),hsl(340,90%,60%));
}

.tg-15__note {
  font-size: .8rem;
  color: var(--muted);
  line-height: 1.65;
}

.tg-15__note code {
  background: rgba(255,255,255,.07);
  border-radius: 3px;
  padding: 1px 5px;
  color: hsl(200,90%,65%);
}

@media (prefers-reduced-motion: reduce) {
  .tg-15__anim {
    animation: none;
    background-position: 0% 0%;
  }
}
```
