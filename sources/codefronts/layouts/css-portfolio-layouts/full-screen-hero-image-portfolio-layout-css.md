---
source: "codefronts"
url: "https://codefronts.com/layouts/css-portfolio-layouts/full-screen-hero-image-portfolio-layout-css/"
title: "Full Screen Hero Image Portfolio Layout CSS"
section: "layouts"
category: "css-portfolio-layouts"
category_name: "CSS Portfolio Layouts"
description: "The visual-storyteller opener: a hero that owns the entire first viewport — layered imagery, a display-scale title, a bouncing scroll cue — followed by the…"
has_js: "false"
---

Here's a working CSS Portfolio Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Full Screen Hero Image Portfolio Layout CSS
Source: https://codefronts.com/layouts/css-portfolio-layouts/full-screen-hero-image-portfolio-layout-css/

The visual-storyteller opener: a hero that owns the entire first viewport — layered imagery, a display-scale title, a bouncing scroll cue — followed by the work. Under the drama sit the two details that separate 2026 heroes from 2016 ones: it's sized with small-viewport units (100svh, not the iOS-broken 100vh), and the hero art recedes with a scroll-driven parallax that costs zero JavaScript and calms itself under prefers-reduced-motion.
## HTML
```html
<section class="cpl-15" aria-label="Full screen hero portfolio demo">
  <div class="cpl-15__stage">
    <div class="cpl-15__scroll">
      <header class="cpl-15__hero">
        <div class="cpl-15__art" aria-hidden="true" style="--img:url('https://images.unsplash.com/photo-1519681393784-d120267933ba?q=80&w=900&auto=format&fit=crop')"></div>
        <div class="cpl-15__scrim" aria-hidden="true"></div>
        <nav class="cpl-15__bar" aria-label="Site">
          <span>VALE.CO</span>
          <a href="#cpl15-work">Work</a>
        </nav>
        <div class="cpl-15__title">
          <p>Director of photography — commercials &amp; documentary</p>
          <h2>Light is<br>the story.</h2>
        </div>
        <a class="cpl-15__cue" href="#cpl15-work" aria-label="Scroll to work"><i aria-hidden="true"></i></a>
      </header>
      <main class="cpl-15__work" id="cpl15-work">
        <h3>Selected frames</h3>
        <div class="cpl-15__reel">
          <a href="#northland" style="--img:url('https://images.unsplash.com/photo-1478720568477-152d9b164e26?q=80&w=900&auto=format&fit=crop');--a:oklch(0.6 0.1 250);--b:oklch(0.3 0.08 270)"><span>Northland — feature doc</span></a>
          <a href="#volt" style="--img:url('https://images.unsplash.com/photo-1549317661-bd32c8ce0db2?q=80&w=900&auto=format&fit=crop');--a:oklch(0.7 0.14 45);--b:oklch(0.4 0.13 20)"><span>Volt EV — launch film</span></a>
          <a href="#stillwater" style="--img:url('https://images.unsplash.com/photo-1500534314209-a25ddb2bd429?q=80&w=900&auto=format&fit=crop');--a:oklch(0.65 0.1 180);--b:oklch(0.35 0.09 210)"><span>Stillwater — short</span></a>
        </div>
      </main>
    </div>
  </div>
</section>
```
## CSS
```css
.cpl-15,
.cpl-15 *,
.cpl-15 *::before,
.cpl-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cpl-15 {
  --ink: oklch(0.96 0.005 90);
  --mut: oklch(0.7 0.01 90);
  --bg: oklch(0.16 0.015 270);
  --acc: oklch(0.82 0.13 80);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
}

.cpl-15__stage {
  width: 100%;
  height: 100vh;
  height: 100svh;
  background: var(--bg);
  overflow: hidden;
}

.cpl-15__scroll {
  height: 100%;
  overflow-y: auto;
  scroll-behavior: smooth;
}

.cpl-15__hero {
  position: relative;
  height: 100vh;
  height: 100svh;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.cpl-15__art {
  position: absolute;
  inset: -12% 0 0;
  background-image: var(--img,none),linear-gradient(170deg,oklch(0.3 0.05 270),oklch(0.18 0.02 270));
  background-size: cover;
  background-position: center;
}

.cpl-15__scrim {
  position: absolute;
  inset: 0;
  background: linear-gradient(to top,oklch(0.14 0.015 270/.85),transparent 45%,oklch(0.14 0.015 270/.35));
}

@supports (animation-timeline: view()) {
  .cpl-15__art {
    animation: cpl15-recede linear both;
    animation-timeline: view();
    animation-range: exit 0% exit 100%;
  }

  @keyframes cpl15-recede {
    to {
      translate: 0 -18%;
      opacity: .25;
    }
  }
}

.cpl-15__bar {
  position: relative;
  z-index: 2;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 26px;
}

.cpl-15__bar span {
  font-size: 13px;
  font-weight: 800;
  letter-spacing: .22em;
}

.cpl-15__bar a {
  font-size: 13px;
  font-weight: 700;
  color: var(--ink);
  text-decoration: none;
  padding: 8px 2px;
  border-bottom: 2px solid transparent;
  transition: border-color .25s,color .25s;
}

.cpl-15__bar a:hover,
.cpl-15__bar a:focus-visible {
  color: var(--acc);
  border-color: var(--acc);
}

.cpl-15__bar a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.cpl-15__title {
  position: relative;
  z-index: 2;
  margin-top: auto;
  padding: 0 26px 66px;
}

.cpl-15__title p {
  font-size: 12.5px;
  font-weight: 600;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--acc);
  margin-bottom: 12px;
}

.cpl-15__title h2 {
  font-size: clamp(34px,8cqi,72px);
  line-height: .98;
  letter-spacing: -.035em;
  font-weight: 700;
}

.cpl-15__cue {
  position: absolute;
  z-index: 2;
  bottom: 16px;
  left: 50%;
  translate: -50% 0;
  width: 44px;
  height: 44px;
  display: grid;
  place-items: center;
  border-radius: 50%;
}

.cpl-15__cue i {
  width: 12px;
  height: 12px;
  border-right: 2.5px solid var(--ink);
  border-bottom: 2.5px solid var(--ink);
  rotate: 45deg;
  animation: cpl15-bob 1.8s ease-in-out infinite;
}

.cpl-15__cue:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

@keyframes cpl15-bob {
  0%,
    100% {
    translate: 0 -2px;
    opacity: .6;
  }

  50% {
    translate: 0 4px;
    opacity: 1;
  }
}

.cpl-15__work {
  padding: 30px 26px 36px;
  scroll-margin-top: 8px;
}

.cpl-15__work h3 {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--mut);
  margin-bottom: 16px;
}

.cpl-15__reel {
  display: grid;
  gap: 12px;
  grid-template-columns: repeat(auto-fit,minmax(min(220px,100%),1fr));
}

.cpl-15__reel a {
  position: relative;
  aspect-ratio: 16/9;
  border-radius: 14px;
  overflow: hidden;
  background-image: var(--img,none),linear-gradient(150deg,var(--a),var(--b));
  background-size: cover;
  background-position: center;
  text-decoration: none;
  color: var(--ink);
  display: grid;
  align-content: end;
  transition: translate .3s cubic-bezier(.2,.7,.2,1);
}

.cpl-15__reel a:hover,
.cpl-15__reel a:focus-visible {
  translate: 0 -4px;
}

.cpl-15__reel a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.cpl-15__reel span {
  padding: 26px 14px 12px;
  font-size: 13px;
  font-weight: 700;
  background: linear-gradient(to top,oklch(0.12 0.015 270/.8),transparent);
}

@media (prefers-reduced-motion: reduce) {
  .cpl-15__scroll {
    scroll-behavior: auto;
  }

  .cpl-15__cue i {
    animation: none;
  }

  .cpl-15__art {
    animation: none;
  }

  .cpl-15 * {
    transition-duration: .01ms !important;
  }
}
```
