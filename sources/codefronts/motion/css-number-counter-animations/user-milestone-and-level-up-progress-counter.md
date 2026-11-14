---
source: "codefronts"
url: "https://codefronts.com/motion/css-number-counter-animations/user-milestone-and-level-up-progress-counter/"
title: "User Milestone & Level-Up Progress Counter"
section: "motion"
category: "css-number-counter-animations"
category_name: "CSS Number Counter Animations"
description: "Duolingo-grade progression in a card: points count up, the XP bar fills past the level threshold, and when it crosses, the level badge flips over with a…"
has_js: "true"
---

Here's a working CSS Number Counter Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: User Milestone & Level-Up Progress Counter
Source: https://codefronts.com/motion/css-number-counter-animations/user-milestone-and-level-up-progress-counter/

Duolingo-grade progression in a card: points count up, the XP bar fills past the level threshold, and when it crosses, the level badge flips over with a burst and the bar wraps to the remainder. The reward is the overflow handling — most XP bars break at exactly the moment they matter, when a single action pushes the user past the line.
## HTML
```html
<section class="cnc-06" aria-label="User milestone and level up progress counter demo">
  <div class="cnc-06__stage">
    <article class="cnc-06__card" style="--cnc-06-p:0">
      <header class="cnc-06__head">
        <div class="cnc-06__badge" aria-hidden="true">
          <span class="cnc-06__lvl">7</span>
          <span class="cnc-06__ring"></span>
        </div>
        <div class="cnc-06__who">
          <p class="cnc-06__name">Jordan Rivera</p>
          <p class="cnc-06__rank">Level <b class="cnc-06__lvltxt">7</b> · Trailblazer</p>
        </div>
        <span class="cnc-06__streak" title="Current streak">🔥 <b>24</b></span>
      </header>
      <p class="cnc-06__xp"><span class="cnc-06__num">0</span><span class="cnc-06__xplabel">XP</span></p>
      <div class="cnc-06__track" role="progressbar" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0" aria-label="Progress to next level">
        <span class="cnc-06__fill"></span>
      </div>
      <p class="cnc-06__togo"><b class="cnc-06__remain">—</b> XP to Level <b class="cnc-06__next">8</b></p>
      <div class="cnc-06__acts">
        <button class="cnc-06__btn" type="button" data-xp="45">Complete lesson +45</button>
        <button class="cnc-06__btn cnc-06__btn--ghost" type="button" data-xp="180">Finish quest +180</button>
      </div>
      <p class="cnc-06__toast" aria-hidden="true">Level up!</p>
      <p class="cnc-06__sr" role="status" aria-live="polite"></p>
    </article>
    <p class="cnc-06__chip" aria-hidden="true">scaleX(var(--p)) bar · modulo level math · animationend-driven burst</p>
  </div>
</section>
```
## CSS
```css
.cnc-06,
.cnc-06 *,
.cnc-06 *::before,
.cnc-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cnc-06 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --cnc-06-bg: oklch(0.18 0.04 285);
  --cnc-06-card: oklch(0.24 0.05 285);
  --cnc-06-ink: oklch(0.98 0.005 280);
  --cnc-06-mut: oklch(0.72 0.03 285);
  --cnc-06-acc: oklch(0.78 0.19 85);
  --cnc-06-acc2: oklch(0.68 0.21 320);
  background: var(--cnc-06-bg);
  color: var(--cnc-06-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
}

.cnc-06__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 20px;
  padding: clamp(18px,4vw,48px);
  background: radial-gradient(60% 45% at 50% 12%,color-mix(in oklch,var(--cnc-06-acc2) 22%,transparent),transparent 70%);
}

.cnc-06__card {
  position: relative;
  width: min(100%,430px);
  padding: 24px;
  border-radius: 22px;
  overflow: hidden;
  background: var(--cnc-06-card);
  box-shadow: inset 0 0 0 1px oklch(1 0 0/.08),0 24px 60px oklch(0 0 0/.45);
}

.cnc-06__head {
  display: flex;
  align-items: center;
  gap: 14px;
}

.cnc-06__badge {
  position: relative;
  display: grid;
  place-items: center;
  width: 56px;
  height: 56px;
  flex: none;
  border-radius: 16px;
  background: linear-gradient(150deg,var(--cnc-06-acc),var(--cnc-06-acc2));
  color: oklch(0.2 0.04 300);
  font-size: 22px;
  font-weight: 800;
  transform-style: preserve-3d;
  transition: rotate .5s;
}

.cnc-06__card[data-levelup] .cnc-06__badge {
  animation: cnc-06-flip .9s cubic-bezier(.16,1,.3,1);
}

@keyframes cnc-06-flip {
  0% {
    rotate: y 0deg;
    scale: 1;
  }

  45% {
    rotate: y 180deg;
    scale: 1.18;
  }

  100% {
    rotate: y 360deg;
    scale: 1;
  }
}

.cnc-06__ring {
  position: absolute;
  inset: -6px;
  border-radius: 22px;
  border: 2px solid var(--cnc-06-acc);
  opacity: 0;
}

.cnc-06__card[data-levelup] .cnc-06__ring {
  animation: cnc-06-burst .9s cubic-bezier(.16,1,.3,1);
}

@keyframes cnc-06-burst {
  0% {
    opacity: .9;
    scale: .6;
  }

  100% {
    opacity: 0;
    scale: 2.1;
  }
}

.cnc-06__who {
  flex: 1;
  min-width: 0;
}

.cnc-06__name {
  font-size: 16px;
  font-weight: 680;
  letter-spacing: -.015em;
}

.cnc-06__rank {
  font-size: 12.5px;
  color: var(--cnc-06-mut);
  margin-top: 2px;
}

.cnc-06__streak {
  font-size: 13px;
  font-weight: 640;
  padding: 6px 10px;
  border-radius: 99px;
  background: oklch(1 0 0/.07);
}

.cnc-06__xp {
  display: flex;
  align-items: baseline;
  gap: 6px;
  margin-top: 22px;
  font-size: clamp(38px,7vw,52px);
  font-weight: 760;
  letter-spacing: -.05em;
  line-height: 1;
  font-variant-numeric: tabular-nums;
  font-feature-settings: 'tnum' 1;
}

.cnc-06__xplabel {
  font-size: .32em;
  font-weight: 660;
  letter-spacing: .1em;
  color: var(--cnc-06-mut);
}

.cnc-06__track {
  height: 14px;
  margin-top: 16px;
  border-radius: 99px;
  background: oklch(0 0 0/.28);
  overflow: hidden;
  box-shadow: inset 0 1px 2px oklch(0 0 0/.4);
}

.cnc-06__fill {
  display: block;
  height: 100%;
  width: 100%;
  border-radius: 99px;
  transform-origin: left center;
  transform: scaleX(var(--cnc-06-p,0));
  background: linear-gradient(90deg,var(--cnc-06-acc2),var(--cnc-06-acc));
  transition: transform .85s cubic-bezier(.16,1,.3,1);
}

.cnc-06__togo {
  margin-top: 10px;
  font-size: 12.5px;
  color: var(--cnc-06-mut);
}

.cnc-06__togo b {
  color: var(--cnc-06-ink);
  font-variant-numeric: tabular-nums;
}

.cnc-06__acts {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 20px;
}

.cnc-06__btn {
  flex: 1;
  min-width: 150px;
  min-height: 46px;
  padding: 0 16px;
  border: 0;
  border-radius: 12px;
  background: var(--cnc-06-acc);
  color: oklch(0.2 0.05 90);
  font: inherit;
  font-size: 13.5px;
  font-weight: 680;
  cursor: pointer;
  transition: transform .2s,filter .2s;
}

.cnc-06__btn--ghost {
  background: oklch(1 0 0/.08);
  color: var(--cnc-06-ink);
  box-shadow: inset 0 0 0 1px oklch(1 0 0/.16);
}

.cnc-06__btn:hover {
  transform: translateY(-2px);
  filter: brightness(1.06);
}

.cnc-06__btn:active {
  transform: translateY(0) scale(.98);
}

.cnc-06__btn:focus-visible {
  outline: 3px solid var(--cnc-06-acc2);
  outline-offset: 3px;
}

.cnc-06__toast {
  position: absolute;
  top: 18px;
  left: 50%;
  translate: -50% -20px;
  padding: 8px 16px;
  border-radius: 99px;
  background: var(--cnc-06-acc);
  color: oklch(0.2 0.05 90);
  font-size: 13px;
  font-weight: 760;
  letter-spacing: .02em;
  opacity: 0;
  pointer-events: none;
}

.cnc-06__card[data-levelup] .cnc-06__toast {
  animation: cnc-06-toast 1.6s cubic-bezier(.16,1,.3,1);
}

@keyframes cnc-06-toast {
  0% {
    opacity: 0;
    translate: -50% -20px;
  }

  18% {
    opacity: 1;
    translate: -50% 0;
  }

  75% {
    opacity: 1;
    translate: -50% 0;
  }

  100% {
    opacity: 0;
    translate: -50% -14px;
  }
}

.cnc-06__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cnc-06__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--cnc-06-mut);
  padding: 7px 14px;
  border: 1px solid oklch(1 0 0/.13);
  border-radius: 99px;
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .cnc-06 * {
    animation: none !important;
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  const nf = new Intl.NumberFormat('en-US');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const floorOf = (lvl) => Math.round(100 * Math.pow(lvl - 1, 1.4));   // level curve

  document.querySelectorAll('.cnc-06__card').forEach((card) => {
    if (card.dataset.wired) return;
    card.dataset.wired = '1';
    const numEl = card.querySelector('.cnc-06__num');
    const track = card.querySelector('.cnc-06__track');
    const remainEl = card.querySelector('.cnc-06__remain');
    const nextEl = card.querySelector('.cnc-06__next');
    const lvlEl = card.querySelector('.cnc-06__lvl');
    const lvlTxt = card.querySelector('.cnc-06__lvltxt');
    const say = card.querySelector('.cnc-06__sr');
    let xp = 1180, level = 7;

    const roll = (from, to, ms = 800) => {
      if (reduce) { numEl.textContent = nf.format(to); return; }
      const t0 = performance.now();
      const frame = (t) => {
        const p = Math.min(1, (t - t0) / ms);
        numEl.textContent = nf.format(p === 1 ? to : Math.round(from + (to - from) * (1 - Math.pow(1 - p, 4))));
        if (p < 1) requestAnimationFrame(frame);
      };
      requestAnimationFrame(frame);
    };

    const render = () => {
      while (xp >= floorOf(level + 1)) {                      // handle multi-level jumps
        level++;
        card.dataset.levelup = '1';
        lvlEl.textContent = level; lvlTxt.textContent = level;
        say.textContent = 'Level ' + level + ' reached';
        card.querySelector('.cnc-06__badge').addEventListener('animationend', () => delete card.dataset.levelup, { once: true });
      }
      const lo = floorOf(level), hi = floorOf(level + 1);
      const p = Math.min(1, (xp - lo) / (hi - lo));
      card.style.setProperty('--cnc-06-p', p.toFixed(4));
      track.setAttribute('aria-valuenow', Math.round(p * 100));
      remainEl.textContent = nf.format(hi - xp);
      nextEl.textContent = level + 1;
    };

    numEl.textContent = '0'; roll(0, xp, 1300); render();
    card.querySelectorAll('.cnc-06__btn').forEach((btn) => {
      btn.addEventListener('click', () => { const prev = xp; xp += +btn.dataset.xp; roll(prev, xp, 700); render(); });
    });
  });
})();
```
