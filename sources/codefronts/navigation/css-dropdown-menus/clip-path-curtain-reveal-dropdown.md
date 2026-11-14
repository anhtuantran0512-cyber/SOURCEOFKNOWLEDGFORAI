---
source: "codefronts"
url: "https://codefronts.com/navigation/css-dropdown-menus/clip-path-curtain-reveal-dropdown/"
title: "Clip-Path Curtain Reveal Dropdown"
section: "navigation"
category: "css-dropdown-menus"
category_name: "CSS Dropdown Menu Designs"
description: "A dramatic curtain-wipe dropdown where the panel is revealed by animating a clip-path polygon from a collapsed top strip to full height."
has_js: "false"
---

Here's a working CSS Dropdown Menu Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Clip-Path Curtain Reveal Dropdown
Source: https://codefronts.com/navigation/css-dropdown-menus/clip-path-curtain-reveal-dropdown/

A dramatic curtain-wipe dropdown where the panel is revealed by animating a clip-path polygon from a collapsed top strip to full height.
## HTML
```html
<div class="dd-02">
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600&display=swap" rel="stylesheet">
  <nav class="dd-02__nav">
    <a href="#" class="dd-02__logo">Vertex</a>
    <div class="dd-02__items">
      <div class="dd-02__item">
        <button class="dd-02__trigger">Company ▾</button>
        <div class="dd-02__panel">
          <div class="dd-02__grid">
            <a href="#" class="dd-02__link">
              <span class="dd-02__badge">&#127959;</span>
              <span>About Us</span>
            </a>
            <a href="#" class="dd-02__link">
              <span class="dd-02__badge">&#128101;</span>
              <span>Careers</span>
            </a>
            <a href="#" class="dd-02__link">
              <span class="dd-02__badge">&#128240;</span>
              <span>Press</span>
            </a>
            <a href="#" class="dd-02__link">
              <span class="dd-02__badge">&#128205;</span>
              <span>Locations</span>
            </a>
          </div>
        </div>
      </div>
      <div class="dd-02__item">
        <button class="dd-02__trigger">Platform ▾</button>
        <div class="dd-02__panel">
          <div class="dd-02__grid">
            <a href="#" class="dd-02__link"><span class="dd-02__badge">&#9889;</span><span>Analytics</span></a>
            <a href="#" class="dd-02__link"><span class="dd-02__badge">&#128202;</span><span>Reporting</span></a>
            <a href="#" class="dd-02__link"><span class="dd-02__badge">&#128736;</span><span>Integrations</span></a>
            <a href="#" class="dd-02__link"><span class="dd-02__badge">&#128274;</span><span>Security</span></a>
          </div>
        </div>
      </div>
      <div class="dd-02__item">
        <button class="dd-02__trigger">Developers ▾</button>
        <div class="dd-02__panel">
          <div class="dd-02__grid">
            <a href="#" class="dd-02__link"><span class="dd-02__badge">&#128196;</span><span>API Docs</span></a>
            <a href="#" class="dd-02__link"><span class="dd-02__badge">&#129520;</span><span>SDKs</span></a>
            <a href="#" class="dd-02__link"><span class="dd-02__badge">&#127381;</span><span>Status</span></a>
          </div>
        </div>
      </div>
    </div>
  </nav>
</div>
```
## CSS
```css
.dd-02,
.dd-02 *,
.dd-02 *::before,
.dd-02 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.dd-02 ::selection {
  background: #f97316;
  color: #fff;
}

.dd-02 {
  --brand: #f97316;
  --surface: #fff;
  --text: #1c1917;
  --muted: #78716c;
  --border: #e7e5e4;
  --hover: #fff7ed;
  font-family: 'DM Sans', sans-serif;
  min-height: 360px;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  padding: 32px 20px;
  background: linear-gradient(160deg, #fff7ed 0%, #fef3c7 100%);
}

.dd-02__nav {
  display: flex;
  align-items: center;
  gap: 32px;
  background: var(--surface);
  border-bottom: 2px solid var(--border);
  padding: 14px 28px;
  width: 100%;
  max-width: 720px;
  border-radius: 12px;
  box-shadow: 0 2px 16px rgba(0,0,0,.06);
  position: relative;
  z-index: 100;
}

.dd-02__logo {
  font-size: 18px;
  font-weight: 700;
  color: var(--brand);
  text-decoration: none;
  letter-spacing: -0.5px;
  margin-right: auto;
}

.dd-02__items {
  display: flex;
  gap: 4px;
}

.dd-02__item {
  position: relative;
}

.dd-02__item::after {
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

.dd-02__trigger {
  background: none;
  border: none;
  cursor: pointer;
  padding: 8px 14px;
  font-size: 14px;
  font-weight: 500;
  color: var(--text);
  border-radius: 8px;
  transition: background 0.15s, color 0.15s;
  font-family: inherit;
}

.dd-02__trigger:hover,
.dd-02__item:hover .dd-02__trigger {
  background: var(--hover);
  color: var(--brand);
}
/* clip-path curtain panel */

.dd-02__panel {
  position: absolute;
  top: calc(100% + 10px);
  left: 50%;
  transform: translateX(-50%);
  min-width: 220px;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 12px;
  box-shadow: 0 16px 48px rgba(0,0,0,.12);
  overflow: hidden;
  clip-path: polygon(0 0, 100% 0, 100% 0, 0 0);
  opacity: 0;
  pointer-events: none;
  transition: clip-path 0.38s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.2s ease;
}

.dd-02__item:hover .dd-02__panel {
  clip-path: polygon(0 0, 100% 0, 100% 100%, 0 100%);
  opacity: 1;
  pointer-events: auto;
}

.dd-02__grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4px;
  padding: 8px;
}

.dd-02__link {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 12px;
  border-radius: 8px;
  text-decoration: none;
  color: var(--text);
  font-size: 13.5px;
  font-weight: 500;
  transition: background 0.15s;
}

.dd-02__link:hover {
  background: var(--hover);
  color: var(--brand);
}

.dd-02__badge {
  font-size: 16px;
  line-height: 1;
}

@media (prefers-reduced-motion: reduce) {
  .dd-02__panel {
    transition: none;
  }
}
```
