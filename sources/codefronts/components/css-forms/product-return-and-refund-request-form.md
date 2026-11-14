---
source: "codefronts"
url: "https://codefronts.com/components/css-forms/product-return-and-refund-request-form/"
title: "Product Return and Refund Request Form"
section: "components"
category: "css-forms"
category_name: "CSS Forms"
description: "A self-serve returns portal: select items from the order as checkbox cards with product photos, and each selected card expands to ask its own quantity and…"
has_js: "true"
---

Here's a working CSS Form from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Product Return and Refund Request Form
Source: https://codefronts.com/components/css-forms/product-return-and-refund-request-form/

A self-serve returns portal: select items from the order as checkbox cards with product photos, and each selected card expands to ask its own quantity and reason (pure :has()); final-sale items are genuinely disabled with an explanation; choose refund to the original card or store credit with a 10% bonus; pick drop-off or courier pickup; and watch an itemised refund total update live before generating a return label.
## HTML
```html
<div class="frm-14">
  <button type="button" class="frm-14__theme" data-theme-toggle aria-label="Dark mode" aria-pressed="false" title="Switch to dark mode"><svg class="frm-14__moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5Z"/></svg><svg class="frm-14__sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg></button>
  <div class="frm-14__stage">
    <div class="frm-14__card" role="form" aria-labelledby="frm-14-title">
      <header class="frm-14__head">
        <div><p class="frm-14__eyebrow">Returns</p><h2 id="frm-14-title">Start a return</h2></div>
        <dl class="frm-14__order"><div><dt>Order</dt><dd>#NW-48213</dd></div><div><dt>Delivered</dt><dd>28 Sep 2026</dd></div><div><dt>Return by</dt><dd>28 Oct 2026</dd></div></dl>
      </header>
      <fieldset class="frm-14__items">
        <legend>Which items are you returning?</legend>
        <div class="frm-14__item">
          <label class="frm-14__top"><input type="checkbox" class="frm-14__pick" data-price="129" data-max="1"><img src="https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=200&h=200&fit=crop&auto=format&q=70" width="72" height="72" alt="" loading="lazy" decoding="async"><span><b>Velocity Runner</b><small>Crimson · UK 9</small></span><em>$129.00</em><i class="frm-14__box" aria-hidden="true"></i></label>
          <div class="frm-14__more">
            <div class="frm-14__f"><label for="frm-14-r1">Reason</label><select id="frm-14-r1" class="frm-14__reason"><option value="">Select a reason</option><option>Too small</option><option>Too large</option><option>Not as described</option><option>Damaged or defective</option><option>Changed my mind</option></select></div>
          </div>
        </div>
        <div class="frm-14__item">
          <label class="frm-14__top"><input type="checkbox" class="frm-14__pick" data-price="34" data-max="3"><img src="https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=200&h=200&fit=crop&auto=format&q=70" width="72" height="72" alt="" loading="lazy" decoding="async"><span><b>Everyday Organic Tee</b><small>White · M · ×3</small></span><em>$34.00 ea</em><i class="frm-14__box" aria-hidden="true"></i></label>
          <div class="frm-14__more">
            <div class="frm-14__f"><label for="frm-14-q2">Quantity</label><select id="frm-14-q2" class="frm-14__qty"><option>1</option><option>2</option><option selected>3</option></select></div>
            <div class="frm-14__f"><label for="frm-14-r2">Reason</label><select id="frm-14-r2" class="frm-14__reason"><option value="">Select a reason</option><option>Too small</option><option>Too large</option><option>Not as described</option><option>Damaged or defective</option><option>Changed my mind</option></select></div>
          </div>
        </div>
        <div class="frm-14__item">
          <label class="frm-14__top"><input type="checkbox" class="frm-14__pick" data-price="89" data-max="1"><img src="https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=200&h=200&fit=crop&auto=format&q=70" width="72" height="72" alt="" loading="lazy" decoding="async"><span><b>Commuter Pack 22L</b><small>Slate</small></span><em>$89.00</em><i class="frm-14__box" aria-hidden="true"></i></label>
          <div class="frm-14__more">
            <div class="frm-14__f"><label for="frm-14-r3">Reason</label><select id="frm-14-r3" class="frm-14__reason"><option value="">Select a reason</option><option>Not as described</option><option>Damaged or defective</option><option>Changed my mind</option></select></div>
          </div>
        </div>
        <div class="frm-14__item is-final">
          <label class="frm-14__top"><input type="checkbox" class="frm-14__pick" disabled aria-describedby="frm-14-final"><span class="frm-14__noimg" aria-hidden="true">Gift card</span><span><b>Digital Gift Card</b><small id="frm-14-final">Final sale — not returnable</small></span><em>$50.00</em><i class="frm-14__box" aria-hidden="true"></i></label>
        </div>
      </fieldset>
      <div class="frm-14__two">
        <fieldset class="frm-14__opts"><legend>Refund to</legend>
          <label><input type="radio" name="frm-14-m" value="card" checked><span><b>Original payment</b><small>Visa •••• 4242 · 3–5 days after we receive it</small></span></label>
          <label><input type="radio" name="frm-14-m" value="credit"><span><b>Store credit <mark>+10% bonus</mark></b><small>Instant, as soon as you drop it off</small></span></label>
        </fieldset>
        <fieldset class="frm-14__opts"><legend>Return method</legend>
          <label><input type="radio" name="frm-14-s" value="0" checked><span><b>Drop-off · Free</b><small>Any UPS Access Point. Show a QR code — no printer.</small></span></label>
          <label><input type="radio" name="frm-14-s" value="5.95"><span><b>Courier pickup · $5.95</b><small>We'll collect from your door. Deducted from refund.</small></span></label>
        </fieldset>
      </div>
      <div class="frm-14__sum">
        <dl>
          <div><dt>Items (<span class="frm-14__cnt">0</span>)</dt><dd data-k="items">$0.00</dd></div>
          <div class="frm-14__bonus"><dt>Store credit bonus</dt><dd data-k="bonus">$0.00</dd></div>
          <div class="frm-14__fee"><dt>Return shipping</dt><dd data-k="ship">Free</dd></div>
          <div class="frm-14__tot"><dt>Estimated refund</dt><dd data-k="total">$0.00</dd></div>
        </dl>
        <button type="button" class="frm-14__go">Get return label</button>
      </div>
      <p class="frm-14__status" role="status"></p>
      <div class="frm-14__label" hidden><span class="frm-14__qr" aria-hidden="true"></span><div><b>Return RMA-90231 created</b><p>Show this QR at the drop-off point. We've also emailed it to you.</p></div></div>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Urbanist:wght@400;500;600;700;800&display=swap');

.frm-14 {
  --bg: #f2f2f0;
  --card: #ffffff;
  --ink: #111110;
  --muted: #6b6b66;
  --line: #e6e6e2;
  --soft: #f8f8f6;
  --hot: #ff5a1f;
  --ok: #16a34a;
  --sans: "Urbanist",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --ease: cubic-bezier(.16,1,.3,1);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@media (prefers-color-scheme: dark) {
  .frm-14:not([data-theme="light"]) {
    --bg: #0d0d0c;
    --card: #161615;
    --ink: #f5f5f2;
    --muted: #a3a39c;
    --line: #2a2a27;
    --soft: #1d1d1b;
    --hot: #ff7a45;
    --ok: #4ade80;
  }
}

.frm-14[data-theme="dark"] {
  --bg: #0d0d0c;
  --card: #161615;
  --ink: #f5f5f2;
  --muted: #a3a39c;
  --line: #2a2a27;
  --soft: #1d1d1b;
  --hot: #ff7a45;
  --ok: #4ade80;
}

.frm-14,
.frm-14 *,
.frm-14 *::before,
.frm-14 *::after {
  box-sizing: border-box;
}

.frm-14__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3.5rem);
}

.frm-14__card {
  width: 100%;
  max-width: 46rem;
  display: grid;
  gap: 1.5rem;
  padding: clamp(1.25rem,4vw,2.5rem);
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 1.5rem;
  box-shadow: 0 30px 70px -40px rgba(0,0,0,.35);
}

.frm-14__head {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: flex-end;
  gap: 1rem;
}

.frm-14__eyebrow {
  margin: 0 0 .2rem;
  font-size: .8rem;
  font-weight: 700;
  color: var(--hot);
  letter-spacing: .06em;
  text-transform: uppercase;
}

.frm-14 h2 {
  margin: 0;
  font-size: clamp(1.7rem,4vw,2.2rem);
  font-weight: 800;
  letter-spacing: -.035em;
}

.frm-14__order {
  display: flex;
  gap: 1.25rem;
  margin: 0;
}

.frm-14__order dt {
  font-size: .72rem;
  color: var(--muted);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: .06em;
}

.frm-14__order dd {
  margin: .1rem 0 0;
  font-weight: 700;
  font-size: .92rem;
}

.frm-14 fieldset {
  border: 0;
  margin: 0;
  padding: 0;
  min-width: 0;
}

.frm-14 legend {
  padding: 0;
  margin-bottom: .7rem;
  font-size: .95rem;
  font-weight: 700;
}

.frm-14__items {
  display: grid;
  gap: .6rem;
}

.frm-14__item {
  border: 1.5px solid var(--line);
  border-radius: 1.1rem;
  background: var(--card);
  transition: border-color .25s, box-shadow .3s var(--ease);
  overflow: hidden;
}

.frm-14__top {
  position: relative;
  display: grid;
  grid-template-columns: auto 1fr auto auto;
  align-items: center;
  gap: .95rem;
  padding: .75rem 1rem .75rem .75rem;
  cursor: pointer;
}

.frm-14__pick {
  position: absolute;
  inset: 0;
  opacity: 0;
  margin: 0;
  cursor: pointer;
}

.frm-14__top img,
.frm-14__noimg {
  width: 4.25rem;
  height: 4.25rem;
  border-radius: .8rem;
  object-fit: cover;
  background: var(--soft);
}

.frm-14__noimg {
  display: grid;
  place-items: center;
  font-size: .7rem;
  font-weight: 700;
  color: var(--muted);
  border: 1px dashed var(--line);
  text-align: center;
}

.frm-14__top b {
  display: block;
  font-weight: 700;
}

.frm-14__top small {
  display: block;
  color: var(--muted);
  font-size: .85rem;
  margin-top: .1rem;
}

.frm-14__top em {
  font-style: normal;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
}

.frm-14__box {
  width: 1.5rem;
  height: 1.5rem;
  border-radius: .45rem;
  border: 1.5px solid var(--line);
  display: grid;
  place-items: center;
  transition: all .25s var(--ease);
}

.frm-14__box::after {
  content: '';
  width: .7rem;
  height: .4rem;
  border-left: 2.5px solid #fff;
  border-bottom: 2.5px solid #fff;
  rotate: -45deg;
  translate: 0 -1px;
  scale: 0;
  transition: scale .3s var(--ease);
}

.frm-14__item:hover:not(.is-final) {
  border-color: color-mix(in oklab,var(--ink) 30%,var(--line));
}

.frm-14__item:has(.frm-14__pick:checked) {
  border-color: var(--ink);
  box-shadow: 0 14px 30px -20px rgba(0,0,0,.45);
}

.frm-14__item:has(.frm-14__pick:checked) .frm-14__box {
  background: var(--hot);
  border-color: var(--hot);
}

.frm-14__item:has(.frm-14__pick:checked) .frm-14__box::after {
  scale: 1;
}

.frm-14__item:has(.frm-14__pick:focus-visible) {
  outline: 2px solid var(--hot);
  outline-offset: 3px;
}

.frm-14__item.is-final {
  background: var(--soft);
}

.frm-14__item.is-final .frm-14__top {
  cursor: not-allowed;
  color: var(--muted);
}

.frm-14__item.is-final small {
  color: var(--hot);
  font-weight: 600;
}

.frm-14__item.is-final .frm-14__box {
  border-style: dashed;
}

.frm-14__more {
  display: none;
  grid-template-columns: repeat(auto-fit,minmax(min(100%,11rem),1fr));
  gap: .8rem;
  padding: 0 1rem 1rem;
  margin-left: 5.95rem;
}

.frm-14__item:has(.frm-14__pick:checked) .frm-14__more {
  display: grid;
  animation: frm-14-in .35s var(--ease);
}

@keyframes frm-14-in {
  from {
    opacity: 0;
    translate: 0 -6px;
  }
}

@media (max-width: 34rem) {
  .frm-14__more {
    margin-left: 0;
  }

  .frm-14__top {
    grid-template-columns: auto 1fr auto;
  }

  .frm-14__top em {
    grid-column: 2;
    grid-row: 2;
  }
}

.frm-14__f {
  display: grid;
  gap: .35rem;
}

.frm-14__f label {
  font-size: .8rem;
  font-weight: 700;
}

.frm-14 select {
  width: 100%;
  min-height: 2.8rem;
  padding: .5rem .8rem;
  border-radius: .7rem;
  border: 1px solid var(--line);
  background: var(--soft);
  color: var(--ink);
  font: inherit;
  font-size: .95rem;
  cursor: pointer;
}

.frm-14 select:focus-visible {
  outline: none;
  border-color: var(--ink);
  box-shadow: 0 0 0 3px color-mix(in oklab,var(--hot) 25%,transparent);
}

.frm-14 select.is-missing {
  border-color: var(--hot);
}

.frm-14__two {
  display: grid;
  gap: 1.25rem;
  grid-template-columns: repeat(auto-fit,minmax(min(100%,17rem),1fr));
}

.frm-14__opts {
  display: grid;
  gap: .5rem;
  align-content: start;
}

.frm-14__opts label {
  position: relative;
}

.frm-14__opts input {
  position: absolute;
  inset: 0;
  opacity: 0;
  margin: 0;
  cursor: pointer;
}

.frm-14__opts span {
  display: grid;
  gap: .15rem;
  padding: .85rem 1rem .85rem 2.6rem;
  border: 1.5px solid var(--line);
  border-radius: 1rem;
  position: relative;
  transition: border-color .2s, background .2s;
}

.frm-14__opts span::before {
  content: '';
  position: absolute;
  left: 1rem;
  top: 1rem;
  width: 1rem;
  height: 1rem;
  border-radius: 50%;
  border: 1.5px solid var(--muted);
  transition: border .25s var(--ease);
}

.frm-14__opts b {
  font-weight: 700;
  font-size: .95rem;
}

.frm-14__opts small {
  color: var(--muted);
  font-size: .82rem;
  line-height: 1.35;
}

.frm-14__opts mark {
  background: color-mix(in oklab,var(--hot) 18%,transparent);
  color: var(--hot);
  padding: .05rem .35rem;
  border-radius: .3rem;
  font-size: .78rem;
  margin-left: .25rem;
}

.frm-14__opts input:checked + span {
  border-color: var(--ink);
  background: var(--soft);
}

.frm-14__opts input:checked + span::before {
  border: 5px solid var(--ink);
}

.frm-14__opts input:focus-visible + span {
  outline: 2px solid var(--hot);
  outline-offset: 2px;
}

.frm-14__sum {
  display: grid;
  grid-template-columns: minmax(0,1fr) auto;
  gap: 1.25rem;
  align-items: end;
  padding: 1.25rem;
  border-radius: 1.1rem;
  background: var(--ink);
  color: var(--card);
}

@media (max-width: 34rem) {
  .frm-14__sum {
    grid-template-columns: 1fr;
  }
}

.frm-14__sum dl {
  margin: 0;
  display: grid;
  gap: .35rem;
}

.frm-14__sum dl div {
  display: flex;
  justify-content: space-between;
  gap: 1rem;
  font-size: .9rem;
}

.frm-14__sum dt {
  opacity: .7;
}

.frm-14__sum dd {
  margin: 0;
  font-variant-numeric: tabular-nums;
  font-weight: 600;
}

.frm-14:not(:has([value="credit"]:checked)) .frm-14__bonus {
  display: none;
}

.frm-14__bonus dd {
  color: #fdba74;
}

.frm-14__tot {
  padding-top: .5rem;
  margin-top: .25rem;
  border-top: 1px solid color-mix(in oklab,var(--card) 18%,transparent);
  font-size: 1.15rem !important;
}

.frm-14__tot dt {
  opacity: 1 !important;
  font-weight: 700;
}

.frm-14__tot dd {
  font-weight: 800 !important;
}

.frm-14__go {
  min-height: 3.2rem;
  padding: 0 1.5rem;
  border: 0;
  border-radius: .9rem;
  cursor: pointer;
  font: inherit;
  font-weight: 800;
  font-size: 1rem;
  color: #111;
  background: var(--hot);
  transition: translate .2s var(--ease), filter .2s;
}

.frm-14__go:hover {
  translate: 0 -2px;
  filter: brightness(1.06);
}

.frm-14__go:focus-visible {
  outline: 2px solid var(--card);
  outline-offset: 3px;
}

.frm-14__status {
  margin: -.75rem 0 0;
  font-weight: 600;
  color: var(--hot);
}

.frm-14__status:empty {
  display: none;
}

.frm-14__label {
  display: flex;
  gap: 1rem;
  align-items: center;
  padding: 1rem;
  border-radius: 1.1rem;
  border: 1.5px dashed var(--ok);
  animation: frm-14-in .45s var(--ease);
}

.frm-14__label[hidden] {
  display: none;
}

.frm-14__label b {
  color: var(--ok);
}

.frm-14__label p {
  margin: .2rem 0 0;
  color: var(--muted);
  font-size: .9rem;
}

.frm-14__qr {
  flex: none;
  width: 4.5rem;
  height: 4.5rem;
  border-radius: .4rem;
  background: repeating-conic-gradient(var(--ink) 0 25%, var(--card) 0 50%) 0 0 / .9rem .9rem;
  box-shadow: 0 0 0 .3rem var(--card), 0 0 0 calc(.3rem + 1px) var(--line);
}

@media (prefers-reduced-motion: reduce) {
  .frm-14 * {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .frm-14__item:has(.frm-14__pick:checked) {
    outline: 2px solid Highlight;
  }

  .frm-14__sum {
    background: Canvas;
    color: CanvasText;
    border: 1px solid CanvasText;
  }

  .frm-14__go {
    border: 1px solid ButtonText;
  }
}
/* Theme toggle — top-right of the demo. Ink-relative colours, so it suits light and dark. */

.frm-14 {
  position: relative;
  padding-top: 72px;
  box-sizing: border-box;
}

.frm-14__theme {
  position: absolute;
  top: 16px;
  right: 16px;
  z-index: 20;
  display: grid;
  place-items: center;
  width: 44px;
  height: 44px;
  padding: 0;
  border-radius: 999px;
  border: 1px solid color-mix(in srgb, currentColor 22%, transparent);
  background: color-mix(in srgb, currentColor 8%, transparent);
  color: inherit;
  cursor: pointer;
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
  transition: background-color .2s, transform .2s;
}

.frm-14__theme:hover {
  background: color-mix(in srgb, currentColor 14%, transparent);
}

.frm-14__theme:active {
  transform: scale(.94);
}

.frm-14__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.frm-14__theme svg {
  width: 20px;
  height: 20px;
  fill: none;
  stroke: currentColor;
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.frm-14__theme .frm-14__sun,
.frm-14__theme[aria-pressed="true"] .frm-14__moon {
  display: none;
}

.frm-14__theme[aria-pressed="true"] .frm-14__sun {
  display: block;
}

@media (prefers-reduced-motion: reduce) {
  .frm-14__theme {
    transition: none;
  }
}

@media (forced-colors: active) {
  .frm-14__theme {
    border-color: ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }
}
```

## JavaScript
```js
// Theme toggle (top-right): flips data-theme on the root and mirrors outside changes.
(() => {
  document.querySelectorAll('.frm-14').forEach((root) => {
    const btn = root.querySelector(':scope > [data-theme-toggle]');
    if (!btn || btn.dataset.wired) return;
    btn.dataset.wired = '1';
    const mq = matchMedia('(prefers-color-scheme: dark)');
    const isDark = () => (root.dataset.theme ? root.dataset.theme === 'dark' : mq.matches);
    const sync = () => {
      const dark = isDark();
      btn.setAttribute('aria-pressed', String(dark));
      btn.title = dark ? 'Switch to light mode' : 'Switch to dark mode';
    };
    btn.addEventListener('click', () => { root.dataset.theme = isDark() ? 'light' : 'dark'; sync(); });
    mq.addEventListener('change', sync);
    new MutationObserver(sync).observe(root, { attributes: true, attributeFilter: ['data-theme'] });
    sync();
  });
})();
(() => {
  const root = document.querySelector('.frm-14');
  if (!root) return;
  const $ = (s) => root.querySelector(s);
  const BONUS = 0.10, fmt = new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' });
  const qtyOf = (c) => { const q = c.closest('.frm-14__item').querySelector('.frm-14__qty'); return q ? Number(q.value) : 1; };
  const calc = () => {
    const picks = [...root.querySelectorAll('.frm-14__pick:checked')];
    const items = picks.reduce((a, c) => a + Number(c.dataset.price) * qtyOf(c), 0);
    const count = picks.reduce((a, c) => a + qtyOf(c), 0);
    const credit = $('[name="frm-14-m"]:checked').value === 'credit', ship = Number($('[name="frm-14-s"]:checked').value);
    const bonus = credit ? items * BONUS : 0, total = Math.max(0, items + bonus - (items ? ship : 0));
    $('.frm-14__cnt').textContent = count;
    $('[data-k="items"]').textContent = fmt.format(items);
    $('[data-k="bonus"]').textContent = '+' + fmt.format(bonus);
    $('[data-k="ship"]').textContent = ship ? '−' + fmt.format(ship) : 'Free';
    $('[data-k="total"]').textContent = fmt.format(total);
  };
  root.addEventListener('change', (e) => { if (e.target.classList.contains('frm-14__reason')) e.target.classList.remove('is-missing'); calc(); });
  $('.frm-14__go').addEventListener('click', () => {
    const status = $('.frm-14__status'), picks = [...root.querySelectorAll('.frm-14__pick:checked')];
    if (!picks.length) { status.textContent = 'Select at least one item to return.'; root.querySelector('.frm-14__pick:not(:disabled)').focus(); return; }
    const missing = picks.map((c) => c.closest('.frm-14__item').querySelector('.frm-14__reason')).find((s) => !s.value);
    if (missing) { missing.classList.add('is-missing'); status.textContent = 'Please choose a reason for each selected item.'; missing.focus(); return; }
    status.textContent = '';
    const label = $('.frm-14__label'); label.hidden = false;
    $('.frm-14__go').textContent = 'Label ready';
  });
  calc();
})();
```
