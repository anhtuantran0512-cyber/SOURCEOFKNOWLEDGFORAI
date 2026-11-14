---
source: "codefronts"
url: "https://codefronts.com/components/css-gradient-buttons/gooey-liquid-gradient-button/"
title: "Gooey Liquid Gradient Button"
section: "components"
category: "css-gradient-buttons"
category_name: "CSS Gradient Buttons"
description: "A candy-gradient pill whose hidden droplets squish outward and merge with the button body through an SVG goo filter on hover, while the core slowly kneads…"
has_js: "false"
---

Here's a working CSS Gradient Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Gooey Liquid Gradient Button
Source: https://codefronts.com/components/css-gradient-buttons/gooey-liquid-gradient-button/

A candy-gradient pill whose hidden droplets squish outward and merge with the button body through an SVG goo filter on hover, while the core slowly kneads its border-radius like soft jelly.
## HTML
```html
<div class="gx-21">
  <svg class="gx-21__defs" aria-hidden="true" focusable="false">
    <defs>
      <filter id="gx-21-goo">
        <feGaussianBlur in="SourceGraphic" stdDeviation="7" result="blur"/>
        <feColorMatrix in="blur" mode="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 20 -10" result="goo"/>
        <feComposite in="SourceGraphic" in2="goo" operator="atop"/>
      </filter>
    </defs>
  </svg>
  <div class="gx-21__hero">
    <p class="gx-21__logo">Blobby</p>
    <h2 class="gx-21__title">The to-do app that <span>celebrates you</span></h2>
    <p class="gx-21__copy">Finish a task and Blobby throws a tiny party. Miss one and it just… gently forgets. No streaks, no guilt.</p>
    <button class="gx-21__btn" type="button">
      <span class="gx-21__goo" aria-hidden="true">
        <span class="gx-21__core"></span>
        <span class="gx-21__blob gx-21__blob--1"></span>
        <span class="gx-21__blob gx-21__blob--2"></span>
        <span class="gx-21__blob gx-21__blob--3"></span>
        <span class="gx-21__blob gx-21__blob--4"></span>
      </span>
      <span class="gx-21__lab">Get the app</span>
    </button>
    <p class="gx-21__meta">Free forever · <strong>4.9</strong> on the App Store</p>
  </div>
</div>
```
## CSS
```css
.gx-21,
.gx-21 *,
.gx-21 *::before,
.gx-21 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gx-21 ::selection {
  background: #e879f9;
  color: #3b0764;
}

.gx-21 {
  --cream: #fff7ed;
  --ink: #431407;
  --mut: #9a7b6c;
  --p1: #fb7185;
  --p2: #e879f9;
  --p3: #fb923c;
  --spring: cubic-bezier(.34,1.8,.4,1);
  font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
  background: radial-gradient(60% 80% at 85% 10%,rgba(232,121,249,.14),transparent 60%), radial-gradient(50% 70% at 10% 90%,rgba(251,146,60,.16),transparent 60%), var(--cream);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 24px;
  text-align: center;
}

.gx-21__defs {
  position: absolute;
  width: 0;
  height: 0;
  overflow: hidden;
}

.gx-21__hero {
  max-width: 460px;
}

.gx-21__logo {
  display: inline-flex;
  align-items: center;
  gap: 9px;
  font-weight: 800;
  font-size: 15px;
  color: var(--ink);
  letter-spacing: .01em;
}

.gx-21__logo::before {
  content: "";
  width: 18px;
  height: 18px;
  border-radius: 60% 40% 55% 45%/50% 60% 40% 50%;
  background: linear-gradient(130deg,var(--p1),var(--p2));
}

.gx-21__title {
  margin-top: 18px;
  font-size: clamp(28px,5vw,38px);
  font-weight: 800;
  letter-spacing: -.03em;
  line-height: 1.08;
  color: var(--ink);
}

.gx-21__title span {
  background: linear-gradient(115deg,var(--p1),var(--p2) 50%,var(--p3));
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.gx-21__copy {
  margin: 14px auto 0;
  max-width: 36ch;
  font-size: 15px;
  line-height: 1.6;
  color: var(--mut);
}
/* The button. All liquid shapes live inside .gx-21__goo, which carries
   the SVG goo filter (blur + alpha-contrast). The label sits OUTSIDE the
   filtered subtree so the text stays perfectly crisp. */

.gx-21__btn {
  position: relative;
  display: inline-block;
  margin-top: 30px;
  padding: 19px 46px;
  border: 0;
  background: transparent;
  font: inherit;
  font-size: 16px;
  font-weight: 700;
  letter-spacing: .01em;
  color: #fff;
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
}

.gx-21__btn:focus-visible {
  outline: 3px solid var(--p2);
  outline-offset: 8px;
  border-radius: 999px;
}

.gx-21__goo {
  position: absolute;
  inset: -44px;
  /* bleed room so blurred blobs never clip */
  filter: url(#gx-21-goo);
  pointer-events: none;
}

.gx-21__core {
  position: absolute;
  inset: 44px;
  border-radius: 999px;
  background: linear-gradient(115deg,var(--p1),var(--p2) 48%,var(--p3));
  transition: transform .5s var(--spring);
  animation: gx-21-wobble 7s ease-in-out infinite;
}

.gx-21__btn:hover .gx-21__core {
  transform: scale(1.045);
}

.gx-21__btn:active .gx-21__core {
  transform: scale(.96);
}

@keyframes gx-21-wobble {
  0%,
    100% {
    border-radius: 999px;
  }

  30% {
    border-radius: 48% 52% 46% 54%/58% 44% 56% 42%;
  }

  65% {
    border-radius: 52% 48% 55% 45%/45% 57% 43% 55%;
  }
}

.gx-21__blob {
  position: absolute;
  border-radius: 50%;
  transform: scale(.01);
  transition: transform .6s var(--spring);
  will-change: transform;
}

.gx-21__blob--1 {
  width: 26px;
  height: 26px;
  left: 64px;
  top: 46px;
  background: var(--p1);
  transition-delay: 0s;
}

.gx-21__blob--2 {
  width: 20px;
  height: 20px;
  right: 76px;
  top: 50px;
  background: var(--p2);
  transition-delay: .05s;
}

.gx-21__blob--3 {
  width: 30px;
  height: 30px;
  left: 128px;
  bottom: 44px;
  background: var(--p2);
  transition-delay: .1s;
}

.gx-21__blob--4 {
  width: 22px;
  height: 22px;
  right: 58px;
  bottom: 48px;
  background: var(--p3);
  transition-delay: .15s;
}

.gx-21__btn:hover .gx-21__blob--1,
.gx-21__btn:focus-visible .gx-21__blob--1 {
  transform: translate(-26px,-30px) scale(1);
}

.gx-21__btn:hover .gx-21__blob--2,
.gx-21__btn:focus-visible .gx-21__blob--2 {
  transform: translate(24px,-26px) scale(1);
}

.gx-21__btn:hover .gx-21__blob--3,
.gx-21__btn:focus-visible .gx-21__blob--3 {
  transform: translate(-10px,30px) scale(1);
}

.gx-21__btn:hover .gx-21__blob--4,
.gx-21__btn:focus-visible .gx-21__blob--4 {
  transform: translate(30px,26px) scale(1);
}

.gx-21__lab {
  position: relative;
  z-index: 1;
  text-shadow: 0 1px 3px rgba(67,20,7,.25);
}

.gx-21__meta {
  margin-top: 20px;
  font-size: 12.5px;
  letter-spacing: .02em;
  color: var(--mut);
}

.gx-21__meta strong {
  color: var(--ink);
}

@media (prefers-reduced-motion: reduce) {
  .gx-21__core {
    animation: none;
    transition: none;
  }

  .gx-21__blob {
    display: none;
  }
}
```
