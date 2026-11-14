---
source: "codefronts"
url: "https://codefronts.com/components/css-liquid-glass-cards/multi-step-wizard-progress-card/"
title: "Multi-Step Wizard Progress Card"
section: "components"
category: "css-liquid-glass-cards"
category_name: "CSS Liquid Glass Cards"
description: "A multi-step workflow card whose progress indicator is built from Liquid Glass step nodes connected by a gooey track — as you advance, the filled progress…"
has_js: "true"
---

Here's a working CSS Liquid Glass Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Multi-Step Wizard Progress Card
Source: https://codefronts.com/components/css-liquid-glass-cards/multi-step-wizard-progress-card/

A multi-step workflow card whose progress indicator is built from Liquid Glass step nodes connected by a gooey track — as you advance, the filled progress fluidly bleeds from one step into the next like connecting drops of water, the liquid neck stretching and merging the nodes. Includes Back/Next controls and a step panel.
## HTML
```html
<section class="lg-20" aria-label="Liquid glass multi-step wizard progress card demo">
  <svg class="lg-20__defs" aria-hidden="true" width="0" height="0"><filter id="lg-20-goo"><feGaussianBlur in="SourceGraphic" stdDeviation="6" result="b"/><feColorMatrix in="b" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 20 -8"/></filter></svg>
  <article class="lg-20__card" style="--step:0">
    <div class="lg-20__prog">
      <span class="lg-20__goo" aria-hidden="true"><span class="lg-20__fill"></span><span class="lg-20__dot" style="left:0%"></span><span class="lg-20__dot" style="left:calc(50% - 15px)"></span><span class="lg-20__dot" style="left:calc(100% - 30px)"></span></span>
      <ol class="lg-20__labels"><li aria-current="step">Account</li><li>Profile</li><li>Done</li></ol>
    </div>
    <div class="lg-20__body">
      <h3 class="lg-20__h" id="lg-20-h">Create your account</h3>
      <p class="lg-20__p" id="lg-20-p">Step 1 of 3 — set up your login credentials to get started.</p>
    </div>
    <div class="lg-20__foot">
      <button class="lg-20__btn lg-20__btn--ghost" id="lg-20-back" type="button" disabled>Back</button>
      <button class="lg-20__btn" id="lg-20-next" type="button">Next</button>
    </div>
    <p class="lg-20__live" id="lg-20-live" aria-live="polite"></p>
  </article>
</section>
```
## CSS
```css
.lg-20,
.lg-20 * {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lg-20 {
  width: 100%;
  --accent: oklch(0.7 0.17 190);
  display: grid;
  place-items: center;
  min-height: 100vh;
  padding: 24px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: conic-gradient(from 120deg at 40% 40%,#0f172a,#0e7490,#155e75,#0f172a);
  background-size: 220% 220%;
  animation: lg-20-bg 22s ease-in-out infinite;
}

@keyframes lg-20-bg {
  50% {
    background-position: 100% 100%;
  }
}

.lg-20__card {
  width: min(380px,100%);
  padding: 26px 24px;
  border-radius: 24px;
  isolation: isolate;
  color: #fff;
  background: color-mix(in oklab,white 11%,transparent);
  border: 1px solid rgba(255,255,255,.35);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.5),0 30px 60px -30px rgba(0,0,0,.7);
  backdrop-filter: blur(22px) saturate(180%);
  -webkit-backdrop-filter: blur(22px) saturate(180%);
}

.lg-20__prog {
  position: relative;
}

.lg-20__goo {
  position: relative;
  display: block;
  height: 30px;
  filter: url(#lg-20-goo);
}

.lg-20__goo::before {
  content: "";
  position: absolute;
  left: 15px;
  right: 15px;
  top: 50%;
  transform: translateY(-50%);
  height: 8px;
  border-radius: 999px;
  background: rgba(255,255,255,.18);
}

.lg-20__fill {
  position: absolute;
  left: 15px;
  top: 50%;
  transform: translateY(-50%);
  height: 8px;
  width: calc(var(--step)/2*(100% - 30px));
  border-radius: 999px;
  background: var(--accent);
  transition: width .5s cubic-bezier(.65,0,.35,1);
}

.lg-20__dot {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background: rgba(255,255,255,.2);
  border: 2px solid rgba(255,255,255,.4);
  transition: background .4s;
}

.lg-20__labels {
  display: flex;
  justify-content: space-between;
  list-style: none;
  margin: 12px 3px 0;
  font-size: 12px;
  color: rgba(255,255,255,.65);
}

.lg-20__labels li[aria-current] {
  color: #fff;
  font-weight: 700;
}

.lg-20__body {
  margin: 22px 0;
}

.lg-20__h {
  font-size: 20px;
  font-weight: 800;
}

.lg-20__p {
  font-size: 13.5px;
  line-height: 1.6;
  color: rgba(255,255,255,.82);
  margin-top: 8px;
}

.lg-20__foot {
  display: flex;
  gap: 10px;
  justify-content: space-between;
}

.lg-20__btn {
  flex: 1;
  min-height: 44px;
  border: 0;
  border-radius: 12px;
  cursor: pointer;
  font-weight: 700;
  font-size: 14px;
  color: #04252b;
  background: color-mix(in oklab,var(--accent) 85%,white);
  box-shadow: 0 10px 24px -12px var(--accent);
}

.lg-20__btn--ghost {
  color: #fff;
  background: rgba(255,255,255,.14);
  border: 1px solid rgba(255,255,255,.3);
  box-shadow: none;
}

.lg-20__btn:disabled {
  opacity: .4;
  cursor: not-allowed;
}

.lg-20__btn:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 3px;
}

.lg-20__live {
  font-size: 11px;
  color: rgba(255,255,255,.7);
  margin-top: 12px;
  min-height: 1.1em;
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .lg-20 {
    animation: none;
  }

  .lg-20__fill {
    transition: none;
  }
}
```

## JavaScript
```js
(() => {
  const card = document.querySelector('.lg-20__card');
  if (!card) return;
  const back = card.querySelector('#lg-20-back');
  const next = card.querySelector('#lg-20-next');
  const dots = [...card.querySelectorAll('.lg-20__dot')];
  const labels = [...card.querySelectorAll('.lg-20__labels li')];
  const h = card.querySelector('#lg-20-h');
  const p = card.querySelector('#lg-20-p');
  const live = card.querySelector('#lg-20-live');
  const steps = [
    { t: 'Create your account', d: 'Step 1 of 3 — set up your login credentials to get started.' },
    { t: 'Complete your profile', d: 'Step 2 of 3 — add your name, avatar and a short bio.' },
    { t: 'All set!', d: 'Step 3 of 3 — review and finish. Your workspace is ready.' },
  ];
  let i = 0;
  const render = () => {
    card.style.setProperty('--step', i);
    dots.forEach((d, n) => d.style.background = n <= i ? 'var(--accent)' : 'rgba(255,255,255,.2)');
    labels.forEach((l, n) => n === i ? l.setAttribute('aria-current', 'step') : l.removeAttribute('aria-current'));
    h.textContent = steps[i].t; p.textContent = steps[i].d;
    back.disabled = i === 0; next.disabled = i === steps.length - 1;
    next.textContent = i === steps.length - 2 ? 'Finish' : 'Next';
    live.textContent = 'Step ' + (i+1) + ' of ' + steps.length + ': ' + steps[i].t;
  };
  next.addEventListener('click', () => { if (i < steps.length-1) { i++; render(); } });
  back.addEventListener('click', () => { if (i > 0) { i--; render(); } });
  render();
})();
```
