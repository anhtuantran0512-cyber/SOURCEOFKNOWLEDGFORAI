---
source: "codefronts"
url: "https://codefronts.com/components/css-3d-tilt-hover-cards/flip-to-back-3d-tilt-card/"
title: "Flip-to-Back 3D Tilt Card"
section: "components"
category: "css-3d-tilt-hover-cards"
category_name: "CSS 3D Tilt Hover Cards"
description: "Tilt and flip in one transform: the card follows the cursor like any tilt card, but click (or press Enter/Space) and it swings a full 180° to reveal contact…"
has_js: "true"
---

Here's a working CSS 3D Tilt Hover Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Flip-to-Back 3D Tilt Card
Source: https://codefronts.com/components/css-3d-tilt-hover-cards/flip-to-back-3d-tilt-card/

Tilt and flip in one transform: the card follows the cursor like any tilt card, but click (or press Enter/Space) and it swings a full 180° to reveal contact details on its back — and keeps tilting while flipped. The trick is composing rotateY(flip + tilt) as a single calc(), never two competing transforms.
## HTML
```html
<section class="thc-12" aria-label="Flip-to-back tilt card demo">
  <div class="thc-12__scene">
    <div class="thc-12__carrier">
      <article class="thc-12__face thc-12__face--front" aria-hidden="false">
        <p class="thc-12__kicker">FREELANCE</p>
        <h3 class="thc-12__name">Jonah Reyes</h3>
        <p class="thc-12__role">Motion &amp; Brand Designer</p>
        <button class="thc-12__flipbtn" type="button" aria-pressed="false">Contact &#8635;</button>
      </article>
      <article class="thc-12__face thc-12__face--back" aria-hidden="true">
        <p class="thc-12__kicker">SAY HELLO</p>
        <ul class="thc-12__contacts">
          <li>[email protected]</li>
          <li>+1 (415) 555-0132</li>
          <li>@jonahmakes</li>
        </ul>
        <button class="thc-12__flipbtn thc-12__flipbtn--back" type="button" aria-pressed="true">Back &#8634;</button>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
.thc-12,
.thc-12 *,
.thc-12 *::before,
.thc-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.thc-12 {
  --acc: oklch(0.75 0.14 80);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(80% 90% at 70% 20%,oklch(0.25 0.05 80 / .7),transparent 60%),oklch(0.15 0.015 270);
}

.thc-12 .thc-12__scene {
  perspective: 1100px;
  width: min(300px,100%);
}

.thc-12 .thc-12__carrier {
  position: relative;
  height: 200px;
  transform-style: preserve-3d;
  transform: rotateX(var(--rx,0deg)) rotateY(calc(var(--flip,0deg) + var(--ry,0deg)));
  transition: transform .7s cubic-bezier(.3,.8,.3,1.1);
}

.thc-12 .thc-12__carrier.is-live {
  transition: transform .09s linear;
}

.thc-12 .thc-12__carrier.is-flipping {
  transition: transform .7s cubic-bezier(.3,.8,.3,1.1);
}

.thc-12 .thc-12__face {
  position: absolute;
  inset: 0;
  border-radius: 18px;
  padding: 26px;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  background: linear-gradient(160deg,oklch(0.23 0.03 80),oklch(0.17 0.02 270));
  border: 1px solid color-mix(in oklab,var(--acc) 35%,transparent);
  box-shadow: 0 26px 54px -26px rgba(0,0,0,.8);
  display: flex;
  flex-direction: column;
}

.thc-12 .thc-12__face--back {
  transform: rotateY(180deg);
}

.thc-12 .thc-12__kicker {
  font: 700 10px ui-monospace,monospace;
  letter-spacing: .2em;
  color: var(--acc);
}

.thc-12 .thc-12__name {
  margin-top: 12px;
  font-size: 24px;
  font-weight: 800;
  color: #fff;
}

.thc-12 .thc-12__role {
  margin-top: 4px;
  font-size: 13px;
  color: rgba(255,255,255,.6);
}

.thc-12 .thc-12__contacts {
  list-style: none;
  margin-top: 14px;
  display: flex;
  flex-direction: column;
  gap: 8px;
  font-size: 13.5px;
  color: rgba(255,255,255,.85);
}

.thc-12 .thc-12__flipbtn {
  margin-top: auto;
  align-self: flex-start;
  font: 600 12px 'Segoe UI',sans-serif;
  color: oklch(0.15 0.02 270);
  background: var(--acc);
  border: none;
  border-radius: 999px;
  padding: 9px 16px;
  cursor: pointer;
  transition: transform .2s ease;
}

.thc-12 .thc-12__flipbtn:hover {
  transform: scale(1.05);
}

.thc-12 .thc-12__flipbtn:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .thc-12 .thc-12__carrier {
    transition: none;
  }
}
```

## JavaScript
```js
(() => {
  const scene = document.querySelector('.thc-12 .thc-12__scene');
  if (!scene) return;
  const carrier = scene.querySelector('.thc-12__carrier');
  const faces = carrier.querySelectorAll('.thc-12__face');
  const btns = carrier.querySelectorAll('.thc-12__flipbtn');
  let flipped = false;
  const setFlip = (f) => {
    flipped = f;
    carrier.style.setProperty('--flip', f ? '180deg' : '0deg');
    faces[0].setAttribute('aria-hidden', String(f));
    faces[1].setAttribute('aria-hidden', String(!f));
    btns.forEach((b) => b.setAttribute('aria-pressed', String(f)));
    carrier.classList.add('is-flipping');          // force the slow bezier for the swing
    carrier.classList.remove('is-live');
    setTimeout(() => carrier.classList.remove('is-flipping'), 700);
  };
  btns.forEach((b) => b.addEventListener('click', () => setFlip(!flipped)));
  if (!matchMedia('(hover:hover) and (pointer:fine)').matches) return;
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const MAX = 10;
  scene.addEventListener('pointermove', (e) => {
    if (carrier.classList.contains('is-flipping')) return; // let the swing finish clean
    const r = scene.getBoundingClientRect();
    const px = (e.clientX - r.left) / r.width, py = (e.clientY - r.top) / r.height;
    const dir = flipped ? -1 : 1;                  // pointer-left is back-face-right
    carrier.style.setProperty('--rx', ((0.5 - py) * MAX).toFixed(2) + 'deg');
    carrier.style.setProperty('--ry', (dir * (px - 0.5) * MAX).toFixed(2) + 'deg');
    carrier.classList.add('is-live');
  });
  scene.addEventListener('pointerleave', () => {
    carrier.classList.remove('is-live');
    carrier.style.setProperty('--rx', '0deg');
    carrier.style.setProperty('--ry', '0deg');
  });
})();
```
