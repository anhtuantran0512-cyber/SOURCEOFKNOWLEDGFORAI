---
source: "codefronts"
url: "https://codefronts.com/components/css-forms/contact-form-with-character-counter/"
title: "Contact Form with Character Counter"
section: "components"
category: "css-forms"
category_name: "CSS Forms"
description: "A contact form that respects the person typing: a textarea that grows with field-sizing:content, a circular counter ring driven by a registered @property…"
has_js: "true"
---

Here's a working CSS Form from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Contact Form with Character Counter
Source: https://codefronts.com/components/css-forms/contact-form-with-character-counter/

A contact form that respects the person typing: a textarea that grows with field-sizing:content, a circular counter ring driven by a registered @property that shifts from calm to amber to red as the limit approaches, screen-reader announcements only at meaningful thresholds (not every keystroke), topic chips built from real radios, and :user-invalid errors that wait until the user has actually left a field.
## HTML
```html
<div class="frm-01">
  <button type="button" class="frm-01__theme" data-theme-toggle aria-label="Dark mode" aria-pressed="false" title="Switch to dark mode"><svg class="frm-01__moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5Z"/></svg><svg class="frm-01__sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg></button>
  <div class="frm-01__stage">
    <div class="frm-01__card" role="form" aria-labelledby="frm-01-title">
      <header class="frm-01__head">
        <p class="frm-01__eyebrow">Get in touch</p>
        <h2 id="frm-01-title" class="frm-01__title">Tell us what you're <em>building.</em></h2>
        <p class="frm-01__lede">We reply to every message within one business day. Fields marked <span aria-hidden="true">*</span><span class="frm-01__sr">with an asterisk</span> are required.</p>
      </header>
      <div class="frm-01__body">
        <div class="frm-01__grid">
          <div class="frm-01__field">
            <label for="frm-01-name">Full name <span aria-hidden="true">*</span></label>
            <input id="frm-01-name" name="name" type="text" autocomplete="name" required placeholder="Ada Lovelace" aria-describedby="frm-01-name-err">
            <p class="frm-01__err" id="frm-01-name-err"><svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="7"/><path d="M8 4.5v4M8 11h.01"/></svg>Please enter your name.</p>
          </div>
          <div class="frm-01__field">
            <label for="frm-01-email">Work email <span aria-hidden="true">*</span></label>
            <input id="frm-01-email" name="email" type="email" autocomplete="email" required placeholder="[email protected]" aria-describedby="frm-01-email-err">
            <p class="frm-01__err" id="frm-01-email-err"><svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="7"/><path d="M8 4.5v4M8 11h.01"/></svg>Enter an email like [email protected].</p>
          </div>
        </div>
        <fieldset class="frm-01__chips">
          <legend>What's this about?</legend>
          <label><input type="radio" name="frm-01-topic" value="project" checked><span>New project</span></label>
          <label><input type="radio" name="frm-01-topic" value="support"><span>Support</span></label>
          <label><input type="radio" name="frm-01-topic" value="press"><span>Press</span></label>
          <label><input type="radio" name="frm-01-topic" value="careers"><span>Careers</span></label>
          <label><input type="radio" name="frm-01-topic" value="other"><span>Something else</span></label>
        </fieldset>
        <div class="frm-01__field">
          <div class="frm-01__labelrow">
            <label for="frm-01-msg">Message <span aria-hidden="true">*</span></label>
            <div class="frm-01__counter" data-state="ok" aria-hidden="true">
              <span class="frm-01__ring"></span>
              <span class="frm-01__count"><b class="frm-01__n">0</b> / <span class="frm-01__max">500</span></span>
            </div>
          </div>
          <textarea id="frm-01-msg" name="message" required minlength="20" data-max="500" placeholder="A few sentences on goals, timeline and budget help us route you to the right person." aria-describedby="frm-01-msg-hint frm-01-msg-err"></textarea>
          <p class="frm-01__hint" id="frm-01-msg-hint">Minimum 20 characters. <span class="frm-01__left">500 characters remaining.</span></p>
          <p class="frm-01__err" id="frm-01-msg-err"><svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="7"/><path d="M8 4.5v4M8 11h.01"/></svg><span class="frm-01__msgerr">Write at least 20 characters.</span></p>
          <p class="frm-01__sr" aria-live="polite" id="frm-01-live"></p>
        </div>
        <div class="frm-01__foot">
          <label class="frm-01__check"><input type="checkbox" name="copy"><span>Send me a copy of this message</span></label>
          <button class="frm-01__send" type="button">
            <span>Send message</span>
            <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12 20 4l-5 16-3-7-8-1Z"/></svg>
          </button>
        </div>
      </div>
      <div class="frm-01__done" hidden tabindex="-1">
        <span class="frm-01__tick" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg></span>
        <h3>Message sent.</h3>
        <p>Thanks — a real person will reply within one business day.</p>
        <button class="frm-01__again" type="button">Send another</button>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Geist:wght@400;500;600&display=swap');

@property --frm-01-p {
  syntax: '<number>';
  inherits: true;
  initial-value: 0;
}

.frm-01 {
  --bg: #f3eee5;
  --card: #fffdf9;
  --field: #faf7f1;
  --ink: #1c1915;
  --muted: #6a6257;
  --line: #e2d9c9;
  --accent: #c2410c;
  --on-accent: #fff;
  --ok: #3f6212;
  --warn: #b45309;
  --bad: #b91c1c;
  --serif: "Instrument Serif",ui-serif,Georgia,serif;
  --sans: "Geist",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --ease: cubic-bezier(.16,1,.3,1);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: radial-gradient(60rem 40rem at 110% -10%, color-mix(in oklab,var(--accent) 14%,transparent), transparent 60%), radial-gradient(50rem 30rem at -20% 110%, color-mix(in oklab,#a16207 12%,transparent), transparent 60%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@media (prefers-color-scheme: dark) {
  .frm-01:not([data-theme="light"]) {
    --bg: #14120f;
    --card: #1d1a16;
    --field: #24201b;
    --ink: #f3ede4;
    --muted: #a59c8f;
    --line: #3a342c;
    --accent: #fb923c;
    --on-accent: #1c0d02;
    --ok: #a3e635;
    --warn: #fbbf24;
    --bad: #f87171;
  }
}

.frm-01[data-theme="dark"] {
  --bg: #14120f;
  --card: #1d1a16;
  --field: #24201b;
  --ink: #f3ede4;
  --muted: #a59c8f;
  --line: #3a342c;
  --accent: #fb923c;
  --on-accent: #1c0d02;
  --ok: #a3e635;
  --warn: #fbbf24;
  --bad: #f87171;
}

.frm-01,
.frm-01 *,
.frm-01 *::before,
.frm-01 *::after {
  box-sizing: border-box;
}

.frm-01__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,5vw,4rem);
}

.frm-01__card {
  position: relative;
  width: 100%;
  max-width: 40rem;
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 1.5rem;
  padding: clamp(1.5rem,5vw,2.75rem);
  box-shadow: 0 1px 0 color-mix(in oklab,white 60%,transparent) inset, 0 30px 60px -30px color-mix(in oklab,var(--ink) 30%,transparent);
  animation: frm-01-rise .8s var(--ease) both;
}

@keyframes frm-01-rise {
  from {
    opacity: 0;
    translate: 0 18px;
  }
}

.frm-01__eyebrow {
  margin: 0 0 .75rem;
  font-size: .75rem;
  font-weight: 600;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--accent);
}

.frm-01__title {
  margin: 0;
  font: 400 clamp(2.1rem,6vw,3.1rem)/1 var(--serif);
  letter-spacing: -.02em;
  text-wrap: balance;
}

.frm-01__title em {
  color: var(--accent);
}

.frm-01__lede {
  margin: .9rem 0 0;
  color: var(--muted);
  line-height: 1.55;
  max-width: 34rem;
  text-wrap: pretty;
}

.frm-01__body {
  display: grid;
  gap: 1.35rem;
  margin-top: 2rem;
}

.frm-01__grid {
  display: grid;
  gap: 1.35rem;
  grid-template-columns: repeat(auto-fit,minmax(min(100%,14rem),1fr));
}

.frm-01__field {
  display: grid;
  gap: .45rem;
}

.frm-01__field label,
.frm-01 legend {
  font-size: .875rem;
  font-weight: 600;
}

.frm-01 input[type="text"],
.frm-01 input[type="email"],
.frm-01 textarea {
  width: 100%;
  font: inherit;
  font-size: 1rem;
  color: var(--ink);
  background: var(--field);
  border: 1px solid var(--line);
  border-radius: .85rem;
  padding: .85rem 1rem;
  min-height: 3.1rem;
  transition: border-color .2s, box-shadow .25s var(--ease), background .2s;
}

.frm-01 ::placeholder {
  color: color-mix(in oklab,var(--muted) 75%,transparent);
}

.frm-01 input:hover,
.frm-01 textarea:hover {
  border-color: color-mix(in oklab,var(--ink) 30%,var(--line));
}

.frm-01 input:focus-visible,
.frm-01 textarea:focus-visible {
  outline: none;
  background: var(--card);
  border-color: var(--accent);
  box-shadow: 0 0 0 4px color-mix(in oklab,var(--accent) 20%,transparent);
}

.frm-01 textarea {
  field-sizing: content;
  min-block-size: 8.5rem;
  max-block-size: 20rem;
  resize: vertical;
  line-height: 1.55;
}

.frm-01 :user-invalid,
.frm-01.is-tried :invalid:not(fieldset) {
  border-color: var(--bad);
}

.frm-01__err {
  display: none;
  align-items: center;
  gap: .4rem;
  margin: 0;
  font-size: .8125rem;
  color: var(--bad);
}

.frm-01__err svg {
  width: 1rem;
  height: 1rem;
  flex: none;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.6;
  stroke-linecap: round;
}

.frm-01__field:has(:user-invalid) .frm-01__err,
.frm-01.is-tried .frm-01__field:has(:invalid) .frm-01__err {
  display: flex;
  animation: frm-01-shake .35s var(--ease);
}

@keyframes frm-01-shake {
  30% {
    translate: -3px 0;
  }

  60% {
    translate: 2px 0;
  }
}

.frm-01__hint {
  margin: 0;
  font-size: .8125rem;
  color: var(--muted);
}

.frm-01__chips {
  border: 0;
  padding: 0;
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  gap: .5rem;
}

.frm-01__chips legend {
  margin-bottom: .6rem;
  padding: 0;
}

.frm-01__chips label {
  position: relative;
  cursor: pointer;
}

.frm-01__chips input {
  position: absolute;
  opacity: 0;
  inset: 0;
  margin: 0;
  cursor: pointer;
}

.frm-01__chips span {
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  min-height: 2.6rem;
  padding: 0 1rem;
  border-radius: 999px;
  border: 1px solid var(--line);
  background: var(--field);
  font-size: .9rem;
  font-weight: 500;
  transition: background .2s, color .2s, border-color .2s, scale .2s var(--ease);
}

.frm-01__chips span::before {
  content: '';
  width: .45rem;
  height: .45rem;
  border-radius: 50%;
  background: currentColor;
  opacity: .25;
  scale: .6;
  transition: opacity .2s, scale .3s var(--ease);
}

.frm-01__chips label:hover span {
  border-color: color-mix(in oklab,var(--ink) 30%,var(--line));
}

.frm-01__chips input:checked + span {
  background: var(--ink);
  color: var(--card);
  border-color: var(--ink);
}

.frm-01__chips input:checked + span::before {
  opacity: 1;
  scale: 1;
  background: var(--accent);
}

.frm-01__chips input:focus-visible + span {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.frm-01__chips label:active span {
  scale: .96;
}

.frm-01__labelrow {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}

.frm-01__counter {
  --ring-c: var(--ok);
  display: inline-flex;
  align-items: center;
  gap: .5rem;
  font-size: .8125rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.frm-01__counter[data-state="warn"] {
  --ring-c: var(--warn);
  color: var(--warn);
}

.frm-01__counter[data-state="over"] {
  --ring-c: var(--bad);
  color: var(--bad);
}

.frm-01__counter b {
  font-weight: 600;
  color: var(--ink);
}

.frm-01__counter[data-state="over"] b {
  color: var(--bad);
}

.frm-01__ring {
  width: 1.25rem;
  height: 1.25rem;
  border-radius: 50%;
  background: conic-gradient(var(--ring-c) calc(var(--frm-01-p) * 1%), var(--line) 0);
  -webkit-mask: radial-gradient(farthest-side,transparent 62%,#000 66%);
  mask: radial-gradient(farthest-side,transparent 62%,#000 66%);
  transition: --frm-01-p .35s var(--ease), scale .3s var(--ease);
}

.frm-01__counter[data-state="over"] .frm-01__ring {
  scale: 1.15;
}

.frm-01__foot {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  padding-top: .5rem;
}

.frm-01__check {
  display: inline-flex;
  align-items: center;
  gap: .6rem;
  font-size: .9rem;
  color: var(--muted);
  cursor: pointer;
  min-height: 2.75rem;
}

.frm-01__check input {
  width: 1.15rem;
  height: 1.15rem;
  accent-color: var(--accent);
  margin: 0;
}

.frm-01__send,
.frm-01__again {
  display: inline-flex;
  align-items: center;
  gap: .6rem;
  min-height: 3.1rem;
  padding: 0 1.5rem;
  border: 0;
  border-radius: 999px;
  font: inherit;
  font-weight: 600;
  color: var(--on-accent);
  background: var(--accent);
  cursor: pointer;
  box-shadow: 0 10px 24px -10px color-mix(in oklab,var(--accent) 80%,black);
  transition: translate .2s var(--ease), box-shadow .2s var(--ease), filter .2s;
}

.frm-01__send svg {
  width: 1.1rem;
  height: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.9;
  stroke-linejoin: round;
  transition: translate .35s var(--ease), rotate .35s var(--ease);
}

.frm-01__send:hover {
  translate: 0 -2px;
  filter: brightness(1.05);
}

.frm-01__send:hover svg {
  translate: 3px -3px;
  rotate: -8deg;
}

.frm-01__send:active {
  translate: 0 1px;
}

.frm-01__send:focus-visible,
.frm-01__again:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.frm-01__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.frm-01__done {
  display: grid;
  justify-items: center;
  text-align: center;
  gap: .6rem;
  padding: 3rem 1rem 1rem;
  outline: none;
}

.frm-01__done:not([hidden]) {
  animation: frm-01-rise .6s var(--ease) both;
}

.frm-01__done h3 {
  margin: .5rem 0 0;
  font: 400 2.4rem/1 var(--serif);
}

.frm-01__done p {
  margin: 0 0 1rem;
  color: var(--muted);
}

.frm-01__tick {
  display: grid;
  place-items: center;
  width: 4.5rem;
  height: 4.5rem;
  border-radius: 50%;
  background: color-mix(in oklab,var(--ok) 16%,transparent);
  color: var(--ok);
}

.frm-01__tick svg {
  width: 2.2rem;
  height: 2.2rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 2.4;
  stroke-linecap: round;
  stroke-linejoin: round;
  stroke-dasharray: 24;
  stroke-dashoffset: 24;
  animation: frm-01-draw .6s .2s var(--ease) forwards;
}

@keyframes frm-01-draw {
  to {
    stroke-dashoffset: 0;
  }
}

.frm-01__body[hidden],
.frm-01__head[hidden],
.frm-01__done[hidden] {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .frm-01 *,
    .frm-01 *::before,
    .frm-01__card {
    animation: none !important;
    transition: none !important;
  }

  .frm-01__tick svg {
    stroke-dashoffset: 0;
  }
}

@media (forced-colors: active) {
  .frm-01__ring {
    background: CanvasText;
  }

  .frm-01__chips input:checked + span {
    background: Highlight;
    color: HighlightText;
  }

  .frm-01__send,
    .frm-01__again {
    border: 1px solid ButtonText;
  }
}
/* Theme toggle — top-right of the demo. Ink-relative colours, so it suits light and dark. */

.frm-01 {
  position: relative;
  padding-top: 72px;
  box-sizing: border-box;
}

.frm-01__theme {
  position: absolute;
  top: 16px;
  right: 16px;
  z-index: 20;
  display: grid;
  place-items: center;
  width: 44px;
  height: 44px;
  padding: 0;
  border-radius: 999px;
  border: 1px solid color-mix(in srgb, currentColor 22%, transparent);
  background: color-mix(in srgb, currentColor 8%, transparent);
  color: inherit;
  cursor: pointer;
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
  transition: background-color .2s, transform .2s;
}

.frm-01__theme:hover {
  background: color-mix(in srgb, currentColor 14%, transparent);
}

.frm-01__theme:active {
  transform: scale(.94);
}

.frm-01__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.frm-01__theme svg {
  width: 20px;
  height: 20px;
  fill: none;
  stroke: currentColor;
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.frm-01__theme .frm-01__sun,
.frm-01__theme[aria-pressed="true"] .frm-01__moon {
  display: none;
}

.frm-01__theme[aria-pressed="true"] .frm-01__sun {
  display: block;
}

@media (prefers-reduced-motion: reduce) {
  .frm-01__theme {
    transition: none;
  }
}

@media (forced-colors: active) {
  .frm-01__theme {
    border-color: ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }
}
```

## JavaScript
```js
// Theme toggle (top-right): flips data-theme on the root and mirrors outside changes.
(() => {
  document.querySelectorAll('.frm-01').forEach((root) => {
    const btn = root.querySelector(':scope > [data-theme-toggle]');
    if (!btn || btn.dataset.wired) return;
    btn.dataset.wired = '1';
    const mq = matchMedia('(prefers-color-scheme: dark)');
    const isDark = () => (root.dataset.theme ? root.dataset.theme === 'dark' : mq.matches);
    const sync = () => {
      const dark = isDark();
      btn.setAttribute('aria-pressed', String(dark));
      btn.title = dark ? 'Switch to light mode' : 'Switch to dark mode';
    };
    btn.addEventListener('click', () => { root.dataset.theme = isDark() ? 'light' : 'dark'; sync(); });
    mq.addEventListener('change', sync);
    new MutationObserver(sync).observe(root, { attributes: true, attributeFilter: ['data-theme'] });
    sync();
  });
})();
(() => {
  const root = document.querySelector('.frm-01');
  if (!root) return;
  const ta = root.querySelector('#frm-01-msg');
  const counter = root.querySelector('.frm-01__counter');
  const n = root.querySelector('.frm-01__n');
  const left = root.querySelector('.frm-01__left');
  const live = root.querySelector('#frm-01-live');
  const msgErr = root.querySelector('.frm-01__msgerr');
  const body = root.querySelector('.frm-01__body');
  const head = root.querySelector('.frm-01__head');
  const done = root.querySelector('.frm-01__done');
  const MAX = Number(ta.dataset.max) || 500, WARN = 50;
  root.querySelector('.frm-01__max').textContent = MAX;
  let lastState = 'ok';
  const update = () => {
    const len = ta.value.length, rem = MAX - len;
    const state = rem < 0 ? 'over' : rem <= WARN ? 'warn' : 'ok';
    root.style.setProperty('--frm-01-p', Math.min(100, (len / MAX) * 100));
    counter.dataset.state = state;
    n.textContent = len;
    left.textContent = rem >= 0 ? rem + ' characters remaining.' : Math.abs(rem) + ' characters over the limit.';
    ta.setCustomValidity(rem < 0 ? 'Too long' : '');
    msgErr.textContent = rem < 0 ? 'Please shorten your message by ' + Math.abs(rem) + ' characters.' : 'Write at least 20 characters.';
    if (state !== lastState) { live.textContent = left.textContent; lastState = state; }
  };
  ta.addEventListener('input', update);
  update();
  root.querySelector('.frm-01__send').addEventListener('click', () => {
    const fields = [...root.querySelectorAll('input[required], textarea[required]')];
    const bad = fields.find((f) => !f.checkValidity());
    if (bad) { root.classList.add('is-tried'); bad.focus(); return; }
    body.hidden = true; head.hidden = true; done.hidden = false; done.focus();
  });
  root.querySelector('.frm-01__again').addEventListener('click', () => {
    root.querySelectorAll('input[type="text"], input[type="email"], textarea').forEach((f) => { f.value = ''; });
    root.classList.remove('is-tried'); update();
    done.hidden = true; body.hidden = false; head.hidden = false;
    root.querySelector('#frm-01-name').focus();
  });
})();
```
