---
source: "codefronts"
url: "https://codefronts.com/components/css-avatars/css-conic-gradient-story-ring-avatar/"
title: "CSS Conic Gradient Story Ring Avatar"
section: "components"
category: "css-avatars"
category_name: "CSS Avatars"
description: "The story-ring pattern with the state model people actually forget: unread is a saturated conic sweep on a slow rotation, seen is a flat grey static ring,…"
has_js: "false"
---

Here's a working CSS Avatar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Conic Gradient Story Ring Avatar
Source: https://codefronts.com/components/css-avatars/css-conic-gradient-story-ring-avatar/

The story-ring pattern with the state model people actually forget: unread is a saturated conic sweep on a slow rotation, seen is a flat grey static ring, and each carries visually-hidden text so the difference is not purely visual. Rotation lives on a pseudo-element so the ring spins while the photo stays perfectly still, and it stops dead under prefers-reduced-motion.
## HTML
```html
<div class="av-04">
  <input class="av-04__sr" type="checkbox" id="av-04-dark">
  <label class="av-04__theme" for="av-04-dark">
    <svg class="av-04__i av-04__i--moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.3A8.4 8.4 0 0 1 9.7 3.5a8.5 8.5 0 1 0 10.8 10.8Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="av-04__i av-04__i--sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.1" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.7 5.7l1.4 1.4M16.9 16.9l1.4 1.4M18.3 5.7l-1.4 1.4M7.1 16.9l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <span class="av-04__vh">Dark theme</span>
  </label>

  <div class="av-04__stage">
    <section class="av-04__wrap" aria-labelledby="av-04-h">
      <header class="av-04__head">
        <p class="av-04__eyebrow">Identity · Avatar</p>
        <h2 class="av-04__h" id="av-04-h">Story rings</h2>
        <p class="av-04__sub">Unread sweeps, seen sits still. Hover a ring to pause it.</p>
      </header>

      <ul class="av-04__rail">
        <li class="av-04__story av-04__story--unread">
          <a class="av-04__link" href="#av-04-h">
            <span class="av-04__fig"><img class="av-04__img" src="https://images.unsplash.com/photo-1554151228-14d9def656e4?w=200&auto=format&fit=facearea&facepad=2.5" alt="Aisha Rahman" width="200" height="200" loading="lazy" decoding="async"></span>
            <span class="av-04__name">Aisha</span>
            <span class="av-04__vh">Unread story</span>
          </a>
        </li>
        <li class="av-04__story av-04__story--unread">
          <a class="av-04__link" href="#av-04-h">
            <span class="av-04__fig"><img class="av-04__img" src="https://images.unsplash.com/photo-1519345182560-3f2917c472ef?w=200&auto=format&fit=facearea&facepad=2.5" alt="Kai Nakamura" width="200" height="200" loading="lazy" decoding="async"></span>
            <span class="av-04__name">Kai</span>
            <span class="av-04__vh">Unread story</span>
          </a>
        </li>
        <li class="av-04__story av-04__story--unread">
          <a class="av-04__link" href="#av-04-h">
            <span class="av-04__fig"><img class="av-04__img" src="https://images.unsplash.com/photo-1601412436009-d964bd02edbc?w=200&auto=format&fit=facearea&facepad=2.5" alt="Nina Kaur" width="200" height="200" loading="lazy" decoding="async"></span>
            <span class="av-04__name">Nina</span>
            <span class="av-04__vh">Unread story</span>
          </a>
        </li>
        <li class="av-04__story av-04__story--seen">
          <a class="av-04__link" href="#av-04-h">
            <span class="av-04__fig"><img class="av-04__img" src="https://images.unsplash.com/photo-1596815064285-45ed8a9c0463?w=200&auto=format&fit=facearea&facepad=2.5" alt="Dev Raman" width="200" height="200" loading="lazy" decoding="async"></span>
            <span class="av-04__name">Dev</span>
            <span class="av-04__vh">Story already seen</span>
          </a>
        </li>
        <li class="av-04__story av-04__story--seen">
          <a class="av-04__link" href="#av-04-h">
            <span class="av-04__fig"><img class="av-04__img" src="https://images.unsplash.com/photo-1618641986557-1ecd230959aa?w=200&auto=format&fit=facearea&facepad=2.5" alt="Tara Whitfield" width="200" height="200" loading="lazy" decoding="async"></span>
            <span class="av-04__name">Tara</span>
            <span class="av-04__vh">Story already seen</span>
          </a>
        </li>
        <li class="av-04__story av-04__story--seen">
          <a class="av-04__link" href="#av-04-h">
            <span class="av-04__fig"><img class="av-04__img" src="https://images.unsplash.com/photo-1564564321837-a57b7070ac4f?w=200&auto=format&fit=facearea&facepad=2.5" alt="Julian Fontaine" width="200" height="200" loading="lazy" decoding="async"></span>
            <span class="av-04__name">Julian</span>
            <span class="av-04__vh">Story already seen</span>
          </a>
        </li>
      </ul>

      <ul class="av-04__legend">
        <li class="av-04__leg"><span class="av-04__swatch av-04__swatch--unread" aria-hidden="true"></span>Unread — saturated sweep, 6s loop</li>
        <li class="av-04__leg"><span class="av-04__swatch av-04__swatch--seen" aria-hidden="true"></span>Seen — flat hairline, no motion</li>
      </ul>
    </section>
  </div>
</div>
```
## CSS
```css
@supports (color: oklch(50% .1 250)) {
  .av-04 {
    --page: oklch(97.6% .004 265);
    --panel: oklch(100% 0 0);
    --panel-2: oklch(96.4% .006 265);
    --ink: oklch(20% .022 265);
    --muted: oklch(53% .022 265);
    --line: oklch(90% .008 265);
    --accent: oklch(58% .196 272);
  }

  .av-04__story--unread {
    --s1: oklch(84% .17 85);
    --s2: oklch(62% .25 5);
    --s3: oklch(52% .25 295);
  }
}

.av-04 {
  --page: #f7f8fa;
  --panel: #ffffff;
  --panel-2: #f1f3f7;
  --ink: #10131a;
  --muted: #5f6672;
  --line: #e2e5ec;
  --accent: #4f46e5;
  --glass: rgba(255,255,255,.68);
  --shadow: 0 1px 2px rgba(16,19,26,.05), 0 16px 36px -20px rgba(16,19,26,.3);
  --r: 18px;
  --ring: 5px;
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
  /* The story rail scrolls horizontally on purpose; without clip here its
       overflow propagates to the document and takes the whole page sideways
       at narrow widths. clip (not hidden) keeps position:sticky usable. */
  overflow-x: clip;
}

.av-04 *,
.av-04 *::before,
.av-04 *::after {
  box-sizing: border-box;
}

.av-04__vh {
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

.av-04__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  margin: 0;
  pointer-events: none;
}

.av-04__theme {
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

.av-04__theme::after {
  content: "";
  position: absolute;
  inset: -.4rem;
  border-radius: inherit;
}

.av-04__theme:hover {
  translate: 0 -1px;
}

.av-04__i {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.av-04__i--sun {
  display: none;
}

.av-04__sr:focus-visible + .av-04__theme {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.av-04__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
}

.av-04__wrap {
  inline-size: min(58rem,100%);
  max-inline-size: 100%;
  min-inline-size: 0;
  display: flex;
  flex-direction: column;
  gap: clamp(1.25rem,3vw,2rem);
}
/* Flex children default to min-width:auto, so the horizontally scrollable
   rail below would otherwise push this wrapper past its own 100% and take
   the document sideways at narrow widths. */

.av-04__wrap > * {
  min-inline-size: 0;
}

.av-04__head {
  display: flex;
  flex-direction: column;
  gap: .4rem;
  padding-inline-end: 3.5rem;
}

.av-04__eyebrow {
  margin: 0;
  font-size: .7rem;
  font-weight: 600;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.av-04__h {
  margin: 0;
  font-size: clamp(1.6rem,4.2vw,2.4rem);
  font-weight: 650;
  letter-spacing: -.03em;
  line-height: 1.05;
}

.av-04__sub {
  margin: 0;
  max-inline-size: 36rem;
  font-size: .95rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.av-04__rail {
  list-style: none;
  margin: 0;
  min-inline-size: 0;
  max-inline-size: 100%;
  display: flex;
  align-items: flex-start;
  gap: clamp(.9rem,2.5vw,1.5rem);
  padding: clamp(1.35rem,3.5vw,2rem) clamp(1rem,3vw,1.75rem);
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: var(--r);
  box-shadow: var(--shadow);
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  scrollbar-width: thin;
  overscroll-behavior-inline: contain;
}

.av-04__story {
  flex: none;
  scroll-snap-align: center;
}

.av-04__link {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: .6rem;
  text-decoration: none;
  color: inherit;
  border-radius: 14px;
  padding: .25rem;
}

.av-04__link:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.av-04__fig {
  position: relative;
  display: block;
  inline-size: clamp(4rem,11vw,5.5rem);
  aspect-ratio: 1;
  border-radius: 50%;
  isolation: isolate;
}

.av-04__fig::before {
  content: "";
  position: absolute;
  inset: calc(var(--ring) * -1);
  border-radius: 50%;
  z-index: 0;
  background: conic-gradient(from 0deg, var(--s1), var(--s2), var(--s3), var(--s1));
  animation: av-04-spin 6s linear infinite;
}

.av-04__img {
  position: relative;
  z-index: 1;
  display: block;
  inline-size: 100%;
  block-size: auto;
  aspect-ratio: 1;
  border-radius: 50%;
  object-fit: cover;
  object-position: center top;
  background: var(--panel-2);
  box-shadow: 0 0 0 3px var(--panel);
}

.av-04__name {
  font-size: .82rem;
  font-weight: 600;
  letter-spacing: -.01em;
}

.av-04__story--seen {
  --s1: var(--line);
  --s2: var(--line);
  --s3: var(--line);
}

.av-04__story--seen .av-04__fig::before {
  animation: none;
  inset: -3px;
}

.av-04__story--seen .av-04__img {
  filter: saturate(.75);
}

.av-04__story--seen .av-04__name {
  color: var(--muted);
  font-weight: 500;
}

.av-04__link:hover .av-04__fig::before {
  animation-play-state: paused;
}

@keyframes av-04-spin {
  to {
    rotate: 360deg;
  }
}

.av-04__legend {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  gap: .5rem 1.5rem;
  font-size: .85rem;
  color: var(--muted);
}

.av-04__leg {
  display: flex;
  align-items: center;
  gap: .5rem;
}

.av-04__swatch {
  inline-size: 1.1rem;
  block-size: 1.1rem;
  border-radius: 50%;
  flex: none;
}

.av-04__swatch--unread {
  background: conic-gradient(from 0deg, #f9ce34, #ee2a7b, #6228d7, #f9ce34);
}

.av-04__swatch--seen {
  background: var(--line);
}

.av-04__story--unread {
  --s1: #f9ce34;
  --s2: #ee2a7b;
  --s3: #6228d7;
}

.av-04:has(#av-04-dark:checked) {
  --page: #0a0b0e;
  --panel: #14161c;
  --panel-2: #1c1f27;
  --ink: #f2f4f9;
  --muted: #98a0b0;
  --line: #2c3140;
  --accent: #8b8cf9;
  --glass: rgba(255,255,255,.07);
  --shadow: 0 1px 2px rgba(0,0,0,.6), 0 20px 44px -24px rgba(0,0,0,.85);
}

.av-04:has(#av-04-dark:checked) .av-04__story--seen {
  --s1: #3d4557;
  --s2: #3d4557;
  --s3: #3d4557;
}

.av-04:has(#av-04-dark:checked) .av-04__i--moon {
  display: none;
}

.av-04:has(#av-04-dark:checked) .av-04__i--sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .av-04:not(:has(#av-04-dark:checked)) {
    --page: #0a0b0e;
    --panel: #14161c;
    --panel-2: #1c1f27;
    --ink: #f2f4f9;
    --muted: #98a0b0;
    --line: #2c3140;
    --accent: #8b8cf9;
    --glass: rgba(255,255,255,.07);
    --shadow: 0 1px 2px rgba(0,0,0,.6), 0 20px 44px -24px rgba(0,0,0,.85);
  }

  .av-04:not(:has(#av-04-dark:checked)) .av-04__story--seen {
    --s1: #3d4557;
    --s2: #3d4557;
    --s3: #3d4557;
  }

  .av-04:not(:has(#av-04-dark:checked)) .av-04__i--moon {
    display: none;
  }

  .av-04:not(:has(#av-04-dark:checked)) .av-04__i--sun {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .av-04 *,
    .av-04 *::before,
    .av-04 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .av-04__fig::before {
    background: CanvasText;
  }

  .av-04__story--seen .av-04__fig::before {
    background: GrayText;
  }

  .av-04__rail,
    .av-04__theme {
    border-color: CanvasText;
  }
}
```
