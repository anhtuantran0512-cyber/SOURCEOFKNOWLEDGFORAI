---
source: "codefronts"
url: "https://codefronts.com/snippets/css-kbd-keys/search-bar-shortcut-hint-with-kbd/"
title: "Search Bar Shortcut Hint with Kbd"
section: "snippets"
category: "css-kbd-keys"
category_name: "CSS Kbd Keys"
description: "The trailing shortcut pill pinned inside a search field."
has_js: "false"
---

Here's a working CSS Kbd Key from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Search Bar Shortcut Hint with Kbd
Source: https://codefronts.com/snippets/css-kbd-keys/search-bar-shortcut-hint-with-kbd/

The trailing shortcut pill pinned inside a search field. The input is deliberately plain chrome; the cap is the subject. It sits optically centred against the field rather than mathematically centred, takes pointer-events: none so a click anywhere still lands in the input, and dims on focus because once you are typing the hint has done its job.
## HTML
```html
<div class="kbd-11">
  <div class="kbd-11__stage">
    <div class="kbd-11__wrap">
      <label class="kbd-11__label" for="kbd-11-input">Search documentation</label>
      <div class="kbd-11__field">
        <input class="kbd-11__input" id="kbd-11-input" type="text" placeholder="Search components, tokens, guides">
        <kbd class="kbd-11__hint" aria-hidden="true"><kbd class="kbd-11__key">⌘</kbd><kbd class="kbd-11__key">K</kbd></kbd>
      </div>
      <p class="kbd-11__note">Click anywhere on the field, including the pill — the cap takes <code class="kbd-11__code">pointer-events: none</code>, so the click lands in the input. Focus the field and the hint fades back.</p>
    </div>
    <div class="kbd-11__theme">
      <input class="kbd-11__themebox" type="checkbox" id="kbd-11-theme">
      <label class="kbd-11__themelabel" for="kbd-11-theme">
        <span class="kbd-11__themedot" aria-hidden="true"></span>
        <span class="kbd-11__themebase">Light</span><span class="kbd-11__themeflip">Dark</span>
      </label>
    </div>
  </div>
</div>
```
## CSS
```css
.kbd-11 {
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  --page: #f4f6f8;
  --field: #ffffff;
  --ink: #1c232b;
  --muted: #6a7684;
  --rule: #d3dae1;
  --cap: #eef1f5;
  --cap-border: #cbd3dc;
  --cap-ink: #47535f;
  --accent: #2563eb;
  --hint-gutter: 10px;
  --radius: 10px;
  --font-key: ui-sans-serif, system-ui, "Segoe UI", sans-serif;
  background: var(--page);
  color: var(--ink);
  font-family: var(--font-key);
  padding: 40px 18px;
}

.kbd-11__stage {
  display: grid;
  place-items: center;
  min-height: calc(100vh - 80px);
}

.kbd-11__wrap {
  inline-size: 100%;
  max-inline-size: 27rem;
  min-inline-size: 0;
}

.kbd-11__label {
  display: block;
  margin-bottom: 8px;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--muted);
}

.kbd-11__field {
  position: relative;
  min-inline-size: 0;
}

.kbd-11__input {
  inline-size: 100%;
  box-sizing: border-box;
  min-block-size: 48px;
  padding-block: 0;
  padding-inline: 14px calc(var(--hint-gutter) + 68px);
  font-family: inherit;
  font-size: 14.5px;
  color: var(--ink);
  background: var(--field);
  border: 1px solid var(--rule);
  border-radius: var(--radius);
  outline: none;
  transition: border-color 150ms ease, box-shadow 150ms ease;
}

.kbd-11__input::placeholder {
  color: var(--muted);
}

.kbd-11__input:focus-visible {
  border-color: var(--accent);
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.22);
}

.kbd-11__hint {
  position: absolute;
  inset-inline-end: var(--hint-gutter);
  inset-block-start: 50%;
  transform: translateY(calc(-50% - 0.5px));
  display: inline-flex;
  align-items: center;
  gap: 4px;
  pointer-events: none;
  font-family: inherit;
  opacity: 1;
  transition: opacity 160ms ease;
}

.kbd-11__field:focus-within .kbd-11__hint {
  opacity: 0.35;
}

.kbd-11__key {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-inline-size: 24px;
  min-block-size: 22px;
  padding: 0 5px;
  box-sizing: border-box;
  font-family: inherit;
  font-size: 11.5px;
  font-weight: 600;
  line-height: 1;
  color: var(--cap-ink);
  background: var(--cap);
  border: 1px solid var(--cap-border);
  border-radius: 5px;
}

.kbd-11__note {
  margin: 16px 0 0;
  font-size: 12.5px;
  line-height: 1.65;
  color: var(--muted);
  text-wrap: pretty;
}

.kbd-11__code {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.9em;
  background: var(--cap);
  padding: 0.15em 0.35em;
  border-radius: 4px;
  color: var(--cap-ink);
}

@media (prefers-reduced-motion: reduce) {
  .kbd-11__input,
    .kbd-11__hint {
    transition: none;
  }
}

.kbd-11[data-theme="dark"],
[data-theme="dark"] .kbd-11 {
  --page: #0f151b;
  --field: #171f28;
  --ink: #e8eef4;
  --muted: #8896a4;
  --rule: #2a3542;
  --cap: #202b36;
  --cap-border: #384554;
  --cap-ink: #cbd8e4;
  --accent: #60a5fa;
}
/* In-demo theme switch. State is one checkbox inside this demo, so the toggle
   themes THIS demo only — no root attribute, no script. */

.kbd-11__theme {
  position: absolute;
  inset-block-start: 14px;
  inset-inline-end: 16px;
  z-index: 5;
  display: flex;
}
/* the pill owns the top-right corner, so the stage reserves that band */

.kbd-11__stage {
  box-sizing: border-box;
  padding-block-start: 46px;
}

.kbd-11__themebox {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  pointer-events: none;
}

.kbd-11__themelabel {
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

.kbd-11__themedot {
  inline-size: 12px;
  block-size: 12px;
  flex: none;
  border-radius: 50%;
  background: currentColor;
}

.kbd-11__themebox:focus-visible + .kbd-11__themelabel {
  outline: 3px solid var(--accent, var(--cap-ink, currentColor));
  outline-offset: 2px;
}

@supports (border-color: color-mix(in oklab, currentColor 50%, transparent)) {
  .kbd-11__themelabel {
    border-color: color-mix(in oklab, currentColor 65%, transparent);
  }
}

.kbd-11__themeflip {
  display: none;
}

.kbd-11:has(.kbd-11__themebox:checked) {
  --page: #0f151b;
  --field: #171f28;
  --ink: #e8eef4;
  --muted: #8896a4;
  --rule: #2a3542;
  --cap: #202b36;
  --cap-border: #384554;
  --cap-ink: #cbd8e4;
  --accent: #60a5fa;
}

.kbd-11:has(.kbd-11__themebox:checked) .kbd-11__themebase {
  display: none;
}

.kbd-11:has(.kbd-11__themebox:checked) .kbd-11__themeflip {
  display: inline;
}
/* The flip-back rule: on the opposite OS preference the unchecked state is the
   flipped palette, and checking the box returns to the demo's own default. */

@media (prefers-color-scheme: dark) {
  .kbd-11:not(:has(.kbd-11__themebox:checked)) {
    --page: #0f151b;
    --field: #171f28;
    --ink: #e8eef4;
    --muted: #8896a4;
    --rule: #2a3542;
    --cap: #202b36;
    --cap-border: #384554;
    --cap-ink: #cbd8e4;
    --accent: #60a5fa;
  }

  .kbd-11:has(.kbd-11__themebox:checked) {
    --page: #f4f6f8;
    --field: #ffffff;
    --ink: #1c232b;
    --muted: #6a7684;
    --rule: #d3dae1;
    --cap: #eef1f5;
    --cap-border: #cbd3dc;
    --cap-ink: #47535f;
    --accent: #2563eb;
  }

  .kbd-11:not(:has(.kbd-11__themebox:checked)) .kbd-11__themebase {
    display: none;
  }

  .kbd-11:not(:has(.kbd-11__themebox:checked)) .kbd-11__themeflip {
    display: inline;
  }

  .kbd-11:has(.kbd-11__themebox:checked) .kbd-11__themebase {
    display: inline;
  }

  .kbd-11:has(.kbd-11__themebox:checked) .kbd-11__themeflip {
    display: none;
  }
}
```
