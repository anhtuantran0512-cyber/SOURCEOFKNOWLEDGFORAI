---
source: "codefronts"
url: "https://codefronts.com/layouts/css-aspect-ratio/css-aspect-ratio-full-screen-hero-video/"
title: "CSS Aspect Ratio Full Screen Hero Video"
section: "layouts"
category: "css-aspect-ratio"
category_name: "CSS Aspect Ratio Demos"
description: "A cinematic hero whose height is negotiated, not hard-coded: aspect-ratio: 21/9 asks for widescreen, min-height keeps it usable on portrait phones,…"
has_js: "false"
---

Here's a working CSS Aspect Ratio Demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Aspect Ratio Full Screen Hero Video
Source: https://codefronts.com/layouts/css-aspect-ratio/css-aspect-ratio-full-screen-hero-video/

A cinematic hero whose height is negotiated, not hard-coded: aspect-ratio: 21/9 asks for widescreen, min-height keeps it usable on portrait phones, max-height: 100svh guarantees it never outgrows the viewport. The background video paints edge to edge with object-fit: cover, falls back to its poster (then to a gradient) if the file never arrives, and drifts through a slow Ken Burns zoom that stops for prefers-reduced-motion. The three-line sizing contract is printed on the page itself.
## HTML
```html
<section class="car-02" aria-label="Full screen hero video demo">
  <div class="car-02__stage" id="car02-top">
    <header class="car-02__hero">
      <figure class="car-02__media" aria-hidden="true">
        <video autoplay muted loop playsinline preload="metadata" poster="https://images.unsplash.com/photo-1506905925346-21bda4d32df4?q=80&w=1800&auto=format&fit=crop">
          <source src="https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.mp4" type="video/mp4">
        </video>
      </figure>
      <div class="car-02__scrim" aria-hidden="true"></div>
      <nav class="car-02__nav" aria-label="Primary">
        <a class="car-02__brand" href="#car02-top">NORTHBOUND</a>
        <div class="car-02__links">
          <a href="#car02-how">Films</a>
          <a href="#car02-how">Journal</a>
          <a href="#car02-how">About</a>
        </div>
      </nav>
      <div class="car-02__copy">
        <p class="car-02__kicker">Field films · Season 04</p>
        <h1>Sized by ratio,<br>bounded by viewport.</h1>
        <p class="car-02__sub">This hero prefers <code>21:9</code>, refuses to shrink below 560px, and never exceeds <code>100svh</code>. The video underneath re-crops itself to whatever wins.</p>
        <div class="car-02__row">
          <a class="car-02__btn car-02__btn--solid" href="#car02-how">How it's sized ↓</a>
          <a class="car-02__btn" href="#car02-how">Watch the reel</a>
        </div>
      </div>
      <code class="car-02__contract" aria-hidden="true">aspect-ratio:21/9 · min-height:560px · max-height:100svh</code>
    </header>
    <section class="car-02__how" id="car02-how">
      <h2>The three-line negotiation</h2>
      <p class="car-02__lede">One preference, two guardrails. The browser resolves them in a fixed order — ratio proposes, min/max dispose:</p>
      <div class="car-02__cards">
        <article><span>Laptop · 1440px</span><h3>Ratio wins</h3><p>21:9 of 1440px is ~617px tall. Neither guard fires — you get the cinematic band the design asked for.</p><i style="--w:100%;--r:21/9"></i></article>
        <article><span>Phone · 390px</span><h3>min-height wins</h3><p>The ratio proposes a 167px sliver. <code>min-height:560px</code> overrules it; <code>object-fit:cover</code> re-crops the footage to portrait.</p><i style="--w:24%;--r:9/16"></i></article>
        <article><span>Ultrawide · 3440px</span><h3>max-height wins</h3><p>The ratio proposes 1474px — taller than the screen. <code>max-height:100svh</code> caps it flush to the fold.</p><i style="--w:100%;--r:32/9"></i></article>
      </div>
      <footer class="car-02__foot">Autoplay checklist baked into the markup: <code>muted</code> · <code>playsinline</code> · <code>loop</code> · <code>preload="metadata"</code> · <code>poster</code> fallback. A demo from the CodeFronts aspect-ratio collection.</footer>
    </section>
  </div>
</section>
```
## CSS
```css
.car-02,
.car-02 *,
.car-02 *::before,
.car-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.car-02 {
  --bg: oklch(0.14 0.01 260);
  --ink: oklch(0.96 0.005 250);
  --mut: oklch(0.7 0.012 250);
  --line: oklch(0.3 0.015 260);
  --acc: oklch(0.82 0.13 160);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
  display: block;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: var(--bg);
}

.car-02__stage {
  width: 100%;
  container: car02/inline-size;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  background: var(--bg);
  scroll-behavior: smooth;
}

.car-02__hero {
  position: relative;
  width: 100%;
  aspect-ratio: 21/9;
  min-height: min(560px,100vh);
  min-height: min(560px,100svh);
  max-height: 100vh;
  max-height: 100svh;
  overflow: clip;
  display: grid;
  grid-template-rows: auto 1fr;
  isolation: isolate;
}

.car-02__media {
  position: absolute;
  inset: 0;
  z-index: -2;
  background: linear-gradient(160deg,oklch(0.35 0.06 250),oklch(0.2 0.04 290));
}

.car-02__media video {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  animation: car02-drift 26s ease-in-out infinite alternate;
}

@keyframes car02-drift {
  from {
    scale: 1;
    translate: 0 0;
  }

  to {
    scale: 1.09;
    translate: 1.5% -1%;
  }
}

.car-02__scrim {
  position: absolute;
  inset: 0;
  z-index: -1;
  background: linear-gradient(to bottom,oklch(0.1 0.02 260/.55),oklch(0.1 0.02 260/.12) 38%,oklch(0.1 0.02 260/.62) 88%);
}

.car-02__nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: clamp(14px,2.5cqi,26px) clamp(18px,4cqi,48px);
}

.car-02__brand {
  font-size: 15px;
  font-weight: 800;
  letter-spacing: .34em;
  color: inherit;
  text-decoration: none;
}

.car-02__links {
  display: flex;
  gap: 2px;
}

.car-02__links a {
  display: grid;
  place-items: center;
  min-height: 44px;
  padding: 0 14px;
  border-radius: 10px;
  font-size: 13px;
  font-weight: 600;
  color: oklch(0.9 0.01 250);
  text-decoration: none;
  transition: background .2s;
}

.car-02__links a:hover,
.car-02__links a:focus-visible {
  background: oklch(0.2 0.02 260/.45);
}

.car-02__links a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
}

.car-02__copy {
  align-self: end;
  padding: 0 clamp(18px,4cqi,48px) clamp(24px,5cqi,56px);
  max-width: 72ch;
}

.car-02__kicker {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .22em;
  text-transform: uppercase;
  color: var(--acc);
  margin-bottom: 12px;
}

.car-02__copy h1 {
  font-size: clamp(34px,6.5cqi,68px);
  line-height: 1.02;
  letter-spacing: -.03em;
  font-weight: 800;
  text-wrap: balance;
  text-shadow: 0 2px 24px oklch(0.1 0.02 260/.5);
}

.car-02__sub {
  margin-top: 14px;
  font-size: 15px;
  line-height: 1.6;
  color: oklch(0.86 0.01 250);
  max-width: 52ch;
}

.car-02__sub code,
.car-02__how code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .88em;
  background: oklch(0.24 0.02 260/.8);
  padding: 2px 6px;
  border-radius: 5px;
  color: var(--acc);
}

.car-02__row {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 22px;
}

.car-02__btn {
  display: grid;
  place-items: center;
  min-height: 46px;
  padding: 0 20px;
  border-radius: 12px;
  font-size: 14px;
  font-weight: 700;
  text-decoration: none;
  color: var(--ink);
  border: 1.5px solid oklch(0.85 0.01 250/.4);
  background: oklch(0.2 0.02 260/.35);
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
  transition: border-color .2s,translate .2s,background .2s;
}

.car-02__btn:hover,
.car-02__btn:focus-visible {
  border-color: var(--acc);
  translate: 0 -2px;
}

.car-02__btn:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.car-02__btn--solid {
  background: var(--acc);
  border-color: var(--acc);
  color: oklch(0.18 0.04 160);
}

.car-02__btn--solid:hover,
.car-02__btn--solid:focus-visible {
  background: color-mix(in oklch,var(--acc) 85%,white);
}

.car-02__contract {
  position: absolute;
  right: clamp(14px,3cqi,28px);
  top: clamp(64px,10cqi,84px);
  writing-mode: vertical-rl;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 10.5px;
  letter-spacing: .08em;
  color: oklch(0.85 0.01 250/.65);
  border-left: 1px solid oklch(0.85 0.01 250/.25);
  padding-left: 10px;
}

.car-02__how {
  padding: clamp(40px,7cqi,80px) clamp(18px,4cqi,48px) 0;
}

.car-02__how h2 {
  font-size: clamp(24px,4cqi,36px);
  letter-spacing: -.025em;
  font-weight: 800;
}

.car-02__lede {
  margin-top: 10px;
  max-width: 60ch;
  font-size: 14.5px;
  line-height: 1.65;
  color: var(--mut);
}

.car-02__cards {
  display: grid;
  gap: 14px;
  grid-template-columns: repeat(auto-fit,minmax(min(250px,100%),1fr));
  margin-top: 26px;
}

.car-02__cards article {
  position: relative;
  padding: 20px 20px 130px;
  border-radius: 16px;
  background: oklch(0.19 0.015 262);
  border: 1px solid var(--line);
  overflow: hidden;
  transition: translate .25s cubic-bezier(.2,.7,.2,1),border-color .25s;
}

.car-02__cards article:hover {
  translate: 0 -3px;
  border-color: color-mix(in oklch,var(--acc) 45%,var(--line));
}

.car-02__cards span {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  font-weight: 700;
  color: var(--acc);
}

.car-02__cards h3 {
  font-size: 16.5px;
  letter-spacing: -.01em;
  margin: 8px 0 8px;
}

.car-02__cards p {
  font-size: 13px;
  line-height: 1.6;
  color: var(--mut);
}

.car-02__cards i {
  position: absolute;
  left: 20px;
  bottom: 18px;
  display: block;
  width: var(--w);
  max-width: calc(100% - 40px);
  aspect-ratio: var(--r);
  max-height: 104px;
  border: 1.5px dashed color-mix(in oklch,var(--acc) 60%,var(--line));
  border-radius: 8px;
  background: linear-gradient(160deg,oklch(0.28 0.05 250/.6),oklch(0.22 0.03 290/.6));
}

.car-02__foot {
  margin-top: clamp(30px,6cqi,56px);
  padding: 22px 0 34px;
  font-size: 12.5px;
  line-height: 1.6;
  color: var(--mut);
  border-top: 1px solid var(--line);
}

@container car02 (width < 560px) {
  .car-02__links {
    display: none;
  }

  .car-02__contract {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .car-02__stage {
    scroll-behavior: auto;
  }

  .car-02__media video {
    animation: none;
  }

  .car-02 * {
    transition-duration: .01ms !important;
  }
}
```
