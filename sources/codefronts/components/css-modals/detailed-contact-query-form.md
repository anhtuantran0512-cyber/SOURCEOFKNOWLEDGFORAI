---
source: "codefronts"
url: "https://codefronts.com/components/css-modals/detailed-contact-query-form/"
title: "Detailed Contact / Query Form"
section: "components"
category: "css-modals"
category_name: "CSS Modals"
description: "A multi-field support form that opens over the current dashboard view so users file a query without losing context — name, email, topic, priority and…"
has_js: "true"
---

Here's a working CSS Modal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Detailed Contact / Query Form
Source: https://codefronts.com/components/css-modals/detailed-contact-query-form/

A multi-field support form that opens over the current dashboard view so users file a query without losing context — name, email, topic, priority and message, with inline validation and a success state. Keeps people in flow.
## HTML
```html
<div class="cm-16">
  <button class="cm-16__open" type="button">Contact support</button>

  <dialog class="cm-16__dlg" aria-labelledby="cm-16-title">
    <div class="cm-16__card">
      <header class="cm-16__head">
        <div><h2 id="cm-16-title">Contact support</h2><p class="cm-16__sub">We usually reply within a few hours.</p></div>
        <button class="cm-16__x" type="button" aria-label="Close">&times;</button>
      </header>

      <form class="cm-16__form">
        <div class="cm-16__row">
          <div class="cm-16__field"><label for="cm-16-name">Name</label>
            <input id="cm-16-name" type="text" required autocomplete="name"></div>
          <div class="cm-16__field"><label for="cm-16-email">Email</label>
            <input id="cm-16-email" type="email" required autocomplete="email"></div>
        </div>
        <div class="cm-16__field"><label for="cm-16-topic">Topic</label>
          <select id="cm-16-topic" required>
            <option value="">Choose a topic…</option>
            <option>Billing &amp; plans</option><option>Technical issue</option>
            <option>Feature request</option><option>Something else</option>
          </select>
        </div>
        <fieldset class="cm-16__field cm-16__prio"><legend>Priority</legend>
          <label><input type="radio" name="cm-16-p" checked> Low</label>
          <label><input type="radio" name="cm-16-p"> Normal</label>
          <label><input type="radio" name="cm-16-p"> Urgent</label>
        </fieldset>
        <div class="cm-16__field"><label for="cm-16-msg">Message</label>
          <textarea id="cm-16-msg" required maxlength="500" rows="4" placeholder="Describe what's happening…"></textarea>
          <span class="cm-16__count"><b id="cm-16-c">0</b>/500</span>
        </div>
        <div class="cm-16__actions">
          <button type="button" class="cm-16__cancel">Cancel</button>
          <button type="submit" class="cm-16__submit">Send message</button>
        </div>
      </form>

      <div class="cm-16__done" hidden role="status">
        <div class="cm-16__tick" aria-hidden="true">✓</div>
        <h3>Message sent</h3>
        <p>Thanks — we've logged your request and emailed a copy to your inbox.</p>
        <button type="button" class="cm-16__close2">Close</button>
      </div>
    </div>
  </dialog>
</div>
```
## CSS
```css
.cm-16,
.cm-16 *,
.cm-16 *::before,
.cm-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cm-16 {
  --accent: oklch(0.7 0.15 260);
  font-family: system-ui,'Segoe UI',sans-serif;
  min-height: 100dvh;
  display: grid;
  place-items: center;
  padding: 32px;
  background: radial-gradient(120% 120% at 50% 0%,#0e0f18,#08080d);
}

.cm-16__open {
  cursor: pointer;
  padding: 13px 26px;
  border-radius: 11px;
  color: #e8e9fb;
  font: 600 15px system-ui;
  border: 1px solid color-mix(in oklch,var(--accent) 45%,#2a2c42);
  background: color-mix(in oklch,var(--accent) 14%,#0e0f18);
  transition: background .2s,border-color .2s;
}

.cm-16__open:hover {
  border-color: var(--accent);
  background: color-mix(in oklch,var(--accent) 22%,#0e0f18);
}

.cm-16__open:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.cm-16__dlg {
  margin: auto;
  width: min(500px,94vw);
  padding: 0;
  border: none;
  border-radius: 18px;
  color: #e7e9f4;
  background: linear-gradient(180deg,#15161f,#0f1017);
  box-shadow: 0 40px 90px -30px #000,0 0 0 1px #262838;
  max-block-size: 92dvh;
  overflow: auto;
  opacity: 0;
  transform: translateY(10px) scale(.98);
  transition: opacity .26s,transform .26s,overlay .26s allow-discrete,display .26s allow-discrete;
}

.cm-16__dlg[open] {
  opacity: 1;
  transform: none;
}

@starting-style {
  .cm-16__dlg[open] {
    opacity: 0;
    transform: translateY(10px) scale(.98);
  }
}

.cm-16__dlg::backdrop {
  background: rgba(6,6,10,0);
  backdrop-filter: blur(0);
  transition: background .3s,backdrop-filter .3s,overlay .3s allow-discrete,display .3s allow-discrete;
}

.cm-16__dlg[open]::backdrop {
  background: rgba(6,6,10,.62);
  backdrop-filter: blur(5px);
}

@starting-style {
  .cm-16__dlg[open]::backdrop {
    background: rgba(6,6,10,0);
    backdrop-filter: blur(0);
  }
}

.cm-16__head {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 16px;
  padding: 26px 28px 8px;
}

.cm-16__head h2 {
  font-size: 20px;
  font-weight: 700;
  color: #f2f3fb;
}

.cm-16__sub {
  font-size: 13px;
  color: #8f92a8;
  margin-top: 4px;
}

.cm-16__x {
  width: 34px;
  height: 34px;
  border: none;
  border-radius: 8px;
  background: transparent;
  color: #888ba0;
  font-size: 22px;
  cursor: pointer;
  flex: none;
}

.cm-16__x:hover {
  background: #1e2030;
  color: #fff;
}

.cm-16__x:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.cm-16__form {
  padding: 16px 28px 26px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.cm-16__row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px;
}

.cm-16__field {
  display: flex;
  flex-direction: column;
  gap: 7px;
  position: relative;
}

.cm-16__field label,
.cm-16__field legend {
  font-size: 12.5px;
  font-weight: 600;
  color: #aab0c4;
}

.cm-16__field input,
.cm-16__field select,
.cm-16__field textarea {
  width: 100%;
  padding: 11px 13px;
  border-radius: 10px;
  border: 1px solid #2b2e42;
  background: #0c0d14;
  color: #eef0f7;
  font: 14px system-ui;
  transition: border-color .2s,box-shadow .2s;
}

.cm-16__field textarea {
  resize: vertical;
  min-height: 92px;
}

.cm-16__field input:focus,
.cm-16__field select:focus,
.cm-16__field textarea:focus {
  outline: none;
  border-color: var(--accent);
  box-shadow: 0 0 0 3px color-mix(in oklch,var(--accent) 26%,transparent);
}

.cm-16__field input:user-invalid,
.cm-16__field textarea:user-invalid,
.cm-16__field select:user-invalid {
  border-color: oklch(0.62 0.2 22);
}

.cm-16__prio {
  border: none;
}

.cm-16__prio {
  flex-direction: row;
  align-items: center;
  gap: 18px;
  flex-wrap: wrap;
}

.cm-16__prio legend {
  flex-basis: 100%;
}

.cm-16__prio label {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  font-size: 14px;
  color: #c6cbdb;
  cursor: pointer;
  font-weight: 400;
}

.cm-16__prio input {
  accent-color: var(--accent);
  width: 16px;
  height: 16px;
}

.cm-16__count {
  position: absolute;
  right: 2px;
  bottom: -20px;
  font-size: 11.5px;
  color: #787c92;
}

.cm-16__count b {
  color: #adb2c5;
}

.cm-16__actions {
  display: flex;
  justify-content: flex-end;
  gap: 12px;
  margin-top: 14px;
}

.cm-16__cancel {
  padding: 12px 20px;
  border-radius: 10px;
  border: 1px solid #2f3247;
  background: #171826;
  color: #d6dae8;
  font: 600 14px system-ui;
  cursor: pointer;
  transition: all .18s;
}

.cm-16__cancel:hover {
  background: #1e2032;
}

.cm-16__submit {
  padding: 12px 22px;
  border: none;
  border-radius: 10px;
  background: var(--accent);
  color: #080615;
  font: 700 14px system-ui;
  cursor: pointer;
  transition: filter .2s,transform .1s;
}

.cm-16__submit:hover {
  filter: brightness(1.08);
}

.cm-16__submit:active {
  transform: translateY(1px);
}

.cm-16__cancel:focus-visible,
.cm-16__submit:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 2px;
}

.cm-16__done {
  padding: 44px 30px;
  text-align: center;
}

.cm-16__tick {
  width: 60px;
  height: 60px;
  margin: 0 auto 18px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  font-size: 28px;
  color: #0a1410;
  background: oklch(0.82 0.16 155);
  box-shadow: 0 0 44px -8px oklch(0.82 0.16 155);
  animation: cm-16-pop .4s cubic-bezier(.2,1.4,.4,1) both;
}

@keyframes cm-16-pop {
  from {
    transform: scale(.3);
    opacity: 0;
  }

  to {
    transform: scale(1);
    opacity: 1;
  }
}

.cm-16__done h3 {
  font-size: 20px;
  font-weight: 700;
  color: #f2f3fb;
  margin-bottom: 8px;
}

.cm-16__done p {
  font-size: 14px;
  line-height: 1.6;
  color: #9599ad;
  max-width: 32ch;
  margin: 0 auto 22px;
}

.cm-16__close2 {
  padding: 12px 28px;
  border: none;
  border-radius: 10px;
  background: var(--accent);
  color: #080615;
  font: 700 14px system-ui;
  cursor: pointer;
}

.cm-16__close2:hover {
  filter: brightness(1.08);
}

.cm-16__close2:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 2px;
}

@media (max-width: 480px) {
  .cm-16__row {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cm-16__dlg,
    .cm-16__dlg::backdrop {
    transition-duration: .001s;
  }

  .cm-16__tick {
    animation: none;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.querySelector('.cm-16');
  var dlg = root.querySelector('.cm-16__dlg');
  var form = root.querySelector('.cm-16__form');
  var done = root.querySelector('.cm-16__done');
  var msg = root.querySelector('#cm-16-msg');
  var count = root.querySelector('#cm-16-c');
  function reset(){ form.hidden = false; done.hidden = true; }
  root.querySelector('.cm-16__open').addEventListener('click', function(){ reset(); dlg.showModal(); });
  root.querySelector('.cm-16__x').addEventListener('click', function(){ dlg.close(); });
  root.querySelector('.cm-16__cancel').addEventListener('click', function(){ dlg.close(); });
  root.querySelector('.cm-16__close2').addEventListener('click', function(){ dlg.close(); });
  msg.addEventListener('input', function(){ count.textContent = msg.value.length; });
  form.addEventListener('submit', function(e){
    e.preventDefault();
    if(!form.checkValidity()){ form.reportValidity(); return; }
    form.hidden = true; done.hidden = false;
    root.querySelector('.cm-16__close2').focus();
  });
  dlg.addEventListener('close', reset);
})();
```
