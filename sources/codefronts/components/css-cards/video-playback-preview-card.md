---
source: "codefronts"
url: "https://codefronts.com/components/css-cards/video-playback-preview-card/"
title: "Video Playback Preview Card"
section: "components"
category: "css-cards"
category_name: "CSS Cards"
description: "Video thumbnail with 56×56 glass play button, duration pill, title, creator row and view count meta. Play button scales on hover."
has_js: "false"
---

Here's a working CSS Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Video Playback Preview Card
Source: https://codefronts.com/components/css-cards/video-playback-preview-card/

Video thumbnail with 56×56 glass play button, duration pill, title, creator row and view count meta. Play button scales on hover.
## HTML
```html
<section class="card-09">
  <article class="card-09__card">
    <div class="card-09__glow" aria-hidden="true"></div>
    <a href="#play" class="card-09__thumb" aria-label="Play video: Building Container Queries in 8 Minutes">
      <img class="card-09__img" src="https://images.unsplash.com/photo-1517180102446-f3ece451e9d8?w=800&q=80&auto=format&fit=crop" alt="CSS Container Queries tutorial" loading="lazy" decoding="async">
      <div class="card-09__thumb-shade" aria-hidden="true"></div>
      <div class="card-09__thumb-glow" aria-hidden="true"></div>
      <span class="card-09__live-badge">
        <span class="card-09__live-dot" aria-hidden="true"></span>
        LIVE
      </span>
      <span class="card-09__quality">4K</span>
      <span class="card-09__play" aria-hidden="true">
        <span class="card-09__play-ring"></span>
        <svg width="22" height="22" viewBox="0 0 24 24" fill="#fff" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>
      </span>
      <div class="card-09__thumb-foot">
        <div class="card-09__progress" aria-hidden="true">
          <span class="card-09__progress-fill"></span>
        </div>
        <div class="card-09__thumb-meta">
          <span class="card-09__watching">
            <span class="card-09__watching-dot" aria-hidden="true"></span>
            2.4k watching
          </span>
          <span class="card-09__dur">12:47</span>
        </div>
      </div>
    </a>
    <div class="card-09__body">
      <span class="card-09__chip">CSS · Tutorial</span>
      <h3 class="card-09__title">Building Container Queries in 8 Minutes</h3>
      <div class="card-09__meta">
        <span class="card-09__avatar" aria-hidden="true">
          JC
          <span class="card-09__avatar-verified" aria-hidden="true">
            <svg width="8" height="8" viewBox="0 0 24 24" fill="#fff" aria-hidden="true"><path d="M9 12l2 2 4-4" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" fill="none"/></svg>
          </span>
        </span>
        <div class="card-09__creator">
          <div class="card-09__name-row">
            <span class="card-09__name">Josh Comeau</span>
            <svg class="card-09__verified" aria-label="Verified" role="img" width="12" height="12" viewBox="0 0 24 24" fill="none">
              <path d="M12 2 L14 4 L17 3 L18 6 L21 7 L20 10 L22 12 L20 14 L21 17 L18 18 L17 21 L14 20 L12 22 L10 20 L7 21 L6 18 L3 17 L4 14 L2 12 L4 10 L3 7 L6 6 L7 3 L10 4 Z" fill="#3b82f6"/>
              <path d="M9 12 L11 14 L15 10" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </div>
          <span class="card-09__subs">128k subscribers · <span class="card-09__sub-delta">+2.1k this week</span></span>
        </div>
        <button type="button" class="card-09__save" aria-label="Save video">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
        </button>
      </div>
      <div class="card-09__reactions">
        <div class="card-09__stats">
          <span class="card-09__stat">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polygon points="12 2 15 9 22 9 17 14 19 21 12 17 5 21 7 14 2 9 9 9"/></svg>
            8.2k
          </span>
          <span class="card-09__stat">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
            342
          </span>
          <span class="card-09__stat">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><line x1="8.6" y1="13.5" x2="15.4" y2="17.5"/><line x1="15.4" y1="6.5" x2="8.6" y2="10.5"/></svg>
            892
          </span>
        </div>
        <div class="card-09__views">
          <time datetime="2026-07-05">Jul 5</time>
          <span class="card-09__views-dot" aria-hidden="true">·</span>
          <span>24.7k views</span>
        </div>
      </div>
    </div>
  </article>
</section>
```
## CSS
```css
.card-09 {
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: clamp(28px, 5vw, 56px) clamp(20px, 4vw, 40px);
  box-sizing: border-box;
  background: radial-gradient(ellipse at 20% 20%, rgba(236, 72, 153, 0.05) 0%, transparent 50%), radial-gradient(ellipse at 80% 80%, rgba(139, 92, 246, 0.05) 0%, transparent 50%), #f8f7f4;
  font-family: 'Inter', system-ui, sans-serif;
  --focus: #ec4899;
}

.card-09 *,
.card-09 *::before,
.card-09 *::after {
  box-sizing: border-box;
}

.card-09__card {
  position: relative;
  width: 100%;
  max-width: 380px;
  margin: 0 auto;
  background: #fff;
  border: 1px solid rgba(0, 0, 0, 0.05);
  border-radius: 22px;
  overflow: hidden;
  box-shadow: 0 30px 60px -30px rgba(80, 20, 90, 0.22), 0 0 0 1px rgba(255, 255, 255, 0.5) inset, 0 -1px 0 rgba(0, 0, 0, 0.02) inset;
  transition: transform 0.35s ease, box-shadow 0.35s;
  isolation: isolate;
}

.card-09__card:hover {
  transform: translateY(-3px);
  box-shadow: 0 40px 80px -30px rgba(80, 20, 90, 0.32), 0 0 0 1px rgba(255, 255, 255, 0.5) inset;
}

.card-09__glow {
  position: absolute;
  top: -80px;
  right: -80px;
  width: 260px;
  height: 260px;
  background: radial-gradient(circle, rgba(236, 72, 153, 0.16) 0%, transparent 55%), radial-gradient(circle at 30% 30%, rgba(139, 92, 246, 0.14) 0%, transparent 55%);
  filter: blur(30px);
  pointer-events: none;
  z-index: -1;
}
/* ── thumb ── */

.card-09__thumb {
  position: relative;
  display: block;
  width: 100%;
  aspect-ratio: 16 / 9;
  overflow: hidden;
  text-decoration: none;
  border-radius: 22px 22px 0 0;
}

.card-09__thumb-bg {
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse at 20% 30%, rgba(255, 255, 255, 0.14) 0%, transparent 50%), linear-gradient(135deg, #0d3b40 0%, #1e4c62 40%, #7e2a8a 100%);
  transition: filter 0.35s, transform 0.6s ease;
}

.card-09__img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform 0.6s ease, filter 0.35s;
}

.card-09__thumb-shade {
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, rgba(0,0,0,0.15) 0%, rgba(0,0,0,0.4) 100%);
  pointer-events: none;
}

.card-09__card:hover .card-09__img {
  transform: scale(1.05);
  filter: brightness(1.1) saturate(1.1);
}

.card-09__thumb-shape {
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at 20% 80%, rgba(236, 72, 153, 0.3) 0%, transparent 35%), radial-gradient(circle at 80% 20%, rgba(34, 211, 238, 0.25) 0%, transparent 30%), radial-gradient(circle at 60% 60%, rgba(139, 92, 246, 0.2) 0%, transparent 40%);
  mix-blend-mode: screen;
  transition: opacity 0.35s;
}

.card-09__thumb-glow {
  position: absolute;
  top: 40%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 60%;
  height: 60%;
  background: radial-gradient(ellipse, rgba(255, 255, 255, 0.2), transparent 70%);
  pointer-events: none;
  transition: opacity 0.35s;
}

.card-09__card:hover .card-09__thumb-bg {
  filter: brightness(1.12) saturate(1.1);
  transform: scale(1.04);
}

.card-09__card:hover .card-09__thumb-glow {
  opacity: 0.7;
}
/* live badge */

.card-09__live-badge {
  position: absolute;
  top: 12px;
  left: 12px;
  display: inline-flex;
  align-items: center;
  gap: 5px;
  padding: 4px 8px;
  background: rgba(220, 38, 38, 0.95);
  color: #fff;
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 9.5px;
  font-weight: 800;
  letter-spacing: 0.14em;
  border-radius: 6px;
  box-shadow: 0 4px 12px rgba(220, 38, 38, 0.35);
}

.card-09__live-dot {
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: #fff;
  animation: card-09-blink 1.4s ease-in-out infinite;
}
/* quality badge */

.card-09__quality {
  position: absolute;
  top: 12px;
  right: 12px;
  padding: 3px 7px;
  background: rgba(0, 0, 0, 0.72);
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
  color: #fff;
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 9.5px;
  font-weight: 800;
  letter-spacing: 0.06em;
  border: 1px solid rgba(255, 255, 255, 0.14);
  border-radius: 5px;
}
/* play button with ring */

.card-09__play {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 56px;
  height: 56px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(0, 0, 0, 0.6);
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
  border: 1.5px solid rgba(255, 255, 255, 0.28);
  border-radius: 50%;
  transition: transform 0.25s cubic-bezier(0.34, 1.2, 0.64, 1), background 0.25s, box-shadow 0.25s;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.35);
}

.card-09__play-ring {
  position: absolute;
  inset: -6px;
  border-radius: 50%;
  border: 1.5px solid rgba(255, 255, 255, 0.18);
  animation: card-09-ring 2.4s ease-in-out infinite;
}

.card-09__card:hover .card-09__play {
  transform: translate(-50%, -50%) scale(1.08);
  background: rgba(236, 72, 153, 0.8);
  box-shadow: 0 12px 32px rgba(236, 72, 153, 0.45);
}

.card-09__play svg {
  margin-left: 3px;
}
/* progress + watching row (bottom of thumb) */

.card-09__thumb-foot {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 0 12px 8px;
  background: linear-gradient(180deg, transparent 0%, rgba(0, 0, 0, 0.6) 100%);
  pointer-events: none;
}

.card-09__progress {
  height: 3px;
  background: rgba(255, 255, 255, 0.16);
  border-radius: 2px;
  overflow: hidden;
  margin-bottom: 6px;
}

.card-09__progress-fill {
  display: block;
  width: 42%;
  height: 100%;
  background: linear-gradient(90deg, #ec4899, #f472b6);
  border-radius: 2px;
}

.card-09__thumb-meta {
  display: flex;
  align-items: center;
  justify-content: space-between;
  color: #fff;
}

.card-09__watching {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.02em;
}

.card-09__watching-dot {
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: #34d399;
  box-shadow: 0 0 6px #34d399;
  animation: card-09-pulse 2s ease-in-out infinite;
}

.card-09__dur {
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: 0.02em;
}

.card-09__thumb:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: -2px;
}
/* ── body ── */

.card-09__body {
  padding: 14px 16px 14px;
  position: relative;
  z-index: 1;
}

.card-09__chip {
  display: inline-block;
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 9.5px;
  font-weight: 700;
  letter-spacing: 0.14em;
  color: #4338ca;
  padding: 2px 8px;
  background: rgba(99, 102, 241, 0.08);
  border: 1px solid rgba(99, 102, 241, 0.16);
  border-radius: 999px;
  margin-bottom: 8px;
  text-transform: uppercase;
}

.card-09__title {
  font-size: 15px;
  font-weight: 700;
  color: #1a1a1a;
  margin: 0 0 12px;
  letter-spacing: -0.015em;
  line-height: 1.3;
  background: linear-gradient(180deg, #1a1a1a 0%, #4b4b57 130%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.card-09__meta {
  display: grid;
  grid-template-columns: 36px 1fr auto;
  align-items: center;
  gap: 10px;
  margin-bottom: 12px;
}

.card-09__avatar {
  position: relative;
  width: 36px;
  height: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  background: linear-gradient(135deg, #ec4899, #f97316);
  color: #fff;
  font-size: 12px;
  font-weight: 800;
  border: 2px solid #fff;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
  letter-spacing: -0.01em;
}

.card-09__avatar-verified {
  position: absolute;
  bottom: -3px;
  right: -3px;
  width: 14px;
  height: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #3b82f6;
  border: 1.5px solid #fff;
  border-radius: 50%;
}

.card-09__creator {
  display: flex;
  flex-direction: column;
  gap: 1px;
  min-width: 0;
}

.card-09__name-row {
  display: inline-flex;
  align-items: center;
  gap: 4px;
}

.card-09__name {
  font-size: 13px;
  font-weight: 700;
  color: #1a1a1a;
  letter-spacing: -0.01em;
}

.card-09__verified {
  flex-shrink: 0;
}

.card-09__subs {
  font-size: 11px;
  color: #6b6b7c;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.card-09__sub-delta {
  color: #059669;
  font-weight: 700;
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 10.5px;
}

.card-09__save {
  width: 34px;
  height: 34px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: transparent;
  border: 1px solid rgba(0, 0, 0, 0.06);
  border-radius: 10px;
  color: #6b6b7c;
  cursor: pointer;
  transition: color 0.18s, background 0.18s, border-color 0.18s, transform 0.18s;
}

.card-09__save:hover {
  color: #ec4899;
  background: rgba(236, 72, 153, 0.06);
  border-color: rgba(236, 72, 153, 0.24);
  transform: translateY(-1px);
}

.card-09__save:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}

.card-09__reactions {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding-top: 10px;
  border-top: 1px solid rgba(0, 0, 0, 0.05);
}

.card-09__stats {
  display: flex;
  gap: 10px;
}

.card-09__stat {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-size: 11.5px;
  font-weight: 700;
  color: #4b4b57;
  font-variant-numeric: tabular-nums;
  letter-spacing: -0.005em;
}

.card-09__stat svg {
  color: #9ca3af;
  flex-shrink: 0;
}

.card-09__views {
  display: flex;
  align-items: center;
  gap: 4px;
  font-size: 11px;
  color: #9ca3af;
}

.card-09__views-dot {
  color: #cbd5e1;
}

@keyframes card-09-blink {
  0%,
    100% {
    opacity: 1;
    transform: scale(1);
  }

  50% {
    opacity: 0.5;
    transform: scale(0.85);
  }
}

@keyframes card-09-ring {
  0%,
    100% {
    transform: scale(1);
    opacity: 0.5;
  }

  50% {
    transform: scale(1.15);
    opacity: 0.1;
  }
}

@keyframes card-09-pulse {
  0%,
    100% {
    transform: scale(1);
    box-shadow: 0 0 6px #34d399;
  }

  50% {
    transform: scale(1.3);
    box-shadow: 0 0 10px #34d399;
  }
}

@media (prefers-reduced-motion: reduce) {
  .card-09__card,
    .card-09__thumb-bg,
    .card-09__play,
    .card-09__save {
    transition: none;
  }

  .card-09__card:hover {
    transform: none;
  }

  .card-09__card:hover .card-09__thumb-bg {
    transform: none;
  }

  .card-09__card:hover .card-09__play {
    transform: translate(-50%, -50%);
  }

  .card-09__save:hover {
    transform: none;
  }

  .card-09__live-dot,
    .card-09__play-ring,
    .card-09__watching-dot {
    animation: none;
  }
}
```
