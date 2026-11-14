---
source: "codefronts"
url: "https://codefronts.com/components/css-flip-cards/gaming-trading-card-character-stats/"
title: "Gaming Trading Card Character Stats"
section: "components"
category: "css-flip-cards"
category_name: "CSS Flip Cards"
description: "Front displays a stylised SVG character illustration with rarity and ability icons; back lists full competitive stats with type badges and a lore quote."
has_js: "false"
---

Here's a working CSS Flip Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Gaming Trading Card Character Stats
Source: https://codefronts.com/components/css-flip-cards/gaming-trading-card-character-stats/

Front displays a stylised SVG character illustration with rarity and ability icons; back lists full competitive stats with type badges and a lore quote.
## HTML
```html
<div class="fc-08">
  <div class="fc-08__scene">
    <div class="fc-08__card">
      <div class="fc-08__front">
        <div class="fc-08__card-header">
          <div class="fc-08__rarity">★ Legendary</div>
          <div class="fc-08__power">CP 4800</div>
        </div>
        <div class="fc-08__art">
          <svg class="fc-08__char-svg" width="160" height="180" viewBox="0 0 160 180">
            <!-- character silhouette -->
            <ellipse cx="80" cy="40" rx="28" ry="30" fill="rgba(239,68,68,.7)"/>
            <ellipse cx="80" cy="40" rx="18" ry="20" fill="#1a000a"/>
            <!-- eyes -->
            <circle cx="72" cy="38" r="5" fill="rgba(251,191,36,.9)"/>
            <circle cx="88" cy="38" r="5" fill="rgba(251,191,36,.9)"/>
            <circle cx="72" cy="38" r="2" fill="#000"/>
            <circle cx="88" cy="38" r="2" fill="#000"/>
            <!-- body/cloak -->
            <path d="M52 75 Q80 60 108 75 L115 150 Q80 160 45 150 Z" fill="rgba(139,92,246,.5)"/>
            <path d="M62 75 Q80 65 98 75 L102 140 Q80 150 58 140 Z" fill="rgba(30,0,50,.8)"/>
            <!-- weapon -->
            <rect x="105" y="50" width="6" height="90" rx="3" fill="rgba(251,191,36,.6)" transform="rotate(15 108 95)"/>
            <polygon points="108,50 114,40 120,55" fill="rgba(239,68,68,.8)" transform="rotate(15 108 95)"/>
            <!-- cape -->
            <path d="M52 80 Q30 120 35 160 Q52 140 52 120" fill="rgba(139,92,246,.3)"/>
            <path d="M108 80 Q130 120 125 160 Q108 140 108 120" fill="rgba(139,92,246,.3)"/>
            <!-- glow -->
            <circle cx="80" cy="40" r="35" fill="none" stroke="rgba(251,191,36,.2)" stroke-width="2"/>
          </svg>
        </div>
        <div class="fc-08__name-plate">
          <div class="fc-08__char-name">Vex Nightbane</div>
          <div class="fc-08__char-class">Dark Sorcerer · Elite</div>
        </div>
        <div class="fc-08__abilities">
          <div class="fc-08__ability">🔥</div>
          <div class="fc-08__ability">⚡</div>
          <div class="fc-08__ability">💀</div>
          <div class="fc-08__ability">🛡</div>
        </div>
      </div>
      <div class="fc-08__back">
        <div class="fc-08__back-header">
          <div class="fc-08__back-name">Vex Nightbane</div>
          <div class="fc-08__back-cp">CP 4800</div>
        </div>
        <div class="fc-08__type-badges">
          <span class="fc-08__type fc-08__type--fire">🔥 Fire</span>
          <span class="fc-08__type fc-08__type--dark">⚡ Dark</span>
        </div>
        <div class="fc-08__stat-grid">
          <div class="fc-08__stat-box"><div class="fc-08__stat-lbl">Attack</div><div class="fc-08__stat-bar-row"><span class="fc-08__stat-num">94</span><div class="fc-08__stat-track"><div class="fc-08__stat-fill fc-08__fill-red" style="width:94%"></div></div></div></div>
          <div class="fc-08__stat-box"><div class="fc-08__stat-lbl">Magic</div><div class="fc-08__stat-bar-row"><span class="fc-08__stat-num">98</span><div class="fc-08__stat-track"><div class="fc-08__stat-fill fc-08__fill-violet" style="width:98%"></div></div></div></div>
          <div class="fc-08__stat-box"><div class="fc-08__stat-lbl">Defense</div><div class="fc-08__stat-bar-row"><span class="fc-08__stat-num">60</span><div class="fc-08__stat-track"><div class="fc-08__stat-fill fc-08__fill-gold" style="width:60%"></div></div></div></div>
          <div class="fc-08__stat-box"><div class="fc-08__stat-lbl">Speed</div><div class="fc-08__stat-bar-row"><span class="fc-08__stat-num">82</span><div class="fc-08__stat-track"><div class="fc-08__stat-fill fc-08__fill-green" style="width:82%"></div></div></div></div>
        </div>
        <div class="fc-08__lore">"Born from shadow and flame, Vex commands armies of wraiths and bends reality itself. Few have witnessed his full power — fewer still survived."</div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.fc-08,
.fc-08 *,
.fc-08 *::before,
.fc-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fc-08 ::selection {
  background: #dc2626;
  color: #fff;
}

.fc-08 {
  --bg: #0a0005;
  --red: #ef4444;
  --gold: #fbbf24;
  --violet: #8b5cf6;
  --white: #fff5f5;
  --card-w: 280px;
  --card-h: 440px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: radial-gradient(ellipse at 30% 50%,#1a0008,#0a0005 65%);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  color: var(--white);
}

.fc-08__scene {
  width: var(--card-w);
  height: var(--card-h);
  perspective: 1200px;
  cursor: pointer;
}

.fc-08__card {
  width: 100%;
  height: 100%;
  position: relative;
  transform-style: preserve-3d;
  transition: transform .9s cubic-bezier(.4,0,.2,1);
}
/* Trading-card reveal — at the midpoint of the flip the card pops forward
   60px on Z; the scene's box-shadow simultaneously expands into a gold
   glow burst (kept on the scene NOT the card, because applying filter
   to a transform-style:preserve-3d element disables backface-visibility
   in Chromium and breaks the flip). Reads as "card revealing its power"
   rather than a flat spin. */

.fc-08__scene {
  transition: box-shadow .45s ease;
}

.fc-08__scene:hover {
  box-shadow: 0 0 60px 8px rgba(251,191,36,.35);
}

.fc-08__scene:hover .fc-08__card {
  animation: fc-08-power-flip .9s cubic-bezier(.4,0,.2,1) forwards;
}

@keyframes fc-08-power-flip {
  0% {
    transform: rotateY(0deg) translateZ(0);
  }

  50% {
    transform: rotateY(90deg) translateZ(60px);
  }

  100% {
    transform: rotateY(180deg) translateZ(0);
  }
}

.fc-08__front,
.fc-08__back {
  position: absolute;
  inset: 0;
  border-radius: 20px;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  overflow: hidden;
}
/* FRONT */

.fc-08__front {
  background: linear-gradient(160deg,#1a0010,#0d000a);
  border: 2px solid rgba(251,191,36,.35);
  display: flex;
  flex-direction: column;
  box-shadow: 0 0 30px rgba(251,191,36,.1),inset 0 1px 0 rgba(251,191,36,.2);
}

.fc-08__card-header {
  padding: 12px 16px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: linear-gradient(90deg,rgba(251,191,36,.15),transparent);
  border-bottom: 1px solid rgba(251,191,36,.15);
}

.fc-08__rarity {
  font-size: 9px;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--gold);
  font-weight: 800;
}

.fc-08__power {
  font-size: 20px;
  font-weight: 900;
  color: var(--gold);
  text-shadow: 0 0 15px rgba(251,191,36,.5);
}

.fc-08__art {
  flex: 1;
  background: linear-gradient(160deg,#2d0020,#0d0030,#1a000a);
  position: relative;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}

.fc-08__art::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at 50% 60%,rgba(239,68,68,.2),transparent 60%);
}
/* character art via SVG */

.fc-08__char-svg {
  position: relative;
  z-index: 1;
}

.fc-08__name-plate {
  padding: 12px 16px;
  background: linear-gradient(90deg,rgba(239,68,68,.15),rgba(139,92,246,.1));
  border-top: 1px solid rgba(251,191,36,.2);
  border-bottom: 1px solid rgba(251,191,36,.1);
}

.fc-08__char-name {
  font-size: 17px;
  font-weight: 900;
  letter-spacing: .04em;
  color: var(--white);
}

.fc-08__char-class {
  font-size: 10px;
  letter-spacing: .15em;
  text-transform: uppercase;
  color: var(--red);
  font-weight: 600;
  margin-top: 2px;
}

.fc-08__abilities {
  display: flex;
  gap: 6px;
  padding: 10px 16px;
}

.fc-08__ability {
  width: 28px;
  height: 28px;
  border-radius: 8px;
  background: rgba(251,191,36,.1);
  border: 1px solid rgba(251,191,36,.2);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 14px;
}
/* BACK */

.fc-08__back {
  background: linear-gradient(160deg,#0d0020,#15001a);
  border: 2px solid rgba(139,92,246,.35);
  transform: rotateY(180deg);
  display: flex;
  flex-direction: column;
  padding: 20px;
  gap: 10px;
  box-shadow: inset 0 1px 0 rgba(139,92,246,.2);
}

.fc-08__back-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2px;
}

.fc-08__back-name {
  font-size: 16px;
  font-weight: 900;
  color: var(--white);
}

.fc-08__back-cp {
  font-size: 12px;
  font-weight: 700;
  color: var(--gold);
}

.fc-08__stat-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
}

.fc-08__stat-box {
  background: rgba(255,255,255,.04);
  border: 1px solid rgba(255,255,255,.07);
  border-radius: 10px;
  padding: 10px 12px;
}

.fc-08__stat-lbl {
  font-size: 9px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: rgba(255,245,245,.35);
  margin-bottom: 3px;
}

.fc-08__stat-bar-row {
  display: flex;
  align-items: center;
  gap: 6px;
}

.fc-08__stat-num {
  font-size: 15px;
  font-weight: 800;
  color: var(--white);
  min-width: 24px;
}

.fc-08__stat-track {
  flex: 1;
  height: 4px;
  background: rgba(255,255,255,.08);
  border-radius: 2px;
  overflow: hidden;
}

.fc-08__stat-fill {
  height: 100%;
  border-radius: 2px;
}

.fc-08__fill-red {
  background: linear-gradient(90deg,var(--red),#f97316);
}

.fc-08__fill-violet {
  background: linear-gradient(90deg,var(--violet),#a78bfa);
}

.fc-08__fill-gold {
  background: linear-gradient(90deg,var(--gold),#fde68a);
}

.fc-08__fill-green {
  background: linear-gradient(90deg,#22c55e,#86efac);
}

.fc-08__lore {
  margin-top: 4px;
  font-size: 11px;
  color: rgba(255,245,245,.45);
  line-height: 1.6;
  font-style: italic;
  border-left: 2px solid rgba(139,92,246,.3);
  padding-left: 10px;
}

.fc-08__type-badges {
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
}

.fc-08__type {
  font-size: 9px;
  padding: 3px 8px;
  border-radius: 20px;
  font-weight: 700;
  letter-spacing: .06em;
}

.fc-08__type--fire {
  background: rgba(239,68,68,.2);
  border: 1px solid rgba(239,68,68,.3);
  color: var(--red);
}

.fc-08__type--dark {
  background: rgba(139,92,246,.2);
  border: 1px solid rgba(139,92,246,.3);
  color: var(--violet);
}

@media (prefers-reduced-motion: reduce) {
  .fc-08__card {
    transition: none;
  }
}
```
