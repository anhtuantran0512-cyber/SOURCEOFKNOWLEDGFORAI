---
source: "codefronts"
url: "https://codefronts.com/components/css-loading-buttons/dark-mode-tokenized-loading-button/"
title: "Dark Mode Tokenized Loading Button"
section: "components"
category: "css-loading-buttons"
category_name: "CSS Loading Buttons"
description: "Every state colour — idle, pending, success, error — declared as a custom property, so rethemeing the whole state machine is a token swap rather than a rewrite."
has_js: "false"
---

Here's a working CSS Loading Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dark Mode Tokenized Loading Button
Source: https://codefronts.com/components/css-loading-buttons/dark-mode-tokenized-loading-button/

Every state colour — idle, pending, success, error — declared as a custom property, so rethemeing the whole state machine is a token swap rather than a rewrite. The light and dark switch inside the demo is native CSS with no script: a visually hidden checkbox and :has() rewrite the tokens on the demo root.
## HTML
```html
<div class="lb-20">
  <div class="lb-20__stage">
    <section class="lb-20__panel" aria-labelledby="lb-20-h">
      <div class="lb-20__head">
        <div class="lb-20__titles">
          <h2 class="lb-20__h" id="lb-20-h">Appearance</h2>
          <p class="lb-20__sub">Every state colour is a token on this panel's root.</p>
        </div>
        <div class="lb-20__switchwrap">
          <input class="lb-20__switch" type="checkbox" id="lb-20-switch">
          <label class="lb-20__switchlab" for="lb-20-switch">
            <span class="lb-20__switchtrack" aria-hidden="true"></span>
            <span class="lb-20__switchtext">Flip theme</span>
          </label>
        </div>
      </div>

      <button class="lb-20__btn" type="button" data-state="idle" aria-busy="false">
        <span class="lb-20__spin" aria-hidden="true"></span>
        <span class="lb-20__faces">
          <span class="lb-20__face lb-20__face--idle">Deploy to production</span>
          <span class="lb-20__face lb-20__face--pending">Deploying</span>
          <span class="lb-20__face lb-20__face--done">Deployed</span>
          <span class="lb-20__face lb-20__face--error">Deploy failed, retry</span>
        </span>
      </button>

      <fieldset class="lb-20__states">
        <legend class="lb-20__legend">State</legend>
        <label class="lb-20__radio"><input type="radio" name="lb-20-state" value="idle" checked> Idle</label>
        <label class="lb-20__radio"><input type="radio" name="lb-20-state" value="pending" class="lb-20__is-pending"> Pending</label>
        <label class="lb-20__radio"><input type="radio" name="lb-20-state" value="done" class="lb-20__is-done"> Done</label>
        <label class="lb-20__radio"><input type="radio" name="lb-20-state" value="error" class="lb-20__is-error"> Failed</label>
      </fieldset>

      <dl class="lb-20__tokens">
        <div class="lb-20__tok"><dt>--idle-bg</dt><dd><span class="lb-20__chip lb-20__chip--idle"></span></dd></div>
        <div class="lb-20__tok"><dt>--pending-bg</dt><dd><span class="lb-20__chip lb-20__chip--pending"></span></dd></div>
        <div class="lb-20__tok"><dt>--done-bg</dt><dd><span class="lb-20__chip lb-20__chip--done"></span></dd></div>
        <div class="lb-20__tok"><dt>--error-bg</dt><dd><span class="lb-20__chip lb-20__chip--error"></span></dd></div>
      </dl>
    </section>
  </div>
</div>
```
## CSS
```css
.lb-20 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --bg: #0e1013;
  --surface: #16191e;
  --ink: #eef1f5;
  --muted: #8f98a4;
  --rule: #262b33;
  --idle-bg: #7c6cff;
  --idle-ink: #0b0a14;
  --pending-bg: #2a3140;
  --pending-ink: #cdd6e2;
  --done-bg: #2ec98a;
  --done-ink: #05130d;
  --error-bg: #ff7a66;
  --error-ink: #1a0805;
  --radius: 16px;
  font-family: ui-sans-serif, system-ui, "Segoe UI", sans-serif;
  background: var(--bg);
  color: var(--ink);
  padding: 40px 16px;
}

.lb-20 *,
.lb-20 *::before,
.lb-20 *::after {
  box-sizing: border-box;
}

.lb-20:has(.lb-20__switch:checked) {
  --bg: #f4f5f7;
  --surface: #ffffff;
  --ink: #14171c;
  --muted: #626b77;
  --rule: #e2e5ea;
  --idle-bg: #4a37d8;
  --idle-ink: #f6f5ff;
  --pending-bg: #e6e9ee;
  --pending-ink: #3b4453;
  --done-bg: #14804f;
  --done-ink: #f2fdf7;
  --error-bg: #b6371f;
  --error-ink: #fff5f2;
}

.lb-20__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  min-height: calc(100vh - 80px);
}

.lb-20__panel {
  inline-size: 100%;
  max-inline-size: 31rem;
  min-inline-size: 0;
  background: var(--surface);
  border: 1px solid var(--rule);
  border-radius: 20px;
  padding: 24px 22px;
}

.lb-20__head {
  display: flex;
  flex-wrap: wrap;
  gap: 14px;
  align-items: flex-start;
  justify-content: space-between;
  min-inline-size: 0;
}

.lb-20__titles {
  min-inline-size: 0;
}

.lb-20__h {
  margin: 0;
  font-size: 19px;
  font-weight: 640;
  letter-spacing: -.015em;
}

.lb-20__sub {
  margin: 6px 0 0;
  font-size: 12.5px;
  color: var(--muted);
  min-inline-size: 0;
}

.lb-20__switchwrap {
  flex: none;
}

.lb-20__switch {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  clip-path: inset(50%);
  overflow: hidden;
  white-space: nowrap;
}

.lb-20__switchlab {
  display: inline-flex;
  align-items: center;
  gap: 9px;
  min-height: 44px;
  font-size: 12px;
  color: var(--muted);
  cursor: pointer;
  border-radius: 999px;
  padding-inline: 4px;
}

.lb-20__switch:focus-visible + .lb-20__switchlab {
  outline: 3px solid var(--idle-bg);
  outline-offset: 2px;
}

.lb-20__switchtrack {
  position: relative;
  inline-size: 40px;
  block-size: 22px;
  border-radius: 999px;
  background: var(--rule);
  flex: none;
  transition: background 160ms ease;
}

.lb-20__switchtrack::after {
  content: "";
  position: absolute;
  inset-block-start: 3px;
  inset-inline-start: 3px;
  inline-size: 16px;
  block-size: 16px;
  border-radius: 50%;
  background: var(--ink);
  transition: transform 160ms ease;
}

.lb-20:has(.lb-20__switch:checked) .lb-20__switchtrack {
  background: var(--idle-bg);
}

.lb-20:has(.lb-20__switch:checked) .lb-20__switchtrack::after {
  transform: translateX(18px);
  background: var(--idle-ink);
}

.lb-20__switchtext {
  min-inline-size: 0;
}

.lb-20__btn {
  appearance: none;
  inline-size: 100%;
  border: 0;
  background: var(--idle-bg);
  color: var(--idle-ink);
  border-radius: var(--radius);
  font: inherit;
  font-size: 14px;
  font-weight: 620;
  padding: 0 20px;
  min-block-size: 50px;
  min-inline-size: 0;
  margin-block-start: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  cursor: pointer;
  transition: background 180ms ease, color 180ms ease;
}

.lb-20__btn:focus-visible {
  outline: 3px solid var(--idle-bg);
  outline-offset: 3px;
}

.lb-20:has(.lb-20__is-pending:checked) .lb-20__btn {
  background: var(--pending-bg);
  color: var(--pending-ink);
  cursor: progress;
}

.lb-20:has(.lb-20__is-done:checked) .lb-20__btn {
  background: var(--done-bg);
  color: var(--done-ink);
}

.lb-20:has(.lb-20__is-error:checked) .lb-20__btn {
  background: var(--error-bg);
  color: var(--error-ink);
}

.lb-20__spin {
  inline-size: 0;
  block-size: 16px;
  border-radius: 50%;
  border: 2px solid currentColor;
  border-inline-start-color: transparent;
  opacity: 0;
}

.lb-20:has(.lb-20__is-pending:checked) .lb-20__spin {
  inline-size: 16px;
  opacity: 1;
  animation: lb-20-spin 720ms linear infinite;
}

@keyframes lb-20-spin {
  to {
    transform: rotate(1turn);
  }
}

.lb-20__faces {
  display: grid;
  place-items: center;
  min-inline-size: 0;
}

.lb-20__face {
  grid-area: 1 / 1;
  white-space: nowrap;
  visibility: hidden;
}

.lb-20__face--idle {
  visibility: visible;
}

.lb-20:has(.lb-20__is-pending:checked) .lb-20__face--idle,
.lb-20:has(.lb-20__is-done:checked) .lb-20__face--idle,
.lb-20:has(.lb-20__is-error:checked) .lb-20__face--idle {
  visibility: hidden;
}

.lb-20:has(.lb-20__is-pending:checked) .lb-20__face--pending,
.lb-20:has(.lb-20__is-done:checked) .lb-20__face--done,
.lb-20:has(.lb-20__is-error:checked) .lb-20__face--error {
  visibility: visible;
}

.lb-20__states {
  margin: 16px 0 0;
  border: 0;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 2px 14px;
  min-inline-size: 0;
}

.lb-20__legend {
  padding: 0;
  font-size: 10.5px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
}

.lb-20__radio {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  font-size: 12px;
  color: var(--muted);
  min-height: 44px;
  cursor: pointer;
}

.lb-20__radio input {
  accent-color: var(--idle-bg);
  inline-size: 15px;
  block-size: 15px;
}

.lb-20__radio input:focus-visible {
  outline: 3px solid var(--idle-bg);
  outline-offset: 3px;
}

.lb-20__tokens {
  margin: 12px 0 0;
  display: grid;
  gap: 8px;
  grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
  border-block-start: 1px solid var(--rule);
  padding-block-start: 14px;
}

.lb-20__tok {
  display: flex;
  align-items: center;
  gap: 8px;
  min-inline-size: 0;
}

.lb-20__tok dt {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 11px;
  color: var(--muted);
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
}

.lb-20__tok dd {
  margin: 0;
  flex: none;
}

.lb-20__chip {
  display: block;
  inline-size: 22px;
  block-size: 14px;
  border-radius: 4px;
  border: 1px solid var(--rule);
}

.lb-20__chip--idle {
  background: var(--idle-bg);
}

.lb-20__chip--pending {
  background: var(--pending-bg);
}

.lb-20__chip--done {
  background: var(--done-bg);
}

.lb-20__chip--error {
  background: var(--error-bg);
}

@media (prefers-reduced-motion: reduce) {
  .lb-20__btn,
    .lb-20__switchtrack,
    .lb-20__switchtrack::after {
    transition: none;
  }

  .lb-20:has(.lb-20__is-pending:checked) .lb-20__spin {
    animation: none;
    border-inline-start-color: currentColor;
    opacity: .6;
  }
}

@media (prefers-color-scheme: light) {
  .lb-20:not(:has(.lb-20__switch:checked)) {
    --bg: #f4f5f7;
    --surface: #ffffff;
    --ink: #14171c;
    --muted: #626b77;
    --rule: #e2e5ea;
    --idle-bg: #4a37d8;
    --idle-ink: #f6f5ff;
    --pending-bg: #e6e9ee;
    --pending-ink: #3b4453;
    --done-bg: #14804f;
    --done-ink: #f2fdf7;
    --error-bg: #b6371f;
    --error-ink: #fff5f2;
  }

  .lb-20:has(.lb-20__switch:checked) {
    --bg: #0e1013;
    --surface: #16191e;
    --ink: #eef1f5;
    --muted: #8f98a4;
    --rule: #262b33;
    --idle-bg: #7c6cff;
    --idle-ink: #0b0a14;
    --pending-bg: #2a3140;
    --pending-ink: #cdd6e2;
    --done-bg: #2ec98a;
    --done-ink: #05130d;
    --error-bg: #ff7a66;
    --error-ink: #1a0805;
  }
}
```
