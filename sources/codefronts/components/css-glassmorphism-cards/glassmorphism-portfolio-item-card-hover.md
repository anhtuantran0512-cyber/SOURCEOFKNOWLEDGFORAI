---
source: "codefronts"
url: "https://codefronts.com/components/css-glassmorphism-cards/glassmorphism-portfolio-item-card-hover/"
title: "Glassmorphism Portfolio Item Card Hover"
section: "components"
category: "css-glassmorphism-cards"
category_name: "CSS Glassmorphism Cards"
description: "Two portfolio tiles: a case-study card whose image wakes from muted grayscale to full colour while a frosted info panel wipes up with role, year and stack —…"
has_js: "false"
---

Here's a working CSS Glassmorphism Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Portfolio Item Card Hover
Source: https://codefronts.com/components/css-glassmorphism-cards/glassmorphism-portfolio-item-card-hover/

Two portfolio tiles: a case-study card whose image wakes from muted grayscale to full colour while a frosted info panel wipes up with role, year and stack — and a duo where a letterboxed glass strip slides in with tags, the pair trading focus via group-dim.
## HTML
```html
<div class="glz-20-group">
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,[email protected],300..800&display=swap" rel="stylesheet">
<section class="glz-20a" aria-label="Portfolio card with color wake hover">
  <a class="glz-20a__tile" href="#" onclick="return false">
    <img src="https://images.unsplash.com/photo-1541701494587-cb58502866ab?q=80&w=900&auto=format&fit=crop" alt="Abstract fluid gradient artwork from the Meridian rebrand" loading="lazy">
    <span class="glz-20a__panel">
      <b class="glz-20a__name">Meridian — brand & app</b>
      <span class="glz-20a__more">
        <em>Lead product designer · 2026</em>
        <span class="glz-20a__tags"><i>Identity</i><i>Design system</i><i>iOS</i></span>
        <u class="glz-20a__cta">View case study ↗</u>
      </span>
    </span>
  </a>
</section>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,[email protected],300..800&display=swap" rel="stylesheet">
<section class="glz-20b" aria-label="Portfolio pair with letterbox captions">
  <div class="glz-20b__pair">
    <a class="glz-20b__tile" href="#" onclick="return false">
      <img src="https://images.unsplash.com/photo-1550745165-9bc0b252726f?q=80&w=800&auto=format&fit=crop" alt="Retro computing hardware still life for the Arcade Archive project" loading="lazy">
      <span class="glz-20b__strip"><b>Arcade Archive</b><em>Web · WebGL · 2025</em></span>
    </a>
    <a class="glz-20b__tile" href="#" onclick="return false">
      <img src="https://images.unsplash.com/photo-1486312338219-ce68d2c6f44d?q=80&w=800&auto=format&fit=crop" alt="Hands on a laptop for the Ledgerly fintech dashboard project" loading="lazy">
      <span class="glz-20b__strip"><b>Ledgerly Dashboard</b><em>Product · Data viz · 2026</em></span>
    </a>
  </div>
</section>
</div>
```
## CSS
```css
.glz-20-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.glz-20-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.glz-20a,
.glz-20a *,
.glz-20a *::before,
.glz-20a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.glz-20a {
  position: relative;
  overflow: hidden;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #0f0d14;
  font-family: 'Bricolage Grotesque',system-ui,sans-serif;
}

.glz-20a::before {
  content: "";
  position: absolute;
  width: 60vmin;
  height: 60vmin;
  border-radius: 50%;
  background: oklch(0.5 0.19 320);
  filter: blur(100px);
  opacity: .45;
  top: -14%;
  right: -4%;
}

.glz-20a::after {
  content: "";
  position: absolute;
  width: 46vmin;
  height: 46vmin;
  border-radius: 50%;
  background: oklch(0.55 0.15 220);
  filter: blur(100px);
  opacity: .4;
  bottom: -12%;
  left: -4%;
}

.glz-20a__tile {
  position: relative;
  z-index: 1;
  display: block;
  width: min(360px,100%);
  aspect-ratio: 4/4.9;
  border-radius: 24px;
  overflow: hidden;
  text-decoration: none;
  border: 1px solid rgba(255,255,255,.18);
  box-shadow: 0 34px 68px -28px rgba(0,0,0,.85);
  transition: transform .35s ease;
}

.glz-20a__tile:hover {
  transform: translateY(-6px);
}

.glz-20a__tile:focus-visible {
  outline: 2px solid oklch(0.78 0.15 320);
  outline-offset: 4px;
}

.glz-20a__tile img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  background: #241f30;
  filter: grayscale(.85) brightness(.82);
  transform: scale(1.01);
  transition: filter .5s ease,transform .65s cubic-bezier(.2,.7,.2,1);
}

.glz-20a__tile:hover img,
.glz-20a__tile:focus-visible img {
  filter: none;
  transform: scale(1.06);
}

.glz-20a__panel {
  position: absolute;
  inset: auto 0 0;
  display: block;
  padding: 14px 20px 20px;
  color: #fff;
  background: linear-gradient(175deg,rgba(20,16,30,.35),rgba(20,16,30,.62));
  backdrop-filter: blur(16px) saturate(160%);
  -webkit-backdrop-filter: blur(16px) saturate(160%);
  border-top: 1px solid rgba(255,255,255,.28);
  transform: translateY(calc(100% - 46px));
  transition: transform .5s cubic-bezier(.2,.8,.25,1);
}

.glz-20a__tile:hover .glz-20a__panel,
.glz-20a__tile:focus-visible .glz-20a__panel {
  transform: none;
}

.glz-20a__name {
  display: block;
  font-size: 17px;
  font-weight: 700;
  letter-spacing: -.01em;
  line-height: 26px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.glz-20a__more {
  display: block;
  padding-top: 10px;
}

.glz-20a__more em {
  display: block;
  font-style: normal;
  font-size: 12px;
  color: rgba(255,255,255,.65);
}

.glz-20a__tags {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-top: 10px;
}

.glz-20a__tags i {
  font-style: normal;
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .08em;
  text-transform: uppercase;
  padding: 5px 9px;
  border-radius: 99px;
  background: rgba(255,255,255,.14);
  border: 1px solid rgba(255,255,255,.3);
}

.glz-20a__cta {
  display: inline-block;
  margin-top: 14px;
  font-size: 12.5px;
  font-weight: 700;
  text-decoration: none;
  color: oklch(0.85 0.12 320);
}

@supports not ((backdrop-filter: blur(2px)) or (-webkit-backdrop-filter: blur(2px))) {
  .glz-20a__panel {
    background: rgba(20,16,30,.88);
  }
}

@media (prefers-reduced-motion: reduce) {
  .glz-20a__tile,
    .glz-20a__tile img,
    .glz-20a__panel {
    transition: none;
  }

  .glz-20a__tile img {
    filter: none;
  }
}

.glz-20b,
.glz-20b *,
.glz-20b *::before,
.glz-20b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.glz-20b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(165deg,#efece5,#e3e6ee);
  font-family: 'Bricolage Grotesque',system-ui,sans-serif;
}

.glz-20b__pair {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 20px;
  width: min(760px,100%);
}

.glz-20b__pair:hover .glz-20b__tile:not(:hover) {
  opacity: .6;
  filter: saturate(.7);
}

.glz-20b__tile {
  position: relative;
  flex: 1 1 300px;
  max-width: 360px;
  aspect-ratio: 4/3;
  border-radius: 22px;
  overflow: hidden;
  display: block;
  box-shadow: 0 28px 56px -26px rgba(70,70,110,.5);
  transition: opacity .35s ease,filter .35s ease,transform .35s ease;
}

.glz-20b__tile:hover {
  transform: translateY(-6px);
}

.glz-20b__tile:focus-visible {
  outline: 2px solid #3c3a6e;
  outline-offset: 4px;
}

.glz-20b__tile img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  background: #c9cadd;
  transition: transform .6s cubic-bezier(.2,.7,.2,1);
}

.glz-20b__tile:hover img {
  transform: scale(1.05);
}

.glz-20b__strip {
  position: absolute;
  left: 12px;
  right: 12px;
  bottom: 12px;
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  gap: 10px;
  padding: 13px 16px;
  border-radius: 14px;
  color: #fff;
  background: rgba(28,26,44,.42);
  backdrop-filter: blur(14px) saturate(150%);
  -webkit-backdrop-filter: blur(14px) saturate(150%);
  border: 1px solid rgba(255,255,255,.35);
  transform: translateY(calc(100% + 14px));
  transition: transform .45s cubic-bezier(.2,.8,.25,1);
}

.glz-20b__tile:hover .glz-20b__strip,
.glz-20b__tile:focus-visible .glz-20b__strip {
  transform: none;
}

.glz-20b__strip b {
  font-size: 14.5px;
  font-weight: 700;
  letter-spacing: -.01em;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.glz-20b__strip em {
  font-style: normal;
  font-size: 10.5px;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: rgba(255,255,255,.7);
  white-space: nowrap;
}

@supports not ((backdrop-filter: blur(2px)) or (-webkit-backdrop-filter: blur(2px))) {
  .glz-20b__strip {
    background: rgba(28,26,44,.88);
  }
}

@media (prefers-reduced-motion: reduce) {
  .glz-20b__tile,
    .glz-20b__tile img,
    .glz-20b__strip {
    transition: none;
  }

  .glz-20b__strip {
    transform: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the image wakes from grayscale while the glass panel (whose resting sliver shows just the title) slides up; both also fire on keyboard focus. */

/* No JavaScript — captions hide fully below the tile and slide in on hover/focus; hovering the pair dims the neighbour so one project holds the room. */
```
