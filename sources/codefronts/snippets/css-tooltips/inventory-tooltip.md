---
source: "codefronts"
url: "https://codefronts.com/snippets/css-tooltips/inventory-tooltip/"
title: "Inventory Tooltip"
section: "snippets"
category: "css-tooltips"
category_name: "CSS Tooltips"
description: "A rarity-tinted tooltip for games, achievements, and collectibles."
has_js: "false"
---

Here's a working CSS Tooltip from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Inventory Tooltip
Source: https://codefronts.com/snippets/css-tooltips/inventory-tooltip/

A rarity-tinted tooltip for games, achievements, and collectibles. Each rarity tier (common → legendary) glows its own color through the border, the stat list, and the pulsing outline. Italic flavor text closes every card the way a good item description should.
## HTML
```html
<div class="tp-06">
  <div class="tp-06__inv">
    <div class="tp-06__slot tp-06__r-legend">
      <svg class="tp-06__icon" viewBox="0 0 64 64" aria-hidden="true">
        <defs><linearGradient id="tp-06__g1" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fde68a"/><stop offset="1" stop-color="#b45309"/></linearGradient></defs>
        <path d="M32 4 L36 22 L52 14 L42 32 L60 36 L42 40 L52 58 L36 50 L32 60 L28 50 L12 58 L22 40 L4 36 L22 32 L12 14 L28 22 Z" fill="url(#tp-06__g1)" stroke="#fde68a" stroke-width="0.5"/>
        <circle cx="32" cy="36" r="6" fill="#fffbeb"/>
      </svg>
      <div class="tp-06__tip">
        <div class="tp-06__tip-name">Sunburst Talisman</div>
        <div class="tp-06__tip-type">Legendary · Amulet</div>
        <div class="tp-06__tip-stat"><span>Spell Power</span><span class="tp-06__v">+84</span></div>
        <div class="tp-06__tip-stat"><span>Critical Strike</span><span class="tp-06__v">+12%</span></div>
        <div class="tp-06__tip-stat"><span>Movement</span><span class="tp-06__v tp-06__neg">−4%</span></div>
        <div class="tp-06__tip-bar">Awakened · 7/10
          <div class="tp-06__tip-bar-track"><div class="tp-06__tip-bar-fill" style="width:70%"></div></div>
        </div>
        <div class="tp-06__tip-divider"></div>
        <div class="tp-06__tip-flavor">"It does not warm — it only insists that warmth was once here."</div>
        <div class="tp-06__tip-foot"><span>BOUND</span><span>vendor: 2,400g</span></div>
      </div>
    </div>

    <div class="tp-06__slot tp-06__r-epic">
      <svg class="tp-06__icon" viewBox="0 0 64 64" aria-hidden="true">
        <defs><linearGradient id="tp-06__g2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e9d5ff"/><stop offset="1" stop-color="#6b21a8"/></linearGradient></defs>
        <path d="M32 6 L42 24 L52 32 L42 40 L32 58 L22 40 L12 32 L22 24 Z" fill="url(#tp-06__g2)" stroke="#e9d5ff" stroke-width="0.6"/>
        <path d="M32 14 L36 28 L32 36 L28 28 Z" fill="#1a0a25"/>
      </svg>
      <div class="tp-06__tip">
        <div class="tp-06__tip-name">Voidshard Pendant</div>
        <div class="tp-06__tip-type">Epic · Pendant</div>
        <div class="tp-06__tip-stat"><span>Intellect</span><span class="tp-06__v">+62</span></div>
        <div class="tp-06__tip-stat"><span>Shadow Mastery</span><span class="tp-06__v">+9%</span></div>
        <div class="tp-06__tip-bar">Charged · 3/5
          <div class="tp-06__tip-bar-track"><div class="tp-06__tip-bar-fill" style="width:60%"></div></div>
        </div>
        <div class="tp-06__tip-divider"></div>
        <div class="tp-06__tip-flavor">"Cool to the touch. Then colder. Then it whispers your name in a voice that almost is."</div>
        <div class="tp-06__tip-foot"><span>SOULBOUND</span><span>vendor: 1,150g</span></div>
      </div>
    </div>

    <div class="tp-06__slot tp-06__r-rare">
      <svg class="tp-06__icon" viewBox="0 0 64 64" aria-hidden="true">
        <defs><linearGradient id="tp-06__g3" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#93c5fd"/><stop offset="1" stop-color="#1e40af"/></linearGradient></defs>
        <path d="M32 4 L36 20 L52 28 L36 32 L32 60 L28 32 L12 28 L28 20 Z" fill="url(#tp-06__g3)" stroke="#dbeafe" stroke-width="0.5"/>
      </svg>
      <div class="tp-06__tip">
        <div class="tp-06__tip-name">Ranger's Compass</div>
        <div class="tp-06__tip-type">Rare · Trinket</div>
        <div class="tp-06__tip-stat"><span>Agility</span><span class="tp-06__v">+34</span></div>
        <div class="tp-06__tip-stat"><span>Stealth</span><span class="tp-06__v">+7%</span></div>
        <div class="tp-06__tip-divider"></div>
        <div class="tp-06__tip-flavor">"True north is whichever direction the deer have not yet noticed you."</div>
        <div class="tp-06__tip-foot"><span>UNIQUE</span><span>vendor: 480g</span></div>
      </div>
    </div>

    <div class="tp-06__slot tp-06__r-uncommon">
      <svg class="tp-06__icon" viewBox="0 0 64 64" aria-hidden="true">
        <defs><linearGradient id="tp-06__g4" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#bef264"/><stop offset="1" stop-color="#3f6212"/></linearGradient></defs>
        <ellipse cx="32" cy="36" rx="20" ry="22" fill="url(#tp-06__g4)" stroke="#ecfccb" stroke-width="0.5"/>
        <path d="M32 14 Q28 24 32 36" stroke="#1a2e0a" stroke-width="2" fill="none"/>
      </svg>
      <div class="tp-06__tip">
        <div class="tp-06__tip-name">Verdant Tonic</div>
        <div class="tp-06__tip-type">Uncommon · Consumable</div>
        <div class="tp-06__tip-stat"><span>Restores</span><span class="tp-06__v">+1,200 HP</span></div>
        <div class="tp-06__tip-stat"><span>Over</span><span class="tp-06__v">8 sec</span></div>
        <div class="tp-06__tip-divider"></div>
        <div class="tp-06__tip-flavor">"Tastes like the smell of a greenhouse in winter."</div>
        <div class="tp-06__tip-foot"><span>STACK · 14</span><span>vendor: 24g</span></div>
      </div>
    </div>

    <div class="tp-06__slot tp-06__r-common">
      <svg class="tp-06__icon" viewBox="0 0 64 64" aria-hidden="true">
        <path d="M22 18 L42 18 L46 26 L46 46 L18 46 L18 26 Z" fill="#9ca3af" stroke="#e5e7eb" stroke-width="0.5"/>
        <rect x="28" y="26" width="8" height="20" fill="#4b5563"/>
      </svg>
      <div class="tp-06__tip">
        <div class="tp-06__tip-name">Iron Lockbox</div>
        <div class="tp-06__tip-type">Common · Container</div>
        <div class="tp-06__tip-stat"><span>Slots</span><span class="tp-06__v">+6</span></div>
        <div class="tp-06__tip-divider"></div>
        <div class="tp-06__tip-flavor">"Heavy enough to be honest about what it contains."</div>
        <div class="tp-06__tip-foot"><span>STACK · 1</span><span>vendor: 8g</span></div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.tp-06 {
  width: 100%;
  min-height: 100vh;
  background: radial-gradient(ellipse at top, #1a1410 0%, #0a0806 100%);
  /* Generous top room — rpg tooltips pop UP from each slot, ~300px
       tall. The inventory grid sits low so the tip has room above. */
  padding: 320px 28px 60px;
  display: flex;
  align-items: flex-end;
  justify-content: center;
}

.tp-06__inv {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 8px;
  width: 100%;
  max-width: 520px;
  padding: 16px;
  background: linear-gradient(180deg, rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.6));
  border: 1px solid rgba(212, 175, 55, 0.2);
  box-shadow: 0 0 0 1px rgba(0, 0, 0, 0.5), 0 0 50px rgba(212, 175, 55, 0.08), inset 0 1px 0 rgba(212, 175, 55, 0.1);
  position: relative;
}

.tp-06__inv::before {
  content: 'INVENTORY';
  position: absolute;
  top: -24px;
  left: 50%;
  transform: translateX(-50%);
  font-family: Georgia, serif;
  font-size: 11px;
  letter-spacing: 0.3em;
  color: #d4af37;
  background: #1a1410;
  padding: 0 14px;
}

.tp-06__slot {
  aspect-ratio: 1;
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.04), rgba(0, 0, 0, 0.4));
  border: 1px solid rgba(212, 175, 55, 0.15);
  position: relative;
  cursor: pointer;
  transition: transform 0.25s, border-color 0.25s;
  display: flex;
  align-items: center;
  justify-content: center;
}

.tp-06__slot:hover {
  border-color: rgba(212, 175, 55, 0.5);
  transform: translateY(-2px);
}

.tp-06__icon {
  width: 60%;
  height: 60%;
  filter: drop-shadow(0 1px 2px rgba(0, 0, 0, 0.5));
}

.tp-06__slot::after {
  content: '';
  position: absolute;
  bottom: 0;
  right: 0;
  width: 0;
  height: 0;
  border-style: solid;
  border-width: 0 0 10px 10px;
  border-color: transparent;
}

.tp-06__r-common {
  --rpg-color: #b8b8b8;
  --rpg-glow: rgba(180, 180, 180, 0.15);
}

.tp-06__r-uncommon {
  --rpg-color: #4ade80;
  --rpg-glow: rgba(74, 222, 128, 0.20);
}

.tp-06__r-rare {
  --rpg-color: #60a5fa;
  --rpg-glow: rgba(96, 165, 250, 0.25);
}

.tp-06__r-epic {
  --rpg-color: #c084fc;
  --rpg-glow: rgba(192, 132, 252, 0.30);
}

.tp-06__r-legend {
  --rpg-color: #fbbf24;
  --rpg-glow: rgba(251, 191, 36, 0.35);
}

.tp-06__r-common::after {
  border-bottom-color: #aaa;
}

.tp-06__r-uncommon::after {
  border-bottom-color: #4caf50;
}

.tp-06__r-rare::after {
  border-bottom-color: #5cb3ff;
}

.tp-06__r-epic::after {
  border-bottom-color: #b366f2;
}

.tp-06__r-legend::after {
  border-bottom-color: #ffb83d;
}

.tp-06__tip {
  position: absolute;
  bottom: calc(100% + 14px);
  left: 50%;
  transform: translateX(-50%) translateY(8px) scale(0.95);
  width: 240px;
  background: linear-gradient(180deg, #1a1410 0%, #0e0a07 100%);
  border: 1px solid var(--rpg-color, #888);
  padding: 12px 13px;
  font-family: 'Inter', system-ui, sans-serif;
  color: #d4c5a9;
  opacity: 0;
  visibility: hidden;
  transition: opacity 0.2s, transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1), visibility 0s linear 0.2s;
  z-index: 30;
  pointer-events: none;
  box-shadow: 0 0 0 1px rgba(0, 0, 0, 0.8), 0 0 26px var(--rpg-glow, rgba(255, 255, 255, 0.1)), 0 18px 36px -10px rgba(0, 0, 0, 0.8);
  text-align: left;
}

.tp-06__slot:hover .tp-06__tip {
  opacity: 1;
  visibility: visible;
  transform: translateX(-50%) translateY(0) scale(1);
  transition-delay: 0s;
}

.tp-06__tip::before {
  content: '';
  position: absolute;
  inset: -1px;
  border: 1px solid var(--rpg-color, #888);
  opacity: 0.3;
  pointer-events: none;
  animation: tp-06-glow 2s ease-in-out infinite;
}

@keyframes tp-06-glow {
  0%,
    100% {
    opacity: 0.2;
  }

  50% {
    opacity: 0.5;
  }
}

.tp-06__tip-name {
  font-family: Georgia, serif;
  font-weight: 700;
  font-size: 15px;
  color: var(--rpg-color, #fff);
  line-height: 1.2;
  margin-bottom: 2px;
  letter-spacing: 0.02em;
}

.tp-06__tip-type {
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-size: 9.5px;
  color: rgba(212, 197, 169, 0.6);
  text-transform: uppercase;
  letter-spacing: 0.15em;
  margin-bottom: 10px;
}

.tp-06__tip-stat {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 11px;
  padding: 3px 0;
  color: #d4c5a9;
}

.tp-06__v {
  color: #6fd09b;
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-weight: 600;
}

.tp-06__neg {
  color: #f06b5c;
}

.tp-06__tip-bar {
  margin-top: 8px;
  margin-bottom: 4px;
  font-size: 9.5px;
  color: rgba(212, 197, 169, 0.5);
}

.tp-06__tip-bar-track {
  margin-top: 3px;
  height: 4px;
  background: rgba(0, 0, 0, 0.5);
  border: 1px solid rgba(212, 197, 169, 0.15);
  position: relative;
}

.tp-06__tip-bar-fill {
  height: 100%;
  background: var(--rpg-color, #888);
}

.tp-06__tip-divider {
  margin: 10px 0 8px;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(212, 197, 169, 0.2), transparent);
}

.tp-06__tip-flavor {
  font-family: Georgia, serif;
  font-style: italic;
  font-size: 12px;
  color: rgba(212, 197, 169, 0.75);
  line-height: 1.4;
}

.tp-06__tip-foot {
  margin-top: 8px;
  padding-top: 6px;
  border-top: 1px dashed rgba(212, 197, 169, 0.15);
  display: flex;
  justify-content: space-between;
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-size: 9.5px;
  color: rgba(212, 197, 169, 0.5);
}
```
