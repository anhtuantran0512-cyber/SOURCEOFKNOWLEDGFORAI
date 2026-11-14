---
source: "codefronts"
url: "https://codefronts.com/motion/css-shake-animation/css-elastic-shake-effect/"
title: "CSS Elastic Shake Effect"
section: "motion"
category: "css-shake-animation"
category_name: "CSS Shake Animations"
description: "Elasticity two ways: a card you 'pull and release' whose snap-back rides the modern linear() spring curve (one keyframe pair, the easing does ALL the…"
has_js: "true"
---

Here's a working CSS Shake Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Elastic Shake Effect
Source: https://codefronts.com/motion/css-shake-animation/css-elastic-shake-effect/

Elasticity two ways: a card you 'pull and release' whose snap-back rides the modern linear() spring curve (one keyframe pair, the easing does ALL the physics), and a rubber-band pill that stretches on hover and twangs back with chained overshoot keyframes for browsers where you want full control of every bounce.
## HTML
```html
<div class="shk-27-group">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&family=JetBrains+Mono:wght@500;600&display=swap" rel="stylesheet">
<section class="shk-27a" aria-label="Card that springs back with linear easing">
  <div class="shk-27a__stage">
    <div class="shk-27a__rail" aria-hidden="true"><span class="shk-27a__anchor"></span></div>
    <button class="shk-27a__card" id="shk-27a-card" type="button">
      <span class="shk-27a__label" id="shk-27a-label">Click to pull</span>
      <code class="shk-27a__curve">linear(0, .38, .78, 1.18, 1.28, 1.06, .94, 1.02, .99, 1)</code>
    </button>
    <p class="shk-27a__hint" aria-hidden="true">the keyframes are just 56px → 0 — every bounce lives in the easing function</p>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,[email protected],500..800&display=swap" rel="stylesheet">
<section class="shk-27b" aria-label="Pill that stretches and twangs back">
  <div class="shk-27b__stage">
    <button class="shk-27b__band" type="button">stretch me</button>
    <p class="shk-27b__hint" aria-hidden="true">hover: slow scaleX pull · leave: 5-stage overshoot chain (1.25 → .88 → 1.08 → .96 → 1)</p>
  </div>
</section>
</div>
```
## CSS
```css
.shk-27-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.shk-27-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.shk-27a,
.shk-27a *,
.shk-27a *::before,
.shk-27a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-27a {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(170deg,#101620,#0a0e15);
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.shk-27a__stage {
  display: grid;
  justify-items: center;
  gap: 22px;
}

.shk-27a__rail {
  width: 280px;
  height: 2px;
  background: rgba(150,180,230,.2);
  position: relative;
}

.shk-27a__anchor {
  position: absolute;
  left: 50%;
  top: 50%;
  width: 10px;
  height: 10px;
  translate: -50% -50%;
  border-radius: 50%;
  background: oklch(0.8 0.14 210);
}

.shk-27a__card {
  display: grid;
  gap: 12px;
  padding: 26px 30px;
  border-radius: 18px;
  border: 1px solid oklch(0.8 0.14 210 / .35);
  background: linear-gradient(180deg,rgba(255,255,255,.07),rgba(255,255,255,.03));
  color: #e6f0fc;
  cursor: pointer;
  transition: translate .35s cubic-bezier(.3,1.2,.5,1);
}

.shk-27a__card.is-pulled {
  translate: 56px 0;
}

.shk-27a__card.is-released {
  animation: shk-27a-snap .9s cubic-bezier(.22,1.6,.36,1) both;
}

@supports (animation-timing-function: linear(0,1)) {
  .shk-27a__card.is-released {
    animation: shk-27a-snap .9s linear(0,.38 6.5%,.78 12.5%,1.18 19%,1.28 22.5%,1.06 30%,.94 36%,1.02 46%,.99 56%,1) both;
  }
}

.shk-27a__label {
  font-size: 17px;
  font-weight: 700;
}

.shk-27a__curve {
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: 10.5px;
  color: oklch(0.8 0.14 210 / .8);
}

.shk-27a__hint {
  font-size: 12px;
  color: rgba(230,240,252,.4);
  max-width: 420px;
  text-align: center;
}

@keyframes shk-27a-snap {
  from {
    translate: 56px 0;
  }

  to {
    translate: 0 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-27a__card.is-released {
    animation: none;
  }

  .shk-27a__card.is-pulled {
    translate: 0 0;
  }
}

.shk-27b,
.shk-27b *,
.shk-27b *::before,
.shk-27b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-27b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(180deg,#fff8e8,#fbeecb);
  font-family: 'Bricolage Grotesque','Segoe UI',system-ui,sans-serif;
}

.shk-27b__stage {
  text-align: center;
}

.shk-27b__band {
  padding: 20px 52px;
  font: inherit;
  font-size: 22px;
  font-weight: 800;
  letter-spacing: -.01em;
  color: #fff8e8;
  background: linear-gradient(180deg,#e2542f,#c23e1e);
  border: 0;
  border-radius: 999px;
  cursor: pointer;
  box-shadow: 0 16px 32px -14px rgba(194,62,30,.65);
  animation: shk-27b-twang .8s cubic-bezier(.36,.07,.19,.97) both;
  transition: scale .45s cubic-bezier(.2,.8,.3,1);
}

.shk-27b__band:hover {
  scale: 1.22 .92;
  animation: none;
}

.shk-27b__band:focus-visible {
  outline: 3px solid #c23e1e;
  outline-offset: 5px;
}

.shk-27b__hint {
  margin-top: 26px;
  font-size: 12px;
  color: rgba(90,40,20,.55);
  max-width: 440px;
  margin-inline: auto;
}

@keyframes shk-27b-twang {
  0% {
    scale: 1.25 .9;
  }

  25% {
    scale: .88 1.07;
  }

  45% {
    scale: 1.08 .96;
  }

  65% {
    scale: .96 1.02;
  }

  82% {
    scale: 1.02 .99;
  }

  100% {
    scale: 1 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-27b__band {
    animation: none;
  }

  .shk-27b__band:hover {
    scale: 1;
  }
}
```

## JavaScript
```js
(function(){
  var card=document.getElementById('shk-27a-card'),label=document.getElementById('shk-27a-label'); if(!card) return;
  var pulled=false;
  card.addEventListener('animationend',function(){ card.classList.remove('is-released'); });
  card.addEventListener('click',function(){
    pulled=!pulled;
    if(pulled){ card.classList.remove('is-released'); card.classList.add('is-pulled'); label.textContent='Click to release'; }
    else{ card.classList.remove('is-pulled'); card.classList.add('is-released'); label.textContent='Click to pull'; }
  });
})();

/* No JavaScript — hover stretches via a slow transition; un-hover re-runs the .band's twang animation (it restarts because hover disabled it with animation:none). Each scale pair conserves volume: X up, Y down. */
```
