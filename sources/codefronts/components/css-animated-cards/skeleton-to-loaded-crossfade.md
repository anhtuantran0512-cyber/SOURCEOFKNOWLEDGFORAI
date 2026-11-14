---
source: "codefronts"
url: "https://codefronts.com/components/css-animated-cards/skeleton-to-loaded-crossfade/"
title: "Skeleton-to-Loaded Crossfade"
section: "components"
category: "css-animated-cards"
category_name: "CSS Animated Cards"
description: "A skeleton that actually helps: same geometry as the real card, a shimmer that sweeps at reading speed, and a crossfade so content arrives instead of snapping."
has_js: "true"
---

Here's a working CSS Animated Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Skeleton-to-Loaded Crossfade
Source: https://codefronts.com/components/css-animated-cards/skeleton-to-loaded-crossfade/

A skeleton that actually helps: same geometry as the real card, a shimmer that sweeps at reading speed, and a crossfade so content arrives instead of snapping. The shimmer is one animated background-position — no pseudo-element pyramid — and the whole card is marked aria-busy so assistive tech waits quietly instead of reading placeholder rectangles.
## HTML
```html
<section class="ac-11" aria-label="Skeleton to loaded crossfade demo">
  <div class="ac-11__stage">
    <header class="ac-11__head">
      <p class="ac-11__eyebrow">Loading states</p>
      <h2 class="ac-11__title">Skeletons that match the shape of the answer</h2>
      <button class="ac-11__btn" type="button" data-reload>
        <svg viewBox="0 0 24 24" width="17" height="17" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M3 12a9 9 0 1 0 3-6.7"/><path d="M3 4v5h5"/></svg>
        Fetch again
      </button>
    </header>
    <ul class="ac-11__grid" role="list" data-grid aria-busy="true">
      <li class="ac-11__card">
        <div class="ac-11__sk" aria-hidden="true">
          <span class="ac-11__b ac-11__b--img"></span>
          <span class="ac-11__srow"><span class="ac-11__b ac-11__b--av"></span><span class="ac-11__scol"><span class="ac-11__b ac-11__b--l1"></span><span class="ac-11__b ac-11__b--l2"></span></span></span>
          <span class="ac-11__b ac-11__b--t1"></span>
          <span class="ac-11__b ac-11__b--t2"></span>
          <span class="ac-11__b ac-11__b--t3"></span>
        </div>
        <div class="ac-11__real">
          <img class="ac-11__img" src="https://images.unsplash.com/photo-1524758631624-e2822e304c36?q=80&w=700&auto=format&fit=crop" alt="Warm modern interior with a low sofa" loading="lazy" decoding="async" width="700" height="400">
          <div class="ac-11__by"><img class="ac-11__av" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?q=80&w=100&h=100&fit=crop&auto=format" alt="" width="36" height="36"><span><b>Elin Marsh</b><i>Interiors · 6 min read</i></span></div>
          <h3 class="ac-11__name">The quiet return of the conversation pit</h3>
          <p class="ac-11__copy">Sunken seating went out with shag carpet. Now it is back — and this time it is engineered for acoustics rather than nostalgia.</p>
        </div>
      </li>
      <li class="ac-11__card">
        <div class="ac-11__sk" aria-hidden="true">
          <span class="ac-11__b ac-11__b--img"></span>
          <span class="ac-11__srow"><span class="ac-11__b ac-11__b--av"></span><span class="ac-11__scol"><span class="ac-11__b ac-11__b--l1"></span><span class="ac-11__b ac-11__b--l2"></span></span></span>
          <span class="ac-11__b ac-11__b--t1"></span>
          <span class="ac-11__b ac-11__b--t2"></span>
          <span class="ac-11__b ac-11__b--t3"></span>
        </div>
        <div class="ac-11__real">
          <img class="ac-11__img" src="https://images.unsplash.com/photo-1483058712412-4245e9b90334?q=80&w=700&auto=format&fit=crop" alt="Desk with notebook, laptop and coffee" loading="lazy" decoding="async" width="700" height="400">
          <div class="ac-11__by"><img class="ac-11__av" src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=100&h=100&fit=crop&auto=format" alt="" width="36" height="36"><span><b>Dan Osei</b><i>Workflow · 4 min read</i></span></div>
          <h3 class="ac-11__name">Everything I stopped measuring in 2026</h3>
          <p class="ac-11__copy">Half of a productivity system is deciding which numbers you are allowed to ignore. Here is the list that survived the cut.</p>
        </div>
      </li>
      <li class="ac-11__card">
        <div class="ac-11__sk" aria-hidden="true">
          <span class="ac-11__b ac-11__b--img"></span>
          <span class="ac-11__srow"><span class="ac-11__b ac-11__b--av"></span><span class="ac-11__scol"><span class="ac-11__b ac-11__b--l1"></span><span class="ac-11__b ac-11__b--l2"></span></span></span>
          <span class="ac-11__b ac-11__b--t1"></span>
          <span class="ac-11__b ac-11__b--t2"></span>
          <span class="ac-11__b ac-11__b--t3"></span>
        </div>
        <div class="ac-11__real">
          <img class="ac-11__img" src="https://images.unsplash.com/photo-1441974231531-c6227db76b6e?q=80&w=700&auto=format&fit=crop" alt="Sunlight through a forest of tall trees" loading="lazy" decoding="async" width="700" height="400">
          <div class="ac-11__by"><img class="ac-11__av" src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?q=80&w=100&h=100&fit=crop&auto=format" alt="" width="36" height="36"><span><b>Ruth Nakamura</b><i>Field notes · 9 min read</i></span></div>
          <h3 class="ac-11__name">Mapping a watershed with a phone and a kayak</h3>
          <p class="ac-11__copy">Consumer GPS is now accurate enough for real hydrology. What it still cannot do is tell you where the water goes underground.</p>
        </div>
      </li>
    </ul>
    <p class="ac-11__status" role="status" aria-live="polite" data-status></p>
    <p class="ac-11__chip" aria-hidden="true">one animated background-position · stacked grid crossfade · geometry-matched blocks · aria-busy handoff</p>
  </div>
</section>
```
## CSS
```css
.ac-11,
.ac-11 *,
.ac-11 *::before,
.ac-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ac-11 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --ac-11-bg: oklch(0.16 0.012 250);
  --ac-11-card: oklch(0.21 0.015 250);
  --ac-11-ink: oklch(0.97 0.004 260);
  --ac-11-mut: oklch(0.69 0.02 255);
  --ac-11-acc: oklch(0.80 0.14 168);
  --ac-11-line: oklch(1 0 0/.10);
  --ac-11-base: oklch(0.27 0.016 250);
  --ac-11-hi: oklch(0.36 0.02 250);
  background: var(--ac-11-bg);
  color: var(--ac-11-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.ac-11__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(16px,2.4vw,26px);
  padding: clamp(20px,5vw,56px);
}

.ac-11__head {
  display: grid;
  justify-items: center;
  gap: 11px;
  text-align: center;
}

.ac-11__eyebrow {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--ac-11-acc);
}

.ac-11__title {
  font-size: clamp(23px,3.4vw,38px);
  font-weight: 650;
  line-height: 1.12;
  letter-spacing: -.03em;
  text-wrap: balance;
}

.ac-11__btn {
  display: inline-flex;
  align-items: center;
  gap: 9px;
  min-height: 44px;
  padding: 0 20px;
  border: 1px solid var(--ac-11-line);
  border-radius: 99px;
  background: oklch(1 0 0/.05);
  color: var(--ac-11-ink);
  font-size: 14px;
  font-weight: 600;
  font-family: inherit;
  cursor: pointer;
  transition: background .2s,transform .2s;
}

.ac-11__btn:hover {
  background: oklch(1 0 0/.1);
  transform: translateY(-1px);
}

.ac-11__btn:focus-visible {
  outline: 2px solid var(--ac-11-acc);
  outline-offset: 3px;
}

.ac-11__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(250px,1fr));
  gap: 14px;
  width: min(100%,960px);
  list-style: none;
}

.ac-11__card {
  display: grid;
  border: 1px solid var(--ac-11-line);
  border-radius: 20px;
  overflow: hidden;
  background: var(--ac-11-card);
}

.ac-11__card>* {
  grid-area: 1/1;
}

.ac-11__sk {
  display: grid;
  gap: 11px;
  padding: 12px 14px 20px;
  opacity: 1;
  visibility: visible;
  transition: opacity .38s ease,visibility 0s .38s;
}

.ac-11__b {
  display: block;
  border-radius: 8px;
  background: linear-gradient(100deg,var(--ac-11-base) 38%,var(--ac-11-hi) 50%,var(--ac-11-base) 62%);
  background-size: 220% 100%;
  animation: ac-11-shimmer 1.4s linear infinite;
}

.ac-11__b--img {
  aspect-ratio: 7/4;
  border-radius: 12px;
}

.ac-11__srow {
  display: flex;
  align-items: center;
  gap: 10px;
}

.ac-11__b--av {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  flex: none;
}

.ac-11__scol {
  display: grid;
  gap: 6px;
  flex: 1;
}

.ac-11__b--l1 {
  height: 10px;
  width: 44%;
}

.ac-11__b--l2 {
  height: 9px;
  width: 64%;
}

.ac-11__b--t1 {
  height: 15px;
  width: 92%;
}

.ac-11__b--t2 {
  height: 15px;
  width: 78%;
}

.ac-11__b--t3 {
  height: 11px;
  width: 58%;
  margin-top: 3px;
}

@keyframes ac-11-shimmer {
  from {
    background-position: 120% 0;
  }

  to {
    background-position: -120% 0;
  }
}

.ac-11__real {
  display: grid;
  gap: 9px;
  padding: 12px 14px 20px;
  align-content: start;
  opacity: 0;
  translate: 0 10px;
  transition: opacity .45s ease .05s,translate .5s cubic-bezier(.16,1,.3,1) .05s;
}

.ac-11__img {
  width: 100%;
  aspect-ratio: 7/4;
  object-fit: cover;
  border-radius: 12px;
  display: block;
  background: linear-gradient(135deg,oklch(0.34 0.05 210),oklch(0.26 0.04 265));
}

.ac-11__by {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-top: 2px;
}

.ac-11__av {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  object-fit: cover;
  flex: none;
  background: var(--ac-11-base);
}

.ac-11__by span {
  display: grid;
  gap: 1px;
  min-width: 0;
}

.ac-11__by b {
  font-size: 13px;
  font-weight: 640;
  letter-spacing: -.01em;
}

.ac-11__by i {
  font-style: normal;
  font-size: 11.5px;
  color: var(--ac-11-mut);
}

.ac-11__name {
  font-size: 16px;
  font-weight: 650;
  line-height: 1.28;
  letter-spacing: -.022em;
  text-wrap: pretty;
}

.ac-11__copy {
  font-size: 13px;
  line-height: 1.55;
  color: var(--ac-11-mut);
  text-wrap: pretty;
}

.ac-11__card[data-ready] .ac-11__sk {
  opacity: 0;
  visibility: hidden;
  transition: opacity .3s ease,visibility 0s .3s;
}

.ac-11__card[data-ready] .ac-11__real {
  opacity: 1;
  translate: 0 0;
}

.ac-11__status {
  font-size: 12.5px;
  color: var(--ac-11-mut);
}

.ac-11__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  line-height: 1.6;
  color: var(--ac-11-mut);
  padding: 8px 15px;
  border: 1px solid var(--ac-11-line);
  border-radius: 99px;
  text-align: center;
  max-width: min(100%,700px);
}

@media (prefers-reduced-motion: reduce) {
  .ac-11__b {
    animation: none;
    background: var(--ac-11-base);
  }

  .ac-11__real,
    .ac-11__sk {
    transition-duration: .01ms;
  }
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('.ac-11').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    const grid = root.querySelector('[data-grid]');
    const cards = [...grid.querySelectorAll('.ac-11__card')];
    const status = root.querySelector('[data-status]');
    let timers = [];

    const run = () => {
      timers.forEach(clearTimeout); timers = [];
      cards.forEach((c) => c.removeAttribute('data-ready'));
      grid.setAttribute('aria-busy', 'true');
      status.textContent = 'Loading 3 articles…';
      // staggered so the list resolves as a wave — simultaneous reveal reads as a flash
      cards.forEach((c, i) => timers.push(setTimeout(() => {
        c.dataset.ready = '';
        if (i === cards.length - 1) {
          grid.setAttribute('aria-busy', 'false');
          status.textContent = '3 articles loaded.';
        }
      }, 900 + i * 260)));
    };

    root.querySelector('[data-reload]').addEventListener('click', run);
    run();
  });
})();
```
