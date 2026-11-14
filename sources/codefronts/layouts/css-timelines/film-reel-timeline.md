---
source: "codefronts"
url: "https://codefronts.com/layouts/css-timelines/film-reel-timeline/"
title: "Film Reel Timeline — Sprocket-Hole Border History Strip"
section: "layouts"
category: "css-timelines"
category_name: "CSS Timelines"
description: "History as celluloid: a vertical strip bordered by repeating sprocket holes (one repeating-radial-gradient, zero images), frame-numbered milestones, and a…"
has_js: "false"
---

Here's a working CSS Timeline from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Film Reel Timeline — Sprocket-Hole Border History Strip
Source: https://codefronts.com/layouts/css-timelines/film-reel-timeline/

History as celluloid: a vertical strip bordered by repeating sprocket holes (one repeating-radial-gradient, zero images), frame-numbered milestones, and a projector-flicker hover — the cinematic treatment for studio histories, film-festival retrospectives and media-brand 'our story' pages.
## HTML
```html
<section class="tls-12" aria-label="Film history timeline demo">
  <div class="tls-12__strip">
    <p class="tls-12__leader">A STUDIO IN FIVE REELS · EST. 1962</p>
    <ol class="tls-12__frames" role="list">
      <li class="tls-12__frame">
        <div class="tls-12__still" style="--g:linear-gradient(160deg,#8c6d46,#3d2f1c)" aria-hidden="true"></div>
        <div class="tls-12__cap"><time datetime="1962">1962</time><p>Two projectionists rent a basement and call it a studio.</p></div>
      </li>
      <li class="tls-12__frame">
        <div class="tls-12__still" style="--g:linear-gradient(160deg,#5e7a8c,#1e2f3d)" aria-hidden="true"></div>
        <div class="tls-12__cap"><time datetime="1974">1974</time><p>First feature. It loses money beautifully.</p></div>
      </li>
      <li class="tls-12__frame">
        <div class="tls-12__still" style="--g:linear-gradient(160deg,#8c4646,#3d1c1c)" aria-hidden="true"></div>
        <div class="tls-12__cap"><time datetime="1989">1989</time><p>The archive fire. Three reels survive; we rebuild from prints.</p></div>
      </li>
      <li class="tls-12__frame">
        <div class="tls-12__still" style="--g:linear-gradient(160deg,#46748c,#12212e)" aria-hidden="true"></div>
        <div class="tls-12__cap"><time datetime="2011">2011</time><p>Full catalogue restored and scanned at 4K.</p></div>
      </li>
    </ol>
  </div>
</section>
```
## CSS
```css
.tls-12,
.tls-12 *,
.tls-12 *::before,
.tls-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tls-12 {
  min-height: 100vh;
  width: 100%;
  --tl-w: 340px;
  --tl-film: #141210;
  --tl-paper: #f5f0e6;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #211d19;
  padding: 56px 24px;
  display: grid;
  place-items: center;
}

.tls-12__strip {
  width: min(var(--tl-w),100%);
  background: var(--tl-film);
  position: relative;
  padding: 22px 44px 30px;
  border-radius: 4px;
  box-shadow: 0 20px 50px -24px rgba(0,0,0,.8);
}

.tls-12__strip::before,
.tls-12__strip::after {
  content: '';
  position: absolute;
  top: 0;
  bottom: 0;
  width: 26px;
  background: repeating-radial-gradient(circle at center,var(--tl-paper) 0 4.5px,transparent 5.5px) center / 100% 26px;
}

.tls-12__strip::before {
  left: 6px;
}

.tls-12__strip::after {
  right: 6px;
}

.tls-12__leader {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 10px;
  letter-spacing: .28em;
  color: #a89e8c;
  text-align: center;
  margin-bottom: 18px;
}

.tls-12__frames {
  list-style: none;
  counter-reset: tls-frame;
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.tls-12__frame {
  counter-increment: tls-frame;
  position: relative;
}

.tls-12__still {
  width: 100%;
  aspect-ratio: 4/3;
  background: var(--g);
  border: 3px solid #2b2723;
  border-radius: 2px;
  position: relative;
  overflow: hidden;
}

.tls-12__still::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(105deg,transparent 40%,rgba(255,250,230,.07) 45%,transparent 52%);
}

@media (prefers-reduced-motion: no-preference) {
  .tls-12__frame:hover .tls-12__still {
    animation: tls-12-flicker .35s steps(2,jump-none) infinite;
  }

  @keyframes tls-12-flicker {
    0% {
      filter: brightness(1);
    }

    50% {
      filter: brightness(1.18);
    }

    100% {
      filter: brightness(.94);
    }
  }
}

.tls-12__cap {
  display: flex;
  gap: 12px;
  align-items: baseline;
  margin-top: 8px;
}

.tls-12__cap::before {
  content: counter(tls-frame,decimal-leading-zero);
  font-family: ui-monospace,Menlo,monospace;
  font-size: 10px;
  color: #6e6353;
  letter-spacing: .1em;
}

.tls-12__cap time {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 13px;
  font-weight: 700;
  color: var(--tl-paper);
}

.tls-12__cap p {
  font-size: 12.5px;
  line-height: 1.5;
  color: #b8ac97;
  text-wrap: pretty;
}
```

## JavaScript
```js
/* No JavaScript — sprocket holes are one repeating-radial-gradient per rail; frame numbers are CSS counters; the flicker is opt-in behind prefers-reduced-motion:no-preference. */
```
