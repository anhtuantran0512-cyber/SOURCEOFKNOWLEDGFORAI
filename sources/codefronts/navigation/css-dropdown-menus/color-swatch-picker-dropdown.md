---
source: "codefronts"
url: "https://codefronts.com/navigation/css-dropdown-menus/color-swatch-picker-dropdown/"
title: "Color Swatch Picker Dropdown"
section: "navigation"
category: "css-dropdown-menus"
category_name: "CSS Dropdown Menu Designs"
description: "A color palette dropdown that reveals a grid of color swatches on hover, with a tooltip label appearing on individual swatch hover using CSS only."
has_js: "false"
---

Here's a working CSS Dropdown Menu Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Color Swatch Picker Dropdown
Source: https://codefronts.com/navigation/css-dropdown-menus/color-swatch-picker-dropdown/

A color palette dropdown that reveals a grid of color swatches on hover, with a tooltip label appearing on individual swatch hover using CSS only.
## HTML
```html
<div class="dd-15">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
  <div class="dd-15__scene">
    <div class="dd-15__control">
      <div class="dd-15__item">
        <button class="dd-15__trigger" style="--current:#6366f1">
          <span class="dd-15__swatch-dot"></span>
          <span>Color</span>
          <span class="dd-15__chevron">▾</span>
        </button>
        <div class="dd-15__panel">
          <p class="dd-15__panel-title">Choose a Color</p>
          <div class="dd-15__grid">
            <div class="dd-15__sw" style="--sw:#ef4444" data-name="Red"></div>
            <div class="dd-15__sw" style="--sw:#f97316" data-name="Orange"></div>
            <div class="dd-15__sw" style="--sw:#f59e0b" data-name="Amber"></div>
            <div class="dd-15__sw" style="--sw:#eab308" data-name="Yellow"></div>
            <div class="dd-15__sw" style="--sw:#84cc16" data-name="Lime"></div>
            <div class="dd-15__sw" style="--sw:#22c55e" data-name="Green"></div>
            <div class="dd-15__sw" style="--sw:#10b981" data-name="Emerald"></div>
            <div class="dd-15__sw" style="--sw:#14b8a6" data-name="Teal"></div>
            <div class="dd-15__sw" style="--sw:#06b6d4" data-name="Cyan"></div>
            <div class="dd-15__sw" style="--sw:#0ea5e9" data-name="Sky"></div>
            <div class="dd-15__sw" style="--sw:#3b82f6" data-name="Blue"></div>
            <div class="dd-15__sw" style="--sw:#6366f1" data-name="Indigo"></div>
            <div class="dd-15__sw" style="--sw:#8b5cf6" data-name="Violet"></div>
            <div class="dd-15__sw" style="--sw:#a855f7" data-name="Purple"></div>
            <div class="dd-15__sw" style="--sw:#d946ef" data-name="Fuchsia"></div>
            <div class="dd-15__sw" style="--sw:#ec4899" data-name="Pink"></div>
            <div class="dd-15__sw" style="--sw:#f43f5e" data-name="Rose"></div>
            <div class="dd-15__sw" style="--sw:#64748b" data-name="Slate"></div>
          </div>
        </div>
      </div>
    </div>
    <p class="dd-15__label">Hover the button to pick a palette color</p>
  </div>
</div>
```
## CSS
```css
.dd-15,
.dd-15 *,
.dd-15 *::before,
.dd-15 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.dd-15 ::selection {
  background: #6366f1;
  color: #fff;
}

.dd-15 {
  --surface: #fff;
  --border: #e2e8f0;
  --text: #0f172a;
  --muted: #64748b;
  font-family: 'Inter', sans-serif;
  min-height: 380px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #fafafa 0%, #f4f4f5 100%);
  padding: 40px 20px;
}

.dd-15__scene {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 24px;
}

.dd-15__control {
  position: relative;
  z-index: 100;
}

.dd-15__item {
  position: relative;
}

.dd-15__item::after {
  content: "";
  position: absolute;
  left: 0;
  right: 0;
  top: 100%;
  height: 10px;
  /* hover-bridge: invisible strip below the trigger covering
       the visible gap before the panel. Lives on .__item (not
       the panel, which has overflow:hidden / pointer-events:
       none in its closed state) so the parent :hover stays
       active while the cursor traverses the gap. */
}

.dd-15__trigger {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 16px;
  border: 1px solid var(--border);
  border-radius: 10px;
  background: var(--surface);
  cursor: pointer;
  font-family: inherit;
  font-size: 14px;
  font-weight: 500;
  color: var(--text);
  box-shadow: 0 1px 4px rgba(0,0,0,.05);
  transition: box-shadow 0.15s, border-color 0.15s;
}

.dd-15__trigger:hover,
.dd-15__item:hover .dd-15__trigger {
  box-shadow: 0 4px 16px rgba(0,0,0,.1);
  border-color: #c7d2fe;
}

.dd-15__swatch-dot {
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: var(--current, #6366f1);
  border: 2px solid rgba(255,255,255,0.8);
  box-shadow: 0 0 0 1px rgba(0,0,0,.12);
  flex-shrink: 0;
}

.dd-15__chevron {
  font-size: 11px;
  color: var(--muted);
  transition: transform 0.2s;
}

.dd-15__item:hover .dd-15__chevron {
  transform: rotate(180deg);
}
/* panel */

.dd-15__panel {
  position: absolute;
  top: calc(100% + 10px);
  left: 50%;
  transform: translateX(-50%) translateY(-6px);
  width: 220px;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 14px;
  box-shadow: 0 12px 40px rgba(0,0,0,.12);
  padding: 14px;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.2s ease, transform 0.28s cubic-bezier(0.16,1,0.3,1);
}

.dd-15__item:hover .dd-15__panel {
  opacity: 1;
  pointer-events: auto;
  transform: translateX(-50%) translateY(0);
}

.dd-15__panel-title {
  font-size: 11px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--muted);
  margin-bottom: 10px;
}

.dd-15__grid {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  gap: 6px;
}

.dd-15__sw {
  width: 26px;
  height: 26px;
  border-radius: 6px;
  background: var(--sw, #ccc);
  cursor: pointer;
  position: relative;
  transition: transform 0.15s, box-shadow 0.15s;
  box-shadow: 0 1px 3px rgba(0,0,0,.15);
}

.dd-15__sw:hover {
  transform: scale(1.22);
  box-shadow: 0 4px 10px rgba(0,0,0,.2);
  z-index: 2;
}
/* CSS tooltip via attr() */

.dd-15__sw::after {
  content: attr(data-name);
  position: absolute;
  bottom: calc(100% + 6px);
  left: 50%;
  transform: translateX(-50%);
  background: #0f172a;
  color: #fff;
  font-size: 10px;
  font-weight: 500;
  padding: 3px 7px;
  border-radius: 5px;
  white-space: nowrap;
  pointer-events: none;
  opacity: 0;
  transition: opacity 0.15s ease 0.1s;
}

.dd-15__sw:hover::after {
  opacity: 1;
}

.dd-15__label {
  font-size: 12.5px;
  color: var(--muted);
  font-style: italic;
}

@media (prefers-reduced-motion: reduce) {
  .dd-15__panel,
    .dd-15__sw,
    .dd-15__sw::after,
    .dd-15__chevron {
    transition: none;
  }
}
```
