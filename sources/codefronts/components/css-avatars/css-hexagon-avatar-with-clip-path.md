---
source: "codefronts"
url: "https://codefronts.com/components/css-avatars/css-hexagon-avatar-with-clip-path/"
title: "CSS Hexagon Avatar with clip-path"
section: "components"
category: "css-avatars"
category_name: "CSS Avatars"
description: "A gaming/esports roster where every face is a clip-path hexagon — and a working answer to the bug everyone hits: clip-path clips pseudo-elements and shadows…"
has_js: "false"
---

Here's a working CSS Avatar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Hexagon Avatar with clip-path
Source: https://codefronts.com/components/css-avatars/css-hexagon-avatar-with-clip-path/

A gaming/esports roster where every face is a clip-path hexagon — and a working answer to the bug everyone hits: clip-path clips pseudo-elements and shadows too, so the rank badge and status dot live on an unclipped wrapper, never on the clipped element. The hex ring is a second, slightly larger clipped layer behind the first, which is the only way to outline a clipped shape.
## HTML
```html
<div class="av-05">
  <input class="av-05__sr" type="checkbox" id="av-05-dark">
  <label class="av-05__theme" for="av-05-dark">
    <svg class="av-05__i av-05__i--moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.3A8.4 8.4 0 0 1 9.7 3.5a8.5 8.5 0 1 0 10.8 10.8Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="av-05__i av-05__i--sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.1" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.7 5.7l1.4 1.4M16.9 16.9l1.4 1.4M18.3 5.7l-1.4 1.4M7.1 16.9l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <span class="av-05__vh">Dark theme</span>
  </label>

  <div class="av-05__stage">
    <section class="av-05__wrap" aria-labelledby="av-05-h">
      <header class="av-05__head">
        <p class="av-05__eyebrow">Roster · Valorant · Div 1</p>
        <h2 class="av-05__h" id="av-05-h">NORTHWIND</h2>
        <p class="av-05__sub">Starting five. Badges sit on the wrapper, never on the clipped photo.</p>
      </header>

      <ul class="av-05__roster">
        <li class="av-05__cell">
          <span class="av-05__frame">
            <span class="av-05__ring" aria-hidden="true"></span>
            <img class="av-05__photo" src="https://images.unsplash.com/photo-1568602471122-7832951cc4c5?w=200&auto=format&fit=facearea&facepad=2.5" alt="Ryan Kowalski" width="200" height="200" loading="lazy" decoding="async">
            <span class="av-05__rank">IGL</span>
            <span class="av-05__dot av-05__dot--live"><span class="av-05__vh">In match</span></span>
          </span>
          <span class="av-05__id"><span class="av-05__tag">K0WAL</span><span class="av-05__real">Ryan Kowalski</span></span>
        </li>
        <li class="av-05__cell av-05__cell--offset">
          <span class="av-05__frame">
            <span class="av-05__ring" aria-hidden="true"></span>
            <img class="av-05__photo" src="https://images.unsplash.com/photo-1611432579699-484f7990b127?w=200&auto=format&fit=facearea&facepad=2.5" alt="Ben Achterberg" width="200" height="200" loading="lazy" decoding="async">
            <span class="av-05__rank">DUEL</span>
            <span class="av-05__dot av-05__dot--live"><span class="av-05__vh">In match</span></span>
          </span>
          <span class="av-05__id"><span class="av-05__tag">ACHT</span><span class="av-05__real">Ben Achterberg</span></span>
        </li>
        <li class="av-05__cell">
          <span class="av-05__frame">
            <span class="av-05__ring" aria-hidden="true"></span>
            <img class="av-05__photo" src="https://images.unsplash.com/photo-1595152452543-e5fc28ebc2b8?w=200&auto=format&fit=facearea&facepad=2.5" alt="Ines Duarte" width="200" height="200" loading="lazy" decoding="async">
            <span class="av-05__rank">SENT</span>
            <span class="av-05__dot av-05__dot--idle"><span class="av-05__vh">Idle in lobby</span></span>
          </span>
          <span class="av-05__id"><span class="av-05__tag">INES</span><span class="av-05__real">Ines Duarte</span></span>
        </li>
        <li class="av-05__cell av-05__cell--offset">
          <span class="av-05__frame">
            <span class="av-05__ring" aria-hidden="true"></span>
            <img class="av-05__photo" src="https://images.unsplash.com/photo-1546525848-3ce03ca516f6?w=200&auto=format&fit=facearea&facepad=2.5" alt="Chris Donnelly" width="200" height="200" loading="lazy" decoding="async">
            <span class="av-05__rank">CTRL</span>
            <span class="av-05__dot av-05__dot--live"><span class="av-05__vh">In match</span></span>
          </span>
          <span class="av-05__id"><span class="av-05__tag">DONN</span><span class="av-05__real">Chris Donnelly</span></span>
        </li>
        <li class="av-05__cell">
          <span class="av-05__frame">
            <span class="av-05__ring" aria-hidden="true"></span>
            <img class="av-05__photo" src="https://images.unsplash.com/photo-1552058544-f2b08422138a?w=200&auto=format&fit=facearea&facepad=2.5" alt="Leo Mbeki" width="200" height="200" loading="lazy" decoding="async">
            <span class="av-05__rank">INIT</span>
            <span class="av-05__dot av-05__dot--off"><span class="av-05__vh">Offline</span></span>
          </span>
          <span class="av-05__id"><span class="av-05__tag">MBK</span><span class="av-05__real">Leo Mbeki</span></span>
        </li>
      </ul>

      <p class="av-05__foot"><code>clip-path</code> also clips shadows, outlines and <code>::after</code> — hoist decorations to the wrapper.</p>
    </section>
  </div>
</div>
```
## CSS
```css
@supports (color: oklch(50% .1 250)) {
  .av-05 {
    --page: oklch(96% .006 265);
    --panel: oklch(100% 0 0);
    --panel-2: oklch(94.5% .008 265);
    --ink: oklch(19% .024 265);
    --muted: oklch(52% .022 265);
    --line: oklch(90% .01 265);
    --accent: oklch(60% .21 12);
    --c1: oklch(64% .22 12);
    --c2: oklch(74% .18 60);
    --live: oklch(72% .19 150);
    --idle: oklch(80% .16 85);
  }
}

.av-05 {
  --page: #f2f3f6;
  --panel: #ffffff;
  --panel-2: #eaecf1;
  --ink: #0e1117;
  --muted: #5c6371;
  --line: #e0e3ea;
  --accent: #e11d48;
  --c1: #f43f5e;
  --c2: #fb923c;
  --live: #22c55e;
  --idle: #f59e0b;
  --glass: rgba(255,255,255,.68);
  --shadow: 0 1px 2px rgba(14,17,23,.05), 0 18px 40px -22px rgba(14,17,23,.35);
  --r: 18px;
  --size: clamp(4.5rem,12vw,6.5rem);
  --hex: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);
  width: 100%;
  inline-size: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui,-apple-system,"Segoe UI",sans-serif;
  -webkit-font-smoothing: antialiased;
}

.av-05 *,
.av-05 *::before,
.av-05 *::after {
  box-sizing: border-box;
}

.av-05__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.av-05__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  margin: 0;
  pointer-events: none;
}

.av-05__theme {
  position: absolute;
  inset-block-start: clamp(.85rem,2.2vw,1.5rem);
  inset-inline-end: clamp(.85rem,2.2vw,1.5rem);
  z-index: 20;
  display: grid;
  place-items: center;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  border-radius: 999px;
  border: 1px solid var(--line);
  background: var(--glass);
  color: var(--ink);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  cursor: pointer;
  transition: translate .2s ease;
}

.av-05__theme::after {
  content: "";
  position: absolute;
  inset: -.4rem;
  border-radius: inherit;
}

.av-05__theme:hover {
  translate: 0 -1px;
}

.av-05__i {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.av-05__i--sun {
  display: none;
}

.av-05__sr:focus-visible + .av-05__theme {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.av-05__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
}

.av-05__wrap {
  inline-size: min(60rem,100%);
  display: flex;
  flex-direction: column;
  gap: clamp(1.25rem,3vw,2rem);
}

.av-05__head {
  display: flex;
  flex-direction: column;
  gap: .35rem;
  padding-inline-end: 3.5rem;
}

.av-05__eyebrow {
  margin: 0;
  font-size: .7rem;
  font-weight: 600;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--accent);
}

.av-05__h {
  margin: 0;
  font-size: clamp(1.9rem,5.5vw,3.1rem);
  font-weight: 800;
  letter-spacing: -.04em;
  line-height: .98;
}

.av-05__sub {
  margin: 0;
  max-inline-size: 36rem;
  font-size: .95rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.av-05__roster {
  list-style: none;
  margin: 0;
  padding: clamp(1.5rem,4vw,2.5rem) clamp(1rem,3vw,2rem) clamp(2rem,5vw,3rem);
  display: grid;
  gap: clamp(1rem,2.5vw,1.75rem);
  grid-template-columns: repeat(auto-fit,minmax(7.5rem,1fr));
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: var(--r);
  box-shadow: var(--shadow);
}

.av-05__cell {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: .7rem;
}

@media (min-width: 44rem) {
  .av-05__cell--offset {
    margin-block-start: 2.25rem;
  }
}

.av-05__frame {
  position: relative;
  display: block;
  inline-size: var(--size);
  aspect-ratio: 1;
  transition: translate .25s cubic-bezier(.2,.7,.3,1);
}

.av-05__cell:hover .av-05__frame {
  translate: 0 -5px;
}

.av-05__ring {
  position: absolute;
  inset: -3px;
  clip-path: var(--hex);
  background: linear-gradient(160deg, var(--c1), var(--c2));
  z-index: 0;
}

.av-05__photo {
  position: relative;
  z-index: 1;
  display: block;
  inline-size: 100%;
  block-size: 100%;
  aspect-ratio: 1;
  clip-path: var(--hex);
  object-fit: cover;
  object-position: center top;
  background: var(--panel-2);
  filter: saturate(.9) contrast(1.03);
  transition: filter .25s ease;
}

.av-05__cell:hover .av-05__photo {
  filter: none;
}

.av-05__rank {
  position: absolute;
  z-index: 2;
  inset-block-end: -.35rem;
  inset-inline-start: 50%;
  translate: -50% 0;
  padding: .16rem .45rem;
  border-radius: 6px;
  background: var(--ink);
  color: var(--panel);
  font-size: .6rem;
  font-weight: 700;
  letter-spacing: .1em;
}

.av-05__dot {
  position: absolute;
  z-index: 2;
  inset-block-start: .15rem;
  inset-inline-end: -.1rem;
  inline-size: .85rem;
  block-size: .85rem;
  border-radius: 50%;
  background: var(--live);
  box-shadow: 0 0 0 3px var(--panel);
}

.av-05__dot--live {
  background: var(--live);
}

.av-05__dot--idle {
  background: var(--idle);
  box-shadow: 0 0 0 3px var(--panel), inset 0 0 0 .18rem var(--panel);
}

.av-05__dot--off {
  background: var(--panel);
  box-shadow: 0 0 0 3px var(--panel), inset 0 0 0 .18rem var(--muted);
}

.av-05__id {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: .05rem;
  text-align: center;
}

.av-05__tag {
  font-size: .9rem;
  font-weight: 750;
  letter-spacing: .02em;
}

.av-05__real {
  font-size: .74rem;
  color: var(--muted);
}

.av-05__foot {
  margin: 0;
  font-size: .82rem;
  color: var(--muted);
  text-wrap: pretty;
}

.av-05__foot code {
  font-family: ui-monospace,SFMono-Regular,Menlo,monospace;
  font-size: .78rem;
  padding: .1rem .3rem;
  border-radius: 5px;
  background: var(--panel-2);
}

.av-05:has(#av-05-dark:checked) {
  --page: #08090c;
  --panel: #12141a;
  --panel-2: #1b1e26;
  --ink: #f2f4f9;
  --muted: #98a0b0;
  --line: #252932;
  --glass: rgba(255,255,255,.07);
  --shadow: 0 1px 2px rgba(0,0,0,.6), 0 22px 46px -24px rgba(0,0,0,.9);
}

.av-05:has(#av-05-dark:checked) .av-05__i--moon {
  display: none;
}

.av-05:has(#av-05-dark:checked) .av-05__i--sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .av-05:not(:has(#av-05-dark:checked)) {
    --page: #08090c;
    --panel: #12141a;
    --panel-2: #1b1e26;
    --ink: #f2f4f9;
    --muted: #98a0b0;
    --line: #252932;
    --glass: rgba(255,255,255,.07);
    --shadow: 0 1px 2px rgba(0,0,0,.6), 0 22px 46px -24px rgba(0,0,0,.9);
  }

  .av-05:not(:has(#av-05-dark:checked)) .av-05__i--moon {
    display: none;
  }

  .av-05:not(:has(#av-05-dark:checked)) .av-05__i--sun {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .av-05 *,
    .av-05 *::before,
    .av-05 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .av-05__ring {
    background: CanvasText;
  }

  .av-05__rank {
    background: Canvas;
    color: CanvasText;
    border: 1px solid CanvasText;
  }

  .av-05__roster,
    .av-05__theme {
    border-color: CanvasText;
  }
}
```
