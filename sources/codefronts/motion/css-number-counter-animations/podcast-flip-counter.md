---
source: "codefronts"
url: "https://codefronts.com/motion/css-number-counter-animations/podcast-flip-counter/"
title: "Retro Flip Odometer & Timer"
section: "motion"
category: "css-number-counter-animations"
category_name: "CSS Number Counter Animations"
description: "The split-flap board, done properly: each digit is a card split across its horizontal midline, and a change flips the top half down over a pre-rendered next…"
has_js: "true"
---

Here's a working CSS Number Counter Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Retro Flip Odometer & Timer
Source: https://codefronts.com/motion/css-number-counter-animations/podcast-flip-counter/

The split-flap board, done properly: each digit is a card split across its horizontal midline, and a change flips the top half down over a pre-rendered next value. The hinge shadow, the card gap and the slight overshoot at the end of the flip are what separate a convincing mechanical display from a rotating rectangle.
## HTML
```html
<section class="cnc-12" aria-label="Retro flip odometer and timer demo">
  <div class="cnc-12__stage">
    <p class="cnc-12__title">Session uptime</p>
    <div class="cnc-12__board" aria-hidden="true">
      <div class="cnc-12__group" data-unit="h"><span class="cnc-12__card" data-d="0"></span><span class="cnc-12__card" data-d="0"></span><small class="cnc-12__cap">hrs</small></div>
      <span class="cnc-12__colon">:</span>
      <div class="cnc-12__group" data-unit="m"><span class="cnc-12__card" data-d="0"></span><span class="cnc-12__card" data-d="0"></span><small class="cnc-12__cap">min</small></div>
      <span class="cnc-12__colon">:</span>
      <div class="cnc-12__group" data-unit="s"><span class="cnc-12__card" data-d="0"></span><span class="cnc-12__card" data-d="0"></span><small class="cnc-12__cap">sec</small></div>
    </div>
    <time class="cnc-12__sr" datetime="PT0S">0 hours 0 minutes 0 seconds elapsed</time>
    <div class="cnc-12__ctrls">
      <button class="cnc-12__btn" type="button" data-act="toggle" aria-pressed="true">Pause</button>
      <button class="cnc-12__btn" type="button" data-act="reset">Reset</button>
    </div>
    <p class="cnc-12__chip" aria-hidden="true">two-leaf 3D hinge · sequenced fold/unfold keyframes · backface-visibility</p>
  </div>
</section>
```
## CSS
```css
.cnc-12,
.cnc-12 *,
.cnc-12 *::before,
.cnc-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cnc-12 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --cnc-12-bg: oklch(0.15 0.008 260);
  --cnc-12-card: oklch(0.26 0.01 260);
  --cnc-12-card2: oklch(0.19 0.01 260);
  --cnc-12-ink: oklch(0.97 0.005 90);
  --cnc-12-mut: oklch(0.62 0.015 260);
  --cnc-12-acc: oklch(0.82 0.15 80);
  background: var(--cnc-12-bg);
  color: var(--cnc-12-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
}

.cnc-12__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 20px;
  padding: clamp(18px,4vw,48px);
  background: radial-gradient(65% 50% at 50% 35%,oklch(0.24 0.02 260/.8),transparent 72%);
}

.cnc-12__title {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--cnc-12-mut);
}

.cnc-12__board {
  display: flex;
  align-items: flex-start;
  gap: clamp(6px,1.6vw,14px);
  font-variant-numeric: tabular-nums;
  font-feature-settings: 'tnum' 1;
}

.cnc-12__group {
  display: flex;
  gap: 5px;
  position: relative;
  padding-bottom: 22px;
}

.cnc-12__cap {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  text-align: center;
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--cnc-12-mut);
}

.cnc-12__colon {
  align-self: center;
  margin-bottom: 22px;
  font-size: clamp(26px,5vw,40px);
  font-weight: 700;
  color: var(--cnc-12-acc);
  animation: cnc-12-blink 2s steps(1,end) infinite;
}

@keyframes cnc-12-blink {
  0%,
    50% {
    opacity: 1;
  }

  51%,
    100% {
    opacity: .28;
  }
}

.cnc-12__card {
  position: relative;
  display: block;
  width: clamp(44px,9vw,68px);
  height: clamp(72px,15vw,108px);
  perspective: 320px;
  font-size: clamp(38px,7.6vw,58px);
  font-weight: 700;
  line-height: 1;
}

.cnc-12__half {
  position: absolute;
  left: 0;
  right: 0;
  height: 50%;
  overflow: hidden;
  backface-visibility: hidden;
  background: var(--cnc-12-card);
  box-shadow: inset 0 0 0 1px oklch(0 0 0/.5);
}

.cnc-12__half span {
  position: absolute;
  left: 0;
  right: 0;
  height: 100%;
  display: grid;
  place-items: center;
  text-shadow: 0 2px 4px oklch(0 0 0/.6);
  line-height: 1;
  -webkit-font-smoothing: antialiased;
}

.cnc-12__half--t {
  top: 0;
  border-radius: 8px 8px 0 0;
  background: linear-gradient(180deg,var(--cnc-12-card),color-mix(in oklch,var(--cnc-12-card) 82%,black));
}

.cnc-12__half--t span {
  top: 0;
  height: 200%;
  place-items: center;
}

.cnc-12__half--b {
  bottom: 0;
  border-radius: 0 0 8px 8px;
  background: linear-gradient(180deg,var(--cnc-12-card2),color-mix(in oklch,var(--cnc-12-card2) 88%,white 6%));
}

.cnc-12__half--b span {
  bottom: 0;
  height: 200%;
  place-items: center;
}

.cnc-12__leaf {
  z-index: 2;
}

.cnc-12__leaf--t {
  transform-origin: bottom center;
  transform: rotateX(0);
}

.cnc-12__leaf--b {
  transform-origin: top center;
  transform: rotateX(90deg);
}

.cnc-12__card::after {
  content: "";
  position: absolute;
  left: 0;
  right: 0;
  top: calc(50% - 1px);
  height: 2px;
  background: oklch(0 0 0/.75);
  z-index: 5;
  border-radius: 1px;
}

.cnc-12__card.is-flip .cnc-12__leaf--t {
  animation: cnc-12-fold .3s cubic-bezier(.4,0,.9,.5) forwards;
}

.cnc-12__card.is-flip .cnc-12__leaf--b {
  animation: cnc-12-unfold .3s .3s cubic-bezier(.15,.7,.4,1.1) forwards;
}

@keyframes cnc-12-fold {
  to {
    transform: rotateX(-90deg);
    filter: brightness(.55);
  }
}

@keyframes cnc-12-unfold {
  from {
    transform: rotateX(90deg);
    filter: brightness(.6);
  }

  to {
    transform: rotateX(0);
    filter: brightness(1);
  }
}

.cnc-12__ctrls {
  display: flex;
  gap: 10px;
}

.cnc-12__btn {
  min-height: 44px;
  padding: 0 18px;
  border: 1px solid oklch(1 0 0/.16);
  border-radius: 99px;
  background: oklch(1 0 0/.06);
  color: var(--cnc-12-ink);
  font: inherit;
  font-size: 13.5px;
  font-weight: 620;
  cursor: pointer;
  transition: background .2s,transform .2s;
}

.cnc-12__btn:hover {
  background: oklch(1 0 0/.13);
  transform: translateY(-1px);
}

.cnc-12__btn:focus-visible {
  outline: 3px solid var(--cnc-12-acc);
  outline-offset: 3px;
}

.cnc-12__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cnc-12__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--cnc-12-mut);
  padding: 7px 14px;
  border: 1px solid oklch(1 0 0/.13);
  border-radius: 99px;
  text-align: center;
  max-width: min(100%,480px);
}

@media (prefers-reduced-motion: reduce) {
  .cnc-12__card.is-flip .cnc-12__leaf--t,
    .cnc-12__card.is-flip .cnc-12__leaf--b {
    animation-duration: 1ms;
  }

  .cnc-12__colon {
    animation: none;
  }
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('.cnc-12').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    const cards = [...root.querySelectorAll('.cnc-12__card')];
    const srEl = root.querySelector('.cnc-12__sr');
    const toggle = root.querySelector('[data-act="toggle"]');

    const half = (kind, leaf, d) => {
      const el = document.createElement('span');
      el.className = 'cnc-12__half cnc-12__half--' + kind + (leaf ? ' cnc-12__leaf cnc-12__leaf--' + kind : '');
      el.innerHTML = '<span>' + d + '</span>';
      return el;
    };
    const paint = (card, d) => {                    // static faces show the current digit
      card.innerHTML = '';
      card.append(half('t', false, d), half('b', false, d));
      card.dataset.d = d;
    };
    const flipTo = (card, d) => {
      if (card.dataset.d === String(d)) return;     // unchanged digits never animate
      const cur = card.dataset.d;
      card.innerHTML = '';
      card.append(half('t', false, d), half('b', false, cur), half('t', true, cur), half('b', true, d));
      card.classList.remove('is-flip'); void card.offsetWidth; card.classList.add('is-flip');
      card.dataset.d = d;
      setTimeout(() => { if (card.dataset.d === String(d)) paint(card, d); }, 640);
    };

    let secs = 0, running = true;
    const render = () => {
      const h = Math.floor(secs / 3600) % 100, m = Math.floor(secs / 60) % 60, s = secs % 60;
      const digits = String(h).padStart(2, '0') + String(m).padStart(2, '0') + String(s).padStart(2, '0');
      [...digits].forEach((d, i) => flipTo(cards[i], d));
      srEl.setAttribute('datetime', 'PT' + h + 'H' + m + 'M' + s + 'S');
      srEl.textContent = h + ' hours ' + m + ' minutes ' + s + ' seconds elapsed';
    };
    cards.forEach((c) => paint(c, '0'));
    secs = 3 * 3600 + 41 * 60 + 57; render();
    const id = setInterval(() => { if (running && document.visibilityState === 'visible') { secs++; render(); } }, 1000);
    toggle.addEventListener('click', () => {
      running = !running;
      toggle.textContent = running ? 'Pause' : 'Resume';
      toggle.setAttribute('aria-pressed', String(running));
    });
    root.querySelector('[data-act="reset"]').addEventListener('click', () => { secs = 0; render(); });
    addEventListener('pagehide', () => clearInterval(id), { once: true });
  });
})();
```
