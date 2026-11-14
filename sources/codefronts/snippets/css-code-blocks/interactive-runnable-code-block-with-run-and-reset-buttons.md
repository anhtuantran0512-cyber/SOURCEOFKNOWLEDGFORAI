---
source: "codefronts"
url: "https://codefronts.com/snippets/css-code-blocks/interactive-runnable-code-block-with-run-and-reset-buttons/"
title: "Interactive Runnable Code Block with Run and Reset Buttons"
section: "snippets"
category: "css-code-blocks"
category_name: "CSS Code Blocks"
description: "The pattern Astro Docs, MDX playgrounds and Sandpack all use: a code block with Run and Reset in the chrome and an output console that slides in underneath."
has_js: "true"
---

Here's a working CSS Code Block from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Interactive Runnable Code Block with Run and Reset Buttons
Source: https://codefronts.com/snippets/css-code-blocks/interactive-runnable-code-block-with-run-and-reset-buttons/

The pattern Astro Docs, MDX playgrounds and Sandpack all use: a code block with Run and Reset in the chrome and an output console that slides in underneath. This demo simulates the run (a 420ms pending state, then staggered output lines with a real exit code) so you can drop it into docs today and wire it to a worker, a WASM sandbox or a remote runner later — the UI contract does not change.
## HTML
```html
<div class="cbk-07" id="cbk-07-root" data-state="idle">
  <button class="cbk-07__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="cbk-07__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="cbk-07__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <div class="cbk-07__stage">
    <input class="cbk-07__tbox" id="cbk-07-tbox" type="checkbox" data-alt="light" aria-label="Toggle light and dark theme">
    <label class="cbk-07__tbtn" for="cbk-07-tbox" title="Toggle light and dark theme">
      <svg class="cbk-07__tsun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4.2"></circle><path d="M12 2.4v2.3M12 19.3v2.3M2.4 12h2.3M19.3 12h2.3M5.2 5.2l1.6 1.6M17.2 17.2l1.6 1.6M18.8 5.2l-1.6 1.6M6.8 17.2l-1.6 1.6"></path></svg>
      <svg class="cbk-07__tmoon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.2 14.6A8.6 8.6 0 0 1 9.4 3.8a8.6 8.6 0 1 0 10.8 10.8Z"></path></svg>
    </label>
    <figure class="cbk-07__block">
      <figcaption class="cbk-07__bar">
        <span class="cbk-07__badge">JS</span>
        <span class="cbk-07__file">group-by.js</span>
        <div class="cbk-07__acts">
          <button class="cbk-07__btn cbk-07__btn--run" type="button" id="cbk-07-run">
            <svg class="cbk-07__pi" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M8 5.6v12.8L19 12z" fill="currentColor"/></svg>
            <svg class="cbk-07__spin" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-dasharray="14 36"/></svg>
            <span class="cbk-07__btn-t">Run</span>
          </button>
          <button class="cbk-07__btn cbk-07__btn--reset" type="button" id="cbk-07-reset" disabled>
            <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M5.5 12a6.5 6.5 0 1 1 2.1 4.8" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/><path d="M5 7.5V12h4.4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
            <span class="cbk-07__btn-t">Reset</span>
          </button>
        </div>
      </figcaption>

      <div class="cbk-07__scroll">
<pre class="cbk-07__pre"><code class="language-js"><span class="tok-keyword">const</span> <span class="tok-variable">releases</span> <span class="tok-op">=</span> <span class="tok-punct">[</span>
  <span class="tok-punct">{</span> <span class="tok-variable">pkg</span><span class="tok-punct">:</span> <span class="tok-string">'astro'</span><span class="tok-punct">,</span>        <span class="tok-variable">channel</span><span class="tok-punct">:</span> <span class="tok-string">'stable'</span> <span class="tok-punct">},</span>
  <span class="tok-punct">{</span> <span class="tok-variable">pkg</span><span class="tok-punct">:</span> <span class="tok-string">'tailwindcss'</span><span class="tok-punct">,</span>  <span class="tok-variable">channel</span><span class="tok-punct">:</span> <span class="tok-string">'stable'</span> <span class="tok-punct">},</span>
  <span class="tok-punct">{</span> <span class="tok-variable">pkg</span><span class="tok-punct">:</span> <span class="tok-string">'framer-motion'</span><span class="tok-punct">,</span> <span class="tok-variable">channel</span><span class="tok-punct">:</span> <span class="tok-string">'beta'</span> <span class="tok-punct">},</span>
<span class="tok-punct">];</span>

<span class="tok-keyword">const</span> <span class="tok-variable">byChannel</span> <span class="tok-op">=</span> <span class="tok-fn2">Object</span><span class="tok-punct">.</span><span class="tok-function">groupBy</span><span class="tok-punct">(</span><span class="tok-variable">releases</span><span class="tok-punct">, (</span><span class="tok-variable">r</span><span class="tok-punct">) =&gt;</span> <span class="tok-variable">r</span><span class="tok-punct">.</span><span class="tok-variable">channel</span><span class="tok-punct">);</span>

<span class="tok-keyword">for</span> <span class="tok-punct">(</span><span class="tok-keyword">const</span> <span class="tok-punct">[</span><span class="tok-variable">channel</span><span class="tok-punct">,</span> <span class="tok-variable">list</span><span class="tok-punct">]</span> <span class="tok-keyword">of</span> <span class="tok-fn2">Object</span><span class="tok-punct">.</span><span class="tok-function">entries</span><span class="tok-punct">(</span><span class="tok-variable">byChannel</span><span class="tok-punct">)) {</span>
  <span class="tok-variable">console</span><span class="tok-punct">.</span><span class="tok-function">log</span><span class="tok-punct">(</span><span class="tok-variable">channel</span><span class="tok-punct">,</span> <span class="tok-variable">list</span><span class="tok-punct">.</span><span class="tok-function">map</span><span class="tok-punct">((</span><span class="tok-variable">r</span><span class="tok-punct">) =&gt;</span> <span class="tok-variable">r</span><span class="tok-punct">.</span><span class="tok-variable">pkg</span><span class="tok-punct">));</span>
<span class="tok-punct">}</span></code></pre>
      </div>

      <div class="cbk-07__out" id="cbk-07-out" role="region" aria-label="Output" aria-live="polite">
        <div>
          <div class="cbk-07__out-in">
            <p class="cbk-07__out-h">
              <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="m7 9 3 3-3 3m6 0h4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/><rect x="3.2" y="4.5" width="17.6" height="15" rx="2.4" stroke="currentColor" stroke-width="1.5"/></svg>
              Console
              <span class="cbk-07__exit">exit 0 &middot; 12ms</span>
            </p>
<pre class="cbk-07__lines"><span class="cbk-07__line" style="--i:0">stable <span class="tok-punct">[</span> <span class="tok-string">'astro'</span><span class="tok-punct">,</span> <span class="tok-string">'tailwindcss'</span> <span class="tok-punct">]</span></span>
<span class="cbk-07__line" style="--i:1">beta <span class="tok-punct">[</span> <span class="tok-string">'framer-motion'</span> <span class="tok-punct">]</span></span>
<span class="cbk-07__line cbk-07__line--dim" style="--i:2">&rarr; 2 channels, 3 packages</span></pre>
          </div>
        </div>
      </div>
    </figure>
  </div>
</div>
```
## CSS
```css
.cbk-07 {
  inline-size: 100%;
  width: 100%;
  min-block-size: 100vh;
  min-block-size: 100svh;
  min-height: 100vh;
  display: block;
  --mono: ui-monospace,"JetBrains Mono","Geist Mono","SF Mono","IBM Plex Mono",Menlo,monospace;
  --sans: system-ui,"Inter","Geist",-apple-system,"Segoe UI",sans-serif;
  --bg: #07080c;
  --surface: #0e1117;
  --bar: #12161f;
  --out: #0a0d13;
  --line: #212634;
  --ink: #e7eaf3;
  --muted: #8e96a7;
  --acc: #34d399;
  --err: #f87171;
  --tok-key: #d2a8ff;
  --tok-str: #7ee787;
  --tok-fn: #79c0ff;
  --tok-var: #ffcb6b;
  --tok-num: #ff85a1;
  --tok-punct: #8b96a8;
  --tok-op: #ff9d6b;
  --tok-fn2: #5eead4;
  background: radial-gradient(60rem 34rem at 50% -10%, #10201c 0%, transparent 62%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
}

@supports (color: oklch(50% .1 200)) {
  .cbk-07 {
    --bg: oklch(12% .012 260);
    --surface: oklch(16.5% .014 260);
    --bar: oklch(20% .016 260);
    --out: oklch(14% .013 260);
    --line: oklch(27% .018 260);
    --ink: oklch(93% .008 260);
    --muted: oklch(69% .02 260);
    --acc: oklch(82% .16 165);
  }
}

.cbk-07 *,
.cbk-07 *::before,
.cbk-07 *::after {
  box-sizing: border-box;
}

.cbk-07__stage {
  display: grid;
  place-items: center;
  min-block-size: inherit;
  padding: clamp(1rem,4vw,3.5rem);
}

.cbk-07__block {
  margin: 0;
  inline-size: min(56rem,100%);
  border: 1px solid var(--line);
  border-radius: 14px;
  background: var(--surface);
  overflow: hidden;
  container-type: inline-size;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.04), 0 22px 56px -30px rgba(0,0,0,.9);
}

.cbk-07__bar {
  display: flex;
  align-items: center;
  gap: .6rem;
  padding: .55rem .6rem .55rem .9rem;
  border-block-end: 1px solid var(--line);
  background: var(--bar);
}

.cbk-07__badge {
  padding: .2rem .45rem;
  border: 1px solid color-mix(in oklab,var(--tok-var) 32%,transparent);
  border-radius: 6px;
  background: color-mix(in oklab,var(--tok-var) 13%,transparent);
  color: var(--tok-var);
  font-family: var(--mono);
  font-size: .6875rem;
  font-weight: 600;
  letter-spacing: .06em;
}

.cbk-07__file {
  color: var(--muted);
  font-family: var(--mono);
  font-size: .78125rem;
}

.cbk-07__acts {
  display: flex;
  gap: .4rem;
  margin-inline-start: auto;
}

.cbk-07__btn {
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  min-block-size: 36px;
  padding: .4rem .7rem;
  border: 1px solid var(--line);
  border-radius: 9px;
  background: color-mix(in oklab,var(--ink) 5%,transparent);
  color: var(--muted);
  font-family: var(--sans);
  font-size: .78125rem;
  font-weight: 500;
  cursor: pointer;
  transition: color .16s, background-color .16s, border-color .16s, scale .12s;
}

.cbk-07__btn svg {
  inline-size: 15px;
  block-size: 15px;
}

.cbk-07__btn:active {
  scale: .96;
}

.cbk-07__btn--run {
  color: #04140d;
  background: var(--acc);
  border-color: color-mix(in oklab,var(--acc) 70%,transparent);
  font-weight: 600;
}

.cbk-07__btn--run:hover {
  filter: brightness(1.08);
}

.cbk-07__btn--reset:hover {
  color: var(--ink);
  border-color: color-mix(in oklab,var(--ink) 26%,transparent);
}

.cbk-07__btn:disabled {
  opacity: .42;
  cursor: not-allowed;
}

.cbk-07__spin {
  display: none;
}

.cbk-07[data-state="running"] .cbk-07__pi {
  display: none;
}

.cbk-07[data-state="running"] .cbk-07__spin {
  display: block;
  animation: cbk-07-spin .7s linear infinite;
}

@keyframes cbk-07-spin {
  to {
    rotate: 360deg;
  }
}

.cbk-07__scroll {
  overflow: auto;
  scrollbar-gutter: stable;
  transition: opacity .2s;
}

.cbk-07[data-state="running"] .cbk-07__scroll {
  opacity: .55;
}

.cbk-07__pre {
  margin: 0;
  padding: 1.1rem 1.25rem 1.25rem;
  font-family: var(--mono);
  font-size: clamp(.78125rem,.45rem + .5cqi,.90625rem);
  line-height: 1.75;
  white-space: pre;
  tab-size: 2;
  font-variant-ligatures: none;
}

.cbk-07__pre code {
  font: inherit;
}

.cbk-07__out {
  display: grid;
  grid-template-rows: 0fr;
  border-block-start: 1px solid transparent;
}

.cbk-07__out > div {
  overflow: hidden;
}

@supports (grid-template-rows: 0fr) {
  .cbk-07__out {
    transition: grid-template-rows .34s cubic-bezier(.2,.9,.25,1), border-color .34s;
  }
}

.cbk-07[data-state="done"] .cbk-07__out {
  grid-template-rows: 1fr;
  border-block-start-color: var(--line);
}

.cbk-07__out-in {
  background: var(--out);
  padding: .85rem 1.25rem 1.1rem;
}

.cbk-07__out-h {
  display: flex;
  align-items: center;
  gap: .4rem;
  margin: 0 0 .5rem;
  color: var(--muted);
  font-size: .71875rem;
  letter-spacing: .06em;
  text-transform: uppercase;
}

.cbk-07__out-h svg {
  inline-size: 14px;
  block-size: 14px;
}

.cbk-07__exit {
  margin-inline-start: auto;
  padding: .12rem .4rem;
  border-radius: 5px;
  text-transform: none;
  letter-spacing: 0;
  background: color-mix(in oklab,var(--acc) 15%,transparent);
  color: var(--acc);
  font-family: var(--mono);
}

.cbk-07__lines {
  margin: 0;
  font-family: var(--mono);
  font-size: .8125rem;
  line-height: 1.8;
  white-space: pre-wrap;
  color: var(--ink);
}

.cbk-07__line {
  display: block;
  opacity: 0;
  translate: 0 4px;
}

.cbk-07[data-state="done"] .cbk-07__line {
  animation: cbk-07-in .28s cubic-bezier(.2,.9,.25,1) forwards;
  animation-delay: calc(var(--i,0) * 60ms);
}

.cbk-07__line--dim {
  color: var(--muted);
}

@keyframes cbk-07-in {
  to {
    opacity: 1;
    translate: 0 0;
  }
}

.cbk-07 .tok-keyword {
  color: var(--tok-key);
}

.cbk-07 .tok-string {
  color: var(--tok-str);
}

.cbk-07 .tok-function {
  color: var(--tok-fn);
}

.cbk-07 .tok-variable {
  color: var(--tok-var);
}

.cbk-07 .tok-number {
  color: var(--tok-num);
}

.cbk-07 .tok-punct {
  color: var(--tok-punct);
}

.cbk-07 .tok-op {
  color: var(--tok-op);
}

.cbk-07 .tok-fn2 {
  color: var(--tok-fn2);
}

.cbk-07 :focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.cbk-07[data-theme="light"] {
  --bg: #f5f8f6;
  --surface: #ffffff;
  --bar: #f0f4f2;
  --out: #f7faf8;
  --line: #e1e7e3;
  --ink: #101319;
  --muted: #59616e;
  --acc: #0f9d63;
  --err: #c0392b;
  --tok-key: #8250df;
  --tok-str: #0a7d3f;
  --tok-fn: #0550ae;
  --tok-var: #8a5a00;
  --tok-num: #b1265c;
  --tok-punct: #57606a;
  --tok-op: #a2410a;
  --tok-fn2: #0f766e;
  background: radial-gradient(60rem 34rem at 50% -10%, #e4f5ec 0%, transparent 62%), var(--bg);
}

.cbk-07[data-theme="light"] .cbk-07__btn--run {
  color: #fff;
}

@media (prefers-color-scheme: light) {
  .cbk-07:not([data-theme="dark"]) {
    --bg: #f5f8f6;
    --surface: #ffffff;
    --bar: #f0f4f2;
    --out: #f7faf8;
    --line: #e1e7e3;
    --ink: #101319;
    --muted: #59616e;
    --acc: #0f9d63;
    --err: #c0392b;
    --tok-key: #8250df;
    --tok-str: #0a7d3f;
    --tok-fn: #0550ae;
    --tok-var: #8a5a00;
    --tok-num: #b1265c;
    --tok-punct: #57606a;
    --tok-op: #a2410a;
    --tok-fn2: #0f766e;
    background: radial-gradient(60rem 34rem at 50% -10%, #e4f5ec 0%, transparent 62%), var(--bg);
  }

  .cbk-07:not([data-theme="dark"]) .cbk-07__btn--run {
    color: #fff;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cbk-07 *,
    .cbk-07 *::before,
    .cbk-07 *::after {
    animation: none !important;
    transition: none !important;
  }

  .cbk-07[data-state="done"] .cbk-07__line {
    opacity: 1;
    translate: 0 0;
  }
}

@media (forced-colors: active) {
  .cbk-07__block {
    border: 2px solid CanvasText;
    background: Canvas;
  }

  .cbk-07__btn {
    border: 1px solid CanvasText;
    color: CanvasText;
    background: Canvas;
  }

  .cbk-07 [class^="tok-"] {
    color: CanvasText;
  }
}
/* theme toggle — pure CSS, :has() driven; :checked = light theme, top-right of the stage */

.cbk-07__stage {
  position: relative;
}

.cbk-07__tbox {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  padding: 0;
  opacity: 0;
  pointer-events: none;
}

.cbk-07__tbtn {
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
  .cbk-07__tbtn {
    background: color-mix(in srgb, var(--ink,#e7eaf3) 10%, transparent);
    border-color: color-mix(in srgb, var(--ink,#e7eaf3) 26%, transparent);
  }
}

.cbk-07__tbtn:hover {
  transform: translateY(-1px);
}

.cbk-07__tbtn svg {
  inline-size: 1.0625rem;
  block-size: 1.0625rem;
}

.cbk-07__tbox:focus-visible + .cbk-07__tbtn {
  outline: 2px solid var(--ink,#e7eaf3);
  outline-offset: 2px;
}

.cbk-07__tmoon {
  display: none;
}

.cbk-07:has(.cbk-07__tbox:checked) .cbk-07__tsun {
  display: none;
}

.cbk-07:has(.cbk-07__tbox:checked) .cbk-07__tmoon {
  display: block;
}

@media (prefers-reduced-motion: reduce) {
  .cbk-07__tbtn {
    transition: none;
  }

  .cbk-07__tbtn:hover {
    transform: none;
  }
}

@media (forced-colors: active) {
  .cbk-07__tbtn {
    border: 1px solid ButtonBorder;
    color: ButtonText;
    background: ButtonFace;
  }
}

.cbk-07:has(.cbk-07__tbox:checked) {
  --bg: #f5f8f6;
  --surface: #ffffff;
  --bar: #f0f4f2;
  --out: #f7faf8;
  --line: #e1e7e3;
  --ink: #101319;
  --muted: #59616e;
  --acc: #0f9d63;
  --err: #c0392b;
  --tok-key: #8250df;
  --tok-str: #0a7d3f;
  --tok-fn: #0550ae;
  --tok-var: #8a5a00;
  --tok-num: #b1265c;
  --tok-punct: #57606a;
  --tok-op: #a2410a;
  --tok-fn2: #0f766e;
  background: radial-gradient(60rem 34rem at 50% -10%, #e4f5ec 0%, transparent 62%), var(--bg);
}

.cbk-07:has(.cbk-07__tbox:checked) .cbk-07__btn--run {
  color: #fff;
}

.cbk-07__theme {
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

.cbk-07[data-theme="dark"] .cbk-07__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .cbk-07:not([data-theme="light"]) .cbk-07__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.cbk-07__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.cbk-07[data-theme="dark"] .cbk-07__theme:hover,
.cbk-07:not([data-theme="light"]) .cbk-07__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.cbk-07__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.cbk-07__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.cbk-07__sun {
  display: none;
}

.cbk-07__theme[aria-pressed="true"] .cbk-07__sun {
  display: block;
}

.cbk-07__theme[aria-pressed="true"] .cbk-07__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .cbk-07__theme {
    transition: none;
  }

  .cbk-07__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.getElementById('cbk-07-root');
  if (!root) return;
  const run = document.getElementById('cbk-07-run');
  const reset = document.getElementById('cbk-07-reset');
  const out = document.getElementById('cbk-07-out');
  let timer;

  const set = (s) => {
    root.dataset.state = s;
    run.disabled = s === 'running';
    reset.disabled = s !== 'done';
    out.setAttribute('aria-busy', String(s === 'running'));
  };

  run.addEventListener('click', () => {
    clearTimeout(timer);
    set('running');
    timer = setTimeout(() => set('done'), 420);
  });

  reset.addEventListener('click', () => {
    clearTimeout(timer);
    set('idle');
    run.focus();
  });
})();
(()=>{const r=document.querySelector('.cbk-07');if(!r)return;const t=r.querySelector('.cbk-07__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
