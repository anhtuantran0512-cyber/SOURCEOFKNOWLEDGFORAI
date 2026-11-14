---
source: "codefronts"
url: "https://codefronts.com/components/css-avatars/css-gradient-ring-avatar/"
title: "CSS Gradient Ring Avatar"
section: "components"
category: "css-avatars"
category_name: "CSS Avatars"
description: "A gradient cannot go in a box-shadow and border-image refuses to follow border-radius — so the ring is built from two stacked backgrounds clipped…"
has_js: "false"
---

Here's a working CSS Avatar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Gradient Ring Avatar
Source: https://codefronts.com/components/css-avatars/css-gradient-ring-avatar/

A gradient cannot go in a box-shadow and border-image refuses to follow border-radius — so the ring is built from two stacked backgrounds clipped differently: the surface colour clipped to padding-box, the gradient clipped to border-box, with a transparent border as the gap between them. Three colourways, one shared structure, and a hover that rotates the gradient rather than repainting it.
## HTML
```html
<div class="av-03">
  <input class="av-03__sr" type="checkbox" id="av-03-dark">
  <label class="av-03__theme" for="av-03-dark">
    <svg class="av-03__i av-03__i--moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.3A8.4 8.4 0 0 1 9.7 3.5a8.5 8.5 0 1 0 10.8 10.8Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="av-03__i av-03__i--sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.1" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.7 5.7l1.4 1.4M16.9 16.9l1.4 1.4M18.3 5.7l-1.4 1.4M7.1 16.9l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <span class="av-03__vh">Dark theme</span>
  </label>

  <div class="av-03__stage">
    <section class="av-03__wrap" aria-labelledby="av-03-h">
      <header class="av-03__head">
        <p class="av-03__eyebrow">Identity · Avatar</p>
        <h2 class="av-03__h" id="av-03-h">Gradient rings</h2>
        <p class="av-03__sub">Two backgrounds, two clip boxes, one transparent border. Hover to sweep the ring.</p>
      </header>

      <ul class="av-03__row">
        <li class="av-03__item av-03__item--aurora">
          <a class="av-03__link" href="#av-03-h">
            <span class="av-03__fig" aria-hidden="true">
              <img class="av-03__img" src="https://images.unsplash.com/photo-1607746882042-944635dfe10e?w=200&auto=format&fit=facearea&facepad=2.5" alt="" width="200" height="200" loading="lazy" decoding="async">
            </span>
            <span class="av-03__who">
              <span class="av-03__name">Zoe Alvarez</span>
              <span class="av-03__role">Aurora</span>
            </span>
          </a>
        </li>
        <li class="av-03__item av-03__item--ember">
          <a class="av-03__link" href="#av-03-h">
            <span class="av-03__fig" aria-hidden="true">
              <img class="av-03__img" src="https://images.unsplash.com/photo-1599566150163-29194dcaad36?w=200&auto=format&fit=facearea&facepad=2.5" alt="" width="200" height="200" loading="lazy" decoding="async">
            </span>
            <span class="av-03__who">
              <span class="av-03__name">Omar Haddad</span>
              <span class="av-03__role">Ember</span>
            </span>
          </a>
        </li>
        <li class="av-03__item av-03__item--mint">
          <a class="av-03__link" href="#av-03-h">
            <span class="av-03__fig" aria-hidden="true">
              <img class="av-03__img" src="https://images.unsplash.com/photo-1502685104226-ee32379fefbe?w=200&auto=format&fit=facearea&facepad=2.5" alt="" width="200" height="200" loading="lazy" decoding="async">
            </span>
            <span class="av-03__who">
              <span class="av-03__name">Lucy Bennett</span>
              <span class="av-03__role">Mint</span>
            </span>
          </a>
        </li>
      </ul>

      <div class="av-03__strip">
        <span class="av-03__stripfig av-03__item--aurora"><img class="av-03__img" src="https://images.unsplash.com/photo-1541823709867-1b206113eafd?w=200&auto=format&fit=facearea&facepad=2.5" alt="Freya Nilsen" width="200" height="200" loading="lazy" decoding="async"></span>
        <span class="av-03__stripfig av-03__item--ember"><img class="av-03__img" src="https://images.unsplash.com/photo-1492562080023-ab3db95bfbce?w=200&auto=format&fit=facearea&facepad=2.5" alt="Simon Wexler" width="200" height="200" loading="lazy" decoding="async"></span>
        <span class="av-03__stripfig av-03__item--mint"><img class="av-03__img" src="https://images.unsplash.com/photo-1487412720507-e7ab37603c6f?w=200&auto=format&fit=facearea&facepad=2.5" alt="Mia Castellano" width="200" height="200" loading="lazy" decoding="async"></span>
        <span class="av-03__striptext">Same structure at 2.5rem — the ring scales with the border width.</span>
      </div>
    </section>
  </div>
</div>
```
## CSS
```css
@supports (color: oklch(50% .1 250)) {
  .av-03 {
    --page: oklch(97.6% .004 265);
    --panel: oklch(100% 0 0);
    --panel-2: oklch(96.4% .006 265);
    --ink: oklch(20% .022 265);
    --muted: oklch(53% .022 265);
    --line: oklch(92% .008 265);
    --accent: oklch(58% .196 272);
  }

  .av-03__item--aurora {
    --c1: oklch(70% .19 300);
    --c2: oklch(78% .15 200);
    --c3: oklch(72% .18 260);
  }

  .av-03__item--ember {
    --c1: oklch(72% .19 40);
    --c2: oklch(80% .16 80);
    --c3: oklch(66% .21 20);
  }

  .av-03__item--mint {
    --c1: oklch(78% .16 165);
    --c2: oklch(84% .13 130);
    --c3: oklch(72% .15 195);
  }
}

@property --av-03-a {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

.av-03 {
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
  --bw: 4px;
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

.av-03 *,
.av-03 *::before,
.av-03 *::after {
  box-sizing: border-box;
}

.av-03__vh {
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

.av-03__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  margin: 0;
  pointer-events: none;
}

.av-03__theme {
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

.av-03__theme::after {
  content: "";
  position: absolute;
  inset: -.4rem;
  border-radius: inherit;
}

.av-03__theme:hover {
  translate: 0 -1px;
}

.av-03__i {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.av-03__i--sun {
  display: none;
}

.av-03__sr:focus-visible + .av-03__theme {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.av-03__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
}

.av-03__wrap {
  inline-size: min(58rem,100%);
  display: flex;
  flex-direction: column;
  gap: clamp(1.25rem,3vw,2rem);
}

.av-03__head {
  display: flex;
  flex-direction: column;
  gap: .4rem;
  padding-inline-end: 3.5rem;
}

.av-03__eyebrow {
  margin: 0;
  font-size: .7rem;
  font-weight: 600;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.av-03__h {
  margin: 0;
  font-size: clamp(1.6rem,4.2vw,2.4rem);
  font-weight: 650;
  letter-spacing: -.03em;
  line-height: 1.05;
}

.av-03__sub {
  margin: 0;
  max-inline-size: 36rem;
  font-size: .95rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.av-03__row {
  list-style: none;
  margin: 0;
  padding: clamp(1.5rem,4vw,2.5rem) clamp(1rem,3vw,2rem);
  display: grid;
  gap: clamp(1.25rem,3vw,2rem);
  grid-template-columns: repeat(auto-fit,minmax(10rem,1fr));
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: var(--r);
  box-shadow: var(--shadow);
}

.av-03__link {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: .8rem;
  text-decoration: none;
  color: inherit;
  border-radius: 14px;
  padding: .5rem;
}

.av-03__link:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.av-03__fig {
  --a: var(--av-03-a);
  display: grid;
  inline-size: clamp(5rem,14vw,7.5rem);
  aspect-ratio: 1;
  padding: 0;
  border: var(--bw) solid transparent;
  border-radius: 50%;
  background: linear-gradient(var(--panel), var(--panel)) padding-box, conic-gradient(from var(--a), var(--c1), var(--c2), var(--c3), var(--c1)) border-box;
  background-origin: border-box;
  transition: translate .25s cubic-bezier(.2,.7,.3,1), --av-03-a .9s linear, border-width .25s ease;
}

.av-03__img {
  display: block;
  inline-size: 100%;
  block-size: auto;
  aspect-ratio: 1;
  border-radius: 50%;
  object-fit: cover;
  object-position: center top;
  background: var(--panel-2);
}

.av-03__link:hover .av-03__fig,
.av-03__link:focus-visible .av-03__fig {
  --av-03-a: 360deg;
  translate: 0 -4px;
}

.av-03__who {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: .1rem;
  text-align: center;
}

.av-03__name {
  font-size: .95rem;
  font-weight: 600;
  letter-spacing: -.01em;
}

.av-03__role {
  font-size: .78rem;
  color: var(--muted);
}

.av-03__item--aurora {
  --c1: #a855f7;
  --c2: #22d3ee;
  --c3: #6366f1;
}

.av-03__item--ember {
  --c1: #fb7185;
  --c2: #fbbf24;
  --c3: #f43f5e;
}

.av-03__item--mint {
  --c1: #34d399;
  --c2: #a3e635;
  --c3: #22d3ee;
}

.av-03__strip {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: .75rem;
  padding: .85rem 1rem;
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 14px;
}

.av-03__stripfig {
  display: block;
  inline-size: 2.5rem;
  aspect-ratio: 1;
  border: 2px solid transparent;
  border-radius: 50%;
  background: linear-gradient(var(--panel), var(--panel)) padding-box, conic-gradient(from 45deg, var(--c1), var(--c2), var(--c3), var(--c1)) border-box;
  background-origin: border-box;
  flex: none;
}

.av-03__striptext {
  font-size: .82rem;
  color: var(--muted);
}

.av-03:has(#av-03-dark:checked) {
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

.av-03:has(#av-03-dark:checked) .av-03__i--moon {
  display: none;
}

.av-03:has(#av-03-dark:checked) .av-03__i--sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .av-03:not(:has(#av-03-dark:checked)) {
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

  .av-03:not(:has(#av-03-dark:checked)) .av-03__i--moon {
    display: none;
  }

  .av-03:not(:has(#av-03-dark:checked)) .av-03__i--sun {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .av-03 *,
    .av-03 *::before,
    .av-03 *::after {
    transition: none !important;
    animation: none !important;
  }

  .av-03__link:hover .av-03__fig {
    --av-03-a: 0deg;
  }
}

@media (forced-colors: active) {
  .av-03__fig,
    .av-03__stripfig {
    background: Canvas;
    border-color: CanvasText;
  }

  .av-03__row,
    .av-03__strip,
    .av-03__theme {
    border-color: CanvasText;
  }
}
```
