---
source: "codefronts"
url: "https://codefronts.com/motion/css-gradient-animation/css-toggle-switch-track-glow/"
title: "CSS Toggle Switch Track Glow"
section: "motion"
category: "css-gradient-animation"
category_name: "CSS Gradient Animations"
description: "A settings panel with five checkbox-driven toggle switches where activating each switch floods the track with a continuously flowing gradient stream and…"
has_js: "true"
---

Here's a working CSS Gradient Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Toggle Switch Track Glow
Source: https://codefronts.com/motion/css-gradient-animation/css-toggle-switch-track-glow/

A settings panel with five checkbox-driven toggle switches where activating each switch floods the track with a continuously flowing gradient stream and emits a soft outer glow — all driven by the CSS :checked pseudo-class with zero JavaScript in the toggle logic.
## HTML
```html
<div class="ga-16">
  <div class="ga-16__card">
    <div class="ga-16__card-head">
      <div>
        <div class="ga-16__card-title">Notification Settings</div>
      </div>
      <span class="ga-16__card-sub">App v4.2</span>
    </div>

    <div class="ga-16__card-body">

      <div class="ga-16__row">
        <div class="ga-16__row-info">
          <span class="ga-16__row-label">Push notifications</span>
          <span class="ga-16__row-desc">Get alerts on your device in real time</span>
        </div>
        <label class="ga-16__toggle">
          <input type="checkbox" checked>
          <span class="ga-16__track"></span>
          <span class="ga-16__knob"></span>
        </label>
      </div>

      <div class="ga-16__row">
        <div class="ga-16__row-info">
          <span class="ga-16__row-label">Activity digest</span>
          <span class="ga-16__row-desc">Weekly summary of your workspace</span>
        </div>
        <label class="ga-16__toggle ga-16__toggle--emerald">
          <input type="checkbox">
          <span class="ga-16__track"></span>
          <span class="ga-16__knob"></span>
        </label>
      </div>

      <div class="ga-16__row">
        <div class="ga-16__row-info">
          <span class="ga-16__row-label">Security alerts</span>
          <span class="ga-16__row-desc">Notify on login from new devices</span>
        </div>
        <label class="ga-16__toggle ga-16__toggle--rose">
          <input type="checkbox" checked>
          <span class="ga-16__track"></span>
          <span class="ga-16__knob"></span>
        </label>
      </div>

      <div class="ga-16__row">
        <div class="ga-16__row-info">
          <span class="ga-16__row-label">Usage reports</span>
          <span class="ga-16__row-desc">Monthly billing and quota updates</span>
        </div>
        <label class="ga-16__toggle ga-16__toggle--amber">
          <input type="checkbox">
          <span class="ga-16__track"></span>
          <span class="ga-16__knob"></span>
        </label>
      </div>

      <div class="ga-16__row">
        <div class="ga-16__row-info">
          <span class="ga-16__row-label">Product updates</span>
          <span class="ga-16__row-desc">New features and release notes</span>
        </div>
        <label class="ga-16__toggle ga-16__toggle--cyan">
          <input type="checkbox" checked>
          <span class="ga-16__track"></span>
          <span class="ga-16__knob"></span>
        </label>
      </div>

    </div>

    <div class="ga-16__ctrl">
      <span class="ga-16__ctrl-label">Flow speed:</span>
      <button class="ga-16__ctrl-btn" data-dur="4s">Slow</button>
      <button class="ga-16__ctrl-btn active" data-dur="2s">Normal</button>
      <button class="ga-16__ctrl-btn" data-dur=".8s">Fast</button>
    </div>
  </div>
</div>
```
## CSS
```css
.ga-16,
.ga-16 *,
.ga-16 *::before,
.ga-16 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.ga-16 ::selection {
  background: rgba(99,102,241,.4);
  color: #fff;
}

.ga-16 {
  --bg: #090b12;
  --card-bg: #0f1120;
  --dur: 2s;
  width: 100%;
  min-height: 100vh;
  background: var(--bg);
  font-family: system-ui, -apple-system, sans-serif;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 24px;
}
/* Settings card */

.ga-16__card {
  width: 100%;
  max-width: 440px;
  background: var(--card-bg);
  border: 1px solid rgba(255,255,255,.06);
  border-radius: 20px;
  overflow: hidden;
}

.ga-16__card-head {
  padding: 20px 24px;
  border-bottom: 1px solid rgba(255,255,255,.05);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.ga-16__card-title {
  font-size: .88rem;
  font-weight: 800;
  color: rgba(255,255,255,.8);
}

.ga-16__card-sub {
  font-size: .7rem;
  font-weight: 600;
  color: rgba(255,255,255,.25);
  letter-spacing: .04em;
}

.ga-16__card-body {
  display: flex;
  flex-direction: column;
}
/* ── Row ── */

.ga-16__row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 18px 24px;
  border-bottom: 1px solid rgba(255,255,255,.04);
  transition: background .2s;
}

.ga-16__row:last-child {
  border-bottom: none;
}

.ga-16__row:hover {
  background: rgba(255,255,255,.02);
}

.ga-16__row-info {
  display: flex;
  flex-direction: column;
  gap: 3px;
}

.ga-16__row-label {
  font-size: .85rem;
  font-weight: 600;
  color: rgba(255,255,255,.7);
}

.ga-16__row-desc {
  font-size: .7rem;
  color: rgba(255,255,255,.28);
  line-height: 1.4;
}
/* ── Toggle switch ── */

.ga-16__toggle {
  position: relative;
  width: 52px;
  height: 28px;
  flex-shrink: 0;
  cursor: pointer;
}
/* Hidden checkbox */

.ga-16__toggle input {
  opacity: 0;
  width: 0;
  height: 0;
  position: absolute;
}
/* Track */

.ga-16__track {
  position: absolute;
  inset: 0;
  border-radius: 999px;
  background: rgba(255,255,255,.1);
  transition: background .3s ease;
  overflow: hidden;
}
/* Flowing gradient inside track — visible when checked */

.ga-16__track::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(
      90deg,
      var(--tc1, #6366f1),
      var(--tc2, #a855f7),
      var(--tc3, #06b6d4),
      var(--tc1, #6366f1)
    );
  background-size: 200% 100%;
  opacity: 0;
  transition: opacity .35s ease;
  animation: ga-16-flow var(--dur) linear infinite;
}

@keyframes ga-16-flow {
  0% {
    background-position: 0% 0;
  }

  100% {
    background-position: -200% 0;
  }
}
/* Glow behind track */

.ga-16__track::after {
  content: '';
  position: absolute;
  inset: -4px;
  border-radius: 999px;
  background: linear-gradient(90deg, var(--tc1, #6366f1), var(--tc2, #a855f7), var(--tc3, #06b6d4));
  filter: blur(8px);
  opacity: 0;
  transition: opacity .35s ease;
  z-index: -1;
}
/* Knob */

.ga-16__knob {
  position: absolute;
  top: 3px;
  left: 3px;
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background: #fff;
  box-shadow: 0 1px 4px rgba(0,0,0,.4);
  transition: transform .35s cubic-bezier(.34,1.56,.64,1), box-shadow .3s;
  z-index: 1;
}
/* Checked state */

input:checked ~ .ga-16__track::before {
  opacity: 1;
}

input:checked ~ .ga-16__track::after {
  opacity: .4;
}

input:checked ~ .ga-16__knob {
  transform: translateX(24px);
  box-shadow: 0 1px 8px rgba(0,0,0,.4), 0 0 0 2px rgba(255,255,255,.1);
}
/* Colour themes per row */

.ga-16__toggle--emerald {
  --tc1: #059669;
  --tc2: #10b981;
  --tc3: #34d399;
}

.ga-16__toggle--rose {
  --tc1: #e11d48;
  --tc2: #f43f5e;
  --tc3: #fb7185;
}

.ga-16__toggle--amber {
  --tc1: #d97706;
  --tc2: #f59e0b;
  --tc3: #fbbf24;
}

.ga-16__toggle--cyan {
  --tc1: #0891b2;
  --tc2: #06b6d4;
  --tc3: #22d3ee;
}
/* Focus ring */

.ga-16__toggle input:focus-visible ~ .ga-16__knob {
  outline: 2px solid rgba(99,102,241,.7);
  outline-offset: 2px;
}
/* Speed control */

.ga-16__ctrl {
  margin-top: 8px;
  padding: 14px 24px;
  display: flex;
  align-items: center;
  gap: 8px;
  border-top: 1px solid rgba(255,255,255,.05);
}

.ga-16__ctrl-label {
  font-size: .68rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: .1em;
  color: rgba(255,255,255,.2);
  margin-right: 4px;
}

.ga-16__ctrl-btn {
  padding: 4px 11px;
  font-size: .7rem;
  font-weight: 700;
  border-radius: 6px;
  border: 1px solid rgba(255,255,255,.08);
  background: rgba(255,255,255,.04);
  color: rgba(255,255,255,.3);
  cursor: pointer;
  transition: all .2s;
}

.ga-16__ctrl-btn.active,
.ga-16__ctrl-btn:hover {
  background: rgba(99,102,241,.15);
  border-color: rgba(99,102,241,.35);
  color: #a5b4fc;
}

@media (prefers-reduced-motion: reduce) {
  .ga-16__track::before {
    animation: none;
    background-position: 0% 0;
  }

  .ga-16__knob {
    transition: transform .2s, box-shadow .2s;
  }
}
```

## JavaScript
```js
(function() {
  const w = document.querySelector('.ga-16');
  w.querySelectorAll('.ga-16__ctrl-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      w.querySelectorAll('.ga-16__ctrl-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      w.style.setProperty('--dur', btn.dataset.dur);
    });
  });
})();
```
