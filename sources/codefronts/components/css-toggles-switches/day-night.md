---
source: "codefronts"
url: "https://codefronts.com/components/css-toggles-switches/day-night/"
title: "Day / Night"
section: "components"
category: "css-toggles-switches"
category_name: "CSS Toggles & Switches"
description: "A dark-mode toggle that morphs from a sun in a sky-blue track to a crescent moon over a deep night track."
has_js: "false"
---

Here's a working CSS Toggles & Switche from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Day / Night
Source: https://codefronts.com/components/css-toggles-switches/day-night/

A dark-mode toggle that morphs from a sun in a sky-blue track to a crescent moon over a deep night track. The most "what does this control" pattern in the bunch.
## HTML
```html
<label class="tgl-39" aria-label="Theme: light or dark">
  <input class="tgl-39__input" type="checkbox" checked>
  <span class="tgl-39__track" aria-hidden="true">
    <span class="tgl-39__thumb">
      <span class="tgl-39__crater tgl-39__c1"></span>
      <span class="tgl-39__crater tgl-39__c2"></span>
      <span class="tgl-39__crater tgl-39__c3"></span>
    </span>
    <span class="tgl-39__star tgl-39__s1"></span>
    <span class="tgl-39__star tgl-39__s2"></span>
    <span class="tgl-39__star tgl-39__s3"></span>
  </span>
</label>
```
## CSS
```css
.tgl-39 {
  font-family: "Inter", "Segoe UI", system-ui, sans-serif;
  font-size: 14px;
  min-height: 100vh;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 24px;
  padding: 48px 20px;
  background: #14141e;
  box-sizing: border-box;
}

.tgl-39__input {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0,0,0,0);
  white-space: nowrap;
  border: 0;
}

.tgl-39__track {
  position: relative;
  width: 72px;
  height: 36px;
  background: linear-gradient(180deg, #87ceeb 0%, #4a90c2 100%);
  border-radius: 999px;
  overflow: hidden;
  transition: background 0.4s ease;
  box-shadow: inset 0 1px 3px rgba(0,0,0,0.2);
}

.tgl-39__thumb {
  position: absolute;
  top: 3px;
  left: 3px;
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background: radial-gradient(circle at 35% 35%, #ffe066 0%, #f5a623 90%);
  box-shadow: 0 0 14px rgba(255, 224, 102, 0.7);
  transition: left 0.4s cubic-bezier(0.4, 0, 0.2, 1), background 0.4s ease, box-shadow 0.4s ease;
}

.tgl-39__crater {
  position: absolute;
  border-radius: 50%;
  background: #2a2a30;
  opacity: 0;
  transition: opacity 0.4s ease;
}

.tgl-39__c1 {
  top: 6px;
  left: 8px;
  width: 6px;
  height: 6px;
}

.tgl-39__c2 {
  top: 14px;
  left: 18px;
  width: 4px;
  height: 4px;
}

.tgl-39__c3 {
  top: 20px;
  left: 6px;
  width: 5px;
  height: 5px;
}

.tgl-39__star {
  position: absolute;
  width: 2px;
  height: 2px;
  background: #fff;
  border-radius: 50%;
  opacity: 0;
  transition: opacity 0.4s ease;
}

.tgl-39__s1 {
  top: 8px;
  left: 14px;
}

.tgl-39__s2 {
  top: 18px;
  left: 24px;
  width: 1.5px;
  height: 1.5px;
}

.tgl-39__s3 {
  top: 10px;
  left: 28px;
}

.tgl-39__input:not(:checked) ~ .tgl-39__track {
  background: linear-gradient(180deg, #0a1322 0%, #1c2540 100%);
}

.tgl-39__input:not(:checked) ~ .tgl-39__track .tgl-39__thumb {
  left: 39px;
  background: radial-gradient(circle at 35% 35%, #e8e6f0 0%, #a8a5bb 90%);
  box-shadow: 0 0 12px rgba(168, 165, 187, 0.5);
}

.tgl-39__input:not(:checked) ~ .tgl-39__track .tgl-39__crater {
  opacity: 0.5;
}

.tgl-39__input:not(:checked) ~ .tgl-39__track .tgl-39__star {
  opacity: 0.85;
}

.tgl-39__input:focus-visible ~ .tgl-39__track {
  outline: 2px solid #ffe066;
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .tgl-39__track,
    .tgl-39__thumb,
    .tgl-39__crater,
    .tgl-39__star {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the thumb's radial gradient swaps sun→moon while crater and star spans crossfade with opacity over the re-graded track. */
```
