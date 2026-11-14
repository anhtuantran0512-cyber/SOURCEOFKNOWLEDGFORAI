---
source: "codefronts"
url: "https://codefronts.com/snippets/css-code-blocks/split-pane-code-live-preview-container/"
title: "Split-Pane CSS Code Block with Live Preview"
section: "snippets"
category: "css-code-blocks"
category_name: "CSS Code Blocks"
description: "Code on the left, the thing it renders on the right — and the divider is genuinely draggable with zero JavaScript, using the CSS resize property on the code…"
has_js: "true"
---

Here's a working CSS Code Block from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Split-Pane CSS Code Block with Live Preview
Source: https://codefronts.com/snippets/css-code-blocks/split-pane-code-live-preview-container/

Code on the left, the thing it renders on the right — and the divider is genuinely draggable with zero JavaScript, using the CSS resize property on the code pane. A container query stacks the panes when the block gets narrow, so the same component works in a wide tutorial and a phone. The preview is a real card built from the code beside it, photo included.
## HTML
```html
<div class="cbk-18">
  <button class="cbk-18__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="cbk-18__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="cbk-18__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <div class="cbk-18__stage">
    <input class="cbk-18__tbox" id="cbk-18-tbox" type="checkbox" data-alt="light" aria-label="Toggle light and dark theme">
    <label class="cbk-18__tbtn" for="cbk-18-tbox" title="Toggle light and dark theme">
      <svg class="cbk-18__tsun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4.2"></circle><path d="M12 2.4v2.3M12 19.3v2.3M2.4 12h2.3M19.3 12h2.3M5.2 5.2l1.6 1.6M17.2 17.2l1.6 1.6M18.8 5.2l-1.6 1.6M6.8 17.2l-1.6 1.6"></path></svg>
      <svg class="cbk-18__tmoon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.2 14.6A8.6 8.6 0 0 1 9.4 3.8a8.6 8.6 0 1 0 10.8 10.8Z"></path></svg>
    </label>
    <div class="cbk-18__block">
      <div class="cbk-18__split">
        <div class="cbk-18__code" role="region" aria-label="Source code">
          <p class="cbk-18__tag">ArticleCard.tsx</p>
<pre class="cbk-18__pre"><code class="language-tsx"><span class="tok-keyword">export function</span> <span class="tok-function">ArticleCard</span><span class="tok-punct">({</span> <span class="tok-variable">post</span> <span class="tok-punct">}) {</span>
  <span class="tok-keyword">return</span> <span class="tok-punct">(</span>
    <span class="tok-punct">&lt;</span><span class="tok-fn2">article</span> <span class="tok-variable">className</span><span class="tok-punct">=</span><span class="tok-string">"card"</span><span class="tok-punct">&gt;</span>
      <span class="tok-punct">&lt;</span><span class="tok-fn2">img</span> <span class="tok-variable">src</span><span class="tok-punct">={</span><span class="tok-variable">post</span><span class="tok-punct">.</span><span class="tok-variable">cover</span><span class="tok-punct">}</span> <span class="tok-variable">alt</span><span class="tok-punct">=</span><span class="tok-string">""</span> <span class="tok-punct">/&gt;</span>
      <span class="tok-punct">&lt;</span><span class="tok-fn2">span</span> <span class="tok-variable">className</span><span class="tok-punct">=</span><span class="tok-string">"pill"</span><span class="tok-punct">&gt;{</span><span class="tok-variable">post</span><span class="tok-punct">.</span><span class="tok-variable">topic</span><span class="tok-punct">}&lt;/</span><span class="tok-fn2">span</span><span class="tok-punct">&gt;</span>
      <span class="tok-punct">&lt;</span><span class="tok-fn2">h3</span><span class="tok-punct">&gt;{</span><span class="tok-variable">post</span><span class="tok-punct">.</span><span class="tok-variable">title</span><span class="tok-punct">}&lt;/</span><span class="tok-fn2">h3</span><span class="tok-punct">&gt;</span>
      <span class="tok-punct">&lt;</span><span class="tok-fn2">footer</span><span class="tok-punct">&gt;</span>
        <span class="tok-punct">{</span><span class="tok-variable">post</span><span class="tok-punct">.</span><span class="tok-variable">author</span><span class="tok-punct">} · {</span><span class="tok-variable">post</span><span class="tok-punct">.</span><span class="tok-variable">readingTime</span><span class="tok-punct">}</span>
      <span class="tok-punct">&lt;/</span><span class="tok-fn2">footer</span><span class="tok-punct">&gt;</span>
    <span class="tok-punct">&lt;/</span><span class="tok-fn2">article</span><span class="tok-punct">&gt;</span>
  <span class="tok-punct">);</span>
<span class="tok-punct">}</span></code></pre>
        </div>

        <div class="cbk-18__preview" role="region" aria-label="Preview">
          <p class="cbk-18__tag cbk-18__tag--pv">Preview</p>
          <article class="cbk-18__card">
            <img class="cbk-18__cover" src="https://picsum.photos/seed/codefronts-cards/640/360" width="640" height="360" alt="" loading="lazy" decoding="async">
            <span class="cbk-18__pill">CSS</span>
            <h3 class="cbk-18__title">Container queries changed how we build cards</h3>
            <footer class="cbk-18__by">Priya Sharma &middot; 6 min read</footer>
          </article>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.cbk-18 {
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
  --pane: #0b0e14;
  --line: #212634;
  --ink: #e7eaf3;
  --muted: #8e96a7;
  --acc: #818cf8;
  --card: #141821;
  --tok-key: #d2a8ff;
  --tok-str: #7ee787;
  --tok-fn: #79c0ff;
  --tok-var: #ffcb6b;
  --tok-num: #ff85a1;
  --tok-punct: #8b96a8;
  --tok-fn2: #5eead4;
  background: radial-gradient(62rem 34rem at 50% -10%, #151830 0%, transparent 62%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
}

@supports (color: oklch(50% .1 200)) {
  .cbk-18 {
    --bg: oklch(12% .012 275);
    --surface: oklch(16.5% .014 275);
    --pane: oklch(14% .013 275);
    --line: oklch(27% .018 275);
    --ink: oklch(93% .008 275);
    --muted: oklch(69% .02 275);
    --acc: oklch(74% .14 285);
    --card: oklch(20% .017 275);
  }
}

.cbk-18 *,
.cbk-18 *::before,
.cbk-18 *::after {
  box-sizing: border-box;
}

.cbk-18__stage {
  display: grid;
  place-items: center;
  min-block-size: inherit;
  padding: clamp(1rem,4vw,3.5rem);
}

.cbk-18__block {
  inline-size: min(70rem,100%);
  border: 1px solid var(--line);
  border-radius: 16px;
  background: var(--surface);
  overflow: hidden;
  container-type: inline-size;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.04), 0 26px 62px -32px rgba(0,0,0,.92);
}

.cbk-18__split {
  display: grid;
  grid-template-columns: auto 1fr;
  align-items: stretch;
}

.cbk-18__code {
  resize: horizontal;
  overflow: auto;
  inline-size: 52%;
  min-inline-size: 15rem;
  max-inline-size: 78%;
  background: var(--pane);
  border-inline-end: 1px solid var(--line);
  position: relative;
  scrollbar-width: thin;
  scrollbar-color: var(--line) transparent;
}

.cbk-18__code::after {
  content: "";
  position: absolute;
  inset-block: calc(50% - 14px) auto;
  inset-inline-end: 3px;
  block-size: 28px;
  inline-size: 3px;
  border-radius: 2px;
  pointer-events: none;
  background: repeating-linear-gradient(180deg, var(--muted) 0 3px, transparent 3px 6px);
  opacity: .5;
}

.cbk-18__tag {
  margin: 0;
  padding: .6rem .9rem;
  border-block-end: 1px solid var(--line);
  color: var(--muted);
  font-family: var(--mono);
  font-size: .71875rem;
  letter-spacing: .08em;
  text-transform: uppercase;
}

.cbk-18__tag--pv {
  color: var(--acc);
}

.cbk-18__pre {
  margin: 0;
  padding: 1rem 1.1rem 1.2rem;
  font-family: var(--mono);
  font-size: clamp(.75rem,.42rem + .42cqi,.875rem);
  line-height: 1.75;
  white-space: pre;
  tab-size: 2;
  font-variant-ligatures: none;
}

.cbk-18__pre code {
  font: inherit;
}

.cbk-18__preview {
  display: flex;
  flex-direction: column;
  min-inline-size: 0;
}

.cbk-18__card {
  margin: clamp(1rem,3cqi,1.75rem);
  border: 1px solid var(--line);
  border-radius: 14px;
  background: var(--card);
  overflow: hidden;
  box-shadow: 0 14px 34px -22px rgba(0,0,0,.85);
}

.cbk-18__cover {
  display: block;
  inline-size: 100%;
  block-size: auto;
  aspect-ratio: 16/9;
  object-fit: cover;
  background: #1b2030;
}

.cbk-18__pill {
  display: inline-block;
  margin: .9rem 1rem 0;
  padding: .16rem .5rem;
  border-radius: 999px;
  background: color-mix(in oklab,var(--acc) 18%,transparent);
  color: var(--acc);
  font-family: var(--mono);
  font-size: .6875rem;
  letter-spacing: .06em;
}

.cbk-18__title {
  margin: .55rem 1rem .4rem;
  font-size: clamp(1rem,.8rem + .5cqi,1.125rem);
  line-height: 1.35;
  font-weight: 600;
  letter-spacing: -.01em;
  text-wrap: pretty;
  color: var(--ink);
}

.cbk-18__by {
  margin: 0 1rem 1rem;
  color: var(--muted);
  font-size: .8125rem;
}

.cbk-18 .tok-keyword {
  color: var(--tok-key);
}

.cbk-18 .tok-string {
  color: var(--tok-str);
}

.cbk-18 .tok-function {
  color: var(--tok-fn);
}

.cbk-18 .tok-variable {
  color: var(--tok-var);
}

.cbk-18 .tok-number {
  color: var(--tok-num);
}

.cbk-18 .tok-punct {
  color: var(--tok-punct);
}

.cbk-18 .tok-fn2 {
  color: var(--tok-fn2);
}

.cbk-18 :focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
}

@container (max-width: 46rem) {
  .cbk-18__split {
    grid-template-columns: 1fr;
  }

  .cbk-18__code {
    resize: none;
    inline-size: auto;
    max-inline-size: none;
    min-inline-size: 0;
    border-inline-end: 0;
    border-block-end: 1px solid var(--line);
  }

  .cbk-18__code::after {
    display: none;
  }
}

.cbk-18[data-theme="light"] {
  --bg: #f6f7fc;
  --surface: #ffffff;
  --pane: #f7f8fd;
  --line: #e3e6f1;
  --ink: #11131a;
  --muted: #5b6373;
  --acc: #5b5bd6;
  --card: #ffffff;
  --tok-key: #8250df;
  --tok-str: #0a7d3f;
  --tok-fn: #0550ae;
  --tok-var: #8a5a00;
  --tok-num: #b1265c;
  --tok-punct: #57606a;
  --tok-fn2: #0f766e;
  background: radial-gradient(62rem 34rem at 50% -10%, #e8eaff 0%, transparent 62%), var(--bg);
}

@media (prefers-color-scheme: light) {
  .cbk-18:not([data-theme="dark"]) {
    --bg: #f6f7fc;
    --surface: #ffffff;
    --pane: #f7f8fd;
    --line: #e3e6f1;
    --ink: #11131a;
    --muted: #5b6373;
    --acc: #5b5bd6;
    --card: #ffffff;
    --tok-key: #8250df;
    --tok-str: #0a7d3f;
    --tok-fn: #0550ae;
    --tok-var: #8a5a00;
    --tok-num: #b1265c;
    --tok-punct: #57606a;
    --tok-fn2: #0f766e;
    background: radial-gradient(62rem 34rem at 50% -10%, #e8eaff 0%, transparent 62%), var(--bg);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cbk-18 * {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .cbk-18__block,
    .cbk-18__card {
    border: 2px solid CanvasText;
    background: Canvas;
  }

  .cbk-18 [class^="tok-"] {
    color: CanvasText;
  }
}
/* theme toggle — pure CSS, :has() driven; :checked = light theme, top-right of the stage */

.cbk-18__stage {
  position: relative;
}

.cbk-18__tbox {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  padding: 0;
  opacity: 0;
  pointer-events: none;
}

.cbk-18__tbtn {
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
  .cbk-18__tbtn {
    background: color-mix(in srgb, var(--ink,#e7eaf3) 10%, transparent);
    border-color: color-mix(in srgb, var(--ink,#e7eaf3) 26%, transparent);
  }
}

.cbk-18__tbtn:hover {
  transform: translateY(-1px);
}

.cbk-18__tbtn svg {
  inline-size: 1.0625rem;
  block-size: 1.0625rem;
}

.cbk-18__tbox:focus-visible + .cbk-18__tbtn {
  outline: 2px solid var(--ink,#e7eaf3);
  outline-offset: 2px;
}

.cbk-18__tmoon {
  display: none;
}

.cbk-18:has(.cbk-18__tbox:checked) .cbk-18__tsun {
  display: none;
}

.cbk-18:has(.cbk-18__tbox:checked) .cbk-18__tmoon {
  display: block;
}

@media (prefers-reduced-motion: reduce) {
  .cbk-18__tbtn {
    transition: none;
  }

  .cbk-18__tbtn:hover {
    transform: none;
  }
}

@media (forced-colors: active) {
  .cbk-18__tbtn {
    border: 1px solid ButtonBorder;
    color: ButtonText;
    background: ButtonFace;
  }
}

.cbk-18:has(.cbk-18__tbox:checked) {
  --bg: #f6f7fc;
  --surface: #ffffff;
  --pane: #f7f8fd;
  --line: #e3e6f1;
  --ink: #11131a;
  --muted: #5b6373;
  --acc: #5b5bd6;
  --card: #ffffff;
  --tok-key: #8250df;
  --tok-str: #0a7d3f;
  --tok-fn: #0550ae;
  --tok-var: #8a5a00;
  --tok-num: #b1265c;
  --tok-punct: #57606a;
  --tok-fn2: #0f766e;
  background: radial-gradient(62rem 34rem at 50% -10%, #e8eaff 0%, transparent 62%), var(--bg);
}

.cbk-18__theme {
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

.cbk-18[data-theme="dark"] .cbk-18__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .cbk-18:not([data-theme="light"]) .cbk-18__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.cbk-18__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.cbk-18[data-theme="dark"] .cbk-18__theme:hover,
.cbk-18:not([data-theme="light"]) .cbk-18__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.cbk-18__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.cbk-18__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.cbk-18__sun {
  display: none;
}

.cbk-18__theme[aria-pressed="true"] .cbk-18__sun {
  display: block;
}

.cbk-18__theme[aria-pressed="true"] .cbk-18__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .cbk-18__theme {
    transition: none;
  }

  .cbk-18__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(()=>{const r=document.querySelector('.cbk-18');if(!r)return;const t=r.querySelector('.cbk-18__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
