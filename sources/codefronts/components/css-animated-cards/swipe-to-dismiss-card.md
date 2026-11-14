---
source: "codefronts"
url: "https://codefronts.com/components/css-animated-cards/swipe-to-dismiss-card/"
title: "Swipe-to-Dismiss Card"
section: "components"
category: "css-animated-cards"
category_name: "CSS Animated Cards"
description: "Notification cards you can throw off screen — with a rubber-band resist before the threshold, colour-coded action reveals behind the card, and momentum-aware…"
has_js: "true"
---

Here's a working CSS Animated Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Swipe-to-Dismiss Card
Source: https://codefronts.com/components/css-animated-cards/swipe-to-dismiss-card/

Notification cards you can throw off screen — with a rubber-band resist before the threshold, colour-coded action reveals behind the card, and momentum-aware release. Built on Pointer Events (one code path for mouse, touch and pen), with touch-action keeping vertical scroll native. Every gesture has a keyboard equivalent, because a swipe-only affordance is an accessibility failure.
## HTML
```html
<section class="ac-10" aria-label="Swipe to dismiss card demo">
  <div class="ac-10__stage">
    <div class="ac-10__phone">
      <header class="ac-10__top">
        <div><p class="ac-10__eyebrow">Inbox</p><h2 class="ac-10__title">Swipe a card away</h2></div>
        <button class="ac-10__reset" type="button" data-reset>Restore</button>
      </header>
      <p class="ac-10__hint">Drag left or right — or focus a card and press <kbd>Delete</kbd>.</p>
      <ul class="ac-10__list" role="list" data-list>
        <li class="ac-10__row">
          <span class="ac-10__under ac-10__under--l" aria-hidden="true">Snooze</span>
          <span class="ac-10__under ac-10__under--r" aria-hidden="true">Archive</span>
          <article class="ac-10__card" data-card tabindex="0" role="button" aria-roledescription="Swipeable card" aria-label="Deployment succeeded. Press Delete to archive.">
            <span class="ac-10__grip" aria-hidden="true"></span>
            <div class="ac-10__body"><h3 class="ac-10__name">Deployment succeeded</h3><p class="ac-10__meta">web-app · 2 min ago</p></div>
            <button class="ac-10__x" type="button" data-arch aria-label="Archive deployment succeeded">
              <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M9 11v6M15 11v6M6 7l1 13h10l1-13"/></svg>
            </button>
          </article>
        </li>
        <li class="ac-10__row">
          <span class="ac-10__under ac-10__under--l" aria-hidden="true">Snooze</span>
          <span class="ac-10__under ac-10__under--r" aria-hidden="true">Archive</span>
          <article class="ac-10__card" data-card tabindex="0" role="button" aria-roledescription="Swipeable card" aria-label="Priya commented on your pull request. Press Delete to archive.">
            <span class="ac-10__grip" aria-hidden="true"></span>
            <div class="ac-10__body"><h3 class="ac-10__name">Priya commented on your PR</h3><p class="ac-10__meta">#218 · 14 min ago</p></div>
            <button class="ac-10__x" type="button" data-arch aria-label="Archive Priya commented on your pull request">
              <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M9 11v6M15 11v6M6 7l1 13h10l1-13"/></svg>
            </button>
          </article>
        </li>
        <li class="ac-10__row">
          <span class="ac-10__under ac-10__under--l" aria-hidden="true">Snooze</span>
          <span class="ac-10__under ac-10__under--r" aria-hidden="true">Archive</span>
          <article class="ac-10__card" data-card tabindex="0" role="button" aria-roledescription="Swipeable card" aria-label="Storage at 82 percent. Press Delete to archive.">
            <span class="ac-10__grip" aria-hidden="true"></span>
            <div class="ac-10__body"><h3 class="ac-10__name">Storage at 82%</h3><p class="ac-10__meta">eu-west-1 · 1 hr ago</p></div>
            <button class="ac-10__x" type="button" data-arch aria-label="Archive storage at 82 percent">
              <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M9 11v6M15 11v6M6 7l1 13h10l1-13"/></svg>
            </button>
          </article>
        </li>
        <li class="ac-10__row">
          <span class="ac-10__under ac-10__under--l" aria-hidden="true">Snooze</span>
          <span class="ac-10__under ac-10__under--r" aria-hidden="true">Archive</span>
          <article class="ac-10__card" data-card tabindex="0" role="button" aria-roledescription="Swipeable card" aria-label="Weekly digest ready. Press Delete to archive.">
            <span class="ac-10__grip" aria-hidden="true"></span>
            <div class="ac-10__body"><h3 class="ac-10__name">Weekly digest is ready</h3><p class="ac-10__meta">Analytics · 3 hr ago</p></div>
            <button class="ac-10__x" type="button" data-arch aria-label="Archive weekly digest">
              <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M9 11v6M15 11v6M6 7l1 13h10l1-13"/></svg>
            </button>
          </article>
        </li>
      </ul>
      <p class="ac-10__empty" data-empty hidden>Inbox zero. Press <b>Restore</b>.</p>
      <p class="ac-10__sr" role="status" aria-live="polite" data-status></p>
    </div>
    <p class="ac-10__chip" aria-hidden="true">Pointer Events + setPointerCapture · touch-action:pan-y · velocity or 35% threshold · rubber-band resist · keyboard parity</p>
  </div>
</section>
```
## CSS
```css
.ac-10,
.ac-10 *,
.ac-10 *::before,
.ac-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ac-10 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --ac-10-bg: oklch(0.16 0.014 255);
  --ac-10-card: oklch(0.23 0.017 255);
  --ac-10-ink: oklch(0.97 0.004 260);
  --ac-10-mut: oklch(0.69 0.02 258);
  --ac-10-acc: oklch(0.72 0.15 250);
  --ac-10-warn: oklch(0.72 0.16 62);
  --ac-10-line: oklch(1 0 0/.11);
  background: var(--ac-10-bg);
  color: var(--ac-10-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.ac-10__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 16px;
  padding: clamp(18px,4vw,50px);
}

.ac-10__phone {
  width: min(100%,430px);
  display: grid;
  gap: 12px;
  padding: clamp(16px,4vw,22px);
  border: 1px solid var(--ac-10-line);
  border-radius: 26px;
  background: oklch(0.19 0.015 255);
  box-shadow: 0 40px 80px -44px oklch(0 0 0/.85);
}

.ac-10__top {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 14px;
}

.ac-10__eyebrow {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--ac-10-acc);
}

.ac-10__title {
  font-size: 21px;
  font-weight: 660;
  letter-spacing: -.03em;
  margin-top: 4px;
}

.ac-10__reset {
  min-height: 44px;
  padding: 0 16px;
  border: 1px solid var(--ac-10-line);
  border-radius: 99px;
  background: transparent;
  color: var(--ac-10-ink);
  font-size: 13px;
  font-weight: 600;
  font-family: inherit;
  cursor: pointer;
  transition: background .2s;
}

.ac-10__reset:hover {
  background: oklch(1 0 0/.07);
}

.ac-10__reset:focus-visible {
  outline: 2px solid var(--ac-10-acc);
  outline-offset: 3px;
}

.ac-10__hint {
  font-size: 12.5px;
  color: var(--ac-10-mut);
}

.ac-10__hint kbd {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  border: 1px solid var(--ac-10-line);
  border-bottom-width: 2px;
  border-radius: 5px;
  padding: 1px 5px;
}

.ac-10__list {
  display: grid;
  gap: 9px;
  list-style: none;
}

.ac-10__row {
  position: relative;
  border-radius: 16px;
  overflow: hidden;
}

.ac-10__under {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  padding: 0 20px;
  font-size: 12.5px;
  font-weight: 700;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: oklch(0.15 0.02 250);
  opacity: 0;
  transition: opacity .18s;
}

.ac-10__under--l {
  justify-content: flex-start;
  background: var(--ac-10-warn);
}

.ac-10__under--r {
  justify-content: flex-end;
  background: oklch(0.72 0.17 20);
}

.ac-10__row[data-dir="1"] .ac-10__under--l {
  opacity: 1;
}

.ac-10__row[data-dir="-1"] .ac-10__under--r {
  opacity: 1;
}

.ac-10__card {
  position: relative;
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 14px 12px 14px 14px;
  border: 1px solid var(--ac-10-line);
  border-radius: 16px;
  background: var(--ac-10-card);
  touch-action: pan-y;
  cursor: grab;
  user-select: none;
  translate: var(--ac-10-x,0) 0;
  rotate: var(--ac-10-r,0deg);
  opacity: var(--ac-10-o,1);
}

.ac-10__card:active {
  cursor: grabbing;
}

.ac-10__card:focus-visible {
  outline: 2px solid var(--ac-10-acc);
  outline-offset: 2px;
}

.ac-10__card[data-settle] {
  transition: translate .42s cubic-bezier(.16,1,.3,1),rotate .42s cubic-bezier(.16,1,.3,1),opacity .3s;
}

.ac-10__grip {
  flex: none;
  width: 4px;
  height: 30px;
  border-radius: 99px;
  background: color-mix(in oklch,var(--ac-10-acc) 60%,transparent);
}

.ac-10__body {
  flex: 1;
  min-width: 0;
  display: grid;
  gap: 3px;
}

.ac-10__name {
  font-size: 14.5px;
  font-weight: 640;
  letter-spacing: -.015em;
  line-height: 1.3;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.ac-10__meta {
  font-size: 12px;
  color: var(--ac-10-mut);
  font-variant-numeric: tabular-nums;
}

.ac-10__x {
  flex: none;
  display: grid;
  place-items: center;
  width: 44px;
  height: 44px;
  border: 0;
  border-radius: 12px;
  background: transparent;
  color: var(--ac-10-mut);
  cursor: pointer;
  transition: background .18s,color .18s;
}

.ac-10__x:hover {
  background: oklch(1 0 0/.08);
  color: var(--ac-10-ink);
}

.ac-10__x:focus-visible {
  outline: 2px solid var(--ac-10-acc);
  outline-offset: 2px;
}

.ac-10__empty {
  text-align: center;
  font-size: 13.5px;
  color: var(--ac-10-mut);
  padding: 22px 0;
}

.ac-10__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.ac-10__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  line-height: 1.6;
  color: var(--ac-10-mut);
  padding: 8px 15px;
  border: 1px solid var(--ac-10-line);
  border-radius: 99px;
  text-align: center;
  max-width: min(100%,720px);
}

@media (prefers-reduced-motion: reduce) {
  .ac-10__card[data-settle] {
    transition-duration: .01ms;
  }
}
```

## JavaScript
```js
(() => {
  const THRESH = 0.35, RESIST_AT = 0.6, FLICK = 0.55;   // fraction of width, damping point, px/ms
  document.querySelectorAll('.ac-10').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    const list = root.querySelector('[data-list]');
    const empty = root.querySelector('[data-empty]');
    const status = root.querySelector('[data-status]');
    const seed = list.innerHTML;

    const sync = () => {
      const n = list.querySelectorAll('.ac-10__row').length;
      empty.hidden = n > 0;
    };

    const dismiss = (card, dir) => {
      const row = card.closest('.ac-10__row');
      const label = card.querySelector('.ac-10__name').textContent;
      card.dataset.settle = '';
      card.style.setProperty('--ac-10-x', dir * (card.offsetWidth + 90) + 'px');
      card.style.setProperty('--ac-10-r', dir * 9 + 'deg');
      card.style.setProperty('--ac-10-o', '0');
      const kill = () => { row.remove(); sync(); };
      card.addEventListener('transitionend', kill, { once: true });
      setTimeout(kill, 500);
      status.textContent = label + (dir < 0 ? ' archived.' : ' snoozed.');
    };

    const wire = (card) => {
      const row = card.closest('.ac-10__row');
      let id = null, x0 = 0, t0 = 0, dx = 0;

      card.addEventListener('pointerdown', (e) => {
        if (e.target.closest('button')) return;
        id = e.pointerId; x0 = e.clientX; t0 = performance.now(); dx = 0;
        card.setPointerCapture(id);
        card.removeAttribute('data-settle');            // no transition while dragging
      });

      card.addEventListener('pointermove', (e) => {
        if (e.pointerId !== id) return;
        const raw = e.clientX - x0, w = card.offsetWidth, limit = w * RESIST_AT;
        // rubber-band past the commit point so the thumb can feel the threshold
        dx = Math.abs(raw) > limit ? Math.sign(raw) * (limit + (Math.abs(raw) - limit) * 0.4) : raw;
        card.style.setProperty('--ac-10-x', dx + 'px');
        card.style.setProperty('--ac-10-r', dx / 26 + 'deg');
        card.style.setProperty('--ac-10-o', String(1 - Math.min(0.55, Math.abs(dx) / w)));
        row.dataset.dir = dx === 0 ? '0' : String(Math.sign(dx));
      });

      const end = (e) => {
        if (e.pointerId !== id) return;
        id = null;
        const w = card.offsetWidth, v = Math.abs(dx) / Math.max(1, performance.now() - t0);
        if (Math.abs(dx) > w * THRESH || (v > FLICK && Math.abs(dx) > 24)) { dismiss(card, Math.sign(dx)); return; }
        card.dataset.settle = '';
        card.style.setProperty('--ac-10-x', '0px');
        card.style.setProperty('--ac-10-r', '0deg');
        card.style.setProperty('--ac-10-o', '1');
        row.dataset.dir = '0';
      };
      card.addEventListener('pointerup', end);
      card.addEventListener('pointercancel', end);

      card.addEventListener('keydown', (e) => {                 // keyboard parity, not an afterthought
        if (e.key === 'Delete' || e.key === 'Backspace') { e.preventDefault(); dismiss(card, -1); }
      });
      card.querySelector('[data-arch]').addEventListener('click', () => dismiss(card, -1));
    };

    const wireAll = () => list.querySelectorAll('[data-card]').forEach(wire);
    root.querySelector('[data-reset]').addEventListener('click', () => {
      list.innerHTML = seed; wireAll(); sync(); status.textContent = 'Cards restored.';
    });
    wireAll(); sync();
  });
})();
```
