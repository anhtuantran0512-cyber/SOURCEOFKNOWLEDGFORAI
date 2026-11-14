---
source: "codefronts"
url: "https://codefronts.com/snippets/css-popovers/user-profile-flyout-menu/"
title: "User Profile Flyout Menu"
section: "snippets"
category: "css-popovers"
category_name: "CSS Popovers"
description: "The canonical product-header pattern, built with no script: an avatar button anchors an account menu that opens toward the page interior and flips inward…"
has_js: "false"
---

Here's a working CSS Popover from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: User Profile Flyout Menu
Source: https://codefronts.com/snippets/css-popovers/user-profile-flyout-menu/

The canonical product-header pattern, built with no script: an avatar button anchors an account menu that opens toward the page interior and flips inward when the header sits near the viewport edge. Because an open popover lives in the top layer, the menu is not clipped by the header's own overflow and needs no z-index at all.
## HTML
```html
<div class="pop-13">
  <div class="pop-13__stage">
    <div class="pop-13__app">
      <header class="pop-13__header">
        <span class="pop-13__logo">Northwind</span>
        <div class="pop-13__spacer"></div>
        <span class="pop-13__crumb">Pipeline</span>
        <button class="pop-13__avatar" type="button" popovertarget="pop-13-menu" aria-label="Account menu for Priya Sharma">PS</button>
      </header>
      <div class="pop-13__content">
        <p class="pop-13__row"><span>Acme Foods</span><span class="pop-13__amt">$41,200</span></p>
        <p class="pop-13__row"><span>Harbor Logistics</span><span class="pop-13__amt">$18,750</span></p>
        <p class="pop-13__row"><span>Verity Health</span><span class="pop-13__amt">$96,400</span></p>
        <p class="pop-13__note">The header clips its own overflow. The menu does not care.</p>
      </div>

      <div class="pop-13__menu" popover="auto" id="pop-13-menu" role="menu" aria-label="Account">
        <div class="pop-13__who">
          <span class="pop-13__whoname">Priya Sharma</span>
          <span class="pop-13__whomail">[email protected]</span>
        </div>
        <button class="pop-13__item" type="button" role="menuitem">
          <svg viewBox="0 0 18 18" width="15" height="15" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="9" cy="6.4" r="3.1"/><path d="M3.4 15c.9-2.7 3-4 5.6-4s4.7 1.3 5.6 4"/></svg>
          Profile and preferences
        </button>
        <button class="pop-13__item" type="button" role="menuitem">
          <svg viewBox="0 0 18 18" width="15" height="15" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="3" y="4" width="12" height="10" rx="1.6"/><path d="M3 7.5h12"/></svg>
          Billing · Team plan
        </button>
        <div class="pop-13__sep" role="separator"></div>
        <button class="pop-13__item pop-13__item--out" type="button" role="menuitem">
          <svg viewBox="0 0 18 18" width="15" height="15" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M11 5V3.6H4v10.8h7V13M8 9h7M12.6 6.6 15 9l-2.4 2.4"/></svg>
          Sign out
        </button>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.pop-13 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --bg: #eceef1;
  --surface: #ffffff;
  --head: #f7f8fa;
  --ink: #171b21;
  --muted: #6b7280;
  --rule: #dfe2e7;
  --accent: #3d4a5c;
  --danger: #a3352b;
  --radius: 14px;
  --font-ui: ui-sans-serif, system-ui, "Segoe UI", sans-serif;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--font-ui);
  padding: 40px 18px;
}

.pop-13__stage {
  display: grid;
  place-items: center;
  max-inline-size: 100%;
  min-height: calc(100vh - 80px);
}

.pop-13__app {
  inline-size: 100%;
  max-inline-size: 32rem;
  min-inline-size: 0;
  background: var(--surface);
  border: 1px solid var(--rule);
  border-radius: var(--radius);
  overflow: hidden;
  isolation: isolate;
}

.pop-13__header {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 8px 10px 8px 16px;
  background: var(--head);
  border-block-end: 1px solid var(--rule);
  overflow: hidden;
}

.pop-13__logo {
  font-size: 13px;
  font-weight: 700;
  letter-spacing: -0.01em;
}

.pop-13__spacer {
  flex: 1 1 auto;
  min-inline-size: 0;
}

.pop-13__crumb {
  font-size: 12px;
  color: var(--muted);
}

.pop-13__avatar {
  flex: none;
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  font: 700 12.5px/1 var(--font-ui);
  letter-spacing: 0.04em;
  color: var(--surface);
  background: var(--accent);
  border: 0;
  border-radius: 999px;
  cursor: pointer;
  anchor-name: --pop-13-anchor;
}

.pop-13__avatar:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

.pop-13__content {
  padding: 16px;
}

.pop-13__row {
  display: flex;
  justify-content: space-between;
  gap: 12px;
  margin: 0 0 10px;
  font-size: 13.5px;
  min-inline-size: 0;
}

.pop-13__amt {
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.pop-13__note {
  margin: 16px 0 0;
  padding-block-start: 12px;
  border-block-start: 1px solid var(--rule);
  font-size: 12px;
  color: var(--muted);
}

.pop-13__menu {
  position: fixed;
  margin: 0;
  inline-size: min(16rem, calc(100vw - 28px));
  max-inline-size: calc(100vw - 28px);
  padding: 6px;
  color: var(--ink);
  background: var(--surface);
  border: 1px solid var(--rule);
  border-radius: var(--radius);
  box-shadow: 0 24px 48px -24px rgba(23, 27, 33, 0.55);
}

@supports (anchor-name: --a) {
  .pop-13__menu {
    position-anchor: --pop-13-anchor;
    position-area: block-end span-inline-start;
    inset: auto;
    margin-block-start: 8px;
    position-try-fallbacks: flip-inline, flip-block;
  }
}

.pop-13__who {
  padding: 10px 11px 12px;
  border-block-end: 1px solid var(--rule);
  margin-bottom: 5px;
  display: grid;
  gap: 3px;
}

.pop-13__whoname {
  font-size: 13px;
  font-weight: 650;
}

.pop-13__whomail {
  font-size: 11.5px;
  color: var(--muted);
  overflow: hidden;
  text-overflow: ellipsis;
}

.pop-13__item {
  display: flex;
  align-items: center;
  gap: 10px;
  inline-size: 100%;
  min-height: 44px;
  padding: 0 11px;
  font: 500 13px/1.3 var(--font-ui);
  text-align: start;
  color: var(--ink);
  background: transparent;
  border: 0;
  border-radius: 9px;
  cursor: pointer;
  min-inline-size: 0;
}

.pop-13__item svg {
  flex: none;
  color: var(--muted);
}

.pop-13__item:hover {
  background: var(--head);
}

.pop-13__item:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: -3px;
}

.pop-13__item--out {
  color: var(--danger);
}

.pop-13__item--out svg {
  color: var(--danger);
}

.pop-13__sep {
  block-size: 1px;
  margin: 5px 4px;
  background: var(--rule);
}

@media (prefers-color-scheme: dark) {
  .pop-13 {
    --bg: #0f1216;
    --surface: #191d23;
    --head: #14181e;
    --ink: #e8ebf0;
    --muted: #8d95a2;
    --rule: #292f38;
    --accent: #93a6c0;
    --danger: #e3897f;
  }

  .pop-13__avatar {
    color: #0f1216;
  }
}

[data-theme="dark"] .pop-13 {
  --bg: #0f1216;
  --surface: #191d23;
  --head: #14181e;
  --ink: #e8ebf0;
  --muted: #8d95a2;
  --rule: #292f38;
  --accent: #93a6c0;
  --danger: #e3897f;
}

[data-theme="dark"] .pop-13 .pop-13__avatar {
  color: #0f1216;
}
```
