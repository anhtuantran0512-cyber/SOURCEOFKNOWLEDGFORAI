---
source: "codefronts"
url: "https://codefronts.com/navigation/css-sticky-navigation/sticky-horizontal-scroll-tab-bar-with-snap-points/"
title: "Sticky Horizontal Scroll Tab Bar with Snap Points"
section: "navigation"
category: "css-sticky-navigation"
category_name: "CSS Sticky Navigations"
description: "Category rails carry the whole navigation of a menu, a storefront or a news app on a phone: more tabs than fit, pinned to the top of the view, snapping…"
has_js: "true"
---

Here's a working CSS Sticky Navigation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sticky Horizontal Scroll Tab Bar with Snap Points
Source: https://codefronts.com/navigation/css-sticky-navigation/sticky-horizontal-scroll-tab-bar-with-snap-points/

Category rails carry the whole navigation of a menu, a storefront or a news app on a phone: more tabs than fit, pinned to the top of the view, snapping cleanly as a thumb flicks across them. This build pairs the scroll mechanics with the full keyboard tab pattern, so the rail works identically from a trackpad, a thumb and an arrow key.
## HTML
```html
<section class="sn-24" aria-label="Sticky horizontal scroll tab bar demo">
    <header class="sn-24__bar">
      <a class="sn-24__brand" href="#sn-24-p1"><span class="sn-24__logo" aria-hidden="true"></span>Fold &amp; Ember</a>
      <p class="sn-24__hours">Open until 22:00</p>
    </header>
  <div class="sn-24__intro">
    <div class="sn-24__introin">
    <p class="sn-24__intro-eyebrow">scroll-snap · role="tablist"</p>
    <h2 class="sn-24__intro-title">More tabs than fit, pinned to the top</h2>
    <p class="sn-24__intro-sub">Drag the rail, or focus a tab and use the arrow keys — selection and scroll stay in sync.</p>
    </div>
  </div>
    <div class="sn-24__railwrap">
      <div class="sn-24__rail" id="sn-24-rail" role="tablist" aria-label="Menu categories">
        <button class="sn-24__tab" type="button" role="tab" id="sn-24-t1" aria-controls="sn-24-p1" aria-selected="true" tabindex="0">All day</button>
        <button class="sn-24__tab" type="button" role="tab" id="sn-24-t2" aria-controls="sn-24-p2" aria-selected="false" tabindex="-1">Bowls</button>
        <button class="sn-24__tab" type="button" role="tab" id="sn-24-t3" aria-controls="sn-24-p3" aria-selected="false" tabindex="-1">From the grill</button>
        <button class="sn-24__tab" type="button" role="tab" id="sn-24-t4" aria-controls="sn-24-p4" aria-selected="false" tabindex="-1">Handhelds</button>
        <button class="sn-24__tab" type="button" role="tab" id="sn-24-t5" aria-controls="sn-24-p5" aria-selected="false" tabindex="-1">Sweets</button>
        <button class="sn-24__tab" type="button" role="tab" id="sn-24-t6" aria-controls="sn-24-p6" aria-selected="false" tabindex="-1">Coffee</button>
      </div>
    </div>
    <main class="sn-24__panels">
      <section class="sn-24__panel" role="tabpanel" id="sn-24-p1" aria-labelledby="sn-24-t1" tabindex="0">
        <article class="sn-24__feature">
          <img class="sn-24__img" src="https://images.unsplash.com/photo-1504674900247-0877df9cc836?q=80&w=900&auto=format&fit=crop" alt="A plated main course served on a dark table" width="900" height="600" loading="lazy" decoding="async">
          <div class="sn-24__fbody"><p class="sn-24__ftag">Chef's plate</p><h3 class="sn-24__fh">Slow-braised shoulder</h3><p class="sn-24__fp">Served from noon. Snap points keep each category flush with the rail's padding.</p></div>
        </article>
        <ul class="sn-24__list"><li class="sn-24__row"><span>Cured trout, dill oil</span><span class="sn-24__price">£14</span></li><li class="sn-24__row"><span>Charred greens, hazelnut</span><span class="sn-24__price">£9</span></li></ul>
      </section>
      <section class="sn-24__panel" role="tabpanel" id="sn-24-p2" aria-labelledby="sn-24-t2" tabindex="0" hidden>
        <article class="sn-24__feature">
          <img class="sn-24__img" src="https://images.unsplash.com/photo-1540189549336-e6e99c3679fe?q=80&w=900&auto=format&fit=crop" alt="A fresh salad bowl with mixed vegetables" width="900" height="600" loading="lazy" decoding="async">
          <div class="sn-24__fbody"><p class="sn-24__ftag">Bowls</p><h3 class="sn-24__fh">Grain bowl, preserved lemon</h3><p class="sn-24__fp">Arrow keys move selection with wraparound; the rail scrolls the focused tab into the centre by arithmetic.</p></div>
        </article>
        <ul class="sn-24__list"><li class="sn-24__row"><span>Roast squash, tahini</span><span class="sn-24__price">£12</span></li><li class="sn-24__row"><span>Chilli butter beans</span><span class="sn-24__price">£11</span></li></ul>
      </section>
      <section class="sn-24__panel" role="tabpanel" id="sn-24-p3" aria-labelledby="sn-24-t3" tabindex="0" hidden>
        <article class="sn-24__feature">
          <img class="sn-24__img" src="https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?q=80&w=900&auto=format&fit=crop" alt="A stone-baked pizza fresh from the oven" width="900" height="600" loading="lazy" decoding="async">
          <div class="sn-24__fbody"><p class="sn-24__ftag">From the grill</p><h3 class="sn-24__fh">Ember flatbread</h3><p class="sn-24__fp">The edge fade is the affordance: a rail cut dead at the boundary reads as finished and nobody scrolls it.</p></div>
        </article>
        <ul class="sn-24__list"><li class="sn-24__row"><span>Flat iron, bone marrow</span><span class="sn-24__price">£23</span></li><li class="sn-24__row"><span>Whole plaice, capers</span><span class="sn-24__price">£26</span></li></ul>
      </section>
      <section class="sn-24__panel" role="tabpanel" id="sn-24-p4" aria-labelledby="sn-24-t4" tabindex="0" hidden>
        <article class="sn-24__feature">
          <img class="sn-24__img" src="https://images.unsplash.com/photo-1568901346375-23c9450c58cd?q=80&w=900&auto=format&fit=crop" alt="A stacked burger with melted cheese on a board" width="900" height="600" loading="lazy" decoding="async">
          <div class="sn-24__fbody"><p class="sn-24__ftag">Handhelds</p><h3 class="sn-24__fh">Dry-aged cheeseburger</h3><p class="sn-24__fp">Every tab is at least 44px tall with 8px between targets, the spacing that survives a moving train.</p></div>
        </article>
        <ul class="sn-24__list"><li class="sn-24__row"><span>Fried chicken, kimchi</span><span class="sn-24__price">£13</span></li><li class="sn-24__row"><span>Mushroom banh mi</span><span class="sn-24__price">£11</span></li></ul>
      </section>
      <section class="sn-24__panel" role="tabpanel" id="sn-24-p5" aria-labelledby="sn-24-t5" tabindex="0" hidden>
        <article class="sn-24__feature">
          <img class="sn-24__img" src="https://images.unsplash.com/photo-1551024506-0bccd828d307?q=80&w=900&auto=format&fit=crop" alt="A dessert plated with cream and berries" width="900" height="600" loading="lazy" decoding="async">
          <div class="sn-24__fbody"><p class="sn-24__ftag">Sweets</p><h3 class="sn-24__fh">Burnt honey custard</h3><p class="sn-24__fp">Panels are plain sections toggled with the hidden attribute — no display juggling, no layout thrash.</p></div>
        </article>
        <ul class="sn-24__list"><li class="sn-24__row"><span>Olive oil cake</span><span class="sn-24__price">£7</span></li><li class="sn-24__row"><span>Salted caramel tart</span><span class="sn-24__price">£8</span></li></ul>
      </section>
      <section class="sn-24__panel" role="tabpanel" id="sn-24-p6" aria-labelledby="sn-24-t6" tabindex="0" hidden>
        <article class="sn-24__feature">
          <img class="sn-24__img" src="https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?q=80&w=900&auto=format&fit=crop" alt="A cup of coffee on a wooden counter" width="900" height="600" loading="lazy" decoding="async">
          <div class="sn-24__fbody"><p class="sn-24__ftag">Coffee</p><h3 class="sn-24__fh">Single origin, rotating</h3><p class="sn-24__fp">Home and End jump to the ends of the rail — small detail, large difference for keyboard users.</p></div>
        </article>
        <ul class="sn-24__list"><li class="sn-24__row"><span>Cortado</span><span class="sn-24__price">£3.40</span></li><li class="sn-24__row"><span>Filter, 12oz</span><span class="sn-24__price">£3.80</span></li></ul>
      </section>
    </main>
  <footer class="sn-24__pagefoot">
    <p class="sn-24__pagefootin">Sticky navigation pattern 24 of 25 · codefronts.com</p>
  </footer>
</section>
```
## CSS
```css
.sn-24 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--sn-24-bg);
  --sn-24-bg: oklch(0.96 0.016 75);
  --sn-24-surface: oklch(0.995 0.005 75);
  --sn-24-ink: oklch(0.23 0.026 55);
  --sn-24-mut: oklch(0.53 0.022 55);
  --sn-24-acc: oklch(0.58 0.16 52);
  --sn-24-line: oklch(0.23 0.026 55/.13);
  --sn-24-h: 56px;
  --sn-24-rail: 58px;
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--sn-24-ink);
  -webkit-font-smoothing: antialiased;
}

.sn-24 *,
.sn-24 *::before,
.sn-24 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sn-24__eyebrow,
.sn-24__intro-eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--sn-24-acc);
}

.sn-24__title,
.sn-24__intro-title {
  font-size: clamp(22px,3.4vw,35px);
  line-height: 1.06;
  letter-spacing: -.03em;
  font-weight: 700;
  text-wrap: balance;
}

.sn-24__sub,
.sn-24__intro-sub {
  font-size: 14.2px;
  line-height: 1.6;
  color: var(--sn-24-mut);
  text-wrap: pretty;
}

.sn-24__scroll:focus-visible,
.sn-24__panel:focus-visible {
  outline: 2px solid var(--sn-24-acc);
  outline-offset: -2px;
}

.sn-24__bar {
  position: sticky;
  top: 0;
  z-index: 30;
  display: flex;
  align-items: center;
  gap: 14px;
  min-height: var(--sn-24-h);
  padding: 0 clamp(14px,2.6vw,20px);
  background: color-mix(in oklch,var(--sn-24-surface) 88%,transparent);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
}

.sn-24__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 15px;
  font-weight: 700;
  letter-spacing: -.03em;
  color: inherit;
  text-decoration: none;
  white-space: nowrap;
}

.sn-24__brand:focus-visible {
  outline: 2px solid var(--sn-24-acc);
  outline-offset: 2px;
}

.sn-24__logo {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: radial-gradient(circle at 32% 30%,oklch(0.85 0.12 78),var(--sn-24-acc));
}

.sn-24__hours {
  margin-inline-start: auto;
  font-size: 12.2px;
  font-weight: 600;
  color: var(--sn-24-acc);
  padding: 5px 11px;
  border-radius: 99px;
  background: color-mix(in oklch,var(--sn-24-acc) 11%,transparent);
}

.sn-24__railwrap {
  position: sticky;
  top: var(--sn-24-h);
  z-index: 20;
  block-size: var(--sn-24-rail);
  background: color-mix(in oklch,var(--sn-24-surface) 90%,transparent);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border-bottom: 1px solid var(--sn-24-line);
}

.sn-24__rail {
  display: flex;
  align-items: center;
  gap: 8px;
  block-size: 100%;
  padding-inline: clamp(14px,2.6vw,20px);
  overflow-x: auto;
  overscroll-behavior-inline: contain;
  scroll-snap-type: inline mandatory;
  scroll-padding-inline-start: clamp(14px,2.6vw,20px);
  scroll-behavior: smooth;
  scrollbar-width: none;
  -webkit-mask-image: linear-gradient(90deg,#000 0,#000 calc(100% - 40px),transparent 100%);
  mask-image: linear-gradient(90deg,#000 0,#000 calc(100% - 40px),transparent 100%);
}

.sn-24__rail::-webkit-scrollbar {
  display: none;
}

.sn-24__tab {
  flex: none;
  scroll-snap-align: start;
  display: flex;
  align-items: center;
  min-block-size: 40px;
  padding: 0 15px;
  border: 1px solid var(--sn-24-line);
  border-radius: 99px;
  background: transparent;
  font-family: inherit;
  font-size: 13.4px;
  font-weight: 620;
  color: var(--sn-24-mut);
  white-space: nowrap;
  cursor: pointer;
  transition: color .2s ease,background .2s ease,border-color .2s ease,transform .2s ease;
}

.sn-24__tab:hover {
  color: var(--sn-24-ink);
  background: oklch(0.23 0.026 55/.05);
}

.sn-24__tab:focus-visible {
  outline: 2px solid var(--sn-24-acc);
  outline-offset: 2px;
}

.sn-24__tab[aria-selected="true"] {
  color: oklch(1 0 0);
  background: var(--sn-24-acc);
  border-color: transparent;
  box-shadow: 0 8px 18px -12px var(--sn-24-acc);
}

.sn-24__tab:active {
  transform: scale(.97);
}

.sn-24__panels {
  padding: clamp(14px,3vw,22px);
}

.sn-24__panel {
  display: grid;
  gap: 14px;
  animation: sn-24-in .34s cubic-bezier(.32,.72,.3,1) both;
}

.sn-24__panel[hidden] {
  display: none;
}

@keyframes sn-24-in {
  from {
    opacity: 0;
    transform: translateY(8px);
  }

  to {
    opacity: 1;
    transform: none;
  }
}

.sn-24__feature {
  border: 1px solid var(--sn-24-line);
  border-radius: 16px;
  overflow: hidden;
  background: var(--sn-24-surface);
  display: grid;
  grid-template-columns: minmax(0,42%) minmax(0,1fr);
}

.sn-24__img {
  inline-size: 100%;
  block-size: 100%;
  min-block-size: 150px;
  object-fit: cover;
  display: block;
  background: linear-gradient(140deg,oklch(0.84 0.09 70),oklch(0.62 0.13 45));
}

.sn-24__fbody {
  display: grid;
  align-content: center;
  gap: 6px;
  padding: clamp(14px,2.6vw,20px);
}

.sn-24__ftag {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 10.6px;
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--sn-24-acc);
}

.sn-24__fh {
  font-size: clamp(17px,2.3vw,21px);
  line-height: 1.16;
  letter-spacing: -.025em;
  font-weight: 700;
  text-wrap: balance;
}

.sn-24__fp {
  font-size: 13.6px;
  line-height: 1.6;
  color: var(--sn-24-mut);
  text-wrap: pretty;
}

.sn-24__list {
  list-style: none;
  display: grid;
  gap: 2px;
}

.sn-24__row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  padding: 13px 4px;
  font-size: 14.2px;
  border-bottom: 1px dashed var(--sn-24-line);
}

.sn-24__price {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 13px;
  color: var(--sn-24-acc);
}

@media (max-width: 600px) {
  .sn-24__feature {
    grid-template-columns: minmax(0,1fr);
  }

  .sn-24__img {
    min-block-size: 126px;
    max-block-size: 126px;
  }

  .sn-24__hours {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sn-24__scroll,
    .sn-24__rail {
    scroll-behavior: auto;
  }

  .sn-24__panel {
    animation: none;
  }

  .sn-24 * {
    transition-duration: .01ms !important;
  }
}
/* ── full-page mode: the demo IS the document, so sticky pins against the real viewport ── */

:root:has(.sn-24) {
  scroll-behavior: smooth;
  scroll-padding-top: calc(var(--sn-24-h) + var(--sn-24-rail));
}

@media (prefers-reduced-motion: reduce) {
  :root:has(.sn-24) {
    scroll-behavior: auto;
  }
}

.sn-24__bar,
.sn-24__barin {
  padding-inline: max(clamp(16px,3vw,26px),calc((100% - 1280px)/2));
}

.sn-24__sec {
  padding-inline: max(clamp(22px,5vw,44px),calc((100% - 1120px)/2));
}

.sn-24__intro {
  display: grid;
  place-items: center;
  min-height: min(90svh,900px);
  padding: clamp(56px,12vh,150px) clamp(20px,5vw,48px) clamp(40px,8vh,90px);
  background: radial-gradient(85% 52% at 50% 0%,oklch(0.98 0.035 68),transparent);
}

.sn-24__introin {
  display: grid;
  justify-items: center;
  gap: clamp(12px,1.8vw,18px);
  text-align: center;
  max-width: 26ch;
}

.sn-24__intro-eyebrow {
  font-size: clamp(11px,1.1vw,13px);
}

.sn-24__intro-title {
  font-size: clamp(38px,7.5vw,86px);
  line-height: .98;
  letter-spacing: -.04em;
  max-width: none;
}

.sn-24__intro-sub {
  font-size: clamp(15px,1.7vw,19px);
  line-height: 1.55;
  max-width: 46ch;
}

.sn-24__intro::after {
  content: "Scroll — the bar stays";
  justify-self: center;
  margin-block-start: clamp(20px,4vh,44px);
  padding: 9px 18px;
  border: 1px solid var(--sn-24-line);
  border-radius: 99px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--sn-24-mut);
  animation: sn-24-cue 2.6s ease-in-out infinite;
}

@keyframes sn-24-cue {
  0%,
    100% {
    transform: translateY(0);
    opacity: .75;
  }

  50% {
    transform: translateY(5px);
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sn-24__intro::after {
    animation: none;
  }
}

.sn-24__pagefoot {
  display: grid;
  place-items: center;
  padding: clamp(44px,9vh,110px) 24px;
  border-top: 1px solid var(--sn-24-line);
}

.sn-24__pagefootin {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  letter-spacing: .06em;
  color: var(--sn-24-mut);
  text-align: center;
}

.sn-24__intro-title,
.sn-24__intro-sub {
  text-wrap: balance;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.sn-24');
  if (!root || root.dataset.snWired) return;
  root.dataset.snWired = '1';
  const rail = root.querySelector('#sn-24-rail');
  const tabs = [...root.querySelectorAll('.sn-24__tab')];
  const centre = (tab) => {
    const left = tab.offsetLeft - (rail.clientWidth - tab.offsetWidth) / 2;
    rail.scrollTo({ left: Math.max(0, left), behavior: 'smooth' });
  };
  const select = (tab, focus) => {
    tabs.forEach((t) => {
      const on = t === tab;
      t.setAttribute('aria-selected', String(on));
      t.tabIndex = on ? 0 : -1;
      const panel = root.querySelector('#' + t.getAttribute('aria-controls'));
      if (panel) panel.hidden = !on;
    });
    if (focus) tab.focus();
    centre(tab);
  };
  tabs.forEach((tab) => tab.addEventListener('click', () => select(tab, false)));
  rail.addEventListener('keydown', (e) => {
    const i = tabs.indexOf(document.activeElement);
    if (i < 0) return;
    const keys = { ArrowRight: i + 1, ArrowLeft: i - 1, Home: 0, End: tabs.length - 1 };
    if (!(e.key in keys)) return;
    e.preventDefault();
    select(tabs[(keys[e.key] + tabs.length) % tabs.length], true);
  });
})();
```
