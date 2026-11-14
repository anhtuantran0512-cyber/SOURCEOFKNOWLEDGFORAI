---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-glassmorphism/frosted-modal/"
title: "Frosted Glass Modal Dialog"
section: "design-styles"
category: "css-glassmorphism"
category_name: "CSS Glassmorphism"
description: "A native <dialog open> rendered as frosted glass over a dimmed, blurred page — the pattern every product needs and most get wrong."
has_js: "false"
---

Here's a working CSS Glassmorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Frosted Glass Modal Dialog
Source: https://codefronts.com/design-styles/css-glassmorphism/frosted-modal/

A native <dialog open> rendered as frosted glass over a dimmed, blurred page — the pattern every product needs and most get wrong. Two layers of blur do the work: a heavy one on the scrim to push the page back, a lighter one on the sheet so it still reads as a surface floating in front of it.
## HTML
```html
<div class="gm-12">
  <input class="gm-12__sr" type="checkbox" id="gm-12-theme">
  <label class="gm-12__theme" for="gm-12-theme" title="Switch theme">
    <svg class="gm-12__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="gm-12__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="gm-12__vh">Switch light or dark theme</span>
  </label>

  <div class="gm-12__page" aria-hidden="true">
    <h2 class="gm-12__ph">Release 4.12 · edge rollout</h2>
    <p class="gm-12__pp">Regional traffic is being shifted to the new glass renderer in three waves. The first wave covers 12% of EU sessions and completes in about nine minutes.</p>
    <p class="gm-12__pp">Rollback stays available for 24 hours after the final wave. Metrics dashboards refresh every 30 seconds while the rollout is active.</p>
    <div class="gm-12__prow"><span></span><span></span><span></span></div>
  </div>

  <div class="gm-12__stage">
    <div class="gm-12__scrim" aria-hidden="true"></div>
    <dialog class="gm-12__sheet" open aria-labelledby="gm-12-title" aria-describedby="gm-12-desc">
      <button class="gm-12__close" type="button" aria-label="Close dialog">
        <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M7 7l10 10M17 7L7 17" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg>
      </button>
      <span class="gm-12__kicker">Confirm rollout</span>
      <h2 class="gm-12__title" id="gm-12-title">Ship the glass renderer to 100%?</h2>
      <p class="gm-12__desc" id="gm-12-desc">All three canary waves passed. Promoting to full traffic will replace the current renderer for every session in the EU and US edge regions.</p>
      <ul class="gm-12__facts">
        <li><span class="gm-12__fk">Waves passed</span><span class="gm-12__fv">3 / 3</span></li>
        <li><span class="gm-12__fk">Error budget used</span><span class="gm-12__fv">4.1%</span></li>
        <li><span class="gm-12__fk">Rollback window</span><span class="gm-12__fv">24 h</span></li>
      </ul>
      <div class="gm-12__actions">
        <button class="gm-12__btn gm-12__btn--primary" type="button">Promote to 100%</button>
        <button class="gm-12__btn" type="button">Keep at 12%</button>
      </div>
      <p class="gm-12__note">Sam Rivera approved this change 6 minutes ago.</p>
    </dialog>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap');

.gm-12 {
  --a1: rgba(99,102,241,.6);
  --a2: rgba(236,72,153,.5);
  --a3: rgba(45,212,191,.45);
  --a4: rgba(251,146,60,.4);
  --base: #05070f;
  --base2: #141033;
  --ink: #f9fafe;
  --muted: rgba(249,250,254,.72);
  --tint: #ffffff;
  --accent: #a78bfa;
  --rim: rgba(255,255,255,.5);
  --rim2: rgba(255,255,255,.15);
  --edge: rgba(255,255,255,.2);
  --scrim: rgba(6,8,20,.5);
  --mono: 'Geist Mono',ui-monospace,'SFMono-Regular',Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  overflow: hidden;
  box-sizing: border-box;
  color: var(--ink);
  isolation: isolate;
  font-family: 'Geist',ui-sans-serif,system-ui,-apple-system,'Segoe UI',sans-serif;
  background: radial-gradient(54% 46% at 16% 18%, var(--a1) 0%, transparent 62%), radial-gradient(48% 42% at 84% 14%, var(--a2) 0%, transparent 58%), radial-gradient(50% 44% at 78% 86%, var(--a3) 0%, transparent 60%), radial-gradient(42% 36% at 16% 88%, var(--a4) 0%, transparent 58%), linear-gradient(158deg, var(--base) 0%, var(--base2) 52%, var(--base) 100%);
}

.gm-12 *,
.gm-12 *::before,
.gm-12 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 300)) {
  .gm-12 {
    --a1: oklch(0.62 0.22 275 / .62);
    --a2: oklch(0.7 0.24 350 / .52);
    --a3: oklch(0.82 0.15 178 / .46);
    --a4: oklch(0.78 0.17 55 / .42);
    --base: oklch(0.13 0.025 272);
    --base2: oklch(0.23 0.1 290);
    --accent: oklch(0.72 0.17 292);
  }
}

.gm-12__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.gm-12__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.gm-12__theme {
  position: absolute;
  inset-block-start: 1.15rem;
  inset-inline-end: 1.15rem;
  z-index: 10;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  border-radius: 999px;
  color: var(--ink);
  background: rgba(255,255,255,.14);
  border: 1px solid var(--edge);
  -webkit-backdrop-filter: blur(10px) saturate(160%);
  backdrop-filter: blur(10px) saturate(160%);
  box-shadow: inset 0 1px 0 var(--rim), 0 10px 24px -14px rgba(0,0,0,.7);
  transition: scale .18s ease;
}

.gm-12__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
  border-radius: inherit;
}

.gm-12__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.gm-12__theme:hover {
  scale: 1.06;
}

.gm-12__sr:focus-visible + .gm-12__theme {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.gm-12__moon {
  display: none;
}
/* mock page content, so the scrim has something to push back */

.gm-12__page {
  position: absolute;
  inset: 0;
  z-index: 0;
  padding: clamp(1.5rem,6vw,5rem);
  max-inline-size: 52rem;
}

.gm-12__ph {
  margin: 0 0 .8rem;
  font-size: clamp(1.6rem,4vw,2.6rem);
  font-weight: 600;
  letter-spacing: -.03em;
  line-height: 1.1;
}

.gm-12__pp {
  margin: 0 0 .7rem;
  max-inline-size: 38rem;
  font-size: 1rem;
  line-height: 1.65;
  color: var(--muted);
}

.gm-12__prow {
  display: flex;
  gap: .8rem;
  margin-block-start: 1.6rem;
}

.gm-12__prow span {
  inline-size: 6.5rem;
  block-size: 4rem;
  border-radius: .9rem;
  background: rgba(255,255,255,.1);
  border: 1px solid var(--edge);
}

.gm-12__stage {
  position: relative;
  z-index: 1;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,4vw,3rem);
}

.gm-12__scrim {
  position: absolute;
  inset: 0;
  background: var(--scrim);
  -webkit-backdrop-filter: blur(8px) saturate(120%);
  backdrop-filter: blur(8px) saturate(120%);
}

.gm-12__sheet {
  position: relative;
  z-index: 1;
  inline-size: min(32rem,100%);
  max-block-size: none;
  margin: 0;
  padding: clamp(1.4rem,3vw,2rem);
  border-radius: 1.75rem;
  color: var(--ink);
  background: rgba(255,255,255,.18);
  border: 1px solid var(--edge);
  box-shadow: inset 0 1px 0 var(--rim), inset 0 -1px 0 var(--rim2), 0 40px 90px -34px rgba(0,0,0,.78);
  display: grid;
  gap: .85rem;
  animation: gm-12-in .22s cubic-bezier(.2,.8,.3,1) both;
}

@supports (background: color-mix(in oklab, white 10%, transparent)) {
  .gm-12__sheet {
    background: color-mix(in oklab, var(--tint) 18%, transparent);
  }
}

@supports ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .gm-12__sheet {
    -webkit-backdrop-filter: blur(28px) saturate(180%);
    backdrop-filter: blur(28px) saturate(180%);
  }
}

@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .gm-12__sheet {
    background: rgba(18,16,44,.94);
  }

  .gm-12__scrim {
    background: rgba(6,8,20,.75);
  }
}

@keyframes gm-12-in {
  from {
    opacity: 0;
    translate: 0 14px;
    scale: .985;
  }

  to {
    opacity: 1;
    translate: 0 0;
    scale: 1;
  }
}

.gm-12__close {
  position: absolute;
  inset-block-start: .85rem;
  inset-inline-end: .85rem;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  border-radius: 999px;
  color: var(--ink);
  background: rgba(255,255,255,.14);
  border: 1px solid var(--edge);
  box-shadow: inset 0 1px 0 var(--rim2);
  transition: background .18s ease, scale .18s ease;
}

.gm-12__close svg {
  inline-size: 1.1rem;
  block-size: 1.1rem;
}

.gm-12__close:hover {
  scale: 1.06;
  background: rgba(255,255,255,.22);
}

.gm-12__close:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.gm-12__kicker {
  font-family: var(--mono);
  font-size: .68rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
}

.gm-12__title {
  margin: 0;
  padding-inline-end: 2.5rem;
  font-size: clamp(1.3rem,2.8vw,1.75rem);
  font-weight: 600;
  letter-spacing: -.028em;
  line-height: 1.15;
  text-wrap: balance;
}

.gm-12__desc {
  margin: 0;
  font-size: .98rem;
  line-height: 1.6;
  color: var(--ink);
  opacity: .86;
  text-wrap: pretty;
}

.gm-12__facts {
  list-style: none;
  margin: .2rem 0 0;
  padding: .9rem 0 0;
  border-block-start: 1px solid var(--rim2);
  display: grid;
  gap: .5rem;
}

.gm-12__facts li {
  display: flex;
  justify-content: space-between;
  gap: 1rem;
  align-items: baseline;
}

.gm-12__fk {
  font-size: .88rem;
  color: var(--muted);
}

.gm-12__fv {
  font-family: var(--mono);
  font-size: .85rem;
  font-variant-numeric: tabular-nums;
}

.gm-12__actions {
  display: flex;
  flex-wrap: wrap;
  gap: .6rem;
  margin-block-start: .3rem;
}

.gm-12__btn {
  min-block-size: 2.75rem;
  padding: .75rem 1.15rem;
  border-radius: .9rem;
  cursor: pointer;
  flex: 1 1 auto;
  font: inherit;
  font-size: .94rem;
  font-weight: 500;
  color: var(--ink);
  background: rgba(255,255,255,.13);
  border: 1px solid var(--edge);
  -webkit-backdrop-filter: blur(12px);
  backdrop-filter: blur(12px);
  box-shadow: inset 0 1px 0 var(--rim2);
  transition: translate .18s ease, background .18s ease;
}

.gm-12__btn--primary {
  color: #150b2c;
  background: var(--accent);
  border-color: transparent;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.5), 0 14px 30px -16px rgba(0,0,0,.7);
}

.gm-12__btn:hover {
  translate: 0 -2px;
}

.gm-12__btn:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.gm-12__note {
  margin: 0;
  font-family: var(--mono);
  font-size: .66rem;
  letter-spacing: .04em;
  color: var(--muted);
}

.gm-12[data-theme="light"],
.gm-12:has(#gm-12-theme:checked) {
  --a1: rgba(165,180,252,.6);
  --a2: rgba(249,168,212,.55);
  --a3: rgba(153,246,228,.5);
  --a4: rgba(253,186,116,.45);
  --base: #f1f3fb;
  --base2: #e3e8fd;
  --ink: #0f1120;
  --muted: rgba(15,17,32,.68);
  --rim: rgba(255,255,255,.95);
  --rim2: rgba(255,255,255,.5);
  --edge: rgba(15,17,32,.12);
  --scrim: rgba(240,242,252,.55);
  --accent: #7c3aed;
}

.gm-12:has(#gm-12-theme:checked) .gm-12__sun {
  display: none;
}

.gm-12:has(#gm-12-theme:checked) .gm-12__moon {
  display: block;
}

.gm-12[data-theme="light"] .gm-12__btn--primary,
.gm-12:has(#gm-12-theme:checked) .gm-12__btn--primary {
  color: #fff;
}

@media (prefers-reduced-motion: reduce) {
  .gm-12 *,
    .gm-12 *::before,
    .gm-12 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .gm-12__sheet,
    .gm-12__btn,
    .gm-12__close,
    .gm-12__theme {
    border-color: CanvasText;
    box-shadow: none;
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
    background: Canvas;
  }

  .gm-12__scrim {
    background: Canvas;
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
  }
}
```
