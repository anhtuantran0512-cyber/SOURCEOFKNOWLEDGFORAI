---
source: "codefronts"
url: "https://codefronts.com/components/css-avatars/css-stacked-avatar-group-with-overlap/"
title: "CSS Stacked Avatar Group with Overlap"
section: "components"
category: "css-avatars"
category_name: "CSS Avatars"
description: "The canonical facepile, with the two details that separate a good one from a broken one: ring separation (a spread of surface colour so neighbours don't…"
has_js: "false"
---

Here's a working CSS Avatar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Stacked Avatar Group with Overlap
Source: https://codefronts.com/components/css-avatars/css-stacked-avatar-group-with-overlap/

The canonical facepile, with the two details that separate a good one from a broken one: ring separation (a spread of surface colour so neighbours don't smear together) and deliberate z-order so the first avatar sits on top instead of last-wins. Three densities (3, 5 and 8 faces) and a live overlap control, all in CSS — the stack tightens as the count grows, exactly as it should.
## HTML
```html
<div class="av-10">
  <input class="av-10__sr" type="checkbox" id="av-10-dark">
  <label class="av-10__theme" for="av-10-dark">
    <svg class="av-10__i av-10__i--moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.3A8.4 8.4 0 0 1 9.7 3.5a8.5 8.5 0 1 0 10.8 10.8Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="av-10__i av-10__i--sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.1" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.7 5.7l1.4 1.4M16.9 16.9l1.4 1.4M18.3 5.7l-1.4 1.4M7.1 16.9l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <span class="av-10__vh">Dark theme</span>
  </label>

  <div class="av-10__stage">
    <section class="av-10__wrap" aria-labelledby="av-10-h">
      <header class="av-10__head">
        <p class="av-10__eyebrow">Collaboration · Facepile</p>
        <h2 class="av-10__h" id="av-10-h">Stacked groups</h2>
        <p class="av-10__sub">First avatar on top, every face ringed in the surface colour.</p>
      </header>

      <fieldset class="av-10__seg">
        <legend class="av-10__vh">Overlap density</legend>
        <label class="av-10__segbtn"><input type="radio" name="av-10-d" id="av-10-cozy"><span>Cozy</span></label>
        <label class="av-10__segbtn"><input type="radio" name="av-10-d" id="av-10-snug" checked><span>Snug</span></label>
        <label class="av-10__segbtn"><input type="radio" name="av-10-d" id="av-10-tight"><span>Tight</span></label>
      </fieldset>

      <div class="av-10__panel">
        <div class="av-10__block">
          <p class="av-10__label">Reviewers <span>3</span></p>
          <ul class="av-10__group" style="--n:3" aria-label="3 reviewers on this pull request">
            <li class="av-10__item" style="--i:0"><img class="av-10__img" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=200&auto=format&fit=facearea&facepad=2.5" alt="Priya Sharma" width="200" height="200" loading="lazy" decoding="async"></li>
            <li class="av-10__item" style="--i:1"><img class="av-10__img" src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=200&auto=format&fit=facearea&facepad=2.5" alt="Alex Chen" width="200" height="200" loading="lazy" decoding="async"></li>
            <li class="av-10__item" style="--i:2"><img class="av-10__img" src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=200&auto=format&fit=facearea&facepad=2.5" alt="Maya Okonkwo" width="200" height="200" loading="lazy" decoding="async"></li>
          </ul>
        </div>

        <div class="av-10__block">
          <p class="av-10__label">Project team <span>5</span></p>
          <ul class="av-10__group" style="--n:5" aria-label="5 people in the Northwind project">
            <li class="av-10__item" style="--i:0"><img class="av-10__img" src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=200&auto=format&fit=facearea&facepad=2.5" alt="Jordan Lee" width="200" height="200" loading="lazy" decoding="async"></li>
            <li class="av-10__item" style="--i:1"><img class="av-10__img" src="https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=200&auto=format&fit=facearea&facepad=2.5" alt="Nadia Petrov" width="200" height="200" loading="lazy" decoding="async"></li>
            <li class="av-10__item" style="--i:2"><img class="av-10__img" src="https://images.unsplash.com/photo-1508214751196-bcfd4ca60f91?w=200&auto=format&fit=facearea&facepad=2.5" alt="Sam Rivera" width="200" height="200" loading="lazy" decoding="async"></li>
            <li class="av-10__item" style="--i:3"><img class="av-10__img" src="https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=200&auto=format&fit=facearea&facepad=2.5" alt="Hannah Wright" width="200" height="200" loading="lazy" decoding="async"></li>
            <li class="av-10__item" style="--i:4"><img class="av-10__img" src="https://images.unsplash.com/photo-1531427186611-ecfd6d936c79?w=200&auto=format&fit=facearea&facepad=2.5" alt="Marcus Hale" width="200" height="200" loading="lazy" decoding="async"></li>
          </ul>
        </div>

        <div class="av-10__block">
          <p class="av-10__label">Everyone in channel <span>8</span></p>
          <ul class="av-10__group" style="--n:8" aria-label="8 people in the design channel">
            <li class="av-10__item" style="--i:0"><img class="av-10__img" src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=200&auto=format&fit=facearea&facepad=2.5" alt="Grace Tan" width="200" height="200" loading="lazy" decoding="async"></li>
            <li class="av-10__item" style="--i:1"><img class="av-10__img" src="https://images.unsplash.com/photo-1521119989659-a83eee488004?w=200&auto=format&fit=facearea&facepad=2.5" alt="Daniel Osei" width="200" height="200" loading="lazy" decoding="async"></li>
            <li class="av-10__item" style="--i:2"><img class="av-10__img" src="https://images.unsplash.com/photo-1580489944761-15a19d654956?w=200&auto=format&fit=facearea&facepad=2.5" alt="Isabel Moreau" width="200" height="200" loading="lazy" decoding="async"></li>
            <li class="av-10__item" style="--i:3"><img class="av-10__img" src="https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?w=200&auto=format&fit=facearea&facepad=2.5" alt="Ethan Brooks" width="200" height="200" loading="lazy" decoding="async"></li>
            <li class="av-10__item" style="--i:4"><img class="av-10__img" src="https://images.unsplash.com/photo-1607746882042-944635dfe10e?w=200&auto=format&fit=facearea&facepad=2.5" alt="Zoe Alvarez" width="200" height="200" loading="lazy" decoding="async"></li>
            <li class="av-10__item" style="--i:5"><img class="av-10__img" src="https://images.unsplash.com/photo-1599566150163-29194dcaad36?w=200&auto=format&fit=facearea&facepad=2.5" alt="Omar Haddad" width="200" height="200" loading="lazy" decoding="async"></li>
            <li class="av-10__item" style="--i:6"><img class="av-10__img" src="https://images.unsplash.com/photo-1502685104226-ee32379fefbe?w=200&auto=format&fit=facearea&facepad=2.5" alt="Lucy Bennett" width="200" height="200" loading="lazy" decoding="async"></li>
            <li class="av-10__item" style="--i:7"><img class="av-10__img" src="https://images.unsplash.com/photo-1519345182560-3f2917c472ef?w=200&auto=format&fit=facearea&facepad=2.5" alt="Kai Nakamura" width="200" height="200" loading="lazy" decoding="async"></li>
          </ul>
        </div>
      </div>

      <p class="av-10__foot">Hover a face — it rises to the top of the stack instead of sliding underneath.</p>
    </section>
  </div>
</div>
```
## CSS
```css
@supports (color: oklch(50% .1 250)) {
  .av-10 {
    --page: oklch(97.6% .004 265);
    --panel: oklch(100% 0 0);
    --panel-2: oklch(96.4% .006 265);
    --ink: oklch(20% .022 265);
    --muted: oklch(53% .022 265);
    --line: oklch(92% .008 265);
    --accent: oklch(58% .196 272);
  }
}

.av-10 {
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

.av-10 *,
.av-10 *::before,
.av-10 *::after {
  box-sizing: border-box;
}

.av-10__vh {
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

.av-10__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  margin: 0;
  pointer-events: none;
}

.av-10__theme {
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

.av-10__theme::after {
  content: "";
  position: absolute;
  inset: -.4rem;
  border-radius: inherit;
}

.av-10__theme:hover {
  translate: 0 -1px;
}

.av-10__i {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.av-10__i--sun {
  display: none;
}

.av-10__sr:focus-visible + .av-10__theme {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.av-10__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
}

.av-10__wrap {
  inline-size: min(54rem,100%);
  display: flex;
  flex-direction: column;
  gap: clamp(1.1rem,2.6vw,1.75rem);
}

.av-10__head {
  display: flex;
  flex-direction: column;
  gap: .4rem;
  padding-inline-end: 3.5rem;
}

.av-10__eyebrow {
  margin: 0;
  font-size: .7rem;
  font-weight: 600;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.av-10__h {
  margin: 0;
  font-size: clamp(1.6rem,4.2vw,2.4rem);
  font-weight: 650;
  letter-spacing: -.03em;
  line-height: 1.05;
}

.av-10__sub {
  margin: 0;
  max-inline-size: 36rem;
  font-size: .95rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.av-10__seg {
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

.av-10__segbtn {
  position: relative;
}

.av-10__segbtn input {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  margin: 0;
}

.av-10__segbtn span {
  display: grid;
  place-items: center;
  min-inline-size: 4rem;
  min-block-size: 2.25rem;
  padding: 0 .7rem;
  border-radius: 999px;
  font-size: .8rem;
  font-weight: 600;
  color: var(--muted);
  cursor: pointer;
  transition: background .18s ease, color .18s ease;
}

.av-10__segbtn:hover span {
  background: var(--panel-2);
}

.av-10__segbtn input:checked + span {
  background: var(--ink);
  color: var(--panel);
}

.av-10__segbtn input:focus-visible + span {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.av-10__panel {
  display: flex;
  flex-direction: column;
  gap: clamp(1.25rem,3vw,2rem);
  padding: clamp(1.5rem,4vw,2.25rem);
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: var(--r);
  box-shadow: var(--shadow);
}

.av-10__block {
  display: flex;
  flex-direction: column;
  gap: .6rem;
}

.av-10__label {
  margin: 0;
  display: flex;
  align-items: center;
  gap: .5rem;
  font-size: .78rem;
  font-weight: 600;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: var(--muted);
}

.av-10__label span {
  padding: .1rem .4rem;
  border-radius: 999px;
  background: var(--panel-2);
  color: var(--ink);
  font-variant-numeric: tabular-nums;
  letter-spacing: 0;
}

.av-10__group {
  --size: clamp(2.75rem,7vw,3.5rem);
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  align-items: center;
}

.av-10__item {
  inline-size: var(--size);
  aspect-ratio: 1;
  flex: none;
  margin-inline-start: calc(var(--size) * var(--dens) * -1);
  z-index: calc(var(--n) - var(--i));
  transition: translate .22s cubic-bezier(.2,.7,.3,1), margin .28s ease;
}

.av-10__item:first-child {
  margin-inline-start: 0;
}

.av-10__item:hover {
  z-index: calc(var(--n) + 1);
  translate: 0 -5px;
}

.av-10__img {
  display: block;
  inline-size: 100%;
  block-size: 100%;
  border-radius: 50%;
  object-fit: cover;
  object-position: center top;
  background: var(--panel-2);
  box-shadow: 0 0 0 var(--sep) var(--panel);
}

.av-10__foot {
  margin: 0;
  font-size: .82rem;
  color: var(--muted);
}

.av-10:has(#av-10-cozy:checked) {
  --dens: .2;
}

.av-10:has(#av-10-tight:checked) {
  --dens: .46;
}

.av-10:has(#av-10-dark:checked) {
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

.av-10:has(#av-10-dark:checked) .av-10__i--moon {
  display: none;
}

.av-10:has(#av-10-dark:checked) .av-10__i--sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .av-10:not(:has(#av-10-dark:checked)) {
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

  .av-10:not(:has(#av-10-dark:checked)) .av-10__i--moon {
    display: none;
  }

  .av-10:not(:has(#av-10-dark:checked)) .av-10__i--sun {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .av-10 *,
    .av-10 *::before,
    .av-10 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .av-10__img {
    box-shadow: 0 0 0 2px Canvas, 0 0 0 3px CanvasText;
  }

  .av-10__segbtn input:checked + span {
    background: Highlight;
    color: HighlightText;
  }

  .av-10__panel,
    .av-10__seg,
    .av-10__theme {
    border-color: CanvasText;
  }
}
```
