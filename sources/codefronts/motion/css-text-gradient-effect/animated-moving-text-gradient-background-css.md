---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-gradient-effect/animated-moving-text-gradient-background-css/"
title: "Animated Moving Text Gradient Background CSS"
section: "motion"
category: "css-text-gradient-effect"
category_name: "CSS Text Gradient Effects"
description: "A hero section where the gradient background-position animates continuously across a 300%-wide gradient, creating a shifting colour sweep through the text."
has_js: "false"
---

Here's a working CSS Text Gradient Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Animated Moving Text Gradient Background CSS
Source: https://codefronts.com/motion/css-text-gradient-effect/animated-moving-text-gradient-background-css/

A hero section where the gradient background-position animates continuously across a 300%-wide gradient, creating a shifting colour sweep through the text.
## HTML
```html
<div class="tg-08">
  <div class="tg-08__hero">
    <div class="tg-08__tag">✦ New — Season 3</div>
    <h1 class="tg-08__title">The Future<br>of <span class="tg-08__anim-grad">Interface</span><br>Design</h1>
    <p class="tg-08__sub">Shifting gradients create motion and energy without a single line of JavaScript.</p>
  </div>
</div>
```
## CSS
```css
.tg-08,
.tg-08 *,
.tg-08 *::before,
.tg-08 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.tg-08 ::selection {
  background: #7c3aed55;
  color: #fff;
}

.tg-08 {
  --c1: #f0abfc;
  --c2: #818cf8;
  --c3: #38bdf8;
  --c4: #34d399;
  --bg: #0a0a12;
  --text: #f8fafc;
  --muted: #94a3b8;
  font-family: system-ui, -apple-system, sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 24px;
}

.tg-08__hero {
  text-align: center;
  max-width: 600px;
}

.tg-08__tag {
  display: inline-block;
  font-size: .75rem;
  font-weight: 700;
  letter-spacing: .1em;
  color: var(--muted);
  margin-bottom: 24px;
}

.tg-08__title {
  font-size: clamp(2.5rem, 8vw, 4.5rem);
  font-weight: 900;
  line-height: 1.08;
  letter-spacing: -.04em;
  color: var(--text);
  margin-bottom: 20px;
}
/*
  Moving gradient: background-size is 300% wide so the 
  gradient has room to travel. background-position animates
  from 0% to 100%, which pans across the extended gradient.
  background-clip:text exposes it through the letterforms.
*/

.tg-08__anim-grad {
  background: linear-gradient(
      90deg,
      var(--c1) 0%,
      var(--c2) 25%,
      var(--c3) 50%,
      var(--c4) 75%,
      var(--c1) 100%
    );
  background-size: 300% 100%;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
  animation: tg-08-shift 4s linear infinite;
}

@keyframes tg-08-shift {
  0% {
    background-position: 0% 50%;
  }

  100% {
    background-position: 100% 50%;
  }
}

.tg-08__sub {
  font-size: 1rem;
  color: var(--muted);
  line-height: 1.7;
  max-width: 480px;
  margin: 0 auto;
}

@media (prefers-reduced-motion: reduce) {
  .tg-08__anim-grad {
    animation: none;
    background-position: 0% 50%;
  }
}
```
