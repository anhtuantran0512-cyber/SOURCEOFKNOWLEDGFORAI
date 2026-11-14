---
source: "codefronts"
url: "https://codefronts.com/snippets/css-popovers/tooltip-on-hover-and-focus/"
title: "Tooltip on Hover and Focus"
section: "snippets"
category: "css-popovers"
category_name: "CSS Popovers"
description: "Popover's built-in trigger is click, so a hover tooltip has to call showPopover and hidePopover itself."
has_js: "true"
---

Here's a working CSS Popover from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tooltip on Hover and Focus
Source: https://codefronts.com/snippets/css-popovers/tooltip-on-hover-and-focus/

Popover's built-in trigger is click, so a hover tooltip has to call showPopover and hidePopover itself. Under twenty-five lines gets pointer and focus parity, an open delay so the tooltip does not fire while the cursor crosses the element, and no close delay so it gets out of the way instantly. This is the case where the API buys you the least.
## HTML
```html
<div class="pop-12">
  <div class="pop-12__stage">
    <article class="pop-12__essay">
      <p class="pop-12__kicker">Field notes · Typesetting</p>
      <h2 class="pop-12__h">The measure of a column</h2>
      <p class="pop-12__p">Set a column too wide and the eye loses the return sweep; too narrow and hyphenation does the reading for you. The old compositors aimed for a
        <button class="pop-12__term" type="button" id="pop-12-trigger" aria-describedby="pop-12-tip">measure</button>
        of sixty-six characters and were rarely wrong, which is why the figure survives in every style manual written since.</p>
      <p class="pop-12__p">Hover the term, or tab to it. The hint appears after a short pause and leaves the moment you move on.</p>
    </article>
  </div>

  <div class="pop-12__tip" popover="manual" id="pop-12-tip" role="tooltip">The number of characters, including spaces, on a single line of set text.</div>
</div>
```
## CSS
```css
.pop-12 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --paper: #fbfaf6;
  --ink: #1a1a18;
  --muted: #6a675e;
  --rule: #e3e0d6;
  --accent: #8c2f1f;
  --font-serif: "Iowan Old Style", Georgia, "Times New Roman", serif;
  --font-ui: ui-sans-serif, system-ui, sans-serif;
  background: var(--paper);
  color: var(--ink);
  font-family: var(--font-serif);
  padding: 44px 20px;
}

.pop-12__stage {
  display: grid;
  place-items: center;
  max-inline-size: 100%;
  min-height: calc(100vh - 88px);
}

.pop-12__essay {
  inline-size: 100%;
  max-inline-size: 32rem;
  min-inline-size: 0;
}

.pop-12__kicker {
  margin: 0 0 12px;
  font: 700 10px/1 var(--font-ui);
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--accent);
}

.pop-12__h {
  margin: 0 0 18px;
  font: 400 clamp(26px, 6vw, 38px)/1.12 var(--font-serif);
  letter-spacing: -0.02em;
}

.pop-12__p {
  margin: 0 0 16px;
  font: 400 clamp(16px, 3.6vw, 18px)/1.72 var(--font-serif);
  color: var(--ink);
  text-wrap: pretty;
}

.pop-12__term {
  display: inline;
  padding: 0;
  font: inherit;
  color: var(--accent);
  background: none;
  border: 0;
  border-block-end: 1px solid var(--accent);
  cursor: help;
  anchor-name: --pop-12-anchor;
}

.pop-12__term:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
  border-radius: 2px;
}

.pop-12__tip {
  position: fixed;
  margin: 0;
  inline-size: min(16rem, calc(100vw - 28px));
  max-inline-size: calc(100vw - 28px);
  padding: 9px 12px;
  font: 400 12.5px/1.5 var(--font-ui);
  color: var(--paper);
  background: var(--ink);
  border: 0;
  border-radius: 4px;
  text-wrap: pretty;
  opacity: 0;
  transition: opacity 140ms ease, display 140ms allow-discrete, overlay 140ms allow-discrete;
}

.pop-12__tip:popover-open {
  opacity: 1;
}

@starting-style {
  .pop-12__tip:popover-open {
    opacity: 0;
  }
}

@supports (anchor-name: --a) {
  .pop-12__tip {
    position-anchor: --pop-12-anchor;
    position-area: block-start center;
    justify-self: anchor-center;
    inset: auto;
    margin-block-end: 8px;
    position-try-fallbacks: flip-block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .pop-12__tip {
    transition: none;
    opacity: 1;
  }

  @starting-style {
    .pop-12__tip:popover-open {
      opacity: 1;
    }
  }
}

@media (prefers-color-scheme: dark) {
  .pop-12 {
    --paper: #14140f;
    --ink: #f3f1e7;
    --muted: #a09a8b;
    --rule: #2f2c23;
    --accent: #e08a6f;
  }

  .pop-12__tip {
    color: #14140f;
    background: var(--ink);
  }
}

[data-theme="dark"] .pop-12 {
  --paper: #14140f;
  --ink: #f3f1e7;
  --muted: #a09a8b;
  --rule: #2f2c23;
  --accent: #e08a6f;
}

[data-theme="dark"] .pop-12 .pop-12__tip {
  color: #14140f;
}
```

## JavaScript
```js
const trigger = document.getElementById('pop-12-trigger');
const tip = document.getElementById('pop-12-tip');
if (HTMLElement.prototype.hasOwnProperty('popover')) {
  let timer = 0;
  const open = (delay) => {
    clearTimeout(timer);
    timer = setTimeout(() => { if (!tip.matches(':popover-open')) tip.showPopover(); }, delay);
  };
  const close = () => {
    clearTimeout(timer);
    if (tip.matches(':popover-open')) tip.hidePopover();
  };
  trigger.addEventListener('pointerenter', () => open(150));
  trigger.addEventListener('pointerleave', close);
  trigger.addEventListener('focusin', () => open(0));
  trigger.addEventListener('focusout', close);
  trigger.addEventListener('click', () => open(0));
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape') close(); });
}
```
