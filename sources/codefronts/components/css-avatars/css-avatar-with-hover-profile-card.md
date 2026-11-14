---
source: "codefronts"
url: "https://codefronts.com/components/css-avatars/css-avatar-with-hover-profile-card/"
title: "CSS Avatar with Hover Profile Card"
section: "components"
category: "css-avatars"
category_name: "CSS Avatars"
description: "The hovercard, built so keyboard users are not second-class: the trigger is a real <button>, the card opens on hover and on focus, closes on Escape, and a…"
has_js: "true"
---

Here's a working CSS Avatar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Avatar with Hover Profile Card
Source: https://codefronts.com/components/css-avatars/css-avatar-with-hover-profile-card/

The hovercard, built so keyboard users are not second-class: the trigger is a real <button>, the card opens on hover and on focus, closes on Escape, and a 120ms hover-intent delay stops it flickering as the pointer crosses a facepile. CSS anchor positioning pins the card to the avatar where supported, with a plain absolute fallback everywhere else — and the card holds exactly what a hovercard should: name, role, timezone, local time and one action.
## HTML
```html
<div class="av-17">
  <button class="av-17__theme" type="button" aria-pressed="false">
    <svg class="av-17__i av-17__i--moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.3A8.4 8.4 0 0 1 9.7 3.5a8.5 8.5 0 1 0 10.8 10.8Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="av-17__i av-17__i--sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.1" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.7 5.7l1.4 1.4M16.9 16.9l1.4 1.4M18.3 5.7l-1.4 1.4M7.1 16.9l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <span class="av-17__vh">Toggle dark theme</span>
  </button>

  <div class="av-17__stage">
    <section class="av-17__wrap" aria-labelledby="av-17-h">
      <header class="av-17__head">
        <p class="av-17__eyebrow">Identity · Hovercard</p>
        <h2 class="av-17__h" id="av-17-h">Point, or tab, at a face</h2>
        <p class="av-17__sub">120ms to open, 220ms to close, Escape to dismiss. Focus does everything hover does.</p>
      </header>

      <ul class="av-17__list">
        <li class="av-17__row" data-av17>
          <button class="av-17__trigger" type="button" aria-expanded="false" aria-describedby="av-17-c1">
            <img class="av-17__img" src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=200&auto=format&fit=facearea&facepad=2.5" alt="Grace Tan" width="200" height="200" loading="lazy" decoding="async">
          </button>
          <span class="av-17__line"><strong>Grace Tan</strong> approved the presence spec <time datetime="2027-03-04T11:40">11:40</time></span>
          <div class="av-17__card" id="av-17-c1" role="dialog" aria-label="Grace Tan profile summary" hidden>
            <div class="av-17__cardtop">
              <img class="av-17__cardimg" src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=200&auto=format&fit=facearea&facepad=2.5" alt="Grace Tan" width="200" height="200" loading="lazy" decoding="async">
              <span class="av-17__cardwho"><strong>Grace Tan</strong><span>Design lead · Design systems</span></span>
            </div>
            <dl class="av-17__meta">
              <dt>Timezone</dt><dd>Singapore · GMT+8</dd>
              <dt>Local time</dt><dd>7:40 pm</dd>
            </dl>
            <button class="av-17__cta" type="button">Message Grace</button>
          </div>
        </li>

        <li class="av-17__row" data-av17>
          <button class="av-17__trigger" type="button" aria-expanded="false" aria-describedby="av-17-c2">
            <img class="av-17__img" src="https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?w=200&auto=format&fit=facearea&facepad=2.5" alt="Ethan Brooks" width="200" height="200" loading="lazy" decoding="async">
          </button>
          <span class="av-17__line"><strong>Ethan Brooks</strong> merged <code>presence/reconnect</code> <time datetime="2027-03-04T11:12">11:12</time></span>
          <div class="av-17__card" id="av-17-c2" role="dialog" aria-label="Ethan Brooks profile summary" hidden>
            <div class="av-17__cardtop">
              <img class="av-17__cardimg" src="https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?w=200&auto=format&fit=facearea&facepad=2.5" alt="Ethan Brooks" width="200" height="200" loading="lazy" decoding="async">
              <span class="av-17__cardwho"><strong>Ethan Brooks</strong><span>Platform engineer · Infrastructure</span></span>
            </div>
            <dl class="av-17__meta">
              <dt>Timezone</dt><dd>Dublin · GMT+1</dd>
              <dt>Local time</dt><dd>12:40 pm</dd>
            </dl>
            <button class="av-17__cta" type="button">Message Ethan</button>
          </div>
        </li>

        <li class="av-17__row" data-av17>
          <button class="av-17__trigger" type="button" aria-expanded="false" aria-describedby="av-17-c3">
            <img class="av-17__img" src="https://images.unsplash.com/photo-1554151228-14d9def656e4?w=200&auto=format&fit=facearea&facepad=2.5" alt="Aisha Rahman" width="200" height="200" loading="lazy" decoding="async">
          </button>
          <span class="av-17__line"><strong>Aisha Rahman</strong> left 3 comments on the roster view <time datetime="2027-03-04T10:58">10:58</time></span>
          <div class="av-17__card" id="av-17-c3" role="dialog" aria-label="Aisha Rahman profile summary" hidden>
            <div class="av-17__cardtop">
              <img class="av-17__cardimg" src="https://images.unsplash.com/photo-1554151228-14d9def656e4?w=200&auto=format&fit=facearea&facepad=2.5" alt="Aisha Rahman" width="200" height="200" loading="lazy" decoding="async">
              <span class="av-17__cardwho"><strong>Aisha Rahman</strong><span>Product designer · Growth</span></span>
            </div>
            <dl class="av-17__meta">
              <dt>Timezone</dt><dd>Toronto · GMT-4</dd>
              <dt>Local time</dt><dd>7:40 am</dd>
            </dl>
            <button class="av-17__cta" type="button">Message Aisha</button>
          </div>
        </li>
      </ul>
    </section>
  </div>
</div>
```
## CSS
```css
@supports (color: oklch(50% .1 250)) {
  .av-17 {
    --page: oklch(97.6% .004 265);
    --panel: oklch(100% 0 0);
    --panel-2: oklch(96.4% .006 265);
    --ink: oklch(20% .022 265);
    --muted: oklch(53% .022 265);
    --line: oklch(92% .008 265);
    --accent: oklch(58% .196 272);
  }
}

.av-17 {
  --page: #f7f8fa;
  --panel: #ffffff;
  --panel-2: #f1f3f7;
  --ink: #10131a;
  --muted: #5f6672;
  --line: #e4e7ee;
  --accent: #4f46e5;
  --glass: rgba(255,255,255,.68);
  --shadow: 0 1px 2px rgba(16,19,26,.05), 0 16px 36px -20px rgba(16,19,26,.3);
  --pop: 0 2px 6px rgba(16,19,26,.06), 0 24px 48px -20px rgba(16,19,26,.4);
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

.av-17 *,
.av-17 *::before,
.av-17 *::after {
  box-sizing: border-box;
}

.av-17__vh {
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

.av-17 [hidden] {
  display: none !important;
}

.av-17__theme {
  position: absolute;
  inset-block-start: clamp(.85rem,2.2vw,1.5rem);
  inset-inline-end: clamp(.85rem,2.2vw,1.5rem);
  z-index: 40;
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

.av-17__theme::after {
  content: "";
  position: absolute;
  inset: -.4rem;
  border-radius: inherit;
}

.av-17__theme:hover {
  translate: 0 -1px;
}

.av-17__theme:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.av-17__i {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.av-17__i--sun {
  display: none;
}

.av-17[data-theme="dark"] .av-17__i--moon {
  display: none;
}

.av-17[data-theme="dark"] .av-17__i--sun {
  display: block;
}

.av-17__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
}

.av-17__wrap {
  inline-size: min(52rem,100%);
  display: flex;
  flex-direction: column;
  gap: clamp(1.1rem,2.6vw,1.6rem);
}

.av-17__head {
  display: flex;
  flex-direction: column;
  gap: .4rem;
  padding-inline-end: 3.5rem;
}

.av-17__eyebrow {
  margin: 0;
  font-size: .7rem;
  font-weight: 600;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.av-17__h {
  margin: 0;
  font-size: clamp(1.6rem,4.2vw,2.4rem);
  font-weight: 650;
  letter-spacing: -.03em;
  line-height: 1.05;
}

.av-17__sub {
  margin: 0;
  max-inline-size: 36rem;
  font-size: .95rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.av-17__list {
  list-style: none;
  margin: 0;
  padding: .5rem;
  display: flex;
  flex-direction: column;
  gap: .2rem;
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: var(--r);
  box-shadow: var(--shadow);
}

.av-17__row {
  position: relative;
  display: flex;
  align-items: center;
  gap: .85rem;
  padding: .7rem .8rem;
  border-radius: 12px;
  transition: background .18s ease;
}

.av-17__row:hover,
.av-17__row:focus-within {
  background: var(--panel-2);
}

.av-17__trigger {
  appearance: none;
  margin: 0;
  padding: 0;
  border: 0;
  background: transparent;
  cursor: pointer;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border-radius: 50%;
  flex: none;
}

.av-17__trigger:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.av-17__img {
  display: block;
  inline-size: 100%;
  block-size: 100%;
  border-radius: 50%;
  object-fit: cover;
  object-position: center top;
  background: var(--panel-2);
  box-shadow: 0 0 0 1px rgba(16,19,26,.08);
  transition: translate .2s ease;
}

.av-17__trigger:hover .av-17__img {
  translate: 0 -2px;
}

.av-17__line {
  font-size: .9rem;
  line-height: 1.45;
  color: var(--muted);
}

.av-17__line strong {
  color: var(--ink);
  font-weight: 650;
}

.av-17__line code {
  font-family: ui-monospace,SFMono-Regular,Menlo,monospace;
  font-size: .8rem;
  padding: .05rem .3rem;
  border-radius: 5px;
  background: var(--panel-2);
}

.av-17__line time {
  font-size: .78rem;
  font-variant-numeric: tabular-nums;
}

.av-17__card {
  position: absolute;
  z-index: 30;
  inset-block-start: calc(100% - .3rem);
  inset-inline-start: 2.5rem;
  inline-size: min(19rem,calc(100vw - 3rem));
  display: flex;
  flex-direction: column;
  gap: .85rem;
  padding: 1rem;
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 16px;
  box-shadow: var(--pop);
}

@supports (transition-behavior: allow-discrete) {
  .av-17__card {
    transition: opacity .18s ease, translate .18s cubic-bezier(.2,.8,.3,1), display .18s allow-discrete;
  }

  @starting-style {
    .av-17__card {
      opacity: 0;
      translate: 0 -.4rem;
    }
  }
}

@supports (anchor-name: --av17) {
  .av-17__trigger {
    anchor-name: --av17;
  }

  .av-17__card {
    position: fixed;
    inset: auto;
    position-anchor: --av17;
    position-area: block-end span-inline-end;
    margin-block-start: .5rem;
    position-try-fallbacks: flip-block, flip-inline;
  }
}

.av-17__cardtop {
  display: flex;
  align-items: center;
  gap: .75rem;
}

.av-17__cardimg {
  inline-size: 3rem;
  block-size: 3rem;
  border-radius: 50%;
  object-fit: cover;
  object-position: center top;
  background: var(--panel-2);
  flex: none;
}

.av-17__cardwho {
  display: flex;
  flex-direction: column;
  gap: .1rem;
  min-inline-size: 0;
}

.av-17__cardwho strong {
  font-size: 1rem;
  font-weight: 650;
  letter-spacing: -.02em;
}

.av-17__cardwho span {
  font-size: .8rem;
  color: var(--muted);
}

.av-17__meta {
  margin: 0;
  display: grid;
  grid-template-columns: auto 1fr;
  gap: .25rem .85rem;
  font-size: .82rem;
}

.av-17__meta dt {
  color: var(--muted);
}

.av-17__meta dd {
  margin: 0;
  font-weight: 600;
  font-variant-numeric: tabular-nums;
}

.av-17__cta {
  appearance: none;
  min-block-size: 2.75rem;
  padding: 0 1rem;
  border-radius: 10px;
  border: 1px solid transparent;
  background: var(--accent);
  color: #fff;
  font: inherit;
  font-size: .88rem;
  font-weight: 650;
  cursor: pointer;
  transition: translate .16s ease, opacity .16s ease;
}

.av-17__cta:hover {
  translate: 0 -1px;
  opacity: .94;
}

.av-17__cta:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.av-17[data-theme="dark"] {
  --page: #0a0b0e;
  --panel: #14161c;
  --panel-2: #1c1f27;
  --ink: #f2f4f9;
  --muted: #98a0b0;
  --line: #262a33;
  --accent: #6d6df5;
  --glass: rgba(255,255,255,.07);
  --shadow: 0 1px 2px rgba(0,0,0,.6), 0 20px 44px -24px rgba(0,0,0,.85);
  --pop: 0 2px 8px rgba(0,0,0,.7), 0 28px 56px -20px rgba(0,0,0,.95);
}

.av-17[data-theme="dark"] .av-17__img {
  box-shadow: 0 0 0 1px rgba(255,255,255,.1);
}

@media (prefers-color-scheme: dark) {
  .av-17:not([data-theme="light"]) {
    --page: #0a0b0e;
    --panel: #14161c;
    --panel-2: #1c1f27;
    --ink: #f2f4f9;
    --muted: #98a0b0;
    --line: #262a33;
    --accent: #6d6df5;
    --glass: rgba(255,255,255,.07);
    --shadow: 0 1px 2px rgba(0,0,0,.6), 0 20px 44px -24px rgba(0,0,0,.85);
    --pop: 0 2px 8px rgba(0,0,0,.7), 0 28px 56px -20px rgba(0,0,0,.95);
  }

  .av-17:not([data-theme="light"]) .av-17__i--moon {
    display: none;
  }

  .av-17:not([data-theme="light"]) .av-17__i--sun {
    display: block;
  }

  .av-17:not([data-theme="light"]) .av-17__img {
    box-shadow: 0 0 0 1px rgba(255,255,255,.1);
  }
}

@media (prefers-reduced-motion: reduce) {
  .av-17 *,
    .av-17 *::before,
    .av-17 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .av-17__card {
    border-color: CanvasText;
    box-shadow: none;
  }

  .av-17__cta {
    background: Highlight;
    color: HighlightText;
  }

  .av-17__list,
    .av-17__theme {
    border-color: CanvasText;
  }
}
```

## JavaScript
```js
const av17 = document.querySelector('.av-17');

av17.querySelectorAll('[data-av17]').forEach((row) => {
  const trigger = row.querySelector('.av-17__trigger');
  const card = row.querySelector('.av-17__card');
  let timer;

  const show = () => { card.hidden = false; trigger.setAttribute('aria-expanded', 'true'); };
  const hide = () => { card.hidden = true; trigger.setAttribute('aria-expanded', 'false'); };
  const openSoon = () => { clearTimeout(timer); timer = setTimeout(show, 120); };
  const closeSoon = () => { clearTimeout(timer); timer = setTimeout(hide, 220); };

  trigger.addEventListener('pointerenter', openSoon);
  trigger.addEventListener('pointerleave', closeSoon);
  trigger.addEventListener('click', () => (card.hidden ? show() : hide()));
  trigger.addEventListener('focus', show);
  card.addEventListener('pointerenter', () => clearTimeout(timer));
  card.addEventListener('pointerleave', closeSoon);
  row.addEventListener('focusout', (e) => { if (!row.contains(e.relatedTarget)) hide(); });
  row.addEventListener('keydown', (e) => { if (e.key === 'Escape') { hide(); trigger.focus(); } });
});

av17.querySelector('.av-17__theme').addEventListener('click', (e) => {
  const on = av17.dataset.theme !== 'dark';
  av17.dataset.theme = on ? 'dark' : 'light';
  e.currentTarget.setAttribute('aria-pressed', String(on));
});
```
