---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-frosted-glass-effect/css-glass-ui-footer-overlay/"
title: "CSS Glass UI Footer Overlay"
section: "design-styles"
category: "css-frosted-glass-effect"
category_name: "CSS Frosted Glass Effects"
description: "A fixed frosted glass footer overlay in the media-player style, floating over a full-height article page — the pattern Apple Music, Spotify web, and YouTube…"
has_js: "false"
---

Here's a working CSS Frosted Glass Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Glass UI Footer Overlay
Source: https://codefronts.com/design-styles/css-frosted-glass-effect/css-glass-ui-footer-overlay/

A fixed frosted glass footer overlay in the media-player style, floating over a full-height article page — the pattern Apple Music, Spotify web, and YouTube Music ship for their persistent bottom controls. Real article content (heading, paragraphs, pull-quote) scrolls behind the footer so the backdrop-filter has genuine text and imagery to blur. Footer contains album art thumbnail, track title + artist, progress bar with elapsed/total time, prev/play/next controls, and a volume slider.
## HTML
```html
<div class="fg-05">
  <article class="fg-05__article">
    <span class="fg-05__eyebrow">Field Notes</span>
    <h1 class="fg-05__title">The quiet return of desk-side music.</h1>
    <p class="fg-05__lede">For a decade our music lived in earbuds, on phones, siloed away from the room. Then something shifted — and it's been shifting quietly enough that most trend pieces have missed it entirely.</p>

    <p>The desktop music revival started with the return of the physical office in 2024. Small teams sharing rooms rediscovered speakers — cheap ones at first, then better ones, then dedicated setups. What started as "let's put on some background jazz" became curated playlists, shared music channels, and the strange social ritual of Slack-DM'ing songs to your desk-mate.</p>

    <blockquote class="fg-05__quote">
      "The song you're listening to at your desk tells your team more about you than your dotfiles."
    </blockquote>

    <p>By late 2025, the desktop music player was quietly one of the most-used pieces of software in engineering orgs. Not Spotify's iOS app. Not the smart-speaker in the corner. The <em>desktop</em> player — sitting persistently at the bottom of your screen, controls always visible, transparent enough to not fight your editor for attention.</p>

    <p>Which brings us to today's design pattern: the frosted glass persistent footer. It floats above your content. It never leaves. It's a chrome layer for something that has quietly become UI infrastructure.</p>

    <p>The frosted glass effect is not decoration here. It's function. The footer needs to remain readable when your editor is dark, when your document is bright, when a full-bleed image slides past behind it. Solid colours fail at least one of those cases. Semi-transparent fails all of them. Only frosted glass — real backdrop-filter blur — solves all three.</p>

    <p>The result is a chrome that adapts to whatever content it's sitting over, without the designer having to hard-code cases. Which is why every major desktop app that's shipped a persistent player in the last 18 months has landed on the same aesthetic. Convergent evolution, driven by CSS finally being good enough.</p>

    <p>The demo below is the copy-paste-ready version. Real album art. Real controls. Real backdrop-filter. Drop it into any project.</p>
  </article>

  <!-- Fixed frosted-glass media-player footer -->
  <div class="fg-05__player" role="region" aria-label="Now playing">
    <div class="fg-05__player-cover" aria-hidden="true"></div>
    <div class="fg-05__player-track">
      <span class="fg-05__player-title">Midnight Drive</span>
      <span class="fg-05__player-artist">Aurora · Nightlands</span>
    </div>
    <div class="fg-05__player-controls">
      <button type="button" class="fg-05__player-btn" aria-label="Previous track">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
          <path d="M19 20L9 12l10-8v16zM7 4h2v16H7z"/>
        </svg>
      </button>
      <button type="button" class="fg-05__player-btn fg-05__player-btn--play" aria-label="Play">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
          <path d="M8 5v14l11-7z"/>
        </svg>
      </button>
      <button type="button" class="fg-05__player-btn" aria-label="Next track">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
          <path d="M5 4l10 8-10 8V4zm10 0h2v16h-2z"/>
        </svg>
      </button>
    </div>
    <div class="fg-05__player-progress">
      <span class="fg-05__player-time">1:47</span>
      <div class="fg-05__progress" role="progressbar" aria-valuenow="42">
        <span class="fg-05__progress-fill"></span>
      </div>
      <span class="fg-05__player-time">4:12</span>
    </div>
    <div class="fg-05__player-volume">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/>
        <path d="M19.07 4.93a10 10 0 010 14.14M15.54 8.46a5 5 0 010 7.07"/>
      </svg>
      <div class="fg-05__volume-bar">
        <span class="fg-05__volume-fill"></span>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.fg-05,
.fg-05 *,
.fg-05 *::before,
.fg-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fg-05 ::selection {
  background: rgba(124,108,255,.28);
  color: #0f172a;
}

.fg-05 {
  --accent: #7c6cff;
  --ink: #0f172a;
  --muted: #64748b;
  --paper: #fafaf7;
  min-height: 100vh;
  background: radial-gradient(circle at 10% 15%, rgba(124,108,255,0.15) 0%, transparent 40%), radial-gradient(circle at 90% 85%, rgba(236,72,153,0.12) 0%, transparent 40%), var(--paper);
  font-family: -apple-system,BlinkMacSystemFont,"Inter","Segoe UI",Roboto,sans-serif;
  color: var(--ink);
  padding: 60px 20px 140px;
  position: relative;
}

.fg-05__article {
  max-width: 680px;
  margin: 0 auto;
}

.fg-05__eyebrow {
  display: inline-block;
  font-size: .72rem;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--accent);
  padding: 5px 12px;
  border-radius: 999px;
  background: rgba(124,108,255,0.10);
  margin-bottom: 16px;
}

.fg-05__title {
  font-family: Georgia,"Times New Roman",serif;
  font-size: clamp(1.8rem,4vw,2.6rem);
  font-weight: 800;
  letter-spacing: -.02em;
  line-height: 1.15;
  margin-bottom: 16px;
}

.fg-05__lede {
  font-size: clamp(1.05rem,1.6vw,1.2rem);
  color: var(--ink);
  line-height: 1.55;
  margin-bottom: 26px;
  font-family: Georgia,"Times New Roman",serif;
}

.fg-05__article p {
  font-size: 1rem;
  line-height: 1.7;
  color: #3f4657;
  margin-bottom: 20px;
}

.fg-05__article p em {
  color: var(--accent);
  font-style: italic;
  font-weight: 600;
}

.fg-05__quote {
  font-family: Georgia,"Times New Roman",serif;
  font-size: clamp(1.25rem,2.2vw,1.5rem);
  font-style: italic;
  line-height: 1.35;
  color: var(--ink);
  padding: 14px 0 14px 22px;
  border-left: 3px solid var(--accent);
  margin: 26px 0;
}
/* Fixed frosted glass player footer */

.fg-05__player {
  position: fixed;
  bottom: 20px;
  left: 20px;
  right: 20px;
  z-index: 20;
  padding: 14px 20px;
  border-radius: 16px;
  background: rgba(255,255,255,0.72);
  -webkit-backdrop-filter: blur(28px) saturate(180%);
  backdrop-filter: blur(28px) saturate(180%);
  border: 1px solid rgba(255,255,255,0.65);
  box-shadow: 0 24px 48px -20px rgba(15,15,30,0.28), inset 0 1px 0 rgba(255,255,255,0.9);
  display: flex;
  align-items: center;
  gap: 16px;
  color: var(--ink);
  will-change: backdrop-filter;
}

@supports not (backdrop-filter: blur(1px)) {
  .fg-05__player {
    background: rgba(255,255,255,0.96);
  }
}

.fg-05__player-cover {
  width: 44px;
  height: 44px;
  border-radius: 8px;
  background: linear-gradient(135deg,#7c6cff,#ec4899);
  flex-shrink: 0;
}

.fg-05__player-track {
  display: flex;
  flex-direction: column;
  gap: 1px;
  min-width: 0;
  flex: 0 0 auto;
  width: clamp(120px,18vw,180px);
}

.fg-05__player-title {
  font-size: .88rem;
  font-weight: 700;
  color: var(--ink);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.fg-05__player-artist {
  font-size: .76rem;
  color: var(--muted);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.fg-05__player-controls {
  display: flex;
  align-items: center;
  gap: 4px;
  flex-shrink: 0;
}

.fg-05__player-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 32px;
  height: 32px;
  background: transparent;
  border: 0;
  border-radius: 8px;
  color: var(--ink);
  cursor: pointer;
  transition: background .2s,transform .1s;
}

.fg-05__player-btn:hover {
  background: rgba(15,15,30,0.06);
}

.fg-05__player-btn:active {
  transform: scale(0.94);
}

.fg-05__player-btn--play {
  width: 36px;
  height: 36px;
  background: var(--accent);
  color: #fff;
  border-radius: 50%;
}

.fg-05__player-btn--play:hover {
  background: #6d5cf0;
}

.fg-05__player-progress {
  flex: 1;
  display: flex;
  align-items: center;
  gap: 10px;
  min-width: 0;
}

.fg-05__player-time {
  font-size: .72rem;
  color: var(--muted);
  font-weight: 600;
  font-feature-settings: "tnum";
  min-width: 32px;
  text-align: center;
}

.fg-05__progress {
  flex: 1;
  height: 4px;
  border-radius: 2px;
  background: rgba(15,15,30,0.10);
  overflow: hidden;
}

.fg-05__progress-fill {
  display: block;
  height: 100%;
  width: 42%;
  background: var(--accent);
  border-radius: 2px;
}

.fg-05__player-volume {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-shrink: 0;
  color: var(--muted);
}

.fg-05__volume-bar {
  width: 80px;
  height: 4px;
  border-radius: 2px;
  background: rgba(15,15,30,0.10);
  overflow: hidden;
}

.fg-05__volume-fill {
  display: block;
  height: 100%;
  width: 65%;
  background: var(--ink);
  border-radius: 2px;
}

@media (max-width: 720px) {
  .fg-05__player {
    gap: 10px;
    padding: 10px 14px;
  }

  .fg-05__player-progress,
    .fg-05__player-volume {
    display: none;
  }

  .fg-05__player-track {
    flex: 1;
    width: auto;
  }
}

@media (prefers-reduced-motion: reduce) {
  .fg-05__player-btn {
    transition: none;
  }
}
```
