---
source: "codefronts"
url: "https://codefronts.com/components/css-glassmorphism-cards/glassmorphism-feature-showcase-card/"
title: "Glassmorphism Feature Showcase Card"
section: "components"
category: "css-glassmorphism-cards"
category_name: "CSS Glassmorphism Cards"
description: "Feature marketing, two densities: a trio of icon cards whose top edge lights up with a travelling gradient on hover, and a single hero showcase where…"
has_js: "false"
---

Here's a working CSS Glassmorphism Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Feature Showcase Card
Source: https://codefronts.com/components/css-glassmorphism-cards/glassmorphism-feature-showcase-card/

Feature marketing, two densities: a trio of icon cards whose top edge lights up with a travelling gradient on hover, and a single hero showcase where floating glass chips orbit a central claim on layered parallax drifts — the “everything app” card.
## HTML
```html
<div class="glz-17-group">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="glz-17a" aria-label="Feature cards with edge light hover">
  <div class="glz-17a__grid">
    <article class="glz-17a__feat"><span class="glz-17a__ic"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M13 3 5 13h5l-1 8 8-11h-5z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg></span><h3>Instant previews</h3><p>Every edit paints in under a frame — no build step between you and the pixels.</p><em>Learn more →</em></article>
    <article class="glz-17a__feat"><span class="glz-17a__ic"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3v18M3 12h18M6 6l12 12M18 6 6 18" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg></span><h3>Merge without fear</h3><p>Branch-aware components diff visually, so design reviews read like pull requests.</p><em>Learn more →</em></article>
    <article class="glz-17a__feat"><span class="glz-17a__ic"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="4" y="4" width="16" height="16" rx="3" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M4 10h16M10 10v10" fill="none" stroke="currentColor" stroke-width="1.8"/></svg></span><h3>Tokens that travel</h3><p>One palette feeds web, iOS and email. Change it once; ship it everywhere.</p><em>Learn more →</em></article>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="glz-17b" aria-label="Hero feature card with floating chips">
  <article class="glz-17b__hero">
    <span class="glz-17b__chip" style="top:12%;left:6%;--dur:8s;--d:-2s">⌘K everywhere</span>
    <span class="glz-17b__chip" style="top:20%;right:8%;--dur:10s;--d:-5s">Offline-first</span>
    <span class="glz-17b__chip" style="bottom:26%;left:9%;--dur:9s;--d:-1s">Realtime cursors</span>
    <span class="glz-17b__chip" style="bottom:14%;right:12%;--dur:11s;--d:-6s">SOC 2 · GDPR</span>
    <p class="glz-17b__eyebrow">Why teams switch</p>
    <h2 class="glz-17b__claim">One canvas.<br>Every deliverable.</h2>
    <p class="glz-17b__sub">Docs, decks and design files stop being three apps pretending to talk.</p>
    <button type="button" class="glz-17b__cta">See it in 90 seconds</button>
  </article>
</section>
</div>
```
## CSS
```css
.glz-17-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.glz-17-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.glz-17a,
.glz-17a *,
.glz-17a *::before,
.glz-17a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.glz-17a {
  position: relative;
  overflow: hidden;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 64px 24px;
  background: #0b0e1a;
  font-family: 'Space Grotesk',system-ui,sans-serif;
}

.glz-17a::before {
  content: "";
  position: absolute;
  width: 70vmin;
  height: 70vmin;
  border-radius: 50%;
  background: radial-gradient(circle,oklch(0.5 0.17 265/.5),transparent 70%);
  top: -20%;
  left: 24%;
  filter: blur(50px);
}

.glz-17a::after {
  content: "";
  position: absolute;
  width: 50vmin;
  height: 50vmin;
  border-radius: 50%;
  background: radial-gradient(circle,oklch(0.6 0.14 190/.4),transparent 70%);
  bottom: -16%;
  right: 10%;
  filter: blur(60px);
}

.glz-17a__grid {
  position: relative;
  z-index: 1;
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(240px,1fr));
  gap: 18px;
  width: min(880px,100%);
}

.glz-17a__feat {
  position: relative;
  overflow: hidden;
  padding: 26px 24px;
  border-radius: 22px;
  color: #e9edfc;
  background: linear-gradient(165deg,rgba(255,255,255,.11),rgba(255,255,255,.03));
  backdrop-filter: blur(20px) saturate(170%);
  -webkit-backdrop-filter: blur(20px) saturate(170%);
  border: 1px solid rgba(255,255,255,.16);
  box-shadow: 0 26px 54px -26px rgba(0,0,0,.8),inset 0 1px 0 rgba(255,255,255,.2);
  transition: transform .35s ease,border-color .35s ease;
}

.glz-17a__feat::before {
  content: "";
  position: absolute;
  top: -1px;
  left: -40%;
  right: -40%;
  height: 2px;
  background: linear-gradient(90deg,transparent,oklch(0.85 0.12 210) 45%,oklch(0.75 0.16 290) 55%,transparent);
  transform: translateX(-30%);
  opacity: 0;
  transition: transform .7s ease,opacity .4s ease;
}

.glz-17a__feat:hover {
  transform: translateY(-6px);
  border-color: rgba(255,255,255,.28);
}

.glz-17a__feat:hover::before {
  transform: translateX(30%);
  opacity: 1;
}

.glz-17a__ic {
  width: 44px;
  height: 44px;
  display: grid;
  place-items: center;
  border-radius: 14px;
  color: oklch(0.85 0.12 210);
  background: oklch(0.85 0.12 210/.1);
  border: 1px solid oklch(0.85 0.12 210/.3);
  transition: color .35s ease,background .35s ease;
}

.glz-17a__feat:hover .glz-17a__ic {
  color: oklch(0.8 0.15 290);
  background: oklch(0.8 0.15 290/.12);
}

.glz-17a__ic svg {
  width: 21px;
  height: 21px;
}

.glz-17a__feat h3 {
  margin-top: 18px;
  font-size: 17.5px;
  font-weight: 600;
  letter-spacing: -.01em;
}

.glz-17a__feat p {
  margin-top: 9px;
  font-size: 13.5px;
  line-height: 1.6;
  color: rgba(233,237,252,.6);
  text-wrap: pretty;
}

.glz-17a__feat em {
  display: inline-block;
  margin-top: 16px;
  font-style: normal;
  font-size: 12.5px;
  font-weight: 700;
  color: oklch(0.85 0.12 210);
}

@supports not ((backdrop-filter: blur(2px)) or (-webkit-backdrop-filter: blur(2px))) {
  .glz-17a__feat {
    background: rgba(17,21,36,.94);
  }
}

@media (prefers-reduced-motion: reduce) {
  .glz-17a__feat,
    .glz-17a__feat::before,
    .glz-17a__ic {
    transition: none;
  }
}

.glz-17b,
.glz-17b *,
.glz-17b *::before,
.glz-17b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.glz-17b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  position: relative;
  overflow: hidden;
  background: radial-gradient(120% 100% at 50% 120%,#241a3d,#0e0a1c 60%);
}

.glz-17b::before {
  content: "";
  position: absolute;
  inset: 0;
  background: radial-gradient(46% 38% at 30% 20%,oklch(0.6 0.2 310/.4),transparent 70%),radial-gradient(40% 34% at 76% 74%,oklch(0.65 0.16 220/.35),transparent 70%);
}

.glz-17b__hero {
  position: relative;
  z-index: 1;
  width: min(560px,100%);
  min-height: 380px;
  display: grid;
  place-content: center;
  text-align: center;
  padding: 56px 32px;
  border-radius: 30px;
  color: #f1edfc;
  font-family: 'Space Grotesk',system-ui,sans-serif;
  background: linear-gradient(165deg,rgba(255,255,255,.11),rgba(255,255,255,.03));
  backdrop-filter: blur(24px) saturate(170%);
  -webkit-backdrop-filter: blur(24px) saturate(170%);
  border: 1px solid rgba(255,255,255,.2);
  box-shadow: 0 40px 80px -30px rgba(0,0,0,.85),inset 0 1px 0 rgba(255,255,255,.24);
}

.glz-17b__chip {
  position: absolute;
  font-size: 11.5px;
  font-weight: 600;
  letter-spacing: .04em;
  padding: 8px 13px;
  border-radius: 99px;
  color: #fff;
  background: rgba(255,255,255,.12);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(255,255,255,.3);
  box-shadow: 0 12px 26px -12px rgba(0,0,0,.7);
  animation: glz-17b-float var(--dur) ease-in-out var(--d) infinite alternate;
}

.glz-17b__eyebrow {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .28em;
  text-transform: uppercase;
  color: oklch(0.8 0.14 310);
}

.glz-17b__claim {
  margin-top: 14px;
  font-size: clamp(30px,5.6vw,44px);
  font-weight: 700;
  line-height: 1.08;
  letter-spacing: -.03em;
}

.glz-17b__sub {
  margin-top: 14px;
  font-size: 14.5px;
  line-height: 1.6;
  color: rgba(241,237,252,.62);
  max-width: 38ch;
  justify-self: center;
  text-wrap: pretty;
}

.glz-17b__cta {
  margin: 26px auto 0;
  padding: 14px 24px;
  border: none;
  border-radius: 99px;
  background: linear-gradient(120deg,oklch(0.72 0.19 310),oklch(0.7 0.16 250));
  color: #fff;
  font: 700 14px 'Space Grotesk',sans-serif;
  cursor: pointer;
  box-shadow: 0 18px 36px -14px oklch(0.72 0.19 310/.8);
  transition: transform .2s ease,box-shadow .2s ease;
}

.glz-17b__cta:hover {
  transform: translateY(-2px);
  box-shadow: 0 24px 44px -14px oklch(0.72 0.19 310/.9);
}

.glz-17b__cta:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 3px;
}

@keyframes glz-17b-float {
  from {
    transform: translateY(-7px);
  }

  to {
    transform: translateY(8px);
  }
}

@supports not ((backdrop-filter: blur(2px)) or (-webkit-backdrop-filter: blur(2px))) {
  .glz-17b__hero {
    background: rgba(26,19,44,.94);
  }

  .glz-17b__chip {
    background: rgba(40,32,64,.9);
  }
}

@media (prefers-reduced-motion: reduce) {
  .glz-17b__chip {
    animation: none;
  }

  .glz-17b__cta {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the top-edge light is an oversized gradient pseudo translated across on hover; icons are currentColor SVG strokes so the hue shift is one property. */

/* No JavaScript — every chip shares one float keyframe but gets its own duration + negative delay, so the field never syncs up. */
```
