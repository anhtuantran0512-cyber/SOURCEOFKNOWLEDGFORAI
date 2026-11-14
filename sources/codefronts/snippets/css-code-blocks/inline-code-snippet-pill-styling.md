---
source: "codefronts"
url: "https://codefronts.com/snippets/css-code-blocks/inline-code-snippet-pill-styling/"
title: "Inline Code Pill Styling for Documentation"
section: "snippets"
category: "css-code-blocks"
category_name: "CSS Code Blocks"
description: "The most-used code style on any docs site and the one most often done badly."
has_js: "true"
---

Here's a working CSS Code Block from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Inline Code Pill Styling for Documentation
Source: https://codefronts.com/snippets/css-code-blocks/inline-code-snippet-pill-styling/

The most-used code style on any docs site and the one most often done badly. These pills get the four details right: padding that does not break the line box, a font size relative to the surrounding text, a background that works inside links and headings, and box-decoration-break so a pill wrapping across two lines still looks like one thing.
## HTML
```html
<div class="cbk-16">
  <button class="cbk-16__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="cbk-16__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="cbk-16__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <div class="cbk-16__stage">
    <input class="cbk-16__tbox" id="cbk-16-tbox" type="checkbox" data-alt="dark" aria-label="Toggle light and dark theme">
    <label class="cbk-16__tbtn" for="cbk-16-tbox" title="Toggle light and dark theme">
      <svg class="cbk-16__tsun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4.2"></circle><path d="M12 2.4v2.3M12 19.3v2.3M2.4 12h2.3M19.3 12h2.3M5.2 5.2l1.6 1.6M17.2 17.2l1.6 1.6M18.8 5.2l-1.6 1.6M6.8 17.2l-1.6 1.6"></path></svg>
      <svg class="cbk-16__tmoon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.2 14.6A8.6 8.6 0 0 1 9.4 3.8a8.6 8.6 0 1 0 10.8 10.8Z"></path></svg>
    </label>
    <article class="cbk-16__doc">
      <h2 class="cbk-16__h">Installing the <code>useToast</code> hook</h2>

      <p class="cbk-16__p">Install the package with <code>npm install @codefronts/toast</code>, then import <code>useToast</code> from <code>@codefronts/toast/react</code>. The hook returns a <code>notify()</code> function and reads its defaults from the nearest <code>&lt;ToastProvider&gt;</code>.</p>

      <p class="cbk-16__p">Set the surface colour with the <code>--toast-surface</code> custom property, or pass <code>tone="critical"</code> for destructive messages. Full options live in the <a class="cbk-16__a" href="#api">API reference for <code>notify(options)</code></a>.</p>

      <p class="cbk-16__p">Press <kbd class="cbk-16__k">Ctrl</kbd> + <kbd class="cbk-16__k">K</kbd> in the playground to open the command palette, then run <code>toast: preview</code> to see every variant at once.</p>
    </article>
  </div>
</div>
```
## CSS
```css
.cbk-16 {
  inline-size: 100%;
  width: 100%;
  min-block-size: 100vh;
  min-block-size: 100svh;
  min-height: 100vh;
  display: block;
  --mono: ui-monospace,"JetBrains Mono","Geist Mono","SF Mono","IBM Plex Mono",Menlo,monospace;
  --sans: system-ui,"Inter","Geist",-apple-system,"Segoe UI",sans-serif;
  --bg: #fbfaf8;
  --surface: #ffffff;
  --ink: #191a1f;
  --muted: #5c6270;
  --line: #e6e5e0;
  --pill-ink: #8a3ffc;
  --pill-bg: rgba(138,63,252,.09);
  --pill-line: rgba(138,63,252,.2);
  --link: #0f62fe;
  --kbd: #f4f4f2;
  background: radial-gradient(52rem 30rem at 50% -12%, #f2eefc 0%, transparent 62%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
}

@supports (color: oklch(50% .1 200)) {
  .cbk-16 {
    --bg: oklch(98.5% .004 85);
    --surface: oklch(100% 0 0);
    --ink: oklch(23% .012 275);
    --muted: oklch(52% .015 275);
    --line: oklch(91% .006 85);
    --pill-ink: oklch(52% .22 300);
    --pill-bg: oklch(52% .22 300 / .1);
    --pill-line: oklch(52% .22 300 / .22);
    --link: oklch(50% .19 258);
    --kbd: oklch(96.5% .004 85);
  }
}

.cbk-16 *,
.cbk-16 *::before,
.cbk-16 *::after {
  box-sizing: border-box;
}

.cbk-16__stage {
  display: grid;
  place-items: center;
  min-block-size: inherit;
  padding: clamp(1.25rem,5vw,4rem);
}

.cbk-16__doc {
  inline-size: min(44rem,100%);
  padding: clamp(1.5rem,4vw,2.75rem);
  border: 1px solid var(--line);
  border-radius: 18px;
  background: var(--surface);
  container-type: inline-size;
  box-shadow: 0 1px 0 rgba(255,255,255,.9) inset, 0 20px 48px -34px rgba(30,26,60,.35);
}

.cbk-16__h {
  margin: 0 0 1.1rem;
  font-size: clamp(1.25rem,.9rem + 1.2cqi,1.75rem);
  line-height: 1.25;
  font-weight: 650;
  letter-spacing: -.015em;
  text-wrap: balance;
}

.cbk-16__p {
  margin: 0 0 1.1rem;
  max-inline-size: 60ch;
  font-size: clamp(.9375rem,.85rem + .3cqi,1.0625rem);
  line-height: 1.78;
  color: var(--muted);
  text-wrap: pretty;
}

.cbk-16__p:last-child {
  margin-block-end: 0;
}

.cbk-16 code {
  font-family: var(--mono);
  font-size: .9em;
  padding: .12em .38em;
  border-radius: .4em;
  border: 1px solid var(--pill-line);
  background: var(--pill-bg);
  color: var(--pill-ink);
  overflow-wrap: break-word;
  -webkit-box-decoration-break: clone;
  box-decoration-break: clone;
  font-variant-ligatures: none;
}

.cbk-16__h code {
  font-size: .86em;
  font-weight: 600;
}

.cbk-16__a {
  color: var(--link);
  text-decoration: underline;
  text-decoration-thickness: 1.5px;
  text-underline-offset: .18em;
  border-radius: .2em;
}

.cbk-16__a:hover {
  text-decoration-thickness: 2.5px;
}

.cbk-16__a code {
  color: var(--link);
  background: color-mix(in oklab,var(--link) 11%,transparent);
  border-color: color-mix(in oklab,var(--link) 26%,transparent);
}

.cbk-16__k {
  font-family: var(--mono);
  font-size: .82em;
  padding: .16em .45em .2em;
  border-radius: .4em;
  border: 1px solid var(--line);
  border-block-end-width: 2px;
  background: var(--kbd);
  color: var(--ink);
  white-space: nowrap;
  box-shadow: 0 1px 0 rgba(255,255,255,.7) inset;
}

.cbk-16 :focus-visible {
  outline: 2px solid var(--link);
  outline-offset: 2px;
}

.cbk-16[data-theme="dark"] {
  --bg: #0b0c10;
  --surface: #12141b;
  --ink: #eceef4;
  --muted: #a8b0c0;
  --line: #242833;
  --pill-ink: #d0b3ff;
  --pill-bg: rgba(208,179,255,.13);
  --pill-line: rgba(208,179,255,.24);
  --link: #7cc4ff;
  --kbd: #1b1f29;
  background: radial-gradient(52rem 30rem at 50% -12%, #191b2c 0%, transparent 62%), var(--bg);
}

.cbk-16[data-theme="dark"] .cbk-16__doc {
  box-shadow: 0 1px 0 rgba(255,255,255,.05) inset, 0 24px 56px -34px rgba(0,0,0,.9);
}

@media (prefers-color-scheme: dark) {
  .cbk-16:not([data-theme="light"]) {
    --bg: #0b0c10;
    --surface: #12141b;
    --ink: #eceef4;
    --muted: #a8b0c0;
    --line: #242833;
    --pill-ink: #d0b3ff;
    --pill-bg: rgba(208,179,255,.13);
    --pill-line: rgba(208,179,255,.24);
    --link: #7cc4ff;
    --kbd: #1b1f29;
    background: radial-gradient(52rem 30rem at 50% -12%, #191b2c 0%, transparent 62%), var(--bg);
  }

  .cbk-16:not([data-theme="light"]) .cbk-16__doc {
    box-shadow: 0 1px 0 rgba(255,255,255,.05) inset, 0 24px 56px -34px rgba(0,0,0,.9);
  }
}

@media (forced-colors: active) {
  .cbk-16__doc {
    border: 2px solid CanvasText;
    background: Canvas;
  }

  .cbk-16 code,
    .cbk-16__k {
    border: 1px solid CanvasText;
    background: Canvas;
    color: CanvasText;
  }

  .cbk-16__a,
    .cbk-16__a code {
    color: LinkText;
  }
}
/* theme toggle — pure CSS, :has() driven; :checked = dark theme, top-right of the stage */

.cbk-16__stage {
  position: relative;
}

.cbk-16__tbox {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  padding: 0;
  opacity: 0;
  pointer-events: none;
}

.cbk-16__tbtn {
  position: absolute;
  inset-block-start: clamp(.7rem,2vw,1.35rem);
  inset-inline-end: clamp(.7rem,2vw,1.35rem);
  z-index: 7;
  display: grid;
  place-items: center;
  inline-size: 2.375rem;
  block-size: 2.375rem;
  border: 1px solid rgba(127,127,127,.34);
  border-radius: 11px;
  background: rgba(127,127,127,.14);
  color: var(--ink,#e7eaf3);
  cursor: pointer;
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
  transition: background .18s ease, border-color .18s ease, transform .18s ease;
}

@supports (color: color-mix(in srgb,red,blue)) {
  .cbk-16__tbtn {
    background: color-mix(in srgb, var(--ink,#e7eaf3) 10%, transparent);
    border-color: color-mix(in srgb, var(--ink,#e7eaf3) 26%, transparent);
  }
}

.cbk-16__tbtn:hover {
  transform: translateY(-1px);
}

.cbk-16__tbtn svg {
  inline-size: 1.0625rem;
  block-size: 1.0625rem;
}

.cbk-16__tbox:focus-visible + .cbk-16__tbtn {
  outline: 2px solid var(--ink,#e7eaf3);
  outline-offset: 2px;
}

.cbk-16__tsun {
  display: none;
}

.cbk-16:has(.cbk-16__tbox:checked) .cbk-16__tmoon {
  display: none;
}

.cbk-16:has(.cbk-16__tbox:checked) .cbk-16__tsun {
  display: block;
}

@media (prefers-reduced-motion: reduce) {
  .cbk-16__tbtn {
    transition: none;
  }

  .cbk-16__tbtn:hover {
    transform: none;
  }
}

@media (forced-colors: active) {
  .cbk-16__tbtn {
    border: 1px solid ButtonBorder;
    color: ButtonText;
    background: ButtonFace;
  }
}

.cbk-16:has(.cbk-16__tbox:checked) {
  --bg: #0b0c10;
  --surface: #12141b;
  --ink: #eceef4;
  --muted: #a8b0c0;
  --line: #242833;
  --pill-ink: #d0b3ff;
  --pill-bg: rgba(208,179,255,.13);
  --pill-line: rgba(208,179,255,.24);
  --link: #7cc4ff;
  --kbd: #1b1f29;
  background: radial-gradient(52rem 30rem at 50% -12%, #191b2c 0%, transparent 62%), var(--bg);
}

.cbk-16:has(.cbk-16__tbox:checked) .cbk-16__doc {
  box-shadow: 0 1px 0 rgba(255,255,255,.05) inset, 0 24px 56px -34px rgba(0,0,0,.9);
}

.cbk-16__theme {
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

.cbk-16[data-theme="dark"] .cbk-16__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .cbk-16:not([data-theme="light"]) .cbk-16__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.cbk-16__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.cbk-16[data-theme="dark"] .cbk-16__theme:hover,
.cbk-16:not([data-theme="light"]) .cbk-16__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.cbk-16__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.cbk-16__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.cbk-16__sun {
  display: none;
}

.cbk-16__theme[aria-pressed="true"] .cbk-16__sun {
  display: block;
}

.cbk-16__theme[aria-pressed="true"] .cbk-16__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .cbk-16__theme {
    transition: none;
  }

  .cbk-16__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(()=>{const r=document.querySelector('.cbk-16');if(!r)return;const t=r.querySelector('.cbk-16__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
