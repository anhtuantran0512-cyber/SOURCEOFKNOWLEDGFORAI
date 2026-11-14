---
source: "codefronts"
url: "https://codefronts.com/motion/css-scroll-animations/cinematic-image-wipe/"
title: "Fill Mode and Why Duration Is Ignored"
section: "motion"
category: "css-scroll-animations"
category_name: "CSS Scroll Animations"
description: "Two rules that trip up everyone."
has_js: "false"
---

Here's a working CSS Scroll Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Fill Mode and Why Duration Is Ignored
Source: https://codefronts.com/motion/css-scroll-animations/cinematic-image-wipe/

Two rules that trip up everyone. animation-duration is ignored on a scroll timeline, because the progress is the scroll offset and there is no time to spend. animation-fill-mode matters more than usual, because it decides what an element looks like outside its range — and here all four values sit side by side at the same offset.
## HTML
```html
<section class="sa-18" aria-labelledby="sa-18-h">
  <fieldset class="sa-18__theme">
    <legend class="sa-18__themelegend">Theme</legend>
    <input class="sa-18__themeinput" type="radio" name="sa-18-theme" id="sa-18-theme-auto" checked>
    <label class="sa-18__themeopt" for="sa-18-theme-auto">Auto</label>
    <input class="sa-18__themeinput" type="radio" name="sa-18-theme" id="sa-18-theme-light">
    <label class="sa-18__themeopt" for="sa-18-theme-light">Light</label>
    <input class="sa-18__themeinput" type="radio" name="sa-18-theme" id="sa-18-theme-dark">
    <label class="sa-18__themeopt" for="sa-18-theme-dark">Dark</label>
  </fieldset>

  <div class="sa-18__stage">
    <header class="sa-18__head">
      <p class="sa-18__eyebrow">fill-mode · duration</p>
      <h2 class="sa-18__h" id="sa-18-h">Four fill modes, one range, no duration</h2>
      <p class="sa-18__sub">All four bars share <span class="sa-18__mono">animation-range: 35% 65%</span> and a <span class="sa-18__mono">4s</span> duration that does nothing. Scroll to the top and bottom of the panel to see them disagree.</p>
    </header>

    <div class="sa-18__scroller" tabindex="0" role="region" aria-label="Fill mode comparison, scrollable">
      <div class="sa-18__pinned">
        <div class="sa-18__cols">
          <div class="sa-18__col">
            <p class="sa-18__cname">forwards</p>
            <div class="sa-18__well"><span class="sa-18__bar sa-18__bar--fwd"></span></div>
            <p class="sa-18__cv">Before: unanimated. After: holds the last keyframe.</p>
          </div>
          <div class="sa-18__col">
            <p class="sa-18__cname">backwards</p>
            <div class="sa-18__well"><span class="sa-18__bar sa-18__bar--bwd"></span></div>
            <p class="sa-18__cv">Before: holds the first keyframe. After: snaps back.</p>
          </div>
          <div class="sa-18__col sa-18__col--pick">
            <p class="sa-18__cname">both</p>
            <div class="sa-18__well"><span class="sa-18__bar sa-18__bar--both"></span></div>
            <p class="sa-18__cv">Holds at both ends. The right default for scroll-bound work.</p>
          </div>
          <div class="sa-18__col">
            <p class="sa-18__cname">none</p>
            <div class="sa-18__well"><span class="sa-18__bar sa-18__bar--none"></span></div>
            <p class="sa-18__cv">Unanimated on both sides. Pops in and out at the boundaries.</p>
          </div>
        </div>
        <p class="sa-18__rangebar"><span class="sa-18__rangewin">active range · 35% – 65%</span></p>
      </div>
      <div class="sa-18__filler">
        <p class="sa-18__p">Keep scrolling. Between 35% and 65% all four agree, because inside the range fill mode is irrelevant.</p>
        <p class="sa-18__p">Outside it they diverge, and that divergence is the whole reason scroll-bound animations appear to flicker.</p>
        <p class="sa-18__p">The <span class="sa-18__mono">4s</span> duration on every bar is inert. Delete it, set it to <span class="sa-18__mono">40s</span> — the scrub is identical.</p>
        <p class="sa-18__p">To make the scrub slower in scroll terms, widen the range. That is the only lever.</p>
        <p class="sa-18__p">Scroll back up slowly and watch the boundaries. The forwards bar drops at 65%, the backwards bar drops at 35%, and the none bar drops at both.</p>
        <p class="sa-18__p">The both column is the only one that never changes appearance except by scrolling through its range. That predictability is why it is the default worth memorising.</p>
        <p class="sa-18__p">The shorthand resets what you do not state, so <span class="sa-18__mono">animation: name linear</span> quietly means fill mode none.</p>
        <p class="sa-18__p">On a document timeline fill mode is mostly a detail of the first and last frame. Here it governs most of the scroll.</p>
        <p class="sa-18__p">If a scroll-bound element flickers at one specific offset, check its range boundary before you touch the keyframes.</p>
        <p class="sa-18__p">Devtools shows the duration as applied. It is applied, it is simply never read.</p>
        <p class="sa-18__p">The same rule covers <span class="sa-18__mono">animation-delay</span>. A delay is a time offset, and there is no time here either.</p>
        <p class="sa-18__p"><span class="sa-18__mono">animation-iteration-count</span> is likewise meaningless: a scroll timeline runs once across its range, in whichever direction you scroll.</p>
        <p class="sa-18__p"><span class="sa-18__mono">animation-direction: reverse</span> does still work, because it flips the mapping from progress to keyframes rather than the passage of time.</p>
        <p class="sa-18__p">And <span class="sa-18__mono">animation-play-state: paused</span> freezes the element at its current progress, which is occasionally useful as a debugging pin.</p>
        <p class="sa-18__p">Practical rule: any property that describes time is inert; any property that describes mapping still applies.</p>
        <p class="sa-18__p">Set the base style to the finished frame, set fill mode to both, and the two agree at every offset outside the range.</p>
        <p class="sa-18__p">When a reviewer asks why the duration is still in the declaration, the honest answer is that it should not be.</p>
        <p class="sa-18__p">Strip inert declarations before shipping. They survive as evidence that the author expected them to do something.</p>
        <p class="sa-18__p">Scroll back to the top and watch the four columns disagree one more time — that disagreement is the entire lesson here.</p>
        <p class="sa-18__p">A quick way to remember it: fill mode answers "what does this look like when the animation is not running", and on a scroll timeline that is most of the page.</p>
        <p class="sa-18__p">Forwards is the safe half of both. If an element only ever needs to hold its finished state, forwards is enough and reads more precisely.</p>
        <p class="sa-18__p">Backwards is rare in scroll work. It mostly appears by accident, copied from a document-timeline entrance where it made sense.</p>
        <p class="sa-18__p">None is the shorthand's default, which is why so many scroll animations flicker on their first review pass.</p>
        <p class="sa-18__p">Prism ships both everywhere and treats any other value as a deliberate, commented decision.</p>
        <p class="sa-18__p">Jordan Lee's review note on the Talon dashboard: three flicker reports, three missing fill modes, one line each to fix.</p>
        <p class="sa-18__p">If you take one thing from this panel: duration is inert, fill mode is not, and the range is the only timing control you have.</p>
        <p class="sa-18__p">Everything below the active window is the same four bars, still disagreeing, still on the same timeline.</p>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.sa-18 {
  --page: #efe7dc;
  --surface: #f7f2ea;
  --ink: #2b211a;
  --muted: #6f5f52;
  --rule: #d8cbba;
  --accent: #a97c26;
  --page: oklch(92% 0.018 70);
  --surface: oklch(95.5% 0.014 75);
  --ink: oklch(26% 0.025 55);
  --muted: oklch(50% 0.028 60);
  --rule: oklch(84% 0.02 70);
  --accent: oklch(60% 0.11 78);
  --font-display: Rockwell, "Bookman Old Style", "Courier New", Georgia, serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  position: relative;
  padding: 3.25rem 0.75rem 2.5rem;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, sans-serif;
}

.sa-18 *,
.sa-18 *::before,
.sa-18 *::after {
  box-sizing: border-box;
}

.sa-18__stage {
  max-inline-size: 58rem;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.sa-18__head {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
  padding-inline: 0.25rem;
}

.sa-18__eyebrow {
  margin: 0;
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.625rem;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--accent);
}

.sa-18__h {
  margin: 0;
  font-family: var(--font-display);
  font-size: clamp(1.25rem, 3.8vw, 1.875rem);
  font-weight: 400;
  letter-spacing: -0.01em;
  line-height: 1.15;
}

.sa-18__sub {
  margin: 0;
  max-inline-size: 44rem;
  font-size: 0.8125rem;
  line-height: 1.5;
  color: var(--muted);
  text-wrap: pretty;
}

.sa-18__mono {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.85em;
  color: var(--accent);
}

.sa-18__scroller {
  block-size: 64vh;
  min-block-size: 20rem;
  overflow-y: auto;
  overscroll-behavior: contain;
  background: var(--surface);
  scroll-timeline: --sa-18-track block;
}

.sa-18__scroller:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: -2px;
}

.sa-18__pinned {
  position: sticky;
  inset-block-start: 0;
  z-index: 2;
  padding: 0.5rem 0.5rem 0.375rem;
  background: var(--surface);
}

.sa-18__cols {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 0.375rem;
}

.sa-18__col {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
  padding: 0.375rem;
  min-inline-size: 0;
}

.sa-18__col--pick {
  background: color-mix(in srgb, var(--accent) 12%, transparent);
}

.sa-18__cname {
  margin: 0;
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.6875rem;
  font-weight: 600;
  letter-spacing: 0.02em;
}

.sa-18__well {
  block-size: 3.25rem;
  background: color-mix(in srgb, var(--ink) 7%, transparent);
  display: flex;
  align-items: end;
}

.sa-18__bar {
  display: block;
  inline-size: 100%;
  block-size: 100%;
  background: var(--accent);
  transform-origin: bottom center;
  transform: scaleY(1);
}

.sa-18__bar--bwd,
.sa-18__bar--none {
  background: color-mix(in srgb, var(--accent) 65%, var(--ink));
}

.sa-18__cv {
  margin: 0;
  font-size: 0.625rem;
  line-height: 1.4;
  color: var(--muted);
  text-wrap: pretty;
}

.sa-18__rangebar {
  margin: 0.375rem 0 0;
  padding: 0.25rem 0.375rem;
  background: color-mix(in srgb, var(--ink) 6%, transparent);
}

.sa-18__rangewin {
  display: block;
  inline-size: 30%;
  margin-inline-start: 35%;
  padding: 0.125rem 0;
  background: var(--accent);
  color: var(--surface);
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.5625rem;
  letter-spacing: 0.04em;
  text-align: center;
  white-space: nowrap;
}

.sa-18__filler {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  min-block-size: calc(100% + 8rem);
  padding: 0.75rem 0.75rem 3rem;
}

.sa-18__p {
  margin: 0;
  font-size: 0.75rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

@keyframes sa-18-rise {
  from {
    transform: scaleY(0.12);
  }

  to {
    transform: scaleY(1);
  }
}

@supports (animation-timeline: scroll()) {
  .sa-18__bar {
    animation-name: sa-18-rise;
    animation-timing-function: linear;
    animation-duration: 4s;
    animation-timeline: --sa-18-track;
    animation-range: 35% 65%;
    transform: scaleY(0.12);
  }

  .sa-18__bar--fwd {
    animation-fill-mode: forwards;
  }

  .sa-18__bar--bwd {
    animation-fill-mode: backwards;
  }

  .sa-18__bar--both {
    animation-fill-mode: both;
  }

  .sa-18__bar--none {
    animation-fill-mode: none;
  }

  .sa-18__bar--fwd,
    .sa-18__bar--none {
    transform: scaleY(1);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sa-18__bar {
    animation: none;
    transform: scaleY(1);
  }
}

.sa-18__theme {
  position: absolute;
  inset-block-start: 0.75rem;
  inset-inline-end: 0.75rem;
  z-index: 9;
  display: inline-flex;
  gap: 0;
  margin: 0;
  padding: 0;
  border: 0;
}

.sa-18__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.sa-18__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.sa-18__themeopt {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-block-size: 2.25rem;
  min-inline-size: 2.75rem;
  padding: 0 0.5rem;
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.625rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--muted);
  cursor: pointer;
  user-select: none;
}

.sa-18__themeinput:checked + .sa-18__themeopt {
  color: var(--surface);
  background: var(--ink);
}

.sa-18__themeinput:focus-visible + .sa-18__themeopt {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

@media (max-width: 40rem) {
  .sa-18__cols {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .sa-18 {
    padding-block-start: 4rem;
  }
}

@media (forced-colors: active) {
  .sa-18__bar {
    background: Highlight;
  }
}

@media (prefers-color-scheme: dark) {
  .sa-18:not(:has(#sa-18-theme-light:checked)) {
    --page: #161210;
    --surface: #1e1917;
    --ink: #f0e6da;
    --muted: #a3928380;
    --muted: #a39283;
    --rule: #322a25;
    --accent: #d4a24a;
  }
}

@media (prefers-color-scheme: light) {
  .sa-18:has(#sa-18-theme-dark:checked) {
    --page: #161210;
    --surface: #1e1917;
    --ink: #f0e6da;
    --muted: #a39283;
    --rule: #322a25;
    --accent: #d4a24a;
  }
}

[data-theme="dark"] .sa-18:not(:has(#sa-18-theme-light:checked)) {
  --page: #161210;
  --surface: #1e1917;
  --ink: #f0e6da;
  --muted: #a39283;
  --rule: #322a25;
  --accent: #d4a24a;
}

.sa-18:has(#sa-18-theme-dark:checked) {
  --page: #161210;
  --surface: #1e1917;
  --ink: #f0e6da;
  --muted: #a39283;
  --rule: #322a25;
  --accent: #d4a24a;
}

.sa-18:has(#sa-18-theme-light:checked) {
  --page: #efe7dc;
  --surface: #f7f2ea;
  --ink: #2b211a;
  --muted: #6f5f52;
  --rule: #d8cbba;
  --accent: #a97c26;
}
```
