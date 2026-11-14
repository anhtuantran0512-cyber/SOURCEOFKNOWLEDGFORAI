---
source: "codefronts"
url: "https://codefronts.com/snippets/css-badges/schema-markup-type/"
title: "Schema Markup Type"
section: "snippets"
category: "css-badges"
category_name: "CSS Badges"
description: "Structured data is a contract between a page and Google's parser."
has_js: "false"
---

Here's a working CSS Badge from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Schema Markup Type
Source: https://codefronts.com/snippets/css-badges/schema-markup-type/

Structured data is a contract between a page and Google's parser. The badge names the @type and lists which SERP features it unlocks — the difference between a plain blue link and a result with stars, FAQs, and how-to steps.
## HTML
```html
<div class="bdg-10-stage">
  <div class="bdg-10-card">
    <div class="bdg-10-header">
      <div class="bdg-10-at">@type</div>
      <div class="bdg-10-type-name">Article</div>
      <div class="bdg-10-valid-tag">✓ Valid JSON-LD</div>
    </div>
    <div class="bdg-10-body">
      <div class="bdg-10-section-label">Unlocks SERP Features</div>
      <div class="bdg-10-chips">
        <div class="bdg-10-chip bdg-10-chip-rich">⬡ Rich Result</div>
        <div class="bdg-10-chip bdg-10-chip-snippet">★ Featured Snippet</div>
        <div class="bdg-10-chip bdg-10-chip-author">⌖ Author Markup</div>
        <div class="bdg-10-chip bdg-10-chip-date">⌚ DatePublished</div>
      </div>
      <div class="bdg-10-section-label">Implementation Preview</div>
      <div class="bdg-10-code-peek">
        <span class="bdg-10-s-gray">&lt;script type="application/ld+json"&gt;</span><br>
        &nbsp;&nbsp;<span class="bdg-10-s-gray">{</span> <span class="bdg-10-s-key">"@context"</span><span class="bdg-10-s-gray">:</span> <span class="bdg-10-s-string">"https://schema.org"</span><span class="bdg-10-s-gray">,</span><br>
        &nbsp;&nbsp;&nbsp;&nbsp;<span class="bdg-10-s-key">"@type"</span><span class="bdg-10-s-gray">:</span> <span class="bdg-10-s-string">"Article"</span><span class="bdg-10-s-gray">,</span><br>
        &nbsp;&nbsp;&nbsp;&nbsp;<span class="bdg-10-s-prop">"headline"</span><span class="bdg-10-s-gray">:</span> <span class="bdg-10-s-string">"…"</span><span class="bdg-10-s-gray">,</span><br>
        &nbsp;&nbsp;&nbsp;&nbsp;<span class="bdg-10-s-prop">"author"</span><span class="bdg-10-s-gray">:</span> <span class="bdg-10-s-gray">{ … }</span> <span class="bdg-10-s-gray">}</span><br>
        <span class="bdg-10-s-gray">&lt;/script&gt;</span>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.bdg-10-stage {
  background: #f6f8fa;
  padding: 50px 40px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
  min-height: 100vh;
}

.bdg-10-card {
  background: #fff;
  border: 1px solid #e0e6ed;
  border-radius: 6px;
  width: 100%;
  max-width: 480px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}

.bdg-10-header {
  background: #f6f8fa;
  border-bottom: 1px solid #e0e6ed;
  padding: 16px 20px;
  display: flex;
  align-items: center;
  gap: 12px;
}

.bdg-10-at {
  font-family: ui-monospace, "JetBrains Mono", monospace;
  font-size: 10px;
  letter-spacing: 0.14em;
  color: #888;
  text-transform: uppercase;
}

.bdg-10-type-name {
  font-family: ui-monospace, "JetBrains Mono", monospace;
  font-size: 18px;
  font-weight: 700;
  color: #1a1612;
  letter-spacing: -0.01em;
}

.bdg-10-valid-tag {
  margin-left: auto;
  display: flex;
  align-items: center;
  gap: 5px;
  font-family: system-ui, "Bricolage Grotesque", sans-serif;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.1em;
  color: #1d8f4a;
  padding: 4px 10px;
  border: 1.5px solid rgba(29, 143, 74, 0.4);
  border-radius: 3px;
}

.bdg-10-body {
  padding: 18px 20px;
}

.bdg-10-section-label {
  font-family: system-ui, "Bricolage Grotesque", sans-serif;
  font-size: 9px;
  letter-spacing: 0.28em;
  text-transform: uppercase;
  color: #aaa;
  margin-bottom: 10px;
}

.bdg-10-chips {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-bottom: 20px;
}

.bdg-10-chip {
  display: flex;
  align-items: center;
  gap: 5px;
  padding: 5px 10px;
  border-radius: 3px;
  font-family: system-ui, "Bricolage Grotesque", sans-serif;
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.04em;
  border: 1px solid;
}

.bdg-10-chip-rich {
  color: #4285f4;
  background: #e8f0fe;
  border-color: #c5d8fd;
}

.bdg-10-chip-snippet {
  color: #1d8f4a;
  background: #e6f4ea;
  border-color: #b7e0c2;
}

.bdg-10-chip-author {
  color: #7c4dff;
  background: #f3e8ff;
  border-color: #d9b8ff;
}

.bdg-10-chip-date {
  color: #b8762d;
  background: #fef3e2;
  border-color: #fdd9a0;
}

.bdg-10-code-peek {
  background: #f6f8fa;
  border: 1px solid #e0e6ed;
  border-radius: 4px;
  padding: 10px 14px;
  font-family: ui-monospace, "JetBrains Mono", monospace;
  font-size: 11.5px;
  line-height: 1.7;
  overflow: hidden;
}

.bdg-10-s-key {
  color: #032f62;
}

.bdg-10-s-string {
  color: #0d6416;
}

.bdg-10-s-gray {
  color: #888;
}

.bdg-10-s-prop {
  color: #5a3d99;
}
```
