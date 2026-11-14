---
source: "codefronts"
url: "https://codefronts.com/components/css-avatars/css-avatar-with-notification-count-badge/"
title: "CSS Avatar with Notification Count Badge"
section: "components"
category: "css-avatars"
category_name: "CSS Avatars"
description: "The count badge that survives real data: 1 digit, 2 digits and 99+ all render without the badge jumping, because the pill is a min-inline-size circle that…"
has_js: "true"
---

Here's a working CSS Avatar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Avatar with Notification Count Badge
Source: https://codefronts.com/components/css-avatars/css-avatar-with-notification-count-badge/

The count badge that survives real data: 1 digit, 2 digits and 99+ all render without the badge jumping, because the pill is a min-inline-size circle that grows only when the text demands it, and the digits are tabular-nums so a 7 is exactly as wide as a 1. The real number goes to assistive tech through aria-label — never inferred from the visual text — and the count is live, so you can watch the width behave.
## HTML
```html
<div class="av-07">
  <button class="av-07__theme" type="button" aria-pressed="false">
    <svg class="av-07__i av-07__i--moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.3A8.4 8.4 0 0 1 9.7 3.5a8.5 8.5 0 1 0 10.8 10.8Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="av-07__i av-07__i--sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.1" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.7 5.7l1.4 1.4M16.9 16.9l1.4 1.4M18.3 5.7l-1.4 1.4M7.1 16.9l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <span class="av-07__vh">Toggle dark theme</span>
  </button>

  <div class="av-07__stage">
    <section class="av-07__wrap" aria-labelledby="av-07-h">
      <header class="av-07__head">
        <p class="av-07__eyebrow">Inbox · Unread</p>
        <h2 class="av-07__h" id="av-07-h">Count badges</h2>
        <p class="av-07__sub">One digit, two digits, 99+ — the pill grows leftward and the avatar never moves.</p>
      </header>

      <div class="av-07__panel">
        <button class="av-07__trigger" type="button" id="av-07-btn" aria-label="7 unread notifications">
          <span class="av-07__fig">
            <img class="av-07__img" src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=200&auto=format&fit=facearea&facepad=2.5" alt="Maya Okonkwo" width="200" height="200" loading="lazy" decoding="async">
            <span class="av-07__badge" id="av-07-badge" aria-hidden="true">7</span>
          </span>
        </button>

        <div class="av-07__ctl">
          <p class="av-07__count"><span id="av-07-num">7</span> unread</p>
          <div class="av-07__btns">
            <button class="av-07__btn" type="button" data-av07="1">+1</button>
            <button class="av-07__btn" type="button" data-av07="9">+9</button>
            <button class="av-07__btn" type="button" data-av07="90">+90</button>
            <button class="av-07__btn av-07__btn--ghost" type="button" data-av07="0">Clear</button>
          </div>
          <p class="av-07__live" id="av-07-live" aria-live="polite"></p>
        </div>
      </div>

      <ul class="av-07__row">
        <li class="av-07__spec">
          <span class="av-07__fig av-07__fig--sm">
            <img class="av-07__img" src="https://images.unsplash.com/photo-1463453091185-61582044d556?w=200&auto=format&fit=facearea&facepad=2.5" alt="Paul Iverson" width="200" height="200" loading="lazy" decoding="async">
            <span class="av-07__badge" aria-hidden="true">3</span>
          </span>
          <span class="av-07__vh">Paul Iverson, 3 unread notifications</span>
          <code class="av-07__snip">1 digit · circle</code>
        </li>
        <li class="av-07__spec">
          <span class="av-07__fig av-07__fig--sm">
            <img class="av-07__img" src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=200&auto=format&fit=facearea&facepad=2.5" alt="Noah Feldman" width="200" height="200" loading="lazy" decoding="async">
            <span class="av-07__badge" aria-hidden="true">24</span>
          </span>
          <span class="av-07__vh">Noah Feldman, 24 unread notifications</span>
          <code class="av-07__snip">2 digits · capsule</code>
        </li>
        <li class="av-07__spec">
          <span class="av-07__fig av-07__fig--sm">
            <img class="av-07__img" src="https://images.unsplash.com/photo-1560250097-0b93528c311a?w=200&auto=format&fit=facearea&facepad=2.5" alt="Victor Cho" width="200" height="200" loading="lazy" decoding="async">
            <span class="av-07__badge" aria-hidden="true">99+</span>
          </span>
          <span class="av-07__vh">Victor Cho, 214 unread notifications</span>
          <code class="av-07__snip">capped · 99+</code>
        </li>
        <li class="av-07__spec">
          <span class="av-07__fig av-07__fig--sm">
            <img class="av-07__img" src="https://images.unsplash.com/photo-1517365830460-955ce3ccd263?w=200&auto=format&fit=facearea&facepad=2.5" alt="Ava Lindqvist" width="200" height="200" loading="lazy" decoding="async">
            <span class="av-07__badge" aria-hidden="true" hidden>0</span>
          </span>
          <span class="av-07__vh">Ava Lindqvist, no unread notifications</span>
          <code class="av-07__snip">zero · hidden</code>
        </li>
      </ul>
    </section>
  </div>
</div>
```
## CSS
```css
@supports (color: oklch(50% .1 250)) {
  .av-07 {
    --page: oklch(97.6% .004 265);
    --panel: oklch(100% 0 0);
    --panel-2: oklch(96.4% .006 265);
    --ink: oklch(20% .022 265);
    --muted: oklch(53% .022 265);
    --line: oklch(92% .008 265);
    --accent: oklch(58% .196 272);
    --badge: oklch(55% .22 22);
  }
}

.av-07 {
  --page: #f7f8fa;
  --panel: #ffffff;
  --panel-2: #f1f3f7;
  --ink: #10131a;
  --muted: #5f6672;
  --line: #e4e7ee;
  --accent: #4f46e5;
  --badge: #dc2626;
  --badge-ink: #ffffff;
  --glass: rgba(255,255,255,.68);
  --shadow: 0 1px 2px rgba(16,19,26,.05), 0 16px 36px -20px rgba(16,19,26,.3);
  --r: 18px;
  width: 100%;
  inline-size: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui,-apple-system,"Segoe UI",sans-serif;
  -webkit-font-smoothing: antialiased;
}

.av-07 *,
.av-07 *::before,
.av-07 *::after {
  box-sizing: border-box;
}

.av-07__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.av-07 [hidden] {
  display: none !important;
}

.av-07__theme {
  position: absolute;
  inset-block-start: clamp(.85rem,2.2vw,1.5rem);
  inset-inline-end: clamp(.85rem,2.2vw,1.5rem);
  z-index: 20;
  display: grid;
  place-items: center;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  border-radius: 999px;
  border: 1px solid var(--line);
  background: var(--glass);
  color: var(--ink);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  cursor: pointer;
  transition: translate .2s ease;
}

.av-07__theme::after {
  content: "";
  position: absolute;
  inset: -.4rem;
  border-radius: inherit;
}

.av-07__theme:hover {
  translate: 0 -1px;
}

.av-07__theme:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.av-07__i {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.av-07__i--sun {
  display: none;
}

.av-07[data-theme="dark"] .av-07__i--moon {
  display: none;
}

.av-07[data-theme="dark"] .av-07__i--sun {
  display: block;
}

.av-07__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
}

.av-07__wrap {
  inline-size: min(56rem,100%);
  display: flex;
  flex-direction: column;
  gap: clamp(1.25rem,3vw,2rem);
}

.av-07__head {
  display: flex;
  flex-direction: column;
  gap: .4rem;
  padding-inline-end: 3.5rem;
}

.av-07__eyebrow {
  margin: 0;
  font-size: .7rem;
  font-weight: 600;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.av-07__h {
  margin: 0;
  font-size: clamp(1.6rem,4.2vw,2.4rem);
  font-weight: 650;
  letter-spacing: -.03em;
  line-height: 1.05;
}

.av-07__sub {
  margin: 0;
  max-inline-size: 36rem;
  font-size: .95rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.av-07__panel {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: clamp(1.25rem,4vw,2.5rem);
  padding: clamp(1.5rem,4vw,2.25rem);
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: var(--r);
  box-shadow: var(--shadow);
}

.av-07__trigger {
  appearance: none;
  padding: .4rem;
  margin: 0;
  border: 0;
  border-radius: 50%;
  background: transparent;
  cursor: pointer;
  min-inline-size: 2.75rem;
  min-block-size: 2.75rem;
  color: inherit;
  transition: translate .22s cubic-bezier(.2,.7,.3,1);
}

.av-07__trigger:hover {
  translate: 0 -2px;
}

.av-07__trigger:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.av-07__fig {
  --size: clamp(4.5rem,12vw,6rem);
  position: relative;
  display: block;
  inline-size: var(--size);
  aspect-ratio: 1;
}

.av-07__img {
  display: block;
  inline-size: 100%;
  block-size: 100%;
  border-radius: 50%;
  object-fit: cover;
  object-position: center top;
  background: var(--panel-2);
  box-shadow: 0 0 0 1px rgba(16,19,26,.06);
}

.av-07__badge {
  position: absolute;
  inset-block-start: -2%;
  inset-inline-end: -6%;
  z-index: 2;
  pointer-events: none;
  display: grid;
  place-items: center;
  min-inline-size: 1.35rem;
  block-size: 1.35rem;
  padding-inline: .32rem;
  border-radius: 999px;
  background: var(--badge);
  color: var(--badge-ink);
  font-size: .72rem;
  font-weight: 700;
  line-height: 1;
  font-variant-numeric: tabular-nums;
  letter-spacing: -.01em;
  box-shadow: 0 0 0 2.5px var(--panel);
}

@supports (transition-behavior: allow-discrete) {
  .av-07__badge {
    transition: scale .22s cubic-bezier(.2,.9,.3,1.2), display .22s allow-discrete;
  }

  @starting-style {
    .av-07__badge {
      scale: .4;
    }
  }
}

.av-07__fig--sm {
  --size: 3.25rem;
}

.av-07__fig--sm .av-07__badge {
  min-inline-size: 1.15rem;
  block-size: 1.15rem;
  font-size: .66rem;
  box-shadow: 0 0 0 2px var(--panel);
}

.av-07__ctl {
  display: flex;
  flex-direction: column;
  gap: .7rem;
  min-inline-size: min(16rem,100%);
}

.av-07__count {
  margin: 0;
  font-size: clamp(1.1rem,2.6vw,1.35rem);
  font-weight: 650;
  letter-spacing: -.02em;
  font-variant-numeric: tabular-nums;
}

.av-07__btns {
  display: flex;
  flex-wrap: wrap;
  gap: .4rem;
}

.av-07__btn {
  appearance: none;
  min-block-size: 2.75rem;
  min-inline-size: 2.75rem;
  padding: 0 .95rem;
  border-radius: 10px;
  border: 1px solid var(--line);
  background: var(--ink);
  color: var(--panel);
  font: inherit;
  font-size: .85rem;
  font-weight: 600;
  cursor: pointer;
  transition: translate .16s ease, opacity .16s ease;
}

.av-07__btn:hover {
  translate: 0 -1px;
  opacity: .9;
}

.av-07__btn:active {
  translate: 0 1px;
}

.av-07__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.av-07__btn--ghost {
  background: transparent;
  color: var(--muted);
}

.av-07__live {
  margin: 0;
  min-block-size: 1.1rem;
  font-size: .8rem;
  color: var(--muted);
}

.av-07__row {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(auto-fit,minmax(9rem,1fr));
}

.av-07__spec {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: .6rem;
  padding: 1.1rem .75rem;
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 14px;
}

.av-07__snip {
  font-size: .68rem;
  font-family: ui-monospace,SFMono-Regular,Menlo,monospace;
  color: var(--muted);
  padding: .2rem .45rem;
  border-radius: 6px;
  background: var(--panel-2);
}

.av-07[data-theme="dark"] {
  --page: #0a0b0e;
  --panel: #14161c;
  --panel-2: #1c1f27;
  --ink: #f2f4f9;
  --muted: #98a0b0;
  --line: #262a33;
  --accent: #8b8cf9;
  --badge: #ef4444;
  --glass: rgba(255,255,255,.07);
  --shadow: 0 1px 2px rgba(0,0,0,.6), 0 20px 44px -24px rgba(0,0,0,.85);
}

.av-07[data-theme="dark"] .av-07__img {
  box-shadow: 0 0 0 1px rgba(255,255,255,.08);
}

@media (prefers-color-scheme: dark) {
  .av-07:not([data-theme="light"]) {
    --page: #0a0b0e;
    --panel: #14161c;
    --panel-2: #1c1f27;
    --ink: #f2f4f9;
    --muted: #98a0b0;
    --line: #262a33;
    --accent: #8b8cf9;
    --badge: #ef4444;
    --glass: rgba(255,255,255,.07);
    --shadow: 0 1px 2px rgba(0,0,0,.6), 0 20px 44px -24px rgba(0,0,0,.85);
  }

  .av-07:not([data-theme="light"]) .av-07__i--moon {
    display: none;
  }

  .av-07:not([data-theme="light"]) .av-07__i--sun {
    display: block;
  }

  .av-07:not([data-theme="light"]) .av-07__img {
    box-shadow: 0 0 0 1px rgba(255,255,255,.08);
  }
}

@media (prefers-reduced-motion: reduce) {
  .av-07 *,
    .av-07 *::before,
    .av-07 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .av-07__badge {
    background: Highlight;
    color: HighlightText;
    box-shadow: 0 0 0 2px Canvas;
  }

  .av-07__panel,
    .av-07__spec,
    .av-07__btn,
    .av-07__theme {
    border-color: CanvasText;
  }
}
```

## JavaScript
```js
const av07 = document.querySelector('.av-07');
const av07badge = av07.querySelector('#av-07-badge');
const av07btn = av07.querySelector('#av-07-btn');
const av07num = av07.querySelector('#av-07-num');
const av07live = av07.querySelector('#av-07-live');
let av07n = 7;

const av07render = () => {
  av07badge.textContent = av07n > 99 ? '99+' : String(av07n);
  av07badge.hidden = av07n === 0;
  av07num.textContent = av07n;
  av07btn.setAttribute('aria-label', av07n + ' unread notifications');
  av07live.textContent = av07n === 0 ? 'Inbox cleared' : av07n + ' unread';
};

av07.querySelectorAll('[data-av07]').forEach((b) => b.addEventListener('click', () => {
  const step = Number(b.dataset.av07);
  av07n = step === 0 ? 0 : Math.min(av07n + step, 999);
  av07render();
}));

av07.querySelector('.av-07__theme').addEventListener('click', (e) => {
  const on = av07.dataset.theme !== 'dark';
  av07.dataset.theme = on ? 'dark' : 'light';
  e.currentTarget.setAttribute('aria-pressed', String(on));
});
av07render();
```
