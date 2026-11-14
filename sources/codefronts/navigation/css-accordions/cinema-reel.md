---
source: "codefronts"
url: "https://codefronts.com/navigation/css-accordions/cinema-reel/"
title: "Cinema Reel Horizontal Accordion — Dark Letterboxed Showcase"
section: "navigation"
category: "css-accordions"
category_name: "CSS Accordions — Vertical & Horizontal"
description: "A film-strip in the dark: near-black panels separated by sprocket-hole perforation rails, each expanding into a letterboxed 'frame' with a title card that…"
has_js: "false"
---

Here's a working CSS Accordions — Vertical & Horizontal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Cinema Reel Horizontal Accordion — Dark Letterboxed Showcase
Source: https://codefronts.com/navigation/css-accordions/cinema-reel/

A film-strip in the dark: near-black panels separated by sprocket-hole perforation rails, each expanding into a letterboxed 'frame' with a title card that tracks in like credits — wide letter-spacing easing to normal. Built for film festivals, video portfolios and anything that wants the lights turned off.
## HTML
```html
<section class="acc-21" aria-label="Cinema reel horizontal accordion demo">
  <div class="acc-21__strip" role="group" aria-label="Festival lineup">
    <div class="acc-21__panel" style="--tint:oklch(0.5 0.14 250 / .25)">
      <input type="radio" name="acc-21" id="acc-21-a" checked>
      <label class="acc-21__face" for="acc-21-a"><span class="acc-21__idx">I</span>
        <span class="acc-21__frame"><b class="acc-21__name">STILL WATER</b><i class="acc-21__slug">dir. E. Almqvist · 96 min · sweden</i><p class="acc-21__log">A ferry pilot on her final crossing discovers a passenger who never boarded.</p></span>
      </label>
    </div>
    <div class="acc-21__panel" style="--tint:oklch(0.5 0.16 25 / .25)">
      <input type="radio" name="acc-21" id="acc-21-b">
      <label class="acc-21__face" for="acc-21-b"><span class="acc-21__idx">II</span>
        <span class="acc-21__frame"><b class="acc-21__name">RED HARVEST</b><i class="acc-21__slug">dir. T. Okonkwo · 121 min · nigeria</i><p class="acc-21__log">Three brothers, one orchard, and the season that will decide who keeps it.</p></span>
      </label>
    </div>
    <div class="acc-21__panel" style="--tint:oklch(0.55 0.12 140 / .22)">
      <input type="radio" name="acc-21" id="acc-21-c">
      <label class="acc-21__face" for="acc-21-c"><span class="acc-21__idx">III</span>
        <span class="acc-21__frame"><b class="acc-21__name">GREENHOUSE</b><i class="acc-21__slug">dir. M. Duval · 84 min · canada</i><p class="acc-21__log">A botanist live-streams her last experiment; the plants start answering back.</p></span>
      </label>
    </div>
  </div>
</section>
```
## CSS
```css
.acc-21,
.acc-21 *,
.acc-21 *::before,
.acc-21 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.acc-21 {
  --holes: repeating-linear-gradient(0deg,transparent 0 10px,#000 10px 22px);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #0a0a0c;
  padding: 44px 24px;
}

.acc-21__strip {
  display: flex;
  width: min(820px,100%);
  height: 380px;
  background: #17171b;
  padding: 0 22px;
  position: relative;
  border-radius: 8px;
}

.acc-21__strip::before,
.acc-21__strip::after {
  content: "";
  position: absolute;
  top: 12px;
  bottom: 12px;
  width: 12px;
  background: var(--holes);
  border-radius: 3px;
}

.acc-21__strip::before {
  left: 5px;
}

.acc-21__strip::after {
  right: 5px;
}

.acc-21__panel {
  display: flex;
  flex-grow: 1;
  flex-basis: 0;
  min-width: 64px;
  position: relative;
  transition: flex-grow .55s cubic-bezier(.4,0,.2,1);
}

.acc-21__panel + .acc-21__panel::before {
  content: "";
  position: absolute;
  left: -6px;
  top: 12px;
  bottom: 12px;
  width: 12px;
  background: var(--holes);
  border-radius: 3px;
  z-index: 2;
}

.acc-21__panel:has(input:checked) {
  flex-grow: 6;
}

.acc-21__panel input {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.acc-21__face {
  position: relative;
  flex: 1;
  display: block;
  cursor: pointer;
  overflow: hidden;
  background: #0f0f13 radial-gradient(70% 60% at 50% 40%,var(--tint),transparent 75%);
  margin: 12px 8px;
  border-radius: 4px;
  box-shadow: inset 0 0 0 1px rgba(255,255,255,.06);
  transition: box-shadow .3s;
}

.acc-21__face:hover {
  box-shadow: inset 0 0 0 1px rgba(255,255,255,.16);
}

.acc-21__idx {
  position: absolute;
  inset: 0;
  display: grid;
  place-content: center;
  font-family: Georgia,serif;
  font-size: 26px;
  color: rgba(240,236,225,.4);
  transition: opacity .25s;
}

.acc-21__panel:has(input:checked) .acc-21__idx {
  opacity: 0;
}

.acc-21__frame {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 12px;
  text-align: center;
  padding: 30px;
  opacity: 0;
  transition: opacity .4s .2s;
  box-shadow: inset 0 14px 0 #000,inset 0 -14px 0 #000;
}

.acc-21__panel:has(input:checked) .acc-21__frame {
  opacity: 1;
}

.acc-21__name {
  font-size: clamp(22px,3.4vw,34px);
  font-weight: 800;
  color: rgba(240,236,225,.92);
  letter-spacing: .5em;
  text-indent: .5em;
  transition: letter-spacing .8s cubic-bezier(.2,.7,.2,1) .2s,text-indent .8s cubic-bezier(.2,.7,.2,1) .2s;
  white-space: nowrap;
}

.acc-21__panel:has(input:checked) .acc-21__name {
  letter-spacing: .06em;
  text-indent: .06em;
}

.acc-21__slug {
  font-style: normal;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: rgba(240,236,225,.55);
}

.acc-21__log {
  font-size: 14px;
  line-height: 1.6;
  color: rgba(240,236,225,.75);
  max-width: 44ch;
}

.acc-21__panel:has(input:focus-visible) .acc-21__face {
  outline: 3px solid rgba(240,236,225,.9);
  outline-offset: 2px;
}

@media (max-width: 620px) {
  .acc-21__strip {
    flex-direction: column;
    height: auto;
    padding: 22px 0;
  }

  .acc-21__strip::before,
    .acc-21__strip::after {
    top: 5px;
    bottom: auto;
    left: 12px;
    right: 12px;
    width: auto;
    height: 12px;
    background: repeating-linear-gradient(90deg,transparent 0 10px,#000 10px 22px);
  }

  .acc-21__strip::after {
    top: auto;
    bottom: 5px;
  }

  .acc-21__panel {
    min-height: 64px;
  }

  .acc-21__panel:has(input:checked) {
    min-height: 280px;
  }

  .acc-21__panel + .acc-21__panel::before {
    display: none;
  }

  .acc-21__name {
    white-space: normal;
  }
}

@media (prefers-reduced-motion: reduce) {
  .acc-21__panel,
    .acc-21__name,
    .acc-21__frame,
    .acc-21__idx {
    transition: none;
  }

  .acc-21__name {
    letter-spacing: .06em;
    text-indent: .06em;
  }
}
```

## JavaScript
```js
/* No JavaScript — sprocket rails are repeating-linear-gradients, letterbox bars are inset box-shadows, and the title's cinematic track-in is a letter-spacing transition fired by :has(input:checked). */
```
