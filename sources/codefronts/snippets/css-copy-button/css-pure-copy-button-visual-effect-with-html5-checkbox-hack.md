---
source: "codefronts"
url: "https://codefronts.com/snippets/css-copy-button/css-pure-copy-button-visual-effect-with-html5-checkbox-hack/"
title: "CSS Pure Copy Button Visual Effect with HTML5 Checkbox Hack"
section: "snippets"
category: "css-copy-button"
category_name: "CSS Copy Buttons"
description: "The zero-JavaScript version of the copy interaction &mdash; and an honest one."
has_js: "false"
---

Here's a working CSS Copy Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Pure Copy Button Visual Effect with HTML5 Checkbox Hack
Source: https://codefronts.com/snippets/css-copy-button/css-pure-copy-button-visual-effect-with-html5-checkbox-hack/

The zero-JavaScript version of the copy interaction &mdash; and an honest one. A hidden checkbox plus :checked drives the entire Copy &rarr; Copied! state change, including the checkmark and the tinted surface. What it deliberately does not do is write to the clipboard: no CSS feature can. This demo is the feedback pattern; the write needs the one line of script shown in demo 05.
## HTML
```html
<div class="cpy-04">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&display=swap">
  <input class="cpy-04__sr" type="checkbox" id="cpy-04-dark">
  <label class="cpy-04__theme" for="cpy-04-dark" title="Switch light or dark theme">
    <svg class="cpy-04__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.3" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.7v2.2M12 19.1v2.2M2.7 12h2.2M19.1 12h2.2M5.4 5.4l1.6 1.6M17 17l1.6 1.6M18.6 5.4 17 7M7 17l-1.6 1.6" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="cpy-04__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="cpy-04__vh">Switch light or dark theme</span>
  </label>

  <div class="cpy-04__stage">
    <div class="cpy-04__card">
      <p class="cpy-04__eyebrow">Pure CSS &middot; feedback only</p>
      <h2 class="cpy-04__title">The state change, with zero script</h2>

      <div class="cpy-04__demo">
        <code class="cpy-04__value">SAVE-STATE-DEMO</code>
        <input class="cpy-04__sr" type="checkbox" id="cpy-04-copied">
        <label class="cpy-04__btn" for="cpy-04-copied">
          <span class="cpy-04__icons">
            <svg class="cpy-04__i1" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><rect x="9" y="9" width="11" height="11" rx="2.4" stroke="currentColor" stroke-width="1.8"/><path d="M15.5 5.6A2.6 2.6 0 0 0 13 4H6.6A2.6 2.6 0 0 0 4 6.6V13a2.6 2.6 0 0 0 1.6 2.4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
            <svg class="cpy-04__i2" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4.8 12.6 9.5 17.3 19.2 7.2" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </span>
          <span class="cpy-04__labels">
            <span class="cpy-04__l1">Copy</span>
            <span class="cpy-04__l2">Copied!</span>
          </span>
        </label>
        <p class="cpy-04__status" role="status">
          <span class="cpy-04__s1">Toggle the state &mdash; no JavaScript is loaded on this demo.</span>
          <span class="cpy-04__s2">State is now <code>:checked</code>. Nothing was written to your clipboard.</span>
        </p>
      </div>

      <div class="cpy-04__truth">
        <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="1.7"/><path d="M12 8.2v.2M12 11.4v4.4" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg>
        <p><strong>CSS cannot write to the clipboard.</strong> Clipboard writes need user activation and a security check, which only <code>navigator.clipboard.writeText()</code> can perform. What you see here is the full feedback choreography built with <code>:checked</code> &mdash; pair it with the one line of script in demo 05 to make it real.</p>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.cpy-04 {
  --bg: #f7f6f4;
  --panel: #ffffff;
  --panel2: #f1efec;
  --ink: #141310;
  --muted: #5f5b53;
  --line: rgba(20,19,16,.12);
  --accent: #b45309;
  --ok: #15803d;
  --ok-bg: rgba(21,128,61,.1);
  --dur: 200ms;
  --sans: system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "JetBrains Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.cpy-04 *,
.cpy-04 *::before,
.cpy-04 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(.5 .1 250)) {
  .cpy-04 {
    --accent: oklch(.56 .14 62);
    --ok: oklch(.55 .15 149);
    --ok-bg: oklch(.55 .15 149/.12);
  }
}

.cpy-04__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  clip-path: inset(50%);
  pointer-events: none;
}

.cpy-04__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cpy-04__theme {
  position: absolute;
  inset-block-start: clamp(1rem,3vw,1.75rem);
  inset-inline-end: clamp(1rem,3vw,1.75rem);
  z-index: 3;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  border-radius: 999px;
  border: 1px solid var(--line);
  background: rgba(255,255,255,.6);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  color: var(--ink);
  cursor: pointer;
}

.cpy-04__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.cpy-04__moon {
  display: none;
}

.cpy-04__sr:focus-visible + .cpy-04__theme {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.cpy-04__stage {
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,6vw,4.5rem);
}

.cpy-04__card {
  inline-size: min(100%,35rem);
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 1.5rem;
  padding: clamp(1.4rem,4vw,2.25rem);
  display: grid;
  gap: 1rem;
  box-shadow: 0 1px 2px rgba(20,19,16,.05),0 26px 50px -34px rgba(20,19,16,.32);
}
/* Grid/flex children default to min-width:auto, so the long copied
   value forced the card past the stage and took the document sideways
   at 320px. */

.cpy-04__card {
  min-inline-size: 0;
}

.cpy-04__card > * {
  min-inline-size: 0;
}

.cpy-04__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--accent);
}

.cpy-04__title {
  margin: 0;
  font-size: clamp(1.4rem,3.4vw,1.85rem);
  line-height: 1.15;
  letter-spacing: -.02em;
  font-weight: 640;
}

.cpy-04__demo {
  display: grid;
  justify-items: start;
  gap: .9rem;
  padding: clamp(1.1rem,3vw,1.6rem);
  border: 1px solid var(--line);
  border-radius: 1.2rem;
  background: var(--panel2);
  transition: background var(--dur),border-color var(--dur);
}

.cpy-04:has(#cpy-04-copied:checked) .cpy-04__demo {
  background: var(--ok-bg);
  border-color: color-mix(in srgb,var(--ok) 30%,transparent);
}

.cpy-04__value {
  font-family: var(--mono);
  font-size: clamp(.95rem,2.4vw,1.15rem);
  letter-spacing: .02em;
}

.cpy-04__btn {
  min-block-size: 2.85rem;
  min-inline-size: 44px;
  display: inline-flex;
  align-items: center;
  gap: .55rem;
  padding-inline: 1.1rem;
  border: 1px solid var(--line);
  border-radius: .85rem;
  background: var(--panel);
  color: var(--ink);
  font-size: .92rem;
  font-weight: 560;
  cursor: pointer;
  user-select: none;
  transition: background var(--dur),color var(--dur),border-color var(--dur),scale var(--dur);
}

.cpy-04__btn:hover {
  background: var(--panel2);
}

.cpy-04__btn:active {
  scale: .975;
}

#cpy-04-copied:focus-visible + .cpy-04__btn {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

#cpy-04-copied:checked + .cpy-04__btn {
  color: var(--ok);
  background: var(--panel);
  border-color: color-mix(in srgb,var(--ok) 40%,transparent);
}

.cpy-04__icons {
  position: relative;
  inline-size: 1.15rem;
  block-size: 1.15rem;
  flex: none;
}

.cpy-04__icons svg {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  transition: opacity var(--dur),scale var(--dur),rotate var(--dur);
}

.cpy-04__i2 {
  opacity: 0;
  scale: .5;
  rotate: -20deg;
}

#cpy-04-copied:checked + .cpy-04__btn .cpy-04__i1 {
  opacity: 0;
  scale: .5;
  rotate: 16deg;
}

#cpy-04-copied:checked + .cpy-04__btn .cpy-04__i2 {
  opacity: 1;
  scale: 1;
  rotate: 0deg;
}

.cpy-04__labels {
  display: grid;
}

.cpy-04__labels span {
  grid-area: 1/1;
  transition: opacity var(--dur),translate var(--dur);
}

.cpy-04__l2 {
  opacity: 0;
  translate: 0 .4rem;
}

#cpy-04-copied:checked + .cpy-04__btn .cpy-04__l1 {
  opacity: 0;
  translate: 0 -.4rem;
}

#cpy-04-copied:checked + .cpy-04__btn .cpy-04__l2 {
  opacity: 1;
  translate: 0 0;
}

.cpy-04__status {
  display: grid;
  margin: 0;
  font-size: .86rem;
  line-height: 1.5;
  color: var(--muted);
}

.cpy-04__status span {
  grid-area: 1/1;
  transition: opacity var(--dur);
}

.cpy-04__s2 {
  opacity: 0;
}

.cpy-04__status code {
  font-family: var(--mono);
  font-size: .78rem;
}

.cpy-04:has(#cpy-04-copied:checked) .cpy-04__s1 {
  opacity: 0;
}

.cpy-04:has(#cpy-04-copied:checked) .cpy-04__s2 {
  opacity: 1;
}

.cpy-04__truth {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: .75rem;
  padding: 1rem 1.1rem;
  border: 1px dashed color-mix(in srgb,var(--accent) 45%,transparent);
  border-radius: 1rem;
  background: color-mix(in srgb,var(--accent) 6%,transparent);
}
/* The paragraph inside this block carries an inline <code> token that
   cannot break, so at 320px it pushed 13px past the card. Let the token
   break instead of the layout. */

.cpy-04__truth p,
.cpy-04__truth code {
  overflow-wrap: anywhere;
  min-inline-size: 0;
}

.cpy-04__truth svg {
  inline-size: 1.2rem;
  block-size: 1.2rem;
  color: var(--accent);
}

.cpy-04__truth p {
  margin: 0;
  font-size: .88rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.cpy-04__truth strong {
  color: var(--ink);
}

.cpy-04__truth code {
  font-family: var(--mono);
  font-size: .78rem;
}

@media not (prefers-color-scheme: dark) {
  .cpy-04:has(#cpy-04-dark:checked) {
    --bg: #0b0a08;
    --panel: #121110;
    --panel2: #1b1917;
    --ink: #f2efe9;
    --muted: rgba(242,239,233,.62);
    --line: rgba(242,239,233,.14);
    --accent: #fbbf24;
    --ok: #6ee7a8;
    --ok-bg: rgba(110,231,168,.13);
  }

  .cpy-04:has(#cpy-04-dark:checked) .cpy-04__theme {
    background: rgba(255,255,255,.07);
  }

  .cpy-04:has(#cpy-04-dark:checked) .cpy-04__sun {
    display: none;
  }

  .cpy-04:has(#cpy-04-dark:checked) .cpy-04__moon {
    display: block;
  }
}

@media (prefers-color-scheme: dark) {
  .cpy-04:not([data-theme="light"]):not(:has(#cpy-04-dark:checked)) {
    --bg: #0b0a08;
    --panel: #121110;
    --panel2: #1b1917;
    --ink: #f2efe9;
    --muted: rgba(242,239,233,.62);
    --line: rgba(242,239,233,.14);
    --accent: #fbbf24;
    --ok: #6ee7a8;
    --ok-bg: rgba(110,231,168,.13);
  }

  .cpy-04__theme {
    background: rgba(255,255,255,.07);
  }

  .cpy-04__sun {
    display: none;
  }

  .cpy-04__moon {
    display: block;
  }

  .cpy-04:has(#cpy-04-dark:checked) .cpy-04__sun {
    display: block;
  }

  .cpy-04:has(#cpy-04-dark:checked) .cpy-04__moon {
    display: none;
  }
}

.cpy-04[data-theme="dark"] {
  --bg: #0b0a08;
  --panel: #121110;
  --panel2: #1b1917;
  --ink: #f2efe9;
  --muted: rgba(242,239,233,.62);
  --line: rgba(242,239,233,.14);
  --accent: #fbbf24;
  --ok: #6ee7a8;
  --ok-bg: rgba(110,231,168,.13);
}

@media (prefers-reduced-motion: reduce) {
  .cpy-04 *,
    .cpy-04 *::before,
    .cpy-04 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .cpy-04__card,
    .cpy-04__demo,
    .cpy-04__btn,
    .cpy-04__theme,
    .cpy-04__truth {
    border-color: CanvasText;
    background: Canvas;
    color: CanvasText;
    box-shadow: none;
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
  }
}
```
