---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-dark-mode-ui/dark-mode-code-editor-surface-with-syntax-layer/"
title: "Dark Mode Code Editor Surface with Syntax Layer"
section: "design-styles"
category: "css-dark-mode-ui"
category_name: "CSS Dark Mode UI"
description: "An editor chrome — file tree, tab bar with a modified dot, gutter, code panel and status bar — where the syntax palette is a token set rather than a…"
has_js: "false"
---

Here's a working CSS Dark Mode UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dark Mode Code Editor Surface with Syntax Layer
Source: https://codefronts.com/design-styles/css-dark-mode-ui/dark-mode-code-editor-surface-with-syntax-layer/

An editor chrome — file tree, tab bar with a modified dot, gutter, code panel and status bar — where the syntax palette is a token set rather than a stylesheet per theme. Keyword, string, comment, function and number colours each own a variable, so the same highlighted markup reads correctly on a near-black editor surface or a paper-white one. Theme toggle sits bottom-right in the status bar, exactly where an editor puts it.
## HTML
```html
<div class="dmu-10">
  <div class="dmu-10__stage">
    <div class="dmu-10__editor">
      <div class="dmu-10__chrome">
        <aside class="dmu-10__tree" aria-label="Files">
          <p class="dmu-10__treeTitle">meridian-web</p>
          <ul class="dmu-10__files">
            <li><button class="dmu-10__file" type="button">
              <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M3.5 6.5h6l1.6 2h9.4v9.5H3.5Z"/></svg>
              app</button></li>
            <li><button class="dmu-10__file dmu-10__file--active" type="button" aria-current="true">
              <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M6.5 3.5h7l4.5 4.5v12h-11.5Z"/><path d="M13.5 3.5V8H18"/></svg>
              theme.css</button></li>
            <li><button class="dmu-10__file" type="button">
              <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M6.5 3.5h7l4.5 4.5v12h-11.5Z"/><path d="M13.5 3.5V8H18"/></svg>
              App.tsx</button></li>
            <li><button class="dmu-10__file" type="button">
              <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M6.5 3.5h7l4.5 4.5v12h-11.5Z"/><path d="M13.5 3.5V8H18"/></svg>
              next.config.mjs</button></li>
            <li><button class="dmu-10__file" type="button">
              <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M6.5 3.5h7l4.5 4.5v12h-11.5Z"/><path d="M13.5 3.5V8H18"/></svg>
              package.json</button></li>
          </ul>
        </aside>

        <div class="dmu-10__main">
          <div class="dmu-10__tabs" role="tablist" aria-label="Open files">
            <button class="dmu-10__tab dmu-10__tab--active" type="button" role="tab" aria-selected="true">
              theme.css <span class="dmu-10__mod" title="Unsaved changes" aria-hidden="true"></span>
            </button>
            <button class="dmu-10__tab" type="button" role="tab" aria-selected="false">App.tsx</button>
            <button class="dmu-10__tab" type="button" role="tab" aria-selected="false">next.config.mjs</button>
          </div>

          <div class="dmu-10__code">
            <div class="dmu-10__gutter" aria-hidden="true"><span>1</span><span>2</span><span>3</span><span>4</span><span>5</span><span>6</span><span>7</span><span>8</span><span>9</span><span>10</span><span>11</span><span>12</span><span>13</span><span>14</span></div>
            <pre class="dmu-10__pre"><code><span class="dmu-10__line"><span class="tok-comment">/* semantic tokens — one source of truth */</span></span>
<span class="dmu-10__line"><span class="tok-keyword">:root</span> <span class="tok-punct">{</span></span>
<span class="dmu-10__line">  <span class="tok-prop">--surface</span><span class="tok-punct">:</span> <span class="tok-fn">light-dark</span><span class="tok-punct">(</span><span class="tok-num">#ffffff</span><span class="tok-punct">,</span> <span class="tok-num">#0d1017</span><span class="tok-punct">);</span></span>
<span class="dmu-10__line">  <span class="tok-prop">--ink</span><span class="tok-punct">:</span>     <span class="tok-fn">light-dark</span><span class="tok-punct">(</span><span class="tok-num">#0d1017</span><span class="tok-punct">,</span> <span class="tok-num">#e8ecf4</span><span class="tok-punct">);</span></span>
<span class="dmu-10__line">  <span class="tok-prop">--accent</span><span class="tok-punct">:</span>  <span class="tok-fn">light-dark</span><span class="tok-punct">(</span><span class="tok-num">#1d4ed8</span><span class="tok-punct">,</span> <span class="tok-num">#82aaff</span><span class="tok-punct">);</span></span>
<span class="dmu-10__line"><span class="tok-punct">}</span></span>
<span class="dmu-10__line"></span>
<span class="dmu-10__line dmu-10__line--active"><span class="tok-keyword">@supports</span> <span class="tok-punct">(</span><span class="tok-prop">color-scheme</span><span class="tok-punct">:</span> <span class="tok-string">light dark</span><span class="tok-punct">)</span> <span class="tok-punct">{</span></span>
<span class="dmu-10__line">  <span class="tok-keyword">.editor</span> <span class="tok-punct">{</span> <span class="tok-prop">color-scheme</span><span class="tok-punct">:</span> <span class="tok-string">light dark</span><span class="tok-punct">;</span> <span class="tok-punct">}</span></span>
<span class="dmu-10__line"><span class="tok-punct">}</span></span>
<span class="dmu-10__line"></span>
<span class="dmu-10__line"><span class="tok-comment">/* syntax layer inherits the same variables */</span></span>
<span class="dmu-10__line"><span class="tok-keyword">.tok-string</span> <span class="tok-punct">{</span> <span class="tok-prop">color</span><span class="tok-punct">:</span> <span class="tok-fn">var</span><span class="tok-punct">(</span><span class="tok-prop">--tok-string</span><span class="tok-punct">);</span> <span class="tok-punct">}</span></span>
<span class="dmu-10__line"><span class="tok-keyword">.tok-comment</span> <span class="tok-punct">{</span> <span class="tok-prop">color</span><span class="tok-punct">:</span> <span class="tok-fn">var</span><span class="tok-punct">(</span><span class="tok-prop">--tok-comment</span><span class="tok-punct">);</span> <span class="tok-punct">}</span></span></code></pre>
          </div>

          <div class="dmu-10__status">
            <span class="dmu-10__statusItem">
              <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M6.5 4.5v9a3 3 0 0 0 3 3h8"/><circle cx="6.5" cy="17.5" r="2.2"/><circle cx="17.5" cy="16.5" r="2.2"/></svg>
              main</span>
            <span class="dmu-10__statusItem">Ln 8, Col 24</span>
            <span class="dmu-10__statusItem">Spaces: 2</span>
            <span class="dmu-10__statusItem">CSS</span>
            <span class="dmu-10__statusSpacer"></span>
            <input class="dmu-10__sr" type="checkbox" id="dmu-10-toggle">
            <label class="dmu-10__toggle" for="dmu-10-toggle">
              <svg class="dmu-10__sun" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"><circle cx="12" cy="12" r="4"/><path d="M12 2.8v2M12 19.2v2M2.8 12h2M19.2 12h2M5.5 5.5 7 7M17 17l1.5 1.5M18.5 5.5 17 7M7 17l-1.5 1.5"/></svg>
              <svg class="dmu-10__moon" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M20 14.4A8.4 8.4 0 0 1 9.6 4a8.4 8.4 0 1 0 10.4 10.4Z"/></svg>
              <span class="dmu-10__toggleText">Theme</span>
            </label>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.dmu-10 {
  --bg: #06070a;
  --chrome: #0d1017;
  --panel: #0a0c12;
  --tree: #0b0e14;
  --ink: #e8ecf4;
  --muted: #8892a6;
  --line: #1c212c;
  --active-line: rgba(130,170,255,.07);
  --accent: #82aaff;
  --accent-ink: #050a17;
  --status: #0b0e14;
  --caret: #82aaff;
  --shadow: rgba(0,0,0,.8);
  --tok-keyword: #c792ea;
  --tok-string: #a5e075;
  --tok-comment: #6f7d94;
  --tok-fn: #82aaff;
  --tok-num: #f78c6c;
  --tok-prop: #7fdbca;
  --tok-punct: #8891a5;
  --sans: system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "JetBrains Mono",ui-monospace,"SF Mono",Menlo,Consolas,monospace;
  color-scheme: dark;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.dmu-10[data-theme="light"],
.dmu-10:has(#dmu-10-toggle:checked) {
  --bg: #eceef3;
  --chrome: #ffffff;
  --panel: #fbfbfd;
  --tree: #f5f6f9;
  --ink: #0d1017;
  --muted: #5a6272;
  --line: #e2e5ec;
  --active-line: rgba(29,78,216,.07);
  --accent: #1d4ed8;
  --accent-ink: #ffffff;
  --status: #f2f3f7;
  --caret: #1d4ed8;
  --shadow: rgba(13,16,23,.18);
  --tok-keyword: #7c3aed;
  --tok-string: #15803d;
  --tok-comment: #5f6b7f;
  --tok-fn: #1d4ed8;
  --tok-num: #b45309;
  --tok-prop: #0f766e;
  --tok-punct: #5a6272;
  color-scheme: light;
}

@media (prefers-color-scheme: light) {
  .dmu-10:not([data-theme="dark"]):not(:has(#dmu-10-toggle:checked)) {
    --bg: #eceef3;
    --chrome: #ffffff;
    --panel: #fbfbfd;
    --tree: #f5f6f9;
    --ink: #0d1017;
    --muted: #5a6272;
    --line: #e2e5ec;
    --active-line: rgba(29,78,216,.07);
    --accent: #1d4ed8;
    --accent-ink: #ffffff;
    --status: #f2f3f7;
    --caret: #1d4ed8;
    --shadow: rgba(13,16,23,.18);
    --tok-keyword: #7c3aed;
    --tok-string: #15803d;
    --tok-comment: #5f6b7f;
    --tok-fn: #1d4ed8;
    --tok-num: #b45309;
    --tok-prop: #0f766e;
    --tok-punct: #5a6272;
    color-scheme: light;
  }
  /* flip-back: light OS + checked restores the dark editor palette */

  .dmu-10:has(#dmu-10-toggle:checked) {
    --bg: #06070a;
    --chrome: #0d1017;
    --panel: #0a0c12;
    --tree: #0b0e14;
    --ink: #e8ecf4;
    --muted: #8892a6;
    --line: #1c212c;
    --active-line: rgba(130,170,255,.07);
    --accent: #82aaff;
    --accent-ink: #050a17;
    --status: #0b0e14;
    --caret: #82aaff;
    --shadow: rgba(0,0,0,.8);
    --tok-keyword: #c792ea;
    --tok-string: #a5e075;
    --tok-comment: #6f7d94;
    --tok-fn: #82aaff;
    --tok-num: #f78c6c;
    --tok-prop: #7fdbca;
    --tok-punct: #8891a5;
    color-scheme: dark;
  }
}

.dmu-10,
.dmu-10 *,
.dmu-10 *::before,
.dmu-10 *::after {
  box-sizing: border-box;
}

.dmu-10__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.dmu-10__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(.75rem,3.5vw,3rem);
}

.dmu-10__editor {
  width: min(72rem,100%);
  border-radius: .9rem;
  overflow: hidden;
  background: var(--chrome);
  border: 1px solid var(--line);
  box-shadow: 0 40px 80px -50px var(--shadow);
}

.dmu-10__chrome {
  display: grid;
  grid-template-columns: 1fr;
}

@media (min-width: 48rem) {
  .dmu-10__chrome {
    grid-template-columns: 13.5rem 1fr;
  }
}

.dmu-10__tree {
  padding: .75rem .6rem;
  background: var(--tree);
  border-bottom: 1px solid var(--line);
}

@media (min-width: 48rem) {
  .dmu-10__tree {
    border-bottom: 0;
    border-right: 1px solid var(--line);
  }
}

.dmu-10__treeTitle {
  margin: .15rem .45rem .55rem;
  font-size: .7rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.dmu-10__files {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: .1rem;
}

.dmu-10__file {
  display: flex;
  align-items: center;
  gap: .45rem;
  width: 100%;
  min-height: 2.1rem;
  padding: 0 .5rem;
  border: 0;
  border-radius: .4rem;
  cursor: pointer;
  font: inherit;
  font-size: .8rem;
  text-align: left;
  background: transparent;
  color: var(--muted);
  transition: background-color .16s ease, color .16s ease;
}

.dmu-10__file svg {
  width: 1rem;
  height: 1rem;
  flex: none;
}

.dmu-10__file:hover {
  background: var(--active-line);
  color: var(--ink);
}

.dmu-10__file:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: -2px;
}

.dmu-10__file--active {
  background: var(--active-line);
  color: var(--ink);
}

.dmu-10__file--active svg {
  color: var(--accent);
}

.dmu-10__main {
  display: grid;
  grid-template-rows: auto 1fr auto;
  min-width: 0;
  background: var(--panel);
}

.dmu-10__tabs {
  display: flex;
  gap: .15rem;
  padding: .4rem .5rem 0;
  background: var(--chrome);
  border-bottom: 1px solid var(--line);
  overflow: auto;
}

.dmu-10__tab {
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  min-height: 2.35rem;
  padding: 0 .8rem;
  white-space: nowrap;
  border: 1px solid transparent;
  border-bottom: 0;
  border-radius: .45rem .45rem 0 0;
  cursor: pointer;
  font: inherit;
  font-size: .78rem;
  font-family: var(--mono);
  background: transparent;
  color: var(--muted);
  transition: background-color .16s ease, color .16s ease;
}

.dmu-10__tab:hover {
  color: var(--ink);
  background: var(--active-line);
}

.dmu-10__tab:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: -2px;
}

.dmu-10__tab--active {
  background: var(--panel);
  color: var(--ink);
  border-color: var(--line);
}

.dmu-10__mod {
  width: .45rem;
  height: .45rem;
  border-radius: 50%;
  background: var(--accent);
}

.dmu-10__code {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: 0;
  min-height: min(26rem,58vh);
  overflow: auto;
  background: var(--panel);
}

.dmu-10__gutter {
  display: grid;
  padding: .9rem .55rem .9rem .8rem;
  text-align: right;
  border-right: 1px solid var(--line);
  font-family: var(--mono);
  font-size: .76rem;
  line-height: 1.7;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
  user-select: none;
  opacity: .8;
}

.dmu-10__pre {
  margin: 0;
  padding: .9rem 1rem;
  overflow-x: auto;
  tab-size: 2;
  font-family: var(--mono);
  font-size: .79rem;
  line-height: 1.7;
  color: var(--ink);
}

.dmu-10__line {
  display: block;
  position: relative;
}

.dmu-10__line--active {
  background: var(--active-line);
  box-shadow: -1rem 0 0 var(--active-line), 1rem 0 0 var(--active-line);
}

.dmu-10__line--active::after {
  content: '';
  position: absolute;
  top: .1em;
  right: -.1rem;
  width: 2px;
  height: 1.2em;
  background: var(--caret);
  animation: dmu-10-caret 1.1s steps(1,end) infinite;
}

@keyframes dmu-10-caret {
  0%,
    49% {
    opacity: 1;
  }

  50%,
    100% {
    opacity: 0;
  }
}

.dmu-10 .tok-keyword {
  color: var(--tok-keyword);
}

.dmu-10 .tok-string {
  color: var(--tok-string);
}

.dmu-10 .tok-comment {
  color: var(--tok-comment);
  font-style: italic;
}

.dmu-10 .tok-fn {
  color: var(--tok-fn);
}

.dmu-10 .tok-num {
  color: var(--tok-num);
}

.dmu-10 .tok-prop {
  color: var(--tok-prop);
}

.dmu-10 .tok-punct {
  color: var(--tok-punct);
}

.dmu-10__status {
  display: flex;
  align-items: center;
  gap: .9rem;
  flex-wrap: wrap;
  padding: .35rem .7rem;
  background: var(--status);
  border-top: 1px solid var(--line);
}

.dmu-10__statusItem {
  display: inline-flex;
  align-items: center;
  gap: .3rem;
  font-family: var(--mono);
  font-size: .7rem;
  color: var(--muted);
}

.dmu-10__statusItem svg {
  width: .85rem;
  height: .85rem;
}

.dmu-10__statusSpacer {
  flex: 1;
}

.dmu-10__toggle {
  display: inline-flex;
  align-items: center;
  gap: .35rem;
  min-height: 1.9rem;
  padding: 0 .5rem;
  border-radius: .4rem;
  cursor: pointer;
  color: var(--muted);
  font-size: .72rem;
  font-family: var(--mono);
  transition: background-color .16s ease, color .16s ease;
}

.dmu-10__toggle:hover {
  background: var(--active-line);
  color: var(--ink);
}

.dmu-10__toggle svg {
  width: .9rem;
  height: .9rem;
}

.dmu-10__sun {
  display: none;
}

.dmu-10__moon {
  display: block;
}

.dmu-10:has(#dmu-10-toggle:checked) .dmu-10__sun {
  display: block;
}

.dmu-10:has(#dmu-10-toggle:checked) .dmu-10__moon {
  display: none;
}

@media (prefers-color-scheme: light) {
  .dmu-10:not(:has(#dmu-10-toggle:checked)) .dmu-10__sun {
    display: block;
  }

  .dmu-10:not(:has(#dmu-10-toggle:checked)) .dmu-10__moon {
    display: none;
  }

  .dmu-10:has(#dmu-10-toggle:checked) .dmu-10__sun {
    display: none;
  }

  .dmu-10:has(#dmu-10-toggle:checked) .dmu-10__moon {
    display: block;
  }
}

.dmu-10:has(#dmu-10-toggle:focus-visible) .dmu-10__toggle {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
  color: var(--ink);
}

@media (prefers-reduced-motion: reduce) {
  .dmu-10__line--active::after {
    animation: none;
  }

  .dmu-10__file,
    .dmu-10__tab,
    .dmu-10__toggle {
    transition: none;
  }
}

@media (forced-colors: active) {
  .dmu-10__editor,
    .dmu-10__tab--active {
    border-color: CanvasText;
    box-shadow: none;
  }

  .dmu-10 .tok-keyword,
    .dmu-10 .tok-string,
    .dmu-10 .tok-fn,
    .dmu-10 .tok-num,
    .dmu-10 .tok-prop,
    .dmu-10 .tok-comment,
    .dmu-10 .tok-punct {
    color: CanvasText;
  }

  .dmu-10__line--active {
    background: Highlight;
    box-shadow: none;
  }
}
```
