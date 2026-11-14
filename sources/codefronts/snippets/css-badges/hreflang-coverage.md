---
source: "codefronts"
url: "https://codefronts.com/snippets/css-badges/hreflang-coverage/"
title: "Hreflang Coverage"
section: "snippets"
category: "css-badges"
category_name: "CSS Badges"
description: "International SEO's most misunderstood tag."
has_js: "false"
---

Here's a working CSS Badge from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Hreflang Coverage
Source: https://codefronts.com/snippets/css-badges/hreflang-coverage/

International SEO's most misunderstood tag. Shows the target locale, alternate version count, and — crucially — flags missing reciprocal links. Hreflang must be bidirectional or the entire cluster invalidates.
## HTML
```html
<div class="bdg-07-stage">
  <div class="bdg-07-card">
    <div class="bdg-07-primary">
      <div class="bdg-07-flag">
        <span style="background:#002868; flex:0.4"></span>
        <span style="background:#bf0a30; flex:0.3"></span>
        <span style="background:#fff; flex:0.3"></span>
      </div>
      <div>
        <div class="bdg-07-code">en-US</div>
        <div class="bdg-07-name">English · United States</div>
      </div>
      <div class="bdg-07-alts-count">→ 14 alternates</div>
    </div>
    <div class="bdg-07-body">
      <div class="bdg-07-section-label">Declared Alternates</div>
      <div class="bdg-07-chips">
        <div class="bdg-07-chip bdg-07-xdefault">x-default</div>
        <div class="bdg-07-chip">en-GB</div>
        <div class="bdg-07-chip">en-AU</div>
        <div class="bdg-07-chip">fr-FR</div>
        <div class="bdg-07-chip">de-DE</div>
        <div class="bdg-07-chip">es-ES</div>
        <div class="bdg-07-chip">es-MX</div>
        <div class="bdg-07-chip">ja-JP</div>
        <div class="bdg-07-chip">pt-BR</div>
        <div class="bdg-07-chip bdg-07-missing">zh-CN ✕</div>
        <div class="bdg-07-chip bdg-07-missing">ko-KR ✕</div>
        <div class="bdg-07-chip">nl-NL</div>
        <div class="bdg-07-chip">it-IT</div>
        <div class="bdg-07-chip">pl-PL</div>
      </div>
      <div class="bdg-07-warning">zh-CN and ko-KR are missing reciprocal hreflang links back to this URL</div>
    </div>
  </div>
</div>
```
## CSS
```css
.bdg-07-stage {
  background: #f4f1eb;
  padding: 50px 40px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
  min-height: 100vh;
}

.bdg-07-card {
  background: #fff;
  border: 1px solid #e2ddd4;
  border-radius: 6px;
  overflow: hidden;
  width: 100%;
  max-width: 480px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}

.bdg-07-primary {
  display: flex;
  align-items: center;
  padding: 20px 20px 18px;
  border-bottom: 1px solid #e2ddd4;
  gap: 14px;
}

.bdg-07-flag {
  width: 8px;
  align-self: stretch;
  flex-shrink: 0;
  border-radius: 2px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.bdg-07-flag span {
  flex: 1;
}

.bdg-07-code {
  font-family: ui-monospace, "JetBrains Mono", monospace;
  font-size: 22px;
  font-weight: 700;
  color: #1a1612;
  letter-spacing: 0.02em;
}

.bdg-07-name {
  font-family: system-ui, "Bricolage Grotesque", sans-serif;
  font-size: 12px;
  color: #4a4239;
  line-height: 1.4;
  letter-spacing: 0.04em;
}

.bdg-07-alts-count {
  font-family: ui-monospace, "JetBrains Mono", monospace;
  font-size: 10px;
  color: #888;
  margin-left: auto;
  text-align: right;
  white-space: nowrap;
}

.bdg-07-body {
  padding: 16px 20px 18px;
}

.bdg-07-section-label {
  font-family: system-ui, "Bricolage Grotesque", sans-serif;
  font-size: 9px;
  letter-spacing: 0.28em;
  text-transform: uppercase;
  color: #aaa;
  margin-bottom: 10px;
}

.bdg-07-chips {
  display: flex;
  flex-wrap: wrap;
  gap: 5px;
  margin-bottom: 16px;
}

.bdg-07-chip {
  padding: 4px 10px;
  border-radius: 3px;
  font-family: ui-monospace, "JetBrains Mono", monospace;
  font-size: 11px;
  letter-spacing: 0.04em;
  background: #f4f1eb;
  border: 1px solid #e2ddd4;
  color: #1a1612;
  transition: background 0.2s;
  cursor: default;
}

.bdg-07-chip:hover {
  background: #e8e4d8;
}

.bdg-07-xdefault {
  background: #e8f0fe;
  border-color: #c5d8fd;
  color: #4285f4;
}

.bdg-07-missing {
  background: #fde8e8;
  border-color: #f8c0c0;
  color: #ff4e42;
}

.bdg-07-warning {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 12px;
  background: #fff8e8;
  border-radius: 4px;
  border-left: 3px solid #ffa400;
  font-family: system-ui, "Bricolage Grotesque", sans-serif;
  font-size: 11px;
  color: #8a5a00;
  letter-spacing: 0.02em;
}

.bdg-07-warning::before {
  content: '⚠';
  flex-shrink: 0;
}
```
