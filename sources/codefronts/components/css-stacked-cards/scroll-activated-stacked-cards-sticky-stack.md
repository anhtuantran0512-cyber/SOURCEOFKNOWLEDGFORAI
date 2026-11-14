---
source: "codefronts"
url: "https://codefronts.com/components/css-stacked-cards/scroll-activated-stacked-cards-sticky-stack/"
title: "Scroll-Activated Stacked Cards (Sticky Stack)"
section: "components"
category: "css-stacked-cards"
category_name: "CSS Stacked Cards"
description: "A vertical \"How It Works\" sequence where each step pins with position: sticky and the previous card scales down and dims as the next slides over it, keeping…"
has_js: "true"
---

Here's a working CSS Stacked Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Scroll-Activated Stacked Cards (Sticky Stack)
Source: https://codefronts.com/components/css-stacked-cards/scroll-activated-stacked-cards-sticky-stack/

A vertical "How It Works" sequence where each step pins with position: sticky and the previous card scales down and dims as the next slides over it, keeping the reader anchored as they scroll. Ideal for feature sections, agency workflows, and process pages. Scroll the demo to see each phase stack over the last.
## HTML
```html
<div class="scd-29">
  <div class="scd-29__rail">
    <span class="scd-29__pip scd-29__pip--on"></span><span class="scd-29__pip"></span><span class="scd-29__pip"></span><span class="scd-29__pip"></span>
  </div>
  <div class="scd-29__scroll-wrap">
    <section class="scd-29__step scd-29__step--s1"><div class="scd-29__grad"></div><div class="scd-29__sheen"></div>
      <div class="scd-29__top"><span class="scd-29__idx">01</span><span class="scd-29__chip">Phase one</span></div>
      <div><h2 class="scd-29__h2">Discover</h2><p class="scd-29__p">We map your goals and audit exactly where you stand today.</p><div class="scd-29__bar"><i></i></div></div></section>
    <section class="scd-29__step scd-29__step--s2"><div class="scd-29__grad"></div><div class="scd-29__sheen"></div>
      <div class="scd-29__top"><span class="scd-29__idx">02</span><span class="scd-29__chip">Phase two</span></div>
      <div><h2 class="scd-29__h2">Design</h2><p class="scd-29__p">Concepts take shape through rapid, collaborative iteration.</p><div class="scd-29__bar"><i></i></div></div></section>
    <section class="scd-29__step scd-29__step--s3"><div class="scd-29__grad"></div><div class="scd-29__sheen"></div>
      <div class="scd-29__top"><span class="scd-29__idx">03</span><span class="scd-29__chip">Phase three</span></div>
      <div><h2 class="scd-29__h2">Build</h2><p class="scd-29__p">Production-ready code, tested and shipped with real care.</p><div class="scd-29__bar"><i></i></div></div></section>
    <section class="scd-29__step scd-29__step--s4"><div class="scd-29__grad"></div><div class="scd-29__sheen"></div>
      <div class="scd-29__top"><span class="scd-29__idx">04</span><span class="scd-29__chip">Phase four</span></div>
      <div><h2 class="scd-29__h2">Launch</h2><p class="scd-29__p">We go live, measure everything, then refine what works.</p><div class="scd-29__bar"><i></i></div></div></section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Geist:wght@300;400;500;600;700&display=swap');

.scd-29,
.scd-29 *,
.scd-29 *::before,
.scd-29 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}
/* Page-scroll demo — mirrors the original source body. The visitor's
   own page (or the playground iframe) provides the scroll; we do NOT
   create an internal overflow:auto scroller. */

.scd-29 {
  position: relative;
  width: 100%;
  min-height: 100vh;
  background: #05060a;
  font-family: 'Geist', sans-serif;
  color: #fff;
  scroll-behavior: smooth;
}

.scd-29::before {
  content: '';
  position: fixed;
  inset: -30%;
  z-index: 0;
  background: radial-gradient(40% 40% at 25% 25%, rgba(99,102,241,.30), transparent 70%), radial-gradient(45% 45% at 75% 30%, rgba(236,72,153,.26), transparent 70%), radial-gradient(50% 50% at 50% 80%, rgba(45,212,191,.24), transparent 70%);
  filter: blur(30px);
  animation: scd-29-drift 20s ease-in-out infinite alternate;
  pointer-events: none;
}

@keyframes scd-29-drift {
  0% {
    transform: translate(-3%,-2%) scale(1);
  }

  100% {
    transform: translate(4%,3%) scale(1.1);
  }
}

.scd-29::after {
  content: '';
  position: fixed;
  inset: 0;
  z-index: 0;
  background: repeating-linear-gradient(0deg, rgba(255,255,255,.02) 0 1px, transparent 1px 3px);
  mix-blend-mode: overlay;
  pointer-events: none;
}

.scd-29__scroll-wrap {
  position: relative;
  z-index: 1;
  width: min(460px, 92vw);
  margin: 0 auto;
  /* vh-based padding matches the source — generous space above + below
       the deck so each card has room to pin without crowding the viewport
       edges. */
  padding: 55vh 0 75vh;
}

.scd-29__rail {
  position: fixed;
  top: 50%;
  right: 24px;
  transform: translateY(-50%);
  z-index: 5;
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.scd-29__pip {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: rgba(255,255,255,.25);
  transition: all .4s;
  display: block;
}

.scd-29__pip--on {
  background: #fff;
  height: 26px;
  border-radius: 6px;
  box-shadow: 0 0 14px rgba(255,255,255,.6);
}

.scd-29__step {
  position: sticky;
  top: 20vh;
  height: 320px;
  border-radius: 28px;
  padding: 38px;
  margin-bottom: 36px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  overflow: hidden;
  transform-origin: 50% 0;
  box-shadow: 0 40px 80px rgba(0,0,0,.55), 0 0 0 1px rgba(255,255,255,.08) inset;
  backdrop-filter: blur(6px);
}

.scd-29__grad {
  position: absolute;
  inset: 0;
  z-index: -1;
  opacity: .95;
  background-size: 200% 200%;
  animation: scd-29-flow 9s ease infinite;
}

@keyframes scd-29-flow {
  0% {
    background-position: 0% 50%;
  }

  50% {
    background-position: 100% 50%;
  }

  100% {
    background-position: 0% 50%;
  }
}

.scd-29__sheen {
  position: absolute;
  top: -50%;
  left: -30%;
  width: 50%;
  height: 200%;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,.35), transparent);
  transform: rotate(18deg);
  animation: scd-29-sweep 6s ease-in-out infinite;
}

@keyframes scd-29-sweep {
  0%,
    100% {
    transform: rotate(18deg) translateX(-300px);
  }

  50% {
    transform: rotate(18deg) translateX(700px);
  }
}

.scd-29__top {
  display: flex;
  align-items: center;
  gap: 14px;
}

.scd-29__idx {
  font-family: 'Instrument Serif', serif;
  font-style: italic;
  font-size: 4rem;
  line-height: .8;
  opacity: .9;
  text-shadow: 0 4px 20px rgba(0,0,0,.3);
}

.scd-29__chip {
  margin-left: auto;
  font-size: .62rem;
  letter-spacing: .22em;
  text-transform: uppercase;
  padding: 7px 14px;
  border-radius: 999px;
  background: rgba(255,255,255,.18);
  border: 1px solid rgba(255,255,255,.25);
  backdrop-filter: blur(6px);
}

.scd-29__h2 {
  font-family: 'Instrument Serif', serif;
  font-size: 2.4rem;
  letter-spacing: -.01em;
}

.scd-29__p {
  opacity: .88;
  max-width: 32ch;
  line-height: 1.55;
  font-weight: 300;
}

.scd-29__bar {
  height: 4px;
  border-radius: 4px;
  background: rgba(255,255,255,.25);
  overflow: hidden;
  margin-top: 16px;
}

.scd-29__bar i {
  display: block;
  height: 100%;
  width: 0;
  background: #fff;
  border-radius: 4px;
  transition: width .5s;
}

.scd-29__step--s1 {
  top: 20vh;
}

.scd-29__step--s1 .scd-29__grad {
  background: linear-gradient(135deg,#1e1b4b,#4338ca 45%,#7c3aed);
}

.scd-29__step--s2 {
  top: 22vh;
}

.scd-29__step--s2 .scd-29__grad {
  background: linear-gradient(135deg,#831843,#be185d 45%,#fb7185);
}

.scd-29__step--s3 {
  top: 24vh;
}

.scd-29__step--s3 .scd-29__grad {
  background: linear-gradient(135deg,#064e3b,#0d9488 50%,#34d399);
}

.scd-29__step--s4 {
  top: 26vh;
}

.scd-29__step--s4 .scd-29__grad {
  background: linear-gradient(135deg,#7c2d12,#ea580c 45%,#fbbf24);
}

@media (prefers-reduced-motion: reduce) {
  .scd-29::before,
    .scd-29__grad,
    .scd-29__sheen,
    .scd-29__step,
    .scd-29__bar i,
    .scd-29__pip {
    animation: none !important;
    transition: none !important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.scd-29');
  if (!root) return;
  const steps = [...root.querySelectorAll('.scd-29__step')];
  const pips = [...root.querySelectorAll('.scd-29__pip')];
  if (!steps.length) return;

  function update() {
    let active = 0;
    steps.forEach((s, i) => {
      const r = s.getBoundingClientRect();
      const stickTop = window.innerHeight * (0.20 + i * 0.02);
      const next = steps[i + 1];
      if (next) {
        const nr = next.getBoundingClientRect();
        const prog = Math.min(Math.max((stickTop + 320 - nr.top) / 320, 0), 1);
        s.style.transform = `scale(${1 - prog * 0.10}) translateY(${prog * -8}px)`;
        s.style.filter = `brightness(${1 - prog * 0.35})`;
        const fill = s.querySelector('.scd-29__bar i');
        if (fill) fill.style.width = (prog * 100) + '%';
      } else {
        const fill = s.querySelector('.scd-29__bar i');
        if (fill) fill.style.width = '100%';
      }
      if (r.top <= stickTop + 10) active = i;
    });
    pips.forEach((p, i) => p.classList.toggle('scd-29__pip--on', i === active));
  }

  window.addEventListener('scroll', update, { passive: true });
  window.addEventListener('resize', update);
  update();
})();
```
