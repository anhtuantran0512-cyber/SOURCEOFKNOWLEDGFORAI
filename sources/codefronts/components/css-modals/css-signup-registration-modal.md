---
source: "codefronts"
url: "https://codefronts.com/components/css-modals/css-signup-registration-modal/"
title: "CSS Signup Registration Modal"
section: "components"
category: "css-modals"
category_name: "CSS Modals"
description: "A B2C signup modal with a signature Origami Fan Deploy entrance — the modal's three horizontal panels (header / form / benefits strip) fan open sequentially…"
has_js: "true"
---

Here's a working CSS Modal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Signup Registration Modal
Source: https://codefronts.com/components/css-modals/css-signup-registration-modal/

A B2C signup modal with a signature Origami Fan Deploy entrance — the modal's three horizontal panels (header / form / benefits strip) fan open sequentially like Japanese origami unfolding, each panel starting rotated backward on the X-axis (rotateX(-90deg) with transform-origin: top) then settling flat. Green + warm cream palette matches the emotional shift from "come back" (login) to "welcome, new here" (signup). Medium intensity — playful enough to feel welcoming, controlled enough to feel professional.
## HTML
```html
<div class="md-03">
  <button class="md-03__trigger" id="md-03-open">Create account</button>
  <div class="md-03__backdrop" id="md-03-dialog" role="dialog" aria-modal="true" aria-labelledby="md-03-title">
    <div class="md-03__stage">
      <div class="md-03__modal">
        <button class="md-03__x md-03__close" aria-label="Close">✕</button>
        <div class="md-03__panel md-03__panel--head">
          <h2 class="md-03__title" id="md-03-title">Create your free account</h2>
          <p class="md-03__sub">Start your 14-day trial · No credit card required</p>
        </div>
        <div class="md-03__panel md-03__panel--form">
          <form class="md-03__form" onsubmit="event.preventDefault()">
            <label class="md-03__label">
              <span>How should we call you?</span>
              <input type="text" name="name" autocomplete="given-name" placeholder="Alex" required />
            </label>
            <label class="md-03__label">
              <span>Email</span>
              <input type="email" name="email" autocomplete="email" placeholder="[email protected]" required />
            </label>
            <label class="md-03__label">
              <span>Password</span>
              <input type="password" name="password" autocomplete="new-password" spellcheck="false" autocorrect="off" required minlength="10" />
              <div class="md-03__meter" aria-hidden="true">
                <span class="md-03__bar md-03__bar--good"></span>
                <span class="md-03__bar md-03__bar--good"></span>
                <span class="md-03__bar md-03__bar--good"></span>
                <span class="md-03__bar"></span>
              </div>
              <small class="md-03__hint">Good · 10+ characters · Not in breach databases</small>
            </label>
            <label class="md-03__check">
              <input type="checkbox" required />
              <span>I agree to the <a href="#">Terms of Service</a> and <a href="#">Privacy Policy</a></span>
            </label>
            <label class="md-03__check">
              <input type="checkbox" />
              <span>Send me product updates and CSS tips (optional)</span>
            </label>
            <button type="submit" class="md-03__submit">Create free account →</button>
          </form>
        </div>
        <div class="md-03__panel md-03__panel--foot">
          <ul class="md-03__benefits">
            <li>✓ 14-day trial</li>
            <li>✓ No credit card</li>
            <li>✓ Cancel anytime</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.md-03 {
  --page-bg: #f7f8fa;
  --card: #ffffff;
  --input: #f7f8fa;
  --ink: #0f0f14;
  --sub: #6b7280;
  --good: #10b981;
  --good-tint: rgba(16,185,129,.14);
  --warn: #f59e0b;
  --danger: #dc2626;
  --line: #e5e7eb;
  font-family: -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
  min-height: 100vh;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 32px;
  background: radial-gradient(70% 100% at 50% 0%, rgba(16,185,129,.06) 0%, transparent 60%), var(--page-bg);
  color: var(--ink);
}

.md-03 *,
.md-03 *::before,
.md-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.md-03 ::selection {
  background: var(--good);
  color: #fff;
}

.md-03__trigger {
  padding: 11px 24px;
  border: none;
  border-radius: 9px;
  background: var(--good);
  color: #fff;
  font-family: inherit;
  font-size: .9rem;
  font-weight: 600;
  cursor: pointer;
  box-shadow: 0 8px 20px -6px rgba(16,185,129,.55);
  transition: transform .12s ease,background .18s ease;
}

.md-03__trigger:hover {
  transform: translateY(-1px);
  background: #059669;
}

.md-03__backdrop {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
  background: rgba(15,23,42,.6);
  backdrop-filter: blur(6px);
  -webkit-backdrop-filter: blur(6px);
  opacity: 0;
  visibility: hidden;
  transition: opacity .22s ease,visibility 0s linear .22s;
}

.md-03__backdrop.is-open {
  opacity: 1;
  visibility: visible;
  transition: opacity .22s ease,visibility 0s linear 0s;
}
/* 3D stage for Origami Fan — perspective gives depth to the fold */

.md-03__stage {
  perspective: 1400px;
  width: min(460px,100%);
}

.md-03__modal {
  position: relative;
  padding: 0;
  border-radius: 14px;
  overflow: hidden;
  background: var(--card);
  box-shadow: 0 40px 60px -20px rgba(0,0,0,.35);
  transform-style: preserve-3d;
}
/* Signature entrance: Origami Fan Deploy — each panel folds down from top */

.md-03__panel {
  padding: 0 32px;
  opacity: 0;
  transform: rotateX(-90deg);
  transform-origin: top center;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
}

.md-03__panel--head {
  padding: 32px 32px 20px;
}

.md-03__panel--form {
  padding: 0 32px 20px;
}

.md-03__panel--foot {
  padding: 16px 32px 22px;
  border-top: 1px solid var(--line);
}

.md-03__backdrop.is-open .md-03__panel {
  animation: md-03-fold .5s cubic-bezier(.34,1.12,.5,1) forwards;
}

.md-03__backdrop.is-open .md-03__panel--head {
  animation-delay: .15s;
}

.md-03__backdrop.is-open .md-03__panel--form {
  animation-delay: .35s;
}

.md-03__backdrop.is-open .md-03__panel--foot {
  animation-delay: .55s;
}

@keyframes md-03-fold {
  from {
    opacity: 0;
    transform: rotateX(-90deg);
  }

  50% {
    opacity: 1;
  }

  to {
    opacity: 1;
    transform: rotateX(0);
  }
}

.md-03__x {
  position: absolute;
  top: 14px;
  right: 14px;
  z-index: 10;
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

.md-03__x:hover {
  background: #f1f5f9;
  color: var(--ink);
}

.md-03__title {
  font-size: 1.55rem;
  font-weight: 800;
  letter-spacing: -.02em;
  line-height: 1.15;
  margin-bottom: 6px;
}

.md-03__sub {
  font-size: .88rem;
  color: var(--sub);
}

.md-03__form {
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.md-03__label {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.md-03__label > span {
  font-size: .78rem;
  font-weight: 600;
  color: var(--sub);
}

.md-03__label input[type=text],
.md-03__label input[type=email],
.md-03__label input[type=password] {
  padding: 11px 14px;
  border: 1px solid var(--line);
  border-radius: 9px;
  background: var(--input);
  color: var(--ink);
  font-family: inherit;
  font-size: .9rem;
  transition: border-color .18s ease,background .18s ease;
}

.md-03__label input:focus {
  outline: none;
  border-color: var(--good);
  background: #fff;
}

.md-03__meter {
  display: flex;
  gap: 4px;
  margin-top: 6px;
}

.md-03__bar {
  flex: 1;
  height: 4px;
  border-radius: 2px;
  background: var(--line);
}

.md-03__bar--good {
  background: var(--good);
}

.md-03__hint {
  font-size: .7rem;
  color: var(--sub);
  letter-spacing: .02em;
}

.md-03__check {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  font-size: .82rem;
  color: var(--ink);
  line-height: 1.4;
  cursor: pointer;
}

.md-03__check input[type=checkbox] {
  flex-shrink: 0;
  margin-top: 2px;
  width: 16px;
  height: 16px;
  accent-color: var(--good);
  cursor: pointer;
}

.md-03__check a {
  color: var(--good);
  text-decoration: underline;
}

.md-03__submit {
  padding: 13px 22px;
  border: none;
  border-radius: 9px;
  background: var(--good);
  color: #fff;
  font-family: inherit;
  font-size: .95rem;
  font-weight: 700;
  cursor: pointer;
  box-shadow: 0 8px 20px -6px rgba(16,185,129,.5);
  transition: transform .12s ease,background .18s ease;
  margin-top: 6px;
}

.md-03__submit:hover {
  background: #059669;
  transform: translateY(-1px);
}

.md-03__submit:focus-visible {
  outline: 2px solid var(--good);
  outline-offset: 2px;
}

.md-03__benefits {
  list-style: none;
  display: flex;
  justify-content: center;
  gap: 16px;
  flex-wrap: wrap;
}

.md-03__benefits li {
  font-size: .72rem;
  color: var(--sub);
  font-weight: 600;
  letter-spacing: .02em;
}

@media (prefers-reduced-motion: reduce) {
  .md-03__backdrop,
    .md-03__panel {
    transition: none!important;
    animation: none!important;
  }

  .md-03__panel {
    opacity: 1!important;
    transform: none!important;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.querySelector('.md-03');
  if (!root) return;
  var openBtn = root.querySelector('#md-03-open');
  var dialog = root.querySelector('#md-03-dialog');
  var closeBtns = root.querySelectorAll('.md-03__close');
  var lastFocus = null;

  function open() {
    lastFocus = document.activeElement;
    dialog.classList.add('is-open');
    document.documentElement.style.overflow = 'hidden';
    var firstInput = dialog.querySelector('input[type=text]');
    if (firstInput) firstInput.focus();
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
