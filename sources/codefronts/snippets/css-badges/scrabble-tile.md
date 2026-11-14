---
source: "codefronts"
url: "https://codefronts.com/snippets/css-badges/scrabble-tile/"
title: "Scrabble Tile"
section: "snippets"
category: "css-badges"
category_name: "CSS Badges"
description: "One letter, one number."
has_js: "false"
---

Here's a working CSS Badge from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Scrabble Tile
Source: https://codefronts.com/snippets/css-badges/scrabble-tile/

One letter, one number. The whole game fits in a square. Hover lifts each tile independently — the kind of small detail that makes a word feel played rather than typed.
## HTML
```html
<div class="bdg-03-stage">
  <div class="bdg-03-wrap">
    <div class="bdg-03-row">
      <div class="bdg-03-cube"><span class="bdg-03-letter">S</span><span class="bdg-03-points">1</span></div>
      <div class="bdg-03-cube"><span class="bdg-03-letter">I</span><span class="bdg-03-points">1</span></div>
      <div class="bdg-03-cube"><span class="bdg-03-letter">M</span><span class="bdg-03-points">3</span></div>
      <div class="bdg-03-cube"><span class="bdg-03-letter">P</span><span class="bdg-03-points">3</span></div>
      <div class="bdg-03-cube"><span class="bdg-03-letter">L</span><span class="bdg-03-points">1</span></div>
      <div class="bdg-03-cube"><span class="bdg-03-letter">E</span><span class="bdg-03-points">1</span></div>
    </div>
    <div class="bdg-03-word-label">10 points · 6 letters · adjective</div>
  </div>
</div>
```
## CSS
```css
.bdg-03-stage {
  background: linear-gradient(145deg, #e8dfc8 0%, #d8d0b4 100%);
  padding: 60px 48px;
  display: flex;
  flex-direction: column;
  gap: 16px;
  justify-content: center;
  align-items: center;
  width: 100%;
  min-height: 100vh;
}

.bdg-03-wrap {
  display: flex;
  flex-direction: column;
  gap: 18px;
  align-items: center;
}

.bdg-03-row {
  display: flex;
  gap: 6px;
  align-items: flex-end;
}

.bdg-03-cube {
  width: 58px;
  height: 58px;
  background: linear-gradient(145deg, #f4e8c2 0%, #e8d8a0 100%);
  border: 1px solid #c8a840;
  border-radius: 4px;
  position: relative;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.5), 2px 3px 0 #b09030, 3px 4px 4px rgba(80,60,0,0.2);
  transition: transform 0.25s cubic-bezier(0.2, 0.8, 0.2, 1), box-shadow 0.25s;
  user-select: none;
}

.bdg-03-cube:hover {
  transform: translateY(-6px) rotate(-2deg);
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.5), 2px 3px 0 #b09030, 6px 12px 16px rgba(80,60,0,0.22);
}

@media (prefers-reduced-motion: reduce) {
  .bdg-03-cube {
    transition: none;
  }
}

.bdg-03-letter {
  font-family: "Cinzel", Georgia, serif;
  font-size: 30px;
  font-weight: 700;
  color: #2a1e08;
  line-height: 1;
}

.bdg-03-points {
  position: absolute;
  bottom: 4px;
  right: 5px;
  font-family: ui-monospace, "JetBrains Mono", monospace;
  font-size: 10px;
  font-weight: 700;
  color: #4a3818;
  line-height: 1;
}

.bdg-03-word-label {
  font-family: "Cormorant Garamond", Georgia, serif;
  font-style: italic;
  font-size: 13px;
  letter-spacing: 0.08em;
  color: #7a6230;
  text-align: center;
  margin-top: 4px;
}
```
