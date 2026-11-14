---
source: "codefronts"
url: "https://codefronts.com/components/css-gradient-buttons/glassmorphism-gradient-button-css/"
title: "Glassmorphism Gradient Button CSS"
section: "components"
category: "css-gradient-buttons"
category_name: "CSS Gradient Buttons"
description: "A frosted-glass membership card and button floating over four drifting gradient blobs, with backdrop-filter doing live blur, saturation and brightness on…"
has_js: "false"
---

Here's a working CSS Gradient Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Gradient Button CSS
Source: https://codefronts.com/components/css-gradient-buttons/glassmorphism-gradient-button-css/

A frosted-glass membership card and button floating over four drifting gradient blobs, with backdrop-filter doing live blur, saturation and brightness on everything behind the glass.
## HTML
```html
<div class="gb-12">
  <div class="gb-12__blob gb-12__blob--1" aria-hidden="true"></div>
  <div class="gb-12__blob gb-12__blob--2" aria-hidden="true"></div>
  <div class="gb-12__blob gb-12__blob--3" aria-hidden="true"></div>
  <div class="gb-12__blob gb-12__blob--4" aria-hidden="true"></div>
  <div class="gb-12__card">
    <h3 class="gb-12__h">Aurora Pass</h3>
    <p class="gb-12__p">One membership, every venue. Frosted-glass entry to 40+ rooftop sessions this season.</p>
    <button class="gb-12__btn" type="button">Get my pass</button>
    <p class="gb-12__meta">From $12/mo · pause anytime</p>
  </div>
</div>
```
## CSS
```css
.gb-12,
.gb-12 *,
.gb-12 *::before,
.gb-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gb-12 ::selection {
  background: rgba(255,255,255,.85);
  color: #5b21b6;
}

.gb-12 {
  --blob-a: #8b5cf6;
  --blob-b: #ec4899;
  --blob-c: #f59e0b;
  --blob-d: #06b6d4;
  font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
  position: relative;
  overflow: hidden;
  background: #241a4a;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 24px;
  isolation: isolate;
}
/* Vibrant drifting blobs — this is the canvas the glass refracts */

.gb-12__blob {
  position: absolute;
  border-radius: 50%;
  filter: blur(60px);
  opacity: .75;
  z-index: -1;
}

.gb-12__blob--1 {
  width: 340px;
  height: 340px;
  left: -6%;
  top: -14%;
  background: var(--blob-a);
  animation: gb-12-drift1 14s ease-in-out infinite alternate;
}

.gb-12__blob--2 {
  width: 300px;
  height: 300px;
  right: -8%;
  top: 8%;
  background: var(--blob-b);
  animation: gb-12-drift2 17s ease-in-out infinite alternate;
}

.gb-12__blob--3 {
  width: 260px;
  height: 260px;
  left: 26%;
  bottom: -22%;
  background: var(--blob-c);
  animation: gb-12-drift3 15s ease-in-out infinite alternate;
}

.gb-12__blob--4 {
  width: 220px;
  height: 220px;
  right: 26%;
  bottom: -10%;
  background: var(--blob-d);
  animation: gb-12-drift1 19s ease-in-out infinite alternate-reverse;
}

@keyframes gb-12-drift1 {
  from {
    transform: translate(0,0) scale(1);
  }

  to {
    transform: translate(60px,44px) scale(1.15);
  }
}

@keyframes gb-12-drift2 {
  from {
    transform: translate(0,0) scale(1);
  }

  to {
    transform: translate(-70px,30px) scale(1.1);
  }
}

@keyframes gb-12-drift3 {
  from {
    transform: translate(0,0) scale(1);
  }

  to {
    transform: translate(46px,-52px) scale(1.2);
  }
}

.gb-12__card {
  width: 100%;
  max-width: 380px;
  border-radius: 24px;
  padding: 36px 32px;
  background: rgba(255,255,255,.1);
  border: 1px solid rgba(255,255,255,.28);
  backdrop-filter: blur(18px) saturate(1.4);
  -webkit-backdrop-filter: blur(18px) saturate(1.4);
  box-shadow: 0 30px 70px -30px rgba(0,0,0,.5),inset 0 1px 0 rgba(255,255,255,.35);
  text-align: center;
}

.gb-12__h {
  color: #fff;
  font-size: 23px;
  font-weight: 800;
  letter-spacing: -.3px;
  margin-bottom: 8px;
  text-shadow: 0 1px 8px rgba(0,0,0,.2);
}

.gb-12__p {
  color: rgba(255,255,255,.75);
  font-size: 14px;
  line-height: 1.6;
  margin-bottom: 28px;
}
/* The button is a second, denser pane of glass with a soft internal
   gradient tint — the blobs stay visible straight through it. */

.gb-12__btn {
  width: 100%;
  padding: 16px 30px;
  border: 1px solid rgba(255,255,255,.45);
  border-radius: 16px;
  font-family: inherit;
  font-size: 16px;
  font-weight: 800;
  color: #fff;
  cursor: pointer;
  background: linear-gradient(120deg,rgba(255,255,255,.28),rgba(255,255,255,.08) 50%,rgba(255,255,255,.2));
  backdrop-filter: blur(10px) saturate(1.6) brightness(1.1);
  -webkit-backdrop-filter: blur(10px) saturate(1.6) brightness(1.1);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.5),0 12px 30px -14px rgba(0,0,0,.45);
  transition: background .35s ease,transform .25s ease,box-shadow .35s ease,border-color .3s ease;
  -webkit-tap-highlight-color: transparent;
}

.gb-12__btn:hover {
  background: linear-gradient(120deg,rgba(255,255,255,.4),rgba(255,255,255,.14) 50%,rgba(255,255,255,.3));
  border-color: rgba(255,255,255,.7);
  transform: translateY(-2px);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.6),0 18px 40px -16px rgba(0,0,0,.55);
}

.gb-12__btn:active {
  transform: translateY(0) scale(.985);
}

.gb-12__btn:focus-visible {
  outline: 3px solid rgba(255,255,255,.9);
  outline-offset: 3px;
}

.gb-12__meta {
  margin-top: 16px;
  font-size: 12px;
  color: rgba(255,255,255,.6);
}

@media (prefers-reduced-motion: reduce) {
  .gb-12__blob {
    animation: none;
  }

  .gb-12__btn {
    transition: none;
  }

  .gb-12__btn:hover {
    transform: none;
  }
}
```
