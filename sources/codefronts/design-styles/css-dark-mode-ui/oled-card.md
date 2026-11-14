---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-dark-mode-ui/oled-card/"
title: "OLED True Black Dark Mode Card"
section: "design-styles"
category: "css-dark-mode-ui"
category_name: "CSS Dark Mode UI"
description: "A product card built for OLED panels, where an unlit pixel is genuinely off: the page is #000 and every layer above it climbs a short surface ramp — #0a0a0a,…"
has_js: "false"
---

Here's a working CSS Dark Mode UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: OLED True Black Dark Mode Card
Source: https://codefronts.com/design-styles/css-dark-mode-ui/oled-card/

A product card built for OLED panels, where an unlit pixel is genuinely off: the page is #000 and every layer above it climbs a short surface ramp — #0a0a0a, #141414, #1c1c1c — instead of relying on shadows that a true-black substrate swallows. The result is deeper contrast, a measurably cheaper screen and an interface that looks like it was designed for the display rather than ported to it.
## HTML
```html
<div class="dmu-11">
  <div class="dmu-11__stage">
    <article class="dmu-11__card">
      <div class="dmu-11__shot">
        <img src="https://picsum.photos/seed/oled-1024/720/540" width="720" height="540" alt="Product photograph placeholder — swap the src for your own asset" loading="lazy" decoding="async">
        <span class="dmu-11__chip">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M13 3.2 5.8 13.4h4.6L10 20.8l7.4-10.4h-4.6Z"/></svg>
          Power-optimized for OLED
        </span>
      </div>

      <div class="dmu-11__body">
        <p class="dmu-11__kicker">Nocturne Series</p>
        <h1 class="dmu-11__title">Halo Desk Lamp</h1>
        <p class="dmu-11__blurb">Continuous 1800K&ndash;5000K dimming with a matte anodised shell. Reads beautifully against a true-black interface.</p>

        <dl class="dmu-11__specs">
          <div><dt>Finish</dt><dd>Anodised graphite</dd></div>
          <div><dt>Output</dt><dd>420 lm &middot; CRI 97</dd></div>
          <div><dt>Ships</dt><dd>Free, 2&ndash;4 days</dd></div>
        </dl>

        <div class="dmu-11__foot">
          <p class="dmu-11__price">&#36;248<span>&#36;310</span></p>
          <div class="dmu-11__actions">
            <button class="dmu-11__btn dmu-11__btn--ghost" type="button">
              <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20.4S3.6 15.3 3.6 9.7A4.1 4.1 0 0 1 12 7.4a4.1 4.1 0 0 1 8.4 2.3c0 5.6-8.4 10.7-8.4 10.7Z"/></svg>
              <span class="dmu-11__sr">Save</span>
            </button>
            <button class="dmu-11__btn dmu-11__btn--primary" type="button">Add to bag</button>
          </div>
        </div>
      </div>
    </article>
  </div>
</div>
```
## CSS
```css
.dmu-11 {
  --void: #000000;
  --surface-0: #0a0a0a;
  --surface-1: #141414;
  --surface-2: #1c1c1c;
  --hair: rgba(255,255,255,.08);
  --sheen: rgba(255,255,255,.06);
  --ink: #fafafa;
  --body: #d4d4d4;
  --muted: #8a8a8a;
  --accent: #e2e8f0;
  --accent-ink: #050505;
  --sans: system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: ui-monospace,"SF Mono","JetBrains Mono",Menlo,monospace;
  color-scheme: dark;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: radial-gradient(90% 60% at 50% 0%,#0b0b0b,var(--void) 70%),var(--void);
  color: var(--body);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.dmu-11,
.dmu-11 *,
.dmu-11 *::before,
.dmu-11 *::after {
  box-sizing: border-box;
}

.dmu-11__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.dmu-11__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3rem);
}

.dmu-11__card {
  width: min(58rem,100%);
  display: grid;
  grid-template-columns: 1fr;
  overflow: hidden;
  border-radius: 1.4rem;
  background: var(--surface-0);
  border: 1px solid var(--hair);
  box-shadow: inset 0 1px 0 var(--sheen);
}

@media (min-width: 52rem) {
  .dmu-11__card {
    grid-template-columns: 1.05fr 1fr;
  }
}

.dmu-11__shot {
  position: relative;
  background: var(--surface-1);
  min-height: 16rem;
}

.dmu-11__shot img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
  aspect-ratio: 4 / 3;
  -webkit-mask-image: linear-gradient(180deg,#000 62%,transparent);
  mask-image: linear-gradient(180deg,#000 62%,transparent);
  filter: saturate(.55) brightness(.78) contrast(1.06);
}

@media (min-width: 52rem) {
  .dmu-11__shot img {
    aspect-ratio: auto;
    -webkit-mask-image: linear-gradient(100deg,#000 60%,transparent);
    mask-image: linear-gradient(100deg,#000 60%,transparent);
  }
}

.dmu-11__chip {
  position: absolute;
  left: 1rem;
  top: 1rem;
  display: inline-flex;
  align-items: center;
  gap: .35rem;
  padding: .35rem .6rem;
  border-radius: 999px;
  font-size: .7rem;
  letter-spacing: .02em;
  background: rgba(0,0,0,.66);
  color: var(--ink);
  border: 1px solid var(--hair);
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
}

.dmu-11__chip svg {
  width: .9rem;
  height: .9rem;
  color: #fde68a;
}

.dmu-11__body {
  padding: clamp(1.4rem,3.5vw,2.4rem);
  display: grid;
  gap: .6rem;
  align-content: center;
}

.dmu-11__kicker {
  margin: 0;
  font-family: var(--mono);
  font-size: .7rem;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--muted);
}

.dmu-11__title {
  margin: 0;
  font-size: clamp(1.7rem,4vw,2.5rem);
  font-weight: 600;
  letter-spacing: -.04em;
  color: var(--ink);
}

.dmu-11__blurb {
  margin: 0 0 .3rem;
  font-size: .95rem;
  line-height: 1.65;
  color: var(--body);
  max-width: 42ch;
  text-wrap: pretty;
}

.dmu-11__specs {
  margin: 0;
  display: grid;
  gap: .1rem;
  padding: .85rem .95rem;
  border-radius: .85rem;
  background: var(--surface-1);
  border: 1px solid var(--hair);
}

.dmu-11__specs div {
  display: grid;
  grid-template-columns: 6.5rem 1fr;
  gap: .6rem;
  padding: .28rem 0;
  font-size: .82rem;
}

.dmu-11__specs dt {
  color: var(--muted);
}

.dmu-11__specs dd {
  margin: 0;
  color: var(--body);
}

.dmu-11__foot {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  flex-wrap: wrap;
  margin-top: .35rem;
}

.dmu-11__price {
  margin: 0;
  display: flex;
  align-items: baseline;
  gap: .5rem;
  font-family: var(--mono);
  font-variant-numeric: tabular-nums;
  font-size: 1.6rem;
  font-weight: 600;
  letter-spacing: -.04em;
  color: var(--ink);
}

.dmu-11__price span {
  font-size: .85rem;
  font-weight: 400;
  color: var(--muted);
  text-decoration: line-through;
}

.dmu-11__actions {
  display: flex;
  gap: .5rem;
}

.dmu-11__btn {
  display: inline-grid;
  place-items: center;
  min-height: 2.9rem;
  padding: 0 1.15rem;
  border-radius: .7rem;
  cursor: pointer;
  font: inherit;
  font-size: .88rem;
  font-weight: 560;
  border: 1px solid var(--hair);
  background: var(--surface-2);
  color: var(--ink);
  transition: background-color .2s ease, translate .2s cubic-bezier(.16,1,.3,1);
}

.dmu-11__btn--ghost {
  width: 2.9rem;
  padding: 0;
}

.dmu-11__btn svg {
  width: 1.1rem;
  height: 1.1rem;
}

.dmu-11__btn:hover {
  translate: 0 -1px;
  background: #242424;
}

.dmu-11__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.dmu-11__btn--primary {
  background: var(--accent);
  color: var(--accent-ink);
  border-color: transparent;
}

.dmu-11__btn--primary:hover {
  background: #ffffff;
}

@media (prefers-reduced-motion: reduce) {
  .dmu-11__btn {
    transition: none;
  }
}

@media (forced-colors: active) {
  .dmu-11__card,
    .dmu-11__specs,
    .dmu-11__chip {
    border-color: CanvasText;
    box-shadow: none;
  }

  .dmu-11__btn--primary {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
  }

  .dmu-11__shot img {
    mask-image: none;
    -webkit-mask-image: none;
  }
}
```
