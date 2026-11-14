---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-liquid-glass-effects/liquid-glass-button-with-glossy-highlight/"
title: "Liquid Glass Button with Glossy Highlight"
section: "design-styles"
category: "css-liquid-glass-effects"
category_name: "CSS Liquid Glass Effects"
description: "A high-converting capsule CTA in the macOS Tahoe / iOS 26 language: a translucent pill with a hairline top rim-light, a soft inner glow, and — on hover — a…"
has_js: "false"
---

Here's a working CSS Liquid Glass Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Liquid Glass Button with Glossy Highlight
Source: https://codefronts.com/design-styles/css-liquid-glass-effects/liquid-glass-button-with-glossy-highlight/

A high-converting capsule CTA in the macOS Tahoe / iOS 26 language: a translucent pill with a hairline top rim-light, a soft inner glow, and — on hover — a specular light beam that sweeps across the surface like light passing through a wet lens. Pure CSS, no JavaScript.
## HTML
```html
<section class="lg-02" aria-label="Liquid glass buttons">
  <div class="lg-02__row">
    <button class="lg-02__btn lg-02__btn--primary" type="button">Get started</button>
    <button class="lg-02__btn" type="button">Learn more</button>
  </div>
</section>
```
## CSS
```css
.lg-02,
.lg-02 *,
.lg-02 *::before,
.lg-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lg-02 {
  --accent: oklch(0.62 0.2 275);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  background: url('https://picsum.photos/seed/lgbtn/1200/900') center/cover fixed,#141024;
}

.lg-02__row {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.lg-02__btn {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  font-size: 16px;
  font-weight: 700;
  letter-spacing: .01em;
  color: #fff;
  padding: 16px 34px;
  border-radius: 9999px;
  border: 1px solid rgba(255,255,255,.4);
  cursor: pointer;
  background: color-mix(in oklab,white 14%,transparent);
  backdrop-filter: blur(16px) saturate(170%);
  -webkit-backdrop-filter: blur(16px) saturate(170%);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.6),inset 0 -8px 18px -10px rgba(0,0,0,.5),0 14px 30px -16px rgba(0,0,0,.6);
  transition: transform .18s,box-shadow .25s;
}

.lg-02__btn--primary {
  background: linear-gradient(180deg,color-mix(in oklab,var(--accent) 88%,white 12%),var(--accent));
  border-color: color-mix(in oklab,var(--accent) 40%,white);
}

.lg-02__btn::after {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 60%;
  height: 100%;
  background: linear-gradient(105deg,transparent 20%,rgba(255,255,255,.55) 50%,transparent 80%);
  transform: translateX(-160%) skewX(-12deg);
  transition: transform .7s cubic-bezier(.2,.8,.2,1);
  pointer-events: none;
  z-index: 2;
}

.lg-02__btn:hover {
  transform: translateY(-2px);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.7),inset 0 -8px 18px -10px rgba(0,0,0,.5),0 20px 40px -16px rgba(0,0,0,.7);
}

.lg-02__btn:hover::after {
  transform: translateX(230%) skewX(-12deg);
}

.lg-02__btn:active {
  transform: translateY(0) scale(.97);
}

.lg-02__btn:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .lg-02__btn,
    .lg-02__btn::after {
    transition: none;
  }

  .lg-02__btn:hover::after {
    transform: translateX(-160%) skewX(-12deg);
  }
}
```

## JavaScript
```js
/* No JavaScript — the capsule uses backdrop-filter for the frost, layered inset shadows for glass thickness, and a ::after diagonal gradient that transitions across on :hover for the specular sweep. */
```
