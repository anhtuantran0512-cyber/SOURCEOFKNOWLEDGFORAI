---
source: "codefronts"
url: "https://codefronts.com/layouts/css-timelines/cinematic-filmstrip/"
title: "Cinematic Filmstrip Timeline — Scroll-Snap Career Frames"
section: "layouts"
category: "css-timelines"
category_name: "CSS Timelines"
description: "A widescreen horizontal narrative: each chapter of a career or story is a letterboxed 'frame' in a scroll-snapping strip with chapter numbers, act labels and…"
has_js: "false"
---

Here's a working CSS Timeline from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Cinematic Filmstrip Timeline — Scroll-Snap Career Frames
Source: https://codefronts.com/layouts/css-timelines/cinematic-filmstrip/

A widescreen horizontal narrative: each chapter of a career or story is a letterboxed 'frame' in a scroll-snapping strip with chapter numbers, act labels and a progress dot rail driven by scroll-snap alone — the storytelling layout for portfolios, agency case studies and anniversary microsites.
## HTML
```html
<section class="tls-17" aria-label="Filmstrip career timeline demo">
  <header class="tls-17__head"><h3 class="tls-17__h">Fifteen years in five frames</h3><p class="tls-17__hint">Scroll sideways →</p></header>
  <ol class="tls-17__strip" role="list" tabindex="0" aria-label="Career chapters, horizontally scrollable">
    <li class="tls-17__frame" style="--g:linear-gradient(150deg,#1d3a5f,#0a1526)">
      <p class="tls-17__act">Act I · <time datetime="2011">2011</time></p>
      <p class="tls-17__no" aria-hidden="true">01</p>
      <h4 class="tls-17__t">The first studio job</h4>
      <p class="tls-17__d">Junior designer. Learned that shipping beats perfect — by shipping something imperfect.</p>
    </li>
    <li class="tls-17__frame" style="--g:linear-gradient(150deg,#4a2c15,#170d05)">
      <p class="tls-17__act">Act II · <time datetime="2015">2015</time></p>
      <p class="tls-17__no" aria-hidden="true">02</p>
      <h4 class="tls-17__t">Freelance years</h4>
      <p class="tls-17__d">Forty clients, three time zones, one folding desk. Rate doubled the year I learned to say no.</p>
    </li>
    <li class="tls-17__frame" style="--g:linear-gradient(150deg,#14453d,#04120f)">
      <p class="tls-17__act">Act III · <time datetime="2019">2019</time></p>
      <p class="tls-17__no" aria-hidden="true">03</p>
      <h4 class="tls-17__t">Building the team</h4>
      <p class="tls-17__d">First design hire → design director. The work became making other people's work better.</p>
    </li>
    <li class="tls-17__frame" style="--g:linear-gradient(150deg,#4c1d3d,#160414)">
      <p class="tls-17__act">Act IV · <time datetime="2023">2023</time></p>
      <p class="tls-17__no" aria-hidden="true">04</p>
      <h4 class="tls-17__t">The product bet</h4>
      <p class="tls-17__d">Left the safe seat to co-found a tool for design systems. Terrifying. Correct.</p>
    </li>
    <li class="tls-17__frame" style="--g:linear-gradient(150deg,#3d3d14,#121204)">
      <p class="tls-17__act">Act V · <time datetime="2026">now</time></p>
      <p class="tls-17__no" aria-hidden="true">05</p>
      <h4 class="tls-17__t">Still in the credits</h4>
      <p class="tls-17__d">10k teams use the thing. The next frame is unwritten on purpose.</p>
    </li>
  </ol>
</section>
```
## CSS
```css
.tls-17,
.tls-17 *,
.tls-17 *::before,
.tls-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tls-17 {
  min-height: 100vh;
  width: 100%;
  --tl-ink: #f2ede4;
  --tl-mut: #9a917f;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #0d0b08;
  padding: 56px 0 64px;
}

.tls-17__head {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  gap: 16px;
  padding: 0 clamp(20px,6vw,64px);
  margin-bottom: 26px;
}

.tls-17__h {
  font-family: Georgia,serif;
  font-size: clamp(20px,3.4vw,28px);
  font-weight: 700;
  color: var(--tl-ink);
  letter-spacing: -.01em;
}

.tls-17__hint {
  font-size: 11px;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--tl-mut);
}

.tls-17__strip {
  list-style: none;
  display: flex;
  gap: 22px;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  scroll-padding-inline: clamp(20px,6vw,64px);
  padding: 4px clamp(20px,6vw,64px) 18px;
  scrollbar-width: thin;
  scrollbar-color: #3d382f transparent;
}

.tls-17__strip:focus-visible {
  outline: 2px solid #c8b98a;
  outline-offset: 4px;
}

.tls-17__frame {
  flex: 0 0 min(560px,88%);
  scroll-snap-align: center;
  aspect-ratio: 21/10;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  gap: 6px;
  background: var(--g);
  border-radius: 6px;
  padding: 28px 30px;
  position: relative;
  overflow: hidden;
}

.tls-17__frame::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg,rgba(6,5,3,.25),transparent 35%,transparent 55%,rgba(6,5,3,.72));
}

.tls-17__act {
  position: relative;
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .24em;
  text-transform: uppercase;
  color: #cdbd93;
}

.tls-17__no {
  position: absolute;
  top: 10px;
  right: 22px;
  font-family: Georgia,serif;
  font-size: clamp(56px,9vw,88px);
  font-weight: 700;
  color: rgba(242,237,228,.12);
  line-height: 1;
}

.tls-17__t {
  position: relative;
  font-family: Georgia,serif;
  font-size: clamp(20px,3vw,27px);
  font-weight: 700;
  color: var(--tl-ink);
  letter-spacing: -.01em;
}

.tls-17__d {
  position: relative;
  font-size: 13.5px;
  line-height: 1.55;
  color: #c9c0af;
  max-width: 44ch;
  text-wrap: pretty;
}

@media (max-width: 560px) {
  .tls-17__strip {
    flex-direction: column;
    overflow: visible;
    scroll-snap-type: none;
  }

  .tls-17__frame {
    flex-basis: auto;
    aspect-ratio: auto;
    min-height: 180px;
  }

  .tls-17__hint {
    display: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the slide feel is scroll-snap-type:x mandatory + scroll-snap-align:center; the browser owns momentum, touch, keyboard and RTL. */
```
