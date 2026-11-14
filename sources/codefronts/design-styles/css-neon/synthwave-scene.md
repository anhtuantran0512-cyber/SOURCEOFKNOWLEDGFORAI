---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-neon/synthwave-scene/"
title: "Layered Glow Scene with Depth Falloff"
section: "design-styles"
category: "css-neon"
category_name: "CSS Neon Effects"
description: "A composed scene where glow intensity falls off with distance: near elements are tight and bright, far ones are wide, dim and desaturated, with a haze layer…"
has_js: "false"
---

Here's a working CSS Neon Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Layered Glow Scene with Depth Falloff
Source: https://codefronts.com/design-styles/css-neon/synthwave-scene/

A composed scene where glow intensity falls off with distance: near elements are tight and bright, far ones are wide, dim and desaturated, with a haze layer between the bands. It is a depth study &mdash; the same three-layer stack tuned three ways to produce atmospheric perspective from nothing but shadow values.
## HTML
```html
<section class="nn-12" aria-labelledby="nn-12-heading">
  <div class="nn-12__stage">
    <div class="nn-12__theme">
      <input class="nn-12__tin" type="checkbox" id="nn-12-theme">
      <label class="nn-12__tlab" for="nn-12-theme">
        <svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M8 1.5v2M8 12.5v2M1.5 8h2M12.5 8h2M3.4 3.4l1.4 1.4M11.2 11.2l1.4 1.4M12.6 3.4l-1.4 1.4M4.8 11.2l-1.4 1.4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"></path><circle cx="8" cy="8" r="2.6" fill="none" stroke="currentColor" stroke-width="1.5"></circle></svg>
        Flip light / dark
      </label>
    </div>
    <header class="nn-12__head">
      <p class="nn-12__kicker">Depth from shadow values alone</p>
      <h2 class="nn-12__heading" id="nn-12-heading">Glow falls off with distance</h2>
      <p class="nn-12__sub">Near light is tight, bright and saturated. Far light is wide, dim and pulled toward the background. Same stack, three tunings.</p>
    </header>

    <div class="nn-12__scene">
      <div class="nn-12__far">
        <span class="nn-12__horizon"></span>
        <span class="nn-12__tower nn-12__tower--a"></span>
        <span class="nn-12__tower nn-12__tower--b"></span>
        <span class="nn-12__tower nn-12__tower--c"></span>
      </div>
      <div class="nn-12__haze"></div>
      <div class="nn-12__mid">
        <span class="nn-12__bar nn-12__bar--1"></span>
        <span class="nn-12__bar nn-12__bar--2"></span>
        <span class="nn-12__bar nn-12__bar--3"></span>
      </div>
      <div class="nn-12__near">
        <p class="nn-12__sign">Vale Terminal</p>
      </div>
      <div class="nn-12__vignette"></div>
    </div>

    <ol class="nn-12__bands">
      <li class="nn-12__band"><span class="nn-12__blabel nn-12__blabel--near">Near</span><span class="nn-12__bval">core 4px / 1.0 &middot; halo 14px / .5 &middot; bloom 34px / .28 &middot; full chroma</span></li>
      <li class="nn-12__band"><span class="nn-12__blabel nn-12__blabel--mid">Mid</span><span class="nn-12__bval">core 3px / .6 &middot; halo 22px / .3 &middot; bloom 46px / .18 &middot; chroma &minus;25%</span></li>
      <li class="nn-12__band"><span class="nn-12__blabel nn-12__blabel--far">Far</span><span class="nn-12__bval">no core &middot; bloom 60px / .2 &middot; chroma &minus;55%, hue pulled to ground</span></li>
    </ol>
  </div>
</section>
```
## CSS
```css
.nn-12 {
  --nn-12-nears: #35e6ff;
  --nn-12-mids: #7fb4ff;
  --nn-12-fars: #ff7ae0;
  --nn-12-bad: #f4a4a4;
  --nn-12-warn: #f0c88a;
}

@media (prefers-color-scheme: light) {
  .nn-12 {
    --nn-12-bad: #a12a20;
    --nn-12-warn: #78490a;
  }

  .nn-12:has(#nn-12-theme:checked) {
    --nn-12-bad: #f4a4a4;
    --nn-12-warn: #f0c88a;
  }
}

@media (prefers-color-scheme: dark) {
  .nn-12:has(#nn-12-theme:checked) {
    --nn-12-bad: #a12a20;
    --nn-12-warn: #78490a;
  }
}

.nn-12[data-theme="light"] {
  --nn-12-bad: #a12a20;
  --nn-12-warn: #78490a;
}

.nn-12 {
  --nn-12-spec-ink: #e8eeff;
  --nn-12-spec-dim: #8e9cc4;
}

.nn-12__theme {
  position: absolute;
  inset-block-start: clamp(10px, 2vw, 18px);
  inset-inline-end: clamp(10px, 2vw, 18px);
  z-index: 5;
  display: flex;
  justify-content: flex-end;
}

.nn-12__tin {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.nn-12__tlab {
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  min-height: 44px;
  padding: 0 .8rem;
  border: 1px solid currentColor;
  font-size: .7rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  cursor: pointer;
  opacity: .7;
}

.nn-12__tlab svg {
  width: .9rem;
  height: .9rem;
  flex: none;
}

.nn-12__tlab:hover {
  opacity: 1;
}

.nn-12__tin:focus-visible + .nn-12__tlab {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

@media (prefers-color-scheme: light) {
  .nn-12:has(#nn-12-theme:checked) {
    --nn-12-bg: #050a1a;
    --nn-12-ink: #e8eeff;
    --nn-12-muted: #8e9cc4;
    --nn-12-line: #1a2547;
    --nn-12-near: #35e6ff;
    --nn-12-mid: #7fb4ff;
    --nn-12-far: #ff7ae0;
  }
}

@media (prefers-color-scheme: dark) {
  .nn-12:has(#nn-12-theme:checked) {
    --nn-12-bg: #e9ecf5;
    --nn-12-ink: #0b1024;
    --nn-12-muted: #4a5372;
    --nn-12-line: #c4cade;
    --nn-12-near: #046a80;
    --nn-12-mid: #2b4d90;
    --nn-12-far: #8f2b74;
  }
}

.nn-12 {
  --nn-12-bg: #050a1a;
  --nn-12-ink: #e8eeff;
  --nn-12-muted: #8e9cc4;
  --nn-12-line: #1a2547;
  --nn-12-near: #35e6ff;
  --nn-12-mid: #7fb4ff;
  --nn-12-far: #ff7ae0;
  --nn-12-font-display: "Helvetica Neue", "Inter Tight", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  position: relative;
  display: block;
  box-sizing: border-box;
  background: var(--nn-12-bg);
  color: var(--nn-12-ink);
  font-family: system-ui, sans-serif;
}

.nn-12 *,
.nn-12 *::before,
.nn-12 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(50% 0.1 200)) {
  .nn-12 {
    --nn-12-bg: oklch(14% 0.035 265);
    --nn-12-ink: oklch(96% 0.018 265);
    --nn-12-muted: oklch(72% 0.035 265);
    --nn-12-line: oklch(28% 0.05 265);
    --nn-12-near: oklch(88% 0.15 200);
    --nn-12-mid: oklch(80% 0.11 255);
    --nn-12-far: oklch(74% 0.13 340);
  }
}

@media (prefers-color-scheme: light) {
  .nn-12 {
    --nn-12-bg: #e9ecf5;
    --nn-12-ink: #0b1024;
    --nn-12-muted: #4a5372;
    --nn-12-line: #c4cade;
    --nn-12-near: #046a80;
    --nn-12-mid: #2b4d90;
    --nn-12-far: #8f2b74;
  }
}

.nn-12[data-theme="light"] {
  --nn-12-bg: #e9ecf5;
  --nn-12-ink: #0b1024;
  --nn-12-muted: #4a5372;
  --nn-12-line: #c4cade;
  --nn-12-near: #046a80;
  --nn-12-mid: #2b4d90;
  --nn-12-far: #8f2b74;
}

.nn-12[data-theme="dark"] {
  --nn-12-bad: #f4a4a4;
  --nn-12-warn: #f0c88a;
  --nn-12-bg: #050a1a;
  --nn-12-ink: #e8eeff;
  --nn-12-muted: #8e9cc4;
  --nn-12-line: #1a2547;
  --nn-12-near: #35e6ff;
  --nn-12-mid: #7fb4ff;
  --nn-12-far: #ff7ae0;
}

.nn-12__stage {
  max-width: 68rem;
  margin: 0 auto;
  padding: clamp(1.75rem, 5vw, 2.5rem) clamp(1.25rem, 5vw, 2.25rem) clamp(2.25rem, 6vw, 3rem);
  display: grid;
  gap: clamp(1.5rem, 4vw, 2rem);
}

.nn-12__kicker {
  margin: 0 0 .5rem;
  font-size: .7rem;
  letter-spacing: .28em;
  text-transform: uppercase;
  color: var(--nn-12-muted);
}

.nn-12__heading {
  margin: 0;
  font-family: var(--nn-12-font-display);
  font-size: clamp(1.45rem, 5vw, 2.15rem);
  font-weight: 600;
  letter-spacing: .04em;
  text-transform: uppercase;
  text-wrap: balance;
}

.nn-12__sub {
  margin: .6rem 0 0;
  max-width: 42rem;
  font-size: .9rem;
  line-height: 1.6;
  color: var(--nn-12-muted);
  text-wrap: pretty;
}

.nn-12__scene {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  min-height: clamp(15rem, 46vw, 24rem);
  border: 1px solid var(--nn-12-line);
  background: linear-gradient(180deg, #06122e 0%, #050a1a 62%, #03060f 100%);
}

.nn-12__far {
  position: absolute;
  inset: auto 0 42% 0;
  height: 34%;
}

.nn-12__horizon {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  height: 1px;
  background: var(--nn-12-fars);
  box-shadow: 0 0 clamp(1.5rem, 7vw, 3.75rem) .5rem color-mix(in srgb, var(--nn-12-fars) 20%, transparent);
}

.nn-12__tower {
  position: absolute;
  bottom: 0;
  width: clamp(1.25rem, 5vw, 2.25rem);
  background: color-mix(in srgb, var(--nn-12-fars) 26%, transparent);
  box-shadow: 0 0 clamp(1.5rem, 7vw, 3.75rem) color-mix(in srgb, var(--nn-12-fars) 20%, transparent);
}

.nn-12__tower--a {
  left: 14%;
  height: 62%;
}

.nn-12__tower--b {
  left: 34%;
  height: 88%;
}

.nn-12__tower--c {
  right: 22%;
  height: 48%;
}

.nn-12__haze {
  position: absolute;
  inset: 30% 0 30% 0;
  background: linear-gradient(180deg, transparent, color-mix(in srgb, var(--nn-12-mids) 12%, transparent) 55%, transparent);
  mix-blend-mode: screen;
  animation: nn-12-drift 18s ease-in-out infinite alternate;
}

@keyframes nn-12-drift {
  from {
    transform: translate3d(-2%, 0, 0);
  }

  to {
    transform: translate3d(2%, 0, 0);
  }
}

.nn-12__mid {
  position: absolute;
  inset: auto 0 26% 0;
  display: flex;
  align-items: flex-end;
  justify-content: center;
  gap: clamp(1rem, 5vw, 2.5rem);
}

.nn-12__bar {
  width: clamp(.4rem, 1.6vw, .7rem);
  background: var(--nn-12-mids);
  box-shadow: 0 0 .2rem color-mix(in srgb, var(--nn-12-mids) 60%, transparent), 0 0 clamp(.9rem, 4vw, 1.4rem) color-mix(in srgb, var(--nn-12-mids) 30%, transparent), 0 0 clamp(1.75rem, 8vw, 2.9rem) color-mix(in srgb, var(--nn-12-mids) 18%, transparent);
}

.nn-12__bar--1 {
  height: clamp(3rem, 12vw, 6rem);
}

.nn-12__bar--2 {
  height: clamp(4.5rem, 17vw, 8.5rem);
}

.nn-12__bar--3 {
  height: clamp(2.5rem, 9vw, 4.5rem);
}

.nn-12__near {
  position: absolute;
  inset: auto 0 clamp(1rem, 4vw, 2rem) 0;
  display: grid;
  place-items: center;
  padding: 0 1rem;
}

.nn-12__sign {
  margin: 0;
  padding: clamp(.6rem, 2.5vw, .9rem) clamp(1rem, 4vw, 1.6rem);
  border: 2px solid var(--nn-12-nears);
  color: var(--nn-12-spec-ink);
  font-family: var(--nn-12-font-display);
  font-size: clamp(.95rem, 4vw, 1.5rem);
  font-weight: 600;
  letter-spacing: .18em;
  text-transform: uppercase;
  text-align: center;
  box-shadow: 0 0 .25rem var(--nn-12-nears), 0 0 clamp(.75rem, 3.5vw, .9rem) color-mix(in srgb, var(--nn-12-nears) 50%, transparent), 0 0 clamp(1.5rem, 8vw, 2.15rem) color-mix(in srgb, var(--nn-12-nears) 28%, transparent);
  text-shadow: 0 0 .3rem color-mix(in srgb, var(--nn-12-nears) 55%, transparent);
}

.nn-12__vignette {
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: radial-gradient(120% 90% at 50% 58%, transparent 40%, rgba(2, 4, 12, .78) 100%);
}

.nn-12__bands {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: 0;
  border-top: 1px solid var(--nn-12-line);
}

.nn-12__band {
  display: grid;
  gap: .3rem .9rem;
  padding: .65rem 0;
  border-bottom: 1px solid var(--nn-12-line);
  grid-template-columns: 1fr;
}

@media (min-width: 40rem) {
  .nn-12__band {
    grid-template-columns: 5rem minmax(0, 1fr);
    align-items: baseline;
  }
}

.nn-12__blabel {
  font-size: .7rem;
  letter-spacing: .18em;
  text-transform: uppercase;
}

.nn-12__blabel--near {
  color: var(--nn-12-near);
}

.nn-12__blabel--mid {
  color: var(--nn-12-mid);
}

.nn-12__blabel--far {
  color: var(--nn-12-far);
}

.nn-12__bval {
  font-family: ui-monospace, Menlo, monospace;
  font-size: .72rem;
  line-height: 1.55;
  color: var(--nn-12-muted);
  min-inline-size: 0;
}

@media (prefers-reduced-motion: reduce) {
  .nn-12__haze {
    animation: none;
    transform: none;
    opacity: 1;
  }
}
```
