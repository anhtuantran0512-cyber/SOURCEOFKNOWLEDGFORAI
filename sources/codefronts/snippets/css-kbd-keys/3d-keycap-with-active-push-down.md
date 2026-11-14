---
source: "codefronts"
url: "https://codefronts.com/snippets/css-kbd-keys/3d-keycap-with-active-push-down/"
title: "3D Keycap with Active Push Down"
section: "snippets"
category: "css-kbd-keys"
category_name: "CSS Kbd Keys"
description: "A cap with a real side wall."
has_js: "false"
---

Here's a working CSS Kbd Key from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: 3D Keycap with Active Push Down
Source: https://codefronts.com/snippets/css-kbd-keys/3d-keycap-with-active-push-down/

A cap with a real side wall. Layered box-shadows build the wall and the shadow it casts, a lighter gradient forms the top face, and the pressed state translates the cap down while collapsing the wall by the same amount, so the key travels instead of sliding. The press fires on both active and focus-visible, because a key you can only push with a mouse is not a key.
## HTML
```html
<div class="kbd-02">
  <div class="kbd-02__stage">
    <p class="kbd-02__hint">Press and hold a cap, or tab to one and hold Enter</p>
    <div class="kbd-02__board">
      <kbd class="kbd-02__key" tabindex="0">Q</kbd>
      <kbd class="kbd-02__key" tabindex="0">W</kbd>
      <kbd class="kbd-02__key" tabindex="0">E</kbd>
      <kbd class="kbd-02__key" tabindex="0">R</kbd>
      <kbd class="kbd-02__key kbd-02__key--wide" tabindex="0">Shift</kbd>
    </div>
    <p class="kbd-02__caption">Travel 4px · wall 6px collapsing to 2px</p>
    <div class="kbd-02__theme">
      <input class="kbd-02__themebox" type="checkbox" id="kbd-02-theme">
      <label class="kbd-02__themelabel" for="kbd-02-theme">
        <span class="kbd-02__themedot" aria-hidden="true"></span>
        <span class="kbd-02__themebase">Dark</span><span class="kbd-02__themeflip">Light</span>
      </label>
    </div>
  </div>
</div>
```
## CSS
```css
.kbd-02 {
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  --board: #101a2e;
  --board-2: #16233c;
  --ink: #e8edf7;
  --muted: #8494b4;
  --cap-top: #f4f6fb;
  --cap-bot: #d8deea;
  --cap-ink: #16233c;
  --wall-col: #94a0b8;
  --wall: 6px;
  --travel: 4px;
  --radius: 8px;
  --font-key: "Helvetica Neue", ui-sans-serif, system-ui, sans-serif;
  background: radial-gradient(120% 90% at 50% 0%, var(--board-2) 0%, var(--board) 70%);
  color: var(--ink);
  padding: 40px 20px;
}

.kbd-02__stage {
  display: grid;
  place-items: center;
  gap: 26px;
  min-height: calc(100vh - 80px);
}

.kbd-02__hint,
.kbd-02__caption {
  margin: 0;
  font: 600 11px/1.5 var(--font-key);
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--muted);
  text-align: center;
  min-inline-size: 0;
}

.kbd-02__board {
  display: flex;
  flex-wrap: wrap;
  gap: 14px;
  justify-content: center;
  align-items: flex-start;
  max-inline-size: 34rem;
}

.kbd-02__key {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-inline-size: 56px;
  min-block-size: 52px;
  padding: 0 14px;
  box-sizing: border-box;
  font-family: var(--font-key);
  font-size: 17px;
  font-weight: 600;
  letter-spacing: 0.04em;
  line-height: 1;
  color: var(--cap-ink);
  background: linear-gradient(180deg, var(--cap-top) 0%, var(--cap-bot) 100%);
  border: 0;
  border-radius: var(--radius);
  cursor: pointer;
  user-select: none;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.9), inset 0 -2px 3px rgba(22, 35, 60, 0.14), 0 var(--wall) 0 var(--wall-col), 0 calc(var(--wall) + 6px) 14px rgba(4, 9, 20, 0.55);
  transition: transform 110ms cubic-bezier(0.3, 0.7, 0.4, 1), box-shadow 110ms cubic-bezier(0.3, 0.7, 0.4, 1);
}

.kbd-02__key--wide {
  min-inline-size: 104px;
  font-size: 14px;
}

.kbd-02__key:hover {
  background: linear-gradient(180deg, #ffffff 0%, var(--cap-bot) 100%);
}

.kbd-02__key:active,
.kbd-02__key:focus-visible {
  transform: translateY(var(--travel));
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.7), inset 0 -1px 2px rgba(22, 35, 60, 0.2), 0 calc(var(--wall) - var(--travel)) 0 var(--wall-col), 0 calc(var(--wall) - var(--travel) + 3px) 6px rgba(4, 9, 20, 0.5);
}

.kbd-02__key:focus-visible {
  outline: 3px solid #ffd166;
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .kbd-02__key {
    transition: none;
  }
}

.kbd-02[data-theme="dark"],
[data-theme="dark"] .kbd-02 {
  --board: #070c16;
  --board-2: #0e1728;
  --wall-col: #6c7a94;
}
/* In-demo theme switch. State is one checkbox inside this demo, so the toggle
   themes THIS demo only — no root attribute, no script. */

.kbd-02__theme {
  position: absolute;
  inset-block-start: 14px;
  inset-inline-end: 16px;
  z-index: 5;
  display: flex;
}
/* the pill owns the top-right corner, so the stage reserves that band */

.kbd-02__stage {
  box-sizing: border-box;
  padding-block-start: 46px;
}

.kbd-02__themebox {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  pointer-events: none;
}

.kbd-02__themelabel {
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

.kbd-02__themedot {
  inline-size: 12px;
  block-size: 12px;
  flex: none;
  border-radius: 50%;
  background: currentColor;
}

.kbd-02__themebox:focus-visible + .kbd-02__themelabel {
  outline: 3px solid var(--accent, var(--cap-ink, currentColor));
  outline-offset: 2px;
}

@supports (border-color: color-mix(in oklab, currentColor 50%, transparent)) {
  .kbd-02__themelabel {
    border-color: color-mix(in oklab, currentColor 65%, transparent);
  }
}

.kbd-02__themeflip {
  display: none;
}

.kbd-02:has(.kbd-02__themebox:checked) {
  --board: #dfe4ec;
  --board-2: #f0f3f8;
  --ink: #1b2434;
  --muted: #5d6b85;
  --cap-top: #ffffff;
  --cap-bot: #e7ebf3;
  --cap-ink: #16233c;
  --wall-col: #a9b4c7;
}

.kbd-02:has(.kbd-02__themebox:checked) .kbd-02__themebase {
  display: none;
}

.kbd-02:has(.kbd-02__themebox:checked) .kbd-02__themeflip {
  display: inline;
}
/* The flip-back rule: on the opposite OS preference the unchecked state is the
   flipped palette, and checking the box returns to the demo's own default. */

@media (prefers-color-scheme: light) {
  .kbd-02:not(:has(.kbd-02__themebox:checked)) {
    --board: #dfe4ec;
    --board-2: #f0f3f8;
    --ink: #1b2434;
    --muted: #5d6b85;
    --cap-top: #ffffff;
    --cap-bot: #e7ebf3;
    --cap-ink: #16233c;
    --wall-col: #a9b4c7;
  }

  .kbd-02:has(.kbd-02__themebox:checked) {
    --board: #101a2e;
    --board-2: #16233c;
    --ink: #e8edf7;
    --muted: #8494b4;
    --cap-top: #f4f6fb;
    --cap-bot: #d8deea;
    --cap-ink: #16233c;
    --wall-col: #94a0b8;
  }

  .kbd-02:not(:has(.kbd-02__themebox:checked)) .kbd-02__themebase {
    display: none;
  }

  .kbd-02:not(:has(.kbd-02__themebox:checked)) .kbd-02__themeflip {
    display: inline;
  }

  .kbd-02:has(.kbd-02__themebox:checked) .kbd-02__themebase {
    display: inline;
  }

  .kbd-02:has(.kbd-02__themebox:checked) .kbd-02__themeflip {
    display: none;
  }
}
```
