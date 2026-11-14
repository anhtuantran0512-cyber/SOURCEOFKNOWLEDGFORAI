---
source: "codefronts"
url: "https://codefronts.com/components/css-modals/order-success-confirmation-modal/"
title: "Order Success Confirmation Modal"
section: "components"
category: "css-modals"
category_name: "CSS Modals"
description: "An e-commerce order success confirmation modal (\"Thanks for your order\") with a signature Morphing Button Elastic entrance + CSS-only confetti burst — the…"
has_js: "true"
---

Here's a working CSS Modal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Order Success Confirmation Modal
Source: https://codefronts.com/components/css-modals/order-success-confirmation-modal/

An e-commerce order success confirmation modal ("Thanks for your order") with a signature Morphing Button Elastic entrance + CSS-only confetti burst — the modal expands elastically from small to full size while colorful confetti particles fire outward from center. Order summary + shipping ETA + tracking CTA + "Share your purchase" social row. Full intensity — order success is the peak dopamine moment, users EXPECT celebration UI.
## HTML
```html
<div class="md-15">
  <button class="md-15__trigger" id="md-15-open">Complete order · $189</button>
  <div class="md-15__backdrop" id="md-15-dialog" role="dialog" aria-modal="true" aria-labelledby="md-15-title">
    <div class="md-15__modal">
      <div class="md-15__confetti" aria-hidden="true">
        <span style="--c:#ff6b6b;--angle:12deg;--dist:180px"></span>
        <span style="--c:#4ecdc4;--angle:47deg;--dist:210px"></span>
        <span style="--c:#c9a961;--angle:88deg;--dist:170px"></span>
        <span style="--c:#a855f7;--angle:128deg;--dist:200px"></span>
        <span style="--c:#10b981;--angle:165deg;--dist:190px"></span>
        <span style="--c:#ff6b6b;--angle:205deg;--dist:220px"></span>
        <span style="--c:#4ecdc4;--angle:240deg;--dist:180px"></span>
        <span style="--c:#c9a961;--angle:275deg;--dist:210px"></span>
        <span style="--c:#a855f7;--angle:312deg;--dist:200px"></span>
        <span style="--c:#10b981;--angle:340deg;--dist:190px"></span>
        <span style="--c:#ec4899;--angle:60deg;--dist:150px"></span>
        <span style="--c:#3b82f6;--angle:220deg;--dist:150px"></span>
      </div>
      <button class="md-15__x md-15__close" aria-label="Close">✕</button>
      <div class="md-15__check-badge" aria-hidden="true">✓</div>
      <p class="md-15__eyebrow">Order #TR-8842</p>
      <h2 class="md-15__title" id="md-15-title">Thanks for your order, Alex</h2>
      <p class="md-15__sub">A confirmation is on its way to <strong>[email protected]</strong>. Your package ships in 24 hours.</p>
      <div class="md-15__eta">
        <div>
          <p class="md-15__eta-label">Estimated delivery</p>
          <p class="md-15__eta-value">Tue, Jul 30 — Thu, Aug 1</p>
        </div>
        <div class="md-15__eta-badge">Free 2-day shipping</div>
      </div>
      <div class="md-15__summary">
        <div class="md-15__row"><span>Subtotal (2 items)</span><span>$168.00</span></div>
        <div class="md-15__row"><span>Shipping</span><span class="md-15__row-good">Free</span></div>
        <div class="md-15__row"><span>Tax</span><span>$21.00</span></div>
        <div class="md-15__row md-15__row--total"><strong>Total charged</strong><strong>$189.00</strong></div>
      </div>
      <button class="md-15__cta md-15__close">Track your order →</button>
      <div class="md-15__aux">
        <button class="md-15__aux-btn md-15__close">Print receipt</button>
        <button class="md-15__aux-btn md-15__close">Share purchase</button>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.md-15 {
  --page-bg: #fdf7f4;
  --card: #faf7f0;
  --ink: #1e293b;
  --sub: #6b6558;
  --brand: #059669;
  --good: #10b981;
  --accent: #ff6b6b;
  --line: #eee5d0;
  font-family: -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
  min-height: 100vh;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 32px;
  background: radial-gradient(60% 100% at 50% 100%, rgba(16,185,129,.08) 0%, transparent 60%), var(--page-bg);
  color: var(--ink);
}

.md-15 *,
.md-15 *::before,
.md-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.md-15 ::selection {
  background: var(--brand);
  color: #fff;
}

.md-15__trigger {
  padding: 13px 26px;
  border: none;
  border-radius: 9px;
  background: var(--ink);
  color: var(--card);
  font-family: inherit;
  font-size: .92rem;
  font-weight: 700;
  cursor: pointer;
  box-shadow: 0 10px 22px -6px rgba(30,41,59,.4);
  transition: background .18s ease;
}

.md-15__trigger:hover {
  background: #000;
}

.md-15__backdrop {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
  background: rgba(30,41,59,.55);
  backdrop-filter: blur(6px);
  -webkit-backdrop-filter: blur(6px);
  opacity: 0;
  visibility: hidden;
  transition: opacity .3s ease,visibility 0s linear .3s;
}

.md-15__backdrop.is-open {
  opacity: 1;
  visibility: visible;
  transition: opacity .3s ease,visibility 0s linear 0s;
}

.md-15__modal {
  position: relative;
  width: min(460px,100%);
  padding: 36px 30px 24px;
  border-radius: 16px;
  background: var(--card);
  box-shadow: 0 40px 60px -20px rgba(30,41,59,.35);
  text-align: center;
  will-change: transform;
  /* Signature entrance: Morphing Button Elastic */
  opacity: 0;
  transform: scale(.12);
  transition: opacity .35s ease,transform .65s cubic-bezier(.68,-0.55,.32,1.55);
}

.md-15__backdrop.is-open .md-15__modal {
  opacity: 1;
  transform: scale(1);
}
/* Confetti burst */

.md-15__confetti {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 0;
  height: 0;
  pointer-events: none;
}

.md-15__confetti span {
  position: absolute;
  width: 10px;
  height: 14px;
  background: var(--c);
  border-radius: 2px;
  opacity: 0;
  transform: translate(-50%,-50%) rotate(0deg);
}

.md-15__backdrop.is-open .md-15__confetti span {
  animation: md-15-confetti 1.2s cubic-bezier(.4,0,.2,1) forwards;
  animation-delay: calc(var(--angle) / 360 * 0.5s);
}

@keyframes md-15-confetti {
  0% {
    opacity: 0;
    transform: translate(-50%,-50%) rotate(0deg);
  }

  15% {
    opacity: 1;
  }

  100% {
    opacity: 0;
    transform: translate(
            calc(-50% + cos(var(--angle)) * var(--dist)),
            calc(-50% + sin(var(--angle)) * var(--dist))
          ) rotate(720deg);
  }
}

.md-15__x {
  position: absolute;
  top: 14px;
  right: 14px;
  z-index: 2;
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

.md-15__x:hover {
  background: rgba(26,26,26,.06);
  color: var(--ink);
}

.md-15__check-badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 52px;
  height: 52px;
  border-radius: 50%;
  background: linear-gradient(135deg,var(--good),var(--brand));
  color: #fff;
  font-size: 24px;
  font-weight: 900;
  margin-bottom: 14px;
  box-shadow: 0 8px 20px -4px rgba(16,185,129,.5);
}

.md-15__eyebrow {
  font-size: .72rem;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--sub);
  margin-bottom: 8px;
  font-family: 'JetBrains Mono',ui-monospace,monospace;
}

.md-15__title {
  font-family: 'Playfair Display',Georgia,serif;
  font-size: 1.55rem;
  font-weight: 800;
  letter-spacing: -.02em;
  line-height: 1.15;
  margin-bottom: 8px;
}

.md-15__sub {
  font-size: .85rem;
  color: var(--sub);
  line-height: 1.55;
  margin-bottom: 18px;
}

.md-15__eta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 12px;
  padding: 12px 14px;
  border-radius: 9px;
  background: rgba(16,185,129,.08);
  text-align: left;
  margin-bottom: 14px;
}

.md-15__eta-label {
  font-size: .66rem;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: var(--brand);
}

.md-15__eta-value {
  font-size: .88rem;
  font-weight: 700;
  color: var(--ink);
  margin-top: 2px;
}

.md-15__eta-badge {
  font-size: .7rem;
  font-weight: 700;
  padding: 5px 10px;
  border-radius: 999px;
  background: var(--good);
  color: #fff;
  white-space: nowrap;
}

.md-15__summary {
  padding: 14px 16px;
  border: 1px solid var(--line);
  border-radius: 9px;
  margin-bottom: 16px;
  text-align: left;
}

.md-15__row {
  display: flex;
  justify-content: space-between;
  font-size: .82rem;
  color: var(--sub);
}

.md-15__row + .md-15__row {
  margin-top: 6px;
}

.md-15__row-good {
  color: var(--good);
  font-weight: 700;
}

.md-15__row--total {
  padding-top: 10px;
  margin-top: 10px;
  border-top: 1px solid var(--line);
  color: var(--ink);
}

.md-15__row--total strong {
  font-size: .9rem;
  font-weight: 800;
}

.md-15__cta {
  width: 100%;
  padding: 14px 22px;
  border: none;
  border-radius: 9px;
  background: var(--ink);
  color: var(--card);
  font-family: inherit;
  font-size: .95rem;
  font-weight: 800;
  cursor: pointer;
  transition: background .18s ease,transform .12s ease;
  margin-bottom: 10px;
}

.md-15__cta:hover {
  background: #000;
  transform: translateY(-1px);
}

.md-15__cta:focus-visible {
  outline: 2px solid var(--brand);
  outline-offset: 3px;
}

.md-15__aux {
  display: flex;
  gap: 8px;
}

.md-15__aux-btn {
  flex: 1;
  padding: 9px 12px;
  border: none;
  border-radius: 6px;
  background: transparent;
  color: var(--sub);
  font-family: inherit;
  font-size: .75rem;
  font-weight: 600;
  cursor: pointer;
  transition: background .18s ease,color .18s ease;
}

.md-15__aux-btn:hover {
  background: rgba(26,26,26,.06);
  color: var(--ink);
}

@media (prefers-reduced-motion: reduce) {
  .md-15__backdrop,
    .md-15__modal {
    transition: opacity .2s ease!important;
  }

  .md-15__modal {
    transform: none!important;
  }

  .md-15__confetti {
    display: none!important;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.querySelector('.md-15');
  if (!root) return;
  var openBtn = root.querySelector('#md-15-open');
  var dialog = root.querySelector('#md-15-dialog');
  var closeBtns = root.querySelectorAll('.md-15__close');
  var lastFocus = null;

  function open() {
    lastFocus = document.activeElement;
    dialog.classList.add('is-open');
    document.documentElement.style.overflow = 'hidden';
    // Focus Track Order — primary action after success
    var cta = dialog.querySelector('.md-15__cta');
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
