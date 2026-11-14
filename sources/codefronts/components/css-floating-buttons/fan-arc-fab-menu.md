---
source: "codefronts"
url: "https://codefronts.com/components/css-floating-buttons/fan-arc-fab-menu/"
title: "Fan and Arc Radial Spread FAB Menu CSS"
section: "components"
category: "css-floating-buttons"
category_name: "CSS Floating Buttons"
description: "Cards fanned from a deck: items spread along an arc, each rotated to face outward from the hub, with a dotted guide showing the path they travel."
has_js: "true"
---

Here's a working CSS Floating Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Fan and Arc Radial Spread FAB Menu CSS
Source: https://codefronts.com/components/css-floating-buttons/fan-arc-fab-menu/

Cards fanned from a deck: items spread along an arc, each rotated to face outward from the hub, with a dotted guide showing the path they travel. The spread angle is a live control — drag it from a tight 40° cluster to a full 180° sweep and watch the trig re-solve. This is the expressive cousin of the speed dial, for launchers that want to be noticed.
## HTML
```html
<section class="fb-14" aria-label="Fan and arc radial spread menu demo">
  <div class="fb-14__page">
    <p class="fb-14__eyebrow">cos · sin · per-item rotation</p>
    <h2 class="fb-14__title">A hand of cards, dealt on an arc</h2>
    <p class="fb-14__sub">Every item faces outward from the hub. Change the spread and the whole fan re-solves — no per-item JavaScript.</p>
    <div class="fb-14__ctl">
      <label class="fb-14__lab" for="fb-14-spread">Spread</label>
      <input class="fb-14__range" id="fb-14-spread" type="range" min="40" max="180" step="5" value="110" aria-describedby="fb-14-out">
      <output class="fb-14__out" id="fb-14-out" for="fb-14-spread">110°</output>
    </div>
  </div>
  <div class="fb-14__hub" id="fb-14-hub" data-open="false" style="--fb-14-spread:110deg">
    <svg class="fb-14__guide" viewBox="0 0 400 400" aria-hidden="true" focusable="false"><circle cx="200" cy="200" r="150" fill="none" stroke="currentColor" stroke-width="1.5" stroke-dasharray="4 9"/></svg>
    <ul class="fb-14__items" id="fb-14-items" style="--fb-14-n:5">
      <li style="--fb-14-i:0"><button class="fb-14__item" type="button" tabindex="-1" aria-label="Camera"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><rect x="3" y="7" width="18" height="13" rx="2.5" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="12" cy="13.5" r="3.4" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M9 7l1.3-2.2h3.4L15 7" fill="none" stroke="currentColor" stroke-width="1.8"/></svg></button></li>
      <li style="--fb-14-i:1"><button class="fb-14__item" type="button" tabindex="-1" aria-label="Music"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M9 18V6l10-2v12" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><circle cx="7" cy="18" r="2.4" fill="currentColor"/><circle cx="17" cy="16" r="2.4" fill="currentColor"/></svg></button></li>
      <li style="--fb-14-i:2"><button class="fb-14__item" type="button" tabindex="-1" aria-label="Gallery"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><rect x="3" y="5" width="18" height="14" rx="2.4" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M4 16l4.5-4.5L12 15l3-3 5 5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><circle cx="8.5" cy="9.5" r="1.5" fill="currentColor"/></svg></button></li>
      <li style="--fb-14-i:3"><button class="fb-14__item" type="button" tabindex="-1" aria-label="Video"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><rect x="3" y="6" width="12" height="12" rx="2.4" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M15 11l6-3.5v9L15 13z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg></button></li>
      <li style="--fb-14-i:4"><button class="fb-14__item" type="button" tabindex="-1" aria-label="Link"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 1 0-5.7-5.7L11.5 6.8" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/><path d="M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 1 0 5.7 5.7l1.5-1.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg></button></li>
    </ul>
    <button class="fb-14__fab" id="fb-14-fab" type="button" aria-expanded="false" aria-controls="fb-14-items" aria-label="Open attachment fan">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 5v14M5 12h14" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg>
    </button>
  </div>
</section>
```
## CSS
```css
.fb-14 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--fb-14-bg);
  --fb-14-bg: radial-gradient(115% 85% at 50% 100%,oklch(0.3 0.07 195),oklch(0.16 0.03 210) 72%);
  --fb-14-accent: oklch(0.82 0.16 175);
  --fb-14-ink: oklch(0.97 0.01 200);
  --fb-14-mut: oklch(0.77 0.02 200);
  --fb-14-r: clamp(112px,26vw,158px);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--fb-14-ink);
  position: relative;
  display: grid;
  grid-template-rows: auto 1fr;
  place-items: center;
  gap: clamp(14px,3vw,26px);
  padding: clamp(20px,5vw,52px) clamp(18px,4vw,40px) clamp(28px,6vw,60px);
  overflow: hidden;
}

.fb-14 *,
.fb-14 *::before,
.fb-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fb-14__page {
  width: min(100%,54ch);
  display: grid;
  gap: 13px;
  justify-items: center;
  text-align: center;
  align-self: end;
}

.fb-14__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--fb-14-accent);
}

.fb-14__title {
  font-size: clamp(25px,4.4vw,42px);
  line-height: 1.05;
  letter-spacing: -.03em;
  font-weight: 700;
  text-wrap: balance;
}

.fb-14__sub {
  font-size: clamp(13.5px,1.7vw,16px);
  line-height: 1.6;
  color: var(--fb-14-mut);
  text-wrap: pretty;
}

.fb-14__ctl {
  display: flex;
  align-items: center;
  gap: 13px;
  flex-wrap: wrap;
  justify-content: center;
  background: oklch(1 0 0/.07);
  border: 1px solid oklch(1 0 0/.14);
  border-radius: 99px;
  padding: 8px 18px;
}

.fb-14__lab {
  font-size: 12px;
  font-weight: 650;
  letter-spacing: .05em;
  text-transform: uppercase;
  color: var(--fb-14-mut);
}

.fb-14__range {
  -webkit-appearance: none;
  appearance: none;
  width: min(44vw,200px);
  height: 44px;
  background: transparent;
  cursor: pointer;
}

.fb-14__range::-webkit-slider-runnable-track {
  height: 5px;
  border-radius: 99px;
  background: linear-gradient(90deg,var(--fb-14-accent),oklch(0.62 0.16 250));
}

.fb-14__range::-moz-range-track {
  height: 5px;
  border-radius: 99px;
  background: linear-gradient(90deg,var(--fb-14-accent),oklch(0.62 0.16 250));
}

.fb-14__range::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 20px;
  height: 20px;
  margin-top: -7.5px;
  border-radius: 50%;
  background: oklch(0.99 0.01 200);
  border: 2px solid var(--fb-14-accent);
}

.fb-14__range::-moz-range-thumb {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: oklch(0.99 0.01 200);
  border: 2px solid var(--fb-14-accent);
}

.fb-14__range:focus-visible {
  outline: 2.5px solid var(--fb-14-accent);
  outline-offset: 4px;
  border-radius: 99px;
}

.fb-14__out {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 13px;
  font-weight: 600;
  min-width: 4.5ch;
  color: var(--fb-14-ink);
}

.fb-14__hub {
  position: relative;
  width: 66px;
  height: 66px;
  align-self: center;
  margin-top: clamp(40px,10vh,90px);
}

.fb-14__guide {
  position: absolute;
  left: 50%;
  top: 50%;
  width: calc(var(--fb-14-r) * 2.34);
  height: calc(var(--fb-14-r) * 2.34);
  translate: -50% -50%;
  color: var(--fb-14-accent);
  opacity: 0;
  pointer-events: none;
  transition: opacity .4s ease;
  rotate: -90deg;
}

.fb-14__hub[data-open="true"] .fb-14__guide {
  opacity: .28;
}

.fb-14__items {
  list-style: none;
  position: absolute;
  inset: 0;
}

.fb-14__items li {
  position: absolute;
  inset: 0;
  --fb-14-a: calc(20deg + var(--fb-14-i) * (var(--fb-14-spread) / (var(--fb-14-n) - 1)));
}

.fb-14__item {
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  width: 54px;
  height: 54px;
  margin: 6px;
  border: 1px solid oklch(1 0 0/.14);
  border-radius: 18px;
  cursor: pointer;
  color: oklch(0.2 0.04 200);
  background: linear-gradient(160deg,oklch(0.99 0.01 190),oklch(0.9 0.03 190));
  box-shadow: 0 10px 26px -10px oklch(0.08 0.02 210/.95);
  opacity: 0;
  scale: .4;
  translate: 0 0;
  rotate: 0deg;
  pointer-events: none;
  transition: translate .42s cubic-bezier(.2,1.1,.3,1),rotate .42s cubic-bezier(.2,1.1,.3,1),scale .34s cubic-bezier(.2,1.35,.4,1),opacity .26s ease,background .2s ease;
  transition-delay: calc((var(--fb-14-n) - var(--fb-14-i)) * 34ms);
}

.fb-14__item svg {
  width: 23px;
  height: 23px;
}

.fb-14__hub[data-open="true"] .fb-14__item {
  opacity: 1;
  scale: 1;
  pointer-events: auto;
  translate: calc(cos(var(--fb-14-a)) * var(--fb-14-r)) calc(sin(var(--fb-14-a)) * var(--fb-14-r) * -1);
  rotate: calc(90deg - var(--fb-14-a));
  transition-delay: calc(var(--fb-14-i) * 46ms);
}

.fb-14__item:hover {
  background: linear-gradient(160deg,var(--fb-14-accent),oklch(0.68 0.14 175));
}

.fb-14__item:focus-visible {
  outline: 3px solid var(--fb-14-accent);
  outline-offset: 3px;
}

.fb-14__item:active {
  scale: .92;
}

.fb-14__fab {
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  width: 66px;
  height: 66px;
  border: 0;
  border-radius: 50%;
  cursor: pointer;
  color: oklch(0.15 0.04 190);
  background: linear-gradient(150deg,oklch(0.92 0.14 145),var(--fb-14-accent));
  box-shadow: 0 16px 40px -12px oklch(0.82 0.16 175/.55),0 2px 6px oklch(0.08 0.02 210/.7);
  transition: transform .3s cubic-bezier(.2,1.3,.4,1);
}

.fb-14__fab svg {
  width: 28px;
  height: 28px;
  transition: rotate .4s cubic-bezier(.3,1.35,.4,1);
}

.fb-14__fab:hover {
  transform: scale(1.05);
}

.fb-14__fab:active {
  transform: scale(.93);
}

.fb-14__fab:focus-visible {
  outline: 3px solid oklch(0.99 0.01 200);
  outline-offset: 5px;
}

.fb-14__fab[aria-expanded="true"] svg {
  rotate: 225deg;
}

@media (prefers-reduced-motion: reduce) {
  .fb-14 * {
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  const hub = document.getElementById('fb-14-hub');
  const fab = document.getElementById('fb-14-fab');
  const range = document.getElementById('fb-14-spread');
  const out = document.getElementById('fb-14-out');
  if (!hub || !fab || fab.dataset.fbWired) return;
  fab.dataset.fbWired = '1';
  const items = [...hub.querySelectorAll('.fb-14__item')];
  const set = (open) => {
    hub.dataset.open = String(open);
    fab.setAttribute('aria-expanded', String(open));
    fab.setAttribute('aria-label', open ? 'Close attachment fan' : 'Open attachment fan');
    items.forEach((i) => { i.tabIndex = open ? 0 : -1; });
  };
  fab.addEventListener('click', () => set(hub.dataset.open !== 'true'));
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && hub.dataset.open === 'true') { set(false); fab.focus(); }
  });
  const sync = () => {
    hub.style.setProperty('--fb-14-spread', range.value + 'deg');
    out.textContent = range.value + '°';
    if (hub.dataset.open !== 'true') set(true);
  };
  range.addEventListener('input', sync);
  hub.style.setProperty('--fb-14-spread', range.value + 'deg');
})();
```
