---
source: "codefronts"
url: "https://codefronts.com/components/css-pricing-tables/skeleton-loading-states/"
title: "Skeleton Loading States"
section: "components"
category: "css-pricing-tables"
category_name: "CSS Pricing Tables"
description: "The perceived-performance pattern for API-priced products: cards render instantly as shimmering gray skeletons in the exact final geometry, then real prices…"
has_js: "true"
---

Here's a working CSS Pricing Table from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Skeleton Loading States
Source: https://codefronts.com/components/css-pricing-tables/skeleton-loading-states/

The perceived-performance pattern for API-priced products: cards render instantly as shimmering gray skeletons in the exact final geometry, then real prices swap in with a soft crossfade when the (simulated) pricing API responds — zero layout shift from first paint to loaded.
## HTML
```html
<section class="prc-21" aria-label="Pricing cards with loading states">
  <header class="prc-21__head">
    <h2>Live pricing</h2>
    <button class="prc-21__reload" id="prc-21-reload">↻ Replay loading</button>
  </header>
  <div class="prc-21__grid" id="prc-21-grid" aria-busy="true">
    <article class="prc-21__card" data-plan="0">
      <span class="prc-21__slot prc-21__slot--name"><span class="prc-21__bone prc-21__bone--name"></span><b class="prc-21__real"></b></span>
      <span class="prc-21__slot prc-21__slot--price"><span class="prc-21__bone prc-21__bone--price"></span><b class="prc-21__real"></b></span>
      <span class="prc-21__slot prc-21__slot--feat"><span class="prc-21__bone prc-21__bone--l1"></span><span class="prc-21__bone prc-21__bone--l2"></span><span class="prc-21__bone prc-21__bone--l3"></span><b class="prc-21__real"></b></span>
      <a href="#" class="prc-21__cta"><span class="prc-21__bone prc-21__bone--btn"></span><b class="prc-21__real"></b></a>
    </article>
    <article class="prc-21__card prc-21__card--hot" data-plan="1">
      <span class="prc-21__slot prc-21__slot--name"><span class="prc-21__bone prc-21__bone--name"></span><b class="prc-21__real"></b></span>
      <span class="prc-21__slot prc-21__slot--price"><span class="prc-21__bone prc-21__bone--price"></span><b class="prc-21__real"></b></span>
      <span class="prc-21__slot prc-21__slot--feat"><span class="prc-21__bone prc-21__bone--l1"></span><span class="prc-21__bone prc-21__bone--l2"></span><span class="prc-21__bone prc-21__bone--l3"></span><b class="prc-21__real"></b></span>
      <a href="#" class="prc-21__cta"><span class="prc-21__bone prc-21__bone--btn"></span><b class="prc-21__real"></b></a>
    </article>
    <article class="prc-21__card" data-plan="2">
      <span class="prc-21__slot prc-21__slot--name"><span class="prc-21__bone prc-21__bone--name"></span><b class="prc-21__real"></b></span>
      <span class="prc-21__slot prc-21__slot--price"><span class="prc-21__bone prc-21__bone--price"></span><b class="prc-21__real"></b></span>
      <span class="prc-21__slot prc-21__slot--feat"><span class="prc-21__bone prc-21__bone--l1"></span><span class="prc-21__bone prc-21__bone--l2"></span><span class="prc-21__bone prc-21__bone--l3"></span><b class="prc-21__real"></b></span>
      <a href="#" class="prc-21__cta"><span class="prc-21__bone prc-21__bone--btn"></span><b class="prc-21__real"></b></a>
    </article>
  </div>
</section>
```
## CSS
```css
.prc-21,
.prc-21 *,
.prc-21 *::before,
.prc-21 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.prc-21 {
  --accent: oklch(0.6 0.18 265);
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #f5f6f9;
  color: #191c26;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 56px 24px;
}

.prc-21__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: min(880px,100%);
  margin: 0 auto 30px;
}

.prc-21__head h2 {
  font-size: clamp(24px,3.6vw,34px);
  font-weight: 800;
  letter-spacing: -.02em;
}

.prc-21__reload {
  font: inherit;
  font-size: 13px;
  font-weight: 700;
  color: var(--accent);
  background: none;
  border: 1.5px solid oklch(0.6 0.18 265/.35);
  border-radius: 99px;
  padding: 9px 16px;
  cursor: pointer;
  transition: background .2s;
}

.prc-21__reload:hover {
  background: oklch(0.6 0.18 265/.08);
}

.prc-21__reload:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

.prc-21__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(220px,1fr));
  gap: 18px;
  width: min(880px,100%);
  margin: 0 auto;
}

.prc-21__card {
  background: #fff;
  border: 1px solid #e3e6ef;
  border-radius: 18px;
  padding: 28px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.prc-21__card--hot {
  border-color: var(--accent);
}

.prc-21__slot {
  position: relative;
  display: block;
}

.prc-21__slot--name {
  height: 18px;
}

.prc-21__slot--price {
  height: 50px;
}

.prc-21__slot--feat {
  height: 88px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.prc-21__bone {
  position: relative;
  display: block;
  background: #e8eaf2;
  border-radius: 6px;
  overflow: hidden;
  transition: opacity .4s;
}

.prc-21__bone::after {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(100deg,transparent 20%,rgba(255,255,255,.85) 50%,transparent 80%);
  transform: translateX(-100%);
  animation: prc-21-sheen 1.4s ease-in-out infinite;
}

@keyframes prc-21-sheen {
  to {
    transform: translateX(100%);
  }
}

.prc-21__bone--name {
  width: 56%;
  height: 16px;
}

.prc-21__bone--price {
  width: 44%;
  height: 44px;
  border-radius: 9px;
}

.prc-21__bone--l1 {
  width: 88%;
  height: 13px;
}

.prc-21__bone--l2 {
  width: 72%;
  height: 13px;
}

.prc-21__bone--l3 {
  width: 80%;
  height: 13px;
}

.prc-21__bone--btn {
  width: 100%;
  height: 100%;
  border-radius: 11px;
  position: absolute;
  inset: 0;
}

.prc-21__real {
  position: absolute;
  inset: 0;
  opacity: 0;
  transition: opacity .45s .1s;
  font-style: normal;
}

.prc-21__ready .prc-21__bone {
  opacity: 0;
}

.prc-21__ready .prc-21__real {
  opacity: 1;
}

.prc-21__slot--name .prc-21__real {
  font-size: 14px;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: #68708a;
}

.prc-21__slot--price .prc-21__real {
  font-size: 40px;
  font-weight: 800;
  letter-spacing: -.03em;
  line-height: 1.2;
}

.prc-21__slot--price .prc-21__real small {
  font-size: 15px;
  color: #8a92ac;
}

.prc-21__slot--feat .prc-21__real {
  font-size: 13.5px;
  color: #4c5470;
  line-height: 1.9;
  font-weight: 400;
}

.prc-21__cta {
  position: relative;
  display: block;
  height: 45px;
  text-align: center;
  text-decoration: none;
  border-radius: 11px;
}

.prc-21__cta .prc-21__real {
  display: grid;
  place-items: center;
  font-size: 13.5px;
  font-weight: 700;
  border: 1.5px solid #dfe2ee;
  border-radius: 11px;
  color: #191c26;
}

.prc-21__card--hot .prc-21__cta .prc-21__real {
  background: var(--accent);
  border-color: var(--accent);
  color: #fff;
}

.prc-21__cta:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .prc-21__bone::after {
    animation: none;
  }

  .prc-21__bone,
    .prc-21__real {
    transition-duration: .01s;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.prc-21');
  const grid = root.querySelector('#prc-21-grid');
  const DELAY = 1800;
  const PLANS = [
    { name: 'Metered', price: '$0.04<small>/1k calls</small>', feats: 'Pay as you go<br>No minimums<br>Community support', cta: 'Start free' },
    { name: 'Reserved', price: '$149<small>/mo</small>', feats: '5M calls included<br>Burst capacity<br>Priority support', cta: 'Choose Reserved' },
    { name: 'Dedicated', price: '$890<small>/mo</small>', feats: 'Isolated cluster<br>Custom limits<br>Solutions engineer', cta: 'Contact sales' },
  ];
  function load() {
    grid.classList.remove('prc-21__ready');
    grid.setAttribute('aria-busy', 'true');
    setTimeout(() => {
      grid.querySelectorAll('.prc-21__card').forEach(card => {
        const p = PLANS[+card.dataset.plan];
        const [name, price, feats, cta] = card.querySelectorAll('.prc-21__real');
        name.textContent = p.name;
        price.innerHTML = p.price;
        feats.innerHTML = p.feats;
        cta.textContent = p.cta;
      });
      grid.setAttribute('aria-busy', 'false');
      grid.classList.add('prc-21__ready');
    }, DELAY);
  }
  root.querySelector('#prc-21-reload').addEventListener('click', load);
  load();
})();
```
