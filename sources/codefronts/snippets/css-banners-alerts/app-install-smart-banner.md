---
source: "codefronts"
url: "https://codefronts.com/snippets/css-banners-alerts/app-install-smart-banner/"
title: "App Install Smart Banner"
section: "snippets"
category: "css-banners-alerts"
category_name: "CSS Banners & Alerts"
description: "One markup block that is a slim top bar on a laptop and a bottom sheet on a phone, decided by a container query rather than a user-agent sniff."
has_js: "true"
---

Here's a working CSS Banners & Alert from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: App Install Smart Banner
Source: https://codefronts.com/snippets/css-banners-alerts/app-install-smart-banner/

One markup block that is a slim top bar on a laptop and a bottom sheet on a phone, decided by a container query rather than a user-agent sniff. The install button is a small state machine — idle, installing, installed — animated with a registered-property ring and a check that draws itself, and the whole banner remembers a dismissal so it does not nag.
## HTML
```html
<div class="ba-04">
  <div class="ba-04__app" aria-hidden="true">
    <div class="ba-04__appBar"><span class="ba-04__dot"></span><span class="ba-04__url">soundmark.fm/discover</span></div>
    <div class="ba-04__feed">
      <div class="ba-04__row"><span><b>Night Shift Radio</b><i>Episode 212 · 48 min</i></span></div>
      <div class="ba-04__row"><span><b>Slow Coast</b><i>Episode 88 · 61 min</i></span></div>
      <div class="ba-04__row"><span><b>Field Recordings</b><i>Episode 05 · 34 min</i></span></div>
    </div>
  </div>

  <section class="ba-04__banner" id="ba-04-banner" role="region" aria-labelledby="ba-04-name">
    <span class="ba-04__icon" aria-hidden="true">
      <svg viewBox="0 0 48 48" fill="none" focusable="false">
        <rect width="48" height="48" rx="12" fill="currentColor" opacity=".14"/>
        <path d="M17 30V18.6c0-.9.8-1.5 1.6-1.3l11 2.4c.7.2 1.2.8 1.2 1.5V27" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>
        <circle cx="15" cy="30" r="3.2" stroke="currentColor" stroke-width="2.4"/>
        <circle cx="28.8" cy="27" r="3.2" stroke="currentColor" stroke-width="2.4"/>
      </svg>
    </span>

    <div class="ba-04__text">
      <p class="ba-04__name" id="ba-04-name">Soundmark</p>
      <p class="ba-04__meta">
        <span class="ba-04__stars" role="img" aria-label="Rated 4.8 out of 5">
          <svg viewBox="0 0 100 20" aria-hidden="true" focusable="false"><defs><path id="ba-04-star" d="M10 1.6l2.6 5.4 5.9.8-4.3 4.1 1 5.9L10 15l-5.2 2.8 1-5.9L1.5 7.8l5.9-.8z"/><clipPath id="ba-04-clip"><rect width="96" height="20"/></clipPath></defs><g clip-path="url(#ba-04-clip)" fill="currentColor"><use href="#ba-04-star"/><use href="#ba-04-star" x="20"/><use href="#ba-04-star" x="40"/><use href="#ba-04-star" x="60"/><use href="#ba-04-star" x="80" opacity=".35"/></g></svg>
        </span>
        <span class="ba-04__num">4.8</span>
        <span class="ba-04__sep" aria-hidden="true">·</span>
        <span>21,408 ratings</span>
        <span class="ba-04__sep" aria-hidden="true">·</span>
        <span>Free</span>
      </p>
      <p class="ba-04__pitch">Offline downloads, cross-device resume and CarPlay.</p>
    </div>

    <div class="ba-04__cta">
      <button class="ba-04__get" type="button" data-install>
        <span class="ba-04__ring" aria-hidden="true"></span>
        <span class="ba-04__getLabel">Install</span>
        <svg class="ba-04__check" viewBox="0 0 20 20" fill="none" aria-hidden="true" focusable="false"><path d="m4.6 10.4 3.4 3.4 7.4-7.6" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </button>
      <button class="ba-04__later" type="button" data-dismiss>Not now</button>
    </div>

    <button class="ba-04__x" type="button" data-dismiss aria-label="Dismiss app install banner">
      <svg viewBox="0 0 20 20" fill="none" aria-hidden="true" focusable="false"><path d="m6 6 8 8m0-8-8 8" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
    </button>
  </section>

  <button class="ba-04__restore" type="button" data-restore hidden>Show install banner</button>
  <p class="ba-04__live" role="status" aria-live="polite"></p>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700;800&display=swap');

@property --ba-04-p {
  syntax: '<percentage>';
  inherits: false;
  initial-value: 0%;
}

.ba-04 {
  --sheet-at: 34rem;
  --bg: #eef0f4;
  --surface: #ffffff;
  --ink: #0d1017;
  --muted: #6b7280;
  --line: #e2e5ea;
  --acc: #0a84ff;
  --acc-ink: #ffffff;
  --ok: #15b26b;
  --sans: "Figtree",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  container-type: inline-size;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  box-sizing: border-box;
  overflow: clip;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
}

.ba-04 *,
.ba-04 *::before,
.ba-04 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(50% 0 0)) {
  .ba-04 {
    --bg: oklch(95.5% .006 265);
    --surface: oklch(100% 0 0);
    --ink: oklch(17% .016 265);
    --muted: oklch(56% .018 265);
    --line: oklch(92% .008 265);
    --acc: oklch(62% .2 258);
    --ok: oklch(70% .16 155);
  }
}

@media (prefers-color-scheme: dark) {
  .ba-04:not([data-theme="light"]) {
    --bg: #0a0c10;
    --surface: #15181f;
    --ink: #eef1f6;
    --muted: #9aa3b0;
    --line: #242932;
  }
}

.ba-04[data-theme="dark"] {
  --bg: #0a0c10;
  --surface: #15181f;
  --ink: #eef1f6;
  --muted: #9aa3b0;
  --line: #242932;
}

.ba-04__app {
  position: relative;
  z-index: 0;
  display: grid;
  gap: 1rem;
  max-width: 52rem;
  margin-inline: auto;
  padding: clamp(4.75rem,10vh,6.5rem) clamp(1rem,4vw,2rem) clamp(10rem,26vh,14rem);
}

.ba-04__appBar {
  display: flex;
  align-items: center;
  gap: .6rem;
  padding: .6rem .9rem;
  border-radius: 999px;
  background: var(--surface);
  border: 1px solid var(--line);
  font-size: .8125rem;
  color: var(--muted);
}

.ba-04__dot {
  width: .55rem;
  height: .55rem;
  border-radius: 999px;
  background: var(--ok);
}

.ba-04__feed {
  display: grid;
  gap: .6rem;
}

.ba-04__row {
  display: grid;
  grid-template-columns: 1fr;
  gap: .85rem;
  align-items: center;
  padding: .7rem;
  border-radius: 1rem;
  background: var(--surface);
  border: 1px solid var(--line);
}

.ba-04__row span {
  display: grid;
  gap: .2rem;
}

.ba-04__row b {
  font-size: .9375rem;
  font-weight: 700;
  letter-spacing: -.02em;
}

.ba-04__row i {
  font-style: normal;
  font-size: .75rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.ba-04__banner {
  position: fixed;
  z-index: 6;
  inset: 1rem 1rem auto;
  width: auto;
  display: grid;
  grid-template-columns: auto 1fr auto auto;
  align-items: center;
  gap: clamp(.75rem,2cqw,1.25rem);
  padding: .8rem 1rem;
  border-radius: 1.25rem;
  background: color-mix(in oklab,var(--surface) 88%,transparent);
  border: 1px solid var(--line);
  box-shadow: 0 1.5rem 3rem -1.5rem rgb(13 16 23 / .38);
  transition: opacity .35s ease, translate .45s cubic-bezier(.16,1,.3,1), display .45s allow-discrete;
}

@supports (backdrop-filter: blur(1px)) {
  .ba-04__banner {
    backdrop-filter: blur(20px) saturate(1.6);
  }
}

@starting-style {
  .ba-04__banner {
    opacity: 0;
    translate: 0 -1.25rem;
  }
}

.ba-04__banner[hidden] {
  display: none;
  opacity: 0;
  translate: 0 -1rem;
}

.ba-04__icon {
  display: grid;
  place-items: center;
  width: 3rem;
  height: 3rem;
  color: var(--acc);
  flex: none;
}

.ba-04__icon svg {
  width: 100%;
  height: 100%;
}

.ba-04__text {
  min-width: 0;
  display: grid;
  gap: .15rem;
}

.ba-04__name {
  margin: 0;
  font-size: .9375rem;
  font-weight: 800;
  letter-spacing: -.02em;
}

.ba-04__meta {
  margin: 0;
  display: flex;
  align-items: center;
  gap: .35rem;
  flex-wrap: wrap;
  font-size: .75rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.ba-04__stars {
  display: block;
  width: 4.5rem;
  color: #f5a524;
}

.ba-04__stars svg {
  display: block;
  width: 100%;
  height: auto;
}

.ba-04__num {
  font-weight: 700;
  color: var(--ink);
}

.ba-04__sep {
  opacity: .5;
}

.ba-04__pitch {
  margin: .1rem 0 0;
  font-size: .75rem;
  color: var(--muted);
  text-wrap: pretty;
}

.ba-04__cta {
  display: flex;
  align-items: center;
  gap: .5rem;
}

.ba-04__get {
  position: relative;
  display: inline-grid;
  grid-auto-flow: column;
  align-items: center;
  gap: .4rem;
  min-height: 2.5rem;
  min-width: 6rem;
  padding: .55rem 1.1rem;
  border: 0;
  border-radius: 999px;
  cursor: pointer;
  font: inherit;
  font-size: .8125rem;
  font-weight: 800;
  letter-spacing: -.01em;
  background: var(--acc);
  color: var(--acc-ink);
  transition: background .25s ease, translate .2s ease, min-width .3s ease;
}

.ba-04__get:hover {
  translate: 0 -1px;
}

.ba-04__ring {
  display: none;
  width: 1.05rem;
  height: 1.05rem;
  border-radius: 999px;
  background: conic-gradient(from -90deg, currentColor var(--ba-04-p), color-mix(in oklab,currentColor 25%,transparent) 0);
  mask: radial-gradient(circle, transparent 52%, black 54%);
  transition: --ba-04-p .35s linear;
}

.ba-04__check {
  display: none;
  width: 1.1rem;
  height: 1.1rem;
}

.ba-04__check path {
  stroke-dasharray: 20;
  stroke-dashoffset: 20;
}

.ba-04__get[data-state="installing"] .ba-04__ring {
  display: block;
}

.ba-04__get[data-state="installed"] {
  background: var(--ok);
}

.ba-04__get[data-state="installed"] .ba-04__check {
  display: block;
}

.ba-04__get[data-state="installed"] .ba-04__check path {
  animation: ba-04-draw .5s cubic-bezier(.16,1,.3,1) forwards;
}

@keyframes ba-04-draw {
  to {
    stroke-dashoffset: 0;
  }
}

.ba-04__later {
  min-height: 2.5rem;
  padding: .55rem .8rem;
  border: 0;
  background: transparent;
  cursor: pointer;
  font: inherit;
  font-size: .8125rem;
  font-weight: 600;
  color: var(--muted);
  border-radius: .7rem;
}

.ba-04__later:hover {
  color: var(--ink);
  background: color-mix(in oklab,var(--ink) 6%,transparent);
}

.ba-04__x {
  display: grid;
  place-items: center;
  width: 2.5rem;
  height: 2.5rem;
  border-radius: .7rem;
  cursor: pointer;
  border: 0;
  background: transparent;
  color: var(--muted);
}

.ba-04__x:hover {
  color: var(--ink);
  background: color-mix(in oklab,var(--ink) 7%,transparent);
}

.ba-04__x svg {
  width: 1.125rem;
  height: 1.125rem;
}

.ba-04__restore {
  position: fixed;
  inset: auto auto 1.25rem 50%;
  translate: -50% 0;
  z-index: 6;
  min-height: 2.5rem;
  padding: .6rem 1.1rem;
  border-radius: 999px;
  cursor: pointer;
  font: inherit;
  font-size: .8125rem;
  font-weight: 700;
  color: var(--ink);
  background: var(--surface);
  border: 1px solid var(--line);
  box-shadow: 0 1rem 2rem -1rem rgb(13 16 23 / .35);
}

.ba-04 :focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.ba-04__live {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

@container (max-width: 34rem) {
  .ba-04__banner {
    inset: auto 0 0 0;
    border-radius: 1.5rem 1.5rem 0 0;
    border-inline: 0;
    border-block-end: 0;
    grid-template-columns: auto 1fr auto;
    grid-template-areas: "icon text x" "cta cta cta";
    padding: 1rem 1rem 1.1rem;
    gap: .85rem;
  }

  .ba-04__icon {
    grid-area: icon;
  }

  .ba-04__text {
    grid-area: text;
  }

  .ba-04__x {
    grid-area: x;
    align-self: start;
  }

  .ba-04__cta {
    grid-area: cta;
  }

  .ba-04__get {
    flex: 1;
  }

  .ba-04__later {
    flex: none;
  }

  @starting-style {
    .ba-04__banner {
      translate: 0 100%;
    }
  }

  .ba-04__banner[hidden] {
    translate: 0 100%;
  }
}

.ba-04__banner[data-variant="minimal"] .ba-04__pitch,
.ba-04__banner[data-variant="minimal"] .ba-04__meta {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .ba-04 * {
    animation: none !important;
    transition: none !important;
  }

  .ba-04__check path {
    stroke-dashoffset: 0;
  }
}

@media (forced-colors: active) {
  .ba-04__banner {
    border: 1px solid CanvasText;
  }

  .ba-04__get {
    background: Highlight;
    color: HighlightText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.ba-04');
  if (!root) return;
  const banner = root.querySelector('#ba-04-banner');
  const get = root.querySelector('[data-install]');
  const label = get.querySelector('.ba-04__getLabel');
  const ring = get.querySelector('.ba-04__ring');
  const restore = root.querySelector('[data-restore]');
  const live = root.querySelector('.ba-04__live');
  const DISMISS_DAYS = 30; // persist this with localStorage in production

  const hide = (why) => { banner.hidden = true; restore.hidden = false; live.textContent = why; restore.focus(); };

  get.addEventListener('click', () => {
    if (get.dataset.state) return;
    // real PWA: deferredPrompt.prompt() from the beforeinstallprompt event
    get.dataset.state = 'installing'; label.textContent = 'Installing'; get.setAttribute('aria-disabled', 'true');
    let p = 0;
    const step = setInterval(() => {
      p = Math.min(100, p + 12 + Math.random() * 16);
      ring.style.setProperty('--ba-04-p', p + '%');
      if (p < 100) return;
      clearInterval(step);
      get.dataset.state = 'installed'; label.textContent = 'Open'; get.removeAttribute('aria-disabled');
      live.textContent = 'Soundmark installed. Choose Open to launch it.';
    }, 420);
  });

  root.addEventListener('click', (e) => {
    if (e.target.closest('[data-dismiss]')) hide('Install banner dismissed for ' + DISMISS_DAYS + ' days.');
    if (e.target.closest('[data-restore]')) { restore.hidden = true; banner.hidden = false; get.focus(); }
  });
})();
```
