---
source: "codefronts"
url: "https://codefronts.com/layouts/css-diagonal-sections/css-skewed-section-with-counter-skewed-content/"
title: "CSS Skewed Section with Counter-Skewed Content"
section: "layouts"
category: "css-diagonal-sections"
category_name: "CSS Diagonal Sections"
description: "The technique that predates clip-path and still ships on thousands of marketing pages: skewY() the band, then skewY() the inner wrapper by the exact opposite…"
has_js: "false"
---

Here's a working CSS Diagonal Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Skewed Section with Counter-Skewed Content
Source: https://codefronts.com/layouts/css-diagonal-sections/css-skewed-section-with-counter-skewed-content/

The technique that predates clip-path and still ships on thousands of marketing pages: skewY() the band, then skewY() the inner wrapper by the exact opposite angle so headings, buttons and images stand up straight. Both edges of the band tilt together, and the demo shows the two flat neighbours you need for the tilt to register — plus the height inflation skew causes, which is the part most tutorials leave out.
## HTML
```html
<div class="dgs-02">
  <input class="dgs-02__sronly" type="checkbox" id="dgs-02-dark">
  <label class="dgs-02__theme" for="dgs-02-dark">
    <svg class="dgs-02__i dgs-02__i--moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.3A8.4 8.4 0 0 1 9.7 3.5a8.5 8.5 0 1 0 10.8 10.8Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="dgs-02__i dgs-02__i--sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.1" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.7 5.7l1.4 1.4M16.9 16.9l1.4 1.4M18.3 5.7l-1.4 1.4M7.1 16.9l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <span class="dgs-02__srtext">Toggle dark theme</span>
  </label>
  <fieldset class="dgs-02__ctl">
    <legend class="dgs-02__vh">Skew controls</legend>
    <input class="dgs-02__sr" type="radio" name="dgs-02-sk" id="dgs-02-s1"><label for="dgs-02-s1">-3&#176;</label>
    <input class="dgs-02__sr" type="radio" name="dgs-02-sk" id="dgs-02-s2" checked><label for="dgs-02-s2">-5&#176;</label>
    <input class="dgs-02__sr" type="radio" name="dgs-02-sk" id="dgs-02-s3"><label for="dgs-02-s3">-8&#176;</label>
    <input class="dgs-02__sr" type="checkbox" id="dgs-02-flip"><label for="dgs-02-flip">Flip</label>
  </fieldset>

  <div class="dgs-02__stage">
    <section class="dgs-02__top" aria-labelledby="dgs-02-a">
      <div class="dgs-02__wrap">
        <p class="dgs-02__tag">Linehaul network</p>
        <h2 class="dgs-02__display" id="dgs-02-a">Freight that<br>never idles</h2>
        <p class="dgs-02__lede">Sixteen thousand trailers, one dispatch layer. Book a lane in the morning and track the trailer to the dock door by evening.</p>
      </div>
    </section>

    <section class="dgs-02__skew" aria-labelledby="dgs-02-b">
      <div class="dgs-02__ticker" aria-hidden="true"><span>DTW &rarr; CHI 04:12&nbsp;&nbsp;/&nbsp;&nbsp;LAX &rarr; PHX 02:38&nbsp;&nbsp;/&nbsp;&nbsp;NJ &rarr; BOS 03:55&nbsp;&nbsp;/&nbsp;&nbsp;ATL &rarr; MIA 08:04&nbsp;&nbsp;/&nbsp;&nbsp;SEA &rarr; PDX 02:11&nbsp;&nbsp;/&nbsp;&nbsp;DFW &rarr; OKC 03:20&nbsp;&nbsp;/&nbsp;&nbsp;</span><span>DTW &rarr; CHI 04:12&nbsp;&nbsp;/&nbsp;&nbsp;LAX &rarr; PHX 02:38&nbsp;&nbsp;/&nbsp;&nbsp;NJ &rarr; BOS 03:55&nbsp;&nbsp;/&nbsp;&nbsp;ATL &rarr; MIA 08:04&nbsp;&nbsp;/&nbsp;&nbsp;SEA &rarr; PDX 02:11&nbsp;&nbsp;/&nbsp;&nbsp;DFW &rarr; OKC 03:20&nbsp;&nbsp;/&nbsp;&nbsp;</span></div>
      <div class="dgs-02__unskew">
        <div class="dgs-02__wrap dgs-02__grid">
          <div>
            <p class="dgs-02__tag dgs-02__tag--dark">Skew, then un-skew</p>
            <h2 class="dgs-02__h2" id="dgs-02-b">The band tilts. The type stays level.</h2>
            <p class="dgs-02__body">One <code class="dgs-02__code">rotate: -5deg</code>-style skew on the section angles both of its edges at once. The inner wrapper carries the exact opposite skew, so every glyph, button and number lands upright while the band underneath keeps the tilt.</p>
            <a class="dgs-02__cta" href="#dgs-02-b">Book a lane
              <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M5 12h13m0 0-5.2-5.2M18 12l-5.2 5.2" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </a>
          </div>
          <dl class="dgs-02__board">
            <div><dt>On-time, 30d</dt><dd>98.4<span>%</span></dd></div>
            <div><dt>Avg. dwell</dt><dd>26<span>min</span></dd></div>
            <div><dt>Empty miles</dt><dd>7.1<span>%</span></dd></div>
            <div><dt>Active lanes</dt><dd>2,148</dd></div>
          </dl>
        </div>
      </div>
    </section>

    <section class="dgs-02__bottom" aria-labelledby="dgs-02-c">
      <div class="dgs-02__wrap">
        <h2 class="dgs-02__h3" id="dgs-02-c">Why skew instead of clip</h2>
        <div class="dgs-02__cols">
          <p><strong>Both edges, one transform.</strong> A skew angles the top and bottom together — a clip-path needs every corner restated.</p>
          <p><strong>Nothing is clipped away.</strong> Shadows, focus rings and dropdowns survive, because the box is transformed, not cut.</p>
          <p><strong>The cost is the counter-skew.</strong> Any child you forget to un-skew leans, and text renders very slightly softer under transform.</p>
        </div>
      </div>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Anton&family=Space+Grotesk:wght@400;500;700&display=swap');

.dgs-02 {
  --skew: -5deg;
  --dark: #0e0f12;
  --dark2: #16181d;
  --ink: #f2f3ef;
  --muted: #9aa0a6;
  --lime: #c8f31d;
  --lime-ink: #14170a;
  --line: rgba(242,243,239,.16);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  overflow-x: clip;
  background: var(--dark);
  color: var(--ink);
  font-family: 'Space Grotesk', system-ui, -apple-system, sans-serif;
  font-size: 16px;
  line-height: 1.55;
  -webkit-font-smoothing: antialiased;
}

.dgs-02 *,
.dgs-02 *::before,
.dgs-02 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.9 0.2 120)) {
  .dgs-02 {
    --dark: oklch(0.16 0.008 260);
    --dark2: oklch(0.215 0.01 260);
    --ink: oklch(0.96 0.005 120);
    --muted: oklch(0.71 0.012 260);
    --lime: oklch(0.91 0.2 118);
    --lime-ink: oklch(0.2 0.04 118);
  }
}

.dgs-02__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.dgs-02__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.dgs-02__ctl {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 40;
  margin: 0;
  padding: 3px;
  display: flex;
  gap: 3px;
  border: 1px solid var(--line);
  border-radius: 999px;
  background: rgba(14,15,18,.75);
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
}

.dgs-02__ctl label {
  min-inline-size: 2.75rem;
  min-block-size: 2.5rem;
  display: grid;
  place-items: center;
  padding-inline: .7rem;
  border-radius: 999px;
  font-size: .74rem;
  font-weight: 700;
  letter-spacing: .06em;
  color: var(--muted);
  cursor: pointer;
  transition: background .18s ease, color .18s ease;
}

.dgs-02__ctl label:hover {
  color: var(--ink);
}

.dgs-02__sr:checked + label {
  background: var(--lime);
  color: var(--lime-ink);
}

.dgs-02__sr:focus-visible + label {
  outline: 2px solid var(--lime);
  outline-offset: 2px;
}

.dgs-02__stage {
  display: flow-root;
}

.dgs-02__wrap {
  inline-size: min(74rem, 100%);
  margin-inline: auto;
}

.dgs-02__top {
  padding: clamp(4rem, 10vw, 7.5rem) clamp(1.25rem, 5vw, 4rem) clamp(5rem, 12vw, 9rem);
}

.dgs-02__tag {
  margin: 0 0 1.1rem;
  display: inline-flex;
  align-items: center;
  gap: .5rem;
  padding: .3rem .7rem;
  border: 1px solid var(--lime);
  border-radius: 999px;
  color: var(--lime);
  font-size: .7rem;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
}

.dgs-02__tag--dark {
  border-color: rgba(20,23,10,.35);
  color: var(--lime-ink);
}

.dgs-02__display {
  margin: 0 0 1.25rem;
  font-family: 'Anton', 'Archivo', system-ui, sans-serif;
  font-weight: 400;
  font-size: clamp(3rem, 13vw, 8.5rem);
  line-height: .86;
  letter-spacing: -.02em;
  text-transform: uppercase;
}

.dgs-02__lede {
  margin: 0;
  max-inline-size: 44ch;
  font-size: clamp(1rem, 2.1vw, 1.2rem);
  color: var(--muted);
  text-wrap: pretty;
}

.dgs-02__skew {
  position: relative;
  z-index: 1;
  background: var(--lime);
  color: var(--lime-ink);
  transform: skewY(var(--skew));
  margin-block: calc(-1 * clamp(2rem, 6vw, 5rem));
  padding-block: clamp(4.5rem, 11vw, 8rem);
}

.dgs-02__unskew {
  transform: skewY(calc(var(--skew) * -1));
  padding-inline: clamp(1.25rem, 5vw, 4rem);
}

.dgs-02__ticker {
  position: absolute;
  inset-inline: 0;
  inset-block-start: clamp(1rem, 3vw, 2rem);
  display: flex;
  gap: 0;
  font-family: ui-monospace, 'SF Mono', Menlo, monospace;
  font-size: clamp(.62rem, 1.4vw, .78rem);
  font-weight: 500;
  letter-spacing: .12em;
  white-space: nowrap;
  opacity: .55;
  overflow: clip;
}

.dgs-02__ticker span {
  animation: dgs-02-roll 26s linear infinite;
  padding-inline-end: 1rem;
  flex: none;
}

@keyframes dgs-02-roll {
  to {
    translate: -100% 0;
  }
}

.dgs-02__grid {
  display: grid;
  gap: clamp(2rem, 5vw, 4rem);
  grid-template-columns: repeat(auto-fit, minmax(19rem, 1fr));
  align-items: start;
}

.dgs-02__h2 {
  margin: 0 0 1rem;
  font-size: clamp(1.7rem, 4.8vw, 3rem);
  font-weight: 700;
  line-height: 1.02;
  letter-spacing: -.035em;
  text-wrap: balance;
}

.dgs-02__body {
  margin: 0 0 1.75rem;
  max-inline-size: 48ch;
  color: rgba(20,23,10,.78);
  text-wrap: pretty;
}

.dgs-02__code {
  font-family: ui-monospace, 'SF Mono', Menlo, monospace;
  font-size: .88em;
  padding: .1em .35em;
  background: rgba(20,23,10,.12);
}

.dgs-02__cta {
  display: inline-flex;
  align-items: center;
  gap: .55rem;
  min-block-size: 2.9rem;
  padding: .7rem 1.35rem;
  background: var(--lime-ink);
  color: var(--lime);
  text-decoration: none;
  border-radius: 2px;
  font-size: .88rem;
  font-weight: 700;
  letter-spacing: .1em;
  text-transform: uppercase;
  transition: translate .2s cubic-bezier(.2,.8,.3,1), background .2s ease;
}

.dgs-02__cta svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
  transition: translate .2s cubic-bezier(.2,.8,.3,1);
}

.dgs-02__cta:hover {
  translate: 0 -2px;
}

.dgs-02__cta:hover svg {
  translate: 3px 0;
}

.dgs-02__cta:focus-visible {
  outline: 3px solid var(--lime-ink);
  outline-offset: 3px;
}

.dgs-02__board {
  margin: 0;
  display: grid;
  gap: 1px;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  background: rgba(20,23,10,.3);
  border: 1px solid rgba(20,23,10,.3);
}

.dgs-02__board > div {
  padding: 1.1rem 1.15rem;
  background: var(--lime);
}

.dgs-02__board dt {
  font-size: .68rem;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: rgba(20,23,10,.62);
}

.dgs-02__board dd {
  margin: .35rem 0 0;
  font-family: 'Anton', sans-serif;
  font-size: clamp(1.7rem, 5vw, 2.6rem);
  line-height: 1;
  letter-spacing: -.01em;
  font-variant-numeric: tabular-nums;
}

.dgs-02__board span {
  font-family: 'Space Grotesk', sans-serif;
  font-size: .8rem;
  font-weight: 700;
  margin-inline-start: .2rem;
}

.dgs-02__bottom {
  background: var(--dark2);
  padding: clamp(4.5rem, 11vw, 8rem) clamp(1.25rem, 5vw, 4rem) clamp(4rem, 9vw, 6rem);
}

.dgs-02__h3 {
  margin: 0 0 1.5rem;
  font-size: clamp(1.35rem, 3.6vw, 2.1rem);
  font-weight: 700;
  letter-spacing: -.03em;
}

.dgs-02__cols {
  display: grid;
  gap: 1.25rem clamp(1.5rem, 4vw, 3rem);
  grid-template-columns: repeat(auto-fit, minmax(15rem, 1fr));
}

.dgs-02__cols p {
  margin: 0;
  padding-block-start: 1rem;
  border-block-start: 2px solid var(--lime);
  color: var(--muted);
  font-size: .95rem;
  text-wrap: pretty;
}

.dgs-02__cols strong {
  color: var(--ink);
}

.dgs-02:has(#dgs-02-s1:checked) {
  --skew: -3deg;
}

.dgs-02:has(#dgs-02-s3:checked) {
  --skew: -8deg;
}

.dgs-02:has(#dgs-02-flip:checked) {
  --skew: 5deg;
}

.dgs-02:has(#dgs-02-flip:checked):has(#dgs-02-s1:checked) {
  --skew: 3deg;
}

.dgs-02:has(#dgs-02-flip:checked):has(#dgs-02-s3:checked) {
  --skew: 8deg;
}

@media (prefers-reduced-motion: reduce) {
  .dgs-02 * {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .dgs-02__skew {
    forced-color-adjust: none;
    background: Canvas;
    color: CanvasText;
    border-block: 1px solid CanvasText;
  }

  .dgs-02__board,
    .dgs-02__board > div,
    .dgs-02__ctl label {
    border: 1px solid CanvasText;
  }

  .dgs-02__sr:checked + label {
    background: Highlight;
    color: HighlightText;
  }
}
/* Standard top-right theme toggle — pure CSS (checkbox + :has()), so demos
   that ship no script stay tagged Pure CSS. Placed on the root rather than
   inside a demo's own control panel so every demo exposes it in one place. */

.dgs-02__sronly,
.dgs-02__srtext {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.dgs-02__theme {
  position: absolute;
  inset-block-start: clamp(.85rem, 2.2vw, 1.5rem);
  inset-inline-end: clamp(.85rem, 2.2vw, 1.5rem);
  z-index: 60;
  display: grid;
  place-items: center;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  border-radius: 999px;
  border: 1px solid currentColor;
  color: inherit;
  background: rgba(127,127,127,.16);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  cursor: pointer;
  transition: translate .2s ease;
}

.dgs-02__theme:hover {
  translate: 0 -1px;
}

.dgs-02__sronly:focus-visible + .dgs-02__theme {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.dgs-02__i {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.dgs-02__i--sun {
  display: none;
}

.dgs-02:has(#dgs-02-dark:checked) .dgs-02__i--moon {
  display: none;
}

.dgs-02:has(#dgs-02-dark:checked) .dgs-02__i--sun {
  display: block;
}

.dgs-02:has(#dgs-02-dark:checked) {
  --dark: #f4f5f1;
  --dark2: #e7e9e2;
  --ink: #14161a;
  --muted: #5b6068;
  --line: rgba(20,22,26,.16);
  --lime: #7fa80c;
  --lime-ink: #ffffff;
}

@media (prefers-reduced-motion: reduce) {
  .dgs-02__theme {
    transition: none;
  }
}

@media (forced-colors: active) {
  .dgs-02__theme {
    border-color: CanvasText;
  }
}
```
