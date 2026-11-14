---
source: "codefronts"
url: "https://codefronts.com/components/css-animated-cards/view-transitions-card-to-detail-morph/"
title: "View Transitions Card-to-Detail Morph"
section: "components"
category: "css-animated-cards"
category_name: "CSS Animated Cards"
description: "Tap a card and it becomes the detail view — the thumbnail grows into the hero, the title slides into the headline, the whole thing morphs instead of cutting."
has_js: "true"
---

Here's a working CSS Animated Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: View Transitions Card-to-Detail Morph
Source: https://codefronts.com/components/css-animated-cards/view-transitions-card-to-detail-morph/

Tap a card and it becomes the detail view — the thumbnail grows into the hero, the title slides into the headline, the whole thing morphs instead of cutting. This is the shared-element transition that native apps have had for a decade, now three lines of web platform: give the paired elements the same view-transition-name and wrap the DOM change in document.startViewTransition().
## HTML
```html
<section class="ac-04" aria-label="View transitions card to detail morph demo">
  <div class="ac-04__stage">
    <header class="ac-04__head">
      <p class="ac-04__eyebrow">Shared element morph</p>
      <h2 class="ac-04__title">Tap a card — it becomes the page</h2>
    </header>
    <ul class="ac-04__grid" role="list" data-grid>
      <li class="ac-04__card">
        <img class="ac-04__thumb" src="https://images.unsplash.com/photo-1505740420928-5e560c06d30e?q=80&w=700&auto=format&fit=crop" alt="Matte black over-ear headphones" loading="lazy" decoding="async" width="700" height="700">
        <div class="ac-04__meta"><h3 class="ac-04__name">Studio Over-Ear</h3><p class="ac-04__price">$249</p></div>
        <button class="ac-04__open" type="button" data-open="0" aria-haspopup="dialog">Open<span class="ac-04__sr"> Studio Over-Ear details</span></button>
      </li>
      <li class="ac-04__card">
        <img class="ac-04__thumb" src="https://images.unsplash.com/photo-1523275335684-37898b6baf30?q=80&w=700&auto=format&fit=crop" alt="Minimal wristwatch on a light surface" loading="lazy" decoding="async" width="700" height="700">
        <div class="ac-04__meta"><h3 class="ac-04__name">Field Watch 38</h3><p class="ac-04__price">$390</p></div>
        <button class="ac-04__open" type="button" data-open="1" aria-haspopup="dialog">Open<span class="ac-04__sr"> Field Watch 38 details</span></button>
      </li>
      <li class="ac-04__card">
        <img class="ac-04__thumb" src="https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?q=80&w=700&auto=format&fit=crop" alt="Compact mirrorless camera body" loading="lazy" decoding="async" width="700" height="700">
        <div class="ac-04__meta"><h3 class="ac-04__name">Rangefinder M</h3><p class="ac-04__price">$1,180</p></div>
        <button class="ac-04__open" type="button" data-open="2" aria-haspopup="dialog">Open<span class="ac-04__sr"> Rangefinder M details</span></button>
      </li>
    </ul>
    <div class="ac-04__detail" data-detail hidden role="dialog" aria-modal="true" aria-labelledby="ac-04-dt">
      <button class="ac-04__back" type="button" data-close>
        <svg viewBox="0 0 24 24" width="17" height="17" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 18l-6-6 6-6"/></svg>
        Back to grid
      </button>
      <img class="ac-04__hero" data-hero alt="" width="900" height="600">
      <div class="ac-04__pane">
        <p class="ac-04__tag" data-tag></p>
        <h3 class="ac-04__dtitle" id="ac-04-dt" data-dtitle></h3>
        <p class="ac-04__copy" data-copy></p>
        <p class="ac-04__dprice" data-dprice></p>
      </div>
    </div>
    <p class="ac-04__chip" aria-hidden="true">document.startViewTransition() · view-transition-name pairs · ::view-transition-group timing · real dialog semantics</p>
  </div>
</section>
```
## CSS
```css
.ac-04,
.ac-04 *,
.ac-04 *::before,
.ac-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ac-04 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --ac-04-bg: oklch(0.97 0.006 95);
  --ac-04-card: oklch(1 0 0);
  --ac-04-ink: oklch(0.22 0.015 60);
  --ac-04-mut: oklch(0.55 0.02 60);
  --ac-04-acc: oklch(0.55 0.15 28);
  --ac-04-line: oklch(0.22 0.015 60/.12);
  background: var(--ac-04-bg);
  color: var(--ac-04-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.ac-04__stage {
  position: relative;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(16px,2.6vw,28px);
  padding: clamp(20px,5vw,58px);
}

.ac-04__head {
  display: grid;
  justify-items: center;
  gap: 9px;
  text-align: center;
}

.ac-04__eyebrow {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--ac-04-acc);
}

.ac-04__title {
  font-size: clamp(23px,3.4vw,38px);
  font-weight: 650;
  line-height: 1.12;
  letter-spacing: -.03em;
  text-wrap: balance;
}

.ac-04__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(210px,1fr));
  gap: clamp(12px,1.8vw,18px);
  width: min(100%,880px);
  list-style: none;
}

.ac-04__card {
  position: relative;
  display: grid;
  gap: 12px;
  padding: 12px;
  border: 1px solid var(--ac-04-line);
  border-radius: 20px;
  background: var(--ac-04-card);
  box-shadow: 0 1px 2px oklch(0.22 0.015 60/.05);
  transition: transform .3s cubic-bezier(.16,1,.3,1),box-shadow .3s;
}

.ac-04__card:hover,
.ac-04__card:focus-within {
  transform: translateY(-4px);
  box-shadow: 0 20px 40px -22px oklch(0.22 0.015 60/.55);
}

.ac-04__thumb {
  width: 100%;
  aspect-ratio: 1;
  object-fit: cover;
  border-radius: 13px;
  display: block;
  background: linear-gradient(135deg,oklch(0.88 0.03 60),oklch(0.8 0.04 30));
}

.ac-04__meta {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 10px;
  padding: 0 4px 4px;
}

.ac-04__name {
  font-size: 15px;
  font-weight: 640;
  letter-spacing: -.02em;
}

.ac-04__price {
  font-size: 14px;
  font-weight: 640;
  color: var(--ac-04-acc);
  font-variant-numeric: tabular-nums;
}

.ac-04__open {
  position: absolute;
  inset: 0;
  width: 100%;
  border: 0;
  border-radius: 20px;
  background: transparent;
  color: transparent;
  font-size: 0;
  cursor: pointer;
}

.ac-04__open:focus-visible {
  outline: 2px solid var(--ac-04-acc);
  outline-offset: 3px;
}

.ac-04__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.ac-04__detail {
  position: absolute;
  inset: clamp(14px,4vw,44px);
  display: grid;
  grid-template-columns: 1.05fr 1fr;
  align-items: stretch;
  gap: 0;
  border: 1px solid var(--ac-04-line);
  border-radius: 24px;
  overflow: hidden;
  background: var(--ac-04-card);
  box-shadow: 0 50px 90px -50px oklch(0.22 0.015 60/.7);
  view-transition-name: ac-04-panel;
}

.ac-04__detail[hidden] {
  display: none;
}

.ac-04__hero {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  background: linear-gradient(135deg,oklch(0.88 0.03 60),oklch(0.8 0.04 30));
}

.ac-04__pane {
  display: grid;
  align-content: center;
  gap: 12px;
  padding: clamp(22px,4vw,48px);
}

.ac-04__tag {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--ac-04-acc);
}

.ac-04__dtitle {
  font-size: clamp(24px,3.4vw,38px);
  font-weight: 660;
  line-height: 1.08;
  letter-spacing: -.035em;
  text-wrap: balance;
}

.ac-04__copy {
  font-size: 14.5px;
  line-height: 1.6;
  color: var(--ac-04-mut);
  text-wrap: pretty;
  max-width: 44ch;
}

.ac-04__dprice {
  font-size: 22px;
  font-weight: 680;
  font-variant-numeric: tabular-nums;
  letter-spacing: -.02em;
}

.ac-04__back {
  position: absolute;
  top: 14px;
  left: 14px;
  z-index: 2;
  display: inline-flex;
  align-items: center;
  gap: 7px;
  min-height: 44px;
  padding: 0 18px;
  border: 1px solid var(--ac-04-line);
  border-radius: 99px;
  background: oklch(1 0 0/.86);
  backdrop-filter: blur(10px);
  color: var(--ac-04-ink);
  font-size: 13.5px;
  font-weight: 600;
  font-family: inherit;
  cursor: pointer;
  transition: background .2s;
}

.ac-04__back:hover {
  background: oklch(1 0 0);
}

.ac-04__back:focus-visible {
  outline: 2px solid var(--ac-04-acc);
  outline-offset: 3px;
}

.ac-04__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  line-height: 1.6;
  color: var(--ac-04-mut);
  padding: 8px 15px;
  border: 1px dashed var(--ac-04-line);
  border-radius: 99px;
  text-align: center;
  max-width: min(100%,680px);
}

.ac-04__card[data-active] .ac-04__thumb {
  view-transition-name: ac-04-hero;
}

.ac-04__card[data-active] .ac-04__name {
  view-transition-name: ac-04-name;
}

.ac-04__detail:not([hidden]) .ac-04__hero {
  view-transition-name: ac-04-hero;
}

.ac-04__detail:not([hidden]) .ac-04__dtitle {
  view-transition-name: ac-04-name;
}

::view-transition-group(ac-04-hero),
::view-transition-group(ac-04-name),
::view-transition-group(ac-04-panel) {
  animation-duration: .46s;
  animation-timing-function: cubic-bezier(.16,1,.3,1);
}

::view-transition-old(ac-04-hero),
::view-transition-new(ac-04-hero) {
  height: 100%;
  object-fit: cover;
  overflow: clip;
}

::view-transition-old(ac-04-panel) {
  animation: ac-04-out .3s cubic-bezier(.5,0,.9,.4) both;
}

::view-transition-new(ac-04-panel) {
  animation: ac-04-pop .46s cubic-bezier(.16,1,.3,1) both;
}

@keyframes ac-04-pop {
  from {
    opacity: 0;
  }

  to {
    opacity: 1;
  }
}

@keyframes ac-04-out {
  to {
    opacity: 0;
  }
}

@media (max-width: 720px) {
  .ac-04__detail {
    grid-template-columns: 1fr;
    grid-template-rows: minmax(0,1fr) auto;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ac-04__card {
    transition: none;
  }

  ::view-transition-group(*),
    ::view-transition-old(*),
    ::view-transition-new(*) {
    animation-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  const DATA = [
    ['Studio Over-Ear', '$249', 'Acoustics', 'Forty-hour battery, adaptive ANC tuned in a real room rather than an anechoic chamber, and a headband that survives being thrown in a bag every day for three years.'],
    ['Field Watch 38', '$390', 'Horology', 'A 38 mm case that disappears under a cuff, sapphire crystal, and a movement rated to 42 hours — designed to be read at a glance in bad light.'],
    ['Rangefinder M', '$1,180', 'Optics', 'Full-frame sensor in a body the size of a paperback. Mechanical dials for every setting that matters, so you never open a menu mid-shot.'],
  ];
  document.querySelectorAll('.ac-04').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    const grid = root.querySelector('[data-grid]');
    const detail = root.querySelector('[data-detail]');
    const el = {
      hero: detail.querySelector('[data-hero]'), tag: detail.querySelector('[data-tag]'),
      title: detail.querySelector('[data-dtitle]'), copy: detail.querySelector('[data-copy]'),
      price: detail.querySelector('[data-dprice]'), back: detail.querySelector('[data-close]'),
    };
    let opener = null;

    // A view-transition-name must be unique per frame — tag only the pair that is morphing.
    // Returns the transition (or undefined) so callers can sequence focus after it settles.
    const run = (fn) => {
      if (!document.startViewTransition) { fn(); return undefined; }
      const t = document.startViewTransition(fn);
      t.ready.catch(() => {});                       // aborts reject; never leave it dangling
      return t;
    };
    // Focus must land AFTER the snapshot phase — a bare rAF during a view transition is dropped.
    const focusAfter = (t, el) => {
      if (!el) return;
      Promise.resolve(t && t.finished).catch(() => {}).finally(() => el.focus({ preventScroll: true }));
    };

    const open = (btn) => {
      const i = +btn.dataset.open, card = btn.closest('.ac-04__card');
      const [name, price, tag, copy] = DATA[i];
      opener = btn;
      card.dataset.active = '1';          // OLD snapshot: the name lives on the thumbnail
      const t = run(() => {
        delete card.dataset.active;       // NEW snapshot: it lives on the detail hero only
        el.hero.src = card.querySelector('.ac-04__thumb').src.replace('w=700', 'w=1200');
        el.hero.alt = card.querySelector('.ac-04__thumb').alt;
        el.tag.textContent = tag; el.title.textContent = name;
        el.copy.textContent = copy; el.price.textContent = price;
        grid.setAttribute('inert', ''); detail.hidden = false;
      });
      focusAfter(t, el.back);            // never leave focus on the now-inert opener
    };

    const close = () => {
      const card = opener && opener.closest('.ac-04__card');
      const t = run(() => {               // reversed: hero → thumbnail, still one name per state
        detail.hidden = true;
        grid.removeAttribute('inert');
        if (card) card.dataset.active = '1';
      });
      focusAfter(t, opener);              // return focus only once the grid is interactive again
      if (card) Promise.resolve(t && t.finished).catch(() => {}).finally(() => delete card.dataset.active);
    };

    grid.addEventListener('click', (e) => { const b = e.target.closest('[data-open]'); if (b) open(b); });
    el.back.addEventListener('click', close);
    root.addEventListener('keydown', (e) => { if (e.key === 'Escape' && !detail.hidden) { e.preventDefault(); close(); } });
  });
})();
```
