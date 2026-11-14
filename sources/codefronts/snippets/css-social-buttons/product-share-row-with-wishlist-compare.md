---
source: "codefronts"
url: "https://codefronts.com/snippets/css-social-buttons/product-share-row-with-wishlist-compare/"
title: "Product Share Row with Wishlist Compare"
section: "snippets"
category: "css-social-buttons"
category_name: "CSS Social Buttons"
description: "The secondary action row that sits under a product title: share, wishlist and compare."
has_js: "true"
---

Here's a working CSS Social Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Product Share Row with Wishlist Compare
Source: https://codefronts.com/snippets/css-social-buttons/product-share-row-with-wishlist-compare/

The secondary action row that sits under a product title: share, wishlist and compare. The heart fills and throws a small burst when saved, compare flips to a checked state, and both are single aria-pressed toggles rather than class juggling. Enough product chrome to read as a real page, no more.
## HTML
```html
<div class="soc-14">
  <div class="soc-14__stage">
    <div class="soc-14__card">
      <img class="soc-14__img" src="https://images.unsplash.com/photo-1501785888041-af3ef285b470?w=900&amp;q=70&amp;auto=format&amp;fit=crop" alt="Framed landscape print of a mountain ridge at sunrise" width="900" height="600" loading="lazy" decoding="async">
      <div class="soc-14__body">
        <p class="soc-14__brand">Northline Editions</p>
        <h2 class="soc-14__title">Alpine Ridge, archival print 50 × 70 cm</h2>
        <p class="soc-14__price"><strong>$148.00</strong><span>Free shipping · Ships in 2 days</span></p>
        <div class="soc-14__row">
          <a class="soc-14__act" href="https://example.com/share/product" target="_blank" rel="noopener">
            <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="17.5" cy="5.5" r="2.6"/><circle cx="6.5" cy="12" r="2.6"/><circle cx="17.5" cy="18.5" r="2.6"/><path d="m8.9 10.7 6.2-3.6"/><path d="m8.9 13.3 6.2 3.6"/></svg>
            <span>Share</span>
          </a>
          <button class="soc-14__act soc-14__heart" type="button" aria-pressed="false">
            <span class="soc-14__icons" aria-hidden="true">
              <svg class="soc-14__out" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19.6C9.2 17.8 4.6 14.6 4.6 10.8A3.9 3.9 0 0 1 12 8.6a3.9 3.9 0 0 1 7.4 2.2c0 3.8-4.6 7-7.4 8.8Z"/></svg>
              <svg class="soc-14__fill" viewBox="0 0 24 24" fill="currentColor"><path d="M12 19.6C9.2 17.8 4.6 14.6 4.6 10.8A3.9 3.9 0 0 1 12 8.6a3.9 3.9 0 0 1 7.4 2.2c0 3.8-4.6 7-7.4 8.8Z"/></svg>
            </span>
            <span class="soc-14__labels">
              <span class="soc-14__l-off">Wishlist</span>
              <span class="soc-14__l-on">Saved</span>
            </span>
          </button>
          <button class="soc-14__act soc-14__cmp" type="button" aria-pressed="false">
            <span class="soc-14__icons" aria-hidden="true">
              <svg class="soc-14__out" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 8.5h13"/><path d="m13.5 5 3.5 3.5-3.5 3.5"/><path d="M20 15.5H7"/><path d="M10.5 12 7 15.5 10.5 19"/></svg>
              <svg class="soc-14__fill" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12.6 4.4 4.4L19 7.4"/></svg>
            </span>
            <span class="soc-14__labels">
              <span class="soc-14__l-off">Compare</span>
              <span class="soc-14__l-on">Added</span>
            </span>
          </button>
        </div>
        <p class="soc-14__live" role="status" aria-live="polite"></p>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&display=swap');

.soc-14 {
  --bg: #f4f4f6;
  --surface: #ffffff;
  --fg: #0e0e12;
  --muted: #6a6a76;
  --line: #e5e5ea;
  --ring: #3d63ff;
  --like: #e0245e;
  --ok: #0e8a55;
  --sans: "Geist",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  color: var(--fg);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(50% 0 0)) {
  .soc-14 {
    --bg: oklch(96.4% .003 285);
    --surface: oklch(100% 0 0);
    --fg: oklch(17% .012 285);
    --muted: oklch(55% .012 285);
    --line: oklch(91.5% .005 285);
    --like: oklch(58% .21 12);
    --ok: oklch(56% .13 158);
  }
}

@media (prefers-color-scheme: dark) {
  .soc-14:not([data-theme="light"]) {
    --bg: #0a0a0d;
    --surface: #131318;
    --fg: #f2f2f5;
    --muted: #9a9aa6;
    --line: #26262e;
    --like: #ff6b8f;
    --ok: #3ecf8e;
  }
}

.soc-14[data-theme="dark"] {
  --bg: #0a0a0d;
  --surface: #131318;
  --fg: #f2f2f5;
  --muted: #9a9aa6;
  --line: #26262e;
  --like: #ff6b8f;
  --ok: #3ecf8e;
}

.soc-14,
.soc-14 *,
.soc-14 *::before,
.soc-14 *::after {
  box-sizing: border-box;
}

.soc-14__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,3.5rem);
}

.soc-14__card {
  inline-size: min(30rem,100%);
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 1.35rem;
  overflow: hidden;
  box-shadow: 0 1px 2px rgb(0 0 0/.04), 0 22px 48px -30px rgb(9 9 20/.45);
}

.soc-14__img {
  display: block;
  inline-size: 100%;
  block-size: 11rem;
  object-fit: cover;
  background: #dcdce2;
}

.soc-14__body {
  padding: clamp(1.25rem,4vw,1.75rem);
}

.soc-14__brand {
  margin: 0 0 .35rem;
  font-size: .72rem;
  font-weight: 600;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
}

.soc-14__title {
  margin: 0 0 .7rem;
  font-size: clamp(1.05rem,1rem + .8vw,1.3rem);
  font-weight: 600;
  line-height: 1.3;
  letter-spacing: -.02em;
  text-wrap: balance;
}

.soc-14__price {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  gap: .6rem;
  margin: 0 0 1.4rem;
  font-size: .82rem;
  color: var(--muted);
}

.soc-14__price strong {
  font-size: 1.15rem;
  color: var(--fg);
  font-variant-numeric: tabular-nums;
}

.soc-14__row {
  display: flex;
  flex-wrap: wrap;
  gap: .5rem;
}

.soc-14__act {
  position: relative;
  isolation: isolate;
  display: inline-flex;
  align-items: center;
  gap: .45rem;
  min-block-size: 2.875rem;
  padding: 0 .95rem;
  min-inline-size: 0;
  border: 1px solid var(--line);
  border-radius: .85rem;
  background: var(--surface);
  color: var(--fg);
  font: inherit;
  font-size: .88rem;
  font-weight: 550;
  text-decoration: none;
  cursor: pointer;
  transition: border-color .2s ease, color .2s ease, background-color .2s ease, translate .2s cubic-bezier(.16,1,.3,1);
}

.soc-14__act:hover {
  translate: 0 -2px;
  border-color: color-mix(in oklab,var(--fg) 30%,var(--line));
}

.soc-14__act:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}

.soc-14__act svg {
  inline-size: 1.1rem;
  block-size: 1.1rem;
}

.soc-14__icons {
  display: grid;
  inline-size: 1.1rem;
  block-size: 1.1rem;
}

.soc-14__icons svg {
  grid-area: 1/1;
  transition: opacity .18s ease, scale .28s cubic-bezier(.16,1,.3,1);
}

.soc-14__fill {
  opacity: 0;
  scale: .5;
}

.soc-14__labels {
  display: grid;
}

.soc-14__labels span {
  grid-area: 1/1;
  opacity: 0;
  white-space: nowrap;
  transition: opacity .16s ease;
}

.soc-14__act[aria-pressed="false"] .soc-14__l-off,
.soc-14__act:not([aria-pressed]) .soc-14__l-off {
  opacity: 1;
}

.soc-14__act[aria-pressed="true"] .soc-14__l-on {
  opacity: 1;
}

.soc-14__act[aria-pressed="true"] .soc-14__out {
  opacity: 0;
  scale: .5;
}

.soc-14__act[aria-pressed="true"] .soc-14__fill {
  opacity: 1;
  scale: 1;
}

.soc-14__heart[aria-pressed="true"] {
  color: var(--like);
  border-color: color-mix(in oklab,var(--like) 45%,var(--line));
  background: color-mix(in oklab,var(--like) 9%,var(--surface));
}

.soc-14__cmp[aria-pressed="true"] {
  color: var(--ok);
  border-color: color-mix(in oklab,var(--ok) 45%,var(--line));
  background: color-mix(in oklab,var(--ok) 9%,var(--surface));
}

.soc-14__heart::after {
  content: '';
  position: absolute;
  z-index: -1;
  inset-block-start: 50%;
  inset-inline-start: 1.4rem;
  inline-size: .5rem;
  block-size: .5rem;
  border-radius: 50%;
  translate: -50% -50%;
  pointer-events: none;
  opacity: 0;
}

.soc-14__heart[aria-pressed="true"]::after {
  animation: soc-14-burst .55s ease-out;
}

@keyframes soc-14-burst {
  0% {
    opacity: .9;
    scale: .2;
    box-shadow: 0 0 0 0 var(--like);
  }

  70% {
    opacity: .35;
  }

  100% {
    opacity: 0;
    scale: 2.6;
    box-shadow: 0 0 0 .45rem color-mix(in oklab,var(--like) 40%,transparent);
  }
}

.soc-14__live {
  margin: 1rem 0 0;
  min-block-size: 1.1rem;
  font-size: .8rem;
  color: var(--muted);
}

@media (prefers-reduced-motion: reduce) {
  .soc-14__act,
    .soc-14__icons svg,
    .soc-14__labels span {
    transition-duration: 1ms;
  }

  .soc-14__act:hover {
    translate: none;
  }

  .soc-14__heart[aria-pressed="true"]::after {
    animation: none;
  }
}

@media (forced-colors: active) {
  .soc-14__act {
    border: 1px solid ButtonText;
    color: ButtonText;
  }

  .soc-14__act[aria-pressed="true"] {
    background: Highlight;
    color: HighlightText;
  }

  .soc-14__heart::after {
    display: none;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.soc-14');
  if (!root) return;
  const live = root.querySelector('.soc-14__live');
  const say = {
    'soc-14__heart': ['Added to your wishlist.', 'Removed from your wishlist.'],
    'soc-14__cmp': ['Added to compare.', 'Removed from compare.']
  };
  root.querySelectorAll('button.soc-14__act').forEach((btn) => {
    btn.addEventListener('click', () => {
      const on = btn.getAttribute('aria-pressed') !== 'true';
      btn.setAttribute('aria-pressed', String(on));
      const key = btn.classList.contains('soc-14__heart') ? 'soc-14__heart' : 'soc-14__cmp';
      live.textContent = say[key][on ? 0 : 1];
    });
  });
})();
```
