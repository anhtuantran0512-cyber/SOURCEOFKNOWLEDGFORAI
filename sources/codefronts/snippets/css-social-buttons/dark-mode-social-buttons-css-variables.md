---
source: "codefronts"
url: "https://codefronts.com/snippets/css-social-buttons/dark-mode-social-buttons-css-variables/"
title: "Dark Mode Social Buttons CSS Variables"
section: "snippets"
category: "css-social-buttons"
category_name: "CSS Social Buttons"
description: "A theme-aware social row with a working light and dark switch and no JavaScript at all."
has_js: "false"
---

Here's a working CSS Social Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dark Mode Social Buttons CSS Variables
Source: https://codefronts.com/snippets/css-social-buttons/dark-mode-social-buttons-css-variables/

A theme-aware social row with a working light and dark switch and no JavaScript at all. A visually-hidden checkbox holds the state and :has() on the demo root rewrites the custom properties, so one :checked flips every colour — including the brand tokens, which are lightened for dark surfaces rather than reused unchanged. Dark is the default; data-theme is the host override.
## HTML
```html
<div class="soc-20">
  <div class="soc-20__stage">
    <div class="soc-20__card">
      <div class="soc-20__top">
        <div>
          <p class="soc-20__eyebrow">Theme aware</p>
          <h2 class="soc-20__title">One checkbox, every token</h2>
        </div>
        <label class="soc-20__toggle">
          <input class="soc-20__switch" type="checkbox" aria-label="Use the light theme">
          <span class="soc-20__track" aria-hidden="true">
            <span class="soc-20__thumb">
              <svg class="soc-20__moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 14.4A8.4 8.4 0 0 1 9.6 4a8.4 8.4 0 1 0 10.4 10.4Z"/></svg>
              <svg class="soc-20__sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="4.2"/><path d="M12 3v2.2M12 18.8V21M4.2 12H6M18 12h1.8M6.5 6.5 7.8 7.8M16.2 16.2l1.3 1.3M17.5 6.5l-1.3 1.3M7.8 16.2l-1.3 1.3"/></svg>
            </span>
          </span>
          <span class="soc-20__toggleText"></span>
        </label>
      </div>
      <div class="soc-20__row">
        <a class="soc-20__btn" style="--bl:#0f1419;--bd:#e8e8ef" href="https://example.com/samrivera" target="_blank" rel="noopener">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round"><path d="M5 5.5 19 18.5"/><path d="M19 5.5 5 18.5"/></svg><span>X</span></a>
        <a class="soc-20__btn" style="--bl:#0a66c2;--bd:#5aa9f5" href="https://example.com/in/samrivera" target="_blank" rel="noopener">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="3.5" y="3.5" width="17" height="17" rx="4.5"/><path d="M8 10.5V16"/><circle cx="8" cy="7.9" r=".9" fill="currentColor" stroke="none"/><path d="M12 16v-3.2a1.9 1.9 0 0 1 3.8 0V16"/></svg><span>LinkedIn</span></a>
        <a class="soc-20__btn" style="--bl:#6f42c1;--bd:#b490ff" href="https://example.com/samrivera" target="_blank" rel="noopener">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="8.6"/><path d="m9.8 9.4-2.3 2.6 2.3 2.6"/><path d="m14.2 9.4 2.3 2.6-2.3 2.6"/></svg><span>GitHub</span></a>
        <a class="soc-20__btn" style="--bl:#c2185b;--bd:#ff86b3" href="https://example.com/samrivera" target="_blank" rel="noopener">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2"><rect x="3.6" y="3.6" width="16.8" height="16.8" rx="5"/><circle cx="12" cy="12" r="3.9"/><circle cx="17.1" cy="6.9" r="1.15" fill="currentColor" stroke="none"/></svg><span>Instagram</span></a>
        <a class="soc-20__btn" style="--bl:#0e8a55;--bd:#3ecf8e" href="https://example.com/newsletter" target="_blank" rel="noopener">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5.2" width="18" height="13.6" rx="3.4"/><path d="m4.4 8 6.7 4.7a1.6 1.6 0 0 0 1.8 0L19.6 8"/></svg><span>Newsletter</span></a>
      </div>
      <p class="soc-20__note">Zero JavaScript: the checkbox holds the state and :has() rewrites the tokens.</p>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&display=swap');

.soc-20 {
  --bg: #08080c;
  --surface: #14141b;
  --fg: #f3f3f7;
  --muted: #9696a4;
  --line: #282833;
  --ring: #8ab4ff;
  --track: #2b2b36;
  --thumb: #f3f3f7;
  --thumb-ink: #14141b;
  --sans: "Geist",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  color: var(--fg);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
  transition: background-color .3s ease, color .3s ease;
}

.soc-20:has(.soc-20__switch:checked),
.soc-20[data-theme="light"] {
  --bg: #f4f4f6;
  --surface: #ffffff;
  --fg: #101015;
  --muted: #6a6a76;
  --line: #e5e5ea;
  --ring: #3d63ff;
  --track: #d9d9e2;
  --thumb: #101015;
  --thumb-ink: #ffffff;
}

.soc-20[data-theme="dark"] {
  --bg: #08080c;
  --surface: #14141b;
  --fg: #f3f3f7;
  --muted: #9696a4;
  --line: #282833;
  --ring: #8ab4ff;
  --track: #2b2b36;
  --thumb: #f3f3f7;
  --thumb-ink: #14141b;
}

.soc-20,
.soc-20 *,
.soc-20 *::before,
.soc-20 *::after {
  box-sizing: border-box;
}

.soc-20__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,3.5rem);
}

.soc-20__card {
  inline-size: min(34rem,100%);
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 1.35rem;
  padding: clamp(1.5rem,4vw,2.25rem);
  box-shadow: 0 22px 48px -32px rgb(0 0 0/.7);
  transition: background-color .3s ease, border-color .3s ease;
}

.soc-20__top {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  margin-block-end: 1.6rem;
}

.soc-20__eyebrow {
  margin: 0 0 .4rem;
  font-size: .72rem;
  font-weight: 600;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
}

.soc-20__title {
  margin: 0;
  font-size: clamp(1.05rem,1rem + .8vw,1.35rem);
  font-weight: 600;
  letter-spacing: -.02em;
}

.soc-20__toggle {
  display: inline-flex;
  align-items: center;
  gap: .6rem;
  min-block-size: 2.75rem;
  padding: 0 .3rem;
  cursor: pointer;
  user-select: none;
  border-radius: 999px;
}

.soc-20__switch {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.soc-20__track {
  position: relative;
  display: block;
  inline-size: 3.4rem;
  block-size: 1.9rem;
  border-radius: 999px;
  background: var(--track);
  transition: background-color .3s ease;
}

.soc-20__thumb {
  position: absolute;
  inset-block-start: .2rem;
  inset-inline-start: .2rem;
  display: grid;
  place-items: center;
  inline-size: 1.5rem;
  block-size: 1.5rem;
  border-radius: 50%;
  background: var(--thumb);
  color: var(--thumb-ink);
  transition: translate .28s cubic-bezier(.16,1,.3,1), background-color .3s ease;
}

.soc-20__thumb svg {
  grid-area: 1/1;
  inline-size: .9rem;
  block-size: .9rem;
  transition: opacity .22s ease;
}

.soc-20__sun {
  opacity: 0;
}

.soc-20:has(.soc-20__switch:checked) .soc-20__thumb {
  translate: 1.5rem 0;
}

.soc-20:has(.soc-20__switch:checked) .soc-20__moon {
  opacity: 0;
}

.soc-20:has(.soc-20__switch:checked) .soc-20__sun {
  opacity: 1;
}

.soc-20__toggleText {
  font-size: .82rem;
  font-weight: 550;
  color: var(--muted);
}

.soc-20__toggleText::after {
  content: "Dark";
}

.soc-20:has(.soc-20__switch:checked) .soc-20__toggleText::after {
  content: "Light";
}

.soc-20__toggle:has(.soc-20__switch:focus-visible) {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}

.soc-20__row {
  display: flex;
  flex-wrap: wrap;
  gap: .6rem;
}

.soc-20__btn {
  display: inline-flex;
  align-items: center;
  gap: .5rem;
  min-block-size: 2.875rem;
  padding: 0 1.05rem;
  min-inline-size: 0;
  border: 1px solid var(--line);
  border-radius: .85rem;
  background: var(--surface);
  color: var(--fg);
  text-decoration: none;
  font-size: .88rem;
  font-weight: 550;
  --brand: var(--bd);
  transition: color .25s ease, border-color .25s ease, background-color .25s ease, translate .2s cubic-bezier(.16,1,.3,1);
}

.soc-20:has(.soc-20__switch:checked) .soc-20__btn,
.soc-20[data-theme="light"] .soc-20__btn {
  --brand: var(--bl);
}

.soc-20[data-theme="dark"] .soc-20__btn {
  --brand: var(--bd);
}

.soc-20__btn svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
  color: var(--brand);
  flex: none;
  transition: color .25s ease;
}

.soc-20__btn span {
  min-inline-size: 0;
}

.soc-20__btn:hover {
  translate: 0 -2px;
  color: var(--brand);
  border-color: color-mix(in oklab,var(--brand) 45%,var(--line));
  background: color-mix(in oklab,var(--brand) 10%,var(--surface));
}

.soc-20__btn:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}

.soc-20__note {
  margin: 1.6rem 0 0;
  font-size: .8rem;
  color: var(--muted);
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .soc-20,
    .soc-20__card,
    .soc-20__btn,
    .soc-20__thumb {
    transition-duration: 1ms;
  }

  .soc-20__btn:hover {
    translate: none;
  }
}

@media (forced-colors: active) {
  .soc-20__btn {
    border: 1px solid ButtonText;
    color: ButtonText;
  }

  .soc-20__track {
    border: 1px solid ButtonText;
  }
}
```
