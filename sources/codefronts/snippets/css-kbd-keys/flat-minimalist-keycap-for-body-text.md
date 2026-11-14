---
source: "codefronts"
url: "https://codefronts.com/snippets/css-kbd-keys/flat-minimalist-keycap-for-body-text/"
title: "Flat Minimalist Keycap for Body Text"
section: "snippets"
category: "css-kbd-keys"
category_name: "CSS Kbd Keys"
description: "No depth, no shadow: a tinted rounded rectangle with a hairline border, sized to disappear into dense body copy."
has_js: "false"
---

Here's a working CSS Kbd Key from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Flat Minimalist Keycap for Body Text
Source: https://codefronts.com/snippets/css-kbd-keys/flat-minimalist-keycap-for-body-text/

No depth, no shadow: a tinted rounded rectangle with a hairline border, sized to disappear into dense body copy. This is the treatment most documentation sites actually ship, because a physical cap repeated forty times down a reference page becomes visual noise. Set beside demo 01 so you can see exactly what you trade away and what you get back.
## HTML
```html
<div class="kbd-04">
  <div class="kbd-04__stage">
    <article class="kbd-04__doc">
      <h2 class="kbd-04__h">Selection and navigation</h2>
      <p class="kbd-04__p">Hold <kbd class="kbd-04__key">Shift</kbd> and use the arrow keys to grow the selection by one character, or add <kbd class="kbd-04__key">Alt</kbd> to grow it by one word. <kbd class="kbd-04__key">Home</kbd> and <kbd class="kbd-04__key">End</kbd> jump to the ends of the visual line; add <kbd class="kbd-04__key">Ctrl</kbd> to jump to the ends of the document instead. Numbered tabs respond to <kbd class="kbd-04__key">Ctrl</kbd> plus <kbd class="kbd-04__key">1</kbd> through <kbd class="kbd-04__key">9</kbd>, and <kbd class="kbd-04__key">Ctrl</kbd> plus <kbd class="kbd-04__key">0</kbd> returns to the last one you looked at.</p>
      <p class="kbd-04__p">Twelve keys in two paragraphs, and the page still reads as prose. That is the argument for the flat treatment.</p>
      <div class="kbd-04__compare">
        <div class="kbd-04__col">
          <p class="kbd-04__collabel">Flat · this demo</p>
          <p class="kbd-04__example">Press <kbd class="kbd-04__key">Ctrl</kbd> <kbd class="kbd-04__key">K</kbd> to search.</p>
          <p class="kbd-04__note">Reference prose, changelogs, dense help pages.</p>
        </div>
        <div class="kbd-04__col">
          <p class="kbd-04__collabel">Raised · demo 01</p>
          <p class="kbd-04__example">Press <kbd class="kbd-04__key kbd-04__key--raised">Ctrl</kbd> <kbd class="kbd-04__key kbd-04__key--raised">K</kbd> to search.</p>
          <p class="kbd-04__note">Tips, callouts, first-run hints — one shortcut at a time.</p>
        </div>
      </div>
    </article>
    <div class="kbd-04__theme">
      <input class="kbd-04__themebox" type="checkbox" id="kbd-04-theme">
      <label class="kbd-04__themelabel" for="kbd-04-theme">
        <span class="kbd-04__themedot" aria-hidden="true"></span>
        <span class="kbd-04__themebase">Light</span><span class="kbd-04__themeflip">Dark</span>
      </label>
    </div>
  </div>
</div>
```
## CSS
```css
.kbd-04 {
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  --page: #fbfbf9;
  --ink: #1b1b1a;
  --muted: #6f6f6a;
  --rule: #e4e4de;
  --cap: #efefe9;
  --cap-border: #d8d8d0;
  --cap-ink: #26261f;
  --radius: 4px;
  --key-size: 0.83em;
  --font-key: ui-sans-serif, system-ui, "Helvetica Neue", sans-serif;
  --font-body: "Iowan Old Style", Palatino, Georgia, serif;
  background: var(--page);
  color: var(--ink);
  padding: 40px 20px;
}

.kbd-04__stage {
  display: grid;
  place-items: center;
  min-height: calc(100vh - 80px);
}

.kbd-04__doc {
  inline-size: 100%;
  max-inline-size: 34rem;
  min-inline-size: 0;
}

.kbd-04__h {
  margin: 0 0 16px;
  font: 400 clamp(23px, 5vw, 30px)/1.2 var(--font-body);
  letter-spacing: -0.01em;
}

.kbd-04__p {
  margin: 0 0 16px;
  font: 400 clamp(15px, 3.3vw, 16.5px)/1.8 var(--font-body);
  text-wrap: pretty;
}

.kbd-04__key {
  display: inline-block;
  padding: 0.2em 0.45em;
  min-inline-size: 1.15em;
  box-sizing: content-box;
  font-family: var(--font-key);
  font-size: var(--key-size);
  font-weight: 500;
  font-variant-numeric: tabular-nums;
  line-height: 1;
  text-align: center;
  color: var(--cap-ink);
  background: var(--cap);
  border: 1px solid var(--cap-border);
  border-radius: var(--radius);
  vertical-align: 0.08em;
  white-space: nowrap;
}

@supports (background: color-mix(in oklab, #000 10%, #fff)) {
  .kbd-04__key {
    background: color-mix(in oklab, var(--ink) 9%, var(--page));
    border-color: color-mix(in oklab, var(--ink) 18%, var(--page));
  }
}

.kbd-04__key--raised {
  background: #ffffff;
  border-color: #cfcfc6;
  box-shadow: 0 1px 0 #bdbdb2;
}

.kbd-04__compare {
  margin-top: 26px;
  padding-top: 22px;
  border-top: 1px solid var(--rule);
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(13rem, 1fr));
  gap: 22px;
}

.kbd-04__col {
  min-inline-size: 0;
}

.kbd-04__collabel {
  margin: 0 0 8px;
  font: 600 9.5px/1 var(--font-key);
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--muted);
}

.kbd-04__example {
  margin: 0 0 8px;
  font: 400 15px/1.7 var(--font-body);
}

.kbd-04__note {
  margin: 0;
  font: 400 12px/1.5 var(--font-key);
  color: var(--muted);
  text-wrap: pretty;
}

.kbd-04[data-theme="dark"],
[data-theme="dark"] .kbd-04 {
  --page: #121212;
  --ink: #ececea;
  --muted: #9a9a95;
  --rule: #2a2a28;
  --cap: #262624;
  --cap-border: #3d3d39;
  --cap-ink: #f0f0ec;
}
/* In-demo theme switch. State is one checkbox inside this demo, so the toggle
   themes THIS demo only — no root attribute, no script. */

.kbd-04__theme {
  position: absolute;
  inset-block-start: 14px;
  inset-inline-end: 16px;
  z-index: 5;
  display: flex;
}
/* the pill owns the top-right corner, so the stage reserves that band */

.kbd-04__stage {
  box-sizing: border-box;
  padding-block-start: 46px;
}

.kbd-04__themebox {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  pointer-events: none;
}

.kbd-04__themelabel {
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

.kbd-04__themedot {
  inline-size: 12px;
  block-size: 12px;
  flex: none;
  border-radius: 50%;
  background: currentColor;
}

.kbd-04__themebox:focus-visible + .kbd-04__themelabel {
  outline: 3px solid var(--accent, var(--cap-ink, currentColor));
  outline-offset: 2px;
}

@supports (border-color: color-mix(in oklab, currentColor 50%, transparent)) {
  .kbd-04__themelabel {
    border-color: color-mix(in oklab, currentColor 65%, transparent);
  }
}

.kbd-04__themeflip {
  display: none;
}

.kbd-04:has(.kbd-04__themebox:checked) {
  --page: #121212;
  --ink: #ececea;
  --muted: #9a9a95;
  --rule: #2a2a28;
  --cap: #262624;
  --cap-border: #3d3d39;
  --cap-ink: #f0f0ec;
}

.kbd-04:has(.kbd-04__themebox:checked) .kbd-04__themebase {
  display: none;
}

.kbd-04:has(.kbd-04__themebox:checked) .kbd-04__themeflip {
  display: inline;
}

.kbd-04:has(.kbd-04__themebox:checked) .kbd-04__key--raised {
  background: #2f2f2c;
  border-color: #4a4a45;
  box-shadow: 0 1px 0 #0c0c0b;
}
/* The flip-back rule: on the opposite OS preference the unchecked state is the
   flipped palette, and checking the box returns to the demo's own default. */

@media (prefers-color-scheme: dark) {
  .kbd-04:not(:has(.kbd-04__themebox:checked)) {
    --page: #121212;
    --ink: #ececea;
    --muted: #9a9a95;
    --rule: #2a2a28;
    --cap: #262624;
    --cap-border: #3d3d39;
    --cap-ink: #f0f0ec;
  }

  .kbd-04:has(.kbd-04__themebox:checked) {
    --page: #fbfbf9;
    --ink: #1b1b1a;
    --muted: #6f6f6a;
    --rule: #e4e4de;
    --cap: #efefe9;
    --cap-border: #d8d8d0;
    --cap-ink: #26261f;
  }

  .kbd-04:not(:has(.kbd-04__themebox:checked)) .kbd-04__themebase {
    display: none;
  }

  .kbd-04:not(:has(.kbd-04__themebox:checked)) .kbd-04__themeflip {
    display: inline;
  }

  .kbd-04:has(.kbd-04__themebox:checked) .kbd-04__themebase {
    display: inline;
  }

  .kbd-04:has(.kbd-04__themebox:checked) .kbd-04__themeflip {
    display: none;
  }

  .kbd-04:not(:has(.kbd-04__themebox:checked)) .kbd-04__key--raised {
    background: #2f2f2c;
    border-color: #4a4a45;
    box-shadow: 0 1px 0 #0c0c0b;
  }

  .kbd-04:has(.kbd-04__themebox:checked) .kbd-04__key--raised {
    background: #ffffff;
    border-color: #cfcfc6;
    box-shadow: 0 1px 0 #bdbdb2;
  }
}
```
