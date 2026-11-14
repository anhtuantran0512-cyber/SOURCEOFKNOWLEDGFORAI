---
source: "codefronts"
url: "https://codefronts.com/components/css-modals/newsletter-signup-modal/"
title: "Newsletter Signup Modal"
section: "components"
category: "css-modals"
category_name: "CSS Modals"
description: "A newsletter signup modal with a signature Depth-Layer Parallax entrance — three visual layers (backdrop, decorative shape, modal card) slide in from…"
has_js: "true"
---

Here's a working CSS Modal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Newsletter Signup Modal
Source: https://codefronts.com/components/css-modals/newsletter-signup-modal/

A newsletter signup modal with a signature Depth-Layer Parallax entrance — three visual layers (backdrop, decorative shape, modal card) slide in from different angles at different speeds, creating a cinematic depth effect. Editorial magazine palette (cream + charcoal + accent red), single-field email input + subscribe CTA + "1-click unsubscribe" trust line. Full intensity — newsletter contexts are low-stakes marketing where visual flair converts.
## HTML
```html
<div class="md-12">
  <button class="md-12__trigger" id="md-12-open">Get the newsletter</button>
  <div class="md-12__backdrop" id="md-12-dialog" role="dialog" aria-modal="true" aria-labelledby="md-12-title">
    <div class="md-12__stage">
      <span class="md-12__decor" aria-hidden="true"></span>
      <div class="md-12__modal">
        <button class="md-12__x md-12__close" aria-label="Close">✕</button>
        <p class="md-12__eyebrow">The Weekly Dispatch</p>
        <h2 class="md-12__title" id="md-12-title">Ideas worth 4 minutes of your Sunday.</h2>
        <p class="md-12__sub">One long-form essay on design, code, and craft. Sent Sunday. 12,400+ readers.</p>
        <form class="md-12__form" onsubmit="event.preventDefault()">
          <label class="md-12__field">
            <span class="sr-only">Email address</span>
            <input type="email" autocomplete="email" placeholder="[email protected]" required />
          </label>
          <button type="submit" class="md-12__cta md-12__close">Subscribe →</button>
        </form>
        <p class="md-12__trust">1-click unsubscribe · No spam, ever · GDPR-compliant</p>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.md-12 {
  --page-bg: #f5efe0;
  --card: #faf7f0;
  --ink: #1a1a1a;
  --sub: #6b6558;
  --accent: #e63946;
  --line: #e5dfd0;
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

.md-12 *,
.md-12 *::before,
.md-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.md-12 ::selection {
  background: var(--accent);
  color: #fff;
}

.md-12 .sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0,0,0,0);
  white-space: nowrap;
  border: 0;
}

.md-12__trigger {
  padding: 12px 24px;
  border: 1px solid var(--ink);
  border-radius: 6px;
  background: var(--ink);
  color: var(--card);
  font-family: inherit;
  font-size: .92rem;
  font-weight: 600;
  cursor: pointer;
  transition: background .18s ease;
}

.md-12__trigger:hover {
  background: #000;
}

.md-12__backdrop {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
  background: rgba(26,26,26,.55);
  backdrop-filter: blur(6px);
  -webkit-backdrop-filter: blur(6px);
  opacity: 0;
  visibility: hidden;
  transition: opacity .3s ease,visibility 0s linear .3s;
}

.md-12__backdrop.is-open {
  opacity: 1;
  visibility: visible;
  transition: opacity .3s ease,visibility 0s linear 0s;
}

.md-12__stage {
  position: relative;
  width: min(460px,100%);
}
/* Layer 1: decorative shape behind modal */

.md-12__decor {
  position: absolute;
  top: -40px;
  right: -40px;
  width: 150px;
  height: 150px;
  border-radius: 50%;
  background: var(--accent);
  z-index: 0;
  opacity: 0;
  transform: translateY(60px) scale(.8);
  transition: opacity .4s ease .1s,transform .5s ease-out .1s;
}

.md-12__backdrop.is-open .md-12__decor {
  opacity: 1;
  transform: translateY(0) scale(1);
}
/* Layer 2: modal card */

.md-12__modal {
  position: relative;
  z-index: 1;
  padding: 34px 32px 28px;
  border-radius: 14px;
  background: var(--card);
  box-shadow: 0 40px 60px -20px rgba(26,26,26,.4);
  overflow: hidden;
  opacity: 0;
  transform: translateY(30px);
  transition: opacity .45s ease .2s,transform .45s cubic-bezier(.22,1,.36,1) .2s;
}

.md-12__backdrop.is-open .md-12__modal {
  opacity: 1;
  transform: translateY(0);
}

.md-12__x {
  position: absolute;
  top: 14px;
  right: 14px;
  z-index: 2;
  width: 32px;
  height: 32px;
  border: none;
  border-radius: 6px;
  background: transparent;
  color: var(--sub);
  font-family: inherit;
  font-size: 15px;
  cursor: pointer;
  transition: background .18s ease,color .18s ease;
}

.md-12__x:hover {
  background: rgba(26,26,26,.06);
  color: var(--ink);
}

.md-12__eyebrow {
  font-size: .7rem;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 10px;
}

.md-12__title {
  font-family: 'Playfair Display',Georgia,serif;
  font-size: 1.7rem;
  font-weight: 800;
  letter-spacing: -.02em;
  line-height: 1.15;
  margin-bottom: 10px;
}

.md-12__sub {
  font-size: .88rem;
  color: var(--sub);
  line-height: 1.55;
  margin-bottom: 20px;
}

.md-12__form {
  display: flex;
  gap: 8px;
  margin-bottom: 12px;
}

@media (max-width: 400px) {
  .md-12__form {
    flex-direction: column;
  }
}

.md-12__field {
  flex: 1;
  display: block;
}

.md-12__field input {
  width: 100%;
  padding: 13px 14px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: #fff;
  color: var(--ink);
  font-family: inherit;
  font-size: .9rem;
  transition: border-color .18s ease;
}

.md-12__field input:focus {
  outline: none;
  border-color: var(--ink);
  box-shadow: 0 0 0 3px rgba(26,26,26,.1);
}

.md-12__cta {
  padding: 13px 22px;
  border: none;
  border-radius: 8px;
  background: var(--ink);
  color: var(--card);
  font-family: inherit;
  font-size: .9rem;
  font-weight: 700;
  cursor: pointer;
  white-space: nowrap;
  transition: background .18s ease,transform .12s ease;
}

.md-12__cta:hover {
  background: #000;
  transform: translateY(-1px);
}

.md-12__cta:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.md-12__trust {
  font-size: .72rem;
  color: var(--sub);
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .md-12__backdrop,
    .md-12__decor,
    .md-12__modal {
    transition: opacity .2s ease!important;
  }

  .md-12__decor,
    .md-12__modal {
    transform: none!important;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.querySelector('.md-12');
  if (!root) return;
  var openBtn = root.querySelector('#md-12-open');
  var dialog = root.querySelector('#md-12-dialog');
  var closeBtns = root.querySelectorAll('.md-12__close');
  var lastFocus = null;

  function open() {
    lastFocus = document.activeElement;
    dialog.classList.add('is-open');
    document.documentElement.style.overflow = 'hidden';
    // Focus email input — users came to sign up
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
