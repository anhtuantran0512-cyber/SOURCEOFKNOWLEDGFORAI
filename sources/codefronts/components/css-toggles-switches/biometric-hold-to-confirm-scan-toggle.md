---
source: "codefronts"
url: "https://codefronts.com/components/css-toggles-switches/biometric-hold-to-confirm-scan-toggle/"
title: "Biometric Hold-to-Confirm Scan Toggle"
section: "components"
category: "css-toggles-switches"
category_name: "CSS Toggles & Switches"
description: "A destructive-action guard styled as a fingerprint sensor: press and HOLD for 1.2 seconds while a scan line sweeps and a progress ring fills — release early…"
has_js: "true"
---

Here's a working CSS Toggles & Switche from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Biometric Hold-to-Confirm Scan Toggle
Source: https://codefronts.com/components/css-toggles-switches/biometric-hold-to-confirm-scan-toggle/

A destructive-action guard styled as a fingerprint sensor: press and HOLD for 1.2 seconds while a scan line sweeps and a progress ring fills — release early and it disarms. Keyboard users get an equivalent hold on Space, and the final state is a real aria-checked switch.
## HTML
```html
<section class="tgl-11" aria-label="Hold to confirm biometric toggle">
  <div class="tgl-11__card">
    <div class="tgl-11__head"><b>Delete production database</b><span>Hold the sensor 1.2s to arm</span></div>
    <button type="button" id="tgl-11-btn" class="tgl-11__btn" role="switch" aria-checked="false">
      <svg class="tgl-11__fp" viewBox="0 0 40 48" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round">
        <path d="M20 6c-8 0-13 6-13 13v6"/><path d="M20 12c-5 0-8 4-8 8v9"/><path d="M20 18c-2.5 0-4 2-4 4v12"/><path d="M20 25v14"/><path d="M25 21c.6 1 .9 2.2.9 3.5V37"/><path d="M29.5 17c1.6 2 2.5 4.5 2.5 7v9"/><path d="M27 9.5c3.7 2.3 6 6.3 6 10.5v3"/>
      </svg>
      <span class="tgl-11__scan" aria-hidden="true"></span>
      <span class="tgl-11__ring" aria-hidden="true"></span>
    </button>
    <p class="tgl-11__state" id="tgl-11-state" aria-live="polite">Locked</p>
  </div>
</section>
```
## CSS
```css
@property --tgl-11-p {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

.tgl-11,
.tgl-11 *,
.tgl-11 *::before,
.tgl-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tgl-11 {
  --ok: oklch(0.75 0.16 155);
  --idle: #5b647a;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  background: #0f1219;
}

.tgl-11__card {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 18px;
  background: #171b25;
  border: 1px solid #242a3a;
  border-radius: 20px;
  padding: 30px 40px;
  width: min(340px,100%);
}

.tgl-11__head {
  text-align: center;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.tgl-11__head b {
  font-size: 16px;
  color: #e7eaf3;
}

.tgl-11__head span {
  font-size: 12.5px;
  color: #79819a;
}

.tgl-11__btn {
  position: relative;
  width: 104px;
  height: 104px;
  border-radius: 50%;
  border: none;
  background: #1e2331;
  color: var(--idle);
  cursor: pointer;
  display: grid;
  place-items: center;
  overflow: hidden;
  transition: color .3s;
  touch-action: none;
  -webkit-user-select: none;
  user-select: none;
}

.tgl-11__fp {
  width: 46px;
  height: 56px;
  position: relative;
  z-index: 1;
  transition: filter .3s;
}

.tgl-11__scan {
  position: absolute;
  left: 18px;
  right: 18px;
  top: 0;
  height: 3px;
  border-radius: 2px;
  background: oklch(0.75 0.15 220);
  box-shadow: 0 0 12px oklch(0.75 0.15 220);
  opacity: 0;
  z-index: 2;
}

.tgl-11__ring {
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: conic-gradient(var(--ok) var(--tgl-11-p),transparent 0);
  -webkit-mask: radial-gradient(circle,transparent 46px,#000 47px);
  mask: radial-gradient(circle,transparent 46px,#000 47px);
}

.tgl-11__btn.tgl-11--holding .tgl-11__scan {
  opacity: 1;
  animation: tgl-11-scan var(--hold,1.2s) ease-in-out;
}

.tgl-11__btn.tgl-11--holding .tgl-11__ring {
  animation: tgl-11-fill var(--hold,1.2s) linear forwards;
}

@keyframes tgl-11-scan {
  0% {
    transform: translateY(14px);
  }

  50% {
    transform: translateY(88px);
  }

  100% {
    transform: translateY(14px);
  }
}

@keyframes tgl-11-fill {
  from {
    --tgl-11-p: 0deg;
  }

  to {
    --tgl-11-p: 360deg;
  }
}

.tgl-11__btn[aria-checked="true"] {
  color: var(--ok);
}

.tgl-11__btn[aria-checked="true"] .tgl-11__fp {
  filter: drop-shadow(0 0 8px color-mix(in oklab,var(--ok) 70%,transparent));
}

.tgl-11__btn[aria-checked="true"] .tgl-11__ring {
  --tgl-11-p: 360deg;
}

.tgl-11__btn:focus-visible {
  outline: 3px solid oklch(0.7 0.15 220);
  outline-offset: 4px;
}

.tgl-11__state {
  font-size: 13px;
  font-weight: 600;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: #79819a;
  min-height: 1.2em;
}

@media (prefers-reduced-motion: reduce) {
  .tgl-11__btn.tgl-11--holding .tgl-11__scan {
    animation: none;
    opacity: 1;
    transform: translateY(50px);
  }
}
```

## JavaScript
```js
(() => {
  const HOLD_MS = 1200;
  const btn = document.querySelector('#tgl-11-btn');
  const state = document.querySelector('#tgl-11-state');
  let timer = null;
  const arm = () => {
    if (timer) return;
    btn.classList.add('tgl-11--holding');
    state.textContent = 'Scanning…';
    timer = setTimeout(() => {
      timer = null;
      btn.classList.remove('tgl-11--holding');
      const next = btn.getAttribute('aria-checked') !== 'true';
      btn.setAttribute('aria-checked', String(next));
      state.textContent = next ? 'Armed — verified' : 'Locked';
    }, HOLD_MS);
  };
  const disarm = () => {
    if (!timer) return;
    clearTimeout(timer); timer = null;
    btn.classList.remove('tgl-11--holding');
    state.textContent = 'Released too early';
  };
  btn.addEventListener('pointerdown', (e) => { btn.setPointerCapture(e.pointerId); arm(); });
  ['pointerup','pointercancel','pointerleave'].forEach(t => btn.addEventListener(t, disarm));
  btn.addEventListener('keydown', (e) => { if ((e.key === ' ' || e.key === 'Enter') && !e.repeat) { e.preventDefault(); arm(); } });
  btn.addEventListener('keyup', (e) => { if (e.key === ' ' || e.key === 'Enter') disarm(); });
})();
```
