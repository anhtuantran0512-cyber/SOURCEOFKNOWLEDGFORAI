---
source: "codefronts"
url: "https://codefronts.com/snippets/css-chat-bubbles/css-comic-book-speech-bubble/"
title: "CSS Comic Book Speech Bubble"
section: "snippets"
category: "css-chat-bubbles"
category_name: "CSS Chat Bubbles"
description: "A four-panel comic strip with the whole balloon vocabulary drawn in CSS: a rounded speech balloon, a starburst shout cut with a 24-point clip-path, a dashed…"
has_js: "false"
---

Here's a working CSS Chat Bubble from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Comic Book Speech Bubble
Source: https://codefronts.com/snippets/css-chat-bubbles/css-comic-book-speech-bubble/

A four-panel comic strip with the whole balloon vocabulary drawn in CSS: a rounded speech balloon, a starburst shout cut with a 24-point clip-path, a dashed whisper, and a narration caption. Halftone dots come from a two-layer radial-gradient, panel art is duotoned with filter + mix-blend-mode, and three ink palettes swap with a pure-CSS control.
## HTML
```html
<div class="cb-12">
  <input class="cb-12__sr" type="radio" name="cb-12-ink" id="cb-12-ink" checked>
  <input class="cb-12__sr" type="radio" name="cb-12-ink" id="cb-12-pulp">
  <input class="cb-12__sr" type="radio" name="cb-12-ink" id="cb-12-riso">

  <div class="cb-12__stage">
    <div class="cb-12__strip">
      <figure class="cb-12__panel">
        <img src="https://images.unsplash.com/photo-1449824913935-59a10b8d2000?auto=format&fit=crop&w=680&q=70" width="680" height="520" alt="An empty city street at dusk" loading="lazy" decoding="async">
        <p class="cb-12__balloon">The whole city went quiet at once.</p>
      </figure>

      <figure class="cb-12__panel">
        <img src="https://images.unsplash.com/photo-1516450360452-9312f5e86fc7?auto=format&fit=crop&w=680&q=70" width="680" height="520" alt="Silhouetted figures under hard shafts of light" loading="lazy" decoding="async">
        <p class="cb-12__shout"><span>Not<br>again!</span></p>
      </figure>

      <figure class="cb-12__panel">
        <img src="https://images.unsplash.com/photo-1509023464722-18d996393ca8?auto=format&fit=crop&w=680&q=70" width="680" height="520" alt="A lone peak across still water at first light" loading="lazy" decoding="async">
        <p class="cb-12__whisper">don't look up yet…</p>
      </figure>

      <figure class="cb-12__panel">
        <img src="https://images.unsplash.com/photo-1419242902214-272b3f66ee7a?auto=format&fit=crop&w=680&q=70" width="680" height="520" alt="A wide field of stars above a dark treeline" loading="lazy" decoding="async">
        <p class="cb-12__caption">Meanwhile, four hundred miles above the argument…</p>
      </figure>
    </div>

    <div class="cb-12__switch" role="radiogroup" aria-label="Ink palette">
      <label class="cb-12__chip" for="cb-12-ink">Ink</label>
      <label class="cb-12__chip" for="cb-12-pulp">Pulp</label>
      <label class="cb-12__chip" for="cb-12-riso">Riso</label>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Bangers&family=Archivo:wght@500;600;700&display=swap');

.cb-12 {
  --ink: #12100e;
  --paper: #f4ead6;
  --pop: #ffd23f;
  --pop-2: #ff4b3e;
  --ink-soft: rgba(18,16,14,.14);
  --display: "Bangers",Impact,"Haettenschweiler","Arial Narrow Bold",sans-serif;
  --sans: "Archivo",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3rem);
  background-color: var(--paper);
  background-image: radial-gradient(circle, var(--ink-soft) 1.1px, transparent 1.2px), radial-gradient(circle, var(--ink-soft) .8px, transparent .9px);
  background-size: 9px 9px, 9px 9px;
  background-position: 0 0, 4.5px 4.5px;
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.cb-12,
.cb-12 *,
.cb-12 *::before,
.cb-12 *::after {
  box-sizing: border-box;
}

.cb-12__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  opacity: 0;
}

.cb-12__stage {
  inline-size: min(100%,58rem);
  display: grid;
  gap: clamp(1.25rem,3vw,2rem);
  justify-items: center;
}

.cb-12__strip {
  inline-size: 100%;
  display: grid;
  gap: clamp(.75rem,2vw,1.15rem);
  grid-template-columns: repeat(2,minmax(0,1fr));
}

@media (min-width: 64rem) {
  .cb-12__strip {
    grid-template-columns: repeat(4,minmax(0,1fr));
  }
}

@media (max-width: 26rem) {
  .cb-12__strip {
    grid-template-columns: minmax(0,1fr);
  }
}
/* ── panel ── */

.cb-12__panel {
  position: relative;
  margin: 0;
  overflow: hidden;
  isolation: isolate;
  aspect-ratio: 5/4;
  border: 3px solid var(--ink);
  border-radius: .35rem;
  background: var(--pop);
  box-shadow: 6px 6px 0 var(--ink);
  transition: transform .32s cubic-bezier(.16,1,.3,1), box-shadow .32s;
}

.cb-12__panel:nth-child(2) {
  rotate: -.8deg;
}

.cb-12__panel:nth-child(3) {
  rotate: .7deg;
}

.cb-12__panel:hover {
  transform: translate(-3px,-4px);
  box-shadow: 10px 11px 0 var(--ink);
}

.cb-12__panel img {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  object-fit: cover;
  filter: grayscale(1) contrast(1.45) brightness(1.05);
  mix-blend-mode: luminosity;
}
/* ── 1 · speech balloon ── */

.cb-12__balloon {
  position: absolute;
  inset: auto 1rem 1.5rem 1rem;
  z-index: 2;
  margin: 0;
  padding: .7rem .95rem;
  border: 3px solid var(--ink);
  border-radius: 1.1rem;
  background: #fff;
  color: var(--ink);
  font-size: clamp(.9rem,2.2vw,1rem);
  font-weight: 600;
  line-height: 1.35;
  text-wrap: pretty;
  box-shadow: 4px 4px 0 var(--ink);
}

.cb-12__balloon::before,
.cb-12__balloon::after {
  content: '';
  position: absolute;
  inline-size: 0;
  block-size: 0;
  inset-block-start: 100%;
  inset-inline-start: 1.9rem;
}

.cb-12__balloon::before {
  border-inline: 12px solid transparent;
  border-block-start: 20px solid var(--ink);
}

.cb-12__balloon::after {
  inset-inline-start: 2.1rem;
  border-inline: 8px solid transparent;
  border-block-start: 14px solid #fff;
}
/* ── 2 · starburst shout ── */

.cb-12__shout {
  position: absolute;
  inset: 50% auto auto 50%;
  translate: -50% -50%;
  z-index: 2;
  margin: 0;
  inline-size: min(84%,15rem);
  aspect-ratio: 1;
  display: grid;
  place-items: center;
  background: var(--pop-2);
  color: #fff;
  clip-path: polygon(50% 0%,58% 14%,68% 4%,71% 19%,84% 12%,82% 27%,97% 26%,89% 38%,100% 47%,88% 55%,97% 66%,83% 68%,87% 82%,73% 79%,71% 94%,60% 85%,50% 100%,40% 85%,29% 94%,27% 79%,13% 82%,17% 68%,3% 66%,12% 55%,0% 47%,11% 38%,3% 26%,18% 27%,16% 12%,29% 19%,32% 4%,42% 14%);
  animation: cb-12-throb 3.4s cubic-bezier(.16,1,.3,1) infinite;
}

.cb-12__shout::before {
  content: '';
  position: absolute;
  inset: -5px;
  z-index: -1;
  background: var(--ink);
  clip-path: inherit;
}

.cb-12__shout span {
  font-family: var(--display);
  font-size: clamp(1.5rem,6vw,2.35rem);
  line-height: .95;
  letter-spacing: .03em;
  text-transform: uppercase;
  text-align: center;
  text-wrap: balance;
  paint-order: stroke fill;
}

@keyframes cb-12-throb {
  0%,
    88%,
    100% {
    scale: 1;
    rotate: -2deg;
  }

  92% {
    scale: 1.05;
    rotate: 1deg;
  }
}
/* ── 3 · dashed whisper ── */

.cb-12__whisper {
  position: absolute;
  inset: auto 1.15rem 1.6rem auto;
  z-index: 2;
  margin: 0;
  max-inline-size: 70%;
  padding: .6rem .9rem;
  border: 2.5px dashed var(--ink);
  border-radius: 1.4rem;
  background: color-mix(in oklab,#fff 88%,var(--pop));
  font-size: clamp(.85rem,2vw,.95rem);
  font-weight: 500;
  font-style: italic;
  line-height: 1.3;
}

.cb-12__whisper::after {
  content: '';
  position: absolute;
  inset-block-start: 100%;
  inset-inline-end: 1.6rem;
  inline-size: .55rem;
  block-size: .55rem;
  border-radius: 50%;
  border: 2.5px dashed var(--ink);
  background: color-mix(in oklab,#fff 88%,var(--pop));
  translate: 0 .35rem;
}
/* ── 4 · narration caption ── */

.cb-12__caption {
  position: absolute;
  inset: .9rem .9rem auto .9rem;
  z-index: 2;
  margin: 0;
  padding: .6rem .85rem;
  border: 3px solid var(--ink);
  background: var(--pop);
  color: var(--ink);
  font-size: clamp(.8rem,1.9vw,.9rem);
  font-weight: 700;
  line-height: 1.3;
  letter-spacing: .01em;
  text-transform: uppercase;
  text-wrap: balance;
  box-shadow: 4px 4px 0 var(--ink);
}
/* ── palettes ── */

.cb-12:has(#cb-12-pulp:checked) {
  --ink: #1a1210;
  --paper: #e8d9b5;
  --pop: #f2884b;
  --pop-2: #c62828;
  --ink-soft: rgba(26,18,16,.18);
}

.cb-12:has(#cb-12-riso:checked) {
  --ink: #141a2e;
  --paper: #eef1f7;
  --pop: #7cc6ff;
  --pop-2: #ff3d8b;
  --ink-soft: rgba(20,26,46,.13);
}
/* ── switch ── */

.cb-12__switch {
  display: flex;
  flex-wrap: wrap;
  gap: .4rem;
  padding: .35rem;
  justify-content: center;
  border: 3px solid var(--ink);
  border-radius: .8rem;
  background: #fff;
  box-shadow: 5px 5px 0 var(--ink);
}

.cb-12__chip {
  min-block-size: 44px;
  display: grid;
  place-items: center;
  padding: .45rem 1.15rem;
  cursor: pointer;
  border-radius: .5rem;
  color: var(--ink);
  font-size: .85rem;
  font-weight: 700;
  letter-spacing: .05em;
  text-transform: uppercase;
  transition: background .18s, color .18s;
}

.cb-12__chip:hover {
  background: var(--pop);
}

#cb-12-ink:checked ~ .cb-12__stage .cb-12__chip[for="cb-12-ink"],
#cb-12-pulp:checked ~ .cb-12__stage .cb-12__chip[for="cb-12-pulp"],
#cb-12-riso:checked ~ .cb-12__stage .cb-12__chip[for="cb-12-riso"] {
  background: var(--ink);
  color: var(--paper);
}

#cb-12-ink:focus-visible ~ .cb-12__stage .cb-12__chip[for="cb-12-ink"],
#cb-12-pulp:focus-visible ~ .cb-12__stage .cb-12__chip[for="cb-12-pulp"],
#cb-12-riso:focus-visible ~ .cb-12__stage .cb-12__chip[for="cb-12-riso"] {
  outline: 3px solid var(--pop-2);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .cb-12 *,
    .cb-12 *::before,
    .cb-12 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .cb-12__panel,
    .cb-12__balloon,
    .cb-12__caption,
    .cb-12__whisper {
    border: 2px solid CanvasText;
    box-shadow: none;
  }

  .cb-12__panel img {
    mix-blend-mode: normal;
    filter: none;
  }
}
```
