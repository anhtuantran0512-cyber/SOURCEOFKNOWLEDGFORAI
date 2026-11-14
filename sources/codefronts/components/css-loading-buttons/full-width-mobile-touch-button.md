---
source: "codefronts"
url: "https://codefronts.com/components/css-loading-buttons/full-width-mobile-touch-button/"
title: "Full Width Mobile Touch Button"
section: "components"
category: "css-loading-buttons"
category_name: "CSS Loading Buttons"
description: "The bottom-anchored primary action: full-bleed, a generous touch target, and a thin indeterminate line along its top edge while the request runs."
has_js: "false"
---

Here's a working CSS Loading Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Full Width Mobile Touch Button
Source: https://codefronts.com/components/css-loading-buttons/full-width-mobile-touch-button/

The bottom-anchored primary action: full-bleed, a generous touch target, and a thin indeterminate line along its top edge while the request runs. It respects env(safe-area-inset-bottom) so it clears the home indicator on a notched phone, and it holds its ground at 320px without creating horizontal overflow.
## HTML
```html
<div class="lb-18">
  <div class="lb-18__stage">
    <div class="lb-18__phone">
      <div class="lb-18__screen">
        <header class="lb-18__top">
          <span class="lb-18__back" aria-hidden="true">
            <svg viewBox="0 0 20 20" width="16" height="16" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 4.5 6.5 10l5.5 5.5"/></svg>
          </span>
          <h2 class="lb-18__h">Review order</h2>
        </header>

        <div class="lb-18__body">
          <div class="lb-18__line"><span>Sourdough loaf ×2</span><span>£9.00</span></div>
          <div class="lb-18__line"><span>Cultured butter</span><span>£4.20</span></div>
          <div class="lb-18__line"><span>Delivery, Thursday</span><span>£2.50</span></div>
          <div class="lb-18__line lb-18__line--total"><span>Total</span><span>£15.70</span></div>
          <p class="lb-18__note">Delivering to Jordan Lee · 14 Ashfield Road</p>
        </div>

        <div class="lb-18__bar">
          <button class="lb-18__cta" type="button" data-state="idle" aria-busy="false">
            <span class="lb-18__line-ind" aria-hidden="true"></span>
            <span class="lb-18__faces">
              <span class="lb-18__face lb-18__face--idle">Place order · £15.70</span>
              <span class="lb-18__face lb-18__face--pending">Processing payment</span>
            </span>
          </button>
          <div class="lb-18__control">
            <input class="lb-18__switch" type="checkbox" id="lb-18-switch">
            <label class="lb-18__lab" for="lb-18-switch">Hold the request open</label>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.lb-18 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --bg: #e9efe8;
  --surface: #ffffff;
  --ink: #1c2a20;
  --muted: #63796a;
  --rule: #d7e2d6;
  --accent: #2f6b4a;
  --press: #24523a;
  font-family: ui-sans-serif, system-ui, "Segoe UI", sans-serif;
  background: var(--bg);
  color: var(--ink);
  padding: 32px 12px;
}

.lb-18 *,
.lb-18 *::before,
.lb-18 *::after {
  box-sizing: border-box;
}

.lb-18__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  min-height: calc(100vh - 64px);
}

.lb-18__phone {
  inline-size: 100%;
  max-inline-size: 22rem;
  min-inline-size: 0;
  background: var(--surface);
  border: 1px solid var(--rule);
  border-radius: 26px;
  padding: 8px;
  box-shadow: 0 26px 50px -34px rgba(28, 42, 32, .6);
}

.lb-18__screen {
  display: flex;
  flex-direction: column;
  min-block-size: 27rem;
  background: var(--surface);
  border-radius: 20px;
  overflow: hidden;
  min-inline-size: 0;
}

.lb-18__top {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 14px 16px;
  border-block-end: 1px solid var(--rule);
  min-inline-size: 0;
}

.lb-18__back {
  display: inline-flex;
  color: var(--muted);
  flex: none;
}

.lb-18__h {
  margin: 0;
  font-size: 14.5px;
  font-weight: 620;
  min-inline-size: 0;
}

.lb-18__body {
  flex: 1 1 auto;
  padding: 16px;
  display: grid;
  gap: 10px;
  align-content: start;
  min-inline-size: 0;
}

.lb-18__line {
  display: flex;
  gap: 12px;
  justify-content: space-between;
  font-size: 13px;
  color: var(--muted);
  min-inline-size: 0;
}

.lb-18__line span:first-child {
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.lb-18__line span:last-child {
  flex: none;
  font-variant-numeric: tabular-nums;
}

.lb-18__line--total {
  color: var(--ink);
  font-weight: 660;
  font-size: 15px;
  padding-block-start: 10px;
  border-block-start: 1px solid var(--rule);
}

.lb-18__note {
  margin: 6px 0 0;
  font-size: 11.5px;
  color: var(--muted);
  min-inline-size: 0;
}

.lb-18__bar {
  position: sticky;
  inset-block-end: 0;
  background: var(--surface);
  border-block-start: 1px solid var(--rule);
  padding: 12px 14px calc(12px + env(safe-area-inset-bottom, 0px));
  min-inline-size: 0;
}

.lb-18__cta {
  appearance: none;
  position: relative;
  overflow: hidden;
  inline-size: 100%;
  border: 0;
  background: var(--accent);
  color: #f4fbf6;
  border-radius: 14px;
  font: inherit;
  font-size: 14.5px;
  font-weight: 640;
  padding: 0 16px;
  min-block-size: 52px;
  min-inline-size: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: background 150ms ease;
}

.lb-18__cta:active {
  background: var(--press);
}

.lb-18__cta:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

.lb-18__faces {
  display: grid;
  place-items: center;
  min-inline-size: 0;
}

.lb-18__face {
  grid-area: 1 / 1;
  white-space: nowrap;
  visibility: hidden;
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
}

.lb-18__face--idle {
  visibility: visible;
}

.lb-18__line-ind {
  position: absolute;
  inset-block-start: 0;
  inset-inline: 0;
  block-size: 2px;
  opacity: 0;
  overflow: hidden;
}

.lb-18__line-ind::before {
  content: "";
  position: absolute;
  inset-block: 0;
  inline-size: 40%;
  background: #f4fbf6;
  animation: lb-18-run 1.1s ease-in-out infinite;
}

@keyframes lb-18-run {
  from {
    transform: translateX(-105%);
  }

  to {
    transform: translateX(290%);
  }
}

.lb-18:has(.lb-18__switch:checked) .lb-18__face--idle {
  visibility: hidden;
}

.lb-18:has(.lb-18__switch:checked) .lb-18__face--pending {
  visibility: visible;
}

.lb-18:has(.lb-18__switch:checked) .lb-18__line-ind {
  opacity: 1;
}

.lb-18:has(.lb-18__switch:checked) .lb-18__cta {
  cursor: progress;
}

.lb-18__control {
  display: flex;
  justify-content: center;
  margin-block-start: 4px;
}

.lb-18__lab {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 11.5px;
  color: var(--muted);
  min-height: 44px;
  cursor: pointer;
}

.lb-18__switch {
  accent-color: var(--accent);
  inline-size: 16px;
  block-size: 16px;
  margin: 0;
}

.lb-18__switch:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .lb-18__line-ind::before {
    animation: none;
    inline-size: 100%;
    opacity: .6;
  }

  .lb-18__cta {
    transition: none;
  }
}

@media (prefers-color-scheme: dark) {
  .lb-18 {
    --bg: #0f150f;
    --surface: #171f18;
    --ink: #e6efe6;
    --muted: #93a795;
    --rule: #253026;
    --accent: #47a377;
    --press: #38835e;
  }

  .lb-18__cta {
    color: #0f150f;
  }

  .lb-18__line-ind::before {
    background: #0f150f;
  }
}

[data-theme="dark"] .lb-18 {
  --bg: #0f150f;
  --surface: #171f18;
  --ink: #e6efe6;
  --muted: #93a795;
  --rule: #253026;
  --accent: #47a377;
  --press: #38835e;
}
```
