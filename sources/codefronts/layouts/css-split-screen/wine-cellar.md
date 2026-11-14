---
source: "codefronts"
url: "https://codefronts.com/layouts/css-split-screen/wine-cellar/"
title: "Wine Cellar"
section: "layouts"
category: "css-split-screen"
category_name: "CSS Split Screen Layouts"
description: "Wine cellar boutique — deep burgundy with gold-leaf accents and cream label typography."
has_js: "false"
---

Here's a working CSS Split Screen Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Wine Cellar
Source: https://codefronts.com/layouts/css-split-screen/wine-cellar/

Wine cellar boutique — deep burgundy with gold-leaf accents and cream label typography. Asymmetric 60/40 split: a single CSS-painted bottle on the left, vintage tasting notes on the right. Real <dl> for the vintage details.
## HTML
```html
<section class="ss-wne" aria-label="Wine bottle and tasting notes">
  <aside class="ss-wne-visual" aria-hidden="true">
    <div class="ss-wne-shelf"></div>
    <div class="ss-wne-bottle">
      <div class="ss-wne-neck"></div>
      <div class="ss-wne-label">
        <em>Château</em>
        <strong>Verdun</strong>
        <span>1987</span>
      </div>
    </div>
    <div class="ss-wne-glow"></div>
  </aside>
  <article class="ss-wne-notes">
    <header>
      <span class="ss-wne-vintage">VINTAGE 1987</span>
      <h2>Château<br /><em>Verdun</em></h2>
      <p>
        A single-vineyard cuvée from the Médoc. Aged 24 months in French oak. Limited release of
        1,200 bottles.
      </p>
    </header>
    <dl class="ss-wne-detail">
      <dt>Region</dt>
      <dd>Bordeaux, France</dd>
      <dt>Varietal</dt>
      <dd>Cabernet Sauvignon (78%)</dd>
      <dt>Aging</dt>
      <dd>24 months · French oak</dd>
      <dt>Tasting</dt>
      <dd>Black cherry, leather, tobacco</dd>
      <dt>Pairing</dt>
      <dd>Dry-aged ribeye, hard cheese</dd>
    </dl>
    <footer class="ss-wne-foot">
      <span class="ss-wne-price">€420 <small>per bottle</small></span>
      <button type="button" class="ss-wne-cta">Add to cellar</button>
    </footer>
  </article>
</section>
```
## CSS
```css
.ss-wne {
  width: 100%;
  display: grid;
  grid-template-columns: 40% 60%;
  min-height: 100vh;
  font-family: 'Cormorant Garamond', 'Georgia', serif;
  background: #1a0a0e;
  color: #f5e6d3;
  border-radius: 0;
  overflow: hidden;
}

.ss-wne-visual {
  position: relative;
  background: radial-gradient(60% 70% at 50% 60%, rgba(80,20,30,0.6) 0%, #0e0608 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.ss-wne-shelf {
  position: absolute;
  bottom: 12%;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(180deg, #5a3825 0%, #3a2415 100%);
  box-shadow: 0 -2px 0 #2a1810, 0 4px 18px rgba(0,0,0,0.6);
}

.ss-wne-bottle {
  position: relative;
  width: 88px;
  height: 280px;
  border-radius: 8px 8px 24px 24px;
  background: linear-gradient(90deg, transparent 0%, rgba(255,255,255,0.06) 30%, transparent 50%), linear-gradient(180deg, #2a0810 0%, #1a0a0e 100%);
  box-shadow: inset -8px 0 24px rgba(0,0,0,0.5), inset 8px 0 12px rgba(180,80,80,0.08), 0 6px 18px rgba(0,0,0,0.5);
  z-index: 2;
}

.ss-wne-neck {
  position: absolute;
  left: 50%;
  top: -54px;
  transform: translateX(-50%);
  width: 28px;
  height: 60px;
  background: linear-gradient(180deg, #1a0608 0%, #2a0810 100%);
  border-radius: 4px 4px 0 0;
  box-shadow: inset -3px 0 8px rgba(0,0,0,0.4);
}

.ss-wne-neck::after {
  content: '';
  position: absolute;
  top: -8px;
  left: -2px;
  right: -2px;
  height: 14px;
  background: linear-gradient(180deg, #d4af37 0%, #8a6f1c 100%);
  border-radius: 3px;
  box-shadow: inset 0 -2px 4px rgba(0,0,0,0.3);
}

.ss-wne-label {
  position: absolute;
  left: 6px;
  right: 6px;
  top: 50%;
  transform: translateY(-50%);
  background: linear-gradient(180deg, #f5e6d3 0%, #e8d4ba 100%);
  padding: 14px 6px;
  text-align: center;
  border-top: 1px solid #d4af37;
  border-bottom: 1px solid #d4af37;
  box-shadow: 0 0 0 0.5px rgba(0,0,0,0.2), 0 2px 4px rgba(0,0,0,0.3);
}

.ss-wne-label em {
  display: block;
  font-family: 'Cormorant Garamond', serif;
  font-size: 9px;
  font-style: italic;
  color: #6e1f1c;
  letter-spacing: 0.08em;
  margin-bottom: 1px;
}

.ss-wne-label strong {
  display: block;
  font-family: 'Cormorant Garamond', serif;
  font-size: 14px;
  font-weight: 700;
  color: #1a0a0e;
  letter-spacing: -0.01em;
  line-height: 1;
}

.ss-wne-label span {
  display: block;
  font-family: 'Inter', sans-serif;
  font-size: 8px;
  font-weight: 700;
  letter-spacing: 0.18em;
  color: #6e1f1c;
  margin-top: 4px;
}

.ss-wne-glow {
  position: absolute;
  bottom: 8%;
  left: 50%;
  transform: translateX(-50%);
  width: 200px;
  height: 30px;
  background: radial-gradient(50% 100% at 50% 0%, rgba(212,175,55,0.18), transparent 70%);
  border-radius: 50%;
  z-index: 1;
}

.ss-wne-notes {
  padding: 44px 48px;
  display: flex;
  flex-direction: column;
  gap: 22px;
  background: radial-gradient(80% 80% at 100% 0%, rgba(110,30,30,0.18) 0%, transparent 70%), #1a0a0e;
}

.ss-wne-vintage {
  font-family: 'Inter', sans-serif;
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 0.3em;
  color: #d4af37;
}

.ss-wne-notes h2 {
  margin: 4px 0 0;
  font-size: clamp(36px, 5vw, 60px);
  font-weight: 500;
  line-height: 0.92;
  color: #f5e6d3;
  letter-spacing: -0.02em;
}

.ss-wne-notes h2 em {
  font-style: italic;
  color: #d4af37;
}

.ss-wne-notes header p {
  margin: 4px 0 0;
  font-size: 15.5px;
  line-height: 1.6;
  color: #c4a888;
  max-width: 440px;
  font-style: italic;
}

.ss-wne-detail {
  margin: 0;
  padding: 18px 0;
  border-top: 1px solid rgba(212,175,55,0.25);
  border-bottom: 1px solid rgba(212,175,55,0.25);
  display: grid;
  grid-template-columns: auto 1fr;
  gap: 10px 22px;
  font-size: 14.5px;
}

.ss-wne-detail dt {
  font-family: 'Inter', sans-serif;
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: #8a6f4a;
  align-self: center;
}

.ss-wne-detail dd {
  margin: 0;
  font-family: 'Cormorant Garamond', serif;
  font-style: italic;
  color: #f5e6d3;
}

.ss-wne-foot {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 14px;
  flex-wrap: wrap;
}

.ss-wne-price {
  font-family: 'Cormorant Garamond', serif;
  font-size: 32px;
  font-weight: 500;
  color: #d4af37;
  letter-spacing: -0.01em;
}

.ss-wne-price small {
  font-family: 'Inter', sans-serif;
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: 0.16em;
  color: #8a6f4a;
  margin-left: 4px;
}

.ss-wne-cta {
  padding: 14px 26px;
  background: transparent;
  color: #d4af37;
  border: 1.5px solid #d4af37;
  font-family: 'Inter', sans-serif;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  cursor: pointer;
  transition: background 0.16s, color 0.16s;
}

.ss-wne-cta:hover {
  background: #d4af37;
  color: #1a0a0e;
}

@media (max-width: 720px) {
  .ss-wne {
    grid-template-columns: 1fr;
  }

  .ss-wne-visual {
    min-height: 320px;
  }
}
```
