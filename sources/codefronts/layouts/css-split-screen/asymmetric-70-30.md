---
source: "codefronts"
url: "https://codefronts.com/layouts/css-split-screen/asymmetric-70-30/"
title: "Asymmetric 70/30"
section: "layouts"
category: "css-split-screen"
category_name: "CSS Split Screen Layouts"
description: "Architecture portfolio — warm grey concrete + ivory + black accents."
has_js: "false"
---

Here's a working CSS Split Screen Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Asymmetric 70/30
Source: https://codefronts.com/layouts/css-split-screen/asymmetric-70-30/

Architecture portfolio — warm grey concrete + ivory + black accents. Asymmetric 70/30 split: a single hero project on the left, oversized index numbers on the right. Print-magazine spread vibe; thin hairlines do all the structuring.
## HTML
```html
<section class="ss-arc" aria-label="Architecture project showcase">
  <article class="ss-arc-hero">
    <header>
      <span class="ss-arc-eye">PROJECT NO. 014 · 2026</span>
      <h2>Casa<br />Hormigón</h2>
      <p>
        A 220 m² family house in Valle de Bravo. Cast-in-place concrete walls, exposed timber roof,
        single oculus skylight above the central courtyard.
      </p>
    </header>
    <div class="ss-arc-photo" aria-hidden="true">
      <span class="ss-arc-bldg"></span>
      <span class="ss-arc-shadow"></span>
    </div>
    <footer class="ss-arc-meta">
      <span><em>Location</em><b>Valle de Bravo, MX</b></span>
      <span><em>Year</em><b>2026</b></span>
      <span><em>Area</em><b>220 m²</b></span>
      <span><em>Status</em><b>Completed</b></span>
    </footer>
  </article>
  <aside class="ss-arc-index">
    <span class="ss-arc-folio">FOLIO</span>
    <ol>
      <li class="active"><span>014</span>Casa Hormigón</li>
      <li><span>013</span>Library Pavilion</li>
      <li><span>012</span>Bridge House</li>
      <li><span>011</span>Sea Cabin</li>
      <li><span>010</span>Garden Atelier</li>
    </ol>
    <footer>est. 2008</footer>
  </aside>
</section>
```
## CSS
```css
.ss-arc {
  width: 100%;
  display: grid;
  grid-template-columns: 70% 30%;
  min-height: 100vh;
  font-family: 'Inter', system-ui, sans-serif;
  background: #f0ece4;
  color: #1a1a1a;
  border-radius: 0;
  overflow: hidden;
}

.ss-arc-hero {
  padding: 44px 48px;
  display: grid;
  grid-template-rows: auto 1fr auto;
  gap: 28px;
  position: relative;
}

.ss-arc-eye {
  font-family: 'Courier New', monospace;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.24em;
  color: #6a6a6a;
}

.ss-arc-hero header h2 {
  margin: 6px 0 12px;
  font-family: 'Cormorant Garamond', serif;
  font-size: clamp(40px, 6vw, 76px);
  font-weight: 500;
  line-height: 0.92;
  color: #1a1a1a;
  letter-spacing: -0.03em;
  font-style: italic;
}

.ss-arc-hero header p {
  margin: 0;
  font-size: 15px;
  line-height: 1.65;
  color: #4a4a4a;
  max-width: 420px;
}

.ss-arc-photo {
  position: relative;
  background: linear-gradient(180deg, #d4cfc1 0%, #b8b3a4 100%);
  border: 1px solid #1a1a1a;
  display: flex;
  align-items: flex-end;
  justify-content: center;
  overflow: hidden;
  min-height: 180px;
}

.ss-arc-bldg {
  width: 60%;
  height: 70%;
  background: linear-gradient(180deg, #5a5a5a 0%, #2a2a2a 100%);
  position: relative;
}

.ss-arc-bldg::before {
  content: '';
  position: absolute;
  top: 12%;
  left: 35%;
  right: 35%;
  height: 14%;
  background: #f5d68a;
  box-shadow: 0 0 0 1px #1a1a1a, 0 0 18px rgba(245,214,138,0.5);
}

.ss-arc-bldg::after {
  content: '';
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  height: 30%;
  background: repeating-linear-gradient(90deg, transparent 0 14%, rgba(255,255,255,0.08) 14% 16%);
}

.ss-arc-shadow {
  position: absolute;
  left: 5%;
  right: 5%;
  bottom: 0;
  height: 16px;
  background: rgba(0,0,0,0.4);
  filter: blur(8px);
}

.ss-arc-meta {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 18px;
  padding-top: 18px;
  border-top: 1px solid #1a1a1a;
}

.ss-arc-meta span {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.ss-arc-meta em {
  font-family: 'Courier New', monospace;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.18em;
  color: #6a6a6a;
  font-style: normal;
}

.ss-arc-meta b {
  font-family: 'Cormorant Garamond', serif;
  font-size: 16px;
  font-weight: 500;
  color: #1a1a1a;
  font-style: italic;
}

.ss-arc-index {
  background: #1a1a1a;
  color: #f0ece4;
  padding: 36px 28px;
  display: flex;
  flex-direction: column;
  gap: 18px;
  font-family: 'Cormorant Garamond', serif;
}

.ss-arc-folio {
  font-family: 'Courier New', monospace;
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: 0.32em;
  color: #6a6a6a;
}

.ss-arc-index ol {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
}

.ss-arc-index li {
  padding: 14px 0;
  font-size: 17px;
  font-style: italic;
  color: #8a8a8a;
  border-bottom: 1px solid rgba(255,255,255,0.1);
  display: grid;
  grid-template-columns: 50px 1fr;
  align-items: baseline;
  cursor: pointer;
  transition: color 0.16s;
}

.ss-arc-index li:hover {
  color: #f0ece4;
}

.ss-arc-index li span {
  font-family: 'Courier New', monospace;
  font-size: 11px;
  font-style: normal;
  color: #6a6a6a;
  letter-spacing: 0.16em;
}

.ss-arc-index li.active {
  color: #f0ece4;
  font-weight: 500;
}

.ss-arc-index li.active span {
  color: #f5d68a;
}

.ss-arc-index footer {
  margin-top: auto;
  font-family: 'Courier New', monospace;
  font-size: 10.5px;
  letter-spacing: 0.24em;
  color: #6a6a6a;
}

@media (max-width: 720px) {
  .ss-arc {
    grid-template-columns: 1fr;
  }

  .ss-arc-meta {
    grid-template-columns: 1fr 1fr;
  }
}
```
