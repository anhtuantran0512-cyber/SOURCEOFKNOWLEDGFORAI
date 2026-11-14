---
source: "codefronts"
url: "https://codefronts.com/components/css-glassmorphism-cards/glassmorphism-service-card-grid-layout/"
title: "Glassmorphism Service Card Grid Layout"
section: "components"
category: "css-glassmorphism-cards"
category_name: "CSS Glassmorphism Cards"
description: "Two agency grids: a 2×2 with giant ghost numerals and an accent underline that draws on hover, and a spotlight grid where the hovered card blooms a radial…"
has_js: "false"
---

Here's a working CSS Glassmorphism Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Service Card Grid Layout
Source: https://codefronts.com/components/css-glassmorphism-cards/glassmorphism-service-card-grid-layout/

Two agency grids: a 2×2 with giant ghost numerals and an accent underline that draws on hover, and a spotlight grid where the hovered card blooms a radial glow from a CSS-variable position while its siblings dim via a group-hover trick — pure CSS, no pointer math.
## HTML
```html
<div class="glz-18-group">
<link href="https://fonts.googleapis.com/css2?family=Archivo:ital,wght@0,400..900;1,400..900&display=swap" rel="stylesheet">
<section class="glz-18a" aria-label="Service cards with ghost numerals">
  <div class="glz-18a__wrap">
    <header class="glz-18a__head"><h2>What we do</h2><p>Four disciplines, one retainer.</p></header>
    <div class="glz-18a__grid">
      <article class="glz-18a__card" style="--acc:oklch(0.8 0.14 210)"><h3>Brand systems</h3><p>Identity, voice and tokens engineered to survive their third rebrand.</p><em>From $12k →</em></article>
      <article class="glz-18a__card" style="--acc:oklch(0.78 0.16 300)"><h3>Product design</h3><p>Flows, prototypes and specs your engineers won't quietly redesign.</p><em>From $18k →</em></article>
      <article class="glz-18a__card" style="--acc:oklch(0.82 0.15 160)"><h3>Design engineering</h3><p>Design systems shipped as code — tokens, docs, CI and all.</p><em>From $22k →</em></article>
      <article class="glz-18a__card" style="--acc:oklch(0.8 0.14 60)"><h3>Motion & 3D</h3><p>Product film, UI motion and WebGL moments that stay under budget.</p><em>From $9k →</em></article>
    </div>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Archivo:ital,wght@0,400..900;1,400..900&display=swap" rel="stylesheet">
<section class="glz-18b" aria-label="Service grid with sibling dimming">
  <div class="glz-18b__grid">
    <article class="glz-18b__card"><span class="glz-18b__ic" aria-hidden="true">◈</span><h3>Audits</h3><p>A 10-day teardown of your funnel, stack and design debt.</p></article>
    <article class="glz-18b__card"><span class="glz-18b__ic" aria-hidden="true">▣</span><h3>Sprints</h3><p>Two-week build cycles with a demo every Friday, no exceptions.</p></article>
    <article class="glz-18b__card"><span class="glz-18b__ic" aria-hidden="true">◎</span><h3>Retainers</h3><p>A senior pod embedded in your Slack, shipping weekly.</p></article>
    <article class="glz-18b__card"><span class="glz-18b__ic" aria-hidden="true">✦</span><h3>Workshops</h3><p>Your team, our playbooks — hands-on, on-site or remote.</p></article>
    <article class="glz-18b__card"><span class="glz-18b__ic" aria-hidden="true">◭</span><h3>Advisory</h3><p>Fractional design leadership for seed to Series B.</p></article>
    <article class="glz-18b__card"><span class="glz-18b__ic" aria-hidden="true">⬡</span><h3>Tooling</h3><p>Internal Figma plugins and CI checks that guard the system.</p></article>
  </div>
  <p class="glz-18b__hint" aria-hidden="true">hover a card — siblings step back</p>
</section>
</div>
```
## CSS
```css
.glz-18-group {
  display: flex;
  flex-direction: column;
  width: 100%;
}

.glz-18-group > section {
  width: 100%;
}

.glz-18a,
.glz-18a *,
.glz-18a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.glz-18a {
  position: relative;
  overflow: hidden;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 64px 24px;
  background: #0d0f16;
  font-family: 'Archivo',system-ui,sans-serif;
}

.glz-18a::before {
  content: "";
  position: absolute;
  width: 64vmin;
  height: 64vmin;
  border-radius: 50%;
  background: oklch(0.5 0.15 265);
  filter: blur(100px);
  opacity: .5;
  top: -16%;
  right: 2%;
}

.glz-18a::after {
  content: "";
  position: absolute;
  width: 48vmin;
  height: 48vmin;
  border-radius: 50%;
  background: oklch(0.55 0.14 180);
  filter: blur(100px);
  opacity: .4;
  bottom: -14%;
  left: 0;
}

.glz-18a__wrap {
  position: relative;
  z-index: 1;
  width: min(820px,100%);
}

.glz-18a__head {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  gap: 14px;
  flex-wrap: wrap;
  margin-bottom: 28px;
}

.glz-18a__head h2 {
  color: #eef0f8;
  font-size: clamp(24px,3.4vw,34px);
  font-weight: 800;
  letter-spacing: -.02em;
}

.glz-18a__head p {
  color: rgba(238,240,248,.5);
  font-size: 13px;
}

.glz-18a__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(250px,1fr));
  gap: 16px;
  counter-reset: glz18a;
}

.glz-18a__card {
  position: relative;
  overflow: hidden;
  counter-increment: glz18a;
  padding: 26px 24px 22px;
  border-radius: 22px;
  color: #edeff8;
  background: linear-gradient(165deg,rgba(255,255,255,.11),rgba(255,255,255,.03));
  backdrop-filter: blur(20px) saturate(170%);
  -webkit-backdrop-filter: blur(20px) saturate(170%);
  border: 1px solid rgba(255,255,255,.15);
  box-shadow: 0 26px 54px -26px rgba(0,0,0,.8),inset 0 1px 0 rgba(255,255,255,.2);
  transition: transform .35s ease,border-color .35s ease;
}

.glz-18a__card::before {
  content: counter(glz18a,decimal-leading-zero) / "";
  position: absolute;
  top: -18px;
  right: 2px;
  font-size: 96px;
  font-weight: 900;
  letter-spacing: -.05em;
  color: rgba(255,255,255,.07);
  pointer-events: none;
}

.glz-18a__card:hover {
  transform: translateY(-6px);
  border-color: color-mix(in oklab,var(--acc) 55%,transparent);
}

.glz-18a__card h3 {
  font-size: 18px;
  font-weight: 800;
  letter-spacing: -.01em;
  padding-bottom: 10px;
  position: relative;
  display: inline-block;
}

.glz-18a__card h3::after {
  content: "";
  position: absolute;
  left: 0;
  bottom: 0;
  width: 100%;
  height: 2.5px;
  border-radius: 2px;
  background: var(--acc);
  transform: scaleX(0);
  transform-origin: left;
  transition: transform .4s cubic-bezier(.2,.7,.2,1);
}

.glz-18a__card:hover h3::after {
  transform: scaleX(1);
}

.glz-18a__card p {
  margin-top: 10px;
  font-size: 13.5px;
  line-height: 1.6;
  color: rgba(237,239,248,.6);
  text-wrap: pretty;
  max-width: 34ch;
}

.glz-18a__card em {
  display: inline-block;
  margin-top: 16px;
  font-style: normal;
  font-size: 12.5px;
  font-weight: 800;
  color: var(--acc);
}

@supports not ((backdrop-filter: blur(2px)) or (-webkit-backdrop-filter: blur(2px))) {
  .glz-18a__card {
    background: rgba(19,22,32,.94);
  }
}

@media (prefers-reduced-motion: reduce) {
  .glz-18a__card,
    .glz-18a__card h3::after {
    transition: none;
  }
}

.glz-18b,
.glz-18b *,
.glz-18b *::before,
.glz-18b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.glz-18b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 24px;
  padding: 64px 24px;
  position: relative;
  overflow: hidden;
  background: linear-gradient(210deg,#160f1e,#0e1420);
}

.glz-18b::before {
  content: "";
  position: absolute;
  inset: 0;
  background: radial-gradient(44% 40% at 24% 20%,oklch(0.55 0.19 330/.35),transparent 70%),radial-gradient(42% 36% at 80% 82%,oklch(0.55 0.15 220/.35),transparent 70%);
}

.glz-18b__grid {
  position: relative;
  z-index: 1;
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(230px,1fr));
  gap: 14px;
  width: min(860px,100%);
}

.glz-18b__card {
  padding: 24px 22px;
  border-radius: 20px;
  color: #f1ecf6;
  font-family: 'Archivo',system-ui,sans-serif;
  background: linear-gradient(165deg,rgba(255,255,255,.1),rgba(255,255,255,.03));
  backdrop-filter: blur(18px) saturate(170%);
  -webkit-backdrop-filter: blur(18px) saturate(170%);
  border: 1px solid rgba(255,255,255,.14);
  box-shadow: 0 24px 50px -24px rgba(0,0,0,.8),inset 0 1px 0 rgba(255,255,255,.18);
  transition: opacity .35s ease,filter .35s ease,transform .35s ease,border-color .35s ease;
}

.glz-18b__grid:hover .glz-18b__card {
  opacity: .5;
  filter: saturate(.6);
}

.glz-18b__grid:hover .glz-18b__card:hover {
  opacity: 1;
  filter: none;
  transform: translateY(-6px);
  border-color: oklch(0.75 0.17 330/.55);
  box-shadow: 0 34px 64px -24px oklch(0.55 0.19 330/.5),inset 0 1px 0 rgba(255,255,255,.22);
}

.glz-18b__ic {
  width: 38px;
  height: 38px;
  display: grid;
  place-items: center;
  border-radius: 12px;
  font-size: 15px;
  color: oklch(0.82 0.15 330);
  background: oklch(0.82 0.15 330/.12);
  border: 1px solid oklch(0.82 0.15 330/.3);
}

.glz-18b__card h3 {
  margin-top: 14px;
  font-size: 16.5px;
  font-weight: 800;
  letter-spacing: -.01em;
}

.glz-18b__card p {
  margin-top: 8px;
  font-size: 12.5px;
  line-height: 1.55;
  color: rgba(241,236,246,.6);
  text-wrap: pretty;
}

.glz-18b__hint {
  position: relative;
  z-index: 1;
  font: 600 11px 'Archivo',sans-serif;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: rgba(220,205,235,.4);
}

@supports not ((backdrop-filter: blur(2px)) or (-webkit-backdrop-filter: blur(2px))) {
  .glz-18b__card {
    background: rgba(24,18,32,.94);
  }
}

@media (prefers-reduced-motion: reduce) {
  .glz-18b__card {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — numerals come from a CSS counter with alternative-text syntax (content:… / "") so screen readers skip them; underlines draw with scaleX. */

/* No JavaScript — .grid:hover dims all cards, .card:hover restores itself: the entire spotlight system is two selectors. */
```
