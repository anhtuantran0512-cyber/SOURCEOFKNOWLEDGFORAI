---
source: "codefronts"
url: "https://codefronts.com/motion/css-hover-effects/css-magnetic-cursor-pull-hover-effect/"
title: "CSS Magnetic Cursor Pull Hover Effect"
section: "motion"
category: "css-hover-effects"
category_name: "CSS Hover Effects"
description: "Buttons and icons that magnetically attract to the cursor when nearby, snapping back smoothly when the cursor leaves — four magnetic element types."
has_js: "true"
---

Here's a working CSS Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Magnetic Cursor Pull Hover Effect
Source: https://codefronts.com/motion/css-hover-effects/css-magnetic-cursor-pull-hover-effect/

Buttons and icons that magnetically attract to the cursor when nearby, snapping back smoothly when the cursor leaves — four magnetic element types.
## HTML
```html
<div class="hv-30">
  <p class="hv-30__label">Magnetic Cursor Pull — 4 Types</p>
  <div class="hv-30__grid">

    <div class="hv-30__wrap">
      <button class="hv-30__btn hv-30__btn--primary hv-30__magnet" data-strength="0.35" data-radius="80">
        <span class="hv-30__btn-inner hv-30__magnet-inner" data-strength="0.55">Get Started</span>
      </button>
      <span class="hv-30__caption">Primary CTA</span>
    </div>

    <div class="hv-30__wrap">
      <button class="hv-30__btn hv-30__btn--outline hv-30__magnet" data-strength="0.4" data-radius="90">
        <span class="hv-30__btn-inner hv-30__magnet-inner" data-strength="0.6">Learn More</span>
      </button>
      <span class="hv-30__caption">Outline Button</span>
    </div>

    <div class="hv-30__wrap">
      <div class="hv-30__icon-btn hv-30__magnet" data-strength="0.5" data-radius="70">
        <span class="hv-30__magnet-inner" data-strength="0.75">★</span>
      </div>
      <span class="hv-30__caption">Icon Pull</span>
    </div>

    <div class="hv-30__wrap">
      <a class="hv-30__pill hv-30__magnet" href="#" data-strength="0.3" data-radius="100">
        <span class="hv-30__magnet-inner" data-strength="0.5">View Project →</span>
      </a>
      <span class="hv-30__caption">Pill Link</span>
    </div>

  </div>
</div>
```
## CSS
```css
.hv-30,
.hv-30 *,
.hv-30 *::before,
.hv-30 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.hv-30 {
  font-family: system-ui, sans-serif;
  background: #090912;
  padding: 3rem 2rem;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2rem;
}

.hv-30__label {
  color: #444;
  font-size: .72rem;
  letter-spacing: .15em;
  text-transform: uppercase;
}

.hv-30__grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 3.5rem 4rem;
  place-items: center;
  padding: 2rem;
}

.hv-30__wrap {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
}

.hv-30__caption {
  color: #333;
  font-size: .68rem;
  letter-spacing: .1em;
  text-transform: uppercase;
}
/* Magnetic elements */

.hv-30__magnet {
  will-change: transform;
  transition: transform .45s cubic-bezier(.23,1,.32,1);
  cursor: pointer;
}

.hv-30__magnet-inner {
  display: inline-block;
  will-change: transform;
  transition: transform .45s cubic-bezier(.23,1,.32,1);
  pointer-events: none;
}
/* Button styles */

.hv-30__btn {
  background: #5b4fcf;
  color: #fff;
  border: none;
  border-radius: 50px;
  padding: .9rem 2.4rem;
  font-size: 1rem;
  font-weight: 600;
  letter-spacing: .02em;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 6px 28px rgba(91,79,207,.4);
}

.hv-30__btn--outline {
  background: transparent;
  border: 2px solid #5b4fcf;
  color: #a99ef7;
  box-shadow: none;
}

.hv-30__btn--outline:hover {
  box-shadow: 0 6px 28px rgba(91,79,207,.25);
}
/* Icon button */

.hv-30__icon-btn {
  width: 64px;
  height: 64px;
  border-radius: 50%;
  background: linear-gradient(135deg, #7c6af7, #f764a8);
  color: #fff;
  font-size: 1.6rem;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 6px 24px rgba(124,106,247,.4);
}
/* Pill link */

.hv-30__pill {
  display: inline-flex;
  align-items: center;
  padding: .65rem 1.8rem;
  background: rgba(255,255,255,.06);
  border: 1px solid rgba(255,255,255,.12);
  border-radius: 50px;
  color: #ccc;
  text-decoration: none;
  font-size: .9rem;
  backdrop-filter: blur(6px);
  transition: transform .45s cubic-bezier(.23,1,.32,1), background .3s, border-color .3s;
}

.hv-30__pill:hover {
  background: rgba(255,255,255,.1);
  border-color: rgba(255,255,255,.22);
  color: #fff;
}

@media (max-width: 500px) {
  .hv-30__grid {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .hv-30__magnet,
    .hv-30__magnet-inner {
    transition: none !important;
  }
}
```

## JavaScript
```js
(function () {
  if (window.matchMedia('(pointer: coarse)').matches) return;

  const magnets = document.querySelectorAll('.hv-30__magnet');

  function handleMove(e, el) {
    const rect = el.getBoundingClientRect();
    const cx = rect.left + rect.width  / 2;
    const cy = rect.top  + rect.height / 2;
    const dx = e.clientX - cx;
    const dy = e.clientY - cy;
    const dist = Math.sqrt(dx * dx + dy * dy);
    const radius   = parseFloat(el.dataset.radius)   || 80;
    const strength = parseFloat(el.dataset.strength)  || 0.35;

    if (dist < radius) {
      const pull = (1 - dist / radius);
      const tx = dx * strength * pull;
      const ty = dy * strength * pull;
      el.style.transform = `translate(${tx}px, ${ty}px)`;

      const inner = el.querySelector('.hv-30__magnet-inner');
      if (inner) {
        const is = parseFloat(inner.dataset.strength) || 0.5;
        inner.style.transform = `translate(${dx * is * pull}px, ${dy * is * pull}px)`;
      }
    } else {
      el.style.transform = '';
      const inner = el.querySelector('.hv-30__magnet-inner');
      if (inner) inner.style.transform = '';
    }
  }

  function handleLeave(el) {
    el.style.transform = '';
    const inner = el.querySelector('.hv-30__magnet-inner');
    if (inner) inner.style.transform = '';
  }

  magnets.forEach(el => {
    document.addEventListener('mousemove', e => handleMove(e, el));
    el.addEventListener('mouseleave', () => handleLeave(el));
  });
})();
```
