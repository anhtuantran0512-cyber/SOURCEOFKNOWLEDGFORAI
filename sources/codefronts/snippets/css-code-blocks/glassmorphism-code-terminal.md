---
source: "codefronts"
url: "https://codefronts.com/snippets/css-code-blocks/glassmorphism-code-terminal/"
title: "Glassmorphism CSS Code Terminal (Backdrop Blur)"
section: "snippets"
category: "css-code-blocks"
category_name: "CSS Code Blocks"
description: "A frosted-glass terminal floating over an ambient photographic backdrop: backdrop-filter: blur(22px) saturate(180%), a hairline inner highlight along the top…"
has_js: "true"
---

Here's a working CSS Code Block from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism CSS Code Terminal (Backdrop Blur)
Source: https://codefronts.com/snippets/css-code-blocks/glassmorphism-code-terminal/

A frosted-glass terminal floating over an ambient photographic backdrop: backdrop-filter: blur(22px) saturate(180%), a hairline inner highlight along the top edge that simulates a lit glass rim, a soft outer shadow for lift, and a token palette bumped in lightness so it survives a translucent surface. Everything degrades to a solid card where backdrop-filter is unavailable.
## HTML
```html
<div class="cbk-15">
  <button class="cbk-15__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="cbk-15__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="cbk-15__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <div class="cbk-15__stage">
    <input class="cbk-15__tbox" id="cbk-15-tbox" type="checkbox" data-alt="light" aria-label="Toggle light and dark theme">
    <label class="cbk-15__tbtn" for="cbk-15-tbox" title="Toggle light and dark theme">
      <svg class="cbk-15__tsun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4.2"></circle><path d="M12 2.4v2.3M12 19.3v2.3M2.4 12h2.3M19.3 12h2.3M5.2 5.2l1.6 1.6M17.2 17.2l1.6 1.6M18.8 5.2l-1.6 1.6M6.8 17.2l-1.6 1.6"></path></svg>
      <svg class="cbk-15__tmoon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.2 14.6A8.6 8.6 0 0 1 9.4 3.8a8.6 8.6 0 1 0 10.8 10.8Z"></path></svg>
    </label>
    <div class="cbk-15__amb" aria-hidden="true">
      <img class="cbk-15__photo" src="https://picsum.photos/seed/codefronts-aurora/1600/900" width="1600" height="900" alt="" loading="lazy" decoding="async">
    </div>

    <figure class="cbk-15__glass">
      <figcaption class="cbk-15__bar">
        <span class="cbk-15__ico" aria-hidden="true">
          <svg viewBox="0 0 24 24" fill="none" focusable="false"><rect x="3" y="4.5" width="18" height="15" rx="2.5" stroke="currentColor" stroke-width="1.6"/><path d="m7.5 10 2.4 2.4-2.4 2.4M12.6 14.8h4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </span>
        <span class="cbk-15__title">deploy.sh</span>
        <span class="cbk-15__chip">edge</span>
      </figcaption>

<pre class="cbk-15__pre"><code class="language-shell"><span class="tok-comment"># Promote the current build to production edge nodes.</span>
<span class="tok-keyword">set</span> <span class="tok-op">-</span><span class="tok-variable">euo</span> <span class="tok-variable">pipefail</span>

<span class="tok-variable">REGIONS</span><span class="tok-op">=</span><span class="tok-punct">(</span><span class="tok-string">"iad1"</span> <span class="tok-string">"lhr1"</span> <span class="tok-string">"syd1"</span><span class="tok-punct">)</span>

<span class="tok-keyword">for</span> <span class="tok-variable">region</span> <span class="tok-keyword">in</span> <span class="tok-string">"${REGIONS[@]}"</span><span class="tok-punct">;</span> <span class="tok-keyword">do</span>
  <span class="tok-function">echo</span> <span class="tok-string">"→ promoting ${region}"</span>
  <span class="tok-function">npx</span> vercel promote <span class="tok-op">--</span>region <span class="tok-string">"${region}"</span> <span class="tok-op">--</span>yes
<span class="tok-keyword">done</span>

<span class="tok-function">echo</span> <span class="tok-string">"✓ live in ${#REGIONS[@]} regions"</span></code></pre>
    </figure>
  </div>
</div>
```
## CSS
```css
.cbk-15 {
  inline-size: 100%;
  width: 100%;
  min-block-size: 100vh;
  min-block-size: 100svh;
  min-height: 100vh;
  display: block;
  --mono: ui-monospace,"JetBrains Mono","Geist Mono","SF Mono","IBM Plex Mono",Menlo,monospace;
  --sans: system-ui,"Inter","Geist",-apple-system,"Segoe UI",sans-serif;
  --bg: #0b1020;
  --ink: #f2f5ff;
  --muted: #c3ccea;
  --tok-key: #e9b8ff;
  --tok-str: #a7f3c4;
  --tok-fn: #a5d8ff;
  --tok-var: #ffe08a;
  --tok-num: #ffb0c4;
  --tok-punct: #c3ccea;
  --tok-op: #ffc9a3;
  --tok-com: #c3ccea;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
}

.cbk-15 *,
.cbk-15 *::before,
.cbk-15 *::after {
  box-sizing: border-box;
}

.cbk-15__stage {
  position: relative;
  display: grid;
  place-items: center;
  min-block-size: inherit;
  isolation: isolate;
  padding: clamp(1.5rem,5vw,4rem);
  overflow: hidden;
}

.cbk-15__amb {
  position: absolute;
  inset: 0;
  z-index: -1;
  background: #131a33;
}

.cbk-15__photo {
  inline-size: 100%;
  block-size: 100%;
  object-fit: cover;
  opacity: .62;
  filter: saturate(135%) contrast(102%);
}

.cbk-15__amb::after {
  content: "";
  position: absolute;
  inset: 0;
  background: radial-gradient(38rem 24rem at 12% 12%, rgba(99,102,241,.55), transparent 68%), radial-gradient(34rem 22rem at 88% 82%, rgba(236,72,153,.45), transparent 70%), linear-gradient(180deg, rgba(6,10,24,.35), rgba(6,10,24,.6));
}

.cbk-15__glass {
  position: relative;
  margin: 0;
  inline-size: min(50rem,100%);
  border-radius: 18px;
  overflow: hidden;
  container-type: inline-size;
  border: 1px solid rgba(255,255,255,.16);
  background: rgba(255,255,255,.07);
  -webkit-backdrop-filter: blur(22px) saturate(180%);
  backdrop-filter: blur(22px) saturate(180%);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.34), 0 30px 70px -30px rgba(0,0,0,.72);
}

@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .cbk-15__glass {
    background: rgba(14,17,24,.93);
  }
}

.cbk-15__bar {
  display: flex;
  align-items: center;
  gap: .6rem;
  padding: .7rem 1rem;
  border-block-end: 1px solid rgba(255,255,255,.14);
  background: rgba(255,255,255,.06);
}

.cbk-15__ico {
  display: grid;
  place-items: center;
  color: var(--ink);
  opacity: .85;
}

.cbk-15__ico svg {
  inline-size: 17px;
  block-size: 17px;
}

.cbk-15__title {
  color: var(--ink);
  font-family: var(--mono);
  font-size: .8125rem;
}

.cbk-15__chip {
  margin-inline-start: auto;
  padding: .18rem .55rem;
  border: 1px solid rgba(255,255,255,.28);
  border-radius: 999px;
  background: rgba(255,255,255,.12);
  color: var(--ink);
  font-family: var(--mono);
  font-size: .6875rem;
  letter-spacing: .08em;
  text-transform: uppercase;
}

.cbk-15__pre {
  margin: 0;
  padding: 1.25rem 1.35rem 1.45rem;
  overflow-x: auto;
  scrollbar-width: thin;
  font-family: var(--mono);
  font-size: clamp(.8125rem,.45rem + .5cqi,.9375rem);
  line-height: 1.8;
  white-space: pre;
  tab-size: 2;
  font-variant-ligatures: none;
  color: var(--ink);
}

.cbk-15__pre code {
  font: inherit;
}

.cbk-15 .tok-keyword {
  color: var(--tok-key);
}

.cbk-15 .tok-string {
  color: var(--tok-str);
}

.cbk-15 .tok-function {
  color: var(--tok-fn);
}

.cbk-15 .tok-variable {
  color: var(--tok-var);
}

.cbk-15 .tok-number {
  color: var(--tok-num);
}

.cbk-15 .tok-punct {
  color: var(--tok-punct);
}

.cbk-15 .tok-op {
  color: var(--tok-op);
}

.cbk-15 .tok-comment {
  color: var(--tok-com);
  font-style: italic;
}

.cbk-15[data-theme="light"] .cbk-15__photo {
  opacity: .5;
}

.cbk-15[data-theme="light"] .cbk-15__amb::after {
  background: radial-gradient(38rem 24rem at 12% 12%, rgba(129,140,248,.45), transparent 68%), radial-gradient(34rem 22rem at 88% 82%, rgba(244,114,182,.38), transparent 70%), linear-gradient(180deg, rgba(8,12,28,.28), rgba(8,12,28,.5));
}

@media (prefers-reduced-motion: reduce) {
  .cbk-15 *,
    .cbk-15 *::before,
    .cbk-15 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .cbk-15__glass {
    border: 2px solid CanvasText;
    background: Canvas;
    backdrop-filter: none;
    -webkit-backdrop-filter: none;
  }

  .cbk-15__amb {
    display: none;
  }

  .cbk-15 [class^="tok-"] {
    color: CanvasText;
  }
}
/* theme toggle — pure CSS, :has() driven; :checked = light theme, top-right of the stage */

.cbk-15__stage {
  position: relative;
}

.cbk-15__tbox {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  padding: 0;
  opacity: 0;
  pointer-events: none;
}

.cbk-15__tbtn {
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
  .cbk-15__tbtn {
    background: color-mix(in srgb, var(--ink,#e7eaf3) 10%, transparent);
    border-color: color-mix(in srgb, var(--ink,#e7eaf3) 26%, transparent);
  }
}

.cbk-15__tbtn:hover {
  transform: translateY(-1px);
}

.cbk-15__tbtn svg {
  inline-size: 1.0625rem;
  block-size: 1.0625rem;
}

.cbk-15__tbox:focus-visible + .cbk-15__tbtn {
  outline: 2px solid var(--ink,#e7eaf3);
  outline-offset: 2px;
}

.cbk-15__tmoon {
  display: none;
}

.cbk-15:has(.cbk-15__tbox:checked) .cbk-15__tsun {
  display: none;
}

.cbk-15:has(.cbk-15__tbox:checked) .cbk-15__tmoon {
  display: block;
}

@media (prefers-reduced-motion: reduce) {
  .cbk-15__tbtn {
    transition: none;
  }

  .cbk-15__tbtn:hover {
    transform: none;
  }
}

@media (forced-colors: active) {
  .cbk-15__tbtn {
    border: 1px solid ButtonBorder;
    color: ButtonText;
    background: ButtonFace;
  }
}

.cbk-15:has(.cbk-15__tbox:checked) .cbk-15__photo {
  opacity: .5;
}

.cbk-15:has(.cbk-15__tbox:checked) .cbk-15__amb::after {
  background: radial-gradient(38rem 24rem at 12% 12%, rgba(129,140,248,.45), transparent 68%), radial-gradient(34rem 22rem at 88% 82%, rgba(244,114,182,.38), transparent 70%), linear-gradient(180deg, rgba(8,12,28,.28), rgba(8,12,28,.5));
}

.cbk-15__theme {
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

.cbk-15[data-theme="dark"] .cbk-15__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .cbk-15:not([data-theme="light"]) .cbk-15__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.cbk-15__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.cbk-15[data-theme="dark"] .cbk-15__theme:hover,
.cbk-15:not([data-theme="light"]) .cbk-15__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.cbk-15__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.cbk-15__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.cbk-15__sun {
  display: none;
}

.cbk-15__theme[aria-pressed="true"] .cbk-15__sun {
  display: block;
}

.cbk-15__theme[aria-pressed="true"] .cbk-15__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .cbk-15__theme {
    transition: none;
  }

  .cbk-15__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(()=>{const r=document.querySelector('.cbk-15');if(!r)return;const t=r.querySelector('.cbk-15__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
