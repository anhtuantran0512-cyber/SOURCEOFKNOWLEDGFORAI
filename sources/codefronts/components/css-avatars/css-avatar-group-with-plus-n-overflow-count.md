---
source: "codefronts"
url: "https://codefronts.com/components/css-avatars/css-avatar-group-with-plus-n-overflow-count/"
title: "CSS Avatar Group with Plus-N Overflow Count"
section: "components"
category: "css-avatars"
category_name: "CSS Avatars"
description: "A facepile that tells the truth about how many people are in the room: the final slot is a +N chip built to exactly the avatar's dimensions — same size…"
has_js: "false"
---

Here's a working CSS Avatar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Avatar Group with Plus-N Overflow Count
Source: https://codefronts.com/components/css-avatars/css-avatar-group-with-plus-n-overflow-count/

A facepile that tells the truth about how many people are in the room: the final slot is a +N chip built to exactly the avatar's dimensions — same size token, same ring, same stack position — so the row's rhythm never breaks. The chip is a real <button> with the full count in its accessible name, and it expands the hidden members with pure CSS via a checkbox and :has().
## HTML
```html
<div class="av-11">
  <input class="av-11__sr" type="checkbox" id="av-11-dark">
  <label class="av-11__theme" for="av-11-dark">
    <svg class="av-11__i av-11__i--moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.3A8.4 8.4 0 0 1 9.7 3.5a8.5 8.5 0 1 0 10.8 10.8Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="av-11__i av-11__i--sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.1" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.7 5.7l1.4 1.4M16.9 16.9l1.4 1.4M18.3 5.7l-1.4 1.4M7.1 16.9l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <span class="av-11__vh">Dark theme</span>
  </label>

  <div class="av-11__stage">
    <section class="av-11__wrap" aria-labelledby="av-11-h">
      <header class="av-11__head">
        <p class="av-11__eyebrow">Collaboration · Overflow</p>
        <h2 class="av-11__h" id="av-11-h">Plus-N counters</h2>
        <p class="av-11__sub">The chip is the same size, ring and stack slot as a face. Open it to see the rest.</p>
      </header>

      <div class="av-11__panel">
        <div class="av-11__block">
          <p class="av-11__label">Northwind redesign <span>17 people</span></p>
          <ul class="av-11__group" style="--n:6" aria-label="17 people in the Northwind redesign project">
            <li class="av-11__item" style="--i:0"><img class="av-11__img" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=200&auto=format&fit=facearea&facepad=2.5" alt="Priya Sharma" width="200" height="200" loading="lazy" decoding="async"></li>
            <li class="av-11__item" style="--i:1"><img class="av-11__img" src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=200&auto=format&fit=facearea&facepad=2.5" alt="Alex Chen" width="200" height="200" loading="lazy" decoding="async"></li>
            <li class="av-11__item" style="--i:2"><img class="av-11__img" src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=200&auto=format&fit=facearea&facepad=2.5" alt="Maya Okonkwo" width="200" height="200" loading="lazy" decoding="async"></li>
            <li class="av-11__item" style="--i:3"><img class="av-11__img" src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=200&auto=format&fit=facearea&facepad=2.5" alt="Jordan Lee" width="200" height="200" loading="lazy" decoding="async"></li>
            <li class="av-11__item" style="--i:4"><img class="av-11__img" src="https://images.unsplash.com/photo-1508214751196-bcfd4ca60f91?w=200&auto=format&fit=facearea&facepad=2.5" alt="Sam Rivera" width="200" height="200" loading="lazy" decoding="async"></li>
            <li class="av-11__item av-11__extra" style="--i:5"><img class="av-11__img" src="https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=200&auto=format&fit=facearea&facepad=2.5" alt="Nadia Petrov" width="200" height="200" loading="lazy" decoding="async"></li>
            <li class="av-11__item av-11__extra" style="--i:6"><img class="av-11__img" src="https://images.unsplash.com/photo-1531427186611-ecfd6d936c79?w=200&auto=format&fit=facearea&facepad=2.5" alt="Marcus Hale" width="200" height="200" loading="lazy" decoding="async"></li>
            <li class="av-11__item av-11__extra" style="--i:7"><img class="av-11__img" src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=200&auto=format&fit=facearea&facepad=2.5" alt="Grace Tan" width="200" height="200" loading="lazy" decoding="async"></li>
            <li class="av-11__item av-11__extra" style="--i:8"><img class="av-11__img" src="https://images.unsplash.com/photo-1580489944761-15a19d654956?w=200&auto=format&fit=facearea&facepad=2.5" alt="Isabel Moreau" width="200" height="200" loading="lazy" decoding="async"></li>
            <li class="av-11__item av-11__chipslot" style="--i:9">
              <label class="av-11__more">
                <input class="av-11__toggle" type="checkbox">
                <span class="av-11__morenum av-11__morenum--closed" aria-hidden="true">+12</span>
                <span class="av-11__morenum av-11__morenum--open" aria-hidden="true">
                  <svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M6 6l12 12M18 6L6 18" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg>
                </span>
                <span class="av-11__vh">Show the 12 other people in this project</span>
              </label>
            </li>
          </ul>
        </div>

        <div class="av-11__block">
          <p class="av-11__label">Waiting on review <span>5 people</span></p>
          <ul class="av-11__group av-11__group--sm" style="--n:4" aria-label="5 people waiting on review">
            <li class="av-11__item" style="--i:0"><img class="av-11__img" src="https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?w=200&auto=format&fit=facearea&facepad=2.5" alt="Ethan Brooks" width="200" height="200" loading="lazy" decoding="async"></li>
            <li class="av-11__item" style="--i:1"><img class="av-11__img" src="https://images.unsplash.com/photo-1607746882042-944635dfe10e?w=200&auto=format&fit=facearea&facepad=2.5" alt="Zoe Alvarez" width="200" height="200" loading="lazy" decoding="async"></li>
            <li class="av-11__item" style="--i:2"><img class="av-11__img" src="https://images.unsplash.com/photo-1599566150163-29194dcaad36?w=200&auto=format&fit=facearea&facepad=2.5" alt="Omar Haddad" width="200" height="200" loading="lazy" decoding="async"></li>
            <li class="av-11__item av-11__chipslot" style="--i:3">
              <span class="av-11__more av-11__more--static" aria-hidden="true">+2</span>
              <span class="av-11__vh">And 2 more people</span>
            </li>
          </ul>
        </div>

        <div class="av-11__block">
          <p class="av-11__label">Signed up today <span>151 people</span></p>
          <ul class="av-11__group av-11__group--sm" style="--n:4" aria-label="151 people signed up today">
            <li class="av-11__item" style="--i:0"><img class="av-11__img" src="https://images.unsplash.com/photo-1554151228-14d9def656e4?w=200&auto=format&fit=facearea&facepad=2.5" alt="Aisha Rahman" width="200" height="200" loading="lazy" decoding="async"></li>
            <li class="av-11__item" style="--i:1"><img class="av-11__img" src="https://images.unsplash.com/photo-1601412436009-d964bd02edbc?w=200&auto=format&fit=facearea&facepad=2.5" alt="Nina Kaur" width="200" height="200" loading="lazy" decoding="async"></li>
            <li class="av-11__item" style="--i:2"><img class="av-11__img" src="https://images.unsplash.com/photo-1596815064285-45ed8a9c0463?w=200&auto=format&fit=facearea&facepad=2.5" alt="Dev Raman" width="200" height="200" loading="lazy" decoding="async"></li>
            <li class="av-11__item av-11__chipslot" style="--i:3">
              <span class="av-11__more av-11__more--static" aria-hidden="true">+148</span>
              <span class="av-11__vh">And 148 more people</span>
            </li>
          </ul>
        </div>
      </div>
    </section>
  </div>
</div>
```
## CSS
```css
@supports (color: oklch(50% .1 250)) {
  .av-11 {
    --page: oklch(97.6% .004 265);
    --panel: oklch(100% 0 0);
    --panel-2: oklch(96.4% .006 265);
    --ink: oklch(20% .022 265);
    --muted: oklch(53% .022 265);
    --line: oklch(92% .008 265);
    --accent: oklch(58% .196 272);
  }
}

.av-11 {
  --page: #f7f8fa;
  --panel: #ffffff;
  --panel-2: #f1f3f7;
  --ink: #10131a;
  --muted: #5f6672;
  --line: #e4e7ee;
  --accent: #4f46e5;
  --glass: rgba(255,255,255,.68);
  --chip: #eef0f6;
  --chip-ink: #2a3040;
  --shadow: 0 1px 2px rgba(16,19,26,.05), 0 16px 36px -20px rgba(16,19,26,.3);
  --r: 18px;
  --sep: 3px;
  --dens: .34;
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

.av-11 *,
.av-11 *::before,
.av-11 *::after {
  box-sizing: border-box;
}

.av-11__vh {
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

.av-11__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  margin: 0;
  pointer-events: none;
}

.av-11__theme {
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

.av-11__theme::after {
  content: "";
  position: absolute;
  inset: -.4rem;
  border-radius: inherit;
}

.av-11__theme:hover {
  translate: 0 -1px;
}

.av-11__i {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.av-11__i--sun {
  display: none;
}

.av-11__sr:focus-visible + .av-11__theme {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.av-11__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
}

.av-11__wrap {
  inline-size: min(54rem,100%);
  display: flex;
  flex-direction: column;
  gap: clamp(1.25rem,3vw,2rem);
}

.av-11__head {
  display: flex;
  flex-direction: column;
  gap: .4rem;
  padding-inline-end: 3.5rem;
}

.av-11__eyebrow {
  margin: 0;
  font-size: .7rem;
  font-weight: 600;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.av-11__h {
  margin: 0;
  font-size: clamp(1.6rem,4.2vw,2.4rem);
  font-weight: 650;
  letter-spacing: -.03em;
  line-height: 1.05;
}

.av-11__sub {
  margin: 0;
  max-inline-size: 36rem;
  font-size: .95rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.av-11__panel {
  display: flex;
  flex-direction: column;
  gap: clamp(1.35rem,3.5vw,2.25rem);
  padding: clamp(1.5rem,4vw,2.25rem);
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: var(--r);
  box-shadow: var(--shadow);
}

.av-11__block {
  display: flex;
  flex-direction: column;
  gap: .65rem;
}

.av-11__label {
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  gap: .55rem;
  font-size: .95rem;
  font-weight: 650;
  letter-spacing: -.015em;
}

.av-11__label span {
  font-size: .78rem;
  font-weight: 500;
  letter-spacing: 0;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.av-11__group {
  --size: clamp(2.75rem,7vw,3.5rem);
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  row-gap: .5rem;
}

.av-11__group--sm {
  --size: 2.75rem;
}

.av-11__item {
  inline-size: var(--size);
  aspect-ratio: 1;
  flex: none;
  margin-inline-start: calc(var(--size) * var(--dens) * -1);
  z-index: calc(var(--n) - var(--i));
  transition: translate .22s cubic-bezier(.2,.7,.3,1);
}

.av-11__item:first-child {
  margin-inline-start: 0;
}

.av-11__item:hover {
  z-index: calc(var(--n) + 2);
  translate: 0 -4px;
}

.av-11__img {
  display: block;
  inline-size: 100%;
  block-size: 100%;
  border-radius: 50%;
  object-fit: cover;
  object-position: center top;
  background: var(--panel-2);
  box-shadow: 0 0 0 var(--sep) var(--panel);
}

.av-11__chipslot {
  z-index: calc(var(--n) + 1);
}

.av-11__more {
  position: relative;
  display: grid;
  place-items: center;
  inline-size: 100%;
  block-size: 100%;
  border-radius: 50%;
  background: var(--chip);
  color: var(--chip-ink);
  box-shadow: 0 0 0 var(--sep) var(--panel), inset 0 0 0 1px rgba(16,19,26,.05);
  font-size: .8rem;
  font-weight: 700;
  letter-spacing: -.02em;
  font-variant-numeric: tabular-nums;
  cursor: pointer;
  transition: background .18s ease, translate .22s cubic-bezier(.2,.7,.3,1);
}

.av-11__more--static {
  cursor: default;
}

.av-11__more:hover {
  translate: 0 -4px;
}

.av-11__more::after {
  content: "";
  position: absolute;
  inset: -.35rem;
  border-radius: inherit;
}

.av-11__toggle {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  margin: 0;
}

.av-11__toggle:focus-visible + .av-11__morenum {
  outline: 2px solid var(--accent);
  outline-offset: .55rem;
  border-radius: 50%;
}

.av-11__morenum {
  display: grid;
  place-items: center;
  inline-size: 100%;
  block-size: 100%;
}

.av-11__morenum--open {
  display: none;
}

.av-11__morenum--open svg {
  inline-size: 45%;
  block-size: 45%;
}

.av-11__extra {
  display: none;
}

.av-11__group:has(.av-11__toggle:checked) .av-11__extra {
  display: block;
}

.av-11__group:has(.av-11__toggle:checked) .av-11__morenum--closed {
  display: none;
}

.av-11__group:has(.av-11__toggle:checked) .av-11__morenum--open {
  display: grid;
}

@supports (transition-behavior: allow-discrete) {
  .av-11__extra {
    transition: opacity .24s ease, scale .24s cubic-bezier(.2,.8,.3,1.1), display .24s allow-discrete;
  }

  @starting-style {
    .av-11__group:has(.av-11__toggle:checked) .av-11__extra {
      opacity: 0;
      scale: .6;
    }
  }
}

.av-11:has(#av-11-dark:checked) {
  --page: #0a0b0e;
  --panel: #14161c;
  --panel-2: #1c1f27;
  --ink: #f2f4f9;
  --muted: #98a0b0;
  --line: #262a33;
  --accent: #8b8cf9;
  --glass: rgba(255,255,255,.07);
  --chip: #242832;
  --chip-ink: #e6eaf2;
  --shadow: 0 1px 2px rgba(0,0,0,.6), 0 20px 44px -24px rgba(0,0,0,.85);
}

.av-11:has(#av-11-dark:checked) .av-11__more {
  box-shadow: 0 0 0 var(--sep) var(--panel), inset 0 0 0 1px rgba(255,255,255,.08);
}

.av-11:has(#av-11-dark:checked) .av-11__i--moon {
  display: none;
}

.av-11:has(#av-11-dark:checked) .av-11__i--sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .av-11:not(:has(#av-11-dark:checked)) {
    --page: #0a0b0e;
    --panel: #14161c;
    --panel-2: #1c1f27;
    --ink: #f2f4f9;
    --muted: #98a0b0;
    --line: #262a33;
    --accent: #8b8cf9;
    --glass: rgba(255,255,255,.07);
    --chip: #242832;
    --chip-ink: #e6eaf2;
    --shadow: 0 1px 2px rgba(0,0,0,.6), 0 20px 44px -24px rgba(0,0,0,.85);
  }

  .av-11:not(:has(#av-11-dark:checked)) .av-11__more {
    box-shadow: 0 0 0 var(--sep) var(--panel), inset 0 0 0 1px rgba(255,255,255,.08);
  }

  .av-11:not(:has(#av-11-dark:checked)) .av-11__i--moon {
    display: none;
  }

  .av-11:not(:has(#av-11-dark:checked)) .av-11__i--sun {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .av-11 *,
    .av-11 *::before,
    .av-11 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .av-11__img,
    .av-11__more {
    box-shadow: 0 0 0 2px Canvas, 0 0 0 3px CanvasText;
  }

  .av-11__panel,
    .av-11__theme {
    border-color: CanvasText;
  }
}
```
