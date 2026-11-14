---
source: "codefronts"
url: "https://codefronts.com/snippets/css-social-buttons/share-button-with-live-count-badge/"
title: "Share Button with Live Count Badge"
section: "snippets"
category: "css-social-buttons"
category_name: "CSS Social Buttons"
description: "A share control with the running total beside it."
has_js: "true"
---

Here's a working CSS Social Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Share Button with Live Count Badge
Source: https://codefronts.com/snippets/css-social-buttons/share-button-with-live-count-badge/

A share control with the running total beside it. The figure uses tabular-nums so digits occupy identical widths and the badge never jitters as the number changes, a short scale pulse marks each increment, and counts above a thousand collapse to 1.2K. State lives in aria-pressed and every change is announced through a polite live region.
## HTML
```html
<div class="soc-08">
  <div class="soc-08__stage">
    <div class="soc-08__card">
      <p class="soc-08__eyebrow">Engagement</p>
      <h2 class="soc-08__title">The state of CSS layout, 2027 edition</h2>
      <div class="soc-08__row">
        <button class="soc-08__btn" type="button" aria-pressed="false">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="17.5" cy="5.5" r="2.6"/><circle cx="6.5" cy="12" r="2.6"/><circle cx="17.5" cy="18.5" r="2.6"/><path d="m8.9 10.7 6.2-3.6"/><path d="m8.9 13.3 6.2 3.6"/></svg>
          <span class="soc-08__label">Share</span>
        </button>
        <p class="soc-08__badge">
          <span class="soc-08__count">1.2K</span>
          <span class="soc-08__unit">shares</span>
        </p>
      </div>
      <p class="soc-08__live" role="status" aria-live="polite">1.2K shares</p>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&display=swap');

.soc-08 {
  --bg: #f4f4f6;
  --surface: #ffffff;
  --fg: #0e0e12;
  --muted: #6a6a76;
  --line: #e5e5ea;
  --ring: #3d63ff;
  --brand: #3d63ff;
  --on-brand: #ffffff;
  --pulse-scale: 1.18;
  --sans: "Geist",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  color: var(--fg);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(50% 0 0)) {
  .soc-08 {
    --bg: oklch(96.4% .003 285);
    --surface: oklch(100% 0 0);
    --fg: oklch(17% .012 285);
    --muted: oklch(55% .012 285);
    --line: oklch(91.5% .005 285);
    --brand: oklch(56% .19 265);
  }
}

@media (prefers-color-scheme: dark) {
  .soc-08:not([data-theme="light"]) {
    --bg: #0a0a0d;
    --surface: #131318;
    --fg: #f2f2f5;
    --muted: #9a9aa6;
    --line: #26262e;
    --brand: #7c9bff;
    --on-brand: #0b0b12;
  }
}

.soc-08[data-theme="dark"] {
  --bg: #0a0a0d;
  --surface: #131318;
  --fg: #f2f2f5;
  --muted: #9a9aa6;
  --line: #26262e;
  --brand: #7c9bff;
  --on-brand: #0b0b12;
}

.soc-08,
.soc-08 *,
.soc-08 *::before,
.soc-08 *::after {
  box-sizing: border-box;
}

.soc-08__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,3.5rem);
}

.soc-08__card {
  inline-size: min(32rem,100%);
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 1.25rem;
  padding: clamp(1.5rem,4vw,2.25rem);
  box-shadow: 0 1px 2px rgb(0 0 0/.04), 0 18px 40px -28px rgb(9 9 20/.4);
}

.soc-08__eyebrow {
  margin: 0 0 .55rem;
  font-size: .72rem;
  font-weight: 600;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
}

.soc-08__title {
  margin: 0 0 1.5rem;
  font-size: clamp(1.1rem,1rem + .9vw,1.4rem);
  font-weight: 600;
  line-height: 1.3;
  letter-spacing: -.02em;
  text-wrap: balance;
}

.soc-08__row {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: .7rem;
}

.soc-08__btn {
  display: inline-flex;
  align-items: center;
  gap: .55rem;
  min-block-size: 2.875rem;
  padding: 0 1.15rem;
  border: 1px solid var(--line);
  border-radius: .85rem;
  background: var(--surface);
  color: var(--fg);
  font: inherit;
  font-size: .92rem;
  font-weight: 550;
  cursor: pointer;
  transition: background-color .2s ease, color .2s ease, border-color .2s ease, translate .2s cubic-bezier(.16,1,.3,1);
}

.soc-08__btn svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.soc-08__btn:hover {
  translate: 0 -2px;
  border-color: color-mix(in oklab,var(--brand) 45%,var(--line));
}

.soc-08__btn:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}

.soc-08__btn[aria-pressed="true"] {
  background: var(--brand);
  border-color: var(--brand);
  color: var(--on-brand);
}

.soc-08__badge {
  display: inline-flex;
  align-items: baseline;
  gap: .4rem;
  margin: 0;
  min-block-size: 2.875rem;
  padding: 0 .9rem;
  border: 1px solid var(--line);
  border-radius: .85rem;
  background: color-mix(in oklab,var(--fg) 4%,var(--surface));
  align-self: stretch;
}

.soc-08__count {
  display: inline-block;
  min-inline-size: 3.2ch;
  text-align: end;
  align-self: center;
  font-size: 1.05rem;
  font-weight: 700;
  letter-spacing: -.02em;
  font-variant-numeric: tabular-nums;
  transform-origin: center;
}

.soc-08__count[data-pulse] {
  animation: soc-08-pulse .42s cubic-bezier(.16,1,.3,1);
}

@keyframes soc-08-pulse {
  0% {
    scale: 1;
  }

  38% {
    scale: var(--pulse-scale);
    color: var(--brand);
  }

  100% {
    scale: 1;
  }
}

.soc-08__unit {
  align-self: center;
  font-size: .8rem;
  color: var(--muted);
}

.soc-08__live {
  margin: 1.2rem 0 0;
  font-size: .8rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

@media (prefers-reduced-motion: reduce) {
  .soc-08__count[data-pulse] {
    animation: none;
  }

  .soc-08__btn {
    transition-duration: 1ms;
  }

  .soc-08__btn:hover {
    translate: none;
  }
}

@media (forced-colors: active) {
  .soc-08__btn {
    border: 1px solid ButtonText;
    color: ButtonText;
  }

  .soc-08__btn[aria-pressed="true"] {
    background: Highlight;
    color: HighlightText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.soc-08');
  if (!root) return;
  const btn = root.querySelector('.soc-08__btn');
  const out = root.querySelector('.soc-08__count');
  const live = root.querySelector('.soc-08__live');
  let n = 1247, on = false;
  const fmt = (v) => {
    if (v < 1000) return String(v);
    const s = (v / 1000).toFixed(1);
    return (s.endsWith('.0') ? s.slice(0, -2) : s) + 'K';
  };
  out.addEventListener('animationend', () => { out.removeAttribute('data-pulse'); });
  btn.addEventListener('click', () => {
    on = !on;
    n += on ? 1 : -1;
    btn.setAttribute('aria-pressed', String(on));
    btn.querySelector('.soc-08__label').textContent = on ? 'Shared' : 'Share';
    out.textContent = fmt(n);
    out.setAttribute('data-pulse', '');
    live.textContent = (on ? 'Shared. ' : 'Share removed. ') + fmt(n) + ' shares';
  });
})();
```
