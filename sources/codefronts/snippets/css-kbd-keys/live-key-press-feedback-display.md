---
source: "codefronts"
url: "https://codefronts.com/snippets/css-kbd-keys/live-key-press-feedback-display/"
title: "Live Key Press Feedback Display"
section: "snippets"
category: "css-kbd-keys"
category_name: "CSS Kbd Keys"
description: "The onboarding and screencast pattern: press a key and it appears on screen as a cap, then fades out on a timer."
has_js: "true"
---

Here's a working CSS Kbd Key from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Live Key Press Feedback Display
Source: https://codefronts.com/snippets/css-kbd-keys/live-key-press-feedback-display/

The onboarding and screencast pattern: press a key and it appears on screen as a cap, then fades out on a timer. Under twenty lines of script handle the three real traps — event.key is not event.code, modifier-only presses need their own labels, and holding a key fires repeat events that would otherwise flood the stack with duplicates.
## HTML
```html
<div class="kbd-15">
  <div class="kbd-15__stage">
    <button class="kbd-15__focus" type="button" id="kbd-15-focus">Click here, then press any key</button>
    <div class="kbd-15__display" id="kbd-15-display" aria-live="polite">
      <p class="kbd-15__idle" id="kbd-15-idle">waiting for input</p>
    </div>
    <p class="kbd-15__note">One cap per physical press · repeat events suppressed · labels come from event.key</p>
    <div class="kbd-15__theme">
      <input class="kbd-15__themebox" type="checkbox" id="kbd-15-theme">
      <label class="kbd-15__themelabel" for="kbd-15-theme">
        <span class="kbd-15__themedot" aria-hidden="true"></span>
        <span class="kbd-15__themebase">Dark</span><span class="kbd-15__themeflip">Light</span>
      </label>
    </div>
  </div>
</div>
```
## CSS
```css
.kbd-15 {
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  --page: #000000;
  --ink: #e9ffe9;
  --muted: #4e6b4e;
  --cap: #0b1a0b;
  --cap-border: #2c5c2c;
  --cap-ink: #b6ff8a;
  --accent: #86ff4d;
  --font-key: ui-monospace, "SFMono-Regular", Menlo, monospace;
  background: var(--page);
  color: var(--ink);
  font-family: var(--font-key);
  padding: 40px 18px;
}

.kbd-15__stage {
  display: grid;
  place-items: center;
  align-content: center;
  gap: 26px;
  min-height: calc(100vh - 80px);
}

.kbd-15__focus {
  min-block-size: 46px;
  min-inline-size: 44px;
  padding: 0 20px;
  font-family: inherit;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--accent);
  background: transparent;
  border: 1px solid var(--cap-border);
  border-radius: 6px;
  cursor: pointer;
  transition: background 150ms ease, box-shadow 150ms ease;
}

.kbd-15__focus:hover {
  background: rgba(134, 255, 77, 0.08);
}

.kbd-15__focus:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
  box-shadow: 0 0 24px -6px rgba(134, 255, 77, 0.6);
}

.kbd-15__display {
  inline-size: 100%;
  max-inline-size: 32rem;
  min-inline-size: 0;
  min-block-size: 108px;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
  gap: 10px;
  padding: 18px;
  box-sizing: border-box;
  border: 1px dashed var(--cap-border);
  border-radius: 10px;
}

.kbd-15__idle {
  margin: 0;
  font-size: 11px;
  letter-spacing: 0.24em;
  text-transform: uppercase;
  color: var(--muted);
}

.kbd-15__key {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-inline-size: 52px;
  min-block-size: 52px;
  padding: 0 14px;
  box-sizing: border-box;
  font-family: inherit;
  font-size: 20px;
  font-weight: 700;
  line-height: 1;
  color: var(--cap-ink);
  background: var(--cap);
  border: 1px solid var(--cap-border);
  border-radius: 12px;
  white-space: nowrap;
  box-shadow: inset 0 0 22px rgba(134, 255, 77, 0.16), 0 0 26px -8px rgba(134, 255, 77, 0.7);
  animation: kbd-15-pop 160ms cubic-bezier(0.2, 0.9, 0.3, 1) both, kbd-15-fade 260ms ease 940ms both;
}

.kbd-15__key--wide {
  font-size: 14px;
  letter-spacing: 0.06em;
}

@keyframes kbd-15-pop {
  from {
    transform: translateY(10px) scale(0.9);
    opacity: 0;
  }

  to {
    transform: translateY(0) scale(1);
    opacity: 1;
  }
}

@keyframes kbd-15-fade {
  to {
    opacity: 0;
    transform: translateY(-6px);
  }
}

.kbd-15__note {
  margin: 0;
  font-size: 10.5px;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--muted);
  text-align: center;
  min-inline-size: 0;
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .kbd-15__key {
    animation: kbd-15-fade 200ms ease 1000ms both;
  }

  .kbd-15__focus {
    transition: none;
  }
}

.kbd-15[data-theme="dark"],
[data-theme="dark"] .kbd-15 {
  --page: #000000;
  --accent: #86ff4d;
}
/* In-demo theme switch. State is one checkbox inside this demo, so the toggle
   themes THIS demo only — no root attribute, no script. */

.kbd-15__theme {
  position: absolute;
  inset-block-start: 14px;
  inset-inline-end: 16px;
  z-index: 5;
  display: flex;
}
/* the pill owns the top-right corner, so the stage reserves that band */

.kbd-15__stage {
  box-sizing: border-box;
  padding-block-start: 46px;
}

.kbd-15__themebox {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  pointer-events: none;
}

.kbd-15__themelabel {
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

.kbd-15__themedot {
  inline-size: 12px;
  block-size: 12px;
  flex: none;
  border-radius: 50%;
  background: currentColor;
}

.kbd-15__themebox:focus-visible + .kbd-15__themelabel {
  outline: 3px solid var(--accent, var(--cap-ink, currentColor));
  outline-offset: 2px;
}

@supports (border-color: color-mix(in oklab, currentColor 50%, transparent)) {
  .kbd-15__themelabel {
    border-color: color-mix(in oklab, currentColor 65%, transparent);
  }
}

.kbd-15__themeflip {
  display: none;
}

.kbd-15:has(.kbd-15__themebox:checked) {
  --page: #f2f6ef;
  --ink: #16240f;
  --muted: #5d7350;
  --cap: #ffffff;
  --cap-border: #b3cba3;
  --cap-ink: #1f5c14;
  --accent: #2f7d1c;
}

.kbd-15:has(.kbd-15__themebox:checked) .kbd-15__themebase {
  display: none;
}

.kbd-15:has(.kbd-15__themebox:checked) .kbd-15__themeflip {
  display: inline;
}

.kbd-15:has(.kbd-15__themebox:checked) .kbd-15__key {
  box-shadow: 0 1px 0 #b3cba3, 0 3px 8px -4px rgba(22, 36, 15, 0.4);
}

.kbd-15:has(.kbd-15__themebox:checked) .kbd-15__focus:focus-visible {
  box-shadow: none;
}
/* The flip-back rule: on the opposite OS preference the unchecked state is the
   flipped palette, and checking the box returns to the demo's own default. */

@media (prefers-color-scheme: light) {
  .kbd-15:not(:has(.kbd-15__themebox:checked)) {
    --page: #f2f6ef;
    --ink: #16240f;
    --muted: #5d7350;
    --cap: #ffffff;
    --cap-border: #b3cba3;
    --cap-ink: #1f5c14;
    --accent: #2f7d1c;
  }

  .kbd-15:has(.kbd-15__themebox:checked) {
    --page: #000000;
    --ink: #e9ffe9;
    --muted: #4e6b4e;
    --cap: #0b1a0b;
    --cap-border: #2c5c2c;
    --cap-ink: #b6ff8a;
    --accent: #86ff4d;
  }

  .kbd-15:not(:has(.kbd-15__themebox:checked)) .kbd-15__themebase {
    display: none;
  }

  .kbd-15:not(:has(.kbd-15__themebox:checked)) .kbd-15__themeflip {
    display: inline;
  }

  .kbd-15:has(.kbd-15__themebox:checked) .kbd-15__themebase {
    display: inline;
  }

  .kbd-15:has(.kbd-15__themebox:checked) .kbd-15__themeflip {
    display: none;
  }

  .kbd-15:not(:has(.kbd-15__themebox:checked)) .kbd-15__key {
    box-shadow: 0 1px 0 #b3cba3, 0 3px 8px -4px rgba(22, 36, 15, 0.4);
  }

  .kbd-15:has(.kbd-15__themebox:checked) .kbd-15__key {
    box-shadow: inset 0 0 22px rgba(134, 255, 77, 0.16), 0 0 26px -8px rgba(134, 255, 77, 0.7);
  }

  .kbd-15:not(:has(.kbd-15__themebox:checked)) .kbd-15__focus:focus-visible {
    box-shadow: none;
  }

  .kbd-15:has(.kbd-15__themebox:checked) .kbd-15__focus:focus-visible {
    box-shadow: 0 0 24px -6px rgba(134, 255, 77, 0.6);
  }
}
```

## JavaScript
```js
// event.key is the character the layout produced; event.code is the physical
// position. A display of what the user typed wants key. Repeat events are
// suppressed so holding a key does not flood the stack.
(function () {
  var display = document.getElementById('kbd-15-display');
  var idle = document.getElementById('kbd-15-idle');
  var btn = document.getElementById('kbd-15-focus');
  if (!display || !btn) return;
  var labels = { ' ': 'Space', Escape: 'Esc', ArrowUp: 'Up', ArrowDown: 'Down', ArrowLeft: 'Left', ArrowRight: 'Right' };
  btn.addEventListener('click', function () { btn.focus(); });
  document.addEventListener('keydown', function (e) {
    if (e.repeat) return;
    var text = labels[e.key] || (e.key.length === 1 ? e.key.toUpperCase() : e.key);
    if (idle) idle.remove(), idle = null;
    var cap = document.createElement('kbd');
    cap.className = 'kbd-15__key' + (text.length > 2 ? ' kbd-15__key--wide' : '');
    cap.textContent = text;
    display.appendChild(cap);
    while (display.childElementCount > 8) display.firstElementChild.remove();
    setTimeout(function () { cap.remove(); }, 1200);
  });
})();
```
