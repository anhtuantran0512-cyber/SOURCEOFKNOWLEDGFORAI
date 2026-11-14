---
source: "codefronts"
url: "https://codefronts.com/snippets/css-banners-alerts/material-design-floating-alert-card/"
title: "Browser Upgrade Notice Bar"
section: "snippets"
category: "css-banners-alerts"
category_name: "CSS Banners & Alerts"
description: "Material 3's floating alert, rebuilt from first principles: elevation as tokens, a state layer instead of hover colours, a ripple driven by a registered…"
has_js: "true"
---

Here's a working CSS Banners & Alert from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Browser Upgrade Notice Bar
Source: https://codefronts.com/snippets/css-banners-alerts/material-design-floating-alert-card/

Material 3's floating alert, rebuilt from first principles: elevation as tokens, a state layer instead of hover colours, a ripple driven by a registered length, and the M3 shape scale as custom properties. It carries a real job — telling someone their browser is two years out of date and what breaks because of it — with an update flow that reports progress instead of spinning forever.
## HTML
```html
<div class="ba-10">
  <div class="ba-10__app" aria-hidden="true">
    <div class="ba-10__appBar"><span class="ba-10__appTitle">Ledger</span><span class="ba-10__avatar"></span></div>
    <div class="ba-10__tiles"><span></span><span></span><span></span><span></span><span></span><span></span></div>
  </div>

  <section class="ba-10__card" data-card role="region" aria-labelledby="ba-10-h">
    <span class="ba-10__leading" aria-hidden="true">
      <svg viewBox="0 0 24 24" fill="none" focusable="false"><circle cx="12" cy="12" r="8.6" stroke="currentColor" stroke-width="1.8"/><path d="M12 7.6v5.2M12 15.8h.01" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
    </span>

    <div class="ba-10__body">
      <h2 class="ba-10__h" id="ba-10-h">Your browser is missing 3 features this app needs</h2>
      <p class="ba-10__supporting">
        Card payments and the export dialog will fail on this version. Updating takes about a minute and keeps your session.
      </p>
      <ul class="ba-10__missing" data-missing></ul>

      <div class="ba-10__progress" data-progress hidden>
        <div class="ba-10__ptrack" role="progressbar" aria-label="Update progress" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0" data-ptrack><span data-pfill></span></div>
        <p class="ba-10__pText" data-ptext>Preparing update…</p>
      </div>
    </div>

    <div class="ba-10__actions">
      <button class="ba-10__btn ba-10__btn--filled" type="button" data-update>
        <span class="ba-10__ripple" aria-hidden="true"></span>
        <svg class="ba-10__check" viewBox="0 0 20 20" fill="none" aria-hidden="true" focusable="false"><path d="m4.8 10.4 3.3 3.3 7.1-7.4" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>
        <span data-updatelabel>Update now</span>
      </button>
      <button class="ba-10__btn ba-10__btn--text" type="button" data-learn>
        <span class="ba-10__ripple" aria-hidden="true"></span>
        What breaks?
      </button>
      <button class="ba-10__btn ba-10__btn--text" type="button" data-dismiss>
        <span class="ba-10__ripple" aria-hidden="true"></span>
        Later
      </button>
    </div>
  </section>

  <div class="ba-10__snack" data-snack hidden>
    <p data-snacktext></p>
    <button type="button" data-snackx>Undo</button>
  </div>
  <p class="ba-10__live" role="status" aria-live="polite"></p>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap');

@property --ba-10-r {
  syntax: '<length>';
  inherits: false;
  initial-value: 0px;
}

.ba-10 {
  --r-xs: .5rem;
  --r-sm: .75rem;
  --r-md: 1rem;
  --r-lg: 1.5rem;
  --r-xl: 1.75rem;
  --e1: 0 1px 2px rgb(0 0 0 / .3), 0 1px 3px 1px rgb(0 0 0 / .15);
  --e3: 0 4px 8px 3px rgb(0 0 0 / .15), 0 1px 3px rgb(0 0 0 / .3);
  --bg: #101418;
  --surface: #181d22;
  --surface-container: #1e242b;
  --on-surface: #e3e7ec;
  --on-surface-variant: #a5adb8;
  --outline: #3a424c;
  --primary: #a8c8ff;
  --on-primary: #00305e;
  --error: #ffb4a8;
  --tertiary: #7fd6b0;
  --sans: "Manrope",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  container-type: inline-size;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  box-sizing: border-box;
  overflow: clip;
  background: var(--bg);
  color: var(--on-surface);
  font-family: var(--sans);
}

.ba-10 *,
.ba-10 *::before,
.ba-10 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(50% 0 0)) {
  .ba-10 {
    --bg: oklch(19% .012 250);
    --surface: oklch(23% .014 250);
    --surface-container: oklch(26% .016 250);
    --on-surface: oklch(92% .008 250);
    --on-surface-variant: oklch(75% .014 250);
    --outline: oklch(45% .018 250);
    --primary: oklch(83% .09 255);
    --on-primary: oklch(30% .1 255);
    --error: oklch(80% .11 25);
    --tertiary: oklch(83% .11 165);
  }
}

@media (prefers-color-scheme: light) {
  .ba-10:not([data-theme="dark"]) {
    --bg: #eef1f6;
    --surface: #ffffff;
    --surface-container: #f3f5f9;
    --on-surface: #191c20;
    --on-surface-variant: #5a616b;
    --outline: #d5dae1;
    --primary: #1a5fbe;
    --on-primary: #ffffff;
    --error: #b3261e;
    --tertiary: #0e7a55;
    --e1: 0 1px 2px rgb(0 0 0 / .12), 0 1px 3px 1px rgb(0 0 0 / .06);
    --e3: 0 4px 8px 3px rgb(0 0 0 / .1), 0 1px 3px rgb(0 0 0 / .14);
  }
}

.ba-10__app {
  padding: clamp(1rem,4vw,2rem) clamp(1rem,4vw,2rem) clamp(18rem,38vh,24rem);
  display: grid;
  gap: 1.25rem;
  max-width: 64rem;
  margin-inline: auto;
}

.ba-10__appBar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: .85rem 1.1rem;
  border-radius: var(--r-xl);
  background: var(--surface-container);
}

.ba-10__appTitle {
  font-size: 1.0625rem;
  font-weight: 800;
  letter-spacing: -.03em;
}

.ba-10__avatar {
  width: 2rem;
  height: 2rem;
  border-radius: 999px;
  background: var(--primary);
}

.ba-10__tiles {
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(auto-fit,minmax(min(100%,12rem),1fr));
}

.ba-10__tiles span {
  display: block;
  height: clamp(5rem,13vh,8rem);
  border-radius: var(--r-lg);
  background: var(--surface);
}

.ba-10__card {
  position: fixed;
  z-index: 6;
  inset: auto clamp(1rem,4vw,2rem) clamp(1rem,4vw,2rem);
  max-width: 38rem;
  margin-inline: auto;
  display: grid;
  grid-template-columns: auto 1fr;
  gap: .85rem 1rem;
  padding: 1.25rem;
  border-radius: var(--r-lg);
  background: var(--surface-container);
  color: var(--on-surface);
  box-shadow: var(--e3);
  transition: opacity .35s cubic-bezier(.2,0,0,1), translate .45s cubic-bezier(.2,0,0,1), display .45s allow-discrete;
}

@starting-style {
  .ba-10__card {
    opacity: 0;
    translate: 0 1.5rem;
  }
}

.ba-10__card[hidden] {
  display: none;
  opacity: 0;
  translate: 0 1rem;
}

.ba-10__leading {
  display: grid;
  place-items: center;
  width: 2.5rem;
  height: 2.5rem;
  border-radius: 999px;
  color: var(--error);
  background: color-mix(in oklab,var(--error) 18%,transparent);
}

.ba-10__leading svg {
  width: 1.5rem;
  height: 1.5rem;
}

.ba-10__body {
  min-width: 0;
  display: grid;
  gap: .5rem;
}

.ba-10__h {
  margin: 0;
  font-size: 1.0625rem;
  font-weight: 700;
  line-height: 1.3;
  letter-spacing: -.02em;
  text-wrap: balance;
}

.ba-10__supporting {
  margin: 0;
  font-size: .875rem;
  line-height: 1.5;
  color: var(--on-surface-variant);
  max-width: 56ch;
  text-wrap: pretty;
}

.ba-10__missing {
  margin: .15rem 0 0;
  padding: 0;
  list-style: none;
  display: flex;
  flex-wrap: wrap;
  gap: .35rem;
}

.ba-10__missing li {
  display: inline-flex;
  align-items: center;
  gap: .35rem;
  padding: .28rem .55rem;
  border-radius: var(--r-xs);
  font-size: .6875rem;
  font-weight: 600;
  letter-spacing: .01em;
  color: var(--on-surface-variant);
  border: 1px solid var(--outline);
}

.ba-10__missing li[data-ok] {
  color: var(--tertiary);
  border-color: color-mix(in oklab,var(--tertiary) 40%,transparent);
}

.ba-10__missing li[data-ok]::before {
  content: "✓";
}

.ba-10__missing li:not([data-ok])::before {
  content: "✕";
  color: var(--error);
}

.ba-10__progress {
  display: grid;
  gap: .4rem;
}

.ba-10__progress[hidden] {
  display: none;
}

.ba-10__ptrack {
  height: .25rem;
  border-radius: 999px;
  background: color-mix(in oklab,var(--primary) 24%,transparent);
  overflow: hidden;
}

.ba-10__ptrack span {
  display: block;
  height: 100%;
  width: 0%;
  border-radius: 999px;
  background: var(--primary);
  transition: width .4s cubic-bezier(.2,0,0,1);
}

.ba-10__pText {
  margin: 0;
  font-size: .75rem;
  color: var(--on-surface-variant);
  font-variant-numeric: tabular-nums;
}

.ba-10__actions {
  grid-column: 2;
  display: flex;
  flex-wrap: wrap;
  gap: .4rem;
  justify-content: flex-end;
}

.ba-10__btn {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  min-height: 2.5rem;
  padding: .6rem 1.1rem;
  border: 0;
  border-radius: 999px;
  cursor: pointer;
  font: inherit;
  font-size: .875rem;
  font-weight: 700;
  letter-spacing: .01em;
  background: transparent;
  color: var(--primary);
}

.ba-10__btn::before {
  content: "";
  position: absolute;
  inset: 0;
  background: currentColor;
  opacity: 0;
  transition: opacity .15s linear;
}

.ba-10__btn:hover::before {
  opacity: .08;
}

.ba-10__btn:active::before {
  opacity: .12;
}

.ba-10__btn--filled {
  background: var(--primary);
  color: var(--on-primary);
  box-shadow: var(--e1);
}

.ba-10__btn--filled:hover {
  box-shadow: var(--e3);
}

.ba-10__btn[aria-disabled="true"] {
  opacity: .55;
  cursor: progress;
}

.ba-10__ripple {
  position: absolute;
  inset-block-start: var(--y,50%);
  inset-inline-start: var(--x,50%);
  width: var(--ba-10-r);
  height: var(--ba-10-r);
  translate: -50% -50%;
  border-radius: 999px;
  background: currentColor;
  opacity: .16;
  pointer-events: none;
}

.ba-10__btn[data-ripple] .ba-10__ripple {
  animation: ba-10-ripple .55s cubic-bezier(.2,0,0,1);
}

@keyframes ba-10-ripple {
  from {
    --ba-10-r: 0px;
    opacity: .22;
  }

  to {
    --ba-10-r: 22rem;
    opacity: 0;
  }
}

.ba-10__check {
  display: none;
  width: 1.1rem;
  height: 1.1rem;
}

.ba-10__check path {
  stroke-dasharray: 22;
  stroke-dashoffset: 22;
}

.ba-10__btn[data-done] .ba-10__check {
  display: block;
}

.ba-10__btn[data-done] .ba-10__check path {
  animation: ba-10-draw .45s cubic-bezier(.2,0,0,1) forwards;
}

@keyframes ba-10-draw {
  to {
    stroke-dashoffset: 0;
  }
}

.ba-10__snack {
  position: fixed;
  z-index: 7;
  inset: auto 50% 1.25rem auto;
  translate: 50% 0;
  display: flex;
  align-items: center;
  gap: 1rem;
  width: min(28rem,calc(100% - 2rem));
  padding: .85rem 1rem .85rem 1.1rem;
  border-radius: var(--r-xs);
  background: var(--on-surface);
  color: var(--surface);
  box-shadow: var(--e3);
  transition: opacity .3s ease, translate .35s cubic-bezier(.2,0,0,1), display .35s allow-discrete;
}

@starting-style {
  .ba-10__snack {
    opacity: 0;
    translate: 50% 1rem;
  }
}

.ba-10__snack[hidden] {
  display: none;
}

.ba-10__snack p {
  margin: 0;
  font-size: .875rem;
  line-height: 1.4;
}

.ba-10__snack button {
  flex: none;
  min-height: 2.25rem;
  padding: .5rem .75rem;
  border: 0;
  border-radius: var(--r-xs);
  cursor: pointer;
  background: transparent;
  color: var(--primary);
  font: inherit;
  font-size: .8125rem;
  font-weight: 700;
}

.ba-10__snack button:hover {
  background: color-mix(in oklab,var(--primary) 14%,transparent);
}

.ba-10 :focus-visible {
  outline: 3px solid var(--primary);
  outline-offset: 2px;
}

.ba-10__live {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

@container (max-width: 34rem) {
  .ba-10__card {
    grid-template-columns: 1fr;
  }

  .ba-10__leading {
    display: none;
  }

  .ba-10__actions {
    grid-column: 1;
    justify-content: stretch;
  }

  .ba-10__btn--filled {
    flex: 1;
    justify-content: center;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ba-10 * {
    animation: none !important;
    transition: none !important;
  }

  .ba-10__check path {
    stroke-dashoffset: 0;
  }
}

@media (forced-colors: active) {
  .ba-10__card,
    .ba-10__snack {
    border: 1px solid CanvasText;
  }

  .ba-10__btn--filled {
    background: Highlight;
    color: HighlightText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.ba-10');
  if (!root) return;
  const card = root.querySelector('[data-card]');
  const live = root.querySelector('.ba-10__live');
  const snack = root.querySelector('[data-snack]');

  // capability detection, never user-agent sniffing
  const FEATURES = [
    ['Anchor positioning', () => CSS.supports('anchor-name: --a')],
    ['Scroll-driven animation', () => CSS.supports('animation-timeline: scroll()')],
    ['View transitions', () => 'startViewTransition' in document],
    ['Container queries', () => CSS.supports('container-type: inline-size')],
    ['@starting-style', () => CSS.supports('transition-behavior: allow-discrete')],
  ];
  const list = root.querySelector('[data-missing]');
  let missing = 0;
  FEATURES.forEach(([label, test]) => {
    let ok = false; try { ok = !!test(); } catch (_) {}
    if (!ok) missing += 1;
    const li = document.createElement('li');
    li.textContent = label;
    if (ok) li.dataset.ok = '1';
    list.append(li);
  });
  root.querySelector('#ba-10-h').textContent = missing
    ? 'Your browser is missing ' + missing + ' feature' + (missing > 1 ? 's' : '') + ' this app needs'
    : 'Your browser supports everything this app needs';

  root.addEventListener('pointerdown', (e) => {
    const btn = e.target.closest('.ba-10__btn');
    if (!btn) return;
    const r = btn.getBoundingClientRect();
    btn.style.setProperty('--x', e.clientX - r.left + 'px');
    btn.style.setProperty('--y', e.clientY - r.top + 'px');
    btn.dataset.ripple = '1';
    setTimeout(() => delete btn.dataset.ripple, 560);
  });

  const update = root.querySelector('[data-update]');
  update.addEventListener('click', () => {
    if (update.dataset.done || update.getAttribute('aria-disabled') === 'true') return;
    const box = root.querySelector('[data-progress]');
    const fill = root.querySelector('[data-pfill]');
    const track = root.querySelector('[data-ptrack]');
    const text = root.querySelector('[data-ptext]');
    box.hidden = false;
    update.setAttribute('aria-disabled', 'true');
    root.querySelector('[data-updatelabel]').textContent = 'Updating';
    let p = 0;
    const id = setInterval(() => {
      p = Math.min(100, p + 9 + Math.random() * 13);
      fill.style.width = p + '%';
      track.setAttribute('aria-valuenow', Math.round(p));
      text.textContent = p < 100 ? 'Downloading update — ' + Math.round(p) + '%' : 'Update ready. Reload to finish.';
      if (p < 100) return;
      clearInterval(id);
      update.dataset.done = '1';
      update.removeAttribute('aria-disabled');
      root.querySelector('[data-updatelabel]').textContent = 'Reload';
      live.textContent = 'Update downloaded. Choose Reload to finish.';
    }, 420);
  });

  root.querySelector('[data-learn]').addEventListener('click', () => {
    const p = root.querySelector('.ba-10__supporting');
    p.textContent = 'Card payments use the Payment Request API, and export uses File System Access. On this version both fall back to a slower flow that can time out on large ledgers.';
    live.textContent = 'Details expanded.';
  });

  root.querySelector('[data-dismiss]').addEventListener('click', () => {
    card.hidden = true;
    snack.hidden = false;
    root.querySelector('[data-snacktext]').textContent = 'Reminder snoozed for 7 days.';
    live.textContent = 'Upgrade notice dismissed for 7 days.';
  });
  root.querySelector('[data-snackx]').addEventListener('click', () => {
    snack.hidden = true; card.hidden = false; update.focus();
  });
})();
```
