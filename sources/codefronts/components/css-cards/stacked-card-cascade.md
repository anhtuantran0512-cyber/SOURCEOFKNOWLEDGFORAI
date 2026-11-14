---
source: "codefronts"
url: "https://codefronts.com/components/css-cards/stacked-card-cascade/"
title: "Stacked Card Cascade"
section: "components"
category: "css-cards"
category_name: "CSS Cards"
description: "Three overlapping project cards."
has_js: "false"
---

Here's a working CSS Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Stacked Card Cascade
Source: https://codefronts.com/components/css-cards/stacked-card-cascade/

Three overlapping project cards. On hover / focus-within the top card lifts and the two behind fan out and rotate — a Trello-style stack peek. Keyboard-accessible.
## HTML
```html
<section class="card-20">
  <div class="card-20__stage" aria-hidden="true">
    <div class="card-20__stage-mesh"></div>
    <div class="card-20__stage-grid"></div>
  </div>

  <div class="card-20__stack" tabindex="0" aria-label="Project stack">
    <header class="card-20__nav">
      <div class="card-20__crumb">
        <span class="card-20__ws" aria-hidden="true">M</span>
        <span class="card-20__crumb-txt">Meridian Labs</span>
      </div>
      <button type="button" class="card-20__search" aria-label="Command palette">
        <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4.35-4.35"/></svg>
        <kbd>⌘K</kbd>
      </button>
    </header>

    <article class="card-20__card card-20__card--back2" aria-hidden="true">
      <div class="card-20__mini-head">
        <span class="card-20__mini-chip card-20__mini-chip--planning">PLANNING</span>
        <span class="card-20__mini-due">Sep 20</span>
      </div>
      <div class="card-20__mini-title">Mobile app redesign</div>
      <div class="card-20__mini-row">
        <div class="card-20__mini-avatars"><span></span><span></span></div>
        <div class="card-20__mini-progress">
          <div class="card-20__mini-progress-bar card-20__mini-progress-bar--planning" style="width:12%"></div>
        </div>
      </div>
    </article>

    <article class="card-20__card card-20__card--back1" aria-hidden="true">
      <div class="card-20__mini-head">
        <span class="card-20__mini-chip card-20__mini-chip--review">IN REVIEW</span>
        <span class="card-20__mini-due">Aug 22</span>
      </div>
      <div class="card-20__mini-title">Payment gateway migration</div>
      <div class="card-20__mini-row">
        <div class="card-20__mini-avatars"><span></span><span></span><span></span></div>
        <div class="card-20__mini-progress">
          <div class="card-20__mini-progress-bar card-20__mini-progress-bar--review" style="width:78%"></div>
        </div>
      </div>
    </article>

    <article class="card-20__card card-20__card--top">
      <div class="card-20__glow" aria-hidden="true"></div>

      <header class="card-20__head">
        <span class="card-20__chip">
          <span class="card-20__chip-dot" aria-hidden="true"></span>
          IN PROGRESS
        </span>
        <span class="card-20__chip card-20__chip--priority">
          <svg width="9" height="9" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><polygon points="12 2 15 9 22 9 17 14 19 21 12 17 5 21 7 14 2 9 9 9"/></svg>
          P1
        </span>
        <div class="card-20__notif" aria-label="4 notifications">
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 8a6 6 0 0 0-12 0c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.73 21a2 2 0 0 1-3.46 0"/></svg>
          <span class="card-20__notif-count">4</span>
        </div>
      </header>

      <h3 class="card-20__title">Homepage redesign</h3>
      <p class="card-20__brief">Due Aug 14 · Q3 milestone · 14 of 22 tasks</p>

      <div class="card-20__progress">
        <div class="card-20__progress-track">
          <div class="card-20__progress-fill"></div>
        </div>
        <div class="card-20__progress-labels">
          <span class="card-20__progress-pct">64%</span>
          <div class="card-20__avatars" aria-hidden="true">
            <span class="card-20__av card-20__av--1">AR</span>
            <span class="card-20__av card-20__av--2">JL</span>
            <span class="card-20__av card-20__av--3">MK</span>
            <span class="card-20__av card-20__av--more">+2</span>
          </div>
        </div>
      </div>

      <footer class="card-20__foot">
        <button type="button" class="card-20__cta card-20__cta--primary">
          <span class="card-20__cta-sheen" aria-hidden="true"></span>
          Open project
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
        </button>
        <span class="card-20__hint">
          <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="9 18 15 12 9 6"/></svg>
          <span>Hover to see 3 more projects</span>
        </span>
      </footer>
    </article>
  </div>
</section>
```
## CSS
```css
.card-20 {
  position: relative;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: clamp(80px, 10vw, 140px) clamp(20px, 4vw, 40px);
  box-sizing: border-box;
  background: radial-gradient(ellipse at 20% 15%, rgba(99, 102, 241, 0.06) 0%, transparent 45%), radial-gradient(ellipse at 80% 85%, rgba(236, 72, 153, 0.05) 0%, transparent 45%), linear-gradient(180deg, #faf9f5 0%, #f0ede5 100%);
  font-family: 'Inter', system-ui, sans-serif;
  --focus: #6366f1;
  --code: 'JetBrains Mono', ui-monospace, Menlo, monospace;
  overflow: hidden;
}

.card-20 *,
.card-20 *::before,
.card-20 *::after {
  box-sizing: border-box;
}
/* ── stage ── */

.card-20__stage {
  position: absolute;
  inset: 0;
  z-index: 0;
  pointer-events: none;
  overflow: hidden;
}

.card-20__stage-mesh {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 900px;
  height: 900px;
  transform: translate(-50%, -50%);
  background: radial-gradient(circle at 30% 30%, rgba(99, 102, 241, 0.10) 0%, transparent 45%), radial-gradient(circle at 70% 70%, rgba(236, 72, 153, 0.06) 0%, transparent 45%);
  filter: blur(60px);
}

.card-20__stage-grid {
  position: absolute;
  inset: 0;
  background-image: linear-gradient(rgba(99, 102, 241, 0.04) 1px, transparent 1px), linear-gradient(90deg, rgba(99, 102, 241, 0.04) 1px, transparent 1px);
  background-size: 36px 36px;
  mask-image: radial-gradient(ellipse at center, black 30%, transparent 70%);
  -webkit-mask-image: radial-gradient(ellipse at center, black 30%, transparent 70%);
}
/* ── stack container ── */

.card-20__stack {
  position: relative;
  z-index: 1;
  width: 100%;
  max-width: 380px;
  padding-top: 48px;
}

.card-20__stack:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 12px;
  border-radius: 24px;
}
/* nav */

.card-20__nav {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
  padding: 0 4px;
}

.card-20__crumb {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 5px 12px 5px 5px;
  background: rgba(255, 255, 255, 0.85);
  border: 1px solid rgba(99, 102, 241, 0.16);
  border-radius: 999px;
  color: #1a1a1a;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: -0.005em;
  box-shadow: 0 2px 8px rgba(60, 40, 100, 0.06);
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
}

.card-20__ws {
  width: 22px;
  height: 22px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 999px;
  background: linear-gradient(135deg, #6366f1, #a855f7);
  color: #fff;
  font-size: 10px;
  font-weight: 800;
  letter-spacing: -0.02em;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.3);
}

.card-20__search {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 8px 6px 10px;
  background: rgba(255, 255, 255, 0.85);
  border: 1px solid rgba(0, 0, 0, 0.06);
  border-radius: 999px;
  color: #6b6b7c;
  font: inherit;
  cursor: pointer;
  transition: background 0.18s, color 0.18s;
  box-shadow: 0 2px 8px rgba(60, 40, 100, 0.04);
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
}

.card-20__search:hover {
  background: #fff;
  color: #4b4b57;
}

.card-20__search kbd {
  font-family: var(--code);
  font-size: 9px;
  font-weight: 700;
  color: #6b6b7c;
  padding: 2px 5px;
  background: rgba(0, 0, 0, 0.04);
  border: 1px solid rgba(0, 0, 0, 0.08);
  border-radius: 4px;
}

.card-20__search:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}
/* ── back cards (rich mini-preview, VISIBLE at rest, generously fanned) ── */

.card-20__card {
  background: #fff;
  border: 1px solid rgba(0, 0, 0, 0.06);
  border-radius: 20px;
  transition: transform 0.55s cubic-bezier(0.34, 1.15, 0.64, 1), box-shadow 0.55s;
}

.card-20__card--back1,
.card-20__card--back2 {
  position: absolute;
  padding: 14px 16px;
  width: 88%;
  box-shadow: 0 20px 40px -12px rgba(60, 40, 100, 0.20), 0 8px 20px -6px rgba(60, 40, 100, 0.12), inset 0 1px 0 rgba(255, 255, 255, 0.6);
}

.card-20__card--back2 {
  top: 68px;
  right: -6%;
  transform: rotate(-8deg);
  z-index: 0;
  background: linear-gradient(180deg, #fefefe 0%, #f9f9f8 100%);
}

.card-20__card--back1 {
  top: 76px;
  left: -6%;
  transform: rotate(7deg);
  z-index: 1;
  background: linear-gradient(180deg, #fff 0%, #fafafa 100%);
}

.card-20__mini-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 8px;
}

.card-20__mini-chip {
  font-family: var(--code);
  font-size: 8.5px;
  font-weight: 800;
  letter-spacing: 0.14em;
  padding: 3px 7px;
  border-radius: 999px;
  text-transform: uppercase;
}

.card-20__mini-chip--planning {
  color: #b45309;
  background: rgba(251, 191, 36, 0.14);
  border: 1px solid rgba(180, 83, 9, 0.24);
}

.card-20__mini-chip--review {
  color: #15803d;
  background: rgba(22, 163, 74, 0.10);
  border: 1px solid rgba(21, 128, 61, 0.24);
}

.card-20__mini-due {
  font-family: var(--code);
  font-size: 9.5px;
  font-weight: 700;
  color: #9ca3af;
  letter-spacing: -0.005em;
}

.card-20__mini-title {
  font-size: 13.5px;
  font-weight: 800;
  color: #1a1a1a;
  margin-bottom: 10px;
  letter-spacing: -0.015em;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.card-20__mini-row {
  display: flex;
  align-items: center;
  gap: 10px;
}

.card-20__mini-avatars {
  display: flex;
  flex-shrink: 0;
}

.card-20__mini-avatars span {
  width: 18px;
  height: 18px;
  border-radius: 50%;
  border: 2px solid #fff;
  margin-left: -5px;
  box-shadow: 0 0 0 1px rgba(0, 0, 0, 0.06);
}

.card-20__mini-avatars span:nth-child(1) {
  background: linear-gradient(135deg, #f472b6, #ec4899);
  margin-left: 0;
}

.card-20__mini-avatars span:nth-child(2) {
  background: linear-gradient(135deg, #60a5fa, #3b82f6);
}

.card-20__mini-avatars span:nth-child(3) {
  background: linear-gradient(135deg, #34d399, #10b981);
}

.card-20__mini-progress {
  flex: 1;
  height: 4px;
  background: rgba(0, 0, 0, 0.06);
  border-radius: 999px;
  overflow: hidden;
}

.card-20__mini-progress-bar {
  height: 100%;
  border-radius: 999px;
}

.card-20__mini-progress-bar--planning {
  background: linear-gradient(90deg, #fbbf24, #d97706);
}

.card-20__mini-progress-bar--review {
  background: linear-gradient(90deg, #22c55e, #15803d);
}
/* ── top card ── */

.card-20__card--top {
  position: relative;
  z-index: 2;
  padding: 20px 22px 18px;
  background: linear-gradient(180deg, #fff 0%, #fefdfa 100%);
  border-color: rgba(99, 102, 241, 0.24);
  box-shadow: 0 40px 70px -20px rgba(60, 40, 100, 0.30), 0 20px 40px -20px rgba(99, 102, 241, 0.22), inset 0 1px 0 rgba(255, 255, 255, 0.7);
  isolation: isolate;
}

.card-20__glow {
  position: absolute;
  top: -50px;
  left: -50px;
  width: 300px;
  height: 300px;
  background: radial-gradient(circle, rgba(99, 102, 241, 0.22) 0%, transparent 55%);
  filter: blur(24px);
  pointer-events: none;
  z-index: -1;
}
/* hover — fan the back cards wider */

.card-20__stack:hover .card-20__card--top,
.card-20__stack:focus-within .card-20__card--top {
  transform: translateY(-6px);
  box-shadow: 0 50px 80px -20px rgba(60, 40, 100, 0.36), 0 26px 46px -20px rgba(99, 102, 241, 0.28), inset 0 1px 0 rgba(255, 255, 255, 0.7);
}

.card-20__stack:hover .card-20__card--back1,
.card-20__stack:focus-within .card-20__card--back1 {
  transform: translate(-40px, 24px) rotate(11deg);
}

.card-20__stack:hover .card-20__card--back2,
.card-20__stack:focus-within .card-20__card--back2 {
  transform: translate(40px, 32px) rotate(-12deg);
}
/* ── top card head ── */

.card-20__head {
  display: flex;
  align-items: center;
  gap: 6px;
  margin-bottom: 14px;
}

.card-20__chip {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-family: var(--code);
  font-size: 9px;
  font-weight: 800;
  letter-spacing: 0.14em;
  color: #4338ca;
  padding: 3px 8px;
  background: rgba(99, 102, 241, 0.10);
  border: 1px solid rgba(99, 102, 241, 0.26);
  border-radius: 999px;
  text-transform: uppercase;
}

.card-20__chip-dot {
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: #6366f1;
  box-shadow: 0 0 6px #6366f1;
  animation: card-20-pulse 2s ease-in-out infinite;
}

.card-20__chip--priority {
  color: #be185d;
  background: rgba(236, 72, 153, 0.10);
  border-color: rgba(236, 72, 153, 0.28);
}

.card-20__chip--priority svg {
  color: #be185d;
}

.card-20__notif {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 28px;
  height: 28px;
  margin-left: auto;
  background: rgba(0, 0, 0, 0.03);
  border: 1px solid rgba(0, 0, 0, 0.06);
  border-radius: 8px;
  color: #4b4b57;
}

.card-20__notif-count {
  position: absolute;
  top: -5px;
  right: -5px;
  min-width: 16px;
  height: 16px;
  padding: 0 4px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: #ec4899;
  color: #fff;
  font-family: var(--code);
  font-size: 9px;
  font-weight: 800;
  border: 1.5px solid #fff;
  border-radius: 999px;
  box-shadow: 0 0 8px rgba(236, 72, 153, 0.5);
}
/* title + brief */

.card-20__title {
  font-size: 22px;
  font-weight: 800;
  margin: 0 0 4px;
  letter-spacing: -0.025em;
  line-height: 1.15;
  color: #1a1a1a;
  background: linear-gradient(180deg, #1a1a1a 0%, #4338ca 140%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.card-20__brief {
  font-size: 11.5px;
  color: #6b6b7c;
  margin: 0 0 16px;
  letter-spacing: -0.005em;
}
/* progress with avatars beside it */

.card-20__progress {
  margin-bottom: 14px;
}

.card-20__progress-track {
  position: relative;
  height: 6px;
  background: rgba(0, 0, 0, 0.06);
  border-radius: 999px;
  overflow: hidden;
  margin-bottom: 8px;
}

.card-20__progress-fill {
  height: 100%;
  width: 64%;
  background: linear-gradient(90deg, #22c55e 0%, #16a34a 60%, #15803d 100%);
  border-radius: 999px;
  box-shadow: 0 0 10px rgba(22, 163, 74, 0.4);
}

.card-20__progress-labels {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.card-20__progress-pct {
  font-family: var(--code);
  font-size: 15px;
  font-weight: 800;
  background: linear-gradient(90deg, #16a34a, #15803d);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  letter-spacing: -0.02em;
}

.card-20__avatars {
  display: flex;
}

.card-20__av {
  width: 24px;
  height: 24px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  color: #fff;
  font-size: 8.5px;
  font-weight: 800;
  border: 2px solid #fff;
  margin-left: -6px;
  letter-spacing: -0.02em;
  box-shadow: 0 0 0 1px rgba(0, 0, 0, 0.06);
}

.card-20__av:first-child {
  margin-left: 0;
}

.card-20__av--1 {
  background: linear-gradient(135deg, #f472b6, #ec4899);
}

.card-20__av--2 {
  background: linear-gradient(135deg, #60a5fa, #3b82f6);
}

.card-20__av--3 {
  background: linear-gradient(135deg, #34d399, #10b981);
}

.card-20__av--more {
  background: rgba(99, 102, 241, 0.12);
  color: #4338ca;
  font-family: var(--code);
  font-size: 8px;
  box-shadow: 0 0 0 1px rgba(99, 102, 241, 0.20);
}
/* foot */

.card-20__foot {
  display: flex;
  align-items: center;
  gap: 10px;
}

.card-20__cta {
  position: relative;
  flex: 1;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  min-height: 42px;
  padding: 10px 16px;
  border: 0;
  border-radius: 12px;
  font: 800 12.5px 'Inter', sans-serif;
  cursor: pointer;
  letter-spacing: -0.01em;
  transition: transform 0.2s, box-shadow 0.2s;
  overflow: hidden;
}

.card-20__cta--primary {
  background: linear-gradient(180deg, #818cf8 0%, #4338ca 100%);
  color: #fff;
  box-shadow: 0 4px 12px rgba(99, 102, 241, 0.35), 0 0 0 1px rgba(255, 255, 255, 0.14) inset;
}

.card-20__cta--primary:hover {
  transform: translateY(-1px);
  box-shadow: 0 8px 20px rgba(99, 102, 241, 0.5), 0 0 0 1px rgba(255, 255, 255, 0.24) inset;
}

.card-20__cta-sheen {
  position: absolute;
  top: 0;
  left: -100%;
  width: 60%;
  height: 100%;
  background: linear-gradient(115deg, transparent 30%, rgba(255,255,255,0.5) 50%, transparent 70%);
  transition: left 0.6s ease;
}

.card-20__cta--primary:hover .card-20__cta-sheen {
  left: 130%;
}

.card-20__cta:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}

.card-20__hint {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-size: 10px;
  font-weight: 600;
  color: #9ca3af;
  letter-spacing: -0.005em;
  max-width: 130px;
  text-align: left;
  line-height: 1.3;
}

.card-20__hint svg {
  flex-shrink: 0;
  color: #6366f1;
}

@keyframes card-20-pulse {
  0%,
    100% {
    transform: scale(1);
    opacity: 1;
  }

  50% {
    transform: scale(1.35);
    opacity: 0.6;
  }
}

@media (prefers-reduced-motion: reduce) {
  .card-20__chip-dot {
    animation: none;
  }

  .card-20__card,
    .card-20__cta,
    .card-20__cta-sheen,
    .card-20__search {
    transition: none;
  }

  .card-20__stack:hover .card-20__card--top,
    .card-20__stack:hover .card-20__card--back1,
    .card-20__stack:hover .card-20__card--back2 {
    transform: none;
  }

  .card-20__cta--primary:hover {
    transform: none;
  }

  .card-20__cta--primary:hover .card-20__cta-sheen {
    left: -100%;
  }
}
```
