---
source: "codefronts"
url: "https://codefronts.com/layouts/css-split-screen/diagonal-split/"
title: "Diagonal Split"
section: "layouts"
category: "css-split-screen"
category_name: "CSS Split Screen Layouts"
description: "Sport magazine — pitch black with electric-orange diagonal cut and concrete-grey supporting tones."
has_js: "false"
---

Here's a working CSS Split Screen Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Diagonal Split
Source: https://codefronts.com/layouts/css-split-screen/diagonal-split/

Sport magazine — pitch black with electric-orange diagonal cut and concrete-grey supporting tones. Headline punches through the diagonal seam. Pure CSS via clip-path: polygon() for the angled wedge; oversized condensed display type sells the impact.
## HTML
```html
<section class="ss-dia" aria-label="Sport magazine cover">
  <div class="ss-dia-orange" aria-hidden="true">
    <span class="ss-dia-num">47</span>
  </div>
  <div class="ss-dia-black">
    <span class="ss-dia-issue">ISSUE 47 · MAY</span>
    <h2>FASTER<br /><span class="ss-dia-italic">than</span><br />YESTERDAY.</h2>
    <p>Inside: how four runners broke their personal records by changing one thing.</p>
    <ul class="ss-dia-list">
      <li><span>01</span> The 6am rule</li>
      <li><span>02</span> Negative splits</li>
      <li><span>03</span> Track over road</li>
    </ul>
    <button type="button" class="ss-dia-cta">Read inside →</button>
  </div>
</section>
```
## CSS
```css
.ss-dia {
  width: 100%;
  position: relative;
  min-height: 100vh;
  font-family: 'Inter', system-ui, sans-serif;
  background: #0e0e10;
  color: #fff;
  border-radius: 0;
  overflow: hidden;
  isolation: isolate;
}

.ss-dia-orange {
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, #ff5e1a 0%, #ff8a00 60%, #ffaa44 100%);
  /* Wedge narrows toward the bottom; top-edge width matches where the
       black panel starts (44%) so the two regions never overlap. */
  clip-path: polygon(0 0, 44% 0, 24% 100%, 0 100%);
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}

.ss-dia-orange::before {
  content: '';
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(60deg, transparent 0 30px, rgba(0,0,0,0.04) 30px 31px);
}

.ss-dia-num {
  font-family: 'Helvetica Neue', sans-serif;
  font-weight: 900;
  /* Cap at 18vw of the WEDGE'S own width (~44vw) so the numeral fits
       inside the orange region on wide viewports and doesn't spike past
       the diagonal seam. */
  font-size: clamp(120px, 22vw, 200px);
  line-height: 0.85;
  color: #0e0e10;
  letter-spacing: -0.05em;
  /* Nudge left so numeral sits centered inside the tapering wedge
       instead of poking into the diagonal seam. */
  transform: translateX(-18%) translateY(6%);
  text-shadow: 0 6px 0 rgba(0,0,0,0.06);
  font-style: italic;
}

.ss-dia-black {
  position: absolute;
  right: 0;
  top: 0;
  bottom: 0;
  /* Panel starts where the orange wedge ends at the top edge (44%)
       so headline typography never overlaps with the wedge. */
  left: 44%;
  padding: 48px 44px;
  display: flex;
  flex-direction: column;
  gap: 18px;
  z-index: 2;
}

.ss-dia-issue {
  font-family: 'Courier New', monospace;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.3em;
  color: #ff8a00;
}

.ss-dia-black h2 {
  margin: 0;
  font-family: 'Helvetica Neue', sans-serif;
  font-size: clamp(40px, 6.5vw, 84px);
  font-weight: 900;
  line-height: 0.9;
  color: #fff;
  letter-spacing: -0.03em;
  text-transform: uppercase;
}

.ss-dia-italic {
  font-style: italic;
  font-weight: 300;
  color: #ff8a00;
  text-transform: lowercase;
  font-family: 'Cormorant Garamond', serif;
}

.ss-dia-black p {
  margin: 0;
  font-size: 15px;
  line-height: 1.55;
  color: #b8b6b0;
  max-width: 380px;
}

.ss-dia-list {
  list-style: none;
  margin: 6px 0 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.ss-dia-list li {
  display: flex;
  align-items: baseline;
  gap: 14px;
  font-family: 'Inter', sans-serif;
  font-size: 15px;
  color: #fff;
  padding: 10px 0;
  border-top: 1px solid rgba(255,255,255,0.1);
}

.ss-dia-list span {
  font-family: 'Courier New', monospace;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.16em;
  color: #ff8a00;
}

.ss-dia-cta {
  margin-top: auto;
  align-self: flex-start;
  padding: 14px 26px;
  background: #ff5e1a;
  color: #0e0e10;
  border: 0;
  font-family: 'Inter', sans-serif;
  font-size: 13px;
  font-weight: 800;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  cursor: pointer;
  transition: background 0.16s, transform 0.12s;
}

.ss-dia-cta:hover {
  background: #ff8a00;
}

.ss-dia-cta:active {
  transform: translateY(1px);
}

@media (max-width: 720px) {
  .ss-dia {
    min-height: 580px;
  }

  .ss-dia-orange {
    clip-path: polygon(0 0, 100% 0, 100% 38%, 0 50%);
  }

  .ss-dia-num {
    transform: translateX(0) translateY(-10%);
    font-size: 120px;
  }

  .ss-dia-black {
    width: 100%;
    top: 50%;
    padding-top: 36px;
  }
}
```
