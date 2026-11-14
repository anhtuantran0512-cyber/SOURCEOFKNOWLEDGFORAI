---
source: "codefronts"
url: "https://codefronts.com/snippets/css-code-blocks/neumorphic-embedded-code-box/"
title: "Neumorphic Embedded CSS Code Box (Soft-UI)"
section: "snippets"
category: "css-code-blocks"
category_name: "CSS Code Blocks"
description: "Soft-UI done responsibly: the code sits in a recessed well carved out of the surface by two opposed inset shadows — light from the top-left, dark from the…"
has_js: "true"
---

Here's a working CSS Code Block from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neumorphic Embedded CSS Code Box (Soft-UI)
Source: https://codefronts.com/snippets/css-code-blocks/neumorphic-embedded-code-box/

Soft-UI done responsibly: the code sits in a recessed well carved out of the surface by two opposed inset shadows — light from the top-left, dark from the bottom-right — with a matching raised chip for the filename. Neumorphism's usual failure is contrast, so the well is tinted a step darker than the panel and the type stays at 8:1, which keeps the look without the audit failure.
## HTML
```html
<div class="cbk-17">
  <button class="cbk-17__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="cbk-17__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="cbk-17__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <div class="cbk-17__stage">
    <input class="cbk-17__tbox" id="cbk-17-tbox" type="checkbox" data-alt="dark" aria-label="Toggle light and dark theme">
    <label class="cbk-17__tbtn" for="cbk-17-tbox" title="Toggle light and dark theme">
      <svg class="cbk-17__tsun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4.2"></circle><path d="M12 2.4v2.3M12 19.3v2.3M2.4 12h2.3M19.3 12h2.3M5.2 5.2l1.6 1.6M17.2 17.2l1.6 1.6M18.8 5.2l-1.6 1.6M6.8 17.2l-1.6 1.6"></path></svg>
      <svg class="cbk-17__tmoon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.2 14.6A8.6 8.6 0 0 1 9.4 3.8a8.6 8.6 0 1 0 10.8 10.8Z"></path></svg>
    </label>
    <figure class="cbk-17__panel">
      <figcaption class="cbk-17__head">
        <span class="cbk-17__chip">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M6.5 3.5h7L18 8v12.5H6.5z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/><path d="M13 3.5V8h5" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg>
          use-media.ts
        </span>
        <span class="cbk-17__meta">hook &middot; 12 lines</span>
      </figcaption>

      <div class="cbk-17__well">
<pre class="cbk-17__pre"><code class="language-ts"><span class="tok-keyword">import</span> <span class="tok-punct">{</span> <span class="tok-variable">useEffect</span><span class="tok-punct">,</span> <span class="tok-variable">useState</span> <span class="tok-punct">}</span> <span class="tok-keyword">from</span> <span class="tok-string">'react'</span><span class="tok-punct">;</span>

<span class="tok-keyword">export function</span> <span class="tok-function">useMedia</span><span class="tok-punct">(</span><span class="tok-variable">query</span><span class="tok-punct">:</span> <span class="tok-fn2">string</span><span class="tok-punct">) {</span>
  <span class="tok-keyword">const</span> <span class="tok-punct">[</span><span class="tok-variable">matches</span><span class="tok-punct">,</span> <span class="tok-variable">setMatches</span><span class="tok-punct">] =</span> <span class="tok-function">useState</span><span class="tok-punct">(</span><span class="tok-keyword">false</span><span class="tok-punct">);</span>

  <span class="tok-function">useEffect</span><span class="tok-punct">(() =&gt; {</span>
    <span class="tok-keyword">const</span> <span class="tok-variable">mql</span> <span class="tok-op">=</span> <span class="tok-variable">matchMedia</span><span class="tok-punct">(</span><span class="tok-variable">query</span><span class="tok-punct">);</span>
    <span class="tok-keyword">const</span> <span class="tok-variable">sync</span> <span class="tok-op">=</span> <span class="tok-punct">() =&gt;</span> <span class="tok-function">setMatches</span><span class="tok-punct">(</span><span class="tok-variable">mql</span><span class="tok-punct">.</span><span class="tok-variable">matches</span><span class="tok-punct">);</span>
    <span class="tok-function">sync</span><span class="tok-punct">();</span>
    <span class="tok-variable">mql</span><span class="tok-punct">.</span><span class="tok-function">addEventListener</span><span class="tok-punct">(</span><span class="tok-string">'change'</span><span class="tok-punct">,</span> <span class="tok-variable">sync</span><span class="tok-punct">);</span>
    <span class="tok-keyword">return</span> <span class="tok-punct">() =&gt;</span> <span class="tok-variable">mql</span><span class="tok-punct">.</span><span class="tok-function">removeEventListener</span><span class="tok-punct">(</span><span class="tok-string">'change'</span><span class="tok-punct">,</span> <span class="tok-variable">sync</span><span class="tok-punct">);</span>
  <span class="tok-punct">}, [</span><span class="tok-variable">query</span><span class="tok-punct">]);</span>

  <span class="tok-keyword">return</span> <span class="tok-variable">matches</span><span class="tok-punct">;</span>
<span class="tok-punct">}</span></code></pre>
      </div>
    </figure>
  </div>
</div>
```
## CSS
```css
.cbk-17 {
  inline-size: 100%;
  width: 100%;
  min-block-size: 100vh;
  min-block-size: 100svh;
  min-height: 100vh;
  display: block;
  --mono: ui-monospace,"JetBrains Mono","Geist Mono","SF Mono","IBM Plex Mono",Menlo,monospace;
  --sans: system-ui,"Inter","Geist",-apple-system,"Segoe UI",sans-serif;
  --bg: #e8eaf0;
  --panel: #e8eaf0;
  --well: #e0e3ea;
  --ink: #1d2028;
  --muted: #5f6577;
  --light: #ffffff;
  --shade: #c3c8d4;
  --acc: #6d5efc;
  --tok-key: #7b3fe4;
  --tok-str: #0a7d3f;
  --tok-fn: #0550ae;
  --tok-var: #1d2028;
  --tok-num: #b1265c;
  --tok-punct: #5f6577;
  --tok-fn2: #0f766e;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
}

@supports (color: oklch(50% .1 200)) {
  .cbk-17 {
    --bg: oklch(92.5% .008 270);
    --panel: oklch(92.5% .008 270);
    --well: oklch(89.5% .009 270);
    --ink: oklch(24% .014 270);
    --muted: oklch(50% .016 270);
    --light: oklch(100% 0 0);
    --shade: oklch(80% .012 270);
    --acc: oklch(58% .2 292);
  }
}

.cbk-17 *,
.cbk-17 *::before,
.cbk-17 *::after {
  box-sizing: border-box;
}

.cbk-17__stage {
  display: grid;
  place-items: center;
  min-block-size: inherit;
  padding: clamp(1.5rem,5vw,4rem);
}

.cbk-17__panel {
  margin: 0;
  inline-size: min(50rem,100%);
  padding: clamp(1.1rem,3vw,1.6rem);
  border-radius: 22px;
  background: var(--panel);
  container-type: inline-size;
  box-shadow: -8px -8px 20px var(--light), 8px 8px 22px var(--shade);
}

.cbk-17__head {
  display: flex;
  align-items: center;
  gap: .75rem;
  margin-block-end: 1.1rem;
}

.cbk-17__chip {
  display: inline-flex;
  align-items: center;
  gap: .45rem;
  padding: .5rem .8rem;
  border-radius: 12px;
  background: var(--panel);
  color: var(--ink);
  font-family: var(--mono);
  font-size: .78125rem;
  font-weight: 500;
  box-shadow: -4px -4px 10px var(--light), 4px 4px 10px var(--shade);
}

.cbk-17__chip svg {
  inline-size: 14px;
  block-size: 14px;
  color: var(--muted);
}

.cbk-17__meta {
  margin-inline-start: auto;
  color: var(--muted);
  font-size: .75rem;
}

.cbk-17__well {
  border-radius: 18px;
  background: var(--well);
  overflow: hidden;
  box-shadow: inset 6px 6px 14px var(--shade), inset -6px -6px 14px var(--light);
}

.cbk-17__pre {
  margin: 0;
  padding: 1.25rem 1.35rem 1.4rem;
  overflow-x: auto;
  scrollbar-width: thin;
  scrollbar-color: var(--shade) transparent;
  font-family: var(--mono);
  font-size: clamp(.78125rem,.45rem + .48cqi,.90625rem);
  line-height: 1.8;
  white-space: pre;
  tab-size: 2;
  font-variant-ligatures: none;
  color: var(--ink);
}

.cbk-17__pre code {
  font: inherit;
}

.cbk-17 .tok-keyword {
  color: var(--tok-key);
  font-weight: 500;
}

.cbk-17 .tok-string {
  color: var(--tok-str);
}

.cbk-17 .tok-function {
  color: var(--tok-fn);
}

.cbk-17 .tok-variable {
  color: var(--tok-var);
}

.cbk-17 .tok-number {
  color: var(--tok-num);
}

.cbk-17 .tok-punct {
  color: var(--tok-punct);
}

.cbk-17 .tok-fn2 {
  color: var(--tok-fn2);
}

.cbk-17 :focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.cbk-17[data-theme="dark"] {
  --bg: #22252c;
  --panel: #22252c;
  --well: #1d2027;
  --ink: #e9ecf2;
  --muted: #a3aab8;
  --light: rgba(255,255,255,.045);
  --shade: rgba(0,0,0,.55);
  --acc: #a08cff;
  --tok-key: #d0b3ff;
  --tok-str: #8ce99a;
  --tok-fn: #8ec8ff;
  --tok-var: #e9ecf2;
  --tok-num: #ff9db4;
  --tok-punct: #a3aab8;
  --tok-fn2: #5eead4;
}

@media (prefers-color-scheme: dark) {
  .cbk-17:not([data-theme="light"]) {
    --bg: #22252c;
    --panel: #22252c;
    --well: #1d2027;
    --ink: #e9ecf2;
    --muted: #a3aab8;
    --light: rgba(255,255,255,.045);
    --shade: rgba(0,0,0,.55);
    --acc: #a08cff;
    --tok-key: #d0b3ff;
    --tok-str: #8ce99a;
    --tok-fn: #8ec8ff;
    --tok-var: #e9ecf2;
    --tok-num: #ff9db4;
    --tok-punct: #a3aab8;
    --tok-fn2: #5eead4;
  }
}

@media (forced-colors: active) {
  .cbk-17__panel,
    .cbk-17__well,
    .cbk-17__chip {
    border: 2px solid CanvasText;
    background: Canvas;
    box-shadow: none;
  }

  .cbk-17 [class^="tok-"] {
    color: CanvasText;
  }
}
/* theme toggle — pure CSS, :has() driven; :checked = dark theme, top-right of the stage */

.cbk-17__stage {
  position: relative;
}

.cbk-17__tbox {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  padding: 0;
  opacity: 0;
  pointer-events: none;
}

.cbk-17__tbtn {
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
  .cbk-17__tbtn {
    background: color-mix(in srgb, var(--ink,#e7eaf3) 10%, transparent);
    border-color: color-mix(in srgb, var(--ink,#e7eaf3) 26%, transparent);
  }
}

.cbk-17__tbtn:hover {
  transform: translateY(-1px);
}

.cbk-17__tbtn svg {
  inline-size: 1.0625rem;
  block-size: 1.0625rem;
}

.cbk-17__tbox:focus-visible + .cbk-17__tbtn {
  outline: 2px solid var(--ink,#e7eaf3);
  outline-offset: 2px;
}

.cbk-17__tsun {
  display: none;
}

.cbk-17:has(.cbk-17__tbox:checked) .cbk-17__tmoon {
  display: none;
}

.cbk-17:has(.cbk-17__tbox:checked) .cbk-17__tsun {
  display: block;
}

@media (prefers-reduced-motion: reduce) {
  .cbk-17__tbtn {
    transition: none;
  }

  .cbk-17__tbtn:hover {
    transform: none;
  }
}

@media (forced-colors: active) {
  .cbk-17__tbtn {
    border: 1px solid ButtonBorder;
    color: ButtonText;
    background: ButtonFace;
  }
}

.cbk-17:has(.cbk-17__tbox:checked) {
  --bg: #22252c;
  --panel: #22252c;
  --well: #1d2027;
  --ink: #e9ecf2;
  --muted: #a3aab8;
  --light: rgba(255,255,255,.045);
  --shade: rgba(0,0,0,.55);
  --acc: #a08cff;
  --tok-key: #d0b3ff;
  --tok-str: #8ce99a;
  --tok-fn: #8ec8ff;
  --tok-var: #e9ecf2;
  --tok-num: #ff9db4;
  --tok-punct: #a3aab8;
  --tok-fn2: #5eead4;
}

.cbk-17__theme {
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

.cbk-17[data-theme="dark"] .cbk-17__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .cbk-17:not([data-theme="light"]) .cbk-17__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.cbk-17__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.cbk-17[data-theme="dark"] .cbk-17__theme:hover,
.cbk-17:not([data-theme="light"]) .cbk-17__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.cbk-17__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.cbk-17__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.cbk-17__sun {
  display: none;
}

.cbk-17__theme[aria-pressed="true"] .cbk-17__sun {
  display: block;
}

.cbk-17__theme[aria-pressed="true"] .cbk-17__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .cbk-17__theme {
    transition: none;
  }

  .cbk-17__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(()=>{const r=document.querySelector('.cbk-17');if(!r)return;const t=r.querySelector('.cbk-17__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
