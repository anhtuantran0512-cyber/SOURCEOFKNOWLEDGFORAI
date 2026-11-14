---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-retro-designs/90s-website-guestbook-widget/"
title: "Nineties Web Guestbook Widget"
section: "design-styles"
category: "css-retro-designs"
category_name: "CSS Retro UI"
description: "A personal-homepage guestbook: odometer hit counter, webring navigation, signed entries and a \"best viewed in\" badge, on the grey ground and ridged borders…"
has_js: "false"
---

Here's a working CSS Retro UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Nineties Web Guestbook Widget
Source: https://codefronts.com/design-styles/css-retro-designs/90s-website-guestbook-widget/

A personal-homepage guestbook: odometer hit counter, webring navigation, signed entries and a "best viewed in" badge, on the grey ground and ridged borders of the era. The point it makes is the one that matters most about this period &mdash; reproduce the look, never the markup, because everything that made these pages work is now the reason they fail.
## HTML
```html
<section class="rt-17" aria-labelledby="rt-17-title">
  <h2 class="rt-17__sr" id="rt-17-title">Nineties personal homepage guestbook</h2>

  <div class="rt-17__theme">
    <input class="rt-17__theme-input" type="checkbox" id="rt-17-theme">
    <label class="rt-17__theme-label" for="rt-17-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="rt-17__sr">Toggle dark ground</span>
    </label>
  </div>

  <div class="rt-17__stage">
    <header class="rt-17__masthead">
      <h3 class="rt-17__h">Dave&rsquo;s Homepage</h3>
      <p class="rt-17__tag">~ under construction since 1997 ~</p>
    </header>

    <div class="rt-17__grid">
      <article class="rt-17__panel" aria-labelledby="rt-17-gb">
        <h4 class="rt-17__panel-h" id="rt-17-gb">Sign my guestbook</h4>
        <ol class="rt-17__entries">
          <li class="rt-17__entry">
            <span class="rt-17__av" aria-hidden="true">AC</span>
            <div class="rt-17__entry-b">
              <p class="rt-17__entry-m"><b>Alex Chen</b> &middot; 14 Nov 1997 &middot; Manchester</p>
              <p class="rt-17__entry-t">Great page! Love the MIDI. Come see my Star Trek shrine sometime.</p>
            </div>
          </li>
          <li class="rt-17__entry">
            <span class="rt-17__av" aria-hidden="true">PS</span>
            <div class="rt-17__entry-b">
              <p class="rt-17__entry-m"><b>Priya Sharma</b> &middot; 2 Dec 1997 &middot; Leeds</p>
              <p class="rt-17__entry-t">Added you to the ring. The tiled background is a bold choice and I respect it.</p>
            </div>
          </li>
          <li class="rt-17__entry">
            <span class="rt-17__av" aria-hidden="true">JL</span>
            <div class="rt-17__entry-b">
              <p class="rt-17__entry-m"><b>Jordan Lee</b> &middot; 19 Jan 1998 &middot; Bristol</p>
              <p class="rt-17__entry-t">Your links page is the best on the web. Signed, a fellow traveller.</p>
            </div>
          </li>
        </ol>
        <p class="rt-17__note">Entries are a real ordered list. No table, no spacer image, no <code>&lt;font&gt;</code> anywhere in this widget.</p>
      </article>

      <aside class="rt-17__side">
        <div class="rt-17__panel rt-17__panel--tight">
          <h4 class="rt-17__panel-h">Visitors</h4>
          <div class="rt-17__counter" role="img" aria-label="Visitor count: 0 0 4 2 1 8 7">
            <span>0</span><span>0</span><span>4</span><span>2</span><span>1</span><span>8</span><span>7</span>
          </div>
          <p class="rt-17__counter-c">since 12 August 1997</p>
        </div>

        <nav class="rt-17__panel rt-17__panel--tight" aria-labelledby="rt-17-ring">
          <h4 class="rt-17__panel-h" id="rt-17-ring">The Retro Web Ring</h4>
          <ul class="rt-17__ring">
            <li><button class="rt-17__ringbtn" type="button">&#171; Prev</button></li>
            <li><button class="rt-17__ringbtn" type="button">Random</button></li>
            <li><button class="rt-17__ringbtn" type="button">List</button></li>
            <li><button class="rt-17__ringbtn" type="button">Next &#187;</button></li>
          </ul>
        </nav>

        <div class="rt-17__panel rt-17__panel--tight">
          <h4 class="rt-17__panel-h">Best viewed in</h4>
          <p class="rt-17__badge">800 &times; 600 &middot; 256 colours</p>
          <p class="rt-17__counter-c">The badge pulses on a two second cycle and stops under reduced motion. The era flashed it; that is the one thing not worth reproducing.</p>
        </div>
      </aside>
    </div>
  </div>
</section>
```
## CSS
```css
.rt-17 {
  --rt-17-face: #c8c8c8;
  --rt-17-face-2: #dcdcdc;
  --rt-17-hi: #ffffff;
  --rt-17-sh: #7a7a7a;
  --rt-17-ink: #16161a;
  --rt-17-ink: oklch(20% 0.006 280);
  --rt-17-ink-2: #4a4a52;
  --rt-17-ink-2: oklch(42% 0.01 280);
  --rt-17-acc: #0f3fa8;
  --rt-17-acc: oklch(42% 0.19 262);
  --rt-17-hot: #a01414;
  --rt-17-hot-ink: #ffffff;
  --rt-17-hot: oklch(43% 0.18 27);
  --rt-17-serif: ui-serif, Georgia, "Times New Roman", Times, serif;
  --rt-17-sans: ui-sans-serif, Verdana, Geneva, "Trebuchet MS", system-ui, sans-serif;
  --rt-17-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  --rt-17-tile-a: #c8c8c8;
  --rt-17-tile-b: #bdbdbd;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background-color: var(--rt-17-tile-a);
  background-image: repeating-conic-gradient(var(--rt-17-tile-b) 0% 25%, var(--rt-17-tile-a) 0% 50%);
  background-size: 8px 8px;
  color: var(--rt-17-ink);
  font-family: var(--rt-17-sans);
  -webkit-text-size-adjust: 100%;
}

.rt-17 *,
.rt-17 *::before,
.rt-17 *::after {
  box-sizing: border-box;
}

@media (prefers-color-scheme: dark) {
  .rt-17 {
    --rt-17-tile-a: #26262a;
    --rt-17-tile-b: #1e1e22;
    --rt-17-face: #33333a;
    --rt-17-face-2: #3d3d45;
    --rt-17-hi: #5c5c66;
    --rt-17-sh: #17171b;
    --rt-17-ink: #eeeef2;
    --rt-17-ink: oklch(95% 0.004 280);
    --rt-17-ink-2: #b0b0ba;
    --rt-17-ink-2: oklch(77% 0.008 280);
    --rt-17-acc: #8fb2ff;
    --rt-17-acc: oklch(78% 0.12 262);
    --rt-17-hot: #ff8f8f;
    --rt-17-hot-ink: #3a0505;
    --rt-17-hot: oklch(78% 0.14 27);
  }
}

.rt-17[data-theme="dark"],
.rt-17:has(.rt-17__theme-input:checked) {
  --rt-17-tile-a: #26262a;
  --rt-17-tile-b: #1e1e22;
  --rt-17-face: #33333a;
  --rt-17-face-2: #3d3d45;
  --rt-17-hi: #5c5c66;
  --rt-17-sh: #17171b;
  --rt-17-ink: #eeeef2;
  --rt-17-ink: oklch(95% 0.004 280);
  --rt-17-ink-2: #b0b0ba;
  --rt-17-ink-2: oklch(77% 0.008 280);
  --rt-17-acc: #8fb2ff;
  --rt-17-acc: oklch(78% 0.12 262);
  --rt-17-hot: #ff8f8f;
  --rt-17-hot-ink: #3a0505;
  --rt-17-hot: oklch(78% 0.14 27);
}

@media (prefers-color-scheme: light) {
  .rt-17:has(.rt-17__theme-input:checked) {
    --rt-17-tile-a: #26262a;
    --rt-17-tile-b: #1e1e22;
    --rt-17-face: #33333a;
    --rt-17-face-2: #3d3d45;
    --rt-17-hi: #5c5c66;
    --rt-17-sh: #17171b;
    --rt-17-ink: #eeeef2;
    --rt-17-ink: oklch(95% 0.004 280);
    --rt-17-ink-2: #b0b0ba;
    --rt-17-ink-2: oklch(77% 0.008 280);
    --rt-17-acc: #8fb2ff;
    --rt-17-acc: oklch(78% 0.12 262);
    --rt-17-hot: #ff8f8f;
    --rt-17-hot-ink: #3a0505;
    --rt-17-hot: oklch(78% 0.14 27);
  }
}

@media (prefers-color-scheme: dark) {
  .rt-17:has(.rt-17__theme-input:checked) {
    --rt-17-tile-a: #c8c8c8;
    --rt-17-tile-b: #bdbdbd;
    --rt-17-face: #c8c8c8;
    --rt-17-face-2: #dcdcdc;
    --rt-17-hi: #ffffff;
    --rt-17-sh: #7a7a7a;
    --rt-17-ink: #16161a;
    --rt-17-ink: oklch(20% 0.006 280);
    --rt-17-ink-2: #4a4a52;
    --rt-17-ink-2: oklch(42% 0.01 280);
    --rt-17-acc: #0f3fa8;
    --rt-17-acc: oklch(42% 0.19 262);
    --rt-17-hot: #a01414;
    --rt-17-hot-ink: #ffffff;
    --rt-17-hot: oklch(43% 0.18 27);
  }
}

.rt-17__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.rt-17__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 6;
}

.rt-17__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 44px;
  block-size: 44px;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.rt-17__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  cursor: pointer;
  background: var(--rt-17-face-2);
  color: var(--rt-17-ink-2);
  box-shadow: inset 2px 2px 0 0 var(--rt-17-hi), inset -2px -2px 0 0 var(--rt-17-sh);
}

.rt-17__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.rt-17__theme-input:focus-visible + .rt-17__theme-label {
  outline: 2px solid var(--rt-17-acc);
  outline-offset: 2px;
}

.rt-17__stage {
  max-inline-size: 62rem;
  margin-inline: auto;
  padding: clamp(3.5rem, 3rem + 3vw, 5rem) clamp(0.75rem, 0.5rem + 1.5vw, 2rem) 4rem;
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1.25rem;
}

.rt-17__masthead {
  min-inline-size: 0;
  text-align: center;
  display: grid;
  gap: 0.3rem;
}

.rt-17__h {
  margin: 0;
  font-family: var(--rt-17-serif);
  font-size: clamp(1.6rem, 1rem + 4vw, 3rem);
  line-height: 1.05;
  color: var(--rt-17-acc);
  min-inline-size: 0;
  text-wrap: balance;
  text-shadow: 2px 2px 0 var(--rt-17-hi);
}

.rt-17__tag {
  margin: 0;
  font-family: var(--rt-17-mono);
  font-size: 0.78rem;
  color: var(--rt-17-hot);
  letter-spacing: 0.04em;
}

.rt-17__grid {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1.1rem;
  align-items: start;
}

.rt-17__panel {
  min-inline-size: 0;
  background: var(--rt-17-face-2);
  padding: clamp(0.85rem, 0.6rem + 1vw, 1.2rem);
  display: grid;
  gap: 0.8rem;
  align-content: start;
  box-shadow: inset 2px 2px 0 0 var(--rt-17-hi), inset -2px -2px 0 0 var(--rt-17-sh), inset 4px 4px 0 0 var(--rt-17-sh), inset -4px -4px 0 0 var(--rt-17-hi);
}

.rt-17__panel--tight {
  gap: 0.55rem;
}

.rt-17__panel-h {
  margin: 0;
  font-family: var(--rt-17-serif);
  font-size: 1.05rem;
  color: var(--rt-17-acc);
  min-inline-size: 0;
}

.rt-17__entries {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 0.7rem;
  min-inline-size: 0;
}

.rt-17__entry {
  display: grid;
  grid-template-columns: 40px minmax(0, 1fr);
  gap: 0.7rem;
  align-items: start;
  padding: 0.65rem;
  background: var(--rt-17-face);
  box-shadow: inset 1px 1px 0 0 var(--rt-17-sh), inset -1px -1px 0 0 var(--rt-17-hi);
}

.rt-17__av {
  inline-size: 40px;
  block-size: 40px;
  display: grid;
  place-items: center;
  flex: none;
  background: var(--rt-17-acc);
  color: #ffffff;
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: 0.04em;
}

.rt-17__entry-b {
  min-inline-size: 0;
  display: grid;
  gap: 0.25rem;
}

.rt-17__entry-m {
  margin: 0;
  font-size: 0.72rem;
  color: var(--rt-17-ink-2);
  min-inline-size: 0;
  overflow-wrap: anywhere;
}

.rt-17__entry-m b {
  color: var(--rt-17-ink);
}

.rt-17__entry-t {
  margin: 0;
  font-family: var(--rt-17-serif);
  font-size: 0.95rem;
  line-height: 1.5;
  min-inline-size: 0;
  text-wrap: pretty;
}

.rt-17__note {
  margin: 0;
  font-size: 0.78rem;
  line-height: 1.5;
  color: var(--rt-17-ink-2);
  min-inline-size: 0;
  text-wrap: pretty;
}

.rt-17__note code {
  font-family: var(--rt-17-mono);
  background: var(--rt-17-face);
  padding: 0.05em 0.3em;
}

.rt-17__side {
  display: grid;
  gap: 1.1rem;
  min-inline-size: 0;
  align-content: start;
}

.rt-17__counter {
  display: flex;
  flex-wrap: wrap;
  gap: 3px;
  min-inline-size: 0;
}

.rt-17__counter span {
  inline-size: 24px;
  block-size: 34px;
  display: grid;
  place-items: center;
  flex: none;
  background: #101010;
  color: #ffd45e;
  font-family: var(--rt-17-mono);
  font-size: 1.05rem;
  font-variant-numeric: tabular-nums;
  box-shadow: inset 0 2px 4px rgba(0,0,0,0.9), 0 1px 0 var(--rt-17-hi);
}

.rt-17__counter-c {
  margin: 0;
  font-size: 0.72rem;
  line-height: 1.5;
  color: var(--rt-17-ink-2);
  min-inline-size: 0;
  text-wrap: pretty;
}

.rt-17__ring {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 4px;
}

.rt-17__ringbtn {
  min-block-size: 44px;
  min-inline-size: 44px;
  flex: 1 1 auto;
  padding: 0.5rem 0.6rem;
  border: 0;
  cursor: pointer;
  font: inherit;
  font-size: 0.78rem;
  background: var(--rt-17-face);
  color: var(--rt-17-acc);
  box-shadow: inset 2px 2px 0 0 var(--rt-17-hi), inset -2px -2px 0 0 var(--rt-17-sh);
}

.rt-17__ringbtn:active {
  box-shadow: inset 2px 2px 0 0 var(--rt-17-sh), inset -2px -2px 0 0 var(--rt-17-hi);
}

.rt-17__ringbtn:focus-visible {
  outline: 2px solid var(--rt-17-acc);
  outline-offset: -6px;
}

.rt-17__badge {
  margin: 0;
  justify-self: start;
  padding: 0.45rem 0.75rem;
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.04em;
  color: var(--rt-17-hot-ink, #ffffff);
  background: var(--rt-17-hot);
  box-shadow: inset 1px 1px 0 0 rgba(255,255,255,0.5), inset -1px -1px 0 0 rgba(0,0,0,0.4);
  animation: rt-17-pulse 2s ease-in-out infinite;
}

@keyframes rt-17-pulse {
  0%,
    100% {
    transform: scale(1);
  }

  50% {
    transform: scale(1.045);
  }
}

@media (prefers-reduced-motion: reduce) {
  .rt-17__badge {
    animation: none;
  }
}

@media (min-width: 52rem) {
  .rt-17__grid {
    grid-template-columns: minmax(0, 1.7fr) minmax(0, 1fr);
  }
}
```
