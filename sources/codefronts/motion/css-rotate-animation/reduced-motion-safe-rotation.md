---
source: "codefronts"
url: "https://codefronts.com/motion/css-rotate-animation/reduced-motion-safe-rotation/"
title: "Reduced Motion Safe Rotation"
section: "motion"
category: "css-rotate-animation"
category_name: "CSS Rotate Animations"
description: "Continuous rotation is a genuine vestibular trigger, so this demo makes the guard the subject."
has_js: "false"
---

Here's a working CSS Rotate Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Reduced Motion Safe Rotation
Source: https://codefronts.com/motion/css-rotate-animation/reduced-motion-safe-rotation/

Continuous rotation is a genuine vestibular trigger, so this demo makes the guard the subject. Three tiers sit side by side — full rotation, a reduced variant that conveys the same state with a single settled angle, and complete suppression — with the media query written in both directions and a simulate toggle so you can see all three without changing your system settings.
## HTML
```html
<section class="rot-20" aria-labelledby="rot-20-h">
  <fieldset class="rot-20__theme">
    <legend class="rot-20__themelegend">Theme</legend>
    <input class="rot-20__themeinput" type="radio" name="rot-20-theme" id="rot-20-theme-auto" checked>
    <label class="rot-20__themeopt" for="rot-20-theme-auto">Auto</label>
    <input class="rot-20__themeinput" type="radio" name="rot-20-theme" id="rot-20-theme-light">
    <label class="rot-20__themeopt" for="rot-20-theme-light">Light</label>
    <input class="rot-20__themeinput" type="radio" name="rot-20-theme" id="rot-20-theme-dark">
    <label class="rot-20__themeopt" for="rot-20-theme-dark">Dark</label>
  </fieldset>
  <label class="rot-20__sim">
    <input class="rot-20__simbox" type="checkbox" id="rot-20-sim">
    <span class="rot-20__simdot" aria-hidden="true">
      <svg viewBox="0 0 16 16" width="12" height="12" focusable="false"><path d="M2.5 8h11" stroke="currentColor" stroke-width="2" stroke-linecap="round"></path></svg>
    </span>
    <span class="rot-20__simtext">Simulate reduce</span>
  </label>

  <div class="rot-20__stage">
    <header class="rot-20__head">
      <p class="rot-20__eyebrow">Prism Health · Motion policy</p>
      <h2 class="rot-20__h" id="rot-20-h">Degrade to the finished state, never to nothing</h2>
      <p class="rot-20__sub">Continuous rotation is a vestibular trigger. Here are the three honest responses to <span class="rot-20__code">prefers-reduced-motion: reduce</span>, side by side.</p>
    </header>

    <div class="rot-20__tiers">
      <article class="rot-20__tier">
        <p class="rot-20__tiernum">Tier 1</p>
        <h3 class="rot-20__tierh">Full rotation</h3>
        <div class="rot-20__well">
          <span class="rot-20__mark rot-20__mark--spin" aria-hidden="true"></span>
        </div>
        <p class="rot-20__tierp">Authored inside <span class="rot-20__code">no-preference</span>, so the motion is the enhancement rather than the default. Runs only when motion is welcome.</p>
      </article>

      <article class="rot-20__tier rot-20__tier--mid">
        <p class="rot-20__tiernum">Tier 2</p>
        <h3 class="rot-20__tierh">Reduced, still informative</h3>
        <div class="rot-20__well">
          <span class="rot-20__mark rot-20__mark--settle" aria-hidden="true"></span>
          <span class="rot-20__fade" aria-hidden="true"></span>
        </div>
        <p class="rot-20__tierp">One settled angle change and a cross-fade instead of continuous rotation. The state still arrives; the movement does not.</p>
      </article>

      <article class="rot-20__tier rot-20__tier--off">
        <p class="rot-20__tiernum">Tier 3</p>
        <h3 class="rot-20__tierh">Suppressed entirely</h3>
        <div class="rot-20__well">
          <span class="rot-20__mark rot-20__mark--static" aria-hidden="true"></span>
        </div>
        <p class="rot-20__tierp">Purely decorative motion should simply not run. The frame, the label and the layout all stay — only the movement is gone.</p>
      </article>
    </div>

    <div class="rot-20__rules">
      <pre class="rot-20__pre">@media (prefers-reduced-motion: no-preference) {
  .mark { animation: turn 6s linear infinite; }
}
@media (prefers-reduced-motion: reduce) {
  .mark { transform: rotate(34deg); }
}</pre>
      <p class="rot-20__rulesp">Both directions, written out. The static state is the default and the animation is opted into — so an element you forget to guard is calm rather than moving.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.rot-20 {
  --page: #f7f5f0;
  --surface: #ffffff;
  --ink: #191b18;
  --muted: #5f635c;
  --rule: #dedcd4;
  --accent: #2f7d54;
  --dur: 6s;
  --rest: 34deg;
  --font-display: ui-sans-serif, "Noto Sans", "Segoe UI", system-ui, sans-serif;
  position: relative;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--page);
  color: var(--ink);
  font-family: var(--font-display);
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(0 0 0)) {
  .rot-20 {
    --accent: oklch(0.52 0.11 158);
  }
}

.rot-20 *,
.rot-20 *::before,
.rot-20 *::after {
  box-sizing: border-box;
}

.rot-20__stage {
  display: grid;
  place-items: center;
  gap: clamp(1.5rem, 4vw, 2.25rem);
  padding: clamp(1.25rem, 4vw, 3rem);
  padding-block-start: 5.25rem;
}

.rot-20__head {
  max-inline-size: 38rem;
  min-inline-size: 0;
  text-align: center;
}

.rot-20__eyebrow {
  margin: 0 0 0.6rem;
  font-size: 0.6875rem;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--accent);
}

.rot-20__h {
  margin: 0 0 0.6rem;
  font-size: clamp(1.375rem, 4.6vw, 2.125rem);
  font-weight: 650;
  letter-spacing: -0.015em;
  line-height: 1.16;
}

.rot-20__sub {
  margin: 0;
  font-size: 0.9375rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.rot-20__code {
  font-family: ui-monospace, Menlo, Consolas, monospace;
  font-size: 0.85em;
  padding: 0.1em 0.3em;
  border-radius: 0.25rem;
  background: color-mix(in srgb, var(--accent) 10%, transparent);
  color: var(--accent);
}

.rot-20__tiers {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(13rem, 1fr));
  gap: 0.875rem;
  inline-size: min(100%, 50rem);
}

.rot-20__tier {
  min-inline-size: 0;
  display: grid;
  gap: 0.5rem;
  justify-items: start;
  padding: 1rem;
  border: 1px solid var(--rule);
  border-radius: 0.75rem;
  background: var(--surface);
}

.rot-20__tier--mid {
  background: color-mix(in srgb, var(--accent) 5%, var(--surface));
}

.rot-20__tier--off {
  background: color-mix(in srgb, var(--ink) 4%, var(--surface));
}

.rot-20__tiernum {
  margin: 0;
  font-family: ui-monospace, Menlo, Consolas, monospace;
  font-size: 0.6875rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--muted);
}

.rot-20__tierh {
  margin: 0 0 0.35rem;
  font-size: 1rem;
  font-weight: 650;
}

.rot-20__well {
  position: relative;
  display: grid;
  place-items: center;
  inline-size: 100%;
  block-size: clamp(5rem, 18vw, 6.5rem);
  border-radius: 0.5rem;
  background: color-mix(in srgb, var(--ink) 3%, transparent);
}

.rot-20__mark {
  position: relative;
  inline-size: clamp(2.5rem, 9vw, 3.25rem);
  aspect-ratio: 1;
  border: 0.28rem solid var(--accent);
  border-radius: 0.4rem;
  transform: rotate(0deg);
}

.rot-20__mark::after {
  content: "";
  position: absolute;
  inset-block-start: -0.75rem;
  inset-inline-start: 50%;
  inline-size: 0.4rem;
  block-size: 0.4rem;
  translate: -50% 0;
  border-radius: 50%;
  background: var(--accent);
}

.rot-20__mark--settle {
  transform: rotate(var(--rest));
}

.rot-20__mark--static {
  transform: rotate(12deg);
  border-color: color-mix(in srgb, var(--ink) 45%, transparent);
}

.rot-20__mark--static::after {
  background: color-mix(in srgb, var(--ink) 45%, transparent);
}

.rot-20__fade {
  position: absolute;
  inset-block-end: 0.5rem;
  inset-inline-start: 50%;
  translate: -50% 0;
  inline-size: 2.5rem;
  block-size: 0.2rem;
  border-radius: 999px;
  background: var(--accent);
  opacity: 0.35;
}

.rot-20__tierp {
  margin: 0;
  font-size: 0.8125rem;
  line-height: 1.6;
  color: var(--muted);
  min-inline-size: 0;
}

.rot-20__rules {
  inline-size: min(100%, 50rem);
  display: grid;
  gap: 0.75rem;
  padding: clamp(0.875rem, 3vw, 1.25rem);
  border: 1px solid var(--rule);
  border-radius: 0.75rem;
  background: var(--surface);
}

.rot-20__pre {
  margin: 0;
  padding: 0.875rem;
  border-radius: 0.5rem;
  background: color-mix(in srgb, var(--accent) 7%, transparent);
  font-family: ui-monospace, Menlo, Consolas, monospace;
  font-size: 0.75rem;
  line-height: 1.65;
  overflow-x: auto;
}

.rot-20__rulesp {
  margin: 0;
  font-size: 0.8125rem;
  line-height: 1.65;
  color: var(--muted);
  min-inline-size: 0;
}

@keyframes rot-20-turn {
  to {
    transform: rotate(360deg);
  }
}

@keyframes rot-20-settle {
  from {
    transform: rotate(0deg);
  }

  to {
    transform: rotate(var(--rest));
  }
}

@media (prefers-reduced-motion: no-preference) {
  .rot-20__mark--spin {
    animation: rot-20-turn var(--dur) linear infinite;
  }

  .rot-20__mark--settle {
    animation: rot-20-settle 700ms cubic-bezier(0.25, 0.8, 0.3, 1) both;
  }
}

@media (prefers-reduced-motion: reduce) {
  .rot-20__mark--spin {
    animation: none;
    transform: rotate(var(--rest));
  }

  .rot-20__mark--settle {
    animation: none;
    transform: rotate(var(--rest));
  }
}

.rot-20:has(.rot-20__simbox:checked) .rot-20__mark--spin {
  animation: none;
  transform: rotate(var(--rest));
}

.rot-20:has(.rot-20__simbox:checked) .rot-20__mark--settle {
  animation: none;
  transform: rotate(var(--rest));
}

.rot-20:has(.rot-20__simbox:checked) .rot-20__simdot {
  background: var(--accent);
  color: var(--surface);
}

.rot-20__theme {
  position: absolute;
  inset-block-start: 0.875rem;
  inset-inline-end: 0.875rem;
  z-index: 9;
  display: flex;
  align-items: center;
  gap: 0.125rem;
  margin: 0;
  padding: 0.1875rem;
  border: 1px solid color-mix(in srgb, currentColor 18%, transparent);
  border-radius: 999px;
  background: color-mix(in srgb, currentColor 8%, transparent);
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
  font-family: system-ui, sans-serif;
}

.rot-20__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.rot-20__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.rot-20__themeopt {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-block-size: 2.25rem;
  min-inline-size: 2.75rem;
  padding: 0 0.6875rem;
  border-radius: 999px;
  font-size: 0.6875rem;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: inherit;
  opacity: 0.55;
  cursor: pointer;
  user-select: none;
  white-space: nowrap;
}

.rot-20__themeopt:hover {
  opacity: 0.85;
}

.rot-20__themeinput:checked + .rot-20__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.rot-20__themeinput:focus-visible + .rot-20__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

.rot-20__sim {
  position: absolute;
  inset-block-start: 0.875rem;
  inset-inline-start: 0.875rem;
  z-index: 9;
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  margin: 0;
  padding: 0.1875rem 0.75rem 0.1875rem 0.1875rem;
  border: 1px solid color-mix(in srgb, currentColor 18%, transparent);
  border-radius: 999px;
  background: color-mix(in srgb, currentColor 8%, transparent);
  font-size: 0.6875rem;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  cursor: pointer;
  user-select: none;
}

.rot-20__simbox {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.rot-20__simdot {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  inline-size: 2.25rem;
  block-size: 2.25rem;
  border-radius: 999px;
  background: color-mix(in srgb, currentColor 12%, transparent);
}

.rot-20__sim:has(.rot-20__simbox:focus-visible) {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

@media (forced-colors: active) {
  .rot-20__theme,
    .rot-20__sim {
    border-color: CanvasText;
    background: Canvas;
  }

  .rot-20__themeinput:checked + .rot-20__themeopt {
    background: Highlight;
    color: HighlightText;
  }
}

@media (prefers-color-scheme: dark) {
  .rot-20:not(:has(#rot-20-theme-light:checked)) {
    --page: #101210;
    --surface: #171a17;
    --ink: #eceee9;
    --muted: #979d95;
    --rule: #262a26;
    --accent: #62c793;
  }
}

@media (prefers-color-scheme: light) {
  .rot-20:has(#rot-20-theme-dark:checked) {
    --page: #101210;
    --surface: #171a17;
    --ink: #eceee9;
    --muted: #979d95;
    --rule: #262a26;
    --accent: #62c793;
  }
}

[data-theme="dark"] .rot-20:not(:has(#rot-20-theme-light:checked)) {
  --page: #101210;
  --surface: #171a17;
  --ink: #eceee9;
  --muted: #979d95;
  --rule: #262a26;
  --accent: #62c793;
}

.rot-20:has(#rot-20-theme-dark:checked) {
  --page: #101210;
  --surface: #171a17;
  --ink: #eceee9;
  --muted: #979d95;
  --rule: #262a26;
  --accent: #62c793;
}

.rot-20:has(#rot-20-theme-dark:checked) .rot-20__simdot {
  color: #0c120e;
}

.rot-20:has(#rot-20-theme-light:checked) {
  --page: #f7f5f0;
  --surface: #ffffff;
  --ink: #191b18;
  --muted: #5f635c;
  --rule: #dedcd4;
  --accent: #2f7d54;
}
```
