---
source: "codefronts"
url: "https://codefronts.com/snippets/css-code-blocks/diff-code-block-with-added-and-removed-line-highlighting/"
title: "Diff Code Block with Added and Removed Line Highlighting"
section: "snippets"
category: "css-code-blocks"
category_name: "CSS Code Blocks"
description: "A GitHub pull-request diff rebuilt as pure CSS: every line carries data-diff=\"add\", \"remove\" or \"context\" and attribute selectors do the rest — tinted row,…"
has_js: "true"
---

Here's a working CSS Code Block from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Diff Code Block with Added and Removed Line Highlighting
Source: https://codefronts.com/snippets/css-code-blocks/diff-code-block-with-added-and-removed-line-highlighting/

A GitHub pull-request diff rebuilt as pure CSS: every line carries data-diff="add", "remove" or "context" and attribute selectors do the rest — tinted row, +/- gutter, old/new line numbers from two counters, and an inline-end accent rail. The gutter markers are real role="img" elements with labels, so a screen reader announces "added line" instead of skipping the most important information on screen.
## HTML
```html
<div class="cbk-03">
  <button class="cbk-03__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="cbk-03__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="cbk-03__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <div class="cbk-03__stage">
    <input class="cbk-03__tbox" id="cbk-03-tbox" type="checkbox" data-alt="light" aria-label="Toggle light and dark theme">
    <label class="cbk-03__tbtn" for="cbk-03-tbox" title="Toggle light and dark theme">
      <svg class="cbk-03__tsun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4.2"></circle><path d="M12 2.4v2.3M12 19.3v2.3M2.4 12h2.3M19.3 12h2.3M5.2 5.2l1.6 1.6M17.2 17.2l1.6 1.6M18.8 5.2l-1.6 1.6M6.8 17.2l-1.6 1.6"></path></svg>
      <svg class="cbk-03__tmoon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.2 14.6A8.6 8.6 0 0 1 9.4 3.8a8.6 8.6 0 1 0 10.8 10.8Z"></path></svg>
    </label>
    <figure class="cbk-03__block">
      <figcaption class="cbk-03__bar">
        <svg class="cbk-03__branch" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="7" cy="6" r="2.4" stroke="currentColor" stroke-width="1.6"/><circle cx="7" cy="18" r="2.4" stroke="currentColor" stroke-width="1.6"/><circle cx="17" cy="9" r="2.4" stroke="currentColor" stroke-width="1.6"/><path d="M7 8.4v7.2M9.4 6.6h4.4a3.2 3.2 0 0 1 3.2 3.2v.4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
        <span class="cbk-03__path">src/lib/<b>rate-limit.ts</b></span>
        <span class="cbk-03__stat cbk-03__stat--add">+6</span>
        <span class="cbk-03__stat cbk-03__stat--rem">&minus;4</span>
        <span class="cbk-03__hunk">@@ &minus;41,10 +41,12 @@</span>
      </figcaption>
      <div class="cbk-03__scroll">
<pre class="cbk-03__pre"><code class="language-diff cbk-03__body"><span class="cbk-03__ln" data-diff="context"><span class="cbk-03__no cbk-03__no--old" aria-hidden="true"></span><span class="cbk-03__no cbk-03__no--new" aria-hidden="true"></span><span class="cbk-03__gut" role="img" aria-label="unchanged line"></span><span class="cbk-03__code"><span class="tok-keyword">export async function</span> <span class="tok-function">check</span><span class="tok-punct">(</span><span class="tok-variable">ip</span><span class="tok-punct">:</span> <span class="tok-fn2">string</span><span class="tok-punct">) {</span></span></span>
<span class="cbk-03__ln" data-diff="remove"><span class="cbk-03__no cbk-03__no--old" aria-hidden="true"></span><span class="cbk-03__no cbk-03__no--new" aria-hidden="true"></span><span class="cbk-03__gut" role="img" aria-label="removed line"></span><span class="cbk-03__code">  <span class="tok-keyword">const</span> <span class="tok-variable">hits</span> <span class="tok-op">=</span> <span class="tok-variable">memory</span><span class="tok-punct">.</span><span class="tok-function">get</span><span class="tok-punct">(</span><span class="tok-variable">ip</span><span class="tok-punct">) ??</span> <span class="tok-number">0</span><span class="tok-punct">;</span></span></span>
<span class="cbk-03__ln" data-diff="remove"><span class="cbk-03__no cbk-03__no--old" aria-hidden="true"></span><span class="cbk-03__no cbk-03__no--new" aria-hidden="true"></span><span class="cbk-03__gut" role="img" aria-label="removed line"></span><span class="cbk-03__code">  <span class="tok-keyword">if</span> <span class="tok-punct">(</span><span class="tok-variable">hits</span> <span class="tok-op">&gt;</span> <span class="tok-number">100</span><span class="tok-punct">)</span> <span class="tok-keyword">throw new</span> <span class="tok-function">Error</span><span class="tok-punct">(</span><span class="tok-string">'rate limited'</span><span class="tok-punct">);</span></span></span>
<span class="cbk-03__ln" data-diff="add"><span class="cbk-03__no cbk-03__no--old" aria-hidden="true"></span><span class="cbk-03__no cbk-03__no--new" aria-hidden="true"></span><span class="cbk-03__gut" role="img" aria-label="added line"></span><span class="cbk-03__code">  <span class="tok-keyword">const</span> <span class="tok-variable">key</span> <span class="tok-op">=</span> <span class="tok-string">'rl:'</span> <span class="tok-op">+</span> <span class="tok-function">hash</span><span class="tok-punct">(</span><span class="tok-variable">ip</span><span class="tok-punct">);</span></span></span>
<span class="cbk-03__ln" data-diff="add"><span class="cbk-03__no cbk-03__no--old" aria-hidden="true"></span><span class="cbk-03__no cbk-03__no--new" aria-hidden="true"></span><span class="cbk-03__gut" role="img" aria-label="added line"></span><span class="cbk-03__code">  <span class="tok-keyword">const</span> <span class="tok-variable">hits</span> <span class="tok-op">=</span> <span class="tok-keyword">await</span> <span class="tok-variable">redis</span><span class="tok-punct">.</span><span class="tok-function">incr</span><span class="tok-punct">(</span><span class="tok-variable">key</span><span class="tok-punct">);</span></span></span>
<span class="cbk-03__ln" data-diff="add"><span class="cbk-03__no cbk-03__no--old" aria-hidden="true"></span><span class="cbk-03__no cbk-03__no--new" aria-hidden="true"></span><span class="cbk-03__gut" role="img" aria-label="added line"></span><span class="cbk-03__code">  <span class="tok-keyword">if</span> <span class="tok-punct">(</span><span class="tok-variable">hits</span> <span class="tok-op">===</span> <span class="tok-number">1</span><span class="tok-punct">)</span> <span class="tok-keyword">await</span> <span class="tok-variable">redis</span><span class="tok-punct">.</span><span class="tok-function">expire</span><span class="tok-punct">(</span><span class="tok-variable">key</span><span class="tok-punct">,</span> <span class="tok-number">60</span><span class="tok-punct">);</span></span></span>
<span class="cbk-03__ln" data-diff="add"><span class="cbk-03__no cbk-03__no--old" aria-hidden="true"></span><span class="cbk-03__no cbk-03__no--new" aria-hidden="true"></span><span class="cbk-03__gut" role="img" aria-label="added line"></span><span class="cbk-03__code">  <span class="tok-keyword">if</span> <span class="tok-punct">(</span><span class="tok-variable">hits</span> <span class="tok-op">&gt;</span> <span class="tok-variable">LIMIT</span><span class="tok-punct">)</span> <span class="tok-keyword">throw new</span> <span class="tok-function">TooManyRequests</span><span class="tok-punct">(</span><span class="tok-variable">key</span><span class="tok-punct">);</span></span></span>
<span class="cbk-03__ln" data-diff="context"><span class="cbk-03__no cbk-03__no--old" aria-hidden="true"></span><span class="cbk-03__no cbk-03__no--new" aria-hidden="true"></span><span class="cbk-03__gut" role="img" aria-label="unchanged line"></span><span class="cbk-03__code"></span></span>
<span class="cbk-03__ln" data-diff="remove"><span class="cbk-03__no cbk-03__no--old" aria-hidden="true"></span><span class="cbk-03__no cbk-03__no--new" aria-hidden="true"></span><span class="cbk-03__gut" role="img" aria-label="removed line"></span><span class="cbk-03__code">  <span class="tok-variable">memory</span><span class="tok-punct">.</span><span class="tok-function">set</span><span class="tok-punct">(</span><span class="tok-variable">ip</span><span class="tok-punct">,</span> <span class="tok-variable">hits</span> <span class="tok-op">+</span> <span class="tok-number">1</span><span class="tok-punct">);</span></span></span>
<span class="cbk-03__ln" data-diff="remove"><span class="cbk-03__no cbk-03__no--old" aria-hidden="true"></span><span class="cbk-03__no cbk-03__no--new" aria-hidden="true"></span><span class="cbk-03__gut" role="img" aria-label="removed line"></span><span class="cbk-03__code">  <span class="tok-keyword">return</span> <span class="tok-punct">{</span> <span class="tok-variable">ok</span><span class="tok-punct">:</span> <span class="tok-keyword">true</span> <span class="tok-punct">};</span></span></span>
<span class="cbk-03__ln" data-diff="add"><span class="cbk-03__no cbk-03__no--old" aria-hidden="true"></span><span class="cbk-03__no cbk-03__no--new" aria-hidden="true"></span><span class="cbk-03__gut" role="img" aria-label="added line"></span><span class="cbk-03__code">  <span class="tok-keyword">return</span> <span class="tok-punct">{</span> <span class="tok-variable">ok</span><span class="tok-punct">:</span> <span class="tok-keyword">true</span><span class="tok-punct">,</span> <span class="tok-variable">remaining</span><span class="tok-punct">:</span> <span class="tok-variable">LIMIT</span> <span class="tok-op">-</span> <span class="tok-variable">hits</span> <span class="tok-punct">};</span></span></span>
<span class="cbk-03__ln" data-diff="context"><span class="cbk-03__no cbk-03__no--old" aria-hidden="true"></span><span class="cbk-03__no cbk-03__no--new" aria-hidden="true"></span><span class="cbk-03__gut" role="img" aria-label="unchanged line"></span><span class="cbk-03__code"><span class="tok-punct">}</span></span></span></code></pre>
      </div>
    </figure>
  </div>
</div>
```
## CSS
```css
.cbk-03 {
  inline-size: 100%;
  width: 100%;
  min-block-size: 100vh;
  min-block-size: 100svh;
  min-height: 100vh;
  display: block;
  --mono: ui-monospace,"JetBrains Mono","Geist Mono","SF Mono","IBM Plex Mono",Menlo,monospace;
  --sans: system-ui,"Inter","Geist",-apple-system,"Segoe UI",sans-serif;
  --bg: #07090d;
  --surface: #0d1017;
  --bar: #11141d;
  --line: #212533;
  --ink: #e6e9f2;
  --muted: #8f97a7;
  --add: #3fb950;
  --rem: #f85149;
  --gut: #171b25;
  --tok-key: #d2a8ff;
  --tok-str: #7ee787;
  --tok-fn: #79c0ff;
  --tok-var: #e6e9f2;
  --tok-num: #ff85a1;
  --tok-punct: #8b96a8;
  --tok-op: #ff9d6b;
  --tok-fn2: #ffcb6b;
  background: radial-gradient(64rem 36rem at 50% -10%, #151a28 0%, transparent 62%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
}

@supports (color: oklch(50% .1 200)) {
  .cbk-03 {
    --bg: oklch(12.5% .012 265);
    --surface: oklch(16.5% .014 265);
    --bar: oklch(19.5% .016 265);
    --line: oklch(27% .018 265);
    --ink: oklch(93% .008 265);
    --muted: oklch(69% .02 265);
    --add: oklch(72% .17 148);
    --rem: oklch(68% .19 22);
    --gut: oklch(20% .014 265);
  }
}

.cbk-03 *,
.cbk-03 *::before,
.cbk-03 *::after {
  box-sizing: border-box;
}

.cbk-03__stage {
  display: grid;
  place-items: center;
  min-block-size: inherit;
  padding: clamp(1rem,4vw,3.5rem);
}

.cbk-03__block {
  margin: 0;
  inline-size: min(66rem,100%);
  border: 1px solid var(--line);
  border-radius: 14px;
  background: var(--surface);
  overflow: hidden;
  box-shadow: 0 26px 64px -32px rgba(0,0,0,.9);
  container-type: inline-size;
}

.cbk-03__bar {
  display: flex;
  align-items: center;
  gap: .6rem;
  flex-wrap: wrap;
  padding: .7rem 1rem;
  border-block-end: 1px solid var(--line);
  background: var(--bar);
  font-size: .8125rem;
}

.cbk-03__branch {
  inline-size: 16px;
  block-size: 16px;
  color: var(--muted);
}

.cbk-03__path {
  font-family: var(--mono);
  color: var(--muted);
}

.cbk-03__path b {
  color: var(--ink);
  font-weight: 600;
}

.cbk-03__stat {
  padding: .15rem .45rem;
  border-radius: 6px;
  font-family: var(--mono);
  font-size: .75rem;
  font-weight: 600;
}

.cbk-03__stat--add {
  color: var(--add);
  background: rgba(63,185,80,.14);
  background: color-mix(in oklab,var(--add) 16%,transparent);
}

.cbk-03__stat--rem {
  color: var(--rem);
  background: rgba(248,81,73,.14);
  background: color-mix(in oklab,var(--rem) 16%,transparent);
}

.cbk-03__block:not(:has([data-diff="remove"])) .cbk-03__stat--rem {
  display: none;
}

.cbk-03__hunk {
  margin-inline-start: auto;
  font-family: var(--mono);
  font-size: .75rem;
  color: var(--muted);
  opacity: .8;
}

.cbk-03__scroll {
  overflow: auto;
  scrollbar-gutter: stable;
}

.cbk-03__pre {
  margin: 0;
  padding: .65rem 0 .8rem;
  font-family: var(--mono);
  font-size: clamp(.78125rem,.42rem + .5cqi,.9375rem);
  line-height: 1.7;
  white-space: pre;
  tab-size: 2;
  font-variant-ligatures: none;
}

.cbk-03__body {
  counter-reset: cbk03old 41 cbk03new 41;
  display: block;
  font: inherit;
}

.cbk-03__ln {
  display: block;
  counter-increment: cbk03old cbk03new;
  padding-inline-end: 1rem;
}

.cbk-03__ln[data-diff="add"] {
  counter-increment: cbk03new;
  background: rgba(63,185,80,.10);
  background: color-mix(in oklab,var(--add) 12%,transparent);
  box-shadow: inset 2px 0 0 var(--add);
}

.cbk-03__ln[data-diff="remove"] {
  counter-increment: cbk03old;
  background: rgba(248,81,73,.10);
  background: color-mix(in oklab,var(--rem) 12%,transparent);
  box-shadow: inset 2px 0 0 var(--rem);
}

.cbk-03__no {
  display: inline-block;
  inline-size: 3ch;
  padding-inline-end: .6rem;
  text-align: end;
  color: var(--muted);
  opacity: .55;
  font-variant-numeric: tabular-nums;
  user-select: none;
}

.cbk-03__no--old::before {
  content: counter(cbk03old);
}

.cbk-03__no--new::before {
  content: counter(cbk03new);
}

.cbk-03__ln[data-diff="add"] .cbk-03__no--old::before {
  content: "";
}

.cbk-03__ln[data-diff="remove"] .cbk-03__no--new::before {
  content: "";
}

.cbk-03__gut {
  display: inline-block;
  inline-size: 2ch;
  text-align: center;
  font-weight: 700;
  user-select: none;
}

.cbk-03__ln[data-diff="add"] .cbk-03__gut::after {
  content: "+";
  color: var(--add);
}

.cbk-03__ln[data-diff="remove"] .cbk-03__gut::after {
  content: "\2212";
  color: var(--rem);
}

.cbk-03__code {
  color: var(--ink);
}

.cbk-03 .tok-keyword {
  color: var(--tok-key);
}

.cbk-03 .tok-string {
  color: var(--tok-str);
}

.cbk-03 .tok-function {
  color: var(--tok-fn);
}

.cbk-03 .tok-variable {
  color: var(--tok-var);
}

.cbk-03 .tok-number {
  color: var(--tok-num);
}

.cbk-03 .tok-punct {
  color: var(--tok-punct);
}

.cbk-03 .tok-op {
  color: var(--tok-op);
}

.cbk-03 .tok-fn2 {
  color: var(--tok-fn2);
}

.cbk-03[data-theme="light"] {
  --bg: #f6f7fb;
  --surface: #ffffff;
  --bar: #f1f3f9;
  --line: #e2e5ef;
  --ink: #11131a;
  --muted: #5c6373;
  --add: #1a7f37;
  --rem: #cf222e;
  --gut: #f6f8fa;
  --tok-key: #8250df;
  --tok-str: #0a7d3f;
  --tok-fn: #0550ae;
  --tok-var: #11131a;
  --tok-num: #b1265c;
  --tok-punct: #57606a;
  --tok-op: #a2410a;
  --tok-fn2: #8a5a00;
  background: radial-gradient(64rem 36rem at 50% -10%, #e9edff 0%, transparent 62%), var(--bg);
}

@media (prefers-color-scheme: light) {
  .cbk-03:not([data-theme="dark"]) {
    --bg: #f6f7fb;
    --surface: #ffffff;
    --bar: #f1f3f9;
    --line: #e2e5ef;
    --ink: #11131a;
    --muted: #5c6373;
    --add: #1a7f37;
    --rem: #cf222e;
    --gut: #f6f8fa;
    --tok-key: #8250df;
    --tok-str: #0a7d3f;
    --tok-fn: #0550ae;
    --tok-var: #11131a;
    --tok-num: #b1265c;
    --tok-punct: #57606a;
    --tok-op: #a2410a;
    --tok-fn2: #8a5a00;
    background: radial-gradient(64rem 36rem at 50% -10%, #e9edff 0%, transparent 62%), var(--bg);
  }
}

@media (forced-colors: active) {
  .cbk-03__block {
    border: 2px solid CanvasText;
    background: Canvas;
  }

  .cbk-03__ln[data-diff] {
    background: Canvas;
  }

  .cbk-03__ln[data-diff="add"] {
    box-shadow: inset 3px 0 0 Highlight;
  }

  .cbk-03__ln[data-diff="remove"] {
    box-shadow: inset 3px 0 0 CanvasText;
  }

  .cbk-03 [class^="tok-"] {
    color: CanvasText;
  }
}
/* theme toggle — pure CSS, :has() driven; :checked = light theme, top-right of the stage */

.cbk-03__stage {
  position: relative;
}

.cbk-03__tbox {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  padding: 0;
  opacity: 0;
  pointer-events: none;
}

.cbk-03__tbtn {
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
  .cbk-03__tbtn {
    background: color-mix(in srgb, var(--ink,#e7eaf3) 10%, transparent);
    border-color: color-mix(in srgb, var(--ink,#e7eaf3) 26%, transparent);
  }
}

.cbk-03__tbtn:hover {
  transform: translateY(-1px);
}

.cbk-03__tbtn svg {
  inline-size: 1.0625rem;
  block-size: 1.0625rem;
}

.cbk-03__tbox:focus-visible + .cbk-03__tbtn {
  outline: 2px solid var(--ink,#e7eaf3);
  outline-offset: 2px;
}

.cbk-03__tmoon {
  display: none;
}

.cbk-03:has(.cbk-03__tbox:checked) .cbk-03__tsun {
  display: none;
}

.cbk-03:has(.cbk-03__tbox:checked) .cbk-03__tmoon {
  display: block;
}

@media (prefers-reduced-motion: reduce) {
  .cbk-03__tbtn {
    transition: none;
  }

  .cbk-03__tbtn:hover {
    transform: none;
  }
}

@media (forced-colors: active) {
  .cbk-03__tbtn {
    border: 1px solid ButtonBorder;
    color: ButtonText;
    background: ButtonFace;
  }
}

.cbk-03:has(.cbk-03__tbox:checked) {
  --bg: #f6f7fb;
  --surface: #ffffff;
  --bar: #f1f3f9;
  --line: #e2e5ef;
  --ink: #11131a;
  --muted: #5c6373;
  --add: #1a7f37;
  --rem: #cf222e;
  --gut: #f6f8fa;
  --tok-key: #8250df;
  --tok-str: #0a7d3f;
  --tok-fn: #0550ae;
  --tok-var: #11131a;
  --tok-num: #b1265c;
  --tok-punct: #57606a;
  --tok-op: #a2410a;
  --tok-fn2: #8a5a00;
  background: radial-gradient(64rem 36rem at 50% -10%, #e9edff 0%, transparent 62%), var(--bg);
}

.cbk-03__theme {
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

.cbk-03[data-theme="dark"] .cbk-03__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .cbk-03:not([data-theme="light"]) .cbk-03__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.cbk-03__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.cbk-03[data-theme="dark"] .cbk-03__theme:hover,
.cbk-03:not([data-theme="light"]) .cbk-03__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.cbk-03__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.cbk-03__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.cbk-03__sun {
  display: none;
}

.cbk-03__theme[aria-pressed="true"] .cbk-03__sun {
  display: block;
}

.cbk-03__theme[aria-pressed="true"] .cbk-03__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .cbk-03__theme {
    transition: none;
  }

  .cbk-03__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(()=>{const r=document.querySelector('.cbk-03');if(!r)return;const t=r.querySelector('.cbk-03__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
