---
source: "codefronts"
url: "https://codefronts.com/components/css-modals/password-reset-modal/"
title: "Password Reset Modal"
section: "components"
category: "css-modals"
category_name: "CSS Modals"
description: "A password reset request modal with a signature Corner Slide-and-Spin entrance — the modal slides in from bottom-right with subtle rotate + scale, feeling…"
has_js: "true"
---

Here's a working CSS Modal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Password Reset Modal
Source: https://codefronts.com/components/css-modals/password-reset-modal/

A password reset request modal with a signature Corner Slide-and-Spin entrance — the modal slides in from bottom-right with subtle rotate + scale, feeling like a helpful assistant materialized rather than a distant modal. Email input for reset link + "Send reset link" CTA + "Return to sign in" link + help microcopy for account recovery. Medium intensity — auth flows are personal but not compliance-heavy.
## HTML
```html
<div class="md-18">
  <button class="md-18__trigger" id="md-18-open">Forgot password?</button>
  <div class="md-18__backdrop" id="md-18-dialog" role="dialog" aria-modal="true" aria-labelledby="md-18-title">
    <div class="md-18__modal">
      <button class="md-18__x md-18__close" aria-label="Close">✕</button>
      <div class="md-18__lock" aria-hidden="true">🔑</div>
      <h2 class="md-18__title" id="md-18-title">Reset your password</h2>
      <p class="md-18__sub">Enter your email and we'll send a link to reset your password. Link expires in 30 minutes.</p>
      <form class="md-18__form" onsubmit="event.preventDefault()">
        <label class="md-18__field">
          <span>Email address</span>
          <input type="email" autocomplete="email" placeholder="[email protected]" required />
        </label>
        <button type="submit" class="md-18__cta md-18__close">Send reset link →</button>
      </form>
      <div class="md-18__foot">
        <button class="md-18__link md-18__close">← Return to sign in</button>
        <p class="md-18__help">Can't access this email? <a href="#">Contact support</a></p>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.md-18 {
  --page-bg: #f8fafc;
  --card: #ffffff;
  --ink: #0f172a;
  --sub: #64748b;
  --brand: #3b82f6;
  --brand-dark: #2563eb;
  --line: #e2e8f0;
  font-family: -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
  min-height: 100vh;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 32px;
  background: radial-gradient(60% 100% at 0% 100%, rgba(59,130,246,.08) 0%, transparent 60%), var(--page-bg);
  color: var(--ink);
}

.md-18 *,
.md-18 *::before,
.md-18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.md-18 ::selection {
  background: var(--brand);
  color: #fff;
}

.md-18__trigger {
  padding: 11px 22px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: var(--card);
  color: var(--brand);
  font-family: inherit;
  font-size: .9rem;
  font-weight: 600;
  cursor: pointer;
  transition: background .18s ease,border-color .18s ease;
}

.md-18__trigger:hover {
  background: #f1f5f9;
  border-color: var(--brand);
}

.md-18__backdrop {
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
  transition: opacity .25s ease,visibility 0s linear .25s;
}

.md-18__backdrop.is-open {
  opacity: 1;
  visibility: visible;
  transition: opacity .25s ease,visibility 0s linear 0s;
}

.md-18__modal {
  position: relative;
  width: min(400px,100%);
  padding: 32px 30px 24px;
  border-radius: 14px;
  background: var(--card);
  box-shadow: 0 30px 60px -20px rgba(15,23,42,.28);
  text-align: center;
  /* Signature entrance: Corner Slide-and-Spin — subtle, personal */
  opacity: 0;
  transform: translate(24px,32px) rotate(3deg) scale(.96);
  transform-origin: bottom right;
  transition: opacity .32s ease .04s,transform .4s cubic-bezier(.34,1.36,.44,1) .04s;
}

.md-18__backdrop.is-open .md-18__modal {
  opacity: 1;
  transform: translate(0,0) rotate(0) scale(1);
}

.md-18__x {
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

.md-18__x:hover {
  background: #f1f5f9;
  color: var(--ink);
}

.md-18__lock {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 52px;
  height: 52px;
  border-radius: 50%;
  background: rgba(59,130,246,.12);
  color: var(--brand);
  font-size: 24px;
  margin-bottom: 14px;
}

.md-18__title {
  font-size: 1.35rem;
  font-weight: 800;
  letter-spacing: -.015em;
  line-height: 1.2;
  margin-bottom: 8px;
}

.md-18__sub {
  font-size: .85rem;
  color: var(--sub);
  line-height: 1.55;
  margin-bottom: 20px;
}

.md-18__form {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.md-18__field {
  display: flex;
  flex-direction: column;
  gap: 5px;
  text-align: left;
}

.md-18__field span {
  font-size: .72rem;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: var(--sub);
}

.md-18__field input {
  padding: 12px 14px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: #fff;
  color: var(--ink);
  font-family: inherit;
  font-size: .9rem;
  transition: border-color .18s ease;
}

.md-18__field input:focus {
  outline: none;
  border-color: var(--brand);
  box-shadow: 0 0 0 3px rgba(59,130,246,.15);
}

.md-18__cta {
  padding: 13px 22px;
  border: none;
  border-radius: 8px;
  background: var(--brand);
  color: #fff;
  font-family: inherit;
  font-size: .92rem;
  font-weight: 700;
  cursor: pointer;
  box-shadow: 0 8px 18px -6px rgba(59,130,246,.5);
  transition: background .18s ease,transform .12s ease;
  margin-top: 4px;
}

.md-18__cta:hover {
  background: var(--brand-dark);
  transform: translateY(-1px);
}

.md-18__cta:focus-visible {
  outline: 2px solid var(--brand);
  outline-offset: 3px;
}

.md-18__foot {
  padding-top: 16px;
  margin-top: 16px;
  border-top: 1px solid var(--line);
}

.md-18__link {
  background: transparent;
  border: none;
  padding: 0 0 8px;
  color: var(--brand);
  font-family: inherit;
  font-size: .82rem;
  font-weight: 600;
  cursor: pointer;
}

.md-18__link:hover {
  text-decoration: underline;
}

.md-18__help {
  font-size: .72rem;
  color: var(--sub);
}

.md-18__help a {
  color: var(--brand);
  text-decoration: underline;
  font-weight: 600;
}

@media (prefers-reduced-motion: reduce) {
  .md-18__backdrop,
    .md-18__modal {
    transition: opacity .2s ease!important;
  }

  .md-18__modal {
    transform: none!important;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.querySelector('.md-18');
  if (!root) return;
  var openBtn = root.querySelector('#md-18-open');
  var dialog = root.querySelector('#md-18-dialog');
  var closeBtns = root.querySelectorAll('.md-18__close');
  var lastFocus = null;

  function open() {
    lastFocus = document.activeElement;
    dialog.classList.add('is-open');
    document.documentElement.style.overflow = 'hidden';
    var email = dialog.querySelector('input[type=email]');
    if (email) email.focus();
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
