---
source: "codefronts"
url: "https://codefronts.com/components/css-loading-buttons/gradient-border-trace-loading-button/"
title: "Gradient Border Trace Loading Button"
section: "components"
category: "css-loading-buttons"
category_name: "CSS Loading Buttons"
description: "A conic gradient border that rotates while the request is pending and stops when it resolves, so the motion itself signals state rather than decorating the…"
has_js: "false"
---

Here's a working CSS Loading Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Gradient Border Trace Loading Button
Source: https://codefronts.com/components/css-loading-buttons/gradient-border-trace-loading-button/

A conic gradient border that rotates while the request is pending and stops when it resolves, so the motion itself signals state rather than decorating the button. The angle is a registered custom property, which is the only way it can animate — an unregistered one silently does nothing, and that is the single most common reason this effect appears broken.
## HTML
```html
<div class="lb-19">
  <div class="lb-19__stage">
    <section class="lb-19__card" aria-labelledby="lb-19-h">
      <p class="lb-19__plan">Pro workspace</p>
      <h2 class="lb-19__h" id="lb-19-h">$24 <span class="lb-19__per">per editor / month</span></h2>
      <ul class="lb-19__feats">
        <li>Unlimited version history</li>
        <li>Shared component libraries</li>
        <li>SAML and SCIM provisioning</li>
      </ul>

      <button class="lb-19__btn" type="button" data-state="idle" aria-busy="false">
        <span class="lb-19__faces">
          <span class="lb-19__face lb-19__face--idle">Upgrade workspace</span>
          <span class="lb-19__face lb-19__face--pending">Provisioning</span>
          <span class="lb-19__face lb-19__face--done">Workspace upgraded</span>
          <span class="lb-19__face lb-19__face--error">Payment failed, retry</span>
        </span>
      </button>

      <fieldset class="lb-19__states">
        <legend class="lb-19__legend">Request state</legend>
        <label class="lb-19__radio"><input type="radio" name="lb-19-state" value="idle" checked> Idle</label>
        <label class="lb-19__radio"><input type="radio" name="lb-19-state" value="pending" class="lb-19__is-pending"> Pending</label>
        <label class="lb-19__radio"><input type="radio" name="lb-19-state" value="done" class="lb-19__is-done"> Done</label>
        <label class="lb-19__radio"><input type="radio" name="lb-19-state" value="error" class="lb-19__is-error"> Failed</label>
      </fieldset>
    </section>
  </div>
</div>
```
## CSS
```css
@property --lb-19-angle {
  syntax: "<angle>";
  inherits: false;
  initial-value: 0deg;
}

.lb-19 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --bg: #08080b;
  --surface: #101017;
  --ink: #f0eef7;
  --muted: #8b889c;
  --rule: #23222c;
  --accent: #6f5cff;
  --hot: #c9c2ff;
  --ok: #3ecf8e;
  --bad: #ff7a66;
  font-family: ui-sans-serif, system-ui, "Segoe UI", sans-serif;
  background: var(--bg);
  color: var(--ink);
  padding: 40px 16px;
}

.lb-19 *,
.lb-19 *::before,
.lb-19 *::after {
  box-sizing: border-box;
}

.lb-19__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  min-height: calc(100vh - 80px);
}

.lb-19__card {
  inline-size: 100%;
  max-inline-size: 25rem;
  min-inline-size: 0;
  background: var(--surface);
  border: 1px solid var(--rule);
  border-radius: 18px;
  padding: 26px 24px;
}

.lb-19__plan {
  margin: 0;
  font-size: 10.5px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--accent);
  font-weight: 700;
}

.lb-19__h {
  margin: 10px 0 0;
  font-size: 30px;
  font-weight: 600;
  letter-spacing: -.03em;
}

.lb-19__per {
  font-size: 12.5px;
  font-weight: 400;
  color: var(--muted);
  letter-spacing: 0;
}

.lb-19__feats {
  list-style: none;
  margin: 18px 0 22px;
  padding: 0;
  display: grid;
  gap: 9px;
  font-size: 13px;
  color: var(--muted);
}

.lb-19__feats li {
  padding-inline-start: 18px;
  position: relative;
  min-inline-size: 0;
}

.lb-19__feats li::before {
  content: "";
  position: absolute;
  inset-inline-start: 0;
  inset-block-start: 7px;
  inline-size: 6px;
  block-size: 6px;
  border-radius: 50%;
  background: var(--accent);
}

.lb-19__btn {
  appearance: none;
  inline-size: 100%;
  border: 2px solid var(--accent);
  background: var(--surface);
  color: var(--ink);
  border-radius: 999px;
  font: inherit;
  font-size: 14px;
  font-weight: 620;
  padding: 0 20px;
  min-block-size: 50px;
  min-inline-size: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
}

.lb-19__btn:focus-visible {
  outline: 3px solid var(--hot);
  outline-offset: 3px;
}

@supports (background: conic-gradient(red, blue)) {
  .lb-19__btn {
    border-color: transparent;
    background: linear-gradient(var(--surface), var(--surface)) padding-box, conic-gradient(from var(--lb-19-angle), var(--rule) 0 62%, var(--accent) 78%, var(--hot) 88%, var(--rule) 96%) border-box;
  }
}

.lb-19:has(.lb-19__is-pending:checked) .lb-19__btn {
  animation: lb-19-turn 1.4s linear infinite;
  cursor: progress;
}

@keyframes lb-19-turn {
  to {
    --lb-19-angle: 360deg;
  }
}

.lb-19:has(.lb-19__is-done:checked) .lb-19__btn {
  background: linear-gradient(var(--surface), var(--surface)) padding-box, linear-gradient(var(--ok), var(--ok)) border-box;
}

.lb-19:has(.lb-19__is-error:checked) .lb-19__btn {
  background: linear-gradient(var(--surface), var(--surface)) padding-box, linear-gradient(var(--bad), var(--bad)) border-box;
}

.lb-19__faces {
  display: grid;
  place-items: center;
  min-inline-size: 0;
}

.lb-19__face {
  grid-area: 1 / 1;
  white-space: nowrap;
  visibility: hidden;
}

.lb-19__face--idle {
  visibility: visible;
}

.lb-19:has(.lb-19__is-pending:checked) .lb-19__face--idle,
.lb-19:has(.lb-19__is-done:checked) .lb-19__face--idle,
.lb-19:has(.lb-19__is-error:checked) .lb-19__face--idle {
  visibility: hidden;
}

.lb-19:has(.lb-19__is-pending:checked) .lb-19__face--pending,
.lb-19:has(.lb-19__is-done:checked) .lb-19__face--done,
.lb-19:has(.lb-19__is-error:checked) .lb-19__face--error {
  visibility: visible;
}

.lb-19:has(.lb-19__is-done:checked) .lb-19__btn {
  color: var(--ok);
}

.lb-19:has(.lb-19__is-error:checked) .lb-19__btn {
  color: var(--bad);
}

.lb-19__states {
  margin: 18px 0 0;
  border: 0;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 2px 14px;
  min-inline-size: 0;
}

.lb-19__legend {
  padding: 0;
  font-size: 10.5px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
}

.lb-19__radio {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  font-size: 12px;
  color: var(--muted);
  min-height: 44px;
  cursor: pointer;
}

.lb-19__radio input {
  accent-color: var(--accent);
  inline-size: 15px;
  block-size: 15px;
}

.lb-19__radio input:focus-visible {
  outline: 3px solid var(--hot);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .lb-19:has(.lb-19__is-pending:checked) .lb-19__btn {
    animation: none;
    background: linear-gradient(var(--surface), var(--surface)) padding-box, conic-gradient(from 220deg, var(--rule) 0 62%, var(--accent) 78%, var(--hot) 88%, var(--rule) 96%) border-box;
  }
}

@media (prefers-color-scheme: light) {
  .lb-19 {
    --bg: #f4f3f8;
    --surface: #ffffff;
    --ink: #17151f;
    --muted: #6a6779;
    --rule: #e2e0ea;
    --accent: #5a45f0;
    --hot: #2d1a9e;
    --ok: #16794f;
    --bad: #b4402c;
  }
}

[data-theme="light"] .lb-19 {
  --bg: #f4f3f8;
  --surface: #ffffff;
  --ink: #17151f;
  --muted: #6a6779;
  --rule: #e2e0ea;
  --accent: #5a45f0;
  --hot: #2d1a9e;
  --ok: #16794f;
  --bad: #b4402c;
}
```
