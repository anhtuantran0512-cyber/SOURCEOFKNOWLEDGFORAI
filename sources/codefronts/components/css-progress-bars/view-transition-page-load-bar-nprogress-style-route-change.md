---
source: "codefronts"
url: "https://codefronts.com/components/css-progress-bars/view-transition-page-load-bar-nprogress-style-route-change/"
title: "View Transition Page Load Bar (NProgress Style Route Change)"
section: "components"
category: "css-progress-bars"
category_name: "CSS Progress Bars"
description: "The 3px bar at the top of the window that every SPA needs: it rushes to 80% in 200ms, holds while the route resolves, then completes and fades."
has_js: "true"
---

Here's a working CSS Progress Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: View Transition Page Load Bar (NProgress Style Route Change)
Source: https://codefronts.com/components/css-progress-bars/view-transition-page-load-bar-nprogress-style-route-change/

The 3px bar at the top of the window that every SPA needs: it rushes to 80% in 200ms, holds while the route resolves, then completes and fades. Wired to document.startViewTransition() so the bar and the page swap belong to the same navigation.
## HTML
```html
<div class="pb-05">
  <span class="pb-05__bar" id="pb-05-bar" aria-hidden="true" data-done="true" style="--value:0"></span>

  <button class="pb-05__theme" type="button" aria-pressed="false" aria-label="Toggle dark or light theme">
    <svg class="pb-05__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="pb-05__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
  </button>

  <div class="pb-05__stage">
    <div class="pb-05__browser">
      <div class="pb-05__chrome">
        <span class="pb-05__lights" aria-hidden="true"><i></i><i></i><i></i></span>
        <p class="pb-05__url pb-05__mono" id="pb-05-url">codefronts.com<span>/guides</span></p>
        <span class="pb-05__badge pb-05__mono" id="pb-05-phase">idle</span>
      </div>

      <div class="pb-05__view" id="pb-05-view" aria-busy="false">
        <p class="pb-05__crumb pb-05__mono" id="pb-05-crumb">/ guides</p>
        <h2 class="pb-05__h" id="pb-05-h">Ship a router that feels instant</h2>
        <p class="pb-05__p" id="pb-05-p">The navigation bar at the top of this frame is doing the work: a 200ms rush to 80%, a hold while the route resolves, then a snap to 100% and a fade. Press the button and watch the timing, not the colour.</p>
        <ul class="pb-05__list" id="pb-05-list">
          <li><span class="pb-05__mono">01</span>Rush to 80% immediately</li>
          <li><span class="pb-05__mono">02</span>Hold — the server owns this part</li>
          <li><span class="pb-05__mono">03</span>Complete, then fade out</li>
        </ul>
      </div>

      <div class="pb-05__dock">
        <button class="pb-05__btn pb-05__btn--primary" type="button" id="pb-05-go">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6.6l5.4 5.4L13 17.4" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg>
          Navigate to /docs
        </button>
        <span class="pb-05__note pb-05__mono">startViewTransition() + scaleX bar</span>
      </div>
    </div>
    <p class="pb-05__live" id="pb-05-live" role="status" aria-live="polite"></p>
  </div>
</div>
```
## CSS
```css
.pb-05 {
  --bg: #08070e;
  --card: #0e0d18;
  --card2: #141324;
  --ink: #f1eeff;
  --muted: rgba(241,238,255,.6);
  --line: rgba(241,238,255,.12);
  --accent: #a78bfa;
  --accent-2: #818cf8;
  --sans: system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: ui-monospace,"JetBrains Mono","Geist Mono",SFMono-Regular,Menlo,monospace;
  inline-size: 100%;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(76% .16 295)) {
  .pb-05 {
    --accent: oklch(76% .16 295);
    --accent-2: oklch(70% .16 277);
  }
}

.pb-05 *,
.pb-05 *::before,
.pb-05 *::after {
  box-sizing: border-box;
}

.pb-05__bar {
  position: fixed;
  inset-block-start: 0;
  inset-inline: 0;
  z-index: 20;
  block-size: 3px;
  display: block;
  transform: scaleX(calc(var(--value,0) / 100));
  transform-origin: left center;
  background: linear-gradient(90deg,var(--accent-2),var(--accent));
  box-shadow: 0 0 12px color-mix(in srgb,var(--accent) 70%,transparent);
  transition: transform .2s cubic-bezier(.4,0,.2,1),opacity .25s linear;
  will-change: transform,opacity;
}

.pb-05__bar[data-done="true"] {
  opacity: 0;
}

.pb-05__stage {
  display: grid;
  place-items: center;
  gap: 1rem;
  min-block-size: 100vh;
  padding: clamp(1.1rem,4vw,3.5rem);
  background: radial-gradient(100% 60% at 50% 0%,color-mix(in srgb,var(--accent) 16%,transparent),transparent 60%);
}

.pb-05__theme {
  position: absolute;
  inset-block-start: clamp(1.1rem,2.6vw,1.8rem);
  inset-inline-end: clamp(.9rem,2.4vw,1.6rem);
  z-index: 25;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  border-radius: 99px;
  border: 1px solid var(--line);
  color: var(--ink);
  background: rgba(255,255,255,.06);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  transition: background .2s,transform .2s;
}

.pb-05__theme:hover {
  transform: translateY(-1px);
  background: rgba(255,255,255,.11);
}

.pb-05__theme:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.pb-05__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.pb-05__sun {
  display: none;
}

.pb-05__moon {
  display: block;
}

.pb-05[data-theme="light"] .pb-05__sun {
  display: block;
}

.pb-05[data-theme="light"] .pb-05__moon {
  display: none;
}

.pb-05__browser {
  inline-size: min(46rem,100%);
  border-radius: 1.3rem;
  overflow: hidden;
  border: 1px solid var(--line);
  background: color-mix(in srgb,var(--card) 94%,transparent);
  box-shadow: 0 1px 0 rgba(255,255,255,.05) inset,0 34px 80px -44px rgba(0,0,0,.95);
}

.pb-05__chrome {
  display: grid;
  grid-template-columns: auto 1fr auto;
  gap: .8rem;
  align-items: center;
  padding: .7rem .9rem;
  border-block-end: 1px solid var(--line);
  background: color-mix(in srgb,var(--ink) 5%,transparent);
}

.pb-05__lights {
  display: flex;
  gap: .35rem;
}

.pb-05__lights i {
  inline-size: .6rem;
  block-size: .6rem;
  border-radius: 99px;
  background: color-mix(in srgb,var(--ink) 22%,transparent);
}

.pb-05__url {
  margin: 0;
  padding: .35rem .7rem;
  border-radius: .55rem;
  background: color-mix(in srgb,var(--ink) 6%,transparent);
  border: 1px solid var(--line);
  color: var(--muted);
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.pb-05__url span {
  color: var(--ink);
}

.pb-05__mono {
  font-family: var(--mono);
  font-size: .74rem;
  font-variant-numeric: tabular-nums;
}

.pb-05__badge {
  padding: .28rem .5rem;
  border-radius: .45rem;
  color: var(--accent);
  background: color-mix(in srgb,var(--accent) 15%,transparent);
  border: 1px solid color-mix(in srgb,var(--accent) 32%,transparent);
}

.pb-05__view {
  display: grid;
  gap: .7rem;
  padding: clamp(1.3rem,3.4vw,2.2rem);
  min-block-size: 15rem;
  align-content: start;
}

.pb-05__view[aria-busy="true"] {
  opacity: .55;
  transition: opacity .2s linear;
}

.pb-05__crumb {
  margin: 0;
  color: var(--accent);
  letter-spacing: .06em;
  text-transform: uppercase;
  font-size: .68rem;
}

.pb-05__h {
  margin: 0;
  font-size: clamp(1.4rem,3.4vw,2.05rem);
  line-height: 1.12;
  letter-spacing: -.022em;
  font-weight: 650;
  text-wrap: balance;
}

.pb-05__p {
  margin: 0;
  max-inline-size: 52ch;
  font-size: clamp(.9rem,1.5vw,1rem);
  line-height: 1.65;
  color: var(--muted);
  text-wrap: pretty;
}

.pb-05__list {
  list-style: none;
  margin: .3rem 0 0;
  padding: 0;
  display: grid;
  gap: 0;
}

.pb-05__list li {
  display: flex;
  gap: .7rem;
  align-items: baseline;
  padding-block: .55rem;
  border-block-start: 1px solid var(--line);
  font-size: .88rem;
  color: var(--ink);
}

.pb-05__list span {
  color: var(--accent);
}

.pb-05__dock {
  display: flex;
  flex-wrap: wrap;
  gap: .8rem;
  align-items: center;
  padding: .9rem clamp(1.1rem,3vw,2.2rem) 1.1rem;
  border-block-start: 1px solid var(--line);
  background: color-mix(in srgb,var(--ink) 4%,transparent);
}

.pb-05__btn {
  display: inline-flex;
  align-items: center;
  gap: .45rem;
  min-block-size: 2.75rem;
  padding: .65rem 1.1rem;
  border-radius: .85rem;
  border: 1px solid var(--line);
  background: color-mix(in srgb,var(--ink) 6%,transparent);
  color: var(--ink);
  font: inherit;
  font-size: .88rem;
  font-weight: 550;
  cursor: pointer;
  transition: transform .18s,background .18s;
}

.pb-05__btn svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
}

.pb-05__btn:hover {
  transform: translateY(-1px);
}

.pb-05__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.pb-05__btn--primary {
  background: var(--accent);
  border-color: transparent;
  color: #170c2b;
  box-shadow: 0 12px 26px -16px var(--accent);
}

.pb-05__btn--primary:hover {
  background: color-mix(in srgb,var(--accent) 88%,white);
}

.pb-05__note {
  color: var(--muted);
}

.pb-05__live {
  margin: 0;
  min-block-size: 1.1rem;
  font-size: .78rem;
  color: var(--muted);
}

.pb-05[data-theme="light"] {
  --bg: #f7f6fd;
  --card: #ffffff;
  --card2: #faf9ff;
  --ink: #150c28;
  --muted: rgba(21,12,40,.62);
  --line: rgba(21,12,40,.1);
  --accent: #7c3aed;
  --accent-2: #4f46e5;
}

.pb-05[data-theme="light"] .pb-05__theme {
  background: rgba(21,12,40,.05);
}

.pb-05[data-theme="light"] .pb-05__btn--primary {
  color: #fff;
}

@media (prefers-color-scheme: light) {
  .pb-05:not([data-theme="dark"]) {
    --bg: #f7f6fd;
    --card: #ffffff;
    --card2: #faf9ff;
    --ink: #150c28;
    --muted: rgba(21,12,40,.62);
    --line: rgba(21,12,40,.1);
    --accent: #7c3aed;
    --accent-2: #4f46e5;
  }

  .pb-05:not([data-theme="dark"]) .pb-05__theme {
    background: rgba(21,12,40,.05);
  }

  .pb-05:not([data-theme="dark"]) .pb-05__btn--primary {
    color: #fff;
  }

  .pb-05:not([data-theme="dark"]) .pb-05__sun {
    display: block;
  }

  .pb-05:not([data-theme="dark"]) .pb-05__moon {
    display: none;
  }

  .pb-05[data-theme="dark"] .pb-05__sun {
    display: none;
  }

  .pb-05[data-theme="dark"] .pb-05__moon {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .pb-05 *,
    .pb-05 *::before,
    .pb-05 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .pb-05__browser,
    .pb-05__btn,
    .pb-05__theme,
    .pb-05__url {
    border-color: CanvasText;
    box-shadow: none;
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
  }

  .pb-05__bar {
    background: Highlight;
    box-shadow: none;
  }
}
```

## JavaScript
```js
const pb05 = document.querySelector('.pb-05');
if (pb05) {
  const q = (s) => pb05.querySelector(s);
  const [bar, view, phase, url, live] = ['#pb-05-bar','#pb-05-view','#pb-05-phase','#pb-05-url','#pb-05-live'].map(q);
  const ROUTES = [
    { path: '/docs', crumb: '/ docs', h: 'Install in one command', p: 'Route swapped through startViewTransition(), so the bar and the content change belong to the same frame budget. Nothing here waited on a spinner.', items: ['Rush, hold, complete', 'No layout during the swap', 'Fallback when the API is missing'] },
    { path: '/guides', crumb: '/ guides', h: 'Ship a router that feels instant', p: 'The navigation bar at the top of this frame is doing the work: a 200ms rush to 80%, a hold while the route resolves, then a snap to 100% and a fade.', items: ['Rush to 80% immediately', 'Hold — the server owns this part', 'Complete, then fade out'] },
  ];
  const set = (v) => bar.style.setProperty('--value', v);
  let i = 0;
  const paint = (r) => {
    q('#pb-05-crumb').textContent = r.crumb; q('#pb-05-h').textContent = r.h; q('#pb-05-p').textContent = r.p;
    q('#pb-05-list').innerHTML = r.items.map((t, n) => '<li><span class="pb-05__mono">0' + (n + 1) + '</span>' + t + '</li>').join('');
    url.innerHTML = 'codefronts.com<span>' + r.path + '</span>';
    q('#pb-05-go').lastChild.textContent = ' Navigate to ' + ROUTES[(i + 1) % 2].path;
  };
  const navigate = async () => {
    const soft = matchMedia('(prefers-reduced-motion: reduce)').matches;
    i = (i + 1) % ROUTES.length; const next = ROUTES[i];
    bar.dataset.done = 'false'; set(0); phase.textContent = 'rush'; view.setAttribute('aria-busy', 'true');
    requestAnimationFrame(() => set(80));
    await new Promise((r) => setTimeout(r, soft ? 0 : 520)); phase.textContent = 'hold';
    const swap = () => paint(next);
    if (!soft && document.startViewTransition) await document.startViewTransition(swap).updateCallbackDone; else swap();
    set(100); phase.textContent = 'done'; view.setAttribute('aria-busy', 'false');
    live.textContent = 'Navigated to ' + next.path + '. ' + next.h + '.';
    setTimeout(() => { bar.dataset.done = 'true'; setTimeout(() => set(0), 260); }, 220);
  };
  q('#pb-05-go').addEventListener('click', navigate);
  q('.pb-05__theme').addEventListener('click', (e) => {
    const light = pb05.dataset.theme !== 'light';
    pb05.dataset.theme = light ? 'light' : 'dark';
    e.currentTarget.setAttribute('aria-pressed', String(!light));
  });
}
```
