---
source: "codefronts"
url: "https://codefronts.com/snippets/css-kbd-keys/glassmorphic-translucent-keycap/"
title: "Glassmorphic Translucent Keycap"
section: "snippets"
category: "css-kbd-keys"
category_name: "CSS Kbd Keys"
description: "Frosted caps over a rich gradient: backdrop-filter blur with a saturate boost, a thin inner rim catching the light along the top edge, and a solid fallback…"
has_js: "false"
---

Here's a working CSS Kbd Key from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphic Translucent Keycap
Source: https://codefronts.com/snippets/css-kbd-keys/glassmorphic-translucent-keycap/

Frosted caps over a rich gradient: backdrop-filter blur with a saturate boost, a thin inner rim catching the light along the top edge, and a solid fallback declared first so engines without backdrop-filter get an opaque cap rather than an invisible one. The trap is documented too — an ancestor combining overflow hidden with a transform kills the effect silently.
## HTML
```html
<div class="kbd-17">
  <div class="kbd-17__stage">
    <div class="kbd-17__panel">
      <p class="kbd-17__eyebrow">Now playing · shortcuts</p>
      <div class="kbd-17__rows">
        <div class="kbd-17__row">
          <span class="kbd-17__label">Play or pause</span>
          <kbd class="kbd-17__combo"><kbd class="kbd-17__key kbd-17__key--wide">Space</kbd></kbd>
        </div>
        <div class="kbd-17__row">
          <span class="kbd-17__label">Next track</span>
          <kbd class="kbd-17__combo"><kbd class="kbd-17__key">⌘</kbd><span class="kbd-17__sep" aria-hidden="true">+</span><kbd class="kbd-17__key">→</kbd></kbd>
        </div>
        <div class="kbd-17__row">
          <span class="kbd-17__label">Volume up</span>
          <kbd class="kbd-17__combo"><kbd class="kbd-17__key">⌥</kbd><span class="kbd-17__sep" aria-hidden="true">+</span><kbd class="kbd-17__key">↑</kbd></kbd>
        </div>
        <div class="kbd-17__row">
          <span class="kbd-17__label">Shuffle queue</span>
          <kbd class="kbd-17__combo"><kbd class="kbd-17__key">⇧</kbd><span class="kbd-17__sep" aria-hidden="true">+</span><kbd class="kbd-17__key">S</kbd></kbd>
        </div>
      </div>
      <p class="kbd-17__foot">Solid fill declared first · blur added behind @supports</p>
    </div>
    <div class="kbd-17__theme">
      <input class="kbd-17__themebox" type="checkbox" id="kbd-17-theme">
      <label class="kbd-17__themelabel" for="kbd-17-theme">
        <span class="kbd-17__themedot" aria-hidden="true"></span>
        <span class="kbd-17__themebase">Dark</span><span class="kbd-17__themeflip">Light</span>
      </label>
    </div>
  </div>
</div>
```
## CSS
```css
.kbd-17 {
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  --ink: #f6f0ff;
  --muted: rgba(246, 240, 255, 0.62);
  --cap-fallback: rgba(255, 255, 255, 0.34);
  --cap-glass: rgba(255, 255, 255, 0.16);
  --cap-border: rgba(255, 255, 255, 0.42);
  --cap-ink: #ffffff;
  --radius: 12px;
  --g-warm: rgba(255, 214, 122, 0.55);
  --g-cool: rgba(64, 224, 208, 0.5);
  --g-1: #4c1d95;
  --g-2: #7c2d8f;
  --g-3: #1e3a8a;
  --font-key: ui-sans-serif, system-ui, "Helvetica Neue", "Apple Symbols", sans-serif;
  background: radial-gradient(90% 70% at 18% 8%, var(--g-warm) 0%, rgba(255, 214, 122, 0) 60%), radial-gradient(80% 80% at 88% 22%, var(--g-cool) 0%, rgba(64, 224, 208, 0) 62%), linear-gradient(155deg, var(--g-1) 0%, var(--g-2) 42%, var(--g-3) 100%);
  color: var(--ink);
  font-family: var(--font-key);
  padding: 40px 18px;
}

.kbd-17__stage {
  display: grid;
  place-items: center;
  min-height: calc(100vh - 80px);
}

.kbd-17__panel {
  inline-size: 100%;
  max-inline-size: 27rem;
  min-inline-size: 0;
  padding: 26px 24px 20px;
  border-radius: 20px;
  background: rgba(255, 255, 255, 0.14);
  border: 1px solid rgba(255, 255, 255, 0.26);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.4), 0 24px 50px -24px rgba(20, 8, 40, 0.7);
}

@supports (backdrop-filter: blur(1px)) {
  .kbd-17__panel {
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(16px) saturate(150%);
  }
}

.kbd-17__eyebrow {
  margin: 0 0 20px;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.26em;
  text-transform: uppercase;
  color: var(--muted);
}

.kbd-17__rows {
  display: grid;
  gap: 2px;
}

.kbd-17__row {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding: 11px 0;
  border-bottom: 1px solid rgba(255, 255, 255, 0.16);
}

.kbd-17__row:last-child {
  border-bottom: 0;
}

.kbd-17__label {
  font-size: 14px;
  min-inline-size: 0;
  flex: 1 1 8rem;
}

.kbd-17__combo {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  flex-wrap: wrap;
  font-family: inherit;
  min-inline-size: 0;
}

.kbd-17__key {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-inline-size: 34px;
  min-block-size: 32px;
  padding: 0 9px;
  box-sizing: border-box;
  font-family: inherit;
  font-size: 14px;
  font-weight: 600;
  line-height: 1;
  color: var(--cap-ink);
  background: var(--cap-fallback);
  border: 1px solid var(--cap-border);
  border-radius: var(--radius);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.55), 0 6px 14px -8px rgba(12, 4, 30, 0.8);
  white-space: nowrap;
  transition: transform 120ms ease, background 160ms ease;
}

@supports (backdrop-filter: blur(1px)) {
  .kbd-17__key {
    background: var(--cap-glass);
    backdrop-filter: blur(10px) saturate(170%);
  }
}

.kbd-17__key--wide {
  min-inline-size: 88px;
  letter-spacing: 0.16em;
  font-size: 12px;
}

.kbd-17__key:hover {
  background: rgba(255, 255, 255, 0.28);
}

.kbd-17__key:active {
  transform: translateY(1px);
}

.kbd-17__sep {
  font-size: 12px;
  color: var(--muted);
  user-select: none;
}

.kbd-17__foot {
  margin: 18px 0 0;
  padding-top: 14px;
  border-top: 1px solid rgba(255, 255, 255, 0.16);
  font-size: 10.5px;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--muted);
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .kbd-17__key {
    transition: none;
  }
}

.kbd-17[data-theme="dark"],
[data-theme="dark"] .kbd-17 {
  --cap-fallback: rgba(255, 255, 255, 0.26);
  --cap-glass: rgba(255, 255, 255, 0.12);
  --cap-border: rgba(255, 255, 255, 0.34);
}
/* In-demo theme switch. State is one checkbox inside this demo, so the toggle
   themes THIS demo only — no root attribute, no script. */

.kbd-17__theme {
  position: absolute;
  inset-block-start: 14px;
  inset-inline-end: 16px;
  z-index: 5;
  display: flex;
}
/* the pill owns the top-right corner, so the stage reserves that band */

.kbd-17__stage {
  box-sizing: border-box;
  padding-block-start: 46px;
}

.kbd-17__themebox {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  pointer-events: none;
}

.kbd-17__themelabel {
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

.kbd-17__themedot {
  inline-size: 12px;
  block-size: 12px;
  flex: none;
  border-radius: 50%;
  background: currentColor;
}

.kbd-17__themebox:focus-visible + .kbd-17__themelabel {
  outline: 3px solid var(--accent, var(--cap-ink, currentColor));
  outline-offset: 2px;
}

@supports (border-color: color-mix(in oklab, currentColor 50%, transparent)) {
  .kbd-17__themelabel {
    border-color: color-mix(in oklab, currentColor 65%, transparent);
  }
}

.kbd-17__themeflip {
  display: none;
}

.kbd-17:has(.kbd-17__themebox:checked) {
  --ink: #1f1b3a;
  --muted: rgba(31, 27, 58, 0.66);
  --cap-fallback: rgba(255, 255, 255, 0.62);
  --cap-glass: rgba(255, 255, 255, 0.4);
  --cap-border: rgba(255, 255, 255, 0.78);
  --cap-ink: #241f52;
  --g-warm: rgba(255, 232, 180, 0.8);
  --g-cool: rgba(150, 240, 230, 0.75);
  --g-1: #c4b5fd;
  --g-2: #e0b5f5;
  --g-3: #a5c8fb;
}

.kbd-17:has(.kbd-17__themebox:checked) .kbd-17__themebase {
  display: none;
}

.kbd-17:has(.kbd-17__themebox:checked) .kbd-17__themeflip {
  display: inline;
}
/* The flip-back rule: on the opposite OS preference the unchecked state is the
   flipped palette, and checking the box returns to the demo's own default. */

@media (prefers-color-scheme: light) {
  .kbd-17:not(:has(.kbd-17__themebox:checked)) {
    --ink: #1f1b3a;
    --muted: rgba(31, 27, 58, 0.66);
    --cap-fallback: rgba(255, 255, 255, 0.62);
    --cap-glass: rgba(255, 255, 255, 0.4);
    --cap-border: rgba(255, 255, 255, 0.78);
    --cap-ink: #241f52;
    --g-warm: rgba(255, 232, 180, 0.8);
    --g-cool: rgba(150, 240, 230, 0.75);
    --g-1: #c4b5fd;
    --g-2: #e0b5f5;
    --g-3: #a5c8fb;
  }

  .kbd-17:has(.kbd-17__themebox:checked) {
    --ink: #f6f0ff;
    --muted: rgba(246, 240, 255, 0.62);
    --cap-fallback: rgba(255, 255, 255, 0.34);
    --cap-glass: rgba(255, 255, 255, 0.16);
    --cap-border: rgba(255, 255, 255, 0.42);
    --cap-ink: #ffffff;
    --g-warm: rgba(255, 214, 122, 0.55);
    --g-cool: rgba(64, 224, 208, 0.5);
    --g-1: #4c1d95;
    --g-2: #7c2d8f;
    --g-3: #1e3a8a;
  }

  .kbd-17:not(:has(.kbd-17__themebox:checked)) .kbd-17__themebase {
    display: none;
  }

  .kbd-17:not(:has(.kbd-17__themebox:checked)) .kbd-17__themeflip {
    display: inline;
  }

  .kbd-17:has(.kbd-17__themebox:checked) .kbd-17__themebase {
    display: inline;
  }

  .kbd-17:has(.kbd-17__themebox:checked) .kbd-17__themeflip {
    display: none;
  }
}
```
