---
source: "codefronts"
url: "https://codefronts.com/layouts/css-full-page-sections/css-full-page-section-reveal-and-scale-effect/"
title: "CSS Full Page Section Reveal and Scale Effect"
section: "layouts"
category: "css-full-page-sections"
category_name: "CSS Full Page Sections"
description: "Each incoming panel rises from scale(.92) and 30% opacity to full size exactly as it snaps into place, then recedes the same way on the way out &mdash; a…"
has_js: "false"
---

Here's a working CSS Full Page Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Full Page Section Reveal and Scale Effect
Source: https://codefronts.com/layouts/css-full-page-sections/css-full-page-section-reveal-and-scale-effect/

Each incoming panel rises from scale(.92) and 30% opacity to full size exactly as it snaps into place, then recedes the same way on the way out &mdash; a single scroll-driven keyframe set doing both halves of the transition. Only scale and opacity animate, so the whole effect runs on the compositor at 60fps.
## HTML
```html
<div class="fps-08">
  <input class="fps-08__sr" type="checkbox" id="fps-08-dark">
  <label class="fps-08__theme" for="fps-08-dark" title="Switch light or dark theme">
    <svg class="fps-08__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="fps-08__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="fps-08__vh">Switch light or dark theme</span>
  </label>

  <div class="fps-08__scroller" tabindex="0" role="group" aria-label="Reveal and scale sections, five panels">

    <section class="fps-08__panel" style="--h:300" id="fps-08-s1" aria-labelledby="fps-08-h1">
      <div class="fps-08__sheet">
        <div class="fps-08__stage">
          <p class="fps-08__eyebrow"><span class="fps-08__num">01 / 05</span><span class="fps-08__mono">scale .92 &rarr; 1</span></p>
          <h2 class="fps-08__title" id="fps-08-h1">Every panel arrives by growing into place</h2>
          <p class="fps-08__lead">One keyframe set drives both halves of the transition: the incoming sheet rises from 92% and 30% opacity, holds perfectly still while it is snapped, then recedes the same way as it leaves.</p>
          <p class="fps-08__cue"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 4.5v13.5M6.5 12.6 12 18.2l5.5-5.6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>Scroll &mdash; the next sheet is already growing</p>
        </div>
      </div>
    </section>

    <section class="fps-08__panel" style="--h:255" id="fps-08-s2" aria-labelledby="fps-08-h2">
      <div class="fps-08__sheet">
        <div class="fps-08__stage">
          <p class="fps-08__eyebrow"><span class="fps-08__num">02 / 05</span><span class="fps-08__mono">one range, two directions</span></p>
          <h2 class="fps-08__title fps-08__title--sm" id="fps-08-h2">The cover range already knows the whole journey</h2>
          <pre class="fps-08__code"><code>@keyframes reveal{
  0%      { scale:.92; opacity:.3 }
  <mark>44%,56% { scale:1;   opacity:1  }</mark>
  100%    { scale:.92; opacity:.3 }
}
.sheet{ animation-range:cover 0% cover 100% }</code></pre>
          <p class="fps-08__lead">No entry animation fighting an exit animation, and no JavaScript deciding which one owns the middle of the screen.</p>
        </div>
      </div>
    </section>

    <section class="fps-08__panel" style="--h:210" id="fps-08-s3" aria-labelledby="fps-08-h3">
      <div class="fps-08__sheet">
        <div class="fps-08__stage">
          <p class="fps-08__eyebrow"><span class="fps-08__num">03 / 05</span><span class="fps-08__mono">the plateau</span></p>
          <h2 class="fps-08__title fps-08__title--sm" id="fps-08-h3">Twelve percent of dead zone in the middle</h2>
          <p class="fps-08__lead">Hold full scale from 44% to 56% of the range and a snapped panel is visually locked. Remove the hold and the sheet breathes on every tiny trackpad nudge &mdash; the single most common reason this effect feels cheap.</p>
          <ul class="fps-08__marks">
            <li><strong>0&ndash;44%</strong><span>entering &mdash; scale and opacity rise</span></li>
            <li><strong>44&ndash;56%</strong><span>snapped &mdash; nothing moves</span></li>
            <li><strong>56&ndash;100%</strong><span>leaving &mdash; recedes symmetrically</span></li>
          </ul>
        </div>
      </div>
    </section>

    <section class="fps-08__panel" style="--h:165" id="fps-08-s4" aria-labelledby="fps-08-h4">
      <div class="fps-08__sheet">
        <div class="fps-08__stage">
          <p class="fps-08__eyebrow"><span class="fps-08__num">04 / 05</span><span class="fps-08__mono">compositor only</span></p>
          <h2 class="fps-08__title fps-08__title--sm" id="fps-08-h4">Two cheap properties, zero expensive ones</h2>
          <div class="fps-08__cols">
            <div class="fps-08__card fps-08__card--yes">
              <p class="fps-08__ch">Free on the compositor</p>
              <ul><li>scale</li><li>opacity</li><li>translate</li><li>rotate</li></ul>
            </div>
            <div class="fps-08__card fps-08__card--no">
              <p class="fps-08__ch">Repaints every frame</p>
              <ul><li>filter: blur()</li><li>width / height</li><li>top / left</li><li>box-shadow</li></ul>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="fps-08__panel" style="--h:120" id="fps-08-s5" aria-labelledby="fps-08-h5">
      <div class="fps-08__sheet">
        <div class="fps-08__stage">
          <p class="fps-08__eyebrow"><span class="fps-08__num">05 / 05</span><span class="fps-08__mono">pick your floor</span></p>
          <h2 class="fps-08__title fps-08__title--sm" id="fps-08-h5">Why 0.92 and not 0.8</h2>
          <p class="fps-08__lead">At <code>.92</code> the displacement reads as depth while body copy stays legible the whole way in. Below roughly <code>.85</code> headlines visibly reflow, the effect starts to feel like a slideshow, and motion-sensitive readers notice it immediately.</p>
          <p class="fps-08__quote">&ldquo;We shipped the reveal at .92 with a held middle. Nobody described it as an animation &mdash; they described the page as feeling fast.&rdquo;<span>Sam Rivera &middot; product designer</span></p>
        </div>
      </div>
    </section>

  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap');

.fps-08 {
  --bg: #eceef2;
  --sheet: #ffffff;
  --ink: #0b0b12;
  --muted: rgba(11,11,18,.6);
  --line: rgba(11,11,18,.10);
  --accent: #a21caf;
  --yes: #0f766e;
  --no: #9f1239;
  --sans: 'Geist',system-ui,-apple-system,'Segoe UI',sans-serif;
  --mono: 'Geist Mono',ui-monospace,'SFMono-Regular',Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  isolation: isolate;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(50% .1 250)) {
  .fps-08 {
    --accent: oklch(52% .21 328);
    --yes: oklch(48% .1 175);
    --no: oklch(48% .16 12);
    --ink: oklch(12% .015 300);
    --bg: oklch(93.5% .006 300);
  }
}

.fps-08 * {
  box-sizing: border-box;
}

.fps-08 h2,
.fps-08 p,
.fps-08 ul,
.fps-08 pre {
  margin: 0;
}

.fps-08 code {
  font-family: var(--mono);
  font-size: .92em;
}

.fps-08__sr,
.fps-08__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.fps-08__theme {
  position: fixed;
  inset-block-start: 1.15rem;
  inset-inline-end: 1.15rem;
  z-index: 80;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  border-radius: 999px;
  cursor: pointer;
  color: var(--ink);
  background: rgba(255,255,255,.62);
  border: 1px solid var(--line);
  -webkit-backdrop-filter: blur(10px) saturate(150%);
  backdrop-filter: blur(10px) saturate(150%);
  box-shadow: 0 8px 24px -12px rgba(11,11,18,.35);
}

.fps-08__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
  border-radius: inherit;
}

.fps-08__theme svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
}

.fps-08__moon {
  display: none;
}

.fps-08__sr:focus-visible + .fps-08__theme {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.fps-08__scroller {
  block-size: 100dvh;
  overflow-y: auto;
  overflow-x: hidden;
  scroll-snap-type: y mandatory;
  scroll-behavior: smooth;
  overscroll-behavior-y: contain;
  scrollbar-width: none;
}

.fps-08__scroller::-webkit-scrollbar {
  width: 0;
  height: 0;
}

.fps-08__scroller:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: -2px;
}

.fps-08__panel {
  position: relative;
  min-block-size: 100dvh;
  scroll-snap-align: start;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: clamp(.6rem,2vh,1.4rem) clamp(.6rem,2.5vw,1.6rem);
}

@supports not (height: 100dvh) {
  .fps-08__scroller {
    block-size: 100vh;
  }

  .fps-08__panel {
    min-block-size: 100vh;
  }
}

.fps-08__sheet {
  inline-size: 100%;
  block-size: 100%;
  min-block-size: calc(100dvh - clamp(1.2rem,4vh,2.8rem));
  display: flex;
  align-items: center;
  justify-content: center;
  transform-origin: 50% 50%;
  padding: clamp(2rem,5vh,3.5rem) clamp(1.25rem,5vw,4rem);
  border-radius: 1.75rem;
  border: 1px solid var(--line);
  background: var(--sheet);
  background-image: radial-gradient(110% 80% at 88% 8%,hsl(var(--h) 85% 92%) 0%,transparent 62%);
  box-shadow: 0 30px 70px -40px rgba(11,11,18,.45);
}

@supports (background: oklch(90% .05 40)) {
  .fps-08__sheet {
    background-image: radial-gradient(110% 80% at 88% 8%,oklch(92% .07 calc(var(--h) * 1deg)) 0%,transparent 62%);
  }
}

@supports not (height: 100dvh) {
  .fps-08__sheet {
    min-block-size: calc(100vh - clamp(1.2rem,4vh,2.8rem));
  }
}

@supports (animation-timeline: view()) {
  .fps-08__panel {
    view-timeline-name: --fps08;
    view-timeline-axis: block;
  }

  .fps-08__sheet {
    animation: fps-08-reveal linear both;
    animation-timeline: --fps08;
    animation-range: cover 0% cover 100%;
  }
}

@keyframes fps-08-reveal {
  0% {
    scale: .92;
    opacity: .3;
    border-radius: 2.6rem;
  }

  44%,
    56% {
    scale: 1;
    opacity: 1;
    border-radius: 1.75rem;
  }

  100% {
    scale: .92;
    opacity: .3;
    border-radius: 2.6rem;
  }
}

.fps-08__stage {
  inline-size: min(58rem,100%);
  display: grid;
  gap: clamp(.85rem,2vh,1.35rem);
  justify-items: start;
}

.fps-08__eyebrow {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: .7rem;
}

.fps-08__num {
  font-family: var(--mono);
  font-size: .7rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--accent);
}

.fps-08__mono {
  font-family: var(--mono);
  font-size: .7rem;
  color: var(--muted);
  padding: .22rem .5rem;
  border: 1px solid var(--line);
  border-radius: .45rem;
}

.fps-08__title {
  font-size: clamp(2rem,5.6vw,4rem);
  line-height: 1.02;
  letter-spacing: -.045em;
  font-weight: 600;
  max-inline-size: 20ch;
  text-wrap: balance;
}

.fps-08__title--sm {
  font-size: clamp(1.65rem,3.6vw,2.6rem);
  letter-spacing: -.035em;
  max-inline-size: 26ch;
}

.fps-08__lead {
  font-size: clamp(.98rem,1.35vw,1.14rem);
  line-height: 1.6;
  color: var(--muted);
  max-inline-size: 58ch;
  text-wrap: pretty;
}

.fps-08__cue {
  display: flex;
  align-items: center;
  gap: .55rem;
  font-family: var(--mono);
  font-size: .82rem;
  color: var(--muted);
}

.fps-08__cue svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
  animation: fps-08-bob 2.4s ease-in-out infinite;
}

@keyframes fps-08-bob {
  0%,
    100% {
    translate: 0 -2px;
  }

  50% {
    translate: 0 3px;
  }
}

.fps-08__code {
  padding: 1rem 1.1rem;
  border-radius: 1rem;
  border: 1px solid var(--line);
  background: color-mix(in srgb,var(--ink) 4%,transparent);
  overflow-x: auto;
}

.fps-08__code code {
  font-size: clamp(.76rem,1vw,.87rem);
  line-height: 1.75;
  color: var(--muted);
  white-space: pre;
}

.fps-08__code mark {
  background: color-mix(in srgb,var(--accent) 14%,transparent);
  color: var(--accent);
  border-radius: .25rem;
  padding: .05rem .2rem;
}

.fps-08__marks {
  list-style: none;
  padding: 0;
  display: grid;
  gap: .3rem;
  inline-size: 100%;
}

.fps-08__marks li {
  display: grid;
  grid-template-columns: 6.5rem 1fr;
  gap: 1rem;
  padding: .65rem 0;
  border-block-start: 1px solid var(--line);
  align-items: baseline;
}

.fps-08__marks strong {
  font-family: var(--mono);
  font-size: .8rem;
  color: var(--accent);
  font-variant-numeric: tabular-nums;
}

.fps-08__marks span {
  font-size: .93rem;
  color: var(--muted);
}

.fps-08__cols {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(12rem,1fr));
  gap: clamp(.8rem,2vw,1.4rem);
  inline-size: 100%;
}

.fps-08__card {
  padding: clamp(1rem,2.2vw,1.4rem);
  border-radius: 1.15rem;
  border: 1px solid var(--line);
  display: grid;
  gap: .7rem;
  background: color-mix(in srgb,var(--ink) 3%,transparent);
}

.fps-08__ch {
  font-family: var(--mono);
  font-size: .68rem;
  letter-spacing: .12em;
  text-transform: uppercase;
}

.fps-08__card--yes .fps-08__ch {
  color: var(--yes);
}

.fps-08__card--no .fps-08__ch {
  color: var(--no);
}

.fps-08__card ul {
  list-style: none;
  padding: 0;
  display: grid;
  gap: .4rem;
  font-family: var(--mono);
  font-size: .85rem;
  color: var(--muted);
}

.fps-08__quote {
  font-size: clamp(1.02rem,1.85vw,1.3rem);
  line-height: 1.45;
  letter-spacing: -.02em;
  max-inline-size: 46ch;
  padding-inline-start: 1.05rem;
  border-inline-start: 2px solid var(--accent);
  display: grid;
  gap: .55rem;
  text-wrap: pretty;
}

.fps-08__quote span {
  font-family: var(--mono);
  font-size: .68rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.fps-08[data-theme="dark"],
.fps-08:has(#fps-08-dark:checked) {
  --bg: #070709;
  --sheet: #0d0d13;
  --ink: #f3f2f8;
  --muted: rgba(243,242,248,.62);
  --line: rgba(243,242,248,.13);
  --accent: #f0abfc;
  --yes: #5eead4;
  --no: #fda4af;
}

.fps-08:has(#fps-08-dark:checked) .fps-08__theme {
  background: rgba(255,255,255,.07);
}

.fps-08:has(#fps-08-dark:checked) .fps-08__sun {
  display: none;
}

.fps-08:has(#fps-08-dark:checked) .fps-08__moon {
  display: block;
}

.fps-08:has(#fps-08-dark:checked) .fps-08__sheet {
  background-image: radial-gradient(110% 80% at 88% 8%,hsl(var(--h) 60% 16%) 0%,transparent 62%);
  box-shadow: 0 30px 70px -40px rgba(0,0,0,.9);
}

@media (prefers-color-scheme: dark) {
  .fps-08:not([data-theme="light"]):not(:has(#fps-08-dark:checked)) {
    --bg: #070709;
    --sheet: #0d0d13;
    --ink: #f3f2f8;
    --muted: rgba(243,242,248,.62);
    --line: rgba(243,242,248,.13);
    --accent: #f0abfc;
    --yes: #5eead4;
    --no: #fda4af;
  }

  .fps-08:not([data-theme="light"]):not(:has(#fps-08-dark:checked)) .fps-08__theme {
    background: rgba(255,255,255,.07);
  }

  .fps-08:not([data-theme="light"]):not(:has(#fps-08-dark:checked)) .fps-08__sun {
    display: none;
  }

  .fps-08:not([data-theme="light"]):not(:has(#fps-08-dark:checked)) .fps-08__moon {
    display: block;
  }

  .fps-08:not([data-theme="light"]):not(:has(#fps-08-dark:checked)) .fps-08__sheet {
    background-image: radial-gradient(110% 80% at 88% 8%,hsl(var(--h) 60% 16%) 0%,transparent 62%);
    box-shadow: 0 30px 70px -40px rgba(0,0,0,.9);
  }
}

@supports not selector(:has(*)) {
  .fps-08__theme {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .fps-08__scroller {
    scroll-snap-type: none;
    scroll-behavior: auto;
  }

  .fps-08 *,
    .fps-08 *::before,
    .fps-08 *::after {
    animation: none !important;
    transition: none !important;
  }

  .fps-08__sheet {
    scale: 1 !important;
    opacity: 1 !important;
    border-radius: 1.75rem !important;
  }
}

@media (forced-colors: active) {
  .fps-08__sheet,
    .fps-08__card,
    .fps-08__code,
    .fps-08__theme {
    border-color: CanvasText;
    box-shadow: none;
    background: Canvas;
    background-image: none;
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
  }
}
```
