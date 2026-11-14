---
source: "codefronts"
url: "https://codefronts.com/components/css-modals/terms-of-service-acceptance-modal/"
title: "Terms of Service Acceptance Modal"
section: "components"
category: "css-modals"
category_name: "CSS Modals"
description: "A Terms of Service + Privacy Policy acceptance modal for post-signup legal consent with a sober Letter-Slide entrance — modal slides down 20px with opacity…"
has_js: "true"
---

Here's a working CSS Modal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Terms of Service Acceptance Modal
Source: https://codefronts.com/components/css-modals/terms-of-service-acceptance-modal/

A Terms of Service + Privacy Policy acceptance modal for post-signup legal consent with a sober Letter-Slide entrance — modal slides down 20px with opacity fade over 320ms `ease-out`, no bounce, no scale. Reads as "a document being placed on the desk" rather than the pure fade Demo #05 HIPAA uses. Distinct but still institutional. Scrollable TOS body with version tag, explicit unchecked "I have read and agree" checkbox, separate marketing consent checkbox (never bundled), Accept + Decline actions with equal visual weight.
## HTML
```html
<div class="md-17">
  <button class="md-17__trigger" id="md-17-open">Complete signup</button>
  <div class="md-17__backdrop" id="md-17-dialog" role="dialog" aria-modal="true" aria-labelledby="md-17-title">
    <div class="md-17__modal">
      <button class="md-17__x md-17__close" aria-label="Close">✕</button>
      <div class="md-17__badge">Terms v3.2 · Updated 2026-07-15</div>
      <h2 class="md-17__title" id="md-17-title">Terms of Service &amp; Privacy Policy</h2>
      <p class="md-17__sub">Please review before continuing. Your acceptance is required to use Northlight.</p>
      <div class="md-17__body">
        <h3>1. Acceptance of terms</h3>
        <p>By accessing Northlight ("the Service"), you agree to be bound by these Terms of Service and our Privacy Policy. If you disagree with any part, do not use the Service.</p>
        <h3>2. Your account</h3>
        <p>You are responsible for maintaining the confidentiality of your account credentials and for all activities that occur under your account. You must notify us immediately of any unauthorized use.</p>
        <h3>3. Data collection &amp; use</h3>
        <p>We collect and process personal data as described in our <a href="#">Privacy Policy</a>. This includes account details, usage analytics, and content you create. We do not sell your data to third parties.</p>
        <h3>4. Content ownership</h3>
        <p>You retain ownership of content you create in the Service. By using the Service, you grant Northlight a limited license to store, process, and display your content for the purpose of providing the Service.</p>
        <h3>5. Termination</h3>
        <p>You may terminate your account at any time. We may suspend or terminate accounts that violate these Terms. Upon termination, we will delete your data within 30 days per GDPR Article 17.</p>
      </div>
      <label class="md-17__check">
        <input type="checkbox" required />
        <span>I have read and agree to the <a href="#">Terms of Service</a> and <a href="#">Privacy Policy</a></span>
      </label>
      <label class="md-17__check">
        <input type="checkbox" />
        <span>Send me product updates and newsletter (separate, optional consent)</span>
      </label>
      <div class="md-17__actions">
        <button class="md-17__btn md-17__btn--ghost md-17__close">Decline</button>
        <button class="md-17__btn md-17__btn--primary md-17__close">Accept &amp; continue</button>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.md-17 {
  --page-bg: #f8fafc;
  --card: #ffffff;
  --ink: #0f172a;
  --sub: #64748b;
  --brand: #0f172a;
  --good: #059669;
  --line: #e2e8f0;
  font-family: -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
  min-height: 100vh;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 32px;
  background: var(--page-bg);
  color: var(--ink);
}

.md-17 *,
.md-17 *::before,
.md-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.md-17 ::selection {
  background: var(--brand);
  color: #fff;
}

.md-17__trigger {
  padding: 12px 24px;
  border: none;
  border-radius: 9px;
  background: var(--brand);
  color: #fff;
  font-family: inherit;
  font-size: .92rem;
  font-weight: 600;
  cursor: pointer;
  transition: background .18s ease;
}

.md-17__trigger:hover {
  background: #1e293b;
}

.md-17__backdrop {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
  background: rgba(15,23,42,.55);
  backdrop-filter: blur(4px);
  -webkit-backdrop-filter: blur(4px);
  opacity: 0;
  visibility: hidden;
  transition: opacity .2s ease,visibility 0s linear .2s;
}

.md-17__backdrop.is-open {
  opacity: 1;
  visibility: visible;
  transition: opacity .2s ease,visibility 0s linear 0s;
}

.md-17__modal {
  position: relative;
  width: min(520px,100%);
  padding: 32px 32px 24px;
  border-radius: 14px;
  background: var(--card);
  box-shadow: 0 30px 60px -20px rgba(15,23,42,.28);
  /* Sober letter-slide entrance: modal slides down 20px + fades over 320ms.
       Reads as "a document being placed on the desk" — institutional, calm,
       no bounce/overshoot. Distinct from Demo #05 HIPAA (pure fade, strictest
       sobriety for medical trust) while still respecting the legal-context
       no-decorative-transform rule. */
  opacity: 0;
  transform: translateY(-20px);
  transition: opacity .32s ease-out .05s,transform .32s ease-out .05s;
}

.md-17__backdrop.is-open .md-17__modal {
  opacity: 1;
  transform: translateY(0);
}

.md-17__x {
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
  font-size: 16px;
  cursor: pointer;
  transition: background .18s ease,color .18s ease;
}

.md-17__x:hover {
  background: #f1f5f9;
  color: var(--ink);
}

.md-17__badge {
  display: inline-block;
  padding: 5px 12px;
  border-radius: 999px;
  background: #f1f5f9;
  color: var(--sub);
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: .7rem;
  font-weight: 700;
  letter-spacing: .02em;
  margin-bottom: 14px;
}

.md-17__title {
  font-size: 1.3rem;
  font-weight: 800;
  letter-spacing: -.015em;
  line-height: 1.2;
  margin-bottom: 8px;
}

.md-17__sub {
  font-size: .85rem;
  color: var(--sub);
  line-height: 1.5;
  margin-bottom: 18px;
}

.md-17__body {
  max-height: 230px;
  overflow-y: auto;
  -webkit-overflow-scrolling: touch;
  padding: 16px 18px;
  border: 1px solid var(--line);
  border-radius: 9px;
  background: #fafbfc;
  margin-bottom: 18px;
}

.md-17__body h3 {
  font-size: .85rem;
  font-weight: 700;
  color: var(--ink);
  margin-bottom: 5px;
}

.md-17__body h3:not(:first-child) {
  margin-top: 12px;
}

.md-17__body p {
  font-size: .78rem;
  color: var(--sub);
  line-height: 1.55;
}

.md-17__body a {
  color: var(--brand);
  text-decoration: underline;
  font-weight: 600;
}

.md-17__check {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  font-size: .82rem;
  color: var(--ink);
  line-height: 1.5;
  cursor: pointer;
  margin-bottom: 10px;
}

.md-17__check input[type=checkbox] {
  flex-shrink: 0;
  margin-top: 2px;
  width: 16px;
  height: 16px;
  accent-color: var(--good);
  cursor: pointer;
}

.md-17__check a {
  color: var(--brand);
  text-decoration: underline;
  font-weight: 600;
}

.md-17__actions {
  display: flex;
  gap: 10px;
  margin-top: 14px;
}

.md-17__btn {
  flex: 1;
  padding: 12px 16px;
  border: none;
  border-radius: 9px;
  font-family: inherit;
  font-size: .9rem;
  font-weight: 700;
  cursor: pointer;
  transition: background .18s ease,transform .12s ease;
}

.md-17__btn:active {
  transform: translateY(1px);
}

.md-17__btn--ghost {
  background: #f1f5f9;
  color: var(--ink);
}

.md-17__btn--ghost:hover {
  background: #e2e8f0;
}

.md-17__btn--primary {
  background: var(--good);
  color: #fff;
}

.md-17__btn--primary:hover {
  background: #047857;
}

.md-17__btn--primary:focus-visible {
  outline: 2px solid var(--good);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .md-17__backdrop,
    .md-17__modal {
    transition: opacity .2s ease!important;
  }

  .md-17__modal {
    transform: none!important;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.querySelector('.md-17');
  if (!root) return;
  var openBtn = root.querySelector('#md-17-open');
  var dialog = root.querySelector('#md-17-dialog');
  var closeBtns = root.querySelectorAll('.md-17__close');
  var lastFocus = null;

  function open() {
    lastFocus = document.activeElement;
    dialog.classList.add('is-open');
    document.documentElement.style.overflow = 'hidden';
    var body = dialog.querySelector('.md-17__body');
    if (body) { body.setAttribute('tabindex', '0'); body.focus(); }
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
