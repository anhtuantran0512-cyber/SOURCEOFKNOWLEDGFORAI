---
source: "codefronts"
url: "https://codefronts.com/components/css-animated-cards/add-to-cart-success-morph/"
title: "Add-to-Cart Success Morph"
section: "components"
category: "css-animated-cards"
category_name: "CSS Animated Cards"
description: "The three-state commerce button done properly: idle → pending → confirmed, with the label collapsing into a spinner and the spinner blooming into a drawn…"
has_js: "true"
---

Here's a working CSS Animated Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Add-to-Cart Success Morph
Source: https://codefronts.com/components/css-animated-cards/add-to-cart-success-morph/

The three-state commerce button done properly: idle → pending → confirmed, with the label collapsing into a spinner and the spinner blooming into a drawn checkmark, then the cart badge counting up. One button element throughout, so focus is never lost and assistive tech follows the state change instead of a disappearing node.
## HTML
```html
<section class="ac-07" aria-label="Add to cart success morph demo">
  <div class="ac-07__stage">
    <div class="ac-07__bar">
      <span class="ac-07__brand">Northline Supply</span>
      <span class="ac-07__cart">
        <svg viewBox="0 0 24 24" width="19" height="19" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 6h15l-1.6 9H7.5L6 6z"/><path d="M6 6L5 3H2"/><circle cx="9" cy="20" r="1.4"/><circle cx="18" cy="20" r="1.4"/></svg>
        <b class="ac-07__badge" data-badge>0</b>
        <span class="ac-07__sr" data-cartsr>Cart is empty</span>
      </span>
    </div>
    <ul class="ac-07__grid" role="list">
      <li class="ac-07__card">
        <span class="ac-07__media"><img src="https://images.unsplash.com/photo-1542291026-7eec264c27ff?q=80&w=700&auto=format&fit=crop" alt="Charcoal running shoe" loading="lazy" decoding="async" width="700" height="700"></span>
        <div class="ac-07__body">
          <h3 class="ac-07__name">Trail Runner GTX</h3>
          <p class="ac-07__desc">Waterproof · 4 colourways</p>
          <div class="ac-07__foot">
            <span class="ac-07__price">$148</span>
            <button class="ac-07__btn" type="button" data-add data-state="idle">
              <span class="ac-07__label">Add to cart</span>
              <span class="ac-07__spin" aria-hidden="true"></span>
              <svg class="ac-07__check" viewBox="0 0 24 24" width="21" height="21" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.4 4.4L19 7.5"/></svg>
            </button>
          </div>
        </div>
      </li>
      <li class="ac-07__card">
        <span class="ac-07__media"><img src="https://images.unsplash.com/photo-1546868871-7041f2a55e12?q=80&w=700&auto=format&fit=crop" alt="Smartwatch with a woven strap" loading="lazy" decoding="async" width="700" height="700"></span>
        <div class="ac-07__body">
          <h3 class="ac-07__name">Pace Watch S2</h3>
          <p class="ac-07__desc">7-day battery · GPS</p>
          <div class="ac-07__foot">
            <span class="ac-07__price">$219</span>
            <button class="ac-07__btn" type="button" data-add data-state="idle">
              <span class="ac-07__label">Add to cart</span>
              <span class="ac-07__spin" aria-hidden="true"></span>
              <svg class="ac-07__check" viewBox="0 0 24 24" width="21" height="21" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.4 4.4L19 7.5"/></svg>
            </button>
          </div>
        </div>
      </li>
    </ul>
    <p class="ac-07__sr" role="status" aria-live="polite" data-status></p>
    <p class="ac-07__chip" aria-hidden="true">data-state machine · width + border-radius morph · stroke-dashoffset check draw · badge pop · focus preserved</p>
  </div>
</section>
```
## CSS
```css
.ac-07,
.ac-07 *,
.ac-07 *::before,
.ac-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ac-07 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --ac-07-bg: oklch(0.97 0.008 145);
  --ac-07-card: oklch(1 0 0);
  --ac-07-ink: oklch(0.22 0.02 160);
  --ac-07-mut: oklch(0.54 0.02 160);
  --ac-07-acc: oklch(0.44 0.11 165);
  --ac-07-ok: oklch(0.62 0.16 148);
  --ac-07-line: oklch(0.22 0.02 160/.12);
  background: var(--ac-07-bg);
  color: var(--ac-07-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.ac-07__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(14px,2.4vw,22px);
  padding: clamp(20px,5vw,58px);
}

.ac-07__bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
  width: min(100%,720px);
  padding: 12px 16px;
  border: 1px solid var(--ac-07-line);
  border-radius: 16px;
  background: var(--ac-07-card);
}

.ac-07__brand {
  font-size: 14px;
  font-weight: 680;
  letter-spacing: -.02em;
}

.ac-07__cart {
  position: relative;
  display: inline-grid;
  place-items: center;
  width: 44px;
  height: 44px;
  color: var(--ac-07-ink);
}

.ac-07__badge {
  position: absolute;
  top: 2px;
  right: 0;
  min-width: 20px;
  height: 20px;
  padding: 0 5px;
  display: grid;
  place-items: center;
  border-radius: 99px;
  background: var(--ac-07-acc);
  color: oklch(0.99 0 0);
  font-size: 11.5px;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
  transition: scale .3s cubic-bezier(.16,1,.3,1),opacity .2s;
  opacity: 0;
  scale: .5;
}

.ac-07__badge[data-on] {
  opacity: 1;
  scale: 1;
}

.ac-07__badge[data-pop] {
  animation: ac-07-pop .45s cubic-bezier(.16,1,.3,1);
}

@keyframes ac-07-pop {
  0% {
    scale: 1;
  }

  35% {
    scale: 1.45;
  }

  100% {
    scale: 1;
  }
}

.ac-07__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(280px,1fr));
  gap: 14px;
  width: min(100%,720px);
  list-style: none;
}

.ac-07__card {
  display: grid;
  grid-template-columns: 118px 1fr;
  gap: 0;
  border: 1px solid var(--ac-07-line);
  border-radius: 20px;
  overflow: hidden;
  background: var(--ac-07-card);
  box-shadow: 0 1px 2px oklch(0.22 0.02 160/.05),0 18px 34px -26px oklch(0.22 0.02 160/.6);
}

.ac-07__media {
  display: block;
  background: linear-gradient(135deg,oklch(0.88 0.03 160),oklch(0.82 0.05 130));
}

.ac-07__media img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.ac-07__body {
  display: grid;
  align-content: center;
  gap: 5px;
  padding: 16px;
}

.ac-07__name {
  font-size: 15.5px;
  font-weight: 650;
  letter-spacing: -.02em;
}

.ac-07__desc {
  font-size: 12.5px;
  color: var(--ac-07-mut);
}

.ac-07__foot {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  margin-top: 8px;
}

.ac-07__price {
  font-size: 17px;
  font-weight: 680;
  font-variant-numeric: tabular-nums;
  letter-spacing: -.02em;
}

.ac-07__btn {
  position: relative;
  display: grid;
  grid-template-columns: minmax(0,1fr);
  place-items: center;
  width: var(--ac-07-w,auto);
  min-width: 52px;
  height: 44px;
  padding: 0 var(--ac-07-p,20px);
  border: 0;
  border-radius: var(--ac-07-r,12px);
  background: var(--ac-07-acc);
  color: oklch(0.99 0 0);
  font-size: 13.5px;
  font-weight: 650;
  font-family: inherit;
  cursor: pointer;
  overflow: hidden;
  transition: width .38s cubic-bezier(.16,1,.3,1),padding .38s cubic-bezier(.16,1,.3,1),border-radius .38s cubic-bezier(.16,1,.3,1),background .3s,scale .12s;
}

.ac-07__btn:hover {
  background: color-mix(in oklch,var(--ac-07-acc) 88%,oklch(0 0 0));
}

.ac-07__btn:active {
  scale: .96;
}

.ac-07__btn:focus-visible {
  outline: 2px solid var(--ac-07-acc);
  outline-offset: 3px;
}

.ac-07__btn>* {
  grid-area: 1/1;
}

.ac-07__label {
  white-space: nowrap;
  transition: opacity .18s,scale .28s;
}

.ac-07__spin {
  width: 19px;
  height: 19px;
  flex: none;
  border-radius: 50%;
  border: 2.4px solid oklch(1 0 0/.32);
  border-top-color: oklch(1 0 0);
  opacity: 0;
  scale: .6;
  transition: opacity .18s,scale .28s;
}

.ac-07__check {
  width: 21px;
  height: 21px;
  flex: none;
  opacity: 0;
  scale: .6;
  transition: opacity .18s,scale .3s cubic-bezier(.16,1,.3,1);
}

.ac-07__check path {
  stroke-dasharray: 26;
  stroke-dashoffset: 26;
}

.ac-07__btn[data-state="pending"] {
  --ac-07-w: 52px;
  --ac-07-p: 0px;
  --ac-07-r: 99px;
}

.ac-07__btn[data-state="pending"] .ac-07__label {
  opacity: 0;
  scale: .8;
}

.ac-07__btn[data-state="pending"] .ac-07__spin {
  opacity: 1;
  scale: 1;
  animation: ac-07-spin .7s linear infinite;
}

.ac-07__btn[data-state="done"] {
  --ac-07-w: 52px;
  --ac-07-p: 0px;
  --ac-07-r: 99px;
  background: var(--ac-07-ok);
}

.ac-07__btn[data-state="done"] .ac-07__label {
  opacity: 0;
  scale: .8;
}

.ac-07__btn[data-state="done"] .ac-07__check {
  opacity: 1;
  scale: 1;
}

.ac-07__btn[data-state="done"] .ac-07__check path {
  animation: ac-07-draw .42s cubic-bezier(.6,0,.3,1) .05s forwards;
}

@keyframes ac-07-spin {
  to {
    rotate: 360deg;
  }
}

@keyframes ac-07-draw {
  to {
    stroke-dashoffset: 0;
  }
}

.ac-07__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.ac-07__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  line-height: 1.6;
  color: var(--ac-07-mut);
  padding: 8px 15px;
  border: 1px dashed var(--ac-07-line);
  border-radius: 99px;
  text-align: center;
  max-width: min(100%,700px);
}

@media (max-width: 420px) {
  .ac-07__card {
    grid-template-columns: 1fr;
  }

  .ac-07__media {
    aspect-ratio: 16/9;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ac-07 * {
    transition-duration: .01ms !important;
  }

  .ac-07__spin {
    animation-duration: 1.4s;
  }

  .ac-07__check path {
    stroke-dashoffset: 0;
    animation: none;
  }
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('.ac-07').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    const badge = root.querySelector('[data-badge]');
    const cartSr = root.querySelector('[data-cartsr]');
    const status = root.querySelector('[data-status]');
    let items = 0;

    root.querySelectorAll('[data-add]').forEach((btn) => {
      let revert = 0;
      btn.addEventListener('click', () => {
        if (btn.dataset.state !== 'idle') return;            // guard: no double-submit
        clearTimeout(revert);
        const name = btn.closest('.ac-07__card').querySelector('.ac-07__name').textContent;
        btn.dataset.state = 'pending';
        btn.setAttribute('aria-disabled', 'true');           // focusable, but inert
        status.textContent = 'Adding ' + name + '…';

        setTimeout(() => {
          btn.dataset.state = 'done';
          items += 1;
          badge.textContent = items;
          badge.dataset.on = '';
          badge.removeAttribute('data-pop');
          void badge.offsetWidth;                            // restart the pop keyframe
          badge.dataset.pop = '';
          cartSr.textContent = items + ' item' + (items === 1 ? '' : 's') + ' in cart';
          status.textContent = name + ' added. Cart has ' + items + ' item' + (items === 1 ? '' : 's') + '.';
          if (navigator.vibrate) navigator.vibrate(8);
          revert = setTimeout(() => { btn.dataset.state = 'idle'; btn.removeAttribute('aria-disabled'); }, 1600);
        }, 760);
      });
    });
  });
})();
```
