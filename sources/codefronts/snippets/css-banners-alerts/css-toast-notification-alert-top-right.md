---
source: "codefronts"
url: "https://codefronts.com/snippets/css-banners-alerts/css-toast-notification-alert-top-right/"
title: "Limited Stock Urgency Banner"
section: "snippets"
category: "css-banners-alerts"
category_name: "CSS Banners & Alerts"
description: "A scarcity banner wired to a proper top-right toast stack: toasts enter with @starting-style, stack with a --i index, run their own auto-dismiss timer as a…"
has_js: "true"
---

Here's a working CSS Banners & Alert from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Limited Stock Urgency Banner
Source: https://codefronts.com/snippets/css-banners-alerts/css-toast-notification-alert-top-right/

A scarcity banner wired to a proper top-right toast stack: toasts enter with @starting-style, stack with a --i index, run their own auto-dismiss timer as a CSS animation, and get removed on animationend — so the timing lives in the stylesheet where a designer can tune it, not buried in a setTimeout.
## HTML
```html
<div class="ba-08" style="--critical-at:8">
  <section class="ba-08__product" aria-labelledby="ba-08-h">
    <figure class="ba-08__media" aria-hidden="true">
      <span class="ba-08__swatch" aria-hidden="true"></span>
      <figcaption class="ba-08__tagline">Rev. 04</figcaption>
    </figure>

    <div class="ba-08__info">
      <p class="ba-08__brand">Atelier Audio</p>
      <h2 class="ba-08__h" id="ba-08-h">Monitor One, closed-back</h2>
      <p class="ba-08__price"><strong>£249</strong><s>£310</s><span class="ba-08__save">Save 20%</span></p>

      <div class="ba-08__stock" data-stock>
        <p class="ba-08__stockLine">
          <span class="ba-08__pulse" aria-hidden="true"></span>
          <span data-stocktext>Only <strong data-left>6</strong> left in Matte Black</span>
        </p>
        <div class="ba-08__bar" role="progressbar" aria-label="Stock remaining" aria-valuemin="0" aria-valuemax="24" aria-valuenow="6" data-bar>
          <span data-barfill></span>
        </div>
        <p class="ba-08__stockMeta"><span data-viewers>12</span> people viewing · restock ETA <time datetime="2026-09-08">8 Sep</time></p>
      </div>

      <div class="ba-08__variants" role="group" aria-label="Colour">
        <button type="button" data-variant="Matte Black" data-count="6" aria-pressed="true"><span style="--sw:#22252a" aria-hidden="true"></span>Matte Black</button>
        <button type="button" data-variant="Bone" data-count="19" aria-pressed="false"><span style="--sw:#e8e2d6" aria-hidden="true"></span>Bone</button>
        <button type="button" data-variant="Cobalt" data-count="2" aria-pressed="false"><span style="--sw:#2b49c9" aria-hidden="true"></span>Cobalt</button>
      </div>

      <div class="ba-08__buy">
        <button class="ba-08__add" type="button" data-add>Add to basket</button>
        <button class="ba-08__wish" type="button" data-wish aria-pressed="false">
          <svg viewBox="0 0 20 20" fill="none" aria-hidden="true" focusable="false"><path d="M10 16.2S3.4 12.4 3.4 8.2A3.4 3.4 0 0 1 10 6.6a3.4 3.4 0 0 1 6.6 1.6c0 4.2-6.6 8-6.6 8z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>
          <span class="ba-08__vh">Save for later</span>
        </button>
      </div>
      <p class="ba-08__ship">Free next-day delivery · 30-day returns · 2-year warranty</p>
    </div>
  </section>

  <div class="ba-08__stack" data-stack></div>
  <p class="ba-08__live" role="status" aria-live="polite"></p>

  <template data-tpl>
    <div class="ba-08__toast" role="group" tabindex="-1">
      <span class="ba-08__tIcon" aria-hidden="true"></span>
      <div class="ba-08__tBody"><p class="ba-08__tTitle"></p><p class="ba-08__tMsg"></p></div>
      <button class="ba-08__tX" type="button" aria-label="Dismiss notification">
        <svg viewBox="0 0 20 20" fill="none" aria-hidden="true" focusable="false"><path d="m6 6 8 8m0-8-8 8" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
      </button>
      <span class="ba-08__tTimer" aria-hidden="true"></span>
    </div>
  </template>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

.ba-08 {
  --bg: #0f1012;
  --surface: #181a1d;
  --ink: #f4f5f6;
  --muted: #9b9fa6;
  --line: #26292e;
  --acc: #ff4d3d;
  --ok: #2fbf71;
  --warn: #ffb020;
  --info: #4d9dff;
  --sans: "Plus Jakarta Sans",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  box-sizing: border-box;
  padding: clamp(1rem,4vw,3rem);
  background: radial-gradient(48rem 32rem at 80% 0%, color-mix(in oklab,var(--acc) 14%,transparent), transparent 65%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
}

.ba-08 *,
.ba-08 *::before,
.ba-08 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(50% 0 0)) {
  .ba-08 {
    --bg: oklch(16% .008 265);
    --surface: oklch(21% .01 265);
    --ink: oklch(96% .004 265);
    --muted: oklch(70% .012 265);
    --line: oklch(29% .012 265);
    --acc: oklch(66% .21 30);
    --ok: oklch(72% .16 155);
    --warn: oklch(80% .16 78);
    --info: oklch(68% .16 255);
  }
}

@media (prefers-color-scheme: light) {
  .ba-08:not([data-theme="dark"]) {
    --bg: #f4f5f7;
    --surface: #ffffff;
    --ink: #111316;
    --muted: #5f656e;
    --line: #e3e6ea;
  }
}

.ba-08[data-theme="light"] {
  --bg: #f4f5f7;
  --surface: #ffffff;
  --ink: #111316;
  --muted: #5f656e;
  --line: #e3e6ea;
}

.ba-08__product {
  container-type: inline-size;
  width: min(56rem,100%);
  display: grid;
  grid-template-columns: minmax(0,1fr) minmax(0,1.1fr);
  gap: clamp(1.25rem,4cqw,2.5rem);
  align-items: center;
  padding: clamp(1rem,3vw,1.75rem);
  border-radius: 1.75rem;
  background: var(--surface);
  border: 1px solid var(--line);
  box-shadow: 0 3rem 6rem -3rem rgb(0 0 0 / .6);
}

.ba-08__media {
  --sw: #22252a;
  position: relative;
  margin: 0;
  aspect-ratio: 1;
  border-radius: 1.25rem;
  overflow: hidden;
  display: grid;
  place-items: center;
  background: radial-gradient(80% 60% at 50% 12%, color-mix(in oklab,var(--sw) 34%,transparent), transparent 70%), var(--line);
  transition: background .5s ease;
}

.ba-08__swatch {
  width: 58%;
  aspect-ratio: 1;
  border-radius: 50%;
  background: radial-gradient(closest-side at 34% 28%, color-mix(in oklab,#fff 30%,var(--sw)), var(--sw) 72%), var(--sw);
  box-shadow: inset 0 -1.5rem 3rem -1rem rgb(0 0 0 / .55), 0 2rem 4rem -1.5rem color-mix(in oklab,var(--sw) 60%,transparent);
  transition: background .5s ease, box-shadow .5s ease;
}

.ba-08__media::after {
  content: "";
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: conic-gradient(from 140deg, transparent 0 42%, color-mix(in oklab,#fff 10%,transparent) 50%, transparent 58% 100%);
}

.ba-08__product:has([data-variant="Bone"][aria-pressed="true"]) .ba-08__media {
  --sw: #e8e2d6;
}

.ba-08__product:has([data-variant="Cobalt"][aria-pressed="true"]) .ba-08__media {
  --sw: #2b49c9;
}

@media (prefers-reduced-motion: reduce) {
  .ba-08__media,
    .ba-08__swatch {
    transition: none;
  }
}

.ba-08__tagline {
  position: absolute;
  inset: auto auto .85rem .85rem;
  padding: .3rem .55rem;
  border-radius: .45rem;
  font-size: .625rem;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  background: rgb(0 0 0 / .55);
  color: #fff;
  backdrop-filter: blur(6px);
}

.ba-08__info {
  min-width: 0;
  display: grid;
  gap: .85rem;
  min-width: 0;
}

.ba-08__brand {
  min-width: 0;
  overflow-wrap: anywhere;
  margin: 0;
  font-size: .6875rem;
  font-weight: 700;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--muted);
}

.ba-08__h {
  min-width: 0;
  overflow-wrap: anywhere;
  margin: 0;
  font-size: clamp(1.5rem,4cqw,2.125rem);
  font-weight: 800;
  line-height: 1.05;
  letter-spacing: -.04em;
  text-wrap: balance;
}

.ba-08__price {
  min-width: 0;
  overflow-wrap: anywhere;
  margin: 0;
  display: flex;
  align-items: baseline;
  gap: .6rem;
  font-variant-numeric: tabular-nums;
}

.ba-08__price strong {
  font-size: 1.5rem;
  font-weight: 800;
  letter-spacing: -.03em;
}

.ba-08__price s {
  color: var(--muted);
  font-size: .9375rem;
}

.ba-08__save {
  font-size: .6875rem;
  font-weight: 800;
  padding: .2rem .45rem;
  border-radius: .35rem;
  background: color-mix(in oklab,var(--ok) 18%,transparent);
  color: var(--ok);
}

.ba-08__stock {
  display: grid;
  gap: .5rem;
  padding: .85rem .95rem;
  border-radius: 1rem;
  --sev: var(--warn);
  background: color-mix(in oklab,var(--sev) 10%,transparent);
  border: 1px solid color-mix(in oklab,var(--sev) 26%,transparent);
  transition: background .35s ease, border-color .35s ease;
}

.ba-08__stock[data-level="critical"] {
  --sev: var(--acc);
}

.ba-08__stock[data-level="ok"] {
  --sev: var(--ok);
}

.ba-08__stockLine {
  margin: 0;
  display: flex;
  align-items: center;
  gap: .5rem;
  font-size: .875rem;
  color: var(--ink);
}

.ba-08__stockLine strong {
  font-weight: 800;
  color: var(--sev);
  font-variant-numeric: tabular-nums;
}

.ba-08__pulse {
  position: relative;
  width: .5rem;
  height: .5rem;
  border-radius: 999px;
  flex: none;
  background: var(--sev);
}

.ba-08__pulse::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 999px;
  border: 1.5px solid var(--sev);
  animation: ba-08-ping 1.8s cubic-bezier(.2,.6,.3,1) infinite;
}

@keyframes ba-08-ping {
  0% {
    scale: 1;
    opacity: .8;
  }

  80%,
    100% {
    scale: 3.2;
    opacity: 0;
  }
}

.ba-08__stock[data-level="ok"] .ba-08__pulse::after {
  animation: none;
  opacity: 0;
}

.ba-08__bar {
  height: .375rem;
  border-radius: 999px;
  background: color-mix(in oklab,var(--ink) 12%,transparent);
  overflow: hidden;
}

.ba-08__bar span {
  display: block;
  height: 100%;
  border-radius: 999px;
  background: var(--sev);
  transition: width .6s cubic-bezier(.16,1,.3,1), background .35s ease;
}

.ba-08__stockMeta {
  margin: 0;
  font-size: .6875rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.ba-08__variants {
  display: flex;
  gap: .4rem;
  flex-wrap: wrap;
}

.ba-08__variants button {
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  min-height: 2.5rem;
  padding: .5rem .75rem;
  border-radius: .7rem;
  cursor: pointer;
  font: inherit;
  font-size: .75rem;
  font-weight: 600;
  color: var(--muted);
  background: transparent;
  border: 1px solid var(--line);
  transition: color .2s ease, border-color .2s ease, background .2s ease;
}

.ba-08__variants button span {
  width: .85rem;
  height: .85rem;
  border-radius: 999px;
  background: var(--sw);
  box-shadow: 0 0 0 1px rgb(255 255 255 / .18) inset;
}

.ba-08__variants button:hover {
  color: var(--ink);
  border-color: var(--muted);
}

.ba-08__variants button[aria-pressed="true"] {
  color: var(--ink);
  border-color: var(--ink);
  background: color-mix(in oklab,var(--ink) 8%,transparent);
}

.ba-08__buy {
  display: flex;
  gap: .5rem;
}

.ba-08__add {
  flex: 1;
  min-height: 3.1rem;
  padding: .9rem 1.4rem;
  border: 0;
  border-radius: .95rem;
  cursor: pointer;
  font: inherit;
  font-size: 1rem;
  font-weight: 800;
  letter-spacing: -.02em;
  background: var(--ink);
  color: var(--surface);
  transition: translate .2s cubic-bezier(.16,1,.3,1), box-shadow .25s ease, opacity .2s ease;
}

.ba-08__add:hover {
  translate: 0 -2px;
  box-shadow: 0 1rem 2rem -1rem rgb(0 0 0 / .55);
}

.ba-08__add[aria-disabled="true"] {
  opacity: .5;
  cursor: not-allowed;
  translate: 0 0;
}

.ba-08__wish {
  display: grid;
  place-items: center;
  width: 3.1rem;
  height: 3.1rem;
  border-radius: .95rem;
  cursor: pointer;
  color: var(--muted);
  background: transparent;
  border: 1px solid var(--line);
  transition: color .2s ease, border-color .2s ease, scale .2s ease;
}

.ba-08__wish:hover {
  color: var(--acc);
  border-color: var(--acc);
}

.ba-08__wish[aria-pressed="true"] {
  color: var(--acc);
  border-color: var(--acc);
}

.ba-08__wish[aria-pressed="true"] svg {
  fill: color-mix(in oklab,var(--acc) 30%,transparent);
  scale: 1.05;
}

.ba-08__wish svg {
  width: 1.25rem;
  height: 1.25rem;
  transition: scale .25s cubic-bezier(.34,1.56,.64,1);
}

.ba-08__ship {
  margin: 0;
  font-size: .6875rem;
  color: var(--muted);
}

.ba-08__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.ba-08 :focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}
/* toast stack, top-right */

.ba-08__stack {
  position: fixed;
  z-index: 20;
  inset: 1rem 1rem auto auto;
  display: grid;
  gap: .6rem;
  width: min(23rem,calc(100vw - 2rem));
  pointer-events: none;
}

.ba-08__toast {
  --life: 5s;
  --k: var(--ok);
  position: relative;
  pointer-events: auto;
  display: grid;
  grid-template-columns: auto 1fr auto;
  gap: .7rem;
  align-items: start;
  padding: .85rem .9rem 1rem;
  border-radius: 1rem;
  overflow: hidden;
  background: color-mix(in oklab,var(--surface) 92%,transparent);
  border: 1px solid color-mix(in oklab,var(--k) 32%,var(--line));
  box-shadow: 0 1.5rem 3rem -1.5rem rgb(0 0 0 / .55);
  animation: ba-08-life var(--life) linear forwards;
  transition: opacity .3s ease, translate .35s cubic-bezier(.16,1,.3,1), display .35s allow-discrete;
}

@supports (backdrop-filter: blur(1px)) {
  .ba-08__toast {
    backdrop-filter: blur(16px) saturate(1.4);
  }
}

@starting-style {
  .ba-08__toast {
    opacity: 0;
    translate: 1.5rem 0;
  }
}

.ba-08__toast[data-out] {
  opacity: 0;
  translate: 1.5rem 0;
}

.ba-08__toast:hover,
.ba-08__toast:focus-within {
  animation-play-state: paused;
}

.ba-08__toast[data-kind="warn"] {
  --k: var(--warn);
}

.ba-08__toast[data-kind="info"] {
  --k: var(--info);
}

.ba-08__toast[data-kind="error"] {
  --k: var(--acc);
}

@keyframes ba-08-life {
  to {
    opacity: 1;
  }
}

.ba-08__tIcon {
  display: grid;
  place-items: center;
  width: 1.6rem;
  height: 1.6rem;
  border-radius: .55rem;
  flex: none;
  font-size: .8125rem;
  font-weight: 800;
  color: var(--k);
  background: color-mix(in oklab,var(--k) 16%,transparent);
}

.ba-08__tBody {
  min-width: 0;
}

.ba-08__tTitle {
  margin: 0;
  font-size: .8125rem;
  font-weight: 800;
  letter-spacing: -.01em;
}

.ba-08__tMsg {
  margin: .15rem 0 0;
  font-size: .75rem;
  line-height: 1.5;
  color: var(--muted);
  text-wrap: pretty;
}

.ba-08__tX {
  display: grid;
  place-items: center;
  width: 2.25rem;
  height: 2.25rem;
  margin: -.25rem -.2rem 0 0;
  border: 0;
  border-radius: .6rem;
  cursor: pointer;
  background: transparent;
  color: var(--muted);
}

.ba-08__tX:hover {
  color: var(--ink);
  background: color-mix(in oklab,var(--ink) 8%,transparent);
}

.ba-08__tX svg {
  width: 1rem;
  height: 1rem;
}

.ba-08__tTimer {
  position: absolute;
  inset: auto 0 0 0;
  height: 2px;
  transform-origin: left;
  background: var(--k);
  animation: ba-08-timer var(--life) linear forwards;
}

@keyframes ba-08-timer {
  from {
    scale: 1 1;
  }

  to {
    scale: 0 1;
  }
}

.ba-08__live {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

@container (max-width: 40rem) {
  .ba-08__product {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ba-08 * {
    animation-duration: .001s !important;
    transition: none !important;
  }

  .ba-08__toast {
    animation: ba-08-life var(--life) linear forwards !important;
  }

  .ba-08__tTimer {
    animation: none;
    scale: 1 1;
    opacity: .4;
  }
}

@media (forced-colors: active) {
  .ba-08__toast,
    .ba-08__product {
    border: 1px solid CanvasText;
  }

  .ba-08__add {
    background: Highlight;
    color: HighlightText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.ba-08');
  if (!root) return;
  const stack = root.querySelector('[data-stack]');
  const tpl = root.querySelector('[data-tpl]');
  const live = root.querySelector('.ba-08__live');
  const stock = root.querySelector('[data-stock]');
  const critical = Number(getComputedStyle(root).getPropertyValue('--critical-at')) || 8;
  const MAX = 24;
  let variant = 'Matte Black', left = 6;

  const close = (t) => { t.dataset.out = '1'; setTimeout(() => t.remove(), 340); };

  const toast = (kind, title, msg, glyph, life) => {
    if (stack.children.length >= 3) close(stack.firstElementChild);
    const t = tpl.content.firstElementChild.cloneNode(true);
    t.dataset.kind = kind;
    t.style.setProperty('--life', life || '5s');
    t.querySelector('.ba-08__tIcon').textContent = glyph;
    t.querySelector('.ba-08__tTitle').textContent = title;
    t.querySelector('.ba-08__tMsg').textContent = msg;
    t.querySelector('.ba-08__tX').addEventListener('click', () => close(t));
    t.addEventListener('animationend', (e) => { if (e.animationName === 'ba-08-life') close(t); });
    stack.append(t);
    live.textContent = title + '. ' + msg;
  };

  const paint = () => {
    const pct = Math.max(0, Math.min(100, (left / MAX) * 100));
    stock.dataset.level = left === 0 ? 'critical' : left <= 3 ? 'critical' : left <= critical ? 'low' : 'ok';
    root.querySelector('[data-left]').textContent = left;
    root.querySelector('[data-barfill]').style.width = pct + '%';
    const bar = root.querySelector('[data-bar]');
    bar.setAttribute('aria-valuenow', left);
    bar.setAttribute('aria-valuetext', left + ' of ' + MAX + ' in ' + variant);
    const txt = root.querySelector('[data-stocktext]');
    txt.innerHTML = left === 0 ? '<strong data-left>Sold out</strong> in ' + variant
      : left <= critical ? 'Only <strong data-left>' + left + '</strong> left in ' + variant
      : '<strong data-left>' + left + '</strong> in stock · ' + variant;
    root.querySelector('[data-add]').setAttribute('aria-disabled', String(left === 0));
  };

  root.addEventListener('click', (e) => {
    const v = e.target.closest('[data-variant]');
    if (v) {
      root.querySelectorAll('[data-variant]').forEach((b) => b.setAttribute('aria-pressed', String(b === v)));
      variant = v.dataset.variant; left = Number(v.dataset.count); paint();
      if (left <= 3) toast('warn', variant + ' is nearly gone', 'Only ' + left + ' units left at this price.', '!', '6s');
      return;
    }
    if (e.target.closest('[data-add]')) {
      if (left === 0) return toast('error', 'Out of stock', variant + ' is unavailable — try Bone or join the waitlist.', '×', '7s');
      left -= 1; paint();
      toast('ok', 'Added to basket', 'Monitor One · ' + variant + ' · £249', '✓');
      if (left && left <= 3) toast('warn', 'Stock is critical', 'Only ' + left + ' left — checkout holds your basket for 15 minutes.', '!', '7s');
      if (!left) toast('error', 'That was the last one', 'You took the final ' + variant + '. Restock lands 8 Sep.', '×', '8s');
      return;
    }
    const w = e.target.closest('[data-wish]');
    if (w) {
      const on = w.getAttribute('aria-pressed') === 'false';
      w.setAttribute('aria-pressed', String(on));
      toast('info', on ? 'Saved for later' : 'Removed from saved', on ? 'We will email you if the price drops.' : 'Monitor One is no longer on your list.', '♥', '4s');
    }
  });

  const viewers = root.querySelector('[data-viewers]');
  setInterval(() => { viewers.textContent = 9 + Math.floor(Math.random() * 8); }, 5200);
  paint();
})();
```
