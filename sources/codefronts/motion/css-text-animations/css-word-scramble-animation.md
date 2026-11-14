---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-animations/css-word-scramble-animation/"
title: "CSS Text Unscramble Animation on Load"
section: "motion"
category: "css-text-animations"
category_name: "CSS Text Animations"
description: "Text decoding out of noise, twice: a 14-line JS scrambler that locks characters left-to-right out of a glyph storm, and a zero-JS slot-machine build where…"
has_js: "true"
---

Here's a working CSS Text Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Text Unscramble Animation on Load
Source: https://codefronts.com/motion/css-text-animations/css-word-scramble-animation/

Text decoding out of noise, twice: a 14-line JS scrambler that locks characters left-to-right out of a glyph storm, and a zero-JS slot-machine build where every letter rides a stepped reel of decoy glyphs into place.
## HTML
```html
<div class="cat-12-group">
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:[email protected]&display=swap" rel="stylesheet">
<section class="cat-12a" aria-label="Text unscramble decode effect">
  <div class="cat-12a__stage">
    <p class="cat-12a__status" aria-hidden="true"><i></i>DECRYPTING PAYLOAD</p>
    <p class="cat-12a__text" id="cat-12a-text" data-value="ACCESS GRANTED" aria-label="ACCESS GRANTED"></p>
    <button class="cat-12a__btn" id="cat-12a-btn" type="button">Run again</button>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:[email protected]&display=swap" rel="stylesheet">
<section class="cat-12b" aria-label="Slot reel decode effect">
  <div class="cat-12b__stage">
    <h1 class="cat-12b__word" aria-label="DECODED">
      <span class="cat-12b__slots" aria-hidden="true"><span class="cat-12b__slot" style="--i:0"><span class="cat-12b__reel"><i>#</i><i>X</i><i>9</i><i>D</i></span></span><span class="cat-12b__slot" style="--i:1"><span class="cat-12b__reel"><i>$</i><i>3</i><i>K</i><i>E</i></span></span><span class="cat-12b__slot" style="--i:2"><span class="cat-12b__reel"><i>%</i><i>W</i><i>7</i><i>C</i></span></span><span class="cat-12b__slot" style="--i:3"><span class="cat-12b__reel"><i>&amp;</i><i>2</i><i>Z</i><i>O</i></span></span><span class="cat-12b__slot" style="--i:4"><span class="cat-12b__reel"><i>+</i><i>Q</i><i>5</i><i>D</i></span></span><span class="cat-12b__slot" style="--i:5"><span class="cat-12b__reel"><i>?</i><i>8</i><i>V</i><i>E</i></span></span><span class="cat-12b__slot" style="--i:6"><span class="cat-12b__reel"><i>*</i><i>J</i><i>4</i><i>D</i></span></span></span>
    </h1>
    <p class="cat-12b__sub" aria-hidden="true">zero JS — each letter is a steps(3) reel of decoy glyphs</p>
  </div>
</section>
</div>
```
## CSS
```css
.cat-12-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.cat-12-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.cat-12a,
.cat-12a *,
.cat-12a *::before,
.cat-12a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-12a {
  --green: oklch(0.88 0.2 150);
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(100% 90% at 50% 10%,#0c1512,#060a08 70%);
  font-family: 'JetBrains Mono',ui-monospace,Menlo,monospace;
}

.cat-12a__stage {
  text-align: center;
  display: grid;
  gap: 22px;
  justify-items: center;
}

.cat-12a__status {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 10.5px;
  letter-spacing: .32em;
  color: rgba(150,220,180,.55);
}

.cat-12a__status i {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: var(--green);
  animation: cat-12a-blink 1s step-end infinite;
}

.cat-12a__text {
  font-size: clamp(26px,5.4vw,58px);
  font-weight: 800;
  letter-spacing: .12em;
  color: var(--green);
  text-shadow: 0 0 22px color-mix(in oklab,var(--green) 55%,transparent);
  min-height: 1.2em;
}

.cat-12a__btn {
  font: inherit;
  font-size: 11px;
  letter-spacing: .22em;
  text-transform: uppercase;
  color: rgba(150,220,180,.7);
  background: transparent;
  border: 1px solid rgba(150,220,180,.3);
  border-radius: 999px;
  padding: 9px 20px;
  cursor: pointer;
  transition: border-color .25s,color .25s;
}

.cat-12a__btn:hover {
  border-color: var(--green);
  color: var(--green);
}

.cat-12a__btn:focus-visible {
  outline: 2px solid var(--green);
  outline-offset: 3px;
}

@keyframes cat-12a-blink {
  50% {
    opacity: .25;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cat-12a__status i {
    animation: none;
  }
}

.cat-12b,
.cat-12b *,
.cat-12b *::before,
.cat-12b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-12b {
  --cyan: oklch(0.86 0.14 200);
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #080d14;
  font-family: 'JetBrains Mono',ui-monospace,Menlo,monospace;
}

.cat-12b__stage {
  text-align: center;
}

.cat-12b__word {
  font-size: clamp(40px,8vw,96px);
  font-weight: 800;
  color: var(--cyan);
}

.cat-12b__slots {
  display: inline-flex;
  gap: .06em;
}

.cat-12b__slot {
  display: inline-block;
  height: 1.05em;
  line-height: 1.05;
  overflow: hidden;
}

.cat-12b__reel {
  display: flex;
  flex-direction: column;
  animation: cat-12b-drop .9s steps(3) calc(var(--i)*100ms + .35s) forwards;
}

.cat-12b__reel i {
  font-style: normal;
  height: 1.05em;
}

.cat-12b__reel i:not(:last-child) {
  opacity: .45;
}

.cat-12b__sub {
  margin-top: 20px;
  font-size: 11px;
  letter-spacing: .16em;
  color: rgba(160,200,230,.4);
}

@keyframes cat-12b-drop {
  to {
    transform: translateY(-3.15em);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cat-12b__reel {
    animation-duration: .01s;
    animation-delay: 0s;
  }
}
```

## JavaScript
```js
(() => {
  const el = document.querySelector('#cat-12a-text'); if (!el) return;
  const FINAL = el.dataset.value, POOL = '!<>-_/[]{}=+*^?#@$%&';
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  let timer;
  const run = () => {
    if (reduce) { el.textContent = FINAL; return; }
    clearInterval(timer); let frame = 0;
    timer = setInterval(() => {
      const done = Math.floor(frame / 2);
      el.textContent = FINAL.split('').map((c, i) =>
        c === ' ' ? ' ' : i < done ? c : POOL[Math.floor(Math.random() * POOL.length)]).join('');
      if (done >= FINAL.length) clearInterval(timer);
      frame++;
    }, 34);
  };
  run();
  const btn = document.querySelector('#cat-12a-btn');
  if (btn) btn.addEventListener('click', run);
})();

/* No JavaScript — every slot is a 1em overflow:hidden window over a 4-glyph column; steps(3) hops it down one glyph at a time until the real letter parks. */
```
