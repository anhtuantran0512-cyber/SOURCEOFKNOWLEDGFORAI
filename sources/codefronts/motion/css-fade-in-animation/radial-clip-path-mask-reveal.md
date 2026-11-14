---
source: "codefronts"
url: "https://codefronts.com/motion/css-fade-in-animation/radial-clip-path-mask-reveal/"
title: "Radial Clip-Path Mask Reveal"
section: "motion"
category: "css-fade-in-animation"
category_name: "CSS Fade In Animation Designs"
description: "A feature panel expands outward from the centre using clip-path: circle(0% → 100%) — a portal-opening radial mask reveal radiating from a single focal point."
has_js: "false"
---

Here's a working CSS Fade In Animation Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Radial Clip-Path Mask Reveal
Source: https://codefronts.com/motion/css-fade-in-animation/radial-clip-path-mask-reveal/

A feature panel expands outward from the centre using clip-path: circle(0% → 100%) — a portal-opening radial mask reveal radiating from a single focal point.
## HTML
```html
<div class="fi-12">
  <div class="fi-12__wrap">
    <div class="fi-12__glow"></div>
    <div class="fi-12__panel">
      <span class="fi-12__emoji">🌀</span>
      <h2 class="fi-12__title">Radial Mask Reveal</h2>
      <p class="fi-12__sub">Content expands outward from a central point using <code>clip-path: circle()</code> — like a portal opening or a spotlight growing to full brightness.</p>
      <div class="fi-12__orbs">
        <div class="fi-12__orb">clip-path</div>
        <div class="fi-12__orb">circle()</div>
        <div class="fi-12__orb">radial reveal</div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.fi-12 {
  --bg: #07080e;
  --sky: #0ea5e9;
  --cobalt: #1d4ed8;
  --text: #f0f9ff;
  font-family: 'Inter',sans-serif;
  min-height: 340px;
  border-radius: 20px;
  display: grid;
  place-items: center;
  padding: 40px;
  overflow: hidden;
}

.fi-12 *,
.fi-12 *::before,
.fi-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fi-12 ::selection {
  background: var(--sky);
  color: #000;
}
/* radial clip-path mask reveal: circle(0%) → circle(100%) */

.fi-12__wrap {
  position: relative;
  max-width: 480px;
  width: 100%;
}

.fi-12__panel {
  background: linear-gradient(135deg,rgba(14,165,233,.12),rgba(29,78,216,.08));
  border: 1px solid rgba(14,165,233,.25);
  border-radius: 20px;
  padding: 36px;
  text-align: center;
  clip-path: circle(0% at 50% 50%);
  animation: fi-12-radial-reveal 1s cubic-bezier(.4,0,.2,1) .15s forwards;
}

.fi-12__glow {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%,-50%);
  width: 200px;
  height: 200px;
  border-radius: 50%;
  background: radial-gradient(circle,rgba(14,165,233,.15),transparent 70%);
  pointer-events: none;
}

.fi-12__emoji {
  font-size: 2.5rem;
  display: block;
  margin-bottom: 16px;
}

.fi-12__title {
  font-family: 'Syne',sans-serif;
  font-size: clamp(1.4rem,3vw,2rem);
  font-weight: 800;
  color: var(--text);
  margin-bottom: 10px;
}

.fi-12__sub {
  font-size: .9rem;
  color: rgba(240,249,255,.5);
  line-height: 1.6;
  margin-bottom: 24px;
}

.fi-12__orbs {
  display: flex;
  gap: 10px;
  justify-content: center;
  flex-wrap: wrap;
}

.fi-12__orb {
  padding: 6px 14px;
  border-radius: 20px;
  font-size: .72rem;
  font-weight: 600;
  background: rgba(14,165,233,.12);
  border: 1px solid rgba(14,165,233,.2);
  color: var(--sky);
}

@keyframes fi-12-radial-reveal {
  to {
    clip-path: circle(100% at 50% 50%);
  }
}

@media (prefers-reduced-motion: reduce) {
  .fi-12__panel {
    animation: none;
    clip-path: none;
  }
}
```
