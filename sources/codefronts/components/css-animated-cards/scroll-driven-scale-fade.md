---
source: "codefronts"
url: "https://codefronts.com/components/css-animated-cards/scroll-driven-scale-fade/"
title: "Scroll-Driven Scale + Fade"
section: "components"
category: "css-animated-cards"
category_name: "CSS Animated Cards"
description: "Cards whose scale, opacity and blur are a direct function of scroll position — scrubbed by the browser off the main thread, so it never janks."
has_js: "false"
---

Here's a working CSS Animated Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Scroll-Driven Scale + Fade
Source: https://codefronts.com/components/css-animated-cards/scroll-driven-scale-fade/

Cards whose scale, opacity and blur are a direct function of scroll position — scrubbed by the browser off the main thread, so it never janks. Uses animation-timeline: view() with a hand-tuned animation-range so cards settle exactly when they become comfortably readable, plus a scroll() driven progress rail at the top. The panel scrolls itself, so the demo works inside any playground.
## HTML
```html
<section class="ac-03" aria-label="Scroll driven scale and fade demo">
  <div class="ac-03__stage">
    <div class="ac-03__panel">
      <div class="ac-03__bar"><span class="ac-03__rail" aria-hidden="true"></span></div>
      <div class="ac-03__scroller" tabindex="0" role="region" aria-label="Scrollable card gallery">
        <div class="ac-03__lead">
          <p class="ac-03__eyebrow">Scroll inside this panel ↓</p>
          <h2 class="ac-03__title">The animation is the scroll position</h2>
          <p class="ac-03__sub">Each card is scrubbed by <code>view()</code>. Scroll back up and it plays in reverse.</p>
        </div>
        <article class="ac-03__card">
          <span class="ac-03__media"><img src="https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?q=80&w=800&auto=format&fit=crop" alt="Fog drifting between pine trees" loading="lazy" decoding="async" width="800" height="500"></span>
          <div class="ac-03__body"><h3 class="ac-03__name">Entry range</h3><p class="ac-03__copy">Starts at <code>entry 15%</code> — after the card has cleared the edge, before it demands attention.</p></div>
        </article>
        <article class="ac-03__card">
          <span class="ac-03__media"><img src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=800&auto=format&fit=crop" alt="Glowing network of connections over a dark globe" loading="lazy" decoding="async" width="800" height="500"></span>
          <div class="ac-03__body"><h3 class="ac-03__name">Cover range</h3><p class="ac-03__copy">Finishes at <code>cover 42%</code> — settled a beat before dead centre, which reads as calm.</p></div>
        </article>
        <article class="ac-03__card">
          <span class="ac-03__media"><img src="https://images.unsplash.com/photo-1493246507139-91e8fad9978e?q=80&w=800&auto=format&fit=crop" alt="Layered mountain ridges at dawn" loading="lazy" decoding="async" width="800" height="500"></span>
          <div class="ac-03__body"><h3 class="ac-03__name">Linear on purpose</h3><p class="ac-03__copy">Scroll is already the easing curve. A bezier on top makes the card feel like it lags your finger.</p></div>
        </article>
        <article class="ac-03__card">
          <span class="ac-03__media"><img src="https://images.unsplash.com/photo-1506744038136-46273834b3fb?q=80&w=800&auto=format&fit=crop" alt="Lake reflecting a wooded shoreline" loading="lazy" decoding="async" width="800" height="500"></span>
          <div class="ac-03__body"><h3 class="ac-03__name">Off the main thread</h3><p class="ac-03__copy">No listener, no rAF, no layout thrash — the compositor scrubs it while JS is busy.</p></div>
        </article>
        <p class="ac-03__end">End of gallery</p>
      </div>
    </div>
    <p class="ac-03__chip" aria-hidden="true">animation-timeline:view() · animation-range:entry/cover · scroll(nearest) progress rail · linear scrub</p>
  </div>
</section>
```
## CSS
```css
.ac-03,
.ac-03 *,
.ac-03 *::before,
.ac-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ac-03 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --ac-03-bg: oklch(0.15 0.015 265);
  --ac-03-card: oklch(0.21 0.018 265);
  --ac-03-ink: oklch(0.97 0.004 260);
  --ac-03-mut: oklch(0.70 0.02 265);
  --ac-03-acc: oklch(0.78 0.15 198);
  --ac-03-line: oklch(1 0 0/.11);
  background: var(--ac-03-bg);
  color: var(--ac-03-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.ac-03__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 16px;
  padding: clamp(18px,4vw,48px);
  background: radial-gradient(100% 70% at 50% 0%,color-mix(in oklch,var(--ac-03-acc) 12%,transparent),transparent 60%);
}

.ac-03__panel {
  width: min(100%,700px);
  height: min(76vh,620px);
  display: grid;
  grid-template-rows: auto 1fr;
  border: 1px solid var(--ac-03-line);
  border-radius: 22px;
  overflow: hidden;
  background: oklch(0.18 0.016 265);
  box-shadow: 0 40px 80px -40px oklch(0 0 0/.8);
}

.ac-03__bar {
  height: 3px;
  background: oklch(1 0 0/.08);
}

.ac-03__rail {
  display: block;
  height: 100%;
  width: 100%;
  transform-origin: 0 50%;
  background: linear-gradient(90deg,var(--ac-03-acc),color-mix(in oklch,var(--ac-03-acc) 40%,oklch(0.75 0.19 320)));
  transform: scaleX(0);
}

.ac-03__scroller {
  overflow: auto;
  scrollbar-width: thin;
  scrollbar-color: var(--ac-03-line) transparent;
  padding: clamp(18px,4vw,30px);
  display: block;
  scroll-behavior: smooth;
}

.ac-03__scroller:focus-visible {
  outline: 2px solid var(--ac-03-acc);
  outline-offset: -2px;
}

.ac-03__lead {
  display: grid;
  gap: 8px;
  padding-block: 8px 4px;
  margin-bottom: clamp(22px,5vw,44px);
  text-align: center;
}

.ac-03__eyebrow {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--ac-03-acc);
}

.ac-03__title {
  font-size: clamp(21px,3.6vw,30px);
  font-weight: 650;
  line-height: 1.14;
  letter-spacing: -.03em;
  text-wrap: balance;
}

.ac-03__sub {
  font-size: 13.5px;
  color: var(--ac-03-mut);
  text-wrap: pretty;
}

.ac-03__sub code,
.ac-03__copy code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  background: oklch(1 0 0/.08);
  padding: 2px 5px;
  border-radius: 5px;
}

.ac-03__card {
  display: grid;
  gap: 0;
  margin-bottom: clamp(22px,5vw,44px);
  border: 1px solid var(--ac-03-line);
  border-radius: 20px;
  overflow: hidden;
  background: var(--ac-03-card);
  transform-origin: 50% 60%;
}

.ac-03__media {
  display: block;
  aspect-ratio: 21/9;
  background: linear-gradient(135deg,oklch(0.34 0.06 220),oklch(0.25 0.04 280));
}

.ac-03__media img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.ac-03__body {
  display: grid;
  gap: 7px;
  padding: 16px 18px 20px;
}

.ac-03__name {
  font-size: 16.5px;
  font-weight: 640;
  letter-spacing: -.02em;
}

.ac-03__copy {
  font-size: 13.5px;
  line-height: 1.55;
  color: var(--ac-03-mut);
  text-wrap: pretty;
}

.ac-03__end {
  text-align: center;
  font-size: 12px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--ac-03-mut);
  padding-block: 10px 30px;
}

@supports (animation-timeline: view()) {
  .ac-03__card {
    animation: ac-03-in linear both;
    animation-timeline: view();
    animation-range: entry 15% cover 42%;
  }

  .ac-03__rail {
    animation: ac-03-rail linear both;
    animation-timeline: scroll(nearest);
  }
}

@supports not (animation-timeline: view()) {
  .ac-03__rail {
    transform: scaleX(.35);
  }
}

@keyframes ac-03-in {
  from {
    opacity: 0;
    transform: scale(.86) translateY(38px);
    filter: blur(10px);
  }

  to {
    opacity: 1;
    transform: none;
    filter: blur(0);
  }
}

@keyframes ac-03-rail {
  from {
    transform: scaleX(0);
  }

  to {
    transform: scaleX(1);
  }
}

.ac-03__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  line-height: 1.6;
  color: var(--ac-03-mut);
  padding: 8px 15px;
  border: 1px solid var(--ac-03-line);
  border-radius: 99px;
  text-align: center;
  max-width: min(100%,660px);
}

@media (prefers-reduced-motion: reduce) {
  .ac-03__card {
    animation-timeline: auto;
    animation-duration: 1ms;
  }

  .ac-03__scroller {
    scroll-behavior: auto;
  }
}
```
