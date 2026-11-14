---
source: "codefronts"
url: "https://codefronts.com/components/css-glassmorphism-cards/glassmorphism-blog-post-card-css/"
title: "Glassmorphism Blog Post Card CSS"
section: "components"
category: "css-glassmorphism-cards"
category_name: "CSS Glassmorphism Cards"
description: "Two article cards: a classic cover-top card with a frosted category chip sitting ON the image, hover zoom and an arrow that slides on the same easing — and a…"
has_js: "false"
---

Here's a working CSS Glassmorphism Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Blog Post Card CSS
Source: https://codefronts.com/components/css-glassmorphism-cards/glassmorphism-blog-post-card-css/

Two article cards: a classic cover-top card with a frosted category chip sitting ON the image, hover zoom and an arrow that slides on the same easing — and a full-bleed editorial card where the entire text block is a glass bar that rises to reveal the excerpt.
## HTML
```html
<div class="glz-16-group">
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,[email protected],300..800&family=Instrument+Sans:ital,wght@0,400..700;1,400..700&display=swap" rel="stylesheet">
<section class="glz-16a" aria-label="Glassmorphism blog card demo">
  <a class="glz-16a__card" href="#" onclick="return false">
    <span class="glz-16a__media"><img src="https://images.unsplash.com/photo-1461749280684-dccba630e2f6?q=80&w=900&auto=format&fit=crop" alt="Code on a laptop screen in a dim room" loading="lazy"><b class="glz-16a__chip">CSS Deep-Dive</b></span>
    <span class="glz-16a__body">
      <time class="glz-16a__meta" datetime="2026-07-14">Jul 14, 2026 · 9 min read</time>
      <h3 class="glz-16a__title">backdrop-filter is a rendering budget: spend it like one</h3>
      <p class="glz-16a__ex">Where the blur actually costs you frames, and the three layering rules that keep 60fps on mid-tier phones.</p>
      <span class="glz-16a__foot"><img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?q=80&w=160&auto=format&fit=crop" alt="" loading="lazy"><em>Maya Okafor</em><i class="glz-16a__arrow" aria-hidden="true">↗</i></span>
    </span>
  </a>
</section>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&family=Instrument+Sans:ital,wght@0,400..700;1,400..700&display=swap" rel="stylesheet">
<section class="glz-16b" aria-label="Editorial glass caption card demo">
  <a class="glz-16b__card" href="#" onclick="return false">
    <img class="glz-16b__bg" src="https://images.unsplash.com/photo-1499750310107-5fef28a66643?q=80&w=900&auto=format&fit=crop" alt="Writing desk with coffee and a notebook by a window" loading="lazy">
    <span class="glz-16b__caption">
      <b class="glz-16b__kicker">Essay · Craft</b>
      <span class="glz-16b__title">Slow interfaces are a feature</span>
      <span class="glz-16b__reveal"><span class="glz-16b__inner"><span class="glz-16b__ex">Speed is table stakes; pacing is design. On latency, ritual, and why your reader's thumb needs a resting place.</span><em class="glz-16b__cta">Read the essay →</em></span></span>
    </span>
  </a>
  <p class="glz-16b__hint" aria-hidden="true">hover the card</p>
</section>
</div>
```
## CSS
```css
.glz-16-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.glz-16-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.glz-16a,
.glz-16a *,
.glz-16a *::before,
.glz-16a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.glz-16a {
  position: relative;
  overflow: hidden;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #0e1116;
  font-family: 'Instrument Sans',system-ui,sans-serif;
}

.glz-16a::before {
  content: "";
  position: absolute;
  width: 56vmin;
  height: 56vmin;
  border-radius: 50%;
  background: oklch(0.55 0.15 250);
  filter: blur(95px);
  opacity: .5;
  top: -12%;
  left: -6%;
}

.glz-16a::after {
  content: "";
  position: absolute;
  width: 44vmin;
  height: 44vmin;
  border-radius: 50%;
  background: oklch(0.6 0.14 150);
  filter: blur(95px);
  opacity: .4;
  bottom: -12%;
  right: -4%;
}

.glz-16a__card {
  position: relative;
  z-index: 1;
  display: block;
  width: min(360px,100%);
  border-radius: 24px;
  overflow: hidden;
  text-decoration: none;
  color: #eef2f6;
  background: linear-gradient(165deg,rgba(255,255,255,.12),rgba(255,255,255,.04));
  backdrop-filter: blur(22px) saturate(170%);
  -webkit-backdrop-filter: blur(22px) saturate(170%);
  border: 1px solid rgba(255,255,255,.18);
  box-shadow: 0 30px 62px -26px rgba(0,0,0,.8),inset 0 1px 0 rgba(255,255,255,.22);
  transition: transform .35s ease,box-shadow .35s ease;
}

.glz-16a__card:hover {
  transform: translateY(-6px);
  box-shadow: 0 44px 78px -28px rgba(0,0,0,.85),inset 0 1px 0 rgba(255,255,255,.22);
}

.glz-16a__card:focus-visible {
  outline: 2px solid oklch(0.75 0.14 230);
  outline-offset: 4px;
}

.glz-16a__media {
  position: relative;
  display: block;
  aspect-ratio: 16/9.5;
  overflow: hidden;
  background: linear-gradient(140deg,#20304a,#1a2438);
}

.glz-16a__media img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform .6s cubic-bezier(.2,.7,.2,1);
}

.glz-16a__card:hover .glz-16a__media img {
  transform: scale(1.07);
}

.glz-16a__chip {
  position: absolute;
  top: 14px;
  left: 14px;
  font: 700 10.5px 'Instrument Sans',sans-serif;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: #fff;
  padding: 7px 12px;
  border-radius: 99px;
  background: rgba(255,255,255,.2);
  backdrop-filter: blur(10px) saturate(160%);
  -webkit-backdrop-filter: blur(10px) saturate(160%);
  border: 1px solid rgba(255,255,255,.4);
}

.glz-16a__body {
  display: block;
  padding: 20px 22px 22px;
}

.glz-16a__meta {
  font-size: 11.5px;
  letter-spacing: .05em;
  color: rgba(238,242,246,.5);
}

.glz-16a__title {
  margin-top: 9px;
  font-family: 'Bricolage Grotesque',sans-serif;
  font-size: 19.5px;
  font-weight: 700;
  line-height: 1.3;
  letter-spacing: -.015em;
  text-wrap: pretty;
}

.glz-16a__ex {
  margin-top: 9px;
  font-size: 13.5px;
  line-height: 1.55;
  color: rgba(238,242,246,.62);
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.glz-16a__foot {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-top: 16px;
  padding-top: 16px;
  border-top: 1px solid rgba(255,255,255,.12);
}

.glz-16a__foot img {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  object-fit: cover;
  background: #2c3648;
}

.glz-16a__foot em {
  font-style: normal;
  font-size: 12.5px;
  font-weight: 600;
  color: rgba(238,242,246,.75);
}

.glz-16a__arrow {
  margin-left: auto;
  width: 32px;
  height: 32px;
  display: grid;
  place-items: center;
  border-radius: 10px;
  font-style: normal;
  background: rgba(255,255,255,.1);
  border: 1px solid rgba(255,255,255,.2);
  transition: transform .3s cubic-bezier(.2,.7,.2,1),background .3s ease;
}

.glz-16a__card:hover .glz-16a__arrow {
  transform: translate(3px,-3px);
  background: rgba(255,255,255,.22);
}

@supports not ((backdrop-filter: blur(2px)) or (-webkit-backdrop-filter: blur(2px))) {
  .glz-16a__card {
    background: rgba(20,25,34,.94);
  }

  .glz-16a__chip {
    background: rgba(30,36,50,.8);
  }
}

@media (prefers-reduced-motion: reduce) {
  .glz-16a__card,
    .glz-16a__media img,
    .glz-16a__arrow {
    transition: none;
  }
}

.glz-16b,
.glz-16b *,
.glz-16b *::before,
.glz-16b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.glz-16b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 22px;
  padding: 48px 24px;
  background: linear-gradient(170deg,#efe9df,#e5dccc);
  font-family: 'Instrument Sans',system-ui,sans-serif;
}

.glz-16b__card {
  position: relative;
  display: block;
  width: min(380px,100%);
  aspect-ratio: 4/4.7;
  border-radius: 26px;
  overflow: hidden;
  text-decoration: none;
  box-shadow: 0 34px 66px -28px rgba(90,70,40,.55);
  transition: transform .35s ease;
}

.glz-16b__card:hover {
  transform: translateY(-6px);
}

.glz-16b__card:focus-visible {
  outline: 2px solid #6b4b2a;
  outline-offset: 4px;
}

.glz-16b__bg {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  background: linear-gradient(150deg,#caa87c,#8f6b48);
  transition: transform .7s cubic-bezier(.2,.7,.2,1);
}

.glz-16b__card:hover .glz-16b__bg {
  transform: scale(1.06);
}

.glz-16b__caption {
  position: absolute;
  inset: auto 12px 12px;
  display: block;
  padding: 18px 20px;
  border-radius: 18px;
  color: #fff;
  background: linear-gradient(170deg,rgba(40,28,16,.4),rgba(40,28,16,.55));
  backdrop-filter: blur(16px) saturate(150%);
  -webkit-backdrop-filter: blur(16px) saturate(150%);
  border: 1px solid rgba(255,255,255,.3);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.3);
}

.glz-16b__kicker {
  font-size: 10px;
  font-weight: 700;
  letter-spacing: .22em;
  text-transform: uppercase;
  color: oklch(0.88 0.08 80);
}

.glz-16b__title {
  display: block;
  margin-top: 8px;
  font-family: 'Playfair Display',Georgia,serif;
  font-size: 23px;
  line-height: 1.25;
  font-weight: 600;
  letter-spacing: .005em;
  text-wrap: pretty;
}

.glz-16b__reveal {
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows .45s cubic-bezier(.2,.7,.2,1);
}

.glz-16b__card:hover .glz-16b__reveal,
.glz-16b__card:focus-visible .glz-16b__reveal {
  grid-template-rows: 1fr;
}

.glz-16b__inner {
  display: block;
  min-height: 0;
  overflow: hidden;
}

.glz-16b__ex {
  display: block;
  padding-top: 10px;
  font-size: 13px;
  line-height: 1.6;
  color: rgba(255,255,255,.82);
}

.glz-16b__cta {
  display: inline-block;
  margin-top: 12px;
  font-style: normal;
  font-size: 12.5px;
  font-weight: 700;
  color: oklch(0.88 0.08 80);
}

.glz-16b__hint {
  font-size: 11px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: rgba(90,70,40,.45);
}

@supports not ((backdrop-filter: blur(2px)) or (-webkit-backdrop-filter: blur(2px))) {
  .glz-16b__caption {
    background: rgba(40,28,16,.85);
  }
}

@media (prefers-reduced-motion: reduce) {
  .glz-16b__card,
    .glz-16b__bg,
    .glz-16b__reveal {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the whole card is one <a>; the chip blurs the cover it overlaps, and the zoom scales only the image inside its overflow:hidden frame. */

/* No JavaScript — the excerpt expands with the grid-template-rows 0fr→1fr trick (height-to-auto, no measuring), synced to the cover zoom. */
```
