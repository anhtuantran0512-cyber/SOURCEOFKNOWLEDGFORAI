---
source: "codefronts"
url: "https://codefronts.com/motion/css-fade-in-animation/skew-sweep-fade/"
title: "Skew Sweep Fade"
section: "motion"
category: "css-fade-in-animation"
category_name: "CSS Fade In Animation Designs"
description: "Three stat panels slice into frame from the left using skewX(15deg) + translateX(-40px) → skewX(0) — a momentum-carrying diagonal sweep entrance."
has_js: "false"
---

Here's a working CSS Fade In Animation Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Skew Sweep Fade
Source: https://codefronts.com/motion/css-fade-in-animation/skew-sweep-fade/

Three stat panels slice into frame from the left using skewX(15deg) + translateX(-40px) → skewX(0) — a momentum-carrying diagonal sweep entrance.
## HTML
```html
<div class="fi-11">
  <div class="fi-11__block">
    <div class="fi-11__num">847K</div>
    <div class="fi-11__stat">Monthly Views</div>
    <div class="fi-11__divider"></div>
    <div class="fi-11__desc">Panels slice into view from the left with a momentum-carrying skew.</div>
  </div>
  <div class="fi-11__block">
    <div class="fi-11__num">12.3K</div>
    <div class="fi-11__stat">Subscribers</div>
    <div class="fi-11__divider"></div>
    <div class="fi-11__desc">skewX(15deg) creates a dynamic diagonal entry effect.</div>
  </div>
  <div class="fi-11__block">
    <div class="fi-11__num">98%</div>
    <div class="fi-11__stat">Satisfaction</div>
    <div class="fi-11__divider"></div>
    <div class="fi-11__desc">Combined with translateX for a satisfying sweeping entrance.</div>
  </div>
</div>
```
## CSS
```css
.fi-11 {
  --bg: #0f0a14;
  --rose: #f43f5e;
  --pink: #ec4899;
  --text: #fff1f2;
  font-family: 'DM Sans',sans-serif;
  min-height: 340px;
  border-radius: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 20px;
  flex-wrap: wrap;
  padding: 40px;
  overflow: hidden;
}

.fi-11 *,
.fi-11 *::before,
.fi-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fi-11 ::selection {
  background: var(--rose);
  color: #fff;
}
/* skew + fade: skewX(15deg) translateX(-40px) opacity:0 → skewX(0) translateX(0) opacity:1 */

.fi-11__block {
  border-radius: 14px;
  padding: 28px 24px;
  flex: 1;
  min-width: 160px;
  max-width: 200px;
  opacity: 0;
  transform: skewX(15deg) translateX(-40px);
  animation: fi-11-skew-in .7s cubic-bezier(.16,1,.3,1) forwards;
}

.fi-11__block:nth-child(1) {
  --d: .05s;
  background: linear-gradient(135deg,rgba(244,63,94,.18),rgba(236,72,153,.08));
  border: 1px solid rgba(244,63,94,.25);
}

.fi-11__block:nth-child(2) {
  --d: .2s;
  background: linear-gradient(135deg,rgba(236,72,153,.18),rgba(168,85,247,.08));
  border: 1px solid rgba(236,72,153,.25);
}

.fi-11__block:nth-child(3) {
  --d: .35s;
  background: linear-gradient(135deg,rgba(168,85,247,.18),rgba(99,102,241,.08));
  border: 1px solid rgba(168,85,247,.25);
}

.fi-11__block {
  animation-delay: var(--d);
}

.fi-11__block:hover {
  transform: skewX(0) translateX(0) scale(1.03)!important;
  transition: transform .25s;
}

.fi-11__num {
  font-family: 'Syne',sans-serif;
  font-size: 2.2rem;
  font-weight: 800;
  line-height: 1;
  margin-bottom: 4px;
}

.fi-11__block:nth-child(1) .fi-11__num {
  color: var(--rose);
}

.fi-11__block:nth-child(2) .fi-11__num {
  color: var(--pink);
}

.fi-11__block:nth-child(3) .fi-11__num {
  color: #a78bfa;
}

.fi-11__stat {
  font-size: .7rem;
  font-weight: 700;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: rgba(255,241,242,.45);
  margin-bottom: 14px;
}

.fi-11__divider {
  height: 1px;
  background: rgba(255,255,255,.08);
  margin-bottom: 12px;
}

.fi-11__desc {
  font-size: .78rem;
  color: rgba(255,241,242,.55);
  line-height: 1.5;
}

@keyframes fi-11-skew-in {
  to {
    opacity: 1;
    transform: skewX(0deg) translateX(0);
  }
}

@media (prefers-reduced-motion: reduce) {
  .fi-11 * {
    animation: none!important;
    opacity: 1!important;
    transform: none!important;
  }
}
```
