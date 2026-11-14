---
source: "codefronts"
url: "https://codefronts.com/motion/css-background-animations/cursor-spotlight-follow-effect/"
title: "Cursor Spotlight Follow Effect"
section: "motion"
category: "css-background-animations"
category_name: "CSS Background Animations"
description: "A torch dragged across a dark surface."
has_js: "true"
---

Here's a working CSS Background Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Cursor Spotlight Follow Effect
Source: https://codefronts.com/motion/css-background-animations/cursor-spotlight-follow-effect/

A torch dragged across a dark surface. Two lines of pointer JavaScript write --mx / --my; everything else — the light falloff, the mask that reveals a hidden colour layer underneath, the grid that brightens only inside the beam — is CSS. It idles on its own orbit until you move, so it is never a dead rectangle on touch devices, and it hard-stops for reduced-motion users.
## HTML
```html
<section class="bga-02" id="bga-02-root" aria-label="Cursor spotlight follow background demo">
  <div class="bga-02__grid" aria-hidden="true"></div>
  <div class="bga-02__reveal" aria-hidden="true">
    <img class="bga-02__photo" src="https://images.unsplash.com/photo-1519681393784-d120267933ba?q=80&w=1800&auto=format&fit=crop" alt="" width="1800" height="1200" loading="lazy" decoding="async">
  </div>
  <div class="bga-02__beam" aria-hidden="true"></div>
  <div class="bga-02__vig" aria-hidden="true"></div>

  <div class="bga-02__stage">
    <div class="bga-02__panel">
      <p class="bga-02__eyebrow">Pointer-reactive · 02</p>
      <h1 class="bga-02__title">Move the light.<br>The surface answers.</h1>
      <p class="bga-02__sub">Two custom properties are written on pointermove. The falloff, the mask, the grid glow and the easing are all CSS — the main thread does almost nothing.</p>
      <ul class="bga-02__meta">
        <li><b>0</b><span>rAF loops</span></li>
        <li><b>2</b><span>properties written</span></li>
        <li><b>1</b><span>passive listener</span></li>
      </ul>
    </div>
    <p class="bga-02__hint">Move your cursor — or wait, and it orbits on its own.</p>
  </div>
</section>
```
## CSS
```css
@property --bga-02-mx {
  syntax: '<percentage>';
  inherits: true;
  initial-value: 50%;
}

@property --bga-02-my {
  syntax: '<percentage>';
  inherits: true;
  initial-value: 44%;
}

.bga-02,
.bga-02 *,
.bga-02 *::before,
.bga-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bga-02 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  overflow: hidden;
  isolation: isolate;
  --bga-02-bg: oklch(0.16 0.024 265);
  --bga-02-acc: oklch(0.78 0.16 232);
  --bga-02-acc2: oklch(0.7 0.19 320);
  --bga-02-r: clamp(240px,32vw,460px);
  --bga-02-mx: 50%;
  --bga-02-my: 44%;
  background: var(--bga-02-bg);
  color: oklch(0.97 0.01 250);
  font-family: ui-sans-serif,system-ui,-apple-system,'Segoe UI',sans-serif;
  -webkit-font-smoothing: antialiased;
  transition: --bga-02-mx .45s cubic-bezier(.16,1,.3,1),--bga-02-my .45s cubic-bezier(.16,1,.3,1);
}

.bga-02.is-idle {
  animation: bga-02-orbit 16s ease-in-out infinite;
}

@keyframes bga-02-orbit {
  0% {
    --bga-02-mx: 26%;
    --bga-02-my: 32%;
  }

  25% {
    --bga-02-mx: 74%;
    --bga-02-my: 26%;
  }

  50% {
    --bga-02-mx: 80%;
    --bga-02-my: 74%;
  }

  75% {
    --bga-02-mx: 22%;
    --bga-02-my: 70%;
  }

  100% {
    --bga-02-mx: 26%;
    --bga-02-my: 32%;
  }
}

.bga-02__grid {
  position: absolute;
  inset: 0;
  opacity: .5;
  background-image: linear-gradient(oklch(1 0 0/.07) 1px,transparent 1px),linear-gradient(90deg,oklch(1 0 0/.07) 1px,transparent 1px);
  background-size: 56px 56px;
}

.bga-02__reveal {
  position: absolute;
  inset: 0;
  background: linear-gradient(90deg,color-mix(in oklab,var(--bga-02-acc) 30%,transparent),color-mix(in oklab,var(--bga-02-acc2) 34%,transparent)), linear-gradient(oklch(1 0 0/.3) 1px,transparent 1px), linear-gradient(90deg,oklch(1 0 0/.3) 1px,transparent 1px);
  background-size: 100% 100%,56px 56px,56px 56px;
  -webkit-mask-image: radial-gradient(circle var(--bga-02-r) at var(--bga-02-mx) var(--bga-02-my),oklch(0 0 0) 0 38%,transparent 74%);
  mask-image: radial-gradient(circle var(--bga-02-r) at var(--bga-02-mx) var(--bga-02-my),oklch(0 0 0) 0 38%,transparent 74%);
}

.bga-02__photo {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  opacity: .62;
  mix-blend-mode: luminosity;
}

.bga-02__beam {
  position: absolute;
  inset: 0;
  mix-blend-mode: screen;
  background: radial-gradient(circle var(--bga-02-r) at var(--bga-02-mx) var(--bga-02-my),
      color-mix(in oklab,var(--bga-02-acc) 46%,transparent) 0%,
      color-mix(in oklab,var(--bga-02-acc) 14%,transparent) 42%,transparent 70%);
}

.bga-02__vig {
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: radial-gradient(130% 110% at 50% 40%,transparent 40%,oklch(0.08 0.02 265/.85) 100%);
}

.bga-02__stage {
  position: relative;
  z-index: 3;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 22px;
  padding: clamp(22px,5vw,68px);
  pointer-events: none;
}

.bga-02__panel {
  width: min(100%,700px);
  display: grid;
  gap: 16px;
  padding: clamp(24px,3.4vw,44px);
  border-radius: 24px;
  text-align: center;
  justify-items: center;
  background: oklch(0.14 0.02 265/.55);
  border: 1px solid oklch(1 0 0/.12);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  box-shadow: 0 40px 90px -40px oklch(0 0 0/.9);
}

.bga-02__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .22em;
  text-transform: uppercase;
  color: var(--bga-02-acc);
}

.bga-02__title {
  font-size: clamp(28px,5.6vw,58px);
  font-weight: 640;
  line-height: 1.05;
  letter-spacing: -.045em;
  text-wrap: balance;
}

.bga-02__sub {
  max-width: 50ch;
  font-size: clamp(13.5px,1.3vw,16px);
  line-height: 1.6;
  color: oklch(0.9 0.01 250/.8);
  text-wrap: pretty;
}

.bga-02__meta {
  list-style: none;
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  justify-content: center;
  margin-top: 4px;
}

.bga-02__meta li {
  display: grid;
  gap: 2px;
  min-width: 112px;
  padding: 11px 16px;
  border-radius: 14px;
  background: oklch(1 0 0/.05);
  border: 1px solid oklch(1 0 0/.1);
}

.bga-02__meta b {
  font-size: 22px;
  font-weight: 660;
  letter-spacing: -.03em;
  color: var(--bga-02-acc);
}

.bga-02__meta span {
  font-size: 10.5px;
  letter-spacing: .09em;
  text-transform: uppercase;
  color: oklch(0.8 0.01 250/.65);
}

.bga-02__hint {
  font-size: 12.5px;
  color: oklch(0.85 0.01 250/.5);
}

@media (prefers-reduced-motion: reduce) {
  .bga-02 {
    transition: none;
  }

  .bga-02.is-idle {
    animation: none;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.getElementById('bga-02-root');
  if (!root) return;
  const calm = matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!calm) root.classList.add('is-idle');

  root.addEventListener('pointermove', (e) => {
    const r = root.getBoundingClientRect();
    root.classList.remove('is-idle');
    root.style.setProperty('--bga-02-mx', ((e.clientX - r.left) / r.width * 100).toFixed(2) + '%');
    root.style.setProperty('--bga-02-my', ((e.clientY - r.top) / r.height * 100).toFixed(2) + '%');
  }, { passive: true });

  root.addEventListener('pointerleave', () => {
    root.style.removeProperty('--bga-02-mx');
    root.style.removeProperty('--bga-02-my');
    if (!calm) root.classList.add('is-idle');
  });
})();
```
