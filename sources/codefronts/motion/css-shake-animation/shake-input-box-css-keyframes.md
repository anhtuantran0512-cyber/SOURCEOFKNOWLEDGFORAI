---
source: "codefronts"
url: "https://codefronts.com/motion/css-shake-animation/shake-input-box-css-keyframes/"
title: "Shake Input Box CSS Keyframes"
section: "motion"
category: "css-shake-animation"
category_name: "CSS Shake Animations"
description: "The keyframes themselves, put under glass: an anatomy specimen that replays the classic decaying shake on a loop next to its actual keyframe table, and an…"
has_js: "false"
---

Here's a working CSS Shake Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Shake Input Box CSS Keyframes
Source: https://codefronts.com/motion/css-shake-animation/shake-input-box-css-keyframes/

The keyframes themselves, put under glass: an anatomy specimen that replays the classic decaying shake on a loop next to its actual keyframe table, and an amplitude scale where the same input box shakes at 2px, 6px and 12px so you can pick a violence level by feel instead of by guessing.
## HTML
```html
<div class="shk-05-group">
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:[email protected]&family=Archivo:[email protected]&display=swap" rel="stylesheet">
<section class="shk-05a" aria-label="Anatomy of shake keyframes">
  <div class="shk-05a__board">
    <div class="shk-05a__left">
      <p class="shk-05a__eyebrow">Specimen · replays every 3.2s</p>
      <div class="shk-05a__stage"><input class="shk-05a__box" type="text" value="hello@wrong" readonly aria-label="Specimen input"><span class="shk-05a__ruler" aria-hidden="true"><i>-12</i><i>0</i><i>+12</i></span></div>
      <p class="shk-05a__cap" aria-hidden="true">decay: 9 → 8 → 6 → 4 → 2 → 1 px</p>
    </div>
    <pre class="shk-05a__code" aria-label="The keyframes"><code>@keyframes shake-input {
  12% { translate: -9px 0 }
  30% { translate:  8px 0 }
  48% { translate: -6px 0 }
  64% { translate:  4px 0 }
  80% { translate: -2px 0 }
  94% { translate:  1px 0 }
}
.box.shake {
  animation: shake-input .5s
    cubic-bezier(.36,.07,.19,.97) both;
}</code></pre>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="shk-05b" aria-label="Same shake at three amplitudes">
  <div class="shk-05b__stack">
    <p class="shk-05b__title">Pick your violence level</p>
    <p class="shk-05b__sub">Hover (or tap) each box — identical keyframes, only <b>--amp</b> changes.</p>
    <label class="shk-05b__row" style="--amp:2px"><span class="shk-05b__tag">2px · whisper</span><input class="shk-05b__box" type="text" placeholder="Subtle nudge — barely there" aria-label="2 pixel shake demo"></label>
    <label class="shk-05b__row" style="--amp:6px"><span class="shk-05b__tag">6px · standard</span><input class="shk-05b__box" type="text" placeholder="The default error shake" aria-label="6 pixel shake demo"></label>
    <label class="shk-05b__row" style="--amp:12px"><span class="shk-05b__tag">12px · alarm</span><input class="shk-05b__box" type="text" placeholder="Reserved for destructive mistakes" aria-label="12 pixel shake demo"></label>
  </div>
</section>
</div>
```
## CSS
```css
.shk-05-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.shk-05-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.shk-05a,
.shk-05a *,
.shk-05a *::before,
.shk-05a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-05a {
  --blue: oklch(0.55 0.13 255);
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #f4f6f9 linear-gradient(rgba(85,120,190,.09) 1px,transparent 1px),linear-gradient(90deg,rgba(85,120,190,.09) 1px,transparent 1px);
  background-size: 100% 100%,28px 28px,28px 28px;
  font-family: 'Archivo','Segoe UI',system-ui,sans-serif;
}

.shk-05a__board {
  display: flex;
  flex-wrap: wrap;
  gap: 34px;
  align-items: center;
  justify-content: center;
  width: min(860px,100%);
}

.shk-05a__left {
  flex: 1 1 320px;
  max-width: 420px;
}

.shk-05a__eyebrow {
  font-family: 'IBM Plex Mono',ui-monospace,monospace;
  font-size: 11px;
  font-weight: 600;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--blue);
}

.shk-05a__stage {
  margin-top: 16px;
  padding: 36px 28px 30px;
  background: #fff;
  border: 1.5px solid rgba(30,45,80,.14);
  border-radius: 16px;
  box-shadow: 0 24px 50px -30px rgba(30,45,80,.4);
}

.shk-05a__box {
  display: block;
  width: 100%;
  padding: 13px 16px;
  font-family: 'IBM Plex Mono',ui-monospace,monospace;
  font-size: 15px;
  color: #26314a;
  background: #fff;
  border: 1.5px solid oklch(0.62 0.19 25);
  border-radius: 11px;
  outline: none;
  box-shadow: 0 0 0 4px oklch(0.62 0.19 25 / .12);
  animation: shk-05a-loop 3.2s cubic-bezier(.36,.07,.19,.97) infinite;
}

.shk-05a__ruler {
  display: flex;
  justify-content: space-between;
  margin-top: 14px;
  font-family: 'IBM Plex Mono',ui-monospace,monospace;
  font-size: 10px;
  color: rgba(38,49,74,.45);
  border-top: 1px dashed rgba(38,49,74,.25);
  padding-top: 6px;
}

.shk-05a__cap {
  margin-top: 12px;
  font-family: 'IBM Plex Mono',ui-monospace,monospace;
  font-size: 11.5px;
  color: rgba(38,49,74,.55);
}

.shk-05a__code {
  flex: 1 1 300px;
  max-width: 400px;
  padding: 24px 26px;
  background: #101a2c;
  color: #c8d6f2;
  border-radius: 16px;
  font-family: 'IBM Plex Mono',ui-monospace,monospace;
  font-size: 12.5px;
  line-height: 1.75;
  box-shadow: 0 30px 60px -30px rgba(16,26,44,.7);
  overflow: auto;
}

@keyframes shk-05a-loop {
  2% {
    translate: -9px 0;
  }

  4.5% {
    translate: 8px 0;
  }

  7% {
    translate: -6px 0;
  }

  9.5% {
    translate: 4px 0;
  }

  12% {
    translate: -2px 0;
  }

  14% {
    translate: 1px 0;
  }

  15.6%,
    100% {
    translate: 0 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-05a__box {
    animation: none;
  }
}

.shk-05b,
.shk-05b *,
.shk-05b *::before,
.shk-05b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-05b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(170deg,#101418,#161c23);
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.shk-05b__stack {
  width: min(480px,100%);
  display: grid;
  gap: 16px;
}

.shk-05b__title {
  font-size: 26px;
  font-weight: 700;
  letter-spacing: -.02em;
  color: #ecf2f8;
}

.shk-05b__sub {
  font-size: 13.5px;
  color: rgba(220,232,244,.55);
  margin-bottom: 8px;
}

.shk-05b__sub b {
  color: oklch(0.82 0.15 75);
}

.shk-05b__row {
  display: grid;
  gap: 7px;
  cursor: pointer;
}

.shk-05b__tag {
  font-size: 11px;
  font-weight: 600;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: rgba(220,232,244,.5);
}

.shk-05b__box {
  width: 100%;
  padding: 14px 17px;
  font: inherit;
  font-size: 14.5px;
  color: #ecf2f8;
  background: rgba(255,255,255,.05);
  border: 1.5px solid rgba(160,185,215,.2);
  border-radius: 13px;
  outline: none;
  transition: border-color .2s;
}

.shk-05b__box::placeholder {
  color: rgba(220,232,244,.4);
}

.shk-05b__row:hover .shk-05b__box {
  border-color: oklch(0.82 0.15 75);
  animation: shk-05b-shake .5s cubic-bezier(.36,.07,.19,.97);
}

.shk-05b__box:focus-visible {
  border-color: oklch(0.75 0.12 250);
  box-shadow: 0 0 0 4px oklch(0.75 0.12 250 / .18);
}

@keyframes shk-05b-shake {
  12% {
    translate: calc(var(--amp) * -1) 0;
  }

  30% {
    translate: calc(var(--amp) * .88) 0;
  }

  48% {
    translate: calc(var(--amp) * -.66) 0;
  }

  64% {
    translate: calc(var(--amp) * .44) 0;
  }

  80% {
    translate: calc(var(--amp) * -.22) 0;
  }

  94% {
    translate: calc(var(--amp) * .11) 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-05b__row:hover .shk-05b__box {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the specimen loops by stretching the .5s shake into a 3.2s timeline (frames land in the first 15.6%, the rest is idle), the same trick used for periodic attention CTAs. */

/* No JavaScript — ONE @keyframes rule serves all three boxes: every offset is calc(var(--amp) * ratio), so amplitude is a per-element custom property, not a copy-pasted keyframe block. */
```
