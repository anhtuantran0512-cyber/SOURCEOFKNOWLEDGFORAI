---
source: "codefronts"
url: "https://codefronts.com/motion/css-number-counter-animations/cyberpunk-gaming-hud/"
title: "Gaming Score & XP Points Counter"
section: "motion"
category: "css-number-counter-animations"
category_name: "CSS Number Counter Animations"
description: "A game HUD built around the problem every score counter hits: points arrive as a stream of overlapping deltas, not as one final value."
has_js: "true"
---

Here's a working CSS Number Counter Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Gaming Score & XP Points Counter
Source: https://codefronts.com/motion/css-number-counter-animations/cyberpunk-gaming-hud/

A game HUD built around the problem every score counter hits: points arrive as a stream of overlapping deltas, not as one final value. A naive tween restarts on each hit and silently drops points. This one keeps a persistent target and a single chasing loop, so twenty hits in two seconds all land — with combo multiplier, floating point pops, an XP bar and a level-up flash.
## HTML
```html
<section class="cnc-23" aria-label="Gaming score and XP points counter demo">
  <div class="cnc-23__stage">
    <div class="cnc-23__hud">
      <header class="cnc-23__top">
        <span class="cnc-23__rank">Rank <b class="cnc-23__rankn">Gold III</b></span>
        <span class="cnc-23__lvl">LVL <b class="cnc-23__lvln">7</b></span>
      </header>
      <p class="cnc-23__score"><span class="cnc-23__num" aria-hidden="true">0</span></p>
      <p class="cnc-23__sub">Score · <b class="cnc-23__combo">×1</b> combo</p>
      <div class="cnc-23__xp">
        <div class="cnc-23__track" role="progressbar" aria-label="Experience to next level" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0">
          <span class="cnc-23__fill"></span>
        </div>
        <p class="cnc-23__xplab"><span class="cnc-23__xpn">0</span> / 1,000 XP to level <span class="cnc-23__next">8</span></p>
      </div>
      <div class="cnc-23__pops" aria-hidden="true"></div>
      <div class="cnc-23__actions">
        <button class="cnc-23__btn" type="button" data-hit="120">Land a hit <small>+120</small></button>
        <button class="cnc-23__btn cnc-23__btn--crit" type="button" data-hit="750">Critical <small>+750</small></button>
        <button class="cnc-23__btn cnc-23__btn--ghost" type="button" data-reset>Reset</button>
      </div>
      <p class="cnc-23__sr" role="status" aria-live="polite"></p>
    </div>
    <p class="cnc-23__chip" aria-hidden="true">mutable target + self-cancelling rAF · @property &lt;percentage&gt; XP · animationend cleanup</p>
  </div>
</section>
```
## CSS
```css
.cnc-23,
.cnc-23 *,
.cnc-23 *::before,
.cnc-23 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

@property --cnc-23-xp {
  syntax: '<percentage>';
  inherits: true;
  initial-value: 0%;
}

.cnc-23 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --cnc-23-bg: oklch(0.15 0.04 285);
  --cnc-23-card: oklch(0.21 0.05 288);
  --cnc-23-ink: oklch(0.98 0.01 285);
  --cnc-23-mut: oklch(0.70 0.03 288);
  --cnc-23-acc: oklch(0.80 0.19 195);
  --cnc-23-hot: oklch(0.75 0.22 340);
  background: radial-gradient(90% 70% at 50% 0%,oklch(0.24 0.08 300),var(--cnc-23-bg));
  color: var(--cnc-23-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
}

.cnc-23__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 18px;
  padding: clamp(16px,4vw,44px);
}

.cnc-23__hud {
  position: relative;
  width: min(100%,470px);
  padding: clamp(20px,4vw,28px);
  border-radius: 24px;
  background: linear-gradient(180deg,color-mix(in oklch,var(--cnc-23-acc) 8%,var(--cnc-23-card)),var(--cnc-23-card));
  box-shadow: 0 0 0 1px oklch(1 0 0/.09),0 0 60px color-mix(in oklch,var(--cnc-23-acc) 12%,transparent),0 30px 70px oklch(0 0 0/.55);
}

.cnc-23__hud[data-flash] {
  animation: cnc-23-flash .9s ease-out;
}

@keyframes cnc-23-flash {
  0% {
    box-shadow: 0 0 0 1px var(--cnc-23-acc),0 0 0 0 color-mix(in oklch,var(--cnc-23-acc) 55%,transparent),0 30px 70px oklch(0 0 0/.55);
  }

  100% {
    box-shadow: 0 0 0 1px oklch(1 0 0/.09),0 0 0 34px color-mix(in oklch,var(--cnc-23-acc) 0%,transparent),0 30px 70px oklch(0 0 0/.55);
  }
}

.cnc-23__top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  font-size: 11px;
  font-weight: 660;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--cnc-23-mut);
}

.cnc-23__top b {
  color: var(--cnc-23-ink);
  letter-spacing: .04em;
}

.cnc-23__lvl {
  padding: 5px 11px;
  border-radius: 99px;
  background: color-mix(in oklch,var(--cnc-23-hot) 18%,transparent);
  color: var(--cnc-23-hot);
}

.cnc-23__lvl b {
  color: inherit;
}

.cnc-23__score {
  margin-top: 16px;
  font-size: clamp(48px,12vw,74px);
  font-weight: 800;
  letter-spacing: -.06em;
  line-height: .92;
  font-variant-numeric: tabular-nums;
  font-feature-settings: 'tnum' 1;
  text-shadow: 0 0 30px color-mix(in oklch,var(--cnc-23-acc) 45%,transparent);
}

.cnc-23__sub {
  margin-top: 6px;
  font-size: 12.5px;
  color: var(--cnc-23-mut);
}

.cnc-23__combo {
  color: var(--cnc-23-acc);
  font-weight: 760;
  font-variant-numeric: tabular-nums;
  display: inline-block;
  transition: scale .25s cubic-bezier(.2,1.6,.4,1);
}

.cnc-23__combo[data-bump] {
  scale: 1.28;
}

.cnc-23__xp {
  margin-top: 22px;
}

.cnc-23__track {
  height: 12px;
  border-radius: 99px;
  background: oklch(1 0 0/.1);
  overflow: hidden;
  box-shadow: inset 0 0 0 1px oklch(1 0 0/.07);
}

.cnc-23__fill {
  display: block;
  height: 100%;
  width: var(--cnc-23-xp);
  border-radius: 99px;
  background: linear-gradient(90deg,var(--cnc-23-hot),var(--cnc-23-acc));
  box-shadow: 0 0 18px color-mix(in oklch,var(--cnc-23-acc) 55%,transparent);
  transition: --cnc-23-xp .7s cubic-bezier(.16,1,.3,1);
}

.cnc-23__xplab {
  margin-top: 9px;
  font-size: 11.5px;
  color: var(--cnc-23-mut);
  font-variant-numeric: tabular-nums;
}

.cnc-23__pops {
  position: absolute;
  top: 96px;
  right: 26px;
  width: 120px;
  height: 120px;
  pointer-events: none;
}

.cnc-23__pops b {
  position: absolute;
  right: 0;
  top: 60px;
  font-size: 17px;
  font-weight: 780;
  color: var(--cnc-23-acc);
  font-variant-numeric: tabular-nums;
  text-shadow: 0 0 14px color-mix(in oklch,var(--cnc-23-acc) 60%,transparent);
  animation: cnc-23-pop .95s cubic-bezier(.16,1,.3,1) forwards;
}

.cnc-23__pops b[data-crit] {
  font-size: 23px;
  color: var(--cnc-23-hot);
  text-shadow: 0 0 18px color-mix(in oklch,var(--cnc-23-hot) 70%,transparent);
}

@keyframes cnc-23-pop {
  0% {
    opacity: 0;
    transform: translateY(14px) scale(.8);
  }

  18% {
    opacity: 1;
    transform: translateY(0) scale(1.06);
  }

  100% {
    opacity: 0;
    transform: translateY(-58px) scale(1);
  }
}

.cnc-23__actions {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 24px;
}

.cnc-23__btn {
  flex: 1 1 128px;
  min-height: 46px;
  padding: 11px 14px;
  border: 0;
  border-radius: 14px;
  font: inherit;
  font-size: 13.5px;
  font-weight: 700;
  color: oklch(0.16 0.04 285);
  background: var(--cnc-23-acc);
  cursor: pointer;
  transition: transform .16s cubic-bezier(.2,1.5,.4,1),filter .18s;
}

.cnc-23__btn small {
  font-weight: 640;
  opacity: .7;
  margin-left: 5px;
}

.cnc-23__btn:hover {
  filter: brightness(1.08);
}

.cnc-23__btn:active {
  transform: scale(.96);
}

.cnc-23__btn:focus-visible {
  outline: 3px solid var(--cnc-23-ink);
  outline-offset: 3px;
}

.cnc-23__btn--crit {
  background: var(--cnc-23-hot);
  color: oklch(0.99 0.01 340);
}

.cnc-23__btn--ghost {
  flex: 0 0 auto;
  background: transparent;
  color: var(--cnc-23-mut);
  box-shadow: inset 0 0 0 1px oklch(1 0 0/.16);
}

.cnc-23__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cnc-23__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--cnc-23-mut);
  padding: 7px 14px;
  border: 1px solid oklch(1 0 0/.13);
  border-radius: 99px;
  text-align: center;
  max-width: min(100%,600px);
}

@media (prefers-reduced-motion: reduce) {
  .cnc-23 * {
    animation-duration: .01ms !important;
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  const nf = new Intl.NumberFormat('en-US');
  const PER_LEVEL = 1000;

  document.querySelectorAll('.cnc-23__hud').forEach((hud) => {
    if (hud.dataset.wired) return;
    hud.dataset.wired = '1';
    const numEl = hud.querySelector('.cnc-23__num');
    const comboEl = hud.querySelector('.cnc-23__combo');
    const fill = hud.querySelector('.cnc-23__fill');
    const track = hud.querySelector('.cnc-23__track');
    const xpn = hud.querySelector('.cnc-23__xpn');
    const lvln = hud.querySelector('.cnc-23__lvln');
    const nextn = hud.querySelector('.cnc-23__next');
    const rankn = hud.querySelector('.cnc-23__rankn');
    const pops = hud.querySelector('.cnc-23__pops');
    const sr = hud.querySelector('.cnc-23__sr');
    const RANKS = ['Bronze I', 'Silver II', 'Gold III', 'Platinum IV', 'Diamond V', 'Mythic'];

    let target = 0, shown = 0, raf = 0, combo = 1, level = 7, xp = 0, lastHit = 0, decay = 0;

    const chase = () => {
      const gap = target - shown;
      shown += Math.sign(gap) * Math.max(1, Math.ceil(Math.abs(gap) * 0.16));
      numEl.textContent = nf.format(shown);
      raf = shown === target ? 0 : requestAnimationFrame(chase);
    };

    const paintXp = () => {
      const pct = (xp / PER_LEVEL) * 100;
      fill.style.setProperty('--cnc-23-xp', pct + '%');
      track.setAttribute('aria-valuenow', Math.round(pct));
      xpn.textContent = nf.format(xp);
      lvln.textContent = level;
      nextn.textContent = level + 1;
      rankn.textContent = RANKS[Math.min(RANKS.length - 1, Math.floor(level / 3))];
    };

    const pop = (pts, crit) => {
      const b = document.createElement('b');
      b.textContent = '+' + nf.format(pts);
      if (crit) b.dataset.crit = '';
      b.style.right = Math.round(Math.random() * 46) + 'px';
      pops.append(b);
      b.addEventListener('animationend', () => b.remove(), { once: true });
    };

    const add = (base, crit) => {
      const now = performance.now();
      combo = now - lastHit < 1600 ? Math.min(9, combo + 1) : 1;
      lastHit = now;
      comboEl.textContent = '×' + combo;
      comboEl.dataset.bump = '';
      setTimeout(() => delete comboEl.dataset.bump, 260);
      clearTimeout(decay);
      decay = setTimeout(() => { combo = 1; comboEl.textContent = '×1'; }, 1700);

      const pts = base * combo;
      target += pts;
      if (!raf) raf = requestAnimationFrame(chase);
      pop(pts, crit);

      xp += pts;
      while (xp >= PER_LEVEL) {
        xp -= PER_LEVEL; level += 1;
        hud.dataset.flash = '';
        hud.addEventListener('animationend', () => delete hud.dataset.flash, { once: true });
        sr.textContent = 'Level ' + level + ' reached. Score ' + nf.format(target) + '.';
      }
      paintXp();
    };

    hud.querySelectorAll('[data-hit]').forEach((btn) => {
      btn.addEventListener('click', () => add(+btn.dataset.hit, btn.dataset.hit === '750'));
    });
    hud.querySelector('[data-reset]').addEventListener('click', () => {
      target = 0; shown = 0; xp = 0; level = 7; combo = 1;
      numEl.textContent = '0'; comboEl.textContent = '×1';
      cancelAnimationFrame(raf); raf = 0;
      paintXp(); sr.textContent = 'Run reset.';
    });
    paintXp();
  });
})();
```
