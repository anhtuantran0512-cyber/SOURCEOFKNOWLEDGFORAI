---
source: "codefronts"
url: "https://codefronts.com/components/css-modals/exit-intent-discount-modal/"
title: "Exit-Intent Discount Modal"
section: "components"
category: "css-modals"
category_name: "CSS Modals"
description: "An exit-intent discount modal (\"Wait!"
has_js: "true"
---

Here's a working CSS Modal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Exit-Intent Discount Modal
Source: https://codefronts.com/components/css-modals/exit-intent-discount-modal/

An exit-intent discount modal ("Wait! 15% off before you go") with a signature Liquid Morph entrance — the modal materializes through an SVG metaball filter with dramatic scale + rotate, signaling urgency and last-chance opportunity. High-contrast e-commerce palette (bold gradient CTA + urgent countdown timer + coupon code reveal). Full intensity — exit-intent contexts warrant maximum visual grab.
## HTML
```html
<div class="md-13">
  <svg width="0" height="0" style="position:absolute" aria-hidden="true">
    <defs>
      <filter id="md-13-goo">
        <feGaussianBlur in="SourceGraphic" stdDeviation="10" result="blur" />
        <feColorMatrix in="blur" mode="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 20 -8" result="goo" />
        <feComposite in="SourceGraphic" in2="goo" operator="atop" />
      </filter>
    </defs>
  </svg>
  <button class="md-13__trigger" id="md-13-open">Simulate exit intent</button>
  <div class="md-13__backdrop" id="md-13-dialog" role="dialog" aria-modal="true" aria-labelledby="md-13-title">
    <div class="md-13__modal">
      <button class="md-13__x md-13__close" aria-label="Close">✕</button>
      <p class="md-13__eyebrow">Wait!</p>
      <h2 class="md-13__title" id="md-13-title">
        <span class="md-13__discount">15% OFF</span>
        <span class="md-13__sub-title">your first order — before you go.</span>
      </h2>
      <div class="md-13__timer">
        <span class="md-13__timer-label">Offer expires in</span>
        <span class="md-13__timer-value">09:47</span>
      </div>
      <div class="md-13__coupon">
        <div>
          <span class="md-13__coupon-label">Your code</span>
          <span class="md-13__coupon-code">SAVE15</span>
        </div>
        <button class="md-13__coupon-copy">Copy</button>
      </div>
      <button class="md-13__cta md-13__close">Claim my discount →</button>
      <button class="md-13__reject md-13__close">No thanks, I'll pay full price</button>
    </div>
  </div>
</div>
```
## CSS
```css
.md-13 {
  --page-bg: #faf5ff;
  --card: #ffffff;
  --ink: #1e1b4b;
  --sub: #6b7280;
  --brand-start: #a855f7;
  --brand-end: #ec4899;
  --urgent: #dc2626;
  --line: #e9d5ff;
  font-family: -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
  min-height: 100vh;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 32px;
  background: radial-gradient(60% 100% at 0% 100%, rgba(168,85,247,.1) 0%, transparent 60%), radial-gradient(50% 80% at 100% 0%, rgba(236,72,153,.08) 0%, transparent 60%), var(--page-bg);
  color: var(--ink);
}

.md-13 *,
.md-13 *::before,
.md-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.md-13 ::selection {
  background: var(--brand-start);
  color: #fff;
}

.md-13__trigger {
  padding: 12px 24px;
  border: 1px dashed var(--sub);
  border-radius: 8px;
  background: transparent;
  color: var(--sub);
  font-family: inherit;
  font-size: .85rem;
  font-weight: 600;
  cursor: pointer;
  transition: border-color .18s ease,color .18s ease;
}

.md-13__trigger:hover {
  border-color: var(--ink);
  color: var(--ink);
}

.md-13__backdrop {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
  background: rgba(30,27,75,.7);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  opacity: 0;
  visibility: hidden;
  transition: opacity .3s ease,visibility 0s linear .3s;
}

.md-13__backdrop.is-open {
  opacity: 1;
  visibility: visible;
  transition: opacity .3s ease,visibility 0s linear 0s;
}

.md-13__modal {
  position: relative;
  width: min(440px,100%);
  padding: 34px 30px 24px;
  border-radius: 18px;
  background: var(--card);
  box-shadow: 0 40px 70px -15px rgba(168,85,247,.4);
  text-align: center;
  /* Signature entrance: Liquid Morph + dramatic rotate for urgency */
  opacity: 0;
  transform: scale(.4) rotate(-4deg);
  filter: url(#md-13-goo);
  transition: opacity .35s ease, transform .55s cubic-bezier(.34,1.56,.64,1), filter 0s linear .55s;
}

.md-13__backdrop.is-open .md-13__modal {
  opacity: 1;
  transform: scale(1) rotate(0deg);
  filter: none;
}

.md-13__x {
  position: absolute;
  top: 14px;
  right: 14px;
  width: 32px;
  height: 32px;
  border: none;
  border-radius: 8px;
  background: transparent;
  color: var(--sub);
  font-family: inherit;
  font-size: 15px;
  cursor: pointer;
  transition: background .18s ease,color .18s ease;
}

.md-13__x:hover {
  background: #f3e8ff;
  color: var(--ink);
}

.md-13__eyebrow {
  display: inline-block;
  font-size: .75rem;
  font-weight: 800;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--urgent);
  padding: 5px 12px;
  border-radius: 999px;
  background: rgba(220,38,38,.1);
  margin-bottom: 14px;
}

.md-13__title {
  display: flex;
  flex-direction: column;
  gap: 6px;
  margin-bottom: 20px;
}

.md-13__discount {
  font-family: 'Playfair Display',Georgia,serif;
  font-size: 2.6rem;
  font-weight: 900;
  letter-spacing: -.03em;
  line-height: 1;
  background: linear-gradient(135deg,var(--brand-start),var(--brand-end));
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.md-13__sub-title {
  font-size: 1rem;
  font-weight: 600;
  color: var(--ink);
}

.md-13__timer {
  display: flex;
  flex-direction: column;
  gap: 2px;
  padding: 10px 16px;
  border-radius: 9px;
  background: rgba(220,38,38,.08);
  color: var(--urgent);
  margin-bottom: 16px;
}

.md-13__timer-label {
  font-size: .68rem;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
}

.md-13__timer-value {
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: 1.35rem;
  font-weight: 800;
  letter-spacing: .02em;
  font-variant-numeric: tabular-nums;
}

.md-13__coupon {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 14px;
  padding: 12px 14px 12px 18px;
  border-radius: 9px;
  border: 1px dashed var(--brand-start);
  background: rgba(168,85,247,.06);
  text-align: left;
  margin-bottom: 16px;
}

.md-13__coupon > div {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.md-13__coupon-label {
  font-size: .66rem;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: var(--sub);
}

.md-13__coupon-code {
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: 1.05rem;
  font-weight: 800;
  letter-spacing: .06em;
  color: var(--ink);
}

.md-13__coupon-copy {
  padding: 8px 14px;
  border: none;
  border-radius: 6px;
  background: var(--ink);
  color: #fff;
  font-family: inherit;
  font-size: .75rem;
  font-weight: 700;
  cursor: pointer;
  transition: background .18s ease;
}

.md-13__coupon-copy:hover {
  background: #0f0a2e;
}

.md-13__cta {
  width: 100%;
  padding: 15px 22px;
  border: none;
  border-radius: 9px;
  background: linear-gradient(135deg,var(--brand-start),var(--brand-end));
  color: #fff;
  font-family: inherit;
  font-size: .98rem;
  font-weight: 800;
  cursor: pointer;
  box-shadow: 0 12px 24px -8px rgba(168,85,247,.55);
  transition: transform .12s ease,box-shadow .18s ease;
  margin-bottom: 10px;
}

.md-13__cta:hover {
  transform: translateY(-1px);
  box-shadow: 0 16px 30px -8px rgba(168,85,247,.65);
}

.md-13__cta:focus-visible {
  outline: 2px solid var(--brand-start);
  outline-offset: 3px;
}

.md-13__reject {
  background: transparent;
  border: none;
  padding: 8px;
  color: var(--sub);
  font-family: inherit;
  font-size: .75rem;
  font-weight: 400;
  cursor: pointer;
  text-decoration: underline;
}

.md-13__reject:hover {
  color: var(--ink);
}

@media (prefers-reduced-motion: reduce) {
  .md-13__backdrop,
    .md-13__modal {
    transition: opacity .2s ease!important;
  }

  .md-13__modal {
    transform: none!important;
    filter: none!important;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.querySelector('.md-13');
  if (!root) return;
  var openBtn = root.querySelector('#md-13-open');
  var dialog = root.querySelector('#md-13-dialog');
  var closeBtns = root.querySelectorAll('.md-13__close');
  var lastFocus = null;

  function open() {
    lastFocus = document.activeElement;
    dialog.classList.add('is-open');
    document.documentElement.style.overflow = 'hidden';
    // Focus Claim CTA — primary action for exit-intent
    var cta = dialog.querySelector('.md-13__cta');
    if (cta) cta.focus();
    document.addEventListener('keydown', onKey);
  }
  function close() {
    dialog.classList.remove('is-open');
    document.documentElement.style.overflow = '';
    document.removeEventListener('keydown', onKey);
    if (lastFocus) lastFocus.focus();
  }
  function onKey(e) { if (e.key === 'Escape') close(); }

  openBtn.addEventListener('click', open);
  closeBtns.forEach(function(b){ b.addEventListener('click', close); });
  dialog.addEventListener('click', function(e){ if (e.target === dialog) close(); });
})();
```
