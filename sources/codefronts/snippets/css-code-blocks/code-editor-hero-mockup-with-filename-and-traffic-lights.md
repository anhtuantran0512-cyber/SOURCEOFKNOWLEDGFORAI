---
source: "codefronts"
url: "https://codefronts.com/snippets/css-code-blocks/code-editor-hero-mockup-with-filename-and-traffic-lights/"
title: "Code Editor Hero Mockup with Filename and Traffic Lights"
section: "snippets"
category: "css-code-blocks"
category_name: "CSS Code Blocks"
description: "The centrepiece every developer-tool landing page needs: a full editor window mockup at hero scale — macOS traffic lights, an active filename tab, a…"
has_js: "true"
---

Here's a working CSS Code Block from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Code Editor Hero Mockup with Filename and Traffic Lights
Source: https://codefronts.com/snippets/css-code-blocks/code-editor-hero-mockup-with-filename-and-traffic-lights/

The centrepiece every developer-tool landing page needs: a full editor window mockup at hero scale — macOS traffic lights, an active filename tab, a line-number gutter, a status bar with branch and cursor position, a blinking caret and a slow @property conic-gradient border that breathes light around the frame. Pure CSS, no screenshot, so it stays crisp at any resolution and re-themes with your brand in one variable.
## HTML
```html
<div class="cbk-04">
  <button class="cbk-04__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="cbk-04__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="cbk-04__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <div class="cbk-04__stage">
    <input class="cbk-04__tbox" id="cbk-04-tbox" type="checkbox" data-alt="light" aria-label="Toggle light and dark theme">
    <label class="cbk-04__tbtn" for="cbk-04-tbox" title="Toggle light and dark theme">
      <svg class="cbk-04__tsun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4.2"></circle><path d="M12 2.4v2.3M12 19.3v2.3M2.4 12h2.3M19.3 12h2.3M5.2 5.2l1.6 1.6M17.2 17.2l1.6 1.6M18.8 5.2l-1.6 1.6M6.8 17.2l-1.6 1.6"></path></svg>
      <svg class="cbk-04__tmoon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.2 14.6A8.6 8.6 0 0 1 9.4 3.8a8.6 8.6 0 1 0 10.8 10.8Z"></path></svg>
    </label>
    <div class="cbk-04__frame">
      <span class="cbk-04__bloom" aria-hidden="true"></span>
      <figure class="cbk-04__win">
        <figcaption class="cbk-04__chrome">
          <span class="cbk-04__lights" aria-hidden="true"><i></i><i></i><i></i></span>
          <span class="cbk-04__tab">
            <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4 4h16v16H4z" fill="currentColor" opacity=".18"/><path d="M7.5 9h9M12 9v7" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
            Component.tsx
            <b class="cbk-04__mod" aria-label="unsaved changes" role="img"></b>
          </span>
          <span class="cbk-04__tab cbk-04__tab--idle">use-toast.ts</span>
          <span class="cbk-04__meta">TypeScript React</span>
        </figcaption>

        <div class="cbk-04__body">
<pre class="cbk-04__pre"><code class="language-tsx cbk-04__code"><span class="cbk-04__l"><span class="tok-keyword">import</span> <span class="tok-punct">{</span> <span class="tok-variable">motion</span> <span class="tok-punct">}</span> <span class="tok-keyword">from</span> <span class="tok-string">'framer-motion'</span><span class="tok-punct">;</span></span>
<span class="cbk-04__l"><span class="tok-keyword">import</span> <span class="tok-punct">{</span> <span class="tok-variable">useToast</span> <span class="tok-punct">}</span> <span class="tok-keyword">from</span> <span class="tok-string">'./use-toast'</span><span class="tok-punct">;</span></span>
<span class="cbk-04__l"></span>
<span class="cbk-04__l"><span class="tok-keyword">type</span> <span class="tok-fn2">Props</span> <span class="tok-op">=</span> <span class="tok-punct">{</span> <span class="tok-variable">label</span><span class="tok-punct">:</span> <span class="tok-fn2">string</span><span class="tok-punct">;</span> <span class="tok-variable">tone</span><span class="tok-punct">?:</span> <span class="tok-string">'brand'</span> <span class="tok-op">|</span> <span class="tok-string">'ghost'</span> <span class="tok-punct">};</span></span>
<span class="cbk-04__l"></span>
<span class="cbk-04__l"><span class="tok-keyword">export function</span> <span class="tok-function">SaveButton</span><span class="tok-punct">({</span> <span class="tok-variable">label</span><span class="tok-punct">,</span> <span class="tok-variable">tone</span> <span class="tok-op">=</span> <span class="tok-string">'brand'</span> <span class="tok-punct">}:</span> <span class="tok-fn2">Props</span><span class="tok-punct">) {</span></span>
<span class="cbk-04__l">  <span class="tok-keyword">const</span> <span class="tok-punct">{</span> <span class="tok-variable">notify</span> <span class="tok-punct">} =</span> <span class="tok-function">useToast</span><span class="tok-punct">();</span></span>
<span class="cbk-04__l"></span>
<span class="cbk-04__l">  <span class="tok-keyword">return</span> <span class="tok-punct">(</span></span>
<span class="cbk-04__l">    <span class="tok-punct">&lt;</span><span class="tok-function">motion.button</span></span>
<span class="cbk-04__l">      <span class="tok-variable">whileTap</span><span class="tok-punct">={{</span> <span class="tok-variable">scale</span><span class="tok-punct">:</span> <span class="tok-number">0.97</span> <span class="tok-punct">}}</span></span>
<span class="cbk-04__l">      <span class="tok-variable">data-tone</span><span class="tok-punct">={</span><span class="tok-variable">tone</span><span class="tok-punct">}</span></span>
<span class="cbk-04__l">      <span class="tok-variable">onClick</span><span class="tok-punct">={() =&gt;</span> <span class="tok-function">notify</span><span class="tok-punct">(</span><span class="tok-string">'Changes saved'</span><span class="tok-punct">)}</span></span>
<span class="cbk-04__l">    <span class="tok-punct">&gt;</span></span>
<span class="cbk-04__l">      <span class="tok-punct">{</span><span class="tok-variable">label</span><span class="tok-punct">}</span><span class="cbk-04__caret" aria-hidden="true"></span></span>
<span class="cbk-04__l">    <span class="tok-punct">&lt;/</span><span class="tok-function">motion.button</span><span class="tok-punct">&gt;</span></span>
<span class="cbk-04__l">  <span class="tok-punct">);</span></span>
<span class="cbk-04__l"><span class="tok-punct">}</span></span></code></pre>
        </div>

        <div class="cbk-04__status">
          <span class="cbk-04__st">
            <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="7" cy="6" r="2.2" stroke="currentColor" stroke-width="1.7"/><circle cx="7" cy="18" r="2.2" stroke="currentColor" stroke-width="1.7"/><circle cx="17" cy="9" r="2.2" stroke="currentColor" stroke-width="1.7"/><path d="M7 8.2v7.6M9.2 6.6h4.6A3 3 0 0 1 16.8 9.6v.2" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
            feat/save-button
          </span>
          <span class="cbk-04__st cbk-04__st--ok">
            <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="m5 12.5 4.2 4.2L19 7" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
            tsc &mdash; 0 errors
          </span>
          <span class="cbk-04__st cbk-04__st--end">Ln 14, Col 32</span>
          <span class="cbk-04__st">Spaces: 2</span>
          <span class="cbk-04__st">UTF-8</span>
        </div>
      </figure>
    </div>
  </div>
</div>
```
## CSS
```css
@property --cbk-04-a {
  syntax: "<angle>";
  inherits: false;
  initial-value: 0deg;
}

.cbk-04 {
  inline-size: 100%;
  width: 100%;
  min-block-size: 100vh;
  min-block-size: 100svh;
  min-height: 100vh;
  display: block;
  --mono: ui-monospace,"JetBrains Mono","Geist Mono","SF Mono","IBM Plex Mono",Menlo,monospace;
  --sans: system-ui,"Inter","Geist",-apple-system,"Segoe UI",sans-serif;
  --bg: #050609;
  --surface: #0c0e15;
  --chrome: #101320;
  --line: #1e2231;
  --ink: #e9ecf5;
  --muted: #8b93a5;
  --acc: #8b7cff;
  --acc2: #22d3ee;
  --ok: #3fb950;
  --tok-key: #d2a8ff;
  --tok-str: #7ee787;
  --tok-fn: #79c0ff;
  --tok-var: #ffcb6b;
  --tok-num: #ff85a1;
  --tok-punct: #8b96a8;
  --tok-op: #ff9d6b;
  --tok-fn2: #5eead4;
  background: radial-gradient(80rem 46rem at 50% -20%, #16182c 0%, transparent 60%), radial-gradient(40rem 30rem at 85% 110%, #101c2a 0%, transparent 70%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
}

@supports (color: oklch(50% .1 200)) {
  .cbk-04 {
    --bg: oklch(10% .012 275);
    --surface: oklch(15% .014 275);
    --chrome: oklch(18% .018 275);
    --line: oklch(25% .02 275);
    --ink: oklch(94% .008 275);
    --muted: oklch(68% .02 275);
    --acc: oklch(70% .18 292);
    --acc2: oklch(82% .13 200);
  }
}

.cbk-04 *,
.cbk-04 *::before,
.cbk-04 *::after {
  box-sizing: border-box;
}

.cbk-04__stage {
  display: grid;
  place-items: center;
  min-block-size: inherit;
  padding: clamp(1rem,5vw,4rem);
}

.cbk-04__frame {
  position: relative;
  inline-size: min(78rem,100%);
  container-type: inline-size;
}

.cbk-04__bloom {
  position: absolute;
  inset: 8% 6% -6%;
  border-radius: 40px;
  opacity: .4;
  filter: blur(58px);
  background: radial-gradient(50% 60% at 22% 30%, var(--acc) 0%, transparent 70%), radial-gradient(46% 60% at 78% 70%, var(--acc2) 0%, transparent 72%);
  pointer-events: none;
}

.cbk-04__win {
  position: relative;
  margin: 0;
  border: 1px solid transparent;
  border-radius: 18px;
  overflow: hidden;
  background: linear-gradient(var(--surface),var(--surface)) padding-box, conic-gradient(from 210deg, color-mix(in oklab,var(--acc) 80%,transparent), color-mix(in oklab,var(--acc2) 70%,transparent) 30%, transparent 56%, color-mix(in oklab,var(--acc) 80%,transparent)) border-box;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.07), 0 40px 100px -40px rgba(0,0,0,.92);
}

@supports at-rule(@property) {
  .cbk-04__win {
    background: linear-gradient(var(--surface),var(--surface)) padding-box, conic-gradient(from var(--cbk-04-a), color-mix(in oklab,var(--acc) 85%,transparent), color-mix(in oklab,var(--acc2) 75%,transparent) 30%, transparent 56%, color-mix(in oklab,var(--acc) 85%,transparent)) border-box;
    animation: cbk-04-spin 12s linear infinite;
  }
}

@keyframes cbk-04-spin {
  to {
    --cbk-04-a: 360deg;
  }
}

.cbk-04__chrome {
  display: flex;
  align-items: center;
  gap: .75rem;
  padding: .6rem .9rem;
  background: var(--chrome);
  border-block-end: 1px solid var(--line);
}

.cbk-04__lights {
  display: flex;
  gap: .45rem;
  padding-inline-end: .35rem;
}

.cbk-04__lights i {
  inline-size: 11px;
  block-size: 11px;
  border-radius: 50%;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.35), 0 0 0 .5px rgba(0,0,0,.35);
}

.cbk-04__lights i:nth-child(1) {
  background: #ff5f57;
}

.cbk-04__lights i:nth-child(2) {
  background: #febc2e;
}

.cbk-04__lights i:nth-child(3) {
  background: #28c840;
}

.cbk-04__tab {
  display: inline-flex;
  align-items: center;
  gap: .45rem;
  padding: .4rem .7rem;
  border-radius: 8px;
  background: color-mix(in oklab,var(--ink) 8%,transparent);
  color: var(--ink);
  font-family: var(--mono);
  font-size: .8125rem;
}

.cbk-04__tab svg {
  inline-size: 14px;
  block-size: 14px;
  color: var(--tok-fn);
}

.cbk-04__tab--idle {
  background: none;
  color: var(--muted);
}

.cbk-04__mod {
  inline-size: 6px;
  block-size: 6px;
  border-radius: 50%;
  background: var(--acc);
  display: inline-block;
}

.cbk-04__meta {
  margin-inline-start: auto;
  color: var(--muted);
  font-size: .75rem;
  letter-spacing: .02em;
}

.cbk-04__body {
  background: var(--surface);
}

.cbk-04__pre {
  margin: 0;
  padding: 1.35rem 1.5rem 1.6rem 0;
  overflow-x: auto;
  scrollbar-gutter: stable;
  font-family: var(--mono);
  font-size: clamp(.8125rem,.5rem + .55cqi,1.0625rem);
  line-height: 1.85;
  white-space: pre;
  tab-size: 2;
  font-variant-ligatures: none;
}

.cbk-04__code {
  counter-reset: cbk04;
  font: inherit;
  display: block;
}

.cbk-04__l {
  display: block;
  counter-increment: cbk04;
  padding-inline-start: 1rem;
}

.cbk-04__l::before {
  content: counter(cbk04);
  display: inline-block;
  inline-size: 3.2ch;
  margin-inline-end: 1.5rem;
  text-align: end;
  color: var(--muted);
  opacity: .42;
  user-select: none;
  font-variant-numeric: tabular-nums;
}

.cbk-04__l:hover {
  background: color-mix(in oklab,var(--ink) 4%,transparent);
}

.cbk-04__caret {
  display: inline-block;
  inline-size: 2px;
  block-size: 1.15em;
  margin-inline-start: 1px;
  vertical-align: text-bottom;
  background: var(--acc2);
  animation: cbk-04-blink 1.1s steps(1,end) infinite;
}

@keyframes cbk-04-blink {
  0%,
    49% {
    opacity: 1;
  }

  50%,
    100% {
    opacity: 0;
  }
}

.cbk-04__status {
  display: flex;
  align-items: center;
  gap: 1.1rem;
  flex-wrap: wrap;
  padding: .5rem .95rem;
  border-block-start: 1px solid var(--line);
  background: var(--chrome);
  color: var(--muted);
  font-size: .71875rem;
  font-family: var(--mono);
}

.cbk-04__st {
  display: inline-flex;
  align-items: center;
  gap: .35rem;
}

.cbk-04__st svg {
  inline-size: 13px;
  block-size: 13px;
}

.cbk-04__st--ok {
  color: var(--ok);
}

.cbk-04__st--end {
  margin-inline-start: auto;
}

.cbk-04 .tok-keyword {
  color: var(--tok-key);
}

.cbk-04 .tok-string {
  color: var(--tok-str);
}

.cbk-04 .tok-function {
  color: var(--tok-fn);
}

.cbk-04 .tok-variable {
  color: var(--tok-var);
}

.cbk-04 .tok-number {
  color: var(--tok-num);
}

.cbk-04 .tok-punct {
  color: var(--tok-punct);
}

.cbk-04 .tok-op {
  color: var(--tok-op);
}

.cbk-04 .tok-fn2 {
  color: var(--tok-fn2);
}

.cbk-04[data-theme="light"] {
  --bg: #f4f5fa;
  --surface: #ffffff;
  --chrome: #f0f2f8;
  --line: #e2e5ef;
  --ink: #101219;
  --muted: #5b6272;
  --acc: #6d5efc;
  --acc2: #0891b2;
  --ok: #1a7f37;
  --tok-key: #8250df;
  --tok-str: #0a7d3f;
  --tok-fn: #0550ae;
  --tok-var: #8a5a00;
  --tok-num: #b1265c;
  --tok-punct: #57606a;
  --tok-op: #a2410a;
  --tok-fn2: #0f766e;
  background: radial-gradient(80rem 46rem at 50% -20%, #e7eaff 0%, transparent 60%), var(--bg);
}

.cbk-04[data-theme="light"] .cbk-04__bloom {
  opacity: .28;
}

.cbk-04[data-theme="light"] .cbk-04__win {
  box-shadow: inset 0 1px 0 #fff, 0 30px 70px -40px rgba(20,24,48,.5);
}

@media (prefers-color-scheme: light) {
  .cbk-04:not([data-theme="dark"]) {
    --bg: #f4f5fa;
    --surface: #ffffff;
    --chrome: #f0f2f8;
    --line: #e2e5ef;
    --ink: #101219;
    --muted: #5b6272;
    --acc: #6d5efc;
    --acc2: #0891b2;
    --ok: #1a7f37;
    --tok-key: #8250df;
    --tok-str: #0a7d3f;
    --tok-fn: #0550ae;
    --tok-var: #8a5a00;
    --tok-num: #b1265c;
    --tok-punct: #57606a;
    --tok-op: #a2410a;
    --tok-fn2: #0f766e;
    background: radial-gradient(80rem 46rem at 50% -20%, #e7eaff 0%, transparent 60%), var(--bg);
  }

  .cbk-04:not([data-theme="dark"]) .cbk-04__bloom {
    opacity: .28;
  }

  .cbk-04:not([data-theme="dark"]) .cbk-04__win {
    box-shadow: inset 0 1px 0 #fff, 0 30px 70px -40px rgba(20,24,48,.5);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cbk-04 *,
    .cbk-04 *::before,
    .cbk-04 *::after {
    animation: none !important;
    transition: none !important;
  }

  .cbk-04__caret {
    opacity: 1;
  }
}

@media (forced-colors: active) {
  .cbk-04__win {
    border: 2px solid CanvasText;
    background: Canvas;
  }

  .cbk-04__bloom {
    display: none;
  }

  .cbk-04 [class^="tok-"] {
    color: CanvasText;
  }
}
/* theme toggle — pure CSS, :has() driven; :checked = light theme, top-right of the stage */

.cbk-04__stage {
  position: relative;
}

.cbk-04__tbox {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  padding: 0;
  opacity: 0;
  pointer-events: none;
}

.cbk-04__tbtn {
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
  .cbk-04__tbtn {
    background: color-mix(in srgb, var(--ink,#e7eaf3) 10%, transparent);
    border-color: color-mix(in srgb, var(--ink,#e7eaf3) 26%, transparent);
  }
}

.cbk-04__tbtn:hover {
  transform: translateY(-1px);
}

.cbk-04__tbtn svg {
  inline-size: 1.0625rem;
  block-size: 1.0625rem;
}

.cbk-04__tbox:focus-visible + .cbk-04__tbtn {
  outline: 2px solid var(--ink,#e7eaf3);
  outline-offset: 2px;
}

.cbk-04__tmoon {
  display: none;
}

.cbk-04:has(.cbk-04__tbox:checked) .cbk-04__tsun {
  display: none;
}

.cbk-04:has(.cbk-04__tbox:checked) .cbk-04__tmoon {
  display: block;
}

@media (prefers-reduced-motion: reduce) {
  .cbk-04__tbtn {
    transition: none;
  }

  .cbk-04__tbtn:hover {
    transform: none;
  }
}

@media (forced-colors: active) {
  .cbk-04__tbtn {
    border: 1px solid ButtonBorder;
    color: ButtonText;
    background: ButtonFace;
  }
}

.cbk-04:has(.cbk-04__tbox:checked) {
  --bg: #f4f5fa;
  --surface: #ffffff;
  --chrome: #f0f2f8;
  --line: #e2e5ef;
  --ink: #101219;
  --muted: #5b6272;
  --acc: #6d5efc;
  --acc2: #0891b2;
  --ok: #1a7f37;
  --tok-key: #8250df;
  --tok-str: #0a7d3f;
  --tok-fn: #0550ae;
  --tok-var: #8a5a00;
  --tok-num: #b1265c;
  --tok-punct: #57606a;
  --tok-op: #a2410a;
  --tok-fn2: #0f766e;
  background: radial-gradient(80rem 46rem at 50% -20%, #e7eaff 0%, transparent 60%), var(--bg);
}

.cbk-04:has(.cbk-04__tbox:checked) .cbk-04__bloom {
  opacity: .28;
}

.cbk-04:has(.cbk-04__tbox:checked) .cbk-04__win {
  box-shadow: inset 0 1px 0 #fff, 0 30px 70px -40px rgba(20,24,48,.5);
}

.cbk-04__theme {
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

.cbk-04[data-theme="dark"] .cbk-04__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .cbk-04:not([data-theme="light"]) .cbk-04__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.cbk-04__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.cbk-04[data-theme="dark"] .cbk-04__theme:hover,
.cbk-04:not([data-theme="light"]) .cbk-04__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.cbk-04__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.cbk-04__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.cbk-04__sun {
  display: none;
}

.cbk-04__theme[aria-pressed="true"] .cbk-04__sun {
  display: block;
}

.cbk-04__theme[aria-pressed="true"] .cbk-04__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .cbk-04__theme {
    transition: none;
  }

  .cbk-04__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(()=>{const r=document.querySelector('.cbk-04');if(!r)return;const t=r.querySelector('.cbk-04__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
