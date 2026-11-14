---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-glassmorphic-sticky-navbars/dark-mode-cyberpunk-neon-glass-navbar-tailwind/"
title: "Dark Mode Cyberpunk Neon Glass Navbar in Tailwind CSS"
section: "navigation"
category: "tailwind-css-glassmorphic-sticky-navbars"
category_name: "Tailwind CSS Glassmorphic Navbars"
description: "Smoked glass over a magenta-to-indigo night sky: a dark translucent bar with a neon hairline, a cyan glow, scanlines and a glowing active underline."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dark Mode Cyberpunk Neon Glass Navbar in Tailwind CSS
Source: https://codefronts.com/navigation/tailwind-css-glassmorphic-sticky-navbars/dark-mode-cyberpunk-neon-glass-navbar-tailwind/

Smoked glass over a magenta-to-indigo night sky: a dark translucent bar with a neon hairline, a cyan glow, scanlines and a glowing active underline. The neon is one @theme token, so border-tgn03-neon/55, the glow shadows and the CTA all re-theme together.
## HTML
```html
<div class="tgn-03 w-full min-h-svh bg-tgn03-sky bg-[radial-gradient(90%_120%_at_85%_10%,var(--color-tgn03-mag)_0%,var(--color-tgn03-ind)_35%,var(--color-tgn03-sky)_75%)] font-tgn03-display">
  <div class="relative h-svh overflow-y-auto scroll-smooth p-3 sm:p-5">
    <header class="sticky top-0 z-10 flex min-h-15 flex-wrap items-center gap-x-5 gap-y-1 rounded-2xl border border-tgn03-neon/55 bg-tgn03-void/60 py-2 pr-2.5 pl-4 shadow-[0_0_18px_color-mix(in_oklab,var(--color-tgn03-neon)_30%,transparent),inset_0_1px_0_rgb(255_255_255/0.06)] backdrop-blur-xl backdrop-saturate-150 backdrop-brightness-110 before:pointer-events-none before:absolute before:inset-0 before:rounded-[inherit] before:bg-[repeating-linear-gradient(0deg,rgb(255_255_255/0.035)_0_1px,transparent_1px_3px)] not-supports-[backdrop-filter:blur(1px)]:bg-tgn03-void sm:flex-nowrap sm:pl-5">
      <a class="rounded-md text-lg font-bold tracking-[0.08em] text-white [text-shadow:0_0_10px_color-mix(in_oklab,var(--color-tgn03-neon)_70%,transparent)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tgn03-neon" href="#">NEO<span class="text-tgn03-neon">/</span>GRID</a>
      <nav class="max-sm:order-last max-sm:-mx-1 max-sm:w-full max-sm:overflow-x-auto max-sm:[scrollbar-width:none] sm:mx-auto" aria-label="Primary">
        <ul class="flex gap-1">
          <li><a href="#" aria-current="page" class="relative flex h-11 items-center rounded-[10px] px-3.5 font-tgn03-mono text-[13px] font-medium tracking-[0.04em] whitespace-nowrap text-tgn03-ink/85 uppercase transition-[color,text-shadow] duration-150 hover:text-white hover:[text-shadow:0_0_12px_var(--color-tgn03-neon)] aria-[current=page]:text-white aria-[current=page]:after:absolute aria-[current=page]:after:inset-x-3 aria-[current=page]:after:bottom-1.5 aria-[current=page]:after:h-0.5 aria-[current=page]:after:rounded-full aria-[current=page]:after:bg-linear-to-r aria-[current=page]:after:from-transparent aria-[current=page]:after:via-tgn03-neon aria-[current=page]:after:to-transparent aria-[current=page]:after:shadow-[0_0_8px_var(--color-tgn03-neon)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tgn03-neon">Arcade</a></li>
          <li><a href="#" class="relative flex h-11 items-center rounded-[10px] px-3.5 font-tgn03-mono text-[13px] font-medium tracking-[0.04em] whitespace-nowrap text-tgn03-ink/85 uppercase transition-[color,text-shadow] duration-150 hover:text-white hover:[text-shadow:0_0_12px_var(--color-tgn03-neon)] aria-[current=page]:text-white aria-[current=page]:after:absolute aria-[current=page]:after:inset-x-3 aria-[current=page]:after:bottom-1.5 aria-[current=page]:after:h-0.5 aria-[current=page]:after:rounded-full aria-[current=page]:after:bg-linear-to-r aria-[current=page]:after:from-transparent aria-[current=page]:after:via-tgn03-neon aria-[current=page]:after:to-transparent aria-[current=page]:after:shadow-[0_0_8px_var(--color-tgn03-neon)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tgn03-neon">Netrun</a></li>
          <li><a href="#" class="relative flex h-11 items-center rounded-[10px] px-3.5 font-tgn03-mono text-[13px] font-medium tracking-[0.04em] whitespace-nowrap text-tgn03-ink/85 uppercase transition-[color,text-shadow] duration-150 hover:text-white hover:[text-shadow:0_0_12px_var(--color-tgn03-neon)] aria-[current=page]:text-white aria-[current=page]:after:absolute aria-[current=page]:after:inset-x-3 aria-[current=page]:after:bottom-1.5 aria-[current=page]:after:h-0.5 aria-[current=page]:after:rounded-full aria-[current=page]:after:bg-linear-to-r aria-[current=page]:after:from-transparent aria-[current=page]:after:via-tgn03-neon aria-[current=page]:after:to-transparent aria-[current=page]:after:shadow-[0_0_8px_var(--color-tgn03-neon)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tgn03-neon">Market</a></li>
          <li><a href="#" class="relative flex h-11 items-center rounded-[10px] px-3.5 font-tgn03-mono text-[13px] font-medium tracking-[0.04em] whitespace-nowrap text-tgn03-ink/85 uppercase transition-[color,text-shadow] duration-150 hover:text-white hover:[text-shadow:0_0_12px_var(--color-tgn03-neon)] aria-[current=page]:text-white aria-[current=page]:after:absolute aria-[current=page]:after:inset-x-3 aria-[current=page]:after:bottom-1.5 aria-[current=page]:after:h-0.5 aria-[current=page]:after:rounded-full aria-[current=page]:after:bg-linear-to-r aria-[current=page]:after:from-transparent aria-[current=page]:after:via-tgn03-neon aria-[current=page]:after:to-transparent aria-[current=page]:after:shadow-[0_0_8px_var(--color-tgn03-neon)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tgn03-neon">Comms</a></li>
        </ul>
      </nav>
      <a class="flex h-11 items-center rounded-[10px] bg-tgn03-neon px-4.5 text-[13px] font-bold tracking-[0.08em] text-tgn03-void uppercase shadow-[0_0_16px_color-mix(in_oklab,var(--color-tgn03-neon)_55%,transparent)] transition-[translate,box-shadow] duration-150 hover:-translate-y-px hover:shadow-[0_0_28px_var(--color-tgn03-neon)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white motion-reduce:transition-none max-sm:ml-auto" href="#">Jack in</a>
    </header>
    <div class="mx-auto max-w-2xl px-2 pt-12 pb-20 text-tgn03-ink/85 [&_p]:mb-3.5 [&_p]:text-[15px]/[1.65] [&_p]:font-medium [&_p]:text-pretty [&_p]:font-tgn03-mono [&_p]:text-[14px]/[1.75] [&_p]:font-normal [&_:is(h1,h2,h3)]:text-balance [&_h2]:mt-5 [&_h2]:mb-3.5 [&_h2]:text-[22px]/[1.2] [&_h2]:font-extrabold [&_h2]:tracking-[-0.015em] [&_h3]:mt-8 [&_h3]:mb-3 [&_h3]:text-lg/[1.25] [&_h3]:font-bold [&_h3]:tracking-[-0.01em] [&_:is(h2,h3)]:tracking-[0.03em] [&_:is(h2,h3)]:text-white [&_:is(h2,h3)]:[text-shadow:0_0_12px_color-mix(in_oklab,var(--color-tgn03-neon)_60%,transparent)] [&_code]:rounded-md [&_code]:px-1.5 [&_code]:py-0.5 [&_code]:font-tgn03-mono [&_code]:text-[12.5px] [&_code]:font-medium [&_code]:border [&_code]:border-tgn03-neon/30 [&_code]:bg-tgn03-void/55 [&_code]:text-tgn03-neon">
      <h2>Broadcast § live from the grid</h2>
      <p>The smoked-glass bar stays pinned to the top as the scene rolls past. Dark translucent fill dims the colour underneath into a smoked pane rather than washing it out to grey.</p>
      <p>Chained <code>backdrop-filter</code> (blur + saturate + brightness) keeps the sampled hues alive under the tint. Drop the brightness and everything reads muddy; push it too far and the smoke turns milky.</p>
      <p>The neon accent is a single custom property (<code>--neon</code>). Swap it for magenta, toxic green, or hot amber and the whole identity re-skins in one line — border glow, hover text-shadow, and the lit underline all key off it.</p>
      <h3>Signal from the deck</h3>
      <p>Scroll further and the bar keeps its glow, keeps its blur, keeps its promise. Sticky + backdrop-filter is a compositor task, no scroll listener needed. The neon border cost is a single pseudo-element with a coloured box-shadow.</p>
      <p>Cyberpunk glass wants a saturated, contrasty background to blur — over pure dark, the effect disappears. Give it neon signage, gradient meshes, or scanline plates and the smoke reads correctly.</p>
      <p>Add a scanline texture with a <code>repeating-linear-gradient</code> overlay at 3-4% opacity for extra grit; the frost softens it into film-grain rather than lines. Push past 6% and it starts to compete with body text.</p>
      <p>Neon text glow can drop contrast below AA; keep the base link colour bright and treat the glow as decoration, never as the legibility mechanism.</p>
      <h3>Palette recipes worth stealing</h3>
      <p>Cyan cyberpunk (this demo): <code>--neon: oklch(0.82 0.16 195)</code>. Classic Blade Runner cool with high perceptual brightness.</p>
      <p>Synthwave magenta: <code>--neon: oklch(0.7 0.25 340)</code>. Reads hotter over dark blue-purple backgrounds; pair with a Miami-style sunset gradient.</p>
      <p>Toxic green: <code>--neon: oklch(0.85 0.2 130)</code>. The Matrix rain palette; works best over deep blacks with occasional emerald mist.</p>
      <p>Hot amber: <code>--neon: oklch(0.75 0.18 60)</code>. Reads as premium arcade cabinet rather than futurist; good for retro-gaming brand contexts.</p>
      <h3>Where cyberpunk glass belongs</h3>
      <p>Web3 wallet-connect flows use it because their audience expects the aesthetic. NFT marketplaces (OpenSea, Blur, Rainbow) mix it with iridescent card foils.</p>
      <p>Gaming portals (Steam frontends, Epic-store style landing pages) use it to signal “premium experience” without needing prose to say it.</p>
      <p>Cybersecurity SaaS (SentinelOne, Snyk-style dashboards) use a muted variant — the same recipe with saturation dialled down to 100% so it reads as serious rather than playful.</p>
      <p>Dev-tool marketing pages (Cursor, Warp, Zed) use dark glass as their default because their audience runs their desktop in dark mode — the marketing page needs to feel like an extension of the product, not a hostile bright-mode intrusion.</p>
      <p>Streaming platforms use dark glass for player chrome (Spotify's mini-player, Apple Music's now-playing bar) because it lets album art bleed through as ambient colour.</p>
      <p>Keep scrolling — the sticky bar demonstrates its resilience across the full page height.</p>
    </div>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgn03-neon: #00e8e9;
  --color-tgn03-neon: oklch(0.84 0.15 195);
  --color-tgn03-mag: #aa24c5;
  --color-tgn03-mag: oklch(0.55 0.24 320);
  --color-tgn03-ind: #29008d;
  --color-tgn03-ind: oklch(0.3 0.2 280);
  --color-tgn03-sky: #010525;
  --color-tgn03-sky: oklch(0.14 0.07 265);
  --color-tgn03-void: #070d1a;
  --color-tgn03-void: oklch(0.16 0.03 265);
  --color-tgn03-ink: #edf2f8;
  --color-tgn03-ink: oklch(0.96 0.01 250);
  --font-tgn03-display: 'Chakra Petch', system-ui, sans-serif;
  --font-tgn03-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tgn-03 {
  width: 100%;
  min-height: 100svh;
}
```
