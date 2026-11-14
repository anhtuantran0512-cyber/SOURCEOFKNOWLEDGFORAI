---
source: "codefronts"
url: "https://codefronts.com/snippets/css-badges/signal-bars/"
title: "Signal Bars"
section: "snippets"
category: "css-badges"
category_name: "CSS Badges"
description: "Four rectangles of increasing height — possibly the most iconic data visualization ever designed."
has_js: "false"
---

Here's a working CSS Badge from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Signal Bars
Source: https://codefronts.com/snippets/css-badges/signal-bars/

Four rectangles of increasing height — possibly the most iconic data visualization ever designed. Confidence, signal, relevance — whatever the product needs. Hover fills all bars to maximum.
## HTML
```html
<div class="bdg-19-stage">
  <div class="bdg-19-badge">
    <div class="bdg-19-bars-group">
      <div class="bdg-19-bar bdg-19-active"></div>
      <div class="bdg-19-bar bdg-19-active"></div>
      <div class="bdg-19-bar bdg-19-active"></div>
      <div class="bdg-19-bar bdg-19-active"></div>
    </div>
    <div class="bdg-19-info">
      <div class="bdg-19-strength">Excellent</div>
      <div class="bdg-19-label">Confidence · 4 / 4</div>
    </div>
  </div>

  <div class="bdg-19-mini-set">
    <div class="bdg-19-row-mini">
      <div class="bdg-19-bars-mini">
        <div class="bdg-19-bar bdg-19-active"></div>
        <div class="bdg-19-bar bdg-19-active"></div>
        <div class="bdg-19-bar bdg-19-active"></div>
        <div class="bdg-19-bar bdg-19-inactive"></div>
      </div>
      <div class="bdg-19-name-mini">Good · 3/4</div>
    </div>
    <div class="bdg-19-row-mini">
      <div class="bdg-19-bars-mini">
        <div class="bdg-19-bar bdg-19-active"></div>
        <div class="bdg-19-bar bdg-19-active"></div>
        <div class="bdg-19-bar bdg-19-inactive"></div>
        <div class="bdg-19-bar bdg-19-inactive"></div>
      </div>
      <div class="bdg-19-name-mini">Fair · 2/4</div>
    </div>
    <div class="bdg-19-row-mini">
      <div class="bdg-19-bars-mini">
        <div class="bdg-19-bar bdg-19-active"></div>
        <div class="bdg-19-bar bdg-19-inactive"></div>
        <div class="bdg-19-bar bdg-19-inactive"></div>
        <div class="bdg-19-bar bdg-19-inactive"></div>
      </div>
      <div class="bdg-19-name-mini">Weak · 1/4</div>
    </div>
  </div>
</div>
```
## CSS
```css
.bdg-19-stage {
  background: #f5f4f2;
  padding: 60px 48px;
  display: flex;
  flex-direction: column;
  gap: 36px;
  align-items: flex-start;
  width: 100%;
  min-height: 100vh;
  align-items: center;
  justify-content: center;
}

.bdg-19-badge {
  display: inline-flex;
  align-items: flex-end;
  gap: 4px;
  padding: 16px 20px 14px;
  background: white;
  border: 1px solid #e0ddd8;
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
  cursor: pointer;
  position: relative;
}

.bdg-19-badge:hover .bdg-19-bar {
  background: #1a1612 !important;
}

.bdg-19-bars-group {
  display: flex;
  align-items: flex-end;
  gap: 4px;
  margin-right: 14px;
}

.bdg-19-bar {
  width: 8px;
  border-radius: 1px;
  transition: background 0.2s, height 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.bdg-19-bars-group .bdg-19-bar:nth-child(1) {
  height: 10px;
}

.bdg-19-bars-group .bdg-19-bar:nth-child(2) {
  height: 18px;
}

.bdg-19-bars-group .bdg-19-bar:nth-child(3) {
  height: 26px;
}

.bdg-19-bars-group .bdg-19-bar:nth-child(4) {
  height: 34px;
}

.bdg-19-active {
  background: #1a1612;
}

.bdg-19-inactive {
  background: #dddbd6;
}

.bdg-19-info {
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  gap: 2px;
}

.bdg-19-strength {
  font-family: Georgia, "Fraunces", serif;
  font-size: 20px;
  font-weight: 500;
  line-height: 1;
  letter-spacing: -0.01em;
  color: #1a1612;
}

.bdg-19-label {
  font-family: system-ui, "Bricolage Grotesque", sans-serif;
  font-size: 10px;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: #4a4239;
}

.bdg-19-mini-set {
  display: flex;
  flex-direction: column;
  gap: 12px;
  padding: 0 4px;
}

.bdg-19-row-mini {
  display: flex;
  align-items: center;
  gap: 12px;
}

.bdg-19-bars-mini {
  display: flex;
  align-items: flex-end;
  gap: 2px;
}

.bdg-19-bars-mini .bdg-19-bar {
  width: 5px;
}

.bdg-19-bars-mini .bdg-19-bar:nth-child(1) {
  height: 6px;
}

.bdg-19-bars-mini .bdg-19-bar:nth-child(2) {
  height: 10px;
}

.bdg-19-bars-mini .bdg-19-bar:nth-child(3) {
  height: 14px;
}

.bdg-19-bars-mini .bdg-19-bar:nth-child(4) {
  height: 18px;
}

.bdg-19-name-mini {
  font-family: system-ui, "Bricolage Grotesque", sans-serif;
  font-size: 11px;
  letter-spacing: 0.1em;
  color: #4a4239;
  text-transform: uppercase;
}

@media (prefers-reduced-motion: reduce) {
  .bdg-19-bar {
    transition: none;
  }
}
```
