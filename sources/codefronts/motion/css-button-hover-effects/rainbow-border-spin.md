---
source: "codefronts"
url: "https://codefronts.com/motion/css-button-hover-effects/rainbow-border-spin/"
title: "Rainbow Border Spin"
section: "motion"
category: "css-button-hover-effects"
category_name: "CSS Button Hover Effects"
description: "A vivid CTA framed by a rotating full-spectrum gradient border with a soft blurred glow bleeding behind it — the 'AI / pro' badge look."
has_js: "false"
---

Here's a working CSS Button Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Rainbow Border Spin
Source: https://codefronts.com/motion/css-button-hover-effects/rainbow-border-spin/

A vivid CTA framed by a rotating full-spectrum gradient border with a soft blurred glow bleeding behind it — the 'AI / pro' badge look. Uses a rotating gradient layer (no @property, unlike topic 08).
## HTML
```html
<div class="bhe-29-group">
<section class="bhe-29a" aria-label="Rainbow border spin button">
  <button class="bhe-29a__btn" type="button"><span>Upgrade to Pro</span></button>
</section>
<section class="bhe-29b" aria-label="Duotone border spin button">
  <button class="bhe-29b__btn" type="button"><span class="bhe-29b__cover"></span><span>Go premium</span></button>
</section>
</div>
```
## CSS
```css
.bhe-29-group {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-wrap: wrap;
}

.bhe-29-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

.bhe-29a,
.bhe-29a *,
.bhe-29a *::before,
.bhe-29a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-29a {
  --card: #12121a;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #07070d;
}

.bhe-29a__btn {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  font-size: 16px;
  font-weight: 800;
  color: #fff;
  padding: 16px 38px;
  border: none;
  border-radius: 14px;
  cursor: pointer;
  background: var(--card);
  transition: transform .2s;
}

.bhe-29a__btn span {
  position: relative;
  z-index: 2;
}

.bhe-29a__btn::before,
.bhe-29a__btn::after {
  content: "";
  position: absolute;
  left: 50%;
  top: 50%;
  width: 150%;
  aspect-ratio: 1;
  transform: translate(-50%,-50%);
  background: conic-gradient(#ff3d81,#ffb03d,#f5f13d,#3dff8b,#3dc9ff,#8b3dff,#ff3d81);
  animation: bhe-29a-spin 4s linear infinite;
}

.bhe-29a__btn::before {
  z-index: 0;
  border-radius: 14px;
}

.bhe-29a__btn::after {
  z-index: -1;
  filter: blur(18px);
  opacity: .55;
}

.bhe-29a__cover {
  position: absolute;
  inset: 2px;
  border-radius: 12px;
  background: var(--card);
  z-index: 1;
}

.bhe-29a__btn:hover {
  transform: translateY(-2px);
}

.bhe-29a__btn:hover::before,
.bhe-29a__btn:hover::after {
  animation-duration: 1.4s;
}

.bhe-29a__btn:hover::after {
  opacity: .85;
}

.bhe-29a__btn:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 4px;
}

@keyframes bhe-29a-spin {
  to {
    transform: translate(-50%,-50%) rotate(360deg);
  }
}

@media (prefers-reduced-motion: reduce) {
  .bhe-29a__btn::before,
    .bhe-29a__btn::after {
    animation: none;
  }
}

.bhe-29b,
.bhe-29b *,
.bhe-29b *::before,
.bhe-29b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-29b {
  --card: #0e1220;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #060810;
}

.bhe-29b__btn {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  font-size: 16px;
  font-weight: 800;
  color: #fff;
  padding: 16px 40px;
  border: none;
  border-radius: 9999px;
  cursor: pointer;
  background: var(--card);
  transition: transform .2s;
}

.bhe-29b__btn>span:last-child {
  position: relative;
  z-index: 2;
}

.bhe-29b__btn::before {
  content: "";
  position: absolute;
  left: 50%;
  top: 50%;
  width: 160%;
  aspect-ratio: 1;
  transform: translate(-50%,-50%);
  background: conic-gradient(from 0deg,#3d7bff,#b03dff,#3d7bff);
  animation: bhe-29b-spin 3s linear infinite;
  z-index: 0;
}

.bhe-29b__cover {
  position: absolute;
  inset: 2px;
  border-radius: 9999px;
  background: var(--card);
  z-index: 1;
}

.bhe-29b__btn:hover {
  transform: translateY(-2px);
}

.bhe-29b__btn:hover::before {
  animation-duration: 1.2s;
}

.bhe-29b__btn:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 4px;
}

@keyframes bhe-29b-spin {
  to {
    transform: translate(-50%,-50%) rotate(360deg);
  }
}

@media (prefers-reduced-motion: reduce) {
  .bhe-29b__btn::before {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — pure CSS; all designs for this title are driven entirely by the css field. */
```
