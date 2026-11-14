---
source: "codefronts"
url: "https://codefronts.com/layouts/css-timelines/brutalist-grid/"
title: "Horizontal Panorama Timeline — Vertical Scroll Drives Sideways Travel"
section: "layouts"
category: "css-timelines"
category_name: "CSS Timelines"
description: "The collection's finale: a century of milestones laid out as one wide horizontal panorama that travels sideways as you scroll DOWN — the sticky-viewport +…"
has_js: "false"
---

Here's a working CSS Timeline from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Horizontal Panorama Timeline — Vertical Scroll Drives Sideways Travel
Source: https://codefronts.com/layouts/css-timelines/brutalist-grid/

The collection's finale: a century of milestones laid out as one wide horizontal panorama that travels sideways as you scroll DOWN — the sticky-viewport + scroll-driven-transform pattern behind award-site history pages, finally possible in pure CSS with animation-timeline: scroll(). No scroll hijacking, no wheel listeners: the scrollbar keeps its native physics and the panorama is simply mapped onto it.
## HTML
```html
<section class="tls-26" aria-label="Horizontal panorama timeline demo">
  <div class="tls-26__runway">
    <div class="tls-26__stage">
      <p class="tls-26__hint">Keep scrolling — the century moves sideways ↓</p>
      <div class="tls-26__window">
        <ol class="tls-26__track" role="list">
          <li class="tls-26__card"><time datetime="1926">1926</time><h4>Television demonstrated</h4><p>Baird's flickering 30-line image convinces a skeptical press in a Soho attic.</p></li>
          <li class="tls-26__card"><time datetime="1947">1947</time><h4>The transistor</h4><p>Three Bell Labs physicists replace the vacuum tube and miniaturize the century.</p></li>
          <li class="tls-26__card"><time datetime="1969">1969</time><h4>ARPANET's first message</h4><p>'LO' — the network crashes before the 'GIN'. It never really stops after that.</p></li>
          <li class="tls-26__card"><time datetime="1989">1989</time><h4>The Web proposed</h4><p>'Vague, but exciting' — the most consequential margin note in computing.</p></li>
          <li class="tls-26__card"><time datetime="2007">2007</time><h4>The smartphone era</h4><p>A phone, an iPod and an internet communicator walk into a keynote.</p></li>
          <li class="tls-26__card"><time datetime="2026">2026</time><h4>CSS animates on scroll</h4><p>The scrollbar becomes a timeline — this page is the demo.</p></li>
        </ol>
      </div>
      <div class="tls-26__ruler" aria-hidden="true"><span>1920s</span><span>1940s</span><span>1960s</span><span>1980s</span><span>2000s</span><span>2020s</span></div>
    </div>
  </div>
</section>
```
## CSS
```css
.tls-26,
.tls-26 *,
.tls-26 *::before,
.tls-26 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tls-26 {
  min-height: 100vh;
  width: 100%;
  --tl-accent: #f59e0b;
  --tl-line: #31313b;
  --tl-ink: #f2f2f4;
  --tl-mut: #9b9ba8;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #16161c;
}

.tls-26__runway {
  height: 320vh;
}

.tls-26__stage {
  position: sticky;
  top: 0;
  height: 100vh;
  display: grid;
  grid-template-rows: auto 1fr auto;
  gap: 10px;
  padding: 28px 0;
  overflow: clip;
}

.tls-26__hint {
  text-align: center;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--tl-mut);
}

.tls-26__window {
  display: grid;
  align-items: center;
  overflow: clip;
}

.tls-26__track {
  list-style: none;
  display: flex;
  gap: 40px;
  width: max-content;
  padding: 0 8vw;
  position: relative;
  align-items: stretch;
}

.tls-26__track::before {
  content: '';
  position: absolute;
  left: 0;
  right: 0;
  top: 50%;
  height: 2px;
  background: var(--tl-line);
}

.tls-26__card {
  position: relative;
  flex: none;
  width: min(340px,72vw);
  background: #1e1e26;
  border: 1px solid var(--tl-line);
  border-radius: 16px;
  padding: 22px 24px;
  z-index: 1;
}

.tls-26__card::before {
  content: '';
  position: absolute;
  top: -27px;
  left: 28px;
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: var(--tl-accent);
  border: 3px solid #16161c;
}

.tls-26__card time {
  font-size: 26px;
  font-weight: 800;
  color: var(--tl-accent);
  letter-spacing: -.02em;
}

.tls-26__card h4 {
  font-size: 16.5px;
  font-weight: 750;
  color: var(--tl-ink);
  margin: 8px 0 7px;
  letter-spacing: -.01em;
}

.tls-26__card p {
  font-size: 13.5px;
  line-height: 1.6;
  color: var(--tl-mut);
  text-wrap: pretty;
}

.tls-26__ruler {
  display: flex;
  justify-content: space-between;
  padding: 0 6vw;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .14em;
  color: #55555f;
}

@supports (animation-timeline: scroll()) {
  @media (prefers-reduced-motion: no-preference) {
    .tls-26__track {
      animation: tls-26-pan linear both;
      animation-timeline: scroll();
    }

    @keyframes tls-26-pan {
      to {
        transform: translateX(calc(-100% + 100vw));
      }
    }
  }

  @media (prefers-reduced-motion: reduce) {
    .tls-26__runway {
      height: auto;
    }

    .tls-26__stage {
      position: static;
      height: auto;
    }

    .tls-26__window {
      overflow-x: auto;
    }
  }
}

@supports not (animation-timeline: scroll()) {
  .tls-26__runway {
    height: auto;
  }

  .tls-26__stage {
    position: static;
    height: auto;
  }

  .tls-26__window {
    overflow-x: auto;
    scroll-snap-type: x proximity;
  }

  .tls-26__card {
    scroll-snap-align: center;
  }
}
```

## JavaScript
```js
/* No JavaScript — vertical progress through the 320vh runway drives translateX via animation-timeline: scroll(); the @supports not (and reduced-motion) paths serve the same century as a native horizontal scroller. */
```
