---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-gradient-text/css-click-ripple-gradient-text-interaction/"
title: "CSS Click Ripple Gradient Text Interaction"
section: "design-styles"
category: "css-gradient-text"
category_name: "CSS Gradient Text Designs"
description: "Clicking the gradient headline spawns a ripple ring at the click point while the headline flashes brighter, demonstrating CSS keyframe injection via JavaScript."
has_js: "true"
---

Here's a working CSS Gradient Text Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Click Ripple Gradient Text Interaction
Source: https://codefronts.com/design-styles/css-gradient-text/css-click-ripple-gradient-text-interaction/

Clicking the gradient headline spawns a ripple ring at the click point while the headline flashes brighter, demonstrating CSS keyframe injection via JavaScript.
## HTML
```html
<div class="gt-16">
  <span class="gt-16__label">Click / tap gradient text</span>
  <span class="gt-16__hint">↓ click the word ↓</span>
  <div class="gt-16__btn" id="gt-16-main">
    CLICK
    <div class="gt-16__ripples" id="gt-16-ripples"></div>
  </div>
  <div class="gt-16__score">Clicks: <span id="gt-16-count">0</span></div>
  <div class="gt-16__palette" id="gt-16-palette">
    <div class="gt-16__swatch" data-grad="linear-gradient(90deg,#ff6b6b,#ffd93d,#6bcb77,#4d96ff,#a855f7,#ff6b6b)"></div>
    <div class="gt-16__swatch" data-grad="linear-gradient(90deg,#6bcb77,#4d96ff,#a855f7,#ec4899,#6bcb77)"></div>
    <div class="gt-16__swatch" data-grad="linear-gradient(90deg,#a855f7,#ec4899,#f43f5e,#fb923c,#a855f7)"></div>
    <div class="gt-16__swatch" data-grad="linear-gradient(90deg,#00f5a0,#00d9f5,#4d96ff,#a855f7,#00f5a0)"></div>
  </div>
</div>
```
## CSS
```css
.gt-16,
.gt-16 *,
.gt-16 *::before,
.gt-16 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.gt-16 {
  --bg: #f8f8f4;
  font-family: 'Outfit', sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 2rem;
  padding: 3rem 2rem;
  user-select: none;
}

.gt-16__label {
  font-size: .7rem;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: #ddd;
}

.gt-16__hint {
  font-size: .75rem;
  color: #ccc;
  letter-spacing: .1em;
}

.gt-16__btn {
  font-size: clamp(3rem, 12vw, 8rem);
  font-weight: 900;
  line-height: 1;
  letter-spacing: .02em;
  background: linear-gradient(90deg, #ff6b6b, #ffd93d, #6bcb77, #4d96ff, #a855f7, #ff6b6b);
  background-size: 300% 100%;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  cursor: pointer;
  position: relative;
  transition: transform .15s ease;
  background-position: 0% center;
  animation: gt-16-drift 8s linear infinite;
}

.gt-16__btn:active {
  transform: scale(.97);
}

.gt-16__btn.is-burst {
  animation: gt-16-burst .5s ease forwards;
}

.gt-16__ripples {
  position: absolute;
  inset: 0;
  pointer-events: none;
  overflow: visible;
}

.gt-16__ripple {
  position: absolute;
  border-radius: 50%;
  transform: translate(-50%, -50%) scale(0);
  animation: gt-16-ripple .8s ease-out forwards;
  pointer-events: none;
  opacity: .5;
}

.gt-16__score {
  font-size: 1rem;
  font-weight: 800;
  color: #ddd;
  letter-spacing: .1em;
}

.gt-16__score span {
  background: linear-gradient(90deg, #ff6b6b, #a855f7);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.gt-16__palette {
  display: flex;
  gap: .5rem;
}

.gt-16__swatch {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  cursor: pointer;
  transition: transform .2s;
  border: 2px solid white;
}

.gt-16__swatch:hover {
  transform: scale(1.2);
}

.gt-16__swatch:nth-child(1) {
  background: linear-gradient(135deg, #ff6b6b, #ffd93d);
}

.gt-16__swatch:nth-child(2) {
  background: linear-gradient(135deg, #6bcb77, #4d96ff);
}

.gt-16__swatch:nth-child(3) {
  background: linear-gradient(135deg, #a855f7, #ec4899);
}

.gt-16__swatch:nth-child(4) {
  background: linear-gradient(135deg, #00f5a0, #00d9f5);
}

@keyframes gt-16-drift {
  0% {
    background-position: 0% center;
  }

  100% {
    background-position: 300% center;
  }
}

@keyframes gt-16-burst {
  0% {
    transform: scale(1);
    filter: brightness(1);
  }

  30% {
    transform: scale(1.06);
    filter: brightness(1.3);
  }

  100% {
    transform: scale(1);
    filter: brightness(1);
  }
}

@keyframes gt-16-ripple {
  0% {
    transform: translate(-50%, -50%) scale(0);
    opacity: .6;
  }

  100% {
    transform: translate(-50%, -50%) scale(6);
    opacity: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .gt-16__btn {
    animation: none;
  }

  .gt-16__btn.is-burst {
    animation: none;
  }

  .gt-16__ripple {
    animation: none;
    display: none;
  }
}
```

## JavaScript
```js
(function() {
  const btn = document.getElementById('gt-16-main');
  const ripples = document.getElementById('gt-16-ripples');
  const countEl = document.getElementById('gt-16-count');
  const palette = document.getElementById('gt-16-palette');
  let count = 0;
  const colors = ['#ff6b6b','#ffd93d','#6bcb77','#4d96ff','#a855f7','#ec4899','#00f5a0'];
  btn.addEventListener('click', (e) => {
    count++;
    countEl.textContent = count;
    const rect = btn.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    const r = document.createElement('div');
    r.className = 'gt-16__ripple';
    const c = colors[Math.floor(Math.random() * colors.length)];
    r.style.cssText = `left:${x}px;top:${y}px;width:80px;height:80px;background:${c};`;
    ripples.appendChild(r);
    btn.classList.remove('is-burst');
    void btn.offsetWidth;
    btn.classList.add('is-burst');
    r.addEventListener('animationend', () => r.remove());
  });
  palette.querySelectorAll('.gt-16__swatch').forEach(sw => {
    sw.addEventListener('click', () => {
      btn.style.backgroundImage = sw.dataset.grad;
    });
  });
})();
```
