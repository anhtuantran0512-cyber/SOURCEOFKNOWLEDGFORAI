---
source: "codefronts"
url: "https://codefronts.com/components/css-search-boxes/command-palette-cmd-k-search-bar/"
title: "Command Palette Cmd+K Search Bar"
section: "components"
category: "css-search-boxes"
category_name: "CSS Search Bars"
description: "The ⌘K palette every modern product ships — a native <dialog> that opens on Command/Control + K, filters grouped commands, pages and people as you type,…"
has_js: "true"
---

Here's a working CSS Search Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Command Palette Cmd+K Search Bar
Source: https://codefronts.com/components/css-search-boxes/command-palette-cmd-k-search-bar/

The ⌘K palette every modern product ships — a native <dialog> that opens on Command/Control + K, filters grouped commands, pages and people as you type, moves an active option with the arrow keys through aria-activedescendant, and returns focus to the trigger on Escape. Blurred ::backdrop, a spring-in with @starting-style, and empty groups that hide themselves with :has().
## HTML
```html
<div class="sb-01">
  <button class="sb-01__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="sb-01__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="sb-01__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <div class="sb-01__stage">
    <button class="sb-01__trigger" type="button" id="sb-01-open" aria-haspopup="dialog" aria-expanded="false" aria-controls="sb-01-dialog">
      <svg class="sb-01__ico" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6.4" stroke="currentColor" stroke-width="1.7"/><path d="m16 16 4.2 4.2" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
      <span class="sb-01__trigger-txt">Search or jump to&hellip;</span>
      <kbd class="sb-01__kbd"><abbr title="Command">&#8984;</abbr>K</kbd>
    </button>

    <dialog class="sb-01__palette" id="sb-01-dialog" aria-label="Command palette">
      <div class="sb-01__field" role="search">
        <svg class="sb-01__ico sb-01__ico--lg" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6.4" stroke="currentColor" stroke-width="1.7"/><path d="m16 16 4.2 4.2" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
        <label class="sb-01__vh" for="sb-01-input">Search commands, pages and people</label>
        <input class="sb-01__input" id="sb-01-input" type="search" role="combobox" placeholder="Type a command or search&hellip;" autocomplete="off" spellcheck="false" aria-controls="sb-01-list" aria-expanded="true" aria-activedescendant="sb-01-o1">
        <kbd class="sb-01__kbd sb-01__kbd--esc">esc</kbd>
      </div>

      <div class="sb-01__scroll">
        <ul class="sb-01__list" id="sb-01-list" role="listbox" aria-label="Commands, pages and people">
          <li class="sb-01__sect" role="presentation">
            <p class="sb-01__sect-h" id="sb-01-h1">Recent</p>
            <ul class="sb-01__sub" role="group" aria-labelledby="sb-01-h1">
              <li class="sb-01__opt" role="option" id="sb-01-o1" aria-selected="true">
                <span class="sb-01__tile" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M6 3.5h7.5L18 8v12.5H6z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M13 3.5V8h5" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg></span>
                <span class="sb-01__label">Q3 revenue forecast<small>Finance &middot; edited 2h ago</small></span>
                <svg class="sb-01__go" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M5 12h13m-5.5-5.5L18 12l-5.5 5.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>
              </li>
              <li class="sb-01__opt" role="option" id="sb-01-o2" aria-selected="false">
                <span class="sb-01__tile" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" focusable="false"><rect x="3.5" y="5" width="17" height="14" rx="2.5" stroke="currentColor" stroke-width="1.6"/><path d="M3.5 9.5h17" stroke="currentColor" stroke-width="1.6"/></svg></span>
                <span class="sb-01__label">Onboarding checklist<small>Product &middot; edited yesterday</small></span>
                <svg class="sb-01__go" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M5 12h13m-5.5-5.5L18 12l-5.5 5.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>
              </li>
              <li class="sb-01__opt" role="option" id="sb-01-o3" aria-selected="false">
                <span class="sb-01__tile" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M4 18V9m5 9V5m5 13v-6m5 6V8" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg></span>
                <span class="sb-01__label">Analytics &rsaquo; Retention<small>Dashboard</small></span>
                <svg class="sb-01__go" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M5 12h13m-5.5-5.5L18 12l-5.5 5.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>
              </li>
            </ul>
          </li>

          <li class="sb-01__sect" role="presentation">
            <p class="sb-01__sect-h" id="sb-01-h2">Actions</p>
            <ul class="sb-01__sub" role="group" aria-labelledby="sb-01-h2">
              <li class="sb-01__opt" role="option" id="sb-01-o4" aria-selected="false">
                <span class="sb-01__tile" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M12 5v14M5 12h14" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg></span>
                <span class="sb-01__label">Create new document</span>
                <kbd class="sb-01__kbd">&#8984;N</kbd>
              </li>
              <li class="sb-01__opt" role="option" id="sb-01-o5" aria-selected="false">
                <span class="sb-01__tile" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M12 4v3m0 10v3m8-8h-3M7 12H4m12.9-4.9-2.1 2.1M9.2 14.8l-2.1 2.1m9.8 0-2.1-2.1M9.2 9.2 7.1 7.1" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><circle cx="12" cy="12" r="2.6" stroke="currentColor" stroke-width="1.6"/></svg></span>
                <span class="sb-01__label">Open workspace settings</span>
                <kbd class="sb-01__kbd">&#8984;,</kbd>
              </li>
              <li class="sb-01__opt" role="option" id="sb-01-o6" aria-selected="false">
                <span class="sb-01__tile" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M16 19a4 4 0 0 0-8 0" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><circle cx="12" cy="9" r="3.2" stroke="currentColor" stroke-width="1.6"/><path d="M19 8.5V5.5h-3" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg></span>
                <span class="sb-01__label">Invite teammates</span>
                <kbd class="sb-01__kbd">&#8984;I</kbd>
              </li>
            </ul>
          </li>

          <li class="sb-01__sect" role="presentation">
            <p class="sb-01__sect-h" id="sb-01-h3">People</p>
            <ul class="sb-01__sub" role="group" aria-labelledby="sb-01-h3">
              <li class="sb-01__opt" role="option" id="sb-01-o7" aria-selected="false">
                <span class="sb-01__av sb-01__av--a" aria-hidden="true">AC</span>
                <span class="sb-01__label">Alex Chen<small>Design engineer &middot; online</small></span>
                <svg class="sb-01__go" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M5 12h13m-5.5-5.5L18 12l-5.5 5.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>
              </li>
              <li class="sb-01__opt" role="option" id="sb-01-o8" aria-selected="false">
                <span class="sb-01__av sb-01__av--b" aria-hidden="true">PS</span>
                <span class="sb-01__label">Priya Sharma<small>Product lead</small></span>
                <svg class="sb-01__go" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M5 12h13m-5.5-5.5L18 12l-5.5 5.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>
              </li>
            </ul>
          </li>
        </ul>
        <p class="sb-01__empty" id="sb-01-empty" role="status" hidden>No matching commands</p>
      </div>

      <footer class="sb-01__foot">
        <span class="sb-01__hint"><kbd class="sb-01__kbd">&uarr;</kbd><kbd class="sb-01__kbd">&darr;</kbd> navigate</span>
        <span class="sb-01__hint"><kbd class="sb-01__kbd">&crarr;</kbd> open</span>
        <span class="sb-01__hint"><kbd class="sb-01__kbd">esc</kbd> close</span>
      </footer>
    </dialog>
  </div>
</div>
```
## CSS
```css
.sb-01 {
  --bg: #08080c;
  --panel: #101017;
  --panel-2: #16161f;
  --ink: #f5f5f8;
  --muted: #8d8da4;
  --line: #24242f;
  --acc: #8b7cff;
  --acc-ink: #c9c2ff;
  --wash: rgba(139,124,255,.14);
  --ring: #a99bff;
  --shadow: rgba(0,0,0,.75);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  box-sizing: border-box;
  font-family: system-ui,-apple-system,"Segoe UI",sans-serif;
  color: var(--ink);
  background: radial-gradient(58rem 34rem at 12% -12%, rgba(139,124,255,.20), transparent 68%), radial-gradient(46rem 30rem at 108% 112%, rgba(56,189,248,.14), transparent 68%), var(--bg);
  -webkit-font-smoothing: antialiased;
}

.sb-01 *,
.sb-01 *::before,
.sb-01 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(50% .1 270)) {
  .sb-01 {
    --bg: oklch(14% .02 285);
    --panel: oklch(18% .02 285);
    --panel-2: oklch(22% .022 285);
    --ink: oklch(97% .005 285);
    --muted: oklch(68% .02 285);
    --line: oklch(28% .02 285);
    --acc: oklch(70% .17 292);
    --acc-ink: oklch(84% .11 292);
    --wash: color-mix(in oklab, oklch(70% .17 292) 16%, transparent);
    --ring: oklch(78% .14 292);
  }
}

.sb-01__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3rem);
}

.sb-01__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}
/* trigger */

.sb-01__trigger {
  display: flex;
  align-items: center;
  gap: .7rem;
  inline-size: min(30rem,100%);
  min-block-size: 52px;
  padding-inline: 1rem .5rem;
  border: 1px solid var(--line);
  border-radius: 14px;
  cursor: pointer;
  background: linear-gradient(180deg, rgba(255,255,255,.05), rgba(255,255,255,.01));
  color: var(--muted);
  font: 500 .95rem/1 inherit;
  text-align: start;
  transition: border-color .18s, color .18s, background .18s, translate .18s;
}

.sb-01__trigger:hover {
  color: var(--ink);
  border-color: color-mix(in oklab, var(--acc) 42%, var(--line));
  translate: 0 -1px;
}

.sb-01__trigger:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}

.sb-01__trigger-txt {
  flex: 1;
}

.sb-01__ico {
  inline-size: 18px;
  block-size: 18px;
  flex: none;
}

.sb-01__ico--lg {
  inline-size: 20px;
  block-size: 20px;
  color: var(--muted);
}

.sb-01__kbd {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 1px;
  min-inline-size: 1.55rem;
  block-size: 1.55rem;
  padding-inline: .4rem;
  border: 1px solid var(--line);
  border-radius: 7px;
  background: var(--panel-2);
  color: var(--muted);
  font: 500 .72rem/1 ui-monospace,"SF Mono",Menlo,monospace;
  letter-spacing: .02em;
}

.sb-01__kbd abbr {
  text-decoration: none;
}
/* palette */

.sb-01__palette {
  inline-size: min(38rem,92vw);
  max-inline-size: none;
  max-block-size: min(30rem,80vh);
  margin-block-start: 12vh;
  padding: 0;
  overflow: hidden;
  color: var(--ink);
  border: 1px solid var(--line);
  border-radius: 18px;
  background: var(--panel);
  box-shadow: 0 40px 90px -24px var(--shadow), 0 0 0 1px rgba(255,255,255,.04) inset;
  flex-direction: column;
}

.sb-01__palette[open] {
  display: flex;
}

.sb-01__palette::backdrop {
  background: rgba(6,6,12,.6);
  backdrop-filter: blur(8px) saturate(140%);
  -webkit-backdrop-filter: blur(8px) saturate(140%);
}

@supports (transition-behavior: allow-discrete) {
  .sb-01__palette {
    opacity: 0;
    translate: 0 -10px;
    scale: .97;
    transition: opacity .22s cubic-bezier(.2,.9,.25,1), translate .22s cubic-bezier(.2,.9,.25,1), scale .22s cubic-bezier(.2,.9,.25,1), overlay .22s allow-discrete, display .22s allow-discrete;
  }

  .sb-01__palette[open] {
    opacity: 1;
    translate: 0 0;
    scale: 1;
  }

  @starting-style {
    .sb-01__palette[open] {
      opacity: 0;
      translate: 0 -10px;
      scale: .97;
    }
  }

  .sb-01__palette::backdrop {
    opacity: 0;
    transition: opacity .22s, overlay .22s allow-discrete, display .22s allow-discrete;
  }

  .sb-01__palette[open]::backdrop {
    opacity: 1;
  }

  @starting-style {
    .sb-01__palette[open]::backdrop {
      opacity: 0;
    }
  }
}
/* field */

.sb-01__field {
  display: flex;
  align-items: center;
  gap: .75rem;
  padding: .95rem 1rem;
  border-block-end: 1px solid var(--line);
}

.sb-01__input {
  flex: 1;
  min-inline-size: 0;
  border: 0;
  background: none;
  color: var(--ink);
  font: 400 1rem/1.4 inherit;
  padding: .15rem 0;
}

.sb-01__input::placeholder {
  color: var(--muted);
}

.sb-01__input:focus {
  outline: none;
}

.sb-01__input::-webkit-search-cancel-button {
  -webkit-appearance: none;
  appearance: none;
}

.sb-01__kbd--esc {
  text-transform: uppercase;
  font-size: .65rem;
}
/* list */

.sb-01__scroll {
  overflow: auto;
  overscroll-behavior: contain;
  scrollbar-gutter: stable;
  padding: .5rem;
}

.sb-01__list,
.sb-01__sub {
  list-style: none;
  margin: 0;
  padding: 0;
}

.sb-01__sect-h {
  margin: .55rem .6rem .3rem;
  color: var(--muted);
  font: 600 .68rem/1 inherit;
  letter-spacing: .09em;
  text-transform: uppercase;
}

.sb-01__sect:not(:has(.sb-01__opt:not([hidden]))) {
  display: none;
}

.sb-01__opt {
  display: flex;
  align-items: center;
  gap: .75rem;
  min-block-size: 48px;
  padding: .5rem .6rem;
  border-radius: 11px;
  cursor: pointer;
  color: var(--ink);
  scroll-margin: .5rem;
  transition: background .14s, translate .14s;
}

.sb-01__opt[aria-selected="true"] {
  background: var(--wash);
  box-shadow: inset 0 0 0 1px color-mix(in oklab, var(--acc) 30%, transparent);
}

.sb-01__opt:hover {
  background: rgba(255,255,255,.045);
}

.sb-01__tile,
.sb-01__av {
  display: grid;
  place-items: center;
  inline-size: 32px;
  block-size: 32px;
  flex: none;
  border-radius: 9px;
  background: var(--panel-2);
  color: var(--muted);
  box-shadow: inset 0 0 0 1px var(--line);
}

.sb-01__tile svg {
  inline-size: 17px;
  block-size: 17px;
}

.sb-01__opt[aria-selected="true"] .sb-01__tile {
  color: var(--acc-ink);
  background: color-mix(in oklab, var(--acc) 22%, var(--panel-2));
}

.sb-01__av {
  font: 600 .72rem/1 inherit;
  letter-spacing: .02em;
  color: #fff;
  box-shadow: none;
}

.sb-01__av--a {
  background: linear-gradient(135deg,#8b7cff,#4f46e5);
}

.sb-01__av--b {
  background: linear-gradient(135deg,#2dd4bf,#0891b2);
}

.sb-01__label {
  display: flex;
  flex-direction: column;
  gap: .15rem;
  flex: 1;
  min-inline-size: 0;
  font: 500 .92rem/1.25 inherit;
}

.sb-01__label small {
  color: var(--muted);
  font: 400 .76rem/1.3 inherit;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.sb-01__go {
  inline-size: 16px;
  block-size: 16px;
  color: var(--muted);
  opacity: 0;
  translate: -4px 0;
  transition: opacity .16s, translate .16s;
}

.sb-01__opt[aria-selected="true"] .sb-01__go {
  opacity: 1;
  translate: 0 0;
  color: var(--acc-ink);
}

.sb-01__empty {
  margin: 1.6rem 0 1.9rem;
  text-align: center;
  color: var(--muted);
  font: 400 .88rem/1 inherit;
}
/* footer */

.sb-01__foot {
  display: flex;
  gap: 1.1rem;
  align-items: center;
  padding: .6rem 1rem;
  border-block-start: 1px solid var(--line);
  background: linear-gradient(180deg, transparent, rgba(255,255,255,.02));
  color: var(--muted);
  font: 500 .72rem/1 inherit;
}

.sb-01__hint {
  display: inline-flex;
  align-items: center;
  gap: .3rem;
}

.sb-01__foot .sb-01__kbd {
  min-inline-size: 1.3rem;
  block-size: 1.3rem;
  font-size: .68rem;
}
/* light fallback (this demo is dark-first) */

.sb-01[data-theme="light"] {
  --bg: #f6f6fa;
  --panel: #fff;
  --panel-2: #f2f2f7;
  --ink: #141420;
  --muted: #6b6b80;
  --line: #e4e4ee;
  --acc: #6d5cf6;
  --acc-ink: #4c3fd6;
  --wash: rgba(109,92,246,.10);
  --ring: #6d5cf6;
  --shadow: rgba(30,30,60,.24);
  background: radial-gradient(58rem 34rem at 12% -12%, rgba(109,92,246,.12), transparent 68%), var(--bg);
}

.sb-01[data-theme="light"] .sb-01__trigger {
  background: #fff;
}

.sb-01[data-theme="light"] .sb-01__palette::backdrop {
  background: rgba(20,20,32,.35);
}

@media (prefers-color-scheme: light) {
  .sb-01:not([data-theme="dark"]) {
    --bg: #f6f6fa;
    --panel: #fff;
    --panel-2: #f2f2f7;
    --ink: #141420;
    --muted: #6b6b80;
    --line: #e4e4ee;
    --acc: #6d5cf6;
    --acc-ink: #4c3fd6;
    --wash: rgba(109,92,246,.10);
    --ring: #6d5cf6;
    --shadow: rgba(30,30,60,.24);
    background: radial-gradient(58rem 34rem at 12% -12%, rgba(109,92,246,.12), transparent 68%), var(--bg);
  }

  .sb-01:not([data-theme="dark"]) .sb-01__trigger {
    background: #fff;
  }

  .sb-01:not([data-theme="dark"]) .sb-01__palette::backdrop {
    background: rgba(20,20,32,.35);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sb-01 *,
    .sb-01 *::before,
    .sb-01 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .sb-01__palette,
    .sb-01__trigger,
    .sb-01__kbd {
    border: 1px solid CanvasText;
  }

  .sb-01__opt[aria-selected="true"] {
    outline: 2px solid Highlight;
  }
}

.sb-01__theme {
  position: absolute;
  inset-block-start: clamp(.75rem,2vw,1.25rem);
  inset-inline-end: clamp(.75rem,2vw,1.25rem);
  z-index: 50;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  padding: 0;
  border-radius: 999px;
  border: 1px solid rgba(0,0,0,.12);
  color: currentColor;
  background: rgba(255,255,255,.72);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  transition: background .25s ease, transform .25s cubic-bezier(.16,1,.3,1), border-color .25s ease;
}

.sb-01[data-theme="dark"] .sb-01__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .sb-01:not([data-theme="light"]) .sb-01__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.sb-01__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.sb-01[data-theme="dark"] .sb-01__theme:hover,
.sb-01:not([data-theme="light"]) .sb-01__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.sb-01__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.sb-01__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.sb-01__sun {
  display: none;
}

.sb-01__theme[aria-pressed="true"] .sb-01__sun {
  display: block;
}

.sb-01__theme[aria-pressed="true"] .sb-01__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .sb-01__theme {
    transition: none;
  }

  .sb-01__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.sb-01');
  if (!root) return;
  const dlg = root.querySelector('#sb-01-dialog');
  const trigger = root.querySelector('#sb-01-open');
  const input = root.querySelector('#sb-01-input');
  const empty = root.querySelector('#sb-01-empty');
  const opts = [...root.querySelectorAll('.sb-01__opt')];
  const shown = () => opts.filter((o) => !o.hidden);

  const select = (el) => {
    if (!el) return;
    opts.forEach((o) => o.setAttribute('aria-selected', String(o === el)));
    input.setAttribute('aria-activedescendant', el.id);
    el.scrollIntoView({ block: 'nearest' });
  };
  const filter = () => {
    const q = input.value.trim().toLowerCase();
    opts.forEach((o) => { o.hidden = q !== '' && !o.textContent.toLowerCase().includes(q); });
    empty.hidden = shown().length > 0;
    select(shown()[0]);                                  /* activedescendant must never point at a hidden id */
  };
  const open = () => { dlg.showModal(); trigger.setAttribute('aria-expanded', 'true'); input.value = ''; filter(); input.focus(); };
  const close = () => { dlg.close(); };

  trigger.addEventListener('click', open);
  dlg.addEventListener('close', () => { trigger.setAttribute('aria-expanded', 'false'); trigger.focus(); });
  dlg.addEventListener('click', (e) => { if (e.target === dlg) close(); });   /* click the backdrop */
  input.addEventListener('input', filter);
  input.addEventListener('keydown', (e) => {
    const list = shown();
    const i = list.indexOf(list.find((o) => o.getAttribute('aria-selected') === 'true'));
    if (e.key === 'ArrowDown') { e.preventDefault(); select(list[(i + 1) % list.length]); }
    if (e.key === 'ArrowUp') { e.preventDefault(); select(list[(i - 1 + list.length) % list.length]); }
    if (e.key === 'Enter') { e.preventDefault(); list[i] && list[i].animate([{ scale: '.98' }, { scale: '1' }], 160); }
  });
  opts.forEach((o) => o.addEventListener('mousemove', () => select(o)));
  document.addEventListener('keydown', (e) => {
    if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') { e.preventDefault(); dlg.open ? close() : open(); }
  });
  requestAnimationFrame(open);                            /* the playground opens on the palette itself */
})();
(()=>{const r=document.querySelector('.sb-01');if(!r)return;const t=r.querySelector('.sb-01__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
