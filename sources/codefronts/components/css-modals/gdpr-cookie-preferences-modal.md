---
source: "codefronts"
url: "https://codefronts.com/components/css-modals/gdpr-cookie-preferences-modal/"
title: "GDPR Cookie Preferences Modal"
section: "components"
category: "css-modals"
category_name: "CSS Modals"
description: "A GDPR-compliant cookie preferences center with a signature 3D Origami Unfold entrance — the modal opens with the header + action buttons visible, then each…"
has_js: "true"
---

Here's a working CSS Modal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: GDPR Cookie Preferences Modal
Source: https://codefronts.com/components/css-modals/gdpr-cookie-preferences-modal/

A GDPR-compliant cookie preferences center with a signature 3D Origami Unfold entrance — the modal opens with the header + action buttons visible, then each of the 4 category rows unfolds downward one-by-one via 3D rotate3d flips like origami paper unfolding. The animation communicates the modal's core purpose (revealing your consent categories layer by layer) rather than being decorative theater. Neutral gray palette — legal compliance surfaces should be sober, not persuasive. Accept All / Reject All / Save Preferences with EQUAL visual weight (CNIL fined dark-pattern-favoring-Accept in 2022).
## HTML
```html
<div class="md-07">
  <button class="md-07__trigger" id="md-07-open">Cookie preferences</button>
  <div class="md-07__backdrop" id="md-07-dialog" role="dialog" aria-modal="true" aria-labelledby="md-07-title">
    <div class="md-07__stage">
      <div class="md-07__modal">
        <button class="md-07__x md-07__close" aria-label="Close">✕</button>
        <h2 class="md-07__title" id="md-07-title">Cookie preferences</h2>
        <p class="md-07__sub">We use cookies to enhance your experience, analyze site traffic, and improve services. You can accept all, reject all non-essential, or customize per category.</p>
        <div class="md-07__categories">
          <div class="md-07__cat">
            <div class="md-07__cat-head">
              <div>
                <h3>Strictly necessary</h3>
                <p>Session cookies, CSRF tokens, load balancing. Cannot be disabled.</p>
              </div>
              <span class="md-07__toggle md-07__toggle--locked" aria-hidden="true">ON</span>
            </div>
          </div>
          <div class="md-07__cat">
            <div class="md-07__cat-head">
              <div>
                <h3>Analytics</h3>
                <p>Google Analytics, PostHog. Helps us understand aggregate usage patterns.</p>
              </div>
              <label class="md-07__toggle-wrap">
                <input type="checkbox" checked />
                <span class="md-07__toggle" aria-hidden="true"></span>
              </label>
            </div>
          </div>
          <div class="md-07__cat">
            <div class="md-07__cat-head">
              <div>
                <h3>Marketing</h3>
                <p>Facebook Pixel, LinkedIn Insight Tag. Enables retargeting and personalized ads.</p>
              </div>
              <label class="md-07__toggle-wrap">
                <input type="checkbox" />
                <span class="md-07__toggle" aria-hidden="true"></span>
              </label>
            </div>
          </div>
          <div class="md-07__cat">
            <div class="md-07__cat-head">
              <div>
                <h3>Personalization</h3>
                <p>Recommendation engine, saved preferences, theme mode. Improves your experience.</p>
              </div>
              <label class="md-07__toggle-wrap">
                <input type="checkbox" checked />
                <span class="md-07__toggle" aria-hidden="true"></span>
              </label>
            </div>
          </div>
        </div>
        <div class="md-07__actions">
          <button class="md-07__btn md-07__btn--secondary md-07__close">Reject all</button>
          <button class="md-07__btn md-07__btn--secondary md-07__close">Save preferences</button>
          <button class="md-07__btn md-07__btn--primary md-07__close">Accept all</button>
        </div>
        <p class="md-07__foot">Read our <a href="#">Cookie Policy</a> and <a href="#">Privacy Policy</a>. You can change preferences anytime.</p>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.md-07 {
  --page-bg: #f8fafc;
  --card: #ffffff;
  --ink: #1e293b;
  --sub: #64748b;
  --good: #059669;
  --brand: #0f172a;
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

.md-07 *,
.md-07 *::before,
.md-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.md-07 ::selection {
  background: var(--brand);
  color: #fff;
}

.md-07__trigger {
  padding: 11px 22px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: var(--card);
  color: var(--ink);
  font-family: inherit;
  font-size: .9rem;
  font-weight: 600;
  cursor: pointer;
  transition: background .18s ease;
}

.md-07__trigger:hover {
  background: #f1f5f9;
}

.md-07__backdrop {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
  background: rgba(15,23,42,.6);
  backdrop-filter: blur(4px);
  -webkit-backdrop-filter: blur(4px);
  opacity: 0;
  visibility: hidden;
  transition: opacity .2s ease,visibility 0s linear .2s;
}

.md-07__backdrop.is-open {
  opacity: 1;
  visibility: visible;
  transition: opacity .2s ease,visibility 0s linear 0s;
}

.md-07__stage {
  position: relative;
  width: min(560px,100%);
  perspective: 1000px;
}

.md-07__modal {
  position: relative;
  z-index: 1;
  padding: 32px 32px 24px;
  border-radius: 14px;
  background: var(--card);
  box-shadow: 0 40px 60px -20px rgba(15,23,42,.35);
  transform-style: preserve-3d;
}

.md-07__x {
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

.md-07__x:hover {
  background: #f1f5f9;
  color: var(--ink);
}

.md-07__title {
  font-size: 1.35rem;
  font-weight: 800;
  letter-spacing: -.015em;
  line-height: 1.2;
  margin-bottom: 8px;
}

.md-07__sub {
  font-size: .85rem;
  color: var(--sub);
  line-height: 1.55;
  margin-bottom: 20px;
}

.md-07__categories {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin-bottom: 20px;
  transform-style: preserve-3d;
  perspective: 900px;
}
/* Signature entrance: 3D Paper Fold — direct port of the folding-ticket technique.
   Each category row folds behind itself via rotate3d(1,0,0,-180deg) with
   transform-origin: bottom, showing the front face on unfold. Staggered
   transition-delay creates the cascade. Base state is 0deg (unfolded); .is-open
   sets -180deg (folded flat behind); .is-unfolding removes the class briefly
   and cascades back to 0deg via transition-delay. */

.md-07__cat {
  padding: 14px 16px;
  border: 1px solid var(--line);
  border-radius: 9px;
  background: #fafbfc;
  transform-origin: bottom;
  transform-style: preserve-3d;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  /* Base state: folded behind (-180deg) + invisible. Cats stay in this state
       from page load onward, so first paint after modal opens = folded — no
       0deg flash. Transition property is defined here so the transition applies
       whether the value changes via .is-unfolding or the reverse. */
  opacity: 0;
  transform: rotate3d(1,0,0,-180deg);
  transition: transform .7s cubic-bezier(.4,.15,.25,1),opacity .3s ease;
}
/* Unfolded state — triggered one rAF after modal opens, cascades with stagger */

.md-07__backdrop.is-unfolding .md-07__cat {
  opacity: 1;
  transform: rotate3d(1,0,0,0deg);
}

.md-07__backdrop.is-unfolding .md-07__cat:nth-child(1) {
  transition-delay: 0s;
}

.md-07__backdrop.is-unfolding .md-07__cat:nth-child(2) {
  transition-delay: .18s;
}

.md-07__backdrop.is-unfolding .md-07__cat:nth-child(3) {
  transition-delay: .36s;
}

.md-07__backdrop.is-unfolding .md-07__cat:nth-child(4) {
  transition-delay: .54s;
}

.md-07__cat-head {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 14px;
}

.md-07__cat h3 {
  font-size: .88rem;
  font-weight: 700;
  color: var(--ink);
  margin-bottom: 2px;
}

.md-07__cat p {
  font-size: .75rem;
  color: var(--sub);
  line-height: 1.4;
}

.md-07__toggle {
  flex-shrink: 0;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 42px;
  height: 22px;
  border-radius: 11px;
  background: var(--good);
  color: #fff;
  font-size: .62rem;
  font-weight: 800;
  letter-spacing: .06em;
  position: relative;
}

.md-07__toggle-wrap {
  cursor: pointer;
  position: relative;
}

.md-07__toggle-wrap input {
  position: absolute;
  opacity: 0;
  width: 0;
  height: 0;
}

.md-07__toggle-wrap .md-07__toggle {
  background: #cbd5e1;
  color: transparent;
  transition: background .18s ease;
}

.md-07__toggle-wrap .md-07__toggle::before {
  content: '';
  position: absolute;
  left: 2px;
  top: 2px;
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: #fff;
  transition: transform .2s ease;
}

.md-07__toggle-wrap input:checked ~ .md-07__toggle {
  background: var(--good);
}

.md-07__toggle-wrap input:checked ~ .md-07__toggle::before {
  transform: translateX(20px);
}

.md-07__toggle--locked {
  background: #94a3b8;
  color: #fff;
}

.md-07__actions {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  margin-bottom: 16px;
}

.md-07__btn {
  flex: 1;
  min-width: 130px;
  padding: 11px 16px;
  border: none;
  border-radius: 8px;
  font-family: inherit;
  font-size: .85rem;
  font-weight: 600;
  cursor: pointer;
  transition: background .18s ease,transform .12s ease;
}

.md-07__btn:active {
  transform: translateY(1px);
}

.md-07__btn--secondary {
  background: #f1f5f9;
  color: var(--ink);
}

.md-07__btn--secondary:hover {
  background: #e2e8f0;
}

.md-07__btn--primary {
  background: var(--brand);
  color: #fff;
}

.md-07__btn--primary:hover {
  background: #334155;
}

.md-07__btn--primary:focus-visible {
  outline: 2px solid var(--brand);
  outline-offset: 2px;
}

.md-07__foot {
  font-size: .72rem;
  color: var(--sub);
  padding-top: 14px;
  border-top: 1px solid var(--line);
}

.md-07__foot a {
  color: var(--brand);
  text-decoration: underline;
}

@media (prefers-reduced-motion: reduce) {
  .md-07__backdrop,
    .md-07__cat {
    transition: opacity .2s ease!important;
    transition-delay: 0s!important;
  }

  .md-07__cat,
    .md-07__backdrop.is-open .md-07__cat,
    .md-07__backdrop.is-unfolding .md-07__cat {
    transform: none!important;
    opacity: 1!important;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.querySelector('.md-07');
  if (!root) return;
  var openBtn = root.querySelector('#md-07-open');
  var dialog = root.querySelector('#md-07-dialog');
  var closeBtns = root.querySelectorAll('.md-07__close');
  var lastFocus = null;

  function open() {
    lastFocus = document.activeElement;
    dialog.classList.add('is-open');
    document.documentElement.style.overflow = 'hidden';
    // Cats sit at -180deg + opacity 0 from CSS base rule (persisted since page
    // load). Adding .is-unfolding on the next frame triggers the cascade unfold
    // to 0deg. rAF gives the browser one paint cycle to commit the folded state
    // before the transition starts — otherwise style batching may skip the
    // starting frame and race the transition.
    requestAnimationFrame(function(){
      dialog.classList.add('is-unfolding');
    });
    var reject = dialog.querySelector('.md-07__btn--secondary');
    if (reject) reject.focus();
    document.addEventListener('keydown', onKey);
  }
  function close() {
    dialog.classList.remove('is-unfolding');
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
