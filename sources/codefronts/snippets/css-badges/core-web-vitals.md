---
source: "codefronts"
url: "https://codefronts.com/snippets/css-badges/core-web-vitals/"
title: "Core Web Vitals"
section: "snippets"
category: "css-badges"
category_name: "CSS Badges"
description: "LCP, INP, CLS — the three real-world page-experience signals Google ranks on."
has_js: "false"
---

Here's a working CSS Badge from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Core Web Vitals
Source: https://codefronts.com/snippets/css-badges/core-web-vitals/

LCP, INP, CLS — the three real-world page-experience signals Google ranks on. Three SVG arcs draw to their verdict on load. Green / amber / red thresholds match Google's field-data classification.
## HTML
```html
<div class="bdg-12-stage">
  <div class="bdg-12-card">
    <div class="bdg-12-header">
      <div class="bdg-12-title">Core Web Vitals · Field Data</div>
      <div class="bdg-12-pass-count">2 / 3 Pass</div>
    </div>
    <div class="bdg-12-gauges">
      <div class="bdg-12-gauge">
        <svg viewBox="0 0 90 90" aria-hidden="true">
          <circle class="bdg-12-gauge-track" cx="45" cy="45" r="36"/>
          <circle class="bdg-12-gauge-arc" cx="45" cy="45" r="36" stroke="#ffa400" data-len="140" transform="rotate(-90 45 45)"/>
          <text x="45" y="43" text-anchor="middle" class="bdg-12-gauge-val">2.9s</text>
          <text x="45" y="57" text-anchor="middle" class="bdg-12-gauge-unit">LCP</text>
        </svg>
        <div class="bdg-12-metric-name">LCP</div>
        <div class="bdg-12-metric-verdict bdg-12-verdict-needs">Needs Work</div>
      </div>
      <div class="bdg-12-gauge">
        <svg viewBox="0 0 90 90" aria-hidden="true">
          <circle class="bdg-12-gauge-track" cx="45" cy="45" r="36"/>
          <circle class="bdg-12-gauge-arc" cx="45" cy="45" r="36" stroke="#0cce6b" data-len="205" transform="rotate(-90 45 45)"/>
          <text x="45" y="43" text-anchor="middle" class="bdg-12-gauge-val">89ms</text>
          <text x="45" y="57" text-anchor="middle" class="bdg-12-gauge-unit">INP</text>
        </svg>
        <div class="bdg-12-metric-name">INP</div>
        <div class="bdg-12-metric-verdict bdg-12-verdict-good">Good</div>
      </div>
      <div class="bdg-12-gauge">
        <svg viewBox="0 0 90 90" aria-hidden="true">
          <circle class="bdg-12-gauge-track" cx="45" cy="45" r="36"/>
          <circle class="bdg-12-gauge-arc" cx="45" cy="45" r="36" stroke="#0cce6b" data-len="193" transform="rotate(-90 45 45)"/>
          <text x="45" y="43" text-anchor="middle" class="bdg-12-gauge-val">0.08</text>
          <text x="45" y="57" text-anchor="middle" class="bdg-12-gauge-unit">CLS</text>
        </svg>
        <div class="bdg-12-metric-name">CLS</div>
        <div class="bdg-12-metric-verdict bdg-12-verdict-good">Good</div>
      </div>
    </div>
    <div class="bdg-12-footer">
      <div class="bdg-12-origin">example.com/blog/seo-guide/</div>
      <div class="bdg-12-date">28-day field data</div>
    </div>
  </div>
</div>
```
## CSS
```css
.bdg-12-stage {
  background: #0d1117;
  padding: 50px 40px;
  display: flex;
  flex-direction: column;
  gap: 28px;
  align-items: center;
  justify-content: center;
  width: 100%;
  min-height: 100vh;
}

.bdg-12-card {
  background: #161b22;
  border: 1px solid #30363d;
  border-radius: 8px;
  padding: 28px 32px 24px;
  width: 100%;
  max-width: 480px;
}

.bdg-12-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 24px;
}

.bdg-12-title {
  font-family: system-ui, "Bricolage Grotesque", sans-serif;
  font-size: 11px;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: #8b949e;
}

.bdg-12-pass-count {
  font-family: ui-monospace, "JetBrains Mono", monospace;
  font-size: 11px;
  letter-spacing: 0.1em;
  color: #0cce6b;
  padding: 3px 10px;
  border: 1px solid rgba(12, 206, 107, 0.3);
  border-radius: 20px;
}

.bdg-12-gauges {
  display: flex;
  gap: 24px;
  justify-content: center;
  align-items: flex-end;
  padding-bottom: 20px;
  border-bottom: 1px solid #21262d;
}

.bdg-12-gauge {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
}

.bdg-12-gauge svg {
  width: 96px;
  height: 96px;
  overflow: visible;
}

.bdg-12-gauge-track {
  fill: none;
  stroke: #21262d;
  stroke-width: 7;
  stroke-linecap: round;
}

.bdg-12-gauge-arc {
  fill: none;
  stroke-width: 7;
  stroke-linecap: round;
  stroke-dasharray: 226;
  stroke-dashoffset: 226;
  animation: bdg-12-draw 1.1s cubic-bezier(0.4, 0, 0.2, 1) 0.3s forwards;
}

@keyframes bdg-12-draw {
  to {
    stroke-dashoffset: var(--bdg-12-target, 86);
  }
}

@media (prefers-reduced-motion: reduce) {
  .bdg-12-gauge-arc {
    animation: none;
    stroke-dashoffset: 86;
  }
}

.bdg-12-gauge-val {
  font-family: ui-monospace, "JetBrains Mono", monospace;
  fill: #e6edf3;
  font-size: 14px;
  font-weight: 700;
}

.bdg-12-gauge-unit {
  font-family: system-ui, "Bricolage Grotesque", sans-serif;
  fill: #8b949e;
  font-size: 10px;
}

.bdg-12-metric-name {
  font-family: ui-monospace, "JetBrains Mono", monospace;
  font-size: 11px;
  letter-spacing: 0.14em;
  color: #8b949e;
  text-transform: uppercase;
}

.bdg-12-metric-verdict {
  font-family: system-ui, "Bricolage Grotesque", sans-serif;
  font-size: 9px;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  margin-top: -2px;
}

.bdg-12-verdict-good {
  color: #0cce6b;
}

.bdg-12-verdict-needs {
  color: #ffa400;
}

.bdg-12-verdict-poor {
  color: #ff4e42;
}

.bdg-12-footer {
  margin-top: 18px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.bdg-12-origin {
  font-family: ui-monospace, "JetBrains Mono", monospace;
  font-size: 10px;
  letter-spacing: 0.06em;
  color: #4a90d9;
}

.bdg-12-date {
  font-family: system-ui, "Bricolage Grotesque", sans-serif;
  font-size: 10px;
  letter-spacing: 0.1em;
  color: #8b949e;
  text-transform: uppercase;
}
```
