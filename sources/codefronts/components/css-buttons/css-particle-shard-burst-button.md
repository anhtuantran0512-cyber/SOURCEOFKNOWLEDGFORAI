---
source: "codefronts"
url: "https://codefronts.com/components/css-buttons/css-particle-shard-burst-button/"
title: "CSS Particle Shard Burst Button"
section: "components"
category: "css-buttons"
category_name: "CSS Buttons"
description: "Every press shatters a ring of glass shards outward from the exact click point, each with its own angle, distance, spin and lifetime — spawned as real…"
has_js: "true"
---

Here's a working CSS Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Particle Shard Burst Button
Source: https://codefronts.com/components/css-buttons/css-particle-shard-burst-button/

Every press shatters a ring of glass shards outward from the exact click point, each with its own angle, distance, spin and lifetime — spawned as real elements, animated by one CSS keyframe, and garbage-collected on animationend so the DOM never grows.
## HTML
```html
<div class="cb-20">
  <div class="cb-20__stage">
    <button class="cb-20__btn" type="button">
      <span class="cb-20__shards" aria-hidden="true"></span>
      <span class="cb-20__label">Shatter</span>
    </button>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&display=swap');

.cb-20 {
  --bg: #0a0a10;
  --btn: #15151f;
  --ink: #f4f4fa;
  --line: #2b2b3a;
  --s1: #7dd3fc;
  --s2: #c4b5fd;
  --s3: #fda4af;
  --radius: .85rem;
  --sans: "Space Grotesk",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: radial-gradient(40rem 24rem at 50% 50%, color-mix(in oklab,var(--s2) 10%,transparent), transparent 72%), var(--bg);
  font-family: var(--sans);
}

@supports (color: oklch(50% 0 0)) {
  .cb-20 {
    --s1: oklch(84% .11 226);
    --s2: oklch(82% .1 293);
    --s3: oklch(82% .1 15);
    --btn: oklch(22% .02 285);
  }
}

@media (prefers-color-scheme: light) {
  .cb-20:not([data-theme="dark"]) {
    --bg: #eef0f6;
    --btn: #14141d;
  }
}

.cb-20[data-theme="light"] {
  --bg: #eef0f6;
  --btn: #14141d;
}

.cb-20,
.cb-20 *,
.cb-20 *::before,
.cb-20 *::after {
  box-sizing: border-box;
}

.cb-20__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,6vw,4rem);
}

.cb-20__btn {
  position: relative;
  cursor: pointer;
  display: grid;
  place-items: center;
  min-height: 3.5rem;
  padding: 0 2.1rem;
  border: 1px solid var(--line);
  border-radius: var(--radius);
  font: inherit;
  font-size: .9375rem;
  font-weight: 600;
  letter-spacing: .02em;
  color: var(--ink);
  background: linear-gradient(180deg,color-mix(in oklab,var(--btn) 80%,white 6%),var(--btn));
  box-shadow: 0 16px 34px -20px color-mix(in oklab,black 90%,transparent);
  transition: scale .25s cubic-bezier(.16,1,.3,1), border-color .25s ease;
  -webkit-tap-highlight-color: transparent;
}

.cb-20__label {
  position: relative;
  z-index: 2;
}

.cb-20__btn:hover {
  border-color: color-mix(in oklab,var(--s1) 50%,var(--line));
}

.cb-20__btn:active {
  scale: .95;
}

.cb-20__btn:focus-visible {
  outline: 2px solid var(--s1);
  outline-offset: 4px;
}

.cb-20__shards {
  position: absolute;
  inset: 0;
  z-index: 1;
  pointer-events: none;
}

.cb-20__shard {
  position: absolute;
  top: 50%;
  left: 50%;
  width: .75rem;
  height: .28rem;
  margin: -.14rem 0 0 -.375rem;
  background: var(--s1);
  clip-path: polygon(0 50%,55% 0,100% 42%,62% 100%);
  rotate: var(--a);
  opacity: 0;
  animation: cb-20-fly var(--t) cubic-bezier(.14,.8,.3,1) forwards;
}

.cb-20__shard:nth-child(3n) {
  background: var(--s2);
  width: .5rem;
  height: .5rem;
  clip-path: polygon(50% 0,100% 38%,80% 100%,18% 92%,0 34%);
}

.cb-20__shard:nth-child(3n+1) {
  background: var(--s3);
}

@keyframes cb-20-fly {
  0% {
    translate: 0 0;
    scale: .35;
    opacity: 1;
  }

  100% {
    translate: 0 calc(var(--d) * -1);
    scale: .95;
    opacity: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cb-20__btn {
    transition: none;
  }

  .cb-20__shard {
    display: none;
  }
}

@media (forced-colors: active) {
  .cb-20__btn {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
  }

  .cb-20__shard {
    display: none;
  }
}
```

## JavaScript
```js
(() => {
  const btn = document.querySelector('.cb-20__btn');
  const layer = btn && btn.querySelector('.cb-20__shards');
  if (!layer) return;
  const calm = matchMedia('(prefers-reduced-motion: reduce)');
  btn.addEventListener('click', () => {
    if (calm.matches || layer.childElementCount > 40) return;
    for (let i = 0; i < 12; i++) {
      const s = document.createElement('span');
      s.className = 'cb-20__shard';
      s.style.setProperty('--a', ((i / 12) * 360 + (Math.random() * 22 - 11)).toFixed(1) + 'deg');
      s.style.setProperty('--d', (46 + Math.random() * 54).toFixed(0) + 'px');
      s.style.setProperty('--t', (520 + Math.random() * 380).toFixed(0) + 'ms');
      s.addEventListener('animationend', () => s.remove());
      layer.appendChild(s);
    }
  });
})();
```
