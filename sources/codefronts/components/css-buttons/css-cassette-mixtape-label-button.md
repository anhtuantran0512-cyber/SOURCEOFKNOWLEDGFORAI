---
source: "codefronts"
url: "https://codefronts.com/components/css-buttons/css-cassette-mixtape-label-button/"
title: "CSS Cassette Mixtape Label Button"
section: "components"
category: "css-buttons"
category_name: "CSS Buttons"
description: "A Type-II cassette with a hand-written label: both reels turn while you hover, the tape between them shifts from one hub to the other, and clicking flips the…"
has_js: "false"
---

Here's a working CSS Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Cassette Mixtape Label Button
Source: https://codefronts.com/components/css-buttons/css-cassette-mixtape-label-button/

A Type-II cassette with a hand-written label: both reels turn while you hover, the tape between them shifts from one hub to the other, and clicking flips the shell to side B. The reels are conic gradients, the spool teeth a repeating conic, the flip a :has(:checked) 3D rotation.
## HTML
```html
<div class="cb-37">
  <div class="cb-37__stage">
    <label class="cb-37__btn">
      <input type="checkbox" aria-label="Flip the cassette to side B">
      <span class="cb-37__shell" aria-hidden="true">
        <span class="cb-37__face cb-37__face--a">
          <span class="cb-37__window"><span class="cb-37__reel"></span><span class="cb-37__reel"></span></span>
          <span class="cb-37__label"><span class="cb-37__hand">summer, mostly</span><span class="cb-37__side">A</span></span>
        </span>
        <span class="cb-37__face cb-37__face--b">
          <span class="cb-37__window"><span class="cb-37__reel"></span><span class="cb-37__reel"></span></span>
          <span class="cb-37__label"><span class="cb-37__hand">the drive home</span><span class="cb-37__side">B</span></span>
        </span>
      </span>
    </label>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Caveat:wght@600;700&family=Archivo:wght@600;700&display=swap');

.cb-37 {
  --bg: #181a20;
  --shell: #2b2f38;
  --shell-hi: #3b414d;
  --paper: #f2ead6;
  --ink: #2c2419;
  --hub: #dfe3ea;
  --tape: #3a2a1c;
  --teeth: #9aa2b0;
  --accent: #ef6c4d;
  --hand: "Caveat",ui-rounded,cursive;
  --sans: "Archivo",ui-sans-serif,system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: radial-gradient(34rem 20rem at 50% 44%, #23262f, transparent 74%), var(--bg);
  font-family: var(--sans);
  perspective: 1000px;
}

@media (prefers-color-scheme: light) {
  .cb-37:not([data-theme="dark"]) {
    --bg: #20232a;
  }
}

.cb-37[data-theme="light"] {
  --bg: #20232a;
}

.cb-37,
.cb-37 *,
.cb-37 *::before,
.cb-37 *::after {
  box-sizing: border-box;
}

.cb-37__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,6vw,4rem);
  perspective: 1000px;
}

.cb-37__btn {
  position: relative;
  display: block;
  cursor: pointer;
  width: 19rem;
  height: 11.5rem;
  -webkit-tap-highlight-color: transparent;
}

.cb-37__btn input {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.cb-37__shell {
  position: relative;
  display: block;
  width: 100%;
  height: 100%;
  transform-style: preserve-3d;
  transition: rotate .9s cubic-bezier(.16,1,.3,1), translate .35s ease;
}

.cb-37__face {
  position: absolute;
  inset: 0;
  display: grid;
  grid-template-rows: auto 1fr;
  gap: .7rem;
  padding: .9rem;
  border-radius: .55rem;
  backface-visibility: hidden;
  background: linear-gradient(180deg, rgba(255,255,255,.12), transparent 34%), linear-gradient(165deg, var(--shell-hi), var(--shell));
  box-shadow: inset 0 1px 0 rgba(255,255,255,.2), inset 0 -2px 6px rgba(0,0,0,.5), 0 18px 30px -14px rgba(0,0,0,.8);
}

.cb-37__face--b {
  rotate: y 180deg;
}

.cb-37__window {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  padding: .55rem 1.4rem;
  border-radius: .3rem;
  background: linear-gradient(180deg, rgba(0,0,0,.5), rgba(0,0,0,.28));
  box-shadow: inset 0 0 0 1px rgba(255,255,255,.08);
}

.cb-37__reel {
  display: block;
  width: 3.1rem;
  height: 3.1rem;
  border-radius: 50%;
  background: repeating-conic-gradient(from 0deg, var(--teeth) 0 8deg, transparent 8deg 30deg), radial-gradient(circle, var(--hub) 30%, var(--tape) 33%, var(--tape) 80%, transparent 81%);
  box-shadow: inset 0 0 0 1px rgba(255,255,255,.12);
  animation: cb-37-spin 3.4s linear infinite;
  animation-play-state: paused;
}

.cb-37__reel:last-child {
  animation-duration: 4.6s;
}

@keyframes cb-37-spin {
  to {
    rotate: 1turn;
  }
}

.cb-37__label {
  position: relative;
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: .75rem;
  padding: .5rem .8rem;
  border-radius: .2rem;
  background: linear-gradient(180deg, color-mix(in oklab,var(--paper) 92%,white), var(--paper));
  box-shadow: inset 0 0 0 1px rgba(0,0,0,.12);
}

.cb-37__label::after {
  content: '';
  position: absolute;
  left: .8rem;
  right: 3rem;
  bottom: 1.05rem;
  height: 1px;
  background: color-mix(in oklab,var(--ink) 22%,transparent);
}

.cb-37__hand {
  position: relative;
  z-index: 2;
  font-family: var(--hand);
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--ink);
}

.cb-37__side {
  font-size: .75rem;
  font-weight: 700;
  letter-spacing: .14em;
  color: var(--accent);
  padding: .15rem .45rem;
  border-radius: .2rem;
  background: color-mix(in oklab,var(--accent) 16%,transparent);
}

.cb-37__btn:hover .cb-37__shell {
  translate: 0 -3px;
}

.cb-37__btn:is(:hover,:has(input:focus-visible)) .cb-37__reel {
  animation-play-state: running;
}

.cb-37__btn:has(input:focus-visible) .cb-37__shell {
  outline: 2px solid var(--accent);
  outline-offset: 6px;
  border-radius: .55rem;
}

.cb-37__btn:has(input:checked) .cb-37__shell {
  rotate: y 180deg;
}

.cb-37__btn:active .cb-37__shell {
  scale: .985;
}

@media (prefers-reduced-motion: reduce) {
  .cb-37__shell {
    transition: none;
  }

  .cb-37__reel {
    animation: none;
  }
}

@media (forced-colors: active) {
  .cb-37__face {
    background: ButtonFace;
    border: 1px solid ButtonText;
    box-shadow: none;
  }

  .cb-37__window {
    background: Canvas;
  }

  .cb-37__label {
    background: Canvas;
  }

  .cb-37__hand,
    .cb-37__side {
    color: CanvasText;
  }
}
```
