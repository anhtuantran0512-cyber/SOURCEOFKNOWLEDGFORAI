---
source: "codefronts"
url: "https://codefronts.com/snippets/css-tooltips/keyboard-shortcut-card/"
title: "Keyboard Shortcut Card"
section: "snippets"
category: "css-tooltips"
category_name: "CSS Tooltips"
description: "A list of shortcuts where each row pops out a full reference card — large action title, big keycaps, plain-English description, three \"when to use\" bullets,…"
has_js: "false"
---

Here's a working CSS Tooltip from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Keyboard Shortcut Card
Source: https://codefronts.com/snippets/css-tooltips/keyboard-shortcut-card/

A list of shortcuts where each row pops out a full reference card — large action title, big keycaps, plain-English description, three "when to use" bullets, and a related-shortcuts pill row. A richer companion to the compact keycap-pill demo earlier in this collection.
## HTML
```html
<div class="tp-10">
  <div class="tp-10__inner">
    <div class="tp-10__t">
      <div class="tp-10__row">
        <span class="tp-10__label">Save file</span>
        <span class="tp-10__keys"><span class="tp-10__key">⌘</span><span class="tp-10__plus">+</span><span class="tp-10__key">S</span></span>
      </div>
      <div class="tp-10__tip">
        <div class="tp-10__top">
          <div class="tp-10__action">Save File</div>
          <div class="tp-10__keys-big"><span class="tp-10__key-big">⌘</span><span class="tp-10__plus-big">+</span><span class="tp-10__key-big">S</span></div>
        </div>
        <div class="tp-10__desc">Saves the current file to disk immediately. If the file has never been saved, opens a Save As dialog to choose a name and location.</div>
        <div class="tp-10__when">
          <div class="tp-10__when-label">When to use</div>
          <div class="tp-10__when-item">After every meaningful change to preserve work</div>
          <div class="tp-10__when-item">Before switching branches or running tests</div>
          <div class="tp-10__when-item">Before closing the editor or tab</div>
        </div>
        <div class="tp-10__related">
          <div class="tp-10__rel-label">Related</div>
          <div class="tp-10__rel-pill">⌘ ⇧ S — Save As</div>
          <div class="tp-10__rel-pill">⌘ ⌥ S — Save All</div>
        </div>
      </div>
    </div>

    <div class="tp-10__t">
      <div class="tp-10__row">
        <span class="tp-10__label">Undo</span>
        <span class="tp-10__keys"><span class="tp-10__key">⌘</span><span class="tp-10__plus">+</span><span class="tp-10__key">Z</span></span>
      </div>
      <div class="tp-10__tip">
        <div class="tp-10__top">
          <div class="tp-10__action">Undo</div>
          <div class="tp-10__keys-big"><span class="tp-10__key-big">⌘</span><span class="tp-10__plus-big">+</span><span class="tp-10__key-big">Z</span></div>
        </div>
        <div class="tp-10__desc">Reverses the last editing action, stepping backwards through the undo history one action at a time. History is preserved across saves.</div>
        <div class="tp-10__when">
          <div class="tp-10__when-label">When to use</div>
          <div class="tp-10__when-item">After accidentally deleting or overwriting text</div>
          <div class="tp-10__when-item">To compare before/after a refactor</div>
          <div class="tp-10__when-item">To recover from an unwanted auto-format</div>
        </div>
        <div class="tp-10__related">
          <div class="tp-10__rel-label">Related</div>
          <div class="tp-10__rel-pill">⌘ ⇧ Z — Redo</div>
          <div class="tp-10__rel-pill">⌘ K U — Clear history</div>
        </div>
      </div>
    </div>

    <div class="tp-10__t">
      <div class="tp-10__row">
        <span class="tp-10__label">Command palette</span>
        <span class="tp-10__keys"><span class="tp-10__key">⌘</span><span class="tp-10__plus">+</span><span class="tp-10__key">⇧</span><span class="tp-10__plus">+</span><span class="tp-10__key">P</span></span>
      </div>
      <div class="tp-10__tip">
        <div class="tp-10__top">
          <div class="tp-10__action">Command Palette</div>
          <div class="tp-10__keys-big"><span class="tp-10__key-big">⌘</span><span class="tp-10__plus-big">+</span><span class="tp-10__key-big">⇧</span><span class="tp-10__plus-big">+</span><span class="tp-10__key-big">P</span></div>
        </div>
        <div class="tp-10__desc">Opens a searchable list of every editor command, extension action, and setting. The fastest way to trigger any feature without memorising its location.</div>
        <div class="tp-10__when">
          <div class="tp-10__when-label">When to use</div>
          <div class="tp-10__when-item">To find any command without digging through menus</div>
          <div class="tp-10__when-item">To run a formatter, linter, or task</div>
          <div class="tp-10__when-item">To change settings quickly by name</div>
        </div>
        <div class="tp-10__related">
          <div class="tp-10__rel-label">Related</div>
          <div class="tp-10__rel-pill">⌘ P — Quick open file</div>
          <div class="tp-10__rel-pill">⌘ ⇧ O — Go to symbol</div>
        </div>
      </div>
    </div>

    <div class="tp-10__t">
      <div class="tp-10__row">
        <span class="tp-10__label">Find in file</span>
        <span class="tp-10__keys"><span class="tp-10__key">⌘</span><span class="tp-10__plus">+</span><span class="tp-10__key">F</span></span>
      </div>
      <div class="tp-10__tip">
        <div class="tp-10__top">
          <div class="tp-10__action">Find in File</div>
          <div class="tp-10__keys-big"><span class="tp-10__key-big">⌘</span><span class="tp-10__plus-big">+</span><span class="tp-10__key-big">F</span></div>
        </div>
        <div class="tp-10__desc">Opens an inline search bar. Supports plain text, regular expressions, and case-sensitive matching. Highlights all occurrences inside the active file.</div>
        <div class="tp-10__when">
          <div class="tp-10__when-label">When to use</div>
          <div class="tp-10__when-item">To locate a variable, function, or string in the file</div>
          <div class="tp-10__when-item">To count occurrences of a term before refactoring</div>
          <div class="tp-10__when-item">With regex to find patterns (e.g. unused imports)</div>
        </div>
        <div class="tp-10__related">
          <div class="tp-10__rel-label">Related</div>
          <div class="tp-10__rel-pill">⌘ H — Find &amp; Replace</div>
          <div class="tp-10__rel-pill">⌘ ⇧ F — Find in workspace</div>
        </div>
      </div>
    </div>

    <div class="tp-10__t">
      <div class="tp-10__row">
        <span class="tp-10__label">Toggle comment</span>
        <span class="tp-10__keys"><span class="tp-10__key">⌘</span><span class="tp-10__plus">+</span><span class="tp-10__key">/</span></span>
      </div>
      <div class="tp-10__tip">
        <div class="tp-10__top">
          <div class="tp-10__action">Toggle Comment</div>
          <div class="tp-10__keys-big"><span class="tp-10__key-big">⌘</span><span class="tp-10__plus-big">+</span><span class="tp-10__key-big">/</span></div>
        </div>
        <div class="tp-10__desc">Toggles line comments on the current line or all selected lines. Uses the correct comment syntax for the file's language automatically.</div>
        <div class="tp-10__when">
          <div class="tp-10__when-label">When to use</div>
          <div class="tp-10__when-item">To temporarily disable a block of code for debugging</div>
          <div class="tp-10__when-item">To add an explanatory comment above a function</div>
          <div class="tp-10__when-item">To comment multiple lines at once (select first)</div>
        </div>
        <div class="tp-10__related">
          <div class="tp-10__rel-label">Related</div>
          <div class="tp-10__rel-pill">⌘ ⇧ / — Block comment</div>
          <div class="tp-10__rel-pill">⌘ K C — Add comment</div>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.tp-10 {
  width: 100%;
  min-height: 100vh;
  background: #111116;
  /* Left room — kchord tips pop to the LEFT of each shortcut row,
       ~260px wide. */
  padding: 36px 28px 36px 320px;
  font-family: 'JetBrains Mono', ui-monospace, monospace;
}

.tp-10__inner {
  max-width: 480px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.tp-10__t {
  position: relative;
}

.tp-10__row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px 12px;
  border-radius: 6px;
  cursor: help;
  transition: background .12s;
}

.tp-10__t:hover .tp-10__row {
  background: rgba(255, 255, 255, 0.04);
}

.tp-10__label {
  font-size: 12.5px;
  color: rgba(255, 255, 255, 0.5);
}

.tp-10__keys {
  display: flex;
  gap: 4px;
  align-items: center;
}

.tp-10__key {
  display: inline-flex;
  align-items: center;
  padding: 3px 7px;
  border-radius: 4px;
  font-size: 10.5px;
  font-weight: 500;
  color: rgba(255, 255, 255, 0.7);
  background: rgba(255, 255, 255, 0.07);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-bottom: 2px solid rgba(255, 255, 255, 0.18);
  line-height: 1;
  letter-spacing: 0.02em;
}

.tp-10__plus {
  font-size: 9px;
  color: rgba(255, 255, 255, 0.2);
}

.tp-10__tip {
  position: absolute;
  right: calc(100% + 12px);
  top: 50%;
  transform: translateY(-50%) translateX(-6px);
  width: 260px;
  background: #1c1c24;
  border: 1px solid rgba(255, 255, 255, 0.09);
  border-radius: 11px;
  box-shadow: 0 16px 44px rgba(0, 0, 0, 0.85);
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transition: opacity .2s, transform .2s cubic-bezier(0.22, 1, 0.36, 1), visibility 0s linear .2s;
  z-index: 30;
  overflow: hidden;
  text-align: left;
}

.tp-10__t:hover .tp-10__tip {
  opacity: 1;
  visibility: visible;
  transform: translateY(-50%) translateX(0);
  transition-delay: 0s;
}

.tp-10__top {
  padding: 14px 14px 11px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.06);
}

.tp-10__action {
  font-size: 15px;
  font-weight: 600;
  color: rgba(255, 255, 255, 0.88);
  margin-bottom: 7px;
}

.tp-10__keys-big {
  display: flex;
  gap: 5px;
  align-items: center;
}

.tp-10__key-big {
  padding: 4px 10px;
  border-radius: 5px;
  font-size: 11.5px;
  font-weight: 600;
  color: rgba(255, 255, 255, 0.8);
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.14);
  border-bottom: 3px solid rgba(255, 255, 255, 0.2);
}

.tp-10__plus-big {
  color: rgba(255, 255, 255, 0.2);
  font-size: 11px;
}

.tp-10__desc {
  padding: 11px 14px;
  font-size: 11.5px;
  color: rgba(255, 255, 255, 0.45);
  line-height: 1.55;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
  font-family: 'Inter', system-ui, sans-serif;
}

.tp-10__when {
  padding: 10px 14px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
}

.tp-10__when-label {
  font-size: 8px;
  color: rgba(255, 255, 255, 0.2);
  letter-spacing: 0.1em;
  text-transform: uppercase;
  margin-bottom: 6px;
}

.tp-10__when-item {
  font-size: 10.5px;
  color: rgba(255, 255, 255, 0.42);
  margin-bottom: 4px;
  padding-left: 10px;
  position: relative;
  font-family: 'Inter', system-ui, sans-serif;
  line-height: 1.4;
}

.tp-10__when-item::before {
  content: '›';
  position: absolute;
  left: 0;
  color: rgba(255, 255, 255, 0.25);
  font-size: 11px;
  top: -1px;
}

.tp-10__related {
  padding: 10px 14px;
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
}

.tp-10__rel-label {
  font-size: 8px;
  color: rgba(255, 255, 255, 0.2);
  letter-spacing: 0.1em;
  text-transform: uppercase;
  width: 100%;
  margin-bottom: 2px;
}

.tp-10__rel-pill {
  font-size: 9.5px;
  padding: 2px 7px;
  border-radius: 4px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.08);
  color: rgba(255, 255, 255, 0.4);
}
```
