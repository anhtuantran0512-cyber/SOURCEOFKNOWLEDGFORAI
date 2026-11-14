---
source: "codefronts"
url: "https://codefronts.com/motion/css-scroll-progress-bar/e-commerce-checkout-step-progress-on-scroll/"
title: "E-Commerce Checkout Step Progress on Scroll"
section: "motion"
category: "css-scroll-progress-bar"
category_name: "CSS Scroll Progress Bar"
description: "Single-page checkouts convert better than multi-page wizards, but they lose the wizard's most valuable feature: a visible sense of how much is left."
has_js: "true"
---

Here's a working CSS Scroll Progress Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: E-Commerce Checkout Step Progress on Scroll
Source: https://codefronts.com/motion/css-scroll-progress-bar/e-commerce-checkout-step-progress-on-scroll/

Single-page checkouts convert better than multi-page wizards, but they lose the wizard's most valuable feature: a visible sense of how much is left. Binding a classic four-step stepper to scroll position restores it. Each step activates as its panel reaches the viewport, the connecting line fills continuously, and nothing about the form state is involved.
## HTML
```html
<section class="sp-12" aria-label="E-commerce checkout step progress demo">
  <header class="sp-12__bar">
    <a class="sp-12__brand" href="#sp-12-p1"><span class="sp-12__logo" aria-hidden="true"></span>Northbound</a>
    <p class="sp-12__secure"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M6 10V8a6 6 0 0 1 12 0v2M5 10h14v10H5z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"></path></svg>Secure checkout</p>
  </header>
  <nav class="sp-12__steps" aria-label="Checkout progress" id="sp-12-steps">
    <ol class="sp-12__list">
      <li class="sp-12__step" data-step="1" aria-current="step"><span class="sp-12__node"><span class="sp-12__num">1</span></span><span class="sp-12__slab">Bag</span></li>
      <li class="sp-12__step" data-step="2"><span class="sp-12__node"><span class="sp-12__num">2</span></span><span class="sp-12__slab">Delivery</span></li>
      <li class="sp-12__step" data-step="3"><span class="sp-12__node"><span class="sp-12__num">3</span></span><span class="sp-12__slab">Payment</span></li>
      <li class="sp-12__step" data-step="4"><span class="sp-12__node"><span class="sp-12__num">4</span></span><span class="sp-12__slab">Review</span></li>
    </ol>
    <div class="sp-12__connector" aria-hidden="true"><i class="sp-12__cfill"></i></div>
  </nav>
  <div class="sp-12__layout" id="sp-12-flow">
    <div class="sp-12__panels">
      <section class="sp-12__panel" id="sp-12-p1" data-step="1">
        <p class="sp-12__pk">Step 1</p>
        <h3 class="sp-12__ph">Your bag</h3>
        <ul class="sp-12__items">
          <li class="sp-12__item"><img class="sp-12__thumb" src="https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&amp;fit=crop&amp;w=400&amp;q=70" alt="Field Watch 38 in stainless steel" loading="lazy" decoding="async"><div class="sp-12__idet"><p class="sp-12__iname">Field Watch 38</p><p class="sp-12__imeta">Steel · 20mm strap</p></div><p class="sp-12__iprice">£240.00</p></li>
          <li class="sp-12__item"><img class="sp-12__thumb" src="https://images.unsplash.com/photo-1560343090-f0409e92791a?auto=format&amp;fit=crop&amp;w=400&amp;q=70" alt="Day Satchel in tan leather" loading="lazy" decoding="async"><div class="sp-12__idet"><p class="sp-12__iname">Day Satchel</p><p class="sp-12__imeta">Tan · 14in laptop</p></div><p class="sp-12__iprice">£310.00</p></li>
        </ul>
        <p class="sp-12__note">Free returns within 30 days. Scroll on to continue — the stepper follows you.</p>
      </section>
      <section class="sp-12__panel" id="sp-12-p2" data-step="2">
        <p class="sp-12__pk">Step 2</p>
        <h3 class="sp-12__ph">Delivery address</h3>
        <div class="sp-12__grid">
          <label class="sp-12__field"><span class="sp-12__flab">Full name</span><input class="sp-12__input" type="text" autocomplete="name" placeholder="Alex Whitfield"></label>
          <label class="sp-12__field"><span class="sp-12__flab">Postcode</span><input class="sp-12__input" type="text" inputmode="text" autocomplete="postal-code" placeholder="SW1A 1AA"></label>
          <label class="sp-12__field sp-12__field--wide"><span class="sp-12__flab">Address line 1</span><input class="sp-12__input" type="text" autocomplete="address-line1" placeholder="14 Rosebery Avenue"></label>
        </div>
        <div class="sp-12__choices" role="radiogroup" aria-label="Delivery speed">
          <button class="sp-12__choice" type="button" role="radio" aria-checked="true"><span class="sp-12__cname2">Standard</span><span class="sp-12__cmeta">3–5 days · Free</span></button>
          <button class="sp-12__choice" type="button" role="radio" aria-checked="false"><span class="sp-12__cname2">Express</span><span class="sp-12__cmeta">Next day · £6.00</span></button>
        </div>
      </section>
      <section class="sp-12__panel" id="sp-12-p3" data-step="3">
        <p class="sp-12__pk">Step 3</p>
        <h3 class="sp-12__ph">Payment</h3>
        <div class="sp-12__grid">
          <label class="sp-12__field sp-12__field--wide"><span class="sp-12__flab">Card number</span><input class="sp-12__input" type="text" inputmode="numeric" autocomplete="cc-number" placeholder="4242 4242 4242 4242"></label>
          <label class="sp-12__field"><span class="sp-12__flab">Expiry</span><input class="sp-12__input" type="text" inputmode="numeric" autocomplete="cc-exp" placeholder="09 / 29"></label>
          <label class="sp-12__field"><span class="sp-12__flab">Security code</span><input class="sp-12__input" type="text" inputmode="numeric" autocomplete="cc-csc" placeholder="123"></label>
        </div>
        <p class="sp-12__note">Autocomplete tokens are not decoration — they are what makes mobile autofill work, and they measurably reduce abandonment.</p>
      </section>
      <section class="sp-12__panel" id="sp-12-p4" data-step="4">
        <p class="sp-12__pk">Step 4</p>
        <h3 class="sp-12__ph">Review and pay</h3>
        <p class="sp-12__note">Everything above stays visible. A single-page checkout only wins if the customer can still see where they are — which is the whole point of binding the stepper to scroll.</p>
        <button class="sp-12__pay" type="button" id="sp-12-pay">Pay £550.00</button>
        <p class="sp-12__trust"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 3l7 3v6c0 4.5-3 7.5-7 9-4-1.5-7-4.5-7-9V6z" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"></path></svg>Encrypted end to end · 30-day returns · No card details stored</p>
        <p class="sp-12__status" id="sp-12-status" role="status"></p>
      </section>
    </div>
    <aside class="sp-12__summary" aria-label="Order summary">
      <p class="sp-12__stitle">Order summary</p>
      <dl class="sp-12__rows">
        <div class="sp-12__row"><dt>Subtotal</dt><dd>£550.00</dd></div>
        <div class="sp-12__row"><dt>Delivery</dt><dd>Free</dd></div>
        <div class="sp-12__row sp-12__row--total"><dt>Total</dt><dd>£550.00</dd></div>
      </dl>
      <p class="sp-12__snote">VAT included. Prices in GBP.</p>
    </aside>
  </div>
  <footer class="sp-12__pagefoot"><p class="sp-12__pagefootin">Scroll progress pattern 12 of 18 · codefronts.com</p></footer>
</section>
```
## CSS
```css
.sp-12 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--sp-12-bg);
  --sp-12-bg: oklch(0.975 0.006 230);
  --sp-12-surface: oklch(1 0 0);
  --sp-12-ink: oklch(0.2 0.02 250);
  --sp-12-mut: oklch(0.53 0.016 250);
  --sp-12-acc: oklch(0.52 0.15 250);
  --sp-12-ok: oklch(0.6 0.14 155);
  --sp-12-line: oklch(0.2 0.02 250/.12);
  --sp-12-p: 0;
  timeline-scope: --sp-12-s1,--sp-12-s2,--sp-12-s3,--sp-12-s4,--sp-12-flow;
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--sp-12-ink);
  -webkit-font-smoothing: antialiased;
}

.sp-12 *,
.sp-12 *::before,
.sp-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sp-12__bar {
  display: flex;
  align-items: center;
  gap: 14px;
  min-block-size: 60px;
  border-block-end: 1px solid var(--sp-12-line);
  background: var(--sp-12-surface);
}

.sp-12__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 15.5px;
  font-weight: 730;
  letter-spacing: -.025em;
  color: inherit;
  text-decoration: none;
}

.sp-12__logo {
  inline-size: 18px;
  block-size: 18px;
  border-radius: 5px;
  background: linear-gradient(140deg,var(--sp-12-acc),oklch(0.65 0.14 210));
}

.sp-12__secure {
  margin-inline-start: auto;
  display: flex;
  align-items: center;
  gap: 7px;
  font-size: 12.4px;
  font-weight: 600;
  color: var(--sp-12-ok);
}

.sp-12__secure svg {
  inline-size: 15px;
  block-size: 15px;
}

.sp-12__steps {
  position: sticky;
  inset-block-start: 0;
  z-index: 45;
  display: grid;
  gap: 0;
  padding-block: 14px 0;
  background: color-mix(in oklch,var(--sp-12-surface) 88%,transparent);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border-block-end: 1px solid var(--sp-12-line);
}

.sp-12__list {
  list-style: none;
  display: grid;
  grid-template-columns: repeat(4,1fr);
  gap: 0;
}

.sp-12__step {
  display: grid;
  justify-items: center;
  gap: 7px;
}

.sp-12__node {
  display: grid;
  place-items: center;
  inline-size: 30px;
  block-size: 30px;
  border-radius: 50%;
  border: 2px solid color-mix(in oklch,var(--sp-12-ink) 18%,transparent);
  background: var(--sp-12-surface);
  color: var(--sp-12-mut);
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12.5px;
  font-weight: 700;
  transition: border-color .25s ease,color .25s ease,background .25s ease,scale .25s ease;
}

.sp-12__slab {
  font-size: 12px;
  font-weight: 620;
  color: var(--sp-12-mut);
  transition: color .25s ease;
}

.sp-12__step[aria-current="step"] .sp-12__node,
.sp-12__step[data-on="true"] .sp-12__node {
  border-color: var(--sp-12-acc);
  background: var(--sp-12-acc);
  color: oklch(1 0 0);
  scale: 1.1;
}

.sp-12__step[aria-current="step"] .sp-12__slab,
.sp-12__step[data-on="true"] .sp-12__slab {
  color: var(--sp-12-ink);
}

@supports (animation-timeline: view()) {
  .sp-12__node,
    .sp-12__slab {
    animation: sp-12-on steps(1,end) both;
    animation-range: cover 22% cover 78%;
  }

  .sp-12__step[data-step="1"] .sp-12__node,
    .sp-12__step[data-step="1"] .sp-12__slab {
    animation-timeline: --sp-12-s1;
  }

  .sp-12__step[data-step="2"] .sp-12__node,
    .sp-12__step[data-step="2"] .sp-12__slab {
    animation-timeline: --sp-12-s2;
  }

  .sp-12__step[data-step="3"] .sp-12__node,
    .sp-12__step[data-step="3"] .sp-12__slab {
    animation-timeline: --sp-12-s3;
  }

  .sp-12__step[data-step="4"] .sp-12__node,
    .sp-12__step[data-step="4"] .sp-12__slab {
    animation-timeline: --sp-12-s4;
  }

  .sp-12__panel[data-step="1"] {
    view-timeline-name: --sp-12-s1;
  }

  .sp-12__panel[data-step="2"] {
    view-timeline-name: --sp-12-s2;
  }

  .sp-12__panel[data-step="3"] {
    view-timeline-name: --sp-12-s3;
  }

  .sp-12__panel[data-step="4"] {
    view-timeline-name: --sp-12-s4;
  }

  .sp-12__panels {
    scroll-timeline-name: --sp-12-flow;
    scroll-timeline-axis: block;
  }

  .sp-12__cfill {
    transform: scaleX(0);
    animation: sp-12-fill linear both;
    animation-timeline: --sp-12-flow;
  }
}

@keyframes sp-12-on {
  0% {
  }

  1%,
    100% {
    border-color: var(--sp-12-acc);
    background: var(--sp-12-acc);
    color: oklch(1 0 0);
    scale: 1.1;
  }
}

@keyframes sp-12-fill {
  from {
    transform: scaleX(0);
  }

  to {
    transform: scaleX(1);
  }
}

.sp-12__connector {
  position: relative;
  block-size: 3px;
  margin: 10px 12.5% 0;
  background: color-mix(in oklch,var(--sp-12-ink) 10%,transparent);
  border-radius: 99px;
  overflow: hidden;
}

.sp-12__cfill {
  display: block;
  block-size: 100%;
  transform-origin: 0 50%;
  transform: scaleX(var(--sp-12-p));
  background: linear-gradient(90deg,var(--sp-12-acc),var(--sp-12-ok));
}

.sp-12__layout {
  display: grid;
  grid-template-columns: minmax(0,1fr) minmax(240px,300px);
  gap: clamp(18px,3vw,40px);
  align-items: start;
  padding-block: clamp(22px,4vh,44px) clamp(30px,6vh,64px);
}

.sp-12__panels {
  display: grid;
  gap: clamp(14px,2vw,22px);
}

.sp-12__panel {
  scroll-margin-top: 120px;
  display: grid;
  gap: 14px;
  align-content: start;
  min-block-size: 70svh;
  padding: clamp(18px,3vw,28px);
  border: 1px solid var(--sp-12-line);
  border-radius: 18px;
  background: var(--sp-12-surface);
}

.sp-12__pk {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 10.5px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--sp-12-acc);
}

.sp-12__ph {
  font-size: clamp(19px,2.4vw,25px);
  line-height: 1.14;
  letter-spacing: -.028em;
  font-weight: 700;
}

.sp-12__items {
  list-style: none;
  display: grid;
  gap: 12px;
}

.sp-12__item {
  display: flex;
  align-items: center;
  gap: 13px;
  padding-block-end: 12px;
  border-block-end: 1px solid var(--sp-12-line);
}

.sp-12__item:last-child {
  border-block-end: 0;
  padding-block-end: 0;
}

.sp-12__thumb {
  inline-size: 58px;
  block-size: 58px;
  border-radius: 12px;
  object-fit: cover;
  flex: none;
  background: linear-gradient(135deg,oklch(0.8 0.03 250),oklch(0.65 0.04 220));
}

.sp-12__idet {
  display: grid;
  gap: 3px;
  min-inline-size: 0;
}

.sp-12__iname {
  font-size: 14.4px;
  font-weight: 650;
}

.sp-12__imeta {
  font-size: 12.4px;
  color: var(--sp-12-mut);
}

.sp-12__iprice {
  margin-inline-start: auto;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 13.4px;
  font-weight: 650;
}

.sp-12__note {
  font-size: 13.6px;
  line-height: 1.6;
  color: var(--sp-12-mut);
  text-wrap: pretty;
}

.sp-12__grid {
  display: grid;
  grid-template-columns: repeat(2,minmax(0,1fr));
  gap: 12px;
}

.sp-12__field {
  display: grid;
  gap: 6px;
}

.sp-12__field--wide {
  grid-column: 1/-1;
}

.sp-12__flab {
  font-size: 12px;
  font-weight: 640;
  color: var(--sp-12-mut);
}

.sp-12__input {
  min-block-size: 44px;
  padding: 0 13px;
  border: 1px solid var(--sp-12-line);
  border-radius: 11px;
  background: oklch(0.99 0.003 250);
  font: inherit;
  font-size: 14.4px;
  color: var(--sp-12-ink);
  transition: border-color .2s ease,box-shadow .2s ease;
}

.sp-12__input::placeholder {
  color: color-mix(in oklch,var(--sp-12-mut) 65%,transparent);
}

.sp-12__input:focus-visible {
  outline: none;
  border-color: var(--sp-12-acc);
  box-shadow: 0 0 0 3px color-mix(in oklch,var(--sp-12-acc) 22%,transparent);
}

.sp-12__choices {
  display: grid;
  grid-template-columns: repeat(2,minmax(0,1fr));
  gap: 10px;
}

.sp-12__choice {
  display: grid;
  gap: 3px;
  justify-items: start;
  min-block-size: 56px;
  padding: 10px 13px;
  border: 1px solid var(--sp-12-line);
  border-radius: 13px;
  background: var(--sp-12-surface);
  cursor: pointer;
  text-align: start;
  transition: border-color .2s ease,background .2s ease;
}

.sp-12__choice[aria-checked="true"] {
  border-color: var(--sp-12-acc);
  background: color-mix(in oklch,var(--sp-12-acc) 8%,transparent);
}

.sp-12__choice:focus-visible,
.sp-12__pay:focus-visible,
.sp-12__brand:focus-visible {
  outline: 2px solid var(--sp-12-acc);
  outline-offset: 2px;
}

.sp-12__cname2 {
  font-size: 13.8px;
  font-weight: 660;
}

.sp-12__cmeta {
  font-size: 12.2px;
  color: var(--sp-12-mut);
}

.sp-12__pay {
  justify-self: start;
  min-block-size: 50px;
  padding: 0 26px;
  border: 0;
  border-radius: 13px;
  background: var(--sp-12-ink);
  color: oklch(1 0 0);
  font: inherit;
  font-size: 15px;
  font-weight: 680;
  cursor: pointer;
  transition: background .2s ease,translate .2s ease;
}

.sp-12__pay:hover {
  background: var(--sp-12-acc);
  translate: 0 -1px;
}

.sp-12__trust {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 12.4px;
  color: var(--sp-12-mut);
}

.sp-12__trust svg {
  inline-size: 15px;
  block-size: 15px;
  color: var(--sp-12-ok);
  flex: none;
}

.sp-12__status {
  min-block-size: 20px;
  font-size: 13px;
  font-weight: 620;
  color: var(--sp-12-ok);
}

.sp-12__summary {
  position: sticky;
  inset-block-start: 132px;
  align-self: start;
  display: grid;
  gap: 12px;
  padding: 18px;
  border: 1px solid var(--sp-12-line);
  border-radius: 18px;
  background: var(--sp-12-surface);
}

.sp-12__stitle {
  font-size: 13px;
  font-weight: 700;
  letter-spacing: .02em;
}

.sp-12__rows {
  display: grid;
  gap: 9px;
}

.sp-12__row {
  display: flex;
  justify-content: space-between;
  gap: 12px;
  font-size: 13.8px;
  color: var(--sp-12-mut);
}

.sp-12__row--total {
  padding-block-start: 9px;
  border-block-start: 1px solid var(--sp-12-line);
  color: var(--sp-12-ink);
  font-weight: 700;
  font-size: 15.5px;
}

.sp-12__snote {
  font-size: 11.6px;
  color: var(--sp-12-mut);
}

.sp-12__pagefoot {
  display: grid;
  place-items: center;
  padding: clamp(36px,7vh,90px) 24px;
  border-block-start: 1px solid var(--sp-12-line);
}

.sp-12__pagefootin {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  letter-spacing: .06em;
  color: var(--sp-12-mut);
  text-align: center;
}

.sp-12__bar,
.sp-12__steps,
.sp-12__layout {
  padding-inline: max(clamp(16px,3.5vw,34px),calc((100% - 1100px)/2));
}

:root:has(.sp-12) {
  scroll-behavior: smooth;
  scroll-padding-top: 132px;
}

@media (max-width: 860px) {
  .sp-12__layout {
    grid-template-columns: minmax(0,1fr);
  }

  .sp-12__summary {
    position: static;
  }

  .sp-12__panel {
    min-block-size: auto;
  }
}

@media (max-width: 560px) {
  .sp-12__grid,
    .sp-12__choices {
    grid-template-columns: minmax(0,1fr);
  }

  .sp-12__slab {
    font-size: 10.5px;
  }
}

@media (prefers-reduced-motion: reduce) {
  :root:has(.sp-12) {
    scroll-behavior: auto;
  }

  .sp-12 * {
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.sp-12');
  if (!root || root.dataset.spWired) return;
  root.dataset.spWired = '1';
  const steps = [...root.querySelectorAll('.sp-12__step')];
  const panels = [...root.querySelectorAll('.sp-12__panel')];
  const flow = root.querySelector('.sp-12__panels');
  const native = CSS.supports('animation-timeline', 'view()');
  let ticking = false, last = -1;
  const paint = () => {
    ticking = false;
    const vh = innerHeight || document.documentElement.clientHeight;
    const r = flow.getBoundingClientRect();
    const span = r.height - vh;
    const p = span > 0 ? Math.min(1, Math.max(0, -r.top / span)) : 0;
    if (!native) root.style.setProperty('--sp-12-p', p.toFixed(4));
    let cur = 0;
    panels.forEach((pn, i) => {
      const b = pn.getBoundingClientRect();
      if (b.top < vh * 0.45 && b.bottom > vh * 0.2) cur = i;
      if (!native) steps[i].dataset.on = String(b.top < vh * 0.6 && b.bottom > 0);
    });
    if (cur !== last) {
      last = cur;
      steps.forEach((s, i) => { if (i === cur) s.setAttribute('aria-current', 'step'); else s.removeAttribute('aria-current'); });
    }
  };
  const onScroll = () => { if (!ticking) { ticking = true; requestAnimationFrame(paint); } };
  addEventListener('scroll', onScroll, { passive: true });
  addEventListener('resize', onScroll, { passive: true });
  paint();
  root.querySelectorAll('.sp-12__choice').forEach((b) => b.addEventListener('click', () => {
    root.querySelectorAll('.sp-12__choice').forEach((o) => o.setAttribute('aria-checked', String(o === b)));
  }));
  const pay = root.querySelector('#sp-12-pay');
  const status = root.querySelector('#sp-12-status');
  pay.addEventListener('click', () => { status.textContent = 'Demo only — no payment was taken.'; });
})();
```
