---
source: "codefronts"
url: "https://codefronts.com/components/css-avatars/css-avatar-picker-grid/"
title: "CSS Avatar Picker Grid"
section: "components"
category: "css-avatars"
category_name: "CSS Avatars"
description: "Choose-your-avatar, done with real form controls: eight options as a radio group, so arrow keys move between them, Space selects, and the browser handles the…"
has_js: "false"
---

Here's a working CSS Avatar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Avatar Picker Grid
Source: https://codefronts.com/components/css-avatars/css-avatar-picker-grid/

Choose-your-avatar, done with real form controls: eight options as a radio group, so arrow keys move between them, Space selects, and the browser handles the roving focus for free. The :checked state paints a ring plus a tick badge — two signals, not just colour — and a live preview at the top updates through :has(). Entirely CSS; the only thing a real app adds is reading .value on submit.
## HTML
```html
<div class="av-19">
  <input class="av-19__sr" type="checkbox" id="av-19-dark">
  <label class="av-19__theme" for="av-19-dark">
    <svg class="av-19__i av-19__i--moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.3A8.4 8.4 0 0 1 9.7 3.5a8.5 8.5 0 1 0 10.8 10.8Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="av-19__i av-19__i--sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.1" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.7 5.7l1.4 1.4M16.9 16.9l1.4 1.4M18.3 5.7l-1.4 1.4M7.1 16.9l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <span class="av-19__vh">Dark theme</span>
  </label>

  <div class="av-19__stage">
    <section class="av-19__wrap" aria-labelledby="av-19-h">
      <header class="av-19__head">
        <p class="av-19__eyebrow">Onboarding · Step 2 of 4</p>
        <h2 class="av-19__h" id="av-19-h">Pick your avatar</h2>
        <p class="av-19__sub">Arrow keys move, Space selects. Selection shows a ring and a tick, never colour alone.</p>
      </header>

      <div class="av-19__previewbar">
        <span class="av-19__pvempty" aria-hidden="true">
          <svg viewBox="0 0 24 24" fill="none" focusable="false"><circle cx="12" cy="9" r="3.6" stroke="currentColor" stroke-width="1.7"/><path d="M5.5 19.5c1.2-3.1 3.6-4.6 6.5-4.6s5.3 1.5 6.5 4.6" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
        </span>
        <span class="av-19__pv av-19__pv--1"><img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=200&auto=format&fit=facearea&facepad=2.5" alt="Selected avatar: portrait one" width="200" height="200" loading="lazy" decoding="async"></span>
        <span class="av-19__pv av-19__pv--2"><img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=200&auto=format&fit=facearea&facepad=2.5" alt="Selected avatar: portrait two" width="200" height="200" loading="lazy" decoding="async"></span>
        <span class="av-19__pv av-19__pv--3"><img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=200&auto=format&fit=facearea&facepad=2.5" alt="Selected avatar: portrait three" width="200" height="200" loading="lazy" decoding="async"></span>
        <span class="av-19__pv av-19__pv--4"><img src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=200&auto=format&fit=facearea&facepad=2.5" alt="Selected avatar: portrait four" width="200" height="200" loading="lazy" decoding="async"></span>
        <span class="av-19__pv av-19__pv--5"><img src="https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=200&auto=format&fit=facearea&facepad=2.5" alt="Selected avatar: portrait five" width="200" height="200" loading="lazy" decoding="async"></span>
        <span class="av-19__pv av-19__pv--6"><img src="https://images.unsplash.com/photo-1508214751196-bcfd4ca60f91?w=200&auto=format&fit=facearea&facepad=2.5" alt="Selected avatar: portrait six" width="200" height="200" loading="lazy" decoding="async"></span>
        <span class="av-19__pv av-19__pv--7 av-19__pv--mono" style="--h:264" aria-hidden="true">MO</span>
        <span class="av-19__pv av-19__pv--8 av-19__pv--mono" style="--h:152" aria-hidden="true">TB</span>
        <span class="av-19__pvtext">
          <span class="av-19__pvname">Your avatar</span>
          <span class="av-19__pvstate" aria-live="polite">
            <span class="av-19__st av-19__st--none">Nothing selected yet</span>
            <span class="av-19__st av-19__st--some">Selected — you can change it any time</span>
          </span>
        </span>
      </div>

      <fieldset class="av-19__grid">
        <legend class="av-19__legend">Choose your avatar</legend>
        <label class="av-19__opt"><input type="radio" name="av-19-pick" id="av-19-o1" value="1">
          <span class="av-19__frame"><img class="av-19__img" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=200&auto=format&fit=facearea&facepad=2.5" alt="Portrait one" width="200" height="200" loading="lazy" decoding="async"><span class="av-19__tick" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M6 12.5l3.6 3.5L18 8" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg></span></span>
        </label>
        <label class="av-19__opt"><input type="radio" name="av-19-pick" id="av-19-o2" value="2">
          <span class="av-19__frame"><img class="av-19__img" src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=200&auto=format&fit=facearea&facepad=2.5" alt="Portrait two" width="200" height="200" loading="lazy" decoding="async"><span class="av-19__tick" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M6 12.5l3.6 3.5L18 8" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg></span></span>
        </label>
        <label class="av-19__opt"><input type="radio" name="av-19-pick" id="av-19-o3" value="3">
          <span class="av-19__frame"><img class="av-19__img" src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=200&auto=format&fit=facearea&facepad=2.5" alt="Portrait three" width="200" height="200" loading="lazy" decoding="async"><span class="av-19__tick" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M6 12.5l3.6 3.5L18 8" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg></span></span>
        </label>
        <label class="av-19__opt"><input type="radio" name="av-19-pick" id="av-19-o4" value="4">
          <span class="av-19__frame"><img class="av-19__img" src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=200&auto=format&fit=facearea&facepad=2.5" alt="Portrait four" width="200" height="200" loading="lazy" decoding="async"><span class="av-19__tick" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M6 12.5l3.6 3.5L18 8" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg></span></span>
        </label>
        <label class="av-19__opt"><input type="radio" name="av-19-pick" id="av-19-o5" value="5">
          <span class="av-19__frame"><img class="av-19__img" src="https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=200&auto=format&fit=facearea&facepad=2.5" alt="Portrait five" width="200" height="200" loading="lazy" decoding="async"><span class="av-19__tick" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M6 12.5l3.6 3.5L18 8" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg></span></span>
        </label>
        <label class="av-19__opt"><input type="radio" name="av-19-pick" id="av-19-o6" value="6">
          <span class="av-19__frame"><img class="av-19__img" src="https://images.unsplash.com/photo-1508214751196-bcfd4ca60f91?w=200&auto=format&fit=facearea&facepad=2.5" alt="Portrait six" width="200" height="200" loading="lazy" decoding="async"><span class="av-19__tick" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M6 12.5l3.6 3.5L18 8" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg></span></span>
        </label>
        <label class="av-19__opt"><input type="radio" name="av-19-pick" id="av-19-o7" value="mono-mo">
          <span class="av-19__frame av-19__frame--mono" style="--h:264"><span class="av-19__mono" aria-hidden="true">MO</span><span class="av-19__vh">Monogram, violet</span><span class="av-19__tick" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M6 12.5l3.6 3.5L18 8" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg></span></span>
        </label>
        <label class="av-19__opt"><input type="radio" name="av-19-pick" id="av-19-o8" value="mono-tb">
          <span class="av-19__frame av-19__frame--mono" style="--h:152"><span class="av-19__mono" aria-hidden="true">TB</span><span class="av-19__vh">Monogram, green</span><span class="av-19__tick" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M6 12.5l3.6 3.5L18 8" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg></span></span>
        </label>
      </fieldset>
    </section>
  </div>
</div>
```
## CSS
```css
@supports (color: oklch(50% .1 250)) {
  .av-19 {
    --page: oklch(97.6% .004 265);
    --panel: oklch(100% 0 0);
    --panel-2: oklch(96.4% .006 265);
    --ink: oklch(20% .022 265);
    --muted: oklch(53% .022 265);
    --line: oklch(92% .008 265);
    --accent: oklch(58% .196 272);
  }

  .av-19__frame--mono,
    .av-19__pv--mono {
    background: oklch(93% .055 var(--h));
    color: oklch(44% .13 var(--h));
  }
}

.av-19 {
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

.av-19 *,
.av-19 *::before,
.av-19 *::after {
  box-sizing: border-box;
}

.av-19__vh {
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

.av-19__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  margin: 0;
  pointer-events: none;
}

.av-19__theme {
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

.av-19__theme::after {
  content: "";
  position: absolute;
  inset: -.4rem;
  border-radius: inherit;
}

.av-19__theme:hover {
  translate: 0 -1px;
}

.av-19__i {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.av-19__i--sun {
  display: none;
}

.av-19__sr:focus-visible + .av-19__theme {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.av-19__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
}

.av-19__wrap {
  inline-size: min(52rem,100%);
  display: flex;
  flex-direction: column;
  gap: clamp(1.1rem,2.6vw,1.6rem);
}

.av-19__head {
  display: flex;
  flex-direction: column;
  gap: .4rem;
  padding-inline-end: 3.5rem;
}

.av-19__eyebrow {
  margin: 0;
  font-size: .7rem;
  font-weight: 600;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.av-19__h {
  margin: 0;
  font-size: clamp(1.6rem,4.2vw,2.4rem);
  font-weight: 650;
  letter-spacing: -.03em;
  line-height: 1.05;
}

.av-19__sub {
  margin: 0;
  max-inline-size: 36rem;
  font-size: .95rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.av-19__previewbar {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem 1.25rem;
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 14px;
  box-shadow: var(--shadow);
}

.av-19__pv {
  display: none;
  inline-size: 3.5rem;
  aspect-ratio: 1;
  border-radius: 50%;
  overflow: hidden;
  flex: none;
  box-shadow: 0 0 0 3px var(--panel), 0 0 0 5px var(--accent);
}

.av-19__pv img {
  display: block;
  inline-size: 100%;
  block-size: 100%;
  object-fit: cover;
  object-position: center top;
}

.av-19__pv--mono {
  display: none;
  place-items: center;
  background: hsl(var(--h) 72% 92%);
  color: hsl(var(--h) 55% 30%);
  font-size: 1.15rem;
  font-weight: 700;
}

.av-19__pvempty {
  display: grid;
  place-items: center;
  inline-size: 3.5rem;
  aspect-ratio: 1;
  border-radius: 50%;
  background: var(--panel-2);
  color: var(--muted);
  flex: none;
}

.av-19__pvempty svg {
  inline-size: 1.6rem;
  block-size: 1.6rem;
}

.av-19:has(input[name="av-19-pick"]:checked) .av-19__pvempty {
  display: none;
}

.av-19__pvtext {
  display: flex;
  flex-direction: column;
  gap: .1rem;
}

.av-19__pvname {
  font-size: .95rem;
  font-weight: 650;
  letter-spacing: -.015em;
}

.av-19__pvstate {
  font-size: .8rem;
  color: var(--muted);
}

.av-19__st {
  display: none;
}

.av-19__st--none {
  display: inline;
}

.av-19__grid {
  margin: 0;
  padding: clamp(1.35rem,3.5vw,2rem) clamp(1rem,3vw,1.75rem);
  border: 1px solid var(--line);
  border-radius: var(--r);
  background: var(--panel);
  box-shadow: var(--shadow);
  display: grid;
  gap: clamp(1rem,2.5vw,1.5rem);
  grid-template-columns: repeat(auto-fit,minmax(4.5rem,1fr));
}

.av-19__legend {
  padding: 0 .4rem;
  font-size: .72rem;
  font-weight: 600;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--muted);
}

.av-19__opt {
  position: relative;
  display: block;
  min-inline-size: 2.75rem;
  min-block-size: 2.75rem;
}

.av-19__opt input {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  margin: 0;
  inset-block-start: 50%;
  inset-inline-start: 50%;
}

.av-19__frame {
  position: relative;
  display: grid;
  place-items: center;
  inline-size: 100%;
  aspect-ratio: 1;
  border-radius: 50%;
  overflow: visible;
  cursor: pointer;
  background: var(--panel-2);
  box-shadow: 0 0 0 1px rgba(16,19,26,.08);
  transition: box-shadow .2s ease, translate .2s cubic-bezier(.2,.7,.3,1);
}

.av-19__opt:hover .av-19__frame {
  translate: 0 -3px;
}

.av-19__img {
  display: block;
  inline-size: 100%;
  block-size: 100%;
  border-radius: 50%;
  object-fit: cover;
  object-position: center top;
}

.av-19__frame--mono {
  background: hsl(var(--h) 72% 92%);
  color: hsl(var(--h) 55% 30%);
}

.av-19__mono {
  font-size: calc(1rem + .6vw);
  font-weight: 700;
  letter-spacing: .02em;
}

.av-19__tick {
  position: absolute;
  inset-block-end: -2%;
  inset-inline-end: -2%;
  z-index: 2;
  display: grid;
  place-items: center;
  inline-size: 38%;
  aspect-ratio: 1;
  border-radius: 50%;
  background: var(--accent);
  color: #fff;
  box-shadow: 0 0 0 3px var(--panel);
  opacity: 0;
  scale: .5;
  transition: opacity .2s ease, scale .22s cubic-bezier(.2,.9,.3,1.3);
}

.av-19__tick svg {
  inline-size: 62%;
  block-size: 62%;
}

.av-19__opt input:checked + .av-19__frame {
  box-shadow: 0 0 0 3px var(--panel), 0 0 0 6px var(--accent);
}

.av-19__opt input:checked + .av-19__frame .av-19__tick {
  opacity: 1;
  scale: 1;
}

.av-19__opt input:focus-visible + .av-19__frame {
  outline: 2px solid var(--ink);
  outline-offset: 7px;
}

.av-19:has(#av-19-o1:checked) .av-19__pv--1,
.av-19:has(#av-19-o2:checked) .av-19__pv--2,
.av-19:has(#av-19-o3:checked) .av-19__pv--3,
.av-19:has(#av-19-o4:checked) .av-19__pv--4,
.av-19:has(#av-19-o5:checked) .av-19__pv--5,
.av-19:has(#av-19-o6:checked) .av-19__pv--6 {
  display: block;
}

.av-19:has(#av-19-o7:checked) .av-19__pv--7,
.av-19:has(#av-19-o8:checked) .av-19__pv--8 {
  display: grid;
}

.av-19:has(input[name="av-19-pick"]:checked) .av-19__st--none {
  display: none;
}

.av-19:has(input[name="av-19-pick"]:checked) .av-19__st--some {
  display: inline;
}

.av-19:has(#av-19-dark:checked) {
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

.av-19:has(#av-19-dark:checked) .av-19__frame--mono,
.av-19:has(#av-19-dark:checked) .av-19__pv--mono {
  background: hsl(var(--h) 42% 22%);
  color: hsl(var(--h) 78% 82%);
}

.av-19:has(#av-19-dark:checked) .av-19__tick {
  color: #0a0b0e;
}

.av-19:has(#av-19-dark:checked) .av-19__i--moon {
  display: none;
}

.av-19:has(#av-19-dark:checked) .av-19__i--sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .av-19:not(:has(#av-19-dark:checked)) {
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

  .av-19:not(:has(#av-19-dark:checked)) .av-19__frame--mono,
    .av-19:not(:has(#av-19-dark:checked)) .av-19__pv--mono {
    background: hsl(var(--h) 42% 22%);
    color: hsl(var(--h) 78% 82%);
  }

  .av-19:not(:has(#av-19-dark:checked)) .av-19__tick {
    color: #0a0b0e;
  }

  .av-19:not(:has(#av-19-dark:checked)) .av-19__i--moon {
    display: none;
  }

  .av-19:not(:has(#av-19-dark:checked)) .av-19__i--sun {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .av-19 *,
    .av-19 *::before,
    .av-19 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .av-19__opt input:checked + .av-19__frame {
    outline: 3px solid Highlight;
    outline-offset: 3px;
  }

  .av-19__tick {
    background: Highlight;
    color: HighlightText;
  }

  .av-19__grid,
    .av-19__previewbar,
    .av-19__theme {
    border-color: CanvasText;
  }
}
```
