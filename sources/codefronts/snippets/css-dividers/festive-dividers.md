---
source: "codefronts"
url: "https://codefronts.com/snippets/css-dividers/festive-dividers/"
title: "Confetti & Sparkle SVG Divider CSS"
section: "snippets"
category: "css-dividers"
category_name: "CSS Dividers"
description: "A festive divider that earns its animation: four-point sparkles twinkle on a staggered loop along a gradient rule, and a single button fires a real confetti…"
has_js: "true"
---

Here's a working CSS Divider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Confetti & Sparkle SVG Divider CSS
Source: https://codefronts.com/snippets/css-dividers/festive-dividers/

A festive divider that earns its animation: four-point sparkles twinkle on a staggered loop along a gradient rule, and a single button fires a real confetti burst — 24 pieces created, animated with the Web Animations API, and removed on finish, so nothing accumulates in the DOM. Exactly the pattern you want for a holiday sale banner or a checkout success state.
## HTML
```html
<section class="div-24" aria-label="Confetti and sparkle divider demo">
  <div class="div-24__stage">
    <p class="div-24__eyebrow">LIMITED · 48 HOURS</p>
    <h2 class="div-24__title">Everything Divided<br><span class="div-24__em">by two</span></h2>
    <div class="div-24__rule" role="separator" aria-label="Divider">
      <span class="div-24__sparkle" style="--div-24-i:0"></span>
      <span class="div-24__sparkle div-24__sparkle--lg" style="--div-24-i:1"></span>
      <span class="div-24__sparkle" style="--div-24-i:2"></span>
    </div>
    <button class="div-24__btn" id="div-24-fire" type="button">Celebrate</button>
    <span class="div-24__burst" id="div-24-burst" aria-hidden="true"></span>
    <p class="div-24__chip">clip-path sparkle · element.animate() · onfinish → remove()</p>
  </div>
</section>
```
## CSS
```css
.div-24 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--div-24-bg);
  --div-24-bg: oklch(0.21 0.05 300);
  --div-24-ink: oklch(0.97 0.012 300);
  --div-24-mut: oklch(0.72 0.04 300);
  --div-24-gold: oklch(0.88 0.15 92);
  --div-24-acc: oklch(0.74 0.18 350);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--div-24-ink);
}

.div-24 *,
.div-24 *::before,
.div-24 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.div-24__stage {
  position: relative;
  min-height: 100svh;
  display: grid;
  place-content: center;
  justify-items: center;
  gap: clamp(16px,3vw,26px);
  text-align: center;
  padding: clamp(28px,6vw,72px) clamp(20px,5vw,56px);
  background: radial-gradient(75% 55% at 50% 40%,oklch(0.3 0.1 320/.8),transparent);
}

.div-24__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .28em;
  color: var(--div-24-gold);
}

.div-24__title {
  font-size: clamp(32px,7vw,68px);
  line-height: 1.02;
  letter-spacing: -.03em;
  font-weight: 750;
  text-wrap: balance;
}

.div-24__em {
  background: linear-gradient(100deg,var(--div-24-gold),var(--div-24-acc));
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  font-style: italic;
}

.div-24__rule {
  width: min(88vw,480px);
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 14px;
}

.div-24__rule::before,
.div-24__rule::after {
  content: '';
  flex: 1 1 0;
  height: 1px;
  background: linear-gradient(90deg,transparent,var(--div-24-gold));
}

.div-24__rule::after {
  background: linear-gradient(90deg,var(--div-24-gold),transparent);
}

.div-24__sparkle {
  width: 13px;
  height: 13px;
  flex: none;
  background: var(--div-24-gold);
  clip-path: polygon(50% 0,58% 42%,100% 50%,58% 58%,50% 100%,42% 58%,0 50%,42% 42%);
  animation: div-24-twinkle 2.6s ease-in-out infinite;
  animation-delay: calc(var(--div-24-i) * -.72s);
  filter: drop-shadow(0 0 7px oklch(0.88 0.15 92/.6));
}

.div-24__sparkle--lg {
  width: 21px;
  height: 21px;
}

@keyframes div-24-twinkle {
  0%,
    100% {
    scale: .6;
    opacity: .5;
    rotate: 0deg;
  }

  50% {
    scale: 1.15;
    opacity: 1;
    rotate: 90deg;
  }
}

.div-24__btn {
  min-height: 48px;
  padding: 0 28px;
  border: 0;
  border-radius: 99px;
  background: linear-gradient(110deg,var(--div-24-acc),oklch(0.68 0.2 20));
  color: oklch(0.99 0.01 350);
  font-family: inherit;
  font-size: 15px;
  font-weight: 680;
  letter-spacing: .01em;
  cursor: pointer;
  box-shadow: 0 10px 26px oklch(0.6 0.2 350/.4);
  transition: transform .18s ease,box-shadow .18s ease;
}

.div-24__btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 15px 32px oklch(0.6 0.2 350/.5);
}

.div-24__btn:active {
  transform: translateY(0);
}

.div-24__btn:focus-visible {
  outline: 2px solid var(--div-24-gold);
  outline-offset: 3px;
}

.div-24__burst {
  position: absolute;
  left: 50%;
  top: 50%;
  width: 0;
  height: 0;
  pointer-events: none;
  overflow: visible;
}

.div-24__piece {
  position: absolute;
  left: 0;
  top: 0;
  border-radius: 1px;
  will-change: transform,opacity;
}

.div-24__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--div-24-mut);
  padding: 8px 14px;
  border: 1px solid oklch(1 0 0/.16);
  border-radius: 99px;
  max-width: 92vw;
}

@media (prefers-reduced-motion: reduce) {
  .div-24__sparkle {
    animation: none;
    scale: 1;
    opacity: 1;
  }
}
```

## JavaScript
```js
(() => {
  const btn = document.getElementById('div-24-fire');
  const host = document.getElementById('div-24-burst');
  if (!btn || !host || btn.dataset.ppWired) return;
  btn.dataset.ppWired = '1';
  const calm = window.matchMedia('(prefers-reduced-motion: reduce)');
  const hues = [92, 350, 20, 300, 200];
  btn.addEventListener('click', () => {
    if (calm.matches) return;
    for (let i = 0; i < 24; i++) {
      const p = document.createElement('i');
      p.className = 'div-24__piece';
      const wide = Math.random() > 0.5;
      p.style.cssText = 'width:' + (wide ? 8 : 3) + 'px;height:' + (wide ? 4 : 10) +
        'px;background:oklch(0.8 0.18 ' + hues[i % hues.length] + ')';
      host.appendChild(p);
      const a = (i / 24) * Math.PI * 2 + Math.random() * 0.5;
      const d = 90 + Math.random() * 150;
      p.animate([
        { translate: '0 0', rotate: '0deg', opacity: 1 },
        { translate: (Math.cos(a) * d).toFixed(0) + 'px ' + (Math.sin(a) * d - 40).toFixed(0) + 'px',
          rotate: (Math.random() * 900 - 450).toFixed(0) + 'deg', opacity: 0 }
      ], { duration: 900 + Math.random() * 600, easing: 'cubic-bezier(.2,.7,.3,1)' })
        .onfinish = () => p.remove();
    }
  });
})();
```
