---
source: "codefronts"
url: "https://codefronts.com/motion/css-fade-in-animation/pure-opacity-hero-fade/"
title: "Pure Opacity Hero Fade"
section: "motion"
category: "css-fade-in-animation"
category_name: "CSS Fade In Animation Designs"
description: "A layered hero section where eyebrow, heading, paragraph, CTA buttons, and indicator dots each fade in sequentially using staggered animation-delay on a…"
has_js: "false"
---

Here's a working CSS Fade In Animation Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure Opacity Hero Fade
Source: https://codefronts.com/motion/css-fade-in-animation/pure-opacity-hero-fade/

A layered hero section where eyebrow, heading, paragraph, CTA buttons, and indicator dots each fade in sequentially using staggered animation-delay on a single opacity keyframe.
## HTML
```html
<div class="fi-01">
  <div class="fi-01__inner">
    <div class="fi-01__eyebrow">Design System v3.0</div>
    <h1 class="fi-01__heading">Build <span>Beautiful</span><br>Interfaces Fast</h1>
    <p class="fi-01__sub">A production-ready design system with 200+ components, dark mode, and accessibility built in.</p>
    <div class="fi-01__cta">
      <button class="fi-01__btn fi-01__btn--primary">Get Started</button>
      <button class="fi-01__btn fi-01__btn--ghost">View Docs</button>
    </div>
    <div class="fi-01__dots">
      <div class="fi-01__dot"></div>
      <div class="fi-01__dot"></div>
      <div class="fi-01__dot"></div>
    </div>
  </div>
</div>
```
## CSS
```css
.fi-01 {
  --bg: #0a0a12;
  --accent: #6c63ff;
  --text: #f0eeff;
  --sub: #9d97c8;
  --dur: 1.2s;
  --ease: cubic-bezier(.16,1,.3,1);
  font-family: 'DM Sans',sans-serif;
  min-height: 320px;
  border-radius: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px;
  overflow: hidden;
  position: relative;
}

.fi-01::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse 60% 50% at 50% 0%,rgba(108,99,255,.18),transparent);
  pointer-events: none;
}

.fi-01 *,
.fi-01 *::before,
.fi-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fi-01 ::selection {
  background: var(--accent);
  color: #fff;
}

.fi-01__inner {
  text-align: center;
  position: relative;
  z-index: 1;
}

.fi-01__eyebrow {
  font-size: .75rem;
  font-weight: 500;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 20px;
  opacity: 0;
  animation: fi-01-fade var(--dur) var(--ease) .1s forwards;
}

.fi-01__heading {
  font-family: 'Syne',sans-serif;
  font-size: clamp(2rem,5vw,3.2rem);
  font-weight: 800;
  color: var(--text);
  line-height: 1.1;
  margin-bottom: 16px;
  opacity: 0;
  animation: fi-01-fade var(--dur) var(--ease) .35s forwards;
}

.fi-01__heading span {
  background: linear-gradient(135deg,#6c63ff,#a78bfa);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.fi-01__sub {
  font-size: 1rem;
  color: var(--sub);
  line-height: 1.6;
  max-width: 440px;
  margin: 0 auto 28px;
  opacity: 0;
  animation: fi-01-fade var(--dur) var(--ease) .55s forwards;
}

.fi-01__cta {
  display: inline-flex;
  gap: 12px;
  align-items: center;
  opacity: 0;
  animation: fi-01-fade var(--dur) var(--ease) .75s forwards;
}

.fi-01__btn {
  padding: 12px 28px;
  border-radius: 10px;
  font-size: .95rem;
  font-weight: 500;
  cursor: pointer;
  border: none;
  transition: transform .2s,box-shadow .2s;
}

.fi-01__btn:hover {
  transform: translateY(-2px);
}

.fi-01__btn--primary {
  background: var(--accent);
  color: #fff;
  box-shadow: 0 8px 24px rgba(108,99,255,.35);
}

.fi-01__btn--primary:hover {
  box-shadow: 0 12px 32px rgba(108,99,255,.5);
}

.fi-01__btn--ghost {
  background: rgba(108,99,255,.1);
  color: var(--text);
  border: 1px solid rgba(108,99,255,.3);
}

.fi-01__dots {
  display: flex;
  gap: 8px;
  justify-content: center;
  margin-top: 24px;
  opacity: 0;
  animation: fi-01-fade var(--dur) var(--ease) .95s forwards;
}

.fi-01__dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--accent);
  opacity: .3;
}

.fi-01__dot:nth-child(2) {
  opacity: .6;
}

.fi-01__dot:nth-child(3) {
  opacity: 1;
}

@keyframes fi-01-fade {
  from {
    opacity: 0;
  }

  to {
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .fi-01 * {
    animation: none!important;
    opacity: 1!important;
  }
}
```
