---
source: "codefronts"
url: "https://codefronts.com/snippets/css-badges/risograph-edition-label/"
title: "Risograph Edition Label"
section: "snippets"
category: "css-badges"
category_name: "CSS Badges"
description: "Two-color riso print laid down by drum and squeegee. Pink and cyan with the deliberate misregistration that gives the process its hand. Hover widens the offset."
has_js: "false"
---

Here's a working CSS Badge from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Risograph Edition Label
Source: https://codefronts.com/snippets/css-badges/risograph-edition-label/

Two-color riso print laid down by drum and squeegee. Pink and cyan with the deliberate misregistration that gives the process its hand. Hover widens the offset.
## HTML
```html
<div class="bdg-23-stage">
  <div class="bdg-23-card">
    <div class="bdg-23-corner bdg-23-cy bdg-23-tl"></div>
    <div class="bdg-23-corner bdg-23-mg bdg-23-tl"></div>
    <div class="bdg-23-corner bdg-23-cy bdg-23-tr"></div>
    <div class="bdg-23-corner bdg-23-mg bdg-23-tr"></div>
    <div class="bdg-23-corner bdg-23-cy bdg-23-bl"></div>
    <div class="bdg-23-corner bdg-23-mg bdg-23-bl"></div>
    <div class="bdg-23-corner bdg-23-cy bdg-23-br"></div>
    <div class="bdg-23-corner bdg-23-mg bdg-23-br"></div>

    <div class="bdg-23-blob"></div>
    <div class="bdg-23-blob bdg-23-cyan"></div>

    <div class="bdg-23-content">
      <div class="bdg-23-eyebrow">
        <span class="bdg-23-pink">— SPECIAL EDITION —</span>
        <span class="bdg-23-cyan-text">— SPECIAL EDITION —</span>
      </div>
      <div class="bdg-23-title">
        <span class="bdg-23-pink">LIMITED</span>
        <span class="bdg-23-cyan-text">LIMITED</span>
      </div>
      <div class="bdg-23-title">
        <span class="bdg-23-pink">RUN '26</span>
        <span class="bdg-23-cyan-text">RUN '26</span>
      </div>

      <div class="bdg-23-divider"></div>

      <div class="bdg-23-number">042 / 250</div>
      <div class="bdg-23-detail">Two-color riso on Lessebo natural · 297 × 420 mm · signed by the artist</div>

      <div class="bdg-23-stamp">PROOF</div>

      <div class="bdg-23-meta-bottom">
        <span>STUDIO PRESS</span>
        <span>NORTH CAROLINA</span>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.bdg-23-stage {
  background: #d6cdb4;
  padding: 50px 40px;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  min-height: 100vh;
  position: relative;
}

.bdg-23-card {
  background: #efe8d2;
  width: 100%;
  max-width: 340px;
  aspect-ratio: 3 / 4.1;
  padding: 30px 28px 24px;
  position: relative;
  overflow: hidden;
  cursor: pointer;
  box-shadow: 0 18px 36px -14px rgba(40,30,10,0.4);
  font-family: "Space Mono", ui-monospace, monospace;
}

.bdg-23-corner {
  position: absolute;
  width: 10px;
  height: 10px;
  mix-blend-mode: multiply;
  z-index: 2;
}

.bdg-23-cy {
  background: #00b4d8;
}

.bdg-23-mg {
  background: #ff4d8d;
  transform: translate(2px, 2px);
}

.bdg-23-tl {
  top: 10px;
  left: 10px;
}

.bdg-23-tr {
  top: 10px;
  right: 10px;
}

.bdg-23-bl {
  bottom: 10px;
  left: 10px;
}

.bdg-23-br {
  bottom: 10px;
  right: 10px;
}

.bdg-23-blob {
  position: absolute;
  width: 260px;
  height: 260px;
  border-radius: 50%;
  background: #ff4d8d;
  mix-blend-mode: multiply;
  top: 45%;
  left: 50%;
  transform: translate(-50%, -50%);
  opacity: 0.7;
  z-index: 1;
  transition: transform 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}

.bdg-23-blob.bdg-23-cyan {
  background: #00b4d8;
  width: 200px;
  height: 200px;
  top: 60%;
  left: 38%;
  opacity: 0.55;
}

.bdg-23-card:hover .bdg-23-blob {
  transform: translate(-46%, -52%);
}

.bdg-23-card:hover .bdg-23-blob.bdg-23-cyan {
  transform: translate(-44%, -48%);
}

.bdg-23-content {
  position: relative;
  z-index: 2;
  height: 100%;
  display: flex;
  flex-direction: column;
}

.bdg-23-eyebrow {
  font-size: 10px;
  letter-spacing: 0.32em;
  text-align: center;
  margin-bottom: 10px;
  position: relative;
  line-height: 1;
  height: 12px;
}

.bdg-23-eyebrow .bdg-23-pink,
.bdg-23-eyebrow .bdg-23-cyan-text {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  mix-blend-mode: multiply;
}

.bdg-23-eyebrow .bdg-23-pink {
  color: #ff4d8d;
}

.bdg-23-eyebrow .bdg-23-cyan-text {
  color: #00b4d8;
  transform: translate(2px, -1px);
  transition: transform 0.4s;
}

.bdg-23-card:hover .bdg-23-eyebrow .bdg-23-cyan-text {
  transform: translate(5px, -2px);
}

.bdg-23-title {
  font-family: "Archivo Black", system-ui, sans-serif;
  font-size: 46px;
  line-height: 0.92;
  letter-spacing: -0.025em;
  text-align: center;
  position: relative;
  margin-bottom: 4px;
  height: 42px;
}

.bdg-23-title .bdg-23-pink,
.bdg-23-title .bdg-23-cyan-text {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  mix-blend-mode: multiply;
}

.bdg-23-title .bdg-23-pink {
  color: #ff4d8d;
}

.bdg-23-title .bdg-23-cyan-text {
  color: #00b4d8;
  transform: translate(3px, -1px);
  transition: transform 0.4s;
}

.bdg-23-card:hover .bdg-23-title .bdg-23-cyan-text {
  transform: translate(7px, -3px);
}

@media (prefers-reduced-motion: reduce) {
  .bdg-23-blob,
    .bdg-23-eyebrow .bdg-23-cyan-text,
    .bdg-23-title .bdg-23-cyan-text {
    transition: none;
  }
}

.bdg-23-divider {
  width: 100%;
  border-top: 1.5px dashed #ff4d8d;
  margin: 28px 0 16px;
  mix-blend-mode: multiply;
  position: relative;
  z-index: 2;
}

.bdg-23-number {
  font-size: 22px;
  font-weight: 700;
  text-align: center;
  color: #1a1a1a;
  margin-bottom: 10px;
  z-index: 2;
  position: relative;
}

.bdg-23-detail {
  font-size: 9px;
  line-height: 1.55;
  letter-spacing: 0.04em;
  text-align: center;
  color: #444;
  max-width: 220px;
  margin: 0 auto;
  z-index: 2;
  position: relative;
}

.bdg-23-stamp {
  position: absolute;
  bottom: 50px;
  right: 18px;
  font-family: "Archivo Black", system-ui, sans-serif;
  font-size: 18px;
  letter-spacing: 0.06em;
  transform: rotate(-10deg);
  z-index: 3;
  line-height: 1;
  border: 2px solid #ff4d8d;
  padding: 6px 10px;
  color: #ff4d8d;
  mix-blend-mode: multiply;
}

.bdg-23-meta-bottom {
  margin-top: auto;
  padding-top: 18px;
  border-top: 1px solid rgba(0,0,0,0.15);
  display: flex;
  justify-content: space-between;
  font-size: 8px;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: #555;
  position: relative;
  z-index: 2;
}
```
