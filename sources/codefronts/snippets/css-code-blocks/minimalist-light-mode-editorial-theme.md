---
source: "codefronts"
url: "https://codefronts.com/snippets/css-code-blocks/minimalist-light-mode-editorial-theme/"
title: "Minimalist Light Mode CSS Code Block (Editorial Theme)"
section: "snippets"
category: "css-code-blocks"
category_name: "CSS Code Blocks"
description: "A code block designed for reading, not for a dark terminal: a warm off-white paper surface, a serif italic filename in the margin, a hairline rule instead of…"
has_js: "true"
---

Here's a working CSS Code Block from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Minimalist Light Mode CSS Code Block (Editorial Theme)
Source: https://codefronts.com/snippets/css-code-blocks/minimalist-light-mode-editorial-theme/

A code block designed for reading, not for a dark terminal: a warm off-white paper surface, a serif italic filename in the margin, a hairline rule instead of a chrome bar, generous leading, and a restrained light syntax palette where every token clears 4.5:1 on paper. The style long-form publishers reach for when code appears inside an essay.
## HTML
```html
<div class="cbk-19">
  <button class="cbk-19__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="cbk-19__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="cbk-19__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <div class="cbk-19__stage">
    <input class="cbk-19__tbox" id="cbk-19-tbox" type="checkbox" data-alt="dark" aria-label="Toggle light and dark theme">
    <label class="cbk-19__tbtn" for="cbk-19-tbox" title="Toggle light and dark theme">
      <svg class="cbk-19__tsun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4.2"></circle><path d="M12 2.4v2.3M12 19.3v2.3M2.4 12h2.3M19.3 12h2.3M5.2 5.2l1.6 1.6M17.2 17.2l1.6 1.6M18.8 5.2l-1.6 1.6M6.8 17.2l-1.6 1.6"></path></svg>
      <svg class="cbk-19__tmoon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.2 14.6A8.6 8.6 0 0 1 9.4 3.8a8.6 8.6 0 1 0 10.8 10.8Z"></path></svg>
    </label>
    <figure class="cbk-19__block">
      <figcaption class="cbk-19__label">theme.config.ts <span class="cbk-19__dot" aria-hidden="true">&middot;</span> <span class="cbk-19__lang">TypeScript</span></figcaption>

<pre class="cbk-19__pre"><code class="language-ts"><span class="tok-comment">// Typography scale for the reading surface.</span>
<span class="tok-keyword">export const</span> <span class="tok-variable">type</span> <span class="tok-op">=</span> <span class="tok-punct">{</span>
  <span class="tok-variable">body</span><span class="tok-punct">: {</span>
    <span class="tok-variable">family</span><span class="tok-punct">:</span> <span class="tok-string">'"Source Serif 4", Georgia, serif'</span><span class="tok-punct">,</span>
    <span class="tok-variable">size</span><span class="tok-punct">:</span> <span class="tok-string">'clamp(1.0625rem, 1rem + 0.3vw, 1.1875rem)'</span><span class="tok-punct">,</span>
    <span class="tok-variable">leading</span><span class="tok-punct">:</span> <span class="tok-number">1.72</span><span class="tok-punct">,</span>
  <span class="tok-punct">},</span>
  <span class="tok-variable">code</span><span class="tok-punct">: {</span>
    <span class="tok-variable">family</span><span class="tok-punct">:</span> <span class="tok-string">'"JetBrains Mono", ui-monospace, monospace'</span><span class="tok-punct">,</span>
    <span class="tok-variable">size</span><span class="tok-punct">:</span> <span class="tok-string">'0.9375rem'</span><span class="tok-punct">,</span>
    <span class="tok-variable">leading</span><span class="tok-punct">:</span> <span class="tok-number">1.85</span><span class="tok-punct">,</span>
  <span class="tok-punct">},</span>
<span class="tok-punct">} </span><span class="tok-keyword">as const</span><span class="tok-punct">;</span></code></pre>
    </figure>
  </div>
</div>
```
## CSS
```css
.cbk-19 {
  inline-size: 100%;
  width: 100%;
  min-block-size: 100vh;
  min-block-size: 100svh;
  min-height: 100vh;
  display: block;
  --mono: ui-monospace,"JetBrains Mono","Geist Mono","SF Mono","IBM Plex Mono",Menlo,monospace;
  --serif: "Iowan Old Style","Source Serif 4",Georgia,"Times New Roman",serif;
  --sans: system-ui,"Inter","Geist",-apple-system,"Segoe UI",sans-serif;
  --bg: #f7f5f0;
  --paper: #fdfcf9;
  --rule: #e8e4da;
  --ink: #22242b;
  --muted: #6b6559;
  --acc: #8a5a1a;
  --tok-key: #6b21a8;
  --tok-str: #15803d;
  --tok-fn: #1d4ed8;
  --tok-var: #22242b;
  --tok-num: #a21458;
  --tok-punct: #5c5f68;
  --tok-op: #9a4a12;
  --tok-com: #7a7466;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
}

@supports (color: oklch(50% .1 200)) {
  .cbk-19 {
    --bg: oklch(96.5% .008 85);
    --paper: oklch(98.6% .006 85);
    --rule: oklch(91% .008 85);
    --ink: oklch(24% .014 265);
    --muted: oklch(50% .018 75);
    --acc: oklch(48% .11 65);
    --tok-key: oklch(45% .2 300);
    --tok-str: oklch(42% .13 150);
    --tok-fn: oklch(42% .16 258);
    --tok-var: oklch(24% .014 265);
    --tok-num: oklch(45% .17 5);
    --tok-punct: oklch(48% .012 265);
    --tok-op: oklch(46% .13 55);
    --tok-com: oklch(50% .02 75);
  }
}

.cbk-19 *,
.cbk-19 *::before,
.cbk-19 *::after {
  box-sizing: border-box;
}

.cbk-19__stage {
  display: grid;
  place-items: center;
  min-block-size: inherit;
  padding: clamp(1.25rem,5vw,4rem);
}

.cbk-19__block {
  margin: 0;
  inline-size: min(50rem,100%);
  padding: 1.35rem clamp(1.1rem,3vw,1.75rem) 1.6rem;
  border: 1px solid var(--rule);
  border-inline-start: 3px solid var(--rule);
  border-radius: 6px;
  background: var(--paper);
  container-type: inline-size;
  transition: border-inline-start-color .25s;
}

.cbk-19__block:hover {
  border-inline-start-color: var(--acc);
}

.cbk-19__label {
  display: flex;
  align-items: baseline;
  gap: .45rem;
  padding-block-end: .75rem;
  margin-block-end: 1.1rem;
  border-block-end: 1px solid var(--rule);
  color: var(--muted);
  font-family: var(--serif);
  font-style: italic;
  font-size: .9375rem;
  letter-spacing: .005em;
}

.cbk-19__dot {
  opacity: .6;
}

.cbk-19__lang {
  font-family: var(--sans);
  font-style: normal;
  font-size: .71875rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  opacity: .85;
}

.cbk-19__pre {
  margin: 0;
  overflow-x: auto;
  scrollbar-width: thin;
  scrollbar-color: var(--rule) transparent;
  font-family: var(--mono);
  font-size: clamp(.8125rem,.5rem + .45cqi,.9375rem);
  line-height: 1.85;
  white-space: pre;
  tab-size: 2;
  font-variant-ligatures: none;
  font-variant-numeric: tabular-nums;
  color: var(--ink);
}

.cbk-19__pre code {
  font: inherit;
}

.cbk-19__pre::selection,
.cbk-19__pre *::selection {
  background: color-mix(in oklab,var(--acc) 20%,transparent);
}

.cbk-19 .tok-keyword {
  color: var(--tok-key);
  font-weight: 500;
}

.cbk-19 .tok-string {
  color: var(--tok-str);
}

.cbk-19 .tok-function {
  color: var(--tok-fn);
}

.cbk-19 .tok-variable {
  color: var(--tok-var);
}

.cbk-19 .tok-number {
  color: var(--tok-num);
}

.cbk-19 .tok-punct {
  color: var(--tok-punct);
}

.cbk-19 .tok-op {
  color: var(--tok-op);
}

.cbk-19 .tok-comment {
  color: var(--tok-com);
  font-style: italic;
}

.cbk-19[data-theme="dark"] {
  --bg: #111014;
  --paper: #17161c;
  --rule: #2a2833;
  --ink: #eeecf2;
  --muted: #a7a0b0;
  --acc: #e0b083;
  --tok-key: #d8b4fe;
  --tok-str: #86efac;
  --tok-fn: #93c5fd;
  --tok-var: #eeecf2;
  --tok-num: #fda4c0;
  --tok-punct: #a7a0b0;
  --tok-op: #fdba74;
  --tok-com: #a7a0b0;
}

@media (prefers-color-scheme: dark) {
  .cbk-19:not([data-theme="light"]) {
    --bg: #111014;
    --paper: #17161c;
    --rule: #2a2833;
    --ink: #eeecf2;
    --muted: #a7a0b0;
    --acc: #e0b083;
    --tok-key: #d8b4fe;
    --tok-str: #86efac;
    --tok-fn: #93c5fd;
    --tok-var: #eeecf2;
    --tok-num: #fda4c0;
    --tok-punct: #a7a0b0;
    --tok-op: #fdba74;
    --tok-com: #a7a0b0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cbk-19 * {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .cbk-19__block {
    border: 2px solid CanvasText;
    background: Canvas;
  }

  .cbk-19 [class^="tok-"] {
    color: CanvasText;
  }
}
/* theme toggle — pure CSS, :has() driven; :checked = dark theme, top-right of the stage */

.cbk-19__stage {
  position: relative;
}

.cbk-19__tbox {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  padding: 0;
  opacity: 0;
  pointer-events: none;
}

.cbk-19__tbtn {
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
  .cbk-19__tbtn {
    background: color-mix(in srgb, var(--ink,#e7eaf3) 10%, transparent);
    border-color: color-mix(in srgb, var(--ink,#e7eaf3) 26%, transparent);
  }
}

.cbk-19__tbtn:hover {
  transform: translateY(-1px);
}

.cbk-19__tbtn svg {
  inline-size: 1.0625rem;
  block-size: 1.0625rem;
}

.cbk-19__tbox:focus-visible + .cbk-19__tbtn {
  outline: 2px solid var(--ink,#e7eaf3);
  outline-offset: 2px;
}

.cbk-19__tsun {
  display: none;
}

.cbk-19:has(.cbk-19__tbox:checked) .cbk-19__tmoon {
  display: none;
}

.cbk-19:has(.cbk-19__tbox:checked) .cbk-19__tsun {
  display: block;
}

@media (prefers-reduced-motion: reduce) {
  .cbk-19__tbtn {
    transition: none;
  }

  .cbk-19__tbtn:hover {
    transform: none;
  }
}

@media (forced-colors: active) {
  .cbk-19__tbtn {
    border: 1px solid ButtonBorder;
    color: ButtonText;
    background: ButtonFace;
  }
}

.cbk-19:has(.cbk-19__tbox:checked) {
  --bg: #111014;
  --paper: #17161c;
  --rule: #2a2833;
  --ink: #eeecf2;
  --muted: #a7a0b0;
  --acc: #e0b083;
  --tok-key: #d8b4fe;
  --tok-str: #86efac;
  --tok-fn: #93c5fd;
  --tok-var: #eeecf2;
  --tok-num: #fda4c0;
  --tok-punct: #a7a0b0;
  --tok-op: #fdba74;
  --tok-com: #a7a0b0;
}

.cbk-19__theme {
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

.cbk-19[data-theme="dark"] .cbk-19__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .cbk-19:not([data-theme="light"]) .cbk-19__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.cbk-19__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.cbk-19[data-theme="dark"] .cbk-19__theme:hover,
.cbk-19:not([data-theme="light"]) .cbk-19__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.cbk-19__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.cbk-19__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.cbk-19__sun {
  display: none;
}

.cbk-19__theme[aria-pressed="true"] .cbk-19__sun {
  display: block;
}

.cbk-19__theme[aria-pressed="true"] .cbk-19__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .cbk-19__theme {
    transition: none;
  }

  .cbk-19__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(()=>{const r=document.querySelector('.cbk-19');if(!r)return;const t=r.querySelector('.cbk-19__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
