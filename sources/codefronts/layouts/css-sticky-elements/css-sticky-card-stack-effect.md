---
source: "codefronts"
url: "https://codefronts.com/layouts/css-sticky-elements/css-sticky-card-stack-effect/"
title: "CSS Sticky Card Stack Effect"
section: "layouts"
category: "css-sticky-elements"
category_name: "CSS Sticky Elements"
description: "The scroll-storytelling deck: four full-screen chapter cards that pile onto each other as you scroll, each new card sliding over the pinned previous one with…"
has_js: "false"
---

Here's a working CSS Sticky Element from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Sticky Card Stack Effect
Source: https://codefronts.com/layouts/css-sticky-elements/css-sticky-card-stack-effect/

The scroll-storytelling deck: four full-screen chapter cards that pile onto each other as you scroll, each new card sliding over the pinned previous one with a staggered 14px offset so the stack reads as physical depth. The pile-up is nothing but sticky elements sharing one parent — the exact opposite wrapper structure of demo 07 — plus a view()-timeline entrance that browsers without scroll-driven animations simply skip.
## HTML
```html
<section class="cst-08" aria-label="Sticky card stack scroll effect demo">
  <div class="cst-08__stage" id="cst08-top">
    <section class="cst-08__hero">
      <p class="cst-08__kicker">Field Notes · A studio year in four moves</p>
      <h1>The work,<br>stacked.</h1>
      <p class="cst-08__sub">Keep scrolling. Each chapter pins to the top and the next one slides over it — every card is <code>position: sticky</code> inside one shared deck. The 14px stagger is the whole illusion.</p>
      <span class="cst-08__cue" aria-hidden="true">↓</span>
    </section>
    <div class="cst-08__deck">
      <article class="cst-08__card" style="--i:0;--hue:265">
        <div>
          <header><span>01</span><em>Research</em></header>
          <h2>Listen before you sketch</h2>
          <p>Six weeks of ride-alongs with dispatchers before a single wireframe. The best interface decisions in this project were transcribed, not invented — the pinned card you're reading proves a point about restraint, too.</p>
          <figure style="--img:url('https://images.unsplash.com/photo-1522202176988-66273c2fd55f?q=80&w=1200&auto=format&fit=crop')"></figure>
        </div>
      </article>
      <article class="cst-08__card" style="--i:1;--hue:200">
        <div>
          <header><span>02</span><em>Design</em></header>
          <h2>Decide in the open</h2>
          <p>Every option we rejected lives in the case file next to the one we shipped. Crits ran twice a week with the dispatchers in the room; the design system grew a component only after the third copy-paste.</p>
          <figure style="--img:url('https://images.unsplash.com/photo-1561070791-2526d30994b5?q=80&w=1200&auto=format&fit=crop')"></figure>
        </div>
      </article>
      <article class="cst-08__card" style="--i:2;--hue:150">
        <div>
          <header><span>03</span><em>Build</em></header>
          <h2>Ship thin slices</h2>
          <p>One dispatch queue, one region, two weeks — then widen. The riskiest assumption always rides in the thinnest slice. By the fourth slice the rollback script had never been run, which is the only metric that matters.</p>
          <figure style="--img:url('https://images.unsplash.com/photo-1517336714731-489689fd1ca8?q=80&w=1200&auto=format&fit=crop')"></figure>
        </div>
      </article>
      <article class="cst-08__card" style="--i:3;--hue:45">
        <div>
          <header><span>04</span><em>Ship</em></header>
          <h2>Launch is a process</h2>
          <p>Feature flags stayed in for a quarter. Support tickets fed Tuesday triage; the roadmap column named “regret” collected everything we'd undo for free. Twelve percent of it, we did.</p>
          <figure style="--img:url('https://images.unsplash.com/photo-1498050108023-c5249f4df085?q=80&w=1200&auto=format&fit=crop')"></figure>
        </div>
      </article>
    </div>
    <section class="cst-08__outro">
      <h2>The stack releases here</h2>
      <p>The deck's bottom edge just scrolled past — every card un-pinned itself, no JavaScript involved. One parent, four stickies, staggered offsets.</p>
      <a href="#cst08-top">Back to top ↑</a>
    </section>
  </div>
</section>
```
## CSS
```css
.cst-08,
.cst-08 *,
.cst-08 *::before,
.cst-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cst-08 {
  --bg: oklch(0.16 0.015 270);
  --ink: oklch(0.94 0.008 270);
  --mut: oklch(0.68 0.015 270);
  --line: oklch(0.32 0.02 270);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
  display: block;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: var(--bg);
}

.cst-08__stage {
  width: 100%;
  container: cst08/inline-size;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  background: var(--bg);
  scroll-behavior: smooth;
}

.cst-08__hero {
  min-height: 92svh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 40px clamp(20px,5cqi,56px);
  background: radial-gradient(80cqi 55cqi at 80% 0%,oklch(0.3 0.06 265/.55),transparent 65%),radial-gradient(60cqi 45cqi at 5% 100%,oklch(0.28 0.05 200/.5),transparent 70%);
}

.cst-08__kicker {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: oklch(0.72 0.12 265);
  margin-bottom: 16px;
}

.cst-08__hero h1 {
  font-size: clamp(48px,11cqi,124px);
  line-height: .92;
  letter-spacing: -.045em;
  font-weight: 800;
}

.cst-08__sub {
  margin-top: 22px;
  max-width: 52ch;
  font-size: 15.5px;
  line-height: 1.65;
  color: var(--mut);
}

.cst-08__sub code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .87em;
  background: oklch(0.28 0.02 270);
  padding: 2px 6px;
  border-radius: 5px;
  color: var(--ink);
}

.cst-08__cue {
  margin-top: 34px;
  width: 46px;
  height: 46px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  font-size: 18px;
  border: 1.5px solid var(--line);
  animation: cst08-bob 1.9s ease-in-out infinite;
}

@keyframes cst08-bob {
  0%,
    100% {
    translate: 0 0;
    opacity: .6;
  }

  50% {
    translate: 0 6px;
    opacity: 1;
  }
}

.cst-08__deck {
  display: grid;
  gap: 26px;
  padding: 0 clamp(14px,3.5cqi,44px);
}

.cst-08__card {
  position: sticky;
  top: calc(20px + var(--i,0) * 14px);
  min-height: min(82svh,720px);
}

.cst-08__card>div {
  display: grid;
  grid-template-columns: minmax(0,1fr) minmax(0,42%);
  gap: clamp(18px,4cqi,44px);
  align-items: center;
  min-height: inherit;
  padding: clamp(24px,5cqi,56px);
  border-radius: 26px;
  background: linear-gradient(160deg,oklch(0.26 0.03 var(--hue,265)),oklch(0.2 0.025 var(--hue,265)));
  border: 1px solid oklch(0.4 0.04 var(--hue,265)/.6);
  box-shadow: 0 -12px 40px oklch(0.05 0.01 270/.55),0 30px 70px oklch(0.05 0.01 270/.5);
  animation: cst08-enter linear both;
  animation-timeline: view();
  animation-range: entry 5% entry 45%;
}

@keyframes cst08-enter {
  from {
    opacity: 0;
    translate: 0 44px;
  }
}

.cst-08__card header {
  grid-column: 1/-1;
  display: flex;
  align-items: baseline;
  gap: 12px;
}

.cst-08__card header span {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 13px;
  font-weight: 700;
  color: oklch(0.78 0.13 var(--hue,265));
}

.cst-08__card header em {
  font-style: normal;
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--mut);
}

.cst-08__card h2 {
  font-size: clamp(28px,5.4cqi,54px);
  line-height: 1;
  letter-spacing: -.035em;
  font-weight: 800;
  text-wrap: balance;
  align-self: start;
}

.cst-08__card p {
  font-size: 14.5px;
  line-height: 1.7;
  color: var(--mut);
  max-width: 52ch;
  align-self: start;
}

.cst-08__card figure {
  grid-row: 2/4;
  grid-column: 2;
  height: 100%;
  min-height: 220px;
  border-radius: 16px;
  background-image: linear-gradient(oklch(0.3 0.05 var(--hue,265)/.25),oklch(0.3 0.05 var(--hue,265)/.25)),var(--img,none),linear-gradient(150deg,oklch(0.45 0.06 var(--hue,265)),oklch(0.3 0.05 var(--hue,265)));
  background-size: cover;
  background-position: center;
  background-blend-mode: overlay,normal,normal;
}

.cst-08__card>div {
  grid-template-rows: auto auto 1fr;
}

.cst-08__outro {
  min-height: 70svh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
  gap: 12px;
  padding: 56px clamp(20px,5cqi,56px);
}

.cst-08__outro h2 {
  font-size: clamp(26px,4.6cqi,44px);
  letter-spacing: -.03em;
  font-weight: 800;
}

.cst-08__outro p {
  max-width: 52ch;
  font-size: 14.5px;
  line-height: 1.65;
  color: var(--mut);
}

.cst-08__outro a {
  display: grid;
  place-items: center;
  min-height: 46px;
  margin-top: 12px;
  padding: 0 20px;
  border-radius: 12px;
  font-size: 14px;
  font-weight: 700;
  text-decoration: none;
  color: var(--bg);
  background: var(--ink);
  transition: translate .2s,background .2s;
}

.cst-08__outro a:hover,
.cst-08__outro a:focus-visible {
  translate: 0 -2px;
  background: oklch(0.99 0 0);
}

.cst-08__outro a:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

@container cst08 (width < 640px) {
  .cst-08__card>div {
    grid-template-columns: 1fr;
    grid-template-rows: auto auto auto 1fr;
  }

  .cst-08__card figure {
    grid-row: auto;
    grid-column: 1;
    min-height: 180px;
  }
}

@media (max-height: 560px) {
  .cst-08__card {
    top: 8px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cst-08__stage {
    scroll-behavior: auto;
  }

  .cst-08__cue {
    animation: none;
  }

  .cst-08__card>div {
    animation: none;
  }

  .cst-08 * {
    transition-duration: .01ms !important;
  }
}
```
