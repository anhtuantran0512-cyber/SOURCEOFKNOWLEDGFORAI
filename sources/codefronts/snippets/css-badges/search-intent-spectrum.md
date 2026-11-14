---
source: "codefronts"
url: "https://codefronts.com/snippets/css-badges/search-intent-spectrum/"
title: "Search Intent Spectrum"
section: "snippets"
category: "css-badges"
category_name: "CSS Badges"
description: "Plots a keyword on the Informational / Navigational / Commercial / Transactional spectrum."
has_js: "false"
---

Here's a working CSS Badge from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Search Intent Spectrum
Source: https://codefronts.com/snippets/css-badges/search-intent-spectrum/

Plots a keyword on the Informational / Navigational / Commercial / Transactional spectrum. Intent mismatch is one of the top reasons pages don't rank — this badge surfaces the right page type before a word is written.
## HTML
```html
<div class="bdg-11-stage">
  <div class="bdg-11-card">
    <div class="bdg-11-query-label">Keyword</div>
    <div class="bdg-11-query-text">"best seo tools 2026"</div>

    <div class="bdg-11-spectrum-wrap">
      <div class="bdg-11-spectrum">
        <div class="bdg-11-zone bdg-11-i">I</div>
        <div class="bdg-11-zone bdg-11-n">N</div>
        <div class="bdg-11-zone bdg-11-c">C</div>
        <div class="bdg-11-zone bdg-11-t">T</div>
      </div>
      <div class="bdg-11-marker"></div>
    </div>
    <div class="bdg-11-zone-labels">
      <span>Informational</span>
      <span>Navigational</span>
      <span>Commercial</span>
      <span>Transactional</span>
    </div>

    <div class="bdg-11-result-row">
      <div class="bdg-11-type-pill">Commercial</div>
      <div class="bdg-11-page-rec">
        <strong>Comparison / Listicle</strong>
        Best-of, tools roundup, pricing page
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.bdg-11-stage {
  background: #f0f4fb;
  padding: 50px 40px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
  min-height: 100vh;
}

.bdg-11-card {
  background: #fff;
  border: 1px solid #dde3ef;
  border-radius: 6px;
  padding: 28px 28px 24px;
  width: 100%;
  max-width: 480px;
  box-shadow: 0 2px 12px rgba(0,0,0,0.06);
}

.bdg-11-query-label {
  font-family: system-ui, "Bricolage Grotesque", sans-serif;
  font-size: 9px;
  letter-spacing: 0.25em;
  text-transform: uppercase;
  color: #888;
  margin-bottom: 6px;
}

.bdg-11-query-text {
  font-family: ui-monospace, "JetBrains Mono", monospace;
  font-size: 16px;
  color: #1a1612;
  margin-bottom: 22px;
  padding: 8px 12px;
  background: #f6f8fc;
  border-radius: 4px;
  border-left: 3px solid #4285f4;
}

.bdg-11-spectrum-wrap {
  position: relative;
  margin-bottom: 8px;
}

.bdg-11-spectrum {
  display: flex;
  height: 44px;
  border-radius: 4px;
  overflow: visible;
  position: relative;
}

.bdg-11-zone {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: ui-monospace, "JetBrains Mono", monospace;
  font-size: 11px;
  font-weight: 700;
  color: rgba(255,255,255,0.85);
  letter-spacing: 0.06em;
}

.bdg-11-zone:first-child {
  border-radius: 4px 0 0 4px;
}

.bdg-11-zone:last-child {
  border-radius: 0 4px 4px 0;
}

.bdg-11-i {
  background: #4285f4;
}

.bdg-11-n {
  background: #0f9d58;
}

.bdg-11-c {
  background: #f4b400;
  color: rgba(0,0,0,0.6);
}

.bdg-11-t {
  background: #db4437;
}

.bdg-11-marker {
  position: absolute;
  top: -6px;
  bottom: -6px;
  width: 4px;
  background: #1a1612;
  border-radius: 2px;
  transform: translateX(-50%);
  box-shadow: 0 0 0 2px #fff, 0 0 0 3.5px #1a1612;
  animation: bdg-11-slide 0.8s cubic-bezier(0.4, 0, 0.2, 1) 0.4s forwards;
  left: 0%;
}

@keyframes bdg-11-slide {
  to {
    left: 68%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .bdg-11-marker {
    animation: none;
    left: 68%;
  }
}

.bdg-11-zone-labels {
  display: flex;
  margin-top: 6px;
  margin-bottom: 20px;
}

.bdg-11-zone-labels span {
  flex: 1;
  text-align: center;
  font-family: system-ui, "Bricolage Grotesque", sans-serif;
  font-size: 9px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #aaa;
}

.bdg-11-result-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-top: 18px;
  border-top: 1px solid #eee;
}

.bdg-11-type-pill {
  padding: 6px 14px;
  border-radius: 20px;
  background: rgba(244, 180, 0, 0.15);
  border: 1px solid rgba(244, 180, 0, 0.4);
  font-family: system-ui, "Bricolage Grotesque", sans-serif;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.06em;
  color: #c48a00;
}

.bdg-11-page-rec {
  font-family: system-ui, "Bricolage Grotesque", sans-serif;
  font-size: 11px;
  color: #888;
  text-align: right;
  line-height: 1.5;
  letter-spacing: 0.04em;
}

.bdg-11-page-rec strong {
  color: #1a1612;
  display: block;
}
```
