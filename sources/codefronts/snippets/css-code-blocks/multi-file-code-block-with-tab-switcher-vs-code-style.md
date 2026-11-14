---
source: "codefronts"
url: "https://codefronts.com/snippets/css-code-blocks/multi-file-code-block-with-tab-switcher-vs-code-style/"
title: "Multi-File Code Block with Tab Switcher (VS Code Style)"
section: "snippets"
category: "css-code-blocks"
category_name: "CSS Code Blocks"
description: "The tabbed file switcher every framework doc ships — VS Code chrome with an active-tab underline, muted inactive tabs, a hover close-X, and a panel swap in…"
has_js: "true"
---

Here's a working CSS Code Block from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Multi-File Code Block with Tab Switcher (VS Code Style)
Source: https://codefronts.com/snippets/css-code-blocks/multi-file-code-block-with-tab-switcher-vs-code-style/

The tabbed file switcher every framework doc ships — VS Code chrome with an active-tab underline, muted inactive tabs, a hover close-X, and a panel swap in under 30 lines of vanilla JS. Wired as a real role="tablist" with roving tabindex, so arrow keys, Home/End and screen readers all behave the way the ARIA Authoring Practices say a tab set should.
## HTML
```html
<div class="cbk-02">
  <button class="cbk-02__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="cbk-02__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="cbk-02__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <div class="cbk-02__stage">
    <input class="cbk-02__tbox" id="cbk-02-tbox" type="checkbox" data-alt="light" aria-label="Toggle light and dark theme">
    <label class="cbk-02__tbtn" for="cbk-02-tbox" title="Toggle light and dark theme">
      <svg class="cbk-02__tsun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4.2"></circle><path d="M12 2.4v2.3M12 19.3v2.3M2.4 12h2.3M19.3 12h2.3M5.2 5.2l1.6 1.6M17.2 17.2l1.6 1.6M18.8 5.2l-1.6 1.6M6.8 17.2l-1.6 1.6"></path></svg>
      <svg class="cbk-02__tmoon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.2 14.6A8.6 8.6 0 0 1 9.4 3.8a8.6 8.6 0 1 0 10.8 10.8Z"></path></svg>
    </label>
    <div class="cbk-02__block" id="cbk-02-block">
      <div class="cbk-02__strip" role="tablist" aria-label="Project files">
        <span class="cbk-02__tabwrap">
          <button class="cbk-02__tab" type="button" role="tab" id="cbk-02-t0" aria-controls="cbk-02-p0" aria-selected="true" tabindex="0">
            <svg class="cbk-02__ext cbk-02__ext--tsx" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 4h16v16H4z" fill="currentColor" opacity=".16"/><path d="M7.5 9h9M12 9v7" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
            App.tsx
          </button>
          <button class="cbk-02__close" type="button" tabindex="-1" aria-label="Close App.tsx">
            <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M7 7l10 10M17 7 7 17" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
          </button>
        </span>
        <span class="cbk-02__tabwrap">
          <button class="cbk-02__tab" type="button" role="tab" id="cbk-02-t1" aria-controls="cbk-02-p1" aria-selected="false" tabindex="-1">
            <svg class="cbk-02__ext cbk-02__ext--css" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 4h16v16H4z" fill="currentColor" opacity=".16"/><path d="M8 15.5c.9.9 2.2 1.2 3.4.8M16 8.5c-.9-.9-2.2-1.2-3.4-.8" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
            theme.css
          </button>
          <button class="cbk-02__close" type="button" tabindex="-1" aria-label="Close theme.css">
            <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M7 7l10 10M17 7 7 17" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
          </button>
        </span>
        <span class="cbk-02__tabwrap">
          <button class="cbk-02__tab" type="button" role="tab" id="cbk-02-t2" aria-controls="cbk-02-p2" aria-selected="false" tabindex="-1">
            <svg class="cbk-02__ext cbk-02__ext--json" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 4h16v16H4z" fill="currentColor" opacity=".16"/><path d="M10 8.5c-1.6 0-1.6 3.5-3 3.5 1.4 0 1.4 3.5 3 3.5m4-7c1.6 0 1.6 3.5 3 3.5-1.4 0-1.4 3.5-3 3.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
            package.json
          </button>
          <button class="cbk-02__close" type="button" tabindex="-1" aria-label="Close package.json">
            <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M7 7l10 10M17 7 7 17" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
          </button>
        </span>
        <span class="cbk-02__tabwrap">
          <button class="cbk-02__tab" type="button" role="tab" id="cbk-02-t3" aria-controls="cbk-02-p3" aria-selected="false" tabindex="-1">
            <svg class="cbk-02__ext cbk-02__ext--md" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 4h16v16H4z" fill="currentColor" opacity=".16"/><path d="M7 15V9l2.5 3L12 9v6m3.5-6v6m0 0 2-2m-2 2-2-2" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
            README.md
          </button>
          <button class="cbk-02__close" type="button" tabindex="-1" aria-label="Close README.md">
            <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M7 7l10 10M17 7 7 17" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
          </button>
        </span>
      </div>

      <section class="cbk-02__panel" role="tabpanel" id="cbk-02-p0" aria-labelledby="cbk-02-t0" tabindex="0">
<pre class="cbk-02__pre"><code class="language-tsx"><span class="tok-keyword">import</span> <span class="tok-punct">{</span> <span class="tok-variable">useQuery</span> <span class="tok-punct">}</span> <span class="tok-keyword">from</span> <span class="tok-string">'@tanstack/react-query'</span><span class="tok-punct">;</span>
<span class="tok-keyword">import</span> <span class="tok-punct">{</span> <span class="tok-function">Board</span> <span class="tok-punct">}</span> <span class="tok-keyword">from</span> <span class="tok-string">'./Board'</span><span class="tok-punct">;</span>

<span class="tok-keyword">export default function</span> <span class="tok-function">App</span><span class="tok-punct">() {</span>
  <span class="tok-keyword">const</span> <span class="tok-punct">{</span> <span class="tok-variable">data</span><span class="tok-punct">,</span> <span class="tok-variable">isPending</span> <span class="tok-punct">} =</span> <span class="tok-function">useQuery</span><span class="tok-punct">({</span>
    <span class="tok-variable">queryKey</span><span class="tok-punct">: [</span><span class="tok-string">'issues'</span><span class="tok-punct">],</span>
    <span class="tok-variable">queryFn</span><span class="tok-punct">: () =&gt;</span> <span class="tok-function">fetch</span><span class="tok-punct">(</span><span class="tok-string">'/api/issues'</span><span class="tok-punct">).</span><span class="tok-function">then</span><span class="tok-punct">((</span><span class="tok-variable">r</span><span class="tok-punct">) =&gt;</span> <span class="tok-variable">r</span><span class="tok-punct">.</span><span class="tok-function">json</span><span class="tok-punct">()),</span>
  <span class="tok-punct">});</span>

  <span class="tok-keyword">if</span> <span class="tok-punct">(</span><span class="tok-variable">isPending</span><span class="tok-punct">)</span> <span class="tok-keyword">return</span> <span class="tok-punct">&lt;</span><span class="tok-function">Board.Skeleton</span> <span class="tok-punct">/&gt;;</span>
  <span class="tok-keyword">return</span> <span class="tok-punct">&lt;</span><span class="tok-function">Board</span> <span class="tok-variable">issues</span><span class="tok-punct">={</span><span class="tok-variable">data</span><span class="tok-punct">} /&gt;;</span>
<span class="tok-punct">}</span></code></pre>
      </section>

      <section class="cbk-02__panel" role="tabpanel" id="cbk-02-p1" aria-labelledby="cbk-02-t1" tabindex="0" hidden>
<pre class="cbk-02__pre"><code class="language-css"><span class="tok-comment">/* Design tokens — one scale, both themes. */</span>
<span class="tok-function">:root</span> <span class="tok-punct">{</span>
  <span class="tok-variable">--surface</span><span class="tok-punct">:</span> <span class="tok-function">oklch</span><span class="tok-punct">(</span><span class="tok-number">17%</span> <span class="tok-number">.015</span> <span class="tok-number">265</span><span class="tok-punct">);</span>
  <span class="tok-variable">--ink</span><span class="tok-punct">:</span> <span class="tok-function">oklch</span><span class="tok-punct">(</span><span class="tok-number">93%</span> <span class="tok-number">.008</span> <span class="tok-number">265</span><span class="tok-punct">);</span>
  <span class="tok-variable">--accent</span><span class="tok-punct">:</span> <span class="tok-function">oklch</span><span class="tok-punct">(</span><span class="tok-number">74%</span> <span class="tok-number">.16</span> <span class="tok-number">300</span><span class="tok-punct">);</span>
  <span class="tok-variable">--radius</span><span class="tok-punct">:</span> <span class="tok-number">14px</span><span class="tok-punct">;</span>
<span class="tok-punct">}</span>

<span class="tok-keyword">@media</span> <span class="tok-punct">(</span><span class="tok-variable">prefers-color-scheme</span><span class="tok-punct">:</span> light<span class="tok-punct">) {</span>
  <span class="tok-function">:root</span> <span class="tok-punct">{</span> <span class="tok-variable">--surface</span><span class="tok-punct">:</span> <span class="tok-function">oklch</span><span class="tok-punct">(</span><span class="tok-number">99%</span> <span class="tok-number">0</span> <span class="tok-number">0</span><span class="tok-punct">); }</span>
<span class="tok-punct">}</span></code></pre>
      </section>

      <section class="cbk-02__panel" role="tabpanel" id="cbk-02-p2" aria-labelledby="cbk-02-t2" tabindex="0" hidden>
<pre class="cbk-02__pre"><code class="language-json"><span class="tok-punct">{</span>
  <span class="tok-variable">"name"</span><span class="tok-punct">:</span> <span class="tok-string">"@codefronts/board"</span><span class="tok-punct">,</span>
  <span class="tok-variable">"type"</span><span class="tok-punct">:</span> <span class="tok-string">"module"</span><span class="tok-punct">,</span>
  <span class="tok-variable">"scripts"</span><span class="tok-punct">: {</span>
    <span class="tok-variable">"dev"</span><span class="tok-punct">:</span> <span class="tok-string">"vite"</span><span class="tok-punct">,</span>
    <span class="tok-variable">"test"</span><span class="tok-punct">:</span> <span class="tok-string">"vitest --coverage"</span>
  <span class="tok-punct">},</span>
  <span class="tok-variable">"dependencies"</span><span class="tok-punct">: {</span>
    <span class="tok-variable">"@tanstack/react-query"</span><span class="tok-punct">:</span> <span class="tok-string">"^5.62.0"</span><span class="tok-punct">,</span>
    <span class="tok-variable">"framer-motion"</span><span class="tok-punct">:</span> <span class="tok-string">"^11.15.0"</span>
  <span class="tok-punct">}</span>
<span class="tok-punct">}</span></code></pre>
      </section>

      <section class="cbk-02__panel" role="tabpanel" id="cbk-02-p3" aria-labelledby="cbk-02-t3" tabindex="0" hidden>
<pre class="cbk-02__pre"><code class="language-markdown"><span class="tok-keyword"># Board</span>

Issue board UI for the Codefronts workspace.

<span class="tok-keyword">## Getting started</span>

<span class="tok-punct">&#96;&#96;&#96;</span>sh
pnpm install
pnpm dev
<span class="tok-punct">&#96;&#96;&#96;</span>

<span class="tok-comment">&gt; Maintained by Priya Sharma and Jordan Lee.</span></code></pre>
      </section>
    </div>
  </div>
</div>
```
## CSS
```css
.cbk-02 {
  inline-size: 100%;
  width: 100%;
  min-block-size: 100vh;
  min-block-size: 100svh;
  min-height: 100vh;
  display: block;
  --mono: ui-monospace,"JetBrains Mono","Geist Mono","SF Mono","IBM Plex Mono",Menlo,monospace;
  --sans: system-ui,"Inter","Geist",-apple-system,"Segoe UI",sans-serif;
  --bg: #08090e;
  --surface: #0f1118;
  --strip: #0a0c12;
  --line: #222634;
  --ink: #e8ebf3;
  --muted: #8d95a6;
  --acc: #38bdf8;
  --tok-key: #d2a8ff;
  --tok-str: #7ee787;
  --tok-fn: #79c0ff;
  --tok-var: #ffcb6b;
  --tok-num: #ff85a1;
  --tok-com: #98a2b3;
  --tok-punct: #8b96a8;
  background: radial-gradient(70rem 40rem at 50% -12%, #141a2c 0%, transparent 60%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
}

@supports (color: oklch(50% .1 200)) {
  .cbk-02 {
    --bg: oklch(12% .012 265);
    --surface: oklch(17% .014 265);
    --strip: oklch(14% .013 265);
    --line: oklch(28% .018 265);
    --ink: oklch(94% .008 265);
    --muted: oklch(68% .02 265);
    --acc: oklch(80% .13 225);
  }
}

.cbk-02 *,
.cbk-02 *::before,
.cbk-02 *::after {
  box-sizing: border-box;
}

.cbk-02__stage {
  display: grid;
  place-items: center;
  min-block-size: inherit;
  padding: clamp(1rem,4vw,3.5rem);
}

.cbk-02__block {
  inline-size: min(62rem,100%);
  border: 1px solid var(--line);
  border-radius: 14px;
  background: var(--surface);
  overflow: hidden;
  box-shadow: 0 1px 0 rgba(255,255,255,.04) inset, 0 30px 70px -34px rgba(0,0,0,.95);
  container-type: inline-size;
}

.cbk-02__strip {
  display: flex;
  gap: 0;
  min-inline-size: 0;
  overflow-x: auto;
  background: var(--strip);
  border-block-end: 1px solid var(--line);
  scroll-snap-type: inline mandatory;
  scrollbar-width: none;
}

.cbk-02__strip::-webkit-scrollbar {
  display: none;
}

.cbk-02__tabwrap {
  position: relative;
  display: flex;
  flex: none;
  scroll-snap-align: start;
}

.cbk-02__tab {
  display: inline-flex;
  align-items: center;
  gap: .5rem;
  min-block-size: 44px;
  padding: .6rem 2.2rem .6rem .95rem;
  border: 0;
  border-inline-end: 1px solid var(--line);
  background: none;
  color: var(--muted);
  font-family: var(--mono);
  font-size: .8125rem;
  cursor: pointer;
  white-space: nowrap;
  transition: color .18s, background-color .18s;
}

.cbk-02__tab::after {
  content: "";
  position: absolute;
  inset-inline: 0;
  inset-block-end: 0;
  block-size: 2px;
  background: var(--acc);
  transform: scaleX(0);
  transform-origin: left;
  transition: transform .22s cubic-bezier(.2,.9,.25,1);
}

.cbk-02__tab:hover {
  color: var(--ink);
  background: color-mix(in oklab,var(--ink) 6%,transparent);
}

.cbk-02__tab[aria-selected="true"] {
  color: var(--ink);
  background: var(--surface);
}

.cbk-02__tab[aria-selected="true"]::after {
  transform: scaleX(1);
}

.cbk-02__ext {
  inline-size: 15px;
  block-size: 15px;
  flex: none;
}

.cbk-02__ext--tsx {
  color: #79c0ff;
}

.cbk-02__ext--css {
  color: #7ee787;
}

.cbk-02__ext--json {
  color: #ffcb6b;
}

.cbk-02__ext--md {
  color: #a1a9b8;
}

.cbk-02__close {
  position: absolute;
  inset-inline-end: .4rem;
  inset-block-start: 50%;
  translate: 0 -50%;
  display: grid;
  place-items: center;
  inline-size: 26px;
  block-size: 26px;
  border: 0;
  border-radius: 6px;
  background: none;
  color: var(--muted);
  cursor: pointer;
  opacity: 0;
  transition: opacity .15s, background-color .15s;
}

.cbk-02__close svg {
  inline-size: 13px;
  block-size: 13px;
}

.cbk-02__close:hover {
  background: color-mix(in oklab,var(--ink) 14%,transparent);
  color: var(--ink);
}

.cbk-02__tabwrap:hover .cbk-02__close,
.cbk-02__close:focus-visible {
  opacity: 1;
}

@supports not selector(:has(*)) {
  .cbk-02__close {
    opacity: .6;
  }
}

.cbk-02__tabwrap:has(.cbk-02__tab[aria-selected="true"]) .cbk-02__close {
  opacity: .75;
}

.cbk-02__panel {
  outline: none;
}

.cbk-02__panel[hidden] {
  display: none;
}

.cbk-02__pre {
  margin: 0;
  padding: 1.15rem 1.25rem 1.4rem;
  overflow-x: auto;
  scrollbar-gutter: stable;
  font-family: var(--mono);
  font-size: clamp(.8125rem,.45rem + .5cqi,.9375rem);
  line-height: 1.75;
  white-space: pre;
  tab-size: 2;
  font-variant-ligatures: none;
}

.cbk-02__pre code {
  font: inherit;
}

.cbk-02 .tok-keyword {
  color: var(--tok-key);
}

.cbk-02 .tok-string {
  color: var(--tok-str);
}

.cbk-02 .tok-function {
  color: var(--tok-fn);
}

.cbk-02 .tok-variable {
  color: var(--tok-var);
}

.cbk-02 .tok-number {
  color: var(--tok-num);
}

.cbk-02 .tok-comment {
  color: var(--tok-com);
  font-style: italic;
}

.cbk-02 .tok-punct {
  color: var(--tok-punct);
}

.cbk-02 :focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
}

.cbk-02[data-theme="light"] {
  --bg: #f5f6fa;
  --surface: #ffffff;
  --strip: #eef0f6;
  --line: #e2e5ef;
  --ink: #11131a;
  --muted: #5c6373;
  --acc: #0284c7;
  --tok-key: #8250df;
  --tok-str: #0a7d3f;
  --tok-fn: #0550ae;
  --tok-var: #8a5a00;
  --tok-num: #b1265c;
  --tok-com: #5d6577;
  --tok-punct: #57606a;
  background: radial-gradient(70rem 40rem at 50% -12%, #e6ecff 0%, transparent 60%), var(--bg);
}

@media (prefers-color-scheme: light) {
  .cbk-02:not([data-theme="dark"]) {
    --bg: #f5f6fa;
    --surface: #ffffff;
    --strip: #eef0f6;
    --line: #e2e5ef;
    --ink: #11131a;
    --muted: #5c6373;
    --acc: #0284c7;
    --tok-key: #8250df;
    --tok-str: #0a7d3f;
    --tok-fn: #0550ae;
    --tok-var: #8a5a00;
    --tok-num: #b1265c;
    --tok-com: #5d6577;
    --tok-punct: #57606a;
    background: radial-gradient(70rem 40rem at 50% -12%, #e6ecff 0%, transparent 60%), var(--bg);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cbk-02 *,
    .cbk-02 *::before,
    .cbk-02 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .cbk-02__block {
    border: 2px solid CanvasText;
    background: Canvas;
  }

  .cbk-02__tab[aria-selected="true"] {
    background: Highlight;
    color: HighlightText;
  }

  .cbk-02 [class^="tok-"] {
    color: CanvasText;
  }
}
/* theme toggle — pure CSS, :has() driven; :checked = light theme, top-right of the stage */

.cbk-02__stage {
  position: relative;
}

.cbk-02__tbox {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  padding: 0;
  opacity: 0;
  pointer-events: none;
}

.cbk-02__tbtn {
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
  .cbk-02__tbtn {
    background: color-mix(in srgb, var(--ink,#e7eaf3) 10%, transparent);
    border-color: color-mix(in srgb, var(--ink,#e7eaf3) 26%, transparent);
  }
}

.cbk-02__tbtn:hover {
  transform: translateY(-1px);
}

.cbk-02__tbtn svg {
  inline-size: 1.0625rem;
  block-size: 1.0625rem;
}

.cbk-02__tbox:focus-visible + .cbk-02__tbtn {
  outline: 2px solid var(--ink,#e7eaf3);
  outline-offset: 2px;
}

.cbk-02__tmoon {
  display: none;
}

.cbk-02:has(.cbk-02__tbox:checked) .cbk-02__tsun {
  display: none;
}

.cbk-02:has(.cbk-02__tbox:checked) .cbk-02__tmoon {
  display: block;
}

@media (prefers-reduced-motion: reduce) {
  .cbk-02__tbtn {
    transition: none;
  }

  .cbk-02__tbtn:hover {
    transform: none;
  }
}

@media (forced-colors: active) {
  .cbk-02__tbtn {
    border: 1px solid ButtonBorder;
    color: ButtonText;
    background: ButtonFace;
  }
}

.cbk-02:has(.cbk-02__tbox:checked) {
  --bg: #f5f6fa;
  --surface: #ffffff;
  --strip: #eef0f6;
  --line: #e2e5ef;
  --ink: #11131a;
  --muted: #5c6373;
  --acc: #0284c7;
  --tok-key: #8250df;
  --tok-str: #0a7d3f;
  --tok-fn: #0550ae;
  --tok-var: #8a5a00;
  --tok-num: #b1265c;
  --tok-com: #5d6577;
  --tok-punct: #57606a;
  background: radial-gradient(70rem 40rem at 50% -12%, #e6ecff 0%, transparent 60%), var(--bg);
}

.cbk-02__theme {
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

.cbk-02[data-theme="dark"] .cbk-02__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .cbk-02:not([data-theme="light"]) .cbk-02__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.cbk-02__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.cbk-02[data-theme="dark"] .cbk-02__theme:hover,
.cbk-02:not([data-theme="light"]) .cbk-02__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.cbk-02__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.cbk-02__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.cbk-02__sun {
  display: none;
}

.cbk-02__theme[aria-pressed="true"] .cbk-02__sun {
  display: block;
}

.cbk-02__theme[aria-pressed="true"] .cbk-02__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .cbk-02__theme {
    transition: none;
  }

  .cbk-02__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(() => {
  const block = document.getElementById('cbk-02-block');
  if (!block) return;
  const tabs = [...block.querySelectorAll('[role="tab"]')];
  const panels = tabs.map((t) => document.getElementById(t.getAttribute('aria-controls')));

  const select = (i, focus) => {
    tabs.forEach((t, n) => {
      t.setAttribute('aria-selected', String(n === i));
      t.tabIndex = n === i ? 0 : -1;
      if (panels[n]) panels[n].hidden = n !== i;
    });
    if (focus) tabs[i].focus();
  };

  tabs.forEach((t, i) => t.addEventListener('click', () => select(i, false)));

  block.querySelector('[role="tablist"]').addEventListener('keydown', (e) => {
    const i = tabs.indexOf(document.activeElement);
    if (i < 0) return;
    const map = { ArrowRight: i + 1, ArrowLeft: i - 1, Home: 0, End: tabs.length - 1 };
    if (!(e.key in map)) return;
    e.preventDefault();
    select((map[e.key] + tabs.length) % tabs.length, true);
  });
})();
(()=>{const r=document.querySelector('.cbk-02');if(!r)return;const t=r.querySelector('.cbk-02__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
