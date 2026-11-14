---
source: "codefronts"
url: "https://codefronts.com/components/css-multi-step-form/account-security-and-kyc-verification-setup/"
title: "Account Security & KYC Verification Setup"
section: "components"
category: "css-multi-step-form"
category_name: "CSS Multi-Step Form UI"
description: "A fintech-grade verification wizard — Identity → Address → 2FA — with an ID-type document selector, and the centerpiece: a proper 6-digit OTP input with…"
has_js: "true"
---

Here's a working CSS Multi-Step Form UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Account Security & KYC Verification Setup
Source: https://codefronts.com/components/css-multi-step-form/account-security-and-kyc-verification-setup/

A fintech-grade verification wizard — Identity → Address → 2FA — with an ID-type document selector, and the centerpiece: a proper 6-digit OTP input with auto-advance, backspace navigation, and full-code paste support. Monospace type and a security checklist rail make the flow feel like a vault, because trust is the product.
## HTML
```html
<section class="msf-14" aria-label="KYC verification demo">
  <form class="msf-14__card" novalidate>
    <aside class="msf-14__rail">
      <span class="msf-14__logo">◉ VAULTPAY</span>
      <ul class="msf-14__checklist">
        <li class="is-active" aria-current="step"><i></i><span>Verify identity</span></li>
        <li><i></i><span>Confirm address</span></li>
        <li><i></i><span>Enable 2FA</span></li>
      </ul>
      <p class="msf-14__note">🔒 Bank-level encryption. Your documents are never stored unencrypted.</p>
    </aside>
    <div class="msf-14__main">
      <fieldset class="msf-14__step">
        <h3 class="msf-14__title" tabindex="-1">Verify your identity</h3>
        <p class="msf-14__sub">Choose a government-issued document.</p>
        <div class="msf-14__docs" role="radiogroup" aria-label="Document type">
          <label class="msf-14__doc"><input type="radio" name="doc" value="Passport" data-hint="Photo page, all corners visible" required><b>🛂</b><span>Passport</span></label>
          <label class="msf-14__doc"><input type="radio" name="doc" value="Driver's license" data-hint="Front and back, glare-free"><b>🪪</b><span>Driver's license</span></label>
          <label class="msf-14__doc"><input type="radio" name="doc" value="National ID" data-hint="Front side, all text legible"><b>🆔</b><span>National ID</span></label>
        </div>
        <p class="msf-14__dochint" aria-live="polite"></p>
        <div class="msf-14__grid">
          <label class="msf-14__field"><span>Legal name (as on document)</span><input type="text" name="name" autocomplete="name" required placeholder="Aria K. Novak"></label>
          <label class="msf-14__field"><span>Document number</span><input type="text" name="docnum" required placeholder="XN4482910" style="font-family:ui-monospace,monospace;letter-spacing:.1em"></label>
        </div>
        <div class="msf-14__nav"><span></span><button type="button" class="msf-14__next">Continue</button></div>
      </fieldset>
      <fieldset class="msf-14__step" hidden>
        <h3 class="msf-14__title" tabindex="-1">Confirm your address</h3>
        <p class="msf-14__sub">Must match a utility bill or bank statement from the last 90 days.</p>
        <div class="msf-14__grid">
          <label class="msf-14__field msf-14__field--full"><span>Street address</span><input type="text" name="addr" autocomplete="street-address" required placeholder="410 Harbor Street, Apt 2C"></label>
          <label class="msf-14__field"><span>City</span><input type="text" name="city" autocomplete="address-level2" required placeholder="Seattle"></label>
          <label class="msf-14__field"><span>Postal code</span><input type="text" name="postal" autocomplete="postal-code" required placeholder="98101"></label>
        </div>
        <div class="msf-14__nav"><button type="button" class="msf-14__back">Back</button><button type="button" class="msf-14__next">Continue</button></div>
      </fieldset>
      <fieldset class="msf-14__step" hidden>
        <h3 class="msf-14__title" tabindex="-1">Enter your verification code</h3>
        <p class="msf-14__sub">We texted a 6-digit code to <b>•••-•••-8842</b>. <span class="msf-14__demo">(Demo: try 482 913)</span></p>
        <div class="msf-14__otp" role="group" aria-label="6-digit verification code">
          <input type="text" inputmode="numeric" maxlength="1" autocomplete="one-time-code" aria-label="Digit 1"><input type="text" inputmode="numeric" maxlength="1" aria-label="Digit 2"><input type="text" inputmode="numeric" maxlength="1" aria-label="Digit 3"><i>–</i><input type="text" inputmode="numeric" maxlength="1" aria-label="Digit 4"><input type="text" inputmode="numeric" maxlength="1" aria-label="Digit 5"><input type="text" inputmode="numeric" maxlength="1" aria-label="Digit 6">
        </div>
        <p class="msf-14__otpmsg" role="alert"></p>
        <p class="msf-14__resend">Didn't get it? <button type="button" class="msf-14__resendbtn">Resend code</button><span class="msf-14__cooldown" aria-live="polite"></span></p>
        <div class="msf-14__nav"><button type="button" class="msf-14__back">Back</button><button type="button" class="msf-14__next msf-14__next--go">Verify &amp; finish</button></div>
      </fieldset>
      <div class="msf-14__done" hidden><b>◉</b><h3 tabindex="-1">Account secured</h3><p>Identity verified · 2FA active. Welcome to VaultPay.</p></div>
    </div>
  </form>
</section>
```
## CSS
```css
.msf-14,
.msf-14 *,
.msf-14 *::before,
.msf-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.msf-14 {
  width: 100%;
  min-height: 100vh;
  --sec: oklch(0.72 0.14 195);
  --bg: oklch(0.15 0.012 240);
  --panel: oklch(0.19 0.014 240);
  --line: oklch(0.3 0.016 240);
  --txt: oklch(0.93 0.004 240);
  --mut: oklch(0.62 0.012 240);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--txt);
  padding: 48px 20px;
  background: var(--bg);
  display: grid;
  place-items: center;
}

.msf-14__card {
  width: min(780px,100%);
  display: grid;
  grid-template-columns: 250px 1fr;
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 18px;
  overflow: hidden;
  box-shadow: 0 40px 90px -40px rgb(0 0 0/.8);
}

@media (max-width: 680px) {
  .msf-14__card {
    grid-template-columns: 1fr;
  }

  .msf-14__rail {
    border-right: none;
    border-bottom: 1px solid var(--line);
  }
}

.msf-14__rail {
  padding: 26px 22px;
  border-right: 1px solid var(--line);
  background: oklch(0.165 0.013 240);
  display: grid;
  gap: 24px;
  align-content: start;
}

.msf-14__logo {
  font-size: 13px;
  font-weight: 800;
  letter-spacing: .18em;
  color: var(--sec);
}

.msf-14__checklist {
  list-style: none;
  display: grid;
  gap: 16px;
}

.msf-14__checklist li {
  display: flex;
  gap: 12px;
  align-items: center;
  font-size: 13.5px;
  font-weight: 600;
  color: var(--mut);
}

.msf-14__checklist i {
  flex: none;
  width: 22px;
  height: 22px;
  border-radius: 50%;
  border: 2px solid var(--line);
  display: grid;
  place-items: center;
  font-size: 11px;
  font-style: normal;
  transition: all .3s;
}

.msf-14__checklist li.is-active {
  color: var(--txt);
}

.msf-14__checklist li.is-active i {
  border-color: var(--sec);
  box-shadow: 0 0 0 4px color-mix(in oklab,var(--sec) 18%,transparent);
}

.msf-14__checklist li.is-done {
  color: var(--sec);
}

.msf-14__checklist li.is-done i {
  background: var(--sec);
  border-color: var(--sec);
  color: var(--bg);
}

.msf-14__checklist li.is-done i::before {
  content: "✓";
  font-weight: 800;
}

.msf-14__note {
  font-size: 12px;
  line-height: 1.55;
  color: var(--mut);
}

.msf-14__main {
  padding: 28px 30px;
}

.msf-14__step {
  border: none;
}

.msf-14__step:not([hidden]) {
  animation: msf-14-in .3s ease;
}

.msf-14__title {
  font-size: 20px;
  letter-spacing: -.01em;
  margin-bottom: 6px;
  outline: none;
}

.msf-14__sub {
  font-size: 13.5px;
  color: var(--mut);
  margin-bottom: 18px;
}

.msf-14__sub b {
  color: var(--txt);
  font-variant-numeric: tabular-nums;
}

.msf-14__demo {
  color: var(--sec);
}

.msf-14__docs {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 10px;
  margin-bottom: 8px;
}

@media (max-width: 480px) {
  .msf-14__docs {
    grid-template-columns: 1fr;
  }
}

.msf-14__doc {
  display: grid;
  justify-items: center;
  gap: 5px;
  padding: 16px 10px;
  border: 1.5px solid var(--line);
  border-radius: 12px;
  cursor: pointer;
  font-size: 13px;
  font-weight: 700;
  transition: all .18s;
}

.msf-14__doc b {
  font-size: 22px;
}

.msf-14__doc input {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.msf-14__doc:hover {
  border-color: color-mix(in oklab,var(--sec) 55%,var(--line));
}

.msf-14__doc:has(:checked) {
  border-color: var(--sec);
  background: color-mix(in oklab,var(--sec) 10%,transparent);
}

.msf-14__doc:has(:focus-visible) {
  outline: 3px solid var(--sec);
  outline-offset: 2px;
}

.msf-14__dochint {
  min-height: 18px;
  font-size: 12px;
  color: var(--sec);
  margin-bottom: 12px;
}

.msf-14__grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 13px;
}

@media (max-width: 480px) {
  .msf-14__grid {
    grid-template-columns: 1fr;
  }
}

.msf-14__field {
  display: grid;
  gap: 6px;
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .03em;
  color: var(--mut);
}

.msf-14__field--full {
  grid-column: 1/-1;
}

.msf-14__field input {
  font: inherit;
  font-weight: 500;
  color: var(--txt);
  padding: 11px 13px;
  background: oklch(0.155 0.012 240);
  border: 1.5px solid var(--line);
  border-radius: 9px;
  transition: border-color .2s,box-shadow .2s;
}

.msf-14__field input:focus-visible {
  outline: none;
  border-color: var(--sec);
  box-shadow: 0 0 0 3px color-mix(in oklab,var(--sec) 20%,transparent);
}

.msf-14__field input[aria-invalid="true"] {
  border-color: oklch(0.65 0.18 25);
}

.msf-14__err {
  grid-column: 1/-1;
  font-size: 12px;
  font-weight: 700;
  color: oklch(0.72 0.15 25);
}

.msf-14__otp {
  display: flex;
  gap: 8px;
  align-items: center;
  margin-bottom: 10px;
}

.msf-14__otp i {
  color: var(--mut);
  font-style: normal;
}

.msf-14__otp input {
  width: 46px;
  height: 56px;
  text-align: center;
  font-family: ui-monospace,monospace;
  font-size: 24px;
  font-weight: 700;
  color: var(--txt);
  background: oklch(0.155 0.012 240);
  border: 1.5px solid var(--line);
  border-radius: 10px;
  caret-color: var(--sec);
  transition: border-color .15s,box-shadow .15s,transform .15s;
}

.msf-14__otp input:focus-visible {
  outline: none;
  border-color: var(--sec);
  box-shadow: 0 0 0 3px color-mix(in oklab,var(--sec) 22%,transparent);
  transform: translateY(-2px);
}

.msf-14__otp.is-bad input {
  border-color: oklch(0.65 0.18 25);
  animation: msf-14-shake .3s;
}

.msf-14__otp.is-good input {
  border-color: var(--sec);
  background: color-mix(in oklab,var(--sec) 10%,oklch(0.155 0.012 240));
}

.msf-14__otpmsg {
  min-height: 18px;
  font-size: 12.5px;
  font-weight: 700;
  color: oklch(0.72 0.15 25);
}

.msf-14__otpmsg.is-good {
  color: var(--sec);
}

.msf-14__resend {
  font-size: 13px;
  color: var(--mut);
  margin-top: 6px;
}

.msf-14__resendbtn {
  font: inherit;
  font-weight: 700;
  color: var(--sec);
  background: none;
  border: none;
  cursor: pointer;
  text-decoration: underline;
  padding: 2px 4px;
}

.msf-14__resendbtn:disabled {
  color: var(--mut);
  text-decoration: none;
  cursor: default;
}

.msf-14__resendbtn:focus-visible {
  outline: 2px solid var(--sec);
  outline-offset: 2px;
}

.msf-14__cooldown {
  font-variant-numeric: tabular-nums;
}

.msf-14__nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 22px;
}

.msf-14__next,
.msf-14__back {
  font: inherit;
  font-weight: 800;
  cursor: pointer;
  border-radius: 9px;
  padding: 12px 24px;
  transition: transform .15s,filter .2s;
}

.msf-14__next {
  border: none;
  color: var(--bg);
  background: var(--sec);
}

.msf-14__next:hover {
  transform: translateY(-1px);
  filter: brightness(1.1);
}

.msf-14__back {
  border: 1.5px solid var(--line);
  background: none;
  color: var(--mut);
}

.msf-14__back:hover {
  color: var(--txt);
}

.msf-14__next:focus-visible,
.msf-14__back:focus-visible {
  outline: 3px solid var(--sec);
  outline-offset: 2px;
}

.msf-14__done[hidden] {
  display: none;
}

.msf-14__done {
  display: grid;
  justify-items: center;
  gap: 8px;
  text-align: center;
  padding: 44px 0;
}

.msf-14__done b {
  display: grid;
  place-items: center;
  width: 54px;
  height: 54px;
  border-radius: 50%;
  background: var(--sec);
  color: var(--bg);
  font-size: 24px;
  animation: msf-14-pop .5s cubic-bezier(.34,1.56,.64,1);
}

.msf-14__done p {
  color: var(--mut);
  font-size: 14px;
}

@keyframes msf-14-in {
  from {
    opacity: 0;
    transform: translateY(8px);
  }

  to {
    opacity: 1;
    transform: none;
  }
}

@keyframes msf-14-pop {
  from {
    transform: scale(.4);
  }

  to {
    transform: scale(1);
  }
}

@keyframes msf-14-shake {
  25% {
    transform: translateX(-4px);
  }

  75% {
    transform: translateX(4px);
  }
}

@media (prefers-reduced-motion: reduce) {
  .msf-14 * {
    animation: none!important;
    transition-duration: .01ms!important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.msf-14'); if (!root) return;
  const form = root.querySelector('.msf-14__card');
  const steps = [...root.querySelectorAll('.msf-14__step')];
  const rail = [...root.querySelectorAll('.msf-14__checklist li')];
  const CODE = '482913';
  let cur = 0;
  const validate = (fs) => {
    let ok = true;
    fs.querySelectorAll('.msf-14__err').forEach(e => e.remove());
    const group = fs.querySelector('[role="radiogroup"]');
    if (group && !group.querySelector(':checked')) {
      const err = document.createElement('p'); err.className='msf-14__err'; err.setAttribute('role','alert');
      err.textContent = 'Choose a document type.'; group.after(err); return false;
    }
    fs.querySelectorAll('.msf-14__field input[required]').forEach(el => {
      const bad = !el.checkValidity(); el.setAttribute('aria-invalid', bad);
      if (bad && ok) { ok = false;
        const err = document.createElement('p'); err.className='msf-14__err'; err.setAttribute('role','alert');
        err.textContent = 'Please complete the highlighted fields.'; el.closest('.msf-14__grid').append(err); el.focus();
      }
    });
    return ok;
  };
  const show = (i) => {
    cur = i;
    steps.forEach((s,k) => s.hidden = k!==i);
    rail.forEach((r,k) => {
      r.classList.toggle('is-active',k===i); r.classList.toggle('is-done',k<i);
      k===i ? r.setAttribute('aria-current','step') : r.removeAttribute('aria-current');
    });
    steps[i].querySelector('.msf-14__title').focus();
  };
  // document hint
  root.addEventListener('change', e => {
    if (e.target.matches('[name="doc"]')) root.querySelector('.msf-14__dochint').textContent = '\ud83d\udcf7 ' + e.target.dataset.hint;
  });
  // ── OTP input ──
  const otp = root.querySelector('.msf-14__otp');
  const boxes = [...otp.querySelectorAll('input')];
  const otpMsg = root.querySelector('.msf-14__otpmsg');
  const value = () => boxes.map(b => b.value).join('');
  const setOtpState = () => {
    const v = value();
    otp.classList.remove('is-bad','is-good'); otpMsg.className = 'msf-14__otpmsg'; otpMsg.textContent = '';
    if (v.length === 6) {
      if (v === CODE) { otp.classList.add('is-good'); otpMsg.className += ' is-good'; otpMsg.textContent = '\u2713 Code verified'; }
      else { otp.classList.add('is-bad'); otpMsg.textContent = 'That code doesn\u2019t match \u2014 check and try again.'; }
    }
  };
  boxes.forEach((box, i) => {
    box.addEventListener('input', () => {
      box.value = box.value.replace(/\D/g,'').slice(-1);
      if (box.value && i < boxes.length-1) boxes[i+1].focus();
      setOtpState();
    });
    box.addEventListener('keydown', e => {
      if (e.key === 'Backspace' && !box.value && i > 0) { boxes[i-1].focus(); boxes[i-1].value=''; setOtpState(); e.preventDefault(); }
      if (e.key === 'ArrowLeft' && i > 0) boxes[i-1].focus();
      if (e.key === 'ArrowRight' && i < boxes.length-1) boxes[i+1].focus();
    });
    box.addEventListener('paste', e => {
      e.preventDefault();
      const digits = (e.clipboardData.getData('text').match(/\d/g) || []).slice(0, boxes.length);
      boxes.forEach((b,k) => b.value = digits[k] || '');
      (boxes[digits.length-1] || boxes[0]).focus();
      setOtpState();
    });
  });
  // resend cooldown
  const resend = root.querySelector('.msf-14__resendbtn'), cd = root.querySelector('.msf-14__cooldown');
  resend.addEventListener('click', () => {
    let t = 30; resend.disabled = true;
    const tick = setInterval(() => {
      cd.textContent = ' \u00b7 new code in ' + t-- + 's';
      if (t < 0) { clearInterval(tick); resend.disabled = false; cd.textContent = ''; }
    }, 1000);
  });
  root.addEventListener('click', e => {
    if (e.target.closest('.msf-14__next:not(.msf-14__next--go):not(.msf-14__submit):not(.msf-14__skip)')) { if (validate(steps[cur])) show(cur+1); }
    if (e.target.closest('.msf-14__back')) show(cur-1);
  });
  root.addEventListener('click', (e) => {
    if (!e.target.closest('.msf-14__next--go, .msf-14__submit, .msf-14__skip')) return;

    e.preventDefault();
    if (value() !== CODE) { otp.classList.add('is-bad'); otpMsg.textContent = value().length < 6 ? 'Enter the 6-digit code we texted you.' : 'That code doesn\u2019t match \u2014 check and try again.'; boxes[0].focus(); return; }
    steps.forEach(s => s.hidden = true);
    rail.forEach(r => { r.classList.add('is-done'); r.classList.remove('is-active'); });
    const done = root.querySelector('.msf-14__done'); done.hidden = false; done.querySelector('h3').focus();
    });
})();
```
