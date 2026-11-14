---
source: "codefronts"
url: "https://codefronts.com/snippets/css-popovers/basic-popover-show-and-hide/"
title: "Basic Popover Show and Hide"
section: "snippets"
category: "css-popovers"
category_name: "CSS Popovers"
description: "The reference build the rest of the collection reuses: one button carrying popovertarget, one element carrying the popover attribute, and no script at all."
has_js: "false"
---

Here's a working CSS Popover from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Basic Popover Show and Hide
Source: https://codefronts.com/snippets/css-popovers/basic-popover-show-and-hide/

The reference build the rest of the collection reuses: one button carrying popovertarget, one element carrying the popover attribute, and no script at all. The browser promotes the panel to the top layer, closes it when you click outside or press Escape, and returns focus to the button — behaviour that used to take a few hundred lines of listener plumbing and a z-index audit.
## HTML
```html
<div class="pop-01">
  <div class="pop-01__stage">
    <div class="pop-01__doc">
      <header class="pop-01__bar">
        <div class="pop-01__brand">
          <span class="pop-01__mark" aria-hidden="true">
            <svg viewBox="0 0 20 20" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 5h12M4 10h12M4 15h7"/></svg>
          </span>
          <span class="pop-01__name">Atlas Docs</span>
        </div>
        <nav class="pop-01__nav" aria-label="Documentation">
          <span class="pop-01__navitem">Guides</span>
          <span class="pop-01__navitem">Reference</span>
          <button class="pop-01__trigger" type="button" popovertarget="pop-01-panel">
            Release notes
            <svg viewBox="0 0 16 16" width="13" height="13" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M4 6.5 8 10.5 12 6.5"/></svg>
          </button>
        </nav>
      </header>

      <article class="pop-01__body">
        <p class="pop-01__eyebrow">Platform</p>
        <h2 class="pop-01__h">Floating panels, no positioning library</h2>
        <p class="pop-01__p">The button above is an invoker: it carries <code class="pop-01__code">popovertarget</code> and points at the id of an element with the <code class="pop-01__code">popover</code> attribute. Open it, then click anywhere on this paragraph — the panel closes itself. Press Escape and it closes too, and focus lands back on the button.</p>
        <p class="pop-01__p">This section has <code class="pop-01__code">overflow: hidden</code> and a stacking context, and the panel still paints over the header. That is the top layer, not a large z-index.</p>
      </article>

      <div class="pop-01__panel" popover="auto" id="pop-01-panel" role="group" aria-labelledby="pop-01-title">
        <div class="pop-01__phead">
          <h3 class="pop-01__ptitle" id="pop-01-title">Release notes</h3>
          <button class="pop-01__close" type="button" popovertarget="pop-01-panel" popovertargetaction="hide" aria-label="Close release notes">
            <svg viewBox="0 0 16 16" width="14" height="14" fill="none" stroke="currentColor" stroke-width="1.9" aria-hidden="true"><path d="M4 4l8 8M12 4l-8 8"/></svg>
          </button>
        </div>
        <ul class="pop-01__list">
          <li class="pop-01__item"><span class="pop-01__ver">4.2.0</span> Query cache keys are now stable across workers.</li>
          <li class="pop-01__item"><span class="pop-01__ver">4.1.6</span> Fixed a regression in the CSV importer on Windows line endings.</li>
          <li class="pop-01__item"><span class="pop-01__ver">4.1.5</span> Audit log entries keep the actor when a token is rotated.</li>
        </ul>
        <p class="pop-01__note">Escape closes this. So does a click anywhere outside it. Neither needed a line of JavaScript.</p>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.pop-01 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --paper: #f7f5f0;
  --surface: #ffffff;
  --ink: #1b1a17;
  --muted: #736e63;
  --rule: #e0dcd1;
  --accent: #1b1a17;
  --font-ui: ui-sans-serif, system-ui, "Segoe UI", sans-serif;
  --font-mono: ui-monospace, "SFMono-Regular", Menlo, monospace;
  background: var(--paper);
  color: var(--ink);
  font-family: var(--font-ui);
  padding: 36px 18px;
}

.pop-01__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  min-height: calc(100vh - 72px);
}

.pop-01__doc {
  inline-size: 100%;
  max-inline-size: 40rem;
  min-inline-size: 0;
  background: var(--surface);
  border: 1px solid var(--rule);
  border-radius: 6px;
  overflow: hidden;
  isolation: isolate;
}

.pop-01__bar {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  align-items: center;
  justify-content: space-between;
  padding: 12px 16px;
  border-bottom: 1px solid var(--rule);
}

.pop-01__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  min-inline-size: 0;
}

.pop-01__mark {
  display: inline-flex;
  color: var(--muted);
}

.pop-01__name {
  font-size: 13px;
  font-weight: 650;
  letter-spacing: -0.01em;
}

.pop-01__nav {
  display: flex;
  align-items: center;
  gap: 6px;
  flex-wrap: wrap;
  min-inline-size: 0;
}

.pop-01__navitem {
  font-size: 12.5px;
  color: var(--muted);
  padding: 0 8px;
}

.pop-01__trigger {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  min-height: 44px;
  padding: 0 14px;
  font: 650 12.5px/1 var(--font-ui);
  color: var(--surface);
  background: var(--accent);
  border: 1px solid var(--accent);
  border-radius: 5px;
  cursor: pointer;
}

.pop-01__trigger:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

.pop-01__body {
  padding: 26px 20px 30px;
}

.pop-01__eyebrow {
  margin: 0 0 10px;
  font: 700 10px/1 var(--font-ui);
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--muted);
}

.pop-01__h {
  margin: 0 0 14px;
  font: 600 clamp(21px, 4.6vw, 28px)/1.2 var(--font-ui);
  letter-spacing: -0.02em;
}

.pop-01__p {
  margin: 0 0 12px;
  font-size: 14.5px;
  line-height: 1.7;
  color: var(--muted);
  text-wrap: pretty;
}

.pop-01__code {
  font: 0.88em/1 var(--font-mono);
  color: var(--ink);
  background: rgba(115, 110, 99, 0.14);
  padding: 0.15em 0.35em;
  border-radius: 3px;
}

.pop-01__panel {
  position: fixed;
  margin: 0;
  inline-size: min(30rem, calc(100vw - 32px));
  max-inline-size: calc(100vw - 32px);
  padding: 18px;
  color: var(--ink);
  background: var(--surface);
  border: 1px solid var(--rule);
  border-radius: 6px;
  box-shadow: 0 18px 44px -22px rgba(27, 26, 23, 0.5);
}

.pop-01__phead {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  margin-bottom: 12px;
}

.pop-01__ptitle {
  margin: 0;
  font: 650 13px/1 var(--font-ui);
  letter-spacing: 0.02em;
}

.pop-01__close {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 44px;
  min-height: 44px;
  margin: -12px -10px -12px 0;
  color: var(--muted);
  background: none;
  border: 0;
  border-radius: 5px;
  cursor: pointer;
}

.pop-01__close:hover {
  color: var(--ink);
}

.pop-01__close:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 1px;
}

.pop-01__list {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: 1px;
  background: var(--rule);
  border: 1px solid var(--rule);
  border-radius: 5px;
  overflow: hidden;
}

.pop-01__item {
  display: flex;
  gap: 12px;
  align-items: baseline;
  padding: 11px 12px;
  background: var(--surface);
  font-size: 13px;
  line-height: 1.5;
  min-inline-size: 0;
}

.pop-01__ver {
  flex: none;
  font: 650 11px/1.4 var(--font-mono);
  color: var(--muted);
}

.pop-01__note {
  margin: 12px 0 0;
  font-size: 12px;
  line-height: 1.6;
  color: var(--muted);
}

@media (prefers-color-scheme: dark) {
  .pop-01 {
    --paper: #14140f;
    --surface: #1d1c17;
    --ink: #f3f0e6;
    --muted: #a09a8b;
    --rule: #322f26;
    --accent: #f3f0e6;
  }
}

[data-theme="dark"] .pop-01 {
  --paper: #14140f;
  --surface: #1d1c17;
  --ink: #f3f0e6;
  --muted: #a09a8b;
  --rule: #322f26;
  --accent: #f3f0e6;
}
```
