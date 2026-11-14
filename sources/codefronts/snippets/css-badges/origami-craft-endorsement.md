---
source: "codefronts"
url: "https://codefronts.com/snippets/css-badges/origami-craft-endorsement/"
title: "Origami Craft Endorsement"
section: "snippets"
category: "css-badges"
category_name: "CSS Badges"
description: "Paper folded along six creases, lit from the upper-left."
has_js: "false"
---

Here's a working CSS Badge from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Origami Craft Endorsement
Source: https://codefronts.com/snippets/css-badges/origami-craft-endorsement/

Paper folded along six creases, lit from the upper-left. A ribbon hangs beneath. Hover lifts the page to catch the fold angles — the lit facets brighten, the shadowed ones recede.
## HTML
```html
<div class="bdg-06-stage">
  <div class="bdg-06-badge">
    <svg class="bdg-06-medal" viewBox="0 0 220 300" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
      <ellipse cx="110" cy="288" rx="68" ry="6" fill="#5a4220" opacity="0.22"/>
      <g>
        <polygon points="80,190 80,260 110,250 110,200" fill="#3d5a6c"/>
        <polygon points="80,260 95,280 110,250" fill="#284252"/>
        <polygon points="110,200 110,250 140,260 140,190" fill="#2a4252"/>
        <polygon points="140,260 125,280 110,250" fill="#1a3242"/>
      </g>
      <polygon class="bdg-06-fold bdg-06-fold-light"  points="110,30 200,82 110,118" fill="#fbe6b0"/>
      <polygon class="bdg-06-fold"                 points="200,82 192,196 110,118" fill="#e8c878"/>
      <polygon class="bdg-06-fold bdg-06-fold-shadow" points="192,196 110,222 110,118" fill="#c8a050"/>
      <polygon class="bdg-06-fold bdg-06-fold-shadow" points="110,222 28,196 110,118" fill="#b8923e"/>
      <polygon class="bdg-06-fold"                 points="28,196 20,82 110,118" fill="#dab866"/>
      <polygon class="bdg-06-fold bdg-06-fold-light"  points="20,82 110,30 110,118" fill="#f4d894"/>
      <line x1="110" y1="30" x2="110" y2="222" stroke="#7a5824" stroke-width="0.4" opacity="0.3"/>
      <line x1="20" y1="82" x2="200" y2="82" stroke="#7a5824" stroke-width="0.4" opacity="0.25"/>
      <line x1="28" y1="196" x2="192" y2="196" stroke="#7a5824" stroke-width="0.4" opacity="0.25"/>
      <polygon points="110,30 200,82 192,196 110,222 28,196 20,82" fill="none" stroke="#fae0a0" stroke-width="0.6" opacity="0.5"/>
      <circle cx="110" cy="118" r="22" fill="#6a4a20" opacity="0.9"/>
      <circle cx="110" cy="118" r="20" fill="none" stroke="#fae0a0" stroke-width="0.6" opacity="0.6"/>
      <text x="110" y="127" text-anchor="middle" font-family="Marcellus, Georgia, serif" font-size="22" fill="#fae0a0" font-weight="400">M</text>
    </svg>
  </div>
  <div class="bdg-06-label">
    <div class="bdg-06-tier">— Master Class —</div>
    <div class="bdg-06-skill">Letterpress &amp; Bindery</div>
    <div class="bdg-06-cert">N° 0247 · Awarded May 2026</div>
  </div>
</div>
```
## CSS
```css
.bdg-06-stage {
  background: linear-gradient(170deg, #eee8d4 0%, #d8d0b8 100%);
  padding: 60px 40px;
  display: flex;
  flex-direction: column;
  gap: 32px;
  align-items: center;
  justify-content: center;
  perspective: 1200px;
  width: 100%;
  min-height: 100vh;
}

.bdg-06-badge {
  position: relative;
  cursor: pointer;
  transform-style: preserve-3d;
  transition: transform 0.6s cubic-bezier(0.2, 0.8, 0.2, 1);
}

.bdg-06-badge:hover {
  transform: rotateY(14deg) rotateX(-6deg);
}

@media (prefers-reduced-motion: reduce) {
  .bdg-06-badge {
    transition: none;
  }
}

.bdg-06-medal {
  width: 220px;
  height: 300px;
  display: block;
  filter: drop-shadow(8px 18px 14px rgba(80,60,20,0.25));
}

.bdg-06-medal .bdg-06-fold {
  transition: filter 0.4s;
}

.bdg-06-badge:hover .bdg-06-medal .bdg-06-fold-light {
  filter: brightness(1.12);
}

.bdg-06-badge:hover .bdg-06-medal .bdg-06-fold-shadow {
  filter: brightness(0.92);
}

.bdg-06-label {
  text-align: center;
}

.bdg-06-tier {
  font-family: system-ui, "Bricolage Grotesque", sans-serif;
  font-size: 9px;
  letter-spacing: 0.42em;
  color: #6a4a20;
  text-transform: uppercase;
  margin-bottom: 6px;
}

.bdg-06-skill {
  font-family: "Marcellus", Georgia, serif;
  font-size: 26px;
  color: #3a2814;
  line-height: 1;
  margin-bottom: 8px;
  letter-spacing: 0.01em;
}

.bdg-06-cert {
  font-family: system-ui, "Bricolage Grotesque", sans-serif;
  font-size: 9px;
  letter-spacing: 0.22em;
  color: #8a6630;
  text-transform: uppercase;
}
```
