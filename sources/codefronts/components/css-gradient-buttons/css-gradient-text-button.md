---
source: "codefronts"
url: "https://codefronts.com/components/css-gradient-buttons/css-gradient-text-button/"
title: "CSS Gradient Text Button"
section: "components"
category: "css-gradient-buttons"
category_name: "CSS Gradient Buttons"
description: "Minimal studio buttons whose labels carry a four-hue oil-slick gradient through background-clip: text, flowing across the letters on hover while the chrome…"
has_js: "false"
---

Here's a working CSS Gradient Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Gradient Text Button
Source: https://codefronts.com/components/css-gradient-buttons/css-gradient-text-button/

Minimal studio buttons whose labels carry a four-hue oil-slick gradient through background-clip: text, flowing across the letters on hover while the chrome stays quiet.
## HTML
```html
<div class="gb-08">
  <div class="gb-08__stage">
    <p class="gb-08__logo">Mono<em>/</em>Studio</p>
    <h3 class="gb-08__h">Brand systems for the post-template era.</h3>
    <div class="gb-08__row">
      <button class="gb-08__btn" type="button"><span>See our work</span></button>
      <button class="gb-08__btn gb-08__btn--ink" type="button"><span>Start a project</span></button>
    </div>
    <p class="gb-08__note">Hover — the oil-slick gradient flows through the letters</p>
  </div>
</div>
```
## CSS
```css
.gb-08,
.gb-08 *,
.gb-08 *::before,
.gb-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gb-08 ::selection {
  background: #111;
  color: #fff;
}

.gb-08 {
  --slick-a: #f59e0b;
  --slick-b: #ec4899;
  --slick-c: #8b5cf6;
  --slick-d: #06b6d4;
  --ink: #111111;
  font-family: "Helvetica Neue",Helvetica,-apple-system,Arial,sans-serif;
  background: #fcfcfa;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 24px;
}

.gb-08__stage {
  max-width: 460px;
  width: 100%;
  text-align: center;
}

.gb-08__logo {
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 5px;
  text-transform: uppercase;
  color: var(--ink);
  margin-bottom: 52px;
}

.gb-08__logo em {
  font-style: normal;
  color: #bbb;
}

.gb-08__h {
  font-size: 34px;
  font-weight: 800;
  letter-spacing: -1.2px;
  line-height: 1.12;
  color: var(--ink);
  margin-bottom: 40px;
}

.gb-08__row {
  display: flex;
  gap: 18px;
  justify-content: center;
  flex-wrap: wrap;
}
/* The label carries the gradient via background-clip:text on a 300%
   canvas; hover slides the position so the hues flow through the
   letters while the button chrome stays quiet. */

.gb-08__btn {
  padding: 16px 34px;
  border: 1.5px solid #e4e4e0;
  border-radius: 999px;
  background: #fff;
  font-family: inherit;
  font-size: 16px;
  font-weight: 800;
  letter-spacing: -.2px;
  cursor: pointer;
  transition: border-color .3s ease,box-shadow .35s ease,transform .25s ease;
  -webkit-tap-highlight-color: transparent;
}

.gb-08__btn span {
  display: inline-block;
  background-image: linear-gradient(100deg,
      var(--slick-a),var(--slick-b) 30%,var(--slick-c) 60%,var(--slick-d) 85%,var(--slick-a));
  background-size: 300% auto;
  background-position: 0% center;
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  transition: background-position .8s cubic-bezier(.22,1,.36,1);
}

.gb-08__btn:hover {
  border-color: #d4d4d0;
  transform: translateY(-2px);
  box-shadow: 0 14px 34px -18px rgba(139,92,246,.45);
}

.gb-08__btn:hover span {
  background-position: 100% center;
}

.gb-08__btn:active {
  transform: translateY(0);
}

.gb-08__btn:focus-visible {
  outline: 3px solid var(--slick-c);
  outline-offset: 3px;
}
/* Inverted twin: ink pill, gradient text pops against black */

.gb-08__btn--ink {
  background: var(--ink);
  border-color: var(--ink);
}

.gb-08__btn--ink:hover {
  border-color: var(--ink);
  box-shadow: 0 14px 34px -16px rgba(17,17,17,.5);
}

.gb-08__note {
  margin-top: 34px;
  font-size: 12.5px;
  color: #aaa;
  letter-spacing: .3px;
}

@media (prefers-reduced-motion: reduce) {
  .gb-08__btn,
    .gb-08__btn span {
    transition: none;
  }

  .gb-08__btn:hover {
    transform: none;
  }

  .gb-08__btn:hover span {
    background-position: 0% center;
  }
}
```
