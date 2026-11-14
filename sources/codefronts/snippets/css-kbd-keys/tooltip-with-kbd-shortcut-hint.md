---
source: "codefronts"
url: "https://codefronts.com/snippets/css-kbd-keys/tooltip-with-kbd-shortcut-hint/"
title: "Tooltip with Kbd Shortcut Hint"
section: "snippets"
category: "css-kbd-keys"
category_name: "CSS Kbd Keys"
description: "A toolbar button whose tooltip names the action and shows its shortcut."
has_js: "false"
---

Here's a working CSS Kbd Key from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tooltip with Kbd Shortcut Hint
Source: https://codefronts.com/snippets/css-kbd-keys/tooltip-with-kbd-shortcut-hint/

A toolbar button whose tooltip names the action and shows its shortcut. The tooltip is deliberately plain — one dark panel, no arrow theatre, no entrance choreography — because the cap is the subject. It opens on hover and on focus-visible, so a keyboard user reaching the button by tab sees exactly what a mouse user sees.
## HTML
```html
<div class="kbd-13">
  <div class="kbd-13__stage">
    <div class="kbd-13__toolbar">
      <div class="kbd-13__slot">
        <button class="kbd-13__btn" type="button" aria-describedby="kbd-13-tip-bold">
          <span class="kbd-13__glyph" aria-hidden="true">B</span>
          <span class="kbd-13__vh">Bold</span>
        </button>
        <span class="kbd-13__tip" id="kbd-13-tip-bold" role="tooltip">
          <span class="kbd-13__tipname">Bold</span>
          <kbd class="kbd-13__combo"><kbd class="kbd-13__key">Ctrl</kbd><span class="kbd-13__sep" aria-hidden="true">+</span><kbd class="kbd-13__key">B</kbd></kbd>
        </span>
      </div>
      <div class="kbd-13__slot">
        <button class="kbd-13__btn" type="button" aria-describedby="kbd-13-tip-link">
          <svg class="kbd-13__icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M10 13a5 5 0 0 0 7 0l2-2a5 5 0 0 0-7-7l-1 1"/><path d="M14 11a5 5 0 0 0-7 0l-2 2a5 5 0 0 0 7 7l1-1"/></svg>
          <span class="kbd-13__vh">Insert link</span>
        </button>
        <span class="kbd-13__tip" id="kbd-13-tip-link" role="tooltip">
          <span class="kbd-13__tipname">Insert link</span>
          <kbd class="kbd-13__combo"><kbd class="kbd-13__key">Ctrl</kbd><span class="kbd-13__sep" aria-hidden="true">+</span><kbd class="kbd-13__key">K</kbd></kbd>
        </span>
      </div>
      <div class="kbd-13__slot">
        <button class="kbd-13__btn" type="button" aria-describedby="kbd-13-tip-comment">
          <svg class="kbd-13__icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 15a3 3 0 0 1-3 3H9l-5 3V6a3 3 0 0 1 3-3h10a3 3 0 0 1 3 3z"/></svg>
          <span class="kbd-13__vh">Add comment</span>
        </button>
        <span class="kbd-13__tip" id="kbd-13-tip-comment" role="tooltip">
          <span class="kbd-13__tipname">Add comment</span>
          <kbd class="kbd-13__combo"><kbd class="kbd-13__key">Ctrl</kbd><span class="kbd-13__sep" aria-hidden="true">+</span><kbd class="kbd-13__key">Alt</kbd><span class="kbd-13__sep" aria-hidden="true">+</span><kbd class="kbd-13__key">M</kbd></kbd>
        </span>
      </div>
    </div>
    <p class="kbd-13__hint">Hover a button, or tab to one — the tooltip opens either way</p>
    <div class="kbd-13__theme">
      <input class="kbd-13__themebox" type="checkbox" id="kbd-13-theme">
      <label class="kbd-13__themelabel" for="kbd-13-theme">
        <span class="kbd-13__themedot" aria-hidden="true"></span>
        <span class="kbd-13__themebase">Light</span><span class="kbd-13__themeflip">Dark</span>
      </label>
    </div>
  </div>
</div>
```
## CSS
```css
.kbd-13 {
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  --page: #e9edf2;
  --bar: #ffffff;
  --ink: #1e2732;
  --muted: #6c7987;
  --rule: #d5dce4;
  --tip-bg: #1c2530;
  --tip-ink: #f2f6fa;
  --cap: #33404f;
  --cap-ink: #e7eef6;
  --accent: #2f6fd0;
  --tip-offset: 12px;
  --font-key: ui-sans-serif, system-ui, "Segoe UI", sans-serif;
  background: var(--page);
  color: var(--ink);
  font-family: var(--font-key);
  padding: 40px 18px;
}

.kbd-13__stage {
  display: grid;
  place-items: center;
  align-content: center;
  gap: 90px;
  min-height: calc(100vh - 80px);
}

.kbd-13__toolbar {
  display: flex;
  gap: 6px;
  padding: 8px;
  background: var(--bar);
  border: 1px solid var(--rule);
  border-radius: 12px;
  box-shadow: 0 1px 2px rgba(30, 39, 50, 0.06);
}

.kbd-13__slot {
  position: relative;
}

.kbd-13__btn {
  inline-size: 46px;
  block-size: 46px;
  min-inline-size: 44px;
  min-block-size: 44px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: transparent;
  border: 0;
  border-radius: 9px;
  color: var(--ink);
  cursor: pointer;
  font-family: inherit;
  font-size: 17px;
  font-weight: 700;
  transition: background 140ms ease;
}

.kbd-13__btn:hover {
  background: rgba(47, 111, 208, 0.1);
}

.kbd-13__btn:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

.kbd-13__glyph {
  font-family: Georgia, serif;
}

.kbd-13__icon {
  inline-size: 21px;
  block-size: 21px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.8;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.kbd-13__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
  white-space: nowrap;
  border: 0;
  padding: 0;
  margin: -1px;
}

.kbd-13__tip {
  position: absolute;
  inset-block-end: calc(100% + var(--tip-offset));
  inset-inline-start: 50%;
  transform: translate(-50%, 4px);
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 8px 10px;
  background: var(--tip-bg);
  color: var(--tip-ink);
  border-radius: 7px;
  white-space: nowrap;
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transition: opacity 140ms ease, transform 140ms ease, visibility 140ms;
}

.kbd-13__btn:hover + .kbd-13__tip,
.kbd-13__btn:focus-visible + .kbd-13__tip {
  opacity: 1;
  visibility: visible;
  transform: translate(-50%, 0);
}

.kbd-13__tipname {
  font-size: 12.5px;
  font-weight: 600;
  letter-spacing: 0.01em;
}

.kbd-13__combo {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-family: inherit;
}

.kbd-13__key {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-inline-size: 22px;
  min-block-size: 20px;
  padding: 0 5px;
  box-sizing: border-box;
  font-family: inherit;
  font-size: 11px;
  font-weight: 600;
  line-height: 1;
  color: var(--cap-ink);
  background: var(--cap);
  border-radius: 4px;
}

.kbd-13__sep {
  font-size: 10px;
  color: #93a3b4;
  user-select: none;
}

.kbd-13__hint {
  margin: 0;
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--muted);
  text-align: center;
  min-inline-size: 0;
}

@media (prefers-reduced-motion: reduce) {
  .kbd-13__tip,
    .kbd-13__btn {
    transition: none;
  }

  .kbd-13__btn:hover + .kbd-13__tip,
    .kbd-13__btn:focus-visible + .kbd-13__tip {
    transform: translate(-50%, 0);
  }
}

.kbd-13[data-theme="dark"],
[data-theme="dark"] .kbd-13 {
  --page: #10161d;
  --bar: #1a222c;
  --ink: #e7eef6;
  --muted: #8593a1;
  --rule: #2a343f;
  --tip-bg: #f2f6fa;
  --tip-ink: #16202b;
  --cap: #d3dde7;
  --cap-ink: #16202b;
  --accent: #6ea8ff;
}
/* In-demo theme switch. State is one checkbox inside this demo, so the toggle
   themes THIS demo only — no root attribute, no script. */

.kbd-13__theme {
  position: absolute;
  inset-block-start: 14px;
  inset-inline-end: 16px;
  z-index: 5;
  display: flex;
}
/* the pill owns the top-right corner, so the stage reserves that band */

.kbd-13__stage {
  box-sizing: border-box;
  padding-block-start: 46px;
}

.kbd-13__themebox {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  pointer-events: none;
}

.kbd-13__themelabel {
  display: inline-flex;
  align-items: center;
  gap: 9px;
  min-block-size: 44px;
  padding: 0 16px;
  box-sizing: border-box;
  font-family: var(--font-key, ui-sans-serif, system-ui, sans-serif);
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  line-height: 1;
  color: var(--ink, var(--cap-ink, currentColor));
  background: transparent;
  border: 1px solid currentColor;
  border-radius: 999px;
  cursor: pointer;
  user-select: none;
}

.kbd-13__themedot {
  inline-size: 12px;
  block-size: 12px;
  flex: none;
  border-radius: 50%;
  background: currentColor;
}

.kbd-13__themebox:focus-visible + .kbd-13__themelabel {
  outline: 3px solid var(--accent, var(--cap-ink, currentColor));
  outline-offset: 2px;
}

@supports (border-color: color-mix(in oklab, currentColor 50%, transparent)) {
  .kbd-13__themelabel {
    border-color: color-mix(in oklab, currentColor 65%, transparent);
  }
}

.kbd-13__themeflip {
  display: none;
}

.kbd-13:has(.kbd-13__themebox:checked) {
  --page: #10161d;
  --bar: #1a222c;
  --ink: #e7eef6;
  --muted: #8593a1;
  --rule: #2a343f;
  --tip-bg: #f2f6fa;
  --tip-ink: #16202b;
  --cap: #d3dde7;
  --cap-ink: #16202b;
  --accent: #6ea8ff;
}

.kbd-13:has(.kbd-13__themebox:checked) .kbd-13__themebase {
  display: none;
}

.kbd-13:has(.kbd-13__themebox:checked) .kbd-13__themeflip {
  display: inline;
}

.kbd-13:has(.kbd-13__themebox:checked) .kbd-13__sep {
  color: #66788a;
}
/* The flip-back rule: on the opposite OS preference the unchecked state is the
   flipped palette, and checking the box returns to the demo's own default. */

@media (prefers-color-scheme: dark) {
  .kbd-13:not(:has(.kbd-13__themebox:checked)) {
    --page: #10161d;
    --bar: #1a222c;
    --ink: #e7eef6;
    --muted: #8593a1;
    --rule: #2a343f;
    --tip-bg: #f2f6fa;
    --tip-ink: #16202b;
    --cap: #d3dde7;
    --cap-ink: #16202b;
    --accent: #6ea8ff;
  }

  .kbd-13:has(.kbd-13__themebox:checked) {
    --page: #e9edf2;
    --bar: #ffffff;
    --ink: #1e2732;
    --muted: #6c7987;
    --rule: #d5dce4;
    --tip-bg: #1c2530;
    --tip-ink: #f2f6fa;
    --cap: #33404f;
    --cap-ink: #e7eef6;
    --accent: #2f6fd0;
  }

  .kbd-13:not(:has(.kbd-13__themebox:checked)) .kbd-13__themebase {
    display: none;
  }

  .kbd-13:not(:has(.kbd-13__themebox:checked)) .kbd-13__themeflip {
    display: inline;
  }

  .kbd-13:has(.kbd-13__themebox:checked) .kbd-13__themebase {
    display: inline;
  }

  .kbd-13:has(.kbd-13__themebox:checked) .kbd-13__themeflip {
    display: none;
  }

  .kbd-13:not(:has(.kbd-13__themebox:checked)) .kbd-13__sep {
    color: #66788a;
  }

  .kbd-13:has(.kbd-13__themebox:checked) .kbd-13__sep {
    color: #93a3b4;
  }
}
/* Responsive guard (Phase A): the tooltip is absolutely positioned and
   centred on its trigger, so near the viewport edge at 320px its right
   edge lands outside the document. Clip at the scoped root. */

.kbd-13 {
  overflow-x: hidden;
}
```
