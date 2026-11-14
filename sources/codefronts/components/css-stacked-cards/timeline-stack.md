---
source: "codefronts"
url: "https://codefronts.com/components/css-stacked-cards/timeline-stack/"
title: "Timeline Stack"
section: "components"
category: "css-stacked-cards"
category_name: "CSS Stacked Cards"
description: "A vertical timeline with a gradient spine and milestone nodes."
has_js: "false"
---

Here's a working CSS Stacked Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Timeline Stack
Source: https://codefronts.com/components/css-stacked-cards/timeline-stack/

A vertical timeline with a gradient spine and milestone nodes. Hover slides each card right and pulses its node. Suited to roadmaps, company history, or changelogs.
## HTML
```html
<div class="scd-35">
  <div class="scd-35__stage">
    <div class="scd-35__node"><div class="scd-35__card"><span class="scd-35__yr">2021</span><h3>The Beginning</h3><p>First prototype shipped to ten beta users.</p></div></div>
    <div class="scd-35__node"><div class="scd-35__card"><span class="scd-35__yr">2023</span><h3>Going Public</h3><p>Launched the open platform to everyone.</p></div></div>
    <div class="scd-35__node"><div class="scd-35__card"><span class="scd-35__yr">2025</span><h3>Scale</h3><p>Crossed one million active accounts.</p></div></div>
    <div class="scd-35__node"><div class="scd-35__card"><span class="scd-35__yr">2026</span><h3>What&#39;s Next</h3><p>Reimagining the experience from scratch.</p></div></div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@700&family=Schibsted+Grotesk:wght@400;500&display=swap');

.scd-35,
.scd-35 *,
.scd-35 *::before,
.scd-35 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.scd-35 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  background: linear-gradient(180deg,#fffaf0,#f0e8dc);
  font-family: 'Schibsted Grotesk', sans-serif;
}

.scd-35__stage {
  position: relative;
  width: 340px;
  padding-left: 40px;
}

.scd-35__stage::before {
  content: '';
  position: absolute;
  left: 14px;
  top: 10px;
  bottom: 10px;
  width: 3px;
  background: linear-gradient(#ff8a5c,#a83279);
  border-radius: 3px;
}

.scd-35__node {
  position: relative;
  margin-bottom: 14px;
}

.scd-35__node::before {
  content: '';
  position: absolute;
  left: -33px;
  top: 18px;
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background: #fff;
  border: 3px solid #ff8a5c;
  transition: transform .35s, background .35s;
}

.scd-35__card {
  background: #fff;
  border-radius: 14px;
  padding: 16px 20px;
  box-shadow: 0 8px 20px rgba(120,60,80,.12);
  transition: transform .35s cubic-bezier(.3,.9,.3,1), box-shadow .35s;
  cursor: pointer;
}

.scd-35__yr {
  font-family: 'Bricolage Grotesque', sans-serif;
  color: #a83279;
  font-size: .8rem;
  letter-spacing: .08em;
}

.scd-35__card h3 {
  font-family: 'Bricolage Grotesque', sans-serif;
  font-size: 1.1rem;
  color: #2a2024;
  margin: 2px 0 4px;
}

.scd-35__card p {
  font-size: .85rem;
  color: #6a5a60;
}

.scd-35__node:hover .scd-35__card {
  transform: translateX(12px);
  box-shadow: 0 14px 30px rgba(120,60,80,.2);
}

.scd-35__node:hover::before {
  transform: scale(1.3);
  background: #a83279;
}

@media (prefers-reduced-motion: reduce) {
  .scd-35__card,
    .scd-35__node::before {
    transition: none !important;
  }
}
```
