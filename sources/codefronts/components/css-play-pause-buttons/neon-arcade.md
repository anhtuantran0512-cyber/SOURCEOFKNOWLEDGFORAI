---
source: "codefronts"
url: "https://codefronts.com/components/css-play-pause-buttons/neon-arcade/"
title: "Retro Arcade Play Pause Button CSS"
section: "components"
category: "css-play-pause-buttons"
category_name: "CSS Play / Pause Buttons"
description: "A physical arcade key: a chunky cap sitting on a coloured plinth, with the whole thing travelling down into the plinth when pressed — the shadow shrinks by…"
has_js: "false"
---

Here's a working CSS Play / Pause Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Retro Arcade Play Pause Button CSS
Source: https://codefronts.com/components/css-play-pause-buttons/neon-arcade/

A physical arcade key: a chunky cap sitting on a coloured plinth, with the whole thing travelling down into the plinth when pressed — the shadow shrinks by exactly the distance the cap moves, which is what makes the depth read as real. The icon is genuine pixel art drawn with a stepped clip-path polygon, so it stays crisp at any size without a single image.
## HTML
```html
<section class="pp-15" aria-label="Retro arcade play pause button demo">
  <div class="pp-15__stage">
    <div class="pp-15__cabinet">
      <p class="pp-15__marquee">INSERT COIN — SIDE B</p>
      <div class="pp-15__screen" aria-hidden="true">
        <span class="pp-15__scan"></span>
        <p class="pp-15__ready">READY</p>
        <p class="pp-15__go">PLAYING</p>
      </div>
      <input class="pp-15-chk" type="checkbox" id="pp-15-toggle" aria-label="Play or pause">
      <label class="pp-15__cap" for="pp-15-toggle">
        <span class="pp-15__px" aria-hidden="true"></span>
        <span class="pp-15__bars" aria-hidden="true"><i></i><i></i></span>
      </label>
      <p class="pp-15__hint">PRESS TO START</p>
    </div>
    <p class="pp-15__chip" aria-hidden="true">travel + matching shadow shrink · stepped clip-path pixel art · 100ms linear</p>
  </div>
</section>
```
## CSS
```css
.pp-15,
.pp-15 *,
.pp-15 *::before,
.pp-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pp-15 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--pp-15-bg);
  --pp-15-bg: oklch(0.2 0.03 285);
  --pp-15-shell: oklch(0.27 0.04 285);
  --pp-15-ink: oklch(0.96 0.02 100);
  --pp-15-mut: oklch(0.72 0.04 285);
  --pp-15-cap: oklch(0.68 0.2 25);
  --pp-15-plinth: oklch(0.44 0.16 25);
  --pp-15-crt: oklch(0.85 0.2 145);
  font-family: ui-monospace,'SFMono-Regular',Menlo,Consolas,monospace;
  color: var(--pp-15-ink);
}

.pp-15__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 24px;
  padding: clamp(20px,5vw,56px);
  background: radial-gradient(70% 55% at 50% 12%,oklch(0.3 0.07 300/.7),transparent 72%);
}

.pp-15__cabinet {
  display: grid;
  justify-items: center;
  gap: 18px;
  width: min(100%,380px);
  padding: 26px 28px 30px;
  border: 4px solid oklch(0.16 0.03 285);
  border-radius: 20px;
  background: var(--pp-15-shell);
  box-shadow: inset 0 2px 0 oklch(1 0 0/.12),0 26px 60px oklch(0 0 0/.55);
}

.pp-15__marquee {
  font-size: 11px;
  letter-spacing: .22em;
  color: var(--pp-15-mut);
}

.pp-15__screen {
  position: relative;
  display: grid;
  place-items: center;
  width: 100%;
  height: 96px;
  border-radius: 8px;
  background: oklch(0.14 0.04 160);
  box-shadow: inset 0 0 24px oklch(0.3 0.14 150/.35),inset 0 0 0 2px oklch(0 0 0/.5);
  overflow: hidden;
}

.pp-15__scan {
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(to bottom,oklch(0 0 0/.35) 0 1px,transparent 1px 3px);
}

.pp-15__ready,
.pp-15__go {
  font-size: 22px;
  letter-spacing: .16em;
  color: var(--pp-15-crt);
  text-shadow: 0 0 12px currentColor;
}

.pp-15__go {
  display: none;
  animation: pp-15-blink 1s steps(2,end) infinite;
}

.pp-15-chk {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.pp-15__cap {
  display: grid;
  place-items: center;
  width: 104px;
  height: 104px;
  margin-top: 6px;
  border-radius: 22px;
  background: linear-gradient(180deg,color-mix(in oklch,var(--pp-15-cap) 88%,white),var(--pp-15-cap));
  cursor: pointer;
  box-shadow: 0 8px 0 var(--pp-15-plinth),0 10px 18px oklch(0 0 0/.45),inset 0 2px 0 oklch(1 0 0/.35);
  transition: translate .1s linear,box-shadow .1s linear;
}

.pp-15__cap:active {
  translate: 0 6px;
  box-shadow: 0 2px 0 var(--pp-15-plinth),0 3px 8px oklch(0 0 0/.45),inset 0 2px 0 oklch(1 0 0/.35);
}

.pp-15-chk:focus-visible+.pp-15__cap {
  outline: 3px dashed var(--pp-15-crt);
  outline-offset: 6px;
}

.pp-15__px {
  width: 46px;
  height: 46px;
  background: oklch(0.16 0.03 25);
  clip-path: polygon(0 0,25% 12.5%,25% 25%,50% 25%,50% 37.5%,75% 37.5%,75% 62.5%,50% 62.5%,50% 75%,25% 75%,25% 87.5%,0 100%);
  translate: 4px 0;
}

.pp-15__bars {
  display: none;
  gap: 10px;
  width: 44px;
  height: 46px;
}

.pp-15__bars i {
  flex: 1;
  background: oklch(0.16 0.03 25);
}

.pp-15-chk:checked+.pp-15__cap {
  translate: 0 6px;
  box-shadow: 0 2px 0 var(--pp-15-plinth),0 3px 8px oklch(0 0 0/.45),inset 0 2px 0 oklch(1 0 0/.35);
}

.pp-15-chk:checked+.pp-15__cap .pp-15__px {
  display: none;
}

.pp-15-chk:checked+.pp-15__cap .pp-15__bars {
  display: flex;
}

.pp-15__cabinet:has(.pp-15-chk:checked) .pp-15__ready {
  display: none;
}

.pp-15__cabinet:has(.pp-15-chk:checked) .pp-15__go {
  display: block;
}

@keyframes pp-15-blink {
  0%,
    50% {
    opacity: 1;
  }

  51%,
    100% {
    opacity: .25;
  }
}

.pp-15__hint {
  font-size: 10.5px;
  letter-spacing: .24em;
  color: var(--pp-15-mut);
}

.pp-15__chip {
  font-size: 11.5px;
  color: var(--pp-15-mut);
  padding: 7px 14px;
  border: 1px solid oklch(1 0 0/.14);
  border-radius: 99px;
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .pp-15__go {
    animation: none;
  }

  .pp-15 * {
    transition-duration: .01ms !important;
  }
}
```
