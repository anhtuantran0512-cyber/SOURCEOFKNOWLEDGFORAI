---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-neumorphism/sunken-form-studio/"
title: "Inset Input Fields and Search Bar"
section: "design-styles"
category: "css-neumorphism"
category_name: "CSS Neumorphism"
description: "Text fields, search, select and textarea as carved wells."
has_js: "false"
---

Here's a working CSS Neumorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Inset Input Fields and Search Bar
Source: https://codefronts.com/design-styles/css-neumorphism/sunken-form-studio/

Text fields, search, select and textarea as carved wells. An inset shadow makes a field look like something you can type into — the strongest affordance soft UI has — but it also hides the focus state, so the focus ring here is a real outline with a colour shift on the icon. Includes the error and valid states that soft UI usually forgets, and the placeholder-contrast trap.
## HTML
```html
<section class="nm-11" aria-labelledby="nm-11-heading">
      <input type="checkbox" id="nm-11-theme" class="nm-11__themeinput">
      <label for="nm-11-theme" class="nm-11__themebtn">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 3a9 9 0 1 0 9 9 7 7 0 0 1-9-9Z"/></svg>
        Theme
      </label>
  <div class="nm-11__stage">
    <header class="nm-11__head">
      <p class="nm-11__kicker">Form · inputs</p>
      <h2 class="nm-11__heading" id="nm-11-heading">Fields carved into the surface</h2>
      <p class="nm-11__sub">Soft UI's best affordance — and the one place its focus state needs the most help.</p>
    </header>

    <div class="nm-11__search">
      <span class="nm-11__searchicon" aria-hidden="true">
        <svg viewBox="0 0 24 24" width="19" height="19"><circle cx="11" cy="11" r="6.4" fill="none" stroke="currentColor" stroke-width="2"/><path d="M15.8 15.8 20 20" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
      </span>
      <input class="nm-11__searchinput" type="search" placeholder="Search invoices, clients, drafts" aria-label="Search">
    </div>

    <form class="nm-11__form">
      <div class="nm-11__field">
        <label class="nm-11__label" for="nm-11-name">Full name</label>
        <div class="nm-11__well">
          <input class="nm-11__input" type="text" id="nm-11-name" value="Ilse Marchetti">
        </div>
        <p class="nm-11__hint">As it appears on the account.</p>
      </div>

      <div class="nm-11__field">
        <label class="nm-11__label" for="nm-11-email">Email</label>
        <div class="nm-11__well nm-11__well--error">
          <input class="nm-11__input" type="email" id="nm-11-email" value="ilse@meridian" aria-describedby="nm-11-emailerr">
          <span class="nm-11__stateicon nm-11__stateicon--error" aria-hidden="true">
            <svg viewBox="0 0 20 20" width="16" height="16"><circle cx="10" cy="10" r="8" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M10 5.6v5M10 13.6v.6" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
          </span>
        </div>
        <p class="nm-11__msg nm-11__msg--error" id="nm-11-emailerr">Missing a domain — try [email protected]</p>
      </div>

      <div class="nm-11__field">
        <label class="nm-11__label" for="nm-11-plan">Billing cycle</label>
        <div class="nm-11__well">
          <select class="nm-11__select" id="nm-11-plan">
            <option>Monthly</option>
            <option selected>Quarterly</option>
            <option>Annual</option>
          </select>
          <span class="nm-11__chev" aria-hidden="true">
            <svg viewBox="0 0 20 20" width="15" height="15"><path d="M5 8l5 5 5-5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </span>
        </div>
      </div>

      <div class="nm-11__field nm-11__field--wide">
        <label class="nm-11__label" for="nm-11-note">Note to the finance team</label>
        <div class="nm-11__well nm-11__well--area">
          <textarea class="nm-11__textarea" id="nm-11-note" rows="3">Please apply the Q3 credit before invoicing.</textarea>
        </div>
        <p class="nm-11__hint">Visible to your team only.</p>
      </div>

      <div class="nm-11__actions">
        <button class="nm-11__submit" type="button">Save details</button>
        <p class="nm-11__msg nm-11__msg--ok">
          <span class="nm-11__stateicon nm-11__stateicon--ok" aria-hidden="true"><svg viewBox="0 0 20 20" width="15" height="15"><path d="M4 10.5l4 4 8-9" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
          Draft saved 2 minutes ago
        </p>
      </div>
    </form>
  </div>
</section>
```
## CSS
```css
.nm-11 {
  position: relative;
  --nm-11-surface: #e9e7e3;
  --nm-11-dark: rgba(180,175,167,0.64);
  --nm-11-light: rgba(255,255,255,0.94);
  --nm-11-ink: #292723;
  --nm-11-muted: #5d5a52;
  --nm-11-placeholder: #6b675f;
  --nm-11-border: #a29d94;
  --nm-11-accent: #3a6a5c;
  --nm-11-error: #a13a2c;
  --nm-11-ok: #37694a;
  --nm-11-inset: 5px;
  --nm-11-font-display: "Inter", "Helvetica Neue", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--nm-11-surface);
  color: var(--nm-11-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

@supports (color: oklch(0.9 0.01 80)) {
  .nm-11 {
    --nm-11-surface: oklch(0.918 0.006 80);
    --nm-11-ink: oklch(0.27 0.008 76);
    --nm-11-muted: oklch(0.46 0.011 76);
    --nm-11-placeholder: oklch(0.51 0.011 76);
    --nm-11-accent: oklch(0.46 0.06 170);
    --nm-11-error: oklch(0.47 0.15 28);
    --nm-11-ok: oklch(0.46 0.09 155);
  }
}

@supports (color: color-mix(in oklab, #fff, #000)) {
  .nm-11 {
    --nm-11-dark: color-mix(in oklab, var(--nm-11-surface), #000 20%);
    --nm-11-light: color-mix(in oklab, var(--nm-11-surface), #fff 92%);
    --nm-11-border: color-mix(in oklab, var(--nm-11-surface), var(--nm-11-ink) 34%);
  }
}

.nm-11 *,
.nm-11 *::before,
.nm-11 *::after {
  box-sizing: border-box;
}

.nm-11__stage {
  max-width: 820px;
  margin: 0 auto;
  min-height: 100vh;
  padding: clamp(26px, 5vw, 56px) clamp(16px, 4vw, 40px);
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: clamp(20px, 3.2vw, 30px);
}

.nm-11__head {
  max-width: 56ch;
  display: flex;
  flex-direction: column;
  gap: 9px;
}

.nm-11__kicker {
  margin: 0;
  font-size: 0.7rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--nm-11-muted);
}

.nm-11__heading {
  margin: 0;
  font-family: var(--nm-11-font-display);
  font-size: clamp(1.5rem, 4.2vw, 2.25rem);
  font-weight: 600;
  letter-spacing: -0.025em;
  line-height: 1.12;
  text-wrap: balance;
}

.nm-11__sub {
  margin: 0;
  font-size: 0.94rem;
  line-height: 1.6;
  color: var(--nm-11-muted);
  text-wrap: pretty;
}

.nm-11__search {
  display: flex;
  align-items: center;
  gap: 12px;
  min-height: 54px;
  padding: 0 20px;
  border-radius: 999px;
  border: 1px solid var(--nm-11-border);
  background: var(--nm-11-surface);
  box-shadow: inset var(--nm-11-inset) var(--nm-11-inset) 11px var(--nm-11-dark), inset calc(var(--nm-11-inset) * -1) calc(var(--nm-11-inset) * -1) 11px var(--nm-11-light);
}

.nm-11__search:focus-within {
  outline: 2px solid var(--nm-11-accent);
  outline-offset: 3px;
}

.nm-11__search:focus-within .nm-11__searchicon {
  color: var(--nm-11-accent);
}

.nm-11__searchicon {
  display: inline-flex;
  color: var(--nm-11-muted);
  flex: none;
  transition: color 160ms ease;
}

.nm-11__searchinput {
  flex: 1;
  min-inline-size: 0;
  border: 0;
  background: transparent;
  font: inherit;
  font-size: 16px;
  color: var(--nm-11-ink);
  outline: none;
  -webkit-appearance: none;
  appearance: none;
}

.nm-11__searchinput::placeholder {
  color: var(--nm-11-placeholder);
}

.nm-11__form {
  display: grid;
  grid-template-columns: 1fr;
  gap: clamp(16px, 2.6vw, 22px);
}

@media (min-width: 640px) {
  .nm-11__form {
    grid-template-columns: 1fr 1fr;
  }

  .nm-11__field--wide,
    .nm-11__actions {
    grid-column: 1 / -1;
  }
}

.nm-11__field {
  display: flex;
  flex-direction: column;
  gap: 8px;
  min-inline-size: 0;
}

.nm-11__label {
  font-family: var(--nm-11-font-display);
  font-size: 0.78rem;
  font-weight: 600;
  letter-spacing: 0.02em;
}

.nm-11__well {
  position: relative;
  display: flex;
  align-items: center;
  gap: 10px;
  min-height: 50px;
  padding: 0 16px;
  border-radius: 14px;
  border: 1px solid var(--nm-11-border);
  background: var(--nm-11-surface);
  box-shadow: inset var(--nm-11-inset) var(--nm-11-inset) 10px var(--nm-11-dark), inset calc(var(--nm-11-inset) * -1) calc(var(--nm-11-inset) * -1) 10px var(--nm-11-light);
}

.nm-11__well--area {
  min-height: 96px;
  padding: 12px 16px;
  align-items: stretch;
}

.nm-11__well--error {
  border-color: var(--nm-11-error);
}

.nm-11__well:focus-within {
  outline: 2px solid var(--nm-11-accent);
  outline-offset: 3px;
}

.nm-11__input,
.nm-11__textarea,
.nm-11__select {
  flex: 1;
  min-inline-size: 0;
  border: 0;
  background: transparent;
  font: inherit;
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  font-size: 16px;
  color: var(--nm-11-ink);
  outline: none;
}

.nm-11__textarea {
  resize: vertical;
  line-height: 1.55;
}

.nm-11__select {
  -webkit-appearance: none;
  appearance: none;
  cursor: pointer;
  padding-right: 8px;
}

.nm-11__chev {
  position: absolute;
  right: 14px;
  display: inline-flex;
  color: var(--nm-11-muted);
  pointer-events: none;
}

.nm-11__stateicon {
  display: inline-flex;
  flex: none;
}

.nm-11__stateicon--error {
  color: var(--nm-11-error);
}

.nm-11__stateicon--ok {
  color: var(--nm-11-ok);
}

.nm-11__hint {
  margin: 0;
  font-size: 0.75rem;
  line-height: 1.5;
  color: var(--nm-11-muted);
}

.nm-11__msg {
  margin: 0;
  display: flex;
  align-items: center;
  gap: 7px;
  font-size: 0.77rem;
  font-weight: 600;
  line-height: 1.5;
}

.nm-11__msg--error {
  color: var(--nm-11-error);
}

.nm-11__msg--ok {
  color: var(--nm-11-ok);
}

.nm-11__actions {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 16px;
}

.nm-11__submit {
  min-height: 48px;
  padding: 0 24px;
  border-radius: 14px;
  border: 1px solid var(--nm-11-accent);
  background: var(--nm-11-surface);
  color: var(--nm-11-accent);
  font: inherit;
  font-family: var(--nm-11-font-display);
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  box-shadow: 7px 7px 15px var(--nm-11-dark), -7px -7px 15px var(--nm-11-light);
  transition: box-shadow 160ms ease;
}

.nm-11__submit:active {
  box-shadow: inset 5px 5px 11px var(--nm-11-dark), inset -5px -5px 11px var(--nm-11-light);
}

.nm-11__submit:focus-visible {
  outline: 2px solid var(--nm-11-accent);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .nm-11__submit,
    .nm-11__searchicon {
    transition: none;
  }
}

@media (prefers-color-scheme: dark) {
  .nm-11 {
    --nm-11-surface: #2b2926;
    --nm-11-dark: rgba(12,11,10,0.72);
    --nm-11-light: rgba(92,88,82,0.44);
    --nm-11-ink: #ecebe6;
    --nm-11-muted: #a49f95;
    --nm-11-placeholder: #9a9views;
    --nm-11-placeholder: #9a9489;
    --nm-11-border: #857f75;
    --nm-11-accent: #6cc0a8;
    --nm-11-error: #e8897a;
    --nm-11-ok: #82c497;
  }

  @supports (color: color-mix(in oklab, #fff, #000)) {
    .nm-11 {
      --nm-11-dark: color-mix(in oklab, var(--nm-11-surface), #000 55%);
      --nm-11-light: color-mix(in oklab, var(--nm-11-surface), #fff 14%);
    }
  }
}

.nm-11[data-theme="dark"] {
  --nm-11-surface: #2b2926;
  --nm-11-dark: rgba(12,11,10,0.72);
  --nm-11-light: rgba(92,88,82,0.44);
  --nm-11-ink: #ecebe6;
  --nm-11-muted: #a49f95;
  --nm-11-placeholder: #9a9489;
  --nm-11-border: #857f75;
  --nm-11-accent: #6cc0a8;
  --nm-11-error: #e8897a;
  --nm-11-ok: #82c497;
}

@supports (color: color-mix(in oklab, #fff, #000)) {
  .nm-11[data-theme="dark"] {
    --nm-11-dark: color-mix(in oklab, var(--nm-11-surface), #000 55%);
    --nm-11-light: color-mix(in oklab, var(--nm-11-surface), #fff 14%);
  }
}
/* Pure-CSS theme toggle. Mirrors the [data-theme="dark"] rules above so
   the demo's own dark palette is reachable from inside the demo. */

.nm-11__themeinput {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: 0;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.nm-11__themebtn {
  position: absolute;
  inset-block-start: clamp(10px, 2vw, 18px);
  inset-inline-end: clamp(10px, 2vw, 18px);
  z-index: 5;
  display: inline-flex;
  align-items: center;
  gap: 7px;
  min-height: 44px;
  padding: 0 14px;
  border-radius: 999px;
  background: var(--nm-11-surface);
  color: var(--nm-11-ink);
  border: 1px solid var(--nm-11-line);
  font: 600 11px/1 var(--nm-11-font-display, system-ui);
  letter-spacing: 0.12em;
  text-transform: uppercase;
  cursor: pointer;
  box-shadow: var(--nm-11-distance, 6px) var(--nm-11-distance, 6px) var(--nm-11-blur, 14px) var(--nm-11-dark), calc(-1 * var(--nm-11-distance, 6px)) calc(-1 * var(--nm-11-distance, 6px)) var(--nm-11-blur, 14px) var(--nm-11-light);
  transition: box-shadow 180ms ease, color 180ms ease;
}

.nm-11__themebtn:hover {
  color: var(--nm-11-ink);
}

.nm-11__themeinput:focus-visible + .nm-11__themebtn {
  outline: 2px solid var(--nm-11-ink);
  outline-offset: 3px;
}

.nm-11:has(#nm-11-theme:checked) .nm-11__themebtn {
  box-shadow: inset var(--nm-11-distance, 6px) var(--nm-11-distance, 6px) var(--nm-11-blur, 14px) var(--nm-11-dark), inset calc(-1 * var(--nm-11-distance, 6px)) calc(-1 * var(--nm-11-distance, 6px)) var(--nm-11-blur, 14px) var(--nm-11-light);
}

.nm-11__themebtn svg {
  inline-size: 13px;
  block-size: 13px;
  flex: none;
}

.nm-11:has(#nm-11-theme:checked) {
  --nm-11-surface: #2b2926;
  --nm-11-dark: rgba(12,11,10,0.72);
  --nm-11-light: rgba(92,88,82,0.44);
  --nm-11-ink: #ecebe6;
  --nm-11-muted: #a49f95;
  --nm-11-placeholder: #9a9489;
  --nm-11-border: #857f75;
  --nm-11-accent: #6cc0a8;
  --nm-11-error: #e8897a;
  --nm-11-ok: #82c497;
}

@media (prefers-color-scheme: light) {
  .nm-11:has(#nm-11-theme:checked) {
    --nm-11-surface: #2b2926;
    --nm-11-dark: rgba(12,11,10,0.72);
    --nm-11-light: rgba(92,88,82,0.44);
    --nm-11-ink: #ecebe6;
    --nm-11-muted: #a49f95;
    --nm-11-placeholder: #9a9489;
    --nm-11-border: #857f75;
    --nm-11-accent: #6cc0a8;
    --nm-11-error: #e8897a;
    --nm-11-ok: #82c497;
  }
}

@media (prefers-color-scheme: dark) {
  /* Base already resolves dark here, so :checked restores light —
       without this the toggle is inert for dark-OS visitors. */

  .nm-11:has(#nm-11-theme:checked) {
    --nm-11-surface: #e9e7e3;
    --nm-11-dark: rgba(180,175,167,0.64);
    --nm-11-light: rgba(255,255,255,0.94);
    --nm-11-ink: #292723;
    --nm-11-muted: #5d5a52;
    --nm-11-placeholder: #6b675f;
    --nm-11-border: #a29d94;
    --nm-11-accent: #3a6a5c;
    --nm-11-error: #a13a2c;
    --nm-11-ok: #37694a;
  }
}

@media (prefers-reduced-motion: reduce) {
  .nm-11__themebtn {
    transition: none;
  }
}
```
