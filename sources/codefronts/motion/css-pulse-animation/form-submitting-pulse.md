---
source: "codefronts"
url: "https://codefronts.com/motion/css-pulse-animation/form-submitting-pulse/"
title: "Form Submitting Pulse"
section: "motion"
category: "css-pulse-animation"
category_name: "CSS Pulse Animations"
description: "A B2B signup form with a submit button that transforms into a processing-pulse state on click — text disappears, replaced by a soft scale-pulse loader…"
has_js: "true"
---

Here's a working CSS Pulse Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Form Submitting Pulse
Source: https://codefronts.com/motion/css-pulse-animation/form-submitting-pulse/

A B2B signup form with a submit button that transforms into a processing-pulse state on click — text disappears, replaced by a soft scale-pulse loader indicating the API request is in flight. Muted purple (#6b46c1) accent on soft lavender background (#f5f3ff) — Superhuman / Vercel / Linear signup aesthetic. The pulse is DELIBERATELY calm (not spinning, not bouncing) because form submission is a trust context — the user just gave you their data and needs to feel it's being handled competently.
## HTML
```html
<div class="pl-12">
  <div class="pl-12__card">
    <p class="pl-12__eyebrow">Free · Personal plan</p>
    <h1 class="pl-12__title">Create your account</h1>
    <p class="pl-12__sub">14-day trial, no credit card required.</p>
    <form class="pl-12__form" id="pl-12-form" novalidate>
      <label class="pl-12__field">
        <span class="pl-12__field-label">Work email</span>
        <input type="email" name="email" value="[email protected]" autocomplete="email" placeholder="[email protected]" />
      </label>
      <label class="pl-12__field">
        <span class="pl-12__field-label">Company</span>
        <input type="text" name="company" value="Northlight Studio" placeholder="Your company name" />
      </label>
      <div class="pl-12__field">
        <span class="pl-12__field-label">Team size</span>
        <div class="pl-12__pills" role="radiogroup" aria-label="Team size">
          <button type="button" class="pl-12__pill" role="radio" aria-checked="false">1–5</button>
          <button type="button" class="pl-12__pill pl-12__pill--sel" role="radio" aria-checked="true">6–20</button>
          <button type="button" class="pl-12__pill" role="radio" aria-checked="false">21–100</button>
          <button type="button" class="pl-12__pill" role="radio" aria-checked="false">100+</button>
        </div>
      </div>
      <button type="submit" class="pl-12__submit" id="pl-12-submit" aria-live="polite">
        <span class="pl-12__submit-text">Create account</span>
        <span class="pl-12__submit-loader" aria-hidden="true"></span>
        <svg class="pl-12__submit-check" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
          <polyline points="4 12 10 18 20 6"/>
        </svg>
      </button>
      <p class="pl-12__foot">By continuing you agree to our <a href="#">Terms</a> and <a href="#">Privacy Policy</a>.</p>
    </form>
  </div>
</div>
```
## CSS
```css
.pl-12 {
  --page-bg: #f5f3ff;
  --card: #ffffff;
  --ink: #1e1b4b;
  --sub: #6b7280;
  --brand: #6b46c1;
  --brand-dark: #553c9a;
  --brand-soft: rgba(107,70,193,.1);
  --brand-glow: rgba(107,70,193,.35);
  --success: #10b981;
  --line: #e9d5ff;
  font-family: -apple-system,BlinkMacSystemFont,'Inter','Segoe UI',sans-serif;
  width: 100%;
  min-height: 100vh;
  position: relative;
  display: grid;
  place-items: center;
  padding: 32px;
  background: radial-gradient(70% 90% at 20% 0%, rgba(167,139,250,.14) 0%, transparent 55%), radial-gradient(60% 80% at 100% 100%, rgba(107,70,193,.08) 0%, transparent 55%), var(--page-bg);
  color: var(--ink);
}

.pl-12 *,
.pl-12 *::before,
.pl-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pl-12 ::selection {
  background: var(--brand);
  color: #fff;
}

.pl-12__card {
  width: min(440px,100%);
  padding: 34px 32px 28px;
  border-radius: 16px;
  background: var(--card);
  box-shadow: 0 20px 50px -12px rgba(76,29,149,.2),0 4px 12px -6px rgba(76,29,149,.08);
  border: 1px solid var(--line);
}

.pl-12__eyebrow {
  font-size: .7rem;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--brand);
  margin-bottom: 8px;
}

.pl-12__title {
  font-size: 1.5rem;
  font-weight: 800;
  letter-spacing: -.02em;
  margin-bottom: 6px;
}

.pl-12__sub {
  font-size: .85rem;
  color: var(--sub);
  margin-bottom: 20px;
}

.pl-12__form {
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.pl-12__field {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.pl-12__field-label {
  font-size: .72rem;
  font-weight: 700;
  letter-spacing: .05em;
  text-transform: uppercase;
  color: var(--sub);
}

.pl-12__field input {
  padding: 11px 14px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: #fafaff;
  color: var(--ink);
  font-family: inherit;
  font-size: .9rem;
  transition: border-color .15s ease,background .15s ease,box-shadow .15s ease;
}

.pl-12__field input:focus {
  outline: none;
  border-color: var(--brand);
  background: var(--card);
  box-shadow: 0 0 0 3px var(--brand-soft);
}

.pl-12__pills {
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
}

.pl-12__pill {
  padding: 8px 14px;
  border: 1px solid var(--line);
  border-radius: 7px;
  background: #fafaff;
  color: var(--sub);
  font-family: inherit;
  font-size: .82rem;
  font-weight: 600;
  cursor: pointer;
  transition: border-color .15s ease,background .15s ease,color .15s ease;
}

.pl-12__pill:hover {
  border-color: var(--brand);
  color: var(--ink);
}

.pl-12__pill--sel {
  background: var(--brand);
  color: #fff;
  border-color: var(--brand);
}
/* Submit button with 3-state machine: resting / submitting / success */

.pl-12__submit {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 46px;
  padding: 12px 22px;
  border: none;
  border-radius: 9px;
  background: var(--brand);
  color: #fff;
  font-family: inherit;
  font-size: .95rem;
  font-weight: 700;
  cursor: pointer;
  overflow: hidden;
  transition: background .18s ease,transform .12s ease;
  margin-top: 4px;
}

.pl-12__submit:hover {
  background: var(--brand-dark);
  transform: translateY(-1px);
}

.pl-12__submit:active {
  transform: translateY(1px);
}

.pl-12__submit:focus-visible {
  outline: 2px solid var(--brand);
  outline-offset: 3px;
}

.pl-12__submit-text {
  transition: opacity .2s ease;
}

.pl-12__submit-loader {
  position: absolute;
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: #fff;
  opacity: 0;
  transition: opacity .2s ease;
}

.pl-12__submit-check {
  position: absolute;
  opacity: 0;
  transition: opacity .2s ease;
}
/* Submitting state — text fades, loader appears + pulses */

.pl-12__submit.is-submitting {
  pointer-events: none;
}

.pl-12__submit.is-submitting .pl-12__submit-text {
  opacity: 0;
}

.pl-12__submit.is-submitting .pl-12__submit-loader {
  opacity: 1;
  animation: pl-12-loader 1.2s ease-in-out infinite;
}

@keyframes pl-12-loader {
  0%,
    100% {
    transform: scale(.85);
    box-shadow: 0 0 0 0 rgba(255,255,255,.5);
  }

  50% {
    transform: scale(1.05);
    box-shadow: 0 0 0 6px rgba(255,255,255,0);
  }
}
/* Success state — loader gone, checkmark visible, green button */

.pl-12__submit.is-success {
  background: var(--success);
  pointer-events: none;
}

.pl-12__submit.is-success .pl-12__submit-text,
.pl-12__submit.is-success .pl-12__submit-loader {
  opacity: 0;
}

.pl-12__submit.is-success .pl-12__submit-loader {
  animation: none;
}

.pl-12__submit.is-success .pl-12__submit-check {
  opacity: 1;
}

.pl-12__foot {
  font-size: .72rem;
  color: var(--sub);
  text-align: center;
  margin-top: 6px;
}

.pl-12__foot a {
  color: var(--brand);
  text-decoration: underline;
  font-weight: 600;
}

@media (prefers-reduced-motion: reduce) {
  .pl-12__submit-loader {
    animation: none!important;
    transform: none!important;
    box-shadow: none!important;
  }

  .pl-12__submit {
    transition: background .18s ease!important;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.querySelector('.pl-12');
  if (!root) return;
  var form = root.querySelector('#pl-12-form');
  var btn  = root.querySelector('#pl-12-submit');
  var pills = root.querySelectorAll('.pl-12__pill');
  if (!form || !btn) return;

  pills.forEach(function(p){
    p.addEventListener('click', function(){
      pills.forEach(function(x){
        x.classList.remove('pl-12__pill--sel');
        x.setAttribute('aria-checked','false');
      });
      p.classList.add('pl-12__pill--sel');
      p.setAttribute('aria-checked','true');
    });
  });

  var cycleTimer = null;
  function runCycle(){
    // Reset to resting
    btn.classList.remove('is-submitting','is-success');
    // Enter submitting state
    setTimeout(function(){
      btn.classList.add('is-submitting');
    }, 800);
    // Enter success state
    setTimeout(function(){
      btn.classList.remove('is-submitting');
      btn.classList.add('is-success');
    }, 3300);
    // Reset for next loop (demo purposes — production removes this)
    cycleTimer = setTimeout(runCycle, 5300);
  }

  form.addEventListener('submit', function(e){
    e.preventDefault();
    if (cycleTimer) clearTimeout(cycleTimer);
    runCycle();
  });

  // Auto-start the demo cycle so preview capture + gallery show the states.
  runCycle();
})();
```
