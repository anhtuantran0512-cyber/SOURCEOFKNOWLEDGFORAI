---
source: "codefronts"
url: "https://codefronts.com/components/css-avatars/css-team-avatar-row-with-hover-spread/"
title: "CSS Team Avatar Row with Hover Spread"
section: "components"
category: "css-avatars"
category_name: "CSS Avatars"
description: "An overlapped row that fans open when you point at it, so a tight facepile becomes a legible team list without a click."
has_js: "false"
---

Here's a working CSS Avatar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Team Avatar Row with Hover Spread
Source: https://codefronts.com/components/css-avatars/css-team-avatar-row-with-hover-spread/

An overlapped row that fans open when you point at it, so a tight facepile becomes a legible team list without a click. Every avatar moves with translate — never margin — so the fan costs nothing in layout, each face carries a name tooltip, and :focus-within means a keyboard user gets exactly the same reveal as a mouse user.
## HTML
```html
<div class="av-12">
  <input class="av-12__sr" type="checkbox" id="av-12-dark">
  <label class="av-12__theme" for="av-12-dark">
    <svg class="av-12__i av-12__i--moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.3A8.4 8.4 0 0 1 9.7 3.5a8.5 8.5 0 1 0 10.8 10.8Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="av-12__i av-12__i--sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.1" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.7 5.7l1.4 1.4M16.9 16.9l1.4 1.4M18.3 5.7l-1.4 1.4M7.1 16.9l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <span class="av-12__vh">Dark theme</span>
  </label>

  <div class="av-12__stage">
    <section class="av-12__wrap" aria-labelledby="av-12-h">
      <header class="av-12__head">
        <p class="av-12__eyebrow">Collaboration · Hover spread</p>
        <h2 class="av-12__h" id="av-12-h">Fan the team open</h2>
        <p class="av-12__sub">Point at the row, or tab into it — the faces separate and name themselves.</p>
      </header>

      <div class="av-12__panel">
        <p class="av-12__title">Platform squad</p>
        <ul class="av-12__row" style="--n:6" aria-label="Platform squad, 6 members">
          <li class="av-12__item" style="--i:0">
            <a class="av-12__link" href="#av-12-h">
              <img class="av-12__img" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=200&auto=format&fit=facearea&facepad=2.5" alt="Priya Sharma" width="200" height="200" loading="lazy" decoding="async">
              <span class="av-12__tip">Priya Sharma<span>Staff engineer</span></span>
            </a>
          </li>
          <li class="av-12__item" style="--i:1">
            <a class="av-12__link" href="#av-12-h">
              <img class="av-12__img" src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=200&auto=format&fit=facearea&facepad=2.5" alt="Alex Chen" width="200" height="200" loading="lazy" decoding="async">
              <span class="av-12__tip">Alex Chen<span>Backend</span></span>
            </a>
          </li>
          <li class="av-12__item" style="--i:2">
            <a class="av-12__link" href="#av-12-h">
              <img class="av-12__img" src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=200&auto=format&fit=facearea&facepad=2.5" alt="Maya Okonkwo" width="200" height="200" loading="lazy" decoding="async">
              <span class="av-12__tip">Maya Okonkwo<span>Design systems</span></span>
            </a>
          </li>
          <li class="av-12__item" style="--i:3">
            <a class="av-12__link" href="#av-12-h">
              <img class="av-12__img" src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=200&auto=format&fit=facearea&facepad=2.5" alt="Jordan Lee" width="200" height="200" loading="lazy" decoding="async">
              <span class="av-12__tip">Jordan Lee<span>SRE</span></span>
            </a>
          </li>
          <li class="av-12__item" style="--i:4">
            <a class="av-12__link" href="#av-12-h">
              <img class="av-12__img" src="https://images.unsplash.com/photo-1508214751196-bcfd4ca60f91?w=200&auto=format&fit=facearea&facepad=2.5" alt="Sam Rivera" width="200" height="200" loading="lazy" decoding="async">
              <span class="av-12__tip">Sam Rivera<span>Data</span></span>
            </a>
          </li>
          <li class="av-12__item" style="--i:5">
            <a class="av-12__link" href="#av-12-h">
              <img class="av-12__img" src="https://images.unsplash.com/photo-1531427186611-ecfd6d936c79?w=200&auto=format&fit=facearea&facepad=2.5" alt="Marcus Hale" width="200" height="200" loading="lazy" decoding="async">
              <span class="av-12__tip">Marcus Hale<span>Mobile</span></span>
            </a>
          </li>
        </ul>

        <p class="av-12__title av-12__title--second">Design guild</p>
        <ul class="av-12__row av-12__row--wide" style="--n:4" aria-label="Design guild, 4 members">
          <li class="av-12__item" style="--i:0">
            <a class="av-12__link" href="#av-12-h">
              <img class="av-12__img" src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=200&auto=format&fit=facearea&facepad=2.5" alt="Grace Tan" width="200" height="200" loading="lazy" decoding="async">
              <span class="av-12__tip">Grace Tan<span>Design lead</span></span>
            </a>
          </li>
          <li class="av-12__item" style="--i:1">
            <a class="av-12__link" href="#av-12-h">
              <img class="av-12__img" src="https://images.unsplash.com/photo-1580489944761-15a19d654956?w=200&auto=format&fit=facearea&facepad=2.5" alt="Isabel Moreau" width="200" height="200" loading="lazy" decoding="async">
              <span class="av-12__tip">Isabel Moreau<span>Brand</span></span>
            </a>
          </li>
          <li class="av-12__item" style="--i:2">
            <a class="av-12__link" href="#av-12-h">
              <img class="av-12__img" src="https://images.unsplash.com/photo-1607746882042-944635dfe10e?w=200&auto=format&fit=facearea&facepad=2.5" alt="Zoe Alvarez" width="200" height="200" loading="lazy" decoding="async">
              <span class="av-12__tip">Zoe Alvarez<span>Motion</span></span>
            </a>
          </li>
          <li class="av-12__item" style="--i:3">
            <a class="av-12__link" href="#av-12-h">
              <img class="av-12__img" src="https://images.unsplash.com/photo-1519345182560-3f2917c472ef?w=200&auto=format&fit=facearea&facepad=2.5" alt="Kai Nakamura" width="200" height="200" loading="lazy" decoding="async">
              <span class="av-12__tip">Kai Nakamura<span>Research</span></span>
            </a>
          </li>
        </ul>
      </div>
    </section>
  </div>
</div>
```
## CSS
```css
@supports (color: oklch(50% .1 250)) {
  .av-12 {
    --page: oklch(97.6% .004 265);
    --panel: oklch(100% 0 0);
    --panel-2: oklch(96.4% .006 265);
    --ink: oklch(20% .022 265);
    --muted: oklch(53% .022 265);
    --line: oklch(92% .008 265);
    --accent: oklch(58% .196 272);
  }
}

.av-12 {
  --page: #f7f8fa;
  --panel: #ffffff;
  --panel-2: #f1f3f7;
  --ink: #10131a;
  --muted: #5f6672;
  --line: #e4e7ee;
  --accent: #4f46e5;
  --glass: rgba(255,255,255,.68);
  --shadow: 0 1px 2px rgba(16,19,26,.05), 0 16px 36px -20px rgba(16,19,26,.3);
  --r: 18px;
  --sep: 3px;
  --fan: .95rem;
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

.av-12 *,
.av-12 *::before,
.av-12 *::after {
  box-sizing: border-box;
}

.av-12__vh {
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

.av-12__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  margin: 0;
  pointer-events: none;
}

.av-12__theme {
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

.av-12__theme::after {
  content: "";
  position: absolute;
  inset: -.4rem;
  border-radius: inherit;
}

.av-12__theme:hover {
  translate: 0 -1px;
}

.av-12__i {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.av-12__i--sun {
  display: none;
}

.av-12__sr:focus-visible + .av-12__theme {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.av-12__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
}

.av-12__wrap {
  inline-size: min(54rem,100%);
  max-inline-size: 100%;
  min-inline-size: 0;
  display: flex;
  flex-direction: column;
  gap: clamp(1.25rem,3vw,2rem);
}
/* Same min-width:auto guard as demo 04 — the fanned avatar row is wider
   than the column at 320px. */

.av-12__wrap > * {
  min-inline-size: 0;
}

.av-12__head {
  display: flex;
  flex-direction: column;
  gap: .4rem;
  padding-inline-end: 3.5rem;
}

.av-12__eyebrow {
  margin: 0;
  font-size: .7rem;
  font-weight: 600;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.av-12__h {
  margin: 0;
  font-size: clamp(1.6rem,4.2vw,2.4rem);
  font-weight: 650;
  letter-spacing: -.03em;
  line-height: 1.05;
}

.av-12__sub {
  margin: 0;
  max-inline-size: 36rem;
  font-size: .95rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.av-12__panel {
  padding: clamp(1.5rem,4vw,2.25rem);
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: var(--r);
  box-shadow: var(--shadow);
}

.av-12__title {
  margin: 0 0 .8rem;
  font-size: .78rem;
  font-weight: 600;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--muted);
}

.av-12__title--second {
  margin-block-start: clamp(2.75rem,7vw,4rem);
}

.av-12__row {
  --size: clamp(2.9rem,7.5vw,3.6rem);
  list-style: none;
  margin: 0;
  padding: 0 calc(var(--n) * var(--fan)) 0 0;
  display: flex;
  align-items: center;
  min-block-size: calc(var(--size) + .5rem);
}

.av-12__row--wide {
  --fan: 1.15rem;
}

.av-12__item {
  inline-size: var(--size);
  aspect-ratio: 1;
  flex: none;
  margin-inline-start: calc(var(--size) * -.36);
  z-index: calc(var(--n) - var(--i));
  transition: translate .32s cubic-bezier(.2,.8,.3,1);
  transition-delay: calc(var(--i) * 18ms);
}

.av-12__item:first-child {
  margin-inline-start: 0;
}

.av-12__row:hover .av-12__item,
.av-12__row:focus-within .av-12__item {
  translate: calc(var(--i) * var(--fan)) 0;
}

.av-12__link {
  position: relative;
  display: block;
  inline-size: 100%;
  block-size: 100%;
  border-radius: 50%;
}

.av-12__link:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.av-12__img {
  display: block;
  inline-size: 100%;
  block-size: 100%;
  border-radius: 50%;
  object-fit: cover;
  object-position: center top;
  background: var(--panel-2);
  box-shadow: 0 0 0 var(--sep) var(--panel);
  transition: translate .24s cubic-bezier(.2,.7,.3,1), box-shadow .24s ease;
}

.av-12__link:hover .av-12__img,
.av-12__link:focus-visible .av-12__img {
  translate: 0 -5px;
  box-shadow: 0 0 0 var(--sep) var(--panel), 0 0 0 calc(var(--sep) + 2px) var(--accent);
}

.av-12__item:hover,
.av-12__item:focus-within {
  z-index: calc(var(--n) + 2);
}

.av-12__tip {
  position: absolute;
  inset-block-end: calc(100% + .7rem);
  inset-inline-start: 50%;
  translate: -50% .3rem;
  z-index: 9;
  display: flex;
  flex-direction: column;
  gap: .05rem;
  inline-size: max-content;
  max-inline-size: 11rem;
  padding: .4rem .6rem;
  border-radius: 10px;
  background: var(--ink);
  color: var(--page);
  font-size: .78rem;
  font-weight: 600;
  line-height: 1.3;
  text-align: center;
  opacity: 0;
  pointer-events: none;
  transition: opacity .2s ease, translate .2s ease;
}

.av-12__tip span {
  font-size: .7rem;
  font-weight: 400;
  opacity: .75;
}

.av-12__link:hover .av-12__tip,
.av-12__link:focus-visible .av-12__tip {
  opacity: 1;
  translate: -50% 0;
}

@media (hover: none) {
  .av-12__item {
    translate: calc(var(--i) * var(--fan)) 0;
  }
}

.av-12:has(#av-12-dark:checked) {
  --page: #0a0b0e;
  --panel: #14161c;
  --panel-2: #1c1f27;
  --ink: #f2f4f9;
  --muted: #98a0b0;
  --line: #262a33;
  --accent: #8b8cf9;
  --glass: rgba(255,255,255,.07);
  --shadow: 0 1px 2px rgba(0,0,0,.6), 0 20px 44px -24px rgba(0,0,0,.85);
}

.av-12:has(#av-12-dark:checked) .av-12__tip {
  background: var(--panel-2);
  color: var(--ink);
  box-shadow: 0 0 0 1px var(--line);
}

.av-12:has(#av-12-dark:checked) .av-12__i--moon {
  display: none;
}

.av-12:has(#av-12-dark:checked) .av-12__i--sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .av-12:not(:has(#av-12-dark:checked)) {
    --page: #0a0b0e;
    --panel: #14161c;
    --panel-2: #1c1f27;
    --ink: #f2f4f9;
    --muted: #98a0b0;
    --line: #262a33;
    --accent: #8b8cf9;
    --glass: rgba(255,255,255,.07);
    --shadow: 0 1px 2px rgba(0,0,0,.6), 0 20px 44px -24px rgba(0,0,0,.85);
  }

  .av-12:not(:has(#av-12-dark:checked)) .av-12__tip {
    background: var(--panel-2);
    color: var(--ink);
    box-shadow: 0 0 0 1px var(--line);
  }

  .av-12:not(:has(#av-12-dark:checked)) .av-12__i--moon {
    display: none;
  }

  .av-12:not(:has(#av-12-dark:checked)) .av-12__i--sun {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .av-12 *,
    .av-12 *::before,
    .av-12 *::after {
    transition: none !important;
    animation: none !important;
  }

  .av-12__item {
    translate: calc(var(--i) * var(--fan)) 0;
  }
}

@media (forced-colors: active) {
  .av-12__img {
    box-shadow: 0 0 0 2px Canvas, 0 0 0 3px CanvasText;
  }

  .av-12__tip {
    background: Canvas;
    color: CanvasText;
    border: 1px solid CanvasText;
  }

  .av-12__panel,
    .av-12__theme {
    border-color: CanvasText;
  }
}
```
