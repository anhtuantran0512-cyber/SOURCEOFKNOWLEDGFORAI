---
source: "codefronts"
url: "https://codefronts.com/components/css-modals/age-verification-modal/"
title: "Age Verification Modal"
section: "components"
category: "css-modals"
category_name: "CSS Modals"
description: "An age verification gate modal for regulated products (alcohol, cannabis, adult content, tobacco, gambling) with a signature Clip-Path Circuit Iris Aperture…"
has_js: "true"
---

Here's a working CSS Modal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Age Verification Modal
Source: https://codefronts.com/components/css-modals/age-verification-modal/

An age verification gate modal for regulated products (alcohol, cannabis, adult content, tobacco, gambling) with a signature Clip-Path Circuit Iris Aperture entrance — the modal reveals through an expanding circular clip-path that opens like a camera iris, distinctive and thematic for a "gatekeeping" moment. Warm amber palette (bourbon/whiskey aesthetic — commercial default for age gates), Date of Birth trio inputs (MM / DD / YYYY), plus session/persistent checkbox.
## HTML
```html
<div class="md-06">
  <button class="md-06__trigger" id="md-06-open">Enter shop</button>
  <div class="md-06__backdrop" id="md-06-dialog" role="dialog" aria-modal="true" aria-labelledby="md-06-title">
    <div class="md-06__modal">
      <div class="md-06__lock" aria-hidden="true">🔒</div>
      <h2 class="md-06__title" id="md-06-title">You must be 21 or older</h2>
      <p class="md-06__sub">This site sells products intended for adults 21+. Please verify your date of birth to continue.</p>
      <form class="md-06__form" onsubmit="event.preventDefault()">
        <div class="md-06__dob">
          <label class="md-06__field">
            <span>Month</span>
            <input type="text" name="bday-month" autocomplete="bday-month" placeholder="MM" inputmode="numeric" pattern="[0-9]{1,2}" maxlength="2" required />
          </label>
          <label class="md-06__field">
            <span>Day</span>
            <input type="text" name="bday-day" autocomplete="bday-day" placeholder="DD" inputmode="numeric" pattern="[0-9]{1,2}" maxlength="2" required />
          </label>
          <label class="md-06__field">
            <span>Year</span>
            <input type="text" name="bday-year" autocomplete="bday-year" placeholder="YYYY" inputmode="numeric" pattern="[0-9]{4}" maxlength="4" required />
          </label>
        </div>
        <label class="md-06__remember">
          <input type="checkbox" />
          <span>Remember me for 30 days on this device</span>
        </label>
        <button type="submit" class="md-06__submit md-06__close">Enter site →</button>
        <button type="button" class="md-06__leave md-06__close">I'm under 21</button>
      </form>
      <p class="md-06__legal">Alcohol is intended for adults 21+. Please drink responsibly. Site restricted per US federal law.</p>
    </div>
  </div>
</div>
```
## CSS
```css
.md-06 {
  --page-bg: #1a0f08;
  --card: #f5ead0;
  --card-warm: #efe0ba;
  --ink: #2a1810;
  --sub: #7a5b3e;
  --brand: #c8552a;
  --brand-dark: #9d3f1f;
  --line: rgba(42,24,16,.16);
  font-family: -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
  min-height: 100vh;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 32px;
  background: radial-gradient(80% 100% at 50% 0%, rgba(200,85,42,.16) 0%, transparent 60%), var(--page-bg);
  color: var(--ink);
}

.md-06 *,
.md-06 *::before,
.md-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.md-06 ::selection {
  background: var(--brand);
  color: #fff;
}

.md-06__trigger {
  padding: 12px 26px;
  border: 1px solid var(--brand);
  border-radius: 8px;
  background: transparent;
  color: var(--brand);
  font-family: inherit;
  font-size: .92rem;
  font-weight: 600;
  cursor: pointer;
  transition: background .18s ease,color .18s ease;
}

.md-06__trigger:hover {
  background: var(--brand);
  color: #fff;
}

.md-06__backdrop {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
  background: rgba(26,15,8,.85);
  backdrop-filter: blur(6px);
  -webkit-backdrop-filter: blur(6px);
  opacity: 0;
  visibility: hidden;
  transition: opacity .25s ease,visibility 0s linear .25s;
}

.md-06__backdrop.is-open {
  opacity: 1;
  visibility: visible;
  transition: opacity .25s ease,visibility 0s linear 0s;
}

.md-06__modal {
  position: relative;
  width: min(400px,100%);
  padding: 36px 24px 28px;
  border-radius: 14px;
  background: linear-gradient(180deg,var(--card),var(--card-warm));
  border: 1px solid rgba(42,24,16,.08);
  box-shadow: 0 40px 60px -20px rgba(26,15,8,.6);
  text-align: center;
  /* Signature entrance: Clip-Path Circuit Iris Aperture — camera iris opening */
  opacity: 0;
  clip-path: circle(0% at 50% 50%);
  transition: opacity .3s ease .05s,clip-path .55s cubic-bezier(.65,0,.35,1) .05s;
}

.md-06__backdrop.is-open .md-06__modal {
  opacity: 1;
  clip-path: circle(150% at 50% 50%);
}

.md-06__lock {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 52px;
  height: 52px;
  border-radius: 50%;
  background: rgba(200,85,42,.16);
  color: var(--brand);
  font-size: 22px;
  margin-bottom: 14px;
}

.md-06__title {
  font-family: 'Playfair Display',Georgia,serif;
  font-size: 1.4rem;
  font-weight: 800;
  letter-spacing: -.015em;
  line-height: 1.2;
  margin-bottom: 8px;
}

.md-06__sub {
  font-size: .85rem;
  color: var(--sub);
  line-height: 1.5;
  margin-bottom: 22px;
}

.md-06__form {
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.md-06__dob {
  display: grid;
  grid-template-columns: 1fr 1fr 1.4fr;
  gap: 8px;
  width: 100%;
}

.md-06__field {
  display: flex;
  flex-direction: column;
  gap: 5px;
  text-align: left;
  min-width: 0;
}

.md-06__field span {
  font-size: .7rem;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: var(--sub);
}

.md-06__field input {
  width: 100%;
  min-width: 0;
  padding: 11px 8px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: #fff;
  color: var(--ink);
  font-family: inherit;
  font-size: .95rem;
  text-align: center;
  font-variant-numeric: tabular-nums;
  transition: border-color .18s ease;
}

.md-06__field input:focus {
  outline: none;
  border-color: var(--brand);
  box-shadow: 0 0 0 3px rgba(200,85,42,.15);
}

.md-06__remember {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: .78rem;
  color: var(--sub);
  cursor: pointer;
  margin-top: 2px;
}

.md-06__remember input {
  width: 14px;
  height: 14px;
  accent-color: var(--brand);
}

.md-06__submit {
  padding: 12px 22px;
  border: none;
  border-radius: 8px;
  background: var(--brand);
  color: #fff;
  font-family: inherit;
  font-size: .95rem;
  font-weight: 700;
  cursor: pointer;
  box-shadow: 0 8px 18px -6px rgba(200,85,42,.5);
  transition: background .18s ease,transform .12s ease;
  margin-top: 6px;
}

.md-06__submit:hover {
  background: var(--brand-dark);
  transform: translateY(-1px);
}

.md-06__submit:focus-visible {
  outline: 2px solid var(--brand);
  outline-offset: 3px;
}

.md-06__leave {
  padding: 8px 20px;
  border: none;
  border-radius: 6px;
  background: transparent;
  color: var(--sub);
  font-family: inherit;
  font-size: .8rem;
  font-weight: 500;
  cursor: pointer;
  transition: color .18s ease;
}

.md-06__leave:hover {
  color: var(--ink);
  text-decoration: underline;
}

.md-06__legal {
  font-size: .68rem;
  color: var(--sub);
  line-height: 1.5;
  padding-top: 16px;
  margin-top: 6px;
  border-top: 1px solid var(--line);
}

@media (prefers-reduced-motion: reduce) {
  .md-06__backdrop,
    .md-06__modal {
    transition: none!important;
  }

  .md-06__modal {
    clip-path: none!important;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.querySelector('.md-06');
  if (!root) return;
  var openBtn = root.querySelector('#md-06-open');
  var dialog = root.querySelector('#md-06-dialog');
  var closeBtns = root.querySelectorAll('.md-06__close');
  var lastFocus = null;

  function open() {
    lastFocus = document.activeElement;
    dialog.classList.add('is-open');
    document.documentElement.style.overflow = 'hidden';
    var firstInput = dialog.querySelector('input[autocomplete=bday-month]');
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
