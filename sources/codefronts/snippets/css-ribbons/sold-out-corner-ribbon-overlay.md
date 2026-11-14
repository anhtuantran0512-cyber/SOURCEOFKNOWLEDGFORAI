---
source: "codefronts"
url: "https://codefronts.com/snippets/css-ribbons/sold-out-corner-ribbon-overlay/"
title: "Sold Out Corner Ribbon Overlay"
section: "snippets"
category: "css-ribbons"
category_name: "CSS Ribbons"
description: "Sold out is a state, not a sticker."
has_js: "true"
---

Here's a working CSS Ribbon from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sold Out Corner Ribbon Overlay
Source: https://codefronts.com/snippets/css-ribbons/sold-out-corner-ribbon-overlay/

Sold out is a state, not a sticker. Toggle the checkbox and one :has() selector re-styles the entire card at once: the photo desaturates and dims, the price greys, the button disables, and a frosted translucent band slides across the corner with backdrop-filter so the product stays visible underneath — the shopper can still see what they missed. Zero JavaScript; the checkbox is the state machine.
## HTML
```html
<section class="rib-02" aria-label="Corner sold out ribbon demo">
  <div class="rib-02__stage">
    <article class="rib-02__card">
      <div class="rib-02__media">
        <img class="rib-02__img" alt="Pair of tan leather sneakers on a pale background" loading="lazy" decoding="async" width="640" height="480"
          src="https://images.unsplash.com/photo-1600185365483-26d7a4cc7519?q=80&w=800&auto=format&fit=crop">
        <div class="rib-02__ribbon" aria-hidden="true"><span class="rib-02__band"><span class="rib-02__label">SOLD OUT</span></span></div>
      </div>
      <div class="rib-02__body">
        <p class="rib-02__brand">Kestrel Supply Co.</p>
        <h3 class="rib-02__name">Ridge Low Leather</h3>
        <p class="rib-02__price"><span class="rib-02__now">$164</span><span class="rib-02__size">UK 9 · Tan</span></p>
        <p class="rib-02__status" role="status">Sold out — no stock in this size</p>
        <div class="rib-02__actions">
          <button class="rib-02__cta" type="button">Add to bag</button>
          <button class="rib-02__alt" type="button">Notify me when back</button>
        </div>
        <label class="rib-02__toggle"><input class="rib-02__state" type="checkbox" checked><span class="rib-02__track" aria-hidden="true"><span class="rib-02__thumb"></span></span><span class="rib-02__togtxt">Simulate sold out</span></label>
      </div>
    </article>
    <p class="rib-02__chip" aria-hidden="true">:has(:checked) state switch · backdrop-filter blur+saturate · grayscale veil</p>
  </div>
</section>
```
## CSS
```css
.rib-02,
.rib-02 *,
.rib-02 *::before,
.rib-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.rib-02 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --rib-02-bg: #eceef1;
  --rib-02-bg: oklch(0.94 0.006 255);
  --rib-02-card: #fff;
  --rib-02-card: oklch(1 0 0);
  --rib-02-ink: #1d2024;
  --rib-02-ink: oklch(0.24 0.012 255);
  --rib-02-mut: #71767e;
  --rib-02-mut: oklch(0.58 0.012 255);
  --rib-02-acc: #2f6bd8;
  --rib-02-acc: oklch(0.56 0.17 258);
  --rib-02-size: clamp(108px,27vw,152px);
  --rib-02-band: 36px;
  --rib-02-offset: 32px;
  --rib-02-len: calc(var(--rib-02-size) * 1.415 + var(--rib-02-band) * 2);
  --rib-02-r: 24px;
  background: var(--rib-02-bg);
  color: var(--rib-02-ink);
  font-family: system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.rib-02__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(16px,3vw,24px);
  padding: clamp(18px,5vw,56px);
}

.rib-02__card {
  position: relative;
  width: min(100%,382px);
  background: var(--rib-02-card);
  border-radius: var(--rib-02-r);
  box-shadow: 0 1px 2px oklch(0 0 0/.05),0 20px 44px -18px oklch(0.3 0.03 255/.38);
}

.rib-02__media {
  position: relative;
  aspect-ratio: 4/3;
  border-radius: var(--rib-02-r) var(--rib-02-r) 0 0;
  clip-path: inset(0 round var(--rib-02-r) var(--rib-02-r) 0 0);
  background: linear-gradient(140deg,oklch(0.9 0.02 255),oklch(0.84 0.03 250));
}

.rib-02__img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: filter .5s cubic-bezier(.16,1,.3,1),scale .6s cubic-bezier(.16,1,.3,1);
}

.rib-02__ribbon {
  position: absolute;
  inset-block-start: 0;
  inset-inline-end: 0;
  inline-size: var(--rib-02-size);
  aspect-ratio: 1;
  overflow: hidden;
  pointer-events: none;
  z-index: 2;
}

.rib-02__band {
  position: absolute;
  inset-block-start: var(--rib-02-offset);
  inset-inline-end: calc((var(--rib-02-len) - var(--rib-02-size)) / -2);
  inline-size: var(--rib-02-len);
  display: grid;
  place-items: center;
  rotate: 45deg;
  background: oklch(0.25 0.01 260/.82);
  background: oklch(0.25 0.01 260/.62);
  -webkit-backdrop-filter: blur(10px) saturate(.5);
  backdrop-filter: blur(10px) saturate(.5);
  border-block: 1px solid oklch(1 0 0/.22);
  box-shadow: inset 0 9px 14px -11px oklch(1 0 0/.4),inset 0 -10px 16px -11px oklch(0 0 0/.6);
  opacity: 0;
  translate: 22px -22px;
  transition: opacity .38s cubic-bezier(.16,1,.3,1),translate .48s cubic-bezier(.16,1,.3,1);
}

.rib-02__label {
  padding: 10px 14px;
  color: oklch(0.99 0 0);
  font-size: 13px;
  font-weight: 750;
  letter-spacing: .16em;
  line-height: 1;
  white-space: nowrap;
}

.rib-02__body {
  display: grid;
  gap: 8px;
  padding: clamp(18px,4vw,24px);
}

.rib-02__brand {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .15em;
  text-transform: uppercase;
  color: var(--rib-02-mut);
}

.rib-02__name {
  font-size: 21px;
  font-weight: 640;
  letter-spacing: -.022em;
  transition: color .35s;
}

.rib-02__price {
  display: flex;
  align-items: baseline;
  gap: 10px;
  font-variant-numeric: tabular-nums;
}

.rib-02__now {
  font-size: 23px;
  font-weight: 750;
  letter-spacing: -.03em;
  transition: color .35s,text-decoration-color .35s;
  text-decoration: line-through;
  text-decoration-color: transparent;
}

.rib-02__size {
  font-size: 13px;
  color: var(--rib-02-mut);
}

.rib-02__status {
  font-size: 13px;
  font-weight: 600;
  color: color-mix(in oklch,oklch(0.6 0.16 150) 82%,black);
}

.rib-02__actions {
  display: grid;
  gap: 8px;
  margin-top: 6px;
}

.rib-02__cta,
.rib-02__alt {
  min-height: 48px;
  border-radius: 13px;
  font: inherit;
  font-size: 15px;
  font-weight: 640;
  cursor: pointer;
  transition: opacity .3s,background .25s,translate .2s,border-color .25s;
}

.rib-02__cta {
  border: 0;
  background: var(--rib-02-ink);
  color: oklch(0.99 0 0);
}

.rib-02__cta:hover {
  translate: 0 -1px;
  background: color-mix(in oklch,var(--rib-02-ink) 85%,var(--rib-02-acc));
}

.rib-02__alt {
  display: none;
  border: 1.5px solid color-mix(in oklch,var(--rib-02-ink) 22%,transparent);
  background: transparent;
  color: var(--rib-02-ink);
}

.rib-02__alt:hover {
  border-color: var(--rib-02-acc);
  color: var(--rib-02-acc);
}

.rib-02__cta:focus-visible,
.rib-02__alt:focus-visible,
.rib-02__state:focus-visible+.rib-02__track {
  outline: 3px solid var(--rib-02-acc);
  outline-offset: 3px;
}

.rib-02__toggle {
  display: flex;
  align-items: center;
  gap: 11px;
  margin-top: 6px;
  padding: 10px 2px;
  min-height: 44px;
  cursor: pointer;
  font-size: 13px;
  color: var(--rib-02-mut);
  user-select: none;
}

.rib-02__state {
  position: absolute;
  opacity: 0;
  width: 1px;
  height: 1px;
}

.rib-02__track {
  flex: none;
  width: 42px;
  height: 25px;
  border-radius: 99px;
  background: oklch(0 0 0/.16);
  display: flex;
  align-items: center;
  padding: 3px;
  transition: background .28s cubic-bezier(.16,1,.3,1);
}

.rib-02__thumb {
  width: 19px;
  height: 19px;
  border-radius: 50%;
  background: oklch(1 0 0);
  box-shadow: 0 1px 3px oklch(0 0 0/.3);
  transition: translate .28s cubic-bezier(.16,1,.3,1);
}

.rib-02__card:has(.rib-02__state:checked) .rib-02__track {
  background: var(--rib-02-acc);
}

.rib-02__card:has(.rib-02__state:checked) .rib-02__thumb {
  translate: 17px 0;
}

.rib-02__card:has(.rib-02__state:checked) .rib-02__band {
  opacity: 1;
  translate: 0 0;
}

.rib-02__card:has(.rib-02__state:checked) .rib-02__img {
  filter: grayscale(.88) brightness(.74) contrast(1.05);
}

.rib-02__card:has(.rib-02__state:checked) .rib-02__name {
  color: var(--rib-02-mut);
}

.rib-02__card:has(.rib-02__state:checked) .rib-02__now {
  color: var(--rib-02-mut);
  text-decoration-color: currentColor;
}

.rib-02__card:has(.rib-02__state:checked) .rib-02__status {
  color: var(--rib-02-mut);
}

.rib-02__card:has(.rib-02__state:checked) .rib-02__cta {
  display: none;
}

.rib-02__card:has(.rib-02__state:checked) .rib-02__alt {
  display: block;
}

.rib-02__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--rib-02-mut);
  padding: 8px 15px;
  border: 1px solid oklch(0 0 0/.12);
  border-radius: 99px;
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .rib-02 * {
    transition-duration: .01ms !important;
    animation: none !important;
  }
}
```

## JavaScript
```js
(() => {
  // Two lines of progressive enhancement: keep the visible status text in sync with the
  // :has() driven visual state, so assistive tech is told what sighted users can see.
  document.querySelectorAll('.rib-02__card').forEach((card) => {
    if (card.dataset.wired) return;
    card.dataset.wired = '1';
    const box = card.querySelector('.rib-02__state');
    const status = card.querySelector('.rib-02__status');
    box.addEventListener('change', () => {
      status.textContent = box.checked
        ? 'Sold out — no stock in this size'
        : 'In stock — 6 pairs left';
    });
  });
})();
```
