---
source: "codefronts"
url: "https://codefronts.com/layouts/css-footer-designs/contact-card/"
title: "Footer with Integrated Contact Form & Map"
section: "layouts"
category: "css-footer-designs"
category_name: "CSS Footer Designs"
description: "A contact block that lives in the footer without feeling bolted on: a three-field enquiry panel beside a map card with the address and hours."
has_js: "true"
---

Here's a working CSS Footer Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Footer with Integrated Contact Form & Map
Source: https://codefronts.com/layouts/css-footer-designs/contact-card/

A contact block that lives in the footer without feeling bolted on: a three-field enquiry panel beside a map card with the address and hours. Field-level errors, a live character counter, a hidden honeypot for bots, and a success state that replaces the panel rather than appending a toast.
## HTML
```html
<section class="ft-20" aria-label="Footer with contact form and map demo">
  <main class="ft-20__main">
    <p class="ft-20__eyebrow">Field-level errors · honeypot · live counter</p>
    <h1 class="ft-20__title">A contact form that doesn't punish anyone</h1>
    <p class="ft-20__sub">Three fields, real labels, no CAPTCHA. Submit it empty to see how failures are announced and where focus lands.</p>
  </main>
  <footer class="ft-20__foot">
    <div class="ft-20__pair">
      <section class="ft-20__panel" aria-labelledby="ft-20-fh">
        <h2 class="ft-20__h" id="ft-20-fh">Send us a note</h2>
        <p class="ft-20__hsub">We reply within one working day. Urgent? Call <a class="ft-20__inline" href="tel:+35315550188">+353 1 555 0188</a>.</p>
        <div class="ft-20__form" id="ft-20-form">
          <div class="ft-20__field">
            <label class="ft-20__label" for="ft-20-name">Your name</label>
            <input class="ft-20__input" id="ft-20-name" type="text" autocomplete="name" aria-describedby="ft-20-name-err">
            <p class="ft-20__err" id="ft-20-name-err" role="alert" hidden></p>
          </div>
          <div class="ft-20__field">
            <label class="ft-20__label" for="ft-20-email">Email</label>
            <input class="ft-20__input" id="ft-20-email" type="email" inputmode="email" autocomplete="email" aria-describedby="ft-20-email-help ft-20-email-err">
            <p class="ft-20__help" id="ft-20-email-help">We only use it to reply.</p>
            <p class="ft-20__err" id="ft-20-email-err" role="alert" hidden></p>
          </div>
          <div class="ft-20__field">
            <label class="ft-20__label" for="ft-20-msg">How can we help?</label>
            <textarea class="ft-20__area" id="ft-20-msg" rows="3" maxlength="400" aria-describedby="ft-20-msg-count ft-20-msg-err"></textarea>
            <p class="ft-20__help" id="ft-20-msg-count" aria-live="polite">400 characters left</p>
            <p class="ft-20__err" id="ft-20-msg-err" role="alert" hidden></p>
          </div>
          <div class="ft-20__pot" aria-hidden="true"><label for="ft-20-company">Company (leave empty)</label><input id="ft-20-company" type="text" tabindex="-1" autocomplete="off"></div>
          <button class="ft-20__btn" id="ft-20-send" type="button">Send message</button>
          <p class="ft-20__legalnote">By sending you agree to our <a class="ft-20__inline" href="#ft-20-a">privacy notice</a>. No marketing, ever.</p>
        </div>
        <div class="ft-20__done" id="ft-20-done" hidden tabindex="-1">
          <span class="ft-20__check" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" focusable="false"><path d="M4 12.5l5 5L20 6.5"/></svg></span>
          <h3 class="ft-20__doneh">Message sent</h3>
          <p class="ft-20__donep">Your reference is <strong>ENQ-2026-4417</strong>. We have emailed you a copy — check spam if it hasn't arrived in ten minutes.</p>
        </div>
      </section>
      <section class="ft-20__panel ft-20__panel--map" aria-labelledby="ft-20-mh">
        <h2 class="ft-20__h" id="ft-20-mh">Or come to the office</h2>
        <div class="ft-20__map">
          <div class="ft-20__canvas" role="img" aria-label="Map showing the studio at 12 Meeting House Lane, Dublin 8">
            <span class="ft-20__road" aria-hidden="true"></span>
            <span class="ft-20__green" aria-hidden="true"></span>
            <span class="ft-20__pin" aria-hidden="true"></span>
          </div>
        </div>
        <address class="ft-20__addr">12 Meeting House Lane<br>Dublin 8, D08 XH92<br>Ireland</address>
        <dl class="ft-20__hours">
          <div><dt>Mon – Thu</dt><dd><time datetime="09:00">09:00</time> – <time datetime="18:00">18:00</time></dd></div>
          <div><dt>Friday</dt><dd><time datetime="09:00">09:00</time> – <time datetime="16:00">16:00</time></dd></div>
          <div><dt>Weekend</dt><dd>Closed</dd></div>
        </dl>
        <a class="ft-20__dir" href="#ft-20-a">Open in Maps<svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M7 17L17 7M9 7h8v8"/></svg></a>
      </section>
    </div>
    <div class="ft-20__bar">
      <div class="ft-20__brand"><span class="ft-20__mark" aria-hidden="true"></span>Meeting House</div>
      <nav class="ft-20__nav" aria-label="Footer"><a class="ft-20__link" href="#ft-20-a">Work</a><a class="ft-20__link" href="#ft-20-a">Studio</a><a class="ft-20__link" href="#ft-20-a">Careers</a><a class="ft-20__link" href="#ft-20-a">Privacy</a></nav>
      <p class="ft-20__copy">© <time datetime="2026">2026</time> Meeting House Design Ltd · CRO 641129</p>
    </div>
  </footer>
</section>
```
## CSS
```css
.ft-20 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  grid-template-rows: 1fr auto;
  background: var(--ft-20-bg);
  --ft-20-bg: oklch(0.97 0.01 130);
  --ft-20-foot: oklch(0.99 0.005 130);
  --ft-20-panel: oklch(1 0 0);
  --ft-20-ink: oklch(0.22 0.03 155);
  --ft-20-mut: oklch(0.53 0.02 155);
  --ft-20-acc: oklch(0.52 0.14 155);
  --ft-20-bad: oklch(0.52 0.19 25);
  --ft-20-line: oklch(0.22 0.03 155/.12);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--ft-20-ink);
  -webkit-font-smoothing: antialiased;
}

.ft-20 *,
.ft-20 *::before,
.ft-20 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ft-20 [hidden] {
  display: none !important;
}

.ft-20__main {
  display: grid;
  align-content: center;
  gap: 14px;
  padding-block: clamp(36px,7vh,80px);
  padding-inline: max(clamp(20px,5vw,48px),calc((100% - 1160px)/2));
}

.ft-20__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: clamp(11px,1.1vw,12.5px);
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--ft-20-acc);
}

.ft-20__title {
  font-size: clamp(28px,5vw,54px);
  line-height: 1.03;
  letter-spacing: -.04em;
  font-weight: 700;
  max-width: 16ch;
  text-wrap: balance;
}

.ft-20__sub {
  font-size: clamp(15px,1.6vw,18px);
  line-height: 1.6;
  color: var(--ft-20-mut);
  max-width: 54ch;
  text-wrap: pretty;
}

.ft-20__foot {
  background: var(--ft-20-foot);
  border-top: 1px solid var(--ft-20-line);
  padding-inline: max(clamp(20px,5vw,48px),calc((100% - 1160px)/2));
}

.ft-20__pair {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(min(20rem,100%),1fr));
  gap: clamp(14px,2vw,22px);
  padding-block: clamp(28px,4vw,48px);
}

.ft-20__panel {
  display: grid;
  align-content: start;
  gap: 10px;
  padding: clamp(18px,2.4vw,26px);
  border-radius: 20px;
  background: var(--ft-20-panel);
  border: 1px solid var(--ft-20-line);
  box-shadow: 0 20px 44px -34px oklch(0.22 0.03 155/.8);
}

.ft-20__h {
  font-size: clamp(18px,2.1vw,22px);
  font-weight: 690;
  letter-spacing: -.025em;
}

.ft-20__hsub {
  font-size: 13.6px;
  line-height: 1.55;
  color: var(--ft-20-mut);
}

.ft-20__form {
  display: grid;
  gap: 12px;
  margin-block-start: 6px;
}

.ft-20__field {
  display: grid;
  gap: 5px;
}

.ft-20__label {
  font-size: 12.6px;
  font-weight: 650;
  letter-spacing: .01em;
}

.ft-20__input,
.ft-20__area {
  width: 100%;
  padding: 12px 14px;
  border-radius: 12px;
  border: 1px solid var(--ft-20-line);
  background: oklch(0.985 0.005 155);
  color: var(--ft-20-ink);
  font: inherit;
  font-size: 15px;
  transition: border-color .2s ease,box-shadow .2s ease,background .2s ease;
}

.ft-20__input {
  min-height: 48px;
}

.ft-20__area {
  resize: vertical;
  min-height: 88px;
  line-height: 1.5;
}

.ft-20__input:focus-visible,
.ft-20__area:focus-visible {
  outline: none;
  background: var(--ft-20-panel);
  border-color: var(--ft-20-acc);
  box-shadow: 0 0 0 3px color-mix(in oklch,var(--ft-20-acc) 22%,transparent);
}

.ft-20__input[aria-invalid="true"],
.ft-20__area[aria-invalid="true"],
.ft-20__input:user-invalid {
  border-color: var(--ft-20-bad);
  box-shadow: 0 0 0 3px color-mix(in oklch,var(--ft-20-bad) 18%,transparent);
}

.ft-20__help {
  font-size: 12px;
  color: var(--ft-20-mut);
}

.ft-20__err {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 12.5px;
  font-weight: 620;
  color: var(--ft-20-bad);
}

.ft-20__err::before {
  content: '!';
  display: grid;
  place-items: center;
  width: 16px;
  height: 16px;
  flex: none;
  border-radius: 50%;
  background: var(--ft-20-bad);
  color: oklch(1 0 0);
  font-size: 11px;
  font-weight: 800;
}

.ft-20__pot {
  position: absolute;
  left: -9999px;
  width: 1px;
  height: 1px;
  overflow: hidden;
}

.ft-20__btn {
  justify-self: start;
  min-height: 48px;
  margin-block-start: 2px;
  padding: 0 24px;
  border: 0;
  border-radius: 12px;
  background: var(--ft-20-ink);
  color: oklch(1 0 0);
  font: inherit;
  font-size: 15px;
  font-weight: 660;
  cursor: pointer;
  transition: background .2s ease,transform .2s ease,box-shadow .2s ease;
}

.ft-20__btn:hover {
  background: var(--ft-20-acc);
  transform: translateY(-1px);
  box-shadow: 0 12px 26px -14px var(--ft-20-acc);
}

.ft-20__btn:focus-visible,
.ft-20__inline:focus-visible,
.ft-20__dir:focus-visible,
.ft-20__link:focus-visible {
  outline: 2px solid var(--ft-20-acc);
  outline-offset: 3px;
  border-radius: 6px;
}

.ft-20__legalnote {
  font-size: 11.8px;
  line-height: 1.5;
  color: var(--ft-20-mut);
}

.ft-20__inline {
  color: var(--ft-20-acc);
  text-decoration: underline;
  text-underline-offset: .22em;
}

.ft-20__done {
  display: grid;
  justify-items: start;
  gap: 8px;
  padding: 20px;
  border-radius: 16px;
  background: color-mix(in oklch,var(--ft-20-acc) 9%,transparent);
  border: 1px solid color-mix(in oklch,var(--ft-20-acc) 30%,transparent);
  animation: ft-20-in .45s cubic-bezier(.2,.8,.2,1) both;
}

@keyframes ft-20-in {
  from {
    opacity: 0;
    transform: translateY(10px);
  }

  to {
    opacity: 1;
    transform: none;
  }
}

.ft-20__check {
  display: grid;
  place-items: center;
  width: 38px;
  height: 38px;
  border-radius: 50%;
  background: var(--ft-20-acc);
  color: oklch(1 0 0);
}

.ft-20__doneh {
  font-size: 17px;
  font-weight: 690;
  letter-spacing: -.02em;
}

.ft-20__donep {
  font-size: 13.8px;
  line-height: 1.6;
  color: var(--ft-20-mut);
  max-width: 42ch;
}

.ft-20__donep strong {
  color: var(--ft-20-ink);
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .94em;
}

.ft-20__panel--map {
  background: linear-gradient(170deg,oklch(0.99 0.008 155),oklch(0.96 0.014 150));
}

.ft-20__map {
  position: relative;
  aspect-ratio: 16/9;
  border-radius: 14px;
  overflow: hidden;
  border: 1px solid var(--ft-20-line);
}

.ft-20__map iframe {
  width: 100%;
  height: 100%;
  border: 0;
  display: block;
}

.ft-20__canvas {
  position: absolute;
  inset: 0;
  background: oklch(0.955 0.012 120);
  background-image: linear-gradient(oklch(1 0 0) 2px,transparent 2px),linear-gradient(90deg,oklch(1 0 0) 2px,transparent 2px);
  background-size: 30px 30px,30px 30px;
}

.ft-20__road {
  position: absolute;
  left: -10%;
  top: 52%;
  width: 120%;
  height: 12px;
  background: oklch(1 0 0);
  rotate: -7deg;
  box-shadow: 0 0 0 1px oklch(0.22 0.03 155/.06);
}

.ft-20__green {
  position: absolute;
  right: 6%;
  bottom: 8%;
  width: 32%;
  height: 44%;
  background: oklch(0.9 0.07 145);
  border-radius: 44% 56% 50% 50%/48% 42% 58% 52%;
}

.ft-20__pin {
  position: absolute;
  left: 38%;
  top: 44%;
  width: 18px;
  height: 18px;
  translate: -50% -100%;
  background: var(--ft-20-acc);
  border-radius: 50% 50% 50% 0;
  rotate: -45deg;
  border: 2.5px solid oklch(1 0 0);
  box-shadow: 0 6px 14px -6px oklch(0.22 0.03 155/.9);
}

.ft-20__addr {
  font-style: normal;
  font-size: 14.5px;
  line-height: 1.62;
  color: var(--ft-20-mut);
  margin-block-start: 4px;
}

.ft-20__hours {
  display: grid;
  gap: 2px;
  margin-block-start: 4px;
}

.ft-20__hours>div {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 12px;
  padding: 7px 0;
  font-size: 13.6px;
  border-bottom: 1px dashed var(--ft-20-line);
}

.ft-20__hours dt {
  color: var(--ft-20-mut);
}

.ft-20__hours dd {
  font-weight: 640;
  font-variant-numeric: tabular-nums;
}

.ft-20__dir {
  display: inline-flex;
  align-items: center;
  justify-self: start;
  gap: 7px;
  min-height: 42px;
  margin-block-start: 6px;
  font-size: 14px;
  font-weight: 650;
  color: var(--ft-20-acc);
  text-decoration: none;
}

.ft-20__dir:hover {
  text-decoration: underline;
  text-underline-offset: .25em;
}

.ft-20__bar {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 12px 24px;
  padding-block: 20px;
  padding-bottom: calc(20px + env(safe-area-inset-bottom,0px));
  border-top: 1px solid var(--ft-20-line);
}

.ft-20__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 15px;
  font-weight: 700;
  letter-spacing: -.02em;
}

.ft-20__mark {
  width: 21px;
  height: 21px;
  border-radius: 7px;
  background: linear-gradient(140deg,var(--ft-20-acc),oklch(0.72 0.13 120));
}

.ft-20__nav {
  display: flex;
  flex-wrap: wrap;
  gap: 2px;
  margin-inline-start: auto;
}

.ft-20__link {
  display: flex;
  align-items: center;
  min-height: 40px;
  padding: 0 11px;
  border-radius: 9px;
  font-size: 13.5px;
  color: var(--ft-20-mut);
  text-decoration: none;
  transition: color .18s ease,background .18s ease;
}

.ft-20__link:hover {
  color: var(--ft-20-ink);
  background: oklch(0.22 0.03 155/.05);
}

.ft-20__copy {
  font-size: 12.8px;
  color: var(--ft-20-mut);
}

@media (max-width: 760px) {
  .ft-20__nav {
    margin-inline-start: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ft-20 * {
    animation-duration: .01ms !important;
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.ft-20');
  if (!root || root.dataset.ready) return;
  root.dataset.ready = '1';
  const q = (s) => root.querySelector(s);
  const form = q('#ft-20-form'), done = q('#ft-20-done');
  const name = q('#ft-20-name'), email = q('#ft-20-email'), msg = q('#ft-20-msg'), pot = q('#ft-20-company');
  const count = q('#ft-20-msg-count');
  const MAX = 400;
  let lastAnnounced = MAX;
  msg.addEventListener('input', () => {
    const left = MAX - msg.value.length;
    if (left <= 20 || Math.abs(lastAnnounced - left) >= 25) { count.textContent = left + ' characters left'; lastAnnounced = left; }
    else count.textContent = left + ' characters left';
  });
  const setErr = (field, id, message) => {
    const el = root.querySelector(id);
    if (message) { el.textContent = message; el.hidden = false; field.setAttribute('aria-invalid', 'true'); }
    else { el.hidden = true; field.removeAttribute('aria-invalid'); }
    return !message;
  };
  const validate = () => {
    const okName = setErr(name, '#ft-20-name-err', name.value.trim() ? '' : 'Tell us what to call you.');
    const v = email.value.trim();
    const okMail = setErr(email, '#ft-20-email-err', !v ? 'We need an email address to reply to.' : (/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v) ? '' : 'Check the address — it should look like [email protected].'));
    const okMsg = setErr(msg, '#ft-20-msg-err', msg.value.trim().length >= 10 ? '' : 'A sentence or two is plenty — at least 10 characters.');
    return { okName, okMail, okMsg };
  };
  q('#ft-20-send').addEventListener('click', () => {
    if (pot.value) { form.hidden = true; done.hidden = false; return; }
    const r = validate();
    if (!r.okName) return name.focus();
    if (!r.okMail) return email.focus();
    if (!r.okMsg) return msg.focus();
    form.hidden = true; done.hidden = false; done.focus();
  });
  [name, email, msg].forEach((f) => f.addEventListener('blur', () => { if (f.getAttribute('aria-invalid')) validate(); }));
})();
```
