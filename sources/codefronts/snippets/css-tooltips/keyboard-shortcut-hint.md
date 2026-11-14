---
source: "codefronts"
url: "https://codefronts.com/snippets/css-tooltips/keyboard-shortcut-hint/"
title: "Keyboard Shortcut Hint"
section: "snippets"
category: "css-tooltips"
category_name: "CSS Tooltips"
description: "A compact label-plus-keycap pill for productivity apps."
has_js: "false"
---

Here's a working CSS Tooltip from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Keyboard Shortcut Hint
Source: https://codefronts.com/snippets/css-tooltips/keyboard-shortcut-hint/

A compact label-plus-keycap pill for productivity apps. Each tooltip wears its shortcut as little 3D keycaps that depress on a loop while the tooltip is shown — the closest pure-CSS can get to communicating "this is a real chord, try it." A 400ms delay keeps it out of the way on quick mouse passes.
## HTML
```html
<div class="tp-02">
  <div class="tp-02__shell">
    <div class="tp-02__titlebar">
      <span class="tp-02__tdot"></span><span class="tp-02__tdot"></span><span class="tp-02__tdot"></span>
      <span class="tp-02__ttitle">Untitled Document — Composer</span>
    </div>
    <div class="tp-02__toolbar">
      <div class="tp-02__group">
        <button class="tp-02__btn" type="button" aria-label="Save">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
          <span class="tp-02__tip">
            <span class="tp-02__tip-label">Save</span>
            <span class="tp-02__tip-keys"><span class="tp-02__key">⌘</span><span class="tp-02__key">S</span></span>
          </span>
        </button>
        <button class="tp-02__btn" type="button" aria-label="Undo">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="1 4 1 10 7 10"/><path d="M3.51 15a9 9 0 1 0 2.13-9.36L1 10"/></svg>
          <span class="tp-02__tip">
            <span class="tp-02__tip-label">Undo</span>
            <span class="tp-02__tip-keys"><span class="tp-02__key">⌘</span><span class="tp-02__key">Z</span></span>
          </span>
        </button>
        <button class="tp-02__btn" type="button" aria-label="Redo">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="23 4 23 10 17 10"/><path d="M20.49 15a9 9 0 1 1-2.13-9.36L23 10"/></svg>
          <span class="tp-02__tip">
            <span class="tp-02__tip-label">Redo</span>
            <span class="tp-02__tip-keys"><span class="tp-02__key">⌘</span><span class="tp-02__key">⇧</span><span class="tp-02__key">Z</span></span>
          </span>
        </button>
      </div>
      <div class="tp-02__group">
        <button class="tp-02__btn tp-02__btn-active" type="button" aria-label="Bold">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 4h8a4 4 0 0 1 4 4 4 4 0 0 1-4 4H6z"/><path d="M6 12h9a4 4 0 0 1 4 4 4 4 0 0 1-4 4H6z"/></svg>
          <span class="tp-02__tip">
            <span class="tp-02__tip-label">Bold</span>
            <span class="tp-02__tip-keys"><span class="tp-02__key">⌘</span><span class="tp-02__key">B</span></span>
          </span>
        </button>
        <button class="tp-02__btn" type="button" aria-label="Italic">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="19" y1="4" x2="10" y2="4"/><line x1="14" y1="20" x2="5" y2="20"/><line x1="15" y1="4" x2="9" y2="20"/></svg>
          <span class="tp-02__tip">
            <span class="tp-02__tip-label">Italic</span>
            <span class="tp-02__tip-keys"><span class="tp-02__key">⌘</span><span class="tp-02__key">I</span></span>
          </span>
        </button>
        <button class="tp-02__btn" type="button" aria-label="Underline">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 3v7a6 6 0 0 0 6 6 6 6 0 0 0 6-6V3"/><line x1="4" y1="21" x2="20" y2="21"/></svg>
          <span class="tp-02__tip">
            <span class="tp-02__tip-label">Underline</span>
            <span class="tp-02__tip-keys"><span class="tp-02__key">⌘</span><span class="tp-02__key">U</span></span>
          </span>
        </button>
      </div>
      <div class="tp-02__group">
        <button class="tp-02__btn" type="button" aria-label="Align Left">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="17" y1="10" x2="3" y2="10"/><line x1="21" y1="6" x2="3" y2="6"/><line x1="21" y1="14" x2="3" y2="14"/><line x1="17" y1="18" x2="3" y2="18"/></svg>
          <span class="tp-02__tip tp-02__tip-ext">
            <span class="tp-02__tip-row">
              <span class="tp-02__tip-label">Align Left</span>
              <span class="tp-02__tip-keys"><span class="tp-02__key">⌘</span><span class="tp-02__key">⇧</span><span class="tp-02__key">L</span></span>
            </span>
            <span class="tp-02__tip-desc">Aligns the current paragraph to the left edge of the column.</span>
          </span>
        </button>
        <button class="tp-02__btn" type="button" aria-label="Settings">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09a1.65 1.65 0 0 0-1-1.51 1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09a1.65 1.65 0 0 0 1.51-1 1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 2.83-2.83l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>
          <span class="tp-02__tip">
            <span class="tp-02__tip-label">Settings</span>
            <span class="tp-02__tip-keys"><span class="tp-02__key">⌘</span><span class="tp-02__key">,</span></span>
          </span>
        </button>
      </div>
    </div>
    <div class="tp-02__content">
      <h3 class="tp-02__h">The cursor as a finger.</h3>
      <p class="tp-02__p">Hover any toolbar button to see its keycap; the keys depress on a loop, the way a real chord would feel if you held the gesture <em>just</em> long enough to second-guess it.</p>
    </div>
  </div>
</div>
```
## CSS
```css
.tp-02 {
  width: 100%;
  min-height: 100vh;
  background: #f5f5f3;
  /* Top room for the small keycap tooltips popping up from each
       toolbar button. ~130px is enough since these tips are compact. */
  padding: 130px 28px 60px;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  font-family: 'Inter', system-ui, sans-serif;
  color: #1a1a1a;
}

.tp-02__shell {
  width: 100%;
  max-width: 600px;
  background: #fff;
  border: 1px solid rgba(0, 0, 0, 0.08);
  border-radius: 10px;
  overflow: visible;
  box-shadow: 0 20px 48px -16px rgba(0, 0, 0, 0.15);
}

.tp-02__titlebar {
  height: 34px;
  background: #fafaf8;
  border-bottom: 1px solid rgba(0, 0, 0, 0.06);
  display: flex;
  align-items: center;
  padding: 0 12px;
  gap: 7px;
  border-radius: 10px 10px 0 0;
}

.tp-02__tdot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: #e2e2de;
}

.tp-02__ttitle {
  flex: 1;
  text-align: center;
  font-family: 'Inter', system-ui, sans-serif;
  font-size: 11.5px;
  color: rgba(0, 0, 0, 0.5);
  letter-spacing: 0.02em;
}

.tp-02__toolbar {
  display: flex;
  align-items: center;
  padding: 10px 12px;
  border-bottom: 1px solid rgba(0, 0, 0, 0.05);
  gap: 4px;
  overflow: visible;
  flex-wrap: wrap;
}

.tp-02__group {
  display: flex;
  gap: 2px;
  padding: 0 6px;
  border-right: 1px solid rgba(0, 0, 0, 0.08);
}

.tp-02__group:last-child {
  border-right: none;
}

.tp-02__btn {
  width: 34px;
  height: 34px;
  border-radius: 7px;
  background: transparent;
  border: none;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  position: relative;
  color: #444;
  transition: background 0.15s, color 0.15s;
  font-family: 'Inter', system-ui, sans-serif;
  padding: 0;
}

.tp-02__btn:hover {
  background: #f0f0ec;
  color: #111;
}

.tp-02__btn-active {
  background: #e8e8e4;
  color: #111;
}

.tp-02__btn svg {
  width: 17px;
  height: 17px;
}

.tp-02__tip {
  position: absolute;
  bottom: calc(100% + 10px);
  left: 50%;
  transform: translateX(-50%) translateY(4px);
  background: #1a1a1a;
  color: #fff;
  padding: 7px 10px;
  border-radius: 7px;
  font-family: 'Inter', system-ui, sans-serif;
  font-size: 11.5px;
  white-space: nowrap;
  display: flex;
  align-items: center;
  gap: 9px;
  opacity: 0;
  visibility: hidden;
  transition: opacity 0.2s, transform 0.25s cubic-bezier(0.22, 1, 0.36, 1), visibility 0s linear 0.2s;
  z-index: 50;
  pointer-events: none;
  box-shadow: 0 6px 18px -4px rgba(0, 0, 0, 0.3), 0 2px 6px -2px rgba(0, 0, 0, 0.2);
}

.tp-02__btn:hover .tp-02__tip {
  opacity: 1;
  visibility: visible;
  transform: translateX(-50%) translateY(0);
  transition-delay: 0.4s, 0.4s, 0s;
}

.tp-02__tip::after {
  content: '';
  position: absolute;
  top: 100%;
  left: 50%;
  transform: translate(-50%, -50%) rotate(45deg);
  width: 7px;
  height: 7px;
  background: #1a1a1a;
}

.tp-02__tip-label {
  font-weight: 500;
  letter-spacing: 0.01em;
}

.tp-02__tip-keys {
  display: flex;
  gap: 3px;
}

.tp-02__key {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 20px;
  height: 20px;
  padding: 0 5px;
  background: linear-gradient(180deg, #3d3d3d 0%, #2a2a2a 100%);
  border: 1px solid #4a4a4a;
  border-bottom-width: 2px;
  border-radius: 4px;
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-size: 10px;
  color: #f5f5f3;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.08);
  transition: transform 0.1s, border-bottom-width 0.1s, box-shadow 0.1s;
}

.tp-02__btn:hover .tp-02__key {
  animation: tp-02-press 1.6s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}

.tp-02__btn:hover .tp-02__key:nth-child(2) {
  animation-delay: 0.1s;
}

.tp-02__btn:hover .tp-02__key:nth-child(3) {
  animation-delay: 0.2s;
}

@keyframes tp-02-press {
  0%,
    50%,
    100% {
    transform: translateY(0);
    border-bottom-width: 2px;
  }

  25% {
    transform: translateY(1px);
    border-bottom-width: 1px;
    box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.04);
  }
}

.tp-02__tip-ext {
  padding: 10px 12px;
  flex-direction: column;
  align-items: flex-start;
  gap: 7px;
  white-space: normal;
  width: 200px;
  text-align: left;
}

.tp-02__tip-row {
  display: flex;
  width: 100%;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
}

.tp-02__tip-desc {
  font-size: 10.5px;
  color: rgba(255, 255, 255, 0.6);
  line-height: 1.5;
  padding-top: 5px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  width: 100%;
}

.tp-02__content {
  padding: 28px 36px 36px;
  font-family: 'Inter', system-ui, sans-serif;
  color: rgba(0, 0, 0, 0.6);
  font-size: 13px;
  line-height: 1.7;
}

.tp-02__h {
  font-family: Georgia, serif;
  font-weight: 400;
  font-size: 24px;
  color: #111;
  margin: 0 0 10px;
  letter-spacing: -0.01em;
}

.tp-02__p {
  max-width: 480px;
  margin: 0;
}

.tp-02__p em {
  color: #2d6a4f;
  font-family: Georgia, serif;
  font-style: italic;
  font-weight: 500;
}
```
