---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-gradient-ui/gradient-scroll-mask-fade/"
title: "Gradient Scroll Mask Fade"
section: "design-styles"
category: "css-gradient-ui"
category_name: "CSS Gradient UI"
description: "The polish detail that separates production UIs from demos: scrollable areas whose clipped edges dissolve through a gradient mask — a horizontal filter-chip…"
has_js: "false"
---

Here's a working CSS Gradient UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Gradient Scroll Mask Fade
Source: https://codefronts.com/design-styles/css-gradient-ui/gradient-scroll-mask-fade/

The polish detail that separates production UIs from demos: scrollable areas whose clipped edges dissolve through a gradient mask — a horizontal filter-chip rail and a vertical changelog feed, with scroll-driven animations revealing the fades only when there is actually more to scroll.
## HTML
```html
<div class="cgu-18-group">
<section class="cgu-18" aria-label="Gradient scroll mask fade demos">
  <div class="cgu-18__inner">
    <header class="cgu-18__head">
      <p class="cgu-18__eyebrow">18 · Scroll mask fade</p>
      <h2 class="cgu-18__title">Edges that dissolve, not clip</h2>
      <p class="cgu-18__sub">Scroll the chip rail and the feed — each fade retracts at its travel limit via <code>animation-timeline: scroll()</code>, so it never lies about more content.</p>
    </header>
    <div class="cgu-18__railwrap">
      <p class="cgu-18__caption">Horizontal · <code>scroll(self inline)</code></p>
      <div class="cgu-18__rail" role="region" aria-label="Topic filters, scrollable" tabindex="0">
        <button class="cgu-18__chip is-on" type="button">All topics</button>
        <button class="cgu-18__chip" type="button">Gradients</button>
        <button class="cgu-18__chip" type="button">Masks</button>
        <button class="cgu-18__chip" type="button">Typography</button>
        <button class="cgu-18__chip" type="button">Layout</button>
        <button class="cgu-18__chip" type="button">Animation</button>
        <button class="cgu-18__chip" type="button">Color science</button>
        <button class="cgu-18__chip" type="button">Accessibility</button>
        <button class="cgu-18__chip" type="button">Performance</button>
        <button class="cgu-18__chip" type="button">Scroll effects</button>
        <button class="cgu-18__chip" type="button">Glassmorphism</button>
        <button class="cgu-18__chip" type="button">Dark mode</button>
      </div>
    </div>
    <div class="cgu-18__feedwrap">
      <p class="cgu-18__caption">Vertical · <code>scroll(self block)</code></p>
      <div class="cgu-18__feed" role="region" aria-label="Changelog, scrollable" tabindex="0">
        <article class="cgu-18__entry"><time class="cgu-18__date">Jul 28</time><div><h3>Scroll-driven fades shipped</h3><p>Edge masks now retract at travel limits — no more phantom "more content" fades.</p></div></article>
        <article class="cgu-18__entry"><time class="cgu-18__date">Jul 21</time><div><h3>oklch palette pipeline</h3><p>All gradient stops migrated to oklch for perceptually even ramps.</p></div></article>
        <article class="cgu-18__entry"><time class="cgu-18__date">Jul 14</time><div><h3>Mask-composite borders</h3><p>Gradient borders now keep transparent centres over imagery.</p></div></article>
        <article class="cgu-18__entry"><time class="cgu-18__date">Jul 07</time><div><h3>Reduced-motion audit</h3><p>Every animation gained a calm fallback; steps() flickers removed.</p></div></article>
        <article class="cgu-18__entry"><time class="cgu-18__date">Jun 30</time><div><h3>Focus ring pass</h3><p>Scrollable regions are keyboard-reachable with visible rings clear of the fade zone.</p></div></article>
        <article class="cgu-18__entry"><time class="cgu-18__date">Jun 23</time><div><h3>Grain overlays</h3><p>SVG turbulence data-URIs replace PNG noise — zero requests, no banding.</p></div></article>
      </div>
    </div>
    <p class="cgu-18__foot">Both scrollers are keyboard-focusable regions; the masks live on the scrollers themselves, never on ancestors.</p>
  </div>
</section>
</div>
```
## CSS
```css
.cgu-18-group {
  display: block;
  width: 100%;
}

.cgu-18,
.cgu-18 *,
.cgu-18 *::before,
.cgu-18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cgu-18 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 64px 24px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: #eef0ff;
  background: linear-gradient(190deg,#0d1018 0%,#0a0b12 70%);
}

.cgu-18__inner {
  width: min(760px,100%);
  display: grid;
  gap: 30px;
}

.cgu-18__head {
  text-align: center;
  display: grid;
  gap: 13px;
  justify-items: center;
}

.cgu-18__eyebrow {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .28em;
  text-transform: uppercase;
  color: #5eead4;
}

.cgu-18__title {
  font-size: clamp(27px,4.2vw,46px);
  font-weight: 800;
  letter-spacing: -.02em;
  line-height: 1.08;
  text-wrap: balance;
}

.cgu-18__sub {
  max-width: 58ch;
  font-size: 15.5px;
  line-height: 1.6;
  color: #a7abc8;
  text-wrap: pretty;
}

.cgu-18__sub code,
.cgu-18__caption code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 12px;
  color: #99f6e4;
  background: rgba(94,234,212,.08);
  padding: 1px 5px;
  border-radius: 5px;
}

.cgu-18__caption {
  font-size: 12.5px;
  font-weight: 650;
  color: #7c81a3;
  margin-bottom: 10px;
}

.cgu-18__rail {
  display: flex;
  gap: 10px;
  overflow-x: auto;
  padding: 10px 4px;
  scroll-snap-type: x proximity;
  scrollbar-width: none;
  -webkit-mask-image: linear-gradient(to right,transparent,#000 48px,#000 calc(100% - 48px),transparent);
  mask-image: linear-gradient(to right,transparent,#000 48px,#000 calc(100% - 48px),transparent);
}

.cgu-18__rail::-webkit-scrollbar {
  display: none;
}

.cgu-18__rail:focus-visible,
.cgu-18__feed:focus-visible {
  outline: 2px solid #5eead4;
  outline-offset: 3px;
  border-radius: 12px;
}

.cgu-18__chip {
  flex: none;
  scroll-snap-align: start;
  font: inherit;
  font-size: 13px;
  font-weight: 650;
  color: #b6bad4;
  padding: 9px 18px;
  border-radius: 9999px;
  cursor: pointer;
  border: 1px solid transparent;
  background: linear-gradient(#12141f,#12141f) padding-box,linear-gradient(135deg,#2b2f45,#2b2f45) border-box;
  transition: color .25s,background .25s;
}

.cgu-18__chip:hover,
.cgu-18__chip:focus-visible {
  color: #fff;
  background: linear-gradient(#12141f,#12141f) padding-box,linear-gradient(135deg,#5eead4,#818cf8) border-box;
}

.cgu-18__chip:focus-visible {
  outline: 2px solid #5eead4;
  outline-offset: 2px;
}

.cgu-18__chip.is-on {
  color: #04211c;
  background: linear-gradient(135deg,#5eead4,#34d399);
  font-weight: 750;
}

.cgu-18__feed {
  display: grid;
  gap: 4px;
  max-height: 300px;
  overflow-y: auto;
  padding: 26px 6px;
  scrollbar-width: none;
  -webkit-mask-image: linear-gradient(to bottom,transparent,#000 44px,#000 calc(100% - 44px),transparent);
  mask-image: linear-gradient(to bottom,transparent,#000 44px,#000 calc(100% - 44px),transparent);
}

.cgu-18__feed::-webkit-scrollbar {
  display: none;
}

.cgu-18__entry {
  display: grid;
  grid-template-columns: 64px 1fr;
  gap: 16px;
  padding: 14px 8px;
  border-radius: 12px;
  transition: background .2s;
}

.cgu-18__entry:hover {
  background: rgba(255,255,255,.03);
}

.cgu-18__date {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11.5px;
  color: #5eead4;
  padding-top: 3px;
}

.cgu-18__entry h3 {
  font-size: 15px;
  font-weight: 750;
  margin-bottom: 3px;
}

.cgu-18__entry p {
  font-size: 13.5px;
  line-height: 1.55;
  color: #9aa0c0;
}

.cgu-18__foot {
  text-align: center;
  font-size: 13px;
  color: #7c81a3;
  max-width: 64ch;
  justify-self: center;
}

@supports (animation-timeline: scroll()) {
  .cgu-18__rail {
    animation: cgu18-x linear both;
    animation-timeline: scroll(self inline);
  }

  .cgu-18__feed {
    animation: cgu18-y linear both;
    animation-timeline: scroll(self block);
  }

  @keyframes cgu18-x {
    0% {
      -webkit-mask-image: linear-gradient(to right,#000,#000 0,#000 calc(100% - 48px),transparent);
      mask-image: linear-gradient(to right,#000,#000 0,#000 calc(100% - 48px),transparent);
    }

    10%,
        90% {
      -webkit-mask-image: linear-gradient(to right,transparent,#000 48px,#000 calc(100% - 48px),transparent);
      mask-image: linear-gradient(to right,transparent,#000 48px,#000 calc(100% - 48px),transparent);
    }

    100% {
      -webkit-mask-image: linear-gradient(to right,transparent,#000 48px,#000 100%,#000);
      mask-image: linear-gradient(to right,transparent,#000 48px,#000 100%,#000);
    }
  }

  @keyframes cgu18-y {
    0% {
      -webkit-mask-image: linear-gradient(to bottom,#000,#000 0,#000 calc(100% - 44px),transparent);
      mask-image: linear-gradient(to bottom,#000,#000 0,#000 calc(100% - 44px),transparent);
    }

    10%,
        90% {
      -webkit-mask-image: linear-gradient(to bottom,transparent,#000 44px,#000 calc(100% - 44px),transparent);
      mask-image: linear-gradient(to bottom,transparent,#000 44px,#000 calc(100% - 44px),transparent);
    }

    100% {
      -webkit-mask-image: linear-gradient(to bottom,transparent,#000 44px,#000 100%,#000);
      mask-image: linear-gradient(to bottom,transparent,#000 44px,#000 100%,#000);
    }
  }
}

@media (prefers-reduced-motion: reduce) {
  .cgu-18__chip,
    .cgu-18__entry {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — gradient mask-image dissolves the scroller edges; scroll-driven animations (animation-timeline: scroll(self)) retract each fade at its travel limit inside an @supports guard. */
```
