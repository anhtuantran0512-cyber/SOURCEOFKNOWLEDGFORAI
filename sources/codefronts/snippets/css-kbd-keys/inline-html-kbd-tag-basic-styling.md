---
source: "codefronts"
url: "https://codefronts.com/snippets/css-kbd-keys/inline-html-kbd-tag-basic-styling/"
title: "Inline HTML Kbd Tag Basic Styling"
section: "snippets"
category: "css-kbd-keys"
category_name: "CSS Kbd Keys"
description: "The reference treatment the rest of the collection builds on: the kbd element styled as a small cap that sits inside a real paragraph of documentation…"
has_js: "false"
---

Here's a working CSS Kbd Key from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Inline HTML Kbd Tag Basic Styling
Source: https://codefronts.com/snippets/css-kbd-keys/inline-html-kbd-tag-basic-styling/

The reference treatment the rest of the collection builds on: the kbd element styled as a small cap that sits inside a real paragraph of documentation without disturbing the line it lives on. A hairline border plus a one-pixel bottom edge reads as key depth, and the label is set slightly smaller than the surrounding prose so the cap optically matches the x-height of the text around it.
## HTML
```html
<div class="kbd-01">
  <div class="kbd-01__stage">
    <article class="kbd-01__doc">
      <p class="kbd-01__eyebrow">Editor · Keyboard</p>
      <h2 class="kbd-01__h">Saving, undoing, escaping</h2>
      <p class="kbd-01__p">Your work is written to disk the moment you press <kbd class="kbd-01__key">Ctrl</kbd> <span class="kbd-01__plus">+</span> <kbd class="kbd-01__key">S</kbd>, and there is no separate confirm step. If an edit turns out wrong, <kbd class="kbd-01__key">Ctrl</kbd> <span class="kbd-01__plus">+</span> <kbd class="kbd-01__key">Z</kbd> walks back through the history one change at a time; <kbd class="kbd-01__key">Esc</kbd> closes whichever panel is in the way first.</p>
      <p class="kbd-01__p">Every key above is a real <code class="kbd-01__code">&lt;kbd&gt;</code> element sitting in ordinary prose. Notice that the lines stay evenly spaced: the cap has <code class="kbd-01__code">line-height: 1</code>, so it never inflates the line box it lives in.</p>
      <dl class="kbd-01__anatomy">
        <div class="kbd-01__row"><dt class="kbd-01__dt">Border</dt><dd class="kbd-01__dd">One hairline, one tone darker than the cap face</dd></div>
        <div class="kbd-01__row"><dt class="kbd-01__dt">Edge</dt><dd class="kbd-01__dd">A single 1px bottom shadow, no blur</dd></div>
        <div class="kbd-01__row"><dt class="kbd-01__dt">Label</dt><dd class="kbd-01__dd">0.82em of the surrounding text, never below 11px</dd></div>
      </dl>
    </article>
    <div class="kbd-01__theme">
      <input class="kbd-01__themebox" type="checkbox" id="kbd-01-theme">
      <label class="kbd-01__themelabel" for="kbd-01-theme">
        <span class="kbd-01__themedot" aria-hidden="true"></span>
        <span class="kbd-01__themebase">Light</span><span class="kbd-01__themeflip">Dark</span>
      </label>
    </div>
  </div>
</div>
```
## CSS
```css
.kbd-01 {
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  --paper: #faf7f1;
  --ink: #221e18;
  --muted: #7c7264;
  --rule: #e2dbcd;
  --cap: #ffffff;
  --cap-border: #cfc7b6;
  --cap-edge: #bdb3a0;
  --cap-ink: #332d24;
  --radius: 5px;
  --key-size: 0.82em;
  --font-key: ui-sans-serif, system-ui, "Helvetica Neue", sans-serif;
  --font-body: Georgia, "Iowan Old Style", "Times New Roman", serif;
  background: var(--paper);
  color: var(--ink);
  padding: 40px 20px;
}

.kbd-01__stage {
  display: grid;
  place-items: center;
  min-height: calc(100vh - 80px);
}

.kbd-01__doc {
  inline-size: 100%;
  max-inline-size: 33rem;
  min-inline-size: 0;
}

.kbd-01__eyebrow {
  margin: 0 0 10px;
  font: 600 10px/1 var(--font-key);
  letter-spacing: 0.24em;
  text-transform: uppercase;
  color: var(--muted);
}

.kbd-01__h {
  margin: 0 0 18px;
  font: 400 clamp(24px, 5vw, 33px)/1.15 var(--font-body);
  letter-spacing: -0.015em;
}

.kbd-01__p {
  margin: 0 0 16px;
  font: 400 clamp(15px, 3.4vw, 17px)/1.75 var(--font-body);
  text-wrap: pretty;
}

.kbd-01__key {
  display: inline-block;
  padding: 0.28em 0.55em;
  min-inline-size: 1.1em;
  font-family: var(--font-key);
  font-size: var(--key-size);
  font-weight: 600;
  line-height: 1;
  text-align: center;
  color: var(--cap-ink);
  background: var(--cap);
  border: 1px solid var(--cap-border);
  border-radius: var(--radius);
  box-shadow: 0 1px 0 var(--cap-edge);
  vertical-align: 0.06em;
  white-space: nowrap;
}

.kbd-01__plus {
  font-family: var(--font-key);
  font-size: 0.78em;
  color: var(--muted);
  padding: 0 0.05em;
}

.kbd-01__code {
  font: 0.86em/1 ui-monospace, "SFMono-Regular", Menlo, monospace;
  background: rgba(124, 114, 100, 0.12);
  padding: 0.2em 0.35em;
  border-radius: 3px;
}

.kbd-01__anatomy {
  margin: 26px 0 0;
  padding-top: 18px;
  border-top: 1px solid var(--rule);
  display: grid;
  gap: 10px;
}

.kbd-01__row {
  display: grid;
  grid-template-columns: 5.5rem 1fr;
  gap: 12px;
  align-items: baseline;
}

.kbd-01__dt {
  margin: 0;
  font: 600 10px/1.4 var(--font-key);
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--muted);
  min-inline-size: 0;
}

.kbd-01__dd {
  margin: 0;
  font: 400 14px/1.5 var(--font-body);
  min-inline-size: 0;
}

@media (max-width: 380px) {
  .kbd-01__row {
    grid-template-columns: 1fr;
    gap: 2px;
  }
}

.kbd-01[data-theme="dark"],
[data-theme="dark"] .kbd-01 {
  --paper: #17150f;
  --ink: #f2ede1;
  --muted: #9a9080;
  --rule: #322d23;
  --cap: #2a251c;
  --cap-border: #4a4232;
  --cap-edge: #100e09;
  --cap-ink: #f6f1e5;
}
/* In-demo theme switch. State is one checkbox inside this demo, so the toggle
   themes THIS demo only — no root attribute, no script. */

.kbd-01__theme {
  position: absolute;
  inset-block-start: 14px;
  inset-inline-end: 16px;
  z-index: 5;
  display: flex;
}
/* the pill owns the top-right corner, so the stage reserves that band */

.kbd-01__stage {
  box-sizing: border-box;
  padding-block-start: 46px;
}

.kbd-01__themebox {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  pointer-events: none;
}

.kbd-01__themelabel {
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

.kbd-01__themedot {
  inline-size: 12px;
  block-size: 12px;
  flex: none;
  border-radius: 50%;
  background: currentColor;
}

.kbd-01__themebox:focus-visible + .kbd-01__themelabel {
  outline: 3px solid var(--accent, var(--cap-ink, currentColor));
  outline-offset: 2px;
}

@supports (border-color: color-mix(in oklab, currentColor 50%, transparent)) {
  .kbd-01__themelabel {
    border-color: color-mix(in oklab, currentColor 65%, transparent);
  }
}

.kbd-01__themeflip {
  display: none;
}

.kbd-01:has(.kbd-01__themebox:checked) {
  --paper: #17150f;
  --ink: #f2ede1;
  --muted: #9a9080;
  --rule: #322d23;
  --cap: #2a251c;
  --cap-border: #4a4232;
  --cap-edge: #100e09;
  --cap-ink: #f6f1e5;
}

.kbd-01:has(.kbd-01__themebox:checked) .kbd-01__themebase {
  display: none;
}

.kbd-01:has(.kbd-01__themebox:checked) .kbd-01__themeflip {
  display: inline;
}
/* The flip-back rule: on the opposite OS preference the unchecked state is the
   flipped palette, and checking the box returns to the demo's own default. */

@media (prefers-color-scheme: dark) {
  .kbd-01:not(:has(.kbd-01__themebox:checked)) {
    --paper: #17150f;
    --ink: #f2ede1;
    --muted: #9a9080;
    --rule: #322d23;
    --cap: #2a251c;
    --cap-border: #4a4232;
    --cap-edge: #100e09;
    --cap-ink: #f6f1e5;
  }

  .kbd-01:has(.kbd-01__themebox:checked) {
    --paper: #faf7f1;
    --ink: #221e18;
    --muted: #7c7264;
    --rule: #e2dbcd;
    --cap: #ffffff;
    --cap-border: #cfc7b6;
    --cap-edge: #bdb3a0;
    --cap-ink: #332d24;
  }

  .kbd-01:not(:has(.kbd-01__themebox:checked)) .kbd-01__themebase {
    display: none;
  }

  .kbd-01:not(:has(.kbd-01__themebox:checked)) .kbd-01__themeflip {
    display: inline;
  }

  .kbd-01:has(.kbd-01__themebox:checked) .kbd-01__themebase {
    display: inline;
  }

  .kbd-01:has(.kbd-01__themebox:checked) .kbd-01__themeflip {
    display: none;
  }
}
```
