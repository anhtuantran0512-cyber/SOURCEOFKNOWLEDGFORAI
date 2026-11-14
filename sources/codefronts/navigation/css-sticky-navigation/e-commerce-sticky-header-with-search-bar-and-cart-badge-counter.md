---
source: "codefronts"
url: "https://codefronts.com/navigation/css-sticky-navigation/e-commerce-sticky-header-with-search-bar-and-cart-badge-counter/"
title: "E-Commerce Sticky Header with Search Bar and Cart Badge Counter"
section: "navigation"
category: "css-sticky-navigation"
category_name: "CSS Sticky Navigations"
description: "The storefront header carrying real work: a persistent search field, account entry and a cart badge that updates as items are added."
has_js: "true"
---

Here's a working CSS Sticky Navigation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: E-Commerce Sticky Header with Search Bar and Cart Badge Counter
Source: https://codefronts.com/navigation/css-sticky-navigation/e-commerce-sticky-header-with-search-bar-and-cart-badge-counter/

The storefront header carrying real work: a persistent search field, account entry and a cart badge that updates as items are added. The demo covers the parts that quietly matter in commerce — announcing the count change to screen reader users, keeping the badge readable at two and three digits, and building a search landmark without a submit-driven form.
## HTML
```html
<section class="sn-17" aria-label="E-commerce sticky header with search and cart demo">
    <header class="sn-17__bar">
      <a class="sn-17__brand" href="#sn-17-s1"><span class="sn-17__logo" aria-hidden="true"></span>Verdant</a>
      <div class="sn-17__search" role="search">
        <label class="sn-17__sr" for="sn-17-q">Search products</label>
        <svg class="sn-17__sicon" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><circle cx="9" cy="9" r="6" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="m13.5 13.5 3.5 3.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
        <input class="sn-17__input" id="sn-17-q" type="search" placeholder="Search plants, pots, tools…" autocomplete="off">
        <button class="sn-17__go" type="button" id="sn-17-go">Search</button>
      </div>
      <div class="sn-17__actions">
        <a class="sn-17__iconlink" href="#sn-17-s2" aria-label="Your account">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="8.5" r="3.6" stroke="currentColor" stroke-width="1.7"/><path d="M4.8 20a7.2 7.2 0 0 1 14.4 0" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
        </a>
        <a class="sn-17__iconlink sn-17__cart" href="#sn-17-s3" id="sn-17-cart" aria-label="Basket, 2 items">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4 6h2.2l2 10.2h9.4L20 8.6H7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/><circle cx="9.5" cy="19.5" r="1.5" fill="currentColor"/><circle cx="17" cy="19.5" r="1.5" fill="currentColor"/></svg>
          <span class="sn-17__badge" id="sn-17-badge" aria-hidden="true">2</span>
        </a>
      </div>
    </header>
    <p class="sn-17__live" id="sn-17-live" role="status" aria-live="polite"></p>
    <main>
      <section class="sn-17__grid" id="sn-17-s1">
        <article class="sn-17__card">
          <img class="sn-17__img" src="https://images.unsplash.com/photo-1485955900006-10f4d324d411?q=80&w=700&auto=format&fit=crop" alt="Potted monstera plant beside a window" width="700" height="700" loading="lazy" decoding="async">
          <h3 class="sn-17__ph">Monstera deliciosa</h3>
          <p class="sn-17__price">£38.00</p>
          <button class="sn-17__add" type="button" data-add>Add to basket</button>
        </article>
        <article class="sn-17__card">
          <img class="sn-17__img" src="https://images.unsplash.com/photo-1459156212016-c812468e2115?q=80&w=700&auto=format&fit=crop" alt="Terracotta plant pots stacked on a shelf" width="700" height="700" loading="lazy" decoding="async">
          <h3 class="sn-17__ph">Terracotta pot, 18cm</h3>
          <p class="sn-17__price">£14.50</p>
          <button class="sn-17__add" type="button" data-add>Add to basket</button>
        </article>
        <article class="sn-17__card">
          <img class="sn-17__img" src="https://images.unsplash.com/photo-1416879595882-3373a0480b5b?q=80&w=700&auto=format&fit=crop" alt="Garden tools laid out on soil" width="700" height="700" loading="lazy" decoding="async">
          <h3 class="sn-17__ph">Brass trowel set</h3>
          <p class="sn-17__price">£62.00</p>
          <button class="sn-17__add" type="button" data-add>Add to basket</button>
        </article>
      </section>
      <section class="sn-17__sec" id="sn-17-s2">
        <h3 class="sn-17__h">The count lives in the label</h3>
        <p class="sn-17__p">The badge is decoration. The number a screen reader hears is part of the link's accessible name, updated on every change and echoed through a polite live region.</p>
      </section>
      <section class="sn-17__sec" id="sn-17-s3">
        <h3 class="sn-17__h">minmax(0, 1fr) or it overflows</h3>
        <p class="sn-17__p">A plain <code>1fr</code> track will not shrink past its content. That single detail is why so many store headers push the basket off the screen on mobile.</p>
      </section>
    </main>
  <footer class="sn-17__pagefoot">
    <p class="sn-17__pagefootin">Sticky navigation pattern 17 of 25 · codefronts.com</p>
  </footer>
</section>
```
## CSS
```css
.sn-17 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--sn-17-bg);
  --sn-17-bg: oklch(0.955 0.014 145);
  --sn-17-surface: oklch(0.995 0.004 145);
  --sn-17-ink: oklch(0.24 0.03 150);
  --sn-17-mut: oklch(0.52 0.025 150);
  --sn-17-acc: oklch(0.5 0.13 152);
  --sn-17-line: oklch(0.24 0.03 150/.13);
  --sn-17-h: 68px;
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--sn-17-ink);
  -webkit-font-smoothing: antialiased;
}

.sn-17 *,
.sn-17 *::before,
.sn-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sn-17__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sn-17__bar {
  position: sticky;
  top: 0;
  z-index: 20;
  display: grid;
  grid-template-columns: auto minmax(0,1fr) auto;
  align-items: center;
  gap: clamp(10px,2vw,20px);
  min-height: var(--sn-17-h);
  padding: 0 clamp(14px,2.6vw,22px);
  background: color-mix(in oklch,var(--sn-17-surface) 90%,transparent);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border-bottom: 1px solid var(--sn-17-line);
}

.sn-17__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 15px;
  font-weight: 700;
  letter-spacing: -.025em;
  color: inherit;
  text-decoration: none;
  white-space: nowrap;
}

.sn-17__logo {
  width: 18px;
  height: 18px;
  border-radius: 50% 50% 50% 2px;
  rotate: -45deg;
  background: var(--sn-17-acc);
}

.sn-17__search {
  position: relative;
  display: flex;
  align-items: center;
  gap: 8px;
  min-width: 0;
  block-size: 42px;
  padding-inline: 12px 6px;
  border: 1px solid var(--sn-17-line);
  border-radius: 99px;
  background: oklch(0.24 0.03 150/.04);
  transition: border-color .2s ease,background .2s ease;
}

.sn-17__search:focus-within {
  border-color: var(--sn-17-acc);
  background: var(--sn-17-surface);
  box-shadow: 0 0 0 3px color-mix(in oklch,var(--sn-17-acc) 18%,transparent);
}

.sn-17__sicon {
  flex: none;
  inline-size: 17px;
  block-size: 17px;
  color: var(--sn-17-mut);
}

.sn-17__input {
  flex: 1;
  min-width: 0;
  border: 0;
  background: transparent;
  font-family: inherit;
  font-size: 14px;
  color: var(--sn-17-ink);
  outline: none;
}

.sn-17__input::placeholder {
  color: color-mix(in oklch,var(--sn-17-mut) 78%,transparent);
}

.sn-17__go {
  flex: none;
  min-height: 32px;
  padding: 0 15px;
  border: 0;
  border-radius: 99px;
  background: var(--sn-17-acc);
  color: oklch(1 0 0);
  font-family: inherit;
  font-size: 12.6px;
  font-weight: 660;
  cursor: pointer;
  transition: filter .18s ease;
}

.sn-17__go:hover {
  filter: brightness(1.07);
}

.sn-17__actions {
  display: flex;
  align-items: center;
  gap: 4px;
}

.sn-17__iconlink {
  position: relative;
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border-radius: 12px;
  color: var(--sn-17-mut);
  text-decoration: none;
  transition: color .18s ease,background .18s ease;
}

.sn-17__iconlink:hover {
  color: var(--sn-17-ink);
  background: oklch(0.24 0.03 150/.06);
}

.sn-17__iconlink svg {
  inline-size: 21px;
  block-size: 21px;
}

.sn-17__badge {
  position: absolute;
  inset-block-start: 5px;
  inset-inline-end: 4px;
  display: grid;
  place-items: center;
  min-inline-size: 18px;
  block-size: 18px;
  padding-inline: 5px;
  border-radius: 99px;
  background: var(--sn-17-acc);
  color: oklch(1 0 0);
  font-size: 10.5px;
  font-weight: 700;
  border: 2px solid var(--sn-17-surface);
}

.sn-17__badge[data-pop="true"] {
  animation: sn-17-pop .42s cubic-bezier(.32,.72,.3,1);
}

@keyframes sn-17-pop {
  0% {
    scale: 1;
  }

  38% {
    scale: 1.42;
  }

  100% {
    scale: 1;
  }
}

.sn-17__go:focus-visible,
.sn-17__iconlink:focus-visible,
.sn-17__brand:focus-visible,
.sn-17__add:focus-visible {
  outline: 2px solid var(--sn-17-acc);
  outline-offset: 2px;
}

.sn-17__live {
  padding: 0 clamp(16px,3vw,26px);
  font-size: 12.5px;
  color: var(--sn-17-acc);
  min-height: 22px;
  display: grid;
  align-items: center;
}

.sn-17__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(210px,1fr));
  gap: clamp(14px,2.4vw,22px);
  padding: clamp(16px,3vw,28px) clamp(16px,3vw,26px) clamp(26px,4vw,40px);
}

.sn-17__card {
  display: grid;
  gap: 7px;
  padding: 12px;
  border: 1px solid var(--sn-17-line);
  border-radius: 14px;
  background: var(--sn-17-surface);
  transition: box-shadow .24s ease,translate .24s ease;
}

.sn-17__card:hover {
  translate: 0 -3px;
  box-shadow: 0 18px 34px -22px oklch(0.24 0.03 150/.5);
}

.sn-17__img {
  inline-size: 100%;
  aspect-ratio: 1;
  object-fit: cover;
  border-radius: 10px;
  background: linear-gradient(150deg,oklch(0.82 0.06 150),oklch(0.7 0.05 130));
}

.sn-17__ph {
  margin-block-start: 4px;
  font-size: 14.6px;
  font-weight: 660;
  letter-spacing: -.015em;
}

.sn-17__price {
  font-size: 13.6px;
  color: var(--sn-17-mut);
}

.sn-17__add {
  min-height: 40px;
  margin-block-start: 4px;
  border: 1px solid var(--sn-17-line);
  border-radius: 10px;
  background: transparent;
  font-family: inherit;
  font-size: 13.2px;
  font-weight: 640;
  color: var(--sn-17-ink);
  cursor: pointer;
  transition: background .18s ease,color .18s ease,border-color .18s ease;
}

.sn-17__add:hover {
  background: var(--sn-17-acc);
  border-color: var(--sn-17-acc);
  color: oklch(1 0 0);
}

.sn-17__sec {
  scroll-margin-top: var(--sn-17-h);
  display: grid;
  gap: 10px;
  align-content: center;
  min-height: 66svh;
  padding: clamp(22px,4vw,44px);
  border-top: 1px solid var(--sn-17-line);
}

.sn-17__h {
  font-size: clamp(18px,2.5vw,25px);
  line-height: 1.18;
  letter-spacing: -.025em;
  font-weight: 690;
  text-wrap: balance;
}

.sn-17__p {
  max-width: 54ch;
  font-size: 14.8px;
  line-height: 1.64;
  color: var(--sn-17-mut);
  text-wrap: pretty;
}

.sn-17__p code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .85em;
  background: oklch(0.24 0.03 150/.07);
  padding: 2px 6px;
  border-radius: 5px;
}

@media (max-width: 640px) {
  .sn-17__go {
    display: none;
  }

  .sn-17__search {
    padding-inline: 12px;
  }
}

@media (max-width: 460px) {
  .sn-17__brand span:not(.sn-17__logo) {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sn-17__badge[data-pop="true"] {
    animation: none;
  }

  .sn-17 * {
    transition-duration: .01ms !important;
  }
}
/* ── full-page mode: the demo IS the document, so sticky pins against the real viewport ── */

:root:has(.sn-17) {
  scroll-behavior: smooth;
  scroll-padding-top: calc(var(--sn-17-h) + 10px);
}

@media (prefers-reduced-motion: reduce) {
  :root:has(.sn-17) {
    scroll-behavior: auto;
  }
}

.sn-17__bar,
.sn-17__barin {
  padding-inline: max(clamp(16px,3vw,26px),calc((100% - 1280px)/2));
}

.sn-17__sec {
  padding-inline: max(clamp(22px,5vw,44px),calc((100% - 1120px)/2));
}

.sn-17__pagefoot {
  display: grid;
  place-items: center;
  padding: clamp(44px,9vh,110px) 24px;
  border-top: 1px solid var(--sn-17-line);
}

.sn-17__pagefootin {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  letter-spacing: .06em;
  color: var(--sn-17-mut);
  text-align: center;
}

.sn-17__intro-title,
.sn-17__intro-sub {
  text-wrap: balance;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.sn-17');
  if (!root || root.dataset.snWired) return;
  root.dataset.snWired = '1';
  const cart = root.querySelector('#sn-17-cart');
  const badge = root.querySelector('#sn-17-badge');
  const live = root.querySelector('#sn-17-live');
  const input = root.querySelector('#sn-17-q');
  let count = 2;
  const render = (name) => {
    badge.textContent = count > 99 ? '99+' : count;
    cart.setAttribute('aria-label', 'Basket, ' + count + (count === 1 ? ' item' : ' items'));
    live.textContent = name + ' added — basket now has ' + count + (count === 1 ? ' item' : ' items');
    badge.dataset.pop = 'true';
    setTimeout(() => badge.removeAttribute('data-pop'), 450);
  };
  root.querySelectorAll('[data-add]').forEach((btn) => btn.addEventListener('click', () => {
    count += 1;
    render(btn.closest('.sn-17__card').querySelector('.sn-17__ph').textContent);
  }));
  const search = () => {
    const q = input.value.trim();
    live.textContent = q ? 'Searching for “' + q + '”…' : 'Enter a search term to continue';
  };
  root.querySelector('#sn-17-go').addEventListener('click', search);
  input.addEventListener('keydown', (e) => { if (e.key === 'Enter') { e.preventDefault(); search(); } });
})();
```
