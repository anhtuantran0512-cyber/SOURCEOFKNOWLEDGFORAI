---
source: "codefronts"
url: "https://codefronts.com/snippets/css-kbd-keys/auto-os-detect-cmd-or-ctrl-display/"
title: "Auto OS Detect Cmd or Ctrl Display"
section: "snippets"
category: "css-kbd-keys"
category_name: "CSS Kbd Keys"
description: "Detect the platform once, write it to a data attribute on the demo root, and let attribute selectors style every key on the page from that single value."
has_js: "false"
---

Here's a working CSS Kbd Key from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Auto OS Detect Cmd or Ctrl Display
Source: https://codefronts.com/snippets/css-kbd-keys/auto-os-detect-cmd-or-ctrl-display/

Detect the platform once, write it to a data attribute on the demo root, and let attribute selectors style every key on the page from that single value. Nine lines of script replace a per-key conditional, and if the script never runs the markup still renders a complete Windows-labelled list rather than an empty one.
## HTML
```html
<div class="kbd-08" id="kbd-08-root">
  <div class="kbd-08__stage">
    <section class="kbd-08__panel">
      <p class="kbd-08__eyebrow">Detected platform</p>
      <p class="kbd-08__os"><span class="kbd-08__mac">macOS</span><span class="kbd-08__win">Windows / Linux</span></p>
      <ul class="kbd-08__list">
        <li class="kbd-08__row">
          <span class="kbd-08__action">Go to file</span>
          <kbd class="kbd-08__combo"><kbd class="kbd-08__key"><span class="kbd-08__mac">⌘</span><span class="kbd-08__win">Ctrl</span></kbd><span class="kbd-08__sep" aria-hidden="true">+</span><kbd class="kbd-08__key">P</kbd></kbd>
        </li>
        <li class="kbd-08__row">
          <span class="kbd-08__action">Find in project</span>
          <kbd class="kbd-08__combo"><kbd class="kbd-08__key"><span class="kbd-08__mac">⇧</span><span class="kbd-08__win">Shift</span></kbd><span class="kbd-08__sep" aria-hidden="true">+</span><kbd class="kbd-08__key"><span class="kbd-08__mac">⌘</span><span class="kbd-08__win">Ctrl</span></kbd><span class="kbd-08__sep" aria-hidden="true">+</span><kbd class="kbd-08__key">F</kbd></kbd>
        </li>
        <li class="kbd-08__row">
          <span class="kbd-08__action">Comment line</span>
          <kbd class="kbd-08__combo"><kbd class="kbd-08__key"><span class="kbd-08__mac">⌘</span><span class="kbd-08__win">Ctrl</span></kbd><span class="kbd-08__sep" aria-hidden="true">+</span><kbd class="kbd-08__key">Slash</kbd></kbd>
        </li>
        <li class="kbd-08__row">
          <span class="kbd-08__action">Rename symbol</span>
          <kbd class="kbd-08__combo"><kbd class="kbd-08__key">F2</kbd></kbd>
        </li>
      </ul>
      <p class="kbd-08__foot">One attribute on the root · every key reads from it</p>
    </section>
    <div class="kbd-08__theme">
      <input class="kbd-08__themebox" type="checkbox" id="kbd-08-theme">
      <label class="kbd-08__themelabel" for="kbd-08-theme">
        <span class="kbd-08__themedot" aria-hidden="true"></span>
        <span class="kbd-08__themebase">Dark</span><span class="kbd-08__themeflip">Light</span>
      </label>
    </div>
  </div>
</div>
```
## CSS
```css
.kbd-08 {
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  --page: #000000;
  --panel: #08090c;
  --ink: #e6f7ff;
  --muted: #5f7080;
  --rule: #161c24;
  --cap: #0d1116;
  --cap-border: #1d2a35;
  --cap-ink: #d6f2ff;
  --accent: #22d3ee;
  --font-key: ui-monospace, "SFMono-Regular", Menlo, monospace;
  background: var(--page);
  color: var(--ink);
  font-family: var(--font-key);
  padding: 40px 18px;
}

.kbd-08__stage {
  display: grid;
  place-items: center;
  min-height: calc(100vh - 80px);
}

.kbd-08__panel {
  inline-size: 100%;
  max-inline-size: 29rem;
  min-inline-size: 0;
  background: var(--panel);
  border: 1px solid var(--rule);
  border-radius: 6px;
  padding: 24px 22px 20px;
  box-shadow: 0 0 0 1px rgba(34, 211, 238, 0.08), 0 0 40px -14px rgba(34, 211, 238, 0.35);
}

.kbd-08__eyebrow {
  margin: 0 0 6px;
  font-size: 9.5px;
  letter-spacing: 0.3em;
  text-transform: uppercase;
  color: var(--muted);
}

.kbd-08__os {
  margin: 0 0 20px;
  font-size: 20px;
  font-weight: 700;
  letter-spacing: -0.01em;
  color: var(--accent);
  text-shadow: 0 0 18px rgba(34, 211, 238, 0.45);
}

.kbd-08__mac {
  display: none;
}

.kbd-08[data-os="mac"] .kbd-08__mac {
  display: inline;
}

.kbd-08[data-os="mac"] .kbd-08__win {
  display: none;
}

.kbd-08__list {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: 1px;
}

.kbd-08__row {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  padding: 11px 0;
  border-bottom: 1px solid var(--rule);
}

.kbd-08__row:last-child {
  border-bottom: 0;
}

.kbd-08__action {
  font-size: 13px;
  letter-spacing: 0.01em;
  min-inline-size: 0;
  flex: 1 1 9rem;
  color: var(--ink);
}

.kbd-08__combo {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  flex-wrap: wrap;
  font-family: inherit;
  min-inline-size: 0;
}

.kbd-08__key {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-inline-size: 28px;
  min-block-size: 26px;
  padding: 0 7px;
  box-sizing: border-box;
  font-family: inherit;
  font-size: 12px;
  font-weight: 600;
  line-height: 1;
  color: var(--cap-ink);
  background: var(--cap);
  border: 1px solid var(--cap-border);
  border-radius: 4px;
  box-shadow: inset 0 0 12px rgba(34, 211, 238, 0.14), 0 0 8px -2px rgba(34, 211, 238, 0.3);
  white-space: nowrap;
}

.kbd-08__sep {
  font-size: 11px;
  color: var(--muted);
  user-select: none;
}

.kbd-08__foot {
  margin: 18px 0 0;
  padding-top: 14px;
  border-top: 1px solid var(--rule);
  font-size: 10.5px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--muted);
}

.kbd-08[data-theme="dark"],
[data-theme="dark"] .kbd-08 {
  --page: #000000;
  --panel: #06070a;
  --accent: #22d3ee;
}
/* In-demo theme switch. State is one checkbox inside this demo, so the toggle
   themes THIS demo only — no root attribute, no script. */

.kbd-08__theme {
  position: absolute;
  inset-block-start: 14px;
  inset-inline-end: 16px;
  z-index: 5;
  display: flex;
}
/* the pill owns the top-right corner, so the stage reserves that band */

.kbd-08__stage {
  box-sizing: border-box;
  padding-block-start: 46px;
}

.kbd-08__themebox {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  pointer-events: none;
}

.kbd-08__themelabel {
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

.kbd-08__themedot {
  inline-size: 12px;
  block-size: 12px;
  flex: none;
  border-radius: 50%;
  background: currentColor;
}

.kbd-08__themebox:focus-visible + .kbd-08__themelabel {
  outline: 3px solid var(--accent, var(--cap-ink, currentColor));
  outline-offset: 2px;
}

@supports (border-color: color-mix(in oklab, currentColor 50%, transparent)) {
  .kbd-08__themelabel {
    border-color: color-mix(in oklab, currentColor 65%, transparent);
  }
}

.kbd-08__themeflip {
  display: none;
}

.kbd-08:has(.kbd-08__themebox:checked) {
  --page: #eef4f7;
  --panel: #ffffff;
  --ink: #0d1b22;
  --muted: #5a707c;
  --rule: #d6e2e8;
  --cap: #f2f8fb;
  --cap-border: #bed3dc;
  --cap-ink: #0f3f4d;
  --accent: #0e7490;
}

.kbd-08:has(.kbd-08__themebox:checked) .kbd-08__themebase {
  display: none;
}

.kbd-08:has(.kbd-08__themebox:checked) .kbd-08__themeflip {
  display: inline;
}

.kbd-08:has(.kbd-08__themebox:checked) .kbd-08__panel {
  box-shadow: 0 1px 2px rgba(13, 27, 34, 0.06), 0 10px 30px -20px rgba(13, 27, 34, 0.4);
}

.kbd-08:has(.kbd-08__themebox:checked) .kbd-08__key {
  box-shadow: 0 1px 0 #bed3dc;
}

.kbd-08:has(.kbd-08__themebox:checked) .kbd-08__os {
  text-shadow: none;
}
/* The flip-back rule: on the opposite OS preference the unchecked state is the
   flipped palette, and checking the box returns to the demo's own default. */

@media (prefers-color-scheme: light) {
  .kbd-08:not(:has(.kbd-08__themebox:checked)) {
    --page: #eef4f7;
    --panel: #ffffff;
    --ink: #0d1b22;
    --muted: #5a707c;
    --rule: #d6e2e8;
    --cap: #f2f8fb;
    --cap-border: #bed3dc;
    --cap-ink: #0f3f4d;
    --accent: #0e7490;
  }

  .kbd-08:has(.kbd-08__themebox:checked) {
    --page: #000000;
    --panel: #08090c;
    --ink: #e6f7ff;
    --muted: #5f7080;
    --rule: #161c24;
    --cap: #0d1116;
    --cap-border: #1d2a35;
    --cap-ink: #d6f2ff;
    --accent: #22d3ee;
  }

  .kbd-08:not(:has(.kbd-08__themebox:checked)) .kbd-08__themebase {
    display: none;
  }

  .kbd-08:not(:has(.kbd-08__themebox:checked)) .kbd-08__themeflip {
    display: inline;
  }

  .kbd-08:has(.kbd-08__themebox:checked) .kbd-08__themebase {
    display: inline;
  }

  .kbd-08:has(.kbd-08__themebox:checked) .kbd-08__themeflip {
    display: none;
  }

  .kbd-08:not(:has(.kbd-08__themebox:checked)) .kbd-08__panel {
    box-shadow: 0 1px 2px rgba(13, 27, 34, 0.06), 0 10px 30px -20px rgba(13, 27, 34, 0.4);
  }

  .kbd-08:has(.kbd-08__themebox:checked) .kbd-08__panel {
    box-shadow: 0 0 0 1px rgba(34, 211, 238, 0.08), 0 0 40px -14px rgba(34, 211, 238, 0.35);
  }

  .kbd-08:not(:has(.kbd-08__themebox:checked)) .kbd-08__key {
    box-shadow: 0 1px 0 #bed3dc;
  }

  .kbd-08:has(.kbd-08__themebox:checked) .kbd-08__key {
    box-shadow: inset 0 0 12px rgba(34, 211, 238, 0.14), 0 0 8px -2px rgba(34, 211, 238, 0.3);
  }

  .kbd-08:not(:has(.kbd-08__themebox:checked)) .kbd-08__os {
    text-shadow: none;
  }

  .kbd-08:has(.kbd-08__themebox:checked) .kbd-08__os {
    text-shadow: 0 0 18px rgba(34, 211, 238, 0.45);
  }
}
```

## JavaScript
```js
// Presentation hint only — a platform string is spoofable and is never a
// capability or security signal. Feature-detect anything that matters.
(function () {
  var root = document.getElementById('kbd-08-root');
  if (!root) return;
  var plat = (navigator.userAgentData && navigator.userAgentData.platform) || navigator.platform || '';
  var isMac = /mac|iphone|ipad|ipod/i.test(plat);
  root.setAttribute('data-os', isMac ? 'mac' : 'win');
})();
```
