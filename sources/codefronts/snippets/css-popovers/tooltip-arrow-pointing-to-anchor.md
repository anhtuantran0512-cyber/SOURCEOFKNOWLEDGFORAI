---
source: "codefronts"
url: "https://codefronts.com/snippets/css-popovers/tooltip-arrow-pointing-to-anchor/"
title: "Tooltip Arrow Pointing to Anchor"
section: "snippets"
category: "css-popovers"
category_name: "CSS Popovers"
description: "The bubble is easy and the arrow is the part that breaks."
has_js: "false"
---

Here's a working CSS Popover from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tooltip Arrow Pointing to Anchor
Source: https://codefronts.com/snippets/css-popovers/tooltip-arrow-pointing-to-anchor/

The bubble is easy and the arrow is the part that breaks. Anchor positioning lets the arrow be positioned against the anchor rather than the bubble, so it stays pointed at the trigger when a fallback flips the panel to the other side. The bubble here is deliberately plain: the lesson is keeping the tail attached through a position change.
## HTML
```html
<div class="pop-08">
  <div class="pop-08__stage">
    <div class="pop-08__card">
      <p class="pop-08__kicker">Team roster</p>
      <ul class="pop-08__rows">
        <li class="pop-08__row">
          <span class="pop-08__who">Priya Sharma</span>
          <span class="pop-08__role">Reviewer</span>
          <button class="pop-08__info" type="button" popovertarget="pop-08-tip" aria-label="What reviewer permissions mean">
            <svg viewBox="0 0 20 20" width="17" height="17" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><circle cx="10" cy="10" r="7.2"/><path d="M10 9v5M10 6.3v.8"/></svg>
          </button>
        </li>
        <li class="pop-08__row">
          <span class="pop-08__who">Sam Rivera</span>
          <span class="pop-08__role">Owner</span>
          <span class="pop-08__spacer" aria-hidden="true"></span>
        </li>
      </ul>
      <p class="pop-08__foot">Open the hint, then narrow the frame — the tail follows the button.</p>
    </div>
  </div>

  <div class="pop-08__tip" popover="auto" id="pop-08-tip" role="group" aria-label="Reviewer permissions">
    Reviewers can comment and approve, but cannot merge or change settings.
  </div>
</div>
```
## CSS
```css
.pop-08 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --bg: #eef1e9;
  --surface: #ffffff;
  --ink: #1d2a22;
  --muted: #5f7263;
  --rule: #d5ded1;
  --sage: #3f6b52;
  --arrow: 11px;
  --gap: 12px;
  --font-ui: ui-sans-serif, system-ui, "Segoe UI", sans-serif;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--font-ui);
  padding: 40px 18px;
}

.pop-08__stage {
  display: grid;
  place-items: center;
  max-inline-size: 100%;
  min-height: calc(100vh - 80px);
}

.pop-08__card {
  inline-size: 100%;
  max-inline-size: 27rem;
  min-inline-size: 0;
  background: var(--surface);
  border: 1px solid var(--rule);
  border-radius: 14px;
  padding: 20px 18px 18px;
  box-shadow: 0 14px 30px -22px rgba(29, 42, 34, 0.4);
}

.pop-08__kicker {
  margin: 0 0 14px;
  font: 700 10px/1 var(--font-ui);
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--sage);
}

.pop-08__rows {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: 4px;
}

.pop-08__row {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 6px 0;
  border-block-end: 1px solid var(--rule);
  min-inline-size: 0;
}

.pop-08__row:last-child {
  border-block-end: 0;
}

.pop-08__who {
  flex: 1 1 auto;
  min-inline-size: 0;
  font-size: 14px;
  font-weight: 600;
}

.pop-08__role {
  flex: none;
  font-size: 12px;
  color: var(--muted);
}

.pop-08__spacer {
  flex: none;
  inline-size: 44px;
}

.pop-08__info {
  flex: none;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 44px;
  min-height: 44px;
  color: var(--sage);
  background: transparent;
  border: 1px solid var(--rule);
  border-radius: 999px;
  cursor: pointer;
  anchor-name: --pop-08-anchor;
}

.pop-08__info:hover {
  background: var(--bg);
}

.pop-08__info:focus-visible {
  outline: 3px solid var(--sage);
  outline-offset: 2px;
}

.pop-08__foot {
  margin: 16px 0 0;
  font-size: 12px;
  line-height: 1.6;
  color: var(--muted);
}

.pop-08__tip {
  position: fixed;
  margin: 0;
  inline-size: min(15rem, calc(100vw - 28px));
  max-inline-size: calc(100vw - 28px);
  padding: 10px 14px;
  font-size: 12.5px;
  line-height: 1.5;
  color: var(--surface);
  background: var(--ink);
  border: 0;
  border-radius: 999px;
  text-wrap: pretty;
  filter: drop-shadow(0 10px 18px rgba(29, 42, 34, 0.28));
}

@supports (anchor-name: --a) {
  .pop-08__tip {
    position-anchor: --pop-08-anchor;
    position-area: block-end center;
    justify-self: anchor-center;
    inset: auto;
    margin-block-start: var(--gap);
    position-try-fallbacks: flip-block;
  }
  /* The tail is anchored to the TRIGGER, not to the bubble, and carries the same
       fallback list — so a flip moves bubble and tail in the same frame. */

  .pop-08__tip::after {
    content: "";
    position: fixed;
    position-anchor: --pop-08-anchor;
    position-area: block-end center;
    justify-self: anchor-center;
    inset: auto;
    inline-size: var(--arrow);
    block-size: var(--arrow);
    margin-block-start: calc(var(--gap) - var(--arrow) / 2);
    background: var(--ink);
    border-radius: 2px;
    transform: rotate(45deg);
    position-try-fallbacks: flip-block;
  }
}

@supports not (anchor-name: --a) {
  .pop-08__tip::after {
    content: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .pop-08__tip {
    transition: none;
  }
}

@media (prefers-color-scheme: dark) {
  .pop-08 {
    --bg: #121611;
    --surface: #1b211a;
    --ink: #e9f0e6;
    --muted: #94a68f;
    --rule: #2c342a;
    --sage: #86bb9b;
  }

  .pop-08__tip {
    color: #121611;
    background: var(--ink);
  }

  .pop-08__tip::after {
    background: var(--ink);
  }
}

[data-theme="dark"] .pop-08 {
  --bg: #121611;
  --surface: #1b211a;
  --ink: #e9f0e6;
  --muted: #94a68f;
  --rule: #2c342a;
  --sage: #86bb9b;
}

[data-theme="dark"] .pop-08 .pop-08__tip {
  color: #121611;
}
```
