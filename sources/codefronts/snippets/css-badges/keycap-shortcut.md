---
source: "codefronts"
url: "https://codefronts.com/snippets/css-badges/keycap-shortcut/"
title: "Keycap Shortcut"
section: "snippets"
category: "css-badges"
category_name: "CSS Badges"
description: "A key is a physical object."
has_js: "true"
---

Here's a working CSS Badge from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Keycap Shortcut
Source: https://codefronts.com/snippets/css-badges/keycap-shortcut/

A key is a physical object. Three stacked box-shadows form the edge — bottom face, outer drop, top highlight. Click any key and feel it go down. Cmd-K and friends, the way they were meant to look.
## HTML
```html
<div class="bdg-04-stage">
  <div class="bdg-04-combo-row">
    <div class="bdg-04-combo">
      <div class="bdg-04-cap bdg-04-wide">⌘</div>
      <div class="bdg-04-sep">+</div>
      <div class="bdg-04-cap">K</div>
    </div>
    <div class="bdg-04-combo-label">Command Palette</div>
  </div>

  <div class="bdg-04-combo-row">
    <div class="bdg-04-combo">
      <div class="bdg-04-cap bdg-04-wide">⌘</div>
      <div class="bdg-04-sep">+</div>
      <div class="bdg-04-cap bdg-04-wide">⇧</div>
      <div class="bdg-04-sep">+</div>
      <div class="bdg-04-cap">P</div>
    </div>
    <div class="bdg-04-combo-label">Quick Actions</div>
  </div>

  <div class="bdg-04-combo-row">
    <div class="bdg-04-combo">
      <div class="bdg-04-cap bdg-04-wide">⌥</div>
      <div class="bdg-04-sep">+</div>
      <div class="bdg-04-cap bdg-04-xl">⌫</div>
    </div>
    <div class="bdg-04-combo-label">Delete Word</div>
  </div>
</div>
```
## CSS
```css
.bdg-04-stage {
  background: #edecea;
  padding: 60px 48px;
  display: flex;
  flex-direction: column;
  gap: 32px;
  justify-content: center;
  align-items: center;
  width: 100%;
  min-height: 100vh;
}

.bdg-04-combo {
  display: flex;
  align-items: center;
  gap: 6px;
}

.bdg-04-sep {
  font-family: system-ui, "Bricolage Grotesque", sans-serif;
  font-size: 14px;
  color: #888;
  padding: 0 2px;
}

.bdg-04-cap {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 44px;
  height: 44px;
  padding: 0 12px;
  background: linear-gradient(180deg, #f8f8f6 0%, #e8e8e3 100%);
  border: 1px solid #bbb;
  border-radius: 6px;
  font-family: ui-monospace, "JetBrains Mono", monospace;
  font-size: 14px;
  font-weight: 500;
  color: #1a1a1a;
  letter-spacing: 0;
  cursor: pointer;
  user-select: none;
  box-shadow: 0 1px 0 rgba(255,255,255,0.9) inset, 0 -1px 0 rgba(0,0,0,0.08) inset, 0 3px 0 #999, 0 4px 4px rgba(0,0,0,0.18);
  transition: transform 0.06s, box-shadow 0.06s;
  position: relative;
}

.bdg-04-cap::before {
  content: '';
  position: absolute;
  inset: 2px 2px 6px;
  border-radius: 4px;
  border-top: 1px solid rgba(255,255,255,0.6);
  pointer-events: none;
}

.bdg-04-cap:active,
.bdg-04-cap.is-pressed {
  transform: translateY(2px);
  box-shadow: 0 1px 0 rgba(255,255,255,0.9) inset, 0 -1px 0 rgba(0,0,0,0.08) inset, 0 1px 0 #999, 0 2px 2px rgba(0,0,0,0.18);
}

.bdg-04-wide {
  min-width: 72px;
  font-size: 13px;
}

.bdg-04-xl {
  min-width: 96px;
  font-size: 13px;
}

.bdg-04-combo-label {
  font-family: system-ui, "Bricolage Grotesque", sans-serif;
  font-size: 10px;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: #888;
  text-align: center;
  margin-top: 6px;
}

.bdg-04-combo-row {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
}
```

## JavaScript
```js
// Click any key to depress it briefly. Matches the CSS :active state
// but lets the visual hold for 200ms so the press registers visually
// even on a quick tap.
document.querySelectorAll('.bdg-04-cap').forEach(function (k) {
  k.addEventListener('click', function () {
    k.classList.add('is-pressed');
    setTimeout(function () { k.classList.remove('is-pressed'); }, 200);
  });
});
```
