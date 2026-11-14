---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-glassmorphism/adaptive-dark-and-light-glass/"
title: "Adaptive Dark and Light Glass"
section: "design-styles"
category: "css-glassmorphism"
category_name: "CSS Glassmorphism"
description: "One glass component, two sets of physics."
has_js: "false"
---

Here's a working CSS Glassmorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Adaptive Dark and Light Glass
Source: https://codefronts.com/design-styles/css-glassmorphism/adaptive-dark-and-light-glass/

One glass component, two sets of physics. Flip the surrounding theme and the panel does not just recolour — it re-tunes: light mode drops to blur(12px) with saturate(200%) over a white overlay, dark mode climbs to blur(24px) saturate(140%) over a black one. Same markup, inverted blur maths, driven entirely by custom properties.
## HTML
```html
<div class="gm-08">
  <input class="gm-08__sr" type="checkbox" id="gm-08-theme">
  <label class="gm-08__theme" for="gm-08-theme" title="Switch surface theme">
    <svg class="gm-08__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="gm-08__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="gm-08__vh">Switch light or dark surface</span>
  </label>

  <div class="gm-08__stage">
    <section class="gm-08__wrap" aria-labelledby="gm-08-h">
      <header class="gm-08__head">
        <p class="gm-08__eyebrow">one component · two physics</p>
        <h2 class="gm-08__h" id="gm-08-h">Glass has to re-tune, not just recolour</h2>
        <p class="gm-08__sub">Flip the surface. Watch the blur drop and the saturation climb — the same card, adapting its maths to the scene behind it.</p>
        <label class="gm-08__switch" for="gm-08-theme">
          <span class="gm-08__track" aria-hidden="true"><span class="gm-08__thumb"></span></span>
          <span class="gm-08__slabel"><span class="gm-08__son">Light surface</span><span class="gm-08__soff">Dark surface</span></span>
        </label>
      </header>

      <article class="gm-08__card">
        <div class="gm-08__cardtop">
          <span class="gm-08__avatar" aria-hidden="true">JL</span>
          <div>
            <h3 class="gm-08__name">Jordan Lee</h3>
            <p class="gm-08__role">Design engineer · Atlas Platform</p>
          </div>
          <span class="gm-08__badge">Adaptive</span>
        </div>
        <p class="gm-08__copy">This card ships one markup tree. Everything that changes between themes is a custom property on the root — blur radius, saturation, film alpha, rim brightness and shadow depth.</p>
        <dl class="gm-08__specs">
          <div><dt>blur</dt><dd class="gm-08__vblur">24px</dd></div>
          <div><dt>saturate</dt><dd class="gm-08__vsat">140%</dd></div>
          <div><dt>film</dt><dd class="gm-08__vfilm">black 42%</dd></div>
          <div><dt>rim</dt><dd class="gm-08__vrim">white 50%</dd></div>
        </dl>
        <div class="gm-08__actions">
          <button class="gm-08__btn gm-08__btn--primary" type="button">Copy tokens</button>
          <button class="gm-08__btn" type="button">View diff</button>
        </div>
      </article>

      <p class="gm-08__foot">Priority order: <span class="gm-08__code">prefers-color-scheme</span> sets the default, <span class="gm-08__code">[data-theme]</span> lets the host force a mode, the in-page switch overrides both.</p>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap');

.gm-08 {
  /* dark surface: thick blur, calm saturation, dark film */
  --blur: 24px;
  --sat: 140%;
  --film: rgba(8,10,22,.42);
  --rim: rgba(255,255,255,.5);
  --rim2: rgba(255,255,255,.14);
  --edge: rgba(255,255,255,.2);
  --amb: 0 30px 66px -30px rgba(0,0,0,.72);
  --a1: rgba(129,140,248,.6);
  --a2: rgba(45,212,191,.5);
  --a3: rgba(244,114,182,.5);
  --a4: rgba(250,204,21,.35);
  --base: #05070f;
  --base2: #141033;
  --ink: #f8fafe;
  --muted: rgba(248,250,254,.7);
  --accent: #a78bfa;
  --mono: 'Geist Mono',ui-monospace,'SFMono-Regular',Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  overflow: hidden;
  box-sizing: border-box;
  color: var(--ink);
  isolation: isolate;
  font-family: 'Geist',ui-sans-serif,system-ui,-apple-system,'Segoe UI',sans-serif;
  background: radial-gradient(54% 46% at 16% 16%, var(--a1) 0%, transparent 62%), radial-gradient(46% 40% at 84% 14%, var(--a2) 0%, transparent 58%), radial-gradient(50% 44% at 78% 88%, var(--a3) 0%, transparent 60%), radial-gradient(42% 36% at 16% 90%, var(--a4) 0%, transparent 58%), linear-gradient(160deg, var(--base) 0%, var(--base2) 54%, var(--base) 100%);
  transition: background-color .3s ease;
}

.gm-08 *,
.gm-08 *::before,
.gm-08 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 300)) {
  .gm-08 {
    --a1: oklch(0.68 0.19 280 / .62);
    --a2: oklch(0.82 0.15 178 / .52);
    --a3: oklch(0.74 0.19 5 / .5);
    --a4: oklch(0.88 0.16 95 / .36);
    --base: oklch(0.13 0.026 272);
    --base2: oklch(0.23 0.1 292);
    --accent: oklch(0.72 0.17 292);
  }
}

.gm-08__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.gm-08__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.gm-08__theme {
  position: absolute;
  inset-block-start: 1.15rem;
  inset-inline-end: 1.15rem;
  z-index: 8;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  border-radius: 999px;
  color: var(--ink);
  background: rgba(255,255,255,.14);
  border: 1px solid var(--edge);
  -webkit-backdrop-filter: blur(10px) saturate(160%);
  backdrop-filter: blur(10px) saturate(160%);
  box-shadow: inset 0 1px 0 var(--rim), 0 10px 24px -14px rgba(0,0,0,.7);
  transition: scale .18s ease;
}

.gm-08__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
  border-radius: inherit;
}

.gm-08__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.gm-08__theme:hover {
  scale: 1.06;
}

.gm-08__sr:focus-visible + .gm-08__theme {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.gm-08__moon {
  display: none;
}

.gm-08__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,4vw,3.5rem);
}

.gm-08__wrap {
  inline-size: min(46rem,100%);
  display: grid;
  gap: clamp(1.25rem,3vw,2rem);
}

.gm-08__head {
  display: grid;
  gap: .7rem;
  justify-items: start;
}

.gm-08__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
}

.gm-08__h {
  margin: 0;
  font-size: clamp(1.85rem,4.4vw,2.9rem);
  font-weight: 600;
  letter-spacing: -.03em;
  line-height: 1.05;
  text-wrap: balance;
}

.gm-08__sub {
  margin: 0;
  font-size: clamp(.95rem,1.4vw,1.05rem);
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.gm-08__switch {
  display: inline-flex;
  align-items: center;
  gap: .7rem;
  margin-block-start: .35rem;
  min-block-size: 2.75rem;
  padding: .4rem .85rem .4rem .5rem;
  border-radius: 999px;
  cursor: pointer;
  background: var(--film);
  border: 1px solid var(--edge);
  -webkit-backdrop-filter: blur(14px) saturate(var(--sat));
  backdrop-filter: blur(14px) saturate(var(--sat));
  box-shadow: inset 0 1px 0 var(--rim);
  font-size: .9rem;
  font-weight: 500;
  color: var(--ink);
}

.gm-08__track {
  position: relative;
  inline-size: 2.9rem;
  block-size: 1.7rem;
  border-radius: 999px;
  background: rgba(255,255,255,.16);
  border: 1px solid var(--edge);
  box-shadow: inset 0 1px 3px rgba(0,0,0,.35);
}

.gm-08__thumb {
  position: absolute;
  inset-block-start: .15rem;
  inset-inline-start: .18rem;
  inline-size: 1.25rem;
  block-size: 1.25rem;
  border-radius: 999px;
  background: rgba(255,255,255,.9);
  box-shadow: 0 2px 6px rgba(0,0,0,.4);
  transition: translate .24s cubic-bezier(.3,.8,.3,1), background .24s ease;
}

.gm-08__son {
  display: none;
}

.gm-08__sr:focus-visible ~ .gm-08__stage .gm-08__switch {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.gm-08__card {
  position: relative;
  display: grid;
  gap: 1rem;
  padding: clamp(1.35rem,2.6vw,2rem);
  border-radius: 1.75rem;
  background: var(--film);
  border: 1px solid var(--edge);
  box-shadow: inset 0 1px 0 var(--rim), inset 0 -1px 0 var(--rim2), var(--amb);
}

@supports ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .gm-08__card {
    -webkit-backdrop-filter: blur(var(--blur)) saturate(var(--sat));
    backdrop-filter: blur(var(--blur)) saturate(var(--sat));
  }
}

@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .gm-08__card {
    background: rgba(14,12,38,.9);
  }
}

.gm-08__cardtop {
  display: flex;
  align-items: center;
  gap: .85rem;
  flex-wrap: wrap;
}

.gm-08__avatar {
  display: grid;
  place-items: center;
  inline-size: 2.9rem;
  block-size: 2.9rem;
  border-radius: 999px;
  font-family: var(--mono);
  font-size: .9rem;
  letter-spacing: .04em;
  background: rgba(255,255,255,.18);
  border: 1px solid var(--edge);
  box-shadow: inset 0 1px 0 var(--rim2);
}

.gm-08__name {
  margin: 0;
  font-size: 1.1rem;
  font-weight: 600;
  letter-spacing: -.015em;
}

.gm-08__role {
  margin: .1rem 0 0;
  font-size: .85rem;
  color: var(--muted);
}

.gm-08__badge {
  margin-inline-start: auto;
  padding: .3rem .6rem;
  border-radius: .5rem;
  font-family: var(--mono);
  font-size: .68rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--ink);
  background: rgba(255,255,255,.16);
  border: 1px solid var(--edge);
}

.gm-08__copy {
  margin: 0;
  font-size: .96rem;
  line-height: 1.6;
  color: var(--ink);
  opacity: .86;
  text-wrap: pretty;
}

.gm-08__specs {
  margin: 0;
  padding-block-start: 1rem;
  border-block-start: 1px solid var(--rim2);
  display: grid;
  gap: .9rem;
  grid-template-columns: repeat(auto-fit,minmax(6.5rem,1fr));
}

.gm-08__specs div {
  display: grid;
  gap: .2rem;
}

.gm-08__specs dt {
  font-family: var(--mono);
  font-size: .64rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
}

.gm-08__specs dd {
  margin: 0;
  font-family: var(--mono);
  font-size: .9rem;
  font-weight: 500;
  font-variant-numeric: tabular-nums;
}

.gm-08__actions {
  display: flex;
  flex-wrap: wrap;
  gap: .6rem;
}

.gm-08__btn {
  min-block-size: 2.75rem;
  padding: .7rem 1.1rem;
  border-radius: .85rem;
  cursor: pointer;
  font: inherit;
  font-size: .92rem;
  font-weight: 500;
  color: var(--ink);
  background: rgba(255,255,255,.14);
  border: 1px solid var(--edge);
  -webkit-backdrop-filter: blur(12px) saturate(var(--sat));
  backdrop-filter: blur(12px) saturate(var(--sat));
  box-shadow: inset 0 1px 0 var(--rim2);
  transition: translate .18s ease, background .18s ease;
}

.gm-08__btn--primary {
  background: var(--accent);
  color: #0b0715;
  border-color: transparent;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.45), 0 10px 24px -14px rgba(0,0,0,.6);
}

.gm-08__btn:hover {
  translate: 0 -2px;
}

.gm-08__btn:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.gm-08__foot {
  margin: 0;
  font-size: .88rem;
  line-height: 1.55;
  color: var(--muted);
}

.gm-08__code {
  font-family: var(--mono);
  font-size: .8rem;
  padding: .12rem .38rem;
  border-radius: .35rem;
  background: rgba(255,255,255,.12);
  border: 1px solid var(--edge);
  color: var(--ink);
}
/* LIGHT SURFACE: less blur, much more saturate, white film */

.gm-08[data-theme="light"],
.gm-08:has(#gm-08-theme:checked) {
  --blur: 12px;
  --sat: 200%;
  --film: rgba(255,255,255,.55);
  --rim: rgba(255,255,255,.95);
  --rim2: rgba(255,255,255,.55);
  --edge: rgba(16,18,32,.12);
  --amb: 0 24px 54px -30px rgba(30,26,70,.45);
  --a1: rgba(165,180,252,.6);
  --a2: rgba(153,246,228,.55);
  --a3: rgba(249,168,212,.55);
  --a4: rgba(254,240,138,.5);
  --base: #f2f4fb;
  --base2: #e2e8fc;
  --ink: #0f1220;
  --muted: rgba(15,18,32,.68);
  --accent: #7c3aed;
}

.gm-08:has(#gm-08-theme:checked) .gm-08__sun {
  display: none;
}

.gm-08:has(#gm-08-theme:checked) .gm-08__moon {
  display: block;
}

.gm-08:has(#gm-08-theme:checked) .gm-08__thumb {
  translate: 1.2rem 0;
  background: #fff;
}

.gm-08:has(#gm-08-theme:checked) .gm-08__son {
  display: inline;
}

.gm-08:has(#gm-08-theme:checked) .gm-08__soff {
  display: none;
}

.gm-08:has(#gm-08-theme:checked) .gm-08__vblur::after {
  content: '';
}

.gm-08:has(#gm-08-theme:checked) .gm-08__vblur {
  font-size: 0;
}

.gm-08:has(#gm-08-theme:checked) .gm-08__vblur::before {
  content: '12px';
  font-size: .9rem;
}

.gm-08:has(#gm-08-theme:checked) .gm-08__vsat {
  font-size: 0;
}

.gm-08:has(#gm-08-theme:checked) .gm-08__vsat::before {
  content: '200%';
  font-size: .9rem;
}

.gm-08:has(#gm-08-theme:checked) .gm-08__vfilm {
  font-size: 0;
}

.gm-08:has(#gm-08-theme:checked) .gm-08__vfilm::before {
  content: 'white 55%';
  font-size: .9rem;
}

.gm-08:has(#gm-08-theme:checked) .gm-08__vrim {
  font-size: 0;
}

.gm-08:has(#gm-08-theme:checked) .gm-08__vrim::before {
  content: 'white 95%';
  font-size: .9rem;
}

.gm-08:has(#gm-08-theme:checked) .gm-08__btn--primary {
  color: #fff;
}

.gm-08:has(#gm-08-theme:checked) .gm-08__track {
  background: rgba(16,18,32,.14);
  box-shadow: inset 0 1px 3px rgba(16,18,32,.2);
}

@media (prefers-reduced-motion: reduce) {
  .gm-08 *,
    .gm-08 *::before,
    .gm-08 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .gm-08__card,
    .gm-08__btn,
    .gm-08__theme,
    .gm-08__switch,
    .gm-08__badge,
    .gm-08__avatar {
    border-color: CanvasText;
    box-shadow: none;
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
    background: Canvas;
  }
}
```
