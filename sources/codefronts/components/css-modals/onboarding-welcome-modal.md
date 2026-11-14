---
source: "codefronts"
url: "https://codefronts.com/components/css-modals/onboarding-welcome-modal/"
title: "Onboarding Welcome Modal"
section: "components"
category: "css-modals"
category_name: "CSS Modals"
description: "A SaaS onboarding welcome modal (\"Welcome to Northlight, Alex\") with a signature Blur-In Content Drop entrance — content elements cascade in from…"
has_js: "true"
---

Here's a working CSS Modal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Onboarding Welcome Modal
Source: https://codefronts.com/components/css-modals/onboarding-welcome-modal/

A SaaS onboarding welcome modal ("Welcome to Northlight, Alex") with a signature Blur-In Content Drop entrance — content elements cascade in from blurred+shifted state to settled state via staggered animation-delay. Progress stepper (3 steps) + hero illustration + primary CTA + skip link. Full intensity — first-time onboarding is the peak-impression moment for SaaS product perception (Linear, Notion, Figma all use decorative onboarding).
## HTML
```html
<div class="md-16">
  <button class="md-16__trigger" id="md-16-open">Sign in as Alex</button>
  <div class="md-16__backdrop" id="md-16-dialog" role="dialog" aria-modal="true" aria-labelledby="md-16-title">
    <div class="md-16__modal">
      <button class="md-16__x md-16__close" aria-label="Skip onboarding for now">✕</button>
      <div class="md-16__stepper" role="progressbar" aria-valuenow="1" aria-valuemin="1" aria-valuemax="3" aria-label="Step 1 of 3">
        <span class="md-16__step md-16__step--sel"></span>
        <span class="md-16__step"></span>
        <span class="md-16__step"></span>
      </div>
      <div class="md-16__drop md-16__illo" role="img" aria-label="Colorful abstract workspace illustration">
        <span class="md-16__illo-shape md-16__illo-shape--a"></span>
        <span class="md-16__illo-shape md-16__illo-shape--b"></span>
        <span class="md-16__illo-shape md-16__illo-shape--c"></span>
      </div>
      <p class="md-16__drop md-16__eyebrow">Welcome, Alex 👋</p>
      <h2 class="md-16__drop md-16__title" id="md-16-title">Let's set up your workspace</h2>
      <p class="md-16__drop md-16__sub">Answer a few quick questions and we'll tailor Northlight to how your team ships. Takes about 2 minutes.</p>
      <button class="md-16__drop md-16__cta md-16__close">Get started · 2 min</button>
      <button class="md-16__drop md-16__skip md-16__close">I'll do this later</button>
    </div>
  </div>
</div>
```
## CSS
```css
.md-16 {
  --page-bg: #faf7ff;
  --card: #ffffff;
  --ink: #1e1b4b;
  --sub: #6b7280;
  --brand: #7c3aed;
  --brand-light: #a78bfa;
  --line: #ede9fe;
  font-family: -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
  min-height: 100vh;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 32px;
  background: radial-gradient(60% 100% at 50% 0%, rgba(124,58,237,.08) 0%, transparent 60%), var(--page-bg);
  color: var(--ink);
}

.md-16 *,
.md-16 *::before,
.md-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.md-16 ::selection {
  background: var(--brand);
  color: #fff;
}

.md-16__trigger {
  padding: 12px 24px;
  border: none;
  border-radius: 9px;
  background: var(--brand);
  color: #fff;
  font-family: inherit;
  font-size: .92rem;
  font-weight: 700;
  cursor: pointer;
  box-shadow: 0 8px 20px -6px rgba(124,58,237,.5);
  transition: background .18s ease,transform .12s ease;
}

.md-16__trigger:hover {
  background: #6d28d9;
  transform: translateY(-1px);
}

.md-16__backdrop {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
  background: rgba(30,27,75,.5);
  backdrop-filter: blur(6px);
  -webkit-backdrop-filter: blur(6px);
  opacity: 0;
  visibility: hidden;
  transition: opacity .3s ease,visibility 0s linear .3s;
}

.md-16__backdrop.is-open {
  opacity: 1;
  visibility: visible;
  transition: opacity .3s ease,visibility 0s linear 0s;
}

.md-16__modal {
  position: relative;
  width: min(440px,100%);
  padding: 32px 32px 24px;
  border-radius: 16px;
  background: var(--card);
  box-shadow: 0 40px 60px -20px rgba(30,27,75,.35);
  text-align: center;
  opacity: 0;
  transition: opacity .35s ease;
}

.md-16__backdrop.is-open .md-16__modal {
  opacity: 1;
}

.md-16__x {
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

.md-16__x:hover {
  background: var(--line);
  color: var(--ink);
}
/* Signature entrance: Blur-In Content Drop */

.md-16__drop {
  opacity: 0;
  filter: blur(8px);
  transform: translateY(12px);
}

.md-16__backdrop.is-open .md-16__drop {
  animation: md-16-drop .5s cubic-bezier(.22,1,.36,1) forwards;
}

.md-16__backdrop.is-open .md-16__illo {
  animation-delay: .20s;
}

.md-16__backdrop.is-open .md-16__eyebrow {
  animation-delay: .32s;
}

.md-16__backdrop.is-open .md-16__title {
  animation-delay: .44s;
}

.md-16__backdrop.is-open .md-16__sub {
  animation-delay: .56s;
}

.md-16__backdrop.is-open .md-16__cta {
  animation-delay: .68s;
}

.md-16__backdrop.is-open .md-16__skip {
  animation-delay: .80s;
}

@keyframes md-16-drop {
  to {
    opacity: 1;
    filter: blur(0);
    transform: translateY(0);
  }
}

.md-16__stepper {
  display: flex;
  justify-content: center;
  gap: 6px;
  margin-bottom: 20px;
}

.md-16__step {
  width: 28px;
  height: 4px;
  border-radius: 2px;
  background: var(--line);
}

.md-16__step--sel {
  background: var(--brand);
}

.md-16__illo {
  position: relative;
  height: 120px;
  margin: 0 auto 18px;
  width: 170px;
}

.md-16__illo-shape {
  position: absolute;
  border-radius: 14px;
}

.md-16__illo-shape--a {
  top: 8px;
  left: 0;
  width: 110px;
  height: 80px;
  background: linear-gradient(135deg,#a78bfa,#7c3aed);
  transform: rotate(-6deg);
}

.md-16__illo-shape--b {
  top: 20px;
  left: 60px;
  width: 90px;
  height: 96px;
  background: linear-gradient(135deg,#fbbf24,#f59e0b);
  transform: rotate(4deg);
}

.md-16__illo-shape--c {
  top: 44px;
  left: 110px;
  width: 60px;
  height: 60px;
  border-radius: 50%;
  background: linear-gradient(135deg,#34d399,#10b981);
}

.md-16__eyebrow {
  font-size: .85rem;
  font-weight: 600;
  color: var(--sub);
  margin-bottom: 6px;
}

.md-16__title {
  font-size: 1.6rem;
  font-weight: 800;
  letter-spacing: -.02em;
  line-height: 1.15;
  margin-bottom: 10px;
  background: linear-gradient(135deg,var(--ink),var(--brand));
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.md-16__sub {
  font-size: .88rem;
  color: var(--sub);
  line-height: 1.55;
  margin-bottom: 20px;
}

.md-16__cta {
  width: 100%;
  padding: 14px 20px;
  border: none;
  border-radius: 9px;
  background: var(--brand);
  color: #fff;
  font-family: inherit;
  font-size: .95rem;
  font-weight: 700;
  cursor: pointer;
  box-shadow: 0 10px 24px -6px rgba(124,58,237,.5);
  transition: background .18s ease,transform .12s ease;
  margin-bottom: 8px;
}

.md-16__cta:hover {
  background: #6d28d9;
  transform: translateY(-1px);
}

.md-16__cta:focus-visible {
  outline: 2px solid var(--brand);
  outline-offset: 3px;
}

.md-16__skip {
  background: transparent;
  border: none;
  padding: 6px;
  color: var(--sub);
  font-family: inherit;
  font-size: .8rem;
  font-weight: 500;
  cursor: pointer;
}

.md-16__skip:hover {
  color: var(--ink);
  text-decoration: underline;
}

@media (prefers-reduced-motion: reduce) {
  .md-16__backdrop,
    .md-16__modal,
    .md-16__drop {
    transition: opacity .2s ease!important;
    animation: none!important;
  }

  .md-16__drop {
    opacity: 1!important;
    filter: none!important;
    transform: none!important;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.querySelector('.md-16');
  if (!root) return;
  var openBtn = root.querySelector('#md-16-open');
  var dialog = root.querySelector('#md-16-dialog');
  var closeBtns = root.querySelectorAll('.md-16__close');
  var lastFocus = null;

  function open() {
    lastFocus = document.activeElement;
    dialog.classList.add('is-open');
    document.documentElement.style.overflow = 'hidden';
    var cta = dialog.querySelector('.md-16__cta');
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
