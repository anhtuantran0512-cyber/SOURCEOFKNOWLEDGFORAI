---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-minimalist-ui/grayscale-palette-with-enough-contrast/"
title: "Grayscale Palette with Enough Contrast"
section: "design-styles"
category: "css-minimalist-ui"
category_name: "CSS Minimalist UI"
description: "A ten-step neutral ramp with the measured contrast ratio printed against every step and a marked cut-off line below which text must not go."
has_js: "false"
---

Here's a working CSS Minimalist UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Grayscale Palette with Enough Contrast
Source: https://codefronts.com/design-styles/css-minimalist-ui/grayscale-palette-with-enough-contrast/

A ten-step neutral ramp with the measured contrast ratio printed against every step and a marked cut-off line below which text must not go. It names the most common minimalist failure directly: light grey secondary text that looks refined at 2.8:1 on a good display and fails WCAG 1.4.3 on a phone in daylight. Build the ramp in oklch(), measure every step, print the number.
## HTML
```html
<section class="mu-10" aria-labelledby="mu-10-title">
  <h2 class="mu-10__sr" id="mu-10-title">Neutral ramp contrast reference</h2>
  <div class="mu-10__theme">
    <input class="mu-10__theme-input" type="checkbox" id="mu-10-theme">
    <label class="mu-10__theme-label" for="mu-10-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="mu-10__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="mu-10__stage">

    <div class="mu-10__ramp" role="table" aria-labelledby="mu-10-ramp-h">
      <p class="mu-10__sr" id="mu-10-ramp-h">Neutral ramp with measured contrast ratios against the active surface</p>
      <div class="mu-10__row mu-10__row--head" role="row">
        <span role="columnheader">Step</span>
        <span role="columnheader">Swatch</span>
        <span role="columnheader">Sample</span>
        <span role="columnheader">Ratio</span>
        <span role="columnheader">Verdict</span>
      </div>

      <div class="mu-10__row" role="row" style="--mu-10-tone: var(--mu-10-t050)">
        <span role="cell"><b>050</b></span>
        <span role="cell"><i class="mu-10__chip"></i></span>
        <span role="cell" class="mu-10__sample">Aa</span>
        <span role="cell" class="mu-10__ratio"><b class="mu-10__num mu-10__num--l">1.07:1</b><b class="mu-10__num mu-10__num--d">16.28:1</b></span>
        <span role="cell"><span class="mu-10__verdict mu-10__verdict--l">Surface only</span><span class="mu-10__verdict mu-10__verdict--d mu-10__verdict--ok">
            <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M5 13l4 4L19 7" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>
            Headings
          </span></span>
      </div>

      <div class="mu-10__row" role="row" style="--mu-10-tone: var(--mu-10-t100)">
        <span role="cell"><b>100</b></span>
        <span role="cell"><i class="mu-10__chip"></i></span>
        <span role="cell" class="mu-10__sample">Aa</span>
        <span role="cell" class="mu-10__ratio"><b class="mu-10__num mu-10__num--l">1.22:1</b><b class="mu-10__num mu-10__num--d">13.49:1</b></span>
        <span role="cell"><span class="mu-10__verdict mu-10__verdict--l">Surface only</span><span class="mu-10__verdict mu-10__verdict--d mu-10__verdict--ok">
            <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M5 13l4 4L19 7" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>
            Primary text
          </span></span>
      </div>

      <div class="mu-10__row" role="row" style="--mu-10-tone: var(--mu-10-t200)">
        <span role="cell"><b>200</b></span>
        <span role="cell"><i class="mu-10__chip"></i></span>
        <span role="cell" class="mu-10__sample">Aa</span>
        <span role="cell" class="mu-10__ratio"><b class="mu-10__num mu-10__num--l">1.51:1</b><b class="mu-10__num mu-10__num--d">10.36:1</b></span>
        <span role="cell"><span class="mu-10__verdict mu-10__verdict--l">Decorative rule</span><span class="mu-10__verdict mu-10__verdict--d mu-10__verdict--ok">
            <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M5 13l4 4L19 7" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>
            Secondary text
          </span></span>
      </div>

      <div class="mu-10__row" role="row" style="--mu-10-tone: var(--mu-10-t300)">
        <span role="cell"><b>300</b></span>
        <span role="cell"><i class="mu-10__chip"></i></span>
        <span role="cell" class="mu-10__sample">Aa</span>
        <span role="cell" class="mu-10__ratio"><b class="mu-10__num mu-10__num--l">2.12:1</b><b class="mu-10__num mu-10__num--d">7.20:1</b></span>
        <span role="cell"><span class="mu-10__verdict mu-10__verdict--l mu-10__verdict--bad">
            <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6 6 18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>
            Fails 1.4.11
          </span><span class="mu-10__verdict mu-10__verdict--d mu-10__verdict--ok">
            <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M5 13l4 4L19 7" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>
            Secondary text
          </span></span>
      </div>

      <div class="mu-10__row mu-10__row--cut-d" role="row" style="--mu-10-tone: var(--mu-10-t400)">
        <span role="cell"><b>400</b></span>
        <span role="cell"><i class="mu-10__chip"></i></span>
        <span role="cell" class="mu-10__sample">Aa</span>
        <span role="cell" class="mu-10__ratio"><b class="mu-10__num mu-10__num--l">2.96:1</b><b class="mu-10__num mu-10__num--d">4.98:1</b></span>
        <span role="cell"><span class="mu-10__verdict mu-10__verdict--l mu-10__verdict--bad">
            <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6 6 18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>
            The classic fail
          </span><span class="mu-10__verdict mu-10__verdict--d mu-10__verdict--ok">
            <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M5 13l4 4L19 7" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>
            Body text floor
          </span></span>
      </div>

      <div class="mu-10__row" role="row" style="--mu-10-tone: var(--mu-10-t500)">
        <span role="cell"><b>500</b></span>
        <span role="cell"><i class="mu-10__chip"></i></span>
        <span role="cell" class="mu-10__sample">Aa</span>
        <span role="cell" class="mu-10__ratio"><b class="mu-10__num mu-10__num--l">4.07:1</b><b class="mu-10__num mu-10__num--d">3.55:1</b></span>
        <span role="cell"><span class="mu-10__verdict mu-10__verdict--l">Large text / borders</span><span class="mu-10__verdict mu-10__verdict--d">Large text / borders</span></span>
      </div>

      <div class="mu-10__row mu-10__row--cut-l" role="row" style="--mu-10-tone: var(--mu-10-t600)">
        <span role="cell"><b>600</b></span>
        <span role="cell"><i class="mu-10__chip"></i></span>
        <span role="cell" class="mu-10__sample">Aa</span>
        <span role="cell" class="mu-10__ratio"><b class="mu-10__num mu-10__num--l">5.85:1</b><b class="mu-10__num mu-10__num--d">2.75:1</b></span>
        <span role="cell"><span class="mu-10__verdict mu-10__verdict--l mu-10__verdict--ok">
            <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M5 13l4 4L19 7" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>
            Body text floor
          </span><span class="mu-10__verdict mu-10__verdict--d mu-10__verdict--bad">
            <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6 6 18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>
            The classic fail
          </span></span>
      </div>

      <div class="mu-10__row" role="row" style="--mu-10-tone: var(--mu-10-t700)">
        <span role="cell"><b>700</b></span>
        <span role="cell"><i class="mu-10__chip"></i></span>
        <span role="cell" class="mu-10__sample">Aa</span>
        <span role="cell" class="mu-10__ratio"><b class="mu-10__num mu-10__num--l">8.60:1</b><b class="mu-10__num mu-10__num--d">1.95:1</b></span>
        <span role="cell"><span class="mu-10__verdict mu-10__verdict--l mu-10__verdict--ok">
            <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M5 13l4 4L19 7" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>
            Secondary text
          </span><span class="mu-10__verdict mu-10__verdict--d mu-10__verdict--bad">
            <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6 6 18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>
            Fails 1.4.11
          </span></span>
      </div>

      <div class="mu-10__row" role="row" style="--mu-10-tone: var(--mu-10-t800)">
        <span role="cell"><b>800</b></span>
        <span role="cell"><i class="mu-10__chip"></i></span>
        <span role="cell" class="mu-10__sample">Aa</span>
        <span role="cell" class="mu-10__ratio"><b class="mu-10__num mu-10__num--l">12.99:1</b><b class="mu-10__num mu-10__num--d">1.42:1</b></span>
        <span role="cell"><span class="mu-10__verdict mu-10__verdict--l mu-10__verdict--ok">
            <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M5 13l4 4L19 7" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>
            Primary text
          </span><span class="mu-10__verdict mu-10__verdict--d">Surface only</span></span>
      </div>

      <div class="mu-10__row" role="row" style="--mu-10-tone: var(--mu-10-t900)">
        <span role="cell"><b>900</b></span>
        <span role="cell"><i class="mu-10__chip"></i></span>
        <span role="cell" class="mu-10__sample">Aa</span>
        <span role="cell" class="mu-10__ratio"><b class="mu-10__num mu-10__num--l">17.65:1</b><b class="mu-10__num mu-10__num--d">1.18:1</b></span>
        <span role="cell"><span class="mu-10__verdict mu-10__verdict--l mu-10__verdict--ok">
            <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M5 13l4 4L19 7" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>
            Headings
          </span><span class="mu-10__verdict mu-10__verdict--d">Surface only</span></span>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.mu-10 {
  --mu-10-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
  --mu-10-ui: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --mu-10-ground: #ffffff;
  --mu-10-ground: oklch(100% 0 0);
  --mu-10-bg: #ffffff;
  --mu-10-bg: oklch(100% 0 0);
  --mu-10-ink: #16191c;
  --mu-10-ink: oklch(20% 0.006 250);
  --mu-10-ink-2: #5d666e;
  --mu-10-ink-2: oklch(48% 0.012 250);
  --mu-10-line: #cfd3d7;
  --mu-10-line: oklch(85.5% 0.005 250);
  --mu-10-ok: #16663d;
  --mu-10-ok: oklch(44% 0.11 155);
  --mu-10-bad: #a32020;
  --mu-10-bad: oklch(45% 0.18 25);
  --mu-10-acc: #16191c;
  --mu-10-acc: oklch(20% 0.006 250);
  --mu-10-t050: #f6f7f8;
  --mu-10-t100: #e7e9eb;
  --mu-10-t200: #cfd3d7;
  --mu-10-t300: #adb3b9;
  --mu-10-t400: #8f979e;
  --mu-10-t500: #767f87;
  --mu-10-t600: #5d666e;
  --mu-10-t700: #454d54;
  --mu-10-t800: #2b3238;
  --mu-10-t900: #16191c;
  --mu-10-d-l: inline-flex;
  --mu-10-d-d: none;
  --mu-10-cut-l: 2px solid var(--mu-10-ink);
  --mu-10-cut-d: 0;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--mu-10-bg);
  color: var(--mu-10-ink);
  font-family: var(--mu-10-ui);
  line-height: 1.5;
  -webkit-text-size-adjust: 100%;
}

.mu-10 *,
.mu-10 *::before,
.mu-10 *::after {
  box-sizing: border-box;
}

@media (prefers-color-scheme: dark) {
  .mu-10 {
    --mu-10-ground: #14171a;
    --mu-10-ground: oklch(19% 0.005 250);
    --mu-10-bg: #14171a;
    --mu-10-bg: oklch(19% 0.005 250);
    --mu-10-ink: #e9ecee;
    --mu-10-ink: oklch(93.5% 0.003 250);
    --mu-10-ink-2: #a1a9b0;
    --mu-10-ink-2: oklch(73% 0.008 250);
    --mu-10-line: #343b41;
    --mu-10-line: oklch(33.5% 0.009 250);
    --mu-10-ok: #62c78f;
    --mu-10-ok: oklch(78% 0.12 155);
    --mu-10-bad: #f08a8a;
    --mu-10-bad: oklch(74% 0.14 25);
    --mu-10-acc: #e9ecee;
    --mu-10-acc: oklch(93.5% 0.003 250);
    --mu-10-t050: #eef1f3;
    --mu-10-t100: #d8dde0;
    --mu-10-t200: #bcc3c8;
    --mu-10-t300: #9aa3aa;
    --mu-10-t400: #7d868d;
    --mu-10-t500: #656e75;
    --mu-10-t600: #545d64;
    --mu-10-t700: #3f474d;
    --mu-10-t800: #2b3238;
    --mu-10-t900: #1e2429;
    --mu-10-d-l: none;
    --mu-10-d-d: inline-flex;
    --mu-10-cut-l: 0;
    --mu-10-cut-d: 2px solid var(--mu-10-ink);
  }
}

.mu-10[data-theme="dark"],
.mu-10:has(.mu-10__theme-input:checked) {
  --mu-10-ground: #14171a;
  --mu-10-ground: oklch(19% 0.005 250);
  --mu-10-bg: #14171a;
  --mu-10-bg: oklch(19% 0.005 250);
  --mu-10-ink: #e9ecee;
  --mu-10-ink: oklch(93.5% 0.003 250);
  --mu-10-ink-2: #a1a9b0;
  --mu-10-ink-2: oklch(73% 0.008 250);
  --mu-10-line: #343b41;
  --mu-10-line: oklch(33.5% 0.009 250);
  --mu-10-ok: #62c78f;
  --mu-10-ok: oklch(78% 0.12 155);
  --mu-10-bad: #f08a8a;
  --mu-10-bad: oklch(74% 0.14 25);
  --mu-10-acc: #e9ecee;
  --mu-10-acc: oklch(93.5% 0.003 250);
  --mu-10-t050: #eef1f3;
  --mu-10-t100: #d8dde0;
  --mu-10-t200: #bcc3c8;
  --mu-10-t300: #9aa3aa;
  --mu-10-t400: #7d868d;
  --mu-10-t500: #656e75;
  --mu-10-t600: #545d64;
  --mu-10-t700: #3f474d;
  --mu-10-t800: #2b3238;
  --mu-10-t900: #1e2429;
  --mu-10-d-l: none;
  --mu-10-d-d: inline-flex;
  --mu-10-cut-l: 0;
  --mu-10-cut-d: 2px solid var(--mu-10-ink);
}

@media (prefers-color-scheme: light) {
  .mu-10:has(.mu-10__theme-input:checked) {
    --mu-10-ground: #14171a;
    --mu-10-ground: oklch(19% 0.005 250);
    --mu-10-bg: #14171a;
    --mu-10-bg: oklch(19% 0.005 250);
    --mu-10-ink: #e9ecee;
    --mu-10-ink: oklch(93.5% 0.003 250);
    --mu-10-ink-2: #a1a9b0;
    --mu-10-ink-2: oklch(73% 0.008 250);
    --mu-10-line: #343b41;
    --mu-10-line: oklch(33.5% 0.009 250);
    --mu-10-ok: #62c78f;
    --mu-10-ok: oklch(78% 0.12 155);
    --mu-10-bad: #f08a8a;
    --mu-10-bad: oklch(74% 0.14 25);
    --mu-10-acc: #e9ecee;
    --mu-10-acc: oklch(93.5% 0.003 250);
    --mu-10-t050: #eef1f3;
    --mu-10-t100: #d8dde0;
    --mu-10-t200: #bcc3c8;
    --mu-10-t300: #9aa3aa;
    --mu-10-t400: #7d868d;
    --mu-10-t500: #656e75;
    --mu-10-t600: #545d64;
    --mu-10-t700: #3f474d;
    --mu-10-t800: #2b3238;
    --mu-10-t900: #1e2429;
    --mu-10-d-l: none;
    --mu-10-d-d: inline-flex;
    --mu-10-cut-l: 0;
    --mu-10-cut-d: 2px solid var(--mu-10-ink);
  }
}

@media (prefers-color-scheme: dark) {
  .mu-10:has(.mu-10__theme-input:checked) {
    --mu-10-ground: #ffffff;
    --mu-10-ground: oklch(100% 0 0);
    --mu-10-bg: #ffffff;
    --mu-10-bg: oklch(100% 0 0);
    --mu-10-ink: #16191c;
    --mu-10-ink: oklch(20% 0.006 250);
    --mu-10-ink-2: #5d666e;
    --mu-10-ink-2: oklch(48% 0.012 250);
    --mu-10-line: #cfd3d7;
    --mu-10-line: oklch(85.5% 0.005 250);
    --mu-10-ok: #16663d;
    --mu-10-ok: oklch(44% 0.11 155);
    --mu-10-bad: #a32020;
    --mu-10-bad: oklch(45% 0.18 25);
    --mu-10-acc: #16191c;
    --mu-10-acc: oklch(20% 0.006 250);
    --mu-10-t050: #f6f7f8;
    --mu-10-t100: #e7e9eb;
    --mu-10-t200: #cfd3d7;
    --mu-10-t300: #adb3b9;
    --mu-10-t400: #8f979e;
    --mu-10-t500: #767f87;
    --mu-10-t600: #5d666e;
    --mu-10-t700: #454d54;
    --mu-10-t800: #2b3238;
    --mu-10-t900: #16191c;
    --mu-10-d-l: inline-flex;
    --mu-10-d-d: none;
    --mu-10-cut-l: 2px solid var(--mu-10-ink);
    --mu-10-cut-d: 0;
  }
}

.mu-10__sr {
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

.mu-10__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 5;
}

.mu-10__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 44px;
  block-size: 44px;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.mu-10__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--mu-10-line);
  border-radius: 2px;
  background: var(--mu-10-bg);
  color: var(--mu-10-ink-2);
  cursor: pointer;
}

.mu-10__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.mu-10__theme-input:focus-visible + .mu-10__theme-label {
  outline: 2px solid var(--mu-10-acc);
  outline-offset: 2px;
}

.mu-10__stage {
  max-inline-size: 64rem;
  margin-inline: auto;
  padding: 4rem 1.25rem 5rem;
  display: grid;
  gap: 2.5rem;
  grid-template-columns: minmax(0, 1fr);
}

.mu-10__ramp {
  min-inline-size: 0;
  display: grid;
  gap: 0;
  border-block-start: 1px solid var(--mu-10-line);
}

.mu-10__row {
  display: grid;
  align-items: center;
  gap: 0.5rem 0.75rem;
  grid-template-columns: 2.75rem 3rem minmax(0, 1fr) 4.25rem;
  padding-block: 0.6875rem;
  border-block-end: 1px solid var(--mu-10-line);
  font-size: 0.8125rem;
  min-inline-size: 0;
}

.mu-10__row > span {
  min-inline-size: 0;
}

.mu-10__row > span:nth-child(5) {
  grid-column: 3 / -1;
}

.mu-10__row--head {
  font-family: var(--mu-10-mono);
  font-size: 0.6875rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--mu-10-ink-2);
}

.mu-10__row--head > span:nth-child(5) {
  grid-column: 3 / -1;
}

.mu-10__row b {
  font-family: var(--mu-10-mono);
  font-weight: 500;
  font-variant-numeric: tabular-nums;
}

.mu-10__chip {
  display: block;
  inline-size: 100%;
  block-size: 26px;
  border-radius: 2px;
  background: var(--mu-10-tone);
  border: 1px solid var(--mu-10-line);
}

.mu-10__sample {
  font-size: 1.125rem;
  font-weight: 500;
  color: var(--mu-10-tone);
  letter-spacing: -0.01em;
}

.mu-10__ratio {
  font-family: var(--mu-10-mono);
  font-variant-numeric: tabular-nums;
  text-align: end;
  color: var(--mu-10-ink);
}

.mu-10__num {
  font-weight: 500;
}

.mu-10__num--l {
  display: var(--mu-10-d-l);
}

.mu-10__num--d {
  display: var(--mu-10-d-d);
}

.mu-10__verdict--l {
  display: var(--mu-10-d-l);
}

.mu-10__verdict--d {
  display: var(--mu-10-d-d);
}

.mu-10__verdict {
  align-items: center;
  gap: 0.375rem;
  font-size: 0.75rem;
  color: var(--mu-10-ink-2);
  min-inline-size: 0;
}

.mu-10__verdict svg {
  inline-size: 14px;
  block-size: 14px;
  flex: none;
}

.mu-10__verdict--ok {
  color: var(--mu-10-ok);
  font-weight: 600;
}

.mu-10__verdict--bad {
  color: var(--mu-10-bad);
  font-weight: 600;
}

.mu-10__row--cut-l {
  border-block-start: var(--mu-10-cut-l);
}

.mu-10__row--cut-d {
  border-block-start: var(--mu-10-cut-d);
}

@media (min-width: 40rem) {
  .mu-10__row {
    grid-template-columns: 3rem 4rem minmax(0, 1fr) 5rem minmax(0, 11rem);
  }

  .mu-10__row > span:nth-child(5),
    .mu-10__row--head > span:nth-child(5) {
    grid-column: auto;
    justify-self: end;
  }

  .mu-10__ratio {
    text-align: end;
  }
}

@media (min-width: 56rem) {
  .mu-10__stage {
    padding-inline: 3rem;
  }
}
```
