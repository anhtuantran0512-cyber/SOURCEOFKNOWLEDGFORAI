---
source: "codefronts"
url: "https://codefronts.com/snippets/css-code-blocks/code-block-with-syntax-highlighting-prism-style-token-colors/"
title: "Code Block with Syntax Highlighting (Prism-Style Token Colors)"
section: "snippets"
category: "css-code-blocks"
category_name: "CSS Code Blocks"
description: "Syntax highlighting is just CSS — the highlighter's only job is to wrap tokens in spans."
has_js: "true"
---

Here's a working CSS Code Block from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Code Block with Syntax Highlighting (Prism-Style Token Colors)
Source: https://codefronts.com/snippets/css-code-blocks/code-block-with-syntax-highlighting-prism-style-token-colors/

Syntax highlighting is just CSS — the highlighter's only job is to wrap tokens in spans. This block hand-wraps a real ES2024 module in <span class="tok-keyword">, tok-string, tok-comment, tok-function, tok-variable, tok-number and tok-punct, then colours them from one oklch() token scale that follows the Prism / One Dark convention. Drop real Prism, Shiki or highlight.js output in later and the same rules light it up.
## HTML
```html
<div class="cbk-01">
  <button class="cbk-01__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="cbk-01__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="cbk-01__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <div class="cbk-01__stage">
    <input class="cbk-01__tbox" id="cbk-01-tbox" type="checkbox" data-alt="light" aria-label="Toggle light and dark theme">
    <label class="cbk-01__tbtn" for="cbk-01-tbox" title="Toggle light and dark theme">
      <svg class="cbk-01__tsun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4.2"></circle><path d="M12 2.4v2.3M12 19.3v2.3M2.4 12h2.3M19.3 12h2.3M5.2 5.2l1.6 1.6M17.2 17.2l1.6 1.6M18.8 5.2l-1.6 1.6M6.8 17.2l-1.6 1.6"></path></svg>
      <svg class="cbk-01__tmoon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.2 14.6A8.6 8.6 0 0 1 9.4 3.8a8.6 8.6 0 1 0 10.8 10.8Z"></path></svg>
    </label>
    <figure class="cbk-01__block">
      <figcaption class="cbk-01__bar">
        <span class="cbk-01__dot" aria-hidden="true"></span>
        <span class="cbk-01__file">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M6.5 3.5h7L18 8v12.5H6.5z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/><path d="M13 3.5V8h5" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg>
          loadWorkspaces.js
        </span>
        <span class="cbk-01__pill">Prism.js compatible</span>
        <span class="cbk-01__lang">JavaScript</span>
      </figcaption>
      <div class="cbk-01__scroll">
<pre class="cbk-01__pre"><code class="language-js"><span class="tok-comment">// Fetch a member's workspaces once, then serve from the LRU cache.</span>
<span class="tok-keyword">import</span> <span class="tok-punct">{</span> <span class="tok-variable">cache</span> <span class="tok-punct">}</span> <span class="tok-keyword">from</span> <span class="tok-string">'./lru-cache.mjs'</span><span class="tok-punct">;</span>

<span class="tok-keyword">const</span> <span class="tok-variable">ENDPOINT</span> <span class="tok-op">=</span> <span class="tok-string">'/api/v2/workspaces'</span><span class="tok-punct">;</span>
<span class="tok-keyword">const</span> <span class="tok-variable">TTL</span> <span class="tok-op">=</span> <span class="tok-number">60_000</span><span class="tok-punct">;</span>

<span class="tok-keyword">export</span> <span class="tok-keyword">async</span> <span class="tok-keyword">function</span> <span class="tok-function">loadWorkspaces</span><span class="tok-punct">(</span><span class="tok-variable">userId</span><span class="tok-punct">, {</span> <span class="tok-variable">limit</span> <span class="tok-op">=</span> <span class="tok-number">25</span> <span class="tok-punct">} = {}) {</span>
  <span class="tok-keyword">const</span> <span class="tok-variable">hit</span> <span class="tok-op">=</span> <span class="tok-variable">cache</span><span class="tok-punct">.</span><span class="tok-function">get</span><span class="tok-punct">(</span><span class="tok-variable">userId</span><span class="tok-punct">, </span><span class="tok-variable">TTL</span><span class="tok-punct">);</span>
  <span class="tok-keyword">if</span> <span class="tok-punct">(</span><span class="tok-variable">hit</span><span class="tok-punct">) </span><span class="tok-keyword">return</span> <span class="tok-variable">hit</span><span class="tok-punct">;</span>

  <span class="tok-keyword">const</span> <span class="tok-variable">res</span> <span class="tok-op">=</span> <span class="tok-keyword">await</span> <span class="tok-function">fetch</span><span class="tok-punct">(</span><span class="tok-string">`${ENDPOINT}?user=${userId}&amp;limit=${limit}`</span><span class="tok-punct">);</span>
  <span class="tok-keyword">if</span> <span class="tok-punct">(!</span><span class="tok-variable">res</span><span class="tok-punct">.</span><span class="tok-variable">ok</span><span class="tok-punct">) </span><span class="tok-keyword">throw</span> <span class="tok-keyword">new</span> <span class="tok-function">Error</span><span class="tok-punct">(</span><span class="tok-string">`workspaces ${res.status}`</span><span class="tok-punct">);</span>
  <span class="tok-keyword">return</span> <span class="tok-variable">cache</span><span class="tok-punct">.</span><span class="tok-function">set</span><span class="tok-punct">(</span><span class="tok-variable">userId</span><span class="tok-punct">, </span><span class="tok-keyword">await</span> <span class="tok-variable">res</span><span class="tok-punct">.</span><span class="tok-function">json</span><span class="tok-punct">());</span>
<span class="tok-punct">}</span></code></pre>
      </div>
    </figure>
  </div>
</div>
```
## CSS
```css
.cbk-01 {
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
  --bar: #12141d;
  --line: #232733;
  --ink: #e7eaf2;
  --muted: #98a0b0;
  --acc: #a78bfa;
  --tok-key: #d2a8ff;
  --tok-str: #7ee787;
  --tok-fn: #79c0ff;
  --tok-var: #ffcb6b;
  --tok-num: #ff85a1;
  --tok-com: #98a2b3;
  --tok-punct: #8b96a8;
  --tok-op: #ff9d6b;
  background: radial-gradient(60rem 34rem at 50% -10%, #171b2b 0%, transparent 62%) , var(--bg);
  color: var(--ink);
  font-family: var(--sans);
}

@supports (color: oklch(50% .1 200)) {
  .cbk-01 {
    --bg: oklch(13% .012 265);
    --surface: oklch(17% .015 265);
    --bar: oklch(20% .017 265);
    --line: oklch(28% .018 265);
    --ink: oklch(93% .008 265);
    --muted: oklch(70% .02 265);
    --acc: oklch(74% .16 300);
    --tok-key: oklch(80% .15 305);
    --tok-str: oklch(85% .18 148);
    --tok-fn: oklch(80% .13 245);
    --tok-var: oklch(85% .13 85);
    --tok-num: oklch(78% .15 5);
    --tok-com: oklch(72% .02 265);
    --tok-punct: oklch(68% .02 265);
    --tok-op: oklch(80% .13 45);
  }
}

.cbk-01 *,
.cbk-01 *::before,
.cbk-01 *::after {
  box-sizing: border-box;
}

.cbk-01__stage {
  display: grid;
  place-items: center;
  min-block-size: inherit;
  padding: clamp(1rem,4vw,3.5rem);
}

.cbk-01__block {
  margin: 0;
  inline-size: min(64rem,100%);
  border: 1px solid var(--line);
  border-radius: 16px;
  background: var(--surface);
  overflow: hidden;
  box-shadow: 0 1px 0 rgba(255,255,255,.05) inset, 0 24px 60px -28px rgba(0,0,0,.9);
}

.cbk-01__bar {
  display: flex;
  align-items: center;
  gap: .7rem;
  padding: .75rem 1rem;
  border-block-end: 1px solid var(--line);
  background: linear-gradient(180deg,var(--bar),var(--surface));
  font-size: .8125rem;
  flex-wrap: wrap;
}

.cbk-01__dot {
  inline-size: 9px;
  block-size: 9px;
  border-radius: 50%;
  background: var(--acc);
  box-shadow: 0 0 0 3px color-mix(in oklab,var(--acc) 22%,transparent);
}

.cbk-01__file {
  display: inline-flex;
  align-items: center;
  gap: .45rem;
  color: var(--ink);
  font-family: var(--mono);
  font-size: .8125rem;
}

.cbk-01__file svg {
  inline-size: 15px;
  block-size: 15px;
  color: var(--muted);
}

.cbk-01__pill {
  margin-inline-start: auto;
  padding: .2rem .55rem;
  border: 1px solid color-mix(in oklab,var(--acc) 38%,transparent);
  border-radius: 999px;
  background: color-mix(in oklab,var(--acc) 14%,transparent);
  color: var(--acc);
  font-size: .6875rem;
  font-weight: 600;
  letter-spacing: .06em;
  text-transform: uppercase;
}

.cbk-01__lang {
  padding: .2rem .5rem;
  border: 1px solid var(--line);
  border-radius: 6px;
  background: var(--bg);
  color: var(--muted);
  font-family: var(--mono);
  font-size: .6875rem;
  letter-spacing: .04em;
}

.cbk-01__scroll {
  overflow: auto;
  scrollbar-gutter: stable;
  overscroll-behavior-inline: contain;
}

.cbk-01__pre {
  margin: 0;
  padding: 1.15rem 1.25rem 1.35rem;
  font-family: var(--mono);
  font-size: clamp(.8125rem,.42rem + .55cqi,.9375rem);
  line-height: 1.75;
  white-space: pre;
  tab-size: 2;
  font-variant-ligatures: none;
  color: var(--ink);
}

.cbk-01__pre code {
  font: inherit;
  color: inherit;
}

.cbk-01 .tok-keyword {
  color: var(--tok-key);
  font-weight: 500;
}

.cbk-01 .tok-string {
  color: var(--tok-str);
}

.cbk-01 .tok-function {
  color: var(--tok-fn);
}

.cbk-01 .tok-variable {
  color: var(--tok-var);
}

.cbk-01 .tok-number {
  color: var(--tok-num);
  font-variant-numeric: tabular-nums;
}

.cbk-01 .tok-comment {
  color: var(--tok-com);
  font-style: italic;
}

.cbk-01 .tok-punct {
  color: var(--tok-punct);
}

.cbk-01 .tok-op {
  color: var(--tok-op);
}

.cbk-01__scroll::-webkit-scrollbar {
  block-size: 10px;
}

.cbk-01__scroll::-webkit-scrollbar-thumb {
  background: var(--line);
  border-radius: 999px;
}

.cbk-01[data-theme="light"] {
  --bg: #f6f7fb;
  --surface: #ffffff;
  --bar: #f2f3f9;
  --line: #e3e6f0;
  --ink: #12141c;
  --muted: #5d6577;
  --acc: #7c3aed;
  --tok-key: #8250df;
  --tok-str: #0a7d3f;
  --tok-fn: #0550ae;
  --tok-var: #8a5a00;
  --tok-num: #b1265c;
  --tok-com: #5d6577;
  --tok-punct: #57606a;
  --tok-op: #a2410a;
  background: radial-gradient(60rem 34rem at 50% -10%, #e9ecff 0%, transparent 62%), var(--bg);
}

.cbk-01[data-theme="light"] .cbk-01__block {
  box-shadow: 0 1px 0 #fff inset, 0 18px 44px -30px rgba(16,20,40,.45);
}

@media (prefers-color-scheme: light) {
  .cbk-01:not([data-theme="dark"]) {
    --bg: #f6f7fb;
    --surface: #ffffff;
    --bar: #f2f3f9;
    --line: #e3e6f0;
    --ink: #12141c;
    --muted: #5d6577;
    --acc: #7c3aed;
    --tok-key: #8250df;
    --tok-str: #0a7d3f;
    --tok-fn: #0550ae;
    --tok-var: #8a5a00;
    --tok-num: #b1265c;
    --tok-com: #5d6577;
    --tok-punct: #57606a;
    --tok-op: #a2410a;
    background: radial-gradient(60rem 34rem at 50% -10%, #e9ecff 0%, transparent 62%), var(--bg);
  }

  .cbk-01:not([data-theme="dark"]) .cbk-01__block {
    box-shadow: 0 1px 0 #fff inset, 0 18px 44px -30px rgba(16,20,40,.45);
  }
}

@media (forced-colors: active) {
  .cbk-01__block {
    border: 2px solid CanvasText;
    background: Canvas;
  }

  .cbk-01__pill,
    .cbk-01__lang {
    border: 1px solid CanvasText;
    color: CanvasText;
    background: Canvas;
  }

  .cbk-01 [class^="tok-"] {
    color: CanvasText;
  }
}
/* theme toggle — pure CSS, :has() driven; :checked = light theme, top-right of the stage */

.cbk-01__stage {
  position: relative;
}

.cbk-01__tbox {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  padding: 0;
  opacity: 0;
  pointer-events: none;
}

.cbk-01__tbtn {
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
  .cbk-01__tbtn {
    background: color-mix(in srgb, var(--ink,#e7eaf3) 10%, transparent);
    border-color: color-mix(in srgb, var(--ink,#e7eaf3) 26%, transparent);
  }
}

.cbk-01__tbtn:hover {
  transform: translateY(-1px);
}

.cbk-01__tbtn svg {
  inline-size: 1.0625rem;
  block-size: 1.0625rem;
}

.cbk-01__tbox:focus-visible + .cbk-01__tbtn {
  outline: 2px solid var(--ink,#e7eaf3);
  outline-offset: 2px;
}

.cbk-01__tmoon {
  display: none;
}

.cbk-01:has(.cbk-01__tbox:checked) .cbk-01__tsun {
  display: none;
}

.cbk-01:has(.cbk-01__tbox:checked) .cbk-01__tmoon {
  display: block;
}

@media (prefers-reduced-motion: reduce) {
  .cbk-01__tbtn {
    transition: none;
  }

  .cbk-01__tbtn:hover {
    transform: none;
  }
}

@media (forced-colors: active) {
  .cbk-01__tbtn {
    border: 1px solid ButtonBorder;
    color: ButtonText;
    background: ButtonFace;
  }
}

.cbk-01:has(.cbk-01__tbox:checked) {
  --bg: #f6f7fb;
  --surface: #ffffff;
  --bar: #f2f3f9;
  --line: #e3e6f0;
  --ink: #12141c;
  --muted: #5d6577;
  --acc: #7c3aed;
  --tok-key: #8250df;
  --tok-str: #0a7d3f;
  --tok-fn: #0550ae;
  --tok-var: #8a5a00;
  --tok-num: #b1265c;
  --tok-com: #5d6577;
  --tok-punct: #57606a;
  --tok-op: #a2410a;
  background: radial-gradient(60rem 34rem at 50% -10%, #e9ecff 0%, transparent 62%), var(--bg);
}

.cbk-01:has(.cbk-01__tbox:checked) .cbk-01__block {
  box-shadow: 0 1px 0 #fff inset, 0 18px 44px -30px rgba(16,20,40,.45);
}

.cbk-01__theme {
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

.cbk-01[data-theme="dark"] .cbk-01__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .cbk-01:not([data-theme="light"]) .cbk-01__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.cbk-01__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.cbk-01[data-theme="dark"] .cbk-01__theme:hover,
.cbk-01:not([data-theme="light"]) .cbk-01__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.cbk-01__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.cbk-01__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.cbk-01__sun {
  display: none;
}

.cbk-01__theme[aria-pressed="true"] .cbk-01__sun {
  display: block;
}

.cbk-01__theme[aria-pressed="true"] .cbk-01__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .cbk-01__theme {
    transition: none;
  }

  .cbk-01__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(()=>{const r=document.querySelector('.cbk-01');if(!r)return;const t=r.querySelector('.cbk-01__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
