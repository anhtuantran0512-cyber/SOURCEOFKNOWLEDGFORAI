---
source: "codefronts"
url: "https://codefronts.com/navigation/css-mobile-navigation/tab-bar-with-sliding-indicator-pill/"
title: "Tab Bar with Sliding Indicator Pill"
section: "navigation"
category: "css-mobile-navigation"
category_name: "CSS Mobile Navigation Patterns"
description: "A dark music-app tab bar with a smooth sliding pill indicator that transitions between four tabs, each with its own accent colour."
has_js: "false"
---

Here's a working CSS Mobile Navigation Pattern from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tab Bar with Sliding Indicator Pill
Source: https://codefronts.com/navigation/css-mobile-navigation/tab-bar-with-sliding-indicator-pill/

A dark music-app tab bar with a smooth sliding pill indicator that transitions between four tabs, each with its own accent colour. Pages switch with a fade-slide animation, all driven by radio inputs.
## HTML
```html
<div class="mn-08">
  <input type="radio" name="mn-08-tab" id="mn-08-t1" checked>
  <input type="radio" name="mn-08-tab" id="mn-08-t2">
  <input type="radio" name="mn-08-tab" id="mn-08-t3">
  <input type="radio" name="mn-08-tab" id="mn-08-t4">

  <div class="mn-08__header">
    <div class="mn-08__logo">Wavify</div>
    <div class="mn-08__notif">🔔</div>
  </div>

  <div class="mn-08__tabs">
    <div class="mn-08__tab-pill"></div>
    <label for="mn-08-t1" class="mn-08__tab-label"><span>🎵</span>Music</label>
    <label for="mn-08-t2" class="mn-08__tab-label"><span>🎙️</span>Pods</label>
    <label for="mn-08-t3" class="mn-08__tab-label"><span>📻</span>Radio</label>
    <label for="mn-08-t4" class="mn-08__tab-label"><span>📚</span>Library</label>
  </div>

  <div class="mn-08__pages">
    <div class="mn-08__page" data-p="1">
      <div class="mn-08__section-title">Trending Now</div>
      <div class="mn-08__track">
        <div class="mn-08__track-art" style="background:linear-gradient(135deg,#22d3ee,#6366f1)">🎵</div>
        <div class="mn-08__track-info"><h4>Neon Lights</h4><p>Synthwave Collective · 3:42</p></div>
        <span class="mn-08__track-more">⋯</span>
      </div>
      <div class="mn-08__track">
        <div class="mn-08__track-art" style="background:linear-gradient(135deg,#fb923c,#f43f5e)">🎸</div>
        <div class="mn-08__track-info"><h4>Midnight Drive</h4><p>Neon Atlas · 4:18</p></div>
        <span class="mn-08__track-more">⋯</span>
      </div>
      <div class="mn-08__track">
        <div class="mn-08__track-art" style="background:linear-gradient(135deg,#a78bfa,#ec4899)">🎹</div>
        <div class="mn-08__track-info"><h4>Electric Dream</h4><p>Pixel Sound · 5:01</p></div>
        <span class="mn-08__track-more">⋯</span>
      </div>
    </div>

    <div class="mn-08__page" data-p="2">
      <div class="mn-08__section-title">Popular Podcasts</div>
      <div class="mn-08__grid">
        <div class="mn-08__grid-card"><div class="mn-08__grid-icon">🧠</div><h4>Deep Dives</h4><p>128 episodes</p></div>
        <div class="mn-08__grid-card"><div class="mn-08__grid-icon">💡</div><h4>Tech Talks</h4><p>84 episodes</p></div>
        <div class="mn-08__grid-card"><div class="mn-08__grid-icon">🌍</div><h4>World News</h4><p>312 episodes</p></div>
        <div class="mn-08__grid-card"><div class="mn-08__grid-icon">🎤</div><h4>Interviews</h4><p>56 episodes</p></div>
      </div>
    </div>

    <div class="mn-08__page" data-p="3">
      <div class="mn-08__section-title">Live Radio</div>
      <div class="mn-08__track">
        <div class="mn-08__track-art" style="background:linear-gradient(135deg,#a78bfa,#7c3aed)">📻</div>
        <div class="mn-08__track-info"><h4>Synthwave FM</h4><p>🔴 Live · 2.4k listeners</p></div>
        <span class="mn-08__track-more">▶</span>
      </div>
      <div class="mn-08__track">
        <div class="mn-08__track-art" style="background:linear-gradient(135deg,#4ade80,#16a34a)">🎶</div>
        <div class="mn-08__track-info"><h4>Chill Beats</h4><p>🔴 Live · 8.1k listeners</p></div>
        <span class="mn-08__track-more">▶</span>
      </div>
    </div>

    <div class="mn-08__page" data-p="4">
      <div class="mn-08__section-title">Your Library</div>
      <div class="mn-08__track">
        <div class="mn-08__track-art" style="background:linear-gradient(135deg,#4ade80,#06b6d4)">⭐</div>
        <div class="mn-08__track-info"><h4>Liked Songs</h4><p>248 tracks</p></div>
        <span class="mn-08__track-more">›</span>
      </div>
      <div class="mn-08__track">
        <div class="mn-08__track-art" style="background:linear-gradient(135deg,#f59e0b,#ef4444)">🎼</div>
        <div class="mn-08__track-info"><h4>My Playlists</h4><p>12 playlists</p></div>
        <span class="mn-08__track-more">›</span>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
*,
*::before,
*::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background: #0f0f13;
  font-family: 'Segoe UI', sans-serif;
}

.mn-08 {
  --bg: #09090b;
  --surface: #18181b;
  --border: #27272a;
  --accent: #22d3ee;
  --accent2: #fb923c;
  --accent3: #a78bfa;
  --accent4: #4ade80;
  --text: #fafafa;
  --muted: #71717a;
  width: 375px;
  height: 667px;
  position: relative;
  overflow: hidden;
  background: var(--bg);
  border-radius: 32px;
  box-shadow: 0 30px 80px rgba(0,0,0,0.8);
}

.mn-08 input[type="radio"] {
  display: none;
}
/* Header */

.mn-08__header {
  padding: 28px 20px 0;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.mn-08__logo {
  font-size: 20px;
  font-weight: 800;
  letter-spacing: -0.5px;
  background: linear-gradient(90deg, var(--accent), var(--accent3));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.mn-08__notif {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: var(--surface);
  border: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
  position: relative;
}

.mn-08__notif::after {
  content: '';
  position: absolute;
  top: 6px;
  right: 7px;
  width: 8px;
  height: 8px;
  background: #ef4444;
  border-radius: 50%;
  border: 2px solid var(--bg);
}
/* Tab pill nav */

.mn-08__tabs {
  position: relative;
  display: flex;
  align-items: center;
  background: var(--surface);
  border-radius: 20px;
  margin: 20px 16px;
  padding: 4px;
  border: 1px solid var(--border);
}

.mn-08__tab-pill {
  position: absolute;
  height: calc(100% - 8px);
  border-radius: 16px;
  top: 4px;
  transition: left 0.35s cubic-bezier(0.4, 0, 0.2, 1), width 0.35s cubic-bezier(0.4, 0, 0.2, 1), background 0.3s;
  pointer-events: none;
}
/* 4 tabs → each 25% */

#mn-08-t1:checked ~ .mn-08__tabs .mn-08__tab-pill {
  left: 4px;
  width: calc(25% - 2px);
  background: var(--accent);
}

#mn-08-t2:checked ~ .mn-08__tabs .mn-08__tab-pill {
  left: calc(25% + 2px);
  width: calc(25% - 2px);
  background: var(--accent2);
}

#mn-08-t3:checked ~ .mn-08__tabs .mn-08__tab-pill {
  left: calc(50% + 2px);
  width: calc(25% - 2px);
  background: var(--accent3);
}

#mn-08-t4:checked ~ .mn-08__tabs .mn-08__tab-pill {
  left: calc(75% + 2px);
  width: calc(25% - 4px);
  background: var(--accent4);
}

.mn-08__tab-label {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 3px;
  padding: 8px 4px;
  cursor: pointer;
  z-index: 1;
  transition: color 0.25s;
  color: var(--muted);
  font-size: 10px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  border-radius: 16px;
}

.mn-08__tab-label span {
  font-size: 18px;
  display: block;
}

#mn-08-t1:checked ~ .mn-08__tabs label[for="mn-08-t1"],
#mn-08-t2:checked ~ .mn-08__tabs label[for="mn-08-t2"],
#mn-08-t3:checked ~ .mn-08__tabs label[for="mn-08-t3"],
#mn-08-t4:checked ~ .mn-08__tabs label[for="mn-08-t4"] {
  color: var(--bg);
}
/* Pages */

.mn-08__pages {
  position: absolute;
  top: 158px;
  left: 0;
  right: 0;
  bottom: 0;
}

.mn-08__page {
  position: absolute;
  inset: 0;
  padding: 0 16px 16px;
  opacity: 0;
  pointer-events: none;
  transform: translateY(10px);
  transition: opacity 0.3s, transform 0.3s;
  overflow-y: auto;
}

#mn-08-t1:checked ~ .mn-08__pages .mn-08__page[data-p="1"],
#mn-08-t2:checked ~ .mn-08__pages .mn-08__page[data-p="2"],
#mn-08-t3:checked ~ .mn-08__pages .mn-08__page[data-p="3"],
#mn-08-t4:checked ~ .mn-08__pages .mn-08__page[data-p="4"] {
  opacity: 1;
  pointer-events: all;
  transform: translateY(0);
}

.mn-08__section-title {
  font-size: 20px;
  font-weight: 700;
  color: var(--text);
  letter-spacing: -0.4px;
  margin-bottom: 16px;
}

.mn-08__track {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 14px;
  padding: 14px 16px;
  display: flex;
  align-items: center;
  gap: 14px;
  margin-bottom: 10px;
}

.mn-08__track-art {
  width: 48px;
  height: 48px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 22px;
  flex-shrink: 0;
}

.mn-08__track-info h4 {
  font-size: 14px;
  font-weight: 600;
  color: var(--text);
}

.mn-08__track-info p {
  font-size: 12px;
  color: var(--muted);
}

.mn-08__track-more {
  margin-left: auto;
  color: var(--muted);
  font-size: 18px;
  cursor: pointer;
}
/* Podcast / video cards */

.mn-08__grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
}

.mn-08__grid-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 14px;
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.mn-08__grid-icon {
  font-size: 28px;
}

.mn-08__grid-card h4 {
  font-size: 13px;
  font-weight: 600;
  color: var(--text);
}

.mn-08__grid-card p {
  font-size: 11px;
  color: var(--muted);
}

@media (prefers-reduced-motion: reduce) {
  .mn-08__tab-pill,
    .mn-08__page {
    transition: none;
  }
}
```
