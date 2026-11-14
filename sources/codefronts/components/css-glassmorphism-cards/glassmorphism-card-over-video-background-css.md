---
source: "codefronts"
url: "https://codefronts.com/components/css-glassmorphism-cards/glassmorphism-card-over-video-background-css/"
title: "Glassmorphism Card Over Video Background CSS"
section: "components"
category: "css-glassmorphism-cards"
category_name: "CSS Glassmorphism Cards"
description: "Glass over motion, done responsibly: a hero card frosting a real looping <video> (poster + gradient underlay so nothing ever looks broken), and the…"
has_js: "false"
---

Here's a working CSS Glassmorphism Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Card Over Video Background CSS
Source: https://codefronts.com/components/css-glassmorphism-cards/glassmorphism-card-over-video-background-css/

Glass over motion, done responsibly: a hero card frosting a real looping <video> (poster + gradient underlay so nothing ever looks broken), and the zero-asset alternative — a pure-CSS “footage” layer of drifting aurora gradients that gives you the cinematic energy with no network cost.
## HTML
```html
<div class="glz-24-group">
<link href="https://fonts.googleapis.com/css2?family=Archivo:ital,wght@0,400..900;1,400..900&display=swap" rel="stylesheet">
<section class="glz-24a" aria-label="Glass card over looping video">
  <video class="glz-24a__video" autoplay muted loop playsinline poster="https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?q=80&w=1600&auto=format&fit=crop" aria-hidden="true"><source src="https://storage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4" type="video/mp4"></video>
  <div class="glz-24a__scrim" aria-hidden="true"></div>
  <article class="glz-24a__card">
    <span class="glz-24a__live">● Live footage behind this glass</span>
    <h2>Shot on location.<br>Blurred on the GPU.</h2>
    <p>backdrop-filter re-frosts every frame of the loop underneath — poster and gradient layers make sure it never paints black.</p>
    <div class="glz-24a__row"><button type="button" class="glz-24a__cta">Watch the film</button><button type="button" class="glz-24a__ghost">Behind the scenes</button></div>
  </article>
</section>
<link href="https://fonts.googleapis.com/css2?family=Archivo:ital,wght@0,400..900;1,400..900&display=swap" rel="stylesheet">
<section class="glz-24b" aria-label="Glass card over CSS-only animated background">
  <div class="glz-24b__aurora" aria-hidden="true"><i></i><i></i><i></i></div>
  <article class="glz-24b__card">
    <span class="glz-24b__chip">0 KB of video</span>
    <h2>Same cinema,<br>no download</h2>
    <p>Three blurred gradients on 26-second drifts stand in for footage — your reduced-data and offline fallback that still sells the frost.</p>
    <button type="button">Use this instead →</button>
  </article>
</section>
</div>
```
## CSS
```css
.glz-24-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.glz-24-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.glz-24a,
.glz-24a *,
.glz-24a *::before,
.glz-24a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.glz-24a {
  position: relative;
  overflow: hidden;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(160deg,#3a2a1c,#141018 70%);
  font-family: 'Archivo',system-ui,sans-serif;
}

.glz-24a__video {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.glz-24a__scrim {
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg,rgba(10,8,14,.35),rgba(10,8,14,.6));
}

.glz-24a__card {
  position: relative;
  z-index: 1;
  width: min(480px,100%);
  padding: 36px 34px;
  border-radius: 26px;
  color: #fbf6ef;
  background: linear-gradient(165deg,rgba(255,255,255,.14),rgba(255,255,255,.05));
  backdrop-filter: blur(22px) saturate(170%);
  -webkit-backdrop-filter: blur(22px) saturate(170%);
  border: 1px solid rgba(255,255,255,.3);
  box-shadow: 0 40px 80px -30px rgba(0,0,0,.85),inset 0 1px 0 rgba(255,255,255,.32);
}

.glz-24a__live {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 10.5px;
  font-weight: 800;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: oklch(0.82 0.16 40);
  animation: glz-24a-blink 2s ease-in-out infinite;
}

.glz-24a__card h2 {
  margin-top: 14px;
  font-size: clamp(26px,4.6vw,36px);
  font-weight: 900;
  line-height: 1.1;
  letter-spacing: -.025em;
}

.glz-24a__card p {
  margin-top: 14px;
  font-size: 14px;
  line-height: 1.65;
  color: rgba(251,246,239,.72);
  text-wrap: pretty;
}

.glz-24a__row {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  margin-top: 24px;
}

.glz-24a__cta {
  padding: 14px 22px;
  border: none;
  border-radius: 13px;
  background: #fbf6ef;
  color: #1c140c;
  font: 800 14px 'Archivo',sans-serif;
  cursor: pointer;
  transition: transform .2s ease,box-shadow .2s ease;
}

.glz-24a__cta:hover {
  transform: translateY(-2px);
  box-shadow: 0 16px 30px -12px rgba(251,246,239,.5);
}

.glz-24a__ghost {
  padding: 14px 20px;
  border: 1px solid rgba(255,255,255,.35);
  border-radius: 13px;
  background: rgba(255,255,255,.08);
  color: #fbf6ef;
  font: 700 14px 'Archivo',sans-serif;
  cursor: pointer;
  transition: background .25s ease;
}

.glz-24a__ghost:hover {
  background: rgba(255,255,255,.18);
}

.glz-24a__cta:focus-visible,
.glz-24a__ghost:focus-visible {
  outline: 2px solid oklch(0.82 0.16 40);
  outline-offset: 3px;
}

@keyframes glz-24a-blink {
  50% {
    opacity: .55;
  }
}

@supports not ((backdrop-filter: blur(2px)) or (-webkit-backdrop-filter: blur(2px))) {
  .glz-24a__card {
    background: rgba(28,20,14,.9);
  }
}

@media (prefers-reduced-motion: reduce) {
  .glz-24a__live {
    animation: none;
  }
}

.glz-24b,
.glz-24b *,
.glz-24b *::before,
.glz-24b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.glz-24b {
  position: relative;
  overflow: hidden;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #070a12;
  font-family: 'Archivo',system-ui,sans-serif;
}

.glz-24b__aurora i {
  position: absolute;
  border-radius: 50%;
  filter: blur(70px);
  mix-blend-mode: screen;
}

.glz-24b__aurora i:nth-child(1) {
  width: 70vmin;
  height: 70vmin;
  background: oklch(0.55 0.2 280/.8);
  top: -16%;
  left: -8%;
  animation: glz-24b-d1 26s ease-in-out infinite alternate;
}

.glz-24b__aurora i:nth-child(2) {
  width: 58vmin;
  height: 58vmin;
  background: oklch(0.65 0.17 190/.7);
  bottom: -14%;
  right: -6%;
  animation: glz-24b-d2 22s ease-in-out infinite alternate;
}

.glz-24b__aurora i:nth-child(3) {
  width: 44vmin;
  height: 44vmin;
  background: oklch(0.68 0.19 350/.55);
  top: 36%;
  left: 44%;
  animation: glz-24b-d3 30s ease-in-out infinite alternate;
}

.glz-24b__card {
  position: relative;
  z-index: 1;
  width: min(460px,100%);
  padding: 36px 34px;
  border-radius: 26px;
  color: #f0f1fb;
  background: linear-gradient(165deg,rgba(255,255,255,.13),rgba(255,255,255,.04));
  backdrop-filter: blur(24px) saturate(180%);
  -webkit-backdrop-filter: blur(24px) saturate(180%);
  border: 1px solid rgba(255,255,255,.26);
  box-shadow: 0 40px 80px -30px rgba(0,0,0,.9),inset 0 1px 0 rgba(255,255,255,.3);
}

.glz-24b__chip {
  display: inline-block;
  font-size: 10.5px;
  font-weight: 800;
  letter-spacing: .18em;
  text-transform: uppercase;
  padding: 6px 12px;
  border-radius: 99px;
  color: oklch(0.85 0.15 170);
  background: oklch(0.85 0.15 170/.12);
  border: 1px solid oklch(0.85 0.15 170/.4);
}

.glz-24b__card h2 {
  margin-top: 16px;
  font-size: clamp(26px,4.6vw,36px);
  font-weight: 900;
  line-height: 1.1;
  letter-spacing: -.025em;
}

.glz-24b__card p {
  margin-top: 14px;
  font-size: 14px;
  line-height: 1.65;
  color: rgba(240,241,251,.68);
  text-wrap: pretty;
}

.glz-24b__card button {
  margin-top: 24px;
  padding: 14px 22px;
  border: none;
  border-radius: 13px;
  background: linear-gradient(120deg,oklch(0.7 0.18 280),oklch(0.72 0.16 200));
  color: #fff;
  font: 800 14px 'Archivo',sans-serif;
  cursor: pointer;
  box-shadow: 0 18px 36px -14px oklch(0.7 0.18 280/.8);
  transition: transform .2s ease;
}

.glz-24b__card button:hover {
  transform: translateY(-2px);
}

.glz-24b__card button:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 3px;
}

@keyframes glz-24b-d1 {
  to {
    transform: translate(14vmin,10vmin) scale(1.2);
  }
}

@keyframes glz-24b-d2 {
  to {
    transform: translate(-12vmin,-8vmin) scale(1.15);
  }
}

@keyframes glz-24b-d3 {
  to {
    transform: translate(-10vmin,12vmin) scale(1.25);
  }
}

@supports not ((backdrop-filter: blur(2px)) or (-webkit-backdrop-filter: blur(2px))) {
  .glz-24b__card {
    background: rgba(15,18,32,.94);
  }
}

@media (prefers-reduced-motion: reduce) {
  .glz-24b__aurora i {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — muted+playsinline+loop autoplay with a poster and gradient underlay; the card's backdrop-filter frosts each frame on the compositor. */

/* No JavaScript — three mix-blend-mode:screen gradient blobs drift on long alternating loops; the glass frosts them exactly as it would frost footage. */
```
