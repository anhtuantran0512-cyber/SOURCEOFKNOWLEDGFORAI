---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-dark-mode-ui/mocha-workstation/"
title: "Mocha Warm Dark Mode Workstation"
section: "design-styles"
category: "css-dark-mode-ui"
category_name: "CSS Dark Mode UI"
description: "Dark mode without the cold: a warm substrate of roasted browns, cream ink and a single burnt-orange accent, built as a focus writing surface with a title…"
has_js: "false"
---

Here's a working CSS Dark Mode UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Mocha Warm Dark Mode Workstation
Source: https://codefronts.com/design-styles/css-dark-mode-ui/mocha-workstation/

Dark mode without the cold: a warm substrate of roasted browns, cream ink and a single burnt-orange accent, built as a focus writing surface with a title field, tag chips, word count and long-form copy. Warm dark themes measurably reduce the blue component of a bright screen at night, and they read as calm rather than clinical — Solarized's idea, rebuilt with 2027 typography and token discipline.
## HTML
```html
<div class="dmu-15">
  <div class="dmu-15__stage">
    <div class="dmu-15__desk">
      <header class="dmu-15__bar">
        <span class="dmu-15__brand">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5.5 8.5h11v5a5.5 5.5 0 0 1-11 0Z"/><path d="M16.5 9.5h1.6a2.2 2.2 0 0 1 0 4.4h-1.6"/><path d="M5 20.5h12"/></svg>
          Mocha
        </span>
        <span class="dmu-15__meta">Draft &middot; saved 2 min ago</span>
        <span class="dmu-15__count">1,248 words</span>
        <input class="dmu-15__sr" type="checkbox" id="dmu-15-toggle">
        <label class="dmu-15__toggle" for="dmu-15-toggle">
          <svg class="dmu-15__sun" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"><circle cx="12" cy="12" r="4"/><path d="M12 2.8v2M12 19.2v2M2.8 12h2M19.2 12h2M5.5 5.5 7 7M17 17l1.5 1.5M18.5 5.5 17 7M7 17l-1.5 1.5"/></svg>
          <svg class="dmu-15__moon" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M20 14.4A8.4 8.4 0 0 1 9.6 4a8.4 8.4 0 1 0 10.4 10.4Z"/></svg>
          <span class="dmu-15__sr">Toggle theme</span>
        </label>
      </header>

      <div class="dmu-15__sheet">
        <label class="dmu-15__sr" for="dmu-15-title">Document title</label>
        <input class="dmu-15__title" id="dmu-15-title" type="text" value="Designing for the last hour of the day" spellcheck="false">

        <div class="dmu-15__tags">
          <input class="dmu-15__sr" type="checkbox" id="dmu-15-t1" checked>
          <label class="dmu-15__tag" for="dmu-15-t1">craft</label>
          <input class="dmu-15__sr" type="checkbox" id="dmu-15-t2" checked>
          <label class="dmu-15__tag" for="dmu-15-t2">dark mode</label>
          <input class="dmu-15__sr" type="checkbox" id="dmu-15-t3">
          <label class="dmu-15__tag" for="dmu-15-t3">typography</label>
          <input class="dmu-15__sr" type="checkbox" id="dmu-15-t4">
          <label class="dmu-15__tag" for="dmu-15-t4">research</label>
        </div>

        <div class="dmu-15__doc">
          <p>Most dark themes are built at noon. They are drawn on a bright display in a bright room, then shipped to people reading at eleven at night with the lights off &mdash; which is why so many of them feel like a photographic negative rather than a designed surface.</p>
          <p>Warm neutrals fix more than they should. Pulling the substrate toward brown drops the blue component of a mostly-lit screen, and cream ink at 4.7:1 stays comfortable far longer than pure white at 15:1. The palette does the work an eye-strain setting pretends to.</p>
          <p>The rule I keep: one accent, and it earns its place. Here the ember only marks the caret, the active tags and the primary action. Everything else is substrate, ink and one hairline.</p>
          <p class="dmu-15__pull">A dark theme is not a colour inversion. It is a second design with the same information architecture.</p>
        </div>

        <footer class="dmu-15__foot">
          <div class="dmu-15__chips">
            <span class="dmu-15__chipInfo">Focus mode</span>
            <span class="dmu-15__chipInfo">65ch measure</span>
          </div>
          <div class="dmu-15__acts">
            <button class="dmu-15__btn" type="button">Preview</button>
            <button class="dmu-15__btn dmu-15__btn--primary" type="button">Publish draft</button>
          </div>
        </footer>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.dmu-15 {
  --bean: #171210;
  --crema: #1f1815;
  --foam: #2a201c;
  --hair: rgba(243,233,223,.12);
  --cream: #f3e9df;
  --milk: #bfa99b;
  --ember: #e0703c;
  --ember-ink: #1a0a04;
  --focus: #f0a06a;
  --sel: rgba(224,112,60,.28);
  --sans: system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: ui-monospace,"SF Mono","JetBrains Mono",Menlo,monospace;
  color-scheme: dark;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: radial-gradient(120% 80% at 15% 0%,#1e1714,var(--bean) 62%),var(--bean);
  color: var(--cream);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.dmu-15[data-theme="light"],
.dmu-15:has(#dmu-15-toggle:checked) {
  --bean: #f4ece3;
  --crema: #fdf8f2;
  --foam: #f6ece1;
  --hair: rgba(52,34,24,.14);
  --cream: #2a1c14;
  --milk: #7a6353;
  --ember: #b4471a;
  --ember-ink: #fff8f3;
  --focus: #b4471a;
  --sel: rgba(180,71,26,.20);
  background: radial-gradient(120% 80% at 15% 0%,#fdf7f0,var(--bean) 62%),var(--bean);
  color-scheme: light;
}

@media (prefers-color-scheme: light) {
  .dmu-15:not([data-theme="dark"]):not(:has(#dmu-15-toggle:checked)) {
    --bean: #f4ece3;
    --crema: #fdf8f2;
    --foam: #f6ece1;
    --hair: rgba(52,34,24,.14);
    --cream: #2a1c14;
    --milk: #7a6353;
    --ember: #b4471a;
    --ember-ink: #fff8f3;
    --focus: #b4471a;
    --sel: rgba(180,71,26,.20);
    background: radial-gradient(120% 80% at 15% 0%,#fdf7f0,var(--bean) 62%),var(--bean);
    color-scheme: light;
  }
  /* flip-back: light OS + checked restores the roasted base */

  .dmu-15:has(#dmu-15-toggle:checked) {
    --bean: #171210;
    --crema: #1f1815;
    --foam: #2a201c;
    --hair: rgba(243,233,223,.12);
    --cream: #f3e9df;
    --milk: #bfa99b;
    --ember: #e0703c;
    --ember-ink: #1a0a04;
    --focus: #f0a06a;
    --sel: rgba(224,112,60,.28);
    background: radial-gradient(120% 80% at 15% 0%,#1e1714,var(--bean) 62%),var(--bean);
    color-scheme: dark;
  }
}

.dmu-15,
.dmu-15 *,
.dmu-15 *::before,
.dmu-15 *::after {
  box-sizing: border-box;
}

.dmu-15 ::selection {
  background: var(--sel);
  color: var(--cream);
}

.dmu-15__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.dmu-15__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3rem);
}

.dmu-15__desk {
  width: min(56rem,100%);
  display: grid;
  gap: .75rem;
}

.dmu-15__bar {
  display: flex;
  align-items: center;
  gap: .85rem;
  flex-wrap: wrap;
  padding: .15rem .35rem;
}

.dmu-15__brand {
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  font-size: .88rem;
  font-weight: 600;
  letter-spacing: -.01em;
}

.dmu-15__brand svg {
  width: 1.15rem;
  height: 1.15rem;
  color: var(--ember);
}

.dmu-15__meta,
.dmu-15__count {
  font-family: var(--mono);
  font-size: .72rem;
  color: var(--milk);
}

.dmu-15__count {
  margin-left: auto;
}

.dmu-15__toggle {
  display: grid;
  place-items: center;
  width: 2.4rem;
  height: 2.4rem;
  border-radius: .65rem;
  cursor: pointer;
  color: var(--cream);
  background: var(--crema);
  border: 1px solid var(--hair);
  transition: background-color .2s ease;
}

.dmu-15__toggle:hover {
  background: var(--foam);
}

.dmu-15__toggle svg {
  width: 1.05rem;
  height: 1.05rem;
}

.dmu-15__sun {
  display: none;
}

.dmu-15__moon {
  display: block;
}

.dmu-15:has(#dmu-15-toggle:checked) .dmu-15__sun {
  display: block;
}

.dmu-15:has(#dmu-15-toggle:checked) .dmu-15__moon {
  display: none;
}

@media (prefers-color-scheme: light) {
  .dmu-15:not(:has(#dmu-15-toggle:checked)) .dmu-15__sun {
    display: block;
  }

  .dmu-15:not(:has(#dmu-15-toggle:checked)) .dmu-15__moon {
    display: none;
  }

  .dmu-15:has(#dmu-15-toggle:checked) .dmu-15__sun {
    display: none;
  }

  .dmu-15:has(#dmu-15-toggle:checked) .dmu-15__moon {
    display: block;
  }
}

.dmu-15:has(#dmu-15-toggle:focus-visible) .dmu-15__toggle {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}

.dmu-15__sheet {
  display: grid;
  gap: .85rem;
  padding: clamp(1.35rem,4vw,2.5rem);
  border-radius: 1.2rem;
  background: var(--crema);
  border: 1px solid var(--hair);
}

.dmu-15__title {
  width: 100%;
  border: 0;
  background: transparent;
  color: var(--cream);
  font: inherit;
  font-size: clamp(1.5rem,3.6vw,2.15rem);
  font-weight: 650;
  letter-spacing: -.035em;
  padding: 0;
  caret-color: var(--ember);
}

.dmu-15__title:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 4px;
  border-radius: .3rem;
}

.dmu-15__tags {
  display: flex;
  gap: .4rem;
  flex-wrap: wrap;
}

.dmu-15__tag {
  display: inline-flex;
  align-items: center;
  min-height: 2.1rem;
  padding: 0 .75rem;
  border-radius: 999px;
  cursor: pointer;
  font-size: .76rem;
  color: var(--milk);
  border: 1px solid var(--hair);
  transition: background-color .18s ease, color .18s ease, border-color .18s ease;
}

.dmu-15__tag::before {
  content: '#';
  margin-right: .15rem;
  opacity: .6;
}

.dmu-15__tag:hover {
  color: var(--cream);
}

.dmu-15__tags input:checked + .dmu-15__tag {
  color: var(--cream);
  border-color: color-mix(in oklab,var(--ember) 55%,transparent);
  background: color-mix(in oklab,var(--ember) 18%,transparent);
}

.dmu-15__tags input:focus-visible + .dmu-15__tag {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}

.dmu-15__doc {
  display: grid;
  gap: .9rem;
  max-width: 65ch;
}

.dmu-15__doc p {
  margin: 0;
  font-size: 1rem;
  line-height: 1.75;
  color: var(--cream);
  text-wrap: pretty;
}

.dmu-15__doc p:first-child::first-letter {
  font-size: 1.05em;
  font-weight: 600;
}

.dmu-15__pull {
  padding-left: 1rem;
  border-left: 2px solid var(--ember);
  color: var(--milk) !important;
  font-style: italic;
}

.dmu-15__foot {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  flex-wrap: wrap;
  padding-top: .85rem;
  border-top: 1px solid var(--hair);
}

.dmu-15__chips {
  display: flex;
  gap: .4rem;
  flex-wrap: wrap;
}

.dmu-15__chipInfo {
  font-family: var(--mono);
  font-size: .7rem;
  color: var(--milk);
  padding: .3rem .55rem;
  border-radius: .4rem;
  background: var(--foam);
}

.dmu-15__acts {
  display: flex;
  gap: .5rem;
}

.dmu-15__btn {
  min-height: 2.8rem;
  padding: 0 1.1rem;
  border-radius: .7rem;
  cursor: pointer;
  font: inherit;
  font-size: .86rem;
  font-weight: 560;
  background: var(--foam);
  color: var(--cream);
  border: 1px solid var(--hair);
  transition: translate .18s ease, filter .18s ease;
}

.dmu-15__btn:hover {
  translate: 0 -1px;
}

.dmu-15__btn:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 3px;
}

.dmu-15__btn--primary {
  background: var(--ember);
  color: var(--ember-ink);
  border-color: transparent;
}

.dmu-15__btn--primary:hover {
  filter: brightness(1.06);
}

@media (prefers-reduced-motion: reduce) {
  .dmu-15__btn,
    .dmu-15__tag,
    .dmu-15__toggle {
    transition: none;
  }
}

@media (forced-colors: active) {
  .dmu-15__sheet,
    .dmu-15__tag,
    .dmu-15__btn {
    border-color: CanvasText;
  }

  .dmu-15__btn--primary {
    background: ButtonFace;
    color: ButtonText;
  }

  .dmu-15__tags input:checked + .dmu-15__tag {
    background: Highlight;
    color: HighlightText;
  }
}
```
