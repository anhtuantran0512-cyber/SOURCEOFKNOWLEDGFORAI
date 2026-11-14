---
source: "codefronts"
url: "https://codefronts.com/components/css-gradient-buttons/css-sliding-gradient-button-on-hover/"
title: "CSS Sliding Gradient Button On Hover"
section: "components"
category: "css-gradient-buttons"
category_name: "CSS Gradient Buttons"
description: "A music-player CTA where a 300%-wide grape-to-tangerine gradient sweeps fully across on hover, chased by a skewed light streak riding the same easing curve."
has_js: "false"
---

Here's a working CSS Gradient Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Sliding Gradient Button On Hover
Source: https://codefronts.com/components/css-gradient-buttons/css-sliding-gradient-button-on-hover/

A music-player CTA where a 300%-wide grape-to-tangerine gradient sweeps fully across on hover, chased by a skewed light streak riding the same easing curve.
## HTML
```html
<div class="gb-07">
  <div class="gb-07__player">
    <div class="gb-07__meta">
      <div class="gb-07__art" aria-hidden="true"></div>
      <div>
        <p class="gb-07__track">Neon Tangerine</p>
        <p class="gb-07__artist">Velvet Static · Midnight EP</p>
      </div>
    </div>
    <div class="gb-07__bar" aria-hidden="true"><i></i></div>
    <button class="gb-07__btn" type="button">Listen now</button>
  </div>
</div>
```
## CSS
```css
.gb-07,
.gb-07 *,
.gb-07 *::before,
.gb-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gb-07 ::selection {
  background: #fb923c;
  color: #1c0a14;
}

.gb-07 {
  --hot: #f43f5e;
  --tang: #fb923c;
  --grape: #a21caf;
  --bg: #1c0a14;
  font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
  background: radial-gradient(900px 460px at 20% -20%,rgba(162,28,175,.35),transparent 60%),var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 24px;
}

.gb-07__player {
  width: 100%;
  max-width: 400px;
  background: rgba(255,255,255,.04);
  border: 1px solid rgba(255,255,255,.08);
  border-radius: 22px;
  padding: 28px;
  display: flex;
  flex-direction: column;
  gap: 22px;
}

.gb-07__meta {
  display: flex;
  gap: 16px;
  align-items: center;
}

.gb-07__art {
  width: 64px;
  height: 64px;
  flex: none;
  border-radius: 14px;
  background: conic-gradient(from 220deg,var(--hot),var(--tang),var(--grape),var(--hot));
  box-shadow: 0 8px 20px -6px rgba(244,63,94,.5);
}

.gb-07__track {
  color: #fff;
  font-size: 16px;
  font-weight: 800;
  letter-spacing: -.2px;
}

.gb-07__artist {
  color: #b58aa5;
  font-size: 13px;
  margin-top: 3px;
}

.gb-07__bar {
  height: 5px;
  border-radius: 99px;
  background: rgba(255,255,255,.1);
  overflow: hidden;
}

.gb-07__bar i {
  display: block;
  height: 100%;
  width: 38%;
  border-radius: inherit;
  background: linear-gradient(90deg,var(--tang),var(--hot));
}
/* The sweep: a 300%-wide three-hue gradient parked at the left.
   Hover slides it fully across — one compositor-friendly move. */

.gb-07__btn {
  position: relative;
  width: 100%;
  padding: 17px 28px;
  border: none;
  border-radius: 14px;
  font-family: inherit;
  font-size: 16px;
  font-weight: 800;
  letter-spacing: .4px;
  color: #fff;
  cursor: pointer;
  overflow: hidden;
  background-image: linear-gradient(90deg,
      var(--grape) 0%,var(--hot) 25%,var(--tang) 50%,var(--hot) 75%,var(--grape) 100%);
  background-size: 300% auto;
  background-position: 0% center;
  box-shadow: 0 12px 30px -10px rgba(244,63,94,.55);
  transition: background-position .7s cubic-bezier(.22,1,.36,1),transform .25s ease;
  -webkit-tap-highlight-color: transparent;
}

.gb-07__btn:hover {
  background-position: 100% center;
  transform: translateY(-2px);
}

.gb-07__btn:active {
  transform: translateY(0) scale(.98);
}

.gb-07__btn:focus-visible {
  outline: 3px solid var(--tang);
  outline-offset: 3px;
}
/* Thin light streak rides along during the sweep */

.gb-07__btn::after {
  content: "";
  position: absolute;
  top: 0;
  bottom: 0;
  left: -30%;
  width: 22%;
  background: linear-gradient(100deg,transparent,rgba(255,255,255,.35),transparent);
  transform: skewX(-18deg);
  transition: left .7s cubic-bezier(.22,1,.36,1);
  pointer-events: none;
}

.gb-07__btn:hover::after {
  left: 120%;
}

@media (prefers-reduced-motion: reduce) {
  .gb-07__btn,
    .gb-07__btn::after {
    transition: none;
  }

  .gb-07__btn:hover {
    background-position: 0% center;
    transform: none;
  }

  .gb-07__btn:hover::after {
    left: -30%;
  }
}
```
