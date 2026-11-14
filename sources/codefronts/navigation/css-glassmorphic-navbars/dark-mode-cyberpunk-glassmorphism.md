---
source: "codefronts"
url: "https://codefronts.com/navigation/css-glassmorphic-navbars/dark-mode-cyberpunk-glassmorphism/"
title: "Dark Mode / Cyberpunk Glassmorphism"
section: "navigation"
category: "css-glassmorphic-navbars"
category_name: "CSS Glassmorphic Sticky Navbars"
description: "The dark-mode-glassmorphism-navbar every night-theme product needs: a smoked-glass bar built on rgba(0,0,0,0.6) with a high blur, a razor-thin neon accent…"
has_js: "false"
---

Here's a working CSS Glassmorphic Sticky Navbar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dark Mode / Cyberpunk Glassmorphism
Source: https://codefronts.com/navigation/css-glassmorphic-navbars/dark-mode-cyberpunk-glassmorphism/

The dark-mode-glassmorphism-navbar every night-theme product needs: a smoked-glass bar built on rgba(0,0,0,0.6) with a high blur, a razor-thin neon accent border, and links that light up with a soft glow on hover. Reads as premium dark-UI or full cyberpunk depending on how hard you push the accent hue.
## HTML
```html
<div class="gn-03">
  <div class="gn-03__stage">
    <header class="gn-03-bar">
      <a class="gn-03-brand" href="#">NEO&#47;GRID</a>
      <nav aria-label="Primary">
        <ul>
          <li><a href="#" aria-current="page">Arcade</a></li>
          <li><a href="#">Netrun</a></li>
          <li><a href="#">Market</a></li>
          <li><a href="#">Comms</a></li>
        </ul>
      </nav>
      <a class="gn-03-cta" href="#">Jack in</a>
    </header>
    <div class="gn-03-body">
      <h2>Broadcast &sect; live from the grid</h2>
      <p>The smoked-glass bar stays pinned to the top as the scene rolls past. Dark translucent fill dims the colour underneath into a smoked pane rather than washing it out to grey.</p>
      <p>Chained <code>backdrop-filter</code> (blur + saturate + brightness) keeps the sampled hues alive under the tint. Drop the brightness and everything reads muddy; push it too far and the smoke turns milky.</p>
      <p>The neon accent is a single custom property (<code>--neon</code>). Swap it for magenta, toxic green, or hot amber and the whole identity re-skins in one line &mdash; border glow, hover text-shadow, and the lit underline all key off it.</p>
      <h3>Signal from the deck</h3>
      <p>Scroll further and the bar keeps its glow, keeps its blur, keeps its promise. Sticky + backdrop-filter is a compositor task, no scroll listener needed. The neon border cost is a single pseudo-element with a coloured box-shadow.</p>
      <p>Cyberpunk glass wants a saturated, contrasty background to blur &mdash; over pure dark, the effect disappears. Give it neon signage, gradient meshes, or scanline plates and the smoke reads correctly.</p>
      <p>Add a scanline texture with a <code>repeating-linear-gradient</code> overlay at 3-4% opacity for extra grit; the frost softens it into film-grain rather than lines. Push past 6% and it starts to compete with body text.</p>
      <p>Neon text glow can drop contrast below AA; keep the base link colour bright and treat the glow as decoration, never as the legibility mechanism.</p>
      <h3>Palette recipes worth stealing</h3>
      <p>Cyan cyberpunk (this demo): <code>--neon: oklch(0.82 0.16 195)</code>. Classic Blade Runner cool with high perceptual brightness.</p>
      <p>Synthwave magenta: <code>--neon: oklch(0.7 0.25 340)</code>. Reads hotter over dark blue-purple backgrounds; pair with a Miami-style sunset gradient.</p>
      <p>Toxic green: <code>--neon: oklch(0.85 0.2 130)</code>. The Matrix rain palette; works best over deep blacks with occasional emerald mist.</p>
      <p>Hot amber: <code>--neon: oklch(0.75 0.18 60)</code>. Reads as premium arcade cabinet rather than futurist; good for retro-gaming brand contexts.</p>
      <h3>Where cyberpunk glass belongs</h3>
      <p>Web3 wallet-connect flows use it because their audience expects the aesthetic. NFT marketplaces (OpenSea, Blur, Rainbow) mix it with iridescent card foils.</p>
      <p>Gaming portals (Steam frontends, Epic-store style landing pages) use it to signal &ldquo;premium experience&rdquo; without needing prose to say it.</p>
      <p>Cybersecurity SaaS (SentinelOne, Snyk-style dashboards) use a muted variant &mdash; the same recipe with saturation dialled down to 100% so it reads as serious rather than playful.</p>
      <p>Dev-tool marketing pages (Cursor, Warp, Zed) use dark glass as their default because their audience runs their desktop in dark mode &mdash; the marketing page needs to feel like an extension of the product, not a hostile bright-mode intrusion.</p>
      <p>Streaming platforms use dark glass for player chrome (Spotify's mini-player, Apple Music's now-playing bar) because it lets album art bleed through as ambient colour.</p>
      <p>Keep scrolling &mdash; the sticky bar demonstrates its resilience across the full page height.</p>
    </div>
  </div>
</div>
```
## CSS
```css
.gn-03 {
  --neon: oklch(0.82 0.16 195);
  font-family: system-ui,'Segoe UI',sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: stretch;
  border-radius: 16px;
  overflow: hidden;
  background: radial-gradient(90% 120% at 85% 10%,oklch(0.55 0.24 320) 0%,oklch(0.3 0.2 280) 35%,oklch(0.14 0.07 265) 75%),linear-gradient(120deg,oklch(0.18 0.1 200),oklch(0.12 0.04 285));
}

.gn-03 * {
  box-sizing: border-box;
}

.gn-03__stage {
  position: relative;
  height: 100vh;
  overflow-y: auto;
  scroll-behavior: smooth;
  padding: 20px;
}

.gn-03-bar {
  position: sticky;
  top: 0;
  z-index: 5;
  display: flex;
  align-items: center;
  gap: 22px;
  width: 100%;
  padding: 0 16px 0 20px;
  height: 60px;
  border-radius: 14px;
  background: rgba(10,12,20,.6);
  border: 1px solid color-mix(in oklab,var(--neon) 55%,transparent);
  box-shadow: 0 0 18px color-mix(in oklab,var(--neon) 30%,transparent),inset 0 1px 0 rgba(255,255,255,.06);
  -webkit-backdrop-filter: blur(20px) saturate(150%) brightness(1.1);
  backdrop-filter: blur(20px) saturate(150%) brightness(1.1);
}

.gn-03-brand {
  font-weight: 800;
  font-size: 17px;
  letter-spacing: .04em;
  color: #fff;
  text-decoration: none;
  text-shadow: 0 0 10px color-mix(in oklab,var(--neon) 70%,transparent);
}

.gn-03-bar nav ul {
  display: flex;
  gap: 4px;
  list-style: none;
  margin: 0;
  padding: 0;
  margin-inline: auto;
}

.gn-03-bar nav a {
  position: relative;
  display: flex;
  align-items: center;
  height: 40px;
  padding: 0 14px;
  border-radius: 9px;
  font: 600 14px/1 system-ui,sans-serif;
  color: rgba(240,244,255,.86);
  text-decoration: none;
  transition: color .16s ease,text-shadow .16s ease;
}

.gn-03-bar nav a:hover {
  color: #fff;
  text-shadow: 0 0 12px var(--neon);
}

.gn-03-bar nav a[aria-current="page"] {
  color: #fff;
}

.gn-03-bar nav a[aria-current="page"]::after {
  content: "";
  position: absolute;
  left: 12px;
  right: 12px;
  bottom: 6px;
  height: 2px;
  border-radius: 2px;
  background: linear-gradient(90deg,transparent,var(--neon),transparent);
  box-shadow: 0 0 8px var(--neon);
}

.gn-03-cta {
  display: flex;
  align-items: center;
  height: 40px;
  padding: 0 18px;
  border-radius: 10px;
  font: 700 13px/1 system-ui,sans-serif;
  letter-spacing: .03em;
  text-transform: uppercase;
  color: oklch(0.16 0.03 250);
  text-decoration: none;
  background: var(--neon);
  box-shadow: 0 0 16px color-mix(in oklab,var(--neon) 55%,transparent);
  transition: transform .16s ease;
}

.gn-03-cta:hover {
  transform: translateY(-1px);
}

.gn-03-bar a:focus-visible {
  outline: 2.5px solid var(--neon);
  outline-offset: 2px;
}

.gn-03-body {
  padding: 40px 8px 80px;
  max-width: 640px;
  margin-inline: auto;
  color: rgba(240,244,255,.82);
}

.gn-03-body h2 {
  margin: 20px 0 14px;
  font: 800 22px/1.2 system-ui,sans-serif;
  letter-spacing: .02em;
  color: #fff;
  text-shadow: 0 0 12px color-mix(in oklab,var(--neon) 60%,transparent);
}

.gn-03-body h3 {
  margin: 28px 0 12px;
  font: 700 18px/1.25 system-ui,sans-serif;
  letter-spacing: .02em;
  color: #fff;
  text-shadow: 0 0 10px color-mix(in oklab,var(--neon) 50%,transparent);
}

.gn-03-body p {
  margin: 0 0 14px;
  font: 500 15px/1.65 system-ui,sans-serif;
}

.gn-03-body code {
  background: rgba(10,12,20,.55);
  border: 1px solid color-mix(in oklab,var(--neon) 30%,transparent);
  padding: 2px 6px;
  border-radius: 5px;
  font-size: 13px;
  color: #fff;
}

@media (max-width: 640px) {
  .gn-03-bar {
    gap: 10px;
    padding: 0 12px 0 14px;
  }

  .gn-03-brand {
    font-size: 15px;
  }

  .gn-03-bar nav {
    display: none;
  }

  .gn-03-cta {
    padding: 0 14px;
    font-size: 12px;
  }
}

@media (max-width: 400px) {
  .gn-03-cta {
    padding: 0 12px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .gn-03 * {
    transition: none;
  }
}
```
