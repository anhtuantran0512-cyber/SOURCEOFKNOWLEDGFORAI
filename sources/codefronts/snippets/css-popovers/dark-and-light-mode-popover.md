---
source: "codefronts"
url: "https://codefronts.com/snippets/css-popovers/dark-and-light-mode-popover/"
title: "Dark and Light Mode Popover"
section: "snippets"
category: "css-popovers"
category_name: "CSS Popovers"
description: "One token set on the root, two palettes, and a switch that is pure CSS: a visually hidden checkbox read with :has() rewrites the custom properties for the…"
has_js: "false"
---

Here's a working CSS Popover from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dark and Light Mode Popover
Source: https://codefronts.com/snippets/css-popovers/dark-and-light-mode-popover/

One token set on the root, two palettes, and a switch that is pure CSS: a visually hidden checkbox read with :has() rewrites the custom properties for the whole demo, panel included. Because the popover reads the same tokens as the page, the panel never ends up light while its surroundings went dark.
## HTML
```html
<div class="pop-19">
  <div class="pop-19__stage">
    <div class="pop-19__card">
      <div class="pop-19__top">
        <p class="pop-19__kicker">Appearance</p>
        <div class="pop-19__toggle">
          <input class="pop-19__switch" type="checkbox" id="pop-19-switch">
          <label class="pop-19__switchlabel" for="pop-19-switch">
            <span class="pop-19__track" aria-hidden="true"><span class="pop-19__knob"></span></span>
            <span class="pop-19__base">Light</span><span class="pop-19__flip">Dark</span>
          </label>
        </div>
      </div>
      <h2 class="pop-19__h">One token set, two palettes</h2>
      <p class="pop-19__p">The panel is in the top layer and still inherits these tokens, so it cannot drift out of sync with the page.</p>
      <button class="pop-19__btn" type="button" popovertarget="pop-19-panel">Open themed panel</button>
      <dl class="pop-19__tokens">
        <div class="pop-19__trow"><dt class="pop-19__dt">--page</dt><dd class="pop-19__dd">page background</dd></div>
        <div class="pop-19__trow"><dt class="pop-19__dt">--panel</dt><dd class="pop-19__dd">floating surface</dd></div>
        <div class="pop-19__trow"><dt class="pop-19__dt">--ink</dt><dd class="pop-19__dd">body text</dd></div>
      </dl>
    </div>
  </div>

  <div class="pop-19__panel" popover="auto" id="pop-19-panel" role="group" aria-label="Themed panel">
    <p class="pop-19__ptitle">Themed panel</p>
    <p class="pop-19__pline">Flip the switch with me open. Both surfaces change in the same frame because they read the same properties.</p>
    <p class="pop-19__ptag">zero JavaScript</p>
  </div>
</div>
```
## CSS
```css
.pop-19 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --page: #f7f7f8;
  --panel: #ffffff;
  --ink: #17181c;
  --muted: #6b6d75;
  --rule: #dfe0e4;
  --accent: #2f5fd0;
  --font-ui: ui-sans-serif, system-ui, "Segoe UI", sans-serif;
  --font-mono: ui-monospace, "SFMono-Regular", Menlo, monospace;
  background: var(--page);
  color: var(--ink);
  font-family: var(--font-ui);
  padding: 38px 18px;
}

.pop-19__stage {
  display: grid;
  place-items: center;
  max-inline-size: 100%;
  min-height: calc(100vh - 76px);
}

.pop-19__card {
  inline-size: 100%;
  max-inline-size: 27rem;
  min-inline-size: 0;
  background: var(--panel);
  border: 1px solid var(--rule);
  border-radius: 12px;
  padding: 18px;
}

.pop-19__top {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 14px;
}

.pop-19__kicker {
  margin: 0;
  font: 700 10px/1 var(--font-ui);
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--muted);
}

.pop-19__toggle {
  display: flex;
  position: relative;
}

.pop-19__switch {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  pointer-events: none;
}

.pop-19__switchlabel {
  display: inline-flex;
  align-items: center;
  gap: 9px;
  min-block-size: 44px;
  padding: 0 12px;
  box-sizing: border-box;
  font: 700 11px/1 var(--font-ui);
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--ink);
  border: 1px solid var(--rule);
  border-radius: 999px;
  cursor: pointer;
  user-select: none;
}

.pop-19__track {
  position: relative;
  inline-size: 28px;
  block-size: 16px;
  border-radius: 999px;
  background: var(--rule);
  flex: none;
}

.pop-19__knob {
  position: absolute;
  inset-block-start: 2px;
  inset-inline-start: 2px;
  inline-size: 12px;
  block-size: 12px;
  border-radius: 50%;
  background: var(--ink);
  transition: translate 140ms ease;
}

.pop-19__switch:focus-visible + .pop-19__switchlabel {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

.pop-19__flip {
  display: none;
}

.pop-19__h {
  margin: 0 0 10px;
  font: 600 clamp(19px, 4.4vw, 24px)/1.2 var(--font-ui);
  letter-spacing: -0.02em;
}

.pop-19__p {
  margin: 0 0 16px;
  font-size: 13.5px;
  line-height: 1.65;
  color: var(--muted);
  text-wrap: pretty;
}

.pop-19__btn {
  min-height: 44px;
  padding: 0 15px;
  font: 650 13px/1 var(--font-ui);
  color: var(--panel);
  background: var(--accent);
  border: 0;
  border-radius: 9px;
  cursor: pointer;
  anchor-name: --pop-19-anchor;
}

.pop-19__btn:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

.pop-19__tokens {
  margin: 18px 0 0;
  padding-block-start: 14px;
  border-block-start: 1px solid var(--rule);
  display: grid;
  gap: 8px;
}

.pop-19__trow {
  display: flex;
  justify-content: space-between;
  gap: 12px;
  min-inline-size: 0;
}

.pop-19__dt {
  margin: 0;
  font: 600 11.5px/1.3 var(--font-mono);
  color: var(--accent);
}

.pop-19__dd {
  margin: 0;
  font-size: 12px;
  color: var(--muted);
}

.pop-19__panel {
  position: fixed;
  margin: 0;
  inline-size: min(18rem, calc(100vw - 28px));
  max-inline-size: calc(100vw - 28px);
  padding: 16px;
  color: var(--ink);
  background: var(--panel);
  border: 1px solid var(--rule);
  border-radius: 12px;
  box-shadow: 0 20px 40px -24px rgba(0, 0, 0, 0.45);
}

@supports (anchor-name: --a) {
  .pop-19__panel {
    position-anchor: --pop-19-anchor;
    position-area: block-end span-inline-end;
    inset: auto;
    margin-block-start: 9px;
    position-try-fallbacks: flip-block;
  }
}

.pop-19__ptitle {
  margin: 0 0 8px;
  font: 700 10.5px/1 var(--font-ui);
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--muted);
}

.pop-19__pline {
  margin: 0 0 12px;
  font-size: 13px;
  line-height: 1.6;
}

.pop-19__ptag {
  margin: 0;
  padding-block-start: 10px;
  border-block-start: 1px solid var(--rule);
  font: 650 11px/1 var(--font-mono);
  color: var(--accent);
}

@media (prefers-reduced-motion: reduce) {
  .pop-19__knob {
    transition: none;
  }
}
/* The switch owns the theme. Checked = dark. */

.pop-19:has(.pop-19__switch:checked) {
  --page: #101116;
  --panel: #191b21;
  --ink: #eceef3;
  --muted: #8f939e;
  --rule: #292c34;
  --accent: #7fa5f5;
}

.pop-19:has(.pop-19__switch:checked) .pop-19__base {
  display: none;
}

.pop-19:has(.pop-19__switch:checked) .pop-19__flip {
  display: inline;
}

.pop-19:has(.pop-19__switch:checked) .pop-19__knob {
  translate: 12px 0;
}

.pop-19:has(.pop-19__switch:checked) .pop-19__btn {
  color: #101116;
}
/* Flip-back: on a dark OS default the unchecked state is dark, and checking
   returns the light palette — so the switch always does something. */

@media (prefers-color-scheme: dark) {
  .pop-19 {
    --page: #101116;
    --panel: #191b21;
    --ink: #eceef3;
    --muted: #8f939e;
    --rule: #292c34;
    --accent: #7fa5f5;
  }

  .pop-19__btn {
    color: #101116;
  }

  .pop-19__base {
    display: none;
  }

  .pop-19__flip {
    display: inline;
  }

  .pop-19:has(.pop-19__switch:checked) {
    --page: #f7f7f8;
    --panel: #ffffff;
    --ink: #17181c;
    --muted: #6b6d75;
    --rule: #dfe0e4;
    --accent: #2f5fd0;
  }

  .pop-19:has(.pop-19__switch:checked) .pop-19__btn {
    color: #ffffff;
  }

  .pop-19:has(.pop-19__switch:checked) .pop-19__base {
    display: inline;
  }

  .pop-19:has(.pop-19__switch:checked) .pop-19__flip {
    display: none;
  }
}
```
