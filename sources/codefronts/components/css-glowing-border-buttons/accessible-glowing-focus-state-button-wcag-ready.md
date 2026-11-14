---
source: "codefronts"
url: "https://codefronts.com/components/css-glowing-border-buttons/accessible-glowing-focus-state-button-wcag-ready/"
title: "Accessible Glowing Focus State Button (WCAG-Ready)"
section: "components"
category: "css-glowing-border-buttons"
category_name: "CSS Glowing Border Buttons"
description: "The enterprise closer: a glowing focus treatment engineered to WCAG 2.2 — a 3px offset outline PLUS a soft glow that appears only for keyboard navigation via…"
has_js: "false"
---

Here's a working CSS Glowing Border Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Accessible Glowing Focus State Button (WCAG-Ready)
Source: https://codefronts.com/components/css-glowing-border-buttons/accessible-glowing-focus-state-button-wcag-ready/

The enterprise closer: a glowing focus treatment engineered to WCAG 2.2 — a 3px offset outline PLUS a soft glow that appears only for keyboard navigation via :focus-visible, stays ≥3:1 against every adjacent color, and swaps itself for system colors under forced-colors mode. Tab into the demo to see it fire.
## HTML
```html
<section class="gbb-15" aria-label="Accessible glowing focus state demo">
  <div class="gbb-15__row">
    <button class="gbb-15__btn gbb-15__btn--solid" type="button">Submit request</button>
    <button class="gbb-15__btn" type="button">Save draft</button>
  </div>
  <p class="gbb-15__hint">Press <kbd>Tab</kbd> — the glow ring fires for keyboard focus only, not clicks</p>
</section>
```
## CSS
```css
.gbb-15,
.gbb-15 *,
.gbb-15 *::before,
.gbb-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gbb-15 {
  --ring: oklch(0.86 0.16 200);
  --solid: oklch(0.62 0.16 258);
  --ease: cubic-bezier(0.16,1,0.3,1);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-content: center;
  justify-items: center;
  gap: 20px;
  padding: 48px 24px;
  background: radial-gradient(55% 60% at 22% 18%,oklch(0.24 0.06 200 / .3),transparent 60%),radial-gradient(50% 55% at 82% 88%,oklch(0.22 0.06 258 / .3),transparent 60%),linear-gradient(170deg,oklch(0.14 0.014 250),oklch(0.11 0.012 260));
}

.gbb-15 .gbb-15__row {
  display: flex;
  flex-wrap: wrap;
  gap: 14px;
  justify-content: center;
}

.gbb-15 .gbb-15__btn {
  cursor: pointer;
  border-radius: 12px;
  padding: 15px 30px;
  font: 600 14.5px/1 'Segoe UI',system-ui,sans-serif;
  letter-spacing: .005em;
  color: #fff;
  background: linear-gradient(180deg,rgba(255,255,255,.06),rgba(255,255,255,.02));
  border: 1px solid rgba(255,255,255,.10);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.08),inset 0 -1px 0 rgba(0,0,0,.15),0 1px 0 rgba(0,0,0,.3);
  transition: background .35s var(--ease),border-color .35s var(--ease),box-shadow .35s var(--ease),transform .25s var(--ease);
}

.gbb-15 .gbb-15__btn--solid {
  background: linear-gradient(180deg,color-mix(in oklab,var(--solid) 92%,#000),color-mix(in oklab,var(--solid) 68%,#000));
  border-color: color-mix(in oklab,var(--solid) 45%,transparent);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.22),inset 0 -1px 0 rgba(0,0,0,.28),0 1px 0 rgba(0,0,0,.4),0 0 0 1px color-mix(in oklab,var(--solid) 35%,transparent),0 10px 24px -10px color-mix(in oklab,var(--solid) 60%,transparent),0 0 34px -8px color-mix(in oklab,var(--solid) 40%,transparent);
}

.gbb-15 .gbb-15__btn:hover {
  background: linear-gradient(180deg,rgba(255,255,255,.09),rgba(255,255,255,.03));
  border-color: rgba(255,255,255,.22);
  transform: translateY(-1px);
}

.gbb-15 .gbb-15__btn--solid:hover {
  background: linear-gradient(180deg,color-mix(in oklab,var(--solid) 100%,#000),color-mix(in oklab,var(--solid) 78%,#000));
  border-color: color-mix(in oklab,var(--solid) 55%,transparent);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.28),inset 0 -1px 0 rgba(0,0,0,.3),0 1px 0 rgba(0,0,0,.5),0 0 0 1px color-mix(in oklab,var(--solid) 55%,transparent),0 14px 32px -10px color-mix(in oklab,var(--solid) 70%,transparent),0 0 52px -8px color-mix(in oklab,var(--solid) 55%,transparent);
  transform: translateY(-1px);
}

.gbb-15 .gbb-15__btn:active {
  transform: translateY(0);
  transition-duration: .1s;
}

.gbb-15 .gbb-15__btn:focus-visible {
  outline: 3px solid var(--ring);
  outline-offset: 3px;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.12),0 0 0 1px color-mix(in oklab,var(--ring) 65%,transparent),0 0 0 6px color-mix(in oklab,var(--ring) 22%,transparent),0 8px 32px -4px color-mix(in oklab,var(--ring) 45%,transparent),0 0 44px color-mix(in oklab,var(--ring) 28%,transparent);
  animation: gbb15-in .25s var(--ease) 1;
}

.gbb-15 .gbb-15__btn--solid:focus-visible {
  box-shadow: inset 0 1px 0 rgba(255,255,255,.24),0 0 0 1px color-mix(in oklab,var(--ring) 65%,transparent),0 0 0 6px color-mix(in oklab,var(--ring) 22%,transparent),0 12px 34px -6px color-mix(in oklab,var(--ring) 45%,transparent),0 0 56px color-mix(in oklab,var(--ring) 30%,transparent);
}

.gbb-15 .gbb-15__hint {
  font: 400 12px/1.5 'Segoe UI',system-ui,sans-serif;
  color: rgba(255,255,255,.42);
  letter-spacing: .005em;
}

.gbb-15 kbd {
  font: 600 10.5px ui-monospace,Menlo,monospace;
  background: linear-gradient(180deg,rgba(255,255,255,.12),rgba(255,255,255,.04));
  border: 1px solid rgba(255,255,255,.16);
  border-radius: 5px;
  padding: 2px 7px;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.12),0 1px 0 rgba(0,0,0,.3);
  color: rgba(255,255,255,.85);
}

@keyframes gbb15-in {
  from {
    box-shadow: 0 0 0 0 color-mix(in oklab,var(--ring) 25%,transparent),0 0 0 color-mix(in oklab,var(--ring) 35%,transparent);
  }
}

@media (forced-colors: active) {
  .gbb-15 .gbb-15__btn:focus-visible {
    outline: 3px solid Highlight;
    box-shadow: none;
    animation: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .gbb-15 .gbb-15__btn,
    .gbb-15 .gbb-15__btn--solid {
    transition: none;
  }

  .gbb-15 .gbb-15__btn:focus-visible {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — :focus-visible fires the glow for keyboard focus only; forced-colors swaps it for the OS Highlight outline (box-shadow doesn't render there). */
```
