---
source: "codefronts"
url: "https://codefronts.com/components/css-pricing-tables/mobile-horizontal-swipe-carousel/"
title: "Mobile Horizontal Swipe Carousel"
section: "components"
category: "css-pricing-tables"
category_name: "CSS Pricing Tables"
description: "Mobile-first pricing that respects thumbs: cards form a horizontal swipe-and-snap deck with momentum scrolling, peeking neighbors, and pagination dots that…"
has_js: "true"
---

Here's a working CSS Pricing Table from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Mobile Horizontal Swipe Carousel
Source: https://codefronts.com/components/css-pricing-tables/mobile-horizontal-swipe-carousel/

Mobile-first pricing that respects thumbs: cards form a horizontal swipe-and-snap deck with momentum scrolling, peeking neighbors, and pagination dots that track position live — CSS scroll-snap does the physics, JS only observes.
## HTML
```html
<section class="prc-19" aria-label="Swipeable pricing plans">
  <h2 class="prc-19__title">Swipe to compare</h2>
  <div class="prc-19__rail" id="prc-19-rail" tabindex="0" aria-label="Pricing plans, horizontally scrollable">
    <article class="prc-19__card"><h3>Mini</h3><p class="prc-19__price">$5<small>/mo</small></p><ul><li>1 device</li><li>SD streaming</li></ul><a href="#" class="prc-19__cta">Get Mini</a></article>
    <article class="prc-19__card prc-19__card--hot"><h3>Duo</h3><p class="prc-19__price">$12<small>/mo</small></p><ul><li>2 devices</li><li>HD streaming</li><li>Offline mode</li></ul><a href="#" class="prc-19__cta prc-19__cta--hot">Get Duo</a></article>
    <article class="prc-19__card"><h3>Family</h3><p class="prc-19__price">$19<small>/mo</small></p><ul><li>6 devices</li><li>4K streaming</li><li>Kids profiles</li></ul><a href="#" class="prc-19__cta">Get Family</a></article>
  </div>
  <div class="prc-19__dots" id="prc-19-dots" role="tablist" aria-label="Plan pager">
    <button role="tab" aria-selected="true" aria-label="Plan 1 of 3"></button>
    <button role="tab" aria-selected="false" aria-label="Plan 2 of 3"></button>
    <button role="tab" aria-selected="false" aria-label="Plan 3 of 3"></button>
  </div>
</section>
```
## CSS
```css
.prc-19,
.prc-19 *,
.prc-19 *::before,
.prc-19 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.prc-19 {
  --accent: oklch(0.63 0.2 350);
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #171219;
  color: #f4eef6;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 56px 0;
}

.prc-19__title {
  text-align: center;
  font-size: clamp(24px,3.6vw,34px);
  font-weight: 800;
  letter-spacing: -.02em;
  margin-bottom: 30px;
  padding: 0 24px;
}

.prc-19__rail {
  display: flex;
  gap: 16px;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  padding: 12px max(24px,calc(50vw - 200px)) 24px;
  scrollbar-width: none;
  -webkit-overflow-scrolling: touch;
}

.prc-19__rail::-webkit-scrollbar {
  display: none;
}

.prc-19__rail:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: -3px;
}

.prc-19__card {
  flex: 0 0 min(78%,340px);
  scroll-snap-align: center;
  background: #211a25;
  border: 1.5px solid #362c3c;
  border-radius: 20px;
  padding: 28px;
  display: flex;
  flex-direction: column;
  gap: 8px;
  transition: transform .35s,border-color .35s;
  transform: scale(.94);
}

.prc-19__card.prc-19__active {
  transform: scale(1);
  border-color: var(--accent);
}

.prc-19__card--hot.prc-19__active {
  box-shadow: 0 20px 50px -28px oklch(0.63 0.2 350/.7);
}

.prc-19__card h3 {
  font-size: 14px;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: #a893b2;
}

.prc-19__price {
  font-size: 42px;
  font-weight: 800;
  letter-spacing: -.03em;
}

.prc-19__price small {
  font-size: 15px;
  font-weight: 600;
  color: #a893b2;
}

.prc-19__card ul {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 9px;
  font-size: 13.5px;
  color: #d3c6da;
  flex: 1;
  margin: 8px 0 18px;
}

.prc-19__card li::before {
  content: "✓";
  color: var(--accent);
  font-weight: 700;
  margin-right: 9px;
}

.prc-19__cta {
  text-align: center;
  text-decoration: none;
  font-weight: 700;
  font-size: 13.5px;
  padding: 12px;
  border-radius: 11px;
  border: 1px solid #43364a;
  color: #f4eef6;
  transition: border-color .2s;
}

.prc-19__cta:hover {
  border-color: var(--accent);
}

.prc-19__cta--hot {
  background: var(--accent);
  border-color: var(--accent);
  color: #fff;
}

.prc-19__cta:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

.prc-19__dots {
  display: flex;
  justify-content: center;
  gap: 10px;
  margin-top: 18px;
}

.prc-19__dots button {
  width: 9px;
  height: 9px;
  border-radius: 99px;
  border: none;
  background: #4a3d52;
  cursor: pointer;
  padding: 0;
  transition: background .3s,width .3s;
}

.prc-19__dots button[aria-selected=true] {
  background: var(--accent);
  width: 26px;
}

.prc-19__dots button:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

@media (min-width: 900px) {
  .prc-19__rail {
    overflow: visible;
    justify-content: center;
    padding: 12px 24px;
  }

  .prc-19__card {
    flex-basis: 280px;
    transform: none;
  }

  .prc-19__dots {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .prc-19__rail {
    scroll-behavior: auto;
  }

  .prc-19__card,
    .prc-19__dots button {
    transition-duration: .01s;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.prc-19');
  const rail = root.querySelector('#prc-19-rail');
  const cards = [...rail.querySelectorAll('.prc-19__card')];
  const dots = [...root.querySelectorAll('#prc-19-dots button')];
  const io = new IntersectionObserver(entries => {
    entries.forEach(e => {
      const i = cards.indexOf(e.target);
      if (e.isIntersecting) {
        cards.forEach((c, j) => c.classList.toggle('prc-19__active', j === i));
        dots.forEach((d, j) => d.setAttribute('aria-selected', j === i));
      }
    });
  }, { root: rail, threshold: 0.6 });
  cards.forEach(c => io.observe(c));
  dots.forEach((d, i) => d.addEventListener('click', () => {
    /* scroll the rail itself — never scrollIntoView, which can move the page */
    const target = cards[i].offsetLeft - (rail.clientWidth - cards[i].offsetWidth) / 2;
    rail.scrollTo({ left: target, behavior: matchMedia('(prefers-reduced-motion:reduce)').matches ? 'auto' : 'smooth' });
  }));
})();
```
