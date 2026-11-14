---
source: "codefronts"
url: "https://codefronts.com/components/css-modals/hipaa-patient-consent-modal/"
title: "HIPAA Patient Consent Modal"
section: "components"
category: "css-modals"
category_name: "CSS Modals"
description: "A HIPAA-compliant patient consent modal for healthcare apps requiring authorization for PHI (Protected Health Information) sharing — telehealth video calls,…"
has_js: "true"
---

Here's a working CSS Modal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: HIPAA Patient Consent Modal
Source: https://codefronts.com/components/css-modals/hipaa-patient-consent-modal/

A HIPAA-compliant patient consent modal for healthcare apps requiring authorization for PHI (Protected Health Information) sharing — telehealth video calls, prescription requests, patient portal access. Uses a deliberate NO-signature entrance (subtle 200ms opacity fade only, zero decorative transform) because healthcare consent contexts REQUIRE the UI to read as sober, institutional, and trustworthy. Bottom-sheet mobile pattern with medical blue palette matching MyChart, Zocdoc, Teladoc conventions.
## HTML
```html
<div class="md-05">
  <button class="md-05__trigger" id="md-05-open">Start telehealth visit</button>
  <div class="md-05__backdrop" id="md-05-dialog" role="dialog" aria-modal="true" aria-labelledby="md-05-title">
    <div class="md-05__modal">
      <button class="md-05__x md-05__close" aria-label="Close">✕</button>
      <div class="md-05__badge">
        <span class="md-05__badge-ico" aria-hidden="true">⚕</span>
        HIPAA-compliant consent · Form v2.3
      </div>
      <h2 class="md-05__title" id="md-05-title">Authorization to share medical information</h2>
      <p class="md-05__sub">Please review before your telehealth visit. This authorization is required to connect you with a licensed provider.</p>
      <div class="md-05__body">
        <h3>What we collect and share</h3>
        <p>To provide telehealth services, we collect: your date of birth, insurance ID, symptom description, current medications, and appointment history. We share this with your assigned provider and, when medically necessary, with your primary care physician.</p>
        <h3>Your rights under HIPAA</h3>
        <p>You have the right to (1) access your PHI, (2) request amendments, (3) receive an accounting of disclosures, and (4) file a complaint. Read the full <a href="#">Notice of Privacy Practices</a> and <a href="#">Rights Under HIPAA</a>.</p>
        <h3>Withdrawing consent</h3>
        <p>You may withdraw this authorization at any time by contacting our Privacy Officer at <a href="#">[email protected]</a>. Withdrawal is effective going forward and does not affect PHI already disclosed.</p>
      </div>
      <label class="md-05__check">
        <input type="checkbox" required />
        <span>I have read and understand this authorization. I consent to the collection and sharing of my PHI as described above for this telehealth visit.</span>
      </label>
      <label class="md-05__check">
        <input type="checkbox" />
        <span>Optional: send me appointment reminders and health tips (separate consent)</span>
      </label>
      <div class="md-05__actions">
        <button class="md-05__btn md-05__btn--ghost md-05__close">I don't consent</button>
        <button class="md-05__btn md-05__btn--primary md-05__close">Sign and begin visit</button>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.md-05 {
  --page-bg: #f0f7fc;
  --card: #ffffff;
  --ink: #0f172a;
  --sub: #5b6b7d;
  --brand: #3b82f6;
  --good: #10b981;
  --line: #dbe3ec;
  font-family: -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
  min-height: 100vh;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 32px;
  background: radial-gradient(70% 100% at 50% 0%, rgba(59,130,246,.08) 0%, transparent 60%), var(--page-bg);
  color: var(--ink);
}

.md-05 *,
.md-05 *::before,
.md-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.md-05 ::selection {
  background: var(--brand);
  color: #fff;
}

.md-05__trigger {
  padding: 12px 24px;
  border: none;
  border-radius: 9px;
  background: var(--brand);
  color: #fff;
  font-family: inherit;
  font-size: .92rem;
  font-weight: 600;
  cursor: pointer;
  box-shadow: 0 8px 20px -6px rgba(59,130,246,.5);
  transition: transform .12s ease,background .18s ease;
}

.md-05__trigger:hover {
  background: #2563eb;
}

.md-05__backdrop {
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

.md-05__backdrop.is-open {
  opacity: 1;
  visibility: visible;
  transition: opacity .2s ease,visibility 0s linear 0s;
}

.md-05__modal {
  position: relative;
  width: min(520px,100%);
  padding: 32px 32px 24px;
  border-radius: 14px;
  background: var(--card);
  box-shadow: 0 30px 60px -20px rgba(15,23,42,.28);
  /* NO-signature entrance: sober 200ms opacity fade only. Deliberate design choice. */
  opacity: 0;
  transition: opacity .2s ease .05s;
}

.md-05__backdrop.is-open .md-05__modal {
  opacity: 1;
}

.md-05__x {
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

.md-05__x:hover {
  background: #f1f5f9;
  color: var(--ink);
}

.md-05__badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 5px 12px;
  border-radius: 999px;
  background: rgba(59,130,246,.10);
  color: var(--brand);
  font-size: .72rem;
  font-weight: 600;
  letter-spacing: .02em;
  margin-bottom: 16px;
}

.md-05__badge-ico {
  font-size: 12px;
}

.md-05__title {
  font-size: 1.3rem;
  font-weight: 800;
  letter-spacing: -.015em;
  line-height: 1.2;
  margin-bottom: 8px;
}

.md-05__sub {
  font-size: .88rem;
  color: var(--sub);
  line-height: 1.5;
  margin-bottom: 18px;
}

.md-05__body {
  max-height: 220px;
  overflow-y: auto;
  -webkit-overflow-scrolling: touch;
  padding: 16px 18px;
  border: 1px solid var(--line);
  border-radius: 9px;
  background: #fafbfc;
  margin-bottom: 18px;
}

.md-05__body h3 {
  font-size: .85rem;
  font-weight: 700;
  color: var(--ink);
  letter-spacing: -.005em;
  margin-bottom: 6px;
}

.md-05__body h3:not(:first-child) {
  margin-top: 14px;
}

.md-05__body p {
  font-size: .8rem;
  color: var(--sub);
  line-height: 1.55;
}

.md-05__body a {
  color: var(--brand);
  text-decoration: underline;
}

.md-05__check {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  font-size: .82rem;
  color: var(--ink);
  line-height: 1.5;
  cursor: pointer;
  margin-bottom: 10px;
}

.md-05__check input[type=checkbox] {
  flex-shrink: 0;
  margin-top: 2px;
  width: 16px;
  height: 16px;
  accent-color: var(--good);
  cursor: pointer;
}

.md-05__actions {
  display: flex;
  gap: 10px;
  margin-top: 14px;
}

.md-05__btn {
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

.md-05__btn:active {
  transform: translateY(1px);
}

.md-05__btn--ghost {
  background: #f1f5f9;
  color: var(--ink);
}

.md-05__btn--ghost:hover {
  background: #e2e8f0;
}

.md-05__btn--primary {
  background: var(--good);
  color: #fff;
}

.md-05__btn--primary:hover {
  background: #059669;
}

.md-05__btn--primary:focus-visible {
  outline: 2px solid var(--good);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .md-05__backdrop,
    .md-05__modal {
    transition: none!important;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.querySelector('.md-05');
  if (!root) return;
  var openBtn = root.querySelector('#md-05-open');
  var dialog = root.querySelector('#md-05-dialog');
  var closeBtns = root.querySelectorAll('.md-05__close');
  var lastFocus = null;

  function open() {
    lastFocus = document.activeElement;
    dialog.classList.add('is-open');
    document.documentElement.style.overflow = 'hidden';
    // Focus the consent body so screen readers announce the content
    var body = dialog.querySelector('.md-05__body');
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
