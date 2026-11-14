---
source: "codefronts"
url: "https://codefronts.com/components/css-flip-cards/video-playlist-thumbnail-card/"
title: "Video Playlist Thumbnail Card"
section: "components"
category: "css-flip-cards"
category_name: "CSS Flip Cards"
description: "Front shows a SVG video poster with play overlay and runtime badge; back reveals description, view stats, a mini playlist, and a Watch Now CTA."
has_js: "false"
---

Here's a working CSS Flip Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Video Playlist Thumbnail Card
Source: https://codefronts.com/components/css-flip-cards/video-playlist-thumbnail-card/

Front shows a SVG video poster with play overlay and runtime badge; back reveals description, view stats, a mini playlist, and a Watch Now CTA.
## HTML
```html
<div class="fc-10">
  <div class="fc-10__scene">
    <div class="fc-10__card">
      <div class="fc-10__front">
        <div class="fc-10__thumb">
          <svg viewBox="0 0 360 210" preserveAspectRatio="xMidYMid slice" fill="none">
            <defs>
              <linearGradient id="code10" x1="0" y1="0" x2="0" y2="1" gradientUnits="objectBoundingBox">
                <stop stop-color="#0d1117"/>
                <stop offset="1" stop-color="#161b22"/>
              </linearGradient>
            </defs>
            <rect width="360" height="210" fill="url(#code10)"/>
            <!-- code editor lines -->
            <rect x="20" y="20" width="320" height="8" rx="4" fill="rgba(239,68,68,.5)"/>
            <rect x="20" y="36" width="240" height="6" rx="3" fill="rgba(249,115,22,.4)"/>
            <rect x="40" y="52" width="200" height="6" rx="3" fill="rgba(139,92,246,.4)"/>
            <rect x="40" y="68" width="280" height="6" rx="3" fill="rgba(34,197,94,.3)"/>
            <rect x="60" y="84" width="160" height="6" rx="3" fill="rgba(14,165,233,.4)"/>
            <rect x="60" y="100" width="220" height="6" rx="3" fill="rgba(251,191,36,.3)"/>
            <rect x="40" y="116" width="180" height="6" rx="3" fill="rgba(139,92,246,.3)"/>
            <rect x="20" y="132" width="260" height="6" rx="3" fill="rgba(249,115,22,.4)"/>
            <rect x="20" y="148" width="120" height="6" rx="3" fill="rgba(239,68,68,.5)"/>
            <!-- glow overlay -->
            <rect width="360" height="210" fill="rgba(0,0,0,.35)"/>
          </svg>
          <div class="fc-10__play-overlay">
            <div class="fc-10__play-btn">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="white"><polygon points="5 3 19 12 5 21 5 3"/></svg>
            </div>
          </div>
          <div class="fc-10__duration">18:42</div>
        </div>
        <div class="fc-10__channel-row">
          <div class="fc-10__channel-avatar">CF</div>
          <div>
            <div class="fc-10__channel-name">CodeFronts</div>
            <div class="fc-10__channel-subs">248K subscribers</div>
          </div>
        </div>
        <div class="fc-10__video-title">Build a Full-Stack Auth System in 18 Minutes</div>
        <div class="fc-10__meta-row">
          <span class="fc-10__views">1.4M views</span>
          <span class="fc-10__dot-sep"></span>
          <span class="fc-10__date">3 months ago</span>
        </div>
        <div class="fc-10__front-hint">Hover for description →</div>
      </div>
      <div class="fc-10__back">
        <div class="fc-10__back-label">About this Video</div>
        <div class="fc-10__desc">In 18 minutes you'll build a production-ready JWT auth system with refresh tokens, protected routes, and Postgres storage — fully from scratch, zero magic libraries.</div>
        <div class="fc-10__stats-row">
          <div class="fc-10__stat"><div class="fc-10__stat-n">1.4M</div><div class="fc-10__stat-l">Views</div></div>
          <div class="fc-10__stat"><div class="fc-10__stat-n">98K</div><div class="fc-10__stat-l">Likes</div></div>
          <div class="fc-10__stat"><div class="fc-10__stat-n">18:42</div><div class="fc-10__stat-l">Runtime</div></div>
        </div>
        <div class="fc-10__playlist">
          <div class="fc-10__pl-item"><span class="fc-10__pl-num">1</span><span class="fc-10__pl-name">Project setup & JWT basics</span><span class="fc-10__pl-dur">4:12</span></div>
          <div class="fc-10__pl-item"><span class="fc-10__pl-num">2</span><span class="fc-10__pl-name">Refresh token strategy</span><span class="fc-10__pl-dur">6:30</span></div>
          <div class="fc-10__pl-item"><span class="fc-10__pl-num">3</span><span class="fc-10__pl-name">Protected routes & middleware</span><span class="fc-10__pl-dur">8:00</span></div>
        </div>
        <button class="fc-10__watch-btn">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="white"><polygon points="5 3 19 12 5 21 5 3"/></svg>
          Watch Now
        </button>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.fc-10,
.fc-10 *,
.fc-10 *::before,
.fc-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fc-10 ::selection {
  background: #dc2626;
  color: #fff;
}

.fc-10 {
  --bg: #0c0800;
  --red: #ef4444;
  --orange: #f97316;
  --white: #fff7ed;
  --card-w: 360px;
  --card-h: 420px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #0c0800;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  color: var(--white);
}

.fc-10__scene {
  width: var(--card-w);
  height: var(--card-h);
  perspective: 1200px;
  cursor: pointer;
}

.fc-10__card {
  width: 100%;
  height: 100%;
  position: relative;
  transform-style: preserve-3d;
  transition: transform .75s cubic-bezier(.4,0,.2,1);
}

.fc-10__scene:hover .fc-10__card {
  transform: rotateY(180deg);
}

.fc-10__front,
.fc-10__back {
  position: absolute;
  inset: 0;
  border-radius: 16px;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  overflow: hidden;
}
/* FRONT */

.fc-10__front {
  background: #111;
  border: 1px solid rgba(239,68,68,.2);
  display: flex;
  flex-direction: column;
}

.fc-10__thumb {
  height: 210px;
  background: linear-gradient(160deg,#1a0800,#0d0d0d,#0d1a2e);
  position: relative;
  overflow: hidden;
  flex-shrink: 0;
}

.fc-10__thumb svg {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
}

.fc-10__play-overlay {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(0,0,0,.3);
}

.fc-10__play-btn {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  background: rgba(239,68,68,.9);
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 0 30px rgba(239,68,68,.5);
}

.fc-10__duration {
  position: absolute;
  bottom: 10px;
  right: 10px;
  background: rgba(0,0,0,.8);
  color: var(--white);
  font-size: 11px;
  font-weight: 700;
  padding: 2px 6px;
  border-radius: 4px;
}

.fc-10__channel-row {
  padding: 16px 18px 8px;
  display: flex;
  align-items: center;
  gap: 10px;
}

.fc-10__channel-avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: linear-gradient(135deg,var(--red),var(--orange));
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 13px;
  font-weight: 800;
  color: #fff;
  flex-shrink: 0;
}

.fc-10__channel-name {
  font-size: 12px;
  font-weight: 700;
  color: rgba(255,247,237,.7);
}

.fc-10__channel-subs {
  font-size: 10px;
  color: rgba(255,247,237,.35);
}

.fc-10__video-title {
  padding: 0 18px;
  font-size: 16px;
  font-weight: 800;
  color: var(--white);
  line-height: 1.4;
}

.fc-10__meta-row {
  padding: 10px 18px;
  display: flex;
  gap: 12px;
  align-items: center;
}

.fc-10__views {
  font-size: 11px;
  color: rgba(255,247,237,.4);
}

.fc-10__dot-sep {
  width: 3px;
  height: 3px;
  border-radius: 50%;
  background: rgba(255,247,237,.3);
}

.fc-10__date {
  font-size: 11px;
  color: rgba(255,247,237,.4);
}

.fc-10__front-hint {
  margin-top: auto;
  padding: 14px 18px;
  font-size: 10px;
  color: rgba(255,247,237,.2);
  letter-spacing: .08em;
  border-top: 1px solid rgba(255,255,255,.05);
}
/* BACK */

.fc-10__back {
  background: linear-gradient(160deg,#1a0400,#0e0e0e);
  border: 1px solid rgba(249,115,22,.2);
  transform: rotateY(180deg);
  display: flex;
  flex-direction: column;
  padding: 24px;
  gap: 14px;
}

.fc-10__back-label {
  font-size: 10px;
  letter-spacing: .15em;
  text-transform: uppercase;
  color: var(--orange);
  font-weight: 700;
}

.fc-10__desc {
  font-size: 13px;
  color: rgba(255,247,237,.65);
  line-height: 1.7;
}

.fc-10__stats-row {
  display: flex;
  gap: 12px;
}

.fc-10__stat {
  flex: 1;
  padding: 12px;
  border-radius: 10px;
  background: rgba(255,255,255,.04);
  border: 1px solid rgba(255,255,255,.07);
  text-align: center;
}

.fc-10__stat-n {
  font-size: 20px;
  font-weight: 800;
  background: linear-gradient(135deg,var(--red),var(--orange));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.fc-10__stat-l {
  font-size: 9px;
  text-transform: uppercase;
  letter-spacing: .1em;
  color: rgba(255,247,237,.35);
  margin-top: 2px;
}

.fc-10__playlist {
  margin-top: 4px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.fc-10__pl-item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 8px 10px;
  border-radius: 8px;
  background: rgba(255,255,255,.03);
  border: 1px solid rgba(255,255,255,.05);
}

.fc-10__pl-num {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: rgba(239,68,68,.15);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 10px;
  font-weight: 700;
  color: var(--red);
  flex-shrink: 0;
}

.fc-10__pl-name {
  font-size: 11px;
  color: rgba(255,247,237,.65);
  flex: 1;
}

.fc-10__pl-dur {
  font-size: 10px;
  color: rgba(255,247,237,.3);
}

.fc-10__watch-btn {
  margin-top: auto;
  width: 100%;
  padding: 13px;
  background: linear-gradient(135deg,var(--red),var(--orange));
  color: #fff;
  font-size: 13px;
  font-weight: 800;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  letter-spacing: .04em;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
}

@media (prefers-reduced-motion: reduce) {
  .fc-10__card {
    transition: none;
  }
}
```
