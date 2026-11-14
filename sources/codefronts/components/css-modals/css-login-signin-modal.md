---
source: "codefronts"
url: "https://codefronts.com/components/css-modals/css-login-signin-modal/"
title: "CSS Login Signin Modal"
section: "components"
category: "css-modals"
category_name: "CSS Modals"
description: "A SaaS login modal with a signature Blur-In Content Drop entrance — the modal shell appears sharp instantly, then each element (brand mark → title → social…"
has_js: "true"
---

Here's a working CSS Modal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Login Signin Modal
Source: https://codefronts.com/components/css-modals/css-login-signin-modal/

A SaaS login modal with a signature Blur-In Content Drop entrance — the modal shell appears sharp instantly, then each element (brand mark → title → social buttons → divider → email/password fields → submit) drops in sequentially with staggered blur-clear (8px → 0 blur + translateY 12px → 0). Reads like a photograph developing, distinct from the standard fade-scale used by every SaaS. Muted intensity (8px blur not 20px) because auth needs trust, not spectacle.
## HTML
```html
<div class="md-02">
  <button class="md-02__trigger" id="md-02-open">Sign in</button>
  <div class="md-02__backdrop" id="md-02-dialog" role="dialog" aria-modal="true" aria-labelledby="md-02-title">
    <div class="md-02__modal">
      <button class="md-02__x md-02__close" aria-label="Close">✕</button>
      <div class="md-02__brand md-02__drop">
        <span class="md-02__brand-mark">◆</span>
        <span>CodeFronts</span>
      </div>
      <h2 class="md-02__title md-02__drop" id="md-02-title">Welcome back</h2>
      <p class="md-02__sub md-02__drop">Sign in to your workspace</p>
      <div class="md-02__social">
        <button class="md-02__soc md-02__drop"><span class="md-02__soc-ico" aria-hidden="true">G</span>Continue with Google</button>
        <button class="md-02__soc md-02__drop"><span class="md-02__soc-ico md-02__soc-ico--gh" aria-hidden="true">◉</span>Continue with GitHub</button>
        <button class="md-02__soc md-02__drop"><span class="md-02__soc-ico md-02__soc-ico--saml" aria-hidden="true">⚡</span>SSO / SAML</button>
      </div>
      <div class="md-02__divider md-02__drop"><span>or continue with email</span></div>
      <form class="md-02__form" onsubmit="event.preventDefault()">
        <label class="md-02__label md-02__drop">
          <span>Email</span>
          <input type="email" name="email" autocomplete="email" placeholder="[email protected]" required />
        </label>
        <label class="md-02__label md-02__drop">
          <span>Password <a href="#" class="md-02__forgot">Forgot?</a></span>
          <input type="password" name="password" autocomplete="current-password" spellcheck="false" autocorrect="off" required />
        </label>
        <button type="submit" class="md-02__submit md-02__drop">Sign in →</button>
      </form>
      <p class="md-02__foot md-02__drop">Don't have an account? <a href="#">Sign up</a></p>
    </div>
  </div>
</div>
```
## CSS
```css
.md-02 {
  --page-bg: #0a0e1c;
  --card: #141a2e;
  --ink: #f0eeff;
  --sub: #9d97c8;
  --brand: #7c3aed;
  --line: rgba(148,163,184,.14);
  font-family: -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
  min-height: 100vh;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 32px;
  background: radial-gradient(80% 100% at 20% 0%, rgba(124,58,237,.14) 0%, transparent 55%), var(--page-bg);
  color: var(--ink);
}

.md-02 *,
.md-02 *::before,
.md-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.md-02 ::selection {
  background: var(--brand);
  color: #fff;
}

.md-02__trigger {
  padding: 11px 24px;
  border: none;
  border-radius: 9px;
  background: linear-gradient(135deg,#8b5cf6,#7c3aed);
  color: #fff;
  font-family: inherit;
  font-size: .9rem;
  font-weight: 600;
  cursor: pointer;
  box-shadow: 0 8px 20px -6px rgba(124,58,237,.55);
  transition: transform .12s ease,box-shadow .18s ease;
}

.md-02__trigger:hover {
  transform: translateY(-1px);
  box-shadow: 0 12px 26px -6px rgba(124,58,237,.7);
}

.md-02__backdrop {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
  background: rgba(5,8,20,.72);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  opacity: 0;
  visibility: hidden;
  transition: opacity .22s ease,visibility 0s linear .22s;
}

.md-02__backdrop.is-open {
  opacity: 1;
  visibility: visible;
  transition: opacity .22s ease,visibility 0s linear 0s;
}

.md-02__modal {
  position: relative;
  width: min(420px,100%);
  padding: 36px 32px 28px;
  border-radius: 16px;
  background: linear-gradient(180deg,rgba(255,255,255,.03),rgba(255,255,255,0)),var(--card);
  border: 1px solid var(--line);
  box-shadow: 0 40px 60px -20px rgba(0,0,0,.6);
  /* Signature entrance: shell appears crisp, content items blur-drop cascade */
  opacity: 0;
  transition: opacity .2s ease .05s;
}

.md-02__backdrop.is-open .md-02__modal {
  opacity: 1;
}
/* Blur-In Content Drop — each child animates in with blur clearing + translateY settle */

.md-02__drop {
  opacity: 0;
  filter: blur(8px);
  transform: translateY(12px);
}

.md-02__backdrop.is-open .md-02__drop {
  animation: md-02-drop .5s cubic-bezier(.22,1,.36,1) forwards;
}

.md-02__backdrop.is-open .md-02__brand {
  animation-delay: .15s;
}

.md-02__backdrop.is-open .md-02__title {
  animation-delay: .22s;
}

.md-02__backdrop.is-open .md-02__sub {
  animation-delay: .28s;
}

.md-02__backdrop.is-open .md-02__social .md-02__soc:nth-child(1) {
  animation-delay: .35s;
}

.md-02__backdrop.is-open .md-02__social .md-02__soc:nth-child(2) {
  animation-delay: .4s;
}

.md-02__backdrop.is-open .md-02__social .md-02__soc:nth-child(3) {
  animation-delay: .45s;
}

.md-02__backdrop.is-open .md-02__divider {
  animation-delay: .55s;
}

.md-02__backdrop.is-open .md-02__form .md-02__label:nth-child(1) {
  animation-delay: .62s;
}

.md-02__backdrop.is-open .md-02__form .md-02__label:nth-child(2) {
  animation-delay: .68s;
}

.md-02__backdrop.is-open .md-02__submit {
  animation-delay: .75s;
}

.md-02__backdrop.is-open .md-02__foot {
  animation-delay: .82s;
}

@keyframes md-02-drop {
  from {
    opacity: 0;
    filter: blur(8px);
    transform: translateY(12px);
  }

  to {
    opacity: 1;
    filter: blur(0);
    transform: translateY(0);
  }
}

.md-02__x {
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

.md-02__x:hover {
  background: rgba(255,255,255,.06);
  color: var(--ink);
}

.md-02__brand {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: .85rem;
  font-weight: 700;
  letter-spacing: .02em;
  color: var(--brand);
  margin-bottom: 24px;
}

.md-02__brand-mark {
  font-size: 14px;
  line-height: 1;
}

.md-02__title {
  font-size: 1.6rem;
  font-weight: 800;
  letter-spacing: -.02em;
  line-height: 1.15;
  margin-bottom: 6px;
}

.md-02__sub {
  font-size: .9rem;
  color: var(--sub);
  margin-bottom: 24px;
}

.md-02__social {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin-bottom: 18px;
}

.md-02__soc {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  padding: 11px 14px;
  border: 1px solid var(--line);
  border-radius: 9px;
  background: rgba(255,255,255,.03);
  color: var(--ink);
  font-family: inherit;
  font-size: .9rem;
  font-weight: 500;
  cursor: pointer;
  transition: background .18s ease,border-color .18s ease;
}

.md-02__soc:hover {
  background: rgba(255,255,255,.06);
  border-color: rgba(148,163,184,.28);
}

.md-02__soc-ico {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 20px;
  height: 20px;
  border-radius: 4px;
  background: #fff;
  color: #0a0e1c;
  font-size: .72rem;
  font-weight: 800;
}

.md-02__soc-ico--gh {
  background: #24292f;
  color: #fff;
  font-size: .85rem;
}

.md-02__soc-ico--saml {
  background: linear-gradient(135deg,#7c3aed,#a78bfa);
  color: #fff;
}

.md-02__divider {
  display: flex;
  align-items: center;
  gap: 12px;
  margin: 14px 0 16px;
  font-size: .72rem;
  color: var(--sub);
  letter-spacing: .04em;
}

.md-02__divider::before,
.md-02__divider::after {
  content: '';
  flex: 1;
  height: 1px;
  background: var(--line);
}

.md-02__form {
  display: flex;
  flex-direction: column;
  gap: 14px;
  margin-bottom: 20px;
}

.md-02__label {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.md-02__label span {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  font-size: .78rem;
  font-weight: 600;
  color: var(--sub);
}

.md-02__forgot {
  color: var(--brand);
  text-decoration: none;
  font-size: .72rem;
  font-weight: 500;
}

.md-02__forgot:hover {
  text-decoration: underline;
}

.md-02__label input {
  padding: 11px 14px;
  border: 1px solid var(--line);
  border-radius: 9px;
  background: rgba(255,255,255,.03);
  color: var(--ink);
  font-family: inherit;
  font-size: .9rem;
  transition: border-color .18s ease,background .18s ease;
}

.md-02__label input:focus {
  outline: none;
  border-color: var(--brand);
  background: rgba(124,58,237,.06);
}

.md-02__submit {
  padding: 12px 22px;
  border: none;
  border-radius: 9px;
  background: linear-gradient(135deg,#8b5cf6,#7c3aed);
  color: #fff;
  font-family: inherit;
  font-size: .92rem;
  font-weight: 600;
  cursor: pointer;
  box-shadow: 0 8px 20px -6px rgba(124,58,237,.5);
  transition: transform .12s ease,box-shadow .18s ease;
}

.md-02__submit:hover {
  transform: translateY(-1px);
  box-shadow: 0 12px 26px -6px rgba(124,58,237,.65);
}

.md-02__submit:focus-visible {
  outline: 2px solid #a78bfa;
  outline-offset: 2px;
}

.md-02__foot {
  font-size: .82rem;
  color: var(--sub);
  text-align: center;
  padding-top: 16px;
  border-top: 1px solid var(--line);
}

.md-02__foot a {
  color: var(--brand);
  text-decoration: none;
  font-weight: 600;
}

.md-02__foot a:hover {
  text-decoration: underline;
}

@media (prefers-reduced-motion: reduce) {
  .md-02__backdrop,
    .md-02__modal,
    .md-02__drop {
    transition: none!important;
    animation: none!important;
  }

  .md-02__drop {
    opacity: 1!important;
    filter: none!important;
    transform: none!important;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.querySelector('.md-02');
  if (!root) return;
  var openBtn = root.querySelector('#md-02-open');
  var dialog = root.querySelector('#md-02-dialog');
  var closeBtns = root.querySelectorAll('.md-02__close');
  var lastFocus = null;

  function open() {
    lastFocus = document.activeElement;
    dialog.classList.add('is-open');
    document.documentElement.style.overflow = 'hidden';
    var firstInput = dialog.querySelector('input');
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
