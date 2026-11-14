---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-gradient-effect/glassmorphism-text-gradient-contrast/"
title: "Glassmorphism Text Gradient Contrast"
section: "motion"
category: "css-text-gradient-effect"
category_name: "CSS Text Gradient Effects"
description: "A backdrop-filter glass card over coloured blobs, with gradient text reinforced by drop-shadow to maintain legibility through the blur."
has_js: "false"
---

Here's a working CSS Text Gradient Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Text Gradient Contrast
Source: https://codefronts.com/motion/css-text-gradient-effect/glassmorphism-text-gradient-contrast/

A backdrop-filter glass card over coloured blobs, with gradient text reinforced by drop-shadow to maintain legibility through the blur.
## HTML
```html
<div class="tg-11">
  <!-- Colourful blobs behind glass -->
  <div class="tg-11__blob tg-11__blob--a" aria-hidden="true"></div>
  <div class="tg-11__blob tg-11__blob--b" aria-hidden="true"></div>
  <div class="tg-11__blob tg-11__blob--c" aria-hidden="true"></div>
  <div class="tg-11__glass">
    <p class="tg-11__eyebrow">— Featured Article</p>
    <h2 class="tg-11__title">Design <span class="tg-11__grad">Systems</span><br>That Scale</h2>
    <p class="tg-11__body">Gradient text on translucent surfaces needs careful colour management. The <code>background-clip: text</code> gradient must maintain ≥4.5:1 contrast against any colour that bleeds through the blur.</p>
    <div class="tg-11__meta">
      <span class="tg-11__avatar">JL</span>
      <div>
        <strong class="tg-11__author">Julia Lam</strong>
        <span class="tg-11__date">Jun 12 · 5 min read</span>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.tg-11,
.tg-11 *,
.tg-11 *::before,
.tg-11 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.tg-11 ::selection {
  background: rgba(168,85,247,.6);
  color: #fff;
}

.tg-11 {
  --g-a: #e879f9;
  --g-b: #818cf8;
  --g-c: #38bdf8;
  --blob-a: #a855f7;
  --blob-b: #ec4899;
  --blob-c: #06b6d4;
  --bg: #06030f;
  --glass: rgba(255,255,255,.07);
  --text: #f0e7ff;
  --muted: rgba(240,231,255,.55);
  font-family: system-ui, -apple-system, sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 24px;
  position: relative;
  overflow: hidden;
}
/* Background colour blobs */

.tg-11__blob {
  position: absolute;
  border-radius: 50%;
  filter: blur(60px);
  opacity: .55;
}

.tg-11__blob--a {
  width: 320px;
  height: 320px;
  background: var(--blob-a);
  top: -80px;
  left: -60px;
}

.tg-11__blob--b {
  width: 280px;
  height: 280px;
  background: var(--blob-b);
  bottom: -60px;
  right: -40px;
}

.tg-11__blob--c {
  width: 200px;
  height: 200px;
  background: var(--blob-c);
  top: 50%;
  left: 55%;
  transform: translate(-50%,-50%);
}
/* Glass card */

.tg-11__glass {
  position: relative;
  z-index: 1;
  background: var(--glass);
  border: 1px solid rgba(255,255,255,.12);
  border-radius: 20px;
  padding: 40px 36px;
  max-width: 500px;
  width: 100%;
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
}

.tg-11__eyebrow {
  font-size: .75rem;
  font-weight: 600;
  letter-spacing: .1em;
  color: var(--muted);
  margin-bottom: 16px;
}

.tg-11__title {
  font-size: clamp(1.8rem, 5vw, 2.8rem);
  font-weight: 800;
  line-height: 1.1;
  letter-spacing: -.03em;
  color: var(--text);
  margin-bottom: 16px;
}
/*
  Contrast strategy: on a blurred translucent surface the background colours
  behind the card bleed through. We use a high-saturation gradient and apply
  a subtle text-shadow on the wrapper to ensure the gradient text reads clearly.
  The gradient direction is angled to maximise the perceived brightness range.
*/

.tg-11__grad {
  background: linear-gradient(110deg, var(--g-a) 0%, var(--g-b) 50%, var(--g-c) 100%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
  filter: drop-shadow(0 1px 8px rgba(232,121,249,.4));
}

.tg-11__body {
  font-size: .9rem;
  color: var(--muted);
  line-height: 1.7;
  margin-bottom: 24px;
}

.tg-11__body code {
  font-size: .8em;
  background: rgba(255,255,255,.1);
  border-radius: 3px;
  padding: 1px 5px;
  color: var(--g-c);
}

.tg-11__meta {
  display: flex;
  align-items: center;
  gap: 12px;
}

.tg-11__avatar {
  width: 34px;
  height: 34px;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--g-a), var(--g-b));
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: .75rem;
  font-weight: 700;
  color: #fff;
  flex-shrink: 0;
}

.tg-11__author {
  display: block;
  font-size: .875rem;
  font-weight: 700;
  color: var(--text);
}

.tg-11__date {
  font-size: .775rem;
  color: var(--muted);
}

@media (prefers-reduced-motion: reduce) {
}
```
