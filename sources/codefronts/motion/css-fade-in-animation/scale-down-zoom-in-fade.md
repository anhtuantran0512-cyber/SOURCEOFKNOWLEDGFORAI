---
source: "codefronts"
url: "https://codefronts.com/motion/css-fade-in-animation/scale-down-zoom-in-fade/"
title: "Scale-Down Zoom In Fade"
section: "motion"
category: "css-fade-in-animation"
category_name: "CSS Fade In Animation Designs"
description: "A premium hero that fades in from scale(1.4), shrinking to normal — a dramatic 'punch out' cinematic entrance where content arrives oversized then settles…"
has_js: "false"
---

Here's a working CSS Fade In Animation Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Scale-Down Zoom In Fade
Source: https://codefronts.com/motion/css-fade-in-animation/scale-down-zoom-in-fade/

A premium hero that fades in from scale(1.4), shrinking to normal — a dramatic 'punch out' cinematic entrance where content arrives oversized then settles into place.
## HTML
```html
<div class="fi-08">
  <div class="fi-08__hero">
    <span class="fi-08__crown">👑</span>
    <h1 class="fi-08__title">Scale-Down<br><em>Entrance</em></h1>
    <p class="fi-08__sub">Content arrives oversized and shrinks to fit — a cinematic "punch out" effect using scale(1.4) → scale(1) with opacity.</p>
    <div class="fi-08__ribbon">
      <div class="fi-08__ritem">Premium</div>
      <div class="fi-08__ritem">Exclusive</div>
      <div class="fi-08__ritem">Gold Tier</div>
    </div>
  </div>
</div>
```
## CSS
```css
.fi-08 {
  --bg: #100c1e;
  --gold: #f59e0b;
  --amber: #d97706;
  --text: #fffbeb;
  font-family: 'DM Sans',sans-serif;
  min-height: 340px;
  border-radius: 20px;
  display: grid;
  place-items: center;
  padding: 40px;
  overflow: hidden;
  position: relative;
}

.fi-08::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(circle 300px at 50% 50%,rgba(245,158,11,.07),transparent);
}

.fi-08 *,
.fi-08 *::before,
.fi-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fi-08 ::selection {
  background: var(--gold);
  color: #000;
}
/* scale-down fade: scale(1.4) opacity:0 → scale(1) opacity:1 — dramatic zoom-in from large */

.fi-08__hero {
  text-align: center;
  position: relative;
  z-index: 1;
  opacity: 0;
  transform: scale(1.4);
  animation: fi-08-zoom-in .9s cubic-bezier(.25,.46,.45,.94) .1s forwards;
}

.fi-08__crown {
  font-size: 3rem;
  margin-bottom: 12px;
  display: block;
}

.fi-08__title {
  font-family: 'Syne',sans-serif;
  font-size: clamp(2rem,5vw,3.5rem);
  font-weight: 800;
  color: var(--text);
  line-height: 1;
  margin-bottom: 8px;
}

.fi-08__title em {
  font-style: normal;
  background: linear-gradient(90deg,var(--gold),var(--amber));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.fi-08__sub {
  font-size: 1rem;
  color: rgba(255,251,235,.5);
  margin: 16px 0 28px;
  max-width: 360px;
  margin-left: auto;
  margin-right: auto;
  line-height: 1.6;
}

.fi-08__ribbon {
  display: inline-flex;
  gap: 20px;
  align-items: center;
  background: rgba(245,158,11,.1);
  border: 1px solid rgba(245,158,11,.25);
  border-radius: 40px;
  padding: 10px 24px;
}

.fi-08__ritem {
  font-size: .8rem;
  font-weight: 600;
  color: var(--gold);
  display: flex;
  gap: 6px;
  align-items: center;
}

.fi-08__ritem::before {
  content: '✦';
  font-size: .6rem;
  opacity: .7;
}

.fi-08__ritem + .fi-08__ritem {
  border-left: 1px solid rgba(245,158,11,.2);
  padding-left: 20px;
}

@keyframes fi-08-zoom-in {
  to {
    opacity: 1;
    transform: scale(1);
  }
}

@media (prefers-reduced-motion: reduce) {
  .fi-08 * {
    animation: none!important;
    opacity: 1!important;
    transform: scale(1)!important;
  }
}
```
