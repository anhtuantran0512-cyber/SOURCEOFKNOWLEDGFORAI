---
source: "codefronts"
url: "https://codefronts.com/components/css-button-groups/css-icon-button-group-for-toolbar-actions-accessible-tooltips-pure-css/"
title: "CSS Icon Button Group for Toolbar Actions (Accessible Tooltips, Pure CSS)"
section: "components"
category: "css-button-groups"
category_name: "CSS Button Groups"
description: "A fused icon toolbar like the ones in Figma, Notion and Google Docs: bold / italic / underline / link / code as a segmented row of icon buttons with hover…"
has_js: "false"
---

Here's a working CSS Button Group from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Icon Button Group for Toolbar Actions (Accessible Tooltips, Pure CSS)
Source: https://codefronts.com/components/css-button-groups/css-icon-button-group-for-toolbar-actions-accessible-tooltips-pure-css/

A fused icon toolbar like the ones in Figma, Notion and Google Docs: bold / italic / underline / link / code as a segmented row of icon buttons with hover tooltips, pressed states and proper labels. The complete 'CSS icon button group toolbar' pattern — every icon button keeps a real accessible name, a 44px hit area and a keyboard focus ring.
## HTML
```html
<section class="btn-07" aria-label="Icon button group toolbar demo">
  <div class="btn-07__bar" role="toolbar" aria-label="Text formatting">
    <button type="button" class="btn-07__tool" aria-label="Bold" aria-pressed="true" data-tip="Bold"><svg viewBox="0 0 24 24" width="19" height="19" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M7 5h6a3.5 3.5 0 0 1 0 7H7zM7 12h7a3.5 3.5 0 0 1 0 7H7z"/></svg></button>
    <button type="button" class="btn-07__tool" aria-label="Italic" data-tip="Italic"><svg viewBox="0 0 24 24" width="19" height="19" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M14 5h-4M14 5l-4 14M14 19h-4"/></svg></button>
    <button type="button" class="btn-07__tool" aria-label="Underline" data-tip="Underline"><svg viewBox="0 0 24 24" width="19" height="19" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M7 4v7a5 5 0 0 0 10 0V4M6 21h12"/></svg></button>
    <span class="btn-07__div"></span>
    <button type="button" class="btn-07__tool" aria-label="Insert link" data-tip="Link"><svg viewBox="0 0 24 24" width="19" height="19" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M10 13a4 4 0 0 0 5.7.6l2.6-2.6a4 4 0 0 0-5.6-5.7l-1.5 1.5M14 11a4 4 0 0 0-5.7-.6L5.7 13a4 4 0 0 0 5.6 5.7l1.5-1.5"/></svg></button>
    <button type="button" class="btn-07__tool" aria-label="Inline code" data-tip="Code"><svg viewBox="0 0 24 24" width="19" height="19" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M9 8l-5 4 5 4M15 8l5 4-5 4"/></svg></button>
    <span class="btn-07__div"></span>
    <button type="button" class="btn-07__tool" aria-label="Clear formatting" data-tip="Clear"><svg viewBox="0 0 24 24" width="19" height="19" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M6 5h12M9 5l-2 14M15 5l1 7M5 19l14-14"/></svg></button>
  </div>
</section>
```
## CSS
```css
.btn-07,
.btn-07 *,
.btn-07 *::before,
.btn-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.btn-07 {
  --accent: oklch(0.7 0.17 135);
  --ink: #1a2415;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  background: linear-gradient(150deg,#20261c,#2c3626);
  padding: 130px 20px;
}

.btn-07__bar {
  display: inline-flex;
  align-items: center;
  gap: 2px;
  padding: 6px;
  background: #f4f7f0;
  border-radius: 16px;
  box-shadow: 0 20px 44px -20px rgba(0,0,0,.7),inset 0 0 0 1px rgba(255,255,255,.6);
}

.btn-07__tool {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 44px;
  height: 44px;
  border: none;
  background: none;
  color: #485a3d;
  border-radius: 11px;
  cursor: pointer;
  transition: background .14s,color .14s;
}

.btn-07__tool:hover {
  background: #e5ecdd;
  color: var(--ink);
}

.btn-07__tool[aria-pressed=true] {
  background: var(--accent);
  color: #12200a;
}

.btn-07__div {
  width: 1px;
  height: 26px;
  background: #d4ddca;
  margin: 0 4px;
}

.btn-07__tool::after {
  content: attr(data-tip);
  position: absolute;
  bottom: calc(100% + 10px);
  left: 50%;
  translate: -50% 0;
  background: var(--ink);
  color: #eef4e8;
  font-size: 12px;
  font-weight: 600;
  padding: 5px 9px;
  border-radius: 7px;
  white-space: nowrap;
  opacity: 0;
  pointer-events: none;
  transition: opacity .15s,translate .15s;
}

.btn-07__tool::before {
  content: "";
  position: absolute;
  bottom: calc(100% + 5px);
  left: 50%;
  translate: -50% 0;
  border: 5px solid transparent;
  border-top-color: var(--ink);
  opacity: 0;
  transition: opacity .15s;
}

.btn-07__tool:hover::after,
.btn-07__tool:focus-visible::after {
  opacity: 1;
  translate: -50% -3px;
}

.btn-07__tool:hover::before,
.btn-07__tool:focus-visible::before {
  opacity: 1;
}

.btn-07__tool:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
  z-index: 1;
}

@media (prefers-reduced-motion: reduce) {
  .btn-07__tool,
    .btn-07__tool::after {
    transition: none;
  }
}
```
