---
source: "codefronts"
url: "https://codefronts.com/components/css-flip-cards/photo-gallery-overlay-card/"
title: "Photo Gallery Overlay Card"
section: "components"
category: "css-flip-cards"
category_name: "CSS Flip Cards"
description: "Front displays a full-bleed SVG aurora landscape scene; back reveals location metadata, camera EXIF settings, content tags, and a download CTA."
has_js: "false"
---

Here's a working CSS Flip Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Photo Gallery Overlay Card
Source: https://codefronts.com/components/css-flip-cards/photo-gallery-overlay-card/

Front displays a full-bleed SVG aurora landscape scene; back reveals location metadata, camera EXIF settings, content tags, and a download CTA.
## HTML
```html
<div class="fc-09">
  <div class="fc-09__scene">
    <div class="fc-09__card">
      <div class="fc-09__front">
        <div class="fc-09__photo">
          <svg viewBox="0 0 340 380" preserveAspectRatio="xMidYMid slice" fill="none">
            <!-- sky gradient -->
            <defs>
              <linearGradient id="sky9" x1="0" y1="0" x2="0" y2="1" gradientUnits="objectBoundingBox">
                <stop stop-color="#041830"/>
                <stop offset=".5" stop-color="#0a2a4a"/>
                <stop offset="1" stop-color="#0d3a5c"/>
              </linearGradient>
              <linearGradient id="water9" x1="0" y1="0" x2="0" y2="1" gradientUnits="objectBoundingBox">
                <stop stop-color="#062035"/>
                <stop offset="1" stop-color="#020d18"/>
              </linearGradient>
            </defs>
            <rect width="340" height="380" fill="url(#sky9)"/>
            <!-- stars -->
            <circle cx="30" cy="30" r="1.5" fill="white" opacity=".8"/>
            <circle cx="80" cy="15" r="1" fill="white" opacity=".6"/>
            <circle cx="150" cy="25" r="1.5" fill="white" opacity=".9"/>
            <circle cx="220" cy="10" r="1" fill="white" opacity=".7"/>
            <circle cx="290" cy="35" r="1.5" fill="white" opacity=".8"/>
            <circle cx="310" cy="15" r="1" fill="white" opacity=".5"/>
            <circle cx="60" cy="60" r="1" fill="white" opacity=".6"/>
            <circle cx="260" cy="60" r="1.5" fill="white" opacity=".7"/>
            <!-- aurora band -->
            <ellipse cx="170" cy="80" rx="200" ry="40" fill="rgba(20,184,166,.15)"/>
            <ellipse cx="170" cy="90" rx="160" ry="25" fill="rgba(14,165,233,.1)"/>
            <!-- mountains far -->
            <path d="M0 220 L60 140 L120 200 L180 130 L240 190 L300 140 L340 180 L340 280 L0 280Z" fill="rgba(12,36,64,.7)"/>
            <!-- mountains near -->
            <path d="M0 260 L80 180 L140 230 L200 170 L260 220 L340 175 L340 280 L0 280Z" fill="rgba(8,24,48,.9)"/>
            <!-- water reflection -->
            <rect x="0" y="280" width="340" height="100" fill="url(#water9)"/>
            <!-- reflection lines -->
            <line x1="50" y1="300" x2="290" y2="300" stroke="rgba(14,165,233,.08)" stroke-width="8"/>
            <line x1="30" y1="320" x2="310" y2="320" stroke="rgba(14,165,233,.05)" stroke-width="12"/>
            <!-- aurora reflection in water -->
            <ellipse cx="170" cy="330" rx="180" ry="20" fill="rgba(20,184,166,.08)"/>
            <!-- moon -->
            <circle cx="260" cy="55" r="20" fill="rgba(240,249,255,.9)"/>
            <circle cx="268" cy="48" r="16" fill="rgba(10,28,48,.95)"/>
          </svg>
          <div class="fc-09__photo-meta">
            <div class="fc-09__cam-icon">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/></svg>
              f/2.8 · 25s · ISO 3200
            </div>
            <div class="fc-09__photo-title">Aurora at Jökulsárlón</div>
          </div>
        </div>
        <div class="fc-09__front-hint">Hover for details & download →</div>
      </div>
      <div class="fc-09__back">
        <div class="fc-09__back-img-thumb">
          <svg viewBox="0 0 340 120" preserveAspectRatio="xMidYMid slice" fill="none">
            <rect width="340" height="120" fill="#041830"/>
            <path d="M0 80 L80 50 L140 70 L200 40 L260 65 L340 45 L340 120 L0 120Z" fill="rgba(12,36,64,.9)"/>
            <ellipse cx="170" cy="30" rx="160" ry="18" fill="rgba(20,184,166,.2)"/>
            <rect x="0" y="90" width="340" height="30" fill="rgba(6,18,30,.9)"/>
          </svg>
        </div>
        <div class="fc-09__detail-grid">
          <div class="fc-09__detail"><div class="fc-09__detail-lbl">Location</div><div class="fc-09__detail-val">Iceland</div></div>
          <div class="fc-09__detail"><div class="fc-09__detail-lbl">Date Captured</div><div class="fc-09__detail-val">Nov 12, 2024</div></div>
          <div class="fc-09__detail"><div class="fc-09__detail-lbl">Camera</div><div class="fc-09__detail-val">Sony A7R V</div></div>
          <div class="fc-09__detail"><div class="fc-09__detail-lbl">Resolution</div><div class="fc-09__detail-val">61 MP RAW</div></div>
        </div>
        <div class="fc-09__tags-row">
          <span class="fc-09__photo-tag">Aurora</span>
          <span class="fc-09__photo-tag">Landscape</span>
          <span class="fc-09__photo-tag">Night Sky</span>
        </div>
        <button class="fc-09__download">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
          Download Full Resolution
        </button>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.fc-09,
.fc-09 *,
.fc-09 *::before,
.fc-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fc-09 ::selection {
  background: #0ea5e9;
  color: #fff;
}

.fc-09 {
  --bg: #080c10;
  --sky: #0ea5e9;
  --teal: #14b8a6;
  --white: #f0f9ff;
  --card-w: 340px;
  --card-h: 440px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: radial-gradient(ellipse at 50% 0%,#061020,#080c10 65%);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  color: var(--white);
}

.fc-09__scene {
  width: var(--card-w);
  height: var(--card-h);
  perspective: 1200px;
  cursor: pointer;
}

.fc-09__card {
  width: 100%;
  height: 100%;
  position: relative;
  transform-style: preserve-3d;
  transform-origin: center top;
  transition: transform .85s cubic-bezier(.4,0,.2,1);
}
/* See note on translateY counter — same as fc-02 (flip-up) but inverted:
   rotating around top edge would push the card UP by its full height; the
   translateY(100%) at the end keeps the visual position fixed. */
/* Fold-out from the TOP edge — the card unfolds downward like peeling
   back a Polaroid, instead of spinning around centre. Preserves the
   photo's visual focus during the transition. */

.fc-09__scene:hover .fc-09__card {
  transform: translateY(100%) rotateX(-180deg);
}

.fc-09__front,
.fc-09__back {
  position: absolute;
  inset: 0;
  border-radius: 20px;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  overflow: hidden;
}
/* FRONT — full-bleed photo */

.fc-09__front {
  display: flex;
  flex-direction: column;
  border: 1px solid rgba(14,165,233,.2);
}

.fc-09__photo {
  flex: 1;
  position: relative;
  overflow: hidden;
  background: linear-gradient(160deg,#0c2340,#041520,#0d2a2a);
}
/* SVG landscape scene */

.fc-09__photo svg {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
}

.fc-09__photo-meta {
  position: absolute;
  bottom: 0;
  inset-x: 0;
  padding: 20px;
  background: linear-gradient(to top,rgba(8,12,16,.9),transparent);
}

.fc-09__cam-icon {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 10px;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: rgba(240,249,255,.5);
}

.fc-09__photo-title {
  font-size: 20px;
  font-weight: 800;
  color: var(--white);
  margin-top: 4px;
}

.fc-09__front-hint {
  padding: 14px;
  text-align: center;
  background: rgba(0,0,0,.4);
  font-size: 10px;
  color: rgba(240,249,255,.3);
  letter-spacing: .08em;
}
/* BACK */

.fc-09__back {
  background: linear-gradient(160deg,#0a1520,#060e18);
  border: 1px solid rgba(20,184,166,.25);
  /* Pre-rotated on X so the top-hinge fold-out brings it forward. */
  transform: rotateX(180deg);
  display: flex;
  flex-direction: column;
  padding: 28px;
  gap: 16px;
}

.fc-09__back-img-thumb {
  height: 120px;
  border-radius: 12px;
  overflow: hidden;
  background: linear-gradient(160deg,#0c2340,#041520,#0d2a2a);
  position: relative;
  flex-shrink: 0;
}

.fc-09__back-img-thumb svg {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
}

.fc-09__detail-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
}

.fc-09__detail {
  background: rgba(255,255,255,.04);
  border: 1px solid rgba(255,255,255,.07);
  border-radius: 10px;
  padding: 10px 12px;
}

.fc-09__detail-lbl {
  font-size: 9px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: rgba(240,249,255,.35);
  margin-bottom: 3px;
}

.fc-09__detail-val {
  font-size: 13px;
  font-weight: 600;
  color: var(--white);
}

.fc-09__tags-row {
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
}

.fc-09__photo-tag {
  font-size: 10px;
  padding: 3px 10px;
  border-radius: 20px;
  background: rgba(14,165,233,.1);
  border: 1px solid rgba(14,165,233,.2);
  color: var(--sky);
}

.fc-09__download {
  margin-top: auto;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 13px;
  border-radius: 12px;
  background: linear-gradient(135deg,var(--sky),var(--teal));
  color: #000;
  font-size: 13px;
  font-weight: 800;
  cursor: pointer;
  border: none;
  letter-spacing: .04em;
}

@media (prefers-reduced-motion: reduce) {
  .fc-09__card {
    transition: none;
  }
}
```
