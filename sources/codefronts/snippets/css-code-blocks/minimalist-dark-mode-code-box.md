---
source: "codefronts"
url: "https://codefronts.com/snippets/css-code-blocks/minimalist-dark-mode-code-box/"
title: "Minimalist Dark Mode CSS Code Block"
section: "snippets"
category: "css-code-blocks"
category_name: "CSS Code Blocks"
description: "The default of this collection: no chrome, no buttons, no decoration — a hairline border, a deep neutral surface, honest monospace type and a comment colour…"
has_js: "true"
---

Here's a working CSS Code Block from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Minimalist Dark Mode CSS Code Block
Source: https://codefronts.com/snippets/css-code-blocks/minimalist-dark-mode-code-box/

The default of this collection: no chrome, no buttons, no decoration — a hairline border, a deep neutral surface, honest monospace type and a comment colour that recedes without disappearing. Everything else in the set is this block plus one idea, which is exactly how a real design system should treat its code display.
## HTML
```html
<div class="cbk-09">
  <button class="cbk-09__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="cbk-09__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="cbk-09__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <div class="cbk-09__stage">
    <input class="cbk-09__tbox" id="cbk-09-tbox" type="checkbox" data-alt="light" aria-label="Toggle light and dark theme">
    <label class="cbk-09__tbtn" for="cbk-09-tbox" title="Toggle light and dark theme">
      <svg class="cbk-09__tsun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4.2"></circle><path d="M12 2.4v2.3M12 19.3v2.3M2.4 12h2.3M19.3 12h2.3M5.2 5.2l1.6 1.6M17.2 17.2l1.6 1.6M18.8 5.2l-1.6 1.6M6.8 17.2l-1.6 1.6"></path></svg>
      <svg class="cbk-09__tmoon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.2 14.6A8.6 8.6 0 0 1 9.4 3.8a8.6 8.6 0 1 0 10.8 10.8Z"></path></svg>
    </label>
    <figure class="cbk-09__block">
      <span class="cbk-09__lang" aria-hidden="true">ts</span>
<pre class="cbk-09__pre"><code class="language-ts"><span class="tok-comment">// Debounce a resize observer callback without dropping the last frame.</span>
<span class="tok-keyword">export function</span> <span class="tok-function">debounce</span><span class="tok-op">&lt;</span><span class="tok-fn2">T</span> <span class="tok-keyword">extends</span> <span class="tok-punct">(...</span><span class="tok-variable">a</span><span class="tok-punct">:</span> <span class="tok-fn2">never</span><span class="tok-punct">[]) =&gt;</span> <span class="tok-fn2">void</span><span class="tok-op">&gt;</span><span class="tok-punct">(</span>
  <span class="tok-variable">fn</span><span class="tok-punct">:</span> <span class="tok-fn2">T</span><span class="tok-punct">,</span>
  <span class="tok-variable">wait</span> <span class="tok-op">=</span> <span class="tok-number">120</span><span class="tok-punct">,</span>
<span class="tok-punct">) {</span>
  <span class="tok-keyword">let</span> <span class="tok-variable">id</span><span class="tok-punct">:</span> <span class="tok-fn2">number</span> <span class="tok-op">|</span> <span class="tok-fn2">undefined</span><span class="tok-punct">;</span>

  <span class="tok-keyword">return</span> <span class="tok-punct">(...</span><span class="tok-variable">args</span><span class="tok-punct">:</span> <span class="tok-fn2">Parameters</span><span class="tok-op">&lt;</span><span class="tok-fn2">T</span><span class="tok-op">&gt;</span><span class="tok-punct">) =&gt; {</span>
    <span class="tok-function">clearTimeout</span><span class="tok-punct">(</span><span class="tok-variable">id</span><span class="tok-punct">);</span>
    <span class="tok-variable">id</span> <span class="tok-op">=</span> <span class="tok-function">setTimeout</span><span class="tok-punct">(() =&gt;</span> <span class="tok-function">fn</span><span class="tok-punct">(...</span><span class="tok-variable">args</span><span class="tok-punct">),</span> <span class="tok-variable">wait</span><span class="tok-punct">);</span>
  <span class="tok-punct">};</span>
<span class="tok-punct">}</span></code></pre>
    </figure>
  </div>
</div>
```
## CSS
```css
.cbk-09 {
  inline-size: 100%;
  width: 100%;
  min-block-size: 100vh;
  min-block-size: 100svh;
  min-height: 100vh;
  display: block;
  --mono: ui-monospace,"JetBrains Mono","Geist Mono","SF Mono","IBM Plex Mono",Menlo,monospace;
  --sans: system-ui,"Inter","Geist",-apple-system,"Segoe UI",sans-serif;
  --bg: #08090c;
  --surface: #0f1116;
  --line: #232733;
  --ink: #e8eaf0;
  --muted: #9aa2b1;
  --acc: #8b7cff;
  --tok-key: #c9a4ff;
  --tok-str: #8ce99a;
  --tok-fn: #82c8ff;
  --tok-var: #e8eaf0;
  --tok-num: #ff8fa9;
  --tok-punct: #8892a3;
  --tok-op: #ffa87a;
  --tok-fn2: #5eead4;
  --tok-com: #9aa2b1;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
}

@supports (color: oklch(50% .1 200)) {
  .cbk-09 {
    --bg: oklch(12% .011 265);
    --surface: oklch(16% .013 265);
    --line: oklch(26% .016 265);
    --ink: oklch(93% .008 265);
    --muted: oklch(66% .018 265);
    --acc: oklch(72% .16 292);
    --tok-com: oklch(66% .018 265);
  }
}

.cbk-09 *,
.cbk-09 *::before,
.cbk-09 *::after {
  box-sizing: border-box;
}

.cbk-09__stage {
  display: grid;
  place-items: center;
  min-block-size: inherit;
  padding: clamp(1rem,4vw,3.5rem);
}

.cbk-09__block {
  position: relative;
  margin: 0;
  inline-size: min(54rem,100%);
  border: 1px solid var(--line);
  border-radius: 14px;
  background: var(--surface);
  overflow: hidden;
  container-type: inline-size;
}

.cbk-09__lang {
  position: absolute;
  inset-block-start: .85rem;
  inset-inline-end: 1.1rem;
  color: var(--muted);
  opacity: .55;
  font-family: var(--mono);
  font-size: .6875rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  user-select: none;
}

.cbk-09__pre {
  margin: 0;
  padding: 1.45rem 1.6rem 1.6rem;
  overflow-x: auto;
  scrollbar-width: thin;
  scrollbar-color: var(--line) transparent;
  font-family: var(--mono);
  font-size: clamp(.8125rem,.45rem + .5cqi,.9375rem);
  line-height: 1.8;
  white-space: pre;
  tab-size: 2;
  font-variant-ligatures: none;
  font-feature-settings: "calt" 0;
}

.cbk-09__pre code {
  font: inherit;
}

.cbk-09__pre::selection,
.cbk-09__pre *::selection {
  background: color-mix(in oklab,var(--acc) 34%,transparent);
  color: #fff;
}

.cbk-09 .tok-keyword {
  color: var(--tok-key);
}

.cbk-09 .tok-string {
  color: var(--tok-str);
}

.cbk-09 .tok-function {
  color: var(--tok-fn);
}

.cbk-09 .tok-variable {
  color: var(--tok-var);
}

.cbk-09 .tok-number {
  color: var(--tok-num);
}

.cbk-09 .tok-punct {
  color: var(--tok-punct);
}

.cbk-09 .tok-op {
  color: var(--tok-op);
}

.cbk-09 .tok-fn2 {
  color: var(--tok-fn2);
}

.cbk-09 .tok-comment {
  color: var(--tok-com);
  font-style: italic;
}

.cbk-09__pre::-webkit-scrollbar {
  block-size: 8px;
}

.cbk-09__pre::-webkit-scrollbar-thumb {
  background: var(--line);
  border-radius: 999px;
}

.cbk-09[data-theme="light"] {
  --bg: #f7f8fa;
  --surface: #ffffff;
  --line: #e4e7ee;
  --ink: #12141a;
  --muted: #5b6272;
  --acc: #6d5efc;
  --tok-key: #8250df;
  --tok-str: #0a7d3f;
  --tok-fn: #0550ae;
  --tok-var: #12141a;
  --tok-num: #b1265c;
  --tok-punct: #57606a;
  --tok-op: #a2410a;
  --tok-fn2: #0f766e;
  --tok-com: #5b6272;
}

@media (prefers-color-scheme: light) {
  .cbk-09:not([data-theme="dark"]) {
    --bg: #f7f8fa;
    --surface: #ffffff;
    --line: #e4e7ee;
    --ink: #12141a;
    --muted: #5b6272;
    --acc: #6d5efc;
    --tok-key: #8250df;
    --tok-str: #0a7d3f;
    --tok-fn: #0550ae;
    --tok-var: #12141a;
    --tok-num: #b1265c;
    --tok-punct: #57606a;
    --tok-op: #a2410a;
    --tok-fn2: #0f766e;
    --tok-com: #5b6272;
  }
}

@media (forced-colors: active) {
  .cbk-09__block {
    border: 2px solid CanvasText;
    background: Canvas;
  }

  .cbk-09 [class^="tok-"] {
    color: CanvasText;
  }
}
/* theme toggle — pure CSS, :has() driven; :checked = light theme, top-right of the stage */

.cbk-09__stage {
  position: relative;
}

.cbk-09__tbox {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  padding: 0;
  opacity: 0;
  pointer-events: none;
}

.cbk-09__tbtn {
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
  .cbk-09__tbtn {
    background: color-mix(in srgb, var(--ink,#e7eaf3) 10%, transparent);
    border-color: color-mix(in srgb, var(--ink,#e7eaf3) 26%, transparent);
  }
}

.cbk-09__tbtn:hover {
  transform: translateY(-1px);
}

.cbk-09__tbtn svg {
  inline-size: 1.0625rem;
  block-size: 1.0625rem;
}

.cbk-09__tbox:focus-visible + .cbk-09__tbtn {
  outline: 2px solid var(--ink,#e7eaf3);
  outline-offset: 2px;
}

.cbk-09__tmoon {
  display: none;
}

.cbk-09:has(.cbk-09__tbox:checked) .cbk-09__tsun {
  display: none;
}

.cbk-09:has(.cbk-09__tbox:checked) .cbk-09__tmoon {
  display: block;
}

@media (prefers-reduced-motion: reduce) {
  .cbk-09__tbtn {
    transition: none;
  }

  .cbk-09__tbtn:hover {
    transform: none;
  }
}

@media (forced-colors: active) {
  .cbk-09__tbtn {
    border: 1px solid ButtonBorder;
    color: ButtonText;
    background: ButtonFace;
  }
}

.cbk-09:has(.cbk-09__tbox:checked) {
  --bg: #f7f8fa;
  --surface: #ffffff;
  --line: #e4e7ee;
  --ink: #12141a;
  --muted: #5b6272;
  --acc: #6d5efc;
  --tok-key: #8250df;
  --tok-str: #0a7d3f;
  --tok-fn: #0550ae;
  --tok-var: #12141a;
  --tok-num: #b1265c;
  --tok-punct: #57606a;
  --tok-op: #a2410a;
  --tok-fn2: #0f766e;
  --tok-com: #5b6272;
}

.cbk-09__theme {
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

.cbk-09[data-theme="dark"] .cbk-09__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .cbk-09:not([data-theme="light"]) .cbk-09__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.cbk-09__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.cbk-09[data-theme="dark"] .cbk-09__theme:hover,
.cbk-09:not([data-theme="light"]) .cbk-09__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.cbk-09__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.cbk-09__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.cbk-09__sun {
  display: none;
}

.cbk-09__theme[aria-pressed="true"] .cbk-09__sun {
  display: block;
}

.cbk-09__theme[aria-pressed="true"] .cbk-09__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .cbk-09__theme {
    transition: none;
  }

  .cbk-09__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(()=>{const r=document.querySelector('.cbk-09');if(!r)return;const t=r.querySelector('.cbk-09__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
