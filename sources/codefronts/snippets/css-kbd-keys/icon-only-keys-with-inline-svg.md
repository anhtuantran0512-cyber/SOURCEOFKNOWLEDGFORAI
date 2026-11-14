---
source: "codefronts"
url: "https://codefronts.com/snippets/css-kbd-keys/icon-only-keys-with-inline-svg/"
title: "Icon Only Keys with Inline SVG"
section: "snippets"
category: "css-kbd-keys"
category_name: "CSS Kbd Keys"
description: "Caps whose label is a mark rather than a word: search, escape, backspace, eject and power."
has_js: "false"
---

Here's a working CSS Kbd Key from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Icon Only Keys with Inline SVG
Source: https://codefronts.com/snippets/css-kbd-keys/icon-only-keys-with-inline-svg/

Caps whose label is a mark rather than a word: search, escape, backspace, eject and power. Every icon is inline SVG drawn with currentColor so it inherits the cap's ink, and every key pairs an aria-hidden graphic with visually hidden text, because an icon-only key with no accessible name is an unlabelled control.
## HTML
```html
<div class="kbd-10">
  <div class="kbd-10__stage">
    <section class="kbd-10__panel">
      <h2 class="kbd-10__h">Icon caps</h2>
      <div class="kbd-10__grid">
        <kbd class="kbd-10__key">
          <svg class="kbd-10__icon" viewBox="0 0 24 24" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5"/><path d="M15.5 15.5 L21 21"/></svg>
          <span class="kbd-10__vh">Search</span>
        </kbd>
        <kbd class="kbd-10__key">
          <svg class="kbd-10__icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M18 6 L6 18"/><path d="M6 18 L6 12"/><path d="M6 18 L12 18"/></svg>
          <span class="kbd-10__vh">Escape</span>
        </kbd>
        <kbd class="kbd-10__key">
          <svg class="kbd-10__icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 12 L6 12"/><path d="M11 7 L6 12 L11 17"/><path d="M20 5 L20 19"/></svg>
          <span class="kbd-10__vh">Backspace</span>
        </kbd>
        <kbd class="kbd-10__key">
          <svg class="kbd-10__icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4 L20 13 L4 13 Z"/><path d="M4 19 L20 19"/></svg>
          <span class="kbd-10__vh">Eject</span>
        </kbd>
        <kbd class="kbd-10__key">
          <svg class="kbd-10__icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3 L12 11"/><path d="M6.6 6.4 A 8 8 0 1 0 17.4 6.4"/></svg>
          <span class="kbd-10__vh">Power</span>
        </kbd>
      </div>
      <p class="kbd-10__note">Each cap pairs an <code class="kbd-10__code">aria-hidden</code> graphic with visually hidden text, so the announced name is a word even though the visible label is a mark.</p>
    </section>
    <div class="kbd-10__theme">
      <input class="kbd-10__themebox" type="checkbox" id="kbd-10-theme">
      <label class="kbd-10__themelabel" for="kbd-10-theme">
        <span class="kbd-10__themedot" aria-hidden="true"></span>
        <span class="kbd-10__themebase">Light</span><span class="kbd-10__themeflip">Dark</span>
      </label>
    </div>
  </div>
</div>
```
## CSS
```css
.kbd-10 {
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  --hue: 268;
  --page: hsl(var(--hue) 30% 96%);
  --panel: hsl(var(--hue) 34% 99%);
  --ink: hsl(var(--hue) 34% 18%);
  --muted: hsl(var(--hue) 14% 46%);
  --rule: hsl(var(--hue) 24% 89%);
  --cap: hsl(var(--hue) 30% 93%);
  --cap-ink: hsl(var(--hue) 52% 30%);
  --radius: 14px;
  --stroke: 1.7;
  --font-key: ui-sans-serif, system-ui, "Helvetica Neue", sans-serif;
  background: var(--page);
  color: var(--ink);
  font-family: var(--font-key);
  padding: 40px 18px;
}

.kbd-10__stage {
  display: grid;
  place-items: center;
  min-height: calc(100vh - 80px);
}

.kbd-10__panel {
  inline-size: 100%;
  max-inline-size: 29rem;
  min-inline-size: 0;
  background: var(--panel);
  border: 1px solid var(--rule);
  border-radius: 18px;
  padding: 26px 24px 22px;
}

.kbd-10__h {
  margin: 0 0 20px;
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: 0.26em;
  text-transform: uppercase;
  color: var(--muted);
}

.kbd-10__grid {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}

.kbd-10__key {
  inline-size: 54px;
  block-size: 54px;
  min-inline-size: 0;
  box-sizing: border-box;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 26px;
  color: var(--cap-ink);
  background: var(--cap);
  border: 0;
  border-radius: var(--radius);
  position: relative;
  transition: background 160ms ease, transform 120ms ease;
}

.kbd-10__key:hover {
  background: hsl(var(--hue) 34% 88%);
}

.kbd-10__key:active {
  transform: translateY(1px);
}

.kbd-10__icon {
  inline-size: 1em;
  block-size: 1em;
  display: block;
  fill: none;
  stroke: currentColor;
  stroke-width: var(--stroke);
  stroke-linecap: round;
  stroke-linejoin: round;
  vector-effect: non-scaling-stroke;
}

.kbd-10__vh {
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

.kbd-10__note {
  margin: 22px 0 0;
  padding-top: 16px;
  border-top: 1px solid var(--rule);
  font-size: 12.5px;
  line-height: 1.65;
  color: var(--muted);
  text-wrap: pretty;
}

.kbd-10__code {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.9em;
  color: var(--cap-ink);
  background: var(--cap);
  padding: 0.15em 0.35em;
  border-radius: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .kbd-10__key {
    transition: none;
  }
}

.kbd-10[data-theme="dark"],
[data-theme="dark"] .kbd-10 {
  --page: hsl(var(--hue) 26% 9%);
  --panel: hsl(var(--hue) 24% 13%);
  --ink: hsl(var(--hue) 22% 93%);
  --muted: hsl(var(--hue) 14% 62%);
  --rule: hsl(var(--hue) 20% 22%);
  --cap: hsl(var(--hue) 24% 20%);
  --cap-ink: hsl(var(--hue) 70% 82%);
}
/* In-demo theme switch. State is one checkbox inside this demo, so the toggle
   themes THIS demo only — no root attribute, no script. */

.kbd-10__theme {
  position: absolute;
  inset-block-start: 14px;
  inset-inline-end: 16px;
  z-index: 5;
  display: flex;
}
/* the pill owns the top-right corner, so the stage reserves that band */

.kbd-10__stage {
  box-sizing: border-box;
  padding-block-start: 46px;
}

.kbd-10__themebox {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  pointer-events: none;
}

.kbd-10__themelabel {
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

.kbd-10__themedot {
  inline-size: 12px;
  block-size: 12px;
  flex: none;
  border-radius: 50%;
  background: currentColor;
}

.kbd-10__themebox:focus-visible + .kbd-10__themelabel {
  outline: 3px solid var(--accent, var(--cap-ink, currentColor));
  outline-offset: 2px;
}

@supports (border-color: color-mix(in oklab, currentColor 50%, transparent)) {
  .kbd-10__themelabel {
    border-color: color-mix(in oklab, currentColor 65%, transparent);
  }
}

.kbd-10__themeflip {
  display: none;
}

.kbd-10:has(.kbd-10__themebox:checked) {
  --page: hsl(var(--hue) 26% 9%);
  --panel: hsl(var(--hue) 24% 13%);
  --ink: hsl(var(--hue) 22% 93%);
  --muted: hsl(var(--hue) 14% 62%);
  --rule: hsl(var(--hue) 20% 22%);
  --cap: hsl(var(--hue) 24% 20%);
  --cap-ink: hsl(var(--hue) 70% 82%);
}

.kbd-10:has(.kbd-10__themebox:checked) .kbd-10__themebase {
  display: none;
}

.kbd-10:has(.kbd-10__themebox:checked) .kbd-10__themeflip {
  display: inline;
}

.kbd-10:has(.kbd-10__themebox:checked) .kbd-10__key:hover {
  background: hsl(var(--hue) 26% 26%);
}
/* The flip-back rule: on the opposite OS preference the unchecked state is the
   flipped palette, and checking the box returns to the demo's own default. */

@media (prefers-color-scheme: dark) {
  .kbd-10:not(:has(.kbd-10__themebox:checked)) {
    --page: hsl(var(--hue) 26% 9%);
    --panel: hsl(var(--hue) 24% 13%);
    --ink: hsl(var(--hue) 22% 93%);
    --muted: hsl(var(--hue) 14% 62%);
    --rule: hsl(var(--hue) 20% 22%);
    --cap: hsl(var(--hue) 24% 20%);
    --cap-ink: hsl(var(--hue) 70% 82%);
  }

  .kbd-10:has(.kbd-10__themebox:checked) {
    --page: hsl(var(--hue) 30% 96%);
    --panel: hsl(var(--hue) 34% 99%);
    --ink: hsl(var(--hue) 34% 18%);
    --muted: hsl(var(--hue) 14% 46%);
    --rule: hsl(var(--hue) 24% 89%);
    --cap: hsl(var(--hue) 30% 93%);
    --cap-ink: hsl(var(--hue) 52% 30%);
  }

  .kbd-10:not(:has(.kbd-10__themebox:checked)) .kbd-10__themebase {
    display: none;
  }

  .kbd-10:not(:has(.kbd-10__themebox:checked)) .kbd-10__themeflip {
    display: inline;
  }

  .kbd-10:has(.kbd-10__themebox:checked) .kbd-10__themebase {
    display: inline;
  }

  .kbd-10:has(.kbd-10__themebox:checked) .kbd-10__themeflip {
    display: none;
  }

  .kbd-10:not(:has(.kbd-10__themebox:checked)) .kbd-10__key:hover {
    background: hsl(var(--hue) 26% 26%);
  }

  .kbd-10:has(.kbd-10__themebox:checked) .kbd-10__key:hover {
    background: hsl(var(--hue) 34% 88%);
  }
}
```
