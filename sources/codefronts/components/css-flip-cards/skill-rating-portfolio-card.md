---
source: "codefronts"
url: "https://codefronts.com/components/css-flip-cards/skill-rating-portfolio-card/"
title: "Skill Rating Portfolio Card"
section: "components"
category: "css-flip-cards"
category_name: "CSS Flip Cards"
description: "Front shows a project preview with tech tags; back displays a tech stack breakdown with animated skill bar meters."
has_js: "false"
---

Here's a working CSS Flip Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Skill Rating Portfolio Card
Source: https://codefronts.com/components/css-flip-cards/skill-rating-portfolio-card/

Front shows a project preview with tech tags; back displays a tech stack breakdown with animated skill bar meters.
## HTML
```html
<div class="fc-05">
  <div class="fc-05__scene">
    <div class="fc-05__card">
      <div class="fc-05__front">
        <div class="fc-05__preview-img">
          <div class="fc-05__preview-grid">
            <div class="fc-05__pg"></div>
            <div class="fc-05__pg"></div>
            <div class="fc-05__pg"></div>
          </div>
        </div>
        <div class="fc-05__project-info">
          <div class="fc-05__proj-cat">Case Study · 2025</div>
          <div class="fc-05__proj-name">Orbit Dashboard</div>
          <div class="fc-05__proj-desc">A real-time analytics platform with customisable widget grids and live WebSocket feeds.</div>
          <div class="fc-05__tags">
            <span class="fc-05__tag">React</span>
            <span class="fc-05__tag">TypeScript</span>
            <span class="fc-05__tag">D3.js</span>
          </div>
        </div>
        <div class="fc-05__front-hint">Hover to see tech stack →</div>
      </div>
      <div class="fc-05__back">
        <div class="fc-05__back-title">Tech Stack & Proficiency</div>
        <div class="fc-05__skills">
          <div class="fc-05__skill-item"><div class="fc-05__skill-row"><span class="fc-05__skill-name">React / Next.js</span><span class="fc-05__skill-pct">96%</span></div><div class="fc-05__skill-track"><div class="fc-05__skill-bar" style="width:96%"></div></div></div>
          <div class="fc-05__skill-item"><div class="fc-05__skill-row"><span class="fc-05__skill-name">TypeScript</span><span class="fc-05__skill-pct">92%</span></div><div class="fc-05__skill-track"><div class="fc-05__skill-bar" style="width:92%"></div></div></div>
          <div class="fc-05__skill-item"><div class="fc-05__skill-row"><span class="fc-05__skill-name">D3.js / Recharts</span><span class="fc-05__skill-pct">85%</span></div><div class="fc-05__skill-track"><div class="fc-05__skill-bar" style="width:85%"></div></div></div>
          <div class="fc-05__skill-item"><div class="fc-05__skill-row"><span class="fc-05__skill-name">Node / WebSocket</span><span class="fc-05__skill-pct">88%</span></div><div class="fc-05__skill-track"><div class="fc-05__skill-bar" style="width:88%"></div></div></div>
          <div class="fc-05__skill-item"><div class="fc-05__skill-row"><span class="fc-05__skill-name">PostgreSQL</span><span class="fc-05__skill-pct">78%</span></div><div class="fc-05__skill-track"><div class="fc-05__skill-bar" style="width:78%"></div></div></div>
        </div>
        <div class="fc-05__stack-icons">
          <div class="fc-05__si">⚛</div>
          <div class="fc-05__si">🟦</div>
          <div class="fc-05__si">📊</div>
          <div class="fc-05__si">🟢</div>
          <div class="fc-05__si">🐘</div>
        </div>
        <button class="fc-05__view-btn">View Live Project →</button>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.fc-05,
.fc-05 *,
.fc-05 *::before,
.fc-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fc-05 ::selection {
  background: #f97316;
  color: #fff;
}

.fc-05 {
  --bg: #0a0a0a;
  --orange: #f97316;
  --amber: #fbbf24;
  --white: #fef3e2;
  --card-w: 340px;
  --card-h: 440px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: radial-gradient(ellipse at 40% 60%,#1a0a00,#0a0a0a 65%);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  color: var(--white);
}

.fc-05__scene {
  width: var(--card-w);
  height: var(--card-h);
  perspective: 1200px;
  cursor: pointer;
}

.fc-05__card {
  width: 100%;
  height: 100%;
  position: relative;
  transform-style: preserve-3d;
  transition: transform .7s cubic-bezier(.4,0,.2,1);
}

.fc-05__scene:hover .fc-05__card {
  transform: rotateY(180deg);
}

.fc-05__front,
.fc-05__back {
  position: absolute;
  inset: 0;
  border-radius: 20px;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  overflow: hidden;
}
/* FRONT — project preview */

.fc-05__front {
  background: #111;
  border: 1px solid rgba(249,115,22,.2);
  display: flex;
  flex-direction: column;
}

.fc-05__preview-img {
  height: 200px;
  background: linear-gradient(135deg,#1c0a00,#0d1a2e);
  position: relative;
  overflow: hidden;
  flex-shrink: 0;
}

.fc-05__preview-img::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at 30% 40%,rgba(249,115,22,.2),transparent 60%);
}

.fc-05__preview-grid {
  position: absolute;
  inset: 20px;
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: 1fr 1fr;
  gap: 8px;
}

.fc-05__pg {
  border-radius: 8px;
  background: rgba(255,255,255,.04);
  border: 1px solid rgba(255,255,255,.07);
}

.fc-05__pg:nth-child(1) {
  grid-column: 1/3;
  background: linear-gradient(135deg,rgba(249,115,22,.12),rgba(251,191,36,.06));
}

.fc-05__project-info {
  padding: 20px 22px;
}

.fc-05__proj-cat {
  font-size: 10px;
  letter-spacing: .15em;
  text-transform: uppercase;
  color: var(--orange);
  font-weight: 700;
  margin-bottom: 6px;
}

.fc-05__proj-name {
  font-size: 20px;
  font-weight: 800;
  color: var(--white);
}

.fc-05__proj-desc {
  font-size: 12px;
  color: rgba(254,243,226,.5);
  margin-top: 6px;
  line-height: 1.6;
}

.fc-05__tags {
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
  margin-top: 12px;
}

.fc-05__tag {
  font-size: 10px;
  padding: 3px 9px;
  border-radius: 20px;
  background: rgba(249,115,22,.1);
  border: 1px solid rgba(249,115,22,.2);
  color: rgba(254,243,226,.7);
  letter-spacing: .06em;
}

.fc-05__front-hint {
  padding: 0 22px 16px;
  font-size: 10px;
  color: rgba(254,243,226,.25);
  letter-spacing: .08em;
}
/* BACK — tech stack + skill bars */

.fc-05__back {
  background: linear-gradient(160deg,#111,#1a1008);
  border: 1px solid rgba(251,191,36,.2);
  transform: rotateY(180deg);
  display: flex;
  flex-direction: column;
  padding: 28px;
  gap: 14px;
}

.fc-05__back-title {
  font-size: 11px;
  letter-spacing: .15em;
  text-transform: uppercase;
  color: var(--amber);
  font-weight: 700;
}

.fc-05__skills {
  display: flex;
  flex-direction: column;
  gap: 12px;
  flex: 1;
}

.fc-05__skill-item {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.fc-05__skill-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.fc-05__skill-name {
  font-size: 12px;
  font-weight: 600;
  color: rgba(254,243,226,.8);
}

.fc-05__skill-pct {
  font-size: 11px;
  font-weight: 700;
  color: var(--orange);
}

.fc-05__skill-track {
  height: 5px;
  background: rgba(255,255,255,.08);
  border-radius: 3px;
  overflow: hidden;
}

.fc-05__skill-bar {
  height: 100%;
  border-radius: 3px;
  background: linear-gradient(90deg,var(--orange),var(--amber));
  transition: width .6s ease;
}

.fc-05__stack-icons {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  margin-top: 4px;
}

.fc-05__si {
  width: 36px;
  height: 36px;
  border-radius: 8px;
  background: rgba(255,255,255,.05);
  border: 1px solid rgba(255,255,255,.08);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
}

.fc-05__view-btn {
  margin-top: auto;
  width: 100%;
  padding: 12px;
  background: linear-gradient(135deg,var(--orange),var(--amber));
  color: #000;
  font-size: 13px;
  font-weight: 800;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  letter-spacing: .04em;
}

@media (prefers-reduced-motion: reduce) {
  .fc-05__card {
    transition: none;
  }
}
```
