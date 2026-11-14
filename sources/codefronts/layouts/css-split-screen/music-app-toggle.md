---
source: "codefronts"
url: "https://codefronts.com/layouts/css-split-screen/music-app-toggle/"
title: "Music App Toggle"
section: "layouts"
category: "css-split-screen"
category_name: "CSS Split Screen Layouts"
description: "Music app — deep purple + neon mint + black vinyl."
has_js: "false"
---

Here's a working CSS Split Screen Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Music App Toggle
Source: https://codefronts.com/layouts/css-split-screen/music-app-toggle/

Music app — deep purple + neon mint + black vinyl. Toggle between equal-split (album list) and focus-mode (now playing dominates). Hidden checkbox + :has(:checked) on the grid template; everything else is CSS.
## HTML
```html
<section class="ss-mus" aria-label="Music player split">
  <input id="ss-mus-t" type="checkbox" />
  <article class="ss-mus-list" aria-label="Album list">
    <header>
      <h3>Library</h3>
      <label for="ss-mus-t" class="ss-mus-toggle" aria-controls="ss-mus-now">⇋ Focus</label>
    </header>
    <ul>
      <li class="active">
        <span
          class="ss-mus-cover"
          style="background: linear-gradient(135deg, #7c3aed, #ec4899)"
        ></span>
        <div><strong>Midnight Drive</strong><em>Aurelia · Side A</em></div>
        <span class="ss-mus-time">3:42</span>
      </li>
      <li>
        <span
          class="ss-mus-cover"
          style="background: linear-gradient(135deg, #0ea5e9, #22d3ee)"
        ></span>
        <div><strong>Glass Hearts</strong><em>Aurelia · Side B</em></div>
        <span class="ss-mus-time">4:18</span>
      </li>
      <li>
        <span
          class="ss-mus-cover"
          style="background: linear-gradient(135deg, #f59e0b, #ef4444)"
        ></span>
        <div><strong>Cherry Static</strong><em>Various</em></div>
        <span class="ss-mus-time">2:54</span>
      </li>
      <li>
        <span
          class="ss-mus-cover"
          style="background: linear-gradient(135deg, #10b981, #84cc16)"
        ></span>
        <div><strong>Forest Floor</strong><em>Aurelia</em></div>
        <span class="ss-mus-time">5:02</span>
      </li>
    </ul>
  </article>
  <article class="ss-mus-now" id="ss-mus-now" aria-label="Now playing">
    <div class="ss-mus-vinyl" aria-hidden="true">
      <span class="ss-mus-disc"></span>
      <span class="ss-mus-hole"></span>
    </div>
    <div class="ss-mus-meta">
      <span class="ss-mus-eye">▸ NOW PLAYING</span>
      <h2>Midnight<br />Drive.</h2>
      <p class="ss-mus-sub">Aurelia · Side A · Track 03</p>
      <div
        class="ss-mus-bar"
        aria-label="Track progress"
        role="progressbar"
        aria-valuenow="42"
        aria-valuemin="0"
        aria-valuemax="100"
      >
        <span style="width: 42%"></span>
      </div>
      <div class="ss-mus-times"><span>1:33</span><span>3:42</span></div>
      <div class="ss-mus-ctrl">
        <button type="button" aria-label="Previous">⏮</button>
        <button type="button" aria-label="Play" class="ss-mus-play">▶</button>
        <button type="button" aria-label="Next">⏭</button>
      </div>
    </div>
  </article>
</section>
```
## CSS
```css
.ss-mus {
  width: 100%;
  position: relative;
  display: grid;
  grid-template-columns: 50% 50%;
  min-height: 100vh;
  font-family: 'Inter', system-ui, sans-serif;
  background: #0e0a1f;
  color: #e6e0ff;
  border-radius: 0;
  overflow: hidden;
  transition: grid-template-columns 0.4s cubic-bezier(0.32, 0.72, 0, 1);
}

.ss-mus:has(input:checked) {
  grid-template-columns: 30% 70%;
}

.ss-mus input {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip: rect(0 0 0 0);
}

.ss-mus-list {
  background: #15102a;
  padding: 30px 24px;
  display: flex;
  flex-direction: column;
  gap: 16px;
  border-right: 1px solid rgba(74,222,128,0.25);
  overflow-y: auto;
}

.ss-mus-list header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-bottom: 14px;
  border-bottom: 1px solid rgba(255,255,255,0.06);
}

.ss-mus-list h3 {
  margin: 0;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #4ade80;
}

.ss-mus-toggle {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.12em;
  padding: 5px 10px;
  background: rgba(74,222,128,0.12);
  color: #4ade80;
  border: 1px solid rgba(74,222,128,0.4);
  cursor: pointer;
  transition: background 0.14s;
}

.ss-mus-toggle:hover {
  background: rgba(74,222,128,0.24);
}

.ss-mus-list ul {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.ss-mus-list li {
  display: grid;
  grid-template-columns: 38px 1fr auto;
  align-items: center;
  gap: 12px;
  padding: 10px;
  border-radius: 8px;
  cursor: pointer;
  transition: background 0.14s;
}

.ss-mus-list li:hover {
  background: rgba(255,255,255,0.04);
}

.ss-mus-list li.active {
  background: rgba(74,222,128,0.1);
  border: 1px solid rgba(74,222,128,0.3);
  padding: 9px;
}

.ss-mus-cover {
  width: 38px;
  height: 38px;
  border-radius: 6px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.5);
}

.ss-mus-list strong {
  display: block;
  font-size: 13.5px;
  font-weight: 700;
  color: #f0eaff;
}

.ss-mus-list em {
  display: block;
  font-size: 11px;
  font-style: normal;
  color: #8a7fb0;
  margin-top: 2px;
}

.ss-mus-time {
  font-family: 'Courier New', monospace;
  font-size: 11px;
  color: #8a7fb0;
}

.ss-mus-now {
  background: radial-gradient(60% 80% at 70% 30%, rgba(124,58,237,0.4) 0%, transparent 60%), radial-gradient(60% 80% at 30% 70%, rgba(74,222,128,0.18) 0%, transparent 60%), #0e0a1f;
  padding: 40px 44px;
  display: grid;
  grid-template-columns: auto 1fr;
  gap: 36px;
  align-items: center;
}

.ss-mus-vinyl {
  position: relative;
  width: 200px;
  height: 200px;
  flex-shrink: 0;
}

.ss-mus-disc {
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: repeating-radial-gradient(circle at 50% 50%, transparent 0 4px, rgba(255,255,255,0.04) 4px 5px), radial-gradient(circle at 50% 50%, #ec4899 0%, #ec4899 14%, #0a0a0a 14%, #0a0a0a 100%);
  box-shadow: inset 0 0 0 14px #1a1a1a, 0 14px 40px rgba(0,0,0,0.6);
  animation: ss-mus-spin 8s linear infinite;
}

.ss-mus-hole {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background: #0e0a1f;
  box-shadow: 0 0 0 3px #4ade80;
}

@keyframes ss-mus-spin {
  to {
    transform: rotate(360deg);
  }
}

@media (prefers-reduced-motion: reduce) {
  .ss-mus-disc {
    animation: none;
  }
}

.ss-mus-meta {
  display: flex;
  flex-direction: column;
  gap: 12px;
  min-width: 0;
}

.ss-mus-eye {
  font-family: 'Courier New', monospace;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.24em;
  color: #4ade80;
  text-shadow: 0 0 12px rgba(74,222,128,0.4);
}

.ss-mus-meta h2 {
  margin: 0;
  font-family: 'Cormorant Garamond', serif;
  font-size: clamp(34px, 5vw, 56px);
  font-weight: 500;
  line-height: 0.94;
  color: #f0eaff;
  letter-spacing: -0.02em;
  font-style: italic;
}

.ss-mus-sub {
  margin: 0;
  font-size: 13px;
  color: #a89cc8;
  letter-spacing: 0.04em;
}

.ss-mus-bar {
  height: 4px;
  background: rgba(255,255,255,0.08);
  border-radius: 2px;
  overflow: hidden;
  margin-top: 8px;
}

.ss-mus-bar span {
  display: block;
  height: 100%;
  background: linear-gradient(90deg, #4ade80 0%, #ec4899 100%);
  border-radius: 2px;
  box-shadow: 0 0 12px rgba(74,222,128,0.5);
}

.ss-mus-times {
  display: flex;
  justify-content: space-between;
  font-family: 'Courier New', monospace;
  font-size: 11px;
  color: #8a7fb0;
}

.ss-mus-ctrl {
  display: flex;
  gap: 12px;
  align-items: center;
  margin-top: 6px;
}

.ss-mus-ctrl button {
  width: 38px;
  height: 38px;
  border-radius: 50%;
  border: 1px solid rgba(255,255,255,0.18);
  background: transparent;
  color: #f0eaff;
  font-size: 14px;
  cursor: pointer;
  transition: background 0.14s, border-color 0.14s;
}

.ss-mus-ctrl button:hover {
  background: rgba(255,255,255,0.06);
  border-color: #4ade80;
  color: #4ade80;
}

.ss-mus-play {
  width: 52px !important;
  height: 52px !important;
  background: linear-gradient(135deg, #4ade80 0%, #22c55e 100%) !important;
  color: #0e0a1f !important;
  border: 0 !important;
  font-size: 16px !important;
  box-shadow: 0 8px 22px rgba(74,222,128,0.45) !important;
}

.ss-mus-play:hover {
  transform: scale(1.05);
}

@media (max-width: 720px) {
  .ss-mus,
    .ss-mus:has(input:checked) {
    grid-template-columns: 1fr;
  }

  .ss-mus-now {
    grid-template-columns: 1fr;
    justify-items: center;
    text-align: center;
  }
}
```
