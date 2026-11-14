---
source: "codefronts"
url: "https://codefronts.com/snippets/css-kbd-keys/mac-command-vs-windows-ctrl-toggle/"
title: "Mac Command vs Windows Ctrl Toggle"
section: "snippets"
category: "css-kbd-keys"
category_name: "CSS Kbd Keys"
description: "A visible platform switch that rewrites an entire shortcut list between Mac glyphs and Windows words, with no JavaScript at all."
has_js: "false"
---

Here's a working CSS Kbd Key from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Mac Command vs Windows Ctrl Toggle
Source: https://codefronts.com/snippets/css-kbd-keys/mac-command-vs-windows-ctrl-toggle/

A visible platform switch that rewrites an entire shortcut list between Mac glyphs and Windows words, with no JavaScript at all. State lives in a hidden radio pair and the has() selector on the demo root swaps which span inside each key is displayed. The Mac side uses the real modifier glyphs in the canonical order that macOS itself renders them.
## HTML
```html
<div class="kbd-06">
  <div class="kbd-06__stage">
    <section class="kbd-06__panel">
      <h2 class="kbd-06__title">Shortcut reference</h2>
      <fieldset class="kbd-06__switch">
        <legend class="kbd-06__vh">Choose a platform</legend>
        <input class="kbd-06__radio kbd-06__radio--mac" type="radio" name="kbd-06-os" id="kbd-06-mac" checked>
        <label class="kbd-06__tab" for="kbd-06-mac">macOS</label>
        <input class="kbd-06__radio kbd-06__radio--win" type="radio" name="kbd-06-os" id="kbd-06-win">
        <label class="kbd-06__tab" for="kbd-06-win">Windows</label>
      </fieldset>
      <ul class="kbd-06__list">
        <li class="kbd-06__row">
          <span class="kbd-06__action">Save file</span>
          <kbd class="kbd-06__combo"><kbd class="kbd-06__key"><span class="kbd-06__mac">⌘</span><span class="kbd-06__win">Ctrl</span></kbd><span class="kbd-06__sep" aria-hidden="true">+</span><kbd class="kbd-06__key">S</kbd></kbd>
        </li>
        <li class="kbd-06__row">
          <span class="kbd-06__action">Redo</span>
          <kbd class="kbd-06__combo"><kbd class="kbd-06__key"><span class="kbd-06__mac">⇧</span><span class="kbd-06__win">Shift</span></kbd><span class="kbd-06__sep" aria-hidden="true">+</span><kbd class="kbd-06__key"><span class="kbd-06__mac">⌘</span><span class="kbd-06__win">Ctrl</span></kbd><span class="kbd-06__sep" aria-hidden="true">+</span><kbd class="kbd-06__key">Z</kbd></kbd>
        </li>
        <li class="kbd-06__row">
          <span class="kbd-06__action">Delete word left</span>
          <kbd class="kbd-06__combo"><kbd class="kbd-06__key"><span class="kbd-06__mac">⌥</span><span class="kbd-06__win">Alt</span></kbd><span class="kbd-06__sep" aria-hidden="true">+</span><kbd class="kbd-06__key"><span class="kbd-06__mac">⌫</span><span class="kbd-06__win">Backspace</span></kbd></kbd>
        </li>
        <li class="kbd-06__row">
          <span class="kbd-06__action">Open terminal</span>
          <kbd class="kbd-06__combo"><kbd class="kbd-06__key"><span class="kbd-06__mac">⌃</span><span class="kbd-06__win">Ctrl</span></kbd><span class="kbd-06__sep" aria-hidden="true">+</span><kbd class="kbd-06__key">Backtick</kbd></kbd>
        </li>
        <li class="kbd-06__row">
          <span class="kbd-06__action">Confirm dialog</span>
          <kbd class="kbd-06__combo"><kbd class="kbd-06__key"><span class="kbd-06__mac">⏎</span><span class="kbd-06__win">Enter</span></kbd></kbd>
        </li>
        <li class="kbd-06__row">
          <span class="kbd-06__action">Dismiss dialog</span>
          <kbd class="kbd-06__combo"><kbd class="kbd-06__key"><span class="kbd-06__mac">⎋</span><span class="kbd-06__win">Esc</span></kbd></kbd>
        </li>
      </ul>
      <p class="kbd-06__foot">Mac modifiers print in the platform order: <span class="kbd-06__glyphrun">⌃ ⌥ ⇧ ⌘</span></p>
    </section>
    <div class="kbd-06__theme">
      <input class="kbd-06__themebox" type="checkbox" id="kbd-06-theme">
      <label class="kbd-06__themelabel" for="kbd-06-theme">
        <span class="kbd-06__themedot" aria-hidden="true"></span>
        <span class="kbd-06__themebase">Dark</span><span class="kbd-06__themeflip">Light</span>
      </label>
    </div>
  </div>
</div>
```
## CSS
```css
.kbd-06 {
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  --bg: #211d19;
  --panel: #2b2621;
  --ink: #f4ece1;
  --muted: #a3937f;
  --rule: #3d362e;
  --cap: #352f28;
  --cap-border: #574d41;
  --cap-ink: #f8f1e5;
  --accent: #f0a63c;
  --tab-radius: 8px;
  --font-key: ui-sans-serif, system-ui, "Helvetica Neue", "Apple Symbols", sans-serif;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--font-key);
  padding: 40px 18px;
}

.kbd-06__stage {
  display: grid;
  place-items: center;
  min-height: calc(100vh - 80px);
}

.kbd-06__panel {
  inline-size: 100%;
  max-inline-size: 30rem;
  min-inline-size: 0;
  background: var(--panel);
  border: 1px solid var(--rule);
  border-radius: 12px;
  padding: 24px 22px 20px;
}

.kbd-06__title {
  margin: 0 0 16px;
  font-size: 17px;
  font-weight: 700;
  letter-spacing: -0.01em;
}

.kbd-06__vh {
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

.kbd-06__switch {
  margin: 0 0 18px;
  padding: 4px;
  border: 1px solid var(--rule);
  border-radius: calc(var(--tab-radius) + 4px);
  display: flex;
  gap: 4px;
  background: rgba(0, 0, 0, 0.22);
}

.kbd-06__radio {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  pointer-events: none;
}

.kbd-06__tab {
  flex: 1 1 0;
  min-inline-size: 0;
  min-block-size: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: var(--tab-radius);
  font-size: 13px;
  font-weight: 600;
  letter-spacing: 0.02em;
  color: var(--muted);
  cursor: pointer;
  user-select: none;
  transition: background 160ms ease, color 160ms ease;
}

.kbd-06:has(.kbd-06__radio--mac:checked) .kbd-06__tab[for="kbd-06-mac"],
.kbd-06:has(.kbd-06__radio--win:checked) .kbd-06__tab[for="kbd-06-win"] {
  background: var(--accent);
  color: #241c10;
}

.kbd-06__radio:focus-visible + .kbd-06__tab {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

.kbd-06__win {
  display: none;
}

.kbd-06:has(.kbd-06__radio--win:checked) .kbd-06__mac {
  display: none;
}

.kbd-06:has(.kbd-06__radio--win:checked) .kbd-06__win {
  display: inline;
}

.kbd-06__list {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: 1px;
}

.kbd-06__row {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  padding: 10px 0;
  border-bottom: 1px solid var(--rule);
}

.kbd-06__row:last-child {
  border-bottom: 0;
}

.kbd-06__action {
  font-size: 13.5px;
  min-inline-size: 0;
  flex: 1 1 9rem;
}

.kbd-06__combo {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  flex-wrap: wrap;
  font-family: inherit;
  min-inline-size: 0;
}

.kbd-06__key {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-inline-size: 30px;
  min-block-size: 28px;
  padding: 0 8px;
  box-sizing: border-box;
  font-family: inherit;
  font-size: 13px;
  font-weight: 600;
  line-height: 1;
  color: var(--cap-ink);
  background: var(--cap);
  border: 1px solid var(--cap-border);
  border-radius: 6px;
  box-shadow: 0 1px 0 #17130f;
  white-space: nowrap;
}

.kbd-06__sep {
  font-size: 11px;
  color: var(--muted);
  user-select: none;
}

.kbd-06__foot {
  margin: 18px 0 0;
  padding-top: 14px;
  border-top: 1px solid var(--rule);
  font-size: 11.5px;
  color: var(--muted);
  text-wrap: pretty;
}

.kbd-06__glyphrun {
  color: var(--accent);
  letter-spacing: 0.22em;
  font-size: 13px;
}

@media (prefers-reduced-motion: reduce) {
  .kbd-06__tab {
    transition: none;
  }
}
/* In-demo theme switch. State is one checkbox inside this demo, so the toggle
   themes THIS demo only — no root attribute, no script. */

.kbd-06__theme {
  position: absolute;
  inset-block-start: 14px;
  inset-inline-end: 16px;
  z-index: 5;
  display: flex;
}
/* the pill owns the top-right corner, so the stage reserves that band */

.kbd-06__stage {
  box-sizing: border-box;
  padding-block-start: 46px;
}

.kbd-06__themebox {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  pointer-events: none;
}

.kbd-06__themelabel {
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

.kbd-06__themedot {
  inline-size: 12px;
  block-size: 12px;
  flex: none;
  border-radius: 50%;
  background: currentColor;
}

.kbd-06__themebox:focus-visible + .kbd-06__themelabel {
  outline: 3px solid var(--accent, var(--cap-ink, currentColor));
  outline-offset: 2px;
}

@supports (border-color: color-mix(in oklab, currentColor 50%, transparent)) {
  .kbd-06__themelabel {
    border-color: color-mix(in oklab, currentColor 65%, transparent);
  }
}

.kbd-06__themeflip {
  display: none;
}

.kbd-06:has(.kbd-06__themebox:checked) {
  --bg: #f6f1e8;
  --panel: #fffdf8;
  --ink: #2b241c;
  --muted: #8a7a64;
  --rule: #e4d9c7;
  --cap: #f6efe2;
  --cap-border: #cdbfa6;
  --cap-ink: #34291d;
  --accent: #c47a12;
}

.kbd-06:has(.kbd-06__themebox:checked) .kbd-06__themebase {
  display: none;
}

.kbd-06:has(.kbd-06__themebox:checked) .kbd-06__themeflip {
  display: inline;
}

.kbd-06:has(.kbd-06__themebox:checked) .kbd-06__switch {
  background: rgba(0, 0, 0, 0.04);
}

.kbd-06:has(.kbd-06__themebox:checked) .kbd-06__key {
  box-shadow: 0 1px 0 #cdbfa6;
}

.kbd-06:has(.kbd-06__themebox:checked):has(.kbd-06__radio--mac:checked) .kbd-06__tab[for="kbd-06-mac"],
.kbd-06:has(.kbd-06__themebox:checked):has(.kbd-06__radio--win:checked) .kbd-06__tab[for="kbd-06-win"] {
  color: #fffdf8;
}
/* The flip-back rule: on the opposite OS preference the unchecked state is the
   flipped palette, and checking the box returns to the demo's own default. */

@media (prefers-color-scheme: light) {
  .kbd-06:not(:has(.kbd-06__themebox:checked)) {
    --bg: #f6f1e8;
    --panel: #fffdf8;
    --ink: #2b241c;
    --muted: #8a7a64;
    --rule: #e4d9c7;
    --cap: #f6efe2;
    --cap-border: #cdbfa6;
    --cap-ink: #34291d;
    --accent: #c47a12;
  }

  .kbd-06:has(.kbd-06__themebox:checked) {
    --bg: #211d19;
    --panel: #2b2621;
    --ink: #f4ece1;
    --muted: #a3937f;
    --rule: #3d362e;
    --cap: #352f28;
    --cap-border: #574d41;
    --cap-ink: #f8f1e5;
    --accent: #f0a63c;
  }

  .kbd-06:not(:has(.kbd-06__themebox:checked)) .kbd-06__themebase {
    display: none;
  }

  .kbd-06:not(:has(.kbd-06__themebox:checked)) .kbd-06__themeflip {
    display: inline;
  }

  .kbd-06:has(.kbd-06__themebox:checked) .kbd-06__themebase {
    display: inline;
  }

  .kbd-06:has(.kbd-06__themebox:checked) .kbd-06__themeflip {
    display: none;
  }

  .kbd-06:not(:has(.kbd-06__themebox:checked)) .kbd-06__switch {
    background: rgba(0, 0, 0, 0.04);
  }

  .kbd-06:has(.kbd-06__themebox:checked) .kbd-06__switch {
    background: rgba(0, 0, 0, 0.22);
  }

  .kbd-06:not(:has(.kbd-06__themebox:checked)) .kbd-06__key {
    box-shadow: 0 1px 0 #cdbfa6;
  }

  .kbd-06:has(.kbd-06__themebox:checked) .kbd-06__key {
    box-shadow: 0 1px 0 #17130f;
  }

  .kbd-06:not(:has(.kbd-06__themebox:checked)):has(.kbd-06__radio--mac:checked) .kbd-06__tab[for="kbd-06-mac"],
    .kbd-06:not(:has(.kbd-06__themebox:checked)):has(.kbd-06__radio--win:checked) .kbd-06__tab[for="kbd-06-win"] {
    color: #fffdf8;
  }

  .kbd-06:has(.kbd-06__themebox:checked):has(.kbd-06__radio--mac:checked) .kbd-06__tab[for="kbd-06-mac"],
    .kbd-06:has(.kbd-06__themebox:checked):has(.kbd-06__radio--win:checked) .kbd-06__tab[for="kbd-06-win"] {
    color: #241c10;
  }
}
```
