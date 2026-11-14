---
source: "codefronts"
url: "https://codefronts.com/layouts/css-hero-sections/vertical-type-hero/"
title: "Vertical Type Hero"
section: "layouts"
category: "css-hero-sections"
category_name: "CSS Hero Sections"
description: "Japanese traditional vertical typography — headline reads top-to-bottom using writing-mode: vertical-rl. Indigo on washi-paper white, vermillion seal stamp."
has_js: "false"
---

Here's a working CSS Hero Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Vertical Type Hero
Source: https://codefronts.com/layouts/css-hero-sections/vertical-type-hero/

Japanese traditional vertical typography — headline reads top-to-bottom using writing-mode: vertical-rl. Indigo on washi-paper white, vermillion seal stamp.
## HTML
```html
<section class="hs-17" aria-label="Hero">
  <div class="hs-17__bg" aria-hidden="true"></div>
  <aside class="hs-17__seal" aria-hidden="true">
    <span>無</span>
    <span>名</span>
  </aside>
  <div class="hs-17__vertical">
    <h2>静かな<em>道具</em>。</h2>
  </div>
  <div class="hs-17__copy">
    <p class="hs-17__jp">Shizuka na dōgu — quiet tools.</p>
    <p class="hs-17__en">
      Hand-forged carpentry implements. Made by one family in Niigata since 1873.
    </p>
    <a class="hs-17__cta" href="#shop">View the catalogue →</a>
  </div>
</section>
```
## CSS
```css
.hs-17 {
  position: relative;
  display: grid;
  grid-template-columns: auto 1fr;
  grid-template-rows: auto auto;
  align-items: center;
  width: 100%;
  min-height: 100vh;
  padding: clamp(28px, 4vw, 56px);
  gap: clamp(28px, 5vw, 64px);
  background: radial-gradient(80% 60% at 50% 0%, rgba(20,40,80,0.06), transparent 70%), #f5ede0;
  font-family: 'Cormorant Garamond', Georgia, serif;
  color: #1a2858;
  box-sizing: border-box;
  overflow: hidden;
}

.hs-17__bg {
  position: absolute;
  right: -60px;
  top: 0;
  bottom: 0;
  width: 280px;
  background: repeating-linear-gradient(0deg, transparent 0 23px, rgba(26,40,88,0.05) 23px 24px);
  pointer-events: none;
}

.hs-17__vertical {
  grid-column: 1;
  grid-row: 1 / 3;
  writing-mode: vertical-rl;
  text-orientation: upright;
  align-self: center;
  display: block;
  height: 100%;
  min-height: 380px;
}

.hs-17 h2 {
  margin: 0;
  font-size: clamp(36px, 4.8vw, 56px);
  font-weight: 700;
  letter-spacing: 0.04em;
  color: #1a2858;
  line-height: 1.2;
  white-space: nowrap;
}

.hs-17 h2 em {
  color: #c63828;
  font-style: normal;
  font-weight: 800;
}

.hs-17__copy {
  grid-column: 2;
  grid-row: 1 / 3;
  display: flex;
  flex-direction: column;
  gap: 18px;
  position: relative;
  z-index: 1;
  max-width: 460px;
}

.hs-17__jp {
  font-family: 'Cormorant Garamond', Georgia, serif;
  font-style: italic;
  font-size: 18px;
  color: #c63828;
  margin: 0;
  letter-spacing: 0.06em;
}

.hs-17__en {
  font-family: 'Inter', system-ui, sans-serif;
  font-size: 15px;
  line-height: 1.6;
  color: #4a5478;
  margin: 0;
}

.hs-17__seal {
  position: absolute;
  top: clamp(20px, 3vw, 32px);
  right: clamp(20px, 3vw, 32px);
  width: 78px;
  height: 78px;
  background: #c63828;
  color: #f5ede0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-family: 'Inter', sans-serif;
  font-weight: 700;
  font-size: 22px;
  border: 2px solid #c63828;
  box-shadow: inset 0 0 0 4px #f5ede0, inset 0 0 0 6px #c63828;
  z-index: 2;
}

.hs-17__cta {
  display: inline-block;
  padding: 12px 22px;
  background: #1a2858;
  color: #f5ede0;
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-decoration: none;
  align-self: flex-start;
  transition: background 0.15s;
}

.hs-17__cta:hover {
  background: #c63828;
}

@media (max-width: 720px) {
  .hs-17 {
    grid-template-columns: 1fr;
    max-height: none;
  }

  .hs-17__vertical {
    grid-column: 1;
    grid-row: auto;
    min-height: 200px;
  }

  .hs-17__copy {
    grid-column: 1;
    grid-row: auto;
  }

  .hs-17__seal {
    top: 16px;
    right: 16px;
    width: 60px;
    height: 60px;
    font-size: 18px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .hs-17__cta {
    transition: none;
  }
}
```
