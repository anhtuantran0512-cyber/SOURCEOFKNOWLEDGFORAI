---
source: "codefronts"
url: "https://codefronts.com/snippets/css-popovers/submenus-and-nested-popovers/"
title: "Submenus and Nested Popovers"
section: "snippets"
category: "css-popovers"
category_name: "CSS Popovers"
description: "Two auto popovers can be open at once if the browser considers one nested inside the other, and cannot if it does not."
has_js: "false"
---

Here's a working CSS Popover from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Submenus and Nested Popovers
Source: https://codefronts.com/snippets/css-popovers/submenus-and-nested-popovers/

Two auto popovers can be open at once if the browser considers one nested inside the other, and cannot if it does not. Nesting is established by DOM containment or by the popovertarget relationship, and getting it wrong makes the parent menu slam shut the instant the submenu opens. This two-level menu shows the working arrangement and names the rule.
## HTML
```html
<div class="pop-10">
  <div class="pop-10__stage">
    <div class="pop-10__app">
      <div class="pop-10__bar">
        <span class="pop-10__title">Ledger · Q3 close</span>
        <button class="pop-10__menubtn" type="button" popovertarget="pop-10-menu">
          Actions
          <svg viewBox="0 0 16 16" width="13" height="13" fill="none" stroke="currentColor" stroke-width="1.9" aria-hidden="true"><path d="M4 6.5 8 10.5 12 6.5"/></svg>
        </button>
      </div>
      <p class="pop-10__rulecopy">Nesting is DOM containment or a popovertarget relationship. Both levels stay open only because the submenu lives inside the menu.</p>

      <div class="pop-10__menu" popover="auto" id="pop-10-menu" role="menu" aria-label="Actions">
        <button class="pop-10__item" type="button" role="menuitem">Lock period</button>
        <button class="pop-10__item" type="button" role="menuitem">Recalculate accruals</button>
        <button class="pop-10__item pop-10__item--sub" type="button" role="menuitem" popovertarget="pop-10-sub">
          Export
          <svg viewBox="0 0 16 16" width="13" height="13" fill="none" stroke="currentColor" stroke-width="1.9" aria-hidden="true"><path d="M6 4l4 4-4 4"/></svg>
        </button>
        <button class="pop-10__item" type="button" role="menuitem">Invite auditor</button>

        <div class="pop-10__sub" popover="auto" id="pop-10-sub" role="menu" aria-label="Export format">
          <button class="pop-10__item" type="button" role="menuitem">CSV · one row per entry</button>
          <button class="pop-10__item" type="button" role="menuitem">XLSX · grouped by account</button>
          <button class="pop-10__item" type="button" role="menuitem">PDF · signed statement</button>
          <p class="pop-10__note">Both levels open. Escape closes this one first.</p>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.pop-10 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --bg: #201d1a;
  --s1: #2a2622;
  --s2: #332e28;
  --s3: #3d372f;
  --ink: #f4efe6;
  --muted: #a89c8b;
  --rule: #443d34;
  --amber: #e8a33d;
  --font-ui: ui-sans-serif, system-ui, "Segoe UI", sans-serif;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--font-ui);
  padding: 40px 18px;
}

.pop-10__stage {
  display: grid;
  place-items: center;
  max-inline-size: 100%;
  min-height: calc(100vh - 80px);
}

.pop-10__app {
  inline-size: 100%;
  max-inline-size: 30rem;
  min-inline-size: 0;
  background: var(--s1);
  border: 1px solid var(--rule);
  border-radius: 4px;
  padding: 16px;
}

.pop-10__bar {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  align-items: center;
  justify-content: space-between;
}

.pop-10__title {
  font-size: 13.5px;
  font-weight: 650;
  letter-spacing: -0.01em;
  min-inline-size: 0;
}

.pop-10__menubtn {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  min-height: 44px;
  padding: 0 14px;
  font: 650 12.5px/1 var(--font-ui);
  color: var(--bg);
  background: var(--amber);
  border: 0;
  border-radius: 4px;
  cursor: pointer;
  anchor-name: --pop-10-anchor;
}

.pop-10__menubtn:focus-visible {
  outline: 3px solid var(--ink);
  outline-offset: 2px;
}

.pop-10__rulecopy {
  margin: 14px 0 0;
  font-size: 12.5px;
  line-height: 1.65;
  color: var(--muted);
  text-wrap: pretty;
}

.pop-10__menu,
.pop-10__sub {
  position: fixed;
  margin: 0;
  inline-size: min(15rem, calc(100vw - 28px));
  max-inline-size: calc(100vw - 28px);
  padding: 5px;
  color: var(--ink);
  border: 1px solid var(--rule);
  border-radius: 4px;
  display: grid;
  gap: 1px;
}

.pop-10__menu {
  background: var(--s2);
}

.pop-10__sub {
  background: var(--s3);
}

@supports (anchor-name: --a) {
  .pop-10__menu {
    position-anchor: --pop-10-anchor;
    position-area: block-end span-inline-start;
    inset: auto;
    margin-block-start: 8px;
    position-try-fallbacks: flip-block;
  }

  .pop-10__sub {
    position-anchor: --pop-10-subanchor;
    position-area: inline-end block-start;
    inset: auto;
    margin-inline-start: 8px;
    position-try-fallbacks: flip-inline, flip-block;
  }
}

.pop-10__item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  inline-size: 100%;
  min-height: 44px;
  padding: 0 11px;
  font: 500 13px/1.3 var(--font-ui);
  text-align: start;
  color: var(--ink);
  background: transparent;
  border: 0;
  border-radius: 3px;
  cursor: pointer;
  min-inline-size: 0;
}

.pop-10__item:hover {
  background: var(--s3);
}

.pop-10__sub .pop-10__item:hover {
  background: var(--rule);
}

.pop-10__item:focus-visible {
  outline: 2px solid var(--amber);
  outline-offset: -2px;
}

.pop-10__item--sub {
  anchor-name: --pop-10-subanchor;
  color: var(--amber);
}

.pop-10__note {
  margin: 6px 5px 2px;
  font-size: 11px;
  line-height: 1.5;
  color: var(--muted);
}

@media (prefers-color-scheme: light) {
  .pop-10 {
    --bg: #f4f1ec;
    --s1: #ffffff;
    --s2: #ffffff;
    --s3: #f2eee7;
    --ink: #241f19;
    --muted: #6f6355;
    --rule: #ded7cc;
    --amber: #8a5a10;
  }

  .pop-10__menubtn {
    color: #ffffff;
  }

  .pop-10__menu,
    .pop-10__sub {
    box-shadow: 0 16px 34px -22px rgba(36, 31, 25, 0.45);
  }

  .pop-10__item:hover {
    background: var(--s3);
  }
}

[data-theme="dark"] .pop-10 {
  --bg: #201d1a;
  --s1: #2a2622;
  --s2: #332e28;
  --s3: #3d372f;
  --ink: #f4efe6;
  --muted: #a89c8b;
  --rule: #443d34;
  --amber: #e8a33d;
}

[data-theme="dark"] .pop-10 .pop-10__menubtn {
  color: var(--bg);
}
```
