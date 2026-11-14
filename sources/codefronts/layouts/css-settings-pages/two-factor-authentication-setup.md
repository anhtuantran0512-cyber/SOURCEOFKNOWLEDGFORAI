---
source: "codefronts"
url: "https://codefronts.com/layouts/css-settings-pages/two-factor-authentication-setup/"
title: "Two-Factor Authentication Setup"
section: "layouts"
category: "css-settings-pages"
category_name: "CSS Settings Pages"
description: "A guided, three-step 2FA enrolment wizard: choose authenticator app or SMS, scan a QR code (with a copyable manual setup key fallback), enter a 6-digit code…"
has_js: "true"
---

Here's a working CSS Settings Page from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Two-Factor Authentication Setup
Source: https://codefronts.com/layouts/css-settings-pages/two-factor-authentication-setup/

A guided, three-step 2FA enrolment wizard: choose authenticator app or SMS, scan a QR code (with a copyable manual setup key fallback), enter a 6-digit code in a premium OTP input that auto-advances, supports paste and backspace, and shakes on error — then save recovery codes with copy and download before finishing. A progress stepper with aria-current keeps users oriented.
## HTML
```html
<section class="csp-10" data-step="1">
  <form class="csp-10__card" data-form novalidate>
    <ol class="csp-10__steps" aria-label="Setup progress">
      <li class="csp-10__dot"><span>1</span>Method</li>
      <li class="csp-10__dot"><span>2</span>Verify</li>
      <li class="csp-10__dot"><span>3</span>Backup</li>
    </ol>

    <div class="csp-10__panel" data-panel="1">
      <h1 tabindex="-1">Secure your account</h1>
      <p class="csp-10__lead">Add a second step at sign-in. Even if your password leaks, your account stays locked.</p>
      <fieldset class="csp-10__methods">
        <legend class="csp-10__sr">Choose a method</legend>
        <label class="csp-10__method"><input type="radio" name="csp10-m" value="app" checked><span class="csp-10__mi">⌘</span><span><b>Authenticator app <em>Recommended</em></b><small>1Password, Google Authenticator, Authy, Microsoft Authenticator</small></span></label>
        <label class="csp-10__method"><input type="radio" name="csp10-m" value="sms"><span class="csp-10__mi">✉</span><span><b>Text message (SMS)</b><small>Receive a code on your phone. Less secure than an app.</small></span></label>
      </fieldset>
      <div class="csp-10__actions"><button type="button" class="csp-10__btn" data-next>Continue</button></div>
    </div>

    <div class="csp-10__panel" data-panel="2">
      <h1 tabindex="-1">Scan and verify</h1>
      <div class="csp-10__scan">
        <div class="csp-10__qr" data-qr aria-label="QR code for authenticator app" role="img"></div>
        <div class="csp-10__scantext">
          <p>Scan this code with your authenticator app, then enter the 6-digit code it shows.</p>
          <p class="csp-10__keylabel">Can't scan? Enter this key:</p>
          <div class="csp-10__key"><code>JBSW Y3DP EHPK 3PXP</code><button type="button" data-copykey>Copy</button></div>
        </div>
      </div>
      <fieldset class="csp-10__otp" data-otp>
        <legend>Verification code</legend>
        <div class="csp-10__boxes">
          <input inputmode="numeric" autocomplete="one-time-code" maxlength="1" aria-label="Digit 1">
          <input inputmode="numeric" maxlength="1" aria-label="Digit 2">
          <input inputmode="numeric" maxlength="1" aria-label="Digit 3">
          <span class="csp-10__sep" aria-hidden="true"></span>
          <input inputmode="numeric" maxlength="1" aria-label="Digit 4">
          <input inputmode="numeric" maxlength="1" aria-label="Digit 5">
          <input inputmode="numeric" maxlength="1" aria-label="Digit 6">
        </div>
        <p class="csp-10__msg" data-msg aria-live="polite">Demo: any 6 digits verify — try 000000 to see the error state.</p>
      </fieldset>
      <div class="csp-10__actions"><button type="button" class="csp-10__ghost" data-back>Back</button><button type="button" class="csp-10__btn" data-verify disabled>Verify code</button></div>
    </div>

    <div class="csp-10__panel" data-panel="3">
      <h1 tabindex="-1">Save your recovery codes</h1>
      <p class="csp-10__lead">If you lose your phone, each code signs you in once. Store them somewhere safe.</p>
      <ol class="csp-10__codes" data-codes></ol>
      <div class="csp-10__codeact"><button type="button" class="csp-10__ghost" data-copycodes>Copy codes</button><button type="button" class="csp-10__ghost" data-dlcodes>Download .txt</button></div>
      <label class="csp-10__ack"><input type="checkbox" data-ack> I've saved my recovery codes</label>
      <div class="csp-10__actions"><button type="button" class="csp-10__btn" data-finish disabled>Finish setup</button></div>
    </div>

    <div class="csp-10__panel csp-10__done" data-panel="4">
      <span class="csp-10__check" aria-hidden="true"></span>
      <h1 tabindex="-1">Two-factor authentication is on</h1>
      <p class="csp-10__lead">You'll be asked for a code when you sign in on a new device.</p>
    </div>
  </form>
</section>
```
## CSS
```css
.csp-10,
.csp-10 *,
.csp-10 *::before,
.csp-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.csp-10 {
  --bg: oklch(0.97 0.008 275);
  --surface: #fff;
  --ink: oklch(0.21 0.025 275);
  --muted: oklch(0.5 0.02 275);
  --line: oklch(0.91 0.01 275);
  --accent: oklch(0.52 0.21 275);
  --ok: oklch(0.58 0.15 155);
  --bad: oklch(0.57 0.21 25);
  color-scheme: light;
  display: grid;
  align-items: center;
  justify-items: center;
  min-height: 100vh;
  min-height: 100dvh;
  padding: 40px 18px;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: radial-gradient(70% 60% at 50% -10%,oklch(0.9 0.06 275/.8),transparent),var(--bg);
  color: var(--ink);
  accent-color: var(--accent);
  width: 100%;
}

.csp-10__sr {
  position: absolute!important;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.csp-10__card {
  width: min(520px,100%);
  padding: 30px;
  border-radius: 24px;
  background: var(--surface);
  border: 1px solid var(--line);
  box-shadow: 0 30px 70px -40px oklch(0.3 0.1 275/.5);
}

.csp-10__steps {
  list-style: none;
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 8px;
  margin-bottom: 26px;
  counter-reset: s;
}

.csp-10__dot {
  position: relative;
  display: flex;
  flex-direction: column;
  gap: 8px;
  font: 600 12px/1 system-ui,sans-serif;
  color: var(--muted);
}

.csp-10__dot::before {
  content: "";
  height: 4px;
  border-radius: 999px;
  background: var(--line);
  transition: background .3s;
}

.csp-10__dot span {
  display: none;
}

.csp-10[data-step="1"] .csp-10__dot:nth-child(-n+1)::before,
.csp-10[data-step="2"] .csp-10__dot:nth-child(-n+2)::before,
.csp-10[data-step="3"] .csp-10__dot:nth-child(-n+3)::before,
.csp-10[data-step="4"] .csp-10__dot::before {
  background: var(--accent);
}

.csp-10[data-step="1"] .csp-10__dot:nth-child(1),
.csp-10[data-step="2"] .csp-10__dot:nth-child(2),
.csp-10[data-step="3"] .csp-10__dot:nth-child(3) {
  color: var(--ink);
}

.csp-10[data-step="4"] .csp-10__steps {
  display: none;
}

.csp-10__panel {
  display: none;
  flex-direction: column;
  gap: 18px;
  animation: csp10-in .35s cubic-bezier(.2,.8,.2,1);
}

.csp-10[data-step="1"] [data-panel="1"],
.csp-10[data-step="2"] [data-panel="2"],
.csp-10[data-step="3"] [data-panel="3"],
.csp-10[data-step="4"] [data-panel="4"] {
  display: flex;
}

.csp-10__panel h1 {
  font: 700 24px/1.15 system-ui,sans-serif;
  letter-spacing: -.02em;
  outline: none;
}

.csp-10__lead {
  font: 400 14.5px/1.55 system-ui,sans-serif;
  color: var(--muted);
  text-wrap: pretty;
}

.csp-10__methods {
  border: 0;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.csp-10__method {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 14px;
  border: 1px solid var(--line);
  border-radius: 14px;
  cursor: pointer;
  transition: border-color .15s,box-shadow .15s,background .15s;
}

.csp-10__method input {
  width: 18px;
  height: 18px;
  flex: none;
  order: 3;
  margin-left: auto;
}

.csp-10__method:has(input:checked) {
  border-color: var(--accent);
  background: oklch(0.98 0.012 275);
  box-shadow: 0 0 0 1px var(--accent);
}

.csp-10__method:has(input:focus-visible) {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.csp-10__mi {
  flex: none;
  display: grid;
  place-items: center;
  width: 42px;
  height: 42px;
  border-radius: 12px;
  font: 600 18px/1 system-ui,sans-serif;
  color: var(--accent);
  background: oklch(0.95 0.03 275);
}

.csp-10__method span:not(.csp-10__mi) {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.csp-10__method b {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
  font: 600 14.5px/1.2 system-ui,sans-serif;
}

.csp-10__method em {
  font: 650 10.5px/1 system-ui,sans-serif;
  font-style: normal;
  padding: 3px 7px;
  border-radius: 999px;
  color: var(--ok);
  background: oklch(0.95 0.04 155);
}

.csp-10__method small {
  font: 400 12.5px/1.4 system-ui,sans-serif;
  color: var(--muted);
}

.csp-10__scan {
  display: flex;
  gap: 20px;
  align-items: center;
}

.csp-10__qr {
  flex: none;
  display: grid;
  grid-template-columns: repeat(21,1fr);
  width: 148px;
  aspect-ratio: 1;
  padding: 10px;
  border-radius: 14px;
  background: #fff;
  border: 1px solid var(--line);
  box-shadow: 0 6px 18px -10px oklch(0 0 0/.25);
}

.csp-10__qr i {
  background: var(--ink);
  border-radius: 1px;
}

.csp-10__qr i.o {
  background: transparent;
}

.csp-10__scantext {
  display: flex;
  flex-direction: column;
  gap: 8px;
  min-width: 0;
  font: 400 14px/1.5 system-ui,sans-serif;
  color: var(--muted);
}

.csp-10__keylabel {
  font-weight: 600;
  color: var(--ink);
  font-size: 13px;
  margin-top: 4px;
}

.csp-10__key {
  display: flex;
  align-items: center;
  gap: 6px;
}

.csp-10__key code {
  flex: 1;
  min-width: 0;
  padding: 8px 10px;
  border-radius: 8px;
  background: var(--bg);
  font: 600 12.5px/1 ui-monospace,Menlo,monospace;
  letter-spacing: .06em;
  color: var(--ink);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.csp-10__key button {
  min-height: 32px;
  padding: 0 10px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: var(--surface);
  font: 600 12px/1 system-ui,sans-serif;
  color: var(--ink);
  cursor: pointer;
}

.csp-10__otp {
  border: 0;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.csp-10__otp legend {
  font: 600 13.5px/1 system-ui,sans-serif;
  margin-bottom: 10px;
}

.csp-10__boxes {
  display: flex;
  align-items: center;
  gap: 8px;
}

.csp-10__boxes input {
  width: 100%;
  max-width: 56px;
  aspect-ratio: .86;
  border: 1.5px solid var(--line);
  border-radius: 12px;
  background: var(--surface);
  text-align: center;
  font: 650 24px/1 ui-monospace,Menlo,monospace;
  color: var(--ink);
  caret-color: var(--accent);
  transition: border-color .15s,box-shadow .15s,background .15s;
}

.csp-10__boxes input:focus {
  outline: none;
  border-color: var(--accent);
  box-shadow: 0 0 0 4px oklch(0.52 0.21 275/.16);
}

.csp-10__boxes input:not(:placeholder-shown) {
  background: oklch(0.98 0.01 275);
}

.csp-10__sep {
  flex: 0 0 10px;
  height: 2px;
  border-radius: 2px;
  background: var(--line);
}

.csp-10__otp.is-error input {
  border-color: var(--bad);
}

.csp-10__otp.is-error .csp-10__boxes {
  animation: csp10-shake .4s;
}

.csp-10__otp.is-error .csp-10__msg {
  color: var(--bad);
}

.csp-10__otp.is-ok input {
  border-color: var(--ok);
  background: oklch(0.97 0.03 155);
}

.csp-10__msg {
  font: 400 12.5px/1.4 system-ui,sans-serif;
  color: var(--muted);
}

.csp-10__codes {
  list-style: none;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
  padding: 16px;
  border-radius: 14px;
  background: var(--bg);
  border: 1px dashed oklch(0.85 0.02 275);
  counter-reset: c;
}

.csp-10__codes li {
  counter-increment: c;
  display: flex;
  gap: 10px;
  font: 600 14px/1.4 ui-monospace,Menlo,monospace;
  letter-spacing: .04em;
}

.csp-10__codes li::before {
  content: counter(c,decimal-leading-zero);
  color: var(--muted);
  font-weight: 400;
}

.csp-10__codeact {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}

.csp-10__ack {
  display: flex;
  align-items: center;
  gap: 10px;
  min-height: 44px;
  font: 500 14px/1.3 system-ui,sans-serif;
  cursor: pointer;
}

.csp-10__ack input {
  width: 18px;
  height: 18px;
}

.csp-10__actions {
  display: flex;
  justify-content: flex-end;
  gap: 8px;
  padding-top: 4px;
}

.csp-10__btn,
.csp-10__ghost {
  min-height: 46px;
  padding: 0 20px;
  border-radius: 12px;
  font: 650 14px/1 system-ui,sans-serif;
  cursor: pointer;
  transition: background .15s,opacity .15s;
}

.csp-10__btn {
  border: 0;
  color: #fff;
  background: var(--accent);
}

.csp-10__btn:hover:not(:disabled) {
  background: oklch(0.47 0.21 275);
}

.csp-10__btn:disabled {
  opacity: .4;
  cursor: not-allowed;
}

.csp-10__ghost {
  border: 1px solid var(--line);
  background: var(--surface);
  color: var(--ink);
}

.csp-10__ghost:hover {
  background: var(--bg);
}

.csp-10 button:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.csp-10__done {
  align-items: center;
  text-align: center;
  padding: 12px 0;
}

.csp-10__check {
  width: 72px;
  height: 72px;
  border-radius: 50%;
  background: var(--ok) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='m6 12.5 4 4 8-9' fill='none' stroke='white' stroke-width='2.4' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/40px no-repeat;
  box-shadow: 0 0 0 10px oklch(0.58 0.15 155/.14);
  animation: csp10-pop .5s cubic-bezier(.3,.7,.3,1.5);
}

@keyframes csp10-in {
  from {
    opacity: 0;
    translate: 12px 0;
  }
}

@keyframes csp10-shake {
  20%,
    60% {
    translate: -6px 0;
  }

  40%,
    80% {
    translate: 6px 0;
  }
}

@keyframes csp10-pop {
  from {
    scale: .4;
    opacity: 0;
  }
}

@media (max-width: 480px) {
  .csp-10__scan {
    flex-direction: column;
    align-items: flex-start;
  }

  .csp-10__card {
    padding: 22px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .csp-10 * {
    animation: none!important;
    transition: none!important;
  }
}
```

## JavaScript
```js
(function () {
  var root = document.querySelector('.csp-10');
  var boxes = Array.prototype.slice.call(root.querySelectorAll('.csp-10__boxes input'));
  var otp = root.querySelector('[data-otp]'), msg = root.querySelector('[data-msg]');
  var verify = root.querySelector('[data-verify]');
  boxes.forEach(function (b) { b.placeholder = ' '; });

  function go(n) {
    root.dataset.step = n;
    var h = root.querySelector('[data-panel="' + n + '"] h1'); if (h) h.focus();
    if (n === 2) setTimeout(function () { boxes[0].focus(); }, 50);
  }
  root.querySelector('[data-next]').addEventListener('click', function () { go(2); });
  root.querySelector('[data-back]').addEventListener('click', function () { go(1); });

  var qr = root.querySelector('[data-qr]'), seed = 7;
  for (var y = 0; y < 21; y++) for (var x = 0; x < 21; x++) {
    var i = document.createElement('i');
    var finder = function (cx, cy) { var dx = x - cx, dy = y - cy; if (dx < 0 || dy < 0 || dx > 6 || dy > 6) return null; return dx === 0 || dy === 0 || dx === 6 || dy === 6 || (dx > 1 && dx < 5 && dy > 1 && dy < 5); };
    var f = finder(0, 0); if (f === null) f = finder(14, 0); if (f === null) f = finder(0, 14);
    seed = (seed * 9301 + 49297) % 233280;
    var on = f === null ? (seed / 233280) > 0.52 : f;
    if (!on) i.className = 'o';
    qr.appendChild(i);
  }

  function code() { return boxes.map(function (b) { return b.value; }).join(''); }
  function check() { otp.classList.remove('is-error'); verify.disabled = code().length !== 6; }
  function spread(text) {
    var d = (text || '').replace(/\D/g, '').slice(0, 6).split('');
    boxes.forEach(function (b, i) { b.value = d[i] || ''; });
    boxes[Math.min(d.length, 5)].focus(); check();
  }
  boxes.forEach(function (b, i) {
    b.addEventListener('input', function () {
      if (b.value.length > 1) return spread(b.value);
      b.value = b.value.replace(/\D/g, '');
      if (b.value && boxes[i + 1]) boxes[i + 1].focus();
      check();
    });
    b.addEventListener('keydown', function (e) {
      if (e.key === 'Backspace' && !b.value && boxes[i - 1]) { boxes[i - 1].focus(); boxes[i - 1].value = ''; check(); }
      if (e.key === 'ArrowLeft' && boxes[i - 1]) boxes[i - 1].focus();
      if (e.key === 'ArrowRight' && boxes[i + 1]) boxes[i + 1].focus();
      if (e.key === 'Enter' && !verify.disabled) verify.click();
    });
    b.addEventListener('focus', function () { b.select(); });
    b.addEventListener('paste', function (e) { e.preventDefault(); spread(e.clipboardData.getData('text')); });
  });

  verify.addEventListener('click', function () {
    verify.disabled = true; verify.textContent = 'Verifying…';
    setTimeout(function () {
      verify.textContent = 'Verify code';
      if (code() === '000000') {
        otp.classList.remove('is-error'); void otp.offsetWidth; otp.classList.add('is-error');
        msg.textContent = 'That code didn\'t match. Check your app and try again.';
        boxes.forEach(function (b) { b.value = ''; }); boxes[0].focus();
      } else {
        otp.classList.add('is-ok'); msg.textContent = 'Code verified.';
        setTimeout(function () { go(3); }, 500);
      }
    }, 700);
  });

  var list = root.querySelector('[data-codes]'), codes = [];
  for (var k = 0; k < 8; k++) {
    var a = new Uint8Array(4); crypto.getRandomValues(a);
    var s = Array.prototype.map.call(a, function (n) { return ('0' + n.toString(36)).slice(-2); }).join('');
    codes.push(s.slice(0, 4) + '-' + s.slice(4, 8));
  }
  codes.forEach(function (c) { var li = document.createElement('li'); li.textContent = c; list.appendChild(li); });
  root.querySelector('[data-copycodes]').addEventListener('click', function (e) {
    if (navigator.clipboard) navigator.clipboard.writeText(codes.join('\n')).catch(function () {});
    e.currentTarget.textContent = 'Copied ✓';
  });
  root.querySelector('[data-dlcodes]').addEventListener('click', function () {
    var url = URL.createObjectURL(new Blob(['Northwind recovery codes\n\n' + codes.join('\n')], { type: 'text/plain' }));
    var a = document.createElement('a'); a.href = url; a.download = 'northwind-recovery-codes.txt'; document.body.appendChild(a); a.click(); a.remove();
    setTimeout(function () { URL.revokeObjectURL(url); }, 1000);
  });
  root.querySelector('[data-copykey]').addEventListener('click', function (e) {
    if (navigator.clipboard) navigator.clipboard.writeText('JBSWY3DPEHPK3PXP').catch(function () {});
    e.currentTarget.textContent = 'Copied';
  });
  var ack = root.querySelector('[data-ack]'), finish = root.querySelector('[data-finish]');
  ack.addEventListener('change', function () { finish.disabled = !ack.checked; });
  finish.addEventListener('click', function () { go(4); });
})();
```
