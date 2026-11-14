---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-dark-mode-ui/dark-mode-modal-dialog-with-backdrop/"
title: "Dark Mode Modal Dialog with Backdrop"
section: "design-styles"
category: "css-dark-mode-ui"
category_name: "CSS Dark Mode UI"
description: "A modal surface that behaves like a real one without a line of script: a <details> disclosure supplies the open state, the <summary> doubles as the trigger…"
has_js: "false"
---

Here's a working CSS Dark Mode UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dark Mode Modal Dialog with Backdrop
Source: https://codefronts.com/design-styles/css-dark-mode-ui/dark-mode-modal-dialog-with-backdrop/

A modal surface that behaves like a real one without a line of script: a <details> disclosure supplies the open state, the <summary> doubles as the trigger and the dismiss control, and a fixed blurred backdrop sits between them. The sheet uses an elevated surface with an inner-glow hairline — the detail that separates a dark modal from a grey box — and animates in with @starting-style so the entrance costs nothing at runtime.
## HTML
```html
<div class="dmu-07">
  <div class="dmu-07__stage">
    <div class="dmu-07__page">
      <header class="dmu-07__pageBar">
        <div>
          <p class="dmu-07__crumb">Settings / Danger zone</p>
          <h1 class="dmu-07__h1">acme-platform</h1>
        </div>
        <div class="dmu-07__pageTools">
          <input class="dmu-07__sr" type="checkbox" id="dmu-07-toggle">
          <label class="dmu-07__toggle" for="dmu-07-toggle">
            <svg class="dmu-07__sun" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"><circle cx="12" cy="12" r="4"/><path d="M12 2.8v2M12 19.2v2M2.8 12h2M19.2 12h2M5.5 5.5 7 7M17 17l1.5 1.5M18.5 5.5 17 7M7 17l-1.5 1.5"/></svg>
            <svg class="dmu-07__moon" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M20 14.4A8.4 8.4 0 0 1 9.6 4a8.4 8.4 0 1 0 10.4 10.4Z"/></svg>
            <span class="dmu-07__sr">Toggle theme</span>
          </label>
        </div>
      </header>

      <p class="dmu-07__blurb">Deleting a workspace removes every deployment, environment variable and log stream it owns. The confirmation sheet below is a pure-CSS disclosure &mdash; no script, no focus-trap library.</p>

      <details class="dmu-07__d">
        <summary class="dmu-07__trigger">
          <span class="dmu-07__triggerBody">
            <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M4.5 7.5h15M9.5 7.5V5.2h5v2.3M6.6 7.5l.9 12h9l.9-12"/><path d="M10.4 11v5M13.6 11v5"/></svg>
            Delete workspace
          </span>
          <span class="dmu-07__close" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round"><path d="M6.5 6.5l11 11M17.5 6.5l-11 11"/></svg>
          </span>
        </summary>

        <div class="dmu-07__sheet" role="dialog" aria-labelledby="dmu-07-title" aria-describedby="dmu-07-desc">
          <div class="dmu-07__sheetHead">
            <span class="dmu-07__warn" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M12 4.6 21 19.4H3Z"/><path d="M12 10v4.1M12 16.6v.1"/></svg>
            </span>
            <div>
              <h2 class="dmu-07__title" id="dmu-07-title">Delete this workspace?</h2>
              <p class="dmu-07__desc" id="dmu-07-desc">This cannot be undone. 3 projects, 41 deployments and 12 secrets will be permanently removed.</p>
            </div>
          </div>

          <dl class="dmu-07__facts">
            <div><dt>Workspace</dt><dd>acme-platform</dd></div>
            <div><dt>Owner</dt><dd>Sam Rivera</dd></div>
            <div><dt>Region</dt><dd>iad1</dd></div>
          </dl>

          <label class="dmu-07__field" for="dmu-07-confirm">
            <span>Type <strong>acme-platform</strong> to confirm</span>
            <input class="dmu-07__input" id="dmu-07-confirm" type="text" placeholder="acme-platform" autocomplete="off" spellcheck="false">
          </label>

          <div class="dmu-07__row">
            <p class="dmu-07__hint">Deletion runs immediately.</p>
            <div class="dmu-07__btns">
              <button class="dmu-07__btn" type="button">Keep workspace</button>
              <button class="dmu-07__btn dmu-07__btn--danger" type="button">Delete forever</button>
            </div>
          </div>
        </div>
      </details>
    </div>
  </div>
</div>
```
## CSS
```css
.dmu-07 {
  --bg: #0a0a0e;
  --surface: #121218;
  --elevated: #1a1a23;
  --ink: #f4f4f6;
  --muted: #9494a3;
  --line: #282833;
  --sheen: rgba(255,255,255,.06);
  --ring-glow: rgba(255,255,255,.04);
  --accent: #f472b6;
  --danger: #fb7185;
  --danger-ink: #26060f;
  --focus: #7dd3fc;
  --scrim: rgba(5,5,9,.72);
  --field: #0e0e14;
  --sheet-w: 31rem;
  --shadow: rgba(0,0,0,.8);
  --sans: system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: ui-monospace,"SF Mono","JetBrains Mono",Menlo,monospace;
  color-scheme: dark;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.dmu-07[data-theme="light"],
.dmu-07:has(#dmu-07-toggle:checked) {
  --bg: #f4f4f7;
  --surface: #ffffff;
  --elevated: #ffffff;
  --ink: #0b0b12;
  --muted: #5c6270;
  --line: #e3e4ea;
  --sheen: rgba(11,11,18,.03);
  --ring-glow: rgba(11,11,18,.05);
  --accent: #be185d;
  --danger: #be123c;
  --danger-ink: #ffffff;
  --focus: #1d4ed8;
  --scrim: rgba(15,15,25,.42);
  --field: #f7f7fa;
  --shadow: rgba(11,11,18,.22);
  color-scheme: light;
}

@media (prefers-color-scheme: light) {
  .dmu-07:not([data-theme="dark"]):not(:has(#dmu-07-toggle:checked)) {
    --bg: #f4f4f7;
    --surface: #ffffff;
    --elevated: #ffffff;
    --ink: #0b0b12;
    --muted: #5c6270;
    --line: #e3e4ea;
    --sheen: rgba(11,11,18,.03);
    --ring-glow: rgba(11,11,18,.05);
    --accent: #be185d;
    --danger: #be123c;
    --danger-ink: #ffffff;
    --focus: #1d4ed8;
    --scrim: rgba(15,15,25,.42);
    --field: #f7f7fa;
    --shadow: rgba(11,11,18,.22);
    color-scheme: light;
  }

  .dmu-07:has(#dmu-07-toggle:checked) {
    --bg: #0a0a0e;
    --surface: #121218;
    --elevated: #1a1a23;
    --ink: #f4f4f6;
    --muted: #9494a3;
    --line: #282833;
    --sheen: rgba(255,255,255,.06);
    --ring-glow: rgba(255,255,255,.04);
    --accent: #f472b6;
    --danger: #fb7185;
    --danger-ink: #26060f;
    --focus: #7dd3fc;
    --scrim: rgba(5,5,9,.72);
    --field: #0e0e14;
    --shadow: rgba(0,0,0,.8);
    color-scheme: dark;
  }
}

.dmu-07,
.dmu-07 *,
.dmu-07 *::before,
.dmu-07 *::after {
  box-sizing: border-box;
}

.dmu-07__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.dmu-07__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3rem);
}

.dmu-07__page {
  width: min(46rem,100%);
  display: grid;
  gap: 1.1rem;
  padding: clamp(1.25rem,3vw,2rem);
  border-radius: 1.15rem;
  background: var(--surface);
  border: 1px solid var(--line);
  box-shadow: 0 30px 60px -46px var(--shadow);
}

.dmu-07__pageBar {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 1rem;
}

.dmu-07__crumb {
  margin: 0 0 .3rem;
  font-family: var(--mono);
  font-size: .72rem;
  color: var(--muted);
}

.dmu-07__h1 {
  margin: 0;
  font-size: clamp(1.35rem,3vw,1.8rem);
  font-weight: 650;
  letter-spacing: -.03em;
}

.dmu-07__pageTools {
  display: flex;
  gap: .5rem;
}

.dmu-07__toggle {
  display: grid;
  place-items: center;
  width: 2.6rem;
  height: 2.6rem;
  border-radius: .7rem;
  cursor: pointer;
  background: var(--elevated);
  border: 1px solid var(--line);
  color: var(--ink);
  transition: border-color .2s ease;
}

.dmu-07__toggle:hover {
  border-color: color-mix(in oklab,var(--focus) 50%,var(--line));
}

.dmu-07__toggle svg {
  width: 1.1rem;
  height: 1.1rem;
}

.dmu-07__sun {
  display: none;
}

.dmu-07__moon {
  display: block;
}

.dmu-07:has(#dmu-07-toggle:checked) .dmu-07__sun {
  display: block;
}

.dmu-07:has(#dmu-07-toggle:checked) .dmu-07__moon {
  display: none;
}

@media (prefers-color-scheme: light) {
  .dmu-07:not(:has(#dmu-07-toggle:checked)) .dmu-07__sun {
    display: block;
  }

  .dmu-07:not(:has(#dmu-07-toggle:checked)) .dmu-07__moon {
    display: none;
  }

  .dmu-07:has(#dmu-07-toggle:checked) .dmu-07__sun {
    display: none;
  }

  .dmu-07:has(#dmu-07-toggle:checked) .dmu-07__moon {
    display: block;
  }
}

.dmu-07:has(#dmu-07-toggle:focus-visible) .dmu-07__toggle {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}

.dmu-07__blurb {
  margin: 0;
  font-size: .92rem;
  line-height: 1.65;
  color: var(--muted);
  max-width: 60ch;
  text-wrap: pretty;
}

.dmu-07__d {
  position: relative;
}

.dmu-07__d summary {
  list-style: none;
}

.dmu-07__d summary::-webkit-details-marker {
  display: none;
}

.dmu-07__trigger {
  display: inline-flex;
  cursor: pointer;
}

.dmu-07__triggerBody {
  display: inline-flex;
  align-items: center;
  gap: .5rem;
  min-height: 2.85rem;
  padding: 0 1.05rem;
  border-radius: .65rem;
  font-size: .88rem;
  font-weight: 560;
  color: var(--danger);
  background: color-mix(in oklab,var(--danger) 12%,transparent);
  border: 1px solid color-mix(in oklab,var(--danger) 40%,transparent);
  transition: background-color .2s ease, translate .2s ease;
}

.dmu-07__triggerBody svg {
  width: 1.05rem;
  height: 1.05rem;
}

.dmu-07__trigger:hover .dmu-07__triggerBody {
  background: color-mix(in oklab,var(--danger) 20%,transparent);
  translate: 0 -1px;
}

.dmu-07__trigger:focus-visible {
  outline: none;
}

.dmu-07__trigger:focus-visible .dmu-07__triggerBody {
  outline: 2px solid var(--focus);
  outline-offset: 3px;
}

.dmu-07__close {
  display: none;
}

.dmu-07__d[open] .dmu-07__triggerBody {
  opacity: .35;
}

.dmu-07__d[open] .dmu-07__trigger::after {
  content: '';
  position: fixed;
  inset: 0;
  z-index: 5;
  background: var(--scrim);
  -webkit-backdrop-filter: blur(8px) saturate(.9);
  backdrop-filter: blur(8px) saturate(.9);
}

.dmu-07__d[open] .dmu-07__close {
  position: fixed;
  z-index: 7;
  top: 1.15rem;
  right: 1.15rem;
  display: grid;
  place-items: center;
  width: 2.6rem;
  height: 2.6rem;
  border-radius: 50%;
  background: var(--elevated);
  color: var(--ink);
  border: 1px solid var(--line);
  box-shadow: 0 8px 20px -12px var(--shadow);
}

.dmu-07__close svg {
  width: 1rem;
  height: 1rem;
}

.dmu-07__sheet {
  position: fixed;
  z-index: 6;
  top: 50%;
  left: 50%;
  translate: -50% -50%;
  width: min(var(--sheet-w),calc(100% - 2rem));
  max-height: min(86vh,40rem);
  overflow: auto;
  display: grid;
  gap: 1rem;
  padding: clamp(1.15rem,3vw,1.6rem);
  border-radius: 1.1rem;
  background: linear-gradient(180deg,var(--elevated),var(--surface));
  border: 1px solid var(--line);
  color: var(--ink);
  box-shadow: inset 0 1px 0 var(--sheen), 0 0 0 1px var(--ring-glow), 0 44px 80px -40px var(--shadow);
  opacity: 1;
  scale: 1;
  transition: opacity .24s ease, scale .24s cubic-bezier(.16,1,.3,1);
}

@starting-style {
  .dmu-07__d[open] .dmu-07__sheet {
    opacity: 0;
    scale: .96;
  }
}

.dmu-07__sheetHead {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: .85rem;
  align-items: start;
}

.dmu-07__warn {
  display: grid;
  place-items: center;
  width: 2.5rem;
  height: 2.5rem;
  border-radius: .7rem;
  background: color-mix(in oklab,var(--danger) 15%,transparent);
  color: var(--danger);
}

.dmu-07__warn svg {
  width: 1.25rem;
  height: 1.25rem;
}

.dmu-07__title {
  margin: 0 0 .3rem;
  font-size: 1.12rem;
  font-weight: 650;
  letter-spacing: -.025em;
}

.dmu-07__desc {
  margin: 0;
  font-size: .86rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.dmu-07__facts {
  margin: 0;
  display: grid;
  gap: .3rem;
  padding: .75rem .85rem;
  border-radius: .7rem;
  background: var(--field);
  border: 1px solid var(--line);
}

.dmu-07__facts div {
  display: grid;
  grid-template-columns: 7rem 1fr;
  gap: .6rem;
  font-size: .8rem;
}

.dmu-07__facts dt {
  color: var(--muted);
}

.dmu-07__facts dd {
  margin: 0;
  font-family: var(--mono);
}

.dmu-07__field {
  display: grid;
  gap: .4rem;
  font-size: .8rem;
  color: var(--muted);
}

.dmu-07__field strong {
  color: var(--ink);
  font-family: var(--mono);
  font-weight: 600;
}

.dmu-07__input {
  min-height: 2.85rem;
  padding: 0 .8rem;
  border-radius: .6rem;
  font: inherit;
  font-size: .9rem;
  background: var(--field);
  color: var(--ink);
  border: 1px solid var(--line);
  transition: border-color .18s ease, box-shadow .18s ease;
}

.dmu-07__input::placeholder {
  color: color-mix(in oklab,var(--muted) 70%,transparent);
}

.dmu-07__input:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 1px;
  border-color: var(--focus);
}

.dmu-07__row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  flex-wrap: wrap;
}

.dmu-07__hint {
  margin: 0;
  font-size: .76rem;
  color: var(--muted);
}

.dmu-07__btns {
  display: flex;
  gap: .5rem;
  flex-wrap: wrap;
}

.dmu-07__btn {
  min-height: 2.75rem;
  padding: 0 1rem;
  border-radius: .6rem;
  cursor: pointer;
  font: inherit;
  font-size: .85rem;
  font-weight: 560;
  background: var(--elevated);
  color: var(--ink);
  border: 1px solid var(--line);
  transition: translate .18s ease, filter .18s ease;
}

.dmu-07__btn:hover {
  translate: 0 -1px;
}

.dmu-07__btn:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}

.dmu-07__btn--danger {
  background: var(--danger);
  color: var(--danger-ink);
  border-color: transparent;
}

.dmu-07__btn--danger:hover {
  filter: brightness(1.06);
}

@media (prefers-reduced-motion: reduce) {
  .dmu-07__sheet,
    .dmu-07__btn,
    .dmu-07__triggerBody,
    .dmu-07__input,
    .dmu-07__toggle {
    transition: none;
  }
}

@media (forced-colors: active) {
  .dmu-07__sheet,
    .dmu-07__page,
    .dmu-07__facts,
    .dmu-07__input {
    border-color: CanvasText;
    box-shadow: none;
  }

  .dmu-07__d[open] .dmu-07__trigger::after {
    background: Canvas;
    backdrop-filter: none;
  }

  .dmu-07__btn--danger {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
  }
}
```
