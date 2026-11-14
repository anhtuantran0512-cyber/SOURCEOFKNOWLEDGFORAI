---
source: "codefronts"
url: "https://codefronts.com/snippets/css-badges/botanical-membership-tier/"
title: "Botanical Membership Tier"
section: "snippets"
category: "css-badges"
category_name: "CSS Badges"
description: "Membership tier grown as SVG flora — petals, leaves, and a budding center on warm paper."
has_js: "false"
---

Here's a working CSS Badge from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Botanical Membership Tier
Source: https://codefronts.com/snippets/css-badges/botanical-membership-tier/

Membership tier grown as SVG flora — petals, leaves, and a budding center on warm paper. Hover sways the leaves outward and blooms the center. Italiana + Cormorant Garamond carry the names.
## HTML
```html
<div class="bdg-26-card">
  <div class="bdg-26-art">
    <svg viewBox="0 0 130 130" aria-hidden="true">
      <path d="M65 115 L65 70" stroke="#5a6a44" stroke-width="2.5" fill="none" class="bdg-26-stem"/>
      <ellipse class="bdg-26-leaf bdg-26-leaf-1" cx="45" cy="90" rx="6" ry="15" fill="#7a8d5f" transform="rotate(-50 45 90)"/>
      <ellipse class="bdg-26-leaf bdg-26-leaf-2" cx="85" cy="90" rx="6" ry="15" fill="#7a8d5f" transform="rotate(50 85 90)"/>
      <g class="bdg-26-petal">
        <ellipse cx="65" cy="40" rx="9" ry="14" fill="#d4a3c2"/>
        <ellipse cx="80" cy="55" rx="9" ry="14" fill="#d4a3c2" transform="rotate(72 80 55)"/>
        <ellipse cx="74" cy="74" rx="9" ry="14" fill="#d4a3c2" transform="rotate(144 74 74)"/>
        <ellipse cx="56" cy="74" rx="9" ry="14" fill="#d4a3c2" transform="rotate(216 56 74)"/>
        <ellipse cx="50" cy="55" rx="9" ry="14" fill="#d4a3c2" transform="rotate(288 50 55)"/>
        <circle cx="65" cy="55" r="6" fill="#e8c878"/>
      </g>
    </svg>
  </div>
  <div class="bdg-26-tier-tag">Tier III</div>
  <div class="bdg-26-tier-name">Bloom</div>
  <div class="bdg-26-tier-desc">All collections, advance previews, and private viewings.</div>
</div>
```
## CSS
```css
.bdg-26-card {
  text-align: center;
  padding: 36px 24px 30px;
  background: linear-gradient(180deg, #f0ede1 0%, #e6e2d1 100%);
  border: 1px solid rgba(66,82,54,0.2);
  border-radius: 4px;
  position: relative;
  cursor: pointer;
  transition: transform 0.5s cubic-bezier(0.2, 0.8, 0.2, 1), box-shadow 0.5s;
  width: 100%;
  min-height: 100vh;
  max-width: 240px;
  margin: 24px auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.bdg-26-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 24px 40px -16px rgba(66, 82, 54, 0.25);
}

.bdg-26-art {
  width: 130px;
  height: 130px;
  margin: 0 auto 20px;
}

.bdg-26-art svg {
  width: 100%;
  height: 100%;
  overflow: visible;
}

.bdg-26-art .bdg-26-leaf,
.bdg-26-art .bdg-26-petal,
.bdg-26-art .bdg-26-stem {
  transition: transform 1.2s cubic-bezier(0.34, 1.56, 0.64, 1);
  transform-origin: 50% 100%;
}

.bdg-26-card:hover .bdg-26-art .bdg-26-leaf-1 {
  transform: rotate(-6deg) translateY(-2px);
}

.bdg-26-card:hover .bdg-26-art .bdg-26-leaf-2 {
  transform: rotate(6deg) translateY(-2px);
}

.bdg-26-card:hover .bdg-26-art .bdg-26-petal {
  transform-origin: 65px 55px;
  transform: scale(1.1);
}

@media (prefers-reduced-motion: reduce) {
  .bdg-26-art .bdg-26-leaf,
    .bdg-26-art .bdg-26-petal {
    transition: none;
  }
}

.bdg-26-tier-tag {
  font-family: "Italiana", Georgia, serif;
  color: #6b7a52;
  font-size: 10px;
  letter-spacing: 0.4em;
  text-transform: uppercase;
  margin-bottom: 4px;
}

.bdg-26-tier-name {
  font-family: "Cormorant Garamond", Georgia, serif;
  color: #2d3a22;
  font-size: 26px;
  font-style: italic;
  font-weight: 400;
  line-height: 1;
  margin-bottom: 12px;
}

.bdg-26-tier-desc {
  font-family: "Cormorant Garamond", Georgia, serif;
  color: #6b7a52;
  font-size: 13px;
  line-height: 1.5;
  padding-top: 12px;
  border-top: 1px solid rgba(66,82,54,0.2);
}
```
