---
source: "codefronts"
url: "https://codefronts.com/motion/css-card-hover-effects/aurora/"
title: "Aurora"
section: "motion"
category: "css-card-hover-effects"
category_name: "CSS Card Hover Effects"
description: "A travel card with layered, drifting northern-lights ribbons over a starfield that brighten and sharpen on hover."
has_js: "false"
---

Here's a working CSS Card Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Aurora
Source: https://codefronts.com/motion/css-card-hover-effects/aurora/

A travel card with layered, drifting northern-lights ribbons over a starfield that brighten and sharpen on hover. Perfect for travel, hospitality, ambient/relaxation, and aspirational brands wanting an atmospheric, dreamlike backdrop.
## HTML
```html
<div class="card-33">
  <article class="card-33__card">
    <div class="card-33__band"></div>
    <div class="card-33__band card-33__b2"></div>
    <div class="card-33__inner">
      <span class="card-33__kicker">Arctic Expeditions</span>
      <h2 class="card-33__title">Chasing<br>the Lights</h2>
      <p class="card-33__desc">Seven nights in Tromsø under the polar sky. Glass-roof cabins, dog sleds, and the slow green fire overhead.</p>
      <div class="card-33__foot">
        <span>Sept – March</span>
        <span>from $2,400</span>
      </div>
    </div>
  </article>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600&family=Jost:wght@300;400;500&display=swap');

.card-33,
.card-33 *,
.card-33 *::before,
.card-33 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.card-33 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  background: #03060d;
  font-family: 'Jost', sans-serif;
  padding: 2rem;
}

.card-33__card {
  position: relative;
  width: 340px;
  height: 450px;
  border-radius: 22px;
  cursor: pointer;
  overflow: hidden;
  background: linear-gradient(180deg, #050b1a 0%, #02040a 100%);
  border: 1px solid rgba(120,255,200,0.1);
}

.card-33__card::before {
  content: "";
  position: absolute;
  inset: 0;
  background-image: radial-gradient(1px 1px at 20% 30%, #fff, transparent), radial-gradient(1px 1px at 70% 20%, #cfe, transparent), radial-gradient(1px 1px at 40% 60%, #fff, transparent), radial-gradient(1px 1px at 85% 75%, #dff, transparent), radial-gradient(1px 1px at 55% 85%, #fff, transparent), radial-gradient(1px 1px at 10% 80%, #cef, transparent);
  opacity: 0.7;
}

.card-33__band {
  position: absolute;
  left: -30%;
  right: -30%;
  height: 60%;
  top: 5%;
  z-index: 1;
  filter: blur(28px);
  opacity: 0.55;
  background: radial-gradient(ellipse 60% 100% at 30% 50%, #2cffa6 0%, transparent 60%), radial-gradient(ellipse 50% 100% at 60% 40%, #3ad0ff 0%, transparent 60%), radial-gradient(ellipse 55% 100% at 80% 60%, #b06cff 0%, transparent 60%);
  transform: translateY(0) skewX(-6deg);
  transition: opacity 0.6s ease, filter 0.6s ease;
  animation: card-33-drift 9s ease-in-out infinite;
}

.card-33__band.card-33__b2 {
  top: 20%;
  opacity: 0.4;
  animation-duration: 13s;
  animation-direction: reverse;
  background: radial-gradient(ellipse 50% 100% at 50% 50%, #5affc4 0%, transparent 60%), radial-gradient(ellipse 50% 100% at 75% 40%, #6a8cff 0%, transparent 60%);
}

@keyframes card-33-drift {
  0%,
    100% {
    transform: translateX(-6%) translateY(0) skewX(-6deg);
  }

  50% {
    transform: translateX(8%) translateY(-12px) skewX(4deg);
  }
}

.card-33__card:hover .card-33__band {
  opacity: 0.85;
  filter: blur(20px);
}

.card-33__inner {
  position: relative;
  z-index: 2;
  height: 100%;
  padding: 2.6rem;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  color: #eafff6;
}

.card-33__kicker {
  font-size: 0.72rem;
  letter-spacing: 0.3em;
  text-transform: uppercase;
  color: #7ff0c4;
  font-weight: 500;
}

.card-33__title {
  font-family: 'Cormorant Garamond', serif;
  font-weight: 500;
  font-size: 3rem;
  line-height: 1;
  margin: 0.6rem 0 0.8rem;
}

.card-33__desc {
  font-size: 0.9rem;
  line-height: 1.65;
  color: #b9d6cc;
  font-weight: 300;
}

.card-33__foot {
  margin-top: 1.4rem;
  display: flex;
  justify-content: space-between;
  font-size: 0.78rem;
  color: #7ff0c4;
  letter-spacing: 0.08em;
  border-top: 1px solid rgba(127,240,196,0.2);
  padding-top: 1rem;
}

@media (prefers-reduced-motion: reduce) {
  .card-33__band {
    animation: none !important;
  }
}
```
