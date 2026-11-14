---
source: "codefronts"
url: "https://codefronts.com/components/css-avatars/css-squircle-avatar/"
title: "CSS Squircle Avatar"
section: "components"
category: "css-avatars"
category_name: "CSS Avatars"
description: "The iOS/Figma superellipse, now a real CSS corner shape."
has_js: "false"
---

Here's a working CSS Avatar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Squircle Avatar
Source: https://codefronts.com/components/css-avatars/css-squircle-avatar/

The iOS/Figma superellipse, now a real CSS corner shape. corner-shape: squircle curves the corner continuously instead of arcing it, which is why an app icon looks softer than a border-radius rectangle at the same radius. The demo puts squircle and plain rounded-rect side by side at matched radii so the difference actually reads, and a radio group cycles every corner-shape value — round, squircle, bevel, notch, scoop — with a tuned border-radius: 30% fallback everywhere the property is unsupported.
## HTML
```html
<div class="av-02">
  <input class="av-02__sr" type="checkbox" id="av-02-dark">
  <label class="av-02__theme" for="av-02-dark">
    <svg class="av-02__i av-02__i--moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.3A8.4 8.4 0 0 1 9.7 3.5a8.5 8.5 0 1 0 10.8 10.8Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="av-02__i av-02__i--sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.1" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.7 5.7l1.4 1.4M16.9 16.9l1.4 1.4M18.3 5.7l-1.4 1.4M7.1 16.9l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <span class="av-02__vh">Dark theme</span>
  </label>

  <div class="av-02__stage">
    <section class="av-02__wrap" aria-labelledby="av-02-h">
      <header class="av-02__head">
        <p class="av-02__eyebrow">Identity · Avatar</p>
        <h2 class="av-02__h" id="av-02-h">Squircle corners</h2>
        <p class="av-02__sub">Continuous curvature, not a spliced arc — the same corner language iOS and Figma use.</p>
      </header>

      <div class="av-02__compare">
        <figure class="av-02__cell">
          <span class="av-02__fig av-02__fig--squircle">
            <img class="av-02__img" src="https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=200&auto=format&fit=facearea&facepad=2.5" alt="Nadia Petrov" width="200" height="200" loading="lazy" decoding="async">
          </span>
          <figcaption class="av-02__cap"><strong>Squircle</strong><span>corner-shape: squircle</span></figcaption>
        </figure>
        <figure class="av-02__cell">
          <span class="av-02__fig av-02__fig--round">
            <img class="av-02__img" src="https://images.unsplash.com/photo-1521119989659-a83eee488004?w=200&auto=format&fit=facearea&facepad=2.5" alt="Daniel Osei" width="200" height="200" loading="lazy" decoding="async">
          </span>
          <figcaption class="av-02__cap"><strong>Rounded rect</strong><span>border-radius only</span></figcaption>
        </figure>
      </div>

      <fieldset class="av-02__seg">
        <legend class="av-02__vh">Corner shape</legend>
        <label class="av-02__segbtn"><input type="radio" name="av-02-s" id="av-02-sq" checked><span>Squircle</span></label>
        <label class="av-02__segbtn"><input type="radio" name="av-02-s" id="av-02-rd"><span>Round</span></label>
        <label class="av-02__segbtn"><input type="radio" name="av-02-s" id="av-02-bv"><span>Bevel</span></label>
        <label class="av-02__segbtn"><input type="radio" name="av-02-s" id="av-02-nt"><span>Notch</span></label>
        <label class="av-02__segbtn"><input type="radio" name="av-02-s" id="av-02-sc"><span>Scoop</span></label>
      </fieldset>

      <ul class="av-02__grid">
        <li class="av-02__member">
          <span class="av-02__fig av-02__fig--live"><img class="av-02__img" src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=200&auto=format&fit=facearea&facepad=2.5" alt="Grace Tan" width="200" height="200" loading="lazy" decoding="async"></span>
          <span class="av-02__who"><span class="av-02__name">Grace Tan</span><span class="av-02__role">Design lead</span></span>
        </li>
        <li class="av-02__member">
          <span class="av-02__fig av-02__fig--live"><img class="av-02__img" src="https://images.unsplash.com/photo-1531427186611-ecfd6d936c79?w=200&auto=format&fit=facearea&facepad=2.5" alt="Marcus Hale" width="200" height="200" loading="lazy" decoding="async"></span>
          <span class="av-02__who"><span class="av-02__name">Marcus Hale</span><span class="av-02__role">iOS engineer</span></span>
        </li>
        <li class="av-02__member">
          <span class="av-02__fig av-02__fig--live"><img class="av-02__img" src="https://images.unsplash.com/photo-1580489944761-15a19d654956?w=200&auto=format&fit=facearea&facepad=2.5" alt="Isabel Moreau" width="200" height="200" loading="lazy" decoding="async"></span>
          <span class="av-02__who"><span class="av-02__name">Isabel Moreau</span><span class="av-02__role">Brand systems</span></span>
        </li>
        <li class="av-02__member">
          <span class="av-02__fig av-02__fig--live"><img class="av-02__img" src="https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?w=200&auto=format&fit=facearea&facepad=2.5" alt="Ethan Brooks" width="200" height="200" loading="lazy" decoding="async"></span>
          <span class="av-02__who"><span class="av-02__name">Ethan Brooks</span><span class="av-02__role">Platform</span></span>
        </li>
      </ul>
      <p class="av-02__foot" id="av-02-note">Unsupported browsers fall back to <code>border-radius: 30%</code>.</p>
    </section>
  </div>
</div>
```
## CSS
```css
@supports (color: oklch(50% .1 250)) {
  .av-02 {
    --page: oklch(97.6% .004 265);
    --panel: oklch(100% 0 0);
    --panel-2: oklch(96.4% .006 265);
    --ink: oklch(20% .022 265);
    --muted: oklch(53% .022 265);
    --line: oklch(92% .008 265);
    --accent: oklch(56% .17 250);
  }
}

.av-02 {
  --page: #f7f8fa;
  --panel: #ffffff;
  --panel-2: #f1f3f7;
  --ink: #10131a;
  --muted: #5f6672;
  --line: #e4e7ee;
  --accent: #2563eb;
  --glass: rgba(255,255,255,.68);
  --shadow: 0 1px 2px rgba(16,19,26,.05), 0 16px 36px -20px rgba(16,19,26,.3);
  --r: 18px;
  --shape: squircle;
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

.av-02 *,
.av-02 *::before,
.av-02 *::after {
  box-sizing: border-box;
}

.av-02__vh {
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

.av-02__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  margin: 0;
  pointer-events: none;
}

.av-02__theme {
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

.av-02__theme::after {
  content: "";
  position: absolute;
  inset: -.4rem;
  border-radius: inherit;
}

.av-02__theme:hover {
  translate: 0 -1px;
}

.av-02__i {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.av-02__i--sun {
  display: none;
}

.av-02__sr:focus-visible + .av-02__theme {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.av-02__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
}

.av-02__wrap {
  inline-size: min(58rem,100%);
  display: flex;
  flex-direction: column;
  gap: clamp(1.25rem,3vw,2rem);
}

.av-02__head {
  display: flex;
  flex-direction: column;
  gap: .4rem;
  padding-inline-end: 3.5rem;
}

.av-02__eyebrow {
  margin: 0;
  font-size: .7rem;
  font-weight: 600;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.av-02__h {
  margin: 0;
  font-size: clamp(1.6rem,4.2vw,2.4rem);
  font-weight: 650;
  letter-spacing: -.03em;
  line-height: 1.05;
}

.av-02__sub {
  margin: 0;
  max-inline-size: 36rem;
  font-size: .95rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.av-02__compare {
  display: grid;
  gap: clamp(1rem,3vw,2rem);
  grid-template-columns: repeat(auto-fit,minmax(11rem,1fr));
  padding: clamp(1.5rem,4vw,2.5rem);
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: var(--r);
  box-shadow: var(--shadow);
}

.av-02__cell {
  margin: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: .85rem;
}

.av-02__cap {
  display: flex;
  flex-direction: column;
  gap: .15rem;
  align-items: center;
  text-align: center;
}

.av-02__cap strong {
  font-size: .95rem;
  font-weight: 600;
}

.av-02__cap span {
  font-size: .7rem;
  font-family: ui-monospace,SFMono-Regular,Menlo,monospace;
  color: var(--muted);
}

.av-02__fig {
  position: relative;
  display: block;
  inline-size: clamp(5.5rem,16vw,8.5rem);
  aspect-ratio: 1;
  border-radius: 30%;
  overflow: hidden;
  background: var(--panel-2);
  box-shadow: inset 0 0 0 1px rgba(16,19,26,.08);
  transition: translate .25s cubic-bezier(.2,.7,.3,1);
}

.av-02__cell:hover .av-02__fig {
  translate: 0 -4px;
}

.av-02__img {
  display: block;
  inline-size: 100%;
  block-size: 100%;
  object-fit: cover;
  object-position: center top;
}

.av-02__fig--round {
  border-radius: 22%;
}

.av-02__seg {
  display: flex;
  flex-wrap: wrap;
  align-self: flex-start;
  gap: .15rem;
  margin: 0;
  padding: .25rem;
  border: 1px solid var(--line);
  border-radius: 999px;
  background: var(--panel);
  box-shadow: var(--shadow);
}

.av-02__segbtn {
  position: relative;
}

.av-02__segbtn input {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  margin: 0;
}

.av-02__segbtn span {
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

.av-02__segbtn:hover span {
  background: var(--panel-2);
}

.av-02__segbtn input:checked + span {
  background: var(--ink);
  color: var(--panel);
}

.av-02__segbtn input:focus-visible + span {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.av-02__grid {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: .5rem;
  grid-template-columns: repeat(auto-fit,minmax(13rem,1fr));
}

.av-02__member {
  display: flex;
  align-items: center;
  gap: .85rem;
  padding: .7rem .85rem;
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 14px;
  transition: border-color .2s ease;
}

.av-02__member:hover {
  border-color: var(--accent);
}

.av-02__fig--live {
  inline-size: 2.75rem;
  border-radius: 30%;
}

.av-02__who {
  display: flex;
  flex-direction: column;
  min-inline-size: 0;
}

.av-02__name {
  font-size: .9rem;
  font-weight: 600;
  letter-spacing: -.01em;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.av-02__role {
  font-size: .78rem;
  color: var(--muted);
}

.av-02__foot {
  margin: 0;
  font-size: .82rem;
  color: var(--muted);
}

.av-02__foot code {
  font-size: .78rem;
  padding: .1rem .3rem;
  border-radius: 5px;
  background: var(--panel-2);
}

@supports (corner-shape: squircle) {
  .av-02__fig {
    border-radius: 42%;
    corner-shape: var(--shape);
  }

  .av-02__fig--round {
    border-radius: 26%;
    corner-shape: round;
  }

  .av-02__fig--live {
    border-radius: 44%;
  }

  .av-02:has(#av-02-rd:checked) {
    --shape: round;
  }

  .av-02:has(#av-02-bv:checked) {
    --shape: bevel;
  }

  .av-02:has(#av-02-nt:checked) {
    --shape: notch;
  }

  .av-02:has(#av-02-sc:checked) {
    --shape: scoop;
  }

  .av-02__foot {
    visibility: hidden;
  }
}

.av-02:has(#av-02-dark:checked) {
  --page: #0a0b0e;
  --panel: #14161c;
  --panel-2: #1c1f27;
  --ink: #f2f4f9;
  --muted: #98a0b0;
  --line: #262a33;
  --accent: #7aa2ff;
  --glass: rgba(255,255,255,.07);
  --shadow: 0 1px 2px rgba(0,0,0,.6), 0 20px 44px -24px rgba(0,0,0,.85);
}

.av-02:has(#av-02-dark:checked) .av-02__fig {
  box-shadow: inset 0 0 0 1px rgba(255,255,255,.1);
}

.av-02:has(#av-02-dark:checked) .av-02__i--moon {
  display: none;
}

.av-02:has(#av-02-dark:checked) .av-02__i--sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .av-02:not(:has(#av-02-dark:checked)) {
    --page: #0a0b0e;
    --panel: #14161c;
    --panel-2: #1c1f27;
    --ink: #f2f4f9;
    --muted: #98a0b0;
    --line: #262a33;
    --accent: #7aa2ff;
    --glass: rgba(255,255,255,.07);
    --shadow: 0 1px 2px rgba(0,0,0,.6), 0 20px 44px -24px rgba(0,0,0,.85);
  }

  .av-02:not(:has(#av-02-dark:checked)) .av-02__fig {
    box-shadow: inset 0 0 0 1px rgba(255,255,255,.1);
  }

  .av-02:not(:has(#av-02-dark:checked)) .av-02__i--moon {
    display: none;
  }

  .av-02:not(:has(#av-02-dark:checked)) .av-02__i--sun {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .av-02 *,
    .av-02 *::before,
    .av-02 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .av-02__fig {
    box-shadow: none;
    outline: 2px solid CanvasText;
  }

  .av-02__segbtn input:checked + span {
    background: Highlight;
    color: HighlightText;
  }

  .av-02__compare,
    .av-02__member,
    .av-02__seg,
    .av-02__theme {
    border-color: CanvasText;
  }
}
```
