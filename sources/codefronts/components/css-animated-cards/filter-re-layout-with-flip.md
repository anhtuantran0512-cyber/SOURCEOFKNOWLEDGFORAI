---
source: "codefronts"
url: "https://codefronts.com/components/css-animated-cards/filter-re-layout-with-flip/"
title: "Filter Re-Layout with FLIP"
section: "components"
category: "css-animated-cards"
category_name: "CSS Animated Cards"
description: "Filter a grid by category and the surviving cards travel to their new positions instead of teleporting."
has_js: "true"
---

Here's a working CSS Animated Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Filter Re-Layout with FLIP
Source: https://codefronts.com/components/css-animated-cards/filter-re-layout-with-flip/

Filter a grid by category and the surviving cards travel to their new positions instead of teleporting. This is FLIP — First, Last, Invert, Play — thirty lines of vanilla JS using getBoundingClientRect and the Web Animations API, the technique behind every polished layout transition. Includes the View Transitions one-liner alternative for browsers that have it.
## HTML
```html
<section class="ac-06" aria-label="Filter re-layout with FLIP demo">
  <div class="ac-06__stage">
    <header class="ac-06__head">
      <p class="ac-06__eyebrow">Layout animation</p>
      <h2 class="ac-06__title">Cards that travel to their new position</h2>
      <div class="ac-06__tabs" role="group" aria-label="Filter cards by category">
        <button class="ac-06__tab" type="button" data-filter="all" aria-pressed="true">All</button>
        <button class="ac-06__tab" type="button" data-filter="ui" aria-pressed="false">Interface</button>
        <button class="ac-06__tab" type="button" data-filter="type" aria-pressed="false">Typography</button>
        <button class="ac-06__tab" type="button" data-filter="motion" aria-pressed="false">Motion</button>
      </div>
    </header>
    <ul class="ac-06__grid" role="list" data-grid>
      <li class="ac-06__card" data-cat="ui"><span class="ac-06__sw" style="--ac-06-c:oklch(0.72 0.17 42)"></span><h3 class="ac-06__name">Command palette</h3><p class="ac-06__tag">Interface</p></li>
      <li class="ac-06__card" data-cat="type"><span class="ac-06__sw" style="--ac-06-c:oklch(0.75 0.15 92)"></span><h3 class="ac-06__name">Fluid type scale</h3><p class="ac-06__tag">Typography</p></li>
      <li class="ac-06__card" data-cat="motion"><span class="ac-06__sw" style="--ac-06-c:oklch(0.74 0.16 155)"></span><h3 class="ac-06__name">Spring easing set</h3><p class="ac-06__tag">Motion</p></li>
      <li class="ac-06__card" data-cat="ui"><span class="ac-06__sw" style="--ac-06-c:oklch(0.70 0.16 262)"></span><h3 class="ac-06__name">Sheet &amp; drawer</h3><p class="ac-06__tag">Interface</p></li>
      <li class="ac-06__card" data-cat="motion"><span class="ac-06__sw" style="--ac-06-c:oklch(0.72 0.18 330)"></span><h3 class="ac-06__name">Page transitions</h3><p class="ac-06__tag">Motion</p></li>
      <li class="ac-06__card" data-cat="type"><span class="ac-06__sw" style="--ac-06-c:oklch(0.78 0.14 200)"></span><h3 class="ac-06__name">Optical sizing</h3><p class="ac-06__tag">Typography</p></li>
      <li class="ac-06__card" data-cat="ui"><span class="ac-06__sw" style="--ac-06-c:oklch(0.68 0.15 300)"></span><h3 class="ac-06__name">Data table kit</h3><p class="ac-06__tag">Interface</p></li>
      <li class="ac-06__card" data-cat="motion"><span class="ac-06__sw" style="--ac-06-c:oklch(0.76 0.16 122)"></span><h3 class="ac-06__name">Scroll choreography</h3><p class="ac-06__tag">Motion</p></li>
      <li class="ac-06__card" data-cat="type"><span class="ac-06__sw" style="--ac-06-c:oklch(0.73 0.15 20)"></span><h3 class="ac-06__name">Balanced headlines</h3><p class="ac-06__tag">Typography</p></li>
    </ul>
    <p class="ac-06__count" role="status" aria-live="polite" data-count></p>
    <p class="ac-06__chip" aria-hidden="true">First · Last · Invert · Play · getBoundingClientRect + Element.animate() · transform-only, 60 fps</p>
  </div>
</section>
```
## CSS
```css
.ac-06,
.ac-06 *,
.ac-06 *::before,
.ac-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ac-06 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --ac-06-bg: oklch(0.98 0.005 265);
  --ac-06-card: oklch(1 0 0);
  --ac-06-ink: oklch(0.23 0.02 265);
  --ac-06-mut: oklch(0.55 0.02 265);
  --ac-06-acc: oklch(0.50 0.19 268);
  --ac-06-line: oklch(0.23 0.02 265/.11);
  background: var(--ac-06-bg);
  color: var(--ac-06-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.ac-06__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(16px,2.4vw,26px);
  padding: clamp(20px,5vw,56px);
}

.ac-06__head {
  display: grid;
  justify-items: center;
  gap: 13px;
  text-align: center;
}

.ac-06__eyebrow {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--ac-06-acc);
}

.ac-06__title {
  font-size: clamp(23px,3.4vw,38px);
  font-weight: 650;
  line-height: 1.12;
  letter-spacing: -.03em;
  text-wrap: balance;
}

.ac-06__tabs {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  justify-content: center;
  padding: 5px;
  border: 1px solid var(--ac-06-line);
  border-radius: 99px;
  background: var(--ac-06-card);
}

.ac-06__tab {
  min-height: 44px;
  padding: 0 20px;
  border: 0;
  border-radius: 99px;
  background: transparent;
  color: var(--ac-06-mut);
  font-size: 13.5px;
  font-weight: 600;
  font-family: inherit;
  cursor: pointer;
  transition: background .22s,color .22s;
}

.ac-06__tab:hover {
  color: var(--ac-06-ink);
  background: oklch(0.23 0.02 265/.05);
}

.ac-06__tab[aria-pressed="true"] {
  background: var(--ac-06-acc);
  color: oklch(0.99 0 0);
}

.ac-06__tab:focus-visible {
  outline: 2px solid var(--ac-06-acc);
  outline-offset: 2px;
}

.ac-06__grid {
  display: grid;
  grid-template-columns: repeat(auto-fill,minmax(178px,1fr));
  gap: 12px;
  width: min(100%,820px);
  list-style: none;
}

.ac-06__card {
  display: grid;
  gap: 9px;
  padding: 16px;
  border: 1px solid var(--ac-06-line);
  border-radius: 17px;
  background: var(--ac-06-card);
  box-shadow: 0 1px 2px oklch(0.23 0.02 265/.05);
  will-change: transform;
}

.ac-06__card[hidden] {
  display: none;
}

.ac-06__sw {
  width: 34px;
  height: 34px;
  border-radius: 10px;
  background: var(--ac-06-c);
  box-shadow: 0 6px 14px -6px var(--ac-06-c);
}

.ac-06__name {
  font-size: 14.5px;
  font-weight: 640;
  letter-spacing: -.015em;
  line-height: 1.3;
}

.ac-06__tag {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--ac-06-mut);
}

.ac-06__count {
  font-size: 12.5px;
  color: var(--ac-06-mut);
  font-variant-numeric: tabular-nums;
}

::view-transition-group(*) {
  animation-duration: .44s;
  animation-timing-function: cubic-bezier(.16,1,.3,1);
}

.ac-06__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  line-height: 1.6;
  color: var(--ac-06-mut);
  padding: 8px 15px;
  border: 1px dashed var(--ac-06-line);
  border-radius: 99px;
  text-align: center;
  max-width: min(100%,700px);
}

@media (prefers-reduced-motion: reduce) {
  .ac-06__tab {
    transition: none;
  }
}
```

## JavaScript
```js
(() => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.querySelectorAll('.ac-06').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    const grid = root.querySelector('[data-grid]');
    const cards = [...grid.querySelectorAll('.ac-06__card')];
    const count = root.querySelector('[data-count]');
    let current = 'all';

    const apply = (f) => cards.forEach((c) => { c.hidden = !(f === 'all' || c.dataset.cat === f); });

    const report = () => {
      const n = cards.filter((c) => !c.hidden).length;
      count.textContent = n + ' of ' + cards.length + ' cards shown';
    };

    const flip = (f) => {
      if (reduce) { apply(f); report(); return; }
      cards.forEach((c) => c.getAnimations().forEach((a) => a.finish()));   // settle before measuring
      const first = new Map(cards.map((c) => [c, c.hidden ? null : c.getBoundingClientRect()]));
      apply(f);                                                            // L — one DOM mutation
      cards.forEach((c) => {
        if (c.hidden) return;
        const a = first.get(c), b = c.getBoundingClientRect();
        if (!a) {                                                          // entering card
          c.animate([{ opacity: 0, transform: 'scale(.86)' }, { opacity: 1, transform: 'none' }],
            { duration: 340, easing: 'cubic-bezier(.16,1,.3,1)', fill: 'both' });
          return;
        }
        const dx = a.left - b.left, dy = a.top - b.top;
        if (!dx && !dy) return;
        c.animate([{ transform: 'translate(' + dx + 'px,' + dy + 'px)' }, { transform: 'none' }],
          { duration: 440, easing: 'cubic-bezier(.16,1,.3,1)' });          // I + P, transform only
      });
      report();
    };

    // Native route: name each card so the browser morphs it between the two layouts itself.
    const vt = (f) => {
      cards.forEach((c, i) => { c.style.viewTransitionName = 'ac-06-c' + i; });
      const t = document.startViewTransition(() => { apply(f); report(); });
      // An abort (tab hidden, or a second click before this one settles) rejects BOTH promises.
      // ready is the one that throws InvalidStateError — leave it dangling and every rapid click
      // logs an unhandled rejection. finished is caught separately so cleanup still runs.
      t.ready.catch(() => {});
      t.finished.catch(() => {}).finally(() => cards.forEach((c) => { c.style.viewTransitionName = ''; }));
    };

    root.querySelectorAll('[data-filter]').forEach((btn) => {
      btn.addEventListener('click', () => {
        const f = btn.dataset.filter;
        if (f === current) return;
        current = f;
        root.querySelectorAll('[data-filter]').forEach((b) => b.setAttribute('aria-pressed', String(b === btn)));
        if (document.startViewTransition && !reduce) vt(f); else flip(f);
      });
    });
    report();
  });
})();
```
