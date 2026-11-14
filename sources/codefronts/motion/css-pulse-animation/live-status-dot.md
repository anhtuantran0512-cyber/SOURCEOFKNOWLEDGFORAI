---
source: "codefronts"
url: "https://codefronts.com/motion/css-pulse-animation/live-status-dot/"
title: "Live Status Dot"
section: "motion"
category: "css-pulse-animation"
category_name: "CSS Pulse Animations"
description: "A streaming platform / chat app live-status indicator — small neon-lime dot with a soft continuous radiating ring signaling that a stream, user, or server is…"
has_js: "false"
---

Here's a working CSS Pulse Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Live Status Dot
Source: https://codefronts.com/motion/css-pulse-animation/live-status-dot/

A streaming platform / chat app live-status indicator — small neon-lime dot with a soft continuous radiating ring signaling that a stream, user, or server is actively "live" right now. Charcoal (#1a1a1a) streamer-lounge palette with neon lime (#84cc16) status color — Twitch / Discord / OBS-adjacent aesthetic. The dot appears in three real contexts within one demo: header ("12,400 watching"), stream card ("LIVE"), and channel list (with viewer count) — showing the pattern's versatility.
## HTML
```html
<div class="pl-06">
  <header class="pl-06__topbar">
    <div class="pl-06__brand">Streamdesk</div>
    <div class="pl-06__viewers">
      <span class="pl-06__dot" aria-label="Live now"></span>
      <span class="pl-06__count">12,400</span>
      <span class="pl-06__unit">watching</span>
    </div>
  </header>
  <main class="pl-06__stage">
    <div class="pl-06__featured">
      <div class="pl-06__thumb">
        <span class="pl-06__live-badge">
          <span class="pl-06__dot pl-06__dot--md" aria-hidden="true"></span>
          <span>LIVE</span>
        </span>
        <span class="pl-06__thumb-count">
          <svg viewBox="0 0 24 24" width="12" height="12" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true">
            <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/>
            <circle cx="12" cy="12" r="3"/>
          </svg>
          8.2k
        </span>
      </div>
      <p class="pl-06__stream-title">Building a game engine in Rust · Day 14</p>
      <p class="pl-06__stream-meta">
        <strong>silverwing</strong>
        <span>·</span>
        <span>Programming</span>
        <span>·</span>
        <span>3h 12m</span>
      </p>
    </div>
    <aside class="pl-06__sidebar">
      <p class="pl-06__sidebar-title">Online now</p>
      <div class="pl-06__channels">
        <div class="pl-06__channel">
          <span class="pl-06__avatar" aria-hidden="true">s</span>
          <div class="pl-06__channel-info">
            <div class="pl-06__channel-name">
              <span>silverwing</span>
              <span class="pl-06__dot" aria-label="Live"></span>
            </div>
            <div class="pl-06__channel-sub">Rust · 8,220</div>
          </div>
        </div>
        <div class="pl-06__channel">
          <span class="pl-06__avatar" aria-hidden="true" style="background:linear-gradient(135deg,#ff6b6b,#f97316)">n</span>
          <div class="pl-06__channel-info">
            <div class="pl-06__channel-name">
              <span>nightcrawler</span>
              <span class="pl-06__dot" aria-label="Live"></span>
            </div>
            <div class="pl-06__channel-sub">FPS · 2,140</div>
          </div>
        </div>
        <div class="pl-06__channel">
          <span class="pl-06__avatar" aria-hidden="true" style="background:linear-gradient(135deg,#a78bfa,#7c3aed)">k</span>
          <div class="pl-06__channel-info">
            <div class="pl-06__channel-name">
              <span>kodachi</span>
              <span class="pl-06__dot" aria-label="Live"></span>
            </div>
            <div class="pl-06__channel-sub">Piano · 640</div>
          </div>
        </div>
      </div>
    </aside>
  </main>
</div>
```
## CSS
```css
.pl-06 {
  --bg: #1a1a1a;
  --surface: #242426;
  --surface-hover: #2d2d30;
  --ink: #f5f5f0;
  --sub: #8a8a90;
  --lime: #84cc16;
  --lime-dim: rgba(132,204,22,.5);
  --line: #333336;
  font-family: -apple-system,BlinkMacSystemFont,'Inter','Segoe UI',sans-serif;
  width: 100%;
  min-height: 100vh;
  position: relative;
  display: grid;
  grid-template-rows: auto 1fr;
  gap: 20px;
  padding: 24px;
  background: var(--bg);
  color: var(--ink);
}

.pl-06 *,
.pl-06 *::before,
.pl-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pl-06 ::selection {
  background: var(--lime);
  color: var(--bg);
}

.pl-06__topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 18px;
  border-radius: 10px;
  background: var(--surface);
  border: 1px solid var(--line);
}

.pl-06__brand {
  font-weight: 700;
  font-size: .95rem;
  letter-spacing: -.02em;
}

.pl-06__viewers {
  display: flex;
  align-items: center;
  gap: 8px;
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: .82rem;
}

.pl-06__count {
  color: var(--ink);
  font-weight: 700;
  font-variant-numeric: tabular-nums;
}

.pl-06__unit {
  color: var(--sub);
  font-family: -apple-system,BlinkMacSystemFont,'Inter',sans-serif;
  font-size: .78rem;
}
/* Live status dot — the core pattern */

.pl-06__dot {
  position: relative;
  flex-shrink: 0;
  display: inline-block;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--lime);
}

.pl-06__dot::before {
  content: '';
  position: absolute;
  inset: -4px;
  border-radius: 50%;
  background: var(--lime-dim);
  pointer-events: none;
  animation: pl-06-ring 1.8s ease-out infinite;
}

.pl-06__dot--md {
  width: 6px;
  height: 6px;
}

.pl-06__dot--md::before {
  inset: -3px;
}

@keyframes pl-06-ring {
  0% {
    transform: scale(1);
    opacity: .55;
  }

  70% {
    transform: scale(2.4);
    opacity: 0;
  }

  100% {
    transform: scale(2.6);
    opacity: 0;
  }
}

.pl-06__stage {
  display: grid;
  grid-template-columns: 1fr 260px;
  gap: 16px;
  min-height: 0;
}

@media (max-width: 640px) {
  .pl-06__stage {
    grid-template-columns: 1fr;
  }
}

.pl-06__featured {
  padding: 16px;
  border-radius: 12px;
  background: var(--surface);
  border: 1px solid var(--line);
  display: flex;
  flex-direction: column;
}

.pl-06__thumb {
  position: relative;
  aspect-ratio: 16/9;
  background: linear-gradient(135deg,#3f3f46 0%,#18181b 55%,#0a0a0b 100%);
  border-radius: 9px;
  margin-bottom: 12px;
}

.pl-06__live-badge {
  position: absolute;
  top: 10px;
  left: 10px;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 4px 8px;
  border-radius: 5px;
  background: rgba(0,0,0,.7);
  color: var(--ink);
  font-size: .7rem;
  font-weight: 800;
  letter-spacing: .08em;
  backdrop-filter: blur(4px);
}

.pl-06__thumb-count {
  position: absolute;
  bottom: 10px;
  right: 10px;
  display: inline-flex;
  align-items: center;
  gap: 5px;
  padding: 4px 8px;
  border-radius: 5px;
  background: rgba(0,0,0,.7);
  color: var(--ink);
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: .72rem;
  font-weight: 700;
  backdrop-filter: blur(4px);
}

.pl-06__stream-title {
  font-size: .95rem;
  font-weight: 700;
  letter-spacing: -.01em;
  margin-bottom: 6px;
  line-height: 1.3;
}

.pl-06__stream-meta {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: .75rem;
  color: var(--sub);
}

.pl-06__stream-meta strong {
  color: var(--ink);
  font-weight: 600;
}

.pl-06__sidebar {
  padding: 14px;
  border-radius: 12px;
  background: var(--surface);
  border: 1px solid var(--line);
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.pl-06__sidebar-title {
  font-size: .7rem;
  font-weight: 700;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--sub);
}

.pl-06__channels {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.pl-06__channel {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 8px;
  border-radius: 8px;
  transition: background .15s ease;
  cursor: pointer;
}

.pl-06__channel:hover {
  background: var(--surface-hover);
}

.pl-06__avatar {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  flex-shrink: 0;
  background: linear-gradient(135deg,#84cc16,#4d7c0f);
  color: var(--bg);
  font-size: .72rem;
  font-weight: 700;
}

.pl-06__channel-info {
  flex: 1;
  min-width: 0;
}

.pl-06__channel-name {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: .82rem;
  font-weight: 600;
}

.pl-06__channel-sub {
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: .7rem;
  color: var(--sub);
  margin-top: 1px;
}

@media (prefers-reduced-motion: reduce) {
  .pl-06__dot::before {
    animation: none!important;
  }
}
```
