---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-dark-mode-ui/slate-stack/"
title: "Slate Stack Layered Dark Mode Card"
section: "design-styles"
category: "css-dark-mode-ui"
category_name: "CSS Dark Mode UI"
description: "The elevation reference for a dark design system: four surface tokens, each a measured step lighter than the last, stacked visually so the ramp is legible at…"
has_js: "false"
---

Here's a working CSS Dark Mode UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Slate Stack Layered Dark Mode Card
Source: https://codefronts.com/design-styles/css-dark-mode-ui/slate-stack/

The elevation reference for a dark design system: four surface tokens, each a measured step lighter than the last, stacked visually so the ramp is legible at a glance. A product tile holds three nested sub-cards, every level labelled with its token and step value — the artefact you paste into documentation when someone asks why the dark theme cannot just use shadows. Light-default with a dark override, mirroring the collection's toggle contract.
## HTML
```html
<div class="dmu-17">
  <div class="dmu-17__stage">
    <div class="dmu-17__wrap">
      <header class="dmu-17__head">
        <div>
          <p class="dmu-17__kicker">Elevation reference</p>
          <h1 class="dmu-17__h1">Four surfaces, no shadows</h1>
        </div>
        <input class="dmu-17__sr" type="checkbox" id="dmu-17-toggle">
        <label class="dmu-17__toggle" for="dmu-17-toggle">
          <svg class="dmu-17__sun" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"><circle cx="12" cy="12" r="4"/><path d="M12 2.8v2M12 19.2v2M2.8 12h2M19.2 12h2M5.5 5.5 7 7M17 17l1.5 1.5M18.5 5.5 17 7M7 17l-1.5 1.5"/></svg>
          <svg class="dmu-17__moon" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M20 14.4A8.4 8.4 0 0 1 9.6 4a8.4 8.4 0 1 0 10.4 10.4Z"/></svg>
          <span class="dmu-17__sr">Toggle theme</span>
        </label>
      </header>

      <div class="dmu-17__cols">
        <div class="dmu-17__stack" aria-hidden="true">
          <span class="dmu-17__layer dmu-17__layer--0"><em>--surface-0</em><b>+4&#37;</b></span>
          <span class="dmu-17__layer dmu-17__layer--1"><em>--surface-1</em><b>+8&#37;</b></span>
          <span class="dmu-17__layer dmu-17__layer--2"><em>--surface-2</em><b>+13&#37;</b></span>
          <span class="dmu-17__layer dmu-17__layer--3"><em>--surface-3</em><b>+19&#37;</b></span>
        </div>

        <article class="dmu-17__tile">
          <div class="dmu-17__tileHead">
            <span class="dmu-17__badge">surface-1</span>
            <h2 class="dmu-17__tileTitle">Release 4.2 checklist</h2>
            <p class="dmu-17__tileSub">Nested panels climb the ramp instead of stacking shadows.</p>
          </div>

          <div class="dmu-17__subs">
            <section class="dmu-17__sub">
              <p class="dmu-17__subTag">surface-2</p>
              <p class="dmu-17__subTitle">Contrast audit</p>
              <p class="dmu-17__subVal">148 pairs &middot; all pass</p>
              <div class="dmu-17__meter"><i style="--w:100%"></i></div>
            </section>
            <section class="dmu-17__sub">
              <p class="dmu-17__subTag">surface-2</p>
              <p class="dmu-17__subTitle">Token coverage</p>
              <p class="dmu-17__subVal">92&#37; of components</p>
              <div class="dmu-17__meter"><i style="--w:92%"></i></div>
            </section>
            <section class="dmu-17__sub">
              <p class="dmu-17__subTag">surface-2</p>
              <p class="dmu-17__subTitle">Focus rings</p>
              <p class="dmu-17__subVal">2px &middot; offset 2</p>
              <div class="dmu-17__meter"><i style="--w:76%"></i></div>
            </section>
          </div>

          <footer class="dmu-17__tileFoot">
            <span class="dmu-17__badge dmu-17__badge--quiet">surface-3 on hover</span>
            <button class="dmu-17__btn" type="button">Open report</button>
          </footer>
        </article>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.dmu-17 {
  --base: #f4f5f7;
  --surface-0: #ffffff;
  --surface-1: #f7f8fa;
  --surface-2: #eef0f4;
  --surface-3: #e5e8ee;
  --ink: #0b0d12;
  --muted: #5a6272;
  --hair: rgba(11,13,18,.12);
  --accent: #2563eb;
  --accent-ink: #ffffff;
  --focus: #2563eb;
  --step: 2.45rem;
  --sans: system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: ui-monospace,"SF Mono","JetBrains Mono",Menlo,monospace;
  color-scheme: light;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--base);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.dmu-17[data-theme="dark"],
.dmu-17:has(#dmu-17-toggle:checked) {
  --base: #0b0d12;
  --surface-0: #12151c;
  --surface-1: #181c25;
  --surface-2: #21262f;
  --surface-3: #2b313c;
  --ink: #eef1f6;
  --muted: #98a1b2;
  --hair: rgba(238,241,246,.14);
  --accent: #7ea6ff;
  --accent-ink: #06122c;
  --focus: #a5c4ff;
  color-scheme: dark;
}

@media (prefers-color-scheme: dark) {
  .dmu-17:not([data-theme="light"]):not(:has(#dmu-17-toggle:checked)) {
    --base: #0b0d12;
    --surface-0: #12151c;
    --surface-1: #181c25;
    --surface-2: #21262f;
    --surface-3: #2b313c;
    --ink: #eef1f6;
    --muted: #98a1b2;
    --hair: rgba(238,241,246,.14);
    --accent: #7ea6ff;
    --accent-ink: #06122c;
    --focus: #a5c4ff;
    color-scheme: dark;
  }
  /* mirrored flip-back: dark OS + checked restores the light ramp */

  .dmu-17:has(#dmu-17-toggle:checked) {
    --base: #f4f5f7;
    --surface-0: #ffffff;
    --surface-1: #f7f8fa;
    --surface-2: #eef0f4;
    --surface-3: #e5e8ee;
    --ink: #0b0d12;
    --muted: #5a6272;
    --hair: rgba(11,13,18,.12);
    --accent: #2563eb;
    --accent-ink: #ffffff;
    --focus: #2563eb;
    color-scheme: light;
  }
}

@supports (color: color-mix(in oklab, white 10%, black)) {
  .dmu-17[data-theme="dark"],
    .dmu-17:has(#dmu-17-toggle:checked) {
    --surface-0: color-mix(in oklab,var(--base),white 4%);
    --surface-1: color-mix(in oklab,var(--base),white 8%);
    --surface-2: color-mix(in oklab,var(--base),white 13%);
    --surface-3: color-mix(in oklab,var(--base),white 19%);
  }

  @media (prefers-color-scheme: dark) {
    .dmu-17:not([data-theme="light"]):not(:has(#dmu-17-toggle:checked)) {
      --surface-0: color-mix(in oklab,var(--base),white 4%);
      --surface-1: color-mix(in oklab,var(--base),white 8%);
      --surface-2: color-mix(in oklab,var(--base),white 13%);
      --surface-3: color-mix(in oklab,var(--base),white 19%);
    }
  }
}

.dmu-17,
.dmu-17 *,
.dmu-17 *::before,
.dmu-17 *::after {
  box-sizing: border-box;
}

.dmu-17__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.dmu-17__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3rem);
}

.dmu-17__wrap {
  width: min(68rem,100%);
  display: grid;
  gap: 1.25rem;
}

.dmu-17__head {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: 1rem;
  flex-wrap: wrap;
}

.dmu-17__kicker {
  margin: 0 0 .25rem;
  font-family: var(--mono);
  font-size: .7rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--accent);
}

.dmu-17__h1 {
  margin: 0;
  font-size: clamp(1.5rem,3.4vw,2.15rem);
  font-weight: 650;
  letter-spacing: -.035em;
}

.dmu-17__toggle {
  display: grid;
  place-items: center;
  width: 2.6rem;
  height: 2.6rem;
  border-radius: .7rem;
  cursor: pointer;
  background: var(--surface-0);
  color: var(--ink);
  border: 1px solid var(--hair);
  transition: background-color .2s ease;
}

.dmu-17__toggle:hover {
  background: var(--surface-2);
}

.dmu-17__toggle svg {
  width: 1.1rem;
  height: 1.1rem;
}

.dmu-17__sun {
  display: none;
}

.dmu-17__moon {
  display: block;
}

.dmu-17:has(#dmu-17-toggle:checked) .dmu-17__moon {
  display: none;
}

.dmu-17:has(#dmu-17-toggle:checked) .dmu-17__sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .dmu-17:not(:has(#dmu-17-toggle:checked)) .dmu-17__sun {
    display: block;
  }

  .dmu-17:not(:has(#dmu-17-toggle:checked)) .dmu-17__moon {
    display: none;
  }

  .dmu-17:has(#dmu-17-toggle:checked) .dmu-17__sun {
    display: none;
  }

  .dmu-17:has(#dmu-17-toggle:checked) .dmu-17__moon {
    display: block;
  }
}

.dmu-17:has(#dmu-17-toggle:focus-visible) .dmu-17__toggle {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}

.dmu-17__cols {
  display: grid;
  gap: 1.1rem;
  align-items: start;
}

@media (min-width: 58rem) {
  .dmu-17__cols {
    grid-template-columns: 20rem 1fr;
  }
}

.dmu-17__stack {
  position: relative;
  height: calc(var(--step) * 3 + 3rem);
}

.dmu-17__layer {
  position: absolute;
  left: 0;
  right: 0;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: .7rem .85rem;
  border-radius: .8rem;
  font-family: var(--mono);
  font-size: .72rem;
  border: 1px solid var(--hair);
}

.dmu-17__layer em {
  font-style: normal;
}

.dmu-17__layer b {
  font-weight: 500;
  color: var(--muted);
}

.dmu-17__layer--0 {
  top: 0;
  background: var(--surface-0);
}

.dmu-17__layer--1 {
  top: var(--step);
  left: .9rem;
  right: .9rem;
  background: var(--surface-1);
}

.dmu-17__layer--2 {
  top: calc(var(--step) * 2);
  left: 1.8rem;
  right: 1.8rem;
  background: var(--surface-2);
}

.dmu-17__layer--3 {
  top: calc(var(--step) * 3);
  left: 2.7rem;
  right: 2.7rem;
  background: var(--surface-3);
}

.dmu-17__tile {
  display: grid;
  gap: .9rem;
  padding: clamp(1.1rem,2.6vw,1.6rem);
  border-radius: 1.1rem;
  background: var(--surface-1);
  border: 1px solid var(--hair);
}

.dmu-17__tileHead {
  display: grid;
  gap: .3rem;
}

.dmu-17__badge {
  width: max-content;
  font-family: var(--mono);
  font-size: .66rem;
  padding: .24rem .45rem;
  border-radius: .35rem;
  background: color-mix(in oklab,var(--accent) 16%,transparent);
  color: var(--accent);
}

.dmu-17__badge--quiet {
  background: var(--surface-3);
  color: var(--muted);
}

.dmu-17__tileTitle {
  margin: 0;
  font-size: 1.1rem;
  font-weight: 620;
  letter-spacing: -.02em;
}

.dmu-17__tileSub {
  margin: 0;
  font-size: .85rem;
  color: var(--muted);
}

.dmu-17__subs {
  display: grid;
  gap: .65rem;
  grid-template-columns: repeat(auto-fit,minmax(11rem,1fr));
}

.dmu-17__sub {
  display: grid;
  gap: .28rem;
  padding: .85rem .9rem;
  border-radius: .8rem;
  background: var(--surface-2);
  border: 1px solid var(--hair);
  transition: background-color .2s ease;
}

.dmu-17__sub:hover {
  background: var(--surface-3);
}

.dmu-17__subTag {
  margin: 0;
  font-family: var(--mono);
  font-size: .64rem;
  color: var(--muted);
}

.dmu-17__subTitle {
  margin: 0;
  font-size: .88rem;
  font-weight: 560;
}

.dmu-17__subVal {
  margin: 0;
  font-family: var(--mono);
  font-size: .76rem;
  color: var(--muted);
}

.dmu-17__meter {
  height: .35rem;
  border-radius: 999px;
  background: var(--surface-0);
  overflow: hidden;
  margin-top: .2rem;
}

.dmu-17__meter i {
  display: block;
  width: var(--w);
  height: 100%;
  border-radius: 999px;
  background: var(--accent);
}

.dmu-17__tileFoot {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  flex-wrap: wrap;
}

.dmu-17__btn {
  min-height: 2.7rem;
  padding: 0 1.05rem;
  border-radius: .65rem;
  cursor: pointer;
  font: inherit;
  font-size: .85rem;
  font-weight: 560;
  background: var(--accent);
  color: var(--accent-ink);
  border: 0;
  transition: filter .18s ease, translate .18s ease;
}

.dmu-17__btn:hover {
  filter: brightness(1.06);
  translate: 0 -1px;
}

.dmu-17__btn:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .dmu-17__sub,
    .dmu-17__btn,
    .dmu-17__toggle {
    transition: none;
  }
}

@media (forced-colors: active) {
  .dmu-17__layer,
    .dmu-17__tile,
    .dmu-17__sub {
    border-color: CanvasText;
  }

  .dmu-17__meter i,
    .dmu-17__btn {
    background: Highlight;
    color: HighlightText;
  }
}
```
