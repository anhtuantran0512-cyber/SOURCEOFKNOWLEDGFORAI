---
source: "codefronts"
url: "https://codefronts.com/snippets/css-badges/crawl-index-status/"
title: "Crawl & Index Status"
section: "snippets"
category: "css-badges"
category_name: "CSS Badges"
description: "Googlebot visits and decides: indexed or not."
has_js: "false"
---

Here's a working CSS Badge from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Crawl & Index Status
Source: https://codefronts.com/snippets/css-badges/crawl-index-status/

Googlebot visits and decides: indexed or not. But there are four states before "indexed," and most pages fail before the first one. This badge shows exactly where in the crawl pipeline a URL sits.
## HTML
```html
<div class="bdg-09-stage">
  <div class="bdg-09-card">
    <div class="bdg-09-status-row">
      <div class="bdg-09-dot bdg-09-dot-indexed"></div>
      <div class="bdg-09-status-text">INDEXED</div>
      <div class="bdg-09-timestamp">Last crawled: 3h ago</div>
    </div>
    <div class="bdg-09-url">/blog/technical-seo-guide-2026/</div>
    <div class="bdg-09-meta-row">
      <span class="bdg-09-meta-tag">Googlebot 2.1</span>
      <span class="bdg-09-sep">·</span>
      <span class="bdg-09-meta-tag">JS Rendered</span>
      <span class="bdg-09-sep">·</span>
      <span class="bdg-09-meta-tag">200 OK</span>
      <span class="bdg-09-sep">·</span>
      <span class="bdg-09-meta-tag">canonical: self</span>
    </div>
    <div class="bdg-09-pipeline">
      <div class="bdg-09-step bdg-09-step-done">Discovered</div>
      <div class="bdg-09-arrow">»</div>
      <div class="bdg-09-step bdg-09-step-done">Crawled</div>
      <div class="bdg-09-arrow">»</div>
      <div class="bdg-09-step bdg-09-step-done">Rendered</div>
      <div class="bdg-09-arrow">»</div>
      <div class="bdg-09-step bdg-09-step-active">Indexed</div>
    </div>
  </div>
</div>
```
## CSS
```css
.bdg-09-stage {
  background: #0a0e18;
  padding: 50px 36px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
  min-height: 100vh;
}

.bdg-09-card {
  background: #111620;
  border: 1px solid #1e2638;
  border-radius: 6px;
  padding: 24px 24px 20px;
  width: 100%;
  max-width: 480px;
  font-family: ui-monospace, "JetBrains Mono", monospace;
}

.bdg-09-status-row {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 14px;
}

.bdg-09-dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  flex-shrink: 0;
}

.bdg-09-dot-indexed {
  background: #0cce6b;
  box-shadow: 0 0 8px #0cce6b;
  animation: bdg-09-pulse 2s infinite;
}

@keyframes bdg-09-pulse {
  0%,
    100% {
    box-shadow: 0 0 6px #0cce6b;
  }

  50% {
    box-shadow: 0 0 14px #0cce6b;
  }
}

@media (prefers-reduced-motion: reduce) {
  .bdg-09-dot-indexed {
    animation: none;
  }
}

.bdg-09-status-text {
  font-size: 20px;
  font-weight: 800;
  letter-spacing: 0.12em;
  color: #0cce6b;
}

.bdg-09-timestamp {
  margin-left: auto;
  font-size: 10px;
  color: #8b949e;
  letter-spacing: 0.06em;
}

.bdg-09-url {
  font-size: 12px;
  color: #4a90d9;
  letter-spacing: 0;
  margin-bottom: 12px;
  padding: 8px 12px;
  background: rgba(66, 133, 244, 0.06);
  border-left: 2px solid rgba(66, 133, 244, 0.3);
  border-radius: 0 3px 3px 0;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.bdg-09-meta-row {
  display: flex;
  gap: 8px;
  align-items: center;
  font-size: 10px;
  color: #8b949e;
  letter-spacing: 0.06em;
  margin-bottom: 20px;
}

.bdg-09-sep {
  color: #30363d;
}

.bdg-09-meta-tag {
  padding: 2px 7px;
  border-radius: 3px;
  background: rgba(139, 148, 158, 0.1);
  border: 1px solid #30363d;
  font-size: 9px;
  letter-spacing: 0.1em;
}

.bdg-09-pipeline {
  display: flex;
  align-items: center;
  gap: 4px;
  padding-top: 16px;
  border-top: 1px solid #1e2638;
}

.bdg-09-step {
  flex: 1;
  text-align: center;
  font-size: 8.5px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  padding: 5px 4px;
  border-radius: 3px;
  border: 1px solid #1e2638;
  color: #8b949e;
}

.bdg-09-step-done {
  color: #0cce6b;
  border-color: rgba(12,206,107,0.3);
  background: rgba(12,206,107,0.06);
}

.bdg-09-step-active {
  color: #fff;
  border-color: rgba(12,206,107,0.6);
  background: rgba(12,206,107,0.15);
  font-weight: 700;
}

.bdg-09-arrow {
  font-size: 10px;
  color: #30363d;
  flex-shrink: 0;
}
```
