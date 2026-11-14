---
source: "codefronts"
url: "https://codefronts.com/snippets/css-code-blocks/mac-style-window-container/"
title: "Mac-Style Terminal Window CSS Code Block"
section: "snippets"
category: "css-code-blocks"
category_name: "CSS Code Blocks"
description: "A documentation-scale macOS terminal window: real titlebar geometry, traffic lights that light up on hover, a centred window title, an inner top highlight…"
has_js: "true"
---

Here's a working CSS Code Block from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Mac-Style Terminal Window CSS Code Block
Source: https://codefronts.com/snippets/css-code-blocks/mac-style-window-container/

A documentation-scale macOS terminal window: real titlebar geometry, traffic lights that light up on hover, a centred window title, an inner top highlight for the glass bevel, and a session of actual command output — pnpm build, a route table, a green success line and a live caret. Smaller and quieter than the hero mockup in demo 04, sized to sit inside a docs page.
## HTML
```html
<div class="cbk-10">
  <button class="cbk-10__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="cbk-10__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="cbk-10__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <div class="cbk-10__stage">
    <input class="cbk-10__tbox" id="cbk-10-tbox" type="checkbox" data-alt="light" aria-label="Toggle light and dark theme">
    <label class="cbk-10__tbtn" for="cbk-10-tbox" title="Toggle light and dark theme">
      <svg class="cbk-10__tsun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4.2"></circle><path d="M12 2.4v2.3M12 19.3v2.3M2.4 12h2.3M19.3 12h2.3M5.2 5.2l1.6 1.6M17.2 17.2l1.6 1.6M18.8 5.2l-1.6 1.6M6.8 17.2l-1.6 1.6"></path></svg>
      <svg class="cbk-10__tmoon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.2 14.6A8.6 8.6 0 0 1 9.4 3.8a8.6 8.6 0 1 0 10.8 10.8Z"></path></svg>
    </label>
    <figure class="cbk-10__win">
      <figcaption class="cbk-10__bar">
        <span class="cbk-10__lights" aria-hidden="true"><i class="cbk-10__x"></i><i class="cbk-10__m"></i><i class="cbk-10__f"></i></span>
        <span class="cbk-10__title">alex@studio &mdash; ~/apps/board</span>
      </figcaption>

<pre class="cbk-10__pre"><code class="language-shell"><span class="cbk-10__p" aria-hidden="true">➜</span> <span class="cbk-10__cmd">pnpm build</span>
<span class="cbk-10__dim">vite v6.0.7 building for production...</span>
<span class="cbk-10__dim">✓ 148 modules transformed</span>

<span class="cbk-10__dim">dist/index.html                 </span><span class="cbk-10__n">0.62 kB</span>
<span class="cbk-10__dim">dist/assets/app-Bn3Kq.css      </span><span class="cbk-10__n">11.48 kB</span>
<span class="cbk-10__dim">dist/assets/app-Dk9Zt.js       </span><span class="cbk-10__n">78.31 kB</span>

<span class="cbk-10__ok">✓ built in 1.41s</span>
<span class="cbk-10__p" aria-hidden="true">➜</span> <span class="cbk-10__caret" aria-hidden="true"></span></code></pre>
    </figure>
  </div>
</div>
```
## CSS
```css
.cbk-10 {
  inline-size: 100%;
  width: 100%;
  min-block-size: 100vh;
  min-block-size: 100svh;
  min-height: 100vh;
  display: block;
  --mono: ui-monospace,"JetBrains Mono","Geist Mono","SF Mono","IBM Plex Mono",Menlo,monospace;
  --sans: system-ui,"Inter","Geist",-apple-system,"Segoe UI",sans-serif;
  --bg: #0a0b0f;
  --surface: #131620;
  --bar: #1c202c;
  --line: #262b39;
  --ink: #e6e9f0;
  --muted: #8d94a3;
  --ok: #4ade80;
  --n: #ffcb6b;
  --acc: #60a5fa;
  background: radial-gradient(56rem 30rem at 50% -6%, #171b28 0%, transparent 64%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
}

@supports (color: oklch(50% .1 200)) {
  .cbk-10 {
    --bg: oklch(13% .011 265);
    --surface: oklch(19% .015 265);
    --bar: oklch(24% .017 265);
    --line: oklch(29% .018 265);
    --ink: oklch(93% .008 265);
    --muted: oklch(68% .02 265);
    --ok: oklch(84% .17 150);
    --n: oklch(85% .13 85);
  }
}

.cbk-10 *,
.cbk-10 *::before,
.cbk-10 *::after {
  box-sizing: border-box;
}

.cbk-10__stage {
  display: grid;
  place-items: center;
  min-block-size: inherit;
  padding: clamp(1rem,4vw,3.5rem);
}

.cbk-10__win {
  margin: 0;
  inline-size: min(46rem,100%);
  border: 1px solid var(--line);
  border-radius: 12px;
  background: var(--surface);
  overflow: hidden;
  container-type: inline-size;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.08), 0 26px 62px -30px rgba(0,0,0,.92);
}

.cbk-10__bar {
  position: relative;
  display: flex;
  align-items: center;
  block-size: 38px;
  padding-inline: 13px;
  background: linear-gradient(180deg,var(--bar),color-mix(in oklab,var(--bar) 82%,#000));
  box-shadow: inset 0 -1px 0 rgba(0,0,0,.5);
}

.cbk-10__lights {
  display: flex;
  gap: 8px;
}

.cbk-10__lights i {
  position: relative;
  inline-size: 11px;
  block-size: 11px;
  border-radius: 50%;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.3), 0 0 0 .5px rgba(0,0,0,.4);
}

.cbk-10__x {
  background: #ff5f57;
}

.cbk-10__m {
  background: #febc2e;
}

.cbk-10__f {
  background: #28c840;
}

.cbk-10__lights i::before {
  content: "";
  position: absolute;
  inset: 0;
  opacity: 0;
  transition: opacity .15s;
  background: linear-gradient(currentColor,currentColor) center/5px 1px no-repeat;
  color: #4a1a17;
}

.cbk-10__x::before {
  background: linear-gradient(45deg,transparent 45%,#4a1a17 45%,#4a1a17 55%,transparent 55%),linear-gradient(-45deg,transparent 45%,#4a1a17 45%,#4a1a17 55%,transparent 55%);
  background-size: 7px 7px;
  background-position: center;
  background-repeat: no-repeat;
}

.cbk-10__f::before {
  background: linear-gradient(#0d3f16,#0d3f16) center/6px 1px no-repeat,linear-gradient(#0d3f16,#0d3f16) center/1px 6px no-repeat;
}

.cbk-10__lights:hover i::before {
  opacity: .6;
}

.cbk-10__title {
  position: absolute;
  inset-inline: 0;
  text-align: center;
  color: var(--muted);
  font-size: .78125rem;
  font-weight: 500;
  pointer-events: none;
}

.cbk-10__pre {
  margin: 0;
  padding: 1.15rem 1.3rem 1.35rem;
  overflow-x: auto;
  scrollbar-width: thin;
  font-family: var(--mono);
  font-size: clamp(.78125rem,.45rem + .5cqi,.90625rem);
  line-height: 1.75;
  white-space: pre;
  font-variant-ligatures: none;
  color: var(--ink);
}

.cbk-10__p {
  color: var(--ok);
  user-select: none;
}

.cbk-10__cmd {
  color: var(--ink);
}

.cbk-10__dim {
  color: var(--muted);
}

.cbk-10__ok {
  color: var(--ok);
}

.cbk-10__n {
  color: var(--n);
}

.cbk-10__caret {
  display: inline-block;
  inline-size: 8px;
  block-size: 1.05em;
  vertical-align: text-bottom;
  background: var(--ink);
  opacity: .8;
  animation: cbk-10-blink 1.15s steps(1,end) infinite;
}

@keyframes cbk-10-blink {
  0%,
    50% {
    opacity: .8;
  }

  51%,
    100% {
    opacity: 0;
  }
}

.cbk-10[data-theme="light"] {
  --bg: #f2f3f7;
  --surface: #ffffff;
  --bar: #e9ebf1;
  --line: #dfe2ea;
  --ink: #12141a;
  --muted: #5c6373;
  --ok: #0f8a4d;
  --n: #8a5a00;
  background: radial-gradient(56rem 30rem at 50% -6%, #e9ecf7 0%, transparent 64%), var(--bg);
}

.cbk-10[data-theme="light"] .cbk-10__win {
  box-shadow: inset 0 1px 0 #fff, 0 20px 48px -30px rgba(18,22,44,.42);
}

@media (prefers-color-scheme: light) {
  .cbk-10:not([data-theme="dark"]) {
    --bg: #f2f3f7;
    --surface: #ffffff;
    --bar: #e9ebf1;
    --line: #dfe2ea;
    --ink: #12141a;
    --muted: #5c6373;
    --ok: #0f8a4d;
    --n: #8a5a00;
    background: radial-gradient(56rem 30rem at 50% -6%, #e9ecf7 0%, transparent 64%), var(--bg);
  }

  .cbk-10:not([data-theme="dark"]) .cbk-10__win {
    box-shadow: inset 0 1px 0 #fff, 0 20px 48px -30px rgba(18,22,44,.42);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cbk-10 *,
    .cbk-10 *::before,
    .cbk-10 *::after {
    animation: none !important;
    transition: none !important;
  }

  .cbk-10__caret {
    opacity: .8;
  }
}

@media (forced-colors: active) {
  .cbk-10__win {
    border: 2px solid CanvasText;
    background: Canvas;
  }

  .cbk-10__lights i {
    border: 1px solid CanvasText;
  }
}
/* theme toggle — pure CSS, :has() driven; :checked = light theme, top-right of the stage */

.cbk-10__stage {
  position: relative;
}

.cbk-10__tbox {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  padding: 0;
  opacity: 0;
  pointer-events: none;
}

.cbk-10__tbtn {
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
  .cbk-10__tbtn {
    background: color-mix(in srgb, var(--ink,#e7eaf3) 10%, transparent);
    border-color: color-mix(in srgb, var(--ink,#e7eaf3) 26%, transparent);
  }
}

.cbk-10__tbtn:hover {
  transform: translateY(-1px);
}

.cbk-10__tbtn svg {
  inline-size: 1.0625rem;
  block-size: 1.0625rem;
}

.cbk-10__tbox:focus-visible + .cbk-10__tbtn {
  outline: 2px solid var(--ink,#e7eaf3);
  outline-offset: 2px;
}

.cbk-10__tmoon {
  display: none;
}

.cbk-10:has(.cbk-10__tbox:checked) .cbk-10__tsun {
  display: none;
}

.cbk-10:has(.cbk-10__tbox:checked) .cbk-10__tmoon {
  display: block;
}

@media (prefers-reduced-motion: reduce) {
  .cbk-10__tbtn {
    transition: none;
  }

  .cbk-10__tbtn:hover {
    transform: none;
  }
}

@media (forced-colors: active) {
  .cbk-10__tbtn {
    border: 1px solid ButtonBorder;
    color: ButtonText;
    background: ButtonFace;
  }
}

.cbk-10:has(.cbk-10__tbox:checked) {
  --bg: #f2f3f7;
  --surface: #ffffff;
  --bar: #e9ebf1;
  --line: #dfe2ea;
  --ink: #12141a;
  --muted: #5c6373;
  --ok: #0f8a4d;
  --n: #8a5a00;
  background: radial-gradient(56rem 30rem at 50% -6%, #e9ecf7 0%, transparent 64%), var(--bg);
}

.cbk-10:has(.cbk-10__tbox:checked) .cbk-10__win {
  box-shadow: inset 0 1px 0 #fff, 0 20px 48px -30px rgba(18,22,44,.42);
}

.cbk-10__theme {
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

.cbk-10[data-theme="dark"] .cbk-10__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .cbk-10:not([data-theme="light"]) .cbk-10__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.cbk-10__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.cbk-10[data-theme="dark"] .cbk-10__theme:hover,
.cbk-10:not([data-theme="light"]) .cbk-10__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.cbk-10__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.cbk-10__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.cbk-10__sun {
  display: none;
}

.cbk-10__theme[aria-pressed="true"] .cbk-10__sun {
  display: block;
}

.cbk-10__theme[aria-pressed="true"] .cbk-10__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .cbk-10__theme {
    transition: none;
  }

  .cbk-10__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(()=>{const r=document.querySelector('.cbk-10');if(!r)return;const t=r.querySelector('.cbk-10__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
