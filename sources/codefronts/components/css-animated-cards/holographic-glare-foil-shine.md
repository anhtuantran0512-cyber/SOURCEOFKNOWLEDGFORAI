---
source: "codefronts"
url: "https://codefronts.com/components/css-animated-cards/holographic-glare-foil-shine/"
title: "Holographic Glare / Foil Shine"
section: "components"
category: "css-animated-cards"
category_name: "CSS Animated Cards"
description: "The collectible-card effect: the card tilts toward the cursor, a rainbow foil layer shifts hue with the angle, a specular highlight tracks the pointer, and a…"
has_js: "true"
---

Here's a working CSS Animated Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Holographic Glare / Foil Shine
Source: https://codefronts.com/components/css-animated-cards/holographic-glare-foil-shine/

The collectible-card effect: the card tilts toward the cursor, a rainbow foil layer shifts hue with the angle, a specular highlight tracks the pointer, and a hard glare sweeps across on entry. Three stacked blend layers over a real 3D transform — and a CSS-only sweep for touch devices where there is no pointer to follow.
## HTML
```html
<section class="ac-22" aria-label="Holographic foil card hover demo">
  <div class="ac-22__stage">
    <header class="ac-22__head">
      <p class="ac-22__eyebrow">Foil stock</p>
      <h2 class="ac-22__title">Hover to tilt the card into the light</h2>
    </header>
    <div class="ac-22__scene" data-scene>
      <article class="ac-22__card" data-card tabindex="0" aria-label="Aurora tier membership card, member since 2021">
        <span class="ac-22__foil" aria-hidden="true"></span>
        <span class="ac-22__spec" aria-hidden="true"></span>
        <span class="ac-22__glare" aria-hidden="true"></span>
        <div class="ac-22__content">
          <div class="ac-22__toprow">
            <span class="ac-22__mark" aria-hidden="true">
              <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"><path d="M12 3l3 6 6.5.9-4.7 4.6 1.1 6.5L12 18l-5.9 3 1.1-6.5L2.5 9.9 9 9l3-6z"/></svg>
            </span>
            <span class="ac-22__tier">Aurora</span>
          </div>
          <div class="ac-22__mid">
            <p class="ac-22__no">4419 · 0286 · 7731</p>
            <p class="ac-22__label">Membership</p>
          </div>
          <div class="ac-22__foot">
            <div><p class="ac-22__k">Member</p><p class="ac-22__v">R. Okafor</p></div>
            <div><p class="ac-22__k">Since</p><p class="ac-22__v">2021</p></div>
            <div><p class="ac-22__k">Points</p><p class="ac-22__v">28,410</p></div>
          </div>
        </div>
      </article>
    </div>
    <p class="ac-22__chip" aria-hidden="true">perspective on parent · rx/ry from normalised pointer · color-dodge foil · overlay specular · entry glare sweep</p>
  </div>
</section>
```
## CSS
```css
.ac-22,
.ac-22 *,
.ac-22 *::before,
.ac-22 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ac-22 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --ac-22-bg: oklch(0.13 0.016 280);
  --ac-22-ink: oklch(0.98 0.004 280);
  --ac-22-mut: oklch(0.72 0.02 280);
  --ac-22-acc: oklch(0.84 0.15 195);
  background: radial-gradient(120% 80% at 50% 0%,oklch(0.21 0.04 285),var(--ac-22-bg) 68%);
  color: var(--ac-22-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.ac-22__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(20px,3vw,32px);
  padding: clamp(20px,5vw,58px);
}

.ac-22__head {
  display: grid;
  justify-items: center;
  gap: 9px;
  text-align: center;
}

.ac-22__eyebrow {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--ac-22-acc);
}

.ac-22__title {
  font-size: clamp(22px,3.2vw,34px);
  font-weight: 650;
  line-height: 1.12;
  letter-spacing: -.03em;
  text-wrap: balance;
}

.ac-22__scene {
  perspective: 1100px;
  width: min(100%,420px);
}

.ac-22__card {
  position: relative;
  aspect-ratio: 1.586;
  border-radius: 20px;
  overflow: hidden;
  isolation: isolate;
  transform-style: preserve-3d;
  background: linear-gradient(145deg,oklch(0.30 0.07 285),oklch(0.20 0.05 265) 42%,oklch(0.26 0.08 210));
  box-shadow: 0 34px 68px -34px oklch(0 0 0/.9),0 0 0 1px oklch(1 0 0/.10) inset;
  rotate: none;
  transform: rotateX(var(--ac-22-rx,0deg)) rotateY(var(--ac-22-ry,0deg));
  transition: transform .5s cubic-bezier(.16,1,.3,1);
  cursor: pointer;
}

.ac-22__card[data-live] {
  transition: transform .08s linear;
}

.ac-22__card:focus-visible {
  outline: 2px solid var(--ac-22-acc);
  outline-offset: 4px;
}

.ac-22__foil {
  position: absolute;
  inset: 0;
  mix-blend-mode: color-dodge;
  opacity: .34;
  background: repeating-linear-gradient(115deg,oklch(0.72 0.20 12) 0 9%,oklch(0.78 0.19 88) 9% 18%,oklch(0.80 0.17 150) 18% 27%,oklch(0.76 0.18 210) 27% 36%,oklch(0.70 0.20 300) 36% 45%,oklch(0.72 0.20 12) 45% 54%);
  background-size: 220% 220%;
  background-position: calc(var(--ac-22-mx,50%) * .6) calc(var(--ac-22-my,50%) * .6);
  transition: background-position .3s ease-out,opacity .4s;
}

.ac-22__card[data-live] .ac-22__foil {
  opacity: .52;
  transition: background-position .08s linear;
}

.ac-22__spec {
  position: absolute;
  inset: 0;
  mix-blend-mode: overlay;
  opacity: 0;
  background: radial-gradient(farthest-corner circle at var(--ac-22-mx,50%) var(--ac-22-my,50%),oklch(1 0 0/.9),oklch(1 0 0/.2) 22%,transparent 48%);
  transition: opacity .4s;
}

.ac-22__card[data-live] .ac-22__spec {
  opacity: 1;
}

.ac-22__glare {
  position: absolute;
  inset: -30%;
  pointer-events: none;
  background: linear-gradient(105deg,transparent 38%,oklch(1 0 0/.55) 50%,transparent 62%);
  translate: -120% 0;
  opacity: 0;
}

.ac-22__card[data-sweep] .ac-22__glare {
  animation: ac-22-sweep .95s cubic-bezier(.3,0,.2,1);
}

@keyframes ac-22-sweep {
  0% {
    translate: -120% 0;
    opacity: 0;
  }

  20% {
    opacity: 1;
  }

  100% {
    translate: 120% 0;
    opacity: 0;
  }
}

.ac-22__content {
  position: relative;
  display: grid;
  align-content: space-between;
  height: 100%;
  padding: 22px;
  transform: translateZ(28px);
}

.ac-22__toprow {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
}

.ac-22__mark {
  display: grid;
  place-items: center;
  width: 40px;
  height: 40px;
  border-radius: 12px;
  background: oklch(1 0 0/.12);
  color: var(--ac-22-acc);
  backdrop-filter: blur(6px);
}

.ac-22__tier {
  font-size: 12px;
  font-weight: 750;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--ac-22-acc);
}

.ac-22__mid {
  display: grid;
  gap: 4px;
}

.ac-22__no {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: clamp(15px,2.6vw,19px);
  font-weight: 600;
  letter-spacing: .08em;
  font-variant-numeric: tabular-nums;
}

.ac-22__label {
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .19em;
  text-transform: uppercase;
  color: var(--ac-22-mut);
}

.ac-22__foot {
  display: flex;
  justify-content: space-between;
  gap: 14px;
}

.ac-22__k {
  font-size: 9.5px;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--ac-22-mut);
}

.ac-22__v {
  margin-top: 3px;
  font-size: 14px;
  font-weight: 640;
  letter-spacing: -.015em;
  font-variant-numeric: tabular-nums;
}

.ac-22__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  line-height: 1.6;
  color: var(--ac-22-mut);
  padding: 8px 15px;
  border: 1px solid oklch(1 0 0/.13);
  border-radius: 99px;
  text-align: center;
  max-width: min(100%,800px);
}

@media (hover: none) {
  .ac-22__foil {
    animation: ac-22-drift 7s ease-in-out infinite;
    opacity: .46;
  }

  @keyframes ac-22-drift {
    0%,
        100% {
      background-position: 0% 40%;
    }

    50% {
      background-position: 100% 60%;
    }
  }
}

@media (prefers-reduced-motion: reduce) {
  .ac-22__card {
    transform: none !important;
    transition: none;
  }

  .ac-22__glare {
    display: none;
  }

  .ac-22__foil {
    animation: none;
  }
}
```

## JavaScript
```js
(() => {
  const MAX_X = 13, MAX_Y = 15;                     // degrees — past ~16 the text starts to blur
  document.querySelectorAll('.ac-22').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    const card = root.querySelector('[data-card]');
    let rect = null, frame = 0, ev = null;

    const paint = () => {
      frame = 0;
      if (!ev || !rect) return;
      const px = (ev.clientX - rect.left) / rect.width - 0.5;    // -0.5 … 0.5
      const py = (ev.clientY - rect.top) / rect.height - 0.5;
      card.style.setProperty('--ac-22-rx', (-py * MAX_X * 2).toFixed(2) + 'deg');
      card.style.setProperty('--ac-22-ry', (px * MAX_Y * 2).toFixed(2) + 'deg');
      card.style.setProperty('--ac-22-mx', ((px + 0.5) * 100).toFixed(1) + '%');
      card.style.setProperty('--ac-22-my', ((py + 0.5) * 100).toFixed(1) + '%');
    };

    card.addEventListener('pointerenter', (e) => {
      if (e.pointerType === 'touch') return;
      rect = card.getBoundingClientRect();          // measured once per hover, never per frame
      card.dataset.live = '';
      card.removeAttribute('data-sweep');
      void card.offsetWidth;
      card.dataset.sweep = '';
    });

    card.addEventListener('pointermove', (e) => {
      if (e.pointerType === 'touch' || !rect) return;
      ev = e;
      if (!frame) frame = requestAnimationFrame(paint);
    }, { passive: true });

    const reset = () => {
      card.removeAttribute('data-live');
      ev = null;
      card.style.setProperty('--ac-22-rx', '0deg');
      card.style.setProperty('--ac-22-ry', '0deg');
      card.style.setProperty('--ac-22-mx', '50%');
      card.style.setProperty('--ac-22-my', '50%');
    };
    card.addEventListener('pointerleave', reset);
    card.addEventListener('blur', reset);
    card.addEventListener('focus', () => { card.removeAttribute('data-sweep'); void card.offsetWidth; card.dataset.sweep = ''; });
  });
})();
```
