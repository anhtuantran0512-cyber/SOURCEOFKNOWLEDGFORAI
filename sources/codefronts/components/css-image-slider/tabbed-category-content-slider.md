---
source: "codefronts"
url: "https://codefronts.com/components/css-image-slider/tabbed-category-content-slider/"
title: "Tabbed Category Content Slider"
section: "components"
category: "css-image-slider"
category_name: "CSS Image Sliders"
description: "Tabbed category content slider — SaaS-style feature carousel where the pagination is a row of wide text tabs instead of dots."
has_js: "false"
---

Here's a working CSS Image Slider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tabbed Category Content Slider
Source: https://codefronts.com/components/css-image-slider/tabbed-category-content-slider/

Tabbed category content slider — SaaS-style feature carousel where the pagination is a row of wide text tabs instead of dots. Clicking a tab reveals its matching panel (image plus copy) with a smooth cross-fade. Pure CSS via the radio-button pattern; the exact structure Stripe, Vercel, and Linear ship on their product feature pages without shadcn Tabs or Radix Tabs primitives.
## HTML
```html
<div class="cis-12">
  <input type="radio" name="cis-12" id="cis-12-1" checked>
  <input type="radio" name="cis-12" id="cis-12-2">
  <input type="radio" name="cis-12" id="cis-12-3">
  <div class="cis-12__tabs">
    <label for="cis-12-1">Overview</label>
    <label for="cis-12-2">Integrations</label>
    <label for="cis-12-3">Reporting</label>
  </div>
  <div class="cis-12__panels">
    <div class="cis-12__panel">
      <div class="cis-12__media"><img src="https://picsum.photos/seed/cis12a/800/560" alt="Overview screen"></div>
      <div class="cis-12__copy"><h3>One workspace for everything</h3><p>Bring docs, tasks and chat into a single, searchable home. Onboard a teammate in minutes.</p></div>
    </div>
    <div class="cis-12__panel">
      <div class="cis-12__media"><img src="https://picsum.photos/seed/cis12b/800/560" alt="Integrations screen"></div>
      <div class="cis-12__copy"><h3>Connect the tools you already use</h3><p>200+ native integrations, a typed API and webhooks that don't drop events.</p></div>
    </div>
    <div class="cis-12__panel">
      <div class="cis-12__media"><img src="https://picsum.photos/seed/cis12c/800/560" alt="Reporting screen"></div>
      <div class="cis-12__copy"><h3>Reports that build themselves</h3><p>Scheduled dashboards, export to anywhere, and alerts when the numbers move.</p></div>
    </div>
  </div>
</div>
```
## CSS
```css
.cis-12,
.cis-12 *,
.cis-12 *::before,
.cis-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cis-12 ::selection {
  background: oklch(0.82 0.14 265);
  color: #0a0620;
}

.cis-12 {
  --accent: oklch(0.72 0.16 270);
  --surface: #12131d;
  --line: #242637;
  --text: #eef0f7;
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--text);
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 22px;
  padding: 44px 20px;
  background: radial-gradient(120% 110% at 50% 0%,#14162200,#0a0b12);
}

.cis-12 input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.cis-12__tabs {
  display: flex;
  gap: 6px;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 14px;
  padding: 6px;
  width: min(560px,94vw);
  overflow-x: auto;
  scrollbar-width: none;
}

.cis-12__tabs::-webkit-scrollbar {
  display: none;
}

.cis-12__tabs label {
  flex: 1;
  white-space: nowrap;
  text-align: center;
  padding: 11px 16px;
  border-radius: 9px;
  font-size: 14px;
  font-weight: 600;
  color: #9298ac;
  cursor: pointer;
  transition: color .25s,background .25s;
}

.cis-12__tabs label:hover {
  color: #fff;
}

#cis-12-1:checked ~ .cis-12__tabs label[for="cis-12-1"],
#cis-12-2:checked ~ .cis-12__tabs label[for="cis-12-2"],
#cis-12-3:checked ~ .cis-12__tabs label[for="cis-12-3"] {
  color: #fff;
  background: color-mix(in oklab,var(--accent) 30%,transparent);
  box-shadow: inset 0 0 0 1px var(--accent);
}

.cis-12__panels {
  position: relative;
  width: min(760px,94vw);
  min-height: 320px;
}

.cis-12__panel {
  position: absolute;
  inset: 0;
  display: grid;
  grid-template-columns: 1.1fr 1fr;
  gap: 24px;
  align-items: center;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 18px;
  padding: 20px;
  opacity: 0;
  transform: translateY(14px);
  pointer-events: none;
  transition: opacity .45s,transform .45s;
}

#cis-12-1:checked ~ .cis-12__panels .cis-12__panel:nth-child(1),
#cis-12-2:checked ~ .cis-12__panels .cis-12__panel:nth-child(2),
#cis-12-3:checked ~ .cis-12__panels .cis-12__panel:nth-child(3) {
  opacity: 1;
  transform: none;
  pointer-events: auto;
}

.cis-12__media {
  aspect-ratio: 8/5.6;
  border-radius: 12px;
  overflow: hidden;
}

.cis-12__media img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.cis-12__copy h3 {
  font-size: 22px;
  font-weight: 700;
  line-height: 1.15;
  margin-bottom: 10px;
  text-wrap: balance;
}

.cis-12__copy p {
  font-size: 14.5px;
  line-height: 1.55;
  color: #9aa0b4;
}

@media (max-width: 640px) {
  .cis-12__panel {
    grid-template-columns: 1fr;
    overflow-y: auto;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cis-12__panel {
    transition: opacity .2s;
  }
}
```

## JavaScript
```js
/* No JavaScript — text tabs are radio labels; :checked cross-fades the panels. */
```
