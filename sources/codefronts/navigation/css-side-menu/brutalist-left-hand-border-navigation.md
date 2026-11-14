---
source: "codefronts"
url: "https://codefronts.com/navigation/css-side-menu/brutalist-left-hand-border-navigation/"
title: "Brutalist Left-Hand Border Navigation"
section: "navigation"
category: "css-side-menu"
category_name: "CSS Side Menus"
description: "A high-contrast brutalist sidebar using only thick black borders, a bold red accent rule, raw condensed typography, and zero gradients or rounded corners."
has_js: "false"
---

Here's a working CSS Side Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Brutalist Left-Hand Border Navigation
Source: https://codefronts.com/navigation/css-side-menu/brutalist-left-hand-border-navigation/

A high-contrast brutalist sidebar using only thick black borders, a bold red accent rule, raw condensed typography, and zero gradients or rounded corners.
## HTML
```html
<div class="sm-12">
  <nav class="sm-12__nav">
    <div class="sm-12__brand">
      <div class="sm-12__brand-eyebrow">EST. 2024</div>
      <div class="sm-12__brand-name">Brutal</div>
      <div class="sm-12__brand-tag">Studio</div>
    </div>
    <div class="sm-12__links">
      <a class="sm-12__link sm-12__link--active" href="#">Home</a>
      <a class="sm-12__link" href="#">Work <span class="sm-12__count">12</span></a>
      <a class="sm-12__link" href="#">Studio</a>
      <a class="sm-12__link" href="#">Journal <span class="sm-12__count">05</span></a>
      <a class="sm-12__link" href="#">Contact</a>
    </div>
    <div class="sm-12__footer">
      <div class="sm-12__footer-label">// USER</div>
      <div class="sm-12__footer-user">J. Haas</div>
    </div>
  </nav>
  <div class="sm-12__main">
    <div class="sm-12__topbar">
      <span class="sm-12__topbar-num">[01]</span>
      <div class="sm-12__page-title">Homepage</div>
    </div>
    <div class="sm-12__content">
      <p class="sm-12__intro">Brutalist sidebar using raw black borders, zero gradients, high-contrast type, and a thick red rule as the only decorative element.</p>
      <div class="sm-12__grid">
        <div class="sm-12__cell"><div class="sm-12__cell-val">24</div><div class="sm-12__cell-lbl">Projects</div></div>
        <div class="sm-12__cell"><div class="sm-12__cell-val">08</div><div class="sm-12__cell-lbl">Clients</div></div>
        <div class="sm-12__cell"><div class="sm-12__cell-val">6yr</div><div class="sm-12__cell-lbl">Experience</div></div>
        <div class="sm-12__cell"><div class="sm-12__cell-val">100%</div><div class="sm-12__cell-lbl">Remote</div></div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.sm-12,
.sm-12 *,
.sm-12 *::before,
.sm-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sm-12 ::selection {
  background: #000;
  color: #fff;
}

.sm-12 {
  --bg: #f5f0e8;
  --text: #0a0a0a;
  --accent: #e63329;
  --yellow: #f7e733;
  --nav-bg: #0a0a0a;
  --nav-text: #f5f0e8;
  --font-head: 'Barlow Condensed', system-ui, sans-serif;
  --font-mono: 'Space Mono', monospace;
  font-family: var(--font-head);
  background: var(--bg);
  color: var(--text);
  display: flex;
  min-height: 100vh;
  border-radius: 0;
  overflow: hidden;
  border: 3px solid var(--text);
  border-radius: 2px;
}

.sm-12__nav {
  width: 200px;
  background: var(--nav-bg);
  color: var(--nav-text);
  border-right: 4px solid var(--accent);
  display: flex;
  flex-direction: column;
  flex-shrink: 0;
}

.sm-12__brand {
  padding: 18px 16px;
  border-bottom: 3px solid var(--accent);
}

.sm-12__brand-eyebrow {
  font-family: var(--font-mono);
  font-size: 8px;
  letter-spacing: 0.2em;
  color: #666;
  margin-bottom: 4px;
}

.sm-12__brand-name {
  font-size: 26px;
  font-weight: 900;
  letter-spacing: -0.02em;
  line-height: 1;
  text-transform: uppercase;
  color: var(--nav-text);
}

.sm-12__brand-tag {
  display: inline-block;
  background: var(--accent);
  color: #fff;
  font-size: 10px;
  font-weight: 800;
  letter-spacing: 0.1em;
  padding: 1px 6px;
  margin-top: 6px;
  text-transform: uppercase;
}

.sm-12__links {
  flex: 1;
}

.sm-12__link {
  display: block;
  padding: 13px 16px;
  color: #666;
  font-size: 18px;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  cursor: pointer;
  text-decoration: none;
  border-bottom: 1px solid #1a1a1a;
  transition: color 0.1s, background 0.1s;
  position: relative;
}

.sm-12__link::before {
  content: '//';
  color: #333;
  margin-right: 8px;
  font-family: var(--font-mono);
  font-size: 12px;
}

.sm-12__link:hover {
  color: var(--yellow);
  background: #111;
}

.sm-12__link--active {
  color: var(--nav-text);
  background: var(--accent);
  border-bottom-color: var(--accent);
}

.sm-12__link--active::before {
  color: rgba(255,255,255,0.5);
}

.sm-12__link--active::after {
  content: '→';
  position: absolute;
  right: 12px;
  top: 50%;
  transform: translateY(-50%);
  font-size: 16px;
  font-family: var(--font-mono);
}

.sm-12__count {
  position: absolute;
  right: 32px;
  top: 50%;
  transform: translateY(-50%);
  font-family: var(--font-mono);
  font-size: 10px;
  color: var(--yellow);
}

.sm-12__link--active .sm-12__count {
  color: rgba(255,255,255,0.7);
  right: 36px;
}

.sm-12__footer {
  border-top: 3px solid var(--accent);
  padding: 12px 16px;
}

.sm-12__footer-label {
  font-family: var(--font-mono);
  font-size: 8px;
  color: #444;
  margin-bottom: 4px;
  letter-spacing: 0.15em;
}

.sm-12__footer-user {
  font-size: 14px;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
/* Main */

.sm-12__main {
  flex: 1;
  border-left: none;
}

.sm-12__topbar {
  padding: 16px 22px;
  border-bottom: 3px solid var(--text);
  display: flex;
  align-items: baseline;
  gap: 12px;
}

.sm-12__topbar-num {
  font-family: var(--font-mono);
  font-size: 11px;
  color: var(--accent);
}

.sm-12__page-title {
  font-size: 28px;
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: -0.01em;
  line-height: 1;
}

.sm-12__content {
  padding: 22px;
}

.sm-12__intro {
  font-size: 15px;
  line-height: 1.6;
  color: #444;
  margin-bottom: 22px;
  font-weight: 600;
  max-width: 380px;
}

.sm-12__grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0;
  border: 3px solid var(--text);
}

.sm-12__cell {
  padding: 14px;
  border-right: 2px solid var(--text);
  border-bottom: 2px solid var(--text);
}

.sm-12__cell:nth-child(even) {
  border-right: none;
}

.sm-12__cell:nth-child(n+3) {
  border-bottom: none;
}

.sm-12__cell-val {
  font-size: 28px;
  font-weight: 900;
  letter-spacing: -0.03em;
  line-height: 1;
  color: var(--text);
}

.sm-12__cell-lbl {
  font-family: var(--font-mono);
  font-size: 10px;
  color: #888;
  margin-top: 4px;
  text-transform: uppercase;
  letter-spacing: 0.1em;
}

@media (prefers-reduced-motion: reduce) {
  .sm-12__link {
    transition: none;
  }
}
```
