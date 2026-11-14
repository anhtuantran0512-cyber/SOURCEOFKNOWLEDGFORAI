---
source: "codefronts"
url: "https://codefronts.com/layouts/css-timelines/scroll-driven-reveal-timeline-animation-timeline-view-entrances/"
title: "Scroll-Driven Reveal Timeline — animation-timeline: view() Entrances"
section: "layouts"
category: "css-timelines"
category_name: "CSS Timelines"
description: "The scroll-driven flagship: milestones fade-and-rise into place and their markers pop exactly as they scroll into view — driven entirely by the CSS…"
has_js: "false"
---

Here's a working CSS Timeline from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Scroll-Driven Reveal Timeline — animation-timeline: view() Entrances
Source: https://codefronts.com/layouts/css-timelines/scroll-driven-reveal-timeline-animation-timeline-view-entrances/

The scroll-driven flagship: milestones fade-and-rise into place and their markers pop exactly as they scroll into view — driven entirely by the CSS animation-timeline: view() API, zero IntersectionObserver, zero JavaScript. Scrub the page up and down and the entrances play forwards and backwards like a scrubbing video, because the scrollbar IS the timeline.
## HTML
```html
<section class="tls-06" aria-label="Scroll-driven reveal timeline demo">
  <div class="tls-06__inner">
    <p class="tls-06__eyebrow">Scroll to reveal — then scroll back up</p>
    <h3 class="tls-06__title">Product journey</h3>
    <ol class="tls-06__list" role="list">
      <li class="tls-06__item">
        <div class="tls-06__card">
          <time class="tls-06__date" datetime="2024-03">March 2024</time>
          <h4 class="tls-06__h">First prototype</h4>
          <p class="tls-06__p">A weekend build shared with 12 friends. Eight replied the same day.</p>
        </div>
      </li>
      <li class="tls-06__item">
        <div class="tls-06__card">
          <time class="tls-06__date" datetime="2024-09">September 2024</time>
          <h4 class="tls-06__h">Private beta</h4>
          <p class="tls-06__p">400 teams on a waitlist. The onboarding survived all of them.</p>
        </div>
      </li>
      <li class="tls-06__item">
        <div class="tls-06__card">
          <time class="tls-06__date" datetime="2025-02">February 2025</time>
          <h4 class="tls-06__h">Public launch</h4>
          <p class="tls-06__p">#1 on launch day. Servers held. Founders did not sleep.</p>
        </div>
      </li>
      <li class="tls-06__item">
        <div class="tls-06__card">
          <time class="tls-06__date" datetime="2025-11">November 2025</time>
          <h4 class="tls-06__h">10,000 customers</h4>
          <p class="tls-06__p">Profitability, a team of nine, and the roadmap the users wrote.</p>
        </div>
      </li>
      <li class="tls-06__item">
        <div class="tls-06__card">
          <time class="tls-06__date" datetime="2026-06">June 2026</time>
          <h4 class="tls-06__h">Platform v2</h4>
          <p class="tls-06__p">The rewrite nobody noticed — which was exactly the point.</p>
        </div>
      </li>
    </ol>
  </div>
</section>
```
## CSS
```css
.tls-06,
.tls-06 *,
.tls-06 *::before,
.tls-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tls-06 {
  min-height: 100vh;
  width: 100%;
  --tl-accent: #6d28d9;
  --tl-line: #e4e0ee;
  --tl-bg: #faf9fc;
  --tl-ink: #241f35;
  --tl-mut: #7a7490;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: var(--tl-bg);
  padding: 72px 24px 96px;
  display: grid;
  place-items: center;
}

.tls-06__inner {
  width: min(560px,100%);
}

.tls-06__eyebrow {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--tl-accent);
  margin-bottom: 8px;
}

.tls-06__title {
  font-size: clamp(24px,4vw,32px);
  font-weight: 800;
  color: var(--tl-ink);
  letter-spacing: -.02em;
  margin-bottom: 36px;
}

.tls-06__list {
  list-style: none;
  display: flex;
  flex-direction: column;
}

.tls-06__item {
  position: relative;
  padding: 0 0 40px 40px;
}

.tls-06__item::after {
  content: '';
  position: absolute;
  left: 7px;
  top: 26px;
  bottom: -8px;
  width: 2px;
  background: var(--tl-line);
}

.tls-06__item:last-child::after {
  display: none;
}

.tls-06__item::before {
  content: '';
  position: absolute;
  left: 0;
  top: 10px;
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background: var(--tl-bg);
  border: 4px solid var(--tl-accent);
  z-index: 1;
}

.tls-06__date {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--tl-accent);
}

.tls-06__h {
  font-size: 18px;
  font-weight: 750;
  color: var(--tl-ink);
  letter-spacing: -.01em;
  margin: 6px 0 6px;
}

.tls-06__p {
  font-size: 14px;
  line-height: 1.6;
  color: var(--tl-mut);
  text-wrap: pretty;
}

@supports (animation-timeline: view()) {
  .tls-06__card {
    animation: tls-06-rise linear both;
    animation-timeline: view();
    animation-range: entry 0% entry 65%;
  }

  .tls-06__item::before {
    animation: tls-06-pop linear both;
    animation-timeline: view();
    animation-range: entry 0% entry 65%;
  }

  @keyframes tls-06-rise {
    from {
      opacity: 0;
      transform: translateY(24px);
    }

    to {
      opacity: 1;
      transform: none;
    }
  }

  @keyframes tls-06-pop {
    0% {
      transform: scale(0);
    }

    60% {
      transform: scale(1.35);
    }

    100% {
      transform: scale(1);
    }
  }

  @media (prefers-reduced-motion: reduce) {
    .tls-06__card,
        .tls-06__item::before {
      animation: none;
    }
  }
}
```

## JavaScript
```js
/* No JavaScript — entrances are animation-timeline: view() with animation-range: entry 0% entry 65%; the @supports gate owns the hidden start state so unsupported browsers see the finished layout. */
```
