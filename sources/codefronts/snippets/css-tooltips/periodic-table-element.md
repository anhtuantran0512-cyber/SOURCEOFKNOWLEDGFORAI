---
source: "codefronts"
url: "https://codefronts.com/snippets/css-tooltips/periodic-table-element/"
title: "Periodic Table Element"
section: "snippets"
category: "css-tooltips"
category_name: "CSS Tooltips"
description: "Periodic-table tiles for the first three periods, color-coded by element category (nonmetal, alkali, halogen, noble, metalloid, etc.). Hover any tile and a…"
has_js: "false"
---

Here's a working CSS Tooltip from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Periodic Table Element
Source: https://codefronts.com/snippets/css-tooltips/periodic-table-element/

Periodic-table tiles for the first three periods, color-coded by element category (nonmetal, alkali, halogen, noble, metalloid, etc.). Hover any tile and a card lifts in with atomic number, mass, electron configuration, melting/boiling points, and discovery credit.
## HTML
```html
<div class="tp-16">
  <div class="tp-16__grid">
    <div class="tp-16__row">
      <div class="tp-16__tile tp-16__nonmetal">
        <div class="tp-16__num">1</div><div class="tp-16__sym">H</div><div class="tp-16__name">Hydrogen</div><div class="tp-16__mass">1.008</div>
        <div class="tp-16__card">
          <div class="tp-16__card-top"><div class="tp-16__card-sym">H</div><div class="tp-16__card-name">Hydrogen</div><span class="tp-16__cat tp-16__cat-nonmetal">Reactive Nonmetal</span></div>
          <div class="tp-16__card-data">
            <div class="tp-16__card-row"><span class="tp-16__card-key">Atomic No.</span><span class="tp-16__card-val">1</span></div>
            <div class="tp-16__card-row"><span class="tp-16__card-key">Atomic Mass</span><span class="tp-16__card-val">1.008 u</span></div>
            <div class="tp-16__card-row"><span class="tp-16__card-key">Config</span><span class="tp-16__card-econfig">1s¹</span></div>
            <div class="tp-16__card-row"><span class="tp-16__card-key">State (25°C)</span><span class="tp-16__card-val">Gas</span></div>
            <div class="tp-16__card-row"><span class="tp-16__card-key">Boiling pt.</span><span class="tp-16__card-val">−252.9 °C</span></div>
          </div>
          <div class="tp-16__card-disc">Discovered 1766 · Henry Cavendish</div>
        </div>
      </div>
      <div class="tp-16__gap" style="width:380px"></div>
      <div class="tp-16__tile tp-16__noble">
        <div class="tp-16__num">2</div><div class="tp-16__sym">He</div><div class="tp-16__name">Helium</div><div class="tp-16__mass">4.003</div>
        <div class="tp-16__card">
          <div class="tp-16__card-top"><div class="tp-16__card-sym">He</div><div class="tp-16__card-name">Helium</div><span class="tp-16__cat tp-16__cat-noble">Noble Gas</span></div>
          <div class="tp-16__card-data">
            <div class="tp-16__card-row"><span class="tp-16__card-key">Atomic No.</span><span class="tp-16__card-val">2</span></div>
            <div class="tp-16__card-row"><span class="tp-16__card-key">Atomic Mass</span><span class="tp-16__card-val">4.003 u</span></div>
            <div class="tp-16__card-row"><span class="tp-16__card-key">Config</span><span class="tp-16__card-econfig">1s²</span></div>
            <div class="tp-16__card-row"><span class="tp-16__card-key">Boiling pt.</span><span class="tp-16__card-val">−268.9 °C</span></div>
          </div>
          <div class="tp-16__card-disc">Discovered 1895 · Ramsey, Clève, Langlet</div>
        </div>
      </div>
    </div>
    <div class="tp-16__row">
      <div class="tp-16__tile tp-16__alkali">
        <div class="tp-16__num">3</div><div class="tp-16__sym">Li</div><div class="tp-16__name">Lithium</div><div class="tp-16__mass">6.941</div>
        <div class="tp-16__card">
          <div class="tp-16__card-top"><div class="tp-16__card-sym">Li</div><div class="tp-16__card-name">Lithium</div><span class="tp-16__cat tp-16__cat-alkali">Alkali Metal</span></div>
          <div class="tp-16__card-data">
            <div class="tp-16__card-row"><span class="tp-16__card-key">Atomic No.</span><span class="tp-16__card-val">3</span></div>
            <div class="tp-16__card-row"><span class="tp-16__card-key">Config</span><span class="tp-16__card-econfig">[He] 2s¹</span></div>
            <div class="tp-16__card-row"><span class="tp-16__card-key">Melting pt.</span><span class="tp-16__card-val">180.5 °C</span></div>
            <div class="tp-16__card-row"><span class="tp-16__card-key">Use</span><span class="tp-16__card-val">Batteries, ceramics</span></div>
          </div>
          <div class="tp-16__card-disc">Discovered 1817 · J. A. Arfwedson</div>
        </div>
      </div>
      <div class="tp-16__tile tp-16__alkaline">
        <div class="tp-16__num">4</div><div class="tp-16__sym">Be</div><div class="tp-16__name">Beryllium</div><div class="tp-16__mass">9.012</div>
        <div class="tp-16__card">
          <div class="tp-16__card-top"><div class="tp-16__card-sym">Be</div><div class="tp-16__card-name">Beryllium</div><span class="tp-16__cat tp-16__cat-alkaline">Alkaline Earth</span></div>
          <div class="tp-16__card-data">
            <div class="tp-16__card-row"><span class="tp-16__card-key">Atomic No.</span><span class="tp-16__card-val">4</span></div>
            <div class="tp-16__card-row"><span class="tp-16__card-key">Config</span><span class="tp-16__card-econfig">[He] 2s²</span></div>
            <div class="tp-16__card-row"><span class="tp-16__card-key">Melting pt.</span><span class="tp-16__card-val">1,287 °C</span></div>
            <div class="tp-16__card-row"><span class="tp-16__card-key">Note</span><span class="tp-16__card-val">Highly toxic dust</span></div>
          </div>
          <div class="tp-16__card-disc">Discovered 1798 · L.-N. Vauquelin</div>
        </div>
      </div>
      <div class="tp-16__gap" style="width:300px"></div>
      <div class="tp-16__tile tp-16__metalloid">
        <div class="tp-16__num">5</div><div class="tp-16__sym">B</div><div class="tp-16__name">Boron</div><div class="tp-16__mass">10.81</div>
        <div class="tp-16__card">
          <div class="tp-16__card-top"><div class="tp-16__card-sym">B</div><div class="tp-16__card-name">Boron</div><span class="tp-16__cat tp-16__cat-metalloid">Metalloid</span></div>
          <div class="tp-16__card-data">
            <div class="tp-16__card-row"><span class="tp-16__card-key">Config</span><span class="tp-16__card-econfig">[He] 2s² 2p¹</span></div>
            <div class="tp-16__card-row"><span class="tp-16__card-key">Melting pt.</span><span class="tp-16__card-val">2,076 °C</span></div>
          </div>
          <div class="tp-16__card-disc">Discovered 1808 · Gay-Lussac, Davy</div>
        </div>
      </div>
      <div class="tp-16__tile tp-16__nonmetal">
        <div class="tp-16__num">6</div><div class="tp-16__sym">C</div><div class="tp-16__name">Carbon</div><div class="tp-16__mass">12.01</div>
        <div class="tp-16__card">
          <div class="tp-16__card-top"><div class="tp-16__card-sym">C</div><div class="tp-16__card-name">Carbon</div><span class="tp-16__cat tp-16__cat-nonmetal">Reactive Nonmetal</span></div>
          <div class="tp-16__card-data">
            <div class="tp-16__card-row"><span class="tp-16__card-key">Config</span><span class="tp-16__card-econfig">[He] 2s² 2p²</span></div>
            <div class="tp-16__card-row"><span class="tp-16__card-key">Allotropes</span><span class="tp-16__card-val">Diamond, graphite</span></div>
            <div class="tp-16__card-row"><span class="tp-16__card-key">Sublimation</span><span class="tp-16__card-val">3,642 °C</span></div>
          </div>
          <div class="tp-16__card-disc">Known since antiquity</div>
        </div>
      </div>
      <div class="tp-16__tile tp-16__nonmetal">
        <div class="tp-16__num">7</div><div class="tp-16__sym">N</div><div class="tp-16__name">Nitrogen</div><div class="tp-16__mass">14.01</div>
        <div class="tp-16__card">
          <div class="tp-16__card-top"><div class="tp-16__card-sym">N</div><div class="tp-16__card-name">Nitrogen</div><span class="tp-16__cat tp-16__cat-nonmetal">Reactive Nonmetal</span></div>
          <div class="tp-16__card-data">
            <div class="tp-16__card-row"><span class="tp-16__card-key">Config</span><span class="tp-16__card-econfig">[He] 2s² 2p³</span></div>
            <div class="tp-16__card-row"><span class="tp-16__card-key">Boiling pt.</span><span class="tp-16__card-val">−195.8 °C</span></div>
            <div class="tp-16__card-row"><span class="tp-16__card-key">Atmosphere</span><span class="tp-16__card-val">78% of air</span></div>
          </div>
          <div class="tp-16__card-disc">Discovered 1772 · Daniel Rutherford</div>
        </div>
      </div>
      <div class="tp-16__tile tp-16__nonmetal">
        <div class="tp-16__num">8</div><div class="tp-16__sym">O</div><div class="tp-16__name">Oxygen</div><div class="tp-16__mass">16.00</div>
        <div class="tp-16__card">
          <div class="tp-16__card-top"><div class="tp-16__card-sym">O</div><div class="tp-16__card-name">Oxygen</div><span class="tp-16__cat tp-16__cat-nonmetal">Reactive Nonmetal</span></div>
          <div class="tp-16__card-data">
            <div class="tp-16__card-row"><span class="tp-16__card-key">Config</span><span class="tp-16__card-econfig">[He] 2s² 2p⁴</span></div>
            <div class="tp-16__card-row"><span class="tp-16__card-key">Boiling pt.</span><span class="tp-16__card-val">−183 °C</span></div>
          </div>
          <div class="tp-16__card-disc">Discovered 1771 · C. W. Scheele</div>
        </div>
      </div>
      <div class="tp-16__tile tp-16__halogen">
        <div class="tp-16__num">9</div><div class="tp-16__sym">F</div><div class="tp-16__name">Fluorine</div><div class="tp-16__mass">19.00</div>
        <div class="tp-16__card">
          <div class="tp-16__card-top"><div class="tp-16__card-sym">F</div><div class="tp-16__card-name">Fluorine</div><span class="tp-16__cat tp-16__cat-halogen">Halogen</span></div>
          <div class="tp-16__card-data">
            <div class="tp-16__card-row"><span class="tp-16__card-key">Config</span><span class="tp-16__card-econfig">[He] 2s² 2p⁵</span></div>
            <div class="tp-16__card-row"><span class="tp-16__card-key">Electronegativity</span><span class="tp-16__card-val">3.98 (highest)</span></div>
            <div class="tp-16__card-row"><span class="tp-16__card-key">Boiling pt.</span><span class="tp-16__card-val">−188 °C</span></div>
          </div>
          <div class="tp-16__card-disc">Isolated 1886 · Henri Moissan</div>
        </div>
      </div>
      <div class="tp-16__tile tp-16__noble">
        <div class="tp-16__num">10</div><div class="tp-16__sym">Ne</div><div class="tp-16__name">Neon</div><div class="tp-16__mass">20.18</div>
        <div class="tp-16__card">
          <div class="tp-16__card-top"><div class="tp-16__card-sym">Ne</div><div class="tp-16__card-name">Neon</div><span class="tp-16__cat tp-16__cat-noble">Noble Gas</span></div>
          <div class="tp-16__card-data">
            <div class="tp-16__card-row"><span class="tp-16__card-key">Config</span><span class="tp-16__card-econfig">[He] 2s² 2p⁶</span></div>
            <div class="tp-16__card-row"><span class="tp-16__card-key">Boiling pt.</span><span class="tp-16__card-val">−246.1 °C</span></div>
            <div class="tp-16__card-row"><span class="tp-16__card-key">Emission</span><span class="tp-16__card-val">Red-orange glow</span></div>
          </div>
          <div class="tp-16__card-disc">Discovered 1898 · Ramsay & Travers</div>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.tp-16 {
  width: 100%;
  min-height: 100vh;
  background: #0d0d10;
  /* Top room — element cards pop UP from each tile, ~240px tall. */
  padding: 260px 28px 40px;
  font-family: 'JetBrains Mono', ui-monospace, monospace;
}

.tp-16__grid {
  max-width: 660px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 5px;
  align-items: center;
}

.tp-16__row {
  display: flex;
  gap: 5px;
}

.tp-16__tile {
  position: relative;
  width: 56px;
  height: 56px;
  border-radius: 4px;
  padding: 5px 6px;
  cursor: help;
  transition: transform .15s;
  border: 1px solid transparent;
  flex-shrink: 0;
}

.tp-16__tile:hover {
  transform: scale(1.08) translateY(-2px);
  z-index: 10;
}

.tp-16__nonmetal {
  background: rgba(40, 80, 40, 0.3);
  border-color: rgba(60, 160, 60, 0.25);
}

.tp-16__alkali {
  background: rgba(80, 20, 20, 0.3);
  border-color: rgba(200, 60, 40, 0.25);
}

.tp-16__alkaline {
  background: rgba(80, 50, 0, 0.3);
  border-color: rgba(200, 140, 0, 0.25);
}

.tp-16__metalloid {
  background: rgba(20, 60, 80, 0.3);
  border-color: rgba(40, 160, 200, 0.25);
}

.tp-16__noble {
  background: rgba(60, 20, 80, 0.3);
  border-color: rgba(160, 60, 200, 0.25);
}

.tp-16__halogen {
  background: rgba(60, 60, 0, 0.3);
  border-color: rgba(180, 180, 20, 0.25);
}

.tp-16__gap {
  height: 56px;
  flex-shrink: 0;
}

.tp-16__num {
  font-size: 7.5px;
  color: rgba(255, 255, 255, 0.25);
}

.tp-16__sym {
  font-size: 19px;
  font-weight: 600;
  color: rgba(255, 255, 255, 0.88);
  line-height: 1;
  margin: 1px 0 2px;
}

.tp-16__name {
  font-size: 7px;
  color: rgba(255, 255, 255, 0.35);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.tp-16__mass {
  font-size: 6.5px;
  color: rgba(255, 255, 255, 0.2);
  margin-top: 1px;
}

.tp-16__card {
  position: absolute;
  bottom: calc(100% + 10px);
  left: 50%;
  transform: translateX(-50%) translateY(-6px);
  z-index: 300;
  width: 220px;
  background: #141418;
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 8px;
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transition: opacity .2s, transform .2s cubic-bezier(0.22, 1, 0.36, 1), visibility 0s linear .2s;
  box-shadow: 0 16px 44px rgba(0, 0, 0, 0.95);
  overflow: hidden;
  text-align: left;
}

.tp-16__tile:hover .tp-16__card {
  opacity: 1;
  visibility: visible;
  transform: translateX(-50%) translateY(0);
  transition-delay: 0s;
}

.tp-16__card-top {
  padding: 11px 13px 9px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.06);
}

.tp-16__card-sym {
  font-size: 24px;
  font-weight: 600;
  color: rgba(255, 255, 255, 0.9);
  line-height: 1;
}

.tp-16__card-name {
  font-size: 13px;
  color: rgba(255, 255, 255, 0.55);
  margin-top: 2px;
}

.tp-16__cat {
  display: inline-block;
  font-size: 7.5px;
  padding: 2px 6px;
  border-radius: 3px;
  margin-top: 6px;
  letter-spacing: 0.07em;
  text-transform: uppercase;
}

.tp-16__cat-nonmetal {
  background: rgba(60, 160, 60, 0.15);
  color: #60c060;
  border: 1px solid rgba(60, 160, 60, 0.2);
}

.tp-16__cat-alkali {
  background: rgba(180, 40, 20, 0.15);
  color: #e06050;
  border: 1px solid rgba(180, 40, 20, 0.2);
}

.tp-16__cat-alkaline {
  background: rgba(160, 100, 0, 0.15);
  color: #c09020;
  border: 1px solid rgba(160, 100, 0, 0.2);
}

.tp-16__cat-metalloid {
  background: rgba(20, 100, 140, 0.15);
  color: #40c0e0;
  border: 1px solid rgba(20, 100, 140, 0.2);
}

.tp-16__cat-noble {
  background: rgba(120, 40, 160, 0.15);
  color: #a060e0;
  border: 1px solid rgba(120, 40, 160, 0.2);
}

.tp-16__cat-halogen {
  background: rgba(140, 140, 0, 0.15);
  color: #c0c020;
  border: 1px solid rgba(140, 140, 0, 0.2);
}

.tp-16__card-data {
  padding: 9px 13px;
}

.tp-16__card-row {
  display: flex;
  justify-content: space-between;
  margin-bottom: 5px;
}

.tp-16__card-key {
  font-size: 7.5px;
  color: rgba(255, 255, 255, 0.2);
  letter-spacing: 0.08em;
}

.tp-16__card-val {
  font-size: 9px;
  color: rgba(255, 255, 255, 0.55);
  font-style: italic;
}

.tp-16__card-econfig {
  font-size: 8px;
  color: rgba(255, 255, 255, 0.35);
  letter-spacing: 0.04em;
}

.tp-16__card-disc {
  padding: 8px 13px;
  border-top: 1px solid rgba(255, 255, 255, 0.04);
  font-size: 8.5px;
  color: rgba(255, 255, 255, 0.2);
  letter-spacing: 0.04em;
}
```
