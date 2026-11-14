---
source: "codefronts"
url: "https://codefronts.com/motion/css-ripple-designs/css-ripple-button-click-animation/"
title: "Material Ink Button Ripple"
section: "motion"
category: "css-ripple-designs"
category_name: "CSS Ripple Effects"
description: "Ink spreads from the exact point of the press and is clipped to the button's own shape, which is where most implementations fall over."
has_js: "true"
---

Here's a working CSS Ripple Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Material Ink Button Ripple
Source: https://codefronts.com/motion/css-ripple-designs/css-ripple-button-click-animation/

Ink spreads from the exact point of the press and is clipped to the button's own shape, which is where most implementations fall over. Four button types share one script: filled, outlined, text and icon. The clipping rules, the interaction between border-radius and the overflow clip, and the centred-origin exception for icon buttons are all shown.
## HTML
```html
<section class="rpl-10" aria-label="Material Ink Button Ripple">
  <input class="rpl-10__theme-input" type="checkbox" id="rpl-10-theme">
  <label class="rpl-10__theme" for="rpl-10-theme">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="rpl-10__theme-sr">Switch between dark and light theme</span>
  </label>
  <div class="rpl-10__win">
    <div class="rpl-10__side">
      <p class="rpl-10__side-t">Inbox</p>
      <span class="rpl-10__side-i rpl-10__side-i--on">All mail</span>
      <span class="rpl-10__side-i">Drafts</span>
      <span class="rpl-10__side-i">Sent</span>
    </div>
    <div class="rpl-10__main">
      <div class="rpl-10__thread">
        <p class="rpl-10__subject">Re: Q3 partner review</p>
        <p class="rpl-10__from">Nadia Okonkwo &middot; 14:02</p>
        <p class="rpl-10__body">Deck looks solid. Can you add the retention slide before Thursday? I'll handle the pricing section.</p>
      </div>
      <div class="rpl-10__compose">
        <div class="rpl-10__field" aria-hidden="true">Sure — adding it tonight.</div>
        <div class="rpl-10__bar" id="rpl-10-bar">
          <button class="rpl-10__btn rpl-10__btn--icon" type="button" aria-label="Attach file">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><path d="M20 11.5 12 19.5a5 5 0 0 1-7-7l8-8a3.5 3.5 0 0 1 5 5l-8 8a2 2 0 0 1-3-3l7.5-7.5"/></svg>
          </button>
          <button class="rpl-10__btn rpl-10__btn--icon" type="button" aria-label="Insert emoji">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M9 10h.01M15 10h.01M8.5 14.5a4.5 4.5 0 0 0 7 0"/></svg>
          </button>
          <span class="rpl-10__gap"></span>
          <button class="rpl-10__btn rpl-10__btn--text" type="button">Save draft</button>
          <button class="rpl-10__btn rpl-10__btn--filled" type="button">
            Send
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M4 12h14m-5-5 5 5-5 5"/></svg>
          </button>
        </div>
      </div>
    </div>
      </div>
</section>
```
## CSS
```css
.rpl-10 {
  --rpl-10-bg: #eef0f4;
  --rpl-10-bg: oklch(0.945 0.005 265);
  --rpl-10-card: #ffffff;
  --rpl-10-card: oklch(1 0 0);
  --rpl-10-side: #f5f6fa;
  --rpl-10-side: oklch(0.972 0.004 265);
  --rpl-10-line: #e2e5ec;
  --rpl-10-line: oklch(0.915 0.006 265);
  --rpl-10-fg: #14161c;
  --rpl-10-fg: oklch(0.205 0.008 265);
  --rpl-10-muted: #585e6b;
  --rpl-10-muted: oklch(0.495 0.014 265);
  --rpl-10-accent: #1b56e0;
  --rpl-10-accent: oklch(0.50 0.21 265);
  --rpl-10-dur: 600ms;
  position: relative;
  display: grid;
  place-items: center;
  min-block-size: 100vh;
  min-block-size: 100svh;
  padding: clamp(14px, 3vw, 44px);
  background: var(--rpl-10-bg);
  color: var(--rpl-10-fg);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif;
  box-sizing: border-box;
}

.rpl-10 *,
.rpl-10 *::before,
.rpl-10 *::after {
  box-sizing: border-box;
}

@media (prefers-color-scheme: dark) {
  .rpl-10:not(:has(#rpl-10-theme:checked)) {
    --rpl-10-bg: #0a0b0f;
    --rpl-10-bg: oklch(0.155 0.006 265);
    --rpl-10-card: #14161c;
    --rpl-10-card: oklch(0.215 0.008 265);
    --rpl-10-side: #101218;
    --rpl-10-side: oklch(0.185 0.008 265);
    --rpl-10-line: #232730;
    --rpl-10-line: oklch(0.285 0.010 265);
    --rpl-10-fg: #eef0f5;
    --rpl-10-fg: oklch(0.955 0.004 265);
    --rpl-10-muted: #929aa8;
    --rpl-10-muted: oklch(0.69 0.014 265);
    --rpl-10-accent: #7f9dff;
    --rpl-10-accent: oklch(0.75 0.145 268);
  }
}

@media (prefers-color-scheme: light) {
  .rpl-10:has(#rpl-10-theme:checked) {
    --rpl-10-bg: #0a0b0f;
    --rpl-10-bg: oklch(0.155 0.006 265);
    --rpl-10-card: #14161c;
    --rpl-10-card: oklch(0.215 0.008 265);
    --rpl-10-side: #101218;
    --rpl-10-side: oklch(0.185 0.008 265);
    --rpl-10-line: #232730;
    --rpl-10-line: oklch(0.285 0.010 265);
    --rpl-10-fg: #eef0f5;
    --rpl-10-fg: oklch(0.955 0.004 265);
    --rpl-10-muted: #929aa8;
    --rpl-10-muted: oklch(0.69 0.014 265);
    --rpl-10-accent: #7f9dff;
    --rpl-10-accent: oklch(0.75 0.145 268);
  }
}

.rpl-10__win {
  position: relative;
  inline-size: 100%;
  max-inline-size: 900px;
  display: grid;
  grid-template-columns: 190px minmax(0, 1fr);
  border: 1px solid var(--rpl-10-line);
  border-radius: 22px;
  background: var(--rpl-10-card);
  overflow: hidden;
  box-shadow: 0 30px 70px -45px oklch(0 0 0 / 0.5);
}

@media (max-width: 700px) {
  .rpl-10__win {
    grid-template-columns: minmax(0, 1fr);
  }

  .rpl-10__side {
    display: none;
  }
}

.rpl-10__side {
  display: flex;
  flex-direction: column;
  gap: 3px;
  padding: 20px 14px;
  background: var(--rpl-10-side);
  border-inline-end: 1px solid var(--rpl-10-line);
}

.rpl-10__side-t {
  margin: 0 8px 10px;
  font-size: 11px;
  letter-spacing: 0.13em;
  text-transform: uppercase;
  color: var(--rpl-10-muted);
}

.rpl-10__side-i {
  padding: 9px 10px;
  border-radius: 10px;
  font-size: 13.5px;
  color: var(--rpl-10-muted);
}

.rpl-10__side-i--on {
  background: color-mix(in oklab, var(--rpl-10-accent) 12%, transparent);
  color: var(--rpl-10-accent);
  font-weight: 600;
}

.rpl-10__main {
  display: flex;
  flex-direction: column;
  min-inline-size: 0;
}

.rpl-10__thread {
  padding: clamp(20px, 3vw, 30px);
  border-block-end: 1px solid var(--rpl-10-line);
}

.rpl-10__subject {
  margin: 0 0 6px;
  font-size: clamp(19px, 2.6vw, 23px);
  font-weight: 620;
  letter-spacing: -0.02em;
}

.rpl-10__from {
  margin: 0 0 16px;
  font-size: 12.5px;
  color: var(--rpl-10-muted);
}

.rpl-10__body {
  margin: 0;
  font-size: 14.5px;
  line-height: 1.6;
  color: var(--rpl-10-fg);
  max-inline-size: 56ch;
  text-wrap: pretty;
}

.rpl-10__compose {
  padding: clamp(16px, 2.4vw, 22px);
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.rpl-10__field {
  min-block-size: 88px;
  padding: 14px 16px;
  border: 1px solid var(--rpl-10-line);
  border-radius: 14px;
  font-size: 14.5px;
  color: var(--rpl-10-fg);
  background: color-mix(in oklab, var(--rpl-10-side) 60%, transparent);
}

.rpl-10__bar {
  display: flex;
  align-items: center;
  gap: 8px;
}

.rpl-10__gap {
  flex: 1;
}

.rpl-10__btn {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  min-block-size: 44px;
  padding: 0 16px;
  border: 1px solid transparent;
  border-radius: 12px;
  background: transparent;
  color: var(--rpl-10-fg);
  font: inherit;
  font-size: 14px;
  font-weight: 560;
  cursor: pointer;
  overflow: hidden;
  isolation: isolate;
  -webkit-tap-highlight-color: transparent;
}

.rpl-10__btn:focus-visible {
  outline: 2px solid var(--rpl-10-accent);
  outline-offset: 2px;
}

.rpl-10__btn--icon {
  inline-size: 44px;
  padding: 0;
  border-radius: 50%;
  color: var(--rpl-10-muted);
}

.rpl-10__btn--icon svg {
  inline-size: 20px;
  block-size: 20px;
}

.rpl-10__btn--text {
  color: var(--rpl-10-muted);
}

.rpl-10__btn--filled {
  background: var(--rpl-10-accent);
  color: oklch(1 0 0);
  padding-inline: 20px;
}

@media (prefers-color-scheme: dark) {
  .rpl-10:not(:has(#rpl-10-theme:checked)) .rpl-10__btn--filled {
    color: oklch(0.19 0.03 265);
  }
}

@media (prefers-color-scheme: light) {
  .rpl-10:has(#rpl-10-theme:checked) .rpl-10__btn--filled {
    color: oklch(0.19 0.03 265);
  }
}

.rpl-10__btn--filled svg {
  inline-size: 17px;
  block-size: 17px;
}
/* overflow: hidden on the button clips the ink to the border-radius — no square corners on a pill. */

.rpl-10__ink {
  position: absolute;
  left: var(--rpl-10-x, 50%);
  top: var(--rpl-10-y, 50%);
  inline-size: calc(var(--rpl-10-r, 60px) * 2);
  block-size: calc(var(--rpl-10-r, 60px) * 2);
  border-radius: 50%;
  background: currentColor;
  opacity: 0.22;
  pointer-events: none;
  z-index: -1;
  animation: rpl-10-ink var(--rpl-10-dur) cubic-bezier(0.16, 0.72, 0.3, 1) forwards;
}

.rpl-10__btn--filled .rpl-10__ink {
  background: oklch(1 0 0);
  opacity: 0.3;
}

@media (prefers-color-scheme: dark) {
  .rpl-10:not(:has(#rpl-10-theme:checked)) .rpl-10__btn--filled .rpl-10__ink {
    background: oklch(0.15 0.02 265);
  }
}

@media (prefers-color-scheme: light) {
  .rpl-10:has(#rpl-10-theme:checked) .rpl-10__btn--filled .rpl-10__ink {
    background: oklch(0.15 0.02 265);
  }
}

@keyframes rpl-10-ink {
  from {
    transform: translate(-50%, -50%) scale(0);
    opacity: 0.3;
  }

  to {
    transform: translate(-50%, -50%) scale(1);
    opacity: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .rpl-10__ink {
    display: none;
  }

  .rpl-10__btn:active {
    filter: brightness(0.92);
  }
}

.rpl-10 {
  position: relative;
}

.rpl-10__theme-input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.rpl-10__theme {
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

.rpl-10__theme:hover {
  background: color-mix(in oklab, currentColor 15%, transparent);
  border-color: color-mix(in oklab, currentColor 38%, transparent);
}

.rpl-10__theme:active {
  transform: scale(0.94);
}

.rpl-10__theme svg {
  inline-size: 19px;
  block-size: 19px;
  display: block;
  transition: transform 320ms cubic-bezier(0.2, 0.7, 0.3, 1);
}

.rpl-10__theme-input:checked + .rpl-10__theme svg {
  transform: rotate(180deg);
}

.rpl-10__theme-input:focus-visible + .rpl-10__theme {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.rpl-10__theme-sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

@media (prefers-reduced-motion: reduce) {
  .rpl-10__theme,
    .rpl-10__theme svg {
    transition: none;
  }
}
```

## JavaScript
```js
const root = document.querySelector('.rpl-10');
const targets = root.querySelectorAll('.rpl-10__btn');
const timers = new Set();

const drop = (event) => {
  const btn = event.currentTarget;
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const box = btn.getBoundingClientRect();
  const x = event.clientX - box.left;
  const y = event.clientY - box.top;
  const r = Math.max(Math.hypot(x, y), Math.hypot(box.width - x, y), Math.hypot(x, box.height - y), Math.hypot(box.width - x, box.height - y));
  const ink = document.createElement('span');
  ink.className = 'rpl-10__ink';
  ink.setAttribute('aria-hidden', 'true');
  ink.style.setProperty('--rpl-10-x', x + 'px');
  ink.style.setProperty('--rpl-10-y', y + 'px');
  ink.style.setProperty('--rpl-10-r', r + 'px');
  ink.addEventListener('animationend', () => ink.remove(), { once: true });
  const t = setTimeout(() => { timers.delete(t); ink.remove(); }, 1400);
  timers.add(t);
  btn.append(ink);
};

targets.forEach((btn) => btn.addEventListener('pointerdown', drop));
root.__rplCleanup = () => { targets.forEach((btn) => btn.removeEventListener('pointerdown', drop)); timers.forEach(clearTimeout); timers.clear(); };
```
