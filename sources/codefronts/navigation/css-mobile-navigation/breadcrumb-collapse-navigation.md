---
source: "codefronts"
url: "https://codefronts.com/navigation/css-mobile-navigation/breadcrumb-collapse-navigation/"
title: "Breadcrumb Collapse Navigation"
section: "navigation"
category: "css-mobile-navigation"
category_name: "CSS Mobile Navigation Patterns"
description: "A file explorer UI with a collapsed breadcrumb showing an ellipsis button that reveals the full ancestor path as a dropdown."
has_js: "false"
---

Here's a working CSS Mobile Navigation Pattern from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Breadcrumb Collapse Navigation
Source: https://codefronts.com/navigation/css-mobile-navigation/breadcrumb-collapse-navigation/

A file explorer UI with a collapsed breadcrumb showing an ellipsis button that reveals the full ancestor path as a dropdown. The dropdown toggles via Pure CSS checkbox with a scale-and-opacity entrance.
## HTML
```html
<div class="mn-13">
  <input type="checkbox" id="mn-13-collapse">
  <div class="mn-13__appbar">
    <div class="mn-13__appbar-row">
      <div class="mn-13__back">‹</div>
      <span class="mn-13__appbar-title">Documents</span>
      <div class="mn-13__appbar-actions">
        <div class="mn-13__icon-btn">🔍</div>
        <div class="mn-13__icon-btn">⋯</div>
      </div>
    </div>
    <!-- Collapsed breadcrumb with ellipsis -->
    <div class="mn-13__breadcrumb">
      <div class="mn-13__bc-item"><a href="#">Home</a></div>
      <span class="mn-13__bc-sep">›</span>
      <div class="mn-13__bc-ellipsis">
        <label for="mn-13-collapse" class="mn-13__ellipsis-btn">···</label>
        <div class="mn-13__bc-dropdown">
          <a href="#"><span>☁️</span> My Drive</a>
          <a href="#"><span>📁</span> Work Projects</a>
          <a href="#"><span>📁</span> 2024</a>
          <a href="#"><span>📁</span> Q4 Reports</a>
        </div>
      </div>
      <span class="mn-13__bc-sep">›</span>
      <div class="mn-13__bc-item is-current">Documents</div>
    </div>
  </div>

  <div class="mn-13__content">
    <div class="mn-13__section-header">Folders <span>+ New</span></div>
    <div class="mn-13__folder-item">
      <span class="mn-13__folder-icon">📁</span>
      <span class="mn-13__folder-name">Design Assets</span>
      <span class="mn-13__folder-count">48 items</span>
      <span class="mn-13__chevron">›</span>
    </div>
    <div class="mn-13__folder-item">
      <span class="mn-13__folder-icon">📁</span>
      <span class="mn-13__folder-name">Client Reports</span>
      <span class="mn-13__folder-count">12 items</span>
      <span class="mn-13__chevron">›</span>
    </div>
    <div class="mn-13__folder-item">
      <span class="mn-13__folder-icon">📁</span>
      <span class="mn-13__folder-name">Contracts</span>
      <span class="mn-13__folder-count">7 items</span>
      <span class="mn-13__chevron">›</span>
    </div>

    <div class="mn-13__section-header">Recent Files</div>
    <div class="mn-13__file-item">
      <div class="mn-13__file-icon" style="background:#eff6ff">📄</div>
      <div class="mn-13__file-info">
        <h4>Q4 Summary Report.pdf</h4>
        <p>PDF · 2.4 MB</p>
      </div>
      <div class="mn-13__file-meta"><p>Today</p><p>14:32</p></div>
    </div>
    <div class="mn-13__file-item">
      <div class="mn-13__file-icon" style="background:#f0fdf4">📊</div>
      <div class="mn-13__file-info">
        <h4>Analytics Dashboard.xlsx</h4>
        <p>Excel · 840 KB</p>
      </div>
      <div class="mn-13__file-meta"><p>Yesterday</p><p>09:15</p></div>
    </div>
    <div class="mn-13__file-item">
      <div class="mn-13__file-icon" style="background:#fef3c7">🖼️</div>
      <div class="mn-13__file-info">
        <h4>Brand Guidelines.fig</h4>
        <p>Figma · 18 MB</p>
      </div>
      <div class="mn-13__file-meta"><p>Dec 3</p><p>11:00</p></div>
    </div>
  </div>

  <div class="mn-13__upload">
    <div class="mn-13__upload-icon">☁️</div>
    <div class="mn-13__upload-text">
      <h4>24.8 GB of 50 GB used</h4>
      <p>Upgrade for more storage</p>
    </div>
    <div class="mn-13__upload-btn">Upgrade</div>
  </div>
</div>
```
## CSS
```css
*,
*::before,
*::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background: #0f0f13;
  font-family: 'Segoe UI', sans-serif;
}

.mn-13 {
  --bg: #fafafa;
  --surface: #ffffff;
  --border: #e4e4e7;
  --accent: #2563eb;
  --accent-hover: #1d4ed8;
  --text: #18181b;
  --muted: #71717a;
  --success: #16a34a;
  width: 375px;
  height: 667px;
  position: relative;
  overflow: hidden;
  background: var(--bg);
  border-radius: 32px;
  box-shadow: 0 30px 80px rgba(0,0,0,0.5);
  display: flex;
  flex-direction: column;
}

.mn-13 #mn-13-collapse {
  display: none;
}
/* Top app bar */

.mn-13__appbar {
  background: var(--surface);
  border-bottom: 1px solid var(--border);
  padding: 14px 16px;
  flex-shrink: 0;
}

.mn-13__appbar-row {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 10px;
}

.mn-13__back {
  width: 32px;
  height: 32px;
  border-radius: 8px;
  background: var(--bg);
  border: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 14px;
  cursor: pointer;
  color: var(--text);
  flex-shrink: 0;
}

.mn-13__appbar-title {
  font-size: 16px;
  font-weight: 600;
  color: var(--text);
  flex: 1;
}

.mn-13__appbar-actions {
  display: flex;
  gap: 8px;
}

.mn-13__icon-btn {
  width: 32px;
  height: 32px;
  border-radius: 8px;
  background: var(--bg);
  border: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 14px;
  cursor: pointer;
}
/* Breadcrumb row */

.mn-13__breadcrumb {
  display: flex;
  align-items: center;
  gap: 0;
  overflow: hidden;
  height: 28px;
}

.mn-13__bc-item {
  display: flex;
  align-items: center;
  gap: 4px;
  font-size: 12px;
  font-weight: 500;
  color: var(--muted);
  white-space: nowrap;
  flex-shrink: 0;
}

.mn-13__bc-item a {
  color: var(--accent);
  text-decoration: none;
  padding: 2px 4px;
  border-radius: 4px;
  transition: background 0.15s;
}

.mn-13__bc-item a:hover {
  background: rgba(37,99,235,0.08);
}

.mn-13__bc-item.is-current {
  color: var(--text);
  font-weight: 600;
}

.mn-13__bc-sep {
  color: var(--border);
  margin: 0 2px;
  font-size: 14px;
}
/* Collapsed ellipsis */

.mn-13__bc-ellipsis {
  display: flex;
  align-items: center;
  gap: 4px;
  flex-shrink: 0;
}

.mn-13__ellipsis-btn {
  width: 28px;
  height: 20px;
  border-radius: 4px;
  background: var(--bg);
  border: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 11px;
  cursor: pointer;
  color: var(--muted);
  font-weight: 700;
  letter-spacing: 1px;
  transition: background 0.2s, border-color 0.2s;
}

.mn-13__ellipsis-btn:hover {
  background: var(--accent);
  color: #fff;
  border-color: var(--accent);
}
/* Dropdown from ellipsis */

.mn-13__bc-dropdown {
  position: absolute;
  top: 88px;
  left: 16px;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 10px;
  box-shadow: 0 8px 24px rgba(0,0,0,0.12);
  z-index: 20;
  min-width: 180px;
  opacity: 0;
  pointer-events: none;
  transform: translateY(-8px) scale(0.96);
  transform-origin: top left;
  transition: opacity 0.2s, transform 0.2s;
}

.mn-13 #mn-13-collapse:checked ~ .mn-13__appbar .mn-13__bc-dropdown {
  opacity: 1;
  pointer-events: all;
  transform: translateY(0) scale(1);
}

.mn-13__bc-dropdown a {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 14px;
  font-size: 13px;
  color: var(--text);
  text-decoration: none;
  border-bottom: 1px solid rgba(0,0,0,0.04);
  transition: background 0.15s;
}

.mn-13__bc-dropdown a:last-child {
  border-bottom: none;
}

.mn-13__bc-dropdown a:hover {
  background: var(--bg);
}

.mn-13__bc-dropdown a span {
  color: var(--muted);
  font-size: 14px;
}
/* Page content */

.mn-13__content {
  flex: 1;
  overflow-y: auto;
}
/* File/folder explorer */

.mn-13__section-header {
  padding: 16px 16px 8px;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 1px;
  text-transform: uppercase;
  color: var(--muted);
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.mn-13__section-header span {
  font-size: 12px;
  font-weight: 500;
  letter-spacing: 0;
  text-transform: none;
  color: var(--accent);
  cursor: pointer;
}

.mn-13__file-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 16px;
  border-bottom: 1px solid rgba(0,0,0,0.04);
  cursor: pointer;
  transition: background 0.15s;
}

.mn-13__file-item:hover {
  background: rgba(0,0,0,0.02);
}

.mn-13__file-icon {
  width: 36px;
  height: 36px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 18px;
  flex-shrink: 0;
}

.mn-13__file-info {
  flex: 1;
}

.mn-13__file-info h4 {
  font-size: 14px;
  font-weight: 500;
  color: var(--text);
}

.mn-13__file-info p {
  font-size: 11px;
  color: var(--muted);
  margin-top: 1px;
}

.mn-13__file-meta {
  font-size: 11px;
  color: var(--muted);
  text-align: right;
}

.mn-13__file-meta p:first-child {
  color: var(--text);
  font-weight: 500;
}
/* Folder items */

.mn-13__folder-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 16px;
  border-bottom: 1px solid rgba(0,0,0,0.04);
  cursor: pointer;
  transition: background 0.15s;
}

.mn-13__folder-item:hover {
  background: rgba(0,0,0,0.02);
}

.mn-13__folder-icon {
  font-size: 22px;
  flex-shrink: 0;
}

.mn-13__folder-name {
  font-size: 14px;
  font-weight: 500;
  color: var(--text);
  flex: 1;
}

.mn-13__folder-count {
  font-size: 12px;
  color: var(--muted);
}

.mn-13__chevron {
  font-size: 12px;
  color: var(--muted);
}
/* Upload bar */

.mn-13__upload {
  background: rgba(37,99,235,0.06);
  border-top: 1px solid rgba(37,99,235,0.15);
  padding: 12px 16px;
  display: flex;
  align-items: center;
  gap: 12px;
  flex-shrink: 0;
}

.mn-13__upload-icon {
  width: 36px;
  height: 36px;
  border-radius: 10px;
  background: var(--accent);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
  color: #fff;
}

.mn-13__upload-text {
  flex: 1;
}

.mn-13__upload-text h4 {
  font-size: 13px;
  font-weight: 600;
  color: var(--text);
}

.mn-13__upload-text p {
  font-size: 11px;
  color: var(--muted);
}

.mn-13__upload-btn {
  font-size: 12px;
  font-weight: 600;
  color: var(--accent);
  cursor: pointer;
  padding: 6px 12px;
  border-radius: 6px;
  border: 1px solid rgba(37,99,235,0.3);
}

@media (prefers-reduced-motion: reduce) {
  .mn-13__bc-dropdown {
    transition: none;
  }
}
```
