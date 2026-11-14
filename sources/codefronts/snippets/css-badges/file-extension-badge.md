---
source: "codefronts"
url: "https://codefronts.com/snippets/css-badges/file-extension-badge/"
title: "File Extension Badge"
section: "snippets"
category: "css-badges"
category_name: "CSS Badges"
description: "Two adjacent flex blocks — colored extension + white filename."
has_js: "false"
---

Here's a working CSS Badge from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: File Extension Badge
Source: https://codefronts.com/snippets/css-badges/file-extension-badge/

Two adjacent flex blocks — colored extension + white filename. Color is the identifier; nothing else is needed. Hover lifts the whole card off the surface the way you pick up a real file.
## HTML
```html
<div class="bdg-17-stage">
  <div class="bdg-17-badge" style="--bdg-17-color:#e84040">
    <div class="bdg-17-ext">PDF</div>
    <div class="bdg-17-info">
      <div class="bdg-17-name">annual-report-2025.pdf</div>
      <div class="bdg-17-meta">2.4 MB · Updated Mar 14</div>
    </div>
  </div>
  <div class="bdg-17-badge" style="--bdg-17-color:#1e8f4a">
    <div class="bdg-17-ext">SVG</div>
    <div class="bdg-17-info">
      <div class="bdg-17-name">logo-lockup-final.svg</div>
      <div class="bdg-17-meta">18 KB · Vector · Scalable</div>
    </div>
  </div>
  <div class="bdg-17-badge" style="--bdg-17-color:#1d6abf">
    <div class="bdg-17-ext">MP3</div>
    <div class="bdg-17-info">
      <div class="bdg-17-name">episode-42-interview.mp3</div>
      <div class="bdg-17-meta">48 MB · 52 min 18 sec</div>
    </div>
  </div>
  <div class="bdg-17-badge" style="--bdg-17-color:#6b3aa0">
    <div class="bdg-17-ext">ZIP</div>
    <div class="bdg-17-info">
      <div class="bdg-17-name">source-assets-v3.zip</div>
      <div class="bdg-17-meta">340 MB · 1,284 files</div>
    </div>
  </div>
  <div class="bdg-17-badge" style="--bdg-17-color:#c87820">
    <div class="bdg-17-ext">CSV</div>
    <div class="bdg-17-info">
      <div class="bdg-17-name">q1-export-raw.csv</div>
      <div class="bdg-17-meta">6.1 MB · 88,412 rows</div>
    </div>
  </div>
</div>
```
## CSS
```css
.bdg-17-stage {
  background: #f0f2f5;
  padding: 50px 40px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  align-items: flex-start;
  width: 100%;
  min-height: 100vh;
  align-items: center;
  justify-content: center;
}

.bdg-17-badge {
  display: inline-flex;
  align-items: stretch;
  overflow: hidden;
  border-radius: 4px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.1);
  cursor: default;
  transition: transform 0.2s, box-shadow 0.2s;
  text-decoration: none;
}

.bdg-17-badge:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(0,0,0,0.14);
}

@media (prefers-reduced-motion: reduce) {
  .bdg-17-badge {
    transition: none;
  }
}

.bdg-17-ext {
  padding: 10px 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  min-width: 56px;
  background: var(--bdg-17-color, #555);
  font-family: ui-monospace, "JetBrains Mono", monospace;
  font-size: 13px;
  font-weight: 700;
  color: #fff;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  flex-shrink: 0;
}

.bdg-17-info {
  padding: 10px 16px;
  background: #fff;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 2px;
}

.bdg-17-name {
  font-family: ui-monospace, "JetBrains Mono", monospace;
  font-size: 13px;
  font-weight: 500;
  color: #1a1612;
  letter-spacing: -0.01em;
  line-height: 1;
}

.bdg-17-meta {
  font-family: system-ui, "Bricolage Grotesque", sans-serif;
  font-size: 10px;
  letter-spacing: 0.12em;
  color: #888;
  text-transform: uppercase;
  line-height: 1;
}
```
