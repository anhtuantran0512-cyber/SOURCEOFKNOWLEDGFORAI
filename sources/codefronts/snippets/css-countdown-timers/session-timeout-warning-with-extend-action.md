---
source: "codefronts"
url: "https://codefronts.com/snippets/css-countdown-timers/session-timeout-warning-with-extend-action/"
title: "Session Timeout Warning with Extend Action"
section: "snippets"
category: "css-countdown-timers"
category_name: "CSS Countdown Timers"
description: "The idle-timeout warning banks and health portals ship: after inactivity a native dialog opens with a running countdown, a Stay signed in action and an…"
has_js: "true"
---

Here's a working CSS Countdown Timer from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Session Timeout Warning with Extend Action
Source: https://codefronts.com/snippets/css-countdown-timers/session-timeout-warning-with-extend-action/

The idle-timeout warning banks and health portals ship: after inactivity a native dialog opens with a running countdown, a Stay signed in action and an explicit Sign out now. Escape is deliberately not a dismissal, focus lands on the primary action, and the extend path is what makes a hard time limit pass WCAG 2.2.1.
## HTML
```html
<section class="cdt-03" aria-labelledby="cdt-03-title">
  <input class="cdt-03__tgl" type="checkbox" id="cdt-03-theme">
  <label class="cdt-03__tglbtn" for="cdt-03-theme">
    <svg class="cdt-03__moon" viewBox="0 0 20 20" width="15" height="15" aria-hidden="true"><path d="M15.7 12.8A6.5 6.5 0 0 1 7.2 4.3a6.6 6.6 0 1 0 8.5 8.5Z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg>
    <svg class="cdt-03__sun" viewBox="0 0 20 20" width="15" height="15" aria-hidden="true"><circle cx="10" cy="10" r="3.7" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M10 1.8v2.1M10 16.1v2.1M1.8 10h2.1M16.1 10h2.1M4.2 4.2l1.5 1.5M14.3 14.3l1.5 1.5M15.8 4.2l-1.5 1.5M5.7 14.3l-1.5 1.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
    <span class="cdt-03__darktext">Dark mode</span><span class="cdt-03__lighttext">Light mode</span>
  </label>
  <div class="cdt-03__stage">
    <div class="cdt-03__app" aria-hidden="true">
      <header class="cdt-03__bar"><strong>Vale Health</strong><span>Priya Sharma · Member portal</span></header>
      <div class="cdt-03__body">
        <h2 class="cdt-03__title" id="cdt-03-title">Claim 4471-B</h2>
        <div class="cdt-03__rows"><span></span><span></span><span></span><span></span></div>
      </div>
    </div>

    <dialog class="cdt-03__dialog" id="cdt-03-dialog" role="alertdialog" aria-labelledby="cdt-03-dtitle" aria-describedby="cdt-03-dtext" hidden>
      <div class="cdt-03__icon" aria-hidden="true">
        <svg viewBox="0 0 24 24" width="22" height="22"><circle cx="12" cy="12" r="9.2" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 7.4v5.1l3.2 2" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
      </div>
      <h3 class="cdt-03__dtitle" id="cdt-03-dtitle">Still there?</h3>
      <p class="cdt-03__dtext" id="cdt-03-dtext">For your security we sign you out after ten minutes without activity. Your claim draft is saved.</p>
      <p class="cdt-03__count" role="timer">Your session expires in <time datetime="" data-clock>2:00</time></p>
      <div class="cdt-03__track" aria-hidden="true"><span data-fill></span></div>
      <div class="cdt-03__actions">
        <button class="cdt-03__btn" type="button" data-extend autofocus>Stay signed in</button>
        <button class="cdt-03__btn cdt-03__btn--ghost" type="button" data-out>Sign out now</button>
      </div>
      <p class="cdt-03__note">Escape will not close this — the warning needs an answer.</p>
      <output class="cdt-03__sr" aria-live="polite" data-live></output>
    </dialog>

    <div class="cdt-03__replay">
      <button class="cdt-03__btn cdt-03__btn--ghost" type="button" data-replay>Replay the idle warning</button>
    </div>
  </div>
</section>
```
## CSS
```css
.cdt-03 {
  --page: #eef2f8;
  --card: #ffffff;
  --ink: #0f1b2d;
  --muted: #5d6b82;
  --rule: #dbe3ef;
  --accent: #1f5fe0;
  --danger: #c0392f;
  --font-display: ui-rounded, "SF Pro Rounded", "Segoe UI Variable", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, -apple-system, sans-serif;
}

@supports (color: oklch(50% 0.1 20)) {
  .cdt-03 {
    --page: oklch(96% 0.012 250);
    --card: oklch(100% 0 0);
    --ink: oklch(24% 0.04 255);
    --muted: oklch(53% 0.03 258);
    --rule: oklch(91% 0.016 252);
    --accent: oklch(52% 0.19 262);
    --danger: oklch(52% 0.19 28);
  }
}

.cdt-03 *,
.cdt-03 *::before,
.cdt-03 *::after {
  box-sizing: border-box;
}

.cdt-03 [hidden] {
  display: none !important;
}

.cdt-03__stage {
  display: grid;
  gap: 18px;
  align-content: center;
  justify-items: center;
  min-height: 100vh;
  max-inline-size: 900px;
  margin-inline: auto;
  padding: clamp(16px, 4vw, 44px);
}

.cdt-03__app {
  inline-size: 100%;
  background: var(--card);
  border: 1px solid var(--rule);
  border-radius: 14px;
  box-shadow: 0 14px 30px -18px rgba(15, 27, 45, 0.4);
  overflow: hidden;
}

.cdt-03__bar {
  display: flex;
  flex-wrap: wrap;
  gap: 4px 14px;
  align-items: baseline;
  justify-content: space-between;
  padding: 14px 18px;
  border-block-end: 1px solid var(--rule);
  font-size: 13px;
  color: var(--muted);
}

.cdt-03__bar strong {
  font: 600 14px/1 var(--font-display);
  color: var(--ink);
}

.cdt-03__body {
  padding: 20px 18px 26px;
}

.cdt-03__title {
  margin: 0 0 16px;
  font: 600 clamp(18px, 3vw, 22px)/1.2 var(--font-display);
}

.cdt-03__rows {
  display: grid;
  gap: 10px;
}

.cdt-03__rows span {
  display: block;
  block-size: 12px;
  border-radius: 6px;
  background: var(--rule);
}

.cdt-03__rows span:nth-child(2) {
  inline-size: 82%;
}

.cdt-03__rows span:nth-child(3) {
  inline-size: 64%;
}

.cdt-03__rows span:nth-child(4) {
  inline-size: 47%;
}

.cdt-03__dialog {
  inline-size: min(420px, calc(100vw - 32px));
  padding: clamp(20px, 4vw, 30px);
  border: 1px solid var(--rule);
  border-radius: 16px;
  background: var(--card);
  color: var(--ink);
  box-shadow: 0 30px 70px -26px rgba(15, 27, 45, 0.55);
}

.cdt-03__dialog::backdrop {
  background: rgba(15, 27, 45, 0.42);
  -webkit-backdrop-filter: blur(3px);
  backdrop-filter: blur(3px);
}

.cdt-03__icon {
  display: grid;
  place-items: center;
  inline-size: 42px;
  block-size: 42px;
  margin-block-end: 14px;
  border-radius: 11px;
  background: rgba(31, 95, 224, 0.1);
  color: var(--accent);
}

.cdt-03__dtitle {
  margin: 0 0 8px;
  font: 600 clamp(19px, 3.4vw, 23px)/1.2 var(--font-display);
}

.cdt-03__dtext {
  margin: 0 0 18px;
  font-size: 13.5px;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.cdt-03__count {
  margin: 0 0 10px;
  font: 500 15px/1.4 var(--font-display);
}

.cdt-03__count time {
  font-variant-numeric: tabular-nums;
  font-weight: 700;
  font-size: 22px;
  letter-spacing: -0.01em;
}

.cdt-03__count[data-urgent] {
  color: var(--danger);
}

.cdt-03__track {
  block-size: 6px;
  border-radius: 99px;
  background: var(--rule);
  overflow: hidden;
}

.cdt-03__track span {
  display: block;
  block-size: 100%;
  inline-size: 100%;
  border-radius: 99px;
  background: var(--accent);
  transform-origin: left center;
  transition: inline-size 0.9s linear, background-color 0.3s linear;
}

.cdt-03__count[data-urgent] ~ .cdt-03__track span {
  background: var(--danger);
}

.cdt-03__actions {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-block-start: 20px;
}

.cdt-03__btn {
  flex: 1 1 150px;
  min-inline-size: 44px;
  min-block-size: 44px;
  padding: 12px 18px;
  border: 1px solid transparent;
  border-radius: 10px;
  background: var(--accent);
  color: #fff;
  font: 600 14px/1 var(--font-display);
  cursor: pointer;
}

.cdt-03__btn--ghost {
  background: transparent;
  color: var(--ink);
  border-color: var(--rule);
}

.cdt-03__btn:hover {
  filter: brightness(1.06);
}

.cdt-03__btn:focus-visible {
  outline: 2px solid var(--danger);
  outline-offset: 2px;
}

.cdt-03__note {
  margin: 14px 0 0;
  font-size: 11.5px;
  color: var(--muted);
}

.cdt-03__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.cdt-03__replay {
  display: flex;
  justify-content: center;
  inline-size: 100%;
}

@media (prefers-reduced-motion: reduce) {
  .cdt-03__track span {
    transition: none;
  }
}
/* --- pure-CSS theme toggle ------------------------------------------- */

.cdt-03 {
  position: relative;
}

.cdt-03__tgl {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.cdt-03__tglbtn {
  position: absolute;
  inset-block-end: 14px;
  inset-inline-end: 14px;
  z-index: 20;
  display: inline-flex;
  align-items: center;
  gap: 7px;
  min-block-size: 44px;
  min-inline-size: 44px;
  padding: 12px 14px;
  border: 1px solid currentColor;
  border-radius: 10px;
  background: transparent;
  color: inherit;
  font: 600 11px/1 system-ui, sans-serif;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  cursor: pointer;
  opacity: 0.62;
}

.cdt-03__tglbtn:hover {
  opacity: 1;
}

.cdt-03__tgl:focus-visible + .cdt-03__tglbtn {
  outline: 2px solid currentColor;
  outline-offset: 2px;
  opacity: 1;
}

.cdt-03__tglbtn svg {
  flex: none;
}

.cdt-03__sun,
.cdt-03__lighttext {
  display: none;
}

.cdt-03:has(.cdt-03__tgl:checked) .cdt-03__moon,
.cdt-03:has(.cdt-03__tgl:checked) .cdt-03__darktext {
  display: none;
}

.cdt-03:has(.cdt-03__tgl:checked) .cdt-03__sun {
  display: block;
}

.cdt-03:has(.cdt-03__tgl:checked) .cdt-03__lighttext {
  display: inline;
}

@media (max-width: 460px) {
  .cdt-03__tglbtn {
    padding: 12px;
  }

  .cdt-03__darktext,
    .cdt-03__lighttext,
    .cdt-03:has(.cdt-03__tgl:checked) .cdt-03__darktext,
    .cdt-03:has(.cdt-03__tgl:checked) .cdt-03__lighttext {
    display: none;
  }
}
/* toggle in the system-light case */

@media (prefers-color-scheme: light) {
  .cdt-03:has(.cdt-03__tgl:checked) {
    --page: #0b1220;
    --card: #131c2c;
    --ink: #eaf0fa;
    --muted: #93a2ba;
    --rule: #223047;
    --accent: #6f9dff;
    --danger: #ff7a68;
  }

  .cdt-03:has(.cdt-03__tgl:checked) .cdt-03__btn {
    color: #0b1220;
  }

  .cdt-03:has(.cdt-03__tgl:checked) .cdt-03__dialog::backdrop {
    background: rgba(4, 8, 16, 0.62);
  }
}

@media (prefers-color-scheme: dark) {
  .cdt-03 {
    --page: #0b1220;
    --card: #131c2c;
    --ink: #eaf0fa;
    --muted: #93a2ba;
    --rule: #223047;
    --accent: #6f9dff;
    --danger: #ff7a68;
  }

  .cdt-03__btn {
    color: #0b1220;
  }

  .cdt-03__dialog::backdrop {
    background: rgba(4, 8, 16, 0.62);
  }
  /* mirror flip-back: checked means the opposite of the system preference */

  .cdt-03:has(.cdt-03__tgl:checked) {
    --page: oklch(96% 0.012 250);
    --card: oklch(100% 0 0);
    --ink: oklch(24% 0.04 255);
    --muted: oklch(53% 0.03 258);
    --rule: oklch(91% 0.016 252);
    --accent: oklch(52% 0.19 262);
    --danger: oklch(52% 0.19 28);
  }

  .cdt-03:has(.cdt-03__tgl:checked) .cdt-03__btn {
    color: #fff;
  }

  .cdt-03:has(.cdt-03__tgl:checked) .cdt-03__dialog::backdrop {
    background: rgba(15, 27, 45, 0.42);
  }
}

[data-theme="dark"] .cdt-03 {
  --page: #0b1220;
  --card: #131c2c;
  --ink: #eaf0fa;
  --muted: #93a2ba;
  --rule: #223047;
  --accent: #6f9dff;
  --danger: #ff7a68;
}

[data-theme="dark"] .cdt-03 .cdt-03__btn {
  color: #0b1220;
}
```

## JavaScript
```js
const root = document.querySelector('.cdt-03');
if (root) {
  const dlg = root.querySelector('#cdt-03-dialog'), clock = dlg.querySelector('[data-clock]');
  const fill = dlg.querySelector('[data-fill]'), live = dlg.querySelector('[data-live]');
  const count = dlg.querySelector('.cdt-03__count'), WARN = 120e3;
  let target = 0, id = 0, seen = null;
  const stop = () => { clearTimeout(id); id = 0; };
  const tick = () => {
    const ms = Math.max(0, target - Date.now()), s = Math.ceil(ms / 1000);
    clock.textContent = Math.floor(s / 60) + ':' + String(s % 60).padStart(2, '0');
    clock.dateTime = new Date(target).toISOString();
    fill.style.inlineSize = (ms / WARN * 100).toFixed(1) + '%';
    count.toggleAttribute('data-urgent', ms <= 30e3);
    const b = ms <= 0 ? 'end' : ms <= 30e3 ? 's30' : ms <= 60e3 ? 'm1' : 'm2';
    if (b !== seen) { seen = b; live.textContent = b === 'end' ? 'Session expired. Sign in again to continue.' : 'Session expires in about ' + Math.ceil(ms / 1000) + ' seconds. Choose stay signed in or sign out.'; }
    if (ms > 0) { id = setTimeout(tick, 1000 - (Date.now() % 1000)); } else { clock.textContent = '0:00'; count.firstChild.textContent = 'Session expired '; }
  };
  const open = () => { target = Date.now() + WARN; seen = null; dlg.hidden = false; dlg.showModal(); stop(); tick(); };
  dlg.addEventListener('cancel', (e) => e.preventDefault());
  dlg.querySelector('[data-extend]').addEventListener('click', () => { stop(); dlg.close(); dlg.hidden = true; });
  dlg.querySelector('[data-out]').addEventListener('click', () => { stop(); dlg.close(); dlg.hidden = true; });
  root.querySelector('[data-replay]').addEventListener('click', open);
  setTimeout(open, 900);
  root.cleanup = stop;
}
```
