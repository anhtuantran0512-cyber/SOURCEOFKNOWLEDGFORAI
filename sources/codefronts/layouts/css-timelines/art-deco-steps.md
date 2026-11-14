---
source: "codefronts"
url: "https://codefronts.com/layouts/css-timelines/art-deco-steps/"
title: "Reading-Progress Timeline — animation-timeline: scroll() Article Tracker"
section: "layouts"
category: "css-timelines"
category_name: "CSS Timelines"
description: "A long-read companion: a progress bar that fills as the article scrolls and a chapter rail whose dots light up as each section passes — both driven by the…"
has_js: "false"
---

Here's a working CSS Timeline from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Reading-Progress Timeline — animation-timeline: scroll() Article Tracker
Source: https://codefronts.com/layouts/css-timelines/art-deco-steps/

A long-read companion: a progress bar that fills as the article scrolls and a chapter rail whose dots light up as each section passes — both driven by the CSS scroll() and view() timelines, the pure-CSS replacement for the scroll-listener progress bars every publisher ships in JavaScript today.
## HTML
```html
<section class="tls-20" aria-label="Reading progress timeline demo">
  <div class="tls-20__frame">
    <div class="tls-20__scroller" tabindex="0">
      <header class="tls-20__bar">
        <p class="tls-20__label">The State of CSS · 12 min read</p>
        <div class="tls-20__track" aria-hidden="true"><div class="tls-20__fill"></div></div>
      </header>
      <article class="tls-20__article">
        <section class="tls-20__sec">
          <h4 class="tls-20__h"><span class="tls-20__dot" aria-hidden="true"></span>1 · The layout wars are over</h4>
          <p>Grid and flexbox settled the argument a decade ago, and the last float-based holdouts have quietly refactored. What remains is choosing the right tool: one-dimensional flow to flexbox, two-dimensional structure to grid, and — since subgrid — nested structure to the parent's tracks.</p>
          <p>The practical consequence is that layout bugs have become placement bugs. We no longer fight the engine; we mis-declare our intent to it. That is enormous progress.</p>
        </section>
        <section class="tls-20__sec">
          <h4 class="tls-20__h"><span class="tls-20__dot" aria-hidden="true"></span>2 · Components query themselves</h4>
          <p>Container queries ended the era of the viewport as the only breakpoint. A card now reshapes for the sidebar it lives in, not the monitor it happens to be displayed on — and design systems finally ship components that are honestly portable.</p>
          <p>The mental shift matters more than the syntax: responsive design becomes a property of the component, not of the page.</p>
        </section>
        <section class="tls-20__sec">
          <h4 class="tls-20__h"><span class="tls-20__dot" aria-hidden="true"></span>3 · The scrollbar becomes a timeline</h4>
          <p>Scroll-driven animations moved an entire genre of JavaScript — progress bars, reveal-on-scroll, parallax — into declarative CSS that runs off the main thread. This very progress bar is one of them: no listener, no rAF loop, no jank budget.</p>
          <p>The rule of thumb: if an effect is a pure function of scroll position, it belongs to the compositor now.</p>
        </section>
        <section class="tls-20__sec">
          <h4 class="tls-20__h"><span class="tls-20__dot" aria-hidden="true"></span>4 · What to learn next</h4>
          <p>:has() for relational styling, view transitions for state changes, anchor positioning for tooltips and menus. None of them are exotic anymore — they are simply what CSS is.</p>
        </section>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
.tls-20,
.tls-20 *,
.tls-20 *::before,
.tls-20 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tls-20 {
  min-height: 100vh;
  width: 100%;
  --tl-accent: #c2410c;
  --tl-line: #f3e5dc;
  --tl-ink: #2b1d14;
  --tl-mut: #8a7263;
  font-family: Georgia,'Times New Roman',serif;
  background: #fdf9f6;
  padding: 64px 24px;
  display: grid;
  place-items: center;
}

.tls-20__frame {
  width: min(620px,100%);
}

.tls-20__scroller {
  height: 420px;
  overflow-y: auto;
  background: #fff;
  border: 1px solid var(--tl-line);
  border-radius: 16px;
  box-shadow: 0 10px 34px -22px rgb(43 29 20 / .3);
}

.tls-20__bar {
  position: sticky;
  top: 0;
  z-index: 2;
  background: #fff;
  padding: 14px 26px 0;
  border-bottom: 1px solid var(--tl-line);
}

.tls-20__label {
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--tl-mut);
  padding-bottom: 10px;
}

.tls-20__track {
  height: 4px;
  background: var(--tl-line);
  border-radius: 2px 2px 0 0;
  overflow: hidden;
}

.tls-20__fill {
  height: 100%;
  background: var(--tl-accent);
  transform-origin: left;
}

.tls-20__article {
  padding: 10px 26px 30px;
}

.tls-20__sec {
  padding: 18px 0 10px;
}

.tls-20__h {
  display: flex;
  align-items: center;
  gap: 10px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-size: 14px;
  font-weight: 800;
  color: var(--tl-ink);
  letter-spacing: -.01em;
  margin-bottom: 10px;
}

.tls-20__dot {
  flex: none;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  border: 2.5px solid var(--tl-accent);
  background: transparent;
}

.tls-20__sec p {
  font-size: 15.5px;
  line-height: 1.7;
  color: #4a3a2e;
  margin-bottom: 12px;
  text-wrap: pretty;
}

@supports (animation-timeline: scroll()) {
  .tls-20__fill {
    transform: scaleX(0);
    animation: tls-20-grow linear both;
    animation-timeline: scroll(nearest);
  }

  @keyframes tls-20-grow {
    to {
      transform: scaleX(1);
    }
  }

  .tls-20__sec {
    view-timeline-name: --tls25-sec;
  }

  .tls-20__dot {
    animation: tls-20-dot linear both;
    animation-timeline: view(nearest);
    animation-range: entry 0% entry 100%;
  }

  @keyframes tls-20-dot {
    to {
      background: var(--tl-accent);
    }
  }
}
```

## JavaScript
```js
/* No JavaScript — the bar is animation-timeline: scroll(nearest) with a scaleX fill (compositor-only); chapter dots fill against per-section view() timelines. Remove the demo's fixed-height scroller and the same CSS tracks the page. */
```
