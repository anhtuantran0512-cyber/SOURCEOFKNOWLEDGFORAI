---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-dark-mode-ui/forest-dim/"
title: "Forest Dim Dark Mode Reading Surface"
section: "design-styles"
category: "css-dark-mode-ui"
category_name: "CSS Dark Mode UI"
description: "A reading surface tuned for length: a green-tinted near-black that scatters less than pure black, ink at a deliberate 12:1 rather than a harsh 18:1, a…"
has_js: "false"
---

Here's a working CSS Dark Mode UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Forest Dim Dark Mode Reading Surface
Source: https://codefronts.com/design-styles/css-dark-mode-ui/forest-dim/

A reading surface tuned for length: a green-tinted near-black that scatters less than pure black, ink at a deliberate 12:1 rather than a harsh 18:1, a 68-character measure, a drop cap and generous leading. Headline, byline, hero image and four paragraphs of real prose — plus a font-size control and a theme switch, both pure CSS, because a reader that cannot be adjusted is not a reader.
## HTML
```html
<div class="dmu-16">
  <div class="dmu-16__stage">
    <article class="dmu-16__article">
      <header class="dmu-16__head">
        <p class="dmu-16__kicker">Craft &middot; 9 min read</p>
        <h1 class="dmu-16__h1">The quiet discipline of reading at night</h1>
        <div class="dmu-16__bylineRow">
          <p class="dmu-16__byline">By <strong>Priya Sharma</strong> &middot; 14 August 2026</p>
          <div class="dmu-16__controls">
            <fieldset class="dmu-16__sizes">
              <legend class="dmu-16__sr">Text size</legend>
              <input class="dmu-16__sr" type="radio" name="dmu-16-size" id="dmu-16-sm">
              <label class="dmu-16__size" for="dmu-16-sm">A</label>
              <input class="dmu-16__sr" type="radio" name="dmu-16-size" id="dmu-16-md" checked>
              <label class="dmu-16__size dmu-16__size--md" for="dmu-16-md">A</label>
              <input class="dmu-16__sr" type="radio" name="dmu-16-size" id="dmu-16-lg">
              <label class="dmu-16__size dmu-16__size--lg" for="dmu-16-lg">A</label>
            </fieldset>
            <input class="dmu-16__sr" type="checkbox" id="dmu-16-toggle">
            <label class="dmu-16__toggle" for="dmu-16-toggle">
              <svg class="dmu-16__sun" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"><circle cx="12" cy="12" r="4"/><path d="M12 2.8v2M12 19.2v2M2.8 12h2M19.2 12h2M5.5 5.5 7 7M17 17l1.5 1.5M18.5 5.5 17 7M7 17l-1.5 1.5"/></svg>
              <svg class="dmu-16__moon" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M20 14.4A8.4 8.4 0 0 1 9.6 4a8.4 8.4 0 1 0 10.4 10.4Z"/></svg>
              <span class="dmu-16__sr">Toggle theme</span>
            </label>
          </div>
        </div>
      </header>

      <figure class="dmu-16__figure">
        <img src="https://picsum.photos/seed/forest-dim-2048/1200/700" width="1200" height="700" alt="Article hero placeholder — swap the src for your own image" loading="lazy" decoding="async">
        <figcaption>Hero placeholder, dimmed to 88&#37; brightness so a bright photograph never blows out the page.</figcaption>
      </figure>

      <div class="dmu-16__body">
        <p>The first thing you notice when you read for four hours on a dark screen is that contrast is not the same as legibility. Pure white on pure black measures beautifully and behaves badly: the letterforms bloom, the counters fill in, and by the third chapter your eyes are doing the work your typographer should have done.</p>
        <p>What actually helps is unglamorous. Give the text a measure it can return from &mdash; sixty-eight characters, not a hundred. Set the leading wider than you would on paper, because a backlit line has no physical edge to guide the eye. Then pull the ink back until it sits comfortably above the substrate rather than shouting off it.</p>
        <p>The tint matters more than it should. A substrate with a few degrees of green or blue in it scatters less across the retina than neutral black, which is why the best reading apps have never used <code>#000000</code>. It is a small choice that survives every other decision you make.</p>
        <p>None of this is a style. It is the same information architecture as the light theme, designed a second time for a different room and a different hour &mdash; which is the only definition of dark mode worth keeping.</p>
      </div>

      <footer class="dmu-16__foot">
        <span class="dmu-16__tag">Typography</span>
        <span class="dmu-16__tag">Accessibility</span>
        <span class="dmu-16__tag">Dark mode</span>
      </footer>
    </article>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,300..600;1,6..72,300..500&display=swap');

.dmu-16 {
  --forest: #0a1210;
  --surface: #0e1815;
  --raised: #132420;
  --hair: rgba(226,240,232,.12);
  --ink: #dfe9e2;
  --muted: #93a89d;
  --accent: #7fd6a8;
  --accent-ink: #052117;
  --focus: #a7e8c6;
  --measure: 68ch;
  --size: 1.075rem;
  --img-dim: .88;
  --serif: "Newsreader","Iowan Old Style",Georgia,"Times New Roman",serif;
  --sans: system-ui,-apple-system,"Segoe UI",sans-serif;
  color-scheme: dark;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--forest);
  color: var(--ink);
  font-family: var(--serif);
  -webkit-font-smoothing: antialiased;
}

.dmu-16[data-theme="light"],
.dmu-16:has(#dmu-16-toggle:checked) {
  --forest: #f2f5f2;
  --surface: #ffffff;
  --raised: #eef3ef;
  --hair: rgba(10,25,20,.14);
  --ink: #101a16;
  --muted: #4e6158;
  --accent: #0f6b45;
  --accent-ink: #ffffff;
  --focus: #0f6b45;
  --img-dim: 1;
  color-scheme: light;
}

@media (prefers-color-scheme: light) {
  .dmu-16:not([data-theme="dark"]):not(:has(#dmu-16-toggle:checked)) {
    --forest: #f2f5f2;
    --surface: #ffffff;
    --raised: #eef3ef;
    --hair: rgba(10,25,20,.14);
    --ink: #101a16;
    --muted: #4e6158;
    --accent: #0f6b45;
    --accent-ink: #ffffff;
    --focus: #0f6b45;
    --img-dim: 1;
    color-scheme: light;
  }
  /* flip-back: light OS + checked restores the tinted dark base */

  .dmu-16:has(#dmu-16-toggle:checked) {
    --forest: #0a1210;
    --surface: #0e1815;
    --raised: #132420;
    --hair: rgba(226,240,232,.12);
    --ink: #dfe9e2;
    --muted: #93a89d;
    --accent: #7fd6a8;
    --accent-ink: #052117;
    --focus: #a7e8c6;
    --img-dim: .88;
    color-scheme: dark;
  }
}

.dmu-16:has(#dmu-16-sm:checked) {
  --size: .98rem;
  --measure: 64ch;
}

.dmu-16:has(#dmu-16-lg:checked) {
  --size: 1.24rem;
  --measure: 60ch;
}

.dmu-16,
.dmu-16 *,
.dmu-16 *::before,
.dmu-16 *::after {
  box-sizing: border-box;
}

.dmu-16 ::selection {
  background: color-mix(in oklab,var(--accent) 32%,transparent);
  color: var(--ink);
}

.dmu-16__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.dmu-16__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  justify-items: center;
  align-content: start;
  padding: clamp(1.25rem,5vw,4rem);
}

.dmu-16__article {
  width: 100%;
  max-width: calc(var(--measure) + 6rem);
  display: grid;
  gap: 1.5rem;
  font-size: var(--size);
}

.dmu-16__head {
  display: grid;
  gap: .6rem;
}

.dmu-16__kicker {
  margin: 0;
  font-family: var(--sans);
  font-size: .74rem;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--accent);
}

.dmu-16__h1 {
  margin: 0;
  font-size: clamp(2rem,5.5vw,3.15rem);
  font-weight: 500;
  line-height: 1.1;
  letter-spacing: -.02em;
  text-wrap: balance;
}

.dmu-16__bylineRow {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  flex-wrap: wrap;
  padding-bottom: .85rem;
  border-bottom: 1px solid var(--hair);
}

.dmu-16__byline {
  margin: 0;
  font-family: var(--sans);
  font-size: .82rem;
  color: var(--muted);
}

.dmu-16__byline strong {
  color: var(--ink);
  font-weight: 600;
}

.dmu-16__controls {
  display: flex;
  align-items: center;
  gap: .5rem;
}

.dmu-16__sizes {
  margin: 0;
  padding: .2rem;
  border: 1px solid var(--hair);
  border-radius: .6rem;
  display: flex;
  gap: .1rem;
}

.dmu-16__size {
  display: grid;
  place-items: center;
  min-width: 2.1rem;
  min-height: 2rem;
  border-radius: .4rem;
  cursor: pointer;
  font-family: var(--sans);
  font-size: .75rem;
  color: var(--muted);
  transition: background-color .18s ease, color .18s ease;
}

.dmu-16__size--md {
  font-size: .9rem;
}

.dmu-16__size--lg {
  font-size: 1.05rem;
}

.dmu-16__size:hover {
  color: var(--ink);
}

.dmu-16__sizes input:checked + .dmu-16__size {
  background: var(--raised);
  color: var(--ink);
}

.dmu-16__sizes input:focus-visible + .dmu-16__size {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}

.dmu-16__toggle {
  display: grid;
  place-items: center;
  width: 2.4rem;
  height: 2.4rem;
  border-radius: .6rem;
  cursor: pointer;
  color: var(--ink);
  border: 1px solid var(--hair);
  transition: background-color .18s ease;
}

.dmu-16__toggle:hover {
  background: var(--raised);
}

.dmu-16__toggle svg {
  width: 1.05rem;
  height: 1.05rem;
}

.dmu-16__sun {
  display: none;
}

.dmu-16__moon {
  display: block;
}

.dmu-16:has(#dmu-16-toggle:checked) .dmu-16__sun {
  display: block;
}

.dmu-16:has(#dmu-16-toggle:checked) .dmu-16__moon {
  display: none;
}

@media (prefers-color-scheme: light) {
  .dmu-16:not(:has(#dmu-16-toggle:checked)) .dmu-16__sun {
    display: block;
  }

  .dmu-16:not(:has(#dmu-16-toggle:checked)) .dmu-16__moon {
    display: none;
  }

  .dmu-16:has(#dmu-16-toggle:checked) .dmu-16__sun {
    display: none;
  }

  .dmu-16:has(#dmu-16-toggle:checked) .dmu-16__moon {
    display: block;
  }
}

.dmu-16:has(#dmu-16-toggle:focus-visible) .dmu-16__toggle {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}

.dmu-16__figure {
  margin: 0;
  display: grid;
  gap: .5rem;
}

.dmu-16__figure img {
  width: 100%;
  height: auto;
  aspect-ratio: 12 / 7;
  object-fit: cover;
  border-radius: .9rem;
  filter: brightness(var(--img-dim)) saturate(.92);
  border: 1px solid var(--hair);
}

.dmu-16__figure figcaption {
  font-family: var(--sans);
  font-size: .76rem;
  line-height: 1.5;
  color: var(--muted);
}

.dmu-16__body {
  display: grid;
  gap: 1.1rem;
  max-width: var(--measure);
}

.dmu-16__body p {
  margin: 0;
  line-height: 1.8;
  text-wrap: pretty;
}

.dmu-16__body code {
  font-family: ui-monospace,"SF Mono",Menlo,monospace;
  font-size: .88em;
  color: var(--accent);
}

.dmu-16__body > p:first-of-type::first-letter {
  float: left;
  font-size: 3.6em;
  line-height: .82;
  padding-right: .07em;
  padding-top: .02em;
  font-weight: 500;
  color: var(--accent);
}

@supports (initial-letter: 3) {
  .dmu-16__body > p:first-of-type::first-letter {
    float: none;
    font-size: inherit;
    padding: 0;
    -webkit-initial-letter: 3;
    initial-letter: 3;
  }
}

.dmu-16__foot {
  display: flex;
  gap: .4rem;
  flex-wrap: wrap;
  padding-top: 1rem;
  border-top: 1px solid var(--hair);
}

.dmu-16__tag {
  font-family: var(--sans);
  font-size: .74rem;
  padding: .35rem .7rem;
  border-radius: 999px;
  color: var(--muted);
  border: 1px solid var(--hair);
}

@media (prefers-reduced-motion: reduce) {
  .dmu-16__size,
    .dmu-16__toggle {
    transition: none;
  }
}

@media (forced-colors: active) {
  .dmu-16__figure img,
    .dmu-16__tag,
    .dmu-16__sizes {
    border-color: CanvasText;
    filter: none;
  }

  .dmu-16__sizes input:checked + .dmu-16__size {
    background: Highlight;
    color: HighlightText;
  }
}
```
