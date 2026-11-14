---
source: "codefronts"
url: "https://codefronts.com/motion/css-bounce-animation/form-error-alert-bounce/"
title: "Form Error Alert Bounce"
section: "motion"
category: "css-bounce-animation"
category_name: "CSS Bounce Animations"
description: "A form field that shakes horizontally when validation fails — the Stripe checkout / Google form field / login form error pattern."
has_js: "true"
---

Here's a working CSS Bounce Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Form Error Alert Bounce
Source: https://codefronts.com/motion/css-bounce-animation/form-error-alert-bounce/

A form field that shakes horizontally when validation fails — the Stripe checkout / Google form field / login form error pattern. Sharp aggressive shake reads as "this needs your attention NOW" without being ambiguous. Muted rose surface with a card email + payment field, red border on the invalid field, and error copy below. Users search for this when building form validation, checkout flows, or any input that needs failure feedback. Pure horizontal translateX shake — never a diagonal or scale change.
## HTML
```html
<div class="bn-14">
  <p class="bn-14__label">Form validation error shake</p>
  <form class="bn-14__form" id="bn-14-form" onsubmit="event.preventDefault()" novalidate>
    <label class="bn-14__field">
      <span>Email address</span>
      <input type="email" value="alex@studio" autocomplete="email" class="bn-14__input bn-14__input--email" />
    </label>
    <label class="bn-14__field">
      <span>Card number</span>
      <input type="text" value="4242 4242 4242 4242" inputmode="numeric" class="bn-14__input bn-14__input--card" id="bn-14-card" aria-invalid="false" aria-describedby="bn-14-err" />
      <span class="bn-14__error" id="bn-14-err" role="alert"></span>
    </label>
    <button type="submit" class="bn-14__submit" id="bn-14-submit">Pay $189</button>
  </form>
  <p class="bn-14__hint">The invalid field shakes horizontally; error copy fades in below.</p>
</div>
```
## CSS
```css
.bn-14 {
  --page-bg: #fef2f2;
  --surface: #ffffff;
  --ink: #450a0a;
  --sub: #9f7d7d;
  --brand: #dc2626;
  --brand-dark: #991b1b;
  --good: #065f46;
  --line: #fecaca;
  --input: #fafafa;
  font-family: -apple-system,BlinkMacSystemFont,'Inter','Segoe UI',sans-serif;
  width: 100%;
  min-height: 100vh;
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 20px;
  padding: 32px;
  background: radial-gradient(70% 60% at 50% 40%, rgba(220,38,38,.06) 0%, transparent 60%), var(--page-bg);
  color: var(--ink);
  text-align: center;
}

.bn-14 *,
.bn-14 *::before,
.bn-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bn-14 ::selection {
  background: var(--brand);
  color: #fff;
}

.bn-14__label {
  font-size: .9rem;
  font-weight: 600;
  color: var(--sub);
  letter-spacing: .02em;
}

.bn-14__form {
  display: flex;
  flex-direction: column;
  gap: 14px;
  width: min(380px,100%);
  padding: 26px 24px;
  border-radius: 14px;
  background: var(--surface);
  border: 1px solid var(--line);
  box-shadow: 0 20px 40px -12px rgba(220,38,38,.15);
  text-align: left;
}

.bn-14__field {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.bn-14__field > span:first-child {
  font-size: .72rem;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: var(--sub);
}

.bn-14__input {
  padding: 11px 14px;
  border: 1.5px solid #e5e7eb;
  border-radius: 8px;
  background: var(--input);
  color: var(--ink);
  font-family: inherit;
  font-size: .9rem;
  transition: border-color .18s ease,background .18s ease;
  will-change: transform;
}

.bn-14__input:focus {
  outline: none;
  border-color: var(--good);
  background: var(--surface);
}

.bn-14__input--card.is-error {
  border-color: var(--brand);
  background: #fef7f7;
}

.bn-14__input--card.is-shaking {
  animation: bn-14-shake .4s ease-out;
}

@keyframes bn-14-shake {
  0% {
    transform: translateX(0);
  }

  20% {
    transform: translateX(-8px);
  }

  40% {
    transform: translateX(8px);
  }

  60% {
    transform: translateX(-6px);
  }

  80% {
    transform: translateX(4px);
  }

  100% {
    transform: translateX(0);
  }
}

.bn-14__error {
  display: none;
  margin-top: 4px;
  font-size: .75rem;
  font-weight: 600;
  color: var(--brand);
  line-height: 1.4;
}

.bn-14__error.is-visible {
  display: block;
  animation: bn-14-error-in .3s ease-out .2s both;
}

@keyframes bn-14-error-in {
  from {
    opacity: 0;
    transform: translateY(-4px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.bn-14__submit {
  padding: 12px 18px;
  border: none;
  border-radius: 8px;
  background: var(--good);
  color: #fff;
  font-family: inherit;
  font-size: .92rem;
  font-weight: 700;
  cursor: pointer;
  box-shadow: 0 8px 18px -6px rgba(6,95,70,.4);
  transition: background .18s ease,transform .12s ease;
  margin-top: 2px;
}

.bn-14__submit:hover {
  background: #047857;
  transform: translateY(-1px);
}

.bn-14__submit:focus-visible {
  outline: 2px solid var(--good);
  outline-offset: 3px;
}

.bn-14__hint {
  font-size: .78rem;
  color: var(--sub);
  max-width: 380px;
  line-height: 1.5;
}

@media (prefers-reduced-motion: reduce) {
  .bn-14__input--card.is-shaking {
    animation: none!important;
    transform: none!important;
  }

  .bn-14__error.is-visible {
    animation: none!important;
    opacity: 1!important;
    transform: none!important;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.querySelector('.bn-14');
  if (!root) return;
  var card = root.querySelector('#bn-14-card');
  var err = root.querySelector('#bn-14-err');
  var btn = root.querySelector('#bn-14-submit');
  var form = root.querySelector('#bn-14-form');
  if (!card || !err || !btn) return;
  var errors = [
    'Card number is invalid. Check the digits and try again.',
    'This card was declined. Try a different card.',
    'Your card has expired. Please use a valid card.'
  ];
  var i = 0;
  function trigger(){
    card.classList.remove('is-shaking','is-error');
    err.classList.remove('is-visible');
    void card.offsetHeight;
    card.classList.add('is-shaking','is-error');
    card.setAttribute('aria-invalid','true');
    err.textContent = errors[i % errors.length];
    err.classList.add('is-visible');
    i++;
    setTimeout(function(){
      card.classList.remove('is-shaking');
    }, 500);
  }
  btn.addEventListener('click', function(e){ e.preventDefault(); trigger(); });
  form.addEventListener('submit', function(e){ e.preventDefault(); trigger(); });
  // Auto-cycle so gallery + preview show the pattern
  setInterval(trigger, 3000);
  setTimeout(trigger, 500);
})();
```
