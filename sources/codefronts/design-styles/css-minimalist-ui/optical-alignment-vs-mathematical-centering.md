---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-minimalist-ui/optical-alignment-vs-mathematical-centering/"
title: "Optical Alignment vs Mathematical Centering"
section: "design-styles"
category: "css-minimalist-ui"
category_name: "CSS Minimalist UI"
description: "A play triangle centred by maths looks left-heavy, and a quotation mark that starts flush looks indented."
has_js: "false"
---

Here's a working CSS Minimalist UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Optical Alignment vs Mathematical Centering
Source: https://codefronts.com/design-styles/css-minimalist-ui/optical-alignment-vs-mathematical-centering/

A play triangle centred by maths looks left-heavy, and a quotation mark that starts flush looks indented. Each pair here shows the mathematically-centred version beside the optically-corrected one with the nudge value printed, so you can see the correction and know exactly how much of it to apply.
## HTML
```html
<section class="mu-04" aria-labelledby="mu-04-title">
  <h2 class="mu-04__sr" id="mu-04-title">Optical alignment examples</h2>
  <div class="mu-04__theme">
    <input class="mu-04__theme-input" type="checkbox" id="mu-04-theme">
    <label class="mu-04__theme-label" for="mu-04-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="mu-04__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="mu-04__stage">

    <div class="mu-04__grid">
      <article class="mu-04__case" aria-labelledby="mu-04-c1">
        <h3 class="mu-04__case-title" id="mu-04-c1">Play triangle in a round button</h3>
        <div class="mu-04__demo">
          <div class="mu-04__slot">
            <button class="mu-04__btn mu-04__btn--guide" type="button">
              <svg class="mu-04__icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M8 5.5v13l11-6.5z" fill="currentColor"/></svg>
              <span class="mu-04__sr">Play &mdash; mathematically centred</span>
            </button>
            <p class="mu-04__label">Mathematical<span>translate: 0</span></p>
          </div>
          <div class="mu-04__slot">
            <button class="mu-04__btn mu-04__btn--guide mu-04__btn--fixed" type="button">
              <svg class="mu-04__icon mu-04__icon--nudged" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M8 5.5v13l11-6.5z" fill="currentColor"/></svg>
              <span class="mu-04__sr">Play &mdash; optically corrected</span>
            </button>
            <p class="mu-04__label">Optical<span>translateX(0.06em)</span></p>
          </div>
        </div>
      </article>

      <article class="mu-04__case" aria-labelledby="mu-04-c2">
        <h3 class="mu-04__case-title" id="mu-04-c2">Opening quotation mark</h3>
        <div class="mu-04__demo mu-04__demo--stack">
          <div class="mu-04__slot mu-04__slot--wide">
            <blockquote class="mu-04__quote">
              <p>Restraint is a budget, not a mood.</p>
            </blockquote>
            <p class="mu-04__label">Mathematical<span>text-indent: 0</span></p>
          </div>
          <div class="mu-04__slot mu-04__slot--wide">
            <blockquote class="mu-04__quote mu-04__quote--hang">
              <p>Restraint is a budget, not a mood.</p>
            </blockquote>
            <p class="mu-04__label">Optical<span>text-indent: &minus;0.42em</span></p>
          </div>
        </div>
      </article>

      <article class="mu-04__case" aria-labelledby="mu-04-c3">
        <h3 class="mu-04__case-title" id="mu-04-c3">Icon beside a label</h3>
        <div class="mu-04__demo">
          <div class="mu-04__slot">
            <span class="mu-04__pill">
              <svg class="mu-04__icon-sm" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 12h13m0 0-5-5m5 5-5 5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
              Continue
            </span>
            <p class="mu-04__label">Mathematical<span>baseline aligned</span></p>
          </div>
          <div class="mu-04__slot">
            <span class="mu-04__pill">
              <svg class="mu-04__icon-sm mu-04__icon-sm--nudged" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 12h13m0 0-5-5m5 5-5 5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
              Continue
            </span>
            <p class="mu-04__label">Optical<span>translateY(&minus;0.03em)</span></p>
          </div>
        </div>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
.mu-04 {
  --mu-04-unit: 0.5rem;
  --mu-04-icon: 1.75rem;
  --mu-04-target: 44px;
  --mu-04-nudge: 0.06em;
  --mu-04-font: ui-rounded, "SF Pro Rounded", "Hiragino Maru Gothic ProN", system-ui, -apple-system, "Segoe UI", sans-serif;
  --mu-04-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
  --mu-04-bg: #08090a;
  --mu-04-bg: oklch(13% 0.004 250);
  --mu-04-surface: #121416;
  --mu-04-surface: oklch(19% 0.005 250);
  --mu-04-ink: #f4f6f7;
  --mu-04-ink: oklch(97% 0.002 250);
  --mu-04-ink-2: #a8b0b6;
  --mu-04-ink-2: oklch(75% 0.008 250);
  --mu-04-line: #2b3034;
  --mu-04-line: oklch(29% 0.007 250);
  --mu-04-guide: #6b747a;
  --mu-04-guide: oklch(56% 0.01 250);
  --mu-04-acc: #6ee7b7;
  --mu-04-acc: oklch(85% 0.13 165);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--mu-04-bg);
  color: var(--mu-04-ink);
  font-family: var(--mu-04-font);
  line-height: 1.5;
  -webkit-text-size-adjust: 100%;
}

.mu-04 *,
.mu-04 *::before,
.mu-04 *::after {
  box-sizing: border-box;
}

@media (prefers-color-scheme: light) {
  .mu-04 {
    --mu-04-bg: #f3f5f6;
    --mu-04-bg: oklch(96% 0.003 250);
    --mu-04-surface: #ffffff;
    --mu-04-surface: oklch(100% 0 0);
    --mu-04-ink: #14171a;
    --mu-04-ink: oklch(19% 0.006 250);
    --mu-04-ink-2: #545c62;
    --mu-04-ink-2: oklch(45% 0.011 250);
    --mu-04-line: #d3d8db;
    --mu-04-line: oklch(86% 0.005 250);
    --mu-04-guide: #8d959a;
    --mu-04-guide: oklch(66% 0.008 250);
    --mu-04-acc: #05704f;
    --mu-04-acc: oklch(45% 0.11 165);
  }
}

.mu-04[data-theme="light"],
.mu-04:has(.mu-04__theme-input:checked) {
  --mu-04-bg: #f3f5f6;
  --mu-04-bg: oklch(96% 0.003 250);
  --mu-04-surface: #ffffff;
  --mu-04-surface: oklch(100% 0 0);
  --mu-04-ink: #14171a;
  --mu-04-ink: oklch(19% 0.006 250);
  --mu-04-ink-2: #545c62;
  --mu-04-ink-2: oklch(45% 0.011 250);
  --mu-04-line: #d3d8db;
  --mu-04-line: oklch(86% 0.005 250);
  --mu-04-guide: #8d959a;
  --mu-04-guide: oklch(66% 0.008 250);
  --mu-04-acc: #05704f;
  --mu-04-acc: oklch(45% 0.11 165);
}

@media (prefers-color-scheme: dark) {
  .mu-04:has(.mu-04__theme-input:checked) {
    --mu-04-bg: #f3f5f6;
    --mu-04-bg: oklch(96% 0.003 250);
    --mu-04-surface: #ffffff;
    --mu-04-surface: oklch(100% 0 0);
    --mu-04-ink: #14171a;
    --mu-04-ink: oklch(19% 0.006 250);
    --mu-04-ink-2: #545c62;
    --mu-04-ink-2: oklch(45% 0.011 250);
    --mu-04-line: #d3d8db;
    --mu-04-line: oklch(86% 0.005 250);
    --mu-04-guide: #8d959a;
    --mu-04-guide: oklch(66% 0.008 250);
    --mu-04-acc: #05704f;
    --mu-04-acc: oklch(45% 0.11 165);
  }
}

@media (prefers-color-scheme: light) {
  .mu-04:has(.mu-04__theme-input:checked) {
    --mu-04-bg: #08090a;
    --mu-04-bg: oklch(13% 0.004 250);
    --mu-04-surface: #121416;
    --mu-04-surface: oklch(19% 0.005 250);
    --mu-04-ink: #f4f6f7;
    --mu-04-ink: oklch(97% 0.002 250);
    --mu-04-ink-2: #a8b0b6;
    --mu-04-ink-2: oklch(75% 0.008 250);
    --mu-04-line: #2b3034;
    --mu-04-line: oklch(29% 0.007 250);
    --mu-04-guide: #6b747a;
    --mu-04-guide: oklch(56% 0.01 250);
    --mu-04-acc: #6ee7b7;
    --mu-04-acc: oklch(85% 0.13 165);
  }
}

.mu-04__sr {
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

.mu-04__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 5;
}

.mu-04__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 44px;
  block-size: 44px;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.mu-04__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--mu-04-line);
  border-radius: 50%;
  background: var(--mu-04-surface);
  color: var(--mu-04-ink-2);
  cursor: pointer;
}

.mu-04__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.mu-04__theme-input:focus-visible + .mu-04__theme-label {
  outline: 2px solid var(--mu-04-acc);
  outline-offset: 2px;
}

.mu-04__stage {
  max-inline-size: 68rem;
  margin-inline: auto;
  padding: calc(var(--mu-04-unit) * 8) calc(var(--mu-04-unit) * 3) calc(var(--mu-04-unit) * 10);
  display: grid;
  gap: calc(var(--mu-04-unit) * 6);
  grid-template-columns: minmax(0, 1fr);
}

.mu-04__grid {
  display: grid;
  gap: calc(var(--mu-04-unit) * 3);
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 18rem), 1fr));
}

.mu-04__case {
  min-inline-size: 0;
  display: grid;
  gap: calc(var(--mu-04-unit) * 2.5);
  align-content: start;
  padding: calc(var(--mu-04-unit) * 3);
  background: var(--mu-04-surface);
  border-radius: 8px;
}

.mu-04__case-title {
  margin: 0;
  font-size: 0.9375rem;
  font-weight: 600;
  letter-spacing: -0.008em;
  min-inline-size: 0;
}

.mu-04__demo {
  display: grid;
  gap: calc(var(--mu-04-unit) * 2);
  grid-template-columns: repeat(2, minmax(0, 1fr));
}

.mu-04__demo--stack {
  grid-template-columns: minmax(0, 1fr);
}

.mu-04__slot {
  min-inline-size: 0;
  display: grid;
  gap: var(--mu-04-unit);
  justify-items: start;
}

.mu-04__slot--wide {
  justify-items: stretch;
}

.mu-04__btn {
  position: relative;
  display: grid;
  place-items: center;
  inline-size: var(--mu-04-target);
  block-size: var(--mu-04-target);
  min-inline-size: var(--mu-04-target);
  min-block-size: var(--mu-04-target);
  border: 1px solid var(--mu-04-line);
  border-radius: 50%;
  background: transparent;
  color: var(--mu-04-ink);
  cursor: pointer;
  padding: 0;
  transition: border-color 160ms ease, color 160ms ease;
}

.mu-04__btn:hover {
  border-color: var(--mu-04-acc);
  color: var(--mu-04-acc);
}

.mu-04__btn:focus-visible {
  outline: 2px solid var(--mu-04-acc);
  outline-offset: 2px;
}

.mu-04__btn--guide::after {
  content: "";
  position: absolute;
  inset-block: 6px;
  inset-inline-start: 50%;
  inline-size: 0;
  border-inline-start: 1px dashed var(--mu-04-guide);
  pointer-events: none;
}

.mu-04__btn--fixed {
  border-color: var(--mu-04-acc);
}

.mu-04__icon {
  inline-size: var(--mu-04-icon);
  block-size: var(--mu-04-icon);
}

.mu-04__icon--nudged {
  translate: var(--mu-04-nudge) 0;
}

.mu-04__label {
  margin: 0;
  font-family: var(--mu-04-mono);
  font-size: 0.6875rem;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--mu-04-ink);
  display: grid;
  gap: 1px;
  min-inline-size: 0;
}

.mu-04__label span {
  text-transform: none;
  letter-spacing: 0;
  color: var(--mu-04-ink-2);
  overflow-wrap: break-word;
}

.mu-04__quote {
  margin: 0;
  padding: calc(var(--mu-04-unit) * 1.5) 0;
  border-block-start: 1px solid var(--mu-04-line);
  min-inline-size: 0;
}

.mu-04__quote p {
  margin: 0;
  font-size: 1.125rem;
  line-height: 1.35;
  letter-spacing: -0.012em;
  text-wrap: pretty;
}

.mu-04__quote p::before {
  content: "\201C";
}

.mu-04__quote p::after {
  content: "\201D";
}

.mu-04__quote--hang p {
  text-indent: -0.42em;
  hanging-punctuation: first;
}

.mu-04__pill {
  display: inline-flex;
  align-items: center;
  gap: calc(var(--mu-04-unit) * 1.25);
  min-block-size: var(--mu-04-target);
  padding-inline: calc(var(--mu-04-unit) * 2);
  border: 1px solid var(--mu-04-line);
  border-radius: 999px;
  font-size: 0.9375rem;
  font-weight: 500;
  min-inline-size: 0;
}

.mu-04__icon-sm {
  inline-size: 18px;
  block-size: 18px;
  flex: none;
}

.mu-04__icon-sm--nudged {
  translate: 0 -0.03em;
}

@media (prefers-reduced-motion: reduce) {
  .mu-04__btn {
    transition: none;
  }
}

@media (min-width: 64rem) {
  .mu-04__stage {
    padding-inline: calc(var(--mu-04-unit) * 6);
  }
}
```
