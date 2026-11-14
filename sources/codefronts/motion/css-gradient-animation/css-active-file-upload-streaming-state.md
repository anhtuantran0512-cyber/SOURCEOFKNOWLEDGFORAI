---
source: "codefronts"
url: "https://codefronts.com/motion/css-gradient-animation/css-active-file-upload-streaming-state/"
title: "CSS Active File Upload Streaming State"
section: "motion"
category: "css-gradient-animation"
category_name: "CSS Gradient Animations"
description: "A file upload UI showing three upload states — active uploading with a spinning conic-gradient border and shimmer progress fill, completed with a green fill,…"
has_js: "true"
---

Here's a working CSS Gradient Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Active File Upload Streaming State
Source: https://codefronts.com/motion/css-gradient-animation/css-active-file-upload-streaming-state/

A file upload UI showing three upload states — active uploading with a spinning conic-gradient border and shimmer progress fill, completed with a green fill, and failed with a red fill — plus a styled drop zone.
## HTML
```html
<div class="ga-15">

  <!-- Uploading -->
  <div class="ga-15__card ga-15__card--uploading">
    <div class="ga-15__card-inner">
      <div class="ga-15__file">
        <div class="ga-15__file-icon ga-15__file-icon--img">🖼</div>
        <div class="ga-15__file-info">
          <div class="ga-15__file-name">hero-banner-v3.png</div>
          <div class="ga-15__file-size">4.2 MB</div>
        </div>
        <span class="ga-15__file-action">✕</span>
      </div>
      <div class="ga-15__prog-row">
        <span class="ga-15__prog-status ga-15__prog-status--up">⟳ Uploading…</span>
        <span class="ga-15__prog-pct">63%</span>
      </div>
      <div class="ga-15__track">
        <div class="ga-15__fill ga-15__fill--up"></div>
      </div>
    </div>
  </div>

  <!-- Done -->
  <div class="ga-15__card ga-15__card--done">
    <div class="ga-15__card-inner">
      <div class="ga-15__file">
        <div class="ga-15__file-icon ga-15__file-icon--pdf">📄</div>
        <div class="ga-15__file-info">
          <div class="ga-15__file-name">proposal-final.pdf</div>
          <div class="ga-15__file-size">1.8 MB</div>
        </div>
        <span class="ga-15__file-action">✕</span>
      </div>
      <div class="ga-15__prog-row">
        <span class="ga-15__prog-status ga-15__prog-status--done">✓ Complete</span>
        <span class="ga-15__prog-pct">100%</span>
      </div>
      <div class="ga-15__track">
        <div class="ga-15__fill ga-15__fill--done"></div>
      </div>
    </div>
  </div>

  <!-- Error -->
  <div class="ga-15__card ga-15__card--error">
    <div class="ga-15__card-inner">
      <div class="ga-15__file">
        <div class="ga-15__file-icon ga-15__file-icon--zip">📦</div>
        <div class="ga-15__file-info">
          <div class="ga-15__file-name">assets-bundle.zip</div>
          <div class="ga-15__file-size">92.4 MB</div>
        </div>
        <span class="ga-15__file-action">↺</span>
      </div>
      <div class="ga-15__prog-row">
        <span class="ga-15__prog-status ga-15__prog-status--err">⚠ Failed</span>
        <span class="ga-15__prog-pct">40%</span>
      </div>
      <div class="ga-15__track">
        <div class="ga-15__fill ga-15__fill--err"></div>
      </div>
    </div>
  </div>

  <!-- Drop zone -->
  <div class="ga-15__drop">
    <span class="ga-15__drop-icon">⬆</span>
    <span class="ga-15__drop-text">Drop files here</span>
    <span class="ga-15__drop-sub">PNG, JPG, PDF, ZIP — max 100 MB</span>
  </div>

  <div class="ga-15__ctrl">
    <button class="ga-15__ctrl-btn" data-dur="4s">Slow</button>
    <button class="ga-15__ctrl-btn active" data-dur="2s">Normal</button>
    <button class="ga-15__ctrl-btn" data-dur=".8s">Fast</button>
  </div>
</div>
```
## CSS
```css
.ga-15,
.ga-15 *,
.ga-15 *::before,
.ga-15 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.ga-15 ::selection {
  background: rgba(6,182,212,.4);
  color: #fff;
}

.ga-15 {
  --bg: #080d14;
  --card-bg: #0e1520;
  --dur: 2s;
  width: 100%;
  min-height: 100vh;
  background: var(--bg);
  font-family: system-ui, -apple-system, sans-serif;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;
  gap: 20px;
  padding: 48px 24px;
}
/* ── Upload card ── */

.ga-15__card {
  width: 280px;
  background: var(--card-bg);
  border-radius: 16px;
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 14px;
  position: relative;
  overflow: hidden;
}
/* Glowing border pulse on uploading card */

.ga-15__card--uploading::before {
  content: '';
  position: absolute;
  inset: -2px;
  border-radius: 18px;
  background: conic-gradient(
      from var(--r, 0deg),
      transparent 0deg,
      #06b6d4 60deg,
      #818cf8 120deg,
      transparent 180deg,
      transparent 360deg
    );
  animation: ga-15-spin var(--dur) linear infinite;
  z-index: 0;
}

.ga-15__card--uploading::after {
  content: '';
  position: absolute;
  inset: 2px;
  background: var(--card-bg);
  border-radius: 14px;
  z-index: 1;
}

@property --r {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

@keyframes ga-15-spin {
  to {
    --r: 360deg;
  }
}
/* Idle card — static border */

.ga-15__card--idle {
  border: 1px solid rgba(255,255,255,.06);
}
/* Done card */

.ga-15__card--done {
  border: 1px solid rgba(16,185,129,.2);
}

.ga-15__card--error {
  border: 1px solid rgba(239,68,68,.2);
}

.ga-15__card-inner {
  position: relative;
  z-index: 2;
  display: flex;
  flex-direction: column;
  gap: 14px;
}
/* File row */

.ga-15__file {
  display: flex;
  align-items: center;
  gap: 12px;
}

.ga-15__file-icon {
  width: 38px;
  height: 38px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1rem;
  flex-shrink: 0;
}

.ga-15__file-icon--img {
  background: rgba(99,102,241,.15);
}

.ga-15__file-icon--pdf {
  background: rgba(239,68,68,.12);
}

.ga-15__file-icon--zip {
  background: rgba(245,158,11,.12);
}

.ga-15__file-info {
  flex: 1;
  min-width: 0;
}

.ga-15__file-name {
  font-size: .82rem;
  font-weight: 700;
  color: rgba(255,255,255,.75);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.ga-15__file-size {
  font-size: .7rem;
  color: rgba(255,255,255,.3);
  margin-top: 2px;
}

.ga-15__file-action {
  font-size: .9rem;
  cursor: pointer;
  color: rgba(255,255,255,.25);
  transition: color .2s;
  flex-shrink: 0;
}

.ga-15__file-action:hover {
  color: rgba(255,255,255,.6);
}
/* Progress row */

.ga-15__prog-row {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
}

.ga-15__prog-status {
  font-size: .7rem;
  font-weight: 700;
  display: flex;
  align-items: center;
  gap: 5px;
}

.ga-15__prog-status--up {
  color: #67e8f9;
}

.ga-15__prog-status--done {
  color: #34d399;
}

.ga-15__prog-status--err {
  color: #f87171;
}

.ga-15__prog-status--idle {
  color: rgba(255,255,255,.3);
}

.ga-15__prog-pct {
  font-size: .7rem;
  font-weight: 800;
  font-variant-numeric: tabular-nums;
  color: rgba(255,255,255,.35);
}
/* Track */

.ga-15__track {
  width: 100%;
  height: 5px;
  border-radius: 999px;
  background: rgba(255,255,255,.07);
  overflow: hidden;
  position: relative;
}

.ga-15__fill {
  height: 100%;
  border-radius: 999px;
  position: relative;
  overflow: hidden;
}

.ga-15__fill--up {
  background: linear-gradient(90deg, #0891b2, #22d3ee, #818cf8);
  width: 63%;
  animation: ga-15-fill-pulse var(--dur) ease-in-out infinite;
}

@keyframes ga-15-fill-pulse {
  0%,
    100% {
    opacity: 1;
  }

  50% {
    opacity: .7;
  }
}
/* Shimmer on uploading fill */

.ga-15__fill--up::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(90deg, transparent 0%, rgba(255,255,255,.25) 50%, transparent 100%);
  animation: ga-15-shimmer 1.2s linear infinite;
}

@keyframes ga-15-shimmer {
  from {
    transform: translateX(-100%);
  }

  to {
    transform: translateX(200%);
  }
}

.ga-15__fill--done {
  background: #10b981;
  width: 100%;
}

.ga-15__fill--err {
  background: #ef4444;
  width: 40%;
}

.ga-15__fill--idle {
  background: rgba(255,255,255,.12);
  width: 0%;
}
/* Upload dropzone */

.ga-15__drop {
  width: 280px;
  height: 160px;
  border-radius: 14px;
  border: 1.5px dashed rgba(255,255,255,.1);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 8px;
  cursor: pointer;
  transition: all .25s;
  position: relative;
  overflow: hidden;
}

.ga-15__drop::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, rgba(6,182,212,.06), rgba(99,102,241,.06));
  opacity: 0;
  transition: opacity .25s;
}

.ga-15__drop:hover {
  border-color: rgba(6,182,212,.35);
}

.ga-15__drop:hover::before {
  opacity: 1;
}

.ga-15__drop-icon {
  font-size: 1.6rem;
}

.ga-15__drop-text {
  font-size: .8rem;
  font-weight: 600;
  color: rgba(255,255,255,.45);
}

.ga-15__drop-sub {
  font-size: .68rem;
  color: rgba(255,255,255,.2);
}
/* Speed control */

.ga-15__ctrl {
  position: absolute;
  bottom: 12px;
  right: 12px;
  display: flex;
  gap: 5px;
}

.ga-15 {
  position: relative;
}

.ga-15__ctrl-btn {
  padding: 4px 10px;
  font-size: .68rem;
  font-weight: 700;
  border-radius: 6px;
  border: 1px solid rgba(255,255,255,.08);
  background: rgba(255,255,255,.04);
  color: rgba(255,255,255,.3);
  cursor: pointer;
  transition: all .2s;
}

.ga-15__ctrl-btn.active,
.ga-15__ctrl-btn:hover {
  background: rgba(6,182,212,.12);
  border-color: rgba(6,182,212,.3);
  color: #67e8f9;
}

@media (prefers-reduced-motion: reduce) {
  .ga-15__card--uploading::before {
    animation: none;
  }

  .ga-15__fill--up,
    .ga-15__fill--up::after {
    animation: none;
  }
}
```

## JavaScript
```js
(function() {
  const w = document.querySelector('.ga-15');
  w.querySelectorAll('.ga-15__ctrl-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      w.querySelectorAll('.ga-15__ctrl-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      w.style.setProperty('--dur', btn.dataset.dur);
    });
  });
})();
```
