---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-neumorphism/aurum-profile-testimonial/"
title: "Neumorphic Modal and Layered Elevation"
section: "design-styles"
category: "css-neumorphism"
category_name: "CSS Neumorphism"
description: "The layer soft UI cannot express: a modal has to sit above everything, and depth-by-shadow has already run out at three levels."
has_js: "true"
---

Here's a working CSS Neumorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neumorphic Modal and Layered Elevation
Source: https://codefronts.com/design-styles/css-neumorphism/aurum-profile-testimonial/

The layer soft UI cannot express: a modal has to sit above everything, and depth-by-shadow has already run out at three levels. The answer is to change technique — a scrim to separate the layers plus the deepest shadow in the system — built on the native <dialog> element so focus trapping, Escape and inertness come for free.
## HTML
```html
<section class="nm-20" aria-labelledby="nm-20-heading">
      <input type="checkbox" id="nm-20-theme" class="nm-20__themeinput">
      <label for="nm-20-theme" class="nm-20__themebtn">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 3a9 9 0 1 0 9 9 7 7 0 0 1-9-9Z"/></svg>
        Theme
      </label>
  <div class="nm-20__stage">
    <header class="nm-20__head">
      <p class="nm-20__kicker">Pattern · overlay</p>
      <h2 class="nm-20__heading" id="nm-20-heading">The layer shadows cannot reach</h2>
      <p class="nm-20__sub">Three elevations is the ceiling. A modal needs a fourth, so it changes mechanism — a scrim, not a bigger shadow.</p>
    </header>

    <div class="nm-20__page">
      <article class="nm-20__card">
        <p class="nm-20__cardtitle">Retention policy</p>
        <p class="nm-20__cardbody">Archived projects are removed after 180 days. Changing this affects every workspace on the account.</p>
        <button class="nm-20__open" type="button">Change policy…</button>
      </article>
      <article class="nm-20__card nm-20__card--muted">
        <p class="nm-20__cardtitle">Export</p>
        <p class="nm-20__cardbody">Download a full archive as CSV or OFX. Large exports are emailed when ready.</p>
      </article>
    </div>

    <dialog class="nm-20__dialog" aria-labelledby="nm-20-dtitle">
      <button class="nm-20__close" type="button" aria-label="Close dialog">
        <svg viewBox="0 0 20 20" width="16" height="16" aria-hidden="true"><path d="M5 5l10 10M15 5L5 15" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
      </button>
      <h3 class="nm-20__dtitle" id="nm-20-dtitle">Change retention policy</h3>
      <p class="nm-20__dbody">Archived projects will be removed after the period you choose. Existing archives older than the new period are deleted within 24 hours.</p>
      <div class="nm-20__dwell">
        <label class="nm-20__dlabel" for="nm-20-period">Retention period</label>
        <select class="nm-20__dselect" id="nm-20-period">
          <option>90 days</option>
          <option selected>180 days</option>
          <option>365 days</option>
          <option>Never delete</option>
        </select>
      </div>
      <div class="nm-20__dactions">
        <button class="nm-20__dbtn nm-20__dbtn--ghost" type="button" data-close>Cancel</button>
        <button class="nm-20__dbtn nm-20__dbtn--primary" type="button" data-close>Apply policy</button>
      </div>
    </dialog>
  </div>
</section>
```
## CSS
```css
.nm-20 {
  position: relative;
  --nm-20-surface: #e7e6e2;
  --nm-20-dark: rgba(174,172,164,0.64);
  --nm-20-light: rgba(255,255,255,0.94);
  --nm-20-ink: #282722;
  --nm-20-muted: #5a584f;
  --nm-20-border: #98958c;
  --nm-20-accent: #385f7a;
  --nm-20-scrim: rgba(40,39,34,0.48);
  --nm-20-font-display: "Signifier", "Iowan Old Style", Georgia, serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--nm-20-surface);
  color: var(--nm-20-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

@supports (color: oklch(0.9 0.01 90)) {
  .nm-20 {
    --nm-20-surface: oklch(0.915 0.006 92);
    --nm-20-ink: oklch(0.27 0.009 84);
    --nm-20-muted: oklch(0.45 0.012 84);
    --nm-20-accent: oklch(0.48 0.08 234);
  }
}

@supports (color: color-mix(in oklab, #fff, #000)) {
  .nm-20 {
    --nm-20-dark: color-mix(in oklab, var(--nm-20-surface), #000 20%);
    --nm-20-light: color-mix(in oklab, var(--nm-20-surface), #fff 92%);
    --nm-20-border: color-mix(in oklab, var(--nm-20-surface), var(--nm-20-ink) 33%);
  }
}

.nm-20 *,
.nm-20 *::before,
.nm-20 *::after {
  box-sizing: border-box;
}

.nm-20__stage {
  max-width: 900px;
  margin: 0 auto;
  min-height: 100vh;
  padding: clamp(26px, 5vw, 56px) clamp(16px, 4vw, 40px);
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: clamp(22px, 3.6vw, 34px);
}

.nm-20__head {
  max-width: 58ch;
  display: flex;
  flex-direction: column;
  gap: 9px;
}

.nm-20__kicker {
  margin: 0;
  font-size: 0.7rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--nm-20-muted);
}

.nm-20__heading {
  margin: 0;
  font-family: var(--nm-20-font-display);
  font-size: clamp(1.6rem, 4.4vw, 2.4rem);
  font-weight: 400;
  letter-spacing: -0.015em;
  line-height: 1.1;
  text-wrap: balance;
}

.nm-20__sub {
  margin: 0;
  font-size: 0.94rem;
  line-height: 1.6;
  color: var(--nm-20-muted);
  text-wrap: pretty;
}

.nm-20__page {
  display: grid;
  grid-template-columns: 1fr;
  gap: clamp(16px, 2.8vw, 24px);
}

@media (min-width: 640px) {
  .nm-20__page {
    grid-template-columns: 1fr 1fr;
  }
}

.nm-20__card {
  border-radius: 22px;
  padding: clamp(18px, 3vw, 26px);
  display: flex;
  flex-direction: column;
  gap: 12px;
  align-items: flex-start;
  min-inline-size: 0;
  background: var(--nm-20-surface);
  border: 1px solid var(--nm-20-border);
  box-shadow: 10px 10px 21px var(--nm-20-dark), -10px -10px 21px var(--nm-20-light);
}

.nm-20__card--muted {
  box-shadow: 5px 5px 11px var(--nm-20-dark), -5px -5px 11px var(--nm-20-light);
}

.nm-20__cardtitle {
  margin: 0;
  font-family: var(--nm-20-font-display);
  font-size: 1.1rem;
}

.nm-20__cardbody {
  margin: 0;
  font-size: 0.85rem;
  line-height: 1.62;
  color: var(--nm-20-muted);
  text-wrap: pretty;
}

.nm-20__open {
  min-height: 46px;
  padding: 0 20px;
  border-radius: 13px;
  border: 1px solid var(--nm-20-accent);
  background: var(--nm-20-surface);
  color: var(--nm-20-accent);
  font: inherit;
  font-size: 0.88rem;
  font-weight: 600;
  cursor: pointer;
  box-shadow: 6px 6px 13px var(--nm-20-dark), -6px -6px 13px var(--nm-20-light);
}

.nm-20__open:active {
  box-shadow: inset 4px 4px 10px var(--nm-20-dark), inset -4px -4px 10px var(--nm-20-light);
}

.nm-20__open:focus-visible {
  outline: 2px solid var(--nm-20-accent);
  outline-offset: 3px;
}

.nm-20__dialog {
  width: min(92vw, 440px);
  border: 1px solid var(--nm-20-border);
  border-radius: 26px;
  padding: clamp(22px, 4vw, 32px);
  background: var(--nm-20-surface);
  color: var(--nm-20-ink);
  box-shadow: 22px 22px 48px rgba(0,0,0,0.28), -14px -14px 32px var(--nm-20-light);
}

.nm-20__dialog::backdrop {
  background: var(--nm-20-scrim);
}

@supports ((-webkit-backdrop-filter: blur(2px)) or (backdrop-filter: blur(2px))) {
  .nm-20__dialog::backdrop {
    -webkit-backdrop-filter: blur(3px);
    backdrop-filter: blur(3px);
  }
}

@supports (transition-behavior: allow-discrete) {
  .nm-20__dialog {
    opacity: 0;
    transform: scale(0.96);
    transition: opacity 220ms ease, transform 220ms cubic-bezier(0.2, 0.9, 0.3, 1), overlay 220ms allow-discrete, display 220ms allow-discrete;
  }

  .nm-20__dialog[open] {
    opacity: 1;
    transform: scale(1);
  }

  @starting-style {
    .nm-20__dialog[open] {
      opacity: 0;
      transform: scale(0.96);
    }
  }

  .nm-20__dialog::backdrop {
    opacity: 0;
    transition: opacity 220ms ease, overlay 220ms allow-discrete, display 220ms allow-discrete;
  }

  .nm-20__dialog[open]::backdrop {
    opacity: 1;
  }

  @starting-style {
    .nm-20__dialog[open]::backdrop {
      opacity: 0;
    }
  }
}

.nm-20__close {
  position: absolute;
  top: 16px;
  right: 16px;
  width: 44px;
  height: 44px;
  display: grid;
  place-items: center;
  border-radius: 50%;
  border: 1px solid var(--nm-20-border);
  background: var(--nm-20-surface);
  color: var(--nm-20-muted);
  cursor: pointer;
  box-shadow: 4px 4px 10px var(--nm-20-dark), -4px -4px 10px var(--nm-20-light);
}

.nm-20__close:active {
  box-shadow: inset 3px 3px 8px var(--nm-20-dark), inset -3px -3px 8px var(--nm-20-light);
}

.nm-20__close:focus-visible {
  outline: 2px solid var(--nm-20-accent);
  outline-offset: 3px;
}

.nm-20__dtitle {
  margin: 0 0 10px;
  padding-right: 48px;
  font-family: var(--nm-20-font-display);
  font-size: 1.3rem;
  font-weight: 400;
  line-height: 1.2;
}

.nm-20__dbody {
  margin: 0 0 20px;
  font-size: 0.86rem;
  line-height: 1.62;
  color: var(--nm-20-muted);
  text-wrap: pretty;
}

.nm-20__dwell {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin-bottom: 22px;
}

.nm-20__dlabel {
  font-size: 0.78rem;
  font-weight: 600;
}

.nm-20__dselect {
  min-height: 48px;
  padding: 0 16px;
  border-radius: 13px;
  border: 1px solid var(--nm-20-border);
  background: var(--nm-20-surface);
  color: var(--nm-20-ink);
  font: inherit;
  font-size: 16px;
  cursor: pointer;
  box-shadow: inset 4px 4px 9px var(--nm-20-dark), inset -4px -4px 9px var(--nm-20-light);
}

.nm-20__dselect:focus-visible {
  outline: 2px solid var(--nm-20-accent);
  outline-offset: 3px;
}

.nm-20__dactions {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  justify-content: flex-end;
}

.nm-20__dbtn {
  min-height: 46px;
  padding: 0 20px;
  border-radius: 13px;
  font: inherit;
  font-size: 0.88rem;
  font-weight: 600;
  cursor: pointer;
  background: var(--nm-20-surface);
  border: 1px solid var(--nm-20-border);
  color: var(--nm-20-ink);
  box-shadow: 5px 5px 11px var(--nm-20-dark), -5px -5px 11px var(--nm-20-light);
}

.nm-20__dbtn--primary {
  color: #fff;
  background: var(--nm-20-accent);
  border-color: var(--nm-20-accent);
}

.nm-20__dbtn--ghost {
  color: var(--nm-20-muted);
  box-shadow: inset 3px 3px 8px var(--nm-20-dark), inset -3px -3px 8px var(--nm-20-light);
}

.nm-20__dbtn:focus-visible {
  outline: 2px solid var(--nm-20-accent);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  @supports (transition-behavior: allow-discrete) {
    .nm-20__dialog {
      transform: none;
      transition: opacity 120ms ease, overlay 120ms allow-discrete, display 120ms allow-discrete;
    }

    .nm-20__dialog[open] {
      transform: none;
    }

    @starting-style {
      .nm-20__dialog[open] {
        transform: none;
      }
    }
  }
}

@media (prefers-color-scheme: dark) {
  .nm-20 {
    --nm-20-surface: #292822;
    --nm-20-dark: rgba(11,11,9,0.72);
    --nm-20-light: rgba(90,88,80,0.44);
    --nm-20-ink: #eae9e3;
    --nm-20-muted: #9e9b91;
    --nm-20-border: #86837a;
    --nm-20-accent: #82b3d2;
    --nm-20-scrim: rgba(8,8,6,0.6);
  }

  @supports (color: color-mix(in oklab, #fff, #000)) {
    .nm-20 {
      --nm-20-dark: color-mix(in oklab, var(--nm-20-surface), #000 55%);
      --nm-20-light: color-mix(in oklab, var(--nm-20-surface), #fff 14%);
    }
  }

  .nm-20__dbtn--primary {
    color: #14202a;
  }
}

.nm-20[data-theme="dark"] {
  --nm-20-surface: #292822;
  --nm-20-dark: rgba(11,11,9,0.72);
  --nm-20-light: rgba(90,88,80,0.44);
  --nm-20-ink: #eae9e3;
  --nm-20-muted: #9e9b91;
  --nm-20-border: #86837a;
  --nm-20-accent: #82b3d2;
  --nm-20-scrim: rgba(8,8,6,0.6);
}

@supports (color: color-mix(in oklab, #fff, #000)) {
  .nm-20[data-theme="dark"] {
    --nm-20-dark: color-mix(in oklab, var(--nm-20-surface), #000 55%);
    --nm-20-light: color-mix(in oklab, var(--nm-20-surface), #fff 14%);
  }
}

.nm-20[data-theme="dark"] .nm-20__dbtn--primary {
  color: #14202a;
}
/* Pure-CSS theme toggle. Mirrors the [data-theme="dark"] rules above so
   the demo's own dark palette is reachable from inside the demo. */

.nm-20__themeinput {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: 0;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.nm-20__themebtn {
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
  background: var(--nm-20-surface);
  color: var(--nm-20-ink);
  border: 1px solid var(--nm-20-line);
  font: 600 11px/1 var(--nm-20-font-display, system-ui);
  letter-spacing: 0.12em;
  text-transform: uppercase;
  cursor: pointer;
  box-shadow: var(--nm-20-distance, 6px) var(--nm-20-distance, 6px) var(--nm-20-blur, 14px) var(--nm-20-dark), calc(-1 * var(--nm-20-distance, 6px)) calc(-1 * var(--nm-20-distance, 6px)) var(--nm-20-blur, 14px) var(--nm-20-light);
  transition: box-shadow 180ms ease, color 180ms ease;
}

.nm-20__themebtn:hover {
  color: var(--nm-20-ink);
}

.nm-20__themeinput:focus-visible + .nm-20__themebtn {
  outline: 2px solid var(--nm-20-ink);
  outline-offset: 3px;
}

.nm-20:has(#nm-20-theme:checked) .nm-20__themebtn {
  box-shadow: inset var(--nm-20-distance, 6px) var(--nm-20-distance, 6px) var(--nm-20-blur, 14px) var(--nm-20-dark), inset calc(-1 * var(--nm-20-distance, 6px)) calc(-1 * var(--nm-20-distance, 6px)) var(--nm-20-blur, 14px) var(--nm-20-light);
}

.nm-20__themebtn svg {
  inline-size: 13px;
  block-size: 13px;
  flex: none;
}

.nm-20:has(#nm-20-theme:checked) {
  --nm-20-surface: #292822;
  --nm-20-dark: rgba(11,11,9,0.72);
  --nm-20-light: rgba(90,88,80,0.44);
  --nm-20-ink: #eae9e3;
  --nm-20-muted: #9e9b91;
  --nm-20-border: #86837a;
  --nm-20-accent: #82b3d2;
  --nm-20-scrim: rgba(8,8,6,0.6);
}

@media (prefers-color-scheme: light) {
  .nm-20:has(#nm-20-theme:checked) {
    --nm-20-surface: #292822;
    --nm-20-dark: rgba(11,11,9,0.72);
    --nm-20-light: rgba(90,88,80,0.44);
    --nm-20-ink: #eae9e3;
    --nm-20-muted: #9e9b91;
    --nm-20-border: #86837a;
    --nm-20-accent: #82b3d2;
    --nm-20-scrim: rgba(8,8,6,0.6);
  }
}

@media (prefers-color-scheme: dark) {
  /* Base already resolves dark here, so :checked restores light —
       without this the toggle is inert for dark-OS visitors. */

  .nm-20:has(#nm-20-theme:checked) {
    --nm-20-surface: #e7e6e2;
    --nm-20-dark: rgba(174,172,164,0.64);
    --nm-20-light: rgba(255,255,255,0.94);
    --nm-20-ink: #282722;
    --nm-20-muted: #5a584f;
    --nm-20-border: #98958c;
    --nm-20-accent: #385f7a;
    --nm-20-scrim: rgba(40,39,34,0.48);
  }
}

@media (prefers-reduced-motion: reduce) {
  .nm-20__themebtn {
    transition: none;
  }
}
```

## JavaScript
```js
const s = document.querySelector('.nm-20');
if (s) {
  const dlg = s.querySelector('.nm-20__dialog');
  s.querySelector('.nm-20__open').addEventListener('click', () => dlg.showModal());
  s.querySelector('.nm-20__close').addEventListener('click', () => dlg.close());
  s.querySelectorAll('[data-close]').forEach(b => b.addEventListener('click', () => dlg.close()));
}
```
