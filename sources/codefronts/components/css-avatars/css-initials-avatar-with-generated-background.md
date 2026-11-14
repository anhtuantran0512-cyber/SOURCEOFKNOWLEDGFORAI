---
source: "codefronts"
url: "https://codefronts.com/components/css-avatars/css-initials-avatar-with-generated-background/"
title: "CSS Initials Avatar with Generated Background"
section: "components"
category: "css-avatars"
category_name: "CSS Avatars"
description: "The no-photo avatar that still looks designed: the app passes a single number — a hue derived from the user's id — and CSS builds the whole swatch from it."
has_js: "false"
---

Here's a working CSS Avatar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Initials Avatar with Generated Background
Source: https://codefronts.com/components/css-avatars/css-initials-avatar-with-generated-background/

The no-photo avatar that still looks designed: the app passes a single number — a hue derived from the user's id — and CSS builds the whole swatch from it. Because oklch() pins lightness and lets only hue vary, every generated background is contrast-safe by construction rather than by luck, and three fills (soft, solid, ringed) all read from the same one variable.
## HTML
```html
<div class="av-14">
  <input class="av-14__sr" type="checkbox" id="av-14-dark">
  <label class="av-14__theme" for="av-14-dark">
    <svg class="av-14__i av-14__i--moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.3A8.4 8.4 0 0 1 9.7 3.5a8.5 8.5 0 1 0 10.8 10.8Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="av-14__i av-14__i--sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.1" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.7 5.7l1.4 1.4M16.9 16.9l1.4 1.4M18.3 5.7l-1.4 1.4M7.1 16.9l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <span class="av-14__vh">Dark theme</span>
  </label>

  <div class="av-14__stage">
    <section class="av-14__wrap" aria-labelledby="av-14-h">
      <header class="av-14__head">
        <p class="av-14__eyebrow">Fallback · Initials</p>
        <h2 class="av-14__h" id="av-14-h">Generated monograms</h2>
        <p class="av-14__sub">The app supplies one hue. CSS derives the fill, the text and the ring — contrast held constant.</p>
      </header>

      <fieldset class="av-14__seg">
        <legend class="av-14__vh">Fill treatment</legend>
        <label class="av-14__segbtn"><input type="radio" name="av-14-t" id="av-14-soft" checked><span>Soft</span></label>
        <label class="av-14__segbtn"><input type="radio" name="av-14-t" id="av-14-solid"><span>Solid</span></label>
        <label class="av-14__segbtn"><input type="radio" name="av-14-t" id="av-14-ring"><span>Ringed</span></label>
      </fieldset>

      <ul class="av-14__grid">
        <li class="av-14__item">
          <span class="av-14__mono" style="--h:264" aria-hidden="true">PS</span>
          <span class="av-14__who"><span class="av-14__name">Priya Sharma</span><span class="av-14__meta">hue 264</span></span>
        </li>
        <li class="av-14__item">
          <span class="av-14__mono" style="--h:22" aria-hidden="true">AC</span>
          <span class="av-14__who"><span class="av-14__name">Alex Chen</span><span class="av-14__meta">hue 22</span></span>
        </li>
        <li class="av-14__item">
          <span class="av-14__mono" style="--h:152" aria-hidden="true">JL</span>
          <span class="av-14__who"><span class="av-14__name">Jordan Lee</span><span class="av-14__meta">hue 152</span></span>
        </li>
        <li class="av-14__item">
          <span class="av-14__mono" style="--h:198" aria-hidden="true">SR</span>
          <span class="av-14__who"><span class="av-14__name">Sam Rivera</span><span class="av-14__meta">hue 198</span></span>
        </li>
        <li class="av-14__item">
          <span class="av-14__mono" style="--h:96" aria-hidden="true">MO</span>
          <span class="av-14__who"><span class="av-14__name">Maya Okonkwo</span><span class="av-14__meta">hue 96</span></span>
        </li>
        <li class="av-14__item">
          <span class="av-14__mono" style="--h:318" aria-hidden="true">TB</span>
          <span class="av-14__who"><span class="av-14__name">Tom Bergström</span><span class="av-14__meta">hue 318</span></span>
        </li>
      </ul>

      <div class="av-14__mix">
        <p class="av-14__mixhead">Mixed with photos, same row</p>
        <ul class="av-14__stack" style="--n:5">
          <li class="av-14__stackitem" style="--i:0"><img class="av-14__img" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=200&auto=format&fit=facearea&facepad=2.5" alt="Priya Sharma" width="200" height="200" loading="lazy" decoding="async"></li>
          <li class="av-14__stackitem" style="--i:1"><span class="av-14__mono av-14__mono--sm" style="--h:22" aria-hidden="true">AC</span><span class="av-14__vh">Alex Chen</span></li>
          <li class="av-14__stackitem" style="--i:2"><img class="av-14__img" src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=200&auto=format&fit=facearea&facepad=2.5" alt="Jordan Lee" width="200" height="200" loading="lazy" decoding="async"></li>
          <li class="av-14__stackitem" style="--i:3"><span class="av-14__mono av-14__mono--sm" style="--h:152" aria-hidden="true">MO</span><span class="av-14__vh">Maya Okonkwo</span></li>
          <li class="av-14__stackitem" style="--i:4"><span class="av-14__mono av-14__mono--sm" style="--h:318" aria-hidden="true">TB</span><span class="av-14__vh">Tom Bergström</span></li>
        </ul>
      </div>
    </section>
  </div>
</div>
```
## CSS
```css
@supports (color: oklch(50% .1 250)) {
  .av-14 {
    --page: oklch(97.6% .004 265);
    --panel: oklch(100% 0 0);
    --panel-2: oklch(96.4% .006 265);
    --ink: oklch(20% .022 265);
    --muted: oklch(53% .022 265);
    --line: oklch(92% .008 265);
    --accent: oklch(58% .196 272);
  }

  .av-14__mono {
    background: oklch(93% .055 var(--h));
    color: oklch(44% .13 var(--h));
  }

  .av-14:has(#av-14-solid:checked) .av-14__mono {
    background: oklch(58% .16 var(--h));
    color: oklch(98% .01 var(--h));
  }

  .av-14:has(#av-14-ring:checked) .av-14__mono {
    background: var(--panel);
    color: oklch(46% .14 var(--h));
    box-shadow: 0 0 0 2px oklch(72% .13 var(--h)), 0 0 0 var(--sep) var(--panel);
  }
}

.av-14 {
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
  --size: clamp(3.25rem,9vw,4.25rem);
  --sep: 3px;
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

.av-14 *,
.av-14 *::before,
.av-14 *::after {
  box-sizing: border-box;
}

.av-14__vh {
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

.av-14__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  margin: 0;
  pointer-events: none;
}

.av-14__theme {
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

.av-14__theme::after {
  content: "";
  position: absolute;
  inset: -.4rem;
  border-radius: inherit;
}

.av-14__theme:hover {
  translate: 0 -1px;
}

.av-14__i {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.av-14__i--sun {
  display: none;
}

.av-14__sr:focus-visible + .av-14__theme {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.av-14__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
}

.av-14__wrap {
  inline-size: min(56rem,100%);
  display: flex;
  flex-direction: column;
  gap: clamp(1.1rem,2.6vw,1.6rem);
}

.av-14__head {
  display: flex;
  flex-direction: column;
  gap: .4rem;
  padding-inline-end: 3.5rem;
}

.av-14__eyebrow {
  margin: 0;
  font-size: .7rem;
  font-weight: 600;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.av-14__h {
  margin: 0;
  font-size: clamp(1.6rem,4.2vw,2.4rem);
  font-weight: 650;
  letter-spacing: -.03em;
  line-height: 1.05;
}

.av-14__sub {
  margin: 0;
  max-inline-size: 38rem;
  font-size: .95rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.av-14__seg {
  display: inline-flex;
  align-self: flex-start;
  gap: .15rem;
  margin: 0;
  padding: .25rem;
  border: 1px solid var(--line);
  border-radius: 999px;
  background: var(--panel);
  box-shadow: var(--shadow);
}

.av-14__segbtn {
  position: relative;
}

.av-14__segbtn input {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  margin: 0;
}

.av-14__segbtn span {
  display: grid;
  place-items: center;
  min-inline-size: 4.25rem;
  min-block-size: 2.25rem;
  padding: 0 .75rem;
  border-radius: 999px;
  font-size: .8rem;
  font-weight: 600;
  color: var(--muted);
  cursor: pointer;
  transition: background .18s ease, color .18s ease;
}

.av-14__segbtn:hover span {
  background: var(--panel-2);
}

.av-14__segbtn input:checked + span {
  background: var(--ink);
  color: var(--panel);
}

.av-14__segbtn input:focus-visible + span {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.av-14__grid {
  list-style: none;
  margin: 0;
  padding: clamp(1.35rem,3.5vw,2rem) clamp(1rem,3vw,1.75rem);
  display: grid;
  gap: clamp(1rem,2.5vw,1.5rem);
  grid-template-columns: repeat(auto-fit,minmax(11rem,1fr));
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: var(--r);
  box-shadow: var(--shadow);
}

.av-14__item {
  display: flex;
  align-items: center;
  gap: .85rem;
  min-inline-size: 0;
}

.av-14__mono {
  display: grid;
  place-items: center;
  inline-size: var(--size);
  aspect-ratio: 1;
  flex: none;
  border-radius: 50%;
  background: hsl(var(--h) 72% 92%);
  color: hsl(var(--h) 55% 30%);
  font-size: calc(var(--size) * .34);
  font-weight: 700;
  letter-spacing: .02em;
  text-transform: uppercase;
  transition: background .22s ease, color .22s ease, box-shadow .22s ease;
}

.av-14:has(#av-14-solid:checked) .av-14__mono {
  background: hsl(var(--h) 62% 45%);
  color: #fff;
}

.av-14:has(#av-14-ring:checked) .av-14__mono {
  background: var(--panel);
  color: hsl(var(--h) 55% 32%);
  box-shadow: 0 0 0 2px hsl(var(--h) 60% 62%), 0 0 0 var(--sep) var(--panel);
}

.av-14__who {
  display: flex;
  flex-direction: column;
  min-inline-size: 0;
}

.av-14__name {
  font-size: .95rem;
  font-weight: 600;
  letter-spacing: -.015em;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.av-14__meta {
  font-size: .76rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.av-14__mix {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 1rem 1.5rem;
  padding: 1rem 1.25rem;
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 14px;
}

.av-14__mixhead {
  margin: 0;
  font-size: .78rem;
  font-weight: 600;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: var(--muted);
}

.av-14__stack {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  align-items: center;
}

.av-14__stackitem {
  inline-size: 2.75rem;
  aspect-ratio: 1;
  flex: none;
  margin-inline-start: -.9rem;
  z-index: calc(var(--n) - var(--i));
  position: relative;
}

.av-14__stackitem:first-child {
  margin-inline-start: 0;
}

.av-14__stackitem:has(.av-14__mono) {
  z-index: calc(var(--n) + 1);
}

.av-14__img {
  display: block;
  inline-size: 100%;
  block-size: 100%;
  border-radius: 50%;
  object-fit: cover;
  object-position: center top;
  background: var(--panel-2);
  box-shadow: 0 0 0 var(--sep) var(--panel);
}

.av-14__mono--sm {
  --size: 2.75rem;
  box-shadow: 0 0 0 var(--sep) var(--panel);
}

.av-14:has(#av-14-dark:checked) {
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

.av-14:has(#av-14-dark:checked) .av-14__mono {
  background: hsl(var(--h) 42% 22%);
  color: hsl(var(--h) 78% 82%);
}

.av-14:has(#av-14-dark:checked) .av-14__i--moon {
  display: none;
}

.av-14:has(#av-14-dark:checked) .av-14__i--sun {
  display: block;
}

@supports (color: oklch(50% .1 250)) {
  .av-14:has(#av-14-dark:checked) .av-14__mono {
    background: oklch(30% .07 var(--h));
    color: oklch(88% .12 var(--h));
  }

  .av-14:has(#av-14-dark:checked):has(#av-14-solid:checked) .av-14__mono {
    background: oklch(60% .17 var(--h));
    color: oklch(16% .03 var(--h));
  }

  .av-14:has(#av-14-dark:checked):has(#av-14-ring:checked) .av-14__mono {
    background: var(--panel);
    color: oklch(85% .13 var(--h));
    box-shadow: 0 0 0 2px oklch(62% .15 var(--h)), 0 0 0 var(--sep) var(--panel);
  }
}

@media (prefers-color-scheme: dark) {
  .av-14:not(:has(#av-14-dark:checked)) {
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

  .av-14:not(:has(#av-14-dark:checked)) .av-14__mono {
    background: hsl(var(--h) 42% 22%);
    color: hsl(var(--h) 78% 82%);
  }

  .av-14:not(:has(#av-14-dark:checked)) .av-14__i--moon {
    display: none;
  }

  .av-14:not(:has(#av-14-dark:checked)) .av-14__i--sun {
    display: block;
  }

  @supports (color: oklch(50% .1 250)) {
    .av-14:not(:has(#av-14-dark:checked)) .av-14__mono {
      background: oklch(30% .07 var(--h));
      color: oklch(88% .12 var(--h));
    }

    .av-14:not(:has(#av-14-dark:checked)):has(#av-14-solid:checked) .av-14__mono {
      background: oklch(60% .17 var(--h));
      color: oklch(16% .03 var(--h));
    }

    .av-14:not(:has(#av-14-dark:checked)):has(#av-14-ring:checked) .av-14__mono {
      background: var(--panel);
      color: oklch(85% .13 var(--h));
      box-shadow: 0 0 0 2px oklch(62% .15 var(--h)), 0 0 0 var(--sep) var(--panel);
    }
  }
}

@media (prefers-reduced-motion: reduce) {
  .av-14 *,
    .av-14 *::before,
    .av-14 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .av-14__mono {
    background: Canvas;
    color: CanvasText;
    box-shadow: 0 0 0 1px CanvasText;
  }

  .av-14__grid,
    .av-14__mix,
    .av-14__seg,
    .av-14__theme {
    border-color: CanvasText;
  }
}
```
