---
source: "codefronts"
url: "https://codefronts.com/components/css-forms/registration-form-with-password-strength/"
title: "Registration Form with Password Strength"
section: "components"
category: "css-forms"
category_name: "CSS Forms"
description: "A sign-up screen on a slow-drifting aurora: a four-segment strength meter whose fill colour is interpolated through oklch, a live requirements checklist that…"
has_js: "true"
---

Here's a working CSS Form from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Registration Form with Password Strength
Source: https://codefronts.com/components/css-forms/registration-form-with-password-strength/

A sign-up screen on a slow-drifting aurora: a four-segment strength meter whose fill colour is interpolated through oklch, a live requirements checklist that ticks itself off, an accessible show/hide toggle using aria-pressed, real-time confirm-password matching, and an entropy-style scorer that rewards length over symbol soup — exactly what NIST SP 800-63B recommends.
## HTML
```html
<div class="frm-02">
  <button type="button" class="frm-02__theme" data-theme-toggle aria-label="Dark mode" aria-pressed="false" title="Switch to dark mode"><svg class="frm-02__moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5Z"/></svg><svg class="frm-02__sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg></button>
  <div class="frm-02__aurora" aria-hidden="true"><i></i><i></i><i></i></div>
  <div class="frm-02__stage">
    <div class="frm-02__card" role="form" aria-labelledby="frm-02-title">
      <div class="frm-02__brand" aria-hidden="true"><span></span>Northwind</div>
      <h2 id="frm-02-title">Create your account</h2>
      <p class="frm-02__sub">Free for 14 days. No card required.</p>
      <button class="frm-02__passkey" type="button">
        <svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="8" cy="9" r="4"/><path d="M2 20c.7-3.3 3-5 6-5 1.4 0 2.7.4 3.7 1.1"/><circle cx="17.5" cy="13.5" r="2.5"/><path d="M17.5 16v5l1.5-1.2M17.5 19l1.5-1"/></svg>
        Sign up with a passkey
      </button>
      <div class="frm-02__or"><span>or with email</span></div>
      <div class="frm-02__field">
        <label for="frm-02-name">Full name</label>
        <input id="frm-02-name" type="text" autocomplete="name" required placeholder="Jordan Avery">
      </div>
      <div class="frm-02__field">
        <label for="frm-02-email">Email</label>
        <input id="frm-02-email" type="email" autocomplete="email" required placeholder="[email protected]" aria-describedby="frm-02-email-err">
        <p class="frm-02__err" id="frm-02-email-err">Enter a valid email address.</p>
      </div>
      <div class="frm-02__field">
        <label for="frm-02-pw">Password</label>
        <div class="frm-02__pw">
          <input id="frm-02-pw" type="password" autocomplete="new-password" required minlength="8" placeholder="At least 8 characters" aria-describedby="frm-02-strength frm-02-rules">
          <button class="frm-02__eye" type="button" aria-pressed="false" aria-controls="frm-02-pw">
            <span class="frm-02__sr">Show password</span>
            <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M2 12s3.6-7 10-7 10 7 10 7-3.6 7-10 7S2 12 2 12Z"/><circle cx="12" cy="12" r="3"/><path class="frm-02__slash" d="M4 4l16 16"/></svg>
          </button>
        </div>
        <div class="frm-02__meter" data-score="0" aria-hidden="true"><i></i><i></i><i></i><i></i></div>
        <p class="frm-02__strength" id="frm-02-strength"><span>Strength:</span> <b>Too short</b></p>
        <p class="frm-02__sr" aria-live="polite" id="frm-02-live"></p>
        <ul class="frm-02__rules" id="frm-02-rules" aria-label="Password requirements">
          <li data-rule="len"><svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="7"/><path d="m4.8 8.2 2.2 2.2 4.2-4.6"/></svg>8+ characters <small>(12+ is better)</small></li>
          <li data-rule="case"><svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="7"/><path d="m4.8 8.2 2.2 2.2 4.2-4.6"/></svg>Upper &amp; lowercase</li>
          <li data-rule="num"><svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="7"/><path d="m4.8 8.2 2.2 2.2 4.2-4.6"/></svg>A number</li>
          <li data-rule="sym"><svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="7"/><path d="m4.8 8.2 2.2 2.2 4.2-4.6"/></svg>A symbol</li>
        </ul>
      </div>
      <div class="frm-02__field frm-02__confirm" data-match="empty">
        <label for="frm-02-pw2">Confirm password</label>
        <input id="frm-02-pw2" type="password" autocomplete="new-password" required placeholder="Re-enter password" aria-describedby="frm-02-match">
        <p class="frm-02__match" id="frm-02-match" aria-live="polite"></p>
      </div>
      <label class="frm-02__terms"><input type="checkbox" required id="frm-02-terms"><span>I agree to the <a href="#terms">Terms</a> and <a href="#privacy">Privacy Policy</a>.</span></label>
      <button class="frm-02__submit" type="button">Create account</button>
      <p class="frm-02__status" role="status"></p>
      <p class="frm-02__alt">Already have an account? <a href="#login">Sign in</a></p>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@400;500;600;700&display=swap');

.frm-02 {
  --bg: #070814;
  --card: rgba(18,20,40,.62);
  --ink: #eef0ff;
  --muted: #9aa0c3;
  --line: rgba(255,255,255,.12);
  --field: rgba(255,255,255,.05);
  --accent: #8b7bff;
  --accent-2: #3dd6c6;
  --weak: #ef4444;
  --fair: #f59e0b;
  --good: #84cc16;
  --great: #22c55e;
  --sans: "Sora",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --ease: cubic-bezier(.16,1,.3,1);
  position: relative;
  isolation: isolate;
  overflow: hidden;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(50% 0 0)) {
  .frm-02 {
    --accent: oklch(68% .19 285);
    --accent-2: oklch(80% .13 180);
    --weak: oklch(63% .22 25);
    --fair: oklch(77% .16 70);
    --good: oklch(78% .19 130);
    --great: oklch(72% .19 150);
  }
}

.frm-02[data-theme="light"] {
  --bg: #eef0fb;
  --card: rgba(255,255,255,.72);
  --ink: #14162b;
  --muted: #5b6080;
  --line: rgba(20,22,43,.12);
  --field: rgba(255,255,255,.7);
}

.frm-02,
.frm-02 *,
.frm-02 *::before,
.frm-02 *::after {
  box-sizing: border-box;
}

.frm-02__aurora {
  position: absolute;
  inset: 0;
  z-index: -1;
  filter: blur(70px) saturate(1.2);
  opacity: .75;
}

.frm-02__aurora i {
  position: absolute;
  width: 46vmax;
  height: 46vmax;
  border-radius: 50%;
  animation: frm-02-drift 18s ease-in-out infinite alternate;
}

.frm-02__aurora i:nth-child(1) {
  background: var(--accent);
  top: -18vmax;
  left: -10vmax;
}

.frm-02__aurora i:nth-child(2) {
  background: var(--accent-2);
  bottom: -22vmax;
  right: -12vmax;
  animation-delay: -6s;
  opacity: .7;
}

.frm-02__aurora i:nth-child(3) {
  background: #d946ef;
  top: 30%;
  left: 55%;
  width: 26vmax;
  height: 26vmax;
  animation-delay: -11s;
  opacity: .45;
}

@keyframes frm-02-drift {
  to {
    translate: 8vmax 6vmax;
    scale: 1.15;
  }
}

.frm-02__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,5vw,4rem);
}

.frm-02__card {
  width: 100%;
  max-width: 27rem;
  display: grid;
  gap: 1.05rem;
  padding: clamp(1.5rem,5vw,2.5rem);
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 1.75rem;
  -webkit-backdrop-filter: blur(24px) saturate(1.4);
  backdrop-filter: blur(24px) saturate(1.4);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.08), 0 40px 80px -30px rgba(0,0,0,.6);
}

.frm-02__brand {
  display: flex;
  align-items: center;
  gap: .55rem;
  font-weight: 600;
  letter-spacing: -.01em;
}

.frm-02__brand span {
  width: 1.6rem;
  height: 1.6rem;
  border-radius: .5rem;
  background: conic-gradient(from 200deg,var(--accent),var(--accent-2),var(--accent));
  box-shadow: 0 0 20px color-mix(in oklab,var(--accent) 60%,transparent);
}

.frm-02 h2 {
  margin: .6rem 0 0;
  font-size: clamp(1.6rem,4vw,1.9rem);
  font-weight: 600;
  letter-spacing: -.03em;
}

.frm-02__sub {
  margin: -.6rem 0 .2rem;
  color: var(--muted);
  font-size: .95rem;
}

.frm-02__passkey {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: .6rem;
  min-height: 3rem;
  border-radius: .9rem;
  border: 1px solid var(--line);
  background: var(--field);
  color: var(--ink);
  font: inherit;
  font-weight: 500;
  cursor: pointer;
  transition: background .2s, border-color .2s;
}

.frm-02__passkey svg {
  width: 1.25rem;
  height: 1.25rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.6;
  stroke-linecap: round;
}

.frm-02__passkey:hover {
  background: color-mix(in oklab,var(--field),white 6%);
  border-color: color-mix(in oklab,var(--line),white 15%);
}

.frm-02__or {
  display: flex;
  align-items: center;
  gap: .8rem;
  color: var(--muted);
  font-size: .8rem;
}

.frm-02__or::before,
.frm-02__or::after {
  content: '';
  flex: 1;
  height: 1px;
  background: var(--line);
}

.frm-02__field {
  display: grid;
  gap: .45rem;
}

.frm-02 label {
  font-size: .85rem;
  font-weight: 500;
}

.frm-02 input[type="text"],
.frm-02 input[type="email"],
.frm-02 input[type="password"] {
  width: 100%;
  min-height: 3rem;
  padding: .75rem 1rem;
  border-radius: .9rem;
  border: 1px solid var(--line);
  background: var(--field);
  color: var(--ink);
  font: inherit;
  font-size: 1rem;
  transition: border-color .2s, box-shadow .25s var(--ease);
}

.frm-02 ::placeholder {
  color: color-mix(in oklab,var(--muted) 70%,transparent);
}

.frm-02 input:focus-visible {
  outline: none;
  border-color: var(--accent);
  box-shadow: 0 0 0 4px color-mix(in oklab,var(--accent) 28%,transparent);
}

.frm-02 input:user-invalid {
  border-color: var(--weak);
}

.frm-02__err {
  display: none;
  margin: 0;
  font-size: .8rem;
  color: var(--weak);
}

.frm-02__field:has(input:user-invalid) .frm-02__err {
  display: block;
}

.frm-02__pw {
  position: relative;
}

.frm-02 .frm-02__pw input {
  padding-right: 3.4rem;
}

.frm-02__eye {
  position: absolute;
  right: .3rem;
  top: 50%;
  translate: 0 -50%;
  width: 2.6rem;
  height: 2.6rem;
  display: grid;
  place-items: center;
  border: 0;
  border-radius: .7rem;
  background: transparent;
  color: var(--muted);
  cursor: pointer;
}

.frm-02__eye:hover {
  color: var(--ink);
  background: var(--field);
}

.frm-02__eye:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 1px;
}

.frm-02__eye svg {
  width: 1.25rem;
  height: 1.25rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
}

.frm-02__slash {
  stroke-dasharray: 23;
  stroke-dashoffset: 0;
  transition: stroke-dashoffset .3s var(--ease);
}

.frm-02__eye[aria-pressed="true"] .frm-02__slash {
  stroke-dashoffset: 23;
}

.frm-02__meter {
  display: grid;
  grid-template-columns: repeat(4,1fr);
  gap: .35rem;
  margin-top: .25rem;
}

.frm-02__meter i {
  height: .32rem;
  border-radius: 99px;
  background: var(--line);
  position: relative;
  overflow: hidden;
}

.frm-02__meter i::after {
  content: '';
  position: absolute;
  inset: 0;
  background: var(--seg,transparent);
  scale: 0 1;
  transform-origin: left;
  transition: scale .45s var(--ease), background .3s;
  border-radius: inherit;
}

.frm-02__meter[data-score="1"] {
  --seg: var(--weak);
}

.frm-02__meter[data-score="2"] {
  --seg: var(--fair);
}

.frm-02__meter[data-score="3"] {
  --seg: var(--good);
}

.frm-02__meter[data-score="4"] {
  --seg: var(--great);
}

.frm-02__meter[data-score="1"] i:nth-child(-n+1)::after,
.frm-02__meter[data-score="2"] i:nth-child(-n+2)::after,
.frm-02__meter[data-score="3"] i:nth-child(-n+3)::after,
.frm-02__meter[data-score="4"] i::after {
  scale: 1 1;
}

.frm-02__meter[data-score="4"] i::after {
  box-shadow: 0 0 12px var(--great);
}

.frm-02__meter i:nth-child(2)::after {
  transition-delay: .05s;
}

.frm-02__meter i:nth-child(3)::after {
  transition-delay: .1s;
}

.frm-02__meter i:nth-child(4)::after {
  transition-delay: .15s;
}

.frm-02__strength {
  margin: 0;
  font-size: .8rem;
  color: var(--muted);
}

.frm-02__strength b {
  font-weight: 600;
  color: var(--ink);
}

.frm-02__rules {
  list-style: none;
  margin: .15rem 0 0;
  padding: 0;
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(10.5rem,1fr));
  gap: .4rem .8rem;
  font-size: .8rem;
  color: var(--muted);
}

.frm-02__rules li {
  display: flex;
  align-items: center;
  gap: .45rem;
  transition: color .25s;
}

.frm-02__rules small {
  opacity: .7;
  font-size: inherit;
}

.frm-02__rules svg {
  width: 1rem;
  height: 1rem;
  flex: none;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.5;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.frm-02__rules circle {
  opacity: .35;
  transition: fill .25s, opacity .25s;
}

.frm-02__rules path {
  stroke-dasharray: 10;
  stroke-dashoffset: 10;
  transition: stroke-dashoffset .35s var(--ease);
}

.frm-02__rules li[data-met="true"] {
  color: var(--ink);
}

.frm-02__rules li[data-met="true"] circle {
  fill: color-mix(in oklab,var(--great) 25%,transparent);
  stroke: var(--great);
  opacity: 1;
}

.frm-02__rules li[data-met="true"] path {
  stroke-dashoffset: 0;
  stroke: var(--great);
}

.frm-02__match {
  margin: 0;
  font-size: .8rem;
  min-height: 1.1em;
}

.frm-02__confirm[data-match="yes"] input {
  border-color: var(--great);
}

.frm-02__confirm[data-match="yes"] .frm-02__match {
  color: var(--great);
}

.frm-02__confirm[data-match="no"] input {
  border-color: var(--weak);
}

.frm-02__confirm[data-match="no"] .frm-02__match {
  color: var(--weak);
}

.frm-02__terms {
  display: flex;
  align-items: flex-start;
  gap: .65rem;
  font-size: .85rem !important;
  font-weight: 400 !important;
  color: var(--muted);
  cursor: pointer;
  line-height: 1.45;
}

.frm-02__terms input {
  width: 1.15rem;
  height: 1.15rem;
  margin: .1rem 0 0;
  accent-color: var(--accent);
  flex: none;
}

.frm-02 a {
  color: var(--ink);
  text-decoration-color: color-mix(in oklab,var(--accent) 70%,transparent);
  text-underline-offset: 3px;
}

.frm-02 a:hover {
  color: var(--accent-2);
}

.frm-02__submit {
  position: relative;
  overflow: hidden;
  min-height: 3.2rem;
  border: 0;
  border-radius: .9rem;
  cursor: pointer;
  font: inherit;
  font-weight: 600;
  color: #0b0b1a;
  background: linear-gradient(110deg,var(--accent),var(--accent-2));
  box-shadow: 0 14px 30px -12px color-mix(in oklab,var(--accent) 80%,transparent);
  transition: translate .2s var(--ease), filter .2s, opacity .2s;
}

.frm-02__submit:hover {
  translate: 0 -2px;
  filter: brightness(1.08);
}

.frm-02__submit:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.frm-02__card:not(:has(#frm-02-terms:checked)) .frm-02__submit {
  opacity: .55;
}

.frm-02__status {
  margin: -.4rem 0 0;
  font-size: .85rem;
  color: var(--great);
  min-height: 0;
  text-align: center;
}

.frm-02__status:empty {
  display: none;
}

.frm-02__alt {
  margin: 0;
  text-align: center;
  font-size: .85rem;
  color: var(--muted);
}

.frm-02__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

@media (prefers-reduced-motion: reduce) {
  .frm-02__aurora i {
    animation: none;
  }

  .frm-02 *,
    .frm-02 *::after {
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .frm-02__aurora {
    display: none;
  }

  .frm-02__meter i::after {
    background: Highlight;
  }

  .frm-02__submit {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
  }
}
/* Theme toggle — top-right of the demo. Ink-relative colours, so it suits light and dark. */

.frm-02 {
  position: relative;
  padding-top: 72px;
  box-sizing: border-box;
}

.frm-02__theme {
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

.frm-02__theme:hover {
  background: color-mix(in srgb, currentColor 14%, transparent);
}

.frm-02__theme:active {
  transform: scale(.94);
}

.frm-02__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.frm-02__theme svg {
  width: 20px;
  height: 20px;
  fill: none;
  stroke: currentColor;
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.frm-02__theme .frm-02__sun,
.frm-02__theme[aria-pressed="true"] .frm-02__moon {
  display: none;
}

.frm-02__theme[aria-pressed="true"] .frm-02__sun {
  display: block;
}

@media (prefers-reduced-motion: reduce) {
  .frm-02__theme {
    transition: none;
  }
}

@media (forced-colors: active) {
  .frm-02__theme {
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
  document.querySelectorAll('.frm-02').forEach((root) => {
    const btn = root.querySelector(':scope > [data-theme-toggle]');
    if (!btn || btn.dataset.wired) return;
    btn.dataset.wired = '1';
    const mq = matchMedia('(prefers-color-scheme: dark)');
    const isDark = () => (root.dataset.theme ? root.dataset.theme === 'dark' : true);
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
  const root = document.querySelector('.frm-02');
  if (!root) return;
  const pw = root.querySelector('#frm-02-pw'), pw2 = root.querySelector('#frm-02-pw2');
  const meter = root.querySelector('.frm-02__meter'), label = root.querySelector('.frm-02__strength b');
  const live = root.querySelector('#frm-02-live'), confirm = root.querySelector('.frm-02__confirm');
  const matchMsg = root.querySelector('#frm-02-match'), eye = root.querySelector('.frm-02__eye');
  const rules = {
    len: (v) => v.length >= 8, case: (v) => /[a-z]/.test(v) && /[A-Z]/.test(v),
    num: (v) => /\d/.test(v), sym: (v) => /[^A-Za-z0-9]/.test(v)
  };
  const names = ['Too short', 'Weak', 'Fair', 'Good', 'Strong'];
  const score = (v) => {
    if (v.length < 8) return v.length ? 1 : 0;
    let s = (v.length >= 12) + (v.length >= 16);
    s += [rules.case(v), rules.num(v), rules.sym(v)].filter(Boolean).length * 0.75;
    if (/^(.)\1+$/.test(v) || /password|qwerty|12345/i.test(v)) s = 0;
    return Math.max(1, Math.min(4, Math.round(s) + 1));
  };
  let last = 0;
  const checkMatch = () => {
    if (!pw2.value) { confirm.dataset.match = 'empty'; matchMsg.textContent = ''; return; }
    const ok = pw2.value === pw.value;
    confirm.dataset.match = ok ? 'yes' : 'no';
    matchMsg.textContent = ok ? 'Passwords match.' : 'Passwords don\'t match yet.';
    pw2.setCustomValidity(ok ? '' : 'Mismatch');
  };
  pw.addEventListener('input', () => {
    const v = pw.value, s = score(v);
    meter.dataset.score = s;
    label.textContent = v.length && v.length < 8 ? 'Too short' : names[s];
    root.querySelectorAll('.frm-02__rules li').forEach((li) => { li.dataset.met = rules[li.dataset.rule](v); });
    if (s !== last) { live.textContent = 'Password strength: ' + label.textContent; last = s; }
    checkMatch();
  });
  pw2.addEventListener('input', checkMatch);
  eye.addEventListener('click', () => {
    const show = eye.getAttribute('aria-pressed') !== 'true';
    eye.setAttribute('aria-pressed', show);
    [pw, pw2].forEach((i) => { i.type = show ? 'text' : 'password'; });
    eye.querySelector('.frm-02__sr').textContent = show ? 'Hide password' : 'Show password';
  });
  root.querySelector('.frm-02__submit').addEventListener('click', () => {
    const status = root.querySelector('.frm-02__status');
    const bad = [...root.querySelectorAll('input[required]')].find((i) => !i.checkValidity());
    if (bad) { bad.focus(); bad.reportValidity(); return; }
    status.textContent = 'Account created — check your inbox to verify your email.';
  });
})();
```
