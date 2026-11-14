---
source: "codefronts"
url: "https://codefronts.com/components/css-animated-cards/starting-style-css-mount-in-animation/"
title: "@starting-style CSS Mount-In Animation"
section: "components"
category: "css-animated-cards"
category_name: "CSS Animated Cards"
description: "Cards that animate in the moment they are inserted into the DOM and animate out before they are removed — the behaviour that used to require Framer Motion or…"
has_js: "true"
---

Here's a working CSS Animated Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: @starting-style CSS Mount-In Animation
Source: https://codefronts.com/components/css-animated-cards/starting-style-css-mount-in-animation/

Cards that animate in the moment they are inserted into the DOM and animate out before they are removed — the behaviour that used to require Framer Motion or a double requestAnimationFrame hack. @starting-style defines the pre-mount state, transition-behavior: allow-discrete lets display and overlay participate in the transition, and the JS is reduced to appendChild and remove.
## HTML
```html
<section class="ac-02" aria-label="starting-style mount-in animation demo">
  <div class="ac-02__stage">
    <header class="ac-02__head">
      <p class="ac-02__eyebrow">Native enter &amp; exit</p>
      <h2 class="ac-02__title">Cards that animate the instant they mount</h2>
      <p class="ac-02__sub">Every card below is inserted with a plain <code>prepend()</code>. The entrance is CSS.</p>
      <div class="ac-02__ctl">
        <button class="ac-02__btn ac-02__btn--go" type="button" data-add>
          <svg viewBox="0 0 24 24" width="17" height="17" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M12 5v14M5 12h14"/></svg>
          Mount a card
        </button>
        <button class="ac-02__btn" type="button" data-clear>Clear all</button>
      </div>
    </header>
    <ul class="ac-02__grid" role="list" data-list>
      <li class="ac-02__card" data-mounted>
        <span class="ac-02__dot" aria-hidden="true"></span>
        <div class="ac-02__body"><h3 class="ac-02__name">Deploy finished</h3><p class="ac-02__meta">web-app · 42 s · main@9f2c1a</p></div>
        <button class="ac-02__x" type="button" data-remove aria-label="Dismiss Deploy finished card">
          <svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>
        </button>
      </li>
      <li class="ac-02__card" data-mounted>
        <span class="ac-02__dot" aria-hidden="true"></span>
        <div class="ac-02__body"><h3 class="ac-02__name">Design review requested</h3><p class="ac-02__meta">Ana K. · checkout flow v4</p></div>
        <button class="ac-02__x" type="button" data-remove aria-label="Dismiss Design review requested card">
          <svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>
        </button>
      </li>
    </ul>
    <p class="ac-02__empty" data-empty hidden>Nothing mounted. Press <b>Mount a card</b>.</p>
    <p class="ac-02__sr" role="status" aria-live="polite" data-status></p>
    <p class="ac-02__chip" aria-hidden="true">@starting-style · transition-behavior:allow-discrete · display transition · zero animation library</p>
  </div>
</section>
```
## CSS
```css
.ac-02,
.ac-02 *,
.ac-02 *::before,
.ac-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ac-02 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --ac-02-bg: oklch(0.98 0.006 255);
  --ac-02-card: oklch(1 0 0);
  --ac-02-ink: oklch(0.24 0.02 265);
  --ac-02-mut: oklch(0.56 0.02 265);
  --ac-02-acc: oklch(0.58 0.20 275);
  --ac-02-line: oklch(0.24 0.02 265/.11);
  background: var(--ac-02-bg);
  color: var(--ac-02-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.ac-02__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(16px,2.4vw,26px);
  padding: clamp(22px,5vw,60px);
  background: radial-gradient(90% 60% at 50% 0%,color-mix(in oklch,var(--ac-02-acc) 11%,transparent),transparent 65%);
}

.ac-02__head {
  display: grid;
  justify-items: center;
  gap: 10px;
  text-align: center;
  max-width: 58ch;
}

.ac-02__eyebrow {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--ac-02-acc);
}

.ac-02__title {
  font-size: clamp(23px,3.4vw,38px);
  font-weight: 650;
  line-height: 1.12;
  letter-spacing: -.03em;
  text-wrap: balance;
}

.ac-02__sub {
  font-size: 14.5px;
  color: var(--ac-02-mut);
  text-wrap: pretty;
}

.ac-02__sub code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 13px;
  background: oklch(0.24 0.02 265/.07);
  padding: 2px 6px;
  border-radius: 6px;
}

.ac-02__ctl {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  justify-content: center;
  margin-top: 6px;
}

.ac-02__btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  min-height: 44px;
  padding: 0 20px;
  border: 1px solid var(--ac-02-line);
  border-radius: 99px;
  background: var(--ac-02-card);
  color: var(--ac-02-ink);
  font-size: 14px;
  font-weight: 600;
  font-family: inherit;
  cursor: pointer;
  transition: transform .2s,box-shadow .2s,background .2s;
}

.ac-02__btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 8px 22px oklch(0.24 0.02 265/.12);
}

.ac-02__btn:active {
  transform: translateY(0) scale(.98);
}

.ac-02__btn:focus-visible {
  outline: 2px solid var(--ac-02-acc);
  outline-offset: 3px;
}

.ac-02__btn--go {
  background: var(--ac-02-acc);
  border-color: transparent;
  color: oklch(0.99 0 0);
}

.ac-02__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(268px,1fr));
  gap: 12px;
  width: min(100%,880px);
  list-style: none;
}

.ac-02__card {
  display: flex;
  align-items: center;
  gap: 13px;
  padding: 15px 14px 15px 16px;
  border: 1px solid var(--ac-02-line);
  border-radius: 16px;
  background: var(--ac-02-card);
  box-shadow: 0 1px 2px oklch(0.24 0.02 265/.05),0 12px 28px -18px oklch(0.24 0.02 265/.5);
  opacity: 1;
  scale: 1;
  translate: 0 0;
  transition: opacity .45s cubic-bezier(.16,1,.3,1),scale .45s cubic-bezier(.16,1,.3,1),translate .45s cubic-bezier(.16,1,.3,1),display .45s allow-discrete;
}

@starting-style {
  .ac-02__card {
    opacity: 0;
    scale: .88;
    translate: 0 -14px;
  }
}

.ac-02__card[data-leaving] {
  opacity: 0;
  scale: .9;
  translate: 0 -8px;
  display: none;
  transition-timing-function: cubic-bezier(.55,0,.85,.35);
  transition-duration: .3s;
}

.ac-02__dot {
  flex: none;
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: var(--ac-02-acc);
  box-shadow: 0 0 0 4px color-mix(in oklch,var(--ac-02-acc) 18%,transparent);
}

.ac-02__body {
  flex: 1;
  min-width: 0;
  display: grid;
  gap: 3px;
}

.ac-02__name {
  font-size: 15px;
  font-weight: 640;
  letter-spacing: -.015em;
  line-height: 1.25;
}

.ac-02__meta {
  font-size: 12.5px;
  color: var(--ac-02-mut);
  font-variant-numeric: tabular-nums;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.ac-02__x {
  flex: none;
  display: grid;
  place-items: center;
  width: 44px;
  height: 44px;
  border: 0;
  border-radius: 12px;
  background: transparent;
  color: var(--ac-02-mut);
  cursor: pointer;
  transition: background .18s,color .18s;
}

.ac-02__x:hover {
  background: oklch(0.24 0.02 265/.07);
  color: var(--ac-02-ink);
}

.ac-02__x:focus-visible {
  outline: 2px solid var(--ac-02-acc);
  outline-offset: 2px;
}

.ac-02__empty {
  font-size: 14px;
  color: var(--ac-02-mut);
}

.ac-02__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.ac-02__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  line-height: 1.6;
  color: var(--ac-02-mut);
  padding: 8px 15px;
  border: 1px dashed var(--ac-02-line);
  border-radius: 99px;
  text-align: center;
  max-width: min(100%,640px);
}

@media (prefers-reduced-motion: reduce) {
  .ac-02__card {
    transition-duration: .01ms;
  }

  .ac-02__btn {
    transition: none;
  }
}
```

## JavaScript
```js
(() => {
  const SEED = [
    ['Build passed', 'api-gateway · 1 m 04 s · #4821'],
    ['New signup', 'northwind.co · Pro trial · Sydney'],
    ['Comment on PR #218', 'Marcus L. · "ship it"'],
    ['Invoice paid', 'INV-2026-0431 · $4,800.00'],
    ['Alert resolved', 'p95 latency back under 200 ms'],
  ];
  document.querySelectorAll('.ac-02').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    const list = root.querySelector('[data-list]');
    const empty = root.querySelector('[data-empty]');
    const status = root.querySelector('[data-status]');
    let i = 0;

    const sync = () => {
      const n = list.querySelectorAll('.ac-02__card:not([data-leaving])').length;
      empty.hidden = n > 0;
      status.textContent = n === 0 ? 'All cards dismissed.' : n + ' card' + (n === 1 ? '' : 's') + ' mounted.';
    };

    root.querySelector('[data-add]').addEventListener('click', () => {
      const [name, meta] = SEED[i++ % SEED.length];
      const li = document.createElement('li');
      li.className = 'ac-02__card';
      li.innerHTML = '<span class="ac-02__dot" aria-hidden="true"></span>' +
        '<div class="ac-02__body"><h3 class="ac-02__name"></h3><p class="ac-02__meta"></p></div>' +
        '<button class="ac-02__x" type="button" data-remove><svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg></button>';
      li.querySelector('.ac-02__name').textContent = name;
      li.querySelector('.ac-02__meta').textContent = meta;
      li.querySelector('[data-remove]').setAttribute('aria-label', 'Dismiss ' + name + ' card');
      list.prepend(li);          // @starting-style does the entrance — no rAF hack, no class toggle
      sync();
    });

    const dismiss = (card) => {
      if (card.dataset.leaving) return;
      card.dataset.leaving = '1';                       // exit transition runs, display flips last
      card.addEventListener('transitionend', (e) => { if (e.propertyName === 'display' || e.propertyName === 'opacity') card.remove(); }, { once: true });
      setTimeout(() => card.remove(), 400);             // safety net if transitions are disabled
      sync();
    };

    list.addEventListener('click', (e) => {
      const btn = e.target.closest('[data-remove]');
      if (btn) dismiss(btn.closest('.ac-02__card'));
    });
    root.querySelector('[data-clear]').addEventListener('click', () => {
      list.querySelectorAll('.ac-02__card').forEach((c, n) => setTimeout(() => dismiss(c), n * 55));
    });
    sync();
  });
})();
```
