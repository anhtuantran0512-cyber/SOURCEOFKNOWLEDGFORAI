---
source: "codefronts"
url: "https://codefronts.com/motion/css-gradient-animation/css-striped-progress-bar-loader/"
title: "CSS Striped Progress Bar Loader"
section: "motion"
category: "css-gradient-animation"
category_name: "CSS Gradient Animations"
description: "Five progress bar variants — indigo deploy, emerald storage, amber CPU, rose queue, plus an indeterminate loader — all using repeating-linear-gradient…"
has_js: "true"
---

Here's a working CSS Gradient Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Striped Progress Bar Loader
Source: https://codefronts.com/motion/css-gradient-animation/css-striped-progress-bar-loader/

Five progress bar variants — indigo deploy, emerald storage, amber CPU, rose queue, plus an indeterminate loader — all using repeating-linear-gradient diagonal stripes that scroll infinitely across the fill to signal active loading status.
## HTML
```html
<div class="ga-14">

  <div class="ga-14__section-label">Standard bars</div>

  <div class="ga-14__bar">
    <div class="ga-14__bar-meta">
      <span class="ga-14__bar-label">Deploying to production</span>
      <span class="ga-14__bar-pct">72%</span>
    </div>
    <div class="ga-14__track">
      <div class="ga-14__fill ga-14__fill--indigo"></div>
    </div>
  </div>

  <div class="ga-14__bar">
    <div class="ga-14__bar-meta">
      <span class="ga-14__bar-label">Storage used</span>
      <span class="ga-14__bar-pct">45 / 100 GB</span>
    </div>
    <div class="ga-14__track ga-14__track--thin">
      <div class="ga-14__fill ga-14__fill--emerald"></div>
    </div>
  </div>

  <div class="ga-14__bar">
    <div class="ga-14__bar-meta">
      <span class="ga-14__bar-label">CPU utilisation</span>
      <span class="ga-14__bar-pct">88%</span>
    </div>
    <div class="ga-14__track ga-14__track--thick">
      <div class="ga-14__fill ga-14__fill--amber ga-14__fill--thick"></div>
    </div>
  </div>

  <div class="ga-14__bar">
    <div class="ga-14__bar-meta">
      <span class="ga-14__bar-label">Request queue</span>
      <span class="ga-14__bar-pct">31%</span>
    </div>
    <div class="ga-14__track">
      <div class="ga-14__fill ga-14__fill--rose"></div>
    </div>
  </div>

  <div class="ga-14__section-label">Indeterminate (unknown duration)</div>

  <div class="ga-14__bar">
    <div class="ga-14__bar-meta">
      <span class="ga-14__bar-label">Syncing cloud data…</span>
    </div>
    <div class="ga-14__track ga-14__track--indeterminate">
      <div class="ga-14__fill ga-14__fill--indeterminate"></div>
    </div>
  </div>

  <div class="ga-14__steps">
    <span class="ga-14__step ga-14__step--done">Build</span>
    <span class="ga-14__step ga-14__step--done">Test</span>
    <span class="ga-14__step ga-14__step--done">Package</span>
    <span class="ga-14__step">Deploy</span>
    <span class="ga-14__step">Verify</span>
  </div>

  <div class="ga-14__ctrl">
    <span class="ga-14__ctrl-label">Stripe speed:</span>
    <button class="ga-14__ctrl-btn" data-dur="1.5s">Slow</button>
    <button class="ga-14__ctrl-btn active" data-dur=".7s">Normal</button>
    <button class="ga-14__ctrl-btn" data-dur=".3s">Fast</button>
  </div>

</div>
```
## CSS
```css
.ga-14,
.ga-14 *,
.ga-14 *::before,
.ga-14 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.ga-14 ::selection {
  background: rgba(99,102,241,.4);
  color: #fff;
}

.ga-14 {
  --bg: #0c0d16;
  --track: #1a1c2e;
  --dur-stripe: .7s;
  width: 100%;
  min-height: 100vh;
  background: var(--bg);
  font-family: system-ui, -apple-system, sans-serif;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 36px;
  padding: 48px 32px;
}
/* ── Progress bar shell ── */

.ga-14__bar {
  width: 100%;
  max-width: 540px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.ga-14__bar-meta {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
}

.ga-14__bar-label {
  font-size: .78rem;
  font-weight: 700;
  color: rgba(255,255,255,.55);
}

.ga-14__bar-pct {
  font-size: .7rem;
  font-weight: 800;
  color: rgba(255,255,255,.4);
  font-variant-numeric: tabular-nums;
}
/* Track */

.ga-14__track {
  width: 100%;
  height: 14px;
  background: var(--track);
  border-radius: 999px;
  overflow: hidden;
  position: relative;
}
/* Fill */

.ga-14__fill {
  height: 100%;
  border-radius: 999px;
  position: relative;
  overflow: hidden;
  transition: width .4s ease;
}
/* Stripe overlay on fill using repeating-linear-gradient */

.ga-14__fill::after {
  content: '';
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(
      -45deg,
      rgba(255,255,255,.12) 0px,
      rgba(255,255,255,.12) 8px,
      transparent 8px,
      transparent 16px
    );
  background-size: 22.63px 22.63px;
  /* √(16²+16²) for perfect diagonal tiling */
  animation: ga-14-stripe var(--dur-stripe) linear infinite;
}

@keyframes ga-14-stripe {
  to {
    background-position: 22.63px 0;
  }
}
/* Colour variants */

.ga-14__fill--indigo {
  background: linear-gradient(90deg, #6366f1, #818cf8);
  width: 72%;
}

.ga-14__fill--emerald {
  background: linear-gradient(90deg, #059669, #34d399);
  width: 45%;
}

.ga-14__fill--amber {
  background: linear-gradient(90deg, #d97706, #fbbf24);
  width: 88%;
}

.ga-14__fill--rose {
  background: linear-gradient(90deg, #e11d48, #fb7185);
  width: 31%;
}

.ga-14__fill--cyan {
  background: linear-gradient(90deg, #0891b2, #22d3ee);
  width: 60%;
}
/* Thin track variant */

.ga-14__track--thin {
  height: 8px;
}

.ga-14__track--thick {
  height: 20px;
  border-radius: 6px;
}

.ga-14__fill--thick {
  border-radius: 4px;
}
/* Indeterminate / infinite fill variant */

.ga-14__fill--indeterminate {
  width: 40%;
  position: absolute;
  animation: ga-14-indeterminate 1.8s ease-in-out infinite;
  background: linear-gradient(90deg, #6366f1, #a855f7, #ec4899);
}

@keyframes ga-14-indeterminate {
  0% {
    left: -40%;
  }

  100% {
    left: 110%;
  }
}

.ga-14__fill--indeterminate::after {
  animation: none;
}

.ga-14__track--indeterminate {
  overflow: hidden;
  position: relative;
  height: 10px;
}
/* Step labels under bar */

.ga-14__steps {
  display: flex;
  justify-content: space-between;
  max-width: 540px;
  width: 100%;
}

.ga-14__step {
  font-size: .62rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: .07em;
  color: rgba(255,255,255,.2);
}

.ga-14__step--done {
  color: #818cf8;
}
/* Section label */

.ga-14__section-label {
  font-size: .65rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: .12em;
  color: rgba(255,255,255,.2);
  width: 100%;
  max-width: 540px;
  margin-bottom: -20px;
}
/* speed control */

.ga-14__ctrl {
  display: flex;
  align-items: center;
  gap: 8px;
}

.ga-14__ctrl-label {
  font-size: .68rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: .09em;
  color: rgba(255,255,255,.2);
}

.ga-14__ctrl-btn {
  padding: 4px 12px;
  font-size: .7rem;
  font-weight: 700;
  border-radius: 6px;
  border: 1px solid rgba(255,255,255,.1);
  background: rgba(255,255,255,.05);
  color: rgba(255,255,255,.35);
  cursor: pointer;
  transition: all .2s;
}

.ga-14__ctrl-btn.active,
.ga-14__ctrl-btn:hover {
  background: rgba(99,102,241,.15);
  border-color: rgba(99,102,241,.35);
  color: #a5b4fc;
}

@media (prefers-reduced-motion: reduce) {
  .ga-14__fill::after {
    animation: none;
  }

  .ga-14__fill--indeterminate {
    animation: none;
    left: 30%;
  }
}
```

## JavaScript
```js
(function() {
  const w = document.querySelector('.ga-14');
  w.querySelectorAll('.ga-14__ctrl-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      w.querySelectorAll('.ga-14__ctrl-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      w.style.setProperty('--dur-stripe', btn.dataset.dur);
    });
  });
})();
```
