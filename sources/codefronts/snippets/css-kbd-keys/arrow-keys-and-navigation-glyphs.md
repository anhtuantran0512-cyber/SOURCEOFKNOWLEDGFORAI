---
source: "codefronts"
url: "https://codefronts.com/snippets/css-kbd-keys/arrow-keys-and-navigation-glyphs/"
title: "Arrow Keys and Navigation Glyphs"
section: "snippets"
category: "css-kbd-keys"
category_name: "CSS Kbd Keys"
description: "The inverted-T arrow cluster laid out in CSS Grid, next to the six-key navigation block."
has_js: "false"
---

Here's a working CSS Kbd Key from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Arrow Keys and Navigation Glyphs
Source: https://codefronts.com/snippets/css-kbd-keys/arrow-keys-and-navigation-glyphs/

The inverted-T arrow cluster laid out in CSS Grid, next to the six-key navigation block. Arrows are real Unicode characters rather than images, each carrying a visually hidden name so the key announces as Arrow up instead of a bare glyph. The cluster uses explicit grid placement because the shape itself carries meaning that flex wrapping would destroy.
## HTML
```html
<div class="kbd-07">
  <div class="kbd-07__stage">
    <div class="kbd-07__blocks">
      <section class="kbd-07__block">
        <h2 class="kbd-07__h">Arrow cluster</h2>
        <div class="kbd-07__arrows">
          <kbd class="kbd-07__key kbd-07__key--up"><span aria-hidden="true">↑</span><span class="kbd-07__vh">Arrow up</span></kbd>
          <kbd class="kbd-07__key kbd-07__key--left"><span aria-hidden="true">←</span><span class="kbd-07__vh">Arrow left</span></kbd>
          <kbd class="kbd-07__key kbd-07__key--down"><span aria-hidden="true">↓</span><span class="kbd-07__vh">Arrow down</span></kbd>
          <kbd class="kbd-07__key kbd-07__key--right"><span aria-hidden="true">→</span><span class="kbd-07__vh">Arrow right</span></kbd>
        </div>
        <p class="kbd-07__note">Explicit grid areas — the T survives every viewport.</p>
      </section>
      <section class="kbd-07__block">
        <h2 class="kbd-07__h">Navigation</h2>
        <div class="kbd-07__nav">
          <kbd class="kbd-07__key kbd-07__key--wide">Home</kbd>
          <kbd class="kbd-07__key kbd-07__key--wide">End</kbd>
          <kbd class="kbd-07__key kbd-07__key--wide">Page <span aria-hidden="true">↑</span><span class="kbd-07__vh">up</span></kbd>
          <kbd class="kbd-07__key kbd-07__key--wide">Page <span aria-hidden="true">↓</span><span class="kbd-07__vh">down</span></kbd>
          <kbd class="kbd-07__key kbd-07__key--wide">Insert</kbd>
          <kbd class="kbd-07__key kbd-07__key--wide">Delete</kbd>
        </div>
        <p class="kbd-07__note">Word labels get their own grid, not the arrow one.</p>
      </section>
    </div>
    <div class="kbd-07__theme">
      <input class="kbd-07__themebox" type="checkbox" id="kbd-07-theme">
      <label class="kbd-07__themelabel" for="kbd-07-theme">
        <span class="kbd-07__themedot" aria-hidden="true"></span>
        <span class="kbd-07__themebase">Light</span><span class="kbd-07__themeflip">Dark</span>
      </label>
    </div>
  </div>
</div>
```
## CSS
```css
.kbd-07 {
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  --page: #eef1e8;
  --surface: #f9fbf5;
  --ink: #222b22;
  --muted: #6d7a68;
  --rule: #d4dccb;
  --cap: #ffffff;
  --cap-border: #b9c6ac;
  --cap-edge: #9aab8c;
  --cap-ink: #2c3a2b;
  --accent: #4a7a52;
  --u: clamp(46px, 13vw, 62px);
  --radius: 10px;
  --font-key: ui-sans-serif, system-ui, "Helvetica Neue", sans-serif;
  background: var(--page);
  color: var(--ink);
  font-family: var(--font-key);
  padding: 40px 18px;
}

.kbd-07__stage {
  display: grid;
  place-items: center;
  min-height: calc(100vh - 80px);
}

.kbd-07__blocks {
  inline-size: 100%;
  max-inline-size: 34rem;
  min-inline-size: 0;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(15rem, 1fr));
  gap: 22px;
}

.kbd-07__block {
  min-inline-size: 0;
  background: var(--surface);
  border: 1px solid var(--rule);
  border-radius: 14px;
  padding: 20px 20px 16px;
}

.kbd-07__h {
  margin: 0 0 16px;
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--accent);
}

.kbd-07__arrows {
  display: grid;
  grid-template-columns: repeat(3, var(--u));
  grid-template-rows: repeat(2, var(--u));
  gap: 7px;
  justify-content: center;
}

.kbd-07__key--up {
  grid-column: 2;
  grid-row: 1;
}

.kbd-07__key--left {
  grid-column: 1;
  grid-row: 2;
}

.kbd-07__key--down {
  grid-column: 2;
  grid-row: 2;
}

.kbd-07__key--right {
  grid-column: 3;
  grid-row: 2;
}

.kbd-07__key {
  display: flex;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
  block-size: var(--u);
  min-block-size: 44px;
  min-inline-size: 0;
  font-family: inherit;
  font-size: 19px;
  font-weight: 600;
  line-height: 1;
  color: var(--cap-ink);
  background: var(--cap);
  border: 1px solid var(--cap-border);
  border-radius: var(--radius);
  box-shadow: 0 2px 0 var(--cap-edge);
}

.kbd-07__nav {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 7px;
}

.kbd-07__key--wide {
  block-size: calc(var(--u) * 0.72);
  font-size: 12.5px;
  letter-spacing: 0.02em;
  gap: 4px;
  padding: 0 6px;
  white-space: nowrap;
}

.kbd-07__vh {
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

.kbd-07__note {
  margin: 16px 0 0;
  padding-top: 12px;
  border-top: 1px dotted var(--rule);
  font-size: 11.5px;
  line-height: 1.5;
  color: var(--muted);
  text-wrap: pretty;
}

.kbd-07[data-theme="dark"],
[data-theme="dark"] .kbd-07 {
  --page: #131811;
  --surface: #1a2118;
  --ink: #e7efe3;
  --muted: #8d9c87;
  --rule: #2b3628;
  --cap: #253022;
  --cap-border: #3d4d38;
  --cap-edge: #101509;
  --cap-ink: #eaf2e6;
  --accent: #8fc196;
}
/* In-demo theme switch. State is one checkbox inside this demo, so the toggle
   themes THIS demo only — no root attribute, no script. */

.kbd-07__theme {
  position: absolute;
  inset-block-start: 14px;
  inset-inline-end: 16px;
  z-index: 5;
  display: flex;
}
/* the pill owns the top-right corner, so the stage reserves that band */

.kbd-07__stage {
  box-sizing: border-box;
  padding-block-start: 46px;
}

.kbd-07__themebox {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  pointer-events: none;
}

.kbd-07__themelabel {
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

.kbd-07__themedot {
  inline-size: 12px;
  block-size: 12px;
  flex: none;
  border-radius: 50%;
  background: currentColor;
}

.kbd-07__themebox:focus-visible + .kbd-07__themelabel {
  outline: 3px solid var(--accent, var(--cap-ink, currentColor));
  outline-offset: 2px;
}

@supports (border-color: color-mix(in oklab, currentColor 50%, transparent)) {
  .kbd-07__themelabel {
    border-color: color-mix(in oklab, currentColor 65%, transparent);
  }
}

.kbd-07__themeflip {
  display: none;
}

.kbd-07:has(.kbd-07__themebox:checked) {
  --page: #131811;
  --surface: #1a2118;
  --ink: #e7efe3;
  --muted: #8d9c87;
  --rule: #2b3628;
  --cap: #253022;
  --cap-border: #3d4d38;
  --cap-edge: #101509;
  --cap-ink: #eaf2e6;
  --accent: #8fc196;
}

.kbd-07:has(.kbd-07__themebox:checked) .kbd-07__themebase {
  display: none;
}

.kbd-07:has(.kbd-07__themebox:checked) .kbd-07__themeflip {
  display: inline;
}
/* The flip-back rule: on the opposite OS preference the unchecked state is the
   flipped palette, and checking the box returns to the demo's own default. */

@media (prefers-color-scheme: dark) {
  .kbd-07:not(:has(.kbd-07__themebox:checked)) {
    --page: #131811;
    --surface: #1a2118;
    --ink: #e7efe3;
    --muted: #8d9c87;
    --rule: #2b3628;
    --cap: #253022;
    --cap-border: #3d4d38;
    --cap-edge: #101509;
    --cap-ink: #eaf2e6;
    --accent: #8fc196;
  }

  .kbd-07:has(.kbd-07__themebox:checked) {
    --page: #eef1e8;
    --surface: #f9fbf5;
    --ink: #222b22;
    --muted: #6d7a68;
    --rule: #d4dccb;
    --cap: #ffffff;
    --cap-border: #b9c6ac;
    --cap-edge: #9aab8c;
    --cap-ink: #2c3a2b;
    --accent: #4a7a52;
  }

  .kbd-07:not(:has(.kbd-07__themebox:checked)) .kbd-07__themebase {
    display: none;
  }

  .kbd-07:not(:has(.kbd-07__themebox:checked)) .kbd-07__themeflip {
    display: inline;
  }

  .kbd-07:has(.kbd-07__themebox:checked) .kbd-07__themebase {
    display: inline;
  }

  .kbd-07:has(.kbd-07__themebox:checked) .kbd-07__themeflip {
    display: none;
  }
}
```
