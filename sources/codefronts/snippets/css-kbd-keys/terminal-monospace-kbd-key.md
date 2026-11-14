---
source: "codefronts"
url: "https://codefronts.com/snippets/css-kbd-keys/terminal-monospace-kbd-key/"
title: "Terminal Monospace Kbd Key"
section: "snippets"
category: "css-kbd-keys"
category_name: "CSS Kbd Keys"
description: "Dev-tool treatment: monospace labels in phosphor green on near-black, square corners, and a faint scanline wash over the panel."
has_js: "false"
---

Here's a working CSS Kbd Key from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Terminal Monospace Kbd Key
Source: https://codefronts.com/snippets/css-kbd-keys/terminal-monospace-kbd-key/

Dev-tool treatment: monospace labels in phosphor green on near-black, square corners, and a faint scanline wash over the panel. The key reads as terminal output rather than as a physical object, which is the point — this is the register for CLI docs, REPL help screens and debugger overlays where a plastic cap would look out of place.
## HTML
```html
<div class="kbd-19">
  <div class="kbd-19__stage">
    <section class="kbd-19__term">
      <p class="kbd-19__prompt"><span class="kbd-19__dollar">$</span> atlas --help keys</p>
      <dl class="kbd-19__list">
        <div class="kbd-19__row"><dt class="kbd-19__dt"><kbd class="kbd-19__combo"><kbd class="kbd-19__key">Ctrl</kbd><span class="kbd-19__sep" aria-hidden="true">+</span><kbd class="kbd-19__key">C</kbd></kbd></dt><dd class="kbd-19__dd">send SIGINT to the foreground job</dd></div>
        <div class="kbd-19__row"><dt class="kbd-19__dt"><kbd class="kbd-19__combo"><kbd class="kbd-19__key">Ctrl</kbd><span class="kbd-19__sep" aria-hidden="true">+</span><kbd class="kbd-19__key">D</kbd></kbd></dt><dd class="kbd-19__dd">end of input, close the session</dd></div>
        <div class="kbd-19__row"><dt class="kbd-19__dt"><kbd class="kbd-19__combo"><kbd class="kbd-19__key">Ctrl</kbd><span class="kbd-19__sep" aria-hidden="true">+</span><kbd class="kbd-19__key">R</kbd></kbd></dt><dd class="kbd-19__dd">reverse search through history</dd></div>
        <div class="kbd-19__row"><dt class="kbd-19__dt"><kbd class="kbd-19__combo"><kbd class="kbd-19__key">Ctrl</kbd><span class="kbd-19__sep" aria-hidden="true">+</span><kbd class="kbd-19__key">L</kbd></kbd></dt><dd class="kbd-19__dd">clear the screen, keep the buffer</dd></div>
        <div class="kbd-19__row"><dt class="kbd-19__dt"><kbd class="kbd-19__combo"><kbd class="kbd-19__key">Ctrl</kbd><span class="kbd-19__sep" aria-hidden="true">+</span><kbd class="kbd-19__key">Z</kbd></kbd></dt><dd class="kbd-19__dd">suspend, resume with fg</dd></div>
        <div class="kbd-19__row"><dt class="kbd-19__dt"><kbd class="kbd-19__combo"><kbd class="kbd-19__key">Tab</kbd><span class="kbd-19__sep kbd-19__sep--x2" aria-hidden="true">x2</span></kbd></dt><dd class="kbd-19__dd">list every completion candidate</dd></div>
      </dl>
      <p class="kbd-19__cursor"><span class="kbd-19__dollar">$</span> <span class="kbd-19__caret" aria-hidden="true"></span></p>
    </section>
    <div class="kbd-19__theme">
      <input class="kbd-19__themebox" type="checkbox" id="kbd-19-theme">
      <label class="kbd-19__themelabel" for="kbd-19-theme">
        <span class="kbd-19__themedot" aria-hidden="true"></span>
        <span class="kbd-19__themebase">Dark</span><span class="kbd-19__themeflip">Light</span>
      </label>
    </div>
  </div>
</div>
```
## CSS
```css
.kbd-19 {
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  --page: #07090a;
  --term: #0b0f10;
  --ink: #b9c9be;
  --muted: #5d7566;
  --rule: #16211a;
  --cap: #111917;
  --cap-border: #2b463a;
  --cap-ink: #7dfaa8;
  --accent: #38f88f;
  --font-key: ui-monospace, "SFMono-Regular", "JetBrains Mono", Menlo, monospace;
  background: var(--page);
  color: var(--ink);
  font-family: var(--font-key);
  padding: 40px 16px;
}

.kbd-19__stage {
  display: grid;
  place-items: center;
  min-height: calc(100vh - 80px);
}

.kbd-19__term {
  position: relative;
  inline-size: 100%;
  max-inline-size: 34rem;
  min-inline-size: 0;
  background: var(--term);
  border: 1px solid var(--rule);
  padding: 20px 18px 16px;
  overflow: hidden;
}

.kbd-19__term::before {
  content: "";
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(0deg, rgba(120, 255, 180, 0.045) 0 1px, rgba(120, 255, 180, 0) 1px 3px);
  pointer-events: none;
}

.kbd-19__prompt {
  margin: 0 0 16px;
  font-size: 12.5px;
  letter-spacing: 0.02em;
  color: var(--ink);
  position: relative;
}

.kbd-19__dollar {
  color: var(--accent);
}

.kbd-19__list {
  margin: 0;
  display: grid;
  gap: 0;
  position: relative;
}

.kbd-19__row {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 12px;
  min-block-size: 26px;
  padding: 3px 0;
  border-bottom: 1px solid var(--rule);
}

.kbd-19__row:last-child {
  border-bottom: 0;
}

.kbd-19__dt {
  margin: 0;
  inline-size: 11ch;
  flex: none;
  min-inline-size: 0;
}

.kbd-19__dd {
  margin: 0;
  font-size: 12px;
  line-height: 1.5;
  color: var(--muted);
  min-inline-size: 0;
  flex: 1 1 12ch;
}

.kbd-19__combo {
  display: inline-flex;
  align-items: center;
  gap: 3px;
  font-family: inherit;
}

.kbd-19__key {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-inline-size: 2ch;
  padding: 3px 5px;
  box-sizing: border-box;
  font-family: inherit;
  font-size: 11.5px;
  font-weight: 500;
  line-height: 1;
  color: var(--cap-ink);
  background: var(--cap);
  border: 1px solid var(--cap-border);
  border-radius: 0;
  text-shadow: 0 0 8px rgba(56, 248, 143, 0.4);
  white-space: nowrap;
}

.kbd-19__sep {
  font-size: 11px;
  color: var(--muted);
  user-select: none;
}

.kbd-19__sep--x2 {
  color: var(--accent);
  font-size: 10px;
}

.kbd-19__cursor {
  margin: 16px 0 0;
  padding-top: 12px;
  border-top: 1px solid var(--rule);
  font-size: 12.5px;
  position: relative;
}

.kbd-19__caret {
  display: inline-block;
  inline-size: 1ch;
  block-size: 1.05em;
  background: var(--accent);
  vertical-align: -0.16em;
  animation: kbd-19-blink 1.1s steps(1, end) infinite;
}

@keyframes kbd-19-blink {
  0%,
    49% {
    opacity: 1;
  }

  50%,
    100% {
    opacity: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .kbd-19__caret {
    animation: none;
    opacity: 1;
  }
}

.kbd-19[data-theme="dark"],
[data-theme="dark"] .kbd-19 {
  --page: #050708;
  --term: #090d0e;
  --ink: #b9c9be;
  --muted: #5d7566;
  --rule: #16211a;
  --cap: #111917;
  --cap-border: #2b463a;
  --cap-ink: #7dfaa8;
  --accent: #38f88f;
}
/* In-demo theme switch. State is one checkbox inside this demo, so the toggle
   themes THIS demo only — no root attribute, no script. */

.kbd-19__theme {
  position: absolute;
  inset-block-start: 14px;
  inset-inline-end: 16px;
  z-index: 5;
  display: flex;
}
/* the pill owns the top-right corner, so the stage reserves that band */

.kbd-19__stage {
  box-sizing: border-box;
  padding-block-start: 46px;
}

.kbd-19__themebox {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  pointer-events: none;
}

.kbd-19__themelabel {
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

.kbd-19__themedot {
  inline-size: 12px;
  block-size: 12px;
  flex: none;
  border-radius: 50%;
  background: currentColor;
}

.kbd-19__themebox:focus-visible + .kbd-19__themelabel {
  outline: 3px solid var(--accent, var(--cap-ink, currentColor));
  outline-offset: 2px;
}

@supports (border-color: color-mix(in oklab, currentColor 50%, transparent)) {
  .kbd-19__themelabel {
    border-color: color-mix(in oklab, currentColor 65%, transparent);
  }
}

.kbd-19__themeflip {
  display: none;
}

.kbd-19:has(.kbd-19__themebox:checked) {
  --page: #e8ebe6;
  --term: #f7f9f5;
  --ink: #23302a;
  --muted: #5a6d61;
  --rule: #d3dcd4;
  --cap: #eaf2eb;
  --cap-border: #a9c4b1;
  --cap-ink: #0e5c34;
  --accent: #0b7a43;
}

.kbd-19:has(.kbd-19__themebox:checked) .kbd-19__themebase {
  display: none;
}

.kbd-19:has(.kbd-19__themebox:checked) .kbd-19__themeflip {
  display: inline;
}

.kbd-19:has(.kbd-19__themebox:checked) .kbd-19__term::before {
  background: repeating-linear-gradient(0deg, rgba(20, 80, 45, 0.035) 0 1px, rgba(20, 80, 45, 0) 1px 3px);
}

.kbd-19:has(.kbd-19__themebox:checked) .kbd-19__key {
  text-shadow: none;
}
/* The flip-back rule: on the opposite OS preference the unchecked state is the
   flipped palette, and checking the box returns to the demo's own default. */

@media (prefers-color-scheme: light) {
  .kbd-19:not(:has(.kbd-19__themebox:checked)) {
    --page: #e8ebe6;
    --term: #f7f9f5;
    --ink: #23302a;
    --muted: #5a6d61;
    --rule: #d3dcd4;
    --cap: #eaf2eb;
    --cap-border: #a9c4b1;
    --cap-ink: #0e5c34;
    --accent: #0b7a43;
  }

  .kbd-19:has(.kbd-19__themebox:checked) {
    --page: #07090a;
    --term: #0b0f10;
    --ink: #b9c9be;
    --muted: #5d7566;
    --rule: #16211a;
    --cap: #111917;
    --cap-border: #2b463a;
    --cap-ink: #7dfaa8;
    --accent: #38f88f;
  }

  .kbd-19:not(:has(.kbd-19__themebox:checked)) .kbd-19__themebase {
    display: none;
  }

  .kbd-19:not(:has(.kbd-19__themebox:checked)) .kbd-19__themeflip {
    display: inline;
  }

  .kbd-19:has(.kbd-19__themebox:checked) .kbd-19__themebase {
    display: inline;
  }

  .kbd-19:has(.kbd-19__themebox:checked) .kbd-19__themeflip {
    display: none;
  }

  .kbd-19:not(:has(.kbd-19__themebox:checked)) .kbd-19__term::before {
    background: repeating-linear-gradient(0deg, rgba(20, 80, 45, 0.035) 0 1px, rgba(20, 80, 45, 0) 1px 3px);
  }

  .kbd-19:has(.kbd-19__themebox:checked) .kbd-19__term::before {
    background: repeating-linear-gradient(0deg, rgba(120, 255, 180, 0.045) 0 1px, rgba(120, 255, 180, 0) 1px 3px);
  }

  .kbd-19:not(:has(.kbd-19__themebox:checked)) .kbd-19__key {
    text-shadow: none;
  }

  .kbd-19:has(.kbd-19__themebox:checked) .kbd-19__key {
    text-shadow: 0 0 8px rgba(56, 248, 143, 0.4);
  }
}
```
