---
source: "codefronts"
url: "https://codefronts.com/components/css-floating-buttons/notification-bell-fab/"
title: "Notification Bell Floating Button with Badge Counter"
section: "components"
category: "css-floating-buttons"
category_name: "CSS Floating Buttons"
description: "A bell that behaves like a bell: it swings from the top when a notification lands, the badge bumps with a spring, the count caps at 99+ with correct tabular…"
has_js: "true"
---

Here's a working CSS Floating Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Notification Bell Floating Button with Badge Counter
Source: https://codefronts.com/components/css-floating-buttons/notification-bell-fab/

A bell that behaves like a bell: it swings from the top when a notification lands, the badge bumps with a spring, the count caps at 99+ with correct tabular alignment, and the whole thing announces politely instead of interrupting. Includes the muted state, because every notification control needs an off switch.
## HTML
```html
<section class="fb-21" aria-label="Notification bell floating button demo">
  <div class="fb-21__page">
    <p class="fb-21__eyebrow">transform-origin 50% 12% · tabular-nums</p>
    <h2 class="fb-21__title">It swings from the crown</h2>
    <p class="fb-21__sub">Send a few notifications and watch the badge bump. Mute it and they still arrive — silently, with no swing and no announcement.</p>
    <div class="fb-21__ctl">
      <button class="fb-21__btn" id="fb-21-add" type="button">Send notification</button>
      <button class="fb-21__btn" id="fb-21-burst" type="button">Send 12 at once</button>
      <button class="fb-21__btn" id="fb-21-reset" type="button">Clear all</button>
    </div>
    <p class="fb-21__note" id="fb-21-status" role="status" aria-live="polite">No new notifications</p>
  </div>
  <div class="fb-21__dock">
    <button class="fb-21__mute" id="fb-21-mute" type="button" aria-pressed="false" aria-label="Mute notifications">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M5 9a7 7 0 0 1 14 0c0 5 2 6 2 6H3s2-1 2-6z" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><path class="fb-21__slash" d="M4 4l16 16" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
    </button>
    <button class="fb-21__bellBtn" id="fb-21-bell" type="button" aria-label="Notifications, none new">
      <span class="fb-21__bell" id="fb-21-bellIco" aria-hidden="true">
        <svg viewBox="0 0 24 24" focusable="false"><path d="M6 10a6 6 0 0 1 12 0c0 4.4 1.8 5.6 1.8 5.6H4.2S6 14.4 6 10z" fill="currentColor"/><path d="M10.2 18.4a2 2 0 0 0 3.6 0" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg>
      </span>
      <span class="fb-21__badge" id="fb-21-badge" data-zero="true">0</span>
    </button>
  </div>
</section>
```
## CSS
```css
.fb-21 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--fb-21-bg);
  --fb-21-bg: linear-gradient(175deg,oklch(0.97 0.01 85),oklch(0.93 0.03 70));
  --fb-21-brand: oklch(0.55 0.16 55);
  --fb-21-brandDeep: oklch(0.42 0.14 52);
  --fb-21-alert: oklch(0.6 0.22 25);
  --fb-21-ink: oklch(0.23 0.025 60);
  --fb-21-mut: oklch(0.53 0.02 60);
  --fb-21-card: oklch(1 0 0);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--fb-21-ink);
  position: relative;
  display: grid;
  place-items: center;
  padding: clamp(20px,5vw,56px);
  overflow: hidden;
}

.fb-21 *,
.fb-21 *::before,
.fb-21 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fb-21__page {
  width: min(100%,54ch);
  display: grid;
  gap: 14px;
  justify-items: center;
  text-align: center;
}

.fb-21__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--fb-21-brand);
}

.fb-21__title {
  font-size: clamp(26px,4.6vw,44px);
  line-height: 1.05;
  letter-spacing: -.03em;
  font-weight: 700;
  text-wrap: balance;
}

.fb-21__sub {
  font-size: clamp(13.5px,1.7vw,16.5px);
  line-height: 1.62;
  color: var(--fb-21-mut);
  text-wrap: pretty;
}

.fb-21__ctl {
  display: flex;
  flex-wrap: wrap;
  gap: 9px;
  justify-content: center;
}

.fb-21__btn {
  min-height: 44px;
  padding: 0 18px;
  border: 1px solid oklch(0.23 0.025 60/.12);
  border-radius: 99px;
  background: var(--fb-21-card);
  color: var(--fb-21-ink);
  font-size: 13.5px;
  font-weight: 620;
  font-family: inherit;
  cursor: pointer;
  box-shadow: 0 6px 18px -14px oklch(0.23 0.025 60/.9);
  transition: background .18s ease,transform .18s ease,border-color .18s ease;
}

.fb-21__btn:hover {
  background: oklch(0.55 0.16 55/.09);
  border-color: oklch(0.55 0.16 55/.35);
}

.fb-21__btn:active {
  transform: scale(.97);
}

.fb-21__btn:focus-visible {
  outline: 3px solid var(--fb-21-brand);
  outline-offset: 2px;
}

.fb-21__note {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  color: var(--fb-21-brandDeep);
  background: oklch(0.55 0.16 55/.1);
  border-radius: 10px;
  padding: 8px 15px;
  min-height: 34px;
}

.fb-21__dock {
  position: absolute;
  right: clamp(18px,4vw,40px);
  bottom: calc(clamp(18px,4vw,40px) + env(safe-area-inset-bottom));
  z-index: 5;
  display: grid;
  gap: 10px;
  justify-items: center;
}

.fb-21__mute {
  display: grid;
  place-items: center;
  width: 44px;
  height: 44px;
  border: 1px solid oklch(0.23 0.025 60/.12);
  border-radius: 50%;
  background: var(--fb-21-card);
  color: var(--fb-21-mut);
  cursor: pointer;
  box-shadow: 0 8px 20px -14px oklch(0.23 0.025 60/.9);
  transition: background .18s ease,color .18s ease;
}

.fb-21__mute svg {
  width: 20px;
  height: 20px;
}

.fb-21__slash {
  opacity: 0;
  transition: opacity .2s ease;
}

.fb-21__mute[aria-pressed="true"] {
  background: oklch(0.23 0.025 60/.85);
  color: oklch(0.98 0.01 60);
}

.fb-21__mute[aria-pressed="true"] .fb-21__slash {
  opacity: 1;
}

.fb-21__mute:focus-visible {
  outline: 3px solid var(--fb-21-brand);
  outline-offset: 3px;
}

.fb-21__bellBtn {
  position: relative;
  display: grid;
  place-items: center;
  inline-size: 64px;
  block-size: 64px;
  border: 0;
  border-radius: 22px;
  cursor: pointer;
  color: oklch(0.99 0.01 55);
  background: linear-gradient(150deg,oklch(0.7 0.16 62),var(--fb-21-brandDeep));
  box-shadow: 0 14px 32px -12px oklch(0.42 0.14 52/.85),0 2px 6px oklch(0.3 0.06 52/.28);
  transition: transform .28s cubic-bezier(.2,1.3,.4,1);
}

.fb-21__bellBtn:hover {
  transform: translateY(-2px);
}

.fb-21__bellBtn:active {
  transform: scale(.94);
}

.fb-21__bellBtn:focus-visible {
  outline: 3px solid var(--fb-21-brandDeep);
  outline-offset: 4px;
}

.fb-21__bell {
  display: grid;
  place-items: center;
  transform-origin: 50% 12%;
}

.fb-21__bell svg {
  width: 29px;
  height: 29px;
}

.fb-21__bell[data-ring="true"] {
  animation: fb-21-ring .9s cubic-bezier(.36,.07,.19,.97);
}

@keyframes fb-21-ring {
  0%,
    100% {
    rotate: 0deg;
  }

  15% {
    rotate: 14deg;
  }

  30% {
    rotate: -11deg;
  }

  45% {
    rotate: 8deg;
  }

  60% {
    rotate: -5deg;
  }

  75% {
    rotate: 2deg;
  }
}

.fb-21__badge {
  position: absolute;
  top: -5px;
  right: -5px;
  min-width: 24px;
  height: 24px;
  padding: 0 7px;
  border-radius: 99px;
  background: var(--fb-21-alert);
  color: oklch(0.99 0.01 25);
  font-size: 12px;
  font-weight: 700;
  line-height: 24px;
  text-align: center;
  font-variant-numeric: tabular-nums;
  box-shadow: 0 0 0 3px oklch(0.95 0.02 72),0 4px 10px -4px oklch(0.4 0.14 25/.9);
  transition: scale .28s cubic-bezier(.2,1.6,.4,1),opacity .2s ease;
}

.fb-21__badge[data-zero="true"] {
  scale: 0;
  opacity: 0;
}

.fb-21__badge[data-bump="true"] {
  animation: fb-21-bump .34s cubic-bezier(.2,1.6,.4,1);
}

@keyframes fb-21-bump {
  0% {
    scale: 1;
  }

  40% {
    scale: 1.32;
  }

  100% {
    scale: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .fb-21 * {
    animation: none !important;
    transition: none !important;
  }
}
```

## JavaScript
```js
(() => {
  const bell = document.getElementById('fb-21-bell');
  const ico = document.getElementById('fb-21-bellIco');
  const badge = document.getElementById('fb-21-badge');
  const status = document.getElementById('fb-21-status');
  const mute = document.getElementById('fb-21-mute');
  if (!bell || bell.dataset.fbWired) return;
  bell.dataset.fbWired = '1';
  let n = 0, muted = false;
  const render = (bump) => {
    badge.textContent = n > 99 ? '99+' : String(n);
    badge.dataset.zero = String(n === 0);
    bell.setAttribute('aria-label', 'Notifications, ' + (n === 0 ? 'none new' : n + ' new'));
    if (bump && !muted) {
      badge.dataset.bump = 'true';
      ico.dataset.ring = 'true';
      setTimeout(() => { badge.dataset.bump = 'false'; ico.dataset.ring = 'false'; }, 950);
      status.textContent = n + (n === 1 ? ' new notification' : ' new notifications');
    }
  };
  const add = (k) => { n += k; render(true); };
  document.getElementById('fb-21-add').addEventListener('click', () => add(1));
  document.getElementById('fb-21-burst').addEventListener('click', () => add(12));
  document.getElementById('fb-21-reset').addEventListener('click', () => { n = 0; render(false); status.textContent = 'No new notifications'; });
  bell.addEventListener('click', () => { n = 0; render(false); status.textContent = 'Notification list opened, badge cleared'; });
  mute.addEventListener('click', () => {
    muted = !muted;
    mute.setAttribute('aria-pressed', String(muted));
    mute.setAttribute('aria-label', muted ? 'Unmute notifications' : 'Mute notifications');
    status.textContent = muted ? 'Notifications muted — counts update silently' : 'Notifications unmuted';
  });
  render(false);
})();
```
