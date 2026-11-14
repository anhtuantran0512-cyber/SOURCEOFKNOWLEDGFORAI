---
source: "codefronts"
url: "https://codefronts.com/motion/css-fade-in-animation/rotatey-flip-card-fade/"
title: "RotateY Flip Card Fade"
section: "motion"
category: "css-fade-in-animation"
category_name: "CSS Fade In Animation Designs"
description: "Three feature cards flip into view from the side via perspective(800px) rotateY(90deg → 0), fanning in sequence like a hand of cards being dealt face-up."
has_js: "false"
---

Here's a working CSS Fade In Animation Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: RotateY Flip Card Fade
Source: https://codefronts.com/motion/css-fade-in-animation/rotatey-flip-card-fade/

Three feature cards flip into view from the side via perspective(800px) rotateY(90deg → 0), fanning in sequence like a hand of cards being dealt face-up.
## HTML
```html
<div class="fi-14">
  <div class="fi-14__card">
    <div class="fi-14__emoji">🎭</div>
    <div class="fi-14__name">UI Craft</div>
    <div class="fi-14__role">Design System</div>
    <div class="fi-14__divider"></div>
    <div class="fi-14__detail">Cards flip into view from the side using rotateY.</div>
  </div>
  <div class="fi-14__card">
    <div class="fi-14__emoji">⚙️</div>
    <div class="fi-14__name">Dev Tools</div>
    <div class="fi-14__role">Engineering</div>
    <div class="fi-14__divider"></div>
    <div class="fi-14__detail">Each card delays 170ms, creating a fan-in sequence.</div>
  </div>
  <div class="fi-14__card">
    <div class="fi-14__emoji">🚀</div>
    <div class="fi-14__name">Launchpad</div>
    <div class="fi-14__role">Products</div>
    <div class="fi-14__divider"></div>
    <div class="fi-14__detail">Hover reveals a subtle counter-tilt for depth feedback.</div>
  </div>
</div>
```
## CSS
```css
.fi-14 {
  --bg: #0c0814;
  --purple: #9333ea;
  --violet: #7c3aed;
  --text: #faf5ff;
  font-family: 'Inter',sans-serif;
  min-height: 360px;
  border-radius: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 20px;
  flex-wrap: wrap;
  padding: 40px;
  overflow: hidden;
  perspective: 1200px;
}

.fi-14 *,
.fi-14 *::before,
.fi-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fi-14 ::selection {
  background: var(--purple);
  color: #fff;
}
/* flip card: rotateY(90deg) opacity:0 → rotateY(0) opacity:1 */

.fi-14__card {
  width: 160px;
  min-height: 200px;
  border-radius: 16px;
  padding: 24px 18px;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: 10px;
  opacity: 0;
  transform: perspective(800px) rotateY(90deg);
  animation: fi-14-flip-reveal .65s cubic-bezier(.16,1,.3,1) forwards;
  cursor: pointer;
  transition: box-shadow .2s;
}

.fi-14__card:nth-child(1) {
  --d: .05s;
  background: linear-gradient(160deg,rgba(147,51,234,.2),rgba(79,70,229,.1));
  border: 1px solid rgba(147,51,234,.3);
}

.fi-14__card:nth-child(2) {
  --d: .22s;
  background: linear-gradient(160deg,rgba(79,70,229,.2),rgba(59,130,246,.1));
  border: 1px solid rgba(79,70,229,.3);
}

.fi-14__card:nth-child(3) {
  --d: .39s;
  background: linear-gradient(160deg,rgba(236,72,153,.2),rgba(147,51,234,.1));
  border: 1px solid rgba(236,72,153,.3);
}

.fi-14__card {
  animation-delay: var(--d);
}

.fi-14__card:hover {
  box-shadow: 0 16px 48px rgba(147,51,234,.3);
  transform: perspective(800px) rotateY(-5deg) translateY(-4px)!important;
  transition: all .3s;
}

.fi-14__emoji {
  font-size: 2rem;
}

.fi-14__name {
  font-family: 'Syne',sans-serif;
  font-size: .95rem;
  font-weight: 800;
  color: var(--text);
}

.fi-14__role {
  font-size: .72rem;
  color: rgba(250,245,255,.45);
  margin-bottom: 8px;
}

.fi-14__divider {
  width: 32px;
  height: 1px;
  background: rgba(255,255,255,.12);
}

.fi-14__detail {
  font-size: .72rem;
  color: rgba(250,245,255,.55);
  line-height: 1.5;
}

@keyframes fi-14-flip-reveal {
  to {
    opacity: 1;
    transform: perspective(800px) rotateY(0deg);
  }
}

@media (prefers-reduced-motion: reduce) {
  .fi-14 * {
    animation: none!important;
    opacity: 1!important;
    transform: none!important;
  }
}
```
