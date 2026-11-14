---
source: "codefronts"
url: "https://codefronts.com/components/css-modals/confirm-delete-modal/"
title: "Confirm Delete Modal"
section: "components"
category: "css-modals"
category_name: "CSS Modals"
description: "A destructive-action confirmation modal with a signature Corner Slide-and-Spin entrance — the card slides in from the bottom-right at a 3° angle then settles…"
has_js: "true"
---

Here's a working CSS Modal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Confirm Delete Modal
Source: https://codefronts.com/components/css-modals/confirm-delete-modal/

A destructive-action confirmation modal with a signature Corner Slide-and-Spin entrance — the card slides in from the bottom-right at a 3° angle then settles horizontally, giving the destructive prompt a distinct arrival that reads as intentional design rather than the standard fade-scale every SaaS uses. Sober gray + red destructive theme, item name emphasized, focus starts on Cancel (SAFE default).
## HTML
```html
<div class="md-01">
  <button class="md-01__trigger" id="md-01-open">Delete report</button>
  <div class="md-01__backdrop" id="md-01-dialog" role="dialog" aria-modal="true" aria-labelledby="md-01-title" aria-describedby="md-01-desc">
    <div class="md-01__modal">
      <div class="md-01__icon" aria-hidden="true">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 6h18M8 6V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2M6 6l1 14a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2l1-14"/></svg>
      </div>
      <h2 class="md-01__title" id="md-01-title">Delete this report?</h2>
      <p class="md-01__desc" id="md-01-desc">You're about to permanently delete <strong>Q3 Financial Report.pdf</strong>. This action cannot be undone and any team members sharing this report will lose access immediately.</p>
      <div class="md-01__actions">
        <button class="md-01__btn md-01__btn--ghost md-01__close">Cancel</button>
        <button class="md-01__btn md-01__btn--danger md-01__close">Delete report</button>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.md-01 {
  --page-bg: #f8fafc;
  --card: #ffffff;
  --ink: #0f172a;
  --sub: #64748b;
  --line: #e2e8f0;
  --danger: #dc2626;
  --danger-tint: rgba(220,38,38,.14);
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

.md-01 *,
.md-01 *::before,
.md-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.md-01 ::selection {
  background: var(--danger);
  color: #fff;
}

.md-01__trigger {
  padding: 11px 22px;
  border: 1px solid var(--danger);
  border-radius: 8px;
  background: transparent;
  color: var(--danger);
  font-family: inherit;
  font-size: .9rem;
  font-weight: 600;
  cursor: pointer;
  transition: background .18s ease,color .18s ease;
}

.md-01__trigger:hover {
  background: var(--danger);
  color: #fff;
}

.md-01__backdrop {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
  background: rgba(15,23,42,.72);
  backdrop-filter: blur(4px);
  -webkit-backdrop-filter: blur(4px);
  opacity: 0;
  visibility: hidden;
  transition: opacity .22s ease,visibility 0s linear .22s;
}

.md-01__backdrop.is-open {
  opacity: 1;
  visibility: visible;
  transition: opacity .22s ease,visibility 0s linear 0s;
}

.md-01__modal {
  width: min(340px,100%);
  padding: 26px 26px 22px;
  border-radius: 14px;
  background: var(--card);
  box-shadow: 0 30px 60px -20px rgba(0,0,0,.4);
  /* Signature entrance: Corner Slide-and-Spin from bottom-right corner */
  opacity: 0;
  transform: translate(24px, 32px) rotate(3deg) scale(.96);
  transform-origin: bottom right;
  transition: opacity .32s ease .04s,transform .4s cubic-bezier(.34,1.36,.44,1) .04s;
  text-align: center;
}

.md-01__backdrop.is-open .md-01__modal {
  opacity: 1;
  transform: translate(0,0) rotate(0) scale(1);
}

.md-01__icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 48px;
  height: 48px;
  border-radius: 50%;
  background: var(--danger-tint);
  color: var(--danger);
  margin-bottom: 16px;
}

.md-01__title {
  font-size: 1.15rem;
  font-weight: 700;
  letter-spacing: -.01em;
  line-height: 1.25;
  margin-bottom: 8px;
}

.md-01__desc {
  font-size: .88rem;
  color: var(--sub);
  line-height: 1.5;
  margin-bottom: 22px;
}

.md-01__desc strong {
  color: var(--ink);
  font-weight: 600;
}

.md-01__actions {
  display: flex;
  gap: 8px;
  justify-content: stretch;
}

.md-01__btn {
  flex: 1;
  padding: 10px 14px;
  border: none;
  border-radius: 8px;
  font-family: inherit;
  font-size: .88rem;
  font-weight: 600;
  cursor: pointer;
  transition: background .18s ease,transform .12s ease;
}

.md-01__btn:active {
  transform: translateY(1px);
}

.md-01__btn:focus-visible {
  outline: 2px solid var(--danger);
  outline-offset: 2px;
}

.md-01__btn--ghost {
  background: #f1f5f9;
  color: var(--ink);
}

.md-01__btn--ghost:hover {
  background: #e2e8f0;
}

.md-01__btn--danger {
  background: var(--danger);
  color: #fff;
}

.md-01__btn--danger:hover {
  background: #b91c1c;
}

@media (prefers-reduced-motion: reduce) {
  .md-01__backdrop,
    .md-01__modal {
    transition: none!important;
  }

  .md-01__modal {
    transform: none!important;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.querySelector('.md-01');
  if (!root) return;
  var openBtn = root.querySelector('#md-01-open');
  var dialog = root.querySelector('#md-01-dialog');
  var closeBtns = root.querySelectorAll('.md-01__close');
  var lastFocus = null;

  function open() {
    lastFocus = document.activeElement;
    dialog.classList.add('is-open');
    document.documentElement.style.overflow = 'hidden';
    var cancel = dialog.querySelector('.md-01__btn--ghost');
    if (cancel) cancel.focus();
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
