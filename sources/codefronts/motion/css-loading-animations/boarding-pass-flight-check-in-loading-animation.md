---
source: "codefronts"
url: "https://codefronts.com/motion/css-loading-animations/boarding-pass-flight-check-in-loading-animation/"
title: "Boarding Pass Flight Check-In Loading Animation"
section: "motion"
category: "css-loading-animations"
category_name: "CSS Loading Animations"
description: "Airline check-in has a natural loading beat — the moment the pass is issued."
has_js: "true"
---

Here's a working CSS Loading Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Boarding Pass Flight Check-In Loading Animation
Source: https://codefronts.com/motion/css-loading-animations/boarding-pass-flight-check-in-loading-animation/

Airline check-in has a natural loading beat — the moment the pass is issued. This loader builds a real boarding pass: a perforated stub punched with mask, a barcode that prints bar-by-bar with steps(), a plane crossing the SFO → LHR route line, and a gate that stays · · until assignment lands. All the pieces of a ticket UI you can reuse beyond the loader.
## HTML
```html
<div class="la-10" data-state="loading">
  <div class="la-10__chrome">
    <button class="la-10__btn la-10__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
      <svg class="la-10__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
      <svg class="la-10__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
    </button>
    <button class="la-10__btn la-10__done" type="button" aria-pressed="false" aria-label="Show completed state">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m5 12.6 4.4 4.4L19 7.4"/></svg>
    </button>
  </div>

  <section class="la-10__pass" role="status" aria-live="polite" aria-label="Checking in, gate not yet assigned">
    <header class="la-10__top">
      <p class="la-10__air">Meridian Air <span aria-hidden="true">·</span> MA 418</p>
      <p class="la-10__state"><span class="la-10__load">Checking in</span><span class="la-10__ready">Boarding pass ready</span></p>
    </header>

    <div class="la-10__route">
      <span class="la-10__code-a">SFO</span>
      <span class="la-10__line" aria-hidden="true">
        <i class="la-10__plane">
          <svg viewBox="0 0 24 24" focusable="false"><path d="M2.5 13.4 21 5.5l-4 8.2 1.4 5.6-3.1-1.1-2.4 3-1.5-5.1z"/></svg>
        </i>
      </span>
      <span class="la-10__code-b">LHR</span>
    </div>

    <dl class="la-10__grid">
      <div><dt>Passenger</dt><dd>Priya Sharma</dd></div>
      <div><dt>Gate</dt><dd id="la-10-gate" class="la-10__pending">· ·</dd></div>
      <div><dt>Seat</dt><dd id="la-10-seat" class="la-10__pending">· ·</dd></div>
      <div><dt>Boards</dt><dd>10:15 AM</dd></div>
    </dl>

    <div class="la-10__stub">
      <span class="la-10__bars" aria-hidden="true"></span>
      <p class="la-10__ref">MA418 · 12 MAY · ZONE 2</p>
    </div>
  </section>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap');

.la-10 {
  --bg: #eef1f6;
  --surface: #ffffff;
  --stub: #f4f6fa;
  --ink: #0d1220;
  --muted: #69748a;
  --line: #e0e5ee;
  --acc: #1d4ed8;
  --ok: #0f9d63;
  --ring: #1d4ed8;
  --shadow: rgba(13,18,32,.18);
  --dur: 3.4s;
  --serif: "Instrument Serif",ui-serif,Georgia,serif;
  --sans: "Geist",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "Geist Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
  background: radial-gradient(100% 65% at 50% -10%, color-mix(in oklab,var(--acc) 16%,transparent), transparent 60%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.la-10,
.la-10 *,
.la-10 *::before,
.la-10 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0 0 0)) {
  .la-10 {
    --acc: oklch(50% .21 264);
    --ok: oklch(62% .15 158);
  }
}

.la-10__pass {
  position: relative;
  inline-size: min(23.5rem,100%);
  display: grid;
  gap: 1rem;
  padding: 1.35rem 1.35rem 0;
  border-radius: 1.4rem;
  background: var(--surface);
  color: var(--ink);
  box-shadow: 0 36px 66px -40px var(--shadow), 0 1px 0 #fff inset;
  -webkit-mask: radial-gradient(circle 10px at 0 71%, transparent 98%, #000) , radial-gradient(circle 10px at 100% 71%, transparent 98%, #000);
  -webkit-mask-composite: source-in;
  mask: radial-gradient(circle 10px at 0 71%, transparent 98%, #000) , radial-gradient(circle 10px at 100% 71%, transparent 98%, #000);
  mask-composite: intersect;
}

.la-10__top {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: .75rem;
}

.la-10__air {
  margin: 0;
  font-family: var(--serif);
  font-size: 1.28rem;
  letter-spacing: -.01em;
}

.la-10__state {
  margin: 0;
  font-family: var(--mono);
  font-size: .64rem;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--acc);
}

.la-10__ready {
  display: none;
}

.la-10__route {
  display: grid;
  grid-template-columns: auto 1fr auto;
  align-items: center;
  gap: .75rem;
}

.la-10__code-a,
.la-10__code-b {
  font-family: var(--sans);
  font-size: 1.5rem;
  font-weight: 600;
  letter-spacing: -.03em;
}

.la-10__line {
  position: relative;
  block-size: 1.4rem;
  border-block-end: 2px dashed color-mix(in oklab,var(--ink) 22%,transparent);
  margin-block-end: .35rem;
}

.la-10__plane {
  position: absolute;
  inset-block-end: -.7rem;
  inset-inline-start: 0;
  inline-size: 1.35rem;
  block-size: 1.35rem;
  color: var(--acc);
  animation: la-10-fly var(--dur) cubic-bezier(.5,0,.5,1) infinite;
}

.la-10__plane svg {
  inline-size: 100%;
  block-size: 100%;
  fill: currentColor;
}

@keyframes la-10-fly {
  0% {
    translate: 0 0;
    rotate: 0deg;
    opacity: 0;
  }

  12% {
    opacity: 1;
  }

  50% {
    rotate: -6deg;
  }

  88% {
    opacity: 1;
  }

  100% {
    translate: calc(100% + 6.4rem) -.15rem;
    rotate: 0deg;
    opacity: 0;
  }
}

.la-10__grid {
  margin: 0;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: .7rem 1rem;
  padding-block-end: .9rem;
  border-block-end: 1px solid var(--line);
}

.la-10__grid dt {
  margin: 0 0 .1rem;
  font-family: var(--mono);
  font-size: .6rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.la-10__grid dd {
  margin: 0;
  font-size: .95rem;
  font-weight: 500;
  font-variant-numeric: tabular-nums;
}

.la-10__pending {
  color: var(--muted);
  letter-spacing: .2em;
  animation: la-10-wait 1.4s ease-in-out infinite alternate;
}

@keyframes la-10-wait {
  from {
    opacity: .35;
  }

  to {
    opacity: .9;
  }
}

.la-10__stub {
  margin-inline: -1.35rem;
  padding: 1rem 1.35rem 1.1rem;
  background: var(--stub);
  border-block-start: 1px dashed color-mix(in oklab,var(--ink) 18%,transparent);
  display: grid;
  gap: .5rem;
  justify-items: center;
}

.la-10__bars {
  block-size: 2.5rem;
  inline-size: 0;
  max-inline-size: 100%;
  background: repeating-linear-gradient(90deg,
      var(--ink) 0 2px, transparent 2px 4px, var(--ink) 4px 7px, transparent 7px 10px,
      var(--ink) 10px 11px, transparent 11px 14px, var(--ink) 14px 17px, transparent 17px 19px);
  background-size: 19px 100%;
  animation: la-10-print var(--dur) steps(18, jump-none) infinite;
}

@keyframes la-10-print {
  from {
    inline-size: 0;
  }

  to {
    inline-size: 100%;
  }
}

.la-10__ref {
  margin: 0;
  font-family: var(--mono);
  font-size: .62rem;
  letter-spacing: .14em;
  color: var(--muted);
}

.la-10.is-ready .la-10__plane,
.la-10.is-ready .la-10__bars,
.la-10.is-ready .la-10__pending {
  animation: none;
}

.la-10.is-ready .la-10__plane {
  translate: calc(100% + 3rem) -.15rem;
  opacity: 1;
}

.la-10.is-ready .la-10__bars {
  inline-size: 100%;
}

.la-10.is-ready .la-10__pending {
  color: var(--ink);
  letter-spacing: 0;
  opacity: 1;
}

.la-10.is-ready .la-10__load {
  display: none;
}

.la-10.is-ready .la-10__ready {
  display: inline;
}

.la-10.is-ready .la-10__state {
  color: var(--ok);
}

.la-10__chrome {
  position: absolute;
  inset-block-start: clamp(.75rem,2.5vw,1.5rem);
  inset-inline-end: clamp(.75rem,2.5vw,1.5rem);
  z-index: 20;
  display: flex;
  gap: .5rem;
}

.la-10__btn {
  inline-size: 2.75rem;
  block-size: 2.75rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  padding: 0;
  border-radius: 999px;
  border: 1px solid color-mix(in oklab,var(--ink) 16%,transparent);
  color: var(--ink);
  background: color-mix(in oklab,var(--surface) 72%,transparent);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  transition: background .25s ease, transform .25s cubic-bezier(.16,1,.3,1);
}

.la-10__btn:hover {
  background: var(--surface);
  transform: translateY(-1px);
}

.la-10__btn:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}

.la-10__btn svg {
  grid-area: 1/1;
  inline-size: 1.15rem;
  block-size: 1.15rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.la-10__sun {
  display: none;
}

.la-10__theme[aria-pressed="true"] .la-10__sun {
  display: block;
}

.la-10__theme[aria-pressed="true"] .la-10__moon {
  display: none;
}

.la-10__done[aria-pressed="true"] {
  background: var(--ok);
  border-color: transparent;
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .la-10:not([data-theme="light"]) {
    --bg: #070910;
    --surface: #121722;
    --stub: #0d121b;
    --ink: #eef2f8;
    --muted: #8f9bb0;
    --line: #222a38;
    --acc: #7aa2ff;
    --ok: #31d68f;
    --ring: #7aa2ff;
    --shadow: rgba(0,0,0,.7);
  }

  .la-10:not([data-theme="light"]) .la-10__pass {
    box-shadow: 0 40px 70px -40px #000, 0 1px 0 rgba(255,255,255,.05) inset;
  }

  .la-10:not([data-theme="light"]) .la-10__done[aria-pressed="true"] {
    color: #04231a;
  }
}

.la-10[data-theme="dark"] {
  --bg: #070910;
  --surface: #121722;
  --stub: #0d121b;
  --ink: #eef2f8;
  --muted: #8f9bb0;
  --line: #222a38;
  --acc: #7aa2ff;
  --ok: #31d68f;
  --ring: #7aa2ff;
  --shadow: rgba(0,0,0,.7);
}

.la-10[data-theme="dark"] .la-10__pass {
  box-shadow: 0 40px 70px -40px #000, 0 1px 0 rgba(255,255,255,.05) inset;
}

.la-10[data-theme="dark"] .la-10__done[aria-pressed="true"] {
  color: #04231a;
}

@media (prefers-reduced-motion: reduce) {
  .la-10 * {
    animation: none !important;
    transition: none !important;
  }

  .la-10__bars {
    inline-size: 76%;
  }

  .la-10__plane {
    translate: 8rem -.15rem;
    opacity: 1;
  }

  .la-10__pending {
    opacity: .8;
  }
}

@media (forced-colors: active) {
  .la-10__pass {
    border: 1px solid CanvasText;
  }

  .la-10__bars {
    background: CanvasText;
  }

  .la-10__btn {
    border: 1px solid ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.la-10');
  if (!root) return;
  const theme = root.querySelector('.la-10__theme');
  const done = root.querySelector('.la-10__done');
  const gate = root.querySelector('#la-10-gate');
  const seat = root.querySelector('#la-10-seat');
  const region = root.querySelector('[role="status"]');
  const dark = () => (root.dataset.theme || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light')) === 'dark';
  const sync = () => {
    theme.setAttribute('aria-pressed', String(dark()));
    theme.setAttribute('aria-label', dark() ? 'Switch to light theme' : 'Switch to dark theme');
  };
  theme.addEventListener('click', () => { root.dataset.theme = dark() ? 'light' : 'dark'; sync(); });
  matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => { if (!root.dataset.theme) sync(); });
  done.addEventListener('click', () => {
    const ready = root.classList.toggle('is-ready');        // check-in API resolved
    root.dataset.state = ready ? 'ready' : 'loading';
    done.setAttribute('aria-pressed', String(ready));
    done.setAttribute('aria-label', ready ? 'Return to loading state' : 'Show completed state');
    gate.textContent = ready ? 'B14' : '· ·';               // gate and seat land together, never early
    seat.textContent = ready ? '22A' : '· ·';
    region.setAttribute('aria-label', ready ? 'Boarding pass ready, gate B14, seat 22A' : 'Checking in, gate not yet assigned');
  });
  sync();
})();
```
