---
source: "codefronts"
url: "https://codefronts.com/navigation/css-dropdown-menus/underline-nav-fade-panel-dropdown/"
title: "Underline Nav Fade Panel Dropdown"
section: "navigation"
category: "css-dropdown-menus"
category_name: "CSS Dropdown Menu Designs"
description: "An editorial navigation style where a scaleX underline sweeps under the active trigger and a clean panel fades in below with category links."
has_js: "false"
---

Here's a working CSS Dropdown Menu Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Underline Nav Fade Panel Dropdown
Source: https://codefronts.com/navigation/css-dropdown-menus/underline-nav-fade-panel-dropdown/

An editorial navigation style where a scaleX underline sweeps under the active trigger and a clean panel fades in below with category links.
## HTML
```html
<div class="dd-08">
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,wght@0,400;0,600;1,400&family=Inter:wght@400;500&display=swap" rel="stylesheet">
  <nav class="dd-08__nav">
    <a href="#" class="dd-08__brand">The&nbsp;<em>Edit</em></a>
    <div class="dd-08__items">
      <div class="dd-08__item" style="--accent:#d97706">
        <a href="#" class="dd-08__trigger">Collections</a>
        <div class="dd-08__panel">
          <div class="dd-08__col">
            <a href="#" class="dd-08__link">Spring 2025</a>
            <a href="#" class="dd-08__link">Essentials</a>
            <a href="#" class="dd-08__link">Archive</a>
          </div>
          <div class="dd-08__col">
            <a href="#" class="dd-08__link">Collaborations</a>
            <a href="#" class="dd-08__link">Limited Editions</a>
            <a href="#" class="dd-08__link">Lookbook</a>
          </div>
        </div>
      </div>
      <div class="dd-08__item" style="--accent:#059669">
        <a href="#" class="dd-08__trigger">Stories</a>
        <div class="dd-08__panel">
          <div class="dd-08__col">
            <a href="#" class="dd-08__link">Feature Articles</a>
            <a href="#" class="dd-08__link">Interviews</a>
            <a href="#" class="dd-08__link">Profiles</a>
          </div>
          <div class="dd-08__col">
            <a href="#" class="dd-08__link">Photography</a>
            <a href="#" class="dd-08__link">Film</a>
          </div>
        </div>
      </div>
      <div class="dd-08__item" style="--accent:#7c3aed">
        <a href="#" class="dd-08__trigger">Studio</a>
        <div class="dd-08__panel">
          <div class="dd-08__col">
            <a href="#" class="dd-08__link">About Us</a>
            <a href="#" class="dd-08__link">Process</a>
            <a href="#" class="dd-08__link">Careers</a>
          </div>
        </div>
      </div>
    </div>
  </nav>
</div>
```
## CSS
```css
.dd-08,
.dd-08 *,
.dd-08 *::before,
.dd-08 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.dd-08 ::selection {
  background: #1e293b;
  color: #f8fafc;
}

.dd-08 {
  --text: #1e293b;
  --muted: #64748b;
  --surface: #fff;
  --border: #e2e8f0;
  font-family: 'Inter', sans-serif;
  min-height: 360px;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  padding: 32px 20px;
  background: #fafaf8;
}

.dd-08__nav {
  display: flex;
  align-items: center;
  gap: 0;
  background: var(--surface);
  border-bottom: 2px solid var(--border);
  width: 100%;
  max-width: 680px;
  padding: 0 24px;
  position: relative;
  z-index: 100;
}

.dd-08__brand {
  font-family: 'Fraunces', serif;
  font-size: 22px;
  font-weight: 600;
  color: var(--text);
  text-decoration: none;
  padding: 18px 0;
  margin-right: 32px;
  letter-spacing: -0.5px;
}

.dd-08__brand em {
  font-style: italic;
  color: #d97706;
}

.dd-08__items {
  display: flex;
  gap: 0;
}

.dd-08__item {
  position: relative;
}

.dd-08__item::after {
  content: "";
  position: absolute;
  left: 0;
  right: 0;
  top: 100%;
  height: 2px;
  /* hover-bridge: invisible strip below the trigger covering
       the visible gap before the panel. Lives on .__item (not
       the panel, which has overflow:hidden / pointer-events:
       none in its closed state) so the parent :hover stays
       active while the cursor traverses the gap. */
}

.dd-08__trigger {
  display: block;
  padding: 18px 16px;
  color: var(--muted);
  text-decoration: none;
  font-size: 13.5px;
  font-weight: 500;
  letter-spacing: 0.02em;
  position: relative;
  transition: color 0.18s;
}
/* scaleX underline */

.dd-08__trigger::after {
  content: '';
  position: absolute;
  bottom: -2px;
  left: 16px;
  right: 16px;
  height: 2px;
  background: var(--accent, var(--text));
  transform: scaleX(0);
  transform-origin: left center;
  transition: transform 0.24s ease-out;
  border-radius: 1px;
}

.dd-08__item:hover .dd-08__trigger {
  color: var(--text);
}

.dd-08__item:hover .dd-08__trigger::after {
  transform: scaleX(1);
}
/* panel */

.dd-08__panel {
  position: absolute;
  top: calc(100% + 2px);
  left: 0;
  background: var(--surface);
  border: 1px solid var(--border);
  border-top: none;
  border-radius: 0 0 12px 12px;
  box-shadow: 0 12px 32px rgba(0,0,0,.08);
  padding: 20px 24px;
  display: flex;
  gap: 32px;
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transition: opacity 0.22s ease, visibility 0s linear 0.22s;
}

.dd-08__item:hover .dd-08__panel {
  opacity: 1;
  visibility: visible;
  pointer-events: auto;
  transition: opacity 0.22s ease, visibility 0s linear 0s;
}

.dd-08__col {
  display: flex;
  flex-direction: column;
  gap: 4px;
  min-width: 140px;
}

.dd-08__link {
  display: block;
  padding: 6px 0;
  color: var(--muted);
  text-decoration: none;
  font-family: 'Fraunces', serif;
  font-size: 15px;
  font-weight: 400;
  transition: color 0.15s;
  border-bottom: 1px solid transparent;
}

.dd-08__link:hover {
  color: var(--text);
  border-bottom-color: var(--accent, var(--text));
}

@media (prefers-reduced-motion: reduce) {
  .dd-08__panel,
    .dd-08__trigger::after {
    transition: none;
  }
}
```
