---
source: "codefronts"
url: "https://codefronts.com/snippets/css-code-blocks/code-block-with-highlighted-line-range-focus-callout/"
title: "Code Block with Highlighted Line Range (Focus Callout)"
section: "snippets"
category: "css-code-blocks"
category_name: "CSS Code Blocks"
description: "Tutorial writing lives or dies on \"look at these lines\"."
has_js: "true"
---

Here's a working CSS Code Block from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Code Block with Highlighted Line Range (Focus Callout)
Source: https://codefronts.com/snippets/css-code-blocks/code-block-with-highlighted-line-range-focus-callout/

Tutorial writing lives or dies on "look at these lines". This block marks a range with data-hl, washes those rows in accent tint with an inline-start rail, dims the rest to 55% so the eye lands where you point, and pins a side annotation to the range — the Docusaurus {4-6} highlight, done in CSS with the range stated as text in the header so it is never colour-only.
## HTML
```html
<div class="cbk-08">
  <button class="cbk-08__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="cbk-08__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="cbk-08__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <div class="cbk-08__stage">
    <input class="cbk-08__tbox" id="cbk-08-tbox" type="checkbox" data-alt="light" aria-label="Toggle light and dark theme">
    <label class="cbk-08__tbtn" for="cbk-08-tbox" title="Toggle light and dark theme">
      <svg class="cbk-08__tsun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4.2"></circle><path d="M12 2.4v2.3M12 19.3v2.3M2.4 12h2.3M19.3 12h2.3M5.2 5.2l1.6 1.6M17.2 17.2l1.6 1.6M18.8 5.2l-1.6 1.6M6.8 17.2l-1.6 1.6"></path></svg>
      <svg class="cbk-08__tmoon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.2 14.6A8.6 8.6 0 0 1 9.4 3.8a8.6 8.6 0 1 0 10.8 10.8Z"></path></svg>
    </label>
    <figure class="cbk-08__block">
      <figcaption class="cbk-08__bar">
        <span class="cbk-08__file">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M6.5 3.5h7L18 8v12.5H6.5z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/><path d="M13 3.5V8h5" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg>
          middleware.ts
        </span>
        <span class="cbk-08__range">highlighting lines 7&ndash;9</span>
        <span class="cbk-08__lang">TypeScript</span>
      </figcaption>

      <div class="cbk-08__body">
        <div class="cbk-08__scroll">
<pre class="cbk-08__pre"><code class="language-ts cbk-08__code"><span class="cbk-08__l"><span class="tok-keyword">import</span> <span class="tok-punct">{</span> <span class="tok-variable">NextResponse</span> <span class="tok-punct">}</span> <span class="tok-keyword">from</span> <span class="tok-string">'next/server'</span><span class="tok-punct">;</span></span>
<span class="cbk-08__l"><span class="tok-keyword">import</span> <span class="tok-punct">{</span> <span class="tok-variable">verifySession</span> <span class="tok-punct">}</span> <span class="tok-keyword">from</span> <span class="tok-string">'@/lib/auth'</span><span class="tok-punct">;</span></span>
<span class="cbk-08__l"></span>
<span class="cbk-08__l"><span class="tok-keyword">export async function</span> <span class="tok-function">middleware</span><span class="tok-punct">(</span><span class="tok-variable">req</span><span class="tok-punct">:</span> <span class="tok-fn2">Request</span><span class="tok-punct">) {</span></span>
<span class="cbk-08__l">  <span class="tok-keyword">const</span> <span class="tok-variable">session</span> <span class="tok-op">=</span> <span class="tok-keyword">await</span> <span class="tok-function">verifySession</span><span class="tok-punct">(</span><span class="tok-variable">req</span><span class="tok-punct">);</span></span>
<span class="cbk-08__l"></span>
<span class="cbk-08__l" data-hl>  <span class="tok-keyword">if</span> <span class="tok-punct">(!</span><span class="tok-variable">session</span><span class="tok-punct">) {</span></span>
<span class="cbk-08__l" data-hl>    <span class="tok-keyword">const</span> <span class="tok-variable">url</span> <span class="tok-op">=</span> <span class="tok-keyword">new</span> <span class="tok-function">URL</span><span class="tok-punct">(</span><span class="tok-string">'/login'</span><span class="tok-punct">,</span> <span class="tok-variable">req</span><span class="tok-punct">.</span><span class="tok-variable">url</span><span class="tok-punct">);</span></span>
<span class="cbk-08__l" data-hl>    <span class="tok-keyword">return</span> <span class="tok-variable">NextResponse</span><span class="tok-punct">.</span><span class="tok-function">redirect</span><span class="tok-punct">(</span><span class="tok-variable">url</span><span class="tok-punct">,</span> <span class="tok-punct">{</span> <span class="tok-variable">status</span><span class="tok-punct">:</span> <span class="tok-number">307</span> <span class="tok-punct">});</span></span>
<span class="cbk-08__l">  <span class="tok-punct">}</span></span>
<span class="cbk-08__l"></span>
<span class="cbk-08__l">  <span class="tok-keyword">return</span> <span class="tok-variable">NextResponse</span><span class="tok-punct">.</span><span class="tok-function">next</span><span class="tok-punct">();</span></span>
<span class="cbk-08__l"><span class="tok-punct">}</span></span>
<span class="cbk-08__l"></span>
<span class="cbk-08__l"><span class="tok-keyword">export const</span> <span class="tok-variable">config</span> <span class="tok-op">=</span> <span class="tok-punct">{</span> <span class="tok-variable">matcher</span><span class="tok-punct">: [</span><span class="tok-string">'/app/:path*'</span><span class="tok-punct">] };</span></span></code></pre>
        </div>

        <aside class="cbk-08__note">
          <b>307, not 302.</b> A temporary redirect that preserves the request method — the whole reason this branch exists.
        </aside>
      </div>
    </figure>
  </div>
</div>
```
## CSS
```css
.cbk-08 {
  inline-size: 100%;
  width: 100%;
  min-block-size: 100vh;
  min-block-size: 100svh;
  min-height: 100vh;
  display: block;
  --mono: ui-monospace,"JetBrains Mono","Geist Mono","SF Mono","IBM Plex Mono",Menlo,monospace;
  --sans: system-ui,"Inter","Geist",-apple-system,"Segoe UI",sans-serif;
  --bg: #07080c;
  --surface: #0e1017;
  --bar: #12151e;
  --line: #212533;
  --ink: #e7eaf3;
  --muted: #8e96a7;
  --acc: #fbbf24;
  --note: #141824;
  --tok-key: #d2a8ff;
  --tok-str: #7ee787;
  --tok-fn: #79c0ff;
  --tok-var: #e7eaf3;
  --tok-num: #ff85a1;
  --tok-punct: #8b96a8;
  --tok-op: #ff9d6b;
  --tok-fn2: #5eead4;
  background: radial-gradient(62rem 34rem at 50% -10%, #1d1a12 0%, transparent 62%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
}

@supports (color: oklch(50% .1 200)) {
  .cbk-08 {
    --bg: oklch(12% .012 265);
    --surface: oklch(16.5% .014 265);
    --bar: oklch(19.5% .016 265);
    --line: oklch(27% .018 265);
    --ink: oklch(93% .008 265);
    --muted: oklch(69% .02 265);
    --acc: oklch(84% .15 85);
    --note: oklch(21% .02 265);
  }
}

.cbk-08 *,
.cbk-08 *::before,
.cbk-08 *::after {
  box-sizing: border-box;
}

.cbk-08__stage {
  display: grid;
  place-items: center;
  min-block-size: inherit;
  padding: clamp(1rem,4vw,3.5rem);
}

.cbk-08__block {
  margin: 0;
  inline-size: min(68rem,100%);
  border: 1px solid var(--line);
  border-radius: 14px;
  background: var(--surface);
  overflow: hidden;
  container-type: inline-size;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.04), 0 22px 56px -30px rgba(0,0,0,.9);
}

.cbk-08__bar {
  display: flex;
  align-items: center;
  gap: .7rem;
  flex-wrap: wrap;
  padding: .65rem 1rem;
  border-block-end: 1px solid var(--line);
  background: var(--bar);
  font-size: .78125rem;
}

.cbk-08__file {
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  color: var(--ink);
  font-family: var(--mono);
}

.cbk-08__file svg {
  inline-size: 14px;
  block-size: 14px;
  color: var(--muted);
}

.cbk-08__range {
  padding: .18rem .5rem;
  border-radius: 6px;
  background: color-mix(in oklab,var(--acc) 15%,transparent);
  color: var(--acc);
  font-family: var(--mono);
  font-size: .71875rem;
}

.cbk-08__lang {
  margin-inline-start: auto;
  color: var(--muted);
  font-size: .71875rem;
  letter-spacing: .03em;
}

.cbk-08__body {
  position: relative;
}

.cbk-08__scroll {
  overflow: auto;
  scrollbar-gutter: stable;
}

.cbk-08__pre {
  margin: 0;
  padding: 1.1rem 0 1.3rem;
  font-family: var(--mono);
  font-size: clamp(.78125rem,.45rem + .48cqi,.90625rem);
  line-height: 1.85;
  white-space: pre;
  tab-size: 2;
  font-variant-ligatures: none;
}

.cbk-08__code {
  counter-reset: cbk08;
  display: block;
  font: inherit;
}

.cbk-08__l {
  display: block;
  counter-increment: cbk08;
  padding-inline: 0 1rem;
  min-inline-size: 100%;
}

.cbk-08__l::before {
  content: counter(cbk08);
  display: inline-block;
  inline-size: 3.5ch;
  margin-inline-end: 1.1rem;
  text-align: end;
  color: var(--muted);
  opacity: .45;
  user-select: none;
  font-variant-numeric: tabular-nums;
}

.cbk-08__code:has([data-hl]) .cbk-08__l:not([data-hl]) {
  opacity: .55;
}

.cbk-08__l[data-hl] {
  background: rgba(251,191,36,.10);
  background: color-mix(in oklab,var(--acc) 12%,transparent);
  box-shadow: inset 3px 0 0 var(--acc);
}

.cbk-08__l[data-hl]::before {
  opacity: .9;
  color: var(--acc);
}

.cbk-08__note {
  position: absolute;
  inset-block-start: calc(1.1rem + 6 * 1.85em);
  inset-inline-end: 1.1rem;
  max-inline-size: 15rem;
  padding: .7rem .85rem;
  border: 1px solid color-mix(in oklab,var(--acc) 30%,var(--line));
  border-radius: 11px;
  background: var(--note);
  color: var(--muted);
  font-size: .78125rem;
  line-height: 1.55;
  text-wrap: pretty;
  box-shadow: 0 12px 30px -18px rgba(0,0,0,.9);
}

.cbk-08__note b {
  color: var(--acc);
  font-weight: 600;
}

.cbk-08__note::after {
  content: "";
  position: absolute;
  inset-inline-start: -5px;
  inset-block-start: 1.15rem;
  inline-size: 9px;
  block-size: 9px;
  rotate: 45deg;
  background: var(--note);
  border-inline-start: 1px solid color-mix(in oklab,var(--acc) 30%,var(--line));
  border-block-end: 1px solid color-mix(in oklab,var(--acc) 30%,var(--line));
}

@container (max-width: 46rem) {
  .cbk-08__note {
    position: static;
    max-inline-size: none;
    margin: 0 1rem 1.1rem;
    box-shadow: none;
  }

  .cbk-08__note::after {
    display: none;
  }
}

.cbk-08 .tok-keyword {
  color: var(--tok-key);
}

.cbk-08 .tok-string {
  color: var(--tok-str);
}

.cbk-08 .tok-function {
  color: var(--tok-fn);
}

.cbk-08 .tok-variable {
  color: var(--tok-var);
}

.cbk-08 .tok-number {
  color: var(--tok-num);
}

.cbk-08 .tok-punct {
  color: var(--tok-punct);
}

.cbk-08 .tok-op {
  color: var(--tok-op);
}

.cbk-08 .tok-fn2 {
  color: var(--tok-fn2);
}

.cbk-08[data-theme="light"] {
  --bg: #f8f7f4;
  --surface: #ffffff;
  --bar: #f4f3ee;
  --line: #e6e4dc;
  --ink: #131318;
  --muted: #5e6068;
  --acc: #b45309;
  --note: #fdfaf3;
  --tok-key: #8250df;
  --tok-str: #0a7d3f;
  --tok-fn: #0550ae;
  --tok-var: #131318;
  --tok-num: #b1265c;
  --tok-punct: #57606a;
  --tok-op: #a2410a;
  --tok-fn2: #0f766e;
  background: radial-gradient(62rem 34rem at 50% -10%, #f6efe1 0%, transparent 62%), var(--bg);
}

@media (prefers-color-scheme: light) {
  .cbk-08:not([data-theme="dark"]) {
    --bg: #f8f7f4;
    --surface: #ffffff;
    --bar: #f4f3ee;
    --line: #e6e4dc;
    --ink: #131318;
    --muted: #5e6068;
    --acc: #b45309;
    --note: #fdfaf3;
    --tok-key: #8250df;
    --tok-str: #0a7d3f;
    --tok-fn: #0550ae;
    --tok-var: #131318;
    --tok-num: #b1265c;
    --tok-punct: #57606a;
    --tok-op: #a2410a;
    --tok-fn2: #0f766e;
    background: radial-gradient(62rem 34rem at 50% -10%, #f6efe1 0%, transparent 62%), var(--bg);
  }
}

@media (forced-colors: active) {
  .cbk-08__block {
    border: 2px solid CanvasText;
    background: Canvas;
  }

  .cbk-08__l[data-hl] {
    box-shadow: inset 4px 0 0 Highlight;
    background: Canvas;
  }

  .cbk-08__code:has([data-hl]) .cbk-08__l:not([data-hl]) {
    opacity: 1;
  }

  .cbk-08 [class^="tok-"] {
    color: CanvasText;
  }
}
/* theme toggle — pure CSS, :has() driven; :checked = light theme, top-right of the stage */

.cbk-08__stage {
  position: relative;
}

.cbk-08__tbox {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  padding: 0;
  opacity: 0;
  pointer-events: none;
}

.cbk-08__tbtn {
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
  .cbk-08__tbtn {
    background: color-mix(in srgb, var(--ink,#e7eaf3) 10%, transparent);
    border-color: color-mix(in srgb, var(--ink,#e7eaf3) 26%, transparent);
  }
}

.cbk-08__tbtn:hover {
  transform: translateY(-1px);
}

.cbk-08__tbtn svg {
  inline-size: 1.0625rem;
  block-size: 1.0625rem;
}

.cbk-08__tbox:focus-visible + .cbk-08__tbtn {
  outline: 2px solid var(--ink,#e7eaf3);
  outline-offset: 2px;
}

.cbk-08__tmoon {
  display: none;
}

.cbk-08:has(.cbk-08__tbox:checked) .cbk-08__tsun {
  display: none;
}

.cbk-08:has(.cbk-08__tbox:checked) .cbk-08__tmoon {
  display: block;
}

@media (prefers-reduced-motion: reduce) {
  .cbk-08__tbtn {
    transition: none;
  }

  .cbk-08__tbtn:hover {
    transform: none;
  }
}

@media (forced-colors: active) {
  .cbk-08__tbtn {
    border: 1px solid ButtonBorder;
    color: ButtonText;
    background: ButtonFace;
  }
}

.cbk-08:has(.cbk-08__tbox:checked) {
  --bg: #f8f7f4;
  --surface: #ffffff;
  --bar: #f4f3ee;
  --line: #e6e4dc;
  --ink: #131318;
  --muted: #5e6068;
  --acc: #b45309;
  --note: #fdfaf3;
  --tok-key: #8250df;
  --tok-str: #0a7d3f;
  --tok-fn: #0550ae;
  --tok-var: #131318;
  --tok-num: #b1265c;
  --tok-punct: #57606a;
  --tok-op: #a2410a;
  --tok-fn2: #0f766e;
  background: radial-gradient(62rem 34rem at 50% -10%, #f6efe1 0%, transparent 62%), var(--bg);
}

.cbk-08__theme {
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

.cbk-08[data-theme="dark"] .cbk-08__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .cbk-08:not([data-theme="light"]) .cbk-08__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.cbk-08__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.cbk-08[data-theme="dark"] .cbk-08__theme:hover,
.cbk-08:not([data-theme="light"]) .cbk-08__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.cbk-08__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.cbk-08__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.cbk-08__sun {
  display: none;
}

.cbk-08__theme[aria-pressed="true"] .cbk-08__sun {
  display: block;
}

.cbk-08__theme[aria-pressed="true"] .cbk-08__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .cbk-08__theme {
    transition: none;
  }

  .cbk-08__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(()=>{const r=document.querySelector('.cbk-08');if(!r)return;const t=r.querySelector('.cbk-08__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
