---
source: "codefronts"
url: "https://codefronts.com/layouts/css-blog-layouts/photo-essay-long-form-story/"
title: "Photo Essay Long-Form Story"
section: "layouts"
category: "css-blog-layouts"
category_name: "CSS Blog Layouts"
description: "A visual story where the photographs run the page: edge-to-edge plates, a sticky-image chapter where text scrolls over a held frame, diptych pairs that share…"
has_js: "false"
---

Here's a working CSS Blog Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Photo Essay Long-Form Story
Source: https://codefronts.com/layouts/css-blog-layouts/photo-essay-long-form-story/

A visual story where the photographs run the page: edge-to-edge plates, a sticky-image chapter where text scrolls over a held frame, diptych pairs that share a caption, and captions set small and quiet in the margin. Chrome is deliberately almost absent — no sidebar, no share bar, no related rail, nothing competing with the image.
## HTML
```html
<article class="bl-14">
  <div class="bl-14__doc">
  <header class="bl-14__hero">
    <img src="https://images.unsplash.com/photo-1519681393784-d120267933ba?w=1800&amp;q=72&amp;auto=format&amp;fit=crop" alt="A snow-covered mountain ridge under a deep blue night sky" width="1800" height="1100" loading="eager" fetchpriority="high" decoding="async">
    <div class="bl-14__heroText">
      <p class="bl-14__rubric">Photo essay</p>
      <h1>Nine winters on the same ridge</h1>
      <p class="bl-14__credit">Photographs and text by <a href="#">Kaisa Lindroth</a></p>
    </div>
  </header>

  <p class="bl-14__standfirst">Every February since 2017, the same six kilometres of ridge above Kilpisjärvi. The route has not changed. Almost everything else has.</p>

  <p>The first year I came here it was to photograph the light, which lasts about four hours in February and arrives sideways. By the third year I was photographing the snow line, because it had moved, and by the sixth I was photographing the people who measure it.</p>

  <figure class="bl-14__plate">
    <img src="https://images.unsplash.com/photo-1483728642387-6c3bdd6c93e5?w=1800&amp;q=72&amp;auto=format&amp;fit=crop" alt="Low sun across a frozen plateau with wind-carved snow" width="1800" height="1000" loading="lazy" decoding="async">
    <figcaption><span>02</span> The plateau at 11:40, the first full light of the day. Wind carving like this lasts a week at most.</figcaption>
  </figure>

  <p>What a repeated photograph gives you is not evidence, exactly. It is a way of noticing. Nobody looking at one frame from 2017 and one from 2026 would draw a conclusion; laid in sequence, the nine of them ask a question the individual images cannot.</p>

  <section class="bl-14__hold" aria-label="The north face">
    <img src="https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=1600&amp;q=72&amp;auto=format&amp;fit=crop" alt="A wide view of a valley with a thin frozen river running through it" width="1600" height="1000" loading="lazy" decoding="async">
    <div class="bl-14__holdText">
      <p>The north face holds its snow longest, which is why the measuring stakes are there and not on the sunlit side.</p>
      <p>In 2017 the lowest stake was buried to the collar by mid-February. This year it was visible for all nine days I was on the mountain.</p>
      <p>Nobody in the research hut talks about it dramatically. They read the stake, they write the number, they make coffee. The drama is entirely in the aggregate.</p>
    </div>
  </section>

  <figure class="bl-14__pair">
    <img src="https://images.unsplash.com/photo-1418985991508-e47386d96a71?w=900&amp;q=72&amp;auto=format&amp;fit=crop" alt="A stand of frost-covered birch trees at the treeline" width="900" height="1100" loading="lazy" decoding="async">
    <img src="https://images.unsplash.com/photo-1439853949127-fa647821eba0?w=900&amp;q=72&amp;auto=format&amp;fit=crop" alt="Bare rock emerging through thin snow cover on a slope" width="900" height="1100" loading="lazy" decoding="async">
    <figcaption><span>03 &amp; 04</span> The treeline in 2018, left, and the same fifty metres in 2026. Birch has moved roughly eleven metres upslope in nine years.</figcaption>
  </figure>

  <p>I keep the frames identical on purpose — same lens, same time of day, same position marked by a cairn I rebuild each year. It is a deliberately boring method, and it is the only thing that makes the pictures comparable.</p>

  <blockquote class="bl-14__quote">
    <p>“You are not documenting a place. You are documenting your own returns to it.”</p>
    <cite>— Hilkka Rautio, glaciologist, Kilpisjärvi station</cite>
  </blockquote>

  <figure class="bl-14__plate">
    <img src="https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?w=1800&amp;q=72&amp;auto=format&amp;fit=crop" alt="Fog filling a forested valley below a ridge at dawn" width="1800" height="1000" loading="lazy" decoding="async">
    <figcaption><span>09</span> The last morning, 2026. Fog to the valley floor — the first time in nine years I have seen it this low in February.</figcaption>
  </figure>

  <p class="bl-14__coda">Kaisa Lindroth is a photographer based in Oulu. The full nine-year sequence, with the station's stake measurements, is published as a book this autumn.</p>
  </div>
</article>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300&family=Archivo:wght@400;500;600&display=swap');

.bl-14 {
  --bg: #0a0a0a;
  --text: #f4f3f1;
  --muted: #8f8d89;
  --line: #232322;
  --acc: #d6d3cd;
  --text-measure: 58ch;
  --plate: 82svh;
  --serif: "Cormorant Garamond",ui-serif,Georgia,serif;
  --sans: "Archivo",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
}

@supports (color: oklch(50% 0 0)) {
  .bl-14 {
    --bg: oklch(11% .002 90);
    --text: oklch(96% .004 90);
    --muted: oklch(64% .006 90);
    --line: oklch(22% .004 90);
  }
}

@media (prefers-color-scheme: light) {
  .bl-14:not([data-theme="dark"]) {
    --bg: #fbfaf8;
    --text: #111110;
    --muted: #6a6862;
    --line: #e4e2dd;
    --acc: #2b2a27;
  }
}

.bl-14[data-theme="light"] {
  --bg: #fbfaf8;
  --text: #111110;
  --muted: #6a6862;
  --line: #e4e2dd;
  --acc: #2b2a27;
}

.bl-14 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  color: var(--text);
  font-family: var(--serif);
  -webkit-font-smoothing: antialiased;
}

.bl-14,
.bl-14 *,
.bl-14 *::before,
.bl-14 *::after {
  box-sizing: border-box;
}

.bl-14__doc {
  display: grid;
  grid-template-columns: [full-start] minmax(1.25rem,1fr) [text-start] min(var(--text-measure),100% - 2.5rem) [text-end] minmax(1.25rem,1fr) [full-end];
  padding-bottom: clamp(4rem,10vw,8rem);
  row-gap: clamp(1.5rem,3vw,2.25rem);
}

.bl-14__doc > * {
  grid-column: text;
  margin: 0;
}

.bl-14 a {
  color: inherit;
}

.bl-14 :focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.bl-14 img {
  display: block;
  width: 100%;
  max-width: 100%;
  height: 100%;
  object-fit: cover;
  background: var(--line);
}

.bl-14 ::selection {
  background: color-mix(in oklab,var(--acc) 30%,transparent);
  color: var(--bg);
}

.bl-14__hero {
  grid-column: full;
  position: relative;
  overflow: clip;
  min-height: min(94svh,52rem);
  display: grid;
  align-items: end;
  isolation: isolate;
  margin-bottom: clamp(1.5rem,4vw,3rem);
}

.bl-14__hero img {
  position: absolute;
  inset: 0;
  z-index: -2;
}

.bl-14__hero::after {
  content: "";
  position: absolute;
  inset: 0;
  z-index: -1;
  background: linear-gradient(to top,rgba(4,4,4,.88) 5%,rgba(4,4,4,.25) 45%,rgba(4,4,4,.35) 100%);
}

.bl-14__heroText {
  display: grid;
  gap: .85rem;
  padding: clamp(2rem,6vw,5rem) clamp(1.25rem,6vw,6rem);
  color: #fff;
}

.bl-14__rubric {
  margin: 0;
  font-family: var(--sans);
  font-size: .625rem;
  font-weight: 600;
  letter-spacing: .28em;
  text-transform: uppercase;
  opacity: .85;
}

.bl-14__hero h1 {
  margin: 0;
  font-weight: 300;
  font-size: clamp(2.5rem,8vw,6.5rem);
  line-height: .94;
  letter-spacing: -.02em;
  text-wrap: balance;
}

.bl-14__credit {
  margin: 0;
  font-family: var(--sans);
  font-size: .75rem;
  letter-spacing: .06em;
  opacity: .8;
}

.bl-14__credit a {
  text-decoration: underline;
  text-underline-offset: .25em;
}

.bl-14__standfirst {
  font-size: clamp(1.375rem,3vw,1.875rem);
  line-height: 1.42;
  font-weight: 300;
  letter-spacing: -.01em;
  text-wrap: pretty;
}

.bl-14__doc > p {
  font-size: clamp(1.125rem,1.6vw,1.3125rem);
  line-height: 1.72;
  text-wrap: pretty;
  color: color-mix(in oklab,var(--text) 88%,transparent);
}

.bl-14__plate {
  grid-column: full;
  min-width: 0;
  overflow: clip;
  display: grid;
  gap: .75rem;
  margin-block: clamp(1.5rem,4vw,3rem);
}

.bl-14__plate img {
  max-inline-size: 100%;
  height: var(--plate);
  max-height: 88svh;
}

.bl-14__plate figcaption,
.bl-14__pair figcaption {
  padding-inline: clamp(1.25rem,6vw,6rem);
  font-family: var(--sans);
  font-size: .75rem;
  line-height: 1.6;
  color: var(--muted);
  max-width: 60ch;
}

.bl-14__plate figcaption span,
.bl-14__pair figcaption span {
  color: var(--text);
  font-weight: 600;
  margin-inline-end: .5rem;
  font-variant-numeric: tabular-nums;
}

@supports (animation-timeline: view()) {
  @media (prefers-reduced-motion: no-preference) {
    .bl-14__plate img {
      animation: bl-14-zoom linear both;
      animation-timeline: view();
      animation-range: entry 0% exit 100%;
    }

    @keyframes bl-14-zoom {
      from {
        scale: 1.08;
      }

      to {
        scale: 1;
      }
    }
  }
}

.bl-14__hold {
  grid-column: full;
  position: relative;
  display: grid;
  grid-template-columns: minmax(0,1fr) minmax(0,1fr);
  align-items: start;
  margin-block: clamp(2rem,5vw,4rem);
}

.bl-14__hold img {
  position: sticky;
  top: 0;
  height: 100svh;
}

.bl-14__holdText {
  display: grid;
  gap: clamp(3rem,14vh,9rem);
  padding: clamp(4rem,18vh,12rem) clamp(1.5rem,5vw,5rem);
}

.bl-14__holdText p {
  margin: 0;
  font-size: clamp(1.25rem,2.4vw,1.75rem);
  line-height: 1.45;
  font-weight: 300;
  text-wrap: pretty;
}

.bl-14__pair {
  grid-column: full;
  display: grid;
  grid-template-columns: repeat(2,minmax(0,1fr));
  gap: .5rem;
  margin-block: clamp(1.5rem,4vw,3rem);
}

.bl-14__pair img {
  aspect-ratio: 4/5;
}

.bl-14__pair figcaption {
  grid-column: 1/-1;
  padding-top: .5rem;
}

.bl-14__quote {
  margin-block: clamp(2rem,5vw,3.5rem);
  display: grid;
  gap: .85rem;
  text-align: center;
}

.bl-14__quote p {
  margin: 0;
  font-size: clamp(1.625rem,4vw,2.5rem);
  line-height: 1.2;
  font-weight: 300;
  font-style: italic;
  letter-spacing: -.015em;
  text-wrap: balance;
}

.bl-14__quote cite {
  font-family: var(--sans);
  font-style: normal;
  font-size: .6875rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
}

.bl-14__coda {
  margin-top: clamp(2rem,4vw,3rem);
  padding-top: 1.5rem;
  border-top: 1px solid var(--line);
  font-family: var(--sans);
  font-size: .8125rem !important;
  line-height: 1.7 !important;
  color: var(--muted);
}

@media (max-width: 52rem) {
  .bl-14__hold {
    grid-template-columns: minmax(0,1fr);
  }

  .bl-14__hold img {
    position: static;
    height: 70svh;
  }

  .bl-14__holdText {
    gap: 1.5rem;
    padding: 2rem clamp(1.25rem,5vw,3rem);
  }

  .bl-14__pair {
    grid-template-columns: minmax(0,1fr);
  }
}

@media (prefers-reduced-motion: reduce) {
  .bl-14 * {
    animation: none !important;
    transition: none !important;
  }
}
```

## JavaScript
```js


```
