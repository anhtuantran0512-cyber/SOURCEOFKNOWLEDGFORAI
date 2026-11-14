---
source: "codefronts"
url: "https://codefronts.com/motion/css-image-hover-effects/css-image-card-flip-3d-animation-hover/"
title: "CSS Image Card Flip 3D Animation Hover"
section: "motion"
category: "css-image-hover-effects"
category_name: "CSS Image Hover Effects"
description: "Cards that rotate 180deg on their Y-axis to reveal a back face with descriptive content, driven entirely by CSS 3D transforms."
has_js: "false"
---

Here's a working CSS Image Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Image Card Flip 3D Animation Hover
Source: https://codefronts.com/motion/css-image-hover-effects/css-image-card-flip-3d-animation-hover/

Cards that rotate 180deg on their Y-axis to reveal a back face with descriptive content, driven entirely by CSS 3D transforms.
## HTML
```html
<div class="ih-20">
  <div class="ih-20__grid">
    <div class="ih-20__scene">
      <div class="ih-20__flipper">
        <div class="ih-20__front">
          <div class="ih-20__front-img ih-20__front-img--1"><span class="ih-20__face-icon">🔭</span></div>
          <div class="ih-20__front-label">
            <p class="ih-20__front-name">Cosmos Explorer</p>
            <p class="ih-20__front-cat">Astrophotography</p>
          </div>
          <span class="ih-20__hint">Hover to flip</span>
        </div>
        <div class="ih-20__back ih-20__back--1">
          <span class="ih-20__back-icon">🌌</span>
          <p class="ih-20__back-title">20-Week Course</p>
          <p class="ih-20__back-desc">Master astrophotography from light pollution basics to deep-sky stacking in Photoshop.</p>
          <button class="ih-20__back-cta">Enroll Now</button>
        </div>
      </div>
    </div>
    <div class="ih-20__scene">
      <div class="ih-20__flipper">
        <div class="ih-20__front">
          <div class="ih-20__front-img ih-20__front-img--2"><span class="ih-20__face-icon">🌿</span></div>
          <div class="ih-20__front-label">
            <p class="ih-20__front-name">Bio Systems</p>
            <p class="ih-20__front-cat">Botany Research</p>
          </div>
          <span class="ih-20__hint">Hover to flip</span>
        </div>
        <div class="ih-20__back ih-20__back--2">
          <span class="ih-20__back-icon">🧬</span>
          <p class="ih-20__back-title">Lab Access</p>
          <p class="ih-20__back-desc">12 months of virtual lab sessions with live microscopy and specimen archive access.</p>
          <button class="ih-20__back-cta">Join Lab</button>
        </div>
      </div>
    </div>
    <div class="ih-20__scene">
      <div class="ih-20__flipper">
        <div class="ih-20__front">
          <div class="ih-20__front-img ih-20__front-img--3"><span class="ih-20__face-icon">🎭</span></div>
          <div class="ih-20__front-label">
            <p class="ih-20__front-name">Digital Arts</p>
            <p class="ih-20__front-cat">Creative Studio</p>
          </div>
          <span class="ih-20__hint">Hover to flip</span>
        </div>
        <div class="ih-20__back ih-20__back--3">
          <span class="ih-20__back-icon">🎨</span>
          <p class="ih-20__back-title">Creator Pack</p>
          <p class="ih-20__back-desc">Unlimited generative art tools, 500+ premium assets, and weekly critique sessions.</p>
          <button class="ih-20__back-cta">Get Access</button>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.ih-20,
.ih-20 *,
.ih-20 *::before,
.ih-20 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.ih-20 ::selection {
  background: #34d399;
  color: #000;
}

.ih-20 {
  --accent: #34d399;
  --accent2: #818cf8;
  --bg: #07070f;
  --text: #f1f5f9;
  --muted: #64748b;
  --duration: 0.65s;
  --ease: cubic-bezier(0.45,0,0.55,1);
  font-family: system-ui,sans-serif;
  background: var(--bg);
  padding: 40px 24px;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  perspective: 1000px;
}

.ih-20__grid {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 20px;
  max-width: 780px;
  width: 100%;
}

.ih-20__scene {
  perspective: 800px;
  aspect-ratio: 3/4;
}
/* The flipper: transform-style:preserve-3d is the key */

.ih-20__flipper {
  position: relative;
  width: 100%;
  height: 100%;
  transform-style: preserve-3d;
  transition: transform var(--duration) var(--ease);
  cursor: pointer;
}

.ih-20__scene:hover .ih-20__flipper {
  transform: rotateY(180deg);
}
/* Both faces share absolute positioning and backface-visibility:hidden */

.ih-20__front,
.ih-20__back {
  position: absolute;
  inset: 0;
  border-radius: 16px;
  overflow: hidden;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
}
/* Back face pre-rotated so it shows on flip */

.ih-20__back {
  transform: rotateY(180deg);
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 20px;
}

.ih-20__front-img {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
}

.ih-20__front-img--1 {
  background: linear-gradient(145deg,#1e1b4b,#312e81,#4338ca,#818cf8);
}

.ih-20__front-img--2 {
  background: linear-gradient(145deg,#052e16,#065f46,#059669,#34d399);
}

.ih-20__front-img--3 {
  background: linear-gradient(145deg,#3b0764,#6b21a8,#9333ea,#e879f9);
}

.ih-20__back--1 {
  background: linear-gradient(135deg,#13103a,#1e1b4b);
}

.ih-20__back--2 {
  background: linear-gradient(135deg,#031b10,#052e16);
}

.ih-20__back--3 {
  background: linear-gradient(135deg,#230335,#3b0764);
}

.ih-20__face-icon {
  font-size: 56px;
  opacity: 0.35;
  position: relative;
  z-index: 1;
}

.ih-20__front-label {
  position: relative;
  z-index: 1;
  padding: 16px;
  background: linear-gradient(to top,rgba(0,0,0,0.8),transparent);
}

.ih-20__front-name {
  font-size: 14px;
  font-weight: 700;
  color: var(--text);
}

.ih-20__front-cat {
  font-size: 10px;
  color: var(--muted);
  margin-top: 2px;
}
/* Back content */

.ih-20__back-icon {
  font-size: 36px;
  margin-bottom: 12px;
}

.ih-20__back-title {
  font-size: 15px;
  font-weight: 800;
  color: var(--text);
  text-align: center;
  margin-bottom: 8px;
}

.ih-20__back-desc {
  font-size: 11px;
  color: var(--muted);
  text-align: center;
  line-height: 1.5;
  margin-bottom: 14px;
}

.ih-20__back-cta {
  padding: 8px 18px;
  border-radius: 24px;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.05em;
  color: #000;
  background: var(--accent);
  border: none;
  cursor: pointer;
  transition: transform 0.2s ease,box-shadow 0.2s ease;
}

.ih-20__back-cta:hover {
  transform: scale(1.04);
  box-shadow: 0 0 16px rgba(52,211,153,0.4);
}

.ih-20__back--3 .ih-20__back-cta {
  background: #e879f9;
  color: #000;
}

.ih-20__back--3 .ih-20__back-cta:hover {
  box-shadow: 0 0 16px rgba(232,121,249,0.4);
}
/* Flip hint badge */

.ih-20__hint {
  position: absolute;
  top: 10px;
  right: 10px;
  z-index: 2;
  background: rgba(255,255,255,0.07);
  border: 1px solid rgba(255,255,255,0.1);
  border-radius: 20px;
  padding: 3px 8px;
  font-size: 9px;
  font-weight: 700;
  color: var(--muted);
  transition: opacity 0.3s ease;
}

.ih-20__scene:hover .ih-20__hint {
  opacity: 0;
}

@media (prefers-reduced-motion: reduce) {
  .ih-20__flipper {
    transition: none;
  }

  .ih-20__scene:hover .ih-20__flipper {
    transform: none;
  }
}
```
