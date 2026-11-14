---
source: "codefronts"
url: "https://codefronts.com/motion/css-animated-buttons/css-hamburger-to-close-button/"
title: "CSS Hamburger To Close Button"
section: "motion"
category: "css-animated-buttons"
category_name: "CSS Animated Buttons"
description: "The classic three-line hamburger menu icon morphs smoothly into an × close icon via CSS transform transitions — no SVG swaps, just rotating and fading three…"
has_js: "true"
---

Here's a working CSS Animated Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Hamburger To Close Button
Source: https://codefronts.com/motion/css-animated-buttons/css-hamburger-to-close-button/

The classic three-line hamburger menu icon morphs smoothly into an × close icon via CSS transform transitions — no SVG swaps, just rotating and fading three spans.
## HTML
```html
<div class="ab-14">
  <div class="ab-14__nav">
    <span class="ab-14__brand">MyApp</span>
    <button class="ab-14__btn" id="ab-14-btn" aria-label="Toggle navigation" aria-expanded="false">
      <span class="ab-14__bar"></span>
      <span class="ab-14__bar"></span>
      <span class="ab-14__bar"></span>
    </button>
  </div>
  <div class="ab-14__menu" id="ab-14-menu" aria-hidden="true">
    <a class="ab-14__link" href="#">Home</a>
    <a class="ab-14__link" href="#">Features</a>
    <a class="ab-14__link" href="#">Pricing</a>
    <a class="ab-14__link" href="#">Docs</a>
  </div>
</div>
```
## CSS
```css
.ab-14,
.ab-14 *,
.ab-14 *::before,
.ab-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ab-14 ::selection {
  background: #7c3aed;
  color: #fff;
}

.ab-14 {
  font-family: system-ui,sans-serif;
  background: #0f172a;
  min-height: 100vh;
}

.ab-14__nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem 1.5rem;
  border-bottom: 1px solid rgba(255,255,255,.07);
}

.ab-14__brand {
  font-size: 1.1rem;
  font-weight: 800;
  color: #f1f5f9;
  letter-spacing: -.01em;
}

.ab-14__btn {
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 6px;
  width: 40px;
  height: 40px;
  background: rgba(255,255,255,.06);
  border: 1px solid rgba(255,255,255,.1);
  border-radius: 8px;
  cursor: pointer;
  outline: none;
  align-items: center;
  transition: background .25s;
}

.ab-14__btn:hover {
  background: rgba(255,255,255,.1);
}

.ab-14__btn.is-open {
  background: rgba(124,58,237,.2);
  border-color: rgba(124,58,237,.4);
}

.ab-14__bar {
  display: block;
  width: 22px;
  height: 2px;
  background: #e2e8f0;
  border-radius: 2px;
  transform-origin: center;
  transition: transform .3s cubic-bezier(.4,0,.2,1),opacity .3s,background .3s;
}

.ab-14__btn.is-open .ab-14__bar:nth-child(1) {
  transform: translateY(8px) rotate(45deg);
  background: #a78bfa;
}

.ab-14__btn.is-open .ab-14__bar:nth-child(2) {
  opacity: 0;
  transform: scaleX(0);
}

.ab-14__btn.is-open .ab-14__bar:nth-child(3) {
  transform: translateY(-8px) rotate(-45deg);
  background: #a78bfa;
}

.ab-14__menu {
  display: flex;
  flex-direction: column;
  overflow: hidden;
  max-height: 0;
  transition: max-height .4s cubic-bezier(.4,0,.2,1),opacity .3s;
  opacity: 0;
  padding: 0 1.5rem;
}

.ab-14__menu.is-open {
  max-height: 200px;
  opacity: 1;
  padding: 1rem 1.5rem;
}

.ab-14__link {
  display: block;
  padding: .6rem 0;
  font-size: .95rem;
  font-weight: 600;
  color: #94a3b8;
  text-decoration: none;
  border-bottom: 1px solid rgba(255,255,255,.05);
  transition: color .2s;
}

.ab-14__link:last-child {
  border-bottom: none;
}

.ab-14__link:hover {
  color: #f1f5f9;
}

@media (prefers-reduced-motion: reduce) {
  .ab-14__bar,
    .ab-14__menu {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  var btn=document.getElementById('ab-14-btn');
  var menu=document.getElementById('ab-14-menu');
  if(!btn||!menu)return;
  btn.addEventListener('click',function(){
    var open=btn.classList.toggle('is-open');
    menu.classList.toggle('is-open',open);
    btn.setAttribute('aria-expanded',open.toString());
    menu.setAttribute('aria-hidden',(!open).toString());
  });
})();
```
