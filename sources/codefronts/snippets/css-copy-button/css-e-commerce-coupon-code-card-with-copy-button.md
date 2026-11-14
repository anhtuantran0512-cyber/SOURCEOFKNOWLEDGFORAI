---
source: "codefronts"
url: "https://codefronts.com/snippets/css-copy-button/css-e-commerce-coupon-code-card-with-copy-button/"
title: "CSS E-commerce Coupon Code Card with Copy Button"
section: "snippets"
category: "css-copy-button"
category_name: "CSS Copy Buttons"
description: "A promo card built the way a store actually ships one: product shot, offer, a dashed voucher rail with SAVE20 set large in mono, and a copy button that…"
has_js: "true"
---

Here's a working CSS Copy Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS E-commerce Coupon Code Card with Copy Button
Source: https://codefronts.com/snippets/css-copy-button/css-e-commerce-coupon-code-card-with-copy-button/

A promo card built the way a store actually ships one: product shot, offer, a dashed voucher rail with SAVE20 set large in mono, and a copy button that confirms in place. The ticket notches are pure CSS radial gradients, and the terms line stays honest &mdash; the copy button is the payoff, not decoration.
## HTML
```html
<div class="cpy-12">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&display=swap">
  <input class="cpy-12__sr" type="checkbox" id="cpy-12-dark">
  <label class="cpy-12__theme" for="cpy-12-dark" title="Switch light or dark theme">
    <svg class="cpy-12__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.3" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.7v2.2M12 19.1v2.2M2.7 12h2.2M19.1 12h2.2M5.4 5.4l1.6 1.6M17 17l1.6 1.6M18.6 5.4 17 7M7 17l-1.6 1.6" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="cpy-12__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="cpy-12__vh">Switch light or dark theme</span>
  </label>

  <div class="cpy-12__stage">
    <article class="cpy-12__card">
      <div class="cpy-12__media">
        <img src="https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=800&q=70" alt="Brushed steel wristwatch on a pale background" width="800" height="800" loading="lazy" decoding="async">
        <span class="cpy-12__flag">Spring drop</span>
      </div>

      <div class="cpy-12__body">
        <p class="cpy-12__eyebrow">20% off accessories</p>
        <h2 class="cpy-12__title">Take a fifth off your first order</h2>

        <div class="cpy-12__ticket">
          <div class="cpy-12__codewrap">
            <span class="cpy-12__label">Coupon code</span>
            <code class="cpy-12__code" id="cpy-12-code">SAVE20</code>
          </div>
          <button class="cpy-12__btn" type="button" data-state="idle">
            <span class="cpy-12__icons">
              <svg class="cpy-12__i1" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><rect x="9" y="9" width="11" height="11" rx="2.4" stroke="currentColor" stroke-width="1.8"/><path d="M15.5 5.6A2.6 2.6 0 0 0 13 4H6.6A2.6 2.6 0 0 0 4 6.6V13a2.6 2.6 0 0 0 1.6 2.4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
              <svg class="cpy-12__i2" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4.8 12.6 9.5 17.3 19.2 7.2" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </span>
            <span class="cpy-12__labels"><span class="cpy-12__l1">Copy code</span><span class="cpy-12__l2">Copied</span></span>
          </button>
        </div>

        <p class="cpy-12__live" role="status" aria-live="polite"></p>
        <p class="cpy-12__terms">Ends 31 August 2027 &middot; minimum spend &pound;60 &middot; one use per customer</p>
      </div>
    </article>
  </div>
</div>
```
## CSS
```css
.cpy-12 {
  --bg: #f7f5f2;
  --panel: #ffffff;
  --panel2: #f2efe9;
  --ink: #141210;
  --muted: #615c54;
  --line: rgba(20,18,16,.13);
  --accent: #c2410c;
  --ok: #15803d;
  --dur: 200ms;
  --sans: system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "JetBrains Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.cpy-12 *,
.cpy-12 *::before,
.cpy-12 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(.5 .1 250)) {
  .cpy-12 {
    --accent: oklch(.55 .19 40);
    --ok: oklch(.55 .15 149);
  }
}

.cpy-12__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  clip-path: inset(50%);
  pointer-events: none;
}

.cpy-12__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cpy-12__theme {
  position: absolute;
  inset-block-start: clamp(1rem,3vw,1.75rem);
  inset-inline-end: clamp(1rem,3vw,1.75rem);
  z-index: 3;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  border-radius: 999px;
  border: 1px solid var(--line);
  background: rgba(255,255,255,.6);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  color: var(--ink);
  cursor: pointer;
}

.cpy-12__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.cpy-12__moon {
  display: none;
}

.cpy-12__sr:focus-visible + .cpy-12__theme {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.cpy-12__stage {
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,6vw,4.5rem);
}

.cpy-12__card {
  inline-size: min(100%,44rem);
  display: grid;
  grid-template-columns: minmax(0,15rem) 1fr;
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 1.6rem;
  overflow: hidden;
  box-shadow: 0 1px 2px rgba(20,18,16,.05),0 30px 60px -40px rgba(20,18,16,.4);
}

.cpy-12__media {
  position: relative;
  min-block-size: 14rem;
  background: var(--panel2);
}

.cpy-12__media img {
  inline-size: 100%;
  block-size: 100%;
  object-fit: cover;
  display: block;
}

.cpy-12__flag {
  position: absolute;
  inset-block-start: .85rem;
  inset-inline-start: .85rem;
  padding: .3rem .6rem;
  border-radius: 999px;
  background: rgba(255,255,255,.88);
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
  font-family: var(--mono);
  font-size: .66rem;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: #141210;
}

.cpy-12__body {
  padding: clamp(1.3rem,3.5vw,2rem);
  display: grid;
  gap: .7rem;
  align-content: center;
}

.cpy-12__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--accent);
}

.cpy-12__title {
  margin: 0 0 .3rem;
  font-size: clamp(1.35rem,3.2vw,1.8rem);
  line-height: 1.15;
  letter-spacing: -.02em;
  font-weight: 640;
  text-wrap: balance;
}

.cpy-12__ticket {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  padding: 1rem 1.2rem;
  border: 2px dashed color-mix(in srgb,var(--accent) 42%,transparent);
  border-radius: 1rem;
  background: color-mix(in srgb,var(--accent) 5%,transparent);
}

.cpy-12__codewrap {
  display: grid;
  gap: .15rem;
  padding-inline-start: .1rem;
}

.cpy-12__label {
  font-family: var(--mono);
  font-size: .66rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.cpy-12__code {
  font-family: var(--mono);
  font-size: clamp(1.5rem,5vw,2.05rem);
  font-weight: 600;
  letter-spacing: .08em;
  user-select: all;
}

.cpy-12__btn {
  flex: none;
  min-block-size: 2.85rem;
  min-inline-size: 44px;
  display: inline-flex;
  align-items: center;
  gap: .5rem;
  padding-inline: 1.1rem;
  border: 1px solid transparent;
  border-radius: .8rem;
  background: var(--ink);
  color: var(--panel);
  font: inherit;
  font-size: .9rem;
  font-weight: 580;
  cursor: pointer;
  transition: background var(--dur),color var(--dur),scale var(--dur);
}

.cpy-12__btn:hover {
  background: color-mix(in srgb,var(--ink) 88%,var(--accent));
}

.cpy-12__btn:active {
  scale: .975;
}

.cpy-12__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.cpy-12__btn[data-state="copied"] {
  background: var(--ok);
  color: #fff;
}

.cpy-12__icons {
  position: relative;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  flex: none;
}

.cpy-12__icons svg {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  transition: opacity var(--dur),scale var(--dur);
}

.cpy-12__i2 {
  opacity: 0;
  scale: .55;
}

.cpy-12__btn[data-state="copied"] .cpy-12__i1 {
  opacity: 0;
  scale: .55;
}

.cpy-12__btn[data-state="copied"] .cpy-12__i2 {
  opacity: 1;
  scale: 1;
}

.cpy-12__labels {
  display: grid;
}

.cpy-12__labels span {
  grid-area: 1/1;
  transition: opacity var(--dur),translate var(--dur);
}

.cpy-12__l2 {
  opacity: 0;
  translate: 0 .35rem;
}

.cpy-12__btn[data-state="copied"] .cpy-12__l1 {
  opacity: 0;
  translate: 0 -.35rem;
}

.cpy-12__btn[data-state="copied"] .cpy-12__l2 {
  opacity: 1;
  translate: 0 0;
}

.cpy-12__live {
  margin: 0;
  min-block-size: 1.25rem;
  font-size: .85rem;
  font-weight: 540;
  color: var(--ok);
}

.cpy-12__terms {
  margin: 0;
  font-size: .78rem;
  line-height: 1.5;
  color: var(--muted);
}

@media (max-width: 44rem) {
  .cpy-12__card {
    grid-template-columns: 1fr;
  }

  .cpy-12__media {
    min-block-size: 11rem;
  }
}

@media not (prefers-color-scheme: dark) {
  .cpy-12:has(#cpy-12-dark:checked) {
    --bg: #0a0908;
    --panel: #12100f;
    --panel2: #1c1917;
    --ink: #f3f0ea;
    --muted: rgba(243,240,234,.62);
    --line: rgba(243,240,234,.14);
    --accent: #fb923c;
    --ok: #6ee7a8;
  }

  .cpy-12:has(#cpy-12-dark:checked) .cpy-12__theme {
    background: rgba(255,255,255,.07);
  }

  .cpy-12:has(#cpy-12-dark:checked) .cpy-12__sun {
    display: none;
  }

  .cpy-12:has(#cpy-12-dark:checked) .cpy-12__moon {
    display: block;
  }

  .cpy-12:has(#cpy-12-dark:checked) .cpy-12__btn {
    background: var(--accent);
    color: #1a0f06;
  }

  .cpy-12:has(#cpy-12-dark:checked) .cpy-12__btn[data-state="copied"] {
    background: var(--ok);
    color: #04231a;
  }
}

@media (prefers-color-scheme: dark) {
  .cpy-12:not([data-theme="light"]):not(:has(#cpy-12-dark:checked)) {
    --bg: #0a0908;
    --panel: #12100f;
    --panel2: #1c1917;
    --ink: #f3f0ea;
    --muted: rgba(243,240,234,.62);
    --line: rgba(243,240,234,.14);
    --accent: #fb923c;
    --ok: #6ee7a8;
  }

  .cpy-12__theme {
    background: rgba(255,255,255,.07);
  }

  .cpy-12__sun {
    display: none;
  }

  .cpy-12__moon {
    display: block;
  }

  .cpy-12:has(#cpy-12-dark:checked) .cpy-12__sun {
    display: block;
  }

  .cpy-12:has(#cpy-12-dark:checked) .cpy-12__moon {
    display: none;
  }

  .cpy-12__btn {
    background: var(--accent);
    color: #1a0f06;
  }

  .cpy-12__btn[data-state="copied"] {
    background: var(--ok);
    color: #04231a;
  }
}

.cpy-12[data-theme="dark"] {
  --bg: #0a0908;
  --panel: #12100f;
  --panel2: #1c1917;
  --ink: #f3f0ea;
  --muted: rgba(243,240,234,.62);
  --line: rgba(243,240,234,.14);
  --accent: #fb923c;
  --ok: #6ee7a8;
}

@media (prefers-reduced-motion: reduce) {
  .cpy-12 *,
    .cpy-12 *::before,
    .cpy-12 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .cpy-12__card,
    .cpy-12__ticket,
    .cpy-12__btn,
    .cpy-12__theme {
    border-color: CanvasText;
    background: Canvas;
    color: CanvasText;
    box-shadow: none;
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
  }
}
```

## JavaScript
```js
const cpy12 = document.querySelector('.cpy-12');
if (cpy12) {
  const btn = cpy12.querySelector('.cpy-12__btn');
  const code = cpy12.querySelector('#cpy-12-code');
  const live = cpy12.querySelector('.cpy-12__live');
  let timer;
  btn.addEventListener('click', async () => {
    const value = code.textContent.trim();
    let ok = true;
    try { await navigator.clipboard.writeText(value); } catch { ok = false; }
    btn.dataset.state = ok ? 'copied' : 'idle';
    live.textContent = ok ? value + ' copied - apply it at checkout' : 'Copy blocked - select ' + value + ' and press Ctrl C';
    clearTimeout(timer);
    timer = setTimeout(() => { btn.dataset.state = 'idle'; live.textContent = ''; }, 2400);
  });
}
```
