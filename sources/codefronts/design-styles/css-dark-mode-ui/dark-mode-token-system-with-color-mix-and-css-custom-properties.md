---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-dark-mode-ui/dark-mode-token-system-with-color-mix-and-css-custom-properties/"
title: "Dark Mode Token System with color-mix and CSS Custom Properties"
section: "design-styles"
category: "css-dark-mode-ui"
category_name: "CSS Dark Mode UI"
description: "The architecture that stops a dark theme from becoming forty hand-picked hex codes."
has_js: "false"
---

Here's a working CSS Dark Mode UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dark Mode Token System with color-mix and CSS Custom Properties
Source: https://codefronts.com/design-styles/css-dark-mode-ui/dark-mode-token-system-with-color-mix-and-css-custom-properties/

The architecture that stops a dark theme from becoming forty hand-picked hex codes. Declare a primitive ramp once (--gray-0 … --gray-12, --accent-500), then derive every semantic token — surface, elevated surface, hairline, ink, muted ink, accent wash — with color-mix(in oklab, …). Two cards sit on opposite surfaces using the identical token names to prove the derivation adapts instead of inverting.
## HTML
```html
<div class="dmu-03">
  <div class="dmu-03__stage">
    <header class="dmu-03__head">
      <p class="dmu-03__kicker">Token layer</p>
      <h1 class="dmu-03__h1">Primitives in, semantics out</h1>
      <p class="dmu-03__lede">Six semantic tokens derived from a three-stop ramp with color-mix(in oklab). Flip the theme by swapping the ends of the ramp.</p>
    </header>

    <div class="dmu-03__cols">
      <section class="dmu-03__ramp" aria-label="Primitive ramp">
        <h2 class="dmu-03__colTitle">Primitives</h2>
        <ul class="dmu-03__swatches">
          <li><span class="dmu-03__chip dmu-03__chip--g0"></span><code>--gray-0</code><em>surface end</em></li>
          <li><span class="dmu-03__chip dmu-03__chip--g6"></span><code>--gray-6</code><em>midpoint</em></li>
          <li><span class="dmu-03__chip dmu-03__chip--g12"></span><code>--gray-12</code><em>ink end</em></li>
          <li><span class="dmu-03__chip dmu-03__chip--acc"></span><code>--accent-500</code><em>brand</em></li>
        </ul>
        <h2 class="dmu-03__colTitle">Derived semantics</h2>
        <ul class="dmu-03__derived">
          <li><span class="dmu-03__chip dmu-03__chip--surface"></span><code>--surface</code><em>mix 3&#37;</em></li>
          <li><span class="dmu-03__chip dmu-03__chip--elev"></span><code>--elevated</code><em>mix 7&#37;</em></li>
          <li><span class="dmu-03__chip dmu-03__chip--line"></span><code>--line</code><em>mix 12&#37;</em></li>
          <li><span class="dmu-03__chip dmu-03__chip--muted"></span><code>--muted</code><em>mix 42&#37;</em></li>
          <li><span class="dmu-03__chip dmu-03__chip--wash"></span><code>--accent-wash</code><em>accent 14&#37;</em></li>
        </ul>
      </section>

      <div class="dmu-03__cards">
        <article class="dmu-03__card dmu-03__card--light">
          <p class="dmu-03__cardTag">Light ramp</p>
          <h3 class="dmu-03__cardTitle">Usage volume</h3>
          <p class="dmu-03__num">184,204<span>events</span></p>
          <div class="dmu-03__bars" aria-hidden="true"><i style="--h:38%"></i><i style="--h:54%"></i><i style="--h:44%"></i><i style="--h:72%"></i><i style="--h:61%"></i><i style="--h:88%"></i><i style="--h:76%"></i></div>
          <div class="dmu-03__cardFoot"><span class="dmu-03__tagline">Same token names</span><button class="dmu-03__btn" type="button">Inspect</button></div>
        </article>
        <article class="dmu-03__card dmu-03__card--dark">
          <p class="dmu-03__cardTag">Dark ramp</p>
          <h3 class="dmu-03__cardTitle">Usage volume</h3>
          <p class="dmu-03__num">184,204<span>events</span></p>
          <div class="dmu-03__bars" aria-hidden="true"><i style="--h:38%"></i><i style="--h:54%"></i><i style="--h:44%"></i><i style="--h:72%"></i><i style="--h:61%"></i><i style="--h:88%"></i><i style="--h:76%"></i></div>
          <div class="dmu-03__cardFoot"><span class="dmu-03__tagline">Recipes unchanged</span><button class="dmu-03__btn" type="button">Inspect</button></div>
        </article>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.dmu-03 {
  --gray-0: #ffffff;
  --gray-6: #71717a;
  --gray-12: #09090b;
  --accent-500: #0284c7;
  --surface: #f7f7f8;
  --elevated: #f1f1f3;
  --line: #e2e2e6;
  --ink: #09090b;
  --muted: #61616b;
  --accent-wash: #e3f2fd;
  --accent-ink: #ffffff;
  --focus: #0284c7;
  --sans: system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: ui-monospace,"SF Mono","JetBrains Mono",Menlo,monospace;
  color-scheme: light dark;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--surface);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@media (prefers-color-scheme: dark) {
  .dmu-03 {
    --gray-0: #0b0b0f;
    --gray-6: #8b8b96;
    --gray-12: #fafafa;
    --accent-500: #38bdf8;
    --surface: #0b0b0f;
    --elevated: #15151b;
    --line: #26262e;
    --ink: #fafafa;
    --muted: #9a9aa5;
    --accent-wash: #0d2b3c;
    --accent-ink: #04121b;
    --focus: #7dd3fc;
  }
}

@supports (color: color-mix(in oklab, white 10%, transparent)) {
  .dmu-03 {
    --surface: color-mix(in oklab,var(--gray-0),var(--gray-12) 3%);
    --elevated: color-mix(in oklab,var(--gray-0),var(--gray-12) 7%);
    --line: color-mix(in oklab,var(--gray-0),var(--gray-12) 12%);
    --ink: var(--gray-12);
    --muted: color-mix(in oklab,var(--gray-12),var(--gray-0) 42%);
    --accent-wash: color-mix(in oklab,var(--accent-500) 14%,var(--gray-0));
  }
}

.dmu-03,
.dmu-03 *,
.dmu-03 *::before,
.dmu-03 *::after {
  box-sizing: border-box;
}

.dmu-03__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  align-content: center;
  gap: clamp(1.4rem,3vw,2.4rem);
  padding: clamp(1.25rem,5vw,3.5rem);
  max-width: 80rem;
  margin-inline: auto;
}

.dmu-03__head {
  display: grid;
  gap: .4rem;
}

.dmu-03__kicker {
  margin: 0;
  font-family: var(--mono);
  font-size: .7rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--accent-500);
}

.dmu-03__h1 {
  margin: 0;
  font-size: clamp(1.4rem,3.2vw,2rem);
  font-weight: 650;
  letter-spacing: -.03em;
}

.dmu-03__lede {
  margin: 0;
  color: var(--muted);
  font-size: .95rem;
  line-height: 1.6;
  max-width: 58ch;
  text-wrap: pretty;
}

.dmu-03__cols {
  display: grid;
  gap: 1rem;
}

@media (min-width: 60rem) {
  .dmu-03__cols {
    grid-template-columns: 19rem 1fr;
    align-items: start;
  }
}

.dmu-03__ramp {
  display: grid;
  gap: .7rem;
  padding: 1.1rem;
  border-radius: 1rem;
  background: var(--elevated);
  border: 1px solid var(--line);
}

.dmu-03__colTitle {
  margin: 0;
  font-size: .72rem;
  font-family: var(--mono);
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.dmu-03__swatches,
.dmu-03__derived {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: .3rem;
}

.dmu-03__swatches li,
.dmu-03__derived li {
  display: grid;
  grid-template-columns: 1.35rem 1fr auto;
  gap: .55rem;
  align-items: center;
  font-family: var(--mono);
  font-size: .74rem;
}

.dmu-03__swatches em,
.dmu-03__derived em {
  font-style: normal;
  color: var(--muted);
  font-size: .68rem;
}

.dmu-03__chip {
  width: 1.35rem;
  height: 1.35rem;
  border-radius: .35rem;
  border: 1px solid var(--line);
}

.dmu-03__chip--g0 {
  background: var(--gray-0);
}

.dmu-03__chip--g6 {
  background: var(--gray-6);
}

.dmu-03__chip--g12 {
  background: var(--gray-12);
}

.dmu-03__chip--acc {
  background: var(--accent-500);
}

.dmu-03__chip--surface {
  background: var(--surface);
}

.dmu-03__chip--elev {
  background: var(--elevated);
}

.dmu-03__chip--line {
  background: var(--line);
}

.dmu-03__chip--muted {
  background: var(--muted);
}

.dmu-03__chip--wash {
  background: var(--accent-wash);
}

.dmu-03__cards {
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(auto-fit,minmax(16rem,1fr));
}

.dmu-03__card {
  display: grid;
  gap: .55rem;
  padding: 1.2rem;
  border-radius: 1rem;
  background: var(--elevated);
  color: var(--ink);
  border: 1px solid var(--line);
  box-shadow: 0 18px 40px -34px rgba(0,0,0,.5);
}

.dmu-03__card--light {
  --gray-0: #ffffff;
  --gray-12: #09090b;
  --accent-500: #0284c7;
  --accent-ink: #ffffff;
  --surface: #f7f7f8;
  --elevated: #ffffff;
  --line: #e2e2e6;
  --ink: #09090b;
  --muted: #61616b;
  --accent-wash: #e3f2fd;
}

.dmu-03__card--dark {
  --gray-0: #0b0b0f;
  --gray-12: #fafafa;
  --accent-500: #38bdf8;
  --accent-ink: #04121b;
  --surface: #0b0b0f;
  --elevated: #15151b;
  --line: #26262e;
  --ink: #fafafa;
  --muted: #9a9aa5;
  --accent-wash: #0d2b3c;
}

@supports (color: color-mix(in oklab, white 10%, transparent)) {
  .dmu-03__card--light,
    .dmu-03__card--dark {
    --elevated: color-mix(in oklab,var(--gray-0),var(--gray-12) 5%);
    --line: color-mix(in oklab,var(--gray-0),var(--gray-12) 13%);
    --ink: var(--gray-12);
    --muted: color-mix(in oklab,var(--gray-12),var(--gray-0) 42%);
    --accent-wash: color-mix(in oklab,var(--accent-500) 16%,var(--gray-0));
  }
}

.dmu-03__cardTag {
  margin: 0;
  display: inline-flex;
  width: max-content;
  padding: .22rem .5rem;
  border-radius: .35rem;
  background: var(--accent-wash);
  color: var(--accent-500);
  font-family: var(--mono);
  font-size: .68rem;
  letter-spacing: .06em;
  text-transform: uppercase;
}

.dmu-03__cardTitle {
  margin: 0;
  font-size: .95rem;
  font-weight: 600;
  letter-spacing: -.01em;
}

.dmu-03__num {
  margin: 0;
  font-family: var(--mono);
  font-variant-numeric: tabular-nums;
  font-size: 1.9rem;
  font-weight: 600;
  letter-spacing: -.04em;
  display: flex;
  align-items: baseline;
  gap: .5rem;
}

.dmu-03__num span {
  font-size: .72rem;
  font-weight: 400;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: var(--muted);
}

.dmu-03__bars {
  display: flex;
  align-items: flex-end;
  gap: .35rem;
  height: 4.5rem;
  padding: .5rem;
  border-radius: .6rem;
  background: var(--surface);
  border: 1px solid var(--line);
}

.dmu-03__bars i {
  flex: 1;
  height: var(--h);
  border-radius: .2rem .2rem .1rem .1rem;
  background: linear-gradient(180deg,var(--accent-500),color-mix(in oklab,var(--accent-500) 35%,var(--surface)));
  transition: height .3s cubic-bezier(.16,1,.3,1);
}

.dmu-03__card:hover .dmu-03__bars i:nth-child(6) {
  height: 100%;
}

.dmu-03__cardFoot {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: .75rem;
}

.dmu-03__tagline {
  font-size: .75rem;
  color: var(--muted);
}

.dmu-03__btn {
  min-height: 2.35rem;
  padding: 0 .9rem;
  border-radius: .5rem;
  border: 1px solid var(--line);
  cursor: pointer;
  background: var(--accent-500);
  color: var(--accent-ink);
  font: inherit;
  font-size: .8rem;
  font-weight: 550;
  transition: filter .18s ease;
}

.dmu-03__btn:hover {
  filter: brightness(1.08);
}

.dmu-03__btn:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .dmu-03__bars i,
    .dmu-03__btn {
    transition: none;
  }
}

@media (forced-colors: active) {
  .dmu-03__card,
    .dmu-03__ramp,
    .dmu-03__bars {
    border-color: CanvasText;
    box-shadow: none;
  }

  .dmu-03__bars i {
    background: Highlight;
  }

  .dmu-03__btn {
    background: ButtonFace;
    color: ButtonText;
  }
}
```
