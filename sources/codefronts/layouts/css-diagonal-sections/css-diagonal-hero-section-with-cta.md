---
source: "codefronts"
url: "https://codefronts.com/layouts/css-diagonal-sections/css-diagonal-hero-section-with-cta/"
title: "CSS Diagonal Hero Section with CTA"
section: "layouts"
category: "css-diagonal-sections"
category_name: "CSS Diagonal Sections"
description: "The canonical SaaS landing pattern: a full-viewport hero whose bottom edge is cut on a diagonal, with the headline, sub and two calls to action sitting well…"
has_js: "false"
---

Here's a working CSS Diagonal Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Diagonal Hero Section with CTA
Source: https://codefronts.com/layouts/css-diagonal-sections/css-diagonal-hero-section-with-cta/

The canonical SaaS landing pattern: a full-viewport hero whose bottom edge is cut on a diagonal, with the headline, sub and two calls to action sitting well clear of the slope. Uses 100svh so mobile browser chrome cannot squash it, and the band below is deliberately flat so the cut is doing the transition rather than decorating it.
## HTML
```html
<div class="dgs-06">
  <input class="dgs-06__sronly" type="checkbox" id="dgs-06-dark">
  <label class="dgs-06__theme" for="dgs-06-dark">
    <svg class="dgs-06__i dgs-06__i--moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.3A8.4 8.4 0 0 1 9.7 3.5a8.5 8.5 0 1 0 10.8 10.8Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="dgs-06__i dgs-06__i--sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.1" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.7 5.7l1.4 1.4M16.9 16.9l1.4 1.4M18.3 5.7l-1.4 1.4M7.1 16.9l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <span class="dgs-06__srtext">Toggle dark theme</span>
  </label>
  <div class="dgs-06__stage">
    <section class="dgs-06__hero" aria-labelledby="dgs-06-a">
      <div class="dgs-06__glow" aria-hidden="true"></div>
      <nav class="dgs-06__nav" aria-label="Product">
        <span class="dgs-06__mark">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4 18 12 4l8 14" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/><path d="M8.4 18h7.2" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
          Arcwork
        </span>
        <ul>
          <li><a href="#dgs-06-a">Platform</a></li>
          <li><a href="#dgs-06-b">Runs</a></li>
          <li><a href="#dgs-06-c">Docs</a></li>
        </ul>
        <a class="dgs-06__ghost" href="#dgs-06-b">Sign in</a>
      </nav>

      <div class="dgs-06__wrap">
        <p class="dgs-06__pill"><span class="dgs-06__live" aria-hidden="true"></span>Agent runs, now with step replay</p>
        <h1 class="dgs-06__display" id="dgs-06-a">Ship agents that hand work back cleanly</h1>
        <p class="dgs-06__lede">Every run is a traced graph you can inspect, fork and re-run from any step. Approvals, retries and human handoff are first-class, not glue code.</p>
        <div class="dgs-06__actions">
          <a class="dgs-06__cta" href="#dgs-06-b">Start a run
            <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M5 12h13m0 0-5.2-5.2M18 12l-5.2 5.2" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </a>
          <a class="dgs-06__alt" href="#dgs-06-c">Read the trace format</a>
        </div>
        <p class="dgs-06__note">No card required &middot; 10,000 free steps a month</p>
      </div>
    </section>

    <section class="dgs-06__proof" aria-labelledby="dgs-06-b">
      <div class="dgs-06__wrap">
        <h2 class="dgs-06__h2" id="dgs-06-b">The hero ends on the angle</h2>
        <p class="dgs-06__body">The cut is on the hero's <em>bottom</em> edge, so the eye is pulled down into the section that follows instead of stopping at a horizontal rule. The light band below is pulled up under the angle, and the wedge of dark that survives beside the copy is what makes the transition feel intentional.</p>
        <ul class="dgs-06__logos" aria-label="Teams shipping on Arcwork">
          <li>Hollow Labs</li><li>Meridian</li><li>Sundial</li><li>Tessellate</li><li>Norlin</li>
        </ul>
      </div>
    </section>

    <section class="dgs-06__specs" aria-labelledby="dgs-06-c">
      <div class="dgs-06__wrap">
        <h2 class="dgs-06__h3" id="dgs-06-c">Hero anatomy</h2>
        <dl class="dgs-06__dl">
          <div><dt>Edge</dt><dd>Bottom, falling left to right</dd></div>
          <div><dt>Depth</dt><dd>clamp(2rem, 7vw, 9rem)</dd></div>
          <div><dt>Glow</dt><dd>Radial gradient, behind content</dd></div>
          <div><dt>Nav</dt><dd>Inside the clipped band</dd></div>
        </dl>
      </div>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@300;400;500;600;700&display=swap');

.dgs-06 {
  --cut: clamp(2rem, 7vw, 9rem);
  --void: #07070b;
  --void2: #101018;
  --on-void: #f6f6fa;
  --dim: #9d9dae;
  --violet: #7c5cff;
  --mint: #5ce1b0;
  --page: #f7f7fa;
  --page2: #eeeef3;
  --ink: #0d0d12;
  --muted: #5a5a6b;
  --line: #e2e2ea;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  overflow-x: clip;
  background: var(--page);
  color: var(--ink);
  font-family: 'Sora', system-ui, -apple-system, sans-serif;
  font-size: 16px;
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}

.dgs-06 *,
.dgs-06 *::before,
.dgs-06 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.6 0.2 292)) {
  .dgs-06 {
    --void: oklch(0.135 0.012 285);
    --void2: oklch(0.2 0.018 285);
    --on-void: oklch(0.97 0.004 285);
    --dim: oklch(0.72 0.015 285);
    --violet: oklch(0.63 0.21 292);
    --mint: oklch(0.83 0.13 168);
    --page: oklch(0.978 0.003 285);
    --page2: oklch(0.948 0.004 285);
    --ink: oklch(0.18 0.012 285);
    --muted: oklch(0.5 0.015 285);
    --line: oklch(0.912 0.006 285);
  }
}

.dgs-06__stage {
  display: flow-root;
}

.dgs-06__wrap {
  inline-size: min(72rem, 100%);
  margin-inline: auto;
}

.dgs-06__hero {
  position: relative;
  z-index: 2;
  isolation: isolate;
  background: var(--void);
  color: var(--on-void);
  clip-path: polygon(0 0, 100% 0, 100% calc(100% - var(--cut)), 0 100%);
  padding: clamp(1rem, 3vw, 1.75rem) clamp(1.25rem, 5vw, 4rem) calc(var(--cut) + clamp(3.5rem, 9vw, 7rem));
}

.dgs-06__glow {
  position: absolute;
  inset: -20% -10% auto -10%;
  block-size: 130%;
  z-index: -1;
  pointer-events: none;
  background: radial-gradient(48rem 30rem at 22% 8%, rgba(124,92,255,.34), transparent 62%), radial-gradient(36rem 26rem at 82% 0%, rgba(92,225,176,.16), transparent 60%);
  animation: dgs-06-drift 22s ease-in-out infinite alternate;
}

@keyframes dgs-06-drift {
  to {
    translate: 2.5% 1.5%;
    scale: 1.06;
  }
}

.dgs-06__nav {
  inline-size: min(72rem, 100%);
  margin-inline: auto;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: .75rem 1.5rem;
  padding: .55rem .55rem .55rem 1rem;
  border: 1px solid rgba(246,246,250,.12);
  border-radius: 999px;
  background: rgba(246,246,250,.05);
  -webkit-backdrop-filter: blur(14px);
  backdrop-filter: blur(14px);
}

.dgs-06__mark {
  display: inline-flex;
  align-items: center;
  gap: .5rem;
  margin-inline-end: auto;
  font-weight: 600;
  letter-spacing: -.02em;
}

.dgs-06__mark svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
  color: var(--mint);
}

.dgs-06__nav ul {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  gap: .25rem;
}

.dgs-06__nav a {
  display: inline-flex;
  align-items: center;
  min-block-size: 2.5rem;
  padding-inline: .85rem;
  border-radius: 999px;
  color: var(--dim);
  text-decoration: none;
  font-size: .9rem;
  transition: color .2s ease, background .2s ease;
}

.dgs-06__nav a:hover {
  color: var(--on-void);
  background: rgba(246,246,250,.08);
}

.dgs-06__nav a:focus-visible {
  outline: 2px solid var(--violet);
  outline-offset: 2px;
}

.dgs-06__ghost {
  border: 1px solid rgba(246,246,250,.18);
}

.dgs-06__hero .dgs-06__wrap {
  padding-block-start: clamp(3rem, 9vw, 6rem);
}

.dgs-06__pill {
  margin: 0 0 1.35rem;
  display: inline-flex;
  align-items: center;
  gap: .55rem;
  padding: .4rem .85rem .4rem .6rem;
  border: 1px solid rgba(246,246,250,.16);
  border-radius: 999px;
  background: rgba(246,246,250,.05);
  font-size: .82rem;
  color: var(--dim);
}

.dgs-06__live {
  inline-size: .45rem;
  block-size: .45rem;
  border-radius: 999px;
  background: var(--mint);
  box-shadow: 0 0 0 0 rgba(92,225,176,.55);
  animation: dgs-06-ping 2.4s ease-out infinite;
}

@keyframes dgs-06-ping {
  70% {
    box-shadow: 0 0 0 .55rem rgba(92,225,176,0);
  }

  100% {
    box-shadow: 0 0 0 0 rgba(92,225,176,0);
  }
}

.dgs-06__display {
  margin: 0 0 1.1rem;
  max-inline-size: 21ch;
  font-size: clamp(2.4rem, 8vw, 5.2rem);
  font-weight: 600;
  line-height: 1.0;
  letter-spacing: -.045em;
  text-wrap: balance;
}

.dgs-06__lede {
  margin: 0 0 2rem;
  max-inline-size: 50ch;
  font-size: clamp(1.02rem, 2.1vw, 1.24rem);
  font-weight: 300;
  color: var(--dim);
  text-wrap: pretty;
}

.dgs-06__actions {
  display: flex;
  flex-wrap: wrap;
  gap: .75rem;
}

.dgs-06__cta {
  position: relative;
  overflow: clip;
  display: inline-flex;
  align-items: center;
  gap: .5rem;
  min-block-size: 3rem;
  padding: .8rem 1.4rem;
  border-radius: 999px;
  text-decoration: none;
  font-size: .95rem;
  font-weight: 500;
  color: #0b0713;
  background: linear-gradient(100deg, var(--mint), #b8a6ff 55%, var(--violet));
  transition: translate .22s cubic-bezier(.2,.8,.3,1), box-shadow .22s ease;
  box-shadow: 0 8px 30px -12px rgba(124,92,255,.7);
}

.dgs-06__cta svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
  transition: translate .22s cubic-bezier(.2,.8,.3,1);
}

.dgs-06__cta::after {
  content: '';
  position: absolute;
  inset: 0 auto 0 -40%;
  inline-size: 35%;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,.55), transparent);
  translate: -120% 0;
}

.dgs-06__cta:hover {
  translate: 0 -2px;
  box-shadow: 0 14px 38px -12px rgba(124,92,255,.8);
}

.dgs-06__cta:hover::after {
  animation: dgs-06-sheen .7s ease;
}

.dgs-06__cta:hover svg {
  translate: 3px 0;
}

@keyframes dgs-06-sheen {
  to {
    translate: 420% 0;
  }
}

.dgs-06__cta:focus-visible,
.dgs-06__alt:focus-visible {
  outline: 2px solid var(--mint);
  outline-offset: 3px;
}

.dgs-06__alt {
  display: inline-flex;
  align-items: center;
  min-block-size: 3rem;
  padding: .8rem 1.25rem;
  border: 1px solid rgba(246,246,250,.2);
  border-radius: 999px;
  color: var(--on-void);
  text-decoration: none;
  font-size: .95rem;
  transition: background .2s ease;
}

.dgs-06__alt:hover {
  background: rgba(246,246,250,.08);
}

.dgs-06__note {
  margin: 1.25rem 0 0;
  font-size: .82rem;
  color: rgba(157,157,174,.8);
}

.dgs-06__proof {
  position: relative;
  z-index: 1;
  background: var(--page);
  margin-block-start: calc(var(--cut) * -1 - 1px);
  padding: calc(var(--cut) + clamp(3rem, 7vw, 5rem)) clamp(1.25rem, 5vw, 4rem) clamp(3rem, 7vw, 4.5rem);
}

.dgs-06__h2 {
  margin: 0 0 1rem;
  max-inline-size: 24ch;
  font-size: clamp(1.5rem, 4.2vw, 2.4rem);
  font-weight: 600;
  letter-spacing: -.035em;
  line-height: 1.08;
  text-wrap: balance;
}

.dgs-06__body {
  margin: 0 0 2rem;
  max-inline-size: 58ch;
  color: var(--muted);
  font-weight: 300;
  text-wrap: pretty;
}

.dgs-06__logos {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  gap: .75rem 2.25rem;
  align-items: center;
}

.dgs-06__logos li {
  font-size: clamp(.95rem, 2.2vw, 1.15rem);
  font-weight: 500;
  letter-spacing: -.02em;
  color: var(--ink);
  opacity: .42;
  transition: opacity .2s ease;
}

.dgs-06__logos li:hover {
  opacity: .9;
}

.dgs-06__specs {
  background: var(--page2);
  padding: clamp(3rem, 7vw, 4.5rem) clamp(1.25rem, 5vw, 4rem) clamp(4rem, 9vw, 6rem);
}

.dgs-06__h3 {
  margin: 0 0 1.5rem;
  font-size: clamp(1.2rem, 3vw, 1.6rem);
  font-weight: 600;
  letter-spacing: -.03em;
}

.dgs-06__dl {
  margin: 0;
  display: grid;
  gap: 1px;
  grid-template-columns: repeat(auto-fit, minmax(12rem, 1fr));
  background: var(--line);
  border: 1px solid var(--line);
  border-radius: 14px;
  overflow: clip;
}

.dgs-06__dl > div {
  padding: 1rem 1.1rem;
  background: var(--page);
}

.dgs-06__dl dt {
  font-size: .72rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
}

.dgs-06__dl dd {
  margin: .3rem 0 0;
  font-size: .95rem;
  font-weight: 500;
}

@media (prefers-reduced-motion: reduce) {
  .dgs-06 *,
    .dgs-06 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .dgs-06__glow {
    display: none;
  }

  .dgs-06__hero {
    forced-color-adjust: none;
    background: Canvas;
    color: CanvasText;
    border-block-end: 1px solid CanvasText;
  }

  .dgs-06__cta {
    background: Highlight;
    color: HighlightText;
  }

  .dgs-06__nav,
    .dgs-06__pill,
    .dgs-06__dl {
    border: 1px solid CanvasText;
  }
}
/* Standard top-right theme toggle — pure CSS (checkbox + :has()), so demos
   that ship no script stay tagged Pure CSS. Placed on the root rather than
   inside a demo's own control panel so every demo exposes it in one place. */

.dgs-06__sronly,
.dgs-06__srtext {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.dgs-06__theme {
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

.dgs-06__theme:hover {
  translate: 0 -1px;
}

.dgs-06__sronly:focus-visible + .dgs-06__theme {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.dgs-06__i {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.dgs-06__i--sun {
  display: none;
}

.dgs-06:has(#dgs-06-dark:checked) .dgs-06__i--moon {
  display: none;
}

.dgs-06:has(#dgs-06-dark:checked) .dgs-06__i--sun {
  display: block;
}

.dgs-06:has(#dgs-06-dark:checked) {
  --page: #0b0d12;
  --page2: #12151d;
  --ink: #eef1f7;
  --muted: #98a0b0;
  --line: #232936;
}

@media (prefers-reduced-motion: reduce) {
  .dgs-06__theme {
    transition: none;
  }
}

@media (forced-colors: active) {
  .dgs-06__theme {
    border-color: CanvasText;
  }
}
```
