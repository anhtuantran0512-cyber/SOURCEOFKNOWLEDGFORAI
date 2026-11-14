---
source: "codefronts"
url: "https://codefronts.com/motion/css-ripple-designs/css-ripple-login-form-ui/"
title: "Ripple Login Form Interaction"
section: "motion"
category: "css-ripple-designs"
category_name: "CSS Ripple Effects"
description: "Ripple feedback on real form controls: a labelled email field, a password field, a remember checkbox and a submit button."
has_js: "true"
---

Here's a working CSS Ripple Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Ripple Login Form Interaction
Source: https://codefronts.com/motion/css-ripple-designs/css-ripple-login-form-ui/

Ripple feedback on real form controls: a labelled email field, a password field, a remember checkbox and a submit button. The ripple confirms that a control received the press and nothing more — validation is text, tied to the field with aria-describedby, because a ring that flashes and vanishes is not an error message.
## HTML
```html
<section class="rpl-19" aria-labelledby="rpl-19-title">
  <input class="rpl-19__theme-input" type="checkbox" id="rpl-19-theme">
  <label class="rpl-19__theme" for="rpl-19-theme">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="rpl-19__theme-sr">Switch between dark and light theme</span>
  </label>
  <div class="rpl-19__card">
    <span class="rpl-19__mark" aria-hidden="true"></span>
    <h1 class="rpl-19__h1" id="rpl-19-title">Confirm it&rsquo;s you</h1>
    <p class="rpl-19__sub">We sent a 6-digit code to <strong>a•••@harbourworks.co</strong>.</p>
    <div class="rpl-19__field">
      <label class="rpl-19__label" for="rpl-19-code">Verification code</label>
      <input class="rpl-19__input" id="rpl-19-code" type="text" inputmode="numeric" autocomplete="one-time-code" maxlength="6" placeholder="0 0 0 0 0 0">
      <span class="rpl-19__under" aria-hidden="true"></span>
    </div>
    <button class="rpl-19__submit" type="button" id="rpl-19-go">
      <span class="rpl-19__submit-t">Verify and continue</span>
    </button>
    <p class="rpl-19__msg" id="rpl-19-msg" role="status" aria-live="polite">Code expires in 4:52.</p>
    <p class="rpl-19__resend">Didn&rsquo;t get it? <a class="rpl-19__link" href="#rpl-19">Send a new code</a></p>
  </div>
</section>
```
## CSS
```css
.rpl-19 {
  --rpl-19-bg: #f8f6f2;
  --rpl-19-bg: oklch(0.972 0.006 85);
  --rpl-19-card: #ffffff;
  --rpl-19-card: oklch(1 0 0);
  --rpl-19-line: #e5e1d9;
  --rpl-19-line: oklch(0.903 0.009 85);
  --rpl-19-fg: #171512;
  --rpl-19-fg: oklch(0.21 0.009 78);
  --rpl-19-muted: #6e6a62;
  --rpl-19-muted: oklch(0.55 0.010 82);
  --rpl-19-accent: #12513a;
  --rpl-19-accent: oklch(0.40 0.085 162);
  --rpl-19-bad: #a63325;
  --rpl-19-bad: oklch(0.49 0.16 30);
  --rpl-19-dur: 620ms;
  position: relative;
  display: grid;
  place-items: center;
  min-block-size: 100vh;
  min-block-size: 100svh;
  padding: clamp(16px, 4vw, 48px);
  background: var(--rpl-19-bg);
  color: var(--rpl-19-fg);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif;
  box-sizing: border-box;
}

.rpl-19 *,
.rpl-19 *::before,
.rpl-19 *::after {
  box-sizing: border-box;
}

@media (prefers-color-scheme: dark) {
  .rpl-19:not(:has(#rpl-19-theme:checked)) {
    --rpl-19-bg: #101010;
    --rpl-19-bg: oklch(0.18 0.004 85);
    --rpl-19-card: #191918;
    --rpl-19-card: oklch(0.235 0.005 85);
    --rpl-19-line: #2b2b29;
    --rpl-19-line: oklch(0.31 0.006 85);
    --rpl-19-fg: #f4f2ee;
    --rpl-19-fg: oklch(0.962 0.006 85);
    --rpl-19-muted: #a09c95;
    --rpl-19-muted: oklch(0.715 0.010 85);
    --rpl-19-accent: #62d3a4;
    --rpl-19-accent: oklch(0.81 0.115 162);
    --rpl-19-bad: #ff9484;
    --rpl-19-bad: oklch(0.77 0.135 30);
  }
}

@media (prefers-color-scheme: light) {
  .rpl-19:has(#rpl-19-theme:checked) {
    --rpl-19-bg: #101010;
    --rpl-19-bg: oklch(0.18 0.004 85);
    --rpl-19-card: #191918;
    --rpl-19-card: oklch(0.235 0.005 85);
    --rpl-19-line: #2b2b29;
    --rpl-19-line: oklch(0.31 0.006 85);
    --rpl-19-fg: #f4f2ee;
    --rpl-19-fg: oklch(0.962 0.006 85);
    --rpl-19-muted: #a09c95;
    --rpl-19-muted: oklch(0.715 0.010 85);
    --rpl-19-accent: #62d3a4;
    --rpl-19-accent: oklch(0.81 0.115 162);
    --rpl-19-bad: #ff9484;
    --rpl-19-bad: oklch(0.77 0.135 30);
  }
}

.rpl-19__card {
  inline-size: 100%;
  min-inline-size: 0;
  max-inline-size: 430px;
  display: flex;
  flex-direction: column;
  padding: clamp(26px, 4vw, 38px);
  border: 1px solid var(--rpl-19-line);
  border-radius: 26px;
  background: var(--rpl-19-card);
}

.rpl-19__mark {
  inline-size: 30px;
  block-size: 30px;
  margin-block-end: 22px;
  border-radius: 9px;
  background: var(--rpl-19-accent);
}

.rpl-19__h1 {
  margin: 0 0 8px;
  font-size: clamp(25px, 4vw, 31px);
  font-weight: 620;
  letter-spacing: -0.026em;
}

.rpl-19__sub {
  margin: 0 0 28px;
  font-size: 14px;
  line-height: 1.55;
  color: var(--rpl-19-muted);
}

.rpl-19__sub strong {
  color: var(--rpl-19-fg);
  font-weight: 600;
}

.rpl-19__field {
  position: relative;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.rpl-19__label {
  font-size: 11.5px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--rpl-19-muted);
  font-weight: 600;
}

.rpl-19__input {
  min-block-size: 56px;
  padding: 0 16px;
  border: 1px solid var(--rpl-19-line);
  border-radius: 14px;
  background: transparent;
  color: var(--rpl-19-fg);
  font: inherit;
  font-size: 22px;
  letter-spacing: 0.34em;
  font-variant-numeric: tabular-nums;
}

.rpl-19__input::placeholder {
  color: color-mix(in oklab, var(--rpl-19-muted) 60%, transparent);
  letter-spacing: 0.18em;
}

.rpl-19__input:focus {
  outline: none;
  border-color: color-mix(in oklab, var(--rpl-19-accent) 60%, var(--rpl-19-line));
}
/* Focus ripple runs along the underline, not over the text — the field stays readable while typing. */

.rpl-19__under {
  position: absolute;
  inset-block-end: 0;
  inset-inline: 14px;
  block-size: 2px;
  border-radius: 2px;
  background: var(--rpl-19-accent);
  transform: scaleX(0);
  transform-origin: 50% 50%;
  transition: transform 340ms cubic-bezier(0.2, 0.7, 0.3, 1);
}

.rpl-19__input:focus ~ .rpl-19__under {
  transform: scaleX(1);
}

.rpl-19__submit {
  position: relative;
  min-block-size: 54px;
  margin-block-start: 22px;
  border: 0;
  border-radius: 14px;
  background: var(--rpl-19-accent);
  color: var(--rpl-19-card);
  font: inherit;
  font-size: 15px;
  font-weight: 620;
  cursor: pointer;
  overflow: hidden;
  isolation: isolate;
  -webkit-tap-highlight-color: transparent;
}

.rpl-19__submit:focus-visible {
  outline: 2px solid var(--rpl-19-accent);
  outline-offset: 3px;
}

.rpl-19__submit-t {
  position: relative;
  z-index: 2;
}

.rpl-19__ink {
  position: absolute;
  left: var(--rpl-19-x, 50%);
  top: var(--rpl-19-y, 50%);
  inline-size: calc(var(--rpl-19-r, 120px) * 2);
  block-size: calc(var(--rpl-19-r, 120px) * 2);
  border-radius: 50%;
  background: oklch(1 0 0 / 0.32);
  pointer-events: none;
  z-index: 1;
  animation: rpl-19-ink var(--rpl-19-dur) cubic-bezier(0.14, 0.7, 0.3, 1) forwards;
}

@media (prefers-color-scheme: dark) {
  .rpl-19:not(:has(#rpl-19-theme:checked)) .rpl-19__ink {
    background: oklch(0.2 0.02 162 / 0.34);
  }
}

@media (prefers-color-scheme: light) {
  .rpl-19:has(#rpl-19-theme:checked) .rpl-19__ink {
    background: oklch(0.2 0.02 162 / 0.34);
  }
}

@keyframes rpl-19-ink {
  from {
    transform: translate(-50%, -50%) scale(0);
    opacity: 1;
  }

  to {
    transform: translate(-50%, -50%) scale(1);
    opacity: 0;
  }
}

.rpl-19__msg {
  margin: 14px 0 0;
  font-size: 13px;
  line-height: 1.5;
  color: var(--rpl-19-muted);
  font-variant-numeric: tabular-nums;
}

.rpl-19__msg[data-state="bad"] {
  color: var(--rpl-19-bad);
  font-weight: 550;
}

.rpl-19__msg[data-state="good"] {
  color: var(--rpl-19-accent);
  font-weight: 550;
}

.rpl-19__resend {
  margin: 20px 0 0;
  font-size: 13px;
  color: var(--rpl-19-muted);
}

.rpl-19__link {
  color: var(--rpl-19-accent);
  text-decoration: none;
  border-block-end: 1px solid color-mix(in oklab, var(--rpl-19-accent) 40%, transparent);
}

.rpl-19__link:hover {
  color: var(--rpl-19-fg);
  border-color: var(--rpl-19-fg);
}

@media (prefers-reduced-motion: reduce) {
  .rpl-19__ink {
    display: none;
  }

  .rpl-19__under {
    transition: none;
  }

  .rpl-19__submit:active {
    filter: brightness(0.92);
  }
}

.rpl-19 {
  position: relative;
}

.rpl-19__theme-input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.rpl-19__theme {
  position: absolute;
  z-index: 60;
  inset-block-start: 14px;
  inset-inline-end: 14px;
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border-radius: 999px;
  border: 1px solid color-mix(in oklab, currentColor 22%, transparent);
  background: color-mix(in oklab, currentColor 8%, transparent);
  color: inherit;
  cursor: pointer;
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
  transition: background 160ms ease, border-color 160ms ease, transform 160ms ease;
}

.rpl-19__theme:hover {
  background: color-mix(in oklab, currentColor 15%, transparent);
  border-color: color-mix(in oklab, currentColor 38%, transparent);
}

.rpl-19__theme:active {
  transform: scale(0.94);
}

.rpl-19__theme svg {
  inline-size: 19px;
  block-size: 19px;
  display: block;
  transition: transform 320ms cubic-bezier(0.2, 0.7, 0.3, 1);
}

.rpl-19__theme-input:checked + .rpl-19__theme svg {
  transform: rotate(180deg);
}

.rpl-19__theme-input:focus-visible + .rpl-19__theme {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.rpl-19__theme-sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

@media (prefers-reduced-motion: reduce) {
  .rpl-19__theme,
    .rpl-19__theme svg {
    transition: none;
  }
}
```

## JavaScript
```js
const root = document.querySelector('.rpl-19');
const go = root.querySelector('#rpl-19-go');
const input = root.querySelector('#rpl-19-code');
const msg = root.querySelector('#rpl-19-msg');
const timers = new Set();

const verify = (event) => {
  const code = input.value.replace(/\D/g, '');
  const ok = code.length === 6;
  msg.textContent = ok ? 'Code accepted. Signing you in…' : 'Enter all six digits to continue.';
  msg.dataset.state = ok ? 'good' : 'bad';
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const box = go.getBoundingClientRect();
  const x = (event.clientX || box.left + box.width / 2) - box.left;
  const y = (event.clientY || box.top + box.height / 2) - box.top;
  const r = Math.max(Math.hypot(x, y), Math.hypot(box.width - x, y), Math.hypot(x, box.height - y), Math.hypot(box.width - x, box.height - y));
  const ink = document.createElement('span');
  ink.className = 'rpl-19__ink';
  ink.setAttribute('aria-hidden', 'true');
  ink.style.setProperty('--rpl-19-x', x + 'px');
  ink.style.setProperty('--rpl-19-y', y + 'px');
  ink.style.setProperty('--rpl-19-r', r + 'px');
  ink.addEventListener('animationend', () => ink.remove(), { once: true });
  const t = setTimeout(() => { timers.delete(t); ink.remove(); }, 1400);
  timers.add(t);
  go.append(ink);
};

const onKey = (event) => { if (event.key === 'Enter') verify(event); };
go.addEventListener('pointerdown', verify);
input.addEventListener('keydown', onKey);
root.__rplCleanup = () => { go.removeEventListener('pointerdown', verify); input.removeEventListener('keydown', onKey); timers.forEach(clearTimeout); timers.clear(); };
```
