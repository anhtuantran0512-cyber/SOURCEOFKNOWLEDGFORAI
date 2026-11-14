---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-glassmorphism/contain-paint-glass-optimization/"
title: "Contain Paint Glass Optimization"
section: "design-styles"
category: "css-glassmorphism"
category_name: "CSS Glassmorphism"
description: "The demo nobody else ships: when not to use backdrop-filter."
has_js: "true"
---

Here's a working CSS Glassmorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Contain Paint Glass Optimization
Source: https://codefronts.com/design-styles/css-glassmorphism/contain-paint-glass-optimization/

The demo nobody else ships: when not to use backdrop-filter. Six glass cards in a scrolling column, with a toggle that adds or removes contain: paint and a will-change opt-in. Scroll with it off, then on — the FPS read-out and the feel of the scroll tell the same story about compositor cost.
## HTML
```html
<div class="gm-10">
  <input class="gm-10__sr" type="checkbox" id="gm-10-theme">
  <label class="gm-10__theme" for="gm-10-theme" title="Switch theme">
    <svg class="gm-10__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="gm-10__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="gm-10__vh">Switch light or dark theme</span>
  </label>

  <div class="gm-10__stage">
    <section class="gm-10__wrap" aria-labelledby="gm-10-h">
      <header class="gm-10__head">
        <p class="gm-10__eyebrow">contain · will-change · content-visibility</p>
        <h2 class="gm-10__h" id="gm-10-h">When not to use backdrop-filter</h2>
        <p class="gm-10__sub">Six blurred cards in a scroller means six blur passes per frame. Scroll the list, flip containment, scroll again.</p>
        <div class="gm-10__controls">
          <button class="gm-10__toggle" type="button" aria-pressed="false">
            <span class="gm-10__dot" aria-hidden="true"></span>
            <span class="gm-10__tlabel">Containment off</span>
          </button>
          <p class="gm-10__fps"><span class="gm-10__fpsnum">—</span><span class="gm-10__fpsunit">fps</span></p>
        </div>
        <p class="gm-10__live" role="status" aria-live="polite"></p>
      </header>

      <div class="gm-10__scroller">
        <div class="gm-10__bar">
          <span class="gm-10__barlabel">Deploy activity</span>
          <span class="gm-10__barmeta">sticky glass · 20px blur</span>
        </div>
        <ul class="gm-10__list">
          <li class="gm-10__card"><div class="gm-10__ctop"><h3 class="gm-10__ctitle">atlas-web · build 4128</h3><span class="gm-10__tag gm-10__tag--ok">passed</span></div><p class="gm-10__ccopy">Edge bundle 168 kB · 42 s · Sam Rivera</p></li>
          <li class="gm-10__card"><div class="gm-10__ctop"><h3 class="gm-10__ctitle">atlas-api · build 4127</h3><span class="gm-10__tag gm-10__tag--ok">passed</span></div><p class="gm-10__ccopy">214 tests · 1 m 08 s · Priya Sharma</p></li>
          <li class="gm-10__card"><div class="gm-10__ctop"><h3 class="gm-10__ctitle">design-tokens · build 4126</h3><span class="gm-10__tag gm-10__tag--warn">slow</span></div><p class="gm-10__ccopy">Snapshot diff 3 files · 4 m 51 s · Alex Chen</p></li>
          <li class="gm-10__card"><div class="gm-10__ctop"><h3 class="gm-10__ctitle">atlas-web · build 4125</h3><span class="gm-10__tag gm-10__tag--fail">failed</span></div><p class="gm-10__ccopy">Type error in glass-panel.tsx · Jordan Lee</p></li>
          <li class="gm-10__card"><div class="gm-10__ctop"><h3 class="gm-10__ctitle">docs-site · build 4124</h3><span class="gm-10__tag gm-10__tag--ok">passed</span></div><p class="gm-10__ccopy">Static export 1 204 pages · 2 m 12 s</p></li>
          <li class="gm-10__card"><div class="gm-10__ctop"><h3 class="gm-10__ctitle">atlas-api · build 4123</h3><span class="gm-10__tag gm-10__tag--ok">passed</span></div><p class="gm-10__ccopy">Migration 0142 applied · 58 s · Sam Rivera</p></li>
        </ul>
      </div>

      <aside class="gm-10__note">
        <p class="gm-10__nhead">The compositor cost</p>
        <p class="gm-10__ncopy">Each blurred surface snapshots its backdrop, blurs it and re-composites — every frame it moves. Containment keeps invalidation local; the real fix for long lists is to blur the sticky chrome and leave the rows opaque.</p>
      </aside>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap');

.gm-10 {
  --a1: rgba(125,211,252,.5);
  --a2: rgba(196,181,253,.55);
  --a3: rgba(110,231,183,.5);
  --a4: rgba(253,164,175,.45);
  --base: #eff3fa;
  --base2: #e1e7fb;
  --ink: #0e1220;
  --muted: rgba(14,18,32,.68);
  --tint: #ffffff;
  --rim: rgba(255,255,255,.95);
  --rim2: rgba(255,255,255,.5);
  --edge: rgba(14,18,32,.12);
  --ok: #047857;
  --warn: #a16207;
  --fail: #be123c;
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
  background: radial-gradient(50% 44% at 12% 16%, var(--a1) 0%, transparent 60%), radial-gradient(52% 46% at 88% 18%, var(--a2) 0%, transparent 62%), radial-gradient(46% 40% at 78% 88%, var(--a3) 0%, transparent 58%), radial-gradient(44% 38% at 16% 90%, var(--a4) 0%, transparent 58%), linear-gradient(162deg, var(--base) 0%, var(--base2) 52%, var(--base) 100%);
}

.gm-10 *,
.gm-10 *::before,
.gm-10 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 300)) {
  .gm-10 {
    --a1: oklch(0.78 0.16 220 / .52);
    --a2: oklch(0.7 0.19 292 / .56);
    --a3: oklch(0.8 0.15 165 / .46);
    --a4: oklch(0.72 0.19 15 / .42);
    --base: oklch(0.97 0.008 275);
    --base2: oklch(0.93 0.015 285);
  }
}

.gm-10__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.gm-10__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.gm-10__theme {
  position: absolute;
  inset-block-start: 1.15rem;
  inset-inline-end: 1.15rem;
  z-index: 8;
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

.gm-10__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
  border-radius: inherit;
}

.gm-10__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.gm-10__theme:hover {
  scale: 1.06;
}

.gm-10__sr:focus-visible + .gm-10__theme {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.gm-10__moon {
  display: none;
}

.gm-10__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,4vw,3.5rem);
}

.gm-10__wrap {
  inline-size: min(56rem,100%);
  display: grid;
  gap: clamp(1.1rem,2.4vw,1.75rem);
}

.gm-10__head {
  display: grid;
  gap: .7rem;
}

.gm-10__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
}

.gm-10__h {
  margin: 0;
  font-size: clamp(1.85rem,4.4vw,2.9rem);
  font-weight: 600;
  letter-spacing: -.03em;
  line-height: 1.05;
  text-wrap: balance;
}

.gm-10__sub {
  margin: 0;
  max-inline-size: 42rem;
  font-size: clamp(.95rem,1.4vw,1.05rem);
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.gm-10__controls {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: .7rem;
  margin-block-start: .3rem;
}

.gm-10__toggle {
  display: inline-flex;
  align-items: center;
  gap: .6rem;
  min-block-size: 2.75rem;
  padding: .65rem 1rem;
  border-radius: 999px;
  cursor: pointer;
  font: inherit;
  font-size: .92rem;
  font-weight: 500;
  color: var(--ink);
  background: rgba(255,255,255,.14);
  border: 1px solid var(--edge);
  -webkit-backdrop-filter: blur(14px) saturate(160%);
  backdrop-filter: blur(14px) saturate(160%);
  box-shadow: inset 0 1px 0 var(--rim);
  transition: translate .18s ease, background .18s ease;
}

.gm-10__toggle:hover {
  translate: 0 -2px;
}

.gm-10__toggle:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.gm-10__dot {
  inline-size: .65rem;
  block-size: .65rem;
  border-radius: 999px;
  background: var(--fail);
  box-shadow: 0 0 0 3px rgba(253,164,175,.2);
  transition: background .2s ease, box-shadow .2s ease;
}

.gm-10__toggle[aria-pressed="true"] .gm-10__dot {
  background: var(--ok);
  box-shadow: 0 0 0 3px rgba(94,234,212,.22);
}

.gm-10__fps {
  margin: 0;
  display: inline-flex;
  align-items: baseline;
  gap: .25rem;
  padding: .55rem .8rem;
  border-radius: .7rem;
  font-family: var(--mono);
  background: rgba(0,0,0,.3);
  border: 1px solid var(--edge);
}

.gm-10__fpsnum {
  font-size: 1rem;
  font-variant-numeric: tabular-nums;
}

.gm-10__fpsunit {
  font-size: .68rem;
  opacity: .65;
}

.gm-10__live {
  margin: 0;
  min-block-size: 1.1rem;
  font-size: .8rem;
  color: var(--muted);
}

.gm-10__scroller {
  position: relative;
  max-block-size: min(24rem,52vh);
  overflow-y: auto;
  overscroll-behavior: contain;
  border-radius: 1.4rem;
  border: 1px solid var(--edge);
  background: rgba(255,255,255,.05);
  box-shadow: inset 0 1px 0 var(--rim2), 0 26px 60px -30px rgba(0,0,0,.65);
  scrollbar-width: thin;
}

.gm-10__bar {
  position: sticky;
  inset-block-start: 0;
  z-index: 2;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1rem;
  padding: .85rem 1.1rem;
  border-block-end: 1px solid var(--rim2);
  background: rgba(255,255,255,.12);
  -webkit-backdrop-filter: blur(20px) saturate(165%);
  backdrop-filter: blur(20px) saturate(165%);
}

.gm-10__barlabel {
  font-size: .95rem;
  font-weight: 600;
  letter-spacing: -.01em;
}

.gm-10__barmeta {
  font-family: var(--mono);
  font-size: .66rem;
  letter-spacing: .06em;
  color: var(--muted);
}

.gm-10__list {
  list-style: none;
  margin: 0;
  padding: .9rem;
  display: grid;
  gap: .8rem;
}

.gm-10__card {
  display: grid;
  gap: .4rem;
  padding: 1rem 1.1rem;
  border-radius: 1.1rem;
  border: 1px solid var(--edge);
  background: rgba(255,255,255,.11);
  -webkit-backdrop-filter: blur(24px) saturate(160%);
  backdrop-filter: blur(24px) saturate(160%);
  box-shadow: inset 0 1px 0 var(--rim), inset 0 -1px 0 var(--rim2);
}

@supports (background: color-mix(in oklab, white 10%, transparent)) {
  .gm-10__card {
    background: color-mix(in oklab, var(--tint) 13%, transparent);
  }
}

@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .gm-10__card,
    .gm-10__bar {
    background: rgba(18,16,44,.9);
  }
}

.gm-10__list.is-contained .gm-10__card {
  contain: paint;
  will-change: transform;
  content-visibility: auto;
  contain-intrinsic-size: auto 5.5rem;
}

.gm-10__ctop {
  display: flex;
  align-items: center;
  gap: .6rem;
  flex-wrap: wrap;
}

.gm-10__ctitle {
  margin: 0;
  font-size: .98rem;
  font-weight: 600;
  letter-spacing: -.01em;
}

.gm-10__tag {
  margin-inline-start: auto;
  padding: .25rem .5rem;
  border-radius: .45rem;
  font-family: var(--mono);
  font-size: .64rem;
  letter-spacing: .08em;
  text-transform: uppercase;
  border: 1px solid var(--edge);
  background: rgba(255,255,255,.1);
}

.gm-10__tag--ok {
  color: var(--ok);
}

.gm-10__tag--warn {
  color: var(--warn);
}

.gm-10__tag--fail {
  color: var(--fail);
}

.gm-10__ccopy {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .02em;
  color: var(--muted);
}

.gm-10__note {
  padding: clamp(1rem,1.8vw,1.3rem);
  border-radius: 1.1rem;
  border: 1px solid var(--edge);
  background: rgba(255,255,255,.08);
  -webkit-backdrop-filter: blur(18px) saturate(150%);
  backdrop-filter: blur(18px) saturate(150%);
  box-shadow: inset 0 1px 0 var(--rim2);
  display: grid;
  gap: .35rem;
}

.gm-10__nhead {
  margin: 0;
  font-family: var(--mono);
  font-size: .7rem;
  letter-spacing: .14em;
  text-transform: uppercase;
}

.gm-10__ncopy {
  margin: 0;
  font-size: .9rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.gm-10[data-theme="light"],
.gm-10:has(#gm-10-theme:checked) {
  --a1: rgba(56,189,248,.5);
  --a2: rgba(167,139,250,.55);
  --a3: rgba(52,211,153,.45);
  --a4: rgba(251,113,133,.4);
  --base: #05070f;
  --base2: #111633;
  --ink: #f8fafe;
  --muted: rgba(248,250,254,.7);
  --rim: rgba(255,255,255,.5);
  --rim2: rgba(255,255,255,.14);
  --edge: rgba(255,255,255,.18);
  --ok: #5eead4;
  --warn: #fcd34d;
  --fail: #fda4af;
}

.gm-10:has(#gm-10-theme:checked) .gm-10__sun {
  display: none;
}

.gm-10:has(#gm-10-theme:checked) .gm-10__moon {
  display: block;
}

.gm-10[data-theme="light"] .gm-10__fps,
.gm-10:has(#gm-10-theme:checked) .gm-10__fps {
  background: rgba(255,255,255,.7);
}

@media (prefers-reduced-motion: reduce) {
  .gm-10 *,
    .gm-10 *::before,
    .gm-10 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .gm-10__card,
    .gm-10__bar,
    .gm-10__scroller,
    .gm-10__theme,
    .gm-10__toggle,
    .gm-10__note {
    border-color: CanvasText;
    box-shadow: none;
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
    background: Canvas;
  }
}
```

## JavaScript
```js
const gm10 = document.querySelector('.gm-10');
if (gm10) {
  const btn = gm10.querySelector('.gm-10__toggle');
  const list = gm10.querySelector('.gm-10__list');
  const label = gm10.querySelector('.gm-10__tlabel');
  const live = gm10.querySelector('.gm-10__live');
  const num = gm10.querySelector('.gm-10__fpsnum');
  btn.addEventListener('click', () => {
    const on = btn.getAttribute('aria-pressed') !== 'true';
    btn.setAttribute('aria-pressed', String(on));
    list.classList.toggle('is-contained', on);
    label.textContent = on ? 'Containment on' : 'Containment off';
    live.textContent = on ? 'contain: paint and will-change applied to all six cards.' : 'Containment removed — every card invalidates the whole list.';
  });
  let frames = 0, last = performance.now();
  const tick = (now) => {
    frames++;
    if (now - last >= 500) { num.textContent = Math.round((frames * 1000) / (now - last)); frames = 0; last = now; }
    requestAnimationFrame(tick);
  };
  requestAnimationFrame(tick);
}
```
