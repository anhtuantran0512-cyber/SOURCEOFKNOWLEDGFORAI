---
source: "codefronts"
url: "https://codefronts.com/navigation/css-dropdown-menus/mega-menu-grid-dropdown/"
title: "Mega Menu Grid Dropdown"
section: "navigation"
category: "css-dropdown-menus"
category_name: "CSS Dropdown Menu Designs"
description: "A full-width mega menu that spans the entire nav bar and organizes links into a multi-column CSS Grid layout with section headings and featured content."
has_js: "false"
---

Here's a working CSS Dropdown Menu Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Mega Menu Grid Dropdown
Source: https://codefronts.com/navigation/css-dropdown-menus/mega-menu-grid-dropdown/

A full-width mega menu that spans the entire nav bar and organizes links into a multi-column CSS Grid layout with section headings and featured content.
## HTML
```html
<div class="dd-07">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <div class="dd-07__wrapper">
    <nav class="dd-07__nav">
      <span class="dd-07__brand">Prism</span>
      <div class="dd-07__items">
        <a href="#" class="dd-07__simple">Home</a>
        <div class="dd-07__item">
          <a href="#" class="dd-07__trigger">Platform ▾</a>
          <div class="dd-07__mega">
            <div class="dd-07__col">
              <p class="dd-07__heading">Core</p>
              <a href="#" class="dd-07__link">&#128202; Analytics</a>
              <a href="#" class="dd-07__link">&#128736; Integrations</a>
              <a href="#" class="dd-07__link">&#127381; Automations</a>
              <a href="#" class="dd-07__link">&#128274; Security</a>
            </div>
            <div class="dd-07__col">
              <p class="dd-07__heading">Growth</p>
              <a href="#" class="dd-07__link">&#128184; Revenue Ops</a>
              <a href="#" class="dd-07__link">&#127775; Marketing Suite</a>
              <a href="#" class="dd-07__link">&#128101; CRM</a>
              <a href="#" class="dd-07__link">&#128172; Support Hub</a>
            </div>
            <div class="dd-07__col">
              <p class="dd-07__heading">Infra</p>
              <a href="#" class="dd-07__link">&#9928; Edge CDN</a>
              <a href="#" class="dd-07__link">&#128190; Storage</a>
              <a href="#" class="dd-07__link">&#9881; Config</a>
              <a href="#" class="dd-07__link">&#128203; Logs</a>
            </div>
            <div class="dd-07__featured">
              <p class="dd-07__heading">What's New</p>
              <div class="dd-07__card">
                <span class="dd-07__new">NEW</span>
                <p class="dd-07__card-title">AI Copilot</p>
                <p class="dd-07__card-desc">Intelligent workflow automation powered by large language models.</p>
                <a href="#" class="dd-07__card-link">Learn more &#8594;</a>
              </div>
            </div>
          </div>
        </div>
        <a href="#" class="dd-07__simple">Pricing</a>
        <a href="#" class="dd-07__simple">Docs</a>
      </div>
      <a href="#" class="dd-07__cta">Sign Up Free</a>
    </nav>
  </div>
</div>
```
## CSS
```css
.dd-07,
.dd-07 *,
.dd-07 *::before,
.dd-07 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.dd-07 ::selection {
  background: #0ea5e9;
  color: #fff;
}

.dd-07 {
  --brand: #0ea5e9;
  --surface: #fff;
  --text: #0f172a;
  --muted: #64748b;
  --border: #e2e8f0;
  --hover: #f0f9ff;
  font-family: 'Inter', sans-serif;
  min-height: 380px;
  background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
  display: flex;
  flex-direction: column;
  align-items: stretch;
}

.dd-07__wrapper {
  width: 100%;
  display: flex;
  justify-content: center;
  padding: 32px 20px 0;
}

.dd-07__nav {
  position: relative;
  display: flex;
  align-items: center;
  gap: 4px;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 14px;
  padding: 10px 10px 10px 20px;
  box-shadow: 0 2px 16px rgba(0,0,0,.06);
  width: 100%;
  max-width: 780px;
  z-index: 100;
}

.dd-07__brand {
  font-size: 18px;
  font-weight: 700;
  color: var(--brand);
  margin-right: 8px;
  letter-spacing: -0.5px;
}

.dd-07__items {
  display: flex;
  align-items: center;
  gap: 2px;
  flex: 1;
}

.dd-07__simple {
  padding: 8px 14px;
  color: var(--text);
  text-decoration: none;
  font-size: 14px;
  font-weight: 500;
  border-radius: 8px;
  transition: background 0.15s, color 0.15s;
}

.dd-07__simple:hover {
  background: var(--hover);
  color: var(--brand);
}

.dd-07__item {
  position: relative;
}
/* hover-bridge: invisible strip below the trigger covering the 12px gap. */

.dd-07__item::after {
  content: "";
  position: absolute;
  left: 0;
  right: 0;
  top: 100%;
  height: 12px;
}

.dd-07__trigger {
  display: block;
  padding: 8px 14px;
  color: var(--text);
  text-decoration: none;
  font-size: 14px;
  font-weight: 500;
  border-radius: 8px;
  transition: background 0.15s, color 0.15s;
  white-space: nowrap;
}

.dd-07__trigger:hover,
.dd-07__item:hover .dd-07__trigger {
  background: var(--hover);
  color: var(--brand);
}
/* mega panel */

.dd-07__mega {
  position: absolute;
  top: calc(100% + 12px);
  left: 50%;
  transform: translateX(-50%) translateY(-8px);
  width: 620px;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 16px;
  box-shadow: 0 20px 60px rgba(0,0,0,.12);
  padding: 24px;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1.4fr;
  gap: 24px;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.24s ease, transform 0.3s cubic-bezier(0.16,1,0.3,1);
}

.dd-07__mega::before {
  content: "";
  position: absolute;
  left: 0;
  right: 0;
  top: -12px;
  height: 12px;
  /* invisible hover-bridge — keeps :hover active while
       the cursor traverses the visible gap between trigger
       and panel. */
}

.dd-07__item:hover .dd-07__mega {
  opacity: 1;
  pointer-events: auto;
  transform: translateX(-50%) translateY(0);
}

.dd-07__heading {
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--muted);
  margin-bottom: 10px;
  padding-bottom: 8px;
  border-bottom: 1px solid var(--border);
}

.dd-07__col {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.dd-07__link {
  display: block;
  padding: 7px 8px;
  border-radius: 8px;
  text-decoration: none;
  color: var(--text);
  font-size: 13px;
  font-weight: 500;
  transition: background 0.15s, color 0.15s;
}

.dd-07__link:hover {
  background: var(--hover);
  color: var(--brand);
}

.dd-07__featured {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.dd-07__card {
  background: linear-gradient(135deg, #f0f9ff, #e0f2fe);
  border: 1px solid #bae6fd;
  border-radius: 12px;
  padding: 16px;
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.dd-07__new {
  display: inline-block;
  font-size: 9px;
  font-weight: 700;
  letter-spacing: 0.1em;
  color: var(--brand);
  background: #e0f2fe;
  padding: 2px 6px;
  border-radius: 4px;
  align-self: flex-start;
}

.dd-07__card-title {
  font-size: 14px;
  font-weight: 700;
  color: var(--text);
}

.dd-07__card-desc {
  font-size: 12px;
  color: var(--muted);
  line-height: 1.5;
}

.dd-07__card-link {
  font-size: 12px;
  font-weight: 600;
  color: var(--brand);
  text-decoration: none;
  margin-top: auto;
  transition: gap 0.15s;
}

.dd-07__cta {
  margin-left: auto;
  padding: 8px 18px;
  background: var(--brand);
  color: #fff;
  border-radius: 8px;
  text-decoration: none;
  font-size: 13.5px;
  font-weight: 600;
  white-space: nowrap;
  transition: opacity 0.15s;
}

.dd-07__cta:hover {
  opacity: 0.88;
}

@media (prefers-reduced-motion: reduce) {
  .dd-07__mega {
    transition: none;
  }
}
```
