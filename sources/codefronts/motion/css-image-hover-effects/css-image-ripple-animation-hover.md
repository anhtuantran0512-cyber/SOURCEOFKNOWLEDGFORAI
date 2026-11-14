---
source: "codefronts"
url: "https://codefronts.com/motion/css-image-hover-effects/css-image-ripple-animation-hover/"
title: "CSS Image Ripple Animation Hover"
section: "motion"
category: "css-image-hover-effects"
category_name: "CSS Image Hover Effects"
description: "Concentric circle ripples emanate outward from a circular avatar on hover, driven by staggered keyframe animations on sibling span elements."
has_js: "false"
---

Here's a working CSS Image Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Image Ripple Animation Hover
Source: https://codefronts.com/motion/css-image-hover-effects/css-image-ripple-animation-hover/

Concentric circle ripples emanate outward from a circular avatar on hover, driven by staggered keyframe animations on sibling span elements.
## HTML
```html
<div class="ih-15">
  <div class="ih-15__grid">
    <div class="ih-15__item">
      <div class="ih-15__frame">
        <span class="ih-15__ring"></span>
        <span class="ih-15__ring"></span>
        <span class="ih-15__ring"></span>
        <div class="ih-15__avatar ih-15__avatar--1">👩‍🚀</div>
      </div>
      <div style="text-align:center">
        <p class="ih-15__name">Dr. Elena Vasquez</p>
        <p class="ih-15__role">Mission Architect</p>
        <div class="ih-15__socials">
          <span class="ih-15__social">𝕏</span>
          <span class="ih-15__social">in</span>
          <span class="ih-15__social">gh</span>
        </div>
      </div>
    </div>
    <div class="ih-15__item">
      <div class="ih-15__frame">
        <span class="ih-15__ring"></span>
        <span class="ih-15__ring"></span>
        <span class="ih-15__ring"></span>
        <div class="ih-15__avatar ih-15__avatar--2">🧙</div>
      </div>
      <div style="text-align:center">
        <p class="ih-15__name">Orion Blackwood</p>
        <p class="ih-15__role">AI Research Lead</p>
        <div class="ih-15__socials">
          <span class="ih-15__social">𝕏</span>
          <span class="ih-15__social">in</span>
          <span class="ih-15__social">gh</span>
        </div>
      </div>
    </div>
    <div class="ih-15__item">
      <div class="ih-15__frame">
        <span class="ih-15__ring"></span>
        <span class="ih-15__ring"></span>
        <span class="ih-15__ring"></span>
        <div class="ih-15__avatar ih-15__avatar--3">👩‍🌾</div>
      </div>
      <div style="text-align:center">
        <p class="ih-15__name">Freya Lindqvist</p>
        <p class="ih-15__role">Growth Engineer</p>
        <div class="ih-15__socials">
          <span class="ih-15__social">𝕏</span>
          <span class="ih-15__social">in</span>
          <span class="ih-15__social">gh</span>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.ih-15,
.ih-15 *,
.ih-15 *::before,
.ih-15 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.ih-15 ::selection {
  background: #2dd4bf;
  color: #000;
}

.ih-15 {
  --accent: #2dd4bf;
  --bg: #060d0d;
  --text: #f1f5f9;
  --muted: #64748b;
  font-family: system-ui,sans-serif;
  background: var(--bg);
  padding: 40px 24px;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.ih-15__grid {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 20px;
  max-width: 780px;
  width: 100%;
}

.ih-15__item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 14px;
  cursor: pointer;
}
/* Ripple container — must be position:relative so pseudo rings use absolute */

.ih-15__frame {
  position: relative;
  width: 140px;
  height: 140px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.ih-15__avatar {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 42px;
  position: relative;
  z-index: 2;
  transition: transform 0.3s cubic-bezier(0.34,1.56,0.64,1);
}

.ih-15__avatar--1 {
  background: radial-gradient(circle,#1e3a5f,#0369a1);
}

.ih-15__avatar--2 {
  background: radial-gradient(circle,#3b0764,#7e22ce);
}

.ih-15__avatar--3 {
  background: radial-gradient(circle,#052e16,#15803d);
}

.ih-15__item:hover .ih-15__avatar {
  transform: scale(1.08);
}
/* Three ripple rings using sibling spans — keyframe scales + fades */

.ih-15__ring {
  position: absolute;
  border-radius: 50%;
  border: 2px solid var(--accent);
  opacity: 0;
  animation: none;
}

.ih-15__item:hover .ih-15__ring {
  animation: ih-15-ripple 1.5s cubic-bezier(0,0.2,0.8,1) infinite;
}

.ih-15__ring:nth-child(2) {
  animation-delay: 0s;
}

.ih-15__ring:nth-child(3) {
  animation-delay: 0.5s;
}

.ih-15__ring:nth-child(4) {
  animation-delay: 1s;
}

@keyframes ih-15-ripple {
  0% {
    width: 100px;
    height: 100px;
    opacity: 0.6;
    top: calc(50% - 50px);
    left: calc(50% - 50px);
  }

  100% {
    width: 140px;
    height: 140px;
    opacity: 0;
    top: calc(50% - 70px);
    left: calc(50% - 70px);
  }
}
/* Colour the rings per item */

.ih-15__item:nth-child(1) .ih-15__ring {
  border-color: #38bdf8;
}

.ih-15__item:nth-child(2) .ih-15__ring {
  border-color: #c084fc;
}

.ih-15__item:nth-child(3) .ih-15__ring {
  border-color: #4ade80;
}

.ih-15__name {
  font-size: 14px;
  font-weight: 700;
  color: var(--text);
}

.ih-15__role {
  font-size: 11px;
  color: var(--muted);
}

.ih-15__socials {
  display: flex;
  gap: 8px;
  margin-top: 4px;
}

.ih-15__social {
  width: 26px;
  height: 26px;
  border-radius: 50%;
  background: rgba(255,255,255,0.06);
  border: 1px solid rgba(255,255,255,0.08);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 12px;
  transition: background 0.2s ease;
}

.ih-15__item:hover .ih-15__social {
  background: rgba(255,255,255,0.1);
}

@media (prefers-reduced-motion: reduce) {
  .ih-15__ring,
    .ih-15__avatar {
    animation: none!important;
    transition: none;
  }
}
```
