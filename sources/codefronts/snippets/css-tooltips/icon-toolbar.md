---
source: "codefronts"
url: "https://codefronts.com/snippets/css-tooltips/icon-toolbar/"
title: "Icon Toolbar"
section: "snippets"
category: "css-tooltips"
category_name: "CSS Tooltips"
description: "Unlabeled toolbar icons — bold, italic, link, image, code, list, settings — that reveal their action name on hover."
has_js: "false"
---

Here's a working CSS Tooltip from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Icon Toolbar
Source: https://codefronts.com/snippets/css-tooltips/icon-toolbar/

Unlabeled toolbar icons — bold, italic, link, image, code, list, settings — that reveal their action name on hover. The tooltip is a compact dark pill with a tail arrow, the workhorse pattern every desktop app ships and every web app should. For editors, design tools, dashboards.
## HTML
```html
<div class="tp-20">
  <div class="tp-20__wrap">
    <div class="tp-20__bar">
      <span class="tp-20__t">
        <button class="tp-20__btn tp-20__btn-active">B</button>
        <span class="tp-20__tip">Bold</span>
      </span>
      <span class="tp-20__t">
        <button class="tp-20__btn" style="font-style:italic">I</button>
        <span class="tp-20__tip">Italic</span>
      </span>
      <span class="tp-20__t">
        <button class="tp-20__btn" style="text-decoration:underline">U</button>
        <span class="tp-20__tip">Underline</span>
      </span>
      <span class="tp-20__t">
        <button class="tp-20__btn" style="text-decoration:line-through;color:#666">S</button>
        <span class="tp-20__tip">Strikethrough</span>
      </span>
      <span class="tp-20__sep"></span>
      <span class="tp-20__t">
        <button class="tp-20__btn"><svg viewBox="0 0 16 16" aria-hidden="true"><path d="M6.354 5.5H4a3 3 0 0 0 0 6h3a3 3 0 0 0 2.83-4H9v.5A2 2 0 0 1 7 9.5H4a2 2 0 0 1 0-4h1.535c.218-.376.495-.717.82-1z"/><path d="M9 5.5a3 3 0 0 0-2.83 4h1.098A2 2 0 0 1 9 6.5h3a2 2 0 1 1 0 4h-1.535a4 4 0 0 1-.82 1H12a3 3 0 1 0 0-6H9z"/></svg></button>
        <span class="tp-20__tip">Insert link</span>
      </span>
      <span class="tp-20__t">
        <button class="tp-20__btn"><svg viewBox="0 0 16 16" aria-hidden="true"><path d="M6.002 5.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0z"/><path d="M2.002 1a2 2 0 0 0-2 2v10a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2h-12zm12 1a1 1 0 0 1 1 1v6.5l-3.777-1.947a.5.5 0 0 0-.577.093l-3.71 3.71-2.66-1.772a.5.5 0 0 0-.63.062L1.002 12V3a1 1 0 0 1 1-1h12z"/></svg></button>
        <span class="tp-20__tip">Insert image</span>
      </span>
      <span class="tp-20__t">
        <button class="tp-20__btn tp-20__btn-code">&lt;/&gt;</button>
        <span class="tp-20__tip">Code block</span>
      </span>
      <span class="tp-20__sep"></span>
      <span class="tp-20__t">
        <button class="tp-20__btn"><svg viewBox="0 0 16 16" aria-hidden="true"><path fill-rule="evenodd" d="M5 11.5a.5.5 0 0 1 .5-.5h9a.5.5 0 0 1 0 1h-9a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h9a.5.5 0 0 1 0 1h-9a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h9a.5.5 0 0 1 0 1h-9a.5.5 0 0 1-.5-.5zm-3 1a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm0 4a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm0 4a1 1 0 1 0 0-2 1 1 0 0 0 0 2z"/></svg></button>
        <span class="tp-20__tip">Bullet list</span>
      </span>
      <span class="tp-20__t">
        <button class="tp-20__btn"><svg viewBox="0 0 16 16" aria-hidden="true"><path d="M14 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h12zM2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z"/><path d="M10.97 4.97a.75.75 0 0 1 1.071 1.05l-3.992 4.99a.75.75 0 0 1-1.08.02L4.324 8.384a.75.75 0 1 1 1.06-1.06l2.094 2.093 3.473-4.425a.235.235 0 0 1 .02-.022z"/></svg></button>
        <span class="tp-20__tip">Checklist</span>
      </span>
      <span class="tp-20__sep"></span>
      <span class="tp-20__t">
        <button class="tp-20__btn"><svg viewBox="0 0 16 16" aria-hidden="true"><path d="M9.405 1.05c-.413-1.4-2.397-1.4-2.81 0l-.1.34a1.464 1.464 0 0 1-2.105.872l-.31-.17c-1.283-.698-2.686.705-1.987 1.987l.169.311c.446.82.023 1.841-.872 2.105l-.34.1c-1.4.413-1.4 2.397 0 2.81l.34.1a1.464 1.464 0 0 1 .872 2.105l-.17.31c-.698 1.283.705 2.686 1.987 1.987l.311-.169a1.464 1.464 0 0 1 2.105.872l.1.34c.413 1.4 2.397 1.4 2.81 0l.1-.34a1.464 1.464 0 0 1 2.105-.872l.31.17c1.283.698 2.686-.705 1.987-1.987l-.169-.311a1.464 1.464 0 0 1 .872-2.105l.34-.1c1.4-.413 1.4-2.397 0-2.81l-.34-.1a1.464 1.464 0 0 1-.872-2.105l.17-.31c.698-1.283-.705-2.686-1.987-1.987l-.311.169a1.464 1.464 0 0 1-2.105-.872l-.1-.34zM8 10.93a2.929 2.929 0 1 1 0-5.86 2.929 2.929 0 0 1 0 5.858z"/></svg></button>
        <span class="tp-20__tip">Preferences</span>
      </span>
    </div>
  </div>
</div>
```
## CSS
```css
.tp-20 {
  width: 100%;
  min-height: 100vh;
  background: #141414;
  /* Top room — labels pop UP from each button, ~30px tall. */
  padding: 80px 28px 60px;
  font-family: system-ui, -apple-system, sans-serif;
}

.tp-20__wrap {
  display: flex;
  justify-content: center;
}

.tp-20__bar {
  display: inline-flex;
  align-items: center;
  gap: 2px;
  background: #1f1f1f;
  border: 1px solid #2a2a2a;
  border-radius: 8px;
  padding: 5px;
}

.tp-20__sep {
  width: 1px;
  height: 20px;
  background: #2e2e2e;
  margin: 0 4px;
  flex-shrink: 0;
  display: inline-block;
}

.tp-20__t {
  position: relative;
  display: inline-block;
}

.tp-20__btn {
  width: 32px;
  height: 32px;
  border-radius: 5px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  cursor: help;
  color: #888;
  font-size: 13px;
  font-weight: 600;
  transition: background .12s, color .12s;
  border: none;
  background: transparent;
  letter-spacing: 0;
  font-family: inherit;
}

.tp-20__btn:hover {
  background: #2a2a2a;
  color: #e0e0e0;
}

.tp-20__btn-active {
  background: #2a2a2a;
  color: #fff;
}

.tp-20__btn-code {
  font-family: ui-monospace, monospace;
  font-size: 11px;
  font-weight: 700;
}

.tp-20__btn svg {
  width: 15px;
  height: 15px;
  fill: currentColor;
}

.tp-20__tip {
  position: absolute;
  bottom: calc(100% + 8px);
  left: 50%;
  transform: translateX(-50%) translateY(4px);
  background: #18181b;
  color: #fff;
  font-size: 11.5px;
  padding: 5px 10px;
  border-radius: 5px;
  white-space: nowrap;
  pointer-events: none;
  opacity: 0;
  visibility: hidden;
  transition: opacity .14s, transform .14s cubic-bezier(0.22, 1, 0.36, 1), visibility 0s linear .14s;
  z-index: 100;
  line-height: 1;
  display: block;
}

.tp-20__t:hover .tp-20__tip {
  opacity: 1;
  visibility: visible;
  transform: translateX(-50%) translateY(0);
  transition-delay: 0s;
}

.tp-20__tip::after {
  content: '';
  position: absolute;
  top: 100%;
  left: 50%;
  transform: translateX(-50%);
  border: 4px solid transparent;
  border-top-color: #18181b;
}
```
